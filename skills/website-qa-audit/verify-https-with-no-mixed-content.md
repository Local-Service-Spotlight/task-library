---
name: verify-https-with-no-mixed-content
description: "Check that pages and their files use safe web links. Find the exact source of a browser warning."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify HTTPS with no mixed content

A browser warning can keep people from using your site. This guide helps you check that pages and their files load over HTTPS. Start with the real public URLs and the host names the site uses.

**The path:** Canonical page → Host variants → Loaded resources → Exact fix and recheck.

**Use this when:** A launch, migration or defined site audit needs HTTPS delivery and mixed-content checks.

## Inputs
- The canonical URL list and actual supported host variants, plus known embedded forms/media/widgets.
- A browser with connection, network and console diagnostics, and an available scoped crawl report.
- The supported page/server configuration sources and authorized repair scope.
- A before-state record and the technical owner for certificate, DNS or delivery issues outside the current edit.

## First-run prompt

> Inspect the supplied canonical pages and configured host variants. Record connection, redirect and actual insecure-resource evidence. Make authorized supported-source fixes, preserve browser protections, and return normal visitor rechecks plus exact remaining technical owners.

## Steps
1. Define the canonical HTTPS host and scoped URL set. Record which www/non-www and old host aliases are actually configured; do not invent new DNS records merely to test a hypothetical variant.
2. Open the normal HTTPS page and inspect the browser’s connection details and any certificate error. Modern browsers may use a site-controls icon instead of a padlock. A familiar icon is not the whole evidence record, and an HTTPS connection does not certify the content or business.
3. Check the configured HTTP and alternate-host variants for the intended permanent canonical redirect, preserving page path where appropriate. A valid 308 can be appropriate as well as 301; record loops, wrong targets and unnecessary chains instead of enforcing one status code universally.
4. Inspect actual resource requests and relevant console messages while viewing representative templates and the rest of the agreed scope. HTTPS pages that load insecure subresources can have mixed content even when the main page uses HTTPS.
5. Record each insecure resource, its initiating page/source and browser behavior. Some requests are auto-upgraded, others blocked. A plain text http URL or top-level navigation link is not automatically the same as an insecure loaded script or image.
6. Trace the issue to the supported markup, theme setting, stylesheet or integration. Confirm a valid HTTPS resource exists before changing it. Do not blindly replace every string in serialized builder data or change global security controls to suppress a warning.
7. Apply exact authorized repairs and use the supported publishing/cache route if needed. For a certificate or host problem beyond the current scope, provide the responsible owner the exact hostname and observed failure rather than bypassing the warning.
8. Recheck normal canonical pages, redirects and affected resources in the browser after saving. Retain coverage, source revision and unresolved warnings; a static scan alone cannot prove all scripts/widgets executed safely.

## Definition of done (QA checklist)

- [ ] Scoped pages have valid HTTPS connection evidence and intended canonical redirects.
- [ ] Actual loaded subresources and browser behavior are checked, with literal text/ordinary links distinguished.
- [ ] Repairs use valid secure targets and preserve supported data formats and controls.
- [ ] Changed canonical responses and resource loads are rechecked after publication.
- [ ] Coverage and remaining certificate/host/resource gaps are explicit without a whole-site security guarantee.

## Example(s)

**Fictional teaching example — no server was tested.** Maple Cycle’s guide loads over HTTPS. Its logo request uses HTTP and is upgraded by the browser, while an old booking iframe is blocked. A body link to an old historical article is ordinary navigation, not a loaded iframe.

The teaching repair checks the correct secure logo and booking endpoints, updates their supported sources and verifies the actual requests. Changing a browser setting to allow insecure content would not fix the visitor’s page.

## Handoff and Content Factory context

The site technical owner receives certificate, redirect or resource issues. [Check mobile performance](https://local-service-spotlight.github.io/task-library/?task=test-mobile-load-time-under-3-seconds#task-test-mobile-load-time-under-3-seconds) can verify a relevant delivery change without substituting a speed score for HTTPS checks.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at launch and after relevant host, certificate, resource or template changes. A continuing monitor requires its real configured scope and cadence.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify HTTPS with no mixed content](https://local-service-spotlight.github.io/task-library/?task=verify-https-with-no-mixed-content#task-verify-https-with-no-mixed-content)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [MDN mixed content](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Mixed_content)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual host/certificate state, supported repair access and canonical resource evidence require the site.
