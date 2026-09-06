---
name: verify-hero-section-contains-real-photo-of-person
description: "Let people see who is behind a personal site. Check that the real photo stays clear on a phone."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify hero section contains real photo of person

People should see the person behind a personal site right away. This guide helps you check the main photo at the top. Start with a real approved photo and its source record.

**The path:** Approved source → Real person in context → First-screen crop → Canonical evidence.

**Use this when:** A personal-brand home-page hero needs its real-owner-photo requirement checked. Other site roles use their own relevant visual plan.

## Inputs
- The canonical personal-site home page and its current hero source/layout.
- The approved original photo and a source record or owner confirmation of who it depicts and permitted use.
- Desktop/phone views at 1440×860 and 390×844, with supported page/media edit scope.
- An asset/viewport report and the actual owner who can resolve missing source evidence.

## First-run prompt

> Review the supplied personal-site hero and approved photo record. Verify source identity, honest context and first-screen desktop/phone crops, perform authorized layout repairs, and return exact visual evidence or a specific missing-asset request without guessing who a face belongs to.

## Steps
1. Confirm the site role and intended person. The personal-brand hero should use that real person’s approved photograph; do not automatically apply the same single-founder rule to a company or another declared page role.
2. Trace the selected photo to its source record and approved identity/use information. Do not guess identity from a face comparison or treat a similar-looking stock model as the owner.
3. Inspect the initial canonical desktop viewport. Confirm useful photo content is visible with the opening, not only a blank frame, background sliver, logo or illustration substituted for the required real-owner photo.
4. Repeat on the phone viewport. Check that the crop retains the person, the face is not covered by text/banner controls, and the photo is large and clear enough to register. Preserve aspect ratio and choose a suitable crop rather than stretching the image.
5. Check the implied scene and caption against the source. A photo can show the person at a place without proving a client, partner or endorsement relationship. Keep stronger unsupported claims HOLD rather than using a photo as a shortcut to credibility.
6. Use reverse-image search only as an authorized clue on public assets if needed. A reused photo is not automatically stock, and no search match does not prove authenticity. Private originals stay out of third-party uploads unless that use is already authorized.
7. Apply authorized asset/crop/layout fixes through the supported source and preserve useful existing media. If no approved real-owner photo exists, give the owner an exact asset request; do not invent a photo shoot or pass an AI avatar as proof.
8. Reopen the normal home page at both widths and save the actual asset, source evidence, visible bounds/crop and remaining gaps. A changed image setting is not enough if a public cache still shows the old hero.

## Definition of done (QA checklist)

- [ ] The task applies to the declared personal-brand role and intended owner.
- [ ] The real photograph has source-backed identity and use rights, not a visual guess.
- [ ] Meaningful owner-photo content is clear in both first viewports with a valid crop.
- [ ] Photo context does not create an unsupported relationship or achievement claim.
- [ ] Authorized changes are publicly checked or the exact asset/delivery gap remains.

## Example(s)

**Fictional teaching example — no hero image was inspected.** Alex supplies an approved original workshop photo for a personal site. The desktop hero shows Alex clearly, but the phone crop displays only the workbench.

The teaching fix changes the supported focal crop so Alex remains visible at 390×844, then checks the canonical page. The source photo can support “At my workshop” if the source record says that; it does not establish a partnership with a brand whose logo happens to be in the scene.

## Handoff and Content Factory context

The page owner receives source and viewport evidence. [Check major home-page visuals](https://local-service-spotlight.github.io/task-library/?task=check-each-homepage-section-includes-relevant-image#task-check-each-homepage-section-includes-relevant-image) reviews the sections below; the hero result alone does not pass them.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at launch and after hero, crop or template changes. Other landing-page heroes are included only in the actual scope, not silently added as a lifetime monitor.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify hero section contains real photo of person](https://local-service-spotlight.github.io/task-library/?task=verify-hero-section-contains-real-photo-of-person#task-verify-hero-section-contains-real-photo-of-person)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual approved photo/source identity, use rights and canonical viewport evidence require the project.
