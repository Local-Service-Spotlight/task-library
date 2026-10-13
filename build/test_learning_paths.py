import copy
import hashlib
import json
import unittest
from pathlib import Path
import learning_paths as lp

ROOT = Path(__file__).resolve().parent.parent

class LearningPaths(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "dashboard/data.json").read_text())
        self.source = json.loads((ROOT / "build/packs.json").read_text())

    def test_actual_five_paths_resolve(self):
        out = lp.compose(self.data, self.source)
        self.assertEqual(len(out["paths"]), 5)
        self.assertEqual(len(out["tasks"]), self.data["stats"]["total"])

    def test_existing_packs_unchanged(self):
        self.assertEqual([p["id"] for p in self.source["packs"]],
            ["wichita-google-ads", "dealcon", "website-qa", "digital-plumbing", "dollar-a-day"])

    def test_no_private_fields_or_raw_body(self):
        t = self.data["categories"][0]["tasks"][0]
        t["privateReview"] = "PRIVATE-SENTINEL"
        t["content"] += "\nPRIVATE-BODY-SENTINEL"
        public = json.dumps(lp.compose(self.data, self.source))
        self.assertNotIn("PRIVATE-SENTINEL", public)
        self.assertNotIn("PRIVATE-BODY-SENTINEL", public)
        self.assertNotIn('"content":', public)

    def test_task_content_change_changes_pin(self):
        before = lp.compose(self.data, self.source)
        t = self.data["categories"][0]["tasks"][0]
        t["content"] += "\nchanged"
        after = lp.compose(self.data, self.source)
        a = {x["slug"]: x for x in after["tasks"]}
        b = {x["slug"]: x for x in before["tasks"]}
        self.assertNotEqual(a[t["slug"]]["contentSha256"], b[t["slug"]]["contentSha256"])

    def test_no_status_promotion(self):
        out = lp.compose(self.data, self.source)
        source = {t["slug"]: t for c in self.data["categories"] for t in c["tasks"]}
        self.assertTrue(all(t["status"] == source[t["slug"]]["status"] for t in out["tasks"]))

    def bad(self, change):
        change(self.source["learningPaths"][0])
        with self.assertRaises(ValueError):
            lp.compose(self.data, self.source)

    def test_missing_lesson_rejected(self):
        self.bad(lambda p: p["lessonSlugs"].append("not-a-real-task"))
    def test_duplicate_lesson_rejected(self):
        self.bad(lambda p: p["lessonSlugs"].append(p["lessonSlugs"][0]))
    def test_unknown_framework_alias_rejected(self):
        self.bad(lambda p: p.update(governingTriangle="ACC"))
    def test_unknown_private_field_rejected(self):
        self.bad(lambda p: p.update(instructorAnswers="secret"))
    def test_empty_audience_rejected(self):
        self.bad(lambda p: p.update(audience=""))
    def test_non_plain_metadata_rejected(self):
        self.bad(lambda p: p.update(goal="<script>alert(1)</script>"))
    def test_invalid_path_id_rejected(self):
        self.bad(lambda p: p.update(id="../paid-course"))
    def test_invalid_session_time_rejected(self):
        self.bad(lambda p: p.update(sessionMinutes=True))
    def test_missing_prerequisites_rejected(self):
        self.bad(lambda p: p.update(prerequisites=[]))
    def test_private_exercise_fields_rejected(self):
        self.bad(lambda p: p["exercise"].update(answerKey="private"))
    def test_duplicate_path_rejected(self):
        self.source["learningPaths"].append(copy.deepcopy(self.source["learningPaths"][0]))
        with self.assertRaises(ValueError):
            lp.compose(self.data, self.source)
    def test_dangerous_source_link_rejected(self):
        self.data["categories"][0]["tasks"][0]["article"] = "javascript:alert(1)"
        with self.assertRaises(ValueError):
            lp.compose(self.data, self.source)
    def test_source_credentials_rejected(self):
        self.data["categories"][0]["tasks"][0]["article"] = "https://name:secret@example.com"
        with self.assertRaises(ValueError):
            lp.compose(self.data, self.source)
    def test_unknown_article_has_task_link(self):
        t = self.data["categories"][0]["tasks"][0]
        t["article"] = None
        t.pop("taskLibraryUrl", None)
        out = next(x for x in lp.compose(self.data, self.source)["tasks"] if x["slug"] == t["slug"])
        self.assertIsNone(out["article"])
        self.assertIn("?task=" + t["slug"], out["taskLibraryUrl"])
    def test_deterministic_output(self):
        self.assertEqual(lp.compose(self.data, self.source), lp.compose(self.data, self.source))
    def test_framework_names_exact(self):
        self.assertEqual(lp.FRAMEWORK["version"], "2026-08-06")
        self.assertEqual(lp.FRAMEWORK["acceptanceStatus"], "Accepted by framework owner Dennis Yu.")
        self.assertEqual(lp.FRAMEWORK["decisionDate"], "2026-08-09")
        self.assertEqual(lp.FRAMEWORK["acceptingCommit"], "3a82b85071e47a9e4ee336cec854d3e004ff0c5f")
        self.assertEqual(lp.TRIANGLES, {
            "SBP": ["Specialist", "Business", "Partner"],
            "AEC": ["Audience", "Engagement", "Conversion"],
            "GCT": ["Goals", "Content", "Targeting"],
            "MAA": ["Metrics", "Analysis", "Action"],
            "DDD": ["Do", "Delegate", "Delete"],
            "CID": ["Communicate", "Iterate", "Delegate"],
            "LDT": ["Learn", "Do", "Teach"],
            "CCS": ["Content", "Checklist", "Software"],
            "MOF": ["Marketing", "Operations", "Finance"],
        })

if __name__ == "__main__":
    unittest.main()
