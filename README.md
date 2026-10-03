# Portfolio2027

The portfolio site for fionacohendesign.com, published with GitHub Pages at
https://fcohen999.github.io/Portfolio2027/ — whatever is on `main` is live.

## Contents

- `content/00-content-inventory-and-audit.md` — site structure, page/nav
  inventory, and audit criteria (flags what's still needed: the current
  site's actual copy)
- `content/01-styling-spec.md` — full design system: type scale, color,
  spacing, layout, desktop + mobile, per page
- `content/02-resume-page.md` — final resume copy
- `content/03-case-study-sound-transit.md` — rewritten Sound Transit case study
- `content/04-case-study-sport-shepherd.md` — Sport Shepherd skeleton (needs
  your input — see file)
- `content/05-image-checklist.md` — exactly which images to export from Framer
- `assets/old-site/` — full-resolution images from every page of the
  current site, one folder per page (see its README)
- `content/12-visual-system-v2.md` — the current visual system (type, grid,
  colour, figures, navigation) and the ERMA asset map
- The site itself is at the top of the repo: `index.html`, `resume.html`
  and the `case-study-*.html` pages. Open `index.html` in a browser to view
  it locally. The homepage and all
  eight case studies use the v2 system (`system.css`, `system.js`,
  self-hosted fonts in `fonts/`). The resume page uses the v2 masthead
  and footer around a printable résumé sheet styled by `resume.css`.

## Résumé PDF

`Fiona_Cohen_Resume.pdf` (the page's "Download PDF" button) is generated
from `resume.html`'s print styles, so edit the page, then rebuild:

    node scripts/build-resume-pdf.mjs

The script needs Playwright and stops with an error if any résumé text
is set below 8pt.

## Still needed from you

See the top of `content/00-content-inventory-and-audit.md` — mainly the
current site's page text and the Sport Shepherd assets/PRD excerpts.
