---
name: fetch-web-assets
description: Download the meaningful images/videos from ONE webpage into a local folder at the highest real resolution available (srcset, <picture>, linked originals, CDN size params), deduped, with an auditable manifest. Use for "fetch web assets from <url>", "fetch portfolio assets from <url> into <dir>", archiving a case study's images, etc.
---

# fetch-web-assets

Thin wrapper around `fetch_web_assets.py` in this skill's base directory (standalone,
also usable outside Claude Code — see README.md next to it).

## Steps

1. **Parse the request.** Extract the page URL. Extract the destination if given
   ("into ./assets/x", "to ./x"); otherwise omit `-o` and the script uses
   `./downloaded-assets/<page-slug>/`.
2. **One page only.** Do not crawl other pages unless the user explicitly asks. If they
   ask for a whole site, first run on ONE page, show the result, and wait for them to
   confirm it looks right. Then use `--list-links` to get same-site page URLs, show the
   list, and run once per page into `<dest>/<page-slug>/`.
3. **Dependencies.** If imports fail: `pip install requests beautifulsoup4 Pillow`.
4. **Run:**
   ```bash
   python3 "<skill base dir>/fetch_web_assets.py" "<URL>" [-o "<DEST>"]
   ```
   Useful flags: `--min-px 48` (tiny-image cutoff), `--max-probe 6` (variants measured
   per asset), `--timeout 30`.
5. **Report back** (short):
   - the exact command run
   - discovered / downloaded / duplicates skipped / filtered / failures
   - each failure (URL + error)
   - each asset flagged `resolution_ambiguous` and why
   - any WARNING lines (e.g. page looks JavaScript-rendered, stylesheet unreachable)
   - path to `asset-manifest.md` and `asset-manifest.json`
6. If a network error blocks the page itself, say so plainly; don't retry endlessly or
   switch to browser automation without asking.

## Guarantees to preserve

Read-only toward the site; never deletes or overwrites local files (identical content is
reused, different content gets a `-2` suffix); no format conversion or upscaling.
