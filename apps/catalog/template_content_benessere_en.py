"""BENESSERE_CONTENT_EN — native wellness-premium translation.

Editorial voice: Goop / Tatler Spa Guide / Condé Nast Traveler Spa register.
Sensorial, literary, intentional. Proper names (Studio Armonia, Bergamo Alta,
Via Arena 15, Sara Conti, Davide Lai, Yara Bonomi, Elena Rossi, Miguel
Ferrari, Chiara Bonomi) preserved verbatim.
"""
from __future__ import annotations

from typing import Any

from apps.catalog.template_content_benessere import (
    _AMBIENT_CANDLES,
    _AMBIENT_MASSAGE,
    _AMBIENT_RITUAL,
    _AMBIENT_TEA,
    _AMBIENT_YOGA,
    _HERO_IMG,
    _MAP_IMG,
    _PORTRAIT_DAVIDE,
    _PORTRAIT_ELENA,
    _PORTRAIT_MIGUEL,
    _PORTRAIT_SARA,
    _PORTRAIT_YARA,
    _ROOM_GARDEN,
    _ROOM_HAMMAM,
    _ROOM_MEDITATION,
    _ROOM_RECEPTION,
    _ROOM_TISANERIA,
    _ROOM_WATER,
)


BENESSERE_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",           "label": "Home",             "kind": "home"},
        {"slug": "filosofia",      "label": "Philosophy",       "kind": "about"},
        {"slug": "rituali",        "label": "Rituals",          "kind": "services"},
        {"slug": "ambienti",       "label": "Rooms",            "kind": "gallery"},
        {"slug": "professionisti", "label": "Practitioners",    "kind": "team"},
        {"slug": "contatti",       "label": "Contact",          "kind": "contact"},
        {"slug": "prenota",        "label": "Reserve",          "kind": "appointment"},
    ],

    "site": {
        "logo_initial":  "A",
        "logo_word":     "Studio Armonia",
        "tag":           "Holistic house · Bergamo Alta · 800 m above sea level",
        "nav_cta":       "Book a ritual",
        "phone":         "+39 035 412 998",
        "email":         "ritual@studioarmonia.it",
        "address":       "Via Arena 15 · 24129 Bergamo Alta",
        "hours_compact": "Mon – Sat · by appointment",
        "hours_footer_rows": [
            "Mon – Fri · 9:00 – 20:00",
            "Saturday · 9:00 – 18:00",
            "Sunday · day of stillness",
        ],
        "license":       "Practitioners certified by FIF and SIAF (Italian professional bodies)",
        "footer_intro":
            "Studio Armonia is an independent holistic house opened in 2011 "
            "within the stone walls of Bergamo Alta. Bespoke rituals, "
            "certified practitioners, unhurried time — for those seeking a "
            "breath, not a service.",
        "socials": [
            ("Instagram", "#"),
            ("Journal",   "#"),
            ("Telegram",  "#"),
        ],
    },

    # ───────────────────────── HOME ─────────────────────────
    "home": {
        "hero_image":  _HERO_IMG,
        "eyebrow":     "Holistic house · Bergamo Alta",
        "headline":    'A breath is the measure of <em>our time</em>',
        "subhead":
            "Bespoke rituals drawn from Mediterranean and Eastern traditions, "
            "held within a stone refuge above the everyday — eight hundred "
            "metres above sea level.",
        "primary_cta":   "Reserve your ritual",
        "secondary_cta": "Read the treatments",
        "hero_meta": [
            "Bergamo Alta",
            "Since 2011",
            "Five certified practitioners",
            "Stillness on Sundays",
        ],

        "manifesto_label": "Manifesto · Studio Armonia",
        "manifesto":
            "At Armonia one does not come to add — one comes to set aside. "
            "To set aside the hurry, the inner voice that scolds, the weary "
            "posture of those carrying three thoughts at once. Our rituals "
            "are made of slow time, warm oils, spring waters and chosen "
            "silences. We are not a hotel spa: we are a laboratory of "
            "presence, open for fifteen years within the upper walls of "
            "Bergamo.",
        "manifesto_signature": "— Chiara Bonomi, founder",

        "rituali_label": "Rituals in focus",
        "rituali_heading": 'Four <em>measures of time</em> to choose from',
        "rituali_intro":
            "The complete list of ten rituals sits on its dedicated page. "
            "Below, the four most often requested by first-time guests.",
        "rituali": [
            ("Mediterranean Massage",
             "55 minutes · olive oil and Sorrento citrus",
             "€ 85"),
            ("Hammam Ritual",
             "90 minutes · steam, coarse salt, red clay",
             "€ 120"),
            ("Energetic Rebalance",
             "60 minutes · pranotherapy and guided breath",
             "€ 95"),
            ("Ayurveda Abhyanga",
             "90 minutes · warm oils, two practitioners",
             "€ 135"),
        ],

        "benefits_label": "What we take away",
        "benefits_heading": 'Three <em>words</em>, not three promises',
        "benefits_intro":
            "We do not promise radical transformation in ninety minutes. "
            "We promise a measured, repeatable slowing-down.",
        "benefits": [
            ("Equilibrium",
             "A nervous system that softens, a posture that finds itself "
             "again, a breath rhythm that stops chasing deadlines."),
            ("Breath",
             "The breath practice is the thread of every ritual. You leave "
             "knowing where your diaphragm sits — and where it had quietly "
             "paused."),
            ("Grounding",
             "Contact with your own weight, with the old stone underfoot, "
             "with this place. One does not meditate in a void: one "
             "meditates at home."),
        ],

        "ambients_label": "Rooms · Studio Armonia",
        "ambients_heading": 'A <em>seventeenth-century</em> building, restored with restraint',
        "ambients_intro":
            "Palazzo Bonomi Suardi, Via Arena 15. Four treatment rooms, a "
            "cloister planted with officinal herbs, a tisane bar open to "
            "every guest.",
        "ambients": [
            (_AMBIENT_MASSAGE, "The Massage Room",      "raking light through full-height glass"),
            (_AMBIENT_TEA,     "Herb Tisane Bar",       "gathered in the cloister · served on porcelain"),
            (_AMBIENT_CANDLES, "The Ritual Room",       "beeswax candles · warm linen towels"),
            (_AMBIENT_YOGA,    "The Breath Studio",     "original parquet · raw-wool rugs"),
        ],

        "therapists_label": "Practitioners",
        "therapists_heading": 'Five <em>hands</em> that know every guest by name',
        "therapists_intro":
            "Every ritual is held personally by a certified practitioner. "
            "The full roster, with extended biographies, is on the "
            "Practitioners page.",
        "therapists_trio": [
            {
                "name": "Sara Conti",
                "role": "Naturopath · Co-founder",
                "bio":
                    "Twelve years in practice, trained at Istituto Riza in "
                    "Milan. She oversees phytotherapy, alpine hydrotherapy "
                    "and the seasonal cleansing programme.",
                "portrait": _PORTRAIT_SARA,
            },
            {
                "name": "Davide Lai",
                "role": "Osteopath D.O.",
                "bio":
                    "Graduated from the Scuola Superiore di Osteopatia "
                    "Italiana, specialised in craniosacral and visceral "
                    "techniques. He receives on Tuesdays and Thursdays.",
                "portrait": _PORTRAIT_DAVIDE,
            },
            {
                "name": "Yara Bonomi",
                "role": "Ayurvedic practitioner",
                "bio":
                    "Trained in Varkala (India) and certified by the Italian "
                    "Ayurvedic Society (S.I.A.). She holds the Abhyanga and "
                    "Hawaiian Lomi-Lomi rituals, always four-handed with a "
                    "second practitioner.",
                "portrait": _PORTRAIT_YARA,
            },
        ],

        "journey_label": "How a visit unfolds",
        "journey_heading": 'The <em>visit</em>, step by step',
        "journey_intro":
            "Every ritual follows the same liturgy: quiet welcome, "
            "treatment, tisane pause, breath. There are no speakers, no "
            "forced music — time measures itself.",
        "journey": [
            {
                "num": "01",
                "title": "Welcome",
                "body":
                    "At the threshold you set aside shoes, phone and hurry. "
                    "You are offered a warm seasonal tisane, a sheet of "
                    "recycled paper for requests and attentions, ten minutes "
                    "of silence before entering the room.",
            },
            {
                "num": "02",
                "title": "Ritual of the body",
                "body":
                    "The treatment you have chosen — massage, hammam, "
                    "shiatsu — is held by your practitioner with oils "
                    "prepared in-house and natural linen cloths. There is "
                    "no waiting inside the room.",
            },
            {
                "num": "03",
                "title": "Tisane pause",
                "body":
                    "After the ritual, fifteen minutes at the tisane bar "
                    "with a blend tuned to the season and to your "
                    "constitution: nettle in spring, lemon balm in summer, "
                    "ginger in winter.",
            },
            {
                "num": "04",
                "title": "Closing breath",
                "body":
                    "Three minutes of guided breathing before phone and "
                    "shoes are returned. It is the shortest part of the "
                    "liturgy — and the one you carry home.",
            },
        ],

        "calendar_label": "Next availability",
        "calendar_heading": 'Choose your <em>moment</em>',
        "calendar_intro":
            "A selection of this week's open slots. For the full diary and "
            "special requests, please use the form on the Reserve page.",
        "calendar": [
            {"day": "Mon", "num": "14", "month": "Apr",
             "slots": ["10:00", "14:30", "17:00"], "has_slots": True, "soldout": False},
            {"day": "Tue", "num": "15", "month": "Apr",
             "slots": ["09:30", "15:00"],         "has_slots": True, "soldout": False},
            {"day": "Wed", "num": "16", "month": "Apr",
             "slots": ["11:00", "16:30"],         "has_slots": True, "soldout": False},
            {"day": "Thu", "num": "17", "month": "Apr",
             "slots": ["fully booked"],           "has_slots": False, "soldout": True},
            {"day": "Fri", "num": "18", "month": "Apr",
             "slots": ["10:30", "14:00", "18:00"], "has_slots": True, "soldout": False},
            {"day": "Sat", "num": "19", "month": "Apr",
             "slots": ["fully booked"],           "has_slots": False, "soldout": True},
            {"day": "Sun", "num": "20", "month": "Apr",
             "slots": ["stillness"],              "has_slots": False, "soldout": True},
        ],
        "calendar_cta": "Open the reservation form",

        "press_label": "Featured in",
        "press": [
            "Vogue Italia Living",
            "Marie Claire",
            "Io Donna",
            "Natural Style",
            "Corriere della Sera · Salute",
        ],
    },

    # ──────────────────── FILOSOFIA (about) ────────────────────
    "filosofia": {
        "eyebrow":  "Our philosophy",
        "headline": "Three words, <em>no promises</em>",
        "intro":
            "Studio Armonia was founded in 2011 around a simple idea: a "
            "holistic house that does not sell transformation, but returns "
            "time. Three pillars — Breath, Ritual, Nature — shape every "
            "choice, from the treatment roster to the herbs in the tisane "
            "bar.",

        "pillars": [
            {
                "init":  "B",
                "title": "Breath",
                "body":
                    "Breath is the thread of every ritual. Each treatment "
                    "opens and closes with three minutes of breath practice "
                    "— we call it the rhythm of return.",
            },
            {
                "init":  "R",
                "title": "Ritual",
                "body":
                    "Not sessions, not packages: rituals. Each with a "
                    "precise, repeatable liturgy that does not depend on "
                    "the practitioner's mood or the week's diary.",
            },
            {
                "init":  "N",
                "title": "Nature",
                "body":
                    "Our materials come from the land: Apulian olive oil, "
                    "Adriatic salt, clays from the Emilian hills, herbs "
                    "harvested in the cloister from March to October.",
            },
        ],

        "photo_image": _AMBIENT_RITUAL,
        "photo_caption":
            "The Ritual Room · Palazzo Bonomi Suardi, Bergamo Alta",
        "photo_sub": "Conservative restoration · 2011",

        "timeline_label": "Our story",
        "timeline_heading": "Fifteen years of <em>quiet work</em>",
        "timeline": [
            {
                "year":  "2011",
                "title": "The first room in Via Arena",
                "body":
                    "Chiara Bonomi and Sara Conti open the first space on "
                    "the ground floor of Palazzo Bonomi Suardi. Two "
                    "treatment rooms, a waiting room, a four-square-metre "
                    "tisane bar.",
            },
            {
                "year":  "2014",
                "title": "The cloister of officinal herbs",
                "body":
                    "The interior cloister is restored and the first "
                    "officinal-herb garden is planted: lemon balm, "
                    "lavender, clary sage, St John's wort, nettle, "
                    "peppermint.",
            },
            {
                "year":  "2018",
                "title": "The hammam and steam room",
                "body":
                    "The hammam room is added, with a barrel vault of "
                    "salvaged brick, designed by architect Valeria Cipolli "
                    "in dialogue with the Heritage Office.",
            },
            {
                "year":  "2022",
                "title": "The Breath Studio",
                "body":
                    "The Breath Studio opens on the first floor, on "
                    "restored period parquet, dedicated to yoga, meditation "
                    "and somatic group practice (six people maximum).",
            },
        ],

        "cta_label": "The next step",
        "cta_heading": 'Meeting <em>Studio Armonia</em> in person',
        "cta_sub":
            "The threshold is not crossed online. Reserve a short ritual "
            "— sixty-five minutes — and let the room do the rest.",
        "cta_primary":   "Reserve a ritual",
        "cta_secondary": "Read the rituals",
    },

    # ──────────────────── RITUALI (services) ────────────────────
    "rituali": {
        "eyebrow":  "Ritual pricelist",
        "headline": "Ten rituals, <em>no fast lane</em>",
        "intro":
            "Every ritual has a precise length, a dedicated practitioner, "
            "a liturgy that has settled over the years. Prices are final "
            "— there are no weekend surcharges nor hidden supplements.",

        "treatments": [
            {
                "name":  "Mediterranean Massage",
                "meta":  "55 min · Sorrento olive oil and citrus",
                "desc":
                    "Long pressures, cold-pressed warm oil, essences of "
                    "bergamot and Sorrento lemon. Suited to first-time "
                    "guests, or to those seeking a gentle introductory "
                    "ritual.",
                "price": "€ 85",
            },
            {
                "name":  "Hammam Ritual",
                "meta":  "90 min · steam, coarse salt, red clay",
                "desc":
                    "Twenty-four minutes in the steam room with essential "
                    "oils of eucalyptus, scrub with coarse Adriatic salt, "
                    "red clay mask from the Bolognese hills, spring-water "
                    "shower, closing tisane. Four-handed.",
                "price": "€ 120",
            },
            {
                "name":  "Energetic Rebalance",
                "meta":  "60 min · pranotherapy and guided breath",
                "desc":
                    "A non-contact pranotherapy session held by Chiara "
                    "Bonomi, with guided breath practice in the first and "
                    "final ten minutes. Suitable during pregnancy from the "
                    "second trimester.",
                "price": "€ 95",
            },
            {
                "name":  "Alpine Hydrotherapy",
                "meta":  "75 min · Monte Resegone spring waters",
                "desc":
                    "Three-basin circuit at rising temperatures with "
                    "spring waters bottled at source, alternated with "
                    "cold jets. Led by Davide Lai.",
                "price": "€ 110",
            },
            {
                "name":  "Hot Stones",
                "meta":  "75 min · volcanic basalt · almond oil",
                "desc":
                    "Twelve basalt stones heated to 48 °C rested upon the "
                    "Shu points of the back, releasing massage with sweet "
                    "almond oil and essential oil of frankincense.",
                "price": "€ 105",
            },
            {
                "name":  "Ayurveda Abhyanga",
                "meta":  "90 min · warm medicated oils · two practitioners",
                "desc":
                    "The classical Ayurvedic ritual, held by Yara Bonomi "
                    "together with a second practitioner. Medicated oils "
                    "are chosen on the basis of the constitution (Vata, "
                    "Pitta, Kapha) identified during the preliminary "
                    "consultation.",
                "price": "€ 135",
            },
            {
                "name":  "Shiatsu",
                "meta":  "60 min · meridian pressures · on futon",
                "desc":
                    "Traditional shiatsu session held by Miguel Ferrari on "
                    "a Japanese futon. The guest remains clothed in "
                    "comfortable garments provided by the studio.",
                "price": "€ 90",
            },
            {
                "name":  "Lomi-Lomi",
                "meta":  "75 min · Hawaiian long-wave massage",
                "desc":
                    "Long waves with forearm and palm, tropical oils of "
                    "coconut and monoi. Led by Yara Bonomi, certified by "
                    "the Hawaiian Lomi-Lomi School of Kauai.",
                "price": "€ 115",
            },
            {
                "name":  "Craniosacral",
                "meta":  "55 min · light touch · cerebrospinal fluids",
                "desc":
                    "Craniosacral osteopathic session held by Davide Lai. "
                    "Very light pressures (under five grammes) to listen "
                    "for and accompany the rhythm of the fluids. Suitable "
                    "during pregnancy.",
                "price": "€ 95",
            },
            {
                "name":  "Mother-Earth Ritual",
                "meta":  "105 min · complete seasonal ritual",
                "desc":
                    "Our longest ritual, designed for the turns of the "
                    "season: brief hydrotherapy, full-body scrub, massage "
                    "with seasonal oils, closing rite with Tibetan bowl "
                    "and rosehip tisane.",
                "price": "€ 150",
            },
        ],
        "reserve_label": "Reserve",

        "advice_label":   "Before your ritual",
        "advice_heading": "Three <em>attentions</em> we recommend",
        "advice": [
            {
                "title": "Arrive fifteen minutes early",
                "body":
                    "The transition is not a luxury: it is part of the "
                    "ritual. Fifteen minutes in the waiting room, with a "
                    "warm tisane, allow the nervous system to align itself "
                    "to the space.",
            },
            {
                "title": "Avoid coffee in the preceding two hours",
                "body":
                    "Caffeine makes the body more reactive to pressures "
                    "and shortens the window of release. A tisane, a glass "
                    "of warm water, a chamomile: far better.",
            },
            {
                "title": "Share every attention",
                "body":
                    "Pregnancy, menstrual cycle, olfactory sensitivities, "
                    "recent injuries, medications: tell us at the moment of "
                    "booking. They are not awkward — they are useful to "
                    "your practitioner.",
            },
        ],

        "packages_label":   "Packages · long weekends",
        "packages_heading": 'Two <em>stays</em> conceived as parentheses',
        "packages_intro":
            "Two proposals stitched together with partner hotels in Bergamo "
            "Alta for those seeking a short restorative stay.",
        "packages": [
            {
                "tag":       "Single day",
                "title":     "Breath",
                "duration":  "1 day · 3 rituals · unlimited tisanes",
                "desc":
                    "A full day at the studio with three concatenated "
                    "rituals, access to the tisane bar from ten to six, "
                    "light lunch in-house prepared by chef Matteo Riva.",
                "includes": [
                    "Arrival 10:00, departure by 18:00",
                    "Energetic Rebalance (60 min)",
                    "Mediterranean Massage (55 min)",
                    "Short Mother-Earth Ritual (75 min)",
                    "Light lunch · unlimited tisane bar",
                ],
                "price": "€ 340",
                "cta":   "Reserve Breath",
            },
            {
                "tag":       "Three days",
                "title":     "Three-day Detox",
                "duration":  "3 days · 5 rituals · seasonal tisane bar",
                "desc":
                    "Three days stitched together with four-star Hotel "
                    "Gombit (double room included), five rituals spread "
                    "across the three days, vegetarian meal plan agreed "
                    "with the naturopath.",
                "includes": [
                    "2 nights · Hotel Gombit 4★",
                    "Five rituals across three days",
                    "Vegetarian meal plan by the naturopath",
                    "Free access to the cloister and the Breath Studio",
                    "Seasonal take-home kit · valued at € 85",
                ],
                "price": "€ 920",
                "cta":   "Reserve the three days",
            },
        ],

        "cta_label": "The next step",
        "cta_heading": 'A single <em>threshold</em> to cross',
        "cta_sub":
            "Reserve the ritual that most invites you. If you are not sure "
            "which one, write to us: we will guide you.",
        "cta_primary":   "Open the reservation form",
        "cta_secondary": "Ask for guidance",
    },

    # ──────────────────── AMBIENTI (gallery) ────────────────────
    "ambienti": {
        "eyebrow":  "Palazzo Bonomi Suardi",
        "headline": 'Eight <em>rooms</em>, a cloister, a tisane bar',
        "intro":
            "Every room has been restored in dialogue with the "
            "Superintendency for Architectural Heritage of Bergamo. Exposed "
            "brick, period parquet, windows that open onto the cloister of "
            "officinal herbs.",
        "rooms": [
            {
                "span":  "a",
                "image": _ROOM_HAMMAM,
                "tag":   "Room I · Hammam",
                "title": "Vaulted Hammam",
                "sub":
                    "Barrel vault in brick salvaged during restoration, "
                    "two-level seating, coarse-salt scrub and cold "
                    "spring-water jet.",
            },
            {
                "span":  "b",
                "image": _AMBIENT_MASSAGE,
                "tag":   "Room II · Massage",
                "title": "The Sun Room",
                "sub":
                    "Two side-by-side beds for four-handed rituals. "
                    "Raking light from the south-east.",
            },
            {
                "span":  "c",
                "image": _ROOM_WATER,
                "tag":   "Room III · Water",
                "title": "The Water Ritual Room",
                "sub":
                    "Hammered-copper hydrotherapy basin, three-temperature "
                    "circuit. Spring water from Resegone.",
            },
            {
                "span":  "d",
                "image": _ROOM_TISANERIA,
                "tag":   "Tisane bar",
                "title": "Herb Tisane Bar",
                "sub":
                    "Seasonal blends harvested in our own cloister. Served "
                    "on white Limoges porcelain.",
            },
            {
                "span":  "e",
                "image": _ROOM_GARDEN,
                "tag":   "Cloister",
                "title": "Officinal garden",
                "sub":
                    "Lemon balm, lavender, clary sage, St John's wort, "
                    "nettle. Open to every guest.",
            },
            {
                "span":  "f",
                "image": _AMBIENT_YOGA,
                "tag":   "Breath Studio",
                "title": "Breath Studio",
                "sub":
                    "Restored period parquet, raw-wool rugs, maximum six "
                    "people per group session.",
            },
            {
                "span":  "g",
                "image": _ROOM_MEDITATION,
                "tag":   "Room IV · Meditation",
                "title": "The Silence Chamber",
                "sub":
                    "Six organic-cotton tatami, an antique Tibetan bowl, "
                    "candlelight in beeswax.",
            },
            {
                "span":  "h",
                "image": _ROOM_RECEPTION,
                "tag":   "Entrance",
                "title": "Threshold · Reception",
                "sub":
                    "Original seventeenth-century floor, guest book, first "
                    "warm tisane beyond the threshold.",
            },
        ],

        "cta_label": "The next step",
        "cta_heading": 'Cross <em>the threshold</em>',
        "cta_sub":
            "Rooms are inhabited, not photographed. The best way to know "
            "them is a short sixty-minute ritual.",
        "cta_primary":   "Reserve a ritual",
        "cta_secondary": "Choose a treatment",
    },

    # ──────────────────── PROFESSIONISTI (team) ────────────────────
    "professionisti": {
        "eyebrow":  "Our practitioners",
        "headline": 'Five <em>signatures</em>, a single guest book',
        "intro":
            "Every practitioner has specific training, a personal diary "
            "and a distinct treatment signature. Whoever welcomes you at "
            "the threshold is the same person who accompanies you into "
            "the ritual.",

        "people": [
            {
                "name":     "Sara Conti",
                "role":     "Naturopath · Co-founder",
                "portrait": _PORTRAIT_SARA,
                "tags":     ["Phytotherapy", "Hydrotherapy", "Seasonal programme"],
                "bio":
                    "Graduated in Naturopathy from Istituto Riza in Milan "
                    "in 2009 and certified by FIF (Italian Federation of "
                    "Phytotherapists). After five years at Spa du Château "
                    "in Annecy she returned to Bergamo and co-founded "
                    "Studio Armonia with Chiara Bonomi. She oversees the "
                    "seasonal cleansing programme and the officinal garden "
                    "in the cloister.",
                "quote":
                    "“There is no detox diet. There is a repeated attention "
                    "to how you eat, when you breathe, how much you sleep.”",
            },
            {
                "name":     "Davide Lai",
                "role":     "Osteopath D.O.",
                "portrait": _PORTRAIT_DAVIDE,
                "tags":     ["Craniosacral", "Visceral", "Structural"],
                "bio":
                    "Graduated from the Scuola Superiore di Osteopatia "
                    "Italiana (S.S.O.I.) in 2014, specialised in "
                    "craniosacral and visceral techniques. He receives on "
                    "Tuesdays and Thursdays by appointment, and is the "
                    "studio's reference for post-partum and chronic pain.",
                "quote":
                    "“The body already knows how to heal — my work is to "
                    "listen for where it has stopped doing so.”",
            },
            {
                "name":     "Yara Bonomi",
                "role":     "Ayurvedic practitioner",
                "portrait": _PORTRAIT_YARA,
                "tags":     ["Abhyanga", "Lomi-Lomi", "Shirodhara"],
                "bio":
                    "Trained in Varkala (Kerala, India) at the Kerala "
                    "Ayurveda Academy in 2016, certified by the Italian "
                    "Ayurvedic Society (S.I.A.). She holds the Abhyanga "
                    "and Shirodhara rituals — always four-handed — and "
                    "the Hawaiian Lomi-Lomi.",
                "quote":
                    "“Abhyanga is not a massage: it is a conversation with "
                    "the skin, made of oil and of time.”",
            },
            {
                "name":     "Elena Rossi",
                "role":     "Certified yoga teacher · RYT-500",
                "portrait": _PORTRAIT_ELENA,
                "tags":     ["Hatha", "Yin", "Somatic breath"],
                "bio":
                    "RYT-500 certified by the Yoga Alliance after four "
                    "years of practice in Rishikesh and two years of "
                    "study with Judith Hanson Lasater in San Francisco. "
                    "She leads group sessions in the Breath Studio on "
                    "Wednesday, Friday and Saturday mornings.",
                "quote":
                    "“The yoga I teach here is not an exotic gymnastics: "
                    "it is a way to remember where the shoulders rest.”",
            },
            {
                "name":     "Miguel Ferrari",
                "role":     "Shiatsu practitioner · FISIEO",
                "portrait": _PORTRAIT_MIGUEL,
                "tags":     ["Namikoshi Shiatsu", "Do-in", "Chinese medicine"],
                "bio":
                    "Graduated from the European School of Shiatsu in "
                    "Milan in 2018 and registered with FISIEO (Italian "
                    "Federation of Shiatsu Operators). He receives on "
                    "Mondays, Wednesdays and Fridays, and curates a "
                    "monthly column on the seasons of the body in "
                    "traditional Chinese medicine.",
                "quote":
                    "“The pressure is not the technique: the technique is "
                    "where I listen before I press.”",
            },
        ],

        "philo_label": "The practitioners' philosophy",
        "philo_quote":
            "“A ritual well held <em>adds</em> nothing to the one who "
            "receives it: it merely reminds them of what they already knew.”",
        "philo_attr": "— Practitioners' manifesto · 2015",

        "cta_label":   "The next step",
        "cta_heading": 'Reserve your <em>first meeting</em>',
        "cta_primary": "Open the reservation form",
    },

    # ──────────────────── CONTATTI (contact) ────────────────────
    "contatti": {
        "eyebrow":  "Finding the studio",
        "headline": 'Via Arena 15, <em>Bergamo Alta</em>',
        "intro":
            "We sit in the heart of the medieval upper city, steps from "
            "Piazza Vecchia and the Basilica of Santa Maria Maggiore. The "
            "entrance is marked by a satin-brass plaque.",

        "map_image": _MAP_IMG,

        "blocks": [
            {"label": "Address",
             "value": "Via Arena 15",
             "sub":   "24129 Bergamo Alta · Palazzo Bonomi Suardi"},
            {"label": "Telephone",
             "value": "+39 035 412 998",
             "sub":   "Direct line 9:00 – 19:00"},
            {"label": "Email",
             "value": "ritual@studioarmonia.it",
             "sub":   "Reply within the day"},
            {"label": "Special requests",
             "value": "+39 346 772 4108",
             "sub":   "WhatsApp · active 9:00 – 18:00"},
        ],

        "access_label": "How to reach us",
        "access": [
            {"mode": "By car",
             "text": "Monterosso car park (Via Fara), then a five-minute "
                     "walk up to Via Arena."},
            {"mode": "Funicular",
             "text": "Bergamo Alta funicular from Viale Vittorio Emanuele, "
                     "alight at Mercato delle Scarpe, two minutes on foot."},
            {"mode": "On foot",
             "text": "From the rail station in Bergamo Bassa take bus "
                     "line 1 (15 minutes), or enjoy a 35-minute walk "
                     "through the city."},
        ],

        "form_title": "Write to us",
        "form_intro":
            "For enquiries on rituals, gift rituals or stay packages, "
            "please use the form below. We always reply within the next "
            "working day.",

        "form_placeholders": {
            "name":    "Chiara Ferrari",
            "email":   "chiara@email.com",
            "phone":   "+39 333 ...",
            "message":
                "I would like to reserve a ritual as a gift, ideally on a "
                "Friday afternoon.",
        },
        "form_helpers": {
            "name":     "How you prefer to be addressed.",
            "email":    "We only use your email to reply.",
            "phone":    "If you would rather we call, please note it here.",
            "interest": "If unsure, choose Initial consultation.",
            "message":  "Keep it to a few lines — we are good at answering "
                        "concrete questions.",
        },
        "form_fields": {
            "interest_label": "Ritual of interest",
            "interest_options": [
                "Initial consultation",
                "Mediterranean Massage",
                "Hammam Ritual",
                "Energetic Rebalance",
                "Ayurveda Abhyanga",
                "Breath Package",
                "Three-day Detox Package",
                "Gift ritual",
                "Other",
            ],
        },
        "form_consent":
            "I consent to the processing of personal data pursuant to "
            "EU Reg. 679/2016. Data is kept within Studio Armonia and is "
            "never passed to third parties.",
        "form_submit_note":
            "Reply within the next working day.",

        "hours_label":   "Opening hours",
        "hours_heading": 'Open <em>six days</em> out of seven',
        "hours_note":
            "On Sundays Studio Armonia observes its day of stillness. For "
            "urgent matters, guests already on a programme may write to "
            "ritual@studioarmonia.it — reply guaranteed within three hours.",
        "hours": [
            {"day": "Monday",    "value": "9:00 – 20:00"},
            {"day": "Tuesday",   "value": "9:00 – 20:00"},
            {"day": "Wednesday", "value": "9:00 – 20:00"},
            {"day": "Thursday",  "value": "9:00 – 20:00"},
            {"day": "Friday",    "value": "9:00 – 20:00"},
            {"day": "Saturday",  "value": "9:00 – 18:00"},
            {"day": "Sunday",    "value": "Day of stillness"},
        ],
    },

    # ──────────────────── PRENOTA (appointment) ────────────────────
    "prenota": {
        "eyebrow":  "Reservation",
        "headline": 'The ritual begins the moment you <em>cross the threshold</em>',
        "intro":
            "The booking is the first gesture of the ritual. Choose the "
            "day that most invites you, fill in the form below: we will "
            "reply within two working hours to confirm.",

        "calendar_heading": 'Seven days of <em>next availability</em>',
        "calendar_hint":    "Indicative · confirmation by email",
        "calendar": [
            {"day": "Mon", "num": "14", "month": "Apr",
             "slots": ["10:00", "14:30", "17:00"], "has_slots": True, "soldout": False},
            {"day": "Tue", "num": "15", "month": "Apr",
             "slots": ["09:30", "13:00", "15:00"], "has_slots": True, "soldout": False},
            {"day": "Wed", "num": "16", "month": "Apr",
             "slots": ["11:00", "16:30"],          "has_slots": True, "soldout": False},
            {"day": "Thu", "num": "17", "month": "Apr",
             "slots": ["fully booked"],            "has_slots": False, "soldout": True},
            {"day": "Fri", "num": "18", "month": "Apr",
             "slots": ["10:30", "14:00", "18:00"], "has_slots": True, "soldout": False},
            {"day": "Sat", "num": "19", "month": "Apr",
             "slots": ["fully booked"],            "has_slots": False, "soldout": True},
            {"day": "Sun", "num": "20", "month": "Apr",
             "slots": ["stillness"],               "has_slots": False, "soldout": True},
        ],

        "form_title":
            'Reservation <em>form</em>',
        "form_side_note":
            "Allow five minutes to complete with care. The more detail you "
            "leave us, the more the ritual we propose will be aligned with "
            "you.",
        "form_side_small": "↓ Private form",

        "why_label": "Why book online",
        "why": [
            "Email confirmation within two working hours.",
            "Courteous cancellation up to 24 hours prior, at no cost.",
            "Sensitivities and attentions read in advance by the practitioner.",
            "Your slot is held until we confirm from our side.",
        ],

        "form_fields": [
            {"name": "name", "label": "Full name",
             "placeholder": "Chiara Ferrari",
             "type": "text", "required": True, "full_width": False,
             "helper": "How you prefer to be addressed."},
            {"name": "email", "label": "Email",
             "placeholder": "chiara@email.com",
             "type": "email", "required": True, "full_width": False,
             "helper": "Confirmation arrives here."},
            {"name": "phone", "label": "Telephone",
             "placeholder": "+39 333 ...",
             "type": "tel", "required": True, "full_width": False,
             "helper": "Used only if needed."},
            {"name": "ritual", "label": "Ritual",
             "type": "select", "required": True, "full_width": False,
             "options": [
                 "Mediterranean Massage (55 min · € 85)",
                 "Hammam Ritual (90 min · € 120)",
                 "Energetic Rebalance (60 min · € 95)",
                 "Alpine Hydrotherapy (75 min · € 110)",
                 "Hot Stones (75 min · € 105)",
                 "Ayurveda Abhyanga (90 min · € 135)",
                 "Shiatsu (60 min · € 90)",
                 "Lomi-Lomi (75 min · € 115)",
                 "Craniosacral (55 min · € 95)",
                 "Mother-Earth Ritual (105 min · € 150)",
                 "Breath Package (1 day · € 340)",
                 "Three-day Detox Package (€ 920)",
             ],
             "helper": "If unsure, choose the Mediterranean Massage: it is "
                       "the gentlest introduction to our work."},
            {"name": "duration", "label": "Preferred length",
             "type": "select", "required": False, "full_width": False,
             "options": [
                 "55 minutes",
                 "60 minutes",
                 "75 minutes",
                 "90 minutes",
                 "105 minutes",
             ],
             "helper": "Optional · consistent with the ritual chosen."},
            {"name": "therapist", "label": "Preferred practitioner",
             "type": "select", "required": False, "full_width": False,
             "options": [
                 "No preference",
                 "Sara Conti (naturopath)",
                 "Davide Lai (osteopath)",
                 "Yara Bonomi (ayurveda)",
                 "Elena Rossi (yoga)",
                 "Miguel Ferrari (shiatsu)",
             ],
             "helper": "If you would like a specific practitioner, note it here."},
            {"name": "date", "label": "Preferred date",
             "placeholder": "14 April 2026",
             "type": "date", "required": True, "full_width": False,
             "helper": "Indicate your first choice; we will propose "
                       "alternatives if unavailable."},
            {"name": "slot", "label": "Time band",
             "type": "select", "required": True, "full_width": False,
             "options": [
                 "Morning (9:00 – 12:30)",
                 "Early afternoon (13:00 – 15:30)",
                 "Afternoon (15:30 – 18:00)",
                 "Late afternoon (18:00 – 20:00)",
             ],
             "helper": "Bands are indicative; we confirm the exact time."},
            {"name": "notes", "label": "Attentions and sensitivities",
             "placeholder":
                 "Pregnancy? Olfactory sensitivities? Recent injuries? "
                 "Anything your practitioner should know? We will read it "
                 "here.",
             "type": "textarea", "required": False, "full_width": True,
             "helper": "Nothing is too small. Pregnancy, cycle, medication, "
                       "anxieties: we read everything in advance."},
        ],

        "form_sections": [
            {"num": "01", "title": "Who you are",
             "meta": "Your essential coordinates.",
             "fields": ["name", "email", "phone"]},
            {"num": "02", "title": "The ritual you wish for",
             "meta": "If in doubt, choose 'no preference' — we will guide you.",
             "fields": ["ritual", "duration", "therapist"]},
            {"num": "03", "title": "When",
             "meta": "Give us your first choice · we confirm by email.",
             "fields": ["date", "slot"]},
            {"num": "04", "title": "Attentions",
             "meta": "Everything your practitioner should know beforehand.",
             "fields": ["notes"]},
        ],

        "consent":
            "I consent to the processing of personal data under the privacy "
            "notice (EU Reg. 679/2016). Clinical data and stated attentions "
            "are held in the private internal archive.",

        "submit_label": "Reserve your moment",
        "form_submit_note":
            "We confirm availability within two working hours.",

        "footnote":
            "The reservation is confirmed only after our reply email. "
            "Courteous cancellation is possible at no cost up to twenty-four "
            "hours before the ritual — thereafter, we retain 50% of the "
            "value as a safeguard for the practitioner.",
    },
}

__all__ = ["BENESSERE_CONTENT_EN"]
