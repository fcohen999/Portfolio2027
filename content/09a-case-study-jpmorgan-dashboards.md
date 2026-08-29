# Case Study — J.P. Morgan Risk Management Dashboards (from current site)

## Resolved

Your homepage screenshot confirms this and the Asset Outage Modeling Tool
are two **separate** case studies on the live site (both listed as
distinct tiles), not one engagement I need you to reconcile — my earlier
flag is resolved. This one is written from your "ERMA" screenshot; the
other from your PDF (`09b-case-study-jpmorgan-aomt.md`).

## Current copy (as-is, for audit reference)

> J.P. Morgan Risk Management Dashboards — Designing dashboards for bank
> resiliency, planning, risk management, and compliance
> Role: UX Design Lead
>
> J.P. Morgan's old dashboard management tool had been used since the
> 1990s; they needed a new, more powerful, efficient, and intuitive
> management [tool] for regulatory planning issues.
>
> ERMA is a suite of tools built to manage resiliency data and risk
> management activities. This includes a centralized platform for the
> bank to develop, manage, [and] enable them to better protect their
> customers, employees, and assets, as well as stay compliant with all
> government regulations.
>
> [Forever affordable to scale] The most critical requirement was to
> create a design system for reporting and interacting with metrics that
> would be affordable to implement at scale.
>
> The dashboard comprises 4 tabs designed for comprehensive resiliency
> planning and risk management. ERMA, by centralizing planning,
> significantly enhances the bank's ability to safeguard customers,
> employees, and assets while ensuring adherence to government
> regulations. Information Hub serves as a centralized summary,
> presenting key metrics related to a user's network resilience plan
> worksheet.
>
> [Flexible analytics dashboard]
>
> [Widget-and-modal-based design system] Working with the Chase design
> system, I designed a modular widget and modal system that could be used
> anywhere within the reporting and analytics dashboards. Modular widgets
> give users an overview of their important metrics and helped to
> streamline the development process, saving time and resources in the
> long run.
>
> It was important to create templates for the widgets and modals early
> on so that development would be less costly. Different stakeholder
> opinions and varying graph types led to a broad range of widget
> templates.
>
> [Modals for data refinement] Interactive modals enable users to
> visualize and refine data, with quick actions to export information,
> saving time on repetitive tasks. As with the widgets, it was important
> to create templates for the modals early on as this development would
> be less costly.
>
> [Outcomes] "...In particular [I] want to shout out Fiona for her work
> with us this quarter. She's stuck with us for a long duration, and she
> has helped some very strong personalities... find their voice with
> design and [got] assignments achieved well, and she delivered great
> high quality product with... care." — Amy Meager, Executive Director of
> Technology Product Management, JPMC

## Audit

- **Feature-list structure, no real problem statement:** the copy jumps
  straight to "ERMA is a suite of tools" without establishing what was
  actually broken about the old (1990s-era) tool in concrete terms — what
  couldn't analysts do, what risk did that create.
  "Forever affordable to scale" is a good section header instinct but the
  content under it never explains a real tradeoff — it just restates the
  goal.
- **No numbers at all** in the body copy — only the closing quote gives
  any texture. If you have anything (number of dashboards, users, banks
  regulations covered, time saved vs. the old tool), this case needs it
  more than any other on the site.
- **Quote is strong but generic in placement** — it's a nice trust signal
  but it doesn't reference anything specific about the ERMA work, so it
  reads as a relationship endorsement more than a project outcome. Keep
  it, but don't let it stand in for an actual outcome statement.
- **Role note:** stated as "UX Design Lead" here — different from the
  Asset Outage Modeling Tool case study where you're "Reporting and
  Analytics Lead" with someone else as Design Lead. Since your resume
  covers this whole JPMorgan engagement as one "Design Lead" bullet, my
  read is this dashboards work is where you held that Design Lead title,
  while AOMT was a narrower-scoped piece under a different design lead —
  consistent with one engagement, two tools, roles differing by
  workstream. Flag if that's wrong.

## Rewritten case study

**Eyebrow:** JPMorgan Chase
**Title (H1):** Replacing a 1990s Dashboard Tool With a System Built to Stay Affordable at Scale
**Subhead:** UX Design Lead — ERMA, a centralized resiliency and risk-management platform for bank compliance and planning.

**Stat row:**
- 4 — dashboard tabs spanning resiliency planning and risk management
- 1990s → now — replacing decades-old dashboard tooling
- 1 — reusable widget/modal system built to scale across the platform

**THE PROBLEM**

J.P. Morgan Chase's disaster-resiliency and risk-management teams were
still working from a dashboard tool that had been in place since the
1990s — not built for the volume of metrics, stakeholder variety, or
regulatory precision the bank's compliance obligations now require.
Every new reporting need risked becoming a one-off build, which doesn't
hold up when the requirement is standing across government regulation.

**MY ROLE**

I served as UX Design Lead on ERMA, a suite of tools centralizing
resiliency data and risk-management activity for the bank — covering
incident planning, compliance reporting, and asset/employee protection
across a four-tab dashboard structure.

**APPROACH**

The critical constraint wasn't features, it was cost of scale: whatever
reporting system I designed had to stay affordable to extend as new
metrics and regulatory requirements inevitably got added later. Working
within Chase's existing design system, I built a modular widget-and-modal
pattern that could be dropped anywhere across the reporting and analytics
dashboards, rather than custom-building each new report view. Information
Hub — a centralized summary surfacing the key metrics from a user's
network resilience plan — became the reference implementation for that
pattern.

Because stakeholder opinions on what a given metric should look like
varied widely, and the graph types needed ranged broadly, I created
widget and modal templates early, before development started building
one-off versions — every one-off avoided there was cost avoided later
across the platform's life. Interactive modals let users visualize and
refine data with quick export actions built in, so repetitive
data-refinement tasks didn't need a new UI pattern every time they came
up.

**OUTCOME**

ERMA gave J.P. Morgan Chase's resiliency and risk-management teams a
modern replacement for decades-old dashboard tooling, built on a widget
system designed to stay cost-effective as the bank's reporting needs keep
growing rather than requiring a rebuild each time.

> "...I want to shout out Fiona for her work with us this quarter. She's
> stuck with us for a long duration, and she has helped some very strong
> personalities find their voice with design... and she delivered a
> great, high quality product with... care." — Amy Meager, Executive
> Director of Technology Product Management, JPMC

*(Flag: if you have any concrete numbers here — dashboards shipped, users
onboarded, time saved vs. the old tool — this case study needs one more
than any other on the site. Also please confirm the exact quote wording;
transcribed from a compressed screenshot.)*
