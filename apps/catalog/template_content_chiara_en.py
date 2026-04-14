"""Chiara — Portfolio Creativo · English content tree.

Mirrors the shape of ``CHIARA_CONTENT_IT`` exactly — same keys, nesting and
list shapes. Authored Session 37 for the live i18n rollout of the
editorial-designer-grid archetype.
"""
from __future__ import annotations

from typing import Any


CHIARA_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Studio",      "kind": "home"},
        {"slug": "studio",     "label": "About",       "kind": "about"},
        {"slug": "lavoro",     "label": "Work",        "kind": "project_list"},
        {"slug": "processo",   "label": "Process",     "kind": "process"},
        {"slug": "contatti",   "label": "Contact",     "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial":   "C",
        "logo_word":      "Chiara Velluti Studio",
        "logo_short":     "CV",
        "tag":            "Art direction · Milan",
        "phone":          "+39 02 8736 4408",
        "email":          "studio@chiaravelluti.it",
        "address":        "Via Tortona 27 · 20144 Milan",
        "hours_compact":  "Mon – Fri · 10:00 – 19:00 · by appointment",
        "license":        "VAT IT 09621460963 · REA MI-2092841",
        "footer_intro":
            "Independent art-direction studio in Milan. Brand identities, "
            "editorial systems and signage for cultural institutions, "
            "publishers and small-luxury maisons. Founded in 2014.",
        "foot_studio":   "The studio",
        "foot_pages":    "Sections",
        "foot_contact":  "Contact",
        "foot_clients":  "Clients who chose the studio",
        "clients_footer_rows": [
            "Triennale Milano",
            "Edizioni Adelphi",
            "Fondazione Prada (2022 commission)",
            "Ateliers Velluti & Co.",
        ],
        # Studio coordinates strip — used in footer + ribbon
        "coordinates": [
            ("Studio",     "Via Tortona 27 · 20144 Milan"),
            ("Founder",    "Chiara Velluti, AD"),
            ("Team",       "5 designers · 1 intern · 2 collaborators"),
            ("Disciplines","Brand · Editorial · Graphic systems"),
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":   "Independent studio · 2014 — 2026",
        # Headline kept short (47 chars) per D-052 to avoid hero overflow
        "headline":  "Forms that endure, <em>one page</em> at a time.",
        "intro":
            "We design brand systems, books and graphic frameworks for "
            "cultural institutions, publishers and small-luxury maisons. "
            "The studio is led by its art director, and every project is "
            "followed personally from the opening of the dossier to the "
            "delivery of the printed guidelines.",
        "primary_cta":   "Request the full portfolio",
        "primary_href":  "contatti",
        "secondary_cta": "Visit the studio",
        "secondary_href":"studio",

        # Hero ledger card footer label + count format (lifted from skin)
        "ledger_full_link_label":   "The full archive",
        "ledger_count_prefix":      "→",
        "ledger_count_unit":        "projects",

        # Project ledger preview — 6 indexed rows
        "ledger_label":   "Selected work · 2022 — 2026",
        "ledger_heading": "Six projects, six disciplines",
        "ledger_intro":
            "A recent selection. The complete archive counts 47 projects "
            "signed since 2014. A printable PDF index of the full archive "
            "is available on request.",
        # Each row: (num, title, discipline, year, medium)
        "ledger_rows": [
            ("01", "Triennale Milano · 2025 catalogue",
             "Art publishing", "2025",
             "Volume 24 × 32 cm · 412 pages · offset print"),
            ("02", "Adelphi · «Carta Bianca» series",
             "Series identity", "2024",
             "Typographic system + 12 covers in sequence"),
            ("03", "Fondazione Querini Stampalia · signage",
             "Signage & wayfinding", "2024",
             "Bilingual system · etched brass + direct print"),
            ("04", "Maison Lambrate · rebrand",
             "Brand identity", "2023",
             "Wordmark + visual system + 96-page guidelines"),
            ("05", "Festival di Pordenone · 38th edition",
             "Event identity", "2023",
             "Temporary mark + print matter + on-site signage"),
            ("06", "Atelier Velluti & Co. · monograph",
             "Studio publishing", "2022",
             "Volume 19 × 25 cm · 240 pages · fine-art print"),
        ],

        # Capabilities preview (full list on /processo)
        "capabilities_label":   "Disciplines",
        "capabilities_heading": "Five crafts, one signature",
        "capabilities_intro":
            "Every project is followed by a multidisciplinary team. "
            "We don't scale by client size — we scale by the complexity "
            "of the problem in front of us.",
        "capabilities": [
            ("Brand identity",
             "Complete identities for institutions and maisons — from "
             "typographic research to the operational guidelines."),
            ("Editorial & books",
             "Art catalogues, authored monographs, editorial series. "
             "Typographic direction and page composition."),
            ("Systems & wayfinding",
             "Signage, graphic systems for exhibition spaces, bilingual "
             "wayfinding and didactic museum matter."),
            ("Art direction",
             "AD consultancy for in-house teams: guideline reviews, "
             "visual audits, mentorship to internal graphic teams."),
        ],

        # Selected clients ribbon (text-only wordmarks)
        "clients_label":   "Clients who chose the studio",
        "clients": [
            "TRIENNALE MILANO",
            "ADELPHI EDIZIONI",
            "FONDAZIONE PRADA",
            "MUSEO POLDI PEZZOLI",
            "QUERINI STAMPALIA",
            "FESTIVAL PORDENONE",
            "MAISON LAMBRATE",
            "ATELIER VELLUTI & CO.",
        ],

        # Featured projects — visual grid below the typo hero. Lightbox-enabled,
        # 4 cards with project image, year, discipline. Reads as a designer's
        # opening reel without breaking the typographic editorial identity.
        "featured_works": {
            "label":   "In the catalogue",
            "heading": "Four projects, <em>four disciplines.</em>",
            "intro":
                "A selection from 2024 — 2025 — typographic systems, "
                "institutional identities, museum signage, printed editorial "
                "objects. Click any card to open the full dossier.",
            "items": [
                {
                    "year":       "2025",
                    "discipline": "Catalogue · Art publishing",
                    "title":      "Triennale Milano 2025",
                    "blurb":      "Typographic direction and composition of the main catalogue for the edition.",
                    "image":      "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2024 — 2025",
                    "discipline": "Typographic system · Editorial",
                    "title":      "«Carta Bianca» series · Adelphi",
                    "blurb":      "Editorial system for twelve titles — covers, typography, colour code.",
                    "image":      "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2024",
                    "discipline": "Signage · Museum identity",
                    "title":      "Querini Stampalia · Venice",
                    "blurb":      "Permanent signage for the galleries + call system for the conference rooms.",
                    "image":      "https://images.unsplash.com/photo-1564399579883-451a5d44ec08?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2023",
                    "discipline": "Monograph · Independent publishing",
                    "title":      "Atelier Velluti · Lambrate",
                    "blurb":      "Studio monograph — 240 pages, custom typographic system, printed at Antiga.",
                    "image":      "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
            ],
            "footer_link":  "See all projects",
            "footer_href":  "lavoro",
        },

        # Press / recognitions — 3 honors
        "press_label":   "Recent recognitions",
        "press_heading": "Awards, exhibitions and reviews",
        "press": [
            {
                "year":  "2025",
                "honor": "ADI Design Index",
                "work":  "Triennale Milano 2025 catalogue",
                "note":  "Art-publishing selection · national jury.",
            },
            {
                "year":  "2024",
                "honor": "European Design Awards · Bronze",
                "work":  "«Carta Bianca» series for Adelphi",
                "note":  "Editorial typographic-systems category.",
            },
            {
                "year":  "2023",
                "honor": "Aiap Design Per · group exhibition",
                "work":  "Monograph Atelier Velluti & Co.",
                "note":  "On view at Triennale for four months.",
            },
        ],

        # Selected commissions — what we accept this year
        "commissions_label":   "2026 commissions",
        "commissions_heading": "What we are looking for this year",
        "commissions_intro":
            "The studio accepts eight to ten projects per year, chosen "
            "for complexity rather than client size. Choosing the work "
            "is the most important discipline we practise.",
        "commissions": [
            ("Identities for cultural institutions",
             "Museums, foundations, festivals. We prefer structural "
             "rebrand mandates to simple refresh work."),
            ("Art catalogues and monographs",
             "Independent art publishers, galleries with an editorial "
             "programme, authored monographs."),
            ("Graphic systems for spaces",
             "Museum signage, bilingual wayfinding, didactic systems "
             "for temporary exhibitions."),
        ],

        # Final CTA band
        "cta_label":   "A preliminary conversation",
        "cta_heading": "Thirty minutes with the AD, no commitment",
        "cta_intro":
            "The first call is with Chiara Velluti directly. We discuss "
            "the scope, the timeline and any potential calendar conflict "
            "— before any written proposal.",
        "cta_primary":      "Write to the studio",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Browse the work",
        "cta_secondary_href":"lavoro",
    },

    # ─── STUDIO (about) ─────────────────────────────────────────
    "studio": {
        "eyebrow":   "The studio · 2014 — 2026",
        "headline":  "An <em>art-director-led</em> studio, twelve years of work.",
        "intro":
            "Chiara Velluti Studio was founded in 2014 in Milan, in a "
            "first thirty-four-square-metre space in Lambrate. Today "
            "we are five designers, two external collaborators and an "
            "intern, in Via Tortona. We still choose our projects one "
            "by one.",

        # Founder block (full bio)
        "founder_label":   "Art direction",
        "founder_heading": "Chiara Velluti, founder",
        "founder": {
            "name":  "Chiara Velluti",
            "role":  "Art director · Founder",
            "bio":
                "Graduated from Isia Urbino in graphic design, three "
                "years at Pentagram New York as a senior designer "
                "(under Paula Scher), five years at Studio Sonnoli in "
                "Rimini as an associate. Opened Velluti Studio in 2014 "
                "in Milan. Teaches typographic design at Politecnico "
                "since 2018, has been a full Aiap member since 2010 "
                "and has directed the «Carta Bianca» editorial series "
                "for Adelphi since 2024.",
            "credentials": [
                "Isia Urbino · Graphic design '06",
                "Pentagram New York · senior '07—'10",
                "Studio Sonnoli Rimini · associate '10—'14",
                "Politecnico Milano · lecturer in typographic design",
                "Aiap · full member since 2010",
                "ADI · Design Index juror 2024",
            ],
            "image": "https://images.unsplash.com/photo-1544717305-2782549b5136?w=1200&q=80&auto=format&fit=crop",
        },

        # Studio team (full team — 4 collaborators beyond founder)
        "team_label":   "Studio team",
        "team_heading": "Five designers, two external collaborators",
        "team_intro":
            "We work in a single open space — no separate offices. "
            "Every project has a dedicated team of three fixed people, "
            "led by the AD. External collaborators step in only on "
            "custom type design and long-form composition work.",
        "team": [
            {"name": "Marco Salvioli",
             "role": "Senior designer · editorial",
             "bio":
                "Five years at Tassinari/Vetta in Trieste before "
                "joining the studio in 2019. Coordinates editorial "
                "projects and typographic guidelines."},
            {"name": "Anna Brambilla",
             "role": "Designer · brand identity",
             "bio":
                "Naba Milan '17, two years at Studio Mut in Bolzano. "
                "Handles studio rebrands and small-luxury maison "
                "identities, from research to the operational manual."},
            {"name": "Lorenzo Tagliabue",
             "role": "Designer · systems & wayfinding",
             "bio":
                "Politecnico Milano '19, internship at Atelier Carvalho "
                "Bernau in Berlin. Leads signage systems and material "
                "for exhibition spaces."},
            {"name": "Sara Pellegrini",
             "role": "Designer · digital",
             "bio":
                "Iuav Venice '20, two years at Cantiere Creativo in "
                "Florence. Extends identities into digital systems "
                "(websites, applications, animated matter)."},
            {"name": "Filippo Vigorelli",
             "role": "Collaborator · type design",
             "bio":
                "Independent type designer, trained at Type@Cooper "
                "in New York. Has collaborated on the studio's custom "
                "typefaces since 2017."},
            {"name": "Beatrice Fornaro",
             "role": "Intern · 2026",
             "bio":
                "Final year at Isia Urbino. Supports the editorial "
                "practice and contributes to the archive of past "
                "projects."},
        ],

        # Studio principles — 4 design notes
        "principles_label":   "Studio principles",
        "principles_heading": "Four <em>non-negotiable</em> rules",
        "principles_intro":
            "These are the four rules that separate a Velluti-signed "
            "project from a standard studio execution. They are written "
            "in the internal 2018 manual, and have never been updated.",
        "principles": [
            ("01", "One voice, from first call to final delivery",
             "The AD is in the first call and signs the delivery. No "
             "hand-offs to juniors after the pitch — the person you "
             "meet in the opening meeting is the same person who "
             "signs off the final guidelines."),
            ("02", "Typography before the mark",
             "On every project, the choice of typefaces precedes the "
             "drawing of the logo. The identities we propose grow out "
             "of a typographic grammar, not a decorative symbol."),
            ("03", "No Pinterest moodboards",
             "The references we bring come from our studio library, "
             "from the archives of the institutions we work with, "
             "and from direct visits to exhibitions. Never downloaded "
             "imagery."),
            ("04", "Guidelines are a book",
             "Every identity closes with a printed operational manual — "
             "not a PDF, a volume of one-hundred-twenty to two-hundred "
             "pages. It lives on the client's bookshelf, not in a "
             "server folder."),
        ],

        # Press band — full press list (extended from home)
        "press_label":   "Awards, exhibitions, reviews",
        "press_heading": "Selection 2020 — 2026",
        "press_full": [
            ("2025", "ADI Design Index",
             "Art-publishing selection", "Triennale 2025 catalogue"),
            ("2024", "European Design Awards · Bronze",
             "Editorial typographic systems", "«Carta Bianca» series"),
            ("2024", "Brand New (Under Consideration)",
             "Critical review", "Maison Lambrate rebrand"),
            ("2023", "Aiap Design Per · group exhibition",
             "Authored publishing", "Monograph Velluti & Co."),
            ("2023", "Type Directors Club New York · Honor",
             "Type design", "Custom typeface Querini"),
            ("2022", "Eye Magazine no. 102",
             "Eight-page illustrated essay", "Velluti Studio identity"),
            ("2021", "ADI Compasso d'Oro · Honourable mention",
             "Visual communication category", "Triennale 2021 system"),
            ("2020", "Brno Biennial Czechia · Selection",
             "Museum identities", "Festival Pordenone 36th"),
        ],

        # Final CTA — visit the studio
        "cta_heading":      "Visit the studio",
        "cta_intro":
            "The studio is at Via Tortona 27, entrance from the inner "
            "courtyard. The library is open by appointment — drop us "
            "a couple of lines and we'll set a morning aside.",
        "cta_primary":      "Book a visit",
        "cta_primary_href": "contatti",
    },

    # ─── LAVORO (project_list) ──────────────────────────────────
    "lavoro": {
        "eyebrow":   "Project archive · 2014 — 2026",
        "headline":  "Forty-seven signed projects, <em>six disciplines</em>.",
        "intro":
            "The complete archive of the studio's projects. The selection "
            "shown here covers the six most recent mandates in each "
            "discipline. For the full portfolio PDF (96 pages, every "
            "project signed since 2014) write to studio@chiaravelluti.it.",

        # Discipline filter pills
        "filter_label": "Disciplines",
        "filters": [
            "All",
            "Art publishing",
            "Brand identity",
            "Systems & wayfinding",
            "Event identity",
            "Art direction",
        ],

        # Ledger row labels (lifted from skin for i18n)
        "row_discipline_label": "Discipline",
        "row_duration_label":   "Duration",
        "row_year_label":       "Year",

        # Index intro band on top of the ledger
        "ledger_label": "Chronological index",
        "ledger_intro":
            "Scroll top to bottom for reverse chronological. Click any "
            "row to open the full project dossier.",

        # CTA before footer
        "cta_label":   "Looking for something specific?",
        "cta_heading": "We send dossiers by discipline on request",
        "cta_intro":
            "If you're considering the studio for a specific mandate, "
            "tell us the discipline and we'll send three relevant "
            "dossiers within 48 hours — A4 format, printed for your "
            "internal presentation.",
        "cta_primary":      "Get in touch",
        "cta_primary_href": "contatti",

        # Dossier (project_detail) labels — constants across all posts,
        # localized via the `lavoro` page_data block.
        "dossier_meta_discipline_label": "Discipline",
        "dossier_meta_year_label":       "Year",
        "dossier_meta_duration_label":   "Duration",
        "dossier_meta_team_label":       "Team",
        "dossier_summary_label":         "Project summary",
        "dossier_deliverables_label":    "Deliverables shipped",
        "dossier_deliverables_heading":  "What we produced",
        "dossier_colophon_label":        "Colophon",
    },

    # ─── PROCESSO (process) ─────────────────────────────────────
    "processo": {
        "eyebrow":   "How we work · studio method",
        "headline":  "Five stages, <em>one file</em> per project.",
        "intro":
            "The studio method is written down, shared with the client "
            "on the first call, and followed without exception. Every "
            "project has its own physical dossier — a green folder with "
            "a number and a typographic label, kept on file for at "
            "least twenty years.",

        # Process step + capability labels (lifted from skin for i18n)
        "step_sequence_label":       "Sequence",
        "step_index_prefix":         "Step",
        "step_index_separator":      "of",
        "capability_duration_label": "Indicative duration",

        # 5-step process (richer than business)
        "process_label":   "Studio sequence",
        "process_heading": "Opening, research, proposal, build, delivery",
        "process": [
            ("01", "Opening the dossier",
             "First call with the AD (45 minutes, free). We discuss "
             "the scope, the client's expectations, any calendar "
             "conflict. Within five days you receive a written proposal "
             "in three pages: scope, deliverables, timeline, fees.",
             "Deliverable", "Written proposal · 3 pages"),
            ("02", "Preliminary research",
             "Four to six weeks of research: visits to the client's "
             "archive, studio library, historical and contemporary "
             "references. Never Pinterest moodboards. The stage closes "
             "with an illustrated brief shared with the client.",
             "Duration", "4 — 6 weeks"),
            ("03", "Direction proposal",
             "A single direction is presented, not three. The "
             "presentation happens in person, at the studio or at the "
             "client's, never by email. The client can accept, ask "
             "for circumscribed revisions (up to two cycles) or "
             "terminate the mandate (an exit clause is built into "
             "the contract).",
             "Duration", "2 — 3 weeks of design + presentation"),
            ("04", "Building the system",
             "The approved direction is declined into a complete "
             "system: typography, palette, grid, marks, materials, "
             "applications. For full identities: ten to sixteen "
             "weeks. The dedicated team works behind closed doors "
             "with two monthly check-ins with the client.",
             "Duration", "10 — 16 weeks depending on scope"),
            ("05", "Delivery and printed manual",
             "Every project closes with a printed operational manual — "
             "120 to 240 pages, A4 format, black-and-white offset "
             "print. One copy to the client, one in the studio "
             "library. Six months of assistance on the application "
             "of the guidelines are included.",
             "Deliverable", "Printed manual + 6-month assistance"),
        ],

        # Capabilities — full list (extended from home)
        "capabilities_label":   "Full disciplines",
        "capabilities_heading": "What we design",
        "capabilities_intro":
            "The disciplines we practise regularly. We don't work on "
            "above-the-line advertising, FMCG packaging, motion graphics "
            "longer than 30 seconds, or on recolourable templates.",
        "capabilities_full": [
            {
                "num": "01",
                "title": "Brand identity",
                "blurb":
                    "Complete identities for cultural institutions and "
                    "small-luxury maisons. Mark + typographic system + "
                    "palette + grid + printed operational manual.",
                "scope": [
                    "Naming and typographic research",
                    "Mark design and variants",
                    "Visual system + grid",
                    "Operational manual (120 — 240 pp.)",
                ],
                "duration": "16 — 24 weeks for a complete identity",
            },
            {
                "num": "02",
                "title": "Art publishing",
                "blurb":
                    "Art catalogues, authored monographs, editorial "
                    "series. Typographic direction, page composition, "
                    "paper selection, print follow-up.",
                "scope": [
                    "Typographic direction",
                    "Composition and editorial grid",
                    "Paper selection + typographic research",
                    "Print follow-up (printer visit)",
                ],
                "duration": "12 — 32 weeks per single volume",
            },
            {
                "num": "03",
                "title": "Systems & wayfinding",
                "blurb":
                    "Museum signage, graphic systems for exhibition "
                    "spaces, bilingual wayfinding, didactic matter for "
                    "temporary shows.",
                "scope": [
                    "Audit of the existing space",
                    "Bilingual/trilingual system",
                    "Signage design",
                    "Production direction (etching/print)",
                ],
                "duration": "10 — 18 weeks for a museum space",
            },
            {
                "num": "04",
                "title": "Event identity",
                "blurb":
                    "Temporary marks for festivals, biennials, limited "
                    "editions. Print matter, on-site signage, digital "
                    "system.",
                "scope": [
                    "Temporary mark + per-year variant",
                    "Print system (posters, brochures, tickets)",
                    "On-site signage",
                    "Digital system (site + animated matter)",
                ],
                "duration": "8 — 14 weeks per edition",
            },
            {
                "num": "05",
                "title": "Art direction",
                "blurb":
                    "AD consultancy for in-house teams: review of "
                    "existing guidelines, visual audits, mentorship "
                    "to the internal graphic team, typographic "
                    "training.",
                "scope": [
                    "Visual audit of the existing material",
                    "Guidelines review",
                    "Mentorship to the graphic team (1 day/month)",
                    "Typographic workshop (training)",
                ],
                "duration": "Annual mandate, renewable",
            },
        ],

        # Final CTA before footer
        "cta_heading":      "Which discipline fits your project?",
        "cta_intro":
            "If the scope is not yet clear, write a couple of lines "
            "of context. We'll come back within 48 hours with the "
            "right discipline — even if the best fit isn't Velluti "
            "Studio itself.",
        "cta_primary":      "Get in touch",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI (contact) ─────────────────────────────────────
    "contatti": {
        "eyebrow":   "A preliminary conversation",
        "headline":  "Thirty minutes with the AD, <em>no commitment</em>.",
        "intro":
            "The first contact is with Chiara Velluti directly, art "
            "director and founder. We discuss the scope of the project, "
            "the timeline and any potential calendar conflict — before "
            "any written proposal.",

        # Studio info side card
        "studio_label":          "The studio",
        "studio_address":        "Via Tortona 27 · 20144 Milan",
        "studio_area":           "Entrance from the inner courtyard · «Velluti» doorbell",
        "studio_metro":          "MM2 Porta Genova · 4 minutes on foot",
        "studio_hours":          "Mon – Fri · 10:00 – 19:00 · by appointment",
        # Studio card row labels (lifted from skin for i18n)
        "studio_address_label":  "Address",
        "studio_area_label":     "Entrance",
        "studio_metro_label":    "Metro",
        "studio_hours_label":    "Hours",

        # Form fields — generic loop in chrome
        "form_label":   "Request a first call",
        "form_heading": "Fill out the form",
        "form_intro":
            "You'll receive confirmation within 48 working hours. Calls "
            "are held on Tuesday and Thursday afternoons, behind closed "
            "doors, with the AD.",
        "form_fields": [
            {"name": "name",      "label": "First name",     "type": "text",     "required": True,  "placeholder": "e.g. Chiara",
             "helper": "First name only, please."},
            {"name": "surname",   "label": "Last name",      "type": "text",     "required": True,  "placeholder": "e.g. Velluti",
             "helper": "As it appears on your business card."},
            {"name": "organization", "label": "Organisation", "type": "text",    "required": True,  "placeholder": "e.g. Triennale Milano",
             "helper": "Institution, publishing house or maison."},
            {"name": "role",      "label": "Role",           "type": "text",     "required": True,  "placeholder": "e.g. Editorial director",
             "helper": "Position of the person who will follow the project."},
            {"name": "email",     "label": "Email",          "type": "email",    "required": True,  "placeholder": "chiara.velluti@triennale.org",
             "helper": "Preferably an institutional address."},
            {"name": "phone",     "label": "Phone",          "type": "tel",      "required": False, "placeholder": "+39 ...",
             "helper": "Direct line · only if you'd rather be called back."},
            {"name": "discipline", "label": "Discipline of interest", "type": "select", "required": True,
             "options": [
                 "To be defined on the call",
                 "Brand identity",
                 "Art publishing",
                 "Systems & wayfinding",
                 "Event identity",
                 "Art direction",
             ],
             "helper": "Choose «to be defined» if the scope touches more than one discipline."},
            {"name": "horizon",   "label": "Time horizon", "type": "select", "required": True,
             "options": [
                 "Kick-off within one month",
                 "Kick-off within three months",
                 "Kick-off within six months",
                 "Exploratory · no urgency",
             ],
             "helper": "Helps us schedule the first call with the AD."},
            {"name": "brief",     "label": "Short description of the project", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Up to 800 characters. No counterparty names — those are only "
                            "discussed after a mutual NDA, if required.",
             "helper": "Enough to tell whether the project falls within our remit."},
        ],

        "form_sections": [
            {"num": "01", "title": "Point of contact",
             "meta": "The person who will follow the project on the client side.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Organisation",
             "meta": "For the preliminary conflict check against other projects in progress.",
             "fields": ["organization", "role"]},
            {"num": "03", "title": "Project scope",
             "meta": "A short description — attachments come on the second call, after NDA.",
             "fields": ["discipline", "horizon", "brief"]},
            {"num": "04", "title": "Attachments (optional)",
             "meta": "Internal brief, institutional dossier, preliminary research. They may bring the first call forward.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "brief_allegato",
            "label":    "Preliminary documents",
            "helper":   "Internal brief, institutional dossier, reference images. "
                        "PDF / DOCX / JPG · max 20 MB total.",
            "accept":   ".pdf,.docx,.jpg,.jpeg,.png",
            "multiple": True,
            "primary":  "Drop documents here or",
            "link":     "browse from your archive",
            "meta":     "PDF / DOCX / JPG · max 20 MB",
        },

        "form_submit_label": "Send request",
        "form_submit_note":
            "Confirmation comes directly from the AD within 48 working "
            "hours. No external account manager, no lead automation.",
        "form_consent":
            "I consent to the processing of my personal data under EU "
            "Regulation 679/2016. Requests are read and archived only "
            "by the art director — no third party is involved.",

        # Channels strip
        "channels_label": "Direct channels",
        "channels": [
            ("Studio email",       "studio@chiaravelluti.it",     "Reply within 48 working hours"),
            ("Switchboard",        "+39 02 8736 4408",            "Mon – Fri · 10:00 – 19:00"),
            ("Studio visit",       "Via Tortona 27 · Milan",      "By appointment, never unannounced"),
        ],

        "footnote":
            "The studio does not reply to anonymous enquiries and does "
            "not issue quotes by email without a first call. Fees and "
            "commercial terms are presented in a written proposal, "
            "never by message.",
    },

    # ─── POSTS — drives /lavoro/<slug>/ project_detail ──────────
    "posts": [
        {
            "slug":        "triennale-milano-catalogo-2025",
            "title":       "Triennale Milano · 2025 catalogue",
            "category":    "Art publishing",
            "year":        "2025",
            "duration":    "32 weeks",
            "client_code": "Triennale Milano · catalogue of the 24th edition · 412 offset pages",
            "lead":
                "Typographic direction and composition of the official "
                "catalogue of the 24th Triennale di Milano. A 412-page "
                "volume, 24 × 32 cm, five-colour offset printing on "
                "130 g/m² uncoated Fedrigoni Arena paper.",
            "summary": [
                "Typographic direction and composition",
                "Variable-grid system for 87 contributions",
                "Custom design of drop-cap initials",
                "Print follow-up · 4 visits · 12 days on press",
            ],
            "discipline":  "Art publishing",
            "team":        "AD + 2 seniors · 32 weeks",
            "deliverables":[
                "Volume 412 pp. · 24 × 32 cm · offset print",
                "Variable-grid system for essays and entries",
                "Custom typeface Triennale Display (12 drop-cap glyphs)",
                "In-house editorial manual · 48 pp.",
            ],
            "credits": [
                ("Client",             "Triennale Milano"),
                ("Editorial direction","Maria Sebregondi"),
                ("Print",              "Grafiche Antiga · Treviso"),
                ("Paper",              "Fedrigoni Arena Natural Smooth 130 g/m²"),
                ("Binding",            "Thread-sewn softcover · 350 g/m² board"),
                ("Print run",          "3,200 copies · second reprint June 2025"),
            ],
            "sections": [
                {
                    "label": "The project",
                    "heading": "Four hundred and twelve pages, eighty-seven authors",
                    "body":
                        "The catalogue of the 24th Triennale documents "
                        "an exhibition of one thousand square metres "
                        "across eight rooms, with eighty-seven "
                        "contributions between critical essays, work "
                        "entries and documentary apparatus. The design "
                        "problem was to build a grid system capable of "
                        "hosting texts of very different lengths (from "
                        "200 to 12,000 words) while preserving a "
                        "unified editorial reading.",
                },
                {
                    "label": "Typographic direction",
                    "heading": "Three families, one voice",
                    "body":
                        "We built the system on three complementary "
                        "typographic families — a transitional serif "
                        "(Lyon Text) for body copy, a geometric "
                        "grotesque (GT Walsheim) for titles and a "
                        "monospace (JetBrains Mono) for the "
                        "documentary apparatus. The three families "
                        "live together on a nine-column grid that "
                        "articulates into different formats without "
                        "breaking recognisability.",
                },
                {
                    "label": "Execution",
                    "heading": "Thirty-two weeks, four press visits",
                    "body":
                        "The volume was composed over thirty-two weeks "
                        "by a team of three studio designers, with "
                        "weekly AD supervision. Four printer visits "
                        "in Treviso between July and September 2025 "
                        "allowed us to calibrate the print directly "
                        "on the press — the cover was reprinted twice "
                        "to reach the desired solid black without "
                        "reflections.",
                },
            ],
            "next_label": "Next mandate",
        },
        {
            "slug":        "adelphi-collana-carta-bianca",
            "title":       "Adelphi · «Carta Bianca» series",
            "category":    "Series identity",
            "year":        "2024",
            "duration":    "44 weeks",
            "client_code": "Adelphi Edizioni · editorial series · 12 titles per year",
            "lead":
                "Visual system and covers for a new series of "
                "contemporary philosophy essays for Adelphi. Twelve "
                "titles per year, 14 × 22 cm format, thread-sewn "
                "softcover on uncoated paper.",
            "summary": [
                "Series direction + typographic system",
                "12 covers in sequence · custom design",
                "Colour system per editorial year",
                "Typographic editorial manual",
            ],
            "discipline":  "Series identity",
            "team":        "AD + senior editorial · 44 weeks",
            "deliverables":[
                "Series visual system · 36 pages",
                "12 covers in sequence · per-title design",
                "Custom typeface Adelphi Sans (for the series)",
                "Typographic editorial manual · 64 pp.",
            ],
            "credits": [
                ("Client",             "Adelphi Edizioni"),
                ("Series editor",      "Roberto Calasso (posthumous) · Aldo Schiavone"),
                ("Paper",              "Munken Pure Smooth 100 g/m²"),
                ("Print",              "Tipografia Mariani · Bergamo"),
                ("Binding",            "Thread-sewn softcover"),
                ("Print run",          "2,000 — 4,500 copies per title"),
            ],
            "sections": [
                {
                    "label": "The project",
                    "heading": "A new series for Adelphi",
                    "body":
                        "Adelphi was looking for a visual system for "
                        "«Carta Bianca», a philosophy-essays series "
                        "meant to host young voices from contemporary "
                        "European philosophy. Twelve titles per year, "
                        "an openly experimental editorial profile — "
                        "yet the Adelphi imprint had to be honoured.",
                },
                {
                    "label": "The idea",
                    "heading": "One architecture, twelve variations",
                    "body":
                        "The system is built on a single typographic "
                        "architecture — the title set in a custom "
                        "typeface (Adelphi Sans, drawn in "
                        "collaboration with Filippo Vigorelli), "
                        "typeset full-bleed on a monochrome ground. "
                        "Each editorial year introduces a six-colour "
                        "palette; each title is printed in two colours "
                        "from the annual palette. Recognition comes "
                        "from the system, not from decoration.",
                },
                {
                    "label": "Execution",
                    "heading": "Forty-four weeks, twelve covers",
                    "body":
                        "The system was delivered in July 2024, the "
                        "first four covers in September, the remaining "
                        "eight on a quarterly cadence up to July 2025. "
                        "Aldo Schiavone's editorial direction signs "
                        "off every cover personally before print. The "
                        "studio also ran training for the in-house "
                        "editorial team on the use of the manual.",
                },
            ],
            "next_label": "Next project",
        },
        {
            "slug":        "querini-stampalia-segnaletica",
            "title":       "Fondazione Querini Stampalia · signage",
            "category":    "Signage & wayfinding",
            "year":        "2024",
            "duration":    "26 weeks",
            "client_code": "Fondazione Querini Stampalia · bilingual system ITA / ENG",
            "lead":
                "Bilingual signage system for the Fondazione Querini "
                "Stampalia in Venice. Three floors, museum + library + "
                "Carlo Scarpa space. Etched brass and direct print on "
                "swappable panels.",
            "summary": [
                "Audit of the existing space · 2 weeks",
                "Bilingual system ITA / ENG · unified grammar",
                "Custom typeface Querini Sans (96 glyphs)",
                "Production direction · etched brass + direct print",
            ],
            "discipline":  "Systems & wayfinding",
            "team":        "AD + senior wayfinding · 26 weeks",
            "deliverables":[
                "Complete signage system · 142 elements",
                "Custom typeface Querini Sans · 96 glyphs · 3 weights",
                "Operational manual · 88 pages",
                "Production direction through to commissioning",
            ],
            "credits": [
                ("Client",             "Fondazione Querini Stampalia, Venice"),
                ("Direction",          "Marigusta Lazzari, director"),
                ("Architecture",       "Studio Carlo Scarpa (1961—63 · original)"),
                ("Brass production",   "Bottega Pasinetti · Murano"),
                ("Direct print",       "Tipografia Adriatica · Mestre"),
                ("Commissioning",      "September 2024 · 142 elements installed"),
            ],
            "sections": [
                {
                    "label": "The problem",
                    "heading": "Signage born of successive additions",
                    "body":
                        "The Foundation's signage had stratified across "
                        "five successive cycles (from the 1960s to a "
                        "2009 revision), with different materials, "
                        "typefaces and placement logics. The result "
                        "was illegible, but the real issue was "
                        "respecting Carlo Scarpa's architecture on "
                        "the ground floor — a space that cannot "
                        "tolerate heavy graphic overlays.",
                },
                {
                    "label": "The approach",
                    "heading": "One grammar, two materials",
                    "body":
                        "We built a unified grammar in two materials: "
                        "bath-etched brass (for the permanent "
                        "signage, in dialogue with Scarpa's brass on "
                        "the ground floor) and direct print on "
                        "swappable aluminium panels (for exhibition "
                        "signage, changeable with every new show). "
                        "The custom typeface Querini Sans picks up "
                        "the proportions of sixteenth-century Veneto "
                        "epigraphic stones.",
                },
                {
                    "label": "The result",
                    "heading": "One hundred and forty-two elements, zero overlays",
                    "body":
                        "The system was installed across three "
                        "successive worksites between June and "
                        "September 2024, with joint commissioning "
                        "with the Soprintendenza for the Scarpa floor. "
                        "The brass engravings were executed by the "
                        "Pasinetti workshop in Murano using traditional "
                        "technique — fifteen weeks of production, all "
                        "verified on site by the studio.",
                },
            ],
            "next_label": "Next project",
        },
    ],
}
