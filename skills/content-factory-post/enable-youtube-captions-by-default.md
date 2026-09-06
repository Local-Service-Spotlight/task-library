---
name: enable-youtube-captions-by-default
description: "Ask the YouTube player to show its real captions. Keep the page silent when it first opens."
category: Content Factory — Post
stage: Post
definitive_article: https://blitzmetrics.com/youtube-captions-on-by-default/
status: needs-work
---

# Enable YouTube captions by default

Captions help people follow a video with the sound off. This guide helps you set the player to show the captions it has. Start with the right video and check which caption tracks are really there.

**The path:** Verified video → Caption settings → Saved player → Silent visitor check.

**Use this when:** A page we control has a YouTube embed whose available captions should be requested by default.

## Inputs
- The correct video ID, page language and actual available caption-track evidence.
- The existing iframe (embedded player) or click-to-play facade, which is the poster/control that loads it. Include any VideoObject schema: the page’s machine-readable description of the video and its embed URL.
- The site’s supported source and edit authority. Check whether the maintained caption filter/helper already handles this embed.
- The page URL, accepted source revision and a way to perform silent desktop/mobile checks.

## First-run prompt

> Inspect the exact embed source and real video I provide. Use the existing supported filter/helper where it applies, set the documented caption and silent-first-load policy, and complete the authorized save. Check normal visitor output and real caption availability. Never invent an ID, track, quote, or playback result.

## Steps
1. Read the maintained [YouTube captions guide](https://blitzmetrics.com/youtube-captions-on-by-default/). Identify whether the current site uses its WordPress filter, a shared app helper, or a one-off iframe. Verify that mechanism exists and applies before relying on it; do not deploy a new fleet plugin for one page without that setup being in scope.
2. Confirm the video ID and page language from the real source. Inspect caption availability. A preferred language parameter does not create a caption track or prove that an automatic transcript is accurate.
3. Use the privacy-enhanced embed host `https://www.youtube-nocookie.com/embed/VIDEO_ID`. Request `cc_load_policy=1` and `cc_lang_pref=en` or the actual page’s two-letter language code. Preserve other needed documented settings.
4. Keep `rel=0`, which limits related videos to the same channel rather than disabling them. Set `autoplay=0` or omit autoplay for the initial player. A future viewer click can load a player, but agent checks still must keep it muted at volume zero.
5. For an app facade, make its loaded player and VideoObject embed URL describe the same video and caption policy. They need not have byte-identical URLs when a documented click-only behavior differs. For a one-off iframe, put the intended parameters on its real src, not only a comment or data label.
6. Save through the supported source and complete an already-authorized publish/build. Read the saved output and the normal public URL. For a facade, inspect the player-building source as well as schema; schema alone does not prove the clicked player used the settings.
7. Check desktop and phone first load: no autoplay, right poster/player, readable controls and no overflow. Before any playback, verify mute and zero volume; otherwise inspect metadata/captions/stills and report the untested behavior.
8. Where silent playback is possible, check whether the intended real caption track appears. Record “parameters present; captions unavailable” if that is the truth. Keep player captions separate from the complete source transcript needed for quoting, then pass results to [Final formatting and QA checks](https://local-service-spotlight.github.io/task-library/?task=step-17-final-formatting-and-qa-checks#task-step-17-final-formatting-and-qa-checks).

## Definition of done (QA checklist)

- [ ] Correct video ID and page language are verified.
- [ ] The real player requests cc_load_policy=1 and the intended cc_lang_pref; privacy-enhanced host and rel=0 are present.
- [ ] First load does not autoplay, and all agent playback checks stay muted at zero volume.
- [ ] Saved source, built output and normal public result agree where applicable.
- [ ] Actual caption availability/behavior is recorded honestly; no track, quote evidence or playback pass is invented.

## Example(s)

**Teaching template — not a real video or tested player.** Replace `VIDEO_ID` with the verified source ID before use:

```text
https://www.youtube-nocookie.com/embed/VIDEO_ID?autoplay=0&rel=0&cc_load_policy=1&cc_lang_pref=en
```

**Fictional teaching example:** a sample English page has a real video ID in its actual source, but that video has no caption track. The editor adds the intended parameters and verifies silent first load. The result is “settings saved; no captions available,” not “captions working.”

If the video later gets a checked track, test it again. Do not create an empty VTT file or treat player-generated words as a verified quotation. The template above must never be published with the literal `VIDEO_ID` placeholder.

## Handoff and Content Factory context

The publisher gets the source revision, actual player URL, caption state and silent QA evidence. [Final formatting and QA checks](https://local-service-spotlight.github.io/task-library/?task=step-17-final-formatting-and-qa-checks#task-step-17-final-formatting-and-qa-checks) verifies the whole page; the article writer still uses the full approved transcript for quotes.

This task serves **Post** in the [Content Factory](https://blitzmetrics.com/content-factory/). Produce supplies the source, Process prepares it, Post places and checks it on the agreed channels, and Promote distributes proven work under its own scope. The task’s actual handoff above defines the next step; list order alone does not create a prerequisite.

## When this runs

Run when adding or changing an embed, its video, page language or player helper. No recurring clock is required by this skill.

## First-run setup and continuity

Use the exact account, source, destination and authority recorded for the job. Carry out publication, messages or repairs already authorized once their required checks pass; do not ask for the same approval again. If an action is outside that scope, finish the authorized work and state the specific remaining need. A login, plugin, or task file does not itself grant new authority.

Keep the latest state, record IDs, revisions and next owner in the project tracker or files. Before a retry, check the current saved/sent/published item to avoid duplicates or overwriting another edit. A model has no guaranteed memory, scheduler or account access just because it is called persistent. A future check needs a configured timer or a named person.

Keep all agent media previews muted with volume zero before playback. If this cannot be verified, use captions, metadata or still frames and state what was not tested. No first-load autoplay is part of these page instructions.

## Write up the real run

For each actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this exact task, source revision, trigger, work, decisions, evidence, result and next owner. Failed, partial and blocked attempts still get a written record. A private draft is a valid writing outcome; public publication follows the existing scope.

Keep one stable execution ID for the actual task run. Retries, checks and changed artifacts do not add runs. A separately scoped child task may have its own ID linked to its parent; writing the parent’s meta record is part of that same run. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains the distinction. Teaching examples below or above are not execution evidence and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/youtube-captions-on-by-default/
- Exact Task Library record: [Enable YouTube captions by default](https://local-service-spotlight.github.io/task-library/?task=enable-youtube-captions-by-default#task-enable-youtube-captions-by-default)
- Working writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [YouTube’s documented player parameters](https://developers.google.com/youtube/player_parameters)

## Review and evidence still needed

The original contributor status in the header is preserved. It does not certify this proposed rewrite or prove that this account, publication, message, player or check has run. Every worked teaching example is explicitly invented; replace it with actual evidence when documenting a real execution.
- Real caption-track availability and muted player behavior still need the target video and page.
