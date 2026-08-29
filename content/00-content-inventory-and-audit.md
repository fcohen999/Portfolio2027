# Step 1–2: Content Inventory & Audit

## Update — full existing site content received

You sent screenshots and a PDF covering the entire current site: homepage,
YAFFED, DOJ, CDC OneLab REACH, JPMorgan Chase (two tools), and Merck. All
audited and rewritten:

- `06-case-study-yaffed.md`
- `07-case-study-doj.md` — a few lines in your screenshot were too small to
  read with confidence; flagged inline, please confirm
- `08-case-study-cdc-onelab-reach.md`
- `09a-case-study-jpmorgan-dashboards.md` (ERMA) and
  `09b-case-study-jpmorgan-aomt.md` (Asset Outage Modeling Tool) — your
  homepage screenshot confirmed these are two separate case studies on
  the live site, not one engagement needing reconciliation, so the
  earlier merged draft has been split and the open question is resolved.
- `10-case-study-merck.md` — new, not previously mentioned in the brief
- `11-homepage-audit-and-rewrite.md` — full audit of the real homepage
  copy (hero, About, logos, bio), which was the most generic/junior-reading
  page on the whole site

## Still open

1. **Sport Shepherd assets/PRD excerpts** — still not provided;
   `04-case-study-sport-shepherd.md` is still a skeleton.
2. **Confirm the "Who I've worked with" logo list** — your homepage
   listed Johnson & Johnson, Girl Scouts of the USA, U.S. Army, and DHS as
   clients; none of these appear in your resume. Confirm they're current
   and accurate before they go live.
3. **JPMorgan Dashboards case study has no real numbers** — the weakest
   spot content-wise across all rewritten case studies; send any if you
   have them (see flag in `09a-case-study-jpmorgan-dashboards.md`).
4. Case study list is now confirmed complete at **8**: Sound Transit, CDC,
   JPMorgan Dashboards, JPMorgan AOMT, DOJ, Merck, YAFFED, Sport Shepherd.

---

## Site structure — confirmed recommendation

I can't check this against the live site (no access), so I can't literally
"confirm what's already there." But against the brief as written, the proposed
structure is the right one and I'd build to it as-is — no changes recommended:

- **Homepage** — hub only. Positioning intro + a teased index of every case
  study (title, one-line framing, one key metric) linking out. Not a
  single-page scroller.
- **Case study pages** — one per project:
  - Existing case studies (list TBD — see gap above)
  - Sound Transit (new)
  - Sport Shepherd (new)
- **Resume page** — dedicated page, content hierarchy as specified, plus a
  downloadable PDF.

Optional additions worth a yes/no from you, not built yet:
- A lightweight **/contact** or just a mailto + LinkedIn link in the footer of
  every page (cheaper than a full contact page, and enough for a portfolio).
- An **/about** section could live inside the homepage hero rather than as its
  own page — keeps the "hub, not scroller" structure intact while still giving
  you room for a fuller bio than a one-liner. Flagging as optional; default
  plan below keeps it in the homepage hero.

## Page list (target)

| Page | Status | Notes |
|---|---|---|
| Homepage | Drafted from real copy | See `11-homepage-audit-and-rewrite.md` |
| Case study — Sound Transit | New, drafted | See `03-case-study-sound-transit.md` |
| Case study — CDC OneLab REACH | Drafted | See `08-case-study-cdc-onelab-reach.md` |
| Case study — JPMorgan Risk Mgmt Dashboards | Drafted, needs real numbers | See `09a-case-study-jpmorgan-dashboards.md` |
| Case study — JPMorgan Asset Outage Modeling Tool | Drafted | See `09b-case-study-jpmorgan-aomt.md` |
| Case study — DOJ | Drafted, confirm unclear lines | See `07-case-study-doj.md` |
| Case study — Merck | Drafted | See `10-case-study-merck.md` |
| Case study — YAFFED | Drafted | See `06-case-study-yaffed.md` |
| Case study — Sport Shepherd | New, skeleton only | See `04-case-study-sport-shepherd.md` |
| Resume | Rebuild | See `02-resume-page.md` |

## Nav structure (target)

Flat, 3–4 items — matches the "underspoken" direction (no mega-menu, no
dropdown case study list in the nav itself; the homepage IS the case study
index):

```
FIONA COHEN            WORK    RESUME    CONTACT (mailto/LinkedIn)
```

## Content blocks per page (template)

**Homepage**
- Nav
- Hero: eyebrow (title/focus line) + positioning statement (H1) + intro
  paragraph + optional credibility strip (years, $ influenced, notable clients)
- Case study index: repeating row of {title, one-line framing, key metric,
  thumbnail} per project, in priority order
- Footer: resume link, contact, LinkedIn, copyright

**Case study page (template — applies to every project)**
- Nav
- Title block: client/project eyebrow, H1 title, one-line role/scope subhead,
  stat row (2–4 metrics)
- Hero image
- Narrative sections (label + body pattern): Problem, Role, Approach, Outcome
  — exact section labels adapt per project
- Supporting visuals: screenshots, diagrams, before/after, data viz
- Pull quote / key metric callout (optional)
- Footer: prev/next case study, back to homepage

**Resume page**
- Nav
- Header block: name, title, location, contact row, download button
- Experience (primary roles, full detail)
- Selected Guidehouse Work (dense/secondary tier)
- Education + Expertise (footer-style two-column)

## Audit criteria (apply once real copy is in hand)

When you send the current case study text, I'll flag anything that:
- Leads with visuals/deliverables ("designed a dashboard") instead of scope,
  ambiguity, or business impact ("owned IA for a platform serving 3 user
  tiers across 400+ screens, resolving conflicting stakeholder priorities")
- Uses passive/generic phrasing that hides your actual role on a team
  ("the team redesigned..." vs. "I led...", "I decided...", "I pushed back on...")
- Omits numbers where you plausibly have them (contract value, defect
  reduction, page/screen counts, team size, timeline)
- Reads as a feature list rather than a decision narrative (what you chose,
  what you deprioritized, why, and what happened as a result)
- Undersells seniority signals already present in your resume content: exec
  presentation, cross-functional leadership, mentorship, ambiguity navigated
