# Record a real task execution

The Task Library registry and Asset Tracker still own the task list. `build/task-executions.json` adds reviewed run records that reference those task slugs; it is not another task registry.

A **task** is the reusable recipe. An **execution** is one actual attempt with a stable ID, start time, result, evidence and written meta article. A **meta article** tells what happened in that execution and what the recipe should learn. Write it after every execution, including failures and blocked work. Publication follows the existing authority and privacy rules; writing does not authorize public posting.

One parent job remains one execution. Internal QA checks, agent contributions, revisions, translations, syndicated copies and derivative articles do not create extra completed runs. A separately scoped, performed and documented child task may have a distinct execution ID with `parentExecutionId`; that child record does not add another completion to the parent task. Use multiple `taskSlugs` only when the same real execution actually performed each named task; do not list merely related skills. Never recreate old executions from pageviews, article dates, estimated cadence or URL counts. Historical runs may be backfilled only with evidence of their distinct identity and outcome.

## Three independent measures

- **Historical verified meta articles:** distinct public URLs in `build/article-meta-orbits.json`, with the recorded audit date and primary parent hub. The existing 85-source inventory is a historical article-volume audit, not 85 executions.
- **Recorded executions:** distinct execution IDs in the new ledger. Completed, failed, running, blocked and cancelled remain separate. Last-30-day completions use `finishedAt`, not the latest edit or publication date. History is partial: counts are documented lower bounds; an untracked task shows **Run frequency unknown**, never zero.
- **Importance:** the existing ordinal estimate based on recurrence, revenue and gating. This is a planning score, not observed task frequency.

None changes task completion, article certification, or a semantic HOLD. Registry `article_kind` may distinguish `task-recipe`, `topic-hub`, `entity-hub`, `reference`, `supporting`, or `unknown` without promoting readiness. Existing `before` and `after` values are generated neighboring stations, not verified prerequisite or handoff contracts; use the recipe's actual inputs and checked output links.

## Record schema, version 1

The ledger contains exactly `schemaVersion: 1` and an `executions` array. Each record has:

| Field | Requirement |
| --- | --- |
| `executionId` | Stable 3–160 character ID using letters, digits, dot, underscore, colon or hyphen. Preserve it across revisions and meta-article publication. |
| `taskSlugs` | Nonempty list of distinct existing task slugs. Slugs, not positional dashboard IDs or WordPress post IDs. |
| `recipeRevisions` | Object keyed by every named task slug; each has the public canonical `articleUrl` and actual `sourceSha256` followed in this attempt. |
| `parentExecutionId` | Optional existing execution ID for a separately scoped and documented child run. No self-link or cycle. |
| `startedAt` | Actual ISO timestamp with timezone. |
| `finishedAt` | Required only for completed, failed or cancelled attempts; absent while running or blocked. |
| `status` | `running`, `completed`, `failed`, `blocked`, or `cancelled`. |
| `result` | Short public-safe result, maximum 600 characters. Do not include private client facts. |
| `evidence` | Array of public URL references or private-content hashes. At least one is required for completed work. |
| `metaArticle` | Written draft, withheld written draft, or published article; see below. |
| `recordedAt` | When the execution was first entered in this ledger, at or after its start. |
| `updatedAt` | Record revision time, at or after `recordedAt` and any finish time. |

Public evidence is exactly `{"visibility":"public","url":"https://…"}`. Private evidence is exactly `{"visibility":"private","sha256":"<actual saved-content SHA-256>"}`. Keep private files, paths, notes and credentials outside this repository. URLs must be public HTTPS without credentials or credential-like query fields. The validator cannot establish that arbitrary prose or a remote page is safe: review the exact public fields and destinations before committing.

A published meta article is exactly `{"status":"published","url":"https://…"}`. A written draft is exactly `{"status":"draft","draftSha256":"<actual saved-draft SHA-256>"}`. A written article intentionally withheld from publication uses the same hash shape with `status: "withheld"`. A URL or a draft hash alone does not prove completion; status and run evidence must reflect what happened. Keep an in-progress meta draft for a running record and update the same record when the work ends.

`build/executions.py` validates this schema. Its public projection explicitly omits hashes and unpublished draft details. `dashboard/executions.json` and each task's `executionHistory` contain only public-safe record fields, status, documented counts, public evidence links and whether private evidence was retained. Treat the source ledger as public-release material too; it must not contain confidential content.

## Validate, record and revise

Build current task data first, including the Asset Tracker CSV when applicable, so the CLI validates against the actual task registry:

```sh
python3 build/build.py
python3 scripts/record_execution.py /path/to/real-run.json --check
python3 scripts/record_execution.py /path/to/real-run.json
python3 -m unittest discover -s build -p 'test_*.py' -v
python3 build/build.py
```

The CLI records only data; it does not run the task, publish a meta article, merge a change, schedule work or grant authority. Review and deploy through the repository's existing pull request and GitHub Pages workflow.

The receipt returns `executionId`, `action` and a SHA-256 `revision`. Resubmitting identical content is idempotent and changes no count. For a correction, resume, completion or published-meta URL, preserve `executionId`, `taskSlugs`, `startedAt` and `recordedAt`, advance `updatedAt`, and supply the exact previous record revision:

```sh
python3 scripts/record_execution.py /path/to/revised-real-run.json --check --expected-revision PREVIOUS_SHA256
python3 scripts/record_execution.py /path/to/revised-real-run.json --expected-revision PREVIOUS_SHA256
```

Stale revisions, unknown tasks, duplicate IDs and unsupported fields fail before replacement. A stable sidecar lock serializes CLI writers. The ledger is written to a temporary file and replaced atomically; failed replacement leaves the previous ledger intact. `--check` validates the proposed insert or update without writing an execution record.

Correct an inaccurate completion on the same ID with a reviewed revision; do not mint a second ID to hide it. Git retains the change history. A retry is a new execution only when it is an actual separate attempt with its own real start, outcome, evidence and written meta article.

## Feed the result back into the recipe

Link the written meta article to the canonical task article and exact Task Library slug. Record what was attempted, observed, failed, corrected and left unknown. Propose source-backed improvements to the canonical recipe or runnable skill, independently review them, then use the existing publish/merge authority. Keep the evidence that justifies the change. The next execution checks the revised recipe; editing the recipe does not itself increase execution counts.

No synthetic production records ship with this implementation. Fixtures remain in tests. The current article-cleanup parent run must receive its actual stable ID, final outcome and saved meta article before it is registered; child-agent notes are supporting evidence for that same parent execution.
