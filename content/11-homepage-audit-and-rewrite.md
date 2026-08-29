# Homepage — Audit & Rewrite (from current site)

## Source

Transcribed from your screenshot of the live homepage. Confident
transcription throughout.

## Current copy (as-is, for audit reference)

> Fiona Cohen — Simple tools for complex systems — Contact | Resume
>
> Hi, my name is Fiona. I'm a product designer in NYC.
>
> I love diving into new domains and working on highly specialized tools.
> I pride myself on my ability to balance high level systems thinking
> with high quality execution and attention to detail.
>
> [Project tiles: Merck Vaccination Explorer, J.P. Morgan Risk Management
> Dashboards]
>
> About me
> I have a passion for simplifying complex workflows and systems into
> easy to use tools.
> I spearhead design and product initiatives from conception through
> development.
> I am an effective design advocate, developing trust through consistent
> delivery of research-backed, high polish design work.
> I work to develop exceptional user experiences with a high degree of
> polish, emphasizing UX research, systems thinking, and effective
> collaboration with developers.
>
> [Project tiles: CDC OneLab REACH (with live site link), J.P. Morgan
> Asset Outage Modeling Tool, DOJ Time to Hire, YAFFED.org]
>
> Who I've worked with
> [Logos: CDC, Johnson & Johnson, Girl Scouts, U.S. Army, Merck, DHS,
> J.P. Morgan, Tampa General Hospital, DHS/VA]
>
> I grew up in Hell's Kitchen, NYC, and graduated from the Maryland
> Institute College of Art (MICA) with a BFA in Graphic Design. I'm
> passionate about data visualization and workflow-driven tool design. In
> my spare time, I enjoy playing piano, home improvement projects, and
> spending time with my little brother.

## Audit

This is the single clearest example in your whole site of the problem the
brief opened with: **the copy reads junior, the work is senior.**

- **"Hi, my name is Fiona. I'm a product designer in NYC."** — This is
  the first sentence a visitor reads, and it establishes nothing: no
  seniority, no specialization, no scope. It reads like a bootcamp
  graduate's intro, not someone whose case studies include presenting
  directly to a federal CIO and generating $9.2M+ in follow-on
  government/enterprise contracts.
- **The four "About me" bullets are all trait claims with zero
  evidence attached, right next to case studies that ARE the evidence.**
  "I am an effective design advocate, developing trust through consistent
  delivery" is an assertion; the CDC quote about winning $9.2M in trust
  is the proof — and they're not connected anywhere on the page. Every
  one of these four bullets restates a personality trait ("passion for
  simplifying," "effective advocate," "high degree of polish") instead of
  pointing at the specific evidence sitting right there in your project
  tiles.
- **No years of experience, no sector breadth, no leadership signal
  anywhere on the homepage.** A visitor has to click into individual case
  studies to learn you've led teams, presented to executives, and managed
  multi-consultant engagements — none of that is asserted at the level
  that actually sets first impressions.
- **"Simple tools for complex systems" (tagline) undersells scope** —
  it's about the *artifacts* (tools), not what actually differentiates
  you: navigating ambiguous, high-stakes, multi-stakeholder problems at
  federal/enterprise scale. Worth testing against a rewritten tagline
  that carries more of that.
- **The personal bio close (Hell's Kitchen, MICA, piano, home
  improvement, little brother) is good and should mostly stay** — it's
  specific, human, and unpretentious, which is a real asset for
  "underspoken confidence." It just needs to stay a closing beat, not
  compete with the positioning statement for the reader's first
  impression.
- **"Who I've worked with" logo strip is a good, underused asset** —
  CDC, J&J, U.S. Army, Merck, DHS, J.P. Morgan, Tampa General, DOJ/VA is
  a genuinely impressive client roster for a homepage to be able to show
  at a glance. Keep it, and it does a lot of the "senior/serious" work
  your prose currently doesn't.

## Rewritten homepage copy

**Eyebrow (replaces "Simple tools for complex systems"):**
SENIOR PRODUCT DESIGNER · COMPLEX SYSTEMS · DATA & AI PRODUCTS

**Hero (replaces "Hi, my name is Fiona...")**

I design the systems that make complicated things usable — for federal
agencies, banks, and transit riders.

Eight years leading product design across government, finance, and
healthcare — turning ambiguous, high-stakes problems into shared design
systems and shippable products. Most recently at Guidehouse; prior
senior/lead work at JPMorgan Chase, the U.S. DOJ, and Sound Transit.

*(This matches what's already in `prototype/index.html` — I'd written it
before I had your real homepage copy, and it holds up against the audit
above, so I'm keeping it rather than rewriting a third version. Tell me
if you want a different angle now that you can see it next to the
original.)*

**About me — rewritten to point at evidence instead of asserting traits**

I spearhead design and product work from early strategy through
implementation and QA — not just the interface, but the research, the
system it lives in, and the case for it to stakeholders ranging from
individual contributors to a federal CIO.

That's meant leading design systems built to hold across organizations
that don't share infrastructure (DOJ), reframing a stalled 5,000+ page
accessibility backlog around systemic risk instead of ticket count
(Sound Transit), and turning a single research deliverable into a
multi-year, $9.2M client relationship (CDC). I've managed and mentored
designers, presented technical and product direction to executive
leadership, and stayed accountable for outcomes through implementation,
not just the design file.

*(This replaces the four generic "I am/I have" bullets with three
concrete, evidence-backed claims, each pointing at a specific case study
a reader can click into. If you'd rather keep a short bulleted format
instead of prose, I can restructure this into 3 bullets instead — say the
word.)*

**Who I've worked with** — keep as-is structurally (logo strip). Confirmed
final client list (Girl Scouts removed — no such logo actually exists on
the site; that was a misread on my part transcribing the screenshot;
J&J, U.S. Army, and DHS confirmed accurate):
CDC · Johnson & Johnson · U.S. Army · Merck · Department of Homeland
Security · J.P. Morgan Chase · Tampa General Hospital · U.S. Department
of Veterans Affairs

**Personal bio close — keep almost verbatim, lightly tightened:**

I grew up in Hell's Kitchen, NYC, and graduated from MICA with a BFA in
Graphic Design. Outside of work, I play piano, take on home improvement
projects, and spend time with my little brother.

## Case study index — confirmed final list (8 total)

Your homepage confirms the full existing case study set. Combined with
the new additions from the brief, the homepage index should show, in
some priority order you choose:

1. Sound Transit (new)
2. CDC OneLab REACH
3. J.P. Morgan Risk Management Dashboards
4. J.P. Morgan Asset Outage Modeling Tool
5. DOJ Time to Hire
6. Merck Vaccination Explorer
7. YAFFED
8. Sport Shepherd (new — still needs your content)

This resolves the earlier open question in `00-content-inventory-and-audit.md`
about whether the case study list was complete.
