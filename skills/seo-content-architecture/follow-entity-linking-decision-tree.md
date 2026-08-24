---
name: follow-entity-linking-decision-tree
description: "Route every entity mentioned in a piece of content to its correct destination — people to personal sites, companies to company sites, concepts to definitive articles — so links build the entity graph instead of noise."
category: SEO & Content Architecture
stage: —
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Follow entity linking decision tree

**Use this when** writing or editing any content that names people, companies, or concepts — which is every piece worth publishing.

## Inputs
- The draft, with every named entity identifiable
- The entity-linking decision tree (/entity-linking)
- Knowledge of which concepts already have definitive articles (the SEO Tree map)

## Steps
1. With the draft in hand, list every entity mentioned: people, companies, concepts and frameworks.
2. Route each by the decision tree: **person** → their personal website; **company** → the company's site; **concept** → its definitive article.
3. Link the first meaningful in-body mention of each entity; do not re-link the same entity on every occurrence.
4. Set the anchor as the entity's actual name or a 3–6 word descriptive phrase — never a generic anchor.
5. If a concept has no definitive article yet, flag it as a gap (a future hub) rather than linking to a weak substitute page — that protects the eventual hub from competition.
6. QA the finished piece: every named entity routed correctly, anchors descriptive, all links in body copy.

## Definition of done (QA checklist)
- [ ] Every entity in the piece routed per the decision tree (person / company / concept)
- [ ] Zero generic anchors; first-mention linking only
- [ ] No concept linked to a non-hub page; missing hubs flagged as gaps
- [ ] Complies with Blog Posting Guidelines (this is Requirement 6 territory)
- [ ] Linked back to the definitive article (https://localservicespotlight.com/article-guidelines/) and relevant siblings

## Example(s)
- The /entity-linking definitive article is the standalone hub for the decision tree itself; /website-qa-audit carries the matching site-wide check ("Verify entity linking follows decision tree").
- Example needed — run the Meta-Article Prompt (/meta-article-prompt-template) after the next fully-routed article.

## Run on a persistent agent (Fable 5)
A persistent agent (Claude Fable 5 or a comparable OpenAI/Google model) routes every named entity in every draft and loops until zero entities are unrouted and zero anchors generic — and where a concept has no definitive article, it logs the gap rather than settling for a weak substitute link.
Its memory grows an entity → destination table across runs, so routing gets faster, stays consistent, and the gap list feeds the gaps-to-create queue.
Each fully-routed article logs a meta-article example via /meta-article-prompt-template.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/
- Related: /entity-linking · step-4-create-links-with-proper-anchor-text-and-placement (/internal-linking) · use-proper-anchor-text-3-6-words-descriptive · build-external-backlinks-from-authoritative-sources (/link-building)
