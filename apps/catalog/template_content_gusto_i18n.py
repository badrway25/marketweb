"""Gusto fine-dining i18n content trees — EN / FR / ES / AR.

Phase 2i.2 step 2 (Session 29): extends the locale-keyed content
registry to gusto-fine-dining. The Italian tree (GUSTO_CONTENT_IT)
lives in template_content.py; this file carries the four non-IT
locales.

Authoring rules (same as cardio/derm i18n files):
- Locale-specific editorial voice, NOT literal translation. Each
  locale reads as if written by a native speaker of premium
  fine-dining hospitality writing.
- Non-localizable data (phone, email, address, image URLs, prices,
  press outlets, wine/producer names, chef/staff names) repeated
  as-is across every locale.
- `pages` list: same slugs + kinds, only labels translated.
- Page slugs (home / filosofia / menu / atmosfera / diario / prenota)
  stay Italian across every locale — avoids per-locale URL maps,
  works for Arabic (ASCII URLs), matches the architectural decision
  from Session 23.
- Wine names, producer names, dish proper names (Piccione di Bresse,
  Risotto al midollo, Barolo Cannubi, Tarbouriech, Pacherhof, Domori,
  San Massimo, Pieropan, Selosse) stay in Latin/Italian script because
  that's how they're known in world food press.
- Press outlets (GUIDA MICHELIN, GAMBERO ROSSO, IDENTITÀ GOLOSE,
  CORRIERE LIVING, VOGUE FOOD) stay in Latin script.
- No machine translation. No placeholder strings. Quality floor:
  reads as a native food writer's work.
- RTL arrows: in Arabic, directional glyphs (←→) are flipped where
  they're reading cues.
"""
from __future__ import annotations
from typing import Any


# ---------------------------------------------------------------------------
# Shared image URL constants — repeated verbatim across every locale.
# Duplicating flat per-locale is the deliberate authoring choice (same as
# cardio/derm i18n files) — keeps review surface = 1 locale per pass.
# ---------------------------------------------------------------------------

_INGREDIENTI_IMG = (
    "https://images.unsplash.com/photo-1610348725531-843dff563e2c"
    "?auto=format&fit=crop&w=1000&q=80"
)
_FILOSOFIA_IMG = (
    "https://images.unsplash.com/photo-1559329007-40df8a9345d8"
    "?auto=format&fit=crop&w=1400&q=80"
)
_ATMO_SALA = (
    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4"
    "?auto=format&fit=crop&w=600&q=80"
)
_ATMO_CUCINA = (
    "https://images.unsplash.com/photo-1581349485608-9469926a8e5e"
    "?auto=format&fit=crop&w=600&q=80"
)
_ATMO_CORTILE = (
    "https://images.unsplash.com/photo-1559329007-40df8a9345d8"
    "?auto=format&fit=crop&w=600&q=80"
)
_ATMO_MISE = (
    "https://images.unsplash.com/photo-1414235077428-338989a2e8c0"
    "?auto=format&fit=crop&w=600&q=80"
)


# ===========================================================================
# ENGLISH — Anglo-American fine-dining editorial voice
# Reads like a New York Times Magazine food feature. "One service per night",
# "tasting menu", "eight courses", Michelin terminology.
# ===========================================================================

GUSTO_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "Home",         "kind": "home"},
        {"slug": "filosofia", "label": "Philosophy",   "kind": "about"},
        {"slug": "menu",      "label": "Menu",         "kind": "menu"},
        {"slug": "atmosfera", "label": "Rooms",        "kind": "gallery"},
        {"slug": "diario",    "label": "Journal",      "kind": "blog_list"},
        {"slug": "prenota",   "label": "Reserve",      "kind": "reservations"},
    ],

    "site": {
        "logo_initial": "OM",
        "logo_word":    "Osteria Moderna",
        "tag":          "One table · Milan, Brera · 14 covers",
        "phone":        "+39 02 3611 9920",
        "email":        "concierge@osteriamoderna.it",
        "address":      "Via San Marco 17 · 20121 Milan",
        "hours_compact":"Wed – Sat · dinner only",
        "star_line":    "★ One Michelin star · est. 2018",
        "footer_intro":
            "Michelin-starred since 2018. Fourteen covers, two services a "
            "week, an eight-course tasting menu that changes every two weeks.",
        "footer_hours_1": "Wed – Sat · 8:00 pm",
        "footer_hours_2": "Sun & Mon · closed",
        "copyright": "© 2026 Osteria Moderna · VAT 09456112094",
    },

    "home": {
        "eyebrow":  "One table · Milan, Brera · 14 covers",
        "headline": "An evening in <em>eight acts.</em>",
        "intro":
            "A tasting menu that rewrites itself every two weeks around the "
            "morning market. Dinner only. Reservation only. For fourteen guests.",
        "primary_cta":   "Reserve the evening",
        "primary_href":  "prenota",
        "secondary_cta": "Meet the chef",
        "secondary_href":"filosofia",

        "chef_label":    "The chef",
        "star_tag":      "★ Act V · 80% Chocolate",
        "photo_label":   "Photography",
        "cuisine_label": "Kitchen",

        "facts": [
            ("14",   "covers per service"),
            ("8",    "acts in the tasting menu"),
            ("180€", "full menu · wine pairing + €90"),
        ],

        "manifesto_drop_cap": "A",
        "manifesto":
            " menu that rewrites itself every two weeks. One dining room of "
            "fourteen covers. An open kitchen that works in silence for four "
            "continuous hours. At Osteria Moderna you do not order à la carte — "
            "you enter a story with an opening, a climax and a close.",

        "signature_courses": [
            ("I",   "Oyster & cucumber",      "sorrel, yuzu pearls",                "Champagne Selosse"),
            ("II",  "Risotto with marrow",    "parsley extract, coffee",            "Soave Pieropan '21"),
            ("III", "Roasted scallop",        "hazelnut butter, Pantelleria capers","Riesling Pacherhof"),
            ("IV",  "Bresse pigeon",          "black figs, green cardamom",         "Barolo Cannubi '17"),
            ("V",   "80% chocolate",          "EVO oil, Maldon salt",               "Marsala Vintage '99"),
        ],

        "courses_label": "Five acts from the running menu · autumn '26",
        "courses_footline": "€ 180 per person · wine pairing + €90",
        "courses_full_cta": "All eight acts",
        "chef_link_filosofia": "The philosophy",
        "chef_link_diario": "The journal",

        "chef": {
            "name":  "Lorenzo Fioravanti",
            "role":  "Chef patron · 1 Michelin star",
            "bio":
                "Born in Rome in 1981. Trained under Bottura, Cracco, and "
                "Brutscher at Mirazur. Opened Osteria Moderna in 2014 in "
                "three rooms of an eighteenth-century Brera palazzo. "
                "Earned a Michelin star in 2018 — held every year since.",
        },

        "press_label": "As seen in",
        "press": ["GUIDA MICHELIN", "GAMBERO ROSSO", "IDENTITÀ GOLOSE",
                  "CORRIERE LIVING", "VOGUE FOOD"],

        "ingredienti": {
            "label": "Sourcing",
            "heading": "Thirty-two growers, <em>all on first-name terms.</em>",
            "text":
                "Osteria Moderna works with a network of thirty-two small "
                "producers — Ligurian fishermen, Piedmontese cattle breeders, "
                "Lodi market gardeners — and Lorenzo knows every one of them "
                "by name, address and mobile number. No middlemen, no catalogue, "
                "no distribution channel.",
            "image": _INGREDIENTI_IMG,
            "image_caption": "Autumn '26 menu ingredients · morning market",
        },

        "atmosphere_teaser": {
            "label": "The rooms",
            "images": [
                (_ATMO_SALA,    "The main dining room"),
                (_ATMO_CUCINA,  "The open kitchen"),
                (_ATMO_CORTILE, "The wisteria courtyard"),
                (_ATMO_MISE,    "Friday-evening mise en place"),
            ],
            "link_label": "Step inside",
            "link_href":  "atmosfera",
        },

        "riconoscimenti": {
            "label": "Recognition",
            "items": [
                ("★", "Michelin Star", "Since 2018 — confirmed every year"),
                ("GR", "Gambero Rosso", "Three Forks · Author-cuisine special prize 2025"),
                ("IG", "Identità Golose", "Dish of the Year 2024 — Bresse pigeon"),
                ("50B", "50 Best Discovery", "Italy selection 2026"),
            ],
        },

        "cta_heading": "Fourteen covers, <em>two services a week.</em>",
        "cta_primary": "Reserve the evening",
        "cta_secondary": "See the full menu",

        "stagione": {
            "label": "Now serving",
            "title": "Autumn '26 menu",
            "subtitle": "Eight acts · 6 to 19 October",
            "text":
                "The new menu has been on the table since Monday. Eight dishes, "
                "four new compositions and four variations on themes we left "
                "in the archive back in 2022. Reservation mandatory.",
            "cta_label": "Discover all eight acts →",
            "cta_href":  "menu",
        },

        "produttori": {
            "label":   "From the producers",
            "heading": "Four hands, <em>a single table.</em>",
            "intro":
                "Every morning part of the dining room comes in through the "
                "kitchen door. The faces are these. Their land, their method — "
                "you'll find them on the menu, line by line.",
            "items": [
                {"portrait":
                    "https://images.unsplash.com/photo-1552058544-f2b08422138a"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Roberto Tarbouriech",
                 "role": "Oysters & shellfish",
                 "area": "Sète · Étang de Thau",
                 "blurb":
                    "The Spéciales oysters come from the Étang de Thau lagoon. "
                    "Delivery on Monday, served Tuesday evening."},
                {"portrait":
                    "https://images.unsplash.com/photo-1568213816046-0ee1c42bd559"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Brezza family",
                 "role": "Barolo & the Langhe",
                 "area": "Barolo · Piedmont",
                 "blurb":
                    "Vineyards in Cannubi and Sarmassa, worked without an "
                    "external oenologist. A vertical on our list from 2008 on."},
                {"portrait":
                    "https://images.unsplash.com/photo-1543418219-44e30b057fea"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Aloïs Lageder",
                 "role": "Mountain biodynamics",
                 "area": "Pacherhof · South Tyrol",
                 "blurb":
                    "White wines delivered directly from the Isarco valley. "
                    "No filtering, no fining."},
                {"portrait":
                    "https://images.unsplash.com/photo-1414235077428-338989a2e8c0"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Gianfranco Pieropan",
                 "role": "Soave Classico",
                 "area": "Soave · Veneto",
                 "blurb":
                    "Calvarino and La Rocca, Soave Classico in purity. They "
                    "have always accompanied the second act."},
            ],
        },
        "private_dining": {
            "label":   "Private events",
            "heading": "Chef's Table & <em>private buy-outs.</em>",
            "intro":
                "For twelve covers in the private room or for the whole "
                "evening — twenty-eight covers, one menu, open kitchen.",
            "experiences": [
                {"icon": "fork", "title": "Chef's Table",
                 "meta":  "12 covers · from €190 / guest",
                 "desc":
                    "A single table overlooking the kitchen. Eight-act menu "
                    "narrated directly by the chef. Tuesdays only."},
                {"icon": "door", "title": "Evening buy-out",
                 "meta":  "28 covers · from €5,800 / night",
                 "desc":
                    "The entire restaurant, a dedicated menu, flowers, "
                    "personal maître d'hôtel. Two-week notice; Fridays declined."},
                {"icon": "wine", "title": "Cellar tasting",
                 "meta":  "6 covers · Thursdays only",
                 "desc":
                    "An evening a month with the sommelier on six bottles "
                    "chosen from the producers on the list. Waiting list only."},
            ],
            "cta_label": "Write to the concierge",
            "cta_href":  "prenota",
        },
        "wine_program": {
            "label":   "The cellar",
            "heading": "Four hundred labels, <em>three pairings per night.</em>",
            "intro":
                "The list follows the menu: every act has its pairing and two "
                "alternatives — classic, contemporary, non-alcoholic.",
            "sommelier": {
                "name": "Greta Vallesi",
                "role": "Maître & sommelier",
                "bio":
                    "Fifteen years between Burgundy, the Langhe and Champagne. "
                    "The list is curated by her, the pairing is always offered "
                    "at the table, never imposed.",
            },
            "pairings": [
                ("01", "Classic pairing",
                 "Blanc de blancs Champagne, Soave Classico, Barolo riserva, Moscato.",
                 "+ €110"),
                ("02", "Contemporary pairing",
                 "Col Fondo from the Veneto, long Erbaluce, amphora Ribolla, "
                 "Timorasso vertical.",
                 "+ €130"),
                ("03", "Zero-alcohol pairing",
                 "Artisan kombucha, slow-infused iced teas, naturally fermented "
                 "grape juice.",
                 "+ €60"),
            ],
            "cellar_facts": [
                ("420", "labels on the list"),
                ("18", "wine regions"),
                ("2005", "oldest vertical (Brunello)"),
            ],
        },
    },

    "filosofia": {
        "eyebrow":  "Philosophy",
        "headline": "One menu, one room, <em>one evening only.</em>",
        "intro":
            "Osteria Moderna was born in 2014 from the idea that a restaurant "
            "is not a service but a theatre. Fourteen covers per service, "
            "two services a week, one cook at the pass, one maître on the floor.",

        "history": [
            ("2014",
             "Lorenzo Fioravanti opens Osteria Moderna in three rooms of an "
             "eighteenth-century palazzo in Brera. Sixteen covers, a single "
             "brigade, a menu that changes every Friday."),
            ("2016",
             "Greta Vallesi joins as maître and cellar manager. The wine list "
             "goes from 80 to 320 references, with a focus on small growers "
             "from North-East Italy and lesser Burgundy."),
            ("2018",
             "Michelin star. From that moment the restaurant narrows to "
             "fourteen covers per service and makes the eight-act tasting "
             "menu the only way to dine."),
            ("2021",
             "The pass opens onto the dining room. The chef cooks in front of "
             "guests for the entire length of service. No wall between kitchen "
             "and table."),
            ("2024",
             "Publication of 'Eight Acts', Giunti editions, a book dedicated "
             "to the first forty evenings of the 2023/24 winter menu."),
        ],

        "filosofia_image": _FILOSOFIA_IMG,
        "filosofia_image_caption": "The kitchen · Lorenzo Fioravanti at work",

        "method_title": "Method",
        "method_paragraphs": [
            "The tasting menu rewrites itself every two weeks around the "
            "morning market. The ingredients arrive from a network of "
            "thirty-two small producers — Ligurian fishermen, Piedmontese "
            "breeders, Lodi market gardeners — and Lorenzo knows each one "
            "by name, address and mobile number.",
            "Each act is composed as a movement of a symphony: there is a "
            "prelude, a mid-service crescendo, a lyrical pause, a finale "
            "that circles back to the opening. The sequence is rewritten "
            "from scratch every two weeks — we never repeat the same "
            "transitions twice.",
            "The wine list is curated by Greta Vallesi: 320 references, "
            "two thirds from small European growers. The pairing is optional "
            "(€ 90 for the full path) but — let us be frank about it — it is "
            "half the work we do.",
        ],

        "values_label": "What we promise",
        "values_heading": "Four promises that <em>will not change</em>.",
        "values": [
            ("Time",        "Three and a half hours of service. Never more, never less."),
            ("Season",      "Nothing on the table that is not locally in season."),
            ("Transparency","We know every producer on the list by first name."),
            ("Discretion",  "No chef photos, no social: the dining room is for dining."),
        ],

        "cta_heading": "Would you like to see the menu <em>running this week?</em>",
        "cta_menu": "The eight acts of autumn '26",
        "cta_prenota": "Reserve the evening",
    },

    "menu": {
        "eyebrow":  "The menu",
        "headline": "Eight acts — <em>autumn '26</em>",
        "intro":
            "The menu is rewritten in full every two weeks. Below is the "
            "programme running from 6 to 19 October 2026. Two services a week, "
            "Wednesday through Saturday, a single sitting from 8:00 pm.",
        "courses_label": "Eight acts · service from 8:00 pm",

        "courses": [
            ("I",    "Oyster & cucumber",
             "Tarbouriech oyster from Sète, organic Lake Como cucumber gel, "
             "wild sorrel, yuzu pearls suspended in Taggiasca olive oil.",
             "Champagne Anselme Selosse · Initial · Avize"),
            ("II",   "Risotto with marrow",
             "San Massimo Carnaroli Riserva 2023, vine-ember roasted marrow, "
             "curly parsley extract, single-origin Ethiopian coffee dust.",
             "Soave Classico Pieropan · La Rocca '21"),
            ("III",  "Roasted scallop",
             "Galician scallop from free-dive fishery, rosemary hazelnut butter, "
             "salt-cured Pantelleria capers, Amalfi lemon gel.",
             "Riesling Pacherhof · Kerner Alto Adige '22"),
            ("IV",   "House pasta",
             "Hand-rolled cappelletti, filling of Bresse capon and Val Trebbia "
             "black truffle, wild boar broth reduced seven times.",
             "Lambrusco di Sorbara Rinaldini · Rosé Brut"),
            ("V",    "Bresse pigeon",
             "Breast served rare, glazed with chestnut honey; leg confit with "
             "black figs from Caprino, Barolo reduction, green Guatemalan "
             "cardamom dust.",
             "Barolo Riserva Cannubi · Brezza '17"),
            ("VI",   "Pre-dessert",
             "Celeriac sorbet, oxalis from our garden, Dro plum granita, "
             "rose-salt crystals.",
             "—"),
            ("VII",  "80% chocolate",
             "Domori Criollo 80% chocolate, Tuscia extra-virgin olive oil, "
             "apple-wood smoked Maldon salt, Calabrian liquorice dust.",
             "Marsala Vintage Marco De Bartoli · 1999"),
            ("VIII", "Mignardises",
             "Three small author-pastries — one chocolate, one citrus, "
             "one honey.",
             "Single-origin Ethiopia Yirgacheffe coffee"),
        ],

        "wine_intro_title": "Wine list",
        "wine_intro":
            "320 references, two thirds of them from small European growers. "
            "Greta Vallesi is on the floor every evening to discuss each "
            "choice — but she is also happy to build a bespoke pairing path, "
            "off the standard menu.",

        "wine_highlights": [
            ("Champagne", "62 references · 24 grower champagnes"),
            ("Burgundy",  "48 growers · focus on Côte de Beaune and Mâconnais"),
            ("Italy",     "112 references · North-East, High Piedmont and volcanic Sicily"),
            ("Fortifieds","18 references · sherry, marsala, madeira, tokaji"),
        ],

        "footer":
            "Full tasting menu: € 180 per person. Optional wine pairing: "
            "€ 90 per person. Magnum package (six magnum pours, shared "
            "format): + € 140. Please notify any intolerance or allergy "
            "at the time of booking.",
    },

    "atmosfera": {
        "eyebrow":  "The rooms",
        "headline": "Three rooms, <em>fourteen chairs,</em> no walls.",
        "intro":
            "Osteria Moderna occupies three rooms of an eighteenth-century "
            "palazzo on Via San Marco, in Brera. No wall between the kitchen "
            "and the dining room. No photography on social media: to "
            "photograph the plate, here, you look at it calmly, seated.",

        "rooms": [
            ("The main dining room",
             "The heart of the restaurant. Nine covers, three tables, a "
             "full-height window on the inner courtyard of the palazzo."),
            ("The open pass",
             "Five covers at the counter, facing the fires. The chef cooks "
             "in silence for the entire length of service."),
            ("The cellar",
             "An underground room holding 320 labels. Private visits by "
             "reservation, following dinner, guided by Greta Vallesi."),
            ("The courtyard",
             "From May to September, two tables en plein air under the "
             "wisteria of the inner courtyard. Reservable for complete "
             "dinners only."),
        ],

        "captions": [
            "The open pass during the Friday-night service.",
            "The first act of the autumn '26 menu: oyster and cucumber.",
            "Greta Vallesi in the cellar, among the 320 labels.",
            "The inner courtyard of the eighteenth-century Via San Marco palazzo.",
            "Lorenzo Fioravanti during service.",
            "The main dining room at the end of mise en place.",
        ],

        "cta_quote": "«To photograph the dish, here, you look at it calmly, seated.»",
        "cta_desc": "Fourteen covers per service. Reservation only. Dinner only. Wed – Sat.",
        "cta_primary": "Reserve the evening",
        "cta_secondary": "See the menu",
    },

    "diario": {
        "eyebrow":  "The floor journal",
        "headline": "Working notes, <em>seasonal notes</em>, floor notes.",
        "intro":
            "Short entries from Lorenzo Fioravanti and Greta Vallesi on the "
            "running menu, on the producers, on memorable evenings and on "
            "what is shifting in the kitchen from week to week.",
        "read_article": "Read the article",
        "min_label": "min",
        "min_read_label": "min read",
        "crumb_label": "Journal",
        "back_link": "← Back to the journal",
        "footer_label": "Osteria Moderna · The floor journal",
        "empty_body": [
            "Entry currently in editorial review. The full piece will be "
            "published here shortly, written personally by the chef or the maître.",
            "This placeholder describes the voice of the floor journal: "
            "short working notes, reflections on producers, stories of "
            "memorable evenings. Never more than two thousand words, "
            "never fewer than five hundred.",
        ],
    },

    "posts": [
        {
            "slug":     "menu-autunno-26",
            "kicker":   "Running menu",
            "title":    "The eight ideas of the autumn '26 menu",
            "date":     "5 October 2026",
            "read_min": 5,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "The new menu went on the table on Monday night. Eight "
                "dishes — four new compositions and four variations on "
                "themes we had left in the archive back in 2022.",
            "body": [
                ("p", "Writing a tasting menu is less a question of recipes and "
                      "more a question of transitions. How you move from savoury "
                      "to sweet. How you circle back mid-service. How you "
                      "introduce the fourth course without breaking the rhythm. "
                      "For the autumn '26 menu we spent two weeks working on "
                      "nothing but the pauses."),
                ("h2", "The four new ideas"),
                ("p", "The first act — oyster and cucumber — is a rereading of a "
                      "dish my mentor Pierre Brutscher used to make at Mirazur. "
                      "I had carried it in my head since 2007, from my "
                      "apprentice days. For fifteen years I could not write "
                      "the ending. I found it last summer, on a bench in Sète, "
                      "watching Tarbouriech harvest his oysters at dawn."),
                ("p", "The fourth act — house pasta — is the first time in three "
                      "years that we have put pasta inside the tasting menu. "
                      "The filling of capon and black truffle is a tribute to a "
                      "Val Trebbia recipe my maternal grandmother used to "
                      "prepare on Christmas Day."),
                ("h2", "The four variations"),
                ("p", "The Bresse pigeon returns after two seasons. It is my "
                      "signature dish, the one I like most of everything I have "
                      "built since opening. This time I pair it with a Barolo "
                      "Cannubi '17 reduction — a wine Greta found after six "
                      "months of phone calls to the Brezza cellar."),
                ("blockquote",
                 "A tasting menu is not a sequence of dishes. It is a path the "
                 "guest takes with the cook, and one the cook rewalks every "
                 "evening with the guest."),
                ("p", "Thanks to Greta for the pairing, to the floor brigade for "
                      "the patience with which they learned eight new service "
                      "descriptions in two weeks, and to every producer who "
                      "helped us build this menu: Tarbouriech, San Massimo, "
                      "Pacherhof, the Brezza brothers, Domori, Marco De Bartoli."),
            ],
        },
        {
            "slug":     "barolo-cannubi-17-brezza",
            "kicker":   "Wine list",
            "title":    "Six months of phone calls for a Barolo",
            "date":     "20 September 2026",
            "read_min": 4,
            "author":   "Greta Vallesi",
            "lede":
                "The story of how the Barolo Cannubi '17 from Brezza made it "
                "onto the list, and why we wanted it at all costs for the "
                "fifth act of the autumn menu.",
        },
        {
            "slug":     "cucina-a-vista",
            "kicker":   "The floor",
            "title":    "Five years of the open pass: what we've learned",
            "date":     "29 August 2026",
            "read_min": 6,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "Opening the kitchen to the public changed the way the "
                "brigade works. It also changed the way guests dine. "
                "A short reflection, five years after the counter opened.",
        },
        {
            "slug":     "ostriche-tarbouriech",
            "kicker":   "Producers",
            "title":    "Tarbouriech: the oyster farmer who tides every twelve hours",
            "date":     "11 August 2026",
            "read_min": 5,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "In Sète, Languedoc, Florent Tarbouriech devised a farming "
                "method that mimics the Atlantic tide inside the Mediterranean. "
                "The result is the oyster of our first act.",
        },
        {
            "slug":     "libro-otto-atti",
            "kicker":   "Publishing",
            "title":    "'Eight Acts', the first book of Osteria Moderna, is out",
            "date":     "1 July 2026",
            "read_min": 3,
            "author":   "Greta Vallesi",
            "lede":
                "On 4 July Giunti publishes 'Eight Acts — forty evenings of "
                "the Osteria Moderna winter menu'. Lorenzo will present it on "
                "12 July at the Triennale di Milano.",
        },
    ],

    "prenota": {
        "eyebrow":  "Reservation",
        "headline": "A dinner <em>is not booked</em>: it is agreed.",
        "intro":
            "At Osteria Moderna there is no online calendar. Reservations "
            "pass through the restaurant's personal concierge, Greta Vallesi, "
            "who replies by email the same day.",

        "process_label": "How it works",
        "process_heading": "Four steps, <em>four days ahead</em>.",
        "hours_label": "Week's services",
        "hours_heading": "Four evenings, <em>one sitting</em>.",
        "private_heading": "Private dinners",
        "form_submit": "Send a note to the concierge",

        "process": [
            ("01", "Write to Greta",
             "A few lines are enough: preferred date, number of guests, any "
             "intolerances, the occasion. Greta reads every request personally."),
            ("02", "Evening proposal",
             "Within the same day Greta proposes one or two compatible dates "
             "(services run Wednesday to Saturday only) and confirms the "
             "current menu."),
            ("03", "Confirmation & deposit",
             "To confirm the booking we ask for a small deposit of € 80 per "
             "person, which is deducted from the final bill."),
            ("04", "Evening brief",
             "The day before you will receive a short email with the dress "
             "code, the running menu and a note on the optional wine pairing."),
        ],

        "concierge": {
            "name":  "Greta Vallesi",
            "role":  "Maître & cellar manager",
            "email": "greta@osteriamoderna.it",
            "phone": "+39 02 3611 9920",
            "bio":
                "Roman-born, Milanese by adoption. Fifteen years on the "
                "floor, nine of which at Osteria Moderna. AIS Sommelier "
                "since 2014. On the floor every evening from 6:30 to 11:30 pm.",
        },

        "hours": [
            ("Wednesday",  "8:00 pm – 11:30 pm",  "1 service · single sitting"),
            ("Thursday",   "8:00 pm – 11:30 pm",  "1 service · single sitting"),
            ("Friday",     "8:00 pm – 11:30 pm",  "1 service · single sitting"),
            ("Saturday",   "8:00 pm – 11:30 pm",  "1 service · single sitting"),
            ("Sunday",     "Closed",               "—"),
            ("Mon & Tue",  "Closed",               "Brigade weekly rest"),
        ],

        "private_title": "Private dinners & events",
        "private_intro":
            "Private dinners (anniversaries, corporate anniversaries, "
            "product launches) are possible on closure days by reserving "
            "the entire dining room. Bespoke packages agreed personally "
            "with the chef.",

        "form_title":  "Write to the concierge",
        "form_fields": [
            ("Full name",           "Mario Rossi",                         "text"),
            ("Email",               "mario@email.com",                     "email"),
            ("Phone",               "+39 333 ...",                         "tel"),
            ("Number of guests",    "2",                                   "number"),
            ("Preferred date",      "Fri 16 October",                      "text"),
            ("Occasion",            "",                                    "select"),
            ("Allergies or intolerances", "Any allergies, intolerances or special requests", "text"),
            ("Note to the concierge","Greta reads every request personally. A few lines are enough.", "textarea"),
        ],
        "occasion_options": ["Romantic dinner", "Birthday", "Business", "No occasion"],
        "consent":
            "I consent to the processing of my personal data in accordance "
            "with the privacy notice pursuant to EU Regulation 679/2016.",

        "address_block": [
            ("Address",   "Via San Marco 17 · 20121 Milan"),
            ("Transport", "Lanza M2 · 4 minutes on foot · Brera"),
            ("Parking",   "APCOA Garibaldi 36 · complimentary shuttle"),
        ],
    },
}


# ===========================================================================
# FRENCH — Haute cuisine register, vous form
# Michelin-guide French. "Dégustation en huit actes", "un seul service".
# ===========================================================================

GUSTO_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "Accueil",      "kind": "home"},
        {"slug": "filosofia", "label": "Philosophie",  "kind": "about"},
        {"slug": "menu",      "label": "Menu",         "kind": "menu"},
        {"slug": "atmosfera", "label": "Les salles",   "kind": "gallery"},
        {"slug": "diario",    "label": "Journal",      "kind": "blog_list"},
        {"slug": "prenota",   "label": "Réserver",     "kind": "reservations"},
    ],

    "site": {
        "logo_initial": "OM",
        "logo_word":    "Osteria Moderna",
        "tag":          "Une seule table · Milan, Brera · 14 couverts",
        "phone":        "+39 02 3611 9920",
        "email":        "concierge@osteriamoderna.it",
        "address":      "Via San Marco 17 · 20121 Milan",
        "hours_compact":"Mer – Sam · dîner uniquement",
        "star_line":    "★ Une étoile Michelin · depuis 2018",
        "footer_intro":
            "Étoilée Michelin depuis 2018. Quatorze couverts, deux services "
            "par semaine, un menu dégustation en huit actes qui se réécrit "
            "toutes les deux semaines.",
        "footer_hours_1": "Mer – Sam · 20h00",
        "footer_hours_2": "Dim & Lun · fermé",
        "copyright": "© 2026 Osteria Moderna · TVA 09456112094",
    },

    "home": {
        "eyebrow":  "Une seule table · Milan, Brera · 14 couverts",
        "headline": "Une soirée en <em>huit actes.</em>",
        "intro":
            "Un menu dégustation qui se réécrit toutes les deux semaines "
            "selon le marché du matin. Dîner uniquement. Sur réservation. "
            "Pour quatorze convives.",
        "primary_cta":   "Réserver la soirée",
        "primary_href":  "prenota",
        "secondary_cta": "Rencontrer le chef",
        "secondary_href":"filosofia",

        "chef_label":    "Le chef",
        "star_tag":      "★ Acte V · Chocolat 80 %",
        "photo_label":   "Photographie",
        "cuisine_label": "Cuisine",

        "facts": [
            ("14",   "couverts par service"),
            ("8",    "actes au menu dégustation"),
            ("180€", "menu complet · accord vins + 90 €"),
        ],

        "manifesto_drop_cap": "U",
        "manifesto":
            "n menu qui se réécrit toutes les deux semaines. Une seule salle "
            "de quatorze couverts. Une cuisine ouverte qui travaille en "
            "silence pendant quatre heures d'affilée. Chez Osteria Moderna "
            "on ne commande pas à la carte — on entre dans un récit qui a "
            "un début, un climax et une fin.",

        "signature_courses": [
            ("I",   "Huître & concombre",     "oseille, perles de yuzu",              "Champagne Selosse"),
            ("II",  "Risotto à la moelle",     "extrait de persil, café",              "Soave Pieropan '21"),
            ("III", "Coquille Saint-Jacques", "beurre noisette, câpres de Pantelleria","Riesling Pacherhof"),
            ("IV",  "Pigeon de Bresse",        "figues noires, cardamome verte",       "Barolo Cannubi '17"),
            ("V",   "Chocolat 80 %",           "huile d'olive, sel de Maldon",         "Marsala Vintage '99"),
        ],

        "courses_label": "Cinq actes du menu en cours · automne '26",
        "courses_footline": "180 € par personne · accord vins + 90 €",
        "courses_full_cta": "Les huit actes en entier",
        "chef_link_filosofia": "La philosophie",
        "chef_link_diario": "Le journal",

        "chef": {
            "name":  "Lorenzo Fioravanti",
            "role":  "Chef propriétaire · 1 étoile Michelin",
            "bio":
                "Romain, né en 1981. Formé auprès de Bottura, Cracco, "
                "et de Brutscher au Mirazur. Ouvre Osteria Moderna en 2014 "
                "dans trois pièces d'un palais brérien du XVIIIᵉ siècle. "
                "Première étoile Michelin en 2018, confirmée chaque année.",
        },

        "press_label": "Ils en ont parlé",
        "press": ["GUIDA MICHELIN", "GAMBERO ROSSO", "IDENTITÀ GOLOSE",
                  "CORRIERE LIVING", "VOGUE FOOD"],

        "ingredienti": {
            "label": "Les producteurs",
            "heading": "Trente-deux producteurs, <em>tous appelés par leur prénom.</em>",
            "text":
                "Le réseau d'Osteria Moderna compte trente-deux petits "
                "producteurs — pêcheurs ligures, éleveurs piémontais, "
                "maraîchers de Lodi — dont Lorenzo connaît personnellement "
                "le prénom, l'adresse et le numéro de portable. Aucun "
                "intermédiaire, aucun catalogue, aucun grossiste.",
            "image": _INGREDIENTI_IMG,
            "image_caption": "Produits du menu automne '26 · marché du matin",
        },

        "atmosphere_teaser": {
            "label": "Les salles",
            "images": [
                (_ATMO_SALA,    "La salle principale"),
                (_ATMO_CUCINA,  "La cuisine ouverte"),
                (_ATMO_CORTILE, "La cour sous la glycine"),
                (_ATMO_MISE,    "Mise en place du vendredi"),
            ],
            "link_label": "Découvrir les salles",
            "link_href":  "atmosfera",
        },

        "riconoscimenti": {
            "label": "Distinctions",
            "items": [
                ("★", "Étoile Michelin", "Depuis 2018 — confirmée chaque année"),
                ("GR", "Gambero Rosso", "Trois Fourchettes · Prix spécial cuisine d'auteur 2025"),
                ("IG", "Identità Golose", "Plat de l'année 2024 — Pigeon de Bresse"),
                ("50B", "50 Best Discovery", "Sélection Italie 2026"),
            ],
        },

        "cta_heading": "Quatorze couverts, <em>deux services par semaine.</em>",
        "cta_primary": "Réserver la soirée",
        "cta_secondary": "Voir le menu complet",

        "stagione": {
            "label": "En ce moment",
            "title": "Menu automne '26",
            "subtitle": "Huit actes · du 6 au 19 octobre",
            "text":
                "Le nouveau menu est à la carte depuis lundi. Huit plats, "
                "quatre compositions inédites et quatre variations sur des "
                "thèmes laissés à l'archive depuis 2022. Réservation "
                "obligatoire.",
            "cta_label": "Découvrir les huit actes →",
            "cta_href":  "menu",
        },

        "produttori": {
            "label":   "Depuis les producteurs",
            "heading": "Quatre mains, <em>une seule table.</em>",
            "intro":
                "Chaque matin, une partie de la salle entre par la porte de la "
                "cuisine. Voici les visages. Leurs terres, leurs méthodes — "
                "à retrouver sur la carte, ligne par ligne.",
            "items": [
                {"portrait":
                    "https://images.unsplash.com/photo-1552058544-f2b08422138a"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Roberto Tarbouriech",
                 "role": "Huîtres & coquillages",
                 "area": "Sète · Étang de Thau",
                 "blurb":
                    "Les huîtres Spéciales viennent de l'Étang de Thau. "
                    "Livraison lundi, servies mardi soir."},
                {"portrait":
                    "https://images.unsplash.com/photo-1568213816046-0ee1c42bd559"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Famille Brezza",
                 "role": "Barolo & Langhe",
                 "area": "Barolo · Piémont",
                 "blurb":
                    "Vignes de Cannubi et Sarmassa, travaillées sans œnologue "
                    "extérieur. Une carte verticale depuis 2008."},
                {"portrait":
                    "https://images.unsplash.com/photo-1543418219-44e30b057fea"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Aloïs Lageder",
                 "role": "Biodynamie de montagne",
                 "area": "Pacherhof · Tyrol du Sud",
                 "blurb":
                    "Vins blancs livrés directement depuis le val d'Isarco. "
                    "Ni filtration, ni collage."},
                {"portrait":
                    "https://images.unsplash.com/photo-1414235077428-338989a2e8c0"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Gianfranco Pieropan",
                 "role": "Soave Classico",
                 "area": "Soave · Vénétie",
                 "blurb":
                    "Calvarino et La Rocca, Soave Classico en pureté. Ils "
                    "accompagnent le second acte depuis toujours."},
            ],
        },
        "private_dining": {
            "label":   "Événements privés",
            "heading": "Chef's Table & <em>privatisations.</em>",
            "intro":
                "Pour douze couverts en salle privée ou pour toute la soirée "
                "— vingt-huit couverts, un menu unique, cuisine à vue.",
            "experiences": [
                {"icon": "fork", "title": "Chef's Table",
                 "meta":  "12 couverts · dès 190 € / personne",
                 "desc":
                    "Une seule table face à la cuisine. Menu en huit actes, "
                    "narré directement par le chef. Mardis uniquement."},
                {"icon": "door", "title": "Privatisation du soir",
                 "meta":  "28 couverts · dès 5 800 € / soirée",
                 "desc":
                    "Le restaurant entier, un menu dédié, les fleurs, un "
                    "maître d'hôtel personnel. Deux semaines de préavis; "
                    "vendredis déclinés."},
                {"icon": "wine", "title": "Dégustation de cave",
                 "meta":  "6 couverts · jeudis uniquement",
                 "desc":
                    "Une soirée par mois avec le sommelier sur six bouteilles "
                    "choisies parmi les producteurs de la carte. Liste "
                    "d'attente uniquement."},
            ],
            "cta_label": "Écrire au concierge",
            "cta_href":  "prenota",
        },
        "wine_program": {
            "label":   "La cave",
            "heading": "Quatre cents étiquettes, <em>trois accords par soir.</em>",
            "intro":
                "La carte suit le menu : chaque acte a son accord et deux "
                "alternatives — classique, contemporain, sans alcool.",
            "sommelier": {
                "name": "Greta Vallesi",
                "role": "Maître & sommelière",
                "bio":
                    "Quinze ans entre Bourgogne, Langhe et Champagne. La carte "
                    "est signée par elle, l'accord est toujours proposé à "
                    "table, jamais imposé.",
            },
            "pairings": [
                ("01", "Accord classique",
                 "Champagne blanc de blancs, Soave Classico, Barolo riserva, Moscato.",
                 "+ 110 €"),
                ("02", "Accord contemporain",
                 "Col Fondo vénitien, Erbaluce long, Ribolla en amphore, "
                 "Timorasso en verticale.",
                 "+ 130 €"),
                ("03", "Accord sans alcool",
                 "Kombucha artisanal, thés glacés en infusion lente, jus de "
                 "raisin en fermentation naturelle.",
                 "+ 60 €"),
            ],
            "cellar_facts": [
                ("420", "étiquettes à la carte"),
                ("18", "régions viticoles"),
                ("2005", "verticale la plus ancienne (Brunello)"),
            ],
        },
    },

    "filosofia": {
        "eyebrow":  "Philosophie",
        "headline": "Un menu, une salle, <em>une seule soirée.</em>",
        "intro":
            "Osteria Moderna est née en 2014 de l'idée qu'un restaurant "
            "n'est pas un service, mais un théâtre. Quatorze couverts par "
            "service, deux services par semaine, un cuisinier au piano, "
            "un maître en salle.",

        "history": [
            ("2014",
             "Lorenzo Fioravanti ouvre Osteria Moderna dans trois pièces "
             "d'un palais brérien du XVIIIᵉ siècle. Seize couverts, une "
             "brigade unique, un menu qui change tous les vendredis."),
            ("2016",
             "Greta Vallesi rejoint la maison comme maître et responsable "
             "de cave. La carte des vins passe de 80 à 320 références, "
             "avec un accent sur les petits vignerons du Nord-Est italien "
             "et de la Bourgogne mineure."),
            ("2018",
             "Étoile Michelin. Le restaurant réduit alors à quatorze "
             "couverts par service et impose le menu dégustation en huit "
             "actes comme unique proposition."),
            ("2021",
             "Ouverture de la cuisine sur la salle. Le chef cuisine face "
             "aux convives pour toute la durée du service. Aucun mur entre "
             "piano et table."),
            ("2024",
             "Parution de 'Huit actes', aux éditions Giunti, consacré aux "
             "quarante premières soirées du menu d'hiver 2023/24."),
        ],

        "filosofia_image": _FILOSOFIA_IMG,
        "filosofia_image_caption": "La cuisine · Lorenzo Fioravanti au travail",

        "method_title": "Méthode",
        "method_paragraphs": [
            "Le menu dégustation se réécrit toutes les deux semaines selon "
            "le marché du matin. Les matières premières arrivent d'un "
            "réseau de trente-deux petits producteurs — pêcheurs ligures, "
            "éleveurs piémontais, maraîchers de Lodi — dont Lorenzo connaît "
            "personnellement le prénom, l'adresse et le numéro de portable.",
            "Chaque acte est pensé comme un mouvement de symphonie : il "
            "y a un prélude, un crescendo en milieu de service, une pause "
            "lyrique, un final qui revient au début pour fermer le cercle. "
            "La séquence est réécrite intégralement toutes les deux "
            "semaines — nous ne répétons jamais les mêmes transitions.",
            "La carte des vins est signée Greta Vallesi : 320 références, "
            "dont deux tiers issues de petits vignerons européens. L'accord "
            "est facultatif (90 € pour le parcours complet) mais — "
            "disons-le franchement — c'est la moitié du travail accompli.",
        ],

        "values_label": "Ce que nous promettons",
        "values_heading": "Quatre promesses qui <em>ne changent jamais</em>.",
        "values": [
            ("Temps",        "Trois heures et demie de service. Jamais plus, jamais moins."),
            ("Saison",       "Rien en salle qui ne soit de saison locale."),
            ("Transparence", "Nous connaissons chaque producteur à la carte par son prénom."),
            ("Discrétion",   "Ni photos du chef, ni réseaux sociaux : en salle, on dîne."),
        ],

        "cta_heading": "Vous voulez voir le menu <em>de cette semaine ?</em>",
        "cta_menu": "Les huit actes de l'automne '26",
        "cta_prenota": "Réserver la soirée",
    },

    "menu": {
        "eyebrow":  "Le menu",
        "headline": "Huit actes — <em>automne '26</em>",
        "intro":
            "Le menu est réécrit intégralement toutes les deux semaines. "
            "Ci-dessous le programme en vigueur du 6 au 19 octobre 2026. "
            "Deux services par semaine, du mercredi au samedi, un seul "
            "seating à 20h00.",
        "courses_label": "Huit actes · service à partir de 20h00",

        "courses": [
            ("I",    "Huître & concombre",
             "Huître Tarbouriech de Sète, gel de concombre bio du lac de "
             "Côme, oseille sauvage, perles de yuzu en suspension dans "
             "l'huile d'olive taggiasca.",
             "Champagne Anselme Selosse · Initial · Avize"),
            ("II",   "Risotto à la moelle",
             "Carnaroli Riserva San Massimo 2023, moelle rôtie sur braise "
             "de sarment, extrait de persil frisé, poudre de café mono-"
             "origine éthiopien.",
             "Soave Classico Pieropan · La Rocca '21"),
            ("III",  "Coquille Saint-Jacques",
             "Saint-Jacques de Galice pêchée en apnée, beurre noisette "
             "au romarin, câpres de Pantelleria au sel, gel de citron "
             "d'Amalfi.",
             "Riesling Pacherhof · Kerner Alto Adige '22"),
            ("IV",   "Pâtes maison",
             "Cappelletti tirés à la main, farce de chapon de Bresse et "
             "truffe noire du Val Trebbia, bouillon de sanglier réduit "
             "sept fois.",
             "Lambrusco di Sorbara Rinaldini · Rosé Brut"),
            ("V",    "Pigeon de Bresse",
             "Poitrine rosée laquée au miel de châtaigne, cuisse confite "
             "aux figues noires de Caprino, réduction de Barolo, poudre de "
             "cardamome verte du Guatemala.",
             "Barolo Riserva Cannubi · Brezza '17"),
            ("VI",   "Pré-dessert",
             "Sorbet au céleri-rave, oxalis de notre potager, granité de "
             "prune de Dro, cristaux de sel rose.",
             "—"),
            ("VII",  "Chocolat 80 %",
             "Chocolat Domori Criollo 80 %, huile d'olive extra-vierge de "
             "Tuscia, sel de Maldon fumé au bois de pommier, poudre de "
             "réglisse calabraise.",
             "Marsala Vintage Marco De Bartoli · 1999"),
            ("VIII", "Mignardises",
             "Trois petites pâtisseries d'auteur : l'une au chocolat, "
             "l'une aux agrumes, l'une au miel.",
             "Café mono-origine Éthiopie Yirgacheffe"),
        ],

        "wine_intro_title": "Carte des vins",
        "wine_intro":
            "320 références, dont deux tiers issues de petits vignerons "
            "européens. Greta Vallesi est en salle chaque soir pour "
            "discuter chaque choix — mais elle est aussi disponible pour "
            "construire un accord sur mesure, hors menu standard.",

        "wine_highlights": [
            ("Champagne", "62 références · 24 champagnes de vignerons"),
            ("Bourgogne", "48 vignerons · focus sur la Côte de Beaune et le Mâconnais"),
            ("Italie",    "112 références · Nord-Est, Haut Piémont et Sicile volcanique"),
            ("Vins mutés","18 références · xérès, marsala, madère, tokaji"),
        ],

        "footer":
            "Menu dégustation complet : 180 € par personne. Accord vins "
            "facultatif : 90 € par personne. Formule magnum (six verres "
            "magnum, format partagé) : + 140 €. Toute intolérance ou "
            "allergie est à signaler au moment de la réservation.",
    },

    "atmosfera": {
        "eyebrow":  "Les salles",
        "headline": "Trois pièces, <em>quatorze chaises,</em> aucun mur.",
        "intro":
            "Osteria Moderna occupe trois pièces d'un palais brérien du "
            "XVIIIᵉ siècle, Via San Marco. Aucun mur entre cuisine et "
            "salle. Aucune image sur les réseaux : pour photographier "
            "le plat, ici, on le regarde calmement, assis.",

        "rooms": [
            ("La salle principale",
             "Le cœur du restaurant. Neuf couverts, trois tables, une "
             "baie vitrée donnant sur la cour intérieure du palais."),
            ("Le pass ouvert",
             "Cinq couverts au comptoir, face aux pianos. Le chef "
             "cuisine en silence pendant tout le service."),
            ("La cave",
             "Une salle hypogée abritant 320 références. Visites "
             "privées sur réservation, en fin de dîner, accompagnées "
             "par Greta Vallesi."),
            ("La cour",
             "De mai à septembre, deux tables en plein air sous la "
             "glycine de la cour intérieure. Réservable uniquement "
             "pour un dîner complet."),
        ],

        "captions": [
            "Le pass ouvert pendant le service du vendredi soir.",
            "Le premier acte du menu automne '26 : huître et concombre.",
            "Greta Vallesi en cave, parmi les 320 références.",
            "La cour intérieure du palais brérien du XVIIIᵉ siècle.",
            "Lorenzo Fioravanti pendant le service.",
            "La salle principale à la fin de la mise en place.",
        ],

        "cta_quote": "« Pour photographier le plat, ici, on le regarde calmement, assis. »",
        "cta_desc": "Quatorze couverts par service. Uniquement sur réservation. Dîner uniquement. Mer – Sam.",
        "cta_primary": "Réserver la soirée",
        "cta_secondary": "Voir le menu",
    },

    "diario": {
        "eyebrow":  "Le journal de salle",
        "headline": "Notes de travail, <em>de saison</em>, de salle.",
        "intro":
            "Brefs billets de Lorenzo Fioravanti et Greta Vallesi sur "
            "le menu en cours, sur les producteurs, sur les soirées "
            "mémorables et sur ce qui change en cuisine de semaine "
            "en semaine.",
        "read_article": "Lire l'article",
        "min_label": "min",
        "min_read_label": "min de lecture",
        "crumb_label": "Journal",
        "back_link": "← Retour au journal",
        "footer_label": "Osteria Moderna · Le journal de salle",
        "empty_body": [
            "Article en cours de relecture éditoriale. La version "
            "intégrale sera publiée très prochainement, rédigée "
            "personnellement par le chef ou le maître.",
            "Ce marque-page décrit la voix du Journal de Salle : "
            "courts billets de travail, réflexions sur les producteurs, "
            "récits de soirées mémorables. Jamais plus de deux mille "
            "mots, jamais moins de cinq cents.",
        ],
    },

    "posts": [
        {
            "slug":     "menu-autunno-26",
            "kicker":   "Menu en cours",
            "title":    "Les huit idées du menu automne '26",
            "date":     "5 octobre 2026",
            "read_min": 5,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "Le nouveau menu est à la carte depuis lundi soir. "
                "Huit plats — quatre nouvelles compositions et quatre "
                "variations sur des thèmes laissés à l'archive depuis 2022.",
            "body": [
                ("p", "Construire un menu dégustation est moins une question "
                      "de recettes qu'une question de transitions. Comment "
                      "on passe du salé au sucré. Comment on revient en "
                      "arrière en milieu de service. Comment on introduit "
                      "le quatrième plat sans casser le rythme. Pour le menu "
                      "automne '26, nous avons travaillé deux semaines sur "
                      "les seules pauses."),
                ("h2", "Les quatre idées inédites"),
                ("p", "Le premier acte, huître et concombre, est une "
                      "relecture d'un plat que mon maître Pierre Brutscher "
                      "faisait au Mirazur. Je le portais en tête depuis 2007, "
                      "du temps où j'étais son apprenti. Pendant quinze ans "
                      "je n'en ai pas trouvé la fin. Je l'ai trouvée l'été "
                      "dernier, sur un banc de Sète, en regardant Tarbouriech "
                      "ramasser ses huîtres à l'aube."),
                ("p", "Le quatrième acte — les pâtes maison — marque la "
                      "première fois en trois ans que nous glissons des "
                      "pâtes dans le menu dégustation. La farce de chapon "
                      "et truffe noire est un hommage à une recette du Val "
                      "Trebbia que ma grand-mère maternelle préparait le "
                      "jour de Noël."),
                ("h2", "Les quatre variations"),
                ("p", "Le pigeon de Bresse revient après deux saisons. "
                      "C'est mon plat-signature, celui que je préfère parmi "
                      "tous ceux que j'ai construits depuis l'ouverture. "
                      "Cette fois, je l'accompagne d'une réduction de Barolo "
                      "Cannubi '17 — un vin que Greta a trouvé après six "
                      "mois d'appels chez Brezza."),
                ("blockquote",
                 "Un menu dégustation n'est pas une suite de plats. C'est "
                 "un chemin que le convive parcourt avec le cuisinier, "
                 "et que le cuisinier refait chaque soir avec le convive."),
                ("p", "Merci à Greta pour l'accord, à la brigade de salle "
                      "pour la patience avec laquelle elle a appris huit "
                      "nouvelles descriptions en deux semaines, et à tous "
                      "les producteurs qui nous ont permis de construire "
                      "ce menu : Tarbouriech, San Massimo, Pacherhof, les "
                      "frères Brezza, Domori, Marco De Bartoli."),
            ],
        },
        {
            "slug":     "barolo-cannubi-17-brezza",
            "kicker":   "Carte des vins",
            "title":    "Six mois d'appels pour un Barolo",
            "date":     "20 septembre 2026",
            "read_min": 4,
            "author":   "Greta Vallesi",
            "lede":
                "L'histoire de l'arrivée à la carte du Barolo Cannubi '17 "
                "de Brezza, et pourquoi nous le voulions à tout prix pour "
                "le cinquième acte du menu d'automne.",
        },
        {
            "slug":     "cucina-a-vista",
            "kicker":   "La salle",
            "title":    "Cinq ans de pass ouvert : ce que nous avons appris",
            "date":     "29 août 2026",
            "read_min": 6,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "Ouvrir la cuisine au public a changé la façon dont on "
                "travaille en brigade. Cela a aussi changé la façon dont "
                "les convives dînent. Brève réflexion, cinq ans après "
                "l'ouverture du comptoir.",
        },
        {
            "slug":     "ostriche-tarbouriech",
            "kicker":   "Les producteurs",
            "title":    "Tarbouriech : l'ostréiculteur qui marée toutes les douze heures",
            "date":     "11 août 2026",
            "read_min": 5,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "À Sète, en Languedoc, Florent Tarbouriech a inventé un "
                "mode d'élevage qui reproduit la marée atlantique en "
                "Méditerranée. Le résultat est l'huître de notre premier acte.",
        },
        {
            "slug":     "libro-otto-atti",
            "kicker":   "Édition",
            "title":    "'Huit actes' paraît chez Giunti",
            "date":     "1 juillet 2026",
            "read_min": 3,
            "author":   "Greta Vallesi",
            "lede":
                "Le 4 juillet, Giunti publie 'Huit actes — quarante soirées "
                "du menu d'hiver d'Osteria Moderna'. Lorenzo le présentera "
                "le 12 juillet à la Triennale de Milan.",
        },
    ],

    "prenota": {
        "eyebrow":  "Réservation",
        "headline": "Un dîner <em>ne se réserve pas</em> : il se convient.",
        "intro":
            "Chez Osteria Moderna il n'existe pas de calendrier en ligne. "
            "Les réservations passent par la concierge personnelle du "
            "restaurant, Greta Vallesi, qui répond par e-mail dans la journée.",

        "process_label": "Comment ça marche",
        "process_heading": "Quatre étapes, <em>quatre jours à l'avance</em>.",
        "hours_label": "Services de la semaine",
        "hours_heading": "Quatre soirs, <em>un seul seating</em>.",
        "private_heading": "Dîners privés",
        "form_submit": "Envoyer une note au concierge",

        "process": [
            ("01", "Écrivez à Greta",
             "Quelques lignes suffisent : date préférée, nombre de convives, "
             "intolérances éventuelles, occasion. Greta lit chaque demande "
             "personnellement."),
            ("02", "Proposition de soirée",
             "Dans la journée Greta vous propose une ou deux dates compatibles "
             "(les services sont du mercredi au samedi) et confirme le menu "
             "en vigueur."),
            ("03", "Confirmation & acompte",
             "Pour confirmer la réservation, un petit acompte de 80 € par "
             "personne est demandé ; il sera déduit de l'addition finale."),
            ("04", "Note de soirée",
             "La veille, vous recevrez un bref e-mail avec le dress code, "
             "le menu en cours et une note sur l'accord vins facultatif."),
        ],

        "concierge": {
            "name":  "Greta Vallesi",
            "role":  "Maître & responsable de cave",
            "email": "greta@osteriamoderna.it",
            "phone": "+39 02 3611 9920",
            "bio":
                "Romaine d'origine, milanaise d'adoption. Quinze ans en "
                "salle, dont neuf chez Osteria Moderna. Sommelière AIS "
                "depuis 2014. En salle tous les soirs de 18h30 à 23h30.",
        },

        "hours": [
            ("Mercredi",  "20h00 – 23h30",  "1 service · seating unique"),
            ("Jeudi",     "20h00 – 23h30",  "1 service · seating unique"),
            ("Vendredi",  "20h00 – 23h30",  "1 service · seating unique"),
            ("Samedi",    "20h00 – 23h30",  "1 service · seating unique"),
            ("Dimanche",  "Fermé",          "—"),
            ("Lun & Mar", "Fermé",          "Repos hebdomadaire de la brigade"),
        ],

        "private_title": "Dîners privés & événements",
        "private_intro":
            "Pour les dîners privés (anniversaires, événements "
            "d'entreprise, présentations de produit) il est possible de "
            "réserver l'intégralité de la salle les jours de fermeture. "
            "Forfaits sur mesure, convenus personnellement avec le chef.",

        "form_title":  "Écrivez au concierge",
        "form_fields": [
            ("Nom et prénom",       "Mario Rossi",                             "text"),
            ("E-mail",              "mario@email.fr",                          "email"),
            ("Téléphone",           "+33 6 ...",                               "tel"),
            ("Nombre de convives",  "2",                                       "number"),
            ("Date préférée",       "ven. 16 octobre",                         "text"),
            ("Occasion",            "",                                        "select"),
            ("Allergies ou intolérances", "Allergies, intolérances ou demandes particulières", "text"),
            ("Note au concierge",   "Greta lit chaque demande personnellement. Quelques lignes suffisent.", "textarea"),
        ],
        "occasion_options": ["Dîner romantique", "Anniversaire", "Professionnel", "Sans occasion"],
        "consent":
            "Je consens au traitement de mes données personnelles "
            "conformément à la notice de confidentialité, au titre du "
            "Règlement UE 679/2016.",

        "address_block": [
            ("Adresse",    "Via San Marco 17 · 20121 Milan"),
            ("Transports", "Lanza M2 · 4 minutes à pied · Brera"),
            ("Parking",    "APCOA Garibaldi 36 · navette gratuite"),
        ],
    },
}


# ===========================================================================
# SPANISH — Peninsular register, formal but warm
# "Menú degustación en ocho actos", "un solo pase".
# ===========================================================================

GUSTO_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "Inicio",       "kind": "home"},
        {"slug": "filosofia", "label": "Filosofía",    "kind": "about"},
        {"slug": "menu",      "label": "Menú",         "kind": "menu"},
        {"slug": "atmosfera", "label": "Las salas",    "kind": "gallery"},
        {"slug": "diario",    "label": "Diario",       "kind": "blog_list"},
        {"slug": "prenota",   "label": "Reservar",     "kind": "reservations"},
    ],

    "site": {
        "logo_initial": "OM",
        "logo_word":    "Osteria Moderna",
        "tag":          "Mesa única · Milán, Brera · 14 comensales",
        "phone":        "+39 02 3611 9920",
        "email":        "concierge@osteriamoderna.it",
        "address":      "Via San Marco 17 · 20121 Milán",
        "hours_compact":"Mié – Sáb · solo cenas",
        "star_line":    "★ Una estrella Michelin · desde 2018",
        "footer_intro":
            "Una estrella Michelin desde 2018. Catorce comensales, dos "
            "servicios por semana, un menú degustación de ocho actos que "
            "se reescribe cada dos semanas.",
        "footer_hours_1": "Mié – Sáb · 20:00 h",
        "footer_hours_2": "Dom & Lun · cerrado",
        "copyright": "© 2026 Osteria Moderna · IVA 09456112094",
    },

    "home": {
        "eyebrow":  "Mesa única · Milán, Brera · 14 comensales",
        "headline": "Una velada en <em>ocho actos.</em>",
        "intro":
            "Un menú degustación que se reescribe cada dos semanas según "
            "el mercado de la mañana. Solo cenas. Solo con reserva. "
            "Para catorce comensales.",
        "primary_cta":   "Reservar la velada",
        "primary_href":  "prenota",
        "secondary_cta": "Conoce al chef",
        "secondary_href":"filosofia",

        "chef_label":    "El chef",
        "star_tag":      "★ Acto V · Chocolate 80 %",
        "photo_label":   "Fotografía",
        "cuisine_label": "Cocina",

        "facts": [
            ("14",   "comensales por servicio"),
            ("8",    "actos en el menú degustación"),
            ("180€", "menú completo · maridaje + 90 €"),
        ],

        "manifesto_drop_cap": "U",
        "manifesto":
            "n menú que se reescribe cada dos semanas. Una sola sala de "
            "catorce comensales. Una cocina vista que trabaja en silencio "
            "durante cuatro horas seguidas. En Osteria Moderna no se pide "
            "a la carta: se entra en un relato con principio, clímax y cierre.",

        "signature_courses": [
            ("I",   "Ostra y pepino",          "acedera, perlas de yuzu",                    "Champagne Selosse"),
            ("II",  "Risotto al tuétano",      "extracto de perejil, café",                  "Soave Pieropan '21"),
            ("III", "Vieira asada",            "mantequilla avellana, alcaparras de Pantelleria","Riesling Pacherhof"),
            ("IV",  "Pichón de Bresse",        "higos negros, cardamomo verde",              "Barolo Cannubi '17"),
            ("V",   "Chocolate 80 %",          "aceite de oliva, sal Maldon",                "Marsala Vintage '99"),
        ],

        "courses_label": "Cinco actos del menú en curso · otoño '26",
        "courses_footline": "180 € por persona · maridaje + 90 €",
        "courses_full_cta": "Los ocho actos al completo",
        "chef_link_filosofia": "La filosofía",
        "chef_link_diario": "El diario",

        "chef": {
            "name":  "Lorenzo Fioravanti",
            "role":  "Chef propietario · 1 estrella Michelin",
            "bio":
                "Romano, nacido en 1981. Formado junto a Bottura, Cracco "
                "y Brutscher en el Mirazur. Abre Osteria Moderna en 2014 "
                "en tres estancias de un palacio bréreo del siglo XVIII. "
                "Primera estrella Michelin en 2018, revalidada cada año.",
        },

        "press_label": "Publicados en",
        "press": ["GUIDA MICHELIN", "GAMBERO ROSSO", "IDENTITÀ GOLOSE",
                  "CORRIERE LIVING", "VOGUE FOOD"],

        "ingredienti": {
            "label": "Los productores",
            "heading": "Treinta y dos productores, <em>a todos por su nombre.</em>",
            "text":
                "La red de Osteria Moderna cuenta con treinta y dos "
                "pequeños productores —pescadores ligures, ganaderos "
                "piamonteses, hortelanos de Lodi— a los que Lorenzo "
                "conoce personalmente por su nombre, dirección y teléfono "
                "móvil. Ni un intermediario, ni un catálogo, ni una red "
                "de distribución.",
            "image": _INGREDIENTI_IMG,
            "image_caption": "Producto del menú otoño '26 · mercado matinal",
        },

        "atmosphere_teaser": {
            "label": "Las salas",
            "images": [
                (_ATMO_SALA,    "La sala principal"),
                (_ATMO_CUCINA,  "La cocina vista"),
                (_ATMO_CORTILE, "El patio bajo la glicinia"),
                (_ATMO_MISE,    "Mise en place del viernes"),
            ],
            "link_label": "Descubre las salas",
            "link_href":  "atmosfera",
        },

        "riconoscimenti": {
            "label": "Reconocimientos",
            "items": [
                ("★", "Estrella Michelin", "Desde 2018 — revalidada cada año"),
                ("GR", "Gambero Rosso", "Tres Tenedores · Premio especial cocina de autor 2025"),
                ("IG", "Identità Golose", "Plato del Año 2024 — Pichón de Bresse"),
                ("50B", "50 Best Discovery", "Selección Italia 2026"),
            ],
        },

        "cta_heading": "Catorce comensales, <em>dos servicios por semana.</em>",
        "cta_primary": "Reservar la velada",
        "cta_secondary": "Ver el menú completo",

        "stagione": {
            "label": "Ahora en carta",
            "title": "Menú otoño '26",
            "subtitle": "Ocho actos · del 6 al 19 de octubre",
            "text":
                "El nuevo menú está en carta desde el lunes. Ocho platos, "
                "cuatro composiciones nuevas y cuatro variaciones sobre "
                "temas que habíamos dejado en el archivo desde 2022. "
                "Reserva obligatoria.",
            "cta_label": "Descubre los ocho actos →",
            "cta_href":  "menu",
        },

        "produttori": {
            "label":   "De los productores",
            "heading": "Cuatro manos, <em>una sola mesa.</em>",
            "intro":
                "Cada mañana una parte del comedor entra por la puerta de la "
                "cocina. Estos son los rostros. Sus tierras, sus métodos — "
                "los encontrará en carta, línea a línea.",
            "items": [
                {"portrait":
                    "https://images.unsplash.com/photo-1552058544-f2b08422138a"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Roberto Tarbouriech",
                 "role": "Ostras y mariscos",
                 "area": "Sète · Étang de Thau",
                 "blurb":
                    "Las ostras Spéciales llegan de la laguna del Étang de "
                    "Thau. Entrega el lunes, servidas el martes por la noche."},
                {"portrait":
                    "https://images.unsplash.com/photo-1568213816046-0ee1c42bd559"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Familia Brezza",
                 "role": "Barolo y Langhe",
                 "area": "Barolo · Piamonte",
                 "blurb":
                    "Viñedos en Cannubi y Sarmassa, trabajados sin enólogo "
                    "externo. Una carta vertical desde 2008."},
                {"portrait":
                    "https://images.unsplash.com/photo-1543418219-44e30b057fea"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Aloïs Lageder",
                 "role": "Biodinámica de montaña",
                 "area": "Pacherhof · Alto Adigio",
                 "blurb":
                    "Vinos blancos que llegan directamente del valle de "
                    "Isarco. Sin filtración, sin clarificación."},
                {"portrait":
                    "https://images.unsplash.com/photo-1414235077428-338989a2e8c0"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Gianfranco Pieropan",
                 "role": "Soave Classico",
                 "area": "Soave · Véneto",
                 "blurb":
                    "Calvarino y La Rocca, Soave Classico en pureza. Han "
                    "acompañado el segundo acto desde siempre."},
            ],
        },
        "private_dining": {
            "label":   "Eventos privados",
            "heading": "Chef's Table y <em>privatizaciones.</em>",
            "intro":
                "Para doce comensales en sala privada o para la velada entera "
                "— veintiocho comensales, un solo menú, cocina a la vista.",
            "experiences": [
                {"icon": "fork", "title": "Chef's Table",
                 "meta":  "12 comensales · desde 190 € / persona",
                 "desc":
                    "Mesa única frente a la cocina. Menú de ocho actos narrado "
                    "directamente por el chef. Solo los martes."},
                {"icon": "door", "title": "Privatización nocturna",
                 "meta":  "28 comensales · desde 5.800 € / velada",
                 "desc":
                    "Todo el restaurante, menú dedicado, flores, maître "
                    "personal. Dos semanas de antelación, declinamos los "
                    "viernes."},
                {"icon": "wine", "title": "Cata de bodega",
                 "meta":  "6 comensales · solo los jueves",
                 "desc":
                    "Una velada al mes con la sumiller sobre seis botellas "
                    "escogidas entre los productores de la carta. Solo en "
                    "lista de espera."},
            ],
            "cta_label": "Escriba al concierge",
            "cta_href":  "prenota",
        },
        "wine_program": {
            "label":   "La bodega",
            "heading": "Cuatrocientas etiquetas, <em>tres maridajes por noche.</em>",
            "intro":
                "La carta sigue al menú: cada acto tiene su maridaje y dos "
                "alternativas — clásica, contemporánea, sin alcohol.",
            "sommelier": {
                "name": "Greta Vallesi",
                "role": "Maître & sumiller",
                "bio":
                    "Quince años entre Borgoña, Langhe y Champaña. La carta "
                    "está firmada por ella, el maridaje se propone siempre "
                    "en mesa, nunca se impone.",
            },
            "pairings": [
                ("01", "Maridaje clásico",
                 "Champagne blanc de blancs, Soave Classico, Barolo riserva, Moscato.",
                 "+ 110 €"),
                ("02", "Maridaje contemporáneo",
                 "Col Fondo veneciano, Erbaluce largo, Ribolla en ánfora, "
                 "Timorasso en vertical.",
                 "+ 130 €"),
                ("03", "Maridaje sin alcohol",
                 "Kombucha artesanal, tés fríos en infusión lenta, zumo de "
                 "uva fermentado naturalmente.",
                 "+ 60 €"),
            ],
            "cellar_facts": [
                ("420", "etiquetas en carta"),
                ("18", "regiones vinícolas"),
                ("2005", "vertical más antigua (Brunello)"),
            ],
        },
    },

    "filosofia": {
        "eyebrow":  "Filosofía",
        "headline": "Un menú, una sala, <em>una sola velada.</em>",
        "intro":
            "Osteria Moderna nace en 2014 de la idea de que un restaurante "
            "no es un servicio, sino un teatro. Catorce comensales por "
            "servicio, dos servicios por semana, un cocinero al pase y "
            "un maître en sala.",

        "history": [
            ("2014",
             "Lorenzo Fioravanti abre Osteria Moderna en tres estancias "
             "de un palacio bréreo del siglo XVIII. Dieciséis comensales, "
             "una sola brigada, un menú que cambia cada viernes."),
            ("2016",
             "Greta Vallesi se incorpora como maître y responsable de "
             "bodega. La carta de vinos pasa de 80 a 320 referencias, "
             "con un foco en pequeños viticultores del noreste italiano "
             "y de la Borgoña menor."),
            ("2018",
             "Estrella Michelin. Desde ese momento el restaurante reduce "
             "a catorce comensales por servicio y establece el menú "
             "degustación de ocho actos como única propuesta."),
            ("2021",
             "Apertura de la cocina a la sala. El chef cocina frente a "
             "los comensales durante todo el servicio. Ni una pared "
             "entre pase y mesa."),
            ("2024",
             "Publicación de 'Ocho actos', editorial Giunti, dedicado "
             "a las primeras cuarenta veladas del menú de invierno 2023/24."),
        ],

        "filosofia_image": _FILOSOFIA_IMG,
        "filosofia_image_caption": "La cocina · Lorenzo Fioravanti trabajando",

        "method_title": "Método",
        "method_paragraphs": [
            "El menú degustación se reescribe cada dos semanas siguiendo "
            "el mercado matinal. Las materias primas llegan de una red "
            "de treinta y dos pequeños productores —pescadores ligures, "
            "ganaderos piamonteses, hortelanos de Lodi— a los que Lorenzo "
            "conoce personalmente por su nombre, dirección y teléfono.",
            "Cada acto está pensado como un movimiento de una sinfonía: "
            "hay un preludio, un crescendo a mitad de servicio, una "
            "pausa lírica, un final que vuelve al principio para cerrar "
            "el círculo. La secuencia se reescribe por completo cada dos "
            "semanas: nunca se repiten las mismas transiciones.",
            "La carta de vinos está firmada por Greta Vallesi: 320 "
            "referencias, dos tercios de ellas de pequeños viticultores "
            "europeos. El maridaje es opcional (90 € el recorrido completo), "
            "pero —dicho sin medias tintas— representa la mitad del "
            "trabajo que hacemos.",
        ],

        "values_label": "Lo que prometemos",
        "values_heading": "Cuatro promesas que <em>no cambian jamás</em>.",
        "values": [
            ("Tiempo",       "Tres horas y media de servicio. Ni más, ni menos."),
            ("Temporada",    "Nada en la mesa que no sea de temporada local."),
            ("Transparencia","Conocemos por su nombre a cada productor de la carta."),
            ("Discreción",   "Ni fotos al chef, ni redes: en la sala se cena."),
        ],

        "cta_heading": "¿Quieres ver el menú <em>de esta semana?</em>",
        "cta_menu": "Los ocho actos del otoño '26",
        "cta_prenota": "Reservar la velada",
    },

    "menu": {
        "eyebrow":  "El menú",
        "headline": "Ocho actos — <em>otoño '26</em>",
        "intro":
            "El menú se reescribe íntegramente cada dos semanas. Lo que "
            "sigue es el programa vigente del 6 al 19 de octubre de 2026. "
            "Dos servicios por semana, de miércoles a sábado, un único "
            "pase a las 20:00 h.",
        "courses_label": "Ocho actos · servicio desde las 20:00 h",

        "courses": [
            ("I",    "Ostra y pepino",
             "Ostra Tarbouriech de Sète, gel de pepino ecológico del lago "
             "de Como, acedera silvestre, perlas de yuzu suspendidas en "
             "aceite de oliva taggiasca.",
             "Champagne Anselme Selosse · Initial · Avize"),
            ("II",   "Risotto al tuétano",
             "Carnaroli Riserva San Massimo 2023, tuétano asado sobre "
             "brasas de sarmiento, extracto de perejil rizado, polvo de "
             "café monoorigen etíope.",
             "Soave Classico Pieropan · La Rocca '21"),
            ("III",  "Vieira asada",
             "Vieira de Galicia de pesca en apnea, mantequilla de avellana "
             "al romero, alcaparras de Pantelleria en sal, gel de limón "
             "de Amalfi.",
             "Riesling Pacherhof · Kerner Alto Adige '22"),
            ("IV",   "Pasta de la casa",
             "Cappelletti estirados a mano, relleno de capón de Bresse "
             "y trufa negra del Val Trebbia, caldo de jabalí reducido "
             "siete veces.",
             "Lambrusco di Sorbara Rinaldini · Rosé Brut"),
            ("V",    "Pichón de Bresse",
             "Pechuga al rojo lacada con miel de castaño, pata confitada "
             "con higos negros de Caprino, reducción de Barolo, polvo de "
             "cardamomo verde guatemalteco.",
             "Barolo Riserva Cannubi · Brezza '17"),
            ("VI",   "Pre-postre",
             "Sorbete de apionabo, oxalis de nuestro huerto, granizado "
             "de ciruela de Dro, cristales de sal rosa.",
             "—"),
            ("VII",  "Chocolate 80 %",
             "Chocolate Domori Criollo 80 %, aceite de oliva virgen extra "
             "de la Tuscia, sal Maldon ahumada con leña de manzano, polvo "
             "de regaliz calabrés.",
             "Marsala Vintage Marco De Bartoli · 1999"),
            ("VIII", "Mignardises",
             "Tres pequeñas pastelerías de autor: una al chocolate, "
             "una a los cítricos, una a la miel.",
             "Café monoorigen Etiopía Yirgacheffe"),
        ],

        "wine_intro_title": "Carta de vinos",
        "wine_intro":
            "320 referencias, dos tercios de ellas de pequeños viticultores "
            "europeos. Greta Vallesi está en sala cada noche para comentar "
            "cada elección, pero también puede armar un maridaje a medida "
            "fuera del recorrido estándar.",

        "wine_highlights": [
            ("Champagne",   "62 referencias · 24 grower champagne"),
            ("Borgoña",     "48 viticultores · foco en la Côte de Beaune y el Mâconnais"),
            ("Italia",      "112 referencias · Noreste, Alto Piamonte y Sicilia volcánica"),
            ("Vinos dulces","18 referencias · jerez, marsala, madeira, tokaji"),
        ],

        "footer":
            "Menú degustación completo: 180 € por persona. Maridaje "
            "opcional: 90 € por persona. Paquete magnum (seis copas "
            "magnum, formato compartido): + 140 €. Toda intolerancia "
            "o alergia debe comunicarse al hacer la reserva.",
    },

    "atmosfera": {
        "eyebrow":  "Las salas",
        "headline": "Tres estancias, <em>catorce sillas,</em> ninguna pared.",
        "intro":
            "Osteria Moderna ocupa tres estancias de un palacio bréreo "
            "del siglo XVIII en la Via San Marco. Ninguna pared entre "
            "cocina y sala. Ninguna imagen en redes: para fotografiar "
            "el plato, aquí, se lo mira con calma, sentado.",

        "rooms": [
            ("La sala principal",
             "El corazón del restaurante. Nueve comensales, tres mesas, "
             "un ventanal que da al patio interior del palacio."),
            ("La cocina vista",
             "Cinco comensales en la barra, frente a los fuegos. El "
             "chef cocina en silencio durante todo el servicio."),
            ("La bodega",
             "Una sala hipogea con 320 referencias. Visitas privadas "
             "con reserva, al terminar la cena, acompañadas por Greta Vallesi."),
            ("El patio",
             "De mayo a septiembre, dos mesas al aire libre bajo la "
             "glicinia del patio interior. Reservables solo para cenas "
             "completas."),
        ],

        "captions": [
            "La cocina vista durante el servicio del viernes por la noche.",
            "El primer acto del menú otoño '26: ostra y pepino.",
            "Greta Vallesi en bodega, entre las 320 referencias.",
            "El patio interior del palacio bréreo del siglo XVIII.",
            "Lorenzo Fioravanti durante el servicio.",
            "La sala principal al terminar la mise en place.",
        ],

        "cta_quote": "«Para fotografiar el plato, aquí, se lo mira con calma, sentado.»",
        "cta_desc": "Catorce comensales por servicio. Solo con reserva. Solo cenas. Mié – Sáb.",
        "cta_primary": "Reservar la velada",
        "cta_secondary": "Ver el menú",
    },

    "diario": {
        "eyebrow":  "El diario de sala",
        "headline": "Notas de trabajo, <em>de temporada</em>, de sala.",
        "intro":
            "Breves apuntes de Lorenzo Fioravanti y Greta Vallesi sobre "
            "el menú en curso, los productores, las veladas memorables "
            "y lo que va cambiando en cocina de semana en semana.",
        "read_article": "Leer el artículo",
        "min_label": "min",
        "min_read_label": "min de lectura",
        "crumb_label": "Diario",
        "back_link": "← Volver al diario",
        "footer_label": "Osteria Moderna · El diario de sala",
        "empty_body": [
            "Artículo en revisión editorial. La versión íntegra estará "
            "disponible en breve, redactada personalmente por el chef "
            "o el maître.",
            "Este marcador describe la voz del Diario de Sala: breves "
            "notas de trabajo, reflexiones sobre los productores, relatos "
            "de veladas memorables. Nunca más de dos mil palabras, "
            "nunca menos de quinientas.",
        ],
    },

    "posts": [
        {
            "slug":     "menu-autunno-26",
            "kicker":   "Menú en curso",
            "title":    "Las ocho ideas del menú otoño '26",
            "date":     "5 de octubre de 2026",
            "read_min": 5,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "El nuevo menú entró en carta el lunes por la noche. "
                "Ocho platos: cuatro composiciones nuevas y cuatro "
                "variaciones sobre temas que habíamos dejado en el "
                "archivo desde 2022.",
            "body": [
                ("p", "Construir un menú degustación es menos una cuestión "
                      "de recetas y más una cuestión de transiciones. Cómo "
                      "se pasa del salado al dulce. Cómo se regresa en "
                      "mitad del servicio. Cómo se introduce el cuarto "
                      "plato sin romper el ritmo. Para el menú otoño '26 "
                      "hemos trabajado dos semanas solo en las pausas."),
                ("h2", "Las cuatro ideas nuevas"),
                ("p", "El primer acto —ostra y pepino— es una relectura "
                      "de un plato que hacía mi maestro Pierre Brutscher "
                      "en el Mirazur. Lo llevaba en la cabeza desde 2007, "
                      "cuando era su aprendiz. Durante quince años no "
                      "logré darle un final. Lo encontré el verano pasado, "
                      "en un banco de Sète, viendo a Tarbouriech recoger "
                      "sus ostras al amanecer."),
                ("p", "El cuarto acto —la pasta de la casa— es la primera "
                      "vez en tres años que metemos pasta en el menú "
                      "degustación. El relleno de capón y trufa negra es "
                      "un homenaje a una receta del Val Trebbia que mi "
                      "abuela materna preparaba el día de Navidad."),
                ("h2", "Las cuatro variaciones"),
                ("p", "El pichón de Bresse vuelve a la carta después de "
                      "dos temporadas. Es mi plato-emblema, el que más "
                      "quiero de todos los que he construido desde la "
                      "apertura. Esta vez lo acompaño con una reducción "
                      "de Barolo Cannubi '17, un vino que Greta encontró "
                      "tras seis meses de llamadas a la bodega Brezza."),
                ("blockquote",
                 "Un menú degustación no es una sucesión de platos. Es "
                 "un camino que el comensal recorre con el cocinero, y "
                 "que el cocinero rehace cada noche junto al comensal."),
                ("p", "Gracias a Greta por el maridaje, a la brigada de "
                      "sala por la paciencia con la que aprendió en dos "
                      "semanas ocho nuevas descripciones, y a todos los "
                      "productores que nos han permitido construir este "
                      "menú: Tarbouriech, San Massimo, Pacherhof, los "
                      "hermanos Brezza, Domori, Marco De Bartoli."),
            ],
        },
        {
            "slug":     "barolo-cannubi-17-brezza",
            "kicker":   "Carta de vinos",
            "title":    "Seis meses de llamadas para un Barolo",
            "date":     "20 de septiembre de 2026",
            "read_min": 4,
            "author":   "Greta Vallesi",
            "lede":
                "La historia de cómo llegó a la carta el Barolo Cannubi "
                "'17 de Brezza, y por qué lo quisimos a toda costa para "
                "el quinto acto del menú de otoño.",
        },
        {
            "slug":     "cucina-a-vista",
            "kicker":   "La sala",
            "title":    "Cinco años de cocina vista: lo que hemos aprendido",
            "date":     "29 de agosto de 2026",
            "read_min": 6,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "Abrir la cocina al público cambió la manera de trabajar "
                "en brigada. También cambió la manera en que los comensales "
                "cenan. Una breve reflexión cinco años después de la "
                "apertura de la barra.",
        },
        {
            "slug":     "ostriche-tarbouriech",
            "kicker":   "Los productores",
            "title":    "Tarbouriech: el ostricultor que marea cada doce horas",
            "date":     "11 de agosto de 2026",
            "read_min": 5,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "En Sète, en el Languedoc, Florent Tarbouriech inventó "
                "un método de cultivo que imita la marea atlántica en "
                "el Mediterráneo. El resultado es la ostra de nuestro "
                "primer acto.",
        },
        {
            "slug":     "libro-otto-atti",
            "kicker":   "Edición",
            "title":    "Sale 'Ocho actos', el primer libro de Osteria Moderna",
            "date":     "1 de julio de 2026",
            "read_min": 3,
            "author":   "Greta Vallesi",
            "lede":
                "El 4 de julio Giunti publica 'Ocho actos — cuarenta "
                "veladas del menú de invierno de Osteria Moderna'. "
                "Lorenzo lo presenta el 12 de julio en la Triennale de Milán.",
        },
    ],

    "prenota": {
        "eyebrow":  "Reserva",
        "headline": "Una cena <em>no se reserva</em>: se acuerda.",
        "intro":
            "En Osteria Moderna no existe un calendario en línea. Las "
            "reservas pasan por el concierge personal del restaurante, "
            "Greta Vallesi, que contesta por correo en el mismo día.",

        "process_label": "Cómo funciona",
        "process_heading": "Cuatro pasos, <em>cuatro días de antelación</em>.",
        "hours_label": "Servicios de la semana",
        "hours_heading": "Cuatro noches, <em>un único pase</em>.",
        "private_heading": "Cenas privadas",
        "form_submit": "Enviar nota al concierge",

        "process": [
            ("01", "Escribe a Greta",
             "Bastan pocas líneas: fecha preferida, número de comensales, "
             "intolerancias, ocasión. Greta lee cada mensaje personalmente."),
            ("02", "Propuesta de velada",
             "En el día Greta te propone una o dos fechas compatibles "
             "(los servicios son de miércoles a sábado) y confirma el "
             "menú vigente."),
            ("03", "Confirmación y depósito",
             "Para confirmar la reserva se pide un pequeño depósito de "
             "80 € por persona, que se descuenta de la cuenta final."),
            ("04", "Nota de velada",
             "La víspera recibirás un breve correo con el código de "
             "vestuario, el menú en carta y una nota sobre el maridaje "
             "opcional."),
        ],

        "concierge": {
            "name":  "Greta Vallesi",
            "role":  "Maître & responsable de bodega",
            "email": "greta@osteriamoderna.it",
            "phone": "+39 02 3611 9920",
            "bio":
                "Romana de nacimiento, milanesa de adopción. Quince años "
                "en sala, nueve de ellos en Osteria Moderna. Sommelier "
                "AIS desde 2014. En sala cada noche de 18:30 a 23:30.",
        },

        "hours": [
            ("Miércoles", "20:00 – 23:30 h", "1 servicio · pase único"),
            ("Jueves",    "20:00 – 23:30 h", "1 servicio · pase único"),
            ("Viernes",   "20:00 – 23:30 h", "1 servicio · pase único"),
            ("Sábado",    "20:00 – 23:30 h", "1 servicio · pase único"),
            ("Domingo",   "Cerrado",          "—"),
            ("Lun & Mar", "Cerrado",          "Descanso semanal de la brigada"),
        ],

        "private_title": "Cenas privadas y eventos",
        "private_intro":
            "Para cenas privadas (aniversarios, actos de empresa, "
            "presentaciones de producto) es posible reservar la sala "
            "entera los días de cierre. Paquetes a medida, acordados "
            "personalmente con el chef.",

        "form_title":  "Escribe al concierge",
        "form_fields": [
            ("Nombre y apellidos",  "Mario Rossi",                               "text"),
            ("Correo electrónico",  "mario@email.es",                            "email"),
            ("Teléfono",            "+34 6 ...",                                 "tel"),
            ("Número de comensales","2",                                         "number"),
            ("Fecha preferida",     "vie. 16 de octubre",                        "text"),
            ("Ocasión",             "",                                          "select"),
            ("Alergias o intolerancias", "Alergias, intolerancias o peticiones especiales", "text"),
            ("Nota al concierge",   "Greta lee cada mensaje personalmente. Bastan unas pocas líneas.", "textarea"),
        ],
        "occasion_options": ["Cena romántica", "Cumpleaños", "Negocios", "Sin ocasión"],
        "consent":
            "Autorizo el tratamiento de mis datos personales conforme a "
            "la política de privacidad, en virtud del Reglamento UE 679/2016.",

        "address_block": [
            ("Dirección", "Via San Marco 17 · 20121 Milán"),
            ("Transporte","Lanza M2 · 4 minutos a pie · Brera"),
            ("Aparcamiento","APCOA Garibaldi 36 · lanzadera gratuita"),
        ],
    },
}


# ===========================================================================
# ARABIC (RTL) — Modern Standard Arabic, formal hospitality register.
# Reads as premium Arabic food editorial. Latin proper names retained
# for canonical items (chef/producer/press/wine names). Arrows flipped
# where they're reading cues.
# ===========================================================================

GUSTO_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "الرئيسية",    "kind": "home"},
        {"slug": "filosofia", "label": "الفلسفة",     "kind": "about"},
        {"slug": "menu",      "label": "القائمة",     "kind": "menu"},
        {"slug": "atmosfera", "label": "القاعات",     "kind": "gallery"},
        {"slug": "diario",    "label": "المدوّنة",     "kind": "blog_list"},
        {"slug": "prenota",   "label": "احجز",        "kind": "reservations"},
    ],

    "site": {
        "logo_initial": "OM",
        "logo_word":    "Osteria Moderna",
        "tag":          "طاولة واحدة · ميلانو، بريرا · 14 ضيفًا",
        "phone":        "+39 02 3611 9920",
        "email":        "concierge@osteriamoderna.it",
        "address":      "Via San Marco 17 · 20121 ميلانو",
        "hours_compact":"من الأربعاء إلى السبت · العشاء فقط",
        "star_line":    "★ نجمة ميشلان واحدة · منذ 2018",
        "footer_intro":
            "نجمة ميشلان منذ 2018. أربعة عشر ضيفًا، خدمتان في الأسبوع، "
            "قائمة تذوّق من ثمانية فصول تُعاد كتابتها كلّ أسبوعين.",
        "footer_hours_1": "أربعاء – سبت · 20:00",
        "footer_hours_2": "أحد وإثنين · مغلق",
        "copyright": "© 2026 Osteria Moderna · الرقم الضريبي 09456112094",
    },

    "home": {
        "eyebrow":  "طاولة واحدة · ميلانو، بريرا · 14 ضيفًا",
        "headline": "سهرة في <em>ثمانية فصول.</em>",
        "intro":
            "قائمة تذوّق تُعاد كتابتها كلّ أسبوعين وفق سوق الصباح. "
            "العشاء فقط. بالحجز حصرًا. لأربعة عشر ضيفًا.",
        "primary_cta":   "احجز السهرة",
        "primary_href":  "prenota",
        "secondary_cta": "تعرّف على الشيف",
        "secondary_href":"filosofia",

        "chef_label":    "الشيف",
        "star_tag":      "★ الفصل الخامس · شوكولاتة 80٪",
        "photo_label":   "تصوير",
        "cuisine_label": "المطبخ",

        "facts": [
            ("14",   "ضيفًا في الخدمة الواحدة"),
            ("8",    "فصول في قائمة التذوّق"),
            ("180€", "القائمة الكاملة · مرافقة النبيذ + 90€"),
        ],

        "manifesto_drop_cap": "ق",
        "manifesto":
            "ائمة تُعاد كتابتها كلّ أسبوعين. قاعة واحدة لأربعة عشر "
            "ضيفًا. مطبخ مفتوح يعمل في صمتٍ طيلة أربع ساعات متواصلة. "
            "في Osteria Moderna لا يُطلَب من القائمة — بل تدخل في "
            "حكايةٍ لها بدايةٌ وذروةٌ وخاتمة.",

        "signature_courses": [
            ("I",   "محار وخيار",       "حميض، لآلئ يوزو",                       "Champagne Selosse"),
            ("II",  "ريزوتّو بالنخاع",   "خلاصة بقدونس، قهوة",                    "Soave Pieropan '21"),
            ("III", "محار الأسقلوب",    "زبدة البندق، كبّار بانتيلليريا",          "Riesling Pacherhof"),
            ("IV",  "يمام بريس",        "تين أسود، هال أخضر",                     "Barolo Cannubi '17"),
            ("V",   "شوكولاتة 80٪",     "زيت زيتون، ملح مالدون",                 "Marsala Vintage '99"),
        ],

        "courses_label": "خمسة فصول من القائمة الحالية · خريف '26",
        "courses_footline": "180€ للشخص · مرافقة النبيذ + 90€",
        "courses_full_cta": "الفصول الثمانية كاملةً",
        "chef_link_filosofia": "الفلسفة",
        "chef_link_diario": "المدوّنة",

        "chef": {
            "name":  "Lorenzo Fioravanti",
            "role":  "شيف ومالك · نجمة ميشلان واحدة",
            "bio":
                "من مواليد روما عام 1981. تدرّب مع Bottura وCracco، "
                "ومع Brutscher في Mirazur. افتتح Osteria Moderna عام "
                "2014 في ثلاث قاعات من قصرٍ بريروي من القرن الثامن عشر. "
                "نال نجمة ميشلان عام 2018 وحافظ عليها حتى اليوم.",
        },

        "press_label": "كُتب عنّا في",
        "press": ["GUIDA MICHELIN", "GAMBERO ROSSO", "IDENTITÀ GOLOSE",
                  "CORRIERE LIVING", "VOGUE FOOD"],

        "ingredienti": {
            "label": "المُنتجون",
            "heading": "اثنان وثلاثون مُنتجًا، <em>كلٌّ منهم بالاسم.</em>",
            "text":
                "تضمّ شبكة Osteria Moderna اثنين وثلاثين مُنتجًا صغيرًا — "
                "صيّادي ليغوريا، ومربّي ماشية بييمونتي، ومزارعي خضروات "
                "لودي — يعرف Lorenzo كلَّ واحدٍ منهم باسمه وعنوانه ورقم "
                "هاتفه. لا وسطاء، لا كتالوجات، لا موزّعون.",
            "image": _INGREDIENTI_IMG,
            "image_caption": "مكوّنات قائمة خريف '26 · سوق الصباح",
        },

        "atmosphere_teaser": {
            "label": "القاعات",
            "images": [
                (_ATMO_SALA,    "القاعة الرئيسية"),
                (_ATMO_CUCINA,  "المطبخ المفتوح"),
                (_ATMO_CORTILE, "القاعة العلويّة"),
                (_ATMO_MISE,    "التحضير مساء الجمعة"),
            ],
            "link_label": "اكتشف القاعات",
            "link_href":  "atmosfera",
        },

        "riconoscimenti": {
            "label": "التكريمات",
            "items": [
                ("★", "نجمة ميشلان", "منذ 2018 — مُؤكَّدة كلّ عام"),
                ("GR", "Gambero Rosso", "ثلاث شوك · جائزة خاصّة لمطبخ المؤلّف 2025"),
                ("IG", "Identità Golose", "طبق العام 2024 — يمام بريس"),
                ("50B", "50 Best Discovery", "اختيار إيطاليا 2026"),
            ],
        },

        "cta_heading": "أربعة عشر ضيفًا، <em>خدمتان في الأسبوع.</em>",
        "cta_primary": "احجز السهرة",
        "cta_secondary": "اطّلع على القائمة الكاملة",

        "stagione": {
            "label": "في هذه اللحظة",
            "title": "قائمة خريف '26",
            "subtitle": "ثمانية فصول · من 6 إلى 19 أكتوبر",
            "text":
                "القائمة الجديدة على المائدة منذ الإثنين. ثمانية أطباق: "
                "أربعة تراكيب جديدة، وأربع تنويعات على ثيمات تركناها في "
                "الأرشيف منذ 2022. الحجز إلزامي.",
            "cta_label": "اكتشف الفصول الثمانية ←",
            "cta_href":  "menu",
        },

        "produttori": {
            "label":   "من المنتجين",
            "heading": "أربعة أيدٍ، <em>مائدة واحدة.</em>",
            "intro":
                "في كلّ صباح يدخل جزء من القاعة من باب المطبخ. هذه هي الوجوه. "
                "أراضيهم وأساليبهم — ستجدونها على القائمة، سطرًا سطرًا.",
            "items": [
                {"portrait":
                    "https://images.unsplash.com/photo-1552058544-f2b08422138a"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Roberto Tarbouriech",
                 "role": "المحار والقشريات",
                 "area": "Sète · Étang de Thau",
                 "blurb":
                    "محار Spéciales يأتي من بحيرة Étang de Thau. يُوصَل الإثنين "
                    "ويُقدَّم مساء الثلاثاء."},
                {"portrait":
                    "https://images.unsplash.com/photo-1568213816046-0ee1c42bd559"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "عائلة Brezza",
                 "role": "Barolo وLanghe",
                 "area": "Barolo · بييمونتي",
                 "blurb":
                    "كرومات في Cannubi وSarmassa تُستثمر بلا خبير خارجيّ. "
                    "قائمة عموديّة منذ 2008."},
                {"portrait":
                    "https://images.unsplash.com/photo-1543418219-44e30b057fea"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Aloïs Lageder",
                 "role": "زراعة ديناميّة حيوية جبلية",
                 "area": "Pacherhof · تيرول الجنوبية",
                 "blurb":
                    "نبيذ أبيض يصل مباشرة من وادي Isarco. بلا ترشيح ولا "
                    "توضيح."},
                {"portrait":
                    "https://images.unsplash.com/photo-1414235077428-338989a2e8c0"
                    "?auto=format&fit=crop&w=800&q=80",
                 "name": "Gianfranco Pieropan",
                 "role": "Soave Classico",
                 "area": "Soave · فينيتو",
                 "blurb":
                    "Calvarino وLa Rocca، Soave Classico صرف. يرافقان الفصل "
                    "الثاني منذ البداية."},
            ],
        },
        "private_dining": {
            "label":   "مناسبات خاصة",
            "heading": "طاولة الشيف و<em>الحجوزات الخاصة.</em>",
            "intro":
                "لاثني عشر ضيفاً في القاعة الخاصّة أو للسهرة بأكملها — ثمانية "
                "وعشرون ضيفاً، قائمة واحدة، ومطبخ مكشوف.",
            "experiences": [
                {"icon": "fork", "title": "طاولة الشيف",
                 "meta":  "١٢ ضيفاً · من ١٩٠ € للشخص",
                 "desc":
                    "طاولة وحيدة تُطلّ على المطبخ. قائمة من ثمانية فصول "
                    "يرويها الشيف مباشرة. أيام الثلاثاء فقط."},
                {"icon": "door", "title": "حجز السهرة كاملاً",
                 "meta":  "٢٨ ضيفاً · من ٥٨٠٠ € للسهرة",
                 "desc":
                    "المطعم كاملاً، قائمة مخصّصة، الزهور، متر مختصّ. مهلة "
                    "أسبوعين كحدّ أدنى، ونعتذر عن الجمعة."},
                {"icon": "wine", "title": "ذَواق القبو",
                 "meta":  "٦ ضيوف · الخميس فقط",
                 "desc":
                    "سهرة شهرياً مع السوميلييه حول ستّ قوارير مختارة من "
                    "المنتجين على القائمة. على لائحة الانتظار فقط."},
            ],
            "cta_label": "اكتب إلى الكونسيرج",
            "cta_href":  "prenota",
        },
        "wine_program": {
            "label":   "القبو",
            "heading": "أربعمئة ماركة، <em>ثلاث توافقات في السهرة.</em>",
            "intro":
                "القائمة تتبع القائمة: كلّ فصل له توافقه وبديلان — كلاسيكيّ، "
                "معاصر، خالٍ من الكحول.",
            "sommelier": {
                "name": "Greta Vallesi",
                "role": "متر و سوميلييه",
                "bio":
                    "خمسة عشر عاماً بين Bourgogne وLanghe وChampagne. القائمة "
                    "مِن توقيعها، والتوافق يُقترَح دائماً على الطاولة ولا يُفرَض.",
            },
            "pairings": [
                ("01", "توافق كلاسيكيّ",
                 "شامبانيا Blanc de Blancs، Soave Classico، Barolo Riserva، Moscato.",
                 "+ ١١٠ €"),
                ("02", "توافق معاصر",
                 "Col Fondo من فينيتو، Erbaluce طويل، Ribolla في أمفورة، "
                 "Timorasso عمودي.",
                 "+ ١٣٠ €"),
                ("03", "توافق بلا كحول",
                 "كومبوتشا حرفيّة، شاي بارد بتحضير بطيء، عصير عنب في تخمّر "
                 "طبيعيّ.",
                 "+ ٦٠ €"),
            ],
            "cellar_facts": [
                ("٤٢٠", "ماركة على القائمة"),
                ("١٨", "منطقة نبيذيّة"),
                ("٢٠٠٥", "الأقدم عمودياً (Brunello)"),
            ],
        },
    },

    "filosofia": {
        "eyebrow":  "الفلسفة",
        "headline": "قائمة واحدة، قاعة واحدة، <em>سهرة واحدة فقط.</em>",
        "intro":
            "وُلد Osteria Moderna عام 2014 من فكرةٍ مفادها أنّ المطعم ليس "
            "خدمة بل مسرح. أربعة عشر ضيفًا في الخدمة الواحدة، خدمتان "
            "في الأسبوع، طاهٍ واحد على البار، مِيتْر واحد في القاعة.",

        "history": [
            ("2014",
             "يفتتح Lorenzo Fioravanti مطعم Osteria Moderna في ثلاث "
             "قاعات من قصرٍ بريروي من القرن الثامن عشر. ستّة عشر ضيفًا، "
             "فريقٌ واحد، قائمةٌ تتبدّل كلّ يوم جمعة."),
            ("2016",
             "تنضمّ Greta Vallesi مِيتْر ومسؤولةً عن القبو. تتوسّع قائمة "
             "النبيذ من 80 إلى 320 مرجعًا، مع تركيز على صغار المُنتجين في "
             "شمال شرق إيطاليا وبورغونيا الصغيرة."),
            ("2018",
             "نجمة ميشلان. من تلك اللحظة يقلّص المطعم عدد ضيوفه إلى "
             "أربعة عشر في الخدمة الواحدة، ويعتمد قائمة التذوّق من "
             "ثمانية فصول وحدها."),
            ("2021",
             "يُفتَح البار على القاعة. يطبخ الشيف أمام الضيوف طوال مدّة "
             "الخدمة. لا جدار بين المطبخ والطاولة."),
            ("2024",
             "صدور كتاب «ثمانية فصول» عن دار Giunti، وهو يتناول "
             "الأمسيات الأربعين الأولى من قائمة شتاء 2023/24."),
        ],

        "filosofia_image": _FILOSOFIA_IMG,
        "filosofia_image_caption": "المطبخ · Lorenzo Fioravanti أثناء العمل",

        "method_title": "المنهج",
        "method_paragraphs": [
            "تُعاد كتابة قائمة التذوّق كلّ أسبوعين تبعًا لسوق الصباح. "
            "تصل المواد الأوّليّة من شبكةٍ من اثنين وثلاثين مُنتجًا "
            "صغيرًا — صيّادي ليغوريا، مربّي ماشية بييمونتي، مزارعي خضروات "
            "لودي — يعرف Lorenzo كلَّ واحدٍ منهم باسمه وعنوانه ورقم هاتفه.",
            "كلّ فصلٍ يُصاغ كحركةٍ من سمفونية: ثمّة افتتاحٌ، وتصاعدٌ في "
            "منتصف الخدمة، وراحةٌ شعريّة، وختامٌ يعود إلى البداية ليُغلق "
            "الدائرة. تُعاد كتابة التسلسل من الصفر كلّ أسبوعين — لا نعيد "
            "الانتقالات نفسها مرّتين.",
            "قائمة النبيذ تُشرف عليها Greta Vallesi: 320 مرجعًا، ثلثاها "
            "من صغار المُنتجين الأوروبيين. المرافقة اختياريّة (90€ "
            "للمسار الكامل) لكنّها — بصراحة — نصف ما نقوم به.",
        ],

        "values_label": "ما نعِد به",
        "values_heading": "أربعة وعودٍ <em>لا تتغيّر أبدًا</em>.",
        "values": [
            ("الوقت",     "ثلاث ساعات ونصف من الخدمة. لا أكثر، لا أقلّ."),
            ("الموسم",    "لا شيء على المائدة إلّا ما هو من موسمه المحلّي."),
            ("الشفافيّة", "نعرف كلَّ مُنتجٍ على القائمة بالاسم."),
            ("التحفّظ",   "لا صور للشيف ولا تواصل اجتماعيّ: في القاعة يُؤكل."),
        ],

        "cta_heading": "هل تريد الاطّلاع على القائمة <em>السارية هذا الأسبوع؟</em>",
        "cta_menu": "الفصول الثمانية لخريف '26",
        "cta_prenota": "احجز السهرة",
    },

    "menu": {
        "eyebrow":  "القائمة",
        "headline": "ثمانية فصول — <em>خريف '26</em>",
        "intro":
            "تُعاد كتابة القائمة بالكامل كلّ أسبوعين. ما يلي هو البرنامج "
            "الساري من 6 إلى 19 أكتوبر 2026. خدمتان في الأسبوع، من الأربعاء "
            "إلى السبت، جلسة واحدة في تمام الساعة 20:00.",
        "courses_label": "ثمانية فصول · الخدمة من 20:00",

        "courses": [
            ("I",    "محار وخيار",
             "محار Tarbouriech من سِيت، جلّ خيار عضويّ من بحيرة كومو، "
             "حميض برّيّ، لآلئ يوزو معلّقة في زيت الزيتون التاجياسكا.",
             "Champagne Anselme Selosse · Initial · Avize"),
            ("II",   "ريزوتّو بالنخاع",
             "كارناروللي ريزرفا San Massimo 2023، نخاعٌ مشويّ على جمر "
             "فروع الكرم، خلاصة بقدونس مُجعّد، بودرة قهوة إثيوبيّة مفردة "
             "الأصل.",
             "Soave Classico Pieropan · La Rocca '21"),
            ("III",  "محار الأسقلوب",
             "أسقلوب الغاليسيّة من الصيد الحرّ، زبدة بندق بالروزماري، "
             "كبّار بانتيلليريا مملَّح، جلّ ليمون أمالفي.",
             "Riesling Pacherhof · Kerner Alto Adige '22"),
            ("IV",   "معكرونة البيت",
             "كابِلِتّي مصنوعةٌ يدويًّا، محشوّةٌ بديك بريس وكمأة Val Trebbia "
             "السوداء، ومرق خنزير برّيٍّ مختزل سبع مرّات.",
             "Lambrusco di Sorbara Rinaldini · Rosé Brut"),
            ("V",    "يمام بريس",
             "صدرٌ ورديٌّ مُلمَّع بعسل الكستناء، فخذٌ كونفيه بتين Caprino "
             "الأسود، اختزال Barolo، وبودرة هال أخضر غواتيماليّ.",
             "Barolo Riserva Cannubi · Brezza '17"),
            ("VI",   "ما قبل الحلوى",
             "شربات كرفس الجذور، أوكساليس من حديقتنا، شراب Dro البرقوقيّ "
             "المثلَّج، وبلّورات ملح وردي.",
             "—"),
            ("VII",  "شوكولاتة 80٪",
             "شوكولاتة Domori Criollo 80٪، زيت زيتون بكر ممتاز من Tuscia، "
             "ملح Maldon مُدخَّن بخشب التفّاح، بودرة عرق السوس الكلابريّ.",
             "Marsala Vintage Marco De Bartoli · 1999"),
            ("VIII", "مِنْيَارْدِيز",
             "ثلاث حلوياتٍ صغيرة من صنع المؤلّف: واحدةٌ بالشوكولاتة، "
             "وأخرى بالحمضيّات، وثالثة بالعسل.",
             "قهوة إثيوبية مفردة الأصل Yirgacheffe"),
        ],

        "wine_intro_title": "قائمة النبيذ",
        "wine_intro":
            "320 مرجعًا، ثلثاها من صغار المُنتجين الأوروبيين. Greta "
            "Vallesi في القاعة كلّ ليلة لمناقشة كلّ اختيار — ومستعدّةٌ "
            "أيضًا لبناء مرافقةٍ شخصيّة تذوّقيّة خارج المسار المعتاد.",

        "wine_highlights": [
            ("Champagne",    "62 مرجعًا · 24 شامبانيا مُنتِج"),
            ("Burgundy",     "48 مُنتِجًا · تركيز على Côte de Beaune و Mâconnais"),
            ("Italy",        "112 مرجعًا · شمال شرق، بييمونتي العليا، وصقليّة البركانيّة"),
            ("Fortifieds",   "18 مرجعًا · شيري، مارسالا، ماديرا، توكاي"),
        ],

        "footer":
            "قائمة التذوّق الكاملة: 180€ للشخص. مرافقة النبيذ الاختياريّة: "
            "90€ للشخص. باقة Magnum (ستّ كؤوس من Magnum، تشاركيّة): + 140€. "
            "يُرجى إعلامنا بأيّ حساسيّة أو عدم تحمّل عند الحجز.",
    },

    "atmosfera": {
        "eyebrow":  "القاعات",
        "headline": "ثلاث غرف، <em>أربعة عشر كرسيًّا،</em> لا جدران.",
        "intro":
            "يشغل Osteria Moderna ثلاث غرفٍ من قصرٍ بريروي من القرن "
            "الثامن عشر في Via San Marco. لا جدار بين المطبخ والقاعة. "
            "لا صور على وسائل التواصل: لتصوير الطبق هنا، يُنظَر إليه "
            "بتمهّلٍ من على المقعد.",

        "rooms": [
            ("القاعة الرئيسيّة",
             "قلب المطعم. تسعة ضيوف، ثلاث طاولات، نافذةٌ مطلّةٌ على "
             "الفناء الداخليّ للقصر."),
            ("المطبخ المفتوح",
             "خمسة ضيوف على البار، أمام النار. يطبخ الشيف في صمتٍ طوال "
             "مدّة الخدمة."),
            ("القبو",
             "غرفة تحت الأرض تضمّ 320 مرجعًا. زياراتٌ خاصّة بالحجز، في "
             "ختام العشاء، برفقة Greta Vallesi."),
            ("الفناء",
             "من مايو إلى سبتمبر، طاولتان في الهواء الطلق تحت شجرة "
             "الوستريا في الفناء الداخليّ. متاحتان للحجز فقط لعشاءٍ كامل."),
        ],

        "captions": [
            "المطبخ المفتوح خلال خدمة مساء الجمعة.",
            "الفصل الأوّل من قائمة خريف '26: محار وخيار.",
            "Greta Vallesi في القبو، بين 320 مرجعًا.",
            "الفناء الداخليّ لقصر Via San Marco البريروي من القرن الثامن عشر.",
            "Lorenzo Fioravanti أثناء الخدمة.",
            "القاعة الرئيسيّة في ختام التحضير.",
        ],

        "cta_quote": "«لتصوير الطبق هنا، يُنظَر إليه بتمهّلٍ من على المقعد.»",
        "cta_desc": "أربعة عشر ضيفًا في الخدمة. بالحجز فقط. العشاء فقط. أربعاء – سبت.",
        "cta_primary": "احجز السهرة",
        "cta_secondary": "اطّلع على القائمة",
    },

    "diario": {
        "eyebrow":  "مدوّنة القاعة",
        "headline": "ملاحظاتُ عمل، <em>ملاحظاتُ موسم</em>، ملاحظاتُ قاعة.",
        "intro":
            "قيوداتٌ قصيرة من Lorenzo Fioravanti و Greta Vallesi حول "
            "القائمة الحاليّة، والمُنتجين، والأمسيات التي لا تُنسى، "
            "وما يتغيّر في المطبخ من أسبوعٍ لآخر.",
        "read_article": "قراءة المقال",
        "min_label": "دقائق",
        "min_read_label": "دقائق قراءة",
        "crumb_label": "المدوّنة",
        "back_link": "→ العودة إلى المدوّنة",
        "footer_label": "Osteria Moderna · مدوّنة القاعة",
        "empty_body": [
            "المقال قيد المراجعة التحريريّة. سينشر بالكامل قريبًا، بقلم "
            "الشيف أو المِيتْر شخصيًّا.",
            "يصف هذا الفاصل صوت مدوّنة القاعة: قيوداتُ عمل قصيرة، "
            "تأمّلاتٌ في المُنتجين، حكاياتٌ عن أمسياتٍ لا تُنسى. لا "
            "تتجاوز ألفي كلمة، ولا تقلّ عن خمسمئة.",
        ],
    },

    "posts": [
        {
            "slug":     "menu-autunno-26",
            "kicker":   "القائمة الحاليّة",
            "title":    "الأفكار الثمانية لقائمة خريف '26",
            "date":     "5 أكتوبر 2026",
            "read_min": 5,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "دخلت القائمة الجديدة المطعم مساء الإثنين. ثمانية "
                "أطباق: أربعة تراكيب جديدة، وأربع تنويعات على ثيماتٍ "
                "تركناها في الأرشيف منذ 2022.",
            "body": [
                ("p", "صياغة قائمة تذوّق ليست مسألةَ وصفاتٍ قدرَ ما هي "
                      "مسألةُ انتقالات. كيف ننتقل من المالح إلى الحلو. "
                      "كيف نعود إلى الوراء في منتصف الخدمة. كيف نُدخل "
                      "الطبق الرابع دون كسر الإيقاع. لقائمة خريف '26 "
                      "عملنا أسبوعين على الوقفات وحدها."),
                ("h2", "الأفكار الأربع الجديدة"),
                ("p", "الفصل الأوّل — محار وخيار — هو إعادة قراءةٍ لطبقٍ "
                      "كان معلّمي Pierre Brutscher يُقدّمه في Mirazur. "
                      "حملته في ذهني منذ 2007، من أيّامي متدرّبًا لديه. "
                      "طوال خمسة عشر عامًا لم أعثر على خاتمته. وجدتها "
                      "الصيف الماضي، على مقعدٍ في سِيت، بينما كان "
                      "Tarbouriech يحصد محاراته عند الفجر."),
                ("p", "الفصل الرابع — معكرونة البيت — أوّل مرّةٍ في "
                      "ثلاث سنوات نضع فيها المعكرونة داخل قائمة التذوّق. "
                      "حشوة الديك والكمأة السوداء تحيّةٌ لوصفةٍ من "
                      "Val Trebbia كانت جدّتي لأمّي تُعدّها يوم عيد الميلاد."),
                ("h2", "التنويعات الأربع"),
                ("p", "يعود يمام بريس بعد موسمين. هو طبقي الأثير، وأحبّ "
                      "ما صنعت منذ الافتتاح. هذه المرّة أرافقه باختزال "
                      "Barolo Cannubi '17 — نبيذٌ عثرت عليه Greta بعد ستّة "
                      "أشهرٍ من المكالمات مع مزرعة Brezza."),
                ("blockquote",
                 "قائمة التذوّق ليست تتابعًا لأطباق. هي طريقٌ يقطعه الضيف "
                 "مع الطاهي، ويُعيد الطاهي سلوكَه كلّ ليلةٍ مع الضيف."),
                ("p", "شكرًا لـGreta على المرافقة، ولفريق القاعة على الصبر "
                      "الذي تعلّموا به في أسبوعين ثماني سرديّاتٍ جديدة، "
                      "ولكلّ مُنتجٍ أتاح لنا بناء هذه القائمة: Tarbouriech، "
                      "San Massimo، Pacherhof، الأخوان Brezza، Domori، "
                      "Marco De Bartoli."),
            ],
        },
        {
            "slug":     "barolo-cannubi-17-brezza",
            "kicker":   "قائمة النبيذ",
            "title":    "ستّة أشهرٍ من المكالمات لأجل Barolo",
            "date":     "20 سبتمبر 2026",
            "read_min": 4,
            "author":   "Greta Vallesi",
            "lede":
                "قصّة وصول Barolo Cannubi '17 من Brezza إلى القائمة، "
                "ولمَ أردناه بأيّ ثمنٍ للفصل الخامس من قائمة الخريف.",
        },
        {
            "slug":     "cucina-a-vista",
            "kicker":   "القاعة",
            "title":    "خمس سنواتٍ من المطبخ المفتوح: ماذا تعلّمنا",
            "date":     "29 أغسطس 2026",
            "read_min": 6,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "غيّر فتحُ المطبخ أمام الجمهور طريقة عمل الفريق. وغيّر "
                "أيضًا طريقة تناول الضيوف الطعام. تأمّلٌ قصيرٌ بعد خمس "
                "سنواتٍ من افتتاح البار.",
        },
        {
            "slug":     "ostriche-tarbouriech",
            "kicker":   "المُنتجون",
            "title":    "Tarbouriech: المُربّي الذي يصنع المدّ كلَّ اثنتي عشرة ساعة",
            "date":     "11 أغسطس 2026",
            "read_min": 5,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "في سِيت، إقليم لانغدوك، ابتكر Florent Tarbouriech "
                "طريقةَ تربيةٍ تحاكي المدّ الأطلسيّ داخل المتوسّط. "
                "ثمرةُ ذلك هي محار الفصل الأوّل عندنا.",
        },
        {
            "slug":     "libro-otto-atti",
            "kicker":   "الإصدار",
            "title":    "يصدر «ثمانية فصول»، أوّل كتابٍ من Osteria Moderna",
            "date":     "1 يوليو 2026",
            "read_min": 3,
            "author":   "Greta Vallesi",
            "lede":
                "تنشر Giunti يوم 4 يوليو كتاب «ثمانية فصول — أربعون أمسيةً "
                "من قائمة شتاء Osteria Moderna». يقدّمه Lorenzo يوم 12 "
                "يوليو في Triennale di Milano.",
        },
    ],

    "prenota": {
        "eyebrow":  "الحجز",
        "headline": "العشاء <em>لا يُحجَز</em>: يُتَّفق عليه.",
        "intro":
            "في Osteria Moderna لا يوجد تقويمٌ إلكترونيّ. تمرّ الحجوزات "
            "عبر Greta Vallesi، مسؤولة استقبال المطعم الشخصيّة، التي "
            "تردّ بالبريد الإلكترونيّ في نفس اليوم.",

        "process_label": "كيف يعمل",
        "process_heading": "أربع خطوات، <em>أربعة أيامٍ مقدّمًا</em>.",
        "hours_label": "خدمات الأسبوع",
        "hours_heading": "أربع ليالٍ، <em>جلسةٌ واحدة</em>.",
        "private_heading": "العشاء الخاصّ",
        "form_submit": "أرسِل ملاحظةً إلى مسؤولة الاستقبال",

        "process": [
            ("01", "اكتب إلى Greta",
             "تكفي أسطرٌ قليلة: التاريخ المفضَّل، عدد الضيوف، أيّ "
             "حساسيّة، المناسبة. تقرأ Greta كلّ طلبٍ بنفسها."),
            ("02", "اقتراح السهرة",
             "في نفس اليوم تقترح Greta تاريخًا أو اثنين متوافقَين "
             "(الخدمات من الأربعاء إلى السبت فقط)، وتؤكّد القائمة "
             "الساريَة."),
            ("03", "التأكيد والعربون",
             "لتأكيد الحجز يُطلَب عربونٌ رمزيٌّ قدره 80€ للشخص، "
             "يُخصم من الفاتورة النهائيّة."),
            ("04", "مذكّرة السهرة",
             "قبل يومٍ من موعدك ستصلك رسالةٌ قصيرة ببريدك تتضمّن "
             "قواعد اللباس، القائمة الساريَة، وملاحظةً حول مرافقة "
             "النبيذ الاختياريّة."),
        ],

        "concierge": {
            "name":  "Greta Vallesi",
            "role":  "مِيتْر ومديرة القبو",
            "email": "greta@osteriamoderna.it",
            "phone": "+39 02 3611 9920",
            "bio":
                "مولودةٌ في روما، مُتبنّاةٌ ميلانيّة. خمسة عشر عامًا "
                "في القاعة، منها تسع في Osteria Moderna. سومِلْيِيه "
                "معتمدة من AIS منذ 2014. في القاعة كلّ مساءٍ من 18:30 "
                "إلى 23:30.",
        },

        "hours": [
            ("الأربعاء",     "20:00 – 23:30", "خدمة واحدة · جلسة واحدة"),
            ("الخميس",       "20:00 – 23:30", "خدمة واحدة · جلسة واحدة"),
            ("الجمعة",       "20:00 – 23:30", "خدمة واحدة · جلسة واحدة"),
            ("السبت",        "20:00 – 23:30", "خدمة واحدة · جلسة واحدة"),
            ("الأحد",        "مغلق",          "—"),
            ("الإثنين والثلاثاء", "مغلق",     "راحة أسبوعيّة للفريق"),
        ],

        "private_title": "عشاءٌ خاصّ وفعّاليّات",
        "private_intro":
            "للعشاءات الخاصّة (ذكريات سنويّة، مناسبات شركات، تقديم "
            "منتجات) يمكن حجز القاعة بكاملها في أيّام الإغلاق. باقاتٌ "
            "على المقاس، يُتّفق عليها مباشرةً مع الشيف.",

        "form_title":  "اكتب إلى مسؤولة الاستقبال",
        "form_fields": [
            ("الاسم الكامل",          "Mario Rossi",                           "text"),
            ("البريد الإلكترونيّ",    "mario@email.ae",                       "email"),
            ("الهاتف",               "+971 5 ...",                            "tel"),
            ("عدد الضيوف",           "2",                                     "number"),
            ("التاريخ المفضَّل",       "جمعة 16 أكتوبر",                         "text"),
            ("المناسبة",              "",                                      "select"),
            ("الحساسيّات أو القيود",   "أيّ حساسيّةٍ أو قيدٍ غذائيّ أو طلبٍ خاصّ", "text"),
            ("ملاحظة إلى الاستقبال",  "تقرأ Greta كلَّ رسالةٍ بنفسها. تكفي بضع عبارات.",    "textarea"),
        ],
        "occasion_options": ["عشاءٌ رومانسيّ", "عيد ميلاد", "عمل", "دون مناسبة"],
        "consent":
            "أوافق على معالجة بياناتي الشخصيّة وفقًا لسياسة الخصوصيّة، "
            "بموجب لائحة الاتحاد الأوروبيّ 679/2016.",

        "address_block": [
            ("العنوان",     "Via San Marco 17 · 20121 ميلانو"),
            ("المواصلات",   "Lanza M2 · على بُعد 4 دقائق مشيًا · بريرا"),
            ("المواقف",    "APCOA Garibaldi 36 · خدمة نقلٍ مجّانيّة"),
        ],
    },
}
