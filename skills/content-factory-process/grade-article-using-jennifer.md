---
name: grade-article-using-jennifer
description: Run a finished article through the Jennifer grading system for a quality score and fix what it flags before the piece moves to the Post stage.
category: Content Factory — Process
stage: Process
definitive_article: GAP — to be written
status: gap
---

# Grade article using Jennifer

**Use this when** an article has cleared proofreading (Step 11) and you want an objective quality score before WordPress posting.

The rubric lives in the Local Service Spotlight pack as `jennifer` (DealCon-Skills). This Task Library skill is the station on the factory line that *calls* it. Hub article still pending — until it ships, run from this file plus `/blog-posting-guidelines`.

## The A- terminator (publish bar)
A- is the publish bar after every hard publish gate passes. **Do not iterate past A-.** When an article hits A- with no `publish_ready: false` cap, return `publish_ready: true` and zero further suggestions. A score never overrides a failed proof, relationship, attribution, or compliance gate. Chasing an A traps agents in infinite revision loops. An A stays reserved for world-class national-publication journalism.

Revision budgets before human escalation: STRONG 3 rounds (target A-), MODERATE 2 (target B+), LIGHT 1 (target B). Below a C after the budget: stop and escalate with the penalty list. Never regrade an article that already earned A- in this run.

## Caps that stack (do not invent a friendlier grader)
1. Promotional or flowery sales tone: cannot score higher than a C.
2. Fewer than 10 specific experience references (names, quotes, places, events): lose one full letter; max B.
3. Fewer than 3 in-network related links: lose one full letter.
4. ChatGPT giveaway language ("X doesn't just Y. It's also Z."): lose one full letter.
5. Any typo: lose one full letter per occurrence.
6. Repurposed from video but source video not embedded: max C.
7. A meaningful loaded visual fails the [canonical rendered first-screen gate](https://github.com/dennisyu/local-service-spotlight-skills/blob/main/standards/visuals-above-the-fold.md) at 390x844 or 1280x800: `publish_ready: false`. First 2–3 paragraphs, an image tag or a letter grade cannot substitute for the actual first-screen screenshot and source-backed review.
8. POV mismatch (third person on a personal-brand site, or first person on a company site): max B.
9. WordPress author set to an admin/team account: max B+ — flag even at A- and run `set-wordpress-author-to-correct-person`.
10. Banned AI-tell words: "honest," "honestly," "quietly."
11. Trophy-name paragraph: two or more recognizable people, brands, titles, awards, or logos appear without a specific shared scene, reader-relevant lesson, and primary source: max C.
12. Relationship noun outruns the evidence (for example, "friend," "partner," "mentor," "client," "endorsed," or "collaborated" when the source proves only an appearance, interview, meeting, or photo): `publish_ready: false` until narrowed or supported.
13. Repeated defensive caveats or verification theater (for example, "this does not prove friendship," "no endorsement is implied," or "every claim below is sourced"): max B. Exempt language that is materially required for a legal, regulatory, or compliance disclosure; keep that disclosure scoped to the triggering claim.
14. Public copy exposes internal scoring or production metadata, including confidence grades, proof-record IDs, harvester/canonical-inventory labels, or repurposing instructions when those systems are not the article's topic: max C.
15. Praise is anonymous, attributed only to a domain/company, paraphrased inside quotation marks, or missing a primary source: `publish_ready: false`; mark the item HOLD. A publishable testimonial is an exact quote from a named person with applicable role/company or city, source link, and permission where required.
16. The first 2–3 sentences do not make the actual reader/situation, reason to care, useful outcome and supporting mechanism clear, or the body does not deliver the opening's promise: `publish_ready: false`. Apply `step-7-write-hook-and-establish-context` and the shared specific-GCT opening standard. Record the exact text and quoted reviewer evidence in the existing tracker. A grade, word count, generic audience label or conversion claim cannot substitute for meaning; unsupported promises also fail.

Jennifer grades; she does not rewrite. Send rewrites to `step-5-write-article-from-transcript` (or Brandon / `definitive-article-writer`), then bring the draft back.

## Inputs
- The finished article draft (post-Step 11, pre-posting)
- The Jennifer skill file from the installed pack (or this section if the pack is not installed)
- The article's GCT statement and transcript
- The Content Library tracker

## Steps
1. Submit the complete article — title, meta, body, captions, testimonial attribution, image alt text, and rendered page when available — to Jennifer. If you are an orchestrator, demand the structured JSON (grade, `publish_ready`, example count, link list, every penalty quoted).
2. Record the score and the full rubric feedback verbatim in the tracker; the score is a Metric in the MAA loop, not a verdict to skim.
3. If the grade is A- or A and every hard publish gate passes: stop. Set `publish_ready`. Hand the file to `step-12-post-article-on-wordpress`. If a hard gate fails, keep `publish_ready: false` regardless of the letter grade.
4. If below A- and rounds remain: fix every stacked cap, stay faithful to the transcript, regrade.
5. If below C after the budget: escalate to a human with the penalty list. Do not keep prompting.
6. Cross-check hard specs after edits: title under 60, meta under 160, keyword in first paragraph, links intact.
7. Attach the final grade to the post record so Rank Math, Jennifer, and the audit travel together.

## Definition of done (QA checklist)
- [ ] Article graded; score and full feedback recorded verbatim
- [ ] A- terminator honored after every hard gate passes — no extra polish after publish_ready and no score-based waiver of a failed gate
- [ ] Every flag below A- fixed or explicitly accepted with a written reason
- [ ] Fixes verified against transcript and GCT (no invented content)
- [ ] Personal-brand copy shows sourced moments in first person; no trophy-name paragraphs
- [ ] Relationship nouns are evidence-bound and every notable name supplies context for a scene or lesson
- [ ] Zero repeated defensive caveats or public internal scoring/repurposing metadata; any retained legal/compliance disclosure is materially necessary and scoped
- [ ] Published praise is exact, named, attributable, and source-linked; anonymous/domain-only claims remain HOLD
- [ ] Author is the site owner or a B+ cap is flagged for `set-wordpress-author-to-correct-person`
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- May 2026, Daniel Goodrich's repurposing pipeline grading "per Jennifer rubric": pass one caught 2 banned constructions, 5 non-verb-led H2s, and 2 preposition endings; pass two terminated at A-. That is the loop this station runs.
- Hub article still a gap — first public meta-article that ships a full JSON grade should be linked here.

## Run on a persistent agent (Fable 5)

The grade-fix-regrade cycle is a loop by design, and a persistent agent (Claude Fable 5, or comparable OpenAI/Google models that loop and hold memory) runs it without fatigue: every flag fixed or explicitly accepted with a written reason, hard specs re-verified after each edit, iterating until the checklist closes — never stopping at a "good enough" score. Memory accumulates Jennifer's recurring findings across articles, so future drafts pre-empt the flags before submission. Log each run's meta-article — the first one defines the rubric for everyone after.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: GAP — to be written ("How to Grade an Article Using Jennifer" is on the Gaps & Tasks to Create list, low priority).
- Related: /blog-posting-guidelines (the standards Jennifer scores against), /website-qa-audit, /maa
- Sibling skills, in run order: `step-11-proofread-with-grammarly-or-chatgpt` → this → `step-12-post-article-on-wordpress` (Post stage)
