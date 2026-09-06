---
name: add-click-to-call-links-for-mobile
description: "Make the phone number on your site easy to tap. Check that it opens the right number."
category: Digital Plumbing
stage: —
definitive_article: /digital-plumbing
status: needs-work
---

# Add Click-to-Call Links for Mobile

Do people have to copy your phone number to call you? This guide helps a site owner make that number a link. Start with the number your team answers, then check each place it shows.

**The path:** Right number → Tap link → Dialer → Call record.

**Use this when:** a site launches, the business number changes, or phone visitors cannot easily start a call.

## Inputs
- The approved business number, country code and intended team or branch. Identify any tracking-number service already in use.
- The live page list and access to the template, menu or content block that owns each number. Save its prior value.
- A phone or device emulator for link checks; an agreed receiving person and test window if a real call is in the existing scope.

## First-run prompt

> Find each phone number on the supplied pages. Make the intended numbers usable as call links within the approved edit scope. Check visible text, link targets and mobile access. Keep tap evidence separate from completed calls and hand over exact gaps.

## Steps
1. List the phone locations: header, contact page, footer, service pages and sticky controls. Match each to the correct branch or team; do not replace distinct valid branch numbers with one global number.
2. Choose the editable source for each location. A shared header should be changed once at its owning template, not patched separately in generated pages. Save the before state for rollback.
3. Wrap each intended number in a telephone link using its real country code, such as the fictional link in the example. Keep readable number text. Do not force every country to use +1 or turn an extension into a different phone number.
4. Check the control at phone width. Keep its label clear, enough space to tap and visible keyboard focus. Place the main call action where the page purpose calls for it, without covering page text or privacy controls.
5. If dynamic number insertion is installed, check both the displayed number and its telephone target after the swap. Preserve the approved attribution setup and the stable business identity record.
6. Save through the supported page or template route. Open the ordinary public URL and confirm that all changed locations contain the expected link, with no stale alternate mobile header.
7. Tap without placing a call first: verify the dialer shows the correct number, then cancel. If end-to-end calling is authorized, place a clearly identified test during the agreed window and record who received it. A dialer check alone leaves call delivery unverified.
8. If measurement is in scope, use the existing tag or analytics setup to record a phone-link click once. Inspect its received event. Use a call-tracking receipt for connected calls; never label every click as a qualified lead.

## Definition of done (QA checklist)

- [ ] Every intended location has a usable telephone link to the correct number.
- [ ] Mobile display, keyboard focus and tap access work without covering content.
- [ ] Any number swap changes the text and link together.
- [ ] Dialer, connected-call and received-event evidence have distinct results and timestamps.
- [ ] Before/after source and the next owner are saved; unresolved call routing stays explicit.

## Example(s)

**Fictional teaching example.** Oak Repair uses the reserved teaching number +1 202-555-0148. Its footer says “202-555-0148” but links to an old number. The replacement is `<a href="tel:+12025550148">Call 202-555-0148</a>`. The lesson check finds the right target in the header, footer and contact page: 3 of 3. Opening the dialer proves those links, but no call has been placed. The result therefore says “links pass; call delivery not tested,” rather than “three leads.” Never dial this teaching number.

## Handoff and Content Factory context

Give the site owner the checked locations. If call attribution is needed next, use [set up call tracking for phone conversions](https://local-service-spotlight.github.io/task-library/?task=set-up-call-tracking-for-phone-conversions#task-set-up-call-tracking-for-phone-conversions). If the dialer works but the call fails, route the receiving-line issue to the actual phone-service owner.

This setup supports the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run once for the setup and after a number, header, theme or tracking-service change. Include it in an existing site check if one is configured; this file creates no recurring job.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/digital-plumbing
- Exact task: [Add Click-to-Call Links for Mobile](https://local-service-spotlight.github.io/task-library/?task=add-click-to-call-links-for-mobile#task-add-click-to-call-links-for-mobile)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Digital Plumbing training](https://blitzmetrics.com/digital-plumbing/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- A real deployment needs the supplied number, owning template and any requested call-delivery evidence.
