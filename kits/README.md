# Phone kits

Phone kits are single pages that a QR code in a printed audit or slide points to. Each one turns a finished Task Library method into buttons a business owner can tap on a phone: open an AI app with the job already typed in, copy a setup message, or install an app.

They are published from `dashboard/kits/<slug>/index.html` by the normal Build & deploy workflow, so they live at:

| Kit | Public URL | Printed in |
|---|---|---|
| Sam DeMaio's agents | https://local-service-spotlight.github.io/task-library/kits/sam/ | Sam DeMaio Personal Brand Audit v1.2, page 20 (QR) |
| Run this audit on your own brand | https://local-service-spotlight.github.io/task-library/kits/audit/ | Sam DeMaio Personal Brand Audit v1.2, page 19 (QR); stage handout |

## Rules for kit pages

- **QR destinations are permanent.** A printed PDF cannot be edited. Never move or delete a kit without leaving a page at the old path that sends people to the new one.
- **Public-safe only.** A kit may name a client and use facts the client already publishes. It never carries private Basecamp details, revenue, contact details for staff, credentials, or anything from a private source.
- **`noindex`.** Kits are QR destinations, not search pages. They must not compete with the hub articles on blitzmetrics.com or localservicespotlight.com.
- **No tracking, no storage.** A prompt leaves the phone only when the person taps a button, and then only to the app they chose.
- **Prompts stay under 2,000 characters** before URL encoding so `claude.ai/new?q=` and `chatgpt.com/?q=` links work on every phone.
- **Test before merge** at a 390 px phone width with an iPhone and an Android user agent: no sideways scrolling, every button has a working link, copy buttons put the exact text on the clipboard, and the empty-name check on the audit kit works.

## Sources behind the app choices (checked 2026-10-07)

- Muse from Meta: free to start with weekly limits, US only, keeps working after the app closes and asks before sending or buying. [Meta announcement](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/), [App Store](https://apps.apple.com/us/app/muse-from-meta/id6760173601), [Google Play](https://play.google.com/store/apps/details?id=com.facebook.aura).
- ChatGPT dots: need ChatGPT Pro or Business Premium and must be created on a computer; after that you can message the dot from the phone app. [OpenAI help](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot).
- Prefilled prompt links: `https://claude.ai/new?q=` and `https://chatgpt.com/?q=` open a new chat with the text filled in.
