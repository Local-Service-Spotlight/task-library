---
name: ensure-no-text-only-sections-spanning-full-viewport
description: "Break up long walls of text with useful visuals. Check that the page is clear on a phone too."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Ensure no text-only sections spanning full viewport

A wall of text can make a useful page hard to follow. This guide helps you give readers clear breaks and useful pictures. Start at the top, then check the long sections on a phone and a large screen.

**The path:** First screen → Long text stretches → Useful visual or edit → Two-width check.

**Use this when:** A public page or defined page set needs first-screen visuals and long text sections reviewed.

## Inputs
- The canonical pages in scope, their intended readers and current full content.
- Real relevant photos, diagrams or source screenshots with appropriate rights.
- Views at 1440×860 and 390×844, the supported editor and authorized layout/edit scope.
- The current [Article Guidelines](https://localservicespotlight.com/article-guidelines/) and an issue log for exact sections and missing assets.

## First-run prompt

> Review the supplied canonical pages at desktop and phone sizes. Check the first meaningful visual and full-body text stretches. Make authorized clarity/layout fixes with accurate visuals, then report exact before/after observations and missing assets without claiming unmeasured engagement results.

## Steps
1. Open each normal canonical URL at both viewports. Capture the initial screen before scrolling and identify the useful visual content actually visible. A blank box, loading border or offscreen image does not satisfy the opening rule.
2. Read the opening. It should explain who the page helps, why and the useful result at grade 5 or below. Confirm the visual reinforces that point rather than adding unrelated decoration to pass a box.
3. Scroll the full in-scope body at each width and identify continuous stretches of unbroken text that fill a screen. Record section names and approximate start/end positions. A few short paragraphs separated by a clear relevant visual differ from a large uninterrupted slab.
4. Use judgment on necessary utility or reference material, with an explicit reason where the visual rule does not apply. Do not insert random pictures into a legal clause or data table simply to interrupt every possible scrolling window. Keep the main article’s first-screen rule intact.
5. Choose a fix tied to meaning: shorten repetition, divide the explanation into clear steps, add a real source photo, or draw a small accurate diagram of the process. A decorative band or meaningless icon row does not make the explanation clearer.
6. Keep visuals readable at phone size. Check actual labels, image content, width and aspect ratio. A long diagram may continue below the fold if the visible part already communicates a useful complete point; a tiny full-figure thumbnail is not automatically better.
7. Apply authorized text/layout changes in the supported source, preserving useful media and factual meaning. Give any missing real asset an owner rather than inventing proof.
8. Recheck the first screen and repaired sections on normal canonical desktop and phone pages. Save exact observations and remaining gaps. This house layout check does not by itself measure bounce rate, engagement or conversion.

## Definition of done (QA checklist)

- [ ] Both first viewports show a meaningful readable visual with clear opening context.
- [ ] The full scoped body is reviewed for long unbroken text stretches at both widths.
- [ ] Fixes help explain the section and preserve source facts and useful existing media.
- [ ] Phone labels/content are readable with no sideways overflow.
- [ ] Exceptions and missing assets are specific, and no unmeasured behavior improvement is claimed.

## Example(s)

**Fictional teaching example — no layout was changed.** Maple Cycle’s quote guide opens with a useful workshop photo, but the phone view then shows two full screens of dense instructions.

The teaching revision removes repeated advice and adds a four-step diagram: “Take clear photos → Add the bike issue → Send to the shop → Receive the next step.” Each label fits at phone width. The diagram describes the guide’s actual process and does not claim that a quote or sale has happened.

The reviewer still checks the normal phone page after saving; an image tag in the source is not proof that readers can see it.

## Handoff and Content Factory context

The page owner receives the repaired-section evidence. [Review major home-page visuals](https://local-service-spotlight.github.io/task-library/?task=check-each-homepage-section-includes-relevant-image#task-check-each-homepage-section-includes-relevant-image) is a companion check for home pages; broader page QA uses its own defined scope.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run before publishing or after significant content/layout changes. An ongoing layout monitor requires a configured site-specific job; this guide creates none.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Ensure no text-only sections spanning full viewport](https://local-service-spotlight.github.io/task-library/?task=ensure-no-text-only-sections-spanning-full-viewport#task-ensure-no-text-only-sections-spanning-full-viewport)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual viewport observations, supported editor behavior and missing real assets require the target pages.
