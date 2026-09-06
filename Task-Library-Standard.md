# The BlitzMetrics Task Library Standard
### How every task becomes a definitive article + a skill.md + linked examples

**Source of truth:** [How to Create a Definitive Article for Any BlitzMetrics Concept](https://blitzmetrics.com/definitive-article-guide/) and the [Task Library Dashboard](https://local-service-spotlight.github.io/task-library/). This standard reflects the task-recipe and per-execution feedback requirements reviewed September 2026.
**Purpose:** a single spec the Fable workers (and any human/agent) follow to bring every registered task up to standard — each one documented, downloadable as a skill, and wired into the SEO Tree. Counts are always derived from the registry/build; never type a task or article count into copy.

---

## The model: three artifacts per task
A task is a repeatable recipe with an explicit starting state and checked result. A topic or entity hub, reference, comparison, story, and task recipe are different page roles. Related topic pages support the task; they do not become task recipes merely because they have a clear opening or visual.

Every actual task in the library targets **three linked artifacts**, and they point at each other. A missing or incomplete artifact stays visibly in progress; a URL mapping alone never makes a page definitive.

1. **Article hub** — the one canonical page that owns the concept. It becomes a **definitive article** only after the Green/ready validation below. It lives at a stable URL on the approved canonical domain for that concept (for example, `blitzmetrics.com` or `localservicespotlight.com`). Declare one working copy; an older-domain page may remain as an archive, but do not map tasks to a replacement until the working copy has content parity and passes validation.
2. **skill.md** — the machine-readable SOP an AI agent runs to *do* the task. Downloadable, one file per task. References its mapped article hub, or explicitly records a GAP.
3. **Examples / meta-articles** — real proof the task was done, each documented with the Meta-Article Prompt and linking back up to the article hub.

> Relationship: **examples / meta-articles → article hub → course/service**, and a ready definitive hub links **across** to related definitive articles. The Task Library card links to the canonical article, while the article links back to its exact Task Library task or normalized hub route. Never publish a second page that competes with a hub (that's "content vandalism").

## Bidirectional Task Library links

- **Task → article:** every mapped Task Library card links to its final canonical article URL. The visible label is derived from the URL-level ready/WIP state; a mapping alone cannot produce a definitive label.
- **Article → exact task:** use `https://local-service-spotlight.github.io/task-library/?task=<permanent-task-slug>#task-<permanent-task-slug>` when an article names one exact SOP. The query drives filtering; the stable fragment identifies the row.
- **Article → all mapped tasks:** use `https://local-service-spotlight.github.io/task-library/?article=<URL-encoded-canonical-article-URL>` in the definitive marker or evidence footer. The dashboard normalizes scheme, `www`, trailing slash, query, and fragment exactly as the build does, then shows every task mapped to that hub.
- The generated `articleHubs[]` index and each task's `taskLibraryUrl` are the machine-readable owners of these reverse URLs. Do not hand-build a second mapping in WordPress.
- An archive or redirecting alias may point readers to the current standard, but tasks and reverse links map only to the approved canonical URL. An archive leaf never receives a Definitive badge.

---

## The Nine Requirements of a Definitive Article
A page is only "definitive" if it meets **all nine**. Miss one and it's a draft (Yellow), not done (Green).

1. **Specific Goal, Content and Targeting in the opening** — make the reader's actual situation, reason to care, useful outcome and supporting mechanism clear in the first two or three sentences at grade 8 or below. Lead with a concrete problem, useful finding or true moment. The body must deliver the promise. Explain unfamiliar terms on their first mention and link the maintained owned explanation. A keyword, grade score or generic audience label cannot approve meaning.
2. **The complete process / framework for the declared page role** — a task recipe must name its trigger or starting state, inputs and required access, prerequisite tasks and their checked outputs, ordered steps with expected results, measurable completion criteria, and the receiving task or handoff. A topic hub may teach a framework and link its recipes. Do not give a reference or story a page-wide recipe label.
3. **Relevant verified examples** — link the real evidence that demonstrates this method or task, with a brief explanation of what each source proves. A count, copied story or unrelated mention is not completion evidence. Preserve failures and incomplete results honestly.
4. **Links to related concepts and entities** — cross-link the other definitive articles and route named people, companies, tools, and concepts through the Entity Destination Rules below (builds the entity graph).
5. **Links to the course/guide/service** — as a CTA near the bottom, not as the core content.
6. **Compliance with the [maintained Article Guidelines](https://localservicespotlight.com/article-guidelines/)** — title <60 chars; meta description <160; primary keyword in first paragraph; H2/H3 structure; short paragraphs; active voice; no AI-fluff phrases; no stock images; entity-linking decision tree for internal links.
7. **A short URL** — memorable redirect (e.g., `/dad`, `/digital-plumbing`) pointing to the hub, not the homepage or a case study.
8. **Article-specific lead visual above the fold, then lower task context** — place a meaningful real photo, source screenshot or task diagram beside or just after the short opening. Verify that useful content and readable labels, not an empty border, are visible on the first anonymous visit at desktop 1440 × 860 and mobile 390 × 844. Every actual task recipe must show a truthful lower task map. Further down each actual task recipe, show its honest place in the Content Factory: Produce → Process → Post → Promote, plus its actual inputs, outputs and handoff. For a Content Factory task, use the full canonical Content Factory diagram when it is needed to explain the workflow, highlight only the relevant parts, and keep surrounding context readable. Support tasks may support several stages without pretending to produce a content asset. The framework map is orientation, not generic hero art; it must not displace the article's primary evidence. Link the relevant task or method nodes and add an accurate caption or text equivalent. For pages that are not task recipes, do not force a generic Content Factory diagram. All media checks remain muted with volume zero; use a silent alternative if that state cannot be verified before playback.
9. **Third-party endorsements / testimonials / E-E-A-T** — media, conference talks, podcasts, practitioner testimonials with proof. Highest-authority first; volume matters. (The `/dad` article is the gold standard.)

---

## Entity Destination Rules
Explain unfamiliar language and apply this decision tree to the **first useful mention only**, with descriptive 3–6 word anchor text. Do not link the same entity repeatedly in one article.

1. **Person with a verified personal-brand site** → that person's own site. Example: Dennis Yu points to `dennisyu.com`, not a WordPress author archive.
2. **Company or organization in our network** → its verified official site. For an outside entity in explanatory copy, use our maintained guide when available; preserve direct primary-proof and required-action links at their actual step.
3. **Tool, platform, or method with a BlitzMetrics training article** → the internal hands-on article that teaches the task. The official product site may be linked separately at the execution step where the reader must open the tool; it does not replace our training link in explanatory copy.
4. **Named entity without a verified home or relevant internal article** → plain text until verified. Never guess a domain, personal site, or destination.

These links exist to help the reader identify the entity and complete the task. They are not decorative SEO links.

---

## When a page may display “Definitive”
The visible label is a validation result, not a writing style or a manually chosen badge.

- The build groups tasks by normalized article URL. A hub is `ready` only when **every task mapped to that URL is `complete`** and no reviewed semantic-certification hold is active. One `needs-work` or `gap` task keeps the entire hub `wip`; a missing article mapping is excluded from article counts.
- A semantic mismatch in the live hub may force the URL to `wip` without falsifying any completed task. Reviewed holds live in `build/article-certifications.json`, require a dated reason, and may only downgrade readiness. Remove a hold only after the hub itself is corrected and reviewed against its authoritative framework or SOP.
- A task-recipe label requires an actual recipe contract; a topic/entity hub, reference or supporting article keeps its own role. Only a task recipe may use **Definitive SOP**. Only a `ready` hub may show the consistent **Definitive article** marker near the top of the page and the **Definitive article ↗** label in the Task Library.
- A `wip` hub must show **Article in progress** where a status label is useful. It must not carry a green/definitive badge merely because the page is published or mapped.
- Catalog readiness and absence of a hold are necessary, not positive semantic certification. Before a Definitive marker, an actual reviewer must confirm the declared role and scope, owner, detailed steps, links, source evidence and acceptance results for that exact revision. Record the reviewer and evidence; neither a mapping nor the build supplies that judgment.
- Re-run live page QA before promotion: the build state is the catalog receipt, while rendered content, links, diagram placement, schema, and mobile layout are the publication receipt.

---

## The 10-Step Creation Process
Run in order for any task in a Yellow/Red (Needs Work / Gap) state:

1. **Identify the concept** and find every existing article that mentions it (the hub organizes them, doesn't replace them).
2. **Write the specific GCT opening** in two or three short sentences at grade 8 or below. Explain the reader's situation, why this matters, the useful outcome and how the task helps. A meaningful task visual may lead. Save the exact opening and quoted reviewer evidence in the existing run receipt; the body must deliver its promise.
3. **Document the process/framework** (the SOP — this is what the skill.md mirrors).
4. **Link the relevant verified examples** (1–2 sentences explaining what each source proves).
5. **Cross-link related concepts and entities** using the Entity Destination Rules (other definitive articles, verified personal sites, verified company sites, and internal training for tools).
6. **Link to the course/service** (CTA).
7. **Set the short URL** (redirect to the hub).
8. **Add the article-specific lead visual above the fold and the task's lower Content Factory context**; preserve the real workflow and do not force a task map onto a non-recipe page.
9. **Add E-E-A-T** (endorsements, testimonials, media — highest authority first).
10. **Write the execution meta article and verify the result.** Write one after every actual task execution, including failed, partial and blocked work. Publication is separately authorized; verify the live result if publication occurred. Link the canonical recipe and exact Task Library task, register the distinct execution ID with evidence, and propose source-backed improvements to the recipe. Revisions and internal checks stay on the parent ID. Add the visible Definitive marker only after the URL-level ready gate passes.

---

## Where definitive articles live in WordPress
- Default new editorial guides to a **Post** when appropriate. Preserve the type, stable URL and durable source of an existing canonical **Page** or Post; this standard does not authorize migration or replacement.
- Assigned to the **Definitive Articles** category only after the URL-level hub is `ready`. A published WIP article stays in its operating/topic category and is not taxonomically presented as definitive.
- Carries the canonical Task Library category or categories represented by its mapped tasks, using names from `build/categories.json`; do not invent a near-duplicate category. Each task has exactly one library category, but a shared hub may represent several.
- Tagged with every **Content Factory stage** represented by its mapped tasks (`Stage: Produce | Process | Post | Promote`) and no others, plus the smallest useful set of existing cross-cutting **Topic:** tags. A hub with no task in the four phases omits the Stage tag. Reuse canonical tag slugs; do not create spelling, punctuation, singular/plural, or capitalization variants.
- The category, stage, article URL, and task status must agree with the corresponding `skill.md` frontmatter and registry entry. This lets agents query the REST API without translating competing taxonomies.
- Prefer the **standard block editor (Gutenberg)** for a new editorial guide when appropriate. Preserve an existing Cornerstone or other builder page and use its supported durable save pipeline. Verify both the stored source and anonymous public result; editing an empty raw post body is not a builder save.

---

## The skill.md standard (one file per task)
Every task gets a `skill.md` an agent can run. House format — keep it tight, SOP-grade, and grounded in the definitive article:

For any task that creates a document, report, presentation, page, article or landing page,
the opening and QA inherit the [maintained specific-GCT source
rule](https://github.com/dennisyu/local-service-spotlight-skills/blob/main/standards/every-article-and-project-starts-with-specific-gct.md).
Use `step-7-write-hook-and-establish-context` as the detailed writing/review station.
Adapt the value to the actual reader: an audit supports a decision, a guide enables a
task, and a money page connects relevant proof to the offer and buying action. Do not
paste an entrepreneur pitch or unsupported conversion promise onto every artifact.
The first page/screen pairs that short opening with a meaningful authentic visual;
later document pages lead with their own useful takeaway. Retain the exact text,
revision, reviewer quotations and PASS/FAIL/UNKNOWN reasons in the existing receipt.
This changes the content contract, not publishing, delivery or scheduling authority.

```markdown
---
name: <kebab-case-task-slug>
description: <one sentence — what running this skill accomplishes, and for whom>
category: <exact canonical category name from build/categories.json>
stage: <Produce | Process | Post | Promote | — >        # Content Factory stage if applicable
definitive_article: <short blitzmetrics.com path, absolute URL on another approved canonical domain, or "GAP — to be written">
status: <complete | needs-work | gap>
---

# <Task Name>

**Use this when** <the trigger situation, in one line>.

## Inputs
- <what the agent/operator needs before starting>
- <for a reader-facing artifact: actual reader/situation, useful outcome, source evidence and relevant opening visual>

## Steps
1. <imperative, concrete step>
2. ...
   (Mirror the definitive article's process exactly; this section IS the SOP.)

## Definition of done (QA checklist)
- [ ] <objective, checkable pass criteria — what "good" looks like>
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with [Article Guidelines](https://localservicespotlight.com/article-guidelines/) (if it publishes content)
- [ ] If it creates a reader-facing artifact, the short opening makes relevance, useful outcome and supporting mechanism clear; quoted reviewer evidence is retained and the artifact delivers its promise

## Example(s)
- <link to a real example / meta-article demonstrating this task>, 1–2 sentences on why it's relevant.
  (If none exists yet: "Example needed — run the Meta-Article Prompt after first real run.")

## Definitive article & links
- Hub: <short URL>
- Related: <sibling definitive articles / skills, in run order>
```

**Rules for skill.md authors (Fable workers):**
- The `name` slug is permanent (installs/bundles depend on it). Match the task slug.
- `category` must exactly match one name in `build/categories.json`; `stage` must be one of `Produce | Process | Post | Promote | —`. Do not create an alias because a WordPress category or tag is spelled differently—fix the taxonomy drift instead.
- Steps must mirror the task's real SOP — use the definitive article's documented process, Dennis's frameworks (GCT, MAA, the 4 P's, SEO Tree, entity-linking decision tree, Dollar a Day mechanics), and the task description. No invented tools or fabricated URLs — reference only the task's real definitive-article short URL and known BlitzMetrics concepts.
- Every skill.md must carry a **Definition of done** checklist (the QA layer) and at least a placeholder **Example** so the meta-article loop has a slot to fill.
- For **gap** tasks (no article yet), set `definitive_article: GAP — to be written`, write the SOP from the description + method, and flag the missing hub.

## Importance (1–5 volume bar)
Every task carries an **importance** score, shown as a 1–5 bar on the dashboard. It is `max(frequency, revenue, gating)`, scored from evidence, not vibes:

- **Frequency** — does this run every factory cycle, weekly, monthly, once per client, or yearly?
- **Revenue** — ads, boosts, pixels, and conversion paths are 5. Publishing the asset ads will amplify is 4. Maintenance is 1–2.
- **Gating** — a small "get access" task is a **5** if skipping it blocks the chain (GSC, GTM, Meta pixel, Business Manager, Descript, WP author).

The scoring table lives in `build/factory.py`. Do not hand-edit bars on the dashboard.

## Factory chain
Tasks are stations on Produce → Process → Post → Promote, with Digital Plumbing as Gate. Every skill.md must name **Before** and **After** (sibling run order). The dashboard renders the chain; agents must not start a station as an isolated chat.

## Model routing
Name the lane: `script` | `local` | `any` | `judgment` | `computer`. **Single-engine is first-class:** an operator with only Grok or only Claude still runs the whole factory. Multi-engine (local overnight writer + frontier Jennifer + REST publish) scales the same line. Pass work as files, never through one vendor's memory. Canonical skill: `run-content-factory-on-any-engine`.

---

## Examples = meta-articles
"Lots of real examples" (Requirement 3) is satisfied by **meta-articles** — each documents one real run of the task via the Meta-Article Prompt and links back to the definitive article. A canonical task article, published skill.md and at least one relevant linked example/meta-article are minimum artifacts; acceptance checks and semantic review must also pass before a task is fully "Green". The canonical `/meta-article-prompt/` and `/internal-linking` hubs are the models to copy; their historical published-example totals come from the dated orbit inventory below, not an execution counter.

Meta-article strength is derived from `build/article-meta-orbits.json`; never type a count into an article or dashboard card. Each audited hub and candidate source preserves the public source URL, normalized hub URL, evidence method, date, counted decision, and reason. Hubs absent from that evidence file are **unknown**, never zero. `partial` counts render with a plus sign because they are a verified lower bound; `verified` counts may render as exact, including a source-backed zero.

The count bands measure documented example volume only—not execution frequency, accuracy, quality, traffic, freshness, or conversion:

- Level 0 — No verified examples: 0
- Level 1 — Emerging: 1–2
- Level 2 — Supported: 3–5
- Level 3 — Strong: 6–10
- Level 4 — Deep: 11+

Keep breadth separate from volume. `priorityCoverage` is the importance-weighted share of mapped task slugs that have at least one verified meta-article; it remains unknown when source records do not name the task slugs they prove.

---

## Every execution feeds the next one

Write the meta article for every real execution. A meta article documents what actually happened in one run; a definitive task article is the reusable recipe. Link both ways through the exact task slug. The meta article identifies the starting state, recipe revision, actual inputs and decisions, output and check evidence, failures, lessons, next owner and handoff. Private or draft publication states remain explicit. Review a proposed lesson before changing the canonical recipe or runnable skill; the next real execution checks that revised method.

`build/task-executions.json` records unique executions under [EXECUTION-LEDGER.md](EXECUTION-LEDGER.md). It is additive to the existing registry, not a second task index. The public UI distinguishes recorded completed runs, failures and unknown history from dated meta-article volume. An untracked execution frequency is **unknown**, never zero. Revisions and derivative articles do not create runs. Internal checks and agent contributions stay part of the parent execution; a separately scoped and documented child execution may have its own ID with `parentExecutionId`, and never increments the parent task's count unless it actually executes that recipe independently.

The `before`/`after` dashboard station suggestions are generated neighbors, not source-verified prerequisites. Label actual prerequisite, input reference, companion, child and downstream links by their real role and condition. Do not expand every task under a referenced hub into a prerequisite list.


## Status legend (matches the dashboard)
- **Complete (Green)** — the individual task's SOP/skill is complete and mapped; this task-level status does not by itself certify a shared article hub. A shared article is labeled definitive only when every task mapped to that normalized URL is Complete and no reviewed semantic-certification hold remains.
- **Needs Work (Yellow)** — a page exists but misses ≥1 requirement, or has no skill.md / no example yet.
- **Gap (Red)** — no definitive article yet; skill.md is authored from the task definition and flags the missing hub.
