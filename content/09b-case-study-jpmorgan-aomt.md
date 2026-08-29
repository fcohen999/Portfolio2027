# Case Study — J.P. Morgan Asset Outage Modeling Tool (from current site)

## Source

Transcribed from your PDF export. High-confidence transcription (real
text layer, not a screenshot) — the only artifact is the PDF's font
encoding rendering every "t" as "!", which I've corrected below.

## Current copy (as-is, for audit reference)

> J.P. Morgan & Chase — A tool for financial analysts to simulate the
> impact of essential service outages.
> Role: Reporting and Analytics Lead
> Timeline: 8 months
> Team: Bill Hess (Design Lead), Meghan Hensley (Disaster Management
> Specialist), Eric Albright (PM)
>
> The J.P. Morgan & Chase Asset Outage Modeling Tool, or AOMT, assists
> analysts with emergency and disaster preparation planning and
> compliance. It is used by disaster management teams to model outage
> scenarios and identify potential cascading failure modes for critical
> financial infrastructure.
>
> AOMT automates common risk analysis workflows and calculations, freeing
> up valuable mindshare for analysts to focus on creating precise and
> thorough strategic plans.
>
> I worked end-to-end, from strategy, to scoping and design, to final
> delivery, guiding the reporting & analytics work stream and
> communicating with the client.
>
> [Research] The early stages of this project focused on extensive domain
> and user research to understand the disaster management landscape,
> including the specific challenges and requirements of J.P. Morgan's own
> disaster management team. This involved user interviews, workflow
> observation sessions, and studying government regulations for disaster
> readiness.
>
> [Scoping the work] Understanding existing workflows, regulatory
> requirements, and individual users was crucial for scoping the design
> work. Through my research, I was able to infer additional feature
> requirements and optimize the layout and interactions based on the
> needs of real analysts. I worked closely with the product owner to
> gather and understand business requirements and with a disaster
> management specialist to prioritize features.
>
> [Six requirement callouts: Navigation, Custom Inputs, Panel Access,
> Affected Items Display, Bi-directional Linkages, Drill-ins & Downloads
> — each a one-line "to do X, the tool needed Y" statement]
>
> [Workflow] This workflow centers on two tasks: 1. Performing a search
> for various assets or compliance criteria, to view an overview of the
> model. 2. Mapping the interdependencies of the resulting data, to
> understand potential cascading failures.
>
> [Example scenario] To remain focused on a real use case while designing
> the interface, I focused on a hypothetical scenario: "As a disaster
> management analyst, I've been tasked with modeling potential
> disruptions to Florida's critical infrastructure in the 2024 hurricane
> season, so I can prepare a strategic overview of our preparedness
> plans." Working against this scenario made it easier to generate
> accurate notional data to present to the client, and helped me
> understand outage modeling enough to create the scope for design and
> implementation.
>
> [Step-by-step workflow diagram: Add Criteria → Click Create Model →
> Review Model → Inspect ranked direct impacts → Click on number to open
> modal → Download data table(s) → Select row to begin inspecting
> dependencies → Use Dependencies Selector → Review generated
> dependencies table(s) → Open downloaded data tables in Excel]
>
> Analysts need to modify their models without starting from scratch,
> viewing in real-time the impact their criteria modification would
> cause. To enable this workflow, I pushed for a two-pane layout allowing
> analysts to reactively refine search queries and filters by interacting
> with the dependency pane.
>
> [Core workflows]
> 1. Performing searches with the criteria panel — always visible on the
>    left-hand side, with tabs to flip between selecting criteria,
>    applying filters, and viewing dependencies.
> 2. Mapping impacts with the dependency selector — ranks affected assets
>    by severity, displaying the chain reaction of potential disruptions
>    in an interactive tree, exported to Excel for broader analysis.
> 3. Moving into Excel with data table downloads — most users would
>    export data to Excel, so this integrated approach streamlines tool
>    adoption while amplifying analytics capabilities.

## Audit

- **This is your best-documented case study on process, and it should
  stay that way** — real research methods named (interviews, workflow
  observation, regulatory study), a grounding hypothetical scenario, and
  a genuine design decision (two-pane reactive layout) with a stated
  reason. Don't lose any of this in the rewrite; tighten framing only.
- **Missing stakes.** The copy explains what AOMT does and how it was
  built, but never states what happens without it — what exposure or
  risk J.P. Morgan carries if outage modeling is slow or wrong. One
  sentence naming the stakes (compliance risk, response time in an actual
  disaster) would make the "why this mattered" case much stronger.
- **The six requirement callouts read like a features spec**, not
  positioned as your design reasoning — each is written as "to do X, the
  tool needed Y" (passive, from the tool's perspective) rather than "I
  decided Y because X." Small rewrite, real improvement.
- **Team context underused:** you're credited as Reporting and Analytics
  Lead with a named Design Lead (Bill Hess) and named specialists on the
  team — worth stating plainly that you owned a specific workstream
  within a larger team, since that's actually a more precise, more
  credible seniority signal than an unscoped "I designed this."

## Rewritten case study

**Eyebrow:** JPMorgan Chase
**Title (H1):** Modeling Cascading Infrastructure Failure, Grounded in One Analyst's Real Workflow
**Subhead:** Reporting &amp; Analytics Lead — the Asset Outage Modeling Tool, built with a 3-person team over 8 months.

**Stat row:**
- 8 mo — engagement timeline
- 2 — core workflows the entire tool was scoped around
- 3 — person team (Design Lead, Disaster Management Specialist, PM)

**THE PROBLEM**

J.P. Morgan Chase's disaster management team needed to model the impact
of essential service outages and cascading failures across critical
financial infrastructure — the kind of scenario planning that directly
feeds emergency preparation and regulatory compliance. Without a
purpose-built tool, that analysis relied on manual, calculation-heavy
workflows that ate into the time analysts should have spent on the
actual strategic judgment calls.

**MY ROLE**

I served as Reporting and Analytics Lead, working end-to-end from
strategy through scoping, design, and final delivery, on a team with a
Design Lead (Bill Hess), a Disaster Management Specialist (Meghan
Hensley), and a PM (Eric Albright). My workstream owned the reporting and
analytics side of the tool and the client relationship for that stream
directly.

**APPROACH**

I grounded the research in the disaster management team's actual
workflow rather than assumptions: user interviews, workflow observation
sessions, and a direct study of government disaster-readiness
regulations, specifically to understand how dependencies between assets
work in practice. That research surfaced a two-task core workflow —
search across assets and compliance criteria, then map the
interdependencies between them to expose cascading failure risk — and I
used a concrete hypothetical scenario (modeling hurricane-season
disruption to Florida's infrastructure) to keep every design decision
tied to a real use case instead of an abstraction.

From that research, I made a specific interaction call: analysts needed
to adjust their models without starting over, watching the impact of a
criteria change in real time. That requirement drove a two-pane layout —
criteria selection always visible on one side, the dependency view
reacting live on the other — rather than a linear wizard-style flow that
would have forced analysts to commit to criteria before seeing any
impact. Because most analysts' actual workflow ended in Excel, I made
data-table export a first-class action throughout, not an afterthought
bolted onto the end.

**OUTCOME**

AOMT gave J.P. Morgan's disaster management analysts a tool that
automated the calculation-heavy parts of outage modeling, so their time
went toward strategic judgment instead of manual analysis — while
integrating with the Excel-based habits analysts already had, rather
than asking them to abandon their existing workflow.

*(Flag: if you have anything on actual usage or time savings after
launch — analysts using it, time saved per model, compliance outcomes —
that would strengthen the outcome section considerably; right now it
stays close to the original copy's scope since no post-launch numbers
were in your source material.)*
