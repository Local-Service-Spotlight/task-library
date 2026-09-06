---
name: step-17-final-formatting-and-qa-checks
description: "Check the page people see. Test its links and layout, then pass on the facts and next steps."
category: Content Factory — Post
stage: Post
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 17: Final formatting and QA checks

A page may look right in the editor but break for a reader. This guide helps you check the live page on a phone and a computer. Start with its normal link and compare what you see with the version you meant to publish.

**The path:** Accepted revision → Normal live page → Phone and desktop checks → Measured handoff.

**Use this when:** An authorized article publication/update needs final visitor checks and reconciliation of the agreed distribution.

## Inputs
- The canonical public URL, latest accepted content revision, saved publication receipt and current [Article Guidelines](https://localservicespotlight.com/article-guidelines/).
- The agreed channel list and exact article/video/social/group/send references with their actual states.
- A browser that can open an ordinary visitor view at 1280×800 and 390×844, plus access to inspect links and media silently.
- Authority to repair the scoped page, the maintained delivery/cache route, tracker and owner of later promotion or pending work.

## First-run prompt

> Use the final accepted revision, normal public URL and agreed channel list I provide. Check both exact first-screen sizes, the full body, links and silent media behavior. Make already-authorized repairs and recheck them. Save per-item evidence and truthful pending states; do not treat a WordPress save or cache-busted page as full public proof.

## Steps
1. Open the normal canonical URL as an ordinary visitor, not just a draft preview or special cache-busted link. Compare the title, opening, key edited sections and intended CSS/media to the latest accepted revision. A saved WordPress result and served page are separate checks.
2. At 1280×800 and 390×844, inspect the first screen before clicking or scrolling. Capture the meaningful visual, readable labels, title/opening and absence of sideways overflow. A whole image need not fit every long page, but the useful visual content must be visible and understandable under the maintained rule.
3. Scroll through the rendered body. Check headings, paragraph gaps, tables, image aspect ratios and any preserved builder blocks. Keep the voice and identity rules from [Article Guidelines](https://localservicespotlight.com/article-guidelines/). Fix observed layout failures in the actual supported source.
4. Check every link in the scoped article, including fragments, calls to action and the exact article/video pair. Confirm targets match their labels and identity. Validate forms without creating a real lead when a supported no-side-effect check exists. Submit a real test only when it is in scope, label and clean it up through the maintained route, and verify the receiving record. Otherwise mark the form action UNKNOWN with its named owner; do not pass it from appearance alone.
5. Check the actual video or hosted source player, caption policy, thumbnails and image descriptions. Keep the player muted with volume zero before any playback. If silence cannot be guaranteed, inspect metadata, frames and captions; mark playback unverified rather than starting sound.
6. Confirm byline, category/tags where applicable, stable canonical URL and served search metadata. Recheck relevant Rank Math flags after content changes, while keeping the plugin score separate from the article’s factual and visual pass.
7. Reconcile only the channels named in the distribution plan. Verify the direct Facebook/LinkedIn/YouTube links, group submission state and sent notifications as applicable. A future metric check, unanswered message or pending group moderation stays visible; do not claim all channels are done by assumption.
8. Run [Check the full article checklist](https://local-service-spotlight.github.io/task-library/?task=verify-all-items-on-blog-posting-checklist#task-verify-all-items-on-blog-posting-checklist) against this exact final revision. Repair in-scope failures and recheck affected output. If normal visitors still see stale content, use only the maintained authorized delivery procedure; record a blocker when that procedure fails rather than bypassing its checks.
9. Save the dated evidence, exact view sizes, revision and result for each channel. Hand verified items to the next owner with actual measurements and unresolved dependencies. Do not mark the entire article package complete while a required live check still fails.

## Required first-screen visual gate

Every visitor-facing page, including home, money, relationship, archive and
utility pages, must show a relevant authentic photograph, source-video poster
or useful diagram above the fold. At 390x844 and 1280x800, test the anonymous
unscrolled first visit with JavaScript on and off. A logo, social icon, decorative
background, thin strip, broken image or empty player rectangle fails.

Use the [canonical numeric standard](https://github.com/dennisyu/local-service-spotlight-skills/blob/main/standards/visuals-above-the-fold.md) and its
[shared browser checker](https://github.com/dennisyu/local-service-spotlight-skills/blob/main/scripts/rendered_visual_check.mjs) in the real builder/publisher:
`rendered_visual_check.mjs --url URL --selector CSS --output DIRECTORY`.
Measure the complete preview with site chrome before release and the ordinary
public URL after the authorized release. Save both screenshot/JSON receipts.
The checker can measure a loaded photographic CSS background as well as images,
diagrams and video posters. Its geometry pass remains `REVIEW_REQUIRED` until
an independent reviewer opens the actual screenshots and source evidence and
accepts the relevance, authentic moment, useful crop, labels and permission.
A source-order regex or an `<img>` count cannot mark this gate complete.

YouTube uses youtube-nocookie.com with rel=0, cc_load_policy=1 and cc_lang_pref.
No media autoplays on first paint. Before any separate playback verification,
mute and set volume zero; if that cannot be verified, use metadata, captions,
frames or a loaded poster and record playback NOT_TESTED. Never play through
the user's speakers without their explicit current request.

## Definition of done (QA checklist)

- [ ] The live first 2–3 sentences pass `step-7-write-hook-and-establish-context`: actual reader/situation, reason to care, useful outcome and supporting mechanism; exact text and quoted reviewer evidence retained, and the body delivers its promise
- [ ] Preview and ordinary-live first-screen geometry plus source-backed screenshot review pass on both viewports; actual evidence stored

- [ ] The normal canonical page matches the final accepted revision, including the actual changed layout/media.
- [ ] Both exact first-screen sizes show a meaningful visible visual and no sideways overflow.
- [ ] Body links, calls to action, source player, identity/voice and metadata have evidence; any untested form or silent-playback limit is UNKNOWN with a named owner.
- [ ] The full article checklist is tied to this final revision and has no hidden required failure.
- [ ] Each agreed distribution item has its own true state, and the next owner has the links, evidence and pending work.

## Example(s)

**Fictional teaching example — no live site was tested.** Maple Cycle’s sample QA ledger has four lines:

| Item | Observed sample result |
| --- | --- |
| Canonical article | Current accepted text visible |
| 1280×800 first screen | Photo and opening readable |
| 390×844 first screen | FAIL: a table makes the page scroll sideways |
| Group post | Pending moderator approval |

The editor fixes the table and rechecks the phone view. The page can then pass its visual check, while the required group item remains pending. The final note separates those outcomes instead of saying “everything passed.” No screenshot, post, or measurement in this teaching example is real.

## Handoff and Content Factory context

The named promotion/measurement owner receives only verified live links and actual results. [The Facebook boost shortlist](https://local-service-spotlight.github.io/task-library/?task=boost-top-3-5-facebook-posts#task-boost-top-3-5-facebook-posts) applies only to relevant eligible Page posts under its own scope; other unresolved items stay with their actual owner.

This task serves **Post** in the [Content Factory](https://blitzmetrics.com/content-factory/). Produce supplies the source, Process prepares it, Post places and checks it on the agreed channels, and Promote distributes proven work under its own scope. The task’s actual handoff above defines the next step; list order alone does not create a prerequisite.

## When this runs

Run after publication and after edits that could affect visitor output. Any later channel/metric check must have a real timer or named owner; this guide itself does not remain awake.

## First-run setup and continuity

Use the exact account, source, destination and authority recorded for the job. Carry out publication, messages or repairs already authorized once their required checks pass; do not ask for the same approval again. If an action is outside that scope, finish the authorized work and state the specific remaining need. A login, plugin, or task file does not itself grant new authority.

Keep the latest state, record IDs, revisions and next owner in the project tracker or files. Before a retry, check the current saved/sent/published item to avoid duplicates or overwriting another edit. A model has no guaranteed memory, scheduler or account access just because it is called persistent. A future check needs a configured timer or a named person.

Keep all agent media previews muted with volume zero before playback. If this cannot be verified, use captions, metadata or still frames and state what was not tested. No first-load autoplay is part of these page instructions.

## Write up the real run

For each actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this exact task, source revision, trigger, work, decisions, evidence, result and next owner. Failed, partial and blocked attempts still get a written record. A private draft is a valid writing outcome; public publication follows the existing scope.

Keep one stable execution ID for the actual task run. Retries, checks and changed artifacts do not add runs. A separately scoped child task may have its own ID linked to its parent; writing the parent’s meta record is part of that same run. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains the distinction. Teaching examples below or above are not execution evidence and must not enter the run count.

## Definitive article & links

- Canonical article: https://localservicespotlight.com/article-guidelines/
- Exact Task Library record: [Step 17: Final formatting and QA checks](https://local-service-spotlight.github.io/task-library/?task=step-17-final-formatting-and-qa-checks#task-step-17-final-formatting-and-qa-checks)
- Working writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Task recipe and publishing standard](https://blitzmetrics.com/definitive-article-guide/)
- [Our YouTube caption-default method](https://blitzmetrics.com/youtube-captions-on-by-default/)

## Review and evidence still needed

The original contributor status in the header is preserved. It does not certify this proposed rewrite or prove that this account, publication, message, player or check has run. Every worked teaching example is explicitly invented; replace it with actual evidence when documenting a real execution.
- Real canonical parity, viewport evidence, player/form checks and channel receipts require the actual live job.
