---
name: how-to-inventory-a-podcast-on-youtube
description: Build and verify a five-tab inventory of every podcast-format video, guest, cross-platform appearance, and repurposing opportunity connected to a YouTube channel.
category: Content Factory — Process
stage: Process
definitive_article: https://blitzmetrics.com/how-to-inventory-a-podcast-on-youtube/
status: complete
---

# How to inventory a podcast on YouTube

**Use this when** a client or personal brand has podcast, interview, or conversation content on YouTube that must be cataloged before the Content Factory can repurpose it.

## Inputs
- The YouTube channel URL, using its handle or channel ID
- The host's canonical full name and any known name variations
- Known podcast or interview-series names on the channel
- Any client-specific instructions, plus access to existing inventory records if they exist

## Tools
- YouTube in a browser, with access to the channel's Playlists, Videos, Live, and channel-search views
- The five-tab [Podcast Inventory Template](https://blitzmetrics.com/wp-content/uploads/2026/08/podcast-inventory-template.xlsx), copied into a client-owned Google Sheet
- Listen Notes and Podchaser for cross-platform discovery
- Browser search, and ChatGPT or Claude with web search for gap-filling that can be independently verified
- YouTube's transcript viewer or Descript; the live SOP also uses a timestamp-removal tool and a word counter

## Steps
1. Create a separate inventory sheet for the client or person. Add five tabs named `Playlists`, `All Episodes`, `Cross-Platform`, `Guests`, and `Summary`; do not bury this inventory as a tab in an unrelated sheet.
2. Map every channel playlist. Record playlist name, video count, URL, and content type (`Interview`, `Solo`, `Training`, or `Mixed`). Flag podcast-format collections indicated by words such as “show,” “podcast,” “interview,” or “with,” guest names, or videos longer than 15 minutes with multiple speakers.
3. Work through each flagged playlist and add every episode to `All Episodes`. Capture episode number when present, title, duration, views, upload date, YouTube URL, guest, series name, and notes. Use an individual video page or the YouTube Data API only when an exact date is required; do not convert a relative date by guessing.
4. Find conversation videos outside playlists. Run at least ten channel searches, including `interview`, `with`, `podcast`, `episode`, `show`, `guest`, `Dr`, `CEO`, and known guest names, then inspect the Live tab. Add only URLs not already in `All Episodes`.
5. Identify every guest from the title, expanded description, thumbnail, or spoken introduction. Mark solo videos `Solo — [Host Name]`; list every person on multi-guest episodes. If identity remains ambiguous, flag the row for review instead of choosing a person.
6. Research each unique guest using exact-name and company searches. Record LinkedIn, X/Twitter, company, title, and personal or brand website when verified. Enter `n/a` or `No account found` when a profile cannot be found; never manufacture a URL.
7. Run the cross-platform sweep: search the host's quoted name in Listen Notes, search Podchaser, search YouTube globally for the host as a guest, check the host's website or podcast page, and use web-enabled AI only to surface leads. Put results in `Cross-Platform`, record the source URL, and verify each lead before treating it as an appearance.
8. Enrich the inventory. For every episode, calculate views per day from its actual view count and upload date and check whether the quoted title appears on Google's first results page. For the top 20% by views per day, extract and clean the transcript and record its word count.
9. Populate `Guests` with one row per unique guest and links to every episode in which that person appears. Populate `Summary` with total episodes, duration, views, average views, top ten by views, top ten by views per day, unique-guest count, and content date range.
10. Reconcile the work: playlist video counts must match captured rows, every conversation must have a guest or solo label, every guest must have at least a verified LinkedIn URL or a documented exception, and duplicate YouTube URLs must equal zero.
11. Mark the top 20% `Priority Repurpose`, document audio-only/platform gaps, identify weak titles or thumbnails and inactive series, and turn `Guests` into a warm outreach list. Include the finished sheet URL plus total time, time per entry, and cost per entry in the work report.

## Definition of done (QA checklist)
- [ ] The inventory is a separate, client-named sheet with all five required tabs
- [ ] All playlists are mapped and every interview/conversation video is reconciled to playlist counts, channel searches, and the Live tab
- [ ] Every episode has the required YouTube fields; duplicate YouTube URLs equal zero
- [ ] Every conversation has a verified guest name or explicit solo label; unresolved identities are visibly flagged, not guessed
- [ ] Every unique guest has a verified LinkedIn URL or a documented `n/a` exception
- [ ] Listen Notes, Podchaser, global YouTube search, and the host's site have been cross-referenced with source URLs
- [ ] Views per day and Google page-one checks are recorded for every episode
- [ ] Transcripts and word counts are recorded for the top 20% by views per day
- [ ] The Summary totals and top-ten lists recalculate correctly from the underlying rows
- [ ] Priority-repurpose rows, platform gaps, guest outreach, and time/cost metrics are complete
- [ ] The work report includes the inventory sheet URL
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- The live SOP documents the BlitzMetrics channel inventory: 100+ conversation videos across seven playlists, then hundreds of additional cross-platform results discovered through Listen Notes and Podchaser. It demonstrates why a channel scan and an appearance scan must be reconciled rather than substituted for one another.
- The article also records inventories for Ethan Van De Hey, America First Dumpsters, Ryan D. Lee, and Dan Leibrandt as examples of the same method across personal-brand and niche-business podcasts.

## Definitive article & links
- Hub: https://blitzmetrics.com/how-to-inventory-a-podcast-on-youtube/
- Related: https://blitzmetrics.com/how-to-inventory-every-podcast-youve-been-on-and-why-its-one-of-the-highest-roi-things-you-can-do/ · https://blitzmetrics.com/how-we-use-listen-notes-to-find-track-and-repurpose-every-podcast-appearance/ · https://blitzmetrics.com/how-we-use-podchaser-to-amplify-authority-and-repurpose-podcast-content/ · /content-factory
- Sibling skills, in run order: `set-up-content-library` → this → `how-to-inventory-every-podcast-youve-been-on-and-why-its-one-of-the-highest-roi-things-you-can-do`
