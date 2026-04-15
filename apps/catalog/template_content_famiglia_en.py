"""FAMIGLIA_CONTENT_EN — native pediatric warm-family translation.

Voice: BabyCentre UK / NCT / RCPCH register. Warm parent-facing, unhurried,
reassuring. No baby-talk, no cartoon tone. Reader is a British or
English-speaking parent looking at a private paediatric practice in Turin.
"""
from __future__ import annotations

from typing import Any


FAMIGLIA_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Home",         "kind": "home"},
        {"slug": "studio",   "label": "The practice", "kind": "about"},
        {"slug": "visite",   "label": "Appointments", "kind": "services"},
        {"slug": "crescita", "label": "Growing up",   "kind": "faq"},
        {"slug": "pediatre", "label": "Paediatricians", "kind": "team"},
        {"slug": "contatti", "label": "Contact",      "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "P",
        "logo_word":    "Pediatria Famiglia Plus",
        "tag":          "Paediatric practice · Turin, Crocetta district",
        "phone":        "011 549 21 88",
        "phone_tel":    "+390115492188",
        "whatsapp":     "+39 349 123 4567",
        "whatsapp_link": "https://wa.me/393491234567",
        "nav_cta_wa":   "WhatsApp",
        "email":        "studio@crocettapediatria.it",
        "address":      "Corso Galileo Ferraris 140 · 10129 Turin",
        "emergency_tel": "+393491234567",

        "hours_compact": "Mon – Fri · 8:30 – 12:30 · 15:00 – 19:00",
        "hours_footer_rows": [
            "Saturday · 9:00 – 12:00 · urgent only",
            "Sunday · on-call by phone",
        ],
        "license":
            "VAT 11234120014 · Turin Medical Board reg. 08/5412",
        "footer_intro":
            "A private paediatric practice in the Crocetta district of "
            "Turin. Four paediatricians, a neonatal specialist and a "
            "dedicated nurse. Thirty-minute appointments, on-call cover "
            "on Sundays and bank holidays, genuine listening for children "
            "and their parents.",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":       "Paediatric practice · Turin, Crocetta",
        "headline":      "Growing up <em>alongside</em> your little ones.",
        "subhead":
            "Four paediatricians, a child psychomotor therapist and a "
            "dedicated nurse. Calm appointments, long enough to listen "
            "properly — because every family deserves a point of "
            "reference, not a ticket number.",
        "primary_cta":   "Call the practice",
        "secondary_cta": "Message us on WhatsApp",

        "hero_image":
            "https://images.pexels.com/photos/7447009/pexels-photo-7447009.jpeg"
            "?auto=compress&cs=tinysrgb&w=1000&h=1250&fit=crop",
        "hero_image_alt":
            "Paediatrician carrying out a well-child check-up with a "
            "little girl in the bright Crocetta consulting room",
        "hero_ribbon":   "Italian NHS (SSN) affiliated",
        "hero_stamp_initial": "E",
        "hero_stamp_name":    "Dr Rambaldi",
        "hero_stamp_meta":    "in clinic today · 8:30 – 13:00",

        "trust_items": [
            {"icon": "clock",  "label": "Thirty-minute appointments, never ten"},
            {"icon": "shield", "label": "24-hour on-call cover for registered patients"},
            {"icon": "people", "label": "A family-sized practice since 1998"},
        ],

        # ── Intro trio · age groups ──
        "age_groups": [
            {
                "icon":  "baby",
                "range": "0 – 2 years",
                "title": "Newborn and first year",
                "blurb":
                    "The pathway that begins in the first week of life: "
                    "breastfeeding, sleep, well-child check-ups, discharge "
                    "from Sant'Anna or Mauriziano hospital. Dr Conti "
                    "follows your little one personally until their "
                    "second birthday.",
                "items": [
                    "Post-natal visit within seven days",
                    "Well-child check-ups at 1, 3, 6, 9 and 12 months",
                    "Breastfeeding and sleep support",
                ],
            },
            {
                "icon":  "child",
                "range": "3 – 10 years",
                "title": "Early and primary-school years",
                "blurb":
                    "The nursery and primary-school years: routine "
                    "immunisations, sports certificates, growth "
                    "monitoring, little setbacks and all the questions "
                    "a parent normally keeps to themselves.",
                "items": [
                    "Yearly well-child check-ups",
                    "Full childhood immunisation schedule",
                    "Non-competitive sports certificates",
                ],
            },
            {
                "icon":  "teen",
                "range": "11 – 18 years",
                "title": "Teenage years",
                "blurb":
                    "The most delicate phase, when young people want "
                    "to speak without parents in the room. Dedicated "
                    "appointments, private listening, a WhatsApp "
                    "channel for the questions they would rather not "
                    "ask out loud.",
                "items": [
                    "Annual appointment on their own",
                    "Endocrinology, growth, puberty",
                    "Private WhatsApp channel for the teenager",
                ],
            },
        ],

        # ── Le pediatre · portrait stack ──
        "team_label":   "The paediatricians",
        "team_heading": "Four signatures, <em>one family record.</em>",
        "team_intro":
            "The practice brings together four paediatricians who "
            "share records, protocols and the same standard of care. "
            "Every child, however, always has one named paediatrician "
            "of reference — the same person from the first check-up "
            "through to their teenage years.",

        "doctors": [
            {
                "name":  "Dr.ssa Elisa Rambaldi",
                "role":  "Family paediatrician",
                "spec":  "Children's nutrition",
                "wa_label": "Message on WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Marta Greco",
                "role":  "Paediatric allergist",
                "spec":  "Asthma and atopic dermatitis",
                "wa_label": "Message on WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Lucia Sferra",
                "role":  "Paediatric endocrinologist",
                "spec":  "Growth and puberty",
                "wa_label": "Message on WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Beatrice Conti",
                "role":  "Paediatric neonatologist",
                "spec":  "Sleep and breastfeeding",
                "wa_label": "Message on WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
        ],

        "team_note":
            "The clinical team is completed by Luisa Ferraro, a "
            "paediatric nurse with fifteen years of experience at the "
            "Regina Margherita Children's Hospital, and Giada Porro, a "
            "child psychomotor therapist specialising in developmental "
            "disorders in the 0–6 age range.",

        # ── Percorso della crescita · milestone timeline ──
        "journey_label":   "The journey through growing up",
        "journey_heading": "From the first weeks to <em>leaving school</em>.",
        "journey_intro":
            "A child meets the same paediatrician at least twelve "
            "times before the age of eighteen. Each meeting is a "
            "check-up, not an emergency visit. Here are the five "
            "milestones that shape the journey the most.",

        "journey_steps": [
            {
                "age":   "1 month",
                "title": "First check-up",
                "desc":  "The paediatrician meets the newborn at the "
                         "practice within forty days: weight, reflexes, "
                         "breastfeeding, sleep and first reassurance "
                         "for parents.",
            },
            {
                "age":   "6 months",
                "title": "Weaning",
                "desc":  "Practical advice on introducing first solid "
                         "foods, growth and weight monitoring and the "
                         "first stage of the childhood immunisation "
                         "schedule.",
            },
            {
                "age":   "1 year",
                "title": "First birthday",
                "desc":  "A full end-of-first-year check-up: motor "
                         "skills, language, first social interactions. "
                         "Family routines settle into place.",
            },
            {
                "age":   "3 years",
                "title": "Starting nursery",
                "desc":  "The move into nursery school: health "
                         "certificate, vision and hearing checks, "
                         "assessment of independence and sleep "
                         "rhythms.",
            },
            {
                "age":   "6 years",
                "title": "School age",
                "desc":  "A check-up before primary school: posture, "
                         "nutrition, first vision tests and guidance "
                         "on physical activity.",
            },
        ],

        # ── FAQ accordion genitori ──
        "faq_label":   "Questions from parents",
        "faq_heading": "The questions we <em>hear</em> most often.",
        "faq_intro":
            "We have gathered the eight questions parents ask us most "
            "often, on the phone or in the waiting room. If yours is "
            "not here, you can reach us on the practice number or on "
            "WhatsApp.",

        "faq": [
            (
                "When should I call the paediatrician?",
                "Straight away if your baby runs a fever above "
                "38.5 °C in the first three months of life, cries "
                "inconsolably, refuses all food or milk for more "
                "than 12 hours, has diarrhoea with blood or a "
                "widespread skin rash. For everything else — a "
                "moderate fever, a night-time cough, a mild "
                "sunburn — you can wait until morning and call "
                "calmly. The practice answers in person.",
            ),
            (
                "How do I book a first appointment?",
                "Simply call 011 549 21 88 from Monday to Friday: "
                "our receptionist, Silvia Pairetto, takes your "
                "child's name, age and the reason for the "
                "appointment. You can also message us on the "
                "dedicated WhatsApp number, even outside working "
                "hours. There is no online calendar — we prefer "
                "to speak to you first.",
            ),
            (
                "What should I bring to the first appointment?",
                "Your child's health record booklet, any discharge "
                "letter from the hospital, a record of "
                "immunisations already given and — for children "
                "over one year old — a weaning diary. You do not "
                "need recent test results: the paediatrician only "
                "asks for what she actually needs.",
            ),
            (
                "Is the practice pushchair-friendly?",
                "Yes. The entrance is on the raised ground floor "
                "of Corso Galileo Ferraris 140, with two steps and "
                "a side ramp. Inside, there is a dedicated "
                "pushchair corner in the waiting room and the "
                "toilet is fitted with a changing table. All "
                "consulting rooms are on the ground floor.",
            ),
            (
                "What happens in the evening or at weekends?",
                "Dr Rambaldi and Dr Greco share on-call cover by "
                "phone for registered patients: weekday evenings, "
                "overnight, Saturday afternoons and Sundays. The "
                "dedicated number is shared with you after the "
                "first appointment. For real emergencies, please "
                "still call 118 or go to Regina Margherita "
                "Children's Hospital.",
            ),
            (
                "Which vaccines are compulsory?",
                "Under the 2017 Lorenzin decree, ten routine "
                "immunisations are required for enrolment in "
                "compulsory schooling in Italy. The practice "
                "follows the Piedmont regional schedule and offers "
                "a private immunisation pathway, with no ASL "
                "queues and the option to space out doses where "
                "parents prefer.",
            ),
            (
                "How long does a check-up appointment last?",
                "A well-child check-up at the practice always "
                "lasts thirty minutes, even when the child is "
                "perfectly well. That is the minimum we need for "
                "a proper physical examination, weighing and "
                "measuring, updating the health record booklet "
                "and answering parents' questions without anyone "
                "feeling rushed.",
            ),
            (
                "How much does a private paediatric appointment cost?",
                "The first appointment is 90 euros, subsequent "
                "check-ups 70 euros, follow-up visits 60 euros. "
                "Families with two or more registered children "
                "receive a 15% discount. All payments are "
                "tax-deductible as medical expenses in Italy, "
                "with a receipt issued on the day.",
            ),
        ],

        # ── Studio child-friendly gallery ──
        "gallery_label":   "Inside the practice",
        "gallery_heading": "A home, <em>not a hospital ward.</em>",
        "gallery_intro":
            "We have designed every room so that children are not "
            "afraid to walk in. From the waiting area lined with "
            "books to the heated changing table, from low play "
            "tables to the colourful consulting rooms.",
        "gallery": [
            {
                "src": "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                       "?auto=compress&cs=tinysrgb&w=1000&h=800&fit=crop",
                "cap": "Consulting room · ground floor",
            },
            {
                "src": "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Playful stethoscope corner",
            },
            {
                "src": "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Breastfeeding room",
            },
            {
                "src": "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Newborn check-up room",
            },
            {
                "src": "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Entrance · Corso Galileo Ferraris",
            },
        ],

        # ── Orari band ──
        "hours_heading": "Opening hours",
        "hours": [
            ("Mon – Fri",  "8:30 – 12:30  ·  15:00 – 19:00"),
            ("Saturday",   "9:00 – 12:00  ·  urgent only"),
            ("Sunday",     "On-call by phone"),
            ("Bank holidays", "Dedicated line for registered patients"),
        ],
        "urgency_label": "Night-time cover",
        "urgency_title": "We are close by outside working hours too.",
        "urgency_text":
            "Registered patients have a dedicated out-of-hours "
            "phone number, open every day from 19:30 to 8:00 "
            "and on Sundays. For genuine emergencies, please "
            "still call 118 or go to Regina Margherita Children's "
            "Hospital.",
        "urgency_phone": "+39 349 123 4567",

        # ── Bottom CTA band ──
        "cta_heading":     "Do you <em>need us</em>?",
        "cta_lead":
            "Calling the practice is the simplest and most human way "
            "to begin. We answer in person, with no phone menus and "
            "no hold times. If you prefer, we are on WhatsApp too.",
        "cta_phone_label": "Practice phone",
        "cta_or":          "or",
        "cta_wa_label":    "Message us on WhatsApp",
    },

    # ─── LO STUDIO (about) ───────────────────────────────────────
    "studio": {
        "eyebrow":  "The practice",
        "headline": "Since 1998, <em>a home</em> for Crocetta families.",
        "intro":
            "We opened as a neighbourhood paediatric practice in 1998, "
            "on Dr Rambaldi's initiative. In twenty-seven years we "
            "have looked after more than three thousand children — "
            "many of whom are now parents themselves, bringing their "
            "own children back to us. It is the loveliest compliment "
            "we could ever receive.",

        "values": [
            {
                "icon":  "clock",
                "title": "Unhurried time",
                "desc":  "Thirty minutes for every appointment, never "
                         "less. Time is the one instrument that really "
                         "makes the difference between a correct and "
                         "a mistaken diagnosis.",
            },
            {
                "icon":  "ear",
                "title": "Genuine listening",
                "desc":  "We listen to parents first, then to "
                         "children, then to teenagers. Each one with "
                         "their own space and their own voice.",
            },
            {
                "icon":  "home",
                "title": "A home atmosphere",
                "desc":  "Colourful but not childish rooms, natural "
                         "light, reassuring scents. A practice should "
                         "feel like a home, not like a hospital ward.",
            },
            {
                "icon":  "people",
                "title": "Continuity of care",
                "desc":  "Every child has their own paediatrician of "
                         "reference, the same one from the first "
                         "check-up to their eighteenth birthday. We "
                         "share records — we do not share people.",
            },
        ],

        "studio_image":
            "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
            "?auto=compress&cs=tinysrgb&w=1600&h=700&fit=crop",
        "studio_image_caption":
            "Paediatric consulting rooms · Corso Galileo Ferraris 140, Turin",

        "history_label":   "Twenty-seven years of paediatrics",
        "history_heading": "Four milestones, <em>three generations</em> of children.",
        "history_intro":
            "The practice has changed address three times on the same "
            "street, expanded the team from one to five professionals "
            "and lived through three reforms of the Italian health "
            "service. One thing has never changed: the appointment "
            "lasts thirty minutes.",

        "history": [
            (
                "1998",
                "Dr Elisa Rambaldi opens the first paediatric "
                "practice in Via Morgari, with two consulting rooms "
                "and a receptionist. The first fifteen families are "
                "all still on our books today.",
            ),
            (
                "2008",
                "The practice moves to Corso Galileo Ferraris 140, "
                "ground floor with pushchair access. Dr Marta Greco "
                "joins as a paediatric allergist and Silvia Pairetto "
                "comes on board as clinical receptionist.",
            ),
            (
                "2016",
                "The team expands with Dr Lucia Sferra (paediatric "
                "endocrinology) and a child psychomotor therapy "
                "service opens for developmental disorders, led by "
                "Giada Porro.",
            ),
            (
                "2026",
                "The practice reaches five professionals with the "
                "arrival of Dr Beatrice Conti (neonatology) and "
                "launches a dedicated WhatsApp channel for teenagers.",
            ),
        ],

        "cta_heading":
            "Would you like to meet the paediatricians <em>before</em> booking?",
        "cta_lead":
            "You can read their profiles, see their faces and choose "
            "who you would like for your first appointment. If you "
            "are unsure, call us: we will help you find the right "
            "person for your child.",
        "cta_primary_label":   "Call the practice",
        "cta_secondary_label": "Meet the four paediatricians",
    },

    # ─── VISITE (services) ───────────────────────────────────────
    "visite": {
        "eyebrow":  "Appointments",
        "headline": "Eight types of appointment, <em>one way</em> of practising paediatrics.",
        "intro":
            "Every appointment at the practice has a clear time, a "
            "clear reason and a clear fee. Call us to book and we "
            "will decide together on the right appointment for your "
            "child's age and needs.",

        "visits": [
            {
                "icon":     "baby",
                "title":    "Newborn check-up",
                "duration": "45 min · 0 – 12 months",
                "desc":
                    "The first full assessment after birth: weight, "
                    "length, primitive reflexes, hip screening, "
                    "breastfeeding and sleep support. Repeated at 1, "
                    "3, 6, 9 and 12 months.",
                "bring_label": "What to bring",
                "bring":    "Health record booklet, hospital discharge "
                            "letter, any newborn screening results.",
                "cta_label": "Book by phone",
            },
            {
                "icon":     "child",
                "title":    "Childhood check-up",
                "duration": "30 min · 1 – 10 years",
                "desc":
                    "An annual review of growth, independence, "
                    "posture, nutrition and psychomotor development. "
                    "It is the appointment parents request most often.",
                "bring_label": "What to bring",
                "bring":    "Up-to-date health record booklet, a "
                            "week's food diary if possible.",
                "cta_label": "Book by phone",
            },
            {
                "icon":     "vaccine",
                "title":    "Immunisations",
                "duration": "20 min · all ages",
                "desc":
                    "The Piedmont regional immunisation schedule, "
                    "carried out at the practice without ASL queues. "
                    "We can space out doses and agree a tailored "
                    "pathway for parents with vaccine concerns.",
                "bring_label": "What to bring",
                "bring":    "Immunisation record booklet and the "
                            "accompanying parent's ID.",
                "cta_label": "Book by phone",
            },
            {
                "icon":     "sport",
                "title":    "Sports medical",
                "duration": "30 min · 6 – 18 years",
                "desc":
                    "A non-competitive medical certificate for school "
                    "and amateur sport. Includes a physical "
                    "examination, blood pressure reading and a resting "
                    "ECG where indicated.",
                "bring_label": "What to bring",
                "bring":    "The sports club's form and the health "
                            "record booklet.",
                "cta_label": "Book by phone",
            },
            {
                "icon":     "moon",
                "title":    "Sleep consultation",
                "duration": "45 min · 0 – 4 years",
                "desc":
                    "For exhausted parents and children who do not "
                    "sleep. A review of the family context, a plan "
                    "to normalise the sleep-wake rhythm and weekly "
                    "telephone follow-ups for one month.",
                "bring_label": "What to bring",
                "bring":    "A sleep diary for your child, filled "
                            "in over seven days.",
                "cta_label": "Book by phone",
            },
            {
                "icon":     "leaf",
                "title":    "Allergy appointment",
                "duration": "45 min · 2 – 18 years",
                "desc":
                    "A paediatric allergy assessment: detailed "
                    "clinical history, skin-prick testing, guidance "
                    "on asthma, atopic dermatitis and food allergies. "
                    "Led by Dr Greco.",
                "bring_label": "What to bring",
                "bring":    "Any recent blood tests and a symptom "
                            "diary.",
                "cta_label": "Book by phone",
            },
            {
                "icon":     "skin",
                "title":    "Paediatric dermatology",
                "duration": "30 min · all ages",
                "desc":
                    "For eczema, rashes, minor skin lesions and "
                    "growing moles. Led by Dr Greco, with photographic "
                    "follow-up to compare changes over time.",
                "bring_label": "What to bring",
                "bring":    "Any dated photographs of the skin "
                            "concern, a list of products you have used.",
                "cta_label": "Book by phone",
            },
            {
                "icon":     "apple",
                "title":    "Nutrition consultation",
                "duration": "45 min · 6 months – 18 years",
                "desc":
                    "For difficult weaning, selective eating, "
                    "overweight or underweight concerns, or simply "
                    "parental uncertainty. Led by Dr Rambaldi with a "
                    "written, tailored plan.",
                "bring_label": "What to bring",
                "bring":    "A seven-day food diary and the growth "
                            "charts from the health record booklet.",
                "cta_label": "Book by phone",
            },
        ],

        "tips_label":   "Three pieces of advice for parents",
        "tips_heading": "Things we would like you to <em>know</em> before you call us.",
        "tips_intro":
            "Some pieces of advice are worth more than a single "
            "appointment. We have put them here because we are "
            "convinced that an informed parent is a calmer parent "
            "— and a calmer child.",

        "tips": [
            {
                "title": "Fever is not the enemy",
                "text":
                    "Fever is a defence mechanism, not a number to "
                    "bring down straight away. Pay more attention to "
                    "how your child behaves — whether they eat, "
                    "drink, play — than to the figure on the "
                    "thermometer.",
            },
            {
                "title": "Five minutes are enough",
                "text":
                    "Every evening, before bed, ask your child how "
                    "their day went. Not at dinner, not while you "
                    "are cooking. In their bedroom, just the two "
                    "of you. Five minutes will change everything.",
            },
            {
                "title": "Call us without hesitation",
                "text":
                    "There are no silly questions in paediatrics. "
                    "The practice answers the phone Monday to "
                    "Friday: calling before you worry is always "
                    "the right thing to do.",
            },
        ],

        "cta_heading":
            "The simplest way to book an appointment is still to <em>call us</em>.",
        "cta_primary_label":   "Call the practice",
        "cta_secondary_label": "Message on WhatsApp",
    },

    # ─── CRESCITA (faq) ──────────────────────────────────────────
    "crescita": {
        "eyebrow":  "Growing up & reassurance",
        "headline": "The questions that <em>run through</em> the first eighteen years.",
        "intro":
            "We have gathered here the questions parents ask us most "
            "often, grouped by theme. Treat it as a first read: for "
            "everything else, please speak to your paediatrician of "
            "reference.",

        "topics": [
            {
                "icon":  "apple",
                "meta":  "Area 01",
                "title": "Nutrition and feeding",
                "intro":
                    "From the first milk let-down to adolescence, "
                    "feeding is the ground where parents and "
                    "paediatricians talk most. Four questions we "
                    "hear every week.",
                "items": [
                    (
                        "At what age should I start weaning?",
                        "Current guidelines point to the end of the "
                        "sixth month as the right moment to begin, "
                        "when the baby sits unaided, has lost the "
                        "tongue-thrust reflex and shows interest in "
                        "adult food. There is no magic day: you "
                        "start when the baby is ready, not when "
                        "the calendar says so.",
                    ),
                    (
                        "Is my child too thin?",
                        "Weight on its own says nothing. Three "
                        "figures must always be read together: "
                        "weight, height and BMI, plotted against "
                        "your child's own growth curve. A child "
                        "who grows steadily along their own "
                        "percentile — even the tenth — is doing "
                        "perfectly well.",
                    ),
                    (
                        "How do I cope with a fussy eater?",
                        "Selective eating between the ages of 2 "
                        "and 5 is normal and expected. No battles "
                        "at the table, no bribes, no special "
                        "plates: you offer, offer again, and wait. "
                        "If after six years of age selectivity "
                        "still covers whole food groups, call the "
                        "practice.",
                    ),
                    (
                        "Do supplements really work?",
                        "In the vast majority of cases, no. A "
                        "child who eats a varied diet does not "
                        "need supplements, apart from vitamin D "
                        "in the first years of life and vitamin "
                        "K in newborns. Everything else is "
                        "marketing, not paediatrics.",
                    ),
                ],
            },
            {
                "icon":  "moon",
                "meta":  "Area 02",
                "title": "Sleep and rest",
                "intro":
                    "Sleep is the subject that exhausts parents "
                    "most in the first three years. Four "
                    "reassurances based on clinical practice, not "
                    "textbooks.",
                "items": [
                    (
                        "How many hours should a child sleep?",
                        "0 to 3 months: 14–17 hours a day, spread "
                        "across naps and night. 4 to 11 months: "
                        "12–15 hours. 1 to 2 years: 11–14 hours. "
                        "3 to 5 years: 10–13 hours. Each child "
                        "has their own rhythm: two-hour "
                        "variations either way are normal.",
                    ),
                    (
                        "Is it normal for them to wake every two hours?",
                        "In the first six months, yes, it is "
                        "physiological: a baby's stomach is small "
                        "and the circadian cycle is not yet "
                        "mature. After six months, if frequent "
                        "waking continues, we can build a plan "
                        "together to normalise sleep.",
                    ),
                    (
                        "Can I have my baby sleep next to me?",
                        "Co-sleeping in the same room (but not "
                        "in the same bed) is recommended up to "
                        "12 months. After that, it depends on "
                        "the family's habits: no approach is "
                        "wrong if it works for both parents and "
                        "child.",
                    ),
                    (
                        "When can I stop using night-time nappies?",
                        "Night-time bladder control typically "
                        "arrives between the ages of 3 and 5. "
                        "It is not a race: some children are "
                        "ready at two and a half, others at six. "
                        "If bedwetting is still frequent at seven, "
                        "let us talk about it.",
                    ),
                ],
            },
            {
                "icon":  "vaccine",
                "meta":  "Area 03",
                "title": "Immunisations and common childhood illnesses",
                "intro":
                    "The immunisation landscape in Italy changed "
                    "in 2017 with the Lorenzin decree. Here we "
                    "answer the four most common questions — "
                    "patiently, and with the data.",
                "items": [
                    (
                        "Which immunisations are compulsory?",
                        "Ten: diphtheria, tetanus, pertussis, "
                        "hepatitis B, poliomyelitis, Hib, measles, "
                        "rubella, mumps and varicella. The "
                        "requirement applies to enrolment in "
                        "compulsory schooling (ages 0–16) and is "
                        "set by the 2017 Lorenzin decree.",
                    ),
                    (
                        "Can I space out the doses?",
                        "Yes. The practice offers personalised "
                        "pathways for families who prefer to "
                        "spread immunisations across several "
                        "appointments rather than give three "
                        "vaccines in a single session. We discuss "
                        "it together at the first check-up.",
                    ),
                    (
                        "How do I deal with roseola (sixth disease)?",
                        "Roseola infantum affects children "
                        "between 6 months and 2 years: three "
                        "days of sudden high fever followed by "
                        "a pink rash. Manage it with fever "
                        "reducers and patience. Call us only if "
                        "the fever rises above 40 °C or lasts "
                        "more than four days.",
                    ),
                    (
                        "Should I worry about a persistent cough?",
                        "A cough for up to three weeks after a "
                        "cold is normal: children's airways are "
                        "more reactive. Call us if the cough is "
                        "accompanied by a fever that does not "
                        "settle within five days, wheezing or "
                        "visible chest indrawing between the "
                        "ribs.",
                    ),
                ],
            },
            {
                "icon":  "comp",
                "meta":  "Area 04",
                "title": "Behaviour and development",
                "intro":
                    "The less medical questions are often the "
                    "most important ones. Here we answer on "
                    "child development, tantrums and the "
                    "teenage years.",
                "items": [
                    (
                        "At what age does a child start talking?",
                        "First words arrive between 10 and 18 "
                        "months, first sentences between 18 and "
                        "24 months. If by 24 months a child is "
                        "not putting two words together, a "
                        "psychomotor assessment is reasonable — "
                        "and we run one in-house with Giada "
                        "Porro.",
                    ),
                    (
                        "Are tantrums normal?",
                        "Yes — they are both normal and "
                        "essential: they are the way a child "
                        "experiments with independence and "
                        "limits. You do not punish them, you "
                        "contain them. They become a concern "
                        "when they regularly involve physical "
                        "aggression or self-harm.",
                    ),
                    (
                        "How much screen time is safe?",
                        "WHO guidance is: no screen time before "
                        "the age of 2, a maximum of one hour a "
                        "day between 2 and 5, and a maximum of "
                        "two hours after the age of 5. "
                        "Television, tablets and smartphones "
                        "all count: yes, the morning cartoon "
                        "counts too.",
                    ),
                    (
                        "How do I talk to my teenager?",
                        "Less than you would like to, and with "
                        "more listening than you think. Open "
                        "questions always work better than "
                        "closed ones: 'How was your day?' beats "
                        "'Have you done your homework?' ten-nil. "
                        "And remember: silence is not refusal, "
                        "it is thinking.",
                    ),
                ],
            },
        ],

        "materials_label":   "Useful materials",
        "materials_heading": "Three <em>downloadable</em> guides.",
        "materials_intro":
            "We have put together three PDF guides for parents "
            "to download and keep at home. They are written by "
            "the paediatricians of the practice and updated "
            "for 2026.",

        "materials": [
            {
                "title":    "Newborn handbook",
                "desc":
                    "Twenty-eight pages on the first three "
                    "months of life: breastfeeding, sleep, "
                    "bathing, early immunisations and when to "
                    "call the practice.",
                "size":     "PDF · 2.4 MB",
                "dl_label": "Download",
            },
            {
                "title":    "2026 immunisation schedule",
                "desc":
                    "The up-to-date Piedmont regional "
                    "immunisation schedule in a summary version, "
                    "with recommended and optional dates.",
                "size":     "PDF · 1.1 MB",
                "dl_label": "Download",
            },
            {
                "title":    "Guide to weaning",
                "desc":
                    "From the sixth month to the first birthday: "
                    "which foods to introduce, in what order, "
                    "with what care. Includes recipes by Dr "
                    "Rambaldi.",
                "size":     "PDF · 3.1 MB",
                "dl_label": "Download",
            },
        ],

        "cta_heading":
            "Did you not find <em>your</em> question?",
        "cta_lead":
            "Call us or message us on WhatsApp: we answer in "
            "person on the same working day. There are no "
            "silly questions in paediatrics.",
        "cta_primary_label":   "Call the practice",
        "cta_secondary_label": "Message on WhatsApp",
    },

    # ─── PEDIATRE (team) ─────────────────────────────────────────
    "pediatre": {
        "eyebrow":  "The paediatricians",
        "headline": "Four signatures, <em>one family record.</em>",
        "intro":
            "We are four paediatricians with different training "
            "backgrounds and one way of working: thirty minutes for "
            "every appointment, records shared between colleagues, "
            "continuity of relationship with every child from birth "
            "to eighteen years old.",

        "doctors": [
            {
                "name":  "Dr.ssa Elisa Rambaldi",
                "role":  "Founder · Family paediatrician",
                "tag":   "Founder",
                "specs": ["Children's nutrition", "Weaning", "School age"],
                "bio":
                    "Medical degree at the University of Turin, "
                    "paediatric specialism at Regina Margherita "
                    "Children's Hospital. Opened the practice in 1998 "
                    "to bring back to community paediatrics its "
                    "unhurried dimension. Author of «Crescere "
                    "insieme» (Growing up together), Einaudi Ragazzi, "
                    "2019.",
                "exp_label": "Experience",
                "exp_value": "28 years · over 3,000 active records",
                "wa_label":  "Message on WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Marta Greco",
                "role":  "Paediatrician · Allergy and dermatology",
                "tag":   "Allergy",
                "specs": ["Childhood asthma", "Atopic dermatitis", "Food allergies"],
                "bio":
                    "Degree and paediatric specialism at the "
                    "University of Pavia, master's in Paediatric "
                    "Allergy at San Raffaele in Milan. With the "
                    "Crocetta practice since 2008, leading the "
                    "paediatric allergy and dermatology pathway. "
                    "Link referrer for Gaslini Children's Hospital "
                    "(Genoa) on community consultations.",
                "exp_label": "Experience",
                "exp_value": "22 years · paediatric allergy since 2006",
                "wa_label":  "Message on WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Lucia Sferra",
                "role":  "Paediatrician · Endocrinology",
                "tag":   "Endocrinology",
                "specs": ["Growth", "Early puberty", "Paediatric thyroid"],
                "bio":
                    "Medical degree at Federico II University in "
                    "Naples, paediatric specialism at the University "
                    "of Bologna, fellowship in Paediatric "
                    "Endocrinology at Boston Children's Hospital. "
                    "With the practice since 2016, looking after "
                    "growth, puberty and endocrine conditions in "
                    "the 8–18 age range.",
                "exp_label": "Experience",
                "exp_value": "18 years · paediatric endocrinology",
                "wa_label":  "Message on WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Beatrice Conti",
                "role":  "Paediatrician · Neonatology",
                "tag":   "Neonatology",
                "specs": ["Breastfeeding", "Sleep 0–3 years", "Prematurity"],
                "bio":
                    "Degree and specialism at the University of "
                    "Turin, fifteen years on the Neonatology ward "
                    "at Sant'Anna Hospital, where she cared for more "
                    "than two thousand premature and full-term "
                    "newborns. IBCLC-certified breastfeeding "
                    "consultant. Joins the practice in 2026 to lead "
                    "the first-year-of-life programme and support "
                    "new mothers.",
                "exp_label": "Experience",
                "exp_value": "15 years · Sant'Anna · IBCLC since 2014",
                "wa_label":  "Message on WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
        ],

        "extra_title": "The clinical team is completed by two further professionals.",
        "extra_text":
            "Luisa Ferraro, a paediatric nurse with fifteen years on "
            "the ward at Regina Margherita Children's Hospital, "
            "looks after immunisations and blood tests at the "
            "practice. Giada Porro, a child psychomotor therapist "
            "specialising in developmental disorders in the 0–6 age "
            "range, sees patients on Tuesdays and Thursdays by "
            "appointment.",
    },

    # ─── CONTATTI (contact) ──────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contact & access",
        "headline": "One <em>number</em>, one person, one answer.",
        "intro":
            "Silvia Pairetto answers the phone in person from Monday "
            "to Friday. She knows every record, every name and every "
            "mother in this practice. For non-urgent enquiries you "
            "can also reach us on WhatsApp or through the form below.",

        "address_label": "Where we are",
        "address_line":  "Corso Galileo Ferraris 140",
        "address_sub":   "10129 Turin · Crocetta district · raised ground floor",
        "phone_label":   "Phone",
        "email_label":   "Email",

        "map_image":
            "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
            "?auto=compress&cs=tinysrgb&w=1000&h=750&fit=crop",

        "travel_heading": "How to reach us",
        "travel": [
            {
                "icon":  "metro",
                "title": "Underground",
                "text":  "Line 1 · Re Umberto station, a 4-minute walk to Corso Galileo Ferraris.",
            },
            {
                "icon":  "car",
                "title": "Car and parking",
                "text":  "Q-Park Crocetta partner car park at Via Governolo 22, 80 metres from the practice.",
            },
            {
                "icon":  "walk",
                "title": "On foot",
                "text":  "Five minutes from Parco del Valentino and 15 minutes from Porta Nuova railway station.",
            },
        ],

        "hours_heading": "Opening hours",
        "hours": [
            ("Mon – Fri",  "8:30 – 12:30 · 15:00 – 19:00"),
            ("Saturday",   "9:00 – 12:00 · urgent only"),
            ("Sunday",     "On-call by phone"),
            ("Bank holidays", "Dedicated line"),
        ],

        "form_title": "Write to the practice",
        "form_intro":
            "For non-urgent enquiries — fees, hours, paperwork, "
            "first appointment — write to us here. We reply within "
            "the working day. For anything urgent, please call.",

        "label_parent_name": "Parent's name",
        "label_child_age":   "Child's age",
        "label_reason":      "Reason for contact",

        "reason_options": [
            "First appointment",
            "Routine check-up",
            "Immunisations",
            "Advice on a specific concern",
            "Administrative information",
            "Other",
        ],

        "form_placeholders": {
            "parent_name": "Giulia Bianchi",
            "email":       "giulia.bianchi@email.it",
            "phone":       "+39 333 …",
            "child_age":   "4 years and a half",
            "message":
                "Write your question here. "
                "We reply on the same working day.",
        },
        "form_helpers": {
            "parent_name": "Please give the name of the parent writing.",
            "email":       "We will reply here within the working day.",
            "phone":       "Optional — helpful if you would rather be called back.",
            "child_age":   "Age and, if you wish, your child's name.",
            "reason":      "If you are not sure, choose «Other».",
            "message":
                "A few lines are plenty — everything else is "
                "better talked through on the phone.",
        },
        "form_consent":
            "I consent to the processing of my personal data in "
            "line with the practice's privacy notice under EU "
            "Regulation 679/2016 (GDPR). Children's data are "
            "held by the practice and are never shared with "
            "third parties.",
        "form_submit_note":
            "We reply within the working day · for anything "
            "urgent, please call the practice directly.",
    },
}
__all__ = ["FAMIGLIA_CONTENT_EN"]
