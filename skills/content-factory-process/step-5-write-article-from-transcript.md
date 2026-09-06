---
name: step-5-write-article-from-transcript
description: Transform the cleaned transcript into a structured article that keeps the speaker's voice and stories while following GCT (Blog Posting Guidelines Step 5).
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 5: Write article from transcript

**Use this when** the outline, timestamps, and GCT statement are ready (Step 4 complete) and the article body needs to be drafted.

## Inputs
- The cleaned, timestamped transcript and the H2/H3 outline
- The GCT statement and the primary keyword (the customer's phrasing)
- Research notes from Step 4
- The article working doc

## Steps
1. Write INTO the outline, section by section, using the transcript as the source of truth. The video is the experience; the article is its written form — not an AI essay on the same theme.
2. Keep the speaker's voice: first person, their phrasing, their stories, their numbers. If the speaker says "we lost the first three quotes," that line survives — specificity is the E-E-A-T.
3. Never let drafting tools invent claims, statistics, or anecdotes that are not in the video or the verified research notes. Everything stated must be traceable.
4. On a personal-brand site, write as the person in first person. Show the moment, not the resume: name the real scene, what happened, what the speaker noticed or learned, and one human detail from the source. Use a small self-aware detail or honest mistake when the source supplies it; never manufacture humor.
5. Treat a famous name as context, not the point. Fail and rewrite a **trophy-name paragraph**: two or more recognizable people, brands, titles, awards, or logos packed together without a specific shared moment, relevance to the reader, and a source. One sourced story may naturally contain several people; a status list may not masquerade as a story.
6. Make relationship language no stronger than the evidence. Use exact verbs such as "interviewed," "spoke with at," "appeared on," or "worked on" when that is what the source shows. Reserve "friend," "client," "partner," "mentor," "endorsed," and "collaborated" for evidence that actually establishes that relationship.
7. Put proof in a compact receipt next to the scene: a source-linked photo, playable video, exact quote, event page, or primary record, with person, place/event, and date when known. Do not narrate the internal verification process in public copy. Confidence scores, proof-record IDs, harvesting notes, canonical-inventory language, and repurposing instructions stay in the tracker unless those systems are the article's actual topic.
8. Do not bury a true story under defensive caveats such as "this does not prove friendship" or "no endorsement is implied." Narrow or remove the unsupported claim instead. Preserve an actual legal, regulatory, or compliance disclosure when materially necessary, and keep it as short and close to the triggering claim as the requirement allows; editorial reassurance is not a compliance disclosure.
9. Publish praise only as an exact quote from a named person with the applicable role/company or city, a source link, and permission where required. A first name, initials, "happy customer," a company/domain by itself, or an unattributed paraphrase remains **HOLD** and is not rendered as a testimonial.
10. Place the primary keyword naturally in the first paragraph (the hook work in Step 7 will refine this paragraph — keyword presence is non-negotiable either way).
11. Write short paragraphs (2–4 sentences), active voice, plain language. No AI-fluff phrases — "in today's fast-paced world," "delve," "game-changer" and kin are banned by the guidelines.
12. Weave research in as support, clearly framed ("according to…"), keeping the speaker's first-hand experience as the spine.
13. Expand each section to fully answer its heading's promise — a reader landing on any H2 from search should get a complete answer.
14. Read the draft against the GCT statement: do the first 2–3 sentences make the reader's situation, reason to care, useful outcome and supporting mechanism clear, and does the body deliver that promise? Apply `step-7-write-hook-and-establish-context`; keep the source-backed moment and useful visual with the opening. Save the exact opening and quoted review evidence in the tracker. Fix or cut what fails, then hand off to `step-6-write-title-and-headings`.

## Definition of done (QA checklist)
- [ ] Every claim traces to the transcript or cited research — nothing invented
- [ ] First person, speaker's voice and stories preserved (spot-check against video)
- [ ] Proof appears as sourced scenes and compact receipts, not a resume or trophy-name paragraph
- [ ] Relationship nouns match the evidence; notable names supply context rather than status
- [ ] Zero repeated defensive caveats and zero public-facing internal scoring, inventory, or repurposing notes; any retained legal/compliance disclosure is materially required and scoped
- [ ] Every published testimonial is an exact quote from a named, attributable source; anonymous or domain-only praise is HOLD
- [ ] Primary keyword appears in the first paragraph
- [ ] Short paragraphs, active voice, zero AI-fluff phrases
- [ ] Each H2/H3 section fully answers its heading
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- Articles produced for clients like Marko Sipila (HVAC Quote) and Zach Peyton (Superior Fence & Rail) follow this transcript-first drafting method; runs are linked from https://localservicespotlight.com/article-guidelines/.
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or a comparable OpenAI/Google model that loops and holds memory) drafts section by section from the transcript, then self-audits the full Definition of done — every claim traceable, keyword in the first paragraph, zero banned fluff phrases — and rewrites until all checks pass, not until it "reads fine." Memory holds the speaker's voice patterns and the banned-phrase list from prior articles, so each draft starts closer to the standard. Log a meta-article example per run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Step 5 of the 18-step SOP)
- Related: /one-minute-video-guide (the source asset), /seo-tree
- Sibling skills, in run order: `step-4-research-edit-add-timestamps-and-outline` → this → `step-6-write-title-and-headings`
