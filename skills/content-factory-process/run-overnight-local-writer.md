---
name: run-overnight-local-writer
description: "Use a local model to draft from your saved source. Check one small job before you leave a batch running."
category: Content Factory — Process
stage: Process
definitive_article: /overnight-content-worker
status: complete
---

# Run overnight local writer

A stack of videos can mean a lot of writing. This guide helps you use a local model for first drafts while you keep control of the work. Start with one source and a small checked test.

**The path:** Checked source queue → One isolated test → Local draft batch → Real review and Post handoff.

**Use this when:** A real source backlog is assigned to the installed Overnight Content Worker for draft preparation, with a named owner and bounded batch.

## Inputs
- The actual Overnight Content Worker checkout, README/INSTALL and script revision, not this Markdown task file alone.
- The client folder, verified source transcripts, voice, entity map and actual accountable owner. Confirm current client status from the maintained roster before client work.
- A known local endpoint/model already installed, permitted device resources and a compatible adapter; no model download is part of this task by default.
- Queue/lock files, one named worker, batch limit, durable output folder and morning review owner.

## First-run prompt

> Inspect the supplied installed worker, queue and local model settings without running a batch yet. Separate fixture dry-run effects from real jobs. Prepare one bounded real test only within existing authority, check its full source-derived draft, and report actual output/error states. Keep publication on the maintained reviewed Post route and do not assume memory, endpoint locality or a working timer.

## Steps
1. Read the current worker code and setup files. Identify the real client folder, source queue and output paths. Keep credentials outside the model inputs. Verify authority and roster status; do not treat billing or a public directory as the client roster.
2. Inspect the current queue and process ownership before work. The reviewed status.py can expire/requeue leases, so it is not a purely read-only probe. One machine/worker per client is the operational constraint; file locks on one Mac do not coordinate independent copies on two Macs.
3. Verify the configured model destination and exact model ID. The reviewed adapter accepts OPENAI_BASE_URL without proving it is local, and it does not send the API key advertised in its docstring. Use an actually compatible local endpoint; do not send client text to an unknown remote URL or guess that a generic qwen alias exists.
4. Check source/transcript, voice and guidelines completeness before claiming work. The current script truncates long inputs and uses a guidelines excerpt; split or prepare a supported bounded job if needed, rather than claiming every source detail was read.
5. Use a copied fixture workspace with only labeled sample jobs for the first no-model exercise. In the reviewed version, night.py --dry-run still claims queue jobs, writes stub drafts and pass QA, and marks them drafted. Never use it as a harmless rehearsal on a production queue or send its stubs to the morning publisher.
6. For a real local test, run one permitted job using the installed script’s documented client and limit arguments. Confirm the actual model responds, the output is not a dry-run stub, and the requested thinking setting took effect. Save observed time and usage only when measured. Do not install another server or retry a timed-out large batch without resolving the observed problem.
7. Read the entire first draft against source and current standards. The worker’s mechanical checks and model self-score are hints, not editorial certification. Its implementation makes one rewrite attempt and then uses needs_human for continuing failures; record that state rather than inflating done counts.
8. Only after the small job is accepted, run the agreed bounded batch with one worker and a real stop condition. Track source IDs, drafted/failed/needs_human states, source truncation and any stuck claims. Do not clear another active worker’s lock just to proceed.
9. Do not publish live from the Mac worker. Hand checked Markdown and evidence to the maintained Post workflow. The reviewed morning.py makes draft POSTs with simple text/player conversion and lacks a prior-post lookup before retry; do not run it blindly on the queue. Fix and review that publishing path first, or use the existing supported WordPress task for the exact checked draft.
10. Close with actual output counts, unresolved jobs and the next reviewer. A two-minute review and a predicted overnight yield are estimates, not acceptance criteria. An overnight timer is optional and needs configured paths, overlap protection, a first-firing receiver and observed result.

## Definition of done (QA checklist)

- [ ] The real source/setup revision, local destination and client owner are known.
- [ ] Fixture outputs are isolated from production and never counted as real drafts.
- [ ] A real small job has source/voice/format review before batch scale-up.
- [ ] Actual output/error states and Post handoff are recorded; no model, lock or schedule guarantee is assumed.

## Example(s)

**Fictional teaching example — no worker was run.** A fixture queue contains one sample bike transcript. The operator runs the installed `night.py --client SAMPLE_CLIENT --n 1 --dry-run` only in that isolated copy. It creates a document labeled DRY RUN and a queue state called drafted. The operator records “fixture plumbing exercised,” not “article completed.”

For a later real job, a source-checked draft may be handed to the publisher. A generated file with a pass JSON but a missing source paragraph still fails editorial review. The example client identifier must be replaced by a real fixture or authorized job, never copied into a production command by guess.

## Handoff and Content Factory context

The named reviewer checks the source and draft, then uses [Proofread the complete draft](https://local-service-spotlight.github.io/task-library/?task=step-11-proofread-with-grammarly-or-chatgpt#task-step-11-proofread-with-grammarly-or-chatgpt) and [the supported WordPress task](https://local-service-spotlight.github.io/task-library/?task=step-12-post-article-on-wordpress#task-step-12-post-article-on-wordpress). The harness owner receives specific code defects; repairing those is not proven by this guide.

Produce supplies the real source. **Process**, this stage of the [Content Factory](https://blitzmetrics.com/content-factory/), turns it into useful finished assets. Post saves or publishes them on the agreed channels. Promote tests and distributes suitable work within its own scope. The handoff above names this task’s actual next step; catalog neighbors alone are not prerequisites.

## When this runs

One bounded source batch, optionally at night. Scheduled operation requires separate real setup and first-firing proof; a guide or local model never schedules itself.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/overnight-content-worker
- Exact task: [Run overnight local writer](https://local-service-spotlight.github.io/task-library/?task=run-overnight-local-writer#task-run-overnight-local-writer)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Overnight worker and its maintained setup](https://blitzmetrics.com/overnight-content-worker/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The existing worker requires reviewed first-run/queue/publication safeguards before unattended production. No local Qwen retry or real worker test was run for this candidate.
