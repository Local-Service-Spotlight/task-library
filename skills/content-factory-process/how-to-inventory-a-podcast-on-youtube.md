---
name: how-to-inventory-a-podcast-on-youtube
description: "List the talks and interviews on a YouTube channel. Find the useful sources your team can use next."
category: Content Factory — Process
stage: Process
definitive_article: https://blitzmetrics.com/how-to-inventory-a-podcast-on-youtube/
status: complete
---

# How to inventory a podcast on YouTube

Good interviews can get lost in a busy channel. This guide helps you list them, check who is in each one, and choose what to use next. Start with the exact channel and a shared sheet.

**The path:** Channel and playlists → Unique episodes → Verified people → Ranked source queue.

**Use this when:** A channel’s podcast-format videos need an evidence-backed inventory for reuse.

## Inputs
- The exact channel ID/URL, host names/variants, series names and existing inventory.
- A client-owned sheet with Playlists, All Episodes, Cross-Platform, Guests and Summary tabs; use the linked guide’s template when available.
- Read access to YouTube and primary episode/show pages, and authorized API quota if using the Data API.
- The intended scope/date range, access limits, metric observation time and next content owner.

## First-run prompt

> Inventory this exact YouTube channel into the five-tab format. Reconcile playlists, videos, live items and searches by video ID; verify guests and public dates. Keep inaccessible rows and metric gaps visible. Calculate transparent summaries and a source-backed priority list without claiming every appearance worldwide was found.

## Steps
1. Create or update one dedicated inventory. Record channel ID, scope, date and search coverage. Keep source rows and summary formulas separate.
2. Map playlists with title, URL, observed count and type. Treat long duration, guest names and “podcast” as discovery clues; inspect the content before classifying it as an interview.
3. Capture each accessible episode with unique video ID, title, series, duration, public date, observed views, guest/host role and source URL. Follow all playlist pages/API nextPageToken values. Keep playlist memberships separately so one video in two playlists remains one episode.
4. Search beyond playlists through Videos, Live and relevant channel queries. The source suggests at least ten targeted searches when useful; record terms and outcomes rather than calling ten queries proof of completeness. Include known names and series variants.
5. Verify each guest from a primary title/description/show page or checked introduction. Use “Solo — host” only when supported. Keep unknown people and inaccessible/private/deleted slots as explicit exceptions rather than invented rows.
6. Build one Guests row per verified person with relevant identity links and episode list. A missing LinkedIn URL is a documented exception, not permission to guess a profile.
7. Cross-check Listen Notes, Podchaser, the host’s site and global YouTube results. Store outside-channel appearances in Cross-Platform and preserve source links. Discovery results and AI suggestions remain leads until verified.
8. For comparable videos with known dates and views, calculate lifetime average views per day using the stated observation time and age rule. It is not recent velocity. Keep same-day/unknown-date rows unranked or explicitly use a disclosed one-day denominator; do not silently divide by zero.
9. Build Summary totals from unique accessible verified rows, plus separate unresolved/unavailable counts. Rank within comparable groups. If using top 20%, state the eligible denominator and rounding rule; retrieve permitted transcripts for selected rows, retain timestamped originals and record actual word counts.
10. Reconcile playlist memberships, unique episodes, exceptions, guest identity and summary formulas. Log a quoted-title search as a dated query/result observation, not guaranteed Google indexing. Hand over priority sources, coverage limits and measured time/cost only when recorded.

## Definition of done (QA checklist)

- [ ] All five tabs exist with exact channel/scope and a reproducible coverage log.
- [ ] Unique video IDs are deduplicated while playlist membership and unavailable slots remain visible.
- [ ] People, dates, metrics and transcripts are verified or labeled unknown with reasons.
- [ ] Summary totals, priority denominator and formula choices reconcile to source rows.

## Example(s)

**Fictional teaching example — no channel was audited.** Playlist A lists five videos; Playlist B lists four, with two IDs shared. The inventory has seven unique listed videos, not nine. One is unavailable, leaving six accessible rows and one exception.

For a sample video with 600 observed views over 30 days, lifetime average is 20 views/day. That does not prove it got 20 views yesterday. If five rows have comparable valid metrics, the top 20% selection is one row. The summary shows the date and denominator rather than calling that row a sales winner.

## Handoff and Content Factory context

The owner receives the sheet and coverage gaps. [Merge all podcast appearances](https://local-service-spotlight.github.io/task-library/?task=how-to-inventory-every-podcast-youve-been-on-and-why-its-one-of-the-highest-roi-things-you-can-do#task-how-to-inventory-every-podcast-youve-been-on-and-why-its-one-of-the-highest-roi-things-you-can-do) reconciles cross-platform sources; [Transcribe selected sources](https://local-service-spotlight.github.io/task-library/?task=step-2-transcribe-video-using-descript#task-step-2-transcribe-video-using-descript) starts only with permitted media.

Produce supplies the real source. **Process**, this stage of the [Content Factory](https://blitzmetrics.com/content-factory/), turns it into useful finished assets. Post saves or publishes them on the agreed channels. Promote tests and distributes suitable work within its own scope. The handoff above names this task’s actual next step; catalog neighbors alone are not prerequisites.

## When this runs

Initial inventory, then a dated delta when new channel content appears or the project requests a refresh. Reuse the same sheet and IDs.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/how-to-inventory-a-podcast-on-youtube/
- Exact task: [How to inventory a podcast on YouTube](https://local-service-spotlight.github.io/task-library/?task=how-to-inventory-a-podcast-on-youtube#task-how-to-inventory-a-podcast-on-youtube)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [YouTube video metadata fields](https://developers.google.com/youtube/v3/docs/videos)
- [YouTube playlist pagination](https://developers.google.com/youtube/v3/docs/playlistItems/list)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Private/deleted content, source rights, exact metrics and any missing identities require real channel evidence.
