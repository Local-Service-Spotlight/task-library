import copy
import unittest
import teaching_materials as tm


class MaterialsTests(unittest.TestCase):
    def setUp(self):
        self.paths = [{"id": "content-factory"}]
        self.material = {"id": "tampa-card", "title": "Fictional exercise", "kind": "exercise",
                         "access": "public", "url": "https://dennisyu.com/tampa/task-card.md",
                         "sourceOwner": "Existing workshop owner", "sourceVersion": "2026.1",
                         "checkedAt": "2026-10-14T00:00:00Z", "useNote": "Fictional practice only.",
                         "pathIds": ["content-factory"], "verification": {"method": "anonymous-get", "status": 200, "sha256": "a" * 64}}
        self.session = {"id": "practice", "title": "Practice", "pathId": "content-factory",
                        "audience": "Growth operators", "goal": "Checked fictional drafts", "minutes": 60,
                        "materialIds": ["tampa-card"], "steps": [{"title": "Read", "instruction": "Read the card.", "materialIds": ["tampa-card"]}],
                        "deliverable": "Saved files", "checks": ["Fictional inputs only"], "sourceVersion": "1"}
        self.source = {"teachingMaterials": [self.material], "practiceSessions": [self.session]}

    def test_valid_and_stable_recipe_hash(self):
        a, b = tm.compose(self.source, self.paths)
        self.assertEqual(a, [self.material])
        self.assertRegex(b[0]["contentSha256"], "^[a-f0-9]{64}$")
        self.assertEqual(b, tm.compose(copy.deepcopy(self.source), self.paths)[1])

    def test_recipe_hash_changes_with_check(self):
        old = tm.compose(self.source, self.paths)[1][0]["contentSha256"]
        self.session["checks"].append("Reopen outputs")
        self.assertNotEqual(old, tm.compose(self.source, self.paths)[1][0]["contentSha256"])

    def test_backwards_compatible_empty(self):
        self.assertEqual(tm.compose({}, self.paths), ([], []))

    def test_reject_private_fields(self):
        for key in ["instructorKey", "paidBody", "protectedUrl", "credentials", "html"]:
            with self.subTest(key=key):
                source = copy.deepcopy(self.source)
                source["teachingMaterials"][0][key] = "SECRET"
                with self.assertRaises(ValueError): tm.compose(source, self.paths)

    def test_reject_nonpublic_urls(self):
        for url in ["http://dennisyu.com/tampa/", "https://docs.google.com/document/d/private",
                    "https://dennisyu.com/tampa/?token=secret", "https://u:p@dennisyu.com/tampa/",
                    "https://dennisyu.com/private/file.pdf", "https://dennisyu.com:443/tampa/",
                    "https://dennisyu.com/%70rivate/file", "https://dennisyu.com/lessons/paid/"]:
            with self.subTest(url=url):
                self.material["url"] = url
                with self.assertRaises(ValueError): tm.compose(self.source, self.paths)

    def test_course_entry_is_link_only(self):
        self.material.update(kind="course", access="protected-entry", url="https://blitzmetrics.com/ntf/")
        self.source["practiceSessions"] = []
        self.assertEqual(tm.compose(self.source, self.paths)[0][0]["access"], "protected-entry")

    def test_course_cannot_be_public_asset(self):
        self.material["kind"] = "course"
        with self.assertRaises(ValueError): tm.compose(self.source, self.paths)

    def test_protected_file_forbidden(self):
        self.material.update(kind="course", access="protected-entry", url="https://blitzmetrics.com/wp-content/uploads/paid.pdf")
        with self.assertRaises(ValueError): tm.compose(self.source, self.paths)

    def test_public_session_cannot_depend_on_paid_entry(self):
        self.material.update(kind="course", access="protected-entry", url="https://blitzmetrics.com/ntf/")
        with self.assertRaises(ValueError): tm.compose(self.source, self.paths)

    def test_failed_or_malformed_check_rejected(self):
        for change in [{"status": 403}, {"status": True}, {"sha256": "unknown"}, {"method": "owner-report"}, {"private": "data"}]:
            with self.subTest(change=change):
                source = copy.deepcopy(self.source)
                source["teachingMaterials"][0]["verification"].update(change)
                with self.assertRaises(ValueError): tm.compose(source, self.paths)

    def test_missing_timezone_rejected(self):
        self.material["checkedAt"] = "2026-10-14"
        with self.assertRaises(ValueError): tm.compose(self.source, self.paths)

    def test_reference_validation(self):
        for field in ["pathIds", "id"]:
            source = copy.deepcopy(self.source)
            source["teachingMaterials"][0][field] = ["missing"] if field == "pathIds" else "tampa card"
            with self.assertRaises(ValueError): tm.compose(source, self.paths)

    def test_duplicate_materials_rejected(self):
        self.source["teachingMaterials"].append(copy.deepcopy(self.material))
        with self.assertRaises(ValueError): tm.compose(self.source, self.paths)

    def test_unresolved_session_material_rejected(self):
        self.session["materialIds"] = ["missing"]
        with self.assertRaises(ValueError): tm.compose(self.source, self.paths)

    def test_wrong_audience_path_rejected(self):
        self.material["pathIds"] = []
        with self.assertRaises(ValueError): tm.compose(self.source, self.paths)

    def test_unresolved_step_rejected(self):
        self.session["steps"][0]["materialIds"] = ["missing"]
        with self.assertRaises(ValueError): tm.compose(self.source, self.paths)

    def test_private_recipe_fields_rejected(self):
        self.session["answerKey"] = "secret"
        with self.assertRaises(ValueError): tm.compose(self.source, self.paths)

    def test_plain_text_only(self):
        self.material["title"] = "<script>alert(1)</script>"
        with self.assertRaises(ValueError): tm.compose(self.source, self.paths)

    def test_exact_youtube_watch_link(self):
        tm.public_url("https://www.youtube.com/watch?v=NTSx7lUoJ-Q")
        for url in ["https://www.youtube.com/watch?v=NTSx7lUoJ-Q&token=x", "https://youtu.be/not-an-id", "https://www.youtube.com/account"]:
            with self.assertRaises(ValueError): tm.public_url(url)


if __name__ == "__main__": unittest.main()
