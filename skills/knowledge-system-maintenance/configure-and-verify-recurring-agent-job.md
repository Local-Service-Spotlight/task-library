---
name: configure-and-verify-recurring-agent-job
description: A task on a calendar has not done the work yet.
category: Knowledge System Maintenance
stage: —
definitive_article: https://blitzmetrics.com/persistent-agents/
status: needs-work
---

# Configure and verify a recurring agent job

A task on a calendar has not done the work yet. This guide helps you set up one repeat job and check its first result. Start with a task that already has clear steps and a way to judge the work.

**The path:** Tested recipe → Saved trigger → Real firing → Checked result

**Start when:** A clear recipe needs repeat execution and the selected job, runtime and schedule are authorized.

## Inputs

- One task recipe, exact source revision, allowed inputs and pass criteria.
- The chosen app, account, plan, machine/cloud location and authority to save a recurring job.
- A state folder, output destination, failure route and named owner, each with verified access.

## Steps

1. Write the job contract: scope, sources, actions, output, pass checks and what to do on failure. Keep secrets in the designated store; ordinary state notes contain references only.
2. Check the selected runtime’s current official scheduling docs. Choose a supported trigger and record timezone, recurrence, resource limits and availability needs. A local-file job needs access to its actual machine; a cloud label alone does not establish it.
3. Inspect existing jobs for overlap. Preserve a working job and its state; update the intended record instead of creating a duplicate.
4. Using the supported scheduler, save the exact job with its owner, source version, output and failure destination. Read back its identifier and next expected firing. At this point it is scheduled, not observed.
5. Run one bounded test, then check the next actual scheduled firing. Verify the result at the receiving destination and compare against the recipe. A manual test does not prove the clock fired.
6. Test an agreed non-destructive failure case or inspect a real failure. Confirm it is visible to the owner. Record last attempt, last success/failure and next expected run separately.
7. Open the previous state from a fresh run and verify it avoids duplicate work. Keep unresolved runtime, delivery or failure checks blocked; do not widen access to force a pass.

## Current implementation

For a supported Claude Cowork account, the current manual setup is Scheduled → New task → Set up manually. Fill the task name, prompt, approval mode and cadence; choose a model or working folder only where needed and supported. Save, reopen the entry, and check its next run and actual output. Official help describes remote jobs that use connectors and files saved to the Claude account; it says those jobs run even when the computer sleeps or the desktop app is closed. The same page separately describes jobs needing local files or apps as local. For that local mode, keep the required computer and apps available and test the actual job. Check which mode the current account and task support; do not apply the remote sleep behavior to a job with local dependencies. This is one platform implementation, not an instruction to move an existing working job into Cowork. [Current official scheduling instructions](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork).

## Definition of done (QA checklist)

[Quality assurance (QA)](https://localservicespotlight.com/article-guidelines/) means checking the work against the agreed result.

- [ ] Saved job identity, trigger/timezone, account and exact task version are verified.
- [ ] At least one real firing has an independently checked output or failure receipt.
- [ ] Next-run state and failure visibility are tested; manual tests and scheduled runs are separate.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A fictional report job is saved for Monday at 09:00 in the team’s timezone. A manual test succeeds on Sunday. Monday’s run fails to read its source, and the owner sees the error. The job is scheduled and observed, but its Monday report failed; it is not a successful weekly report.

## Handoff and Content Factory context

This work supports the [Content Factory, our four stages of using real content](https://blitzmetrics.com/content-factory/): Produce → Process → Post → Promote. Use the specific inputs and next task below to place the work; a maintenance task does not manufacture transcripts, clips or other stage outputs it does not call for.

The job owner retains the operating record. Use [the original-thread status task](https://local-service-spotlight.github.io/task-library/?task=reply-with-task-status-in-origin-thread#task-reply-with-task-status-in-origin-thread) for an authorized status reply and review changes before the next firing.

## Run with an agent

Give the AI worker this recipe, the real Inputs above, the intended result and the actions already authorized. Ask it to return the saved output, checks, evidence and remaining owner. Check its work against this guide; loading a skill does not prove access, installation of a job, or successful execution. Keep media muted with volume at zero if playback is needed.

For recurring work, keep the actual trigger, owner and runtime in the job record. Scheduling and observed firings are separate. Do not create a schedule merely because this guide mentions a review interval.

## Record the real execution

Open the run record when the work starts. Keep the exact starting recipe revision, one execution ID, source evidence and actual state. Write a [meta article, the record of one run](https://blitzmetrics.com/meta-article-prompt/) with decisions, results, checks, failures and next owner. Link it to this task and register it through the [Task Library](https://local-service-spotlight.github.io/task-library/) execution process. Writing is part of the work; public release follows existing authority.

Reuse the same execution ID for revisions, QA, meta writing and retries within that run. A blocked run stays open with its dependency and next owner; do not invent a finish time. Use supported findings to propose and verify a better recipe. A historical public-example count without distinct run IDs remains dated article volume, not verified execution frequency.

## Definitive article & links

- [Maintained source guide](https://blitzmetrics.com/persistent-agents/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=configure-and-verify-recurring-agent-job#task-configure-and-verify-recurring-agent-job)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [current article guide](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records work together](https://localservicespotlight.com/meta-articles/)

## Review and evidence still needed

The inherited contributor status is `needs-work`. It is preserved, not promoted by this rewrite. That label alone does not verify document readiness, a client outcome, access or an executed task.

Actual runtime access, supported schedule configuration, first firing and failure-route test remain unverified until executed. Official scheduling controls depend on the selected surface and plan. The fictional example teaches the method; a real example with relevant proof is still needed where required. The task-specific flow above is source guidance; its visible presentation and the full document need a named reviewer and desktop/mobile checks.
