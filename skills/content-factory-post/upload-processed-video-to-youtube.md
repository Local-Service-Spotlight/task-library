---
name: upload-processed-video-to-youtube
description: "Put the finished video on the right YouTube channel. Set its real details and check the chosen viewing state."
category: Content Factory — Post
stage: Post
definitive_article: GAP — to be written
status: needs-work
---

# Upload processed video to YouTube

Your finished video needs a place where people can watch it. This guide helps you upload it to the right channel and link it to the article. Start with the final file and the viewing plan for this job.

**The path:** Final source → Channel and details → Viewing state → Checked article pair.

**Use this when:** A source-checked edited video is ready for the brand’s YouTube channel under an agreed draft/private/unlisted/public/scheduled plan.

## Inputs
- The final video, rights, facts, source transcript and caption review state. Keep the source file/version identifiable.
- The exact channel and upload access through its approved account or role. Use [the channel setup task](https://local-service-spotlight.github.io/task-library/?task=set-up-youtube-channel-with-proper-branding#task-set-up-youtube-channel-with-proper-branding) only if this prerequisite is actually missing.
- The planned title, description, real thumbnail, relevant playlist and checked article URL if already public.
- The requested viewing state and any scheduled date/time/timezone, plus the article editor and content tracker.

## First-run prompt

> Use the final source file, exact channel and visibility plan I provide. Check for an existing upload, set accurate details, complete the already-authorized save/publication, and record the real ID and state. Keep preview checks silent and distinguish upload, processing, captions and article cross-links.

## Steps
1. Confirm the channel identity in YouTube Studio and check its content list for this source/version. A retry should resume or repair the known upload rather than create another copy.
2. Choose Create → Upload videos and select the final file. Wait for the actual upload and processing state. Name the source revision in the private tracker, not in the public description.
3. Enter a clear title and accurate description. The current limits are 100 characters for a title and 5,000 for a description. Include the specific article when it is live; do not send viewers to a private draft or say an article exists when it does not.
4. Choose the real thumbnail and a fitting playlist where the channel supports them. Set audience, branded-content, altered/synthetic-content and other required disclosures from the actual content. If the article will embed this video, confirm the upload’s license/distribution setting allows embedding. Do not guess these settings from the client’s business category.
5. Review language and captions. Use a verified caption file or correct available captions as the job permits. Tags may help disambiguation, but do not replace a clear title and description or prove the video will rank.
6. Read the platform checks and any restrictions. Choose the viewing state already authorized for the job and save/publish it. If the task authorizes Public and checks pass, complete it without a new approval request. Unlisted is not private; a scheduled item is not live yet. Give a named receiver the scheduled time and timezone so the first firing is checked after the due time.
7. Check the resulting video page, channel and visibility with media muted and volume zero. Confirm intended processing quality and caption availability before claiming a complete viewing check. If it is scheduled, keep the result scheduled until the receiver verifies the public page after the first firing. If silence cannot be verified, use metadata/captions/stills and state the playback gap.
8. Give the video ID/URL to [Embed the source video](https://local-service-spotlight.github.io/task-library/?task=step-10-embed-source-video#task-step-10-embed-source-video) and [Set caption defaults](https://local-service-spotlight.github.io/task-library/?task=enable-youtube-captions-by-default#task-enable-youtube-captions-by-default). When the article is live, verify its embed and the video description link both point to the correct pair.
9. Record upload ID, source version, channel, state, time, first-firing owner when scheduled, caption/check results and the article-pair status. If either side is not yet public, keep that cross-link step pending rather than invent a closed loop.

## Definition of done (QA checklist)

- [ ] The upload is the intended source/version on the correct channel, without an accidental duplicate.
- [ ] Title, description, thumbnail, disclosures and embedding permission match the actual source, allowed use and article plan.
- [ ] Saved visibility and time match the job; private, unlisted, scheduled and public states are distinct, and a schedule has a named first-firing receiver.
- [ ] Caption and silent viewing checks have actual evidence or a specific unresolved limitation.
- [ ] Article/video links are checked when both exist, and missing parts have a named owner.

## Example(s)

**Fictional teaching example — no video was uploaded.** Maple Cycle’s final sample file is `quote-guide-v3.mp4`. The intended title is “What to send before a bike repair quote.” The job asks for an unlisted review copy today, not a public launch.

The sample tracker therefore records “unlisted review copy; article draft pending.” Its description does not contain a made-up live article URL. Once the real article and public release are authorized, the publisher updates the description and the article embed, then checks the pair.

“Upload finished” alone would not prove correct visibility, available captions, or a linked article. No invented video ID is supplied in this teaching example.

## Handoff and Content Factory context

The article editor receives the verified video URL/ID and caption state. Distribution tasks use it only in the agreed viewing state; [Final formatting and QA checks](https://local-service-spotlight.github.io/task-library/?task=step-17-final-formatting-and-qa-checks#task-step-17-final-formatting-and-qa-checks) checks the final article/video pair.

This task serves **Post** in the [Content Factory](https://blitzmetrics.com/content-factory/). Produce supplies the source, Process prepares it, Post places and checks it on the agreed channels, and Promote distributes proven work under its own scope. The task’s actual handoff above defines the next step; list order alone does not create a prerequisite.

## When this runs

Run for a finished video or its defined correction. A future release uses an actual configured date/time, timezone and named receiver who checks the first firing; this task does not establish recurring uploads.

## First-run setup and continuity

Use the exact account, source, destination and authority recorded for the job. Carry out publication, messages or repairs already authorized once their required checks pass; do not ask for the same approval again. If an action is outside that scope, finish the authorized work and state the specific remaining need. A login, plugin, or task file does not itself grant new authority.

Keep the latest state, record IDs, revisions and next owner in the project tracker or files. Before a retry, check the current saved/sent/published item to avoid duplicates or overwriting another edit. A model has no guaranteed memory, scheduler or account access just because it is called persistent. A future check needs a configured timer or a named person.

Keep all agent media previews muted with volume zero before playback. If this cannot be verified, use captions, metadata or still frames and state what was not tested. No first-load autoplay is part of these page instructions.

## Write up the real run

For each actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this exact task, source revision, trigger, work, decisions, evidence, result and next owner. Failed, partial and blocked attempts still get a written record. A private draft is a valid writing outcome; public publication follows the existing scope.

Keep one stable execution ID for the actual task run. Retries, checks and changed artifacts do not add runs. A separately scoped child task may have its own ID linked to its parent; writing the parent’s meta record is part of that same run. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains the distinction. Teaching examples below or above are not execution evidence and must not enter the run count.

## Definitive article & links

- Dedicated canonical article: not mapped in this source record. The owned training references below remain the method until that gap is reviewed.
- Exact Task Library record: [Upload processed video to YouTube](https://local-service-spotlight.github.io/task-library/?task=upload-processed-video-to-youtube#task-upload-processed-video-to-youtube)
- Working writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [YouTube’s current upload controls](https://support.google.com/youtube/answer/57407?hl=en)
- [Our YouTube caption-default method](https://blitzmetrics.com/youtube-captions-on-by-default/)

## Review and evidence still needed

The original contributor status in the header is preserved. It does not certify this proposed rewrite or prove that this account, publication, message, player or check has run. Every worked teaching example is explicitly invented; replace it with actual evidence when documenting a real execution.
- Actual channel capability, processing/caption state and live visibility need the real upload; no dedicated canonical upload article is mapped.
