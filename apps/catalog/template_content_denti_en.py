"""Denti+Co — Studio Dentistico · English (EN) content tree.

Wave 1 Pass-2 (T46 · 2026-05-11) · workflow C multilingual rollout.
Authored as part of the 4 sub-agent parallel translator pass (EN/FR/ES/AR)
that mirrors the IT tree at `template_content_denti.py` (DENTI_CONTENT_IT)
established in T45 Pass-1.

Mirror policy
=============
Strict shape-parity with DENTI_CONTENT_IT. Every top-level key, every
nested key, every tuple arity is preserved verbatim — the Django template
engine fails ungracefully on missing keys, so this tree is a 1:1 structural
clone of the Italian source. Only the *visible labels, headings, body
copy, FAQs, treatment names and CTAs* are localised. Page slugs stay
Italian (home/studio/visite/medici/pubblicazioni/contatti/richiedi-visita)
because URLs are language-agnostic in the specialist routing layer; only
the `label` field on each pages-entry is translated.

Voice anchor: igiene → hygiene
==============================
The IT brand voice is built on the noun-em italic word "igiene" (clinical
hygiene as repeated motif). The EN tree carries that anchor by using
`<em>hygiene</em>` in the same surface locations IT uses `<em>igiene</em>`
— hero headline, manifesto, side-quote, FAQ, CTA band. The verb-em form
on the side-quote and body becomes the verb-form derived from "hygiene"
(e.g. "Hygiene is not a detail — it's the first chapter").

Tone register
=============
Anglo-American clinical-premium. Direct, unembellished, precise. Think
NYT Wellness or Atlantic Health desk — NOT mechanical IT→EN gloss, NOT
NHS-bureaucratic, NOT marketingese. Dental terminology is the natural
EN clinical register: "professional cleaning" (not "professional hygiene"
as a service name — though the anchor word "hygiene" survives), "fillings"
(not "restorations" unless clinically precise), "Invisalign" stays
Invisalign, "clear aligners" for the SmileLab equivalent.

Non-localisable verbatim data
=============================
- phone "+39 02 7770 4488"
- email "studio@denticostudio.it"
- address "Via Manzoni 18 · 20121 Milan" ("Milano" → "Milan" only here)
- all prices in € (€ 95, € 220, € 1,850, ...)
- doctor surnames + given names (Chiara Vespa, Riccardo Berti,
  Sofia Liccardi, Andrea Carofiglio). "Dr.ssa" honorific collapsed to
  "Dr." for both genders per Anglo convention.
- press outlets in original Italian script (Il Dentista Moderno,
  Dental Tribune, Bocca & Salute, Corriere Salute, Vanity Fair Italia).
- imagery URLs (_CHIEF_PORTRAIT, _LEAD_IMAGE, the three inline doctor
  portraits, the studio_image, the map_fallback_image) — pulled
  verbatim from the IT tree via re-import.
"""
from __future__ import annotations

from typing import Any

from apps.catalog.template_content_denti import (
    _CHIEF_PORTRAIT,
    _LEAD_IMAGE,
)


DENTI_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Studio",           "kind": "home"},
        {"slug": "studio",          "label": "The Studio",       "kind": "about"},
        {"slug": "visite",          "label": "Treatments",       "kind": "services"},
        {"slug": "medici",          "label": "Dentists",         "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Publications",     "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contact",          "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Book a cleaning",  "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "D",
        "logo_word":    "Denti+Co",
        "tag":          "Associated dental practice · Milan Brera",
        "phone":        "+39 02 7770 4488",
        "email":        "studio@denticostudio.it",
        "address":      "Via Manzoni 18 · 20121 Milan",
        "hours_compact": "Mon – Fri · 8:30 – 19:30",
        "hours_footer_rows": [
            "Saturday · 9:00 – 13:00",
            "Sunday · closed",
        ],
        "license":      "OMCeO Milan registration 03 / 18742 · Medical Director Dr. C. Vespa",
        "footer_intro":
            "An associated dental practice for conservative dentistry, "
            "professional hygiene and implantology. Four clinicians, "
            "one shared chart per patient.",
    },

    "home": {
        # Hero — editorial-magazine variant: portrait-driven, different
        # silhouette from Cardio's default split-consultive.
        "hero_variant": "editorial-magazine",
        "eyebrow":  "Dentistry · Milan Brera",
        "headline": "<em>Hygiene</em> is not a detail. It's the first chapter.",
        "intro":
            "Professional hygiene, conservative dentistry, implantology "
            "and clear-aligner orthodontics. Four associated dentists, "
            "one shared chart, twice-yearly check-ups included in the "
            "annual plan.",
        "primary_cta":   "Book a cleaning",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "About the studio",
        "secondary_href":"studio",

        # Three-fact band (Cardio uses 3 numbers · we use 3 dental-coded)
        "facts": [
            ("12", "years as an associated practice"),
            ("3,400", "cleanings & check-ups per year"),
            ("4", "in-house dental specialists"),
        ],

        # Manifesto with drop-cap (specialist archetype signature)
        "manifesto_drop_cap": "O",
        "manifesto":
            "ral health is not something you fix twice a year — it's "
            "something you sustain every day. That is why Denti+Co "
            "starts every patient relationship with hygiene: "
            "professional, repeatable, measurable. Conservative work, "
            "implantology and orthodontics are built around it. Four "
            "specialists, one shared clinical chart, one signature on "
            "every care plan. No upselling, no fragmented treatment: "
            "hygiene is the first chapter and the only real gate.",

        # Hero right sidebar (when hero_variant is split-consultive only —
        # but we kept the pulse data so the editorial-magazine pulse rail
        # also renders.)
        "hero_sidebar_top_label": "Clinical leadership",
        "hero_sidebar_quote":
            "“Done properly, professional hygiene prevents seventy "
            "percent of invasive treatment. For us it is serious clinical "
            "work, not a cosmetic service.”",
        "hero_sidebar_author": "— Dr. Chiara Vespa · Medical Director",
        "hero_sidebar_pulse": [
            ("Studio",    "Milan · Brera"),
            ("Since",     "2013"),
            ("Field",     "Associated dentistry"),
        ],

        # Anchor subnav (helps a dense home read like a magazine)
        "anchor_nav": [
            ("metodo",      "Method"),
            ("trattamenti", "Treatments"),
            ("percorso",    "Patient journey"),
            ("medico",      "Clinical leadership"),
            ("studio",      "Location & contact"),
        ],

        # Signature treatments (numbered 01-04 · the dental version of
        # Cardio's signature_visits — four core dental categories)
        "signature_visits_label":   "Treatments & pathways",
        "signature_visits_heading": "Four clinical pathways, <em>one chart.</em>",
        "signature_visits_intro":
            "The four families of treatment we are asked for most often. "
            "The full list lives on the Treatments page.",
        "signature_visits": [
            ("01", "Twice-yearly professional cleaning",
             "Supra- and subgingival scaling, sodium-bicarbonate "
             "air-polishing, bleeding index and PSR charting. Included "
             "in the annual maintenance plan."),
            ("02", "Conservative dentistry",
             "Layered composite fillings, aesthetic rebuilds, "
             "root-canal treatment with apical locator. Rubber dam "
             "mandatory on every conservative procedure."),
            ("03", "Implantology & bone regeneration",
             "Single implants and full-arch rehabilitations with "
             "immediate loading. Computer-guided planning and 3D-printed "
             "surgical guides produced in our in-house lab."),
            ("04", "Clear-aligner orthodontics",
             "Invisalign and SmileLab clear aligners for adults, "
             "interceptive orthodontics for children aged 8–12 with "
             "removable appliances. Monthly check-ins included."),
        ],

        # Trattamenti tabs section (the four dental categories with
        # detailed treatment lists — uses the trattamenti_tabs DNA hook
        # the specialist skin already supports, see home.html L954+).
        "trattamenti_tabs": {
            "label":   "Treatment price list",
            "heading": "What we do, on <em>what terms.</em>",
            "intro":
                "Four clinical categories, each with a written protocol "
                "and a declared price. No bespoke quote for routine items "
                "— only for structured care plans.",
            "tabs": [
                {
                    "id":      "igiene",
                    "label":   "Hygiene",
                    "eyebrow": "Professional hygiene",
                    "heading": "Forty-five minutes, not twenty.",
                    "body":
                        "Hygiene is not a routine slot — it is a "
                        "forty-five-minute clinical appointment with "
                        "periodontal charting, bleeding index, "
                        "bicarbonate air-polishing and check-up photos.",
                    "items": [
                        ("Single professional cleaning", "45 min · € 95"),
                        ("Annual plan (2 cleanings + 1 check-up)", "yearly · € 220"),
                        ("Bicarbonate air-polishing", "included · free"),
                        ("Fissure sealing (per tooth)", "10 min · € 30"),
                    ],
                    "cta_label": "All hygiene plans →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "conservativa",
                    "label":   "Conservative",
                    "eyebrow": "Conservative dentistry",
                    "heading": "Layered composite, always under rubber dam.",
                    "body":
                        "Light-cured composite fillings, aesthetic "
                        "rebuilds, root-canal treatment with apical "
                        "locator. Rubber dam is mandatory on every "
                        "conservative procedure. No amalgam fillings "
                        "in this studio since 2013.",
                    "items": [
                        ("Single-surface filling", "45 min · € 140"),
                        ("Multi-surface filling (2–3 surfaces)", "60 min · € 220"),
                        ("Single-root endodontic treatment", "75 min · € 280"),
                        ("Multi-root endodontic treatment", "120 min · € 420"),
                    ],
                    "cta_label": "Full conservative price list →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "implantologia",
                    "label":   "Implantology",
                    "eyebrow": "Implantology & bone regeneration",
                    "heading": "Italian implants, lifetime fixture warranty.",
                    "body":
                        "Sweden+Martina implants made in Italy, "
                        "computer-guided planning with cone-beam CT, "
                        "3D-printed surgical guide produced in our "
                        "in-house lab. Immediate loading only in "
                        "selected cases after clinical assessment.",
                    "items": [
                        ("Single implant (fixture + zirconia crown)", "procedure · € 1,850"),
                        ("Mini sinus lift", "procedure · € 950"),
                        ("Bone regeneration (single site)", "procedure · € 480"),
                        ("Fixed full-arch on 4 implants", "plan · custom quote"),
                    ],
                    "cta_label": "Implantology pathways →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "ortodonzia",
                    "label":   "Orthodontics",
                    "eyebrow": "Clear aligners & interceptive orthodontics",
                    "heading": "Clear aligners for adults, interceptive for children.",
                    "body":
                        "Invisalign and SmileLab clear aligners with "
                        "iTero intraoral scanning and a simulated 3D "
                        "plan reviewed before treatment begins. "
                        "Interceptive orthodontics ages 8–12 with "
                        "removable appliances. Monthly check-in "
                        "included in the plan.",
                    "items": [
                        ("Invisalign aligners — complete plan", "12–18 months · € 3,200"),
                        ("SmileLab aligners — complete plan", "10–14 months · € 2,400"),
                        ("Interceptive orthodontics for children", "12–24 months · € 1,600"),
                        ("Nightly retainer after treatment", "permanent · € 220"),
                    ],
                    "cta_label": "Orthodontic protocols →",
                    "cta_href":  "visite",
                },
            ],
        },

        "chief_label":   "Clinical leadership",
        "chief_heading": "One signature <em>on every chart.</em>",
        "chief": {
            "name":  "Dr. Chiara Vespa",
            "role":  "Medical Director · Conservative dentistry & endodontics",
            "bio":
                "Specialist in conservative dentistry, trained at the "
                "University of Milan and post-qualified at Loma Linda "
                "University in California. Member of the SIE (Italian "
                "Society of Endodontics) and a regular lecturer at the "
                "annual courses of the Lombard School of Dentistry. "
                "Medical Director of the studio since 2013.",
            "portrait": _CHIEF_PORTRAIT,
        },

        # Patient journey — five steps in dental key (Cardio uses
        # arrival → anamnesi → ECG → diagnostica → piano scritto; we
        # use arrival → check-in → cartella+foto → trattamento → follow-up)
        "percorso": {
            "label":   "Patient journey",
            "heading": "What to expect from the <em>first visit.</em>",
            "intro":
                "Your first visit is dedicated to building the clinical "
                "chart: photos, indices, intraoral scan and a written "
                "care plan. We never treat on the first session — "
                "except for documented emergencies.",
            "steps": [
                {
                    "num": "01",
                    "icon": "clipboard",
                    "title": "Check-in & medical history",
                    "desc": "Reception, medical-history form covering "
                            "general and dental history, any prior "
                            "radiographs or recent panoramic.",
                    "duration": "10 min",
                },
                {
                    "num": "02",
                    "icon": "book",
                    "title": "Full clinical examination",
                    "desc": "Periodontal charting, plaque index, "
                            "bleeding index, objective exam of soft "
                            "tissues and oral mucosa.",
                    "duration": "20 min",
                },
                {
                    "num": "03",
                    "icon": "heart",
                    "title": "Photography & scanning",
                    "desc": "Standardised photo set (8 intraoral + 4 "
                            "extraoral), iTero intraoral scan for the "
                            "digital archive.",
                    "duration": "15 min",
                },
                {
                    "num": "04",
                    "icon": "chart",
                    "title": "Written care plan",
                    "desc": "Plan discussed at the chair with an "
                            "itemised quote line by line, delivered "
                            "also as a PDF.",
                    "duration": "15 min",
                },
                {
                    "num": "05",
                    "icon": "document",
                    "title": "Scheduling & follow-up",
                    "desc": "Appointment calendar, hygiene recall when "
                            "indicated, direct WhatsApp channel for "
                            "any clinical urgency.",
                    "duration": "5 min",
                },
            ],
        },

        # Press strip (dental-coded outlets · NOT cardiology titles)
        "press": ["Il Dentista Moderno", "Dental Tribune", "Bocca & Salute",
                  "Corriere Salute", "Vanity Fair Italia"],
        "press_label": "Featured in",

        # FAQ (dental-specific questions, not cardio)
        "faq": {
            "label": "Frequently asked questions",
            "heading": "The questions <em>we hear most often.</em>",
            "items": [
                ("How often should I have a professional cleaning?",
                 "For patients without active periodontal disease the "
                 "cadence is every six months. For patients with "
                 "gingivitis, periodontitis or orthodontic appliances "
                 "it drops to every three or four months. The plan is "
                 "personalised after the first visit."),
                ("Do composite fillings really last?",
                 "Yes — provided the cavity is rebuilt under rubber dam "
                 "with layered composite and a qualified LED light. Our "
                 "fillings have a median survival of ten years with "
                 "regular check-ups. We have not used amalgam since 2013."),
                ("How much does an implant actually cost?",
                 "A single implant (Sweden+Martina titanium fixture + "
                 "zirconia crown) is € 1,850, VAT included. Any "
                 "preliminary regenerative work (sinus lift, GBR) is "
                 "excluded and only quoted after a cone-beam CT."),
                ("Do clear aligners really work for adults?",
                 "For around ninety percent of adult clinical cases, "
                 "clear aligners (Invisalign or SmileLab) are as "
                 "effective as traditional fixed braces. The cases that "
                 "still require fixed braces — severe premolar rotations "
                 "and marked extrusions — are flagged openly in the "
                 "treatment plan."),
                ("Can I bring my children to the same studio?",
                 "Yes. Dr. Liccardi handles interceptive orthodontics "
                 "for children aged 8–12 with removable appliances. "
                 "Paediatric hygiene is included for the children of "
                 "patients on an active annual plan."),
            ],
        },

        # Bottom CTA band
        "cta_heading":
            "Every care plan is <em>written, declared, shared.</em>",
        "cta_primary_label":   "Book a cleaning",
        "cta_secondary_label": "Studio contact details",

        # Sede / Location — Milan Brera, different from Cardio Roma Parioli
        # and Derm Roma Veneto
        "location": {
            "label":   "Studio location",
            "heading": "Via Manzoni 18, <em>Milan.</em>",
            "intro":
                "The studio occupies the piano nobile of a historic "
                "palazzo in the Brera district, a hundred and twenty "
                "metres from Via Montenapoleone. Four operatories, a "
                "cone-beam CT radiology room, an in-house orthodontic "
                "laboratory.",
            "map_image": "",
            "map_fallback_image":
                # Bright clean modern dental clinic room — Daniel Frank
                # 3888×2592 · used as map-fallback when Mapbox tile fails
                "https://images.pexels.com/photos/305567/pexels-photo-305567.jpeg"
                "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
            "details": [
                ("Address",
                 "Via Manzoni 18\n20121 Milan"),
                ("Underground",
                 "M3 Montenapoleone\n3 minutes on foot"),
                ("Parking",
                 "Partner garage in Via Bigli\n50 metres from the entrance"),
                ("Accessibility",
                 "Step-free entrance with lift\nto the piano nobile"),
            ],
            "hours_short": [
                ("Mon – Fri", "8:30 – 19:30"),
                ("Saturday",  "9:00 – 13:00"),
                ("Sunday",    "Closed"),
            ],
            "cta_label": "Get directions",
            "cta_href":  "contatti",
        },
    },

    # ─── STUDIO (about) — full content, all keys the specialist
    # about.html requires (history, method_*, values_*, cta_*).
    "studio": {
        "eyebrow":   "The studio · Milan Brera",
        "headline":  "Four dentists, <em>one shared chart.</em>",
        "intro":
            "Denti+Co is an associated practice founded in 2013 by four "
            "clinicians who share the same clinical chart and the same "
            "working protocol: photographs before and after, rubber dam "
            "every time, written quote delivered as a PDF, scheduled "
            "follow-up.",
        # 5-row history timeline (year + 1-line description · 2-tuples)
        "history": [
            ("2013",
             "Founding of the associated practice in Via Manzoni with "
             "two specialists and one operatory."),
            ("2016",
             "Launch of the implantology unit with a Carestream CS 9600 "
             "cone-beam CT and a dedicated surgical room."),
            ("2019",
             "Adoption of iTero intraoral scanning and simulated 3D "
             "orthodontic plans before treatment."),
            ("2022",
             "Opening of the in-house orthodontic lab with 3D printing "
             "of surgical guides and night retainers."),
            ("2025",
             "The studio closes the year with four full-time associates "
             "and a team of six hygienists."),
        ],
        "studio_image":
            # Stylish modern dentist office wide — Cedric Fauntleroy 8244×5496
            "https://images.pexels.com/photos/4269268/pexels-photo-4269268.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop",
        "studio_image_caption": "Operatory · Via Manzoni 18",
        "method_title": "The Denti+Co method",
        "method_paragraphs": [
            "Hygiene is the first chapter because it is also the most "
            "repeatable. Almost nobody walks into the studio for the "
            "first time with a mouth in good order: for most patients "
            "there is groundwork to do before we can talk about "
            "aesthetics, orthodontics or implantology. Forty minutes "
            "of professional hygiene, done well, change the way every "
            "subsequent quote is read.",
            "There is only one clinical chart — the same one for all "
            "four associates — because a patient is not the patient of "
            "a single dentist, they are the patient of the studio. When "
            "the hygienist notes gingival recession during a recall, "
            "she flags it to the periodontist in the same clinical "
            "document. No fragmented treatment.",
            "Prices are declared for routine items (cleaning, "
            "conservative work, whitening, check-up). For more "
            "structured plans — implantology with regeneration, "
            "complex orthodontics, full-mouth rehabilitations — the "
            "quote is custom-built after a seventy-minute first visit, "
            "but always written, signed and handed over.",
        ],
        "values_label":   "Studio values",
        "values_heading": "Four commitments, <em>written into the chart.</em>",
        "values": [
            ("Rubber dam every time",
             "On every conservative, endodontic and composite "
             "procedure. No exceptions."),
            ("Photos before and after",
             "Standardised photo set handed to the patient in digital "
             "form at the end of every care plan."),
            ("Written quote",
             "Cost is never discussed verbally only. PDF by email or "
             "delivered in studio before any work begins."),
            ("Scheduled follow-up",
             "Maintenance-appointment calendar sent by SMS or "
             "WhatsApp. No patient is left to themselves after a "
             "procedure."),
        ],
        "cta_heading":
            "The first step is always <em>a seventy-minute visit.</em>",
        "cta_primary_label":   "Meet the dentists",
        "cta_secondary_label": "Book your first visit",
        "press_label": "Featured in",
        "press": ["Il Dentista Moderno", "Dental Tribune",
                  "Bocca & Salute", "Corriere Salute"],
    },

    # ─── VISITE (services) — services.html expects `treatments`
    # as a list of 4-tuples (name, meta, desc, price) + cta_*.
    "visite": {
        "eyebrow":  "Treatments · 2026 price list",
        "headline": "What we do, <em>what it costs, what we stand behind.</em>",
        "intro":
            "The full price list for routine items. Structured care "
            "plans (complex implantology, orthodontics, full-mouth "
            "rehabilitations) always receive a personalised quote "
            "after the first visit.",
        "service_image":
            # Close-up advanced dental chair setup with instruments —
            # cottonbro studio 6365×4244 · evokes precision + sterilità
            "https://images.pexels.com/photos/6502543/pexels-photo-6502543.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop",
        "service_image_caption": "Operatory · instrumentation and in-house lab",
        "treatments": [
            ("Single professional cleaning",
             "45 min · no referral required",
             "Periodontal charting, bleeding index, sodium-bicarbonate "
             "air-polishing, check-up photos. Includes a review of "
             "at-home hygiene habits and, where indicated, a trial "
             "sonic toothbrush.",
             "€ 95"),
            ("Annual maintenance plan",
             "yearly · 2 cleanings + 1 check-up + bitewings",
             "Two six-monthly cleanings scheduled in advance, one "
             "follow-up visit with photos, bitewing radiographs when "
             "indicated. Direct WhatsApp channel for any urgent issue.",
             "€ 220"),
            ("Conservative filling (single surface)",
             "45 min · layered composite under rubber dam",
             "Tokuyama or 3M composite, always under rubber dam, with "
             "a qualified LED light. Five-year sealing warranty with "
             "regular check-ups.",
             "€ 140"),
            ("Single-root endodontic treatment",
             "75 min · apical locator + thermoplastic obturation",
             "Endodontic treatment with a Morita apical locator, "
             "three-dimensional obturation with thermoplastic "
             "gutta-percha, composite coronal restoration. Radiographic "
             "follow-up at six and twelve months.",
             "€ 280"),
            ("Single implant (fixture + zirconia crown)",
             "procedure + 2 check-ups · lifetime fixture warranty",
             "Italian Sweden+Martina implant, stabilised zirconia "
             "abutment, monolithic crown milled in the in-house lab. "
             "Preliminary cone-beam CT included.",
             "€ 1,850"),
            ("Invisalign clear aligners (complete plan)",
             "12–18 months · iTero scan + 3D plan + retainer",
             "iTero intraoral scan, 3D simulated plan handed to the "
             "patient before starting. Aligners delivered stage by "
             "stage. Night retainer after treatment included.",
             "€ 3,200"),
            ("Professional in-chair whitening",
             "60 min · 35 % peroxide + gingival-barrier gel",
             "A single sixty-minute session with 35 % hydrogen "
             "peroxide, light-cured gingival-barrier gel, salivary "
             "pH check before and after treatment.",
             "€ 380"),
            ("First visit (chart + plan)",
             "70 min · history + iTero scan + plan as PDF",
             "Medical and dental history, objective exam, periodontal "
             "charting, intraoral scan, photos, written care plan "
             "delivered as a PDF. Cost deducted from the first "
             "treatment.",
             "€ 80"),
        ],
        "footnote_heading": "What is NOT included in the price list",
        "footnote":
            "The routine items above are declared. Structured care "
            "plans (full-mouth rehabilitations, implantology with "
            "extensive regeneration, orthodontics combined with "
            "orthognathic surgery) receive a personalised quote after "
            "the seventy-minute first visit. We never quote over the "
            "phone or by email before a clinical examination.",
        "cta_heading":
            "Every quote is <em>written, signed and delivered as a PDF.</em>",
        "cta_primary_label":   "Book your first visit",
        "cta_secondary_label": "Get in touch",
    },

    # ─── MEDICI (team) — 4 dental specialists, mix gender ───
    "medici": {
        "eyebrow":  "The dentists · associated team",
        "headline": "Four signatures, <em>one shared chart.</em>",
        "intro":
            "The four associates share the same clinical chart and "
            "consult one another on complex plans. Each patient has a "
            "named reference dentist, but maintenance hygiene can be "
            "carried out by any member of the team.",
        "doctors": [
            {
                "name":  "Dr. Chiara Vespa",
                "role":  "Medical Director · Conservative & endodontics",
                "bio":
                    "Specialist in conservative dentistry, trained at "
                    "the University of Milan and post-qualified at "
                    "Loma Linda University. Member of the SIE (Italian "
                    "Society of Endodontics). Clinical coordinator of "
                    "the studio since 2013.",
                "portrait": _CHIEF_PORTRAIT,
            },
            {
                "name":  "Dr. Riccardo Berti",
                "role":  "Implantology & bone regeneration",
                "bio":
                    "Implantologist trained at the New York University "
                    "College of Dentistry and post-qualified in "
                    "Clinical Gnathology at the University of Pavia. "
                    "Focuses on computer-guided implantology, complex "
                    "rehabilitations and bone regeneration.",
                "portrait":
                    # Medical pro in protective gear — kaboompics 4480×6720
                    "https://images.pexels.com/photos/6627850/pexels-photo-6627850.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
            {
                "name":  "Dr. Sofia Liccardi",
                "role":  "Orthodontics & paediatric dentistry",
                "bio":
                    "Specialist in orthodontics, trained at the "
                    "Università Cattolica del Sacro Cuore. Certified "
                    "Invisalign Diamond Provider. Focuses on adult "
                    "orthodontics, interceptive treatment for children "
                    "and paediatric care up to the age of sixteen.",
                "portrait":
                    # Asian female dentist in clinic — Polina Zimmerman
                    # 3646×5469 · matches female lead role
                    "https://images.pexels.com/photos/4687404/pexels-photo-4687404.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
            {
                "name":  "Dr. Andrea Carofiglio",
                "role":  "Periodontology & oral medicine",
                "bio":
                    "Periodontist trained at the University of Bologna "
                    "and post-qualified at the University of Bern. "
                    "Member of the SIdP (Italian Society of "
                    "Periodontology and Implantology). Focuses on "
                    "chronic periodontitis and oral medicine.",
                "portrait":
                    # Dentist performing dental care — cottonbro studio
                    # 4047×6070 · portrait orientation, white coat
                    "https://images.pexels.com/photos/6529057/pexels-photo-6529057.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
        ],
        "portrait_city": "Milan · Brera",
    },

    # ─── PUBBLICAZIONI (blog_list) — page metadata at this level,
    # the actual post list lives at the TOP-LEVEL `posts` key (sibling
    # to `pubblicazioni`), the same shape Cardio + Derm use.
    "pubblicazioni": {
        "eyebrow":  "Publications & writing",
        "headline": "What we have written, <em>and for whom.</em>",
        "intro":
            "Plain-language articles published in specialist dental "
            "press and clinical contributions to scientific journals. "
            "Every piece is reviewed personally by Dr. Vespa before "
            "publication.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Denti+Co · Associated dental practice · Milan",
        "empty_body_fallback_paragraphs": [
            "Article in editorial preparation. The full text will be "
            "available shortly.",
            "This placeholder stands in for the article's voice: a "
            "clinical note written by the dentist, in direct prose, "
            "free of jargon, intended for patients who want reliable "
            "information about their own oral health.",
        ],
    },

    # Posts list — TOP-LEVEL, sibling to `pubblicazioni`. Same shape
    # the blog_list.html template expects (slug, kicker, title, date,
    # read_min, author, lede).
    "posts": [
        {
            "slug":     "igiene-professionale-perche-semestrale",
            "kicker":   "Hygiene & prevention",
            "title":    "Professional hygiene: why the six-month cadence is a clinical choice",
            "date":     "12 March 2025",
            "read_min": 8,
            "author":   "Dr. Chiara Vespa",
            "lede":
                "The clinical literature supports a personalised "
                "hygiene cadence, but the six-month rule remains the "
                "best compromise between cost, patient adherence and "
                "long-term periodontal outcome.",
        },
        {
            "slug":     "impianti-carico-immediato-quando",
            "kicker":   "Implantology",
            "title":    "Immediate loading in implantology: when it is genuinely indicated",
            "date":     "23 January 2025",
            "read_min": 12,
            "author":   "Dr. Riccardo Berti",
            "lede":
                "Immediate loading is attractive for its shorter "
                "treatment time, but it is not a universal solution. "
                "The patient-selection criteria are strict, and they "
                "deserve to be explained openly before surgery.",
        },
        {
            "slug":     "allineatori-trasparenti-cosa-non-fanno",
            "kicker":   "Orthodontics",
            "title":    "Clear aligners: three things they don't do",
            "date":     "5 November 2024",
            "read_min": 6,
            "author":   "Dr. Sofia Liccardi",
            "lede":
                "They work in most adults, but they don't solve "
                "everything. Three honest clinical limits every "
                "patient should know about before starting a plan.",
        },
        {
            "slug":     "parodontite-non-e-solo-gengivite",
            "kicker":   "Periodontology",
            "title":    "Periodontitis is not just \"bleeding gums\"",
            "date":     "18 September 2024",
            "read_min": 5,
            "author":   "Dr. Andrea Carofiglio",
            "lede":
                "Chronic periodontitis affects one adult in two after "
                "the age of thirty-five, but it is diagnosed late "
                "because the early signs are silent. Three periodontal "
                "indices any patient can ask their dentist about.",
        },
    ],

    # ─── CONTATTI (contact) — contact.html expects blocks 3-tuples,
    # form_title/intro/placeholders/consent, hours 3-tuples, transport
    # 2-tuples.
    "contatti": {
        "eyebrow":  "Contact & location",
        "headline": "Write to us, <em>we'll call you back the same day.</em>",
        "intro":
            "To book a first visit or a maintenance cleaning, call us, "
            "message us on WhatsApp or fill in the form below. We "
            "reply within the same working day.",
        # 4 info-blocks: (label, value, sub) 3-tuples · matches the four
        # SVG icons hard-coded in contact.html (pin · phone · email · clock)
        "blocks": [
            ("Address",
             "Via Manzoni 18\n20121 Milan",
             "Piano nobile · independent entrance"),
            ("Phone",
             "+39 02 7770 4488",
             "Same working day response"),
            ("Email",
             "studio@denticostudio.it",
             "For non-urgent enquiries"),
            ("Hours",
             "Mon – Fri · 8:30 – 19:30\nSat · 9:00 – 13:00",
             "Closed on Sunday"),
        ],
        "form_title": "Write to us, we'll call you back the same day.",
        "form_intro":
            "Form for information requests or to book a first visit. "
            "For clinical emergencies please call us directly.",
        "form_placeholders": {
            "first_name": "Mary",
            "last_name":  "Bennett",
            "email":      "mary.bennett@email.com",
            "phone":      "+39 333 12 34 567",
            "subject":    "First visit / cleaning / emergency",
            "message":    "Please indicate your preferred time slot and any preferred dentist.",
        },
        "form_helpers": {},
        "form_consent":
            "I consent to the processing of my personal data for the "
            "sole purpose of being contacted back by the studio. "
            "GDPR Art. 6 · DPO available at dpo@denticostudio.it.",
        "form_submit_note":
            "Reply within the next working day.",
        "hours_heading":    "Opening hours",
        # 3-tuples (day, am, pm) — matches contact.html line 175
        "hours": [
            ("Monday",    "8:30 – 13:00", "14:00 – 19:30"),
            ("Tuesday",   "8:30 – 13:00", "14:00 – 19:30"),
            ("Wednesday", "8:30 – 13:00", "14:00 – 19:30"),
            ("Thursday",  "8:30 – 13:00", "14:00 – 19:30"),
            ("Friday",    "8:30 – 13:00", "14:00 – 19:30"),
            ("Saturday",  "9:00 – 13:00", "—"),
            ("Sunday",    "—", "Closed"),
        ],
        "transport_heading": "How to reach us",
        # 2-tuples (label, text)
        "transport": [
            ("Underground", "M3 Montenapoleone · 3 minutes on foot"),
            ("Tram",        "Line 1 · Manzoni stop"),
            ("Train",       "Stazione Centrale · 12 minutes on M3"),
            ("Parking",     "Garage in Via Bigli · 50 metres · partner rate"),
        ],
    },

    # ─── RICHIEDI-VISITA (appointment) — needs process steps + flat
    # form_fields (form_sections is optional · the appointment.html
    # falls back to a flat field list at line 173-174 when sections
    # are absent).
    "richiedi-visita": {
        "eyebrow":  "Book a cleaning · first visit",
        "headline": "Book online, <em>we get back to you within 24 hours.</em>",
        "intro":
            "Fill in the form: reception books your first appointment "
            "within the next working day and confirms by SMS or "
            "WhatsApp.",
        "process_label":   "The booking journey",
        "process_heading": "From form to first <em>appointment</em>, in four steps.",
        # 4 process steps (num, title, blurb) — 3-tuples
        "process": [
            ("01", "Form & call-back",
             "Reception receives the form, checks that all the "
             "information we need is there, and calls you back within "
             "the next working day to set the appointment."),
            ("02", "Confirmation & reminder",
             "You'll receive a confirmation by SMS or WhatsApp with "
             "date, time, reference dentist, studio address and "
             "directions."),
            ("03", "Seventy-minute first visit",
             "Medical history, full clinical examination, iTero scan, "
             "intraoral and extraoral photos, periodontal charting, "
             "written care plan delivered as a PDF."),
            ("04", "Written plan",
             "Plan discussed at the chair with an itemised quote. The "
             "cost of the first visit is deducted from the first "
             "treatment in the plan."),
        ],
        "form_title": "Book your first appointment",
        "form_band_side_note":
            "Reply within 24 working hours. For clinical emergencies "
            "please call +39 02 7770 4488 directly.",
        "form_band_side_note_small":
            "Data is used solely to contact you back · GDPR Art. 6.",
        "form_fields": [
            {"name": "first_name", "label": "First name",
             "type": "text",       "required": True,
             "placeholder": "Mary"},
            {"name": "last_name",  "label": "Last name",
             "type": "text",       "required": True,
             "placeholder": "Bennett"},
            {"name": "email",      "label": "Email",
             "type": "email",      "required": True,
             "placeholder": "mary.bennett@email.com"},
            {"name": "phone",      "label": "Phone",
             "type": "tel",        "required": True,
             "placeholder": "+39 333 12 34 567"},
            {"name": "service",    "label": "Treatment requested",
             "type": "select",     "required": True,
             "options": [
                 "Professional cleaning",
                 "First visit (chart + plan)",
                 "Dental emergency",
                 "Implantology consultation",
                 "Orthodontic consultation",
                 "Other",
             ]},
            {"name": "preferred",  "label": "Preferred time slot",
             "type": "select",     "required": False,
             "options": [
                 "Morning (8:30 – 13:00)",
                 "Afternoon (14:00 – 19:30)",
                 "Saturday morning",
                 "No preference",
             ]},
            {"name": "notes",      "label": "Notes (optional)",
             "type": "textarea",   "required": False,
             "full_width": True,
             "placeholder": "Please mention any drug allergies, previous tests or preferred dentist."},
        ],
        "submit_label": "Book appointment",
        "consent":
            "I consent to the processing of my personal data for the "
            "sole purpose of being contacted back by the studio. "
            "GDPR Art. 6 · DPO available at dpo@denticostudio.it.",
        "footnote":
            "Data is used solely to contact you back about this "
            "request. GDPR Art. 6 compliant · DPO available at "
            "dpo@denticostudio.it.",
    },
}
