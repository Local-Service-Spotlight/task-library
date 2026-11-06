#!/usr/bin/env python3
"""Render a personal brand poster to a print-ready PDF and a PNG preview, with QA.

Part of the Local Service Spotlight Task Library kit for the task
make-a-personal-brand-poster. It fills poster-template-18x24.html (or your own
artboard) from a fact sheet and a photo sheet, checks the result, and writes
versioned, dated files that never overwrite an earlier version:

  <Subject>-<Deliverable>-18x24-v<N>-<YYYY-MM-DD>.pdf         print file, trim size
  <Subject>-<Deliverable>-18x24-bleed-v<N>-<YYYY-MM-DD>.pdf   print file with bleed (only with --bleed)
  <Subject>-<Deliverable>-preview-v<N>-<YYYY-MM-DD>.png       screen preview
  <Subject>-<Deliverable>-qa-v<N>-<YYYY-MM-DD>.json           what was checked

Copy facts-template.csv to facts.csv and photos-template.csv to photos.csv, fill them, then:

  python3 render_poster.py --template poster-template-18x24.html \\
      --facts facts.csv --photos photos.csv \\
      --subject "Jane Doe" --deliverable "Brand Poster" --version 1 --date 2026-11-05 \\
      --out ./out --draft

A final render (no --draft) refuses or fails unless:
  - every fact has a source URL, the words the source says, a check date and status verified.
    A row marked pending-release passes only with --live-check, which fetches the page and finds
    those words on it.
  - no [FILL: ...] placeholder, unfilled slot or empty photo box is left on the poster.
  - every photo has an owner and a permission record. "found-public" and "pending" never qualify.
  - every raster photo is a camera original the script can confirm from its EXIF data, or has
    its original pixel width (native_px_w) recorded, so an enlarged copy cannot pass as print quality.
  - photos reach 240 ppi at printed size, the figure Vistaprint gives for 18 x 24 in seen from
    3 to 6 ft. 150 to 239 ppi warns; under 150 fails.
  - no text is under 9 pt, and no text sits within 0.5 in of the trim, where a frame covers it.

A draft (--draft) is for checking layout. It renders with gaps, is watermarked and named DRAFT,
never places a photo that lacks permission, and fails text within 0.25 in of the trim.

  --bleed 0.125  also write a bleed PDF for printers that ask for one. The page grows by that much
                 on every side, edge colors run into it, and the PDF TrimBox marks the cut line.
                 The kit makes RGB files; ask your printer about color (CMYK).
  --live-check   fetch every source URL and confirm its source_says words are on the page.
  --check-only   audit a finished artboard HTML (no fact or photo sheet) and write nothing.

Needs a computer with Python 3.9+, `pip install playwright pypdf pillow numpy`, then
`python3 -m playwright install chromium`. Most chat apps cannot run this step.
Exit codes: 0 passed (warnings allowed), 2 refused before rendering, 3 rendered but failed QA,
4 tool or environment problem.
"""
import argparse, csv, datetime, hashlib, html, html.parser, io, json, os, re, shutil, sys, tempfile
import urllib.error, urllib.request

SCRIPT_VERSION = "1.1.0 (2026-11-05)"
PX_PER_IN = 96            # CSS reference pixel: 1in = 96px (CSS Values and Units)
PT_PER_PX = 0.75          # 1pt = 1/72in, so 1px = 0.75pt
MIN_PT = 9.0              # nothing on the poster smaller than this
READ_PT = 10.5            # text below this that is not marked data-fineprint gets a WARN for a human look
TRIM_SAFE_IN = 0.25       # hard floor for every render: text this close to the trim can be cut off
FRAME_SAFE_IN = 0.5       # a final render fails inside this: a frame lip or mat covers the outer edge
PPI_TARGET = 240          # Vistaprint: 240 DPI for 18 x 24 in, typical indoor viewing at 3-6 ft
PPI_FLOOR = 150           # Vistaprint: 150 DPI is for large signs viewed from afar; below it fails
CLAIM_OWNERS = {"subject", "counted", "reported", "third-party", "design"}
FACT_STATUSES = {"verified", "pending-release", "omit"}
PHOTO_OK = {"client-owned", "owner-written-ok", "own-work"}   # "found-public" and "pending" never qualify
YES = {"yes", "y", "true", "1"}
SLOT_MARK = "⟦"      # the bracket every unfilled slot hint starts with
FILL_MARK = re.compile(r"\[\s*FILL\b", re.I)
USER_AGENT = f"render_poster.py/{SCRIPT_VERSION.split()[0]} live-check (Local Service Spotlight Task Library poster kit)"


class Report:
    def __init__(self):
        self.items = []

    def add(self, level, check, message, **data):
        self.items.append({"level": level, "check": check, "message": message, **data})

    def failed(self):
        return any(i["level"] == "FAIL" for i in self.items)

    def show(self):
        for i in self.items:
            print(f"  {i['level']:<4} {i['check']}: {i['message']}")


def name_part(text):
    """'Jane Doe' -> 'Jane-Doe'. Keeps capitals, drops characters a file system or URL dislikes."""
    words = re.findall(r"[A-Za-z0-9]+(?:'[A-Za-z]+)?", text.replace("&", " and "))
    return "-".join(w.replace("'", "") for w in words)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def norm(text):
    """Compare text the way a reader would: entities decoded, curly quotes and dashes made plain, case and spacing ignored."""
    text = html.unescape(text).translate(str.maketrans({
        "‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-",
        " ": " ", " ": " ", " ": " ", "…": "..."}))
    return re.sub(r"\s+", " ", text).strip().lower()


class TagCounter(html.parser.HTMLParser):
    TRACK = ("div", "section", "figure", "blockquote", "ol", "ul", "li", "p", "span", "main", "h1", "h2")

    def __init__(self):
        super().__init__()
        self.counts = {t: [0, 0] for t in self.TRACK}

    def handle_starttag(self, tag, attrs):
        if tag in self.counts:
            self.counts[tag][0] += 1

    def handle_endtag(self, tag):
        if tag in self.counts:
            self.counts[tag][1] += 1


def check_tag_balance(path, rep):
    counter = TagCounter()
    with open(path, encoding="utf-8") as f:
        counter.feed(f.read())
    bad = {t: c for t, c in counter.counts.items() if c[0] != c[1]}
    if bad:
        rep.add("FAIL", "tag-balance", "opening and closing tags do not match (a stray tag breaks the layout): "
                + ", ".join(f"<{t}> {c[0]} open / {c[1]} closed" for t, c in bad.items()))
    else:
        rep.add("PASS", "tag-balance", "every tracked tag that opens also closes")


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return [{(k or "").strip(): (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f)]


def load_facts(path, rep, strict):
    """Read the fact sheet. Returns the facts to print and the rows whose sources can be checked live."""
    facts, sources, level = {}, [], ("FAIL" if strict else "WARN")
    for n, row in enumerate(read_csv(path), start=2):
        fid = row.get("fact_id", "")
        if not fid or fid.startswith("#"):
            continue
        status = row.get("status", "").lower()
        if status == "omit":
            facts[fid] = {"omit": True}
            continue
        text, owner, url = row.get("printed_text", ""), row.get("claim_owner", "").lower(), row.get("source_url", "")
        problems = []
        if not text:
            problems.append("printed_text is empty")
        if SLOT_MARK in text:
            problems.append("printed_text still holds a slot hint")
        if FILL_MARK.search(text):
            problems.append("printed_text still holds a [FILL: ...] placeholder")
        if owner not in CLAIM_OWNERS:
            problems.append(f"claim_owner must be one of {sorted(CLAIM_OWNERS)}")
        if status not in FACT_STATUSES:
            problems.append(f"status is '{status or 'blank'}'; use verified, pending-release or omit")
        if owner != "design":
            if not re.match(r"https?://", url):
                problems.append("needs a source_url a stranger can open")
            if not row.get("source_says"):
                problems.append("source_says is empty: copy the words on the source page that support this fact")
            if not row.get("checked_on"):
                problems.append("checked_on date is missing")
            if re.match(r"https?://", url) and row.get("source_says"):
                sources.append({"row": n, "fact_id": fid, "url": url, "says": row["source_says"], "status": status})
        if problems:
            rep.add(level, "fact-sheet", f"row {n} ({fid}): " + "; ".join(problems))
        facts[fid] = {"text": text, "owner": owner, "omit": False, "status": status}
    reported = [k for k, v in facts.items() if k.startswith("results.") and not v.get("omit") and v.get("owner") == "reported"]
    if reported and (facts.get("results.disclosure", {}).get("omit", True)):
        rep.add(level, "fact-sheet", "client-reported results are on the poster without results.disclosure saying whose report they are")
    return facts, sources


def fetch_page_text(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read(8_000_000)
        charset = r.headers.get_content_charset() or "utf-8"
    text = raw.decode(charset, "replace")
    text = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", text)
    return norm(re.sub(r"(?s)<[^>]+>", " ", text))


def live_check(sources, facts, rep, strict):
    """Fetch each source once and look for the quoted words. pending-release rows must be found."""
    pages, results, missing = {}, [], {}
    for s in sources:
        if s["url"] not in pages:
            try:
                pages[s["url"]] = ("ok", fetch_page_text(s["url"]))
            except urllib.error.HTTPError as e:
                pages[s["url"]] = ("error", f"HTTP {e.code}")
            except Exception as e:  # network, TLS, timeout
                pages[s["url"]] = ("error", type(e).__name__ + ": " + str(e)[:80])
        state, body = pages[s["url"]]
        found = state == "ok" and norm(s["says"]) in body
        results.append({"fact_id": s["fact_id"], "url": s["url"], "status": s["status"],
                        "result": "found" if found else ("not-found" if state == "ok" else body)})
        if s["status"] == "pending-release":
            if found:
                facts[s["fact_id"]]["status"] = "verified"
            else:
                why = "the quoted words are not on the page yet" if state == "ok" else f"could not fetch the page ({body})"
                rep.add("FAIL" if strict else "WARN", "live-check",
                        f"row {s['row']} ({s['fact_id']}) is pending-release and {why}: {s['url']}")
        elif not found:
            missing.setdefault((s["url"], "the quoted words are no longer on the page" if state == "ok" else f"could not fetch it ({body})"), []).append(s["fact_id"])
    for (url, why), ids in missing.items():
        rep.add("WARN", "live-check", f"{url}: {why} for {len(ids)} verified row(s) ({', '.join(ids[:4])}{'…' if len(ids) > 4 else ''}); "
                "relying on the check recorded in checked_on")
    found_n = sum(1 for r in results if r["result"] == "found")
    rep.add("PASS" if found_n == len(results) else "INFO", "live-check",
            f"found the quoted words on the live page for {found_n} of {len(results)} sourced rows ({len(pages)} pages fetched)")
    return results


def image_info(path):
    """Pixel size and camera data. Returns None when Pillow is not installed."""
    try:
        from PIL import Image
    except ImportError:
        return None
    with Image.open(path) as im:
        w, h = im.size
        ex = im.getexif()
        sub = ex.get_ifd(0x8769) if hasattr(ex, "get_ifd") else {}
        make, model = ex.get(271), ex.get(272)
        exif_w = sub.get(40962) or ex.get(256)
    return {"px_w": w, "px_h": h, "camera": " ".join(str(x).strip() for x in (make, model) if x) or "",
            "exif_px_w": int(exif_w) if isinstance(exif_w, int) or (isinstance(exif_w, str) and exif_w.isdigit()) else None}


def enlargement_score(path):
    """How much of the finest detail is left. An enlarged copy has almost none, because it holds no
    detail beyond its smaller original. This compares the power in the finest frequency band with a
    middle band, on a center crop. Original photos measured 0.03 to 0.08; copies enlarged 1.5x to
    2.5x measured 0.004 to 0.014. A warning signal only: a very soft original can look the same."""
    try:
        import numpy as np
        from PIL import Image
    except ImportError:
        return None
    with Image.open(path) as im:
        g = im.convert("L")
    w, h = g.size
    if w > 1024 or h > 1024:
        left, top = (w - min(w, 1024)) // 2, (h - min(h, 1024)) // 2
        g = g.crop((left, top, left + min(w, 1024), top + min(h, 1024)))
    a = np.asarray(g, dtype=np.float64)
    a = a - a.mean()
    hh, ww = a.shape
    if hh < 64 or ww < 64:
        return None
    power = np.abs(np.fft.fft2(a * np.outer(np.hanning(hh), np.hanning(ww)))) ** 2
    r = np.maximum(np.abs(np.fft.fftfreq(ww))[None, :], np.abs(np.fft.fftfreq(hh))[:, None])
    top, mid = power[(r > 0.3) & (r <= 0.5)].mean(), power[(r > 0.15) & (r <= 0.2)].mean()
    ratio = float(top / mid) if mid > 0 else 0.0
    return {"fine_detail_ratio": round(ratio, 4), "looks_enlarged": ratio < 0.02}


def load_photos(path, base, rep, strict):
    """Read the photo sheet. Returns photos to place, provenance for the receipt, and photos refused a place."""
    photos, meta, blocked, level = {}, {}, {}, ("FAIL" if strict else "WARN")
    for n, row in enumerate(read_csv(path), start=2):
        pid = row.get("photo_id", "")
        if not pid or pid.startswith("#"):
            continue
        perm = row.get("permission_status", "").lower()
        if perm == "omit":
            photos[pid] = {"omit": True}
            continue
        file_path = row.get("file", "")
        full = file_path if os.path.isabs(file_path) else os.path.join(base, file_path)
        if perm not in PHOTO_OK:
            # Never placed, not even on a draft: a draft gets passed around and can look final.
            blocked[pid] = f"no permission ({perm or 'blank'})"
            rep.add("FAIL", "photo-permission",
                    f"row {n} ({pid}): permission_status is '{perm or 'blank'}'; needs one of {sorted(PHOTO_OK)}. "
                    "A photo found on a public post is not permission. It was not placed on the poster.")
            continue
        problems = []
        exists = bool(file_path) and os.path.isfile(full)
        if not exists:
            problems.append(f"file not found: {file_path or '(blank)'}")
            blocked[pid] = "file not found"
        if perm != "own-work":
            if not row.get("owner"):
                problems.append("owner is empty: name who owns the photo (the photographer or the company that holds it)")
            if not row.get("permission_record"):
                problems.append("permission_record is empty: say where the owner's OK or the client's ownership is recorded")
            if not re.match(r"https?://", row.get("source_url", "")):
                problems.append("needs the source_url where the photo came from")
        if row.get("shows_outside_people", "").lower() in YES and perm == "own-work":
            problems.append("a photo of real people is not own-work; record its owner and permission")
        for col in ("alt", "caption_or_credit"):
            if not row.get(col):
                problems.append(f"{col} is empty")
        for col in ("alt", "caption_or_credit", "who_or_what", "event_place_date", "owner", "permission_record",
                    "source_url", "source_file_url", "shows_outside_people"):
            if FILL_MARK.search(row.get(col, "")):
                problems.append(f"{col} still holds a [FILL: ...] placeholder")
        info = {"file": os.path.abspath(full) if exists else file_path, "native_px_w": row.get("native_px_w", ""),
                "kind": row.get("kind", "photo"), "permission_status": perm, "owner": row.get("owner", ""),
                "camera_original": row.get("camera_original", "").lower() in YES}
        if exists:
            info["sha256"] = sha256_file(full)
            if row.get("sha256") and row["sha256"].lower() != info["sha256"]:
                problems.append("sha256 does not match the file (the photo changed after it was recorded)")
            if not full.lower().endswith(".svg"):
                problems += check_raster(pid, full, row, perm, info, rep)
        meta[pid] = info
        if problems:
            rep.add(level, "photo-sheet", f"row {n} ({pid}): " + "; ".join(problems))
        if exists:
            photos[pid] = {"src": "file://" + os.path.abspath(full), "alt": row.get("alt", ""), "omit": False}
    return photos, meta, blocked


def check_raster(pid, full, row, perm, info, rep):
    """An enlarged copy must not pass as print quality: confirm a camera original, or require the original width."""
    problems = []
    px = image_info(full)
    if px:
        info.update({"file_px": [px["px_w"], px["px_h"]], "camera": px["camera"], "exif_px_w": px["exif_px_w"]})
    if info["camera_original"]:
        if not px:
            problems.append("camera_original needs Pillow to read the camera data (pip install pillow); "
                            "or record native_px_w and source_file_url instead")
        elif not px["camera"]:
            problems.append("camera_original is yes, but the file carries no camera data (EXIF make or model); "
                            "record native_px_w and source_file_url instead")
        elif px["exif_px_w"] and px["exif_px_w"] < px["px_w"]:
            problems.append(f"the file is {px['px_w']} px wide but its camera data says {px['exif_px_w']} px: it was enlarged")
        else:
            info["native_px_w"] = str(px["px_w"])
    else:
        if not row.get("native_px_w", "").isdigit():
            problems.append("native_px_w is empty: record the pixel width of the original file. Without it the script "
                            "cannot tell an enlarged copy from an original (or set camera_original yes for a camera file)")
        if perm != "own-work" and not row.get("source_file_url"):
            problems.append("source_file_url is empty: record the exact file you downloaded")
    score = enlargement_score(full)
    if score:
        info["enlargement_score"] = score
        if score["looks_enlarged"]:
            rep.add("WARN", "photo-enlarged", f"{pid}: the finest detail is missing (ratio {score['fine_detail_ratio']}; originals "
                    "usually measure 0.03 or more), so the file looks enlarged from a smaller original or very soft. "
                    "Confirm it is the original and that native_px_w is the original's true width")
    return problems


FILL_JS = r"""({facts, photos, blocked, draft}) => {
  const root = document.querySelector('[data-print-size]');
  const res = {filled: 0, omitted: [], unknownFacts: [], unknownPhotos: [], missing: [], photoMissing: [], blocked: []};
  for (const [id, f] of Object.entries(facts)) {
    const els = root.querySelectorAll('[data-fact="' + CSS.escape(id) + '"]');
    if (!els.length) { if (!f.omit) res.unknownFacts.push(id); continue; }  // an omitted fact may already be gone with its item
    els.forEach(el => {
      if (f.omit) { (el.closest('[data-item]') || el).remove(); res.omitted.push(id); }
      else { el.textContent = f.text; el.setAttribute('data-filled', ''); res.filled++; }
    });
  }
  for (const [id, p] of Object.entries(photos)) {
    const img = root.querySelector('img[data-photo="' + CSS.escape(id) + '"]');
    if (!img) { res.unknownPhotos.push(id); continue; }
    if (p.omit) { (img.closest('[data-item]') || img).remove(); res.omitted.push('photo:' + id); continue; }
    img.src = p.src; img.alt = p.alt; img.setAttribute('data-filled', '');
    const box = root.querySelector('[data-slot-for="' + CSS.escape(id) + '"]'); if (box) box.classList.add('filled');
  }
  for (const [id, reason] of Object.entries(blocked)) {
    const img = root.querySelector('img[data-photo="' + CSS.escape(id) + '"]');
    if (!img) continue;
    img.removeAttribute('src'); img.setAttribute('data-blocked', reason); res.blocked.push(id);
    const box = root.querySelector('[data-slot-for="' + CSS.escape(id) + '"]');
    if (box) box.setAttribute('data-slot-label', 'NOT PLACED · ' + id + ' · ' + reason);
  }
  root.querySelectorAll('[data-fact]:not([data-filled])').forEach(el => res.missing.push(el.getAttribute('data-fact')));
  root.querySelectorAll('img[data-photo]:not([data-filled]):not([data-blocked])').forEach(el => res.photoMissing.push(el.getAttribute('data-photo')));
  if (draft) {
    root.style.position = 'relative';
    const w = document.createElement('div');
    w.setAttribute('aria-hidden', 'true');
    w.textContent = 'DRAFT · NOT FOR PRINT';
    w.style.cssText = 'position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-30deg);font:800 190px/1 sans-serif;color:rgba(209,0,111,.30);-webkit-text-stroke:4px rgba(255,255,255,.55);white-space:nowrap;pointer-events:none;z-index:99';
    root.appendChild(w);
    for (const edge of ['top', 'bottom']) {
      const b = document.createElement('div');
      b.setAttribute('aria-hidden', 'true');
      b.textContent = 'DRAFT · NOT FOR PRINT · DRAFT · NOT FOR PRINT · DRAFT · NOT FOR PRINT';
      b.style.cssText = 'position:absolute;left:0;right:0;' + edge + ':0;height:38px;background:#D1006F;color:#fff;font:700 21px/38px sans-serif;letter-spacing:.3em;text-align:center;white-space:nowrap;overflow:hidden;z-index:99';
      root.appendChild(b);
    }
  }
  return res;
}"""

MEASURE_JS = r"""async ({rootSelector}) => {
  const root = document.querySelector(rootSelector);
  if (!root) return {error: 'artboard not found: ' + rootSelector};
  await document.fonts.ready;
  await Promise.all([...root.querySelectorAll('img')].filter(i => i.getAttribute('src')).map(i => i.decode().catch(() => null)));
  const R = root.getBoundingClientRect();
  const out = {width: R.width, height: R.height, minPt: null, tooSmall: [], smallNotFine: [], edges: [], overflow: [], intoPadding: [], wide: [],
               fonts: [], images: [], slotText: [], placeholders: [], emptyPhotos: [], zones: [], sizes: {}};
  const watermark = el => { const h = el.closest('[aria-hidden="true"]'); return !!(h && h.textContent.includes('DRAFT')); };
  const fams = new Set();
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    const t = n.textContent.replace(/\s+/g, ' ').trim(); if (!t) continue;
    const el = n.parentElement; const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none' || watermark(el)) continue;
    const range = document.createRange(); range.selectNodeContents(n);
    const rects = [...range.getClientRects()].filter(r => r.width > 0 && r.height > 0);
    if (!rects.length) continue;
    if (t.includes('⟦')) out.slotText.push(t.slice(0, 70));
    if (/\[\s*FILL\b/i.test(t)) out.placeholders.push(t.slice(0, 70));
    const pt = Math.round(parseFloat(cs.fontSize) * 0.75 * 100) / 100;
    out.sizes[pt] = (out.sizes[pt] || 0) + t.length;
    const fine = !!el.closest('[data-fineprint]');
    if (out.minPt === null || pt < out.minPt) out.minPt = pt;
    if (pt < 9 - 1e-6) out.tooSmall.push({text: t.slice(0, 60), pt});
    else if (pt < 10.5 - 1e-6 && !fine) out.smallNotFine.push({text: t.slice(0, 60), pt});
    fams.add(cs.fontFamily.split(',')[0].trim().replace(/^["']|["']$/g, ''));
    let best = null;
    for (const rc of rects) {
      const d = Math.min(rc.left - R.left, rc.top - R.top, R.right - rc.right, R.bottom - rc.bottom);
      if (best === null || d < best) best = d;
    }
    out.edges.push({text: t.slice(0, 60), px: Math.round(best * 10) / 10});
  }
  out.edges.sort((a, b) => a.px - b.px); out.edges = out.edges.slice(0, 12);
  const faces = [...document.fonts];
  for (const fam of fams) {
    const declared = faces.filter(f => f.family.replace(/^["']|["']$/g, '') === fam);
    out.fonts.push({family: fam, declared: declared.length, loaded: declared.filter(f => f.status === 'loaded').length});
  }
  root.querySelectorAll('section, [data-zone]').forEach((s, i) => {
    if (s.scrollHeight > s.clientHeight + 1) out.overflow.push({section: s.getAttribute('data-zone') || i + 1, over: s.scrollHeight - s.clientHeight});
    const pb = parseFloat(getComputedStyle(s).paddingBottom) || 0; const sb = s.getBoundingClientRect().bottom - pb;
    let maxB = 0; s.querySelectorAll('*').forEach(e => { if (watermark(e)) return; const b = e.getBoundingClientRect(); if (b.height > 0) maxB = Math.max(maxB, b.bottom); });
    if (maxB > sb + 1) out.intoPadding.push({section: s.getAttribute('data-zone') || i + 1, px: Math.round(maxB - sb)});
  });
  root.querySelectorAll('[data-zone]').forEach(z => {
    const r = z.getBoundingClientRect();
    out.zones.push({zone: z.getAttribute('data-zone'), x: Math.round(r.left - R.left), y: Math.round(r.top - R.top), w: Math.round(r.width), h: Math.round(r.height)});
  });
  root.querySelectorAll('*').forEach(e => {
    if (e.children.length === 0 && e.textContent.trim() && getComputedStyle(e).display !== 'inline' && e.scrollWidth > e.clientWidth + 1 && !watermark(e))
      out.wide.push({text: e.textContent.trim().slice(0, 50), over: e.scrollWidth - e.clientWidth});
  });
  // A photo box that would print empty: a slot box nobody filled, or a photo that did not load.
  const empty = new Set();
  root.querySelectorAll('[data-slot-for]').forEach(box => {
    const r = box.getBoundingClientRect(), cs = getComputedStyle(box);
    if (r.width && r.height && cs.display !== 'none' && cs.visibility !== 'hidden' && !box.classList.contains('filled')) empty.add(box.getAttribute('data-slot-for'));
  });
  root.querySelectorAll('img[data-photo]').forEach(img => {
    const r = img.getBoundingClientRect();
    if (r.width && r.height && getComputedStyle(img).display !== 'none' && !(img.getAttribute('src') && img.naturalWidth)) empty.add(img.getAttribute('data-photo'));
  });
  out.emptyPhotos = [...empty];
  root.querySelectorAll('img').forEach(img => {
    const src = img.currentSrc || img.src; if (!src || !img.naturalWidth) return;
    const cs = getComputedStyle(img); if (cs.display === 'none' || cs.visibility === 'hidden') return;
    const cw = img.clientWidth, ch = img.clientHeight, nw = img.naturalWidth, nh = img.naturalHeight;
    const fit = cs.objectFit; let scale;
    if (fit === 'cover') scale = Math.max(cw / nw, ch / nh);
    else if (fit === 'contain') scale = Math.min(cw / nw, ch / nh);
    else if (fit === 'none') scale = 1;
    else if (fit === 'scale-down') scale = Math.min(1, Math.min(cw / nw, ch / nh));
    else scale = Math.max(cw / nw, ch / nh);
    out.images.push({photo: img.getAttribute('data-photo') || '', alt: img.alt, src: src.slice(-80), vector: /\.svg(\?|$)/i.test(src) || src.startsWith('data:image/svg'),
      naturalW: nw, naturalH: nh, boxW: cw, boxH: ch, fit, ppi: Math.round(96 / scale), printedWidthIn: Math.round(nw * scale / 96 * 100) / 100});
  });
  return out;
}"""

BLEED_JS = r"""({rootSelector, bleedPx}) => {
  const root = document.querySelector(rootSelector);
  const R = root.getBoundingClientRect(), b = bleedPx, notes = [];
  const near = (x, y) => Math.abs(x - y) < 0.75;
  const opaque = c => c && c !== 'transparent' && !/rgba\([^)]*,\s*0\)$/.test(c);
  for (const el of [...root.querySelectorAll('*')]) {
    const h = el.closest('[aria-hidden="true"]'); if (h && h.textContent.includes('DRAFT')) continue;
    const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
    const L = near(r.left, R.left), T = near(r.top, R.top), Rt = near(r.right, R.right), B = near(r.bottom, R.bottom);
    if (!(L || T || Rt || B)) continue;
    const cs = getComputedStyle(el);
    if (el.tagName === 'IMG' || (cs.backgroundImage && cs.backgroundImage !== 'none'))
      notes.push((el.getAttribute('data-photo') || el.getAttribute('data-zone') || el.className || el.tagName) + ' touches the trim with a picture or gradient; only flat colors run into the bleed');
    if (!opaque(cs.backgroundColor)) continue;
    const c = cs.backgroundColor, sh = [];
    if (L) sh.push(-b + 'px 0 0 0 ' + c); if (Rt) sh.push(b + 'px 0 0 0 ' + c);
    if (T) sh.push('0 ' + -b + 'px 0 0 ' + c); if (B) sh.push('0 ' + b + 'px 0 0 ' + c);
    if (L && T) sh.push(-b + 'px ' + -b + 'px 0 0 ' + c); if (Rt && T) sh.push(b + 'px ' + -b + 'px 0 0 ' + c);
    if (L && B) sh.push(-b + 'px ' + b + 'px 0 0 ' + c); if (Rt && B) sh.push(b + 'px ' + b + 'px 0 0 ' + c);
    el.style.boxShadow = (cs.boxShadow && cs.boxShadow !== 'none' ? cs.boxShadow + ', ' : '') + sh.join(', ');
  }
  const bg = getComputedStyle(root).backgroundColor;
  root.style.overflow = 'visible';
  document.documentElement.style.background = bg; document.body.style.background = bg;
  document.body.style.margin = '0'; document.body.style.padding = b + 'px';
  return {notes};
}"""


def judge_layout(m, rep, size_in, photo_meta, final, ppi_target, ppi_floor):
    w_in, h_in = size_in
    if abs(m["width"] - w_in * PX_PER_IN) > 0.5 or abs(m["height"] - h_in * PX_PER_IN) > 0.5:
        rep.add("FAIL", "artboard-size", f"artboard is {m['width']}x{m['height']} px; {w_in}x{h_in} in needs {w_in*PX_PER_IN}x{h_in*PX_PER_IN} px")
    else:
        rep.add("PASS", "artboard-size", f"{int(m['width'])}x{int(m['height'])} px = {w_in}x{h_in} in at {PX_PER_IN} px per inch")
    if m["slotText"]:
        rep.add("FAIL", "slots", f"{len(m['slotText'])} unfilled slot hint(s) still on the poster, e.g. {m['slotText'][0]!r}")
    if m["placeholders"]:
        rep.add("FAIL" if final else "WARN", "placeholders",
                f"{len(m['placeholders'])} [FILL: ...] placeholder(s) still on the poster, e.g. {m['placeholders'][0]!r}")
    if m["emptyPhotos"]:
        rep.add("FAIL" if final else "WARN", "empty-photo",
                "photo box(es) would print empty: " + ", ".join(m["emptyPhotos"])
                + ". Fill the photo, or mark it omit so its whole block is removed.")
    if m["tooSmall"]:
        rep.add("FAIL", "type-size", f"{len(m['tooSmall'])} text run(s) under {MIN_PT} pt, e.g. {m['tooSmall'][0]}")
    else:
        rep.add("PASS", "type-size", f"smallest type {m['minPt']} pt (floor {MIN_PT} pt)")
    if m["smallNotFine"]:
        uniq = sorted({(x["text"], x["pt"]) for x in m["smallNotFine"]}, key=lambda x: x[1])
        rep.add("WARN", "type-size", f"{len(uniq)} text run(s) under {READ_PT} pt are not marked data-fineprint; read them at arm's length: "
                + "; ".join(f"{t!r} {p}pt" for t, p in uniq[:6]))
    close = m["edges"][0]["px"] if m["edges"] else None
    if close is not None:
        floor = FRAME_SAFE_IN if final else TRIM_SAFE_IN
        if close < floor * PX_PER_IN:
            bad = [e for e in m["edges"] if e["px"] < floor * PX_PER_IN]
            why = ("a final render needs 0.5 in, because a frame lip or mat covers the outer edge" if final
                   else "even a draft needs 0.25 in, or the trim can cut it")
            rep.add("FAIL", "safe-margin", f"text {close/PX_PER_IN:.2f} in from the trim edge ({why}): "
                    + "; ".join(f"{e['text']!r} {e['px']/PX_PER_IN:.2f} in" for e in bad[:4]))
        elif close < FRAME_SAFE_IN * PX_PER_IN:
            rep.add("WARN", "safe-margin", f"closest text is {close/PX_PER_IN:.2f} in from the edge; the final render fails inside {FRAME_SAFE_IN} in")
        else:
            rep.add("PASS", "safe-margin", f"all text at least {close/PX_PER_IN:.2f} in from every edge")
    for o in m["overflow"]:
        rep.add("FAIL", "overflow", f"section {o['section']} content is {o['over']} px taller than its box")
    for o in m["intoPadding"]:
        rep.add("WARN", "overflow", f"section {o['section']} content runs {o['px']} px into its bottom padding")
    for o in m["wide"][:5]:
        rep.add("FAIL", "overflow", f"text wider than its box by {o['over']} px: {o['text']!r}")
    for f in m["fonts"]:
        if f["declared"] and not f["loaded"]:
            rep.add("FAIL", "fonts", f"'{f['family']}' did not load; the PDF would use a fallback font")
        elif not f["declared"]:
            rep.add("WARN", "fonts", f"'{f['family']}' is not a web font; it depends on what this computer has installed")
    for img in m["images"]:
        label = img["photo"] or img["alt"][:40] or img["src"]
        if img["vector"]:
            rep.add("PASS", "photo-resolution", f"{label}: vector art, prints sharp at any size")
            continue
        ppi, native = img["ppi"], img["ppi"]
        meta = photo_meta.get(img["photo"], {})
        if str(meta.get("native_px_w", "")).isdigit() and int(meta["native_px_w"]) < img["naturalW"]:
            native = round(img["ppi"] * int(meta["native_px_w"]) / img["naturalW"])
        detail = (f"{label}: {img['naturalW']}x{img['naturalH']} px printed {img['printedWidthIn']} in wide = {ppi} ppi"
                  + (f", but only {native} ppi counting the original {meta['native_px_w']} px" if native != ppi else ""))
        level = "FAIL" if native < ppi_floor else "WARN" if native < ppi_target else "PASS"
        rep.add(level, "photo-resolution", detail + ("" if level == "PASS" else
                f" (Vistaprint gives {ppi_target} dpi for 18 x 24 in seen from 3 to 6 ft; under {ppi_floor} fails. "
                "Ask for a larger original; enlarging a small file adds no detail)"))


def verify_pdf(path, size_in, version, date, draft, rep, label="pdf", trim_in=None):
    try:
        from pypdf import PdfReader
    except ImportError:
        rep.add("FAIL", "pdf", "pypdf is not installed (pip install pypdf); the PDF could not be checked")
        return {}
    r = PdfReader(path)
    info = {"pages": len(r.pages)}
    page = r.pages[0]
    mb = page.mediabox
    info["page_pt"] = [round(float(mb.width), 2), round(float(mb.height), 2)]
    want = [size_in[0] * 72, size_in[1] * 72]
    if len(r.pages) != 1:
        rep.add("FAIL", f"{label}-pages", f"{len(r.pages)} pages; a poster is one page")
    if abs(info["page_pt"][0] - want[0]) > 0.5 or abs(info["page_pt"][1] - want[1]) > 0.5:
        rep.add("FAIL", f"{label}-size", f"page is {info['page_pt']} pt; {size_in[0]:g}x{size_in[1]:g} in is {want} pt")
    else:
        rep.add("PASS", f"{label}-size", f"page is {info['page_pt'][0]:g} x {info['page_pt'][1]:g} pt = exactly {size_in[0]:g} x {size_in[1]:g} in")
    if trim_in:
        tb = [round(float(x), 2) for x in page.trimbox]
        info["trimbox_pt"] = tb
        b = (size_in[0] - trim_in[0]) / 2 * 72
        want_tb = [b, b, b + trim_in[0] * 72, b + trim_in[1] * 72]
        if all(abs(x - y) < 0.5 for x, y in zip(tb, want_tb)):
            rep.add("PASS", f"{label}-trimbox", f"TrimBox {tb} marks the {trim_in[0]:g} x {trim_in[1]:g} in cut")
        else:
            rep.add("FAIL", f"{label}-trimbox", f"TrimBox is {tb}; the cut needs {want_tb}")
    fonts, seen = [], set()

    def walk(resources):
        if not resources:
            return
        resources = resources.get_object()
        for _, ref in (resources.get("/Font") or {}).items():
            font = ref.get_object()
            if id(font) in seen:
                continue
            seen.add(id(font))
            sub = font.get("/Subtype")
            desc = None
            if sub == "/Type0":
                desc = font["/DescendantFonts"][0].get_object().get("/FontDescriptor")
            elif sub != "/Type3":
                desc = font.get("/FontDescriptor")
            embedded = sub == "/Type3" or bool(desc and any(k in desc.get_object() for k in ("/FontFile", "/FontFile2", "/FontFile3")))
            fonts.append({"name": str(font.get("/BaseFont", "?")), "subtype": str(sub), "embedded": embedded})
        for _, ref in (resources.get("/XObject") or {}).items():
            x = ref.get_object()
            if x.get("/Subtype") == "/Form":
                walk(x.get("/Resources"))

    walk(page.get("/Resources"))
    info["fonts"] = fonts
    missing = [f["name"] for f in fonts if not f["embedded"]]
    if missing:
        rep.add("FAIL", f"{label}-fonts", "fonts not embedded: " + ", ".join(missing))
    else:
        rep.add("PASS", f"{label}-fonts", f"all {len(fonts)} fonts embedded")
    type3 = [f for f in fonts if f["subtype"] == "/Type3"]
    if type3:
        rep.add("WARN", f"{label}-fonts", f"{len(type3)} of {len(fonts)} fonts are Type 3. Chromium makes them from variable web fonts"
                + (", and on a draft from the outlined DRAFT watermark" if draft else "")
                + ". Some printers' preflight flags Type 3: render with --offline-fonts-css pointing at static font files.")
    title = str((r.metadata or {}).get("/Title", "") or "")
    info["title"] = title
    if f"v{version}" in title and date in title and (("DRAFT" in title) == draft):
        rep.add("PASS", f"{label}-title", f"PDF title carries the version and date: {title!r}")
    else:
        rep.add("FAIL", f"{label}-title", f"PDF title {title!r} must carry v{version} and {date}")
    return info


def check_bleed_png(png_bytes, bleed_px, rep):
    """Sample the bleed strips against the colors just inside the trim, row by row."""
    try:
        from PIL import Image
    except ImportError:
        rep.add("WARN", "bleed-colors", "Pillow is not installed, so the bleed colors were not compared with the edge")
        return
    im = Image.open(io.BytesIO(png_bytes)).convert("RGB")
    W, H = im.size
    b = bleed_px
    px = im.load()
    out_d, in_d = max(1, b // 2), b + 2

    def far(c1, c2):
        return sum(abs(x - y) for x, y in zip(c1, c2)) > 45

    sides = {"left": [(out_d, y, in_d, y) for y in range(b + 4, H - b - 4, 6)],
             "right": [(W - 1 - out_d, y, W - 1 - in_d, y) for y in range(b + 4, H - b - 4, 6)],
             "top": [(x, out_d, x, in_d) for x in range(b + 4, W - b - 4, 6)],
             "bottom": [(x, H - 1 - out_d, x, H - 1 - in_d) for x in range(b + 4, W - b - 4, 6)]}
    worst = []
    for side, pairs in sides.items():
        bad = sum(1 for x1, y1, x2, y2 in pairs if far(px[x1, y1], px[x2, y2]))
        share = bad / max(1, len(pairs))
        if share > 0.02:
            worst.append(f"{side} {share:.0%}")
    if worst:
        rep.add("WARN", "bleed-colors", "the bleed does not continue the edge everywhere (" + ", ".join(worst)
                + " of samples differ); look at the bleed PDF before sending it")
    else:
        rep.add("PASS", "bleed-colors", "the bleed continues the colors at every edge")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--template", help="artboard HTML with data-fact and data-photo slots")
    ap.add_argument("--facts", help="fact sheet CSV (copy facts-template.csv to facts.csv)")
    ap.add_argument("--photos", help="photo sheet CSV (copy photos-template.csv to photos.csv)")
    ap.add_argument("--subject", help='whose poster, e.g. "Jane Doe"')
    ap.add_argument("--deliverable", default="Brand Poster", help='poster name, e.g. "Flight Record"')
    ap.add_argument("--version", type=int, help="version number; every new render gets a new one")
    ap.add_argument("--date", help="YYYY-MM-DD for the file names and PDF title")
    ap.add_argument("--out", default=".", help="folder for the outputs (never overwritten)")
    ap.add_argument("--size", default=None, help="WxH in inches; read from data-print-size when omitted")
    ap.add_argument("--draft", action="store_true", help="layout proof: allow gaps; watermark and name it DRAFT")
    ap.add_argument("--bleed", type=float, default=0.0, metavar="IN", help="also write a bleed PDF this many inches past the trim, e.g. 0.125")
    ap.add_argument("--live-check", action="store_true", help="fetch every source and confirm its source_says words are on the page")
    ap.add_argument("--ppi-target", type=int, default=PPI_TARGET, help=f"photo ppi that passes (default {PPI_TARGET})")
    ap.add_argument("--ppi-floor", type=int, default=PPI_FLOOR, help=f"photo ppi below which a render fails (default {PPI_FLOOR})")
    ap.add_argument("--check-only", metavar="HTML", help="audit a finished artboard HTML and write nothing")
    ap.add_argument("--root-selector", default="[data-print-size]", help="CSS selector of the artboard element")
    ap.add_argument("--offline-fonts-css", help="CSS file with @font-face rules to use instead of Google Fonts")
    ap.add_argument("--preview-scale", type=float, default=1.0, help="PNG preview pixel scale (1 = 96 px per inch)")
    a = ap.parse_args(argv)
    rep = Report()
    final = not a.draft

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is missing: pip install playwright pypdf pillow numpy && python3 -m playwright install chromium")
        return 4

    html_path = a.check_only or a.template
    if not html_path or not os.path.isfile(html_path):
        print("Give --template FILE (render) or --check-only FILE (audit).")
        return 2
    if a.bleed < 0 or a.bleed > 0.5:
        print("--bleed must be between 0 and 0.5 inches (printers usually ask for 0.125).")
        return 2
    check_tag_balance(html_path, rep)

    size_in = None
    if a.size:
        size_in = tuple(float(x) for x in a.size.lower().split("x"))
    else:
        m = re.search(r'data-print-size="(\d+(?:\.\d+)?)x(\d+(?:\.\d+)?)"', open(html_path, encoding="utf-8").read())
        if m:
            size_in = (float(m.group(1)), float(m.group(2)))
    if not size_in:
        print("Print size unknown: add data-print-size=\"18x24\" to the artboard or pass --size 18x24.")
        return 2
    size_label = f"{size_in[0]:g}x{size_in[1]:g}"

    facts, photos, photo_meta, blocked, outputs, live = {}, {}, {}, {}, {}, []
    if not a.check_only:
        if not (a.subject and a.version and a.date):
            print("A render needs --subject, --version and --date (versioned, dated file names are required).")
            return 2
        if a.version < 1 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.date):
            print("--version must be 1 or more and --date must look like 2026-11-05.")
            return 2
        try:
            datetime.date.fromisoformat(a.date)
        except ValueError:
            print(f"--date {a.date} is not a real calendar date.")
            return 2
        sources = []
        if a.facts:
            facts, sources = load_facts(a.facts, rep, final)
        elif final:
            rep.add("FAIL", "fact-sheet", "a final render needs --facts")
        if a.live_check and sources:
            live = live_check(sources, facts, rep, final)
        pending = [f for f, v in facts.items() if not v.get("omit") and v.get("status") == "pending-release"]
        if pending:
            rep.add("FAIL" if final else "WARN", "fact-sheet",
                    f"{len(pending)} fact(s) are pending-release (their source page is not live yet): {', '.join(pending[:6])}"
                    + ("…" if len(pending) > 6 else "") + ". Re-run with --live-check once the page is live.")
        if a.photos:
            photos, photo_meta, blocked = load_photos(a.photos, os.path.dirname(os.path.abspath(a.photos)), rep, final)
        elif final:
            rep.add("FAIL", "photo-sheet", "a final render needs --photos")

        stem = f"{name_part(a.subject)}-{name_part(a.deliverable)}" + ("-DRAFT" if a.draft else "")
        os.makedirs(a.out, exist_ok=True)
        names = {"pdf": f"{stem}-{size_label}-v{a.version}-{a.date}.pdf",
                 "png": f"{stem}-preview-v{a.version}-{a.date}.png",
                 "qa": f"{stem}-qa-v{a.version}-{a.date}.json"}
        if a.bleed:
            names["bleed"] = f"{stem}-{size_label}-bleed-v{a.version}-{a.date}.pdf"
        used = re.compile(rf"^{re.escape(stem)}-(?:{re.escape(size_label)}(?:-bleed)?|preview|qa)-v(\d+)-\d{{4}}-\d{{2}}-\d{{2}}\.(?:pdf|png|json)$")
        versions = sorted({int(mm.group(1)) for f in os.listdir(a.out) if (mm := used.match(f))})
        if a.version in versions or any(os.path.exists(os.path.join(a.out, n)) for n in names.values()):
            print(f"REFUSED: v{a.version} of {stem} already exists in {a.out}. Earlier versions are kept, never "
                  f"overwritten. Use --version {max(versions + [a.version]) + 1}.")
            return 2
        if versions and a.version < max(versions):
            rep.add("WARN", "version", f"v{max(versions)} already exists; v{a.version} will sort before it")
        rep.add("PASS", "file-names", "new versioned names: " + ", ".join(v for k, v in names.items() if k != "qa"))
        if final and rep.failed():
            print(f"REFUSED before rendering {stem} v{a.version}:")
            rep.show()
            print("Fix the rows above, or use --draft for a watermarked layout proof that must not be printed.")
            return 2

    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    started = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    tmp, m, bleed_notes = None, {}, []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(**({"proxy": {"server": proxy}} if proxy else {}))
        page = browser.new_page(viewport={"width": int(size_in[0] * PX_PER_IN), "height": int(size_in[1] * PX_PER_IN)},
                                device_scale_factor=a.preview_scale)
        page.goto("file://" + os.path.abspath(html_path), wait_until="load")
        if a.offline_fonts_css:
            css = open(a.offline_fonts_css, encoding="utf-8").read()
            page.evaluate("""(css) => { document.querySelectorAll('link[href*="fonts.googleapis.com"]').forEach(l => l.remove());
                             const s = document.createElement('style'); s.textContent = css; document.head.appendChild(s); }""", css)
        if not a.check_only:
            fill = page.evaluate(FILL_JS, {"facts": facts, "photos": photos, "blocked": blocked, "draft": a.draft})
            level = "FAIL" if final else "WARN"
            if fill["missing"]:
                rep.add(level, "slots", f"{len(fill['missing'])} text slot(s) not in the fact sheet: {', '.join(fill['missing'][:8])}")
            if fill["photoMissing"]:
                rep.add(level, "slots", f"photo slot(s) not in the photo sheet: {', '.join(fill['photoMissing'])}")
            if fill["unknownFacts"] or fill["unknownPhotos"]:
                rep.add("WARN", "slots", "rows that match no slot: " + ", ".join(fill["unknownFacts"] + fill["unknownPhotos"]))
        m = page.evaluate(MEASURE_JS, {"rootSelector": a.root_selector})
        if m.get("error"):
            print(m["error"])
            browser.close()
            return 4
        judge_layout(m, rep, size_in, photo_meta, final, a.ppi_target, a.ppi_floor)
        if a.draft:  # a draft is expected to have open slots; every other failure stays a FAIL
            rep.items = [dict(i, level="WARN") if i["level"] == "FAIL" and i["check"] in ("slots", "fact-sheet", "photo-sheet") else i
                         for i in rep.items]

        if not a.check_only and (a.draft or not rep.failed()):
            deliv = a.deliverable.strip()
            noun = "" if re.search(r"poster$", deliv, re.I) else " poster"
            title = f"{a.subject} - {deliv}{noun}, {size_label} in - v{a.version} ({a.date})" + (" DRAFT" if a.draft else "")
            page.evaluate("t => { document.title = t; }", title)
            tmp = tempfile.mkdtemp(prefix="poster-")
            pdf_tmp, png_tmp = os.path.join(tmp, names["pdf"]), os.path.join(tmp, names["png"])
            page.screenshot(path=png_tmp, full_page=False)
            page.pdf(path=pdf_tmp, width=f"{size_in[0]}in", height=f"{size_in[1]}in", print_background=True,
                     page_ranges="1", prefer_css_page_size=True)
            outputs["pdf"] = verify_pdf(pdf_tmp, size_in, a.version, a.date, a.draft, rep)
            for kind, p in (("pdf", pdf_tmp), ("png", png_tmp)):
                outputs.setdefault(kind, {}).update({"file": names[kind], "sha256": sha256_file(p), "bytes": os.path.getsize(p)})
            if a.bleed and not rep.failed():
                bpx = round(a.bleed * PX_PER_IN)
                full_in = (size_in[0] + 2 * a.bleed, size_in[1] + 2 * a.bleed)
                bleed_notes = page.evaluate(BLEED_JS, {"rootSelector": a.root_selector, "bleedPx": bpx})["notes"]
                for note in bleed_notes[:5]:
                    rep.add("WARN", "bleed", note)
                page.evaluate("""([w, h]) => { const s = document.createElement('style');
                                 s.textContent = '@page{size:' + w + 'in ' + h + 'in;margin:0}'; document.head.appendChild(s); }""", list(full_in))
                page.set_viewport_size({"width": round(full_in[0] * PX_PER_IN), "height": round(full_in[1] * PX_PER_IN)})
                check_bleed_png(page.screenshot(full_page=False, scale="css"), bpx, rep)
                raw_tmp = os.path.join(tmp, "bleed-raw.pdf")
                page.pdf(path=raw_tmp, width=f"{full_in[0]}in", height=f"{full_in[1]}in", print_background=True,
                         page_ranges="1", prefer_css_page_size=True)
                from pypdf import PdfWriter
                from pypdf.generic import RectangleObject
                wr = PdfWriter(clone_from=raw_tmp)
                bpt = a.bleed * 72
                wr.pages[0].trimbox = RectangleObject([bpt, bpt, bpt + size_in[0] * 72, bpt + size_in[1] * 72])
                wr.pages[0].bleedbox = RectangleObject([0, 0, full_in[0] * 72, full_in[1] * 72])
                wr.add_metadata({"/Title": f"{title} - with {a.bleed:g} in bleed"})
                bleed_tmp = os.path.join(tmp, names["bleed"])
                with open(bleed_tmp, "wb") as fh:
                    wr.write(fh)
                outputs["bleed"] = verify_pdf(bleed_tmp, full_in, a.version, a.date, a.draft, rep, label="bleed-pdf", trim_in=size_in)
                outputs["bleed"].update({"file": names["bleed"], "sha256": sha256_file(bleed_tmp), "bytes": os.path.getsize(bleed_tmp),
                                         "bleed_in": a.bleed})
        browser.close()

    finished = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    ok = not rep.failed()
    print(("PASSED" if ok else "FAILED") + (" (DRAFT)" if a.draft else "") + f": {html_path}")
    rep.show()
    if a.check_only:
        return 0 if ok else 3
    receipt = {"tool": "render_poster.py", "tool_version": SCRIPT_VERSION, "started_utc": started, "finished_utc": finished,
               "subject": a.subject, "deliverable": a.deliverable, "version": a.version, "date": a.date, "draft": a.draft,
               "size_in": size_label, "bleed_in": a.bleed or None,
               "inputs": {k: {"file": os.path.basename(v), "sha256": sha256_file(v)}
                          for k, v in (("template", html_path), ("facts", a.facts), ("photos", a.photos)) if v},
               "photos": photo_meta, "photos_not_placed": blocked, "live_checks": live, "outputs": outputs,
               "result": "PASS" if ok else "FAIL", "checks": rep.items,
               "measurements": {k: m.get(k) for k in ("minPt", "sizes", "edges", "images", "fonts", "zones", "emptyPhotos")}}
    if not ok and not a.draft:
        with open(os.path.join(a.out, "qa-last-failed-run.json"), "w", encoding="utf-8") as f:
            json.dump(receipt, f, indent=1)
        print("Nothing was saved under a version name. See qa-last-failed-run.json, fix it, and render again.")
        return 3
    for kind in [k for k in ("pdf", "png", "bleed") if k in outputs]:
        shutil.move(os.path.join(tmp, names[kind]), os.path.join(a.out, names[kind]))
    with open(os.path.join(a.out, names["qa"]), "x", encoding="utf-8") as f:
        json.dump(receipt, f, indent=1)
    print("Saved: " + "  ".join(names[k] for k in ("pdf", "bleed", "png", "qa") if k in names and (k == "qa" or k in outputs)))
    return 0 if ok else 3


if __name__ == "__main__":
    sys.exit(main())
