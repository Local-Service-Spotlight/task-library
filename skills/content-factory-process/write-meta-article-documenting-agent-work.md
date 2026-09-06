---
name: write-meta-article-documenting-agent-work
description: "Write what happened when a task ran. Link the work, the checks, and the next step."
category: Content Factory — Process
stage: Process
definitive_article: https://blitzmetrics.com/meta-article-prompt/
status: complete
---

# Write a meta article documenting a task execution

The next person should not have to guess what you did. This guide helps you write a clear record of the work and its result. Start with the task, the real evidence, and what is still left.

**The path:** Actual task evidence → Clear run story → Same execution record → Checked handoff.

**Use this when:** An actual task attempt needs its written record, including an ongoing, blocked, partial, failed or completed outcome.

## Inputs
- The exact task slug, stable execution ID, canonical recipe URL and source revision actually followed.
- Actual start, inputs, steps, decisions, output checks, result and next owner; use UNKNOWN for unmeasured telemetry.
- The saved artifacts/evidence with public/private limits and the meta article’s intended draft or publication state.
- The existing Task Library execution ledger/CLI and current previous record revision if updating; internal organization note requirements remain separate.

## First-run prompt

> Write the meta article for this actual task execution from the supplied evidence. Preserve its stable ID and recipe revision, state the real result and unknowns, and make a public-safe draft. Prepare and validate the existing ledger format without inventing telemetry, publication or extra runs. Record a supported next step even when the outcome is blocked.

## Steps
1. Read the real run evidence and existing record before writing. Separate the intended outcome from what actually happened. Keep one ID across retries, checks and derivative artifacts; a genuinely separate performed child can have its own parent-linked ID.
2. Write a plain opening with who needed the work, why it started and the useful result or remaining blocker. Describe the starting condition, source material and actual recipe revision.
3. Explain the steps actually performed, important decisions and checks. Use dated evidence and concrete observed results. Mark untested or unavailable fields; never fill time, cost, tokens or completion counts from estimates.
4. Show a meaningful real artifact or a clearly labeled diagram of the observed workflow/result. Link the canonical task and exact Task Library route, and explain new terms with owned guides. Keep secrets, private paths and private evidence URLs out of a public-safe version.
5. Record acceptance state from evidence: passed checks, failures, not-checked items, partial work and next owner. The story can be useful even when the task is blocked. Do not turn a written meta into automatic task certification.
6. Save the actual draft and compute its content hash if using the ledger’s draft form. For a published meta, verify the exact live page and use its URL. Preserve the separate internal agent-note required by the organization.
7. Prepare the ledger candidate using the existing schema: taskSlugs, recipeRevisions, actual startedAt, status, result, evidence and metaArticle. Running/blocked have no finishedAt; ended completed/partial/failed/cancelled attempts have their actual finish time. recordedAt is the first insertion time, not a rewritten start.
8. Validate with scripts/record_execution.py CANDIDATE.json --check. For an existing ID, supply --expected-revision with the prior actual revision, then use the maintained review/deploy rail for the authorized insert/update. Private evidence uses actual saved-content hashes, while the public projection omits private paths and draft detail.
9. Link useful lessons to a proposed recipe/skill correction and its evidence. Improve the source only when the run supports a change; a clean run need not invent a lesson. Hand the real result and pending work to the next owner under the existing communication scope.

## Definition of done (QA checklist)

- [ ] The written record links the actual task/revision and stable execution ID.
- [ ] Result, telemetry, evidence and remaining work are truthful and public-safe.
- [ ] Draft/published and ongoing/ended states match actual evidence; ledger validation passes before registration.
- [ ] Retries and derivatives do not inflate counts, and any source improvement is supported.

## Example(s)

**Fictional teaching example — do not register it.** A sample run prepares three article drafts. Two pass source review; one has an unclear quote. The work stops for the day with that output incomplete.

Its written result says “Two drafts checked; one quote review remains.” If this were a real ended attempt, `partial` with its actual finish time would fit. If the same run is still waiting on a reviewer, `blocked` without a finish time would fit. The draft hash must come from the real saved document, never an invented hex string.

The source also references the real `recipe-audit-20260905-080140` parent job. Read its current ledger entry for its state; a stale sentence saying “still in progress” is not current evidence. This teaching example adds no execution.

## Handoff and Content Factory context

The task owner receives the written meta and validated candidate record. The standards owner receives any supported recipe change; [Update the canonical task guide](https://local-service-spotlight.github.io/task-library/?task=create-or-update-a-definitive-article#task-create-or-update-a-definitive-article) is used when a real change is needed, not as an automatic endless meta loop.

Produce supplies the real source. **Process**, this stage of the [Content Factory](https://blitzmetrics.com/content-factory/), turns it into useful finished assets. Post saves or publishes them on the agreed channels. Promote tests and distributes suitable work within its own scope. The handoff above names this task’s actual next step; catalog neighbors alone are not prerequisites.

## When this runs

Write for every actual attempt, with same-ID updates as its state changes. Writing the parent’s record is part of that run; it does not create an automatic recurring publication task.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/meta-article-prompt/
- Exact task: [Write a meta article documenting a task execution](https://local-service-spotlight.github.io/task-library/?task=write-meta-article-documenting-agent-work#task-write-meta-article-documenting-agent-work)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Task recipe and publishing standard](https://blitzmetrics.com/definitive-article-guide/)
- [Task Library execution schema and CLI](https://github.com/Local-Service-Spotlight/task-library/blob/main/EXECUTION-LEDGER.md)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual evidence, source revision, draft hash and current ledger revision must come from the real execution.
