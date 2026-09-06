#!/usr/bin/env python3
"""Keep the credibility-voice publish gates attached to their canonical owners."""
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path):
    return (ROOT / relative_path).read_text(encoding="utf-8")


class CredibilityVoiceGuidelines(unittest.TestCase):
    def test_drafting_owner_keeps_scene_and_relationship_rules(self):
        content = read("skills/content-factory-process/step-5-write-article-from-transcript.md")
        for phrase in (
            "Show the moment, not the resume",
            "trophy-name paragraph",
            "Make relationship language no stronger than the evidence",
            "internal verification process",
            "remains **HOLD**",
        ):
            self.assertIn(phrase, content)

    def test_jennifer_keeps_hard_publish_caps(self):
        content = read("skills/content-factory-process/grade-article-using-jennifer.md")
        for phrase in (
            "A score never overrides a failed proof",
            "Trophy-name paragraph",
            "Relationship noun outruns the evidence",
            "Repeated defensive caveats or verification theater",
            "Public copy exposes internal scoring or production metadata",
            "attributed only to a domain/company",
        ):
            self.assertIn(phrase, content)

    def test_post_gate_covers_public_copy_and_compliance_exception(self):
        content = read("skills/content-factory-post/verify-all-items-on-blog-posting-checklist.md")
        for phrase in (
            "first person on a personal-brand site",
            "no trophy-name paragraph",
            "no repeated defensive caveats",
            "domain/company-only attribution fail publication",
            "materially necessary legal, regulatory, or compliance disclosure",
        ):
            self.assertIn(phrase, content)

    def test_sitewide_owners_keep_proof_and_hold_rules(self):
        achievements = read(
            "skills/website-qa-audit/verify-achievements-are-evidenced-not-just-claimed.md"
        )
        photos = read("skills/website-qa-audit/verify-social-proof-photos-present.md")
        for content in (achievements, photos):
            self.assertIn("trophy-name", content)
            self.assertIn("relationship", content.lower())
            self.assertIn("HOLD", content)
            self.assertIn("repurposing", content)
            self.assertIn("compliance disclosure", content)


if __name__ == "__main__":
    unittest.main()
