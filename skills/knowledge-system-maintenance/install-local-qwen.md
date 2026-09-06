---
name: install-local-qwen
description: "A local worker whose endpoint returns the verified test response and can receive a bounded draft task."
category: Knowledge System Maintenance
stage: —
definitive_article: https://blitzmetrics.com/install-local-qwen/
status: needs-work
---

# Install local Qwen

**Use this when:** An authorized Mac user wants the local MLX Qwen worker available for bounded draft work.

This is a registered recipe in review. A published guide or this new record does not certify its runtime behavior. Read the current [canonical procedure](https://blitzmetrics.com/install-local-qwen/) before executing; it contains the detailed actions and current source-specific instructions.

## Inputs
- Compatible local hardware and storage
- The documented model and setup files
- Permission for the download
- A terminal-capable conductor

## Prerequisite tasks
- No separate mandatory task is established by the reviewed source; use the explicit starting condition and inputs above.
## Input references
- [Cursor and Local Qwen Are Not the Same Qwen](https://blitzmetrics.com/cursor-and-local-qwen/)
## Steps
1. Install the documented local stack.
2. Start the loopback server.
3. Run its PONG test.
4. Configure the conductor to call the worker.
5. Keep send, publish and spend decisions with the conductor.

## Definition of done (QA checklist)

**Expected result:** A local worker whose endpoint returns the verified test response and can receive a bounded draft task.

- [ ] The model and endpoint are identified
- [ ] PONG is observed from the local endpoint
- [ ] The service stays on loopback
- [ ] Cursor’s cloud model picker is not mistaken for this local worker
- [ ] Record the exact source revision, actual result and evidence; retain failure, partial, blocked and unknown states.
- [ ] Write the execution's meta article and link the canonical task. Publication is a separate action under the current authority.
- [ ] Keep this parent job's internal retries, checks and agent contributions on the same execution ID; derivatives and revisions add no runs. A separately scoped and documented child execution may have its own ID with parentExecutionId, without adding a second completion to this parent recipe.
- [ ] Verify permissions for publishing, sending, spending, scheduling or changing access before that action. A task record does not grant them.

## Child or companion tasks
- No separate mandatory task is established by the reviewed source; use the explicit starting condition and inputs above.
## Handoff and Content Factory context

The conductor submits a staged drafting task and checks the result before any outside action.

The Content Factory turns source material into useful work through Produce, Process, Post and Promote. This recipe's reviewed placement is **cross stage support**. Support tasks help the relevant stages; do not force a support operation into a production stage. The canonical article's lower diagram should show the same context while its lead visual explains this particular task.

### Downstream tasks
- [How We Run the Content Factory Overnight on a Mac](https://blitzmetrics.com/overnight-content-worker/) — Task Library: [run-overnight-local-writer](https://local-service-spotlight.github.io/task-library/?task=run-overnight-local-writer#task-run-overnight-local-writer)
## Example(s)

No independently verified completed execution has been assigned to this new task record. Historical examples in the article remain source material, not reconstructed execution counts. Write the meta article for each real attempt, including failed or blocked work, and register only its actual identity and result.

## Open review items
- Exact commands are current-source evidence, not revalidated in this audit. No install or model download has been run.
- This is WIP until the current source procedure, access, linked task outputs and live acceptance checks have been independently reviewed. A workflow-summary addition alone does not pass those checks.
- All media tests stay muted with volume zero; if silence cannot be verified before playback, inspect captions, metadata or frames instead.

## Definitive article & links
- Canonical task procedure: https://blitzmetrics.com/install-local-qwen/
- Exact Task Library record: https://local-service-spotlight.github.io/task-library/?task=install-local-qwen#task-install-local-qwen
- Meta-article method: https://blitzmetrics.com/meta-article-prompt/
- Recipe and execution relationship: https://localservicespotlight.com/meta-articles/
- Content Factory context: https://blitzmetrics.com/content-factory/
- Article and task recipe standard: https://blitzmetrics.com/definitive-article-guide/

Source basis: canonical article WordPress ID 113272; reviewed source SHA-256 `bc6abe383b309a4ae1a7a27dd8443cc7c162cf4f2897f2bc7847e598c3b6309a`. The task record summarizes that source and keeps its unresolved items visible. It does not certify installations, provider commands, source-system access or a completed run.
