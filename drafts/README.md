# Copy drafts

Before any copy change goes live, save a comparison here. Each file shows
the live text and the draft text side by side, with the differences
highlighted:

- **Left (Live):** the pages on the `main` branch on GitHub. That's what
  the public site shows, at https://fcohen999.github.io/Portfolio2027/prototype/
- **Right (Draft):** the pages on the branch being worked on. Not public
  until that branch is merged into `main`.

Red, struck-through words were removed; green words are new. Only pages
whose text changed are included. Images, captions and layout aren't compared.

To make a new one, from the repo folder:

    python3 scripts/compare-copy.py "short name for the change"

It saves `drafts/<date>-<short-name>.html`. Open it in a browser.

Note: GitHub Pages currently publishes this whole repo, so these files
are public at /Portfolio2027/drafts/ too.
