---
name: set-up-sop-amendment-proposal-tracking-system
description: Your team needs to know which fixes are waiting and which are live.
category: Knowledge System Maintenance
stage: —
definitive_article: /knowledge-system-maintenance
status: gap
---

# Set up task guide Amendment Proposal tracking system

Your team needs to know which fixes are waiting and which are live. This guide sets up that record from request to result. Start with the shared proposal home and the person who reviews it.

**The path:** Shared queue → Tracking fields → Test cycle → Real review setup

**Start when:** The shared proposal home exists but needs decision metadata, a test loop and a review workflow.

## Inputs

- [The checked proposal location](https://local-service-spotlight.github.io/task-library/?task=create-shared-location-for-sop-amendment-proposals#task-create-shared-location-for-sop-amendment-proposals) or its existing equivalent.
- The four-part/500-word format, named reviewer and agreed weekly review window.
- Authority for metadata, access, calendar changes and team notices.

## Steps

1. Reuse the approved location and preserve existing proposal IDs and history. Verify the current submit/review roles before adding fields.
2. Create or map title, affected guide, submitter, submission date, priority, decision state, resolution note and resulting source version. Add decision/release dates and evidence links so later metrics have actual timestamps.
3. Keep queued, returned, approved, rejected and awaiting evidence distinct; track release separately from approval. Preserve earlier decisions instead of overwriting them with the latest status.
4. Pin the format and seed a labeled test proposal. Check a full sample loop through tagging, review and resolution on test records, including a test-only version/changelog if used.
5. Agree the weekly reviewer and save any authorized event/job. Read back identifier, date/timezone and agenda; the saved review slot is not an observed review.
6. Test a small export and verify that real proposal IDs, submission/decision dates and states remain usable for later analysis. Exclude test proposals from production counts.
7. Link the maintained workflow to the system and issue only authorized notices. Record the real readiness gaps and the owner of the first live review.

## Definition of done (QA checklist)

[Quality assurance (QA)](https://localservicespotlight.com/article-guidelines/) means checking the work against the agreed result.

- [ ] Required metadata and history are retained in one accessible system.
- [ ] A test round trip and export work, with samples excluded from real counts.
- [ ] Review slot and real review/release outcomes are kept separate.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A fictional test proposal is approved against a test guide, creating a test version and changelog. Its row is marked sample. The first real proposal is still queued. The tracking system test passed; no real process improvement has been released yet.

## Handoff and Content Factory context

This work supports the [Content Factory, our four stages of using real content](https://blitzmetrics.com/content-factory/): Produce → Process → Post → Promote. Use the specific inputs and next task below to place the work; a maintenance task does not manufacture transcripts, clips or other stage outputs it does not call for.

[Review queued changes](https://local-service-spotlight.github.io/task-library/?task=senior-team-member-reviews-weekly#task-senior-team-member-reviews-weekly) handles live proposals; [the later pattern review](https://local-service-spotlight.github.io/task-library/?task=review-past-6-months-of-sop-amendment-proposals-for-patterns#task-review-past-6-months-of-sop-amendment-proposals-for-patterns) reads the retained metadata.

## Run with an agent

Give the AI worker this recipe, the real Inputs above, the intended result and the actions already authorized. Ask it to return the saved output, checks, evidence and remaining owner. Check its work against this guide; loading a skill does not prove access, installation of a job, or successful execution. Keep media muted with volume at zero if playback is needed.

For recurring work, keep the actual trigger, owner and runtime in the job record. Scheduling and observed firings are separate. Do not create a schedule merely because this guide mentions a review interval.

## Record the real execution

Open the run record when the work starts. Keep the exact starting recipe revision, one execution ID, source evidence and actual state. Write a [meta article, the record of one run](https://blitzmetrics.com/meta-article-prompt/) with decisions, results, checks, failures and next owner. Link it to this task and register it through the [Task Library](https://local-service-spotlight.github.io/task-library/) execution process. Writing is part of the work; public release follows existing authority.

Reuse the same execution ID for revisions, QA, meta writing and retries within that run. A blocked run stays open with its dependency and next owner; do not invent a finish time. Use supported findings to propose and verify a better recipe. A historical public-example count without distinct run IDs remains dated article volume, not verified execution frequency.

## Definitive article & links

- [Maintained source guide](https://blitzmetrics.com/knowledge-system-maintenance/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=set-up-sop-amendment-proposal-tracking-system#task-set-up-sop-amendment-proposal-tracking-system)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [current article guide](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records work together](https://localservicespotlight.com/meta-articles/)

## Review and evidence still needed

The inherited contributor status is `gap`. It is preserved, not promoted by this rewrite. That label alone does not verify document readiness, a client outcome, access or an executed task.

A real execution still needs its own source, reviewer, saved result and handoff evidence. The fictional example teaches the method; a real example with relevant proof is still needed where required. The task-specific flow above is source guidance; its visible presentation and the full document need a named reviewer and desktop/mobile checks.
