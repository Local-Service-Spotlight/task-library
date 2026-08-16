#!/usr/bin/env python3
"""Tests for build_ownership_map.py.  Run:  python3 -m unittest -v

Standard library only, no network. The API layer is exercised through a fake
urlopen so pagination, retries and rate-limit handling are covered without
touching GitHub.
"""

import io
import json
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).parent))

import build_ownership_map as m  # noqa: E402


# --------------------------------------------------------------------------
# CODEOWNERS parsing
# --------------------------------------------------------------------------

class TestParseCodeowners(unittest.TestCase):
    def test_root_star(self):
        self.assertEqual(m.parse_codeowners("* @danielg"), "danielg")

    def test_ignores_comments_and_blanks(self):
        text = "# owners\n\n   # another\n*   @dennisyu\n"
        self.assertEqual(m.parse_codeowners(text), "dennisyu")

    def test_trailing_comment_on_rule(self):
        self.assertEqual(m.parse_codeowners("* @josh  # primary"), "josh")

    def test_subdirectory_rule_is_not_repo_ownership(self):
        self.assertIsNone(m.parse_codeowners("/docs/ @josh\n/src/ @austin"))

    def test_root_rule_wins_over_later_subdir_rule(self):
        self.assertEqual(m.parse_codeowners("/docs/ @josh\n* @austin"), "austin")

    def test_first_root_rule_wins(self):
        self.assertEqual(m.parse_codeowners("* @first\n* @second"), "first")

    def test_team_handle_skipped_individual_used(self):
        self.assertEqual(m.parse_codeowners("* @org/platform @dennisyu"), "dennisyu")

    def test_email_owner_is_not_a_handle(self):
        self.assertIsNone(m.parse_codeowners("* dennis@localservicespotlight.com"))

    def test_pattern_with_no_owner(self):
        self.assertIsNone(m.parse_codeowners("*"))

    def test_empty_and_none(self):
        self.assertIsNone(m.parse_codeowners(""))
        self.assertIsNone(m.parse_codeowners(None))

    def test_slash_and_glob_root_forms(self):
        for pattern in ("/", "/*", "**"):
            self.assertEqual(m.parse_codeowners(f"{pattern} @who"), "who", pattern)


class TestSlugify(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(m.slugify("Dennis Yu"), "dennis-yu")

    def test_punctuation_and_case(self):
        self.assertEqual(m.slugify("Goodrich-Dev"), "goodrich-dev")
        self.assertEqual(m.slugify("a..b__c"), "a-b-c")

    def test_degenerate_input(self):
        self.assertEqual(m.slugify(""), "unknown")
        self.assertEqual(m.slugify("---"), "unknown")
        self.assertEqual(m.slugify(None), "unknown")


class TestNextLink(unittest.TestCase):
    def test_finds_next(self):
        h = '<https://api.github.com/x?page=2>; rel="next", <https://api.github.com/x?page=9>; rel="last"'
        self.assertEqual(m._next_link(h), "https://api.github.com/x?page=2")

    def test_no_next_when_only_last_and_prev(self):
        h = '<https://api.github.com/x?page=1>; rel="prev", <https://api.github.com/x?page=9>; rel="last"'
        self.assertIsNone(m._next_link(h))

    def test_empty(self):
        self.assertIsNone(m._next_link(""))
        self.assertIsNone(m._next_link(None))


# --------------------------------------------------------------------------
# HTTP layer, with a fake urlopen
# --------------------------------------------------------------------------

class FakeResponse(io.BytesIO):
    def __init__(self, payload, link="", status=200):
        super().__init__(json.dumps(payload).encode())
        self.status = status
        self.headers = {"Link": link}

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()
        return False


def http_error(code, headers=None):
    return urllib.error.HTTPError(
        "https://api.github.com/x", code, "boom", headers or {}, None)


class TestApiGet(unittest.TestCase):
    def test_returns_payload_and_link(self):
        with mock.patch.object(m.urllib.request, "urlopen",
                               return_value=FakeResponse([{"a": 1}], link="L")):
            payload, link = m.api_get("/x", "tok")
        self.assertEqual(payload, [{"a": 1}])
        self.assertEqual(link, "L")

    def test_sends_auth_and_version_headers(self):
        seen = {}

        def fake(req, timeout=None):
            seen.update(req.headers)
            return FakeResponse([])

        with mock.patch.object(m.urllib.request, "urlopen", side_effect=fake):
            m.api_get("/x", "sekrit")
        # urllib title-cases header keys
        self.assertEqual(seen.get("Authorization"), "Bearer sekrit")
        self.assertIn("X-github-api-version", seen)

    def test_404_allowed_returns_none(self):
        with mock.patch.object(m.urllib.request, "urlopen",
                               side_effect=http_error(404)):
            payload, _ = m.api_get("/missing", "tok", allow_404=True)
        self.assertIsNone(payload)

    def test_404_not_allowed_raises(self):
        with mock.patch.object(m.urllib.request, "urlopen",
                               side_effect=http_error(404)):
            with self.assertRaises(m.ApiError):
                m.api_get("/missing", "tok")

    def test_retries_on_500_then_succeeds(self):
        seq = [http_error(500), FakeResponse([{"ok": True}])]

        def fake(req, timeout=None):
            nxt = seq.pop(0)
            if isinstance(nxt, Exception):
                raise nxt
            return nxt

        with mock.patch.object(m.urllib.request, "urlopen", side_effect=fake), \
             mock.patch.object(m.time, "sleep"):
            payload, _ = m.api_get("/x", "tok")
        self.assertEqual(payload, [{"ok": True}])

    def test_gives_up_after_retries(self):
        with mock.patch.object(m.urllib.request, "urlopen",
                               side_effect=http_error(503)), \
             mock.patch.object(m.time, "sleep"):
            with self.assertRaises(m.ApiError):
                m.api_get("/x", "tok", retries=2)

    def test_honours_retry_after_on_429(self):
        seq = [http_error(429, {"Retry-After": "7"}), FakeResponse([1])]
        slept = []

        def fake(req, timeout=None):
            nxt = seq.pop(0)
            if isinstance(nxt, Exception):
                raise nxt
            return nxt

        with mock.patch.object(m.urllib.request, "urlopen", side_effect=fake), \
             mock.patch.object(m.time, "sleep", side_effect=slept.append):
            m.api_get("/x", "tok")
        self.assertEqual(slept, [7])

    def test_403_without_rate_limit_headers_raises_immediately(self):
        with mock.patch.object(m.urllib.request, "urlopen",
                               side_effect=http_error(403)):
            with self.assertRaises(m.ApiError):
                m.api_get("/x", "tok")

    def test_empty_body_returns_empty_list(self):
        class Empty(io.BytesIO):
            status = 204
            headers = {"Link": ""}

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        with mock.patch.object(m.urllib.request, "urlopen", return_value=Empty(b"")):
            payload, _ = m.api_get("/x", "tok")
        self.assertEqual(payload, [])


class TestApiPaged(unittest.TestCase):
    def test_follows_next_links(self):
        pages = [
            FakeResponse([1, 2], link='<https://api.github.com/x?page=2>; rel="next"'),
            FakeResponse([3], link=""),
        ]
        with mock.patch.object(m.urllib.request, "urlopen",
                               side_effect=lambda *a, **k: pages.pop(0)):
            self.assertEqual(m.api_paged("/x", "tok"), [1, 2, 3])

    def test_respects_page_cap(self):
        forever = '<https://api.github.com/x?page=99>; rel="next"'
        with mock.patch.object(m.urllib.request, "urlopen",
                               side_effect=lambda *a, **k: FakeResponse([1], link=forever)):
            self.assertEqual(len(m.api_paged("/x", "tok", cap=3)), 3)


class TestFetchCodeowners(unittest.TestCase):
    def test_falls_through_paths_until_found(self):
        import base64
        blob = {"content": base64.b64encode(b"* @austin").decode()}
        calls = []

        def fake_get(path, token, allow_404=False, retries=4):
            calls.append(path)
            if path.endswith("/.github/CODEOWNERS"):
                return None, ""
            return blob, ""

        with mock.patch.object(m, "api_get", side_effect=fake_get):
            self.assertEqual(m.fetch_codeowners("O", "r", "t"), "austin")
        self.assertEqual(len(calls), 2)

    def test_returns_none_when_absent_everywhere(self):
        with mock.patch.object(m, "api_get", return_value=(None, "")):
            self.assertIsNone(m.fetch_codeowners("O", "r", "t"))

    def test_survives_undecodable_content(self):
        with mock.patch.object(m, "api_get", return_value=({"content": "!!!not base64!!!"}, "")):
            self.assertIsNone(m.fetch_codeowners("O", "r", "t"))


# --------------------------------------------------------------------------
# build()
# --------------------------------------------------------------------------

class TestBuild(unittest.TestCase):
    REPOS = [
        {"name": "task-library", "private": False, "pushed_at": "2026-08-14T09:00:00Z"},
        {"name": "agent-runtime", "private": True, "pushed_at": "2026-08-13T09:00:00Z"},
        {"name": "old-thing", "private": True, "archived": True, "pushed_at": "2024-01-01T00:00:00Z"},
    ]
    CONTRIBS = {
        "task-library": [{"login": "Goodrich-Dev", "contributions": 48},
                         {"login": "dennisyu", "contributions": 21}],
        "agent-runtime": [{"login": "dennisyu", "contributions": 74}],
    }

    def _paged(self, path, token, cap=20):
        if "/repos?" in path:
            return self.REPOS
        for name, rows in self.CONTRIBS.items():
            if f"/{name}/contributors" in path:
                return rows
        return []

    def _build(self, codeowners=None, **kw):
        with mock.patch.object(m, "api_paged", side_effect=self._paged), \
             mock.patch.object(m, "fetch_codeowners",
                               side_effect=lambda o, r, t: (codeowners or {}).get(r)):
            return m.build("Test-Org", "tok", **kw)

    def test_skips_archived_by_default(self):
        data = self._build()
        self.assertEqual({r["name"] for r in data["repos"]},
                         {"task-library", "agent-runtime"})

    def test_include_archived_flag(self):
        data = self._build(include_archived=True)
        self.assertIn("old-thing", {r["name"] for r in data["repos"]})

    def test_owner_is_top_committer(self):
        data = self._build()
        tl = next(r for r in data["repos"] if r["name"] == "task-library")
        self.assertEqual(tl["owner"], "goodrich-dev")
        self.assertEqual(tl["owner_source"], "top committer")

    def test_codeowners_overrides_top_committer(self):
        data = self._build(codeowners={"task-library": "josh-lss"})
        tl = next(r for r in data["repos"] if r["name"] == "task-library")
        self.assertEqual(tl["owner"], "josh-lss")
        self.assertEqual(tl["owner_source"], "CODEOWNERS")

    def test_commits_are_summed_from_contributors(self):
        data = self._build()
        tl = next(r for r in data["repos"] if r["name"] == "task-library")
        self.assertEqual(tl["commits"], 69)

    def test_visibility_mapping(self):
        data = self._build()
        vis = {r["name"]: r["visibility"] for r in data["repos"]}
        self.assertEqual(vis["task-library"], "public")
        self.assertEqual(vis["agent-runtime"], "private")

    def test_last_push_is_date_only(self):
        data = self._build()
        self.assertEqual(
            next(r for r in data["repos"] if r["name"] == "task-library")["last_push"],
            "2026-08-14")

    def test_people_ordered_by_total_commits_and_slotted(self):
        data = self._build()
        # dennisyu 74+21=95 beats Goodrich-Dev 48
        self.assertEqual([p["login"] for p in data["people"]],
                         ["dennisyu", "Goodrich-Dev"])
        self.assertEqual([p["slot"] for p in data["people"]], [0, 1])

    def test_repo_with_no_contributors_is_unassigned(self):
        repos = [{"name": "empty", "private": True, "pushed_at": "2026-01-01T00:00:00Z"}]
        with mock.patch.object(m, "api_paged",
                               side_effect=lambda p, t, cap=20: repos if "/repos?" in p else []), \
             mock.patch.object(m, "fetch_codeowners", return_value=None):
            data = m.build("O", "tok")
        self.assertEqual(data["repos"][0]["owner"], "unassigned")
        self.assertEqual(data["repos"][0]["owner_source"], "no commits")
        self.assertIn("unassigned", [p["id"] for p in data["people"]])

    def test_empty_org_raises(self):
        with mock.patch.object(m, "api_paged", return_value=[]):
            with self.assertRaises(m.ApiError):
                m.build("Nope", "tok")

    def test_ninth_person_gets_no_slot(self):
        repos = [{"name": f"r{i}", "private": True, "pushed_at": "2026-01-01T00:00:00Z"}
                 for i in range(9)]

        def paged(path, token, cap=20):
            if "/repos?" in path:
                return repos
            i = int(path.split("/contributors")[0].rsplit("/r", 1)[1])
            return [{"login": f"user{i}", "contributions": 100 - i}]

        with mock.patch.object(m, "api_paged", side_effect=paged), \
             mock.patch.object(m, "fetch_codeowners", return_value=None):
            data = m.build("O", "tok")
        slots = [p["slot"] for p in data["people"]]
        self.assertEqual(slots[:8], list(range(8)))
        self.assertIsNone(slots[8])


# --------------------------------------------------------------------------
# assemble() / render()
# --------------------------------------------------------------------------

class TestAssemble(unittest.TestCase):
    def _repos(self, *names):
        return [{"name": n, "commits": 1, "contributors": [], "owner": "x",
                 "owner_login": "x", "owner_source": "t", "visibility": "private",
                 "last_push": "2026-01-01"} for n in names]

    def test_known_repos_land_in_their_layer(self):
        data = m.assemble("O", self._repos("agent-runtime", "task-library"), [], sample=False)
        titles = {L["title"]: L["repos"] for L in data["layers"]}
        self.assertEqual(titles["Shared runtime"], ["agent-runtime"])
        self.assertEqual(titles["Content and data"], ["task-library"])

    def test_unknown_repo_is_surfaced_not_dropped(self):
        data = m.assemble("O", self._repos("brand-new-repo"), [], sample=False)
        titles = {L["title"]: L["repos"] for L in data["layers"]}
        self.assertEqual(titles["Unclassified"], ["brand-new-repo"])

    def test_empty_layers_are_omitted(self):
        data = m.assemble("O", self._repos("agent-runtime"), [], sample=False)
        self.assertEqual([L["title"] for L in data["layers"]], ["Shared runtime"])

    def test_every_repo_appears_exactly_once_across_layers(self):
        names = ["agent-runtime", "task-library", "second-ring", "mystery"]
        data = m.assemble("O", self._repos(*names), [], sample=False)
        flat = [n for L in data["layers"] for n in L["repos"]]
        self.assertEqual(sorted(flat), sorted(names))
        self.assertEqual(len(flat), len(set(flat)))

    def test_timestamps_present(self):
        data = m.assemble("O", self._repos("x"), [], sample=False)
        self.assertIn("generated_at", data)
        self.assertRegex(data["generated_at_display"], r"UTC$")


class TestRender(unittest.TestCase):
    def test_placeholder_is_replaced_with_valid_json(self):
        data = m.sample_data()
        html = m.render(data)
        self.assertNotIn("__DATA__", html)
        blob = html.split('type="application/json">', 1)[1].split("</script>", 1)[0]
        self.assertEqual(json.loads(blob.replace("<\\/", "</"))["org"],
                         "Local-Service-Spotlight")

    def test_script_close_sequence_is_neutralised(self):
        data = m.assemble("O</script><script>alert(1)</script>",
                          [], [], sample=False)
        html = m.render(data)
        # the injected close tag must not survive as a real tag
        self.assertNotIn("<script>alert(1)</script>", html)

    def test_missing_placeholder_raises(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as fh:
            fh.write("<html>no placeholder</html>")
            path = Path(fh.name)
        try:
            with self.assertRaises(ValueError):
                m.render({}, template=path)
        finally:
            path.unlink()


class TestSampleData(unittest.TestCase):
    def test_ten_repos_matching_the_mirror(self):
        data = m.sample_data()
        self.assertEqual(len(data["repos"]), 10)
        self.assertEqual(
            sorted(r["name"] for r in data["repos"]),
            sorted(["agent-runtime", "dennis-os", "task-library", "content-agent",
                    "hq", "bm-wordpress", "sitebuilder-wordpress-themes",
                    "second-ring", "white-label-dash-front-end",
                    "white-label-dash-back-end"]))

    def test_total_matches_the_502_commits_actually_mirrored(self):
        data = m.sample_data()
        self.assertEqual(sum(r["commits"] for r in data["repos"]), 502)

    def test_flagged_as_sample_with_an_explanatory_note(self):
        data = m.sample_data()
        self.assertTrue(data["sample"])
        self.assertIn("placeholder", data["sample_note"])

    def test_task_library_is_the_public_one(self):
        data = m.sample_data()
        pub = [r["name"] for r in data["repos"] if r["visibility"] == "public"]
        self.assertEqual(pub, ["task-library"])

    def test_owner_slots_stay_inside_the_validated_palette(self):
        data = m.sample_data()
        slots = [p["slot"] for p in data["people"] if p["slot"] is not None]
        self.assertTrue(all(0 <= s < 8 for s in slots))
        self.assertEqual(len(slots), len(set(slots)), "slots must be unique")

    def test_every_repo_owner_resolves_to_a_named_person(self):
        data = m.sample_data()
        ids = {p["id"] for p in data["people"]}
        for r in data["repos"]:
            self.assertIn(r["owner"], ids, r["name"])

    def test_commit_totals_match_contributor_sums(self):
        for r in m.sample_data()["repos"]:
            self.assertEqual(r["commits"], sum(c["commits"] for c in r["contributors"]))


class TestMain(unittest.TestCase):
    def test_sample_run_writes_a_file(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "nested" / "map.html"
            js = Path(d) / "data.json"
            rc = m.main(["--sample", "--out", str(out), "--json-out", str(js)])
            self.assertEqual(rc, 0)
            self.assertIn("Who owns what", out.read_text())
            self.assertEqual(json.loads(js.read_text())["sample"], True)

    def test_missing_token_exits_1_with_guidance(self):
        with mock.patch.dict(m.os.environ, {}, clear=True):
            err = io.StringIO()
            with mock.patch.object(m.sys, "stderr", err):
                self.assertEqual(m.main(["--out", "/dev/null"]), 1)
            self.assertIn("GITHUB_TOKEN", err.getvalue())

    def test_api_failure_exits_2(self):
        with mock.patch.dict(m.os.environ, {"GITHUB_TOKEN": "t"}, clear=True), \
             mock.patch.object(m, "build", side_effect=m.ApiError("nope")), \
             mock.patch.object(m.sys, "stderr", io.StringIO()):
            self.assertEqual(m.main(["--out", "/dev/null"]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
