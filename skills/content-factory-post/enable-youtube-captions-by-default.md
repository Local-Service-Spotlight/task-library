---
name: enable-youtube-captions-by-default
description: "An embed with the intended caption parameters and truthful caption availability."
category: Content Factory — Post
stage: Post
definitive_article: https://blitzmetrics.com/youtube-captions-on-by-default/
status: needs-work
---

# Enable YouTube captions by default

**Use this when:** A page contains a YouTube embed that should offer its available captions by default.

This is a registered recipe in review. A published guide or this new record does not certify its runtime behavior. Read the current [canonical procedure](https://blitzmetrics.com/youtube-captions-on-by-default/) before executing; it contains the detailed actions and current source-specific instructions.

## Inputs
- Verified YouTube video ID
- Existing player or facade markup
- Available caption track and intended language

## Prerequisite tasks
- No separate mandatory task is established by the reviewed source; use the explicit starting condition and inputs above.
## Input references
- [Article guidelines (how we write, and how your agent should)](https://localservicespotlight.com/article-guidelines/)
## Steps
1. Use the privacy-enhanced embed host.
2. Add rel=0 and caption parameters.
3. Keep first paint silent and require a click before autoplay.
4. Match the actual player and schema embed URL.
5. Verify the available caption behavior without inventing a track.

## Definition of done (QA checklist)

**Expected result:** An embed with the intended caption parameters and truthful caption availability.

- [ ] cc_load_policy=1 and the language preference are present
- [ ] First paint does not autoplay with sound
- [ ] The video ID is correct
- [ ] Missing captions remain missing; player captions are not quote evidence
- [ ] Record the exact source revision, actual result and evidence; retain failure, partial, blocked and unknown states.
- [ ] Write the execution's meta article and link the canonical task. Publication is a separate action under the current authority.
- [ ] Keep this parent job's internal retries, checks and agent contributions on the same execution ID; derivatives and revisions add no runs. A separately scoped and documented child execution may have its own ID with parentExecutionId, without adding a second completion to this parent recipe.
- [ ] Verify permissions for publishing, sending, spending, scheduling or changing access before that action. A task record does not grant them.

## Child or companion tasks
- No separate mandatory task is established by the reviewed source; use the explicit starting condition and inputs above.
## Handoff and Content Factory context

Continue article QA and use the full source transcript for any quoted text.

The Content Factory turns source material into useful work through Produce, Process, Post and Promote. This recipe's reviewed placement is **post**. Support tasks help the relevant stages; do not force a support operation into a production stage. The canonical article's lower diagram should show the same context while its lead visual explains this particular task.

### Downstream tasks
- [step 17 final formatting and qa checks](https://local-service-spotlight.github.io/task-library/?task=step-17-final-formatting-and-qa-checks#task-step-17-final-formatting-and-qa-checks)
## Example(s)

No independently verified completed execution has been assigned to this new task record. Historical examples in the article remain source material, not reconstructed execution counts. Write the meta article for each real attempt, including failed or blocked work, and register only its actual identity and result.

## Open review items
- This is WIP until the current source procedure, access, linked task outputs and live acceptance checks have been independently reviewed. A workflow-summary addition alone does not pass those checks.
- All media tests stay muted with volume zero; if silence cannot be verified before playback, inspect captions, metadata or frames instead.

## Definitive article & links
- Canonical task procedure: https://blitzmetrics.com/youtube-captions-on-by-default/
- Exact Task Library record: https://local-service-spotlight.github.io/task-library/?task=enable-youtube-captions-by-default#task-enable-youtube-captions-by-default
- Meta-article method: https://blitzmetrics.com/meta-article-prompt/
- Recipe and execution relationship: https://localservicespotlight.com/meta-articles/
- Content Factory context: https://blitzmetrics.com/content-factory/
- Article and task recipe standard: https://blitzmetrics.com/definitive-article-guide/

Source basis: canonical article WordPress ID 113738; reviewed source SHA-256 `9ed0bf10e1d6e0d3552c82ae386e40414bbb938642220ecdd7954241f7818e9e`. The task record summarizes that source and keeps its unresolved items visible. It does not certify installations, provider commands, source-system access or a completed run.
