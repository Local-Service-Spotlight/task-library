---
name: install-canonical-skill-packs
description: You can try one useful task before adding more tools.
category: Knowledge System Maintenance
stage: —
definitive_article: https://localservicespotlight.com/install/
status: needs-work
---

# Install the canonical skill packs

You can try one useful task before adding more tools. This guide helps you choose the right skill pack and check that it works in your app. Start with the task you want done and the files it needs.

**The path:** Choose one task → Verify package → Install supported parts → Check result

**Start when:** The user wants a supported package available for one bounded task in their actual app.

## Inputs

- One bounded draft task, its real sources and intended result.
- The chosen product/surface/plan and authority for installation or account changes.
- Current [install guide](https://localservicespotlight.com/install/) and [plugin explainer](https://localservicespotlight.com/plugin/).

## Steps

1. Open the maintained install guide and identify the path for the actual app. A guide ZIP and a platform-installable plugin are different packages. A read of a public URL is neither installation nor source-account access.
2. Inspect the current installed package, version and dependent jobs before replacing anything. Preserve a recovery copy and do not uninstall an unknown working setup.
3. For the Claude marketplace path, use the supported marketplace control to add https://github.com/dennisyu/local-service-spotlight-skills and install the reviewed lss-everything package. Confirm this surface and account support that route using current official help; do not substitute a GitHub upload page.
4. Record the package identity and manifest revision. Verify the needed skills are actually listed and enabled; a broad task-library count is not the installed package count.
5. In a fresh task, explicitly select or ask for the intended installed skill. Supply the allowed inputs and request one bounded draft. Record which skill loaded and inspect the actual output against its checks.
6. If the source files cannot be reached, record the exact access gap. Do not copy secrets into prompts or assume an installed skill grants its connectors.
7. Report downloaded, installed, enabled and tested states separately. Set up a recurring job only if requested, through its separate recipe; the first useful manual result is still useful without a schedule.

## Current implementation

For the current Claude marketplace route, open Customize, then Plugins. Under Personal plugins, use the plus control, choose Add marketplace, then Add from a repository. Add [the maintained marketplace](https://github.com/dennisyu/local-service-spotlight-skills), inspect its package, and install `lss-everything`. In Cowork, enter the Cowork tab before opening Customize. Then use `/` or the plus control in a fresh task to select the intended skill. Confirm the actual account has these controls; plugins and every feature they can carry do not have identical support on every surface. [Current official Claude plugin instructions](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

## Definition of done (QA checklist)

[Quality assurance (QA)](https://localservicespotlight.com/article-guidelines/) means checking the work against the agreed result.

- [ ] Canonical package/revision and actual app/account are recorded.
- [ ] The intended skill is observed loading and produces a checked result or an honest failure.
- [ ] Existing setup and access boundaries are preserved; no automatic schedule or update is claimed.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A fictional user can read a guide ZIP and gets a draft from a chat. No installed skill is selected. The result is “guide used for one draft,” not “plugin installed.” After a supported install, a fresh task shows the named skill loaded and its result passes the selected task’s checks; that is separate activation evidence.

## Handoff and Content Factory context

This work supports the [Content Factory, our four stages of using real content](https://blitzmetrics.com/content-factory/): Produce → Process → Post → Promote. Use the specific inputs and next task below to place the work; a maintenance task does not manufacture transcripts, clips or other stage outputs it does not call for.

The user continues with the tested task. [Configure a recurring job](https://local-service-spotlight.github.io/task-library/?task=configure-and-verify-recurring-agent-job#task-configure-and-verify-recurring-agent-job) is optional when repeat work is authorized.

## Run with an agent

Give the AI worker this recipe, the real Inputs above, the intended result and the actions already authorized. Ask it to return the saved output, checks, evidence and remaining owner. Check its work against this guide; loading a skill does not prove access, installation of a job, or successful execution. Keep media muted with volume at zero if playback is needed.

For recurring work, keep the actual trigger, owner and runtime in the job record. Scheduling and observed firings are separate. Do not create a schedule merely because this guide mentions a review interval.

## Record the real execution

Open the run record when the work starts. Keep the exact starting recipe revision, one execution ID, source evidence and actual state. Write a [meta article, the record of one run](https://blitzmetrics.com/meta-article-prompt/) with decisions, results, checks, failures and next owner. Link it to this task and register it through the [Task Library](https://local-service-spotlight.github.io/task-library/) execution process. Writing is part of the work; public release follows existing authority.

Reuse the same execution ID for revisions, QA, meta writing and retries within that run. A blocked run stays open with its dependency and next owner; do not invent a finish time. Use supported findings to propose and verify a better recipe. A historical public-example count without distinct run IDs remains dated article volume, not verified execution frequency.

## Definitive article & links

- [Maintained source guide](https://localservicespotlight.com/install/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=install-canonical-skill-packs#task-install-canonical-skill-packs)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [current article guide](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records work together](https://localservicespotlight.com/meta-articles/)

## Review and evidence still needed

The inherited contributor status is `needs-work`. It is preserved, not promoted by this rewrite. That label alone does not verify document readiness, a client outcome, access or an executed task.

Actual install controls vary by app and plan. No account installation or activation is performed by authoring this guide. The fictional example teaches the method; a real example with relevant proof is still needed where required. The task-specific flow above is source guidance; its visible presentation and the full document need a named reviewer and desktop/mobile checks.
