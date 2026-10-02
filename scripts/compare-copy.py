#!/usr/bin/env python3
"""Compare the site's text between the live version and a draft.

Live  = the pages on the main branch on GitHub (what the public site shows).
Draft = the pages in this folder right now (the branch you're working on).

Writes one HTML page to drafts/ with the two versions side by side and the
differences highlighted: removed words in red on the left, added words in
green on the right. Only pages whose text changed are included. Images,
figure captions and layout are left out; this is about the copy.

Usage:  python3 scripts/compare-copy.py <name> [--base origin/main]
        e.g. python3 scripts/compare-copy.py final-case-study-copy
"""
import argparse, datetime, difflib, html, os, re, subprocess

SITE_DIR = "prototype"
LIVE_URL = "https://fcohen999.github.io/Portfolio2027/prototype/"

ap = argparse.ArgumentParser()
ap.add_argument("name", help="name for this draft, used as the file name")
ap.add_argument("--base", default="origin/main", help="git ref for the live version")
args = ap.parse_args()
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True).stdout.strip()

git("fetch", "-q", "origin")
branch = git("rev-parse", "--abbrev-ref", "HEAD")
base_sha, head_sha = git("rev-parse", "--short", args.base), git("rev-parse", "--short", "HEAD")

def blocks(src):
    """Visible copy as (tag, text) blocks, skipping figures, nav and asides."""
    if "<main" not in src:
        return []
    m = src[src.index("<main"):src.index("</main>")]
    for pat in (r"<figure.*?</figure>", r'<div class="gh">.*?</div>', r"<nav.*?</nav>", r"<aside.*?</aside>"):
        m = re.sub(pat, "", m, flags=re.S)
    # quote credits: <footer><b>Name</b><span>Title</span></footer>
    m = re.sub(r"<footer>(.*?)</footer>",
               lambda f: "<p>— " + ", ".join(re.findall(r">([^<]+)<", f.group(1))) + "</p>", m, flags=re.S)
    out = []
    for tag, body in re.findall(r"<(h1|h2|h3|p|li|dt|dd|span class=\"r-[a-z]+\")\b[^>]*>(.*?)</(?:h1|h2|h3|p|li|dt|dd|span)>", m, flags=re.S):
        t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", body))).strip()
        if t and not re.fullmatch(r"[0-9 /←Index]+", t):
            out.append((tag.split()[0], t))
    return out

def tokens(bl):
    toks = []
    for tag, t in bl:
        toks.append(f"\x00{tag}")          # block marker
        toks.extend(t.split(" "))
    return toks

def render(toks, ops, side):
    out, open_tag = [], None
    def close():
        if open_tag:
            out.append({"h1": "</h4>", "h2": "</h4>", "h3": "</h5>"}.get(open_tag, "</p>"))
    for op, i1, i2, j1, j2 in ops:
        seg = toks[i1:i2] if side == "old" else toks[j1:j2]
        mark = (side == "old" and op in ("delete", "replace")) or (side == "new" and op in ("insert", "replace"))
        words = []
        def flush():
            if words:
                txt = html.escape(" ".join(words))
                out.append((f"<del>{txt}</del> " if side == "old" else f"<ins>{txt}</ins> ") if mark else txt + " ")
                words.clear()
        for t in seg:
            if t.startswith("\x00"):
                flush(); close()
                open_tag = t[1:]
                out.append({"h1": "<h4>", "h2": "<h4>", "h3": "<h5>", "dt": '<p class="k">', "li": "<p>— "}.get(open_tag, "<p>"))
            else:
                words.append(t)
        flush()
    close()
    return "".join(out)

def merge_small(ops, n=3):
    """Fold short matching runs (a few shared words like "and the") between
    two changes into the change, so rewritten passages read as whole blocks."""
    out = []
    for op in ops:
        tag, i1, i2, j1, j2 = op
        if out and out[-1][0] != "equal" and (tag != "equal" or i2 - i1 < n):
            _, a1, _, b1, _ = out[-1]
            out[-1] = ("replace", a1, i2, b1, j2)
        else:
            out.append(op)
    # a short "equal" folded in at the very end gets split back out
    return [("replace" if t != "equal" and (i2 - i1 and j2 - j1) else ("delete" if t != "equal" and i2 - i1 else "insert" if t != "equal" else t), i1, i2, j1, j2) for t, i1, i2, j1, j2 in out]

sections, names = [], []
for f in sorted(os.listdir(SITE_DIR)):
    if not f.endswith(".html"):
        continue
    old = git("show", f"{args.base}:{SITE_DIR}/{f}")
    new = open(os.path.join(SITE_DIR, f)).read()
    ot, nt = tokens(blocks(old)), tokens(blocks(new))
    if ot == nt:
        continue
    ops = merge_small(difflib.SequenceMatcher(None, ot, nt, autojunk=False).get_opcodes())
    removed = sum(i2 - i1 for o, i1, i2, _, _ in ops if o in ("delete", "replace"))
    added = sum(j2 - j1 for o, _, _, j1, j2 in ops if o in ("insert", "replace"))
    title = re.search(r"<title>(.*?)</title>", new)
    name = "Homepage" if f == "index.html" else html.unescape(title.group(1)).split(" — ")[0] if title else f
    names.append((f, name))
    sections.append(f'''<section id="{f}"><h2>{html.escape(name)}</h2>
<p class="meta"><code>{f}</code> · about {removed} words removed, {added} words added · <a href="{LIVE_URL}{f}">open live page</a></p>
<div class="cols"><div class="col old">{render(ot, ops, "old")}</div><div class="col new">{render(nt, ops, "new")}</div></div></section>''')

today = datetime.date.today().isoformat()
doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Copy Draft: {html.escape(args.name)}</title>
<style>
:root{{--bg:#f5f5f2;--ink:#141414;--ink2:#555;--rule:#cdcdc7;--col:#fff;--del:#f6d5cc;--delink:#8a2a14;--ins:#cdeccf;--insink:#1d5c22}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#161616;--ink:#eee;--ink2:#aaa;--rule:#3a3a3a;--col:#1f1f1f;--del:#4a2219;--delink:#ffb4a2;--ins:#1e3d21;--insink:#a8e6ad}}}}
:root[data-theme="dark"]{{--bg:#161616;--ink:#eee;--ink2:#aaa;--rule:#3a3a3a;--col:#1f1f1f;--del:#4a2219;--delink:#ffb4a2;--ins:#1e3d21;--insink:#a8e6ad}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,sans-serif;padding:24px 16px}}
.wrap{{max-width:1300px;margin:0 auto}} h1{{font-size:24px;margin:0 0 12px}} a{{color:inherit}}
.where{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:0 0 16px}} .where div{{background:var(--col);border:1px solid var(--rule);padding:12px 14px;border-radius:4px}}
.where b{{display:block;font-size:13px;text-transform:uppercase;letter-spacing:.05em}} .where p{{margin:4px 0 0;color:var(--ink2)}}
.legend{{color:var(--ink2)}} nav a{{margin-right:14px}}
section{{border-top:2px solid var(--ink);margin-top:36px;padding-top:12px}} h2{{margin:0}} .meta{{color:var(--ink2);margin:2px 0 12px}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:20px}} .col{{background:var(--col);border:1px solid var(--rule);padding:6px 16px 10px;border-radius:4px;min-width:0}}
h4{{font-size:17px;margin:16px 0 6px}} h5{{font-size:15px;margin:14px 0 4px}} .col p{{margin:0 0 9px}} .k{{font-size:12px;text-transform:uppercase;color:var(--ink2);margin:10px 0 0!important}}
del{{background:var(--del);color:var(--delink);text-decoration:line-through}} ins{{background:var(--ins);color:var(--insink);text-decoration:none}}
@media (max-width:760px){{.cols,.where{{grid-template-columns:1fr}}}}
</style></head><body><div class="wrap">
<h1>Copy draft: {html.escape(args.name)}</h1>
<div class="where">
<div><b>Left — Live</b><p>What the public site shows now: the <code>main</code> branch on GitHub (commit <code>{base_sha}</code>), published at <a href="{LIVE_URL}">{LIVE_URL}</a>.</p></div>
<div><b>Right — Draft</b><p>Not published. The <code>{html.escape(branch)}</code> branch (commit <code>{head_sha}</code>). It goes live only when it's merged into <code>main</code>.</p></div>
</div>
<p class="legend"><del>Red, struck through</del> = removed from the live text. <ins>Green</ins> = new in the draft. Generated {today}. Images, captions and layout aren't compared.</p>
<nav>{"".join(f'<a href="#{f}">{html.escape(n)}</a>' for f, n in names) or "No text changes."}</nav>
{"".join(sections)}
</div></body></html>'''

os.makedirs("drafts", exist_ok=True)
path = f"drafts/{today}-{re.sub(r'[^a-z0-9]+', '-', args.name.lower()).strip('-')}.html"
open(path, "w").write(doc)
print(path, "-", len(names), "pages changed")
