---
name: verify-testimonials-include-headshots-with-attribution
description: Checks that every testimonial on the site pairs a real headshot with a name and attribution, so praise is visibly from real people.
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify testimonials include headshots with attribution

**Use this when** running Layer 2 (Content Architecture Checks) of the Website QA Audit — an anonymous quote with no face reads as invented.

## Inputs
- Site URL with all testimonial placements identified (homepage, services pages, dedicated testimonials page)
- Google Images reverse search for headshot verification
- The audit report/spreadsheet for logging results

## Steps
1. Inventory every testimonial across the site, including sliders and carousels (advance them — hidden slides count).
2. For each testimonial, check for a headshot: a real photo of the actual person quoted, not an initials avatar, a logo, or a stock face.
3. Check for attribution: at minimum the person's real full name; flag "J.D.", "Happy Customer", first-name-only entries, and a company/domain presented without a named speaker.
4. Reverse-search any headshot that looks like a stock model — a stock face on a testimonial fails the whole block's credibility.
5. Where headshot or attribution is missing, note what to collect from the client (photo permission, full name, exact source quote) as the fix. Keep the praise HOLD and off the public testimonial block until those fields are verified.
6. Log each testimonial with headshot and attribution verdicts in the audit report.

## Definition of done (QA checklist)
- [ ] 100% of testimonials display a real, non-stock headshot of the person quoted
- [ ] 100% of testimonials carry at least a verifiable full name — zero anonymous, initials-only, first-name-only, or domain/company-only quotes
- [ ] Incomplete praise is marked HOLD and is not rendered as a testimonial
- [ ] Testimonial inventory logged in the audit report, linked back to /website-qa-audit

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run.

## Run on a persistent agent (Fable 5)
A persistent agent (Fable 5 / comparable OpenAI or Google models) inventories every testimonial site-wide — advancing every slider and carousel so hidden slides count — verifies headshot and full name on each, reverse-searches every face, and loops collect-and-recheck until 100% pass with zero anonymous or stock-faced entries.
Memory keeps the testimonial inventory with verdicts, so re-runs only audit testimonials added or changed since the last pass.
Each run logs one worked example to ## Example(s) so the audit library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /website-qa-audit
- Related: Layer 3 sibling: verify-testimonials-with-full-attribution (the stricter trust-level pass) · previous: verify-social-proof-photos-present · next check: check-lead-magnet-section-has-visual-mockup
