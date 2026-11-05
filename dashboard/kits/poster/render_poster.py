#!/usr/bin/env python3
"""Render a personal brand poster to a print-ready PDF and a PNG preview, with QA.

Part of the Local Service Spotlight Task Library kit for the task
make-a-personal-brand-poster. It fills poster-template-18x24.html (or your own
artboard) from facts.csv and photos.csv, checks the result, and writes
versioned, dated files that never overwrite an earlier version:

  <Subject>-<Deliverable>-18x24-v<N>-<YYYY-MM-DD>.pdf      print file
  <Subject>-<Deliverable>-preview-v<N>-<YYYY-MM-DD>.png    screen preview
  <Subject>-<Deliverable>-qa-v<N>-<YYYY-MM-DD>.json        what was checked

Example:
  python3 render_poster.py --template poster-template-18x24.html \\
      --facts facts.csv --photos photos.csv \\
      --subject "Jane Doe" --deliverable "Brand Poster" --version 1 --date 2026-11-05 \\
      --out ./out

  --draft        render even with unfilled slots or unsourced facts; the PDF carries a
                 DRAFT watermark and "-DRAFT" in its name. Never send a draft to print.
  --check-only   audit a finished artboard HTML (no facts or photos): layout, type size,
                 safe margins, fonts and photo resolution. Writes nothing.

Needs: Python 3.9+, `pip install playwright pypdf`, then `python3 -m playwright install chromium`.
Exit codes: 0 passed (warnings allowed), 2 refused before rendering, 3 rendered but failed QA,
4 tool or environment problem.
"""
import argparse, csv, datetime, hashlib, html.parser, json, os, re, shutil, sys, tempfile

SCRIPT_VERSION = "1.0.0 (2026-11-05)"
PX_PER_IN = 96            # CSS reference pixel: 1in = 96px (CSS Values and Units)
PT_PER_PX = 0.75          # 1pt = 1/72in, so 1px = 0.75pt
MIN_PT = 9.0              # nothing on the poster smaller than this
READ_PT = 10.5            # text below this that is not marked data-fineprint gets a WARN for a human look
TRIM_SAFE_IN = 0.25       # text closer than this to the trim edge fails
FRAME_SAFE_IN = 0.5       # text closer than this warns: a frame lip or mat can hide it
PPI_FAIL, PPI_WARN = 100, 150   # effective photo resolution at printed size, counted on original pixels
CLAIM_OWNERS = {"subject", "counted", "reported", "third-party", "design"}
PHOTO_OK = {"client-owned", "owner-written-ok", "own-work"}   # "found-public" and "pending" never qualify
SLOT_MARK = "⟦"      # the bracket every unfilled slot hint starts with


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
    facts, level = {}, ("FAIL" if strict else "WARN")
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
        if owner not in CLAIM_OWNERS:
            problems.append(f"claim_owner must be one of {sorted(CLAIM_OWNERS)}")
        if owner != "design" and not re.match(r"https?://", url):
            problems.append("needs a source_url a stranger can open")
        if status != "verified":
            problems.append(f"status is '{status or 'blank'}', not verified")
        if owner != "design" and not row.get("checked_on"):
            problems.append("checked_on date is missing")
        if problems:
            rep.add(level, "fact-sheet", f"row {n} ({fid}): " + "; ".join(problems))
        facts[fid] = {"text": text, "owner": owner, "omit": False}
    reported = [k for k, v in facts.items() if k.startswith("results.") and not v.get("omit") and v.get("owner") == "reported"]
    if reported and (facts.get("results.disclosure", {}).get("omit", True)):
        rep.add(level, "fact-sheet", "client-reported results are on the poster without results.disclosure saying whose report they are")
    return facts


def load_photos(path, base, rep, strict):
    photos, meta, level = {}, {}, ("FAIL" if strict else "WARN")
    for n, row in enumerate(read_csv(path), start=2):
        pid = row.get("photo_id", "")
        if not pid or pid.startswith("#"):
            continue
        if row.get("permission_status", "").lower() == "omit":
            photos[pid] = {"omit": True}
            continue
        file_path = row.get("file", "")
        full = file_path if os.path.isabs(file_path) else os.path.join(base, file_path)
        problems = []
        if not os.path.isfile(full):
            problems.append(f"file not found: {file_path}")
        perm = row.get("permission_status", "").lower()
        if perm not in PHOTO_OK:
            problems.append(f"permission_status is '{perm or 'blank'}'; needs one of {sorted(PHOTO_OK)} "
                            "(a photo found on a public post is not permission)")
        if perm != "own-work":
            if not row.get("owner"):
                problems.append("owner is empty: name who owns the photo (the photographer or the company that holds it)")
            if not row.get("permission_record"):
                problems.append("permission_record is empty: say where the owner's OK or the client's ownership is recorded")
            if not re.match(r"https?://", row.get("source_url", "")):
                problems.append("needs the source_url where the photo came from")
        if row.get("shows_outside_people", "").lower() in ("yes", "y", "true") and perm == "own-work":
            problems.append("a photo of real people is not own-work; record its owner and permission")
        for col in ("alt", "caption_or_credit"):
            if not row.get(col):
                problems.append(f"{col} is empty")
        if os.path.isfile(full):
            digest = sha256_file(full)
            if row.get("sha256") and row["sha256"].lower() != digest:
                problems.append("sha256 does not match the file (the photo changed after it was recorded)")
            meta[pid] = {"file": os.path.abspath(full), "sha256": digest, "native_px_w": row.get("native_px_w", ""),
                         "kind": row.get("kind", "photo")}
        if problems:
            rep.add(level, "photo-sheet", f"row {n} ({pid}): " + "; ".join(problems))
        if os.path.isfile(full):
            photos[pid] = {"src": "file://" + os.path.abspath(full), "alt": row.get("alt", ""), "omit": False}
    return photos, meta


FILL_JS = r"""({facts, photos, draft}) => {
  const root = document.querySelector('[data-print-size]');
  const res = {filled: 0, omitted: [], unknownFacts: [], unknownPhotos: [], missing: [], photoMissing: []};
  for (const [id, f] of Object.entries(facts)) {
    const els = root.querySelectorAll('[data-fact="' + CSS.escape(id) + '"]');
    if (!els.length) { res.unknownFacts.push(id); continue; }
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
    const box = img.closest('.slot-photo'); if (box) box.classList.add('filled');
  }
  root.querySelectorAll('[data-fact]:not([data-filled])').forEach(el => res.missing.push(el.getAttribute('data-fact')));
  root.querySelectorAll('img[data-photo]:not([data-filled])').forEach(el => res.photoMissing.push(el.getAttribute('data-photo')));
  if (draft) {
    root.style.position = 'relative';
    const w = document.createElement('div');
    w.setAttribute('aria-hidden', 'true');
    w.textContent = 'DRAFT · NOT FOR PRINT';
    w.style.cssText = 'position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-30deg);font:800 190px/1 sans-serif;color:rgba(209,0,111,.22);white-space:nowrap;pointer-events:none;z-index:99';
    root.appendChild(w);
  }
  return res;
}"""

MEASURE_JS = r"""async ({rootSelector}) => {
  const root = document.querySelector(rootSelector);
  if (!root) return {error: 'artboard not found: ' + rootSelector};
  await document.fonts.ready;
  await Promise.all([...root.querySelectorAll('img')].filter(i => i.getAttribute('src')).map(i => i.decode().catch(() => null)));
  const R = root.getBoundingClientRect();
  const out = {width: R.width, height: R.height, minPt: null, tooSmall: [], smallNotFine: [], edges: [], overflow: [], intoPadding: [], wide: [], fonts: [], images: [], slotText: [], sizes: {}};
  const fams = new Set();
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    const t = n.textContent.replace(/\s+/g, ' ').trim(); if (!t) continue;
    const el = n.parentElement; const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none' || el.closest('[aria-hidden="true"]') && el.closest('[aria-hidden="true"]').textContent.includes('DRAFT')) continue;
    const range = document.createRange(); range.selectNodeContents(n);
    const rects = [...range.getClientRects()].filter(r => r.width > 0 && r.height > 0);
    if (!rects.length) continue;
    if (t.includes('⟦')) out.slotText.push(t.slice(0, 70));
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
    if (s.scrollHeight > s.clientHeight + 1) out.overflow.push({section: i + 1, over: s.scrollHeight - s.clientHeight});
    const pb = parseFloat(getComputedStyle(s).paddingBottom) || 0; const sb = s.getBoundingClientRect().bottom - pb;
    let maxB = 0; s.querySelectorAll('*').forEach(e => { const b = e.getBoundingClientRect(); if (b.height > 0) maxB = Math.max(maxB, b.bottom); });
    if (maxB > sb + 1) out.intoPadding.push({section: i + 1, px: Math.round(maxB - sb)});
  });
  root.querySelectorAll('*').forEach(e => {
    if (e.children.length === 0 && e.textContent.trim() && getComputedStyle(e).display !== 'inline' && e.scrollWidth > e.clientWidth + 1)
      out.wide.push({text: e.textContent.trim().slice(0, 50), over: e.scrollWidth - e.clientWidth});
  });
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


def judge_layout(m, rep, size_in, photo_meta):
    w_in, h_in = size_in
    if abs(m["width"] - w_in * PX_PER_IN) > 0.5 or abs(m["height"] - h_in * PX_PER_IN) > 0.5:
        rep.add("FAIL", "artboard-size", f"artboard is {m['width']}x{m['height']} px; {w_in}x{h_in} in needs {w_in*PX_PER_IN}x{h_in*PX_PER_IN} px")
    else:
        rep.add("PASS", "artboard-size", f"{int(m['width'])}x{int(m['height'])} px = {w_in}x{h_in} in at {PX_PER_IN} px per inch")
    if m["slotText"]:
        rep.add("FAIL", "slots", f"{len(m['slotText'])} unfilled slot hint(s) still on the poster, e.g. {m['slotText'][0]!r}")
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
        if close < TRIM_SAFE_IN * PX_PER_IN:
            bad = [e for e in m["edges"] if e["px"] < TRIM_SAFE_IN * PX_PER_IN]
            rep.add("FAIL", "safe-margin", f"text {close/PX_PER_IN:.2f} in from the trim edge (needs {TRIM_SAFE_IN} in): "
                    + "; ".join(f"{e['text']!r} {e['px']/PX_PER_IN:.2f} in" for e in bad[:4]))
        elif close < FRAME_SAFE_IN * PX_PER_IN:
            rep.add("WARN", "safe-margin", f"closest text is {close/PX_PER_IN:.2f} in from the edge; a frame lip or mat can hide text inside {FRAME_SAFE_IN} in")
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
        if meta.get("native_px_w", "").isdigit() and int(meta["native_px_w"]) < img["naturalW"]:
            native = round(img["ppi"] * int(meta["native_px_w"]) / img["naturalW"])
        detail = (f"{label}: {img['naturalW']}x{img['naturalH']} px printed {img['printedWidthIn']} in wide = {ppi} ppi"
                  + (f", but only {native} ppi counting the original {meta['native_px_w']} px" if native != ppi else ""))
        level = "FAIL" if native < PPI_FAIL else "WARN" if native < PPI_WARN else "PASS"
        rep.add(level, "photo-resolution", detail + ("" if level == "PASS" else " (aim for 150+ ppi at printed size; 300 for close viewing)"))


def verify_pdf(path, size_in, version, date, draft, rep):
    try:
        from pypdf import PdfReader
    except ImportError:
        rep.add("FAIL", "pdf", "pypdf is not installed (pip install pypdf); the PDF could not be checked")
        return {}
    r = PdfReader(path)
    info = {"pages": len(r.pages)}
    mb = r.pages[0].mediabox
    info["page_pt"] = [round(float(mb.width), 2), round(float(mb.height), 2)]
    want = [size_in[0] * 72, size_in[1] * 72]
    if len(r.pages) != 1:
        rep.add("FAIL", "pdf-pages", f"{len(r.pages)} pages; a poster is one page")
    if abs(info["page_pt"][0] - want[0]) > 0.5 or abs(info["page_pt"][1] - want[1]) > 0.5:
        rep.add("FAIL", "pdf-size", f"page is {info['page_pt']} pt; {size_in[0]}x{size_in[1]} in is {want} pt")
    else:
        rep.add("PASS", "pdf-size", f"page is {info['page_pt'][0]:g} x {info['page_pt'][1]:g} pt = exactly {size_in[0]} x {size_in[1]} in")
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
            fonts.append({"name": str(font.get("/BaseFont", "?")), "embedded": embedded})
        for _, ref in (resources.get("/XObject") or {}).items():
            x = ref.get_object()
            if x.get("/Subtype") == "/Form":
                walk(x.get("/Resources"))

    walk(r.pages[0].get("/Resources"))
    info["fonts"] = fonts
    missing = [f["name"] for f in fonts if not f["embedded"]]
    if missing:
        rep.add("FAIL", "pdf-fonts", "fonts not embedded: " + ", ".join(missing))
    else:
        rep.add("PASS", "pdf-fonts", f"all {len(fonts)} fonts embedded")
    title = str((r.metadata or {}).get("/Title", "") or "")
    info["title"] = title
    if f"v{version}" in title and date in title and (("DRAFT" in title) == draft):
        rep.add("PASS", "pdf-title", f"PDF title carries the version and date: {title!r}")
    else:
        rep.add("FAIL", "pdf-title", f"PDF title {title!r} must carry v{version} and {date}")
    return info


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--template", help="artboard HTML with data-fact and data-photo slots")
    ap.add_argument("--facts", help="fact sheet CSV (see facts-template.csv)")
    ap.add_argument("--photos", help="photo provenance CSV (see photos-template.csv)")
    ap.add_argument("--subject", help='whose poster, e.g. "Jane Doe"')
    ap.add_argument("--deliverable", default="Brand Poster", help='poster name, e.g. "Flight Record"')
    ap.add_argument("--version", type=int, help="version number; every new render gets a new one")
    ap.add_argument("--date", help="YYYY-MM-DD for the file names and PDF title")
    ap.add_argument("--out", default=".", help="folder for the outputs (never overwritten)")
    ap.add_argument("--size", default=None, help="WxH in inches; read from data-print-size when omitted")
    ap.add_argument("--draft", action="store_true", help="allow unfilled slots and unchecked rows; watermark and name it DRAFT")
    ap.add_argument("--check-only", metavar="HTML", help="audit a finished artboard HTML and write nothing")
    ap.add_argument("--root-selector", default="[data-print-size]", help="CSS selector of the artboard element")
    ap.add_argument("--offline-fonts-css", help="CSS file with @font-face rules to use instead of Google Fonts")
    ap.add_argument("--preview-scale", type=float, default=1.0, help="PNG preview pixel scale (1 = 96 px per inch)")
    a = ap.parse_args(argv)
    rep = Report()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is missing: pip install playwright pypdf && python3 -m playwright install chromium")
        return 4

    html_path = a.check_only or a.template
    if not html_path or not os.path.isfile(html_path):
        print("Give --template FILE (render) or --check-only FILE (audit).")
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

    facts, photos, photo_meta, outputs = {}, {}, {}, {}
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
        strict = not a.draft
        if a.facts:
            facts = load_facts(a.facts, rep, strict)
        elif strict:
            rep.add("FAIL", "fact-sheet", "a final render needs --facts")
        if a.photos:
            photos, photo_meta = load_photos(a.photos, os.path.dirname(os.path.abspath(a.photos)), rep, strict)
        elif strict:
            rep.add("FAIL", "photo-sheet", "a final render needs --photos")

        stem = f"{name_part(a.subject)}-{name_part(a.deliverable)}" + ("-DRAFT" if a.draft else "")
        os.makedirs(a.out, exist_ok=True)
        names = {"pdf": f"{stem}-{size_label}-v{a.version}-{a.date}.pdf",
                 "png": f"{stem}-preview-v{a.version}-{a.date}.png",
                 "qa": f"{stem}-qa-v{a.version}-{a.date}.json"}
        used = re.compile(rf"^{re.escape(stem)}-(?:{re.escape(size_label)}|preview|qa)-v(\d+)-\d{{4}}-\d{{2}}-\d{{2}}\.(?:pdf|png|json)$")
        versions = sorted({int(mm.group(1)) for f in os.listdir(a.out) if (mm := used.match(f))})
        if a.version in versions or any(os.path.exists(os.path.join(a.out, n)) for n in names.values()):
            print(f"REFUSED: v{a.version} of {stem} already exists in {a.out}. Earlier versions are kept, never "
                  f"overwritten. Use --version {max(versions + [a.version]) + 1}.")
            return 2
        if versions and a.version < max(versions):
            rep.add("WARN", "version", f"v{max(versions)} already exists; v{a.version} will sort before it")
        rep.add("PASS", "file-names", f"new versioned names: {names['pdf']}, {names['png']}")
        if rep.failed():
            print(f"REFUSED before rendering {stem} v{a.version}:")
            rep.show()
            print("Fix the rows above, or use --draft for a watermarked proof that must not be printed.")
            return 2

    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    started = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
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
            fill = page.evaluate(FILL_JS, {"facts": facts, "photos": photos, "draft": a.draft})
            level = "WARN" if a.draft else "FAIL"
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
        judge_layout(m, rep, size_in, photo_meta)
        if a.draft:  # a draft is expected to have open slots; every other failure stays a FAIL
            rep.items = [dict(i, level="WARN") if i["level"] == "FAIL" and i["check"] in ("slots", "fact-sheet", "photo-sheet") else i
                         for i in rep.items]

        if not a.check_only and (a.draft or not rep.failed()):
            title = (f"{a.subject} - {a.deliverable} poster, {size_label} in - v{a.version} ({a.date})" + (" DRAFT" if a.draft else ""))
            page.evaluate("t => { document.title = t; }", title)
            tmp = tempfile.mkdtemp(prefix="poster-")
            pdf_tmp, png_tmp = os.path.join(tmp, names["pdf"]), os.path.join(tmp, names["png"])
            page.screenshot(path=png_tmp, full_page=False)
            page.pdf(path=pdf_tmp, width=f"{size_in[0]}in", height=f"{size_in[1]}in", print_background=True,
                     page_ranges="1", prefer_css_page_size=True)
            outputs["pdf"] = verify_pdf(pdf_tmp, size_in, a.version, a.date, a.draft, rep)
            for kind, p in (("pdf", pdf_tmp), ("png", png_tmp)):
                outputs.setdefault(kind, {}).update({"file": names[kind], "sha256": sha256_file(p), "bytes": os.path.getsize(p)})
        browser.close()

    finished = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    ok = not rep.failed()
    print(("PASSED" if ok else "FAILED") + (" (DRAFT)" if a.draft else "") + f": {html_path}")
    rep.show()
    if a.check_only:
        return 0 if ok else 3
    receipt = {"tool": "render_poster.py", "tool_version": SCRIPT_VERSION, "started_utc": started, "finished_utc": finished,
               "subject": a.subject, "deliverable": a.deliverable, "version": a.version, "date": a.date, "draft": a.draft,
               "size_in": size_label, "inputs": {k: {"file": os.path.basename(v), "sha256": sha256_file(v)}
                                                 for k, v in (("template", html_path), ("facts", a.facts), ("photos", a.photos)) if v},
               "photos": photo_meta, "outputs": outputs, "result": "PASS" if ok else "FAIL", "checks": rep.items,
               "measurements": {k: m[k] for k in ("minPt", "sizes", "edges", "images", "fonts")}}
    if not ok and not a.draft:
        with open(os.path.join(a.out, "qa-last-failed-run.json"), "w", encoding="utf-8") as f:
            json.dump(receipt, f, indent=1)
        print("Nothing was saved under a version name. See qa-last-failed-run.json, fix it, and render again.")
        return 3
    for kind in ("pdf", "png"):
        shutil.move(os.path.join(tmp, names[kind]), os.path.join(a.out, names[kind]))
    with open(os.path.join(a.out, names["qa"]), "x", encoding="utf-8") as f:
        json.dump(receipt, f, indent=1)
    print(f"Saved: {names['pdf']}  {names['png']}  {names['qa']}")
    return 0 if ok else 3


if __name__ == "__main__":
    sys.exit(main())
