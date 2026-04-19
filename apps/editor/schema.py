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


# ---------------------------------------------------------------------------
# A.8 · Gusto (fine-dining archetype) schema
# ---------------------------------------------------------------------------
#
# Third editable archetype. Recipe mirrors A.6 Pragma: ~10 sidebar groups of
# scalar fields + 3 STRUCTURED_FIELD_SHAPES readonly lists (signature_courses,
# menu.courses, produttori.items). No mutable repeaters, no per-locale image,
# no detail-page editor — those remain out of scope per A.8 planning.
#
# Page slugs follow the Italian fine-dining registry (home / filosofia / menu /
# atmosfera / diario / prenota). All 5 locales use the same slugs per D-023
# (every locale ships a `pages` list with identical slugs + kinds, only the
# labels translate).
#
# Image fields exposed customer-side: home.ingredienti.image +
# filosofia.filosofia_image. The 4 portrait URLs inside home.produttori.items
# stay readonly at the registry level — their column is intentionally omitted
# from the dict shape's ``cols`` so the editor cannot reach them.
#
# prenota.form_sections is intentionally NOT in the schema: the content
# registry has it in IT but not in EN/FR/ES/AR (the skin has a
# ``{% if page_data.form_sections %}`` guard). Keeping it out of the
# editable whitelist sidesteps the parity asymmetry without a registry
# patch — pure A.8 scope containment.

GUSTO_FINE_DINING_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".fd-nav, .fd-foot",
        "page": "*",
        "keywords": ["logo", "nome", "ristorante", "tagline", "insegna"],
        "help": "Nome del ristorante, iniziale logo e tagline.",
        "fields": [
            ("site.logo_word",    {"label": "Nome ristorante", "type": "text", "max_length": 40,
                                    "placeholder": "Osteria Moderna"}),
            ("site.logo_initial", {"label": "Iniziale / crest", "type": "text", "max_length": 4,
                                    "help": "Iniziale usata nel crest del nav."}),
            ("site.tag",          {"label": "Tagline", "type": "text", "max_length": 100}),
            ("site.star_line",    {"label": "Riga stella / est.", "type": "text", "max_length": 80,
                                    "help": "\"★ Una stella Michelin · est. 2018\" — appare nel chrome."}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".fd-lead",
        "page": "home",
        "keywords": ["hero", "apertura", "headline", "eyebrow", "copertina", "manifesto"],
        "help": "Primo scroll della home: eyebrow, headline, intro, CTA e manifesto.",
        "fields": [
            ("home.eyebrow",             {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("home.headline",            {"label": "Headline", "type": "richtext", "max_length": 220,
                                           "help": "Consentiti i tag <em> per gli italici."}),
            ("home.intro",               {"label": "Intro", "type": "textarea", "max_length": 400}),
            ("home.primary_cta",         {"label": "CTA primaria · etichetta", "type": "text", "max_length": 40}),
            ("home.primary_href",        {"label": "CTA primaria · destinazione", "type": "select",
                                           "choices": ["home", "filosofia", "menu", "atmosfera", "diario", "prenota"]}),
            ("home.secondary_cta",       {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 40}),
            ("home.secondary_href",      {"label": "CTA secondaria · destinazione", "type": "select",
                                           "choices": ["home", "filosofia", "menu", "atmosfera", "diario", "prenota"]}),
            ("home.chef_label",          {"label": "Etichetta chef · card", "type": "text", "max_length": 40}),
            ("home.star_tag",            {"label": "Tag atto · card chef", "type": "text", "max_length": 80}),
            ("home.photo_label",         {"label": "Etichetta foto · card", "type": "text", "max_length": 40}),
            ("home.cuisine_label",       {"label": "Etichetta cucina · card", "type": "text", "max_length": 40}),
            ("home.manifesto_drop_cap",  {"label": "Drop cap manifesto", "type": "text", "max_length": 2}),
            ("home.manifesto",           {"label": "Manifesto home", "type": "textarea", "max_length": 700}),
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".fd-section, .fd-cta-band",
        "page": "home",
        "keywords": ["atti", "press", "pubblicato", "cta", "chef link"],
        "help": "Label ed eyebrow delle fasce home (atti, press, CTA finali).",
        "fields": [
            ("home.courses_label",        {"label": "Atti · eyebrow", "type": "text", "max_length": 80}),
            ("home.courses_footline",     {"label": "Atti · nota prezzi", "type": "text", "max_length": 140}),
            ("home.courses_full_cta",     {"label": "Atti · CTA \"tutti\"", "type": "text", "max_length": 40}),
            ("home.press_label",          {"label": "Pubblicato su · eyebrow", "type": "text", "max_length": 40}),
            ("home.chef_link_filosofia",  {"label": "Link chef · filosofia", "type": "text", "max_length": 40}),
            ("home.chef_link_diario",     {"label": "Link chef · diario", "type": "text", "max_length": 40}),
            ("home.cta_heading",          {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("home.cta_primary",          {"label": "CTA finale · pulsante", "type": "text", "max_length": 40}),
            ("home.cta_secondary",        {"label": "CTA finale · secondario", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "home_editorial_bands",
        "label": "Home · chef, ingredienti, stagione",
        "icon": "bi-person-badge",
        "region": ".fd-ingredients, .fd-chef, .fd-season",
        "page": "home",
        "keywords": ["chef", "ingredienti", "materia prima", "sourcing", "stagione", "menu in corso"],
        "help": "Card chef · banda ingredienti · card stagionale.",
        "fields": [
            ("home.chef.name",                 {"label": "Chef · nome", "type": "text", "max_length": 80}),
            ("home.chef.role",                 {"label": "Chef · ruolo", "type": "text", "max_length": 120}),
            ("home.chef.bio",                  {"label": "Chef · bio", "type": "textarea", "max_length": 600}),
            ("home.ingredienti.label",         {"label": "Ingredienti · eyebrow", "type": "text", "max_length": 80}),
            ("home.ingredienti.heading",       {"label": "Ingredienti · titolo", "type": "richtext", "max_length": 220}),
            ("home.ingredienti.text",          {"label": "Ingredienti · testo", "type": "textarea", "max_length": 500}),
            ("home.ingredienti.image",         {"label": "Ingredienti · immagine", "type": "image", "max_length": 400}),
            ("home.ingredienti.image_caption", {"label": "Ingredienti · caption", "type": "text", "max_length": 140}),
            ("home.stagione.label",            {"label": "Stagione · eyebrow", "type": "text", "max_length": 80}),
            ("home.stagione.title",            {"label": "Stagione · titolo", "type": "text", "max_length": 120}),
            ("home.stagione.subtitle",         {"label": "Stagione · sottotitolo", "type": "text", "max_length": 120}),
            ("home.stagione.text",             {"label": "Stagione · testo", "type": "textarea", "max_length": 400}),
            ("home.stagione.cta_label",        {"label": "Stagione · CTA", "type": "text", "max_length": 60}),
            ("home.stagione.cta_href",         {"label": "Stagione · destinazione", "type": "select",
                                                 "choices": ["home", "filosofia", "menu", "atmosfera", "diario", "prenota"]}),
        ],
    },
    {
        "id": "home_producers_events_wine",
        "label": "Home · produttori, eventi, cantina",
        "icon": "bi-award",
        "region": ".fd-producers, .fd-private, .fd-wine",
        "page": "home",
        "keywords": ["produttori", "artigiani", "fornitori", "eventi privati", "chef's table",
                     "vino", "cantina", "sommelier"],
        "help": "Copy di apertura delle fasce produttori / eventi / cantina. Le card readonly "
                "restano dal registry.",
        "fields": [
            ("home.produttori.label",            {"label": "Produttori · eyebrow", "type": "text", "max_length": 80}),
            ("home.produttori.heading",          {"label": "Produttori · titolo", "type": "richtext", "max_length": 220}),
            ("home.produttori.intro",            {"label": "Produttori · intro", "type": "textarea", "max_length": 500}),
            ("home.private_dining.label",        {"label": "Eventi · eyebrow", "type": "text", "max_length": 80}),
            ("home.private_dining.heading",      {"label": "Eventi · titolo", "type": "richtext", "max_length": 220}),
            ("home.private_dining.intro",        {"label": "Eventi · intro", "type": "textarea", "max_length": 500}),
            ("home.private_dining.cta_label",    {"label": "Eventi · CTA", "type": "text", "max_length": 60}),
            ("home.private_dining.cta_href",     {"label": "Eventi · destinazione", "type": "select",
                                                   "choices": ["home", "filosofia", "menu", "atmosfera", "diario", "prenota"]}),
            ("home.wine_program.label",          {"label": "Cantina · eyebrow", "type": "text", "max_length": 80}),
            ("home.wine_program.heading",        {"label": "Cantina · titolo", "type": "richtext", "max_length": 220}),
            ("home.wine_program.intro",          {"label": "Cantina · intro", "type": "textarea", "max_length": 500}),
            ("home.wine_program.sommelier.name", {"label": "Sommelier · nome", "type": "text", "max_length": 80}),
            ("home.wine_program.sommelier.role", {"label": "Sommelier · ruolo", "type": "text", "max_length": 120}),
            ("home.wine_program.sommelier.bio",  {"label": "Sommelier · bio", "type": "textarea", "max_length": 500}),
        ],
    },
    {
        "id": "filosofia_page",
        "label": "Pagina Filosofia",
        "icon": "bi-book",
        "region": ".fd-section",
        "page": "filosofia",
        "keywords": ["filosofia", "about", "metodo", "valori", "storia"],
        "help": "Contenuti della pagina Filosofia.",
        "fields": [
            ("filosofia.eyebrow",                 {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("filosofia.headline",                {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("filosofia.intro",                   {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("filosofia.filosofia_image",         {"label": "Immagine filosofia", "type": "image", "max_length": 400}),
            ("filosofia.filosofia_image_caption", {"label": "Caption immagine", "type": "text", "max_length": 160}),
            ("filosofia.method_title",            {"label": "Metodo · titolo", "type": "text", "max_length": 80}),
            ("filosofia.values_label",            {"label": "Valori · eyebrow", "type": "text", "max_length": 80}),
            ("filosofia.values_heading",          {"label": "Valori · titolo", "type": "richtext", "max_length": 220}),
            ("filosofia.cta_heading",             {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("filosofia.cta_menu",                {"label": "CTA · pulsante menu", "type": "text", "max_length": 60}),
            ("filosofia.cta_prenota",             {"label": "CTA · pulsante prenota", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "menu_page",
        "label": "Pagina Menu",
        "icon": "bi-journal-text",
        "region": ".fd-section, .fd-menu-list",
        "page": "menu",
        "keywords": ["menu", "atti", "corsi", "piatti", "vini", "carta"],
        "help": "Contenuti della pagina Menu (otto atti + copy carta vini).",
        "fields": [
            ("menu.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("menu.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("menu.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("menu.courses_label",    {"label": "Atti · eyebrow", "type": "text", "max_length": 100}),
            ("menu.wine_intro_title", {"label": "Vini · titolo", "type": "text", "max_length": 80}),
            ("menu.wine_intro",       {"label": "Vini · intro", "type": "textarea", "max_length": 500}),
            ("menu.footer",           {"label": "Footer note · prezzi / intolleranze", "type": "textarea", "max_length": 600}),
        ],
    },
    {
        "id": "atmosfera_page",
        "label": "Pagina Atmosfera",
        "icon": "bi-images",
        "region": ".fd-section",
        "page": "atmosfera",
        "keywords": ["atmosfera", "sala", "ambienti", "gallery"],
        "help": "Contenuti della pagina Atmosfera (ambienti / CTA). Le card sala restano da registry.",
        "fields": [
            ("atmosfera.eyebrow",        {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("atmosfera.headline",       {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("atmosfera.intro",          {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("atmosfera.cta_quote",      {"label": "Quote finale", "type": "textarea", "max_length": 240}),
            ("atmosfera.cta_desc",       {"label": "Descrizione CTA", "type": "textarea", "max_length": 240}),
            ("atmosfera.cta_primary",    {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
            ("atmosfera.cta_secondary",  {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "diario_page",
        "label": "Pagina Diario (index)",
        "icon": "bi-newspaper",
        "region": ".fd-section",
        "page": "diario",
        "keywords": ["diario", "blog", "journal", "note", "articoli"],
        "help": "Copy della pagina-indice del diario di sala. I singoli post restano da registry.",
        "fields": [
            ("diario.eyebrow",  {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("diario.headline", {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("diario.intro",    {"label": "Intro", "type": "textarea", "max_length": 600}),
        ],
    },
    {
        "id": "prenota_page",
        "label": "Pagina Prenota",
        "icon": "bi-calendar-check",
        "region": ".fd-section",
        "page": "prenota",
        "keywords": ["prenotazione", "prenota", "concierge", "form"],
        "help": "Copy della pagina di prenotazione + card concierge. "
                "Struttura del form + opzioni select restano da registry.",
        "fields": [
            ("prenota.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("prenota.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("prenota.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("prenota.process_label",    {"label": "Processo · eyebrow", "type": "text", "max_length": 80}),
            ("prenota.process_heading",  {"label": "Processo · titolo", "type": "richtext", "max_length": 220}),
            ("prenota.hours_label",      {"label": "Orari · eyebrow", "type": "text", "max_length": 80}),
            ("prenota.hours_heading",    {"label": "Orari · titolo", "type": "richtext", "max_length": 220}),
            ("prenota.private_heading",  {"label": "Privati · titolo", "type": "richtext", "max_length": 220}),
            ("prenota.private_title",    {"label": "Privati · sub-header", "type": "text", "max_length": 120}),
            ("prenota.private_intro",    {"label": "Privati · intro", "type": "textarea", "max_length": 500}),
            ("prenota.form_title",       {"label": "Form · titolo", "type": "text", "max_length": 80}),
            ("prenota.form_submit",      {"label": "Form · CTA invio", "type": "text", "max_length": 60}),
            ("prenota.form_submit_note", {"label": "Form · nota sotto invio", "type": "textarea", "max_length": 240}),
            ("prenota.concierge.name",   {"label": "Concierge · nome", "type": "text", "max_length": 80}),
            ("prenota.concierge.role",   {"label": "Concierge · ruolo", "type": "text", "max_length": 120}),
            ("prenota.concierge.email",  {"label": "Concierge · email", "type": "text", "max_length": 120}),
            ("prenota.concierge.phone",  {"label": "Concierge · telefono", "type": "text", "max_length": 40}),
            ("prenota.concierge.bio",    {"label": "Concierge · bio", "type": "textarea", "max_length": 500}),
        ],
    },
    {
        "id": "contact_info",
        "label": "Contatti · footer",
        "icon": "bi-telephone",
        "region": ".fd-foot",
        "page": "*",
        "keywords": ["footer", "contatti", "phone", "telefono", "email", "indirizzo", "address",
                     "orari", "copyright"],
        "help": "Dati di contatto visibili nel footer e nella pagina Prenota.",
        "fields": [
            ("site.phone",          {"label": "Telefono", "type": "text", "max_length": 40}),
            ("site.email",          {"label": "Email", "type": "text", "max_length": 80}),
            ("site.address",        {"label": "Indirizzo", "type": "text", "max_length": 120}),
            ("site.hours_compact",  {"label": "Orari sintetici", "type": "text", "max_length": 80}),
            ("site.footer_intro",   {"label": "Intro footer", "type": "textarea", "max_length": 400}),
            ("site.footer_hours_1", {"label": "Footer · riga orari attivi", "type": "text", "max_length": 60}),
            ("site.footer_hours_2", {"label": "Footer · riga orari chiusura", "type": "text", "max_length": 60}),
            ("site.copyright",      {"label": "Copyright", "type": "text", "max_length": 160}),
        ],
    },
]


# ---------------------------------------------------------------------------
# A.9 · Medical-specialist schema (Cardio + Derm · archetype `specialist`)
# ---------------------------------------------------------------------------
#
# Fourth editable archetype. First multi-template archetype: one schema
# unlocks two templates (``cardio-studio-specialistico`` +
# ``dermatologia-elite-roma``) because both carry ``archetype: 'specialist'``
# in their DNA and share 95% of the content-tree shape (100% on studio /
# visite / medici / pubblicazioni / contatti / richiedi-visita / site · 85%
# on home — 29 shared keys · 5 Cardio-only · 5 Derm-only).
#
# The 10 divergent home premium sections (D-064 Session 30 split) are
# intentionally NOT exposed here: ``home.anchor_nav``, ``home.insurance``,
# ``home.location``, ``home.percorso``, ``home.tecnologie`` on Cardio; and
# ``home.before_after``, ``home.credentials``, ``home.editorial_feed``,
# ``home.gallery_strip``, ``home.trattamenti_tabs`` on Derm. Their authored
# values keep rendering unchanged; customers simply can't edit them in A.9.
# Dedicated regression test ``test_a9_specialist_divergent_premium_sections_excluded``
# locks this boundary so a later coverage pass can't accidentally reopen it.
#
# Form-structure blocks that are IT-only in the registry
# (``contatti.form_consent``, ``contatti.form_helpers``,
# ``richiedi-visita.form_sections``, ``richiedi-visita.upload_field``) stay
# out of the whitelist — same exclusion strategy Gusto A.8 used for
# ``prenota.form_sections``.
#
# Image fields exposed customer-side (all global per D-098): the 5 scalar
# images on home.chief.portrait, studio.studio_image, visite.service_image,
# pubblicazioni.lead_image, plus the 3 doctor portraits inside
# ``medici.doctors[*].portrait`` — the latter omitted from the dict shape
# ``cols`` so they stay registry-only (same pattern as Gusto
# produttori.items portrait).

MEDICAL_SPECIALIST_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".sp-nav, .sp-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "studio", "tagline", "medico", "specialista"],
        "help": "Nome dello studio, iniziale del crest e tagline.",
        "fields": [
            ("site.logo_word",    {"label": "Nome studio", "type": "text", "max_length": 60,
                                    "placeholder": "Studio Marani"}),
            ("site.logo_initial", {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.tag",          {"label": "Tagline", "type": "text", "max_length": 100}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".sp-hero",
        "page": "home",
        "keywords": ["hero", "apertura", "headline", "eyebrow", "intro", "cta", "direzione clinica"],
        "help": "Primo scroll della home: eyebrow, headline, intro, CTA principali, drop-cap + manifesto.",
        "fields": [
            ("home.eyebrow",           {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("home.headline",          {"label": "Headline", "type": "richtext", "max_length": 220,
                                         "help": "Consentiti i tag <em> per gli italici."}),
            ("home.intro",             {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("home.primary_cta",       {"label": "CTA primaria · etichetta", "type": "text", "max_length": 40}),
            ("home.primary_href",      {"label": "CTA primaria · destinazione", "type": "select",
                                         "choices": ["home", "studio", "visite", "medici",
                                                     "pubblicazioni", "contatti", "richiedi-visita"]}),
            ("home.secondary_cta",     {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 40}),
            ("home.secondary_href",    {"label": "CTA secondaria · destinazione", "type": "select",
                                         "choices": ["home", "studio", "visite", "medici",
                                                     "pubblicazioni", "contatti", "richiedi-visita"]}),
            ("home.manifesto_drop_cap", {"label": "Drop cap manifesto", "type": "text", "max_length": 2}),
            ("home.manifesto",         {"label": "Manifesto home", "type": "textarea", "max_length": 700}),
            ("home.press_label",       {"label": "Pubblicato su · eyebrow", "type": "text", "max_length": 40}),
            ("home.hero_sidebar_top_label", {"label": "Sidebar hero · eyebrow", "type": "text", "max_length": 60}),
            ("home.hero_sidebar_quote", {"label": "Sidebar hero · citazione", "type": "textarea", "max_length": 400}),
            ("home.hero_sidebar_author", {"label": "Sidebar hero · fonte", "type": "text", "max_length": 120}),
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".sp-section",
        "page": "home",
        "keywords": ["visite", "signature", "chief", "direzione", "cta", "testimonianza", "faq"],
        "help": "Label, eyebrow e intro delle fasce shared (signature visits, direzione clinica, CTA finale, testimonianza, FAQ).",
        "fields": [
            ("home.signature_visits_label",   {"label": "Signature visits · eyebrow", "type": "text", "max_length": 80}),
            ("home.signature_visits_heading", {"label": "Signature visits · titolo", "type": "richtext", "max_length": 220}),
            ("home.signature_visits_intro",   {"label": "Signature visits · intro", "type": "textarea", "max_length": 500}),
            ("home.chief_label",              {"label": "Direzione clinica · eyebrow", "type": "text", "max_length": 80}),
            ("home.chief_heading",            {"label": "Direzione clinica · titolo", "type": "richtext", "max_length": 220}),
            ("home.testimonianza.quote",      {"label": "Testimonianza · citazione", "type": "textarea", "max_length": 400}),
            ("home.testimonianza.author",     {"label": "Testimonianza · autore", "type": "text", "max_length": 120}),
            ("home.testimonianza.context",    {"label": "Testimonianza · contesto", "type": "text", "max_length": 160}),
            ("home.faq.label",                {"label": "FAQ · eyebrow", "type": "text", "max_length": 80}),
            ("home.faq.heading",              {"label": "FAQ · titolo", "type": "richtext", "max_length": 220}),
            ("home.cta_heading",              {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("home.cta_primary_label",        {"label": "CTA finale · primario", "type": "text", "max_length": 40}),
            ("home.cta_secondary_label",      {"label": "CTA finale · secondario", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "home_chief",
        "label": "Home · direzione clinica",
        "icon": "bi-person-badge",
        "region": ".sp-chief",
        "page": "home",
        "keywords": ["direzione", "chief", "medico", "titolare", "portrait"],
        "help": "Card direttore clinico (nome / ruolo / bio / portrait).",
        "fields": [
            ("home.chief.name",     {"label": "Direzione · nome", "type": "text", "max_length": 80}),
            ("home.chief.role",     {"label": "Direzione · ruolo", "type": "text", "max_length": 120}),
            ("home.chief.bio",      {"label": "Direzione · bio", "type": "textarea", "max_length": 600}),
            ("home.chief.portrait", {"label": "Direzione · ritratto (URL)", "type": "image", "max_length": 400}),
        ],
    },
    {
        "id": "studio_page",
        "label": "Pagina Studio",
        "icon": "bi-building",
        "region": ".sp-section",
        "page": "studio",
        "keywords": ["studio", "about", "storia", "metodo", "valori", "impegni"],
        "help": "Pagina Chi siamo: storia, metodo, valori, CTA finale.",
        "fields": [
            ("studio.eyebrow",              {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("studio.headline",             {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("studio.intro",                {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("studio.studio_image",         {"label": "Immagine studio", "type": "image", "max_length": 400}),
            ("studio.studio_image_caption", {"label": "Caption immagine", "type": "text", "max_length": 160}),
            ("studio.method_title",         {"label": "Metodo · titolo", "type": "text", "max_length": 80}),
            ("studio.values_label",         {"label": "Valori · eyebrow", "type": "text", "max_length": 80}),
            ("studio.values_heading",       {"label": "Valori · titolo", "type": "richtext", "max_length": 220}),
            ("studio.cta_heading",          {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("studio.cta_primary_label",    {"label": "CTA · pulsante primario", "type": "text", "max_length": 60}),
            ("studio.cta_secondary_label",  {"label": "CTA · pulsante secondario", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "visite_page",
        "label": "Pagina Visite",
        "icon": "bi-clipboard2-pulse",
        "region": ".sp-section",
        "page": "visite",
        "keywords": ["visite", "servizi", "trattamenti", "percorsi", "clinica"],
        "help": "Pagina Visite / servizi (lista trattamenti readonly).",
        "fields": [
            ("visite.eyebrow",               {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("visite.headline",              {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("visite.intro",                 {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("visite.service_image",         {"label": "Immagine servizio", "type": "image", "max_length": 400}),
            ("visite.service_image_caption", {"label": "Caption immagine", "type": "text", "max_length": 160}),
            ("visite.footnote",              {"label": "Nota piè pagina", "type": "textarea", "max_length": 400}),
            ("visite.footnote_heading",      {"label": "Nota · titolo breve", "type": "text", "max_length": 80}),
            ("visite.cta_heading",           {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("visite.cta_primary_label",     {"label": "CTA · pulsante primario", "type": "text", "max_length": 60}),
            ("visite.cta_secondary_label",   {"label": "CTA · pulsante secondario", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "medici_page",
        "label": "Pagina Medici",
        "icon": "bi-people",
        "region": ".sp-section",
        "page": "medici",
        "keywords": ["medici", "team", "dottori", "equipe"],
        "help": "Pagina team: intro + lista medici readonly.",
        "fields": [
            ("medici.eyebrow",       {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("medici.headline",      {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("medici.intro",         {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("medici.portrait_city", {"label": "Etichetta città ritratti", "type": "text", "max_length": 80}),
        ],
    },
    {
        "id": "pubblicazioni_page",
        "label": "Pagina Pubblicazioni",
        "icon": "bi-journal-text",
        "region": ".sp-section",
        "page": "pubblicazioni",
        "keywords": ["pubblicazioni", "articoli", "press", "blog", "journal"],
        "help": "Pagina-indice pubblicazioni. I singoli post restano da registry.",
        "fields": [
            ("pubblicazioni.eyebrow",     {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("pubblicazioni.headline",    {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("pubblicazioni.intro",       {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("pubblicazioni.lead_image",  {"label": "Immagine di testata", "type": "image", "max_length": 400}),
            ("pubblicazioni.footer_strap", {"label": "Strap footer", "type": "text", "max_length": 120}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-telephone",
        "region": ".sp-section",
        "page": "contatti",
        "keywords": ["contatti", "contact", "form", "orari", "trasporti"],
        "help": "Pagina contatti: copy, form title + intro. Struttura form / placeholder select / consenso restano da registry.",
        "fields": [
            ("contatti.eyebrow",            {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("contatti.headline",           {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("contatti.intro",              {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("contatti.form_title",         {"label": "Form · titolo", "type": "text", "max_length": 80}),
            ("contatti.form_intro",         {"label": "Form · intro", "type": "textarea", "max_length": 300}),
            ("contatti.hours_heading",      {"label": "Orari · titolo", "type": "text", "max_length": 80}),
            ("contatti.transport_heading",  {"label": "Trasporti · titolo", "type": "text", "max_length": 80}),
            ("contatti.form_submit_note",   {"label": "Form · nota submit", "type": "textarea", "max_length": 240}),
        ],
    },
    {
        "id": "appointment_page",
        "label": "Pagina Richiedi visita",
        "icon": "bi-calendar-check",
        "region": ".sp-section",
        "page": "richiedi-visita",
        "keywords": ["appointment", "prenota", "richiedi", "visita", "form"],
        "help": "Pagina Richiedi visita: copy + card processo. Struttura form + upload field restano da registry.",
        "fields": [
            ("richiedi-visita.eyebrow",                 {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("richiedi-visita.headline",                {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("richiedi-visita.intro",                   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("richiedi-visita.process_label",           {"label": "Processo · eyebrow", "type": "text", "max_length": 80}),
            ("richiedi-visita.process_heading",         {"label": "Processo · titolo", "type": "richtext", "max_length": 220}),
            ("richiedi-visita.form_title",              {"label": "Form · titolo", "type": "text", "max_length": 80}),
            ("richiedi-visita.form_band_side_note",     {"label": "Form · nota laterale", "type": "textarea", "max_length": 240}),
            ("richiedi-visita.form_band_side_note_small", {"label": "Form · micro nota", "type": "text", "max_length": 60}),
            ("richiedi-visita.submit_label",            {"label": "Form · CTA submit", "type": "text", "max_length": 60}),
            ("richiedi-visita.form_submit_note",        {"label": "Form · nota sotto submit", "type": "textarea", "max_length": 240}),
            ("richiedi-visita.consent",                 {"label": "Privacy · testo consenso", "type": "textarea", "max_length": 400}),
            ("richiedi-visita.footnote",                {"label": "Footnote piè pagina", "type": "textarea", "max_length": 400}),
        ],
    },
    {
        "id": "contact_info",
        "label": "Contatti · footer",
        "icon": "bi-telephone-forward",
        "region": ".sp-foot",
        "page": "*",
        "keywords": ["footer", "phone", "telefono", "email", "indirizzo", "orari", "licenza"],
        "help": "Dati di contatto + strip licenza + intro footer.",
        "fields": [
            ("site.phone",         {"label": "Telefono", "type": "text", "max_length": 40}),
            ("site.email",         {"label": "Email", "type": "text", "max_length": 80}),
            ("site.address",       {"label": "Indirizzo", "type": "text", "max_length": 120}),
            ("site.hours_compact", {"label": "Orari sintetici", "type": "text", "max_length": 80}),
            ("site.license",       {"label": "Licenza / albo", "type": "text", "max_length": 120}),
            ("site.footer_intro",  {"label": "Intro footer", "type": "textarea", "max_length": 400}),
        ],
    },
]


# ---------------------------------------------------------------------------
# A.10 · Lex (classic-gold archetype · law family) schema
# ---------------------------------------------------------------------------
#
# Fifth editable archetype. Single-template archetype (lex-studio-legale only).
# Juris (modern-transparent) is a separate archetype and will be enrolled as
# A.10b in its own phase — the A.9 shared-schema recipe does NOT apply here
# because the two law templates carry distinct DNA + distinct skin folders +
# distinct page slug sets. See A.10 Planning Session for the audit evidence.
#
# Shape notes from Step 0 audit:
#   • 5-locale parity: PERFECT across every section (pages · top-level keys ·
#     every section's key-set identical cross-locale). Zero IT-only gaps on
#     contatti.form_fields / form_sections / upload_field (cleaner than Gusto
#     and specialist).
#   • Single scalar image field: notabili.lead_image (blog index hero). No
#     portrait fields anywhere — Lex lawyers + partners dicts do NOT carry
#     portrait URLs in the registry, so the portrait-excluded pattern used in
#     Gusto produttori.items and specialist medici.doctors is not needed here.
#   • RTL CSS block already mature in `classic-gold/_base.html` (lines 331+).
#     Skin uses `.lx-*` selectors (NOT `.cg-*`).
#   • Form structure blocks (contatti.form_fields · form_sections ·
#     upload_field) stay OUT of the whitelist — same policy as Gusto /
#     specialist. Their authored values keep rendering unchanged.
#   • pratiche.services[*].scope is a `list[str]` inside the dict (bullet
#     points). Omitted from the dict shape `cols` so the registry value keeps
#     rendering — only scalar cols exposed.

# A.11 · Juris modern-transparent — 5th enrolled editor archetype, second
# template in the lawyer category (Lex classic-gold was the first, in A.10).
# Single-template admission: the two law templates ship distinct archetypes
# + distinct skin folders + only ~25% content-tree overlap, so the A.9
# shared-schema recipe does NOT apply. Juris ships ZERO image fields — the
# advisory-modern DNA explicitly rejects founder portraits / case photos,
# so no image widget ever reaches the editor perimeter here.
#
# Shape contract notes (see Step 0 audit in the A.11 phase memory):
#   • 11 sidebar groups cover all 6 Juris pages (home, approccio, servizi,
#     settori, insights, contatti) + chrome (brand, nav, contact_info).
#     Skin uses `.jr-*` selectors.
#   • Complex shapes explicitly KEPT OUT of the perimeter by design:
#       - ``approccio.dashboard_mock`` (nested dict with columns → cards)
#       - ``home.trust_logos`` (flat list-of-str marquee wordmarks)
#       - ``insights.topics`` (flat list-of-str filter pills)
#       - ``servizi.services[*].deliverables`` (nested list-of-str bullets)
#       - ``settori.sectors[*].pain_points / signals / legal_ops``
#         (nested list-of-str bullets) — same policy as Lex
#         ``pratiche.services[*].scope``.
#     These stay registry-only; the customer cannot reach them through
#     the editor. The test suite asserts this explicitly.
#   • Form structure blocks (contatti.form_fields · form_sections) stay
#     OUT of the whitelist — same policy as Gusto / specialist / Lex.
#   • blog_list (insights) surfaces only the page-level copy; per-post
#     content (``posts[*].title`` / sections) stays registry-only.

JURIS_MODERN_TRANSPARENT_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".jr-nav, .jr-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "studio", "tagline", "wordmark", "crest"],
        "help": "Nome studio, iniziale crest e tagline advisory.",
        "fields": [
            ("site.logo_word",    {"label": "Nome studio", "type": "text", "max_length": 60,
                                    "placeholder": "Martini & Partners"}),
            ("site.logo_initial", {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.tag",          {"label": "Tagline", "type": "text", "max_length": 100}),
            ("site.nav_cta",      {"label": "CTA nav", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".jr-lead",
        "page": "home",
        "keywords": ["hero", "apertura", "headline", "eyebrow", "intro", "cta", "sprint", "slot"],
        "help": "Primo scroll della home: eyebrow, headline, intro, CTA principali e chip prossimo slot.",
        "fields": [
            ("home.eyebrow",         {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("home.headline",        {"label": "Headline", "type": "richtext", "max_length": 220,
                                       "help": "Consentiti i tag <em> per gli italici."}),
            ("home.intro",           {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("home.primary_cta",     {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
            ("home.primary_href",    {"label": "CTA primaria · destinazione", "type": "select",
                                       "choices": ["home", "approccio", "servizi", "settori",
                                                   "insights", "contatti"]}),
            ("home.secondary_cta",   {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
            ("home.secondary_href",  {"label": "CTA secondaria · destinazione", "type": "select",
                                       "choices": ["home", "approccio", "servizi", "settori",
                                                   "insights", "contatti"]}),
            ("home.sprint_chip",     {"label": "Chip · testo", "type": "text", "max_length": 120}),
            ("home.sprint_chip_cta", {"label": "Chip · etichetta CTA", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".jr-section",
        "page": "home",
        "keywords": ["sectors", "settori", "process", "metric", "insights", "trust", "cta"],
        "help": "Label, eyebrow e intro delle fasce home (settori, processo, metriche, trust, insights, CTA finale).",
        "subgroups": [
            {"label": "Settori · intestazione", "fields": [
                ("home.sectors_label",     {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.sectors_heading",   {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.sectors_intro",     {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Processo · intestazione", "fields": [
                ("home.process_label",     {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.process_heading",   {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.process_intro",     {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Metriche · intestazione", "fields": [
                ("home.metric_label",      {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.metric_heading",    {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Trust band", "fields": [
                ("home.trust_label",       {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ]},
            {"label": "Insights · intestazione", "fields": [
                ("home.insights_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.insights_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.insights_intro",    {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.insights_link",     {"label": "Link · etichetta", "type": "text", "max_length": 60}),
                ("home.insights_link_href",{"label": "Link · destinazione", "type": "select",
                                             "choices": ["home", "approccio", "servizi", "settori",
                                                         "insights", "contatti"]}),
            ]},
            {"label": "CTA finale", "fields": [
                ("home.cta_label",         {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.cta_heading",       {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.cta_intro",         {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.cta_primary",       {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.cta_primary_href",  {"label": "CTA primaria · destinazione", "type": "select",
                                             "choices": ["home", "approccio", "servizi", "settori",
                                                         "insights", "contatti"]}),
                ("home.cta_secondary",     {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
                ("home.cta_secondary_href",{"label": "CTA secondaria · destinazione", "type": "select",
                                             "choices": ["home", "approccio", "servizi", "settori",
                                                         "insights", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "approccio_page",
        "label": "Pagina Approccio",
        "icon": "bi-compass",
        "region": ".jr-section",
        "page": "approccio",
        "keywords": ["approccio", "about", "manifesto", "story", "dashboard", "sedi", "fondatori"],
        "help": "Pagina Approccio: manifesto, storia, dashboard advisory, fondatori, sedi.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("approccio.eyebrow",            {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("approccio.headline",           {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("approccio.intro",              {"label": "Intro", "type": "textarea", "max_length": 700}),
            ]},
            {"label": "Manifesto · intestazione", "fields": [
                ("approccio.manifesto_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("approccio.manifesto_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("approccio.manifesto_intro",    {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Storia · intestazione", "fields": [
                ("approccio.story_label",        {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("approccio.story_heading",      {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Dashboard · intestazione", "fields": [
                ("approccio.dashboard_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("approccio.dashboard_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("approccio.dashboard_intro",    {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Fondatori · intestazione", "fields": [
                ("approccio.founders_label",     {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("approccio.founders_heading",   {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Sedi · intestazione", "fields": [
                ("approccio.offices_label",      {"label": "Eyebrow", "type": "text", "max_length": 80}),
            ]},
            {"label": "CTA finale", "fields": [
                ("approccio.cta_heading",        {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("approccio.cta_intro",          {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("approccio.cta_primary",        {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("approccio.cta_primary_href",   {"label": "CTA · destinazione", "type": "select",
                                                    "choices": ["home", "approccio", "servizi", "settori",
                                                                "insights", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "servizi_page",
        "label": "Pagina Servizi",
        "icon": "bi-briefcase",
        "region": ".jr-section",
        "page": "servizi",
        "keywords": ["servizi", "services", "offerte", "processo", "faq", "prezzi"],
        "help": "Pagina Servizi: intestazione, etichette card, processo, FAQ, CTA finale. Le 7 offerte sono editabili per riga nel blocco indicizzato `Servizi · Offerte`.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("servizi.eyebrow",               {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("servizi.headline",              {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("servizi.intro",                 {"label": "Intro", "type": "textarea", "max_length": 600}),
            ]},
            {"label": "Card · etichette meta", "fields": [
                ("servizi.svc_duration_label",    {"label": "Durata · etichetta", "type": "text", "max_length": 40}),
                ("servizi.svc_price_label",       {"label": "Prezzo · etichetta", "type": "text", "max_length": 40}),
                ("servizi.svc_deliverables_label",{"label": "Deliverables · etichetta", "type": "text", "max_length": 60}),
                ("servizi.svc_engagement_label",  {"label": "Modalità · etichetta", "type": "text", "max_length": 40}),
            ]},
            {"label": "Processo · intestazione", "fields": [
                ("servizi.process_label",         {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("servizi.process_heading",       {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "FAQ · intestazione", "fields": [
                ("servizi.faq_label",             {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("servizi.faq_heading",           {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "CTA finale", "fields": [
                ("servizi.cta_heading",           {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("servizi.cta_intro",             {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("servizi.cta_primary",           {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("servizi.cta_primary_href",      {"label": "CTA · destinazione", "type": "select",
                                                     "choices": ["home", "approccio", "servizi", "settori",
                                                                 "insights", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "settori_page",
        "label": "Pagina Settori",
        "icon": "bi-diagram-3",
        "region": ".jr-section",
        "page": "settori",
        "keywords": ["settori", "sectors", "team", "aree", "partner"],
        "help": "Pagina Settori: intestazione, heading fascia settori, heading team. Le 6 aree e il team (10 persone) sono editabili per riga nei blocchi indicizzati.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("settori.eyebrow",         {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("settori.headline",        {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("settori.intro",           {"label": "Intro", "type": "textarea", "max_length": 600}),
            ]},
            {"label": "Aree · intestazione", "fields": [
                ("settori.sectors_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("settori.sectors_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Team · intestazione", "fields": [
                ("settori.team_label",      {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("settori.team_heading",    {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("settori.team_intro",      {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "CTA finale", "fields": [
                ("settori.cta_heading",     {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("settori.cta_intro",       {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("settori.cta_primary",     {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("settori.cta_primary_href",{"label": "CTA · destinazione", "type": "select",
                                              "choices": ["home", "approccio", "servizi", "settori",
                                                          "insights", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "insights_page",
        "label": "Pagina Insights (blog index)",
        "icon": "bi-journal-richtext",
        "region": ".jr-section",
        "page": "insights",
        "keywords": ["insights", "blog", "note", "pubblicazioni", "archivio"],
        "help": "Pagina-indice insights. I singoli post (titolo, corpo) restano da registry.",
        "fields": [
            ("insights.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("insights.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("insights.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("insights.posts_intro",      {"label": "Intro sopra le card", "type": "textarea", "max_length": 400}),
            ("insights.card_topic_label",    {"label": "Card · etichetta Area", "type": "text", "max_length": 40}),
            ("insights.card_author_label",   {"label": "Card · etichetta Autore", "type": "text", "max_length": 40}),
            ("insights.card_reading_label",  {"label": "Card · etichetta Lettura", "type": "text", "max_length": 40}),
            ("insights.topics_label",     {"label": "Filtro · etichetta", "type": "text", "max_length": 40}),
            ("insights.cta_heading",      {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("insights.cta_intro",        {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("insights.cta_primary",      {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
            ("insights.cta_primary_href", {"label": "CTA · destinazione", "type": "select",
                                             "choices": ["home", "approccio", "servizi", "settori",
                                                         "insights", "contatti"]}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-telephone",
        "region": ".jr-section",
        "page": "contatti",
        "keywords": ["contatti", "form", "sedi", "canali", "slot", "call", "strategy"],
        "help": "Pagina Contatti: copy, chip prossimo slot, titoli form + etichette campi indirizzo. Struttura form (campi, select, sezioni) resta da registry.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("contatti.eyebrow",              {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("contatti.headline",             {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("contatti.intro",                {"label": "Intro", "type": "textarea", "max_length": 700}),
            ]},
            {"label": "Prossimo slot · chip", "fields": [
                ("contatti.slot_label",           {"label": "Etichetta slot", "type": "text", "max_length": 60}),
                ("contatti.slot_value",           {"label": "Valore slot", "type": "text", "max_length": 120}),
                ("contatti.slot_note",            {"label": "Nota slot", "type": "textarea", "max_length": 240}),
            ]},
            {"label": "Form · titolo e invio", "fields": [
                ("contatti.form_label",           {"label": "Eyebrow", "type": "text", "max_length": 60}),
                ("contatti.form_heading",         {"label": "Titolo form", "type": "richtext", "max_length": 220}),
                ("contatti.form_intro",           {"label": "Intro form", "type": "textarea", "max_length": 500}),
                ("contatti.form_submit_label",    {"label": "CTA submit", "type": "text", "max_length": 60}),
                ("contatti.form_submit_note",     {"label": "Nota sotto il pulsante", "type": "textarea", "max_length": 300}),
                ("contatti.form_consent",         {"label": "Testo consenso privacy", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Indirizzo ufficio · etichette", "fields": [
                ("contatti.office_address_label", {"label": "Etichetta Indirizzo", "type": "text", "max_length": 40}),
                ("contatti.office_area_label",    {"label": "Etichetta Quartiere", "type": "text", "max_length": 40}),
                ("contatti.office_phone_label",   {"label": "Etichetta Telefono", "type": "text", "max_length": 40}),
                ("contatti.office_email_label",   {"label": "Etichetta Email", "type": "text", "max_length": 40}),
            ]},
            {"label": "Sedi · intestazione", "fields": [
                ("contatti.offices_label",        {"label": "Eyebrow", "type": "text", "max_length": 60}),
            ]},
            {"label": "Canali · intestazione", "fields": [
                ("contatti.channels_label",       {"label": "Eyebrow", "type": "text", "max_length": 60}),
            ]},
            {"label": "Footnote", "fields": [
                ("contatti.footnote",             {"label": "Footnote piè pagina", "type": "textarea", "max_length": 500}),
            ]},
        ],
    },
    {
        "id": "contact_info",
        "label": "Contatti · footer",
        "icon": "bi-telephone-forward",
        "region": ".jr-foot",
        "page": "*",
        "keywords": ["footer", "phone", "email", "indirizzo", "orari", "licenza", "hours"],
        "help": "Dati di contatto visibili in footer + orari + licenza/P.IVA + intro voce dello studio.",
        "fields": [
            ("site.phone",         {"label": "Telefono", "type": "text", "max_length": 40}),
            ("site.email",         {"label": "Email", "type": "text", "max_length": 80}),
            ("site.address",       {"label": "Indirizzo sede primaria", "type": "text", "max_length": 120}),
            ("site.hours_compact", {"label": "Orari sintetici", "type": "text", "max_length": 100}),
            ("site.license",       {"label": "Licenza / P.IVA", "type": "text", "max_length": 160}),
            ("site.footer_intro",  {"label": "Intro footer", "type": "textarea", "max_length": 500}),
            ("site.foot_studio",   {"label": "Footer · titolo Studio", "type": "text", "max_length": 40}),
            ("site.foot_pages",    {"label": "Footer · titolo Pagine", "type": "text", "max_length": 40}),
            ("site.foot_contact",  {"label": "Footer · titolo Contatti", "type": "text", "max_length": 40}),
            ("site.foot_offices",  {"label": "Footer · titolo Sedi", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "post_chrome",
        "label": "Insights · etichette post",
        "icon": "bi-tags",
        "region": ".jr-section",
        "page": "insights",
        "keywords": ["post", "insights", "meta", "pubblicato", "lettura", "autore", "area"],
        "help": "Etichette meta comuni a ogni post (pubblicato il, lettura, autore, area, link back).",
        "fields": [
            ("site.post_date_label",    {"label": "Etichetta Pubblicato", "type": "text", "max_length": 40}),
            ("site.post_reading_label", {"label": "Etichetta Lettura", "type": "text", "max_length": 40}),
            ("site.post_author_label",  {"label": "Etichetta Autore", "type": "text", "max_length": 40}),
            ("site.post_topic_label",   {"label": "Etichetta Area", "type": "text", "max_length": 40}),
            ("site.post_back_label",    {"label": "Etichetta link all'archivio", "type": "text", "max_length": 60}),
        ],
    },
]


# A.12 · Casa mass-market — 7th enrolled editor archetype, first template
# of the real-estate family (`real-estate` category). Villa
# (`ultra-luxury-cinematic`) stays explicitly OUT of this phase and is
# reserved for a separate A.12b enrollment with its own schema + skin
# bridge + lifecycle test. The two real-estate templates carry distinct
# archetypes + distinct skin folders + ZERO non-home page-slug overlap
# (Casa: home/immobili/quartieri/agenzia/valutazione/contatti vs Villa:
# home/collezione/territorio/studio/esperienza/concierge), so the A.9
# shared-schema recipe does NOT apply here — A.12/A.12b mirrors the
# A.10/A.11 law-family closure topology (two dedicated schemas).
#
# Casa is the SECOND zero-image archetype after Juris (A.11) — DNA
# mass-market doesn't ship any image fields in the registry. This is
# locked by the user-imposed guardrail test
# `test_a12_casa_schema_contains_zero_image_fields` that iterates the
# entire schema + `STRUCTURED_FIELD_SHAPES` tree asserting no field
# carries `type: "image"`.
#
# Shape contract notes (see mini-audit in the A.12 planning memo):
#   • 10 sidebar groups cover all 6 Casa pages (home, immobili, quartieri,
#     agenzia, valutazione, contatti) + chrome (brand, contact_info,
#     post_chrome). Skin uses `.dm-*` selectors (23 mature html[dir="rtl"]
#     rules already in `real-estate/mass-market/_base.html`).
#   • ``home.search_widget`` (nested dict, 15 keys) is FLATTENED into
#     scalar fields inside the ``hero_home`` group per the A.12 planning
#     decision (14 scalars IN — no sub-dict editor widget is introduced).
#     Its ``popular_tags`` list-of-str stays registry-only.
#   • Complex shapes explicitly KEPT OUT of the perimeter by design:
#       - ``home.search_widget.popular_tags`` (flat list-of-str)
#       - ``immobili.filters`` + ``immobili.sort_options`` (flat
#         list-of-str — same exclusion pattern as Juris trust_logos)
#       - Property-detail entries in ``posts`` (12 property records with
#         per-property copy like Lex ``notabili``) — stays registry-only
#   • Form structure blocks (``valutazione.form_fields`` +
#     ``form_sections``, ``contatti.form_fields`` + ``form_sections``)
#     stay OUT — same policy as Gusto / specialist / Lex / Juris.
#   • 15 readonly indexed lists (more than Juris's 6 because Casa is
#     structurally richer — 5 home lists + 3 quartieri lists + 2 agenzia
#     lists + 3 valutazione lists + 1 immobili list + 1 contatti list).
#     No `mutable: True` flag anywhere (same as every archetype except
#     Vertex A.3a).

CASA_MASS_MARKET_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".dm-nav, .dm-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "agenzia", "tagline", "insegna"],
        "help": "Nome agenzia, iniziale crest e tagline.",
        "fields": [
            ("site.logo_word",    {"label": "Nome agenzia", "type": "text", "max_length": 60,
                                    "placeholder": "Domus Immobiliare"}),
            ("site.logo_initial", {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.tag",          {"label": "Tagline", "type": "text", "max_length": 100}),
            ("site.nav_cta",      {"label": "CTA nav", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home · search widget",
        "icon": "bi-easel",
        "region": ".dm-hero, .dm-search",
        "page": "home",
        "keywords": ["hero", "apertura", "headline", "eyebrow", "intro", "cta", "search", "ricerca", "widget"],
        "help": "Primo scroll della home: eyebrow, headline, intro, CTA principali e widget di ricerca (label + valori dei 4 campi + CTA + nota).",
        "subgroups": [
            {"label": "Hero copy", "fields": [
                ("home.eyebrow",             {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("home.headline",            {"label": "Headline", "type": "richtext", "max_length": 220,
                                                "help": "Consentiti i tag <em> per gli italici."}),
                ("home.intro",               {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.primary_cta",         {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.primary_href",        {"label": "CTA primaria · destinazione", "type": "select",
                                                "choices": ["home", "immobili", "quartieri", "agenzia",
                                                            "valutazione", "contatti"]}),
                ("home.secondary_cta",       {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
                ("home.secondary_href",      {"label": "CTA secondaria · destinazione", "type": "select",
                                                "choices": ["home", "immobili", "quartieri", "agenzia",
                                                            "valutazione", "contatti"]}),
                ("home.hero_availability",   {"label": "Disponibilità (pill)", "type": "text", "max_length": 80}),
                ("home.hero_response",       {"label": "Tempo risposta (pill)", "type": "text", "max_length": 80}),
            ]},
            {"label": "Search widget · intestazione", "fields": [
                ("home.search_widget.label",           {"label": "Etichetta widget", "type": "text", "max_length": 60}),
                ("home.search_widget.intro",           {"label": "Intro widget", "type": "textarea", "max_length": 200}),
            ]},
            {"label": "Search widget · 4 campi", "fields": [
                ("home.search_widget.location_label",  {"label": "Dove · etichetta", "type": "text", "max_length": 40}),
                ("home.search_widget.location_value",  {"label": "Dove · valore mostrato", "type": "text", "max_length": 80}),
                ("home.search_widget.type_label",      {"label": "Tipo · etichetta", "type": "text", "max_length": 40}),
                ("home.search_widget.type_value",      {"label": "Tipo · valore mostrato", "type": "text", "max_length": 80}),
                ("home.search_widget.price_label",     {"label": "Prezzo · etichetta", "type": "text", "max_length": 40}),
                ("home.search_widget.price_value",     {"label": "Prezzo · valore mostrato", "type": "text", "max_length": 80}),
                ("home.search_widget.rooms_label",     {"label": "Camere · etichetta", "type": "text", "max_length": 40}),
                ("home.search_widget.rooms_value",     {"label": "Camere · valore mostrato", "type": "text", "max_length": 80}),
            ]},
            {"label": "Search widget · CTA", "fields": [
                ("home.search_widget.cta",             {"label": "Cerca · CTA", "type": "text", "max_length": 60}),
                ("home.search_widget.cta_href",        {"label": "Cerca · destinazione", "type": "select",
                                                         "choices": ["home", "immobili", "quartieri", "agenzia",
                                                                     "valutazione", "contatti"]}),
                ("home.search_widget.secondary_note", {"label": "Nota secondaria (WhatsApp)", "type": "textarea", "max_length": 200}),
                ("home.search_widget.popular_label",   {"label": "Popolari · etichetta", "type": "text", "max_length": 40}),
            ]},
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".dm-section",
        "page": "home",
        "keywords": ["featured", "neighborhoods", "stats", "agents", "valuation", "testimonial", "cta", "fasce", "quartieri home"],
        "help": "Eyebrow, titoli, intro delle fasce home (featured · quartieri · stats · agenti · valutazione · testimonial).",
        "subgroups": [
            {"label": "Featured listings · intestazione", "fields": [
                ("home.featured_label",        {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.featured_heading",      {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.featured_intro",        {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.featured_link",         {"label": "Link all'elenco · etichetta", "type": "text", "max_length": 60}),
                ("home.featured_link_href",    {"label": "Link · destinazione", "type": "select",
                                                 "choices": ["home", "immobili", "quartieri", "agenzia",
                                                             "valutazione", "contatti"]}),
            ]},
            {"label": "Quartieri · intestazione", "fields": [
                ("home.neighborhoods_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.neighborhoods_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.neighborhoods_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.neighborhoods_cta",     {"label": "CTA · etichetta", "type": "text", "max_length": 80}),
                ("home.neighborhoods_cta_href",{"label": "CTA · destinazione", "type": "select",
                                                 "choices": ["home", "immobili", "quartieri", "agenzia",
                                                             "valutazione", "contatti"]}),
            ]},
            {"label": "Stats · intestazione", "fields": [
                ("home.stats_label",           {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.stats_heading",         {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.stats_intro",           {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.stats_note",            {"label": "Nota in calce", "type": "textarea", "max_length": 240}),
            ]},
            {"label": "Agenti · intestazione", "fields": [
                ("home.agents_label",          {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.agents_heading",        {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.agents_intro",          {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.agents_cta",            {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("home.agents_cta_href",       {"label": "CTA · destinazione", "type": "select",
                                                 "choices": ["home", "immobili", "quartieri", "agenzia",
                                                             "valutazione", "contatti"]}),
            ]},
            {"label": "Valutazione · CTA band", "fields": [
                ("home.valuation_label",       {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.valuation_heading",     {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.valuation_intro",       {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.valuation_cta",         {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.valuation_cta_href",    {"label": "CTA primaria · destinazione", "type": "select",
                                                 "choices": ["home", "immobili", "quartieri", "agenzia",
                                                             "valutazione", "contatti"]}),
                ("home.valuation_secondary",   {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
                ("home.valuation_secondary_href", {"label": "CTA secondaria · destinazione", "type": "select",
                                                    "choices": ["home", "immobili", "quartieri", "agenzia",
                                                                "valutazione", "contatti"]}),
            ]},
            {"label": "Testimonial", "fields": [
                ("home.testimonial_label",     {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.testimonial_quote",     {"label": "Citazione", "type": "textarea", "max_length": 400}),
                ("home.testimonial_author",    {"label": "Autore", "type": "text", "max_length": 80}),
                ("home.testimonial_meta",      {"label": "Meta (ruolo/contesto)", "type": "text", "max_length": 120}),
            ]},
        ],
    },
    {
        "id": "immobili_page",
        "label": "Pagina Immobili",
        "icon": "bi-buildings",
        "region": ".dm-section",
        "page": "immobili",
        "keywords": ["immobili", "annunci", "listings", "filtri", "ordina", "properties"],
        "help": "Pagina elenco immobili: intestazione + etichette filtri/ordina. I 12 immobili e i filtri (list-of-str) restano registry-only.",
        "fields": [
            ("immobili.eyebrow",           {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("immobili.headline",          {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("immobili.intro",             {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("immobili.filter_label",      {"label": "Etichetta filtro", "type": "text", "max_length": 40}),
            ("immobili.sort_label",        {"label": "Etichetta ordina", "type": "text", "max_length": 40}),
            ("immobili.map_label",         {"label": "Mappa · eyebrow", "type": "text", "max_length": 60}),
            ("immobili.map_heading",       {"label": "Mappa · titolo", "type": "richtext", "max_length": 220}),
            ("immobili.map_intro",         {"label": "Mappa · intro", "type": "textarea", "max_length": 400}),
            ("immobili.cta_heading",       {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("immobili.cta_intro",         {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("immobili.cta_primary",       {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
            ("immobili.cta_primary_href",  {"label": "CTA · destinazione", "type": "select",
                                             "choices": ["home", "immobili", "quartieri", "agenzia",
                                                         "valutazione", "contatti"]}),
        ],
    },
    {
        "id": "quartieri_page",
        "label": "Pagina Quartieri",
        "icon": "bi-geo",
        "region": ".dm-section",
        "page": "quartieri",
        "keywords": ["quartieri", "neighborhoods", "guide", "faq", "aree"],
        "help": "Pagina quartieri: intestazione, label sezioni guide/faq, CTA finale.",
        "fields": [
            ("quartieri.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("quartieri.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("quartieri.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("quartieri.guides_label",     {"label": "Guide · eyebrow", "type": "text", "max_length": 80}),
            ("quartieri.guides_heading",   {"label": "Guide · titolo", "type": "richtext", "max_length": 220}),
            ("quartieri.guides_intro",     {"label": "Guide · intro", "type": "textarea", "max_length": 500}),
            ("quartieri.faq_label",        {"label": "FAQ · eyebrow", "type": "text", "max_length": 80}),
            ("quartieri.faq_heading",      {"label": "FAQ · titolo", "type": "richtext", "max_length": 220}),
            ("quartieri.cta_heading",      {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("quartieri.cta_intro",        {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("quartieri.cta_primary",      {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
            ("quartieri.cta_primary_href", {"label": "CTA · destinazione", "type": "select",
                                             "choices": ["home", "immobili", "quartieri", "agenzia",
                                                         "valutazione", "contatti"]}),
        ],
    },
    {
        "id": "agenzia_page",
        "label": "Pagina Agenzia",
        "icon": "bi-people",
        "region": ".dm-section",
        "page": "agenzia",
        "keywords": ["agenzia", "team", "agenti", "fatti", "storia"],
        "help": "Pagina agenzia: intestazione, label sezioni agenti/fatti, CTA finale. 9 agenti e 4 facts editabili per riga nei blocchi indicizzati.",
        "fields": [
            ("agenzia.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("agenzia.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("agenzia.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("agenzia.agents_label",     {"label": "Agenti · eyebrow", "type": "text", "max_length": 80}),
            ("agenzia.agents_heading",   {"label": "Agenti · titolo", "type": "richtext", "max_length": 220}),
            ("agenzia.facts_label",      {"label": "Fatti · eyebrow", "type": "text", "max_length": 80}),
            ("agenzia.facts_heading",    {"label": "Fatti · titolo", "type": "richtext", "max_length": 220}),
            ("agenzia.cta_heading",      {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("agenzia.cta_intro",        {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("agenzia.cta_primary",      {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
            ("agenzia.cta_primary_href", {"label": "CTA · destinazione", "type": "select",
                                           "choices": ["home", "immobili", "quartieri", "agenzia",
                                                       "valutazione", "contatti"]}),
        ],
    },
    {
        "id": "valutazione_page",
        "label": "Pagina Valutazione",
        "icon": "bi-calculator",
        "region": ".dm-section",
        "page": "valutazione",
        "keywords": ["valutazione", "services", "stima", "come-funziona", "faq", "prove", "form"],
        "help": "Pagina valutazione: intestazione, label sezioni how_it_works/proof/faq, label sopra il form + nota invio + testo consenso. Struttura form (campi/sezioni) resta registry-only.",
        "fields": [
            ("valutazione.eyebrow",             {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("valutazione.headline",            {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("valutazione.intro",               {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("valutazione.how_it_works_label",  {"label": "Processo · eyebrow", "type": "text", "max_length": 80}),
            ("valutazione.how_it_works_heading",{"label": "Processo · titolo", "type": "richtext", "max_length": 220}),
            ("valutazione.proof_label",         {"label": "Prove · eyebrow", "type": "text", "max_length": 80}),
            ("valutazione.proof_heading",       {"label": "Prove · titolo", "type": "richtext", "max_length": 220}),
            ("valutazione.faq_label",           {"label": "FAQ · eyebrow", "type": "text", "max_length": 80}),
            ("valutazione.faq_heading",         {"label": "FAQ · titolo", "type": "richtext", "max_length": 220}),
            ("valutazione.form_label",          {"label": "Form · eyebrow", "type": "text", "max_length": 80}),
            ("valutazione.form_heading",        {"label": "Form · titolo", "type": "richtext", "max_length": 220}),
            ("valutazione.form_intro",          {"label": "Form · intro", "type": "textarea", "max_length": 500}),
            ("valutazione.form_submit_label",   {"label": "Form · CTA submit", "type": "text", "max_length": 60}),
            ("valutazione.form_submit_note",    {"label": "Form · nota submit", "type": "textarea", "max_length": 300}),
            ("valutazione.form_consent",        {"label": "Form · testo consenso", "type": "textarea", "max_length": 500}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-telephone",
        "region": ".dm-section",
        "page": "contatti",
        "keywords": ["contatti", "contact", "sedi", "canali", "form", "ufficio"],
        "help": "Pagina contatti: copy + label sezione sedi/canali + label form. Struttura form resta registry-only.",
        "fields": [
            ("contatti.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("contatti.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("contatti.intro",            {"label": "Intro", "type": "textarea", "max_length": 700}),
            ("contatti.offices_label",    {"label": "Sedi · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.offices_heading",  {"label": "Sedi · titolo", "type": "richtext", "max_length": 220}),
            ("contatti.channels_label",   {"label": "Canali · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.channels_heading", {"label": "Canali · titolo", "type": "richtext", "max_length": 220}),
            ("contatti.form_label",       {"label": "Form · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.form_heading",     {"label": "Form · titolo", "type": "richtext", "max_length": 220}),
            ("contatti.form_intro",       {"label": "Form · intro", "type": "textarea", "max_length": 500}),
            ("contatti.form_submit_label",{"label": "Form · CTA submit", "type": "text", "max_length": 60}),
            ("contatti.form_submit_note", {"label": "Form · nota submit", "type": "textarea", "max_length": 300}),
            ("contatti.form_consent",     {"label": "Form · testo consenso", "type": "textarea", "max_length": 500}),
        ],
    },
    {
        "id": "contact_info",
        "label": "Contatti · footer",
        "icon": "bi-telephone-forward",
        "region": ".dm-foot",
        "page": "*",
        "keywords": ["footer", "phone", "email", "indirizzo", "orari", "licenza", "whatsapp"],
        "help": "Dati di contatto visibili in footer + intro voce dell'agenzia + titoli sezioni footer + etichette tile immobili (riusate nel listing).",
        "fields": [
            ("site.phone",             {"label": "Telefono", "type": "text", "max_length": 40}),
            ("site.email",             {"label": "Email", "type": "text", "max_length": 80}),
            ("site.address",           {"label": "Indirizzo sede primaria", "type": "text", "max_length": 120}),
            ("site.address_short",     {"label": "Indirizzo compatto", "type": "text", "max_length": 60}),
            ("site.hours_compact",     {"label": "Orari sintetici", "type": "text", "max_length": 100}),
            ("site.phone_label",       {"label": "Telefono · etichetta", "type": "text", "max_length": 40}),
            ("site.whatsapp",          {"label": "WhatsApp · numero", "type": "text", "max_length": 40}),
            ("site.whatsapp_note",     {"label": "WhatsApp · nota", "type": "textarea", "max_length": 200}),
            ("site.license",           {"label": "Licenza / P.IVA", "type": "text", "max_length": 160}),
            ("site.footer_intro",      {"label": "Intro footer", "type": "textarea", "max_length": 500}),
            ("site.foot_studio",       {"label": "Footer · titolo Agenzia", "type": "text", "max_length": 40}),
            ("site.foot_pages",        {"label": "Footer · titolo Pagine", "type": "text", "max_length": 40}),
            ("site.foot_contact",      {"label": "Footer · titolo Contatti", "type": "text", "max_length": 40}),
            ("site.foot_offices",      {"label": "Footer · titolo Sedi", "type": "text", "max_length": 40}),
            ("site.visit_request_label",{"label": "CTA Visita · etichetta", "type": "text", "max_length": 60}),
            ("site.showings_schedule", {"label": "Visite · disponibilità", "type": "text", "max_length": 160}),
        ],
    },
    {
        "id": "tile_labels",
        "label": "Etichette tile immobile",
        "icon": "bi-tag",
        "region": ".dm-tile",
        "page": "*",
        "keywords": ["tile", "card", "immobile", "etichette", "rooms", "surface", "bathrooms", "reference", "energy"],
        "help": "Etichette riusate su ogni card immobile (camere, superficie, bagni, classe energetica, piano, prezzo, rif.).",
        "fields": [
            ("site.tile_rooms_label",      {"label": "Camere · etichetta", "type": "text", "max_length": 40}),
            ("site.tile_surface_label",    {"label": "Superficie · etichetta", "type": "text", "max_length": 40}),
            ("site.tile_bathrooms_label",  {"label": "Bagni · etichetta", "type": "text", "max_length": 40}),
            ("site.tile_surface_unit",     {"label": "Superficie · unità", "type": "text", "max_length": 16}),
            ("site.tile_visit_cta",        {"label": "Card · CTA visita", "type": "text", "max_length": 60}),
            ("site.tile_reference_label",  {"label": "Rif. · etichetta", "type": "text", "max_length": 40}),
            ("site.price_label",           {"label": "Prezzo · etichetta", "type": "text", "max_length": 40}),
            ("site.energy_class_label",    {"label": "Classe energetica · etichetta", "type": "text", "max_length": 60}),
            ("site.floor_label",           {"label": "Piano · etichetta", "type": "text", "max_length": 40}),
            ("site.parking_label",         {"label": "Posto auto · etichetta", "type": "text", "max_length": 40}),
            ("site.elevator_label",        {"label": "Ascensore · etichetta", "type": "text", "max_length": 40}),
            ("site.filter_label",          {"label": "Filtro · etichetta", "type": "text", "max_length": 40}),
            ("site.sort_label",            {"label": "Ordina · etichetta", "type": "text", "max_length": 40}),
            ("site.viewings_unit",         {"label": "Visite · unità", "type": "text", "max_length": 60}),
            ("site.surface_short",         {"label": "Superficie · unità breve", "type": "text", "max_length": 16}),
        ],
    },
]


# A.12b · Villa ultra-luxury-cinematic — 8th enrolled editor archetype,
# second template of the real-estate family. Closes the real-estate
# family opened in A.12 with Casa (mass-market). The two real-estate
# templates ship distinct archetypes + distinct skin folders
# (`real-estate/mass-market/` with `.dm-*` vs `real-estate/
# ultra-luxury-cinematic/` with `.vp-*`) and ~0% non-home page-slug
# overlap (Casa: home/immobili/quartieri/agenzia/valutazione/contatti
# vs Villa: home/collezione/territorio/studio/esperienza/concierge —
# only `home` shared). Shared-schema (A.9 recipe) is impossible; Casa
# + Villa close the family via the staged dedicated-schema progression
# D-098 topology (A.12 first, A.12b second).
#
# Villa is IMAGERY-HEAVY (the DNA is cinematographic editorial luxury).
# Shape contract notes:
#   • 4 SCALAR image fields: ``home.cover_image`` · ``home.advisor_portrait``
#     · ``studio.director_portrait`` · ``collezione.lead_image``.
#   • 4 LIST-OF-DICT paths expose an image col (22 total image cells):
#       - ``home.signature[].image`` (4 signature properties)
#       - ``territorio.territories[].image`` (6 territory hero images)
#       - ``studio.advisors[].portrait`` (4 advisor portraits)
#       - ``posts[].image`` — INTENTIONALLY OUT of perimeter (posts stay
#         registry-only like Lex notabili / Juris insights / Casa posts)
#     Image-in-dict-row is NOT a novel widget pattern — Vertex has shipped
#     it since A.3a/A.4 (`studio.partners[].portrait`, production since
#     Session 58). Villa is the second archetype to use it, with a
#     strictly smaller surface because Villa's lists are non-mutable
#     (no add/remove row, just cell-level edits).
#   • Complex shapes explicitly KEPT OUT of the perimeter:
#       - ``collezione.filter_groups[].options`` (nested list-of-str,
#         8 filter options per group)
#       - ``concierge.form_fields[].options`` (nested list-of-str,
#         4 select options per field)
#       - Flat list-of-str containers: ``site.hours_footer_rows``,
#         ``site.offices_footer_rows``, ``site.office_rows``,
#         ``home.territory`` (7 territory wordmarks),
#         ``home.press_items`` (5 press wordmarks),
#         ``collezione.sort_options``
#       - ``concierge.form_fields`` structure block (form structure
#         stays registry-only, same policy as every prior archetype)
#       - ``posts`` list entries (8 blog post records, same policy as
#         Lex/Juris/Casa)
#   • 14 readonly indexed lists (4 with image cols). No `mutable: True`.

VILLA_ULTRA_LUXURY_CINEMATIC_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".vp-nav, .vp-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "villa", "tagline", "advisory", "private"],
        "help": "Nome studio, iniziale crest, sottolinea e tagline.",
        "fields": [
            ("site.logo_word",    {"label": "Nome studio", "type": "text", "max_length": 60,
                                    "placeholder": "Villa Prestige"}),
            ("site.logo_initial", {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.logo_subline", {"label": "Sottolinea (anno / claim breve)", "type": "text", "max_length": 80}),
            ("site.tag",          {"label": "Tagline / portfolio header", "type": "text", "max_length": 120}),
            ("site.nav_cta",      {"label": "CTA nav", "type": "text", "max_length": 60}),
            ("site.nav_cta_short",{"label": "CTA nav · variante breve", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".vp-hero",
        "page": "home",
        "keywords": ["hero", "cover", "headline", "series", "counter", "cta", "credit"],
        "help": "Primo scroll della home: cover image + crediti, hero copy, serie/counter, CTA, credit cells.",
        "subgroups": [
            {"label": "Cover image + credit", "fields": [
                ("home.cover_image",         {"label": "Cover image · URL", "type": "image", "max_length": 400}),
                ("home.cover_location",      {"label": "Cover · location", "type": "text", "max_length": 120}),
                ("home.cover_image_credit",  {"label": "Cover · credit", "type": "text", "max_length": 160}),
            ]},
            {"label": "Hero copy", "fields": [
                ("home.eyebrow",             {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("home.headline",            {"label": "Headline", "type": "richtext", "max_length": 220,
                                                "help": "Consentiti i tag <em> per gli italici."}),
                ("home.sub",                 {"label": "Sottotitolo", "type": "textarea", "max_length": 500}),
                ("home.hero_wordmark",       {"label": "Wordmark hero", "type": "text", "max_length": 40}),
                ("home.hero_location",       {"label": "Location hero", "type": "text", "max_length": 120}),
            ]},
            {"label": "Counter + series", "fields": [
                ("home.hero_counter_label",  {"label": "Counter · label", "type": "text", "max_length": 60}),
                ("home.hero_counter_value",  {"label": "Counter · valore", "type": "text", "max_length": 40}),
                ("home.hero_series_label",   {"label": "Series · label", "type": "text", "max_length": 40}),
                ("home.hero_series_title",   {"label": "Series · titolo", "type": "text", "max_length": 120}),
                ("home.hero_series_note",    {"label": "Series · nota", "type": "textarea", "max_length": 300}),
            ]},
            {"label": "CTA hero", "fields": [
                ("home.primary_cta",         {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.primary_cta_href",    {"label": "CTA primaria · destinazione", "type": "select",
                                                "choices": ["home", "collezione", "territorio", "studio",
                                                            "esperienza", "concierge"]}),
                ("home.secondary_cta",       {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
                ("home.secondary_cta_href",  {"label": "CTA secondaria · destinazione", "type": "select",
                                                "choices": ["home", "collezione", "territorio", "studio",
                                                            "esperienza", "concierge"]}),
            ]},
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".vp-section",
        "page": "home",
        "keywords": ["signature", "territory", "advisor", "numbers", "press", "private", "fasce"],
        "help": "Eyebrow, titoli, intro delle fasce home (signature · territory · advisor · numbers · press · private CTA).",
        "subgroups": [
            {"label": "Signature · intestazione", "fields": [
                ("home.signature_label",      {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.signature_heading",    {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.signature_intro",      {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.signature_link_all",   {"label": "Link all'archivio · etichetta", "type": "text", "max_length": 80}),
                ("home.signature_link_href",  {"label": "Link · destinazione", "type": "select",
                                                 "choices": ["home", "collezione", "territorio", "studio",
                                                             "esperienza", "concierge"]}),
            ]},
            {"label": "Territory · intestazione", "fields": [
                ("home.territory_label",      {"label": "Eyebrow", "type": "text", "max_length": 80}),
            ]},
            {"label": "Advisor · featured", "fields": [
                ("home.advisor_label",        {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.advisor_heading",      {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.advisor_intro",        {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.advisor_name",         {"label": "Nome advisor", "type": "text", "max_length": 80}),
                ("home.advisor_role",         {"label": "Ruolo advisor", "type": "text", "max_length": 120}),
                ("home.advisor_bio",          {"label": "Bio advisor", "type": "textarea", "max_length": 500}),
                ("home.advisor_portrait",     {"label": "Advisor · ritratto (URL)", "type": "image", "max_length": 400}),
                ("home.advisor_cta",          {"label": "CTA advisor · etichetta", "type": "text", "max_length": 60}),
                ("home.advisor_cta_href",     {"label": "CTA advisor · destinazione", "type": "select",
                                                 "choices": ["home", "collezione", "territorio", "studio",
                                                             "esperienza", "concierge"]}),
            ]},
            {"label": "Numbers · intestazione", "fields": [
                ("home.numbers_label",        {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.numbers_heading",      {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.numbers_note",         {"label": "Nota in calce", "type": "textarea", "max_length": 240}),
            ]},
            {"label": "Press · intestazione", "fields": [
                ("home.press_label",          {"label": "Eyebrow", "type": "text", "max_length": 60}),
                ("home.press_intro",          {"label": "Intro breve", "type": "text", "max_length": 60}),
            ]},
            {"label": "Private CTA band", "fields": [
                ("home.private_label",        {"label": "Eyebrow", "type": "text", "max_length": 60}),
                ("home.private_heading",      {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.private_intro",        {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.private_primary",      {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.private_primary_href", {"label": "CTA primaria · destinazione", "type": "select",
                                                 "choices": ["home", "collezione", "territorio", "studio",
                                                             "esperienza", "concierge"]}),
                ("home.private_secondary",    {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
                ("home.private_secondary_href", {"label": "CTA secondaria · destinazione", "type": "select",
                                                   "choices": ["home", "collezione", "territorio", "studio",
                                                               "esperienza", "concierge"]}),
            ]},
        ],
    },
    {
        "id": "collezione_page",
        "label": "Pagina Collezione (blog-list)",
        "icon": "bi-collection",
        "region": ".vp-section",
        "page": "collezione",
        "keywords": ["collezione", "blog-list", "archivio", "filter", "sort", "lead"],
        "help": "Pagina collezione: intestazione, lead image, meta sort/filter, label post-card. I post (blog detail) restano registry-only.",
        "fields": [
            ("collezione.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("collezione.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("collezione.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("collezione.lead_image",       {"label": "Lead image · URL", "type": "image", "max_length": 400}),
            ("collezione.filter_label",     {"label": "Filtro · etichetta", "type": "text", "max_length": 40}),
            ("collezione.sort_label",       {"label": "Ordina · etichetta", "type": "text", "max_length": 40}),
            ("collezione.posts_intro",      {"label": "Intro sopra le card", "type": "textarea", "max_length": 400}),
            ("collezione.card_territory_label", {"label": "Card · etichetta Territorio", "type": "text", "max_length": 40}),
            ("collezione.card_read_label",  {"label": "Card · etichetta Lettura", "type": "text", "max_length": 40}),
            ("collezione.cta_heading",      {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("collezione.cta_intro",        {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("collezione.cta_primary",      {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
            ("collezione.cta_primary_href", {"label": "CTA · destinazione", "type": "select",
                                               "choices": ["home", "collezione", "territorio", "studio",
                                                           "esperienza", "concierge"]}),
        ],
    },
    {
        "id": "territorio_page",
        "label": "Pagina Territorio (about)",
        "icon": "bi-map",
        "region": ".vp-section",
        "page": "territorio",
        "keywords": ["territorio", "regioni", "provenance", "about", "stats"],
        "help": "Pagina territori: intestazione, intro fascia territori, intro statistiche. Le 6 territorie (con image col) sono editabili per riga.",
        "fields": [
            ("territorio.eyebrow",         {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("territorio.headline",        {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("territorio.intro",           {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("territorio.territories_label",   {"label": "Territori · eyebrow", "type": "text", "max_length": 80}),
            ("territorio.territories_heading", {"label": "Territori · titolo", "type": "richtext", "max_length": 220}),
            ("territorio.territories_intro",   {"label": "Territori · intro", "type": "textarea", "max_length": 500}),
            ("territorio.stats_label",     {"label": "Stats · eyebrow", "type": "text", "max_length": 80}),
            ("territorio.stats_heading",   {"label": "Stats · titolo", "type": "richtext", "max_length": 220}),
            ("territorio.cta_heading",     {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("territorio.cta_intro",       {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("territorio.cta_primary",     {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
            ("territorio.cta_primary_href",{"label": "CTA · destinazione", "type": "select",
                                              "choices": ["home", "collezione", "territorio", "studio",
                                                          "esperienza", "concierge"]}),
        ],
    },
    {
        "id": "studio_page",
        "label": "Pagina Studio (team)",
        "icon": "bi-people",
        "region": ".vp-section",
        "page": "studio",
        "keywords": ["studio", "advisor", "partner", "press", "director", "team", "storia"],
        "help": "Pagina studio: intestazione, director block + portrait, intro advisors/partners/press/numbers. I 4 advisor (con portrait col) sono editabili per riga.",
        "fields": [
            ("studio.eyebrow",         {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("studio.headline",        {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("studio.intro",           {"label": "Intro", "type": "textarea", "max_length": 700}),
            ("studio.director_name",   {"label": "Director · nome", "type": "text", "max_length": 80}),
            ("studio.director_role",   {"label": "Director · ruolo", "type": "text", "max_length": 120}),
            ("studio.director_bio",    {"label": "Director · bio", "type": "textarea", "max_length": 800}),
            ("studio.director_portrait", {"label": "Director · ritratto (URL)", "type": "image", "max_length": 400}),
            ("studio.advisors_label",  {"label": "Advisors · eyebrow", "type": "text", "max_length": 80}),
            ("studio.advisors_heading",{"label": "Advisors · titolo", "type": "richtext", "max_length": 220}),
            ("studio.advisors_intro",  {"label": "Advisors · intro", "type": "textarea", "max_length": 500}),
            ("studio.partners_label",  {"label": "Partners · eyebrow", "type": "text", "max_length": 80}),
            ("studio.partners_heading",{"label": "Partners · titolo", "type": "richtext", "max_length": 220}),
            ("studio.partners_intro",  {"label": "Partners · intro", "type": "textarea", "max_length": 500}),
            ("studio.press_label",     {"label": "Press · eyebrow", "type": "text", "max_length": 80}),
            ("studio.press_heading",   {"label": "Press · titolo", "type": "richtext", "max_length": 220}),
            ("studio.numbers_label",   {"label": "Numbers · eyebrow", "type": "text", "max_length": 80}),
            ("studio.numbers_heading", {"label": "Numbers · titolo", "type": "richtext", "max_length": 220}),
            ("studio.cta_heading",     {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("studio.cta_intro",       {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("studio.cta_primary",     {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
            ("studio.cta_primary_href",{"label": "CTA · destinazione", "type": "select",
                                          "choices": ["home", "collezione", "territorio", "studio",
                                                      "esperienza", "concierge"]}),
        ],
    },
    {
        "id": "esperienza_page",
        "label": "Pagina Esperienza (services)",
        "icon": "bi-gem",
        "region": ".vp-section",
        "page": "esperienza",
        "keywords": ["esperienza", "services", "processo", "faq"],
        "help": "Pagina esperienza: intestazione, intro processo, intro FAQ. I 5 step + le 6 FAQ sono editabili per riga.",
        "fields": [
            ("esperienza.eyebrow",         {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("esperienza.headline",        {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("esperienza.intro",           {"label": "Intro", "type": "textarea", "max_length": 700}),
            ("esperienza.process_label",   {"label": "Processo · eyebrow", "type": "text", "max_length": 80}),
            ("esperienza.process_heading", {"label": "Processo · titolo", "type": "richtext", "max_length": 220}),
            ("esperienza.process_intro",   {"label": "Processo · intro", "type": "textarea", "max_length": 500}),
            ("esperienza.faq_label",       {"label": "FAQ · eyebrow", "type": "text", "max_length": 80}),
            ("esperienza.faq_heading",     {"label": "FAQ · titolo", "type": "richtext", "max_length": 220}),
            ("esperienza.cta_heading",     {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("esperienza.cta_intro",       {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("esperienza.cta_primary",     {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
            ("esperienza.cta_primary_href",{"label": "CTA · destinazione", "type": "select",
                                              "choices": ["home", "collezione", "territorio", "studio",
                                                          "esperienza", "concierge"]}),
        ],
    },
    {
        "id": "concierge_page",
        "label": "Pagina Concierge (contact)",
        "icon": "bi-telephone",
        "region": ".vp-section",
        "page": "concierge",
        "keywords": ["concierge", "contact", "form", "sedi", "press", "telefono", "email"],
        "help": "Pagina concierge: intestazione, label form (struttura campi resta registry-only), sedi e press contact. Etichette campi indirizzo.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("concierge.eyebrow",         {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("concierge.headline",        {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("concierge.intro",           {"label": "Intro", "type": "textarea", "max_length": 700}),
            ]},
            {"label": "Phone band", "fields": [
                ("concierge.phone_label",     {"label": "Phone band · etichetta", "type": "text", "max_length": 60}),
                ("concierge.phone_intro",     {"label": "Phone band · intro", "type": "textarea", "max_length": 400}),
            ]},
            {"label": "Form · copy e submit", "fields": [
                ("concierge.form_section_label", {"label": "Form · eyebrow", "type": "text", "max_length": 60}),
                ("concierge.form_section_intro", {"label": "Form · intro", "type": "textarea", "max_length": 400}),
                ("concierge.form_helper_required", {"label": "Form · helper campi obbligatori", "type": "text", "max_length": 120}),
                ("concierge.form_submit_button", {"label": "Form · CTA submit", "type": "text", "max_length": 60}),
                ("concierge.form_submit_note", {"label": "Form · nota submit", "type": "textarea", "max_length": 400}),
            ]},
            {"label": "Sedi", "fields": [
                ("concierge.offices_label",   {"label": "Sedi · eyebrow", "type": "text", "max_length": 60}),
                ("concierge.offices_heading", {"label": "Sedi · titolo", "type": "richtext", "max_length": 220}),
                ("concierge.offices_intro",   {"label": "Sedi · intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Press contact", "fields": [
                ("concierge.press_contact_label", {"label": "Press · etichetta", "type": "text", "max_length": 60}),
                ("concierge.press_contact_text",  {"label": "Press · testo", "type": "textarea", "max_length": 500}),
                ("concierge.press_contact_email", {"label": "Press · email", "type": "text", "max_length": 80}),
            ]},
        ],
    },
    {
        "id": "contact_info",
        "label": "Contatti · footer",
        "icon": "bi-telephone-forward",
        "region": ".vp-foot",
        "page": "*",
        "keywords": ["footer", "phone", "email", "indirizzo", "orari", "licenza"],
        "help": "Dati di contatto visibili in footer + intro voce dello studio + titoli sezioni footer.",
        "fields": [
            ("site.phone",         {"label": "Telefono", "type": "text", "max_length": 80}),
            ("site.email",         {"label": "Email", "type": "text", "max_length": 80}),
            ("site.email_label",   {"label": "Email · etichetta", "type": "text", "max_length": 40}),
            ("site.phone_label",   {"label": "Telefono · etichetta", "type": "text", "max_length": 60}),
            ("site.address",       {"label": "Indirizzo sede primaria", "type": "text", "max_length": 160}),
            ("site.hours_compact", {"label": "Orari sintetici", "type": "text", "max_length": 120}),
            ("site.license",       {"label": "Licenza / P.IVA", "type": "text", "max_length": 200}),
            ("site.footer_intro",  {"label": "Intro footer", "type": "textarea", "max_length": 500}),
            ("site.foot_studio",   {"label": "Footer · titolo Studio", "type": "text", "max_length": 40}),
            ("site.foot_pages",    {"label": "Footer · titolo Pagine", "type": "text", "max_length": 40}),
            ("site.foot_contact",  {"label": "Footer · titolo Contatti", "type": "text", "max_length": 40}),
            ("site.foot_offices",  {"label": "Footer · titolo Sedi", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "tile_labels",
        "label": "Etichette dossier / tile",
        "icon": "bi-tag",
        "region": ".vp-tile",
        "page": "*",
        "keywords": ["dossier", "portfolio", "territorio", "superficie", "provenance", "access", "availability", "tile"],
        "help": "Etichette riusate su ogni card immobile/dossier + note legali chrome.",
        "fields": [
            ("site.dossier_label",       {"label": "Dossier · etichetta", "type": "text", "max_length": 40}),
            ("site.portfolio_label",     {"label": "Portafoglio · etichetta", "type": "text", "max_length": 40}),
            ("site.territorio_label",    {"label": "Territorio · etichetta", "type": "text", "max_length": 40}),
            ("site.superficie_label",    {"label": "Superficie · etichetta", "type": "text", "max_length": 40}),
            ("site.provenance_label",    {"label": "Provenance · etichetta", "type": "text", "max_length": 40}),
            ("site.access_label",        {"label": "Accesso · etichetta", "type": "text", "max_length": 40}),
            ("site.availability_label",  {"label": "Disponibilità · etichetta", "type": "text", "max_length": 40}),
            ("site.price_note",          {"label": "Prezzo · nota default", "type": "text", "max_length": 80}),
            ("site.nda_required_label",  {"label": "NDA · etichetta", "type": "text", "max_length": 80}),
            ("site.viewing_on_request",  {"label": "Viewing · nota default", "type": "text", "max_length": 80}),
            ("site.referent_label",      {"label": "Referente · etichetta", "type": "text", "max_length": 60}),
            ("site.concierge_line_label",{"label": "Linea concierge · etichetta", "type": "text", "max_length": 60}),
        ],
    },
]


# A.13 · Chiara editorial-designer-grid — 9th enrolled editor archetype,
# first template of the portfolio family. Pixel (cinematic-photographer)
# stays explicitly OUT until the dedicated A.13b phase. The two portfolio
# templates ship distinct archetypes + distinct skin folders + only
# `home`+`contatti` page-slug overlap (2/5) — same divergence pattern as
# law (Lex/Juris) and real-estate (Casa/Villa). Shared-schema impossible;
# closure follows staged dedicated-schema progression like A.12+A.12b.
#
# Skin uses `.ed-*` selectors (chrome `.ed-nav`/`.ed-foot`, home
# sections `.ed-hero`/`.ed-projects`/`.ed-press`/`.ed-clients`/etc.,
# studio sections `.ed-founder`/`.ed-team`/`.ed-principles`/etc.) — note
# the prefix collides with the editor sidebar's own `.ed-*` namespace,
# but the two live in DIFFERENT DOM trees (editor shell vs preview
# iframe) so there is no functional conflict; just be aware when adding
# CSS guard rules in `_base.html`.
#
# Shape contract notes (Step-0 audit verified):
#   • 5 pages: home / studio (about) / lavoro (project_list) / processo
#     (NOVEL `process` kind, just a string identifier — no view dispatch)
#     / contatti (contact). 5-locale parity PERFECT (164 keys × 5).
#   • Skin ships 46 `html[dir="rtl"]` rules (highest count of any enrolled
#     archetype, beats Villa's 34) — RTL mature thanks to Session 37
#     D-070 Chiara perfection pass.
#   • 1 SCALAR image field nested inside a parent dict:
#     `studio.founder.image` — same shape as Vertex `home.cover.image`
#     (production since A.1).
#   • 1 list-of-dict path with image col at deep path:
#     `home.featured_works.items[].image` × 4 rows (path is 2 levels
#     deep through `home.featured_works` parent dict). Third precedent
#     of image-in-dict-row after Vertex `studio.partners[].portrait`
#     (A.3a/A.4) and Villa `home.signature/territories/advisors[].image`
#     (A.12b). `_resolve_path` walks any depth — verified.
#   • Total editable image surface: 5 (1 scalar + 4 image cells).
#   • Complex shapes explicitly KEPT OUT of the perimeter:
#       - `studio.founder.credentials` (nested list-of-str, 6 items)
#       - `processo.capabilities_full[].scope` (nested list-of-str
#         inside dict rows · same exclusion policy as Juris
#         `deliverables` and Casa `posts`)
#       - Flat list-of-str: `home.clients` (8 wordmarks · same as Juris
#         `trust_logos`) · `lavoro.filters` (6 filter pills · same as
#         Casa `immobili.filters`)
#       - Form structure blocks: `contatti.form_fields` +
#         `contatti.form_sections` + `contatti.upload_field`
#       - **`posts` list (3 project detail records)** — DETAIL-PAGE
#         editing is NOT in A.13 scope. This is a coherent perimeter
#         decision aligned with Lex `notabili`, Juris `insights`, Casa
#         `posts`, Villa `posts` — per-item content stays registry-only
#         across every enrolled archetype. Detail-page editing is a
#         horizontal feature deferred to a future phase (not bundled
#         into enrollment).

CHIARA_EDITORIAL_DESIGNER_GRID_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".ed-nav, .ed-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "studio", "tagline", "wordmark"],
        "help": "Nome studio, iniziale crest, logo breve e tagline (status badge nav).",
        "fields": [
            ("site.logo_word",    {"label": "Nome studio", "type": "text", "max_length": 60,
                                    "placeholder": "Chiara Velluti"}),
            ("site.logo_initial", {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.logo_short",   {"label": "Logo · forma breve", "type": "text", "max_length": 8}),
            ("site.tag",          {"label": "Tagline (status badge nav)", "type": "text", "max_length": 120}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".ed-hero, .ed-hero-card",
        "page": "home",
        "keywords": ["hero", "headline", "eyebrow", "intro", "cta", "ledger", "registro"],
        "help": "Primo scroll della home: eyebrow, headline, intro, CTA principali, ledger meta (popola .ed-hero-card).",
        "subgroups": [
            {"label": "Hero copy", "fields": [
                ("home.eyebrow",        {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("home.headline",       {"label": "Headline", "type": "richtext", "max_length": 220,
                                          "help": "Consentiti i tag <em> per gli italici."}),
                ("home.intro",          {"label": "Intro", "type": "textarea", "max_length": 600}),
                ("home.primary_cta",    {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.primary_href",   {"label": "CTA primaria · destinazione", "type": "select",
                                          "choices": ["home", "studio", "lavoro", "processo", "contatti"]}),
                ("home.secondary_cta",  {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
                ("home.secondary_href", {"label": "CTA secondaria · destinazione", "type": "select",
                                          "choices": ["home", "studio", "lavoro", "processo", "contatti"]}),
            ]},
            {"label": "Ledger (popola hero card)", "fields": [
                ("home.ledger_label",          {"label": "Ledger · eyebrow", "type": "text", "max_length": 80}),
                ("home.ledger_heading",        {"label": "Ledger · titolo", "type": "richtext", "max_length": 220}),
                ("home.ledger_intro",          {"label": "Ledger · intro", "type": "textarea", "max_length": 500}),
                ("home.ledger_count_prefix",   {"label": "Ledger · prefisso conteggio", "type": "text", "max_length": 8}),
                ("home.ledger_count_unit",     {"label": "Ledger · unità conteggio", "type": "text", "max_length": 24}),
                ("home.ledger_full_link_label",{"label": "Ledger · link archivio · etichetta", "type": "text", "max_length": 60}),
            ]},
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".ed-capabilities, .ed-projects, .ed-clients, .ed-press, .ed-commissions, .ed-cta",
        "page": "home",
        "keywords": ["capabilities", "projects", "clients", "press", "commissions", "cta finale"],
        "help": "Eyebrow, titoli, intro delle fasce home (capabilities, featured projects, clients, press, commissions, CTA finale).",
        "subgroups": [
            {"label": "Capabilities · intestazione", "fields": [
                ("home.capabilities_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.capabilities_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.capabilities_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Featured works · intestazione (parent dict scalars)", "fields": [
                ("home.featured_works.label",       {"label": "Featured · eyebrow", "type": "text", "max_length": 80}),
                ("home.featured_works.heading",     {"label": "Featured · titolo", "type": "richtext", "max_length": 220}),
                ("home.featured_works.intro",       {"label": "Featured · intro", "type": "textarea", "max_length": 500}),
                ("home.featured_works.footer_link", {"label": "Featured · footer link", "type": "text", "max_length": 80}),
                ("home.featured_works.footer_href", {"label": "Featured · footer destinazione", "type": "select",
                                                       "choices": ["home", "studio", "lavoro", "processo", "contatti"]}),
            ]},
            {"label": "Clients · intestazione", "fields": [
                ("home.clients_label",        {"label": "Eyebrow", "type": "text", "max_length": 80}),
            ]},
            {"label": "Press · intestazione", "fields": [
                ("home.press_label",          {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.press_heading",        {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Commissions · intestazione", "fields": [
                ("home.commissions_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.commissions_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.commissions_intro",    {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "CTA finale", "fields": [
                ("home.cta_label",            {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.cta_heading",          {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.cta_intro",            {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.cta_primary",          {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.cta_primary_href",     {"label": "CTA primaria · destinazione", "type": "select",
                                                 "choices": ["home", "studio", "lavoro", "processo", "contatti"]}),
                ("home.cta_secondary",        {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
                ("home.cta_secondary_href",   {"label": "CTA secondaria · destinazione", "type": "select",
                                                 "choices": ["home", "studio", "lavoro", "processo", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "studio_page",
        "label": "Pagina Studio",
        "icon": "bi-building",
        "region": ".ed-lead, .ed-founder, .ed-team, .ed-principles, .ed-press-ledger, .ed-cta-about",
        "page": "studio",
        "keywords": ["studio", "about", "founder", "team", "principles", "press", "credentials"],
        "help": "Pagina studio: lead, founder block (con portrait), team intro, principles intro, press intro, CTA finale.",
        "subgroups": [
            {"label": "Intestazione (lead)", "fields": [
                ("studio.eyebrow",            {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("studio.headline",           {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("studio.intro",              {"label": "Intro", "type": "textarea", "max_length": 700}),
            ]},
            {"label": "Founder block · intestazione", "fields": [
                ("studio.founder_label",      {"label": "Founder · eyebrow", "type": "text", "max_length": 80}),
                ("studio.founder_heading",    {"label": "Founder · titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Founder · scalar block (incl. portrait)", "fields": [
                ("studio.founder.name",       {"label": "Founder · nome", "type": "text", "max_length": 80}),
                ("studio.founder.role",       {"label": "Founder · ruolo", "type": "text", "max_length": 120}),
                ("studio.founder.bio",        {"label": "Founder · biografia", "type": "textarea", "max_length": 800}),
                ("studio.founder.image",      {"label": "Founder · ritratto (URL)", "type": "image", "max_length": 400}),
                # `studio.founder.credentials` (list-of-str) intentionally
                # omitted — complex-shape exclusion (registry-only).
            ]},
            {"label": "Team · intestazione", "fields": [
                ("studio.team_label",         {"label": "Team · eyebrow", "type": "text", "max_length": 80}),
                ("studio.team_heading",       {"label": "Team · titolo", "type": "richtext", "max_length": 220}),
                ("studio.team_intro",         {"label": "Team · intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Principles · intestazione", "fields": [
                ("studio.principles_label",   {"label": "Principles · eyebrow", "type": "text", "max_length": 80}),
                ("studio.principles_heading", {"label": "Principles · titolo", "type": "richtext", "max_length": 220}),
                ("studio.principles_intro",   {"label": "Principles · intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Press · intestazione", "fields": [
                ("studio.press_label",        {"label": "Press · eyebrow", "type": "text", "max_length": 80}),
                ("studio.press_heading",      {"label": "Press · titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "CTA finale", "fields": [
                ("studio.cta_heading",        {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("studio.cta_intro",          {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("studio.cta_primary",        {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("studio.cta_primary_href",   {"label": "CTA · destinazione", "type": "select",
                                                 "choices": ["home", "studio", "lavoro", "processo", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "lavoro_page",
        "label": "Pagina Lavoro (project_list)",
        "icon": "bi-grid-3x3",
        "region": ".ed-section",
        "page": "lavoro",
        "keywords": ["lavoro", "projects", "project_list", "filtri", "ledger", "row labels", "dossier"],
        "help": "Pagina elenco lavori: intestazione + label filtri + ledger meta + row/dossier label tile + CTA. I 3 progetti (project detail) restano registry-only — la modifica per-progetto è una feature orizzontale fuori dalla A.13.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("lavoro.eyebrow",                 {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("lavoro.headline",                {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("lavoro.intro",                   {"label": "Intro", "type": "textarea", "max_length": 600}),
            ]},
            {"label": "Filter + ledger", "fields": [
                ("lavoro.filter_label",            {"label": "Filtro · etichetta", "type": "text", "max_length": 40}),
                ("lavoro.ledger_label",            {"label": "Ledger · eyebrow", "type": "text", "max_length": 80}),
                ("lavoro.ledger_intro",            {"label": "Ledger · intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Row meta · etichette tile", "fields": [
                ("lavoro.row_year_label",          {"label": "Row · etichetta Anno", "type": "text", "max_length": 40}),
                ("lavoro.row_discipline_label",   {"label": "Row · etichetta Disciplina", "type": "text", "max_length": 40}),
                ("lavoro.row_duration_label",     {"label": "Row · etichetta Durata", "type": "text", "max_length": 40}),
            ]},
            {"label": "Dossier (per-detail labels — riusati nel detail page registry-only)", "fields": [
                ("lavoro.dossier_summary_label",        {"label": "Dossier · etichetta Sommario", "type": "text", "max_length": 60}),
                ("lavoro.dossier_deliverables_label",   {"label": "Dossier · etichetta Deliverables (col)", "type": "text", "max_length": 60}),
                ("lavoro.dossier_deliverables_heading", {"label": "Dossier · titolo Deliverables", "type": "text", "max_length": 60}),
                ("lavoro.dossier_meta_year_label",      {"label": "Dossier meta · etichetta Anno", "type": "text", "max_length": 40}),
                ("lavoro.dossier_meta_discipline_label",{"label": "Dossier meta · etichetta Disciplina", "type": "text", "max_length": 40}),
                ("lavoro.dossier_meta_duration_label",  {"label": "Dossier meta · etichetta Durata", "type": "text", "max_length": 40}),
                ("lavoro.dossier_meta_team_label",      {"label": "Dossier meta · etichetta Team", "type": "text", "max_length": 40}),
                ("lavoro.dossier_colophon_label",       {"label": "Dossier · etichetta Colophon", "type": "text", "max_length": 40}),
            ]},
            {"label": "CTA finale", "fields": [
                ("lavoro.cta_label",         {"label": "CTA finale · eyebrow", "type": "text", "max_length": 80}),
                ("lavoro.cta_heading",       {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
                ("lavoro.cta_intro",         {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
                ("lavoro.cta_primary",       {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("lavoro.cta_primary_href",  {"label": "CTA · destinazione", "type": "select",
                                                "choices": ["home", "studio", "lavoro", "processo", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "processo_page",
        "label": "Pagina Processo (novel kind)",
        "icon": "bi-list-ol",
        "region": ".ed-section",
        "page": "processo",
        "keywords": ["processo", "process", "fasi", "capabilities"],
        "help": "Pagina processo (novel `process` kind, dispatchato come stringa registro · nessun view layer custom): intestazione, intro processo, intro capabilities, label step.",
        "fields": [
            ("processo.eyebrow",                 {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("processo.headline",                {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("processo.intro",                   {"label": "Intro", "type": "textarea", "max_length": 700}),
            ("processo.process_label",           {"label": "Processo · eyebrow", "type": "text", "max_length": 80}),
            ("processo.process_heading",         {"label": "Processo · titolo", "type": "richtext", "max_length": 220}),
            ("processo.capabilities_label",      {"label": "Capabilities · eyebrow", "type": "text", "max_length": 80}),
            ("processo.capabilities_heading",    {"label": "Capabilities · titolo", "type": "richtext", "max_length": 220}),
            ("processo.capabilities_intro",      {"label": "Capabilities · intro", "type": "textarea", "max_length": 500}),
            ("processo.capability_duration_label",{"label": "Capability · etichetta Durata", "type": "text", "max_length": 40}),
            ("processo.step_index_prefix",       {"label": "Step · prefisso indice", "type": "text", "max_length": 8}),
            ("processo.step_index_separator",    {"label": "Step · separatore indice", "type": "text", "max_length": 4}),
            ("processo.step_sequence_label",     {"label": "Step · etichetta sequenza", "type": "text", "max_length": 40}),
            ("processo.cta_heading",             {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("processo.cta_intro",               {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("processo.cta_primary",             {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
            ("processo.cta_primary_href",        {"label": "CTA · destinazione", "type": "select",
                                                   "choices": ["home", "studio", "lavoro", "processo", "contatti"]}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-telephone",
        "region": ".ed-section",
        "page": "contatti",
        "keywords": ["contatti", "contact", "form", "canali", "studio", "indirizzo"],
        "help": "Pagina contatti: copy, label form (struttura form + upload restano registry-only), studio address block.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("contatti.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("contatti.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("contatti.intro",            {"label": "Intro", "type": "textarea", "max_length": 700}),
            ]},
            {"label": "Form · copy + submit", "fields": [
                ("contatti.form_label",       {"label": "Form · eyebrow", "type": "text", "max_length": 60}),
                ("contatti.form_heading",     {"label": "Form · titolo", "type": "richtext", "max_length": 220}),
                ("contatti.form_intro",       {"label": "Form · intro", "type": "textarea", "max_length": 500}),
                ("contatti.form_submit_label",{"label": "Form · CTA submit", "type": "text", "max_length": 60}),
                ("contatti.form_submit_note", {"label": "Form · nota submit", "type": "textarea", "max_length": 400}),
                ("contatti.form_consent",     {"label": "Form · testo consenso", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Channels · intestazione", "fields": [
                ("contatti.channels_label",   {"label": "Channels · eyebrow", "type": "text", "max_length": 60}),
            ]},
            {"label": "Studio address block", "fields": [
                ("contatti.studio_label",         {"label": "Studio · eyebrow", "type": "text", "max_length": 40}),
                ("contatti.studio_address",       {"label": "Studio · indirizzo", "type": "text", "max_length": 120}),
                ("contatti.studio_address_label", {"label": "Studio · etichetta indirizzo", "type": "text", "max_length": 40}),
                ("contatti.studio_area",          {"label": "Studio · area", "type": "text", "max_length": 120}),
                ("contatti.studio_area_label",    {"label": "Studio · etichetta area", "type": "text", "max_length": 40}),
                ("contatti.studio_metro",         {"label": "Studio · metro", "type": "text", "max_length": 100}),
                ("contatti.studio_metro_label",   {"label": "Studio · etichetta metro", "type": "text", "max_length": 40}),
                ("contatti.studio_hours",         {"label": "Studio · orari", "type": "text", "max_length": 120}),
                ("contatti.studio_hours_label",   {"label": "Studio · etichetta orari", "type": "text", "max_length": 40}),
            ]},
            {"label": "Footnote", "fields": [
                ("contatti.footnote",         {"label": "Footnote piè pagina", "type": "textarea", "max_length": 500}),
            ]},
        ],
    },
    {
        "id": "contact_info",
        "label": "Contatti · footer",
        "icon": "bi-telephone-forward",
        "region": ".ed-foot",
        "page": "*",
        "keywords": ["footer", "phone", "email", "indirizzo", "license", "clients"],
        "help": "Dati di contatto visibili in footer + intro voce dello studio + titoli sezioni footer.",
        "fields": [
            ("site.phone",         {"label": "Telefono", "type": "text", "max_length": 80}),
            ("site.email",         {"label": "Email", "type": "text", "max_length": 80}),
            ("site.address",       {"label": "Indirizzo sede primaria", "type": "text", "max_length": 160}),
            ("site.hours_compact", {"label": "Orari sintetici", "type": "text", "max_length": 120}),
            ("site.license",       {"label": "Licenza / P.IVA", "type": "text", "max_length": 200}),
            ("site.footer_intro",  {"label": "Intro footer", "type": "textarea", "max_length": 500}),
            ("site.foot_studio",   {"label": "Footer · titolo Studio", "type": "text", "max_length": 40}),
            ("site.foot_pages",    {"label": "Footer · titolo Pagine", "type": "text", "max_length": 40}),
            ("site.foot_contact",  {"label": "Footer · titolo Contatti", "type": "text", "max_length": 40}),
            ("site.foot_clients",  {"label": "Footer · titolo Clients", "type": "text", "max_length": 40}),
        ],
    },
]


# A.13b · Pixel cinematic-photographer — 10th enrolled editor archetype,
# second template of the portfolio family. **Closes the portfolio
# family** opened in A.13 with Chiara. Same staged dedicated-schema
# progression topology as real-estate (A.12+A.12b) · third family-
# closure via staged dedicated-schema after real-estate and the
# natural continuation of the pattern.
#
# Skin uses `.cp-*` selectors (chrome `.cp-nav`/`.cp-foot`, home
# sections `.cp-hero`/`.cp-cover`/`.cp-index-band`, page sections
# `.cp-essay`/`.cp-kit`/`.cp-awards`/`.cp-exhib`/`.cp-press`/
# `.cp-publications`/`.cp-contact-wrap`/`.cp-form` etc.) — distinct
# from Chiara `.ed-*` · no namespace collision with editor sidebar.
# 38 mature `html[dir="rtl"]` rules in `_base.html`.
#
# Shape contract notes (Step-0 audit verified):
#   • 5 pages: home / serie (NOVEL `series_list` kind) / biografia
#     (about) / pubblicazioni (NOVEL `publications` kind) / contatti.
#     5-locale parity PERFECT (154 keys × 5 locales, zero gaps).
#     Both novel page kinds are plain string identifiers in the
#     registry — no view layer dispatches on them.
#   • 1 SCALAR image field only: `home.hero_image` (top-level flat
#     path · same pattern as Pragma `home.hero_image` / Casa-level
#     scalar images). Total editable image surface: 1.
#   • `posts` list (3 series detail records) stays REGISTRY-ONLY —
#     DETAIL-PAGE EDITING IS OUT OF A.13b SCOPE per the consistent
#     perimeter policy applied to Lex `notabili` / Juris `insights`
#     / Casa `posts` / Villa `posts` / Chiara `posts`. A.13b is the
#     SIXTH uniform enforcement of this policy. The `posts[].cover_image`
#     image col is explicitly rejected by `validate_key_path` via the
#     complex-shape exclusion guardrail test — never reaches the editor.
#   • Complex shapes explicitly KEPT OUT of the perimeter:
#       - `serie.filters` (5 filter pills · flat list-of-str)
#       - `biografia.statement_paragraphs` (5 bio paragraphs · flat
#         list-of-str · could be exposed as scalar-kind indexed list
#         in a future coverage-expansion phase; kept OUT here to avoid
#         introducing the scalar-kind pattern as A.13b's only novelty)
#       - `site.kit_footer_rows` (3 footer kit rows · flat list-of-str)
#       - `contatti.form_fields` + `contatti.form_sections` + `contatti.upload_field`
#         (form structure blocks · same policy as every prior archetype)
#       - `posts` + all `posts[N].*` paths (per-series detail records)
#   • 10 readonly indexed lists (9 tuple + 1 dict) · no image cols
#     anywhere · no nested complexity. `home.filmstrip` exposes 4/5
#     tuple cols (slug stays registry-only as structural href).

PIXEL_CINEMATIC_PHOTOGRAPHER_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".cp-nav, .cp-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "fotografo", "tagline", "studio"],
        "help": "Nome fotografo/studio, iniziale crest, logo breve, tagline, CTA nav.",
        "fields": [
            ("site.logo_word",    {"label": "Nome fotografo / studio", "type": "text", "max_length": 60,
                                     "placeholder": "Lorenzo Bianchi"}),
            ("site.logo_initial", {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.logo_short",   {"label": "Logo · forma breve", "type": "text", "max_length": 8}),
            ("site.tag",          {"label": "Tagline (status badge nav)", "type": "text", "max_length": 120}),
            ("site.nav_cta",      {"label": "CTA nav", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".cp-hero, .cp-cover, .cp-hero-wrap",
        "page": "home",
        "keywords": ["hero", "cover", "headline", "eyebrow", "subhead", "cta", "counter", "pulse"],
        "help": "Primo scroll della home: cover image, eyebrow, headline, subhead, status pulse, CTA principali, counter serie.",
        "subgroups": [
            {"label": "Cover image", "fields": [
                ("home.hero_image",     {"label": "Hero image · URL", "type": "image", "max_length": 400}),
                ("home.hero_image_alt", {"label": "Hero image · alt text", "type": "text", "max_length": 200}),
            ]},
            {"label": "Hero copy", "fields": [
                ("home.eyebrow",           {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("home.headline",          {"label": "Headline", "type": "richtext", "max_length": 220,
                                              "help": "Consentiti i tag <em> per gli italici."}),
                ("home.subhead",           {"label": "Subhead", "type": "textarea", "max_length": 400}),
                ("home.status_pulse",      {"label": "Status pulse (status badge)", "type": "text", "max_length": 80}),
            ]},
            {"label": "Series counter", "fields": [
                ("home.series_counter_label", {"label": "Counter · label", "type": "text", "max_length": 40}),
                ("home.series_counter_value", {"label": "Counter · valore", "type": "text", "max_length": 40}),
            ]},
            {"label": "CTA hero", "fields": [
                ("home.primary_cta",     {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.primary_href",    {"label": "CTA primaria · destinazione", "type": "select",
                                            "choices": ["home", "serie", "biografia", "pubblicazioni", "contatti"]}),
                ("home.secondary_cta",   {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
                ("home.secondary_href",  {"label": "CTA secondaria · destinazione", "type": "select",
                                            "choices": ["home", "serie", "biografia", "pubblicazioni", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".cp-index-band, .cp-about-excerpt, .cp-publications, .cp-cta",
        "page": "home",
        "keywords": ["filmstrip", "about", "publications", "cta", "fasce"],
        "help": "Eyebrow, titoli, intro delle fasce home (filmstrip · about excerpt · publications · CTA finale).",
        "subgroups": [
            {"label": "Filmstrip · intestazione", "fields": [
                ("home.filmstrip_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.filmstrip_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.filmstrip_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "About excerpt", "fields": [
                ("home.about_label",     {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.about_heading",   {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.about_excerpt",   {"label": "Excerpt", "type": "textarea", "max_length": 500}),
                ("home.about_cta",       {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("home.about_cta_href",  {"label": "CTA · destinazione", "type": "select",
                                            "choices": ["home", "serie", "biografia", "pubblicazioni", "contatti"]}),
            ]},
            {"label": "Publications · intestazione", "fields": [
                ("home.publications_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.publications_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "CTA finale", "fields": [
                ("home.cta_label",          {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.cta_heading",        {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.cta_intro",          {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.cta_primary",        {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.cta_primary_href",   {"label": "CTA primaria · destinazione", "type": "select",
                                               "choices": ["home", "serie", "biografia", "pubblicazioni", "contatti"]}),
                ("home.cta_secondary",      {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
                ("home.cta_secondary_href", {"label": "CTA secondaria · destinazione", "type": "select",
                                               "choices": ["home", "serie", "biografia", "pubblicazioni", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "serie_page",
        "label": "Pagina Serie (series_list)",
        "icon": "bi-images",
        "region": ".cp-index-band, .cp-filter",
        "page": "serie",
        "keywords": ["serie", "series_list", "filters", "index", "card", "post labels"],
        "help": "Pagina elenco serie (novel `series_list` kind): intestazione, filter label, index, card meta labels per detail route. I 3 series detail records restano registry-only.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("serie.eyebrow",           {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("serie.headline",          {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("serie.subhead",           {"label": "Subhead", "type": "textarea", "max_length": 500}),
                ("serie.status_pulse",      {"label": "Status pulse", "type": "text", "max_length": 80}),
            ]},
            {"label": "Index + filter", "fields": [
                ("serie.index_label",       {"label": "Index · eyebrow", "type": "text", "max_length": 80}),
                ("serie.index_intro",       {"label": "Index · intro", "type": "textarea", "max_length": 400}),
                ("serie.filter_label",      {"label": "Filtro · etichetta", "type": "text", "max_length": 40}),
                ("serie.card_arrow_label",  {"label": "Card · etichetta freccia", "type": "text", "max_length": 40}),
            ]},
            {"label": "Post meta labels (detail card)", "fields": [
                ("serie.post_discipline_label", {"label": "Post · etichetta Disciplina", "type": "text", "max_length": 40}),
                ("serie.post_edition_label",    {"label": "Post · etichetta Edizione", "type": "text", "max_length": 40}),
                ("serie.post_frames_label",     {"label": "Post · etichetta Frame", "type": "text", "max_length": 40}),
                ("serie.post_gallery_label",    {"label": "Post · etichetta Gallery", "type": "text", "max_length": 40}),
                ("serie.post_location_label",   {"label": "Post · etichetta Location", "type": "text", "max_length": 40}),
                ("serie.post_period_label",     {"label": "Post · etichetta Periodo", "type": "text", "max_length": 40}),
            ]},
            {"label": "Series counter", "fields": [
                ("serie.series_counter_label",  {"label": "Counter · label", "type": "text", "max_length": 40}),
                ("serie.series_counter_value",  {"label": "Counter · valore", "type": "text", "max_length": 40}),
            ]},
            {"label": "CTA finale", "fields": [
                ("serie.cta_label",            {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("serie.cta_heading",          {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("serie.cta_intro",            {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("serie.cta_primary",          {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("serie.cta_primary_href",     {"label": "CTA · destinazione", "type": "select",
                                                  "choices": ["home", "serie", "biografia", "pubblicazioni", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "biografia_page",
        "label": "Pagina Biografia (about)",
        "icon": "bi-person",
        "region": ".cp-lead, .cp-essay, .cp-kit",
        "page": "biografia",
        "keywords": ["biografia", "about", "statement", "kit", "timeline"],
        "help": "Pagina biografia: intestazione, statement heading/label, kit heading/label + availability labels, timeline heading/label, series counter. I 5 statement_paragraphs restano registry-only (flat list-of-str exclusion).",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("biografia.eyebrow",      {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("biografia.headline",     {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("biografia.subhead",      {"label": "Subhead", "type": "textarea", "max_length": 500}),
                ("biografia.status_pulse", {"label": "Status pulse", "type": "text", "max_length": 80}),
            ]},
            {"label": "Statement", "fields": [
                ("biografia.statement_label",   {"label": "Statement · eyebrow", "type": "text", "max_length": 80}),
                ("biografia.statement_heading", {"label": "Statement · titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Kit + availability", "fields": [
                ("biografia.kit_label",              {"label": "Kit · eyebrow", "type": "text", "max_length": 80}),
                ("biografia.kit_heading",            {"label": "Kit · titolo", "type": "richtext", "max_length": 220}),
                ("biografia.kit_availability_label", {"label": "Kit · etichetta disponibilità", "type": "text", "max_length": 40}),
                ("biografia.kit_availability_value", {"label": "Kit · valore disponibilità", "type": "text", "max_length": 80}),
            ]},
            {"label": "Timeline", "fields": [
                ("biografia.timeline_label",   {"label": "Timeline · eyebrow", "type": "text", "max_length": 80}),
                ("biografia.timeline_heading", {"label": "Timeline · titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Series counter", "fields": [
                ("biografia.series_counter_label", {"label": "Counter · label", "type": "text", "max_length": 40}),
                ("biografia.series_counter_value", {"label": "Counter · valore", "type": "text", "max_length": 40}),
            ]},
            {"label": "CTA finale", "fields": [
                ("biografia.cta_heading",      {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
                ("biografia.cta_intro",        {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
                ("biografia.cta_primary",      {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("biografia.cta_primary_href", {"label": "CTA · destinazione", "type": "select",
                                                  "choices": ["home", "serie", "biografia", "pubblicazioni", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "pubblicazioni_page",
        "label": "Pagina Pubblicazioni (publications)",
        "icon": "bi-journal-richtext",
        "region": ".cp-press, .cp-exhib, .cp-awards",
        "page": "pubblicazioni",
        "keywords": ["pubblicazioni", "publications", "press", "exhibitions", "awards"],
        "help": "Pagina pubblicazioni (novel `publications` kind): intestazione, intro press/exhibitions/awards, series counter, CTA finale.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("pubblicazioni.eyebrow",      {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("pubblicazioni.headline",     {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("pubblicazioni.subhead",      {"label": "Subhead", "type": "textarea", "max_length": 500}),
                ("pubblicazioni.status_pulse", {"label": "Status pulse", "type": "text", "max_length": 80}),
            ]},
            {"label": "Press · intestazione", "fields": [
                ("pubblicazioni.press_label",   {"label": "Press · eyebrow", "type": "text", "max_length": 80}),
                ("pubblicazioni.press_heading", {"label": "Press · titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Exhibitions · intestazione", "fields": [
                ("pubblicazioni.exhibitions_label",   {"label": "Exhibitions · eyebrow", "type": "text", "max_length": 80}),
                ("pubblicazioni.exhibitions_heading", {"label": "Exhibitions · titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Awards · intestazione", "fields": [
                ("pubblicazioni.awards_label",   {"label": "Awards · eyebrow", "type": "text", "max_length": 80}),
                ("pubblicazioni.awards_heading", {"label": "Awards · titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Series counter", "fields": [
                ("pubblicazioni.series_counter_label", {"label": "Counter · label", "type": "text", "max_length": 40}),
                ("pubblicazioni.series_counter_value", {"label": "Counter · valore", "type": "text", "max_length": 40}),
            ]},
            {"label": "CTA finale", "fields": [
                ("pubblicazioni.cta_heading",      {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
                ("pubblicazioni.cta_intro",        {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
                ("pubblicazioni.cta_primary",      {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("pubblicazioni.cta_primary_href", {"label": "CTA · destinazione", "type": "select",
                                                     "choices": ["home", "serie", "biografia", "pubblicazioni", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-telephone",
        "region": ".cp-contact-wrap, .cp-form",
        "page": "contatti",
        "keywords": ["contatti", "contact", "form", "studio", "channels"],
        "help": "Pagina contatti: copy, label form (struttura form + upload restano registry-only), studio address block + row labels, channels eyebrow, footnote.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("contatti.eyebrow",      {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("contatti.headline",     {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("contatti.subhead",      {"label": "Subhead", "type": "textarea", "max_length": 500}),
                ("contatti.status_pulse", {"label": "Status pulse", "type": "text", "max_length": 80}),
            ]},
            {"label": "Form · copy + submit", "fields": [
                ("contatti.form_label",       {"label": "Form · eyebrow", "type": "text", "max_length": 60}),
                ("contatti.form_heading",     {"label": "Form · titolo", "type": "richtext", "max_length": 220}),
                ("contatti.form_intro",       {"label": "Form · intro", "type": "textarea", "max_length": 500}),
                ("contatti.form_submit_label",{"label": "Form · CTA submit", "type": "text", "max_length": 60}),
                ("contatti.form_submit_note", {"label": "Form · nota submit", "type": "textarea", "max_length": 400}),
                ("contatti.form_consent",     {"label": "Form · testo consenso", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Channels · intestazione", "fields": [
                ("contatti.channels_label", {"label": "Channels · eyebrow", "type": "text", "max_length": 60}),
            ]},
            {"label": "Studio address block", "fields": [
                ("contatti.studio_label",         {"label": "Studio · eyebrow", "type": "text", "max_length": 40}),
                ("contatti.studio_address",       {"label": "Studio · indirizzo", "type": "text", "max_length": 120}),
                ("contatti.studio_area",          {"label": "Studio · area", "type": "text", "max_length": 120}),
                ("contatti.studio_metro",         {"label": "Studio · metro", "type": "text", "max_length": 100}),
                ("contatti.studio_hours",         {"label": "Studio · orari", "type": "text", "max_length": 120}),
                ("contatti.studio_row_address_label",  {"label": "Studio row · etichetta indirizzo", "type": "text", "max_length": 40}),
                ("contatti.studio_row_entrance_label", {"label": "Studio row · etichetta entrata", "type": "text", "max_length": 40}),
                ("contatti.studio_row_metro_label",    {"label": "Studio row · etichetta metro", "type": "text", "max_length": 40}),
                ("contatti.studio_row_hours_label",    {"label": "Studio row · etichetta orari", "type": "text", "max_length": 40}),
            ]},
            {"label": "Series counter", "fields": [
                ("contatti.series_counter_label", {"label": "Counter · label", "type": "text", "max_length": 40}),
                ("contatti.series_counter_value", {"label": "Counter · valore", "type": "text", "max_length": 40}),
            ]},
            {"label": "Footnote", "fields": [
                ("contatti.footnote", {"label": "Footnote piè pagina", "type": "textarea", "max_length": 500}),
            ]},
        ],
    },
    {
        "id": "contact_info",
        "label": "Contatti · footer",
        "icon": "bi-telephone-forward",
        "region": ".cp-foot",
        "page": "*",
        "keywords": ["footer", "phone", "email", "indirizzo", "license", "exif"],
        "help": "Dati di contatto visibili in footer + intro voce + titoli sezioni footer (studio/pages/contact/kit).",
        "fields": [
            ("site.phone",         {"label": "Telefono", "type": "text", "max_length": 80}),
            ("site.email",         {"label": "Email", "type": "text", "max_length": 80}),
            ("site.address",       {"label": "Indirizzo sede primaria", "type": "text", "max_length": 160}),
            ("site.hours_compact", {"label": "Orari sintetici", "type": "text", "max_length": 120}),
            ("site.license",       {"label": "Licenza / P.IVA", "type": "text", "max_length": 200}),
            ("site.footer_intro",  {"label": "Intro footer", "type": "textarea", "max_length": 500}),
            ("site.foot_studio",   {"label": "Footer · titolo Studio", "type": "text", "max_length": 40}),
            ("site.foot_pages",    {"label": "Footer · titolo Pagine", "type": "text", "max_length": 40}),
            ("site.foot_contact",  {"label": "Footer · titolo Contatti", "type": "text", "max_length": 40}),
            ("site.foot_kit",      {"label": "Footer · titolo Kit", "type": "text", "max_length": 40}),
        ],
    },
]


# A.14 · Sapore trattoria-warm — 11th enrolled editor archetype, first
# template of the restaurant-continuation family. OPENS the family via
# staged dedicated-schema progression (mirror of real-estate A.12+A.12b
# and portfolio A.13+A.13b). Brace (street-modern) stays OUT until
# A.14b. Distinct archetype from Brace: distinct skin folders
# (restaurant/trattoria-warm/ with `.tw-*` prefix vs restaurant/street-
# modern/ with `.sm-*`), 50% page-slug overlap (home/menu/contatti
# shared; storia/forno/eventi Sapore vs lab/moments/ordina Brace),
# fundamentally different menu shape (Sapore nested tuple vs Brace
# nested dict-with-image-col), image surface ratio 1:3.5 — shared-schema
# (A.9 recipe) is IMPOSSIBLE.
#
# Skin uses `.tw-*` selectors (chrome `.tw-nav`/`.tw-foot`, pages
# `.tw-hero`/`.tw-forno`/`.tw-storia`/`.tw-eventi`/`.tw-contact` etc.).
# 18 mature `html[dir="rtl"]` rules in `_base.html` — RTL validated
# since Session 48 D-078 Sapore rollout.
#
# Shape contract notes (Step-0 audit verified):
#   • 6 pages: home · menu · storia (about) · forno (signature · NOVEL
#     kind) · eventi (events · NOVEL kind) · contatti. 5-locale parity
#     PERFECT (224 keys × 5 locales, zero gaps).
#   • 7 SCALAR image fields (home.hero_image, home.forno_image,
#     home.tavolata_image, storia.photo_image, forno.forno_story_image,
#     forno.dough_image, eventi.birthday_image). Plus 2 image-in-dict-row
#     lists (home.family[].portrait × 3 rows + storia.family[].portrait
#     × 3 rows = 6 image cells). Total editable image surface: 13
#     (7 scalar + 6 cells). Image-in-dict-row precedent: Vertex A.3a/A.4
#     (shallow dict-list pattern) — no new infrastructure required.
#   • `posts` list is EMPTY in the content registry — Sapore ships no
#     blog posts. First enrollment since A.10 without a posts list.
#     Consequence: NO `posts.*` paths in the complex-shape exclusion
#     guardrail (there's nothing to reject). Detail-page registry-only
#     policy doesn't apply — the absence is structural, not a perimeter
#     decision.
#   • Menu rows are KEPT INSIDE the perimeter as deep-path tuple cells.
#     `menu.sections` is a list-of-dict (5 sections) with cols
#     (heading/label) exposed + `dishes` col EXCLUDED at the parent
#     level. Each section's dishes (tuple 7×3: name/desc/price) are
#     instead registered as 5 separate STRUCTURED_FIELD_SHAPES entries
#     at deep paths `menu.sections.0.dishes` through `menu.sections.4.dishes`
#     — each tuple 7×3. Shape is novel (nested tuple inside a dict-list
#     parent) but requires no new infrastructure because `_resolve_path`
#     walks arbitrary-depth dotted paths. Without menu rows in perimeter
#     the enrollment would be fake-editable (menu is the editorial heart
#     of the template).
#   • Complex shapes explicitly KEPT OUT of the perimeter:
#       - `storia.story` (4 bio paragraphs · flat list-of-str · same
#         category as Pixel `biografia.statement_paragraphs`)
#       - `contatti.form_sections` + `contatti.form_fields` (form
#         structure blocks · same policy as every prior archetype with a
#         contact form)
#       - `contatti.occasion_options` (7 option strings for form select
#         · flat list-of-str)
#       - `site.hours_footer_rows` (2 hours rows · flat list-of-str)
#       - `pages` (top-level navigation index · always out)
#   • Zero mutable repeater — all 20 indexed lists stay readonly (cell-
#     level edit only, no add/remove). Repeater-mutable family remains
#     out-of-scope per D-098.
#   • 20 readonly indexed list entries in STRUCTURED_FIELD_SHAPES
#     (15 base lists + 5 menu.sections.{0..4}.dishes deep paths).
#     home.family + storia.family carry the `portrait` image col
#     (image-in-dict-row precedent — Vertex A.3a/A.4 infra).

SAPORE_TRATTORIA_WARM_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".tw-nav, .tw-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "trattoria", "tagline", "chrome"],
        "help": "Nome trattoria, iniziale crest, tagline, contatti sintetici, chrome footer, CTA di navigazione.",
        "fields": [
            ("site.logo_word",        {"label": "Nome trattoria", "type": "text", "max_length": 60,
                                         "placeholder": "Trattoria Da Nonna Rosa"}),
            ("site.logo_initial",     {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.tag",              {"label": "Tagline (strip superiore nav)", "type": "text", "max_length": 160}),
            ("site.phone",            {"label": "Telefono (display)", "type": "text", "max_length": 40}),
            ("site.phone_tel",        {"label": "Telefono (tel: href)", "type": "text", "max_length": 40}),
            ("site.whatsapp",         {"label": "WhatsApp (display)", "type": "text", "max_length": 40}),
            ("site.whatsapp_link",    {"label": "WhatsApp · URL completo", "type": "url", "max_length": 300}),
            ("site.email",            {"label": "Email", "type": "text", "max_length": 120}),
            ("site.address",          {"label": "Indirizzo (una riga)", "type": "text", "max_length": 200}),
            ("site.hours_compact",    {"label": "Orari sintetici (strip nav)", "type": "text", "max_length": 160}),
            ("site.license",          {"label": "Licenza / P.IVA", "type": "text", "max_length": 200}),
            ("site.footer_intro",     {"label": "Intro footer", "type": "textarea", "max_length": 500}),
            ("site.nav_cta",          {"label": "CTA nav · etichetta", "type": "text", "max_length": 60}),
            ("site.nav_cta_href",     {"label": "CTA nav · destinazione", "type": "select",
                                         "choices": ["home", "menu", "storia", "forno", "eventi", "contatti"]}),
            ("site.nav_phone_cta",    {"label": "CTA nav · telefono", "type": "text", "max_length": 80}),
            ("site.star_line",        {"label": "Nav · strip stellina", "type": "text", "max_length": 120}),
            ("site.copyright",        {"label": "Footer · copyright", "type": "text", "max_length": 200}),
            ("site.footer_hours_1",   {"label": "Footer · riga orari 1", "type": "text", "max_length": 120}),
            ("site.footer_hours_2",   {"label": "Footer · riga orari 2", "type": "text", "max_length": 120}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".tw-hero",
        "page": "home",
        "keywords": ["hero", "headline", "eyebrow", "intro", "cta", "stamp"],
        "help": "Primo scroll della home: hero image, eyebrow, headline, intro, stamp, CTA principali.",
        "subgroups": [
            {"label": "Cover image", "fields": [
                ("home.hero_image",    {"label": "Hero image · URL", "type": "image", "max_length": 400}),
                ("home.hero_caption",  {"label": "Hero image · didascalia", "type": "text", "max_length": 200}),
                ("home.hero_stamp",    {"label": "Hero stamp (dal 1987)", "type": "text", "max_length": 40}),
            ]},
            {"label": "Hero copy", "fields": [
                ("home.eyebrow",       {"label": "Eyebrow", "type": "text", "max_length": 160}),
                ("home.headline",      {"label": "Headline", "type": "richtext", "max_length": 220,
                                          "help": "Consentiti i tag <em> per italici."}),
                ("home.intro",         {"label": "Intro (paragrafo sotto headline)", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "CTA hero", "fields": [
                ("home.primary_cta",   {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.primary_href",  {"label": "CTA primaria · destinazione", "type": "select",
                                          "choices": ["home", "menu", "storia", "forno", "eventi", "contatti"]}),
                ("home.secondary_cta", {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
            ]},
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".tw-chalkboard, .tw-family, .tw-forno-band, .tw-reviews, .tw-hours, .tw-tavolata, .tw-home-cta",
        "page": "home",
        "keywords": ["chalkboard", "famiglia", "forno", "reviews", "hours", "tavolata", "cta"],
        "help": "Fasce copy della home: lavagna della settimana, famiglia, forno band, reviews, orari, tavolata, CTA finale.",
        "subgroups": [
            {"label": "Lavagna della settimana", "fields": [
                ("home.chalkboard_label",       {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.chalkboard_heading",     {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.chalkboard_intro",       {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.chalkboard_buongiorno",  {"label": "Frase di chiusura", "type": "text", "max_length": 80}),
            ]},
            {"label": "Famiglia · intestazione", "fields": [
                ("home.family_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.family_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Forno band", "fields": [
                ("home.forno_label",     {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.forno_heading",   {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.forno_text",      {"label": "Paragrafo", "type": "textarea", "max_length": 700}),
                ("home.forno_image",     {"label": "Forno · immagine URL", "type": "image", "max_length": 400}),
                ("home.forno_caption",   {"label": "Forno · didascalia", "type": "text", "max_length": 200}),
                ("home.forno_cta",       {"label": "Forno CTA · etichetta", "type": "text", "max_length": 60}),
                ("home.forno_cta_href",  {"label": "Forno CTA · destinazione", "type": "select",
                                            "choices": ["home", "menu", "storia", "forno", "eventi", "contatti"]}),
            ]},
            {"label": "Reviews · intestazione", "fields": [
                ("home.reviews_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
            ]},
            {"label": "Orari · intestazione", "fields": [
                ("home.hours_label",     {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.hours_note",      {"label": "Nota orari (sotto la tabella)", "type": "text", "max_length": 200}),
            ]},
            {"label": "Tavolata band", "fields": [
                ("home.tavolata_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.tavolata_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.tavolata_text",     {"label": "Paragrafo", "type": "textarea", "max_length": 700}),
                ("home.tavolata_cta",      {"label": "Tavolata CTA · etichetta", "type": "text", "max_length": 60}),
                ("home.tavolata_cta_href", {"label": "Tavolata CTA · destinazione", "type": "select",
                                              "choices": ["home", "menu", "storia", "forno", "eventi", "contatti"]}),
                ("home.tavolata_image",    {"label": "Tavolata · immagine URL", "type": "image", "max_length": 400}),
            ]},
            {"label": "CTA finale", "fields": [
                ("home.cta_label",         {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.cta_heading",       {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.cta_intro",         {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.cta_primary",       {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.cta_primary_href",  {"label": "CTA primaria · destinazione", "type": "select",
                                              "choices": ["home", "menu", "storia", "forno", "eventi", "contatti"]}),
                ("home.cta_secondary",     {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
            ]},
        ],
    },
    {
        "id": "menu_page",
        "label": "Pagina Menu",
        "icon": "bi-journal-text",
        "region": ".tw-menu, .tw-menu-hero, .tw-wine-house",
        "page": "menu",
        "keywords": ["menu", "piatti", "vino", "allergeni"],
        "help": "Intestazione pagina menu, vino della casa, nota allergeni. Le sezioni del menu e i piatti si modificano dai gruppi indexed `Menu · Sections` e `Menu · Sezione N · Piatti`.",
        "fields": [
            ("menu.eyebrow",             {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("menu.headline",            {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("menu.intro",               {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("menu.wine_house_label",    {"label": "Vino della casa · eyebrow", "type": "text", "max_length": 80}),
            ("menu.wine_house_heading",  {"label": "Vino della casa · titolo", "type": "richtext", "max_length": 220}),
            ("menu.wine_house_text",     {"label": "Vino della casa · paragrafo", "type": "textarea", "max_length": 600}),
            ("menu.allergen_note",       {"label": "Nota allergeni", "type": "textarea", "max_length": 400}),
        ],
    },
    {
        "id": "storia_page",
        "label": "Pagina Storia (about)",
        "icon": "bi-book",
        "region": ".tw-storia, .tw-storia-hero, .tw-timeline, .tw-values, .tw-storia-photo",
        "page": "storia",
        "keywords": ["storia", "about", "timeline", "valori", "rosa"],
        "help": "Intestazione pagina storia, etichette famiglia/timeline/valori, foto in fondo. I paragrafi del racconto (`storia.story`) restano registry-only.",
        "fields": [
            ("storia.eyebrow",         {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("storia.headline",        {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("storia.intro",           {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("storia.timeline_label",  {"label": "Timeline · eyebrow", "type": "text", "max_length": 80}),
            ("storia.family_label",    {"label": "Famiglia · eyebrow", "type": "text", "max_length": 80}),
            ("storia.values_label",    {"label": "Valori · eyebrow", "type": "text", "max_length": 80}),
            ("storia.values_heading",  {"label": "Valori · titolo", "type": "richtext", "max_length": 220}),
            ("storia.photo_image",     {"label": "Foto in fondo · URL", "type": "image", "max_length": 400}),
            ("storia.photo_caption",   {"label": "Foto in fondo · didascalia", "type": "text", "max_length": 200}),
        ],
    },
    {
        "id": "forno_page",
        "label": "Pagina Forno (signature)",
        "icon": "bi-fire",
        "region": ".tw-forno, .tw-forno-hero, .tw-pizza-signatures, .tw-pasta-signatures, .tw-forno-story, .tw-producers",
        "page": "forno",
        "keywords": ["forno", "pizza", "pasta", "signature", "produttori", "dough"],
        "help": "Pagina pizza & pasta: hero, signature di pizza e pasta, storia del forno, produttori, foto dough. Le liste dei piatti signature e dei produttori si modificano dai gruppi indexed.",
        "fields": [
            ("forno.eyebrow",              {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("forno.headline",             {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("forno.intro",                {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("forno.pizza_label",          {"label": "Pizza signatures · eyebrow", "type": "text", "max_length": 80}),
            ("forno.pizza_heading",        {"label": "Pizza signatures · titolo", "type": "richtext", "max_length": 220}),
            ("forno.pizza_intro",          {"label": "Pizza signatures · intro", "type": "textarea", "max_length": 500}),
            ("forno.pasta_label",          {"label": "Pasta signatures · eyebrow", "type": "text", "max_length": 80}),
            ("forno.pasta_heading",        {"label": "Pasta signatures · titolo", "type": "richtext", "max_length": 220}),
            ("forno.pasta_intro",          {"label": "Pasta signatures · intro", "type": "textarea", "max_length": 500}),
            ("forno.forno_story_label",    {"label": "Story forno · eyebrow", "type": "text", "max_length": 80}),
            ("forno.forno_story_heading",  {"label": "Story forno · titolo", "type": "richtext", "max_length": 220}),
            ("forno.forno_story_text_1",   {"label": "Story forno · paragrafo 1", "type": "textarea", "max_length": 600}),
            ("forno.forno_story_text_2",   {"label": "Story forno · paragrafo 2", "type": "textarea", "max_length": 600}),
            ("forno.forno_story_image",    {"label": "Story forno · immagine URL", "type": "image", "max_length": 400}),
            ("forno.forno_story_caption",  {"label": "Story forno · didascalia", "type": "text", "max_length": 200}),
            ("forno.producers_label",      {"label": "Producers · eyebrow", "type": "text", "max_length": 80}),
            ("forno.producers_heading",    {"label": "Producers · titolo", "type": "richtext", "max_length": 220}),
            ("forno.dough_image",          {"label": "Dough · immagine URL", "type": "image", "max_length": 400}),
            ("forno.dough_caption",        {"label": "Dough · didascalia", "type": "text", "max_length": 200}),
        ],
    },
    {
        "id": "eventi_page",
        "label": "Pagina Eventi",
        "icon": "bi-calendar-heart",
        "region": ".tw-eventi, .tw-eventi-hero, .tw-birthday, .tw-eventi-contact",
        "page": "eventi",
        "keywords": ["eventi", "tavolate", "compleanni", "anniversari"],
        "help": "Pagina tavolate & eventi: hero, compleanni/anniversari, contact block. Le formule esperienza si modificano dal gruppo indexed `Eventi · Experiences`.",
        "fields": [
            ("eventi.eyebrow",            {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("eventi.headline",           {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("eventi.intro",              {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("eventi.experiences_label",  {"label": "Formule · eyebrow", "type": "text", "max_length": 80}),
            ("eventi.meta_menu_label",    {"label": "Meta · etichetta Menu (dentro le formule)", "type": "text", "max_length": 40}),
            ("eventi.meta_wine_label",    {"label": "Meta · etichetta Vini (dentro le formule)", "type": "text", "max_length": 40}),
            ("eventi.birthday_label",     {"label": "Compleanni · eyebrow", "type": "text", "max_length": 80}),
            ("eventi.birthday_heading",   {"label": "Compleanni · titolo", "type": "richtext", "max_length": 220}),
            ("eventi.birthday_text",      {"label": "Compleanni · paragrafo", "type": "textarea", "max_length": 600}),
            ("eventi.birthday_image",     {"label": "Compleanni · immagine URL", "type": "image", "max_length": 400}),
            ("eventi.birthday_caption",   {"label": "Compleanni · didascalia", "type": "text", "max_length": 200}),
            ("eventi.contact_label",      {"label": "Contact block · eyebrow", "type": "text", "max_length": 80}),
            ("eventi.contact_heading",    {"label": "Contact block · titolo", "type": "richtext", "max_length": 220}),
            ("eventi.contact_text",       {"label": "Contact block · paragrafo", "type": "textarea", "max_length": 500}),
            ("eventi.contact_phone",      {"label": "Contact block · telefono", "type": "text", "max_length": 40}),
            ("eventi.contact_whatsapp",   {"label": "Contact block · whatsapp", "type": "text", "max_length": 40}),
            ("eventi.contact_email",      {"label": "Contact block · email", "type": "text", "max_length": 120}),
            ("eventi.contact_cta",        {"label": "Contact block · CTA · etichetta", "type": "text", "max_length": 60}),
            ("eventi.contact_cta_href",   {"label": "Contact block · CTA · destinazione", "type": "select",
                                             "choices": ["home", "menu", "storia", "forno", "eventi", "contatti"]}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-geo-alt",
        "region": ".tw-contact, .tw-contact-hero, .tw-map, .tw-transport",
        "page": "contatti",
        "keywords": ["contatti", "indirizzo", "orari", "mappa", "trasporti"],
        "help": "Pagina trovaci & prenota: indirizzo, orari, contatti, form labels, mappa, trasporti. La struttura form (`form_sections`/`form_fields`/`occasion_options`) resta registry-only.",
        "fields": [
            ("contatti.eyebrow",                   {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("contatti.headline",                  {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("contatti.intro",                     {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("contatti.address_label",             {"label": "Indirizzo · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.address_heading",           {"label": "Indirizzo · titolo", "type": "text", "max_length": 120}),
            ("contatti.address_text",              {"label": "Indirizzo · paragrafo", "type": "textarea", "max_length": 500}),
            ("contatti.address_city",              {"label": "Indirizzo · città + quartiere", "type": "text", "max_length": 120}),
            ("contatti.hours_label",               {"label": "Orari · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.hours_heading",             {"label": "Orari · titolo", "type": "richtext", "max_length": 220}),
            ("contatti.contact_label",             {"label": "Parla con noi · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.contact_heading",           {"label": "Parla con noi · titolo", "type": "richtext", "max_length": 220}),
            ("contatti.contact_phone_label",       {"label": "Phone · etichetta", "type": "text", "max_length": 60}),
            ("contatti.contact_phone_value",       {"label": "Phone · valore", "type": "text", "max_length": 40}),
            ("contatti.contact_phone_hours",       {"label": "Phone · nota", "type": "text", "max_length": 120}),
            ("contatti.contact_whatsapp_label",    {"label": "Whatsapp · etichetta", "type": "text", "max_length": 60}),
            ("contatti.contact_whatsapp_value",    {"label": "Whatsapp · valore", "type": "text", "max_length": 40}),
            ("contatti.contact_whatsapp_hours",    {"label": "Whatsapp · nota", "type": "text", "max_length": 120}),
            ("contatti.contact_email_label",       {"label": "Email · etichetta", "type": "text", "max_length": 60}),
            ("contatti.contact_email_value",       {"label": "Email · valore", "type": "text", "max_length": 120}),
            ("contatti.contact_email_hours",       {"label": "Email · nota", "type": "text", "max_length": 120}),
            ("contatti.form_label",                {"label": "Form · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.form_heading",              {"label": "Form · titolo", "type": "richtext", "max_length": 220}),
            ("contatti.form_intro",                {"label": "Form · intro", "type": "textarea", "max_length": 500}),
            ("contatti.consent",                   {"label": "Form · consenso (stringa sotto i field)", "type": "textarea", "max_length": 400}),
            ("contatti.form_submit",               {"label": "Form · CTA submit", "type": "text", "max_length": 60}),
            ("contatti.form_submit_note",          {"label": "Form · nota post-submit", "type": "text", "max_length": 200}),
            ("contatti.map_label",                 {"label": "Map · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.map_heading",               {"label": "Map · titolo", "type": "text", "max_length": 160}),
            ("contatti.map_link",                  {"label": "Map · CTA esterno (label)", "type": "text", "max_length": 80}),
            ("contatti.transport_label",           {"label": "Trasporti · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.transport_heading",         {"label": "Trasporti · titolo", "type": "richtext", "max_length": 220}),
        ],
    },
]


# A.14b · Brace street-modern — 12th enrolled editor archetype, second
# template of the restaurant-continuation family. **Closes the
# restaurant-continuation family** opened in A.14 with Sapore. Same
# staged dedicated-schema progression topology as real-estate
# (A.12+A.12b) and portfolio (A.13+A.13b) — third staged closure.
#
# Skin uses `.sm-*` selectors (chrome `.sm-nav`/`.sm-foot`, pages
# `.sm-hero`/`.sm-menu`/`.sm-lab`/`.sm-moments`/`.sm-ordina`/
# `.sm-contact` etc.). 24 mature `html[dir="rtl"]` rules in
# `_base.html` since D-078 Brace rollout.
#
# Shape contract notes (Step-0 audit verified):
#   • 6 pages: home · menu · lab (about) · moments (gallery) · ordina
#     (**novel `order` kind**) · contatti. 5-locale parity PERFECT
#     (273 keys × 5 locales, zero gaps).
#   • 3 SCALAR image fields (home.hero_image, lab.hero_image,
#     moments.featured_image) + 41 image cells across 6 image-in-dict-
#     row lists: home.menu_strip_items[].image × 6, home.crew[].portrait
#     × 3, home.atmo_strip[].image × 3, lab.crew[].portrait × 4,
#     moments.grid[].image × 6, **menu.sections.{0..4}.items[].image
#     × 19 (deep-path 2-level · Chiara precedent mechanical reuse)**.
#     Total editable image surface: 44 (3 scalar + 41 cells · 3.4×
#     Sapore, 2.4× Villa).
#   • Menu rows stay INSIDE perimeter via 5 deep-path shape entries
#     `menu.sections.{i}.items` · shape identical to Chiara
#     `home.featured_works.items` (dict-in-dict-list parent) — same
#     depth, same infra. **Tag col IN** (Step-0 audit: 'TOP'/'NEW'/
#     'VEG' editorial badges visible, not structural).
#   • **Ordina routes nested lines stay INSIDE perimeter** via 3
#     deep-path shape entries `ordina.routes.{i}.lines` · shape
#     identical to Sapore `menu.sections.{i}.dishes` (tuple-in-dict-list
#     parent) — same infra via commit f66ac24. **Correzione ipotesi
#     Step-0 audit**: initial hypothesis was "OUT default unless audit
#     proves editorial value"; audit demonstrated strong editorial
#     value (address/phone/delivery partners values · customer would
#     absolutely change them). IN.
#   • `posts` list EMPTY (same as Sapore · structural absence · detail-
#     page policy stays at 6-archetype uniform enforcement: Lex/Juris/
#     Casa/Villa/Chiara/Pixel).
#   • **No form structures** — Brace ships NO `contatti.form_sections`/
#     `form_fields` list structures; only scalar form labels. Smaller
#     out-policy set than Sapore.
#   • Complex shapes explicitly KEPT OUT of the perimeter:
#       - `site.hours_footer_rows` (2 rows · flat list-of-str)
#       - `home.manifesto_paragraphs` (3 paragraphs · flat list-of-str)
#       - `moments.categories` (6 filter pills · flat list-of-str)
#       - `pages` (top-level navigation index)
#   • Col-level exclusions (structural identifiers / routing flags):
#       - `menu.sections[].id` (section slug like 'burger'/'fritti')
#       - `moments.grid[].filename` (structural ID like 'MO-001')
#       - `ordina.routes[].id` + `ordina.routes[].cta_kind` (structural)
#       - `contatti.channels[].icon` + `contatti.channels[].kind`
#   • Zero mutable repeater · zero image per-locale · pure enrollment.
#   • 30 readonly indexed list entries in STRUCTURED_FIELD_SHAPES
#     (22 parent + 5 menu.sections.{i}.items + 3 ordina.routes.{i}.lines).

BRACE_STREET_MODERN_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".sm-nav, .sm-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "brace", "tagline", "chrome", "social"],
        "help": "Nome lab, iniziale crest, contatti sintetici, chrome footer, social handles, CTA navigazione.",
        "fields": [
            ("site.logo_word",        {"label": "Nome lab", "type": "text", "max_length": 60,
                                         "placeholder": "BRACE STREET LAB"}),
            ("site.logo_initial",     {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.tag",              {"label": "Tagline (strip superiore nav)", "type": "text", "max_length": 160}),
            ("site.phone",            {"label": "Telefono (display breve)", "type": "text", "max_length": 40}),
            ("site.phone_tel",        {"label": "Telefono (tel: href)", "type": "text", "max_length": 40}),
            ("site.phone_display",    {"label": "Telefono (display esteso)", "type": "text", "max_length": 40}),
            ("site.whatsapp",         {"label": "WhatsApp (display)", "type": "text", "max_length": 40}),
            ("site.whatsapp_link",    {"label": "WhatsApp · URL completo", "type": "url", "max_length": 300}),
            ("site.email",            {"label": "Email", "type": "text", "max_length": 120}),
            ("site.address",          {"label": "Indirizzo (una riga)", "type": "text", "max_length": 200}),
            ("site.hours_compact",    {"label": "Orari sintetici (strip nav)", "type": "text", "max_length": 200}),
            ("site.license",          {"label": "Licenza / P.IVA", "type": "text", "max_length": 200}),
            ("site.footer_intro",     {"label": "Intro footer", "type": "textarea", "max_length": 500}),
            ("site.nav_cta",          {"label": "CTA nav · etichetta", "type": "text", "max_length": 60}),
            ("site.nav_cta_href",     {"label": "CTA nav · destinazione", "type": "select",
                                         "choices": ["home", "menu", "lab", "moments", "ordina", "contatti"]}),
            ("site.nav_phone_cta",    {"label": "CTA nav · telefono", "type": "text", "max_length": 80}),
            ("site.star_line",        {"label": "Nav · strip stellina", "type": "text", "max_length": 120}),
            ("site.copyright",        {"label": "Footer · copyright", "type": "text", "max_length": 200}),
            ("site.footer_hours_1",   {"label": "Footer · riga orari 1", "type": "text", "max_length": 120}),
            ("site.footer_hours_2",   {"label": "Footer · riga orari 2", "type": "text", "max_length": 120}),
            ("site.instagram_handle", {"label": "Instagram · handle", "type": "text", "max_length": 40}),
            ("site.instagram_link",   {"label": "Instagram · URL", "type": "url", "max_length": 300}),
            ("site.tiktok_handle",    {"label": "TikTok · handle", "type": "text", "max_length": 40}),
            ("site.tiktok_link",      {"label": "TikTok · URL", "type": "url", "max_length": 300}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".sm-hero",
        "page": "home",
        "keywords": ["hero", "headline", "eyebrow", "intro", "badge", "counter", "cta"],
        "help": "Primo scroll della home: hero image, eyebrow, headline, intro, badge prezzo, counter stato banco, CTA.",
        "subgroups": [
            {"label": "Cover image", "fields": [
                ("home.hero_image", {"label": "Hero image · URL", "type": "image", "max_length": 400}),
                ("home.hero_alt",   {"label": "Hero image · alt text", "type": "text", "max_length": 200}),
            ]},
            {"label": "Hero copy", "fields": [
                ("home.eyebrow",  {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("home.headline", {"label": "Headline", "type": "richtext", "max_length": 220,
                                     "help": "Consentiti i tag <em> per italici."}),
                ("home.intro",    {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Hero badge (piatto in vetrina)", "fields": [
                ("home.hero_badge_price", {"label": "Badge · prezzo", "type": "text", "max_length": 40}),
                ("home.hero_badge_label", {"label": "Badge · nome piatto", "type": "text", "max_length": 80}),
                ("home.hero_badge_tag",   {"label": "Badge · tag", "type": "text", "max_length": 40}),
            ]},
            {"label": "Counter stato banco", "fields": [
                ("home.counter_label",         {"label": "Counter · etichetta coda", "type": "text", "max_length": 60}),
                ("home.counter_value",         {"label": "Counter · valore coda", "type": "text", "max_length": 40}),
                ("home.counter_kitchen_label", {"label": "Counter · etichetta cucina", "type": "text", "max_length": 60}),
                ("home.counter_kitchen_value", {"label": "Counter · valore cucina", "type": "text", "max_length": 40}),
                ("home.counter_last_label",    {"label": "Counter · etichetta ultimo ordine", "type": "text", "max_length": 60}),
                ("home.counter_last_value",    {"label": "Counter · valore ultimo ordine", "type": "text", "max_length": 40}),
            ]},
            {"label": "CTA hero", "fields": [
                ("home.primary_cta",    {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.primary_href",   {"label": "CTA primaria · destinazione", "type": "select",
                                           "choices": ["home", "menu", "lab", "moments", "ordina", "contatti"]}),
                ("home.secondary_cta",  {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
                ("home.secondary_href", {"label": "CTA secondaria · destinazione", "type": "select",
                                           "choices": ["home", "menu", "lab", "moments", "ordina", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".sm-menu-strip, .sm-delivery, .sm-manifesto, .sm-crew, .sm-atmo, .sm-final",
        "page": "home",
        "keywords": ["menu strip", "delivery", "manifesto", "crew", "atmo", "final", "cta"],
        "help": "Fasce copy della home: stats, menu strip, delivery, manifesto, crew, atmo, CTA finale.",
        "subgroups": [
            {"label": "Stats intestazione", "fields": [
                ("home.stats_label", {"label": "Stats · eyebrow", "type": "text", "max_length": 80}),
            ]},
            {"label": "Menu strip band", "fields": [
                ("home.menu_strip_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.menu_strip_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.menu_strip_intro",    {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.menu_strip_cta",      {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("home.menu_strip_cta_href", {"label": "CTA · destinazione", "type": "select",
                                                "choices": ["home", "menu", "lab", "moments", "ordina", "contatti"]}),
            ]},
            {"label": "Delivery band", "fields": [
                ("home.delivery_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.delivery_subtitle", {"label": "Subtitle", "type": "text", "max_length": 160}),
            ]},
            {"label": "Manifesto band", "fields": [
                ("home.manifesto_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.manifesto_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.manifesto_cta",      {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("home.manifesto_cta_href", {"label": "CTA · destinazione", "type": "select",
                                                "choices": ["home", "menu", "lab", "moments", "ordina", "contatti"]}),
            ]},
            {"label": "Crew intestazione", "fields": [
                ("home.crew_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.crew_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Atmo intestazione", "fields": [
                ("home.atmo_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.atmo_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Final CTA", "fields": [
                ("home.final_label",         {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.final_heading",       {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.final_intro",         {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.final_primary_cta",   {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.final_primary_href",  {"label": "CTA primaria · destinazione", "type": "select",
                                                "choices": ["home", "menu", "lab", "moments", "ordina", "contatti"]}),
                ("home.final_phone_cta",     {"label": "CTA telefono · etichetta", "type": "text", "max_length": 60}),
                ("home.final_phone_href",    {"label": "CTA telefono · href (tel:)", "type": "text", "max_length": 40}),
            ]},
        ],
    },
    {
        "id": "menu_page",
        "label": "Pagina Menu",
        "icon": "bi-journal-text",
        "region": ".sm-menu, .sm-menu-hero, .sm-producers",
        "page": "menu",
        "keywords": ["menu", "piatti", "producers", "allergeni"],
        "help": "Intestazione pagina menu, allergeni, producers intestazione. Le sezioni del menu e i piatti si modificano dai gruppi indexed `Menu · Sections` e `Menu · Sezione N · Items`.",
        "fields": [
            ("menu.eyebrow",             {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("menu.headline",            {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("menu.intro",               {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("menu.allergen_label",      {"label": "Allergeni · label", "type": "text", "max_length": 80}),
            ("menu.allergen_text",       {"label": "Allergeni · testo", "type": "textarea", "max_length": 400}),
            ("menu.producers_label",     {"label": "Producers · eyebrow", "type": "text", "max_length": 80}),
            ("menu.producers_heading",   {"label": "Producers · titolo", "type": "richtext", "max_length": 220}),
            ("menu.producers_intro",     {"label": "Producers · intro", "type": "textarea", "max_length": 400}),
            ("menu.final_label",         {"label": "Final · eyebrow", "type": "text", "max_length": 80}),
            ("menu.final_heading",       {"label": "Final · titolo", "type": "richtext", "max_length": 220}),
            ("menu.final_primary_cta",   {"label": "Final · CTA primaria etichetta", "type": "text", "max_length": 60}),
            ("menu.final_primary_href",  {"label": "Final · CTA primaria destinazione", "type": "select",
                                            "choices": ["home", "menu", "lab", "moments", "ordina", "contatti"]}),
            ("menu.final_secondary_cta", {"label": "Final · CTA secondaria etichetta", "type": "text", "max_length": 60}),
            ("menu.final_secondary_href",{"label": "Final · CTA secondaria destinazione", "type": "select",
                                            "choices": ["home", "menu", "lab", "moments", "ordina", "contatti"]}),
        ],
    },
    {
        "id": "lab_page",
        "label": "Pagina Lab (about)",
        "icon": "bi-fire",
        "region": ".sm-lab, .sm-lab-hero, .sm-process, .sm-values, .sm-kitchen",
        "page": "lab",
        "keywords": ["lab", "manifesto", "process", "values", "kitchen", "crew"],
        "help": "Pagina il Lab: hero, manifesto, processo, valori, scheda tecnica cucina. Le crew/values/manifesto/process dettaglio si modificano dai gruppi indexed.",
        "fields": [
            ("lab.eyebrow",             {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("lab.headline",            {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("lab.intro",               {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("lab.hero_image",          {"label": "Hero image · URL", "type": "image", "max_length": 400}),
            ("lab.hero_caption",        {"label": "Hero image · didascalia", "type": "text", "max_length": 200}),
            ("lab.manifesto_label",     {"label": "Manifesto · eyebrow", "type": "text", "max_length": 80}),
            ("lab.process_label",       {"label": "Process · eyebrow", "type": "text", "max_length": 80}),
            ("lab.process_heading",     {"label": "Process · titolo", "type": "richtext", "max_length": 220}),
            ("lab.crew_label",          {"label": "Crew · eyebrow", "type": "text", "max_length": 80}),
            ("lab.crew_heading",        {"label": "Crew · titolo", "type": "richtext", "max_length": 220}),
            ("lab.values_label",        {"label": "Values · eyebrow", "type": "text", "max_length": 80}),
            ("lab.values_heading",      {"label": "Values · titolo", "type": "richtext", "max_length": 220}),
            ("lab.kitchen_label",       {"label": "Kitchen · eyebrow", "type": "text", "max_length": 80}),
            ("lab.kitchen_heading",     {"label": "Kitchen · titolo", "type": "richtext", "max_length": 220}),
            ("lab.final_label",         {"label": "Final · eyebrow", "type": "text", "max_length": 80}),
            ("lab.final_heading",       {"label": "Final · titolo", "type": "richtext", "max_length": 220}),
            ("lab.final_intro",         {"label": "Final · intro", "type": "textarea", "max_length": 500}),
            ("lab.final_primary_cta",   {"label": "Final · CTA primaria etichetta", "type": "text", "max_length": 60}),
            ("lab.final_primary_href",  {"label": "Final · CTA primaria destinazione", "type": "select",
                                            "choices": ["home", "menu", "lab", "moments", "ordina", "contatti"]}),
            ("lab.final_secondary_cta", {"label": "Final · CTA secondaria etichetta", "type": "text", "max_length": 60}),
            ("lab.final_secondary_href",{"label": "Final · CTA secondaria destinazione", "type": "select",
                                            "choices": ["home", "menu", "lab", "moments", "ordina", "contatti"]}),
        ],
    },
    {
        "id": "moments_page",
        "label": "Pagina Moments (gallery)",
        "icon": "bi-images",
        "region": ".sm-moments, .sm-moments-hero, .sm-featured",
        "page": "moments",
        "keywords": ["moments", "gallery", "diary", "featured"],
        "help": "Pagina Moments: hero, categoria etichette, featured quote, CTA social. La griglia delle foto si modifica dal gruppo indexed `Moments · Grid`.",
        "fields": [
            ("moments.eyebrow",                {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("moments.headline",               {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("moments.intro",                  {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("moments.categories_label",       {"label": "Categories · label", "type": "text", "max_length": 40}),
            ("moments.categories_all_label",   {"label": "Categories · label \"Tutti\"", "type": "text", "max_length": 40}),
            ("moments.featured_image",         {"label": "Featured · immagine URL", "type": "image", "max_length": 400}),
            ("moments.featured_quote",         {"label": "Featured · quote", "type": "textarea", "max_length": 500}),
            ("moments.featured_author",        {"label": "Featured · autore", "type": "text", "max_length": 200}),
            ("moments.featured_filename",      {"label": "Featured · filename (label visibile)", "type": "text", "max_length": 40}),
            ("moments.final_label",            {"label": "Final · eyebrow", "type": "text", "max_length": 80}),
            ("moments.final_heading",          {"label": "Final · titolo", "type": "richtext", "max_length": 220}),
            ("moments.final_intro",            {"label": "Final · intro", "type": "textarea", "max_length": 500}),
            ("moments.final_instagram_cta",    {"label": "Final · Instagram CTA", "type": "text", "max_length": 80}),
            ("moments.final_tiktok_cta",       {"label": "Final · TikTok CTA", "type": "text", "max_length": 80}),
        ],
    },
    {
        "id": "ordina_page",
        "label": "Pagina Ordina (order · NOVEL kind)",
        "icon": "bi-basket",
        "region": ".sm-ordina, .sm-routes, .sm-partners, .sm-phone, .sm-faq",
        "page": "ordina",
        "keywords": ["ordina", "order", "routes", "partners", "phone", "faq"],
        "help": "Pagina Ordina: hero, counter stato banco, etichette routes/partners/hours/phone/FAQ. Rotte, partners, hours, FAQ si modificano dai gruppi indexed.",
        "fields": [
            ("ordina.eyebrow",                {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("ordina.headline",               {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("ordina.intro",                  {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("ordina.counter_status_label",   {"label": "Counter · stato label", "type": "text", "max_length": 60}),
            ("ordina.counter_queue_label",    {"label": "Counter · coda label", "type": "text", "max_length": 60}),
            ("ordina.counter_queue_value",    {"label": "Counter · coda valore", "type": "text", "max_length": 40}),
            ("ordina.counter_kitchen_label",  {"label": "Counter · cucina label", "type": "text", "max_length": 60}),
            ("ordina.counter_kitchen_value",  {"label": "Counter · cucina valore", "type": "text", "max_length": 40}),
            ("ordina.counter_last_label",     {"label": "Counter · ultimo ordine label", "type": "text", "max_length": 60}),
            ("ordina.counter_last_value",     {"label": "Counter · ultimo ordine valore", "type": "text", "max_length": 40}),
            ("ordina.routes_label",           {"label": "Routes · eyebrow", "type": "text", "max_length": 80}),
            ("ordina.routes_heading",         {"label": "Routes · titolo", "type": "richtext", "max_length": 220}),
            ("ordina.partners_label",         {"label": "Partners · eyebrow", "type": "text", "max_length": 80}),
            ("ordina.partners_heading",       {"label": "Partners · titolo", "type": "richtext", "max_length": 220}),
            ("ordina.hours_label",            {"label": "Hours · eyebrow", "type": "text", "max_length": 80}),
            ("ordina.hours_heading",          {"label": "Hours · titolo", "type": "richtext", "max_length": 220}),
            ("ordina.hours_note",             {"label": "Hours · nota", "type": "textarea", "max_length": 300}),
            ("ordina.allergen_label",         {"label": "Allergeni · label", "type": "text", "max_length": 80}),
            ("ordina.allergen_text",          {"label": "Allergeni · testo", "type": "textarea", "max_length": 400}),
            ("ordina.phone_label",            {"label": "Phone · eyebrow", "type": "text", "max_length": 80}),
            ("ordina.phone_heading",          {"label": "Phone · titolo", "type": "richtext", "max_length": 220}),
            ("ordina.phone_intro",            {"label": "Phone · intro", "type": "textarea", "max_length": 500}),
            ("ordina.phone_cta_label",        {"label": "Phone · CTA etichetta", "type": "text", "max_length": 60}),
            ("ordina.phone_cta_href",         {"label": "Phone · CTA tel:href", "type": "text", "max_length": 40}),
            ("ordina.faq_label",              {"label": "FAQ · eyebrow", "type": "text", "max_length": 80}),
            ("ordina.faq_heading",            {"label": "FAQ · titolo", "type": "richtext", "max_length": 220}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-geo-alt",
        "region": ".sm-contact, .sm-contact-hero, .sm-map, .sm-transport, .sm-jobs",
        "page": "contatti",
        "keywords": ["contatti", "indirizzo", "mappa", "jobs", "social", "form"],
        "help": "Pagina contatti: indirizzo, mappa, channels label, jobs, social label, form scalars. Channels/hours/transport/jobs/social list si modificano dai gruppi indexed.",
        "fields": [
            ("contatti.eyebrow",                         {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("contatti.headline",                        {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("contatti.intro",                           {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("contatti.address_label",                   {"label": "Indirizzo · label", "type": "text", "max_length": 60}),
            ("contatti.address_value",                   {"label": "Indirizzo · valore", "type": "text", "max_length": 200}),
            ("contatti.address_note",                    {"label": "Indirizzo · nota", "type": "text", "max_length": 200}),
            ("contatti.map_lat",                         {"label": "Mappa · latitudine", "type": "text", "max_length": 20}),
            ("contatti.map_lon",                         {"label": "Mappa · longitudine", "type": "text", "max_length": 20}),
            ("contatti.map_zoom",                        {"label": "Mappa · zoom", "type": "text", "max_length": 8}),
            ("contatti.map_label",                       {"label": "Mappa · label", "type": "text", "max_length": 160}),
            ("contatti.channels_label",                  {"label": "Channels · eyebrow", "type": "text", "max_length": 80}),
            ("contatti.hours_label",                     {"label": "Hours · eyebrow", "type": "text", "max_length": 80}),
            ("contatti.hours_note",                      {"label": "Hours · nota", "type": "textarea", "max_length": 300}),
            ("contatti.transport_label",                 {"label": "Transport · eyebrow", "type": "text", "max_length": 80}),
            ("contatti.jobs_label",                      {"label": "Jobs · eyebrow", "type": "text", "max_length": 80}),
            ("contatti.jobs_heading",                    {"label": "Jobs · titolo", "type": "richtext", "max_length": 220}),
            ("contatti.jobs_intro",                      {"label": "Jobs · intro", "type": "textarea", "max_length": 500}),
            ("contatti.jobs_cta_label",                  {"label": "Jobs · CTA etichetta", "type": "text", "max_length": 60}),
            ("contatti.jobs_cta_href",                   {"label": "Jobs · CTA href (email)", "type": "text", "max_length": 120}),
            ("contatti.social_label",                    {"label": "Social · eyebrow", "type": "text", "max_length": 80}),
            ("contatti.form_label",                      {"label": "Form · eyebrow", "type": "text", "max_length": 80}),
            ("contatti.form_heading",                    {"label": "Form · titolo", "type": "richtext", "max_length": 220}),
            ("contatti.form_intro",                      {"label": "Form · intro", "type": "textarea", "max_length": 500}),
            ("contatti.form_field_name",                 {"label": "Form · campo Nome label", "type": "text", "max_length": 60}),
            ("contatti.form_field_email",                {"label": "Form · campo Email label", "type": "text", "max_length": 60}),
            ("contatti.form_field_phone",                {"label": "Form · campo Telefono label", "type": "text", "max_length": 60}),
            ("contatti.form_field_message",              {"label": "Form · campo Messaggio label", "type": "text", "max_length": 60}),
            ("contatti.form_field_message_placeholder",  {"label": "Form · Messaggio placeholder", "type": "text", "max_length": 200}),
            ("contatti.form_submit_label",               {"label": "Form · CTA submit", "type": "text", "max_length": 60}),
            ("contatti.form_submit_note",                {"label": "Form · nota post-submit", "type": "text", "max_length": 300}),
        ],
    },
]


# A.15 · Bottega artisan-workshop — 13th enrolled editor archetype,
# first template of the ecommerce family. OPENS the family via staged
# dedicated-schema progression (fourth staged opening after real-estate,
# portfolio, restaurant-continuation). Luxe (`fashion-editorial`) stays
# OUT until A.15b.
#
# BOUNDARY EDITOR VS COMMERCE-ADMIN (verified Step-0 runtime):
#   • Editor scope = template_content_bottega.py REGISTRY = presentational
#     demo showcase (product card listing demo · single-product demo
#     record · hero · copy bands · journal entries).
#   • Commerce-admin scope = apps.commerce.Storefront/Product/Variant/
#     Cart/Order/PaymentIntent = REAL catalog backend · managed via
#     seller dashboard (Phase 3a/3b).
#   • LiveTemplateView (apps/catalog/views.py) does NOT import from
#     apps.commerce · the two surfaces are ORTHOGONAL.
#   • Editor enrollment touches ONLY template_content presentational
#     demo content. Zero touches to apps.commerce models/services/URLs.
#
# Skin uses `.aw-*` selectors (chrome `.aw-nav`/`.aw-foot`, sections
# `.aw-section`/`.aw-card`/`.aw-stamp`/`.aw-wrap` etc.) · 31 mature
# `html[dir="rtl"]` rules in `_base.html`.
#
# Shape contract notes (Step-0 audit verified):
#   • 6 pages: home · shop (NOVEL) · product (NOVEL) · atelier (about)
#     · journal (NOVEL) · contatti. 5-locale parity PERFECT (236 keys
#     × 5 locales, zero gaps). Three novel page kinds (`shop`/`product`/
#     `journal`) — plain string identifiers, no view dispatch.
#   • 0 scalar image at top-level (artisan-workshop is typographic-led
#     DNA per Session 42 observations · no hero photo).
#   • 2 nested-dict scalar images (`product.artisan_portrait` ·
#     `atelier.founder_portrait`) · Chiara `studio.founder.image`
#     precedent shape.
#   • 4 image-in-dict-row lists (home.latest_items × 4, home.makers ×
#     4, shop.products × 9, product.related_items × 3) · 20 image
#     cells · shallow shape (Vertex/Villa/Chiara/Sapore/Brace precedents).
#   • Total editable image surface: 22 (0 scalar top + 2 nested-dict
#     scalar + 20 dict-row cells).
#   • Menu-like shape: `shop.products` is a 9-item demo product listing
#     (dict 11 cols). Col-level exclusions: `id` (slug for routing) +
#     `available` (bool flag). Cols IN: name/artisan/place/meta/price/
#     tag/image/n/edition. **`n`/`edition` kept IN despite looking
#     "technical" — audit confirms they are editorial visible content:
#     'N° 042' / '3 / 8' / 'Esaurito' are customer-facing badges, same
#     category as Sapore forno.pizza_signatures.n (roman numeral visible
#     counter · kept IN) and Chiara ledger_rows num. Stringent IN call
#     per user Step 1 guidance.**
#   • `posts` list EMPTY (same as Sapore · Brace · structural absence ·
#     detail-page policy stays at 6-archetype uniform enforcement).
#   • Complex shapes explicitly KEPT OUT of the perimeter:
#       - site.hours_footer_rows · site.stockists_rows (flat list-of-str)
#       - home.press_items (5 · flat list-of-str)
#       - shop.filter_groups · shop.sort_options (form-like structural)
#       - product.gallery (4 image URLs · flat list-of-str · same
#         category as Sapore storia.story flat list-of-str policy)
#       - product.size_options (flat list-of-str)
#       - contatti.card_hours_rows (flat list-of-str)
#       - contatti.form_fields (form structure)
#       - pages (navigation index)
#       - posts (empty)
#   • Col-level exclusions (structural identifiers):
#       - shop.products[].id + .available
#       - home.latest_items[].id
#       - product.related_items[].id
#   • Zero mutable repeater · zero image per-locale · pure enrollment.
#   • 14 readonly indexed list entries in STRUCTURED_FIELD_SHAPES ·
#     tutti parent · ZERO deep-path (Bottega has no list-nested-in-list
#     parent · simpler than Sapore/Brace).

BOTTEGA_ARTISAN_WORKSHOP_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".aw-nav, .aw-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "bottega", "tagline", "chrome"],
        "help": "Nome bottega, iniziale crest, tagline, contatti sintetici, chrome footer, labels generici (material/made_in/edition/artisan/shipping/guarantee).",
        "fields": [
            ("site.logo_word",        {"label": "Nome bottega", "type": "text", "max_length": 60,
                                         "placeholder": "La Bottega di Martino"}),
            ("site.logo_initial",     {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.tag",              {"label": "Tagline (nav + strip)", "type": "text", "max_length": 160}),
            ("site.phone",            {"label": "Telefono", "type": "text", "max_length": 40}),
            ("site.whatsapp",         {"label": "WhatsApp (display)", "type": "text", "max_length": 40}),
            ("site.whatsapp_link",    {"label": "WhatsApp · URL completo", "type": "url", "max_length": 300}),
            ("site.email",            {"label": "Email", "type": "text", "max_length": 120}),
            ("site.address",          {"label": "Indirizzo (una riga)", "type": "text", "max_length": 200}),
            ("site.hours_compact",    {"label": "Orari sintetici (nav/footer)", "type": "text", "max_length": 160}),
            ("site.license",          {"label": "Licenza / P.IVA", "type": "text", "max_length": 200}),
            ("site.footer_intro",     {"label": "Intro footer", "type": "textarea", "max_length": 500}),
            ("site.nav_cta",          {"label": "CTA nav · etichetta", "type": "text", "max_length": 60}),
            ("site.currency_symbol",  {"label": "Simbolo valuta (€/£/$)", "type": "text", "max_length": 4}),
            ("site.material_label",   {"label": "Label · Materiale", "type": "text", "max_length": 40}),
            ("site.made_in_label",    {"label": "Label · Fatto a", "type": "text", "max_length": 40}),
            ("site.edition_label",    {"label": "Label · Edizione", "type": "text", "max_length": 40}),
            ("site.artisan_label",    {"label": "Label · Firmato da", "type": "text", "max_length": 40}),
            ("site.shipping_label",   {"label": "Label · Spedizione", "type": "text", "max_length": 40}),
            ("site.shipping_value",   {"label": "Valore · Spedizione", "type": "text", "max_length": 160}),
            ("site.guarantee_label",  {"label": "Label · Garanzia", "type": "text", "max_length": 40}),
            ("site.guarantee_value",  {"label": "Valore · Garanzia", "type": "text", "max_length": 160}),
            ("site.shop_count_unit",  {"label": "Unità catalogo (es. 'pezzi')", "type": "text", "max_length": 40}),
            ("site.shop_filter_label",{"label": "Label · Filtri catalogo", "type": "text", "max_length": 40}),
            ("site.foot_studio",      {"label": "Footer · titolo bottega", "type": "text", "max_length": 40}),
            ("site.foot_pages",       {"label": "Footer · titolo Mappa", "type": "text", "max_length": 40}),
            ("site.foot_contact",     {"label": "Footer · titolo Contatti", "type": "text", "max_length": 40}),
            ("site.foot_stockists",   {"label": "Footer · titolo Stockists", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".aw-hero, .aw-stamp",
        "page": "home",
        "keywords": ["hero", "headline", "eyebrow", "intro", "cta", "stamp"],
        "help": "Primo scroll della home (artisan-workshop · typographic-led · no hero image scalar) · eyebrow/headline/intro + CTAs + stamp decorative block.",
        "subgroups": [
            {"label": "Hero copy", "fields": [
                ("home.eyebrow",        {"label": "Eyebrow", "type": "text", "max_length": 120}),
                ("home.headline",       {"label": "Headline", "type": "richtext", "max_length": 220,
                                           "help": "Consentiti i tag <em> per italici."}),
                ("home.intro",          {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "CTA hero", "fields": [
                ("home.primary_cta",    {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.primary_href",   {"label": "CTA primaria · destinazione", "type": "select",
                                           "choices": ["home", "shop", "product", "atelier", "journal", "contatti"]}),
                ("home.secondary_cta",  {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
                ("home.secondary_href", {"label": "CTA secondaria · destinazione", "type": "select",
                                           "choices": ["home", "shop", "product", "atelier", "journal", "contatti"]}),
            ]},
            {"label": "Stamp decorative block", "fields": [
                ("home.stamp_label",        {"label": "Stamp · eyebrow", "type": "text", "max_length": 80}),
                ("home.stamp_heading",      {"label": "Stamp · titolo", "type": "richtext", "max_length": 220}),
                ("home.stamp_footer",       {"label": "Stamp · footer caption", "type": "text", "max_length": 200}),
                ("home.stamp_corner_index", {"label": "Stamp · indice angolo", "type": "text", "max_length": 8}),
                ("home.stamp_corner_word",  {"label": "Stamp · parola angolo", "type": "text", "max_length": 40}),
            ]},
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".aw-section",
        "page": "home",
        "keywords": ["latest", "makers", "provenance", "care", "press", "journal", "cta"],
        "help": "Fasce copy della home: latest items · makers · provenance · care · press label · journal teaser · CTA finale.",
        "subgroups": [
            {"label": "Latest items intestazione", "fields": [
                ("home.latest_label",      {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.latest_heading",    {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.latest_link_label", {"label": "Link · etichetta", "type": "text", "max_length": 60}),
                ("home.latest_link_href",  {"label": "Link · destinazione", "type": "select",
                                              "choices": ["home", "shop", "product", "atelier", "journal", "contatti"]}),
            ]},
            {"label": "Makers intestazione", "fields": [
                ("home.makers_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.makers_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.makers_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Provenance intestazione", "fields": [
                ("home.provenance_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.provenance_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.provenance_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Care intestazione", "fields": [
                ("home.care_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.care_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Press intestazione", "fields": [
                ("home.press_label", {"label": "Eyebrow", "type": "text", "max_length": 80}),
            ]},
            {"label": "Journal teaser", "fields": [
                ("home.journal_teaser_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.journal_teaser_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.journal_teaser_link",    {"label": "Link · etichetta", "type": "text", "max_length": 60}),
                ("home.journal_teaser_href",    {"label": "Link · destinazione", "type": "select",
                                                   "choices": ["home", "shop", "product", "atelier", "journal", "contatti"]}),
            ]},
            {"label": "CTA finale", "fields": [
                ("home.cta_label",         {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.cta_heading",       {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.cta_intro",         {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.cta_primary",       {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.cta_primary_href",  {"label": "CTA primaria · destinazione", "type": "select",
                                              "choices": ["home", "shop", "product", "atelier", "journal", "contatti"]}),
                ("home.cta_secondary",     {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
            ]},
        ],
    },
    {
        "id": "shop_page",
        "label": "Pagina Shop (catalog listing demo · novel `shop` kind)",
        "icon": "bi-grid",
        "region": ".aw-shop, .aw-shop-hero, .aw-products",
        "page": "shop",
        "keywords": ["shop", "catalogo", "listing", "products"],
        "help": "Pagina catalogo demo: hero + filter/sort label + result_count + footer_note. La griglia dei prodotti demo si modifica dal gruppo indexed `Shop · Products (9 demo)`.",
        "fields": [
            ("shop.eyebrow",              {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("shop.headline",             {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("shop.intro",                {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("shop.filter_section_label", {"label": "Filter section · label", "type": "text", "max_length": 80}),
            ("shop.sort_label",           {"label": "Sort · label", "type": "text", "max_length": 80}),
            ("shop.result_count",         {"label": "Result · count text", "type": "text", "max_length": 80}),
            ("shop.result_subtitle",      {"label": "Result · subtitle", "type": "textarea", "max_length": 300}),
            ("shop.footer_note_label",    {"label": "Footer note · label", "type": "text", "max_length": 60}),
            ("shop.footer_note",          {"label": "Footer note · text", "type": "textarea", "max_length": 500}),
        ],
    },
    {
        "id": "product_page",
        "label": "Pagina Product (single demo record · novel `product` kind)",
        "icon": "bi-box",
        "region": ".aw-product, .aw-product-hero, .aw-artisan, .aw-care, .aw-provenance",
        "page": "product",
        "keywords": ["product", "prodotto", "item", "artisan", "care", "provenance"],
        "help": "Pagina demo singolo prodotto (NON commerce state · DEMO presentational). Customer edita il record showcase. Related items si modificano dal gruppo indexed `Product · Related items (3)`.",
        "fields": [
            ("product.n",                 {"label": "Numero pezzo (visible)", "type": "text", "max_length": 16}),
            ("product.edition",           {"label": "Edizione (visible · '3/8' · 'Esaurito')", "type": "text", "max_length": 40}),
            ("product.edition_note",      {"label": "Edizione · nota estesa", "type": "textarea", "max_length": 300}),
            ("product.name",              {"label": "Nome prodotto", "type": "text", "max_length": 120}),
            ("product.subtitle",          {"label": "Subtitle (materiale · tecnica)", "type": "textarea", "max_length": 300}),
            ("product.price",             {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
            ("product.vat_note",          {"label": "Nota IVA / spedizione", "type": "textarea", "max_length": 300}),
            ("product.intro",             {"label": "Intro lunga", "type": "textarea", "max_length": 800}),
            ("product.info_label",        {"label": "Info rows · label", "type": "text", "max_length": 60}),
            ("product.size_label",        {"label": "Size · label", "type": "text", "max_length": 60}),
            ("product.size_intro",        {"label": "Size · intro", "type": "textarea", "max_length": 300}),
            ("product.size_chart_link",   {"label": "Size · chart link label", "type": "text", "max_length": 80}),
            ("product.size_chart_href",   {"label": "Size · chart link destinazione", "type": "select",
                                              "choices": ["home", "shop", "product", "atelier", "journal", "contatti"]}),
            ("product.artisan_label",     {"label": "Artisan · label", "type": "text", "max_length": 60}),
            ("product.artisan_name",      {"label": "Artisan · nome", "type": "text", "max_length": 120}),
            ("product.artisan_role",      {"label": "Artisan · ruolo", "type": "text", "max_length": 160}),
            ("product.artisan_bio",       {"label": "Artisan · bio", "type": "textarea", "max_length": 800}),
            ("product.artisan_portrait",  {"label": "Artisan · portrait URL (nested-dict scalar image)", "type": "image", "max_length": 400}),
            ("product.buy_primary",       {"label": "Buy · CTA primaria (demo · no commerce state)", "type": "text", "max_length": 60}),
            ("product.buy_secondary",     {"label": "Buy · CTA secondaria", "type": "text", "max_length": 60}),
            ("product.buy_note",          {"label": "Buy · nota", "type": "textarea", "max_length": 400}),
            ("product.care_label",        {"label": "Care · label", "type": "text", "max_length": 60}),
            ("product.care_intro",        {"label": "Care · intro", "type": "textarea", "max_length": 500}),
            ("product.provenance_label",  {"label": "Provenance · label", "type": "text", "max_length": 60}),
            ("product.provenance_heading",{"label": "Provenance · titolo", "type": "richtext", "max_length": 220}),
            ("product.related_label",     {"label": "Related · label", "type": "text", "max_length": 60}),
            ("product.related_intro",     {"label": "Related · intro", "type": "textarea", "max_length": 400}),
        ],
    },
    {
        "id": "atelier_page",
        "label": "Pagina Atelier (about)",
        "icon": "bi-building",
        "region": ".aw-atelier, .aw-atelier-hero, .aw-mission, .aw-numbers, .aw-process, .aw-visit",
        "page": "atelier",
        "keywords": ["atelier", "about", "mission", "numbers", "process", "visit", "founder"],
        "help": "Pagina about: hero · founder block (portrait nested-dict) · mission · numbers · process intestazione · visit block.",
        "fields": [
            ("atelier.eyebrow",            {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("atelier.headline",           {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("atelier.intro",              {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("atelier.founder_label",      {"label": "Founder · label", "type": "text", "max_length": 60}),
            ("atelier.founder_heading",    {"label": "Founder · titolo", "type": "richtext", "max_length": 220}),
            ("atelier.founder_text",       {"label": "Founder · paragrafo", "type": "textarea", "max_length": 800}),
            ("atelier.founder_portrait",   {"label": "Founder · portrait URL (nested-dict scalar image)", "type": "image", "max_length": 400}),
            ("atelier.founder_caption",    {"label": "Founder · didascalia", "type": "text", "max_length": 200}),
            ("atelier.mission_label",      {"label": "Mission · label", "type": "text", "max_length": 60}),
            ("atelier.mission_heading",    {"label": "Mission · titolo", "type": "richtext", "max_length": 220}),
            ("atelier.mission_text",       {"label": "Mission · paragrafo", "type": "textarea", "max_length": 600}),
            ("atelier.numbers_label",      {"label": "Numbers · label", "type": "text", "max_length": 60}),
            ("atelier.process_label",      {"label": "Process · label", "type": "text", "max_length": 60}),
            ("atelier.process_heading",    {"label": "Process · titolo", "type": "richtext", "max_length": 220}),
            ("atelier.visit_label",        {"label": "Visit · label", "type": "text", "max_length": 60}),
            ("atelier.visit_heading",      {"label": "Visit · titolo", "type": "richtext", "max_length": 220}),
            ("atelier.visit_text",         {"label": "Visit · paragrafo", "type": "textarea", "max_length": 500}),
            ("atelier.visit_primary",      {"label": "Visit · CTA primaria", "type": "text", "max_length": 60}),
            ("atelier.visit_primary_href", {"label": "Visit · CTA primaria destinazione", "type": "select",
                                              "choices": ["home", "shop", "product", "atelier", "journal", "contatti"]}),
            ("atelier.visit_secondary",    {"label": "Visit · CTA secondaria", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "journal_page",
        "label": "Pagina Journal (novel `journal` kind)",
        "icon": "bi-journal",
        "region": ".aw-journal, .aw-journal-hero, .aw-entries",
        "page": "journal",
        "keywords": ["journal", "quaderno", "note", "entries"],
        "help": "Pagina diario/journal: hero + entries intestazione. Le entries si modificano dal gruppo indexed `Journal · Entries (6)`.",
        "fields": [
            ("journal.eyebrow",  {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("journal.headline", {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("journal.intro",    {"label": "Intro", "type": "textarea", "max_length": 500}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-geo-alt",
        "region": ".aw-contact, .aw-contact-hero, .aw-contact-card, .aw-faq",
        "page": "contatti",
        "keywords": ["contatti", "bottega", "card", "faq", "form-labels"],
        "help": "Pagina contatti: hero · card (address/hours/phone/whatsapp/email labels+values) · FAQ intestazione · form scalar labels (struttura form OUT).",
        "fields": [
            ("contatti.eyebrow",                 {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("contatti.headline",                {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("contatti.intro",                   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("contatti.card_label",              {"label": "Card · label", "type": "text", "max_length": 60}),
            ("contatti.card_address_value",      {"label": "Card · indirizzo valore", "type": "text", "max_length": 200}),
            ("contatti.card_directions_label",   {"label": "Card · directions label", "type": "text", "max_length": 60}),
            ("contatti.card_directions_text",    {"label": "Card · directions text", "type": "textarea", "max_length": 400}),
            ("contatti.card_hours_label",        {"label": "Card · hours label", "type": "text", "max_length": 60}),
            ("contatti.card_phone_label",        {"label": "Card · phone label", "type": "text", "max_length": 60}),
            ("contatti.card_phone_value",        {"label": "Card · phone value", "type": "text", "max_length": 40}),
            ("contatti.card_whatsapp_label",     {"label": "Card · whatsapp label", "type": "text", "max_length": 60}),
            ("contatti.card_whatsapp_value",     {"label": "Card · whatsapp value", "type": "text", "max_length": 40}),
            ("contatti.card_email_label",        {"label": "Card · email label", "type": "text", "max_length": 60}),
            ("contatti.card_email_value",        {"label": "Card · email value", "type": "text", "max_length": 120}),
            ("contatti.faq_label",               {"label": "FAQ · label", "type": "text", "max_length": 60}),
            ("contatti.form_section_label",      {"label": "Form section · label", "type": "text", "max_length": 60}),
            ("contatti.form_section_intro",      {"label": "Form section · intro", "type": "textarea", "max_length": 400}),
            ("contatti.form_helper_required",    {"label": "Form · helper required", "type": "text", "max_length": 120}),
            ("contatti.form_submit_button",      {"label": "Form · CTA submit", "type": "text", "max_length": 60}),
            ("contatti.form_submit_note",        {"label": "Form · nota post-submit", "type": "textarea", "max_length": 400}),
        ],
    },
]


# ---------------------------------------------------------------------------
# A.15b · fashion-editorial (Luxe · luxe-fashion-store) — closes the
# ecommerce family opened by A.15 Bottega (artisan-workshop). Dedicated
# schema · staged dedicated-schema closure pattern (4th precedent after
# real-estate + portfolio + restaurant-continuation). Distinct skin
# folder (.fe-*) · photographically editorial campaign-driven · ALL 31
# image surfaces rendered (NO storage-only, unlike Bottega's typographic
# DNA) · novel page kinds `collection` + `lookbook` · zero touches to
# apps/commerce (boundary editor-vs-commerce-admin preserved · editor
# edits template_content registry showcase only). Six pages: home,
# collezione (collection), product, maison (about), lookbook, contatti.
# Stringent IN col-level audit (audit-driven · non-inertial): drop/n/tag
# IN (editorial badges · customer-facing) · id/available OUT (structural
# routing + commerce-state-like boolean).
# ---------------------------------------------------------------------------
LUXE_FASHION_EDITORIAL_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".fe-nav, .fe-foot",
        "page": "*",
        "keywords": ["logo", "maison", "luxe", "tagline", "chrome", "private"],
        "help": "Nome maison, iniziale crest, subline (Milano · Parigi · Tokyo), tagline, contatti (direzione clienti + concierge), chrome footer, label meta strip (drop/season/shipping/viewing/waitlist/rsvp).",
        "fields": [
            ("site.logo_word",            {"label": "Nome maison", "type": "text", "max_length": 60,
                                             "placeholder": "Maison Luxe"}),
            ("site.logo_initial",         {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.logo_subline",         {"label": "Subline (città maison)", "type": "text", "max_length": 80}),
            ("site.tag",                  {"label": "Tagline (nav · strip · atelier collezione)", "type": "text", "max_length": 160}),
            ("site.phone",                {"label": "Telefono", "type": "text", "max_length": 40}),
            ("site.private_phone_label",  {"label": "Label · direzione clienti", "type": "text", "max_length": 60}),
            ("site.email",                {"label": "Email", "type": "text", "max_length": 120}),
            ("site.private_email_label",  {"label": "Label · concierge clienti", "type": "text", "max_length": 60}),
            ("site.address",              {"label": "Indirizzo (una riga)", "type": "text", "max_length": 200}),
            ("site.showroom_paris",       {"label": "Showroom Parigi (una riga)", "type": "text", "max_length": 200}),
            ("site.showroom_tokyo",       {"label": "Showroom Tokyo (una riga)", "type": "text", "max_length": 200}),
            ("site.hours_compact",        {"label": "Orari sintetici", "type": "text", "max_length": 160}),
            ("site.license",              {"label": "Licenza / P.IVA / CCIAA", "type": "text", "max_length": 240}),
            ("site.footer_intro",         {"label": "Intro footer", "type": "textarea", "max_length": 500}),
            ("site.nav_cta",              {"label": "CTA nav · etichetta", "type": "text", "max_length": 60}),
            ("site.currency_symbol",      {"label": "Simbolo valuta (€/£/$)", "type": "text", "max_length": 4}),
            ("site.collection_label",     {"label": "Label · Collezione", "type": "text", "max_length": 40}),
            ("site.drop_label",           {"label": "Label · Drop", "type": "text", "max_length": 40}),
            ("site.season_label",         {"label": "Label · Stagione", "type": "text", "max_length": 40}),
            ("site.shipping_label",       {"label": "Label · Consegna riservata", "type": "text", "max_length": 60}),
            ("site.shipping_value",       {"label": "Valore · Consegna riservata", "type": "text", "max_length": 200}),
            ("site.viewing_label",        {"label": "Label · Private viewing", "type": "text", "max_length": 40}),
            ("site.viewing_value",        {"label": "Valore · Private viewing", "type": "text", "max_length": 200}),
            ("site.waitlist_label",       {"label": "Label · Lista d'attesa", "type": "text", "max_length": 40}),
            ("site.rsvp_label",           {"label": "Label · RSVP", "type": "text", "max_length": 40}),
            ("site.foot_studio",          {"label": "Footer · titolo La maison", "type": "text", "max_length": 40}),
            ("site.foot_pages",           {"label": "Footer · titolo Mappa", "type": "text", "max_length": 40}),
            ("site.foot_contact",         {"label": "Footer · titolo Direzione clienti", "type": "text", "max_length": 40}),
            ("site.foot_offices",         {"label": "Footer · titolo Atelier & showroom", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".fe-hero",
        "page": "home",
        "keywords": ["hero", "cover", "headline", "eyebrow", "intro", "cta", "styling"],
        "help": "Primo scroll della home · cover scalar image (rendered · editorial cover LEFT) · issue + styling + cover labels · hero copy + CTAs.",
        "subgroups": [
            {"label": "Cover (rendered scalar image)", "fields": [
                ("home.cover_image",          {"label": "Cover image · URL (rendered)", "type": "image", "max_length": 400}),
                ("home.issue",                {"label": "Issue (es. 'Issue 12 · Primavera 26')", "type": "text", "max_length": 160}),
                ("home.issue_label",          {"label": "Issue · label", "type": "text", "max_length": 40}),
                ("home.cover_styling_label",  {"label": "Styling · label", "type": "text", "max_length": 40}),
                ("home.cover_styling_name",   {"label": "Styling · nome (es. 'Carla Sozzani')", "type": "text", "max_length": 120}),
                ("home.cover_label",          {"label": "Cover · label", "type": "text", "max_length": 40}),
                ("home.cover_subject",        {"label": "Cover · soggetto (es. 'La Muse en Velours')", "type": "text", "max_length": 160}),
            ]},
            {"label": "Hero copy", "fields": [
                ("home.eyebrow",              {"label": "Eyebrow", "type": "text", "max_length": 160}),
                ("home.headline",             {"label": "Headline", "type": "richtext", "max_length": 220,
                                                 "help": "Consentiti i tag <em> per italici editoriali."}),
                ("home.headline_credit_line", {"label": "Headline credit line", "type": "text", "max_length": 200}),
                ("home.intro",                {"label": "Intro", "type": "textarea", "max_length": 600}),
            ]},
            {"label": "CTA hero", "fields": [
                ("home.primary_cta",          {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.primary_href",         {"label": "CTA primaria · destinazione", "type": "select",
                                                 "choices": ["home", "collezione", "product", "maison", "lookbook", "contatti"]}),
                ("home.secondary_label",      {"label": "CTA secondaria · label (es. 'Direzione creativa')", "type": "text", "max_length": 60}),
                ("home.secondary_name",       {"label": "CTA secondaria · nome", "type": "text", "max_length": 120}),
            ]},
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".fe-section",
        "page": "home",
        "keywords": ["edition", "tiles", "manifesto", "atelier-numbers", "lookbook-teaser", "press", "drop", "private"],
        "help": "Fasce copy della home: edition tiles intestazione · manifesto · atelier numbers intestazione · lookbook teaser · press · drop band · private viewing band.",
        "subgroups": [
            {"label": "Edition tiles intestazione", "fields": [
                ("home.edition_label",        {"label": "Edition · label", "type": "text", "max_length": 80}),
                ("home.edition_subline",      {"label": "Edition · subline", "type": "text", "max_length": 160}),
            ]},
            {"label": "Manifesto", "fields": [
                ("home.manifesto_label",      {"label": "Manifesto · label", "type": "text", "max_length": 80}),
                ("home.manifesto_heading",    {"label": "Manifesto · titolo", "type": "richtext", "max_length": 220}),
                ("home.manifesto_text",       {"label": "Manifesto · paragrafo", "type": "textarea", "max_length": 700}),
            ]},
            {"label": "Atelier numbers intestazione", "fields": [
                ("home.atelier_numbers_label",{"label": "Atelier numbers · label", "type": "text", "max_length": 80}),
            ]},
            {"label": "Lookbook teaser", "fields": [
                ("home.lookbook_teaser_label",   {"label": "Lookbook teaser · label", "type": "text", "max_length": 80}),
                ("home.lookbook_teaser_heading", {"label": "Lookbook teaser · titolo", "type": "richtext", "max_length": 220}),
                ("home.lookbook_teaser_intro",   {"label": "Lookbook teaser · intro", "type": "textarea", "max_length": 600}),
                ("home.lookbook_teaser_link",    {"label": "Lookbook teaser · link label", "type": "text", "max_length": 60}),
                ("home.lookbook_teaser_href",    {"label": "Lookbook teaser · link destinazione", "type": "select",
                                                    "choices": ["home", "collezione", "product", "maison", "lookbook", "contatti"]}),
            ]},
            {"label": "Press intestazione", "fields": [
                ("home.press_label",          {"label": "Press · label", "type": "text", "max_length": 80}),
                ("home.press_intro",          {"label": "Press · intro (es. 'Recensita su')", "type": "text", "max_length": 120}),
            ]},
            {"label": "Drop band", "fields": [
                ("home.drop_label",           {"label": "Drop · label (es. 'Prossimo drop')", "type": "text", "max_length": 80}),
                ("home.drop_heading",         {"label": "Drop · titolo", "type": "richtext", "max_length": 220}),
                ("home.drop_subhead",         {"label": "Drop · subhead", "type": "textarea", "max_length": 300}),
                ("home.drop_cta",             {"label": "Drop · CTA etichetta", "type": "text", "max_length": 60}),
                ("home.drop_cta_href",        {"label": "Drop · CTA destinazione", "type": "select",
                                                 "choices": ["home", "collezione", "product", "maison", "lookbook", "contatti"]}),
            ]},
            {"label": "Private viewing band", "fields": [
                ("home.private_label",        {"label": "Private · label", "type": "text", "max_length": 80}),
                ("home.private_heading",      {"label": "Private · titolo", "type": "richtext", "max_length": 220}),
                ("home.private_intro",        {"label": "Private · intro", "type": "textarea", "max_length": 600}),
                ("home.private_primary",      {"label": "Private · CTA primaria", "type": "text", "max_length": 60}),
                ("home.private_primary_href", {"label": "Private · CTA primaria destinazione", "type": "select",
                                                 "choices": ["home", "collezione", "product", "maison", "lookbook", "contatti"]}),
                ("home.private_secondary",    {"label": "Private · CTA secondaria", "type": "text", "max_length": 60}),
                ("home.private_secondary_href",{"label":"Private · CTA secondaria destinazione", "type": "select",
                                                 "choices": ["home", "collezione", "product", "maison", "lookbook", "contatti"]}),
            ]},
        ],
    },
    {
        "id": "collezione_page",
        "label": "Pagina Collezione (catalog listing demo · novel `collection` kind)",
        "icon": "bi-grid",
        "region": ".fe-collection, .fe-products",
        "page": "collezione",
        "keywords": ["collezione", "collection", "catalogo", "listing", "drop"],
        "help": "Pagina catalogo demo: season chip + hero + filter/sort label + result_count + footer_note. La griglia dei capi demo si modifica dal gruppo indexed `Collezione · Products (9 demo)`.",
        "fields": [
            ("collezione.season_chip",       {"label": "Season chip", "type": "text", "max_length": 80}),
            ("collezione.eyebrow",           {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("collezione.headline",          {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("collezione.intro",             {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("collezione.filter_label",      {"label": "Filter · label", "type": "text", "max_length": 80}),
            ("collezione.sort_label",        {"label": "Sort · label", "type": "text", "max_length": 80}),
            ("collezione.result_count",      {"label": "Result · count text", "type": "text", "max_length": 120}),
            ("collezione.result_subtitle",   {"label": "Result · subtitle", "type": "textarea", "max_length": 300}),
            ("collezione.footer_note_label", {"label": "Footer note · label", "type": "text", "max_length": 80}),
            ("collezione.footer_note",       {"label": "Footer note · text", "type": "textarea", "max_length": 600}),
        ],
    },
    {
        "id": "product_page",
        "label": "Pagina Product (single demo record · `product` kind)",
        "icon": "bi-box",
        "region": ".fe-product, .fe-product-hero, .fe-atelier, .fe-care, .fe-provenance",
        "page": "product",
        "keywords": ["product", "prodotto", "look", "atelier", "care", "provenance"],
        "help": "Pagina demo singolo prodotto (NON commerce state · DEMO presentational). Customer edita il record showcase. Related items si modificano dal gruppo indexed `Product · Related items (3)`.",
        "fields": [
            ("product.n",                   {"label": "Numero look (visible · es. 'Look 11 · Drop 02')", "type": "text", "max_length": 40}),
            ("product.name",                {"label": "Nome capo", "type": "text", "max_length": 120}),
            ("product.subtitle",            {"label": "Subtitle (materia · tecnica)", "type": "textarea", "max_length": 300}),
            ("product.price",               {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
            ("product.vat_note",            {"label": "Nota IVA / consegna", "type": "textarea", "max_length": 300}),
            ("product.tag",                 {"label": "Tag (editorial badge · es. 'Lista d'attesa · Drop 02')", "type": "text", "max_length": 120}),
            ("product.intro",               {"label": "Intro lunga", "type": "textarea", "max_length": 800}),
            ("product.gallery_caption_styling",  {"label": "Gallery caption · styling", "type": "text", "max_length": 160}),
            ("product.gallery_caption_photo",    {"label": "Gallery caption · foto", "type": "text", "max_length": 160}),
            ("product.gallery_caption_location", {"label": "Gallery caption · location", "type": "text", "max_length": 200}),
            ("product.info_label",          {"label": "Info rows · label", "type": "text", "max_length": 60}),
            ("product.size_label",          {"label": "Size · label", "type": "text", "max_length": 60}),
            ("product.color_label",         {"label": "Color · label", "type": "text", "max_length": 60}),
            ("product.edition_label",       {"label": "Edition · label", "type": "text", "max_length": 60}),
            ("product.edition_value",       {"label": "Edition · valore", "type": "text", "max_length": 160}),
            ("product.edition_note",        {"label": "Edition · nota estesa", "type": "textarea", "max_length": 400}),
            ("product.atelier_label",       {"label": "Atelier · label", "type": "text", "max_length": 60}),
            ("product.atelier_name",        {"label": "Atelier · nome", "type": "text", "max_length": 120}),
            ("product.atelier_founded",     {"label": "Atelier · data apertura", "type": "text", "max_length": 60}),
            ("product.atelier_text",        {"label": "Atelier · paragrafo", "type": "textarea", "max_length": 800}),
            ("product.atelier_portrait",    {"label": "Atelier · portrait URL (nested-dict scalar · RENDERED)", "type": "image", "max_length": 400}),
            ("product.buy_primary",         {"label": "Buy · CTA primaria (demo · no commerce state)", "type": "text", "max_length": 60}),
            ("product.buy_primary_href",    {"label": "Buy · CTA primaria destinazione", "type": "select",
                                                "choices": ["home", "collezione", "product", "maison", "lookbook", "contatti"]}),
            ("product.buy_secondary",       {"label": "Buy · CTA secondaria", "type": "text", "max_length": 60}),
            ("product.buy_note",            {"label": "Buy · nota", "type": "textarea", "max_length": 400}),
            ("product.care_label",          {"label": "Care · label", "type": "text", "max_length": 60}),
            ("product.care_intro",          {"label": "Care · intro", "type": "textarea", "max_length": 500}),
            ("product.provenance_label",    {"label": "Provenance · label", "type": "text", "max_length": 60}),
            ("product.provenance_heading",  {"label": "Provenance · titolo", "type": "richtext", "max_length": 220}),
            ("product.related_label",       {"label": "Related · label", "type": "text", "max_length": 60}),
            ("product.related_intro",       {"label": "Related · intro", "type": "textarea", "max_length": 400}),
        ],
    },
    {
        "id": "maison_page",
        "label": "Pagina Maison (about)",
        "icon": "bi-building",
        "region": ".fe-maison, .fe-maison-hero, .fe-statement, .fe-ateliers, .fe-direction, .fe-numbers, .fe-visit",
        "page": "maison",
        "keywords": ["maison", "about", "statement", "ateliers", "direction", "numbers", "visit"],
        "help": "Pagina about · hero · statement · ateliers intestazione · direction block (portrait nested-dict scalar · rendered) · numbers · visit block. Press items si modificano dal gruppo indexed `Maison · Press (5)`.",
        "fields": [
            ("maison.eyebrow",               {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("maison.headline",              {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("maison.intro",                 {"label": "Intro", "type": "textarea", "max_length": 800}),
            ("maison.statement_label",       {"label": "Statement · label", "type": "text", "max_length": 60}),
            ("maison.statement_heading",     {"label": "Statement · titolo", "type": "richtext", "max_length": 220}),
            ("maison.statement_text",        {"label": "Statement · paragrafo", "type": "textarea", "max_length": 700}),
            ("maison.ateliers_label",        {"label": "Ateliers · label", "type": "text", "max_length": 60}),
            ("maison.ateliers_heading",      {"label": "Ateliers · titolo", "type": "richtext", "max_length": 220}),
            ("maison.ateliers_intro",        {"label": "Ateliers · intro", "type": "textarea", "max_length": 500}),
            ("maison.direction_label",       {"label": "Direction · label", "type": "text", "max_length": 60}),
            ("maison.direction_name",        {"label": "Direction · nome", "type": "text", "max_length": 120}),
            ("maison.direction_role",        {"label": "Direction · ruolo", "type": "text", "max_length": 160}),
            ("maison.direction_text",        {"label": "Direction · paragrafo", "type": "textarea", "max_length": 700}),
            ("maison.direction_portrait",    {"label": "Direction · portrait URL (nested-dict scalar · RENDERED)", "type": "image", "max_length": 400}),
            ("maison.direction_quote",       {"label": "Direction · quote", "type": "textarea", "max_length": 500}),
            ("maison.direction_quote_attribution", {"label": "Direction · quote attribution", "type": "text", "max_length": 200}),
            ("maison.press_label",           {"label": "Press · label", "type": "text", "max_length": 60}),
            ("maison.press_heading",         {"label": "Press · titolo", "type": "richtext", "max_length": 220}),
            ("maison.numbers_label",         {"label": "Numbers · label", "type": "text", "max_length": 60}),
            ("maison.visit_label",           {"label": "Visit · label", "type": "text", "max_length": 60}),
            ("maison.visit_heading",         {"label": "Visit · titolo", "type": "richtext", "max_length": 220}),
            ("maison.visit_text",            {"label": "Visit · paragrafo", "type": "textarea", "max_length": 500}),
            ("maison.visit_primary",         {"label": "Visit · CTA primaria", "type": "text", "max_length": 60}),
            ("maison.visit_primary_href",    {"label": "Visit · CTA primaria destinazione", "type": "select",
                                                 "choices": ["home", "collezione", "product", "maison", "lookbook", "contatti"]}),
        ],
    },
    {
        "id": "lookbook_page",
        "label": "Pagina Lookbook (novel `lookbook` kind)",
        "icon": "bi-camera",
        "region": ".fe-lookbook, .fe-lookbook-hero, .fe-credits, .fe-looks, .fe-pullquote, .fe-notes, .fe-shop",
        "page": "lookbook",
        "keywords": ["lookbook", "issue", "credits", "looks", "pullquote", "notes", "shop"],
        "help": "Pagina lookbook editoriale · hero + issue number · pullquote + attribution · notes intro · shop CTA band. Credits rows, looks, notes_items si modificano dai gruppi indexed corrispondenti.",
        "fields": [
            ("lookbook.issue",               {"label": "Issue (es. 'Spring-Summer 2026')", "type": "text", "max_length": 120}),
            ("lookbook.issue_label",         {"label": "Issue · label", "type": "text", "max_length": 40}),
            ("lookbook.issue_n",             {"label": "Issue · numero (es. 'Issue 12')", "type": "text", "max_length": 40}),
            ("lookbook.eyebrow",             {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("lookbook.headline",            {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("lookbook.intro",               {"label": "Intro", "type": "textarea", "max_length": 800}),
            ("lookbook.credits_label",       {"label": "Credits · label", "type": "text", "max_length": 60}),
            ("lookbook.looks_label",         {"label": "Looks · label", "type": "text", "max_length": 60}),
            ("lookbook.looks_intro",         {"label": "Looks · intro", "type": "textarea", "max_length": 400}),
            ("lookbook.pullquote",           {"label": "Pullquote", "type": "textarea", "max_length": 500}),
            ("lookbook.pullquote_attribution", {"label": "Pullquote · attribution", "type": "text", "max_length": 200}),
            ("lookbook.notes_label",         {"label": "Notes · label", "type": "text", "max_length": 60}),
            ("lookbook.notes_intro",         {"label": "Notes · intro", "type": "textarea", "max_length": 500}),
            ("lookbook.shop_label",          {"label": "Shop · label", "type": "text", "max_length": 60}),
            ("lookbook.shop_heading",        {"label": "Shop · titolo", "type": "richtext", "max_length": 220}),
            ("lookbook.shop_intro",          {"label": "Shop · intro", "type": "textarea", "max_length": 500}),
            ("lookbook.shop_primary",        {"label": "Shop · CTA primaria", "type": "text", "max_length": 60}),
            ("lookbook.shop_primary_href",   {"label": "Shop · CTA primaria destinazione", "type": "select",
                                                 "choices": ["home", "collezione", "product", "maison", "lookbook", "contatti"]}),
            ("lookbook.shop_secondary",      {"label": "Shop · CTA secondaria", "type": "text", "max_length": 60}),
            ("lookbook.shop_secondary_href", {"label": "Shop · CTA secondaria destinazione", "type": "select",
                                                 "choices": ["home", "collezione", "product", "maison", "lookbook", "contatti"]}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti (private appointment · `contact` kind)",
        "icon": "bi-geo-alt",
        "region": ".fe-contact, .fe-contact-hero, .fe-maison-cards, .fe-faq",
        "page": "contatti",
        "keywords": ["contatti", "private", "maison-cards", "faq", "form-labels"],
        "help": "Pagina contatti · hero · form scalar labels (struttura form OUT · form_fields resta registry-only) · FAQ intestazione · card label. Le 3 maison cards e le 4 FAQ si modificano dai gruppi indexed corrispondenti.",
        "fields": [
            ("contatti.eyebrow",                 {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("contatti.headline",                {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("contatti.intro",                   {"label": "Intro", "type": "textarea", "max_length": 800}),
            ("contatti.form_section_label",      {"label": "Form section · label", "type": "text", "max_length": 60}),
            ("contatti.form_section_intro",      {"label": "Form section · intro", "type": "textarea", "max_length": 500}),
            ("contatti.form_helper_required",    {"label": "Form · helper required", "type": "text", "max_length": 120}),
            ("contatti.form_submit_button",      {"label": "Form · CTA submit", "type": "text", "max_length": 60}),
            ("contatti.form_submit_note",        {"label": "Form · nota post-submit", "type": "textarea", "max_length": 400}),
            ("contatti.card_label",              {"label": "Card · label (es. 'Le tre maison')", "type": "text", "max_length": 60}),
            ("contatti.faq_label",               {"label": "FAQ · label", "type": "text", "max_length": 60}),
        ],
    },
]


# ---------------------------------------------------------------------------
# A.16 · clinic (Salute · salute-studio-medico) — OPENS the medical-other
# family via staged dedicated-schema progression (extended to 3-phase
# variant: A.16 Salute opener · A.16b Benessere · A.16c Famiglia closure).
# First 3-template staged progression · guard-removal sub-recipe extended
# to 2 removal phases (wellness-out removed in A.16b · family-out removed
# in A.16c). Distinct skin folder (.cl-*) · 7 pages with 2 novel kinds
# (prevention + appointment). Clinic-shape distinctives: 18 raw icon_svg
# fields (OUT col-level · 5th OUT category precedent) · 2 form structures
# (contatti.form_fields + prenota.form_fields + prenota.form_sections ·
# Juris/Bottega/Luxe precedent) · 1 bool flag `prevenzione.packages.is_popular`
# (OUT col-level · preserves customer editability of popular_label text
# without adding bool field type · Luxe available precedent). Stringent
# IN col-level: num + popular_label IN (editorial visible numbering +
# badge · precedent chain Sapore→Brace→Bottega→Luxe→Salute). 15 image
# surfaces all rendered (1 scalar + 14 image-in-dict-row cells).
# ---------------------------------------------------------------------------
SALUTE_CLINIC_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".cl-nav, .cl-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "poliambulatorio", "tagline", "chrome"],
        "help": "Nome studio, iniziale crest, tagline, contatti (numero verde · email · indirizzo), orari sintetici, license sanitaria, label footer/contatti.",
        "fields": [
            ("site.logo_word",        {"label": "Nome studio", "type": "text", "max_length": 60,
                                         "placeholder": "SaluteVita"}),
            ("site.logo_initial",     {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.tag",              {"label": "Tagline (nav + strip)", "type": "text", "max_length": 160}),
            ("site.phone_label",      {"label": "Label · numero verde", "type": "text", "max_length": 60}),
            ("site.phone",            {"label": "Numero telefono (display)", "type": "text", "max_length": 40}),
            ("site.phone_tel",        {"label": "Numero telefono · tel: URL", "type": "text", "max_length": 40}),
            ("site.email",            {"label": "Email", "type": "text", "max_length": 120}),
            ("site.address",          {"label": "Indirizzo (una riga)", "type": "text", "max_length": 200}),
            ("site.hours_compact",    {"label": "Orari sintetici", "type": "text", "max_length": 160}),
            ("site.foot_extra_label", {"label": "Footer · titolo extra (es. 'Convenzioni')", "type": "text", "max_length": 60}),
            ("site.license",          {"label": "Licenza / P.IVA / iscrizione registro", "type": "text", "max_length": 240}),
            ("site.footer_intro",     {"label": "Intro footer", "type": "textarea", "max_length": 500}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".cl-hero",
        "page": "home",
        "keywords": ["hero", "headline", "eyebrow", "subhead", "cta", "trust"],
        "help": "Primo scroll della home · eyebrow + headline + subhead + CTA primaria (Prenota) + CTA secondaria (Numero verde) + trust note.",
        "fields": [
            ("home.eyebrow",        {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("home.headline",       {"label": "Headline", "type": "richtext", "max_length": 220,
                                       "help": "Consentiti i tag <em> per italici."}),
            ("home.subhead",        {"label": "Subhead", "type": "textarea", "max_length": 500}),
            ("home.primary_cta",    {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
            ("home.primary_href",   {"label": "CTA primaria · destinazione", "type": "select",
                                       "choices": ["home", "studio", "servizi", "prevenzione", "medici", "contatti", "prenota"]}),
            ("home.secondary_cta",  {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 80}),
            ("home.secondary_href", {"label": "CTA secondaria · destinazione", "type": "select",
                                       "choices": ["home", "studio", "servizi", "prevenzione", "medici", "contatti", "prenota"]}),
            ("home.trust_note",     {"label": "Trust note (sotto CTA)", "type": "text", "max_length": 160}),
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".cl-section",
        "page": "home",
        "keywords": ["specialties", "journey", "prevenzione", "team", "partners"],
        "help": "Fasce copy della home: specialties · journey · prevenzione cards · team ribbon · partners. Le liste indexed si modificano dai gruppi indexed corrispondenti.",
        "subgroups": [
            {"label": "Specialties intestazione", "fields": [
                ("home.specialties_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.specialties_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.specialties_intro",    {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Journey intestazione", "fields": [
                ("home.journey_label",        {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.journey_heading",      {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.journey_intro",        {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Prevenzione cards intestazione", "fields": [
                ("home.prevenzione_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.prevenzione_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.prevenzione_intro",    {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Team ribbon intestazione", "fields": [
                ("home.team_label",           {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.team_heading",         {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.team_intro",           {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.team_footnote_prefix", {"label": "Footnote prefix", "type": "text", "max_length": 200}),
                ("home.team_footnote_link",   {"label": "Footnote · link label", "type": "text", "max_length": 60}),
            ]},
            {"label": "Partners intestazione", "fields": [
                ("home.partners_label",       {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.partners_heading",     {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
        ],
    },
    {
        "id": "studio_page",
        "label": "Pagina Studio (about)",
        "icon": "bi-building",
        "region": ".cl-studio, .cl-studio-hero, .cl-values, .cl-photo, .cl-timeline",
        "page": "studio",
        "keywords": ["studio", "about", "values", "photo", "timeline"],
        "help": "Pagina about · hero · values intestazione · photo block (con scalar image rendered) · timeline intestazione. Values e timeline rows si modificano dai gruppi indexed corrispondenti.",
        "fields": [
            ("studio.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("studio.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("studio.intro",            {"label": "Intro", "type": "textarea", "max_length": 800}),
            ("studio.values_label",     {"label": "Values · label", "type": "text", "max_length": 60}),
            ("studio.values_heading",   {"label": "Values · titolo", "type": "richtext", "max_length": 220}),
            ("studio.photo_label",      {"label": "Photo · label", "type": "text", "max_length": 60}),
            ("studio.photo_heading",    {"label": "Photo · titolo", "type": "richtext", "max_length": 220}),
            ("studio.photo_body",       {"label": "Photo · paragrafo", "type": "textarea", "max_length": 600}),
            ("studio.photo_caption",    {"label": "Photo · didascalia", "type": "text", "max_length": 200}),
            ("studio.photo_src",        {"label": "Photo · URL (scalar rendered image)", "type": "image", "max_length": 400}),
            ("studio.timeline_label",   {"label": "Timeline · label", "type": "text", "max_length": 60}),
            ("studio.timeline_heading", {"label": "Timeline · titolo", "type": "richtext", "max_length": 220}),
        ],
    },
    {
        "id": "servizi_page",
        "label": "Pagina Servizi",
        "icon": "bi-clipboard-pulse",
        "region": ".cl-servizi, .cl-servizi-hero, .cl-pricelist, .cl-faq",
        "page": "servizi",
        "keywords": ["servizi", "services", "prezzi", "faq", "price"],
        "help": "Pagina servizi · hero · pricelist intestazione + label prezzo/CTA book · FAQ intestazione. Services e FAQs si modificano dai gruppi indexed (icon_svg + items OUT col-level).",
        "fields": [
            ("servizi.eyebrow",     {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("servizi.headline",    {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("servizi.intro",       {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("servizi.svc_label",   {"label": "Services · label", "type": "text", "max_length": 60}),
            ("servizi.svc_heading", {"label": "Services · titolo", "type": "richtext", "max_length": 220}),
            ("servizi.price_label", {"label": "Price · label (es. 'Prima visita')", "type": "text", "max_length": 60}),
            ("servizi.book_cta",    {"label": "Book · CTA etichetta", "type": "text", "max_length": 60}),
            ("servizi.faq_label",   {"label": "FAQ · label", "type": "text", "max_length": 60}),
            ("servizi.faq_heading", {"label": "FAQ · titolo", "type": "richtext", "max_length": 220}),
        ],
    },
    {
        "id": "prevenzione_page",
        "label": "Pagina Prevenzione (novel `prevention` kind)",
        "icon": "bi-heart-pulse",
        "region": ".cl-prevenzione, .cl-prevenzione-hero, .cl-packages, .cl-how",
        "page": "prevenzione",
        "keywords": ["prevenzione", "prevention", "check-up", "pacchetti"],
        "help": "Pagina check-up prevenzione · hero · packages intestazione + label duration/exams · how_steps intestazione. Packages si modificano dal gruppo indexed (is_popular + includes OUT col-level).",
        "fields": [
            ("prevenzione.eyebrow",         {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("prevenzione.headline",        {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("prevenzione.intro",           {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("prevenzione.pack_label",      {"label": "Packages · label", "type": "text", "max_length": 60}),
            ("prevenzione.pack_heading",    {"label": "Packages · titolo", "type": "richtext", "max_length": 220}),
            ("prevenzione.duration_label",  {"label": "Duration · label", "type": "text", "max_length": 60}),
            ("prevenzione.exams_label",     {"label": "Exams · label", "type": "text", "max_length": 60}),
            ("prevenzione.how_label",       {"label": "How · label", "type": "text", "max_length": 60}),
            ("prevenzione.how_heading",     {"label": "How · titolo", "type": "richtext", "max_length": 220}),
        ],
    },
    {
        "id": "medici_page",
        "label": "Pagina Medici (team)",
        "icon": "bi-people",
        "region": ".cl-medici, .cl-medici-hero, .cl-doctors, .cl-footnote",
        "page": "medici",
        "keywords": ["medici", "team", "doctors", "specialisti"],
        "help": "Pagina team · hero · book CTA · footnote. Doctor cards si modificano dal gruppo indexed (tags OUT col-level).",
        "fields": [
            ("medici.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("medici.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("medici.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("medici.book_cta",         {"label": "Book · CTA etichetta", "type": "text", "max_length": 80}),
            ("medici.footnote_strong",  {"label": "Footnote · testo forte", "type": "text", "max_length": 200}),
            ("medici.footnote_body",    {"label": "Footnote · paragrafo", "type": "textarea", "max_length": 500}),
            ("medici.footnote_link",    {"label": "Footnote · link label", "type": "text", "max_length": 80}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-geo-alt",
        "region": ".cl-contact, .cl-contact-hero, .cl-map, .cl-hours, .cl-access, .cl-form",
        "page": "contatti",
        "keywords": ["contatti", "mappa", "orari", "accesso", "form-labels"],
        "help": "Pagina contatti · hero · map labels + caption · hours intestazione · form scalar labels (struttura form OUT · contatti.form_fields registry-only).",
        "fields": [
            ("contatti.eyebrow",       {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("contatti.headline",      {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("contatti.intro",         {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("contatti.map_aria",      {"label": "Mappa · ARIA label", "type": "text", "max_length": 200}),
            ("contatti.map_stamp",     {"label": "Mappa · stamp (caption)", "type": "text", "max_length": 160}),
            ("contatti.address_label", {"label": "Address · label", "type": "text", "max_length": 60}),
            ("contatti.email_label",   {"label": "Email · label", "type": "text", "max_length": 60}),
            ("contatti.hours_heading", {"label": "Hours · titolo", "type": "text", "max_length": 120}),
            ("contatti.form_title",    {"label": "Form · titolo", "type": "text", "max_length": 120}),
            ("contatti.form_intro",    {"label": "Form · intro", "type": "textarea", "max_length": 400}),
            ("contatti.consent",       {"label": "Form · consenso privacy", "type": "textarea", "max_length": 500}),
            ("contatti.submit_label",  {"label": "Form · CTA submit", "type": "text", "max_length": 60}),
            ("contatti.form_note",     {"label": "Form · nota post-submit", "type": "textarea", "max_length": 300}),
        ],
    },
    {
        "id": "prenota_page",
        "label": "Pagina Prenota (novel `appointment` kind)",
        "icon": "bi-calendar-check",
        "region": ".cl-prenota, .cl-prenota-hero, .cl-form, .cl-help, .cl-alt",
        "page": "prenota",
        "keywords": ["prenota", "appointment", "form", "help", "numero-verde"],
        "help": "Pagina prenotazione · hero · form scalar labels (struttura form OUT · prenota.form_fields + prenota.form_sections registry-only) · help intestazione · alt block (numero verde). Help steps si modificano dal gruppo indexed.",
        "fields": [
            ("prenota.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("prenota.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("prenota.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("prenota.consent",          {"label": "Form · consenso privacy", "type": "textarea", "max_length": 500}),
            ("prenota.submit_label",     {"label": "Form · CTA submit", "type": "text", "max_length": 60}),
            ("prenota.form_submit_note", {"label": "Form · nota post-submit", "type": "text", "max_length": 200}),
            ("prenota.help_title",       {"label": "Help · titolo", "type": "text", "max_length": 160}),
            ("prenota.alt_title",        {"label": "Alt block · titolo", "type": "text", "max_length": 160}),
            ("prenota.alt_body",         {"label": "Alt block · paragrafo", "type": "textarea", "max_length": 500}),
        ],
    },
]


# ---------------------------------------------------------------------------
# A.16b · wellness (Benessere · benessere-centro-olistico) — middle phase
# of the medical-other 3-phase staged dedicated-schema progression (A.16
# Salute opener · A.16b Benessere middle · A.16c Famiglia closer).
# First 3-template staged progression continues here · removes wellness-
# out guard half of the dual-out planted in A.16 · family-out guard
# PRESERVED for A.16c. Distinct skin folder (.we-*) · 7 pages with
# novel `gallery` page kind + shared `appointment` kind with Salute.
# 19 image surfaces (3 scalar + 16 image-in-dict-row cells across 3
# lists) · ALL RENDERED (editorial olistico skin · no storage-only
# split). Stringent IN col-level extends to 6 archetypes: calendar
# day/num/month + pillars.init + packages.tag + journey.num IN (editorial
# visible · 6th archetype precedent). NOVEL Benessere-specific OUT
# decision: 4 bool flag cols (home.calendar + prenota.calendar ·
# has_slots + soldout · scheduler-state-like · Luxe/Salute precedent
# re-application). DEFERRED from first wave: home.ambients tuple-with-
# image (4 tiles · novel shape · ZERO precedent in existing archetypes ·
# whole list OUT · future expansion candidate after infra verification).
# ---------------------------------------------------------------------------
BENESSERE_WELLNESS_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".we-nav, .we-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "studio", "tagline", "chrome", "olistico"],
        "help": "Nome centro olistico, iniziale crest, tagline, contatti (telefono · email · indirizzo), orari sintetici, license (operatori certificati FIF/SIAF).",
        "fields": [
            ("site.logo_word",    {"label": "Nome centro", "type": "text", "max_length": 60,
                                     "placeholder": "Studio Armonia"}),
            ("site.logo_initial", {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.tag",          {"label": "Tagline (nav + strip)", "type": "text", "max_length": 160}),
            ("site.nav_cta",      {"label": "CTA nav · etichetta", "type": "text", "max_length": 60}),
            ("site.phone",        {"label": "Telefono", "type": "text", "max_length": 40}),
            ("site.email",        {"label": "Email", "type": "text", "max_length": 120}),
            ("site.address",      {"label": "Indirizzo (una riga)", "type": "text", "max_length": 200}),
            ("site.hours_compact",{"label": "Orari sintetici", "type": "text", "max_length": 160}),
            ("site.license",      {"label": "Licenza / certificazione", "type": "text", "max_length": 240}),
            ("site.footer_intro", {"label": "Intro footer", "type": "textarea", "max_length": 500}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".we-hero",
        "page": "home",
        "keywords": ["hero", "cover", "headline", "eyebrow", "subhead", "manifesto", "cta"],
        "help": "Primo scroll della home · scalar hero_image (rendered cover) · eyebrow + headline + subhead + CTAs + manifesto block.",
        "subgroups": [
            {"label": "Cover (rendered scalar image)", "fields": [
                ("home.hero_image",        {"label": "Hero image · URL (rendered)", "type": "image", "max_length": 400}),
            ]},
            {"label": "Hero copy", "fields": [
                ("home.eyebrow",           {"label": "Eyebrow", "type": "text", "max_length": 160}),
                ("home.headline",          {"label": "Headline", "type": "richtext", "max_length": 220,
                                              "help": "Consentiti i tag <em> per italici."}),
                ("home.subhead",           {"label": "Subhead", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "CTA hero", "fields": [
                ("home.primary_cta",       {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.secondary_cta",     {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
            ]},
            {"label": "Manifesto band", "fields": [
                ("home.manifesto_label",   {"label": "Manifesto · label", "type": "text", "max_length": 80}),
                ("home.manifesto",         {"label": "Manifesto · testo", "type": "textarea", "max_length": 700}),
                ("home.manifesto_signature", {"label": "Manifesto · firma", "type": "text", "max_length": 160}),
            ]},
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".we-section",
        "page": "home",
        "keywords": ["rituali", "benefits", "ambients", "therapists", "journey", "calendar", "press"],
        "help": "Fasce copy della home: rituali · benefits · ambients · therapists trio · journey · calendar · press. Le liste indexed si modificano dai gruppi indexed corrispondenti.",
        "subgroups": [
            {"label": "Rituali intestazione", "fields": [
                ("home.rituali_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.rituali_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.rituali_intro",    {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Benefits intestazione", "fields": [
                ("home.benefits_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.benefits_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.benefits_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Ambients intestazione", "fields": [
                ("home.ambients_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.ambients_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.ambients_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Therapists trio intestazione", "fields": [
                ("home.therapists_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.therapists_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.therapists_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Journey intestazione", "fields": [
                ("home.journey_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.journey_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.journey_intro",    {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Calendar intestazione", "fields": [
                ("home.calendar_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.calendar_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.calendar_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.calendar_cta",     {"label": "CTA · etichetta", "type": "text", "max_length": 80}),
            ]},
            {"label": "Press intestazione", "fields": [
                ("home.press_label",      {"label": "Eyebrow", "type": "text", "max_length": 80}),
            ]},
        ],
    },
    {
        "id": "filosofia_page",
        "label": "Pagina Filosofia (about)",
        "icon": "bi-compass",
        "region": ".we-filosofia, .we-filosofia-hero, .we-pillars, .we-photo, .we-timeline, .we-cta",
        "page": "filosofia",
        "keywords": ["filosofia", "about", "pillars", "photo", "timeline", "cta"],
        "help": "Pagina about · hero · pillars intestazione · photo block (scalar image rendered · caption · sub) · timeline intestazione · cta finale. Pillars e timeline rows si modificano dai gruppi indexed.",
        "fields": [
            ("filosofia.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("filosofia.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("filosofia.intro",            {"label": "Intro", "type": "textarea", "max_length": 800}),
            ("filosofia.photo_image",      {"label": "Photo · URL (scalar rendered image)", "type": "image", "max_length": 400}),
            ("filosofia.photo_caption",    {"label": "Photo · didascalia", "type": "text", "max_length": 200}),
            ("filosofia.photo_sub",        {"label": "Photo · subtitle", "type": "text", "max_length": 200}),
            ("filosofia.timeline_label",   {"label": "Timeline · label", "type": "text", "max_length": 60}),
            ("filosofia.timeline_heading", {"label": "Timeline · titolo", "type": "richtext", "max_length": 220}),
            ("filosofia.cta_label",        {"label": "CTA · label", "type": "text", "max_length": 60}),
            ("filosofia.cta_heading",      {"label": "CTA · titolo", "type": "richtext", "max_length": 220}),
            ("filosofia.cta_sub",          {"label": "CTA · subtitle", "type": "textarea", "max_length": 500}),
            ("filosofia.cta_primary",      {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
            ("filosofia.cta_secondary",    {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "rituali_page",
        "label": "Pagina Rituali (services)",
        "icon": "bi-flower1",
        "region": ".we-rituali, .we-rituali-hero, .we-treatments, .we-advice, .we-packages, .we-cta",
        "page": "rituali",
        "keywords": ["rituali", "services", "treatments", "advice", "packages"],
        "help": "Pagina rituali · hero · reserve label · advice intestazione · packages intestazione (2 pacchetti demo · `includes` nested list-of-str OUT) · cta finale. Treatments, advice, packages si modificano dai gruppi indexed.",
        "fields": [
            ("rituali.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("rituali.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("rituali.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("rituali.reserve_label",    {"label": "Reserve · label", "type": "text", "max_length": 60}),
            ("rituali.advice_label",     {"label": "Advice · label", "type": "text", "max_length": 60}),
            ("rituali.advice_heading",   {"label": "Advice · titolo", "type": "richtext", "max_length": 220}),
            ("rituali.packages_label",   {"label": "Packages · label", "type": "text", "max_length": 80}),
            ("rituali.packages_heading", {"label": "Packages · titolo", "type": "richtext", "max_length": 220}),
            ("rituali.packages_intro",   {"label": "Packages · intro", "type": "textarea", "max_length": 500}),
            ("rituali.cta_label",        {"label": "CTA · label", "type": "text", "max_length": 60}),
            ("rituali.cta_heading",      {"label": "CTA · titolo", "type": "richtext", "max_length": 220}),
            ("rituali.cta_sub",          {"label": "CTA · subtitle", "type": "textarea", "max_length": 500}),
            ("rituali.cta_primary",      {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
            ("rituali.cta_secondary",    {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "ambienti_page",
        "label": "Pagina Ambienti (novel `gallery` kind)",
        "icon": "bi-images",
        "region": ".we-ambienti, .we-ambienti-hero, .we-rooms, .we-cta",
        "page": "ambienti",
        "keywords": ["ambienti", "gallery", "rooms", "palazzo"],
        "help": "Pagina gallery (novel kind · plain string identifier · no dispatch) · hero · rooms intestazione implicita · cta finale. Rooms (8 sale) si modificano dal gruppo indexed.",
        "fields": [
            ("ambienti.eyebrow",       {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("ambienti.headline",      {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("ambienti.intro",         {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("ambienti.cta_label",     {"label": "CTA · label", "type": "text", "max_length": 60}),
            ("ambienti.cta_heading",   {"label": "CTA · titolo", "type": "richtext", "max_length": 220}),
            ("ambienti.cta_sub",       {"label": "CTA · subtitle", "type": "textarea", "max_length": 500}),
            ("ambienti.cta_primary",   {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
            ("ambienti.cta_secondary", {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "professionisti_page",
        "label": "Pagina Professionisti (team)",
        "icon": "bi-people",
        "region": ".we-professionisti, .we-professionisti-hero, .we-people, .we-philo, .we-cta",
        "page": "professionisti",
        "keywords": ["professionisti", "team", "operatori", "philosophy"],
        "help": "Pagina team · hero · philo quote block (attribution) · cta finale. People (5 operatori · `tags` nested list-of-str OUT) si modificano dal gruppo indexed.",
        "fields": [
            ("professionisti.eyebrow",     {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("professionisti.headline",    {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("professionisti.intro",       {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("professionisti.philo_label", {"label": "Philo · label", "type": "text", "max_length": 60}),
            ("professionisti.philo_quote", {"label": "Philo · quote", "type": "textarea", "max_length": 700}),
            ("professionisti.philo_attr",  {"label": "Philo · attribution", "type": "text", "max_length": 200}),
            ("professionisti.cta_label",   {"label": "CTA · label", "type": "text", "max_length": 60}),
            ("professionisti.cta_heading", {"label": "CTA · titolo", "type": "richtext", "max_length": 220}),
            ("professionisti.cta_primary", {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-geo-alt",
        "region": ".we-contact, .we-contact-hero, .we-map, .we-access, .we-hours, .we-form",
        "page": "contatti",
        "keywords": ["contatti", "mappa", "orari", "access", "form-labels"],
        "help": "Pagina contatti · hero · map scalar image · access intestazione · hours intestazione · form scalar labels (struttura form OUT: contatti.form_placeholders + form_helpers + form_fields tutti registry-only).",
        "fields": [
            ("contatti.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("contatti.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("contatti.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("contatti.map_image",        {"label": "Map · URL (scalar rendered image)", "type": "image", "max_length": 400}),
            ("contatti.access_label",     {"label": "Access · label", "type": "text", "max_length": 60}),
            ("contatti.form_title",       {"label": "Form · titolo", "type": "text", "max_length": 120}),
            ("contatti.form_intro",       {"label": "Form · intro", "type": "textarea", "max_length": 500}),
            ("contatti.form_consent",     {"label": "Form · consenso privacy", "type": "textarea", "max_length": 500}),
            ("contatti.form_submit_note", {"label": "Form · nota post-submit", "type": "textarea", "max_length": 300}),
            ("contatti.hours_label",      {"label": "Hours · label", "type": "text", "max_length": 60}),
            ("contatti.hours_heading",    {"label": "Hours · titolo", "type": "richtext", "max_length": 220}),
            ("contatti.hours_note",       {"label": "Hours · nota", "type": "textarea", "max_length": 500}),
        ],
    },
    {
        "id": "prenota_page",
        "label": "Pagina Prenota (novel `appointment` kind · shared con Salute)",
        "icon": "bi-calendar-check",
        "region": ".we-prenota, .we-prenota-hero, .we-calendar, .we-form, .we-why",
        "page": "prenota",
        "keywords": ["prenota", "appointment", "calendar", "form", "why"],
        "help": "Pagina prenotazione · hero · calendar intestazione + hint · form scalar labels (struttura form OUT: prenota.form_fields + form_sections registry-only · bool flags has_slots/soldout + nested list-of-str slots OUT col-level). Calendar e help_steps si modificano dal gruppo indexed.",
        "fields": [
            ("prenota.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("prenota.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("prenota.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("prenota.calendar_heading", {"label": "Calendar · titolo", "type": "richtext", "max_length": 220}),
            ("prenota.calendar_hint",    {"label": "Calendar · hint", "type": "text", "max_length": 200}),
            ("prenota.form_title",       {"label": "Form · titolo", "type": "richtext", "max_length": 160}),
            ("prenota.form_side_note",   {"label": "Form side · nota", "type": "textarea", "max_length": 500}),
            ("prenota.form_side_small",  {"label": "Form side · small", "type": "text", "max_length": 100}),
            ("prenota.why_label",        {"label": "Why · label", "type": "text", "max_length": 80}),
            ("prenota.consent",          {"label": "Form · consenso privacy", "type": "textarea", "max_length": 500}),
            ("prenota.submit_label",     {"label": "Form · CTA submit", "type": "text", "max_length": 60}),
            ("prenota.form_submit_note", {"label": "Form · nota post-submit", "type": "text", "max_length": 200}),
            ("prenota.footnote",         {"label": "Footnote", "type": "textarea", "max_length": 500}),
        ],
    },
]


# ---------------------------------------------------------------------------
# A.16c · family (Famiglia · famiglia-pediatria) — CLOSER phase of the
# medical-other 3-phase staged dedicated-schema progression (A.16 Salute
# opener · A.16b Benessere middle · A.16c Famiglia closer). **CLOSES the
# medical-other family** · removes family-out guard residuo from A.16
# Salute tests (6th precedent of guard removal pattern · completes the
# 2-removal-phase sub-recipe variant established in A.16b). Distinct
# skin folder (.fm-*) · 6 pages with novel `faq` page kind · NO
# `appointment` kind (phone-and-WhatsApp CTA pattern). 16 image surfaces
# all rendered (3 scalar + 13 image-in-dict-row cells across 3 lists).
# **DEEP-PATH shape `crescita.topics[].items`** (4 sections × 4 tuples ×
# 2 cols = 32 cells · Sapore `menu.sections.{i}.dishes` precedent mirror ·
# mechanical reuse of f66ac24 render-side contract-alignment fix · zero
# new infra needed · 4 sub-path entries mirror Sapore's 5). Novel col
# name `src` (vs prior `image`/`portrait`/`avatar`) on home.gallery —
# mechanical reuse via col registration. Zero raw SVG (icons are short
# Bootstrap text refs · customer-editable IN). Zero bool flags (no
# scheduler-state). NO `form_fields` list-of-dict (form exposed as
# flat scalars · simpler than Benessere).
# ---------------------------------------------------------------------------
FAMIGLIA_FAMILY_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".fm-nav, .fm-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "studio", "tagline", "chrome", "pediatria"],
        "help": "Nome studio pediatrico, iniziale crest, tagline, contatti (telefono · WhatsApp · email · indirizzo · emergenze), orari sintetici, license (P.IVA · iscrizione OMCeO).",
        "fields": [
            ("site.logo_word",      {"label": "Nome studio", "type": "text", "max_length": 60,
                                       "placeholder": "Pediatria Famiglia Plus"}),
            ("site.logo_initial",   {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.tag",            {"label": "Tagline (nav + strip)", "type": "text", "max_length": 160}),
            ("site.nav_cta_wa",     {"label": "CTA nav · etichetta WhatsApp", "type": "text", "max_length": 40}),
            ("site.phone",          {"label": "Telefono (display)", "type": "text", "max_length": 40}),
            ("site.phone_tel",      {"label": "Telefono · tel: URL", "type": "text", "max_length": 40}),
            ("site.whatsapp",       {"label": "WhatsApp (display)", "type": "text", "max_length": 40}),
            ("site.whatsapp_link",  {"label": "WhatsApp · URL completo", "type": "url", "max_length": 300}),
            ("site.email",          {"label": "Email", "type": "text", "max_length": 120}),
            ("site.address",        {"label": "Indirizzo (una riga)", "type": "text", "max_length": 200}),
            ("site.emergency_tel",  {"label": "Urgenze · tel: URL", "type": "text", "max_length": 40}),
            ("site.hours_compact",  {"label": "Orari sintetici", "type": "text", "max_length": 160}),
            ("site.license",        {"label": "Licenza / P.IVA / iscrizione OMCeO", "type": "text", "max_length": 240}),
            ("site.footer_intro",   {"label": "Intro footer", "type": "textarea", "max_length": 500}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".fm-hero",
        "page": "home",
        "keywords": ["hero", "headline", "eyebrow", "subhead", "cta", "ribbon", "stamp"],
        "help": "Primo scroll della home · scalar hero_image (rendered) + alt · eyebrow + headline + subhead + CTA primaria (telefono) + CTA secondaria (WhatsApp) + ribbon convenzionato + stamp pediatra di turno.",
        "subgroups": [
            {"label": "Cover (rendered scalar image)", "fields": [
                ("home.hero_image",     {"label": "Hero image · URL (rendered)", "type": "image", "max_length": 400}),
                ("home.hero_image_alt", {"label": "Hero image · alt text", "type": "textarea", "max_length": 300}),
            ]},
            {"label": "Hero copy", "fields": [
                ("home.eyebrow",        {"label": "Eyebrow", "type": "text", "max_length": 160}),
                ("home.headline",       {"label": "Headline", "type": "richtext", "max_length": 220,
                                           "help": "Consentiti i tag <em> per italici."}),
                ("home.subhead",        {"label": "Subhead", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "CTA hero", "fields": [
                ("home.primary_cta",    {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
                ("home.secondary_cta",  {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
            ]},
            {"label": "Ribbon + stamp decorative", "fields": [
                ("home.hero_ribbon",         {"label": "Ribbon ('Convenzionato SSN')", "type": "text", "max_length": 80}),
                ("home.hero_stamp_initial",  {"label": "Stamp · iniziale pediatra", "type": "text", "max_length": 4}),
                ("home.hero_stamp_name",     {"label": "Stamp · nome pediatra in turno", "type": "text", "max_length": 120}),
                ("home.hero_stamp_meta",     {"label": "Stamp · meta (orario)", "type": "text", "max_length": 160}),
            ]},
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".fm-section",
        "page": "home",
        "keywords": ["team", "journey", "faq", "gallery", "hours", "urgency", "cta"],
        "help": "Fasce copy della home: team ribbon · journey · FAQ · gallery · hours · urgency · CTA finale. Le liste indexed si modificano dai gruppi indexed corrispondenti.",
        "subgroups": [
            {"label": "Team ribbon intestazione", "fields": [
                ("home.team_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.team_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.team_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
                ("home.team_note",    {"label": "Nota team (professioniste extra)", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Journey intestazione", "fields": [
                ("home.journey_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.journey_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.journey_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "FAQ intestazione", "fields": [
                ("home.faq_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.faq_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.faq_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Gallery intestazione", "fields": [
                ("home.gallery_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.gallery_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.gallery_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Hours intestazione", "fields": [
                ("home.hours_heading", {"label": "Hours · titolo", "type": "text", "max_length": 120}),
            ]},
            {"label": "Urgency band", "fields": [
                ("home.urgency_label", {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.urgency_title", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.urgency_text",  {"label": "Paragrafo", "type": "textarea", "max_length": 500}),
                ("home.urgency_phone", {"label": "Urgenze · numero display", "type": "text", "max_length": 40}),
            ]},
            {"label": "CTA finale", "fields": [
                ("home.cta_heading",      {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.cta_lead",         {"label": "Lead", "type": "textarea", "max_length": 500}),
                ("home.cta_phone_label",  {"label": "CTA · telefono label", "type": "text", "max_length": 60}),
                ("home.cta_or",           {"label": "CTA · connettore (es. 'oppure')", "type": "text", "max_length": 20}),
                ("home.cta_wa_label",     {"label": "CTA · WhatsApp label", "type": "text", "max_length": 60}),
            ]},
        ],
    },
    {
        "id": "studio_page",
        "label": "Pagina Studio (about)",
        "icon": "bi-building",
        "region": ".fm-studio, .fm-studio-hero, .fm-values, .fm-photo, .fm-history, .fm-cta",
        "page": "studio",
        "keywords": ["studio", "about", "values", "photo", "history", "cta"],
        "help": "Pagina about · hero · values intestazione · photo block (scalar image rendered · caption) · history intestazione · cta finale. Values e history rows si modificano dai gruppi indexed.",
        "fields": [
            ("studio.eyebrow",              {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("studio.headline",             {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("studio.intro",                {"label": "Intro", "type": "textarea", "max_length": 800}),
            ("studio.studio_image",         {"label": "Photo · URL (scalar rendered image)", "type": "image", "max_length": 400}),
            ("studio.studio_image_caption", {"label": "Photo · didascalia", "type": "text", "max_length": 200}),
            ("studio.history_label",        {"label": "History · label", "type": "text", "max_length": 60}),
            ("studio.history_heading",      {"label": "History · titolo", "type": "richtext", "max_length": 220}),
            ("studio.history_intro",        {"label": "History · intro", "type": "textarea", "max_length": 500}),
            ("studio.cta_heading",          {"label": "CTA · titolo", "type": "richtext", "max_length": 220}),
            ("studio.cta_lead",             {"label": "CTA · lead", "type": "textarea", "max_length": 500}),
            ("studio.cta_primary_label",    {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
            ("studio.cta_secondary_label",  {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "visite_page",
        "label": "Pagina Visite (services)",
        "icon": "bi-clipboard-heart",
        "region": ".fm-visite, .fm-visite-hero, .fm-visits, .fm-tips, .fm-cta",
        "page": "visite",
        "keywords": ["visite", "services", "visits", "tips", "cta"],
        "help": "Pagina servizi · hero · tips intestazione · cta finale. Visits e tips si modificano dai gruppi indexed.",
        "fields": [
            ("visite.eyebrow",              {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("visite.headline",             {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("visite.intro",                {"label": "Intro", "type": "textarea", "max_length": 800}),
            ("visite.tips_label",           {"label": "Tips · label", "type": "text", "max_length": 60}),
            ("visite.tips_heading",         {"label": "Tips · titolo", "type": "richtext", "max_length": 220}),
            ("visite.tips_intro",           {"label": "Tips · intro", "type": "textarea", "max_length": 500}),
            ("visite.cta_heading",          {"label": "CTA · titolo", "type": "richtext", "max_length": 220}),
            ("visite.cta_primary_label",    {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
            ("visite.cta_secondary_label",  {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "crescita_page",
        "label": "Pagina Crescita (novel `faq` kind · DEEP-PATH)",
        "icon": "bi-question-circle",
        "region": ".fm-crescita, .fm-crescita-hero, .fm-topics, .fm-materials, .fm-cta",
        "page": "crescita",
        "keywords": ["crescita", "faq", "topics", "materials", "cta"],
        "help": "Pagina FAQ (novel kind · plain string identifier · no dispatch) · hero · materials intestazione · cta finale. Topics (4 aree) si modificano dal gruppo indexed parent · le 4 Q&A per topic si modificano dai 4 gruppi DEEP-PATH `crescita.topics.{i}.items` (mechanical reuse di Sapore menu.sections.{i}.dishes · f66ac24 render-side fix).",
        "fields": [
            ("crescita.eyebrow",              {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("crescita.headline",             {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("crescita.intro",                {"label": "Intro", "type": "textarea", "max_length": 800}),
            ("crescita.materials_label",      {"label": "Materials · label", "type": "text", "max_length": 60}),
            ("crescita.materials_heading",    {"label": "Materials · titolo", "type": "richtext", "max_length": 220}),
            ("crescita.materials_intro",      {"label": "Materials · intro", "type": "textarea", "max_length": 500}),
            ("crescita.cta_heading",          {"label": "CTA · titolo", "type": "richtext", "max_length": 220}),
            ("crescita.cta_lead",             {"label": "CTA · lead", "type": "textarea", "max_length": 500}),
            ("crescita.cta_primary_label",    {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
            ("crescita.cta_secondary_label",  {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
        ],
    },
    {
        "id": "pediatre_page",
        "label": "Pagina Pediatre (team)",
        "icon": "bi-people",
        "region": ".fm-pediatre, .fm-pediatre-hero, .fm-doctors, .fm-extra",
        "page": "pediatre",
        "keywords": ["pediatre", "team", "doctors", "extra"],
        "help": "Pagina team · hero · extra block (professioniste non-pediatriche). Doctors (4 pediatre) si modificano dal gruppo indexed (`specs` nested list-of-str OUT).",
        "fields": [
            ("pediatre.eyebrow",     {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("pediatre.headline",    {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("pediatre.intro",       {"label": "Intro", "type": "textarea", "max_length": 800}),
            ("pediatre.extra_title", {"label": "Extra · titolo", "type": "text", "max_length": 200}),
            ("pediatre.extra_text",  {"label": "Extra · paragrafo", "type": "textarea", "max_length": 500}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-geo-alt",
        "region": ".fm-contact, .fm-contact-hero, .fm-travel, .fm-hours, .fm-form",
        "page": "contatti",
        "keywords": ["contatti", "travel", "orari", "form-labels"],
        "help": "Pagina contatti · hero · address block · map scalar image · travel intestazione · hours intestazione · form scalar labels (struttura form OUT · contatti.form_placeholders + contatti.form_helpers nested-dicts registry-only). NO list-of-dict form_fields (form shown con scalari label_*).",
        "fields": [
            ("contatti.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 160}),
            ("contatti.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("contatti.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("contatti.address_label",    {"label": "Address · label", "type": "text", "max_length": 60}),
            ("contatti.address_line",     {"label": "Address · via", "type": "text", "max_length": 200}),
            ("contatti.address_sub",      {"label": "Address · sub (cap · quartiere)", "type": "text", "max_length": 200}),
            ("contatti.phone_label",      {"label": "Phone · label", "type": "text", "max_length": 60}),
            ("contatti.email_label",      {"label": "Email · label", "type": "text", "max_length": 60}),
            ("contatti.map_image",        {"label": "Map · URL (scalar rendered image)", "type": "image", "max_length": 400}),
            ("contatti.travel_heading",   {"label": "Travel · titolo", "type": "text", "max_length": 120}),
            ("contatti.hours_heading",    {"label": "Hours · titolo", "type": "text", "max_length": 120}),
            ("contatti.form_title",       {"label": "Form · titolo", "type": "text", "max_length": 120}),
            ("contatti.form_intro",       {"label": "Form · intro", "type": "textarea", "max_length": 500}),
            ("contatti.label_parent_name",{"label": "Form · label nome genitore", "type": "text", "max_length": 80}),
            ("contatti.label_child_age",  {"label": "Form · label età bambino", "type": "text", "max_length": 80}),
            ("contatti.label_reason",     {"label": "Form · label motivo", "type": "text", "max_length": 80}),
            ("contatti.form_consent",     {"label": "Form · consenso privacy", "type": "textarea", "max_length": 500}),
            ("contatti.form_submit_note", {"label": "Form · nota post-submit", "type": "textarea", "max_length": 300}),
        ],
    },
]


# ---------------------------------------------------------------------------
# A.17 · Aura (agency-digital-studio) — single-template closer of the
# agency-secondary family. Pure 3-file enrollment surface (schema +
# _base.html atomic fixes + tests). 6 pages (home · studio · capabilities
# · lavori · sprint · brief) + 1 derived kind (project_detail via
# posts[]). Posts stay registry-only per the 7th uniform enforcement of
# the per-item content policy (after Chiara + Pixel + Sapore + Brace +
# Bottega + Luxe · detail-page editing is OUT of scope).
#
# **Form-structure scaffolding on the `brief` page stays OUT entire** ·
# 5th precedent after Gusto/Juris/Casa/Villa:
#   • brief.step1 / step2 / step3  (nested-dict form step metadata)
#   • brief.labels / placeholders  (nested-dict form field labels)
#   • brief.scope_options           (flat list-of-str · select options)
#   • brief.slots                   (tuple list · id=form-option-value
#                                    is structural · despite the label
#                                    being editorially visible, the list
#                                    identity — which days/hours are
#                                    offered — is a form-schema concern
#                                    requiring a calendar integration,
#                                    not a customer copy edit)
# brief.form_submit_label / submit_note / response_rows remain IN as
# editorial button copy + SLA response table.
#
# Flat list-of-str stay OUT entire (established policy):
#   • site.foot_stack_marquee / foot_stack_rows
#   • studio.story_paragraphs
#   • lavori.tabs
#   • brief.scope_options
#
# Nested list-of-str inside dict rows stay OUT col-level (Juris
# precedent + 6-archetype chain):
#   • home.capab_cards.{i}.tags
#   • home.work_cards.{i}.stack
#   • studio.team.{i}.stack
#   • capabilities.capabilities.{i}.scope + .stack
#   • capabilities.engagement_tiles.{i}.includes
#   • posts.{i}.problem_paragraphs / solution_paragraphs (posts registry-only)
#
# Stringent IN (technical-looking but customer-facing · 8th precedent):
#   • site.foot_boot_line     ("aura.studio · uptime 99.98 · ...")
#   • site.foot_current_sprint ("sprint 07/Q2 · live")
#   • site.sprint_chip         navbar chip
#   • home.sprints.{i}.output  ("OUT · brief + backlog")
#
# 12 image surfaces all image-in-dict-row (no scalar top-level · no
# nested-dict scalar · no deep-path):
#   • home.work_cards.{i}.cover        × 3
#   • studio.team.{i}.portrait         × 3
#   • lavori.projects.{i}.cover        × 6
# Posts `cover_image` × 6 stays registry-only (not exposed).
#
# Zero raw SVG · zero bool flags · zero scheduler-state · zero novel
# page kinds · zero novel shapes · zero mutable repeater · zero image
# per-locale · zero commerce/clinic boundary.
# ---------------------------------------------------------------------------

AURA_AGENCY_DIGITAL_STUDIO_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".au-nav, .au-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "studio", "tagline", "chrome", "nav cta", "footer"],
        "help": "Nome studio, tagline, navbar chip (sprint live), CTA header, dati di contatto, voce footer e micro-copy tecnico del footer (shiplog · current sprint · stack labels · boot line).",
        "fields": [
            ("site.logo_word",          {"label": "Nome studio (logo word)", "type": "text", "max_length": 60,
                                           "placeholder": "Aura"}),
            ("site.tag",                {"label": "Tagline (sotto nav · footer)", "type": "text", "max_length": 120}),
            ("site.sprint_chip",        {"label": "Navbar chip (sprint live · stringent IN)", "type": "text", "max_length": 60,
                                           "help": "Chip editoriale vicino al logo (es. 'Sprint 07/Q2 · live')."}),
            ("site.nav_cta",            {"label": "CTA header · etichetta", "type": "text", "max_length": 40}),
            ("site.inquiry_page_slug",  {"label": "CTA header · pagina di destinazione", "type": "select",
                                           "choices": ["home", "studio", "capabilities", "lavori", "sprint", "brief"]}),
            ("site.phone",              {"label": "Telefono", "type": "text", "max_length": 40}),
            ("site.email",              {"label": "Email", "type": "text", "max_length": 120}),
            ("site.address",            {"label": "Indirizzo", "type": "text", "max_length": 200}),
            ("site.hours_compact",      {"label": "Orari sintetici", "type": "text", "max_length": 120}),
            ("site.license",            {"label": "Licenza / P.IVA", "type": "text", "max_length": 200}),
            ("site.footer_intro",       {"label": "Intro footer", "type": "textarea", "max_length": 500}),
            ("site.foot_shiplog_label", {"label": "Footer · label shiplog", "type": "text", "max_length": 60}),
            ("site.foot_current_sprint",{"label": "Footer · current sprint (stringent IN)", "type": "text", "max_length": 60}),
            ("site.foot_studio_label",  {"label": "Footer · label studio", "type": "text", "max_length": 40}),
            ("site.foot_stack_label",   {"label": "Footer · label stack", "type": "text", "max_length": 40}),
            ("site.foot_boot_line",     {"label": "Footer · boot line (stringent IN · uptime + last deploy)",
                                           "type": "textarea", "max_length": 300}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-stars",
        "region": ".au-hero",
        "page": "home",
        "keywords": ["hero", "headline", "chip", "intro", "cta home", "primo scroll"],
        "help": "Primo scroll della home: chip disponibilità · headline · intro · CTA primaria (prenota call) · CTA secondaria (lavori).",
        "fields": [
            ("home.chip",            {"label": "Chip (es. '3 slot disponibili · Q3 2026')", "type": "text", "max_length": 100}),
            ("home.headline",        {"label": "Headline", "type": "richtext", "max_length": 220,
                                       "help": "Consentiti i tag <em> per italici."}),
            ("home.intro",           {"label": "Intro", "type": "textarea", "max_length": 700}),
            ("home.primary_cta",     {"label": "CTA primaria · etichetta", "type": "text", "max_length": 40}),
            ("home.primary_href",    {"label": "CTA primaria · pagina destinazione", "type": "select",
                                       "choices": ["home", "studio", "capabilities", "lavori", "sprint", "brief"]}),
            ("home.secondary_cta",   {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 40}),
            ("home.secondary_href",  {"label": "CTA secondaria · pagina destinazione", "type": "select",
                                       "choices": ["home", "studio", "capabilities", "lavori", "sprint", "brief"]}),
        ],
    },
    {
        "id": "console_home",
        "label": "Console dashboard · home",
        "icon": "bi-speedometer2",
        "region": ".au-console",
        "page": "home",
        "keywords": ["console", "dashboard", "metric", "kpi", "home"],
        "help": "Il tile dashboard sotto l'hero della home · path · status chip · metrica principale · meta sprint corrente. Le 4 righe KPI si modificano dal gruppo indexed `home.console.kpi`.",
        "fields": [
            ("home.console.path",           {"label": "Path dashboard (es. 'aura.studio/clients/...')", "type": "text", "max_length": 160}),
            ("home.console.status_chip",    {"label": "Status chip (es. 'LIVE · sprint 07/Q2')", "type": "text", "max_length": 80}),
            ("home.console.primary_metric", {"label": "Metrica primaria (es. '+34%')", "type": "text", "max_length": 40}),
            ("home.console.primary_label",  {"label": "Metrica primaria · label", "type": "text", "max_length": 200}),
            ("home.console.meta_label",     {"label": "Meta · label (es. 'Sprint corrente')", "type": "text", "max_length": 60}),
            ("home.console.meta_value",     {"label": "Meta · value (es. '07/Q2 · week 2 of 2')", "type": "text", "max_length": 80}),
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".au-section",
        "page": "home",
        "keywords": ["capab", "sprint", "work", "metric strip", "cta home", "bands"],
        "help": "Intestazioni delle fasce copy della home · capabilities mini · sprint strip · lavori cards · CTA finale. Le liste (capab_cards · sprints · work_cards · metric_strip) si modificano dai gruppi indexed.",
        "subgroups": [
            {"label": "Capabilities · intestazione", "fields": [
                ("home.capab_label",    {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.capab_heading",  {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.capab_intro",    {"label": "Intro", "type": "textarea", "max_length": 600}),
            ]},
            {"label": "Sprint strip · intestazione", "fields": [
                ("home.sprint_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.sprint_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.sprint_intro",   {"label": "Intro", "type": "textarea", "max_length": 600}),
            ]},
            {"label": "Lavori cards · intestazione", "fields": [
                ("home.work_label",     {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("home.work_heading",   {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.work_intro",     {"label": "Intro", "type": "textarea", "max_length": 600}),
                ("home.work_page_slug", {"label": "Link al listing lavori · pagina", "type": "select",
                                           "choices": ["home", "studio", "capabilities", "lavori", "sprint", "brief"]}),
            ]},
            {"label": "CTA finale home", "fields": [
                ("home.cta_label",      {"label": "Eyebrow", "type": "text", "max_length": 60}),
                ("home.cta_heading",    {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("home.cta_sub",        {"label": "Descrizione", "type": "textarea", "max_length": 500}),
                ("home.cta_chip",       {"label": "Chip (es. '30 min · zero committment')", "type": "text", "max_length": 80}),
                ("home.cta_primary",    {"label": "CTA · etichetta", "type": "text", "max_length": 40}),
            ]},
        ],
    },
    {
        "id": "studio_page",
        "label": "Pagina Studio (about)",
        "icon": "bi-building",
        "region": ".au-section",
        "page": "studio",
        "keywords": ["chi siamo", "about", "team", "storia", "valori", "bio"],
        "help": "About dello studio · chip · headline · standfirst · intestazioni di saggio storia · team · valori. Le liste (facts · team · values) si modificano dai gruppi indexed. story_paragraphs (flat list-of-str · saggio) stays OUT entire.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("studio.chip",       {"label": "Chip", "type": "text", "max_length": 120}),
                ("studio.headline",   {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("studio.standfirst", {"label": "Standfirst", "type": "textarea", "max_length": 800}),
            ]},
            {"label": "Story · saggio intestazione", "fields": [
                ("studio.story_label",   {"label": "Eyebrow saggio", "type": "text", "max_length": 80}),
                ("studio.story_heading", {"label": "Titolo saggio", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Team · intestazione", "fields": [
                ("studio.team_label",   {"label": "Eyebrow team", "type": "text", "max_length": 80}),
                ("studio.team_heading", {"label": "Titolo team", "type": "richtext", "max_length": 220}),
                ("studio.team_intro",   {"label": "Intro team", "type": "textarea", "max_length": 500}),
            ]},
            {"label": "Valori · intestazione", "fields": [
                ("studio.values_label",   {"label": "Eyebrow valori", "type": "text", "max_length": 80}),
                ("studio.values_heading", {"label": "Titolo valori", "type": "richtext", "max_length": 220}),
            ]},
        ],
    },
    {
        "id": "capabilities_page",
        "label": "Pagina Capabilities (services)",
        "icon": "bi-gem",
        "region": ".au-section",
        "page": "capabilities",
        "keywords": ["capabilities", "services", "discipline", "engagement", "ingaggio"],
        "help": "Pagina servizi · chip · headline · standfirst · intestazione tile di ingaggio · CTA finale. Le liste (capabilities · engagement_tiles) si modificano dai gruppi indexed. Nested list-of-str (scope · stack · includes) stay OUT col-level.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("capabilities.chip",       {"label": "Chip", "type": "text", "max_length": 120}),
                ("capabilities.headline",   {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("capabilities.standfirst", {"label": "Standfirst", "type": "textarea", "max_length": 800}),
            ]},
            {"label": "Engagement tiles · intestazione", "fields": [
                ("capabilities.engagement_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("capabilities.engagement_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("capabilities.engagement_intro",   {"label": "Intro", "type": "textarea", "max_length": 600}),
            ]},
            {"label": "CTA finale", "fields": [
                ("capabilities.cta_label",   {"label": "Eyebrow", "type": "text", "max_length": 60}),
                ("capabilities.cta_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("capabilities.cta_primary", {"label": "CTA · etichetta", "type": "text", "max_length": 40}),
            ]},
        ],
    },
    {
        "id": "lavori_page",
        "label": "Pagina Lavori (project_list)",
        "icon": "bi-images",
        "region": ".au-section",
        "page": "lavori",
        "keywords": ["lavori", "progetti", "archivio", "portfolio", "velocity"],
        "help": "Pagina progetti · chip · headline · standfirst · counter archivio · intestazione velocity. La lista projects si modifica dal gruppo indexed · velocity_stats anche. Tabs (flat list-of-str · filtri) stays OUT entire. Per-project detail (posts[]) stays registry-only (7th uniform enforcement).",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("lavori.chip",       {"label": "Chip", "type": "text", "max_length": 120}),
                ("lavori.headline",   {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("lavori.standfirst", {"label": "Standfirst", "type": "textarea", "max_length": 800}),
            ]},
            {"label": "Tabs · counter archivio", "fields": [
                ("lavori.tabs_count_label", {"label": "Label counter (es. '// totali archivio')", "type": "text", "max_length": 60}),
                ("lavori.tabs_count_value", {"label": "Value counter (es. '047')", "type": "text", "max_length": 20}),
            ]},
            {"label": "Velocity · intestazione", "fields": [
                ("lavori.velocity_label",   {"label": "Eyebrow", "type": "text", "max_length": 60}),
                ("lavori.velocity_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("lavori.velocity_body",    {"label": "Body", "type": "textarea", "max_length": 700}),
            ]},
        ],
    },
    {
        "id": "sprint_page",
        "label": "Pagina Sprint (process)",
        "icon": "bi-diagram-3",
        "region": ".au-section",
        "page": "sprint",
        "keywords": ["sprint", "process", "fasi", "mindset", "stack", "delivery"],
        "help": "Pagina metodologia · chip · headline · standfirst · intestazione mindset + stack. Le liste (sprints · mindset_cards · stack_tiles) si modificano dai gruppi indexed. deliverables nested list-of-str stays OUT col-level.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("sprint.chip",       {"label": "Chip", "type": "text", "max_length": 120}),
                ("sprint.headline",   {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("sprint.standfirst", {"label": "Standfirst", "type": "textarea", "max_length": 800}),
            ]},
            {"label": "Mindset · intestazione", "fields": [
                ("sprint.mindset_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("sprint.mindset_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
            ]},
            {"label": "Stack · intestazione", "fields": [
                ("sprint.stack_label",   {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("sprint.stack_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("sprint.stack_intro",   {"label": "Intro", "type": "textarea", "max_length": 500}),
            ]},
        ],
    },
    {
        "id": "brief_page",
        "label": "Pagina Brief (contact)",
        "icon": "bi-envelope",
        "region": ".au-section",
        "page": "brief",
        "keywords": ["brief", "contatti", "form", "call", "async", "response"],
        "help": "Pagina contatti · chip · headline · standfirst · form intestazioni (submit · note) · async block · response SLA intestazione · footer boot. Form scaffolding (step1/2/3 · labels · placeholders · scope_options · slots) stays OUT entire — form structure · 5th precedent dopo Gusto/Juris/Casa/Villa. response_rows si modifica dal gruppo indexed.",
        "subgroups": [
            {"label": "Intestazione", "fields": [
                ("brief.chip",       {"label": "Chip (es. '3 slot aperti · Q3 2026')", "type": "text", "max_length": 120}),
                ("brief.headline",   {"label": "Headline", "type": "richtext", "max_length": 220}),
                ("brief.standfirst", {"label": "Standfirst", "type": "textarea", "max_length": 800}),
            ]},
            {"label": "Form · intestazione + submit", "fields": [
                ("brief.form_heading",      {"label": "Titolo form (es. '// brief intake · 3 step')", "type": "text", "max_length": 120}),
                ("brief.form_submit_label", {"label": "Submit · etichetta pulsante", "type": "text", "max_length": 40}),
                ("brief.form_submit_note",  {"label": "Submit · nota sotto il pulsante", "type": "textarea", "max_length": 300}),
            ]},
            {"label": "Async block", "fields": [
                ("brief.async_label",   {"label": "Eyebrow", "type": "text", "max_length": 60}),
                ("brief.async_heading", {"label": "Titolo", "type": "richtext", "max_length": 220}),
                ("brief.async_body",    {"label": "Body", "type": "textarea", "max_length": 500}),
                ("brief.studio_label",  {"label": "Label 'Lo studio'", "type": "text", "max_length": 40}),
            ]},
            {"label": "Response SLA · intestazione", "fields": [
                ("brief.response_label", {"label": "Eyebrow (es. '// SLA di risposta')", "type": "text", "max_length": 60}),
            ]},
            {"label": "Footer boot", "fields": [
                ("brief.boot_left",  {"label": "Boot · sinistra", "type": "text", "max_length": 200}),
                ("brief.boot_right", {"label": "Boot · destra",   "type": "text", "max_length": 200}),
            ]},
        ],
    },
]


LEX_CLASSIC_GOLD_SCHEMA: list[dict[str, Any]] = [
    {
        "id": "brand",
        "label": "Brand",
        "icon": "bi-bookmark-star",
        "region": ".lx-nav, .lx-foot",
        "page": "*",
        "keywords": ["logo", "marchio", "studio", "tagline", "foro", "insegna"],
        "help": "Nome studio, iniziale crest e tagline istituzionale.",
        "fields": [
            ("site.logo_word",    {"label": "Nome studio", "type": "text", "max_length": 60,
                                    "placeholder": "Studio Legale Ferri"}),
            ("site.logo_initial", {"label": "Iniziale / crest", "type": "text", "max_length": 4}),
            ("site.tag",          {"label": "Tagline", "type": "text", "max_length": 100}),
            ("site.nav_cta",      {"label": "CTA nav", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "hero_home",
        "label": "Hero home",
        "icon": "bi-easel",
        "region": ".lx-lead, .lx-hero",
        "page": "home",
        "keywords": ["hero", "apertura", "headline", "eyebrow", "intro", "cta", "credits"],
        "help": "Primo scroll della home: eyebrow, headline, intro, CTA principali, credits direzione.",
        "fields": [
            ("home.eyebrow",             {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("home.headline",            {"label": "Headline", "type": "richtext", "max_length": 220,
                                           "help": "Consentiti i tag <em> per gli italici."}),
            ("home.intro",               {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("home.primary_cta",         {"label": "CTA primaria · etichetta", "type": "text", "max_length": 60}),
            ("home.primary_href",        {"label": "CTA primaria · destinazione", "type": "select",
                                           "choices": ["home", "studio", "pratiche", "avvocati",
                                                       "notabili", "contatti"]}),
            ("home.secondary_cta",       {"label": "CTA secondaria · etichetta", "type": "text", "max_length": 60}),
            ("home.secondary_href",      {"label": "CTA secondaria · destinazione", "type": "select",
                                           "choices": ["home", "studio", "pratiche", "avvocati",
                                                       "notabili", "contatti"]}),
        ],
    },
    {
        "id": "home_bands",
        "label": "Home · fasce copy",
        "icon": "bi-layout-three-columns",
        "region": ".lx-section, .lx-cta-band",
        "page": "home",
        "keywords": ["pratiche", "partners", "pubblicazioni", "stats", "cta"],
        "help": "Label, eyebrow e intro delle fasce home (pratiche, partners, pubblicazioni, stats, CTA finale).",
        "fields": [
            ("home.practice_label",       {"label": "Pratiche · eyebrow", "type": "text", "max_length": 80}),
            ("home.practice_heading",     {"label": "Pratiche · titolo", "type": "richtext", "max_length": 220}),
            ("home.practice_intro",       {"label": "Pratiche · intro", "type": "textarea", "max_length": 500}),
            ("home.partners_label",       {"label": "Partners · eyebrow", "type": "text", "max_length": 80}),
            ("home.partners_heading",     {"label": "Partners · titolo", "type": "richtext", "max_length": 220}),
            ("home.partners_intro",       {"label": "Partners · intro", "type": "textarea", "max_length": 500}),
            ("home.publications_label",   {"label": "Pubblicazioni · eyebrow", "type": "text", "max_length": 80}),
            ("home.stats_label",          {"label": "Stats · eyebrow", "type": "text", "max_length": 80}),
            ("home.stats_heading",        {"label": "Stats · titolo", "type": "richtext", "max_length": 220}),
            ("home.cta_label",            {"label": "CTA finale · eyebrow", "type": "text", "max_length": 80}),
            ("home.cta_heading",          {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("home.cta_intro",            {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("home.cta_primary",          {"label": "CTA finale · primario", "type": "text", "max_length": 60}),
            ("home.cta_primary_href",     {"label": "CTA finale · destinazione primaria", "type": "select",
                                            "choices": ["home", "studio", "pratiche", "avvocati",
                                                        "notabili", "contatti"]}),
            ("home.cta_secondary",        {"label": "CTA finale · secondario", "type": "text", "max_length": 60}),
            ("home.cta_secondary_href",   {"label": "CTA finale · destinazione secondaria", "type": "select",
                                            "choices": ["home", "studio", "pratiche", "avvocati",
                                                        "notabili", "contatti"]}),
        ],
    },
    {
        "id": "studio_page",
        "label": "Pagina Studio",
        "icon": "bi-building",
        "region": ".lx-section",
        "page": "studio",
        "keywords": ["studio", "storia", "valori", "metodo", "sedi"],
        "help": "Pagina Lo studio: storia, valori, metodo, CTA finale.",
        "fields": [
            ("studio.eyebrow",          {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("studio.headline",         {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("studio.intro",            {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("studio.history_label",    {"label": "Storia · eyebrow", "type": "text", "max_length": 80}),
            ("studio.history_heading",  {"label": "Storia · titolo", "type": "richtext", "max_length": 220}),
            ("studio.history_intro",    {"label": "Storia · intro", "type": "textarea", "max_length": 500}),
            ("studio.values_label",     {"label": "Valori · eyebrow", "type": "text", "max_length": 80}),
            ("studio.values_heading",   {"label": "Valori · titolo", "type": "richtext", "max_length": 220}),
            ("studio.values_intro",     {"label": "Valori · intro", "type": "textarea", "max_length": 500}),
            ("studio.coordinates_label", {"label": "Sedi · eyebrow", "type": "text", "max_length": 80}),
            ("studio.cta_heading",      {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("studio.cta_intro",        {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("studio.cta_primary",      {"label": "CTA · pulsante primario", "type": "text", "max_length": 60}),
            ("studio.cta_primary_href", {"label": "CTA · destinazione", "type": "select",
                                          "choices": ["home", "studio", "pratiche", "avvocati",
                                                      "notabili", "contatti"]}),
        ],
    },
    {
        "id": "pratiche_page",
        "label": "Pagina Pratiche",
        "icon": "bi-briefcase",
        "region": ".lx-section",
        "page": "pratiche",
        "keywords": ["pratiche", "aree", "servizi", "processo", "iter"],
        "help": "Pagina aree di pratica: headline, intro, processo, etichette pratica.",
        "fields": [
            ("pratiche.eyebrow",             {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("pratiche.headline",            {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("pratiche.intro",               {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("pratiche.process_label",       {"label": "Processo · eyebrow", "type": "text", "max_length": 80}),
            ("pratiche.process_heading",     {"label": "Processo · titolo", "type": "richtext", "max_length": 220}),
            ("pratiche.svc_lead_label",      {"label": "Etichetta socio responsabile", "type": "text", "max_length": 60}),
            ("pratiche.svc_jurisdiction_label", {"label": "Etichetta foro di riferimento", "type": "text", "max_length": 60}),
            ("pratiche.cta_heading",         {"label": "CTA finale · titolo", "type": "richtext", "max_length": 220}),
            ("pratiche.cta_intro",           {"label": "CTA finale · intro", "type": "textarea", "max_length": 500}),
            ("pratiche.cta_primary",         {"label": "CTA · pulsante", "type": "text", "max_length": 60}),
            ("pratiche.cta_primary_href",    {"label": "CTA · destinazione", "type": "select",
                                               "choices": ["home", "studio", "pratiche", "avvocati",
                                                           "notabili", "contatti"]}),
        ],
    },
    {
        "id": "avvocati_page",
        "label": "Pagina Avvocati",
        "icon": "bi-people",
        "region": ".lx-section",
        "page": "avvocati",
        "keywords": ["avvocati", "team", "soci", "collaboratori", "foro", "specializzazione"],
        "help": "Pagina team: intro + etichette colonne lista avvocati.",
        "fields": [
            ("avvocati.eyebrow",                     {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("avvocati.headline",                    {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("avvocati.intro",                       {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("avvocati.lawyer_foro_label",           {"label": "Etichetta Foro", "type": "text", "max_length": 40}),
            ("avvocati.lawyer_specialization_label", {"label": "Etichetta Specializzazione", "type": "text", "max_length": 60}),
            ("avvocati.lawyer_year_label",           {"label": "Etichetta Iscrizione", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "notabili_page",
        "label": "Pagina Notabili (blog index)",
        "icon": "bi-journal-richtext",
        "region": ".lx-section",
        "page": "notabili",
        "keywords": ["notabili", "cause", "pubblicazioni", "blog"],
        "help": "Pagina-indice cause notabili. I singoli post restano da registry.",
        "fields": [
            ("notabili.eyebrow",    {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("notabili.headline",   {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("notabili.intro",      {"label": "Intro", "type": "textarea", "max_length": 500}),
            ("notabili.lead_image", {"label": "Immagine di testata", "type": "image", "max_length": 400}),
        ],
    },
    {
        "id": "contatti_page",
        "label": "Pagina Contatti",
        "icon": "bi-telephone",
        "region": ".lx-section",
        "page": "contatti",
        "keywords": ["contatti", "contact", "modulo", "sedi", "canali"],
        "help": "Pagina contatti: copy + titoli form + etichette campi indirizzi. Struttura form e upload field restano da registry.",
        "fields": [
            ("contatti.eyebrow",              {"label": "Eyebrow", "type": "text", "max_length": 120}),
            ("contatti.headline",             {"label": "Headline", "type": "richtext", "max_length": 220}),
            ("contatti.intro",                {"label": "Intro", "type": "textarea", "max_length": 600}),
            ("contatti.footnote",             {"label": "Footnote piè pagina", "type": "textarea", "max_length": 500}),
            ("contatti.channels_label",       {"label": "Canali · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.offices_label",        {"label": "Sedi · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.form_label",           {"label": "Form · eyebrow", "type": "text", "max_length": 60}),
            ("contatti.form_heading",         {"label": "Form · titolo", "type": "richtext", "max_length": 220}),
            ("contatti.form_intro",           {"label": "Form · intro", "type": "textarea", "max_length": 400}),
            ("contatti.form_submit_label",    {"label": "Form · CTA submit", "type": "text", "max_length": 60}),
            ("contatti.form_submit_note",     {"label": "Form · nota submit", "type": "textarea", "max_length": 300}),
            ("contatti.office_address_label", {"label": "Etichetta Indirizzo", "type": "text", "max_length": 40}),
            ("contatti.office_area_label",    {"label": "Etichetta Zona", "type": "text", "max_length": 40}),
            ("contatti.office_phone_label",   {"label": "Etichetta Telefono", "type": "text", "max_length": 40}),
            ("contatti.office_email_label",   {"label": "Etichetta Email", "type": "text", "max_length": 40}),
            ("contatti.office_hours_label",   {"label": "Etichetta Orario", "type": "text", "max_length": 40}),
        ],
    },
    {
        "id": "contact_info",
        "label": "Contatti · footer",
        "icon": "bi-telephone-forward",
        "region": ".lx-foot",
        "page": "*",
        "keywords": ["footer", "phone", "email", "indirizzo", "orari", "licenza", "casi"],
        "help": "Dati di contatto visibili in footer + etichette case summary (lead/outcome/practice/year).",
        "fields": [
            ("site.phone",                {"label": "Telefono", "type": "text", "max_length": 40}),
            ("site.email",                {"label": "Email", "type": "text", "max_length": 80}),
            ("site.address",              {"label": "Indirizzo sede primaria", "type": "text", "max_length": 120}),
            ("site.hours_compact",        {"label": "Orari sintetici", "type": "text", "max_length": 80}),
            ("site.license",              {"label": "Licenza / Albo", "type": "text", "max_length": 120}),
            ("site.footer_intro",         {"label": "Intro footer", "type": "textarea", "max_length": 400}),
            ("site.case_lead_label",      {"label": "Case · etichetta Patrocinio", "type": "text", "max_length": 40}),
            ("site.case_outcome_label",   {"label": "Case · etichetta Esito", "type": "text", "max_length": 40}),
            ("site.case_practice_label",  {"label": "Case · etichetta Pratica", "type": "text", "max_length": 40}),
            ("site.case_year_label",      {"label": "Case · etichetta Anno", "type": "text", "max_length": 40}),
            ("site.foot_contact",         {"label": "Footer · titolo Contatti", "type": "text", "max_length": 40}),
            ("site.foot_offices",         {"label": "Footer · titolo Sedi", "type": "text", "max_length": 40}),
            ("site.foot_pages",           {"label": "Footer · titolo Pagine", "type": "text", "max_length": 40}),
            ("site.foot_studio",          {"label": "Footer · titolo Studio", "type": "text", "max_length": 40}),
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
    # A.8 · Gusto fine-dining — 3 readonly indexed lists (signature courses
    # on home, full menu courses on menu page, producers dict on home).
    # All tuple cells + dict cols omit any image column (portrait in
    # produttori.items is NOT exposed so the customer cannot reach it
    # through the editor; it stays global at the registry level).
    "fine-dining": {
        "home.signature_courses": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Atti in corso (piatti firma)",
            "icon": "bi-list-ol",
            "region": ".fd-signature-courses",
            "keywords": ["atti", "corsi", "menu", "piatti", "signature"],
            "tuple_order": ["num", "title", "detail", "wine"],
            "cols": [
                ("num",    {"label": "Numero", "type": "text", "max_length": 8}),
                ("title",  {"label": "Titolo piatto", "type": "text", "max_length": 80}),
                ("detail", {"label": "Dettagli", "type": "textarea", "max_length": 240}),
                ("wine",   {"label": "Abbinamento", "type": "text", "max_length": 120}),
            ],
        },
        "menu.courses": {
            "kind": "tuple",
            "page": "menu",
            "label": "Menu · Otto atti",
            "icon": "bi-journal-text",
            "region": ".fd-menu-list",
            "keywords": ["menu", "corsi", "piatti", "atti", "otto atti"],
            "tuple_order": ["num", "title", "detail", "wine"],
            "cols": [
                ("num",    {"label": "Numero", "type": "text", "max_length": 8}),
                ("title",  {"label": "Titolo piatto", "type": "text", "max_length": 80}),
                ("detail", {"label": "Dettagli", "type": "textarea", "max_length": 400}),
                ("wine",   {"label": "Abbinamento", "type": "text", "max_length": 160}),
            ],
        },
        "home.produttori.items": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Produttori (copy)",
            "icon": "bi-people",
            "region": ".fd-producers",
            "keywords": ["produttori", "artigiani", "fornitori"],
            "cols": [
                ("name",  {"label": "Nome", "type": "text", "max_length": 80}),
                ("role",  {"label": "Ruolo / prodotto", "type": "text", "max_length": 80}),
                ("area",  {"label": "Area / origine", "type": "text", "max_length": 80}),
                ("blurb", {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                # portrait intenzionalmente omesso: resta readonly al registry
            ],
        },
    },
    # A.9 · medical-specialist — 6 readonly indexed lists shared between
    # Cardio and Derm (same shape + same paths). All exposed text/label
    # cells stay global at the cell level per D-098. The ``portrait``
    # column on ``medici.doctors`` is intentionally omitted from the
    # dict shape ``cols`` so the 3 doctor portraits stay registry-only
    # (same pattern Gusto produttori.items).
    "specialist": {
        "home.facts": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Fatti clinici",
            "icon": "bi-bar-chart",
            "region": ".sp-hero",
            "keywords": ["fatti", "numeri", "esperienza", "visite"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 60}),
                ("value", {"label": "Valore",    "type": "text", "max_length": 40}),
            ],
        },
        "home.signature_visits": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Visite firma",
            "icon": "bi-list-ol",
            "region": ".sp-signature-visits",
            "keywords": ["visite", "signature", "percorsi", "trattamenti"],
            "tuple_order": ["num", "title", "body"],
            "cols": [
                ("num",   {"label": "Numero", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo visita", "type": "text", "max_length": 80}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "medici.doctors": {
            "kind": "dict",
            "page": "medici",
            "label": "Medici · Team (copy)",
            "icon": "bi-people",
            "region": ".sp-team",
            "keywords": ["medici", "team", "dottori", "equipe"],
            "cols": [
                ("name",  {"label": "Nome", "type": "text", "max_length": 80}),
                ("role",  {"label": "Ruolo", "type": "text", "max_length": 120}),
                ("bio",   {"label": "Biografia", "type": "textarea", "max_length": 600}),
                ("focus", {"label": "Area focus", "type": "text", "max_length": 120}),
                # portrait intenzionalmente omesso: resta readonly al registry
            ],
        },
        "studio.history": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Cronologia",
            "icon": "bi-clock-history",
            "region": ".sp-history",
            "keywords": ["storia", "timeline", "cronologia", "tappe"],
            "tuple_order": ["year", "title", "body"],
            "cols": [
                ("year",  {"label": "Anno", "type": "text", "max_length": 12}),
                ("title", {"label": "Titolo", "type": "text", "max_length": 80}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "studio.values": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Impegni / Valori",
            "icon": "bi-check2-square",
            "region": ".sp-values",
            "keywords": ["valori", "impegni", "promesse", "garanzie"],
            "tuple_order": ["title", "body"],
            "cols": [
                ("title", {"label": "Titolo", "type": "text", "max_length": 80}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "visite.treatments": {
            "kind": "tuple",
            "page": "visite",
            "label": "Visite · Trattamenti",
            "icon": "bi-heart-pulse",
            "region": ".sp-treatments",
            "keywords": ["trattamenti", "visite", "procedure", "servizi"],
            "tuple_order": ["num", "title", "body", "duration"],
            "cols": [
                ("num",      {"label": "Numero", "type": "text", "max_length": 8}),
                ("title",    {"label": "Titolo", "type": "text", "max_length": 80}),
                ("body",     {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("duration", {"label": "Durata / nota", "type": "text", "max_length": 80}),
            ],
        },
    },
    # A.10 · Lex classic-gold — 6 readonly indexed lists. No portrait column
    # appears in ``avvocati.lawyers`` or ``home.partners`` in this registry
    # (Lex doesn't ship lawyer portraits) so no col-exclusion is needed here.
    # The `scope` nested-list-of-str inside ``pratiche.services`` rows stays
    # registry-only: it's a list of bullet points, not a scalar — the dict
    # shape `cols` enumerates only the 5 text-typed scalars.
    "classic-gold": {
        "avvocati.lawyers": {
            "kind": "dict",
            "page": "avvocati",
            "label": "Avvocati · Team",
            "icon": "bi-people",
            "region": ".lx-lawyers",
            "keywords": ["avvocati", "team", "foro", "specializzazione"],
            "cols": [
                ("name",           {"label": "Nome", "type": "text", "max_length": 80}),
                ("role",           {"label": "Ruolo", "type": "text", "max_length": 120}),
                ("specialization", {"label": "Specializzazione", "type": "text", "max_length": 160}),
                ("foro",           {"label": "Foro", "type": "text", "max_length": 80}),
                ("year",           {"label": "Iscrizione", "type": "text", "max_length": 120}),
                ("bio",            {"label": "Biografia", "type": "textarea", "max_length": 800}),
            ],
        },
        "pratiche.services": {
            "kind": "dict",
            "page": "pratiche",
            "label": "Pratiche · Aree di pratica",
            "icon": "bi-briefcase",
            "region": ".lx-services",
            "keywords": ["pratiche", "aree", "servizi", "competenze"],
            "cols": [
                ("num",          {"label": "Numero", "type": "text", "max_length": 8}),
                ("title",        {"label": "Titolo area", "type": "text", "max_length": 80}),
                ("blurb",        {"label": "Descrizione", "type": "textarea", "max_length": 600}),
                ("lead",         {"label": "Socio responsabile", "type": "text", "max_length": 120}),
                ("jurisdiction", {"label": "Foro di riferimento", "type": "text", "max_length": 120}),
                # scope (list of str bullet points) intenzionalmente omesso:
                # resta readonly al registry.
            ],
        },
        "pratiche.process": {
            "kind": "tuple",
            "page": "pratiche",
            "label": "Pratiche · Iter mandato",
            "icon": "bi-list-ol",
            "region": ".lx-process",
            "keywords": ["processo", "iter", "fasi", "mandato"],
            "tuple_order": ["num", "title", "body"],
            "cols": [
                ("num",   {"label": "Numero", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo fase", "type": "text", "max_length": 80}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "studio.history": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Cronologia",
            "icon": "bi-clock-history",
            "region": ".lx-history",
            "keywords": ["storia", "timeline", "tappe", "cronologia"],
            "tuple_order": ["year", "title", "body"],
            "cols": [
                ("year",  {"label": "Anno", "type": "text", "max_length": 12}),
                ("title", {"label": "Titolo", "type": "text", "max_length": 80}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "studio.values": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Principi",
            "icon": "bi-check2-square",
            "region": ".lx-values",
            "keywords": ["valori", "principi", "impegni", "regole"],
            "tuple_order": ["num", "title", "body"],
            "cols": [
                ("num",   {"label": "Numero", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo principio", "type": "text", "max_length": 80}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "contatti.offices": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Sedi",
            "icon": "bi-geo-alt",
            "region": ".lx-offices",
            "keywords": ["sedi", "offices", "indirizzo", "telefono"],
            "cols": [
                ("city",    {"label": "Città", "type": "text", "max_length": 80}),
                ("tag",     {"label": "Etichetta sede", "type": "text", "max_length": 60}),
                ("address", {"label": "Indirizzo", "type": "text", "max_length": 160}),
                ("area",    {"label": "Zona", "type": "text", "max_length": 120}),
                ("phone",   {"label": "Telefono", "type": "text", "max_length": 40}),
                ("email",   {"label": "Email", "type": "text", "max_length": 80}),
                ("hours",   {"label": "Orari", "type": "text", "max_length": 120}),
            ],
        },
    },
    # A.11 · Juris modern-transparent — 6 readonly indexed lists. No
    # ``mutable: True`` flag (same as Lex / Pragma / Gusto / specialist).
    # Nested list-of-str cells inside dict rows are NEVER exposed in the
    # dict-shape cols (stay registry-only):
    #   - ``servizi.services[*].deliverables`` (4-bullet list per offer)
    #   - ``settori.sectors[*].pain_points / signals / legal_ops``
    #     (each a bullet list per area — same policy as Lex
    #     ``pratiche.services[*].scope``).
    # Juris ships ZERO image/portrait fields anywhere in the registry,
    # so no col-exclusion pattern for portraits is needed.
    "modern-transparent": {
        "approccio.founders": {
            "kind": "dict",
            "page": "approccio",
            "label": "Approccio · Fondatori",
            "icon": "bi-people",
            "region": ".jr-section",
            "keywords": ["fondatori", "founders", "partner", "managing"],
            "cols": [
                ("name", {"label": "Nome",       "type": "text",     "max_length": 80}),
                ("role", {"label": "Ruolo",      "type": "text",     "max_length": 120}),
                ("bio",  {"label": "Biografia",  "type": "textarea", "max_length": 700}),
                # credentials (list of str) intenzionalmente omesso:
                # resta readonly al registry.
            ],
        },
        "approccio.story": {
            "kind": "tuple",
            "page": "approccio",
            "label": "Approccio · Storia",
            "icon": "bi-clock-history",
            "region": ".jr-section",
            "keywords": ["storia", "timeline", "tappe", "cronologia"],
            "tuple_order": ["year", "title", "body"],
            "cols": [
                ("year",  {"label": "Anno",   "type": "text",     "max_length": 12}),
                ("title", {"label": "Titolo", "type": "text",     "max_length": 80}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "approccio.manifesto": {
            "kind": "tuple",
            "page": "approccio",
            "label": "Approccio · Manifesto",
            "icon": "bi-list-check",
            "region": ".jr-section",
            "keywords": ["manifesto", "principi", "valori", "regole"],
            "tuple_order": ["num", "title", "body"],
            "cols": [
                ("num",   {"label": "Numero", "type": "text",     "max_length": 8}),
                ("title", {"label": "Titolo principio", "type": "text", "max_length": 100}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 600}),
            ],
        },
        "servizi.services": {
            "kind": "dict",
            "page": "servizi",
            "label": "Servizi · Offerte",
            "icon": "bi-briefcase",
            "region": ".jr-section",
            "keywords": ["offerte", "servizi", "prezzi", "durata", "modalità"],
            "cols": [
                ("num",        {"label": "Numero", "type": "text", "max_length": 8}),
                ("title",      {"label": "Titolo offerta", "type": "text", "max_length": 100}),
                ("tier",       {"label": "Tier", "type": "text", "max_length": 40}),
                ("blurb",      {"label": "Descrizione", "type": "textarea", "max_length": 600}),
                ("duration",   {"label": "Durata", "type": "text", "max_length": 80}),
                ("engagement", {"label": "Modalità", "type": "text", "max_length": 120}),
                ("price",      {"label": "Prezzo", "type": "text", "max_length": 100}),
                # deliverables (list of str bullet points) intenzionalmente
                # omesso: resta readonly al registry.
            ],
        },
        "settori.sectors": {
            "kind": "dict",
            "page": "settori",
            "label": "Settori · Aree",
            "icon": "bi-diagram-3",
            "region": ".jr-section",
            "keywords": ["settori", "sectors", "aree", "partner", "legal ops"],
            "cols": [
                ("num",          {"label": "Numero", "type": "text", "max_length": 8}),
                ("title",        {"label": "Titolo area", "type": "text", "max_length": 80}),
                ("tagline",      {"label": "Tagline", "type": "text", "max_length": 160}),
                ("case_snippet", {"label": "Caso esemplare", "type": "textarea", "max_length": 600}),
                ("partner",      {"label": "Partner responsabile", "type": "text", "max_length": 120}),
                ("legal_ops",    {"label": "Legal ops di riferimento", "type": "text", "max_length": 120}),
                # pain_points / signals / legal_ops (list-of-str bullet
                # points) intenzionalmente omessi: restano readonly al
                # registry. Note: la col `legal_ops` qui è il campo
                # scalar "legal ops · persona" (non la lista).
            ],
        },
        "settori.team": {
            "kind": "dict",
            "page": "settori",
            "label": "Settori · Team completo",
            "icon": "bi-people",
            "region": ".jr-section",
            "keywords": ["team", "avvocati", "legal ops", "partner", "office"],
            "cols": [
                ("name",   {"label": "Nome", "type": "text", "max_length": 80}),
                ("role",   {"label": "Ruolo", "type": "text", "max_length": 140}),
                ("bio",    {"label": "Biografia breve", "type": "textarea", "max_length": 400}),
                ("office", {"label": "Sede", "type": "text", "max_length": 60}),
                ("email",  {"label": "Email", "type": "text", "max_length": 100}),
            ],
        },
    },
    # A.12 · Casa mass-market — 15 readonly indexed lists (second zero-image
    # archetype after Juris). No image cols anywhere — Casa registry ships
    # no portrait / photo / image fields. No ``mutable: True`` flag (same
    # policy as Lex / Pragma / Gusto / specialist / Juris). Flat
    # list-of-str fields (``immobili.filters``, ``immobili.sort_options``,
    # ``home.search_widget.popular_tags``) are intentionally NOT exposed
    # as indexed lists — they stay registry-only per the A.11 complex-shape
    # exclusion pattern. The ``posts`` list (12 property entries) also
    # stays registry-only — per-property detail editing is out of the
    # A.12 perimeter (same policy as Lex ``notabili`` posts / Juris
    # ``insights`` posts).
    "mass-market": {
        "home.featured_listings": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Immobili in evidenza",
            "icon": "bi-buildings",
            "region": ".dm-section",
            "keywords": ["immobili", "featured", "evidenza", "prezzo"],
            "tuple_order": ["price", "title", "location", "rooms", "surface", "bathrooms", "badge", "reference"],
            "cols": [
                ("title",    {"label": "Titolo annuncio", "type": "text", "max_length": 120}),
                ("location", {"label": "Località", "type": "text", "max_length": 100}),
                ("price",    {"label": "Prezzo", "type": "text", "max_length": 40}),
                ("badge",    {"label": "Badge (Esclusiva/Novità)", "type": "text", "max_length": 40}),
            ],
        },
        "home.neighborhoods": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Quartieri",
            "icon": "bi-geo",
            "region": ".dm-section",
            "keywords": ["quartieri", "neighborhoods", "aree"],
            "tuple_order": ["name", "tagline", "meta", "price_from"],
            "cols": [
                ("name",       {"label": "Nome quartiere", "type": "text", "max_length": 80}),
                ("tagline",    {"label": "Tagline", "type": "text", "max_length": 120}),
                ("meta",       {"label": "Meta (immobili disponibili)", "type": "text", "max_length": 80}),
                ("price_from", {"label": "Prezzo da", "type": "text", "max_length": 40}),
            ],
        },
        "home.stats": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Statistiche",
            "icon": "bi-bar-chart",
            "region": ".dm-section",
            "keywords": ["stats", "numeri", "fatti", "kpi"],
            "tuple_order": ["number", "suffix", "label"],
            "cols": [
                ("number", {"label": "Numero", "type": "text", "max_length": 16}),
                ("suffix", {"label": "Suffisso (+ · k · %)", "type": "text", "max_length": 8}),
                ("label",  {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "home.agents_preview": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Agenti in anteprima",
            "icon": "bi-people",
            "region": ".dm-section",
            "keywords": ["agenti", "team home", "agents"],
            "tuple_order": ["name", "role", "area", "years"],
            "cols": [
                ("name",  {"label": "Nome", "type": "text", "max_length": 80}),
                ("role",  {"label": "Ruolo", "type": "text", "max_length": 80}),
                ("area",  {"label": "Area", "type": "text", "max_length": 80}),
                ("years", {"label": "Anni esperienza", "type": "text", "max_length": 40}),
            ],
        },
        "home.valuation_proof": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Valutazione · prove",
            "icon": "bi-shield-check",
            "region": ".dm-section",
            "keywords": ["valutazione", "prove", "kpi", "tempo"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 40}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "immobili.map_cells": {
            "kind": "tuple",
            "page": "immobili",
            "label": "Immobili · Mappa · celle città",
            "icon": "bi-map",
            "region": ".dm-section",
            "keywords": ["mappa", "città", "map"],
            "tuple_order": ["area", "count_label"],
            "cols": [
                ("area",        {"label": "Area", "type": "text", "max_length": 80}),
                ("count_label", {"label": "Conteggio immobili", "type": "text", "max_length": 80}),
            ],
        },
        "quartieri.guides": {
            "kind": "tuple",
            "page": "quartieri",
            "label": "Quartieri · Guide",
            "icon": "bi-journal-text",
            "region": ".dm-section",
            "keywords": ["guide", "quartiere", "dettaglio"],
            "tuple_order": ["name", "tagline", "price", "inventory", "transit", "green", "tone", "description", "agent_note"],
            "cols": [
                ("name",        {"label": "Nome quartiere", "type": "text", "max_length": 80}),
                ("tagline",     {"label": "Tagline", "type": "text", "max_length": 140}),
                ("price",       {"label": "Prezzo al m²", "type": "text", "max_length": 40}),
                ("inventory",   {"label": "Immobili disponibili", "type": "text", "max_length": 80}),
                ("description", {"label": "Descrizione", "type": "textarea", "max_length": 500}),
                ("agent_note",  {"label": "Nota agente residente", "type": "textarea", "max_length": 300}),
            ],
        },
        "quartieri.faq": {
            "kind": "tuple",
            "page": "quartieri",
            "label": "Quartieri · FAQ",
            "icon": "bi-question-circle",
            "region": ".dm-section",
            "keywords": ["faq", "domande", "quartieri"],
            "tuple_order": ["question", "answer"],
            "cols": [
                ("question", {"label": "Domanda", "type": "text", "max_length": 200}),
                ("answer",   {"label": "Risposta", "type": "textarea", "max_length": 600}),
            ],
        },
        "agenzia.agents": {
            "kind": "dict",
            "page": "agenzia",
            "label": "Agenzia · Team agenti",
            "icon": "bi-people-fill",
            "region": ".dm-section",
            "keywords": ["agenti", "team", "agenzia", "bio"],
            "cols": [
                ("name",       {"label": "Nome", "type": "text", "max_length": 80}),
                ("role",       {"label": "Ruolo", "type": "text", "max_length": 120}),
                ("area",       {"label": "Area di competenza", "type": "text", "max_length": 100}),
                ("years",      {"label": "Anni di esperienza", "type": "text", "max_length": 40}),
                ("languages",  {"label": "Lingue", "type": "text", "max_length": 120}),
                ("speciality", {"label": "Specialità", "type": "text", "max_length": 160}),
                ("phone",      {"label": "Telefono", "type": "text", "max_length": 40}),
                ("email",      {"label": "Email", "type": "text", "max_length": 80}),
                ("quote",      {"label": "Citazione personale", "type": "textarea", "max_length": 400}),
            ],
        },
        "agenzia.facts": {
            "kind": "tuple",
            "page": "agenzia",
            "label": "Agenzia · Fatti chiave",
            "icon": "bi-123",
            "region": ".dm-section",
            "keywords": ["fatti", "numeri", "kpi", "storia"],
            "tuple_order": ["number", "suffix", "label"],
            "cols": [
                ("number", {"label": "Numero", "type": "text", "max_length": 16}),
                ("suffix", {"label": "Suffisso", "type": "text", "max_length": 8}),
                ("label",  {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "valutazione.how_it_works": {
            "kind": "tuple",
            "page": "valutazione",
            "label": "Valutazione · Come funziona",
            "icon": "bi-list-ol",
            "region": ".dm-section",
            "keywords": ["processo", "come funziona", "fasi"],
            "tuple_order": ["num", "title", "body"],
            "cols": [
                ("num",   {"label": "Numero", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo fase", "type": "text", "max_length": 100}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "valutazione.proof": {
            "kind": "tuple",
            "page": "valutazione",
            "label": "Valutazione · Prove",
            "icon": "bi-shield-check",
            "region": ".dm-section",
            "keywords": ["prove", "numeri", "valutazione"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 40}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "valutazione.faq": {
            "kind": "tuple",
            "page": "valutazione",
            "label": "Valutazione · FAQ",
            "icon": "bi-question-circle",
            "region": ".dm-section",
            "keywords": ["faq", "domande", "valutazione"],
            "tuple_order": ["question", "answer"],
            "cols": [
                ("question", {"label": "Domanda", "type": "text", "max_length": 200}),
                ("answer",   {"label": "Risposta", "type": "textarea", "max_length": 600}),
            ],
        },
        "contatti.channels": {
            "kind": "tuple",
            "page": "contatti",
            "label": "Contatti · Canali diretti",
            "icon": "bi-broadcast",
            "region": ".dm-section",
            "keywords": ["canali", "telefono", "email", "contatti"],
            "tuple_order": ["label", "value", "note"],
            "cols": [
                ("label", {"label": "Etichetta canale", "type": "text", "max_length": 40}),
                ("value", {"label": "Valore (numero/email)", "type": "text", "max_length": 120}),
                ("note",  {"label": "Nota", "type": "text", "max_length": 200}),
            ],
        },
        "contatti.offices": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Sedi",
            "icon": "bi-geo-alt",
            "region": ".dm-section",
            "keywords": ["sedi", "offices", "indirizzo"],
            "cols": [
                ("name",       {"label": "Nome sede", "type": "text", "max_length": 80}),
                ("address",    {"label": "Indirizzo", "type": "text", "max_length": 160}),
                ("metro",      {"label": "Metro / trasporti", "type": "text", "max_length": 120}),
                ("hours",      {"label": "Orari", "type": "text", "max_length": 120}),
                ("phone",      {"label": "Telefono", "type": "text", "max_length": 40}),
                ("email",      {"label": "Email", "type": "text", "max_length": 80}),
                ("lead_agent", {"label": "Agente responsabile", "type": "text", "max_length": 80}),
                ("parking",    {"label": "Parcheggio", "type": "text", "max_length": 120}),
                ("note",       {"label": "Nota", "type": "textarea", "max_length": 300}),
                # whatsapp / whatsapp_href / map_link / map_href stay
                # registry-only (structural href cells, not editorial copy).
            ],
        },
    },
    # A.12b · Villa ultra-luxury-cinematic — 14 readonly indexed lists,
    # FOUR with image cols (home.signature.image · territorio.territories.image
    # · studio.advisors.portrait · + home scalar image fields separately in
    # the flat schema). The image-in-dict-row pattern is NOT novel — it
    # mirrors Vertex ``studio.partners.portrait`` (production since A.3a/A.4).
    # No ``mutable: True`` flag (same as every archetype except Vertex).
    # Flat list-of-str containers (`home.territory`, `home.press_items`,
    # `collezione.sort_options`) intentionally NOT exposed. Nested
    # list-of-str inside dict rows (`collezione.filter_groups[].options`,
    # `concierge.form_fields[].options`) intentionally NOT exposed.
    # The `posts` list (8 blog entries, incl. image col) stays
    # registry-only — same policy as Lex/Juris/Casa per-post entries.
    "ultra-luxury-cinematic": {
        "home.signature": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Signature (4 dimore)",
            "icon": "bi-gem",
            "region": ".vp-section",
            "keywords": ["signature", "dimore", "immobili", "featured"],
            "cols": [
                ("index",        {"label": "Index / N°", "type": "text", "max_length": 12}),
                ("title",        {"label": "Titolo dimora", "type": "text", "max_length": 120}),
                ("territorio",   {"label": "Territorio", "type": "text", "max_length": 80}),
                ("superficie",   {"label": "Superficie", "type": "text", "max_length": 60}),
                ("provenance",   {"label": "Provenance", "type": "text", "max_length": 120}),
                ("availability", {"label": "Disponibilità", "type": "text", "max_length": 120}),
                ("image",        {"label": "Cover image · URL", "type": "image", "max_length": 400}),
            ],
        },
        "home.hero_credit_cells": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Hero credit cells",
            "icon": "bi-123",
            "region": ".vp-hero",
            "keywords": ["credit", "cells", "hero meta"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 40}),
                ("value", {"label": "Valore", "type": "text", "max_length": 40}),
            ],
        },
        "home.numbers": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Numbers",
            "icon": "bi-bar-chart",
            "region": ".vp-section",
            "keywords": ["numbers", "stats", "metriche"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 16}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "collezione.filter_groups": {
            "kind": "dict",
            "page": "collezione",
            "label": "Collezione · Filter groups (label)",
            "icon": "bi-funnel",
            "region": ".vp-section",
            "keywords": ["filtri", "filter groups", "label"],
            "cols": [
                ("label", {"label": "Label gruppo filtri", "type": "text", "max_length": 60}),
                # `options` (list-of-str len=8 per row) intenzionalmente
                # omesso: resta readonly al registry (complex-shape
                # exclusion · stesso pattern di Juris deliverables).
            ],
        },
        "territorio.territories": {
            "kind": "dict",
            "page": "territorio",
            "label": "Territorio · Territori (6 con image)",
            "icon": "bi-geo",
            "region": ".vp-section",
            "keywords": ["territori", "regioni", "provenance"],
            "cols": [
                ("name",       {"label": "Nome territorio", "type": "text", "max_length": 80}),
                ("region",     {"label": "Regione", "type": "text", "max_length": 80}),
                ("history",    {"label": "History / descrizione", "type": "textarea", "max_length": 500}),
                ("architects", {"label": "Architetti / registi", "type": "text", "max_length": 200}),
                ("count",      {"label": "Count immobili", "type": "text", "max_length": 40}),
                ("since",      {"label": "Dal (anno)", "type": "text", "max_length": 40}),
                ("image",      {"label": "Hero image · URL", "type": "image", "max_length": 400}),
            ],
        },
        "territorio.stats": {
            "kind": "tuple",
            "page": "territorio",
            "label": "Territorio · Stats",
            "icon": "bi-bar-chart",
            "region": ".vp-section",
            "keywords": ["stats", "numeri", "territorio"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 16}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "studio.advisors": {
            "kind": "dict",
            "page": "studio",
            "label": "Studio · Advisors (4 con portrait)",
            "icon": "bi-people",
            "region": ".vp-section",
            "keywords": ["advisors", "team", "portrait"],
            "cols": [
                ("name",       {"label": "Nome", "type": "text", "max_length": 80}),
                ("role",       {"label": "Ruolo", "type": "text", "max_length": 120}),
                ("bio",        {"label": "Biografia", "type": "textarea", "max_length": 600}),
                ("territories",{"label": "Territori (scalar)", "type": "text", "max_length": 200}),
                ("since",      {"label": "In studio dal", "type": "text", "max_length": 40}),
                ("portrait",   {"label": "Ritratto · URL", "type": "image", "max_length": 400}),
                ("langs",      {"label": "Lingue", "type": "text", "max_length": 120}),
            ],
        },
        "studio.partners": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Partners istituzionali",
            "icon": "bi-building",
            "region": ".vp-section",
            "keywords": ["partners", "studi", "notarili", "istituzionali"],
            "tuple_order": ["name", "note"],
            "cols": [
                ("name", {"label": "Nome partner", "type": "text", "max_length": 120}),
                ("note", {"label": "Nota / contesto", "type": "text", "max_length": 160}),
            ],
        },
        "studio.press_items": {
            "kind": "dict",
            "page": "studio",
            "label": "Studio · Press",
            "icon": "bi-newspaper",
            "region": ".vp-section",
            "keywords": ["press", "stampa", "magazine"],
            "cols": [
                ("magazine", {"label": "Magazine", "type": "text", "max_length": 80}),
                ("issue",    {"label": "Issue / numero", "type": "text", "max_length": 80}),
                ("title",    {"label": "Titolo pezzo", "type": "text", "max_length": 200}),
                ("byline",   {"label": "Firma", "type": "text", "max_length": 120}),
            ],
        },
        "studio.numbers": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Numbers",
            "icon": "bi-bar-chart",
            "region": ".vp-section",
            "keywords": ["numbers", "fatti", "kpi"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 16}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "esperienza.process": {
            "kind": "dict",
            "page": "esperienza",
            "label": "Esperienza · Processo (5 step)",
            "icon": "bi-list-ol",
            "region": ".vp-section",
            "keywords": ["processo", "fasi", "esperienza"],
            "cols": [
                ("n",        {"label": "Numero", "type": "text", "max_length": 8}),
                ("title",    {"label": "Titolo fase", "type": "text", "max_length": 120}),
                ("duration", {"label": "Durata", "type": "text", "max_length": 60}),
                ("text",     {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "esperienza.faq_items": {
            "kind": "dict",
            "page": "esperienza",
            "label": "Esperienza · FAQ",
            "icon": "bi-question-circle",
            "region": ".vp-section",
            "keywords": ["faq", "domande", "esperienza"],
            "cols": [
                ("q", {"label": "Domanda", "type": "text", "max_length": 240}),
                ("a", {"label": "Risposta", "type": "textarea", "max_length": 700}),
            ],
        },
        "concierge.phone_rows": {
            "kind": "tuple",
            "page": "concierge",
            "label": "Concierge · Phone rows",
            "icon": "bi-telephone",
            "region": ".vp-section",
            "keywords": ["phone", "canali", "concierge"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 80}),
                ("value", {"label": "Valore (email/telefono)", "type": "text", "max_length": 120}),
            ],
        },
        "concierge.offices": {
            "kind": "dict",
            "page": "concierge",
            "label": "Concierge · Sedi",
            "icon": "bi-geo-alt",
            "region": ".vp-section",
            "keywords": ["sedi", "offices", "concierge"],
            "cols": [
                ("city",    {"label": "Città", "type": "text", "max_length": 80}),
                ("address", {"label": "Indirizzo", "type": "text", "max_length": 160}),
                ("hours",   {"label": "Orari", "type": "text", "max_length": 160}),
                ("email",   {"label": "Email", "type": "text", "max_length": 80}),
                ("role",    {"label": "Ruolo sede", "type": "text", "max_length": 120}),
            ],
        },
    },
    # A.13 · Chiara editorial-designer-grid — 11 readonly indexed lists.
    # `home.featured_works.items` is the **third precedent** of image-in-
    # dict-row exposure (after Vertex `studio.partners[].portrait` and
    # Villa `home.signature/territories/advisors[].image`). Path is 2
    # levels deep through the `home.featured_works` parent dict, but
    # `_resolve_path` walks any depth — verified Step-0. No service-layer
    # / rendering / widget changes required. Posts list (3 project detail
    # records) stays registry-only — detail-page editing is OUT of A.13
    # scope, consistent with Lex/Juris/Casa/Villa per-item content
    # policy. Flat list-of-str (`home.clients`, `lavoro.filters`) +
    # nested list-of-str (`studio.founder.credentials`,
    # `processo.capabilities_full[].scope`) + form structure
    # (`contatti.form_fields` + `form_sections` + `upload_field`) all
    # excluded via complex-shape policy.
    "editorial-designer-grid": {
        "home.ledger_rows": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Ledger rows",
            "icon": "bi-list-ol",
            "region": ".ed-hero-card",
            "keywords": ["ledger", "registro", "lavori", "rows"],
            "tuple_order": ["num", "title", "category", "year", "medium"],
            "cols": [
                ("num",      {"label": "Numero", "type": "text", "max_length": 8}),
                ("title",    {"label": "Titolo lavoro", "type": "text", "max_length": 120}),
                ("category", {"label": "Categoria", "type": "text", "max_length": 80}),
                ("year",     {"label": "Anno", "type": "text", "max_length": 16}),
                ("medium",   {"label": "Medium / spec", "type": "text", "max_length": 200}),
            ],
        },
        "home.capabilities": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Capabilities",
            "icon": "bi-grid-3x3-gap",
            "region": ".ed-capabilities",
            "keywords": ["capabilities", "discipline", "competenze"],
            "tuple_order": ["title", "body"],
            "cols": [
                ("title", {"label": "Titolo capability", "type": "text", "max_length": 80}),
                ("body",  {"label": "Body", "type": "textarea", "max_length": 400}),
            ],
        },
        "home.featured_works.items": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Featured works (4 items con image)",
            "icon": "bi-images",
            "region": ".ed-projects",
            "keywords": ["featured", "projects", "lavori", "image"],
            "cols": [
                ("year",       {"label": "Anno", "type": "text", "max_length": 16}),
                ("discipline", {"label": "Disciplina", "type": "text", "max_length": 80}),
                ("title",      {"label": "Titolo progetto", "type": "text", "max_length": 120}),
                ("blurb",      {"label": "Blurb", "type": "textarea", "max_length": 400}),
                ("image",      {"label": "Cover image · URL", "type": "image", "max_length": 400}),
                # `href` (link slug) intenzionalmente omesso: stays
                # registry-only · structural reference, not editorial copy.
            ],
        },
        "home.press": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Press (3 entries)",
            "icon": "bi-newspaper",
            "region": ".ed-press",
            "keywords": ["press", "stampa", "honor", "award"],
            "cols": [
                ("year",  {"label": "Anno", "type": "text", "max_length": 16}),
                ("honor", {"label": "Onorificenza", "type": "text", "max_length": 120}),
                ("work",  {"label": "Lavoro citato", "type": "text", "max_length": 120}),
                ("note",  {"label": "Nota", "type": "text", "max_length": 200}),
            ],
        },
        "home.commissions": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Commissions",
            "icon": "bi-briefcase",
            "region": ".ed-commissions",
            "keywords": ["commissions", "incarichi", "tipologie"],
            "tuple_order": ["title", "blurb"],
            "cols": [
                ("title", {"label": "Titolo commissione", "type": "text", "max_length": 120}),
                ("blurb", {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "studio.team": {
            "kind": "dict",
            "page": "studio",
            "label": "Studio · Team (6 persone)",
            "icon": "bi-people",
            "region": ".ed-team",
            "keywords": ["team", "studio", "people"],
            "cols": [
                ("name", {"label": "Nome", "type": "text", "max_length": 80}),
                ("role", {"label": "Ruolo", "type": "text", "max_length": 120}),
                ("bio",  {"label": "Biografia breve", "type": "textarea", "max_length": 400}),
            ],
        },
        "studio.principles": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Principles (4)",
            "icon": "bi-list-check",
            "region": ".ed-principles",
            "keywords": ["principles", "principi", "valori"],
            "tuple_order": ["num", "title", "body"],
            "cols": [
                ("num",   {"label": "Numero", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo principio", "type": "text", "max_length": 120}),
                ("body",  {"label": "Body", "type": "textarea", "max_length": 600}),
            ],
        },
        "studio.press_full": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Press completa (8)",
            "icon": "bi-journal-text",
            "region": ".ed-press-ledger",
            "keywords": ["press", "stampa", "completa", "press ledger"],
            "tuple_order": ["year", "outlet", "category", "work"],
            "cols": [
                ("year",     {"label": "Anno", "type": "text", "max_length": 16}),
                ("outlet",   {"label": "Outlet", "type": "text", "max_length": 80}),
                ("category", {"label": "Categoria", "type": "text", "max_length": 100}),
                ("work",     {"label": "Lavoro citato", "type": "text", "max_length": 200}),
            ],
        },
        "processo.process": {
            "kind": "tuple",
            "page": "processo",
            "label": "Processo · Steps (5)",
            "icon": "bi-list-ol",
            "region": ".ed-section",
            "keywords": ["processo", "steps", "fasi"],
            "tuple_order": ["num", "title", "body", "deliverable_label", "deliverable_value"],
            "cols": [
                ("num",                {"label": "Numero", "type": "text", "max_length": 8}),
                ("title",              {"label": "Titolo step", "type": "text", "max_length": 120}),
                ("body",               {"label": "Body", "type": "textarea", "max_length": 700}),
                ("deliverable_label",  {"label": "Deliverable · etichetta", "type": "text", "max_length": 60}),
                ("deliverable_value",  {"label": "Deliverable · valore", "type": "text", "max_length": 200}),
            ],
        },
        "processo.capabilities_full": {
            "kind": "dict",
            "page": "processo",
            "label": "Processo · Capabilities full (5)",
            "icon": "bi-gem",
            "region": ".ed-section",
            "keywords": ["capabilities", "competenze", "completo"],
            "cols": [
                ("num",      {"label": "Numero", "type": "text", "max_length": 8}),
                ("title",    {"label": "Titolo capability", "type": "text", "max_length": 120}),
                ("blurb",    {"label": "Blurb", "type": "textarea", "max_length": 500}),
                ("duration", {"label": "Durata", "type": "text", "max_length": 80}),
                # `scope` (list-of-str bullet points) intenzionalmente
                # omesso: complex-shape exclusion (registry-only · stesso
                # pattern di Juris `deliverables`).
            ],
        },
        "contatti.channels": {
            "kind": "tuple",
            "page": "contatti",
            "label": "Contatti · Channels",
            "icon": "bi-broadcast",
            "region": ".ed-section",
            "keywords": ["channels", "canali", "email", "phone"],
            "tuple_order": ["label", "value", "note"],
            "cols": [
                ("label", {"label": "Etichetta canale", "type": "text", "max_length": 60}),
                ("value", {"label": "Valore (email/numero)", "type": "text", "max_length": 120}),
                ("note",  {"label": "Nota", "type": "text", "max_length": 200}),
            ],
        },
    },
    # A.13b · Pixel cinematic-photographer — 10 readonly indexed lists
    # (9 tuple + 1 dict). Zero image cols anywhere — Pixel's only
    # editable image surface is the top-level scalar `home.hero_image`
    # (exposed as a flat schema field). The `posts` list (3 series
    # detail records incl. `posts[].cover_image` image col) stays
    # registry-only — detail-page editing is OUT of A.13b scope, 6th
    # uniform enforcement of the cross-archetype per-item content
    # policy (Lex+Juris+Casa+Villa+Chiara+Pixel).
    "cinematic-photographer": {
        "home.hero_credit_cells": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Hero credit cells",
            "icon": "bi-123",
            "region": ".cp-hero",
            "keywords": ["credit", "cells", "hero meta"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 40}),
                ("value", {"label": "Valore", "type": "text", "max_length": 80}),
            ],
        },
        "home.filmstrip": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Filmstrip (4 serie)",
            "icon": "bi-film",
            "region": ".cp-index-band",
            "keywords": ["filmstrip", "serie", "index"],
            "tuple_order": ["num", "title", "discipline", "period", "slug"],
            "cols": [
                ("num",        {"label": "Numero", "type": "text", "max_length": 8}),
                ("title",      {"label": "Titolo serie", "type": "text", "max_length": 120}),
                ("discipline", {"label": "Disciplina", "type": "text", "max_length": 100}),
                ("period",     {"label": "Periodo", "type": "text", "max_length": 60}),
                # `slug` (structural href) intenzionalmente omesso:
                # resta readonly al registry · stessa policy di Chiara
                # `home.featured_works.items.href`.
            ],
        },
        "home.publications": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Publications (3 voci)",
            "icon": "bi-newspaper",
            "region": ".cp-publications",
            "keywords": ["publications", "press", "home press"],
            "tuple_order": ["outlet", "text", "period"],
            "cols": [
                ("outlet", {"label": "Outlet", "type": "text", "max_length": 120}),
                ("text",   {"label": "Descrizione", "type": "textarea", "max_length": 300}),
                ("period", {"label": "Periodo", "type": "text", "max_length": 40}),
            ],
        },
        "biografia.kit": {
            "kind": "tuple",
            "page": "biografia",
            "label": "Biografia · Kit fotografico (4)",
            "icon": "bi-camera",
            "region": ".cp-kit",
            "keywords": ["kit", "camera", "equipment"],
            "tuple_order": ["num", "model", "body", "availability_label", "availability_value"],
            "cols": [
                ("num",                  {"label": "Numero", "type": "text", "max_length": 8}),
                ("model",                {"label": "Modello", "type": "text", "max_length": 80}),
                ("body",                 {"label": "Descrizione", "type": "textarea", "max_length": 600}),
                ("availability_label",   {"label": "Availability · etichetta", "type": "text", "max_length": 40}),
                ("availability_value",   {"label": "Availability · valore", "type": "text", "max_length": 120}),
            ],
        },
        "biografia.timeline": {
            "kind": "tuple",
            "page": "biografia",
            "label": "Biografia · Timeline (12 tappe)",
            "icon": "bi-clock-history",
            "region": ".cp-essay",
            "keywords": ["timeline", "storia", "tappe"],
            "tuple_order": ["year", "title", "body"],
            "cols": [
                ("year",  {"label": "Anno", "type": "text", "max_length": 16}),
                ("title", {"label": "Titolo", "type": "text", "max_length": 120}),
                ("body",  {"label": "Body", "type": "textarea", "max_length": 400}),
            ],
        },
        "pubblicazioni.press": {
            "kind": "dict",
            "page": "pubblicazioni",
            "label": "Pubblicazioni · Press (8 voci)",
            "icon": "bi-newspaper",
            "region": ".cp-press",
            "keywords": ["press", "stampa", "magazine"],
            "cols": [
                ("year",    {"label": "Anno", "type": "text", "max_length": 16}),
                ("outlet",  {"label": "Outlet", "type": "text", "max_length": 80}),
                ("type",    {"label": "Tipologia", "type": "text", "max_length": 80}),
                ("subject", {"label": "Soggetto", "type": "text", "max_length": 200}),
                ("format",  {"label": "Formato", "type": "text", "max_length": 160}),
            ],
        },
        "pubblicazioni.exhibitions": {
            "kind": "tuple",
            "page": "pubblicazioni",
            "label": "Pubblicazioni · Exhibitions (6)",
            "icon": "bi-easel3",
            "region": ".cp-exhib",
            "keywords": ["exhibitions", "mostre"],
            "tuple_order": ["year", "title", "meta", "period"],
            "cols": [
                ("year",   {"label": "Anno", "type": "text", "max_length": 16}),
                ("title",  {"label": "Titolo mostra", "type": "text", "max_length": 160}),
                ("meta",   {"label": "Meta", "type": "text", "max_length": 200}),
                ("period", {"label": "Periodo", "type": "text", "max_length": 80}),
            ],
        },
        "pubblicazioni.awards": {
            "kind": "tuple",
            "page": "pubblicazioni",
            "label": "Pubblicazioni · Awards (6)",
            "icon": "bi-trophy",
            "region": ".cp-awards",
            "keywords": ["awards", "premi"],
            "tuple_order": ["year", "title", "subject"],
            "cols": [
                ("year",    {"label": "Anno", "type": "text", "max_length": 16}),
                ("title",   {"label": "Titolo award", "type": "text", "max_length": 200}),
                ("subject", {"label": "Soggetto", "type": "text", "max_length": 200}),
            ],
        },
        "contatti.channels": {
            "kind": "tuple",
            "page": "contatti",
            "label": "Contatti · Channels",
            "icon": "bi-broadcast",
            "region": ".cp-contact-wrap",
            "keywords": ["channels", "canali", "email", "phone"],
            "tuple_order": ["label", "value", "note"],
            "cols": [
                ("label", {"label": "Etichetta canale", "type": "text", "max_length": 60}),
                ("value", {"label": "Valore (email/numero)", "type": "text", "max_length": 120}),
                ("note",  {"label": "Nota", "type": "text", "max_length": 200}),
            ],
        },
        "site.exif_footer": {
            "kind": "tuple",
            "page": "*",
            "label": "Footer · EXIF strip (4 celle)",
            "icon": "bi-camera-reels",
            "region": ".cp-exif-strip",
            "keywords": ["exif", "footer strip", "chrome"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta EXIF", "type": "text", "max_length": 40}),
                ("value", {"label": "Valore EXIF", "type": "text", "max_length": 120}),
            ],
        },
    },

    # A.14 · Sapore trattoria-warm — 20 readonly indexed lists (15 base
    # + 5 menu.sections.{i}.dishes deep paths). 2 dict lists carry the
    # `portrait` image col (image-in-dict-row pattern · Vertex A.3a/A.4
    # precedent). Menu rows stay INSIDE perimeter as deep-path tuple
    # cells — each menu section's dishes register separately so the
    # customer can edit dish name/desc/price without the menu being
    # fake-editable.
    "trattoria-warm": {
        "home.family": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Famiglia (3 volti)",
            "icon": "bi-people",
            "region": ".tw-family",
            "keywords": ["family", "famiglia", "staff", "portraits"],
            "cols": [
                ("name",     {"label": "Nome", "type": "text", "max_length": 80}),
                ("role",     {"label": "Ruolo", "type": "text", "max_length": 120}),
                ("blurb",    {"label": "Blurb", "type": "textarea", "max_length": 500}),
                ("portrait", {"label": "Portrait · URL", "type": "image", "max_length": 400}),
            ],
        },
        "home.reviews": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Reviews (3 voci)",
            "icon": "bi-quote",
            "region": ".tw-reviews",
            "keywords": ["reviews", "press", "quotes"],
            "cols": [
                ("quote",  {"label": "Citazione", "type": "textarea", "max_length": 400}),
                ("author", {"label": "Autore / testata", "type": "text", "max_length": 200}),
            ],
        },
        "home.facts": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Facts (3 celle)",
            "icon": "bi-123",
            "region": ".tw-hero",
            "keywords": ["facts", "numeri", "stats"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 60}),
                ("value", {"label": "Valore", "type": "text", "max_length": 80}),
            ],
        },
        "home.chalkboard_days": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Chalkboard (5 giorni)",
            "icon": "bi-journal-bookmark",
            "region": ".tw-chalkboard",
            "keywords": ["chalkboard", "lavagna", "settimana", "piatti"],
            "tuple_order": ["day", "dish", "side", "note"],
            "cols": [
                ("day",  {"label": "Giorno", "type": "text", "max_length": 40}),
                ("dish", {"label": "Piatto del giorno", "type": "text", "max_length": 160}),
                ("side", {"label": "Side / contorno", "type": "text", "max_length": 160}),
                ("note", {"label": "Nota", "type": "text", "max_length": 200}),
            ],
        },
        "home.hours_rows": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Hours (3 righe)",
            "icon": "bi-clock",
            "region": ".tw-hours",
            "keywords": ["hours", "orari", "apertura"],
            "tuple_order": ["days", "hours", "note"],
            "cols": [
                ("days",  {"label": "Giorni", "type": "text", "max_length": 80}),
                ("hours", {"label": "Orari", "type": "text", "max_length": 80}),
                ("note",  {"label": "Nota", "type": "text", "max_length": 200}),
            ],
        },
        "menu.sections": {
            "kind": "dict",
            "page": "menu",
            "label": "Menu · Sections (5 sezioni)",
            "icon": "bi-list-ul",
            "region": ".tw-menu-sections",
            "keywords": ["menu", "sezioni", "categorie"],
            "cols": [
                ("label",   {"label": "Etichetta sezione", "type": "text", "max_length": 80}),
                ("heading", {"label": "Titolo sezione", "type": "richtext", "max_length": 220}),
                # `dishes` col excluded at parent level — dishes are
                # registered as 5 separate indexed lists at deep paths
                # `menu.sections.{0..4}.dishes` so each section's
                # tuple cells (name/desc/price) are editable explicitly.
            ],
        },
        "menu.sections.0.dishes": {
            "kind": "tuple",
            "page": "menu",
            "label": "Menu · Sezione 1 · Piatti (7)",
            "icon": "bi-egg-fried",
            "region": ".tw-menu-sections",
            "keywords": ["piatti", "antipasti", "dishes", "menu"],
            "tuple_order": ["name", "desc", "price"],
            "cols": [
                ("name",  {"label": "Nome piatto", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
            ],
        },
        "menu.sections.1.dishes": {
            "kind": "tuple",
            "page": "menu",
            "label": "Menu · Sezione 2 · Piatti (7)",
            "icon": "bi-egg-fried",
            "region": ".tw-menu-sections",
            "keywords": ["piatti", "primi", "dishes", "menu"],
            "tuple_order": ["name", "desc", "price"],
            "cols": [
                ("name",  {"label": "Nome piatto", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
            ],
        },
        "menu.sections.2.dishes": {
            "kind": "tuple",
            "page": "menu",
            "label": "Menu · Sezione 3 · Piatti (6)",
            "icon": "bi-egg-fried",
            "region": ".tw-menu-sections",
            "keywords": ["piatti", "pizza", "dishes", "menu"],
            "tuple_order": ["name", "desc", "price"],
            "cols": [
                ("name",  {"label": "Nome piatto", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
            ],
        },
        "menu.sections.3.dishes": {
            "kind": "tuple",
            "page": "menu",
            "label": "Menu · Sezione 4 · Piatti (5)",
            "icon": "bi-egg-fried",
            "region": ".tw-menu-sections",
            "keywords": ["piatti", "secondi", "dishes", "menu"],
            "tuple_order": ["name", "desc", "price"],
            "cols": [
                ("name",  {"label": "Nome piatto", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
            ],
        },
        "menu.sections.4.dishes": {
            "kind": "tuple",
            "page": "menu",
            "label": "Menu · Sezione 5 · Piatti (5)",
            "icon": "bi-egg-fried",
            "region": ".tw-menu-sections",
            "keywords": ["piatti", "dolci", "dishes", "menu"],
            "tuple_order": ["name", "desc", "price"],
            "cols": [
                ("name",  {"label": "Nome piatto", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
            ],
        },
        "storia.timeline": {
            "kind": "dict",
            "page": "storia",
            "label": "Storia · Timeline (3 tappe)",
            "icon": "bi-clock-history",
            "region": ".tw-timeline",
            "keywords": ["timeline", "tappe", "date"],
            "cols": [
                ("year",  {"label": "Anno", "type": "text", "max_length": 16}),
                ("title", {"label": "Titolo tappa", "type": "text", "max_length": 160}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "storia.family": {
            "kind": "dict",
            "page": "storia",
            "label": "Storia · Famiglia (3 volti)",
            "icon": "bi-people",
            "region": ".tw-storia-family",
            "keywords": ["family", "famiglia", "staff", "portraits"],
            "cols": [
                ("name",     {"label": "Nome", "type": "text", "max_length": 80}),
                ("role",     {"label": "Ruolo", "type": "text", "max_length": 120}),
                ("blurb",    {"label": "Blurb", "type": "textarea", "max_length": 500}),
                ("portrait", {"label": "Portrait · URL", "type": "image", "max_length": 400}),
            ],
        },
        "storia.values": {
            "kind": "dict",
            "page": "storia",
            "label": "Storia · Valori (4 regole)",
            "icon": "bi-check-circle",
            "region": ".tw-values",
            "keywords": ["valori", "regole", "principi"],
            "cols": [
                ("title", {"label": "Titolo regola", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "forno.pizza_signatures": {
            "kind": "dict",
            "page": "forno",
            "label": "Forno · Pizza signatures (4)",
            "icon": "bi-disc",
            "region": ".tw-pizza-signatures",
            "keywords": ["pizza", "signature", "forno"],
            "cols": [
                ("n",     {"label": "Numero (I/II/III/IV)", "type": "text", "max_length": 8}),
                ("name",  {"label": "Nome pizza", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
            ],
        },
        "forno.pasta_signatures": {
            "kind": "dict",
            "page": "forno",
            "label": "Forno · Pasta signatures (4)",
            "icon": "bi-bounding-box-circles",
            "region": ".tw-pasta-signatures",
            "keywords": ["pasta", "signature", "mattarello"],
            "cols": [
                ("n",     {"label": "Numero (I/II/III/IV)", "type": "text", "max_length": 8}),
                ("name",  {"label": "Nome pasta", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
            ],
        },
        "forno.producers": {
            "kind": "dict",
            "page": "forno",
            "label": "Forno · Producers (5 fornitori)",
            "icon": "bi-box-seam",
            "region": ".tw-producers",
            "keywords": ["producers", "fornitori", "ingredienti"],
            "cols": [
                ("name",       {"label": "Nome fornitore", "type": "text", "max_length": 120}),
                ("place",      {"label": "Luogo", "type": "text", "max_length": 120}),
                ("ingredient", {"label": "Ingrediente", "type": "textarea", "max_length": 300}),
            ],
        },
        "eventi.experiences": {
            "kind": "dict",
            "page": "eventi",
            "label": "Eventi · Experiences (3 formule)",
            "icon": "bi-calendar-heart",
            "region": ".tw-experiences",
            "keywords": ["experiences", "formule", "tavolate"],
            "cols": [
                ("n",       {"label": "Numero (01/02/03)", "type": "text", "max_length": 8}),
                ("title",   {"label": "Titolo formula", "type": "text", "max_length": 120}),
                ("persons", {"label": "Persone", "type": "text", "max_length": 80}),
                ("menu",    {"label": "Menu", "type": "textarea", "max_length": 400}),
                ("wine",    {"label": "Vini inclusi", "type": "text", "max_length": 200}),
                ("desc",    {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "contatti.transport": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Transport (4 modi)",
            "icon": "bi-bus-front",
            "region": ".tw-transport",
            "keywords": ["transport", "trasporti", "come arrivare"],
            "cols": [
                ("mode", {"label": "Modo (Metro/Bus/Auto/etc.)", "type": "text", "max_length": 40}),
                ("line", {"label": "Linea / dettaglio", "type": "text", "max_length": 160}),
                ("note", {"label": "Nota", "type": "text", "max_length": 300}),
            ],
        },
        "contatti.hours_table": {
            "kind": "tuple",
            "page": "contatti",
            "label": "Contatti · Hours table (4 righe)",
            "icon": "bi-clock",
            "region": ".tw-contact",
            "keywords": ["hours", "orari", "tabella"],
            "tuple_order": ["days", "hours", "note"],
            "cols": [
                ("days",  {"label": "Giorni", "type": "text", "max_length": 80}),
                ("hours", {"label": "Orari", "type": "text", "max_length": 80}),
                ("note",  {"label": "Nota", "type": "text", "max_length": 200}),
            ],
        },
    },

    # A.14b · Brace street-modern — 30 readonly indexed lists (22 parent
    # + 5 menu.sections.{i}.items deep-path + 3 ordina.routes.{i}.lines
    # deep-path). Image cols on 6 lists (home.menu_strip_items + home.crew
    # + home.atmo_strip + lab.crew + moments.grid + menu.sections.{i}.items
    # × 5). Total editable image surface: 44 (3 scalar + 41 cells). Menu
    # rows inside perimeter as deep-path dict-in-dict-list parent (Chiara
    # precedent · same depth · same infra). Ordina routes lines inside
    # perimeter as deep-path tuple-in-dict-list parent (Sapore precedent ·
    # same infra via commit f66ac24 A.14 Step 2 contract-alignment fix).
    # Complex-shape exclusion: site.hours_footer_rows + home.manifesto_paragraphs
    # + moments.categories + pages + posts (empty). Col-exclusion:
    # menu.sections[].id (structural slug) · moments.grid[].filename (ID) ·
    # ordina.routes[].id + cta_kind (structural) · contatti.channels[].icon
    # + kind (structural). Zero form structures (Brace ships no form).
    "street-modern": {
        "home.stats": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Stats (4 celle)",
            "icon": "bi-bar-chart",
            "region": ".sm-stats",
            "keywords": ["stats", "numeri", "metrics"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 60}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 80}),
            ],
        },
        "home.menu_strip_items": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Menu strip items (6 piatti)",
            "icon": "bi-egg-fried",
            "region": ".sm-menu-strip",
            "keywords": ["menu", "strip", "items", "piatti"],
            "cols": [
                ("name",  {"label": "Nome piatto", "type": "text", "max_length": 80}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 300}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
                ("tag",   {"label": "Tag (TOP/NEW/VEG)", "type": "text", "max_length": 40}),
                ("image", {"label": "Image · URL", "type": "image", "max_length": 400}),
            ],
        },
        "home.delivery_partners": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Delivery partners (4)",
            "icon": "bi-bicycle",
            "region": ".sm-delivery",
            "keywords": ["delivery", "partners", "consegna"],
            "tuple_order": ["name", "eta", "min"],
            "cols": [
                ("name", {"label": "Nome partner", "type": "text", "max_length": 60}),
                ("eta",  {"label": "ETA", "type": "text", "max_length": 40}),
                ("min",  {"label": "Minimo ordine", "type": "text", "max_length": 60}),
            ],
        },
        "home.crew": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Crew (3 volti)",
            "icon": "bi-people",
            "region": ".sm-crew",
            "keywords": ["crew", "staff", "portraits"],
            "cols": [
                ("name",     {"label": "Nome", "type": "text", "max_length": 80}),
                ("role",     {"label": "Ruolo", "type": "text", "max_length": 120}),
                ("quote",    {"label": "Quote", "type": "textarea", "max_length": 500}),
                ("portrait", {"label": "Portrait · URL", "type": "image", "max_length": 400}),
            ],
        },
        "home.atmo_strip": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Atmo strip (3 foto)",
            "icon": "bi-image",
            "region": ".sm-atmo",
            "keywords": ["atmo", "atmosphere", "strip", "foto"],
            "cols": [
                ("cap",   {"label": "Caption", "type": "text", "max_length": 200}),
                ("image", {"label": "Image · URL", "type": "image", "max_length": 400}),
            ],
        },
        "menu.sections": {
            "kind": "dict",
            "page": "menu",
            "label": "Menu · Sections (5 sezioni)",
            "icon": "bi-list-ul",
            "region": ".sm-menu-sections",
            "keywords": ["menu", "sezioni", "categorie"],
            "cols": [
                ("label", {"label": "Etichetta sezione ('01'/'02'/...)", "type": "text", "max_length": 40}),
                ("title", {"label": "Titolo sezione", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione sezione", "type": "textarea", "max_length": 300}),
                # `id` col excluded (structural slug · 'burger'/'fritti'/etc.
                # used for routing). `items` col excluded at parent level —
                # dishes registered as 5 separate deep-path entries below so
                # each section's items (dict-with-image-col) are editable.
            ],
        },
        "menu.producers": {
            "kind": "dict",
            "page": "menu",
            "label": "Menu · Producers (3 fornitori)",
            "icon": "bi-box-seam",
            "region": ".sm-producers",
            "keywords": ["producers", "fornitori"],
            "cols": [
                ("name", {"label": "Nome fornitore", "type": "text", "max_length": 120}),
                ("city", {"label": "Città", "type": "text", "max_length": 120}),
                ("role", {"label": "Ruolo / descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "lab.manifesto_paragraphs": {
            "kind": "dict",
            "page": "lab",
            "label": "Lab · Manifesto (4 paragrafi)",
            "icon": "bi-journal",
            "region": ".sm-manifesto",
            "keywords": ["manifesto", "paragrafi"],
            "cols": [
                ("title", {"label": "Titolo paragrafo", "type": "text", "max_length": 120}),
                ("text",  {"label": "Testo", "type": "textarea", "max_length": 600}),
            ],
        },
        "lab.process": {
            "kind": "dict",
            "page": "lab",
            "label": "Lab · Process (3 step)",
            "icon": "bi-arrow-right-circle",
            "region": ".sm-process",
            "keywords": ["process", "step"],
            "cols": [
                ("num",   {"label": "Numero ('01'/'02'/...)", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo step", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "lab.crew": {
            "kind": "dict",
            "page": "lab",
            "label": "Lab · Crew completa (4 volti)",
            "icon": "bi-people",
            "region": ".sm-crew",
            "keywords": ["crew", "staff", "portraits", "lab"],
            "cols": [
                ("name",     {"label": "Nome", "type": "text", "max_length": 80}),
                ("role",     {"label": "Ruolo", "type": "text", "max_length": 120}),
                ("quote",    {"label": "Quote", "type": "textarea", "max_length": 500}),
                ("portrait", {"label": "Portrait · URL", "type": "image", "max_length": 400}),
            ],
        },
        "lab.values": {
            "kind": "dict",
            "page": "lab",
            "label": "Lab · Values (4 regole)",
            "icon": "bi-check-circle",
            "region": ".sm-values",
            "keywords": ["values", "regole", "principi"],
            "cols": [
                ("title", {"label": "Titolo regola", "type": "text", "max_length": 120}),
                ("tag",   {"label": "Tag", "type": "text", "max_length": 40}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "lab.kitchen_specs": {
            "kind": "tuple",
            "page": "lab",
            "label": "Lab · Kitchen specs (6 celle)",
            "icon": "bi-tools",
            "region": ".sm-kitchen",
            "keywords": ["kitchen", "specs", "scheda tecnica"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 60}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 80}),
            ],
        },
        "moments.grid": {
            "kind": "dict",
            "page": "moments",
            "label": "Moments · Grid (6 foto)",
            "icon": "bi-grid",
            "region": ".sm-grid",
            "keywords": ["moments", "grid", "gallery"],
            "cols": [
                ("cap",   {"label": "Caption", "type": "textarea", "max_length": 300}),
                ("tag",   {"label": "Tag (COUNTER QUEUE/DJ NIGHTS/...)", "type": "text", "max_length": 60}),
                ("image", {"label": "Image · URL", "type": "image", "max_length": 400}),
                # `filename` col excluded (structural ID · 'MO-001'/etc.).
            ],
        },
        "ordina.routes": {
            "kind": "dict",
            "page": "ordina",
            "label": "Ordina · Routes (3 rotte)",
            "icon": "bi-signpost-2",
            "region": ".sm-routes",
            "keywords": ["routes", "rotte", "ordina"],
            "cols": [
                ("title",      {"label": "Titolo rotta", "type": "text", "max_length": 120}),
                ("subtitle",   {"label": "Subtitle", "type": "text", "max_length": 120}),
                ("desc",       {"label": "Descrizione", "type": "textarea", "max_length": 500}),
                ("cta_label",  {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
                ("cta_href",   {"label": "CTA · href (URL/tel/anchor)", "type": "text", "max_length": 300}),
                # `id` col excluded (structural '01'/'02'/'03').
                # `cta_kind` col excluded (structural 'external'/'tel'/'anchor').
                # `lines` col excluded at parent level — registered as 3 separate
                # deep-path entries below so each route's nested tuple
                # (label/value) cells are editable.
            ],
        },
        "ordina.partners": {
            "kind": "dict",
            "page": "ordina",
            "label": "Ordina · Partners (4 partner delivery)",
            "icon": "bi-bicycle",
            "region": ".sm-partners",
            "keywords": ["partners", "delivery", "consegna"],
            "cols": [
                ("name", {"label": "Nome partner", "type": "text", "max_length": 60}),
                ("eta",  {"label": "ETA", "type": "text", "max_length": 40}),
                ("min",  {"label": "Minimo ordine", "type": "text", "max_length": 60}),
                ("zone", {"label": "Zona copertura", "type": "text", "max_length": 160}),
            ],
        },
        "ordina.hours_rows": {
            "kind": "tuple",
            "page": "ordina",
            "label": "Ordina · Hours (7 giorni)",
            "icon": "bi-clock",
            "region": ".sm-ordina",
            "keywords": ["hours", "orari"],
            "tuple_order": ["day", "hours"],
            "cols": [
                ("day",   {"label": "Giorno", "type": "text", "max_length": 40}),
                ("hours", {"label": "Orari", "type": "text", "max_length": 80}),
            ],
        },
        "ordina.faq": {
            "kind": "dict",
            "page": "ordina",
            "label": "Ordina · FAQ (4 domande)",
            "icon": "bi-question-circle",
            "region": ".sm-faq",
            "keywords": ["faq", "domande"],
            "cols": [
                ("q", {"label": "Domanda", "type": "text", "max_length": 200}),
                ("a", {"label": "Risposta", "type": "textarea", "max_length": 500}),
            ],
        },
        "contatti.channels": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Channels (3 canali)",
            "icon": "bi-broadcast",
            "region": ".sm-channels",
            "keywords": ["channels", "canali"],
            "cols": [
                ("label", {"label": "Etichetta canale", "type": "text", "max_length": 60}),
                ("value", {"label": "Valore (numero/email)", "type": "text", "max_length": 120}),
                ("note",  {"label": "Nota", "type": "text", "max_length": 200}),
                ("href",  {"label": "Href", "type": "text", "max_length": 300}),
                # `icon` col excluded (structural icon slug 'phone'/'mail'/etc.).
                # `kind` col excluded (structural routing flag 'tel'/'email'/...).
            ],
        },
        "contatti.hours_rows": {
            "kind": "tuple",
            "page": "contatti",
            "label": "Contatti · Hours (3 righe)",
            "icon": "bi-clock",
            "region": ".sm-contact",
            "keywords": ["hours", "orari"],
            "tuple_order": ["days", "hours"],
            "cols": [
                ("days",  {"label": "Giorni", "type": "text", "max_length": 80}),
                ("hours", {"label": "Orari", "type": "text", "max_length": 80}),
            ],
        },
        "contatti.transport_rows": {
            "kind": "tuple",
            "page": "contatti",
            "label": "Contatti · Transport (4 modi)",
            "icon": "bi-bus-front",
            "region": ".sm-transport",
            "keywords": ["transport", "trasporti"],
            "tuple_order": ["mode", "note"],
            "cols": [
                ("mode", {"label": "Modo (BUS/TRENO/...)", "type": "text", "max_length": 40}),
                ("note", {"label": "Nota", "type": "text", "max_length": 200}),
            ],
        },
        "contatti.jobs": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Jobs (3 posizioni)",
            "icon": "bi-briefcase",
            "region": ".sm-jobs",
            "keywords": ["jobs", "lavoro"],
            "cols": [
                ("role", {"label": "Ruolo", "type": "text", "max_length": 80}),
                ("type", {"label": "Tipologia (FULL TIME/...)", "type": "text", "max_length": 40}),
                ("city", {"label": "Città", "type": "text", "max_length": 60}),
            ],
        },
        "contatti.social": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Social (2 account)",
            "icon": "bi-instagram",
            "region": ".sm-social",
            "keywords": ["social", "instagram", "tiktok"],
            "cols": [
                ("platform", {"label": "Piattaforma", "type": "text", "max_length": 60}),
                ("handle",   {"label": "Handle", "type": "text", "max_length": 60}),
                ("href",     {"label": "URL completo", "type": "url", "max_length": 300}),
            ],
        },
        # --- Menu deep-path · 5 separate entries (dict-in-dict-list
        # parent · Chiara precedent) · each items list has image col ---
        "menu.sections.0.items": {
            "kind": "dict",
            "page": "menu",
            "label": "Menu · Sezione 1 · Items (4 piatti con foto)",
            "icon": "bi-egg-fried",
            "region": ".sm-menu-sections",
            "keywords": ["piatti", "burger", "items", "menu"],
            "cols": [
                ("name",  {"label": "Nome piatto", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
                ("tag",   {"label": "Tag (TOP/NEW/VEG)", "type": "text", "max_length": 40}),
                ("image", {"label": "Image · URL", "type": "image", "max_length": 400}),
            ],
        },
        "menu.sections.1.items": {
            "kind": "dict",
            "page": "menu",
            "label": "Menu · Sezione 2 · Items (4 piatti con foto)",
            "icon": "bi-egg-fried",
            "region": ".sm-menu-sections",
            "keywords": ["piatti", "fritti", "items", "menu"],
            "cols": [
                ("name",  {"label": "Nome piatto", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
                ("tag",   {"label": "Tag", "type": "text", "max_length": 40}),
                ("image", {"label": "Image · URL", "type": "image", "max_length": 400}),
            ],
        },
        "menu.sections.2.items": {
            "kind": "dict",
            "page": "menu",
            "label": "Menu · Sezione 3 · Items (4 piatti con foto)",
            "icon": "bi-egg-fried",
            "region": ".sm-menu-sections",
            "keywords": ["piatti", "pizza", "items", "menu"],
            "cols": [
                ("name",  {"label": "Nome piatto", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
                ("tag",   {"label": "Tag", "type": "text", "max_length": 40}),
                ("image", {"label": "Image · URL", "type": "image", "max_length": 400}),
            ],
        },
        "menu.sections.3.items": {
            "kind": "dict",
            "page": "menu",
            "label": "Menu · Sezione 4 · Items (4 piatti con foto)",
            "icon": "bi-egg-fried",
            "region": ".sm-menu-sections",
            "keywords": ["piatti", "drink", "items", "menu"],
            "cols": [
                ("name",  {"label": "Nome piatto", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
                ("tag",   {"label": "Tag", "type": "text", "max_length": 40}),
                ("image", {"label": "Image · URL", "type": "image", "max_length": 400}),
            ],
        },
        "menu.sections.4.items": {
            "kind": "dict",
            "page": "menu",
            "label": "Menu · Sezione 5 · Items (3 piatti con foto)",
            "icon": "bi-egg-fried",
            "region": ".sm-menu-sections",
            "keywords": ["piatti", "dolci", "items", "menu"],
            "cols": [
                ("name",  {"label": "Nome piatto", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("price", {"label": "Prezzo", "type": "text", "max_length": 40}),
                ("tag",   {"label": "Tag", "type": "text", "max_length": 40}),
                ("image", {"label": "Image · URL", "type": "image", "max_length": 400}),
            ],
        },
        # --- Ordina.routes deep-path · 3 separate entries (tuple-in-dict-list
        # parent · Sapore precedent · same infra via f66ac24 A.14 Step 2) ---
        "ordina.routes.0.lines": {
            "kind": "tuple",
            "page": "ordina",
            "label": "Ordina · Route 1 · Lines (3 righe)",
            "icon": "bi-signpost",
            "region": ".sm-routes",
            "keywords": ["lines", "indirizzo", "banco"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta (INDIRIZZO/TELEFONO/...)", "type": "text", "max_length": 60}),
                ("value", {"label": "Valore", "type": "text", "max_length": 300}),
            ],
        },
        "ordina.routes.1.lines": {
            "kind": "tuple",
            "page": "ordina",
            "label": "Ordina · Route 2 · Lines (3 righe)",
            "icon": "bi-signpost",
            "region": ".sm-routes",
            "keywords": ["lines", "takeaway", "telefono"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 60}),
                ("value", {"label": "Valore", "type": "text", "max_length": 300}),
            ],
        },
        "ordina.routes.2.lines": {
            "kind": "tuple",
            "page": "ordina",
            "label": "Ordina · Route 3 · Lines (3 righe)",
            "icon": "bi-signpost",
            "region": ".sm-routes",
            "keywords": ["lines", "delivery", "partner"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 60}),
                ("value", {"label": "Valore", "type": "text", "max_length": 300}),
            ],
        },
    },

    # A.15 · Bottega artisan-workshop — 14 readonly indexed lists, tutti
    # parent-level (zero deep-path · Bottega has no list-nested-in-list-
    # parent). 4 image-in-dict-row lists (home.latest_items, home.makers,
    # shop.products, product.related_items · 20 image cells). Col-level
    # exclusions per structural identifiers:
    #   - shop.products[].id + .available (slug + bool flag)
    #   - home.latest_items[].id
    #   - product.related_items[].id
    # Stringent IN call per Step-0 audit on `n`/`edition`/`icon`: values
    # are editorial visible content ('N° 042' / '3/8' / 'Esaurito' /
    # '01'/'02'/'03') in the same category as Sapore forno.pizza_signatures.n
    # and Chiara ledger_rows.num — customer-facing catalog numbering,
    # kept IN.
    "artisan-workshop": {
        "home.latest_items": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Latest items (4 pezzi demo)",
            "icon": "bi-grid",
            "region": ".aw-latest",
            "keywords": ["latest", "items", "products", "demo"],
            "cols": [
                ("n",       {"label": "Numero pezzo (visible)", "type": "text", "max_length": 16}),
                ("name",    {"label": "Nome pezzo", "type": "text", "max_length": 120}),
                ("meta",    {"label": "Meta (materiale · luogo)", "type": "text", "max_length": 200}),
                ("place",   {"label": "Luogo produzione", "type": "text", "max_length": 120}),
                ("price",   {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
                ("edition", {"label": "Edizione (visible)", "type": "text", "max_length": 40}),
                ("tag",     {"label": "Tag (editorial badge)", "type": "text", "max_length": 40}),
                ("image",   {"label": "Image · URL", "type": "image", "max_length": 400}),
                # `id` col excluded (structural slug · routing to /product/)
            ],
        },
        "home.makers": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Makers (4 artigiani)",
            "icon": "bi-people",
            "region": ".aw-makers",
            "keywords": ["makers", "artisans", "portraits"],
            "cols": [
                ("name",     {"label": "Nome artigiano", "type": "text", "max_length": 120}),
                ("craft",    {"label": "Mestiere", "type": "text", "max_length": 120}),
                ("place",    {"label": "Luogo", "type": "text", "max_length": 120}),
                ("since",    {"label": "Since (anno)", "type": "text", "max_length": 80}),
                ("quote",    {"label": "Quote", "type": "textarea", "max_length": 500}),
                ("portrait", {"label": "Portrait · URL", "type": "image", "max_length": 400}),
            ],
        },
        "home.provenance_items": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Provenance (3 territori)",
            "icon": "bi-geo-alt",
            "region": ".aw-provenance",
            "keywords": ["provenance", "territori", "origine"],
            "cols": [
                ("icon",  {"label": "Indice ('01'/'02'/'03')", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo territorio", "type": "text", "max_length": 120}),
                ("place", {"label": "Luogo (km da città)", "type": "text", "max_length": 160}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "home.stamp_rows": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Stamp rows (4 celle)",
            "icon": "bi-stamp",
            "region": ".aw-stamp",
            "keywords": ["stamp", "regole", "bottega"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 80}),
                ("value", {"label": "Valore", "type": "text", "max_length": 200}),
            ],
        },
        "home.care_items": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Care items (4 celle)",
            "icon": "bi-shield-check",
            "region": ".aw-care",
            "keywords": ["care", "garanzie"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 80}),
                ("value", {"label": "Valore", "type": "text", "max_length": 200}),
            ],
        },
        "shop.products": {
            "kind": "dict",
            "page": "shop",
            "label": "Shop · Products (9 pezzi demo · NON commerce state)",
            "icon": "bi-bag",
            "region": ".aw-products",
            "keywords": ["products", "catalogo", "demo"],
            "cols": [
                ("n",       {"label": "Numero pezzo (visible)", "type": "text", "max_length": 16}),
                ("name",    {"label": "Nome pezzo", "type": "text", "max_length": 120}),
                ("artisan", {"label": "Artigiano", "type": "text", "max_length": 120}),
                ("place",   {"label": "Luogo", "type": "text", "max_length": 120}),
                ("meta",    {"label": "Meta (materiale)", "type": "text", "max_length": 200}),
                ("price",   {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
                ("edition", {"label": "Edizione (visible · '3/8' · 'Esaurito')", "type": "text", "max_length": 40}),
                ("tag",     {"label": "Tag (editorial badge)", "type": "text", "max_length": 40}),
                ("image",   {"label": "Image · URL", "type": "image", "max_length": 400}),
                # `id` excluded (structural slug) · `available` excluded
                # (bool flag · commerce-state-like semantic · OUT stringent)
            ],
        },
        "product.info_rows": {
            "kind": "tuple",
            "page": "product",
            "label": "Product · Info rows (8 specs)",
            "icon": "bi-list-ul",
            "region": ".aw-info",
            "keywords": ["info", "specs", "specifiche"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta spec", "type": "text", "max_length": 80}),
                ("value", {"label": "Valore spec", "type": "text", "max_length": 300}),
            ],
        },
        "product.care_items": {
            "kind": "tuple",
            "page": "product",
            "label": "Product · Care items (4 celle)",
            "icon": "bi-shield-check",
            "region": ".aw-product-care",
            "keywords": ["care", "manutenzione"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 80}),
                ("value", {"label": "Valore", "type": "textarea", "max_length": 300}),
            ],
        },
        "product.provenance_steps": {
            "kind": "tuple",
            "page": "product",
            "label": "Product · Provenance steps (4 tappe)",
            "icon": "bi-geo",
            "region": ".aw-product-provenance",
            "keywords": ["provenance", "tappe"],
            "tuple_order": ["step", "place", "desc"],
            "cols": [
                ("step",  {"label": "Step (label)", "type": "text", "max_length": 80}),
                ("place", {"label": "Luogo", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 300}),
            ],
        },
        "product.related_items": {
            "kind": "dict",
            "page": "product",
            "label": "Product · Related items (3 pezzi correlati)",
            "icon": "bi-link",
            "region": ".aw-related",
            "keywords": ["related", "correlati"],
            "cols": [
                ("n",     {"label": "Numero pezzo (visible)", "type": "text", "max_length": 16}),
                ("name",  {"label": "Nome pezzo", "type": "text", "max_length": 120}),
                ("meta",  {"label": "Meta (materiale · artigiano)", "type": "text", "max_length": 200}),
                ("price", {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
                ("image", {"label": "Image · URL", "type": "image", "max_length": 400}),
                # `id` excluded (structural slug)
            ],
        },
        "atelier.process_steps": {
            "kind": "dict",
            "page": "atelier",
            "label": "Atelier · Process steps (5 tappe)",
            "icon": "bi-arrow-right-circle",
            "region": ".aw-process",
            "keywords": ["process", "atelier", "tappe"],
            "cols": [
                ("n",        {"label": "Step ('01'/'02'/...)", "type": "text", "max_length": 8}),
                ("title",    {"label": "Titolo step", "type": "text", "max_length": 120}),
                ("place",    {"label": "Luogo", "type": "text", "max_length": 160}),
                ("duration", {"label": "Durata", "type": "text", "max_length": 120}),
                ("desc",     {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "atelier.numbers_items": {
            "kind": "tuple",
            "page": "atelier",
            "label": "Atelier · Numbers (4 celle)",
            "icon": "bi-123",
            "region": ".aw-numbers",
            "keywords": ["numbers", "cifre"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 80}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "journal.entries": {
            "kind": "dict",
            "page": "journal",
            "label": "Journal · Entries (6 voci)",
            "icon": "bi-journal",
            "region": ".aw-entries",
            "keywords": ["journal", "entries", "diario"],
            "cols": [
                ("n",       {"label": "Numero entry (visible)", "type": "text", "max_length": 8}),
                ("title",   {"label": "Titolo entry", "type": "text", "max_length": 160}),
                ("place",   {"label": "Luogo · data", "type": "text", "max_length": 160}),
                ("excerpt", {"label": "Excerpt", "type": "textarea", "max_length": 500}),
                ("minutes", {"label": "Tempo di lettura", "type": "text", "max_length": 80}),
            ],
        },
        "contatti.faq_items": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · FAQ (4 domande)",
            "icon": "bi-question-circle",
            "region": ".aw-faq",
            "keywords": ["faq", "domande"],
            "cols": [
                ("q", {"label": "Domanda", "type": "text", "max_length": 200}),
                ("a", {"label": "Risposta", "type": "textarea", "max_length": 500}),
            ],
        },
    },
    # -----------------------------------------------------------------
    # A.15b · Luxe fashion-editorial. Seventeen indexed lists, all
    # parent-level (zero deep-path). Image-in-dict-row on 6 lists
    # (home.tiles + home.lookbook_teaser_tiles + collezione.products +
    # product.related_items + maison.ateliers + lookbook.looks) = 30
    # image cells · plus home.cover_image scalar + product.atelier_portrait
    # + maison.direction_portrait = 3 nested-dict scalar images = 31
    # image surfaces total. All rendered (photographically editorial DNA ·
    # zero storage-only, unlike Bottega typographic DNA). Stringent IN
    # col-level: drop/n/tag IN (editorial badges) · id/available OUT
    # (structural routing + commerce-state-like boolean).
    # -----------------------------------------------------------------
    "fashion-editorial": {
        "home.tiles": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Edition tiles (4 silhouettes)",
            "icon": "bi-grid",
            "region": ".fe-tiles",
            "keywords": ["edition", "tiles", "silhouettes", "home"],
            "cols": [
                ("tag",   {"label": "Tag (editorial badge)", "type": "text", "max_length": 40}),
                ("name",  {"label": "Nome capo", "type": "text", "max_length": 120}),
                ("price", {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
                ("image", {"label": "Image · URL (rendered)", "type": "image", "max_length": 400}),
                # `id` col excluded (structural slug · routing to /product/)
            ],
        },
        "home.atelier_numbers": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Atelier numbers (4 celle)",
            "icon": "bi-123",
            "region": ".fe-atelier-numbers",
            "keywords": ["atelier", "numbers", "cifre"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 80}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "home.lookbook_teaser_tiles": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Lookbook teaser tiles (3 immagini)",
            "icon": "bi-images",
            "region": ".fe-lookbook-teaser",
            "keywords": ["lookbook", "teaser", "tiles"],
            "cols": [
                ("title",  {"label": "Titolo look", "type": "text", "max_length": 160}),
                ("credit", {"label": "Credit (stilismo · foto · atelier)", "type": "text", "max_length": 160}),
                ("image",  {"label": "Image · URL (rendered)", "type": "image", "max_length": 400}),
            ],
        },
        "home.drop_metadata": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Drop metadata (4 celle)",
            "icon": "bi-calendar-event",
            "region": ".fe-drop",
            "keywords": ["drop", "metadata", "capsule"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 80}),
                ("value", {"label": "Valore", "type": "text", "max_length": 200}),
            ],
        },
        "collezione.products": {
            "kind": "dict",
            "page": "collezione",
            "label": "Collezione · Products (9 look demo · NON commerce state)",
            "icon": "bi-bag",
            "region": ".fe-products",
            "keywords": ["products", "collezione", "catalogo", "demo"],
            "cols": [
                ("n",     {"label": "Numero look (visible)", "type": "text", "max_length": 16}),
                ("name",  {"label": "Nome capo", "type": "text", "max_length": 120}),
                ("meta",  {"label": "Meta (materia · tessitoria)", "type": "text", "max_length": 200}),
                ("drop",  {"label": "Drop (visible · 'Drop 01 · Spring 26')", "type": "text", "max_length": 80}),
                ("price", {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
                ("tag",   {"label": "Tag (editorial badge · 'Lista d'attesa' · 'Sold-out')", "type": "text", "max_length": 60}),
                ("image", {"label": "Image · URL (rendered)", "type": "image", "max_length": 400}),
                # `id` excluded (structural slug) · `available` excluded
                # (bool flag · commerce-state-like · OUT stringent audit)
            ],
        },
        "product.info_rows": {
            "kind": "tuple",
            "page": "product",
            "label": "Product · Info rows (8 specs atelier)",
            "icon": "bi-list-ul",
            "region": ".fe-info",
            "keywords": ["info", "specs", "specifiche", "atelier"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta spec", "type": "text", "max_length": 80}),
                ("value", {"label": "Valore spec", "type": "text", "max_length": 300}),
            ],
        },
        "product.care_items": {
            "kind": "tuple",
            "page": "product",
            "label": "Product · Care items (4 celle)",
            "icon": "bi-shield-check",
            "region": ".fe-product-care",
            "keywords": ["care", "manutenzione"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Etichetta", "type": "text", "max_length": 80}),
                ("value", {"label": "Valore", "type": "textarea", "max_length": 300}),
            ],
        },
        "product.provenance_steps": {
            "kind": "tuple",
            "page": "product",
            "label": "Product · Provenance steps (4 tappe)",
            "icon": "bi-geo",
            "region": ".fe-product-provenance",
            "keywords": ["provenance", "tappe", "atelier"],
            "tuple_order": ["n", "title", "desc"],
            "cols": [
                ("n",     {"label": "Step ('01'/'02'/...)", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo tappa", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "product.related_items": {
            "kind": "dict",
            "page": "product",
            "label": "Product · Related items (3 capi correlati)",
            "icon": "bi-link",
            "region": ".fe-related",
            "keywords": ["related", "correlati"],
            "cols": [
                ("n",     {"label": "Numero look (visible)", "type": "text", "max_length": 16}),
                ("name",  {"label": "Nome capo", "type": "text", "max_length": 120}),
                ("meta",  {"label": "Meta (materia · atelier)", "type": "text", "max_length": 200}),
                ("price", {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
                ("image", {"label": "Image · URL (rendered)", "type": "image", "max_length": 400}),
                # `id` excluded (structural slug)
            ],
        },
        "maison.ateliers": {
            "kind": "dict",
            "page": "maison",
            "label": "Maison · Ateliers (3 città)",
            "icon": "bi-building",
            "region": ".fe-ateliers",
            "keywords": ["ateliers", "città", "maison"],
            "cols": [
                ("city",  {"label": "Città", "type": "text", "max_length": 80}),
                ("place", {"label": "Indirizzo (via · quartiere)", "type": "text", "max_length": 160}),
                ("role",  {"label": "Ruolo atelier", "type": "text", "max_length": 200}),
                ("since", {"label": "Apertura (es. 'Aperta nel 2014')", "type": "text", "max_length": 80}),
                ("head",  {"label": "Capo atelier · nome e ruolo", "type": "text", "max_length": 200}),
                ("team",  {"label": "Team (una riga)", "type": "text", "max_length": 240}),
                ("image", {"label": "Image · URL (rendered)", "type": "image", "max_length": 400}),
            ],
        },
        "maison.press_items": {
            "kind": "dict",
            "page": "maison",
            "label": "Maison · Press (5 apparizioni)",
            "icon": "bi-newspaper",
            "region": ".fe-press",
            "keywords": ["press", "editoriale", "magazine"],
            "cols": [
                ("magazine", {"label": "Magazine", "type": "text", "max_length": 120}),
                ("issue",    {"label": "Issue (data)", "type": "text", "max_length": 80}),
                ("title",    {"label": "Titolo pezzo", "type": "text", "max_length": 200}),
                ("byline",   {"label": "Byline (firma)", "type": "text", "max_length": 200}),
            ],
        },
        "maison.numbers_items": {
            "kind": "tuple",
            "page": "maison",
            "label": "Maison · Numbers (4 celle)",
            "icon": "bi-123",
            "region": ".fe-numbers",
            "keywords": ["numbers", "cifre"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 80}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "lookbook.credits_rows": {
            "kind": "tuple",
            "page": "lookbook",
            "label": "Lookbook · Credits (8 righe)",
            "icon": "bi-people",
            "region": ".fe-credits",
            "keywords": ["credits", "crediti", "stylist", "foto"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Ruolo", "type": "text", "max_length": 80}),
                ("value", {"label": "Nome", "type": "text", "max_length": 240}),
            ],
        },
        "lookbook.looks": {
            "kind": "dict",
            "page": "lookbook",
            "label": "Lookbook · Looks (6 look editoriali)",
            "icon": "bi-camera",
            "region": ".fe-looks",
            "keywords": ["looks", "editoriali", "lookbook"],
            "cols": [
                ("n",      {"label": "Numero look (visible · 'Look 03')", "type": "text", "max_length": 16}),
                ("title",  {"label": "Titolo look", "type": "text", "max_length": 160}),
                ("outfit", {"label": "Outfit (descrizione completa)", "type": "textarea", "max_length": 400}),
                ("credit", {"label": "Credit (atelier · stylist · set)", "type": "text", "max_length": 200}),
                ("image",  {"label": "Image · URL (rendered)", "type": "image", "max_length": 400}),
            ],
        },
        "lookbook.notes_items": {
            "kind": "dict",
            "page": "lookbook",
            "label": "Lookbook · Notes dal set (3 voci)",
            "icon": "bi-journal",
            "region": ".fe-notes",
            "keywords": ["notes", "set", "giornate"],
            "cols": [
                ("label", {"label": "Label (es. 'Giorno 01 · Salone')", "type": "text", "max_length": 160}),
                ("text",  {"label": "Testo", "type": "textarea", "max_length": 500}),
            ],
        },
        "contatti.maison_cards": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Maison cards (3 città)",
            "icon": "bi-geo-alt",
            "region": ".fe-maison-cards",
            "keywords": ["maison", "cards", "città"],
            "cols": [
                ("city",    {"label": "Città", "type": "text", "max_length": 80}),
                ("address", {"label": "Indirizzo completo", "type": "text", "max_length": 200}),
                ("phone",   {"label": "Telefono", "type": "text", "max_length": 40}),
                ("email",   {"label": "Email", "type": "text", "max_length": 120}),
                ("hours",   {"label": "Orari", "type": "text", "max_length": 160}),
            ],
        },
        "contatti.faq_items": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · FAQ (4 domande)",
            "icon": "bi-question-circle",
            "region": ".fe-faq",
            "keywords": ["faq", "domande"],
            "cols": [
                ("q", {"label": "Domanda", "type": "text", "max_length": 200}),
                ("a", {"label": "Risposta", "type": "textarea", "max_length": 500}),
            ],
        },
    },
    # -----------------------------------------------------------------
    # A.16 · Salute clinic. Sixteen indexed lists · tutti parent-level ·
    # ZERO deep-path. Image-in-dict-row on 2 lists (home.team_ribbon_people ·
    # medici.doctors = 14 image cells) · plus 1 scalar top-level
    # `studio.photo_src` = 15 image surfaces total · ALL RENDERED (clinic
    # skin renders all portraits · specialist-family precedent).
    # Stringent IN col-level (editorial visible): num (journey/how/help
    # steps) · popular_label (customer-facing badge text). Stringent
    # OUT col-level: is_popular (bool flag · no type support · Luxe
    # available precedent) · nested list-of-str (includes · items · tags ·
    # Juris precedent) · raw icon_svg (new 5th OUT category · safety +
    # poor UX for raw SVG XML editing).
    # -----------------------------------------------------------------
    "clinic": {
        "home.stats": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Stats (3 celle hero)",
            "icon": "bi-123",
            "region": ".cl-stats",
            "keywords": ["stats", "cifre", "hero"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 60}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "home.stats_strip": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Stats strip (4 celle)",
            "icon": "bi-bar-chart",
            "region": ".cl-stats-strip",
            "keywords": ["stats", "cifre", "strip"],
            "tuple_order": ["value", "label"],
            "cols": [
                ("value", {"label": "Valore", "type": "text", "max_length": 60}),
                ("label", {"label": "Etichetta", "type": "text", "max_length": 120}),
            ],
        },
        "home.specialties": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Specialties (8 reparti)",
            "icon": "bi-grid",
            "region": ".cl-specialties",
            "keywords": ["specialties", "reparti", "specialità"],
            "cols": [
                ("title",      {"label": "Titolo reparto", "type": "text", "max_length": 120}),
                ("blurb",      {"label": "Blurb", "type": "textarea", "max_length": 400}),
                ("link_label", {"label": "Link · etichetta", "type": "text", "max_length": 60}),
                # `icon_svg` col excluded (raw SVG XML · OUT per raw-SVG policy)
            ],
        },
        "home.journey_steps": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Journey steps (4 passi)",
            "icon": "bi-arrow-right-circle",
            "region": ".cl-journey",
            "keywords": ["journey", "percorso", "steps"],
            "cols": [
                ("num",   {"label": "Step ('01'/'02'/...)", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo step", "type": "text", "max_length": 160}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "home.prevenzione_cards": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Prevenzione cards (3 pacchetti)",
            "icon": "bi-heart-pulse",
            "region": ".cl-prev-cards",
            "keywords": ["prevenzione", "cards", "pacchetti"],
            "cols": [
                ("eyebrow",         {"label": "Eyebrow", "type": "text", "max_length": 80}),
                ("title",           {"label": "Titolo pacchetto", "type": "text", "max_length": 160}),
                ("desc",            {"label": "Descrizione", "type": "textarea", "max_length": 500}),
                ("duration_label",  {"label": "Duration · label", "type": "text", "max_length": 40}),
                ("duration",        {"label": "Duration · valore", "type": "text", "max_length": 80}),
                ("price_label",     {"label": "Price · label", "type": "text", "max_length": 60}),
                ("price",           {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
                ("cta",             {"label": "CTA etichetta", "type": "text", "max_length": 60}),
                # `includes` col excluded (nested list-of-str · Juris precedent)
            ],
        },
        "home.team_ribbon_people": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Team ribbon (8 medici in home)",
            "icon": "bi-person-circle",
            "region": ".cl-team-ribbon",
            "keywords": ["team", "ribbon", "medici", "home"],
            "cols": [
                ("name",      {"label": "Nome medico", "type": "text", "max_length": 120}),
                ("specialty", {"label": "Specialità", "type": "text", "max_length": 120}),
                ("avatar",    {"label": "Avatar · URL (rendered)", "type": "image", "max_length": 400}),
            ],
        },
        "studio.values": {
            "kind": "dict",
            "page": "studio",
            "label": "Studio · Values (4 valori)",
            "icon": "bi-stars",
            "region": ".cl-values",
            "keywords": ["values", "valori", "studio"],
            "cols": [
                ("title", {"label": "Titolo valore", "type": "text", "max_length": 120}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "studio.timeline": {
            "kind": "dict",
            "page": "studio",
            "label": "Studio · Timeline (4 tappe storiche)",
            "icon": "bi-clock-history",
            "region": ".cl-timeline",
            "keywords": ["timeline", "storia", "tappe"],
            "cols": [
                ("year",  {"label": "Anno", "type": "text", "max_length": 40}),
                ("title", {"label": "Titolo tappa", "type": "text", "max_length": 160}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "servizi.services": {
            "kind": "dict",
            "page": "servizi",
            "label": "Servizi · Services (10 visite)",
            "icon": "bi-clipboard-pulse",
            "region": ".cl-services",
            "keywords": ["servizi", "services", "visite"],
            "cols": [
                ("eyebrow", {"label": "Eyebrow (specialità)", "type": "text", "max_length": 80}),
                ("title",   {"label": "Titolo visita", "type": "text", "max_length": 200}),
                ("desc",    {"label": "Descrizione", "type": "textarea", "max_length": 500}),
                ("price",   {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
                # `icon_svg` col excluded (raw SVG XML · OUT)
                # `items` col excluded (nested list-of-str · Juris precedent)
            ],
        },
        "servizi.faqs": {
            "kind": "tuple",
            "page": "servizi",
            "label": "Servizi · FAQs (3 domande)",
            "icon": "bi-question-circle",
            "region": ".cl-faq",
            "keywords": ["faq", "domande"],
            "tuple_order": ["q", "a"],
            "cols": [
                ("q", {"label": "Domanda", "type": "text", "max_length": 200}),
                ("a", {"label": "Risposta", "type": "textarea", "max_length": 600}),
            ],
        },
        "prevenzione.packages": {
            "kind": "dict",
            "page": "prevenzione",
            "label": "Prevenzione · Packages (3 check-up)",
            "icon": "bi-heart-pulse",
            "region": ".cl-packages",
            "keywords": ["packages", "check-up", "prevenzione"],
            "cols": [
                ("eyebrow",       {"label": "Eyebrow (fascia età)", "type": "text", "max_length": 80}),
                ("title",         {"label": "Titolo pacchetto", "type": "text", "max_length": 160}),
                ("desc",          {"label": "Descrizione", "type": "textarea", "max_length": 500}),
                ("price",         {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
                ("price_meta",    {"label": "Prezzo · meta (es. 'tutto incluso')", "type": "text", "max_length": 80}),
                ("duration",      {"label": "Durata", "type": "text", "max_length": 80}),
                ("exams_count",   {"label": "Numero esami (display)", "type": "text", "max_length": 40}),
                ("cta",           {"label": "CTA etichetta", "type": "text", "max_length": 60}),
                ("popular_label", {"label": "Badge 'popular' etichetta", "type": "text", "max_length": 60}),
                # `is_popular` col excluded (bool flag · Luxe available precedent · preserves popular_label editability)
                # `includes` col excluded (nested list-of-str · Juris precedent)
            ],
        },
        "prevenzione.how_steps": {
            "kind": "dict",
            "page": "prevenzione",
            "label": "Prevenzione · How steps (4 passi)",
            "icon": "bi-arrow-right-circle",
            "region": ".cl-how-steps",
            "keywords": ["how", "steps", "passi"],
            "cols": [
                ("num",   {"label": "Step ('01'/'02'/...)", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo step", "type": "text", "max_length": 160}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "medici.doctors": {
            "kind": "dict",
            "page": "medici",
            "label": "Medici · Doctors (6 specialisti)",
            "icon": "bi-people",
            "region": ".cl-doctors",
            "keywords": ["medici", "doctors", "specialisti"],
            "cols": [
                ("name",        {"label": "Nome medico", "type": "text", "max_length": 120}),
                ("role",        {"label": "Ruolo / specializzazione", "type": "text", "max_length": 200}),
                ("credentials", {"label": "Credenziali / bio", "type": "textarea", "max_length": 800}),
                ("portrait",    {"label": "Portrait · URL (rendered)", "type": "image", "max_length": 400}),
                # `tags` col excluded (nested list-of-str · Juris precedent)
            ],
        },
        "contatti.hours_table": {
            "kind": "tuple",
            "page": "contatti",
            "label": "Contatti · Hours (4 righe)",
            "icon": "bi-clock",
            "region": ".cl-hours-table",
            "keywords": ["hours", "orari"],
            "tuple_order": ["day", "value"],
            "cols": [
                ("day",   {"label": "Giorno / range", "type": "text", "max_length": 120}),
                ("value", {"label": "Orario", "type": "text", "max_length": 120}),
            ],
        },
        "contatti.access": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Access (4 modalità)",
            "icon": "bi-signpost",
            "region": ".cl-access",
            "keywords": ["access", "come-raggiungerci", "parcheggio"],
            "cols": [
                ("icon",  {"label": "Icon nome (Bootstrap icon · es. 'car')", "type": "text", "max_length": 40}),
                ("title", {"label": "Titolo", "type": "text", "max_length": 120}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "prenota.help_steps": {
            "kind": "dict",
            "page": "prenota",
            "label": "Prenota · Help steps (4 passi)",
            "icon": "bi-info-circle",
            "region": ".cl-help-steps",
            "keywords": ["help", "steps", "passi"],
            "cols": [
                ("num",   {"label": "Step ('01'/'02'/...)", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo step", "type": "text", "max_length": 160}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
    },
    # -----------------------------------------------------------------
    # A.16b · Benessere wellness. Seventeen indexed lists · tutti
    # parent-level · ZERO deep-path. Image-in-dict-row on 3 lists
    # (ambienti.rooms × 8 + home.therapists_trio × 3 + professionisti.people
    # × 5 = 16 image cells) · plus 3 scalar top-level (home.hero_image +
    # filosofia.photo_image + contatti.map_image) = 19 image surfaces
    # total. All rendered (editorial olistico skin · no storage-only
    # split). Stringent IN col-level (editorial visible): day/num/month
    # (calendar) + num (journey) + init (pillars) + tag (packages).
    # Stringent OUT col-level: has_slots/soldout bool flags on both
    # calendar lists (scheduler-state-like · Luxe available + Salute
    # is_popular precedent) · slots nested list-of-str on both calendar
    # lists + includes + tags + interest_options (Juris precedent).
    # DEFERRED from first wave: home.ambients tuple-with-image (4 tiles ·
    # novel shape · ZERO precedent · whole list OUT via complex-shape
    # exclusion in perimeter test).
    # -----------------------------------------------------------------
    "wellness": {
        "site.socials": {
            "kind": "tuple",
            "page": "*",
            "label": "Site · Socials (3 celle footer)",
            "icon": "bi-link-45deg",
            "region": ".we-foot",
            "keywords": ["socials", "footer"],
            "tuple_order": ["label", "url"],
            "cols": [
                ("label", {"label": "Etichetta social", "type": "text", "max_length": 40}),
                ("url",   {"label": "URL", "type": "url", "max_length": 300}),
            ],
        },
        "home.rituali": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Rituali (4 trattamenti in evidenza)",
            "icon": "bi-flower1",
            "region": ".we-home-rituali",
            "keywords": ["rituali", "home", "trattamenti"],
            "tuple_order": ["name", "desc", "price"],
            "cols": [
                ("name",  {"label": "Nome rituale", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione (durata · materiali)", "type": "textarea", "max_length": 400}),
                ("price", {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
            ],
        },
        "home.benefits": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Benefits (3 parole chiave)",
            "icon": "bi-heart",
            "region": ".we-benefits",
            "keywords": ["benefits", "home", "parole"],
            "tuple_order": ["title", "body"],
            "cols": [
                ("title", {"label": "Parola chiave", "type": "text", "max_length": 80}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "home.therapists_trio": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Therapists trio (3 operatori)",
            "icon": "bi-person-heart",
            "region": ".we-therapists-trio",
            "keywords": ["therapists", "trio", "home", "operatori"],
            "cols": [
                ("name",     {"label": "Nome operatore", "type": "text", "max_length": 120}),
                ("role",     {"label": "Ruolo", "type": "text", "max_length": 160}),
                ("bio",      {"label": "Bio breve", "type": "textarea", "max_length": 500}),
                ("portrait", {"label": "Portrait · URL (rendered)", "type": "image", "max_length": 400}),
            ],
        },
        "home.journey": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Journey (4 passi del rituale)",
            "icon": "bi-arrow-right-circle",
            "region": ".we-journey",
            "keywords": ["journey", "home", "passi"],
            "cols": [
                ("num",   {"label": "Step ('01'/'02'/...)", "type": "text", "max_length": 8}),
                ("title", {"label": "Titolo step", "type": "text", "max_length": 160}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "home.calendar": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Calendar (7 giorni disponibilità · demo display)",
            "icon": "bi-calendar3",
            "region": ".we-calendar",
            "keywords": ["calendar", "home", "giorni"],
            "cols": [
                ("day",   {"label": "Giorno abbreviato ('Lun'/'Mar'/...)", "type": "text", "max_length": 16}),
                ("num",   {"label": "Numero giorno ('14'/'15'/...)", "type": "text", "max_length": 8}),
                ("month", {"label": "Mese abbreviato ('Apr'/...)", "type": "text", "max_length": 16}),
                # `slots` col excluded (nested list-of-str · time-slots · Juris precedent)
                # `has_slots` col excluded (bool · scheduler-state-like · Luxe available precedent)
                # `soldout` col excluded (bool · scheduler-state-like · Luxe available precedent)
            ],
        },
        "filosofia.pillars": {
            "kind": "dict",
            "page": "filosofia",
            "label": "Filosofia · Pillars (3 parole cardine)",
            "icon": "bi-stars",
            "region": ".we-pillars",
            "keywords": ["pillars", "filosofia", "parole"],
            "cols": [
                ("init",  {"label": "Iniziale grafica ('A'/'B'/...)", "type": "text", "max_length": 4}),
                ("title", {"label": "Titolo pillar", "type": "text", "max_length": 120}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "filosofia.timeline": {
            "kind": "dict",
            "page": "filosofia",
            "label": "Filosofia · Timeline (4 tappe storiche)",
            "icon": "bi-clock-history",
            "region": ".we-timeline",
            "keywords": ["timeline", "storia", "tappe"],
            "cols": [
                ("year",  {"label": "Anno", "type": "text", "max_length": 40}),
                ("title", {"label": "Titolo tappa", "type": "text", "max_length": 160}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "rituali.treatments": {
            "kind": "dict",
            "page": "rituali",
            "label": "Rituali · Treatments (10 trattamenti listino)",
            "icon": "bi-flower2",
            "region": ".we-treatments",
            "keywords": ["treatments", "rituali", "listino"],
            "cols": [
                ("name",  {"label": "Nome rituale", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
                ("meta",  {"label": "Meta (durata · materia · operatore)", "type": "text", "max_length": 240}),
                ("price", {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
            ],
        },
        "rituali.advice": {
            "kind": "dict",
            "page": "rituali",
            "label": "Rituali · Advice (3 raccomandazioni)",
            "icon": "bi-info-circle",
            "region": ".we-advice",
            "keywords": ["advice", "raccomandazioni"],
            "cols": [
                ("title", {"label": "Titolo raccomandazione", "type": "text", "max_length": 160}),
                ("body",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "rituali.packages": {
            "kind": "dict",
            "page": "rituali",
            "label": "Rituali · Packages (2 soggiorni retreat)",
            "icon": "bi-bag-heart",
            "region": ".we-packages",
            "keywords": ["packages", "retreat", "soggiorni"],
            "cols": [
                ("tag",      {"label": "Tag (editorial category · 'Giornata singola')", "type": "text", "max_length": 60}),
                ("title",    {"label": "Titolo pacchetto", "type": "text", "max_length": 160}),
                ("duration", {"label": "Durata sintetica", "type": "text", "max_length": 200}),
                ("desc",     {"label": "Descrizione", "type": "textarea", "max_length": 700}),
                ("price",    {"label": "Prezzo (display)", "type": "text", "max_length": 40}),
                ("cta",      {"label": "CTA etichetta", "type": "text", "max_length": 60}),
                # `includes` col excluded (nested list-of-str · Juris precedent)
            ],
        },
        "ambienti.rooms": {
            "kind": "dict",
            "page": "ambienti",
            "label": "Ambienti · Rooms (8 sale · novel `gallery` kind)",
            "icon": "bi-door-closed",
            "region": ".we-rooms",
            "keywords": ["rooms", "sale", "gallery", "ambienti"],
            "cols": [
                ("span",  {"label": "Span grid (a/b/c · controllo layout)", "type": "text", "max_length": 4}),
                ("tag",   {"label": "Tag (numerazione sala · 'Sala I · Hammam')", "type": "text", "max_length": 80}),
                ("title", {"label": "Titolo sala", "type": "text", "max_length": 160}),
                ("sub",   {"label": "Sottotitolo / descrizione", "type": "textarea", "max_length": 500}),
                ("image", {"label": "Image · URL (rendered)", "type": "image", "max_length": 400}),
            ],
        },
        "professionisti.people": {
            "kind": "dict",
            "page": "professionisti",
            "label": "Professionisti · People (5 operatori)",
            "icon": "bi-people",
            "region": ".we-people",
            "keywords": ["professionisti", "people", "operatori"],
            "cols": [
                ("name",     {"label": "Nome operatore", "type": "text", "max_length": 120}),
                ("role",     {"label": "Ruolo / specializzazione", "type": "text", "max_length": 200}),
                ("portrait", {"label": "Portrait · URL (rendered)", "type": "image", "max_length": 400}),
                ("bio",      {"label": "Bio estesa", "type": "textarea", "max_length": 800}),
                ("quote",    {"label": "Quote breve", "type": "textarea", "max_length": 400}),
                # `tags` col excluded (nested list-of-str · Juris precedent)
            ],
        },
        "contatti.blocks": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Blocks (4 card informative)",
            "icon": "bi-grid-3x3-gap",
            "region": ".we-blocks",
            "keywords": ["contatti", "blocks", "card"],
            "cols": [
                ("label", {"label": "Label", "type": "text", "max_length": 80}),
                ("value", {"label": "Valore", "type": "text", "max_length": 200}),
                ("sub",   {"label": "Sub / nota", "type": "textarea", "max_length": 300}),
            ],
        },
        "contatti.access": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Access (3 modalità)",
            "icon": "bi-signpost",
            "region": ".we-access",
            "keywords": ["access", "come-raggiungerci"],
            "cols": [
                ("mode", {"label": "Modalità (a piedi/auto/funicolare)", "type": "text", "max_length": 80}),
                ("text", {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "contatti.hours": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Hours (7 giorni)",
            "icon": "bi-clock",
            "region": ".we-hours",
            "keywords": ["hours", "orari"],
            "cols": [
                ("day",   {"label": "Giorno / range", "type": "text", "max_length": 120}),
                ("value", {"label": "Orario", "type": "text", "max_length": 120}),
            ],
        },
        "prenota.calendar": {
            "kind": "dict",
            "page": "prenota",
            "label": "Prenota · Calendar (7 giorni disponibilità · demo display)",
            "icon": "bi-calendar3",
            "region": ".we-prenota-calendar",
            "keywords": ["calendar", "prenota", "giorni"],
            "cols": [
                ("day",   {"label": "Giorno abbreviato ('Lun'/'Mar'/...)", "type": "text", "max_length": 16}),
                ("num",   {"label": "Numero giorno ('14'/'15'/...)", "type": "text", "max_length": 8}),
                ("month", {"label": "Mese abbreviato ('Apr'/...)", "type": "text", "max_length": 16}),
                # `slots` col excluded (nested list-of-str · time-slots · Juris precedent)
                # `has_slots` col excluded (bool · scheduler-state-like · Luxe available precedent · mirrors home.calendar)
                # `soldout` col excluded (bool · scheduler-state-like · Luxe available precedent · mirrors home.calendar)
            ],
        },
    },
    # -----------------------------------------------------------------
    # A.16c · Famiglia family. Twenty indexed lists · 16 parent-level
    # (12 dict + 4 tuple) + 4 DEEP-PATH (`crescita.topics.{0..3}.items`
    # · mechanical reuse of Sapore `menu.sections.{0..4}.dishes` pattern ·
    # f66ac24 render-side contract-alignment fix already covers path
    # walk). Image-in-dict-row on 3 lists (home.doctors × 4 + home.gallery
    # × 5 + pediatre.doctors × 4 = 13 image cells) · plus 3 scalar
    # top-level (home.hero_image + studio.studio_image + contatti.map_image)
    # = 16 image surfaces total · all rendered (pediatric skin · no
    # storage-only split). Novel col name `src` on home.gallery (vs
    # prior `image`/`portrait`/`avatar` · mechanical reuse via col
    # registration). Stringent IN col-level 7th archetype: `meta`
    # (editorial area labels) · `icon` (Bootstrap text refs · NOT raw
    # SVG) · `tag`/`exp_label`/`exp_value`/`wa_label`/`age` (editorial
    # visible). Stringent OUT col-level: `items` on home.age_groups +
    # `specs` on pediatre.doctors (nested list-of-str · Juris precedent) ·
    # `items` on crescita.topics parent (deep-path excluded at parent
    # level · IN via 4 sub-path entries). Zero raw SVG · zero bool
    # flags · zero form_fields list-of-dict (form exposed as flat
    # scalars · simpler than Benessere).
    # -----------------------------------------------------------------
    "family": {
        "home.trust_items": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Trust items (3 chip iniziali)",
            "icon": "bi-patch-check",
            "region": ".fm-trust",
            "keywords": ["trust", "home", "convenzioni"],
            "cols": [
                ("icon",  {"label": "Icon (Bootstrap icon name · es. 'clock')", "type": "text", "max_length": 40}),
                ("label", {"label": "Label", "type": "text", "max_length": 200}),
            ],
        },
        "home.age_groups": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Age groups (3 fasce di età)",
            "icon": "bi-diagram-3",
            "region": ".fm-age-groups",
            "keywords": ["age", "groups", "fasce"],
            "cols": [
                ("icon",  {"label": "Icon (Bootstrap icon name)", "type": "text", "max_length": 40}),
                ("range", {"label": "Range età (editorial visible · '0–2 anni')", "type": "text", "max_length": 60}),
                ("title", {"label": "Titolo fascia", "type": "text", "max_length": 160}),
                ("blurb", {"label": "Blurb", "type": "textarea", "max_length": 600}),
                # `items` col excluded (nested list-of-str · 3 per row · Juris precedent)
            ],
        },
        "home.doctors": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Doctors (4 pediatre in home)",
            "icon": "bi-person-heart",
            "region": ".fm-team-ribbon",
            "keywords": ["doctors", "team", "home", "pediatre"],
            "cols": [
                ("name",     {"label": "Nome pediatra", "type": "text", "max_length": 120}),
                ("role",     {"label": "Ruolo", "type": "text", "max_length": 160}),
                ("spec",     {"label": "Specializzazione", "type": "text", "max_length": 160}),
                ("wa_label", {"label": "WhatsApp · etichetta CTA", "type": "text", "max_length": 60}),
                ("portrait", {"label": "Portrait · URL (rendered)", "type": "image", "max_length": 400}),
            ],
        },
        "home.journey_steps": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Journey steps (5 tappe crescita)",
            "icon": "bi-arrow-right-circle",
            "region": ".fm-journey",
            "keywords": ["journey", "steps", "crescita"],
            "cols": [
                ("age",   {"label": "Range età ('0–2'/'3–5'/...)", "type": "text", "max_length": 60}),
                ("title", {"label": "Titolo tappa", "type": "text", "max_length": 160}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "home.faq": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · FAQ (8 domande genitori)",
            "icon": "bi-question-circle",
            "region": ".fm-faq",
            "keywords": ["faq", "home", "domande"],
            "tuple_order": ["q", "a"],
            "cols": [
                ("q", {"label": "Domanda", "type": "text", "max_length": 240}),
                ("a", {"label": "Risposta", "type": "textarea", "max_length": 600}),
            ],
        },
        "home.gallery": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Gallery (5 immagini studio)",
            "icon": "bi-images",
            "region": ".fm-gallery",
            "keywords": ["gallery", "home", "studio"],
            "cols": [
                ("cap", {"label": "Didascalia", "type": "text", "max_length": 200}),
                ("src", {"label": "Image · URL (rendered · novel col name)", "type": "image", "max_length": 400}),
            ],
        },
        "home.hours": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Hours (4 righe orari)",
            "icon": "bi-clock",
            "region": ".fm-hours",
            "keywords": ["hours", "home", "orari"],
            "tuple_order": ["day", "value"],
            "cols": [
                ("day",   {"label": "Giorno / range", "type": "text", "max_length": 120}),
                ("value", {"label": "Orario", "type": "text", "max_length": 120}),
            ],
        },
        "studio.values": {
            "kind": "dict",
            "page": "studio",
            "label": "Studio · Values (4 valori)",
            "icon": "bi-stars",
            "region": ".fm-values",
            "keywords": ["values", "studio", "valori"],
            "cols": [
                ("icon",  {"label": "Icon (Bootstrap icon name)", "type": "text", "max_length": 40}),
                ("title", {"label": "Titolo valore", "type": "text", "max_length": 120}),
                ("desc",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "studio.history": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · History (4 tappe storiche)",
            "icon": "bi-clock-history",
            "region": ".fm-history",
            "keywords": ["history", "storia", "tappe"],
            "tuple_order": ["year", "desc"],
            "cols": [
                ("year", {"label": "Anno / range", "type": "text", "max_length": 60}),
                ("desc", {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "visite.visits": {
            "kind": "dict",
            "page": "visite",
            "label": "Visite · Visits (8 tipi di visita)",
            "icon": "bi-clipboard-pulse",
            "region": ".fm-visits",
            "keywords": ["visits", "visite"],
            "cols": [
                ("icon",        {"label": "Icon (Bootstrap icon name)", "type": "text", "max_length": 40}),
                ("title",       {"label": "Titolo visita", "type": "text", "max_length": 160}),
                ("duration",    {"label": "Durata (display · '45 min · 0–12 mesi')", "type": "text", "max_length": 200}),
                ("desc",        {"label": "Descrizione", "type": "textarea", "max_length": 700}),
                ("bring_label", {"label": "Bring · label", "type": "text", "max_length": 60}),
                ("bring",       {"label": "Bring · cose da portare", "type": "textarea", "max_length": 400}),
                ("cta_label",   {"label": "CTA · etichetta", "type": "text", "max_length": 60}),
            ],
        },
        "visite.tips": {
            "kind": "dict",
            "page": "visite",
            "label": "Visite · Tips (3 consigli)",
            "icon": "bi-info-circle",
            "region": ".fm-tips",
            "keywords": ["tips", "consigli"],
            "cols": [
                ("title", {"label": "Titolo consiglio", "type": "text", "max_length": 160}),
                ("text",  {"label": "Descrizione", "type": "textarea", "max_length": 500}),
            ],
        },
        "crescita.topics": {
            "kind": "dict",
            "page": "crescita",
            "label": "Crescita · Topics (4 aree · DEEP-PATH parent)",
            "icon": "bi-grid-3x3",
            "region": ".fm-topics",
            "keywords": ["crescita", "topics", "aree", "faq"],
            "cols": [
                ("icon",  {"label": "Icon (Bootstrap icon name)", "type": "text", "max_length": 40}),
                ("meta",  {"label": "Meta (editorial · 'Area 01')", "type": "text", "max_length": 60}),
                ("title", {"label": "Titolo area", "type": "text", "max_length": 160}),
                ("intro", {"label": "Intro area", "type": "textarea", "max_length": 700}),
                # `items` col excluded at parent level (deep-path · Q&A
                # tuples editable via 4 sub-path entries sotto)
            ],
        },
        # DEEP-PATH entries · mechanical reuse of Sapore menu.sections.{i}.dishes
        # pattern via f66ac24 render-side contract-alignment fix · 4 topics ×
        # 4 tuple-rows × 2 cols = 32 editable cells total. Each topic's
        # `items` list is a tuple-in-dict-list (list-parent walk via f66ac24).
        "crescita.topics.0.items": {
            "kind": "tuple",
            "page": "crescita",
            "label": "Crescita · Topic 1 · Items (4 Q&A)",
            "icon": "bi-patch-question",
            "region": ".fm-topics",
            "keywords": ["crescita", "items", "qa", "topic1"],
            "tuple_order": ["q", "a"],
            "cols": [
                ("q", {"label": "Domanda", "type": "text", "max_length": 240}),
                ("a", {"label": "Risposta", "type": "textarea", "max_length": 700}),
            ],
        },
        "crescita.topics.1.items": {
            "kind": "tuple",
            "page": "crescita",
            "label": "Crescita · Topic 2 · Items (4 Q&A)",
            "icon": "bi-patch-question",
            "region": ".fm-topics",
            "keywords": ["crescita", "items", "qa", "topic2"],
            "tuple_order": ["q", "a"],
            "cols": [
                ("q", {"label": "Domanda", "type": "text", "max_length": 240}),
                ("a", {"label": "Risposta", "type": "textarea", "max_length": 700}),
            ],
        },
        "crescita.topics.2.items": {
            "kind": "tuple",
            "page": "crescita",
            "label": "Crescita · Topic 3 · Items (4 Q&A)",
            "icon": "bi-patch-question",
            "region": ".fm-topics",
            "keywords": ["crescita", "items", "qa", "topic3"],
            "tuple_order": ["q", "a"],
            "cols": [
                ("q", {"label": "Domanda", "type": "text", "max_length": 240}),
                ("a", {"label": "Risposta", "type": "textarea", "max_length": 700}),
            ],
        },
        "crescita.topics.3.items": {
            "kind": "tuple",
            "page": "crescita",
            "label": "Crescita · Topic 4 · Items (4 Q&A)",
            "icon": "bi-patch-question",
            "region": ".fm-topics",
            "keywords": ["crescita", "items", "qa", "topic4"],
            "tuple_order": ["q", "a"],
            "cols": [
                ("q", {"label": "Domanda", "type": "text", "max_length": 240}),
                ("a", {"label": "Risposta", "type": "textarea", "max_length": 700}),
            ],
        },
        "crescita.materials": {
            "kind": "dict",
            "page": "crescita",
            "label": "Crescita · Materials (3 PDF scaricabili)",
            "icon": "bi-file-earmark-pdf",
            "region": ".fm-materials",
            "keywords": ["materials", "pdf", "download"],
            "cols": [
                ("title",    {"label": "Titolo materiale", "type": "text", "max_length": 160}),
                ("desc",     {"label": "Descrizione", "type": "textarea", "max_length": 400}),
                ("size",     {"label": "Size (display · '2.1 MB')", "type": "text", "max_length": 40}),
                ("dl_label", {"label": "Download · etichetta CTA", "type": "text", "max_length": 60}),
            ],
        },
        "pediatre.doctors": {
            "kind": "dict",
            "page": "pediatre",
            "label": "Pediatre · Doctors (4 pediatre)",
            "icon": "bi-people",
            "region": ".fm-doctors",
            "keywords": ["doctors", "pediatre", "team"],
            "cols": [
                ("name",      {"label": "Nome pediatra", "type": "text", "max_length": 120}),
                ("role",      {"label": "Ruolo", "type": "text", "max_length": 200}),
                ("tag",       {"label": "Tag editorial ('Fondatrice')", "type": "text", "max_length": 60}),
                ("bio",       {"label": "Bio estesa", "type": "textarea", "max_length": 800}),
                ("exp_label", {"label": "Experience · label", "type": "text", "max_length": 60}),
                ("exp_value", {"label": "Experience · value", "type": "text", "max_length": 200}),
                ("wa_label",  {"label": "WhatsApp · etichetta CTA", "type": "text", "max_length": 60}),
                ("portrait",  {"label": "Portrait · URL (rendered)", "type": "image", "max_length": 400}),
                # `specs` col excluded (nested list-of-str · 3 per doctor · Juris precedent)
            ],
        },
        "contatti.travel": {
            "kind": "dict",
            "page": "contatti",
            "label": "Contatti · Travel (3 modalità)",
            "icon": "bi-signpost",
            "region": ".fm-travel",
            "keywords": ["travel", "come-raggiungerci"],
            "cols": [
                ("icon",  {"label": "Icon (Bootstrap icon name)", "type": "text", "max_length": 40}),
                ("title", {"label": "Titolo modalità", "type": "text", "max_length": 120}),
                ("text",  {"label": "Descrizione", "type": "textarea", "max_length": 400}),
            ],
        },
        "contatti.hours": {
            "kind": "tuple",
            "page": "contatti",
            "label": "Contatti · Hours (4 righe orari)",
            "icon": "bi-clock",
            "region": ".fm-contact-hours",
            "keywords": ["hours", "contatti", "orari"],
            "tuple_order": ["day", "value"],
            "cols": [
                ("day",   {"label": "Giorno / range", "type": "text", "max_length": 120}),
                ("value", {"label": "Orario", "type": "text", "max_length": 120}),
            ],
        },
    },

    # A.17 · Aura (agency-digital-studio) — 18 indexed lists · zero
    # deep-path · all 12 image cells are image-in-dict-row at
    # `<list>.{i}.<col>`. Nested list-of-str cols (tags · stack · scope ·
    # includes) excluded (Juris precedent · 6-archetype chain). Nested
    # list-of-tuple `kpi` inside lavori.projects excluded col-level
    # (no sub-tuple-list kind). bool `featured` on engagement_tiles
    # excluded col-level (bool stays OUT · 4 OUT-category precedent).
    # `slug` cols excluded (structural identifier). `output` on
    # home.sprints IN as stringent editorial tag.
    "agency-digital-studio": {

        # ── BRAND ───────────────────────────────────────────────────────
        "site.foot_shiplog_rows": {
            "kind": "tuple",
            "page": "*",
            "label": "Footer · Ship log (6 righe · stringent IN)",
            "icon": "bi-terminal",
            "region": ".au-foot .shiplog",
            "keywords": ["shiplog", "footer", "versioni", "deploy"],
            "tuple_order": ["date", "ver", "desc"],
            "cols": [
                ("date", {"label": "Data (es. 'ieri · 18:04')", "type": "text", "max_length": 40}),
                ("ver",  {"label": "Versione (es. 'v2.14')",   "type": "text", "max_length": 20}),
                ("desc", {"label": "Descrizione deploy",        "type": "textarea", "max_length": 300}),
            ],
        },

        # ── HOME ────────────────────────────────────────────────────────
        "home.hero_metrics": {
            "kind": "tuple",
            "page": "home",
            "label": "Hero home · Metriche (3 tuple)",
            "icon": "bi-bar-chart",
            "region": ".au-hero .metric",
            "keywords": ["hero", "metrics", "kpi", "numeri"],
            "tuple_order": ["num", "label"],
            "cols": [
                ("num",   {"label": "Numero (richtext · <em>)", "type": "richtext", "max_length": 80}),
                ("label", {"label": "Label",                     "type": "text", "max_length": 160}),
            ],
        },
        "home.console.kpi": {
            "kind": "tuple",
            "page": "home",
            "label": "Console home · KPI (4 tuple)",
            "icon": "bi-speedometer2",
            "region": ".au-console .kpi",
            "keywords": ["console", "kpi", "dashboard"],
            "tuple_order": ["num", "label"],
            "cols": [
                ("num",   {"label": "Numero (richtext · <em>)", "type": "richtext", "max_length": 80}),
                ("label", {"label": "Label",                     "type": "text", "max_length": 200}),
            ],
        },
        "home.capab_cards": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Capab cards (4 card)",
            "icon": "bi-gem",
            "region": ".au-capab .card",
            "keywords": ["capab", "cards", "home", "aree"],
            "cols": [
                ("id",    {"label": "ID card (es. 'C.01')", "type": "text", "max_length": 20}),
                ("title", {"label": "Titolo (richtext · <em>)", "type": "richtext", "max_length": 160}),
                ("body",  {"label": "Body", "type": "textarea", "max_length": 500}),
                # `tags` col excluded (nested list-of-str · 4 per row · Juris precedent)
            ],
        },
        "home.sprints": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Sprint strip (4 sprint)",
            "icon": "bi-arrow-right-circle",
            "region": ".au-sprints .sprint-card",
            "keywords": ["sprint", "strip", "home", "fasi"],
            "cols": [
                ("id",       {"label": "ID sprint (es. 'S.00')", "type": "text", "max_length": 20}),
                ("duration", {"label": "Durata (es. 'Sprint 0 · 1 settimana')", "type": "text", "max_length": 120}),
                ("title",    {"label": "Titolo (richtext · <em>)", "type": "richtext", "max_length": 80}),
                ("body",     {"label": "Body", "type": "textarea", "max_length": 500}),
                ("output",   {"label": "Output tag (stringent IN · es. 'OUT · brief + backlog')", "type": "text", "max_length": 120}),
            ],
        },
        "home.work_cards": {
            "kind": "dict",
            "page": "home",
            "label": "Home · Work cards (3 progetti featured)",
            "icon": "bi-images",
            "region": ".au-work .card",
            "keywords": ["work", "cards", "home", "lavori", "image"],
            "cols": [
                ("id",          {"label": "ID card (es. 'W.01')", "type": "text", "max_length": 20}),
                ("title",       {"label": "Titolo progetto", "type": "text", "max_length": 160}),
                ("client",      {"label": "Cliente", "type": "text", "max_length": 120}),
                ("metric_chip", {"label": "Metric chip (es. '+18% retention · D30')", "type": "text", "max_length": 120}),
                ("cover",       {"label": "Cover · URL (rendered)", "type": "image", "max_length": 400}),
                # `slug` col excluded (structural identifier for detail page routing)
                # `stack` col excluded (nested list-of-str · Juris precedent)
            ],
        },
        "home.metric_strip": {
            "kind": "tuple",
            "page": "home",
            "label": "Home · Metric strip (4 tuple)",
            "icon": "bi-graph-up",
            "region": ".au-metric-band .stat",
            "keywords": ["metric", "strip", "home", "band"],
            "tuple_order": ["num", "label", "note"],
            "cols": [
                ("num",   {"label": "Numero (richtext · <em>)", "type": "richtext", "max_length": 80}),
                ("label", {"label": "Label",                     "type": "text", "max_length": 120}),
                ("note",  {"label": "Nota",                      "type": "text", "max_length": 200}),
            ],
        },

        # ── STUDIO (about) ──────────────────────────────────────────────
        "studio.facts": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Facts (4 tuple)",
            "icon": "bi-123",
            "region": ".au-studio-facts",
            "keywords": ["facts", "studio", "numeri"],
            "tuple_order": ["num", "label", "note"],
            "cols": [
                ("num",   {"label": "Numero (richtext · <em>)", "type": "richtext", "max_length": 80}),
                ("label", {"label": "Label",                     "type": "text", "max_length": 80}),
                ("note",  {"label": "Nota",                      "type": "text", "max_length": 200}),
            ],
        },
        "studio.team": {
            "kind": "dict",
            "page": "studio",
            "label": "Studio · Team (3 persone)",
            "icon": "bi-people",
            "region": ".au-team .member",
            "keywords": ["team", "persone", "bio", "portrait"],
            "cols": [
                ("name",     {"label": "Nome", "type": "text", "max_length": 120}),
                ("role",     {"label": "Ruolo", "type": "text", "max_length": 200}),
                ("bio",      {"label": "Bio",   "type": "textarea", "max_length": 800}),
                ("portrait", {"label": "Portrait · URL (rendered)", "type": "image", "max_length": 400}),
                # `stack` col excluded (nested list-of-str · Juris precedent)
            ],
        },
        "studio.values": {
            "kind": "tuple",
            "page": "studio",
            "label": "Studio · Values (4 tuple)",
            "icon": "bi-compass",
            "region": ".au-values",
            "keywords": ["values", "valori", "principi"],
            "tuple_order": ["id", "title", "body"],
            "cols": [
                ("id",    {"label": "ID (es. 'V.01')",            "type": "text", "max_length": 20}),
                ("title", {"label": "Titolo (richtext · <em>)", "type": "richtext", "max_length": 200}),
                ("body",  {"label": "Body",                       "type": "textarea", "max_length": 500}),
            ],
        },

        # ── CAPABILITIES (services) ─────────────────────────────────────
        "capabilities.capabilities": {
            "kind": "dict",
            "page": "capabilities",
            "label": "Capabilities · Capabilities (4 card)",
            "icon": "bi-gem",
            "region": ".au-capab .card",
            "keywords": ["capabilities", "services", "card"],
            "cols": [
                ("id",          {"label": "ID (es. 'CAP.01 · Product launch')", "type": "text", "max_length": 80}),
                ("title",       {"label": "Titolo (richtext · <em>)", "type": "richtext", "max_length": 200}),
                ("tagline",     {"label": "Tagline (durata + KPI)", "type": "text", "max_length": 200}),
                ("body",        {"label": "Body", "type": "textarea", "max_length": 800}),
                ("scope_label", {"label": "Scope · label (stringent IN)", "type": "text", "max_length": 40}),
                # `scope` col excluded (nested list-of-str · 8 per row · Juris precedent)
                # `stack` col excluded (nested list-of-str · Juris precedent)
            ],
        },
        "capabilities.engagement_tiles": {
            "kind": "dict",
            "page": "capabilities",
            "label": "Capabilities · Engagement tiles (3 modelli)",
            "icon": "bi-diagram-3",
            "region": ".au-engagement .tile",
            "keywords": ["engagement", "ingaggio", "tile"],
            "cols": [
                ("id",    {"label": "ID (es. 'E.01 · Discovery')", "type": "text", "max_length": 80}),
                ("title", {"label": "Titolo (richtext · <em>)", "type": "richtext", "max_length": 160}),
                ("range", {"label": "Range / durata", "type": "text", "max_length": 120}),
                ("body",  {"label": "Body", "type": "textarea", "max_length": 500}),
                # `includes` col excluded (nested list-of-str · Juris precedent)
                # `featured` col excluded (bool · OUT-category precedent)
            ],
        },

        # ── LAVORI (project_list) ───────────────────────────────────────
        "lavori.projects": {
            "kind": "dict",
            "page": "lavori",
            "label": "Lavori · Projects (6 progetti)",
            "icon": "bi-images",
            "region": ".au-projects .project-card",
            "keywords": ["lavori", "projects", "portfolio", "image"],
            "cols": [
                ("id",         {"label": "ID (es. 'P.01')", "type": "text", "max_length": 20}),
                ("title",      {"label": "Titolo", "type": "text", "max_length": 200}),
                ("client",     {"label": "Cliente", "type": "text", "max_length": 120}),
                ("discipline", {"label": "Disciplina", "type": "text", "max_length": 120}),
                ("year",       {"label": "Anno", "type": "text", "max_length": 20}),
                ("blurb",      {"label": "Blurb", "type": "textarea", "max_length": 500}),
                ("cover",      {"label": "Cover · URL (rendered)", "type": "image", "max_length": 400}),
                # `slug` col excluded (structural identifier for detail page routing)
                # `kpi` col excluded (nested list-of-tuple · no sub-list kind)
            ],
        },
        "lavori.velocity_stats": {
            "kind": "tuple",
            "page": "lavori",
            "label": "Lavori · Velocity stats (4 tuple)",
            "icon": "bi-speedometer",
            "region": ".au-velocity .stat",
            "keywords": ["velocity", "stats", "lavori"],
            "tuple_order": ["num", "label"],
            "cols": [
                ("num",   {"label": "Numero (richtext · <em>)", "type": "richtext", "max_length": 80}),
                ("label", {"label": "Label",                     "type": "text", "max_length": 160}),
            ],
        },

        # ── SPRINT (process) ────────────────────────────────────────────
        "sprint.sprints": {
            "kind": "dict",
            "page": "sprint",
            "label": "Sprint · Sprints (4 fasi)",
            "icon": "bi-diagram-3",
            "region": ".au-sprint-phase",
            "keywords": ["sprint", "fasi", "process"],
            "cols": [
                ("id",                 {"label": "ID sprint (es. 'Sprint 0 · Signal')", "type": "text", "max_length": 80}),
                ("duration",           {"label": "Durata", "type": "text", "max_length": 80}),
                ("title",              {"label": "Titolo (richtext · <em>)", "type": "richtext", "max_length": 200}),
                ("tagline",            {"label": "Tagline (stringent IN · '// output: ...')", "type": "text", "max_length": 200}),
                ("body",               {"label": "Body", "type": "textarea", "max_length": 800}),
                ("deliverables_label", {"label": "Deliverables · label (stringent IN)", "type": "text", "max_length": 40}),
                # `deliverables` col excluded (nested list-of-str · 6 per row · Juris precedent)
            ],
        },
        "sprint.mindset_cards": {
            "kind": "dict",
            "page": "sprint",
            "label": "Sprint · Mindset cards (3 principi)",
            "icon": "bi-compass",
            "region": ".au-mindset .card",
            "keywords": ["mindset", "principi", "process"],
            "cols": [
                ("id",    {"label": "ID (es. 'P.01')", "type": "text", "max_length": 20}),
                ("title", {"label": "Titolo (richtext · <em>)", "type": "richtext", "max_length": 160}),
                ("body",  {"label": "Body", "type": "textarea", "max_length": 500}),
            ],
        },
        "sprint.stack_tiles": {
            "kind": "dict",
            "page": "sprint",
            "label": "Sprint · Stack tiles (8 categorie delivery)",
            "icon": "bi-stack",
            "region": ".au-stack .tile",
            "keywords": ["stack", "delivery", "tecnologie"],
            "cols": [
                ("category", {"label": "Category (es. '// frontend')", "type": "text", "max_length": 60}),
                ("list",     {"label": "List (HTML richtext · <strong>/<span>)", "type": "richtext", "max_length": 400}),
            ],
        },

        # ── BRIEF (contact) ─────────────────────────────────────────────
        # brief.slots (tuple list `(id, label)` · 9 rows) stays OUT entire.
        # The id is a form-option-value (structural form-schema concern
        # requiring calendar integration, not a customer copy edit) ·
        # 5th precedent of form-structure OUT after Gusto/Juris/Casa/
        # Villa. brief.labels + placeholders + step1/2/3 + scope_options
        # likewise OUT entire. Only response_rows (SLA table) is exposed.
        "brief.response_rows": {
            "kind": "tuple",
            "page": "brief",
            "label": "Brief · Response SLA (4 tuple)",
            "icon": "bi-clock-history",
            "region": ".au-response",
            "keywords": ["response", "sla", "tempi"],
            "tuple_order": ["label", "value"],
            "cols": [
                ("label", {"label": "Fase (es. 'Brief')",      "type": "text", "max_length": 80}),
                ("value", {"label": "Tempi (es. '< 48h')",     "type": "text", "max_length": 80}),
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
    "fine-dining":            ("gusto-fine-dining",     "it"),
    # A.9 · one archetype, two templates. Baseline anchors Cardio because
    # it was the i18n pilot (Session 23) and carries the canonical list
    # lengths the sidebar uses when materializing indexed groups. Derm
    # shares exactly the same shape and gets editable "for free".
    "specialist":             ("cardio-studio-specialistico", "it"),
    "classic-gold":           ("lex-studio-legale",          "it"),
    # A.11 · Juris (modern-transparent) joins as 5th enrolled archetype —
    # second template in the lawyer category, distinct archetype + skin
    # from Lex's classic-gold.
    "modern-transparent":     ("juris-avvocato-moderno",    "it"),
    # A.12 · Casa (mass-market) joins as 7th enrolled archetype — first
    # template of the real-estate family. Villa (ultra-luxury-cinematic)
    # stays OUT until A.12b. Second zero-image archetype after Juris.
    "mass-market":            ("casa-agenzia-immobiliare",  "it"),
    # A.12b · Villa (ultra-luxury-cinematic) joins as 8th enrolled
    # archetype — closes the real-estate family opened in A.12. Second
    # archetype to use image-in-dict-row exposure (after Vertex
    # studio.partners.portrait). 4 scalar image + 22 image cells across
    # 3 dict lists.
    "ultra-luxury-cinematic": ("villa-immobili-lusso",      "it"),
    # A.13 · Chiara (editorial-designer-grid) joins as 9th enrolled
    # archetype — first template of the portfolio family. Pixel
    # (cinematic-photographer) stays OUT until A.13b. Third archetype
    # to use image-in-dict-row (after Vertex + Villa) — `home.featured_works.items[].image`
    # at deep path 2 levels through `home.featured_works` parent dict.
    # Posts list (3 project detail records) stays registry-only —
    # detail-page editing is OUT of A.13 scope, consistent with every
    # prior family closure's per-item content policy.
    "editorial-designer-grid": ("chiara-portfolio-creativo", "it"),
    # A.13b · Pixel (cinematic-photographer) joins as 10th enrolled
    # archetype — closes the portfolio family opened in A.13 with
    # Chiara. Same staged dedicated-schema progression topology as
    # real-estate (A.12+A.12b). Simpler shape than Chiara: 1 scalar
    # image (home.hero_image) · zero image-in-dict-row · 10 readonly
    # indexed lists all without image cols. Posts list stays
    # registry-only per 6th uniform enforcement of the cross-archetype
    # per-item content policy.
    "cinematic-photographer":  ("pixel-portfolio-fotografico", "it"),
    # A.14 · Sapore (trattoria-warm) joins as 11th enrolled archetype —
    # first template of the restaurant-continuation family. OPENS the
    # family via staged dedicated-schema progression (mirror of real-
    # estate A.12+A.12b and portfolio A.13+A.13b). Brace (street-modern)
    # stays OUT of the gate until A.14b — the two restaurant-
    # continuation templates ship distinct archetypes, distinct skin
    # folders (.tw-* vs .sm-*), 50% page-slug overlap, and menu shape
    # fundamentally different (tuple vs dict-with-image-col); shared-
    # schema (A.9 recipe) is impossible. Sapore exposes menu rows as
    # DEEP-PATH tuple cells via 5 separate STRUCTURED_FIELD_SHAPES
    # entries at `menu.sections.{i}.dishes` so the menu is NOT fake-
    # editable. Sapore ships no posts list — first enrollment since A.10
    # without a posts.* complex-shape exclusion path.
    "trattoria-warm":         ("sapore-trattoria-pizzeria", "it"),
    # A.14b · Brace (street-modern) joins as 12th enrolled archetype —
    # second template of the restaurant-continuation family. **Closes
    # the family** opened in A.14 with Sapore · third staged dedicated-
    # schema closure after real-estate (A.12+A.12b) and portfolio
    # (A.13+A.13b). Distinct archetype from Sapore: 50% page-slug
    # overlap, menu shape fundamentally different (dict-with-image-col
    # vs nested tuple), image surface 3.4× larger, zero form structures.
    # Reuses infra fully: deep-path dict-in-dict-list parent (Chiara
    # precedent for menu.sections.{i}.items) + deep-path tuple-in-dict-
    # list parent (Sapore precedent for ordina.routes.{i}.lines via
    # f66ac24 A.14 Step 2 render-side contract-alignment fix). Zero
    # new infrastructure required.
    "street-modern":          ("brace-street-food-lab", "it"),
    # A.15 · Bottega (artisan-workshop) joins as 13th enrolled archetype —
    # first template of the ecommerce family. **Opens the family** via
    # staged dedicated-schema progression · fourth staged opening after
    # real-estate / portfolio / restaurant-continuation. Luxe (fashion-
    # editorial) stays OUT until A.15b. Boundary verified Step-0:
    # editor edits ONLY template_content registry (presentational demo
    # showcase) · apps.commerce (real catalog backend) is ORTHOGONAL
    # and managed via seller dashboard Phase 3a/3b. Zero touches to
    # apps.commerce required.
    "artisan-workshop":       ("bottega-shop-artigianale", "it"),
    # A.15b · Luxe (fashion-editorial) joins as 14th enrolled archetype —
    # second template of the ecommerce family. **Closes the family**
    # opened in A.15 with Bottega · fourth staged dedicated-schema
    # closure (after real-estate + portfolio + restaurant-continuation).
    # Distinct archetype from Bottega: editorial campaign-driven DNA
    # (fashion press · runway) · .fe-* skin · six pages with two novel
    # kinds (collection + lookbook) · 31 image surfaces ALL RENDERED
    # (zero storage-only · unlike Bottega typographic DNA). Boundary
    # preserved: editor edits template_content registry showcase only ·
    # zero tocchi a apps/commerce · commerce state managed via seller
    # dashboard. Stringent IN col-level: drop/n/tag IN (editorial
    # badges) · id/available OUT (structural routing + commerce-state-
    # like boolean).
    "fashion-editorial":      ("luxe-fashion-store", "it"),
    # A.16 · Salute (clinic) joins as 15th enrolled archetype — first
    # template of the medical-other family. **Opens the family** via
    # staged dedicated-schema progression extended to 3-phase variant
    # (A.16 Salute opener · A.16b Benessere · A.16c Famiglia closer).
    # First 3-template family to enroll · guard-removal sub-recipe
    # extends to 2 removal phases (wellness-out removed in A.16b ·
    # family-out removed in A.16c). Distinct skin folder (.cl-*) · 7
    # pages with 2 novel kinds (prevention + appointment). 15 image
    # surfaces all rendered (1 scalar + 14 image-in-dict-row cells ·
    # specialist-precedent skin). Stringent IN col-level: num +
    # popular_label IN (editorial visible numbering + badge text).
    # Stringent OUT col-level: is_popular bool (Luxe available
    # precedent) · nested list-of-str includes/items/tags (Juris
    # precedent) · raw icon_svg fields (new 5th OUT category precedent ·
    # safety + poor UX for raw SVG XML editing).
    "clinic":                 ("salute-studio-medico", "it"),
    # A.16b · Benessere (wellness) joins as 16th enrolled archetype —
    # second template of the medical-other family · middle phase of
    # 3-phase staged dedicated-schema progression (Salute A.16 ·
    # Benessere A.16b · Famiglia A.16c). Removes wellness-out guard half
    # of the dual-out planted in A.16 · family-out guard PRESERVED for
    # A.16c closer. Distinct skin folder (.we-*) · 7 pages with novel
    # `gallery` page kind + shared `appointment` kind with Salute. 19
    # image surfaces all rendered (3 scalar + 16 image-in-dict-row cells
    # across 3 lists · editorial olistico skin · no storage-only split).
    # Stringent IN col-level: calendar day/num/month + pillars.init +
    # packages.tag + journey.num IN (editorial visible · 6th archetype
    # precedent). Stringent OUT col-level: has_slots/soldout bool flags
    # on both calendar lists (scheduler-state-like · Luxe available +
    # Salute is_popular precedent) · slots nested list-of-str on both
    # calendars (Juris precedent) · includes/tags/interest_options
    # nested list-of-str (Juris precedent). DEFERRED from first wave:
    # home.ambients tuple-with-image (4 tiles · novel shape · ZERO
    # precedent in existing archetypes · whole list OUT · future
    # expansion candidate after infra verification).
    "wellness":               ("benessere-centro-olistico", "it"),
    # A.16c · Famiglia (family) joins as 17th enrolled archetype —
    # third template of the medical-other family · CLOSER phase of
    # 3-phase staged dedicated-schema progression (Salute A.16 opener ·
    # Benessere A.16b middle · Famiglia A.16c closer). **CLOSES the
    # medical-other family** · removes family-out guard residuo planted
    # in A.16 Salute (6th precedent of guard removal pattern · completes
    # the 2-removal-phase sub-recipe variant established in A.16b).
    # Distinct skin folder (.fm-*) · 6 pages (1 fewer than Salute/
    # Benessere) with novel `faq` page kind · NO `appointment` kind
    # (phone-and-WhatsApp CTA pattern). 16 image surfaces all rendered
    # (3 scalar + 13 image-in-dict-row cells across 3 lists: home.doctors
    # × 4 + home.gallery × 5 + pediatre.doctors × 4). **DEEP-PATH shape
    # crescita.topics[].items** (4 sections × 4 tuples × 2 cols = 32
    # cells · Sapore menu.sections.{i}.dishes precedent mirror ·
    # mechanical reuse of f66ac24 render-side contract-alignment fix ·
    # zero new infra needed). Novel col name `src` on home.gallery
    # (mechanical reuse via col registration). Zero raw SVG (icons are
    # Bootstrap text refs · customer-editable IN). Zero bool flags.
    # NO form_fields list-of-dict (form as flat scalars · simpler than
    # Benessere). 5th staged dedicated-schema family closure (after
    # real-estate + portfolio + restaurant-continuation + ecommerce +
    # medical-other).
    "family":                 ("famiglia-pediatria", "it"),
    # A.17 · Aura (agency-digital-studio) — CLOSER of the agency-secondary
    # family (single-template · first single-template closure with one
    # phase · mirror of A.17b Elevate upcoming for startup-saas-landing).
    # 18 indexed lists · 12 image-in-dict-row cells (home.work_cards.cover
    # × 3 · studio.team.portrait × 3 · lavori.projects.cover × 6) · zero
    # scalar top-level image · zero deep-path · zero novel shape. Posts
    # list (6 project_detail records) stays registry-only · 7th uniform
    # enforcement of the per-item content policy. Form-scaffolding on
    # brief page OUT entire (step1/2/3 · labels · placeholders ·
    # scope_options · slots) · 5th form-structure OUT precedent.
    "agency-digital-studio":  ("aura-digital-studio", "it"),
}


# ---------------------------------------------------------------------------
# Schema lookup
# ---------------------------------------------------------------------------

_ARCHETYPE_SCHEMAS: dict[str, list[dict[str, Any]]] = {
    "agency-creative-studio": AGENCY_CREATIVE_STUDIO_SCHEMA,
    "corporate-suite":        PRAGMA_CORPORATE_SUITE_SCHEMA,
    "fine-dining":            GUSTO_FINE_DINING_SCHEMA,
    "specialist":             MEDICAL_SPECIALIST_SCHEMA,
    "classic-gold":           LEX_CLASSIC_GOLD_SCHEMA,
    # A.11 · Juris — single-template admission in the 2-template lawyer
    # category. Distinct archetype from Lex; shared-schema recipe A.9 was
    # audited and does not apply (only ~25% content-tree overlap, distinct
    # skin folders, distinct DNA dimensions).
    "modern-transparent":     JURIS_MODERN_TRANSPARENT_SCHEMA,
    # A.12 · Casa — first-template enrollment of the real-estate family.
    # Villa (ultra-luxury-cinematic) stays out until A.12b — the two
    # real-estate templates ship distinct archetypes, distinct skin
    # folders (dm-* vs vp-*) and ZERO non-home page-slug overlap, so
    # shared-schema (A.9 recipe) is impossible. Casa is the second
    # zero-image archetype after Juris.
    "mass-market":            CASA_MASS_MARKET_SCHEMA,
    # A.12b · Villa — closes the real-estate family. Second archetype
    # to expose image cols inside dict rows (after Vertex studio.partners).
    # Infrastructure proven since A.3a/A.4 — no service/rendering/widget
    # changes required.
    "ultra-luxury-cinematic": VILLA_ULTRA_LUXURY_CINEMATIC_SCHEMA,
    # A.13 · Chiara — first-template enrollment of the portfolio family.
    # Pixel (cinematic-photographer) stays out until A.13b. Third use
    # of image-in-dict-row pattern (after Vertex + Villa). Detail-page
    # editing (posts) stays OUT — consistent with all prior family
    # closures' per-item content policy.
    "editorial-designer-grid": CHIARA_EDITORIAL_DESIGNER_GRID_SCHEMA,
    # A.13b · Pixel — closes the portfolio family opened in A.13.
    # Mechanical reuse of the A.13 recipe: 1 scalar image, zero
    # image-in-dict-row, zero deep paths, 10 readonly indexed lists
    # without image cols. Pure 3-file enrollment, no service-layer
    # changes required.
    "cinematic-photographer":  PIXEL_CINEMATIC_PHOTOGRAPHER_SCHEMA,
    # A.14 · Sapore — first-template enrollment of the restaurant-
    # continuation family. Brace (street-modern) stays out until A.14b;
    # the two templates ship distinct archetypes, distinct skin folders,
    # 50% page-slug overlap, and fundamentally different menu shape.
    # Shared-schema (A.9 recipe) is impossible. First enrollment to
    # register deep-path structured lists (menu.sections.{i}.dishes)
    # because the menu shape requires per-section dish editability.
    "trattoria-warm":         SAPORE_TRATTORIA_WARM_SCHEMA,
    # A.14b · Brace — closes the restaurant-continuation family opened
    # in A.14 with Sapore. Third staged dedicated-schema closure.
    # Mechanical reuse of all A.14-established infra: deep-path tuple-
    # in-dict-list (Sapore) + deep-path dict-in-dict-list (Chiara) +
    # image-in-dict-row (Vertex/Villa). Zero service-layer / rendering /
    # editor-widget changes required — pure enrollment on 3-file surface.
    "street-modern":          BRACE_STREET_MODERN_SCHEMA,
    # A.15 · Bottega — first-template enrollment of the ecommerce family.
    # Luxe (fashion-editorial) stays OUT until A.15b. Editor edits
    # template_content registry (presentational demo showcase): product
    # card listings demo + single-product demo record + copy bands +
    # journal entries + atelier about. Real catalog state in
    # apps.commerce (Storefront/Product/Variant/Cart/Order) is
    # out-of-scope · managed via seller dashboard. Zero tocchi a
    # apps/commerce required · pure 3-file enrollment surface.
    "artisan-workshop":       BOTTEGA_ARTISAN_WORKSHOP_SCHEMA,
    # A.15b · Luxe — closes the ecommerce family opened in A.15 with
    # Bottega. Fourth staged dedicated-schema closure (real-estate +
    # portfolio + restaurant-continuation + ecommerce). Distinct skin
    # folder (.fe-*) · editorial campaign-driven DNA · 31 image surfaces
    # ALL RENDERED (no storage-only distinction like Bottega's
    # typographic skin). Two novel page kinds (collection + lookbook).
    # Zero tocchi a apps/commerce · services.py · rendering.py · editor
    # shell — pure 3-file enrollment on the established surface.
    "fashion-editorial":      LUXE_FASHION_EDITORIAL_SCHEMA,
    # A.16 · Salute — first-template enrollment of the medical-other
    # family. Benessere (`wellness`) + Famiglia (`family`) stay OUT
    # until A.16b + A.16c. First 3-template staged progression. Same
    # shared-schema infeasibility as Bottega/Luxe ecommerce (content-
    # tree overlap ~0% across all 3). Clinic has 2 novel page kinds
    # (prevention + appointment). 18 raw icon_svg fields OUT col-level
    # (5th OUT category precedent · safety + poor UX). 2 form structures
    # OUT (contatti.form_fields + prenota.form_fields + form_sections ·
    # Juris/Gusto/Bottega/Luxe precedent). Zero deep-path · zero tocchi
    # a apps/commerce · services.py · rendering.py · editor shell.
    "clinic":                 SALUTE_CLINIC_SCHEMA,
    # A.16b · Benessere — middle-phase enrollment of the medical-other
    # family · removes wellness-out guard half of the dual-out planted
    # in A.16 · family-out guard preserved for A.16c closer. Distinct
    # skin folder (.we-*) · 7 pages with novel `gallery` page kind +
    # shared `appointment` kind with Salute. 19 image surfaces all
    # rendered (3 scalar + 16 image-in-dict-row cells · editorial
    # olistico skin). 4 bool flag cols OUT (home.calendar + prenota.
    # calendar has_slots + soldout · scheduler-state-like · Luxe/Salute
    # precedent re-application). 5 form-related structures OUT (contatti
    # form_placeholders/form_helpers/form_fields + prenota form_fields/
    # form_sections · Juris precedent uniform enforcement). DEFERRED
    # novel shape: home.ambients tuple-with-image (no precedent · whole
    # list OUT first-wave). Zero deep-path · zero tocchi a apps/commerce
    # · services.py · rendering.py · editor shell.
    "wellness":               BENESSERE_WELLNESS_SCHEMA,
    # A.16c · Famiglia — CLOSER phase of the medical-other 3-phase
    # progression · CLOSES the medical-other family (5th staged
    # dedicated-schema closure after real-estate + portfolio + restaurant-
    # continuation + ecommerce). Removes family-out guard residuo from
    # A.16 Salute tests · 6th precedent of guard removal pattern ·
    # completes the 2-removal-phase sub-recipe variant established in
    # A.16b. Distinct skin folder (.fm-*) · 6 pages (1 fewer than
    # siblings) with novel `faq` page kind · NO `appointment` kind.
    # 16 image surfaces all rendered. **DEEP-PATH shape crescita.topics[].
    # items** (tuple-in-dict-list · Sapore precedent mirror · mechanical
    # reuse of f66ac24 render-side fix · zero new infra needed · 4 sub-
    # path entries in STRUCTURED_FIELD_SHAPES). Novel col name `src` on
    # home.gallery (vs prior image/portrait/avatar · mechanical reuse).
    # Zero raw SVG · zero bool flags · NO form_fields list-of-dict
    # (form as flat scalars · simpler OUT policy). Zero tocchi a
    # apps/commerce · services.py · rendering.py · editor shell.
    "family":                 FAMIGLIA_FAMILY_SCHEMA,
    # A.17 · Aura single-template closure of agency-secondary family.
    # Pure 3-file enrollment surface · 9 sidebar groups · ~95 scalar +
    # 18 indexed lists (6 tuple + 12 dict · including home.console.kpi
    # nested inside home.console parent dict) · 12 image-in-dict-row
    # cells all rendered · zero deep-path. brief.slots OUT entire
    # (form-structure · 5th precedent). Zero tocchi a services.py ·
    # rendering.py · editor shell.
    "agency-digital-studio":  AURA_AGENCY_DIGITAL_STUDIO_SCHEMA,
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
    """Walk a dotted path through dicts + lists (numeric segments index
    into lists). Mirrors the subset of ``apps.projects.services._resolve_path``
    needed by the schema helpers; tuple column-name resolution is not
    required here because callers only ask for the LIST at the end of
    the path (not a cell value). Used by ``_iter_indexed_groups`` to
    find nested lists such as Sapore's ``menu.sections.0.dishes``
    (A.14 · tuple-inside-dict-list parent pattern)."""
    cursor: Any = tree
    for segment in dotted.split("."):
        if isinstance(cursor, dict):
            cursor = cursor.get(segment)
        elif isinstance(cursor, list):
            try:
                idx = int(segment)
            except ValueError:
                return None
            if idx < 0 or idx >= len(cursor):
                return None
            cursor = cursor[idx]
        else:
            return None
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
    # A.8 · Gusto fine-dining joins the multi-locale gate simultaneously
    # with its editor enrollment (single phase · D-098 recipe). Gated by
    # ``test_a8_gusto_full_multilocale_lifecycle_end_to_end``.
    "fine-dining",
    # A.9 · medical-specialist (Cardio + Derm · first multi-template
    # archetype) joins editor + multi-locale in a single phase. Gated by
    # ``test_a9_cardio_full_multilocale_lifecycle_end_to_end`` AND
    # ``test_a9_derm_full_multilocale_lifecycle_end_to_end`` so each
    # template of the pair gets dedicated regression coverage.
    "specialist",
    # A.10 · Lex (classic-gold archetype · law family · single template)
    # joins editor + multi-locale in a single phase. Juris (modern-
    # transparent) stays out and is the subject of a separate A.10b
    # enrollment — the two law templates carry distinct DNA + distinct
    # skin folders so the A.9 shared-schema recipe does NOT apply.
    # Gated by ``test_a10_lex_full_multilocale_lifecycle_end_to_end``.
    "classic-gold",
    # A.11 · Juris (modern-transparent archetype · law family · second
    # template) closes the law family with a dedicated schema. Zero image
    # fields by design. Gated by
    # ``test_a11_juris_full_multilocale_lifecycle_end_to_end``.
    "modern-transparent",
    # A.12 · Casa (mass-market archetype · real-estate family · first
    # template) joins editor + multi-locale in a single phase. Second
    # zero-image archetype after Juris. Villa (ultra-luxury-cinematic)
    # stays out of the gate until A.12b. Gated by
    # ``test_a12_casa_full_multilocale_lifecycle_end_to_end``.
    "mass-market",
    # A.12b · Villa (ultra-luxury-cinematic archetype · real-estate
    # family · second template) joins editor + multi-locale in a single
    # phase, closing the real-estate family. Image-in-dict-row pattern
    # exposed on 3 indexed lists (home.signature / territorio.territories
    # / studio.advisors). Gated by
    # ``test_a12b_villa_full_multilocale_lifecycle_end_to_end``.
    "ultra-luxury-cinematic",
    # A.13 · Chiara (editorial-designer-grid · portfolio family · first
    # template) joins editor + multi-locale in a single phase. Third
    # archetype to use image-in-dict-row (`home.featured_works.items[].image`).
    # Pixel (cinematic-photographer) stays OUT of the gate until
    # A.13b. Posts list (project detail records) stays registry-only —
    # detail-page editing is OUT of scope. Gated by
    # ``test_a13_chiara_full_multilocale_lifecycle_end_to_end``.
    "editorial-designer-grid",
    # A.13b · Pixel (cinematic-photographer · portfolio family ·
    # second template) joins editor + multi-locale in a single phase,
    # closing the portfolio family. Mechanical reuse of the A.13
    # recipe minus the deep-path complexity. 1 scalar image surface
    # (`home.hero_image`) · zero image-in-dict-row · posts + series
    # detail records stay registry-only (6th uniform enforcement of
    # per-item content policy). Gated by
    # ``test_a13b_pixel_full_multilocale_lifecycle_end_to_end``.
    "cinematic-photographer",
    # A.14 · Sapore (trattoria-warm · restaurant-continuation family ·
    # first template) joins editor + multi-locale in a single phase,
    # OPENING the restaurant-continuation family. Brace (street-modern)
    # stays OUT of the gate until A.14b. Mechanical reuse of the A.13
    # recipe + staged dedicated-schema topology. No posts list in the
    # registry (first enrollment since A.10 without posts.* exclusions).
    # Menu rows exposed as deep-path tuple cells to avoid fake-editable
    # regressions. Gated by
    # ``test_a14_sapore_full_multilocale_lifecycle_end_to_end``.
    "trattoria-warm",
    # A.14b · Brace (street-modern · restaurant-continuation family ·
    # second template) joins editor + multi-locale in a single phase,
    # CLOSING the restaurant-continuation family opened by A.14 Sapore.
    # Third staged dedicated-schema closure topology (real-estate and
    # portfolio closed · restaurant-continuation now third). Mechanical
    # reuse of A.14 recipe: menu rows via deep-path dict-in-dict-list
    # parent (Chiara precedent), ordina routes via deep-path tuple-in-
    # dict-list parent (Sapore precedent via f66ac24 fix). No posts
    # list in the registry (first enrollment since A.10 to share this
    # structural absence with Sapore). No form structures (Brace ships
    # zero). Gated by
    # ``test_a14b_brace_full_multilocale_lifecycle_end_to_end``.
    "street-modern",
    # A.15 · Bottega (artisan-workshop · ecommerce family · first
    # template) joins editor + multi-locale in a single phase, OPENING
    # the ecommerce family. Luxe (fashion-editorial) stays OUT of the
    # gate until A.15b. Fourth staged opening after real-estate /
    # portfolio / restaurant-continuation. Boundary editor-vs-commerce-
    # admin verified Step-0: LiveTemplateView does NOT import from
    # apps.commerce · editor edits registry presentational demo only ·
    # commerce state managed via seller dashboard Phase 3a/3b. Posts
    # list empty (same as Sapore/Brace · structural absence). No form
    # structures OUT (contatti.form_fields excluded). Zero mutable
    # repeater · zero image per-locale · pure 3-file enrollment. Gated
    # by ``test_a15_bottega_full_multilocale_lifecycle_end_to_end``.
    "artisan-workshop",
    # A.15b · Luxe (fashion-editorial · ecommerce family · second
    # template) joins editor + multi-locale in a single phase, CLOSING
    # the ecommerce family opened by A.15 Bottega. Fourth staged
    # dedicated-schema closure (real-estate + portfolio + restaurant-
    # continuation + ecommerce). Distinct skin folder (.fe-*) from
    # Bottega (.aw-*) · 50% page-slug overlap (home + contatti) · other
    # four pages distinct (collezione/product/maison/lookbook vs
    # shop/product/atelier/journal) with two novel kinds (collection +
    # lookbook). 31 image surfaces ALL RENDERED (photographically
    # editorial DNA · zero storage-only distinction like Bottega's
    # typographic skin). Stringent IN col-level audit: drop/n/tag IN
    # (editorial badges customer-facing) · id/available OUT (structural
    # routing + commerce-state-like boolean). Posts list empty · no
    # form structures (contatti.form_fields registry-only). Boundary
    # editor-vs-commerce-admin preserved (LiveTemplateView does NOT
    # import apps.commerce). Zero tocchi a apps/commerce · services.py ·
    # rendering.py · editor shell. Gated by
    # ``test_a15b_luxe_full_multilocale_lifecycle_end_to_end``.
    "fashion-editorial",
    # A.16 · Salute (clinic · medical-other family · first template)
    # joins editor + multi-locale in a single phase, OPENING the
    # medical-other family. Benessere (`wellness`) + Famiglia (`family`)
    # stay OUT of the gate until A.16b + A.16c. **First 3-template
    # staged progression** — dual-out guard planted for both siblings ·
    # guard-removal sub-recipe extends to 2 removal phases (wellness-out
    # removed in A.16b via `test_a16b_benessere_out_guard_was_removed_from_salute_tests` ·
    # family-out removed in A.16c via `test_a16c_family_out_guard_was_removed_from_salute_tests`).
    # 15 image surfaces all rendered · 16 indexed list entries · zero
    # deep-path. Novel contributions: raw icon_svg col-level OUT (5th
    # OUT category precedent) · bool flag OUT (is_popular · preserves
    # popular_label text editability). Gated by
    # ``test_a16_salute_full_multilocale_lifecycle_end_to_end``.
    "clinic",
    # A.16b · Benessere (wellness · medical-other family · second
    # template) joins editor + multi-locale in a single phase · MIDDLE
    # phase of the 3-phase staged progression. Removes wellness-out
    # guard half of the dual-out planted in A.16 · family-out guard
    # PRESERVED for A.16c closer (Famiglia stays OUT). 5th precedent
    # of guard removal pattern via `test_a16b_benessere_out_guard_was_removed_from_salute_tests`.
    # Distinct skin (.we-*) · 7 pages with novel `gallery` kind +
    # shared `appointment` with Salute. 19 image surfaces all rendered
    # (3 scalar + 16 image-in-dict-row cells · 3 lists · editorial
    # olistico skin). 17 indexed list entries · zero deep-path. 4 bool
    # flag cols OUT (calendar has_slots + soldout · scheduler-state ·
    # Luxe/Salute precedent). 5 form structures OUT. DEFERRED:
    # home.ambients tuple-with-image novel shape (whole list OUT first-
    # wave). Gated by ``test_a16b_benessere_full_multilocale_lifecycle_end_to_end``.
    "wellness",
    # A.16c · Famiglia (family · medical-other family · third template)
    # joins editor + multi-locale in a single phase · **CLOSER phase**
    # of the 3-phase staged progression · **CLOSES the medical-other
    # family**. Removes family-out guard residuo from A.16 Salute tests
    # (6th precedent of guard removal pattern via
    # `test_a16c_family_out_guard_was_removed_from_salute_tests` ·
    # completes the 2-removal-phase sub-recipe variant established in
    # A.16b). 5th staged dedicated-schema family closure (real-estate +
    # portfolio + restaurant-continuation + ecommerce + medical-other).
    # Distinct skin (.fm-*) · 6 pages (1 fewer than siblings) with
    # novel `faq` page kind · NO `appointment` kind (phone-and-WhatsApp
    # CTA pattern). 16 image surfaces all rendered (3 scalar + 13
    # image-in-dict-row cells · 3 lists · pediatric skin). 20 indexed
    # list entries (12 dict + 4 tuple + **4 DEEP-PATH** crescita.topics.
    # {0..3}.items · Sapore menu.sections.{i}.dishes precedent mirror ·
    # mechanical reuse of f66ac24 render-side fix). Zero raw SVG · zero
    # bool flags · NO form_fields list-of-dict (form as flat scalars).
    # Novel col name `src` on home.gallery (mechanical reuse). Gated by
    # ``test_a16c_family_full_multilocale_lifecycle_end_to_end``.
    "family",
    # A.17 · Aura (agency-digital-studio) — single-template closer of
    # the agency-secondary family. 5-locale content already authored
    # with perfect 544-key parity pre-enrollment. Gated by
    # ``test_a17_aura_full_multilocale_lifecycle_end_to_end``. Pure
    # 3-file surface · zero horizontal touches.
    "agency-digital-studio",
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
