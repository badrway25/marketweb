"""Cornice — Architecture studio (corporate-suite archetype) ·
English locale content tree.

Phase X.5 Cornice · workflow C · multilingual rollout on top of the
locked LF-2 Italian draft (A.6 review-lock). Mirrors the shape of
``CORNICE_CONTENT_IT`` exactly — same keys, same nesting, same list
shapes. Only values are translated and adapted.

Voice register: editorial-curatorial · architectural-discipline.
Native English equivalent of the IT register — the architecture-press
English of Architectural Review, The Architects' Journal, Domus
international and A+U / 10+1. Adult-to-adult, declarative, never
SaaS-marketing, never developer-pitch. Reference voices: AR · AJ ·
Architectural Record critical pieces · El Croquis English captions ·
Domus English editorials.

Voice anchor (CS-EXEC-01 / CS-BLOCK-11 · preserved
verbatim-in-translation across all 5 locales · the load-bearing
italic moves with the equivalent CURATORIAL noun):
    "Every project is a built <em>argument</em>, not a service rendered."

Italian normative references and proper nouns are preserved (D.lgs.
24/2023 whistleblowing, Codice dei Beni Culturali D.lgs. 42/2004,
D.M. 154/2017 MIBAC restoration qualification, OAPPC Milano, CNAPPC,
Soprintendenza Belle Arti, PRG, DAStU Politecnico di Milano, Reg. UE
679/2016 / GDPR). Italian addresses, phone formats, Euro figures and
years are kept as-is. Anti-pattern guardrails carry across: no
"Unlock your project's potential", no "Best architecture firm in
Milan", no Frank Lloyd Wright / Le Corbusier / Bjarke Ingels quotes,
no Pinterest moodboard photo references.
"""
from __future__ import annotations

from typing import Any


# Pool URLs imported from the IT module — single source of truth so
# the build-time corporate_suite checks see the same registered Pexels
# URLs across every locale. Mirrors the Solaria / Continua Pass B
# precedent.
from apps.catalog.template_content_cornice import (  # noqa: E402
    _HERO_BOLOGNA_PORTICO,
    _PORTRAIT_FOUNDER,
    _CASE_CONCORSO,
    _CASE_RESIDENZIALE,
    _CASE_RESTAURO,
    _CASE_CORNICE_DETAIL,
)


CORNICE_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "The studio",  "kind": "home"},
        {"slug": "studio",    "label": "Archive",     "kind": "about"},
        {"slug": "servizi",   "label": "Practice",    "kind": "services"},
        {"slug": "progetti",  "label": "Projects",    "kind": "case_study_list"},
        {"slug": "contatti",  "label": "Contact",     "kind": "contact"},
    ],

    "site": {
        "logo_initial": "C",
        "logo_word":     "CORNICE",
        "logo_subtitle": "architecture studio",
        "tag":           "Editorial architecture · Milan · since 2008",
        "phone":         "+39 02 6610 4708",
        "email":         "fascicolo@cornice-architettura.it",
        "address":       "Via Pasquale Paoli 9 · 20143 Milan",
        "hours_compact": "Tue – Fri · 10:00 – 18:00 · by appointment",
        "hours_footer_rows": [
            "Saturday · by appointment for site reviews only",
            "Sunday · closed",
        ],
        "license": "OAPPC Milan Register N° 12,847 · CNAPPC · MIBAC restoration qualification",
        "footer_intro":
            "Editorial architecture · public and private commissions · "
            "Milan since 2008. Forty-seven works built, twenty-three "
            "competitions submitted, ninety dossiers opened in our "
            "monographic series.",
        "foot_studio":   "Studio",
        "foot_pages":    "Pages",
        "foot_contact":  "Contact",
        "foot_offices":  "Office",
        "offices_footer_rows": [
            "Milan · Via Paoli 9 (single office)",
            "Studio open by appointment · Tuesday-Friday",
            "Active sites · Bologna · Pietrasanta · Rome",
        ],
        "whistleblowing_footer": {
            "heading":      "Whistleblowing",
            "eyebrow":      "Internal channel · D.lgs. 24/2023",
            "note":
                "The studio operates an internal reporting channel "
                "compliant with D.lgs. 24/2023 (EU Directive "
                "2019/1937). Anonymity safeguarded, data confidential. "
                "Open to public clients, site contractors and "
                "external collaborators.",
            "email":        "whistleblowing@cornice-architettura.it",
            "policy_label": "Reporting management policy",
            "policy_href":  "contatti",
        },
        "case_practice_label":     "Programme",
        "case_year_label":         "Dossier year",
        "case_duration_label":     "Site status",
        "case_lead_label":         "Lead architect",
        "case_lead_partner_label": "Lead architect",
        "case_team_label":         "Site team",
        "case_timeline_label":     "Site chronology",
    },

    "home": {
        "eyebrow":     "ARCHITECTURE STUDIO · MILAN · SINCE 2008",
        # Voice anchor verbatim · italic on the curatorial noun
        # `argument` (English equivalent of `argomento`). The IT word
        # carries a discursive-thesis sense closer to "argument" than
        # "topic" or "case"; the editorial-architectural register makes
        # "argument" the unambiguous choice (cf. Architectural Review
        # critical essays).
        "headline":
            "Every project is a built <em>argument</em>, not a service rendered.",
        "intro":
            "Editorial architecture studio · public and private "
            "commissions · ninety open dossiers since 2008.",
        "primary_cta":   "Open a project dossier",
        "primary_href":  "contatti",
        "secondary_cta": "The studio · publications",
        "secondary_href":"studio",

        "hero_image":              _HERO_BOLOGNA_PORTICO,
        "hero_image_alt":          "Restored portico in Bologna · 2023",
        "hero_image_credit_left":  ("Bologna · restored portico · 2023", "dossier no. 31"),
        "hero_image_credit_right": ("Studio office", "Milan · Via Paoli 9"),
        "hero_meta_strip": [
            ("Built works",       "47"),
            ("Years of practice", "18"),
            ("Italian cities",    "6"),
        ],
        # Side-quote em on the verb form — building the editorial-
        # curatorial motif (the IT version uses `argomenta`, the
        # reflexive verb derived from `argomento`; English keeps the
        # same root via `argued`).
        "hero_side_quote":
            "Good architecture is <em>argued</em> — not demonstrated, "
            "not sold, not decorated.",

        "narrative_label":   "THE STUDIO · EDITORIAL MANIFESTO",
        "narrative_drop":    "G",
        "narrative_blocks": [
            ("drop",
             "ood architecture is argued. Cornice is an editorial "
             "architecture studio: every published project is an "
             "argument built upon the site, the client, the constraint. "
             "We do not sign appealing images — we publish works, each "
             "with its own site history and full documentation. The "
             "studio exists to measure context before drawing it, to "
             "write the programme before inhabiting it, to recognise "
             "what is already there before adding what is missing. It "
             "is a slow craft, producing few pages a year, but "
             "producing them whole."),

            ("quote",
             "Survey is the <em>first</em> form of respect. "
             "What is argued upon a site already read will always be "
             "more solid than what is decorated upon a mute site."),

            ("para",
             "Every commission passes through four seasons. The "
             "survey, first of all: the existing work is read as a "
             "text, with its accents, paragraphs and caesurae. Then "
             "the context: the client, the use, the constraints of "
             "the local plan and the Soprintendenza, the habits of "
             "the landscape. Then the argument: the project is "
             "written like a thesis — what problem it solves, what "
             "inheritance it respects, what figure it proposes. Only "
             "then do we open the site, and follow it week by week, "
             "place by place, until handover. Project decisions stay "
             "written: we publish every built work in our monographic "
             "series, because architecture without memory leaves no "
             "rule."),

            ("quote",
             "An <em>author</em> is not the one who signs more "
             "projects, but the one who can name the project they "
             "did not sign — and why."),

            ("para",
             "We work for public and private clients seeking an "
             "author — not an executor, not a turnkey package. "
             "Municipalities restoring a historic courtyard, cultural "
             "boards reprogramming a disused building, families "
             "rewriting a country house, private developers with "
             "editorial sensibility, municipal technical offices "
             "calling for a competition. Our signature is that of a "
             "single architect, not a multi-handed brand: authorial "
             "responsibility stays concentrated, because an argument "
             "must have one voice to be recognisable. Collaborations "
             "with structural engineers, landscape architects, "
             "restorers and site technicians pass through the studio, "
             "they do not replace it."),

            ("quote",
             "To publish a project is not to promote it. "
             "It is to leave a <em>rule</em> — so that whoever comes "
             "after may contest it, modify it, or recognise it."),

            ("para",
             "The works published here are not a commercial "
             "portfolio. They are built arguments, gathered by "
             "programme and by year, with the site documentation that "
             "accompanies them. Each entry names the site, the "
             "client, the brief, the chronology, the constraint, and "
             "the project's argument in five lines — because a work "
             "that cannot be told in five lines has probably not yet "
             "been clarified."),
        ],
        "narrative_side_rail": [
            ("The studio", "studio"),
            ("Practice · commissions", "servizi"),
            ("Projects · dossiers", "progetti"),
            ("Contact · office", "contatti"),
        ],

        "sectors_label": "PROGRAMME TYPES",
        "sectors_lead":
            "The studio works on twelve principal programme types, "
            "grouped by scale of the work, brief of the client, and "
            "relation to landscape or heritage constraint. We do not "
            "work to a service menu: each entry names an argument "
            "already built, already published as a monographic dossier.",
        "sectors": [
            "residential", "public", "interiors", "landscape",
            "restoration", "competition", "cultural", "offices",
            "industrial", "healthcare", "schools", "mixed-use",
        ],
        "sectors_trailing":
            "Restoration and competition works pass through the MIBAC "
            "qualification and the Soprintendenza procedures; public "
            "commissions enter through tender or through invited "
            "competition.",
        "sectors_counter":
            "Numbering of the works published in the series: since "
            "2008, <em>ninety</em> dossiers opened — forty-seven "
            "works built and handed over, twenty-three competitions "
            "submitted, ten major publications.",

        "leadership_label":   "STUDIO FOUNDER · ARCHITECT",
        "leadership_heading": "Marta <em>Roveri</em>",
        "leadership_role":    "founder · editorial lead on the dossiers",
        "leadership_caption": "Studio · interior · 2024",
        "leadership_portrait": _PORTRAIT_FOUNDER,
        "leadership_bio_paragraphs": [
            "Marta Roveri opened Cornice in 2008, after ten years of "
            "practice between Milan and Bologna in two public-"
            "restoration studios. She trained at the Politecnico di "
            "Milano under the chair of architectural restoration, "
            "with a research period at the École Polytechnique de "
            "Lausanne on the stereotomic character of stone vaults. "
            "She works full-time on the studio's projects: she "
            "directs the survey, writes the dossier's argument, "
            "follows the site to handover, and curates the "
            "monographic series that publishes the built works.",

            "Built works of note include the restoration of the "
            "courtyard of Palazzo Lignari in Bologna (2019, MIBAC "
            "qualification), the winning entry for the new civic "
            "library of Pietrasanta (2021, on site) and the "
            "residential building on Via Volpe in Rome (2023, six "
            "apartments on a narrow plot). Her critical notes — on "
            "the relation between cornice and minor façade, on the "
            "rule of the module in public competitions — are "
            "collected in two monographs published by the studio's "
            "series (2018, 2024) and in essays appearing in "
            "Casabella, Domus and Il Giornale dell'Architettura.",
        ],
        "leadership_credentials": [
            "OAPPC Register · Architects' Order of Milan N° 12,847",
            "CNAPPC · National Council of Architects, Planners, Landscape Architects and Conservators",
            "MIBAC · Architectural restoration qualification (D.M. 154/2017)",
            "Politecnico di Milano · Adjunct Professor · Chair of Restoration",
        ],
        "leadership_secondary_cta_label": "The studio · extended biography",
        "leadership_secondary_cta_href":  "studio",

        "cases_label":   "PROJECTS — BUILT ARGUMENTS",
        "cases_intro":
            "Four open dossiers, in order of publication. Site, "
            "client, brief, year, constraint, and the project's "
            "argument.",
        "cases_magazine": [
            {
                "rank":     "hero",
                "num":      "01",
                "eyebrow":  "01 · COMPETITION WON · 2021 · PIETRASANTA (LU)",
                "title":    "Civic library · the argument is the <em>geometry</em> of the module",
                "body":
                    "Invited competition for the new civic library "
                    "of Pietrasanta. Plot at the edge of the "
                    "historic centre, sixty metres from the city "
                    "wall, with landscape constraint and a double "
                    "frontage (urban street to the east, public park "
                    "to the west). The project's argument is a "
                    "module of six by nine metres, repeated eight "
                    "times, organising three reading rooms, a "
                    "double-height stack and a continuous portico "
                    "facing the park. The exposed concrete skin "
                    "narrates the rule, the openings read the light, "
                    "the cornice of the front holds together the "
                    "civic weight of the building.",
                "pill":     "Programme · competition / cultural  ·  1,450 sqm  ·  €5.2 M",
                "photo":    _CASE_CONCORSO,
                "photo_alt":"Minimalist architecture in concrete · Pietrasanta competition",
                "slug":     "biblioteca-pietrasanta-concorso",
            },
            {
                "rank":     "small",
                "num":      "02",
                "eyebrow":  "02 · BUILT WORK · 2023 · ROME (TIBURTINO)",
                "title":    "Via Volpe — six apartments on a narrow <em>lot</em>",
                "body":
                    "Residential building of six apartments on an "
                    "urban plot nine metres wide and twenty-eight "
                    "deep. The argument is depth: the front closes, "
                    "the interior opens onto a blind courtyard "
                    "carried up to the roof. Five levels plus attic, "
                    "reinforced-concrete frame, exposed brick "
                    "infill. Published in dossier no. 38 of the "
                    "series.",
                "pill":     "Programme · residential  ·  720 sqm  ·  private",
                "photo":    _CASE_RESIDENZIALE,
                "photo_alt":"Contemporary residential buildings in Rome · Via Volpe",
                "slug":     "via-volpe-roma-residenziale",
            },
            {
                "rank":     "small",
                "num":      "03",
                "eyebrow":  "03 · PUBLIC RESTORATION · 2019 · BOLOGNA (CENTRE)",
                "title":    "Palazzo Lignari — the courtyard as a civic <em>argument</em>",
                "body":
                    "Restoration of the inner courtyard and the "
                    "piano nobile of Palazzo Lignari, seat of a "
                    "municipal cultural institute. The argument is "
                    "the courtyard as civic space: the restored "
                    "portico becomes a public passage again, the "
                    "terracotta floors read the three stratified "
                    "historical interventions. MIBAC restoration "
                    "qualification; Soprintendenza Belle Arti of "
                    "Bologna.",
                "pill":     "Programme · restoration / public  ·  980 sqm  ·  MIBAC",
                "photo":    _CASE_RESTAURO,
                "photo_alt":"Restored historic Bolognese courtyard · Palazzo Lignari",
                "slug":     "palazzo-lignari-bologna-restauro",
            },
            {
                "rank":     "small",
                "num":      "04",
                "eyebrow":  "04 · PUBLICATION · 2024 · ESSAY IN SERIES",
                "title":    "The cornice of the <em>minor</em> façade — a critical note",
                "body":
                    "Illustrated essay on the rule of the cornice in "
                    "the minor façades of nineteenth-century Milanese "
                    "building. One hundred and twenty-four façades "
                    "surveyed, twenty-two cornice typologies, eight "
                    "documented rules of proportion. The publication "
                    "argues for the value of the cornice as a civic "
                    "device, not a decorative one. Co-published with "
                    "Politecnico di Milano · DAStU.",
                "pill":     "Programme · publication  ·  124 façades  ·  DAStU",
                "photo":    _CASE_CORNICE_DETAIL,
                "photo_alt":"Cornice and capital detail · 2024 essay in the series",
                "slug":     "cornice-fronte-minore-saggio",
            },
        ],
        "cases_trailing_label": "All open dossiers · chronology 2008–2024",
        "cases_trailing_href":  "progetti",

        "cta_label":     "PROJECT DOSSIER",
        "cta_intro":
            "Commissions begin from a single page: the project dossier.",
        "cta_heading":
            "Every project is a built <em>argument</em>, not a service rendered.",
        "cta_form_hint":
            "Brief in English or Italian · site · programme · "
            "schedule · documents already available. Reply within "
            "five working days.",
        "cta_primary":   "Open a project dossier",
        "cta_primary_href": "contatti",
        "cta_closing_line":
            "No discovery call. No metered estimate. Only the "
            "project's argument, and its rule.",
        "cta_sub_line":
            "Cornice · architecture studio · Milan · since 2008",
    },

    "studio": {
        "eyebrow":   "THE STUDIO · ARCHIVE · CV",
        "headline":  "Cornice · editorial architecture studio since <em>2008</em>.",
        "intro":
            "Milan. One founding architect, two collaborators, ninety "
            "open dossiers. We work little, and whole.",

        "history_label":   "STUDIO MILESTONES",
        "history_heading": "Five dates, sixteen years of editorial practice.",
        "history_intro":
            "Five structural choices behind which the studio's "
            "character can be read — the authoriality of a single "
            "architect, the monographic series as method, the survey "
            "as the first gesture of respect, the cornice as a civic "
            "device, qualified restoration as a practice of reading.",
        "history": [
            ("2008", "Founding",
             "Marta Roveri opens Cornice on Via Paoli in Milan, "
             "after ten years of collaboration in two public-"
             "restoration studios between Milan and Bologna. The "
             "office is chosen for one reason only: two rooms on "
             "an inner courtyard, one for survey, one for writing."),
            ("2014", "MIBAC restoration qualification",
             "Marta Roveri obtains the qualification for "
             "architectural restoration (D.M. 154/2017). From that "
             "year the studio accepts restoration commissions on "
             "buildings constrained under the Code of Cultural "
             "Heritage and handles the Soprintendenza Belle Arti "
             "procedures internally."),
            ("2017", "Chair at Politecnico di Milano",
             "Marta Roveri is appointed Adjunct Professor on the "
             "Chair of Restoration at the Politecnico di Milano. "
             "Teaching practice enters the studio's method: the "
             "survey, the context and the argument are written like "
             "a thesis."),
            ("2019", "Palazzo Lignari · first public restoration",
             "The studio hands over the restoration of the "
             "courtyard and piano nobile of Palazzo Lignari in "
             "Bologna (municipal cultural seat · Soprintendenza "
             "Belle Arti). Published in dossier no. 31 of the "
             "monographic series."),
            ("2024", "Essay on the cornice of the minor façade",
             "Co-publication with Politecnico di Milano · DAStU · "
             "illustrated essay on the rule of the cornice in the "
             "minor façades of nineteenth-century Milanese building. "
             "Published in dossier no. 47. The monographic series "
             "reaches ninety open dossiers."),
        ],

        "values_label":   "EDITORIAL PRINCIPLES",
        "values_heading": "Four <em>non-negotiable</em> principles",
        "values_intro":
            "These are the four principles that separate a Cornice "
            "dossier from a standardised commission. They are "
            "written into the engagement letter signed at the first "
            "meeting, not on the website.",
        "values": [
            ("01", "A single authorial architect",
             "The signature on the project is that of a single "
             "architect, not a multi-handed brand. Authorial "
             "responsibility stays concentrated, because an "
             "argument must have one voice to be recognisable. "
             "External collaborations pass through the studio, "
             "they do not replace it."),
            ("02", "Survey as the first gesture",
             "Every commission opens with a serious survey. The "
             "existing work is read as a text, with its accents, "
             "paragraphs and caesurae. No project before the site "
             "has been read in full."),
            ("03", "The monographic series as method",
             "All built works are published in the monographic "
             "series within twelve months of handover, with the "
             "complete site documentation. The series is not "
             "marketing: it is the rule we leave behind."),
            ("04", "No metered estimates",
             "Studio fees are calculated on the CNAPPC minimum "
             "tariffs by class and category, without percentage "
             "discounts. The first appraisal of a commission is "
             "free of charge; rejected preliminary studies are "
             "not invoiced."),
        ],

        "team_label":   "STUDIO AND COLLABORATORS",
        "team_heading": "Three architects, one office.",
        "team_intro":
            "The studio is made up of one founding architect and "
            "two collaborators. We work full-time on three or four "
            "commissions in parallel, never more. Soprintendenza "
            "filings, municipal offices and contracting authorities "
            "are handled in-studio, never delegated.",
        "team": [
            {"name": "Marta Roveri",
             "role": "Studio Founder · Architect",
             "office": "Milan",
             "bio": "Founder. Politecnico di Milano · chair of "
                    "architectural restoration · research at the "
                    "EPFL Lausanne on the stereotomic character of "
                    "stone vaults. OAPPC Milan Register N° 12,847 "
                    "· CNAPPC · MIBAC restoration qualification. "
                    "Adjunct Professor at Politecnico di Milano "
                    "since 2017."},
            {"name": "Associate architect",
             "role": "Associate architect · Site",
             "office": "Milan",
             "bio": "Associate architect since 2018. Politecnico "
                    "di Torino · master in landscape design. "
                    "OAPPC Milan Register. Looks after the site and "
                    "the coordination of public commissions, in "
                    "particular Soprintendenza filings and "
                    "municipal-office procedures."},
            {"name": "Junior architect",
             "role": "Junior architect · Survey",
             "office": "Milan",
             "bio": "Junior architect since 2022. Politecnico di "
                    "Milano · thesis on the cornice as a civic "
                    "device (supervisor: Roveri). OAPPC Milan "
                    "Register. Looks after the digital survey, "
                    "the model and the graphic editing of the "
                    "dossiers. Co-author of the cornice essay "
                    "(series, 2024)."},
        ],

        "coordinates_label": "THE OFFICE",
        "coordinates": [
            ("Milan", "Via Pasquale Paoli 9 · 20143 · two rooms on an inner courtyard"),
            ("Studio", "open by appointment · Tuesday-Friday · 10:00-18:00"),
            ("Active sites", "Bologna · Pietrasanta · Rome · in progress 2024-2026"),
        ],

        "cta_heading": "A commission begins from a single page.",
        "cta_intro":
            "The first page of every commission is the project "
            "dossier: a one-page summary the studio reads in full, "
            "and replies to within five working days with a "
            "critical note.",
        "cta_primary":   "Open a project dossier",
        "cta_primary_href": "contatti",
    },

    "servizi": {
        "eyebrow":  "PRACTICE · COMMISSIONS · QUALIFICATIONS",
        "headline": "Four modes of <em>commission</em>.",
        "intro":
            "The studio accepts direct commissions, public "
            "competitions, MIBAC-qualified restorations and "
            "publications in the series. No turnkey packages.",

        "svc_duration_label": "Cadence",
        "svc_leader_label":   "Lead architect",

        "services": [
            {
                "num":   "01",
                "title": "Direct commission",
                "blurb":
                    "Families rewriting a country house, private "
                    "developers with editorial sensibility, religious "
                    "communities reprogramming a disused building, "
                    "small businesses building a headquarters. The "
                    "direct commission is the studio's oldest mode: "
                    "the client brings a site and a brief, the studio "
                    "writes the argument and follows the project to "
                    "handover.",
                "scope": [
                    "Initial survey included · five days on site",
                    "Monographic dossier included · published at handover",
                    "Building permits and site supervision included",
                    "CNAPPC minimum tariffs · no percentage discounts",
                ],
                "duration": "From survey to handover · 18-30 months",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "02",
                "title": "Public competition",
                "blurb":
                    "The studio enters public design competitions "
                    "(open tender, restricted procedure, competitive "
                    "dialogue) and invited competitions issued by "
                    "municipalities, cultural boards, foundations and "
                    "regional authorities. Our signature is that of a "
                    "single architect — not of a multidisciplinary "
                    "consortium — so we accept competitions only when "
                    "the project's argument can carry our voice.",
                "scope": [
                    "Twenty-three competitions submitted since 2008",
                    "Six won · four shortlisted · thirteen published",
                    "Boards archived and available to the client",
                    "CNAPPC registration verifiable",
                ],
                "duration": "Depends on the brief · 2-9 months",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "03",
                "title": "MIBAC-qualified restoration",
                "blurb":
                    "Marta Roveri is qualified for architectural "
                    "restoration under D.M. 154/2017. The studio "
                    "accepts restoration commissions on buildings "
                    "constrained under the Code of Cultural Heritage "
                    "(D.lgs. 42/2004) and on courtyards, porticoes, "
                    "minor façades, nineteenth- and twentieth-"
                    "century buildings. Stratigraphies are read as "
                    "texts.",
                "scope": [
                    "MIBAC qualification verifiable (D.M. 154/2017)",
                    "Soprintendenza filings handled internally",
                    "Three public restoration works built",
                    "Full publication in the monographic series",
                ],
                "duration": "24-48 months · constraints included",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "04",
                "title": "Editorial publication",
                "blurb":
                    "The studio publishes its own projects in a "
                    "monographic series, but also accepts external "
                    "publication commissions: monographs on minor "
                    "façades, typological essays, critical entries "
                    "for exhibition catalogues, entries for "
                    "architectural reference works. A project's "
                    "argument published without being built is an "
                    "argument the discipline can pick up.",
                "scope": [
                    "Illustrated essay · 80-200 pages",
                    "Co-publication with academic institutions",
                    "Limited print run · 200 numbered copies",
                    "Distribution via museums + specialist bookshops",
                ],
                "duration": "From brief to print · 12-18 months",
                "leader":   "Marta Roveri",
            },
        ],

        "process_label":   "METHOD · FOUR SEASONS",
        "process_heading": "Four phases, one editorial sequence.",
        "process": [
            ("01", "Survey",
             "The existing work is read as a text. Measures, "
             "materials, caesurae, accents. The survey is the first "
             "form of respect and typically lasts five days on site."),
            ("02", "Context",
             "Client, local-plan constraints, landscape and "
             "Soprintendenza constraints, building regulations, "
             "habits of the site. The context is the project's frame."),
            ("03", "Argument",
             "The project is written like a thesis — what problem "
             "it solves, what inheritance it respects, what figure "
             "it proposes. Five lines in which the work must be "
             "able to be told."),
            ("04", "Site",
             "Week by week, place by place, until handover. "
             "Everything stays written in the monographic dossier — "
             "published within twelve months of handover."),
        ],

        "cta_heading":   "Which mode fits your project?",
        "cta_intro":
            "If the mode is not clear, write to us a short "
            "description of the site and of the intervention "
            "envisaged. We will name the right mode within five "
            "working days — even if we do not open a dossier.",
        "cta_primary":   "Open a project dossier",
        "cta_primary_href": "contatti",
    },

    "progetti": {
        "eyebrow":  "PROJECTS · OPEN DOSSIERS · 2008-2024",
        "headline": "Forty <em>built</em> arguments.",
        "intro":
            "Forty-seven works built, twenty-three competitions "
            "submitted, ten major publications. All dossiers are in "
            "the monographic series.",

        "cases_label": "Four representative dossiers · in detail",
        "cases_intro":
            "For each open dossier we publish here the argument "
            "page — site, client, brief, chronology, constraint, "
            "and the project's argument in five lines.",

        "cta_heading":   "An argument similar to yours?",
        "cta_intro":
            "The complete dossiers (survey, technical drawings, "
            "site documentation, closing critical note) are "
            "available in the studio on motivated request. "
            "Consultation is free of charge; the printed dossier "
            "is provided at print cost.",
        "cta_primary":   "Request a dossier in studio",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "biblioteca-pietrasanta-concorso",
            "title":    "Civic library · the argument is the geometry of the module",
            "category": "Competition · cultural",
            "year":     "2021",
            "duration": "Site open · handover scheduled 2026",
            "client_code":
                "Invited competition won · Municipality of "
                "Pietrasanta (Cultural Department) · 1,450 sqm · "
                "€5.2 M · landscape constraint · double frontage "
                "(urban + park).",
            "lead":
                "Invited competition for the new civic library of "
                "Pietrasanta. The project's argument is a module of "
                "six by nine metres, repeated eight times, "
                "organising three reading rooms, a double-height "
                "stack and a continuous portico facing the public "
                "park.",
            "sections": [
                {
                    "label": "The site",
                    "heading": "A double frontage and a landscape constraint",
                    "body":
                        "Plot at the edge of the historic centre of "
                        "Pietrasanta, sixty metres from the city "
                        "wall, with landscape constraint under the "
                        "Code of Cultural Heritage (D.lgs. 42/2004) "
                        "and a double frontage: urban street to the "
                        "east, public park to the west. The survey "
                        "closed with twelve weeks on site in 2020, "
                        "two stratigraphies on the perimeter walls "
                        "and a photographic campaign on the "
                        "neighbouring contexts.",
                },
                {
                    "label": "The argument",
                    "heading": "A module that is argued, not seen",
                    "body":
                        "The module of six by nine metres is "
                        "repeated eight times along an orthogonal "
                        "matrix. The exposed concrete skin narrates "
                        "the rule, the openings read solar light "
                        "along the arc of the day, the cornice of "
                        "the front holds together the civic weight "
                        "of the building toward the street and the "
                        "opening to the park toward the west. The "
                        "module is not seen: it is argued.",
                },
                {
                    "label": "The site works",
                    "heading": "Site opened November 2023",
                    "body":
                        "Site opened in November 2023 after delivery "
                        "of the executive design in May 2023. Site "
                        "supervision held by the studio. Handover "
                        "scheduled for June 2026, with public "
                        "opening in September 2026 on the occasion "
                        "of the inauguration of the municipal "
                        "cultural season. The monographic dossier "
                        "will be published at handover (no. 44 of "
                        "the series).",
                },
            ],
            "kpi": [
                ("1,450 sqm", "net floor area"),
                ("8",         "repeated modules"),
                ("€5.2 M",    "construction value"),
                ("2026",      "scheduled handover"),
            ],
            "lead_partner": "Marta Roveri · Studio Founder",
            "team":         "Architect + 2 collaborators · external structural engineer · in-house site supervision",
            "next_label":   "Next dossier",
        },
        {
            "slug":     "via-volpe-roma-residenziale",
            "title":    "Via Volpe — six apartments on a narrow lot",
            "category": "Residential · private",
            "year":     "2023",
            "duration": "Built · handover June 2023",
            "client_code":
                "Residential building · six apartments · private "
                "client · urban plot 9×28 m · 720 sqm GFA · five "
                "levels + attic · published in dossier no. 38.",
            "lead":
                "Residential building of six apartments on an urban "
                "plot nine metres wide and twenty-eight deep. The "
                "argument is depth: the front closes, the interior "
                "opens onto a blind courtyard carried up to the roof.",
            "sections": [
                {
                    "label": "The site",
                    "heading": "Nine metres of frontage, twenty-eight of depth",
                    "body":
                        "Residential plot in Tiburtino, Rome, on a "
                        "street of mixed building stock from the "
                        "Fifties. Local-plan constraints fairly "
                        "permissive on height, but tight on the "
                        "depth of the elevation. The client asked "
                        "for six saleable apartments, an underground "
                        "garage, and a shared green area.",
                },
                {
                    "label": "The argument",
                    "heading": "Depth carried up to the roof",
                    "body":
                        "The project's argument resolves the depth "
                        "constraint by carrying the blind courtyard "
                        "from the basement up to the roof — a "
                        "shared rooftop patio, five metres by eight, "
                        "lit by skylight. The street front closes "
                        "in exposed brick; the apartments receive "
                        "light from the two short sides and from "
                        "the rooftop patio.",
                },
                {
                    "label": "The site works",
                    "heading": "Nineteen months · site closed 2023",
                    "body":
                        "Site opened October 2021, handed over June "
                        "2023. Reinforced-concrete frame, exposed "
                        "brick infill, bronze-anodised aluminium "
                        "joinery. Site supervision held by the "
                        "studio. Dossier no. 38 was published in "
                        "the series in June 2024.",
                },
            ],
            "kpi": [
                ("720 sqm",  "total GFA"),
                ("6",        "apartments · 70-130 sqm"),
                ("19 months","site duration"),
                ("no. 38",   "dossier in the series"),
            ],
            "lead_partner": "Marta Roveri · Studio Founder",
            "team":         "Architect + 2 collaborators · structural engineer + in-house supervision",
            "next_label":   "Next dossier",
        },
        {
            "slug":     "palazzo-lignari-bologna-restauro",
            "title":    "Palazzo Lignari — the courtyard as a civic argument",
            "category": "Restoration · public",
            "year":     "2019",
            "duration": "Built · handover June 2019",
            "client_code":
                "Restoration of inner courtyard + piano nobile · "
                "Municipality of Bologna (Culture Department) · "
                "MIBAC qualification · Soprintendenza Belle Arti "
                "Bologna · 980 sqm · published in dossier no. 31 "
                "of the series (2020).",
            "lead":
                "Restoration of the inner courtyard and the piano "
                "nobile of Palazzo Lignari, seat of a municipal "
                "cultural institute dedicated to heritage teaching. "
                "The argument is the courtyard as civic space.",
            "sections": [
                {
                    "label": "The site",
                    "heading": "A porticoed courtyard of fifteenth-century origin",
                    "body":
                        "Bologna, historic centre, A1 zone. "
                        "Constraint under the Code of Cultural "
                        "Heritage (D.lgs. 42/2004) and "
                        "Soprintendenza Belle Arti constraint for "
                        "the metropolitan city. Palazzo Lignari is "
                        "of fifteenth-century origin, reworked in "
                        "the seventeenth, the nineteenth and the "
                        "post-war period. The porticoed inner "
                        "courtyard preserves two Renaissance fronts "
                        "and three distinct historical layers.",
                },
                {
                    "label": "The argument",
                    "heading": "Restoration does not add figure, it makes the stratigraphy legible",
                    "body":
                        "We wrote two gestures: the first, the "
                        "terracotta floor laid on site along three "
                        "slightly different orientations, one for "
                        "each historical layer read in the survey; "
                        "the second, the lighting integrated into "
                        "the floor strips, lighting the caesurae "
                        "after sunset and drawing the courtyard as "
                        "a text legible at night. The rule: "
                        "restoration makes the stratigraphy that is "
                        "already there legible.",
                },
                {
                    "label": "The site works",
                    "heading": "Thirty-one months · independent stratigraphic campaign",
                    "body":
                        "Site opened November 2016, handed over "
                        "June 2019. The 31 weeks of stratigraphic "
                        "campaign on the floors required the "
                        "collaboration of a qualified restorer and "
                        "of a team of specialised pavers. "
                        "Soprintendenza filings required eleven "
                        "technical inspections and three revisions "
                        "of the executive design. Handover without "
                        "prescriptions.",
                },
            ],
            "kpi": [
                ("980 sqm",   "courtyard + piano nobile"),
                ("31 months", "site duration"),
                ("no. 31",    "dossier in the series 2020"),
                ("MIBAC",     "restoration qualification"),
            ],
            "lead_partner": "Marta Roveri · Studio Founder",
            "team":         "Architect + 2 collaborators · external restorer · in-house supervision",
            "next_label":   "Next dossier",
        },
        {
            "slug":     "cornice-fronte-minore-saggio",
            "title":    "The cornice of the minor façade — a critical note",
            "category": "Publication · essay",
            "year":     "2024",
            "duration": "Published · in bookshops",
            "client_code":
                "Illustrated essay · co-publication with "
                "Politecnico di Milano (DAStU) · 124 façades "
                "surveyed · 22 cornice typologies · 8 rules of "
                "proportion · published in dossier no. 47 of the "
                "series (2024) · 200 numbered copies.",
            "lead":
                "Illustrated essay on the rule of the cornice in "
                "the minor façades of nineteenth-century Milanese "
                "building. The publication argues for the value of "
                "the cornice as a civic device, not a decorative one.",
            "sections": [
                {
                    "label": "The survey",
                    "heading": "One hundred and twenty-four minor façades in Milan",
                    "body":
                        "The survey closed between 2021 and 2023 on "
                        "one hundred and twenty-four minor "
                        "nineteenth-century façades in the Brera, "
                        "Magenta, Porta Nuova and Porta Romana "
                        "neighbourhoods. For each façade: graphic "
                        "survey at 1:50, photographic campaign in "
                        "daylight and grazing light, typological "
                        "card on the cornice and on its relations "
                        "with the front.",
                },
                {
                    "label": "The argument",
                    "heading": "The cornice as a civic device",
                    "body":
                        "The cornice of the minor façade is not "
                        "ornament: it is the civic device that "
                        "holds the front of the building together "
                        "with the curtain of the street. It is the "
                        "rule that allows different fronts to stay "
                        "in conversation. The essay argues for "
                        "eight documentable rules of proportion "
                        "and twenty recurrent typologies, and "
                        "proposes an operative guideline for "
                        "contemporary restoration.",
                },
                {
                    "label": "The publication",
                    "heading": "Co-publication Politecnico DAStU · 200 copies",
                    "body":
                        "Co-publication with Politecnico di Milano "
                        "· DAStU. Format 24×33 cm, 192 pages, "
                        "uncoated paper cover, four-colour offset "
                        "printing, limited run of 200 numbered "
                        "copies. Distribution: specialist "
                        "bookshops · Politecnico libraries · "
                        "Triennale di Milano · MAXXI Architettura.",
                },
            ],
            "kpi": [
                ("124", "façades surveyed"),
                ("22",  "cornice typologies"),
                ("192", "illustrated pages"),
                ("200", "numbered copies"),
            ],
            "lead_partner": "Marta Roveri · Studio Founder",
            "team":         "Architect + 2 collaborators · co-publication DAStU",
            "next_label":   "Next dossier",
        },
    ],

    "contatti": {
        "eyebrow":  "OPEN A PROJECT DOSSIER",
        "headline": "A commission begins from a single <em>page</em>.",
        "intro":
            "Brief in English or Italian. Site · programme · "
            "schedule · documents already available. Reply within "
            "five working days.",

        "form_label":   "PROJECT DOSSIER",
        "form_heading": "Fill in the opening dossier",
        "form_intro":
            "The studio accepts three or four new commissions a "
            "year. The first page of every commission is the "
            "project dossier: the studio reads it in full, and "
            "replies within five working days with a critical "
            "note. The critical note is free of charge and is the "
            "form in which we declare whether the commission is "
            "in line with the series.",

        "form_fields": [
            {"name": "name",      "label": "First name", "type": "text", "required": True,
             "placeholder": "e.g. Anna",
             "helper": "Given name only, please."},
            {"name": "surname",   "label": "Surname",    "type": "text", "required": True,
             "placeholder": "e.g. Bianchi",
             "helper": "As it appears in the client's documents."},
            {"name": "email",     "label": "Email",      "type": "email", "required": True,
             "placeholder": "anna@domain.com",
             "helper": "An inbox that will receive the fiduciary critical note."},
            {"name": "phone",     "label": "Phone",      "type": "tel", "required": False,
             "placeholder": "+39 ...",
             "helper": "Direct line for the first contact. Optional."},
            {"name": "tipologia", "label": "Programme type", "type": "select", "required": True,
             "options": [
                 "residential",
                 "public",
                 "interiors",
                 "landscape",
                 "restoration",
                 "competition",
                 "cultural",
                 "offices",
                 "industrial",
                 "healthcare",
                 "schools",
                 "mixed-use",
             ],
             "helper": "The programme type of the envisaged intervention."},
            {"name": "cronoprogramma", "label": "Desired schedule", "type": "select", "required": True,
             "options": [
                 "Less than 12 months",
                 "Between 12 and 24 months",
                 "Between 24 and 36 months",
                 "More than 36 months",
             ],
             "helper": "The time horizon agreed with the client."},
            {"name": "documenti", "label": "Documents already available", "type": "select", "required": False,
             "options": [
                 "Survey · plans",
                 "Constraints · local plan · Soprintendenza",
                 "Building regulations · briefs",
                 "Initial concept",
                 "Other",
                 "None (we begin from the survey)",
             ],
             "helper": "Documents already available to the client. Optional."},
            {"name": "sito", "label": "The site · the intervention · the client",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Maximum 800 characters. Tell us briefly the "
                 "location (Municipality · province), the type of "
                 "intervention and from which client the request "
                 "comes. One voice — completeness is not required.",
             "helper":
                 "Enough to tell whether the site deserves a "
                 "survey. Figures and other data are discussed at "
                 "the first meeting, never in writing during first "
                 "contact."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contact",
             "meta": "The person who will sign the engagement at the first meeting.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Project argument",
             "meta": "Programme type · schedule · documents already available.",
             "fields": ["tipologia", "cronoprogramma", "documenti"]},
            {"num": "03", "title": "The site",
             "meta": "The site is the project's first text. Four hundred words are enough.",
             "fields": ["sito"]},
        ],

        "form_submit_label": "Open the dossier",
        "form_submit_note":
            "The studio will read the dossier within five working "
            "days and reply with a critical note to the address "
            "given. No external BDR, no sequence automation — "
            "first contact is with the architect.",
        "form_consent":
            "I consent to the processing of my personal data "
            "pursuant to Reg. UE 679/2016 and D.lgs. 196/2003. "
            "Data are kept at the studio on Via Paoli with access "
            "limited to the three architects. I am informed of "
            "the whistleblowing channel (D.lgs. 24/2023) active "
            "at the studio.",

        "office_address_label": "Address",
        "office_area_label":    "Area",
        "office_phone_label":   "Phone",
        "office_email_label":   "Email",

        "offices_label":   "THE OFFICE",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Single office",
                "address": "Via Pasquale Paoli 9 · 20143",
                "area":    "Sant'Agostino · near Bocconi",
                "phone":   "+39 02 6610 4708",
                "email":   "fascicolo@cornice-architettura.it",
            },
        ],

        "channels_label": "DIRECT CHANNELS",
        "channels": [
            ("Studio reception",                 "+39 02 6610 4708",                       "Tue – Fri · 10:00 – 18:00"),
            ("Fiduciary email",                  "fascicolo@cornice-architettura.it",      "Reply within 5 working days"),
            ("Whistleblowing (D.lgs. 24/2023)",  "whistleblowing@cornice-architettura.it", "Internal channel · encrypted"),
        ],

        "footnote":
            "Cornice does not respond to anonymous requests and "
            "does not issue preliminary opinions in writing without "
            "a first dialogue. Information on fees is illustrated "
            "at the first meeting, according to the CNAPPC minimum "
            "tariffs. The whistleblowing channel is operated under "
            "D.lgs. 24/2023 and is open to public clients, site "
            "contractors and external collaborators.",
    },
}
