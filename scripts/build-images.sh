#!/usr/bin/env bash
# Builds the web copies of the archived old-site images that the site uses.
# Source: assets/old-site/<page>/files (full resolution, never published).
# Output: docs/images/<page>/ — PNGs become WebP, at most 2400px wide.
# SVGs and videos are copied unchanged. Re-run after adding to the archive.
set -euo pipefail
cd "$(dirname "$0")/.."

for dir in assets/old-site/*/files; do
  page=$(basename "$(dirname "$dir")")
  out="docs/images/$page"
  mkdir -p "$out"
  for src in "$dir"/*; do
    name=$(basename "${src%.*}")
    case "$src" in
      *.png|*.jpg|*.jpeg)
        convert "$src" -resize '2400x>' -strip -quality 84 -define webp:method=6 "$out/$name.webp" ;;
      *.svg|*.mp4)
        cp "$src" "$out/" ;;
    esac
  done
done
