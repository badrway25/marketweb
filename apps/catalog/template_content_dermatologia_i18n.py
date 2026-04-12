"""Dermatologia Elite i18n — EN / FR / ES / AR content blocks.

Session 24, Phase 2i.2. This file isolates the non-IT locale trees for
`dermatologia-elite-roma` so the main `template_content.py` stays
readable. The IT block is the authoritative source and remains inline
in `template_content.py` (keyed as `DERMATOLOGIA_CONTENT_IT`).

Authoring rules
---------------
- Locale-specific editorial voice — NOT literal word-for-word translation
  of the Italian copy. Dermatology discourse shifts per market:
  - EN: precise Anglo-American clinical language, authoritative but warm,
    British Journal of Dermatology register.
  - FR: classical French dermatological prose, "vous" register, refined
    and analytical — Annales de Dermatologie et de Vénéréologie tone.
  - ES: Spanish peninsular register, elegant yet accessible, warm
    precision — "usted" for clinical context.
  - AR: Modern Standard Arabic, formal medical register, RTL-aware
    punctuation (Arabic comma ، and question mark ؟ where appropriate).
- Non-localizable data (phone, email, address, years, prices, doctor
  portrait URLs, press outlets) is repeated as-is across locales.
  A Roma clinic's address is "Via Veneto 116" in every language.
- The `pages` list preserves the same slugs + kinds across locales —
  only the labels are translated.
- Doctor names, dates, and press outlets stay in the original script.
  Arabic renders them as-is (mixed-script is handled by the RTL shell).
- Quality floor: no machine translation, no placeholder strings, no
  half-sentences. Every section must read as if authored by a native
  speaker working for a premium dermatology practice in Rome.
- IDENTITY: Dermatologia is NOT Cardio. The editorial voice centers on
  skin health, visual precision, dermatoscopic archives, surgical
  dermatology, aesthetic-clinical duality. Avoid borrowing phrases,
  rhythms, or structural echoes from the Cardio content trees.
"""
from __future__ import annotations

from typing import Any


# Shared non-localizable assets — repeated verbatim per locale block so
# each content tree stays flat (no shared refs = no shared-reference bugs).
_CHIEF_PORTRAIT = (
    "https://images.unsplash.com/photo-1594824476967-48c8b964273f"
    "?auto=format&fit=crop&w=900&q=80"
)
_DR_VITALI_PORTRAIT = (
    "https://images.unsplash.com/photo-1582750433449-648ed127bb54"
    "?auto=format&fit=crop&w=900&q=80"
)
_DR_MORELLI_PORTRAIT = (
    "https://images.unsplash.com/photo-1666214280557-f1b5022eb634"
    "?auto=format&fit=crop&w=900&q=80"
)
_LEAD_IMAGE = (
    "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d"
    "?auto=format&fit=crop&w=900&q=80"
)


# ===========================================================================
# ENGLISH
# ===========================================================================

DERMATOLOGIA_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Practice",        "kind": "home"},
        {"slug": "studio",          "label": "The Practice",    "kind": "about"},
        {"slug": "visite",          "label": "Treatments",      "kind": "services"},
        {"slug": "medici",          "label": "Physicians",      "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Publications",    "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contact",         "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Request a visit", "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "R",
        "logo_word":    "Studio Ricciardi",
        "tag":          "Clinical, surgical & aesthetic dermatology · Rome Via Veneto",
        "phone":        "+39 06 487 2311",
        "email":        "studio@ricciardidermatologia.it",
        "address":      "Via Veneto 116 · 00187 Rome",
        "hours_compact": "Mon – Fri · 10:00 – 20:00",
        "hours_footer_rows": [
            "Saturday · surgery by appointment",
            "Sunday · closed",
        ],
        "license":      "Rome Medical Board reg. 3 / 11982",
        "footer_intro":
            "A private specialist practice in clinical, surgical and aesthetic "
            "dermatology. By appointment only.",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "hero_variant": "editorial-magazine",
        "eyebrow":  "Clinical dermatology · Rome Via Veneto",
        "headline": "The skin is an <em>identity document</em>. We read it in full.",
        "intro":
            "Clinical, surgical and aesthetic dermatology under one roof on "
            "Via Veneto. Digital mole mapping, early skin-cancer detection, "
            "day-surgery excisions and physician-led aesthetic treatments.",
        "primary_cta":   "Book a first visit",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "Discover the practice",
        "secondary_href":"studio",

        "facts": [
            ("18",    "years of private dermatology practice"),
            ("2,400", "mole mappings per year"),
            ("3",     "dedicated rooms · 1 surgical suite"),
        ],

        "manifesto_drop_cap": "E",
        "manifesto":
            "very skin tells a story written by environment, time, genes "
            "and habits. The dermatologist is the reader of that story — "
            "with the dermatoscope, with trained hands, with the clinical "
            "eye of someone who has examined tens of thousands of patients "
            "before you. At Studio Ricciardi, we never rush a consultation.",

        "signature_visits": [
            ("01", "Digital mole mapping",
             "High-resolution videodermatoscopy of every mole, digital "
             "archiving and comparison with the patient's historical "
             "record. Report delivered same day."),
            ("02", "Dermatological day-surgery",
             "Excision of suspicious lesions under local anaesthesia with "
             "dedicated histopathological analysis. Minor reconstructive "
             "plastic surgery included in the pathway."),
            ("03", "Dermatological laser",
             "Fractional CO2 laser, vascular laser and next-generation "
             "depilation laser for scars, vascular lesions and "
             "non-invasive cutaneous surgery."),
            ("04", "Aesthetic dermatology",
             "Fillers, botulinum toxin, medical peels and skin boosters "
             "performed personally by the dermatologist. Never delegated "
             "to non-physician staff."),
        ],

        "chief": {
            "name":  "Dr. Alessandra Ricciardi",
            "role":  "Clinical director · Dermatologist",
            "bio":
                "Board-certified in dermatology and venereology at the "
                "Università Cattolica del Sacro Cuore in Rome, advanced "
                "fellowship in dermoscopy at Memorial Sloan Kettering in "
                "New York and in dermatological surgery at the Charité in "
                "Berlin. Member of SIDeMaST, EADV and the International "
                "Dermoscopy Society. Author of over fifty indexed publications.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "press": ["JAMA Dermatology", "British Journal of Dermatology",
                  "Vanity Fair Wellness", "Corriere Salute", "Vogue Italia"],
        "press_label": "Published in",

        "hero_sidebar_top_label": "Clinical direction",
        "hero_sidebar_quote":
            "\u201cThe skin is not a symptom to be silenced. "
            "It is a tissue that speaks \u2014 you just need to learn to listen.\u201d",
        "hero_sidebar_author": "\u2014 JAMA Dermatology \u00b7 2025",
        "hero_sidebar_pulse": [
            ("Practice", "Rome \u00b7 Via Veneto"),
            ("Since",    "2008"),
            ("Focus",    "Integrated dermatology"),
        ],

        "signature_visits_label":   "Treatments & pathways",
        "signature_visits_heading": "Four clinical areas, <em>a single archive.</em>",
        "signature_visits_intro":
            "The four areas in which we work every day. "
            "The full list of pathways is on the Treatments page.",

        "chief_label":   "Clinical direction",
        "chief_heading": "One archive <em>for every skin.</em>",

        "credentials": {
            "label": "Accreditations & certifications",
            "items": [
                ("FotoFinder", "Certified centre of reference for FotoFinder Systems digital dermoscopy", "since 2012"),
                ("SIDeMaST", "Italian Society of Medical, Surgical, Aesthetic Dermatology and STDs — active member", ""),
                ("EADV", "European Academy of Dermatology and Venereology — full member", ""),
                ("IDS", "International Dermoscopy Society — Advanced Certified Dermoscopist", "since 2015"),
            ],
        },

        "cta_heading":
            "A pathway that begins <em>with the first visit.</em>",
        "cta_primary_label":   "Book a first visit",
        "cta_secondary_label": "Directions & contact",
    },

    # ─── THE PRACTICE (about) ───���─────────────────────────────
    "studio": {
        "eyebrow":  "The practice",
        "headline": "Eighteen years of <em>integrated private dermatology</em>.",
        "intro":
            "Studio Ricciardi was founded in 2008 on the principle that modern "
            "dermatology cannot survive on check-ups alone: it requires clinical "
            "time, dedicated surgery and an aesthetic office that speaks the "
            "same language as diagnosis.",

        "history": [
            ("2008",
             "Opening of the first premises at Via Veneto 116 \u2014 three rooms "
             "and one secretary. The first dermatological consultation was "
             "delivered on 4 February 2008."),
            ("2012",
             "Installation of the FotoFinder ATBM digital videodermatoscope "
             "\u2014 the first in a private Roman practice. Mole mappings shift "
             "from paper to an incremental digital archive, comparable "
             "year on year on the same machine."),
            ("2015",
             "Outfitting of the dedicated ambulatory surgical suite, with an "
             "external anaesthetist for complex procedures. The day-surgery "
             "dermatological service is born."),
            ("2019",
             "Arrival of the Lumenis UltraPulse fractional CO2 laser and the "
             "Candela Vbeam Prima vascular laser. The dermatological laser "
             "area launches, with protocols for scars, actinic keratoses and "
             "vascular lesions."),
            ("2024",
             "Dr. Morelli joins as head of the aesthetic dermatology pathway. "
             "For the first time, aesthetic medicine in the practice is "
             "led full-time by a board-certified dermatologist."),
        ],

        "method_title": "Method",
        "method_paragraphs": [
            "A consultation at Studio Ricciardi always begins with a simple "
            "question: when did you first notice it? That date is our true "
            "starting point. Skin lesions are not read in section alone: "
            "they are read across time, comparing photographs, reports and "
            "the patient\u2019s own observations.",
            "For every patient we build a digital dermatoscopic archive that "
            "accompanies the person for life: from the first teenage visit "
            "to the check-ups of maturity. Every mole is photographed, "
            "catalogued and compared at every subsequent appointment. It is "
            "the change, not the isolated image, that generates clinical "
            "suspicion.",
            "Dermatological surgery, when indicated, is performed the same "
            "day under local anaesthesia by the physician who raised the "
            "indication. The histological specimen is entrusted to a "
            "laboratory specialising in dermatopathology, with whom we "
            "maintain a direct telephone dialogue for the most complex cases.",
        ],

        "values": [
            ("Precision",      "Digital videodermatoscopy for every patient, at every check-up."),
            ("Prevention",     "Annual mole mapping entered by default in the schedule from the second year."),
            ("Traceability",   "A permanent photographic archive, available to the patient at any time."),
            ("Clinical aesthetics", "No aesthetic treatment without a prior dermatological consultation."),
        ],

        "values_label":   "What we guarantee",
        "values_heading": "Four commitments that <em>never change.</em>",

        "cta_heading":
            "Would you like to meet the dermatologists <em>before booking?</em>",
        "cta_primary_label":   "The three dermatologists \u2192",
        "cta_secondary_label": "Request a private visit \u2192",
    },

    # ─── TREATMENTS (services) ────────────────────────────────
    "visite": {
        "eyebrow":  "Treatments",
        "headline": "Six clinical pathways, <em>a single file.</em>",
        "intro":
            "Every consultation at Studio Ricciardi follows a defined clinical "
            "pathway, with a written duration, price and follow-up plan. "
            "No hidden fees, no verbal estimates.",

        "treatments": [
            ("Full dermatological consultation",
             "40 min \u00b7 first visit",
             "Extended history-taking, full-body skin examination (including "
             "scalp, oral cavity and genital area), manual dermatoscopy, "
             "personal reporting and a written follow-up plan.",
             "\u20ac 180"),
            ("Digital mole mapping",
             "60 min \u00b7 FotoFinder ATBM",
             "High-resolution videodermatoscopy of every mole, digital "
             "archiving, comparison with the historical record, written "
             "report detailing at-risk lesions.",
             "\u20ac 240"),
            ("Ambulatory dermatological surgery",
             "On indication \u00b7 day-surgery",
             "Excision of suspicious lesions under local anaesthesia, "
             "histopathological examination by a specialist dermatopathology "
             "laboratory, report within eight working days with a dedicated "
             "telephone consultation.",
             "from \u20ac 320"),
            ("Fractional CO2 laser",
             "45 min \u00b7 single session",
             "Treatment of scars, perioral wrinkles, sun spots and actinic "
             "keratoses with the Lumenis UltraPulse system. First session "
             "always preceded by a dedicated dermatological consultation.",
             "\u20ac 420"),
            ("Medical dermatological peel",
             "30 min \u00b7 4-session course",
             "Superficial and medium peels (TCA, mandelic, salicylic, dilute "
             "phenol) performed personally by the dermatologist, with a "
             "protocol tailored to skin type and actinic damage.",
             "\u20ac 260 / session"),
            ("Annual prevention pathway",
             "Annual \u00b7 3 appointments",
             "Full dermatological consultation, digital mole mapping with "
             "historical comparison, personalised photoprotection advice, "
             "direct line to the physician for minor concerns during the year.",
             "\u20ac 580"),
        ],

        "footnote":
            "All payments are tax-deductible as healthcare expenses. The "
            "practice issues a healthcare receipt with a revenue stamp. "
            "Surgical estimates are always written and signed by the "
            "physician in advance, inclusive of histological examinations "
            "and follow-up visits.",
        "footnote_heading": "Administrative notes",

        "cta_heading":
            "A consultation at Studio Ricciardi is <em>personally prepared</em>.",
        "cta_primary_label":   "Request form \u2192",
        "cta_secondary_label": "Front-desk direct number \u2192",
    },

    # ──�� PHYSICIANS (team) ─────���──────────────────────────────
    "medici": {
        "eyebrow":  "The physicians",
        "headline": "Three signatures, a single <em>surgical suite.</em>",
        "intro":
            "The practice comprises three dermatologists who share records, "
            "the dermatoscopic archive and clinical protocols. Every patient, "
            "however, always has one referring dermatologist.",

        "portrait_city": "Rome \u00b7 Via Veneto",

        "doctors": [
            {
                "name":  "Dr. Alessandra Ricciardi",
                "role":  "Clinical director \u00b7 Dermatologist",
                "tags":  ["Advanced dermoscopy", "Skin cancer", "Clinical dermatology"],
                "bio":
                    "Board-certified in dermatology and venereology at the "
                    "Universit\u00e0 Cattolica del Sacro Cuore in Rome, advanced "
                    "dermoscopy fellowship at Memorial Sloan Kettering in New "
                    "York. Member of SIDeMaST, EADV and the International "
                    "Dermoscopy Society. Author of over fifty indexed "
                    "publications, including two chapters of the Bolognia-Italia "
                    "dermatology textbook.",
                "portrait": _CHIEF_PORTRAIT,
                "links": [("PubMed", "#"), ("ORCID", "#")],
            },
            {
                "name":  "Dr. Emanuele Vitali",
                "role":  "Dermatologist \u00b7 Dermatological surgery",
                "tags":  ["Ambulatory surgery", "Reconstructive plastics", "Dermatopathology"],
                "bio":
                    "Trained at the Policlinico Gemelli in Rome, advanced "
                    "fellowship in dermatological surgery at the Charit\u00e9 in "
                    "Berlin. Since 2015, head of the practice\u2019s ambulatory "
                    "surgical suite. Surgical consultant for two university "
                    "dermatology departments in Rome.",
                "portrait": _DR_VITALI_PORTRAIT,
                "links": [("Curriculum", "#")],
            },
            {
                "name":  "Dr. Caterina Morelli",
                "role":  "Dermatologist \u00b7 Aesthetics & Laser",
                "tags":  ["CO2 laser", "Aesthetic medicine", "Medical peels"],
                "bio":
                    "Trained at the University of Padua, PhD in aesthetic "
                    "dermatology. Advanced fellowship in laser therapy at the "
                    "Wellman Center in Boston. Since 2024, head of the "
                    "aesthetic dermatology pathway at Studio Ricciardi. "
                    "No delegation to non-physician staff.",
                "portrait": _DR_MORELLI_PORTRAIT,
                "links": [("Publications", "#")],
            },
        ],
    },

    # ─── PUBLICATIONS (blog list / detail) ────────────────────
    "pubblicazioni": {
        "eyebrow":  "Publications & insights",
        "headline": "Scientific work, <em>critical readings</em>, dermatological writing.",
        "intro":
            "A selection of the practice\u2019s publications and of the educational "
            "pieces written for the general public. Every text is personally "
            "reviewed by Dr. Ricciardi before publication.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Studio Ricciardi \u00b7 Integrated dermatology",
        "empty_body_fallback_paragraphs": [
            "Article in editorial preparation. The full text will be "
            "available shortly.",
            "This placeholder describes the article\u2019s voice: a clinical "
            "note written by the dermatologist, in a direct and jargon-free "
            "tone, aimed at patients and families seeking reliable information.",
        ],
    },

    "posts": [
        {
            "slug":     "mappatura-nei-quando-farla",
            "kicker":   "Prevention",
            "title":    "Mole mapping: how often should you really have it done",
            "date":     "18 March 2026",
            "read_min": 7,
            "author":   "Dr. Alessandra Ricciardi",
            "lede":
                "The most frequently asked question in the consulting room "
                "is also the one with the most nuanced answer. There is no "
                "universal frequency: there is your skin type, your archive "
                "and your family history.",
            "body": [
                ("p", "Every year in Italy, roughly fifteen thousand new cases of "
                      "cutaneous melanoma are diagnosed. It is the skin cancer with "
                      "the highest lethality and, at the same time, the one with the "
                      "best prognosis when caught early. The boundary between these "
                      "two realities is called serial digital dermoscopy."),
                ("h2", "Three risk categories"),
                ("ol", [
                    "Patient without family history, few moles (under 30), skin type II\u2013III: mapping every 24 months.",
                    "Patient with many moles (over 50), fair skin type or childhood sunburns: annual mapping.",
                    "Patient with first-degree family history of melanoma or a flagged mole in the archive: mapping every six to twelve months.",
                ]),
                ("p", "These intervals are not rigid rules: every dermatologist "
                      "adjusts them to the individual patient. What matters is "
                      "that the mapping is not an isolated procedure but a clinical "
                      "act repeated over time \u2014 with the same machines, the same "
                      "physician and the same digital archive."),
                ("h2", "What \u2018digital archive\u2019 means"),
                ("p", "It means every mole is photographed under high-resolution "
                      "videodermatoscopy and stored with precise skin coordinates. "
                      "At every subsequent check-up, the physician does not look at "
                      "a new mole: they compare the same photograph with last year\u2019s. "
                      "It is the change, not the isolated image, that generates "
                      "clinical suspicion."),
                ("blockquote",
                 "Mole mapping does not aim to find a melanoma. It aims to know, "
                 "for every lesion, what it looked like last year. It is an act "
                 "of clinical memory, before it is an act of diagnosis."),
                ("p", "For new patients, the first mapping is always a founding "
                      "act: today\u2019s photographs become the benchmark for the next "
                      "ten years. It is worth dedicating a full hour of clinical "
                      "time, and half the first consultation is devoted to it."),
            ],
        },
        {
            "slug":     "chirurgia-dermatologica-ambulatoriale",
            "kicker":   "Dermatological surgery",
            "title":    "Day-surgery dermatological excision: what to actually expect",
            "date":     "2 March 2026",
            "read_min": 5,
            "author":   "Dr. Emanuele Vitali",
            "lede":
                "Ambulatory dermatological excisions are frightening only until "
                "the anaesthesia takes effect. Afterwards, in 95% of cases, the "
                "patient leaves the practice walking exactly as they came in.",
        },
        {
            "slug":     "laser-co2-cicatrici",
            "kicker":   "Dermatological laser",
            "title":    "Fractional CO2 laser: when it is the right choice for scars",
            "date":     "15 February 2026",
            "read_min": 6,
            "author":   "Dr. Caterina Morelli",
            "lede":
                "The fractional CO2 laser does not erase scars: it remodels "
                "them. Understanding this distinction is the first step towards "
                "a realistic choice, free of unattainable expectations.",
        },
        {
            "slug":     "fotoprotezione-quotidiana",
            "kicker":   "Prevention",
            "title":    "Daily photoprotection: the three rules that truly matter",
            "date":     "28 January 2026",
            "read_min": 4,
            "author":   "Dr. Alessandra Ricciardi",
            "lede":
                "An SPF 50 applied in the wrong amount is worth an SPF 15 "
                "applied properly. After fifteen thousand dermatological "
                "consultations, 80% of patients always make the same mistake.",
        },
        {
            "slug":     "medicina-estetica-dermatologica",
            "kicker":   "Clinical aesthetics",
            "title":    "Why at Studio Ricciardi aesthetic medicine is performed only by the dermatologist",
            "date":     "10 January 2026",
            "read_min": 5,
            "author":   "Dr. Caterina Morelli",
            "lede":
                "Aesthetic dermatological medicine is not a task to be "
                "delegated. A firm stance that we explain to patients "
                "at the very first visit, without mincing words.",
        },
    ],

    # ─── CONTACT ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contact",
        "headline": "One front desk, <em>one person</em> at the other end of the line.",
        "intro":
            "The practice answers telephone calls in person Monday to Friday. "
            "The clinical secretary is Mrs Bianca Martelli, who has known every "
            "chart and every patient by name for over ten years.",

        "blocks": [
            ("Address",   "Via Veneto 116", "00187 Rome \u00b7 unit 3, staircase A"),
            ("Phone",     "+39 06 487 2311",   "Direct answer 10:00 \u2013 20:00"),
            ("Email",     "studio@ricciardidermatologia.it", "Reply within 24 working hours"),
            ("Emergencies", "+39 339 221 7080", "Line reserved for existing patients"),
        ],

        "hours": [
            ("Monday",    "10:00 \u2013 14:00", "15:30 \u2013 20:00"),
            ("Tuesday",   "10:00 \u2013 14:00", "15:30 \u2013 20:00"),
            ("Wednesday", "10:00 \u2013 14:00", "15:30 \u2013 20:00"),
            ("Thursday",  "10:00 \u2013 14:00", "15:30 \u2013 20:00"),
            ("Friday",    "10:00 \u2013 14:00", "15:30 \u2013 19:00"),
            ("Saturday",  "Surgery by appointment", "Scheduled procedures only"),
            ("Sunday",    "Closed", "\u2014"),
        ],

        "transport": [
            ("Metro",  "Line A \u00b7 Barberini station, 7 minutes on foot"),
            ("Car",    "Saba Ludovisi car park (agreement), entrance from Via Sicilia"),
            ("Train",  "Roma Termini station \u00b7 11 minutes by taxi"),
        ],

        "form_title": "Write to the practice",
        "form_intro":
            "For non-urgent enquiries \u2014 treatment information, prices, "
            "preparation for mole mapping \u2014 write to us below. The clinical "
            "secretary replies personally.",

        "hours_heading":     "Opening hours",
        "transport_heading": "How to reach us",

        "form_placeholders": {
            "first_name": "Maria",
            "last_name":  "Bianchi",
            "email":      "maria.bianchi@email.it",
            "phone":      "+39 335 ...",
            "subject":    "Information about the first dermatological consultation",
            "message":
                "Keep it brief \u2014 the secretary will get back to you "
                "within 24 working hours.",
        },
    },

    # ─── APPOINTMENT ──────��───────────────────────────────────
    "richiedi-visita": {
        "eyebrow":  "Dermatological visit request",
        "headline": "A dermatological consultation <em>is not booked</em>: it is prepared.",
        "intro":
            "There is no online calendar. The practice reserves every first "
            "visit after reading a brief description of the case. Requests "
            "are reviewed personally by the physician within 48 working hours.",

        "process_label":   "How it works",
        "process_heading":
            "Four steps, in <em>forty-eight working hours.</em>",

        "process": [
            ("01", "Fill in the form",
             "Ten lines are enough to outline your request. If you have "
             "suspicious lesions, attach a photograph: it helps prioritise "
             "the case in advance."),
            ("02", "Clinical reading",
             "The physician personally reads the request within 48 working "
             "hours and determines whether the first visit is clinical, "
             "surgical or aesthetic dermatology."),
            ("03", "Appointment proposal",
             "The secretary proposes two time slots compatible with your "
             "schedule and with the visit duration (40 min for a general "
             "consultation, 60 min for a complete mole mapping)."),
            ("04", "Confirmation & preparation",
             "You receive by email a list of what to bring (previous exams, "
             "lesion photographs, current therapy) and practical instructions "
             "for the visit \u2014 make-up free and no nail polish if a "
             "mapping is planned."),
        ],

        "form_title": "Request form",
        "form_band_side_note":
            "Allow yourself a few minutes. Carefully prepared requests are "
            "read by the dermatologist in full \u2014 hasty ones are not.",
        "form_band_side_note_small": "\u2193 Reserved form",

        "form_fields": [
            {"label": "Full name", "placeholder": "Maria Bianchi",
             "type": "text", "full_width": False},
            {"label": "Email", "placeholder": "maria@email.it",
             "type": "email", "full_width": False},
            {"label": "Phone", "placeholder": "+39 335 ...",
             "type": "tel", "full_width": False},
            {"label": "Age", "placeholder": "38",
             "type": "number", "full_width": False},
            {"label": "Visit type", "type": "select", "full_width": False,
             "options": ["Dermatological consultation", "Mole mapping",
                         "Dermatological surgery", "Aesthetic medicine"]},
            {"label": "Preferred availability", "type": "select", "full_width": False,
             "options": ["Morning", "Afternoon", "No preference"]},
            {"label": "Referring physician", "placeholder": "Dr. ...",
             "type": "text", "full_width": True},
            {"label": "Brief case description",
             "placeholder":
                 "Reason for the visit, lesions of interest, recent "
                 "symptoms, current treatments. Keep to ten lines.",
             "type": "textarea", "full_width": True},
        ],

        "submit_label": "Submit request",

        "consent":
            "I consent to the processing of personal data under the privacy "
            "notice pursuant to EU Regulation 679/2016. Clinical data and "
            "dermatoscopic photographs are stored in an encrypted digital "
            "archive accessible only to the treating physician.",

        "footnote":
            "The practice does not respond to anonymous requests and does "
            "not issue clinical opinions by email without a consultation. "
            "For administrative queries (prices, hours, parking) please "
            "use the contact page.",
    },
}


# ===========================================================================
# FRENCH
# ===========================================================================

DERMATOLOGIA_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Cabinet",          "kind": "home"},
        {"slug": "studio",          "label": "Le Cabinet",       "kind": "about"},
        {"slug": "visite",          "label": "Consultations",    "kind": "services"},
        {"slug": "medici",          "label": "M\u00e9decins",    "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Publications",     "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contact",          "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Demander un RDV",  "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "R",
        "logo_word":    "Studio Ricciardi",
        "tag":          "Dermatologie clinique, chirurgicale et esth\u00e9tique \u00b7 Rome Via Veneto",
        "phone":        "+39 06 487 2311",
        "email":        "studio@ricciardidermatologia.it",
        "address":      "Via Veneto 116 \u00b7 00187 Rome",
        "hours_compact": "Lun \u2013 Ven \u00b7 10 h 00 \u2013 20 h 00",
        "hours_footer_rows": [
            "Samedi \u00b7 chirurgie sur rendez-vous",
            "Dimanche \u00b7 ferm\u00e9",
        ],
        "license":      "Ordre des m\u00e9decins de Rome n\u00b0 3 / 11982",
        "footer_intro":
            "Cabinet priv\u00e9 de dermatologie clinique, chirurgicale et "
            "esth\u00e9tique. Sur rendez-vous uniquement.",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "hero_variant": "editorial-magazine",
        "eyebrow":  "Dermatologie clinique \u00b7 Rome Via Veneto",
        "headline": "La peau est une <em>carte d\u2019identit\u00e9</em>. Nous la lisons int\u00e9gralement.",
        "intro":
            "Dermatologie clinique, chirurgicale et esth\u00e9tique r\u00e9unies "
            "dans un seul cabinet priv\u00e9 sur la Via Veneto. Cartographie "
            "num\u00e9rique des n\u00e6vi, d\u00e9tection pr\u00e9coce des cancers cutan\u00e9s, "
            "chirurgie dermatologique en ambulatoire et m\u00e9decine esth\u00e9tique "
            "ex\u00e9cut\u00e9e par le dermatologue.",
        "primary_cta":   "R\u00e9server une premi\u00e8re visite",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "D\u00e9couvrir le cabinet",
        "secondary_href":"studio",

        "facts": [
            ("18",    "ann\u00e9es de dermatologie priv\u00e9e"),
            ("2 400", "cartographies de n\u00e6vi par an"),
            ("3",     "salles d\u00e9di\u00e9es \u00b7 1 bloc op\u00e9ratoire"),
        ],

        "manifesto_drop_cap": "C",
        "manifesto":
            "haque peau raconte une histoire \u00e9crite par l\u2019environnement, le "
            "temps, les g\u00e8nes et les habitudes. Le dermatologue en est le "
            "lecteur \u2014 au dermatoscope, \u00e0 main nue, avec l\u2019\u0153il clinique "
            "de celui qui a examin\u00e9 des dizaines de milliers de patients "
            "avant vous. Au Studio Ricciardi, aucune consultation n\u2019est "
            "jamais \u00e9court\u00e9e.",

        "signature_visits": [
            ("01", "Cartographie num\u00e9rique des n\u00e6vi",
             "Vid\u00e9odermatoscopie haute r\u00e9solution de chaque n\u00e6vus, archivage "
             "num\u00e9rique et comparaison avec l\u2019historique du patient. Compte "
             "rendu d\u00e9livr\u00e9 le jour m\u00eame."),
            ("02", "Chirurgie dermatologique ambulatoire",
             "Ex\u00e9r\u00e8se des l\u00e9sions suspectes sous anesth\u00e9sie locale avec "
             "analyse histopathologique d\u00e9di\u00e9e. Petite chirurgie plastique "
             "reconstructrice incluse dans le parcours."),
            ("03", "Laser dermatologique",
             "Laser CO2 fractionn\u00e9, laser vasculaire et laser d\u2019\u00e9pilation "
             "de derni\u00e8re g\u00e9n\u00e9ration pour cicatrices, l\u00e9sions vasculaires "
             "et chirurgie cutan\u00e9e non invasive."),
            ("04", "Dermatologie esth\u00e9tique",
             "Acide hyaluronique, toxine botulique, peelings m\u00e9dicaux et "
             "skinboosters pratiqu\u00e9s personnellement par le dermatologue. "
             "Jamais d\u00e9l\u00e9gu\u00e9s au personnel non m\u00e9dical."),
        ],

        "chief": {
            "name":  "Dr Alessandra Ricciardi",
            "role":  "Directrice clinique \u00b7 Dermatologue",
            "bio":
                "Sp\u00e9cialiste en dermatologie et v\u00e9n\u00e9r\u00e9ologie \u00e0 l\u2019Universit\u00e0 "
                "Cattolica del Sacro Cuore de Rome, perfectionn\u00e9e en "
                "dermoscopie avanc\u00e9e au Memorial Sloan Kettering de New York "
                "et en chirurgie dermatologique \u00e0 la Charit\u00e9 de Berlin. "
                "Membre de la SIDeMaST, de l\u2019EADV et de l\u2019International "
                "Dermoscopy Society. Autrice de plus de cinquante publications "
                "index\u00e9es.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "press": ["JAMA Dermatology", "British Journal of Dermatology",
                  "Vanity Fair Wellness", "Corriere Salute", "Vogue Italia"],
        "press_label": "Publi\u00e9 dans",

        "hero_sidebar_top_label": "Direction clinique",
        "hero_sidebar_quote":
            "\u00ab\u202fLa peau n\u2019est pas un sympt\u00f4me \u00e0 faire taire. "
            "C\u2019est un tissu qui parle \u2014 il suffit d\u2019apprendre \u00e0 l\u2019\u00e9couter.\u202f\u00bb",
        "hero_sidebar_author": "\u2014 JAMA Dermatology \u00b7 2025",
        "hero_sidebar_pulse": [
            ("Cabinet",    "Rome \u00b7 Via Veneto"),
            ("Depuis",     "2008"),
            ("R\u00e9f\u00e9rence", "Dermatologie int\u00e9gr\u00e9e"),
        ],

        "signature_visits_label":   "Consultations et parcours",
        "signature_visits_heading": "Quatre domaines cliniques, <em>un seul dossier.</em>",
        "signature_visits_intro":
            "Les quatre domaines dans lesquels nous travaillons au quotidien. "
            "La liste compl\u00e8te des parcours se trouve sur la page Consultations.",

        "chief_label":   "Direction clinique",
        "chief_heading": "Un seul dossier <em>pour chaque peau.</em>",

        "credentials": {
            "label": "Accr\u00e9ditations et certifications",
            "items": [
                ("FotoFinder", "Centre certifi\u00e9 de r\u00e9f\u00e9rence pour la dermoscopie num\u00e9rique FotoFinder Systems", "depuis 2012"),
                ("SIDeMaST", "Soci\u00e9t\u00e9 italienne de dermatologie m\u00e9dicale, chirurgicale, esth\u00e9tique et des MST \u2014 membre actif", ""),
                ("EADV", "European Academy of Dermatology and Venereology \u2014 full member", ""),
                ("IDS", "International Dermoscopy Society \u2014 Advanced Certified Dermoscopist", "depuis 2015"),
            ],
        },

        "cta_heading":
            "Un parcours qui commence <em>d\u00e8s la premi\u00e8re visite.</em>",
        "cta_primary_label":   "R\u00e9server une premi\u00e8re visite",
        "cta_secondary_label": "Acc\u00e8s et coordonn\u00e9es",
    },

    # ──��� LE CABINET (about) ─────────���─────────────────────────
    "studio": {
        "eyebrow":  "Le cabinet",
        "headline": "Dix-huit ans de <em>dermatologie priv\u00e9e int\u00e9gr\u00e9e</em>.",
        "intro":
            "Le Studio Ricciardi est n\u00e9 en 2008 de la conviction que la "
            "dermatologie contemporaine ne peut se limiter aux consultations de "
            "contr\u00f4le\u202f: elle exige du temps clinique, une chirurgie d\u00e9di\u00e9e et un "
            "cabinet esth\u00e9tique qui parle la m\u00eame langue que le diagnostic.",

        "history": [
            ("2008",
             "Ouverture du premier cabinet au 116 Via Veneto\u202f: trois pi\u00e8ces et "
             "une secr\u00e9taire. La premi\u00e8re consultation dermatologique est "
             "d\u00e9livr\u00e9e le 4 f\u00e9vrier 2008."),
            ("2012",
             "Installation du vid\u00e9odermatoscope num\u00e9rique FotoFinder ATBM, "
             "premier en cabinet priv\u00e9 romain. Les cartographies passent "
             "du papier \u00e0 un archivage num\u00e9rique incr\u00e9mental, comparables "
             "d\u2019ann\u00e9e en ann\u00e9e sur la m\u00eame machine."),
            ("2015",
             "Am\u00e9nagement du bloc chirurgical ambulatoire d\u00e9di\u00e9, avec un "
             "anesth\u00e9siste externe pour les interventions complexes. Na\u00eet "
             "le service de chirurgie dermatologique en ambulatoire."),
            ("2019",
             "Acquisition du laser CO2 fractionn\u00e9 Lumenis UltraPulse et du "
             "laser vasculaire Candela Vbeam Prima. L\u2019espace laser "
             "dermatologique est inaugur\u00e9, avec des protocoles pour "
             "cicatrices, k\u00e9ratoses actiniques et l\u00e9sions vasculaires."),
            ("2024",
             "Arriv\u00e9e du Dr Morelli en tant que responsable du parcours de "
             "m\u00e9decine esth\u00e9tique dermatologique. L\u2019esth\u00e9tique b\u00e9n\u00e9ficie, "
             "pour la premi\u00e8re fois dans le cabinet, d\u2019un dermatologue "
             "\u00e0 temps plein."),
        ],

        "method_title": "M\u00e9thode",
        "method_paragraphs": [
            "Une consultation au Studio Ricciardi commence toujours par une "
            "question simple\u202f: quand l\u2019avez-vous remarqu\u00e9 pour la premi\u00e8re "
            "fois\u202f? Cette date est notre v\u00e9ritable point de d\u00e9part. Les "
            "l\u00e9sions cutan\u00e9es ne se lisent pas seulement en coupe\u202f: elles se "
            "lisent dans le temps, en comparant photographies, comptes rendus "
            "et ressentis du patient.",
            "Pour chaque patient, nous constituons un dossier dermatoscopique "
            "num\u00e9rique qui accompagne la personne toute sa vie\u202f: du premier "
            "contr\u00f4le \u00e0 l\u2019adolescence jusqu\u2019aux bilans de la maturit\u00e9. Chaque "
            "n\u00e6vus est photographi\u00e9, catalogu\u00e9 et compar\u00e9 \u00e0 chaque contr\u00f4le "
            "suivant. C\u2019est le changement, et non l\u2019image isol\u00e9e, qui "
            "g\u00e9n\u00e8re la suspicion clinique.",
            "La chirurgie dermatologique, lorsqu\u2019elle est indiqu\u00e9e, est "
            "pratiqu\u00e9e le jour m\u00eame, sous anesth\u00e9sie locale, par le "
            "m\u00e9decin qui a pos\u00e9 l\u2019indication. La pi\u00e8ce histologique est "
            "confi\u00e9e \u00e0 un laboratoire sp\u00e9cialis\u00e9 en dermatopathologie, avec "
            "lequel nous entretenons un dialogue t\u00e9l\u00e9phonique direct pour "
            "les cas les plus complexes.",
        ],

        "values": [
            ("Pr\u00e9cision",        "Vid\u00e9odermatoscopie num\u00e9rique pour chaque patient, \u00e0 chaque contr\u00f4le."),
            ("Pr\u00e9vention",       "Cartographie annuelle des n\u00e6vi inscrite d\u2019office dans l\u2019agenda d\u00e8s la deuxi\u00e8me ann\u00e9e."),
            ("Tra\u00e7abilit\u00e9", "Archives photographiques permanentes, transmissibles au patient \u00e0 tout moment."),
            ("Esth\u00e9tique clinique", "Aucun acte esth\u00e9tique sans consultation dermatologique pr\u00e9alable."),
        ],

        "values_label":   "Nos engagements",
        "values_heading": "Quatre promesses qui <em>ne changent jamais.</em>",

        "cta_heading":
            "Vous souhaitez rencontrer les dermatologues <em>avant de prendre rendez-vous\u202f?</em>",
        "cta_primary_label":   "Les trois dermatologues \u2192",
        "cta_secondary_label": "Demander une consultation \u2192",
    },

    # ─── CONSULTATIONS (services) ─────────────────────────────
    "visite": {
        "eyebrow":  "Consultations",
        "headline": "Six parcours cliniques, <em>un seul dossier.</em>",
        "intro":
            "Chaque consultation au Studio Ricciardi suit un parcours clinique "
            "d\u00e9fini, avec une dur\u00e9e, un tarif et un plan de suivi \u00e9crits. "
            "Aucun forfait cach\u00e9, aucun devis oral.",

        "treatments": [
            ("Consultation dermatologique compl\u00e8te",
             "40 min \u00b7 premi\u00e8re visite",
             "Anamn\u00e8se approfondie, examen cutan\u00e9 complet (y compris cuir "
             "chevelu, cavit\u00e9 buccale et zone g\u00e9nitale), dermatoscopie "
             "manuelle, compte rendu personnel et plan de suivi \u00e9crit.",
             "180 \u20ac"),
            ("Cartographie num\u00e9rique des n\u00e6vi",
             "60 min \u00b7 FotoFinder ATBM",
             "Vid\u00e9odermatoscopie haute r\u00e9solution de chaque n\u00e6vus, archivage "
             "num\u00e9rique, comparaison avec l\u2019historique, rapport d\u00e9taill\u00e9 "
             "des l\u00e9sions \u00e0 risque.",
             "240 \u20ac"),
            ("Chirurgie dermatologique ambulatoire",
             "Sur indication \u00b7 ambulatoire",
             "Ex\u00e9r\u00e8se de l\u00e9sions suspectes sous anesth\u00e9sie locale, examen "
             "histopathologique par un laboratoire sp\u00e9cialis\u00e9, compte rendu "
             "dans les huit jours ouvr\u00e9s avec consultation t\u00e9l\u00e9phonique.",
             "\u00e0 partir de 320 \u20ac"),
            ("Laser CO2 fractionn\u00e9",
             "45 min \u00b7 s\u00e9ance unique",
             "Traitement de cicatrices, rides p\u00e9ri-orales, taches solaires "
             "et k\u00e9ratoses actiniques avec le syst\u00e8me Lumenis UltraPulse. "
             "Premi\u00e8re s\u00e9ance toujours pr\u00e9c\u00e9d\u00e9e d\u2019une consultation d\u00e9di\u00e9e.",
             "420 \u20ac"),
            ("Peeling m\u00e9dical dermatologique",
             "30 min \u00b7 cycle de 4 s\u00e9ances",
             "Peelings superficiels et moyens (TCA, mandelic, salicylique, "
             "ph\u00e9nol dilu\u00e9) pratiqu\u00e9s par le dermatologue, protocole "
             "individualis\u00e9 selon le phototype et le dommage actinique.",
             "260 \u20ac / s\u00e9ance"),
            ("Parcours pr\u00e9vention annuel",
             "Annuel \u00b7 3 rendez-vous",
             "Consultation compl\u00e8te, cartographie avec comparaison "
             "historique, conseil photoprotecteur personnalis\u00e9, ligne "
             "directe avec le m\u00e9decin pour les urgences mineures.",
             "580 \u20ac"),
        ],

        "footnote":
            "Tous les paiements sont d\u00e9ductibles en tant que frais de sant\u00e9. "
            "Le cabinet d\u00e9livre un re\u00e7u m\u00e9dical avec timbre fiscal. Les devis "
            "chirurgicaux sont toujours \u00e9crits et sign\u00e9s en amont par le "
            "m\u00e9decin, incluant examens histologiques et visites de suivi.",
        "footnote_heading": "Notes administratives",

        "cta_heading":
            "Une consultation au Studio Ricciardi est <em>pr\u00e9par\u00e9e personnellement</em>.",
        "cta_primary_label":   "Formulaire de demande \u2192",
        "cta_secondary_label": "Ligne directe du secr\u00e9tariat \u2192",
    },

    # ─── M\u00c9DECINS (team) ────────────────────────────────────
    "medici": {
        "eyebrow":  "Les m\u00e9decins",
        "headline": "Trois signatures, un seul <em>bloc op\u00e9ratoire.</em>",
        "intro":
            "Le cabinet est compos\u00e9 de trois dermatologues qui partagent "
            "dossiers, archives dermatoscopiques et protocole clinique. "
            "Chaque patient a toutefois toujours un seul dermatologue r\u00e9f\u00e9rent.",

        "portrait_city": "Rome \u00b7 Via Veneto",

        "doctors": [
            {
                "name":  "Dr Alessandra Ricciardi",
                "role":  "Directrice clinique \u00b7 Dermatologue",
                "tags":  ["Dermoscopie avanc\u00e9e", "Tumeurs cutan\u00e9es", "Dermatologie clinique"],
                "bio":
                    "Sp\u00e9cialiste en dermatologie et v\u00e9n\u00e9r\u00e9ologie \u00e0 l\u2019Universit\u00e0 "
                    "Cattolica del Sacro Cuore de Rome, perfectionn\u00e9e en "
                    "dermoscopie avanc\u00e9e au Memorial Sloan Kettering de New York. "
                    "Membre de la SIDeMaST, de l\u2019EADV et de l\u2019International "
                    "Dermoscopy Society. Autrice de plus de cinquante publications "
                    "index\u00e9es, dont deux chapitres du trait\u00e9 Bolognia-Italia.",
                "portrait": _CHIEF_PORTRAIT,
                "links": [("PubMed", "#"), ("ORCID", "#")],
            },
            {
                "name":  "Dr Emanuele Vitali",
                "role":  "Dermatologue \u00b7 Chirurgie dermatologique",
                "tags":  ["Chirurgie ambulatoire", "Plastique reconstructrice", "Dermatopathologie"],
                "bio":
                    "Form\u00e9 au Policlinico Gemelli de Rome, perfectionn\u00e9 en "
                    "chirurgie dermatologique \u00e0 la Charit\u00e9 de Berlin. Depuis 2015, "
                    "responsable du bloc chirurgical ambulatoire du cabinet. "
                    "Consultant chirurgical pour deux services universitaires "
                    "de dermatologie romains.",
                "portrait": _DR_VITALI_PORTRAIT,
                "links": [("Curriculum", "#")],
            },
            {
                "name":  "Dr Caterina Morelli",
                "role":  "Dermatologue \u00b7 Esth\u00e9tique et Laser",
                "tags":  ["Laser CO2", "M\u00e9decine esth\u00e9tique", "Peelings m\u00e9dicaux"],
                "bio":
                    "Form\u00e9e \u00e0 l\u2019Universit\u00e9 de Padoue, doctorat en dermatologie "
                    "esth\u00e9tique. Perfectionn\u00e9e en lasth\u00e9rapie au Wellman Center de "
                    "Boston. Depuis 2024, responsable du parcours de m\u00e9decine "
                    "esth\u00e9tique dermatologique au Studio Ricciardi. Aucune "
                    "d\u00e9l\u00e9gation au personnel non m\u00e9dical.",
                "portrait": _DR_MORELLI_PORTRAIT,
                "links": [("Publications", "#")],
            },
        ],
    },

    # ─── PUBLICATIONS ─────────────────────────────────────────
    "pubblicazioni": {
        "eyebrow":  "Publications et lectures",
        "headline": "Travaux scientifiques, <em>lectures critiques</em>, vulgarisation dermatologique.",
        "intro":
            "Une s\u00e9lection des travaux du cabinet et des textes de "
            "vulgarisation r\u00e9dig\u00e9s pour le grand public. Chaque contenu est "
            "relu personnellement par le Dr Ricciardi avant publication.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Studio Ricciardi \u00b7 Dermatologie int\u00e9gr\u00e9e",
        "empty_body_fallback_paragraphs": [
            "Article en cours de pr\u00e9paration \u00e9ditoriale. Le texte int\u00e9gral "
            "sera disponible sous peu.",
            "Cet espace d\u00e9crit la voix de l\u2019article\u202f: une note clinique "
            "r\u00e9dig\u00e9e par la dermatologue, dans un ton direct et accessible, "
            "destin\u00e9e aux patients et familles en qu\u00eate d\u2019informations fiables.",
        ],
    },

    "posts": [
        {
            "slug":     "mappatura-nei-quando-farla",
            "kicker":   "Pr\u00e9vention",
            "title":    "Cartographie des n\u00e6vi\u202f: \u00e0 quelle fr\u00e9quence r\u00e9ellement\u202f?",
            "date":     "18 mars 2026",
            "read_min": 7,
            "author":   "Dr Alessandra Ricciardi",
            "lede":
                "La question la plus fr\u00e9quente en consultation est aussi celle "
                "dont la r\u00e9ponse est la plus nuanc\u00e9e. Il n\u2019existe pas de "
                "fr\u00e9quence universelle\u202f: il y a votre phototype, votre dossier "
                "et votre histoire familiale.",
            "body": [
                ("p", "Chaque ann\u00e9e en Italie, on diagnostique environ quinze mille "
                      "nouveaux cas de m\u00e9lanome cutan\u00e9. C\u2019est le cancer de la peau le "
                      "plus l\u00e9tal et, simultan\u00e9ment, celui dont le pronostic est le "
                      "meilleur s\u2019il est d\u00e9tect\u00e9 \u00e0 temps. La fronti\u00e8re entre ces deux "
                      "r\u00e9alit\u00e9s s\u2019appelle dermoscopie num\u00e9rique s\u00e9ri\u00e9e."),
                ("h2", "Trois cat\u00e9gories de risque"),
                ("ol", [
                    "Patient sans ant\u00e9c\u00e9dent familial, peu de n\u00e6vi (moins de 30), phototype II\u2013III\u202f: cartographie tous les 24 mois.",
                    "Patient avec de nombreux n\u00e6vi (plus de 50), peau claire ou br\u00fblures solaires durant l\u2019enfance\u202f: cartographie annuelle.",
                    "Patient avec ant\u00e9c\u00e9dent familial de premier degr\u00e9 de m\u00e9lanome ou n\u00e6vus suspect dans le dossier\u202f: cartographie tous les six \u00e0 douze mois.",
                ]),
                ("p", "Ces intervalles ne sont pas des r\u00e8gles rigides\u202f: chaque "
                      "dermatologue les adapte au cas individuel. Ce qui compte, "
                      "c\u2019est que la cartographie ne soit pas un acte isol\u00e9, mais "
                      "un geste clinique r\u00e9p\u00e9t\u00e9 dans le temps \u2014 avec les m\u00eames "
                      "machines, le m\u00eame m\u00e9decin et le m\u00eame dossier num\u00e9rique."),
                ("h2", "Que signifie \u00ab\u202fdossier num\u00e9rique\u202f\u00bb"),
                ("p", "Cela signifie que chaque n\u00e6vus est photographi\u00e9 en "
                      "vid\u00e9odermatoscopie haute r\u00e9solution et archiv\u00e9 avec des "
                      "coordonn\u00e9es cutan\u00e9es pr\u00e9cises. \u00c0 chaque contr\u00f4le suivant, le "
                      "m\u00e9decin ne regarde pas un nouveau n\u00e6vus\u202f: il compare la m\u00eame "
                      "photo avec celle de l\u2019ann\u00e9e pr\u00e9c\u00e9dente. C\u2019est le changement, "
                      "et non l\u2019image isol\u00e9e, qui g\u00e9n\u00e8re la suspicion clinique."),
                ("blockquote",
                 "La cartographie des n\u00e6vi ne vise pas \u00e0 trouver un m\u00e9lanome. "
                 "Elle vise \u00e0 savoir, pour chaque l\u00e9sion, \u00e0 quoi elle ressemblait "
                 "l\u2019ann\u00e9e derni\u00e8re. C\u2019est un acte de m\u00e9moire clinique, avant "
                 "d\u2019\u00eatre un acte de diagnostic."),
                ("p", "Pour les nouveaux patients, la premi\u00e8re cartographie est "
                      "toujours un acte fondateur\u202f: les photographies d\u2019aujourd\u2019hui "
                      "deviennent la r\u00e9f\u00e9rence pour les dix ann\u00e9es suivantes. Cela "
                      "vaut la peine d\u2019y consacrer une heure de temps clinique, et "
                      "la moiti\u00e9 de la premi\u00e8re consultation y est d\u00e9di\u00e9e."),
            ],
        },
        {
            "slug":     "chirurgia-dermatologica-ambulatoriale",
            "kicker":   "Chirurgie dermatologique",
            "title":    "Chirurgie dermatologique en ambulatoire\u202f: \u00e0 quoi s\u2019attendre",
            "date":     "2 mars 2026",
            "read_min": 5,
            "author":   "Dr Emanuele Vitali",
            "lede":
                "Les ex\u00e9r\u00e8ses dermatologiques ambulatoires font peur seulement "
                "jusqu\u2019\u00e0 l\u2019anesth\u00e9sie. Apr\u00e8s, dans 95\u202f% des cas, le patient quitte "
                "le cabinet du m\u00eame pas qu\u2019en arrivant.",
        },
        {
            "slug":     "laser-co2-cicatrici",
            "kicker":   "Laser dermatologique",
            "title":    "Laser CO2 fractionn\u00e9\u202f: quand c\u2019est le bon choix pour les cicatrices",
            "date":     "15 f\u00e9vrier 2026",
            "read_min": 6,
            "author":   "Dr Caterina Morelli",
            "lede":
                "Le laser CO2 fractionn\u00e9 n\u2019efface pas les cicatrices\u202f: il les "
                "remodelle. Comprendre cette distinction est le premier pas "
                "vers un choix r\u00e9aliste, libre d\u2019attentes irr\u00e9alisables.",
        },
        {
            "slug":     "fotoprotezione-quotidiana",
            "kicker":   "Pr\u00e9vention",
            "title":    "Photoprotection au quotidien\u202f: les trois r\u00e8gles qui comptent vraiment",
            "date":     "28 janvier 2026",
            "read_min": 4,
            "author":   "Dr Alessandra Ricciardi",
            "lede":
                "Un SPF 50 appliqu\u00e9 en quantit\u00e9 insuffisante vaut un SPF 15 "
                "bien appliqu\u00e9. Apr\u00e8s quinze mille consultations dermatologiques, "
                "80\u202f% des patients commettent toujours la m\u00eame erreur.",
        },
        {
            "slug":     "medicina-estetica-dermatologica",
            "kicker":   "Esth\u00e9tique clinique",
            "title":    "Pourquoi au Studio Ricciardi l\u2019esth\u00e9tique n\u2019est pratiqu\u00e9e que par le dermatologue",
            "date":     "10 janvier 2026",
            "read_min": 5,
            "author":   "Dr Caterina Morelli",
            "lede":
                "La m\u00e9decine esth\u00e9tique dermatologique ne se d\u00e9l\u00e8gue pas. "
                "Un choix ferme que nous expliquons aux patients d\u00e8s la "
                "premi\u00e8re consultation, sans d\u00e9tour.",
        },
    ],

    # ─── CONTACT ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contact",
        "headline": "Un seul accueil, <em>une seule personne</em> au bout du fil.",
        "intro":
            "Le cabinet r\u00e9pond personnellement aux appels du lundi au vendredi. "
            "Le secr\u00e9tariat clinique est assur\u00e9 par Mme Bianca Martelli, qui "
            "conna\u00eet chaque dossier et chaque patient par son nom depuis plus "
            "de dix ans.",

        "blocks": [
            ("Adresse",     "Via Veneto 116", "00187 Rome \u00b7 int\u00e9rieur 3, escalier A"),
            ("T\u00e9l\u00e9phone", "+39 06 487 2311", "R\u00e9ponse directe 10 h 00 \u2013 20 h 00"),
            ("E-mail",      "studio@ricciardidermatologia.it", "R\u00e9ponse sous 24 h ouvr\u00e9es"),
            ("Urgences",    "+39 339 221 7080", "Ligne r\u00e9serv\u00e9e aux patients suivis"),
        ],

        "hours": [
            ("Lundi",    "10 h 00 \u2013 14 h 00", "15 h 30 \u2013 20 h 00"),
            ("Mardi",    "10 h 00 \u2013 14 h 00", "15 h 30 \u2013 20 h 00"),
            ("Mercredi", "10 h 00 \u2013 14 h 00", "15 h 30 \u2013 20 h 00"),
            ("Jeudi",    "10 h 00 \u2013 14 h 00", "15 h 30 \u2013 20 h 00"),
            ("Vendredi", "10 h 00 \u2013 14 h 00", "15 h 30 \u2013 19 h 00"),
            ("Samedi",   "Chirurgie sur rendez-vous", "Interventions programm\u00e9es uniquement"),
            ("Dimanche", "Ferm\u00e9", "\u2014"),
        ],

        "transport": [
            ("M\u00e9tro",  "Ligne A \u00b7 station Barberini, 7 minutes \u00e0 pied"),
            ("Voiture", "Parking Saba Ludovisi (convention), entr\u00e9e Via Sicilia"),
            ("Train",   "Gare Roma Termini \u00b7 11 minutes en taxi"),
        ],

        "form_title": "\u00c9crire au cabinet",
        "form_intro":
            "Pour les demandes non urgentes \u2014 informations sur les "
            "consultations, tarifs, pr\u00e9paration \u00e0 la cartographie \u2014 "
            "\u00e9crivez-nous ci-dessous. Le secr\u00e9tariat r\u00e9pond personnellement.",

        "hours_heading":     "Horaires d\u2019ouverture",
        "transport_heading": "Comment nous rejoindre",

        "form_placeholders": {
            "first_name": "Marie",
            "last_name":  "Dupont",
            "email":      "marie.dupont@email.fr",
            "phone":      "+33 6 ...",
            "subject":    "Renseignements sur la premi\u00e8re consultation dermatologique",
            "message":
                "Restez bref \u2014 le secr\u00e9tariat vous recontacte "
                "sous 24 heures ouvr\u00e9es.",
        },
    },

    # ���── APPOINTMENT ────────────���─────────────────────────────
    "richiedi-visita": {
        "eyebrow":  "Demande de consultation dermatologique",
        "headline": "Une consultation dermatologique <em>ne se r\u00e9serve pas</em>\u202f: elle se pr\u00e9pare.",
        "intro":
            "Il n\u2019y a pas de calendrier en ligne. Le cabinet r\u00e9serve chaque "
            "premi\u00e8re consultation apr\u00e8s lecture d\u2019un bref descriptif du cas. "
            "Les demandes sont \u00e9valu\u00e9es personnellement par le m\u00e9decin dans "
            "un d\u00e9lai de 48 heures ouvr\u00e9es.",

        "process_label":   "Comment \u00e7a fonctionne",
        "process_heading":
            "Quatre \u00e9tapes, en <em>quarante-huit heures ouvr\u00e9es.</em>",

        "process": [
            ("01", "Remplissez le formulaire",
             "Dix lignes suffisent pour d\u00e9crire votre demande. Si vous avez "
             "des l\u00e9sions suspectes, joignez une photographie\u202f: cela permet "
             "d\u2019\u00e9valuer la priorit\u00e9 en amont."),
            ("02", "Lecture clinique",
             "Le m\u00e9decin lit personnellement la demande dans les 48 heures "
             "ouvr\u00e9es et d\u00e9termine si la premi\u00e8re consultation rel\u00e8ve de la "
             "dermatologie clinique, chirurgicale ou esth\u00e9tique."),
            ("03", "Proposition de rendez-vous",
             "Le secr\u00e9tariat propose deux cr\u00e9neaux horaires compatibles "
             "avec vos disponibilit\u00e9s et la dur\u00e9e de la consultation "
             "(40 min pour la g\u00e9n\u00e9rale, 60 min pour la cartographie)."),
            ("04", "Confirmation et pr\u00e9paration",
             "Vous recevez par e-mail la liste des documents \u00e0 apporter "
             "(examens ant\u00e9rieurs, photos de l\u00e9sions, traitements en cours) "
             "et les consignes pratiques \u2014 sans maquillage ni vernis \u00e0 "
             "ongles si une cartographie est pr\u00e9vue."),
        ],

        "form_title": "Formulaire de demande",
        "form_band_side_note":
            "Prenez quelques minutes. Les demandes soign\u00e9es sont lues en "
            "int\u00e9gralit\u00e9 par la dermatologue \u2014 les h\u00e2tives, non.",
        "form_band_side_note_small": "\u2193 Formulaire r\u00e9serv\u00e9",

        "form_fields": [
            {"label": "Nom complet", "placeholder": "Marie Dupont",
             "type": "text", "full_width": False},
            {"label": "E-mail", "placeholder": "marie@email.fr",
             "type": "email", "full_width": False},
            {"label": "T\u00e9l\u00e9phone", "placeholder": "+33 6 ...",
             "type": "tel", "full_width": False},
            {"label": "\u00c2ge", "placeholder": "38",
             "type": "number", "full_width": False},
            {"label": "Type de consultation", "type": "select", "full_width": False,
             "options": ["Consultation dermatologique", "Cartographie des n\u00e6vi",
                         "Chirurgie dermatologique", "M\u00e9decine esth\u00e9tique"]},
            {"label": "Disponibilit\u00e9s pr\u00e9f\u00e9r\u00e9es", "type": "select", "full_width": False,
             "options": ["Matin", "Apr\u00e8s-midi", "Indiff\u00e9rent"]},
            {"label": "M\u00e9decin traitant", "placeholder": "Dr ...",
             "type": "text", "full_width": True},
            {"label": "Description du cas",
             "placeholder":
                 "Motif de la consultation, l\u00e9sions concern\u00e9es, sympt\u00f4mes "
                 "r\u00e9cents, traitements en cours. Restez dans les dix lignes.",
             "type": "textarea", "full_width": True},
        ],

        "submit_label": "Envoyer la demande",

        "consent":
            "Je consens au traitement de mes donn\u00e9es personnelles conform\u00e9ment "
            "\u00e0 la politique de confidentialit\u00e9 au sens du R\u00e8glement UE 679/2016. "
            "Les donn\u00e9es cliniques et les photographies dermatoscopiques sont "
            "conserv\u00e9es dans un dossier num\u00e9rique chiffr\u00e9 accessible uniquement "
            "au m\u00e9decin traitant.",

        "footnote":
            "Le cabinet ne r\u00e9pond pas aux demandes anonymes et ne d\u00e9livre "
            "pas d\u2019avis clinique par e-mail sans consultation. Pour les "
            "renseignements administratifs (tarifs, horaires, stationnement), "
            "merci d\u2019utiliser la page contact.",
    },
}


# ===========================================================================
# SPANISH
# ===========================================================================

DERMATOLOGIA_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Cl\u00ednica",          "kind": "home"},
        {"slug": "studio",          "label": "La Cl\u00ednica",       "kind": "about"},
        {"slug": "visite",          "label": "Tratamientos",     "kind": "services"},
        {"slug": "medici",          "label": "M\u00e9dicos",          "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Publicaciones",    "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contacto",         "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Solicitar cita",   "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "R",
        "logo_word":    "Studio Ricciardi",
        "tag":          "Dermatolog\u00eda cl\u00ednica, quir\u00fargica y est\u00e9tica \u00b7 Roma V\u00eda Veneto",
        "phone":        "+39 06 487 2311",
        "email":        "studio@ricciardidermatologia.it",
        "address":      "Via Veneto 116 \u00b7 00187 Roma",
        "hours_compact": "Lun \u2013 Vie \u00b7 10:00 \u2013 20:00",
        "hours_footer_rows": [
            "S\u00e1bado \u00b7 cirug\u00eda con cita previa",
            "Domingo \u00b7 cerrado",
        ],
        "license":      "Colegio de M\u00e9dicos de Roma n.\u00ba 3 / 11982",
        "footer_intro":
            "Cl\u00ednica privada de dermatolog\u00eda cl\u00ednica, quir\u00fargica y "
            "est\u00e9tica. Solo con cita previa.",
    },

    # ─── HOME ───���──────────────────────────────────────────────
    "home": {
        "hero_variant": "editorial-magazine",
        "eyebrow":  "Dermatolog\u00eda cl\u00ednica \u00b7 Roma V\u00eda Veneto",
        "headline": "La piel es un <em>documento de identidad</em>. Lo leemos por completo.",
        "intro":
            "Dermatolog\u00eda cl\u00ednica, quir\u00fargica y est\u00e9tica reunidas en una "
            "sola cl\u00ednica privada en V\u00eda Veneto. Mapeo digital de lunares, "
            "detecci\u00f3n precoz de c\u00e1ncer cut\u00e1neo, cirug\u00eda ambulatoria y "
            "medicina est\u00e9tica realizada por el dermat\u00f3logo.",
        "primary_cta":   "Reservar una primera visita",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "Descubrir la cl\u00ednica",
        "secondary_href":"studio",

        "facts": [
            ("18",    "a\u00f1os de dermatolog\u00eda privada"),
            ("2.400", "mapeos de lunares al a\u00f1o"),
            ("3",     "salas dedicadas \u00b7 1 quir\u00f3fano"),
        ],

        "manifesto_drop_cap": "C",
        "manifesto":
            "ada piel cuenta una historia escrita por el entorno, el tiempo, "
            "los genes y los h\u00e1bitos. El dermat\u00f3logo es el lector de esa "
            "historia \u2014 con el dermatoscopio, con las manos, con la mirada "
            "entrenada de quien ha examinado a decenas de miles de pacientes "
            "antes que usted. En el Studio Ricciardi, nunca tenemos prisa "
            "por terminar una consulta.",

        "signature_visits": [
            ("01", "Mapeo digital de lunares",
             "Videodermatoscop\u00eda de alta resoluci\u00f3n de todos los lunares, "
             "archivo digital y comparaci\u00f3n con el historial del paciente. "
             "Informe entregado en el mismo d\u00eda."),
            ("02", "Cirug\u00eda dermatol\u00f3gica ambulatoria",
             "Escisi\u00f3n de lesiones sospechosas bajo anestesia local con "
             "an\u00e1lisis histopatol\u00f3gico dedicado. Peque\u00f1a cirug\u00eda pl\u00e1stica "
             "reconstructiva incluida en el recorrido."),
            ("03", "L\u00e1ser dermatol\u00f3gico",
             "L\u00e1ser CO2 fraccionado, l\u00e1ser vascular y l\u00e1ser de depilaci\u00f3n de "
             "\u00faltima generaci\u00f3n para cicatrices, lesiones vasculares y "
             "cirug\u00eda cut\u00e1nea no invasiva."),
            ("04", "Dermatolog\u00eda est\u00e9tica",
             "Rellenos, toxina botul\u00ednica, peelings m\u00e9dicos y skinboosters "
             "realizados personalmente por el dermat\u00f3logo. Nunca delegados "
             "en personal no m\u00e9dico."),
        ],

        "chief": {
            "name":  "Dra. Alessandra Ricciardi",
            "role":  "Directora cl\u00ednica \u00b7 Dermat\u00f3loga",
            "bio":
                "Especialista en dermatolog\u00eda y venereolog\u00eda por la "
                "Universit\u00e0 Cattolica del Sacro Cuore de Roma, formaci\u00f3n "
                "avanzada en dermoscop\u00eda en el Memorial Sloan Kettering de "
                "Nueva York y en cirug\u00eda dermatol\u00f3gica en la Charit\u00e9 de "
                "Berl\u00edn. Miembro de SIDeMaST, EADV y la International "
                "Dermoscopy Society. Autora de m\u00e1s de cincuenta publicaciones "
                "indexadas.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "press": ["JAMA Dermatology", "British Journal of Dermatology",
                  "Vanity Fair Wellness", "Corriere Salute", "Vogue Italia"],
        "press_label": "Publicado en",

        "hero_sidebar_top_label": "Direcci\u00f3n cl\u00ednica",
        "hero_sidebar_quote":
            "\u00abLa piel no es un s\u00edntoma que silenciar. "
            "Es un tejido que habla\u2009\u2014\u2009basta aprender a escucharlo.\u00bb",
        "hero_sidebar_author": "\u2014 JAMA Dermatology \u00b7 2025",
        "hero_sidebar_pulse": [
            ("Cl\u00ednica",    "Roma \u00b7 V\u00eda Veneto"),
            ("Desde",      "2008"),
            ("Referencia", "Dermatolog\u00eda integrada"),
        ],

        "signature_visits_label":   "Tratamientos y recorridos",
        "signature_visits_heading": "Cuatro \u00e1reas cl\u00ednicas, <em>un solo archivo.</em>",
        "signature_visits_intro":
            "Las cuatro \u00e1reas en las que trabajamos cada d\u00eda. "
            "La lista completa est\u00e1 en la p\u00e1gina de Tratamientos.",

        "chief_label":   "Direcci\u00f3n cl\u00ednica",
        "chief_heading": "Un solo archivo <em>para cada piel.</em>",

        "credentials": {
            "label": "Acreditaciones y certificaciones",
            "items": [
                ("FotoFinder", "Centro certificado de referencia en dermoscop\u00eda digital FotoFinder Systems", "desde 2012"),
                ("SIDeMaST", "Sociedad Italiana de Dermatolog\u00eda m\u00e9dica, quir\u00fargica, est\u00e9tica y ETS \u2014 miembro activo", ""),
                ("EADV", "European Academy of Dermatology and Venereology \u2014 full member", ""),
                ("IDS", "International Dermoscopy Society \u2014 Advanced Certified Dermoscopist", "desde 2015"),
            ],
        },

        "cta_heading":
            "Un recorrido que empieza <em>desde la primera visita.</em>",
        "cta_primary_label":   "Reservar una primera visita",
        "cta_secondary_label": "C\u00f3mo llegar y contacto",
    },

    # ─── LA CL\u00cdNICA (about) ──────────────────────────────────
    "studio": {
        "eyebrow":  "La cl\u00ednica",
        "headline": "Dieciocho a\u00f1os de <em>dermatolog\u00eda privada integrada</em>.",
        "intro":
            "El Studio Ricciardi nace en 2008 de la convicci\u00f3n de que la "
            "dermatolog\u00eda contempor\u00e1nea no puede vivir solo de revisiones: "
            "exige tiempo cl\u00ednico, cirug\u00eda dedicada y un consultorio "
            "est\u00e9tico que hable el mismo idioma que el diagn\u00f3stico.",

        "history": [
            ("2008",
             "Apertura de la primera sede en Via Veneto 116: tres salas y "
             "una secretaria. La primera consulta dermatol\u00f3gica se realiza "
             "el 4 de febrero de 2008."),
            ("2012",
             "Instalaci\u00f3n del videodermatoscopio digital FotoFinder ATBM, "
             "primero en consulta privada romana. Los mapeos pasan del "
             "papel a un archivo digital incremental, comparable a\u00f1o tras "
             "a\u00f1o en la misma m\u00e1quina."),
            ("2015",
             "Habilitaci\u00f3n del quir\u00f3fano ambulatorio dedicado, con anestesista "
             "externo para las intervenciones complejas. Nace el servicio "
             "de cirug\u00eda dermatol\u00f3gica ambulatoria."),
            ("2019",
             "Llegada del l\u00e1ser CO2 fraccionado Lumenis UltraPulse y del "
             "l\u00e1ser vascular Candela Vbeam Prima. Se inaugura el \u00e1rea "
             "dermatol\u00f3gica l\u00e1ser, con protocolos para cicatrices, queratosis "
             "act\u00ednicas y lesiones vasculares."),
            ("2024",
             "Incorporaci\u00f3n de la Dra. Morelli como responsable del "
             "recorrido de medicina est\u00e9tica dermatol\u00f3gica. Por primera vez, "
             "la est\u00e9tica en la cl\u00ednica est\u00e1 a cargo de una dermat\u00f3loga "
             "a tiempo completo."),
        ],

        "method_title": "M\u00e9todo",
        "method_paragraphs": [
            "Una consulta en el Studio Ricciardi comienza siempre con una "
            "pregunta sencilla: \u00bfcu\u00e1ndo empez\u00f3 a notarlo? Esa fecha es "
            "nuestro verdadero punto de partida. Las lesiones cut\u00e1neas no "
            "se leen solo en secci\u00f3n: se leen en el tiempo, comparando "
            "fotograf\u00edas, informes y sensaciones del paciente.",
            "Para cada paciente construimos un archivo dermatosc\u00f3pico "
            "digital que acompa\u00f1a a la persona durante toda la vida: "
            "desde la primera revisi\u00f3n en la adolescencia hasta los "
            "controles de madurez. Cada lunar se fotograf\u00eda, cataloga y "
            "compara en cada revisi\u00f3n posterior. Es el cambio, no la "
            "imagen aislada, lo que genera la sospecha cl\u00ednica.",
            "La cirug\u00eda dermatol\u00f3gica, cuando est\u00e1 indicada, se realiza "
            "en el mismo d\u00eda bajo anestesia local, por el m\u00e9dico que "
            "estableci\u00f3 la indicaci\u00f3n. La pieza histol\u00f3gica se conf\u00eda a un "
            "laboratorio especializado en dermatopatolog\u00eda, con el que "
            "mantenemos un di\u00e1logo telef\u00f3nico directo para los casos "
            "de mayor complejidad.",
        ],

        "values": [
            ("Precisi\u00f3n",        "Videodermatoscop\u00eda digital para cada paciente, en cada revisi\u00f3n."),
            ("Prevenci\u00f3n",       "Mapeo anual de lunares incluido autom\u00e1ticamente en la agenda desde el segundo a\u00f1o."),
            ("Trazabilidad",     "Archivo fotogr\u00e1fico permanente, entregable al paciente en cualquier momento."),
            ("Est\u00e9tica cl\u00ednica", "Ning\u00fan tratamiento est\u00e9tico sin consulta dermatol\u00f3gica previa."),
        ],

        "values_label":   "Lo que garantizamos",
        "values_heading": "Cuatro compromisos que <em>nunca cambian.</em>",

        "cta_heading":
            "\u00bfDesea conocer a las dermat\u00f3logas <em>antes de reservar?</em>",
        "cta_primary_label":   "Las tres dermat\u00f3logas \u2192",
        "cta_secondary_label": "Solicitar consulta privada \u2192",
    },

    # ─── TRATAMIENTOS (services) ──────────────────────────────
    "visite": {
        "eyebrow":  "Tratamientos",
        "headline": "Seis recorridos cl\u00ednicos, <em>una sola historia.</em>",
        "intro":
            "Cada consulta en el Studio Ricciardi es un recorrido cl\u00ednico "
            "definido, con duraci\u00f3n, precio y plan de seguimiento por escrito. "
            "Sin forfaits ocultos ni presupuestos verbales.",

        "treatments": [
            ("Consulta dermatol\u00f3gica completa",
             "40 min \u00b7 primera visita",
             "Anamnesis amplia, exploraci\u00f3n cut\u00e1nea de cuerpo completo "
             "(incluyendo cuero cabelludo, cavidad oral y \u00e1rea genital), "
             "dermatoscop\u00eda manual, informe personal y plan de seguimiento.",
             "180 \u20ac"),
            ("Mapeo digital de lunares",
             "60 min \u00b7 FotoFinder ATBM",
             "Videodermatoscop\u00eda de alta resoluci\u00f3n de cada lunar, archivo "
             "digital, comparaci\u00f3n con el historial, informe detallado de "
             "las lesiones de riesgo.",
             "240 \u20ac"),
            ("Cirug\u00eda dermatol\u00f3gica ambulatoria",
             "Seg\u00fan indicaci\u00f3n \u00b7 ambulatorio",
             "Escisi\u00f3n de lesiones sospechosas bajo anestesia local, examen "
             "histopatol\u00f3gico por laboratorio especializado, informe en ocho "
             "d\u00edas h\u00e1biles con consulta telef\u00f3nica dedicada.",
             "desde 320 \u20ac"),
            ("L\u00e1ser CO2 fraccionado",
             "45 min \u00b7 sesi\u00f3n \u00fanica",
             "Tratamiento de cicatrices, arrugas periorales, manchas solares "
             "y queratosis act\u00ednicas con sistema Lumenis UltraPulse. Primera "
             "sesi\u00f3n siempre precedida de consulta dermatol\u00f3gica dedicada.",
             "420 \u20ac"),
            ("Peeling m\u00e9dico dermatol\u00f3gico",
             "30 min \u00b7 ciclo de 4 sesiones",
             "Peelings superficiales y medios (TCA, mand\u00e9lico, salic\u00edlico, "
             "fenol diluido) realizados por la dermat\u00f3loga, con protocolo "
             "individualizado seg\u00fan fototipo y da\u00f1o act\u00ednico.",
             "260 \u20ac / sesi\u00f3n"),
            ("Programa de prevenci\u00f3n anual",
             "Anual \u00b7 3 citas",
             "Consulta completa, mapeo con comparaci\u00f3n hist\u00f3rica, asesor\u00eda "
             "fotoprotectora personalizada, l\u00ednea directa con el m\u00e9dico "
             "para consultas menores durante el a\u00f1o.",
             "580 \u20ac"),
        ],

        "footnote":
            "Todos los pagos son deducibles como gastos sanitarios. La cl\u00ednica "
            "emite recibo sanitario con marca de bollo. Los presupuestos "
            "quir\u00fargicos son siempre escritos y firmados por el m\u00e9dico, "
            "incluyendo ex\u00e1menes histol\u00f3gicos y visitas de seguimiento.",
        "footnote_heading": "Notas administrativas",

        "cta_heading":
            "Una consulta en el Studio Ricciardi es <em>preparada personalmente</em>.",
        "cta_primary_label":   "Formulario de solicitud \u2192",
        "cta_secondary_label": "L\u00ednea directa de secretar\u00eda \u2192",
    },

    # ─── M\u00c9DICOS (team) ────��────────────────────────────────
    "medici": {
        "eyebrow":  "Los m\u00e9dicos",
        "headline": "Tres firmas, un solo <em>quir\u00f3fano.</em>",
        "intro":
            "La cl\u00ednica est\u00e1 formada por tres dermat\u00f3logas que comparten "
            "historiales, archivo dermatosc\u00f3pico y protocolo cl\u00ednico. "
            "Cada paciente, sin embargo, tiene siempre una sola dermat\u00f3loga "
            "de referencia.",

        "portrait_city": "Roma \u00b7 V\u00eda Veneto",

        "doctors": [
            {
                "name":  "Dra. Alessandra Ricciardi",
                "role":  "Directora cl\u00ednica \u00b7 Dermat\u00f3loga",
                "tags":  ["Dermoscop\u00eda avanzada", "Tumores cut\u00e1neos", "Dermatolog\u00eda cl\u00ednica"],
                "bio":
                    "Especialista en dermatolog\u00eda y venereolog\u00eda por la "
                    "Universit\u00e0 Cattolica del Sacro Cuore de Roma, formaci\u00f3n "
                    "avanzada en dermoscop\u00eda en el Memorial Sloan Kettering de "
                    "Nueva York. Miembro de SIDeMaST, EADV y la International "
                    "Dermoscopy Society. Autora de m\u00e1s de cincuenta publicaciones "
                    "indexadas, incluyendo dos cap\u00edtulos del tratado Bolognia-Italia.",
                "portrait": _CHIEF_PORTRAIT,
                "links": [("PubMed", "#"), ("ORCID", "#")],
            },
            {
                "name":  "Dr. Emanuele Vitali",
                "role":  "Dermat\u00f3logo \u00b7 Cirug\u00eda dermatol\u00f3gica",
                "tags":  ["Cirug\u00eda ambulatoria", "Pl\u00e1stica reconstructiva", "Dermatopatolog\u00eda"],
                "bio":
                    "Formado en el Policlinico Gemelli de Roma, perfeccionado en "
                    "cirug\u00eda dermatol\u00f3gica en la Charit\u00e9 de Berl\u00edn. Desde 2015, "
                    "responsable del quir\u00f3fano ambulatorio de la cl\u00ednica. "
                    "Consultor quir\u00fargico de dos servicios universitarios de "
                    "dermatolog\u00eda en Roma.",
                "portrait": _DR_VITALI_PORTRAIT,
                "links": [("Curr\u00edculum", "#")],
            },
            {
                "name":  "Dra. Caterina Morelli",
                "role":  "Dermat\u00f3loga \u00b7 Est\u00e9tica y L\u00e1ser",
                "tags":  ["L\u00e1ser CO2", "Medicina est\u00e9tica", "Peelings m\u00e9dicos"],
                "bio":
                    "Formada en la Universidad de Padua, doctorado en "
                    "dermatolog\u00eda est\u00e9tica. Perfeccionada en laserterapia en "
                    "el Wellman Center de Boston. Desde 2024, responsable del "
                    "recorrido de medicina est\u00e9tica dermatol\u00f3gica del Studio "
                    "Ricciardi. Sin delegaci\u00f3n en personal no m\u00e9dico.",
                "portrait": _DR_MORELLI_PORTRAIT,
                "links": [("Publicaciones", "#")],
            },
        ],
    },

    # ─── PUBLICACIONES ────────────────────────────────────────
    "pubblicazioni": {
        "eyebrow":  "Publicaciones y lecturas",
        "headline": "Trabajos cient\u00edficos, <em>lecturas cr\u00edticas</em>, divulgaci\u00f3n dermatol\u00f3gica.",
        "intro":
            "Una selecci\u00f3n de los trabajos de la cl\u00ednica y de los textos "
            "divulgativos escritos para el p\u00fablico general. Todos los contenidos "
            "son revisados personalmente por la Dra. Ricciardi antes de su "
            "publicaci\u00f3n.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Studio Ricciardi \u00b7 Dermatolog\u00eda integrada",
        "empty_body_fallback_paragraphs": [
            "Art\u00edculo en preparaci\u00f3n editorial. El texto completo estar\u00e1 "
            "disponible en breve.",
            "Este espacio describe la voz del art\u00edculo: una nota cl\u00ednica "
            "escrita por la dermat\u00f3loga, en tono directo y sin tecnicismos, "
            "pensada para pacientes y familiares que buscan informaci\u00f3n fiable.",
        ],
    },

    "posts": [
        {
            "slug":     "mappatura-nei-quando-farla",
            "kicker":   "Prevenci\u00f3n",
            "title":    "Mapeo de lunares: cada cu\u00e1nto hacerlo realmente",
            "date":     "18 de marzo de 2026",
            "read_min": 7,
            "author":   "Dra. Alessandra Ricciardi",
            "lede":
                "La pregunta m\u00e1s frecuente en consulta es tambi\u00e9n la que tiene "
                "la respuesta m\u00e1s matizada. No existe una frecuencia universal: "
                "existe su fototipo, su archivo y su historia familiar.",
            "body": [
                ("p", "Cada a\u00f1o en Italia se diagnostican unos quince mil nuevos "
                      "casos de melanoma cut\u00e1neo. Es el c\u00e1ncer de piel con mayor "
                      "letalidad y, al mismo tiempo, el de mejor pron\u00f3stico cuando "
                      "se detecta a tiempo. La frontera entre ambas realidades se "
                      "llama dermoscop\u00eda digital seriada."),
                ("h2", "Tres categor\u00edas de riesgo"),
                ("ol", [
                    "Paciente sin antecedentes familiares, pocos lunares (menos de 30), fototipo II\u2013III: mapeo cada 24 meses.",
                    "Paciente con muchos lunares (m\u00e1s de 50), piel clara o quemaduras solares en la infancia: mapeo anual.",
                    "Paciente con antecedente familiar de primer grado de melanoma o lunar sospechoso en archivo: mapeo cada seis a doce meses.",
                ]),
                ("p", "Estas frecuencias no son reglas r\u00edgidas: cada dermat\u00f3logo "
                      "las adapta al paciente individual. Lo importante es que el "
                      "mapeo no sea una prestaci\u00f3n aislada, sino un acto cl\u00ednico "
                      "repetido en el tiempo \u2014 con las mismas m\u00e1quinas, el mismo "
                      "m\u00e9dico y el mismo archivo digital."),
                ("h2", "Qu\u00e9 significa \u2018archivo digital\u2019"),
                ("p", "Significa que cada lunar se fotograf\u00eda en videodermatoscop\u00eda "
                      "de alta resoluci\u00f3n y se archiva con coordenadas cut\u00e1neas "
                      "precisas. En cada revisi\u00f3n posterior, el m\u00e9dico no examina un "
                      "lunar nuevo: compara la misma fotograf\u00eda con la del a\u00f1o "
                      "anterior. Es el cambio, no la imagen aislada, lo que genera "
                      "la sospecha cl\u00ednica."),
                ("blockquote",
                 "El mapeo de lunares no busca encontrar un melanoma. Busca saber, "
                 "de cada lesi\u00f3n, c\u00f3mo era el a\u00f1o pasado. Es un acto de memoria "
                 "cl\u00ednica, antes que de diagn\u00f3stico."),
                ("p", "Para los nuevos pacientes, el primer mapeo es siempre un acto "
                      "fundacional: las fotograf\u00edas de hoy se convierten en la "
                      "referencia para los pr\u00f3ximos diez a\u00f1os. Vale la pena dedicarle "
                      "una hora de tiempo cl\u00ednico, y la mitad de la primera consulta "
                      "se destina a ello."),
            ],
        },
        {
            "slug":     "chirurgia-dermatologica-ambulatoriale",
            "kicker":   "Cirug\u00eda dermatol\u00f3gica",
            "title":    "Cirug\u00eda dermatol\u00f3gica ambulatoria: qu\u00e9 esperar realmente",
            "date":     "2 de marzo de 2026",
            "read_min": 5,
            "author":   "Dr. Emanuele Vitali",
            "lede":
                "Las escisiones dermatol\u00f3gicas ambulatorias asustan solo hasta "
                "el momento de la anestesia. Despu\u00e9s, en el 95\u202f% de los casos, "
                "el paciente sale de la cl\u00ednica caminando igual que entr\u00f3.",
        },
        {
            "slug":     "laser-co2-cicatrici",
            "kicker":   "L\u00e1ser dermatol\u00f3gico",
            "title":    "L\u00e1ser CO2 fraccionado: cu\u00e1ndo es la elecci\u00f3n correcta para cicatrices",
            "date":     "15 de febrero de 2026",
            "read_min": 6,
            "author":   "Dra. Caterina Morelli",
            "lede":
                "El l\u00e1ser CO2 fraccionado no borra las cicatrices: las remodela. "
                "Entender esta distinci\u00f3n es el primer paso hacia una elecci\u00f3n "
                "realista y libre de expectativas inalcanzables.",
        },
        {
            "slug":     "fotoprotezione-quotidiana",
            "kicker":   "Prevenci\u00f3n",
            "title":    "Fotoprotecci\u00f3n diaria: las tres reglas que realmente importan",
            "date":     "28 de enero de 2026",
            "read_min": 4,
            "author":   "Dra. Alessandra Ricciardi",
            "lede":
                "Un SPF 50 aplicado en cantidad incorrecta equivale a un SPF 15 "
                "bien aplicado. Tras quince mil consultas dermatol\u00f3gicas, el "
                "80\u202f% de los pacientes comete siempre el mismo error.",
        },
        {
            "slug":     "medicina-estetica-dermatologica",
            "kicker":   "Est\u00e9tica cl\u00ednica",
            "title":    "Por qu\u00e9 en el Studio Ricciardi la est\u00e9tica la realiza solo el dermat\u00f3logo",
            "date":     "10 de enero de 2026",
            "read_min": 5,
            "author":   "Dra. Caterina Morelli",
            "lede":
                "La medicina est\u00e9tica dermatol\u00f3gica no es una tarea que se "
                "delegue. Una decisi\u00f3n firme que explicamos a los pacientes "
                "en la primera consulta, sin rodeos.",
        },
    ],

    # ─── CONTACTO ─────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contacto",
        "headline": "Una sola secretar\u00eda, <em>una sola persona</em> al otro lado del tel\u00e9fono.",
        "intro":
            "La cl\u00ednica atiende las llamadas telef\u00f3nicas personalmente de "
            "lunes a viernes. La secretar\u00eda cl\u00ednica est\u00e1 a cargo de la "
            "Sra. Bianca Martelli, que conoce cada historial y cada paciente "
            "por su nombre desde hace m\u00e1s de diez a\u00f1os.",

        "blocks": [
            ("Direcci\u00f3n",  "Via Veneto 116", "00187 Roma \u00b7 interior 3, escalera A"),
            ("Tel\u00e9fono",  "+39 06 487 2311",   "Respuesta directa 10:00 \u2013 20:00"),
            ("Email",     "studio@ricciardidermatologia.it", "Respuesta en 24 horas h\u00e1biles"),
            ("Urgencias", "+39 339 221 7080",  "L\u00ednea reservada a pacientes en seguimiento"),
        ],

        "hours": [
            ("Lunes",     "10:00 \u2013 14:00", "15:30 \u2013 20:00"),
            ("Martes",    "10:00 \u2013 14:00", "15:30 \u2013 20:00"),
            ("Mi\u00e9rcoles", "10:00 \u2013 14:00", "15:30 \u2013 20:00"),
            ("Jueves",    "10:00 \u2013 14:00", "15:30 \u2013 20:00"),
            ("Viernes",   "10:00 \u2013 14:00", "15:30 \u2013 19:00"),
            ("S\u00e1bado",    "Cirug\u00eda con cita previa", "Solo intervenciones programadas"),
            ("Domingo",   "Cerrado", "\u2014"),
        ],

        "transport": [
            ("Metro",  "L\u00ednea A \u00b7 estaci\u00f3n Barberini, 7 minutos a pie"),
            ("Coche",  "Aparcamiento Saba Ludovisi (convenio), entrada por Via Sicilia"),
            ("Tren",   "Estaci\u00f3n Roma Termini \u00b7 11 minutos en taxi"),
        ],

        "form_title": "Escribir a la cl\u00ednica",
        "form_intro":
            "Para consultas no urgentes \u2014 informaci\u00f3n sobre tratamientos, "
            "precios, preparaci\u00f3n para el mapeo \u2014 escr\u00edbanos a continuaci\u00f3n. "
            "Responde personalmente la secretar\u00eda cl\u00ednica.",

        "hours_heading":     "Horario de apertura",
        "transport_heading": "C\u00f3mo llegar",

        "form_placeholders": {
            "first_name": "Mar\u00eda",
            "last_name":  "Garc\u00eda",
            "email":      "maria.garcia@email.es",
            "phone":      "+34 6 ...",
            "subject":    "Informaci\u00f3n sobre la primera consulta dermatol\u00f3gica",
            "message":
                "Sea breve \u2014 la secretar\u00eda le contactar\u00e1 en 24 horas h\u00e1biles.",
        },
    },

    # ─── SOLICITAR CITA ──────────���────────────────────────────
    "richiedi-visita": {
        "eyebrow":  "Solicitud de consulta dermatol\u00f3gica",
        "headline": "Una consulta dermatol\u00f3gica <em>no se reserva</em>: se prepara.",
        "intro":
            "No existe un calendario en l\u00ednea. La cl\u00ednica reserva cada primera "
            "consulta tras leer una breve descripci\u00f3n del caso. Las solicitudes "
            "son evaluadas personalmente por el m\u00e9dico en un plazo de 48 horas "
            "h\u00e1biles.",

        "process_label":   "C\u00f3mo funciona",
        "process_heading":
            "Cuatro pasos, en <em>cuarenta y ocho horas h\u00e1biles.</em>",

        "process": [
            ("01", "Rellene el formulario",
             "Diez l\u00edneas bastan para describir su caso. Si tiene lesiones "
             "sospechosas, adjunte una fotograf\u00eda: ayuda a valorar la "
             "prioridad con antelaci\u00f3n."),
            ("02", "Lectura cl\u00ednica",
             "El m\u00e9dico lee personalmente la solicitud en un plazo de "
             "48 horas h\u00e1biles y determina si la primera consulta "
             "corresponde a dermatolog\u00eda cl\u00ednica, quir\u00fargica o est\u00e9tica."),
            ("03", "Propuesta de cita",
             "La secretar\u00eda propone dos franjas horarias compatibles "
             "con sus preferencias y con la duraci\u00f3n de la consulta "
             "(40 min para la general, 60 min para el mapeo completo)."),
            ("04", "Confirmaci\u00f3n y preparaci\u00f3n",
             "Recibe por email la lista de lo que debe traer (ex\u00e1menes "
             "previos, fotos de lesiones, terapia actual) e instrucciones "
             "pr\u00e1cticas para la consulta \u2014 sin maquillaje ni esmalte de "
             "u\u00f1as si se prev\u00e9 un mapeo."),
        ],

        "form_title": "Formulario de solicitud",
        "form_band_side_note":
            "Ded\u00edquele unos minutos. Las solicitudes preparadas con cuidado "
            "son le\u00eddas \u00edntegramente por la dermat\u00f3loga \u2014 las apresuradas, no.",
        "form_band_side_note_small": "\u2193 Formulario reservado",

        "form_fields": [
            {"label": "Nombre completo", "placeholder": "Mar\u00eda Garc\u00eda",
             "type": "text", "full_width": False},
            {"label": "Email", "placeholder": "maria@email.es",
             "type": "email", "full_width": False},
            {"label": "Tel\u00e9fono", "placeholder": "+34 6 ...",
             "type": "tel", "full_width": False},
            {"label": "Edad", "placeholder": "38",
             "type": "number", "full_width": False},
            {"label": "Tipo de consulta", "type": "select", "full_width": False,
             "options": ["Consulta dermatol\u00f3gica", "Mapeo de lunares",
                         "Cirug\u00eda dermatol\u00f3gica", "Medicina est\u00e9tica"]},
            {"label": "Disponibilidad preferida", "type": "select", "full_width": False,
             "options": ["Ma\u00f1ana", "Tarde", "Indiferente"]},
            {"label": "M\u00e9dico de cabecera", "placeholder": "Dr. ...",
             "type": "text", "full_width": True},
            {"label": "Descripci\u00f3n breve del caso",
             "placeholder":
                 "Motivo de la consulta, lesiones de inter\u00e9s, s\u00edntomas "
                 "recientes, tratamientos en curso. No m\u00e1s de diez l\u00edneas.",
             "type": "textarea", "full_width": True},
        ],

        "submit_label": "Enviar solicitud",

        "consent":
            "Consiento el tratamiento de mis datos personales seg\u00fan la "
            "pol\u00edtica de privacidad conforme al Reglamento UE 679/2016. "
            "Los datos cl\u00ednicos y las fotograf\u00edas dermatosc\u00f3picas se "
            "conservan en archivo digital cifrado con acceso exclusivo "
            "del m\u00e9dico responsable.",

        "footnote":
            "La cl\u00ednica no responde a solicitudes an\u00f3nimas ni emite "
            "opiniones cl\u00ednicas por email sin consulta. Para informaci\u00f3n "
            "administrativa (precios, horarios, aparcamiento), utilice la "
            "p\u00e1gina de contacto.",
    },
}


# ===========================================================================
# ARABIC (RTL)
# ===========================================================================

DERMATOLOGIA_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "العيادة",            "kind": "home"},
        {"slug": "studio",          "label": "عن العيادة",          "kind": "about"},
        {"slug": "visite",          "label": "العلاجات",           "kind": "services"},
        {"slug": "medici",          "label": "الأطباء",            "kind": "team"},
        {"slug": "pubblicazioni",   "label": "المنشورات",          "kind": "blog_list"},
        {"slug": "contatti",        "label": "تواصل",             "kind": "contact"},
        {"slug": "richiedi-visita", "label": "طلب موعد",          "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "R",
        "logo_word":    "Studio Ricciardi",
        "tag":          "طب الجلد السريري والجراحي والتجميلي · روما فيا فينيتو",
        "phone":        "+39 06 487 2311",
        "email":        "studio@ricciardidermatologia.it",
        "address":      "Via Veneto 116 · 00187 روما",
        "hours_compact": "الاثنين – الجمعة · 10:00 – 20:00",
        "hours_footer_rows": [
            "السبت · جراحة بموعد مسبق",
            "الأحد · مغلق",
        ],
        "license":      "نقابة أطباء روما 3 / 11982",
        "footer_intro":
            "عيادة خاصة متخصصة في طب الجلد السريري والجراحي والتجميلي. "
            "الزيارة بموعد مسبق فقط.",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "hero_variant": "editorial-magazine",
        "eyebrow":  "طب الجلد السريري · روما فيا فينيتو",
        "headline": "البشرة <em>وثيقة هوية</em>. نقرأها بالكامل.",
        "intro":
            "طب الجلد السريري والجراحي والتجميلي تحت سقف واحد في فيا "
            "فينيتو. رسم خرائط الشامات الرقمية، الكشف المبكر عن سرطان "
            "الجلد، جراحة يومية واستئصالات، وعلاجات تجميلية يُجريها "
            "طبيب الأمراض الجلدية شخصياً.",
        "primary_cta":   "احجز زيارة أولى",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "اكتشف العيادة",
        "secondary_href":"studio",

        "facts": [
            ("18",    "عاماً من طب الجلد الخاص"),
            ("2.400", "خريطة شامات في السنة"),
            ("3",     "غرف مخصصة · 1 غرفة جراحية"),
        ],

        "manifesto_drop_cap": "ك",
        "manifesto":
            "لّ بشرة تروي حكاية كتبتها البيئة والزمن والجينات والعادات. "
            "طبيب الأمراض الجلدية هو قارئ تلك الحكاية — بالمنظار الجلدي، "
            "وباليدين، وبعين المتمرّس الذي فحص عشرات الآلاف من المرضى "
            "قبلكم. في Studio Ricciardi، لا نتعجّل أبداً في إنهاء الاستشارة.",

        "signature_visits": [
            ("01", "رسم خرائط الشامات الرقمي",
             "تصوير جلدي بالفيديو عالي الدقة لكلّ شامة، أرشفة رقمية "
             "ومقارنة مع السجل التاريخي للمريض. يُسلَّم التقرير في اليوم نفس��."),
            ("02", "جراحة جلدية نهارية",
             "استئصال الآفات المشبوهة تحت التخدير الموضعي مع تحليل "
             "نسيجي مرضي مخصص. تتضمّن جراحة ترميمية تجميلية صغيرة "
             "ضمن المسار العلاجي."),
            ("03", "ليزر جلدي",
             "ليزر CO2 المجزّأ، ليزر الأوعية الدموية وليزر إزالة الشعر "
             "من أحدث جيل لعلاج الندوب والآفات الوعائية والجراحة "
             "الجلدية غير الغازية."),
            ("04", "طب الجلد التجميلي",
             "فيلر، توكسين البوتولينوم، تقشير طبي و skinboosters يُنفَّذها "
             "طبيب الأمراض الجلدية شخصياً. لا تُفوَّض أبداً لغير الأطباء."),
        ],

        "chief": {
            "name":  "الدكتورة أليساندرا ريتشاردي",
            "role":  "المديرة السريرية · طبيبة أمراض جلدية",
            "bio":
                "متخصصة في طب الأمراض الجلدية والتناسلية من Università "
                "Cattolica del Sacro Cuore في روما، وأكملت تدريباً متقدماً "
                "في التنظير الجلدي في Memorial Sloan Kettering في نيويورك "
                "وفي الجراحة الجلدية في Charité في برلين. عضو في SIDeMaST "
                "و EADV و International Dermoscopy Society. مؤلفة لأكثر "
                "من خمسين بحثاً مفهرساً.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "press": ["JAMA Dermatology", "British Journal of Dermatology",
                  "Vanity Fair Wellness", "Corriere Salute", "Vogue Italia"],
        "press_label": "نُشر في",

        "hero_sidebar_top_label": "الإدارة السرير��ة",
        "hero_sidebar_quote":
            "«البشرة ليست عَرَضاً يُسكَت. "
            "إنها نسيجٌ يتحدث — يكفي أن تتعلّم الإصغاء إليه.»",
        "hero_sidebar_author": "— JAMA Dermatology · 2025",
        "hero_sidebar_pulse": [
            ("العيادة",  "روما · فيا فينيتو"),
            ("منذ",      "2008"),
            ("التخصص",  "طب الجلد المتكامل"),
        ],

        "signature_visits_label":   "العلاجات والمسارات",
        "signature_visits_heading": "أربعة مجالات سريرية، <em>أرشيف واحد.</em>",
        "signature_visits_intro":
            "المجالات الأربعة التي نعمل فيها يومياً. "
            "القائمة الكاملة في صفحة العلاجات.",

        "chief_label":   "الإدارة السريرية",
        "chief_heading": "أرشيف واحد <em>لكلّ بشرة.</em>",

        "credentials": {
            "label": "الاعتمادات والشهادات",
            "items": [
                ("FotoFinder", "مركز معتمد مرجعي للتنظير الجلدي الرقمي FotoFinder Systems", "منذ 2012"),
                ("SIDeMaST", "الجمعية الإيطالية لطب الجلد الطبي والجراحي والتجميلي — عضو فاعل", ""),
                ("EADV", "European Academy of Dermatology and Venereology — full member", ""),
                ("IDS", "International Dermoscopy Society — Advanced Certified Dermoscopist", "منذ 2015"),
            ],
        },

        "cta_heading":
            "مسار يبدأ <em>من الزيارة الأولى.</em>",
        "cta_primary_label":   "احجز زيارة أولى",
        "cta_secondary_label": "الموقع والتواصل",
    },

    # ─── عن العيادة (about) ──────���────────────────────────────
    "studio": {
        "eyebrow":  "عن العيادة",
        "headline": "ثمانية عشر عاماً من <em>طب الجلد الخاص المتكامل</em>.",
        "intro":
            "تأسّس Studio Ricciardi عام 2008 انطلاقاً من قناعة بأن طب "
            "الجلد المعاصر لا يمكن أن يعيش على الفحوصات الروتينية وحدها: "
            "فهو يتطلب وقتاً سريرياً، وجراحة مخصصة، وعيادة تجميلية "
            "تتحدث لغة التشخيص نفسها.",

        "history": [
            ("2008",
             "افتتاح المقر الأول في Via Veneto 116 — ثلاث غرف وسكرتيرة "
             "واحدة. أُجريت أول استشارة جلدية في 4 فبراير 2008."),
            ("2012",
             "تركيب جهاز التصوير الجلدي الرقمي FotoFinder ATBM، الأول "
             "في عيادة خاصة رومانية. تحوّل رسم خرائط الشامات من الورق "
             "إلى أرشيف رقمي تراكمي قابل للمقارنة عاماً بعد عام."),
            ("2015",
             "تجهيز غرفة العمليات الجراحية المخصصة، مع طبيب تخدير خارجي "
             "للعمليات المعقدة. يُولد خدمة الجراحة الجلدية النهارية."),
            ("2019",
             "وصول ليزر CO2 المجزّأ Lumenis UltraPulse وليزر الأوعية "
             "Candela Vbeam Prima. يُفتتح قسم الليزر الجلدي ببروتوكولات "
             "مخصصة للندوب والتقرّنات الشمسية والآفات الوعائية."),
            ("2024",
             "انضمام الدكتورة موريلّي مسؤولةً عن مسار طب الجلد التجميلي. "
             "لأول مرة، يتولّى طبيب أمراض جلدية متفرّغ الطب التجميلي "
             "في العيادة."),
        ],

        "method_title": "المنهج",
        "method_paragraphs": [
            "تبدأ الاستشارة في Studio Ricciardi دائماً بسؤال بسيط: متى "
            "لاحظتها لأول مرة؟ ذلك التاريخ هو نقطة انطلاقنا الحقيقية. "
            "الآفات الجلدية لا تُقرأ بالمقاطع وحدها: بل تُقرأ عبر الزمن، "
            "بمقارنة الصور والتقارير وملاحظات المريض.",
            "لكلّ مريض نبني أرشيفاً جلدياً رقمياً يرافقه مدى الحياة: من "
            "أول فحص في سن المراهقة وحتى المراجعات في مرحلة النضج. "
            "كلّ شامة تُصوَّر وتُفهرس وتُقارَن في كلّ مراجعة لاحقة. "
            "التغيّر — لا الصورة المنفردة — هو ما يولّد الشبهة السريرية.",
            "الجراحة الجلدية، عند وجود المؤشر، تُجرى في اليوم نفسه تحت "
            "التخدير الموضعي على يد الطبيب الذي وضع المؤشر. تُرسَل العيّنة "
            "النسيجية إلى مختبر متخصص في أمراض الجلد النسيجية، نتحاور "
            "معه هاتفياً مباشرة في الحالات الأكثر تعقيداً.",
        ],

        "values": [
            ("الدقة",          "تصوير جلدي رقمي لكلّ مريض، في كلّ مراجعة."),
            ("الوقاية",        "رسم خرائط سنوي للشامات يُدرَج تلقائياً في الأجندة منذ العام الثاني."),
            ("قابلية التتبع",  "أرشيف فوتوغرافي دائم يُسلَّم للمريض في أي وقت."),
            ("التجميل السريري","لا علاج تجميلي بدون استشارة جلدية مسبقة."),
        ],

        "values_label":   "ما نضمنه",
        "values_heading": "أربعة التزامات <em>لا تتغيّر أبداً.</em>",

        "cta_heading":
            "هل تودّ التعرّف على طبيبات الأمراض الجلدية <em>قبل الحجز؟</em>",
        "cta_primary_label":   "الطبيبات الثلاث →",
        "cta_secondary_label": "اطلب زيارة خاصة →",
    },

    # ─── العلاجات (services) ──────────────────────────────────
    "visite": {
        "eyebrow":  "العلاجات",
        "headline": "ستة مسارات سريرية، <em>ملف واحد.</em>",
        "intro":
            "كلّ استشارة في Studio Ricciardi مسار سريري محدّد بمدّة وسعر "
            "وخطّة متابعة مكتوبة. لا رسوم مخفية ولا تقديرات شفهية.",

        "treatments": [
            ("استشارة جلدية ش��ملة",
             "40 دقيقة · زيارة أولى",
             "استجواب سريري موسَّع، فحص كامل للجلد (يشمل فروة الرأس "
             "والتجويف الفموي والمنطقة التناسلية)، تنظير جلدي يدوي، "
             "تقرير شخصي وخطّة متابعة مكتوبة.",
             "€ 180"),
            ("رسم خرائط الشامات الرقمي",
             "60 دقيقة · FotoFinder ATBM",
             "تصوير جلدي بالفيديو عالي الدقة لكلّ شامة، أرشفة رقمية، "
             "مقارنة مع السجل التاريخي، تقرير مفصّل بالآفات ذات الخطورة.",
             "€ 240"),
            ("جراحة جلدية نهارية",
             "حسب المؤشر · نهارية",
             "استئصال الآفات المشبوهة تحت التخدير الموضعي، فحص نسيجي "
             "مرضي بواسطة مختبر متخصص، تقرير خلال ثمانية أيام عمل مع "
             "استشارة هاتفية مخصصة.",
             "ابتداءً من € 320"),
            ("ليزر CO2 المجزّأ",
             "45 دقيقة · جلسة واحدة",
             "علاج الندوب والتجاعيد حول الفم والبقع الشمسية والتقرّنات "
             "الشمسية بنظام Lumenis UltraPulse. الجلسة الأولى دائماً بعد "
             "استشارة جلدية مخصصة.",
             "€ 420"),
            ("تقشير طبي جلدي",
             "30 دقيقة · دورة 4 جلسات",
             "تقشير سطحي ومتوسط (TCA، مندليك، ساليسيليك، فينول "
             "مخفف) يُنفَّذ شخصياً من طبيبة الأمراض الجلدية، وفق بروتوكول "
             "مخصص حسب النمط الضوئي والضرر الشمسي.",
             "€ 260 / جلسة"),
            ("برنامج الوقاية السنوي",
             "سنوي · 3 مواعيد",
             "استشارة شاملة، رسم خرائط مع مقارنة تاريخية، استشارة "
             "حماية ضوئية شخصية، خط مباشر مع الطبيب للحالات الطفيفة "
             "خلال العام.",
             "€ 580"),
        ],

        "footnote":
            "جميع المدفوعات قابلة للخصم كمصاريف صحية. تُصدر العيادة "
            "إيصالاً صحياً بطابع ضريبي. تقديرات الجراحة دائماً مكتوبة "
            "وموقَّعة من الطبيب مسبقاً، شاملة الفحوص النسيجية "
            "وزيارات المتابعة.",
        "footnote_heading": "ملاحظات إدارية",

        "cta_heading":
            "كلّ استشارة في Studio Ricciardi <em>يُعدّها الطبيب شخصياً</em>.",
        "cta_primary_label":   "نموذج الطلب →",
        "cta_secondary_label": "الخط المباشر للسكرتارية →",
    },

    # ─── الأطباء (team) ──────────────────────────────────────
    "medici": {
        "eyebrow":  "الأطباء",
        "headline": "ثلاث توقيعات، <em>غرفة عمليات واحدة.</em>",
        "intro":
            "تتكوّن العيادة من ثلاث طبيبات أمراض جلدية يتشاركن الملفات "
            "والأرشيف الجلدي والبروتوكول السريري. لكنّ كلّ مريض يحتفظ "
            "دائماً بطبيبة مرجعية واحدة.",

        "portrait_city": "روما · فيا فينيتو",

        "doctors": [
            {
                "name":  "الدكتورة أليساندرا ريتشاردي",
                "role":  "المديرة السريرية · طبيبة أمراض جلدية",
                "tags":  ["التنظير الجلدي المتقدم", "أورام الجلد", "طب الجلد السريري"],
                "bio":
                    "متخصصة في طب الأمراض الجلدية والتناسلية من "
                    "Università Cattolica del Sacro Cuore في روما، "
                    "أكملت تدريباً متقدماً في التنظير الجلدي في Memorial "
                    "Sloan Kettering في نيويورك. عضو في SIDeMaST "
                    "و EADV و International Dermoscopy Society. مؤلفة "
                    "لأكثر من خمسين بحثاً مفهرساً، بما فيها فصلان من كتاب "
                    "Bolognia-Italia المرجعي.",
                "portrait": _CHIEF_PORTRAIT,
                "links": [("PubMed", "#"), ("ORCID", "#")],
            },
            {
                "name":  "الدكتور إيمانويلي فيتالي",
                "role":  "طبيب أمراض جلدية · جراحة جلدية",
                "tags":  ["جراحة نهارية", "ترميم تجميلي", "أمراض الجلد النسيجية"],
                "bio":
                    "تدرّب في Policlinico Gemelli في روما، وأكمل تدريباً "
                    "متقدماً في الجراحة الجلدية في Charité في برلين. "
                    "منذ 2015 مسؤول عن غرفة العمليات النهارية في العيادة. "
                    "مستشار جراحي لقسمين جامعيين لطب الأمراض الجلدية "
                    "في روما.",
                "portrait": _DR_VITALI_PORTRAIT,
                "links": [("السيرة الذاتية", "#")],
            },
            {
                "name":  "الدكتورة كاتيرينا موريلّي",
                "role":  "طبيبة أمراض جلدية · تجميل وليزر",
                "tags":  ["ليزر CO2", "طب تجميلي", "تقشير طبي"],
                "bio":
                    "تدرّبت في جامعة بادوا، دكتوراه في طب الجلد التجميلي. "
                    "أكملت تدريباً متقدماً في العلاج بالليزر في Wellman "
                    "Center في بوسطن. منذ 2024 مسؤولة عن مسار طب الجلد "
                    "التجميلي في Studio Ricciardi. لا تفويض لغير الأطباء.",
                "portrait": _DR_MORELLI_PORTRAIT,
                "links": [("المنشورات", "#")],
            },
        ],
    },

    # ─── المنشورات ────────────────────────────────────────────
    "pubblicazioni": {
        "eyebrow":  "المنشورات والقراءات",
        "headline": "أعمال علمية، <em>قراءات نقدية</em>، تثقيف جلدي.",
        "intro":
            "مختارات من أعمال العيادة ومن النصوص التثقيفية المكتوبة "
            "للجمهور العام. جميع المحتويات يُراجعها شخصياً "
            "الدكتورة ريتشاردي قبل النشر.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Studio Ricciardi · طب الجلد المتكامل",
        "empty_body_fallback_paragraphs": [
            "المقال قيد الإعداد التحريري. سيتوفر النص الكامل قريباً.",
            "يصف هذا الموضع صوت المقال: مذكّرة سريرية كتبتها طبيبة "
            "الأمراض الجلدية بأسلوب مباشر خالٍ من المصطلحات المتخصصة، "
            "موجّهة للمرضى والعائلات الباحثين عن معلومات موثوقة.",
        ],
    },

    "posts": [
        {
            "slug":     "mappatura-nei-quando-farla",
            "kicker":   "الوقاية",
            "title":    "رسم خرائط الشامات: كم مرة يجب إجراؤه فعلاً؟",
            "date":     "18 مارس 2026",
            "read_min": 7,
            "author":   "الدكتورة أليساندر�� ريتشاردي",
            "lede":
                "السؤال الأكثر تكراراً في العيادة هو أيضاً ذو الإجابة "
                "الأكثر دقّةً وتعقيداً. لا توجد وتيرة عالمية: بل يوجد "
                "نمطك الضوئي، وأرشيفك، وتاريخك العائلي.",
            "body": [
                ("p", "كلّ عام في إيطاليا يُشخَّص نحو خمسة عشر ألف حالة جديدة "
                      "من الورم الميلانيني الجلدي. إنه سرطان الجلد الأكثر فتكاً "
                      "وفي الوقت نفسه الأفضل توقعاً حين يُكشَف مبكراً. الحدّ "
                      "الفاصل بين هاتين الحقيقتين يُسمّى التنظير الجلدي الرقمي "
                      "المتسلسل."),
                ("h2", "ثلاث فئات خطورة"),
                ("ol", [
                    "مريض بدون تاريخ عائلي، شامات قليلة (أقل من 30)، نمط ضوئي II–III: رسم خرائط كل 24 شهراً.",
                    "مريض بشامات كثيرة (أكثر من 50)، بشرة فاتحة أو حروق شمسية في الطفولة: رسم خرائط سنوي.",
                    "مريض بتاريخ عائلي من الدرجة الأولى للورم الميلانيني أو شامة مشبوهة في الأرشيف: رسم خرائط كل ستة إلى اثني عشر شهراً.",
                ]),
                ("p", "هذه الفترات ليست قواعد جامدة: يُكيّفها كلّ طبيب أمراض "
                      "جلدية حسب المريض. المهم أن يكون رسم الخرائط فعلاً سريرياً "
                      "متكرراً عبر الزمن — بالأجهزة نفسها والطبيب نفسه والأرشيف "
                      "الرقمي نفسه."),
                ("h2", "ماذا يعني «أرشيف رقمي»"),
                ("p", "يعني أن كلّ شامة تُصوَّر بالتنظير الجلدي عالي الدقة "
                      "وتُحفَظ بإحداثيات جلدية دقيقة. في كلّ مراجعة لاحقة، "
                      "لا ينظر الطبيب إلى شامة جديدة: بل يقارن الصورة نفسها "
                      "مع صورة العام الماضي. التغيّر — لا الصورة المنفردة — هو "
                      "ما يولّد الشبهة السريرية."),
                ("blockquote",
                 "رسم خرائط الشامات لا يهدف إلى العثور على ورم ميلانيني. "
                 "بل يهدف إلى معرفة كيف كانت كلّ آفة في العام الماضي. "
                 "إنه فعل ذاكرة سريرية قبل أن يكون فعل تشخيص."),
                ("p", "بالنسبة للمرضى الجدد، يكون أول رسم خرائط دائماً فعلاً "
                      "تأسيسياً: صور اليوم تصبح المرجع للسنوات العشر القادمة. "
                      "تستحق ساعة كاملة من الوقت السريري، ونصف الاستشارة الأولى "
                      "مكرَّس لها."),
            ],
        },
        {
            "slug":     "chirurgia-dermatologica-ambulatoriale",
            "kicker":   "جراحة جلدية",
            "title":    "الجراحة الجلدية النهارية: ماذا تتوقع فعلاً؟",
            "date":     "2 مارس 2026",
            "read_min": 5,
            "author":   "الدكتور إيمانويلي فيتالي",
            "lede":
                "عمليات الاستئصال الجلدي النهارية مخيفة فقط حتى لحظة "
                "التخدير. بعدها، في 95% من الحالات، يغادر المريض العيادة "
                "بنفس المشية التي دخل بها.",
        },
        {
            "slug":     "laser-co2-cicatrici",
            "kicker":   "ليزر جلدي",
            "title":    "ليزر CO2 المجزّأ: متى يكون الخيار الصحيح للندوب؟",
            "date":     "15 فبراير 2026",
            "read_min": 6,
            "author":   "الدكتورة كاتيرينا موريلّي",
            "lede":
                "ليزر CO2 المجزّأ لا يمحو الندوب: بل يعيد تشكيلها. فهم هذا "
                "الفرق هو الخطوة الأولى نحو خيار واقعي بعيد عن التوقعات "
                "غير القابلة للتحقيق.",
        },
        {
            "slug":     "fotoprotezione-quotidiana",
            "kicker":   "الوقاي��",
            "title":    "الحماية الضوئية اليومية: القواعد الثلاث التي تهمّ فعلاً",
            "date":     "28 يناير 2026",
            "read_min": 4,
            "author":   "الدكتورة أليساندرا ريتشاردي",
            "lede":
                "واقي شمسي SPF 50 بكمية خاطئة يعادل SPF 15 بكمية صحيحة. "
                "بعد خمسة عشر ألف استشارة جلدية، 80% من المرضى يرتكبون "
                "الخطأ نفسه دائماً.",
        },
        {
            "slug":     "medicina-estetica-dermatologica",
            "kicker":   "التجميل السريري",
            "title":    "لماذا في Studio Ricciardi لا يُمارس التجميل إلا طبيب الأمراض الجلدية",
            "date":     "10 يناير 2026",
            "read_min": 5,
            "author":   "الدكتورة كاتيرينا موريلّي",
            "lede":
                "الطب التجميلي الجلدي ليس مهمة تُفوَّض. موقف حازم نشرحه "
                "للمرضى منذ الزيارة الأولى، بوضوح تام.",
        },
    ],

    # ─── تواصل (contact) ─────────────────────────────────────
    "contatti": {
        "eyebrow":  "تواصل",
        "headline": "سكرتارية واحدة، <em>شخص واحد</em> على الطرف الآخر من الخط.",
        "intro":
            "تردّ العيادة شخصياً على المكالمات الهاتفية من الاثنين إلى "
            "الجمعة. السكرتارية السريرية بإدارة السيدة بيانكا مارتيلّي، "
            "التي تعرف كلّ ملف وكلّ مريض بالاسم منذ أكثر من عشر سنوات.",

        "blocks": [
            ("العنوان",    "Via Veneto 116", "00187 روما · الداخلي 3، السلم A"),
            ("الهاتف",     "+39 06 487 2311",   "ردّ مباشر 10:00 – 20:00"),
            ("البريد الإلكتروني", "studio@ricciardidermatologia.it", "ردّ خلال 24 ساعة عمل"),
            ("الطوارئ",    "+39 339 221 7080",  "خط مخصص للمرضى المتابَعين"),
        ],

        "hours": [
            ("الاثنين",    "10:00 – 14:00", "15:30 – 20:00"),
            ("الثلاثاء",   "10:00 – 14:00", "15:30 – 20:00"),
            ("الأربعاء",   "10:00 – 14:00", "15:30 – 20:00"),
            ("الخميس",    "10:00 – 14:00", "15:30 – 20:00"),
            ("الجمعة",    "10:00 – 14:00", "15:30 – 19:00"),
            ("السبت",     "جراحة بموعد مسبق", "عمليات مجدولة فقط"),
            ("الأحد",     "مغلق", "—"),
        ],

        "transport": [
            ("المترو",   "الخط A · محطة Barberini، 7 دقائق سيراً"),
            ("السيارة",  "موقف Saba Ludovisi (اتفاقية)، المدخل من Via Sicilia"),
            ("القطار",   "محطة Roma Termini · 11 دقيقة بسيارة أجرة"),
        ],

        "form_title": "اكتب إلى العيادة",
        "form_intro":
            "للاستفسارات غير العاجلة — معلومات عن العلاجات، الأسعار، "
            "التحضير لرسم خرائط الشامات — اكتب لنا أدناه. تردّ "
            "السكرتارية السريرية شخصياً.",

        "hours_heading":     "ساعات العمل",
        "transport_heading": "كيف تصل إلينا",

        "form_placeholders": {
            "first_name": "فاطمة",
            "last_name":  "الأحمد",
            "email":      "fatima@email.com",
            "phone":      "+966 5 ...",
            "subject":    "استفسار عن الاستشارة الجلدية الأولى",
            "message":
                "كن موجزاً — ستتواصل معك السكرتارية خلال 24 ساعة عمل.",
        },
    },

    # ──��� طلب موعد (appointment) ──────────────────────────────
    "richiedi-visita": {
        "eyebrow":  "طلب استشارة جلدية",
        "headline": "الاستشارة الجلدية <em>لا تُحجَز</em>: بل تُحضَّر.",
        "intro":
            "لا يوجد تقويم إلكتروني. تحتفظ العيادة بكلّ زيارة أولى بعد "
            "قراءة وصف موجز للحالة. تُقيَّم الطلبات شخصياً من الطبيب "
            "خلال 48 ساعة عمل.",

        "process_label":   "كيف يعمل النظام",
        "process_heading":
            "أربع خطوات، في <em>ثمانٍ وأربعين ساعة عمل.</em>",

        "process": [
            ("01", "املأ النموذج",
             "عشرة أسطر تكفي لوصف حالتك. إذا كانت لديك آفات مشبوهة، "
             "أرفق صورة: تساعد في تقييم الأولوية مسبقاً."),
            ("02", "قراءة سريرية",
             "يقرأ الطبيب الطلب شخصياً خلال 48 ساعة عمل ويحدّد ما إذا "
             "كانت الزيارة الأولى تتعلق بطب الجلد السريري أو الجراحي "
             "أو التجميلي."),
            ("03", "اقتراح موعد",
             "تقترح السكرتارية فترتين زمنيتين متوافقتين مع تفضيلاتك "
             "ومدّة الاستشارة (40 دقيقة للاستشارة العامة، 60 دقيقة "
             "لرسم خرائط الشامات الكامل)."),
            ("04", "التأكيد والتحضير",
             "تتلقى عبر البريد الإلكتروني قائمة بما يجب إحضاره (فحوصات "
             "سابقة، صور الآفات، العلاج الحالي) وتعليمات عملية — بدون "
             "مكياج وبدون طلاء أظافر إذا كان مخططاً لرسم الخرائط."),
        ],

        "form_title": "نموذج الطلب",
        "form_band_side_note":
            "خصّص بضع دقائق. الطلبات المُعَدّة بعناية تقرأها الطبيبة "
            "بالكامل — المتسرعة، لا.",
        "form_band_side_note_small": "↓ نموذج مخصص",

        "form_fields": [
            {"label": "الاسم الكامل", "placeholder": "فاطمة الأحمد",
             "type": "text", "full_width": False},
            {"label": "البريد الإلكتروني", "placeholder": "fatima@email.com",
             "type": "email", "full_width": False},
            {"label": "اله��تف", "placeholder": "+966 5 ...",
             "type": "tel", "full_width": False},
            {"label": "العمر", "placeholder": "38",
             "type": "number", "full_width": False},
            {"label": "نوع الاستشارة", "type": "select", "full_width": False,
             "options": ["استشارة جلدية", "رسم خرائط الشامات",
                         "جراحة جلدية", "طب تجميلي"]},
            {"label": "التوقيت المفضل", "type": "select", "full_width": False,
             "options": ["صباحاً", "بعد الظهر", "لا تفضيل"]},
            {"label": "الطبيب المعالج", "placeholder": "د. ...",
             "type": "text", "full_width": True},
            {"label": "وصف موجز للحالة",
             "placeholder":
                 "سبب الزيارة، الآفات محلّ الاهتمام، الأعراض الأخيرة، "
                 "العلاجات الجارية. لا تتجاوز عشرة أسطر.",
             "type": "textarea", "full_width": True},
        ],

        "submit_label": "إرسال الطلب",

        "consent":
            "أوافق على معالجة بياناتي الشخصية وفقاً لسياسة الخصوصية "
            "بموجب اللائحة الأوروبية 679/2016. تُحفَظ البيانات السريرية "
            "والصور الجلدية في أرشيف رقمي مشفَّر لا يصل إليه سوى "
            "الطبيب المعالج.",

        "footnote":
            "لا تردّ العيادة على الطلبات المجهولة ولا تُصدر آراءً سريرية "
            "عبر البريد الإلكتروني بدون استشارة. للاستفسارات الإدارية "
            "(الأسعار، المواعيد، المواقف) استخدم صفحة التواص��.",
    },
}
