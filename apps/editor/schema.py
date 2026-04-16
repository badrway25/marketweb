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
        "keywords": ["contatti", "contact", "form", "richiedi", "email", "mail", "inquiry", "brief",
                     "label", "etichetta", "placeholder", "canali", "telefono", "risposta", "promessa"],
        "help": "Inquiry page: form, canali diretti e promessa di risposta.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("contatti.eyebrow",    {"label": "Eyebrow",    "type": "text",     "max_length": 100}),
                ("contatti.headline",   {"label": "Headline",   "type": "richtext", "max_length": 220}),
                ("contatti.standfirst", {"label": "Standfirst", "type": "textarea", "max_length": 600}),
            ]},
            {"label": "Form · titolo e invio", "fields": [
                ("contatti.form_heading",      {"label": "Titolo form",        "type": "text",     "max_length": 120}),
                ("contatti.form_submit_label", {"label": "Etichetta pulsante invio",
                                                 "type": "text",     "max_length": 40}),
                ("contatti.form_submit_note",  {"label": "Nota sotto il pulsante",
                                                 "type": "textarea", "max_length": 240}),
            ]},
            {"label": "Form · etichette campi", "fields": [
                ("contatti.labels.name",       {"label": "Etichetta · nome",        "type": "text", "max_length": 60}),
                ("contatti.labels.role",       {"label": "Etichetta · ruolo",       "type": "text", "max_length": 60}),
                ("contatti.labels.company",    {"label": "Etichetta · organizzazione", "type": "text", "max_length": 60}),
                ("contatti.labels.email",      {"label": "Etichetta · email",       "type": "text", "max_length": 60}),
                ("contatti.labels.discipline", {"label": "Etichetta · disciplina",  "type": "text", "max_length": 80}),
                ("contatti.labels.budget",     {"label": "Etichetta · budget",      "type": "text", "max_length": 60}),
                ("contatti.labels.brief",      {"label": "Etichetta · brief",       "type": "text", "max_length": 60}),
            ]},
            {"label": "Form · placeholder", "fields": [
                ("contatti.placeholders.name",    {"label": "Placeholder · nome",      "type": "text", "max_length": 80}),
                ("contatti.placeholders.role",    {"label": "Placeholder · ruolo",     "type": "text", "max_length": 100}),
                ("contatti.placeholders.company", {"label": "Placeholder · organizzazione",
                                                    "type": "text", "max_length": 100}),
                ("contatti.placeholders.email",   {"label": "Placeholder · email",     "type": "text", "max_length": 80}),
                ("contatti.placeholders.brief",   {"label": "Placeholder · brief",     "type": "textarea", "max_length": 400}),
            ]},
            {"label": "Email diretta", "fields": [
                ("contatti.direct_label",   {"label": "Eyebrow",  "type": "text",     "max_length": 60}),
                ("contatti.direct_heading", {"label": "Heading",  "type": "richtext", "max_length": 220}),
                ("contatti.studio_label",   {"label": "Etichetta · lo studio",
                                              "type": "text",     "max_length": 40}),
            ]},
            {"label": "Tempi di risposta", "fields": [
                ("contatti.reply_label",   {"label": "Eyebrow", "type": "text",     "max_length": 60}),
                ("contatti.reply_heading", {"label": "Heading", "type": "richtext", "max_length": 220}),
                ("contatti.reply_body",    {"label": "Body",    "type": "textarea", "max_length": 600}),
            ]},
            {"label": "Canali · intestazione", "fields": [
                ("contatti.channels_label", {"label": "Eyebrow canali", "type": "text", "max_length": 40}),
            ]},
            {"label": "Promessa", "fields": [
                ("contatti.promise_label",   {"label": "Eyebrow",  "type": "text",     "max_length": 60}),
                ("contatti.promise_heading", {"label": "Heading",  "type": "richtext", "max_length": 400}),
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
#
# A.2.6b updates: list-level overwrites stay locked (you cannot replace
# the whole list to add or remove rows), but individual cells of every
# list in STRUCTURED_FIELD_SHAPES are now editable as scalar fields.
LOCKED_KEYS_NOTE: dict[str, str] = {
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
    "_repeater_intro":
        "Le liste hanno un numero di righe fissato dall'archetipo: puoi "
        "modificare il contenuto di ogni cella, ma non aggiungere o rimuovere "
        "righe (Phase A.3 — repeater widget).",
}


# ---------------------------------------------------------------------------
# A.2.6b · Indexed-row contract — STRUCTURED_FIELD_SHAPES
# ---------------------------------------------------------------------------
#
# The content registry stores several editorial lists as either tuples,
# dicts or plain strings. A.2.6b exposes the cells of those lists as
# indexed scalar fields: ``studio.facts.0.label`` walks to row 0 of
# ``studio.facts`` and updates only the ``label`` cell, leaving the
# rest of the tuple intact and the other rows untouched.
#
# Shape declaration::
#
#   {
#       "kind":      "tuple" | "dict" | "scalar",
#       "page":      "<page slug for navigation/highlight>",
#       "label":     "<sidebar accordion label>",
#       "icon":      "<bootstrap icon>",
#       "region":    "<CSS selector to highlight>",
#       "keywords":  [<extra search tokens>],
#       # Tuple-specific:
#       "tuple_order": [<full list of column names, in tuple position>],
#       # Tuple/dict-specific (the exposed subset, in editor display order):
#       "cols":      [(col_name, field_spec), ...],
#       # Scalar-specific (one value per cell):
#       "cell_spec": {<field spec for every row>},
#   }
#
# For tuple lists, ``tuple_order`` lists ALL columns including the locked
# ones (None). The splicer at apply time uses it to convert the cell name
# (e.g. "title") into the tuple index. ``cols`` lists only the editable
# subset — locked columns (slugs, ordinals) never appear in the schema or
# the editor sidebar.
#
# For dict lists (each item is a ``{"name": ..., "role": ...}`` dict),
# ``cols`` lists the dict-keys to expose, in editor display order. The
# splicer just sets ``item[col]`` directly; no order translation needed.
#
# For scalar lists (plain ``["Monocle", "Domus", ...]``), there is no
# column dimension — each row IS the value. ``cell_spec`` is the field
# spec applied to every row.

STRUCTURED_FIELD_SHAPES: dict[str, dict[str, dict[str, Any]]] = {
    "agency-creative-studio": {

        # ── HOME ────────────────────────────────────────────────────────
        "home.ledger_rows": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Registro lavori",
            "icon": "bi-journal-text",
            "region": ".vx-ledger",
            "keywords": ["registro", "ledger", "portfolio home", "progetti home"],
            "tuple_order": ["index", "title", "client", "discipline", "year", "slug"],
            "cols": [
                ("title",  {"label": "Titolo",  "type": "text", "max_length": 100}),
                ("client", {"label": "Cliente", "type": "text", "max_length": 80}),
            ],
        },
        "home.capab_items": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Capacità (riepilogo)",
            "icon": "bi-grid-3x3-gap",
            "region": ".vx-capab",
            "keywords": ["capacità", "discipline", "home capacità", "pilastri"],
            "tuple_order": ["num", "title", "body", "bullets"],
            "cols": [
                ("title", {"label": "Titolo", "type": "text",     "max_length": 80}),
                ("body",  {"label": "Body",   "type": "textarea", "max_length": 300}),
            ],
        },
        "home.press_publications": {
            "kind": "scalar",
            "page": "home",
            "label": "Home · Pubblicazioni",
            "icon": "bi-megaphone",
            "region": ".vx-press",
            "keywords": ["press", "stampa", "pubblicazioni", "marquee"],
            "cell_spec": {"label": "Voce", "type": "text", "max_length": 60},
        },
        "home.manifesto_principles": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Manifesto · principi",
            "icon": "bi-list-check",
            "region": ".vx-manifesto",
            "keywords": ["manifesto", "principi", "valori"],
            "tuple_order": ["num", "title", "body"],
            "cols": [
                ("title", {"label": "Titolo", "type": "richtext", "max_length": 120}),
                ("body",  {"label": "Body",   "type": "textarea", "max_length": 300}),
            ],
        },

        # ── STUDIO ──────────────────────────────────────────────────────
        "studio.facts": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Fatti chiave",
            "icon": "bi-123",
            "region": ".vx-section",
            "keywords": ["numeri", "fatti", "facts", "metriche", "kpi", "anni"],
            "tuple_order": ["number", "label", "sub"],
            "cols": [
                ("number", {"label": "Numero",      "type": "text", "max_length": 12}),
                ("label",  {"label": "Etichetta",   "type": "text", "max_length": 80}),
                ("sub",    {"label": "Sotto-testo", "type": "text", "max_length": 140}),
            ],
        },
        "studio.partners": {
            "kind": "dict",
            "page": "studio",
            "label": "Studio · Partner",
            "icon": "bi-people",
            "region": ".vx-section",
            "keywords": ["partner", "team", "soci", "fondatori", "bio"],
            "cols": [
                ("name",     {"label": "Nome",          "type": "text",     "max_length": 80}),
                ("role",     {"label": "Ruolo",         "type": "text",     "max_length": 120}),
                ("bio",      {"label": "Biografia",     "type": "textarea", "max_length": 600}),
                ("portrait", {"label": "Ritratto · URL","type": "image",    "max_length": 400}),
            ],
        },
        "studio.timeline_rows": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Cronologia",
            "icon": "bi-clock-history",
            "region": ".vx-section",
            "keywords": ["cronologia", "timeline", "anni", "tappe"],
            "tuple_order": ["year", "title", "body"],
            "cols": [
                ("year",  {"label": "Anno",  "type": "text",     "max_length": 12}),
                ("title", {"label": "Titolo","type": "text",     "max_length": 120}),
                ("body",  {"label": "Body",  "type": "textarea", "max_length": 400}),
            ],
        },

        # ── CAPACITA ────────────────────────────────────────────────────
        "capacita.disciplines": {
            "kind": "dict",
            "page": "capacita",
            "label": "Capacità · Discipline",
            "icon": "bi-gem",
            "region": ".vx-section",
            "keywords": ["discipline", "servizi", "capacità", "pilastri"],
            "cols": [
                ("title",   {"label": "Titolo",   "type": "richtext", "max_length": 100}),
                ("tagline", {"label": "Tagline",  "type": "text",     "max_length": 140}),
                ("body",    {"label": "Body",     "type": "textarea", "max_length": 700}),
            ],
        },
        "capacita.engagement_tiles": {
            "kind": "dict",
            "page": "capacita",
            "label": "Capacità · Modi di lavorare",
            "icon": "bi-handshake",
            "region": ".vx-section",
            "keywords": ["engagement", "ingaggio", "modalità", "incarichi"],
            "cols": [
                ("title", {"label": "Titolo",   "type": "richtext", "max_length": 100}),
                ("range", {"label": "Tempistica","type": "text",    "max_length": 100}),
                ("body",  {"label": "Body",     "type": "textarea", "max_length": 400}),
            ],
        },

        # ── LAVORI ──────────────────────────────────────────────────────
        "lavori.filters": {
            "kind": "scalar",
            "page": "lavori",
            "label": "Lavori · Filtri",
            "icon": "bi-funnel",
            "region": ".vx-section",
            "keywords": ["filtri", "filters", "categorie", "tag"],
            "cell_spec": {"label": "Voce", "type": "text", "max_length": 40},
        },
        "lavori.projects": {
            "kind": "dict",
            "page": "lavori",
            "label": "Lavori · Progetti",
            "icon": "bi-briefcase",
            "region": ".vx-section",
            "keywords": ["progetti", "portfolio", "lavori", "case study"],
            "cols": [
                ("title",      {"label": "Titolo",     "type": "text", "max_length": 120}),
                ("client",     {"label": "Cliente",    "type": "text", "max_length": 100}),
                ("year",       {"label": "Anno",       "type": "text", "max_length": 16}),
            ],
        },
        "lavori.archive_stats": {
            "kind": "tuple",
            "page": "lavori",
            "label": "Lavori · Statistiche archivio",
            "icon": "bi-bar-chart",
            "region": ".vx-section",
            "keywords": ["statistiche", "archivio", "numeri lavori"],
            "tuple_order": ["number", "label"],
            "cols": [
                ("number", {"label": "Numero",    "type": "richtext", "max_length": 24}),
                ("label",  {"label": "Etichetta", "type": "text",     "max_length": 80}),
            ],
        },

        # ── MANIFESTO ───────────────────────────────────────────────────
        "manifesto.phases": {
            "kind": "dict",
            "page": "manifesto",
            "label": "Manifesto · Fasi del processo",
            "icon": "bi-diagram-3",
            "region": ".vx-section",
            "keywords": ["fasi", "processo", "metodo", "phases"],
            "cols": [
                ("duration", {"label": "Durata",  "type": "text",     "max_length": 60}),
                ("title",    {"label": "Titolo",  "type": "richtext", "max_length": 120}),
                ("tagline",  {"label": "Tagline", "type": "text",     "max_length": 120}),
                ("body",     {"label": "Body",    "type": "textarea", "max_length": 700}),
            ],
        },
        "manifesto.principles": {
            "kind": "tuple",
            "page": "manifesto",
            "label": "Manifesto · Principi di studio",
            "icon": "bi-list-check",
            "region": ".vx-section",
            "keywords": ["principi", "valori", "regole", "manifesto"],
            "tuple_order": ["num", "title", "body"],
            "cols": [
                ("title", {"label": "Titolo", "type": "richtext", "max_length": 120}),
                ("body",  {"label": "Body",   "type": "textarea", "max_length": 400}),
            ],
        },
        "manifesto.promise_stats": {
            "kind": "tuple",
            "page": "manifesto",
            "label": "Manifesto · Promessa numerica",
            "icon": "bi-trophy",
            "region": ".vx-section",
            "keywords": ["promessa", "numeri", "statistiche", "stats"],
            "tuple_order": ["number", "label", "sub"],
            "cols": [
                ("number", {"label": "Numero",      "type": "richtext", "max_length": 30}),
                ("label",  {"label": "Etichetta",   "type": "text",     "max_length": 80}),
                ("sub",    {"label": "Sotto-testo", "type": "textarea", "max_length": 240}),
            ],
        },

        # ── CONTATTI ────────────────────────────────────────────────────
        "contatti.discipline_options": {
            "kind": "scalar",
            "page": "contatti",
            "label": "Contatti · Opzioni disciplina (form)",
            "icon": "bi-list-ul",
            "region": ".vx-section",
            "keywords": ["discipline", "form", "select", "opzioni form", "scelta"],
            "cell_spec": {"label": "Voce", "type": "text", "max_length": 80},
        },
        "contatti.budget_bands": {
            "kind": "tuple",
            "page": "contatti",
            "label": "Contatti · Bande budget (form)",
            "icon": "bi-cash-stack",
            "region": ".vx-section",
            "keywords": ["budget", "bande", "fasce", "prezzo", "form"],
            "tuple_order": ["slug", "label"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 60}),
            ],
        },
        "contatti.channels": {
            "kind": "tuple",
            "page": "contatti",
            "label": "Contatti · Canali diretti",
            "icon": "bi-broadcast",
            "region": ".vx-section",
            "keywords": ["canali", "channels", "telefono", "email", "linkedin", "studio"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 40}),
                ("value", {"label": "Valore",    "type": "text", "max_length": 100}),
            ],
        },
    },
}


# Map archetype → (template_slug, default_locale) so that the indexed
# field generator can find the baseline list lengths. Foundation v1
# only has one template per archetype so a flat dict is enough; once
# multiple templates share an archetype this becomes a query.
_ARCHETYPE_BASELINE_TEMPLATE: dict[str, tuple[str, str]] = {
    "agency-creative-studio": ("vertex-creative-agency", "it"),
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
    metadata like ``page`` and ``region``. A.2.6b: synthetic groups for
    the indexed-row contract are appended after the curated scalar
    groups so the editor sidebar shows them in the canonical order
    (chrome → home → page-by-page → contact_info / footer → indexed).
    """
    base = list(_ARCHETYPE_SCHEMAS.get(archetype) or [])
    base.extend(_iter_indexed_groups(archetype))
    return base


def iter_editable_fields(archetype: str) -> list[tuple[str, dict[str, Any]]]:
    """Flat list of (key_path, field_spec) tuples for an archetype.

    Groups may expose either a flat ``fields`` list OR a ``subgroups``
    list of ``{label, fields}`` dicts — this helper flattens both
    shapes so downstream validators see a uniform stream of tuples.
    A.2.6b: indexed-row paths (``studio.facts.0.label`` etc.) flow in
    via ``_iter_indexed_groups`` and are exposed identically.
    """
    out: list[tuple[str, dict[str, Any]]] = []
    for group in iter_groups(archetype):
        if "subgroups" in group:
            for sub in group["subgroups"]:
                out.extend(sub["fields"])
        else:
            out.extend(group["fields"])
    return out


# ---------------------------------------------------------------------------
# A.2.6b · Indexed group generator
# ---------------------------------------------------------------------------

def _iter_indexed_groups(archetype: str) -> list[dict[str, Any]]:
    """Build synthetic schema groups for every list in
    ``STRUCTURED_FIELD_SHAPES[archetype]``.

    Row counts come from the baseline content registry — we never
    invent rows the template doesn't already author. Each list becomes
    one accordion with one subgroup per row (``Riga 1`` … ``Riga N``)
    and one field per editable column. The subgroup label leans on the
    customer's own first column where it reads well (``"Riga 1 · 8"``
    for ``studio.facts``); everywhere else it stays a clean ``Riga N``.
    """
    shapes = STRUCTURED_FIELD_SHAPES.get(archetype) or {}
    if not shapes:
        return []

    baseline = _baseline_content_for(archetype)
    if not baseline:
        return []

    out: list[dict[str, Any]] = []
    for list_path, shape in shapes.items():
        list_data = _resolve_path(baseline, list_path)
        if not isinstance(list_data, list) or not list_data:
            continue
        rows = len(list_data)
        out.append(_build_indexed_group(list_path, shape, list_data, rows))
    return out


def _build_indexed_group(
    list_path: str,
    shape: dict[str, Any],
    list_data: list[Any],
    rows: int,
) -> dict[str, Any]:
    kind = shape["kind"]
    group_id = f"idx__{list_path.replace('.', '__')}"
    subgroups: list[dict[str, Any]] = []
    for i in range(rows):
        sub_label = _row_subgroup_label(i, shape, list_data[i])
        fields: list[tuple[str, dict[str, Any]]] = []
        if kind == "scalar":
            fields.append((f"{list_path}.{i}", dict(shape["cell_spec"])))
        else:  # tuple or dict
            for col_name, col_spec in shape["cols"]:
                fields.append((f"{list_path}.{i}.{col_name}", dict(col_spec)))
        subgroups.append({"label": sub_label, "fields": fields})
    return {
        "id": group_id,
        "label": shape["label"],
        "icon": shape.get("icon", "bi-list-ol"),
        "region": shape.get("region", ".vx-section"),
        "page": shape["page"],
        "keywords": list(shape.get("keywords") or []) + ["lista", "righe"],
        "help": (
            f"Modifica le {rows} righe di questa lista. Per aggiungere o "
            f"rimuovere righe attendi la Phase A.3 (repeater widget)."
        ),
        "subgroups": subgroups,
    }


def _row_subgroup_label(idx: int, shape: dict[str, Any], row_data: Any) -> str:
    """Friendly per-row label (``Riga 1 · Margherita Serafini`` etc.).

    Falls back to a clean ``Riga N`` when no concise hint is available.
    """
    base = f"Riga {idx + 1}"
    hint: str | None = None
    kind = shape["kind"]
    if kind == "dict" and isinstance(row_data, dict):
        for candidate in ("name", "title", "label"):
            value = row_data.get(candidate)
            if isinstance(value, str) and value.strip():
                hint = value
                break
    elif kind == "tuple" and isinstance(row_data, (list, tuple)):
        order = shape.get("tuple_order") or []
        for candidate in ("title", "label", "year", "number"):
            if candidate in order:
                pos = order.index(candidate)
                if pos < len(row_data):
                    value = row_data[pos]
                    if isinstance(value, str) and value.strip():
                        hint = value
                        break
    elif kind == "scalar" and isinstance(row_data, str) and row_data.strip():
        hint = row_data
    if hint:
        # Strip rich-text tags so the subgroup label stays clean.
        clean = hint.replace("<em>", "").replace("</em>", "")
        clean = clean.strip()
        if len(clean) > 38:
            clean = clean[:36].rstrip() + "…"
        return f"{base} · {clean}"
    return base


def _baseline_content_for(archetype: str) -> dict[str, Any] | None:
    """Lazy helper — fetches the IT baseline registry for an archetype.

    Lazy import prevents a startup-time circular dep against
    ``apps.catalog`` (which transitively wants the editor schema for
    its admin forms).
    """
    pair = _ARCHETYPE_BASELINE_TEMPLATE.get(archetype)
    if pair is None:
        return None
    template_slug, locale = pair
    try:
        from apps.catalog import template_content  # local import — see docstring
    except Exception:
        return None
    return template_content.get_content(template_slug, locale) or None


def _resolve_path(tree: Any, dotted: str) -> Any:
    cursor: Any = tree
    for segment in dotted.split("."):
        if not isinstance(cursor, dict):
            return None
        cursor = cursor.get(segment)
        if cursor is None:
            return None
    return cursor


def get_structured_shapes(archetype: str) -> dict[str, dict[str, Any]]:
    """Public accessor used by the rendering splicer."""
    return STRUCTURED_FIELD_SHAPES.get(archetype) or {}


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
