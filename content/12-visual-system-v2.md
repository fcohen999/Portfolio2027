# Visual system v2 (supersedes the look in `01-styling-spec.md`)

Content and IA are unchanged. This replaces the visual layer only.
Converted: the homepage and all eight case studies. `resume.html` and
`type-scale-mockups.html` still use the old `styles.css`.
Files: `prototype/system.css`, `prototype/system.js`, `prototype/fonts/`.

## Decisions

- **Type.** One family, Schibsted Grotesk (a grotesk drawn for a news
  publisher), does all reading and display work. IBM Plex Mono is used only
  for indexing: project and figure numbers, metadata keys, running labels.
  The serif is gone. Sizes: case-study title 42, homepage statement 34,
  section heading 22, thesis 20, body 16/1.6 at about 64ch, captions 13,
  keys 11.5 mono. Both fonts are self-hosted under the SIL Open Font License.
- **Colour.** Neutral paper `#F5F5F2`, ink `#141414`, two greys, a hairline
  `#CDCDC7`. There is one accent, vermilion `#C8361A`. It marks figure and
  section numbers, the current section, selected tabs, link hover and the one
  typographic data plate, and nothing else. Colour otherwise comes from the work.
- **Grid.** 12 columns, 24px gutters, 40px margins, 1440px max width.
  - Homepage index: No. / Client and role / Case study / Image.
  - Case study: a sticky contents rail (cols 1–3) and content (cols 4–12, a
    9-column subgrid). Inside the content, prose takes 6 columns and margin
    notes take 3. Figures span 9 columns, split 7+2 or 6+3, or use even two-up
    grids.
- **Figures.** Real screenshots sit on a flat grey matte, with no browser
  chrome, device frames, rounded cards or shadows. Every figure has a numbered
  caption. Clicking any figure opens it at full resolution, with an
  "Actual size" toggle so dense UI can be inspected on a phone.
- **Metadata.** Rule-separated key/value rows: the header strip, the facts
  column for metrics, and the homepage index columns. There are no pills and
  no KPI cards.
- **Navigation.** A running header shows the project number and the current
  section. The rail shows contents, the current section and reading progress.
  On mobile it becomes a sticky horizontal section strip. Previous/next links
  are numbered.
- **Motion.** Only hover colour, the tab switch and the rail state. Everything
  is turned off under `prefers-reduced-motion`. Without JS, tab panels stack.

## Homepage changes worth knowing

- About, the client list and the bio moved below the work index (they were
  between the hero and the work). The wording is unchanged.
- Projects 01–05 are featured rows. 06–08 are a compact "further work" table.
  The order is unchanged.
- Sound Transit has no imagery in the archive, so its slot uses a typographic
  plate built from its own stated figures (~80%, 5,000+ pages). This is not a
  mock screenshot.
- ERMA's cover now uses the full Info Hub screen (`erma/files/image-02.png`)
  instead of the old cropped chart cover (`home/files/image-02-erma.png`).
  The old cover is only a cropped piece of the chart widget, so the full screen
  shows the actual work better.

## ERMA asset map (archive `assets/old-site/erma/`, 18 files)

| File | Figure | Shows |
|---|---|---|
| image-05 | Fig. 1a | ERMA Home, Info Hub tab |
| image-03 | Fig. 1b | Action Center tab |
| image-04 | Fig. 1c | Measurement Viewer tab |
| image-07.svg | Fig. 2a | Donut widget template (zone-coded) |
| image-08.svg | Fig. 2b | Measurement Viewer widget template |
| image-06 | Fig. 3 | Action Center widgets at high resolution |
| image-13, image-14 | Fig. 4a/b | Staff widget card, two states |
| image-12 | Fig. 5 | Modal template schematic |
| image-09, -10, -11 | Fig. 6a–c | Three modals built on the template |
| image-15 … -18 | Fig. 7A–D | Staff modal: default, month focus, total-line toggle, both |
| image-02 | Homepage cover | Info Hub, unframed crop |
| **image-01** | **not placed** | **Same Info Hub screen as image-05 (pixel diff after resizing shows only resampling). Needs your decision.** |

Activity Calendar, the fourth tab, has no asset in the archive. Fig. 1
notes that it isn't pictured.

## Asset maps, other case studies

Every archived image is placed except the two flagged duplicates
(`erma/image-01`, `cdc/image-01`).

**Sound Transit.** Nothing in the archive. Two diagrams are built in HTML from
figures already in the copy: the unit of analysis (5,000+ pages → 160 / 29) and
the pipeline (URLs → Audit → Aggregate → Deduplicate → Analyze). The remediation
phases are set as a three-column table. Five dashed "image pending" slots name
the files the page still expects.

**CDC** (`cdc/`, 16 files)

| File | Figure |
|---|---|
| image-11 | Fig. 1, landing page top |
| image-03 … -10 | Fig. 2.1–2.8, design-system sheets |
| image-02 | Fig. 3, course cards |
| image-12, -13 | Fig. 4a/b, landing-page entry points |
| image-14, -15, -16 | Fig. 5a–c, My Learner Hub states |
| **image-01** | **not placed.** The same card group as image-02 at a looser crop; image-02 is sharper. Needs your decision. |

**AOMT** (`outage-modeler/`, 10 files, plus the homepage cover)

| File | Figure |
|---|---|
| video-01.mp4 (poster: image-01) | Fig. 1, walkthrough. Has controls and never autoplays. |
| home/image-04-outage-modeler | Fig. 2, analyst workflow diagram |
| image-04 | Fig. 3, dependency model |
| image-05 | Fig. 4, dependency patterns |
| image-01, -02, -03 | Figs. 5–7, steps |
| image-06, -07 | Details beside Figs. 6 and 7 |
| image-08 | Fig. 8, dependent impacts |
| image-09 | Fig. 9, export modal |

**DOJ** (`tth/`, 12 files)

| File | Figure |
|---|---|
| image-01 | Fig. 1, hiring case |
| image-02 … -09 | Fig. 2.1–2.8, attachments component in 8 states |
| image-10, -11, -12 | Fig. 3.1–3.3, completing a segment |

**Merck** (`merck/`, 7 files)

| File | Figure |
|---|---|
| image-02 | Fig. 1, explorer |
| image-01 | Fig. 2, medical/social split |
| image-04, -05, -03 | Fig. 3.1–3.3, choropleth from state to county |
| image-06 | Fig. 4, location overlay |
| image-07 | Fig. 5, social data on the map |

**YAFFED** (`yaffed/`, 7 files)

| File | Figure |
|---|---|
| image-01 | Fig. 1, homepage; reused as 7b "after" |
| image-02 | Fig. 2, petition then donation |
| image-04 | Fig. 3, donation modal |
| image-03 | Fig. 4, sticky sidebar |
| image-05 | Fig. 5, about section |
| image-06 | Fig. 6, infographic templates |
| image-07 | Fig. 7a, before |

**Sport Shepherd.** Still waiting on content. The placeholder note is restyled
and has one image-pending slot.

## Titles (changed on request)

Each project is now titled by name, as on fionacohendesign.com, with the
current site's one-line description under it. The narrative headline moves
below that as the hook. On the homepage, the old framing sentence under each
featured headline is gone; the same sentence still appears on each case-study
page.

The descriptions come from the current site, with one typo fixed
("dependcies"). Sound Transit and Sport Shepherd aren't on the current site:
- **Sound Transit:** the name "Sound Transit Accessibility Strategy" and its
  description are new. Please check them.
- **Sport Shepherd:** its existing headline is used as the description.

## Diagrams and stats (changed on request)

**Stats removed.** The number column at the top of each case study is gone,
and the title takes the space. Every figure that mattered is still in the body
copy. The homepage intro still has its three stats (8 yrs, $3M+, 4 sectors).

**Diagram language.** This is part of `system.css`, under DIAGRAMS. The
diagrams below are redrawn in it instead of shown as pasted images:
- AOMT Fig. 2: analyst workflow
- AOMT Fig. 3: dependency model
- AOMT Fig. 4: dependency patterns
- ERMA Fig. 2: widget templates
- ERMA Fig. 5: modal template

Every redrawn diagram uses the same vocabulary:
- **Analyst action:** outlined box
- **System response:** filled pill
- **Optional step:** dashed box
- **Decision:** diamond
- **Loop:** accent arrow
- **Relation:** mono label on a hairline arrow
- **Reserved spacing:** accent hatching

Each caption has an "Original" link that opens the archived image, so the
originals are still one click away. Screenshots, design-system sheets and
infographics stay as images.

Open question: the original AOMT dependency-pattern diagram marks two loops
red and one green. The redraw keeps that as accent vs. ink but doesn't say
what the colours meant.
