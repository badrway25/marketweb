"""Tests for scripts/check_imagery_pack.py · X.3 Commit 3.

Offline-only (no network calls). The ``check_network`` function is
exercised with an injected ``http_head`` stub so the tests stay
hermetic · CI-safe.

Invoked with Python's stdlib unittest discovery:

    python -m unittest discover -t . -s tests

(This test module deliberately does NOT live under apps/ so it is
outside Django's test runner; it stays a pure-Python standalone unit
test around the standalone validator script.)
"""

from __future__ import annotations

import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


# ── Import the validator script as a module ───────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = REPO_ROOT / "scripts" / "check_imagery_pack.py"

_spec = importlib.util.spec_from_file_location("check_imagery_pack", SCRIPT_PATH)
check_imagery_pack = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(check_imagery_pack)  # type: ignore[union-attr]


# ── Helpers ───────────────────────────────────────────────────────


def _make_pack_text(urls: list[str]) -> str:
    """Assemble a fake pack markdown string for a list of URLs."""
    lines = ["# Imagery Pack · test\n\n## URL list\n\n### hero\n"]
    for i, u in enumerate(urls, 1):
        lines.append(f"{i}. `{u}`")
        lines.append(f"   - Caption: test {i}")
        lines.append("")
    return "\n".join(lines)


def _pexels_url(pid: int) -> str:
    return f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg"


def _unsplash_url(pid: str) -> str:
    return f"https://images.unsplash.com/photo-{pid}"


# ── Tests ─────────────────────────────────────────────────────────


class ExtractUrlsTests(unittest.TestCase):
    """extract_urls() is pure · deterministic · regex-based."""

    def test_extracts_pexels_urls_from_backticked_markdown(self):
        md = _make_pack_text([_pexels_url(1), _pexels_url(2)])
        urls = check_imagery_pack.extract_urls(md)
        self.assertEqual(len(urls), 2)
        self.assertIn(_pexels_url(1), urls)
        self.assertIn(_pexels_url(2), urls)

    def test_preserves_duplicates_for_caller_to_decide(self):
        md = _make_pack_text([_pexels_url(7), _pexels_url(7), _pexels_url(9)])
        urls = check_imagery_pack.extract_urls(md)
        self.assertEqual(len(urls), 3)
        self.assertEqual(urls.count(_pexels_url(7)), 2)

    def test_ignores_non_url_content(self):
        md = "Just some text · no URLs here · `code fragment` but no http."
        urls = check_imagery_pack.extract_urls(md)
        self.assertEqual(urls, [])

    def test_matches_mixed_allowed_domains(self):
        md = _make_pack_text([_pexels_url(1), _unsplash_url("abc123")])
        urls = check_imagery_pack.extract_urls(md)
        self.assertIn(_pexels_url(1), urls)
        self.assertIn(_unsplash_url("abc123"), urls)


class StructuralValidationTests(unittest.TestCase):
    """validate_structural() enforces count + dup + domain gates."""

    def _validate(self, urls):
        return check_imagery_pack.validate_structural(Path("test.md"), urls)

    def test_ok_pack_has_no_errors(self):
        urls = [_pexels_url(i) for i in range(100, 125)]  # 25 distinct URLs
        report = self._validate(urls)
        self.assertTrue(report.ok)
        self.assertEqual(report.errors, [])

    def test_count_below_minimum_fails(self):
        urls = [_pexels_url(i) for i in range(100, 105)]  # 5 URLs
        report = self._validate(urls)
        self.assertFalse(report.ok)
        self.assertTrue(
            any("count: 5" in e and "< min 20" in e for e in report.errors),
            f"expected min-count error, got {report.errors}",
        )

    def test_count_above_maximum_fails(self):
        urls = [_pexels_url(i) for i in range(100, 150)]  # 50 URLs
        report = self._validate(urls)
        self.assertFalse(report.ok)
        self.assertTrue(
            any("count: 50" in e and "> max 40" in e for e in report.errors),
            f"expected max-count error, got {report.errors}",
        )

    def test_duplicate_urls_within_pack_fail(self):
        urls = [_pexels_url(1)] * 25  # 25 copies of the same URL
        report = self._validate(urls)
        self.assertFalse(report.ok)
        self.assertTrue(
            any("duplicate within pack" in e for e in report.errors),
            f"expected duplicate error, got {report.errors}",
        )

    def test_disallowed_domain_fails(self):
        urls = [_pexels_url(i) for i in range(100, 120)] + [
            "https://shutterstock.com/evil/photo.jpg"
        ]
        report = self._validate(urls)
        self.assertFalse(report.ok)
        self.assertTrue(
            any("disallowed domain" in e for e in report.errors),
            f"expected disallowed-domain error, got {report.errors}",
        )

    def test_overridden_allowed_domains(self):
        """Allowed domains are a frozenset argument · tests can narrow/widen."""
        urls = [_pexels_url(i) for i in range(100, 125)]
        report = check_imagery_pack.validate_structural(
            Path("test.md"),
            urls,
            allowed_domains=frozenset({"images.unsplash.com"}),  # Pexels now disallowed
        )
        self.assertFalse(report.ok)
        self.assertTrue(any("disallowed domain" in e for e in report.errors))


class NetworkProbeTests(unittest.TestCase):
    """check_network() exercised with injected http_head stub."""

    def test_all_urls_return_ok_image(self):
        stub = lambda url: (200, "image/jpeg")
        failures = check_imagery_pack.check_network(
            [_pexels_url(1), _pexels_url(2)],
            http_head=stub,
        )
        self.assertEqual(failures, [])

    def test_non_2xx_status_is_failure(self):
        stub = lambda url: (404, "text/html")
        failures = check_imagery_pack.check_network(
            [_pexels_url(1)],
            http_head=stub,
        )
        self.assertEqual(len(failures), 1)
        self.assertIn("status 404", failures[0][1])

    def test_wrong_content_type_is_failure(self):
        stub = lambda url: (200, "text/html")
        failures = check_imagery_pack.check_network(
            [_pexels_url(1)],
            http_head=stub,
        )
        self.assertEqual(len(failures), 1)
        self.assertIn("content-type", failures[0][1])

    def test_network_error_is_failure(self):
        stub = lambda url: (0, "error:connection refused")
        failures = check_imagery_pack.check_network(
            [_pexels_url(1)],
            http_head=stub,
        )
        self.assertEqual(len(failures), 1)
        self.assertIn("network error", failures[0][1])

    def test_redirect_treated_as_ok(self):
        # CDN redirect (Pexels sometimes 301s between subdomains) →
        # not an error per our contract.
        stub = lambda url: (301, "")
        failures = check_imagery_pack.check_network(
            [_pexels_url(1)],
            http_head=stub,
        )
        self.assertEqual(failures, [])


class CrossPackDuplicationTests(unittest.TestCase):
    """detect_cross_pack_duplicates() finds URLs in 2+ packs."""

    def _report(self, name: str, urls: list[str]):
        r = check_imagery_pack.PackReport(Path(name))
        r.urls = urls
        return r

    def test_clean_cross_packs_return_empty(self):
        a = self._report("a.md", [_pexels_url(1), _pexels_url(2)])
        b = self._report("b.md", [_pexels_url(3), _pexels_url(4)])
        result = check_imagery_pack.detect_cross_pack_duplicates([a, b])
        self.assertEqual(result, {})

    def test_shared_url_is_flagged(self):
        shared = _pexels_url(999)
        a = self._report("a.md", [shared, _pexels_url(1)])
        b = self._report("b.md", [shared, _pexels_url(2)])
        result = check_imagery_pack.detect_cross_pack_duplicates([a, b])
        self.assertIn(shared, result)
        self.assertEqual(set(result[shared]), {"a.md", "b.md"})


class RunnerTests(unittest.TestCase):
    """End-to-end ``run()`` + ``main()`` with --no-network default."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def _write_pack(self, name: str, urls: list[str]):
        (self.dir / name).write_text(_make_pack_text(urls), encoding="utf-8")

    def test_run_returns_zero_when_all_packs_valid(self):
        urls = [_pexels_url(i) for i in range(1000, 1025)]  # 25 URLs · valid
        self._write_pack("one.md", urls)
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = check_imagery_pack.run(
                [self.dir], use_network=False, check_cross=False
            )
        self.assertEqual(rc, 0, buf.getvalue())
        self.assertIn("[OK ]", buf.getvalue())

    def test_run_returns_nonzero_on_count_violation(self):
        self._write_pack("tiny.md", [_pexels_url(1), _pexels_url(2)])
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = check_imagery_pack.run(
                [self.dir], use_network=False, check_cross=False
            )
        self.assertEqual(rc, 1)
        self.assertIn("[FAIL]", buf.getvalue())

    def test_run_returns_two_when_no_files_found(self):
        empty_dir = self.dir / "empty"
        empty_dir.mkdir()
        buf = io.StringIO()
        with redirect_stdout(buf), \
             self.assertLogs() if False else _nullcontext():
            rc = check_imagery_pack.run(
                [empty_dir], use_network=False, check_cross=False
            )
        self.assertEqual(rc, 2)

    def test_run_flags_cross_pack_duplicates(self):
        shared_urls = [_pexels_url(i) for i in range(2000, 2025)]
        self._write_pack("a.md", shared_urls)
        self._write_pack("b.md", shared_urls)  # same URLs → cross-pack dup
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = check_imagery_pack.run(
                [self.dir], use_network=False, check_cross=True
            )
        self.assertEqual(rc, 1, buf.getvalue())
        self.assertIn("Cross-pack duplicates", buf.getvalue())

    def test_main_cli_offline_default_succeeds_on_valid_pack(self):
        urls = [_pexels_url(i) for i in range(3000, 3025)]
        self._write_pack("cli.md", urls)
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = check_imagery_pack.main([str(self.dir)])
        self.assertEqual(rc, 0)


class _nullcontext:
    def __enter__(self):
        return self

    def __exit__(self, *a, **kw):
        return False


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
