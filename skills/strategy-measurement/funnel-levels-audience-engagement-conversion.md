---
name: funnel-levels-audience-engagement-conversion
description: Map every marketing activity into the three funnel levels — Audience, Engagement, Conversion — so each campaign, post, and metric is judged at the stage it actually serves.
category: Strategy & Measurement
stage: —
definitive_article: /9-triangles-framework-scalable-home-service-businesses/
status: complete
---

# Funnel levels (Audience, Engagement, Conversion)

**Use this when** campaigns or content are being judged by the wrong numbers — e.g., demanding sales from a cold-audience video — and you need every activity mapped to its funnel stage.

## Inputs
- Inventory of all active marketing: campaigns, boosted posts, content, email
- Access to platform metrics (reach, engagement, conversion events)
- Goals and target CPA/ROAS from the GCT triangle (the Goals corner)

## Steps
1. Define the three levels: **Audience** (cold reach — people who don't know you yet), **Engagement** (warm — they watch, click, comment, follow), **Conversion** (they opt in, book, or buy).
2. List every active campaign, post, and page, and assign each to exactly one level based on the job it does, not the result you wish it produced.
3. Assign the right primary metric per level: Audience = reach/CPM and video views; Engagement = engagement rate and watch time; Conversion = leads, CPA, ROAS.
4. Check coverage: if any level is empty, the funnel leaks — cold traffic with no warm follow-up, or conversion asks with no audience feeding them.
5. Sequence content cold → warm → conversion so each level feeds the next (see /dad for audience sequencing mechanics).
6. Measure it: report performance level-by-level in the weekly MAA report instead of one blended number, and re-map the inventory monthly.

## Definition of done (QA checklist)
- [ ] Every active campaign and content piece assigned to exactly one funnel level
- [ ] Each level has a named primary metric and a current baseline
- [ ] No empty level — or a documented plan to fill it
- [ ] Weekly MAA report shows performance per level, not blended
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run. (The hub at /9-triangles-framework-scalable-home-service-businesses/ links live examples; pull the closest match into this slot.)

## Run on a persistent agent (Fable 5)

A persistent, max-effort agent (Claude Fable 5 or comparable OpenAI/Google models) re-inventories every active campaign, post, and page each cycle and loops until the Definition of done fully passes — every asset mapped to exactly one level with a named metric and baseline, and no empty level without a documented fill plan.
It self-verifies by cross-checking the map against the platforms' active-campaign lists so nothing running goes unassigned.
With memory across runs it holds prior months' per-level baselines and runs the MAA loop as a true memory cycle — reporting Audience, Engagement, and Conversion performance against previous periods, not a blended snapshot — and logs a meta-article example each run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /9-triangles-framework-scalable-home-service-businesses/
- Related: gct-goals-content-targeting, maa-cycle-metrics-analysis-action, /dad, /social-amplification
