"""Mechanical contrast tests for the corporate-suite archetype
(Phase X.4b · AP-4 pass 1).

Scope
-----
These tests lock the contracts shipped by
``apps.catalog.cs_contrast_audit`` and the Django checks
``corporate_suite.E004 / E005 / W003 / W004`` in
``apps.catalog.checks``. They are intentionally separated from the
parent ``apps.catalog.tests`` module so the mechanical-contrast surface
can grow without bloating the existing X.4a test bedrock.

Test layout (mirrors the ``CorporateSuiteThemeSafetyTests`` /
``CorporateSuiteImageryPolicyTests`` pattern in ``tests.py``):

1. WCAG math sanity (``ContrastMathTests``).
2. Per-palette pair audit (``PalettePairAuditTests``).
3. CSS scanner (``CssAccentScannerTests`` — the AP-4 fingerprint).
4. Chrome enumeration (``ChromeAuditTests``).
5. Enrolled-palette audit (``EnrolledPaletteAuditTests``).
6. Django checks E004 / E005 + W003 / W004 (``ContrastChecksRegistrationTests``).

No DB hits. No browser. Pure-Python static asserts, identical posture
to the existing palette-safety + chrome contract tests.
"""
from __future__ import annotations

import warnings

from django.test import TestCase

from apps.catalog.cs_contrast_audit import (
    DARK_BAND_CLASSES,
    KNOWN_AP4_BASELINE_SELECTORS,
    LEGACY_AP4_PALETTE_EXEMPT_SLUGS,
    WCAG_AA_BODY,
    WCAG_DECORATIVE,
    audit_chrome_for_ap4,
    audit_enrolled_palettes,
    find_accent_text_on_dark_in_css,
    hex_distance,
    is_accent_text_safe_on_primary,
    palette_pair_audit,
    parse_css_rules,
    should_audit,
)


# ── 1. WCAG math sanity ──────────────────────────────────────────────


class ContrastMathTests(TestCase):
    """``cs_contrast_audit`` rests on the ``theme_safety`` color-math
    primitives. These tests guard the *combined* helpers (decision
    helpers + RGB distance) the AP-4 layer adds on top.
    """

    def test_accent_text_safe_pass_on_pragma_emerald(self):
        # Pragma: accent #10B981 (emerald) on primary #1E293B (slate)
        # ≈ 7.5:1 AAA — comfortably above the AA body floor.
        self.assertTrue(is_accent_text_safe_on_primary("#10B981", "#1E293B"))

    def test_accent_text_safe_fail_on_fiscus_dark_on_dark(self):
        # Fiscus: accent #1C3D5A (deep navy) on primary #1F2937 (charcoal)
        # ≈ 1.3:1 — the canonical AP-4 cell.
        self.assertFalse(is_accent_text_safe_on_primary("#1C3D5A", "#1F2937"))

    def test_accent_text_safe_fail_on_solaria_warm_on_warm(self):
        # Solaria: accent #8B5A2B (deep caramel) on primary #2B2A28 (carbon)
        # ≈ 1.9:1 — the warm-palette analog of the same AP-4 trap.
        self.assertFalse(is_accent_text_safe_on_primary("#8B5A2B", "#2B2A28"))

    def test_invalid_hex_falls_through_as_unsafe(self):
        # The helper must not raise on a malformed palette — the
        # build-time check needs to surface the defect, not 500 the
        # check runner itself.
        self.assertFalse(is_accent_text_safe_on_primary("not-a-hex", "#1E293B"))

    def test_hex_distance_known_endpoints(self):
        # Pure black to pure white = sqrt(3 * 255**2) ≈ 441.67
        self.assertAlmostEqual(hex_distance("#000000", "#FFFFFF"), 441.67, places=1)
        # Identity = 0
        self.assertEqual(hex_distance("#1E293B", "#1E293B"), 0.0)
        # Fiscus accent vs primary should be well under the AG-6 §3.2
        # "≥ 120" hard-veto floor — locks the math against accidental
        # drift.
        self.assertLess(hex_distance("#1C3D5A", "#1F2937"), 60.0)

    def test_should_audit_only_for_corporate_suite(self):
        self.assertTrue(should_audit("corporate-suite"))
        self.assertFalse(should_audit("startup-saas-landing"))
        self.assertFalse(should_audit(None))


# ── 2. Per-palette pair audit ────────────────────────────────────────


class PalettePairAuditTests(TestCase):
    """``palette_pair_audit`` returns every canonical foreground ×
    background ratio the corporate-suite chrome actually paints.
    """

    def test_pragma_palette_passes_accent_text_on_primary_floor(self):
        # AP-4 floor is the accent-on-primary text contract (DS-16 /
        # BO-08). Pragma emerald (#10B981) on slate (#1E293B) clears
        # AA body comfortably (~7.5:1). The accent-on-paper ratio is
        # OUT of AP-4 scope: emerald on cream measures only 2.22:1
        # but the chrome reserves accent-on-paper to the trailing
        # arrow glyph (decorative · DS-15) and to italic emphasis
        # under serif headings rendered at large-text sizes — both
        # honored by the design standard via separate rules. AP-4
        # pass 1 deliberately stays narrow.
        report = palette_pair_audit(
            "pragma-corporate-suite",
            {"primary": "#1E293B", "secondary": "#3B82F6", "accent": "#10B981"},
        )
        self.assertTrue(report.accent_text_on_primary_passes_aa)
        self.assertGreaterEqual(report.accent_on_primary, WCAG_AA_BODY)
        self.assertTrue(report.accent_decorative_on_primary_passes)

    def test_fiscus_palette_fails_accent_text_on_primary(self):
        report = palette_pair_audit(
            "fiscus-commercialista",
            {"primary": "#1F2937", "secondary": "#B58F4A", "accent": "#1C3D5A"},
        )
        self.assertFalse(report.accent_text_on_primary_passes_aa)
        self.assertLess(report.accent_on_primary, WCAG_AA_BODY)
        # The decorative floor (≥ 3:1 for ≤ 2 px rules / focus rings) is
        # also missed for Fiscus accent — so even non-text use needs
        # care; the standard already constrains accent to small
        # decorative widths on dark surfaces.
        self.assertFalse(report.accent_decorative_on_primary_passes)

    def test_solaria_palette_fails_accent_text_on_primary(self):
        report = palette_pair_audit(
            "solaria-coaching",
            {"primary": "#2B2A28", "secondary": "#C8621A", "accent": "#8B5A2B"},
        )
        self.assertFalse(report.accent_text_on_primary_passes_aa)
        self.assertLess(report.accent_on_primary, WCAG_AA_BODY)
        # Solaria's secondary (#C8621A burnt orange) clears AA on the
        # carbon primary — locks the safe-channel asymmetry that the
        # archetype standards take for granted.
        self.assertGreater(report.secondary_on_primary, WCAG_DECORATIVE)

    def test_continua_palette_passes_decorative_floor_only(self):
        # Brass on pine measures 3.88:1 — clears the WCAG_DECORATIVE
        # ≥ 3.0 floor for ≤ 2 px rules / focus glyphs, but fails the
        # AA body text floor (4.5). The em italic emphasis on dark
        # bands therefore lands on the same documented AP-4 baseline
        # as Fiscus / Solaria / Cornice / Causa, and Continua is
        # carried on LEGACY_AP4_PALETTE_EXEMPT_SLUGS pending pass-2.
        report = palette_pair_audit(
            "continua-stewardship",
            {"primary": "#0F3A30", "secondary": "#5A6E78", "accent": "#B0875E"},
        )
        self.assertFalse(report.accent_text_on_primary_passes_aa)
        self.assertGreaterEqual(report.accent_on_primary, WCAG_DECORATIVE)
        self.assertLess(report.accent_on_primary, WCAG_AA_BODY)

    def test_invalid_palette_returns_floor_ratios_without_raising(self):
        report = palette_pair_audit(
            "broken",
            {"primary": "not-a-hex", "secondary": "", "accent": ""},
        )
        # All ratios degrade to the floor (1.0) but the call returns a
        # well-formed report — never raises.
        self.assertEqual(report.accent_on_primary, 1.0)
        self.assertFalse(report.accent_text_on_primary_passes_aa)


# ── 3. CSS scanner ───────────────────────────────────────────────────


class CssAccentScannerTests(TestCase):
    """``find_accent_text_on_dark_in_css`` is the AP-4 fingerprint —
    detect a ``color: var(--accent)`` rule whose selector touches a
    known dark-band class.
    """

    def test_scanner_flags_dark_band_em_rule(self):
        css = """
            .cs-section.dark em { color: var(--accent); font-style: italic; }
        """
        findings = find_accent_text_on_dark_in_css(css, file_path="<test>")
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].normalised_selector, ".cs-section.dark em")

    def test_scanner_flags_grouped_dark_band_selector(self):
        css = """
            .cs-kpi-band em, .cs-cta em, .cs-foot em { color: var(--accent); }
        """
        findings = find_accent_text_on_dark_in_css(css, file_path="<test>")
        self.assertEqual(len(findings), 1)
        self.assertIn(".cs-kpi-band em", findings[0].normalised_selector)
        self.assertIn(".cs-cta em", findings[0].normalised_selector)
        self.assertIn(".cs-foot em", findings[0].normalised_selector)

    def test_scanner_ignores_paper_context_rules(self):
        css = """
            em { color: var(--accent); }
            .cs-lead h1 em { color: var(--accent); }
            .cs-btn-primary:after { color: var(--accent); }
        """
        findings = find_accent_text_on_dark_in_css(css, file_path="<test>")
        self.assertEqual(findings, [])

    def test_scanner_ignores_non_text_accent_uses(self):
        # Only `color: var(--accent)` is the AP-4 fingerprint. Border /
        # outline / background / shadow uses of accent are explicitly
        # decorative under DS-15 and must not surface as findings.
        css = """
            .cs-section.dark em { border-color: var(--accent); }
            .cs-cta { background: var(--accent); }
            .cs-nav .links a:focus-visible { outline-color: var(--accent); }
            .cs-foot .top h5 { box-shadow: 0 0 4px var(--accent); }
        """
        findings = find_accent_text_on_dark_in_css(css, file_path="<test>")
        self.assertEqual(findings, [])

    def test_scanner_normalises_whitespace_for_baseline_match(self):
        css = """
            .cs-section.dark      em
              {   color : var(  --accent  )  ;   }
        """
        findings = find_accent_text_on_dark_in_css(css, file_path="<test>")
        self.assertEqual(len(findings), 1)
        # Whitespace inside the selector is collapsed so a future
        # CSS-formatter pass cannot silently invalidate the baseline.
        self.assertEqual(findings[0].normalised_selector, ".cs-section.dark em")

    def test_parse_css_rules_walks_nested_media_blocks(self):
        css = """
            @media (min-width: 960px) {
                .cs-cta em { color: var(--accent); }
            }
            .cs-section.dark em { color: var(--accent); }
        """
        rules = list(parse_css_rules(css))
        # The walker recurses into the @media wrapper and surfaces both
        # inner rules with their original selectors.
        selectors = [r[0].strip() for r in rules]
        self.assertIn(".cs-cta em", selectors)
        self.assertIn(".cs-section.dark em", selectors)

    def test_dark_band_classes_cover_the_documented_archetype(self):
        # Lock the canonical dark-band vocabulary — adding a new dark
        # band to the archetype must be a deliberate change in this
        # module + a fresh baseline review.
        for klass in (
            ".cs-nav", ".cs-section.dark", ".cs-kpi-band",
            ".cs-cta", ".cs-foot",
        ):
            self.assertIn(klass, DARK_BAND_CLASSES)


# ── 4. Chrome enumeration ────────────────────────────────────────────


class ChromeAuditTests(TestCase):
    """``audit_chrome_for_ap4`` returns the live aggregate over every
    chrome HTML file under
    ``templates/live_templates/business/corporate-suite/``.
    """

    def test_audit_walks_every_chrome_file(self):
        report = audit_chrome_for_ap4()
        # _base.html + every _layouts/lf*/styles.html.
        self.assertGreaterEqual(len(report.files_scanned), 4)
        self.assertTrue(any("_base.html" in p for p in report.files_scanned))
        self.assertTrue(any("_layouts" in p for p in report.files_scanned))

    def test_audit_finds_at_least_the_baseline_selectors(self):
        # The baseline pins selectors that exist in the chrome today.
        # The audit must surface every one of them — if a baseline
        # selector is missing, that is the W004 cleanup signal.
        report = audit_chrome_for_ap4()
        for selector in KNOWN_AP4_BASELINE_SELECTORS:
            self.assertIn(
                selector,
                report.selectors_seen,
                f"baseline selector {selector!r} missing — see W004",
            )

    def test_audit_reports_zero_regressions_on_current_state(self):
        # The whole point of the X.4b detection layer: any selector NOT
        # pinned in KNOWN_AP4_BASELINE_SELECTORS that paints accent text
        # on a dark band is a regression. Current state ships clean.
        report = audit_chrome_for_ap4()
        regressions = report.regressions
        self.assertEqual(
            regressions,
            [],
            "Unexpected dark-band accent-text rule(s): "
            + "; ".join(
                f"{r.normalised_selector!r} at {r.file_path}:{r.line_no}"
                for r in regressions
            ),
        )


# ── 5. Enrolled-palette audit ────────────────────────────────────────


class EnrolledPaletteAuditTests(TestCase):
    """``audit_enrolled_palettes`` exercises every corporate-suite slug
    declared in ``SEED_TEMPLATES`` and returns a stable verdict per slug.
    """

    def test_audit_returns_one_finding_per_enrolled_slug(self):
        findings = audit_enrolled_palettes()
        slugs = {f.slug for f in findings}
        # Every known enrolled corporate-suite slug shows up in the
        # audit. Missing slugs would mean the seed source moved and the
        # check is silently skipping templates.
        for expected in (
            "pragma-corporate-suite",
            "fiscus-commercialista",
            "solaria-coaching",
        ):
            self.assertIn(expected, slugs)

    def test_pragma_passes_aa_text_floor(self):
        findings = {f.slug: f for f in audit_enrolled_palettes()}
        pragma = findings["pragma-corporate-suite"]
        self.assertTrue(pragma.passes_aa_text_floor)
        self.assertEqual(pragma.severity, "ok")

    def test_legacy_exempt_palettes_surface_as_warning_not_error(self):
        findings = {f.slug: f for f in audit_enrolled_palettes()}
        for slug in LEGACY_AP4_PALETTE_EXEMPT_SLUGS:
            if slug not in findings:
                # The slug may not be in seed yet (Solaria stays at
                # tier=draft per AP-15 fence) — skip silently if so.
                continue
            f = findings[slug]
            self.assertFalse(f.passes_aa_text_floor, slug)
            self.assertTrue(f.is_legacy_exempt, slug)
            self.assertEqual(f.severity, "warning", slug)

    def test_no_unexpected_failing_palette(self):
        # Every failing palette must be on the documented exemption
        # list. A failing slug not on the list means a new pilot
        # introduced an AP-4 cell without the prerequisite fix — the
        # E004 build-time check would catch it; this test catches it
        # one layer earlier.
        for f in audit_enrolled_palettes():
            if f.passes_aa_text_floor:
                continue
            self.assertTrue(
                f.is_legacy_exempt,
                f"slug {f.slug!r} fails accent-text-on-primary "
                f"({f.accent_on_primary}:1) but is NOT on "
                "LEGACY_AP4_PALETTE_EXEMPT_SLUGS — add it to the "
                "exemption list with a follow-up plan reference, or "
                "swap the accent for one that clears WCAG_AA_BODY.",
            )


# ── 6. Django checks E004 / E005 + W003 / W004 ───────────────────────


class ContrastChecksRegistrationTests(TestCase):
    """The two new checks must be registered via ``CatalogConfig.ready``
    and behave correctly on the current enrolled state and on synthetic
    payloads.
    """

    def test_e004_and_e005_are_registered(self):
        from django.core.checks import registry

        registered = list(registry.registry.get_checks())
        names = {getattr(c, "__name__", "") for c in registered}
        self.assertIn(
            "check_corporate_suite_accent_contrast",
            names,
            "E004 / W003 check not registered via CatalogConfig.ready",
        )
        self.assertIn(
            "check_corporate_suite_chrome_accent_text",
            names,
            "E005 / W004 check not registered via CatalogConfig.ready",
        )

    def test_e004_accent_check_emits_only_warnings_on_current_state(self):
        # AP-4 pass 2 (2026-05-10) updated semantics:
        # - The chrome now safe-degrades accent text on dark bands via
        #   ``--accent-text-on-primary-safe`` (theme_safety token).
        # - ``CHROME_SAFE_DEGRADES_ACCENT_ON_DARK = True`` therefore
        #   marks every failing palette as ``is_legacy_exempt = True``,
        #   downgrading the finding from E004 (error) to W003 (warning).
        # - LEGACY_AP4_PALETTE_EXEMPT_SLUGS is now empty by default; the
        #   five W003 warnings we still see come from the chrome-flag
        #   logic, not from a hardcoded exemption list.
        # The contract for this test:
        #   (a) zero E004 errors on current state.
        #   (b) at least one W003 warning per failing enrolled palette
        #       (Fiscus / Solaria / Cornice / Causa / Continua).
        from apps.catalog.checks import check_corporate_suite_accent_contrast

        findings = check_corporate_suite_accent_contrast(app_configs=None)
        errors = [f for f in findings if f.id == "corporate_suite.E004"]
        warnings_found = [f for f in findings if f.id == "corporate_suite.W003"]
        self.assertEqual(
            errors,
            [],
            "Unexpected E004 errors on current state: "
            + "; ".join(str(e) for e in errors),
        )
        # At least one W003 must surface — the failing palettes still
        # have weak accent-on-primary contrast (the chrome handles it
        # via safe-degrade, but the palette itself is informational).
        self.assertGreater(
            len(warnings_found),
            0,
            "Expected at least one W003 warning for a failing "
            "enrolled palette; got zero. Either every enrolled palette "
            "now passes WCAG_AA_BODY on its primary, or the check "
            "stopped seeing seed data.",
        )

    def test_e004_fires_on_new_unexempted_failing_palette(self):
        # Inject a synthetic enrolled palette that fails the floor and
        # is NOT on the exemption list. The check must surface an
        # ERROR for it.
        from apps.catalog import checks
        from apps.catalog.cs_contrast_audit import EnrolledPaletteFinding

        original = checks.audit_enrolled_palettes
        try:
            checks.audit_enrolled_palettes = lambda: [
                EnrolledPaletteFinding(
                    slug="hypothetical-new-pilot",
                    primary="#1F2937",
                    accent="#1C3D5A",  # Fiscus-style dark-on-dark
                    accent_on_primary=1.3,
                    passes_aa_text_floor=False,
                    is_legacy_exempt=False,
                ),
            ]
            findings = checks.check_corporate_suite_accent_contrast(
                app_configs=None
            )
        finally:
            checks.audit_enrolled_palettes = original

        errors = [f for f in findings if f.id == "corporate_suite.E004"]
        self.assertEqual(len(errors), 1)
        self.assertIn("hypothetical-new-pilot", str(errors[0]))

    def test_e005_chrome_check_clean_on_current_state(self):
        # Current chrome ships exactly the four pinned baseline
        # selectors — the check must surface zero E005 errors.
        from apps.catalog.checks import check_corporate_suite_chrome_accent_text

        findings = check_corporate_suite_chrome_accent_text(app_configs=None)
        errors = [f for f in findings if f.id == "corporate_suite.E005"]
        self.assertEqual(
            errors,
            [],
            "Unexpected E005 regressions on current chrome: "
            + "; ".join(str(e) for e in errors),
        )

    def test_e005_fires_on_synthetic_new_dark_band_accent_rule(self):
        # Inject a synthetic ChromeAuditReport with a regression and
        # confirm the check raises E005.
        from apps.catalog import checks
        from apps.catalog.cs_contrast_audit import (
            ChromeAuditReport,
            CssAccentFinding,
        )

        original = checks.audit_chrome_for_ap4
        try:
            def fake_audit():
                report = ChromeAuditReport()
                report.files_scanned = ["<synthetic>"]
                report.findings = [
                    # Surface a fully-pinned baseline so .baseline_misses
                    # does not accidentally trigger W004 noise.
                    CssAccentFinding(
                        file_path="<synthetic>",
                        selector=s,
                        line_no=1,
                    )
                    for s in KNOWN_AP4_BASELINE_SELECTORS
                ]
                # Plus one new rule that violates the contract.
                report.findings.append(
                    CssAccentFinding(
                        file_path="<synthetic>",
                        selector=".cs-section.dark .new-emphasis",
                        line_no=42,
                    )
                )
                return report

            checks.audit_chrome_for_ap4 = fake_audit
            findings = checks.check_corporate_suite_chrome_accent_text(
                app_configs=None
            )
        finally:
            checks.audit_chrome_for_ap4 = original

        errors = [f for f in findings if f.id == "corporate_suite.E005"]
        self.assertEqual(len(errors), 1)
        self.assertIn(".cs-section.dark .new-emphasis", str(errors[0]))

    def test_w004_fires_on_stale_baseline_selector(self):
        # If a baseline selector is removed from the chrome (good — a
        # remediation pass just lifted it onto a safe token), the
        # check must surface W004 to invite a baseline cleanup.
        from apps.catalog import checks
        from apps.catalog.cs_contrast_audit import ChromeAuditReport

        original = checks.audit_chrome_for_ap4
        try:
            def fake_audit():
                report = ChromeAuditReport()
                report.files_scanned = ["<synthetic>"]
                # Empty findings → every pinned baseline selector is
                # now "stale" and must surface as W004.
                report.findings = []
                return report

            checks.audit_chrome_for_ap4 = fake_audit
            findings = checks.check_corporate_suite_chrome_accent_text(
                app_configs=None
            )
        finally:
            checks.audit_chrome_for_ap4 = original

        warnings_found = [f for f in findings if f.id == "corporate_suite.W004"]
        # One W004 per pinned baseline selector.
        self.assertEqual(len(warnings_found), len(KNOWN_AP4_BASELINE_SELECTORS))


# ── 7. End-to-end: theme_safety + cs_contrast_audit handshake ────────


class ThemeSafetyAndContrastAuditHandshakeTests(TestCase):
    """The X.4a ``theme_safety`` enrichment computes
    ``accent_on_primary_contrast`` per theme, and the X.4b audit module
    consumes the same WCAG primitive. These tests confirm the two
    layers agree on every enrolled palette so a future drift between
    them surfaces immediately.
    """

    def test_enrich_and_audit_agree_on_pragma(self):
        from apps.catalog.theme_safety import enrich_corporate_suite_theme

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            enriched = enrich_corporate_suite_theme(
                {"primary": "#1E293B", "accent": "#10B981"},
                template_slug="pragma-corporate-suite",
            )
        report = palette_pair_audit(
            "pragma-corporate-suite",
            {"primary": "#1E293B", "secondary": "#3B82F6", "accent": "#10B981"},
        )
        self.assertAlmostEqual(
            enriched["accent_on_primary_contrast"],
            report.accent_on_primary,
            places=2,
        )

    def test_enrich_and_audit_agree_on_fiscus(self):
        from apps.catalog.theme_safety import enrich_corporate_suite_theme

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            enriched = enrich_corporate_suite_theme(
                {"primary": "#1F2937", "accent": "#1C3D5A"},
                template_slug="fiscus-commercialista",
            )
        report = palette_pair_audit(
            "fiscus-commercialista",
            {"primary": "#1F2937", "secondary": "#B58F4A", "accent": "#1C3D5A"},
        )
        self.assertAlmostEqual(
            enriched["accent_on_primary_contrast"],
            report.accent_on_primary,
            places=2,
        )
        # And the failing-state agreement: enrich computes the ratio,
        # audit gates it.
        self.assertFalse(report.accent_text_on_primary_passes_aa)
        self.assertLess(enriched["accent_on_primary_contrast"], WCAG_AA_BODY)
