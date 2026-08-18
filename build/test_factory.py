#!/usr/bin/env python3
"""Lock factory scoring, spine coverage, and layer insertion."""
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import factory  # noqa: E402


class FactoryScoring(unittest.TestCase):
    def test_ads_is_five(self):
        rec = factory.annotate("run-dollar-a-day-campaign-on-winning-content",
                               "Content Factory — Promote", "Promote")
        self.assertEqual(rec["importance"], 5)
        self.assertEqual(rec["revenue"], 5)
        self.assertEqual(rec["phase"], "Promote")

    def test_small_gate_can_be_five(self):
        rec = factory.annotate("install-meta-pixel-with-standard-events",
                               "Digital Plumbing", "—")
        self.assertEqual(rec["importance"], 5)
        self.assertEqual(rec["gating"], 5)
        self.assertEqual(rec["phase"], "Gate")

    def test_gsc_is_five(self):
        rec = factory.annotate("verify-google-search-console-and-connect-to-ga4",
                               "Digital Plumbing", "—")
        self.assertEqual(rec["importance"], 5)

    def test_author_does_not_match_authoritative(self):
        rec = factory.annotate(
            "build-external-backlinks-from-authoritative-sources",
            "SEO & Content Architecture", "—")
        self.assertLessEqual(rec["importance"], 3)
        self.assertFalse(factory.keyword_hit(
            "build-external-backlinks-from-authoritative-sources", "author"))
        self.assertTrue(factory.keyword_hit(
            "set-wordpress-author-to-correct-person", "author"))

    def test_favicon_is_not_five(self):
        rec = factory.annotate("set-favicon", "Digital Plumbing", "—")
        self.assertLessEqual(rec["importance"], 3)

    def test_knowledge_maintenance_is_low(self):
        rec = factory.annotate("audit-this-maintenance-article-every-6-months",
                               "Knowledge System Maintenance", "—")
        self.assertLessEqual(rec["importance"], 3)

    def test_descript_is_gate_and_frequent(self):
        rec = factory.annotate("step-2-transcribe-video-using-descript",
                               "Content Factory — Process", "Process")
        self.assertEqual(rec["importance"], 5)
        self.assertEqual(rec["phase"], "Process")
        self.assertEqual(rec["lane"], "computer")

    def test_importance_in_range(self):
        for slug, cat in (
            ("record-one-minute-videos", "Content Factory — Produce"),
            ("step-12-post-article-on-wordpress", "Content Factory — Post"),
            ("maa-cycle-metrics-analysis-action", "Strategy & Measurement"),
        ):
            rec = factory.annotate(slug, cat, "")
            self.assertIn(rec["importance"], (1, 2, 3, 4, 5))

    def test_spine_neighbors(self):
        rec = factory.annotate("step-2-transcribe-video-using-descript",
                               "Content Factory — Process", "Process")
        self.assertEqual(rec["before"], "step-1-upload-video-to-google-drive-and-descript")
        self.assertEqual(rec["after"], "use-descript-underlord-to-remove-filler-words")

    def test_layer_idempotent(self):
        rec = factory.annotate("set-favicon", "Digital Plumbing", "—")
        block = factory.layer_markdown("set-favicon", rec)
        text = "# Set favicon\n\n## Definitive article & links\n- Hub: /digital-plumbing\n"
        once = factory.apply_layer(text, block)
        twice = factory.apply_layer(once, block)
        self.assertEqual(once.count(factory.MARKER_START), 1)
        self.assertEqual(twice.count(factory.MARKER_START), 1)
        self.assertIn("Importance:", twice)

    def test_parse_siblings(self):
        md = "Sibling skills, in run order: `alpha-task` → this → `beta-task`"
        self.assertEqual(factory.parse_siblings(md), ["alpha-task", "beta-task"])

    def test_doctrine_mentions_single_engine(self):
        self.assertIn("ONLY Grok", factory.DOCTRINE)
        self.assertIn("ONLY Claude", factory.DOCTRINE)

    def test_meta_has_four_plus_gate(self):
        ids = [p["id"] for p in factory.factory_meta()["phases"]]
        self.assertEqual(ids, ["Gate", "Produce", "Process", "Post", "Promote"])


if __name__ == "__main__":
    unittest.main()
