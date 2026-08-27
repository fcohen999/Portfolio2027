# Case Study — Merck Pharmaceuticals (from current site)

## Source

Transcribed from your screenshot. Confident transcription — legible
throughout.

## Current copy (as-is, for audit reference)

> Merck Pharmaceuticals — Uncovering correlations in social and
> healthcare data to improve HPV vaccination coverage in under-served
> communities
> Role: Product Designer · Timeline: 1 month · Team: Josie (Design Lead), Madison (Brand Design)
>
> Merck's HPV Vaccination Explorer is a geospatial research and analytics
> tool used by healthcare researchers to better understand the factors
> that affect vaccination coverage rates. The insights provided by this
> tool are also used by marketers to improve awareness and access to
> information about vaccines in areas with low coverage rates.
>
> Through user research, we learned that researchers used a range of data
> points to understand why specific communities had low vaccination
> rates. Among these reasons are lack of awareness, misinformation, and
> lack of mobility or access to vaccination sites.
>
> To enable these multi-faceted insights, I designed a map-focused layout
> that provides quick actions to filter and overlay multiple data sources
> on the map at once.
>
> [Breaking down data] One design challenge was how to present multiple
> datasets in a way that matches the mental model of researchers. Through
> user interviews, I learned that the data could be broken into two
> categories: qualitative medical data (like sex, age, and infection
> rates) and qualitative social data (like income, education level, and
> vaccine site accessibility).
>
> Quantitative medical data is exposed as filters on the left, and
> dynamic data displays overlaying the map. Qualitative information, also
> called "social determinants of health," are always visible on the right
> side, making them easy to cross-reference.
>
> [Drill-ins & choropleths] Researchers need to view this data at
> different levels of granularity (state, county, and area code). To
> support this workflow, I introduced a choropleth visualization. This
> was useful because it made it easy for researchers to identify
> under-served areas visually, doubling as a form of heatmap. By clicking
> on a cell, researchers can easily drill down to view detailed data
> about the most underserved areas.
>
> [Data overlays] At any point, a user can overlay additional data
> points, such as Vaccine Administer Locations, to uncover correlations
> between societal and physical metrics.
>
> [Social Determinants of Health Panel] A user can view additional,
> non-medical factors in the right panel and get an overview of how the
> selected area and applied filters compare to larger areas, but they can
> also use the map view toggle to overlay that data directly onto the map
> canvas, adding yet another layer of possible hidden insights.
>
> [Outcomes] COVID-19 meant a necessary change in priorities for Merck,
> pausing this project before it could be built. Even so, Merck's team
> sent over some glowing feedback:
>
> "[Final] deliverables are OUTSTANDING! I have enjoyed working on this
> project with this team and have learned so much. I remain optimistic
> that future projects are in store." — Carl E. Johnson, Director of
> Outcomes Research, Merck
>
> Because of the trust we were able to earn with Merck through the design
> process, they later returned to kick off several more projects,
> resulting in upwards of $500,000 of new contracts.

## Audit

- **This is a genuinely strong case study already** — it has a real
  design decision (splitting quantitative medical data from qualitative
  social determinants, and why), a specific visualization choice
  (choropleth, and the reasoning), and a real outcome number ($500K in
  follow-on contracts) plus a named client quote. Keep the structure;
  tighten the framing and surface the number earlier.
- **The COVID pause is an asset, not a weakness — but it's introduced
  apologetically.** "COVID-19 meant a necessary change in priorities...
  pausing this project before it could be built" reads like an excuse.
  Reframed, it's actually a strong signal: the work was good enough that
  a client whose own project got shelved by a global pandemic still came
  back with $500K in new work. That's a story about earned trust
  surviving a bad outcome, which is a more senior narrative than "this
  one shipped and everyone was happy."
- **Timeline (1 month) is worth stating plainly rather than omitting** —
  a well-reasoned data-model decision and a full visualization system in
  one month is a fast turnaround worth being explicit about, not hiding.
- **Team credit:** Josie (Design Lead) and Madison (Brand Design) are
  named — good practice, keep it, and it correctly positions your role
  here as Product Designer within a small team rather than overclaiming
  sole ownership.

## Rewritten case study

**Eyebrow:** Merck — Product Designer
**Title (H1):** A Project COVID Shelved — and a Client Who Came Back With $500K in New Work Anyway
**Subhead:** Product Designer, on a 3-person team — a geospatial tool for understanding HPV vaccination coverage gaps in under-served communities.

**Stat row:**
- 1 mo — from research to final deliverable
- 2 — data categories unified in one map view (medical + social determinants)
- $500K+ — in new Merck contracts after this project was shelved

**THE PROBLEM**

Merck needed to understand *why* HPV vaccination coverage was low in
specific communities — not just where, but which combination of factors
(awareness, misinformation, mobility, access to vaccination sites) was
actually driving the gap in each place. Healthcare researchers needed a
tool that could hold both medical data and social/community data at once,
and let them cross-reference the two, since neither alone explained the
coverage patterns Merck was seeing.

**MY ROLE**

I worked as Product Designer on a 3-person team (Design Lead, Brand
Design) to design a geospatial research and analytics tool — the HPV
Vaccination Explorer — built for healthcare researchers first, with
downstream use by Merck's marketing team to target awareness efforts in
low-coverage areas.

**APPROACH**

The core design decision came out of user interviews: researchers'
mental model split the data into two distinct categories — quantitative
medical data (sex, age, infection rates) and qualitative social data,
often called social determinants of health (income, education level,
vaccine site accessibility). I designed the interface around that exact
split rather than a generic filter panel: medical data became filters on
the left with dynamic map overlays, while social determinants stayed
permanently visible on the right, so researchers could cross-reference
the two without losing either from view.

Because researchers needed to move between state, county, and area-code
granularity, I introduced a choropleth visualization — which let them
visually spot under-served areas at a glance, functioning as a heatmap,
while still supporting drill-down into the specific data behind any given
area. On top of that base layer, users could add further overlays (like
vaccine administration locations) to test correlations between social
and physical factors directly on the map, with a toggle to bring the
social determinants panel data directly onto the map canvas for a
combined view.

**OUTCOME**

COVID-19 forced Merck to shelve this project before it went into
development — but the research and design work was strong enough that
the client came back anyway. Merck's Director of Outcomes Research called
the deliverables "outstanding," and the trust built through that one-month
engagement led directly to Merck returning for additional projects,
generating $500K+ in new contracts.

> "[Final] deliverables are OUTSTANDING! I have enjoyed working on this
> project with this team and have learned so much. I remain optimistic
> that future projects are in store." — Carl E. Johnson, Director of
> Outcomes Research, Merck
