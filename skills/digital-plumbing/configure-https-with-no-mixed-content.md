---
name: configure-https-with-no-mixed-content
description: "Make your site use a secure web link. Check that its pictures, forms and pages still work."
category: Digital Plumbing
stage: —
definitive_article: /digital-plumbing
status: needs-work
---

# Configure HTTPS With No Mixed Content

A browser warning can stop a buyer from using your site. This guide helps a site owner fix secure page links and the files they load. Start with the site’s real host and the web addresses people use.

**The path:** Known host → Valid certificate → Secure files → Public checks.

**Use this when:** a site launches, moves hosts, changes domains, or reports certificate or mixed-content warnings.

## Inputs
- The actual host, content delivery service, canonical hostname and required aliases, with supported access for the planned changes.
- The current certificate and renewal configuration, redirect rules and a recoverable before state.
- A representative page list including forms, images, downloads and login paths; the CMS’s actual installation and public URL settings.

## First-run prompt

> Inspect the requested hostnames and their HTTPS setup. Fix supported certificate, redirect or mixed-resource defects in scope, preserving paths and working features. Validate normal public URLs and report renewal configuration separately from future renewal proof.

## Steps
1. List the intended public hostname and aliases actually used by visitors or existing links. Capture current DNS, certificate coverage and redirects. Do not invent extra hostnames or change nameservers for this task.
2. Use the host’s supported certificate flow for those names. Verify the certificate is trusted, covers the names and is valid now. Check the actual renewal job or managed-service setting; a model or a hosting brand alone does not prove renewals will run.
3. Set HTTP-to-HTTPS redirection at the existing owning layer. Preserve the intended path and query, and avoid loops between the edge and origin. A supported permanent redirect may use 301 or 308. Do not add HSTS preload as an unrequested side effect.
4. Check CMS public URL and installation URL settings against the real architecture. They need not be identical when WordPress is installed in a subdirectory. Use the supported source update and backup procedure instead of a blind text replacement in stored database data.
5. Inspect loaded subresources on key pages. Update owned image, script, stylesheet and embed references to working HTTPS endpoints. Ordinary outbound HTTP navigation is a different issue from insecure resources loaded inside an HTTPS page.
6. For a third-party resource without secure support, replace or remove it only within the page’s approved scope and preserve necessary functionality. Do not bypass certificate checks or weaken browser security to hide the failure.
7. Read the normal public pages with network and console evidence. Check for blocked or auto-upgraded insecure resources, and confirm forms, media controls and images still work. Keep all media silent.
8. Verify relevant public redirects again and save final evidence. Check the existing Search Console property scope: a Domain property covers protocols; a URL-prefix property is more specific. Add a new property only if the actual measurement setup needs it.

## Definition of done (QA checklist)

- [ ] Required hostnames have valid trusted certificates and correct canonical redirects.
- [ ] No unintended insecure subresource request remains on the checked pages.
- [ ] Paths, queries, forms and meaningful media survive the changes.
- [ ] Renewal configuration and rollback location are documented without claiming an unobserved future renewal.
- [ ] Public URL, time, representative page coverage and any untested host or feature are recorded.

## Example(s)

**Fictional teaching example.** `http://example.com/repair/?source=card` redirects to the same path and query on HTTPS. The page’s hero image still uses HTTP and the browser upgrades it. The editor changes that source image URL to its working HTTPS address. Afterward, the checked home and repair pages make zero insecure subresource requests. The record says two pages checked; it does not claim every page or the next certificate renewal has been tested.

## Handoff and Content Factory context

Give the final host and redirect map to the site owner. Use [ensure proper dns records](https://local-service-spotlight.github.io/task-library/?task=ensure-proper-dns-records#task-ensure-proper-dns-records) for a DNS mismatch, or [ensure site loads under 3 seconds on mobile](https://local-service-spotlight.github.io/task-library/?task=ensure-site-loads-under-3-seconds-on-mobile#task-ensure-site-loads-under-3-seconds-on-mobile) once secure page delivery works.

This setup supports the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at launch or host/domain changes and when monitoring reports a defect. Certificate renewal needs the actual hosting or certificate service; this guide does not create that service.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/digital-plumbing
- Exact task: [Configure HTTPS With No Mixed Content](https://local-service-spotlight.github.io/task-library/?task=configure-https-with-no-mixed-content#task-configure-https-with-no-mixed-content)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Digital Plumbing training](https://blitzmetrics.com/digital-plumbing/)
- [MDN mixed content](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Mixed_content)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The supplied host’s certificate and cache controls must be verified before real changes.
