---
name: run-overnight-local-writer
description: Take Blog Posting Guidelines steps 4–7 and 11 off Claude and run them overnight on a Mac with a local model and a shared job queue.
category: Content Factory — Post
stage: Post
definitive_article: /overnight-content-worker
status: complete
---

# Run overnight local writer

**Use this when** a client backlog would burn frontier tokens if one chat wrote every draft, and a teammate can leave a laptop on overnight.

## Inputs
- Client folder under `Overnight-Content-Worker/clients/`
- Queue file `queue/QUEUE.json`
- Local Qwen with thinking off (or `--dry-run`)

## Steps
1. Confirm you are Accountable for that client, or Accountable said yes.
2. Run `status.py`. If the client lock is held, pick another client.
3. Dinner, then night, then stop. Do not publish live from the Mac worker.
4. Morning QA is two minutes per article: voice, links, featured image.
5. `morning.py` POSTs drafts. Rank Math click-path stays human when REST cannot set it.
6. Hand the draft URLs to `grade-article-using-jennifer`, then `step-12-post-article-on-wordpress` if they are not already drafted. Promote stays a later station.

## Definition of done (QA checklist)
- [ ] Client lock shows your worker
- [ ] No duplicate job_id in `claimed` by two workers
- [ ] Drafts are markdown with YAML, not live posts
- [ ] `needs_human` rows are in the morning pile, not silently skipped
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Public SOP: https://blitzmetrics.com/overnight-content-worker/ — local Qwen drafts; the local model never hits YouTube or WordPress. Same collision rule as Dennis OS "In flight."

## Definitive article & links
- Hub: /overnight-content-worker
- Related: /blog-posting-guidelines · /content-factory · /application-passwords
- Sibling skills, in run order: `step-4-research-edit-add-timestamps-and-outline` → this → `grade-article-using-jennifer`
