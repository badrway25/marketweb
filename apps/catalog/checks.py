"""Corporate-suite archetype build-time gates (Phase X.4a Step 2 · P0-1 / P0-2).

Scope
-----
These checks promote two archetype-level contracts from runtime
``UserWarning`` (the Step 1A / Step 1C posture) to build-time failures
via ``django.core.checks``. They fire on every ``manage.py check`` and
every ``manage.py test`` invocation, so a regression re-introducing a
Solaria-class palette defect or a non-Pexels pool URL fails CI before
review — the floor the X.4a hardening plan requires.

What these checks enforce
-------------------------
1. ``corporate_suite.E001`` (T-P0-1) — every enrolled ``corporate-suite``
   template must ship a ``--primary`` that passes
   ``theme_safety.is_primary_safe_on_cream``. The source of truth for
   the enrolled palettes is ``SEED_TEMPLATES`` in
   ``apps/catalog/management/commands/seed_templates.py`` (static — no
   DB hit). Failure ⇒ CI exits non-zero with an ``Error`` naming the
   offending slug + hex.

2. ``corporate_suite.E002`` (T-P0-2) — every registered pool in
   ``CORPORATE_SUITE_POOL_KEYS`` minus ``LEGACY_EXEMPT_KEYS`` must ship
   Pexels-only URLs. ``LEGACY_EXEMPT_KEYS`` is empty in main since
   Sprint 1 T13 (AP-2 closure on 2026-05-10 · the legacy carve-out for
   Pragma's ``business-corporate`` pool was retired). Any future pool
   enrolled there is reported as ``corporate_suite.W001`` (Warning)
   so the pending-retro state stays visible without blocking the
   gate — but the project ships zero W001 today.

Why static (not DB) is correct here
-----------------------------------
The seed data is the authoritative declaration of what ships. A palette
that is not in ``SEED_TEMPLATES`` has not been enrolled. Reading from
the DB would be subject to migration order + fixture state — fragile in
CI. Reading the seed module is deterministic and works on any
checkout.

Cross-references
----------------
- ``apps/catalog/theme_safety.py`` — ``is_primary_safe_on_cream``.
- ``apps/catalog/imagery_policy.py`` —
  ``validate_corporate_suite_imagery_key`` + ``CORPORATE_SUITE_POOL_KEYS``
  + ``LEGACY_EXEMPT_KEYS``.
- ``factory/standards/corporate-suite-design-standard.md`` §CS-PAL-01.
- ``factory/standards/corporate-suite-imagery-standard.md`` §CS-IMG-SRC-01.
- ``factory/reports/hardening/step2-followup-plan.md`` §T-P0-1 / §T-P0-2.
"""
from __future__ import annotations

from typing import Iterable

from django.core.checks import Error, Warning as ChecksWarning

from apps.catalog.cs_contrast_audit import (
    LEGACY_AP4_PALETTE_EXEMPT_SLUGS,
    WCAG_AA_BODY,
    audit_chrome_for_ap4,
    audit_enrolled_palettes,
)
from apps.catalog.imagery_policy import (
    CORPORATE_SUITE_ARCHETYPE,
    CORPORATE_SUITE_POOL_KEYS,
    LEGACY_EXEMPT_KEYS,
    validate_corporate_suite_imagery_key,
)
from apps.catalog.theme_safety import is_primary_safe_on_cream


# ---------------------------------------------------------------------------
# Helpers — iterate enrolled corporate-suite templates from the seed source.
# ---------------------------------------------------------------------------

def _enrolled_corporate_suite_palettes() -> Iterable[tuple[str, str]]:
    """Yield ``(slug, primary_hex)`` for every enrolled corporate-suite
    template.

    The pairing is computed from two static registries:

    - ``apps.catalog.template_dna.TEMPLATE_DNA`` — authoritative source
      for ``archetype`` per slug.
    - ``apps.catalog.management.commands.seed_templates.SEED_TEMPLATES``
      — authoritative source for the brand ``palette`` per slug.

    Deferred imports isolate any circular-import risk during app startup.
    """
    from apps.catalog.management.commands.seed_templates import SEED_TEMPLATES
    from apps.catalog.template_dna import TEMPLATE_DNA

    for entry in SEED_TEMPLATES:
        slug = entry.get("slug")
        dna = TEMPLATE_DNA.get(slug) if slug else None
        if not dna or dna.get("archetype") != CORPORATE_SUITE_ARCHETYPE:
            continue
        brand = entry.get("brand") or {}
        palette = brand.get("palette") or {}
        primary = palette.get("primary")
        if not primary:
            continue
        yield slug, primary


# ---------------------------------------------------------------------------
# Registered check functions
# ---------------------------------------------------------------------------

def check_corporate_suite_palettes(app_configs, **kwargs):  # noqa: ARG001
    """T-P0-1 · Fail when any enrolled corporate-suite ``--primary`` is
    unsafe on cream paper (CS-PAL-01).

    Each defect surfaces as ``django.core.checks.Error`` with id
    ``corporate_suite.E001``. ``manage.py check`` exits non-zero when
    one or more Errors are returned.
    """
    errors: list[Error] = []
    for slug, primary_hex in _enrolled_corporate_suite_palettes():
        is_safe, lum, ratio = is_primary_safe_on_cream(primary_hex)
        if is_safe:
            continue
        errors.append(
            Error(
                (
                    f"corporate-suite template {slug!r} ships an unsafe "
                    f"primary {primary_hex!r} "
                    f"(luminance={lum:.4f}, contrast-vs-cream={ratio:.2f}). "
                    "CS-PAL-01 requires luminance ≤ 0.12 and contrast ≥ "
                    "7.0:1 against the cream body paper. The dark skin "
                    "surfaces (navbar, KPI band, footer) paint cream on "
                    "primary — a light primary makes every h1/h2/h3 on "
                    "the body paper unreadable (Solaria Commit A incident)."
                ),
                hint=(
                    "Swap the palette entry in "
                    "apps/catalog/management/commands/seed_templates.py "
                    "SEED_TEMPLATES for a primary with luminance ≤ 0.12 "
                    "(typically a navy / charcoal / slate in the "
                    "#0F172A .. #2C1810 band)."
                ),
                obj=slug,
                id="corporate_suite.E001",
            )
        )
    return errors


def check_corporate_suite_imagery(app_configs, **kwargs):  # noqa: ARG001
    """T-P0-2 · Fail when any non-legacy-exempt corporate-suite imagery
    pool ships a non-Pexels URL (CS-IMG-SRC-01).

    Reports the legacy-exempt ``business-corporate`` pool as a
    ``Warning`` (``corporate_suite.W001``) so the grandfather stays
    visible without blocking CI.
    """
    findings: list[Error | ChecksWarning] = []
    for key in sorted(CORPORATE_SUITE_POOL_KEYS):
        report = validate_corporate_suite_imagery_key(key)
        # If the pool key is not registered in IMAGERY_CONFIG (e.g.
        # Solaria stays deferred), skip silently — the archetype is
        # gated by the imagery_policy module's own dispatcher and
        # there is nothing to validate yet.
        if not report.is_known:
            continue

        if key in LEGACY_EXEMPT_KEYS:
            if not report.pexels_only:
                findings.append(
                    ChecksWarning(
                        (
                            f"corporate-suite imagery pool {key!r} is "
                            "grandfathered under LEGACY_EXEMPT_KEYS and "
                            f"ships {len(report.non_pexels_urls)} "
                            "non-Pexels url(s) pending AP3 retro-curation. "
                            "The archetype accepts this; the gatekeeper "
                            "must cite it explicitly (O7 precondition)."
                        ),
                        obj=key,
                        id="corporate_suite.W001",
                    )
                )
            continue

        if not report.pexels_only:
            findings.append(
                Error(
                    (
                        f"corporate-suite imagery pool {key!r} ships "
                        f"{len(report.non_pexels_urls)} non-Pexels url(s). "
                        "CS-IMG-SRC-01 requires every new corporate-suite "
                        "url to come from images.pexels.com. Offending: "
                        + ", ".join(report.non_pexels_urls[:3])
                        + ("" if len(report.non_pexels_urls) <= 3 else ", …")
                    ),
                    hint=(
                        "Swap the offending urls in "
                        "apps/catalog/preview_imagery.py IMAGERY_CONFIG "
                        "with Pexels CDN equivalents, or enroll the pool "
                        "under LEGACY_EXEMPT_KEYS with a dated retro-"
                        "curation backlog entry (discouraged)."
                    ),
                    obj=key,
                    id="corporate_suite.E002",
                )
            )

        if not report.shape_is_canonical:
            findings.append(
                Error(
                    (
                        f"corporate-suite imagery pool {key!r} has a "
                        "non-canonical shape; CS-IMG-POOL-01 requires "
                        "exactly 6 urls in the [hero, feature, portrait, "
                        "portrait, detail, ambient] slot order."
                    ),
                    obj=key,
                    id="corporate_suite.E003",
                )
            )
    return findings


# ---------------------------------------------------------------------------
# Phase X.4b · AP-4 mechanical contrast enforcement
# ---------------------------------------------------------------------------

def check_corporate_suite_accent_contrast(app_configs, **kwargs):  # noqa: ARG001
    """AP-4 pass 1 · Fail when an enrolled corporate-suite accent fails the
    WCAG AA body floor against its own primary AND that palette is not on
    the documented legacy exemption list.

    Each defect surfaces as ``django.core.checks.Error`` with id
    ``corporate_suite.E004``. Documented legacy debt surfaces as
    ``django.core.checks.Warning`` with id ``corporate_suite.W003`` so it
    stays visible on every ``manage.py check`` invocation without blocking
    CI on the in-flight remediation.

    Cross-references
    ----------------
    - DS-16 (factory design standard): never use ``--accent`` as text on
      ``--primary``. The four chrome rules currently violating this for
      Fiscus / Solaria / Cornice / Causa are the AP-4 baseline carried by
      ``apps.catalog.cs_contrast_audit.KNOWN_AP4_BASELINE_SELECTORS``.
    - BO-08 (factory scorecard override): ``color: var(--accent)`` used
      as text on ``var(--primary)`` is an automatic override; the build-
      time gate makes a *new* failing palette catch on this rule before
      the gatekeeper walk is scheduled.
    - BLOCK-11 (factory blocking-rules): WCAG AA body text on a sampled
      pixel; the live-walk auditor still runs (BR-20) — this build-time
      gate is the *upstream* sentinel.
    """
    findings: list[Error | ChecksWarning] = []
    for f in audit_enrolled_palettes():
        if f.passes_aa_text_floor:
            continue
        if f.is_legacy_exempt:
            findings.append(
                ChecksWarning(
                    (
                        f"corporate-suite template {f.slug!r} ships an accent "
                        f"{f.accent!r} on primary {f.primary!r} with a contrast "
                        f"ratio of {f.accent_on_primary:.2f}:1 (AA body floor "
                        f"{WCAG_AA_BODY:.1f}:1). The palette accent is too "
                        "weak to read as text on the dark band, but the "
                        "chrome safe-degrades it via the "
                        "`--accent-text-on-primary-safe` token (see "
                        "apps.catalog.theme_safety) — italic emphasis on "
                        "dark bands renders cream-on-dark instead of "
                        "unreadable accent-on-dark. This Warning surfaces "
                        "the palette weakness so it stays visible during "
                        "review; no remediation blocks CI."
                    ),
                    obj=f.slug,
                    id="corporate_suite.W003",
                )
            )
            continue
        findings.append(
            Error(
                (
                    f"corporate-suite template {f.slug!r} ships an accent "
                    f"{f.accent!r} that fails the AA body floor on its "
                    f"primary {f.primary!r}: contrast ratio "
                    f"{f.accent_on_primary:.2f}:1, required ≥ "
                    f"{WCAG_AA_BODY:.1f}:1 (DS-16 / BO-08 / BLOCK-11). The "
                    "archetype's chrome paints accent as text on dark "
                    "bands (.cs-section.dark em, .cs-cta h2 em, .cs-foot "
                    "em, .cs-foot-col--whistleblowing — see "
                    "apps.catalog.cs_contrast_audit."
                    "KNOWN_AP4_BASELINE_SELECTORS) so a failing accent "
                    "lands as unreadable italic emphasis on the live "
                    "skin. Pick an accent with ≥ 4.5:1 against primary, "
                    "OR if the palette is intentional add the slug to "
                    "LEGACY_AP4_PALETTE_EXEMPT_SLUGS together with a "
                    "follow-up plan reference (the exemption surfaces as "
                    "a visible Warning, not a silent pass)."
                ),
                hint=(
                    "Tools: apps.catalog.cs_contrast_audit."
                    "palette_pair_audit(slug, palette) returns every "
                    "canonical pair (accent_on_primary, secondary_on_"
                    "primary, accent_on_paper, ...). Pick a darker / "
                    "brighter accent until accent_on_primary clears 4.5."
                ),
                obj=f.slug,
                id="corporate_suite.E004",
            )
        )
    return findings


def check_corporate_suite_chrome_accent_text(app_configs, **kwargs):  # noqa: ARG001
    """AP-4 pass 1 · Fail when the corporate-suite live chrome contains a
    ``color: var(--accent)`` rule whose selector touches a known dark-band
    class AND that selector is NOT pinned in
    ``KNOWN_AP4_BASELINE_SELECTORS``.

    Each *new* dark-band accent-text rule surfaces as
    ``django.core.checks.Error`` with id ``corporate_suite.E005``. A
    pinned baseline selector that no longer appears in the chrome
    surfaces as ``django.core.checks.Warning`` ``corporate_suite.W004``
    (a hint to clean up the baseline once a remediation pass deletes
    one of the four documented sites — keeping the regression guard
    accurate).

    Cross-references
    ----------------
    - ``apps.catalog.cs_contrast_audit.audit_chrome_for_ap4`` — scanner.
    - DS-16 / BR-20 / BO-08 / BLOCK-11 (same rules as E004).
    """
    findings: list[Error | ChecksWarning] = []
    report = audit_chrome_for_ap4()
    for finding in report.regressions:
        findings.append(
            Error(
                (
                    f"corporate-suite chrome contains a new dark-band "
                    f"accent-text rule at {finding.file_path}:"
                    f"{finding.line_no} — selector "
                    f"{finding.normalised_selector!r}. DS-16 / BO-08 / "
                    "BLOCK-11 — `color: var(--accent)` rendered as text "
                    "on a dark band fails AA on multiple enrolled "
                    "palettes (Fiscus / Solaria / Cornice / Causa). The "
                    "AP-4 baseline pins exactly the four legacy "
                    "selectors that already shipped this pattern; any "
                    "new selector adds to the trap and must be lifted "
                    "onto a safe-degrading token, removed, or — if the "
                    "addition is deliberate — added to "
                    "KNOWN_AP4_BASELINE_SELECTORS together with a "
                    "follow-up entry in the AP-4 pass-2 plan."
                ),
                hint=(
                    "If the rule is not text (e.g. it sets a "
                    "border-color or outline-color), restate it as such — "
                    "the scanner intentionally only flags the literal "
                    "`color: var(--accent)` text declaration."
                ),
                obj=finding.normalised_selector,
                id="corporate_suite.E005",
            )
        )
    for stale in sorted(report.baseline_misses):
        findings.append(
            ChecksWarning(
                (
                    f"corporate-suite AP-4 baseline selector {stale!r} no "
                    "longer appears in the chrome — the regression guard "
                    "is now slightly over-strict. After verifying the "
                    "selector was deleted intentionally (not renamed), "
                    "remove it from "
                    "apps.catalog.cs_contrast_audit."
                    "KNOWN_AP4_BASELINE_SELECTORS so the baseline "
                    "stays accurate."
                ),
                obj=stale,
                id="corporate_suite.W004",
            )
        )
    return findings
