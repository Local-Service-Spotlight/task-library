---
name: keep-speaker-bureau-profile-bookable
description: Keep the speaker kit, bureau profile, and speaking page in sync so organizers can book the person from published fees, talks, and proof — without a scavenger hunt.
category: Personal Branding
stage: —
definitive_article: /speaker-kit
status: needs-work
---

# Keep speaker bureau profile bookable

**Use this when** a personal brand is taking paid stages (keynotes, workshops, campus talks) and the bureau profile, speaker page, or one-sheet is empty, stale, or still carrying a retired brand.

## Inputs
- Canonical speaker kit in git (example: https://github.com/dennisyu/dennis-yu-speaking) with positioning, bios, fees, programs, testimonials, stages, and media
- Live bureau login (for NSA members this is often eSpeakers; speaker ID and dashboard URL live in the kit, not in this skill)
- Live speaker page on the personal-name domain (example: https://dennisyu.com/speaking/)
- Inquiry path the organizer can submit without emailing a private inbox
- Fees the human has set — never invent a number

## Steps
1. **Read the kit before touching any public form.** Positioning, fees, talk titles, bios, and brand name come from the kit. If the kit and the live page disagree, the kit wins until a human changes the kit.
2. **Lock the brand.** Lead with the current operating company. Retired brands (BlitzMetrics, a Content Factory typo, an old domain) stay as prior-history only. Do not put a street address or private phone on a public bureau profile.
3. **Publish fees.** Bureau profiles that say “inquire” lose search rank and look unfinished. Write the U.S., international, and virtual numbers exactly as the kit states them, plus travel billed separately.
4. **Load programs from the kit, not from memory.** Each talk needs a title, format (keynote / workshop / campus), audience, description, and takeaways. Industry rooms (funeral homes, landscapers, campuses, affiliates) get their own program, not one generic “AI talk.”
5. **Fill bio, audience benefit, and one-liner from the kit files.** Short bio for cards; full bio for the profile. First person on the personal site; third person on bureau directories unless the bureau requires first person.
6. **Put proof on the profile:** canonical headshot, stage photos (real, no stock), one talk video, and named testimonials with role and event. Link the speaker page, not a homepage that buries speaking.
7. **Add three future calendar holds** the organizer can see (named events with dates). Empty calendars read as inactive.
8. **Mirror the same facts on the personal-site speaking page** so Google and the bureau are not telling two stories. Then click the public bureau URL as a stranger and check: name, brand, fees, at least one program, video or photo, inquiry path.
9. **Log the run** as a meta-article that links back to /speaker-kit. Feed recordings and stage photos into `film-conference-presentations` after the gig.

## Definition of done (QA checklist)
- [ ] Public bureau profile shows current brand, published fees, ≥1 program, bio, and a link to the speaker page
- [ ] Speaker page on yourname.com matches the kit on fees, talks, and positioning
- [ ] No retired brand, typo domain, or street address in public fields
- [ ] At least one named testimonial and one real stage photo or talk video
- [ ] Three future calendar dates visible, or an explicit note in the kit that the calendar is the human’s job this week
- [ ] Inquiry path works without a private email
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Dennis Yu speaker kit — https://github.com/dennisyu/dennis-yu-speaking — the source of truth this skill reads: fees, seven programs, bios, eSpeakers field map.
- eSpeakers public profile — https://www.espeakers.com/marketplace/profile/48283 — the bureau surface the monthly eSEO mail grades (fees, programs, calendar).
- dennisyu.com/speaking — the entity-home speaking page the bureau and Google should both point at.
- Conference inventory — https://blitzmetrics.com/dennis-yu-conference-speaking-appearances/ — 277+ verified appearances used as proof, not as the booking page.

## Run on a persistent agent (Fable 5)
A persistent agent (Claude Fable 5 or a comparable OpenAI/Google model) treats the kit as memory: it diffs the live bureau profile and speaker page against the kit, writes only what the kit authorizes, and loops until the Definition of done passes — not 90%. It never invents a fee or a talk title. After each booked gig it files the recording and stage photos for the Content Factory and logs a meta-article example so the next agent does not start from a blank profile.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /speaker-kit
- Related: /personal-brand · /content-factory · /digital-plumbing · /one-minute-video-guide
- Sibling skills, in run order: `build-personal-brand-website` → `add-consistent-headshots-and-bios-across-profiles` → **this** → `secure-guest-appearances-and-speaking-engagements` → `film-conference-presentations` → `build-third-party-validation`
