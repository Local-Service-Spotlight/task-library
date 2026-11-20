#!/usr/bin/env python3
"""Tests for render_poster.py. Run: python3 test_render_poster.py  (or pytest test_render_poster.py)

Every test renders a synthetic "Jane Doe" poster from the kit template with generated images,
so no client data is involved. Rendering needs Playwright with Chromium, pypdf, Pillow and numpy.
Fonts load from Google Fonts unless POSTER_TEST_FONTS_CSS points at a CSS file of @font-face rules.
"""
import csv, http.server, json, os, re, shutil, subprocess, sys, tempfile, threading

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "render_poster.py")
TEMPLATE = os.path.join(HERE, "poster-template-18x24.html")
DATE = "2026-11-05"


def make_image(path, w, h, seed, exif=None):
    from PIL import Image, ImageDraw
    base = Image.effect_noise((w, h), 70).convert("RGB")
    d = ImageDraw.Draw(base)
    for i in range(40):
        x, y = (seed * 97 + i * 131) % w, (seed * 53 + i * 71) % h
        d.rectangle([x, y, x + w // 9, y + h // 11], outline=((i * 40) % 255, (seed * 30) % 255, 120), width=3)
    kw = {"quality": 92}
    if exif:
        ex = Image.Exif()
        ex[271], ex[272] = exif.get("make", "TestCam"), exif.get("model", "Model 1")
        ex[0x8769] = {40962: exif.get("px_w", w), 40963: exif.get("px_h", h)}
        kw["exif"] = ex
    base.save(path, **kw)


class Fixture:
    """A folder with a template, a fact sheet, a photo sheet and photos that pass a final render."""

    def __init__(self):
        self.dir = tempfile.mkdtemp(prefix="poster-test-")
        self.out = os.path.join(self.dir, "out")
        self.template = os.path.join(self.dir, "template.html")
        shutil.copy(TEMPLATE, self.template)
        rows = list(csv.DictReader(open(os.path.join(HERE, "facts-template.csv"), newline="", encoding="utf-8")))
        self.facts = []
        for r in rows:
            fid = r["fact_id"]
            text = {"subject.name": "Jane Doe", "subject.role": "Founder, Example Co.", "quote.text": "Practice beats talent.",
                    "brand.line": "EXAMPLE CO.", "brand.urls": "example.org"}.get(fid)
            if text is None:  # short enough for every slot, so a fixture never overflows
                last = fid.rsplit(".", 1)[-1]
                text = {"value": "42", "when": "2020", "code": "ABC", "label": "LABEL", "kicker": "KICKER", "name": "Ann Lee",
                        "heading": "A heading", "verb": "Had her on a show", "role": "Coach", "what": "A short line"}.get(last, "Short text")
            row = dict(r, printed_text=text, status="verified")
            if r["claim_owner"] != "design":
                row.update(source_url="https://example.org/record", source_says="Jane Doe", checked_on=DATE)
            self.facts.append(row)
        self.photos = []
        specs = [("hero", 1600, 1110, "photo", "no"), ("portrait", 600, 600, "photo", "no"),
                 ("team.1", 300, 300, "photo", "no"), ("team.2", 300, 300, "photo", "no"), ("team.3", 300, 300, "photo", "no")]
        for n, (pid, w, h, kind, people) in enumerate(specs):
            f = f"{pid.replace('.', '-')}.jpg"
            make_image(os.path.join(self.dir, f), w, h, n + 1)
            self.photos.append({"photo_id": pid, "file": f, "kind": kind, "who_or_what": "Synthetic test image", "event_place_date": "Test",
                                "owner": "Example Co.", "permission_status": "client-owned", "permission_record": "Test fixture",
                                "source_url": "https://example.org/photos", "source_file_url": "https://example.org/photos/" + f,
                                "native_px_w": str(w), "camera_original": "", "shows_outside_people": people, "alt": f"Test {pid}",
                                "caption_or_credit": "Photo: Example Co.", "sha256": "", "checked_on": DATE, "notes": ""})
        with open(os.path.join(self.dir, "map.svg"), "w") as fh:
            fh.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 405"><rect width="700" height="405" fill="#ece6da"/>'
                     '<circle cx="350" cy="200" r="60" fill="#e2b43b"/></svg>')
        self.photos.append({"photo_id": "places-map", "file": "map.svg", "kind": "diagram", "who_or_what": "Test map", "event_place_date": "",
                            "owner": "", "permission_status": "own-work", "permission_record": "", "source_url": "", "source_file_url": "",
                            "native_px_w": "", "camera_original": "", "shows_outside_people": "no", "alt": "Test map",
                            "caption_or_credit": "Map: Example Co.", "sha256": "", "checked_on": DATE, "notes": ""})

    def fact(self, fid, **kw):
        next(r for r in self.facts if r["fact_id"] == fid).update(kw)

    def photo(self, pid, **kw):
        next(r for r in self.photos if r["photo_id"] == pid).update(kw)

    def write(self):
        for name, rows in (("facts.csv", self.facts), ("photos.csv", self.photos)):
            with open(os.path.join(self.dir, name), "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
                w.writeheader()
                w.writerows(rows)

    def run(self, *extra, version=1, template=None):
        self.write()
        args = [sys.executable, SCRIPT, "--template", template or self.template, "--facts", os.path.join(self.dir, "facts.csv"),
                "--photos", os.path.join(self.dir, "photos.csv"), "--subject", "Jane Doe", "--version", str(version),
                "--date", DATE, "--out", self.out, *extra]
        if os.environ.get("POSTER_TEST_FONTS_CSS"):
            args += ["--offline-fonts-css", os.environ["POSTER_TEST_FONTS_CSS"]]
        env = dict(os.environ, NO_PROXY="127.0.0.1,localhost", no_proxy="127.0.0.1,localhost")
        p = subprocess.run(args, capture_output=True, text=True, env=env, timeout=300)
        return p.returncode, p.stdout + p.stderr

    def qa(self, draft=False, version=1):
        stem = "Jane-Doe-Brand-Poster" + ("-DRAFT" if draft else "")
        path = os.path.join(self.out, f"{stem}-qa-v{version}-{DATE}.json")
        if not os.path.exists(path):
            path = os.path.join(self.out, "qa-last-failed-run.json")
        return json.load(open(path))

    def cleanup(self):
        shutil.rmtree(self.dir, ignore_errors=True)


def checks(qa, check, level=None):
    return [i for i in qa["checks"] if i["check"] == check and (level is None or i["level"] == level)]


def pdf_image_widths(path):
    from pypdf import PdfReader
    page = PdfReader(path).pages[0]
    widths = []
    for _, ref in (page["/Resources"].get("/XObject") or {}).items():
        x = ref.get_object()
        if x.get("/Subtype") == "/Image":
            widths.append(int(x["/Width"]))
        elif x.get("/Subtype") == "/Form":
            for _, r2 in ((x.get("/Resources") or {}).get("/XObject") or {}).items():
                y = r2.get_object()
                if y.get("/Subtype") == "/Image":
                    widths.append(int(y["/Width"]))
    return widths


# ---------------------------------------------------------------- the tests

def test_help_shows_example_and_exit_codes():
    p = subprocess.run([sys.executable, SCRIPT, "--help"], capture_output=True, text=True)
    assert p.returncode == 0 and "Exit codes" in p.stdout and "--draft" in p.stdout and "facts.csv" in p.stdout, p.stdout[:400]


def test_final_passes_and_title_reads_well():
    f = Fixture()
    try:
        code, out = f.run()
        assert code == 0, out
        pdf = os.path.join(f.out, f"Jane-Doe-Brand-Poster-18x24-v1-{DATE}.pdf")
        from pypdf import PdfReader
        r = PdfReader(pdf)
        title = str(r.metadata.get("/Title"))
        assert "v1" in title and DATE in title and "poster poster" not in title.lower() and "Poster poster" not in title, title
        assert [round(float(x)) for x in r.pages[0].mediabox[2:]] == [1296, 1728]
        code, out = f.run()  # same version again
        assert code == 2 and "REFUSED" in out, out
    finally:
        f.cleanup()


def test_missing_source_is_refused():
    f = Fixture()
    try:
        f.fact("subject.name", source_url="")
        code, out = f.run()
        assert code == 2 and "source_url" in out, out
    finally:
        f.cleanup()


def test_fill_placeholder_is_refused_in_a_final():
    f = Fixture()
    try:
        f.fact("hero.caption", printed_text="[FILL: event · place · year]")
        code, out = f.run()
        assert code == 2 and "[FILL" in out, out
        f.fact("hero.caption", printed_text="Test event · Test city · 2026")
        f.photo("hero", source_file_url="[FILL: URL of the original file]")
        code, out = f.run()
        assert code == 2 and "source_file_url still holds a [FILL" in out, out
    finally:
        f.cleanup()


def test_found_public_photo_is_refused_in_a_final():
    f = Fixture()
    try:
        f.photo("hero", permission_status="found-public")
        code, out = f.run()
        assert code == 2 and "not permission" in out, out
    finally:
        f.cleanup()


def test_draft_never_places_a_found_public_photo():
    """Review finding 5c: a draft used to place a photo found on a public post."""
    f = Fixture()
    try:
        f.photo("hero", permission_status="found-public")
        code, out = f.run("--draft")
        assert code == 3, out  # saved as a draft, but the QA result is FAIL
        qa = f.qa(draft=True)
        assert "hero" in qa["photos_not_placed"], qa["photos_not_placed"]
        assert checks(qa, "photo-permission", "FAIL"), "no photo-permission FAIL in the draft receipt"
        pdf = os.path.join(f.out, f"Jane-Doe-Brand-Poster-DRAFT-18x24-v1-{DATE}.pdf")
        assert 1600 not in pdf_image_widths(pdf), "the found-public hero (1600 px) was embedded in the draft PDF"
    finally:
        f.cleanup()


def test_omitting_the_hero_removes_its_whole_block():
    """Review finding 5d: omitting the hero used to leave a striped box and an orphan caption."""
    f = Fixture()
    try:
        f.photo("hero", permission_status="omit")
        f.fact("hero.caption", printed_text="ORPHAN CAPTION TEST")
        code, out = f.run()
        assert code == 0, out
        qa = f.qa()
        assert qa["measurements"]["emptyPhotos"] == [], qa["measurements"]["emptyPhotos"]
        from pypdf import PdfReader
        text = PdfReader(os.path.join(f.out, f"Jane-Doe-Brand-Poster-18x24-v1-{DATE}.pdf")).pages[0].extract_text()
        assert "ORPHAN CAPTION TEST" not in text
    finally:
        f.cleanup()


def test_a_final_with_an_empty_photo_box_fails():
    """Review finding 5d: a template without a removable hero block must not print an empty box."""
    f = Fixture()
    try:
        html = open(f.template, encoding="utf-8").read().replace('<div class="hero" data-item>', '<div class="hero">')
        custom = os.path.join(f.dir, "custom-template.html")
        open(custom, "w", encoding="utf-8").write(html)
        f.photo("hero", permission_status="omit")
        code, out = f.run(template=custom)
        assert code == 3 and "empty-photo" in out, out
    finally:
        f.cleanup()


def test_margins_final_fails_under_half_inch_draft_floor_is_quarter_inch():
    """Review finding 5a: 0.33 in used to pass a final with a warning."""
    f = Fixture()
    try:
        html = open(f.template, encoding="utf-8").read()
        tight = html.replace(".foot{min-height:180px;flex:none;background:var(--ink);color:var(--on-ink);padding:20px 72px 48px;",
                             ".foot{min-height:180px;flex:none;background:var(--ink);color:var(--on-ink);padding:20px 72px 30px;")
        assert tight != html
        t1 = os.path.join(f.dir, "tight.html")
        open(t1, "w", encoding="utf-8").write(tight)
        code, out = f.run(template=t1)
        assert code == 3 and re.search(r"FAIL safe-margin: text 0\.3\d in", out), out
        code, out = f.run("--draft", template=t1)
        assert code == 0 and "WARN safe-margin" in out, out
        tighter = html.replace(".foot{min-height:180px;flex:none;background:var(--ink);color:var(--on-ink);padding:20px 72px 48px;",
                               ".foot{min-height:180px;flex:none;background:var(--ink);color:var(--on-ink);padding:20px 72px 16px;")
        t2 = os.path.join(f.dir, "tighter.html")
        open(t2, "w", encoding="utf-8").write(tighter)
        code, out = f.run("--draft", template=t2, version=2)
        assert code == 3 and "FAIL safe-margin" in out, out
    finally:
        f.cleanup()


def test_raster_photo_needs_its_original_width():
    """Review finding 5b: without native_px_w an enlarged copy passed on its file pixels."""
    f = Fixture()
    try:
        f.photo("hero", native_px_w="")
        code, out = f.run()
        assert code == 2 and "native_px_w is empty" in out, out
    finally:
        f.cleanup()


def test_resolution_is_counted_on_the_original_pixels():
    f = Fixture()
    try:
        f.photo("hero", native_px_w="800")  # a 1600 px file enlarged from 800 px: 128 ppi across 6.25 in
        code, out = f.run()
        assert code == 3 and re.search(r"FAIL photo-resolution: hero: .*only 128 ppi", out), out
    finally:
        f.cleanup()


def test_camera_original_is_confirmed_from_its_camera_data():
    f = Fixture()
    try:
        make_image(os.path.join(f.dir, "cam.jpg"), 1600, 1110, 9, exif={"px_w": 1600, "px_h": 1110})
        f.photo("hero", file="cam.jpg", native_px_w="", camera_original="yes")
        code, out = f.run()
        assert code == 0, out
        make_image(os.path.join(f.dir, "cam-big.jpg"), 1600, 1110, 9, exif={"px_w": 800, "px_h": 555})
        f.photo("hero", file="cam-big.jpg")
        code, out = f.run(version=2)
        assert code == 2 and "it was enlarged" in out, out
        make_image(os.path.join(f.dir, "no-exif.jpg"), 1600, 1110, 9)
        f.photo("hero", file="no-exif.jpg")
        code, out = f.run(version=2)
        assert code == 2 and "no camera data" in out, out
    finally:
        f.cleanup()


def test_enlarged_pixels_get_a_warning():
    from PIL import Image
    f = Fixture()
    try:
        make_image(os.path.join(f.dir, "small.jpg"), 800, 555, 4)
        Image.open(os.path.join(f.dir, "small.jpg")).resize((1600, 1110), Image.LANCZOS).save(os.path.join(f.dir, "blown-up.jpg"), quality=92)
        f.photo("hero", file="blown-up.jpg", native_px_w="1600")  # someone typed the file width, not the original's
        code, out = f.run("--draft")
        assert "WARN photo-enlarged: hero" in out, out
    finally:
        f.cleanup()


def test_pending_release_rows_need_a_live_check():
    page_dir = tempfile.mkdtemp(prefix="poster-live-")
    open(os.path.join(page_dir, "live.html"), "w").write("<html><body><p>Jane Doe has trained <b>2,000+</b> reps.</p></body></html>")
    open(os.path.join(page_dir, "old.html"), "w").write("<html><body><p>Coming soon.</p></body></html>")
    handler = lambda *a, **k: http.server.SimpleHTTPRequestHandler(*a, directory=page_dir, **k)
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    server.RequestHandlerClass.log_message = lambda *a: None
    threading.Thread(target=server.serve_forever, daemon=True).start()
    port = server.server_address[1]
    f = Fixture()
    try:
        for row in f.facts:  # every source is the local page, so the test never leaves this machine
            if row["claim_owner"] != "design":
                row.update(source_url=f"http://127.0.0.1:{port}/live.html", source_says="Jane Doe")
        f.fact("band.counted.1.value", status="pending-release", source_says="has trained 2,000+ reps")
        code, out = f.run()
        assert code == 2 and "pending-release" in out, out
        code, out = f.run("--live-check")
        assert code == 0, out
        f.fact("band.counted.1.value", source_url=f"http://127.0.0.1:{port}/old.html")
        code, out = f.run("--live-check", version=2)
        assert code == 2 and "not on the page yet" in out, out
    finally:
        server.shutdown()
        f.cleanup()
        shutil.rmtree(page_dir, ignore_errors=True)


def test_bleed_pdf_has_the_right_boxes_and_colors():
    f = Fixture()
    try:
        code, out = f.run("--bleed", "0.125")
        assert code == 0, out
        from pypdf import PdfReader
        r = PdfReader(os.path.join(f.out, f"Jane-Doe-Brand-Poster-18x24-bleed-v1-{DATE}.pdf"))
        page = r.pages[0]
        assert [round(float(x)) for x in page.mediabox[2:]] == [1314, 1746], page.mediabox
        assert [round(float(x)) for x in page.trimbox] == [9, 9, 1305, 1737], page.trimbox
        assert "PASS bleed-colors" in out, out
        assert os.path.exists(os.path.join(f.out, f"Jane-Doe-Brand-Poster-18x24-v1-{DATE}.pdf")), "trim-size PDF missing"
    finally:
        f.cleanup()


def main():
    tests = [(n, fn) for n, fn in sorted(globals().items()) if n.startswith("test_") and callable(fn)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"PASS {name}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL {name}: {str(e)[:1500]}")
        except Exception as e:  # environment problems show up here
            failed += 1
            print(f"ERROR {name}: {type(e).__name__}: {e}")
    print(f"{len(tests) - failed} of {len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
