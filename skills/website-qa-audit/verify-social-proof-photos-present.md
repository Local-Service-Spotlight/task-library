---
name: verify-social-proof-photos-present
description: Confirms social proof sections show real photographic evidence — client photos, job results, event shots — not text-only claims that anyone could type.
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify social proof photos present

**Use this when** running Layer 2 (Content Architecture Checks) of the Website QA Audit — text-only proof is just a claim; photos make it evidence.

## Inputs
- Site URL with the social proof sections identified (testimonials, results, logos, press, reviews)
- The no-stock verification method (reverse image search) from earlier checks
- The audit report/spreadsheet for logging results

## Steps
1. Locate every social proof element on the site: testimonial blocks, results/case-study sections, client logo strips, press mentions, review embeds.
2. For each, record whether it includes a real photo or visual artifact — client headshot, before/after job photo, screenshot of an actual review or analytics result, event photo.
3. Fail any social proof section that is text-only (quotes with no faces, claims with no captures).
4. Verify the photos are real: reverse-search suspect headshots; a "client" who appears on stock sites fails the section.
5. Confirm visuals match the claim — a review screenshot must show the named platform and reviewer, a results image must show the metric claimed, and an event or meal photo must match the named people and setting. A photo proves the depicted moment; it does not by itself prove friendship, partnership, mentorship, client status, or endorsement.
6. Read the public caption and surrounding copy. Pass a compact receipt that identifies the person, scene/event, date when known, source link, and useful lesson. Fail a trophy-name wall, name-dropping caption, or paragraph that explains at length what the evidence does or does not prove.
7. Verify every quote attached to the visual is exact and comes from the named person. A logo, domain, company name, initials, first name, or "happy customer" is not testimonial attribution; keep that item HOLD until full attribution, source, and any required permission exist.
8. Fail public confidence scores, proof-record IDs, inventory/harvester labels, and repurposing instructions when those systems are not the page's topic. Preserve a materially necessary legal, regulatory, or compliance disclosure and scope it to the triggering claim.
9. Log each social proof element, its visual evidence, caption, and verdict in the internal audit report.

## Definition of done (QA checklist)
- [ ] Every social proof section includes at least one real photo or screenshot artifact — zero text-only proof blocks
- [ ] All proof photos verified non-stock and consistent with the claims they support
- [ ] Captions show a real scene and useful lesson with a compact receipt; no trophy-name wall, inflated relationship noun, or repeated defensive caveat
- [ ] Every attached quote is exact, named, attributable, and source-linked; anonymous/domain-only praise remains HOLD
- [ ] Zero public internal scoring/inventory/repurposing metadata; any retained legal/compliance disclosure is materially necessary and scoped
- [ ] Element-by-element verdicts logged in the audit report, linked back to /website-qa-audit

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run.

## Run on a persistent agent (Fable 5)
A persistent Fable 5 agent (or comparable OpenAI/Google model) sweeps every social proof element across the entire site — every testimonial block, results section, logo strip, and review embed — verifying each carries real photographic evidence, and loops until zero text-only proof blocks remain anywhere.
Memory tracks each proof element's verdict, so re-runs only inspect new or edited blocks, and any new testimonial added without a photo re-opens the check automatically.
Each run logs one worked example to ## Example(s), compounding the library.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /website-qa-audit
- Related: /blog-posting-guidelines (real images only) · previous: check-each-homepage-section-includes-relevant-image · next check: verify-testimonials-include-headshots-with-attribution
