# fetch-web-assets

Download the meaningful visual/media assets from **one** web page at the highest real
resolution available, deduplicated, with a JSON + Markdown manifest.

A standalone Python script (`fetch_web_assets.py`) plus a thin Claude Code skill
(`SKILL.md`) that calls it.

## Install

```bash
pip install requests beautifulsoup4 Pillow   # Pillow optional but strongly recommended (dimensions)
```

Install the Claude Code skill at user level so it works in every project:

```bash
mkdir -p ~/.claude/skills/fetch-web-assets
cp fetch_web_assets.py app.py SKILL.md README.md ~/.claude/skills/fetch-web-assets/
```

## The simple way: a window in your browser

Double-click **`Fetch Web Assets.command`** (Mac), or run `python3 app.py`. A page opens at
`http://127.0.0.1:8765` with:

- a box for one or more URLs (one per line)
- **Also fetch every page these link to?** No / Yes (Yes = every same-site page linked from each URL)
- **Save to**: type a folder or press **Choose…** for the normal folder picker
  (default `~/Downloads/web-assets`)

Each page is saved to `<folder>/<site>/<page-name>/`, e.g.
`web-assets/fionacohendesign.com/work-case-merck/`. Progress and any failures show
on the page, and **Open folder** reveals the result in Finder. It all runs on your
machine; the server only listens on 127.0.0.1 and rejects requests from other sites.

The first time on a Mac, macOS may block the double-click because the file came from the
internet: right-click it → **Open** once. The launcher installs the three Python
packages on first run if they're missing.

## Command line

```bash
python3 fetch_web_assets.py URL [-o OUT_DIR] [--min-px 48] [--max-probe 6] [--timeout 30]
python3 fetch_web_assets.py URL --list-links    # print same-site page links, download nothing
```

The default output is `./downloaded-assets/<page-slug>/`.

From Claude Code:

- `fetch web assets from https://example.com/case-study`
- `fetch web assets from https://example.com/case-study into ./assets/case-study`

## Output

```
<out>/
├── files/                 # one file per unique asset (SHA-256 deduped)
├── asset-manifest.json    # full detail, incl. every candidate URL considered
└── asset-manifest.md      # audit table
```

Each manifest record contains:

- the source page, plus the original and selected asset URLs, and how the selected URL was found
- the local path, type, MIME type, byte size and dimensions
- the alt text and nearby caption
- the order on the page, the SHA-256 hash, and every other place on the page that references the asset
- `higher_res_found`, `resolution_ambiguous` and `selection_note`
- the candidate list, with measured dimensions for each candidate

The manifest also lists everything that was skipped or failed, and why.

## Supported patterns

- `<img src>`, `srcset`, `<picture>/<source srcset>`
- lazy-load attributes: `data-src`, `data-srcset`, `data-lazy-src`, `data-original`, `data-full`, `data-hires`, and similar
- an `<img>` wrapped in `<a href>` that points to an image (a linked original)
- bare `<a href>` links to image or video files
- `background-image` in inline `style`, in `<style>` blocks and in linked stylesheets (`@font-face` blocks are ignored)
- `<video src>`, `<video poster>`, and `<source>` inside `<video>`
- `og:image` / `twitter:image` meta tags, which are often the largest export

## High-resolution selection

For each asset, the script collects every candidate URL:

- `src`, lazy-load attributes, `srcset` entries and `<picture>` sources
- the linked original
- a **CDN-original guess**: the same URL with size and quality params removed, such as `scale-down-to`, `w`, `width`, `h`, `q`, `dpr`, `format`, `fit` and `resize` (Framer, Imgix, Squarespace, Shopify, Contentful and others), and with WordPress `-300x200` filename suffixes removed

Then it **measures** the actual pixel dimensions of up to `--max-probe` candidates. Each probe streams only the image header, using Pillow. The candidate with the largest real pixel area wins.

An asset is flagged `resolution_ambiguous` in these cases:

- no candidate could be measured, so the choice fell back to `srcset` descriptors
- a candidate that wasn't probed claims a larger width than the winner
- the best source failed to download and the script fell back to a lower-ranked one

Images are never converted, re-encoded or upscaled.

## Filtering

These are skipped and listed in the manifest with the reason:

- tracking pixels, analytics, favicons, cookie-banner images, and social icons or logos (matched by URL or alt text)
- images ≤ `--min-px` in both dimensions
- SVGs and images ≤128px inside `<header>`, `<nav>` or `<footer>`

Content images are never dropped just because they look alike. Only byte-identical files are deduplicated.

## Safety

- Only GET requests are sent to the site; it is read-only.
- Fetches one page only. `--list-links` just prints links.
- Never deletes local files. If a filename already exists with identical content, the file is reused. If the content is different, the new file gets a `-2` (`-3`, …) suffix.
- The manifest files themselves are regenerated on every run.

## Limitations

- Parses static HTML only. Assets injected by JavaScript after load are not seen. The script prints a warning when the page has many scripts but few assets.
- The CDN-original guess may not match a provider's private URL scheme. The script falls back to the largest measured variant.
- Video dimensions are not measured.
- CSS `image-set()` and `@import`ed stylesheets are not followed.
