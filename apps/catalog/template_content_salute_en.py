"""SALUTE_CONTENT_EN — native translation per D-072 multilingual voice law.

Voice contract (EN): British NHS/BUPA/Nuffield Health register — accessible,
reassuring, slightly formal. "The practice", "appointment booking", "clinical
team", "specialist consultation". Italian proper names preserved (SaluteVita,
Dr Elisa Conti, Via Galvani, Milan Centrale). Italian insurance schemes kept
with brief context gloss. Prices in euro (Italian practice). Hours styled
"Mon – Sat · 7:00 am – 9:00 pm".
"""
from __future__ import annotations

from typing import Any

from apps.catalog.template_content_salute import (
    ICO_STETHOSCOPE,
    ICO_BABY,
    ICO_DERM,
    ICO_ULTRASOUND,
    ICO_WOMAN,
    ICO_BONE,
    ICO_BRAIN,
    ICO_EYE,
)


SALUTE_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",        "label": "Home",          "kind": "home"},
        {"slug": "studio",      "label": "The practice",  "kind": "about"},
        {"slug": "servizi",     "label": "Services",      "kind": "services"},
        {"slug": "prevenzione", "label": "Prevention",    "kind": "prevention"},
        {"slug": "medici",      "label": "Clinicians",    "kind": "team"},
        {"slug": "contatti",    "label": "Contact",       "kind": "contact"},
        {"slug": "prenota",     "label": "Book",          "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "S",
        "logo_word":    "SaluteVita",
        "tag":          "Multi-specialty clinic · Milan Centrale",
        "phone_label":  "Freephone",
        "phone":        "800 123 456",
        "phone_tel":    "+39800123456",
        "email":        "book@salutevita.clinic",
        "address":      "Via Galvani 18 · 20124 Milan",
        "hours_compact": "Mon – Sat · 7:00 am – 9:00 pm",
        "hours_footer_rows": [
            "Mon – Fri · 7:00 am – 9:00 pm",
            "Sat · 8:00 am – 6:00 pm",
            "Sunday · closed",
        ],
        "foot_extra_label": "Insurance partners",
        "foot_extra_rows": [
            "Inail · Unisalute · Generali",
            "RBM Salute · Previmedical",
            "Caspie · MioDottore",
        ],
        "license": "Registered with ATS Milano healthcare facilities registry · VAT 09812345678",
        "footer_intro":
            "A multi-specialty practice in the heart of Milan Centrale. "
            "More than 40 clinicians across 12 departments, open six days a "
            "week — a trusted medical hub close to families since 1998.",
    },

    "home": {
        "eyebrow":   "Multi-specialty clinic · Milan Centrale · since 1998",
        "headline":  'Your health, our <em>everyday</em> work.',
        "subhead":
            "More than 40 specialists, joined-up diagnostic pathways and a "
            "patient experience designed to put you at ease from the very "
            "first call. Book online in 30 seconds, Mon – Sat, 7 am – 9 pm.",
        "primary_cta":    "Book an appointment",
        "primary_href":   "prenota",
        "secondary_cta":  "Freephone 800 123 456",
        "secondary_href": "contatti",
        "trust_note":     "Reply within two hours · no obligation",

        "stats": [
            ("40+",  "Specialist clinicians"),
            ("12",   "Departments"),
            ("98%",  "Patients who would return"),
        ],

        "booking_widget": {
            "aria_label":  "Three-step online booking",
            "title":       "Book online in 30 seconds",
            "subtitle":    "First slot usually within 48 working hours",
            "badge":       "6 slots still open today",
            "specialty_label": "Specialty",
            "specialty_value": "Cardiology",
            "date_label":      "Earliest available",
            "date_value":      "Tue 14 Apr · 10:30 am",
            "doctor_label":    "Clinician",
            "doctor_value":    "Dr Elisa Conti",
            "cta":             "Confirm appointment",
            "footnote":        "Free · cancel up to 24 h in advance",
            "secure_label":    "Encrypted data",
        },

        "stats_strip": [
            ("1998",    "Year founded"),
            ("28,000",  "Patients seen each year"),
            ("6",       "Days open each week"),
            ("€ 0",     "Cost of your first call"),
        ],

        "specialties_label": "Our specialties",
        "specialties_heading": 'Twelve departments under <em>one roof</em>.',
        "specialties_intro":
            "Every appointment a Milanese family is likely to need, kept "
            "under one coordinated roof: if your cardiologist requests a "
            "scan, we book it for you the same day, in the same building.",
        "specialties": [
            {
                "icon_svg": ICO_STETHOSCOPE,
                "title":    "Cardiology",
                "blurb":    "Cardiology consultation, resting and stress ECG, "
                            "echocardiography, 24-hour blood-pressure and Holter monitoring.",
                "link_label": "View the department",
            },
            {
                "icon_svg": ICO_BABY,
                "title":    "Paediatrics",
                "blurb":    "Well-child reviews from 0 to 14 years, vaccinations "
                            "and urgent paediatric advice within 24 hours.",
                "link_label": "View the department",
            },
            {
                "icon_svg": ICO_DERM,
                "title":    "Dermatology",
                "blurb":    "Digital-dermatoscopy mole mapping, dermatitis, "
                            "acne and skin-cancer screening.",
                "link_label": "View the department",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "title":    "Radiology & diagnostics",
                "blurb":    "Multi-organ ultrasound, CT, MRI and mammography. "
                            "Same-day report on request.",
                "link_label": "View the department",
            },
            {
                "icon_svg": ICO_WOMAN,
                "title":    "Gynaecology",
                "blurb":    "Obstetrics and gynaecology consultations, transvaginal "
                            "ultrasound, smear test and pregnancy pathways.",
                "link_label": "View the department",
            },
            {
                "icon_svg": ICO_BONE,
                "title":    "Orthopaedics & physiotherapy",
                "blurb":    "Orthopaedic consultation, ultrasound-guided "
                            "injections and post-operative rehabilitation with a dedicated physiotherapist.",
                "link_label": "View the department",
            },
            {
                "icon_svg": ICO_BRAIN,
                "title":    "Neurology",
                "blurb":    "Neurology consultation, EEG and assessment of "
                            "recurring headaches and sleep disorders.",
                "link_label": "View the department",
            },
            {
                "icon_svg": ICO_EYE,
                "title":    "Ophthalmology",
                "blurb":    "Comprehensive eye examination, retinal OCT, "
                            "visual-field test and cataract assessment in partnership "
                            "with affiliated surgical centres.",
                "link_label": "View the department",
            },
        ],

        "journey_label":    "The patient journey",
        "journey_heading":  'From booking to report, <em>four simple steps</em>.',
        "journey_intro":
            "We designed every step the way a family would want to be looked "
            "after: no queueing on your feet, no lost paperwork, no having "
            "to tell the same story twice.",
        "journey_steps": [
            {"num": "01", "title": "Online booking",
             "body": "Choose specialty, clinician and time slot in 30 seconds. "
                     "You receive an SMS reminder two days before."},
            {"num": "02", "title": "Welcome",
             "body": "Reception opens at 7 am. We walk you to the waiting room "
                     "and call you by name as soon as the clinician is ready."},
            {"num": "03", "title": "Consultation",
             "body": "Your clinician already has your clinical history to hand. "
                     "Thorough examination, same-day tests where possible."},
            {"num": "04", "title": "Digital report",
             "body": "Report and prescriptions in your patient area within 24 "
                     "hours, downloadable as PDF and shareable with your GP."},
        ],

        "prevenzione_label":   "Prevention check-ups",
        "prevenzione_heading": 'Prevention costs <em>less</em> than treatment.',
        "prevenzione_intro":
            "Three packages built around the age brackets where regular "
            "screening matters most. 15% off when you renew your check-up "
            "within 12 months.",
        "prevenzione_cards": [
            {
                "eyebrow":  "Women 40+",
                "title":    "Women 40+ check-up",
                "desc":     "Gynaecology consultation, pelvic ultrasound, smear test, "
                            "mammogram and nutrition review — all in a single morning.",
                "includes": [
                    "Comprehensive gynaecology consultation",
                    "Smear and HPV test",
                    "Pelvic ultrasound + mammogram",
                    "30-minute nutrition review",
                ],
                "duration_label": "Duration",
                "duration":       "3 hours",
                "price_label":    "All-inclusive price",
                "price":          "€ 320",
                "cta":            "Book the check-up",
            },
            {
                "eyebrow":  "Men 45+",
                "title":    "Men 45+ check-up",
                "desc":     "Cardiology, urology, metabolic screening, abdominal "
                            "and prostate ultrasound. Consolidated report within 48 hours.",
                "includes": [
                    "Cardiology consultation + ECG",
                    "Urology consultation + PSA",
                    "Full abdominal ultrasound",
                    "Lipid and metabolic profile",
                ],
                "duration_label": "Duration",
                "duration":       "3.5 hours",
                "price_label":    "All-inclusive price",
                "price":          "€ 280",
                "cta":            "Book the check-up",
            },
            {
                "eyebrow":  "Over 60",
                "title":    "Over-60 check-up",
                "desc":     "Cardiovascular, bone, neurological and eye assessment, "
                            "coordinated by a consultant in internal medicine who "
                            "pulls the whole picture together.",
                "includes": [
                    "Cardiology + echocardiogram + Holter",
                    "DEXA bone densitometry",
                    "Cognitive neurology consultation",
                    "Ophthalmology + tonometry",
                ],
                "duration_label": "Duration",
                "duration":       "4 hours",
                "price_label":    "All-inclusive price",
                "price":          "€ 420",
                "cta":            "Book the check-up",
            },
        ],

        "team_label":   "Our specialists",
        "team_heading": 'Eight faces <em>from our busiest departments</em>.',
        "team_intro":
            "More than 40 clinicians work with SaluteVita. Here you meet the "
            "heads of our eight most-booked departments — the full roster lives "
            "on a dedicated page.",
        "team_ribbon_people": [
            {
                "avatar": "https://images.pexels.com/photos/5327585/pexels-photo-5327585.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Elisa Conti",
                "specialty":"Cardiology",
            },
            {
                "avatar": "https://images.pexels.com/photos/5452293/pexels-photo-5452293.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Marco Ferri",
                "specialty":"Paediatrics",
            },
            {
                "avatar": "https://images.pexels.com/photos/5452274/pexels-photo-5452274.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Sofia Lenzi",
                "specialty":"Dermatology",
            },
            {
                "avatar": "https://images.pexels.com/photos/4173239/pexels-photo-4173239.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Luca Russo",
                "specialty":"Radiology",
            },
            {
                "avatar": "https://images.pexels.com/photos/5327921/pexels-photo-5327921.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Chiara Moretti",
                "specialty":"Gynaecology",
            },
            {
                "avatar": "https://images.pexels.com/photos/6129507/pexels-photo-6129507.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Paolo Serra",
                "specialty":"Orthopaedics",
            },
            {
                "avatar": "https://images.pexels.com/photos/7659562/pexels-photo-7659562.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Andrea Villa",
                "specialty":"Neurology",
            },
            {
                "avatar": "https://images.pexels.com/photos/5215024/pexels-photo-5215024.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Laura Bianchi",
                "specialty":"Ophthalmology",
            },
        ],
        "team_footnote_prefix": "More than 40 specialists make up the full clinical team.",
        "team_footnote_link":   "See every clinician",

        "partners_label":   "Insurance & partner schemes",
        "partners_heading": "We work directly with the leading Italian health insurers and mutual-benefit funds.",
        "partners": [
            "Inail", "Unisalute", "Generali Welion",
            "RBM Salute", "Previmedical", "Caspie",
            "MioDottore", "Consap",
        ],

        "cta_band": {
            "heading":      "Need an appointment this week?",
            "body":         "Book online in 30 seconds, or ring our freephone line: the team answers every day from 7 am to 9 pm.",
            "primary_cta":  "Book online",
            "primary_href": "prenota",
            "secondary_cta":"Call 800 123 456",
        },
    },

    "studio": {
        "eyebrow":   "The practice · in Milan since 1998",
        "headline":  'A trusted medical hub <em>close to people</em>.',
        "intro":
            "SaluteVita was founded in 1998 by three Milanese clinicians with "
            "one goal: to shorten the distance between the hospital and the "
            "family, offering a complete practice a few steps from Milan Centrale.",

        "values_label":   "Our values",
        "values_heading": 'Four things that <em>will not change</em>.',
        "values": [
            {"title": "Joined-up care",
             "body":  "No patient is sent away: if you need a test, we book it "
                      "for you in the same building. Shared reports across "
                      "every specialist who sees you."},
            {"title": "Welcome",
             "body":  "Reception answers the phone from 7 am. We call you by "
                      "name — no ticket numbers, no queueing on your feet."},
            {"title": "Technology that serves",
             "body":  "Digital clinical records, PDF reports within 24 hours, "
                      "digital dermatoscopy and a latest-generation 1.5T MRI scanner."},
            {"title": "Continuity",
             "body":  "If your daughter saw our paediatrician three years ago, "
                      "the orthopaedic team can pull up the same history when "
                      "she needs them today. No starting from scratch."},
        ],

        "photo_label":   "The practice",
        "photo_heading": "Four floors, twelve departments, one single reception.",
        "photo_body":
            "Via Galvani 18 houses consulting rooms, a phlebotomy suite, "
            "diagnostic imaging and physiotherapy. Everything sits on the "
            "ground or first floor, step-free throughout, with discounted "
            "parking 40 metres away.",
        "photo_caption": "Via Galvani 18 · Milan Centrale district",
        "photo_src":     "https://images.pexels.com/photos/7108324/pexels-photo-7108324.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",

        "timeline_label":   "Our story",
        "timeline_heading": 'Twenty-six years, <em>one constant</em>: the person in front of us.',
        "timeline": [
            {"year": "1998", "title": "The beginning",
             "body": "Three clinicians — a physician, a paediatrician and a "
                     "cardiologist — open the first practice on Via Galvani, 180 sqm."},
            {"year": "2008", "title": "The second floor",
             "body": "We open diagnostic imaging with MRI, CT and mammography. "
                     "Departments grow to eight."},
            {"year": "2018", "title": "Fully digital",
             "body": "We complete the move to fully digital records and the "
                     "online patient area. Every test reported within 24 hours."},
            {"year": "2024", "title": "Today",
             "body": "40+ specialists, 12 departments, 28,000 patients seen "
                     "each year. Still the family practice we set out to be."},
        ],

        "cta_band": {
            "heading":    "Would you like to meet us in person?",
            "body":       "Book your first appointment or simply drop in: reception opens at 7 am, no booking needed.",
            "primary_cta":"Book an appointment",
            "secondary_cta": "Call 800 123 456",
        },
    },

    "servizi": {
        "eyebrow":   "Services · 12 departments · 40+ specialists",
        "headline":  'Every appointment <em>a family could need</em>.',
        "intro":
            "From cardiology to physiotherapy, by way of paediatrics, "
            "dermatology and diagnostic imaging. Every consultation is "
            "bookable online, with transparent prices and dedicated prevention "
            "packages.",

        "svc_label":   "All services",
        "svc_heading": 'Specialist consultations, <em>transparent pricing</em>.',
        "price_label": "First consultation",
        "book_cta":    "Book",

        "services": [
            {
                "icon_svg": ICO_STETHOSCOPE,
                "eyebrow":  "Cardiology",
                "title":    "Cardiology consultation with ECG",
                "desc":     "Thorough history, auscultation, 12-lead ECG, "
                            "cardiovascular-risk assessment and guidance on "
                            "any further tests when clinically indicated.",
                "items":    ["ECG included", "Same-day report", "40 min"],
                "price":    "€ 140",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "eyebrow":  "Cardiology",
                "title":    "Colour-Doppler echocardiography",
                "desc":     "Morphological and functional assessment of the "
                            "heart with a latest-generation scanner. Useful for "
                            "murmurs, hypertension and post-event follow-up.",
                "items":    ["Doppler included", "Report in 24 h", "35 min"],
                "price":    "€ 160",
            },
            {
                "icon_svg": ICO_BABY,
                "eyebrow":  "Paediatrics",
                "title":    "Paediatric consultation 0–14",
                "desc":     "Well-child review covering growth, psychomotor "
                            "development and nutrition. Vaccination advice "
                            "aligned with the regional schedule on request.",
                "items":    ["0–14 years", "Urgent slot within 24 h", "45 min"],
                "price":    "€ 120",
            },
            {
                "icon_svg": ICO_DERM,
                "eyebrow":  "Dermatology",
                "title":    "Mole mapping with digital dermatoscopy",
                "desc":     "Skin-cancer screening with a video-dermatoscope. "
                            "Images archived for year-on-year comparison. "
                            "Recommended from 30 years of age.",
                "items":    ["5-year archive", "Digital imaging", "40 min"],
                "price":    "€ 180",
            },
            {
                "icon_svg": ICO_WOMAN,
                "eyebrow":  "Gynaecology",
                "title":    "Obstetrics & gynaecology consultation + scan",
                "desc":     "Full consultation with transvaginal or abdominal "
                            "ultrasound. Dedicated pathways for first pregnancy "
                            "and menopause.",
                "items":    ["Smear test available", "Scan included", "45 min"],
                "price":    "€ 150",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "eyebrow":  "Radiology",
                "title":    "1.5T MRI scan",
                "desc":     "Latest-generation open scanner, suited to "
                            "claustrophobic patients too. Radiology report "
                            "within 24 working hours.",
                "items":    ["Open · claustrophobia-friendly", "Report in 24 h", "30 min"],
                "price":    "from € 220",
            },
            {
                "icon_svg": ICO_BONE,
                "eyebrow":  "Orthopaedics",
                "title":    "Orthopaedic consultation + musculoskeletal ultrasound",
                "desc":     "Clinical and ultrasound assessment in a single "
                            "session. Ultrasound-guided injections of hyaluronic "
                            "acid or corticosteroid where indicated.",
                "items":    ["Ultrasound included", "Injections available", "40 min"],
                "price":    "€ 150",
            },
            {
                "icon_svg": ICO_BONE,
                "eyebrow":  "Physiotherapy",
                "title":    "Rehabilitation physiotherapy session",
                "desc":     "Tailored pathway with a dedicated physiotherapist, "
                            "following referral from the orthopaedic team or your "
                            "GP. Bundles of 5 and 10 sessions available.",
                "items":    ["Session bundles", "Post-surgery", "50 min"],
                "price":    "€ 55 · session",
            },
            {
                "icon_svg": ICO_BRAIN,
                "eyebrow":  "Neurology",
                "title":    "Neurology consultation with EEG",
                "desc":     "Assessment of headaches, sleep disorders and "
                            "tremors, with an optional EEG in the same session. "
                            "Cognitive testing on request.",
                "items":    ["EEG available", "Cognitive tests", "50 min"],
                "price":    "€ 170",
            },
            {
                "icon_svg": ICO_EYE,
                "eyebrow":  "Ophthalmology",
                "title":    "Comprehensive eye examination",
                "desc":     "Visual acuity, tonometry, fundus examination and "
                            "retinal OCT. Cataract-surgery assessment in "
                            "partnership with affiliated surgical centres.",
                "items":    ["OCT included", "Tonometry", "35 min"],
                "price":    "€ 130",
            },
        ],

        "faq_label":   "Frequently asked",
        "faq_heading": 'The <em>three</em> questions we hear most often.',
        "faqs": [
            ("Can I use my health insurance or mutual-benefit scheme?",
             "Yes. SaluteVita has direct agreements with Unisalute, Generali "
             "Welion, RBM Salute, Previmedical, Caspie and Consap. In most "
             "cases the scheme settles the cost directly, with no upfront "
             "payment. Send us your card when you book and we confirm cover "
             "within 24 hours."),
            ("How soon do I get my report?",
             "Clinical consultations: digital report in your patient area "
             "within 24 working hours. Diagnostic imaging (ultrasound, CT, "
             "MRI): radiology report in 24 to 48 hours. If you need it on "
             "the same day, just ask when you book — it is almost always "
             "possible."),
            ("Can I cancel or move my appointment?",
             "Of course. You can reschedule or cancel from your patient "
             "area up to 24 hours in advance, at no cost. Inside 24 hours, "
             "ring our freephone line on 800 123 456: we treat each case on "
             "its merits, with no penalty for medical reasons."),
        ],

        "cta_band": {
            "heading":    "Pick the service, we handle the rest.",
            "body":       "Book online in a few seconds: if the specialty you need is not listed, ring our freephone line and we will point you the right way.",
            "primary_cta":"Book an appointment",
            "secondary_cta":"Call 800 123 456",
        },
    },

    "prevenzione": {
        "eyebrow":   "Prevention · three dedicated pathways",
        "headline":  'A full check-up in <em>half a day</em>.',
        "intro":
            "Three packages built for the age brackets where screening "
            "matters most — women 40+, men 45+, over 60. A consultant in "
            "internal medicine coordinates everything and delivers a single "
            "report within 48 hours.",

        "pack_label":   "The three pathways",
        "pack_heading": 'Choose by <em>age and profile</em>.',
        "duration_label": "Duration",
        "exams_label":    "Tests",

        "packages": [
            {
                "eyebrow": "WOMEN 40+",
                "title":   "Women 40+ check-up",
                "desc":    "Designed for anyone who wants to keep gynaecological, "
                           "breast and metabolic health in check, all in one morning.",
                "price":   "€ 320",
                "price_meta": "all inclusive",
                "duration": "3 hours",
                "exams_count": "7 tests",
                "includes": [
                    "Gynaecology consultation with pelvic ultrasound",
                    "Smear and HPV test",
                    "Bilateral mammogram",
                    "30-minute nutrition review",
                    "Metabolic-profile blood work",
                    "Breast follow-up consultation",
                    "Consolidated report within 48 hours",
                ],
                "cta":      "Book the check-up",
                "is_popular": True,
                "popular_label": "Most booked",
            },
            {
                "eyebrow": "MEN 45+",
                "title":   "Men 45+ check-up",
                "desc":    "The screening we all put off and never should: "
                           "heart, prostate, metabolism, liver — all in one half-day.",
                "price":   "€ 280",
                "price_meta": "all inclusive",
                "duration": "3.5 hours",
                "exams_count": "7 tests",
                "includes": [
                    "Cardiology consultation with ECG",
                    "Colour-Doppler echocardiography",
                    "Urology consultation with PSA",
                    "Full abdominal ultrasound",
                    "Lipid and glucose profile",
                    "Cardiovascular-risk assessment",
                    "Consolidated report within 48 hours",
                ],
                "cta":      "Book the check-up",
                "is_popular": False,
                "popular_label": "",
            },
            {
                "eyebrow": "OVER 60",
                "title":   "Over-60 check-up",
                "desc":    "A complete picture coordinated by a consultant in "
                           "internal medicine who keeps heart, bones, brain and eyes all in view.",
                "price":   "€ 420",
                "price_meta": "all inclusive",
                "duration": "4 hours",
                "exams_count": "9 tests",
                "includes": [
                    "Cardiology + echocardiogram + 24-hour Holter",
                    "DEXA bone densitometry",
                    "Neurology consultation with cognitive tests",
                    "Ophthalmology with retinal OCT",
                    "Tonometry and visual-field test",
                    "Full metabolic profile",
                    "Coordinating internal-medicine consultation",
                    "Final review with the lead clinician",
                    "Consolidated report within 48 hours",
                ],
                "cta":      "Book the check-up",
                "is_popular": False,
                "popular_label": "",
            },
        ],

        "how_label":   "How it works",
        "how_heading": 'Four steps, <em>no surprises</em>.',
        "how_steps": [
            {"num": "01", "title": "Book online",
             "body": "Choose the check-up that suits you and a day. You "
                     "receive an email with the preparation instructions."},
            {"num": "02", "title": "Fasting in the morning",
             "body": "The blood work needs an 8-hour fast. Still water is "
                     "allowed up to an hour before you arrive."},
            {"num": "03", "title": "Half a morning with us",
             "body": "You arrive at 7:30 am and leave by noon. Every test is "
                     "lined up back-to-back, with no waiting in between."},
            {"num": "04", "title": "One report within 48 hours",
             "body": "The lead clinician calls you to walk through the "
                     "results and hand over the consolidated PDF."},
        ],

        "cta_band": {
            "heading":    "One check-up a year, better nights of sleep.",
            "body":       "Book today; we call you back within two working hours to confirm the date and preparation details.",
            "primary_cta":"Book a check-up",
            "secondary_cta":"Call 800 123 456",
        },
    },

    "medici": {
        "eyebrow":   "Clinicians · 40+ specialists",
        "headline":  'The team that will <em>look after you</em>.',
        "intro":
            "Here are the six clinicians who lead our most-booked departments. "
            "The full team is more than 40 specialists strong: if you are "
            "looking for someone in particular, ring reception and we will help.",

        "book_cta": "Book with this clinician",

        "doctors": [
            {
                "portrait": "https://images.pexels.com/photos/5327585/pexels-photo-5327585.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Cardiology · department head",
                "name":     "Dr Elisa Conti",
                "credentials":
                    "Cardiology specialty training at the University of Milan. "
                    "22 years of clinical practice, with further training at "
                    "Centro Cardiologico Monzino. Member of the Italian Society "
                    "of Cardiology.",
                "tags": ["Cardiology", "Echocardiography", "CV prevention"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5452293/pexels-photo-5452293.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Paediatrics · department head",
                "name":     "Dr Marco Ferri",
                "credentials":
                    "Community paediatrician, specialty training at Clinica De "
                    "Marchi. 18 years caring for Milanese families, with a "
                    "focus on neonatology and childhood respiratory conditions.",
                "tags": ["0–14 years", "Vaccinations", "Paediatric respiratory"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5452274/pexels-photo-5452274.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Dermatology",
                "name":     "Dr Sofia Lenzi",
                "credentials":
                    "Dermatologist, specialty training at Università Vita-Salute "
                    "San Raffaele. A decade of experience in digital dermatoscopy "
                    "and skin-cancer surveillance.",
                "tags": ["Dermatoscopy", "Skin oncology", "Acne"],
            },
            {
                "portrait": "https://images.pexels.com/photos/4173239/pexels-photo-4173239.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Radiology · director of imaging",
                "name":     "Dr Luca Russo",
                "credentials":
                    "Radiologist with 25 years of hospital experience before "
                    "joining SaluteVita in 2015. MRI and CT lead, heads a team "
                    "of six radiographers.",
                "tags": ["1.5T MRI", "CT", "Multi-organ ultrasound"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5327921/pexels-photo-5327921.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Gynaecology · obstetrics",
                "name":     "Dr Chiara Moretti",
                "credentials":
                    "Gynaecologist and obstetrician, specialty training at "
                    "Clinica Mangiagalli. Leads low-risk pregnancy pathways, "
                    "menopause care and women's cancer screening.",
                "tags": ["Pregnancy", "Menopause", "Smear + HPV"],
            },
            {
                "portrait": "https://images.pexels.com/photos/6129507/pexels-photo-6129507.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Orthopaedics · sports medicine",
                "name":     "Dr Paolo Serra",
                "credentials":
                    "Orthopaedic surgeon, specialty training at Istituto Galeazzi. "
                    "Expert in musculoskeletal ultrasound and ultrasound-guided "
                    "injections, treats Serie A athletes and recreational sportspeople alike.",
                "tags": ["Musculoskeletal ultrasound", "Injections", "Sports medicine"],
            },
        ],

        "footnote_strong": "More than 40 specialists make up the full team.",
        "footnote_body":
            "Neurology, ophthalmology, ENT, urology, endocrinology and another "
            "seven specialties. Reach out to reception for help choosing the "
            "right clinician for your needs: ",
        "footnote_link": "message us from the contact page",
    },

    "contatti": {
        "eyebrow":   "Contact · Via Galvani 18 · Milan",
        "headline":  'We are <em>where you need us</em>: a few steps from Milan Centrale.',
        "intro":
            "Reception is open 7 am to 9 pm, Monday to Friday. Write to us or "
            "ring in: we reply within two working hours, with no automated "
            "answering service.",

        "map_aria":    "Illustrative map of the SaluteVita premises at Via Galvani 18, Milan",
        "map_stamp":   "Via Galvani 18 · Milan Centrale",

        "address_label": "Address",
        "email_label":   "Email",

        "hours_heading": "Opening hours",
        "hours_table": [
            ("Monday – Friday", "7:00 am – 9:00 pm"),
            ("Saturday",        "8:00 am – 6:00 pm"),
            ("Sunday",          "Closed"),
            ("Bank holidays",   "Closed · freephone line active"),
        ],

        "access": [
            {"icon": "car",        "title": "Partner car park",
             "body": "Garage Centrale 40 metres away. € 2 per hour for SaluteVita patients."},
            {"icon": "metro",      "title": "Metro",
             "body": "M2/M3 Milan Centrale · a 4-minute walk. Trams 5 and 9 outside the door."},
            {"icon": "wheelchair", "title": "Step-free access",
             "body": "Step-free entrance, lift and accessible WC on the ground floor."},
            {"icon": "info",       "title": "Emergencies",
             "body": "We are not an A&E service. For medical emergencies please call 112."},
        ],

        "form_title": "Send us a message",
        "form_intro":
            "For a general question or information before booking, drop us a "
            "line here. We reply within two working hours.",

        "form_fields": [
            {"name": "nome",       "label": "First name",  "type": "text",     "placeholder": "Mario",                  "required": True},
            {"name": "cognome",    "label": "Surname",     "type": "text",     "placeholder": "Rossi",                  "required": True},
            {"name": "email",      "label": "Email",       "type": "email",    "placeholder": "mario.rossi@email.com",  "required": True},
            {"name": "telefono",   "label": "Phone",       "type": "tel",      "placeholder": "+39 ...",                "required": False},
            {"name": "specialita", "label": "Specialty of interest", "type": "select", "required": False,
             "options": ["Cardiology", "Paediatrics", "Dermatology", "Radiology",
                         "Gynaecology", "Orthopaedics", "Neurology", "Ophthalmology",
                         "Other / general information"]},
            {"name": "oggetto",    "label": "Subject",     "type": "text",     "placeholder": "Prevention information", "required": True},
            {"name": "messaggio",  "label": "Message",     "type": "textarea", "placeholder": "Tell us briefly what you need…",
             "required": True, "full_width": True,
             "helper": "Please do not share sensitive medical data in this form: for reports use your patient area."},
        ],
        "consent":
            "I consent to the processing of my personal data under EU Regulation "
            "2016/679, for the sole purpose of responding to this enquiry.",
        "submit_label": "Send message",
        "form_note":    "Reply within two working hours",
    },

    "prenota": {
        "eyebrow":   "Book · online in 30 seconds",
        "headline":  'Tell us when, <em>we handle the rest</em>.',
        "intro":
            "Fill in the form below: we call you back within two working "
            "hours to confirm the date, clinician and preparation. If you "
            "would rather speak to a person, ring freephone 800 123 456.",

        "form_sections": [
            {"num": "01", "title": "Your details", "meta": "so we can contact you",
             "fields": ["nome", "cognome", "email", "telefono", "data_nascita", "codice_fiscale"]},
            {"num": "02", "title": "Appointment details", "meta": "type and specialty",
             "fields": ["specialita", "medico_preferito", "tipo_visita", "convenzione"]},
            {"num": "03", "title": "When suits you", "meta": "we call back to confirm",
             "fields": ["data_preferita", "fascia_orario", "note"]},
        ],

        "form_fields": [
            {"name": "nome",            "label": "First name",      "type": "text",  "placeholder": "Mario",                    "required": True},
            {"name": "cognome",         "label": "Surname",         "type": "text",  "placeholder": "Rossi",                    "required": True},
            {"name": "email",           "label": "Email",           "type": "email", "placeholder": "mario.rossi@email.com",    "required": True,
             "helper": "We send SMS reminders and the digital report here."},
            {"name": "telefono",        "label": "Phone",           "type": "tel",   "placeholder": "+39 335 ...",              "required": True},
            {"name": "data_nascita",    "label": "Date of birth",   "type": "date",  "placeholder": "dd/mm/yyyy",               "required": True},
            {"name": "codice_fiscale",  "label": "Italian tax code","type": "text",  "placeholder": "RSSMRA80A01F205X",         "required": False,
             "helper": "Helpful if you have insurance cover — we process it faster."},
            {"name": "specialita",      "label": "Specialty",       "type": "select","required": True,
             "options": ["Cardiology", "Paediatrics", "Dermatology",
                         "Radiology & diagnostics", "Gynaecology",
                         "Orthopaedics & physiotherapy", "Neurology", "Ophthalmology",
                         "Prevention check-up", "Other specialty"]},
            {"name": "medico_preferito","label": "Preferred clinician","type": "select","required": False,
             "options": ["No preference · first available",
                         "Dr Elisa Conti · Cardiology",
                         "Dr Marco Ferri · Paediatrics",
                         "Dr Sofia Lenzi · Dermatology",
                         "Dr Luca Russo · Radiology",
                         "Dr Chiara Moretti · Gynaecology",
                         "Dr Paolo Serra · Orthopaedics",
                         "Dr Andrea Villa · Neurology",
                         "Dr Laura Bianchi · Ophthalmology"]},
            {"name": "tipo_visita",     "label": "Appointment type","type": "select","required": True,
             "options": ["First consultation", "Follow-up consultation", "Diagnostic test",
                         "Urgent review (within 24–48 h)"]},
            {"name": "convenzione",     "label": "Using an insurance scheme?", "type": "select", "required": False,
             "options": ["None · private payment",
                         "Unisalute", "Generali Welion", "RBM Salute",
                         "Previmedical", "Caspie", "MioDottore", "Consap",
                         "Inail", "Other insurer / mutual fund"]},
            {"name": "data_preferita",  "label": "Preferred date",  "type": "date",  "placeholder": "dd/mm/yyyy", "required": True,
             "helper": "Choose within 30 days. If an earlier slot opens, we let you know."},
            {"name": "fascia_orario",   "label": "Time band",       "type": "select","required": True,
             "options": ["Early morning · 7:00 – 9:00 am",
                         "Morning · 9:00 am – 12:00 pm",
                         "Early afternoon · 1:00 – 4:00 pm",
                         "Late afternoon · 4:00 – 7:00 pm",
                         "Evening · 7:00 – 9:00 pm",
                         "No preference"]},
            {"name": "note",            "label": "Notes for the clinician", "type": "textarea",
             "placeholder": "Jot down any symptoms, current medication or specific questions…",
             "required": False, "full_width": True,
             "helper": "Optional. We only ask for what the clinician needs to prepare."},
        ],

        "consent":
            "I consent to the processing of my personal data under EU Regulation "
            "2016/679 and the SaluteVita privacy notice. The data will be used "
            "solely to manage this booking.",
        "submit_label":     "Confirm appointment",
        "form_submit_note": "We call you back within two working hours",

        "help_title": "How booking works",
        "help_steps": [
            {"num": "1", "title": "You fill in the form",
             "body": "Ninety seconds is enough. No upfront payment required."},
            {"num": "2", "title": "We call you back within two hours",
             "body": "A member of reception confirms the date, clinician and preparation."},
            {"num": "3", "title": "SMS reminder",
             "body": "Two days before, an SMS with date, time and consulting room."},
            {"num": "4", "title": "Digital report",
             "body": "Within 24–48 hours your report and prescriptions land in your patient area, downloadable as PDF."},
        ],

        "alt_title": "Would you rather speak to a person?",
        "alt_body":
            "The freephone line is open seven days a week, 7 am to 9 pm. Our average pick-up time is under 40 seconds.",

        "trust": [
            "End-to-end encrypted data (AES-256, healthcare standard)",
            "Cancel or reschedule up to 24 h before, at no cost",
            "Direct agreements with 8 leading insurers and mutual funds",
        ],
    },
}

__all__ = ["SALUTE_CONTENT_EN"]
