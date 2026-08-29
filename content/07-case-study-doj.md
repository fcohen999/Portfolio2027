# Case Study — DOJ Employee Service Portal (from current site)

## Source

Transcribed from your screenshot. **Lower confidence than the others** —
several lines were too small/compressed to read with certainty, marked
`[unclear]` below. Please correct anything I misread, especially the
product acronym and the final outcome sentence.

## Current copy (as-is, for audit reference)

> Department of Justice — Automating & consolidating manual processes to
> improve efficiency
> Role: Design Lead · Timeline: 4 months
>
> The DOJ Employee Service Portal [unclear acronym] is a product created
> as part of an effort to modernize internal operations across the DOJ's
> internal tooling. [It] is a centralized platform for workforce
> management.
>
> As the product design lead, I worked with the client to create a design
> system and manage implementation across time. One of those release
> items was "Time to Hire," a robust onboarding tool that consolidated the
> recruitment process across all agencies.
>
> Utilizing integrations, auto-populating smart fields, and generation of
> documents, all in one place, this tool was created to streamline
> previously manual, tedious steps involving hundreds of staff and hours
> of work by users.
>
> [Document Generation] Generation of documents on a per-page basis allows
> for relevant fields to be pulled and filled without the user having to
> search for that information elsewhere. This [reduces] manual effort...
> allowing for [reduced] redundancy in the process.
>
> [Generated Document Download] Downloading generated pre-filled documents
> reduces friction for gathering paperwork and, more importantly, ensures
> accuracy across multiple related tasks in one place.
>
> [Reviewed Document Upload] Uploading reviewed documents directly on the
> network form provides a more organized experience, ensuring documents
> flow efficiently through the document upload process.
>
> [File Checklist] The widget also serves as a checklist of necessary
> documents for both staff and hiring managers.
>
> [Designed to reduce redundancy] The attachment upload was set up to help
> lighten load for various tasks... helping capture data [and] improving
> progress and efficiency.
>
> [Outcomes] "While this case study covers just a slice of my contribution
> to this project, it['s a] critical piece of the larger foundational...
> influence, especially in regards to the Office of the Chief Information
> Officer." [unclear — please confirm exact wording]

## Audit

- **Undersold, badly:** this is the weakest-written of your case studies
  relative to what your resume claims for the same engagement. Your
  resume says you established OCIO's entire design system foundation,
  presented to the CIO directly, and led Time to Hire within that system.
  The current case study copy reads like release notes for one feature
  (document upload/download widgets) and never mentions the design
  system, the multi-org accommodation problem, or executive presentation
  at all.
- **Feature-list structure:** Document Generation → Download → Upload →
  Checklist → "reduce redundancy" is five sections describing the same
  document-handling widget from slightly different angles. There's no
  single throughline about *why* this was hard (multi-agency process
  consolidation) or what you decided.
- **The real story is scoping, not widgets:** "consolidated the
  recruitment process across all agencies" is the actual hard problem —
  DOJ's OCIO serves domain-separated orgs with independent technical
  environments (per your resume). Reconciling that into one Time to Hire
  flow is a design-system/IA problem, not a form-widget problem. The
  current copy buries this in one sentence and spends five sections on
  UI mechanics instead.
- **Outcome is a non-answer.** "This case study covers just a slice of my
  contribution... critical piece of the larger foundational impactful
  influence" says nothing concrete. No metric, no scope number (agencies
  covered, hours saved, hires processed), no before/after.

*Flag: I need real numbers here if you have them — agencies/orgs covered
by Time to Hire, hours or steps saved per hire, hires processed, staff
size affected. The resume doesn't have JEOD-specific numbers either, so
if none exist, I'll keep the outcome qualitative but tie it explicitly to
the design-system framing instead of leaving it as filler.*

## Rewritten case study

**Eyebrow:** U.S. DOJ — Office of the CIO
**Title (H1):** One Hiring Process, Built to Work Across Agencies That Don't Share a Tech Stack
**Subhead:** Design Lead — Time to Hire, built on a design system created to hold across domain-separated DOJ organizations.

**Stat row:**
- 4 mo — Time to Hire build timeline
- 1 — shared design system, multiple independent org environments
- CIO — presented direction to DOJ executive leadership directly

**THE PROBLEM**

DOJ's recruitment process ran manually across agencies that don't share a
common technical environment — each domain-separated org has its own
systems and constraints. Onboarding involved hundreds of staff hours
spent chasing documents, re-entering the same information across
disconnected steps, and manually assembling paperwork with no shared
source of truth. Consolidating that into one process meant designing
something that had to hold up across environments that weren't built to
talk to each other.

**MY ROLE**

I came in as Design Lead responsible for establishing OCIO's product
design foundation — shared components, interaction patterns, and
accessibility standards — that other teams could build on. Time to Hire
was the first major feature built on top of that foundation, and I
presented the direction, including this system, directly to DOJ executive
leadership, including the CIO.

**APPROACH**

The foundation had to solve a harder problem than any single feature:
create one common design language flexible enough to work across
independently-run technical environments, without forcing every domain
org onto identical infrastructure. I designed it to be cloned and adapted
rather than assuming any org could just adopt it wholesale — the reuse
model had to match how DOJ's orgs actually operate, separately.

Time to Hire applied that foundation to the recruitment process
specifically: integrations, auto-populating smart fields, and in-place
document generation replaced steps that previously required staff to
gather the same information from multiple disconnected systems by hand.
Generated documents could be downloaded pre-filled, reviewed copies
uploaded back into the same flow, and a built-in checklist tracked what
both staff and hiring managers still needed to provide — collapsing what
had been a multi-system, manually-tracked process into one place.

**OUTCOME**

Time to Hire shipped as the first feature built on OCIO's new design
foundation, consolidating a previously manual, multi-agency recruitment
process into a single flow — and proving the underlying system could
actually hold across DOJ's independently-run technical environments, not
just work as a one-off feature.

*(Flag: please correct the product acronym I couldn't read clearly, and
give me any real numbers — agencies covered, hours saved, hires
processed — if they exist. Right now the outcome stays qualitative
because I don't have them.)*
