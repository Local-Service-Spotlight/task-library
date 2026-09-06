---
name: verify-testimonials-with-full-attribution
description: Holds every testimonial to the full trust standard — name, title, company, and headshot — so any skeptical visitor could verify the person is real.
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify testimonials with full attribution

**Use this when** starting Layer 3 (Authority & Trust Checks) of the Website QA Audit — this is the stricter pass on testimonials: complete, verifiable attribution.

## Inputs
- The testimonial inventory from the Layer 2 headshot check (verify-testimonials-include-headshots-with-attribution)
- A browser for verifying the people are findable (LinkedIn/company-site lookup)
- The audit report/spreadsheet for logging results

## Steps
1. Take every testimonial on the site and score it against all four attribution fields: full name, title/role, company (or city for consumer clients), and real headshot. Also capture the primary source URL and permission state.
2. Fail any testimonial missing one or more fields — Layer 2 passed "name plus face"; Layer 3 requires the complete set. A company or domain by itself names an organization, not the person who supplied the praise; keep it HOLD.
3. Verify a sample: look up the named person (LinkedIn or their company site) and confirm they exist and plausibly match the headshot and title.
4. Compare the published words with the primary source. The quote must be exact; do not put a paraphrase or composite inside quotation marks. Prefer linked attribution where the person agreed — name linking to their LinkedIn or company turns the testimonial into checkable evidence.
5. For each incomplete testimonial, list exactly which field to collect from the client, with the owner's outreach note.
6. Log the four-field scorecard per testimonial in the audit report.

## Definition of done (QA checklist)
- [ ] 100% of testimonials carry all four fields — full name, title, company, headshot — plus an exact source-linked quote and any required permission, with zero anonymous, domain-only, or partial entries
- [ ] Incomplete or unverified praise remains HOLD and is not rendered as a testimonial
- [ ] Spot-checked people are real and findable; fabricated-looking entries removed
- [ ] Four-field scorecard logged in the audit report, linked back to /website-qa-audit

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run.

## Run on a persistent agent (Fable 5)
A persistent Fable 5 agent (or comparable OpenAI/Google model) scores every testimonial on the site against all four fields — name, title, company, headshot — and looks up every named person rather than a sample, looping collect-verify until 100% carry complete, checkable attribution.
Memory keeps the four-field scorecard per testimonial, so re-runs only score new or edited entries and re-verify links that previously passed.
Each run logs one worked example to ## Example(s) so the audit library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /website-qa-audit
- Related: Layer 2 sibling: verify-testimonials-include-headshots-with-attribution · next check: check-social-profiles-linked-and-prominent
