---
name: audit-local-service-website
description: "Find what helps or blocks a customer on your site. Leave a clear list of facts, fixes and next owners."
category: Website QA Audit
stage: —
definitive_article: https://blitzmetrics.com/website-audit-checklist/
status: needs-work
---

# Audit a local-service website

Your site should help customers reach your business. This guide helps you check the pages, lead path and systems behind that job. Start with the main action you want a customer to take.

**The path:** Business job → Real customer path → Measured systems → Testable fix plan.

**Use this when:** A local-service site needs a functional baseline before repairs, a redesign or an architecture/migration decision.

## Inputs
- The exact in-scope business/site, current roster/engagement status and primary services, service areas and customer action.
- The real lead destination and receiving owner, plus authorized test identities, measurement access and submission scope.
- Current platform, CMS, hosting, dependency/license and supported publishing records, with existing recovery/export evidence.
- The agreed audit scope, last baseline if any, actual report recipient and authority for repairs or delivery.

## First-run prompt

> Audit the supplied local-service site against its real customer job and approved test scope. Check public pages, lead routing, measurement, search controls, delivery and recovery evidence. Complete authorized repairs/delivery, preserve unknowns, and leave a testable baseline with exact next owners before recommending an architecture change.

## Steps
1. Confirm the client/site is authorized under the current roster and engagement. Define the business job: call, inquiry, booking or purchase, and what counts as a received/qualified outcome. Do not choose a new host or CMS before understanding that baseline.
2. Inspect the canonical pages as a visitor on desktop and phone. Check clear services/areas, grade-5 opening context, meaningful first-screen visuals, navigation, real proof, usable controls and relevant media without audible playback. Record page-level evidence and scope.
3. Trace the primary lead path using [CTA checks](https://local-service-spotlight.github.io/task-library/?task=check-all-cta-buttons-lead-to-correct-destinations#task-check-all-cta-buttons-lead-to-correct-destinations) and, where appropriate, [form-flow checks](https://local-service-spotlight.github.io/task-library/?task=verify-email-opt-in-form-exists-and-works#task-verify-email-opt-in-form-exists-and-works). Perform real calls, sends, bookings or purchases only if already included in the job’s controlled test plan. Confirm receiver/CRM routing separately from a success screen.
4. Check measurement ownership and the actual event path. Distinguish browser/tag activity from destination receipt and real leads. Use the relevant GA4/GTM/Pixel task only when that architecture is present; record unavailable account evidence rather than installing a default stack.
5. Review served search controls and identity: useful title/description, canonical URLs, robots rules, sitemap and appropriate business/schema facts. Check important redirects against their actual destinations. Use current per-check criteria, not a combined score from unrelated audit frameworks.
6. Record actual delivery and recovery: HTTPS, publishing layers, backup/export location, retention and the responsible recovery owner. Inspect existing restore evidence. A provider logo or a backup file is not a tested recovery; do not restore production during a baseline audit.
7. Map each used plugin, snippet, integration and fee to its business function and owner. Flag unknown, unused or license/access gaps. For a proposed migration, list acceptance tests for all current dynamic behavior and retain the source/rollback path until the separately authorized change passes them.
8. Produce the baseline with pass/fail/unknown/not-applicable per defined check, exact evidence, severity and next owner. Carry out repairs already authorized and recheck the public result. Deliver only to the verified recipient/channel already in scope, with a real receipt; staged output remains a draft.

## Definition of done (QA checklist)

- [ ] The business job, site scope and actual lead receiver are defined.
- [ ] Public experience and authorized lead tests have specific evidence, with delivery distinct from visible success.
- [ ] Measurement/search controls reflect the actual architecture and current criteria.
- [ ] Dependencies, recovery and migration acceptance needs are explicit; unknown proof is not a guarantee.
- [ ] The dated baseline, repaired/public states, remaining owners and actual delivery state are recorded.

## Example(s)

**Fictional teaching example — no business site was audited.** Maple Cycle wants repair inquiries. Its phone link is correct, its form shows success, but the sample CRM record is absent. Analytics records a button click, and a backup ZIP exists without a restore receipt.

The baseline says “phone target checked; live call untested,” “form delivery failed/pending investigation,” “click received, accepted inquiry not proven,” and “backup available, restore untested.” The next fix belongs to the form/CRM owner. Moving hosts would not by itself prove any of those functions now work.

## Handoff and Content Factory context

The site/business owner receives the baseline and prioritized defects. The exact failed function determines the next task. A proposed migration uses this baseline as acceptance evidence; this local-service guide supports the [Website QA master](https://blitzmetrics.com/website-qa-audit/) and does not become a competing audit trunk.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run for an initial baseline or a defined review/change. Repeated site QA needs its actual agreed schedule; this guide does not activate monitoring, migration or new paid services.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-audit-checklist/
- Exact task: [Audit a local-service website](https://local-service-spotlight.github.io/task-library/?task=audit-local-service-website#task-audit-local-service-website)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual client scope, supported systems access, controlled test receipts, dependency ownership and recovery evidence require the site.
- No independently verified completed execution is added by this authored candidate; the source contributor state remains needs-work.
