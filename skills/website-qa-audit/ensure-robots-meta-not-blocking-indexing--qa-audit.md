---
name: ensure-robots-meta-not-blocking-indexing--qa-audit
description: "Check that public pages can be read by search engines. Keep private pages private."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Ensure robots meta not blocking indexing

A public page should not be hidden from search by mistake. This guide helps you check the rules that search engines receive. Start by deciding which pages should be public and which should stay out of search.

**The path:** Page intent → Served rules → Exact cause → Verified correction.

**Use this when:** A launch, migration or audit needs unintended indexing restrictions checked.

## Inputs
- The exact URLs and owner-supplied index intent: public, intentionally excluded, private or staging.
- Public response headers, page source, robots.txt and redirect/canonical information.
- Supported CMS/server configuration access for repairs already in scope; Search Console access if indexed/live-test evidence is required.
- A dated evidence log and current source/configuration snapshot before changes.

## First-run prompt

> Use the supplied URL list and intended visibility. Inspect current headers, meta directives and crawl rules, correct already-authorized unintended restrictions, and verify canonical responses. Keep private exclusions intact and report eligibility, observed indexed state and unavailable account evidence separately.

## Steps
1. Record the intended visibility of each page before diagnosing its rules. Keep deliberate private, staging and low-value exclusions. A global “make everything indexable” change is not a valid audit repair.
2. Read the normal final page response, including redirect chain and X-Robots-Tag headers, then inspect robots and googlebot meta tags in the served HTML. Record all applicable directives; multiple rules can combine restrictively.
3. Separate noindex from nofollow. Noindex asks a crawler that can read it not to index the page; nofollow concerns following links. The shorthand none combines both. Do not call a nofollow-only page non-indexable merely because of that directive.
4. Inspect the applicable robots.txt crawl rules for the host and user agent. A disallowed page can prevent Google from reading its noindex instruction and may still appear as a URL in search. Google does not use a noindex directive in robots.txt as a supported indexing control.
5. Compare with supported CMS settings when access exists. On WordPress, the search-engine-visibility setting is one possible source, not the only cause. Check page-level SEO settings, templates and response headers before changing unrelated global options.
6. If Search Console is available, record the indexed inspection result and crawl date separately from a current live test. “Indexing allowed” establishes eligibility for that test, not a promise that Google has indexed or will rank the page. Without access, finish public-rule checks and label Search Console evidence unavailable.
7. Repair only the unintended exact restriction already in scope using the supported source. Preserve intentional exclusions and privacy. Recheck the canonical headers, body rules and relevant crawl rule after saving; do not rely only on a CMS checkbox.
8. Save intent, before/after directives, cause, actual test date and remaining issues. Hand any indexing request or later observation to its authorized search owner, without promising immediate indexing.

## Definition of done (QA checklist)

- [ ] Each checked URL has an explicit intended visibility and actual served directives.
- [ ] Noindex, nofollow and crawl blocking are distinguished accurately.
- [ ] Repairs preserve intentional private/staging restrictions and target the actual supported source.
- [ ] Public rule changes are verified on canonical responses; Search Console snapshot/live evidence remain separate.
- [ ] Eligibility, actual indexed state and rankings are not treated as the same outcome.

## Example(s)

**Fictional teaching example — no search settings were changed.** Maple Cycle’s public quote guide serves `noindex, follow` left from staging. Its private staff page is intentionally excluded. A third public page has only `nofollow`.

The proposed scoped repair removes the accidental noindex from the quote guide through its real metadata source, then checks the served response. It leaves the staff page’s intended protection alone. The nofollow-only page needs a link-policy review; it is not failed as “noindex” based on that token.

A successful live eligibility check still does not justify writing “Google has indexed all three pages.”

## Handoff and Content Factory context

The site/search owner receives exact directive evidence and any approved next inspection. [Verify the sitemap](https://local-service-spotlight.github.io/task-library/?task=verify-xml-sitemap-exists-and-in-robotstxt#task-verify-xml-sitemap-exists-and-in-robotstxt) is a related discovery check; sitemap presence does not override noindex.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run before launch and after relevant CMS, header or migration changes. Later index observations use the actual agreed search-review cadence, not a guaranteed automated recurrence.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Ensure robots meta not blocking indexing](https://local-service-spotlight.github.io/task-library/?task=ensure-robots-meta-not-blocking-indexing--qa-audit#task-ensure-robots-meta-not-blocking-indexing--qa-audit)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Google robots meta and headers](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The target site’s visibility intent, supported configuration source and actual Search Console evidence require the project.
