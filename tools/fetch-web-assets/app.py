#!/usr/bin/env python3
"""Tiny local web UI for fetch_web_assets.py.

    python3 app.py            # opens http://127.0.0.1:8765 in your browser

Paste one or more URLs, choose whether to also grab every page they link to on the
same site, pick a folder, press Fetch. Runs entirely on your machine.
"""
from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
import threading
import uuid
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fetch_web_assets as fwa  # noqa: E402

PORT = int(os.environ.get("FWA_PORT", "8765"))
DEFAULT_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads", "web-assets")
JOBS: dict[str, dict] = {}


def page_folder(root: str, url: str) -> str:
    p = urlparse(url)
    return os.path.join(root, p.netloc or "site", fwa.slugify(p.path) or "home")


def run_job(job: dict, urls: list[str], all_pages: bool, folder: str) -> None:
    log = job["log"].append
    try:
        pages: list[str] = []
        for u in urls:
            if u not in pages:
                pages.append(u)
            if all_pages:
                log(f"Finding pages linked from {u} …")
                try:
                    found = [x for x in fwa.list_links(u, 30) if x.rstrip("/") != u.rstrip("/")]
                    log(f"  found {len(found)} more page(s)")
                    pages += [x for x in found if x not in pages]
                except Exception as e:  # noqa: BLE001
                    log(f"  couldn't list links: {e}")
        job["total"] = len(pages)
        for i, u in enumerate(pages, 1):
            out = page_folder(folder, u)
            log(f"[{i}/{len(pages)}] {u}")
            try:
                m = fwa.fetch_page(u, out)
                s = m["summary"]
                log(f"  ✓ {s['downloaded']} saved · {s['duplicates_skipped']} duplicates · "
                    f"{s['filtered_skipped']} filtered · {s['failures']} failed · {s['ambiguous_resolution']} ambiguous")
                for w in m["warnings"]:
                    log(f"  ⚠ {w}")
                job["results"].append({"url": u, "folder": out, **s})
            except Exception as e:  # noqa: BLE001
                log(f"  ✗ {e}")
                job["results"].append({"url": u, "folder": out, "error": str(e)})
            job["done_pages"] = i
        log(f"Done. Saved under {folder}")
    finally:
        job["done"] = True


def pick_folder() -> str:
    """Native folder chooser. macOS: AppleScript; elsewhere: Tk if available."""
    try:
        if platform.system() == "Darwin":
            r = subprocess.run(["osascript", "-e", 'POSIX path of (choose folder with prompt "Save assets to…")'],
                               capture_output=True, text=True, timeout=600)
            return r.stdout.strip()
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        path = filedialog.askdirectory(title="Save assets to…")
        root.destroy()
        return path or ""
    except Exception:  # noqa: BLE001
        return ""


def reveal(path: str) -> None:
    if not os.path.isdir(path):
        return
    cmd = {"Darwin": ["open"], "Windows": ["explorer"]}.get(platform.system(), ["xdg-open"])
    subprocess.Popen(cmd + [path])


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # keep the terminal quiet
        pass

    def _json(self, obj, code=200):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _body(self) -> dict:
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}")

    def _local_only(self) -> bool:
        # Reject cross-site requests so other web pages can't drive this server.
        origin = self.headers.get("Origin")
        if origin and urlparse(origin).netloc not in (f"127.0.0.1:{PORT}", f"localhost:{PORT}"):
            self._json({"error": "forbidden"}, 403)
            return False
        return True

    def do_GET(self):
        if self.path == "/" or self.path.startswith("/?"):
            body = PAGE.replace("__DEFAULT_FOLDER__", json.dumps(DEFAULT_FOLDER)).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path.startswith("/status/"):
            job = JOBS.get(self.path.rsplit("/", 1)[-1])
            self._json(job or {"error": "unknown job"}, 200 if job else 404)
        else:
            self._json({"error": "not found"}, 404)

    def do_POST(self):
        if not self._local_only():
            return
        data = self._body()
        if self.path == "/start":
            urls = [u.strip() for u in data.get("urls", "").split() if u.strip()]
            urls = [u if "://" in u else "https://" + u for u in urls]
            folder = os.path.abspath(os.path.expanduser(data.get("folder") or DEFAULT_FOLDER))
            if not urls:
                return self._json({"error": "Paste at least one URL."}, 400)
            jid = uuid.uuid4().hex[:8]
            JOBS[jid] = {"log": [], "results": [], "done": False, "total": len(urls), "done_pages": 0, "folder": folder}
            threading.Thread(target=run_job, args=(JOBS[jid], urls, bool(data.get("all_pages")), folder), daemon=True).start()
            self._json({"job": jid})
        elif self.path == "/pick-folder":
            self._json({"folder": pick_folder()})
        elif self.path == "/reveal":
            reveal(data.get("path", ""))
            self._json({"ok": True})
        else:
            self._json({"error": "not found"}, 404)


PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fetch Web Assets</title>
<style>
:root{--bg:#f6f6f4;--card:#fff;--ink:#1c1c1a;--muted:#6b6b66;--line:#dcdcd6;--accent:#2f5bea;--ok:#1f7a4d;--bad:#b3261e;--on-accent:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#141413;--card:#1e1e1c;--ink:#ececea;--muted:#9a9a94;--line:#34342f;--accent:#7f9cff;--ok:#5fc08c;--bad:#ff8a80;--on-accent:#10131f}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
main{max-width:640px;margin:48px auto;padding:0 16px}
h1{font-size:22px;margin:0 0 4px}p.sub{color:var(--muted);margin:0 0 24px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px}
label.t{display:block;font-weight:600;margin:0 0 6px}.field{margin-bottom:20px}
textarea,input[type=text]{width:100%;font:inherit;color:inherit;background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:10px}
textarea{min-height:110px;resize:vertical;font-family:ui-monospace,Menlo,monospace;font-size:13px}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.seg input{position:absolute;opacity:0;width:1px;height:1px}.seg input:focus-visible+label{outline:2px solid var(--accent);outline-offset:-2px}.seg label{padding:7px 18px;cursor:pointer}.seg input:checked+label{background:var(--accent);color:var(--on-accent)}
.hint{color:var(--muted);font-size:13px;margin-top:6px}
.row{display:flex;gap:8px}.row input{flex:1}
button{font:inherit;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:8px;padding:9px 14px;cursor:pointer}
button.primary{background:var(--accent);border-color:var(--accent);color:var(--on-accent);font-weight:600;width:100%;padding:12px}
button:disabled{opacity:.5;cursor:default}
#out{margin-top:20px;display:none}
progress{width:100%;height:8px;margin:4px 0 12px}
pre{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:12px;max-height:320px;overflow:auto;font-size:12.5px;white-space:pre-wrap;margin:0 0 12px}
.err{color:var(--bad)}
</style></head><body><main>
<h1>Fetch Web Assets</h1>
<p class="sub">Downloads every image and video on a page, at the largest size the site offers.</p>
<div class="card">
  <div class="field"><label class="t" for="urls">URLs</label>
    <textarea id="urls" placeholder="https://fionacohendesign.com&#10;https://example.com/case-study"></textarea>
    <div class="hint">One per line.</div></div>
  <div class="field"><span class="t" style="font-weight:600;display:block;margin-bottom:6px">Also fetch every page these link to (same site)?</span>
    <div class="seg"><input type="radio" name="all" id="no" value="0" checked><label for="no">No</label><input type="radio" name="all" id="yes" value="1"><label for="yes">Yes</label></div></div>
  <div class="field"><label class="t" for="folder">Save to</label>
    <div class="row"><input type="text" id="folder"><button type="button" id="pick">Choose…</button></div>
    <div class="hint">Each page gets its own subfolder: <code>site/page-name/</code>. Nothing is ever overwritten.</div></div>
  <button class="primary" id="go">Fetch</button>
  <div id="out"><progress id="bar" value="0" max="1"></progress><pre id="log"></pre><button type="button" id="open">Open folder</button></div>
</div></main>
<script>
const $=id=>document.getElementById(id);
const def=__DEFAULT_FOLDER__;
try{$("folder").value=localStorage.getItem("fwa-folder")||def}catch(e){$("folder").value=def}
$("pick").onclick=async()=>{ $("pick").disabled=true;
  try{const r=await (await fetch("/pick-folder",{method:"POST"})).json(); if(r.folder) $("folder").value=r.folder;}
  finally{$("pick").disabled=false} };
$("open").onclick=()=>fetch("/reveal",{method:"POST",body:JSON.stringify({path:$("folder").value})});
$("go").onclick=async()=>{
  const body={urls:$("urls").value,all_pages:document.querySelector("input[name=all]:checked").value==="1",folder:$("folder").value};
  try{localStorage.setItem("fwa-folder",body.folder)}catch(e){}
  $("out").style.display="block"; $("log").textContent="Starting…"; $("go").disabled=true;
  const r=await fetch("/start",{method:"POST",body:JSON.stringify(body)}); const j=await r.json();
  if(!r.ok){$("log").innerHTML='<span class="err"></span>';$("log").firstChild.textContent=j.error;$("go").disabled=false;return}
  const poll=async()=>{ const s=await (await fetch("/status/"+j.job)).json();
    $("log").textContent=s.log.join("\n"); $("log").scrollTop=1e9;
    $("bar").max=s.total||1; $("bar").value=s.done_pages;
    if(s.done){$("go").disabled=false} else setTimeout(poll,700) };
  poll();
};
</script></body></html>"""


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}/"
    print(f"Fetch Web Assets is running at {url}  (Ctrl+C to stop)")
    if "--no-browser" not in sys.argv:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
