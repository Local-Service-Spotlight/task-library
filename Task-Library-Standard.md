# The BlitzMetrics Task Library Standard
### How every task becomes a definitive article + a skill.md + linked examples

**Source of truth:** [How to Create a Definitive Article for Any BlitzMetrics Concept](https://blitzmetrics.com/definitive-article-guide/) (v1.1, Apr 2026) and the [Task Library Dashboard](https://blitzmetrics.com/task-library-dashboard/).
**Purpose:** a single spec the Fable workers (and any human/agent) follow to bring every registered task up to standard — each one documented, downloadable as a skill, and wired into the SEO Tree. Counts are always derived from the registry/build; never type a task or article count into copy.

---

## The model: three artifacts per concept
Every concept/task in the library targets **three linked artifacts**, and they point at each other. A missing or incomplete artifact stays visibly in progress; a URL mapping alone never makes a page definitive.

1. **Article hub** — the one canonical page that owns the concept. It becomes a **definitive article** only after the Green/ready validation below. It lives at a stable URL on the approved canonical domain for that concept (for example, `blitzmetrics.com` or `localservicespotlight.com`). Declare one working copy; an older-domain page may remain as an archive, but do not map tasks to a replacement until the working copy has content parity and passes validation.
2. **skill.md** — the machine-readable SOP an AI agent runs to *do* the task. Downloadable, one file per task. References its mapped article hub, or explicitly records a GAP.
3. **Examples / meta-articles** — real proof the task was done, each documented with the Meta-Article Prompt and linking back up to the article hub.

> Relationship (one direction up): **examples / meta-articles → article hub → course/service**, and a ready definitive hub links **across** to related definitive articles. Never publish a second page that competes with a hub (that's "content vandalism").

---

## The Nine Requirements of a Definitive Article
A page is only "definitive" if it meets **all nine**. Miss one and it's a draft (Yellow), not done (Green).

1. **Clear definition in the first two paragraphs** — what it is, what it is *not*, who it's for. Plain language, no unexplained jargon.
2. **The complete process / framework** — the full SOP, every stage/step/checklist. Detailed enough to follow without further instruction.
3. **Lots of real examples** — link *every* example that exists, not three or five. Each with a 1–2 sentence note on why it's relevant.
4. **Links to related concepts and entities** — cross-link the other definitive articles and route named people, companies, tools, and concepts through the Entity Destination Rules below (builds the entity graph).
5. **Links to the course/guide/service** — as a CTA near the bottom, not as the core content.
6. **Compliance with Blog Posting Guidelines** — title <60 chars; meta description <160; primary keyword in first paragraph; H2/H3 structure; short paragraphs; active voice; no AI-fluff phrases; no stock images; entity-linking decision tree for internal links.
7. **A short URL** — memorable redirect (e.g., `/dad`, `/digital-plumbing`) pointing to the hub, not the homepage or a case study.
8. **Article-specific lead visual, then task-specific framework context near the top** — after the 2–3 sentence opening summary, lead with real visual evidence specific to the article: its workflow, source screenshot, task diagram, result, or canonical diagram when the article itself teaches that framework. If the task belongs to a larger approved framework, place the full canonical framework diagram immediately after that lead visual, still near the top, and outline, shade, or recolor only the task's honest sub-components while leaving the rest visible for context. For a Content Factory task, this context map is the full canonical Content Factory diagram. The framework map is orientation, not generic hero art: it must not displace the article's primary evidence or imply components the task does not use. Make applicable nodes link to their section or sub-concept hub, add descriptive alt text and a caption naming where this task fits, and verify both visuals on desktop and mobile. If no multi-part framework applies, do not force a generic Content Factory diagram; keep the real, relevant lead visual.
9. **Third-party endorsements / testimonials / E-E-A-T** — media, conference talks, podcasts, practitioner testimonials with proof. Highest-authority first; volume matters. (The `/dad` article is the gold standard.)

---

## Entity Destination Rules
Apply this decision tree to the **first useful mention only**, with descriptive 3–6 word anchor text. Do not link the same entity repeatedly in one article.

1. **Person with a verified personal-brand site** → that person's own site. Example: Dennis Yu points to `dennisyu.com`, not a WordPress author archive.
2. **Company or organization** → its verified official site.
3. **Tool, platform, or method with a BlitzMetrics training article** → the internal hands-on article that teaches the task. The official product site may be linked separately at the execution step where the reader must open the tool; it does not replace our training link in explanatory copy.
4. **Named entity without a verified home or relevant internal article** → plain text until verified. Never guess a domain, personal site, or destination.

These links exist to help the reader identify the entity and complete the task. They are not decorative SEO links.

---

## When a page may display “Definitive”
The visible label is a validation result, not a writing style or a manually chosen badge.

- The build groups tasks by normalized article URL. A hub is `ready` only when **every task mapped to that URL is `complete`**. One `needs-work` or `gap` task keeps the entire hub `wip`; a missing article mapping is excluded from article counts.
- Only a `ready` hub may show the consistent **Definitive article** / **Definitive SOP** marker near the top of the page and the **Definitive article ↗** label in the Task Library.
- A `wip` hub must show **Article in progress** where a status label is useful. It must not carry a green/definitive badge merely because the page is published or mapped.
- Re-run live page QA before promotion: the build state is the catalog receipt, while rendered content, links, diagram placement, schema, and mobile layout are the publication receipt.

---

## The 10-Step Creation Process
Run in order for any task in a Yellow/Red (Needs Work / Gap) state:

1. **Identify the concept** and find every existing article that mentions it (the hub organizes them, doesn't replace them).
2. **Write the definition** (2 paragraphs; model on `/dad`).
3. **Document the process/framework** (the SOP — this is what the skill.md mirrors).
4. **Link every example** (1–2 sentences each).
5. **Cross-link related concepts and entities** using the Entity Destination Rules (other definitive articles, verified personal sites, verified company sites, and internal training for tools).
6. **Link to the course/service** (CTA).
7. **Set the short URL** (redirect to the hub).
8. **Add the article-specific lead visual, then any applicable canonical framework map** near the top; highlight only the task's honest sub-components without removing surrounding system context, and do not force generic framework art onto an unrelated task.
9. **Add E-E-A-T** (endorsements, testimonials, media — highest authority first).
10. **Publish, validate the ready/WIP state, then run the Meta-Article Prompt** to create the companion meta-article that documents how it was built. Add the visible Definitive marker only after the URL-level ready gate passes.

---

## Where definitive articles live in WordPress
- Published as a **Post** (not a Page).
- Assigned to the **Definitive Articles** category only after the URL-level hub is `ready`. A published WIP article stays in its operating/topic category and is not taxonomically presented as definitive.
- Carries the canonical Task Library category or categories represented by its mapped tasks, using names from `build/categories.json`; do not invent a near-duplicate category. Each task has exactly one library category, but a shared hub may represent several.
- Tagged with every **Content Factory stage** represented by its mapped tasks (`Stage: Produce | Process | Post | Promote`) and no others, plus the smallest useful set of existing cross-cutting **Topic:** tags. A hub with no task in the four phases omits the Stage tag. Reuse canonical tag slugs; do not create spelling, punctuation, singular/plural, or capitalization variants.
- The category, stage, article URL, and task status must agree with the corresponding `skill.md` frontmatter and registry entry. This lets agents query the REST API without translating competing taxonomies.
- Authored in the **standard block editor (Gutenberg)** — **not Cornerstone** or any proprietary builder (builder content is opaque to AI agents and hard to update programmatically).

---

## The skill.md standard (one file per task)
Every task gets a `skill.md` an agent can run. House format — keep it tight, SOP-grade, and grounded in the definitive article:

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

## Steps
1. <imperative, concrete step>
2. ...
   (Mirror the definitive article's process exactly; this section IS the SOP.)

## Definition of done (QA checklist)
- [ ] <objective, checkable pass criteria — what "good" looks like>
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

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
"Lots of real examples" (Requirement 3) is satisfied by **meta-articles** — each documents one real run of the task via the Meta-Article Prompt and links back to the definitive article. A task is fully "Green" when its definitive article exists, its skill.md is published, and it has at least one linked example/meta-article. The `/meta-article-prompt-template` (29 linked examples) and `/internal-linking` ("includes skill file for AI agents") are the models to copy.

---

## Status legend (matches the dashboard)
- **Complete (Green)** — the task's article exists and meets all nine requirements; skill.md present; ≥1 example. A shared article is labeled definitive only when every task mapped to that normalized URL is Complete.
- **Needs Work (Yellow)** — a page exists but misses ≥1 requirement, or has no skill.md / no example yet.
- **Gap (Red)** — no definitive article yet; skill.md is authored from the task definition and flags the missing hub.
