"""Brace — Brace Street Lab (street-modern archetype) — EN content tree.

Phase 2g3.6b — Restaurant live-completion EN rollout (Session 48, 2026-04-15).

Voice contract (EN):
- Native English street-food register. Reference voices: Eater city guides,
  Bon Appétit's BA Best Burgers, Vice Munchies Bologna, Time Out food.
- Direct second-person imperative ("order at the counter", "skip the line",
  "grab one before 11 pm"). Confident, urban, sharp, fast-casual.
- UPPERCASE display headlines (mirrors IT big-shoulders display vibe).
- Lowercase descriptions with short punch sentences. NO em-dash drama.
- Italian dish names stay Italian: Margherita, Marinara, Fritto misto,
  Mortadella e pistacchio, Cesanese. Parenthetical gloss only on first
  mention if obscure.
- Italian proper names stay Italian: Brace Street Lab, Bologna, Via
  Indipendenza, Tortellini, Macelleria Sarti, Forno Beretta, Tosi.
- Prices keep "€ 9.50" format. Hours "12:00 – 24:00". Tabular labels
  translate: "LUN – DOM" → "MON – SUN".

Differentiation contract (D-054):
- Sharply opposite register from:
  · Sapore EN (warm Roman trattoria food-writer reportage)
  · Gusto EN (Michelin editorial-chef register, tasting-menu concierge)
- Brace EN = urban street-food brutalist, price-grid driven, counter-queue
  energy, delivery partners marquee, smashburger / pizza al taglio flow.
"""
from __future__ import annotations

from typing import Any


BRACE_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Home",      "kind": "home"},
        {"slug": "menu",     "label": "Menu",      "kind": "menu"},
        {"slug": "lab",      "label": "The Lab",   "kind": "about"},
        {"slug": "moments",  "label": "Moments",   "kind": "gallery"},
        {"slug": "ordina",   "label": "Order",     "kind": "order"},
        {"slug": "contatti", "label": "Find us",   "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "B",
        "logo_word":    "BRACE STREET LAB",
        "tag":          "Bologna · Via Indipendenza 42 · 12:00 → 24:00",
        "phone":        "051 234 5566",
        "phone_tel":    "+390512345566",
        "phone_display": "051 234 5566",
        "whatsapp":     "051 234 5566",
        "whatsapp_link": "https://wa.me/390512345566",
        "email":        "orders@bracestreetlab.it",
        "address":      "Via Indipendenza 42 · 40121 Bologna",
        "hours_compact": "EVERY DAY · 12:00 – 24:00 · FRI/SAT UNTIL 01:30",
        "hours_footer_rows": [
            "MON – THU · 12:00 – 24:00",
            "FRI – SAT · 12:00 – 01:30",
            "SUN · 12:00 – 24:00",
        ],
        "license":      "VAT IT 04127880371 · CCIAA Bologna REA 358912",
        "footer_intro":
            "Street-food lab in Bologna. Smashburgers on Piemontese scottona, "
            "fries fired to order, pizza al taglio from the wood oven. Order "
            "at the counter, pick up by number, eat on the fly. Open late, "
            "every day, Sundays too.",
        "nav_cta":      "ORDER NOW",
        "nav_cta_href": "ordina",
        "nav_phone_cta": "051 234 5566",
        "star_line":    "STREET FOOD LAB · BOLOGNA",
        "copyright":    "© 2026 Brace Street Lab · VAT IT 04127880371",

        # Mirror the fine-dining/_base.html footer keys used by the chrome
        "footer_hours_1": "MON – THU · 12:00 – 24:00",
        "footer_hours_2": "FRI – SAT · 12:00 – 01:30",

        # Social
        "instagram_handle": "@brace.lab",
        "instagram_link":   "https://instagram.com/brace.lab",
        "tiktok_handle":    "@brace.bologna",
        "tiktok_link":      "https://tiktok.com/@brace.bologna",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "STREET FOOD LAB · BOLOGNA",
        "headline": 'FIRED ON <em>LIVE FLAME.</em>',
        "intro":
            "Smashburgers on Piemontese scottona, fries against the grain, pizza al "
            "taglio from the wood oven. Order at the counter, pick up by number, eat on the fly.",
        "primary_cta":   "ORDER NOW",
        "primary_href":  "ordina",
        "secondary_cta": "SEE THE MENU",
        "secondary_href": "menu",

        # Hero product cutout
        "hero_image":       "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=1400&q=80&auto=format&fit=crop",
        "hero_alt":         "Doppio Brace smashburger close-up",
        "hero_badge_price": "€ 9.50",
        "hero_badge_label": "DOPPIO BRACE",
        "hero_badge_tag":   "TOP",

        # Real-time queue counter strip
        "counter_label": "COUNTER QUEUE",
        "counter_value": "≈ 4 MIN",
        "counter_kitchen_label": "KITCHEN OPEN",
        "counter_kitchen_value": "UNTIL 24:00",
        "counter_last_label":    "LAST ORDER",
        "counter_last_value":    "23:30",

        # Stat band — 4 numbers
        "stats_label": "THE LAB IN NUMBERS",
        "stats": [
            ("12,000",  "BURGERS / MONTH"),
            ("4.9 ★",   "OVER 1,380 REVIEWS"),
            ("100%",    "PIEMONTESE SCOTTONA"),
            ("420°C",   "WOOD OVEN"),
        ],

        # Menu strip — 6 product-grid items on home (teaser of full menu)
        "menu_strip_label":   "FROM THE COUNTER TONIGHT",
        "menu_strip_heading": 'THE MENU <em>ON THE FLY.</em>',
        "menu_strip_intro":
            "Six pieces coming hot off the pass every fifteen minutes. "
            "Point, pick, pay at the counter, we call you by number.",
        "menu_strip_cta":      "SEE THE FULL MENU",
        "menu_strip_cta_href": "menu",
        "menu_strip_items": [
            {
                "name":  "DOPPIO BRACE",
                "desc":  "double scottona, melted cheddar, house brace sauce",
                "price": "€ 9.50",
                "tag":   "TOP",
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "SMASH CLASSICO",
                "desc":  "single scottona, cheddar, caramelised onion",
                "price": "€ 7.50",
                "tag":   "",
                "image": "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "FRITTO MISTO",
                "desc":  "fries, battered jalapeños, fried baccalà",
                "price": "€ 6.00",
                "tag":   "SPICY",
                "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "PIZZA ROSSA",
                "desc":  "San Marzano DOP tomato, fior di latte, basil",
                "price": "€ 4.50",
                "tag":   "VEG",
                "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "FRIES BRACE",
                "desc":  "double-fried potatoes, coarse salt, brace sauce",
                "price": "€ 4.50",
                "tag":   "",
                "image": "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "SODA BRACE",
                "desc":  "house lemonade with fresh basil",
                "price": "€ 3.00",
                "tag":   "NEW",
                "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Delivery partners marquee strip
        "delivery_label":    "ORDER ANY WAY YOU WANT",
        "delivery_subtitle": "DELIVERY IN 30 MINUTES · DOWNTOWN BOLOGNA",
        "delivery_partners": [
            ("GLOVO",     "30 MIN", "MIN € 12"),
            ("DELIVEROO", "25 MIN", "MIN € 10"),
            ("JUST EAT",  "35 MIN", "MIN € 15"),
            ("UBER EATS", "30 MIN", "MIN € 12"),
        ],

        # Lab manifesto — 3 short bold paragraphs
        "manifesto_label":   "THE LAB",
        "manifesto_heading": 'WHY FIRE. <em>WHY ON THE FLY.</em>',
        "manifesto_paragraphs": [
            "Brace is a lab. No wallpaper, no tablecloths. Just steel, fire "
            "and five people working in plain sight, one hundred and eighty "
            "seconds per plate.",

            "We only use Piemontese scottona, ground over the counter every "
            "morning. Every potato is hand-cut at ten. Every sauce is built "
            "inside the lab, never bought in.",

            "Come whenever you want. Open noon to midnight, every day, "
            "Sundays too. Saturday we push until 01:30. The kitchen never "
            "closes before the last person through the door.",
        ],
        "manifesto_cta":      "SEE THE LAB",
        "manifesto_cta_href": "lab",

        # Crew band — 3 people (chef, griller, founder)
        "crew_label":   "THE CREW",
        "crew_heading": 'FIVE AT THE COUNTER. <em>ONE CREW.</em>',
        "crew": [
            {
                "name":   "DARIO RIVA",
                "role":   "FOUNDER & GRILLER",
                "quote":  "«A good smash is hot steel, cold scottona, ninety seconds and nothing else.»",
                "portrait": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "AMINA BERETTA",
                "role":   "PIZZAIOLA · WOOD OVEN",
                "quote":  "«The oven needs attention every two minutes. That's why I never look at my phone.»",
                "portrait": "https://images.unsplash.com/photo-1554727242-741c14fa561c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "LUKA HOXHA",
                "role":   "FRIES & SAUCES",
                "quote":  "«I sign off on the brace mayo. No secret, just patience.»",
                "portrait": "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Urban photo strip — 3 atmosphere shots
        "atmo_label":   "THE ATMOSPHERE",
        "atmo_heading": 'COUNTER. NEON. <em>QUEUE.</em>',
        "atmo_strip": [
            {
                "image": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=900&q=80&auto=format&fit=crop",
                "cap":   "Counter queue · 19:40 on a Saturday night",
            },
            {
                "image": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=900&q=80&auto=format&fit=crop",
                "cap":   "Late-night DJ set · last Friday of every month",
            },
            {
                "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=900&q=80&auto=format&fit=crop",
                "cap":   "Wood oven fired from 11:00 until close",
            },
        ],

        # Final CTA band — late-night order push
        "final_label":   "READY TO ORDER?",
        "final_heading": 'LAST ORDER <em>AT 23:30.</em>',
        "final_intro":
            "Three ways to get us on your plate. Come to the counter. Call "
            "for takeaway. Order through our delivery partners. Move fast.",
        "final_primary_cta":   "ORDER NOW",
        "final_primary_href":  "ordina",
        "final_phone_cta":     "CALL 051 234 5566",
        "final_phone_href":    "+390512345566",
    },

    # ─── MENU ────────────────────────────────────────────────────
    "menu": {
        "eyebrow":  "MENU · FROM THE COUNTER",
        "headline": 'EVERYTHING <em>WE FIRE.</em>',
        "intro":
            "Five sections, twenty-two pieces, counter prices. Point a finger, "
            "pay, we call you by number. No cover charge, no service fee.",

        "sections": [
            {
                "id":    "burger",
                "label": "01",
                "title": "BURGERS",
                "desc":  "Piemontese scottona · ground every morning · brioche bun on burnt-wheat flour",
                "items": [
                    {
                        "name":  "DOPPIO BRACE",
                        "desc":  "double scottona, melted cheddar, brace sauce, raw onion",
                        "price": "€ 9.50",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "SMASH CLASSICO",
                        "desc":  "single scottona, cheddar, caramelised onion, house sauce",
                        "price": "€ 7.50",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "VEGGIE PATTY",
                        "desc":  "lentil and beetroot patty, lemon hummus, rocket",
                        "price": "€ 8.00",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BRACE PICCANTE",
                        "desc":  "scottona, fried jalapeños, spicy cheddar, brace sriracha",
                        "price": "€ 9.00",
                        "tag":   "SPICY",
                        "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "fritti",
                "label": "02",
                "title": "FRIES",
                "desc":  "hand-cut at 10:00 · double-fried · Cervia sea salt",
                "items": [
                    {
                        "name":  "FRIES BRACE",
                        "desc":  "double-fried potatoes, coarse salt, brace sauce in a cup",
                        "price": "€ 4.50",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "FRITTO MISTO",
                        "desc":  "fries, battered jalapeños, fried baccalà, onion rings",
                        "price": "€ 6.00",
                        "tag":   "SPICY",
                        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "JALAPEÑO POPPER",
                        "desc":  "jalapeños stuffed with cheddar, breaded, fried, lime dip",
                        "price": "€ 5.50",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "ONION RINGS",
                        "desc":  "Tropea red onion rings in tempura, house bbq",
                        "price": "€ 5.00",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "pizza",
                "label": "03",
                "title": "PIZZA AL TAGLIO",
                "desc":  "72-hour cold ferment · wood oven at 420°C · sixty seconds to bake",
                "items": [
                    {
                        "name":  "PIZZA ROSSA",
                        "desc":  "San Marzano DOP tomato, fior di latte, basil",
                        "price": "€ 4.50",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BIANCA AL TARTUFO",
                        "desc":  "fior di latte, summer black truffle shavings, evo oil",
                        "price": "€ 6.50",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "DIAVOLA NEW",
                        "desc":  "tomato, fior di latte, spicy Calabrese salami, honey drizzle",
                        "price": "€ 5.50",
                        "tag":   "SPICY",
                        "image": "https://images.unsplash.com/photo-1593504049359-74330189a345?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "MORTADELLA & PISTACCHIO",
                        "desc":  "fior di latte, Mortadella di Bologna IGP, Bronte pistachio",
                        "price": "€ 6.00",
                        "tag":   "NEW",
                        "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "drink",
                "label": "04",
                "title": "SODAS & DRINKS",
                "desc":  "house sodas pressed at the counter · Bolognese beers on tap · wine by the glass",
                "items": [
                    {
                        "name":  "SODA BRACE",
                        "desc":  "house lemonade with fresh basil and ginger",
                        "price": "€ 3.00",
                        "tag":   "NEW",
                        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "ICED TEA HOUSE",
                        "desc":  "Earl Grey iced tea with chestnut honey and lemon zest",
                        "price": "€ 3.00",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BIRRA SPINA",
                        "desc":  "Bolognese lager from Birrificio Sant'Orsola · 0.33l",
                        "price": "€ 4.50",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "WINE BY THE GLASS",
                        "desc":  "Sangiovese di Romagna DOC · Cantina Ronchi di Solarolo",
                        "price": "€ 5.00",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "dolci",
                "label": "05",
                "title": "SWEETS",
                "desc":  "made inside the lab · small portions, to eat on the fly",
                "items": [
                    {
                        "name":  "BRACE COOKIE",
                        "desc":  "cocoa cookie with a still-warm nutella core",
                        "price": "€ 3.50",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "ARTISAN GELATO",
                        "desc":  "fior di panna or pistachio · supplied by Gelateria Stefino",
                        "price": "€ 3.00",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "TIRAMISÙ ON THE FLY",
                        "desc":  "in a jar, fresh mascarpone, savoiardi, Bolognese coffee",
                        "price": "€ 4.00",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
        ],

        # Allergen line at bottom
        "allergen_label": "ALLERGENS",
        "allergen_text":
            "All dishes are cooked in a space that handles gluten, dairy, eggs, "
            "soy, tree nuts. For serious intolerances talk to the counter before "
            "you order. Full allergen list available at the counter.",

        # Producer band — 3 producer names with city
        "producers_label":   "OUR SUPPLIERS",
        "producers_heading": 'WHERE EVERY <em>PIECE COMES FROM.</em>',
        "producers_intro":
            "We work with three long-time suppliers in town. Every product is "
            "signed off, traceable, delivered in small weekly batches.",
        "producers": [
            {
                "name":   "MACELLERIA SARTI",
                "city":   "BOLOGNA · VIA PETRONI",
                "role":   "Piemontese scottona, ground fresh every morning at seven.",
            },
            {
                "name":   "FORNO BERETTA",
                "city":   "MODENA · CASTELFRANCO",
                "role":   "Burnt-wheat brioche buns and 72-hour pizza dough.",
            },
            {
                "name":   "ORTOFRUTTA TOSI",
                "city":   "BOLOGNA · MERCATO ALBANI",
                "role":   "Potatoes, Tropea red onions, greenhouse jalapeños.",
            },
        ],

        # Final CTA
        "final_label":         "ORDER NOW",
        "final_heading":       'POINT. <em>PAY. PICK UP.</em>',
        "final_primary_cta":   "ORDER NOW",
        "final_primary_href":  "ordina",
        "final_secondary_cta": "FIND US",
        "final_secondary_href": "contatti",
    },

    # ─── LAB (about) ─────────────────────────────────────────────
    "lab": {
        "eyebrow":  "THE LAB",
        "headline": 'WHY FIRE. <em>WHY ON THE FLY.</em>',
        "intro":
            "Brace is a lab, open every day from noon to midnight. Five people, "
            "one counter, two ovens. Nothing more, nothing less.",

        # Big atmosphere photo
        "hero_image":   "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1600&q=80&auto=format&fit=crop",
        "hero_caption": "Open counter · wood oven at 420°C · every shift starts here",

        # Manifesto — 4 short bold paragraphs
        "manifesto_label":   "MANIFESTO",
        "manifesto_paragraphs": [
            {
                "title": "01 DOUGH",
                "text":  "Sourdough starter refreshed every twelve hours. Type 1 flours "
                         "stone-milled by Forno Beretta in Castelfranco. Seventy-two hours "
                         "of slow cold ferment, never less. You feel the pizza on your "
                         "fingers before your mouth.",
            },
            {
                "title": "02 FIRE",
                "text":  "The wood oven burns only Cimino oak, nothing else. It hits "
                         "420°C in thirty-five minutes. The grill plate runs at 280°C: "
                         "Piemontese scottona goes down, pressed with the iron, ninety "
                         "seconds per side.",
            },
            {
                "title": "03 MATTER",
                "text":  "Only Piemontese scottona from Macelleria Sarti, ground over "
                         "the counter every morning at seven. Tosi potatoes hand-cut at "
                         "ten. San Marzano DOP tomato from the Agro Sarnese. Everything "
                         "signed off, everything traceable.",
            },
            {
                "title": "04 SPEED",
                "text":  "Three minutes from counter to pass. Fourteen seconds to flip "
                         "a smash. Sixty seconds for a pizza. One hundred and eighty "
                         "seconds total service. Fast, yes, but made the right way.",
            },
        ],

        # Process strip — 3-step
        "process_label":   "THE PROCESS",
        "process_heading": "THREE MOVES. <em>NOTHING ELSE.</em>",
        "process": [
            {
                "num":   "01",
                "title": "DOUGH",
                "desc":  "every night at 23:00, 72h ferment in the cell at 4°C",
            },
            {
                "num":   "02",
                "title": "FIRE",
                "desc":  "oven lit at 11:00, grill plate at 280°C from 12:00",
            },
            {
                "num":   "03",
                "title": "SERVICE",
                "desc":  "three minutes from counter to pass, we call you by number",
            },
        ],

        # Crew band — 4 people
        "crew_label":   "THE FULL CREW",
        "crew_heading": 'FIVE AT THE COUNTER. <em>ONE CREW.</em>',
        "crew": [
            {
                "name":   "DARIO RIVA",
                "role":   "FOUNDER & GRILLER",
                "quote":  "«A good smash is hot steel, cold scottona, ninety seconds and nothing else.»",
                "portrait": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "AMINA BERETTA",
                "role":   "PIZZAIOLA · WOOD OVEN",
                "quote":  "«The oven needs attention every two minutes. That's why I never look at my phone.»",
                "portrait": "https://images.unsplash.com/photo-1554727242-741c14fa561c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "LUKA HOXHA",
                "role":   "FRIES & SAUCES",
                "quote":  "«I sign off on the brace mayo. No secret, just patience.»",
                "portrait": "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "SOFIA MARTINI",
                "role":   "COUNTER & SHIFTS",
                "quote":  "«If I've seen you twice, I call you by name. House rule.»",
                "portrait": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Values grid — 4 cards
        "values_label":   "OUR VALUES",
        "values_heading": "FOUR THINGS <em>WE DON'T NEGOTIATE.</em>",
        "values": [
            {"title": "TIME",        "tag": "ZERO WAIT",      "desc": "three minutes counter to pass, every time"},
            {"title": "TEMPERATURE", "tag": "420°C / 280°C",  "desc": "oven and grill in plain sight, never less"},
            {"title": "QUALITY",     "tag": "100% PIEMONTE",  "desc": "scottona signed off, traceable, morning-ground"},
            {"title": "ENERGY",      "tag": "EVERY DAY",      "desc": "open noon to midnight, Sundays too"},
        ],

        # Kitchen energy band
        "kitchen_label":   "THE SPEC SHEET",
        "kitchen_heading": 'THE KITCHEN <em>IN NUMBERS.</em>',
        "kitchen_specs": [
            ("210°C", "SMASH PLATE"),
            ("420°C", "WOOD OVEN"),
            ("14 SEC", "SMASH FLIP"),
            ("90 SEC", "PIZZA BAKE"),
            ("3 MIN", "COUNTER TO PASS"),
            ("72 HRS", "DOUGH FERMENT"),
        ],

        # Final CTA
        "final_label":   "COME SEE IT",
        "final_heading": 'THE LAB <em>NEVER CLOSES.</em>',
        "final_intro":
            "Open noon to midnight, every day. Come whenever you want, point "
            "a finger, pay at the counter. No reservations, no cover charge.",
        "final_primary_cta":   "SEE THE MENU",
        "final_primary_href":  "menu",
        "final_secondary_cta": "FIND US",
        "final_secondary_href": "contatti",
    },

    # ─── MOMENTS (gallery) ───────────────────────────────────────
    "moments": {
        "eyebrow":  "MOMENTS · STREET DIARY",
        "headline": 'EVERY NIGHT <em>A MOMENT.</em>',
        "intro":
            "Brace's photo diary. Counter queue, late-night DJ, fries on "
            "fire, crew at work. All shot here, by us.",

        # Category pills
        "categories_label": "FILTER",
        "categories_all_label": "ALL",
        "categories": [
            "DJ NIGHTS",
            "COUNTER QUEUE",
            "LATE NIGHT",
            "FRY MOMENTS",
            "CREW",
            "OPENING",
        ],

        # 6-image grid
        "grid": [
            {
                "image":    "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-001",
                "cap":      "Counter queue · Saturday 23:14 · eighty people down Via Indipendenza",
                "tag":      "COUNTER QUEUE",
            },
            {
                "image":    "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-002",
                "cap":      "DJ Tito Brama · last Friday set · vinyl only until 02:00",
                "tag":      "DJ NIGHTS",
            },
            {
                "image":    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-003",
                "cap":      "Wood oven · 420°C · eleventh hour of service",
                "tag":      "LATE NIGHT",
            },
            {
                "image":    "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-004",
                "cap":      "Double-fried potatoes · Cervia salt · ready in three hundred seconds",
                "tag":      "FRY MOMENTS",
            },
            {
                "image":    "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-005",
                "cap":      "Luka on the pass · Friday 20:34 · seventh cover of the night",
                "tag":      "CREW",
            },
            {
                "image":    "https://images.unsplash.com/photo-1567521464027-f127ff144326?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-006",
                "cap":      "Opening · March 13, 2024 · first guest through the counter at 12:01",
                "tag":      "OPENING",
            },
        ],

        # Featured shot with quote overlay
        "featured_image": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1600&q=80&auto=format&fit=crop",
        "featured_quote": "«Brace is the spot you go to when you want to eat well and fast, and nobody asks you what you do for a living.»",
        "featured_author": "ZERO MAGAZINE · BOLOGNA · MARCH 2025",
        "featured_filename": "MO-FEAT-002",

        # End CTA
        "final_label":     "SEE THE REST",
        "final_heading":   'FOLLOW US <em>ON SOCIAL.</em>',
        "final_intro":
            "Every day a new story, every Friday the drop of the week. "
            "Instagram for the diary, TikTok for what happens behind the counter.",
        "final_instagram_cta": "INSTAGRAM @brace.lab",
        "final_tiktok_cta":    "TIKTOK @brace.bologna",
    },

    # ─── ORDINA ──────────────────────────────────────────────────
    "ordina": {
        "eyebrow":  "ORDER ON THE FLY",
        "headline": 'THREE WAYS. <em>ONE PLATE.</em>',
        "intro":
            "Come to the counter, call for takeaway, order through our "
            "delivery partners. We call you by number when it's ready, never before.",

        # Counter-status band
        "counter_status_label":  "COUNTER STATUS",
        "counter_queue_label":   "COUNTER QUEUE",
        "counter_queue_value":   "≈ 4 MIN",
        "counter_kitchen_label": "KITCHEN OPEN",
        "counter_kitchen_value": "UNTIL 24:00",
        "counter_last_label":    "LAST ORDER",
        "counter_last_value":    "23:30",

        # 3-route grid — counter / takeaway / delivery
        "routes_label":   "THREE ROUTES",
        "routes_heading": 'PICK <em>HOW YOU ORDER.</em>',
        "routes": [
            {
                "id":      "01",
                "title":   "AT THE COUNTER",
                "subtitle": "COME AND POINT",
                "desc":
                    "Via Indipendenza 42, Bologna. Point a finger at the menu, pay at "
                    "the counter, we call you by number when it's ready. No reservations, "
                    "no cover charge, no service fee. Three minutes from pass to plate.",
                "lines": [
                    ("ADDRESS",    "Via Indipendenza 42, Bologna"),
                    ("QUEUE ETA",  "≈ 4 MIN"),
                    ("HOURS",      "12:00 – 24:00 · every day"),
                ],
                "cta_label": "OPEN MAP",
                "cta_href":  "https://www.openstreetmap.org/?mlat=44.4949&mlon=11.3426#map=17/44.4949/11.3426",
                "cta_kind":  "external",
            },
            {
                "id":      "02",
                "title":   "TAKEAWAY",
                "subtitle": "CALL AND COLLECT",
                "desc":
                    "Call the counter, tell us what you want, we'll give you a pickup "
                    "time. Ready in twelve minutes, always. Pay on pickup, cash or card. "
                    "WhatsApp if you'd rather type.",
                "lines": [
                    ("PHONE",     "051 234 5566"),
                    ("WHATSAPP",  "Text 051 234 5566"),
                    ("READY IN",  "12 MIN"),
                ],
                "cta_label": "CALL NOW",
                "cta_href":  "+390512345566",
                "cta_kind":  "tel",
            },
            {
                "id":      "03",
                "title":   "DELIVERY",
                "subtitle": "TO YOUR DOOR",
                "desc":
                    "Four delivery partners, all across central Bologna. Minimum "
                    "order ten euros, delivery in thirty minutes, free over twenty "
                    "euros. Open whichever app you use most.",
                "lines": [
                    ("PARTNERS",   "GLOVO · DELIVEROO · JUST EAT · UBER EATS"),
                    ("ZONE",       "Downtown Bologna · 4 km radius"),
                    ("MIN ORDER",  "€ 10"),
                ],
                "cta_label": "SEE THE PARTNERS",
                "cta_href":  "#partners",
                "cta_kind":  "anchor",
            },
        ],

        # Delivery partners detail
        "partners_label":   "DELIVERY PARTNERS",
        "partners_heading": 'DELIVERY IN <em>30 MINUTES.</em>',
        "partners": [
            {"name": "GLOVO",     "eta": "30 MIN", "min": "MIN € 12", "zone": "Downtown Bologna · 4 km"},
            {"name": "DELIVEROO", "eta": "25 MIN", "min": "MIN € 10", "zone": "Downtown Bologna · 3 km"},
            {"name": "JUST EAT",  "eta": "35 MIN", "min": "MIN € 15", "zone": "Bologna · 6 km"},
            {"name": "UBER EATS", "eta": "30 MIN", "min": "MIN € 12", "zone": "Downtown Bologna · 5 km"},
        ],

        # Late-night opening hours table
        "hours_label":   "WHEN WE'RE OPEN",
        "hours_heading": 'SUNDAYS <em>TOO.</em>',
        "hours_rows": [
            ("MON", "12:00 – 24:00"),
            ("TUE", "12:00 – 24:00"),
            ("WED", "12:00 – 24:00"),
            ("THU", "12:00 – 24:00"),
            ("FRI", "12:00 – 01:30"),
            ("SAT", "12:00 – 01:30"),
            ("SUN", "12:00 – 24:00"),
        ],
        "hours_note":
            "Last order always 30 minutes before close. The kitchen only closes early "
            "if the pizza dough runs out, never before midnight.",

        # Allergen note
        "allergen_label": "ALLERGENS",
        "allergen_text":
            "All dishes are cooked in a space that handles gluten, dairy, eggs, "
            "soy, tree nuts. For serious intolerances talk to the counter before "
            "you order or message us on WhatsApp.",

        # Big phone CTA band
        "phone_label":   "READY NOW",
        "phone_heading": 'CALL US <em>AT THE COUNTER.</em>',
        "phone_intro":
            "Three rings to answer, even mid-service. If we don't pick up, we're "
            "flipping a smash. Try again in thirty seconds.",
        "phone_cta_label": "CALL 051 234 5566",
        "phone_cta_href":  "+390512345566",

        # FAQ accordion — 4 questions
        "faq_label":   "FREQUENTLY ASKED",
        "faq_heading": 'THINGS <em>PEOPLE ASK A LOT.</em>',
        "faq": [
            {
                "q": "DO YOU HAVE GLUTEN-FREE OPTIONS?",
                "a": "Gluten-free brioche bun on request, we need thirty extra minutes "
                     "of wait time. Let the counter know before you order. Potatoes, "
                     "meat and sauces are naturally gluten-free, but cooked in the "
                     "same space. For serious intolerances talk to the counter first.",
            },
            {
                "q": "DO YOU TAKE GROUP RESERVATIONS?",
                "a": "No reserved covers, no reservations. For groups above twelve, "
                     "message us on WhatsApp two days ahead: we'll tell you if we can "
                     "fit you in a quieter slot (usually Tue/Wed at 19:00).",
            },
            {
                "q": "DO YOU HAVE VEG AND VEGAN OPTIONS?",
                "a": "Yes, three veg options on the counter at all times: lentil "
                     "veggie patty, pizza rossa, fries brace. Vegan options (dairy-free) "
                     "rotate weekly — ask the counter what's on today.",
            },
            {
                "q": "DO YOU DO CATERING OR PRIVATE EVENTS?",
                "a": "Yes, from twenty to sixty people. Smashburgers, pizza al taglio, "
                     "fries, house sodas. Mobile oven for events in Bologna and province. "
                     "Email events@bracestreetlab.it with date, place, headcount — we "
                     "reply within 24 hours with a quote.",
            },
        ],
    },

    # ─── CONTATTI ────────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "FIND US · BOLOGNA",
        "headline": 'VIA INDIPENDENZA <em>42.</em>',
        "intro":
            "Central Bologna, two steps from the Due Torri. Open every day, "
            "Sundays too, until late. Walk over if you can.",

        # Address card
        "address_label": "ADDRESS",
        "address_value": "Via Indipendenza 42 · 40121 Bologna",
        "address_note":  "Between Piazza Maggiore and the station · pedestrian zone",

        # Map iframe
        "map_lat":   "44.4949",
        "map_lon":   "11.3426",
        "map_zoom":  "16",
        "map_label": "OpenStreetMap · Via Indipendenza 42, Bologna",

        # Contact channels grid
        "channels_label": "TALK TO THE COUNTER",
        "channels": [
            {
                "icon":  "phone",
                "label": "PHONE",
                "value": "051 234 5566",
                "note":  "three rings to answer, even mid-service",
                "href":  "+390512345566",
                "kind":  "tel",
            },
            {
                "icon":  "whatsapp",
                "label": "WHATSAPP",
                "value": "051 234 5566",
                "note":  "text us if you prefer, we reply within 30 minutes",
                "href":  "https://wa.me/390512345566",
                "kind":  "external",
            },
            {
                "icon":  "email",
                "label": "EMAIL",
                "value": "orders@bracestreetlab.it",
                "note":  "for catering, events, suppliers",
                "href":  "orders@bracestreetlab.it",
                "kind":  "mail",
            },
        ],

        # Hours grid (compact)
        "hours_label": "OPENING HOURS",
        "hours_rows": [
            ("MON – THU", "12:00 – 24:00"),
            ("FRI – SAT", "12:00 – 01:30"),
            ("SUNDAY",    "12:00 – 24:00"),
        ],
        "hours_note": "Last order 30 minutes before close · kitchen always live",

        # Transport note
        "transport_label": "HOW TO GET HERE",
        "transport_rows": [
            ("BUS",      "lines 11, 14, 27 · Indipendenza stop"),
            ("TRAIN",    "Bologna Centrale · 8-minute walk"),
            ("PARKING",  "Riva di Reno · 4-minute walk"),
            ("BIKE",     "rack on Via dell'Indipendenza"),
        ],

        # Jobs band
        "jobs_label":    "WORK WITH US",
        "jobs_heading":  'HIRING <em>FIVE PEOPLE.</em>',
        "jobs_intro":
            "Brace is growing. We open a second lab in Modena by summer 2026. "
            "We need real people, not perfect CVs.",
        "jobs": [
            {"role": "GRILLER",        "type": "FULL TIME", "city": "BOLOGNA"},
            {"role": "PIZZAIOLO",      "type": "PART TIME", "city": "BOLOGNA"},
            {"role": "RUNNER & COUNTER", "type": "WEEKENDS", "city": "BOLOGNA"},
        ],
        "jobs_cta_label": "SEND A MESSAGE",
        "jobs_cta_href":  "jobs@bracestreetlab.it",

        # Social block
        "social_label": "FOLLOW US",
        "social": [
            {"platform": "INSTAGRAM", "handle": "@brace.lab",      "href": "https://instagram.com/brace.lab"},
            {"platform": "TIKTOK",    "handle": "@brace.bologna",  "href": "https://tiktok.com/@brace.bologna"},
        ],

        # Mini reservation/inquiry form
        "form_label":   "WRITE TO US",
        "form_heading": 'TWO LINES <em>ARE ENOUGH.</em>',
        "form_intro":
            "For catering, groups above twelve, suppliers. To order, message "
            "us on WhatsApp — it's faster.",
        "form_field_name":     "Name",
        "form_field_email":    "Email",
        "form_field_phone":    "Phone",
        "form_field_message":  "What you need",
        "form_field_message_placeholder": "Catering, event, supply, other…",
        "form_submit_label":   "SEND",
        "form_submit_note":
            "Demo form · nothing will be sent. To order for real, call "
            "051 234 5566 or message us on WhatsApp.",
    },

    # No blog on Brace
    "posts": [],
}
