---
name: configure-and-verify-recurring-agent-job
description: "One configured job with retained state and an observed, independently checkable run or failure."
category: Knowledge System Maintenance
stage: —
definitive_article: https://blitzmetrics.com/persistent-agents/
status: needs-work
---

# Configure and verify a recurring agent job

**Use this when:** A documented task should run on a real trigger without someone remembering to start it.

This is a registered recipe in review. A published guide or this new record does not certify its runtime behavior. Read the current [canonical procedure](https://blitzmetrics.com/persistent-agents/) before executing; it contains the detailed actions and current source-specific instructions.

## Inputs
- One documented skill and its acceptance checks
- Authorized runtime and schedule
- Persistent working state
- A verified output and failure destination

## Prerequisite tasks
- No separate mandatory task is established by the reviewed source; use the explicit starting condition and inputs above.
## Input references
- [A Skill Is How. A Routine Is When.](https://blitzmetrics.com/skills-and-routines/)
- [How Our AI Agents Share Memory and Coordinate Work](https://blitzmetrics.com/set-up-cross-agent-shared-memory/)
## Steps
1. Write the task standard.
2. Choose and configure a real recurring trigger.
3. Give the job a working folder.
4. Read the previous state before acting.
5. Verify the outcome from the outside.
6. Record failures and feed learning back.

## Definition of done (QA checklist)

**Expected result:** One configured job with retained state and an observed, independently checkable run or failure.

- [ ] The trigger exists in the runtime
- [ ] A firing leaves timestamped evidence
- [ ] Output is checked where its reader receives it
- [ ] A failed or missing result is visible to the owner
- [ ] The next run can read the previous state
- [ ] Record the exact source revision, actual result and evidence; retain failure, partial, blocked and unknown states.
- [ ] Write the execution's meta article and link the canonical task. Publication is a separate action under the current authority.
- [ ] Keep this parent job's internal retries, checks and agent contributions on the same execution ID; derivatives and revisions add no runs. A separately scoped and documented child execution may have its own ID with parentExecutionId, without adding a second completion to this parent recipe.
- [ ] Verify permissions for publishing, sending, spending, scheduling or changing access before that action. A task record does not grant them.

## Child or companion tasks
- No separate mandatory task is established by the reviewed source; use the explicit starting condition and inputs above.
## Handoff and Content Factory context

Deliver the result or honest error to the configured destination, then write the run’s meta record and review useful changes.

The Content Factory turns source material into useful work through Produce, Process, Post and Promote. This recipe's reviewed placement is **cross stage support**. Support tasks help the relevant stages; do not force a support operation into a production stage. The canonical article's lower diagram should show the same context while its lead visual explains this particular task.

### Downstream tasks
- No separate mandatory task is established by the reviewed source; use the explicit starting condition and inputs above.
## Example(s)

No independently verified completed execution has been assigned to this new task record. Historical examples in the article remain source material, not reconstructed execution counts. Write the meta article for each real attempt, including failed or blocked work, and register only its actual identity and result.

## Open review items
- Replace optional-public-artifact language with required writing for each execution while retaining the publication gate.
- Working-state examples must keep credentials in the designated secret store, not ordinary notes.
- This is WIP until the current source procedure, access, linked task outputs and live acceptance checks have been independently reviewed. A workflow-summary addition alone does not pass those checks.
- All media tests stay muted with volume zero; if silence cannot be verified before playback, inspect captions, metadata or frames instead.

## Definitive article & links
- Canonical task procedure: https://blitzmetrics.com/persistent-agents/
- Exact Task Library record: https://local-service-spotlight.github.io/task-library/?task=configure-and-verify-recurring-agent-job#task-configure-and-verify-recurring-agent-job
- Meta-article method: https://blitzmetrics.com/meta-article-prompt/
- Recipe and execution relationship: https://localservicespotlight.com/meta-articles/
- Content Factory context: https://blitzmetrics.com/content-factory/
- Article and task recipe standard: https://blitzmetrics.com/definitive-article-guide/

Source basis: canonical article WordPress ID 110662; reviewed source SHA-256 `de27b82e0edeea7771e4fdddb97bc4d34159dad54e5433ea8c797888ec3802c4`. The task record summarizes that source and keeps its unresolved items visible. It does not certify installations, provider commands, source-system access or a completed run.
