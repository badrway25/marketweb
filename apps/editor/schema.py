"""Editor schema — DNA-locked vs editable field whitelist.

Per EDITOR_SCHEMA_BLUEPRINT.md and D-083: the archetype decides the
structural DNA (section order, hero style, navbar style, conversion
pattern, page kinds). The editor customer controls copy + palette +
fonts + selected content slots. Structural / conversion keys are
locked; attempting to write them from the service layer raises
``InvalidEditableField``.

Phase A.2 extends Foundation v1 (D-085) by widening the editable
whitelist for ``agency-creative-studio`` and by decorating each group
with UI-level metadata — icon + preview region — that the editor UI
uses to drive the premium sidebar and the hover-to-highlight mapping
onto the live iframe.

Shape of each schema entry::

    {
        "label": "Headline",         # UI label
        "type": "text"|"textarea"|"richtext"|"color"|"font"|"select"|"url",
        "help": "...",                # optional UI help text
        "max_length": 140,            # optional soft constraint
        "choices": [...],             # for select / font
        "placeholder": "...",         # optional field placeholder
    }

Group-level metadata (consumed by the editor UI only, never written
back to the model):

- ``icon`` — Bootstrap Icons key (e.g. ``bi-house``)
- ``region`` — CSS selector(s) on the live preview that the editor
  should flash when a field in this group gets focus/hover. The
  selector is interpreted inside the iframe by preview-bridge.js.
- ``page`` — slug of the template page a group's fields belong to,
  so the editor can navigate the preview iframe to that page before
  painting the highlight. Use ``"*"`` for chrome that appears on every
  page (navbar, footer, brand). Phase A.2.5 page-aware targeting.
- ``keywords`` — optional list of extra search tokens (synonyms,
  common customer questions, English equivalents). Consumed by the
  Phase A.2.5 command-palette search so "mail" finds the contact
  email field, "chi siamo" finds the studio page, etc. Keep it lean —
  3-6 words per group, no per-field annotation.

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
        "label": "Colore primario",
        "type": "color",
        "help": "Titoli, inchiostro principale, sfondi scuri.",
    },
    "palette_secondary": {
        "label": "Colore secondario",
        "type": "color",
        "help": "Sfondi chiari e superfici di riposo.",
    },
    "palette_accent": {
        "label": "Colore d'accento",
        "type": "color",
        "help": "Pulsanti, link, sottolineature, stati attivi.",
    },
    "heading_font": {
        "label": "Font dei titoli",
        "type": "select",
        "choices": ProjectDesignTokens.CURATED_FONTS,
        "help": "Applicato a tutti i titoli e agli eyebrow.",
    },
    "body_font": {
        "label": "Font del corpo",
        "type": "select",
        "choices": ProjectDesignTokens.CURATED_FONTS,
        "help": "Applicato ai paragrafi, alle liste e ai form.",
    },
}


# ---------------------------------------------------------------------------
# Per-archetype content schema
# ---------------------------------------------------------------------------

AGENCY_CREATIVE_STUDIO_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".vx-nav, .vx-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "nome studio", "tagline", "disponibilità", "claim"],
        "help": "Logo, tagline e voce del tuo studio.",
        "fields": [
            ("site.logo_word",     {"label": "Nome del logo", "type": "text", "max_length": 32,
                                     "placeholder": "Vertex Studio"}),
            ("site.tag",           {"label": "Tagline", "type": "text", "max_length": 80,
                                     "placeholder": "Independent creative studio · Milano"}),
            ("site.availability",  {"label": "Stato di disponibilità", "type": "text", "max_length": 80,
                                     "help": "Micro-badge che appare vicino al logo."}),
        ],
    },
    {
        "id": "nav",
        "label": "Navigazione",
        "icon": "bi-list",
        "region": ".vx-nav",
        "page": "*",
        "keywords": ["menu", "nav", "cta header", "bottone in alto", "navbar"],
        "help": "Etichetta e destinazione del pulsante in alto a destra.",
        "fields": [
            ("site.nav_cta",       {"label": "Etichetta CTA nav", "type": "text", "max_length": 32}),
            ("site.inquiry_page_slug", {"label": "Pagina di destinazione CTA nav", "type": "select",
                                         "choices": ["home", "studio", "capacita", "lavori", "manifesto", "contatti"]}),
        ],
    },
    {
        "id": "hero",
        "label": "Hero della home",
        "icon": "bi-stars",
        "region": ".vx-hero",
        "page": "home",
        "keywords": ["titolo", "headline", "eyebrow", "primo scroll", "apertura", "pull quote", "claim home"],
        "help": "Il primo scroll della home: eyebrow, headline, intro e CTA.",
        "fields": [
            ("home.eyebrow",      {"label": "Eyebrow",         "type": "text",     "max_length": 120}),
            ("home.headline",     {"label": "Headline",        "type": "richtext", "max_length": 180,
                                   "help": "Consentiti i tag <em> per gli accenti italici."}),
            ("home.pull_quote",   {"label": "Pull-quote",      "type": "textarea", "max_length": 400}),
            ("home.intro",        {"label": "Intro",           "type": "textarea", "max_length": 600}),
            ("home.primary_cta",  {"label": "CTA primaria · etichetta",  "type": "text", "max_length": 40}),
            ("home.primary_href", {"label": "CTA primaria · destinazione", "type": "select",
                                   "choices": ["home", "studio", "capacita", "lavori", "manifesto", "contatti"]}),
            ("home.secondary_cta",  {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 40}),
            ("home.secondary_href", {"label": "CTA secondaria · destinazione", "type": "select",
                                     "choices": ["home", "studio", "capacita", "lavori", "manifesto", "contatti"]}),
        ],
    },
    {
        "id": "cover",
        "label": "Copertina editoriale",
        "icon": "bi-image",
        "region": ".vx-hero .right",
        "page": "home",
        "keywords": ["foto", "immagine", "cover", "copertina", "case study", "cliente home"],
        "help": "Il riquadro visivo che accompagna l'hero: immagine e didascalie.",
        "fields": [
            ("home.cover.image",    {"label": "Immagine", "type": "image", "max_length": 400,
                                      "help": "Incolla l'URL di un'immagine pubblica (HTTPS). Consigliato almeno 1200px di larghezza."}),
            ("home.cover.badge",    {"label": "Badge", "type": "text", "max_length": 40}),
            ("home.cover.client_name", {"label": "Cliente · intestazione", "type": "text", "max_length": 80}),
            ("home.cover.title",    {"label": "Titolo sulla cover", "type": "richtext", "max_length": 200}),
            ("home.cover.discipline", {"label": "Disciplina", "type": "text", "max_length": 60}),
            ("home.cover.year",     {"label": "Anno / periodo", "type": "text", "max_length": 30}),
            ("home.cover.credit_left_label",  {"label": "Credito sinistro · label", "type": "text", "max_length": 30}),
            ("home.cover.credit_left_value",  {"label": "Credito sinistro · valore", "type": "text", "max_length": 60}),
            ("home.cover.credit_right_label", {"label": "Credito destro · label", "type": "text", "max_length": 30}),
            ("home.cover.credit_right_value", {"label": "Credito destro · valore", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "manifesto",
        "label": "Manifesto · home",
        "icon": "bi-quote",
        "region": ".vx-manifesto",
        "page": "home",
        "keywords": ["manifesto home", "citazione", "quote", "valori", "mission"],
        "help": "La sezione manifesto della home: intro, testo principale e cappello.",
        "fields": [
            ("home.manifesto_label",   {"label": "Eyebrow",  "type": "text",     "max_length": 80}),
            ("home.manifesto_heading", {"label": "Heading",  "type": "richtext", "max_length": 200}),
            ("home.manifesto_body",    {"label": "Body",     "type": "textarea", "max_length": 900}),
        ],
    },
    {
        "id": "cta_home",
        "label": "Call to action home",
        "icon": "bi-send",
        "region": ".vx-inquiry",
        "page": "home",
        "keywords": ["cta", "call to action", "invito", "contatto", "chiusura home", "bottone home"],
        "help": "Il blocco finale della home che invita al contatto.",
        "fields": [
            ("home.cta_label",    {"label": "Eyebrow",       "type": "text", "max_length": 60}),
            ("home.cta_heading",  {"label": "Heading",       "type": "richtext", "max_length": 200}),
            ("home.cta_sub",      {"label": "Descrizione",   "type": "textarea", "max_length": 400}),
            ("home.cta_primary",  {"label": "CTA · etichetta", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "ledger",
        "label": "Registro lavori · home",
        "icon": "bi-journal-bookmark",
        "region": ".vx-ledger",
        "page": "home",
        "keywords": ["registro", "portfolio home", "progetti home", "archivio lavori"],
        "help": "Intestazione del registro lavori mostrato in home.",
        "fields": [
            ("home.ledger_heading", {"label": "Heading",  "type": "richtext", "max_length": 120}),
            ("home.ledger_link",    {"label": "Link all'archivio", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "studio",
        "label": "Pagina Studio",
        "icon": "bi-building",
        "region": ".vx-section",
        "page": "studio",
        "keywords": ["chi siamo", "about", "team", "storia", "partner", "bio", "saggio", "cronologia"],
        "help": "About dello studio: voce, racconto e partner.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("studio.eyebrow",    {"label": "Eyebrow",   "type": "text",     "max_length": 100}),
                ("studio.headline",   {"label": "Headline",  "type": "richtext", "max_length": 220}),
                ("studio.standfirst", {"label": "Standfirst", "type": "textarea", "max_length": 600}),
            ]},
            {"label": "Storia · saggio editoriale", "fields": [
                ("studio.essay_label",     {"label": "Eyebrow saggio",   "type": "text",     "max_length": 80}),
                ("studio.essay_heading",   {"label": "Titolo saggio",    "type": "richtext", "max_length": 220}),
                ("studio.essay_pullquote", {"label": "Pull-quote saggio", "type": "textarea", "max_length": 400}),
            ]},
            {"label": "Partner · introduzione", "fields": [
                ("studio.partners_label",   {"label": "Eyebrow partner", "type": "text",     "max_length": 80}),
                ("studio.partners_heading", {"label": "Titolo partner",  "type": "richtext", "max_length": 180}),
                ("studio.partners_intro",   {"label": "Intro partner",   "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Cronologia", "fields": [
                ("studio.timeline_label",   {"label": "Eyebrow cronologia", "type": "text",     "max_length": 60}),
                ("studio.timeline_heading", {"label": "Titolo cronologia",  "type": "richtext", "max_length": 180}),
            ]},
        ],
    },
    {
        "id": "capacita",
        "label": "Pagina Capacità",
        "icon": "bi-gem",
        "region": ".vx-section",
        "page": "capacita",
        "keywords": ["servizi", "services", "capacità", "discipline", "pilastri", "offerta"],
        "help": "Intestazione e pilastri della pagina capacità.",
        "fields": [
            ("capacita.eyebrow",    {"label": "Eyebrow",    "type": "text",     "max_length": 100}),
            ("capacita.headline",   {"label": "Headline",   "type": "richtext", "max_length": 220}),
            ("capacita.standfirst", {"label": "Standfirst", "type": "textarea", "max_length": 600}),
        ],
    },
    {
        "id": "manifesto_page",
        "label": "Pagina Manifesto",
        "icon": "bi-compass",
        "region": ".vx-section",
        "page": "manifesto",
        "keywords": ["processo", "metodo", "fasi", "principi", "come lavoriamo", "process"],
        "help": "Intestazione della pagina manifesto + introduzione delle fasi.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("manifesto.eyebrow",    {"label": "Eyebrow",    "type": "text",     "max_length": 100}),
                ("manifesto.headline",   {"label": "Headline",   "type": "richtext", "max_length": 240}),
                ("manifesto.standfirst", {"label": "Standfirst", "type": "textarea", "max_length": 600}),
            ]},
            {"label": "Principi dello studio", "fields": [
                ("manifesto.principles_label",   {"label": "Eyebrow principi", "type": "text",     "max_length": 80}),
                ("manifesto.principles_heading", {"label": "Titolo principi",  "type": "richtext", "max_length": 200}),
            ]},
            {"label": "Promessa · numeri", "fields": [
                ("manifesto.promise_label",   {"label": "Eyebrow promessa", "type": "text",     "max_length": 60}),
                ("manifesto.promise_heading", {"label": "Titolo promessa",  "type": "richtext", "max_length": 180}),
            ]},
        ],
    },
    {
        "id": "lavori",
        "label": "Pagina Lavori",
        "icon": "bi-images",
        "region": ".vx-section",
        "page": "lavori",
        "keywords": ["progetti", "portfolio", "archivio", "projects", "case study", "lavori"],
        "help": "Intestazione dell'archivio lavori.",
        "fields": [
            ("lavori.eyebrow",    {"label": "Eyebrow",    "type": "text",     "max_length": 100}),
            ("lavori.headline",   {"label": "Headline",   "type": "richtext", "max_length": 220}),
            ("lavori.standfirst", {"label": "Standfirst", "type": "textarea", "max_length": 600}),
        ],
    },
    {
        "id": "contatti",
        "label": "Pagina Contatti",
        "icon": "bi-envelope",
        "region": ".vx-section",
        "page": "contatti",
        "keywords": ["contatti", "contact", "form", "richiedi", "email", "mail", "inquiry", "brief"],
        "help": "Inquiry page: copy del form e voce editoriale.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("contatti.eyebrow",    {"label": "Eyebrow",    "type": "text",     "max_length": 100}),
                ("contatti.headline",   {"label": "Headline",   "type": "richtext", "max_length": 220}),
                ("contatti.standfirst", {"label": "Standfirst", "type": "textarea", "max_length": 600}),
            ]},
            {"label": "Form", "fields": [
                ("contatti.form_heading", {"label": "Titolo form",  "type": "text", "max_length": 120}),
            ]},
        ],
    },
    {
        "id": "contact_info",
        "label": "Contatti · footer",
        "icon": "bi-telephone",
        "region": ".vx-foot",
        "page": "*",
        "keywords": ["telefono", "phone", "email", "mail", "indirizzo", "address", "p.iva", "piva", "orari", "footer contatti"],
        "help": "Dati di contatto che appaiono nel footer.",
        "fields": [
            ("site.phone",       {"label": "Telefono",  "type": "text", "max_length": 40}),
            ("site.email",       {"label": "Email",     "type": "text", "max_length": 80}),
            ("site.address",     {"label": "Indirizzo", "type": "text", "max_length": 120}),
            ("site.hours_compact", {"label": "Orari studio", "type": "text", "max_length": 80}),
            ("site.license",     {"label": "Licenza / P.IVA", "type": "text", "max_length": 120}),
        ],
    },
    {
        "id": "footer_copy",
        "label": "Footer · voce",
        "icon": "bi-card-text",
        "region": ".vx-foot",
        "page": "*",
        "keywords": ["footer", "piede pagina", "colophon", "standfirst footer", "note legali"],
        "help": "Voce editoriale del footer.",
        "fields": [
            ("site.footer_intro",    {"label": "Intro studio", "type": "textarea", "max_length": 500}),
            ("site.foot_standfirst", {"label": "Standfirst",   "type": "textarea", "max_length": 500}),
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
        "Il registro lavori è una lista curata del tuo portfolio — diventerà "
        "editabile nella Phase A.3 (repeater widget).",
    "home.capab_items":
        "Le capacità dello studio hanno una griglia archetipo — personalizzabili "
        "nella Phase A.3.",
    "section_order":
        "L'ordine delle sezioni è parte del DNA dell'archetipo (D-054). "
        "Cambiarlo rientra nella Phase A.3+.",
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


def iter_groups(archetype: str) -> list[dict[str, Any]]:
    """Return the raw group list for an archetype (empty if unsupported).

    Used by the editor view and by tests that need to introspect group
    metadata like ``page`` and ``region``.
    """
    return list(_ARCHETYPE_SCHEMAS.get(archetype) or [])


def iter_editable_fields(archetype: str) -> list[tuple[str, dict[str, Any]]]:
    """Flat list of (key_path, field_spec) tuples for an archetype.

    Groups may expose either a flat ``fields`` list OR a ``subgroups``
    list of ``{label, fields}`` dicts — this helper flattens both
    shapes so downstream validators see a uniform stream of tuples.
    """
    schema = get_schema(archetype)
    if not schema:
        return []
    out: list[tuple[str, dict[str, Any]]] = []
    for group in schema:
        if "subgroups" in group:
            for sub in group["subgroups"]:
                out.extend(sub["fields"])
        else:
            out.extend(group["fields"])
    return out


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
            f"for the current editor phase."
        )


def validate_value(archetype: str, key_path: str, value: Any) -> Any:
    """Lightweight value validation per field spec. Returns the coerced value."""
    spec = get_field_spec(archetype, key_path)
    if spec is None:
        raise InvalidEditableField(key_path)

    # Strip strings and cap length. Image values are exempt from
    # `max_length` — the spec's length cap is for UI hinting, while the
    # real cap for image is a byte-size check below. Truncating a
    # data-URI would silently corrupt it.
    if spec["type"] in {"text", "textarea", "richtext", "url"} and isinstance(value, str):
        value = value.strip()
        max_len = spec.get("max_length")
        if max_len and len(value) > max_len:
            value = value[:max_len]
    elif spec["type"] == "image" and isinstance(value, str):
        value = value.strip()

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

    if spec["type"] == "url":
        # URL type is strict: HTTP(S) only. Empty resets to baseline.
        if value and not (value.startswith("http://") or value.startswith("https://")):
            raise InvalidEditableField(
                f"URL for {key_path!r} must start with http:// or https://."
            )

    if spec["type"] == "image":
        # Image accepts HTTP(S) for CDN paste AND data: URIs so the
        # micro-fix "Carica file" button can work without a separate
        # upload endpoint. Empty resets to baseline.
        if value and not (
            value.startswith("http://")
            or value.startswith("https://")
            or value.startswith("data:image/")
        ):
            raise InvalidEditableField(
                f"Image value for {key_path!r} must be an HTTP(S) URL or a data:image/ URI."
            )
        # Drop huge data URIs outright (keep the overrides table sane).
        if value and value.startswith("data:") and len(value) > 2_000_000:
            raise InvalidEditableField(
                f"Image for {key_path!r} is too large (>2MB). "
                f"Carica un'immagine più leggera o incolla un URL pubblico."
            )

    return value
