---
name: grade-article-using-jennifer
description: "Check the words and proof in a draft. List what needs a fix."
category: Content Factory — Process
stage: Process
definitive_article: GAP — to be written
status: gap
---

# Grade article using Jennifer

A polished article can still have a wrong fact or weak proof. This guide helps you check it with a named set of rules. Start with the full draft, its source, and the rules you will use.

**The path:** Exact draft and rubric → Evidence-based findings → Bounded fixes → Clear readiness decision.

**Use this when:** A finished draft needs a bounded, recorded quality review before its next publishing step.

## Inputs
- The complete versioned article, GCT, page role, transcript/primary proof, visuals, links and author context.
- The actual Jennifer rubric file/version and current [Article Guidelines](https://localservicespotlight.com/article-guidelines/) plus task standard. Jennifer is the named review rubric, not proof of a running installed agent.
- The requested review tier and revision budget, a writer for corrections, and a tracker for findings.
- Rendered page evidence when available; draft-only checks stay separate from public checks.

## First-run prompt

> Review this exact article and source using the supplied Jennifer version plus current owned standards. First list rubric conflicts. Return quoted, located findings and hard-gate states; give a letter only when the rubric supports it. Keep fixes bounded, do not manufacture proof to meet quotas, and do not equate A- with publication authority.

## Steps
1. Record the exact draft and rubric versions. Check the rubric against current standards before grading. Check for version conflicts such as unconditional A- readiness, arbitrary ten-reference/three-link quotas or claims that every personal article proves a personal relationship. Newer revisions may have already fixed some clauses; cite the exact version you inspect. Preserve those conflicts as findings instead of inventing evidence to satisfy them.
2. Use the maintained role-specific standard for hard decisions: truthful facts/relationships, attributed permitted praise, clear GCT, meaningful lead visual, correct voice, useful links, and complete task contract where applicable. A score never overrides a failed proof, relationship, attribution, or compliance gate. Apply the named credibility caps from the canonical source: a Trophy-name paragraph without a specific shared scene, reader lesson, and primary source is capped; a Relationship noun outruns the evidence when the article claims a stronger bond than its source proves; Repeated defensive caveats or verification theater are capped unless a legal, regulatory, or compliance disclosure materially requires them; Public copy exposes internal scoring or production metadata when it publishes internal proof IDs, scores, or repurposing instructions that are not the article's topic; and praise that is anonymous or attributed only to a domain/company remains `publish_ready: false` and HOLD until it has the required named source, exact quote, and permission. Do not silently call a revised rubric the unchanged legacy Jennifer.
3. Review the full article, media/alt/caption context, source and available rendering. Quote each real defect and identify its location, violated rule, severity, evidence and requested fix. A count of names or links is not proof of quality.
4. Return structured review fields: draft revision, rubric revision, rubric conflicts, grade if a consistent rubric supports one, publish_ready, hard-gate states and actionable findings. Use grade UNKNOWN when unresolved rubric conflicts prevent a defensible letter; do not mint a flattering substitute score.
5. Keep publish_ready false while a hard gate fails or required evidence is untested. Under a reconciled Jennifer rubric, A- or A can end cosmetic iteration only after applicable hard checks pass. A letter never grants publication authority.
6. Send exact defects to the writer. Preserve the source budget when used: STRONG up to three rounds, MODERATE two, LIGHT one; tier targets do not waive hard gates. At the budget limit, return the remaining list and next decision rather than looping indefinitely.
7. Recheck the changed revision and affected sources. Do not regrade unchanged accepted copy to chase an A, but a substantive new change or newly failed hard gate requires a new check of the current revision.
8. Save findings, fixes, unresolved conflicts, actual round count and readiness. If the installed rubric remains inconsistent, hand its exact source clauses to the standards owner and use the clearly labeled maintained article checklist for useful review meanwhile.

## Opening meaning review

Keep the opening to two or three short sentences at grade 5 or below. It must show the actual reader’s situation, why the subject matters, the useful result, and how this page helps. A source-backed moment or useful finding can lead. Keep its relevant visual in the first screen; check that the body delivers the opening’s promise.

Save the exact opening and artifact revision in the existing run receipt. Have the reviewer quote the words that establish the situation, reason to care, result and method. Record PASS, FAIL or UNKNOWN with reasons and a readability diagnostic. A grade score, keyword, generic audience label or unsupported conversion promise cannot approve meaning. Follow [Step 7: write and review the opening](https://local-service-spotlight.github.io/task-library/?task=step-7-write-hook-and-establish-context#task-step-7-write-hook-and-establish-context) and the [maintained opening standard](https://github.com/dennisyu/local-service-spotlight-skills/blob/main/standards/every-article-and-project-starts-with-specific-gct.md).

A failed or untested opening-meaning gate keeps `publish_ready: false`. A meaningful loaded visual must also pass the [canonical rendered first-screen gate](https://github.com/dennisyu/local-service-spotlight-skills/blob/main/standards/visuals-above-the-fold.md) at 390x844 and 1280x800. The first two or three paragraphs, an image tag or a letter grade cannot replace actual first-screen screenshots and source-backed review.

## Definition of done (QA checklist)

- [ ] Exact article/rubric revisions and any conflicts are recorded.
- [ ] Findings quote actual text and distinguish evidence gates from style preferences.
- [ ] Readiness is never inferred solely from a grade or contributor status.
- [ ] Revision budget and remaining owner/action are explicit; no fabricated grade or proof count is used.

## Example(s)

**Fictional teaching example — no article was scored by Jennifer.** A sample review finds: “exact price from one photo” conflicts with the source’s inspection requirement. It records a hard factual failure at the opening. The draft also lacks a meaningful lead visual.

The review output is `grade: UNKNOWN`, `publish_ready: false`, with the unresolved legacy rubric version conflict and those two precise issues. The writer fixes the promise and adds a relevant diagram. That improves the article, but does not retroactively prove the legacy grader ran or that a public page passed. A consistent reviewed rubric and current evidence are needed for a letter-grade claim.

## Handoff and Content Factory context

The writer uses [Write from the checked source](https://local-service-spotlight.github.io/task-library/?task=step-5-write-article-from-transcript#task-step-5-write-article-from-transcript) for substantive fixes. The publisher gets the reviewed revision through [the maintained article checklist](https://local-service-spotlight.github.io/task-library/?task=verify-all-items-on-blog-posting-checklist#task-verify-all-items-on-blog-posting-checklist) and [WordPress placement](https://local-service-spotlight.github.io/task-library/?task=step-12-post-article-on-wordpress#task-step-12-post-article-on-wordpress) when applicable.

Produce supplies the real source. **Process**, this stage of the [Content Factory](https://blitzmetrics.com/content-factory/), turns it into useful finished assets. Post saves or publishes them on the agreed channels. Promote tests and distributes suitable work within its own scope. The handoff above names this task’s actual next step; catalog neighbors alone are not prerequisites.

## When this runs

Per substantive draft review, within the chosen round budget. Recheck after material changes, not indefinitely after an accepted unchanged draft.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Dedicated canonical article: not mapped in this source record. Use the maintained owned training below until that article gap is reviewed.
- Exact task: [Grade article using Jennifer](https://local-service-spotlight.github.io/task-library/?task=grade-article-using-jennifer#task-grade-article-using-jennifer)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Task recipe and publishing standard](https://blitzmetrics.com/definitive-article-guide/)
- [Jennifer rubric source and conflict review](https://localservicespotlight.com/jennifer-our-article-grader-skill-file-for-claude/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The upstream Jennifer rubric needs reviewed synchronization with current standards before a consistent named grade is claimed. Dedicated canonical task article remains unmapped.
