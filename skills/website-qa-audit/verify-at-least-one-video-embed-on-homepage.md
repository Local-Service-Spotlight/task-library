---
name: verify-at-least-one-video-embed-on-homepage
description: "Check the real video on the home page. Make sure people can view it there and read its captions."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify at least one video embed on homepage

A real video can help people meet the person behind the site. This guide helps you check that the player works on the page. Start with the right source video and keep all agent tests silent.

**The path:** Real source → Actual player → Silent two-width check → Evidence.

**Use this when:** A personal-brand home page is being checked for the owned real-video requirement. For another page role, use the agreed relevant source rather than assuming every site is one person’s brand.

## Inputs
- The canonical home page, actual source video and evidence that it features the intended owner or relevant approved representative.
- The current embed/host settings and permission to embed the source, including a third-party host when that is legitimate.
- Desktop and phone views plus a way to verify player mute and volume zero before playback.
- Available caption track, supported page edit access and a place for player/layout evidence.

## First-run prompt

> Use the supplied home page and source video. Inspect autoplay first, verify an actual relevant embed at both viewports, and test playback only after mute and volume zero are proven. Apply authorized fixes and report source, captions, visible layout and actual playback evidence separately.

## Steps
1. Inspect the page source for autoplay before opening a player. Ensure agent previews cannot emit sound; if mute and volume zero cannot be controlled before playback, use captions, frames and metadata and leave playback untested.
2. Locate the actual embedded player in the page body. A static thumbnail or link to another site is useful navigation but does not meet the in-page player requirement.
3. Confirm the source video and its factual role from the approved inventory. Do not require that every valid source be uploaded to the owner’s own channel; an authorized third-party interview can be the correct source if embedding is permitted.
4. Check that at least one relevant player is present and usable at 1440×860 and 390×844. Preserve the intended aspect ratio and a useful first-screen visual; the player need not displace an existing good lead photo.
5. For YouTube, apply [captions by default](https://local-service-spotlight.github.io/task-library/?task=enable-youtube-captions-by-default#task-enable-youtube-captions-by-default) through the supported embed. Use the page’s caption language and disable first-load autoplay. Caption preferences do not create missing captions; rel=0 restricts related videos to the same channel rather than removing them all.
6. When verified muted playback is possible and in scope, start the player briefly on each viewport, confirm time advances and no blocking error appears, then stop it. Record player error codes or source restrictions rather than attributing every unrelated console warning to the embed.
7. Check actual captions for availability and useful visible text without claiming a full transcript/audio review from a short silent test. Repair authorized source/embed/caption settings; missing source-owner permission or captions gets a concrete handoff.
8. Recheck the normal canonical page after changes and save source ID, location, viewport, mute state, caption result and playback scope. A poster loaded or a player script present alone is not verified playback.

## Definition of done (QA checklist)

- [ ] At least one actual in-page player uses the intended legitimate source for this page role.
- [ ] Desktop and phone layout fit and first-load autoplay is disabled.
- [ ] Any playback was muted at volume zero before start; unavailable control leaves playback untested.
- [ ] Captions are actually available or a precise caption gap remains.
- [ ] Loaded, playable, source-verified and fully reviewed are distinct evidence states.

## Example(s)

**Fictional teaching example — no video was played.** Maple Cycle’s page has a picture with a play triangle that opens YouTube in another tab. It also has an interview player farther down the page, but the phone layout hides it.

The picture does not count as an embed. The teaching fix restores the real interview player in the phone layout and checks its legitimate source, captions and silent playback controls. If the tester cannot verify mute before start, the report says “player visible; playback untested,” not “video works.”

## Handoff and Content Factory context

The page owner receives the player evidence. [Embed the source video](https://local-service-spotlight.github.io/task-library/?task=step-10-embed-source-video#task-step-10-embed-source-video) handles a missing/incorrect player, while the source owner supplies any required caption or embedding permission.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at launch and when the source, visibility, player or layout changes. A recurring check needs an actual configured owner and cadence; no silent failure monitor is created by this file.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify at least one video embed on homepage](https://local-service-spotlight.github.io/task-library/?task=verify-at-least-one-video-embed-on-homepage#task-verify-at-least-one-video-embed-on-homepage)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [YouTube player parameters](https://developers.google.com/youtube/player_parameters)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual player controls, source rights, caption availability and rendered playback evidence require the page.
