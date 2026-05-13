"""Regression tests for the pages app.

Phase 2.1 — guard against the multi-line ``{# ... #}`` template-comment
leakage that bled raw comment text into the rendered HTML of every public
page (see docs/AUDIT_REPORT_2026-05-13_PHASE2_STABILIZATION.md §7 P1).
Django's ``{# ... #}`` comment syntax is single-line only — multi-line
blocks must use ``{% comment %} ... {% endcomment %}``.
"""
import re

from django.test import TestCase, override_settings


@override_settings(AXES_ENABLED=False)
class TemplateCommentLeakageRegressionTests(TestCase):
    """Catches multi-line ``{# ... #}`` blocks that render as visible text."""

    # Pages crawlers index — must stay clean.
    PUBLIC_URLS = ["/", "/templates/", "/templates/categories/"]

    # ``{#`` followed by non-``#}`` content and a newline → a multi-line
    # opener that Django did NOT strip (the parser would have stripped a
    # well-formed single-line ``{# ... #}``).
    LEAKAGE_RE = re.compile(r"\{#(?:(?!#\}).)*\n", re.DOTALL)

    def test_no_multiline_django_comment_leaks_into_rendered_html(self):
        for url in self.PUBLIC_URLS:
            with self.subTest(url=url):
                resp = self.client.get(url)
                self.assertEqual(resp.status_code, 200, f"{url} did not return 200")
                body = resp.content.decode("utf-8")
                match = self.LEAKAGE_RE.search(body)
                self.assertIsNone(
                    match,
                    f"Multi-line {{# #}} comment leaked into {url!r} HTML. "
                    f"Use {{% comment %}} ... {{% endcomment %}} for multi-line. "
                    f"Snippet: {body[match.start():match.start()+120]!r}"
                    if match else "",
                )
