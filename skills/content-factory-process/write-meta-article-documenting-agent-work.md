---
name: write-meta-article-documenting-agent-work
description: Write the evidence-backed record of each task execution and connect it to its canonical recipe and Task Library record.
category: Content Factory — Process
stage: Process
definitive_article: https://blitzmetrics.com/meta-article-prompt/
status: complete
---

# Write a meta article documenting a task execution

## Inputs
Run this as part of closing each task execution, including partial and failed results. Have the stable task ID, execution ID, recipe URL and revision, starting state, inputs, actual output, checks, decisions, failures, owner, and next task. Use UNKNOWN for unmeasured time, tokens, costs, or outcomes. Publication authority is an input to release, not to writing the record.

## Steps
1. Preserve the execution evidence and the private organization agent-note when required.
2. Write the meta article: who/what the task served, why it started, the starting condition, inputs, recipe followed, actual steps, decisions, output, acceptance evidence, failures, lessons, and next handoff.
3. Explain unfamiliar terms on first mention and link to the maintained owned guide. Link to the one primary task recipe, detailed sub-tasks used, and the exact Task Library record.
4. Show the real result with meaningful images or diagrams, clear captions, and an accessible link to the deliverable when sharing it is authorized. Follow https://localservicespotlight.com/article-guidelines/.
5. Check the article against this recipe. Record PASS, PARTIAL, FAIL, NOT CHECKED, or NEEDS HUMAN from evidence. Do not copy a pre-passed scorecard.
6. Register the execution ID and its task mapping, recipe revision, result, evidence, and meta article state. Revisions and internal retries keep the same parent execution ID; a separately scoped later attempt needs its own actual evidence and ID. The writing step is part of its original run, not a new meta-of-meta task unless separately scoped.
7. Keep the article private or in draft when needed. Publish a public-safe version only under the recorded authority; verify the exact live page and update the publication state. Do not place private evidence URLs in a public registry.
8. Send the verified result to the next task or receiving function under the required communication authority. Turn a supported lesson into a proposed recipe/skill change; review and test it before making the accepted revision current.

## Definition of done (QA checklist)
- One execution record has a stable task and execution ID and links the canonical recipe revision.
- The meta article states the actual result and evidence for each acceptance check; partial and failed results stay visible.
- Inputs, decisions, failures, unavailable telemetry, and next owner/action are stated.
- The public/private/draft state is explicit, and a published page has a verified live read-back.
- The required internal agent-note is written and verified separately.
- The Task Library can link this run to its recipe. One run's revisions do not increase execution frequency.

## What happens next
The receiving task starts only after its own prerequisites are met. Review repeated failures and useful lessons to improve the canonical method. The next execution uses that accepted revision.

## Example(s)
The current article-cleanup run is still in progress. Its agent notes support one parent execution; no completed count is claimed here.

## Definitive article & links
- Relationship explainer: https://localservicespotlight.com/meta-articles/
- Recipe standard: https://blitzmetrics.com/definitive-article-guide/
- Factory context: https://blitzmetrics.com/content-factory/
- Task Library: https://local-service-spotlight.github.io/task-library/?task=write-meta-article-documenting-agent-work
