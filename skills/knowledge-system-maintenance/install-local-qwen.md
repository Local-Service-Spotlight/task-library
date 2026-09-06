---
name: install-local-qwen
description: A local AI worker can help draft text on your Mac.
category: Knowledge System Maintenance
stage: —
definitive_article: https://blitzmetrics.com/install-local-qwen/
status: needs-work
---

# Install local Qwen

A local AI worker can help draft text on your Mac. This guide shows how to set it up and check one small reply. Start by checking your Mac, free space, and the exact model you plan to use.

**The path:** Check Mac → Install reviewed stack → Local test → Bounded draft

**Start when:** An authorized Mac user wants the documented local worker for bounded draft work.

## Inputs

- An Apple Silicon Mac, available memory/storage, Python 3.11 and permission for the model download.
- The exact documented checkpoint mlx-community/Qwen3.8-27B-4bit and reviewed setup revision.
- An authorized terminal, a local working folder and a lead AI worker that can make a local web request.

## Steps

1. Read the owned install guide and the model card. Record hardware, free resources and model revision. The published 128 GB-Mac result is historical; it does not prove this machine has enough memory.
2. Use a dedicated environment for the reviewed stack. Preserve an existing installation and active jobs. The concrete commands below reproduce the documented Python 3.11/MLX-VLM path; confirm compatibility before replacing an environment.
3. Download the exact checkpoint through its supported model source under the approved download scope. Record model identity and errors. HF_HUB_DISABLE_XET=1 was a workaround on the documented Mac, not a universal requirement.
4. Start the server bound to 127.0.0.1 on the agreed port. Inspect startup output and confirm the intended process owns the listener. Do not expose or tunnel the unauthenticated local service.
5. Request the model list, then send one bounded “Reply with PONG” test to the returned model ID. Save the status code, response and time. A model-list response alone proves no text generation.
6. Ask for one small draft from allowed test text and check its facts. The local endpoint is the worker; a cloud model with a similar name or a Cursor picker entry does not prove this endpoint ran.
7. Give the lead AI worker the actual endpoint/model and a failure path. Keep drafts staged; send, publish and spend stay under existing authority. Record how to stop the process and do not install a startup job unless requested.

## Current implementation

The owned guide documents this stack from its August 2026 setup. Run these commands from the reviewed team setup folder that contains its requirements.txt. The owned guide identifies that private checkout; access must already be granted. If it is unavailable, obtain that approved setup or follow the official upstream install path and record it as a different environment. The commands below are instructions, not evidence that this audit installed it. Keep the process local. The model card and [MLX-VLM documentation](https://github.com/Blaizzy/mlx-vlm) explain the loader; [the exact model card](https://huggingface.co/mlx-community/Qwen3.8-27B-4bit) identifies the checkpoint. Do not generalize that checkpoint’s mlx-lm loading failure to every Qwen model.

```bash
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m mlx_vlm.server --help
.venv/bin/python -m mlx_vlm.server --model mlx-community/Qwen3.8-27B-4bit --host 127.0.0.1 --port 8080
```

Use the actual installed server’s `--help` to verify its controls before starting it. The server stays in that terminal; use a second terminal for the two read/test requests:

```bash
curl -sS --max-time 120 http://127.0.0.1:8080/v1/models -H 'Authorization: Bearer local'
curl -sS --max-time 120 http://127.0.0.1:8080/v1/chat/completions -H 'Authorization: Bearer local' -H 'Content-Type: application/json' -d '{"model":"mlx-community/Qwen3.8-27B-4bit","messages":[{"role":"user","content":"Reply with PONG only."}],"max_tokens":16,"temperature":0,"enable_thinking":false}'
```

The small probe explicitly turns thinking off, matching the documented team wrapper; otherwise a short token budget may yield no visible reply. Match the model ID to the model list. Review the completion itself and retain a failed response honestly. Stop the server with the terminal’s interrupt control when the test is over unless the authorized job needs it left running. The `qwen` convenience wrapper is only available if that separate team setup was actually installed.

## Definition of done (QA checklist)

[Quality assurance (QA)](https://localservicespotlight.com/article-guidelines/) means checking the work against the agreed result.

- [ ] Exact checkpoint, environment and loopback listener are identified.
- [ ] A real completion returns the test reply; a bounded draft is independently checked.
- [ ] Errors, resource limits and shutdown method are recorded; no automatic scheduling or savings claim is made.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A fictional setup returns the expected model ID but its PONG request times out. Record “server visible, generation failed.” Do not claim the worker is usable or rerun downloads blindly. Diagnose the retained error and resources before retrying the same setup task.

## Handoff and Content Factory context

This work supports the [Content Factory, our four stages of using real content](https://blitzmetrics.com/content-factory/): Produce → Process → Post → Promote. Use the specific inputs and next task below to place the work; a maintenance task does not manufacture transcripts, clips or other stage outputs it does not call for.

The lead AI worker receives the checked endpoint and draft limits. [An overnight drafting task](https://local-service-spotlight.github.io/task-library/?task=run-overnight-local-writer#task-run-overnight-local-writer) is separate work requiring its own schedule and output checks.

## Run with an agent

Give the AI worker this recipe, the real Inputs above, the intended result and the actions already authorized. Ask it to return the saved output, checks, evidence and remaining owner. Check its work against this guide; loading a skill does not prove access, installation of a job, or successful execution. Keep media muted with volume at zero if playback is needed.

For recurring work, keep the actual trigger, owner and runtime in the job record. Scheduling and observed firings are separate. Do not create a schedule merely because this guide mentions a review interval.

## Record the real execution

Open the run record when the work starts. Keep the exact starting recipe revision, one execution ID, source evidence and actual state. Write a [meta article, the record of one run](https://blitzmetrics.com/meta-article-prompt/) with decisions, results, checks, failures and next owner. Link it to this task and register it through the [Task Library](https://local-service-spotlight.github.io/task-library/) execution process. Writing is part of the work; public release follows existing authority.

Reuse the same execution ID for revisions, QA, meta writing and retries within that run. A blocked run stays open with its dependency and next owner; do not invent a finish time. Use supported findings to propose and verify a better recipe. A historical public-example count without distinct run IDs remains dated article volume, not verified execution frequency.

## Definitive article & links

- [Maintained source guide](https://blitzmetrics.com/install-local-qwen/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=install-local-qwen#task-install-local-qwen)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [current article guide](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records work together](https://localservicespotlight.com/meta-articles/)

## Review and evidence still needed

The inherited contributor status is `needs-work`. It is preserved, not promoted by this rewrite. That label alone does not verify document readiness, a client outcome, access or an executed task.

No model download, installation, PONG request or current hardware test was performed while writing this guide. The checkpoint’s actual capacity and compatibility require a real authorized run. The fictional example teaches the method; a real example with relevant proof is still needed where required. The task-specific flow above is source guidance; its visible presentation and the full document need a named reviewer and desktop/mobile checks.
