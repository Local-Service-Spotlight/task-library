---
name: run-content-factory-on-any-engine
description: Run the whole Content Factory — Produce → Process → Post → Promote — on whichever engine you have. Claude-only and Grok-only are first-class. Multi-engine is optional sophistication, not a second playbook.
category: Strategy & Measurement
stage: —
definitive_article: /content-factory
status: complete
---

# Run the Content Factory on any engine

**Use this when** you are about to process a recording (or a backlog of recordings) and need the line, the handoff files, and the model routing — including the case where the operator only has Grok, or only has Claude.

This is the operating system for the Task Library. Every other Content Factory skill is a station on this line. Do not start a station as if it were a standalone chat.

## Inputs
- One raw recording (or a batch in the Content Library) plus the client's positioning and hub URLs
- Access register for the destination site (GSC, GA4, GTM, Meta pixel, WP application password) — run the Gate skills first if any ID is missing
- One engine the operator actually has: Claude, ChatGPT, Grok, or a local Qwen. Not a wishlist.

## The line (never skip a phase)

1. **Gate / Plumbing** — pixels, GTM, GA4, GSC, Meta Business Manager, domain. A Dollar-a-Day campaign with no pixel is spend you cannot retarget. See `install-meta-pixel-with-standard-events` and `verify-google-search-console-and-connect-to-ga4`.
2. **Produce (gather)** — Topic Wheel questions, one-minute videos, conference clips, a 50-clip batch. Human on camera. Agent preps the list and logs the files.
3. **Process (Descript)** — upload → transcribe → filler pass → GCT → article from transcript → Jennifer grade → clips → ad creatives. This is where a local model can take the overnight writing slice.
4. **Post** — WordPress draft with the *owner* as author, Rank Math, SEO Tree, YouTube, Facebook, LinkedIn. The live URL is the handoff, not the chat.
5. **Promote (ads)** — boost only proven organic. $1/day × 7, kill the bottom 90%, $30 over 30 days on winners. Highest money on the line.

Map to the public 4 P's without forking the playbook: **Plumbing = Gate**, **Publish = Produce+Process+Post**, **Promote = Promote**, **Perform = MAA** (`maa-cycle-metrics-analysis-action`). The 6-stage assembly line (capture → transcribe → hub → atomize → distribute → boost) is the same line with finer Process grains.

## Single-engine path (first-class)

People who arrive with ONLY Grok, or ONLY Claude, still execute the whole factory.

1. Open this skill. Confirm the Gate IDs exist. If not, run the Gate skills in this same engine with a browser.
2. Produce: human records; you log files into `01-Raw/`.
3. Process: you drive Descript (browser) and write `transcript.md`, `gct.md`, `article.html` in the client folder. If the engine cannot talk to Descript, export the transcript from Descript once and keep working from the file.
4. Grade with Jennifer in the same engine (`grade-article-using-jennifer`). A- is the publish bar — do not iterate past it.
5. Post via WordPress REST with a full Chrome User-Agent (BlitzMetrics WAF 403s a minimal UA) or via wp-admin if REST is blocked.
6. Promote in Meta Ads Manager (browser). Same engine. Same kill/scale rules.

Do not wait for a second vendor. Do not keep a "Claude version" and a "Grok version" of this SOP.

## Optional multi-engine (same line, more throughput)

- **Tier 0 / script:** yt-dlp, WP REST, sitemap checks, zip builds. No model.
- **Tier 1 / local:** overnight Qwen (`run-overnight-local-writer`) drafts Process writing. It never hits YouTube, WordPress, or ads.
- **Tier 1 / any chat model:** social copy, title options, clip-selection lists.
- **Tier 2 / judgment:** Jennifer, entity disambiguation, the subject's voice. Claude, ChatGPT, or Grok — whichever you have that clears the bar.
- **Computer-use:** Descript, Ads Manager, GSC, GTM. Any engine with a browser.

That split is how you scale the SAME factory when you have extra engines. It is not a second playbook.

## Handoff packets (files, never vendor memory)

| From | Write these files | Next skill reads |
|---|---|---|
| Gate | Access register row: GTM-ID, G-ID, pixel ID, GSC property | Every later skill |
| Produce | `01-Raw/YYYY-MM-DD-*.mp4` + tracker row | `step-1-upload-video-to-google-drive-and-descript` |
| Process | `transcript.md`, `gct.md`, `article.html`, `clips/`, `04-Promote-Creatives/` | `step-12-post-article-on-wordpress` |
| Post | Live URL, post ID, author user, featured-image media ID | Promote ranking |
| Promote | Organic metrics + kill/scale log + pixel ID | Next week's five |

If the work only exists in a chat thread, the next engine (or the next person) starts from zero. That is how factories stall.

## Steps
1. Check Gate IDs. Stop and run plumbing if GSC, GTM, GA4, or the Meta pixel is missing — this is a 5 even though the task is small.
2. Confirm there is raw media in `01-Raw/` or record it (`record-one-minute-videos` / `batch-record-50-raw-clips-in-one-session`).
3. Run Process in order: Descript transcription → GCT → article → Jennifer (stop at A-) → clips → Dollar-a-Day creatives.
4. Post to WordPress as a draft, set the owner as author, then the Rank Math / SEO Tree / checklist skills. Publish only when the checklist is green.
5. Wait for organic signal. Rank the last 60–90 days. Boost the top 5 at $1/day for 7 days. Kill the bottom 90%. Scale winners.
6. Write the meta-article for the run so the next recording starts from a sharper SOP.

## Definition of done (QA checklist)
- [ ] Gate IDs recorded (GTM, GA4, GSC, pixel) or an explicit blocker named with the Gate skill to run
- [ ] Files exist on disk for every completed phase — not only in a chat
- [ ] Article graded to A- (or the run is still in Process with the grade attached)
- [ ] Live URL exists before any dollar is spent
- [ ] Boosts, if any, are on proven organic only, $1/day, with a day-7 kill date
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Overnight local writer SOP: https://blitzmetrics.com/overnight-content-worker/ — Qwen drafts; a human (or Claude/Grok) does the morning voice pass; scripts post drafts. Promote stays a separate station.
- Marko Sipila / HVAC Quote: phone-shot conference interviews → YouTube → $1/day on winners. That is this line with no second vendor required.
- Anthony Hilb (July 2026): 16 articles shipped to a site with no GSC. Six never indexed. The Gate was skipped; the factory looked busy and produced nothing measurable. See `verify-google-search-console-and-connect-to-ga4`.

## Definitive article & links
- Hub: /content-factory
- Related: /dad · /blog-posting-guidelines · /overnight-content-worker · /digital-plumbing · /model-judgment
- Sibling skills, in run order: `verify-google-search-console-and-connect-to-ga4` → `step-1-upload-video-to-google-drive-and-descript` → `grade-article-using-jennifer` → `step-12-post-article-on-wordpress` → `run-dollar-a-day-campaign-on-winning-content`
