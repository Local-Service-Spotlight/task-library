---
name: kill-underperformers-scale-winners
description: Act on the weekly diagnosis — cut campaigns and content that miss target, and gradually increase investment in what works — so budget continuously migrates toward proof.
category: Strategy & Measurement
stage: —
definitive_article: /9-triangles-framework-scalable-home-service-businesses/
status: complete
---

# Kill underperformers, scale winners

**Use this when** the weekly MAA analysis is done and it's time to act — this is the Action corner of the MAA triangle, executed without sentiment.

## Inputs
- The diagnosed underperformer list and the winners list (from the MAA analysis)
- Target cost per result (CPA/ROAS) per item, from the GCT/Stage 2 goals
- Ad account and publishing access to actually pause, edit, and re-budget

## Steps
1. Set the kill rule before looking at favorites: anything past its evaluation window and above target cost per result gets cut. Sunk cost is not an argument; the ad spend is gone either way.
2. **Kill:** pause every flagged underperformer now — don't taper "to be safe." If the diagnosis was fixable (creative/targeting/offer) and it hasn't had its one retry, relaunch the fixed variant as a new test instead of letting the old one run.
3. **Scale winners gradually:** increase budget on items beating target — but no more than 2× per adjustment (per /dad), because abrupt jumps reset delivery optimization and can break what was working.
4. Extend winners sideways as well as up: apply winning creative to new audiences via switch boosts, and feed proven content into the 90% greatest-hits pool.
5. Reallocate the freed budget from kills to the scaled winners the same day, so total spend keeps working instead of idling.
6. Log every kill and scale decision — item, metric, threshold, action, date — in the Friday MAA report; next week's first check is whether the scaled winners held their cost per result.

## Definition of done (QA checklist)
- [ ] Every diagnosed underperformer paused (or relaunched as a fixed variant) — none left running on hope
- [ ] No winner's budget increased more than 2× in a single adjustment
- [ ] Freed budget reallocated to winners, not left unspent
- [ ] Every action logged with item, metric, threshold, and date in the MAA report
- [ ] Scaled winners flagged for next week's first review
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run. (The hub at /9-triangles-framework-scalable-home-service-businesses/ links live examples; pull the closest match into this slot.)

## Run on a persistent agent (Fable 5)

A persistent, max-effort agent (Claude Fable 5 or comparable OpenAI/Google models) executes the Action corner without sentiment: it pauses every flagged underperformer the same day, scales winners no more than 2× per adjustment, and loops until the Definition of done fully passes — nothing left running on hope, freed budget reallocated, every decision logged with item, metric, threshold, and date.
It self-verifies by re-reading the ad account state after acting to confirm the pauses and budget changes actually took.
Memory closes the loop as a true MAA memory cycle: next run opens by checking whether last week's scaled winners held their cost per result versus prior periods, and a meta-article example is logged each run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /9-triangles-framework-scalable-home-service-businesses/ (parent methodology: /maa)
- Related, in run order: analyze-why-underperformers-fail, content-strategy-90-greatest-hits-10-new, submit-weekly-maa-report-every-friday, /dad
