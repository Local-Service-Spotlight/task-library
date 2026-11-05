# QA checklist: 18 x 24 in personal brand poster

Use this before anything goes to print. `render_poster.py` checks the items marked **(auto)** on every render and refuses or fails when they do not pass. The rest need a person, or an agent that did not build the poster, looking at the actual file.

## Facts

- [ ] Every printed name, number, date and title has a row in `facts.csv` with a source a stranger can open and the date it was checked. **(auto)**
- [ ] Company claims and your own counts sit in separate, labeled places: "COMPANY · AS PUBLISHED" and "NAME · ON THE PUBLIC RECORD". **(auto: claim_owner required)**
- [ ] Counts are de-duplicated. One episode posted as audio and as video counts once, and a one-minute clip is not an interview.
- [ ] Job titles and employers match the subject's own About page. If another page disagrees, use the subject's own page and note the conflict.
- [ ] Results that clients reported to the subject say whose report they are, and do not read like audited case studies. **(auto: results.disclosure required)**
- [ ] Each person gets the narrowest verb the source supports ("Had her on [show name]", "Wrote the foreword to [book title]"). No friend, partner or mentor unless the source says so.
- [ ] Every quote is the exact words of a named person, with a link.
- [ ] An award, ranking or title appears only with a source that grants it. A mention from a stage is not an award.
- [ ] Names are spelled the way the person or their company spells them. When two sources differ (a nickname and a full name), ask the client's team which to print.

## Photos

- [ ] Before a photo goes on the poster, its row records who owns it and where the permission is kept. **(auto)**
- [ ] A photo found on a public post is not permission. Use the client's own photos, or get the owner's written OK. **(auto: `found-public` is refused)**
- [ ] No photos of public figures or partners pulled from the web. For a photo of the client with someone else, ask the client's team for one they own.
- [ ] Each row names the exact file you downloaded (`source_file_url`) and its original pixel width (`native_px_w`).
- [ ] Resolution at printed size, counted on the original pixels: 150 ppi or more passes, 100 to 149 is a warning (fine from about 3 ft; ask for a bigger original), under 100 fails. Enlarging a small file does not add detail. **(auto)**

## Layout and type

- [ ] Every tag that opens also closes. One stray `</div>` can move a whole section. **(auto)**
- [ ] No text under 9 pt. **(auto)** Read anything under 10.5 pt that is not fine print at arm's length on a 100% view.
- [ ] No text closer than 0.25 in to the trim edge **(auto: fail)**; keep 0.5 in for a framed poster, because the frame lip and mat cover the edge **(auto: warning)**.
- [ ] No section or text box overflows. **(auto)**
- [ ] The web fonts loaded, so nothing prints in a fallback font. **(auto)**

## Print file

- [ ] One page at exactly the print size: 18 x 24 in is 1296 x 1728 pt. **(auto)**
- [ ] All fonts embedded. **(auto)**
- [ ] The PDF title carries the version and date. **(auto)**
- [ ] Ask the printer about bleed (many ask for 0.125 in past the trim when colour runs to the edge) and colour (CMYK) before you order.

## Files and approval

- [ ] File names follow `<Subject>-<Deliverable>-18x24-v<N>-<YYYY-MM-DD>.pdf`, with the preview `<Subject>-<Deliverable>-preview-v<N>-<YYYY-MM-DD>.png`. **(auto)**
- [ ] Every new version gets a new file name, and earlier versions are kept. **(auto: the script refuses to reuse a version)**
- [ ] The client's team approves the proof (facts, names, photos) before it goes to print, and the approval is recorded.
- [ ] The run has a meta article (the record of this execution) with its execution ID, recipe revision, what changed in each version, checks, open items and next owner.
