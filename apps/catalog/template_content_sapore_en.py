"""Sapore — Trattoria Da Nonna Rosa (trattoria-warm archetype) — EN content tree.

Phase 2g3.6 — Restaurant live-completion (Session 48, 2026-04-15).

Voice contract (EN):
- Bon Appétit / Saveur / NYT Food-section register reviewing a Roman
  family trattoria. Warm, observant, inclusive second-person "you".
  Never glossy, never machine-translated, never marketing-speak.
- "Like Nonna's house, only louder" energy. Proud, casual, confident.
- Italian dish names stay Italian: Cacio e pepe, Carbonara, Bucatini
  all'amatriciana, Coda alla vaccinara, Tonnarelli, Margherita Verace,
  Cesanese del Lazio. A short EN gloss in parentheses on first mention
  only when the dish is obscure.
- Italian proper names stay Italian: Trattoria Da Nonna Rosa, Rosa
  Trezzi, Marco Trezzi, Giulia Trezzi, Trastevere, Roma, Via dei
  Salumi, Lazio, Amatrice. Never translated, never transliterated.
- European 24h clock and metric units. Currency stays "€ 12.00"
  (decimal point for EN).

Differentiation contract vs Gusto EN (D-054 enforcement):
- Sapore EN = Bon Appétit / NYT Food food-writer reportage on a Roman
  family trattoria. Gusto EN = Michelin editorial-chef critic register.
- Sapore vocabulary: trattoria · Nonna · family · wood-fired oven ·
  cacio · guanciale · Cesanese · long table · covers · house wine.
  Gusto vocabulary: acts · tasting menu · sommelier · Michelin star ·
  cellar · maître · private.

Differentiation contract vs Brace EN (street-modern):
- Brace EN = black-pill street-food brutalist Bologna register with
  order-now flows. Sapore EN = warm rustic editorial with a rosso-casa
  accent and reservation flows.
"""
from __future__ import annotations

from typing import Any


SAPORE_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Home",                  "kind": "home"},
        {"slug": "menu",     "label": "Menu",                  "kind": "menu"},
        {"slug": "storia",   "label": "Our story",             "kind": "about"},
        {"slug": "forno",    "label": "Wood-fired oven",       "kind": "signature"},
        {"slug": "eventi",   "label": "Group dinners",         "kind": "events"},
        {"slug": "contatti", "label": "Find us & book",        "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "R",
        "logo_word":    "Trattoria Da Nonna Rosa",
        "tag":          "Family trattoria · Trastevere · since 1987",
        "phone":        "06 581 4488",
        "phone_tel":    "+390658144880",
        "whatsapp":     "06 581 4488",
        "whatsapp_link": "https://wa.me/390658144880",
        "email":        "ciao@trattoriadanonnarosa.it",
        "address":      "Via dei Salumi 16/a · 00153 Roma · Trastevere",
        "hours_compact": "Tue – Sat · 12:30 – 15:00 · 19:00 – 23:30",
        "hours_footer_rows": [
            "Sunday · lunch only · 12:30 – 15:00",
            "Monday · closed",
        ],
        "license":      "VAT IT 07634211006 · CCIAA Roma REA 1138992",
        "footer_intro":
            "A family trattoria opened in 1987 by Rosa Trezzi. Pasta rolled out "
            "by hand every morning on the mattarello, pizza from the wood-fired "
            "oven every evening, a glass of house wine on us when you come back a "
            "second time. Sixty covers, two dining rooms, three generations in "
            "the kitchen.",
        "nav_cta":      "Book a table",
        "nav_cta_href": "contatti",
        "nav_phone_cta": "Call: 06 581 4488",
        "star_line":    "Family trattoria · since 1987",
        "copyright":    "© 2026 Trattoria Da Nonna Rosa · VAT IT 07634211006",

        # Mirror the fine-dining _base.html footer keys used by the chrome
        "footer_hours_1": "Tue – Sat · lunch & dinner",
        "footer_hours_2": "Sunday · lunch only",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Family trattoria · Trastevere · since 1987",
        "headline": "At Nonna Rosa's, <em>like family.</em>",
        "intro":
            "Pasta rolled out by hand every morning on the mattarello, pizza from "
            "the wood-fired oven every evening, and a glass of house wine on us "
            "when you come back a second time. Sixty covers, two rooms, three "
            "generations in the kitchen.",
        "primary_cta":   "Book a table",
        "primary_href":  "contatti",
        "secondary_cta": "Message us on WhatsApp",
        "secondary_href_is_whatsapp": True,

        # Hero photo-frame
        "hero_image":   "https://images.unsplash.com/photo-1481931098730-318b6f776db0?w=1600&q=80&auto=format&fit=crop",
        "hero_caption": "Tuesday's Cacio e pepe · tonnarelli rolled by hand",
        "hero_stamp":   "Since 1987",

        # Facts band — 3 numbers/claims
        "facts": [
            ("1987",   "the year Rosa opened the kitchen"),
            ("60",     "covers across two rooms · no bookings after 8 pm"),
            ("3",      "generations of family in the kitchen"),
        ],

        # Chalkboard — 5 daily specials lun → ven
        "chalkboard_label":   "This week's chalkboard",
        "chalkboard_heading": "Today's dish, <em>written by hand.</em>",
        "chalkboard_intro":
            "Every morning Nonna Rosa chalks up the board at the counter, "
            "deciding on the spot what we'll be cooking that day. Here's how "
            "the week is shaping up.",
        "chalkboard_buongiorno": "Buon appetito!",
        "chalkboard_days": [
            ("Mon",  "Cacio e pepe",              "tonnarelli rolled by hand",                      "€ 10.00"),
            ("Tue",  "Bucatini all'amatriciana",  "Sarnelli guanciale from Amatrice",               "€ 11.00"),
            ("Wed",  "Coda alla vaccinara",       "Nonna Rosa's recipe, unchanged since 1987",      "€ 14.00"),
            ("Thu",  "Gnocchi al sugo d'arrosto", "made in the morning from old-stock potatoes",    "€ 11.00"),
            ("Fri",  "Baccalà in pastella",       "confit cherry tomatoes and Roman artichoke",     "€ 13.00"),
        ],

        # Family strip — 3 portraits with personal blurbs
        "family_label":   "The family in the kitchen",
        "family_heading": "Three generations, <em>one long table.</em>",
        "family": [
            {
                "name":   "Rosa Trezzi",
                "role":   "Fresh pasta since 1987",
                "blurb":
                    "Nonna Rosa opened the trattoria on 3 September 1987 with a "
                    "dream and two rolling pins. Today she is eighty-two and still "
                    "rolls the pasta every morning from seven onwards. Her motto is "
                    "simple: \"you can feel good pasta under your hands — you don't "
                    "need a scale.\"",
                "portrait": "https://images.unsplash.com/photo-1604908554027-b6e7c2c5db1f?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Marco Trezzi",
                "role":   "Pizzaiolo · wood-fired oven since 2003",
                "blurb":
                    "Rosa's son, raised between flour and bricks. He lights the "
                    "oven every afternoon at four — Cimino oak, nothing else — and "
                    "keeps it burning until midnight. His Margherita Verace was "
                    "learned from Peppe Guida in Vico Equense in 2008.",
                "portrait": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Giulia Trezzi",
                "role":   "Front of house & house desserts",
                "blurb":
                    "Rosa's granddaughter, thirty years old, looks after the dining "
                    "room and the sweets. Tiramisù with Sarnelli mascarpone, sour-"
                    "cherry crostata when the season allows, maritozzi with whipped "
                    "cream only on Saturday mornings. She'll greet you with a smile "
                    "and a jug of sparkling water.",
                "portrait": "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Forno teaser band
        "forno_label":   "The wood-fired oven",
        "forno_heading": "Lit every afternoon at <em>four on the dot.</em>",
        "forno_text":
            "Marco's dome oven is built from Viterbo brick, laid by hand in 2003 by "
            "the pizzaiolo Gennaro Esposito. It burns only Cimino oak, hits 420 °C "
            "and turns out a pizza in sixty seconds. Tuesday through Saturday, "
            "evenings only, once the first dining room has emptied out after lunch.",
        "forno_image":    "https://images.unsplash.com/photo-1593504049359-74330189a345?w=1200&q=80&auto=format&fit=crop",
        "forno_caption":  "Margherita Verace · 420 °C · sixty seconds",
        "forno_cta":      "Meet the pizza & pasta",
        "forno_cta_href": "forno",

        # Reviews band — 2–3 quotes
        "reviews_label": "What they say about us",
        "reviews": [
            {
                "quote":  "I felt like I was in the grandmother's kitchen I never had.",
                "author": "Gambero Rosso · Tre Spicchi 2024",
            },
            {
                "quote":  "One of the last real trattorias in Trastevere. Walk there, in the evening, and order the coda.",
                "author": "Corriere della Sera · Cook",
            },
            {
                "quote":  "Rosa's carbonara shuts everyone up — even the Testaccio crowd.",
                "author": "Puntarella Rossa · 2025",
            },
        ],

        # Hours strip — 3 rows under reviews
        "hours_label":  "When we're open",
        "hours_rows": [
            ("Tue – Sat",   "12:30 – 15:00", "lunch"),
            ("Tue – Sat",   "19:00 – 23:30", "dinner · wood-fired oven"),
            ("Sunday",      "12:30 – 15:00", "lunch only · last tables at 16:00"),
        ],
        "hours_note": "Closed Mondays · open every public holiday except Christmas Day",

        # Tavolata band — group experience teaser
        "tavolata_label":   "The long table",
        "tavolata_heading": "Twelve friends, <em>one single table.</em>",
        "tavolata_text":
            "The tavolata is our long twelve-seat table in the fireplace room. Fixed "
            "menu at thirty-two euro, house wine included, Giulia's desserts to close. "
            "For birthdays, christenings, school reunions — or simply because today "
            "is a good day to sit together.",
        "tavolata_cta":      "Put together a tavolata",
        "tavolata_cta_href": "eventi",
        "tavolata_image":    "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=1200&q=80&auto=format&fit=crop",

        # Final CTA band
        "cta_label":    "Come see us",
        "cta_heading":  "Via dei Salumi sixteen, <em>ring hard.</em>",
        "cta_intro":
            "We're on Via dei Salumi, two minutes from the Lungotevere. Green wooden "
            "door, loud bell — don't be shy, ring hard. We'll pour you a cold glass "
            "of Cesanese and slide out a slice of pizza rossa, straight from the oven.",
        "cta_primary":      "Book a table",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Message on WhatsApp",
    },

    # ─── MENU ────────────────────────────────────────────────────
    "menu": {
        "eyebrow":  "The menu · autumn '26 season",
        "headline": "Hand-rolled pasta, wood-fired pizza, <em>desserts from the house.</em>",
        "intro":
            "The menu shifts only a little — because the house dishes are the house "
            "dishes: Cacio e pepe, Amatriciana, Carbonara, Coda, Saltimbocca. The "
            "pizzas rotate with the season. Everything else Nonna Rosa decides at "
            "the counter, in the morning.",

        "wine_house_label":   "House wine",
        "wine_house_heading": "Cesanese del Lazio, <em>by the carafe, € 18.00 a litre.</em>",
        "wine_house_text":
            "The house wine comes from Olevano Romano, from the Proietti Riccardi "
            "estate, who have been making it for forty years. We serve it in "
            "litre, half-litre and quarter-litre carafes. The white: Malvasia "
            "Puntinata dei Castelli, from Cantina Ribelà — also by the carafe.",

        "allergen_note":
            "Dishes marked (G) contain gluten, (L) lactose, (P) fish. If you "
            "have a specific allergy, please ask at the counter before ordering: "
            "Rosa took the HACCP course back in 2019 and she knows everything.",

        "sections": [
            {
                "label": "House antipasti",
                "heading": "From the garden and the counter",
                "dishes": [
                    ("Bruschetta al pomodoro",        "Piennolo cherry tomatoes, basil, EVO Sabina DOP olive oil", "€ 7.00"),
                    ("Carciofo alla giudia",          "Roman artichoke, twice-fried, Amalfi lemon",                "€ 9.00"),
                    ("Supplì classico",               "rice, stringy mozzarella, house meat ragù",                 "€ 4.00"),
                    ("Fiori di zucca fritti",         "stuffed with mozzarella and anchovy, light batter",         "€ 8.00"),
                    ("Puntarelle alla romana",        "Cantabrian anchovies, garlic, red wine vinegar",            "€ 8.00"),
                    ("Tagliere of salumi & cheeses",  "Amatrice guanciale, Pecorino di Pienza, olives",            "€ 14.00"),
                    ("Polpette di Nonna Rosa",        "tomato sauce, country bread on the side",                   "€ 10.00"),
                ],
            },
            {
                "label": "Primi · pasta rolled by hand",
                "heading": "Off the morning mattarello",
                "dishes": [
                    ("Cacio e pepe",                  "tonnarelli rolled by hand, Pecorino di Pienza",             "€ 12.00"),
                    ("Carbonara classica",            "Amatrice guanciale, pecorino romano, 5 yolks",              "€ 13.00"),
                    ("Bucatini all'amatriciana",      "guanciale, San Marzano tomato, pecorino",                   "€ 12.00"),
                    ("Gnocchi al sugo d'arrosto",     "made in the morning, Rosa's Thursday gravy",                "€ 11.00"),
                    ("Fettuccine alla papalina",      "prosciutto crudo, fresh peas, eggs, parmigiano",            "€ 13.00"),
                    ("Rigatoni con la pajata",        "milk-fed veal intestine, tomato sauce",                     "€ 15.00"),
                    ("Tonnarelli cacio e tartufo",    "Norcia black truffle, pecorino, pepper",                    "€ 18.00"),
                ],
            },
            {
                "label": "Pizza from the wood-fired oven",
                "heading": "Evenings only · Tuesday → Saturday",
                "dishes": [
                    ("Margherita Verace",             "San Marzano tomato, fiordilatte, basil",                    "€ 9.00"),
                    ("Capricciosa di Nonna Rosa",     "artichokes, mushrooms, cooked ham, egg",                    "€ 12.00"),
                    ("Diavola al guanciale",          "tomato, fiordilatte, spicy salami, guanciale",              "€ 11.00"),
                    ("Bianca al cacio e pepe",        "fiordilatte, pecorino, Pondichéry black pepper",            "€ 10.00"),
                    ("Nonna Rosa (house signature)",  "Andria stracciatella, semi-dry cherry tomatoes, basil",     "€ 13.00"),
                    ("Zucca e salsiccia",             "pumpkin purée, Norcia sausage, rosemary",                   "€ 12.00"),
                ],
            },
            {
                "label": "Secondi from the counter",
                "heading": "Out of Sunday's kitchen",
                "dishes": [
                    ("Saltimbocca alla romana",       "veal, prosciutto crudo, sage, white wine",                  "€ 16.00"),
                    ("Coda alla vaccinara",           "oxtail, celery, cocoa, pine nuts, raisins",                 "€ 17.00"),
                    ("Abbacchio a scottadito",        "lamb chops, rosemary, lemon",                               "€ 19.00"),
                    ("Trippa alla romana",            "tripe, tomato sauce, wild mint, pecorino",                  "€ 14.00"),
                    ("Baccalà in pastella",           "creamed salt cod, light batter, cherry tomatoes",           "€ 14.00"),
                ],
            },
            {
                "label": "House desserts",
                "heading": "Giulia's hands",
                "dishes": [
                    ("Tiramisù di Giulia",            "Sarnelli mascarpone, savoiardi, stovetop-moka coffee",       "€ 6.00"),
                    ("Panna cotta alla vaniglia",     "with Nonna Rosa's sour cherries in syrup",                  "€ 5.00"),
                    ("Crostata di visciole",          "house shortcrust, sour cherries from the 2025 jar",         "€ 6.00"),
                    ("Maritozzo con la panna",        "Saturday mornings only · Valentini fresh cream",            "€ 4.00"),
                    ("Gelato del nonno",              "three scoops · fior di latte, hazelnut, chocolate",         "€ 5.00"),
                ],
            },
        ],
    },

    # ─── STORIA (about) ──────────────────────────────────────────
    "storia": {
        "eyebrow":  "Our story · since 1987",
        "headline": "Forty years of pasta <em>rolled on the mattarello.</em>",
        "intro":
            "Trattoria Da Nonna Rosa opened on 3 September 1987 in two rooms on "
            "Via dei Salumi, inherited from Rosa Trezzi's mother. Thirty years "
            "later, we're still here, in the same kitchen, with an oven more and "
            "three generations of family taking turns behind the counter.",

        "story": [
            "Rosa Trezzi was born in Roma in 1944, daughter of an innkeeper from "
            "Testaccio. She grew up among pots, rolling pins and the noise of the "
            "Porta Portese market. At fifteen she married Marino, who was a baker, "
            "and the two of them opened a first osteria on Via dei Foraggi. It "
            "lasted six years, until 1987, when Marino's father left them two rooms "
            "on Via dei Salumi, over in Trastevere.",

            "On 3 September 1987 the trattoria opened at number sixteen/a, with "
            "twelve covers, a gas oven and a single wall-mounted fridge. The menu "
            "that first evening was written in pen on a sheet of greaseproof "
            "paper: Cacio e pepe, Amatriciana, Coda alla vaccinara, and a "
            "tiramisù made with mascarpone from the dairy downstairs. Total cost "
            "of dinner: four thousand lire.",

            "In 2003 her son Marco took over the second room — the workshop of a "
            "carpenter who had retired — and built the wood-fired oven with the "
            "pizzaiolo Gennaro Esposito, who had come to Roma for a wedding. From "
            "that summer on, pizza joined the menu evenings only, Tuesdays and "
            "Saturdays. Then every evening, from 2005.",

            "In 2024 Giulia, Rosa's granddaughter, came home from Barcellona, "
            "where she was working in a pastry kitchen, and took over the dining "
            "room and the desserts. Today the trattoria has sixty covers, three "
            "generations, a wood-fired oven, one long-time waiter — Beppe, since "
            "1996 — and the same handwritten sign on the door: come back twice, "
            "the house wine's on us.",
        ],

        # Timeline — 3 steps
        "timeline_label":   "Three dates",
        "timeline": [
            {
                "year":  "1987",
                "title": "Rosa opens at number sixteen/a",
                "desc":  "Third of September, twelve covers, four thousand lire a head. The first menu written in pen on greaseproof paper.",
            },
            {
                "year":  "2003",
                "title": "Enter the wood-fired oven",
                "desc":  "Marco takes over the second room and builds the oven with Gennaro Esposito. First Margherita: the twenty-second of June.",
            },
            {
                "year":  "2024",
                "title": "Giulia comes home",
                "desc":  "Giulia returns from Barcellona and takes the dining room. First Saturday maritozzo: the twenty-sixth of October.",
            },
        ],

        # Family portraits (reused shape from home but with longer blurbs)
        "family_label":   "The hands that serve you",
        "family": [
            {
                "name":   "Rosa Trezzi",
                "role":   "Founder · fresh pasta since 1987",
                "blurb":
                    "Eighty-two, a grandchild for every finger on one hand, and a "
                    "mattarello she knows by heart. She rolls the pasta every morning "
                    "from seven to ten, then moves on to chalk up the board of the "
                    "day. Only she makes the carbonara: it's a jealous little ritual.",
                "portrait": "https://images.unsplash.com/photo-1604908554027-b6e7c2c5db1f?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Marco Trezzi",
                "role":   "Pizzaiolo · wood-fired oven since 2003",
                "blurb":
                    "Raised in the trattoria, a carpenter for three years, a "
                    "pizzaiolo for twenty-two. He lights the oven at four in the "
                    "afternoon, gets the Cimino oak crackling, and mixes the dough "
                    "by hand with a mother starter from 2008. He slides the "
                    "Margherita in with his eyes closed — sixty seconds.",
                "portrait": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Giulia Trezzi",
                "role":   "Front of house & desserts · since 2024",
                "blurb":
                    "Two years with Josep Maria in a Barcellona pastry kitchen, "
                    "then home. She runs the dining room alongside Beppe the "
                    "waiter, makes the desserts of the day, and writes the wine "
                    "list. She turns out the best maritozzo west of the Tiber — "
                    "but only on Saturday mornings.",
                "portrait": "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Valori grid — 4 cards
        "values_label":   "Our rules",
        "values_heading": "Four things <em>that never change.</em>",
        "values": [
            {
                "title": "The pasta dough",
                "desc":
                    "Flour from Molino Paolo Mariani, Roma tap water, egg yolks "
                    "from Paolo Parisi. Rolled on the mattarello every morning "
                    "from seven onwards. Never dried, never frozen, never from "
                    "yesterday.",
            },
            {
                "title": "The wood-fired oven",
                "desc":
                    "Cimino oak only, cut in Vitorchiano. Lit every afternoon at "
                    "four on the dot. If the oven doesn't hit 420 °C, that "
                    "evening the pizza doesn't leave the kitchen — full stop.",
            },
            {
                "title": "The house wine",
                "desc":
                    "Cesanese from Olevano Romano by Proietti Riccardi, Malvasia "
                    "from the Castelli by Cantina Ribelà. In a carafe, by the "
                    "litre. Eighteen euro — same price since 2019.",
            },
            {
                "title": "The glass rule",
                "desc":
                    "Come back a second time and the house wine's on us. It's "
                    "written on the board, it's been there since day one, we've "
                    "never changed it. Even if we recognise you, ask anyway.",
            },
        ],

        "photo_image":   "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1600&q=80&auto=format&fit=crop",
        "photo_caption": "The fireplace room · Saturday dinner · November 2025",
    },

    # ─── FORNO (signature · pizza & pasta) ────────────────────────
    "forno": {
        "eyebrow":  "Pizza & pasta · the house signatures",
        "headline": "Four pizzas and four pastas <em>written by hand.</em>",
        "intro":
            "Our signatures are eight — four out of the oven, four off the "
            "mattarello. They don't change, they don't scale, they don't "
            "rotate. They're the dishes Nonna Rosa laid down in 1987, the "
            "ones the family has staked its reputation on for forty years.",

        # Pizza section
        "pizza_label":   "From the wood-fired oven",
        "pizza_heading": "Four pizzas, <em>four house signatures.</em>",
        "pizza_intro":
            "Marco's wood-fired oven burns only Cimino oak, hits 420 °C and "
            "turns out a pizza in sixty seconds. A twenty-four-hour rise on a "
            "mother starter from 2008. San Marzano DOP tomato, Agerola "
            "fiordilatte from the Sorrentina dairy.",
        "pizza_signatures": [
            {
                "n":     "I",
                "name":  "Margherita Verace",
                "desc":  "San Marzano DOP tomato, Agerola fiordilatte, Genoese basil DOP, cold-pressed Sabina EVO oil.",
                "price": "€ 9.00",
            },
            {
                "n":     "II",
                "name":  "Capricciosa di Nonna Rosa",
                "desc":  "Sautéed Roman artichokes, champignon mushrooms, Prato cooked ham, organic Parisi egg in the middle.",
                "price": "€ 12.00",
            },
            {
                "n":     "III",
                "name":  "Diavola al guanciale",
                "desc":  "Tomato, fiordilatte, Amatrice spicy salami, Sarnelli guanciale, Diamante chilli.",
                "price": "€ 11.00",
            },
            {
                "n":     "IV",
                "name":  "Nonna Rosa (the house signature)",
                "desc":  "Andria stracciatella added raw, semi-dry cherry tomatoes, basil, Sabina EVO oil, Amalfi lemon zest.",
                "price": "€ 13.00",
            },
        ],

        # Pasta section
        "pasta_label":   "Off the mattarello",
        "pasta_heading": "Four pastas, <em>rolled by hand from seven on.</em>",
        "pasta_intro":
            "Pasta rolled on the mattarello every morning from seven to ten. "
            "Flour from Molino Paolo Mariani, Roma tap water, egg yolks from "
            "Paolo Parisi. Never dried, never frozen, never from yesterday.",
        "pasta_signatures": [
            {
                "n":     "I",
                "name":  "Cacio e pepe",
                "desc":  "Tonnarelli rolled on the mattarello, Pecorino di Pienza DOP, Pondichéry black pepper ground to order.",
                "price": "€ 12.00",
            },
            {
                "n":     "II",
                "name":  "Carbonara classica",
                "desc":  "Spaghetti, Amatrice guanciale, pecorino romano, five Parisi yolks, black pepper. No cream — ever.",
                "price": "€ 13.00",
            },
            {
                "n":     "III",
                "name":  "Bucatini all'amatriciana",
                "desc":  "Stone-milled bucatini, crisp Amatrice guanciale, San Marzano, pecorino romano grated at the table.",
                "price": "€ 12.00",
            },
            {
                "n":     "IV",
                "name":  "Fettuccine alla papalina",
                "desc":  "Fettuccine, San Daniele prosciutto crudo, fresh peas, eggs, thirty-six-month Parmigiano Reggiano.",
                "price": "€ 13.00",
            },
        ],

        # Forno story
        "forno_story_label":   "The wood-fired oven",
        "forno_story_heading": "Four hundred and twenty degrees, <em>sixty seconds.</em>",
        "forno_story_text_1":
            "Marco's dome oven was built by hand in 2003 by the pizzaiolo "
            "Gennaro Esposito — brick by brick, with Viterbo refractory clay. "
            "Two metres ten across, six pizzas at a time, 420 °C on a basket "
            "of Cimino oak cut in Vitorchiano.",
        "forno_story_text_2":
            "Lit every afternoon at four on the dot. If it hasn't reached "
            "temperature by six, that evening the pizza doesn't leave the "
            "kitchen — it's happened three times in twenty-two years, most "
            "recently during the February 2024 blizzard, and everyone ate "
            "pasta that night.",
        "forno_story_image":
            "https://images.unsplash.com/photo-1571997478779-2adcbbe9ab2f?w=1600&q=80&auto=format&fit=crop",
        "forno_story_caption": "Cimino oak · oven at 420 °C · July 2025",

        # Ingredients/producers band
        "producers_label":   "Five hands who sign with us",
        "producers_heading": "Where it comes from, <em>and from whom.</em>",
        "producers": [
            {
                "name":       "Sarnelli Guanciale",
                "place":      "Amatrice · Lazio",
                "ingredient": "Guanciale from Casertan black pig · 90-day cure",
            },
            {
                "name":       "Molino Paolo Mariani",
                "place":      "Barchi · Marche",
                "ingredient": "Type 0 and 00 flour · Senatore Cappelli wheat · stone-milled",
            },
            {
                "name":       "Proietti Riccardi",
                "place":      "Olevano Romano · Lazio",
                "ingredient": "Cesanese del Lazio by the carafe · bush-trained vines · 2024 vintage",
            },
            {
                "name":       "Caseificio Sorrentina",
                "place":      "Agerola · Campania",
                "ingredient": "Campanian buffalo fiordilatte · delivered daily",
            },
            {
                "name":       "Paolo Parisi",
                "place":      "Usigliano di Lari · Toscana",
                "ingredient": "Eggs from hens raised on goat's milk · deep-orange yolks",
            },
        ],

        # Dough photo
        "dough_image":   "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=1600&q=80&auto=format&fit=crop",
        "dough_caption": "Twenty-four-hour rise · mother starter from 2008",
    },

    # ─── EVENTI (events & tavolate) ──────────────────────────────
    "eventi": {
        "eyebrow":  "Long tables & events · groups of twelve to sixty",
        "headline": "One long table, <em>everyone sitting close.</em>",
        "intro":
            "The fireplace room opens up for long tables of twelve or more. Fixed "
            "menu, house wine included, Giulia's desserts to close. For birthdays, "
            "christenings, school reunions, bachelor parties, company dinners — or "
            "simply because being together feels good.",

        # 3 group experiences
        "experiences_label":   "Three formats",
        "meta_menu_label":     "Menu",
        "meta_wine_label":     "Wine",
        "experiences": [
            {
                "n":       "01",
                "title":   "The long table",
                "persons": "12 to 20 guests",
                "menu":    "Mixed antipasto, two pastas to choose from, main, dessert · € 32.00",
                "wine":    "House Cesanese and water included",
                "desc":
                    "Our oldest format: a long table in the fireplace room, "
                    "dishes to share, unhurried pace. Perfect for birthdays, "
                    "school reunions, bachelor parties. Book at least four "
                    "days ahead.",
            },
            {
                "n":       "02",
                "title":   "Christenings & first communions",
                "persons": "20 to 40 guests",
                "menu":    "Antipasto buffet, two pastas, two mains, cake · € 48.00",
                "wine":    "Cesanese + Malvasia + soft drinks included · sparkling separate",
                "desc":
                    "Both rooms opened up, children welcome, Giulia's cake "
                    "included (choose from three: ricotta and sour cherries, "
                    "chocolate and pear, vanilla millefeuille). Book two "
                    "weeks ahead.",
            },
            {
                "n":       "03",
                "title":   "Company dinner",
                "persons": "25 to 60 guests",
                "menu":    "Five-course tasting menu · € 62.00",
                "wine":    "Pairings from our house sommelier · four glasses",
                "desc":
                    "The whole trattoria privatised, one weeknight evening "
                    "(Tue–Thu). Menu in three languages if needed, projector "
                    "for presentations, free Wi-Fi. Book a month ahead.",
            },
        ],

        # Birthday/celebration block
        "birthday_label":   "Birthdays & anniversaries",
        "birthday_heading": "Giulia's cake, candles, <em>and a toast with Nonna Rosa.</em>",
        "birthday_text":
            "For every birthday, Giulia bakes a cake to order (tell us your "
            "favourite flavour two days ahead). We carry it out with the candles "
            "lit, Nonna Rosa steps out of the kitchen for the toast, and — if "
            "you're lucky — she even sings you a verse of Roma nun fa' la stupida "
            "stasera. But only if you ask her yourself, because she never does it "
            "for us.",
        "birthday_image":   "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=1200&q=80&auto=format&fit=crop",
        "birthday_caption": "Ricotta and sour-cherry cake · Beppe's sixtieth birthday",

        # Contact card specific to events
        "contact_label":    "To put a long table together",
        "contact_heading":  "Speak directly <em>with Giulia.</em>",
        "contact_text":
            "Giulia handles the long tables and the events herself. Call her "
            "between ten and noon (that's the hour before she's back in the "
            "dining room) or message her on WhatsApp — she'll reply by the "
            "afternoon. Email also works, if that's easier.",
        "contact_phone":    "06 581 4488",
        "contact_whatsapp": "06 581 4488",
        "contact_email":    "eventi@trattoriadanonnarosa.it",
        "contact_cta":      "Write to Giulia",
        "contact_cta_href": "contatti",
    },

    # ─── CONTATTI (reservations + find us) ────────────────────────
    "contatti": {
        "eyebrow":  "Find us & book · Via dei Salumi 16/a",
        "headline": "Book a table, <em>or just walk in.</em>",
        "intro":
            "We're on Via dei Salumi, in Trastevere, a five-minute walk from the "
            "Lungotevere. Two or three of you? No need to book — just come in, "
            "we'll find you a table. From four up, a call the day before is "
            "better. Groups of twelve or more, head over to the long-tables page.",

        # Address card
        "address_label":   "Where we are",
        "address_heading": "Via dei Salumi 16/a",
        "address_text":
            "In Trastevere, between Piazza dei Mercanti and the Lungotevere Ripa. "
            "Green wooden door, loud bell. Metro line B, Circo Massimo stop (ten "
            "minutes on foot), tram 8 Belli stop (four minutes), bus H Sonnino stop.",
        "address_city":    "00153 Roma · Trastevere",

        # Hours table — 4 rows
        "hours_label":   "Opening hours",
        "hours_heading": "Lunch & dinner, <em>closed Mondays.</em>",
        "hours_table": [
            ("Tuesday – Saturday", "12:30 – 15:00",         "lunch"),
            ("Tuesday – Saturday", "19:00 – 23:30",         "dinner · wood-fired oven on"),
            ("Sunday",             "12:30 – 15:00",         "lunch only · last tables at 16:00"),
            ("Monday",             "closed",                "weekly rest day"),
        ],

        # Phone/WhatsApp/email card
        "contact_label":     "Talk to us",
        "contact_heading":   "Three ways, <em>all of them good.</em>",
        "contact_phone_label":    "Call the counter",
        "contact_phone_value":    "06 581 4488",
        "contact_phone_hours":    "Giulia picks up from 10:00 to 23:00",
        "contact_whatsapp_label": "Message on WhatsApp",
        "contact_whatsapp_value": "06 581 4488",
        "contact_whatsapp_hours": "We reply within the hour",
        "contact_email_label":    "Send us an email",
        "contact_email_value":    "ciao@trattoriadanonnarosa.it",
        "contact_email_hours":    "We reply by the next day",

        # Reservation form
        "form_label":    "Book online",
        "form_heading":  "Book a table, <em>we'll chalk you up.</em>",
        "form_intro":
            "Fill in the form below. You'll get a confirmation by SMS or WhatsApp "
            "within two hours (we're in the kitchen, but we keep an eye on the "
            "phones). For groups of twelve or more, message us on WhatsApp "
            "directly.",

        "form_sections": [
            {
                "num":   "01",
                "title": "Who you are",
                "meta":  "So we can confirm your table",
                "fields": ["name", "email", "phone"],
            },
            {
                "num":   "02",
                "title": "When you're coming",
                "meta":  "Date, time and how many of you",
                "fields": ["date", "time", "people"],
            },
            {
                "num":   "03",
                "title": "Notes",
                "meta":  "Occasion, allergies, preferences",
                "fields": ["occasion", "notes"],
            },
        ],

        "form_fields": [
            {
                "name":     "name",
                "label":    "Name and surname",
                "type":     "text",
                "placeholder": "What we'll call you at the table",
                "required": True,
                "helper":   "We chalk it on the bookings board.",
            },
            {
                "name":     "email",
                "label":    "Email",
                "type":     "email",
                "placeholder": "name@example.com",
                "required": True,
                "helper":   "We'll send your confirmation here.",
            },
            {
                "name":     "phone",
                "label":    "Phone or WhatsApp",
                "type":     "tel",
                "placeholder": "+39 333 123 45 67",
                "required": True,
                "helper":   "Only used if something unexpected comes up.",
            },
            {
                "name":     "date",
                "label":    "Date",
                "type":     "date",
                "placeholder": "dd/mm/yyyy",
                "required": True,
                "helper":   "We're closed on Mondays.",
            },
            {
                "name":     "time",
                "label":    "Time",
                "type":     "time",
                "placeholder": "e.g. 20:30",
                "required": True,
                "helper":   "Lunch 12:30–14:30 · dinner 19:00–22:30.",
            },
            {
                "name":     "people",
                "label":    "How many of you",
                "type":     "number",
                "placeholder": "number of covers",
                "required": True,
                "helper":   "More than twelve? Message us on WhatsApp instead.",
            },
            {
                "name":     "occasion",
                "label":    "Occasion",
                "type":     "select",
                "placeholder": "",
                "required": False,
                "full_width": True,
                "helper":   "If it's a birthday, we'll get Giulia's cake ready.",
            },
            {
                "name":     "notes",
                "label":    "Notes for the kitchen",
                "type":     "textarea",
                "placeholder": "Allergies, favourite dishes, special requests…",
                "required": False,
                "full_width": True,
                "helper":   "Nonna Rosa took the HACCP course in 2019 — just tell us.",
            },
        ],

        "occasion_options": [
            "Regular dinner",
            "Birthday",
            "Anniversary",
            "Work dinner",
            "First time with us",
            "Long table (12+)",
            "Other",
        ],

        "consent":
            "I agree to my data being processed to handle the booking "
            "(no newsletter, no marketing, ever).",
        "form_submit":      "Book the table",
        "form_submit_note": "We'll confirm within two hours, by SMS or WhatsApp.",

        # Map
        "map_label":    "On the map",
        "map_heading":  "Via dei Salumi 16/a · Trastevere",
        "map_embed":
            "https://www.openstreetmap.org/export/embed.html"
            "?bbox=12.4660%2C41.8880%2C12.4720%2C41.8910"
            "&layer=mapnik&marker=41.8893%2C12.4690",
        "map_link":     "Open in OpenStreetMap",
        "map_link_href":"https://www.openstreetmap.org/?mlat=41.8893&mlon=12.4690#map=17/41.8893/12.4690",

        # Getting-here notes
        "transport_label":   "How to get here",
        "transport_heading": "Three ways, <em>all on foot from the centre.</em>",
        "transport": [
            {
                "mode":  "Metro",
                "line":  "B · Circo Massimo stop",
                "note":  "Ten minutes on foot along Via di Monte Savello and the Lungotevere Ripa.",
            },
            {
                "mode":  "Tram",
                "line":  "8 · Belli stop",
                "note":  "Four minutes on foot, crossing Piazza Trilussa toward Via dei Salumi.",
            },
            {
                "mode":  "Bus",
                "line":  "H · Sonnino stop",
                "note":  "Six minutes on foot, through Piazza in Piscinula.",
            },
            {
                "mode":  "On foot from the centre",
                "line":  "Ponte Sisto · fifteen minutes",
                "note":  "From Piazza Navona, through Campo de' Fiori and over Ponte Sisto.",
            },
        ],
    },

    # No blog
    "posts": [],
}
