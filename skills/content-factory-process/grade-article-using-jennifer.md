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
A- is the publish bar. **Do not iterate past A-.** When an article hits A-, return `publish_ready: true` and zero further suggestions. Chasing an A traps agents in infinite revision loops. An A stays reserved for world-class national-publication journalism.

Revision budgets before human escalation: STRONG 3 rounds (target A-), MODERATE 2 (target B+), LIGHT 1 (target B). Below a C after the budget: stop and escalate with the penalty list. Never regrade an article that already earned A- in this run.

## Caps that stack (do not invent a friendlier grader)
1. Promotional or flowery sales tone: cannot score higher than a C.
2. Fewer than 10 specific experience references (names, quotes, places, events): lose one full letter; max B.
3. Fewer than 3 in-network related links: lose one full letter.
4. ChatGPT giveaway language ("X doesn't just Y. It's also Z."): lose one full letter.
5. Any typo: lose one full letter per occurrence.
6. Repurposed from video but source video not embedded: max C.
7. Lead visual missing from the first 2–3 paragraphs: max B+.
8. POV mismatch (third person on a personal-brand site, or first person on a company site): max B.
9. WordPress author set to an admin/team account: max B+ — flag even at A- and run `set-wordpress-author-to-correct-person`.
10. Banned AI-tell words: "honest," "honestly," "quietly."

Jennifer grades; she does not rewrite. Send rewrites to `step-5-write-article-from-transcript` (or Brandon / `definitive-article-writer`), then bring the draft back.

## Inputs
- The finished article draft (post-Step 11, pre-posting)
- The Jennifer skill file from the installed pack (or this section if the pack is not installed)
- The article's GCT statement and transcript
- The Content Library tracker

## Steps
1. Submit the complete article — title, meta, body, image alt text — to Jennifer. If you are an orchestrator, demand the structured JSON (grade, `publish_ready`, example count, link list, every penalty quoted).
2. Record the score and the full rubric feedback verbatim in the tracker; the score is a Metric in the MAA loop, not a verdict to skim.
3. If the grade is A- or A: stop. Set `publish_ready`. Hand the file to `step-12-post-article-on-wordpress`.
4. If below A- and rounds remain: fix every stacked cap, stay faithful to the transcript, regrade.
5. If below C after the budget: escalate to a human with the penalty list. Do not keep prompting.
6. Cross-check hard specs after edits: title under 60, meta under 160, keyword in first paragraph, links intact.
7. Attach the final grade to the post record so Rank Math, Jennifer, and the audit travel together.

## Definition of done (QA checklist)
- [ ] Article graded; score and full feedback recorded verbatim
- [ ] A- terminator honored — no extra polish after publish_ready
- [ ] Every flag below A- fixed or explicitly accepted with a written reason
- [ ] Fixes verified against transcript and GCT (no invented content)
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
