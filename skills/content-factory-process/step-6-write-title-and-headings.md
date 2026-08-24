---
name: step-6-write-title-and-headings
description: Write an SEO title under 60 characters, a meta description under 160, and descriptive H2/H3 subheadings built on the focus keyword (Blog Posting Guidelines Step 6).
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 6: Write title and headings

**Use this when** the article body is drafted (Step 5 complete) and needs its search-facing title, meta description, and final heading pass.

## Inputs
- The drafted article and the GCT statement
- The primary/focus keyword (the customer's phrasing of the question)
- Character counter (RankMath previews these at publish time, but write to spec now)

## Steps
1. Write the SEO title: under 60 characters, containing the focus keyword, promising exactly what the article delivers. The customer's question phrasing usually beats a clever rewrite.
2. Reject clickbait and vague titles — the title must match the Content (GCT honesty test: would the video's speaker stand behind this promise?).
3. Write the meta description: under 160 characters, includes the focus keyword, states the concrete benefit of reading, written as one active-voice sentence or two short ones.
4. Pass over every H2/H3: each must be descriptive enough to stand alone in a table of contents — "How a $1/day budget gets read" beats "Budget."
5. Work the focus keyword and its natural variants into 2–3 headings where they fit honestly; never stuff every heading.
6. Verify heading hierarchy: H2s for major sections, H3s nested beneath, no skipped levels, no headings styled as bold paragraphs.
7. Confirm the H1 (post title) will be the only H1 on the page — headings start at H2 inside the body.
8. Record title and meta in the working doc header for Step 14a (RankMath), update the tracker, and hand off to `step-7-write-hook-and-establish-context`.

## Definition of done (QA checklist)
- [ ] SEO title under 60 characters with the focus keyword
- [ ] Meta description under 160 characters with the focus keyword and a concrete benefit
- [ ] Title promise matches what the article actually delivers
- [ ] Every H2/H3 is descriptive standing alone; hierarchy is clean with no skipped levels
- [ ] Title and meta recorded for the RankMath step
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- Title and heading specs are enforced on every run documented at https://localservicespotlight.com/article-guidelines/ and audited later by the Website QA Audit title/meta checks.
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

Character counts make this step machine-checkable: a persistent agent (Claude Fable 5, or comparable long-horizon OpenAI/Google models) loops title and meta drafts until the hard specs pass — under 60, under 160, keyword present, promise honest — then walks every heading for hierarchy, never stopping at "close enough." Memory recalls which title patterns worked on past runs, so each new title builds on evidence instead of taste. Close with a logged meta-article example.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Step 6 of the 18-step SOP)
- Related: /website-qa-audit (the downstream title/meta audits), /seo-tree
- Sibling skills, in run order: `step-5-write-article-from-transcript` → this → `step-7-write-hook-and-establish-context`
