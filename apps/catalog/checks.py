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
   Pexels-only URLs. The legacy exemption on ``business-corporate``
   (Pragma) is reported as a ``Warning`` (``corporate_suite.W001``) so
   the grandfathered state stays visible in the output without blocking
   the gate — this mirrors the ``is_legacy_exempt = True`` policy the
   Step 1C helper already encodes.

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
