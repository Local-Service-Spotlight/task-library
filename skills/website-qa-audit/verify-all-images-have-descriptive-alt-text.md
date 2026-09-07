---
name: verify-all-images-have-descriptive-alt-text
description: "Help people who cannot see an image get its point. Check each image where it is used."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify all images have descriptive alt text

Some readers hear a page read by a screen reader. This guide helps you give each useful image the right words. Start with what the image does on that page, not just its file name.

**The path:** Image placement → Purpose → Right text alternative → Served check.

**Use this when:** A page set needs image text alternatives reviewed for accessibility.

## Inputs
- The scoped page inventory and image placements, including linked images, background visuals and diagrams.
- The actual images and surrounding text, an available crawl/report and rendered page inspection.
- Supported page/media edit access and the current [Article Guidelines](https://localservicespotlight.com/article-guidelines/).
- A log that distinguishes missing attributes, intentional empty alternatives and descriptions that need correction.

## First-run prompt

> Review each supplied image placement and its role. Draft or apply authorized text alternatives based on what the image actually communicates. Preserve intentional decorative empties, name functional links correctly, and verify served content with a clear coverage and exception log.

## Steps
1. Inventory image placements as well as distinct files. The same file can do different jobs on different pages, so a media-library row alone is not enough.
2. Classify each image by its purpose. An informative photo needs the useful information in context; a decorative image normally uses an empty alt value. Missing alt is not the same as an intentionally empty attribute.
3. For an image that is the only content of a link or button, provide an accessible name that explains its destination or action. Do not merely describe “blue arrow” when the reader needs to know “Next repair step.”
4. For text embedded in an image, make the meaningful words available as text. For a complex diagram, give a brief identifying alternative and a nearby equivalent explanation or accessible detail. Do not stuff all chart values into an unreadable alt sentence.
5. Review existing alternatives against the actual visual and source facts. Replace file names, vague “image” text and keyword lists. Do not identify an unknown person or invent an achievement from appearance. A universal 100-character cutoff is not the accessibility rule.
6. Fix each affected placement through the supported source. In WordPress, confirm how that site stores existing block/builder alt values; changing a media-library default alone may leave old placements unchanged.
7. Inspect the served page and accessible names after saving. Check linked images, lazy-loaded content and mobile variants. Decorative CSS backgrounds need no duplicated prose, but a meaningful background-only message needs an accessible equivalent.
8. Save placement counts, purpose decisions, before/after alternatives and remaining unknown visual facts. A clean crawler report is one input, not proof that the wording communicates the right thing.

## Definition of done (QA checklist)

- [ ] All scoped image placements have a purpose-based text-alternative decision.
- [ ] Informative, decorative, functional and complex images are treated appropriately.
- [ ] Descriptions match source facts without keyword stuffing or invented identity.
- [ ] Actual served placements reflect authorized changes; media defaults alone are not the final check.
- [ ] Coverage, deliberate empty alternatives and unresolved source facts are explicit.

## Example(s)

**Fictional teaching example — no alt text was changed.** Maple Cycle uses a brake photo beside instructions. The teaching alternative is “Brake pad worn close to its wear line,” if that is what the source photo truly shows.

A repeated decorative chain pattern uses `alt=""`. A logo that is the only link back home needs an accessible name such as “Maple Cycle home.” A four-step repair diagram has a short label plus the full steps in nearby text.

Writing “bike repair shop best bike repair” on all four images would not help the reader understand their different roles.

## Handoff and Content Factory context

The page/accessibility owner receives exact placement fixes and unresolved visual facts. [Check image provenance](https://local-service-spotlight.github.io/task-library/?task=ensure-no-stock-images-used#task-ensure-no-stock-images-used) handles source authenticity, which alt wording cannot establish.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run before publishing and when images, links or surrounding context change. A repeated file can need another review if its use changes.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify all images have descriptive alt text](https://local-service-spotlight.github.io/task-library/?task=verify-all-images-have-descriptive-alt-text#task-verify-all-images-have-descriptive-alt-text)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [W3C image text alternatives](https://www.w3.org/WAI/tutorials/images/decision-tree/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The real image content, supported builder behavior and accessible page evidence require the site.
