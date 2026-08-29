# Step 4.1: Case Study — Sound Transit

Replaced with your own polished rewrite (2026-08-27) — this supersedes
the earlier draft entirely. Stored here as final copy for the case study
page, structured to the template in `01-styling-spec.md`.

---

**Eyebrow:** SOUND TRANSIT — 2024–2025
**Role line:** Accessibility Lead
**Title (H1):** Turning an Unactionable Accessibility Audit into a Strategy Engineering Could Execute
**Subhead:** An 8-month engagement, extended beyond its original scope, reframing a stalled 5,000+ page accessibility backlog around systemic risk instead of ticket count.

**Headline metrics (stat row):**
- 5,000+ — total pages
- 160 / 29 — highest-traffic pages / shared templates scoped
- 4 — reusable applications designed and built
- ~80% — of issues traced to shared components
- 3-phase — remediation strategy, client-owned post-engagement

---

**THE PROBLEM**

Sound Transit's site had already been through an accessibility audit
before I joined — it produced thousands of Jira tickets and stalled
there. Every ticket looked equally urgent, because the backlog treated
each occurrence as its own problem, even when dozens traced back to one
shared component. As a public transit agency, Sound Transit carries real
ADA litigation exposure — this wasn't a polish project, it was risk
management, and I was the person relied on to make sure that risk
actually got closed, not just documented.

**MY ROLE**

My title was Accessibility Lead, but the job was closer to design and
technical strategist: I owned the call on what not to fix as much as
what to fix — including telling the client that their existing plan,
clear all 7,000+ tickets, was the wrong plan. I designed the audit
methodology, built the software to run it at scale, analyzed the
resulting data, authored the remediation strategy, and trained the
developers who'd carry it forward without me. Every deliverable existed
to support one decision: where the site's real risk actually lived, and
what order of operations would retire the most of it fastest.

> "I had to tell the client that their existing plan — clear all 7,000+
> tickets — was the wrong plan."

*(Pull quote — set large, own visual break. Strongest single line in the
case study; should carry more visual weight than body text.)*

**REFRAMING THE SCOPE**

Auditing 5,000+ pages individually was the wrong unit of analysis — most
of the site is generated from a small set of shared components and
templates, so page-by-page tracking hides the real risk surface instead
of revealing it. I scoped around two lenses instead: 160 highest-traffic
pages, where rider impact concentrated, and 29 shared templates, the
structural layer generating the rest of the site. Traffic told me what
people used. Templates told me how the site was built. Where the
interface demanded it, I broke scope down further still — route pages,
for example, carried independent states (Schedule, Arrivals, Alerts,
More Info) that each needed separate evaluation.

*(Visual: scoping diagram — 5,000+ pages → 160 high-traffic + 29 templates)*

**BUILDING THE SYSTEM**

Manual testing dropped straight into Jira couldn't produce the
structured data a real strategy needs — it could only produce more
tickets. So I designed a four-part, reusable system: URLs → Audit →
Aggregate → Deduplicate → Analyze. An audit app turned URLs into
structured findings. An aggregator normalized results across testing
sources. A deduplicator — the pivotal piece — collapsed occurrences into
root causes, so a component failing on 100 pages became one systemic
issue, not 100 tickets. Analytics made the dataset queryable, which is
how I found the number that shaped everything after: roughly 80% of all
issues traced back to shared components.

I wasn't automating accessibility judgment — I was automating the work
around it, so manual testing time went to the ambiguous cases that
actually needed a human.

*(Visual: Audit App UI, large. Visual: Deduplicator before/after.)*

**DEFECT DEEP DIVE: THE ROUTE-PAGE TABS**

A tab component on route pages looked and worked fine visually — the
kind of thing an automated scanner passes clean. Under screen-reader
testing, activating a tab triggered a page refresh that broke the
interaction entirely; a screen-reader user couldn't move between tabs
the way the interface implied they could. I documented the actual
behavior, diagnosed why the pattern broke, and used it to teach the dev
team correct ARIA behavior going forward. A visually functional interface
can still be completely unusable — the clearest proof in the engagement
that automated scanning alone wasn't enough.

*(Visual: screen-reader tab defect — expected vs. actual)*

**THE REMEDIATION STRATEGY**

The deduplicated data showed accessibility problems followed the site's
own architecture — components, then templates, then pages — while the
Jira backlog had flattened all three into one list. I rebuilt
remediation around where a fix would actually propagate:

- **Phase 1 — "80%."** Shared components first — one fix resolved every
  page inheriting from it. Highest leverage, went first regardless of the
  existing backlog's priority order.
- **Phase 2 — "Template Pages."** Narrower blast radius, still
  propagating across every page on that template.
- **Phase 3 — "Everything Else."** The long tail of isolated findings —
  explicitly deprioritized, since fixing these first would have
  reproduced the same trap the original 7,000-ticket backlog was already
  in.

Fix once, resolve everywhere. The real move wasn't finding more issues —
it was proving "thousands of tickets" was actually a two-dozen-components
problem, and getting the client to act on that instead of the ticket
count.

*(Visual: three-phase remediation diagram)*

**OUTCOME**

Convincing the client to abandon a plan they'd already committed to in
writing took walking their team and engineering leads through the data
directly, then training developers on the underlying concepts — ARIA,
semantic structure, focus and keyboard behavior — so the reframe would
hold after I left. It did: the engagement was extended beyond its
original scope on the strength of this approach, and Sound Transit ended
with 160 pages and 29 templates instead of 5,000+ flat entries, a
dataset proving ~80% of the problem was systemic, four reusable tools
instead of a spreadsheet, and — for an agency carrying real litigation
exposure — a defensible, evidence-based plan for closing that risk, not
just a longer list of findings.
