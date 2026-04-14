"""Luxe — Fashion Store (fashion-editorial archetype) — ES content tree.

Phase 2g3.5 — eCommerce live rollout (Session 41, 2026-04-14).

Voice contract (ES, peninsular):
- Maison editorial italiana dirigiéndose a cliente española — registro
  Vogue España / Loewe / The Gentlewoman edición ES / Vanidad.
- USTED formal en todo el árbol (nunca tú): «el perfil de Usted», «Sus
  medidas», «Le reservamos». Esta es la frontera explícita frente a
  Bottega ES, que emplea tú artesanal y cálido.
- Cadencia de prensa de moda española: «atelier», «maison», «visita
  privada», «drop», «cápsula», «lista de espera», «con cita previa»,
  «concierge». Nunca «checkout», «carrito» ni «taller»: la conversión
  es una cita privada con la dirección de clientes.
- Puntuación española: ¿ ¡ de apertura donde corresponde. Comillas
  angulares « » para citas editoriales. Precio en formato peninsular
  «2.480 €» (número + espacio + símbolo).
- Topónimos españoles: Milán, París, Tokio, Florencia. Biella y Como
  se conservan en su grafía italiana por tradición textil. Nombres
  propios de diseñador, marca, magazine y producto se conservan
  LITERALES: «Maison Luxe», «Rack Atelier», «Bomber Siena», «Vogue
  Italia», «The Gentlewoman», «Carla Sozzani», «Grand Hôtel Villa
  d'Este».
- Tejidos en ES cuando tienen equivalente natural («cachemira alpaca»,
  «lana cardada», «crepé de seda», «piel napa»); italianos cuando
  forman parte del lenguaje técnico sartorial («cady», «sellier»).

Differentiation contract vs Bottega ES (D-054 enforcement):
- Luxe ES: usted + maison editorial + vocabulario «atelier / visita
  privada / lista de espera / cápsula / drop / RSVP / concierge».
- Bottega ES: tú + artesano cálido + «taller / hecho a mano / edición
  artesanal / WhatsApp». Nunca debe haber solapamiento de vocabulario.
"""
from __future__ import annotations

from typing import Any


LUXE_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Maison",     "kind": "home"},
        {"slug": "collezione", "label": "Colección",  "kind": "collection"},
        {"slug": "product",    "label": "Look",       "kind": "product"},
        {"slug": "maison",     "label": "Atelier",    "kind": "about"},
        {"slug": "lookbook",   "label": "Lookbook",   "kind": "lookbook"},
        {"slug": "contatti",   "label": "Privado",    "kind": "contact"},
    ],

    # Site-wide chrome (consumed by _base.html nav + footer).
    "site": {
        "logo_initial": "L",
        "logo_word":    "Maison Luxe",
        "logo_subline": "Milán · París · Tokio",
        "tag":          "Atelier · Primavera–Verano 2026",
        "phone":        "+39 02 7600 1492",
        "private_phone_label": "Dirección de clientes",
        "email":        "private@maisonluxe.com",
        "private_email_label": "Concierge de clientes",
        "address":      "Via Senato 28 · 20121 Milán",
        "showroom_paris": "9 rue du Mail · 75002 París",
        "showroom_tokyo": "1-1-7 Aoyama · Minato-ku · Tokio",
        "hours_compact": "Mar – Sáb · 11:00 – 19:00 · con cita previa",
        "hours_footer_rows": [
            "Domingo · privado",
            "Lunes · cerrado",
        ],
        "license":      "Maison Luxe Srl · P.IVA 11489720152 · CCIAA Milano REA 2589441",
        "footer_intro":
            "Maison fundada en Milán en 2014 por Giulia Maison, con atelier en París y "
            "showroom en Tokio. Prendas dibujadas y cosidas entre Milán y París, en series "
            "limitadas, exclusivamente en lista de espera. Dos drops por temporada, de "
            "cuarenta y cinco prendas y nueve siluetas firmadas.",

        # Nav reservation CTA (private viewing)
        "nav_cta":      "Solicitar visita",
        "nav_cta_kind": "appointment",  # links to /contatti/

        # Marketplace footer chrome labels
        "foot_studio":   "La maison",
        "foot_pages":    "Mapa",
        "foot_contact":  "Dirección de clientes",
        "foot_offices":  "Ateliers y showroom",
        "office_rows": [
            "Milán · Via Senato 28",
            "París · 9 rue du Mail",
            "Tokio · 1-1-7 Aoyama",
        ],

        # Cross-page meta-strip labels (D-047)
        "currency_symbol":  "€",
        "collection_label": "Colección",
        "drop_label":       "Drop",
        "season_label":     "Temporada",
        "shipping_label":   "Entrega reservada",
        "shipping_value":   "Mensajería maison Milán · 48 horas España · 72 horas Europa",
        "viewing_label":    "Visita privada",
        "viewing_value":    "Solo con cita previa · concierge dedicado",
        "waitlist_label":   "Lista de espera",
        "rsvp_label":       "RSVP",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "issue":    "Issue 12 · Primavera '26",
        "issue_label": "Issue",
        "cover_styling_label": "Estilismo",
        "cover_styling_name":  "Carla Sozzani",
        "cover_label":         "Portada",
        "cover_subject":       "La Muse en Velours",
        "cover_image":
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1600&q=80&auto=format&fit=crop",

        "eyebrow":  "Lookbook · Primavera Verano 2026",
        "headline": "El nuevo cuerpo <em>del vestir.</em>",
        "headline_credit_line": "Cincuenta prendas · noventa gestos de sastrería",
        "intro":
            "Una sola colección, tejida entre Como y Prato, fotografiada en el Grand Hôtel "
            "Villa d'Este. Drops mensuales, exclusivamente para quien esté en lista de "
            "espera. La maison nunca vende dos veces la misma prenda.",

        "primary_cta":   "Acceder al lookbook",
        "primary_href":  "lookbook",
        "secondary_label":   "Dirección creativa",
        "secondary_name":    "Giulia Maison",

        # Editorial tile strip — 4 silhouettes pinned below hero
        "edition_label":   "Edición limitada",
        "edition_subline": "cuatro piezas seleccionadas",
        "tiles": [
            {
                "id":       "rack-atelier",
                "tag":      "Nuevo",
                "name":     "Rack Atelier",
                "price":    "2.480 €",
                "image":    "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "bomber-siena",
                "tag":      "Cápsula",
                "name":     "Bomber Siena",
                "price":    "1.290 €",
                "image":    "https://images.unsplash.com/photo-1551803091-e20673f15770?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "pelletteria-isola",
                "tag":      "Atelier",
                "name":     "Borsa Isola",
                "price":    "860 €",
                "image":    "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "tag":      "Archivo",
                "name":     "Sessione Vogue",
                "price":    "1.940 €",
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200&q=80&auto=format&fit=crop",
            },
        ],

        # Manifesto / maison statement
        "manifesto_label":   "Maison statement",
        "manifesto_heading": "Cuarenta y cinco prendas <em>por temporada, ni una más.</em>",
        "manifesto_text":
            "Dibujamos la colección dos veces al año, en un atelier de ciento cuarenta metros "
            "cuadrados entre Brera y Sentier. Cada prenda se corta a mano, se cose a la "
            "medida de la clienta y queda firmada por quien la ha realizado. Nada de outlet, "
            "nada de rebajas, nada de marcas revendidas. Sólo lo que ha salido de la maison.",

        # Atelier numbers — KPI strip
        "atelier_numbers_label":   "El atelier en cifras",
        "atelier_numbers": [
            ("12",     "años de maison"),
            ("45",     "prendas por temporada"),
            ("9",      "siluetas firmadas"),
            ("3",      "ateliers en el mundo"),
        ],

        # Lookbook teaser — editorial 3-tile
        "lookbook_teaser_label":   "Lookbook en curso",
        "lookbook_teaser_heading": "Dieciocho imágenes, <em>una sola luz.</em>",
        "lookbook_teaser_intro":
            "Fotografiado en el Grand Hôtel Villa d'Este, sobre el lago de Como, con luz "
            "natural de marzo. Estilismo a cargo de Carla Sozzani, fotografía de Letizia "
            "Carrera, dirección artística de la maison.",
        "lookbook_teaser_link": "Hojear el lookbook",
        "lookbook_teaser_href": "lookbook",
        "lookbook_teaser_tiles": [
            {
                "title":   "Look 03 · Cady doble capa",
                "credit":  "Estilismo · Carla Sozzani",
                "image":   "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "title":   "Look 09 · Lana cardada de Biella",
                "credit":  "Fotografía · Letizia Carrera",
                "image":   "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "title":   "Look 14 · Crepé de seda de Como",
                "credit":  "Atelier · Sentier París",
                "image":   "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1000&q=80&auto=format&fit=crop",
            },
        ],

        # Press / editorial mentions strip
        "press_label":   "Editorial",
        "press_intro":   "Reseñada en",
        "press_items":   ["Vogue Italia", "The Gentlewoman", "AnOther Magazine", "Le Monde D'Hermès", "Wallpaper*"],

        # Seasonal drop card
        "drop_label":    "Próximo drop",
        "drop_heading":  "SS26 · Cápsula 04 — <em>la luz de Como.</em>",
        "drop_subhead":  "Apertura de lista de espera · viernes 24 de abril, 11:00 CET",
        "drop_metadata": [
            ("Prendas",      "9 siluetas"),
            ("Materia",      "Crepé de seda · cady · alpaca"),
            ("Exclusividad", "12 piezas por silueta"),
            ("Apertura",     "Lista de espera · viernes 24 de abril"),
        ],
        "drop_cta":      "Inscribirse a la lista",
        "drop_cta_href": "contatti",

        # Private viewing CTA band
        "private_label":   "Visita privada",
        "private_heading": "Tres salones, <em>una sala reservada para Usted.</em>",
        "private_intro":
            "Las maisons de Milán, París y Tokio abren solo con cita previa. La dirección "
            "de clientes reserva una hora de sala, prepara las prendas de Su perfil y "
            "organiza la prueba con la modista. Servicio gratuito · concierge dedicado.",
        "private_primary":     "Solicitar una visita privada",
        "private_primary_href":"contatti",
        "private_secondary":   "Ver los ateliers",
        "private_secondary_href":"maison",
    },

    # ─── COLLEZIONE (shop list) ───────────────────────────────
    "collezione": {
        "season_chip":  "Primavera–Verano 2026",
        "eyebrow":      "Colección completa · drop 04 · cápsulas 01–04",
        "headline":     "Cuarenta y cinco prendas, <em>nueve siluetas firmadas.</em>",
        "intro":
            "La colección íntegra Primavera–Verano 2026, ordenada por silueta. Cada prenda "
            "se reserva exclusivamente en lista de espera: desde la confirmación hasta la "
            "entrega, de cuatro a seis semanas.",

        "filter_label":  "Filtrar",
        "filter_groups": [
            {
                "label": "Silueta",
                "options": ["Traje fluido", "Robe-manteau", "Pantalón wide", "Punto editorial", "Marroquinería atelier"],
            },
            {
                "label": "Materia",
                "options": ["Cachemira alpaca", "Cady doble capa", "Crepé de seda de Como", "Lana cardada de Biella", "Piel de Florencia"],
            },
            {
                "label": "Disponibilidad",
                "options": ["En showroom", "Lista de espera abierta", "Agotado · bajo reserva"],
            },
        ],
        "sort_label":    "Ordenar",
        "sort_options":  ["Por silueta", "Por drop", "Precio ascendente", "Novedades"],

        "result_count":     "45 prendas en la colección",
        "result_subtitle":  "Actualizada el primer día de cada mes, tras el drop",

        "products": [
            {
                "id":       "robe-manteau-grigio-perla",
                "n":        "Look 03",
                "name":     "Robe-manteau Gris Perla",
                "meta":     "Cachemira alpaca doble · Maglificio Lanifer Biella",
                "drop":     "Drop 01 · Spring 26",
                "price":    "2.840 €",
                "tag":      "Lista de espera",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tailleur-cady-bianco",
                "n":        "Look 07",
                "name":     "Tailleur Cady Blanco",
                "meta":     "Cady doble capa · Setificio Tessitura Como",
                "drop":     "Drop 02 · Spring 26",
                "price":    "3.420 €",
                "tag":      "En showroom",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "rack-atelier-nero",
                "n":        "Look 11",
                "name":     "Rack Atelier Negro",
                "meta":     "Piel napa de Florencia · costura sellier",
                "drop":     "Drop 02 · Spring 26",
                "price":    "2.480 €",
                "tag":      "Lista de espera",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1551803091-e20673f15770?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "bomber-siena",
                "n":        "Look 14",
                "name":     "Bomber Siena",
                "meta":     "Cady teñido en Siena · bordado Atelier Sentier",
                "drop":     "Drop 03 · Summer 26",
                "price":    "1.290 €",
                "tag":      "Cápsula",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "pantalone-wide-crepe",
                "n":        "Look 16",
                "name":     "Pantalón Wide Crepé",
                "meta":     "Crepé de seda de Como · cinturón sellier",
                "drop":     "Drop 03 · Summer 26",
                "price":    "1.180 €",
                "tag":      "Lista de espera",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "borsa-isola",
                "n":        "Look 18",
                "name":     "Borsa Isola",
                "meta":     "Piel Atelier Firenze · pochette de día",
                "drop":     "Drop 03 · Summer 26",
                "price":    "860 €",
                "tag":      "Atelier",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "abito-sera-organza",
                "n":        "Look 22",
                "name":     "Vestido de Noche Organza",
                "meta":     "Organza trenzada de Como · bordado Lesage",
                "drop":     "Drop 04 · Summer 26",
                "price":    "4.690 €",
                "tag":      "Agotado · reservable",
                "available":False,
                "image":    "https://images.unsplash.com/photo-1611042553365-9b101441c135?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "maglia-cashmere-corta",
                "n":        "Look 24",
                "name":     "Jersey Cachemira Corto",
                "meta":     "Cachemira de 12 cabos · Maglificio Lanifer Biella",
                "drop":     "Drop 04 · Summer 26",
                "price":    "1.420 €",
                "tag":      "Lista de espera",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "n":        "Look 26",
                "name":     "Sessione Vogue",
                "meta":     "Abrigo de archivo · reedición drop 2024",
                "drop":     "Archivo · 2024",
                "price":    "1.940 €",
                "tag":      "Archivo",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
        ],

        "featured_product_id": "rack-atelier-nero",

        "footer_note_label": "Drop 04 en apertura",
        "footer_note":
            "Las inscripciones al Drop 04 — cápsula de la luz de Como — abren el viernes 24 "
            "de abril a las 11:00 CET. Las clientas ya inscritas en lista de espera tienen "
            "prioridad absoluta sobre todas las siluetas. Para ser añadida a la lista: "
            "escribir directamente a la dirección de clientes.",
    },

    # ─── PRODUCT DETAIL ───────────────────────────────────────
    "product": {
        "id":       "rack-atelier-nero",
        "n":        "Look 11 · Drop 02",
        "name":     "Rack Atelier Negro",
        "subtitle": "Piel napa de Florencia · costura sellier · perfil gold",
        "price":    "2.480 €",
        "vat_note": "IVA incluido · entrega por mensajería maison · 48 horas España",
        "tag":      "Lista de espera · Drop 02 SS26",
        "intro":
            "Bolso de día y noche en piel napa de Florencia, cosido a mano en el atelier de "
            "Sentier con costura sellier dorada a tres caras. Perfil pulido con cera de "
            "abeja, fondo reforzado en piel Vacchetta. Diseñado sobre el cuerpo de la "
            "directora creativa, producido en doce ejemplares numerados, firmado en el "
            "fondo por el atelier que lo ha realizado.",

        "gallery": [
            "https://images.unsplash.com/photo-1551803091-e20673f15770?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1591561954557-26941169b49e?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1611042553365-9b101441c135?w=1400&q=80&auto=format&fit=crop",
        ],

        # Editorial caption strip below gallery
        "gallery_caption_styling":  "Estilismo · Carla Sozzani",
        "gallery_caption_photo":    "Foto · Letizia Carrera",
        "gallery_caption_location": "Grand Hôtel Villa d'Este · marzo de 2026",

        # Right-side info panel — italic captioned
        "info_label":  "Fichas del atelier",
        "info_rows": [
            ("Atelier",      "Sentier · París"),
            ("Materia",      "Napa de Florencia · curtido vegetal"),
            ("Costura",      "Sellier dorada a tres caras · hilo encerado"),
            ("Perfil",       "Cera de abeja · pulido a mano"),
            ("Fondo",        "Vacchetta reforzada · tacos de latón"),
            ("Herrajes",     "Latón bañado en oro de 24 K"),
            ("Medidas",      "32 × 24 × 12 cm · bandolera 105 cm"),
            ("Elaboración",  "21 horas de atelier por pieza"),
        ],

        # Sizing / variant card (silhouette comes in 2 dimensions + 3 tonalities)
        "size_label":    "Tamaño",
        "size_options":  ["Día · 32 × 24", "Noche · 25 × 18"],
        "color_label":   "Tonalidad",
        "color_options": ["Negro noche", "Burdeos Como", "Marfil crema"],

        # Edition note
        "edition_label": "Edición",
        "edition_value": "12 ejemplares numerados · n.º 03/12 disponible",
        "edition_note":
            "Cada ejemplar va marcado en frío en el interior con el número progresivo, el "
            "nombre del sellier principal y la fecha de entrega en atelier.",

        # Atelier signature
        "atelier_label":   "Firmado por el atelier",
        "atelier_name":    "Atelier Sentier · París",
        "atelier_founded": "Abierto en 2017",
        "atelier_text":
            "Atelier de marroquinería de gestión directa de la maison, en rue du Mail. Seis "
            "sellier formados en las escuelas de Hermès y Goyard, una cortadora y una "
            "pulidora. Trabajan exclusivamente para Maison Luxe — ningún tercero, ninguna "
            "producción bajo marca blanca.",
        "atelier_portrait":
            "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=600&q=80&auto=format&fit=crop",

        # Buy band — private request style
        "buy_primary":   "Solicitar a la maison",
        "buy_primary_href":  "contatti",
        "buy_secondary": "Añadir a la lista de espera",
        "buy_note":
            "Adquisición con cita previa o solicitud directa a la dirección de clientes. "
            "Señal del treinta por ciento en la confirmación. Entrega en 4–6 semanas desde "
            "el pedido, por mensajería maison Milán, en caja firmada.",

        # Care section (italic editorial style)
        "care_label":   "Cuidado de la pieza",
        "care_intro":
            "La napa de Florencia es una piel viva: adopta la forma de quien la lleva, "
            "ablandándose en los primeros meses sin perder jamás estructura. Tratada en "
            "atelier con cera de abeja neutra, no requiere mantenimiento durante los dos "
            "primeros años de uso diario.",
        "care_items": [
            ("Limpieza",      "Paño suave ligeramente húmedo. Nunca productos químicos."),
            ("Hidratación",   "Cera de abeja maison cada doce meses. Stick incluido de serie."),
            ("Conservación",  "Bolsa de algodón biológico, nunca plástico. Nunca sol directo."),
            ("Lluvia",        "Secado natural a la sombra. Después, una pasada de cera."),
        ],

        # Atelier provenance
        "provenance_label":   "Procedencia",
        "provenance_heading": "Cuatro etapas, <em>cuatro firmas.</em>",
        "provenance_steps": [
            ("01", "Curtiduría",      "Conceria della Madonna · Florencia · curtido vegetal 45 días"),
            ("02", "Corte",           "Atelier Sentier · París · corte a mano alzada"),
            ("03", "Costura sellier", "Atelier Sentier · París · 21 horas por pieza"),
            ("04", "Embalaje",        "Maison Milán · caja y cordón firmados"),
        ],

        # Related — three other atelier pieces
        "related_label":   "Del mismo atelier",
        "related_intro":   "Marroquinería firmada Sentier · París.",
        "related_items": [
            {
                "id":      "borsa-isola",
                "n":       "Look 18",
                "name":    "Borsa Isola",
                "meta":    "Pochette de día · Atelier Sentier",
                "price":   "860 €",
                "image":   "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "rack-atelier",
                "n":        "Look 09",
                "name":     "Rack Atelier Crema",
                "meta":     "Bolso de día · Atelier Sentier",
                "price":    "2.480 €",
                "image":    "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "n":        "Look 26",
                "name":     "Abrigo Sessione Vogue",
                "meta":     "Abrigo de archivo · drop 2024",
                "price":    "1.940 €",
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
        ],
    },

    # ─── MAISON (about) ───────────────────────────────────────
    "maison": {
        "eyebrow":  "La maison",
        "headline": "Tres ciudades, <em>una sola firma.</em>",
        "intro":
            "Maison Luxe fue fundada en Milán en 2014 por Giulia Maison, tras ocho años "
            "entre Hermès y Bottega Veneta. Hoy dibuja dos colecciones al año, en ateliers "
            "entre Brera y Sentier, y recibe sólo con cita previa en las tres maisons de "
            "Milán, París y Tokio. Cuarenta y cinco prendas por temporada, ni una más.",

        # Maison statement panel
        "statement_label":   "Statement",
        "statement_heading": "Cuarenta y cinco prendas <em>por temporada.</em>",
        "statement_text":
            "La cantidad es una decisión editorial, no una limitación. Cada prenda debe "
            "poder ser dibujada por la directora creativa, cortada en atelier, cosida por "
            "una modista que la firma, fotografiada para el lookbook y acompañada "
            "personalmente en la entrega. Cuarenta y cinco es el número máximo que nos "
            "permite hacerlo bien.",

        # Atelier cards — 3 cities
        "ateliers_label":   "Los tres ateliers",
        "ateliers_heading": "Milán, París, <em>Tokio.</em>",
        "ateliers_intro":
            "Tres casas, una sola maison. Milán dibuja y dirige. París cose y borda. Tokio "
            "recibe a la clienta asiática en un salón privado de Aoyama.",
        "ateliers": [
            {
                "city":   "Milán",
                "place":  "Via Senato 28 · Brera",
                "role":   "Atelier creativo · dirección · sastrería",
                "since":  "Abierto en 2014",
                "head":   "Giulia Maison · directora creativa",
                "team":   "Seis modistas · dos cortadoras · una dirección de clientes",
                "image":  "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=900&q=80&auto=format&fit=crop",
            },
            {
                "city":   "París",
                "place":  "9 rue du Mail · Sentier",
                "role":   "Atelier de marroquinería · costura sellier",
                "since":  "Abierto en 2017",
                "head":   "Jean-Luc Berthier · maître sellier",
                "team":   "Seis sellier · una cortadora · una pulidora",
                "image":  "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=900&q=80&auto=format&fit=crop",
            },
            {
                "city":   "Tokio",
                "place":  "1-1-7 Aoyama · Minato-ku",
                "role":   "Salón privado · recepción de clientas",
                "since":  "Abierto en 2021",
                "head":   "Yumi Tanaka · concierge",
                "team":   "Tres concierges · modista itinerante",
                "image":  "https://images.unsplash.com/photo-1559563458-527698bf5295?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Direction credit
        "direction_label":   "Dirección creativa",
        "direction_name":    "Giulia Maison",
        "direction_role":    "Directora creativa · fundadora",
        "direction_text":
            "Giulia Maison se formó en Central Saint Martins de Londres y trabajó ocho años "
            "entre Hermès y Bottega Veneta antes de fundar la maison en 2014. Su escritura "
            "es italiana, de Brera, pero su mano corta en francés. La maison es su estudio.",
        "direction_portrait":
            "https://images.unsplash.com/photo-1624206112918-f140f087f9b5?w=600&q=80&auto=format&fit=crop",
        "direction_quote":
            "«La cantidad es una decisión, no una consecuencia. Cuarenta y cinco prendas "
            "por temporada es el número que nos permite mirar a la cara a cada clienta.»",
        "direction_quote_attribution": "Giulia Maison · The Gentlewoman, 2025",

        # Press / editorial mentions
        "press_label":   "Editorial",
        "press_heading": "Apariciones en prensa <em>recientes.</em>",
        "press_items": [
            {
                "magazine": "Vogue Italia",
                "issue":    "Abril de 2026",
                "title":    "El nuevo silencio del lujo italiano",
                "byline":   "Reportaje · Sara Maino",
            },
            {
                "magazine": "The Gentlewoman",
                "issue":    "Spring 2025",
                "title":    "Forty-five pieces. Never one more.",
                "byline":   "Perfil · Penny Martin",
            },
            {
                "magazine": "AnOther Magazine",
                "issue":    "AW25",
                "title":    "L'atelier de Sentier",
                "byline":   "Foto · Mark Borthwick",
            },
            {
                "magazine": "Le Monde D'Hermès",
                "issue":    "Número 84",
                "title":    "Filiation italienne",
                "byline":   "Texto · Stefano Tonchi",
            },
            {
                "magazine": "Wallpaper*",
                "issue":    "Marzo de 2025",
                "title":    "Une maison bien cachée",
                "byline":   "Atelier visit · Tony Chambers",
            },
        ],

        # Numbers
        "numbers_label":   "Cifras de la maison",
        "numbers_items": [
            ("12",    "años desde la fundación"),
            ("3",     "ateliers en el mundo"),
            ("45",    "prendas por temporada"),
            ("9",     "siluetas por drop"),
        ],

        # Visit card — 3 cities
        "visit_label":   "Visite la maison",
        "visit_heading": "Tres casas, <em>tres salones privados.</em>",
        "visit_text":
            "Las maisons de Milán, París y Tokio abren sólo con cita previa. La dirección "
            "de clientes reserva una sala, prepara las prendas de Su perfil y organiza la "
            "prueba con la modista. Servicio gratuito, reservado.",
        "visit_primary":   "Solicitar una cita",
        "visit_primary_href": "contatti",
    },

    # ─── LOOKBOOK ─────────────────────────────────────────────
    "lookbook": {
        "issue":     "Primavera–Verano 2026",
        "issue_label":"Issue",
        "issue_n":   "Issue 12",
        "eyebrow":   "Lookbook · Issue 12",
        "headline":  "La luz de <em>Como, en marzo.</em>",
        "intro":
            "Dieciocho imágenes tomadas en tres jornadas de marzo en el Grand Hôtel Villa "
            "d'Este, sobre el lago de Como. Estilismo a cargo de Carla Sozzani, fotografía "
            "de Letizia Carrera, diseño de set de Sebastiano Pellion di Persano. La luz "
            "natural de la mañana fue el único instrumento de iluminación.",

        # Credits panel
        "credits_label":   "Créditos",
        "credits_rows": [
            ("Dirección creativa",  "Giulia Maison · Maison Luxe Milán"),
            ("Estilismo",           "Carla Sozzani"),
            ("Fotografía",          "Letizia Carrera"),
            ("Diseño de set",       "Sebastiano Pellion di Persano"),
            ("Peluquería y maquillaje", "Lina Hammar · Art + Commerce"),
            ("Modelo",              "Sara Grace Wallerstedt · IMG Models"),
            ("Localización",        "Grand Hôtel Villa d'Este · Cernobbio"),
            ("Impresión",           "Tirada analógica · Studio Riffraff Milán"),
        ],

        # Editorial grid — 6 looks
        "looks_label":   "Los dieciocho looks",
        "looks_intro":   "Seis seleccionados para prensa, doce en la biblioteca privada.",
        "looks": [
            {
                "n":       "Look 03",
                "title":   "Cady doble capa",
                "outfit":  "Robe-manteau cady doble · botas de piel Sentier",
                "credit":  "Estilismo · pañuelo de archivo 2018",
                "image":   "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 07",
                "title":   "Tailleur Cady Blanco",
                "outfit":  "Chaqueta + pantalón wide · zapatos Atelier Sentier · pochette Isola",
                "credit":  "Set · jardín de las camelias",
                "image":   "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 09",
                "title":   "Lana cardada de Biella",
                "outfit":  "Abrigo cardado · pantalón crepé · botín sellier",
                "credit":  "Abrigo Maglificio Lanifer",
                "image":   "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 11",
                "title":   "Rack Atelier Negro",
                "outfit":  "Jersey cachemira corto · pantalón crepé · bolso Atelier",
                "credit":  "Bolso Atelier Sentier · 21 horas de elaboración",
                "image":   "https://images.unsplash.com/photo-1551803091-e20673f15770?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 14",
                "title":   "Crepé de seda de Como",
                "outfit":  "Bomber Siena · pantalón wide crepé · sandalia atada",
                "credit":  "Tejido Setificio Tessitura Como",
                "image":   "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 18",
                "title":   "Borsa Isola · día",
                "outfit":  "Jersey cardado · vaqueros atelier · bolso Isola",
                "credit":  "Bolso Atelier Sentier · piel Madonna",
                "image":   "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1200&q=80&auto=format&fit=crop",
            },
        ],

        # Editorial pull-quote
        "pullquote":
            "«Como en marzo es una habitación cerrada. La maison ha salido de ella con "
            "dieciocho fotografías que la hacen legible.»",
        "pullquote_attribution": "Carla Sozzani · estilista del lookbook",

        # Notes from set
        "notes_label":   "Notas de rodaje",
        "notes_intro":
            "Tres jornadas de marzo, sol velado, viento de norte-noreste. La modelo posó "
            "sin interrupciones de siete a once, a la luz de entrada de la mañana. La "
            "chaqueta cady del Look 03 requirió dos horas de planchado cada mañana para "
            "recuperar los pliegues.",
        "notes_items": [
            {
                "label": "Día 01 · Salón de las camelias",
                "text":  "Siete looks en cinco horas de luz. Cambio de traje entre una "
                         "toma y otra en sala contigua. Almuerzo a las quince.",
            },
            {
                "label": "Día 02 · Mirador sobre el lago",
                "text":  "Seis looks con luz frontal de la mañana. Lluvia ligera entre las "
                         "once y el mediodía: toma aplazada a la tarde.",
            },
            {
                "label": "Día 03 · Salón privado",
                "text":  "Cinco looks con luz de vela y ventana. Las últimas tres "
                         "fotografías las pidió la directora creativa para el pullquote "
                         "de apertura.",
            },
        ],

        # Buy from lookbook CTA
        "shop_label":   "Reservar desde el lookbook",
        "shop_heading": "Cada look conduce <em>a la prenda de la colección.</em>",
        "shop_intro":
            "Los dieciocho looks son navegables desde la colección completa. Para "
            "solicitar una prenda, escriba a la dirección de clientes — la lista de "
            "espera abre el viernes 24 de abril.",
        "shop_primary":     "Ir a la colección",
        "shop_primary_href":"collezione",
        "shop_secondary":   "Inscribirse a la lista de espera",
        "shop_secondary_href":"contatti",
    },

    # ─── CONTATTI (private appointment form) ──────────────────
    "contatti": {
        "eyebrow":  "Dirección de clientes privada",
        "headline": "Solo con <em>cita previa.</em>",
        "intro":
            "La maison recibe exclusivamente con cita previa, en tres salones privados de "
            "Milán, París y Tokio. La dirección de clientes prepara las prendas de Su "
            "perfil antes de Su llegada y Le reserva a la modista para la prueba. "
            "Servicio reservado, gratuito, bajo solicitud directa.",

        # Form intro
        "form_section_label":  "Solicitud privada",
        "form_section_intro":
            "Le rogamos cumplimente la ficha con los datos de Su cita o de Su solicitud. "
            "La dirección de clientes responde al siguiente día hábil. Para la lista de "
            "espera del Drop 04 — apertura el 24 de abril — seleccione la opción dedicada.",

        "form_helper_required":  "Los campos señalados son obligatorios",
        "form_submit_button":    "Enviar solicitud privada",
        "form_submit_note":
            "Sus datos son tratados exclusivamente por la dirección de clientes. Ninguna "
            "newsletter, ninguna comunicación comercial.",

        "form_fields": [
            {"name":"titolo",    "label":"Tratamiento",    "type":"select", "required":True,
             "options":["Sra.","Sr.","Mx","Estudio·Atelier","Prensa·Press"]},
            {"name":"nome",      "label":"Nombre y apellidos", "type":"text", "placeholder":"P. ej. Sra. Eleonora Cattaneo", "required":True},
            {"name":"email",     "label":"Correo electrónico", "type":"email", "placeholder":"e.cattaneo@ejemplo.es",       "required":True},
            {"name":"telefono",  "label":"Teléfono",           "type":"tel",   "placeholder":"+34 …",                        "required":False},
            {"name":"city",      "label":"Maison de interés",  "type":"select", "required":True,
             "options":["Milán · Via Senato","París · Sentier","Tokio · Aoyama","Indistinto"]},
            {"name":"servizio",  "label":"Servicio solicitado", "type":"select", "required":True,
             "options":["Visita privada","Lista de espera Drop 04","Prenda a medida","Reedición de archivo","Prensa y press"]},
            {"name":"capo",      "label":"Look o prenda (opc.)", "type":"text", "placeholder":"P. ej. Look 11 · Rack Atelier Negro", "required":False},
            {"name":"messaggio", "label":"Notas a la dirección de clientes", "type":"textarea", "placeholder":"Indique fecha preferida, tallas, perfil personal.", "required":True, "rows":5},
        ],

        # Right-side card — three maison addresses
        "card_label":   "Las tres maisons",
        "maison_cards": [
            {
                "city":    "Milán",
                "address": "Via Senato 28 · 20121 Milán",
                "phone":   "+39 02 7600 1492",
                "email":   "milano@maisonluxe.com",
                "hours":   "Mar – Sáb · 11:00 – 19:00 · solo con cita previa",
            },
            {
                "city":    "París",
                "address": "9 rue du Mail · 75002 París",
                "phone":   "+33 1 4296 4720",
                "email":   "paris@maisonluxe.com",
                "hours":   "Mar – Vie · 11:00 – 19:00 · solo con cita previa",
            },
            {
                "city":    "Tokio",
                "address": "1-1-7 Aoyama · Minato-ku · Tokio 107-0062",
                "phone":   "+81 3 6450 5018",
                "email":   "tokyo@maisonluxe.com",
                "hours":   "Mié – Sáb · 12:00 – 20:00 · solo con cita previa",
            },
        ],

        # FAQ accordion (private viewing oriented)
        "faq_label":   "Preguntas frecuentes",
        "faq_items": [
            {
                "q": "¿Con cuánta antelación se reserva una visita privada?",
                "a": "Al menos una semana de antelación para Milán y París; dos semanas "
                     "para Tokio. Para solicitudes urgentes, escriba directamente a la "
                     "dirección de clientes.",
            },
            {
                "q": "¿Tiene coste el servicio de visita privada?",
                "a": "No, es gratuito y reservado. Incluye preparación de las prendas, "
                     "modista en sala, café y champán, y un mapa personalizado de la "
                     "colección.",
            },
            {
                "q": "¿Es posible encargar una prenda a medida?",
                "a": "Sí, sobre la base de las siluetas existentes. Plazos de entrega: de "
                     "ocho a doce semanas. Señal del cincuenta por ciento en la "
                     "confirmación del diseño.",
            },
            {
                "q": "¿Cómo funciona la lista de espera?",
                "a": "Las inscritas en la lista tienen prioridad absoluta en todos los "
                     "drops. La lista no supone obligación alguna de compra. Inscripción "
                     "gratuita, bajo solicitud directa.",
            },
        ],
    },
}
