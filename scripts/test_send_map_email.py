#!/usr/bin/env python3
"""Tests for send_map_email.py.  Run:  python3 -m unittest -v"""

import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).parent))

import build_ownership_map as bm  # noqa: E402
import send_map_email as s  # noqa: E402


class TestRecipients(unittest.TestCase):
    def test_comma_separated(self):
        self.assertEqual(s.recipients("a@x.com, b@y.com"), ["a@x.com", "b@y.com"])

    def test_mixed_separators(self):
        self.assertEqual(
            s.recipients("a@x.com; b@y.com\nc@z.com  d@w.com"),
            ["a@x.com", "b@y.com", "c@z.com", "d@w.com"])

    def test_strips_angle_brackets(self):
        self.assertEqual(s.recipients("<a@x.com>"), ["a@x.com"])

    def test_deduplicates_case_insensitively(self):
        self.assertEqual(s.recipients("A@X.com, a@x.com"), ["A@X.com"])

    def test_drops_entries_without_an_at_sign(self):
        self.assertEqual(s.recipients("nope, a@x.com"), ["a@x.com"])

    def test_empty_input(self):
        self.assertEqual(s.recipients(""), [])
        self.assertEqual(s.recipients(None), [])


class TestSummarise(unittest.TestCase):
    def setUp(self):
        self.data = bm.sample_data()

    def test_headline_has_counts(self):
        headline, lines = s.summarise(self.data)
        self.assertIn("10 repos", headline)
        self.assertIn("502 commits", headline)
        self.assertIn("3 with a single contributor", headline)
        self.assertEqual(len(lines), 10)

    def test_lines_sorted_by_commits_descending(self):
        _, lines = s.summarise(self.data)
        self.assertTrue(lines[0].startswith("agent-runtime"))

    def test_bus_factor_marked_only_on_solo_repos(self):
        _, lines = s.summarise(self.data)
        flagged = [l.split(" —")[0] for l in lines if "bus factor 1" in l]
        self.assertEqual(sorted(flagged),
                         ["dennis-os", "second-ring", "sitebuilder-wordpress-themes"])

    def test_owner_names_resolved_not_ids(self):
        _, lines = s.summarise(self.data)
        self.assertIn("Dennis Yu", lines[0])
        self.assertNotIn("dennis-yu", lines[0])

    def test_unknown_owner_falls_back_gracefully(self):
        data = dict(self.data)
        data["repos"] = [dict(data["repos"][0], owner="ghost")]
        _, lines = s.summarise(data)
        self.assertIn("no clear owner", lines[0])

    def test_singular_contributor_wording(self):
        _, lines = s.summarise(self.data)
        solo = [l for l in lines if l.startswith("dennis-os")][0]
        self.assertIn("1 contributor", solo)
        self.assertNotIn("1 contributors", solo)
        shared = [l for l in lines if l.startswith("agent-runtime")][0]
        self.assertIn("2 contributors", shared)


class TestBuildMessage(unittest.TestCase):
    def setUp(self):
        self.data = bm.sample_data()
        self.tmp = tempfile.TemporaryDirectory()
        self.html = Path(self.tmp.name) / "map.html"
        self.html.write_text("<html>the map</html>", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def _msg(self, to=None):
        return s.build_message(self.data, self.html, "https://example.test/map",
                               "bot@lss.test", to or ["a@x.com", "b@y.com"])

    def test_headers(self):
        m = self._msg()
        self.assertIn("Who owns what", m["Subject"])
        self.assertIn("2026-", m["Subject"])
        self.assertEqual(m["From"], "bot@lss.test")
        self.assertEqual(m["To"], "a@x.com, b@y.com")

    def test_has_plain_and_html_alternatives(self):
        m = self._msg()
        subtypes = {p.get_content_subtype() for p in m.walk()
                    if p.get_content_maintype() == "text"}
        self.assertIn("plain", subtypes)
        self.assertIn("html", subtypes)

    def test_attaches_the_generated_page(self):
        m = self._msg()
        names = [p.get_filename() for p in m.iter_attachments()]
        self.assertIn("ownership-map.html", names)

    def test_plain_body_lists_every_repo_and_the_url(self):
        body = self._msg().get_body(("plain",)).get_content()
        for r in self.data["repos"]:
            self.assertIn(r["name"], body)
        self.assertIn("https://example.test/map", body)

    def test_plain_body_names_the_bus_factor_repos(self):
        body = self._msg().get_body(("plain",)).get_content()
        self.assertIn("Bus factor 1", body)
        self.assertIn("second-ring", body)

    def test_html_body_escapes_injected_markup(self):
        self.data["org"] = "<script>alert(1)</script>"
        html = self._msg().get_body(("html",)).get_content()
        self.assertNotIn("<script>alert(1)</script>", html)
        self.assertIn("&lt;script&gt;", html)

    def test_no_bus_factor_line_when_every_repo_is_shared(self):
        for r in self.data["repos"]:
            if len(r["contributors"]) == 1:
                r["contributors"].append({"login": "x", "name": "x", "commits": 1})
        body = self._msg().get_body(("plain",)).get_content()
        self.assertIn("No repository depends on a single person", body)


class TestSendTransport(unittest.TestCase):
    def test_port_465_uses_implicit_tls(self):
        with mock.patch.object(s.smtplib, "SMTP_SSL") as ssl_srv, \
             mock.patch.object(s.smtplib, "SMTP") as plain:
            s.send(mock.MagicMock(), "smtp.test", 465, "u", "p")
        ssl_srv.assert_called_once()
        plain.assert_not_called()

    def test_port_587_uses_starttls(self):
        with mock.patch.object(s.smtplib, "SMTP_SSL") as ssl_srv, \
             mock.patch.object(s.smtplib, "SMTP") as plain:
            s.send(mock.MagicMock(), "smtp.test", 587, "u", "p")
        plain.assert_called_once()
        ssl_srv.assert_not_called()
        conn = plain.return_value.__enter__.return_value
        conn.starttls.assert_called_once()
        conn.login.assert_called_once_with("u", "p")


class TestMain(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        self.html, self.json = d / "m.html", d / "m.json"
        self.html.write_text("<html>x</html>", encoding="utf-8")
        self.json.write_text(json.dumps(bm.sample_data()), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def _argv(self, *extra):
        return ["--html", str(self.html), "--json", str(self.json),
                "--url", "https://example.test", *extra]

    def test_no_recipients_is_a_clean_exit_not_a_failure(self):
        with mock.patch.dict(s.os.environ, {"MAIL_TO": ""}, clear=True), \
             mock.patch.object(s.sys, "stderr", io.StringIO()):
            self.assertEqual(s.main(self._argv()), 0)

    def test_missing_credentials_exits_1(self):
        with mock.patch.dict(s.os.environ, {"MAIL_TO": "a@x.com"}, clear=True), \
             mock.patch.object(s.sys, "stderr", io.StringIO()):
            self.assertEqual(s.main(self._argv()), 1)

    def test_dry_run_prints_without_credentials(self):
        out = io.StringIO()
        with mock.patch.dict(s.os.environ, {"MAIL_TO": "a@x.com"}, clear=True), \
             mock.patch.object(s.sys, "stdout", out), \
             mock.patch.object(s, "send") as sender:
            self.assertEqual(s.main(self._argv("--dry-run")), 0)
        sender.assert_not_called()
        self.assertIn("agent-runtime", out.getvalue())

    def test_happy_path_calls_send_once(self):
        env = {"MAIL_TO": "a@x.com", "MAIL_USERNAME": "u", "MAIL_PASSWORD": "p"}
        with mock.patch.dict(s.os.environ, env, clear=True), \
             mock.patch.object(s, "send") as sender, \
             mock.patch.object(s.sys, "stderr", io.StringIO()):
            self.assertEqual(s.main(self._argv()), 0)
        sender.assert_called_once()

    def test_smtp_failure_exits_2(self):
        env = {"MAIL_TO": "a@x.com", "MAIL_USERNAME": "u", "MAIL_PASSWORD": "p"}
        with mock.patch.dict(s.os.environ, env, clear=True), \
             mock.patch.object(s, "send", side_effect=s.smtplib.SMTPException("no")), \
             mock.patch.object(s.sys, "stderr", io.StringIO()):
            self.assertEqual(s.main(self._argv()), 2)

    def test_default_port_when_env_blank(self):
        env = {"MAIL_TO": "a@x.com", "MAIL_USERNAME": "u",
               "MAIL_PASSWORD": "p", "MAIL_PORT": ""}
        with mock.patch.dict(s.os.environ, env, clear=True), \
             mock.patch.object(s, "send") as sender, \
             mock.patch.object(s.sys, "stderr", io.StringIO()):
            s.main(self._argv())
        self.assertEqual(sender.call_args[0][2], 587)


if __name__ == "__main__":
    unittest.main(verbosity=2)
