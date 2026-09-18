# Checking the guide your team will use

A clear guide helps your team do a job and check the result. We added a way to record which version was checked, so an old review cannot approve a changed page. This work supports the [Task Library Standard](../Task-Library-Standard.md) and the [main guide to writing a definitive article](https://blitzmetrics.com/definitive-article-guide/).

```mermaid
flowchart LR
  A[Read the guide] --> B[Check its meaning]
  B --> C[Check the current version]
  C --> D[Try the task]
  D --> E[Save proof and improve]
```

## What we attempted

This is the work record for `article-review-20260918-063904`, begun September 18, 2026 at 06:39:04 UTC. Its scoped task was to improve the definitive-article guide's opening and make article review evidence recordable. The outcome is **partial**: the code passed its checks; the article edit is staged and was not saved to WordPress.

The starting guide source was captured before editing as SHA-256 `be544b8ad0d81921fe2cf865ebde323f58384bd6dfa88c0dd0d637f11f69f07f`. The candidate source is `5f4a981dd5d5b3ed52ea6eca4179a1ea872da25b6f728e782c4b5a652ab7a6a8`.

## What changed

The existing article evidence file now supports ten explicit review checks and a separate observation of the current article version. A review records its task, mapped URL, source hash, reviewer, date, verdicts and proof. The observation must match that source and be no more than 24 hours old. A missing or stale observation stays unknown. A changed source fails the match. Existing holds remain in force.

The checks cover the opening, page role, owner, steps, links, examples and source evidence, Content Factory handoff, visuals and layout, publishing standards, and acceptance results. They do not turn contributor status into proof of a successful task or first-time setup. The [evidence format](../build/ARTICLE-SEMANTIC-REVIEWS.md) explains the fields.

The staged guide opens with three short sentences: what the guide helps a business do, why clear steps help its team, and how it connects to the linked Content Factory. Independent editorial review found the opening clear; its approximate Automated Readability Index was grade 4.8. A reading score alone does not establish meaning or certify the whole article.

## What the checks found

All 121 build tests and 89 script tests passed. Tests cover missing criteria, invalid evidence, old or changed sources, hold precedence and unchanged legacy records. No positive semantic certification was inserted. The current baseline remains 276 tasks, 275 reviewed instruction versions, three instruction-requirement passes, and zero fully verified tasks.

A preview using the real public page shell exposed a layout defect: the opening ran below the first phone screen. Reducing the lead diagram's vertical spacing preserved its labels and arrows. The revised preview showed the complete opening on a 1280-by-800 desktop screen and a 390-by-844 phone screen. Actual screenshots were reviewed for desktop with JavaScript on and off and phone with JavaScript off. Phone geometry passed with JavaScript on, but its final reliable screenshot remains unverified.

The browser connection then failed while loading its request-header policy. One retry failed too. We retained the candidate and did not publish it. This is a tool failure, not evidence that the public page passed or failed the remaining check. The newly added Content Factory link still needs its final destination-content check.

## What the next run should do

Recover the supported browser connection, check the final phone view and link destination, then re-read the WordPress source before any save. If the starting source has changed, reconcile it first. Publish only the reviewed candidate and verify the ordinary public page. Record a full article verdict only after all ten checks have evidence.

Next, extend the existing run records to capture a real new user's setup and an independently accepted result. Then use those fields on actual tasks, starting with the highest-priority actionable rows. Writing this work record, running tests, and improving a recipe do not create successful business executions.
