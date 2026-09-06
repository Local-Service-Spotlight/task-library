---
name: create-clear-conversion-path
description: Build one obvious, trackable path from landing to conversion (call, form, or booking) so visitors never wonder what to do next.
category: Digital Plumbing
stage: —
definitive_article: /digital-plumbing
status: needs-work
---

# Create Clear Conversion Path

**Use this when** the site gets traffic but few leads, CTAs compete or dead-end, or a visitor landing on any page can't reach the conversion in two clicks.

## Inputs
- The primary conversion action, decided with the owner per GCT Goals: call, form, or booking — pick one as primary
- Website edit access
- Working contact form and click-to-call links (run those skills first)

## Steps
1. Define the one primary conversion (GCT: Goals before Content before Targeting). Everything else — newsletter, socials — is secondary and must look secondary.
2. Map the current paths: from the homepage and each major landing page, count the clicks to complete the conversion. Target: two clicks or fewer from anywhere.
3. Put one primary CTA above the fold on the homepage and every service page — specific verb, specific outcome ("Get a fence quote," not "Learn more").
4. Repeat the CTA at natural decision points down the page and in the header (button) so it's always one tap away on mobile.
5. Remove or demote competing CTAs and fix dead ends — every page must link onward toward the conversion, and every button must route to the right destination.
6. Confirm the conversion completes with a trackable end state (thank-you page/message firing GA4 + pixel events).
7. Walk the path on a phone as a cold visitor: land on a blog post, find your way to converting. If you hesitate anywhere, fix that step.

## Definition of done (QA checklist)
- [ ] Each money-page opening makes the customer's situation, supported value and next buying step clear in the first 2–3 sentences, with relevant authentic proof; `step-7-write-hook-and-establish-context` review is recorded, not inferred from a CTA or unmeasured conversion promise
- [ ] One primary conversion defined and documented (GCT)
- [ ] Conversion reachable in ≤2 clicks from the homepage and every service page
- [ ] Primary CTA visible above the fold on home and service pages, on mobile
- [ ] Every CTA button routes to its correct destination; no dead ends on the path
- [ ] Conversion end state fires tracking events (GA4, pixel)
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run.

## Run on a persistent agent (Fable 5)
A persistent agent (Claude Fable 5 or a comparable OpenAI/Google model) walks the path like a cold visitor from every entry page, fixes each dead end or hesitation, then walks it again — looping until the whole Definition of done passes (≤2 clicks, tracked end state), not 90%.
It self-verifies against that checklist on a phone-sized view, holds the chosen primary conversion and page map in memory so later runs protect the path instead of redesigning it, and logs a meta-article example each run so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /digital-plumbing
- Related (run order): ensure-working-contact-form-delivers-notifications → add-click-to-call-links-for-mobile → this
- Cross-links: /website-qa-audit (Layer 2 CTA checks) · /nine-triangles (Funnel: Audience → Engagement → Conversion) · /dad
