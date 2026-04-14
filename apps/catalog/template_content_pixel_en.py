"""Pixel — Portfolio Fotografico · English content tree.

Mirrors the shape of ``PIXEL_CONTENT_IT`` exactly — same keys, nesting and
list shapes. Authored Session 39 for the Pixel live i18n rollout of the
cinematic-photographer archetype. Anglo-American long-form reportage register.
"""
from __future__ import annotations

from typing import Any


PIXEL_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Index",         "kind": "home"},
        {"slug": "serie",         "label": "Work",          "kind": "series_list"},
        {"slug": "biografia",     "label": "Biography",     "kind": "about"},
        {"slug": "pubblicazioni", "label": "Publications",  "kind": "publications"},
        {"slug": "contatti",      "label": "Contact",       "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial":   "P",
        "logo_word":      "Pixel — Lorenzo Bianchi",
        "logo_short":     "PXL",
        "tag":            "Independent photographer · Milan · Trieste",
        "phone":          "+39 348 211 7720",
        "email":          "studio@lorenzobianchi.photo",
        "address":        "Via Tadino 18 · 20124 Milan",
        "hours_compact":  "Available for commissions · 2026 — 27",
        "license":        "Registered · Albo Fotografi Professionisti no. 4421/2014",
        "footer_intro":
            "Independent author photographer. Long-form reportage, "
            "editorial portrait and brand commissions for publishers, "
            "galleries and fashion houses. Represented by Galleria Carla "
            "Sozzani for fine art prints.",
        # Primary nav bracket CTA (right-side) — lifted Session 39 per D-047
        "nav_cta":       "Open a conversation",
        "foot_studio":   "The studio",
        "foot_pages":    "Index",
        "foot_contact":  "Contact",
        "foot_kit":      "Equipment",
        # EXIF-style footer cells
        "exif_footer": [
            ("Based in",     "Milan · Trieste"),
            ("Available",    "Commissions 2026 — 27"),
            ("Representation", "Galleria Carla Sozzani · Milan"),
            ("Printing",     "Atelier Druckwerkstatt · Berlin"),
        ],
        # Footer kit column rows (per-tenant — never inline in skin per D-047)
        "kit_footer_rows": [
            "Mamiya 7II · Sony α7R V",
            "Kodak Portra 400",
            "Printing · Druckwerkstatt Berlin",
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        # Series counter chip (top-left of hero)
        "series_counter_label": "Current series",
        "series_counter_value": "07 / 24",

        # Status pulse on nav (right side)
        "status_pulse": "Available · 2026 — 27",

        # Eyebrow + headline
        "eyebrow":   "Author photography · 2014 — 2026",
        # All-caps cinematic hero per archetype
        "headline":  "OBSERVE WHAT REMAINS <em>when the light shifts</em>",
        "subhead":
            "Long-form reportage, editorial portrait and brand "
            "commissions. I work on medium-format film and on a "
            "dual-sensor digital system — for projects that ask for "
            "ten days or three years of time.",
        "primary_cta":   "Open the full series",
        "primary_href":  "serie",
        "secondary_cta": "Availability 2026",
        "secondary_href":"contatti",

        # Hero image — fullbleed dominant
        "hero_image":
            "https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?w=2000&q=85&auto=format&fit=crop",
        "hero_image_alt":
            "View from the port of Trieste at 6:14 in the morning · "
            "November 2025 · Kodak Portra 400 film",

        # EXIF credit cells under hero (4-cell mono bar)
        "hero_credit_cells": [
            ("Camera",   "Mamiya 7II"),
            ("Film",     "Kodak Portra 400"),
            ("Location", "Porto Vecchio · Trieste"),
            ("Date",     "November 2025"),
        ],

        # Featured series (filmstrip on home — 4 series)
        "filmstrip_label":   "Recent work",
        "filmstrip_heading": "FOUR SERIES · 2024 — 2026",
        "filmstrip_intro":
            "Four long-term projects closed over the past two years. "
            "The full series are accessible in the Work section — "
            "each one includes between twenty and forty photographs.",
        # Each: (num, title, discipline, year, slug-for-link)
        "filmstrip": [
            ("07", "Porto Vecchio · Trieste",
             "Long-form reportage", "2024 — 2026",
             "porto-vecchio-trieste"),
            ("06", "Atelier Velluti & Co.",
             "Editorial commission", "2025",
             "atelier-velluti"),
            ("05", "The stone houses",
             "Architectural reportage", "2023 — 2024",
             "case-di-pietra-puglia"),
            ("04", "Portraits of the Po",
             "Author portrait", "2023",
             "ritratti-del-po"),
        ],

        # Reel — REMOVED per D-068 (Session 36).
        # A short-film claim without a real signed MP4 shipped as a placeholder
        # contradicts the cinematic-photographer identity; the "Play · 3:12" +
        # "Reel · 1080p · 24 fps" meta also trespassed into codec-theatre.
        # Lorenzo's identity is stills — the filmstrip + EXIF cells + series
        # index already carry the cinematic voice. When a genuine Carso reel
        # exists, this block can return with a real `src` and meta pruned of
        # pseudo-technical cues.

        # About excerpt — 3 sentences (full bio on /biografia)
        "about_label":   "Autobiographical notes",
        "about_heading": "LORENZO BIANCHI",
        "about_excerpt":
            "Born in Trieste in 1986, I live between Milan and the "
            "Carso plateau above Trieste. I began photographing the "
            "markets of Sarajevo in 2009 and I have not changed "
            "discipline since — only time, light and format. I work "
            "on Kodak Portra 400 medium-format film for personal work, "
            "on a Sony dual-sensor digital system for commissions.",
        "about_cta":     "Read the biography",
        "about_cta_href":"biografia",

        # Recent publications strip (3 selected)
        "publications_label":   "Recently published",
        "publications_heading": "PRESS & EDITORIAL · 2025",
        "publications": [
            ("FOAM Magazine no. 64",
             "Eight-page portfolio on the series «Porto Vecchio»",
             "November 2025"),
            ("Internazionale no. 1612",
             "Illustrated reportage on the stone houses of Salento",
             "September 2025"),
            ("Domus no. 1102",
             "Editorial commission for the Carlo Scarpa monograph issue",
             "April 2025"),
        ],

        # Final CTA band — commission inquiry
        "cta_label":   "Commissions · availability 2026 — 2027",
        "cta_heading": "[ OPEN A CONVERSATION ]",
        "cta_intro":
            "I am available for editorial commissions, author portrait "
            "and long-term projects through September 2027. Brand "
            "commissions are considered case by case — I prefer mandates "
            "that come with long time.",
        "cta_primary":      "Write a brief",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Go to representation",
        "cta_secondary_href":"biografia",
    },

    # ─── SERIE (series_list) ────────────────────────────────────
    "serie": {
        "series_counter_label": "Archive",
        "series_counter_value": "24 SERIES",
        "status_pulse":         "Available · 2026 — 27",

        "eyebrow":   "Archive of the series · 2009 — 2026",
        "headline":  "TWENTY-FOUR SERIES, <em>one discipline</em>",
        "subhead":
            "The complete archive of signed series. Long-form "
            "reportage, author portrait, editorial commissions. "
            "The selection shown covers the most recent work — "
            "the historical series (2009 — 2018) are accessible "
            "on request for study or publication.",

        # Discipline filter pills
        "filter_label": "Disciplines",
        "filters": [
            "All",
            "Long-form reportage",
            "Author portrait",
            "Editorial commission",
            "Architectural reportage",
        ],

        # Index intro band
        "index_label": "Selection 2018 — 2026",
        "index_intro":
            "Click on the cover to open the full series. Each "
            "series includes between twenty and forty photographs, "
            "with critical apparatus and shooting EXIF.",

        # CTA before footer
        "cta_label":   "Looking for something specific?",
        "cta_heading": "[ RESERVED ARCHIVE · PRESS & STUDIO ]",
        "cta_intro":
            "To access the historical archive (2009 — 2018), to "
            "request fine art prints, or to commission new work: "
            "open a preliminary conversation.",
        "cta_primary":      "Write to the photographer",
        "cta_primary_href": "contatti",

        # Chrome labels shared by serie card + series_detail page.
        # Lifted Session 39 (D-047 lift) — same labels across every post,
        # so they live on the parent serie block rather than on each post.
        "card_arrow_label":        "open series",
        "post_discipline_label":   "Discipline",
        "post_period_label":       "Duration",
        "post_location_label":     "Location",
        "post_frames_label":       "Frames",
        "post_gallery_label":      "Gallery",
        "post_edition_label":      "Edition",
    },

    # ─── BIOGRAFIA (about) ──────────────────────────────────────
    "biografia": {
        "series_counter_label": "Autobiographical notes",
        "series_counter_value": "1986 — 2026",
        "status_pulse":         "Based in · Milan + Trieste",

        "eyebrow":   "Autobiographical notes · 1986 — 2026",
        "headline":  "LORENZO BIANCHI <em>independent photographer</em>",
        "subhead":
            "Born in Trieste in 1986, I live between Milan and the "
            "Carso plateau above Trieste. I began photographing the "
            "markets of Sarajevo in 2009 — an essay for Granta that "
            "never saw print. I have not changed discipline since, "
            "only time, light and format.",

        # Bio statement — 5 paragraphs
        "statement_label":   "Statement",
        "statement_heading": "WHY I PHOTOGRAPH",
        "statement_paragraphs": [
            "I photograph in order to stay long in a place. "
            "Photography is the only discipline that forces me to "
            "return. A series, for me, is ten or twenty trips months "
            "apart to the same precise spot, until something changes "
            "enough to deserve a frame.",
            "I work on medium-format film — Mamiya 7II, two lenses, "
            "Kodak Portra 400. The mechanical slowing-down is the "
            "discipline, not an affectation. I develop and print "
            "myself, in a kitchen turned darkroom for small editions, "
            "and at Druckwerkstatt Berlin for fine art.",
            "For editorial commissions I use a Sony Alpha "
            "dual-sensor digital system — the delivery speed a "
            "newsroom requires is not compatible with the pace of "
            "film. But the way of looking stays the same; digital "
            "is just another carrier.",
            "I have been represented since 2018 by Galleria Carla "
            "Sozzani in Milan for fine art prints and the secondary "
            "market. For editorial and brand commissions I work "
            "directly, without an agent — an agent means a filter "
            "between photographer and client, and I lose the "
            "conversations that matter to me most.",
            "I have taught documentary photography at CFP Bauer in "
            "Milan since 2019 — one day a week, to second-year "
            "students. It is the only fixed engagement on the "
            "studio calendar. Everything else is chosen by project.",
        ],

        # Camera kit — what we shoot with.
        # Availability label + value lifted Session 39 (D-047).
        "kit_label":                "Working equipment",
        "kit_heading":              "FOUR SYSTEMS, ONE CHOICE PER PROJECT",
        "kit_availability_label":   "Available",
        "kit_availability_value":   "On commission",
        "kit": [
            ("01", "Mamiya 7II",
             "Medium-format 6 × 7 cm rangefinder, two lenses (80mm and 43mm). "
             "For personal work on film — long-form reportage and "
             "author portrait.",
             "Studio film", "Kodak Portra 400 + Tri-X 400"),
            ("02", "Sony α7R V + α7S III",
             "Dual sensor (high resolution + high sensitivity). "
             "For editorial commissions and work that requires "
             "delivery within 72 hours.",
             "Lenses", "GM 24/35/85 + Voigtländer 50/1.5"),
            ("03", "Linhof Master Technika 4 × 5",
             "Large-format view camera for fine art prints and "
             "studio portrait. Reserved for eight to ten exposures "
             "a year for the gallery.",
             "Sheet film", "Ilford FP4+ · Foma Retropan 320"),
            ("04", "Darkroom · kitchen in Milan",
             "Development and printing for small editions (up to "
             "18 × 24 cm). Fine art editions are printed at "
             "Druckwerkstatt Berlin in collaboration with Anna "
             "Wedekind.",
             "Studio paper", "Ilford Multigrade FB Classic"),
        ],

        # Exhibitions + publications timeline (selected — full list /pubblicazioni)
        "timeline_label":   "Exhibitions & publications · selected",
        "timeline_heading": "TWELVE MILESTONES, FIFTEEN YEARS",
        "timeline": [
            ("2026", "FOAM Talent Lounge · Amsterdam",
             "Group show · series «Porto Vecchio»"),
            ("2025", "FOAM Magazine no. 64",
             "Eight-page portfolio on the series «Porto Vecchio»"),
            ("2024", "Triennale Milano · «Geography of a land»",
             "Solo show · series «The stone houses»"),
            ("2024", "World Press Photo Story of the Year · Finalist",
             "Long-term projects category, series «The stone houses»"),
            ("2023", "Internazionale Festival Ferrara",
             "Group show · series «Portraits of the Po»"),
            ("2022", "Photo London · Galleria Carla Sozzani booth",
             "Fine art prints · selection 2018 — 2022"),
            ("2021", "Magnum Foundation Grant · finalist",
             "Emerging photographer category"),
            ("2020", "MAXXI Rome · «Lockdown diaries»",
             "Group show · personal contribution 12 prints"),
            ("2019", "GUP Magazine no. 60 · cover",
             "Illustrated essay on the Sarajevo markets archive"),
            ("2018", "FOAM Talent · Amsterdam · selection",
             "Series «The night trains»"),
            ("2016", "Premio Marco Pesaresi · finalist",
             "Italian reportage · «The passage»"),
            ("2009", "Granta Magazine · commissioned essay (never published)",
             "The markets of Sarajevo · professional debut"),
        ],

        # Final CTA — commissions
        "cta_heading":      "[ COMMISSIONS 2026 — 2027 ]",
        "cta_intro":
            "The studio accepts six to eight commissions a year, "
            "chosen by available time and by coherence with the "
            "discipline of the work. Editorial and brand proposals "
            "are considered case by case — I prefer mandates that "
            "come with long time.",
        "cta_primary":      "Open a conversation",
        "cta_primary_href": "contatti",
    },

    # ─── PUBBLICAZIONI (publications) ───────────────────────────
    "pubblicazioni": {
        "series_counter_label": "Press archive",
        "series_counter_value": "47 PUBLICATIONS",
        "status_pulse":         "Updated · January 2026",

        "eyebrow":   "Publications & exhibitions · 2009 — 2026",
        "headline":  "FORTY-SEVEN PUBLICATIONS, <em>fifteen years</em>",
        "subhead":
            "The full archive of print publications, solo and "
            "group exhibitions, awards and residencies. The list "
            "is updated to January 2026 — further releases are "
            "expected over the course of the year.",

        # Press band — magazine + book covers
        "press_label":   "Press & editorial · principal releases",
        "press_heading": "MAGAZINES & MONOGRAPHS",
        "press": [
            {
                "year":    "2025",
                "outlet":  "FOAM Magazine no. 64",
                "type":    "Editorial portfolio",
                "subject": "Series «Porto Vecchio · Trieste»",
                "format":  "8 pages · offset print · Amsterdam",
            },
            {
                "year":    "2025",
                "outlet":  "Internazionale no. 1612",
                "type":    "Illustrated reportage",
                "subject": "Series «The stone houses · Salento»",
                "format":  "12 pages · rotogravure print · Rome",
            },
            {
                "year":    "2025",
                "outlet":  "Domus no. 1102",
                "type":    "Editorial commission",
                "subject": "Carlo Scarpa monograph issue",
                "format":  "16 pages · offset print · Milan",
            },
            {
                "year":    "2024",
                "outlet":  "The stone houses (monograph)",
                "type":    "Monograph volume",
                "subject": "Architectural reportage Salento 2023 — 24",
                "format":  "Publisher Quodlibet · 168 pp. · 24 × 28 cm",
            },
            {
                "year":    "2024",
                "outlet":  "GUP Magazine no. 73",
                "type":    "Critical essay",
                "subject": "Conversation with Sarah Kelly on long time",
                "format":  "10 pages · offset print · Amsterdam",
            },
            {
                "year":    "2023",
                "outlet":  "Vogue Italia · Photography section",
                "type":    "Editorial portrait",
                "subject": "Portraits of the Po · selected series",
                "format":  "6 pages · offset print · Milan",
            },
            {
                "year":    "2022",
                "outlet":  "Aperture no. 248",
                "type":    "Illustrated essay",
                "subject": "Reflection on film in the digital age",
                "format":  "8 pages · offset print · New York",
            },
            {
                "year":    "2019",
                "outlet":  "GUP Magazine no. 60 · cover",
                "type":    "Cover + illustrated essay",
                "subject": "Sarajevo markets archive 2009",
                "format":  "Cover + 14 pp. · offset print · Amsterdam",
            },
        ],

        # Exhibitions
        "exhibitions_label":   "Exhibitions · solo and group",
        "exhibitions_heading": "TWELVE SHOWS, FIFTEEN YEARS",
        "exhibitions": [
            ("2026", "FOAM Talent Lounge · Amsterdam",
             "Group show · 18 international photographers",
             "March — May 2026"),
            ("2024", "Triennale Milano · «Geography of a land»",
             "Solo show · series «The stone houses» · 38 prints",
             "September — December 2024"),
            ("2023", "Internazionale Festival Ferrara",
             "Group show · long-term projects section",
             "October 2023"),
            ("2022", "Photo London · Galleria Carla Sozzani booth",
             "Fine art market · 14 prints for sale",
             "May 2022"),
            ("2020", "MAXXI Rome · «Lockdown diaries»",
             "Group show · 12 prints of the personal contribution",
             "September — November 2020"),
            ("2018", "FOAM Talent · Amsterdam · selected series",
             "Group show · series «The night trains» · 16 prints",
             "April — June 2018"),
        ],

        # Awards & residencies
        "awards_label":   "Awards & residencies",
        "awards_heading": "RECOGNITIONS",
        "awards": [
            ("2024", "World Press Photo · Finalist · long-term projects",
             "Series «The stone houses»"),
            ("2023", "Magnum Foundation · Photography & Social Justice · selected",
             "Mentorship programme · 6 months in New York"),
            ("2021", "Magnum Foundation Grant · finalist emerging",
             "Study grant for personal work"),
            ("2020", "Premio Voglino · finalist",
             "Italian reportage category"),
            ("2016", "Premio Marco Pesaresi · finalist",
             "Italian reportage · «The passage»"),
            ("2014", "Premio Angelo Frontoni · selected",
             "Documentary photography category"),
        ],

        # Final CTA — speaking + workshops
        "cta_heading":      "[ TALKS · WORKSHOPS · LECTURES ]",
        "cta_intro":
            "For academic engagements (festivals, schools, "
            "universities), workshops on medium-format film or "
            "editorial lectures: open a conversation. Availability "
            "is scheduled at least three months in advance.",
        "cta_primary":      "Open a conversation",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI (contact) ─────────────────────────────────────
    "contatti": {
        "series_counter_label": "Availability",
        "series_counter_value": "2026 — 27",
        "status_pulse":         "Open to commissions",

        "eyebrow":   "Preliminary conversation · no intermediaries",
        "headline":  "[ OPEN A CONVERSATION ] <em>directly</em>",
        "subhead":
            "Commissions are discussed directly with the "
            "photographer, without an agent. For editorial "
            "proposals, brand commissions or fine art prints "
            "(representation Galleria Carla Sozzani · Milan): "
            "write a brief. I respond within seventy-two "
            "working hours.",

        # Studio info side card (dark style)
        "studio_label":   "Working studio",
        "studio_address": "Via Tadino 18 · 20124 Milan",
        "studio_area":    "Porta Venezia · side entrance · buzzer «Bianchi»",
        "studio_metro":   "MM1 / MM3 Loreto · 4 minutes on foot",
        "studio_hours":   "Available by appointment · never unannounced",
        "studio_row_address_label":  "Address",
        "studio_row_entrance_label": "Entrance",
        "studio_row_metro_label":    "Metro",
        "studio_row_hours_label":    "Available",

        # Form fields
        "form_label":   "Commission brief",
        "form_heading": "[ FILL THE BRIEF ]",
        "form_intro":
            "A commission brief is a structured description of "
            "the photographic project. Not a marketing brief — "
            "a preliminary conversation to see whether the "
            "discipline of the work matches mine.",
        "form_fields": [
            {"name": "name",      "label": "First name",    "type": "text",     "required": True,  "placeholder": "E.g. Lorenzo",
             "helper": "Given name only, thank you."},
            {"name": "surname",   "label": "Last name",     "type": "text",     "required": True,  "placeholder": "E.g. Bianchi",
             "helper": "As it appears in your byline."},
            {"name": "organization", "label": "Organisation", "type": "text", "required": False, "placeholder": "E.g. FOAM Magazine",
             "helper": "If the commission is editorial or brand."},
            {"name": "email",     "label": "Email",         "type": "email",    "required": True,  "placeholder": "lorenzo@foam.org",
             "helper": "Direct email · reply within 72 working hours."},
            {"name": "phone",     "label": "Phone",         "type": "tel",      "required": False, "placeholder": "+39 ...",
             "helper": "Only if you prefer a call back."},
            {"name": "discipline", "label": "Commission discipline", "type": "select", "required": True,
             "options": [
                 "To be defined in conversation",
                 "Long-form reportage",
                 "Editorial portrait",
                 "Brand commission",
                 "Architectural reportage",
                 "Fine art prints (Galleria Sozzani)",
                 "Workshop / lecture",
             ],
             "helper": "Choose «to be defined» if the scope is not yet clear."},
            {"name": "timeline",  "label": "Delivery time", "type": "select", "required": True,
             "options": [
                 "Within a month (fast delivery)",
                 "Three — six months (editorial commission)",
                 "Six — eighteen months (long-form work)",
                 "Exploratory · no deadline",
             ],
             "helper": "Delivery times determine the format (digital vs film)."},
            {"name": "location",  "label": "Location", "type": "text", "required": False,
             "placeholder": "E.g. Salento · Trieste · Sarajevo",
             "helper": "Indicate city / region / country · used to estimate travel."},
            {"name": "story",     "label": "The story you would like to tell", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Up to 1000 characters. A description of the subject, the reasons "
                            "behind the project and the planned publication. No marketing brief "
                            "— what matters here is the content, not the deliverable.",
             "helper": "If you do not know where to start, write what struck you."},
        ],

        "form_sections": [
            {"num": "01", "title": "Point of contact",
             "meta": "The person who will follow the commission from the client side.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Publication",
             "meta": "To understand the editorial or brand context.",
             "fields": ["organization"]},
            {"num": "03", "title": "Commission scope",
             "meta": "Delivery times determine the capture format — film vs digital.",
             "fields": ["discipline", "timeline", "location", "story"]},
            {"num": "04", "title": "References (optional)",
             "meta": "Editorial brief, issue plan, reference images. They can anticipate the conversation.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "brief_allegato",
            "label":    "Preliminary references",
            "helper":   "Editorial brief, issue plan, reference images. "
                        "PDF / DOCX / JPG / PNG · max 25 MB total.",
            "accept":   ".pdf,.docx,.jpg,.jpeg,.png",
            "multiple": True,
            "primary":  "Drag the documents here or",
            "link":     "browse from the archive",
            "meta":     "PDF / DOCX / JPG · max 25 MB",
        },

        "form_submit_label": "[ SEND THE BRIEF ]",
        "form_submit_note":
            "Reply directly from the photographer within 72 working hours. "
            "No agent, no lead automation.",
        "form_consent":
            "I consent to the processing of my personal data under "
            "EU Regulation 679/2016. Commission requests are read "
            "and archived by the photographer only. For fine art "
            "prints (secondary market) representation is held by "
            "Galleria Carla Sozzani.",

        # Sidebar — channels (EXIF style)
        "channels_label": "Direct channels",
        "channels": [
            ("Studio",         "studio@lorenzobianchi.photo",      "Reply within 72 hours"),
            ("Mobile",         "+39 348 211 7720",                 "Mon – Fri · 10:00 – 19:00"),
            ("Fine art prints", "Galleria Carla Sozzani · Milan",  "Corso Como 10 · +39 02 6555 2223"),
            ("Teaching",       "CFP Bauer · Milan",                "Documentary · 2nd year · Thursdays"),
        ],

        "footnote":
            "For fine art prints — secondary-market sales, limited "
            "editions, gallery exhibitions — exclusive representation "
            "is held by Galleria Carla Sozzani in Milan since 2018. "
            "Commercial print requests should be addressed directly "
            "to the gallery.",
    },

    # ─── POSTS — drives /serie/<slug>/ series_detail ────────────
    "posts": [
        {
            "slug":        "porto-vecchio-trieste",
            "title":       "Porto Vecchio · Trieste",
            "category":    "Long-form reportage",
            "discipline":  "Long-form reportage",
            "year":        "2024 — 2026",
            "duration":    "24 months · 18 trips",
            "location":    "Porto Vecchio · Trieste · Italy",
            "frame_count": "47 photographs",
            "edition":     "Limited edition · 12 + 2 AP per print",
            "print_meta": [
                ("Edition",        "12 + 2 AP per photograph"),
                ("Printing",       "Druckwerkstatt Berlin"),
                ("Paper",          "Hahnemühle Photo Rag Baryta 315 g/m²"),
                ("Representation", "Galleria Carla Sozzani · Milan"),
            ],
            "lead":
                "Twenty-four months inside the decommissioned port "
                "of Trieste — a sixty-six-hectare area between the "
                "Adriatic sea and the city, in transition between "
                "Habsburg industrial archaeology and an urban future "
                "still undecided. Forty-seven photographs on "
                "Kodak Portra 400 medium-format film.",
            "cover_image":
                "https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Camera",      "Mamiya 7II · 80mm + 43mm"),
                ("Film",        "Kodak Portra 400 medium format"),
                ("Period",      "November 2024 — January 2026"),
                ("Printing",    "Druckwerkstatt Berlin · 30 × 40 cm"),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=1600&q=85&auto=format&fit=crop",
                 "Frame 03",
                 "Porto Vecchio at dawn · San Marco basin · November 2024"),
                ("https://images.unsplash.com/photo-1505820013142-f86a3439c5b2?w=1600&q=85&auto=format&fit=crop",
                 "Frame 11",
                 "Abandoned warehouses · February 2025 · 6:14 in the morning"),
                ("https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1600&q=85&auto=format&fit=crop",
                 "Frame 18",
                 "View from the seaplane base · spring 2025"),
                ("https://images.unsplash.com/photo-1499346030926-9a72daac6c63?w=1600&q=85&auto=format&fit=crop",
                 "Frame 24",
                 "Decommissioned shipyard · summer 2025"),
                ("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1600&q=85&auto=format&fit=crop",
                 "Frame 31",
                 "Waterline · October 2025 · raking light"),
                ("https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=1600&q=85&auto=format&fit=crop",
                 "Frame 39",
                 "Final view · January 2026 · last trip"),
            ],
            "sections": [
                {
                    "label": "The series",
                    "heading": "Sixty-six hectares, twenty-four months",
                    "body":
                        "The Porto Vecchio of Trieste is a "
                        "sixty-six-hectare area on the Adriatic sea, "
                        "decommissioned since 1991 and still waiting "
                        "for a definitive urban plan. The series "
                        "follows its suspended state between November "
                        "2024 and January 2026 — eighteen trips, "
                        "three complete seasons, only the early-morning "
                        "light. The work was published in FOAM Magazine "
                        "no. 64 (November 2025) and is on view at the "
                        "FOAM Talent Lounge in Amsterdam from March 2026.",
                },
                {
                    "label": "The method",
                    "heading": "Film, dawn, return",
                    "body":
                        "I always photographed with Mamiya 7II and "
                        "Kodak Portra 400 medium-format film — two "
                        "lenses, eighty and forty-three millimetres. "
                        "The entire work was made between 5:30 and "
                        "7:00 in the morning, before the arrival of "
                        "the security staff. The light of Trieste in "
                        "that window is particular — the overnight "
                        "bora wind cleans the air, the water in the "
                        "basin is a mirror, the sun has not yet risen "
                        "above the Carso.",
                },
                {
                    "label": "The edition",
                    "heading": "Fine art print · twelve copies",
                    "body":
                        "The fine art edition includes twelve prints "
                        "+ two artist proofs for each photograph, "
                        "printed on Hahnemühle Photo Rag Baryta "
                        "315 g/m² paper at Druckwerkstatt Berlin in "
                        "collaboration with Anna Wedekind. The print "
                        "size is 30 × 40 cm. Fine art distribution is "
                        "exclusive to Galleria Carla Sozzani in Milan.",
                },
            ],
            "next_label": "Next series",
        },
        {
            "slug":        "case-di-pietra-puglia",
            "title":       "The stone houses · Salento",
            "category":    "Architectural reportage",
            "discipline":  "Architectural reportage",
            "year":        "2023 — 2024",
            "duration":    "16 months · 9 trips",
            "location":    "Salento · Puglia · Italy",
            "frame_count": "62 photographs",
            "edition":     "Monograph edition · Quodlibet · 168 pp.",
            "print_meta": [
                ("Edition",        "1,500 copies · first reprint sold out"),
                ("Printing",       "Quodlibet · Macerata"),
                ("Paper",          "Munken Pure 130 g/m² · uncoated"),
                ("Representation", "Galleria Carla Sozzani · Milan"),
            ],
            "lead":
                "Sixteen months inside the drystone farmhouses of "
                "southern Salento — forty buildings, no contemporary "
                "intervention. Documentary architectural reportage, "
                "published as a monograph by Quodlibet (November 2024) "
                "and in Internazionale no. 1612 (September 2025).",
            "cover_image":
                "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Camera",      "Mamiya 7II + Sony α7R V"),
                ("Film",        "Kodak Portra 400 + dual-sensor digital"),
                ("Period",      "March 2023 — July 2024"),
                ("Printing",    "Quodlibet volume · 24 × 28 cm · 168 pp."),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1543248939-4296e1fea89b?w=1600&q=85&auto=format&fit=crop",
                 "Frame 04",
                 "Masseria San Giovanni · Otranto · spring 2023"),
                ("https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?w=1600&q=85&auto=format&fit=crop",
                 "Frame 12",
                 "Trullo dei Cento Giganti · Locorotondo · summer 2023"),
                ("https://images.unsplash.com/photo-1512100356356-de1b84283e18?w=1600&q=85&auto=format&fit=crop",
                 "Frame 22",
                 "Masseria Pulicchia · Galatina · autumn 2023"),
                ("https://images.unsplash.com/photo-1518131672697-613becd4fab5?w=1600&q=85&auto=format&fit=crop",
                 "Frame 31",
                 "Interior lamia · Sannicola · January 2024"),
                ("https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600&q=85&auto=format&fit=crop",
                 "Frame 41",
                 "Drystone wall · Specchia · March 2024"),
                ("https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=1600&q=85&auto=format&fit=crop",
                 "Frame 53",
                 "Inner courtyard · Tricase · July 2024"),
            ],
            "sections": [
                {
                    "label": "The series",
                    "heading": "Forty buildings, sixteen months",
                    "body":
                        "The reportage documents forty drystone "
                        "buildings of southern Salento — masserie, "
                        "lamie, lesser trulli, pajare. The idea was "
                        "to document them before any possible "
                        "restoration or demolition, in collaboration "
                        "with the Centro Studi Salentini in Lecce. "
                        "Sixteen months of work, nine trips, "
                        "sixty-two selected photographs.",
                },
                {
                    "label": "The method",
                    "heading": "Dual format for documentation",
                    "body":
                        "Unlike the personal work, here I worked in "
                        "dual format — Mamiya 7II on film for the "
                        "exteriors and Sony α7R V digital for the "
                        "interiors (for precise architectural "
                        "documentation). The two formats live side "
                        "by side in the Quodlibet volume without "
                        "obvious editorial distinction — film and "
                        "digital, once on the printed page, become "
                        "indistinguishable at 24 × 28 cm.",
                },
                {
                    "label": "The volume",
                    "heading": "One hundred and sixty-eight pages, Quodlibet",
                    "body":
                        "The monograph volume «The stone houses» "
                        "was published by Quodlibet (November 2024) "
                        "with a critical essay by Salvatore Settis. "
                        "One hundred and sixty-eight pages, 24 × 28 cm "
                        "format, sewn paperback, uncoated Munken "
                        "Pure 130 g/m² paper. Edition of 1,500 "
                        "copies, first reprint sold out in three "
                        "months. Finalist selection at the World "
                        "Press Photo 2024 in the long-term projects "
                        "category.",
                },
            ],
            "next_label": "Next series",
        },
        {
            "slug":        "ritratti-del-po",
            "title":       "Portraits of the Po",
            "category":    "Author portrait",
            "discipline":  "Author portrait",
            "year":        "2023",
            "duration":    "8 months · 7 trips",
            "location":    "Po Delta · Veneto · Italy",
            "frame_count": "28 photographs",
            "edition":     "Published · Vogue Italia photography",
            "print_meta": [
                ("Edition",        "8 + 2 AP per selected print"),
                ("Printing",       "Personal prints · kitchen in Milan"),
                ("Paper",          "Ilford Multigrade FB Classic"),
                ("Representation", "Galleria Carla Sozzani · Milan"),
            ],
            "lead":
                "Twenty-eight portraits of fishermen, clam harvesters "
                "and barge pilots from the Veneto Po Delta. Eight "
                "months of work between spring and autumn 2023, "
                "published in the Photography section of Vogue Italia "
                "(December 2023) and shown at the Internazionale "
                "Festival in Ferrara (October 2023).",
            "cover_image":
                "https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Camera",      "Mamiya 7II · 80mm"),
                ("Film",        "Kodak Portra 400 medium format"),
                ("Period",      "April — November 2023"),
                ("Printing",    "Personal prints · kitchen in Milan"),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=1600&q=85&auto=format&fit=crop",
                 "Frame 01",
                 "Aldo · fisherman · Pila · May 2023"),
                ("https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=1600&q=85&auto=format&fit=crop",
                 "Frame 06",
                 "Maria · clam harvester · Goro · June 2023"),
                ("https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=1600&q=85&auto=format&fit=crop",
                 "Frame 12",
                 "Carlo and Giuseppe · fisherman brothers · July 2023"),
                ("https://images.unsplash.com/photo-1502323777036-f29e3972d82f?w=1600&q=85&auto=format&fit=crop",
                 "Frame 17",
                 "Anna · restaurant owner · September 2023"),
                ("https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=1600&q=85&auto=format&fit=crop",
                 "Frame 22",
                 "Luca · barge pilot · October 2023"),
                ("https://images.unsplash.com/photo-1521252659862-eec69941b071?w=1600&q=85&auto=format&fit=crop",
                 "Frame 28",
                 "Final portrait · November 2023 · last light"),
            ],
            "sections": [
                {
                    "label": "The series",
                    "heading": "Twenty-eight people, eight months",
                    "body":
                        "A series of twenty-eight portraits of those "
                        "who live the Veneto Po Delta as a working "
                        "place — fishermen, clam harvesters, "
                        "restaurateurs, barge pilots. Eight months "
                        "of work between April and November 2023, "
                        "seven trips across the two provinces "
                        "(Rovigo + Ferrara). Each portrait was "
                        "preceded by at least one day spent with the "
                        "subject — never drop-in sessions.",
                },
                {
                    "label": "The method",
                    "heading": "One camera, one light",
                    "body":
                        "All the portraits were made with Mamiya 7II "
                        "and the eighty-millimetre lens, in natural "
                        "available light — no flash, no diffuser "
                        "panels. The film is always Kodak Portra "
                        "400, developed at home. The choice of a "
                        "single lens (instead of a kit of three or "
                        "four) is a formal discipline — it forces "
                        "me to move in relation to the subject "
                        "rather than turn the lens ring.",
                },
                {
                    "label": "The publication",
                    "heading": "Vogue Italia · Ferrara Festival",
                    "body":
                        "The series was published in the Photography "
                        "section of Vogue Italia (December 2023, "
                        "six pages) and shown in a group exhibition "
                        "at the Internazionale Festival in Ferrara "
                        "(October 2023, twelve selected prints). "
                        "One print has entered the permanent "
                        "collection of MAXXI in Rome.",
                },
            ],
            "next_label": "Next series",
        },
    ],
}
