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

import re
from typing import Any


# A.3a · structural sentinels + uid pattern.
# `__meta__` is the reserved child-key for a mutable list's structural
# mutations. `UID_RE` matches the `a<digits>` shape used for rows the
# customer added. Baseline rows keep integer indices so the math of
# existing cell-override paths stays untouched.
META_KEY = "__meta__"
UID_RE = re.compile(r"^a\d+$")


def is_uid(segment: str) -> bool:
    """True if ``segment`` is a well-formed added-row uid (``a0``, ``a12``)."""
    return bool(UID_RE.match(segment))

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

# ---------------------------------------------------------------------------
# A.6 · Pragma (corporate-suite archetype) schema
# ---------------------------------------------------------------------------
#
# Second editable archetype. Scope is deliberately tighter than Vertex:
# ~50 scalar fields across 7 sidebar groups + 1 image field (hero) +
# 3 readonly indexed lists (pillars, kpi_strip, leadership). No mutable
# repeaters in this wave — the pattern is proven on Vertex, adding it
# here would only bundle complexity without new learning.
#
# Page slugs follow pragma-corporate-suite registry pages: home (`home`),
# chi-siamo (`about`), competenze (`services`), case-studies
# (`case_study_list`), contatti (`contact`). Indexed row cells stay
# editable cell-by-cell (A.2.6b contract); customers cannot add, remove
# or reorder. Widening mutability on Pragma is A.6b if ever needed.

PRAGMA_CORPORATE_SUITE_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".cs-nav, .cs-foot",
        "page": "*",
        "keywords": ["logo", "nome", "tagline", "marchio", "advisory"],
        "help": "Logo, tagline e voce dello studio.",
        "fields": [
            ("site.logo_word",     {"label": "Nome del logo", "type": "text", "max_length": 32,
                                     "placeholder": "Pragma Advisors"}),
            ("site.logo_initial",  {"label": "Iniziale logo", "type": "text", "max_length": 4,
                                     "help": "Lettera singola usata nel crest del nav."}),
            ("site.tag",           {"label": "Tagline", "type": "text", "max_length": 80,
                                     "placeholder": "Advisory corporate · Milano"}),
        ],
    },
    {
        "id": "hero_board",
        "label": "Hero boardroom (home)",
        "icon": "bi-easel",
        "region": ".cs-hero",
        "page": "home",
        "keywords": ["hero", "apertura", "headline", "eyebrow", "copertina", "board"],
        "help": "Primo scroll della home: eyebrow, headline, intro e CTA.",
        "fields": [
            ("home.eyebrow",        {"label": "Eyebrow",     "type": "text",     "max_length": 120}),
            ("home.headline",       {"label": "Headline",    "type": "richtext", "max_length": 220,
                                      "help": "Consentiti i tag <em> per l'italico."}),
            ("home.intro",          {"label": "Intro",       "type": "textarea", "max_length": 600}),
            ("home.primary_cta",    {"label": "CTA primaria · etichetta", "type": "text", "max_length": 40}),
            ("home.primary_href",   {"label": "CTA primaria · destinazione", "type": "select",
                                     "choices": ["home", "chi-siamo", "competenze", "case-studies", "contatti"]}),
            ("home.secondary_cta",  {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 40}),
            ("home.secondary_href", {"label": "CTA secondaria · destinazione", "type": "select",
                                     "choices": ["home", "chi-siamo", "competenze", "case-studies", "contatti"]}),
            ("home.hero_image",     {"label": "Immagine hero · URL", "type": "image", "max_length": 400,
                                      "help": "Fotografia boardroom che affianca l'hero."}),
        ],
    },
    {
        "id": "home_bands",
        "label": "Sezioni home",
        "icon": "bi-layout-three-columns",
        "region": ".cs-pillars, .cs-kpi-band, .cs-sectors, .cs-leadership, .cs-cases-preview, .cs-cta-band",
        "page": "home",
        "keywords": ["pillars", "kpi", "settori", "sectors", "leadership", "case studies", "cta", "banda"],
        "help": "Titoli e testi introduttivi delle bande della home.",
        "fields": [
            ("home.pillars_label",     {"label": "Pilastri · eyebrow",    "type": "text", "max_length": 60}),
            ("home.pillars_heading",   {"label": "Pilastri · titolo",     "type": "richtext", "max_length": 160}),
            ("home.pillars_intro",     {"label": "Pilastri · intro",      "type": "textarea", "max_length": 400}),
            ("home.kpi_heading",       {"label": "KPI · titolo",          "type": "text", "max_length": 140}),
            ("home.sectors_label",     {"label": "Settori · eyebrow",     "type": "text", "max_length": 60}),
            ("home.trust_label",       {"label": "Clienti · eyebrow",     "type": "text", "max_length": 80}),
            ("home.leadership_label",  {"label": "Leadership · eyebrow",  "type": "text", "max_length": 60}),
            ("home.leadership_heading",{"label": "Leadership · titolo",   "type": "richtext", "max_length": 160}),
            ("home.leadership_intro",  {"label": "Leadership · intro",    "type": "textarea", "max_length": 400}),
            ("home.cases_label",       {"label": "Case studies · eyebrow","type": "text", "max_length": 60}),
            ("home.cases_heading",     {"label": "Case studies · titolo", "type": "richtext", "max_length": 160}),
            ("home.cases_intro",       {"label": "Case studies · intro",  "type": "textarea", "max_length": 400}),
            ("home.cta_label",         {"label": "CTA finale · eyebrow",  "type": "text", "max_length": 60}),
            ("home.cta_heading",       {"label": "CTA finale · titolo",   "type": "richtext", "max_length": 160}),
            ("home.cta_intro",         {"label": "CTA finale · intro",    "type": "textarea", "max_length": 400}),
            ("home.cta_primary",       {"label": "CTA finale · pulsante",      "type": "text", "max_length": 40}),
            ("home.cta_primary_href",  {"label": "CTA finale · destinazione",  "type": "select",
                                         "choices": ["home", "chi-siamo", "competenze", "case-studies", "contatti"]}),
            ("home.cta_secondary",     {"label": "CTA finale · secondaria",    "type": "text", "max_length": 40}),
            ("home.cta_secondary_href",{"label": "CTA finale · sec. destinazione", "type": "select",
                                         "choices": ["home", "chi-siamo", "competenze", "case-studies", "contatti"]}),
        ],
    },
    {
        "id": "about_page",
        "label": "Pagina Chi siamo",
        "icon": "bi-people",
        "region": ".cs-hero, .cs-history, .cs-values, .cs-team, .cs-coords",
        "page": "chi-siamo",
        "keywords": ["chi siamo", "studio", "storia", "valori", "team", "sedi"],
        "help": "Contenuti della pagina Chi siamo.",
        "fields": [
            ("chi-siamo.eyebrow",          {"label": "Eyebrow",   "type": "text",     "max_length": 120}),
            ("chi-siamo.headline",         {"label": "Headline",  "type": "richtext", "max_length": 220}),
            ("chi-siamo.intro",            {"label": "Intro",     "type": "textarea", "max_length": 600}),
            ("chi-siamo.history_label",    {"label": "Storia · eyebrow", "type": "text",     "max_length": 60}),
            ("chi-siamo.history_heading",  {"label": "Storia · titolo",  "type": "richtext", "max_length": 160}),
            ("chi-siamo.history_intro",    {"label": "Storia · intro",   "type": "textarea", "max_length": 400}),
            ("chi-siamo.values_label",     {"label": "Metodo · eyebrow", "type": "text",     "max_length": 60}),
            ("chi-siamo.values_heading",   {"label": "Metodo · titolo",  "type": "richtext", "max_length": 160}),
            ("chi-siamo.values_intro",     {"label": "Metodo · intro",   "type": "textarea", "max_length": 400}),
            ("chi-siamo.team_label",       {"label": "Equipe · eyebrow", "type": "text",     "max_length": 60}),
            ("chi-siamo.team_heading",     {"label": "Equipe · titolo",  "type": "richtext", "max_length": 160}),
            ("chi-siamo.team_intro",       {"label": "Equipe · intro",   "type": "textarea", "max_length": 400}),
        ],
    },
    {
        "id": "services_page",
        "label": "Pagina Competenze",
        "icon": "bi-briefcase",
        "region": ".cs-services, .cs-process, .cs-cta-svc",
        "page": "competenze",
        "keywords": ["competenze", "practice", "servizi", "processo", "metodo"],
        "help": "Contenuti della pagina Competenze.",
        "fields": [
            ("competenze.eyebrow",         {"label": "Eyebrow",   "type": "text",     "max_length": 120}),
            ("competenze.headline",        {"label": "Headline",  "type": "richtext", "max_length": 220}),
            ("competenze.intro",           {"label": "Intro",     "type": "textarea", "max_length": 600}),
            ("competenze.process_label",   {"label": "Processo · eyebrow", "type": "text",     "max_length": 60}),
            ("competenze.process_heading", {"label": "Processo · titolo",  "type": "richtext", "max_length": 160}),
            ("competenze.cta_heading",     {"label": "CTA finale · titolo", "type": "richtext", "max_length": 160}),
            ("competenze.cta_intro",       {"label": "CTA finale · intro",  "type": "textarea", "max_length": 400}),
            ("competenze.cta_primary",     {"label": "CTA finale · pulsante", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "cases_page",
        "label": "Pagina Case studies",
        "icon": "bi-journals",
        "region": ".cs-cases-list, .cs-cta-list",
        "page": "case-studies",
        "keywords": ["case studies", "lavori", "portfolio", "mandati"],
        "help": "Contenuti della pagina Case studies.",
        "fields": [
            ("case-studies.eyebrow",       {"label": "Eyebrow",  "type": "text",     "max_length": 120}),
            ("case-studies.headline",      {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("case-studies.intro",         {"label": "Intro",    "type": "textarea", "max_length": 600}),
            ("case-studies.cases_label",   {"label": "Lista · eyebrow", "type": "text",     "max_length": 60}),
            ("case-studies.cases_intro",   {"label": "Lista · intro",   "type": "textarea", "max_length": 400}),
            ("case-studies.cta_heading",   {"label": "CTA finale · titolo", "type": "richtext", "max_length": 160}),
            ("case-studies.cta_intro",     {"label": "CTA finale · intro",  "type": "textarea", "max_length": 400}),
            ("case-studies.cta_primary",   {"label": "CTA finale · pulsante", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "contact_info",
        "label": "Contatti · footer",
        "icon": "bi-telephone",
        "region": ".cs-foot, .cs-contact-wrap",
        "page": "*",
        "keywords": ["telefono", "phone", "email", "mail", "indirizzo", "address", "orari", "footer"],
        "help": "Dati di contatto usati nel footer e nella pagina contatti.",
        "fields": [
            ("site.phone",         {"label": "Telefono",   "type": "text", "max_length": 40}),
            ("site.email",         {"label": "Email",      "type": "text", "max_length": 80}),
            ("site.address",       {"label": "Indirizzo",  "type": "text", "max_length": 120}),
            ("site.hours_compact", {"label": "Orari studio", "type": "text", "max_length": 80}),
            ("site.license",       {"label": "Licenza / albo", "type": "text", "max_length": 120}),
            ("site.footer_intro",  {"label": "Intro footer", "type": "textarea", "max_length": 600}),
        ],
    },
]


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
        "L'ordine delle sezioni è fissato dal design del template. "
        "Arriverà nelle prossime versioni.",
    "navbar_style":
        "Lo stile della navbar è parte del template scelto. "
        "Per cambiarlo scegli un template diverso.",
    "hero_style":
        "Lo stile dell'hero fa parte del template. "
        "Per un hero diverso scegli un altro template.",
    "pages":
        "Le pagine del sito sono quelle del template. "
        "Aggiungere pagine personalizzate arriverà a breve.",
    "_repeater_intro":
        "Puoi modificare il contenuto di ogni riga delle liste. "
        "Aggiungere o rimuovere righe arriverà a breve.",
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
            # A.3a — first wave repeater. Customer can add/remove rows
            # between these bounds. Other mutable=True lists ship in A.3c.
            "mutable": True,
            "min_rows": 1,
            "max_rows": 8,
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
            # A.3a — first wave repeater. min=2 preserves the "a partnership,
            # not a solo studio" narrative of the agency archetype.
            "mutable": True,
            "min_rows": 2,
            "max_rows": 8,
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
            # A.3c — widen. min=2 preserves the narrative "un prima e
            # un oggi" of the studio history block.
            "mutable": True,
            "min_rows": 2,
            "max_rows": 10,
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
            # A.3c — widen. min=1 allows an email-only studio; max=10
            # keeps the sidebar channels block readable.
            "mutable": True,
            "min_rows": 1,
            "max_rows": 10,
        },
    },
    # A.6 · Pragma corporate-suite — 3 indexed lists exposed as readonly
    # cells (customer edits per-column; add/remove/reorder deferred to
    # A.6b if ever needed). No `mutable: True` flag.
    "corporate-suite": {
        "home.pillars": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Pilastri",
            "icon": "bi-grid-3x3-gap",
            "region": ".cs-pillars",
            "keywords": ["pillars", "practice", "competenze"],
            "tuple_order": ["num", "title", "body"],
            "cols": [
                ("title", {"label": "Titolo", "type": "text",     "max_length": 80}),
                ("body",  {"label": "Body",   "type": "textarea", "max_length": 400}),
            ],
        },
        "home.kpi_strip": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · KPI",
            "icon": "bi-bar-chart",
            "region": ".cs-kpi-band",
            "keywords": ["kpi", "numeri", "stats", "metriche"],
            "tuple_order": ["number", "label"],
            "cols": [
                ("number", {"label": "Numero",    "type": "text", "max_length": 20}),
                ("label",  {"label": "Etichetta", "type": "text", "max_length": 80}),
            ],
        },
        "home.leadership": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Leadership",
            "icon": "bi-people",
            "region": ".cs-leadership",
            "keywords": ["leadership", "partner", "team", "bio"],
            "cols": [
                ("name", {"label": "Nome",      "type": "text",     "max_length": 80}),
                ("role", {"label": "Ruolo",     "type": "text",     "max_length": 120}),
                ("bio",  {"label": "Biografia", "type": "textarea", "max_length": 600}),
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
    "corporate-suite":        ("pragma-corporate-suite", "it"),
}


# ---------------------------------------------------------------------------
# Schema lookup
# ---------------------------------------------------------------------------

_ARCHETYPE_SCHEMAS: dict[str, list[dict[str, Any]]] = {
    "agency-creative-studio": AGENCY_CREATIVE_STUDIO_SCHEMA,
    "corporate-suite":        PRAGMA_CORPORATE_SUITE_SCHEMA,
}


class InvalidEditableField(Exception):
    """Raised when a write targets a key not in the archetype whitelist."""


def get_schema(archetype: str) -> list[dict[str, Any]] | None:
    """Return the editable-field schema for an archetype, or None."""
    return _ARCHETYPE_SCHEMAS.get(archetype)


def is_supported_archetype(archetype: str) -> bool:
    return archetype in _ARCHETYPE_SCHEMAS


def iter_groups(
    archetype: str,
    meta_by_path: dict[str, dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Return the raw group list for an archetype (empty if unsupported).

    When ``meta_by_path`` is supplied, indexed groups reflect the
    **effective** row state of a specific project (baseline minus
    removed rows + added uid rows). When it is None the returned
    groups describe the baseline registry shape — the form required
    by ``iter_editable_fields`` and ``validate_key_path``.
    """
    base = list(_ARCHETYPE_SCHEMAS.get(archetype) or [])
    base.extend(_iter_indexed_groups(archetype, meta_by_path))
    return base


def iter_editable_fields(archetype: str) -> list[tuple[str, dict[str, Any]]]:
    """Flat list of (key_path, field_spec) tuples for an archetype.

    Baseline-only (no project meta). Added-row uid paths are validated
    via ``_validate_uid_cell_path`` in ``validate_key_path``.
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

def _iter_indexed_groups(
    archetype: str,
    meta_by_path: dict[str, dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Build synthetic schema groups for every list in
    ``STRUCTURED_FIELD_SHAPES[archetype]``.

    Baseline mode (``meta_by_path=None``): one subgroup per baseline
    row, keyed on integer index. Used by ``iter_editable_fields``.

    Project mode: each mutable list consults ``meta_by_path[list_path]``
    so the sidebar reflects the effective row state — removed baseline
    rows are hidden and added uid rows appended. Every subgroup carries
    ``row_identity`` so the UI can render the correct remove button.
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
        meta = (meta_by_path or {}).get(list_path)
        out.append(_build_indexed_group(list_path, shape, list_data, meta))
    return out


def _build_indexed_group(
    list_path: str,
    shape: dict[str, Any],
    baseline_rows: list[Any],
    meta: dict[str, Any] | None,
) -> dict[str, Any]:
    kind = shape["kind"]
    group_id = f"idx__{list_path.replace('.', '__')}"
    removed = set(
        (meta.get("removed") or []) if isinstance(meta, dict) else []
    )
    added_entries = (
        (meta.get("added") or []) if isinstance(meta, dict) else []
    )

    # A.3b — honor meta.order when present, else default baseline-then-added.
    added_clean = [
        e for e in added_entries
        if isinstance(e, dict) and isinstance(e.get("uid"), str)
    ]
    default_order = [
        str(i) for i in range(len(baseline_rows)) if i not in removed
    ] + [e["uid"] for e in added_clean]
    raw_order = (meta or {}).get("order") if isinstance(meta, dict) else None
    if isinstance(raw_order, list):
        cleaned = [s for s in raw_order if isinstance(s, str)]
        if set(cleaned) == set(default_order) and len(cleaned) == len(default_order):
            order = cleaned
        else:
            order = default_order
    else:
        order = default_order

    uid_set = {e["uid"] for e in added_clean}
    subgroups: list[dict[str, Any]] = []
    total = len(order)
    for pos, segment in enumerate(order):
        if segment in uid_set:
            fields = _build_row_fields(list_path, shape, segment)
            subgroups.append({
                "label": f"Riga {pos + 1}",
                "fields": fields,
                "row_identity": {
                    "kind": "added",
                    "uid": segment,
                    "segment": segment,
                    "can_move_up": pos > 0,
                    "can_move_down": pos < total - 1,
                },
            })
            continue
        try:
            baseline_idx = int(segment)
        except ValueError:
            continue
        if baseline_idx < 0 or baseline_idx >= len(baseline_rows) or baseline_idx in removed:
            continue
        row = baseline_rows[baseline_idx]
        sub_label = _row_subgroup_label(pos, shape, row)
        fields = _build_row_fields(list_path, shape, str(baseline_idx))
        subgroups.append({
            "label": sub_label,
            "fields": fields,
            "row_identity": {
                "kind": "baseline",
                "baseline_idx": baseline_idx,
                "segment": str(baseline_idx),
                "can_move_up": pos > 0,
                "can_move_down": pos < total - 1,
            },
        })

    mutable = bool(shape.get("mutable"))
    min_rows = shape.get("min_rows", 1)
    max_rows = shape.get("max_rows", len(baseline_rows))
    help_text = (
        f"Modifica il contenuto di ognuna delle {len(subgroups)} righe. "
        f"Aggiungere o rimuovere righe arriverà a breve."
    )
    if mutable:
        help_text = (
            f"Modifica il contenuto di ognuna delle {len(subgroups)} righe. "
            f"Puoi aggiungere o rimuovere righe (minimo {min_rows}, massimo {max_rows})."
        )

    return {
        "id": group_id,
        "label": shape["label"],
        "icon": shape.get("icon", "bi-list-ol"),
        "region": shape.get("region", ".vx-section"),
        "page": shape["page"],
        "keywords": list(shape.get("keywords") or []) + ["lista", "righe"],
        "help": help_text,
        "subgroups": subgroups,
        # A.3a — expose mutability metadata for the sidebar UI.
        "mutable": mutable,
        "min_rows": min_rows,
        "max_rows": max_rows,
        "list_path": list_path,
        "effective_length": len(subgroups),
    }


def _build_row_fields(
    list_path: str, shape: dict[str, Any], segment: str,
) -> list[tuple[str, dict[str, Any]]]:
    """Build (key_path, spec) pairs for one row — baseline idx or uid."""
    kind = shape["kind"]
    if kind == "scalar":
        return [(f"{list_path}.{segment}", dict(shape["cell_spec"]))]
    return [
        (f"{list_path}.{segment}.{col}", dict(spec))
        for col, spec in (shape.get("cols") or [])
    ]


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
    """Look up the widget spec for a key_path (None if not editable).

    A.3a: also resolves uid cell paths (``studio.partners.a0.name``) by
    matching the list's ``cols`` spec — the spec is identical between a
    baseline row and an added row, only the path prefix differs.
    """
    for path, spec in iter_editable_fields(archetype):
        if path == key_path:
            return spec
    # A.3a — uid cell fallback
    parts = key_path.split(".")
    for cut in range(len(parts) - 1, 0, -1):
        list_path = ".".join(parts[:cut])
        shape = get_list_shape(archetype, list_path)
        if not shape or not shape.get("mutable"):
            continue
        remaining = parts[cut:]
        if not remaining or not is_uid(remaining[0]):
            return None
        kind = shape.get("kind")
        if kind == "scalar" and len(remaining) == 1:
            return dict(shape["cell_spec"])
        if kind in ("tuple", "dict") and len(remaining) == 2:
            col = remaining[1]
            for name, spec in (shape.get("cols") or []):
                if name == col:
                    return dict(spec)
    return None


def get_list_shape(archetype: str, list_path: str) -> dict[str, Any] | None:
    """Return the STRUCTURED_FIELD_SHAPES entry for a list, or None."""
    return (STRUCTURED_FIELD_SHAPES.get(archetype) or {}).get(list_path)


def is_mutable_list(archetype: str, list_path: str) -> bool:
    """A.3a — True iff the list is opted-in to row add/remove."""
    shape = get_list_shape(archetype, list_path)
    return bool(shape and shape.get("mutable"))


def _validate_uid_cell_path(archetype: str, key_path: str) -> bool:
    """A.3a — accept ``<mutable_list>.a<N>.<col>`` for dict/tuple lists and
    ``<mutable_list>.a<N>`` for scalar lists. Returns True if the path is a
    well-formed cell override against a mutable list's added row. The
    service layer is responsible for verifying that the uid actually
    exists in the project's meta; validator stays stateless.
    """
    parts = key_path.split(".")
    if len(parts) < 2:
        return False
    # Walk longest-prefix-first so nested lists (none today, guarded for
    # future phases) prefer the deepest mutable match.
    for cut in range(len(parts) - 1, 0, -1):
        list_path = ".".join(parts[:cut])
        shape = get_list_shape(archetype, list_path)
        if not shape or not shape.get("mutable"):
            continue
        remaining = parts[cut:]
        if not remaining or not is_uid(remaining[0]):
            return False
        kind = shape.get("kind")
        if kind == "scalar":
            return len(remaining) == 1
        # tuple / dict
        if len(remaining) != 2:
            return False
        col = remaining[1]
        col_names = [name for name, _spec in (shape.get("cols") or [])]
        return col in col_names
    return False


def validate_key_path(archetype: str, key_path: str) -> None:
    """Raise ``InvalidEditableField`` if the path is not writable.

    A.3a extends A.2.6b by accepting ``<mutable_list>.a<N>.<col>`` shapes
    for cell overrides on added rows. The structural ``__meta__`` sentinel
    is NOT accepted here — it is written exclusively through
    ``services.add_row`` / ``services.remove_row`` so customer autosave
    can never corrupt a list's structural state.
    """
    if get_field_spec(archetype, key_path) is not None:
        return
    if _validate_uid_cell_path(archetype, key_path):
        return
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
        # Accept HTTP(S) for CDN paste, data: URIs (A.2.2 inline
        # fallback, still tolerated), and relative /media/... URLs
        # produced by the A.4 upload endpoint. Anything else (raw
        # file paths, javascript:, etc.) is rejected.
        if value and not (
            value.startswith("http://")
            or value.startswith("https://")
            or value.startswith("data:image/")
            or value.startswith("/media/")
        ):
            raise InvalidEditableField(
                f"Image value for {key_path!r} must be an HTTP(S) URL, a "
                f"data:image/ URI, or a /media/ upload URL."
            )
        # Drop huge data URIs outright (keep the overrides table sane).
        if value and value.startswith("data:") and len(value) > 2_000_000:
            raise InvalidEditableField(
                f"Image for {key_path!r} is too large (>2MB). "
                f"Carica un'immagine più leggera o incolla un URL pubblico."
            )

    return value


# ---------------------------------------------------------------------------
# A.7 · Multi-locale contract (Step 0 — metadata only, no behaviour change)
# ---------------------------------------------------------------------------
#
# Fields flagged translatable are persisted per-locale in the A.7 overlay
# shape ({"globals": {...}, "by_locale": {"it": {...}, ...}}). Fields that
# are not translatable live under "globals" and apply to every locale.
#
# Rules for this first wave (Vertex only):
#   • Only scalar text types (text · textarea · richtext) can be translatable.
#   • Paths in ``_GLOBAL_TEXT_PATHS`` stay global even if text-typed
#     (branding identity + contact universals that don't change per language).
#   • Any path belonging to a structured repeater list (baseline-indexed
#     row cells AND added-row uid cells) stays global — repeater structure
#     + row content are frozen out of A.7.
#   • Archetypes that haven't opted in via ``_MULTILOCALE_ENABLED_ARCHETYPES``
#     return False for every path (e.g. Pragma in A.7, to become A.7b).

_TRANSLATABLE_TEXT_TYPES: frozenset[str] = frozenset({"text", "textarea", "richtext"})

_GLOBAL_TEXT_PATHS: frozenset[str] = frozenset({
    "site.logo_word",
    "site.logo_initial",
    "site.phone",
    "site.email",
    "site.address",
    "site.license",
})

_MULTILOCALE_ENABLED_ARCHETYPES: frozenset[str] = frozenset({
    "agency-creative-studio",
    # A.7b · Pragma joins the multi-locale gate. Enrollment is a pure
    # set-extension per D-098: no schema shape change, no service layer
    # touch. Gated by the dedicated lifecycle regression test
    # ``test_a7b_pragma_full_multilocale_lifecycle_end_to_end`` so a
    # future one-liner flip on a new archetype cannot ship without
    # matching coverage.
    "corporate-suite",
})


def _is_under_structured_list(archetype: str, key_path: str) -> bool:
    """True iff the path addresses a cell (baseline-index or uid) inside
    a STRUCTURED_FIELD_SHAPES list for this archetype."""
    shapes = STRUCTURED_FIELD_SHAPES.get(archetype) or {}
    for list_path in shapes:
        if key_path == list_path or key_path.startswith(list_path + "."):
            return True
    return False


def is_translatable(archetype: str, key_path: str) -> bool:
    """Return True iff an override for this key_path is persisted per-locale.

    A.7 Step 0 contract: read-only classification. The service + autosave
    layers consult this helper in Step 1/2 to route overrides into
    ``by_locale[locale]`` vs ``globals``.
    """
    if archetype not in _MULTILOCALE_ENABLED_ARCHETYPES:
        return False
    spec = get_field_spec(archetype, key_path)
    if spec is None:
        return False
    if spec.get("type") not in _TRANSLATABLE_TEXT_TYPES:
        return False
    if key_path in _GLOBAL_TEXT_PATHS:
        return False
    if _is_under_structured_list(archetype, key_path):
        return False
    return True


def supported_locales(archetype: str) -> list[str]:
    """Locales a project of this archetype can have per-locale overrides for.

    Step 0 returns an empty list for non-enabled archetypes and the
    canonical 5 for multi-locale-enabled ones. Step 2 will wire this
    into ``editor_ctx`` so the sidebar pill strip can render it.
    """
    if archetype not in _MULTILOCALE_ENABLED_ARCHETYPES:
        return []
    return ["it", "en", "fr", "es", "ar"]


# A.7 Step 1 · storage-key encoding for per-locale overrides. Translatable
# rows in ProjectContent carry a ``@<locale>:`` prefix so the existing flat
# (project, key_path) uniqueness still applies and the shape is readable
# straight from the DB. Plain rows (no prefix) stay global — legacy
# projects keep rendering cross-locale exactly as before.

_LOCALE_KEY_RE = re.compile(r"^@([a-z]{2}):(.+)$")


def encode_locale_key(locale: str, key_path: str) -> str:
    """Build the storage-layer key_path for a per-locale override."""
    return f"@{locale}:{key_path}"


def decode_locale_key(key: str) -> tuple[str | None, str]:
    """Return ``(locale, path)`` for a per-locale key, or ``(None, key)``.

    Plain rows — the legacy shape — decode to a None locale so callers
    can treat them as globals with no branching.
    """
    m = _LOCALE_KEY_RE.match(key)
    if not m:
        return None, key
    return m.group(1), m.group(2)
