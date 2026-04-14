"""Bottega — Shop Artigianale (artisan-workshop archetype) — Spanish (ES).

Phase 2g3.5 — eCommerce live rollout (Session 41, 2026-04-14).

Voice contract (ES — peninsular, Apartamento / Loewe Craft Prize register):
- Native peninsular Spanish read by a Spanish customer visiting a small
  Tuscan artisan boutique. Warm, soulful, materially precise, never
  marketing-speak.
- ``tú`` form throughout — the bottega speaks like a friendly maker.
  Maison Luxe will carry ``usted``; Bottega stays cercana y cordial.
- Spanish punctuation: opening « ¿ » and « ¡ » where applicable; maker
  quotes wrapped in « » (peninsular comillas latinas).
- Concrete details: ciudades italianas quedan en italiano (Santa Croce
  sull'Arno, Montelupo Fiorentino, Prato, Greve in Chianti, Firenze,
  Toscana). Latin proper names and brand ``La Bottega di Martino``
  literal. Edition numbers (N° 042) and prices (€ 420) literal.
- Material vocab: cuero curtido al vegetal, cerámica torneada a mano,
  lino tejido, pieza única, edición, firmado por el artesano.
- Press names stay Italian (Vogue Italia, Domus, La Repubblica,
  Apartamento, Cereal Magazine).

Differentiation guard vs ``template_content_luxe_es.py`` (Maison Luxe):
- Bottega ES: ``tú`` + artisan warmth + tactile workshop vocab.
- Luxe ES: ``usted`` + maison/couture vocabulary + Vogue España register.
- If drift to usted or maison-fashion vocab appears, STOP.
"""
from __future__ import annotations

from typing import Any


BOTTEGA_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Bottega",   "kind": "home"},
        {"slug": "shop",     "label": "Catálogo",  "kind": "shop"},
        {"slug": "product",  "label": "Pieza",     "kind": "product"},
        {"slug": "atelier",  "label": "Atelier",   "kind": "about"},
        {"slug": "journal",  "label": "Cuaderno",  "kind": "journal"},
        {"slug": "contatti", "label": "Contacto",  "kind": "contact"},
    ],

    # Site-wide chrome (consumed by _base.html nav + footer).
    "site": {
        "logo_initial": "M",
        "logo_word":    "La Bottega di Martino",
        "tag":          "Firenze · desde 1968 · hecho a mano",
        "phone":        "+39 055 234 11 90",
        "whatsapp":     "055 234 11 90",
        "whatsapp_link": "https://wa.me/390552341190",
        "email":        "bottega@bottegadimartino.it",
        "address":      "Via dei Serragli 47/r · 50124 Firenze",
        "hours_compact": "Mar – Sáb · 10:00 – 19:30",
        "hours_footer_rows": [
            "Domingo · solo con cita previa",
            "Lunes · cerrado",
        ],
        "license":      "P.IVA 04891240484 · CCIAA Firenze REA 502118",
        "footer_intro":
            "Taller artesano fundado en 1968 por Martino Boncompagni. "
            "Cuero, cerámica y tejidos hechos a mano en la Toscana, en pequeñas "
            "ediciones que no se repiten. Envío en 48 horas en Italia, dos días más "
            "en el resto de Europa.",
        # Nav CTA — primary action button next to nav links
        "nav_cta":      "Visita la bottega",
        "nav_cta_kind": "appointment",  # links to /contatti/

        # Marketplace footer chrome labels
        "foot_studio":   "La bottega",
        "foot_pages":    "Mapa del sitio",
        "foot_contact":  "Bottega y pedidos",
        "foot_stockists":"Tiendas seleccionadas",
        "stockists_rows": [
            "10 Corso Como · Milano",
            "Eataly Lingotto · Torino",
            "Spazio B**K · Milano",
            "Atelier Pitti · Firenze",
        ],

        # Cross-page meta-strip labels (D-047 lifts on shop/product/atelier)
        "currency_symbol":  "€",
        "shop_filter_label": "Filtros",
        "shop_count_unit":   "piezas",
        "edition_label":     "Edición",
        "made_in_label":     "Hecho en",
        "artisan_label":     "Firmado por",
        "material_label":    "Material",
        "shipping_label":    "Envío",
        "shipping_value":    "48 horas en Italia · 4 días en Europa",
        "guarantee_label":   "Garantía",
        "guarantee_value":   "Reparación gratuita durante dos años",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Catálogo otoño · edición 47",
        "headline": "Piezas únicas cosidas, torneadas y tejidas <em>en la bottega.</em>",
        "intro":
            "Cuero curtido al vegetal en Santa Croce sull'Arno, cerámicas torneadas a mano en "
            "Montelupo Fiorentino, lino tejido en Prato. Cada pieza lleva la firma del artesano "
            "que la hizo — y un número correlativo que no se repite jamás.",
        "primary_cta":   "Visita la bottega",
        "primary_href":  "contatti",
        "secondary_cta": "Hojea el catálogo",
        "secondary_href":"shop",

        # Stamp-aside data — the rubber-stamped right column of the hero
        "stamp_label":  "Nuestra regla",
        "stamp_heading":"Tres manos, <em>un objeto.</em>",
        "stamp_rows": [
            ("Artesanos",    "12 talleres"),
            ("Materiales",   "100 % italianos"),
            ("Edición",      "Nunca más de 50"),
            ("Envío",        "En 48 horas"),
        ],
        "stamp_footer": "Escrito a mano · empaquetado en la bottega",
        "stamp_corner_index": "01",
        "stamp_corner_word":  "LA BOTTEGA",

        # Latest-arrived band — 4 product cards
        "latest_label":   "Las últimas llegadas",
        "latest_heading": "Recién salidas <em>del banco de trabajo.</em>",
        "latest_link_label": "Todo el catálogo",
        "latest_link_href":  "shop",
        "latest_items": [
            {
                "id":       "giubbotto-terra",
                "n":        "N° 042",
                "edition":  "3 / 8",
                "name":     "Cazadora Terra",
                "meta":     "Cuero vegetal · Santa Croce",
                "price":    "€ 420",
                "tag":      "Pieza única",
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "camicia-lino",
                "n":        "N° 108",
                "edition":  "1 / 6",
                "name":     "Camisa de lino",
                "meta":     "Lino crudo · Prato",
                "price":    "€ 95",
                "tag":      "Hecho a mano",
                "image":    "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "ceramica-cucina",
                "n":        "N° 213",
                "edition":  "7 / 24",
                "name":     "Vajilla de cocina",
                "meta":     "Cerámica esmaltada · Montelupo",
                "price":    "€ 148",
                "tag":      "Edición",
                "image":    "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "conserve-chianti",
                "n":        "N° 317",
                "edition":  "12 / 60",
                "name":     "Conservas del mercado",
                "meta":     "Tomates cherry · Chianti",
                "price":    "€ 18",
                "tag":      "Temporada",
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Makers band — 4 artisans with portrait
        "makers_label":   "Manos que firman",
        "makers_heading": "Doce talleres, <em>una sola enseña.</em>",
        "makers_intro":
            "Trabajamos solo con artesanos a los que conocemos por su nombre. "
            "Cada pieza que sale de nuestra enseña lleva su firma — "
            "porque quien la ha hecho tiene derecho a dar la cara.",
        "makers": [
            {
                "name":   "Severino Falchi",
                "craft":  "Maestro curtidor",
                "place":  "Santa Croce sull'Arno",
                "since":  "En el taller desde 1989",
                "quote":  "«El cuero bueno se reconoce por el olor. Si huele a química, no lo hemos curtido nosotros.»",
                "portrait": "https://images.unsplash.com/photo-1581094271901-8022df4466f9?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Caterina Lippi",
                "craft":  "Alfarera al torno",
                "place":  "Montelupo Fiorentino",
                "since":  "Taller abierto en 2003",
                "quote":  "«Cada pieza vuelve al horno tres veces. Si a la tercera no canta, la rompo.»",
                "portrait": "https://images.unsplash.com/photo-1604881991720-f91add269bed?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Bruno Ricci",
                "craft":  "Tejedor de lino",
                "place":  "Prato · Via del Telaio",
                "since":  "Telar manual desde 1976",
                "quote":  "«El lino crudo es una planta. Se trata como el pan: con calma y con hambre.»",
                "portrait": "https://images.unsplash.com/photo-1521119989659-a83eee488004?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Adele Pignatelli",
                "craft":  "Conservera del Chianti",
                "place":  "Greve in Chianti",
                "since":  "Tres generaciones de tarros",
                "quote":  "«La mermelada se hace cuando la fruta quiere. No cuando lo decide el calendario.»",
                "portrait": "https://images.unsplash.com/photo-1607743386760-88ac62b89b8a?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Provenance trio — 3 cards on materials & places
        "provenance_label":   "Procedencia",
        "provenance_heading": "Tres territorios, <em>tres materias.</em>",
        "provenance_intro":
            "Nada llega desde más de doscientos kilómetros. La materia prima es la primera firma "
            "del artesano: si sabe decirte dónde la ha cogido, te está diciendo cómo la ha trabajado.",
        "provenance_items": [
            {
                "icon":  "01",
                "title": "Cuero del Valdarno",
                "desc":  "Curtido al vegetal con corteza de castaño y mimosa. "
                         "Cuarenta días en cuba, nunca cromo, nunca atajos. "
                         "Proveedor único: Conceria Falchi, Santa Croce sull'Arno.",
                "place": "Santa Croce sull'Arno · 38 km de Firenze",
            },
            {
                "icon":  "02",
                "title": "Arcilla de Montelupo",
                "desc":  "Arcilla roja local, esmaltada en frío con óxidos naturales. "
                         "Tres cocciones a 980° en horno de leña. Torneado a mano alzada.",
                "place": "Montelupo Fiorentino · 22 km de Firenze",
            },
            {
                "icon":  "03",
                "title": "Lino de Prato",
                "desc":  "Lino crudo sin blanquear, tejido en telar mecánico de los años cincuenta. "
                         "Trama ancha, urdimbre cerrada. Cada rollo pesa distinto.",
                "place": "Prato · 24 km de Firenze",
            },
        ],

        # Care / guarantee strip
        "care_label":   "Garantías y cuidado",
        "care_heading": "Reparado en la bottega, <em>para siempre.</em>",
        "care_items": [
            ("Reparación gratuita durante dos años",
             "Asa descosida, esmalte desportillado, bordado flojo: te lo arreglamos nosotros, en la bottega."),
            ("Devolución aceptada siete días",
             "Si la pieza no te convence, la recogemos sin gastos y sin preguntas."),
            ("Envío en 48 horas",
             "Enviamos desde Firenze al día siguiente del pedido, en caja de papel grueso y cordel."),
            ("Pago seguro",
             "Tarjeta o transferencia. Sin suscripciones, sin cuentas, sin cookies publicitarias."),
        ],

        # Press / stockists strip
        "press_label":   "Hablan de nosotros",
        "press_items":   ["Vogue Italia", "Domus", "La Repubblica", "Apartamento", "Cereal Magazine"],

        "journal_teaser_label":   "Del cuaderno",
        "journal_teaser_heading": "Notas de taller, <em>escritas a mano.</em>",
        "journal_teaser_link":    "Abre el cuaderno",
        "journal_teaser_href":    "journal",

        # Final CTA band
        "cta_label":   "Visita la bottega",
        "cta_heading": "Ven a vernos a Firenze, <em>te invitamos a un café.</em>",
        "cta_intro":
            "La bottega está en via dei Serragli, a cuatro pasos de Pitti. Abierta de martes a "
            "sábado, de diez a siete y media de la tarde. Te enseñamos cómo se curte el cuero, "
            "cómo se tornea un plato y — si quieres — te presentamos a los artesanos en persona.",
        "cta_primary":   "Reserva una visita",
        "cta_primary_href": "contatti",
        "cta_secondary": "Escríbenos por WhatsApp",
        # cta_secondary_href is rendered as site.whatsapp_link
    },

    # ─── SHOP ─────────────────────────────────────────────────
    "shop": {
        "eyebrow":  "Catálogo · 47ª edición",
        "headline": "Todo el <em>banco de trabajo,</em> abierto.",
        "intro":
            "Cuarenta y siete piezas únicas, doce artesanos, tres territorios. "
            "Cada número es correlativo desde 1968 y no se repite jamás. Filtra por "
            "materia, por artesano o por disponibilidad.",

        "filter_section_label": "Filtra por",
        "filter_groups": [
            {
                "label": "Materia",
                "options": ["Cuero", "Cerámica", "Lino y tejidos", "Conservas", "Papel y encuadernación"],
            },
            {
                "label": "Artesano",
                "options": ["Severino Falchi", "Caterina Lippi", "Bruno Ricci", "Adele Pignatelli", "Todos"],
            },
            {
                "label": "Disponibilidad",
                "options": ["En la bottega", "Bajo reserva", "Edición agotada"],
            },
        ],

        "sort_label": "Ordena por",
        "sort_options": ["Últimas llegadas", "Número correlativo", "Precio ascendente", "Precio descendente"],

        "result_count":    "47 piezas actualmente en catálogo",
        "result_subtitle": "Actualizado los lunes por la mañana, antes de abrir la bottega",

        "products": [
            {
                "id":       "giubbotto-terra",
                "n":        "N° 042",
                "edition":  "3 / 8",
                "name":     "Cazadora Terra",
                "meta":     "Cuero vegetal teñido a mano",
                "place":    "Santa Croce sull'Arno",
                "artisan":  "Severino Falchi",
                "price":    "€ 420",
                "tag":      "Pieza única",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "borsa-cartolina",
                "n":        "N° 056",
                "edition":  "2 / 12",
                "name":     "Bolso Cartolina",
                "meta":     "Cuero natural + costura de guarnicionero",
                "place":    "Santa Croce sull'Arno",
                "artisan":  "Severino Falchi",
                "price":    "€ 280",
                "tag":      "Pieza única",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "camicia-lino",
                "n":        "N° 108",
                "edition":  "1 / 6",
                "name":     "Camisa de lino",
                "meta":     "Lino crudo sin blanquear",
                "place":    "Prato",
                "artisan":  "Bruno Ricci",
                "price":    "€ 95",
                "tag":      "Hecho a mano",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tovaglia-armaiolo",
                "n":        "N° 134",
                "edition":  "5 / 30",
                "name":     "Mantel Armaiolo",
                "meta":     "Lino y algodón · trama ancha",
                "place":    "Prato",
                "artisan":  "Bruno Ricci",
                "price":    "€ 165",
                "tag":      "Edición",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "ceramica-cucina",
                "n":        "N° 213",
                "edition":  "7 / 24",
                "name":     "Vajilla de cocina",
                "meta":     "Cerámica esmaltada en frío",
                "place":    "Montelupo Fiorentino",
                "artisan":  "Caterina Lippi",
                "price":    "€ 148",
                "tag":      "Edición",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tazze-tornite",
                "n":        "N° 219",
                "edition":  "11 / 24",
                "name":     "Tazas torneadas",
                "meta":     "Arcilla roja local · cocción en horno de leña",
                "place":    "Montelupo Fiorentino",
                "artisan":  "Caterina Lippi",
                "price":    "€ 78",
                "tag":      "Edición",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1610701596007-11502861dcfa?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "vassoio-noce",
                "n":        "N° 251",
                "edition":  "Agotado",
                "name":     "Bandeja de nogal",
                "meta":     "Nogal macizo · acabado al aceite",
                "place":    "Pratovecchio",
                "artisan":  "Severino Falchi",
                "price":    "€ 210",
                "tag":      "Lista de espera",
                "available": False,
                "image":    "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "conserve-chianti",
                "n":        "N° 317",
                "edition":  "12 / 60",
                "name":     "Conservas del mercado",
                "meta":     "Tomates cuore di bue + AOVE",
                "place":    "Greve in Chianti",
                "artisan":  "Adele Pignatelli",
                "price":    "€ 18",
                "tag":      "Temporada",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "marmellata-fichi",
                "n":        "N° 322",
                "edition":  "21 / 80",
                "name":     "Mermelada de higos",
                "meta":     "Higos negros de septiembre · cocción lenta",
                "place":    "Greve in Chianti",
                "artisan":  "Adele Pignatelli",
                "price":    "€ 14",
                "tag":      "Temporada",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Featured product detail link — used by smoke and "see more"
        "featured_product_id": "giubbotto-terra",

        "footer_note_label": "Bottega",
        "footer_note":
            "Sin algoritmos, sin recomendaciones: el catálogo está ordenado como en los estantes "
            "de la bottega. Si buscas una pieza concreta, escríbenos por WhatsApp — te respondemos "
            "nosotros, una persona a la vez.",
    },

    # ─── PRODUCT (detail) ─────────────────────────────────────
    "product": {
        # Hero (uses featured_product_id from shop)
        "id":       "giubbotto-terra",
        "n":        "N° 042",
        "edition":  "3 / 8",
        "edition_note": "Edición de ocho piezas · quedan tres",
        "name":     "Cazadora Terra",
        "subtitle": "Cuero curtido al vegetal · cosido a guarnicionero · teñido a mano",
        "price":    "€ 420",
        "vat_note": "IVA incluido · envío en 48 horas en Italia",
        "intro":
            "Una cazadora corta en cuero del Valdarno, curtida al vegetal durante cuarenta días "
            "con corteza de castaño y mimosa. El tinte se da a mano con un paño de lino empapado "
            "de pigmento natural tierra de Siena: cada pieza toma el color de forma ligeramente "
            "distinta y ninguna es nunca igual a la anterior.",

        "gallery": [
            "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=1200&q=80&auto=format&fit=crop",
        ],

        # Right-side info aside (the rubber-stamped data block)
        "info_label":  "Ficha técnica",
        "info_rows": [
            ("Materia",       "Cuero del Valdarno · curtición vegetal"),
            ("Grosor",        "1,8 mm uniforme"),
            ("Tinte",         "Tierra de Siena · pigmento natural"),
            ("Costura",       "Punto de guarnicionero, hilo encerado"),
            ("Forro",         "Lino crudo sin blanquear"),
            ("Botones",       "Cuerno de buey · procedencia Toscana"),
            ("Peso",          "780 g (talla M)"),
            ("Elaboración",   "11 días de taller"),
        ],

        # Sizing card
        "size_label":    "Tallas disponibles",
        "size_intro":    "A medida posible en tres semanas. Escríbenos por WhatsApp.",
        "size_options":  ["S", "M", "L", "XL", "A medida"],
        "size_chart_link": "Mira la guía de tallas",
        "size_chart_href": "atelier",

        # Made by
        "artisan_label": "Firmado por",
        "artisan_name":  "Severino Falchi",
        "artisan_role":  "Maestro curtidor · en el taller desde 1989",
        "artisan_bio":
            "Severino curte el cuero en su cuba desde 1989. Trabaja con dos hijos y un nieto, "
            "y tiñe cada piel a mano. Su lema en la tenería es «despacio es mejor».",
        "artisan_portrait":
            "https://images.unsplash.com/photo-1581094271901-8022df4466f9?w=400&q=80&auto=format&fit=crop",

        # Buy band
        "buy_primary":   "Añadir al cesto",
        "buy_secondary": "Escríbenos por WhatsApp",
        "buy_note":
            "Tarjeta, transferencia o pago a la entrega si recoges en la bottega. "
            "Enviamos en 48 horas, en caja de papel grueso y cordel.",

        # Care
        "care_label":   "Cuidado de la pieza",
        "care_intro":
            "El cuero vegetal pide poco y dura toda la vida. Ya lo hemos tratado en la tenería "
            "con aceite de linaza crudo. Los primeros meses cambiará de color muy poco, aclarándose "
            "en los pliegues — es normal y buscado.",
        "care_items": [
            ("Limpieza",      "Paño seco. Nunca detergentes, nunca alcohol."),
            ("Hidratación",   "Aceite de linaza o crema neutra una vez al año."),
            ("Reparación",    "Durante dos años la hacemos gratis en la bottega."),
            ("Lluvia",        "Seca lejos de fuentes de calor. Nada de secadores."),
        ],

        # Provenance map
        "provenance_label":   "Procedencia",
        "provenance_heading": "Tres etapas, <em>cuarenta kilómetros.</em>",
        "provenance_steps": [
            ("01", "Tenería",     "Conceria Falchi · Santa Croce sull'Arno · 38 km"),
            ("02", "Tintado",     "Bottega di Martino · Firenze · 0 km"),
            ("03", "Costura",     "Bottega di Martino · Firenze · 0 km"),
            ("04", "Embalaje",    "Papel de estraza de Greve in Chianti · 32 km"),
        ],

        # Related products band
        "related_label":   "También de la misma mano",
        "related_intro":   "Piezas nacidas en el mismo taller, de la misma firma.",
        "related_items": [
            {
                "id":      "borsa-cartolina",
                "n":       "N° 056",
                "name":    "Bolso Cartolina",
                "meta":    "Cuero natural · Severino Falchi",
                "price":   "€ 280",
                "image":   "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":      "vassoio-noce",
                "n":       "N° 251",
                "name":    "Bandeja de nogal",
                "meta":    "Nogal macizo · Severino Falchi",
                "price":   "€ 210",
                "image":   "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":      "ceramica-cucina",
                "n":       "N° 213",
                "name":    "Vajilla de cocina",
                "meta":    "Cerámica esmaltada · Caterina Lippi",
                "price":   "€ 148",
                "image":   "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
        ],
    },

    # ─── ATELIER (about) ──────────────────────────────────────
    "atelier": {
        "eyebrow":  "El atelier de via dei Serragli",
        "headline": "Una bottega <em>de bottega.</em>",
        "intro":
            "Abierta en 1968 por Martino Boncompagni, hoy es un espacio de ciento diez metros "
            "cuadrados en via dei Serragli, donde doce artesanos toscanos traen sus piezas tres "
            "veces por semana. Sin almacén central, sin cadena — todo lo que ves en el escaparate "
            "está hecho a menos de doscientos kilómetros de aquí.",

        # Mission stamp panel
        "mission_label":   "La regla de la bottega",
        "mission_heading": "Tres manos, un objeto. <em>Siempre.</em>",
        "mission_text":
            "Cada pieza pasa por tres manos: quien trabaja la materia prima, quien la remata, quien "
            "comprueba que el número correlativo esté escrito a pluma antes del envío. Ninguna "
            "máquina sustituye a la última firma. Si no conseguimos que una pieza pase por tres "
            "manos, no la hacemos.",

        # Process timeline — 5 steps
        "process_label":   "El recorrido",
        "process_heading": "De la materia prima <em>al cordel.</em>",
        "process_steps": [
            {
                "n":    "01",
                "title":"Vamos a por la materia",
                "place":"Valdarno · Mugello · Chianti",
                "desc": "Cuero de las tenerías del Valdarno, arcilla roja de Montelupo, "
                        "lino de los telares de Prato. Vamos personalmente, nunca por mensajero.",
                "duration": "Una semana al mes",
            },
            {
                "n":    "02",
                "title":"Se deja reposar",
                "place":"Bottega · trastienda",
                "desc": "El cuero está cuarenta días en cuba. La arcilla se seca despacio "
                        "al aire. El lino espera a que cambie el tiempo. Sin ciclos acelerados.",
                "duration": "De dos semanas a tres meses",
            },
            {
                "n":    "03",
                "title":"Se trabaja a mano",
                "place":"Banco de trabajo · vidriera al jardín",
                "desc": "La pieza toma forma bajo las manos del artesano principal. "
                        "Costura de guarnicionero, torneado libre, telar mecánico de los años cincuenta.",
                "duration": "De cuatro a doce días",
            },
            {
                "n":    "04",
                "title":"Se remata",
                "place":"Bottega · banco de Anna",
                "desc": "Anna comprueba, lija, tiñe. Añade el número correlativo. "
                        "Si no pasa su control, vuelve al banco principal.",
                "duration": "Media jornada por pieza",
            },
            {
                "n":    "05",
                "title":"Se empaqueta",
                "place":"Bottega · banco de embalaje",
                "desc": "Papel de estraza de Greve, cordel de cáñamo, tarjeta escrita a mano "
                        "con el nombre de quien ha hecho la pieza. Enviamos desde Firenze en 48 horas.",
                "duration": "El mismo día del envío",
            },
        ],

        # Founder
        "founder_label":   "Quiénes somos",
        "founder_heading": "Martino, Anna, <em>y doce talleres.</em>",
        "founder_text":
            "Martino abrió en el 68 con un banco de tres metros y un fardo de cuero. Hoy lleva "
            "la bottega con su sobrina Anna — él está más en el banco, ella se ocupa de quien entra, "
            "de quien llama, de quien escribe. Juntos mantienen el trato con los doce artesanos. "
            "Sin llegar a ser nunca una empresa.",
        "founder_portrait":
            "https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=600&q=80&auto=format&fit=crop",
        "founder_caption":
            "Martino Boncompagni y Anna Boncompagni · Bottega de via dei Serragli, Firenze",

        # Numbers stamp
        "numbers_label":   "Cifras de la bottega",
        "numbers_items": [
            ("57",     "años de apertura ininterrumpida"),
            ("12",     "artesanos que firman para nosotros"),
            ("47ª",    "edición del catálogo"),
            ("0",      "maquinaria industrial"),
        ],

        # Visit card
        "visit_label":   "Ven a vernos",
        "visit_heading": "Via dei Serragli 47/r, <em>a cuatro pasos de Pitti.</em>",
        "visit_text":
            "La bottega abre de martes a sábado, de diez a siete y media. Los domingos solo con "
            "cita previa. Si vienes el jueves por la tarde, suele haber algún artesano de visita "
            "entregando piezas. Café y libro de visitas listos.",
        "visit_primary":   "Reserva una visita",
        "visit_primary_href": "contatti",
        "visit_secondary": "Escríbenos por WhatsApp",
    },

    # ─── JOURNAL ──────────────────────────────────────────────
    "journal": {
        "eyebrow":  "El cuaderno de la bottega",
        "headline": "Notas de taller, <em>escritas a pluma.</em>",
        "intro":
            "Una página al mes, escrita por Anna en las tardes tranquilas. Se habla de quién ha "
            "venido a vernos, de un material nuevo que ha llegado, de una pieza que ha exigido "
            "el doble de tiempo. No es un blog: es el diario de la bottega.",

        "list_label":  "Notas recientes",
        "entries": [
            {
                "n":      "47",
                "title":  "Un otoño de tintes naturales",
                "place":  "Bottega · 12 de marzo de 2026",
                "excerpt":
                    "Severino ha vuelto de la tenería con seis pieles teñidas solo con corteza de "
                    "castaño. En la cazadora Terra ya es el tinte del próximo lote.",
                "minutes":"3 minutos de lectura",
            },
            {
                "n":      "46",
                "title":  "Caterina y el horno que canta",
                "place":  "Montelupo · 22 de febrero de 2026",
                "excerpt":
                    "Caterina ha rehecho el horno de leña de su taller. La primera cocción ha sido "
                    "de seis piezas y todas han cantado al enfriarse. Es buena señal.",
                "minutes":"4 minutos de lectura",
            },
            {
                "n":      "45",
                "title":  "El telar de Bruno vuelve a sonar",
                "place":  "Prato · 31 de enero de 2026",
                "excerpt":
                    "Estuvo parado dos meses por el cambio del peine. Bruno ha vuelto a tejer "
                    "el lunes. La primera pieza es un mantel de lino color arena.",
                "minutes":"5 minutos de lectura",
            },
            {
                "n":      "44",
                "title":  "Adele en el mercado de Greve",
                "place":  "Chianti · 14 de diciembre de 2025",
                "excerpt":
                    "Adele fue al mercado de diciembre a por los higos tardíos. Las mermeladas "
                    "de enero son todas de esa recogida.",
                "minutes":"3 minutos de lectura",
            },
            {
                "n":      "43",
                "title":  "Una jornada en la tenería",
                "place":  "Santa Croce · 8 de noviembre de 2025",
                "excerpt":
                    "Anna pasó un día con Severino. Se ve cómo una piel entra en cuba, se gira "
                    "cada cuatro días, y después de cuarenta sale distinta.",
                "minutes":"6 minutos de lectura",
            },
            {
                "n":      "42",
                "title":  "Conservas, libros y manos nuevas",
                "place":  "Firenze · 19 de octubre de 2025",
                "excerpt":
                    "Desde octubre dos nuevos artesanos trabajan para la bottega: un encuadernador "
                    "de Pistoia y una papelera de San Frediano. Ediciones en camino para primavera.",
                "minutes":"4 minutos de lectura",
            },
        ],

        "footer_note_label": "Cuaderno",
        "footer_note":
            "Las páginas antiguas se quedan, no las actualizamos. Si te gusta recibir el cuaderno "
            "en papel, escríbenos un correo — te lo mandamos impreso dos veces al año.",
    },

    # ─── CONTATTI (form) ──────────────────────────────────────
    "contatti": {
        "eyebrow":  "Ven a vernos",
        "headline": "Escribe, llama, <em>o pásate.</em>",
        "intro":
            "La bottega está en via dei Serragli, a cuatro pasos de Pitti. Abierta de martes a "
            "sábado, de diez a siete y media. Si quieres saber si una pieza sigue en el escaparate, "
            "escríbenos por WhatsApp — te respondemos en menos de una hora.",

        # Two-column layout: left form, right contact card
        "form_section_label": "Mándanos dos líneas",
        "form_section_intro":
            "Bastan nombre, contacto y qué estás buscando. Te responde Anna antes de acabar el "
            "día laboral siguiente. Si quieres pedir una pieza a medida, escríbelo aquí abajo: "
            "te devolvemos un boceto con tiempos y precios en tres días.",

        # Form helper
        "form_helper_required":  "Los campos con asterisco son obligatorios",
        "form_submit_button":    "Envía la solicitud",
        "form_submit_note":      "Sin boletines. Usamos tus líneas solo para responderte.",

        "form_fields": [
            {"name": "nome",          "label": "Nombre y apellidos",    "type": "text",     "placeholder": "Ej. María García", "required": True},
            {"name": "email",         "label": "Correo electrónico",    "type": "email",    "placeholder": "maria@ejemplo.es", "required": True},
            {"name": "telefono",      "label": "Teléfono o WhatsApp",   "type": "tel",      "placeholder": "Opcional · +34 …", "required": False},
            {"name": "interesse",     "label": "Qué te interesa",       "type": "select",   "required": True,
             "options": ["Una pieza del catálogo", "Un encargo a medida", "Una visita a la bottega", "Una colaboración", "Prensa y medios"]},
            {"name": "pezzo",         "label": "Pieza o número (opc.)", "type": "text",     "placeholder": "Ej. N° 042 · Cazadora Terra", "required": False},
            {"name": "messaggio",     "label": "Tu petición",           "type": "textarea", "placeholder": "Cuéntanos qué estás buscando, con dos líneas nos vale.", "required": True, "rows": 5},
        ],

        # Right-side card
        "card_label":   "Bottega di Martino",
        "card_address_label":  "Dirección",
        "card_address_value":  "Via dei Serragli 47/r · 50124 Firenze",
        "card_phone_label":    "Teléfono",
        "card_phone_value":    "+39 055 234 11 90",
        "card_whatsapp_label": "WhatsApp",
        "card_whatsapp_value": "055 234 11 90",
        "card_email_label":    "Correo",
        "card_email_value":    "bottega@bottegadimartino.it",
        "card_hours_label":    "Horario de apertura",
        "card_hours_rows": [
            "Martes – sábado · 10:00 – 19:30",
            "Domingo · solo con cita previa",
            "Lunes · cerrado",
        ],
        "card_directions_label": "Cómo llegar",
        "card_directions_text":
            "Tres minutos a pie desde Palazzo Pitti. Autobús 11, parada Serragli. "
            "Desde la estación SMN: quince minutos a pie atravesando el centro.",

        # FAQ accordion
        "faq_label":   "Preguntas frecuentes",
        "faq_items": [
            {
                "q": "¿Enviáis al extranjero?",
                "a": "Sí, a toda Europa en cuatro días laborables. Para Estados Unidos y "
                     "Japón escríbenos antes — confirmamos los tiempos caso por caso.",
            },
            {
                "q": "¿Puedo ver una pieza antes de comprarla?",
                "a": "Claro. Resérvala llamando a la bottega y, cuando pases, te la enseñamos "
                     "sin compromiso. Si no te convence, ninguna presión.",
            },
            {
                "q": "¿Hacéis encargos a medida?",
                "a": "Sí, en cuero, cerámica y tejido. Plazos: de tres a ocho semanas según "
                     "la pieza. Señal del treinta por ciento al confirmar el boceto.",
            },
            {
                "q": "¿Qué pasa si la pieza se rompe?",
                "a": "Durante dos años te la arreglamos en la bottega sin coste. Para reparaciones "
                     "posteriores, aplicamos un coste simbólico — normalmente por debajo de los treinta euros.",
            },
        ],
    },
}
