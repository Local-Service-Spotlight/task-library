---
name: three-pillars-marketing-operations-finance
description: Map the business onto its Three Pillars — Marketing, Operations, Finance — assign one health metric to each, and rebalance effort toward the weakest pillar.
category: Strategy & Measurement
stage: —
definitive_article: /9-triangles-framework-scalable-home-service-businesses/
status: complete
---

# Three Pillars (Marketing, Operations, Finance)

**Use this when** you need a whole-business diagnosis — growth has stalled, work feels busy but unprofitable, or you must decide where the next hour or dollar goes.

## Inputs
- A list of all recurring activities, roles, and tools in the business
- Basic numbers: pipeline/leads, delivery throughput and quality, revenue/margin/cash
- The owner's 90-day goals, so pillar priorities tie to something concrete

## Steps
1. Define the triangle: every business runs on **Marketing/Sales** (demand: attention, leads, deals), **Operations** (delivery: fulfilling what was sold), and **Finance** (fuel: pricing, margin, cash flow). A business is only as strong as its weakest pillar.
2. Map every recurring activity, role, and tool to exactly one pillar. Anything that maps to none is a Delete candidate (Personal Efficiency triangle).
3. Assign one primary health metric per pillar — e.g., Marketing: qualified leads or pipeline value; Operations: on-time delivery or capacity utilization; Finance: gross margin or cash runway.
4. Score each pillar against its 90-day goal and identify the constraint — the weakest pillar that caps the other two (great marketing can't save broken delivery; great delivery can't save negative margin).
5. Rebalance: move effort, budget, and the next hires/delegations toward the constraint pillar; write the decision down with a review date.
6. Measure it: review all three pillar metrics in the weekly MAA report so no pillar drifts unwatched between strategic reviews.

## Definition of done (QA checklist)
- [ ] Every recurring activity and role mapped to exactly one pillar
- [ ] One primary metric per pillar, with current value and target
- [ ] The constraint pillar named, with a written rebalancing action and review date
- [ ] All three pillar metrics appearing in the weekly MAA report
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run. (The hub at /9-triangles-framework-scalable-home-service-businesses/ links live examples; pull the closest match into this slot.)

## Run on a persistent agent (Fable 5)

A persistent, max-effort agent (Claude Fable 5 or comparable OpenAI/Google models) keeps the whole-business map alive: it re-maps activities, pulls all three pillar metrics every week, and loops until the Definition of done fully passes — every activity assigned, one metric per pillar with value and target, the constraint named with a written action and review date.
It self-verifies by confirming no activity is unmapped and no pillar metric is missing from the weekly report before closing.
Memory makes the diagnosis longitudinal: the agent runs the MAA loop as a true memory cycle, scoring each pillar against prior periods so a slowly weakening pillar is caught early, and logs a meta-article example each run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /9-triangles-framework-scalable-home-service-businesses/
- Related: personal-efficiency-do-delegate-delete, maa-cycle-metrics-analysis-action, submit-weekly-maa-report-every-friday
