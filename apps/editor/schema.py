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
