---
name: verify-email-opt-in-form-exists-and-works
description: "Check that a sign-up form does what it promises. Trace a test from the page to the right inbox."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify email opt-in form exists and works

A sign-up box should do more than show a success message. This guide helps you check that the right list and promised email receive a test. Start with the real form, its offer and a test inbox you control.

**The path:** Offer and form → Authorized test → List and email evidence → Exact result.

**Use this when:** A site’s agreed email-sign-up offer needs an end-to-end test before launch or after a relevant change.

## Inputs
- The scoped form placements and actual promised outcome, including whether an opt-in is part of this site’s plan.
- The connected email platform/list, supported form settings, relevant access and exact designated test receiver.
- Existing authority for the test submission and its expected downstream messages; the duplicate/cleanup plan for test records.
- The actual offered file/link, expected notifications and current consent/confirmation flow.

## First-run prompt

> Review the supplied form, offer, platform and test plan. Complete already-authorized tests on desktop and phone, verify list/confirmation/message states separately, and fix scoped faults. Return exact evidence and remaining access or delivery issues without exposing private addresses or creating duplicate tests.

## Steps
1. List every distinct form and placement in scope, including mobile-only versions. If the approved site plan has no email opt-in, record the product decision rather than creating a form to satisfy an old universal checklist.
2. Read the promise and current flow. Record the expected list, confirmation step, owner notification if configured, and lead-magnet delivery. Do not assume every form uses immediate single opt-in or must send an owner notification.
3. Check the page layout, labels, validation and privacy/consent text. Verify the actual connected destination in the supported settings before a live test. If the job is read-only, complete those checks and leave submission/delivery explicitly untested.
4. For an authorized end-to-end test, use the designated controlled address and a recognizable test reference. Confirm no other worker has just submitted the same test. Submit once from the specified desktop flow and record its actual success/error state.
5. Read back the platform record and its exact subscription state. A pending double-opt-in contact is not an active subscriber until the intended confirmation is completed. Keep API/form success separate from the actual list record.
6. Check the test inbox for the promised message, working resource link and any configured owner notification. Record delay, bounce, spam placement or missing delivery. Do not call dispatch or a thank-you screen delivered email.
7. Repeat the required phone flow with a planned separate test identity or the platform’s known existing-contact behavior, so duplicate suppression does not look like a new delivery failure. Fix already-authorized settings and re-test the changed step without flooding the list.
8. Record each placement/flow result, actual recipient/list evidence, checked time and test-record cleanup under the existing plan. Any follow-up timer or cleanup send must be part of that plan; do not unsubscribe or remove a real customer.

## Definition of done (QA checklist)

- [ ] The actual offer and expected form flow are stated, with no invented universal opt-in requirement.
- [ ] Each in-scope test distinguishes page success, platform record, confirmation state and delivered message.
- [ ] Desktop and phone evidence use a controlled duplicate-aware test plan.
- [ ] Failures, spam placement and missing access remain specific, not passed by a screenshot of the form.
- [ ] Test identities and cleanup stay within authorized scope and public reports contain no private recipient data.

## Example(s)

**Fictional teaching example — no form was submitted.** Maple Cycle offers a photo checklist. Its sample flow requires the user to confirm an email address before receiving the file.

The page says success and the platform shows “pending confirmation.” That is the expected intermediate state. After the controlled test inbox receives the confirmation and the authorized tester confirms it, the subscriber becomes active and the checklist message should arrive.

If the checklist is missing, the task remains partial even though the form and list record worked. The report names the failed delivery step instead of adding repeated test subscribers.

## Handoff and Content Factory context

The form/email owner receives the exact failed step and test reference. [Check the offer preview](https://local-service-spotlight.github.io/task-library/?task=check-lead-magnet-section-has-visual-mockup#task-check-lead-magnet-section-has-visual-mockup) is a companion visual check, not proof of delivery.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at launch and after form, list or delivery-flow changes. A recurring submission test needs a configured cadence, controlled identity and cleanup plan; this guide does not start perpetual live sign-ups.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify email opt-in form exists and works](https://local-service-spotlight.github.io/task-library/?task=verify-email-opt-in-form-exists-and-works#task-verify-email-opt-in-form-exists-and-works)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual platform settings, test authority/receiver, delivered messages and cleanup state require the project.
