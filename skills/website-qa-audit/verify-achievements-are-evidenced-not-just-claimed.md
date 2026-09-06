---
name: verify-achievements-are-evidenced-not-just-claimed
description: Audits every expertise and results claim on the site for attached proof — links, photos, screenshots, named sources — converting assertions into E-E-A-T evidence.
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify achievements are evidenced, not just claimed

**Use this when** running Layer 3 (Authority & Trust Checks) of the Website QA Audit — "award-winning" and "trusted by hundreds" mean nothing without something a visitor can check.

## Inputs
- Site URL (about page, homepage, and bio sections are the claim hotspots)
- The owner's actual proof inventory: press links, podcast/talk recordings, certifications, review platform profiles, real metrics
- The audit report/spreadsheet for logging results

## Steps
1. Sweep the site and list every achievement claim: years in business, jobs completed, awards, certifications, media features, "as seen on" logos, revenue/results numbers.
2. For each claim, check for attached evidence on the page: a link to the source, a photo of the award or jobsite, a screenshot of the metric or review, a named publication with a working link.
3. Inspect how the proof is told. On a personal-brand site, pass first-person scenes that show what happened, why it mattered, and one human detail, followed by a compact source receipt. Fail resume-like lists and trophy-name paragraphs that stack recognizable people, brands, titles, awards, or logos without a specific shared moment and reader-relevant lesson.
4. Check every relationship noun against its source. A photo, co-appearance, or interview does not by itself establish "friend," "client," "partner," "mentor," "endorsed," or "collaborated." Narrow the public noun/verb to what the record supports or mark the stronger claim HOLD.
5. Fail unevidenced claims — especially logo walls that don't link to the actual feature, round-number boasts with no source, anonymous praise, and testimonials attributed only to a domain or company. Publish praise only as an exact quote from a named person with applicable role/company or city, a primary source, and permission where required; otherwise keep it HOLD.
6. Fail verification theater in public copy: repeated "this does not prove friendship/endorsement" caveats, confidence scores, proof-record IDs, canonical-inventory/harvester labels, or repurposing instructions when those systems are not the page's subject. Preserve a materially necessary legal, regulatory, or compliance disclosure, scoped to the triggering claim.
7. Verify the evidence itself: click press links (the article must actually mention the owner), and confirm certificates and review counts are current.
8. For every failed claim, pair it with the proof to add from the owner's inventory — or flag it for removal/HOLD if no proof exists. Do not add a caveat to make an unsupported claim feel safer.
9. Log the internal claim-to-evidence table in the audit report; do not publish the table or its confidence/status fields as page copy.

## Definition of done (QA checklist)
- [ ] 100% of achievement claims on the site carry attached, working evidence — zero naked claims, zero logos without linked features
- [ ] Claims with no obtainable proof removed rather than left unsupported
- [ ] Personal-brand proof reads as first-person scenes and lessons with compact receipts, not trophy-name paragraphs
- [ ] Relationship nouns match the evidence; published praise is exact, named, source-linked, and fully attributed; anonymous/domain-only praise remains HOLD
- [ ] Zero repeated defensive caveats or public internal audit/repurposing metadata; any retained legal/compliance disclosure is materially necessary and scoped
- [ ] Claim-to-evidence table logged in the audit report, linked back to /website-qa-audit

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run.

## Run on a persistent agent (Fable 5)
A persistent Fable 5 agent (or comparable OpenAI/Google long-horizon model) sweeps every page for claims — not just the about page — pairs each with working evidence from the owner's proof inventory, and loops until 100% of claims carry checkable proof or are removed, re-clicking every evidence link each run because press links rot.
Memory holds the claim-to-evidence table, so re-runs only evaluate new claims and re-verify previously passing links.
Each run logs one worked example to ## Example(s) so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /website-qa-audit
- Related: /seo-audit (E-E-A-T signals) · previous: check-social-profiles-linked-and-prominent · next check: verify-google-business-profile-is-verified
