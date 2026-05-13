"""Content tree · `petro-veterinario` · T52 multilingual rollout (EN).

English translation of `PETRO_CONTENT_IT`. Built for the marketweb T52
multilingual pass (IT → EN/FR/ES/AR · AAA walk · public flip). Shape
parity contract enforced against `template_content_petro.py`:

  * Same top-level keys, same nested keys at every depth.
  * Same list lengths (5 history rows, 4 values, 8 treatments,
    3 doctors, 2 posts, 4 contatti blocks, 3 hours rows, 4 transport,
    3 process steps, 7 form fields, etc.).
  * Same tuple positions for tuple-typed values (home.facts 2-tuples,
    home.signature_visits 3-tuples, studio.history 2-tuples,
    studio.values 2-tuples, visite.treatments 4-tuples,
    contatti.blocks 3-tuples, contatti.hours 3-tuples,
    contatti.transport 2-tuples, richiedi-visita.process 3-tuples).
  * Same `pages[].slug` values (labels translated, slugs preserved).
  * Same `posts[].slug` values, same `page kind`.

Voice anchor — `preventive care` (preventive-medicine veterinary
register · AVMA Journal / Royal Veterinary College / Cornell Vet
artisan-vet idiom · American spelling, NOT "preventative") carries
the IT `cura preventiva` load-bearing promise across the same
surfaces (hero H1 with `<em>` italic emphasis, manifesto, cta_heading,
studio values, visite, signature_visits, doctor bios). Italian
heritage proper-names (Padova, Borgo Trento, Via Belzoni 71,
Università di Padova, Royal Veterinary College London, Cornell
University Vet School, Ospedale Veterinario di Legnaro, Clinica
San Marco di Veggiano, SCIVAC, ANMVI, AAEMV, Esaote MyLab Omega,
Carestream, OMV Padova 1428) preserved verbatim. Brand name
`Studio Veterinario Petro` preserved. Veterinary technical terms
(WSAVA, DA2PPi-L, FRCP+FeLV, RHDV1+2, Mixoma, BCS, laparoscopy)
kept Anglo. Lead practitioner is `Dr. Marco Petro, veterinarian`
(Anglo · NOT "vet" colloquial); secondary `Dr. Anna Bressan,
exotic-animals veterinarian`.
"""
from __future__ import annotations

from typing import Any


# Imagery URLs from the X.3 curator pack
# `docs/content-factory/imagery/packs/veterinary.md`. All URLs
# Pexels License (CC0-compatible · commercial use OK).
_CHIEF_PORTRAIT = (
    # Veterinarian with white coat examining a small dog · matches
    # Dr. Petro "lead veterinarian" hands-on persona
    "https://images.pexels.com/photos/6235648/pexels-photo-6235648.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_STUDIO_IMAGE = (
    # Veterinary clinic interior — exam table + bright clinical
    "https://images.pexels.com/photos/7468978/pexels-photo-7468978.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop"
)
_LEAD_IMAGE = (
    # Bright veterinary clinic consultation · used as blog_list lead
    "https://images.pexels.com/photos/6235244/pexels-photo-6235244.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)
_MAP_FALLBACK = (
    # Modern veterinary clinic reception · map-fallback when Mapbox
    # tile fails to load
    "https://images.pexels.com/photos/6235241/pexels-photo-6235241.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)
_SERVICE_IMAGE = (
    # Vet auscultating cat patient close-up — visite page hero
    "https://images.pexels.com/photos/7470779/pexels-photo-7470779.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=900&fit=crop"
)


PETRO_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Practice",              "kind": "home"},
        {"slug": "studio",          "label": "The Practice",          "kind": "about"},
        {"slug": "visite",          "label": "Visits",                "kind": "services"},
        {"slug": "medici",          "label": "Veterinarians",         "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Clinical journal",      "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contact",               "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Book a visit",          "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "P",
        "logo_word":    "Petro",
        "tag":          "Veterinary practice · Padova Borgo Trento · dogs cats exotic pets",
        "phone":        "+39 049 6731 220",
        "email":        "studio@studiopetro.it",
        "address":      "Via Belzoni 71 · 35121 Padova",
        "hours_compact": "Mon – Fri · 8:00 AM – 8:00 PM · Sat 9:00 AM – 1:00 PM",
        "hours_footer_rows": [
            "Sunday · emergencies on call only",
            "24/7 night on-call line · +39 333 410 7726",
        ],
        "license":      "OMV Padova Veterinary Register no. 1428 · Clinical director Dr. M. Petro",
        "footer_intro":
            "Independent veterinary practice focused on preventive "
            "care, soft-tissue surgery and geriatric medicine for "
            "dogs, cats and small exotic pets. Three veterinarians, "
            "one shared chart per animal, night on-call line.",
    },

    "home": {
        "hero_variant": "split-consultive",
        "eyebrow":  "Veterinary medicine · Padova Borgo Trento",
        "headline": "Animals don't speak. <em>Preventive care</em> listens first.",
        "intro":
            "Annual preventive check-ups, scheduled vaccinations, "
            "diagnostic imaging and soft-tissue surgery for dogs, "
            "cats and small exotic pets. Three associate "
            "veterinarians, 24/7 night on-call line, one shared "
            "clinical chart per patient.",
        "primary_cta":   "Book a preventive check-up",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "The veterinarians",
        "secondary_href":"medici",

        "facts": [
            ("17",    "years of independent veterinary practice"),
            ("4,200", "animals treated each year"),
            ("3",     "associate veterinarians on site"),
        ],

        "manifesto_drop_cap": "A",
        "manifesto":
            "nimals don't describe pain: they hide it. The cat "
            "hides, the dog eats less, the rabbit stops moving. "
            "That's why at Petro medicine is above all preventive "
            "care — a full annual check-up, a six-month geriatric "
            "screening from age seven onwards, a dental check every "
            "two years, scheduled vaccinations. By the time an "
            "animal arrives at the practice with visible symptoms, "
            "we're often already halfway through the problem. Our "
            "clinical chart exists so we can get there sooner.",

        "hero_sidebar_top_label": "Clinical direction",
        "hero_sidebar_quote":
            "«Animals don't tell us where it hurts. The "
            "preventive check-up is the only honest way to "
            "practice veterinary medicine — the rest is just "
            "emergency work.»",
        "hero_sidebar_author": "— Dr. Marco Petro · Clinical director · OMV Padova 1428",
        "hero_sidebar_pulse": [
            ("Practice",  "Padova · Borgo Trento"),
            ("Since",     "2008"),
            ("Reference", "Dogs cats exotic pets"),
        ],

        "anchor_nav": [
            ("metodo",        "Clinical method"),
            ("visite",        "Preventive check-ups"),
            ("percorso",      "Patient pathway"),
            ("medico",        "Clinical direction"),
            ("studio",        "Practice & contact"),
        ],

        "signature_visits_label":   "Four families of care",
        "signature_visits_heading": "Four clinical pathways, <em>one shared chart per animal.</em>",
        "signature_visits_intro":
            "The four most-requested families in small-animal "
            "veterinary medicine. The full list lives on the Visits "
            "page.",
        "signature_visits": [
            ("01", "Annual preventive check-up",
             "Complete physical exam, weight and BCS, cardiopulmonary "
             "auscultation, abdominal palpation, dental check, "
             "vaccination history and parasite prophylaxis review. "
             "Forty minutes, by appointment."),
            ("02", "Vaccinations & prophylaxis",
             "Dog (DA2PPi-L) and cat (FRCP-FeLV) vaccines on the "
             "WSAVA schedule. Heartworm, leishmania and tick "
             "prophylaxis. Rabbit (RHDV-Mixoma) and ferret "
             "vaccines. Health record updated on site."),
            ("03", "Soft-tissue surgery",
             "Laparoscopic spay/neuter for dogs and cats "
             "(minimally invasive, shorter recovery), removal of "
             "skin lesions, oncologic surgery with histology, "
             "subcuticular cosmetic sutures."),
            ("04", "Diagnostic imaging",
             "On-site abdominal and cardiac ultrasound, digital "
             "radiography with images handed to the owner, "
             "fine-needle aspirate cytology read within 24 hours "
             "by the partner lab at the Università di Padova."),
        ],

        "trattamenti_tabs": {
            "label":   "Visit & procedure price list",
            "heading": "What we do, with <em>what criteria.</em>",
            "intro":
                "Four clinical families, each with a written "
                "protocol and a stated cost. No custom quotes for "
                "routine items — only for structured care plans "
                "(complex surgery, oncology therapy, "
                "rehabilitation).",
            "tabs": [
                {
                    "id":      "preventiva",
                    "label":   "Preventive",
                    "eyebrow": "Preventive medicine",
                    "heading": "Forty minutes, once a year.",
                    "body":
                        "The annual preventive check-up is not a quick "
                        "control: it is a complete forty-minute "
                        "clinical assessment with history, systematic "
                        "physical exam, dental check, weight/BCS, "
                        "auscultation and palpation. From age seven "
                        "onwards we add the six-month geriatric "
                        "screening.",
                    "items": [
                        ("Annual preventive check-up · dog/cat", "40 min · €65"),
                        ("Geriatric screening (≥ 7 years)", "60 min · €95"),
                        ("Preventive check-up · exotic (rabbit/ferret)", "45 min · €75"),
                        ("Pre-adoption visit · puppy/kitten", "30 min · €50"),
                    ],
                    "cta_label": "All preventive protocols →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "vaccinazioni",
                    "label":   "Vaccinations",
                    "eyebrow": "Vaccines & parasite prophylaxis",
                    "heading": "WSAVA protocol, record kept on site.",
                    "body":
                        "Vaccines follow the WSAVA guidelines (dog "
                        "DA2PPi-L core annual, cat FRCP-FeLV core "
                        "triennial after the booster). The health "
                        "record is issued on site, including an "
                        "electronic version via app. Monthly or "
                        "quarterly antiparasite prophylaxis depending "
                        "on breed and environment.",
                    "items": [
                        ("Dog DA2PPi-L vaccine (annual)", "appointment · €45"),
                        ("Cat FRCP + FeLV vaccine", "appointment · €55"),
                        ("Rabbit RHDV1+2 / Mixoma vaccine", "appointment · €50"),
                        ("Heartworm + tick prophylaxis (12 months)", "plan · €95"),
                    ],
                    "cta_label": "Full vaccination calendar →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "chirurgia",
                    "label":   "Surgery",
                    "eyebrow": "Soft-tissue surgery",
                    "heading": "Minimally invasive laparoscopy wherever possible.",
                    "body":
                        "Laparoscopic spay/neuter for dogs and cats "
                        "(three small access points · day "
                        "hospitalisation · reduced post-operative "
                        "pain). Removal of skin lesions with "
                        "histology performed at the Pathology Lab of "
                        "the Università di Padova. Resorbable "
                        "subcuticular cosmetic sutures.",
                    "items": [
                        ("Cat spay (laparoscopic)", "procedure · €320"),
                        ("Dog spay < 20 kg", "procedure · €480"),
                        ("Dog spay > 20 kg", "procedure · €620"),
                        ("Skin lesion removal + histology", "procedure · €220"),
                    ],
                    "cta_label": "Full surgical pathways →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "diagnostica",
                    "label":   "Diagnostics",
                    "eyebrow": "Imaging & laboratory diagnostics",
                    "heading": "Ultrasound, digital X-ray, cytology within 24 h.",
                    "body":
                        "On-site abdominal and cardiac ultrasound "
                        "with Esaote MyLab Omega · Carestream "
                        "digital radiography with images delivered "
                        "to the owner via cloud · fine-needle "
                        "aspirate cytology read within 24 hours by "
                        "the Pathology Lab of the Università di "
                        "Padova. On-site blood chemistry results "
                        "in 30 minutes.",
                    "items": [
                        ("Complete abdominal ultrasound", "30 min · €95"),
                        ("Cardiac ultrasound (echocardiogram)", "45 min · €130"),
                        ("Digital radiography (2 projections)", "20 min · €75"),
                        ("Full on-site blood chemistry", "30 min · €85"),
                    ],
                    "cta_label": "Diagnostic protocols →",
                    "cta_href":  "visite",
                },
            ],
        },

        "chief_label":   "Clinical direction",
        "chief_heading": "One veterinarian <em>signs every chart.</em>",
        "chief": {
            "name":  "Dr. Marco Petro",
            "role":  "Clinical director · Internal medicine & soft-tissue surgery",
            "bio":
                "Degree in Veterinary Medicine at the Università di "
                "Padova in 2000, advanced training at the Royal "
                "Veterinary College London (2002-2004) in small "
                "animals, specialisation residency at Cornell "
                "University Vet School (NY, USA) in 2006. Member of "
                "SCIVAC (Italian Cultural Society of Companion-Animal "
                "Veterinarians) and ANMVI (Italian National "
                "Association of Veterinarians). OMV Padova Register "
                "no. 1428 since 2001. Clinical director of the "
                "practice since 2008.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "percorso": {
            "label":   "Patient pathway",
            "heading": "What to expect from the <em>first visit.</em>",
            "intro":
                "The first visit to the practice runs one hour and "
                "is dedicated to building the complete clinical "
                "chart: history, physical exam, basic abdominal "
                "ultrasound where indicated, written care plan. No "
                "non-urgent procedures at the first visit.",
            "steps": [
                {
                    "num": "01",
                    "icon": "clipboard",
                    "title": "Check-in & history",
                    "desc": "Front-desk welcome, complete history form "
                            "(breed, age, diet, environment, other "
                            "animals in the household), any prior "
                            "records from the previous veterinarian.",
                    "duration": "10 min",
                },
                {
                    "num": "02",
                    "icon": "book",
                    "title": "Complete physical exam",
                    "desc": "Weight and Body Condition Score, "
                            "cardiopulmonary auscultation, abdominal "
                            "palpation, oral cavity inspection, skin "
                            "and coat check, lymph-node palpation.",
                    "duration": "20 min",
                },
                {
                    "num": "03",
                    "icon": "heart",
                    "title": "Baseline diagnostics",
                    "desc": "Orienting abdominal ultrasound (where "
                            "indicated), any blood draws for on-site "
                            "blood chemistry processed in thirty "
                            "minutes. Radiography if trauma is "
                            "suspected.",
                    "duration": "15 min",
                },
                {
                    "num": "04",
                    "icon": "chart",
                    "title": "Written care plan",
                    "desc": "Discussion of the preventive or "
                            "therapeutic plan with the owner, "
                            "itemised written quote, also delivered "
                            "by email as a PDF.",
                    "duration": "10 min",
                },
                {
                    "num": "05",
                    "icon": "document",
                    "title": "Scheduling & follow-up",
                    "desc": "Calendar of recall visits, WhatsApp "
                            "reminders for vaccines and prophylaxis, "
                            "a direct line to the front desk for "
                            "non-urgent questions.",
                    "duration": "5 min",
                },
            ],
        },

        "press": ["Veterinaria Italiana", "SCIVAC Bulletin", "Il Mondo del Cane",
                  "QuattroZampe Mondadori", "Corriere Animali"],
        "press_label": "Featured in",

        "faq": {
            "label": "Frequently asked",
            "heading": "The questions <em>owners ask us most often.</em>",
            "items": [
                ("How often is a preventive check-up needed?",
                 "For healthy adult dogs and cats the schedule is "
                 "annual. From age seven onwards (geriatric "
                 "animals) we add a six-month screening visit with "
                 "blood chemistry. For rabbits and ferrets the "
                 "schedule is six-monthly from the first visit, "
                 "because life expectancy is shorter."),
                ("Do you perform laparoscopic spays?",
                 "Yes, for cats and dogs up to 35 kg. Laparoscopic "
                 "spaying uses three small 5 mm abdominal access "
                 "points instead of the traditional incision, day "
                 "hospitalisation, reduced post-operative pain, "
                 "and a return to normal within 48 hours. For "
                 "sizes above 35 kg we evaluate case by case."),
                ("Do you see rabbits, ferrets, birds and reptiles?",
                 "Rabbits, ferrets and guinea pigs yes, across all "
                 "pathways (preventive, vaccinations, surgery, "
                 "diagnostics). Birds and reptiles for basic "
                 "visits only — for complex conditions we refer "
                 "to exotic-animal specialists at university "
                 "clinics."),
                ("Do you have a night on-call service?",
                 "Yes, Dr. Petro is on call 24/7 for his own "
                 "patients at +39 333 410 7726. For emergencies "
                 "on animals not on our charts we direct owners "
                 "to the Università di Padova Veterinary Hospital "
                 "(Legnaro, open 24h) or to the Clinica San Marco "
                 "di Veggiano."),
                ("How does the annual prevention plan work?",
                 "It includes a preventive check-up, dog DA2PPi-L "
                 "or cat FRCP vaccines, monthly heartworm and tick "
                 "prophylaxis, annual blood-chemistry screening, "
                 "and one free six-month booster. Cost €245/year "
                 "for dogs, €195/year for cats. 15% discount on "
                 "scheduled surgical procedures within the "
                 "following twelve months."),
            ],
        },

        "cta_heading":
            "Every care plan is <em>written, stated, shared with the owner.</em>",
        "cta_primary_label":   "Book a preventive check-up",
        "cta_secondary_label": "Practice contact",

        "location": {
            "label":   "Practice address",
            "heading": "Via Belzoni 71, <em>Padova.</em>",
            "intro":
                "The practice occupies the ground floor of a "
                "nineteenth-century building in the Borgo Trento "
                "district, four hundred metres from the central "
                "station and a ten-minute walk from the "
                "Veterinary Medicine Faculty. Three separate "
                "exam rooms (dog/cat/exotic), a surgical theatre, "
                "a diagnostic room with ultrasound and digital "
                "X-ray, and a day-hospitalisation area.",
            "map_image": "",
            "map_fallback_image": _MAP_FALLBACK,
            "details": [
                ("Address",
                 "Via Belzoni 71\n35121 Padova"),
                ("Station",
                 "Padova Centrale\n6-minute walk"),
                ("Parking",
                 "Free Borgo Trento parking\n80 metres from the practice"),
                ("Accessibility",
                 "Ground-floor entrance with no steps\naccessible to wheelchairs and large carriers"),
            ],
            "hours_short": [
                ("Mon – Fri", "8:00 AM – 8:00 PM"),
                ("Saturday",  "9:00 AM – 1:00 PM"),
                ("Sunday",    "Emergencies on call only"),
            ],
            "cta_label": "Get directions",
            "cta_href":  "contatti",
        },
    },

    # ─── STUDIO (about) ────────────────────────────────────────
    "studio": {
        "eyebrow":   "The practice · Padova Borgo Trento",
        "headline":  "Three veterinarians, <em>one chart per animal.</em>",
        "intro":
            "Studio Veterinario Petro is an associate practice "
            "founded in 2008 by Marco Petro together with two "
            "colleagues trained at the Università di Padova. Three "
            "veterinarians, one shared clinical chart per patient, "
            "one signature at the bottom of every care plan. Night "
            "on-call line for patients already on our charts.",
        "history": [
            ("2008",
             "Marco Petro opens the practice on Via Belzoni with "
             "a single exam room and one assistant. Seventy-five "
             "animals on chart in the first year."),
            ("2012",
             "Dr. Anna Bressan joins as a second associate "
             "veterinarian · specialisation in exotic animals "
             "(rabbit, ferret, guinea pig, small reptiles)."),
            ("2015",
             "The surgical theatre opens with isoflurane "
             "inhalation anaesthesia and multiparameter "
             "monitoring. Laparoscopic surgery is introduced for "
             "spays and neuters."),
            ("2018",
             "Esaote MyLab Omega ultrasound and Carestream "
             "digital X-ray acquired. All diagnostic imaging is "
             "brought on site."),
            ("2023",
             "Dr. Tommaso Zen joins as third associate · "
             "specialisation in veterinary oncology and "
             "reconstructive surgery. The practice closes the "
             "year with 4,200 animals on chart."),
        ],
        "studio_image": _STUDIO_IMAGE,
        "studio_image_caption": "Exam room · Via Belzoni 71 · Padova",
        "method_title": "The Petro method",
        "method_paragraphs": [
            "Small-animal veterinary medicine doesn't resemble "
            "human medicine for one reason: the patient does not "
            "speak. The cat that starts drinking three times as "
            "much already has kidney insufficiency half the way "
            "in. The dog that limps on alternate days already "
            "has advanced arthritis. That's why at Petro "
            "preventive care is not an add-on: it is the first "
            "chapter, and for many patients it is also the only "
            "one truly needed.",
            "There is one clinical chart — shared across the "
            "three associates — because an animal is not the "
            "patient of a single veterinarian, it is the "
            "patient of the practice. When Anna spots a "
            "suspicious skin lesion during a vaccination, she "
            "flags it to Tommaso for surgical removal inside the "
            "same clinical document. No fragmented care, no "
            "reports getting lost between colleagues.",
            "Costs are stated for routine items (preventive "
            "check-up, vaccines, spay/neuter, ultrasound, "
            "baseline diagnostics). For structured plans — "
            "oncology therapy, post-trauma rehabilitation, "
            "complex orthopaedic surgery — the quote is built "
            "after a complete clinical assessment, but always "
            "delivered in writing and signed at the bottom.",
        ],
        "values_label":   "Practice values",
        "values_heading": "Four commitments, <em>written into the chart.</em>",
        "values": [
            ("Preventive care first",
             "The annual preventive check-up is the starting "
             "point of every relationship with a patient. Never "
             "a non-urgent procedure without a complete history."),
            ("One single chart",
             "Three veterinarians share the same clinical "
             "chart for each animal. No lost reports, no "
             "missed follow-ups between colleagues."),
            ("Stated costs",
             "Written rates for routine items. Signed PDF "
             "quote for every complex plan before treatments "
             "begin."),
            ("On call for our own patients",
             "24/7 night on-call line on Dr. Petro's direct "
             "number for animals already on chart. No patient "
             "left on their own."),
        ],
        "cta_heading":
            "The first step is always <em>a one-hour preventive check-up.</em>",
        "cta_primary_label":   "Meet the veterinarians",
        "cta_secondary_label": "Book the first visit",
        "press_label": "Featured in",
        "press": ["Veterinaria Italiana", "SCIVAC Bulletin", "Il Mondo del Cane",
                  "QuattroZampe Mondadori", "Corriere Animali"],
    },

    # ─── VISITE (services) ─────────────────────────────────────
    "visite": {
        "eyebrow":  "Visits & procedures",
        "headline": "Four families of care, <em>one shared chart per animal.</em>",
        "intro":
            "The full list of clinical pathways available on "
            "site. The stated costs are for routine items; for "
            "structured plans the quote is written after a "
            "complete clinical assessment.",
        "service_image": _SERVICE_IMAGE,
        "service_image_caption": "Cardiopulmonary auscultation · preventive check-up",
        # Treatments — 4-tuples (name, meta, desc, price) per
        # specialist services.html:121 unpacking contract.
        "treatments": [
            ("Annual preventive check-up · dog/cat",
             "40 min · by appointment",
             "Complete history, weight and Body Condition Score, "
             "cardiopulmonary auscultation, abdominal palpation, "
             "oral cavity check, skin and coat inspection, "
             "lymph-node palpation, vaccination and antiparasite "
             "calendar review.",
             "€65"),
            ("Geriatric screening (≥ 7 years)",
             "60 min · twice yearly",
             "Complete check-up + blood chemistry (CBC, renal and "
             "hepatic function, electrolytes, T4 in cats), blood "
             "pressure, orienting abdominal ultrasound. Indicated "
             "for dogs and cats from seven years onwards.",
             "€95"),
            ("Dog DA2PPi-L vaccine (annual)",
             "appointment · 30 min",
             "Combined distemper, adenovirus, parvovirus, "
             "parainfluenza, four-strain leptospirosis (L4) "
             "vaccine. WSAVA schedule, health record updated "
             "on site.",
             "€45"),
            ("Cat FRCP + FeLV vaccine",
             "appointment · 30 min",
             "Combined rhinotracheitis, calicivirus, "
             "panleukopenia + feline leukaemia (FeLV) vaccine. "
             "For indoor-only cats, FRCP triennial after the "
             "booster, €40.",
             "€55"),
            ("Cat spay (laparoscopic)",
             "procedure · day hospitalisation",
             "Minimally invasive ovariectomy with three 5 mm "
             "access points, isoflurane inhalation anaesthesia, "
             "multiparameter monitoring, resorbable subcuticular "
             "sutures. Same-day discharge.",
             "€320"),
            ("Dog spay < 20 kg (laparoscopic)",
             "procedure · day hospitalisation",
             "Laparoscopic ovariectomy with three abdominal "
             "access points, inhalation anaesthesia, multimodal "
             "post-operative analgesia, same-day discharge.",
             "€480"),
            ("Complete abdominal ultrasound",
             "30 min · by appointment",
             "Esaote MyLab Omega · assessment of liver, spleen, "
             "kidneys, bladder, gastrointestinal walls, "
             "mesenteric lymph nodes, prostate. Report delivered "
             "same day.",
             "€95"),
            ("Echocardiogram",
             "45 min · by appointment",
             "Ultrasound study of the cardiac chambers, valve "
             "assessment, measurement of ejection fraction and "
             "contractility. Indicated pre-anaesthesia in "
             "geriatric patients or predisposed breeds (Cavalier "
             "King Charles, Boxer, Maine Coon).",
             "€130"),
        ],
        "footnote_heading": "What we don't do on site",
        "footnote":
            "Interventional cardiology, neurosurgery, complex "
            "reconstructive orthopaedics, equine obstetrics. For "
            "these cases we refer to the Università di Padova "
            "Veterinary Hospital (Legnaro) with which we have a "
            "direct partnership and a fast-track lane for our "
            "patients.",
        "cta_heading":
            "Want to book a <em>preventive check-up or a follow-up?</em>",
        "cta_primary_label":   "Book a visit",
        "cta_secondary_label": "Meet the veterinarians",
    },

    # ─── MEDICI (team) ─────────────────────────────────────────
    "medici": {
        "eyebrow":  "The veterinarians",
        "headline": "Three associate veterinarians, <em>three complementary specialisations.</em>",
        "intro":
            "Three veterinarians have shared the practice since "
            "2008 (Marco), since 2012 (Anna) and since 2023 "
            "(Tommaso). Three complementary specialisations cover "
            "internal medicine, exotic animals and reconstructive "
            "surgery. One shared clinical chart per patient.",
        "doctors": [
            {
                "name":  "Dr. Marco Petro",
                "role":  "Clinical director",
                "specialty": "Internal medicine · soft-tissue surgery",
                "bio":
                    "Degree at the Università di Padova in 2000. "
                    "Royal Veterinary College London 2002-2004. "
                    "Cornell University Vet School (NY, USA) "
                    "residency 2006. OMV Padova Register no. 1428 "
                    "since 2001. Clinical director since 2008. "
                    "Member of SCIVAC and ANMVI. Preventive care "
                    "as the load-bearing register of his practice.",
                "portrait": _CHIEF_PORTRAIT,
                "year_label": "Since",
                "year": "2008",
            },
            {
                "name":  "Dr. Anna Bressan",
                "role":  "Associate veterinarian",
                "specialty": "Exotic animals · rabbit, ferret, guinea pig, reptiles",
                "bio":
                    "Degree at the Università di Padova in 2010. "
                    "Master's in Exotic-Animal Medicine in "
                    "Cremona (Università di Milano) 2011-2012. "
                    "Member of AAEMV (Italian Association of "
                    "Exotic-Animal Veterinarians). Leads the "
                    "exotic-pets section of the practice since "
                    "2012, with the same preventive-care register "
                    "applied to small exotic pets.",
                "portrait":
                    "https://images.pexels.com/photos/6235113/pexels-photo-6235113.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
                "year_label": "Since",
                "year": "2012",
            },
            {
                "name":  "Dr. Tommaso Zen",
                "role":  "Associate veterinarian",
                "specialty": "Veterinary oncology · reconstructive surgery",
                "bio":
                    "Degree at the Università di Bologna in 2014. "
                    "Specialisation in Veterinary Oncology at the "
                    "Universidad Complutense de Madrid 2017-2019. "
                    "Published in the Journal of Small Animal "
                    "Practice (2018) and Veterinary Surgery "
                    "(2020). Leads the oncologic surgery section "
                    "of the practice since 2023, with preventive "
                    "care woven into every post-surgical pathway.",
                "portrait":
                    "https://images.pexels.com/photos/6234600/pexels-photo-6234600.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
                "year_label": "Since",
                "year": "2023",
            },
        ],
        "portrait_city": "Padova · Borgo Trento",
    },

    # ─── PUBBLICAZIONI (blog_list) ─────────────────────────────
    "pubblicazioni": {
        "eyebrow":  "Clinical journal of the practice",
        "headline": "Working notes <em>from the exam room.</em>",
        "intro":
            "Brief notes from the three veterinarians on the "
            "clinical protocols in use, on the most representative "
            "cases of the year, on seasonal vaccines and "
            "prophylaxis. Intended for owners of patients already "
            "on chart and for colleagues.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Studio Veterinario Petro · The clinical journal",
        "empty_body_fallback_paragraphs": [
            "Article in editorial preparation. The full piece "
            "will be available shortly, written personally by "
            "one of the three associate veterinarians.",
            "This placeholder describes the voice of the "
            "Clinical Journal: short working notes, reflections "
            "on preventive-care protocols, accounts of "
            "representative clinical cases. Never more than two "
            "thousand words, never fewer than five hundred.",
        ],
    },

    "posts": [
        {
            "slug":     "calendario-vaccinale-2026",
            "kicker":   "Vaccinations in progress",
            "title":    "The practice vaccination calendar · 2026 update",
            "date":     "8 October 2026",
            "read_min": 4,
            "author":   "Dr. Marco Petro",
            "cover_image": _LEAD_IMAGE,
            "lede":
                "WSAVA released its new core-vaccine guidelines for "
                "dogs and cats in September. What changes from "
                "October 2026 in the booster calendar of our "
                "patients.",
            "body": [
                ("p", "The WSAVA 2026 guidelines confirm the annual "
                      "schedule for dog core vaccines (DA2PPi-L) and "
                      "consolidate the move to triennial after the "
                      "booster for cat core vaccines (FRCP) for cats "
                      "living strictly indoors. For cats with outdoor "
                      "access the schedule remains annual for FRCP "
                      "too."),
                ("h2", "What changes for prophylaxis"),
                ("p", "Four-strain leptospirosis (L4) remains a core "
                      "annual for dogs in the urban Padova "
                      "environment — incidence over recent seasons "
                      "has stayed stable but has not dropped. For "
                      "indoor cats we recalibrate FeLV to triennial "
                      "after the first-year booster, while for "
                      "free-roaming cats FeLV stays annual."),
                ("h2", "What we're doing from October"),
                ("p", "Owners of patients on chart will receive the "
                      "updated vaccination plan via WhatsApp. For "
                      "new patients the calendar is built at the "
                      "first preventive check-up based on breed, "
                      "age, living environment and contact with "
                      "other animals."),
            ],
        },
        {
            "slug":     "sterilizzazione-laparoscopia-perche",
            "kicker":   "Surgery",
            "title":    "Why we prefer laparoscopy for spays and neuters",
            "date":     "25 September 2026",
            "read_min": 5,
            "author":   "Dr. Tommaso Zen",
            "cover_image":
                "https://images.pexels.com/photos/7470769/pexels-photo-7470769.jpeg"
                "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
            "lede":
                "Since 2015 the practice has performed cat and dog "
                "spays under minimally invasive laparoscopy. Here is "
                "why it is our standard, and when we still do the "
                "traditional procedure.",
            "body": [
                ("p", "Laparoscopic spaying uses three 5 mm "
                      "abdominal access points instead of the "
                      "traditional 4-7 cm incision. The difference "
                      "is not cosmetic: it is first of all "
                      "physiological. Reduced post-operative pain, "
                      "return to normal within 48 hours, lower risk "
                      "of infectious complications, day "
                      "hospitalisation instead of an overnight "
                      "stay."),
                ("h2", "When we still perform open surgery"),
                ("p", "Three clinical situations. First: dogs above "
                      "35 kg, where laparoscopic access becomes "
                      "technically complex (the ovary is deeper, "
                      "the operating space limited). Second: "
                      "pyometra (uterine infection) — the uterus "
                      "must be removed intact and open access works "
                      "well. Third: ovarian tumours, for the same "
                      "reason."),
                ("h2", "The practice numbers"),
                ("p", "From 2015 to date we have performed around "
                      "1,400 laparoscopic spays. Major complication "
                      "rate under 1%. Minor complication rate "
                      "(seromas, local oedema) around 3%. Owner "
                      "satisfaction index (seven-day follow-up "
                      "questionnaire) above 95%."),
            ],
        },
    ],

    # ─── CONTATTI ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contact & address",
        "headline": "Three channels, <em>one front desk.</em>",
        "intro":
            "Routine appointments are booked via the online form "
            "or by phone during opening hours. For emergencies "
            "the on-call number is active 24/7 for patients "
            "already on chart.",
        # Blocks — 3-tuples (label, value, sub) per specialist
        # contact.html:105 unpacking contract.
        "blocks": [
            ("Front desk",
             "+39 049 6731 220",
             "Mon – Fri · 8:00 AM – 8:00 PM · Sat 9:00 AM – 1:00 PM"),
            ("Night on call",
             "+39 333 410 7726",
             "24/7 · only for patients already on chart"),
            ("Email",
             "studio@studiopetro.it",
             "Reply within 24 h during opening hours"),
            ("Address",
             "Via Belzoni 71 · 35121 Padova",
             "Borgo Trento · 6 minutes from the central station"),
        ],
        "form_title": "Write to us",
        "form_intro":
            "For routine appointments please use the Book a "
            "visit form. This form is for general enquiries, "
            "requests for a copy of the clinical chart, second "
            "opinions or questions about our protocols.",
        "form_placeholders": {
            "name":    "First and last name",
            "email":   "Email",
            "phone":   "Phone",
            "subject": "Subject",
            "message": "How can we help? Please include the animal's name and species.",
        },
        "form_helpers": {
            "name":    "Used to address our reply.",
            "email":   "We reply within 24 hours during opening hours.",
            "phone":   "Only for callback requests.",
            "subject": "Example: «second-opinion request» or «chart copy».",
        },
        "form_consent":
            "I agree to the processing of my data under GDPR. Privacy policy available on site.",
        "form_submit_note":
            "For clinical emergencies on patients already on "
            "chart, please call the 24/7 on-call line. This "
            "form is not monitored outside opening hours.",
        "hours_heading": "Opening hours",
        # hours — 3-tuples (day, am, pm) per specialist contact.html:175.
        "hours": [
            ("Mon – Fri", "8:00 AM – 1:00 PM", "2:30 PM – 8:00 PM"),
            ("Saturday",  "9:00 AM – 1:00 PM", "closed"),
            ("Sunday",    "closed",            "on-call only"),
        ],
        "transport_heading": "How to reach us",
        "transport": [
            ("Train",   "Padova Centrale station · 6-minute walk"),
            ("Car",     "Padova Est motorway exit · 12 minutes by car"),
            ("Tram",    "SIR1 line · Borgo Trento stop · 2-minute walk"),
            ("Parking", "Free Borgo Trento parking · 80 metres from the practice"),
        ],
    },

    # ─── RICHIEDI-VISITA (appointment) ─────────────────────────
    "richiedi-visita": {
        "eyebrow":  "Book a visit",
        "headline": "A preventive check-up, <em>forty minutes.</em>",
        "intro":
            "Book your animal's first preventive check-up "
            "online. The front desk confirms the appointment "
            "within 24 hours during opening hours. For "
            "emergencies please call the on-call line.",
        "process_label": "How it works",
        "process_heading": "Three steps, <em>one visit.</em>",
        # process — 3-tuples (num, title, blurb) per specialist
        # appointment.html:97 unpacking contract.
        "process": [
            ("01", "Fill in the form",
             "Tell us the animal's name, species, breed, age and "
             "the reason for the visit. Any prior records can be "
             "attached or brought to the practice."),
            ("02", "Confirmation within 24 hours",
             "The front desk gets in touch within 24 hours to "
             "confirm date and time. For urgent visits "
             "(sudden lameness, loss of appetite, recurrent "
             "vomiting) please call the front desk directly."),
            ("03", "First visit · 60 minutes",
             "History, complete physical exam, baseline "
             "diagnostics where indicated, written care plan. "
             "The quote is also delivered as a PDF."),
        ],
        "form_title": "Booking form",
        "form_band_side_note":
            "Preventive check-up — 40 minutes — €65 (dog/cat), "
            "€75 (exotic).",
        "form_band_side_note_small":
            "Costs are stated for routine items. For structured "
            "plans the quote is written after the first visit.",
        "form_fields": [
            {
                "name":    "owner_name",
                "label":   "Owner's name",
                "type":    "text",
                "required": True,
                "placeholder": "Owner's first and last name",
            },
            {
                "name":    "email",
                "label":   "Email",
                "type":    "email",
                "required": True,
                "placeholder": "For the appointment confirmation",
            },
            {
                "name":    "phone",
                "label":   "Phone",
                "type":    "tel",
                "required": True,
                "placeholder": "For quick contacts if needed",
            },
            {
                "name":    "pet_name",
                "label":   "Animal's name",
                "type":    "text",
                "required": True,
                "placeholder": "E.g. Luna · Briciola · Pepe",
            },
            {
                "name":    "pet_species",
                "label":   "Species and breed",
                "type":    "text",
                "required": True,
                "placeholder": "E.g. Cat · Dwarf rabbit · Border Collie dog",
            },
            {
                "name":    "pet_age",
                "label":   "Animal's age",
                "type":    "text",
                "required": True,
                "placeholder": "E.g. 8 years · 6 months",
            },
            {
                "name":    "visit_reason",
                "label":   "Reason for the visit",
                "type":    "textarea",
                "required": True,
                "placeholder":
                    "E.g. annual preventive check-up · "
                    "post-operative follow-up · feeding "
                    "questions. For emergencies call the "
                    "on-call line.",
            },
        ],
        "submit_label": "Send request",
        "consent":
            "I agree to the processing of my personal data and "
            "my animal's health data under GDPR. The clinical "
            "chart will be shared between the three associate "
            "veterinarians of the practice.",
        "footnote":
            "For clinical emergencies outside opening hours "
            "(sudden lameness, recurrent vomiting, prostration, "
            "trauma), please call the 24/7 on-call line: "
            "+39 333 410 7726. For patients not yet on chart we "
            "direct owners to the Ospedale Veterinario di "
            "Legnaro or to the Clinica San Marco di Veggiano.",
    },
}
