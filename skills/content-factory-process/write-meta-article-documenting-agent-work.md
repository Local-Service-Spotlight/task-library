---
name: write-meta-article-documenting-agent-work
description: Use the Meta-Article Prompt Template to document a real AI-agent task run as a publishable article — the proof layer that turns work into examples.
category: Content Factory — Process
stage: Process
definitive_article: /meta-article-prompt/
status: complete
---

# Write meta-article documenting agent work

**Use this when** an AI agent (or human + agent) has just completed a real task run — any Task Library skill execution — and the run should become a linked example for its definitive article.

## Inputs
- The completed run: prompts used, tool outputs, before/after states, final deliverable
- The Meta-Article Prompt Template (the hub at /meta-article-prompt/)
- The task's definitive article short URL (the hub this example will link up to)
- WordPress access for publishing per Blog Posting Guidelines

## Steps
1. Gather the artifacts of the run while fresh: the exact prompts, key decisions, screenshots of before/after, the output, time taken, and anything that went wrong.
2. Run the Meta-Article Prompt against those artifacts to draft the article: what the task was, why it was run, what the agent actually did step by step, and what resulted.
3. Show the real work — include the actual prompts and honest friction points. The value is reproducibility, not a polished success story.
4. State results concretely: what shipped, what changed, what was measured (feed numbers into MAA where they exist).
5. Link the meta-article UP to its definitive article (one direction: example → hub). Never write the meta-article as a competing explanation of the concept — that is content vandalism; it documents one run.
6. Apply the entity-linking decision tree for every person, company, and concept mentioned.
7. Publish per the Blog Posting Guidelines pipeline (title <60, meta <160, keyword in first paragraph, real screenshots as images, RankMath 70+ at the Post stage).
8. Register the example: add it to the definitive article's examples section and the Task Library tracker — this is what moves a task toward Green (article + skill + ≥1 example).

## Definition of done (QA checklist)
- [ ] Documents one real run with actual prompts and honest results — no hypotheticals
- [ ] Links up to the task's definitive article; does not compete with the hub
- [ ] Concrete outcomes stated (deliverable, metrics, time)
- [ ] Complies with Blog Posting Guidelines (it publishes content)
- [ ] Example registered on the hub's examples list and in the tracker
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- The hub at /meta-article-prompt/ carries 29 linked example meta-articles — the largest example set in the library and the model for this loop.

## Run on a persistent agent (Fable 5)

This task is the compounding mechanism itself: a persistent agent (Claude Fable 5, or comparable long-horizon OpenAI/Google models) runs it automatically at the end of every other skill run, while the exact prompts, friction points, and results are still in working memory. It loops until the example is published per Blog Posting Guidelines and registered on the hub and tracker — an unregistered example fails the Definition of done. Every pass adds one more linked example, which is exactly how the library compounds run over run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /meta-article-prompt/
- Related: /blog-posting-guidelines (publishing pipeline), /internal-linking (its hub ships a skill file — a documented precedent), /knowledge-system-maintenance (capture loop)
- Sibling skills, in run order: any completed task run → this → `step-12-post-article-on-wordpress` (Post stage)
