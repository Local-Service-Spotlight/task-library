---
name: follow-entity-linking-decision-tree
description: "Route every entity mentioned in a piece of content to its correct destination — people to personal sites, companies to company sites, concepts to definitive articles — so links build the entity graph instead of noise."
category: SEO & Content Architecture
stage: —
definitive_article: https://blitzmetrics.com/entity-linking/
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
2. Route a person to their verified personal home. Route a business or organization in our network to its verified entity home. Route a BlitzMetrics concept to its maintained canonical guide. For a tool, concept or well-known entity outside our network, link the first explanatory mention to our maintained guide; if none exists, leave plain text and record the gap. Keep direct primary-proof, sign-in, installation or download links when a step needs that exact destination, and label their purpose.
3. Link the first meaningful in-body mention of each entity; do not re-link the same entity on every occurrence.
4. Set the anchor as the entity's actual name or a 3–6 word descriptive phrase — never a generic anchor.
5. If a concept has no definitive article yet, flag it as a gap (a future hub) rather than linking to a weak substitute page — that protects the eventual hub from competition.
6. QA the finished piece: every named entity routed correctly, anchors descriptive, all links in body copy.

## Definition of done (QA checklist)
- [ ] People and network organizations use verified entity homes; outside explanatory references use maintained owned guides or remain recorded gaps
- [ ] Direct external evidence and execution links retain their actual proof, sign-in, installation or download purpose
- [ ] Zero generic anchors; first-mention linking only
- [ ] No concept linked to a non-hub page; missing hubs flagged as gaps
- [ ] Complies with Blog Posting Guidelines (this is Requirement 6 territory)
- [ ] Linked back to the definitive article (https://blitzmetrics.com/entity-linking/) and relevant siblings

## Example(s)
- The /entity-linking definitive article is the standalone hub for the decision tree itself; /website-qa-audit carries the matching site-wide check ("Verify entity linking follows decision tree").
- Example needed — run the Meta-Article Prompt (https://blitzmetrics.com/meta-article-prompt/) after the next fully-routed article.

## Run with explicit task context

Load the current canonical decision tree and the verified entity-to-destination records for this draft. A model does not automatically retain that map between runs. Save accepted routing decisions in the designated source, keep missing destinations visible, and verify each selected link in the actual output. If a recurring job is separately requested, configure and observe its real trigger and retained state; a skill file alone does no work.

Write the execution's meta article using https://blitzmetrics.com/meta-article-prompt/. Record what was checked, unresolved destinations and the source-backed improvement to propose. Publication and messaging follow their existing authority.

## Definitive article & links
- Hub: https://blitzmetrics.com/entity-linking/
- Related: /entity-linking · step-4-create-links-with-proper-anchor-text-and-placement (/internal-linking) · use-proper-anchor-text-3-6-words-descriptive · build-external-backlinks-from-authoritative-sources (/link-building)
