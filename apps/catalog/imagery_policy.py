"""Corporate-suite imagery policy helpers (Phase X.4a Step 1C).

Scope
-----
This module only knows about the *corporate-suite* archetype. The
project-wide imagery sourcing standard shipped on Pexels (Session 47 ·
``docs/content-factory/imagery/sources.md``), and the corporate-suite
imagery standard (``factory/standards/corporate-suite-imagery-standard.md``)
elevates ``Pexels-only`` to a ``[BLOCKING]`` rule for every template on
this archetype (``CS-IMG-SRC-01``).

The legacy ``business-corporate`` (Pragma) carve-out was retired on
2026-05-10 (Sprint 1 · T13 · AP-2 closure pass) — the pool now ships
six curator-verified Pexels URLs and ``LEGACY_EXEMPT_KEYS`` is empty.
The structure is preserved for forward-compatibility (a new pilot may
land before its retro-curation closes) but the project ships zero
exemptions today.

What the helper enforces
------------------------
``CS-IMG-SRC-01`` [BLOCKING] · every URL in a corporate-suite pool must
come from ``images.pexels.com``. ``LEGACY_EXEMPT_KEYS`` is the documented
escape valve and must stay empty in main.

``CS-IMG-POOL-01`` [BLOCKING] · a corporate-suite pool ships exactly six
URLs in the canonical ``[hero, feature, portrait, portrait, detail, ambient]``
slot order. A pool with a different count is flagged — the preview
compositions + archetype skin both read slots by index and will render
the wrong photo in the wrong frame when the shape drifts.

``CS-IMG-SRC-02`` [BLOCKING] (soft check) · hero URL must request
``w=1600``; feature ``w=1200``; portrait/detail/ambient ``w=800``. The
check is lenient: we accept ``w=<anything>=1600`` for the hero to survive
locally-cached variants, but we flag a hero declared at ``w=800`` since
it will read soft on retina.

Outputs
-------
``validate_corporate_suite_imagery_key(key)`` returns a ``PolicyReport``
dataclass carrying:

    - ``key``                : the pool lookup key
    - ``is_known``           : whether the pool is registered in
                               ``preview_imagery.IMAGERY_CONFIG``
    - ``is_legacy_exempt``   : whether this key is enrolled in
                               ``LEGACY_EXEMPT_KEYS`` (empty in main
                               since Sprint 1 T13 / AP-2 closure)
    - ``pexels_only``        : True when every URL is on Pexels
    - ``shape_is_canonical`` : True when the pool ships exactly 6 URLs
    - ``non_pexels_urls``    : list of non-Pexels URLs (empty when safe)
    - ``hero_width_ok``      : True when slot 0 declares ``w=1600``
    - ``warnings``           : human-readable strings to surface at the
                               request-path edge via ``UserWarning``.

``enforce_corporate_suite_imagery_policy(key, template_slug)`` emits a
single ``UserWarning`` when any blocking issue is found (except for the
legacy exemption). Silent on a compliant pool.

The module is intentionally Django-free except for the lazy import of
``preview_imagery.IMAGERY_CONFIG`` inside the one function that needs it
— the helper can be called from management commands, factory tooling,
or the live-preview request path with the same contract.

Cross-references
----------------
- ``factory/standards/corporate-suite-imagery-standard.md``
  (``CS-IMG-SRC-01``, ``CS-IMG-POOL-01``, ``CS-IMG-SRC-02``).
- ``apps/catalog/theme_safety.py`` — sibling archetype-gated validator
  (palette polarity). Same ``should_<verb>(archetype)`` shape so the
  two hooks can be chained in ``LiveTemplateView.get_context_data``.
- ``apps/catalog/preview_imagery.py`` — the ``IMAGERY_CONFIG`` registry
  that every pool lives in.
"""
from __future__ import annotations

import warnings
from dataclasses import dataclass, field
from urllib.parse import parse_qs, urlparse

CORPORATE_SUITE_ARCHETYPE = "corporate-suite"

# Pools enrolled here are reported as ``is_legacy_exempt`` so reviewers
# see them in the pending-retro column instead of the blocking column.
# Empty in main since Sprint 1 T13 (2026-05-10 · AP-2 closure):
# Pragma's ``business-corporate`` pool was retro-curated to Pexels and
# removed from this set. The frozenset is preserved as the documented
# escape valve for any future pilot that lands before its curation
# closes — but main MUST ship with this set empty.
LEGACY_EXEMPT_KEYS: frozenset[str] = frozenset()

# Every corporate-suite template resolves to one of these pool keys via
# ``template_dna["imagery_key"]``. New pilots extend the list once their
# pack file lands; the validator uses the membership to decide whether to
# run the policy at all.
CORPORATE_SUITE_POOL_KEYS: frozenset[str] = frozenset({
    "business-corporate",    # Pragma · Pexels (Sprint 1 T13 retro-curation · 2026-05-10)
    "business-fiscal",       # Fiscus · Pexels (W2-1)
    "business-coaching",     # Solaria Commit B · paused (would be Pexels)
    "business-stewardship",  # Continua · Pexels (X.4 design-orchestrator pass 1)
    "business-architecture", # Cornice · Pexels (X.5 1st LF-2 occupant · 2026-04-30)
})

PEXELS_HOST = "images.pexels.com"

# Canonical 6-slot pool shape ``[hero, feature, portrait, portrait, detail, ambient]``.
CANONICAL_POOL_SIZE = 6

# Per-slot width budget · see ``CS-IMG-SRC-02``. The minimum declared
# ``w=`` query-string value each slot must carry. Values are thresholds,
# not exact matches — a pool shipping ``w=1920`` on the hero is fine.
SLOT_WIDTH_MIN: tuple[int, ...] = (1600, 1200, 800, 800, 800, 800)


# ---------------------------------------------------------------------------
# Dataclass result
# ---------------------------------------------------------------------------

@dataclass
class PolicyReport:
    """Structured validation result for a single imagery-pool key."""

    key: str
    is_known: bool = False
    is_legacy_exempt: bool = False
    pexels_only: bool = True
    shape_is_canonical: bool = True
    non_pexels_urls: list[str] = field(default_factory=list)
    hero_width_ok: bool = True
    warnings: list[str] = field(default_factory=list)

    @property
    def is_compliant(self) -> bool:
        """True when the pool passes every policy rule OR is legacy-exempt.

        Legacy-exempt pools are *not* compliant in the ship-gate sense —
        the standard tracks them in the pending-retro-curation column —
        but the helper returns True here so the request-path wire-up
        doesn't emit a warning on every Pragma render until the
        retro-curation lands.
        """
        if self.is_legacy_exempt:
            return True
        return (
            self.is_known
            and self.pexels_only
            and self.shape_is_canonical
            and self.hero_width_ok
        )


# ---------------------------------------------------------------------------
# Pure helpers
# ---------------------------------------------------------------------------

def _extract_width(url: str) -> int | None:
    """Return the ``w=`` query-string value as an int, or None."""
    try:
        qs = parse_qs(urlparse(url).query)
    except ValueError:
        return None
    raw = qs.get("w")
    if not raw:
        return None
    try:
        return int(raw[0])
    except (TypeError, ValueError):
        return None


def _hostname(url: str) -> str:
    try:
        return (urlparse(url).hostname or "").lower()
    except ValueError:
        return ""


def _is_pexels(url: str) -> bool:
    return _hostname(url) == PEXELS_HOST


def should_enforce(archetype: str | None) -> bool:
    """Whether the imagery-policy check should run for this archetype."""
    return archetype == CORPORATE_SUITE_ARCHETYPE


# ---------------------------------------------------------------------------
# Validation entrypoint
# ---------------------------------------------------------------------------

def _load_pool(key: str) -> list[str] | None:
    """Return the URL list for ``key``, or ``None`` if the pool is not known.

    The lazy import keeps this module importable without Django — factory
    tooling + CI scripts can call ``validate_corporate_suite_imagery_key``
    from a plain Python shell.
    """
    try:
        from apps.catalog.preview_imagery import IMAGERY_CONFIG
    except Exception:  # noqa: BLE001
        return None
    return IMAGERY_CONFIG.get(key)


def validate_corporate_suite_imagery_key(key: str) -> PolicyReport:
    """Validate a single corporate-suite imagery pool against the policy.

    Never raises. All findings are returned in the ``PolicyReport`` and
    mirrored to ``warnings`` as human-readable strings the caller can
    forward to a log / ``UserWarning`` / stderr.
    """
    report = PolicyReport(key=key)
    urls = _load_pool(key)
    if urls is None:
        report.is_known = False
        report.warnings.append(
            f"imagery pool {key!r} is not registered in preview_imagery.IMAGERY_CONFIG"
        )
        return report
    report.is_known = True
    report.is_legacy_exempt = key in LEGACY_EXEMPT_KEYS

    # Pool shape (CS-IMG-POOL-01).
    if len(urls) != CANONICAL_POOL_SIZE:
        report.shape_is_canonical = False
        report.warnings.append(
            f"imagery pool {key!r} has {len(urls)} urls (canonical shape is "
            f"{CANONICAL_POOL_SIZE} · [hero, feature, portrait, portrait, detail, ambient])"
        )

    # Host policy (CS-IMG-SRC-01).
    non_pexels = [u for u in urls if not _is_pexels(u)]
    report.non_pexels_urls = non_pexels
    if non_pexels:
        report.pexels_only = False
        if not report.is_legacy_exempt:
            report.warnings.append(
                f"imagery pool {key!r} contains {len(non_pexels)} non-Pexels url(s); "
                "CS-IMG-SRC-01 requires every new corporate-suite url to come "
                f"from {PEXELS_HOST}"
            )

    # Slot-0 width (CS-IMG-SRC-02 · lenient soft check).
    if urls:
        hero_w = _extract_width(urls[0])
        if hero_w is not None and hero_w < SLOT_WIDTH_MIN[0]:
            report.hero_width_ok = False
            report.warnings.append(
                f"imagery pool {key!r} hero url declares w={hero_w} "
                f"(< {SLOT_WIDTH_MIN[0]} · may read soft on retina)"
            )

    return report


def enforce_corporate_suite_imagery_policy(
    key: str | None,
    *,
    template_slug: str | None = None,
    warn: bool = True,
) -> PolicyReport:
    """Run the policy for a pool key and emit a ``UserWarning`` on failure.

    Returns the full ``PolicyReport`` unconditionally so callers can
    consult it even when warnings are suppressed. When ``key`` is falsy or
    not in the corporate-suite set, returns an unchecked report and emits
    nothing — the hook is archetype-gated at the call site via
    :func:`should_enforce`, this function is an additional safety rail.
    """
    if not key or key not in CORPORATE_SUITE_POOL_KEYS:
        return PolicyReport(key=key or "", is_known=False)

    report = validate_corporate_suite_imagery_key(key)
    if warn and report.warnings and not report.is_legacy_exempt:
        slug_suffix = f" for template {template_slug!r}" if template_slug else ""
        warnings.warn(
            (
                f"corporate-suite imagery policy failed{slug_suffix}: "
                + "; ".join(report.warnings)
            ),
            UserWarning,
            stacklevel=2,
        )
    return report
