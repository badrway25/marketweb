"""Cardio i18n pilot — EN / FR / ES / AR content blocks.

Session 23, Phase 2i.1. This file isolates the non-IT locale trees for
`cardio-studio-specialistico` so the main `template_content.py` stays
readable. The IT block is the authoritative source and remains inline
in `template_content.py` (keyed as `CARDIO_CONTENT_IT`).

Authoring rules
---------------
- Locale-specific editorial voice — NOT literal word-for-word translation
  of the Italian copy. Cardiology discourse shifts per market:
  - EN: Anglo-American clinical tone, direct and unembellished.
  - FR: classical French medical prose, "vous" register, a little more
    formal than EN.
  - ES: Spanish peninsular register, warm yet precise.
  - AR: Modern Standard Arabic, formal medical register, RTL-aware
    punctuation (Arabic comma ، and question mark ؟ where appropriate).
- Non-localizable data (phone, email, address, years, prices, doctor
  portrait URLs, press outlets) is repeated as-is across locales.
  A Roma clinic's address is "Viale Parioli 142" in every language.
- The `pages` list preserves the same slugs + kinds across locales —
  only the labels are translated.
- Doctor names, dates, and press outlets stay in the original script.
  Arabic renders them as-is (mixed-script is handled by the RTL shell).
- Quality floor: no machine translation, no placeholder strings, no
  half-sentences. Every section must read as if authored by a native
  speaker working for a premium cardiology practice in Rome.
"""
from __future__ import annotations

from typing import Any


# Shared non-localizable helpers — repeated verbatim in every locale block
# so the content trees stay flat (no shared refs = no shared-reference bugs).
_CHIEF_PORTRAIT = (
    "https://images.unsplash.com/photo-1559757148-5c350d0d3c56"
    "?auto=format&fit=crop&w=900&q=80"
)
_DR_MARANI_PORTRAIT = (
    "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d"
    "?auto=format&fit=crop&w=900&q=80"
)
_DR_SALIERI_PORTRAIT = (
    "https://images.unsplash.com/photo-1559839734-2b71ea197ec2"
    "?auto=format&fit=crop&w=900&q=80"
)
_DR_LOMBARDI_PORTRAIT = (
    "https://images.unsplash.com/photo-1622253692010-333f2da6031d"
    "?auto=format&fit=crop&w=900&q=80"
)
_LEAD_IMAGE = (
    "https://images.unsplash.com/photo-1576091160550-2173dba999ef"
    "?auto=format&fit=crop&w=900&q=80"
)


# ===========================================================================
# ENGLISH
# ===========================================================================

CARDIO_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Practice",       "kind": "home"},
        {"slug": "studio",          "label": "The Practice",   "kind": "about"},
        {"slug": "visite",          "label": "Consultations",  "kind": "services"},
        {"slug": "medici",          "label": "Team",           "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Publications",   "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contact",        "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Book a visit",   "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "M",
        "logo_word":    "Studio Marani",
        "tag":          "Clinical cardiology · Rome Parioli",
        "phone":        "+39 06 320 1144",
        "email":        "studio@maranicardiologia.it",
        "address":      "Viale Parioli 142 · 00197 Rome",
        "hours_compact": "Mon – Fri · 9:00 – 19:00",
        "hours_footer_rows": [
            "Saturday · on-call only",
            "Sunday · closed",
        ],
        "license":      "Rome Medical Board no. 12 / 4408",
        "footer_intro":
            "A private specialist practice in clinical cardiology and "
            "cardiovascular prevention. By appointment only.",
    },

    "home": {
        "hero_variant": "split-consultive",
        "eyebrow":  "Clinical cardiology · Rome Parioli",
        "headline": "A <em>tailored cardiology</em>, for those who refuse shortcuts.",
        "intro":
            "Specialist consultations, second opinions, individual prevention "
            "programmes. One schedule, one physician, one signature.",
        "primary_cta":   "Request a private visit",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "The practice",
        "secondary_href":"studio",

        "facts": [
            ("15",    "years of private clinical practice"),
            ("1,200", "specialist consultations per year"),
            ("4",     "partner hospitals across Rome"),
        ],

        "manifesto_drop_cap": "C",
        "manifesto":
            "ardiology is not an assembly line. It is a long conversation — "
            "patient history taken slowly, exams read twice, follow-up phone "
            "calls from the doctor himself. For fifteen years Studio Marani "
            "has accompanied public and private patients through a "
            "cardiovascular prevention journey built around the person, "
            "with discretion and with method.",

        "signature_visits": [
            ("01", "Complete cardiology consultation",
             "Extended anamnesis, ECG, personal reporting and a written "
             "follow-up timeline tailored to the patient."),
            ("02", "Specialist second opinion",
             "For patients with complex diagnoses or multiple ongoing "
             "therapies — read dossier in hand, together with the "
             "referring physician."),
            ("03", "Prevention programme",
             "Six months of integrated monitoring with a dietitian and "
             "sports physician, indicated for families with a history of "
             "early cardiovascular events."),
            ("04", "Holter & echocardiography",
             "24-hour cardiac recording and transthoracic echocardiogram, "
             "reported the same day, on site."),
        ],

        "chief": {
            "name":  "Dr. Riccardo Marani",
            "role":  "Clinical director · Cardiologist",
            "bio":
                "Trained in cardiology at the University La Sapienza of Rome "
                "and specialised at the Institut de Cardiologie de Montréal. "
                "Member of the Italian Society of Cardiology and of the "
                "European Society of Cardiology. Author of over forty "
                "peer-reviewed publications.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "press": ["LANCET", "European Heart Journal", "Corriere Salute",
                  "Sole 24 Ore", "RAI Med"],
        "press_label": "Featured in",

        "hero_sidebar_top_label": "Clinical direction",
        "hero_sidebar_quote":
            "“Cardiology is not an assembly line. "
            "It is a long conversation, made of time.”",
        "hero_sidebar_author": "— Lancet · 2024",
        "hero_sidebar_pulse": [
            ("Practice", "Rome · Parioli"),
            ("Since",    "2010"),
            ("Focus",    "Clinical cardiology"),
        ],

        "signature_visits_label":   "Consultations & programmes",
        "signature_visits_heading": "Six clinical pathways, <em>a single signature.</em>",
        "signature_visits_intro":
            "Four of the practice's most requested consultations. "
            "The complete list is on the Consultations page.",

        "chief_label":   "Clinical direction",
        "chief_heading": "One signature <em>on every chart.</em>",

        "tecnologie": {
            "label": "Technology & equipment",
            "heading": "State-of-the-art <em>diagnostics</em>, in-house.",
            "items": [
                {"icon": "ecg", "title": "12-lead ECG", "desc": "Resting electrocardiogram with immediate reporting and historical comparison."},
                {"icon": "echo", "title": "Philips EPIQ 7 echocardiography", "desc": "2D and colour-Doppler cardiac ultrasound, reported on the same day."},
                {"icon": "holter", "title": "Schiller MT-200 Holter", "desc": "24-hour ECG recording with variability and silent arrhythmia analysis."},
                {"icon": "stress", "title": "Exercise stress test", "desc": "Cycle ergometer test with continuous blood-pressure monitoring."},
            ],
        },
        "testimonianza": {
            "quote": "For two years I looked for a cardiologist who would actually read my file before examining me. At Studio Marani they spent forty minutes on my records before even touching the stethoscope.",
            "author": "Practice patient",
            "context": "Second cardiology opinion · 2025",
        },
        "faq": {
            "label": "Frequently asked questions",
            "heading": "The questions <em>we hear most often.</em>",
            "items": [
                ("How long does a first cardiology visit last?", "A full first visit takes approximately forty-five minutes and includes history, physical examination, 12-lead ECG, reporting and discussion of the follow-up plan."),
                ("Do I need a GP referral?", "No. As a private specialist practice, no referral letter is required. A summary from your GP is helpful but not mandatory."),
                ("Can I bring test results from another hospital?", "Absolutely. Second opinions are one of our specialities. Please bring all reports, discharge letters and current prescriptions."),
                ("Is an echocardiogram painful?", "No, it is completely painless and non-invasive. The probe is placed on the chest with conductive gel. The exam takes about twenty to thirty minutes."),
                ("How does the prevention programme work?", "The six-month programme includes four scheduled visits, two ECGs, one 24-hour Holter, an integrated assessment with a dietician and sports physician, and a direct line to the practice physician."),
            ],
        },

        "cta_heading":
            "Every consultation is <em>personally arranged</em> with the physician.",
        "cta_primary_label":   "Request a private visit",
        "cta_secondary_label": "Practice contacts",
    },

    "studio": {
        "eyebrow":  "The practice",
        "headline": "Fifteen years of <em>independent clinical cardiology</em>.",
        "intro":
            "Studio Marani was founded in 2010 on the belief that cardiology "
            "deserves the dimension of slow time: forty-five-minute "
            "consultations, personal reporting, direct telephone follow-up "
            "from the physician.",

        "history": [
            ("2010",
             "Opening of the first premises on Viale Parioli — two rooms and "
             "a single secretary. The first fifteen clinical charts are still "
             "archived in their original paper form."),
            ("2014",
             "Convention with the Policlinico Umberto I for cases requiring "
             "admission or second-level interventional procedures."),
            ("2017",
             "Acquisition of a Philips EPIQ 7 echocardiograph of the latest "
             "generation and a Schiller MT-200 Holter system — same-day "
             "diagnostics become possible."),
            ("2020",
             "Set-up of a second consulting room dedicated to second opinions "
             "on multidisciplinary dossiers, with access to European "
             "teleconsultation."),
            ("2024",
             "Dr. Margherita Salieri joins as head of the familial "
             "cardiovascular prevention programme."),
        ],

        "studio_image":
            "https://images.unsplash.com/photo-1631815588090-d4bfec5b1ccb"
            "?auto=format&fit=crop&w=1400&q=80",
        "studio_image_caption": "Cardiology clinic · Viale Parioli, Rome",

        "method_title": "Method",
        "method_paragraphs": [
            "A visit at Studio Marani always begins with the file the patient "
            "brings along. Previous exams, discharge letters, referring "
            "physician's notes, current medication. Everything is read, "
            "annotated and discussed before the stethoscope is even picked up.",
            "History-taking lasts as long as it needs to — on average thirty-"
            "five minutes. From it flows a written clinical plan, handed to "
            "the patient in a recycled-paper folder, signed by the physician "
            "and carrying the timeline of follow-up checks.",
            "Every chart remains accessible to the patient for ten years and "
            "can be requested in copy at any time, including for transfer to "
            "another specialist.",
        ],

        "values": [
            ("Time",           "Forty-five minutes for every first visit, never less."),
            ("Independence",   "No affiliation with pharmaceutical companies or referral clinics."),
            ("Traceability",   "A complete clinical file, reconstructible at any point."),
            ("Discretion",     "Absolute confidentiality on data and on people."),
        ],

        "values_label":   "What we commit to",
        "values_heading": "Four promises that <em>never change.</em>",

        "cta_heading":
            "Would you like to meet the physicians <em>before booking?</em>",
        "cta_primary_label":   "The three physicians →",
        "cta_secondary_label": "Request a private visit →",
    },

    "visite": {
        "eyebrow":  "Consultations",
        "headline": "Six clinical pathways, <em>a single signature.</em>",
        "intro":
            "Every consultation at Studio Marani is a defined clinical "
            "pathway, with a written duration, price and follow-up plan.",

        "service_image":
            "https://images.unsplash.com/photo-1530497610245-94d3c16cda28"
            "?auto=format&fit=crop&w=1400&q=80",
        "service_image_caption": "Cardiac diagnostics · Studio Marani",

        "treatments": [
            ("Complete cardiology consultation",
             "45 min · first visit",
             "Extended anamnesis, physical examination, 12-lead "
             "electrocardiogram, personal reporting and a written follow-up plan.",
             "€ 220"),
            ("Follow-up consultation",
             "30 min · returning patients",
             "Therapy review, control ECG, reading of recent blood-work panels.",
             "€ 140"),
            ("Specialist second opinion",
             "60 min · dossier-based",
             "Complete reading of reports, diagnostic exams and existing "
             "clinical file, with a signed final report and reference "
             "bibliography.",
             "€ 280"),
            ("Transthoracic echocardiography",
             "30 min · on site",
             "Two-dimensional and colour-Doppler echocardiographic exam with "
             "the Philips EPIQ 7 system. Same-day reporting.",
             "€ 180"),
            ("24-hour Holter",
             "Recording + reading",
             "24-hour electrocardiographic monitoring with the Schiller "
             "MT-200 system, personal reading and reporting.",
             "€ 160"),
            ("Six-month prevention programme",
             "Annual journey",
             "Four scheduled visits, two ECGs, one Holter, integrated "
             "evaluation with a dietitian and a sports physician, direct "
             "access to the physician's channel.",
             "€ 980"),
        ],

        "footnote":
            "All payments are deductible as healthcare expenses. The practice "
            "issues a healthcare receipt with a revenue stamp. For patients "
            "living outside Rome, a package including remote follow-up "
            "teleconsultation can be arranged.",
        "footnote_heading": "Administrative notes",

        "cta_heading":
            "A consultation at Studio Marani is <em>personally arranged</em>.",
        "cta_primary_label":   "Booking form →",
        "cta_secondary_label": "Front-desk direct number →",
    },

    "medici": {
        "eyebrow":  "The team",
        "headline": "Three signatures, a single <em>clinical chart.</em>",
        "intro":
            "The practice is staffed by three cardiologists who share charts, "
            "methods and reporting standards. Each patient, however, always "
            "has a single referring physician.",

        "portrait_city": "Rome · Parioli",

        "doctors": [
            {
                "name":  "Dr. Riccardo Marani",
                "role":  "Clinical director · Cardiologist",
                "tags":  ["Cardiovascular prevention", "Second opinions", "Clinical cardiology"],
                "bio":
                    "Specialised in cardiology at the University La Sapienza of "
                    "Rome, further trained in clinical echocardiography at the "
                    "Institut de Cardiologie de Montréal. Member of SIC and ESC. "
                    "Author of over forty peer-reviewed publications, including "
                    "two chapters of the Italian edition of the Braunwald "
                    "cardiology textbook.",
                "portrait": _DR_MARANI_PORTRAIT,
                "links": [("PubMed", "#"), ("ORCID", "#")],
            },
            {
                "name":  "Dr. Margherita Salieri",
                "role":  "Cardiologist · Head of prevention",
                "tags":  ["Prevention programme", "Family cardiology", "Rehabilitation"],
                "bio":
                    "Graduated in Bologna, PhD in cardiovascular physiology at "
                    "the University of Padua. Since 2024, coordinator of the "
                    "familial cardiovascular prevention programme. Her clinical "
                    "focus is on perimenopausal women and on households with "
                    "a history of early cardiovascular events.",
                "portrait": _DR_SALIERI_PORTRAIT,
                "links": [("Curriculum", "#")],
            },
            {
                "name":  "Dr. Andrea Lombardi",
                "role":  "Cardiologist · Imaging diagnostics",
                "tags":  ["Echocardiography", "Holter", "Sports cardiology"],
                "bio":
                    "Specialised at Sant'Andrea hospital in Rome, further "
                    "trained in advanced echocardiography at Saint-Joseph in "
                    "Paris. Since 2018, reference physician for imaging "
                    "diagnostics at the practice. Cardiology consultant for "
                    "two Serie B football clubs.",
                "portrait": _DR_LOMBARDI_PORTRAIT,
                "links": [("Publications", "#")],
            },
        ],
    },

    "pubblicazioni": {
        "eyebrow":  "Publications & long-reads",
        "headline": "Scientific work, <em>critical readings</em>, clinical writing.",
        "intro":
            "A selection of the practice's publications and of the "
            "editorial pieces written for the general public. Every text "
            "is personally reviewed by Dr. Marani before publication.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Studio Marani · Clinical cardiology",
        "empty_body_fallback_paragraphs": [
            "Article in editorial preparation. The full text will be "
            "published shortly.",
            "This placeholder describes the voice of the article: a "
            "clinical note written by the physician, in a direct, "
            "jargon-free tone, intended for patients and family members "
            "looking for reliable information.",
        ],
    },

    "posts": [
        {
            "slug":     "secondo-parere-quando-richiederlo",
            "kicker":   "Clinical practice",
            "title":    "When a cardiology second opinion actually makes sense",
            "date":     "12 March 2026",
            "read_min": 6,
            "author":   "Dr. Riccardo Marani",
            "lede":
                "It is not a loss of trust in the first physician. It is an "
                "act of clinical hygiene that — when done well — protects "
                "the patient, the referring doctor, and the healthcare system.",
            "body": [
                ("p", "Every year the practice receives roughly two hundred "
                      "second-opinion requests. Almost always they come from "
                      "frightened patients: an unexpected diagnosis, a complex "
                      "therapy, a surgical recommendation. Our first job is to "
                      "lower the emotional temperature."),
                ("h2", "Three situations in which a second opinion is indicated"),
                ("ol", [
                    "A new, high-impact diagnosis received in the space of a few hours or in the emergency room.",
                    "A long-term pharmacological therapy with relevant side effects.",
                    "An indication for an invasive procedure (pacemaker implant, cardioversion, ablation)."
                ]),
                ("p", "In every other case — a routine yearly check, a minor "
                      "blood-pressure variation, an isolated episode of "
                      "palpitations — a long conversation with your own "
                      "cardiologist is almost always enough."),
                ("h2", "What to bring to a second opinion"),
                ("p", "A second opinion without paperwork is a wrong second "
                      "opinion. To do our job properly we need: the discharge "
                      "letter of the referring physician, every imaging exam "
                      "in the original format (ECG, echo, Holter, angiograms "
                      "if relevant), the last six months of blood-work, and "
                      "an updated list of current medication including "
                      "dosages and administration times."),
                ("blockquote",
                 "A second opinion does not replace your physician: it "
                 "accompanies him. When the two specialists talk to each "
                 "other, the patient wins twice."),
            ],
        },
        {
            "slug":     "prevenzione-familiare-cardiovascolare",
            "kicker":   "Prevention",
            "title":    "Familial cardiovascular prevention programme: what it really means",
            "date":     "27 February 2026",
            "read_min": 4,
            "author":   "Dr. Margherita Salieri",
            "lede":
                "Six months of integrated monitoring is not a sales package. "
                "It is a clinical tool for those with direct familial history "
                "of an early cardiovascular event.",
        },
        {
            "slug":     "ecocardiografia-quando-serve",
            "kicker":   "Diagnostics",
            "title":    "Transthoracic echocardiography: when it is really needed",
            "date":     "11 February 2026",
            "read_min": 5,
            "author":   "Dr. Andrea Lombardi",
            "lede":
                "Not every patient asking for an echo actually needs one. "
                "An honest guide to the real clinical indications and to the "
                "cases where the exam is redundant.",
        },
        {
            "slug":     "donne-cuore-perimenopausa",
            "kicker":   "Gender cardiology",
            "title":    "Women and the heart: the silence of perimenopause",
            "date":     "23 January 2026",
            "read_min": 7,
            "author":   "Dr. Margherita Salieri",
            "lede":
                "For decades cardiology protocols have been built around male "
                "patients. As a result, many women between forty-five and "
                "sixty still receive late or incorrect diagnoses today.",
        },
        {
            "slug":     "sport-amatoriale-controlli",
            "kicker":   "Sports cardiology",
            "title":    "Amateur sport: the heart screenings that actually matter",
            "date":     "8 January 2026",
            "read_min": 4,
            "author":   "Dr. Andrea Lombardi",
            "lede":
                "Three great myths about pre-sport cardiology screenings, "
                "from the physician who signs them daily for cyclists, "
                "runners and swimmers in their forties and fifties.",
        },
    ],

    "contatti": {
        "eyebrow":  "Contact",
        "headline": "One number, <em>one person</em> at the other end of the line.",
        "intro":
            "The practice answers phone calls in person from Monday to "
            "Friday. The clinical front desk is run by Ms Adele Petrucci, "
            "who knows every chart and every patient by name.",

        "blocks": [
            ("Address",    "Viale Parioli 142", "00197 Rome · stair B, interior 4"),
            ("Phone",      "+39 06 320 1144",   "Direct line 9:00 – 19:00"),
            ("Email",      "studio@maranicardiologia.it", "Reply within the same working day"),
            ("Emergencies","+39 335 642 8011",  "Reserved line for active patients"),
        ],

        "hours": [
            ("Monday",     "9:00 – 13:00", "15:00 – 19:00"),
            ("Tuesday",    "9:00 – 13:00", "15:00 – 19:00"),
            ("Wednesday",  "9:00 – 13:00", "15:00 – 19:00"),
            ("Thursday",   "9:00 – 13:00", "15:00 – 19:00"),
            ("Friday",     "9:00 – 13:00", "—"),
            ("Saturday",   "Closed to public", "On-call for active patients"),
            ("Sunday",     "Closed", "—"),
        ],

        "transport": [
            ("Metro", "Line B · Termini → bus 168, stop Parioli/Liegi"),
            ("Car",   "Partner parking Q-Park Parioli, entrance via Via Bertoloni"),
            ("Train", "Termini station · 12 minutes by taxi"),
        ],

        "form_title": "Write to the practice",
        "form_intro":
            "For non-urgent enquiries — information on visits, pricing, "
            "logistics — please use this form. The clinical front desk "
            "will reply in person.",

        "hours_heading":     "Opening hours",
        "transport_heading": "How to reach us",

        "form_placeholders": {
            "first_name": "Mark",
            "last_name":  "Smith",
            "email":      "mark.smith@email.com",
            "phone":      "+44 7 ...",
            "subject":    "Information on a follow-up visit",
            "message":
                "Keep it to a few lines — the front desk will reply the "
                "same working day.",
        },
    },

    "richiedi-visita": {
        "eyebrow":  "Private visit request",
        "headline": "A private visit <em>is not booked</em>: it is arranged.",
        "intro":
            "There is no online calendar. Every first consultation is "
            "reserved after the physician has read a short description "
            "of the case. Requests are personally evaluated within 48 "
            "working hours.",

        "process_label":   "How it works",
        "process_heading": "Four steps, across <em>four working days.</em>",

        "process": [
            ("01", "Fill in the form",
             "Ten lines are enough to frame your request. Attach recent "
             "exams if you wish — it saves asking for them twice."),
            ("02", "Clinical reading",
             "The physician personally reads the request within 48 "
             "working hours and decides whether the first visit falls "
             "within his expertise."),
            ("03", "Appointment proposal",
             "If it does, the front desk proposes two time slots that "
             "are compatible with your availability."),
            ("04", "Confirmation and dossier",
             "Once confirmed, you receive by email the list of documents "
             "to bring and the address of the practice with access notes."),
        ],

        "form_title": "Request form",
        "form_band_side_note":
            "Take a few minutes. Carefully written requests are read by "
            "the physician in full — rushed ones are not.",
        "form_band_side_note_small": "↓ Reserved form",

        "form_fields": [
            {"label": "Full name", "placeholder": "Mark Smith",
             "type": "text", "full_width": False},
            {"label": "Email", "placeholder": "mark@email.com",
             "type": "email", "full_width": False},
            {"label": "Phone", "placeholder": "+44 7 ...",
             "type": "tel", "full_width": False},
            {"label": "Age", "placeholder": "52",
             "type": "number", "full_width": False},
            {"label": "Type of visit", "type": "select", "full_width": False,
             "options": ["First visit", "Second opinion",
                         "Prevention programme", "Follow-up"]},
            {"label": "Preferred availability", "type": "select", "full_width": False,
             "options": ["Morning", "Afternoon", "Either"]},
            {"label": "Referring physician", "placeholder": "Dr. ...",
             "type": "text", "full_width": True},
            {"label": "Short description of the case",
             "placeholder":
                 "Symptoms, exams already performed, current diagnosis, "
                 "ongoing therapy. Keep it to ten lines.",
             "type": "textarea", "full_width": True},
        ],

        "submit_label": "Send request",

        "consent":
            "I consent to the processing of my personal data in accordance "
            "with the privacy notice and with EU Regulation 679/2016. "
            "Clinical data is held exclusively in the practice's paper "
            "archive.",

        "footnote":
            "The practice does not respond to anonymous requests and does "
            "not issue clinical opinions by email without a visit. For "
            "administrative enquiries (pricing, hours, parking) please use "
            "the contact page.",
    },
}


# ===========================================================================
# FRENCH
# ===========================================================================

CARDIO_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Cabinet",        "kind": "home"},
        {"slug": "studio",          "label": "Le cabinet",     "kind": "about"},
        {"slug": "visite",          "label": "Consultations",  "kind": "services"},
        {"slug": "medici",          "label": "Médecins",       "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Publications",   "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contact",        "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Demander un RDV","kind": "appointment"},
    ],

    "site": {
        "logo_initial": "M",
        "logo_word":    "Studio Marani",
        "tag":          "Cardiologie clinique · Rome Parioli",
        "phone":        "+39 06 320 1144",
        "email":        "studio@maranicardiologia.it",
        "address":      "Viale Parioli 142 · 00197 Rome",
        "hours_compact": "Lun – Ven · 9h – 19h",
        "hours_footer_rows": [
            "Samedi · garde téléphonique",
            "Dimanche · fermé",
        ],
        "license":      "Ordre des Médecins de Rome 12 / 4408",
        "footer_intro":
            "Cabinet privé spécialisé en cardiologie clinique et "
            "prévention cardiovasculaire. Uniquement sur rendez-vous.",
    },

    "home": {
        "hero_variant": "split-consultive",
        "eyebrow":  "Cardiologie clinique · Rome Parioli",
        "headline": "Une cardiologie <em>sur mesure</em>, pour celles et ceux qui refusent les raccourcis.",
        "intro":
            "Consultations spécialisées, seconds avis, programmes de "
            "prévention individuelle. Un seul agenda, un seul médecin, "
            "une seule signature.",
        "primary_cta":   "Demander une consultation privée",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "Le cabinet",
        "secondary_href":"studio",

        "facts": [
            ("15",    "années de pratique clinique privée"),
            ("1 200", "consultations spécialisées par an"),
            ("4",     "hôpitaux de référence à Rome"),
        ],

        "manifesto_drop_cap": "L",
        "manifesto":
            "a cardiologie n'est pas une chaîne de montage. C'est un dialogue "
            "au long cours, fait d'une anamnèse patiente, d'examens relus "
            "deux fois, de temps donné. Depuis quinze ans, le Studio Marani "
            "accompagne patients publics et privés dans un parcours de "
            "prévention cardiovasculaire construit sur mesure — avec "
            "discrétion et méthode.",

        "signature_visits": [
            ("01", "Consultation cardiologique complète",
             "Anamnèse approfondie, ECG, compte-rendu personnel et plan "
             "de suivi personnalisé remis en main propre."),
            ("02", "Second avis spécialisé",
             "Pour les patients avec un diagnostic complexe ou des "
             "thérapies multiples en cours — dossier lu avec le "
             "médecin traitant."),
            ("03", "Programme de prévention",
             "Six mois de suivi intégré avec diététicien et médecin du "
             "sport, indiqué pour les familles avec antécédents "
             "cardiovasculaires précoces."),
            ("04", "Holter & échocardiographie",
             "Enregistrement cardiaque de 24 heures et échocardiographie "
             "transthoracique, compte-rendu remis dans la journée, sur place."),
        ],

        "chief": {
            "name":  "Dr. Riccardo Marani",
            "role":  "Directeur clinique · Cardiologue",
            "bio":
                "Spécialiste en cardiologie à l'Université La Sapienza de "
                "Rome, perfectionné à l'Institut de Cardiologie de Montréal. "
                "Membre de la Société Italienne de Cardiologie et de la "
                "Société Européenne de Cardiologie. Auteur de plus de "
                "quarante publications indexées.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "press": ["LANCET", "European Heart Journal", "Corriere Salute",
                  "Sole 24 Ore", "RAI Med"],
        "press_label": "Publié dans",

        "hero_sidebar_top_label": "Direction clinique",
        "hero_sidebar_quote":
            "« La cardiologie n'est pas une chaîne de montage. "
            "C'est un dialogue au long cours, fait de temps. »",
        "hero_sidebar_author": "— Lancet · 2024",
        "hero_sidebar_pulse": [
            ("Cabinet",  "Rome · Parioli"),
            ("Depuis",   "2010"),
            ("Référence","Cardiologie clinique"),
        ],

        "signature_visits_label":   "Consultations & parcours",
        "signature_visits_heading": "Six parcours cliniques, <em>une seule signature.</em>",
        "signature_visits_intro":
            "Quatre des consultations les plus demandées du cabinet. "
            "La liste complète se trouve à la page Consultations.",

        "chief_label":   "Direction clinique",
        "chief_heading": "Une seule signature <em>sur chaque dossier.</em>",

        "tecnologie": {
            "label": "Technologies & équipements",
            "heading": "Diagnostic de <em>dernière génération</em>, au cabinet.",
            "items": [
                {"icon": "ecg", "title": "ECG à 12 dérivations", "desc": "Électrocardiogramme de repos avec compte rendu immédiat et comparaison historique."},
                {"icon": "echo", "title": "Échocardiographie Philips EPIQ 7", "desc": "Échographie cardiaque 2D et Doppler couleur de dernière génération, résultat le jour même."},
                {"icon": "holter", "title": "Holter Schiller MT-200", "desc": "Enregistrement ECG sur 24 heures avec analyse de la variabilité et des arythmies silencieuses."},
                {"icon": "stress", "title": "Épreuve d'effort", "desc": "Test sur cyclo-ergomètre avec surveillance continue de la pression artérielle."},
            ],
        },
        "testimonianza": {
            "quote": "J'ai cherché pendant deux ans un cardiologue qui lise vraiment mon dossier avant de m'examiner. Au Studio Marani, ils ont passé quarante minutes sur mes résultats avant même de toucher le stéthoscope.",
            "author": "Patient du cabinet",
            "context": "Deuxième avis cardiologique · 2025",
        },
        "faq": {
            "label": "Questions fréquentes",
            "heading": "Les questions que <em>l'on nous pose le plus souvent.</em>",
            "items": [
                ("Combien de temps dure une première consultation ?", "Une première consultation complète dure environ quarante-cinq minutes et comprend l'anamnèse, l'examen clinique, un ECG à 12 dérivations, le compte rendu et la discussion du plan de suivi."),
                ("Faut-il une ordonnance du médecin traitant ?", "Non. En tant que cabinet spécialisé privé, aucune lettre d'adressage n'est nécessaire. Un courrier du médecin traitant est utile mais non obligatoire."),
                ("Puis-je apporter des examens d'un autre hôpital ?", "Bien sûr. Le deuxième avis est l'une de nos spécialités. Apportez tous les comptes rendus, lettres de sortie et traitements en cours."),
                ("L'échocardiogramme est-il douloureux ?", "Non, c'est un examen totalement indolore et non invasif. La sonde est posée sur la poitrine avec un gel conducteur. L'examen dure environ vingt à trente minutes."),
                ("Comment fonctionne le programme de prévention ?", "Le programme semestriel comprend quatre consultations programmées, deux ECG, un Holter de 24 heures, un bilan intégré avec un diététicien et un médecin du sport, et un canal direct avec le médecin du cabinet."),
            ],
        },

        "cta_heading":
            "Chaque consultation est <em>convenue personnellement</em> avec le médecin.",
        "cta_primary_label":   "Demander une consultation privée",
        "cta_secondary_label": "Contacter le cabinet",
    },

    "studio": {
        "eyebrow":  "Le cabinet",
        "headline": "Quinze ans de <em>cardiologie clinique</em> indépendante.",
        "intro":
            "Le Studio Marani est né en 2010 de l'idée de rendre à la "
            "cardiologie sa dimension de temps long : consultations de "
            "quarante-cinq minutes, compte-rendu personnel, suivi "
            "téléphonique direct du médecin.",

        "history": [
            ("2010",
             "Ouverture du premier cabinet Viale Parioli, deux salles et "
             "une secrétaire. Les quinze premiers dossiers sont encore "
             "archivés sous leur forme papier d'origine."),
            ("2014",
             "Convention avec le Policlinico Umberto I pour les cas "
             "nécessitant une hospitalisation ou des procédures "
             "interventionnelles de second niveau."),
            ("2017",
             "Acquisition d'un échocardiographe Philips EPIQ 7 de dernière "
             "génération et d'un Holter Schiller MT-200 pour le diagnostic "
             "dans la journée."),
            ("2020",
             "Ouverture d'une seconde salle de consultation dédiée aux "
             "seconds avis sur dossiers multidisciplinaires, avec accès "
             "aux téléconsultations européennes."),
            ("2024",
             "Arrivée du Dr. Margherita Salieri comme responsable du "
             "programme de prévention cardiovasculaire familiale."),
        ],

        "studio_image":
            "https://images.unsplash.com/photo-1631815588090-d4bfec5b1ccb"
            "?auto=format&fit=crop&w=1400&q=80",
        "studio_image_caption": "Cabinet de cardiologie · Viale Parioli, Rome",

        "method_title": "Méthode",
        "method_paragraphs": [
            "Une consultation au Studio Marani commence toujours par le "
            "dossier que le patient apporte avec lui. Examens antérieurs, "
            "lettres de sortie, notes du médecin traitant, thérapies en "
            "cours : tout est lu, annoté et discuté avant même de saisir "
            "le stéthoscope.",
            "L'anamnèse dure le temps qu'il faut : en moyenne trente-cinq "
            "minutes. Elle donne lieu à un plan clinique écrit, remis en "
            "main propre dans un dossier en papier recyclé, signé par le "
            "médecin et portant le calendrier des contrôles à venir.",
            "Chaque dossier reste accessible au patient pendant dix ans "
            "et peut être demandé en copie à tout moment, y compris pour "
            "transfert vers un autre spécialiste.",
        ],

        "values": [
            ("Temps",           "Quarante-cinq minutes pour chaque première consultation, jamais moins."),
            ("Indépendance",    "Aucune affiliation à des laboratoires ni à des cliniques conventionnées."),
            ("Traçabilité",     "Dossier clinique complet, reconstructible à tout moment."),
            ("Discrétion",      "Confidentialité absolue sur les données et sur les personnes."),
        ],

        "values_label":   "Ce à quoi nous nous engageons",
        "values_heading": "Quatre engagements qui <em>ne changent jamais.</em>",

        "cta_heading":
            "Souhaitez-vous connaître l'équipe médicale <em>avant de réserver ?</em>",
        "cta_primary_label":   "Les trois médecins →",
        "cta_secondary_label": "Demander une consultation privée →",
    },

    "visite": {
        "eyebrow":  "Les consultations",
        "headline": "Six parcours cliniques, <em>une seule signature.</em>",
        "intro":
            "Chaque consultation au Studio Marani est un parcours clinique "
            "défini, avec une durée, un tarif et un plan de suivi écrits.",

        "service_image":
            "https://images.unsplash.com/photo-1530497610245-94d3c16cda28"
            "?auto=format&fit=crop&w=1400&q=80",
        "service_image_caption": "Diagnostic cardiaque · Studio Marani",

        "treatments": [
            ("Consultation cardiologique complète",
             "45 min · première visite",
             "Anamnèse approfondie, examen clinique, électrocardiogramme "
             "12 dérivations, compte-rendu personnel et plan de suivi écrit.",
             "220 €"),
            ("Consultation de contrôle",
             "30 min · patients suivis",
             "Révision du traitement, ECG de contrôle, lecture des analyses "
             "biologiques récentes.",
             "140 €"),
            ("Second avis spécialisé",
             "60 min · sur dossier",
             "Lecture complète des comptes-rendus, des examens instrumentaux "
             "et du dossier clinique, avec un rapport final signé et la "
             "bibliographie de référence.",
             "280 €"),
            ("Échocardiographie transthoracique",
             "30 min · sur place",
             "Examen échocardiographique bidimensionnel et Doppler couleur "
             "avec le système Philips EPIQ 7. Compte-rendu dans la journée.",
             "180 €"),
            ("Holter cardiaque 24h",
             "Enregistrement + lecture",
             "Monitorage électrocardiographique sur 24 heures avec le "
             "système Schiller MT-200, lecture et compte-rendu personnel.",
             "160 €"),
            ("Programme de prévention 6 mois",
             "Parcours annuel",
             "Quatre consultations planifiées, deux ECG, un Holter, "
             "évaluation intégrée avec diététicien et médecin du sport, "
             "accès direct au canal du médecin.",
             "980 €"),
        ],

        "footnote":
            "Tous les paiements sont déductibles au titre des frais "
            "médicaux. Le cabinet délivre un reçu sanitaire avec timbre "
            "fiscal. Pour les patients résidant hors de Rome, un "
            "forfait incluant une téléconsultation de suivi peut être "
            "convenu.",
        "footnote_heading": "Notes administratives",

        "cta_heading":
            "Une consultation au Studio Marani est <em>convenue personnellement</em>.",
        "cta_primary_label":   "Formulaire de demande →",
        "cta_secondary_label": "Numéro direct du secrétariat →",
    },

    "medici": {
        "eyebrow":  "Les médecins",
        "headline": "Trois signatures, un seul <em>dossier clinique.</em>",
        "intro":
            "Le cabinet est composé de trois cardiologues qui partagent "
            "dossiers, méthodes et standards de compte-rendu. Chaque "
            "patient a cependant un seul médecin référent.",

        "portrait_city": "Rome · Parioli",

        "doctors": [
            {
                "name":  "Dr. Riccardo Marani",
                "role":  "Directeur clinique · Cardiologue",
                "tags":  ["Prévention cardiovasculaire", "Seconds avis", "Cardiologie clinique"],
                "bio":
                    "Spécialiste en cardiologie à l'Université La Sapienza de "
                    "Rome, perfectionné en échocardiographie clinique à "
                    "l'Institut de Cardiologie de Montréal. Membre de la SIC "
                    "et de l'ESC. Auteur de plus de quarante publications "
                    "indexées, dont deux chapitres du traité Braunwald-Italia.",
                "portrait": _DR_MARANI_PORTRAIT,
                "links": [("PubMed", "#"), ("ORCID", "#")],
            },
            {
                "name":  "Dr. Margherita Salieri",
                "role":  "Cardiologue · Responsable prévention",
                "tags":  ["Programme de prévention", "Cardiologie familiale", "Réhabilitation"],
                "bio":
                    "Diplômée à Bologne, doctorat en physiologie "
                    "cardiovasculaire à Padoue. Coordinatrice du programme "
                    "de prévention cardiovasculaire familiale du Studio "
                    "Marani depuis 2024. Son exercice est centré sur les "
                    "femmes en période périménopausique et sur les noyaux "
                    "familiaux avec antécédents d'événements précoces.",
                "portrait": _DR_SALIERI_PORTRAIT,
                "links": [("Curriculum", "#")],
            },
            {
                "name":  "Dr. Andrea Lombardi",
                "role":  "Cardiologue · Imagerie diagnostique",
                "tags":  ["Échocardiographie", "Holter", "Cardiologie du sport"],
                "bio":
                    "Spécialiste à l'hôpital Sant'Andrea de Rome, formé en "
                    "échocardiographie avancée à l'hôpital Saint-Joseph de "
                    "Paris. Depuis 2018, référent pour l'imagerie "
                    "diagnostique du cabinet. Consultant cardiologique pour "
                    "deux clubs de football de Serie B.",
                "portrait": _DR_LOMBARDI_PORTRAIT,
                "links": [("Publications", "#")],
            },
        ],
    },

    "pubblicazioni": {
        "eyebrow":  "Publications & lectures",
        "headline": "Travaux scientifiques, <em>lectures critiques</em>, écriture clinique.",
        "intro":
            "Une sélection des publications du cabinet et des textes de "
            "vulgarisation écrits pour le grand public. Tous les contenus "
            "sont relus personnellement par le Dr. Marani avant publication.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Studio Marani · Cardiologie clinique",
        "empty_body_fallback_paragraphs": [
            "Article en préparation éditoriale. La version intégrale sera "
            "disponible prochainement.",
            "Ce paragraphe décrit la voix de l'article : une note clinique "
            "rédigée par le médecin, dans un ton direct et sans jargon, "
            "pensée pour les patients et leurs proches en recherche "
            "d'informations fiables.",
        ],
    },

    "posts": [
        {
            "slug":     "secondo-parere-quando-richiederlo",
            "kicker":   "Pratique clinique",
            "title":    "Quand un second avis cardiologique a vraiment du sens",
            "date":     "12 mars 2026",
            "read_min": 6,
            "author":   "Dr. Riccardo Marani",
            "lede":
                "Ce n'est pas une défiance envers le premier médecin. "
                "C'est un geste d'hygiène clinique qui — bien fait — "
                "protège le patient, son médecin traitant et le système.",
            "body": [
                ("p", "Chaque année, le cabinet reçoit environ deux cents "
                      "demandes de second avis. Elles viennent presque "
                      "toujours de patients inquiets : un diagnostic "
                      "inattendu, une thérapie complexe, une indication "
                      "chirurgicale. Notre premier travail consiste à "
                      "faire baisser la température émotionnelle."),
                ("h2", "Trois situations dans lesquelles le second avis est indiqué"),
                ("ol", [
                    "Un diagnostic nouveau et à fort impact, posé en quelques heures ou aux urgences.",
                    "Une thérapie pharmacologique de longue durée avec des effets indésirables notables.",
                    "Une indication à une procédure invasive (pose de pacemaker, cardioversion, ablation).",
                ]),
                ("p", "Dans tous les autres cas — un simple contrôle annuel, "
                      "une variation mineure de tension, un épisode isolé "
                      "de palpitations — un long échange avec votre propre "
                      "cardiologue suffit presque toujours."),
                ("h2", "Que faut-il apporter à un second avis ?"),
                ("p", "Un second avis sans documents est un second avis "
                      "erroné. Pour travailler correctement, il nous faut : "
                      "la lettre de sortie du médecin traitant, tous les "
                      "examens d'imagerie en original (ECG, échographie, "
                      "Holter, éventuelles coronarographies), les analyses "
                      "de sang des six derniers mois et la liste à jour du "
                      "traitement en cours, avec posologies et horaires "
                      "de prise."),
                ("blockquote",
                 "Le second avis ne remplace pas le médecin traitant : "
                 "il l'accompagne. Quand le dialogue entre les deux "
                 "spécialistes fonctionne, le patient gagne deux fois."),
            ],
        },
        {
            "slug":     "prevenzione-familiare-cardiovascolare",
            "kicker":   "Prévention",
            "title":    "Prévention cardiovasculaire familiale : ce que cela veut vraiment dire",
            "date":     "27 février 2026",
            "read_min": 4,
            "author":   "Dr. Margherita Salieri",
            "lede":
                "Six mois de suivi intégré ne sont pas un forfait "
                "commercial. C'est un outil clinique pour celles et ceux "
                "qui ont un antécédent familial direct d'événement "
                "cardiovasculaire précoce.",
        },
        {
            "slug":     "ecocardiografia-quando-serve",
            "kicker":   "Diagnostic",
            "title":    "Échocardiographie transthoracique : quand est-elle vraiment nécessaire",
            "date":     "11 février 2026",
            "read_min": 5,
            "author":   "Dr. Andrea Lombardi",
            "lede":
                "Tous les patients qui demandent « une écho » n'en ont "
                "pas besoin. Un guide honnête des indications cliniques "
                "réelles et des cas où l'examen est redondant.",
        },
        {
            "slug":     "donne-cuore-perimenopausa",
            "kicker":   "Cardiologie de genre",
            "title":    "Femmes et cœur : le silence de la périménopause",
            "date":     "23 janvier 2026",
            "read_min": 7,
            "author":   "Dr. Margherita Salieri",
            "lede":
                "Pendant des décennies, les protocoles de cardiologie ont "
                "été construits sur des patients masculins. Beaucoup de "
                "femmes entre quarante-cinq et soixante ans reçoivent "
                "encore aujourd'hui des diagnostics tardifs ou erronés.",
        },
        {
            "slug":     "sport-amatoriale-controlli",
            "kicker":   "Sport et cœur",
            "title":    "Sport amateur : les contrôles cardiologiques qui comptent vraiment",
            "date":     "8 janvier 2026",
            "read_min": 4,
            "author":   "Dr. Andrea Lombardi",
            "lede":
                "Trois grands mythes sur les contrôles pré-sportifs "
                "amateurs, par celui qui les signe quotidiennement "
                "pour cyclistes, coureurs et nageurs entre quarante "
                "et soixante ans.",
        },
    ],

    "contatti": {
        "eyebrow":  "Contact",
        "headline": "Un seul numéro, <em>une seule personne</em> à l'autre bout du fil.",
        "intro":
            "Le cabinet répond personnellement aux appels du lundi au "
            "vendredi. Le secrétariat clinique est tenu par Mme Adele "
            "Petrucci, qui connaît chaque dossier et chaque patient "
            "par son nom.",

        "blocks": [
            ("Adresse",   "Viale Parioli 142", "00197 Rome · escalier B, intérieur 4"),
            ("Téléphone", "+39 06 320 1144",   "Ligne directe 9h – 19h"),
            ("E-mail",    "studio@maranicardiologia.it", "Réponse dans la journée ouvrée"),
            ("Urgences",  "+39 335 642 8011",  "Ligne réservée aux patients suivis"),
        ],

        "hours": [
            ("Lundi",     "9h – 13h", "15h – 19h"),
            ("Mardi",     "9h – 13h", "15h – 19h"),
            ("Mercredi",  "9h – 13h", "15h – 19h"),
            ("Jeudi",     "9h – 13h", "15h – 19h"),
            ("Vendredi",  "9h – 13h", "—"),
            ("Samedi",    "Fermé au public", "Garde téléphonique pour patients suivis"),
            ("Dimanche",  "Fermé", "—"),
        ],

        "transport": [
            ("Métro",   "Ligne B · Termini → bus 168 arrêt Parioli/Liegi"),
            ("Voiture", "Parking partenaire Q-Park Parioli, entrée Via Bertoloni"),
            ("Train",   "Gare de Termini · 12 minutes en taxi"),
        ],

        "form_title": "Écrire au cabinet",
        "form_intro":
            "Pour les demandes non urgentes — informations sur les "
            "consultations, tarifs, logistique — utilisez ce formulaire. "
            "Le secrétariat clinique répond personnellement.",

        "hours_heading":     "Horaires d'ouverture",
        "transport_heading": "Comment nous rejoindre",

        "form_placeholders": {
            "first_name": "Jean",
            "last_name":  "Dupont",
            "email":      "jean.dupont@email.fr",
            "phone":      "+33 6 ...",
            "subject":    "Informations pour une consultation de contrôle",
            "message":
                "Quelques lignes suffisent — le secrétariat vous "
                "recontacte dans la journée ouvrée.",
        },
    },

    "richiedi-visita": {
        "eyebrow":  "Demande de consultation privée",
        "headline": "Une consultation privée <em>ne se réserve pas</em> : elle se convient.",
        "intro":
            "Il n'existe pas d'agenda en ligne. Chaque première "
            "consultation est réservée après lecture d'une brève "
            "description du cas. Les demandes sont évaluées "
            "personnellement par le médecin sous 48 heures ouvrées.",

        "process_label":   "Comment cela fonctionne",
        "process_heading": "Quatre étapes, en <em>quatre jours ouvrés.</em>",

        "process": [
            ("01", "Remplissez le formulaire",
             "Dix lignes suffisent à cadrer votre demande. Joignez les "
             "examens récents si vous le souhaitez : cela évite de "
             "vous les redemander."),
            ("02", "Lecture clinique",
             "Le médecin lit personnellement la demande sous 48 "
             "heures ouvrées et évalue si la première consultation "
             "relève de sa compétence."),
            ("03", "Proposition de rendez-vous",
             "Si le cas est de notre ressort, le secrétariat vous "
             "propose deux créneaux compatibles avec vos disponibilités."),
            ("04", "Confirmation et dossier",
             "Une fois le rendez-vous confirmé, vous recevez par "
             "e-mail la liste des documents à apporter et l'adresse "
             "du cabinet avec les indications d'accès."),
        ],

        "form_title": "Formulaire de demande",
        "form_band_side_note":
            "Prenez quelques minutes. Les demandes soignées sont lues "
            "intégralement par le médecin — les demandes bâclées, non.",
        "form_band_side_note_small": "↓ Formulaire réservé",

        "form_fields": [
            {"label": "Nom et prénom", "placeholder": "Jean Dupont",
             "type": "text", "full_width": False},
            {"label": "E-mail", "placeholder": "jean@email.fr",
             "type": "email", "full_width": False},
            {"label": "Téléphone", "placeholder": "+33 6 ...",
             "type": "tel", "full_width": False},
            {"label": "Âge", "placeholder": "52",
             "type": "number", "full_width": False},
            {"label": "Type de consultation", "type": "select", "full_width": False,
             "options": ["Première consultation", "Second avis",
                         "Programme de prévention", "Consultation de contrôle"]},
            {"label": "Disponibilités préférées", "type": "select", "full_width": False,
             "options": ["Matin", "Après-midi", "Indifférent"]},
            {"label": "Médecin traitant", "placeholder": "Dr. ...",
             "type": "text", "full_width": True},
            {"label": "Brève description du cas",
             "placeholder":
                 "Symptômes, examens déjà réalisés, diagnostic actuel, "
                 "traitement en cours. Restez dans les dix lignes.",
             "type": "textarea", "full_width": True},
        ],

        "submit_label": "Envoyer la demande",

        "consent":
            "J'accepte le traitement de mes données personnelles "
            "conformément à la notice d'information et au Règlement "
            "UE 679/2016. Les données cliniques sont conservées dans "
            "les seules archives papier du cabinet.",

        "footnote":
            "Le cabinet ne répond pas aux demandes anonymes et ne "
            "délivre pas d'avis cliniques par e-mail sans consultation. "
            "Pour les informations administratives (tarifs, horaires, "
            "parking), utilisez la page contact.",
    },
}


# ===========================================================================
# SPANISH
# ===========================================================================

CARDIO_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Consulta",        "kind": "home"},
        {"slug": "studio",          "label": "La consulta",     "kind": "about"},
        {"slug": "visite",          "label": "Consultas",       "kind": "services"},
        {"slug": "medici",          "label": "Médicos",         "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Publicaciones",   "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contacto",        "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Solicitar cita",  "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "M",
        "logo_word":    "Studio Marani",
        "tag":          "Cardiología clínica · Roma Parioli",
        "phone":        "+39 06 320 1144",
        "email":        "studio@maranicardiologia.it",
        "address":      "Viale Parioli 142 · 00197 Roma",
        "hours_compact": "Lun – Vie · 9:00 – 19:00",
        "hours_footer_rows": [
            "Sábado · solo guardia telefónica",
            "Domingo · cerrado",
        ],
        "license":      "Colegio de Médicos de Roma 12 / 4408",
        "footer_intro":
            "Consulta privada especializada en cardiología clínica y "
            "prevención cardiovascular. Atención solo con cita previa.",
    },

    "home": {
        "hero_variant": "split-consultive",
        "eyebrow":  "Cardiología clínica · Roma Parioli",
        "headline": "Una cardiología <em>a medida</em>, para quien no acepta atajos.",
        "intro":
            "Consultas especializadas, segundas opiniones, programas de "
            "prevención individual. Una sola agenda, un solo médico, "
            "una sola firma.",
        "primary_cta":   "Solicitar consulta privada",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "La consulta",
        "secondary_href":"studio",

        "facts": [
            ("15",    "años de práctica clínica privada"),
            ("1.200", "consultas especializadas al año"),
            ("4",     "hospitales de referencia en Roma"),
        ],

        "manifesto_drop_cap": "L",
        "manifesto":
            "a cardiología no es una cadena de montaje. Es una conversación "
            "larga, hecha de anamnesis paciente, de exploraciones leídas "
            "dos veces, de tiempo. Durante quince años, Studio Marani ha "
            "acompañado a pacientes públicos y privados en un recorrido "
            "de prevención cardiovascular construido a medida — con "
            "discreción y con método.",

        "signature_visits": [
            ("01", "Consulta cardiológica completa",
             "Anamnesis amplia, ECG, informe personal y plan de "
             "seguimiento redactado con un calendario adaptado al paciente."),
            ("02", "Segunda opinión especializada",
             "Para pacientes con diagnósticos complejos o tratamientos "
             "múltiples en curso — dossier en mano, junto con el "
             "médico de cabecera."),
            ("03", "Programa de prevención",
             "Seis meses de seguimiento integrado con dietista y médico "
             "deportivo, indicado para familias con antecedentes de "
             "eventos cardiovasculares precoces."),
            ("04", "Holter y ecocardiografía",
             "Registro cardíaco de 24 horas y ecocardiograma "
             "transtorácico, informados en el día, en la consulta."),
        ],

        "chief": {
            "name":  "Dr. Riccardo Marani",
            "role":  "Director clínico · Cardiólogo",
            "bio":
                "Especialista en cardiología por la Universidad La "
                "Sapienza de Roma, perfeccionado en el Institut de "
                "Cardiologie de Montréal. Miembro de la Sociedad Italiana "
                "de Cardiología y de la Sociedad Europea de Cardiología. "
                "Autor de más de cuarenta publicaciones indexadas.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "press": ["LANCET", "European Heart Journal", "Corriere Salute",
                  "Sole 24 Ore", "RAI Med"],
        "press_label": "Publicado en",

        "hero_sidebar_top_label": "Dirección clínica",
        "hero_sidebar_quote":
            "«La cardiología no es una cadena de montaje. "
            "Es una conversación larga, hecha de tiempo.»",
        "hero_sidebar_author": "— Lancet · 2024",
        "hero_sidebar_pulse": [
            ("Consulta",   "Roma · Parioli"),
            ("Desde",      "2010"),
            ("Referencia", "Cardiología clínica"),
        ],

        "signature_visits_label":   "Consultas y programas",
        "signature_visits_heading": "Seis recorridos clínicos, <em>una sola firma.</em>",
        "signature_visits_intro":
            "Cuatro de las consultas más solicitadas de la consulta. "
            "La lista completa está en la página Consultas.",

        "chief_label":   "Dirección clínica",
        "chief_heading": "Una sola firma <em>en cada historia clínica.</em>",

        "tecnologie": {
            "label": "Tecnología y equipamiento",
            "heading": "Diagnóstico de <em>última generación</em>, en consulta.",
            "items": [
                {"icon": "ecg", "title": "ECG de 12 derivaciones", "desc": "Electrocardiograma en reposo con informe inmediato y comparación histórica."},
                {"icon": "echo", "title": "Ecocardiografía Philips EPIQ 7", "desc": "Ecografía cardíaca 2D y Doppler color de última generación, informe en el día."},
                {"icon": "holter", "title": "Holter Schiller MT-200", "desc": "Registro de ECG de 24 horas con análisis de variabilidad y arritmias silentes."},
                {"icon": "stress", "title": "Prueba de esfuerzo", "desc": "Test en cicloergómetro con monitorización continua de la presión arterial."},
            ],
        },
        "testimonianza": {
            "quote": "Busqué durante dos años un cardiólogo que leyera de verdad mi historial antes de examinarme. En el Studio Marani dedicaron cuarenta minutos a mis pruebas antes siquiera de coger el estetoscopio.",
            "author": "Paciente de la consulta",
            "context": "Segunda opinión cardiológica · 2025",
        },
        "faq": {
            "label": "Preguntas frecuentes",
            "heading": "Las preguntas que <em>nos hacen con más frecuencia.</em>",
            "items": [
                ("¿Cuánto dura una primera visita cardiológica?", "Una primera visita completa dura aproximadamente cuarenta y cinco minutos e incluye anamnesis, exploración física, ECG de 12 derivaciones, informe y discusión del plan de seguimiento."),
                ("¿Necesito volante del médico de cabecera?", "No. Al tratarse de una consulta especializada privada, no es necesaria la derivación del médico de familia. Un informe del médico de cabecera es útil pero no obligatorio."),
                ("¿Puedo traer pruebas de otro hospital?", "Por supuesto. La segunda opinión es una de nuestras especialidades. Traiga todos los informes, cartas de alta y tratamientos en curso."),
                ("¿El ecocardiograma es doloroso?", "No, es una prueba completamente indolora y no invasiva. La sonda se coloca sobre el tórax con un gel conductor. La exploración dura entre veinte y treinta minutos."),
                ("¿Cómo funciona el programa de prevención?", "El programa semestral incluye cuatro visitas programadas, dos ECG, un Holter de 24 horas, una valoración integrada con dietista y médico del deporte, y una línea directa con el médico de la consulta."),
            ],
        },

        "cta_heading":
            "Cada consulta se <em>acuerda personalmente</em> con el médico.",
        "cta_primary_label":   "Solicitar consulta privada",
        "cta_secondary_label": "Contactar con la consulta",
    },

    "studio": {
        "eyebrow":  "La consulta",
        "headline": "Quince años de <em>cardiología clínica</em> independiente.",
        "intro":
            "Studio Marani nació en 2010 con la idea de devolverle a la "
            "cardiología su dimensión de tiempo largo: consultas de "
            "cuarenta y cinco minutos, informe personal, seguimiento "
            "telefónico directo del médico.",

        "history": [
            ("2010",
             "Apertura de la primera consulta en Viale Parioli, dos salas "
             "y una secretaria. Las primeras quince historias clínicas "
             "aún se conservan archivadas en su formato papel original."),
            ("2014",
             "Convenio con el Policlinico Umberto I para los casos que "
             "requieren hospitalización o procedimientos intervencionistas "
             "de segundo nivel."),
            ("2017",
             "Adquisición de un ecocardiógrafo Philips EPIQ 7 de última "
             "generación y de un Holter Schiller MT-200 para diagnóstico "
             "en el mismo día."),
            ("2020",
             "Apertura de una segunda sala de consulta dedicada a las "
             "segundas opiniones sobre dossieres multidisciplinares, "
             "con acceso a teleconsulta europea."),
            ("2024",
             "Incorporación de la Dra. Margherita Salieri como "
             "responsable del programa de prevención cardiovascular "
             "familiar."),
        ],

        "studio_image":
            "https://images.unsplash.com/photo-1631815588090-d4bfec5b1ccb"
            "?auto=format&fit=crop&w=1400&q=80",
        "studio_image_caption": "Consulta de cardiología · Viale Parioli, Roma",

        "method_title": "Método",
        "method_paragraphs": [
            "Una consulta en Studio Marani empieza siempre por la carpeta "
            "que el paciente trae consigo. Pruebas previas, informes de "
            "alta, notas del médico de cabecera, tratamientos en curso. "
            "Todo se lee, se anota y se comenta antes de siquiera tomar "
            "el fonendoscopio.",
            "La anamnesis dura lo que sea necesario: en promedio, treinta "
            "y cinco minutos. De ella nace un plan clínico escrito, "
            "entregado en mano al paciente en una carpeta de papel "
            "reciclado, firmado por el médico y con el calendario de "
            "los controles posteriores.",
            "Cada historia clínica permanece accesible al paciente "
            "durante diez años y puede solicitarse en copia en cualquier "
            "momento, incluso para su traslado a otro especialista.",
        ],

        "values": [
            ("Tiempo",       "Cuarenta y cinco minutos para toda primera visita, nunca menos."),
            ("Independencia","Sin vínculos con laboratorios farmacéuticos ni con clínicas concertadas."),
            ("Trazabilidad", "Historia clínica completa, reconstruible en cualquier momento."),
            ("Discreción",   "Confidencialidad absoluta sobre los datos y sobre las personas."),
        ],

        "values_label":   "Lo que garantizamos",
        "values_heading": "Cuatro compromisos que <em>no cambian nunca.</em>",

        "cta_heading":
            "¿Quiere conocer a los médicos de la consulta <em>antes de reservar?</em>",
        "cta_primary_label":   "Los tres médicos →",
        "cta_secondary_label": "Solicitar consulta privada →",
    },

    "visite": {
        "eyebrow":  "Las consultas",
        "headline": "Seis recorridos clínicos, <em>una sola firma.</em>",
        "intro":
            "Cada consulta en Studio Marani es un recorrido clínico "
            "definido, con una duración, un precio y un plan de "
            "seguimiento escritos.",

        "service_image":
            "https://images.unsplash.com/photo-1530497610245-94d3c16cda28"
            "?auto=format&fit=crop&w=1400&q=80",
        "service_image_caption": "Diagnóstico cardíaco · Studio Marani",

        "treatments": [
            ("Consulta cardiológica completa",
             "45 min · primera visita",
             "Anamnesis amplia, exploración física, electrocardiograma "
             "de 12 derivaciones, informe personal y plan de seguimiento "
             "escrito.",
             "220 €"),
            ("Consulta de control",
             "30 min · pacientes ya seguidos",
             "Revisión del tratamiento, ECG de control, lectura de "
             "analíticas recientes.",
             "140 €"),
            ("Segunda opinión especializada",
             "60 min · sobre dossier",
             "Lectura completa de informes, pruebas instrumentales y "
             "historia clínica existente, con informe final firmado y "
             "bibliografía de referencia.",
             "280 €"),
            ("Ecocardiografía transtorácica",
             "30 min · en consulta",
             "Exploración ecocardiográfica bidimensional y Doppler color "
             "con sistema Philips EPIQ 7. Informe en el mismo día.",
             "180 €"),
            ("Holter cardíaco 24h",
             "Registro + lectura",
             "Monitorización electrocardiográfica de 24 horas con sistema "
             "Schiller MT-200, lectura e informe personal.",
             "160 €"),
            ("Programa de prevención 6 meses",
             "Recorrido anual",
             "Cuatro visitas programadas, dos ECG, un Holter, valoración "
             "integrada con dietista y médico deportivo, canal directo "
             "con el médico.",
             "980 €"),
        ],

        "footnote":
            "Todos los pagos son deducibles como gastos sanitarios. La "
            "consulta emite recibo sanitario con timbre fiscal. Para "
            "pacientes residentes fuera de Roma es posible acordar un "
            "paquete que incluya teleconsulta de seguimiento.",
        "footnote_heading": "Notas administrativas",

        "cta_heading":
            "Una consulta en Studio Marani se <em>acuerda personalmente</em>.",
        "cta_primary_label":   "Formulario de solicitud →",
        "cta_secondary_label": "Número directo de la secretaría →",
    },

    "medici": {
        "eyebrow":  "Los médicos",
        "headline": "Tres firmas, una sola <em>historia clínica.</em>",
        "intro":
            "La consulta está formada por tres cardiólogos que comparten "
            "historias, métodos y estándares de informe. Cada paciente, "
            "sin embargo, tiene siempre un solo médico de referencia.",

        "portrait_city": "Roma · Parioli",

        "doctors": [
            {
                "name":  "Dr. Riccardo Marani",
                "role":  "Director clínico · Cardiólogo",
                "tags":  ["Prevención cardiovascular", "Segundas opiniones", "Cardiología clínica"],
                "bio":
                    "Especialista en cardiología por la Universidad La "
                    "Sapienza de Roma, perfeccionado en ecocardiografía "
                    "clínica en el Institut de Cardiologie de Montréal. "
                    "Miembro de la SIC y de la ESC. Autor de más de "
                    "cuarenta publicaciones indexadas, entre ellas dos "
                    "capítulos del tratado Braunwald-Italia.",
                "portrait": _DR_MARANI_PORTRAIT,
                "links": [("PubMed", "#"), ("ORCID", "#")],
            },
            {
                "name":  "Dra. Margherita Salieri",
                "role":  "Cardióloga · Responsable de prevención",
                "tags":  ["Programa de prevención", "Cardiología familiar", "Rehabilitación"],
                "bio":
                    "Licenciada en Bolonia, doctorado en fisiología "
                    "cardiovascular en Padua. Coordinadora del programa "
                    "de prevención cardiovascular familiar de Studio "
                    "Marani desde 2024. Se ocupa en particular de "
                    "mujeres en edad perimenopáusica y de núcleos "
                    "familiares con antecedentes de eventos precoces.",
                "portrait": _DR_SALIERI_PORTRAIT,
                "links": [("Curriculum", "#")],
            },
            {
                "name":  "Dr. Andrea Lombardi",
                "role":  "Cardiólogo · Diagnóstico por imagen",
                "tags":  ["Ecocardiografía", "Holter", "Cardiología del deporte"],
                "bio":
                    "Especialista en el Sant'Andrea de Roma, formado en "
                    "ecocardiografía avanzada en el Saint-Joseph de París. "
                    "Desde 2018, referente para el diagnóstico por "
                    "imagen de la consulta. Consultor cardiológico para "
                    "dos clubes de fútbol de Serie B.",
                "portrait": _DR_LOMBARDI_PORTRAIT,
                "links": [("Publicaciones", "#")],
            },
        ],
    },

    "pubblicazioni": {
        "eyebrow":  "Publicaciones y lecturas",
        "headline": "Trabajos científicos, <em>lecturas críticas</em>, escritura clínica.",
        "intro":
            "Una selección de las publicaciones de la consulta y de los "
            "textos divulgativos escritos para el público general. Todos "
            "los contenidos son revisados personalmente por el Dr. Marani "
            "antes de su publicación.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Studio Marani · Cardiología clínica",
        "empty_body_fallback_paragraphs": [
            "Artículo en preparación editorial. La versión íntegra "
            "estará disponible en breve.",
            "Este marcador describe la voz del artículo: una nota "
            "clínica escrita por el médico, en un tono directo y sin "
            "tecnicismos, pensada para pacientes y familiares que "
            "buscan información fiable.",
        ],
    },

    "posts": [
        {
            "slug":     "secondo-parere-quando-richiederlo",
            "kicker":   "Práctica clínica",
            "title":    "Cuándo tiene sentido pedir una segunda opinión cardiológica",
            "date":     "12 de marzo de 2026",
            "read_min": 6,
            "author":   "Dr. Riccardo Marani",
            "lede":
                "No es desconfianza hacia el primer médico. Es un acto "
                "de higiene clínica que — cuando se hace bien — protege "
                "al paciente, al médico de cabecera y al sistema sanitario.",
            "body": [
                ("p", "Cada año la consulta recibe alrededor de doscientas "
                      "solicitudes de segunda opinión. Casi siempre llegan "
                      "de pacientes asustados: un diagnóstico inesperado, "
                      "un tratamiento complejo, una indicación quirúrgica. "
                      "Nuestra primera tarea es bajar la temperatura emocional."),
                ("h2", "Tres situaciones en las que la segunda opinión está indicada"),
                ("ol", [
                    "Diagnóstico nuevo y de alto impacto, recibido en pocas horas o en urgencias.",
                    "Tratamiento farmacológico de larga duración con efectos secundarios relevantes.",
                    "Indicación de un procedimiento invasivo (marcapasos, cardioversión, ablación).",
                ]),
                ("p", "En los demás casos — un control anual, una "
                      "variación menor de la tensión, un episodio "
                      "aislado de palpitaciones — casi siempre basta "
                      "con una conversación en profundidad con su "
                      "propio cardiólogo."),
                ("h2", "Qué llevar a una segunda opinión"),
                ("p", "Una segunda opinión sin documentos es una segunda "
                      "opinión equivocada. Para trabajar bien necesitamos: "
                      "el informe de alta del médico de cabecera, todas "
                      "las pruebas de imagen en original (ECG, eco, "
                      "Holter, coronariografías en su caso), las "
                      "analíticas de los últimos seis meses y la lista "
                      "actualizada del tratamiento en curso, con "
                      "posologías y horarios."),
                ("blockquote",
                 "La segunda opinión no sustituye al médico de "
                 "cabecera: lo acompaña. Cuando el diálogo entre los "
                 "dos especialistas funciona, el paciente gana dos veces."),
            ],
        },
        {
            "slug":     "prevenzione-familiare-cardiovascolare",
            "kicker":   "Prevención",
            "title":    "Programa de prevención cardiovascular familiar: qué significa de verdad",
            "date":     "27 de febrero de 2026",
            "read_min": 4,
            "author":   "Dra. Margherita Salieri",
            "lede":
                "Seis meses de seguimiento integrado no son un paquete "
                "comercial. Son una herramienta clínica para quien tiene "
                "antecedentes familiares directos de un evento "
                "cardiovascular precoz.",
        },
        {
            "slug":     "ecocardiografia-quando-serve",
            "kicker":   "Diagnóstico",
            "title":    "Ecocardiografía transtorácica: cuándo es realmente necesaria",
            "date":     "11 de febrero de 2026",
            "read_min": 5,
            "author":   "Dr. Andrea Lombardi",
            "lede":
                "No todos los pacientes que piden «una eco» la necesitan. "
                "Una guía honesta sobre las indicaciones clínicas reales "
                "y sobre los casos en los que la prueba es redundante.",
        },
        {
            "slug":     "donne-cuore-perimenopausa",
            "kicker":   "Cardiología de género",
            "title":    "Mujer y corazón: el silencio de la perimenopausia",
            "date":     "23 de enero de 2026",
            "read_min": 7,
            "author":   "Dra. Margherita Salieri",
            "lede":
                "Durante décadas los protocolos de cardiología se "
                "construyeron sobre pacientes varones. Como "
                "consecuencia, muchas mujeres entre los cuarenta y "
                "cinco y los sesenta aún reciben hoy diagnósticos "
                "tardíos o equivocados.",
        },
        {
            "slug":     "sport-amatoriale-controlli",
            "kicker":   "Deporte y corazón",
            "title":    "Deporte amateur: los controles cardiológicos que de verdad importan",
            "date":     "8 de enero de 2026",
            "read_min": 4,
            "author":   "Dr. Andrea Lombardi",
            "lede":
                "Tres grandes mitos sobre los controles previos al "
                "deporte amateur, contados por quien los firma a diario "
                "para ciclistas, runners y nadadores entre cuarenta y "
                "sesenta años.",
        },
    ],

    "contatti": {
        "eyebrow":  "Contacto",
        "headline": "Un solo número, <em>una sola persona</em> al otro lado del hilo.",
        "intro":
            "La consulta responde personalmente a las llamadas de lunes "
            "a viernes. La secretaría clínica la atiende la Sra. Adele "
            "Petrucci, que conoce cada historia y a cada paciente por "
            "su nombre.",

        "blocks": [
            ("Dirección",  "Viale Parioli 142", "00197 Roma · escalera B, interior 4"),
            ("Teléfono",   "+39 06 320 1144",   "Línea directa 9:00 – 19:00"),
            ("Email",      "studio@maranicardiologia.it", "Respuesta en el mismo día laborable"),
            ("Urgencias",  "+39 335 642 8011",  "Línea reservada para pacientes en seguimiento"),
        ],

        "hours": [
            ("Lunes",      "9:00 – 13:00", "15:00 – 19:00"),
            ("Martes",     "9:00 – 13:00", "15:00 – 19:00"),
            ("Miércoles",  "9:00 – 13:00", "15:00 – 19:00"),
            ("Jueves",     "9:00 – 13:00", "15:00 – 19:00"),
            ("Viernes",    "9:00 – 13:00", "—"),
            ("Sábado",     "Cerrado al público", "Guardia telefónica para pacientes en seguimiento"),
            ("Domingo",    "Cerrado", "—"),
        ],

        "transport": [
            ("Metro",  "Línea B · Termini → autobús 168 parada Parioli/Liegi"),
            ("Coche",  "Parking concertado Q-Park Parioli, entrada Via Bertoloni"),
            ("Tren",   "Estación Termini · 12 minutos en taxi"),
        ],

        "form_title": "Escribir a la consulta",
        "form_intro":
            "Para consultas no urgentes — información sobre consultas, "
            "precios, logística — escríbanos mediante este formulario. "
            "Le responde personalmente la secretaría clínica.",

        "hours_heading":     "Horario de apertura",
        "transport_heading": "Cómo llegar",

        "form_placeholders": {
            "first_name": "Juan",
            "last_name":  "García",
            "email":      "juan.garcia@email.es",
            "phone":      "+34 6 ...",
            "subject":    "Información sobre una consulta de control",
            "message":
                "Basta con unas líneas — la secretaría le responderá "
                "dentro del mismo día laborable.",
        },
    },

    "richiedi-visita": {
        "eyebrow":  "Solicitud de consulta privada",
        "headline": "Una consulta privada <em>no se reserva</em>: se acuerda.",
        "intro":
            "No existe un calendario online. Cada primera consulta se "
            "reserva tras leer una breve descripción del caso. Las "
            "solicitudes son evaluadas personalmente por el médico "
            "en un plazo de 48 horas laborables.",

        "process_label":   "Cómo funciona",
        "process_heading": "Cuatro pasos, en <em>cuatro días laborables.</em>",

        "process": [
            ("01", "Rellena el formulario",
             "Bastan diez líneas para encuadrar tu solicitud. Adjunta "
             "las pruebas recientes si quieres: evita que te las "
             "pidamos dos veces."),
            ("02", "Lectura clínica",
             "El médico lee personalmente la solicitud en un plazo de "
             "48 horas laborables y valora si la primera consulta es "
             "de su competencia."),
            ("03", "Propuesta de cita",
             "Si el caso es de nuestra competencia, la secretaría "
             "propone dos franjas horarias compatibles con tu "
             "disponibilidad."),
            ("04", "Confirmación y dossier",
             "Una vez confirmada la cita, recibes por correo "
             "electrónico el listado de documentos a traer y la "
             "dirección de la consulta con las indicaciones de acceso."),
        ],

        "form_title": "Formulario de solicitud",
        "form_band_side_note":
            "Reserva unos minutos. Las solicitudes redactadas con "
            "cuidado son leídas íntegramente por el médico — las "
            "apresuradas, no.",
        "form_band_side_note_small": "↓ Formulario reservado",

        "form_fields": [
            {"label": "Nombre y apellidos", "placeholder": "Juan García",
             "type": "text", "full_width": False},
            {"label": "Correo electrónico", "placeholder": "juan@email.es",
             "type": "email", "full_width": False},
            {"label": "Teléfono", "placeholder": "+34 6 ...",
             "type": "tel", "full_width": False},
            {"label": "Edad", "placeholder": "52",
             "type": "number", "full_width": False},
            {"label": "Tipo de consulta", "type": "select", "full_width": False,
             "options": ["Primera visita", "Segunda opinión",
                         "Programa de prevención", "Consulta de control"]},
            {"label": "Disponibilidad preferida", "type": "select", "full_width": False,
             "options": ["Mañana", "Tarde", "Indistinto"]},
            {"label": "Médico de cabecera", "placeholder": "Dr. ...",
             "type": "text", "full_width": True},
            {"label": "Breve descripción del caso",
             "placeholder":
                 "Síntomas, pruebas ya realizadas, diagnóstico actual, "
                 "tratamiento en curso. No más de diez líneas.",
             "type": "textarea", "full_width": True},
        ],

        "submit_label": "Enviar solicitud",

        "consent":
            "Acepto el tratamiento de mis datos personales conforme al "
            "aviso de privacidad y al Reglamento UE 679/2016. Los datos "
            "clínicos se conservan únicamente en el archivo en papel "
            "de la consulta.",

        "footnote":
            "La consulta no responde a solicitudes anónimas y no emite "
            "opiniones clínicas por correo electrónico sin visita. Para "
            "información administrativa (precios, horarios, aparcamiento) "
            "utilice la página de contacto.",
    },
}


# ===========================================================================
# ARABIC (RTL)
# ===========================================================================

CARDIO_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "المركز",           "kind": "home"},
        {"slug": "studio",          "label": "عن المركز",         "kind": "about"},
        {"slug": "visite",          "label": "الاستشارات",        "kind": "services"},
        {"slug": "medici",          "label": "الأطباء",            "kind": "team"},
        {"slug": "pubblicazioni",   "label": "المنشورات",          "kind": "blog_list"},
        {"slug": "contatti",        "label": "تواصل",             "kind": "contact"},
        {"slug": "richiedi-visita", "label": "طلب زيارة",         "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "M",
        "logo_word":    "Studio Marani",
        "tag":          "أمراض القلب السريرية · روما باريولي",
        "phone":        "+39 06 320 1144",
        "email":        "studio@maranicardiologia.it",
        "address":      "Viale Parioli 142 · 00197 روما",
        "hours_compact": "الاثنين – الجمعة · 9:00 – 19:00",
        "hours_footer_rows": [
            "السبت · على الاستعداد فقط",
            "الأحد · مغلق",
        ],
        "license":      "نقابة أطباء روما 12 / 4408",
        "footer_intro":
            "عيادة خاصة متخصصة في أمراض القلب السريرية والوقاية من "
            "أمراض القلب والأوعية الدموية. الزيارة بموعد مسبق فقط.",
    },

    "home": {
        "hero_variant": "split-consultive",
        "eyebrow":  "أمراض القلب السريرية · روما باريولي",
        "headline": "طبّ قلب <em>مُفصَّل خصّيصاً</em> لمن لا يقبل بالاختصارات.",
        "intro":
            "استشارات تخصصية، آراء ثانية، برامج وقاية فردية. "
            "جدول واحد، طبيب واحد، توقيع واحد.",
        "primary_cta":   "اطلب زيارة خاصة",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "عن المركز",
        "secondary_href":"studio",

        "facts": [
            ("15",    "سنةً من الممارسة السريرية الخاصة"),
            ("1.200", "استشارة تخصصية في السنة"),
            ("4",     "مستشفيات مرجعية في روما"),
        ],

        "manifesto_drop_cap": "ط",
        "manifesto":
            "بّ القلب ليس خطّ إنتاج. إنّه حوار طويل، يقوم على إصغاء "
            "صبور لتاريخ المريض، وقراءة الفحوص مرّتين، وعلى متابعة "
            "هاتفية مباشرة من الطبيب نفسه. منذ خمسة عشر عاماً، يرافق "
            "Studio Marani مرضاه في مسارٍ وقائيٍّ للقلب والأوعية الدموية "
            "مبنيٍّ على مقاسهم تماماً — بتكتّم ومنهجية.",

        "signature_visits": [
            ("01", "استشارة قلبية شاملة",
             "استجواب سريري مفصّل، تخطيط كهربية القلب، تقرير شخصي "
             "وخطّة متابعة مكتوبة بتسلسل زمني مخصص للمريض."),
            ("02", "رأي تخصصي ثانٍ",
             "للمرضى ذوي التشخيصات المعقدة أو العلاجات المتعددة الجارية، "
             "مع قراءة الملف كاملاً بالاشتراك مع الطبيب المعالج."),
            ("03", "برنامج وقاية",
             "ستة أشهر من المتابعة المتكاملة بالتعاون مع أخصائي "
             "التغذية وطبيب الرياضة، موصى به للعائلات ذات سوابق "
             "أحداث قلبية مبكرة."),
            ("04", "هولتر وتخطيط صدى القلب",
             "تسجيل قلبي على مدى 24 ساعة وتخطيط صدى القلب عبر الصدر، "
             "مع تقرير يُسلَّم في اليوم نفسه داخل المركز."),
        ],

        "chief": {
            "name":  "الدكتور ريكاردو ماراني",
            "role":  "المدير السريري · طبيب قلب",
            "bio":
                "متخصص في أمراض القلب من جامعة لا سابينزا في روما، "
                "واستكمل تدريبه في معهد أمراض القلب في مونتريال. "
                "عضو في الجمعية الإيطالية لأمراض القلب والجمعية "
                "الأوروبية لأمراض القلب. مؤلف لأكثر من أربعين بحثاً "
                "محكَّماً منشوراً في دوريات مفهرسة.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "press": ["LANCET", "European Heart Journal", "Corriere Salute",
                  "Sole 24 Ore", "RAI Med"],
        "press_label": "نُشر في",

        "hero_sidebar_top_label": "الإدارة السريرية",
        "hero_sidebar_quote":
            "«طبّ القلب ليس خطّ إنتاج. إنّه حوار طويل، يبنى على الوقت.»",
        "hero_sidebar_author": "— Lancet · 2024",
        "hero_sidebar_pulse": [
            ("المركز",  "روما · باريولي"),
            ("منذ",     "2010"),
            ("التخصص", "أمراض القلب السريرية"),
        ],

        "signature_visits_label":   "الاستشارات والبرامج",
        "signature_visits_heading": "ستة مسارات سريرية، <em>توقيع واحد.</em>",
        "signature_visits_intro":
            "أربعة من الاستشارات الأكثر طلباً في المركز. "
            "القائمة الكاملة متاحة في صفحة الاستشارات.",

        "chief_label":   "الإدارة السريرية",
        "chief_heading": "توقيع واحد <em>على كلّ ملف.</em>",

        "tecnologie": {
            "label": "التقنيات والتجهيزات",
            "heading": "تشخيص <em>متقدّم</em>، داخل العيادة.",
            "items": [
                {"icon": "ecg", "title": "تخطيط قلب كهربائي ١٢ اتجاهًا", "desc": "تخطيط كهربائي أثناء الراحة مع تقرير فوري ومقارنة تاريخية."},
                {"icon": "echo", "title": "تصوير القلب بالصدى Philips EPIQ 7", "desc": "تصوير قلب ثنائي الأبعاد ودوبلر ملوّن من الجيل الأخير، يُسلَّم التقرير في اليوم ذاته."},
                {"icon": "holter", "title": "هولتر Schiller MT-200", "desc": "تسجيل تخطيط كهربائي على مدار ٢٤ ساعة مع تحليل التباين واضطرابات النظم الصامتة."},
                {"icon": "stress", "title": "اختبار الجهد", "desc": "اختبار على جهاز دراجة مع مراقبة مستمرة لضغط الدم."},
            ],
        },
        "testimonianza": {
            "quote": "بحثتُ لمدة عامَين عن طبيب قلب يقرأ ملفّي فعلاً قبل أن يفحصني. في ستوديو ماراني أمضوا أربعين دقيقة على فحوصاتي قبل أن يلمسوا السمّاعة.",
            "author": "مريض في العيادة",
            "context": "رأي ثانٍ في أمراض القلب · ٢٠٢٥",
        },
        "faq": {
            "label": "الأسئلة الشائعة",
            "heading": "الأسئلة التي <em>تُطرح علينا كثيرًا.</em>",
            "items": [
                ("كم تستغرق الزيارة الأولى لطبيب القلب؟", "تستغرق الزيارة الأولى الكاملة نحو خمسٍ وأربعين دقيقة وتشمل السيرة المرضية والفحص السريري وتخطيط القلب الكهربائي ذي الاثنتي عشرة اتجاهًا والتقرير ومناقشة خطة المتابعة."),
                ("هل أحتاج إلى تحويل من طبيب الأسرة؟", "لا. بوصفنا عيادة متخصصة خاصة، لا يلزم خطاب تحويل. رسالة من طبيب الأسرة مفيدة لكنها غير إلزامية."),
                ("هل يمكنني إحضار فحوصات من مستشفى آخر؟", "بالتأكيد. الرأي الثاني هو أحد تخصصاتنا. أحضر جميع التقارير وخطابات الخروج والعلاجات الجارية."),
                ("هل تصوير القلب بالصدى مؤلم؟", "لا، هو فحص غير مؤلم تمامًا وغير جراحي. يُوضع المسبار على الصدر مع جل موصل. يستغرق الفحص نحو عشرين إلى ثلاثين دقيقة."),
                ("كيف يعمل برنامج الوقاية؟", "يشمل البرنامج نصف السنوي أربع زيارات مجدولة وتخطيطَي قلب كهربائيَّين وهولتر على مدار ٢٤ ساعة وتقييمًا متكاملًا مع اختصاصي تغذية وطبيب رياضي وخطًا مباشرًا مع طبيب العيادة."),
            ],
        },

        "cta_heading":
            "كلّ استشارة <em>تُنسَّق شخصياً</em> مع الطبيب.",
        "cta_primary_label":   "اطلب زيارة خاصة",
        "cta_secondary_label": "تواصل مع المركز",
    },

    "studio": {
        "eyebrow":  "عن المركز",
        "headline": "خمسة عشر عاماً من <em>طبّ القلب السريري</em> المستقلّ.",
        "intro":
            "تأسّس Studio Marani عام 2010 انطلاقاً من فكرة إعادة الوقت "
            "الطويل إلى طبّ القلب: استشارات مدّتها خمس وأربعون دقيقة، "
            "تقارير شخصية، ومتابعة هاتفية مباشرة من الطبيب.",

        "history": [
            ("2010",
             "افتتاح المقر الأول في Viale Parioli — غرفتان وسكرتيرة "
             "واحدة. الملفات الخمسة عشر الأولى لا تزال محفوظة بصيغتها "
             "الورقية الأصلية."),
            ("2014",
             "اتفاقية مع Policlinico Umberto I للحالات التي تتطلّب "
             "دخولاً إلى المستشفى أو إجراءات تداخلية من المستوى الثاني."),
            ("2017",
             "اقتناء جهاز تخطيط صدى القلب Philips EPIQ 7 من أحدث جيل، "
             "وجهاز هولتر Schiller MT-200 لإتاحة التشخيص في اليوم نفسه."),
            ("2020",
             "تجهيز غرفة استشارة ثانية مخصصة للآراء الثانية على "
             "ملفات متعددة الاختصاصات، مع إمكانية الاستشارة عن بُعد "
             "على المستوى الأوروبي."),
            ("2024",
             "انضمام الدكتورة مارغريتا ساليري مسؤولةً عن برنامج "
             "الوقاية القلبية الوعائية العائلي."),
        ],

        "studio_image":
            "https://images.unsplash.com/photo-1631815588090-d4bfec5b1ccb"
            "?auto=format&fit=crop&w=1400&q=80",
        "studio_image_caption": "عيادة أمراض القلب · فيالي باريولي، روما",

        "method_title": "المنهج",
        "method_paragraphs": [
            "تبدأ الاستشارة في Studio Marani دائماً من الملف الذي "
            "يحضره المريض معه: الفحوصات السابقة، رسائل الخروج من "
            "المستشفى، ملاحظات الطبيب المعالج، العلاجات الحالية. "
            "كلّ ذلك يُقرأ ويُدوَّن ويُناقش قبل أن تُلمس السمّاعة.",
            "يستغرق الاستجواب السريري ما يلزم من الوقت: في المتوسط "
            "خمساً وثلاثين دقيقة. ينبثق منه خطة سريرية مكتوبة، تُسلَّم "
            "للمريض في ملف ورقي معاد تدويره، موقّعة من الطبيب، "
            "ومُرفقة بالجدول الزمني للمتابعات اللاحقة.",
            "يبقى كلّ ملف متاحاً للمريض لمدة عشر سنوات، ويمكن "
            "الحصول على نسخة منه في أيّ وقت، بما في ذلك في حالة "
            "التحويل إلى طبيب آخر.",
        ],

        "values": [
            ("الوقت",        "خمس وأربعون دقيقة لكلّ زيارة أولى، لا أقلّ من ذلك أبداً."),
            ("الاستقلالية",  "لا ارتباط بأيّ شركة أدوية أو عيادة متعاقدة."),
            ("قابلية التتبع","ملف سريري كامل يمكن إعادة بنائه في أيّ وقت."),
            ("التكتّم",       "سرّيّة مطلقة على البيانات وعلى الأشخاص."),
        ],

        "values_label":   "ما نلتزم به",
        "values_heading": "أربعة التزامات <em>لا تتغيّر أبداً.</em>",

        "cta_heading":
            "هل تودّ التعرّف على أطباء المركز <em>قبل الحجز؟</em>",
        "cta_primary_label":   "الأطباء الثلاثة →",
        "cta_secondary_label": "اطلب زيارة خاصة →",
    },

    "visite": {
        "eyebrow":  "الاستشارات",
        "headline": "ستة مسارات سريرية، <em>توقيع واحد.</em>",
        "intro":
            "كلّ استشارة في Studio Marani هي مسار سريري محدّد، "
            "بمدّة وسعر وخطّة متابعة مكتوبة.",

        "service_image":
            "https://images.unsplash.com/photo-1530497610245-94d3c16cda28"
            "?auto=format&fit=crop&w=1400&q=80",
        "service_image_caption": "التشخيص القلبي · ستوديو ماراني",

        "treatments": [
            ("استشارة قلبية شاملة",
             "45 دقيقة · زيارة أولى",
             "استجواب سريري مفصّل، فحص جسدي، تخطيط كهربية القلب "
             "باثني عشر اتجاهاً، تقرير شخصي وخطّة متابعة مكتوبة.",
             "€ 220"),
            ("استشارة متابعة",
             "30 دقيقة · للمرضى المتابَعين",
             "مراجعة العلاج، تخطيط كهربية قلب للمتابعة، قراءة "
             "التحاليل المخبرية الحديثة.",
             "€ 140"),
            ("رأي تخصصي ثانٍ",
             "60 دقيقة · اعتماداً على الملف",
             "قراءة كاملة للتقارير والفحوصات التصويرية والملف "
             "السريري، مع تقرير نهائي موقَّع ومراجع علمية.",
             "€ 280"),
            ("تخطيط صدى القلب عبر الصدر",
             "30 دقيقة · داخل المركز",
             "فحص صدى قلب ثنائي الأبعاد ودوبلر ملوّن بنظام "
             "Philips EPIQ 7، مع تقرير في اليوم نفسه.",
             "€ 180"),
            ("هولتر قلبي 24 ساعة",
             "تسجيل + قراءة",
             "مراقبة كهربية قلبية على مدار 24 ساعة بنظام "
             "Schiller MT-200، قراءة وتقرير شخصي.",
             "€ 160"),
            ("برنامج وقاية 6 أشهر",
             "مسار سنوي",
             "أربع زيارات مجدولة، فحصان لكهربية القلب، هولتر واحد، "
             "تقييم متكامل بالتعاون مع أخصائي التغذية وطبيب الرياضة، "
             "قناة تواصل مباشرة مع الطبيب.",
             "€ 980"),
        ],

        "footnote":
            "جميع المدفوعات قابلة للخصم كنفقات صحية. يصدر المركز "
            "إيصالاً صحياً مع طابع مالي. للمرضى المقيمين خارج روما، "
            "يمكن الاتفاق على حزمة تتضمّن استشارة متابعة عن بُعد.",
        "footnote_heading": "ملاحظات إدارية",

        "cta_heading":
            "استشارة في Studio Marani <em>تُنسَّق شخصياً</em>.",
        "cta_primary_label":   "استمارة الطلب →",
        "cta_secondary_label": "الرقم المباشر للسكرتارية →",
    },

    "medici": {
        "eyebrow":  "الأطباء",
        "headline": "ثلاث تواقيع، <em>ملف سريري واحد.</em>",
        "intro":
            "يتكوّن المركز من ثلاثة أطباء قلب يتشاركون الملفات "
            "والمناهج ومعايير التقارير. غير أنّ لكلّ مريض طبيباً "
            "مرجعياً واحداً دائماً.",

        "portrait_city": "روما · باريولي",

        "doctors": [
            {
                "name":  "الدكتور ريكاردو ماراني",
                "role":  "المدير السريري · طبيب قلب",
                "tags":  ["الوقاية القلبية الوعائية", "الآراء الثانية", "طبّ القلب السريري"],
                "bio":
                    "متخصص في أمراض القلب من جامعة لا سابينزا في "
                    "روما، واستكمل تدريبه في تخطيط صدى القلب السريري "
                    "في معهد أمراض القلب في مونتريال. عضو في SIC و ESC. "
                    "مؤلف لأكثر من أربعين بحثاً محكَّماً، بما في ذلك "
                    "فصلان من الطبعة الإيطالية لكتاب Braunwald.",
                "portrait": _DR_MARANI_PORTRAIT,
                "links": [("PubMed", "#"), ("ORCID", "#")],
            },
            {
                "name":  "الدكتورة مارغريتا ساليري",
                "role":  "طبيبة قلب · مسؤولة برنامج الوقاية",
                "tags":  ["برنامج الوقاية", "طبّ القلب العائلي", "إعادة التأهيل"],
                "bio":
                    "تخرّجت في بولونيا، ونالت الدكتوراه في فسيولوجيا "
                    "القلب والأوعية الدموية في بادوفا. تنسّق منذ عام "
                    "2024 برنامج الوقاية القلبية الوعائية العائلي في "
                    "Studio Marani. تهتم بشكل خاص بالنساء في مرحلة ما "
                    "قبل انقطاع الطمث والعائلات ذات سوابق أحداث مبكرة.",
                "portrait": _DR_SALIERI_PORTRAIT,
                "links": [("السيرة الذاتية", "#")],
            },
            {
                "name":  "الدكتور أندريا لومباردي",
                "role":  "طبيب قلب · تشخيص بالتصوير",
                "tags":  ["تخطيط صدى القلب", "هولتر", "طبّ القلب الرياضي"],
                "bio":
                    "متخصص في مستشفى Sant'Andrea في روما، ومتدرّب في "
                    "تخطيط صدى القلب المتقدّم في مستشفى Saint-Joseph "
                    "في باريس. منذ 2018 هو المسؤول عن التشخيص "
                    "بالتصوير في المركز. مستشار طبّ القلب لناديي "
                    "كرة قدم في الدرجة الثانية.",
                "portrait": _DR_LOMBARDI_PORTRAIT,
                "links": [("المنشورات", "#")],
            },
        ],
    },

    "pubblicazioni": {
        "eyebrow":  "المنشورات والقراءات",
        "headline": "أبحاث علمية، <em>قراءات نقدية</em>، كتابة سريرية.",
        "intro":
            "مجموعة مختارة من منشورات المركز والنصوص التثقيفية "
            "المكتوبة للجمهور العام. تتمّ مراجعة جميع المواد شخصياً "
            "من قبل الدكتور ماراني قبل النشر.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Studio Marani · طبّ القلب السريري",
        "empty_body_fallback_paragraphs": [
            "المقال قيد الإعداد التحريري. سيُنشر النصّ الكامل قريباً.",
            "هذه الفقرة النموذجية تصف أسلوب المقال: ملاحظة سريرية "
            "يكتبها الطبيب بلغة مباشرة خالية من المصطلحات المعقّدة، "
            "مُوجَّهة إلى المرضى وذويهم الباحثين عن معلومات موثوقة.",
        ],
    },

    "posts": [
        {
            "slug":     "secondo-parere-quando-richiederlo",
            "kicker":   "الممارسة السريرية",
            "title":    "متى يصبح طلب رأي ثانٍ في أمراض القلب منطقياً فعلاً",
            "date":     "12 مارس 2026",
            "read_min": 6,
            "author":   "الدكتور ريكاردو ماراني",
            "lede":
                "الأمر ليس انعدام ثقة في الطبيب الأول. إنّه عملٌ من "
                "أعمال النظافة السريرية، ويحمي — إن أُحسن — المريض "
                "والطبيب المعالج والنظام الصحي كلّه.",
            "body": [
                ("p", "يستقبل المركز سنوياً نحو مئتي طلب للحصول على "
                      "رأي ثانٍ. في أغلب الأحيان يأتي هؤلاء المرضى "
                      "في حالة خوف: تشخيص مفاجئ، علاج معقّد، توصية "
                      "بإجراء جراحي. مهمّتنا الأولى هي خفض الحرارة "
                      "العاطفية للموقف."),
                ("h2", "ثلاث حالات يُستحسن فيها اللجوء إلى رأي ثانٍ"),
                ("ol", [
                    "تشخيص جديد وثقيل الأثر، يُتلقّى في ساعات قليلة أو في غرفة الطوارئ.",
                    "علاج دوائي طويل الأمد مع آثار جانبية ملحوظة.",
                    "توصية بإجراء تداخلي (زرع ناظمة، تقويم نظم، استئصال)."
                ]),
                ("p", "في جميع الحالات الأخرى — مراجعة سنوية بسيطة، "
                      "تغيّر طفيف في ضغط الدم، نوبة خفقان معزولة — "
                      "يكفي في الغالب حوار متأنٍّ مع طبيب القلب المعالج."),
                ("h2", "ما الذي يجب إحضاره عند طلب رأي ثانٍ"),
                ("p", "رأي ثانٍ بلا وثائق هو رأي خاطئ. للعمل بشكل "
                      "صحيح نحتاج إلى: رسالة خروج الطبيب المعالج، "
                      "جميع الفحوصات التصويرية في نسخها الأصلية "
                      "(تخطيط كهربية القلب، تخطيط صدى القلب، هولتر، "
                      "تصوير الأوعية التاجية عند الحاجة)، تحاليل الدم "
                      "خلال الأشهر الستة الماضية، وقائمة محدثة بالعلاج "
                      "الدوائي الحالي مع الجرعات وأوقات تناولها."),
                ("blockquote",
                 "الرأي الثاني لا يحلّ محلّ الطبيب المعالج: إنّه "
                 "يرافقه. حين يعمل الحوار بين الاختصاصيَّين، يربح "
                 "المريض مرّتين."),
            ],
        },
        {
            "slug":     "prevenzione-familiare-cardiovascolare",
            "kicker":   "الوقاية",
            "title":    "برنامج الوقاية القلبية الوعائية العائلي: ما يعنيه حقاً",
            "date":     "27 فبراير 2026",
            "read_min": 4,
            "author":   "الدكتورة مارغريتا ساليري",
            "lede":
                "ستة أشهر من المتابعة المتكاملة ليست صفقة تجارية. "
                "إنّها أداة سريرية لمن لديهم قرابة مباشرة بأحد "
                "المصابين بحدث قلبي مبكر.",
        },
        {
            "slug":     "ecocardiografia-quando-serve",
            "kicker":   "التشخيص",
            "title":    "تخطيط صدى القلب عبر الصدر: متى يكون ضرورياً فعلاً",
            "date":     "11 فبراير 2026",
            "read_min": 5,
            "author":   "الدكتور أندريا لومباردي",
            "lede":
                "لا يحتاج كلّ مريض يطلب «تخطيط صدى القلب» إلى "
                "إجراءه فعلاً. دليل نزيه إلى المؤشّرات السريرية "
                "الحقيقية وإلى الحالات التي يصبح فيها الفحص "
                "زائداً عن الحاجة.",
        },
        {
            "slug":     "donne-cuore-perimenopausa",
            "kicker":   "طبّ القلب بين الجنسين",
            "title":    "المرأة والقلب: صمت مرحلة ما قبل انقطاع الطمث",
            "date":     "23 يناير 2026",
            "read_min": 7,
            "author":   "الدكتورة مارغريتا ساليري",
            "lede":
                "لعقود طويلة بُنيت بروتوكولات طبّ القلب على "
                "مرضى ذكور. والنتيجة أنّ كثيراً من النساء بين "
                "الخامسة والأربعين والستين لا يزلن يتلقّين تشخيصاً "
                "متأخّراً أو خاطئاً حتى اليوم.",
        },
        {
            "slug":     "sport-amatoriale-controlli",
            "kicker":   "الرياضة والقلب",
            "title":    "الرياضة الهاوية: الفحوص القلبية التي تهمّ فعلاً",
            "date":     "8 يناير 2026",
            "read_min": 4,
            "author":   "الدكتور أندريا لومباردي",
            "lede":
                "ثلاث خرافات كبرى حول فحوصات ما قبل الرياضة "
                "الهاوية، يرويها مَن يوقّعها يومياً لدرّاجي "
                "وعدّائي وسبّاحي الأربعينيات والخمسينيات.",
        },
    ],

    "contatti": {
        "eyebrow":  "تواصل",
        "headline": "رقم واحد، <em>شخص واحد</em> على الطرف الآخر من الخط.",
        "intro":
            "يردّ المركز شخصياً على الاتصالات من الاثنين إلى الجمعة. "
            "تتولّى السكرتارية السيدة أديلي بيتروتشي، التي تعرف كلّ "
            "ملف وكلّ مريض بالاسم.",

        "blocks": [
            ("العنوان",     "Viale Parioli 142", "00197 روما · الدرج B، داخل 4"),
            ("الهاتف",       "+39 06 320 1144",   "خط مباشر 9:00 – 19:00"),
            ("البريد",       "studio@maranicardiologia.it", "الرد خلال يوم العمل نفسه"),
            ("الطوارئ",      "+39 335 642 8011",  "خط محجوز للمرضى المتابَعين"),
        ],

        "hours": [
            ("الاثنين",   "9:00 – 13:00", "15:00 – 19:00"),
            ("الثلاثاء",  "9:00 – 13:00", "15:00 – 19:00"),
            ("الأربعاء",  "9:00 – 13:00", "15:00 – 19:00"),
            ("الخميس",    "9:00 – 13:00", "15:00 – 19:00"),
            ("الجمعة",    "9:00 – 13:00", "—"),
            ("السبت",     "مغلق للجمهور", "على الاستعداد للمرضى المتابَعين"),
            ("الأحد",     "مغلق", "—"),
        ],

        "transport": [
            ("المترو",   "الخط B · Termini → الحافلة 168 محطة Parioli/Liegi"),
            ("السيارة",  "موقف متعاقد Q-Park Parioli، المدخل من Via Bertoloni"),
            ("القطار",   "محطة Termini · 12 دقيقة بسيارة أجرة"),
        ],

        "form_title": "اكتب إلى المركز",
        "form_intro":
            "للاستفسارات غير العاجلة — معلومات عن الاستشارات "
            "والأسعار والتفاصيل العملية — استخدم هذه الاستمارة. "
            "السكرتارية السريرية هي من يردّ شخصياً.",

        "hours_heading":     "ساعات العمل",
        "transport_heading": "كيفية الوصول",

        "form_placeholders": {
            "first_name": "محمد",
            "last_name":  "العلوي",
            "email":      "mohammed@email.com",
            "phone":      "+39 ...",
            "subject":    "استفسار عن استشارة متابعة",
            "message":
                "تكفي بضعة أسطر — ستعاود السكرتارية الاتصال "
                "بك خلال يوم العمل نفسه.",
        },
    },

    "richiedi-visita": {
        "eyebrow":  "طلب زيارة خاصة",
        "headline": "الزيارة الخاصة <em>لا تُحجز</em>: يُتَّفق عليها.",
        "intro":
            "لا يوجد جدول مواعيد عبر الإنترنت. يحتفظ المركز بكلّ "
            "زيارة أولى بعد قراءة وصف مختصر للحالة. يقوم الطبيب "
            "شخصياً بتقييم الطلبات خلال 48 ساعة عمل.",

        "process_label":   "كيف يتمّ ذلك",
        "process_heading": "أربع خطوات، خلال <em>أربعة أيام عمل.</em>",

        "process": [
            ("01", "املأ الاستمارة",
             "تكفي عشرة أسطر لتأطير طلبك. أرفق الفحوصات الحديثة إن "
             "أردت: هذا يغنيك عن طلبها منك مرّتين."),
            ("02", "قراءة سريرية",
             "يقرأ الطبيب شخصياً الطلب خلال 48 ساعة عمل، ويقرّر "
             "ما إذا كانت الزيارة الأولى من اختصاصه."),
            ("03", "اقتراح موعد",
             "إن كانت الحالة من اختصاصنا، تقترح السكرتارية "
             "فترتين زمنيتين تتوافقان مع توفّرك."),
            ("04", "التأكيد والملف",
             "بعد تأكيد الموعد، تتلقّى عبر البريد الإلكتروني "
             "قائمة الوثائق اللازمة وعنوان المركز مع تعليمات "
             "الوصول."),
        ],

        "form_title": "استمارة الطلب",
        "form_band_side_note":
            "خصّص بضع دقائق. الطلبات المكتوبة بعناية يقرأها الطبيب "
            "كاملةً — أمّا الطلبات المتسرّعة فلا.",
        "form_band_side_note_small": "↓ استمارة محجوزة",

        "form_fields": [
            {"label": "الاسم الكامل", "placeholder": "محمد العلوي",
             "type": "text", "full_width": False},
            {"label": "البريد الإلكتروني", "placeholder": "mohammed@email.com",
             "type": "email", "full_width": False},
            {"label": "الهاتف", "placeholder": "+39 ...",
             "type": "tel", "full_width": False},
            {"label": "العمر", "placeholder": "52",
             "type": "number", "full_width": False},
            {"label": "نوع الاستشارة", "type": "select", "full_width": False,
             "options": ["زيارة أولى", "رأي ثانٍ",
                         "برنامج وقاية", "استشارة متابعة"]},
            {"label": "الفترة المفضّلة", "type": "select", "full_width": False,
             "options": ["صباحاً", "بعد الظهر", "لا يهم"]},
            {"label": "الطبيب المعالج", "placeholder": "د. ...",
             "type": "text", "full_width": True},
            {"label": "وصف مختصر للحالة",
             "placeholder":
                 "الأعراض، الفحوصات السابقة، التشخيص الحالي، "
                 "العلاج الجاري. لا تتجاوز عشرة أسطر.",
             "type": "textarea", "full_width": True},
        ],

        "submit_label": "إرسال الطلب",

        "consent":
            "أوافق على معالجة بياناتي الشخصية وفقاً لإشعار الخصوصية "
            "وللائحة الاتحاد الأوروبي 679/2016. تُحفظ البيانات "
            "السريرية في أرشيف المركز الورقي حصراً.",

        "footnote":
            "لا يردّ المركز على الطلبات المجهولة، ولا يُصدر آراء "
            "سريرية عبر البريد الإلكتروني دون زيارة. للاستفسارات "
            "الإدارية (الأسعار، المواعيد، موقف السيارات) استخدم "
            "صفحة التواصل.",
    },
}
