---
name: verify-featured-images-unique-per-blog-post
description: "Give each post its own clear image. Find blank cards and covers that all look the same."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify featured images unique per blog post

A row of the same picture makes posts hard to tell apart. This guide helps you give each post a useful cover. Start with the full post list and the images readers really see.

**The path:** Post list → Asset and archive map → Relevant cover → Canonical check.

**Use this when:** A blog/archive or new post batch needs its featured images checked under the owned editorial standard.

## Inputs
- The exact published post inventory and archive/card templates in scope.
- Featured-media settings or equivalent supported cover source, actual image files and their provenance.
- Approved real photos, source screenshots or meaningful accurate diagrams tied to each post.
- Supported edit access and a post-to-asset report with actual public placement evidence.

## First-run prompt

> Map the supplied posts to their actual cover sources and visible cards. Identify missing or repeated visuals, choose truthful relevant assets within scope, and verify canonical desktop/phone layouts. Return the post-to-asset table and any real source requests or reviewed exceptions.

## Steps
1. Join the published post list with its stored featured-media ID/URL and live archive card. Record where the theme intentionally uses another supported cover source; a missing WP featured-media field alone does not prove the public card is blank.
2. Inspect the archive grid and individual post pages on desktop and phone. Identify missing covers, unrelated fallbacks and visual repeats that obscure the topics.
3. Compare distinct files and visual content, not only file names. Different IDs or crops can still reuse the same underlying picture. The same source frame with a new filename is not a genuinely distinct proof asset.
4. Apply the house standard of a useful article-specific cover. Prefer real relevant photos or approved accurate visuals. A process diagram can be appropriate; the no-stock proof rule does not require an invented photo when the article explains a method.
5. For each missing or repeated cover, choose an actual relevant asset or write an exact source request. Do not distort a real scene, label it as another job or claim search results must show the chosen cover.
6. Set the authorized cover through the correct source, preserving existing body media and canonical URL. Check crop, focal subject, aspect ratio and accessible text in the actual template.
7. Verify the normal archive and post after saving, plus the served social-image setting if it is in scope. Archive cover, body lead image and social preview can be different fields; record their actual relationship instead of assuming one edit changes all three.
8. Save each post’s final asset, source/rights, visual-distinctness result and remaining exceptions. A permitted special-case reuse needs an explicit editorial reason; do not silently pass a wall of defaults.

## Definition of done (QA checklist)

- [ ] The full scoped post inventory is mapped to stored and visibly served covers.
- [ ] Article covers are relevant and visually distinct under the house standard or have an explicit reviewed exception.
- [ ] Assets retain truthful provenance and appropriate rights.
- [ ] Desktop/phone crops and canonical archive/post rendering are checked after edits.
- [ ] Social/search preview outcomes are not inferred from a featured-media ID.

## Example(s)

**Fictional teaching example — no cover image was assigned.** Maple Cycle has three posts about quote photos, worn brake pads and preparing for a visit. Each currently uses the same shop-logo card.

The teaching plan uses an approved quote-photo example, a real brake close-up and a useful preparation checklist diagram. Copying the logo into three new filenames would not make the covers meaningfully distinct. The reviewer checks each actual archive crop after assignment rather than only inspecting the media-library IDs.

## Handoff and Content Factory context

The editor receives the cover map. [Prepare article photos and featured media](https://local-service-spotlight.github.io/task-library/?task=step-8-add-photos-and-featured-image#task-step-8-add-photos-and-featured-image) supplies missing article assets; [Check home-page article cards](https://local-service-spotlight.github.io/task-library/?task=add-homepage-blog-card-thumbnails#task-add-homepage-blog-card-thumbnails) covers a separate home-page module.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run for a new post batch and after archive or cover-source changes. No media generation, upload or continuing scheduler is automatically installed.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify featured images unique per blog post](https://local-service-spotlight.github.io/task-library/?task=verify-featured-images-unique-per-blog-post#task-verify-featured-images-unique-per-blog-post)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The actual post inventory, cover-source mapping and approved replacement assets require the site.
