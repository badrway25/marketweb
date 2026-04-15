"""Brace — Brace Street Lab (street-modern archetype) — IT content tree.

Phase 2g3.6 — Restaurant live-completion (Session 48, 2026-04-15).

Voice contract (IT):
- Bologna street-food register, second-person direct, imperative.
- "ordina", "scegli", "non aspettare", short rolling punch sentences.
- UPPERCASE display headlines, lowercase descriptions.
- NO em-dash editorial drama. Periods + comma rhythm, fast-casual.
- Numerics: "€ 9.50" with euro symbol + space. Hours "12:00 – 24:00".
- Mono-font reads on technical labels (queue time, ETA, kitchen specs).

Differentiation contract vs Gusto (D-054 enforcement):
- Brace is brutalist near-black + neon yellow + flame red. Big Shoulders
  Display condensed UPPERCASE. Product-cutout heroes with PRICE BADGES.
  Gusto is editorial dark with Playfair italic drama, plated tasting-menu
  photography, sommelier registers, concierge tile.
- Brace conversion path: ORDER NOW (delivery + takeaway + counter queue).
  Gusto conversion path: appointment-only concierge booking.
- Brace vocabulary: brace · fuoco · scottona · banco · fritti · al volo ·
  consegna · coda · drop · neon. Gusto vocabulary: portata · degustazione
  · sommelier · stella · maître · cantina · privè.

Differentiation contract vs Sapore (trattoria-warm):
- Brace is dark + neon yellow + lab-energy. Sapore is warm cream paper
  + rosso casa + family chalkboard.
- Brace photography: smashburger close-cutouts, fries flying, urban
  brick + neon, late-night counter queue, DJ booth, kitchen filaments.
  Sapore photography: hands on dough, family tavolata, terracotta plates
  in sunlight, forno a legna burning. Pools must NOT overlap.
- Brace flow: order-now (price grids + AGGIUNGI buttons + delivery
  partners marquee). Sapore flow: reservation (chalkboard daily menu +
  family portraits + WhatsApp prenota un tavolo).
"""
from __future__ import annotations

from typing import Any


BRACE_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Home",      "kind": "home"},
        {"slug": "menu",     "label": "Menu",      "kind": "menu"},
        {"slug": "lab",      "label": "Il Lab",    "kind": "about"},
        {"slug": "moments",  "label": "Moments",   "kind": "gallery"},
        {"slug": "ordina",   "label": "Ordina",    "kind": "order"},
        {"slug": "contatti", "label": "Trovaci",   "kind": "contact"},
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
        "email":        "ordini@bracestreetlab.it",
        "address":      "Via Indipendenza 42 · 40121 Bologna",
        "hours_compact": "OGNI GIORNO · 12:00 – 24:00 · VEN/SAB FINO ALL'01:30",
        "hours_footer_rows": [
            "LUN – GIO · 12:00 – 24:00",
            "VEN – SAB · 12:00 – 01:30",
            "DOM · 12:00 – 24:00",
        ],
        "license":      "P.IVA 04127880371 · CCIAA Bologna REA 358912",
        "footer_intro":
            "Street food lab a Bologna. Smashburger di scottona piemontese, "
            "fritti scottati al momento, pizza al taglio dal forno a legna. "
            "Ordini al banco, ritiri al numero, divori al volo. Aperti fino "
            "a tardi, ogni giorno, anche la domenica.",
        "nav_cta":      "ORDINA ORA",
        "nav_cta_href": "ordina",
        "nav_phone_cta": "051 234 5566",
        "star_line":    "STREET FOOD LAB · BOLOGNA",
        "copyright":    "© 2026 Brace Street Lab · P.IVA 04127880371",

        # Mirror the fine-dining/_base.html footer keys used by the chrome
        "footer_hours_1": "LUN – GIO · 12:00 – 24:00",
        "footer_hours_2": "VEN – SAB · 12:00 – 01:30",

        # Social
        "instagram_handle": "@brace.lab",
        "instagram_link":   "https://instagram.com/brace.lab",
        "tiktok_handle":    "@brace.bologna",
        "tiktok_link":      "https://tiktok.com/@brace.bologna",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "STREET FOOD LAB · BOLOGNA",
        "headline": 'BRUCIATO AL <em>FUOCO VIVO.</em>',
        "intro":
            "Smashburger di scottona piemontese, fritti contro corrente, pizza al "
            "taglio dal forno a legna. Ordini al banco, ritiri al numero, divori al volo.",
        "primary_cta":   "ORDINA ORA",
        "primary_href":  "ordina",
        "secondary_cta": "VEDI IL MENU",
        "secondary_href": "menu",

        # Hero product cutout
        "hero_image":       "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=1400&q=80&auto=format&fit=crop",
        "hero_alt":         "Doppio Brace smashburger close-up",
        "hero_badge_price": "€ 9.50",
        "hero_badge_label": "DOPPIO BRACE",
        "hero_badge_tag":   "TOP",

        # Real-time queue counter strip
        "counter_label": "CODA AL BANCO",
        "counter_value": "≈ 4 MIN",
        "counter_kitchen_label": "CUCINA APERTA",
        "counter_kitchen_value": "FINO ALLE 24:00",
        "counter_last_label":    "ULTIMO ORDINE",
        "counter_last_value":    "23:30",

        # Stat band — 4 numbers
        "stats_label": "I NUMERI DEL LAB",
        "stats": [
            ("12.000",  "BURGER / MESE"),
            ("4.9 ★",   "SU 1.380 RECENSIONI"),
            ("100%",    "SCOTTONA PIEMONTESE"),
            ("420°C",   "FORNO A LEGNA"),
        ],

        # Menu strip — 6 product-grid items on home (teaser of full menu)
        "menu_strip_label":   "DAL BANCO STASERA",
        "menu_strip_heading": 'IL MENU <em>DEL VOLO.</em>',
        "menu_strip_intro":
            "Sei pezzi che escono caldi dal pass ogni quindici minuti. "
            "Punta, scegli, paga al banco, ti chiamiamo al numero.",
        "menu_strip_cta":      "VEDI TUTTO IL MENU",
        "menu_strip_cta_href": "menu",
        "menu_strip_items": [
            {
                "name":  "DOPPIO BRACE",
                "desc":  "doppia scottona, cheddar fuso, salsa brace",
                "price": "€ 9.50",
                "tag":   "TOP",
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "SMASH CLASSICO",
                "desc":  "scottona singola, cheddar, cipolla caramellata",
                "price": "€ 7.50",
                "tag":   "",
                "image": "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "FRITTO MISTO",
                "desc":  "patate, jalapeño impanati, baccalà fritto",
                "price": "€ 6.00",
                "tag":   "PICCANTE",
                "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "PIZZA ROSSA",
                "desc":  "pomodoro san marzano dop, fior di latte, basilico",
                "price": "€ 4.50",
                "tag":   "VEG",
                "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "FRIES BRACE",
                "desc":  "patate doppia frittura, sale grosso, salsa brace",
                "price": "€ 4.50",
                "tag":   "",
                "image": "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "SODA BRACE",
                "desc":  "limonata fatta in casa con basilico fresco",
                "price": "€ 3.00",
                "tag":   "NEW",
                "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Delivery partners marquee strip
        "delivery_label":    "ORDINA DOVE VUOI",
        "delivery_subtitle": "CONSEGNA IN 30 MINUTI · BOLOGNA CENTRO",
        "delivery_partners": [
            ("GLOVO",     "30 MIN", "MIN € 12"),
            ("DELIVEROO", "25 MIN", "MIN € 10"),
            ("JUST EAT",  "35 MIN", "MIN € 15"),
            ("UBER EATS", "30 MIN", "MIN € 12"),
        ],

        # Lab manifesto — 3 short bold paragraphs
        "manifesto_label":   "IL LAB",
        "manifesto_heading": 'PERCHÉ FUOCO. <em>PERCHÉ VOLO.</em>',
        "manifesto_paragraphs": [
            "Brace è un laboratorio. Niente carta da parati, niente tovaglie. "
            "Solo ferro, fuoco e cinque persone che lavorano a vista per "
            "centottanta secondi a piatto.",

            "Lavoriamo solo scottona piemontese, macinata al mattino con il grano "
            "sopra il banco. Ogni patata viene tagliata a mano alle dieci. Ogni "
            "salsa è fatta dentro il lab, mai comprata.",

            "Vieni quando vuoi. Aperti dalle dodici a mezzanotte, ogni giorno, "
            "anche la domenica. Il sabato si tira fino all'una e mezza. La cucina "
            "non chiude prima dell'ultimo che entra.",
        ],
        "manifesto_cta":      "SCOPRI IL LAB",
        "manifesto_cta_href": "lab",

        # Crew band — 3 people (chef, griller, founder)
        "crew_label":   "LA CREW",
        "crew_heading": 'CINQUE AL BANCO. <em>UNA SOLA SQUADRA.</em>',
        "crew": [
            {
                "name":   "DARIO RIVA",
                "role":   "FONDATORE & GRILLER",
                "quote":  "«Una smash buona è ferro caldo, scottona fredda, novanta secondi e basta.»",
                "portrait": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "AMINA BERETTA",
                "role":   "PIZZAIOLA · FORNO A LEGNA",
                "quote":  "«Il forno chiede attenzione ogni due minuti. Per questo non guardo il telefono.»",
                "portrait": "https://images.unsplash.com/photo-1554727242-741c14fa561c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "LUKA HOXHA",
                "role":   "FRITTI & SALSE",
                "quote":  "«La maionese alla brace la firmo io. Nessun segreto, solo paziensa.»",
                "portrait": "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Urban photo strip — 3 atmosphere shots
        "atmo_label":   "L'ATMOSFERA",
        "atmo_heading": 'BANCO. NEON. <em>CODA.</em>',
        "atmo_strip": [
            {
                "image": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=900&q=80&auto=format&fit=crop",
                "cap":   "Coda al banco · 19:40 di un sabato sera",
            },
            {
                "image": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=900&q=80&auto=format&fit=crop",
                "cap":   "Late-night DJ set · ogni ultimo venerdì del mese",
            },
            {
                "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=900&q=80&auto=format&fit=crop",
                "cap":   "Forno a legna acceso dalle 11:00 fino a chiusura",
            },
        ],

        # Final CTA band — late-night order push
        "final_label":   "PRONTO A ORDINARE?",
        "final_heading": 'ULTIMO ORDINE <em>ALLE 23:30.</em>',
        "final_intro":
            "Tre modi per averci nel piatto. Vieni al banco. Chiama per il "
            "takeaway. Ordina con i partner di consegna. Fai presto.",
        "final_primary_cta":   "ORDINA ADESSO",
        "final_primary_href":  "ordina",
        "final_phone_cta":     "CHIAMA 051 234 5566",
        "final_phone_href":    "+390512345566",
    },

    # ─── MENU ────────────────────────────────────────────────────
    "menu": {
        "eyebrow":  "MENU · DAL BANCO",
        "headline": 'TUTTO QUELLO <em>CHE SI BRUCIA.</em>',
        "intro":
            "Cinque sezioni, ventidue pezzi, prezzi al banco. Punta col dito, "
            "paga, ti chiamiamo al numero. Niente coperto, niente servizio.",

        "sections": [
            {
                "id":    "burger",
                "label": "01",
                "title": "BURGER",
                "desc":  "scottona piemontese · macinata al mattino · pane brioche di grano arso",
                "items": [
                    {
                        "name":  "DOPPIO BRACE",
                        "desc":  "doppia scottona, cheddar fuso, salsa brace, cipolla cruda",
                        "price": "€ 9.50",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "SMASH CLASSICO",
                        "desc":  "scottona singola, cheddar, cipolla caramellata, salsa house",
                        "price": "€ 7.50",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "VEGGIE PATTY",
                        "desc":  "patty di lenticchie e barbabietola, hummus al limone, rucola",
                        "price": "€ 8.00",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BRACE PICCANTE",
                        "desc":  "scottona, jalapeño fritti, cheddar piccante, sriracha brace",
                        "price": "€ 9.00",
                        "tag":   "PICCANTE",
                        "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "fritti",
                "label": "02",
                "title": "FRITTI",
                "desc":  "patate tagliate a mano alle 10:00 · doppia frittura · sale di Cervia",
                "items": [
                    {
                        "name":  "FRIES BRACE",
                        "desc":  "patate doppia frittura, sale grosso, salsa brace in coppetta",
                        "price": "€ 4.50",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "FRITTO MISTO",
                        "desc":  "patate, jalapeño impanati, baccalà fritto, anelli di cipolla",
                        "price": "€ 6.00",
                        "tag":   "PICCANTE",
                        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "JALAPEÑO POPPER",
                        "desc":  "jalapeño ripieni di cheddar, panati, fritti, salsa al lime",
                        "price": "€ 5.50",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "ONION RINGS",
                        "desc":  "anelli di cipolla rossa di tropea in tempura, bbq house",
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
                "desc":  "impasto a 72 ore · forno a legna 420°C · sessanta secondi di cottura",
                "items": [
                    {
                        "name":  "PIZZA ROSSA",
                        "desc":  "pomodoro san marzano dop, fior di latte, basilico",
                        "price": "€ 4.50",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BIANCA AL TARTUFO",
                        "desc":  "fior di latte, scaglie di tartufo nero estivo, olio evo",
                        "price": "€ 6.50",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "DIAVOLA NEW",
                        "desc":  "pomodoro, fior di latte, salame piccante calabrese, miele",
                        "price": "€ 5.50",
                        "tag":   "PICCANTE",
                        "image": "https://images.unsplash.com/photo-1593504049359-74330189a345?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "MORTADELLA & PISTACCHIO",
                        "desc":  "fior di latte, mortadella di bologna igp, pistacchio bronte",
                        "price": "€ 6.00",
                        "tag":   "NEW",
                        "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "drink",
                "label": "04",
                "title": "SODA & BEVANDE",
                "desc":  "soda house pressate al banco · birre di bologna alla spina · vino al calice",
                "items": [
                    {
                        "name":  "SODA BRACE",
                        "desc":  "limonata fatta in casa con basilico fresco e zenzero",
                        "price": "€ 3.00",
                        "tag":   "NEW",
                        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "ICED TEA HOUSE",
                        "desc":  "tè freddo earl grey con miele di castagno e scorza limone",
                        "price": "€ 3.00",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BIRRA SPINA",
                        "desc":  "lager bolognese del birrificio sant'orsola · 0,33l",
                        "price": "€ 4.50",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "VINO AL CALICE",
                        "desc":  "sangiovese di romagna doc · cantina ronchi di solarolo",
                        "price": "€ 5.00",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "dolci",
                "label": "05",
                "title": "DOLCI",
                "desc":  "fatti dentro il lab · porzioni piccole, da mangiare al volo",
                "items": [
                    {
                        "name":  "BRACE COOKIE",
                        "desc":  "cookie al cacao con cuore di nutella ancora caldo",
                        "price": "€ 3.50",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "GELATO ARTIGIANALE",
                        "desc":  "fior di panna o pistacchio · fornito da gelateria stefino",
                        "price": "€ 3.00",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "TIRAMISÙ AL VOLO",
                        "desc":  "in vasetto, mascarpone fresco, savoiardi, caffè bolognese",
                        "price": "€ 4.00",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
        ],

        # Allergen line at bottom
        "allergen_label": "ALLERGENI",
        "allergen_text":
            "Tutti i piatti sono cucinati in un ambiente che lavora glutine, latticini, "
            "uova, soia, frutta a guscio. Per intolleranze gravi parla col banco prima "
            "di ordinare. Lista allergeni completa disponibile al banco.",

        # Producer band — 3 producer names with city
        "producers_label":   "I FORNITORI",
        "producers_heading": 'DA CHI ARRIVA <em>OGNI COSA.</em>',
        "producers_intro":
            "Lavoriamo con tre fornitori storici della città. Ogni prodotto firmato, "
            "tracciato, in piccoli lotti settimanali.",
        "producers": [
            {
                "name":   "MACELLERIA SARTI",
                "city":   "BOLOGNA · VIA PETRONI",
                "role":   "Scottona piemontese, macinata fresca ogni mattina alle sette.",
            },
            {
                "name":   "FORNO BERETTA",
                "city":   "MODENA · CASTELFRANCO",
                "role":   "Pane brioche di grano arso e impasto pizza a 72 ore.",
            },
            {
                "name":   "ORTOFRUTTA TOSI",
                "city":   "BOLOGNA · MERCATO ALBANI",
                "role":   "Patate, cipolle rosse di tropea, jalapeño coltivati in serra.",
            },
        ],

        # Final CTA
        "final_label":         "ORDINA SUBITO",
        "final_heading":       'PUNTA. <em>PAGA. RITIRA.</em>',
        "final_primary_cta":   "ORDINA ORA",
        "final_primary_href":  "ordina",
        "final_secondary_cta": "TROVACI",
        "final_secondary_href": "contatti",
    },

    # ─── LAB (about) ─────────────────────────────────────────────
    "lab": {
        "eyebrow":  "IL LAB",
        "headline": 'PERCHÉ IL FUOCO. <em>PERCHÉ IL VOLO.</em>',
        "intro":
            "Brace è un laboratorio aperto ogni giorno dalle dodici a mezzanotte. "
            "Cinque persone, un banco, due forni. Niente di più, niente di meno.",

        # Big atmosphere photo
        "hero_image":   "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1600&q=80&auto=format&fit=crop",
        "hero_caption": "Il banco aperto · forno a legna a 420°C · ogni servizio inizia qui",

        # Manifesto — 4 short bold paragraphs
        "manifesto_label":   "MANIFESTO",
        "manifesto_paragraphs": [
            {
                "title": "01 IMPASTO",
                "text":  "Lievito madre rinnovato ogni dodici ore. Farine di tipo 1 macinate a "
                         "pietra dal forno Beretta di Castelfranco. Settantadue ore di lievitazione "
                         "lenta in cella, mai meno. La pizza si sente sulle dita prima che in bocca.",
            },
            {
                "title": "02 FUOCO",
                "text":  "Il forno a legna brucia solo quercia del Cimino, mai altro. Raggiunge i "
                         "420°C in trentacinque minuti. La piastra del grill arriva a 280°C: "
                         "scottona piemontese giù, schiacciata col ferro, novanta secondi a faccia.",
            },
            {
                "title": "03 MATERIA",
                "text":  "Solo scottona piemontese di Macelleria Sarti, macinata sopra il banco "
                         "ogni mattina alle sette. Patate Tosi tagliate a mano alle dieci. "
                         "Pomodoro san marzano dop dell'Agro Sarnese. Tutto firmato, tutto tracciato.",
            },
            {
                "title": "04 VELOCITÀ",
                "text":  "Tre minuti dal banco al pass. Quattordici secondi per girare lo smash. "
                         "Sessanta secondi per la pizza. Centottanta secondi totali di servizio. "
                         "Veloci sì, ma fatti come si deve.",
            },
        ],

        # Process strip — 3-step
        "process_label":   "IL PROCESSO",
        "process_heading": "TRE GESTI. <em>NIENT'ALTRO.</em>",
        "process": [
            {
                "num":   "01",
                "title": "IMPASTO",
                "desc":  "ogni notte alle 23:00, lievitazione 72h in cella a 4°C",
            },
            {
                "num":   "02",
                "title": "FUOCO",
                "desc":  "forno acceso alle 11:00, piastra a 280°C dalle 12:00",
            },
            {
                "num":   "03",
                "title": "SERVIZIO",
                "desc":  "tre minuti dal banco al pass, ti chiamiamo al numero",
            },
        ],

        # Crew band — 4 people
        "crew_label":   "LA CREW AL COMPLETO",
        "crew_heading": 'CINQUE AL BANCO. <em>UNA SOLA SQUADRA.</em>',
        "crew": [
            {
                "name":   "DARIO RIVA",
                "role":   "FONDATORE & GRILLER",
                "quote":  "«Una smash buona è ferro caldo, scottona fredda, novanta secondi e basta.»",
                "portrait": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "AMINA BERETTA",
                "role":   "PIZZAIOLA · FORNO A LEGNA",
                "quote":  "«Il forno chiede attenzione ogni due minuti. Per questo non guardo il telefono.»",
                "portrait": "https://images.unsplash.com/photo-1554727242-741c14fa561c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "LUKA HOXHA",
                "role":   "FRITTI & SALSE",
                "quote":  "«La maionese alla brace la firmo io. Nessun segreto, solo paziensa.»",
                "portrait": "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "SOFIA MARTINI",
                "role":   "BANCO & TURNI",
                "quote":  "«Ti chiamo per nome se ci sei già stata due volte. È la regola della casa.»",
                "portrait": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Values grid — 4 cards
        "values_label":   "I VALORI",
        "values_heading": 'QUATTRO COSE <em>NON NEGOZIABILI.</em>',
        "values": [
            {"title": "TEMPO",       "tag": "ZERO ATTESA",    "desc": "tre minuti dal banco al pass, sempre"},
            {"title": "TEMPERATURA", "tag": "420°C / 280°C",  "desc": "forno e piastra controllati a vista, mai meno"},
            {"title": "QUALITÀ",     "tag": "100% PIEMONTE",  "desc": "scottona firmata, tracciata, macinata al mattino"},
            {"title": "ENERGIA",     "tag": "OGNI GIORNO",    "desc": "aperti dalle 12 a mezzanotte, anche la domenica"},
        ],

        # Kitchen energy band
        "kitchen_label":   "LA SCHEDA TECNICA",
        "kitchen_heading": 'I NUMERI <em>DELLA CUCINA.</em>',
        "kitchen_specs": [
            ("210°C", "PIASTRA SMASH"),
            ("420°C", "FORNO A LEGNA"),
            ("14 SEC", "FLIP DELLO SMASH"),
            ("90 SEC", "COTTURA PIZZA"),
            ("3 MIN", "BANCO AL PASS"),
            ("72 ORE", "LIEVITAZIONE"),
        ],

        # Final CTA
        "final_label":   "VIENI A VEDERLO",
        "final_heading": 'IL LAB È <em>SEMPRE APERTO.</em>',
        "final_intro":
            "Aperti dalle dodici a mezzanotte, ogni giorno. Vieni quando vuoi, "
            "punta col dito, paga al banco. Niente prenotazioni, niente coperto.",
        "final_primary_cta":   "VEDI IL MENU",
        "final_primary_href":  "menu",
        "final_secondary_cta": "TROVACI",
        "final_secondary_href": "contatti",
    },

    # ─── MOMENTS (gallery) ───────────────────────────────────────
    "moments": {
        "eyebrow":  "MOMENTS · STREET DIARY",
        "headline": 'OGNI SERA <em>UN MOMENTO.</em>',
        "intro":
            "Il diario fotografico di Brace. Coda al banco, late-night DJ, "
            "frittura in fiamme, crew al lavoro. Tutto scattato qui, da noi.",

        # Category pills
        "categories_label": "FILTRA",
        "categories_all_label": "TUTTI",
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
                "cap":      "Coda al banco · sabato 23:14 · ottanta persone in via Indipendenza",
                "tag":      "COUNTER QUEUE",
            },
            {
                "image":    "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-002",
                "cap":      "DJ Tito Brama · last friday set · vinile only fino alle 02:00",
                "tag":      "DJ NIGHTS",
            },
            {
                "image":    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-003",
                "cap":      "Forno a legna · 420°C · undicesima ora di servizio",
                "tag":      "LATE NIGHT",
            },
            {
                "image":    "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-004",
                "cap":      "Doppia frittura patate · sale di Cervia · pronto in trecento secondi",
                "tag":      "FRY MOMENTS",
            },
            {
                "image":    "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-005",
                "cap":      "Luka al pass · venerdì 20:34 · settimo coperchio della serata",
                "tag":      "CREW",
            },
            {
                "image":    "https://images.unsplash.com/photo-1567521464027-f127ff144326?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-006",
                "cap":      "Apertura · 13 marzo 2024 · primo ingresso al banco alle 12:01",
                "tag":      "OPENING",
            },
        ],

        # Featured shot with quote overlay
        "featured_image": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1600&q=80&auto=format&fit=crop",
        "featured_quote": "«Brace è il posto dove vai se vuoi mangiare bene e veloce, e nessuno ti chiede di che lavori.»",
        "featured_author": "ZERO MAGAZINE · BOLOGNA · MARZO 2025",
        "featured_filename": "MO-FEAT-002",

        # End CTA
        "final_label":     "VEDI TUTTO IL RESTO",
        "final_heading":   'SEGUICI <em>SUI SOCIAL.</em>',
        "final_intro":
            "Ogni giorno una storia nuova, ogni venerdì il drop della settimana. "
            "Su Instagram trovi il diario, su TikTok come si lavora dietro al banco.",
        "final_instagram_cta": "INSTAGRAM @brace.lab",
        "final_tiktok_cta":    "TIKTOK @brace.bologna",
    },

    # ─── ORDINA ──────────────────────────────────────────────────
    "ordina": {
        "eyebrow":  "ORDINA AL VOLO",
        "headline": 'TRE MODI. <em>UN PIATTO SOLO.</em>',
        "intro":
            "Vieni al banco, chiama per il takeaway, ordina con i partner di "
            "consegna. Ti chiamiamo al numero quando è pronto, mai prima.",

        # Counter-status band
        "counter_status_label":  "STATO DEL BANCO",
        "counter_queue_label":   "CODA AL BANCO",
        "counter_queue_value":   "≈ 4 MIN",
        "counter_kitchen_label": "CUCINA APERTA",
        "counter_kitchen_value": "FINO ALLE 24:00",
        "counter_last_label":    "ULTIMO ORDINE",
        "counter_last_value":    "23:30",

        # 3-route grid — counter / takeaway / delivery
        "routes_label":   "TRE ROTTE",
        "routes_heading": 'SCEGLI <em>COME ORDINI.</em>',
        "routes": [
            {
                "id":      "01",
                "title":   "AL BANCO",
                "subtitle": "VIENI E PUNTA",
                "desc":
                    "Via Indipendenza 42, Bologna. Punta col dito sul menu, paga al "
                    "banco, ti chiamiamo al numero quando è pronto. Niente prenotazioni, "
                    "niente coperto, niente servizio. Tre minuti dal pass al piatto.",
                "lines": [
                    ("INDIRIZZO",    "Via Indipendenza 42, Bologna"),
                    ("CODA STIMATA", "≈ 4 MIN"),
                    ("ORARI",        "12:00 – 24:00 · ogni giorno"),
                ],
                "cta_label": "APRI MAPPA",
                "cta_href":  "https://www.openstreetmap.org/?mlat=44.4949&mlon=11.3426#map=17/44.4949/11.3426",
                "cta_kind":  "external",
            },
            {
                "id":      "02",
                "title":   "TAKEAWAY",
                "subtitle": "CHIAMA E RITIRA",
                "desc":
                    "Chiama il banco, dicci cosa vuoi, ti diamo un orario di ritiro. "
                    "Pronto in dodici minuti, sempre. Paghi al ritiro, in contanti o "
                    "con carta. WhatsApp se preferisci scrivere.",
                "lines": [
                    ("TELEFONO",   "051 234 5566"),
                    ("WHATSAPP",   "Scrivi 051 234 5566"),
                    ("PRONTO IN",  "12 MIN"),
                ],
                "cta_label": "CHIAMA ORA",
                "cta_href":  "+390512345566",
                "cta_kind":  "tel",
            },
            {
                "id":      "03",
                "title":   "DELIVERY",
                "subtitle": "CONSEGNA A CASA",
                "desc":
                    "Quattro partner di consegna, tutti su Bologna centro. Ordine "
                    "minimo dai dieci euro, consegna in trenta minuti, gratuita sopra "
                    "i venti euro. Apri l'app del partner che usi di più.",
                "lines": [
                    ("PARTNER",   "GLOVO · DELIVEROO · JUST EAT · UBER EATS"),
                    ("ZONA",      "Bologna centro · raggio 4 km"),
                    ("MIN ORDINE", "€ 10"),
                ],
                "cta_label": "VEDI I PARTNER",
                "cta_href":  "#partners",
                "cta_kind":  "anchor",
            },
        ],

        # Delivery partners detail
        "partners_label":   "I PARTNER DI CONSEGNA",
        "partners_heading": 'CONSEGNA IN <em>30 MINUTI.</em>',
        "partners": [
            {"name": "GLOVO",     "eta": "30 MIN", "min": "MIN € 12", "zone": "Bologna centro · 4 km"},
            {"name": "DELIVEROO", "eta": "25 MIN", "min": "MIN € 10", "zone": "Bologna centro · 3 km"},
            {"name": "JUST EAT",  "eta": "35 MIN", "min": "MIN € 15", "zone": "Bologna · 6 km"},
            {"name": "UBER EATS", "eta": "30 MIN", "min": "MIN € 12", "zone": "Bologna centro · 5 km"},
        ],

        # Late-night opening hours table
        "hours_label":   "QUANDO SIAMO APERTI",
        "hours_heading": 'ANCHE LA <em>DOMENICA.</em>',
        "hours_rows": [
            ("LUN", "12:00 – 24:00"),
            ("MAR", "12:00 – 24:00"),
            ("MER", "12:00 – 24:00"),
            ("GIO", "12:00 – 24:00"),
            ("VEN", "12:00 – 01:30"),
            ("SAB", "12:00 – 01:30"),
            ("DOM", "12:00 – 24:00"),
        ],
        "hours_note":
            "Ultimo ordine sempre 30 minuti prima della chiusura. La cucina chiude in "
            "anticipo solo se finisce l'impasto della pizza, mai prima di mezzanotte.",

        # Allergen note
        "allergen_label": "ALLERGENI",
        "allergen_text":
            "Tutti i piatti sono cucinati in un ambiente che lavora glutine, latticini, "
            "uova, soia, frutta a guscio. Per intolleranze gravi parla col banco prima "
            "di ordinare o scrivici su WhatsApp.",

        # Big phone CTA band
        "phone_label":   "PRONTO ORA",
        "phone_heading": 'CHIAMACI <em>AL BANCO.</em>',
        "phone_intro":
            "Risposta in tre squilli, anche durante il servizio. Se non rispondiamo, "
            "stiamo girando uno smash. Riprova in trenta secondi.",
        "phone_cta_label": "CHIAMA 051 234 5566",
        "phone_cta_href":  "+390512345566",

        # FAQ accordion — 4 questions
        "faq_label":   "DOMANDE FREQUENTI",
        "faq_heading": 'COSE CHE <em>CI CHIEDONO SPESSO.</em>',
        "faq": [
            {
                "q": "AVETE OPZIONI GLUTEN FREE?",
                "a": "Pane brioche gluten free su richiesta, ti chiediamo trenta minuti "
                     "in più di attesa. Avvisa al banco prima di ordinare. Patate, "
                     "carne e salse sono naturalmente gluten free, ma cucinate nello "
                     "stesso ambiente — per intolleranze gravi parla col banco.",
            },
            {
                "q": "FATE PRENOTAZIONI PER GRUPPI?",
                "a": "No coperti riservati, nessuna prenotazione. Per gruppi sopra le "
                     "dodici persone scrivici su WhatsApp due giorni prima: ti diciamo "
                     "se possiamo organizzare un orario meno affollato (di solito mar/mer "
                     "alle 19:00).",
            },
            {
                "q": "AVETE OPZIONI VEG E VEGANE?",
                "a": "Sì, sempre tre opzioni veg: veggie patty di lenticchie, pizza "
                     "rossa, fries brace. Le opzioni vegane (senza latticini) ruotano "
                     "ogni settimana — chiedi al banco quale c'è oggi.",
            },
            {
                "q": "FATE CATERING O EVENTI PRIVATI?",
                "a": "Sì, da venti a sessanta persone. Smash burger, pizza al taglio, "
                     "fritti, soda house. Forno mobile per eventi a Bologna e provincia. "
                     "Scrivi a eventi@bracestreetlab.it con data, posto, numero persone — "
                     "rispondiamo in 24 ore con un preventivo.",
            },
        ],
    },

    # ─── CONTATTI ────────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "TROVACI · BOLOGNA",
        "headline": 'VIA INDIPENDENZA <em>42.</em>',
        "intro":
            "Centro di Bologna, due passi dalle Due Torri. Aperti ogni giorno, "
            "anche la domenica, fino a tarda sera. Vieni a piedi se puoi.",

        # Address card
        "address_label": "INDIRIZZO",
        "address_value": "Via Indipendenza 42 · 40121 Bologna",
        "address_note":  "Tra Piazza Maggiore e la stazione · zona pedonale",

        # Map iframe
        "map_lat":   "44.4949",
        "map_lon":   "11.3426",
        "map_zoom":  "16",
        "map_label": "Mappa OpenStreetMap · Via Indipendenza 42, Bologna",

        # Contact channels grid
        "channels_label": "PARLA CON IL BANCO",
        "channels": [
            {
                "icon":  "phone",
                "label": "TELEFONO",
                "value": "051 234 5566",
                "note":  "risposta in tre squilli, anche durante il servizio",
                "href":  "+390512345566",
                "kind":  "tel",
            },
            {
                "icon":  "whatsapp",
                "label": "WHATSAPP",
                "value": "051 234 5566",
                "note":  "scrivi se preferisci, rispondiamo entro 30 minuti",
                "href":  "https://wa.me/390512345566",
                "kind":  "external",
            },
            {
                "icon":  "email",
                "label": "EMAIL",
                "value": "ordini@bracestreetlab.it",
                "note":  "per catering, eventi, fornitori",
                "href":  "ordini@bracestreetlab.it",
                "kind":  "mail",
            },
        ],

        # Hours grid (compact)
        "hours_label": "ORARI DI APERTURA",
        "hours_rows": [
            ("LUN – GIO", "12:00 – 24:00"),
            ("VEN – SAB", "12:00 – 01:30"),
            ("DOMENICA",  "12:00 – 24:00"),
        ],
        "hours_note": "Ultimo ordine 30 minuti prima della chiusura · cucina sempre attiva",

        # Transport note
        "transport_label": "COME ARRIVI",
        "transport_rows": [
            ("BUS",      "linee 11, 14, 27 · fermata Indipendenza"),
            ("TRENO",    "Stazione Centrale · 8 minuti a piedi"),
            ("PARCHEGGIO", "Riva di Reno · 4 minuti a piedi"),
            ("BICI",     "rastrelliera in via dell'Indipendenza"),
        ],

        # Jobs band
        "jobs_label":    "LAVORA CON NOI",
        "jobs_heading":  'CERCHIAMO <em>CINQUE PERSONE.</em>',
        "jobs_intro":
            "Brace cresce. Apriamo un secondo lab a Modena entro l'estate 2026. "
            "Ci servono persone vere, non curriculum perfetti.",
        "jobs": [
            {"role": "GRILLER",   "type": "FULL TIME", "city": "BOLOGNA"},
            {"role": "PIZZAIOLO", "type": "PART TIME", "city": "BOLOGNA"},
            {"role": "RUNNER & BANCO", "type": "WEEKEND", "city": "BOLOGNA"},
        ],
        "jobs_cta_label": "MANDA UN MESSAGGIO",
        "jobs_cta_href":  "lavoro@bracestreetlab.it",

        # Social block
        "social_label": "SEGUICI",
        "social": [
            {"platform": "INSTAGRAM", "handle": "@brace.lab",      "href": "https://instagram.com/brace.lab"},
            {"platform": "TIKTOK",    "handle": "@brace.bologna",  "href": "https://tiktok.com/@brace.bologna"},
        ],

        # Mini reservation/inquiry form
        "form_label":   "SCRIVICI",
        "form_heading": 'DUE RIGHE <em>BASTANO.</em>',
        "form_intro":
            "Per catering, gruppi sopra dodici persone, fornitori. Per ordinare "
            "scrivici su WhatsApp, è più veloce.",
        "form_field_name":     "Nome",
        "form_field_email":    "Email",
        "form_field_phone":    "Telefono",
        "form_field_message":  "Cosa ti serve",
        "form_field_message_placeholder": "Catering, evento, fornitura, altro…",
        "form_submit_label":   "MANDA",
        "form_submit_note":
            "Demo dimostrativa · nessun dato verrà inviato. Per ordinare davvero, "
            "chiama 051 234 5566 o scrivi su WhatsApp.",
    },

    # No blog on Brace
    "posts": [],
}
