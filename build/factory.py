#!/usr/bin/env python3
"""Content Factory graph, importance scoring, and model routing.

Single source of truth for:
  - the four-phase line (Produce → Process → Post → Promote)
  - gating / plumbing tasks that unblock that line
  - 1–5 importance (max of frequency, revenue, gating)
  - which engine can run which task, including a first-class single-engine path

Imported by build.py. Also runnable: python3 build/factory.py
"""
from __future__ import annotations

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

PHASES = ("Produce", "Process", "Post", "Promote")

# Supporting categories that are not one of the four phases but sit on the line.
GATE_PHASE = "Gate"

# ---------------------------------------------------------------------------
# Explicit spine. Order is the default run order an agent should follow.
# A small access task belongs here if skipping it breaks the next phase.
# ---------------------------------------------------------------------------
SPINE = {
    "Gate": [
        "verify-domain-ownership-and-registrar-access",
        "ensure-proper-dns-records",
        "configure-https-with-no-mixed-content",
        "set-up-content-library",
        "install-google-tag-manager-container",
        "set-up-ga4-with-internal-traffic-filtering",
        "verify-google-search-console-and-connect-to-ga4",
        "install-meta-pixel-with-standard-events",
        "set-up-digital-plumbing-pixels-tracking",
        "set-up-meta-business-manager-and-public-figure-pages",
        "claim-and-brand-facebook-page",
        "create-xml-sitemap-and-reference-in-robots-txt",
        "ensure-robots-meta-not-blocking-indexing",
        "ensure-working-contact-form-delivers-notifications",
        "create-clear-conversion-path",
    ],
    "Produce": [
        "map-out-one-minute-video-topics-using-topic-wheel",
        "batch-record-50-raw-clips-in-one-session",
        "record-one-minute-videos",
        "capture-client-stories-on-phone",
        "film-conference-presentations",
        "record-screen-shares-of-real-audits",
        "film-casual-team-conversations",
        "create-a-3-minute-why-video",
        "create-a-3x3-video-grid",
    ],
    "Process": [
        "step-1-upload-video-to-google-drive-and-descript",
        "step-2-transcribe-video-using-descript",
        "use-descript-underlord-to-remove-filler-words",
        "step-3-watch-video-and-identify-gct",
        "step-4-research-edit-add-timestamps-and-outline",
        "extract-15-60-second-clips-from-long-form-video",
        "create-quote-cards-from-strongest-statements",
        "step-5-write-article-from-transcript",
        "run-overnight-local-writer",
        "step-6-write-title-and-headings",
        "step-7-write-hook-and-establish-context",
        "step-8-add-photos-and-featured-image",
        "step-9-add-internal-links-with-proper-anchor-text",
        "step-10-embed-source-video",
        "step-11-proofread-with-grammarly-or-chatgpt",
        "grade-article-using-jennifer",
        "create-social-media-posts-per-platform",
        "write-email-newsletter-from-video-key-insight",
        "create-dollar-a-day-ad-creatives",
        "write-meta-article-documenting-agent-work",
        "process-videos-via-marketscale",
    ],
    "Post": [
        "step-12-post-article-on-wordpress",
        "set-wordpress-author-to-correct-person",
        "step-13-categorize-post-and-add-tags",
        "step-14a-configure-rankmath-seo-plugin",
        "step-14b-run-linkwhisper-for-internal-links",
        "place-content-on-seo-tree-with-proper-links",
        "step-17-final-formatting-and-qa-checks",
        "verify-all-items-on-blog-posting-checklist",
        "upload-processed-video-to-youtube",
        "post-to-facebook-page",
        "post-to-linkedin",
        "share-in-44k-facebook-group",
        "email-and-dm-client-about-published-article",
    ],
    "Promote": [
        "identify-signals-worth-amplifying",
        "run-dollar-a-day-campaign-on-winning-content",
        "boost-top-3-5-facebook-posts",
        "boost-one-minute-videos-for-personal-branding",
        "set-1-day-budget-per-ad-set",
        "create-facebook-instagram-campaigns-with-location-targeting",
        "create-new-saved-audiences-from-audience-insights",
        "execute-switch-boost-to-target-new-audiences",
        "execute-switch-boosts-to-new-audiences",
        "sequence-content-cold-warm-conversion",
        "sequence-content-from-awareness-to-conversion",
        "set-up-remarketing-ads-for-landing-page-abandoners",
        "run-multiple-simultaneous-tests",
        "analyze-cost-per-result-and-engagement",
        "kill-underperforming-ads",
        "scale-winners-by-increasing-budget-gradually",
        "review-budget-allocation-by-channel",
        "create-youtube-campaigns-using-aducate-model",
        "set-up-tiktok-campaigns",
        "run-twitter-x-promotion-for-thought-leader-threads",
        "engage-with-social-comments",
        "apply-metrics-decomposition",
        "compare-current-vs-last-period-performance",
        "list-top-3-5-recommendations-for-next-7-days",
        "use-dollar-a-day-to-influence-media-coverage",
    ],
}

# Evidence, not vibes. Frequency of use in the daily factory / scheduled jobs /
# ads path, revenue (ads is highest money), gating value (unblocks a chain).
# importance = max(frequency, revenue, gating). A tiny "get access" task is a 5
# when it unblocks spend or publishing.
SCORE_OVERRIDES = {
    # Gates that unblock ads or indexing — 5 even if they run once per client.
    "install-meta-pixel-with-standard-events": (4, 5, 5),
    "install-google-tag-manager-container": (4, 5, 5),
    "set-up-ga4-with-internal-traffic-filtering": (4, 4, 5),
    "verify-google-search-console-and-connect-to-ga4": (5, 4, 5),
    "set-up-digital-plumbing-pixels-tracking": (4, 5, 5),
    "set-up-meta-business-manager-and-public-figure-pages": (3, 5, 5),
    "verify-domain-ownership-and-registrar-access": (3, 3, 5),
    "ensure-proper-dns-records": (2, 3, 5),
    "configure-https-with-no-mixed-content": (2, 3, 5),
    "set-up-content-library": (5, 3, 5),
    "claim-and-brand-facebook-page": (3, 5, 5),
    "create-clear-conversion-path": (4, 5, 5),
    "ensure-working-contact-form-delivers-notifications": (4, 5, 5),
    "create-xml-sitemap-and-reference-in-robots-txt": (4, 3, 4),
    "ensure-robots-meta-not-blocking-indexing": (4, 3, 5),
    "set-up-call-tracking-for-phone-conversions": (3, 5, 4),
    "set-up-professional-email-on-domain": (2, 3, 4),
    "configure-spf-dkim-dmarc-for-deliverability": (2, 3, 4),
    # Produce — volume of raw material.
    "map-out-one-minute-video-topics-using-topic-wheel": (5, 3, 4),
    "batch-record-50-raw-clips-in-one-session": (4, 3, 3),
    "record-one-minute-videos": (5, 3, 3),
    "capture-client-stories-on-phone": (4, 3, 2),
    "film-conference-presentations": (3, 4, 2),
    # Process — Descript is the hinge.
    "step-1-upload-video-to-google-drive-and-descript": (5, 3, 5),
    "step-2-transcribe-video-using-descript": (5, 3, 5),
    "use-descript-underlord-to-remove-filler-words": (5, 2, 3),
    "step-5-write-article-from-transcript": (5, 4, 3),
    "run-overnight-local-writer": (4, 3, 2),
    "grade-article-using-jennifer": (5, 4, 4),
    "create-dollar-a-day-ad-creatives": (5, 5, 4),
    "extract-15-60-second-clips-from-long-form-video": (5, 4, 3),
    "create-social-media-posts-per-platform": (5, 4, 2),
    "step-11-proofread-with-grammarly-or-chatgpt": (5, 3, 3),
    "write-meta-article-documenting-agent-work": (5, 2, 3),
    # Post — nothing to promote if this fails.
    "step-12-post-article-on-wordpress": (5, 4, 5),
    "set-wordpress-author-to-correct-person": (5, 3, 5),
    "upload-processed-video-to-youtube": (4, 4, 3),
    "post-to-facebook-page": (5, 5, 3),
    "post-to-linkedin": (4, 4, 2),
    "place-content-on-seo-tree-with-proper-links": (5, 4, 3),
    # Promote / Dollar a Day — highest money.
    "run-dollar-a-day-campaign-on-winning-content": (5, 5, 4),
    "boost-top-3-5-facebook-posts": (5, 5, 3),
    "boost-one-minute-videos-for-personal-branding": (5, 5, 3),
    "set-1-day-budget-per-ad-set": (5, 5, 4),
    "kill-underperforming-ads": (5, 5, 4),
    "scale-winners-by-increasing-budget-gradually": (5, 5, 3),
    "execute-switch-boost-to-target-new-audiences": (5, 5, 3),
    "execute-switch-boosts-to-new-audiences": (5, 5, 3),
    "sequence-content-cold-warm-conversion": (5, 5, 4),
    "sequence-content-from-awareness-to-conversion": (5, 5, 4),
    "set-up-remarketing-ads-for-landing-page-abandoners": (4, 5, 5),
    "create-new-saved-audiences-from-audience-insights": (4, 5, 4),
    "create-facebook-instagram-campaigns-with-location-targeting": (5, 5, 4),
    "review-budget-allocation-by-channel": (4, 5, 3),
    "identify-signals-worth-amplifying": (5, 5, 4),
    "verify-prerequisites-product-customers-content": (3, 5, 5),
    "build-audience-layers": (4, 5, 4),
    "thank-you-machine/boost-with-dollar-a-day": (4, 5, 2),
    "boost-with-dollar-a-day": (4, 5, 2),
    "stage-1-plumbing-fb-ads-google-ads-analytics": (4, 5, 5),
    "stage-5-amplification-boost-posts-remarketing-ads": (5, 5, 3),
    "run-content-factory-on-any-engine": (5, 5, 5),
}

# Slug substrings → default (freq, rev, gate) when not in SCORE_OVERRIDES.
KEYWORD_SCORES = [
    (("pixel", "gtm", "tag-manager", "ads-manager", "business-manager", "remarketing"), (4, 5, 5)),
    (("dollar-a-day", "boost", "ad-set", "campaign", "audience", "lookalike"), (5, 5, 3)),
    (("descript", "transcri"), (5, 3, 5)),
    (("search-console", "gsc", "indexing", "robots"), (4, 3, 5)),
    (("wordpress", "author", "application-password", "gutenberg"), (5, 4, 5)),
    (("ga4", "analytics", "gtm"), (4, 4, 5)),
    (("dns", "domain", "https", "ssl", "registrar"), (2, 3, 5)),
    (("jennifer", "grade-article"), (5, 4, 4)),
    (("youtube", "tiktok", "linkedin", "facebook-page"), (4, 4, 2)),
    (("maa", "metrics", "budget"), (4, 4, 2)),
    (("schema", "knowledge-panel", "sameas"), (3, 3, 3)),
    (("favicon", "nap", "headshot", "bio"), (2, 2, 2)),
]

CAT_DEFAULTS = {
    "Content Factory — Produce": (3, 3, 2),
    "Content Factory — Process": (4, 3, 2),
    "Content Factory — Post": (4, 4, 2),
    "Content Factory — Promote": (4, 5, 3),
    "Digital Plumbing": (3, 3, 3),
    "Dollar a Day Campaigns": (4, 5, 3),
    "Website QA Audit": (3, 2, 3),
    "SEO & Content Architecture": (3, 3, 2),
    "Personal Branding": (3, 3, 2),
    "Strategy & Measurement": (3, 3, 2),
    "Thank You Machine": (3, 3, 2),
    "Knowledge System Maintenance": (2, 1, 2),
    "Gaps & Tasks to Create": (2, 2, 2),
}

# Engine lanes. Single-engine is first-class: Claude-only or Grok-only can run
# the whole factory if they have files + a browser. Multi-engine is optional.
LANES = {
    "script": "No model. Shell, REST, yt-dlp, Descript export, WP application-password publish.",
    "local": "Dumb local model (Qwen overnight, Ollama). First drafts and bulk rewrite only. Never hits ads, WP, or judgment.",
    "any": "Any capable chat model (Claude, ChatGPT, Grok, Gemini). SOP following, drafts, checklists.",
    "judgment": "Frontier judgment: honest scoring, entity disambiguation, the subject's voice. Claude, ChatGPT, or Grok — pick the one you have.",
    "computer": "Logged-in UI (Meta Ads Manager, Descript, GSC, wp-admin when REST is blocked). Any engine with a browser.",
}

SLUG_LANES = {
    "step-2-transcribe-video-using-descript": "computer",
    "step-1-upload-video-to-google-drive-and-descript": "computer",
    "use-descript-underlord-to-remove-filler-words": "computer",
    "step-12-post-article-on-wordpress": "script",
    "run-overnight-local-writer": "local",
    "grade-article-using-jennifer": "judgment",
    "step-5-write-article-from-transcript": "any",
    "step-11-proofread-with-grammarly-or-chatgpt": "any",
    "run-dollar-a-day-campaign-on-winning-content": "computer",
    "install-meta-pixel-with-standard-events": "computer",
    "install-google-tag-manager-container": "computer",
    "set-up-ga4-with-internal-traffic-filtering": "computer",
    "verify-google-search-console-and-connect-to-ga4": "computer",
    "set-up-meta-business-manager-and-public-figure-pages": "computer",
    "create-facebook-instagram-campaigns-with-location-targeting": "computer",
    "kill-underperforming-ads": "computer",
    "boost-top-3-5-facebook-posts": "computer",
    "execute-switch-boost-to-target-new-audiences": "computer",
    "set-up-remarketing-ads-for-landing-page-abandoners": "computer",
    "create-dollar-a-day-ad-creatives": "any",
    "extract-15-60-second-clips-from-long-form-video": "computer",
    "write-meta-article-documenting-agent-work": "any",
    "run-content-factory-on-any-engine": "any",
}

HANDOFF = {
    "Produce": "Raw files in Content Library `01-Raw/` plus a tracker row (question, date, speaker). Next skill never needs the chat — it needs the files.",
    "Process": "Write `transcript.md`, `gct.md`, `article.html` (or overnight draft), `clips/` and `04-Promote-Creatives/`. The next engine opens those files. Do not pass work through one vendor's memory.",
    "Post": "Draft URL or WP post ID, slug, author user ID, featured-image media ID. Promote reads the live URL, not the draft.",
    "Promote": "Organic metrics CSV (or Ads Manager export), pixel ID, creative filenames, kill/scale log. Next week's ranking starts from this file.",
    "Gate": "Record the property IDs (GTM-…, G-…, pixel, GSC) in the client access register. Nothing ships until those IDs exist.",
}

DOCTRINE = (
    "People who arrive with ONLY Grok or ONLY Claude still run the whole factory. "
    "The playbook does not fork by vendor. Multi-engine (local Qwen overnight + Claude "
    "voice pass + ChatGPT proofread) is optional sophistication that scales the SAME "
    "line. Bridge through files, never through one vendor's memory."
)

MARKER_START = "<!-- factory-layer:start -->"
MARKER_END = "<!-- factory-layer:end -->"


def _index_spine():
    pos = {}
    phase_of = {}
    for phase, slugs in SPINE.items():
        for i, slug in enumerate(slugs):
            pos[slug] = (phase, i)
            phase_of[slug] = phase
    return pos, phase_of


SPINE_POS, SPINE_PHASE = _index_spine()


def parse_siblings(text: str):
    """Return ordered slug list from 'Sibling skills, in run order' or 'Run order' lines."""
    if not text:
        return []
    out = []
    for line in text.splitlines():
        if "in run order" in line.lower() or line.lower().lstrip("- ").startswith("run order"):
            found = re.findall(r"`([a-z0-9][a-z0-9-]{3,})`", line)
            out.extend(found)
    # de-dupe preserve order
    seen, uniq = set(), []
    for s in out:
        if s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq


def keyword_hit(slug: str, key: str) -> bool:
    """Hyphen-token match so 'author' does not fire inside 'authoritative'."""
    s = (slug or "").lower()
    k = (key or "").lower()
    if not k:
        return False
    if "-" in k:
        return k in s
    parts = s.split("-")
    if k in parts:
        return True
    # Intentional stems (transcri → transcribe / transcription).
    if k in {"transcri"}:
        return any(p.startswith(k) for p in parts)
    return False


def score_tuple(slug: str, category: str, stage: str):
    if slug in SCORE_OVERRIDES:
        return SCORE_OVERRIDES[slug]
    for keys, trip in KEYWORD_SCORES:
        if any(keyword_hit(slug, k) for k in keys):
            return trip
    if category in CAT_DEFAULTS:
        return CAT_DEFAULTS[category]
    if stage in PHASES:
        return CAT_DEFAULTS.get("Content Factory — " + stage, (3, 3, 2))
    return (2, 2, 2)


def importance(freq, rev, gate):
    return max(int(freq), int(rev), int(gate))


def factory_phase(slug: str, stage: str, category: str):
    if slug in SPINE_PHASE:
        return SPINE_PHASE[slug]
    if stage in PHASES:
        return stage
    if category.startswith("Content Factory"):
        for p in PHASES:
            if p.lower() in category.lower():
                return p
    if category in ("Digital Plumbing", "Dollar a Day Campaigns"):
        return "Gate" if category == "Digital Plumbing" else "Promote"
    if "dollar a day" in (category or "").lower():
        return "Promote"
    return GATE_PHASE if category == "Digital Plumbing" else (stage if stage in PHASES else "—")


def lane_for(slug: str, stage: str, category: str, phase: str):
    if slug in SLUG_LANES:
        return SLUG_LANES[slug]
    low = slug.lower()
    if any(k in low for k in ("pixel", "gtm", "ads-manager", "business-manager", "boost",
                              "campaign", "descript", "search-console", "ga4")):
        return "computer"
    if any(k in low for k in ("xml-sitemap", "robots", "favicon", "https", "dns")):
        return "script"
    if any(k in low for k in ("grade", "jennifer", "voice", "entity", "knowledge-panel")):
        return "judgment"
    if "overnight" in low or "local-writer" in low:
        return "local"
    if phase == "Promote" or "dollar" in low:
        return "computer"
    if phase == "Post" and "wordpress" in low:
        return "script"
    if phase in ("Produce", "Process"):
        return "any"
    return "any"


def neighbors(slug: str, phase: str, siblings: list):
    """before / after slugs. Prefer spine, then sibling line."""
    before = after = None
    if slug in SPINE_POS:
        ph, i = SPINE_POS[slug]
        seq = SPINE[ph]
        if i > 0:
            before = seq[i - 1]
        if i + 1 < len(seq):
            after = seq[i + 1]
        # Phase handoff: last of Produce → first of Process, etc.
        if after is None:
            order = ["Gate", "Produce", "Process", "Post", "Promote"]
            if ph in order:
                nxt = order[order.index(ph) + 1] if order.index(ph) + 1 < len(order) else None
                if nxt and SPINE.get(nxt):
                    after = SPINE[nxt][0]
        if before is None:
            order = ["Gate", "Produce", "Process", "Post", "Promote"]
            if ph in order and order.index(ph) > 0:
                prev = order[order.index(ph) - 1]
                if SPINE.get(prev):
                    before = SPINE[prev][-1]
    if siblings and slug in siblings:
        i = siblings.index(slug)
        if i > 0:
            before = before or siblings[i - 1]
        if i + 1 < len(siblings):
            after = after or siblings[i + 1]
    elif siblings:
        # slug not in the list; treat list as context
        if not before and siblings:
            before = siblings[0]
        if not after and len(siblings) > 1:
            after = siblings[-1]
    return before, after


def annotate(slug: str, category: str, stage: str, content: str = ""):
    freq, rev, gate = score_tuple(slug, category, stage or "")
    imp = importance(freq, rev, gate)
    phase = factory_phase(slug, stage or "", category or "")
    siblings = parse_siblings(content or "")
    before, after = neighbors(slug, phase, siblings)
    lane = lane_for(slug, stage or "", category or "", phase)
    why = []
    if freq >= 4:
        why.append("runs every factory cycle or weekly")
    if rev >= 5:
        why.append("ads/revenue path")
    elif rev >= 4:
        why.append("creates the asset ads amplify")
    if gate >= 5:
        why.append("unblocks a chain (access/plumbing)")
    elif gate >= 4:
        why.append("gates a phase")
    return {
        "importance": imp,
        "freq": freq,
        "revenue": rev,
        "gating": gate,
        "phase": phase if phase in PHASES or phase == GATE_PHASE else "—",
        "before": before,
        "after": after,
        "lane": lane,
        "lane_label": LANES.get(lane, lane),
        "why": "; ".join(why) or "supporting",
        "handoff": HANDOFF.get(phase if phase in HANDOFF else stage, HANDOFF.get("Process")),
    }


def layer_markdown(slug: str, rec: dict) -> str:
    """Idempotent block inserted into every skill.md so an agent sees the chain."""
    def tick(n, filled):
        return "●" * filled + "○" * (n - filled)

    def link(s):
        return f"`{s}`" if s else "—"

    lines = [
        MARKER_START,
        "",
        "## Factory chain (do not treat this as isolated)",
        "",
        f"- **Phase:** {rec['phase']}",
        f"- **Importance:** {rec['importance']}/5 `{tick(5, rec['importance'])}` — frequency {rec['freq']}, revenue {rec['revenue']}, gating {rec['gating']} ({rec['why']})",
        f"- **Before:** {link(rec['before'])}",
        f"- **After:** {link(rec['after'])}",
        f"- **Handoff:** {rec['handoff']}",
        "",
        "## Model routing (same factory, any engine)",
        "",
        f"- **This task's lane:** `{rec['lane']}` — {rec['lane_label']}",
        "- **Single-engine path:** If you only have Grok, or only have Claude, run this task anyway. Do not wait for a second vendor. Pass the handoff files to the next skill in this same engine.",
        "- **Optional multi-engine:** local/Qwen can draft Process writing overnight; a frontier model (Claude, ChatGPT, or Grok) does Jennifer + voice; scripts publish. That is the same line, not a second playbook.",
        "- **Never** store the working state in one vendor's memory. Files in the Content Library are the bridge.",
        "",
        MARKER_END,
    ]
    return "\n".join(lines)


def apply_layer(text: str, block: str) -> str:
    if MARKER_START in text and MARKER_END in text:
        return re.sub(
            re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
            block.strip(),
            text,
            count=1,
            flags=re.S,
        )
    # Insert before Definitive article heading, else before trailing Run-on-persistent, else append.
    m = re.search(r"\n## Definitive article", text)
    if m:
        return text[: m.start()] + "\n\n" + block + "\n" + text[m.start() + 1 :]
    m = re.search(r"\n## Run on a persistent agent", text)
    if m:
        return text[: m.start()] + "\n\n" + block + "\n" + text[m.start() + 1 :]
    return text.rstrip() + "\n\n" + block + "\n"


def write_incomplete_inventory(tasks, path):
    """Full inventory of needs-work + gap rows. Never a sample."""
    rows = [t for t in tasks if t.get("status") in ("needs-work", "gap")]
    rows.sort(key=lambda t: (-int(t.get("importance") or 0), t.get("status") or "", t.get("slug") or ""))
    stats = {
        "total": len(tasks),
        "complete": sum(t.get("status") == "complete" for t in tasks),
        "needsWork": sum(t.get("status") == "needs-work" for t in tasks),
        "gaps": sum(t.get("status") == "gap" for t in tasks),
    }
    dist = {i: sum(int(t.get("importance") or 0) == i for t in tasks) for i in range(1, 6)}
    lines = [
        "# Task Library incomplete inventory",
        "",
        f"Generated from `build/build.py` after scoring in `build/factory.py`.",
        "",
        f"Library: **{stats['total']}** tasks — {stats['complete']} complete, "
        f"{stats['needsWork']} needs-work, {stats['gaps']} gaps.",
        "",
        f"Importance distribution: 5★={dist[5]}, 4★={dist[4]}, 3★={dist[3]}, 2★={dist[2]}, 1★={dist[1]}",
        "",
        "Scoring: `importance = max(frequency, revenue, gating)`. Ads, pixels, GSC, Descript, "
        "WP-author, and Meta BM are 5s even when the task is small, because they unblock the line.",
        "",
        f"Incomplete: **{len(rows)}**. This file is the work order. Do not re-sample.",
        "",
        "| ★ | Status | Phase | Category | Slug | Lane | Why |",
        "|---|---|---|---|---|---|---|",
    ]
    for t in rows:
        lines.append(
            f"| {t.get('importance') or ''} | {t.get('status')} | {t.get('phase') or '—'} | "
            f"{t.get('category') or ''} | `{t.get('slug')}` | {t.get('lane') or ''} | "
            f"{(t.get('why') or '').replace('|', '/')} |"
        )
    lines.append("")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return len(rows)


def factory_meta():
    return {
        "phases": [
            {
                "id": "Gate",
                "label": "Gate / Plumbing",
                "blurb": "Access, pixels, GSC, GTM, GA4, Meta BM. A $1/day campaign with no pixel is money you cannot follow.",
                "color": "#8b5cf6",
            },
            {
                "id": "Produce",
                "label": "1 · Produce (gather)",
                "blurb": "Record once. Topic Wheel questions, one-minute videos, conference clips, batch sessions.",
                "color": "#f59e0b",
            },
            {
                "id": "Process",
                "label": "2 · Process (Descript)",
                "blurb": "Transcribe, clean filler, GCT, write the hub, cut clips, grade with Jennifer, cut ad creatives.",
                "color": "#f97316",
            },
            {
                "id": "Post",
                "label": "3 · Post",
                "blurb": "WordPress (right author), YouTube, Facebook, LinkedIn, SEO Tree. Draft URL is the handoff.",
                "color": "#3b82f6",
            },
            {
                "id": "Promote",
                "label": "4 · Promote (ads)",
                "blurb": "Boost only proven organic. $1/day × 7, kill the bottom 90%, $30/30 on winners. Highest money.",
                "color": "#14b8a6",
            },
        ],
        "doctrine": DOCTRINE,
        "lanes": LANES,
        "scoring": (
            "Importance is max(frequency, revenue, gating), scored 1–5 from evidence: "
            "daily factory / scheduled jobs, ads-and-pixel revenue path, and tasks that "
            "unblock a chain (a small get-access task can be a 5)."
        ),
    }


def main():
    """Print a coverage report against the local skills tree."""
    root = os.path.join(os.path.dirname(HERE), "skills")
    n = 0
    dist = {i: 0 for i in range(1, 6)}
    for dirpath, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            slug = fn[:-3]
            n += 1
            # category from folder is approximate; build.py uses registry
            rec = annotate(slug, "", "")
            dist[rec["importance"]] += 1
    print(f"skills={n} importance_dist={dist}")
    print("spine", {k: len(v) for k, v in SPINE.items()})


if __name__ == "__main__":
    main()
