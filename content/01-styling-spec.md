# Step 5: Styling System Spec

Editorial, warm, understated, precise. Confidence through restraint, not
volume. Everything below is specific enough to punch into Framer's style
panel directly (or a stylesheet, if you move off Framer).

## Reference points

Three genuinely well-known sites in this register, and what to steal from
each. I can't screenshot these live from here (network policy blocks fetching
them from this session), so treat the specifics as "go look, here's what
you're looking for" rather than pixel-verified specs:

1. **Craig Mod's personal site (craigmod.com)** — long-form writer/photographer
   site. What works: warm off-white ground (never pure white), a serif body
   face at a genuinely large size for reading comfort, almost no chrome —
   nav is a couple of text links, no buttons-as-UI-widgets. Steal: body text
   treated as the main event, not filler around images.
2. **Are.na (are.na)** — a research/bookmarking tool, not a portfolio, but the
   closest mainstream example of "square-edged, restrained, warm-neutral."
   What works: zero border-radius anywhere, hairline 1px borders instead of
   shadows to separate content, a plain grotesque type system that stays
   quiet because of spacing rather than styling. Steal: hairline-border
   grid module as the base unit for laying out a case study's supporting
   images/data instead of cards-with-shadows.
3. **Print-derived studio/agency case-study pages** (the general Pentagram /
   independent-studio school of portfolio site) — what works: a narrow
   label column running down the left of each section (small caps, tracked
   out) paired with a wider body column — a print margin-note device
   translated to web. Steal: this exact label+body pattern, used below as
   the core structural unit for case study narrative sections.

None of these use color for emphasis — all three lean on type scale,
whitespace, and hairline rules to create hierarchy. That's the model here:
color stays almost entirely neutral, with one warm accent used sparingly
enough that it still reads as a decision, not a UI convention.

## Typography

Three real directions, rendered (not just named) in
`prototype/type-scale-mockups.html` and as PNG screenshots sent alongside
this doc. Summary of the tradeoff:

- **A — Archivo only** (Expanded/SemiExpanded headline + regular body, one
  family). Most architectural, most "square-edges-carry-through-typography."
  Risk: can read slightly cold/technical without a serif to soften body copy.
- **B — Archivo Expanded headline + Newsreader body** (grotesque + serif
  pairing). Squared, heavy headlines with a warm, readable serif underneath
  for the actual case-study prose. **This is my recommendation** — it's the
  direction that most directly answers "editorial + warm" while keeping the
  square-edge architecture in the headline weight.
- **C — Space Grotesk headline + Fraunces body**. Space Grotesk is a close
  cousin of Archivo (similar squared/technical character, slightly more
  humanist in the lowercase). Fraunces brings real personality — it has
  "wonky" optical-size variation and is more expressive than Newsreader.
  Good if you want more warmth/personality; risk is it reads less
  "understated" than the brief calls for, since Fraunces has more visual
  flavor than a portfolio this restrained typically wants.

**Recommendation: B.** Go look at the mockups and tell me if you agree —
easy to swap to A or C, all three use only free Google Fonts.

### Type scale (Option B — Archivo + Newsreader)

All sizes desktop / mobile. Line-height as a unitless multiplier.

| Role | Font | Weight | Size (desktop / mobile) | Line-height | Letter-spacing |
|---|---|---|---|---|---|
| Display / homepage hero | Archivo Expanded | 800 | 72px / 40px | 1.05 | -0.01em |
| H1 — case study / page title | Archivo SemiExpanded | 700 | 48px / 32px | 1.1 | -0.005em |
| H2 — section head | Archivo | 700 | 32px / 24px | 1.2 | normal |
| H3 — sub-section | Archivo | 600 | 22px / 19px | 1.3 | normal |
| Eyebrow / label | Archivo | 600 | 13px / 12px | 1.4 | 0.08em, uppercase |
| Body | Newsreader | 400 | 18px / 16px | 1.6 | normal |
| Body — lead/intro paragraph | Newsreader | 400 (italic for pull quotes) | 22px / 18px | 1.5 | normal |
| Caption / metadata | Archivo | 500 | 14px / 13px | 1.4 | 0.02em |
| Nav link | Archivo | 600 | 15px / 15px | 1 | 0.03em, uppercase |
| Stat number (case study metrics) | Archivo Expanded | 800 | 40px / 28px | 1 | -0.01em |

Google Fonts imports needed:
`Archivo:ital,wght@0,400;0,600;0,700;0,800` (use the Expanded/SemiExpanded
width axis — Archivo is a variable font with a width axis in the Google
Fonts variable delivery; if Framer's font picker only exposes static
weights, pull the static "Archivo Expanded" and "Archivo SemiExpanded"
families instead) and `Newsreader:ital,wght@0,400;1,400;0,500`.

## Color palette

Warm neutrals, cream base, one accent. No pure black, no pure white, no
saturated primaries.

| Token | Hex | Use |
|---|---|---|
| `bg-primary` | `#F5F1EA` | Page background everywhere |
| `bg-secondary` | `#EDE6D8` | Section-break backgrounds, footer, resume "dense tier" block |
| `text-primary` | `#2A2622` | Headlines, body text |
| `text-secondary` | `#6B6258` | Captions, metadata, nav (non-active state) |
| `border` | `#D9D0BF` | Hairline rules, dividers, image/card borders, input borders |
| `accent` | `#B4552D` | Links, key metric numbers, hover states, active nav underline — used sparingly |
| `accent-hover-bg` | `#B4552D` (same as accent) | Button fill on hover; text flips to `bg-primary` |

Usage rule: `accent` never fills large areas. It marks the single most
important number or link in a given block (one stat per case study section,
one link state) — if two things on screen are both orange, pull one back to
`text-primary`.

## Spacing scale

Base unit 8px.

| Token | Value |
|---|---|
| `xs` | 4px |
| `sm` | 8px |
| `md` | 16px |
| `lg` | 24px |
| `xl` | 32px |
| `2xl` | 48px |
| `3xl` | 64px |
| `4xl` | 96px |
| `5xl` | 128px |

- Section vertical padding: `5xl` (128px) top/bottom desktop → `3xl` (64px) mobile.
- Between paragraphs within a section: `lg` (24px).
- Grid gutters: `lg` (24px) desktop → `md` (16px) mobile.
- Container max-width: 1200px, with `4xl` (96px) side margin desktop →
  `md`–`lg` (16–24px) side margin mobile.

## Edges, borders, elevation

- `border-radius: 0` — every element, no exceptions (buttons, images,
  inputs, containers).
- No box-shadow, ever. Separation comes from a 1px `border` hairline or
  whitespace, never elevation.
- Buttons: 1px solid border in `text-primary`, transparent fill, `text-primary`
  label. Hover: fill flips to `accent`, text flips to `bg-primary`. Square
  padding (`sm` vertical / `lg` horizontal), no pill shape.
- Images: 1px `border` around every photo/screenshot instead of a shadow.
  Crop to consistent aspect ratios within a row (don't mix 16:9 and 4:3 in
  the same grid).
- Dividers between sections/rows: 1px `border`, full container width.

## Grid

- Desktop: 12-column grid, `lg` gutters, 1200px max container.
- Mobile: 4-column grid, `md` gutters, full-bleed edge-to-edge images
  allowed (images can ignore the side margin; text content respects it).
- Breakpoint: single breakpoint at 768px is enough for this content
  (homepage index, case study label+body, resume) — no need for a
  tablet-specific third layout given the content density here.

## Page-by-page layout

### Homepage

**Desktop**
- Nav: single row, `FIONA COHEN` left (Archivo 700, 15px, uppercase not
  needed on the wordmark itself), `WORK · RESUME · CONTACT` right, `lg`
  padding, bottom 1px `border` hairline, no background fill (sits on
  `bg-primary`).
- Hero: left-aligned block, max-width 9 of 12 columns. Eyebrow line
  ("SENIOR PRODUCT DESIGNER · COMPLEX SYSTEMS · DATA & AI PRODUCTS"), then
  Display-size positioning statement (2–3 lines, e.g. "I design the systems
  that make complicated things usable — for federal agencies, banks, and
  transit riders."), then one Body-lead paragraph. `5xl` top padding, `3xl`
  bottom padding before the index starts.
- Optional credibility strip: 3–4 stat pairs in a single row (e.g. "8 YRS",
  "$3M+ IN CONTRACTS INFLUENCED", "4 SECTORS") — Caption-size labels under
  Stat-number-size figures, separated by 1px vertical `border` rules.
- Case study index: full-width rows, each row a 2-column layout inside
  itself — image left (5 of 12 cols) / text right (7 of 12 cols), alternating
  L/R per row optional (or keep consistent left-image for scanability — pick
  one, don't alternate AND vary text length, that reads chaotic). Text side:
  eyebrow (client/project name), H2 title, one-line framing in Body size,
  one key metric in accent-colored Stat style. Full-width 1px `border`
  divider between rows, `2xl` vertical padding per row. Entire row is a
  single click target.
- Footer: `bg-secondary` fill, `2xl` padding, resume link / email / LinkedIn
  as a single text row, copyright line below in Caption/muted.

**Mobile**
- Nav collapses to wordmark + a simple stacked text menu (no hamburger icon
  needed at only 3 items — tap wordmark or a plain "MENU" text toggle that
  reveals `WORK / RESUME / CONTACT` stacked below the fold of the nav bar;
  avoid an icon-only affordance so it stays true to "no decorative UI").
- Hero: full column width, Display size drops to 40px (still bold/architectural,
  just narrower measure), credibility strip goes from one row to a 2×2 grid
  with `border` dividers between cells instead of a single row of verticals.
- Case study index: image moves ABOVE text, full-bleed (edge-to-edge, ignores
  side margin) at a fixed 4:3 or 16:9 crop, then eyebrow/title/framing/metric
  stacked below with normal side margins. `xl` vertical padding per row,
  1px `border` divider between rows.
- Footer: same content, stacked vertically, `lg` padding.

### Case study page (template)

**Desktop**
- Nav: same as homepage, plus a persistent "← WORK" text link at the very
  top-left of the content area (above the title block) so users can bail
  back to the index without scrolling to a footer.
- Title block: eyebrow (`CLIENT — YEAR`), H1 project title, one-line
  role/scope subhead in Body-lead italic, then a stat row: 2–4 stat blocks
  (Stat-number + Caption label under each), separated by 1px vertical
  `border` rules, NOT boxed/carded.
- Hero image: full container width (12 cols), 1px `border`, `2xl` margin
  below before narrative starts.
- Narrative sections — the core repeating pattern: 12-col grid split
  3/9. Left 3 cols: section eyebrow label (e.g. "THE PROBLEM"), sticky-ish
  but not required to actually implement `position: sticky` — just
  vertically top-aligned with the right column. Right 9 cols: Body-size
  Newsreader prose. `3xl` gap between sections, 1px `border` divider above
  each new section label.
- Data/comparison visuals (e.g. before/after page-count reduction, the
  Sound Transit 7,000→160-page narrowing): full-width breakout that ignores
  the 3/9 split — full 12 cols, `border`-framed, Caption-style label
  centered beneath.
- Screenshot grids: 2-up or 3-up within the 9-col text column (not full
  12-col) so images stay visually subordinate to the narrative; `lg`
  gutters, 1px `border` per image, consistent aspect ratio per row.
- Pull quote / key metric callout: centered, full 12 cols, Stat-number size
  in `accent`, 1px `border` rule above and below, generous (`2xl`) padding.
- Footer: prev/next case study as two text links (← previous / next →)
  plus "back to work index," `bg-secondary` fill matching homepage footer.

**Mobile**
- "← WORK" link stays, sits directly under nav.
- Title block: stacks fully. Stat row goes from horizontal-with-vertical-rules
  to a 2×2 grid with horizontal `border` dividers between rows (vertical
  rules don't survive at narrow width).
- Narrative sections: the 3/9 split COLLAPSES — eyebrow label sits as its
  own line above the body paragraph, with a 1px `border` rule directly
  beneath the label (this rule is what replaces the visual separation the
  side-by-side columns used to provide). `lg` gap between label and body,
  `2xl` gap between sections.
- Data/comparison visuals: this is the hard case named in the brief.
  - For a genuine before/after or reduction narrative (Sound Transit's
    7,000-page → 160-page framing): rebuild as a **stacked stat comparison**
    — two Stat-number blocks stacked vertically with a small "→" or "DOWN
    TO" Caption-label between them, not a side-by-side chart. This preserves
    meaning without needing horizontal space.
  - For an actual multi-column data table (rare in this content, but keep
    the rule): wrap the table in a `border`-framed container with
    `overflow-x: auto` and a visible "→ scroll" Caption label at its top
    edge, rather than silently collapsing columns.
  - For side-by-side UI comparisons (e.g. two screen states): stack them
    vertically, each full-width, with a Caption label ("BEFORE" / "AFTER")
    above each rather than relying on left/right position to convey it.
- Screenshot grids: 2-up/3-up collapses to single column, full width,
  `md` gap between images, no side margin (full-bleed) since the images
  themselves already have a `border`.
- Pull quote: same treatment, just narrower measure.
- Footer: prev/next links stack vertically instead of side-by-side.

### Resume page

**Desktop**
- Nav: same global nav.
- Header block: Name as H1 ("FIONA COHEN"), title/focus line directly below
  in Body-lead ("Senior Product Designer · Complex Systems · Data & AI
  Products"), location in Caption, then a contact row (Email · Portfolio ·
  LinkedIn) as plain text links separated by " · ", `accent` on hover only.
  "Download PDF" button (bordered square button per the button spec) sits
  to the right of this block, vertically centered against it.
- Experience section: full prose treatment, most prominent. Each role is a
  block: `CLIENT — YEARS` as an H2-weight eyebrow, title(s) as H3, then
  body-size bullet list (use a simple hairline-topped list, not bullet
  glyphs — a thin `border-top` rule per item reads more editorial than a
  bullet dot). `3xl` gap between roles.
- Selected Guidehouse Work: `bg-secondary` full-width band to visually
  demote this section under Experience. Denser: each client is one
  compact block — `Client (bold, Archivo 600, 16px)` — `Project name, role`
  on the same or next line in Caption size — 1–2 line outcome in Body at
  16px (below the 18px primary-tier body size) — sub-items run in as a
  single inline comma-separated line rather than bullets. `lg` gap between
  clients, tighter than Experience's `3xl`.
- Education + Expertise: two-column footer band on `bg-primary`, 6/6 split.
  Education as plain stacked lines. Expertise as a single Caption-size line,
  items separated by " · " (not chips/pills — stays consistent with "no
  pill UI").

**Mobile**
- Header block: stacks — name, title line, location, contact row (wraps
  naturally), Download PDF button full-width below the contact row.
- Experience: unchanged structurally, just single-column at narrower
  measure — this section already reads fine narrow.
- Selected Guidehouse Work: same compact block pattern, already narrow-friendly.
- Education + Expertise: stack vertically instead of 6/6.

## Touch targets & interaction (mobile, all pages)

- Minimum tap target 44×44px for nav links, buttons, and case-study index
  rows (the whole row is the tap target, not just the title text).
- Body line length: cap at ~65 characters even on wider mobile devices —
  don't let Newsreader body text stretch edge-to-edge on a phone in
  landscape; keep the `md`/`lg` side margins regardless of viewport width.
- No hover-only affordances anywhere (the desktop button hover-fill has no
  mobile equivalent needed — default bordered state is enough on touch).
