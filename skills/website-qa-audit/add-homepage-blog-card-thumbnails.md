---
name: add-homepage-blog-card-thumbnails
description: "Show a real photo on each home page article card. Keep the words and links easy to use."
category: Website QA Audit
stage: Post
definitive_article: https://blitzmetrics.com/blog-card-thumbnails-standard/
status: needs-work
---

# Add homepage blog-card thumbnails

A real photo helps readers choose which post to open. This guide helps you add one to the card and keep its words and link. Start with the source image and the site’s own editor.

**The path:** Real article asset → Correct card layout → Supported save → Public two-width check.

**Use this when:** An existing home-page article card lacks the meaningful real thumbnail required by its personal-brand card standard.

## Inputs
- The exact canonical home page, affected cards and each card’s existing text/destination.
- Approved post featured images, legitimate source-video frames or real subject photos, with source/use evidence.
- The actual card markup/computed layout and supported WordPress/theme/builder save route with edit scope.
- A prior source/revision snapshot and canonical visitor QA access at desktop/phone widths.

## First-run prompt

> Use the supplied cards, real article assets and supported editor. Prepare source-preserving thumbnail layouts, complete authorized saves/publication and check normal canonical desktop/phone pages. Return exact source/public evidence and pending delivery layers without inventing assets or changing card destinations.

## Steps
1. Inventory only the affected existing article-card module. If the home page has no such module, record not applicable or the separately requested module-build scope. Do not create a new blog section just to complete a thumbnail check.
2. Read each linked article and choose its real relevant asset: the actual featured image first, then a permitted source-video frame or real subject photo. Do not assume Rank Math universally generates thumbnails. A card about a real story needs its actual human/work source, not a stock or generated stand-in.
3. Validate the actual image content, format, dimensions and source. A small/large response body alone cannot prove that a thumbnail is valid rather than a placeholder. If a needed source frame cannot be obtained through the supported authorized media route, request the precise asset; do not move untrusted remote media through model context.
4. Inspect the card’s real layout. For a clipped card, an edge-aligned image may fit with existing padding. For an open/overflow-visible card, a full-width image above a padded body wrapper can preserve the original text. Choose from measured behavior rather than blindly pasting fixed margins.
5. Prepare a source-preserving change that keeps each title, date, excerpt, link and useful style. Compare text, destination URLs and relevant markup/style counts before saving. Fragment parsing can move or lose style elements; verify the actual serialized result rather than trusting a parsing method by name.
6. Save through the site’s currently supported editor/builder pipeline. The source article records an Elementor 3.x case where raw metadata saved but new images did not render; treat that as a reason to verify this site’s real route, not a universal version guarantee. Do not bypass a failed supported save gate.
7. Read back the saved source, then check normal anonymous canonical desktop and phone pages. Confirm actual image content, readable text, intended crop, no sideways overflow, and working original links. A logged-in preview or cache-busted fetch alone is not the visitor result.
8. If a known cache/static delivery layer still serves old cards, use only its maintained authorized publishing/recovery procedure and verify parity. Keep saved-but-not-public state explicit. Record the accepted card pattern and affected pages for later builds without claiming a fleet-wide rollout from one repair.

## Definition of done (QA checklist)

- [ ] Every affected card retains its actual article text and canonical destination.
- [ ] Thumbnails are real relevant source assets, not placeholders or size-heuristic passes.
- [ ] Layout preserves readable content, useful crop and no overflow on desktop and phone.
- [ ] The actual supported save route and normal public rendering are both verified.
- [ ] Pending publishing/cache layers and out-of-scope modules remain explicit.

## Example(s)

**Fictional teaching example — no card was edited.** Maple Cycle’s home page has three text-only article cards. The quote-guide article already has a real workshop frame. Its card uses visible overflow and padding.

The teaching change puts the image above a body wrapper that keeps the original title, excerpt and link. A save response succeeds, but the public home page still lacks the picture. The result remains “saved; public delivery pending” until the supported builder/cache path and normal visitor view show it.

Downloading a placeholder with a large file size or renaming a stock image would not meet the standard.

## Handoff and Content Factory context

The site/page owner receives the checked card pattern and source/public receipts. [Review article covers](https://local-service-spotlight.github.io/task-library/?task=verify-featured-images-unique-per-blog-post#task-verify-featured-images-unique-per-blog-post) supplies missing source assets, while the [Website QA master](https://blitzmetrics.com/website-qa-audit/) governs the resulting page check.

This task’s source placement is **Post** in the [Content Factory](https://blitzmetrics.com/content-factory/). It puts real article assets into an existing public page and checks their delivery. Produce supplies real source media, Process prepares the article/assets, and Promote remains separate. The exact asset and page tasks above define dependencies; catalog order does not.

## When this runs

Run when an existing card lacks its relevant thumbnail or its layout/source changes. Apply the pattern to future builds when those builds are actually assigned; this guide creates no automatic fleet-wide edits.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/blog-card-thumbnails-standard/
- Exact task: [Add homepage blog-card thumbnails](https://local-service-spotlight.github.io/task-library/?task=add-homepage-blog-card-thumbnails#task-add-homepage-blog-card-thumbnails)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [WordPress post fields and list pagination](https://developer.wordpress.org/rest-api/reference/posts/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual source assets, card layout, supported builder route and public delivery evidence require the site.
- The historical owned article’s version-specific workarounds and thumbnail/cache shortcuts need current owner reconciliation; this candidate does not certify those old commands.
- No independently verified completed execution is added by this authored needs-work candidate.
