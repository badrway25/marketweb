"""Brace — Brace Street Lab (street-modern archetype) — Spanish (ES) content tree.

Phase 2g3.6 — Restaurant live-completion · ES locale rollout (Session 48).

Voice contract (ES — peninsular street-food, El País Gastro / Time Out
Madrid food guides / Cinco Días Lifestyle register):
- Native peninsular Spanish reviewing a Bologna smashburger lab.
- Direct, fast, second-person ``tú`` imperative ("pide en barra", "pasa",
  "no esperes"). Confident, urban, sharp.
- MAYÚSCULAS display headlines (mirror IT UPPERCASE display vibe). NO
  acentos en mayúsculas (Spanish convention).
- Italian dish names stay Italian: Margherita, Marinara, Fritto misto,
  Cesanese, Mortadella e pistacchio. Brief gloss only on first mention.
- Italian proper names stay Italian: Brace Street Lab, Bologna, Via
  Indipendenza, Tortellini. NEVER transliterate.
- Currency: ``9,50 €`` (peninsular convention).
- Italian tabular labels translate: LUN – DOM, LUN – JUE, VIE – SÁB.
- Spanish punctuation: ¿…? ¡…! opening marks where applicable.
- Peninsular vocabulary (`tú`, `mola`, `pillar`, `currar`) — NOT Latin
  American.

Differentiation contract:
- Voice MUST stay sharply opposite from Sapore ES (warm Roman trattoria
  food-writer reportage `tú`) and from Gusto ES (Michelin editorial-chef
  `usted`). Brace ES = peninsular street-food urban-imperative register.
"""
from __future__ import annotations

from typing import Any


BRACE_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Inicio",       "kind": "home"},
        {"slug": "menu",     "label": "Carta",        "kind": "menu"},
        {"slug": "lab",      "label": "El Lab",       "kind": "about"},
        {"slug": "moments",  "label": "Moments",      "kind": "gallery"},
        {"slug": "ordina",   "label": "Pedir",        "kind": "order"},
        {"slug": "contatti", "label": "Encuéntranos", "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "B",
        "logo_word":    "BRACE STREET LAB",
        "tag":          "BOLONIA · VIA INDIPENDENZA 42 · 12:00 → 24:00",
        "phone":        "051 234 5566",
        "phone_tel":    "+390512345566",
        "phone_display": "051 234 5566",
        "whatsapp":     "051 234 5566",
        "whatsapp_link": "https://wa.me/390512345566",
        "email":        "ordini@bracestreetlab.it",
        "address":      "Via Indipendenza 42 · 40121 Bolonia",
        "hours_compact": "TODOS LOS DIAS · 12:00 – 24:00 · VIE/SAB HASTA LA 01:30",
        "hours_footer_rows": [
            "LUN – JUE · 12:00 – 24:00",
            "VIE – SAB · 12:00 – 01:30",
            "DOM · 12:00 – 24:00",
        ],
        "license":      "NIF IT 04127880371 · Cámara de Bolonia REA 358912",
        "footer_intro":
            "Street food lab en Bolonia. Smashburger de scottona piamontesa, "
            "fritos a la minuto, pizza al taglio del horno de leña. Pides en "
            "barra, recoges con tu número, comes al vuelo. Abrimos hasta tarde, "
            "todos los días, también el domingo.",
        "nav_cta":      "PIDE AHORA",
        "nav_cta_href": "ordina",
        "nav_phone_cta": "051 234 5566",
        "star_line":    "STREET FOOD LAB · BOLONIA",
        "copyright":    "© 2026 Brace Street Lab · NIF IT 04127880371",

        # Mirror the fine-dining/_base.html footer keys used by the chrome
        "footer_hours_1": "LUN – JUE · 12:00 – 24:00",
        "footer_hours_2": "VIE – SAB · 12:00 – 01:30",

        # Social
        "instagram_handle": "@brace.lab",
        "instagram_link":   "https://instagram.com/brace.lab",
        "tiktok_handle":    "@brace.bologna",
        "tiktok_link":      "https://tiktok.com/@brace.bologna",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "STREET FOOD LAB · BOLONIA",
        "headline": 'AL FUEGO VIVO. <em>AL VUELO.</em>',
        "intro":
            "Smashburger de scottona piamontesa, fritos contracorriente, pizza "
            "al taglio del horno de leña. Pides en barra, recoges con tu número, "
            "comes al vuelo.",
        "primary_cta":   "PIDE AHORA",
        "primary_href":  "ordina",
        "secondary_cta": "LA CARTA",
        "secondary_href": "menu",

        # Hero product cutout
        "hero_image":       "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=1400&q=80&auto=format&fit=crop",
        "hero_alt":         "Doppio Brace smashburger en primer plano",
        "hero_badge_price": "9,50 €",
        "hero_badge_label": "DOPPIO BRACE",
        "hero_badge_tag":   "TOP",

        # Real-time queue counter strip
        "counter_label": "LA COLA EN BARRA",
        "counter_value": "≈ 4 MIN",
        "counter_kitchen_label": "COCINA ABIERTA",
        "counter_kitchen_value": "HASTA LAS 24:00",
        "counter_last_label":    "ULTIMO PEDIDO",
        "counter_last_value":    "23:30",

        # Stat band — 4 numbers
        "stats_label": "LOS NUMEROS DEL LAB",
        "stats": [
            ("12.000",  "BURGER / MES"),
            ("4.9 ★",   "SOBRE 1.380 RESEÑAS"),
            ("100%",    "SCOTTONA PIAMONTESA"),
            ("420°C",   "HORNO DE LEÑA"),
        ],

        # Menu strip — 6 product-grid items on home (teaser of full menu)
        "menu_strip_label":   "DE LA BARRA ESTA NOCHE",
        "menu_strip_heading": 'LA CARTA <em>DEL VUELO.</em>',
        "menu_strip_intro":
            "Seis piezas que salen calientes del pase cada quince minutos. "
            "Apunta, elige, pagas en barra, te cantamos por el número.",
        "menu_strip_cta":      "VER LA CARTA ENTERA",
        "menu_strip_cta_href": "menu",
        "menu_strip_items": [
            {
                "name":  "DOPPIO BRACE",
                "desc":  "doble scottona, cheddar fundido, salsa brace",
                "price": "9,50 €",
                "tag":   "TOP",
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "SMASH CLASICO",
                "desc":  "scottona simple, cheddar, cebolla caramelizada",
                "price": "7,50 €",
                "tag":   "",
                "image": "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "FRITTO MISTO",
                "desc":  "patatas, jalapeños rebozados, bacalao frito",
                "price": "6,00 €",
                "tag":   "PICANTE",
                "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "PIZZA ROSSA",
                "desc":  "tomate san marzano dop, fior di latte, albahaca",
                "price": "4,50 €",
                "tag":   "VEG",
                "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "FRIES BRACE",
                "desc":  "patatas doble fritura, sal gorda, salsa brace",
                "price": "4,50 €",
                "tag":   "",
                "image": "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "SODA BRACE",
                "desc":  "limonada de la casa con albahaca fresca",
                "price": "3,00 €",
                "tag":   "NUEVO",
                "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Delivery partners marquee strip
        "delivery_label":    "PIDE DESDE DONDE QUIERAS",
        "delivery_subtitle": "ENTREGA EN 30 MINUTOS · BOLONIA CENTRO",
        "delivery_partners": [
            ("GLOVO",     "30 MIN", "MIN 12 €"),
            ("DELIVEROO", "25 MIN", "MIN 10 €"),
            ("JUST EAT",  "35 MIN", "MIN 15 €"),
            ("UBER EATS", "30 MIN", "MIN 12 €"),
        ],

        # Lab manifesto — 3 short bold paragraphs
        "manifesto_label":   "EL LAB",
        "manifesto_heading": 'POR QUE FUEGO. <em>POR QUE VUELO.</em>',
        "manifesto_paragraphs": [
            "Brace es un laboratorio. Nada de papel pintado, nada de manteles. "
            "Solo hierro, fuego y cinco personas currando a la vista durante "
            "ciento ochenta segundos por plato.",

            "Trabajamos solo scottona piamontesa, picada por la mañana con la "
            "picadora encima de la barra. Cada patata se corta a mano a las "
            "diez. Cada salsa se hace dentro del lab, nunca comprada.",

            "Pasa cuando quieras. Abrimos de doce a medianoche, todos los días, "
            "también el domingo. El sábado tiramos hasta la una y media. La "
            "cocina no cierra antes del último que entre.",
        ],
        "manifesto_cta":      "DESCUBRE EL LAB",
        "manifesto_cta_href": "lab",

        # Crew band — 3 people (chef, griller, founder)
        "crew_label":   "LA CREW",
        "crew_heading": 'CINCO EN BARRA. <em>UN SOLO EQUIPO.</em>',
        "crew": [
            {
                "name":   "DARIO RIVA",
                "role":   "FUNDADOR & GRILLER",
                "quote":  "«Una smash buena es hierro caliente, scottona fría, noventa segundos y punto.»",
                "portrait": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "AMINA BERETTA",
                "role":   "PIZZAIOLA · HORNO DE LEÑA",
                "quote":  "«El horno te pide atención cada dos minutos. Por eso no miro el móvil.»",
                "portrait": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "LUKA HOXHA",
                "role":   "FRITOS & SALSAS",
                "quote":  "«La mayonesa a la brasa la firmo yo. Sin secreto, solo paciencia.»",
                "portrait": "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Urban photo strip — 3 atmosphere shots
        "atmo_label":   "EL AMBIENTE",
        "atmo_heading": 'BARRA. NEON. <em>COLA.</em>',
        "atmo_strip": [
            {
                "image": "https://images.unsplash.com/photo-1485962398834-fef83cc41e4f?w=900&q=80&auto=format&fit=crop",
                "cap":   "Cola en barra · sábado a las 19:40",
            },
            {
                "image": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=900&q=80&auto=format&fit=crop",
                "cap":   "DJ set late-night · cada último viernes del mes",
            },
            {
                "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=900&q=80&auto=format&fit=crop",
                "cap":   "Horno de leña encendido desde las 11:00 hasta el cierre",
            },
        ],

        # Final CTA band — late-night order push
        "final_label":   "¿LISTO PARA PEDIR?",
        "final_heading": 'ULTIMO PEDIDO <em>A LAS 23:30.</em>',
        "final_intro":
            "Tres maneras de tenernos en el plato. Pasa por la barra. Llama "
            "para el takeaway. Pide con los partners de entrega. No te duermas.",
        "final_primary_cta":   "PIDE YA",
        "final_primary_href":  "ordina",
        "final_phone_cta":     "LLAMA AL 051 234 5566",
        "final_phone_href":    "+390512345566",
    },

    # ─── MENU ────────────────────────────────────────────────────
    "menu": {
        "eyebrow":  "CARTA · DESDE LA BARRA",
        "headline": 'TODO LO QUE <em>SE QUEMA.</em>',
        "intro":
            "Cinco secciones, veintidós piezas, precios en barra. Apunta con "
            "el dedo, paga, te cantamos por el número. Ni cubierto ni servicio.",

        "sections": [
            {
                "id":    "burger",
                "label": "01",
                "title": "BURGER",
                "desc":  "scottona piamontesa · picada por la mañana · pan brioche de trigo quemado",
                "items": [
                    {
                        "name":  "DOPPIO BRACE",
                        "desc":  "doble scottona, cheddar fundido, salsa brace, cebolla cruda",
                        "price": "9,50 €",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "SMASH CLASICO",
                        "desc":  "scottona simple, cheddar, cebolla caramelizada, salsa de la casa",
                        "price": "7,50 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "VEGGIE PATTY",
                        "desc":  "hamburguesa de lentejas y remolacha, hummus al limón, rúcula",
                        "price": "8,00 €",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BRACE PICANTE",
                        "desc":  "scottona, jalapeños fritos, cheddar picante, sriracha brace",
                        "price": "9,00 €",
                        "tag":   "PICANTE",
                        "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "fritti",
                "label": "02",
                "title": "FRITOS",
                "desc":  "patatas cortadas a mano a las 10:00 · doble fritura · sal de Cervia",
                "items": [
                    {
                        "name":  "FRIES BRACE",
                        "desc":  "patatas doble fritura, sal gorda, salsa brace en cazuelita",
                        "price": "4,50 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "FRITTO MISTO",
                        "desc":  "patatas, jalapeños rebozados, bacalao frito, aros de cebolla",
                        "price": "6,00 €",
                        "tag":   "PICANTE",
                        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "JALAPEÑO POPPER",
                        "desc":  "jalapeños rellenos de cheddar, rebozados, fritos, salsa de lima",
                        "price": "5,50 €",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "ONION RINGS",
                        "desc":  "aros de cebolla roja de Tropea en tempura, bbq de la casa",
                        "price": "5,00 €",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "pizza",
                "label": "03",
                "title": "PIZZA AL TAGLIO",
                "desc":  "masa de 72 horas · horno de leña a 420°C · sesenta segundos de cocción",
                "items": [
                    {
                        "name":  "PIZZA ROSSA",
                        "desc":  "tomate san marzano dop, fior di latte, albahaca",
                        "price": "4,50 €",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BIANCA AL TARTUFO",
                        "desc":  "fior di latte, lascas de trufa negra de verano, aceite oliva virgen",
                        "price": "6,50 €",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "DIAVOLA NEW",
                        "desc":  "tomate, fior di latte, salame picante calabrés, miel",
                        "price": "5,50 €",
                        "tag":   "PICANTE",
                        "image": "https://images.unsplash.com/photo-1593504049359-74330189a345?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "MORTADELLA & PISTACCHIO",
                        "desc":  "fior di latte, mortadella di Bologna igp, pistacho de Bronte",
                        "price": "6,00 €",
                        "tag":   "NUEVO",
                        "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "drink",
                "label": "04",
                "title": "SODA & BEBIDAS",
                "desc":  "soda de la casa prensada en barra · cerveza boloñesa de barril · vino por copas",
                "items": [
                    {
                        "name":  "SODA BRACE",
                        "desc":  "limonada casera con albahaca fresca y jengibre",
                        "price": "3,00 €",
                        "tag":   "NUEVO",
                        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "ICED TEA HOUSE",
                        "desc":  "té frío earl grey con miel de castaño y piel de limón",
                        "price": "3,00 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BIRRA SPINA",
                        "desc":  "lager boloñesa de la cervecería Sant'Orsola · 0,33 l",
                        "price": "4,50 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "VINO POR COPAS",
                        "desc":  "sangiovese di Romagna doc · bodega Ronchi di Solarolo",
                        "price": "5,00 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "dolci",
                "label": "05",
                "title": "POSTRES",
                "desc":  "hechos dentro del lab · porciones pequeñas, para comer al vuelo",
                "items": [
                    {
                        "name":  "BRACE COOKIE",
                        "desc":  "cookie de cacao con corazón de Nutella todavía caliente",
                        "price": "3,50 €",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "GELATO ARTESANO",
                        "desc":  "fior di panna o pistacho · servido por la gelateria Stefino",
                        "price": "3,00 €",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "TIRAMISU AL VUELO",
                        "desc":  "en tarrito, mascarpone fresco, savoiardi, café boloñés",
                        "price": "4,00 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
        ],

        # Allergen line at bottom
        "allergen_label": "ALERGENOS",
        "allergen_text":
            "Todos los platos se cocinan en un entorno que trabaja gluten, "
            "lácteos, huevo, soja y frutos secos. Para intolerancias graves "
            "habla con la barra antes de pedir. Lista completa de alérgenos "
            "disponible en barra.",

        # Producer band — 3 producer names with city
        "producers_label":   "LOS PROVEEDORES",
        "producers_heading": 'DE DONDE LLEGA <em>CADA COSA.</em>',
        "producers_intro":
            "Trabajamos con tres proveedores históricos de la ciudad. Cada "
            "producto firmado, trazado, en pequeños lotes semanales.",
        "producers": [
            {
                "name":   "MACELLERIA SARTI",
                "city":   "BOLONIA · VIA PETRONI",
                "role":   "Scottona piamontesa, picada fresca cada mañana a las siete.",
            },
            {
                "name":   "FORNO BERETTA",
                "city":   "MODENA · CASTELFRANCO",
                "role":   "Pan brioche de trigo quemado y masa de pizza fermentada 72 horas.",
            },
            {
                "name":   "ORTOFRUTTA TOSI",
                "city":   "BOLONIA · MERCADO ALBANI",
                "role":   "Patatas, cebollas rojas de Tropea, jalapeños cultivados en invernadero.",
            },
        ],

        # Final CTA
        "final_label":         "PIDE YA",
        "final_heading":       'APUNTA. <em>PAGA. RECOGE.</em>',
        "final_primary_cta":   "PIDE AHORA",
        "final_primary_href":  "ordina",
        "final_secondary_cta": "ENCUENTRANOS",
        "final_secondary_href": "contatti",
    },

    # ─── LAB (about) ─────────────────────────────────────────────
    "lab": {
        "eyebrow":  "EL LAB",
        "headline": 'POR QUE EL FUEGO. <em>POR QUE EL VUELO.</em>',
        "intro":
            "Brace es un laboratorio abierto todos los días de doce a "
            "medianoche. Cinco personas, una barra, dos hornos. Nada más, "
            "nada menos.",

        # Big atmosphere photo
        "hero_image":   "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1600&q=80&auto=format&fit=crop",
        "hero_caption": "La barra abierta · horno de leña a 420°C · cada servicio empieza aquí",

        # Manifesto — 4 short bold paragraphs
        "manifesto_label":   "MANIFIESTO",
        "manifesto_paragraphs": [
            {
                "title": "01 MASA",
                "text":  "Masa madre refrescada cada doce horas. Harinas tipo 1 molidas a "
                         "piedra por el Forno Beretta de Castelfranco. Setenta y dos horas "
                         "de fermentación lenta en cámara, nunca menos. La pizza se siente "
                         "en los dedos antes que en la boca.",
            },
            {
                "title": "02 FUEGO",
                "text":  "El horno de leña quema solo encina del Cimino, nada más. Llega "
                         "a 420°C en treinta y cinco minutos. La plancha del grill alcanza "
                         "los 280°C: scottona piamontesa al hierro, aplastada, noventa "
                         "segundos por cara.",
            },
            {
                "title": "03 MATERIA",
                "text":  "Solo scottona piamontesa de la Macelleria Sarti, picada encima "
                         "de la barra cada mañana a las siete. Patatas Tosi cortadas a "
                         "mano a las diez. Tomate san marzano dop del Agro Sarnese. Todo "
                         "firmado, todo trazado.",
            },
            {
                "title": "04 VELOCIDAD",
                "text":  "Tres minutos de la barra al pase. Catorce segundos para girar "
                         "la smash. Sesenta segundos de pizza. Ciento ochenta segundos "
                         "totales de servicio. Rápidos sí, pero hechos como dios manda.",
            },
        ],

        # Process strip — 3-step
        "process_label":   "EL PROCESO",
        "process_heading": "TRES GESTOS. <em>NADA MAS.</em>",
        "process": [
            {
                "num":   "01",
                "title": "MASA",
                "desc":  "cada noche a las 23:00, fermentación 72 h en cámara a 4°C",
            },
            {
                "num":   "02",
                "title": "FUEGO",
                "desc":  "horno encendido a las 11:00, plancha a 280°C desde las 12:00",
            },
            {
                "num":   "03",
                "title": "SERVICIO",
                "desc":  "tres minutos de la barra al pase, te cantamos por el número",
            },
        ],

        # Crew band — 4 people
        "crew_label":   "LA CREW AL COMPLETO",
        "crew_heading": 'CINCO EN BARRA. <em>UN SOLO EQUIPO.</em>',
        "crew": [
            {
                "name":   "DARIO RIVA",
                "role":   "FUNDADOR & GRILLER",
                "quote":  "«Una smash buena es hierro caliente, scottona fría, noventa segundos y punto.»",
                "portrait": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "AMINA BERETTA",
                "role":   "PIZZAIOLA · HORNO DE LEÑA",
                "quote":  "«El horno te pide atención cada dos minutos. Por eso no miro el móvil.»",
                "portrait": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "LUKA HOXHA",
                "role":   "FRITOS & SALSAS",
                "quote":  "«La mayonesa a la brasa la firmo yo. Sin secreto, solo paciencia.»",
                "portrait": "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "SOFIA MARTINI",
                "role":   "BARRA & TURNOS",
                "quote":  "«Te llamo por tu nombre si ya has venido dos veces. Es la regla de la casa.»",
                "portrait": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Values grid — 4 cards
        "values_label":   "LOS VALORES",
        "values_heading": 'CUATRO COSAS <em>NO NEGOCIABLES.</em>',
        "values": [
            {"title": "TIEMPO",      "tag": "CERO ESPERA",    "desc": "tres minutos de la barra al pase, siempre"},
            {"title": "TEMPERATURA", "tag": "420°C / 280°C",  "desc": "horno y plancha controlados a la vista, nunca menos"},
            {"title": "CALIDAD",     "tag": "100% PIAMONTE",  "desc": "scottona firmada, trazada, picada por la mañana"},
            {"title": "ENERGIA",     "tag": "TODOS LOS DIAS", "desc": "abierto de 12 a medianoche, también el domingo"},
        ],

        # Kitchen energy band
        "kitchen_label":   "LA FICHA TECNICA",
        "kitchen_heading": 'LOS NUMEROS <em>DE LA COCINA.</em>',
        "kitchen_specs": [
            ("210°C", "PLANCHA SMASH"),
            ("420°C", "HORNO DE LEÑA"),
            ("14 SEG", "FLIP DE LA SMASH"),
            ("90 SEG", "COCCION PIZZA"),
            ("3 MIN", "BARRA AL PASE"),
            ("72 H", "FERMENTACION"),
        ],

        # Final CTA
        "final_label":   "PASATE A VERLO",
        "final_heading": 'EL LAB SIEMPRE <em>ESTA ABIERTO.</em>',
        "final_intro":
            "Abrimos de doce a medianoche, todos los días. Pasa cuando "
            "quieras, apunta con el dedo, paga en barra. Sin reservas, sin "
            "cubierto.",
        "final_primary_cta":   "VER LA CARTA",
        "final_primary_href":  "menu",
        "final_secondary_cta": "ENCUENTRANOS",
        "final_secondary_href": "contatti",
    },

    # ─── MOMENTS (gallery) ───────────────────────────────────────
    "moments": {
        "eyebrow":  "MOMENTS · STREET DIARY",
        "headline": 'CADA NOCHE <em>UN MOMENTO.</em>',
        "intro":
            "El diario fotográfico de Brace. Cola en barra, late-night DJ, "
            "fritura en llamas, crew currando. Todo disparado aquí, por "
            "nosotros.",

        # Category pills
        "categories_label": "FILTRA",
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
                "image":    "https://images.unsplash.com/photo-1485962398834-fef83cc41e4f?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-001",
                "cap":      "Cola en barra · sábado 23:14 · ochenta personas en Via Indipendenza",
                "tag":      "COUNTER QUEUE",
            },
            {
                "image":    "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-002",
                "cap":      "DJ Tito Brama · last friday set · solo vinilo hasta las 02:00",
                "tag":      "DJ NIGHTS",
            },
            {
                "image":    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-003",
                "cap":      "Horno de leña · 420°C · undécima hora de servicio",
                "tag":      "LATE NIGHT",
            },
            {
                "image":    "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-004",
                "cap":      "Doble fritura de patata · sal de Cervia · listo en trescientos segundos",
                "tag":      "FRY MOMENTS",
            },
            {
                "image":    "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-005",
                "cap":      "Luka en el pase · viernes 20:34 · séptima tapa de la noche",
                "tag":      "CREW",
            },
            {
                "image":    "https://images.unsplash.com/photo-1567521464027-f127ff144326?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-006",
                "cap":      "Apertura · 13 de marzo de 2024 · primer cliente en barra a las 12:01",
                "tag":      "OPENING",
            },
        ],

        # Featured shot with quote overlay
        "featured_image": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1600&q=80&auto=format&fit=crop",
        "featured_quote": "«Brace es el sitio al que vas si quieres comer bien y rápido, y nadie te pregunta de qué curras.»",
        "featured_author": "ZERO MAGAZINE · BOLONIA · MARZO 2025",
        "featured_filename": "MO-FEAT-002",

        # End CTA
        "final_label":     "MIRA TODO LO DEMAS",
        "final_heading":   'SIGUENOS <em>EN REDES.</em>',
        "final_intro":
            "Cada día una historia nueva, cada viernes el drop de la semana. "
            "En Instagram tienes el diario, en TikTok cómo se curra detrás "
            "de la barra.",
        "final_instagram_cta": "INSTAGRAM @brace.lab",
        "final_tiktok_cta":    "TIKTOK @brace.bologna",
    },

    # ─── ORDINA ──────────────────────────────────────────────────
    "ordina": {
        "eyebrow":  "PIDE AL VUELO",
        "headline": 'TRES MANERAS. <em>UN SOLO PLATO.</em>',
        "intro":
            "Pasa por la barra, llama para el takeaway, pide con los partners "
            "de entrega. Te cantamos por el número cuando esté listo, nunca "
            "antes.",

        # Counter-status band
        "counter_status_label":  "ESTADO DE LA BARRA",
        "counter_queue_label":   "LA COLA EN BARRA",
        "counter_queue_value":   "≈ 4 MIN",
        "counter_kitchen_label": "COCINA ABIERTA",
        "counter_kitchen_value": "HASTA LAS 24:00",
        "counter_last_label":    "ULTIMO PEDIDO",
        "counter_last_value":    "23:30",

        # 3-route grid — counter / takeaway / delivery
        "routes_label":   "TRES RUTAS",
        "routes_heading": 'ELIGE <em>COMO PIDES.</em>',
        "routes": [
            {
                "id":      "01",
                "title":   "EN BARRA",
                "subtitle": "PASA Y APUNTA",
                "desc":
                    "Via Indipendenza 42, Bolonia. Apunta con el dedo en la "
                    "carta, paga en barra, te cantamos por el número cuando "
                    "esté listo. Sin reservas, sin cubierto, sin servicio. "
                    "Tres minutos del pase al plato.",
                "lines": [
                    ("DIRECCION",  "Via Indipendenza 42, Bolonia"),
                    ("COLA ESTIMADA", "≈ 4 MIN"),
                    ("HORARIO",    "12:00 – 24:00 · todos los días"),
                ],
                "cta_label": "ABRIR MAPA",
                "cta_href":  "https://www.openstreetmap.org/?mlat=44.4949&mlon=11.3426#map=17/44.4949/11.3426",
                "cta_kind":  "external",
            },
            {
                "id":      "02",
                "title":   "TAKEAWAY",
                "subtitle": "LLAMA Y RECOGE",
                "desc":
                    "Llama a la barra, dinos qué quieres, te damos hora de "
                    "recogida. Listo en doce minutos, siempre. Pagas al "
                    "recoger, en efectivo o con tarjeta. WhatsApp si "
                    "prefieres escribir.",
                "lines": [
                    ("TELEFONO",   "051 234 5566"),
                    ("WHATSAPP",   "Escribe al 051 234 5566"),
                    ("LISTO EN",   "12 MIN"),
                ],
                "cta_label": "LLAMA YA",
                "cta_href":  "+390512345566",
                "cta_kind":  "tel",
            },
            {
                "id":      "03",
                "title":   "DELIVERY",
                "subtitle": "ENTREGA EN CASA",
                "desc":
                    "Cuatro partners de entrega, todos en Bolonia centro. "
                    "Pedido mínimo desde diez euros, entrega en treinta "
                    "minutos, gratuita por encima de veinte. Abre la app "
                    "del partner que más uses.",
                "lines": [
                    ("PARTNERS",   "GLOVO · DELIVEROO · JUST EAT · UBER EATS"),
                    ("ZONA",       "Bolonia centro · radio 4 km"),
                    ("MIN PEDIDO", "10 €"),
                ],
                "cta_label": "VER PARTNERS",
                "cta_href":  "#partners",
                "cta_kind":  "anchor",
            },
        ],

        # Delivery partners detail
        "partners_label":   "LOS PARTNERS DE ENTREGA",
        "partners_heading": 'ENTREGA EN <em>30 MINUTOS.</em>',
        "partners": [
            {"name": "GLOVO",     "eta": "30 MIN", "min": "MIN 12 €", "zone": "Bolonia centro · 4 km"},
            {"name": "DELIVEROO", "eta": "25 MIN", "min": "MIN 10 €", "zone": "Bolonia centro · 3 km"},
            {"name": "JUST EAT",  "eta": "35 MIN", "min": "MIN 15 €", "zone": "Bolonia · 6 km"},
            {"name": "UBER EATS", "eta": "30 MIN", "min": "MIN 12 €", "zone": "Bolonia centro · 5 km"},
        ],

        # Late-night opening hours table
        "hours_label":   "CUANDO ABRIMOS",
        "hours_heading": 'TAMBIEN EL <em>DOMINGO.</em>',
        "hours_rows": [
            ("LUN", "12:00 – 24:00"),
            ("MAR", "12:00 – 24:00"),
            ("MIE", "12:00 – 24:00"),
            ("JUE", "12:00 – 24:00"),
            ("VIE", "12:00 – 01:30"),
            ("SAB", "12:00 – 01:30"),
            ("DOM", "12:00 – 24:00"),
        ],
        "hours_note":
            "Último pedido siempre 30 minutos antes del cierre. La cocina "
            "cierra antes solo si se acaba la masa de pizza, nunca antes de "
            "medianoche.",

        # Allergen note
        "allergen_label": "ALERGENOS",
        "allergen_text":
            "Todos los platos se cocinan en un entorno que trabaja gluten, "
            "lácteos, huevo, soja y frutos secos. Para intolerancias graves "
            "habla con la barra antes de pedir o escríbenos por WhatsApp.",

        # Big phone CTA band
        "phone_label":   "AL TELEFONO YA",
        "phone_heading": 'LLAMANOS <em>A LA BARRA.</em>',
        "phone_intro":
            "Te cogemos en tres tonos, también durante el servicio. Si no "
            "contestamos, estamos girando una smash. Vuelve a intentarlo en "
            "treinta segundos.",
        "phone_cta_label": "LLAMA AL 051 234 5566",
        "phone_cta_href":  "+390512345566",

        # FAQ accordion — 4 questions
        "faq_label":   "PREGUNTAS FRECUENTES",
        "faq_heading": 'COSAS QUE <em>NOS PREGUNTAN A MENUDO.</em>',
        "faq": [
            {
                "q": "¿TENEIS OPCIONES SIN GLUTEN?",
                "a": "Pan brioche sin gluten bajo demanda, te pedimos treinta "
                     "minutos más de espera. Avisa en barra antes de pedir. "
                     "Patatas, carne y salsas son sin gluten de manera natural, "
                     "pero se cocinan en el mismo entorno — para intolerancias "
                     "graves habla con la barra.",
            },
            {
                "q": "¿RESERVAIS PARA GRUPOS?",
                "a": "Sin mesas reservadas, sin reservas. Para grupos por "
                     "encima de doce personas escríbenos por WhatsApp con dos "
                     "días de antelación: te decimos si podemos organizar un "
                     "horario menos lleno (normalmente mar/mié a las 19:00).",
            },
            {
                "q": "¿TENEIS OPCIONES VEG Y VEGANAS?",
                "a": "Sí, siempre tres opciones veg: veggie patty de lentejas, "
                     "pizza rossa, fries brace. Las opciones veganas (sin "
                     "lácteos) van rotando cada semana — pregunta en barra "
                     "cuál tenemos hoy.",
            },
            {
                "q": "¿HACEIS CATERING O EVENTOS PRIVADOS?",
                "a": "Sí, de veinte a sesenta personas. Smashburger, pizza al "
                     "taglio, fritos, soda de la casa. Horno móvil para eventos "
                     "en Bolonia y provincia. Escribe a eventi@bracestreetlab.it "
                     "con fecha, sitio, número de personas — respondemos en "
                     "24 horas con presupuesto.",
            },
        ],
    },

    # ─── CONTATTI ────────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "ENCUENTRANOS · BOLONIA",
        "headline": 'VIA INDIPENDENZA <em>42.</em>',
        "intro":
            "Centro de Bolonia, a dos pasos de las Due Torri. Abrimos todos "
            "los días, también el domingo, hasta tarde. Pásate andando si "
            "puedes.",

        # Address card
        "address_label": "DIRECCION",
        "address_value": "Via Indipendenza 42 · 40121 Bolonia",
        "address_note":  "Entre Piazza Maggiore y la estación · zona peatonal",

        # Map iframe
        "map_lat":   "44.4949",
        "map_lon":   "11.3426",
        "map_zoom":  "16",
        "map_label": "Mapa OpenStreetMap · Via Indipendenza 42, Bolonia",

        # Contact channels grid
        "channels_label": "HABLA CON LA BARRA",
        "channels": [
            {
                "icon":  "phone",
                "label": "TELEFONO",
                "value": "051 234 5566",
                "note":  "te cogemos en tres tonos, también durante el servicio",
                "href":  "+390512345566",
                "kind":  "tel",
            },
            {
                "icon":  "whatsapp",
                "label": "WHATSAPP",
                "value": "051 234 5566",
                "note":  "escribe si prefieres, contestamos en 30 minutos",
                "href":  "https://wa.me/390512345566",
                "kind":  "external",
            },
            {
                "icon":  "email",
                "label": "EMAIL",
                "value": "ordini@bracestreetlab.it",
                "note":  "para catering, eventos, proveedores",
                "href":  "ordini@bracestreetlab.it",
                "kind":  "mail",
            },
        ],

        # Hours grid (compact)
        "hours_label": "HORARIO DE APERTURA",
        "hours_rows": [
            ("LUN – JUE", "12:00 – 24:00"),
            ("VIE – SAB", "12:00 – 01:30"),
            ("DOMINGO",   "12:00 – 24:00"),
        ],
        "hours_note": "Último pedido 30 minutos antes del cierre · cocina siempre activa",

        # Transport note
        "transport_label": "COMO LLEGAS",
        "transport_rows": [
            ("BUS",        "líneas 11, 14, 27 · parada Indipendenza"),
            ("TREN",       "Estación Central · 8 minutos andando"),
            ("PARKING",    "Riva di Reno · 4 minutos andando"),
            ("BICI",       "aparcabicis en Via dell'Indipendenza"),
        ],

        # Jobs band
        "jobs_label":    "TRABAJA CON NOSOTROS",
        "jobs_heading":  'BUSCAMOS <em>CINCO PERSONAS.</em>',
        "jobs_intro":
            "Brace crece. Abrimos un segundo lab en Modena antes del verano "
            "de 2026. Necesitamos personas reales, no currículums perfectos.",
        "jobs": [
            {"role": "GRILLER",    "type": "JORNADA COMPLETA", "city": "BOLONIA"},
            {"role": "PIZZAIOLO",  "type": "MEDIA JORNADA",    "city": "BOLONIA"},
            {"role": "RUNNER & BARRA", "type": "FIN DE SEMANA", "city": "BOLONIA"},
        ],
        "jobs_cta_label": "MANDA UN MENSAJE",
        "jobs_cta_href":  "lavoro@bracestreetlab.it",

        # Social block
        "social_label": "SIGUENOS",
        "social": [
            {"platform": "INSTAGRAM", "handle": "@brace.lab",      "href": "https://instagram.com/brace.lab"},
            {"platform": "TIKTOK",    "handle": "@brace.bologna",  "href": "https://tiktok.com/@brace.bologna"},
        ],

        # Mini reservation/inquiry form
        "form_label":   "ESCRIBENOS",
        "form_heading": 'DOS LINEAS <em>BASTAN.</em>',
        "form_intro":
            "Para catering, grupos por encima de doce personas, proveedores. "
            "Para pedir escríbenos por WhatsApp, va más rápido.",
        "form_field_name":     "Nombre",
        "form_field_email":    "Email",
        "form_field_phone":    "Teléfono",
        "form_field_message":  "Qué te hace falta",
        "form_field_message_placeholder": "Catering, evento, proveedor, otro…",
        "form_submit_label":   "MANDA",
        "form_submit_note":
            "Demo de muestra · no se enviará ningún dato. Para pedir de "
            "verdad, llama al 051 234 5566 o escribe por WhatsApp.",
    },

    # No blog on Brace
    "posts": [],
}
