"""Editor schema — DNA-locked vs editable field whitelist.

Per EDITOR_SCHEMA_BLUEPRINT.md and D-083: the archetype decides the
structural DNA (section order, hero style, navbar style, conversion
pattern, page kinds). The editor customer controls copy + palette +
fonts + selected content slots. Structural / conversion keys are
locked; attempting to write them from the service layer raises
``InvalidEditableField``.

Foundation v1 (D-085 Phase A.1) ships the whitelist for ONE
archetype — `agency-creative-studio` (Vertex). Extending to other
archetypes is mechanical: copy the pattern, add entries, ship.

Shape of each schema entry::

    {
        "label": "Headline",         # UI label
        "type": "text"|"textarea"|"richtext"|"color"|"font"|"select",
        "help": "...",                # optional UI help text
        "max_length": 140,            # optional soft constraint
        "choices": [...],             # for select / font
    }

Locked keys — and anything NOT in this whitelist — cannot be written.
"""
from __future__ import annotations

from typing import Any

from apps.projects.models import ProjectDesignTokens


# ---------------------------------------------------------------------------
# Design-token schema (global to all archetypes for now)
# ---------------------------------------------------------------------------

DESIGN_TOKEN_FIELDS: dict[str, dict[str, Any]] = {
    "palette_primary": {
        "label": "Primary colour",
        "type": "color",
        "help": "Used for focused states, underlines, accent text.",
    },
    "palette_secondary": {
        "label": "Secondary colour",
        "type": "color",
        "help": "Background variants, subdued surfaces.",
    },
    "palette_accent": {
        "label": "Accent colour",
        "type": "color",
        "help": "Buttons, highlights, dots, active states.",
    },
    "heading_font": {
        "label": "Heading font",
        "type": "select",
        "choices": ProjectDesignTokens.CURATED_FONTS,
    },
    "body_font": {
        "label": "Body font",
        "type": "select",
        "choices": ProjectDesignTokens.CURATED_FONTS,
    },
}


# ---------------------------------------------------------------------------
# Per-archetype content schema
#
# Foundation v1 exposes a deliberately tight set of fields — the
# minimum that exercises the end-to-end editor loop without demanding
# the full blueprint on day one. Each field block lists its UI group,
# the editable key paths, and the widget type.
#
# Any key not listed here (e.g. `home.ledger_rows`, `home.cover.image`,
# `home.capab_items`) is DNA-locked in this slice. Phase A.2+ opens up
# repeater widgets for lists.
# ---------------------------------------------------------------------------

AGENCY_CREATIVE_STUDIO_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "site",
        "label": "Identità dello studio",
        "help": "Dati di contatto e voce editoriale dell'intestazione e del footer.",
        "fields": [
            ("site.logo_word", {"label": "Logo word", "type": "text", "max_length": 32}),
            ("site.tag",       {"label": "Tagline",   "type": "text", "max_length": 80}),
            ("site.availability", {"label": "Disponibilità", "type": "text", "max_length": 80}),
            ("site.nav_cta",   {"label": "CTA nav",   "type": "text", "max_length": 32}),
            ("site.phone",     {"label": "Telefono",  "type": "text", "max_length": 40}),
            ("site.email",     {"label": "Email",     "type": "text", "max_length": 80}),
            ("site.address",   {"label": "Indirizzo", "type": "text", "max_length": 120}),
            ("site.hours_compact", {"label": "Orari studio", "type": "text", "max_length": 80}),
            ("site.footer_intro",  {"label": "Footer · intro studio", "type": "textarea", "max_length": 400}),
            ("site.foot_standfirst", {"label": "Footer · standfirst", "type": "textarea", "max_length": 400}),
        ],
    },
    {
        "id": "home",
        "label": "Pagina Home",
        "help": "Hero, manifesto e call-to-action della home.",
        "fields": [
            ("home.eyebrow",      {"label": "Eyebrow",        "type": "text",     "max_length": 100}),
            ("home.headline",     {"label": "Headline (hero)","type": "richtext", "max_length": 160,
                                   "help": "HTML limitato: <em> è consentito per gli accenti italici serif."}),
            ("home.pull_quote",   {"label": "Pull-quote",     "type": "textarea", "max_length": 400}),
            ("home.intro",        {"label": "Intro",          "type": "textarea", "max_length": 600}),
            ("home.primary_cta",  {"label": "CTA primaria · label",    "type": "text", "max_length": 40}),
            ("home.primary_href", {"label": "CTA primaria · page slug", "type": "select",
                                   "choices": ["home", "studio", "capacita", "lavori", "manifesto", "contatti"]}),
            ("home.secondary_cta",  {"label": "CTA secondaria · label",    "type": "text", "max_length": 40}),
            ("home.secondary_href", {"label": "CTA secondaria · page slug", "type": "select",
                                     "choices": ["home", "studio", "capacita", "lavori", "manifesto", "contatti"]}),
            ("home.manifesto_heading", {"label": "Manifesto · heading", "type": "richtext", "max_length": 200}),
            ("home.manifesto_body",    {"label": "Manifesto · body",    "type": "textarea", "max_length": 800}),
            ("home.cta_heading",   {"label": "Blocco CTA · heading", "type": "richtext", "max_length": 200}),
            ("home.cta_sub",       {"label": "Blocco CTA · descrizione", "type": "textarea", "max_length": 400}),
            ("home.cta_primary",   {"label": "Blocco CTA · label",  "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "studio",
        "label": "Pagina Studio",
        "help": "About / chi siamo.",
        "fields": [
            ("studio.eyebrow",  {"label": "Eyebrow",  "type": "text", "max_length": 100}),
            ("studio.headline", {"label": "Headline", "type": "richtext", "max_length": 200}),
        ],
    },
    {
        "id": "contatti",
        "label": "Pagina Contatti",
        "help": "Inquiry form headline e copy.",
        "fields": [
            ("contatti.eyebrow",  {"label": "Eyebrow",  "type": "text", "max_length": 100}),
            ("contatti.headline", {"label": "Headline", "type": "richtext", "max_length": 200}),
            ("contatti.intro",    {"label": "Intro",    "type": "textarea", "max_length": 500}),
        ],
    },
]


# Keys explicitly documented as DNA-locked (surfaced in the editor UI
# as a read-only "Perché non è modificabile?" note). These are the
# structural decisions the archetype owns — exposing them would be a
# D-054 Premium Differentiation Law violation per EDITOR_SCHEMA_BLUEPRINT
# §1.1–1.3.
LOCKED_KEYS_NOTE: dict[str, str] = {
    "home.ledger_rows":
        "Il registro lavori è una lista curata del tuo portfolio — verrà editabile "
        "nella Phase A.2 (repeater widget).",
    "home.capab_items":
        "Le capacità dello studio hanno una griglia archetipo — personalizzabili "
        "nella Phase A.2.",
    "home.cover":
        "Immagini di copertina richiedono upload asset — disponibili nella Phase A.6.",
    "section_order":
        "L'ordine delle sezioni è parte del DNA dell'archetipo (D-054). "
        "Cambiarlo rientra nella Phase A.2+.",
    "navbar_style":
        "Lo stile della navbar è DNA-locked — un cambio richiede un archetipo diverso.",
    "hero_style":
        "Lo stile dell'hero è DNA-locked per preservare il premium differentiation "
        "(D-054, 10-gate matrix).",
    "pages":
        "La lista pagine è archetipo-driven in Foundation v1 — nuove pagine "
        "opt-in arrivano nella Phase A.4.",
}


# ---------------------------------------------------------------------------
# Schema lookup
# ---------------------------------------------------------------------------

_ARCHETYPE_SCHEMAS: dict[str, list[dict[str, Any]]] = {
    "agency-creative-studio": AGENCY_CREATIVE_STUDIO_SCHEMA,
}


class InvalidEditableField(Exception):
    """Raised when a write targets a key not in the archetype whitelist."""


def get_schema(archetype: str) -> list[dict[str, Any]] | None:
    """Return the editable-field schema for an archetype, or None."""
    return _ARCHETYPE_SCHEMAS.get(archetype)


def is_supported_archetype(archetype: str) -> bool:
    return archetype in _ARCHETYPE_SCHEMAS


def iter_editable_fields(archetype: str) -> list[tuple[str, dict[str, Any]]]:
    """Flat list of (key_path, field_spec) tuples for an archetype."""
    schema = get_schema(archetype)
    if not schema:
        return []
    return [pair for group in schema for pair in group["fields"]]


def get_field_spec(archetype: str, key_path: str) -> dict[str, Any] | None:
    """Look up the widget spec for a key_path (None if not editable)."""
    for path, spec in iter_editable_fields(archetype):
        if path == key_path:
            return spec
    return None


def validate_key_path(archetype: str, key_path: str) -> None:
    """Raise ``InvalidEditableField`` if the path is DNA-locked."""
    if get_field_spec(archetype, key_path) is None:
        raise InvalidEditableField(
            f"Field '{key_path}' is not editable for archetype "
            f"'{archetype}'. It is either DNA-locked or out of scope "
            f"for Foundation v1."
        )


def validate_value(archetype: str, key_path: str, value: Any) -> Any:
    """Lightweight value validation per field spec. Returns the coerced value."""
    spec = get_field_spec(archetype, key_path)
    if spec is None:
        raise InvalidEditableField(key_path)

    # Strip strings and cap length
    if spec["type"] in {"text", "textarea", "richtext"} and isinstance(value, str):
        value = value.strip()
        max_len = spec.get("max_length")
        if max_len and len(value) > max_len:
            value = value[:max_len]

    if spec["type"] == "select":
        choices = spec.get("choices") or []
        if value not in choices:
            raise InvalidEditableField(
                f"Value {value!r} is not a valid choice for {key_path}. "
                f"Allowed: {choices}"
            )

    if spec["type"] == "color":
        if not isinstance(value, str) or not value.startswith("#"):
            raise InvalidEditableField(
                f"Value {value!r} is not a valid hex colour for {key_path}."
            )

    return value
