#!/bin/bash
# Double-click on a Mac to open the Fetch Web Assets window in your browser.
cd "$(dirname "$0")" || exit 1
if ! python3 -c "import requests, bs4, PIL" 2>/dev/null; then
  echo "Installing requests, beautifulsoup4, Pillow (one time)…"
  python3 -m pip install --user --quiet requests beautifulsoup4 Pillow || exit 1
fi
exec python3 app.py
