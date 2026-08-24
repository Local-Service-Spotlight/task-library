---
name: email-and-dm-client-about-published-article
description: Notify the client by email and direct message that their article is live (Step 15), with the links and a specific ask that turns them into the first amplifier.
category: Content Factory — Post
stage: Post
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Email and DM client about published article

**Use this when** the client's article has just gone live — Step 15 of the Blog Posting process; notification happens the same day as publication.

## Inputs
- Live article URL, headline, and distribution links (YouTube, Facebook, LinkedIn)
- Client's email address and the channel where you actually talk (Messenger, LinkedIn DM, text, Slack)
- The original customer question or video the article came from

## Steps
1. Send the **email** (the record): subject "Your article is live: <title>". Body: the link, two sentences on what it covers and where it sits on their site's SEO Tree, and what happens next (distribution done, promotion starting).
2. Make one **specific ask** in the email: share it to your network, comment on the Facebook/LinkedIn posts, and send it to the customer who originally asked the question — their share is the first organic amplification signal.
3. Send the **DM** (the attention): a short personal note on the channel the client actually checks — "Your article on <topic> just went live: <link>. Took a screenshot of my favorite line — would love your comment on the post."
4. Include the social post links in one of the messages so the client can engage natively rather than hunting for them.
5. Log the notification (date, channels) in the tracker; if the client hasn't responded in 48 hours, follow up once on the DM channel.
6. When the client replies happy, capture it: their reaction is testimonial raw material and a Thank You Machine trigger.

## Definition of done (QA checklist)
- [ ] Email sent with live link, context, and a specific share/comment ask
- [ ] DM sent on the client's real channel the same day
- [ ] Social post links included; notification logged; 48-hour follow-up scheduled
- [ ] Client response captured (testimonial / Thank You Machine trigger if positive)
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run. Candidate: notifying Marko Sipila (HVAC Quote) that his customer-question article is live and logging his share.

## Run on a persistent agent (Fable 5)
A persistent agent (Fable 5, or a comparable OpenAI/Google model) sends the email and DM same-day from the publication record in memory, then keeps the task alive across the 48-hour window — following up, capturing the client's reply, and triggering the Thank You Machine on a positive response — because the Definition of done includes those later boxes, not just "messages sent."
It remembers each client's real channel and past response pattern, so every notification lands better than the last.
Each run logs a meta-article example so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/
- Related: /thank-you-machine (positive replies trigger gratitude videos) · /content-factory
- Run order (Post stage): distribution posts live → **email-and-dm-client-about-published-article** (Step 15) → share-in-44k-facebook-group (Step 16)
