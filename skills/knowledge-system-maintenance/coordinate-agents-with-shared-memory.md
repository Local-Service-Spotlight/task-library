---
name: coordinate-agents-with-shared-memory
description: Two AI workers should not undo each other’s work.
category: Knowledge System Maintenance
stage: —
definitive_article: https://blitzmetrics.com/set-up-cross-agent-shared-memory/
status: needs-work
---

# Coordinate agents with shared memory

Two AI workers should not undo each other’s work. This guide gives them shared notes and a clear owner for each change. Start with one real task and the sources that hold its facts.

**The path:** Source owners → Task claim → Verified work → Fresh handoff

**Start when:** More than one authorized worker needs to contribute to or resume the same real task.

## Inputs

- An owned shared folder or [Obsidian, a workspace for shared notes](https://blitzmetrics.com/obsidian-cowork-layer-shared-memory-across-agents/) with agreed read/write access.
- The task, allowed actions, actual source systems and a shared claim/checkpoint format.
- Canonical skill sources and a designated secret store; no credential values in the working notes.

## Steps

1. Map each record type to its authority: task/source system for live work, repository for maintained instructions, shared notes for context, secret store for credentials. Vendor memory and copied packs are caches.
2. Prepare only the context needed for the task: current goal, relevant source links/revisions, evidence, constraints and next action. Keep unrelated client records out of the packet.
3. Read active task claims before editing. Claim the exact targets with owner, task ID and timestamp using the team’s supported shared mechanism. If another claim overlaps, coordinate or choose independent work; a timestamp alone is not permission to overwrite.
4. Read the current source just before writing and compare its revision to the claimed base. Preserve concurrent edits. Perform only the task’s authorized actions through the source system.
5. Check the saved result where it lives. Update the checkpoint with completed work, output references, failures, remaining decisions and next owner. Release or hand off the claim explicitly.
6. Have a fresh authorized agent read the packet, identify the live authorities and resume a bounded next step. Compare its understanding against the source; access to the folder alone does not prove a successful handoff.
7. Write the run record and required private team note. Propose reusable changes to the canonical skill, then verify its separate distribution/activation state.

## Definition of done (QA checklist)

[Quality assurance (QA)](https://localservicespotlight.com/article-guidelines/) means checking the work against the agreed result.

- [ ] Each fact type has one identified authority and privacy boundary.
- [ ] Overlap is detected before writes; current-source revision guards preserve other work.
- [ ] A fresh agent can recover the real task state and find its checked result.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

Two fictional workers plan to edit the same page. Worker A has a current claim. Worker B reviews links in a separate file, then sends findings to A. A’s checkpoint records the saved page hash and two open checks. The next worker resumes those two checks instead of starting a second rewrite.

## Handoff and Content Factory context

This work supports the [Content Factory, our four stages of using real content](https://blitzmetrics.com/content-factory/): Produce → Process → Post → Promote. Use the specific inputs and next task below to place the work; a maintenance task does not manufacture transcripts, clips or other stage outputs it does not call for.

[The receiving agent](https://local-service-spotlight.github.io/task-library/?task=onboard-agent-for-first-scoped-task#task-onboard-agent-for-first-scoped-task) reads the checkpoint and executes only its assigned next task.

## Run with an agent

Give the AI worker this recipe, the real Inputs above, the intended result and the actions already authorized. Ask it to return the saved output, checks, evidence and remaining owner. Check its work against this guide; loading a skill does not prove access, installation of a job, or successful execution. Keep media muted with volume at zero if playback is needed.

For recurring work, keep the actual trigger, owner and runtime in the job record. Scheduling and observed firings are separate. Do not create a schedule merely because this guide mentions a review interval.

## Record the real execution

Open the run record when the work starts. Keep the exact starting recipe revision, one execution ID, source evidence and actual state. Write a [meta article, the record of one run](https://blitzmetrics.com/meta-article-prompt/) with decisions, results, checks, failures and next owner. Link it to this task and register it through the [Task Library](https://local-service-spotlight.github.io/task-library/) execution process. Writing is part of the work; public release follows existing authority.

Reuse the same execution ID for revisions, QA, meta writing and retries within that run. A blocked run stays open with its dependency and next owner; do not invent a finish time. Use supported findings to propose and verify a better recipe. A historical public-example count without distinct run IDs remains dated article volume, not verified execution frequency.

## Definitive article & links

- [Maintained source guide](https://blitzmetrics.com/set-up-cross-agent-shared-memory/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=coordinate-agents-with-shared-memory#task-coordinate-agents-with-shared-memory)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [current article guide](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records work together](https://localservicespotlight.com/meta-articles/)

## Review and evidence still needed

The inherited contributor status is `needs-work`. It is preserved, not promoted by this rewrite. That label alone does not verify document readiness, a client outcome, access or an executed task.

A real execution still needs its own source, reviewer, saved result and handoff evidence. The fictional example teaches the method; a real example with relevant proof is still needed where required. The task-specific flow above is source guidance; its visible presentation and the full document need a named reviewer and desktop/mobile checks.
