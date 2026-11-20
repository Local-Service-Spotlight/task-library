# QA checklist: 18 x 24 in personal brand poster

Use this before anything goes to print. `render_poster.py` checks the items marked **(auto)** on every render and refuses or fails when they do not pass. The rest need a person, or an agent that did not build the poster, looking at the actual file.

Copy `facts-template.csv` to `facts.csv` and `photos-template.csv` to `photos.csv` before you fill them. Rendering needs a computer with Python 3.9+, Playwright with Chromium, pypdf, Pillow and numpy. `test_render_poster.py` checks the script itself.

## Facts

- [ ] Every printed name, number, date and title has a row in `facts.csv` with a source a stranger can open, the words the source says and the date it was checked. **(auto)**
- [ ] Status is `verified` only after someone opened the source and found those words. A page that is not live yet is `pending-release`; a final render passes it only with `--live-check`, which finds the words on the live page. **(auto)**
- [ ] No `[FILL: …]` placeholder is left anywhere on the poster. **(auto)**
- [ ] Company claims and your own counts sit in separate, labeled places: "COMPANY · AS PUBLISHED" and "NAME · ON THE PUBLIC RECORD". **(auto: claim_owner required)**
- [ ] Counts are de-duplicated. One episode posted as audio and as video counts once, and a one-minute clip is not an interview.
- [ ] Job titles and employers match the subject's own About page. If another page disagrees, use the subject's own page and note the conflict.
- [ ] Results that clients reported to the subject say whose report they are, and do not read like audited case studies. **(auto: results.disclosure required)**
- [ ] Each person gets the narrowest verb the source supports ("Had her on [show name]", "Wrote the foreword to [book title]"). No friend, partner or mentor unless the source says so.
- [ ] Every quote is the exact words of a named person, with a link.
- [ ] An award, ranking or title appears only with a source that grants it. A mention from a stage is not an award.
- [ ] A theme line is design, not a claim. It must not read like a title, nickname or award they have not used publicly.
- [ ] Names are spelled the way the person or their company spells them. When two sources differ (a nickname and a full name), ask the client's team which to print.

## Photos

- [ ] Before a photo goes on the poster, its row records who owns it and where the permission is kept. **(auto)**
- [ ] A photo found on a public post is not permission. Use the client's own photos, or get the owner's written OK. **(auto: `found-public` and `pending` are refused in a final and never placed on a draft)**
- [ ] If the right photo has no permission yet, do not print. Wait for the owner's written OK, or use a photo the client owns.
- [ ] No photos of public figures or partners pulled from the web. For a photo of the client with someone else, ask the client's team for one they own.
- [ ] Each raster photo is a camera original (`camera_original` yes, confirmed from the file's camera data), or its row gives the original file's pixel width (`native_px_w`) and the exact file you downloaded (`source_file_url`). Without one of these the script cannot tell an enlarged copy from an original. **(auto)** It also warns when a file's finest detail is missing, a sign it was enlarged. **(auto: warning)**
- [ ] Resolution at printed size, counted on the original pixels. Vistaprint recommends 240 dpi for an 18 x 24 in poster seen from 3 to 6 ft, and uses 150 dpi only for signs seen from far away. 240 ppi or more passes, 150 to 239 warns (ask for a larger original), and under 150 fails. Enlarging a small file adds no detail. **(auto)**
- [ ] No photo box would print empty. To drop a photo, mark its row `omit`; its whole block goes with it. **(auto)**

## Layout and type

- [ ] Every tag that opens also closes. One stray `</div>` can move a whole section. **(auto)**
- [ ] No text under 9 pt. **(auto)** Read anything under 10.5 pt that is not fine print at arm's length on a 100% view.
- [ ] No text within 0.5 in of the trim, because a frame lip or mat covers the edge. **(auto: a final fails inside 0.5 in; a draft fails inside 0.25 in and warns up to 0.5 in)**
- [ ] No section or text box overflows. **(auto)**
- [ ] The web fonts loaded, so nothing prints in a fallback font. **(auto)** If the PDF has Type 3 fonts, which Chromium makes from variable web fonts, render with `--offline-fonts-css` and static font files; some printers flag Type 3. **(auto: warning)**

## Print file

- [ ] One page at exactly the print size: 18 x 24 in is 1296 x 1728 pt. **(auto)**
- [ ] All fonts embedded. **(auto)**
- [ ] The PDF title carries the version and date. **(auto)**
- [ ] Bleed: ask the printer. Many ask for 0.125 in past the trim when color runs to the edge. `--bleed 0.125` writes a second PDF whose edge colors run into the bleed, with a TrimBox marking the cut. **(auto: the bleed PDF's size, TrimBox and edge colors are checked)**
- [ ] Color: the kit makes RGB files. Ask the printer whether they want CMYK and whether they convert it for you.

## Files and approval

- [ ] File names follow `<Subject>-<Deliverable>-18x24-v<N>-<YYYY-MM-DD>.pdf`, with the preview `<Subject>-<Deliverable>-preview-v<N>-<YYYY-MM-DD>.png`. **(auto)**
- [ ] Every new version gets a new file name, and earlier versions are kept. **(auto: the script refuses to reuse a version)**
- [ ] The client's team approves the proof (facts, names, photos) before it goes to print, and the approval is recorded.
- [ ] The run has a meta article (the record of this execution) with its execution ID, recipe revision, what changed in each version, checks, open items and next owner.
