#!/usr/bin/env python3
"""fetch_web_assets.py — download the meaningful visual/media assets of ONE web page.

Picks the highest-resolution real source available for each asset (srcset,
<picture>, linked originals, CDN size params), dedupes by SHA-256, and writes
asset-manifest.json + asset-manifest.md next to a files/ folder.

Usage:
    python fetch_web_assets.py URL [-o OUT_DIR]
    python fetch_web_assets.py URL --list-links      # print same-site page links, download nothing

Dependencies: requests, beautifulsoup4, Pillow (optional, for dimensions).
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import mimetypes
import os
import re
import sys
from datetime import datetime, timezone
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup

try:
    from PIL import Image

    Image.MAX_IMAGE_PIXELS = None
except ImportError:  # dimensions just become unknown
    Image = None

UA = "Mozilla/5.0 (compatible; fetch-web-assets/1.0; +read-only asset archiver)"
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif", ".svg", ".bmp", ".tif", ".tiff", ".heic"}
VIDEO_EXT = {".mp4", ".webm", ".mov", ".m4v", ".ogv"}
MEDIA_EXT = IMAGE_EXT | VIDEO_EXT
LAZY_SRC_ATTRS = ("data-src", "data-lazy-src", "data-original", "data-lazy", "data-url",
                  "data-full", "data-full-src", "data-hires", "data-zoom-src", "data-large-src")
LAZY_SRCSET_ATTRS = ("data-srcset", "data-lazy-srcset")
# Query params that only control delivered size/quality on common CDNs (Framer, Imgix,
# Cloudinary-ish, Squarespace, Shopify, Contentful, Sanity, Webflow, WordPress Photon).
SIZE_PARAMS = {"scale-down-to", "width", "w", "height", "h", "resize", "fit", "crop", "quality",
               "q", "dpr", "auto", "fm", "format", "size", "max-w", "max-h", "lossless", "strip"}
SKIP_URL_PATTERNS = re.compile(
    r"(favicon|apple-touch-icon|tracking|pixel\.gif|/pixel|spacer\.gif|blank\.gif|analytics|"
    r"google-analytics|googletagmanager|doubleclick|facebook\.com/tr|bat\.bing|hotjar|"
    r"cookie(bot|law|consent|banner)?|onetrust|gravatar|"
    r"(twitter|facebook|linkedin|instagram|dribbble|behance|github|youtube|tiktok|pinterest|x)[-_]?(icon|logo)|"
    r"social[-_]?icons?)",
    re.I,
)
CSS_URL_RE = re.compile(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)", re.I)
UGLY_NAME_RE = re.compile(r"^(?=.*\d)[A-Za-z0-9_-]{16,}$|^[0-9a-f-]{8,}$|^\d+$", re.I)


# ---------------------------------------------------------------- helpers

def slugify(text: str, maxlen: int = 50) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:maxlen].rstrip("-")


def page_slug(url: str) -> str:
    p = urlparse(url)
    return slugify(f"{p.netloc} {p.path}") or "page"


def ext_of(url: str) -> str:
    return os.path.splitext(urlparse(url).path)[1].lower()


def strip_size_params(url: str) -> str:
    p = urlparse(url)
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if k.lower() not in SIZE_PARAMS]
    path = p.path
    # WordPress-style thumbnails: name-300x200.jpg -> name.jpg ; Squarespace ?format=500w handled above
    path = re.sub(r"-\d{2,5}x\d{2,5}(?=\.[a-z0-9]{3,4}$)", "", path, flags=re.I)
    return urlunparse(p._replace(path=path, query=urlencode(q)))


def parse_srcset(value: str, base: str) -> list[tuple[str, float, str]]:
    """Return [(abs_url, numeric_descriptor, kind)] where kind is 'w', 'x' or ''."""
    out = []
    # split on commas that are followed by whitespace+url (URLs may contain commas, e.g. Cloudinary)
    for part in re.split(r",\s+(?=\S)", (value or "").strip()):
        bits = part.strip().split()
        if not bits:
            continue
        u, desc = bits[0].rstrip(","), (bits[1] if len(bits) > 1 else "")
        m = re.match(r"^([\d.]+)([wx])$", desc)
        num, kind = (float(m.group(1)), m.group(2)) if m else (0.0, "")
        if not u.startswith("data:"):
            out.append((urljoin(base, u), num, kind))
    return out


def nearby_caption(el) -> str:
    fig = el.find_parent("figure")
    if fig and fig.find("figcaption"):
        return fig.find("figcaption").get_text(" ", strip=True)[:300]
    link = el if el.name == "a" else el.find_parent("a")
    if link is not None:
        txt = link.get_text(" ", strip=True)
        if txt and len(txt) <= 300:
            return txt
    parent = el.parent
    for _ in range(2):  # only very local text; never the whole page
        if parent is None or parent.name in ("body", "html", "main", "[document]"):
            break
        txt = parent.get_text(" ", strip=True)
        if txt:
            return txt[:200] if len(txt) <= 300 else ""
        parent = parent.parent
    return ""


def link_href(el, base: str) -> str:
    if el is None:
        return ""
    link = el if el.name == "a" else el.find_parent("a")
    return urljoin(base, link["href"]) if link is not None and link.get("href") else ""


def in_site_chrome(el) -> bool:
    return any(el.find_parent(t) for t in ("header", "nav", "footer"))


def sniff_dims(data: bytes, mime: str) -> tuple[int | None, int | None]:
    if "svg" in mime or data[:5] in (b"<?xml", b"<svg ") or b"<svg" in data[:500]:
        return svg_dims(data)
    if Image is None or not mime.startswith("image"):
        return None, None
    try:
        with Image.open(io.BytesIO(data)) as im:
            return im.size
    except Exception:
        return None, None


SVG_UNITS = {"": 1, "px": 1, "in": 96, "cm": 96 / 2.54, "mm": 96 / 25.4, "pt": 4 / 3, "pc": 16}


def svg_dims(data: bytes) -> tuple[int | None, int | None]:
    """Intrinsic size of an SVG: width/height attributes (unit-converted) first, then viewBox."""
    m = re.search(rb"<svg\b[^>]*>", data[:8000], re.S)
    tag = m.group(0).decode("utf-8", "replace") if m else ""

    def attr(name):
        a = re.search(rf'\s{name}\s*=\s*["\']\s*([\d.]+)\s*([a-z]*)\s*["\']', tag)
        if a and a.group(2) in SVG_UNITS:
            return round(float(a.group(1)) * SVG_UNITS[a.group(2)])
        return None

    w, h = attr("width"), attr("height")
    if w and h:
        return w, h
    vb = re.search(r'viewBox\s*=\s*["\'][\d.\-]+[ ,]+[\d.\-]+[ ,]+([\d.]+)[ ,]+([\d.]+)', tag)
    return (round(float(vb.group(1))), round(float(vb.group(2)))) if vb else (None, None)


# ---------------------------------------------------------------- core

class Fetcher:
    def __init__(self, timeout: int):
        self.s = requests.Session()
        self.s.headers["User-Agent"] = UA
        self.timeout = timeout
        self._probe_cache: dict[str, tuple] = {}

    def get(self, url: str, **kw) -> requests.Response:
        r = self.s.get(url, timeout=self.timeout, allow_redirects=True, **kw)
        r.raise_for_status()
        return r

    def probe(self, url: str) -> tuple[int | None, int | None, int | None, str]:
        """Read just enough of an image to learn its dimensions. Returns (w, h, bytes_len, error)."""
        if url in self._probe_cache:
            return self._probe_cache[url]
        res = (None, None, None, "")
        try:
            r = self.s.get(url, timeout=self.timeout, stream=True, allow_redirects=True)
            r.raise_for_status()
            mime = r.headers.get("Content-Type", "").split(";")[0]
            clen = r.headers.get("Content-Length")
            buf = b""
            for chunk in r.iter_content(65536):
                buf += chunk
                w, h = sniff_dims(buf, mime)
                if w or len(buf) > 4_000_000:
                    break
            r.close()
            w, h = sniff_dims(buf, mime)
            res = (w, h, int(clen) if clen and clen.isdigit() else None, "")
        except Exception as e:  # noqa: BLE001
            res = (None, None, None, str(e)[:200])
        self._probe_cache[url] = res
        return res


def discover(soup: BeautifulSoup, base: str, fetcher: Fetcher, warnings: list) -> list[dict]:
    """Return ordered asset groups; each group = one logical asset with candidate URLs."""
    groups: list[dict] = []

    def add(kind, el, candidates, alt="", origin=""):
        cands = []
        seen = set()
        for c in candidates:
            if c["url"] and not c["url"].startswith(("data:", "javascript:", "blob:")) and c["url"] not in seen:
                seen.add(c["url"])
                cands.append(c)
        if not cands:
            return
        pos = (getattr(el, "sourceline", None) or 10**9, getattr(el, "sourcepos", None) or 0) if el is not None else (10**9, 0)
        groups.append({
            "pos": pos,
            "kind": kind, "origin": origin, "alt": alt or "",
            "caption": nearby_caption(el) if el is not None else "",
            "link_href": link_href(el, base),
            "chrome": in_site_chrome(el) if el is not None else False,
            "candidates": cands,
        })

    def cand(url, source, w=0.0, kind=""):
        return {"url": urljoin(base, url.strip()), "source": source, "descriptor": w, "descriptor_kind": kind}

    # <img> (incl. inside <picture>)
    for img in soup.find_all("img"):
        cs = []
        for a in ("src",) + LAZY_SRC_ATTRS:
            if img.get(a):
                cs.append(cand(img[a], a))
        for a in ("srcset",) + LAZY_SRCSET_ATTRS:
            for u, n, k in parse_srcset(img.get(a, ""), base):
                cs.append({"url": u, "source": a, "descriptor": n, "descriptor_kind": k})
        pic = img.find_parent("picture")
        if pic:
            for s in pic.find_all("source"):
                for a in ("srcset",) + LAZY_SRCSET_ATTRS:
                    for u, n, k in parse_srcset(s.get(a, ""), base):
                        cs.append({"url": u, "source": f"picture>{a}", "descriptor": n, "descriptor_kind": k})
        link = img.find_parent("a")
        if link and link.get("href") and ext_of(link["href"]) in IMAGE_EXT:
            cs.append(cand(link["href"], "linked-original"))
        add("image", img, cs, alt=img.get("alt", ""), origin="img")

    # <video> and its <source>s + poster
    for v in soup.find_all("video"):
        cs = []
        for a in ("src", "data-src"):
            if v.get(a):
                cs.append(cand(v[a], a))
        for s in v.find_all("source"):
            for a in ("src", "data-src"):
                if s.get(a):
                    cs.append(cand(s[a], f"source>{a}"))
        add("video", v, cs, origin="video")
        if v.get("poster"):
            add("image", v, [cand(v["poster"], "poster")], origin="video-poster")

    # bare image links not wrapping an <img> (e.g. "view full size")
    for a in soup.find_all("a", href=True):
        if ext_of(a["href"]) in MEDIA_EXT and not a.find("img"):
            kind = "video" if ext_of(a["href"]) in VIDEO_EXT else "image"
            add(kind, a, [cand(a["href"], "a-href")], alt=a.get_text(" ", strip=True), origin="link")

    # inline style background-image
    for el in soup.find_all(style=True):
        for u in CSS_URL_RE.findall(el["style"]):
            if ext_of(urljoin(base, u)) in IMAGE_EXT or "image" in u:
                add("image", el, [cand(u, "inline-style")], origin="css-background")

    # <style> blocks and linked stylesheets
    css_sources = [(base, st.get_text()) for st in soup.find_all("style")]
    for link in soup.find_all("link", href=True):
        rel = " ".join(link.get("rel", [])).lower()
        if "stylesheet" in rel:
            css_url = urljoin(base, link["href"])
            try:
                css_sources.append((css_url, fetcher.get(css_url).text))
            except Exception as e:  # noqa: BLE001
                warnings.append(f"stylesheet not fetched: {css_url} ({e})")
    for css_base, css in css_sources:
        css = re.sub(r"@font-face\s*{[^}]*}", "", css)
        for u in CSS_URL_RE.findall(css):
            full = urljoin(css_base, u)
            if ext_of(full) in IMAGE_EXT:
                add("image", None, [cand(full, "stylesheet")], origin="css")

    # social preview image — often the largest real export on portfolio sites
    for m in soup.find_all("meta"):
        if (m.get("property") or m.get("name") or "").lower() in ("og:image", "twitter:image") and m.get("content"):
            add("image", None, [cand(m["content"], "meta")], origin="meta-" + (m.get("property") or m.get("name")))

    groups.sort(key=lambda g: g["pos"])  # page order; stylesheet/meta assets last
    return groups


def choose_best(group: dict, fetcher: Fetcher, max_probe: int) -> dict:
    """Pick the highest-resolution real source among a group's candidates."""
    cands = group["candidates"]
    # Add CDN-original guesses (size params stripped) as extra candidates.
    for c in list(cands):
        stripped = strip_size_params(c["url"])
        if stripped != c["url"] and all(x["url"] != stripped for x in cands):
            cands.append({"url": stripped, "source": "cdn-original-guess", "descriptor": 0.0, "descriptor_kind": ""})

    if group["kind"] == "video":
        return {"selected": cands[0], "ambiguous": False, "note": "", "higher_res_found": len(cands) > 1}

    if len(cands) == 1:
        return {"selected": cands[0], "ambiguous": False, "note": "single source", "higher_res_found": False}

    # Probe real dimensions of the most promising candidates.
    def prio(c):
        order = {"linked-original": 0, "cdn-original-guess": 1}
        return (order.get(c["source"], 2), -c["descriptor"])

    for c in sorted(cands, key=prio)[:max_probe]:
        w, h, size, err = fetcher.probe(c["url"])
        c.update(width=w, height=h, bytes=size, probe_error=err or None)

    measured = [c for c in cands if c.get("width") and c.get("height")]
    if measured:
        best = max(measured, key=lambda c: (c["width"] * c["height"], c.get("bytes") or 0, c["source"] != "cdn-original-guess"))
        unmeasured_ok = [c for c in cands if "width" not in c]  # never probed
        ambiguous = bool(unmeasured_ok) and any(
            c["descriptor_kind"] == "w" and best["width"] and c["descriptor"] > best["width"] for c in unmeasured_ok)
        start = cands[0]
        return {"selected": best, "ambiguous": ambiguous,
                "note": "chosen by measured pixel area" + ("; unprobed candidate claims larger width" if ambiguous else ""),
                "higher_res_found": best["url"] != start["url"]}

    # Nothing measurable (no Pillow, SVG without viewBox, probe failures): fall back to descriptors.
    reachable = [c for c in cands if not c.get("probe_error")] or cands
    with_desc = [c for c in reachable if c["descriptor"]]
    best = max(with_desc, key=lambda c: c["descriptor"]) if with_desc else reachable[0]
    return {"selected": best, "ambiguous": True,
            "note": "dimensions not measurable; chose by srcset descriptor" if with_desc else "dimensions not measurable; chose first reachable source",
            "higher_res_found": best["url"] != cands[0]["url"]}


def is_ugly(stem: str) -> bool:
    """Hash/CDN-ID-looking names: long, no word separators, digits or mixed case."""
    if UGLY_NAME_RE.match(stem):
        return True
    return (len(stem) >= 16 and not re.search(r"[-_ .]", stem)
            and (bool(re.search(r"\d", stem)) or (stem != stem.lower() and stem != stem.upper())))


def nice_filename(url: str, mime: str, kind: str, index: int, context: str) -> str:
    path = urlparse(url).path
    stem, ext = os.path.splitext(os.path.basename(path))
    if not ext or ext.lower() not in MEDIA_EXT:
        ext = mimetypes.guess_extension(mime or "") or ext or ".bin"
        ext = {".jpe": ".jpg"}.get(ext, ext)
    raw, stem = stem, slugify(stem, 80)
    if not stem or is_ugly(raw):
        stem = f"{kind}-{index:02d}" + (f"-{slugify(context, 40)}" if slugify(context, 40) else "")
    return stem + ext.lower()


def safe_write(files_dir: str, name: str, data: bytes, digest: str) -> tuple[str, bool]:
    """Write without clobbering. Returns (filename, reused_existing_identical_file)."""
    stem, ext = os.path.splitext(name)
    n, candidate = 1, name
    while True:
        path = os.path.join(files_dir, candidate)
        if not os.path.exists(path):
            with open(path, "wb") as f:
                f.write(data)
            return candidate, False
        with open(path, "rb") as f:
            if hashlib.sha256(f.read()).hexdigest() == digest:
                return candidate, True
        n += 1
        candidate = f"{stem}-{n}{ext}"


def run(url: str, out_dir: str, timeout: int, max_probe: int, min_px: int) -> dict:
    fetcher = Fetcher(timeout)
    warnings: list[str] = []
    resp = fetcher.get(url)
    final_url = resp.url
    if final_url != url:
        warnings.append(f"page redirected to {final_url}")
    soup = BeautifulSoup(resp.content, "html.parser")  # bytes: let bs4 honour <meta charset>

    groups = discover(soup, final_url, fetcher, warnings)
    files_dir = os.path.join(out_dir, "files")
    os.makedirs(files_dir, exist_ok=True)

    assets, skipped, failures = [], [], []
    by_hash: dict[str, dict] = {}
    seen_selected: dict[str, dict] = {}
    duplicates = 0
    counters = {"image": 0, "video": 0}

    for order, g in enumerate(groups, 1):
        first_url = g["candidates"][0]["url"]
        if any(SKIP_URL_PATTERNS.search(c["url"]) for c in g["candidates"]) or SKIP_URL_PATTERNS.search(g["alt"] or ""):
            skipped.append({"order": order, "url": first_url, "reason": "matches tracking/icon/social/cookie pattern"})
            continue
        if first_url in seen_selected:  # same URL already handled earlier on the page
            seen_selected[first_url]["also_referenced_at_order"].append(order)
            duplicates += 1
            continue

        choice = choose_best(g, fetcher, max_probe)
        sel = choice["selected"]
        ordered = [sel] + [c for c in g["candidates"] if c is not sel]
        data = mime = None
        err = ""
        for c in ordered:  # fall back to next-best if the selected source fails
            try:
                r = fetcher.get(c["url"])
                data, mime = r.content, r.headers.get("Content-Type", "").split(";")[0].strip()
                if mime.startswith("text/html"):
                    raise ValueError("got HTML, not media")
                if c is not sel:
                    choice["note"] += f"; selected source failed ({err}), fell back"
                    choice["ambiguous"] = True
                sel = c
                break
            except Exception as e:  # noqa: BLE001
                err = str(e)[:200]
                data = None
        if data is None:
            fail = {"order": order, "url": sel["url"], "error": err, "also_referenced_at_order": []}
            failures.append(fail)
            for c in g["candidates"]:
                seen_selected.setdefault(c["url"], fail)  # later references count as duplicates
            continue
        if mime and not (mime.startswith(("image/", "video/")) or mime in ("application/octet-stream", "binary/octet-stream")):
            skipped.append({"order": order, "url": sel["url"], "reason": f"unsupported type {mime}"})
            continue
        mime = mime if mime and "octet-stream" not in mime else (mimetypes.guess_type(sel["url"])[0] or mime)

        w, h = sniff_dims(data, mime or "")
        if w and h and (w <= min_px and h <= min_px) and not ("svg" in (mime or "") and w <= 1 and h <= 1):
            skipped.append({"order": order, "url": sel["url"], "reason": f"tiny ({w}x{h})"})
            continue
        if g["chrome"] and (("svg" in (mime or "")) or (w and h and max(w, h) <= 128)):
            skipped.append({"order": order, "url": sel["url"], "reason": "small asset in header/nav/footer"})
            continue

        digest = hashlib.sha256(data).hexdigest()
        all_urls = [c["url"] for c in g["candidates"]]
        if digest in by_hash:
            prior = by_hash[digest]
            prior["also_referenced_at_order"].append(order)
            prior["all_source_urls"] = sorted(set(prior["all_source_urls"]) | set(all_urls))
            for u in all_urls:
                seen_selected.setdefault(u, prior)
            duplicates += 1
            continue

        kind = g["kind"]
        counters[kind] = counters.get(kind, 0) + 1
        context = g["alt"] or urlparse(g["link_href"]).path.rstrip("/").rsplit("/", 1)[-1] if (g["alt"] or g["link_href"]) else ""
        name = nice_filename(sel["url"], mime, kind, counters[kind], context)
        local, reused = safe_write(files_dir, name, data, digest)

        rec = {
            "order": order,
            "source_page_url": final_url,
            "original_asset_url": first_url,
            "selected_asset_url": sel["url"],
            "selected_via": sel["source"],
            "local_path": f"files/{local}",
            "reused_existing_file": reused,
            "asset_type": kind,
            "discovered_from": g["origin"],
            "mime_type": mime,
            "bytes": len(data),
            "width": w, "height": h,
            "alt": g["alt"],
            "caption": g["caption"],
            "link_href": g["link_href"],
            "sha256": digest,
            "higher_res_found": choice["higher_res_found"],
            "resolution_ambiguous": choice["ambiguous"],
            "selection_note": choice["note"],
            "candidates": [{k: c.get(k) for k in ("url", "source", "descriptor", "descriptor_kind", "width", "height", "bytes", "probe_error")
                            if c.get(k) not in (None, "", 0.0)} for c in g["candidates"]],
            "all_source_urls": all_urls,
            "also_referenced_at_order": [],
        }
        assets.append(rec)
        by_hash[digest] = rec
        for u in all_urls:
            seen_selected.setdefault(u, rec)

    # Heuristic warning for JS-rendered pages whose media isn't in the initial HTML.
    scripts = len(soup.find_all("script"))
    if len(groups) < 3 and scripts > 5:
        warnings.append("very few assets in the initial HTML but many <script> tags — page is probably "
                        "JavaScript-rendered; some assets may be missing (static HTML parsing only)")

    return {
        "source_page_url": url, "final_page_url": final_url,
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "page_title": (soup.title.get_text(strip=True) if soup.title else ""),
        "summary": {
            "discovered": len(groups), "downloaded": len(assets), "duplicates_skipped": duplicates,
            "filtered_skipped": len(skipped), "failures": len(failures),
            "ambiguous_resolution": sum(a["resolution_ambiguous"] for a in assets),
        },
        "warnings": warnings, "assets": assets, "skipped": skipped, "failures": failures,
    }


def write_markdown(m: dict, path: str) -> None:
    s = m["summary"]
    L = [f"# Asset manifest — {m['page_title'] or m['final_page_url']}", "",
         f"- Page: {m['final_page_url']}", f"- Fetched: {m['fetched_at']}",
         f"- Discovered {s['discovered']} · downloaded {s['downloaded']} · duplicates {s['duplicates_skipped']} · "
         f"filtered {s['filtered_skipped']} · failures {s['failures']} · ambiguous resolution {s['ambiguous_resolution']}", ""]
    if m["warnings"]:
        L += ["## Warnings", ""] + [f"- {w}" for w in m["warnings"]] + [""]
    L += ["## Downloaded", "", "| # | File | Type | Size (px) | Hi-res found | Ambiguous | Alt / caption | Selected source |",
          "|---|---|---|---|---|---|---|---|"]
    for a in m["assets"]:
        dims = f"{a['width']}×{a['height']}" if a["width"] else "?"
        text = (a["alt"] or a["caption"] or "").replace("|", "/")[:80]
        L.append(f"| {a['order']} | [{a['local_path']}]({a['local_path']}) | {a['asset_type']} | {dims} | "
                 f"{'yes' if a['higher_res_found'] else 'no'} | {'⚠️ ' + a['selection_note'] if a['resolution_ambiguous'] else ''} | "
                 f"{text} | {a['selected_asset_url']} |")
    for title, key, field in (("Filtered / skipped", "skipped", "reason"), ("Failures", "failures", "error")):
        if m[key]:
            L += ["", f"## {title}", ""] + [f"- #{x['order']} {x['url']} — {x[field]}" for x in m[key]]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


def list_links(url: str, timeout: int) -> list[str]:
    r = Fetcher(timeout).get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    host = urlparse(r.url).netloc
    out = []
    for a in soup.find_all("a", href=True):
        u = urljoin(r.url, a["href"]).split("#")[0]
        if urlparse(u).netloc == host and ext_of(u) not in MEDIA_EXT and u not in out and u.startswith("http"):
            out.append(u)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Download the highest-resolution media assets from ONE web page.")
    ap.add_argument("url")
    ap.add_argument("-o", "--out", help="output folder (default: ./downloaded-assets/<page-slug>)")
    ap.add_argument("--timeout", type=int, default=30)
    ap.add_argument("--max-probe", type=int, default=6, help="max candidate variants to measure per asset")
    ap.add_argument("--min-px", type=int, default=48, help="skip images whose width AND height are <= this")
    ap.add_argument("--list-links", action="store_true", help="print same-site page links and exit (no downloads)")
    args = ap.parse_args(argv)

    if args.list_links:
        print("\n".join(list_links(args.url, args.timeout)))
        return 0

    out = args.out or os.path.join("downloaded-assets", page_slug(args.url))
    os.makedirs(out, exist_ok=True)
    try:
        manifest = run(args.url, out, args.timeout, args.max_probe, args.min_px)
    except requests.RequestException as e:
        print(f"ERROR: could not fetch page {args.url}: {e}", file=sys.stderr)
        return 2

    with open(os.path.join(out, "asset-manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    write_markdown(manifest, os.path.join(out, "asset-manifest.md"))

    s = manifest["summary"]
    print(f"Page:                 {manifest['final_page_url']}")
    print(f"Output:               {out}")
    print(f"Discovered:           {s['discovered']}")
    print(f"Downloaded:           {s['downloaded']}")
    print(f"Duplicates skipped:   {s['duplicates_skipped']}")
    print(f"Filtered/skipped:     {s['filtered_skipped']}")
    print(f"Failures:             {s['failures']}")
    print(f"Ambiguous resolution: {s['ambiguous_resolution']}")
    for w in manifest["warnings"]:
        print(f"WARNING: {w}")
    for x in manifest["failures"]:
        print(f"FAILED #{x['order']}: {x['url']} — {x['error']}")
    for a in manifest["assets"]:
        if a["resolution_ambiguous"]:
            print(f"AMBIGUOUS #{a['order']}: {a['local_path']} — {a['selection_note']}")
    print(f"Manifest:             {os.path.join(out, 'asset-manifest.json')} (+ .md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
