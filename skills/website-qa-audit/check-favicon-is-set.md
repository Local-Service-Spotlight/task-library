---
name: check-favicon-is-set
description: "Check the small icon next to your site’s name. Make sure it is clear and uses the right brand."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: needs-work
---

# Check favicon is set

The small icon in a browser tab helps people spot your site. This guide helps you check that it loads and uses your brand. Start with the live home page and the icon it declares.

**The path:** Declared icon → Real image → Browser view → Search eligibility.

**Use this when:** A site launch, brand change or audit needs the browser/site icon checked.

## Inputs
- The canonical home page and approved square brand icon or clear identity mark.
- Public page source, icon response and browser tab view; supported site settings access if a correction is in scope.
- The expected hostname and any deliberately separate subdomain icons.
- A record of the prior icon source and declared icon links for safe comparison.

## First-run prompt

> Inspect the supplied home page’s declared icons, actual image responses and browser display. Fix authorized icon settings through the supported source. Report exact asset dimensions, desktop/mobile observations and Google eligibility separately from any observed search result.

## Steps
1. Read the home page’s icon declarations, such as link rel="icon", and resolve the href to its real URL. A relative path, absolute path or supported CDN URL can be valid. Do not require /favicon.ico when the page correctly declares another path.
2. Fetch or inspect the declared asset as an image. Confirm it is not a 200 response containing an HTML error page. Record format, dimensions and square aspect ratio, and check that the mark remains clear at tab size.
3. Open the canonical home page in a fresh browser context and inspect the actual tab icon. Compare it with the declared file. Check the mobile browser’s displayed site identity where available; installing a home-screen shortcut is not required for this audit.
4. Inspect competing icon declarations and relevant supported site settings if the wrong icon persists. In WordPress, use the current Site Icon control supported by that site’s version/theme; do not assume an old menu path is universal.
5. Apply the authorized icon or declaration correction. Preserve the approved brand and a stable asset URL where appropriate. Recheck the normal page and browser after the supported cache refresh, rather than treating a cache-busted asset alone as success.
6. For Google eligibility, follow its current favicon rules: a square image at least 8×8 pixels, with a larger image than 48×48 recommended; home page and icon must be crawlable by the relevant Google crawlers. Keep this separate from the larger dimensions a CMS may request for its Site Icon upload.
7. Record browser display and search eligibility separately. Google can take days or weeks to recrawl and does not guarantee favicon display even when the rules are met. An old search icon is not proof the saved icon change failed.
8. Save the actual icon URL, dimensions, checks, date and any unresolved browser/cache or search observation. Do not create a new app manifest or install anything just to complete this single check.

## Definition of done (QA checklist)

- [ ] The declared icon resolves to the correct real square image and is legible at small size.
- [ ] The normal browser view uses the intended icon, or a specific cache/display gap remains.
- [ ] A missing undeclared /favicon.ico is not falsely reported as the declared icon failing.
- [ ] Google eligibility and observed search display are recorded as different results.
- [ ] No app install or unrelated global theme change was added to the task.

## Example(s)

**Fictional teaching example — no site settings were changed.** Maple Cycle declares `/media/maple-icon.png`, a 192×192 square icon. That file loads as an image and appears in the browser tab. `/favicon.ico` returns 404.

The browser icon check passes because the declared valid file is what the browser uses. The missing optional root path is not a failure. If a Google result still shows an older icon, record “browser correct; search still shows prior icon as of this check” and recheck under the agreed scope. Do not claim that requesting a recrawl guarantees replacement.

## Handoff and Content Factory context

The site owner receives the icon evidence and any supported settings/cache fix. If only search display is pending, a future observation belongs to the existing search review owner, not a new guaranteed timer.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at launch and when branding or icon delivery changes. A search recrawl follow-up is optional and needs an actual owner or configured schedule.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Check favicon is set](https://local-service-spotlight.github.io/task-library/?task=check-favicon-is-set#task-check-favicon-is-set)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Google favicon guidelines](https://developers.google.com/search/docs/appearance/favicon-in-search)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The actual site icon, current CMS control, cache behavior and browser observation require the target site.
