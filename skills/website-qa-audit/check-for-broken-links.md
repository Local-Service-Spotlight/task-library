---
name: check-for-broken-links
description: "Find links that leave readers stuck. Check the cause and fix the right target."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Check for broken links

A dead link wastes a reader’s time. This guide helps you find links that fail and choose the right fix. Start with a clear list of pages so you know what the check covers.

**The path:** Known pages → Link results → Cause and fix → Fresh evidence.

**Use this when:** A launch, migration, content update or defined audit needs link destinations checked.

## Inputs
- The canonical site, full published URL list where available, and the agreed internal/external link scope.
- An available crawler or supported link report, a browser and the ability to inspect response status and final destinations.
- The current topic/URL map and edit scope, including any authorized redirects.
- An issue tracker with exact source pages, anchor text, target URLs and owners.

## First-run prompt

> Use the supplied published inventory and link scope. Build a dated report, verify each failure’s cause, fix already-authorized exact targets and recheck normal canonical pages. Separate broken, restricted, transient and untested results, and return remaining issues with owners.

## Steps
1. Record the known page inventory and crawl settings. Reconcile crawl coverage with the published list; list restricted or unvisited pages. Save the scan date and avoid claiming the whole site was checked from a small sample.
2. Collect each source page and outgoing target, separating internal links, external links and named fragments. Exclude actions such as tel:, mailto: and state-changing submissions from an ordinary HTTP crawl; send them to their relevant safe test.
3. Review reported failures. A 404 or 410 differs from a 401/403 access block, 429 rate limit or temporary 5xx response. Some targets reject HEAD requests or bots but work for a normal visitor. Verify with the appropriate safe page read rather than repeatedly hammering the server.
4. Inspect apparent successes too: a 200 status can contain an error or unrelated page. Check that the destination answers the anchor’s promise and that a #fragment exists. A redirect is not automatically broken; note its final destination, loops and unnecessary internal chains.
5. For an internal stale link, identify the exact equivalent current page and update the source link directly within scope. Use a redirect only when the actual URL migration warrants it. Do not send every missing page to the home page.
6. For an external failure, verify whether the source moved or an authoritative replacement supports the same claim. Update it or remove/rewrite the unsupported sentence as appropriate. A login-blocked valid primary source is an access limitation, not automatic evidence that the link is dead.
7. Apply authorized repairs with the supported page or redirect source. Preserve unrelated links and concurrent edits. Stage any unresolved content decision with the exact owner and proposed replacement.
8. Rerun the relevant scan after changes and inspect changed canonical source pages. Log checked links, confirmed failures, repaired/verified links and remaining unknowns. Zero known failures within a stated scope is not a promise that all future links will work.

## Definition of done (QA checklist)

- [ ] Scope, scan date and missing coverage are explicit.
- [ ] Each failure records its exact source, target, observed response and actual cause where known.
- [ ] Access restrictions, rate limits, transient errors and broken destinations are not collapsed into one result.
- [ ] Repairs point to relevant canonical equivalents and survive a fresh public check.
- [ ] Unresolved issues have owners and no unsupported site-wide zero claim.

## Example(s)

**Fictional teaching example — no links were requested.** Maple Cycle’s sample scan reports three problems. `/old-quote/` redirects twice to the current quote guide; an internal body link should use that final guide directly. A parts supplier returns 403 to the crawler but opens for a normal visitor, so the result is “crawler restricted,” not “dead supplier.” `/brake-photo/#rear-view` opens a real page but has no matching section, so the fragment needs correction.

The useful report keeps those three causes separate. Redirecting all three targets to the home page would hide the problem and mislead the reader.

## Handoff and Content Factory context

The site/content owner receives verified fixes and unresolved targets. [Review internal link relevance](https://local-service-spotlight.github.io/task-library/?task=audit-internal-links-between-all-blog-posts#task-audit-internal-links-between-all-blog-posts) handles missing editorial connections that a status-code check cannot judge.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run for defined audits and after relevant migrations or edits. A scheduled crawl is optional and must use the site’s real configured cadence and rate limits.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Check for broken links](https://local-service-spotlight.github.io/task-library/?task=check-for-broken-links#task-check-for-broken-links)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [SEO Tree](https://blitzmetrics.com/seo-tree/)
- [Entity linking](https://blitzmetrics.com/entity-linking/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Current site coverage, actual destination responses and authorized repair/readback evidence remain site-specific.
