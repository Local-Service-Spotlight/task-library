import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class StableTaskDeepLink(unittest.TestCase):
    def test_query_parameter_routes_to_the_requested_slug(self):
        app = (ROOT / "dashboard" / "app.js").read_text(encoding="utf-8")

        self.assertIn(
            "new URLSearchParams(window.location.search).get('task')", app
        )
        self.assertIn("if (linkedTask) gotoSlug(linkedTask);", app)

    def test_wordpress_message_bridge_is_origin_scoped(self):
        app = (ROOT / "dashboard" / "app.js").read_text(encoding="utf-8")

        self.assertIn("e.origin !== 'https://blitzmetrics.com'", app)
        self.assertIn("gotoSlug(e.data.btlTask)", app)

    def test_crafted_inherited_property_is_not_treated_as_a_task(self):
        app = (ROOT / "dashboard" / "app.js").read_text(encoding="utf-8")

        self.assertIn("const bySlug = Object.create(null);", app)
        self.assertIn("Object.prototype.hasOwnProperty.call(bySlug, slug)", app)


if __name__ == "__main__":
    unittest.main()
