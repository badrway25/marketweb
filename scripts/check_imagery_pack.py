#!/usr/bin/env python3
"""Imagery pack validator · X.3 Commit 3.

Standalone · zero Django dependency · no app imports. Reads markdown
imagery pack files from ``docs/content-factory/imagery/packs/`` and
enforces the X.2 / X.3 curation contract:

  1. 20 ≤ URLs ≤ 40 per pack.
  2. No duplicate URL within the same pack.
  3. Only allowed image-host domains (Pexels primary, Unsplash
     secondary, per ``imagery/sources.md``).
  4. No cross-pack duplication when ``--check-cross`` is passed.
  5. Optional HTTP HEAD probe when ``--network`` is passed (default
     is offline structural validation · CI-safe).

Usage
-----
::

    # Offline structural check (default):
    python scripts/check_imagery_pack.py docs/content-factory/imagery/packs/

    # Include network HEAD probe per URL:
    python scripts/check_imagery_pack.py --network docs/content-factory/imagery/packs/

    # Check cross-pack duplication:
    python scripts/check_imagery_pack.py --check-cross docs/content-factory/imagery/packs/

    # Validate a single pack file:
    python scripts/check_imagery_pack.py docs/content-factory/imagery/packs/dental.md

Exit codes
----------
* 0 · all packs valid
* 1 · one or more validation failures
* 2 · invocation error (bad path, no inputs, ...)

Design notes
------------
* No Django bootstrap. This script is callable on a bare Python
  install with no env setup beyond the standard library.
* Markdown parsing is intentionally naive (regex URL extraction). The
  pack files follow a known shape authored by the factory pipeline;
  we do not need a full MD parser.
* The allowed-domain set lives in a module-level constant so tests
  can override it. The default mirrors ``sources.md``.
* Network mode is off by default so CI runs are hermetic. An operator
  can opt in at curation time to catch dead URLs.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable


# ── Policy (mirror of docs/content-factory/imagery/sources.md) ───

MIN_URLS_PER_PACK = 20
MAX_URLS_PER_PACK = 40

ALLOWED_DOMAINS = frozenset(
    {
        "images.pexels.com",
        "images.unsplash.com",
    }
)

# Crude but sufficient URL matcher for markdown packs. The pack
# format authored by the factory wraps URLs in backticks; we match
# any https://<domain>/path that starts with http(s) and ends at a
# whitespace or backtick boundary.
URL_REGEX = re.compile(r"https?://([A-Za-z0-9.\-]+)(/[^\s`\"'<>)]*)")


class PackReport:
    """Structured result for one pack file."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.urls: list[str] = []
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.network_failures: list[tuple[str, str]] = []

    @property
    def ok(self) -> bool:
        return not self.errors

    def summary_line(self) -> str:
        marker = "OK " if self.ok else "FAIL"
        return (
            f"[{marker}] {self.path.name}: {len(self.urls)} URLs "
            f"({len(self.errors)} errors, {len(self.warnings)} warnings)"
        )


# ── Core extraction + validation ──────────────────────────────────


def extract_urls(markdown_text: str) -> list[str]:
    """Return the ordered list of URLs found in the markdown text.

    Duplicates are preserved in the returned list; the caller decides
    how to treat them (this function is pure extraction).
    """
    out: list[str] = []
    for match in URL_REGEX.finditer(markdown_text):
        domain = match.group(1)
        path = match.group(2)
        url = f"https://{domain}{path}"
        out.append(url)
    return out


def validate_structural(
    path: Path,
    urls: list[str],
    allowed_domains: frozenset[str] = ALLOWED_DOMAINS,
    min_urls: int = MIN_URLS_PER_PACK,
    max_urls: int = MAX_URLS_PER_PACK,
) -> PackReport:
    """Run all offline checks on a pack. Returns a populated report."""
    report = PackReport(path)
    report.urls = urls

    # Count gate
    if len(urls) < min_urls:
        report.errors.append(
            f"count: {len(urls)} URLs < min {min_urls}"
        )
    if len(urls) > max_urls:
        report.errors.append(
            f"count: {len(urls)} URLs > max {max_urls}"
        )

    # Duplicate-within-pack gate
    seen: set[str] = set()
    dups: list[str] = []
    for u in urls:
        if u in seen:
            dups.append(u)
        seen.add(u)
    if dups:
        # Show up to the first 5 offenders to keep output bounded.
        sample = ", ".join(dups[:5])
        more = "" if len(dups) <= 5 else f" (+{len(dups) - 5} more)"
        report.errors.append(f"duplicate within pack: {sample}{more}")

    # Allowed-domain gate
    disallowed: list[str] = []
    for u in urls:
        m = URL_REGEX.match(u)
        if not m:
            disallowed.append(u)
            continue
        domain = m.group(1)
        if domain not in allowed_domains:
            disallowed.append(u)
    if disallowed:
        sample = ", ".join(disallowed[:5])
        more = (
            ""
            if len(disallowed) <= 5
            else f" (+{len(disallowed) - 5} more)"
        )
        report.errors.append(f"disallowed domain: {sample}{more}")

    return report


def check_network(
    urls: Iterable[str],
    http_head=None,
    timeout: float = 8.0,
) -> list[tuple[str, str]]:
    """Probe each URL with HTTP HEAD.

    Returns a list of ``(url, reason)`` tuples for any URL that
    fails the probe. An empty list means all URLs answered with a
    2xx response and an ``image/*`` content-type (or a redirect,
    which we treat as OK).

    The ``http_head`` argument is injectable for tests so they can
    mock HTTP behaviour without touching the network.
    """
    if http_head is None:
        import urllib.request

        def _default_head(url: str):  # pragma: no cover · exercised in --network runs
            req = urllib.request.Request(url, method="HEAD")
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return r.status, r.headers.get("Content-Type", "")
            except Exception as e:
                return 0, f"error:{e!r}"

        http_head = _default_head

    failures: list[tuple[str, str]] = []
    for u in urls:
        status, content_type = http_head(u)
        if status == 0:
            failures.append((u, f"network error {content_type}"))
            continue
        if not (200 <= status < 400):
            failures.append((u, f"status {status}"))
            continue
        if status < 300 and "image/" not in (content_type or ""):
            failures.append((u, f"content-type {content_type!r}"))
    return failures


# ── Cross-pack duplication ────────────────────────────────────────


def detect_cross_pack_duplicates(
    reports: list[PackReport],
) -> dict[str, list[str]]:
    """Return ``url → [pack paths]`` for URLs appearing in 2+ packs."""
    registry: dict[str, list[str]] = {}
    for r in reports:
        for u in r.urls:
            registry.setdefault(u, []).append(r.path.name)
    return {u: packs for u, packs in registry.items() if len(packs) > 1}


# ── Runner ────────────────────────────────────────────────────────


def iter_pack_files(target: Path) -> list[Path]:
    """Expand a target into the list of .md files to validate."""
    if target.is_dir():
        return sorted(target.glob("*.md"))
    if target.is_file() and target.suffix == ".md":
        return [target]
    return []


def run(
    targets: list[Path],
    use_network: bool = False,
    check_cross: bool = False,
) -> int:
    pack_files: list[Path] = []
    for t in targets:
        pack_files.extend(iter_pack_files(t))
    if not pack_files:
        print("ERROR: no markdown pack files resolved from the provided targets.", file=sys.stderr)
        return 2

    reports: list[PackReport] = []
    any_fail = False
    for path in pack_files:
        md = path.read_text(encoding="utf-8")
        urls = extract_urls(md)
        report = validate_structural(path, urls)
        if use_network:
            failures = check_network(urls)
            if failures:
                report.network_failures = failures
                report.errors.append(
                    f"network: {len(failures)} URL(s) did not respond 2xx image/*"
                )
        reports.append(report)
        print(report.summary_line())
        for err in report.errors:
            print(f"  error: {err}")
        for w in report.warnings:
            print(f"  warn:  {w}")
        if not report.ok:
            any_fail = True

    if check_cross:
        dups = detect_cross_pack_duplicates(reports)
        if dups:
            any_fail = True
            print("\nCross-pack duplicates:")
            for url, packs in dups.items():
                print(f"  {url} → {', '.join(packs)}")
        else:
            print("\nCross-pack duplication: clean.")

    return 1 if any_fail else 0


def _build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="check_imagery_pack",
        description=(
            "Validate MarketWeb content-factory imagery packs against "
            "the X.3 Commit 1 curation contract."
        ),
    )
    p.add_argument(
        "targets",
        nargs="+",
        type=Path,
        help="Pack .md files or a directory containing them.",
    )
    p.add_argument(
        "--network",
        action="store_true",
        help="Probe each URL with HTTP HEAD (off by default for CI hermeticity).",
    )
    p.add_argument(
        "--no-network",
        action="store_true",
        help="Explicit offline mode (alias for the default · kept for callsite clarity).",
    )
    p.add_argument(
        "--check-cross",
        action="store_true",
        help="Detect URLs shared across 2+ packs (one-URL-one-cluster invariant).",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    parser = _build_arg_parser()
    args = parser.parse_args(argv)
    use_network = bool(args.network) and not args.no_network
    return run(
        targets=args.targets,
        use_network=use_network,
        check_cross=args.check_cross,
    )


if __name__ == "__main__":
    sys.exit(main())
