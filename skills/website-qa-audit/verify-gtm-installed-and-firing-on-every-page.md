---
name: verify-gtm-installed-and-firing-on-every-page
description: "Check that the site loads the right tag tool. Then check the tags and where their data goes."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify GTM installed and firing on every page

A code snippet alone does not prove your site reports visits. This guide helps you check the tag tool and the data it sends. Start with the real tracking plan and the pages it covers.

**The path:** Expected container → Loaded code → Intended tag events → Real destination evidence.

**Use this when:** A site that uses Google Tag Manager needs its installation and intended tag behavior audited. GTM loads configured tags according to their triggers and consent rules.

## Inputs
- The exact site/page inventory, expected web-container IDs and intended measurement plan.
- Authorized read access to the relevant GTM container/version plus supported page and tag tools.
- The actual required tags, triggers, consent behavior and downstream destination IDs.
- A scope for repairs, publication and test interactions, plus a record of source and live versions.

## First-run prompt

> Use the supplied tracking plan, container and page inventory. Check source presence, actual container load, intended tag behavior and downstream evidence separately. Preserve consent and version boundaries, complete already-authorized fixes/publication, and return exact coverage and remaining test gaps.

## Steps
1. Confirm the actual architecture and expected container. A site may use a direct Google tag or another supported setup; missing GTM is not automatically a failure when the measurement plan does not require it. Do not install a new container just to satisfy this task label.
2. Reconcile the scoped published page list with crawl coverage. Inspect expected web snippets and IDs in the normal served source, using the supported integration. For a standard web container, the documented script belongs high in head and the noscript fallback after the opening body.
3. Check the running page with Tag Assistant or supported diagnostics. Record container loading separately from source presence. A static fetch that finds GTM- text does not prove a browser loaded the container.
4. Inspect each intended tag’s trigger and consent condition. Run only the test interactions already in scope and record fired/not-fired reasons. A lead tag should not be forced to fire on every page load; a legitimate consent block is not an instruction to bypass consent.
5. Distinguish preview from normal live delivery. GTM Preview may run an unpublished draft. Record the previewed version and check the actual published configuration used by a normal visitor before claiming production behavior.
6. Look for unintended duplicate installations or events. Exactly one expected path is a useful simple-site design, but multiple intentionally documented containers are not automatically wrong. Follow the real architecture and avoid removing another valid owner’s tag.
7. Where the job includes end-to-end measurement, verify the intended destination received the controlled event with matching context. Container loaded, tag fired and destination received are three separate evidence fields.
8. Repair authorized exact-source/tag issues, publish only when that change is already in scope, and recheck normal canonical pages and relevant destinations. Report page coverage and every remaining unknown instead of saying every downstream tag works because GTM is present.

## Definition of done (QA checklist)

- [ ] The actual required architecture, IDs and page coverage are documented.
- [ ] Snippet presence, container load, tag firing and destination receipt are separate checks.
- [ ] Preview success is not mistaken for the published normal-visitor result.
- [ ] Trigger/consent rules and intentional multi-container designs are preserved.
- [ ] Authorized changes have actual canonical/version evidence; untested pages/events remain explicit.

## Example(s)

**Fictional teaching example — no tag was executed.** Maple Cycle’s source contains the expected GTM ID, and the browser loads that container. In Preview, a new quote event fires, but the normal published version does not contain it yet.

The installation check can pass while the new event remains preview-only. The report still needs an authorized published version and actual receiver evidence before claiming the new quote event works live. It must not generate a fake customer quote just to make an event appear.

## Handoff and Content Factory context

The measurement owner receives the page/version/tag map. [Verify GA4 receipt and internal-traffic treatment](https://local-service-spotlight.github.io/task-library/?task=verify-ga4-configured-with-internal-traffic-filtered#task-verify-ga4-configured-with-internal-traffic-filtered) handles the Analytics-specific destination checks; other tags use their own scoped tests.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at installation and after relevant templates, container versions, triggers or consent rules change. Repeated checks need an actual configured job and stored version map, not guaranteed model persistence.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify GTM installed and firing on every page](https://local-service-spotlight.github.io/task-library/?task=verify-gtm-installed-and-firing-on-every-page#task-verify-gtm-installed-and-firing-on-every-page)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Google Tag Manager web-container installation](https://support.google.com/tagmanager/answer/14847097?hl=en-AU)
- [Google Tag Manager preview and debug](https://support.google.com/tagmanager/answer/6107056?hl=en)
- [Google Analytics DebugView](https://support.google.com/analytics/answer/7201382?hl=en)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual tracking architecture, current published version, event test scope and destination evidence require the project.
