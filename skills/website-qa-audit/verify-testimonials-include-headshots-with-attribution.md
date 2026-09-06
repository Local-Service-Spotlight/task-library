---
name: verify-testimonials-include-headshots-with-attribution
description: "Check the person behind each quote. Use a real approved photo and a full name."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify testimonials include headshots with attribution

A quote should come from a real named person. This guide helps you check the face and name shown with each quote. Start with the person’s source record, not a stock photo or a guess.

**The path:** Every placement → Named source → Approved headshot → Visible or held result.

**Use this when:** A site’s testimonial blocks need the owned headshot-and-name presentation gate checked.

## Inputs
- The full scoped testimonial inventory, including carousel slides and responsive variants.
- Each exact quote’s primary source, speaker identity, approved portrait and applicable use permission.
- Supported page/widget edit access and scope for correcting or removing incomplete blocks.
- A private attribution/asset register and the real owner for missing evidence requests.

## First-run prompt

> Use the supplied testimonial source records and placement list. Verify full names, actual approved portraits, exact quote associations and permission. Fix authorized complete blocks, hold incomplete ones, and return precise missing evidence without guessing identity or sending unrequested outreach.

## Steps
1. List each distinct testimonial and every placement. Inspect static copies and slides; advance only silent text/image carousels where safe. A hidden slide is still a public placement even when the first slide looks complete.
2. Read the displayed full name and compare it with the primary quote/source record. Initials, a first name alone, “happy customer” or a domain/company are incomplete speaker attribution under this standard.
3. Trace the headshot to the approved source and the named speaker’s identity record. Do not assign a similar face, avatar, logo, stock person or generated portrait to make a quote look real.
4. Check the exact words and use permission alongside the photo. A name and portrait do not establish that the person supplied this quote. A public profile image is not automatically permission for every testimonial use.
5. Keep missing name, portrait, source or required permission HOLD and outside the public testimonial block. Write the exact evidence request for the owner. Do not contact the speaker unless outreach is already part of the job.
6. If an asset is questioned, use reliable original records and owner confirmation; an authorized reverse search is only a supporting lead. Multiple appearances online do not prove stock, and a clean search does not certify identity.
7. Apply authorized complete assets/attribution or held-block removal through the supported source. Check desktop and phone portrait crop, name/quote pairing and carousel behavior. Do not pair one person’s photo with another slide’s quote.
8. Record the visible result for every placement and hand the verified name/portrait evidence to the full-attribution check. Passing this visual gate alone does not certify the role/company, source quote or every other trust requirement.

## Definition of done (QA checklist)

- [ ] Every public testimonial placement pairs the correct named speaker with an approved real portrait.
- [ ] Exact quote/source and required permission support the association.
- [ ] Incomplete or uncertain blocks remain HOLD without invented replacements.
- [ ] Desktop/phone and slide pairing are checked on canonical pages after changes.
- [ ] The full-attribution review remains distinct from this portrait/name gate.

## Example(s)

**Fictional teaching example — no person’s photo or quote was used.** A sample slider shows “Alex Rivera” beside a shop logo. The supplied record includes Alex’s exact words and permission for an actual portrait, but the portrait is missing from the folder.

The task remains HOLD for that testimonial until the approved portrait is obtained and paired correctly. Searching for another Alex Rivera and copying a face would not solve the gap. A teaching mockup must never be published as customer praise.

## Handoff and Content Factory context

The content owner receives the portrait/name inventory and held requests. [Verify full testimonial attribution](https://local-service-spotlight.github.io/task-library/?task=verify-testimonials-with-full-attribution#task-verify-testimonials-with-full-attribution) uses those source records for the remaining trust fields.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run before a testimonial is published and when its source, image or placement changes. Recurring review does not automatically authorize contacting every speaker again.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify testimonials include headshots with attribution](https://local-service-spotlight.github.io/task-library/?task=verify-testimonials-include-headshots-with-attribution#task-verify-testimonials-include-headshots-with-attribution)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Real approved portraits, primary quotes, identity/use permission and canonical placement checks require the project.
