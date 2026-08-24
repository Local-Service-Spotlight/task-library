import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class StableTaskDeepLink(unittest.TestCase):
    def test_query_parameter_routes_to_the_requested_slug(self):
        app = (ROOT / "dashboard" / "app.js").read_text(encoding="utf-8")

        self.assertIn(
            "const params = new URLSearchParams(window.location.search);", app
        )
        self.assertIn("task: params.get('task') || ''", app)
        self.assertIn("if (linkedRoute.task) gotoSlug(linkedRoute.task);", app)
        self.assertIn('id="task-', app)

    def test_article_query_filters_every_task_on_the_normalized_hub(self):
        app = (ROOT / "dashboard" / "app.js").read_text(encoding="utf-8")

        self.assertIn("article: params.get('article') || ''", app)
        self.assertIn("else if (linkedRoute.article) gotoArticle(linkedRoute.article);", app)
        self.assertIn("t._articleKey === state.articleKey", app)
        self.assertIn("normalizeArticleUrl(t.article)", app)
        self.assertIn("Object.prototype.hasOwnProperty.call(byArticle, key)", app)

    def test_wordpress_message_bridge_is_origin_scoped(self):
        app = (ROOT / "dashboard" / "app.js").read_text(encoding="utf-8")

        self.assertIn("e.origin !== 'https://blitzmetrics.com'", app)
        self.assertIn("gotoSlug(e.data.btlTask)", app)
        self.assertIn("gotoArticle(e.data.btlArticle)", app)

    def test_crafted_inherited_property_is_not_treated_as_a_task(self):
        app = (ROOT / "dashboard" / "app.js").read_text(encoding="utf-8")

        self.assertIn("const bySlug = Object.create(null);", app)
        self.assertIn("Object.prototype.hasOwnProperty.call(bySlug, slug)", app)


if __name__ == "__main__":
    unittest.main()
