"""Albergo Borgo — Hospitalidad de relais en una aldea toscana UNESCO (ES).

T57 · Wave 2 Pass-2 close-out (2026-05-12) · ES Peninsular translation
of ALBERGO_CONTENT_IT. Mirrors IT shape exactly: 225 leaf paths · zero
missing · zero extra.

Voice contract (ES Peninsular):
- Registro hospitalidad editorial: El País Viajero · Condé Nast
  Traveler España · National Geographic Traveler España · Conde Nast
  Brides España. Nunca travel-blog informal, nunca marketing de
  cadena hotelera. Tercera persona formal; tratamiento de usted al
  huésped (plural: ustedes peninsular en lugar del «voi» italiano).
- Detalle concreto: Val d'Orcia · Pienza · Siena · zona Patrimonio
  UNESCO · siglo XVII · restauración de 2009 firmada por el estudio
  Castellini-Mancini · 8 suites · brigada de 14 personas · spa Aqua
  subterránea · restaurante con estrella Michelin (chef Tommaso
  Brigliadori) · pérgola de glicinia · bodega del siglo XVIII.
- Anclaje de voz `hospitalidad de borgo` — registro que consagra la
  promesa de hospitalidad de aldea: un relais dentro de un borgo
  toscano todavía habitado (no un resort, no una cadena hotelera, no
  una villa de campo en venta). El término `borgo` se conserva como
  italianismo según uso consagrado de El País Viajero en su
  cobertura de las aldeas toscanas. Es portador de sentido en el
  titular y en cada banda primaria de hospitalidad.
- Vocabulario: hospitalidad · borgo · relais · brigada · maître ·
  concierge · noche · estancia · spa · cata · bodega · pérgola.
  Nunca: reserva online · check-in inmediato · early-bird · resort ·
  all-inclusive.
- Nombres propios italianos preservados verbatim: Borgo San Marco,
  Vittoria Sernigi, Federico Bonechi, Tommaso Brigliadori, Anna
  Ricci, Caterina Sandri, La Vigna, Il Frantoio, Il Pozzo, La
  Cisterna, La Torre, Il Cortile, La Loggia, La Cantina, Pienza,
  Val d'Orcia, Brunello, Vino Nobile, Sangiovese, Relais &
  Châteaux, Touring Club Italiano, Michelin, AIS, denominaciones
  DOCG/DOC, etc.
"""
from __future__ import annotations

from typing import Any


# Imagery — Unsplash CC0 travel-boutique-hotel pool (mirrored from IT).
_HERO_COURTYARD = "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=1600&q=80&auto=format&fit=crop"
_SUITE_VIGNA = "https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=1200&q=80&auto=format&fit=crop"
_SUITE_FRANTOIO = "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1200&q=80&auto=format&fit=crop"
_SUITE_POZZO = "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=1200&q=80&auto=format&fit=crop"
_SUITE_CISTERNA = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1200&q=80&auto=format&fit=crop"
_SUITE_TORRE = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200&q=80&auto=format&fit=crop"
_SUITE_CORTILE = "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=1200&q=80&auto=format&fit=crop"
_SUITE_LOGGIA = "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=1200&q=80&auto=format&fit=crop"
_SUITE_CANTINA = "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=1200&q=80&auto=format&fit=crop"
_BORGO_VALDORCIA = "https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?w=1200&q=80&auto=format&fit=crop"
_BORGO_PIENZA = "https://images.unsplash.com/photo-1568822617270-2c1579f8dfe2?w=1200&q=80&auto=format&fit=crop"
_BORGO_MONTALCINO = "https://images.unsplash.com/photo-1517760444937-f6397edcbbcd?w=1200&q=80&auto=format&fit=crop"
_BORGO_CIPRESSI = "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=1200&q=80&auto=format&fit=crop"
_BORGO_CHIANTI = "https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=1200&q=80&auto=format&fit=crop"
_BORGO_PIENZA_PIAZZA = "https://images.unsplash.com/photo-1543429776-2782fc8e1acd?w=1200&q=80&auto=format&fit=crop"
_PORTRAIT_DIRECTOR = "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_MAITRE = "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_CHEF = "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_SOMMELIER = "https://images.unsplash.com/photo-1566753323558-f4e0952af115?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_SPA = "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=900&q=80&auto=format&fit=crop"


ALBERGO_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "El borgo",     "kind": "home"},
        {"slug": "camere",     "label": "Las suites",   "kind": "blog_list"},
        {"slug": "borgo",      "label": "El territorio", "kind": "about"},
        {"slug": "brigata",    "label": "La brigada",   "kind": "team"},
        {"slug": "soggiorno",  "label": "La estancia",  "kind": "services"},
        {"slug": "concierge",  "label": "Concierge",    "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":   "B",
        "logo_word":      "Borgo San Marco",
        "logo_subline":   "Relais & Spa · Pienza desde 1612",
        "tag":            "Temporada 2026 · reservas abiertas de mayo a octubre",
        "phone":          "+39 0578 748 124",
        "phone_label":    "Línea directa de concierge",
        "email":          "concierge@borgosanmarco.it",
        "email_label":    "Escriban a la dirección",
        "address":        "Borgo San Marco di Sopra · 53026 Pienza · Siena",
        "hours_compact":  "Recepción 24 horas · check-in desde las 14 · check-out hasta las 11",
        "hours_footer_rows": [
            "Recepción abierta 24 horas con concierge en sala",
            "Idiomas de sala: italiano · english · français · deutsch",
        ],
        "license":        "Código CITRA 0521-053026-100201 · Cat. Cinco Estrellas Gran Lujo · Insc. Confindustria Alberghi 0428",
        "footer_intro":
            "Borgo San Marco es un relais de ocho suites alojado en la casa parroquial "
            "del siglo XVII del borgo homónimo, aldea colinar de Pienza asomada a la "
            "Val d'Orcia UNESCO. Restauración del estudio Castellini-Mancini en 2009, "
            "afiliación a Relais & Châteaux desde 2014, una estrella Michelin para el "
            "restaurante Trebbio desde 2019. La hospitalidad de borgo es nuestra "
            "promesa: una sola recepción para ocho habitaciones, una brigada de sala "
            "de catorce personas y la quietud de un borgo todavía habitado.",

        # Nav reservation CTA (hospitality)
        "nav_cta":         "Reserve su estancia",
        "nav_cta_kind":    "appointment",
        "nav_cta_short":   "Reservar",

        # Footer labels
        "foot_studio":   "El relais",
        "foot_pages":    "Mapa",
        "foot_contact":  "Concierge",
        "foot_offices":  "Sedes",
        "offices_footer_rows": [
            "Borgo San Marco di Sopra · 53026 Pienza · Siena",
            "Tenuta Trebbio · bodega y olivar · 1,2 km al sur",
        ],
        "office_rows": [
            "Borgo San Marco di Sopra 17 · 53026 Pienza · Siena",
            "Tel +39 0578 748 124 · concierge@borgosanmarco.it",
        ],
        "dossier_label":     "Suites",
        "portfolio_label":   "Noches / año",
        "territorio_label":  "Borgo",
        "superficie_label":  "Superficie",
        "provenance_label":  "Vistas",
        "access_label":      "Idiomas de sala",
        "availability_label": "Temporada",
        "price_note":        "Tarifa bajo petición · paquetes de temporada",
        "nda_required_label": "Reservado",
        "viewing_on_request": "Solo bajo reserva",
        "referent_label":    "Referente en sala",
        "concierge_line_label": "Concierge dedicado",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "cover_location":    "Borgo San Marco di Sopra · Val d'Orcia · UNESCO",
        "cover_image_credit": "Fotografía · Massimo Listri",
        "cover_image":       _HERO_COURTYARD,

        "eyebrow":           "Relais & Spa · Val d'Orcia · Pienza desde 1612",
        "headline":          'Ocho suites en un borgo toscano del siglo XVII. <em>Hospitalidad de borgo</em>, una sola temporada al año.',
        "sub":
            "Un relais de ocho suites instalado en la casa parroquial del siglo XVII "
            "de Borgo San Marco di Sopra, aldea colinar de Pienza asomada a la "
            "Val d'Orcia. Hospitalidad de borgo en formato editorial: apertura "
            "estacional de mayo a finales de octubre · una sola recepción · cocina "
            "con estrella Michelin · spa Aqua di Borgo en la cisterna del siglo "
            "XVIII · bodega propia.",
        "hero_wordmark":     "Borgo San Marco",
        "hero_location":     "Pienza · Siena · Toscana",
        "hero_counter_label": "Suites",
        "hero_counter_value": "8",
        "hero_series_label": "Temporada",
        "hero_series_title": "2026 · Abril – Octubre",
        "hero_series_note":  "Apertura el 18 de abril · cierre el 27 de octubre · brigada de 14 personas en sala",

        "primary_cta":         "Reserve su estancia",
        "primary_cta_href":    "concierge",
        "secondary_cta":       "Descubran las suites",
        "secondary_cta_href":  "camere",

        # Hero credit cells — list[4] of tuple[2] (label, value)
        "hero_credit_cells": [
            ("Afiliación",    "Relais & Châteaux"),
            ("Cocina",        "Una estrella Michelin"),
            ("Restauración",  "Castellini-Mancini · 2009"),
            ("Apertura",      "Estacional · 24 semanas"),
        ],

        # Signature suite section — list[6] of dict
        "signature_label":    "Las suites",
        "signature_heading":  "Las suites de la casa, una por cada estancia del borgo.",
        "signature_intro":
            "Ocho suites, cada una alojada en un ambiente histórico de la casa "
            "parroquial y de la bodega del siglo XVIII contigua. Ninguna habitación "
            "es igual a la otra; todas asomadas a la Val d'Orcia.",
        "signature": [
            {
                "slug":         "suite-la-vigna",
                "image":        _SUITE_VIGNA,
                "index":        "Suite 01",
                "title":        "La Vigna",
                "territorio":   "Lado oeste · primera planta",
                "superficie":   "62 m² · matrimonial king",
                "provenance":   "Vistas al viñedo histórico de Sangiovese",
                "availability": "Disponible de mayo a septiembre",
            },
            {
                "slug":         "suite-il-frantoio",
                "image":        _SUITE_FRANTOIO,
                "index":        "Suite 02",
                "title":        "Il Frantoio",
                "territorio":   "Planta baja · ala sur",
                "superficie":   "78 m² · matrimonial + saloncito",
                "provenance":   "Antigua muela del molino de aceite de 1620 en el centro de la habitación",
                "availability": "Disponible toda la temporada",
            },
            {
                "slug":         "suite-il-pozzo",
                "image":        _SUITE_POZZO,
                "index":        "Suite 03",
                "title":        "Il Pozzo",
                "territorio":   "Patio interior · planta baja",
                "superficie":   "54 m² · matrimonial estándar",
                "provenance":   "Pozo octogonal del siglo XVII en el patio privado",
                "availability": "Bajo petición · solo parejas",
            },
            {
                "slug":         "suite-la-cisterna",
                "image":        _SUITE_CISTERNA,
                "index":        "Suite 04",
                "title":        "La Cisterna",
                "territorio":   "Ala este · planta sótano",
                "superficie":   "88 m² · cama con dosel",
                "provenance":   "Bóveda de la cisterna del siglo XVIII · luz natural cenital",
                "availability": "Bajo petición · luna de miel recomendada",
            },
            {
                "slug":         "suite-la-torre",
                "image":        _SUITE_TORRE,
                "index":        "Suite 05",
                "title":        "La Torre",
                "territorio":   "Torre angular · segunda planta",
                "superficie":   "70 m² · cama matrimonial + estudio",
                "provenance":   "Vistas de 270° sobre la Val d'Orcia hasta el Monte Amiata",
                "availability": "Disponible de abril a octubre",
            },
            {
                "slug":         "suite-il-cortile",
                "image":        _SUITE_CORTILE,
                "index":        "Suite 06",
                "title":        "Il Cortile",
                "territorio":   "Planta baja · ala norte",
                "superficie":   "65 m² · matrimonial + jardín privado",
                "provenance":   "Pequeña logia privada sobre la pérgola de glicinia",
                "availability": "Disponible de mayo a octubre",
            },
        ],
        "signature_link_all":  "Vean las ocho suites",
        "signature_link_href": "camere",

        # Territory chip-row — list of scalar strings
        "territory_label": "Territorio",
        "territory": [
            "Pienza · Val d'Orcia",
            "Montalcino · bodegas del Brunello",
            "Montepulciano · Vino Nobile",
            "San Quirico d'Orcia · vías históricas",
            "Bagno Vignoni · termas medievales",
            "Monte Amiata · excursiones",
            "Siena · Palio en julio y agosto",
            "Cortona · vías etruscas",
        ],

        # Director / advisor band
        "advisor_label":     "La dirección",
        "advisor_heading":   "Una directora que trabaja en sala. <em>Treinta y dos temporadas de hostelería</em>.",
        "advisor_intro":
            "Borgo San Marco está dirigido en primera persona por Vittoria Sernigi, "
            "hotelera toscana nacida en 1964, discípula del Maestro Casiraghi en el "
            "Plaza Athénée de París y del Maestro Cipriani en el Cipriani de Venecia. "
            "Treinta y dos temporadas de hostelería de lujo antes de hacerse cargo "
            "del borgo en 2008, donde firmó la promesa de hospitalidad de borgo "
            "que hoy define a la casa.",
        "advisor_name":      "Vittoria Sernigi",
        "advisor_role":      "Directora · miembro del Touring Club Italiano · sumiller AIS",
        "advisor_bio":
            "Treinta y dos años de hostelería internacional antes de Pienza: Plaza "
            "Athénée París · Cipriani Venecia · Villa San Michele Fiesole. Miembro "
            "del Touring Club Italiano desde 1995, sumiller AIS desde 2002, "
            "formadora en la Scuola Alberghiera de Siena. En sala cada mañana al "
            "desayuno, cada tarde en la entrega de llaves.",
        "advisor_portrait":  _PORTRAIT_DIRECTOR,
        "advisor_cta":       "Escriban a Vittoria",
        "advisor_cta_href":  "concierge",

        # Numbers band — list[4] of tuple[2] (counter, label)
        "numbers_label":    "Borgo San Marco en cifras",
        "numbers_heading":  "Una temporada, una sola recepción, una brigada.",
        "numbers": [
            ("8",   "Suites · ninguna igual a otra"),
            ("14",  "Personas en la brigada de sala"),
            ("1",   "Estrella Michelin · restaurante Trebbio"),
            ("12",  "Años de afiliación a Relais & Châteaux"),
        ],
        "numbers_note":
            "Apertura estacional del 18 de abril al 27 de octubre · brigada de sala "
            "completa en los 12 turnos de servicio · recepción 24 horas · "
            "hospitalidad de borgo en cada turno.",

        # Press band — list of scalar strings (home version)
        "press_label":   "Prensa",
        "press_intro":   "Borgo San Marco en los reportajes editoriales de 2023-2025",
        "press_items": [
            "Condé Nast Traveler España",
            "El País Viajero",
            "National Geographic Traveler España",
            "Monocle Travel",
            "Conde Nast Brides España",
        ],

        # Private band — closing CTA
        "private_label":     "Para sus invitados más queridos",
        "private_heading":   "El borgo entero, una sola familia. <em>Exclusiva de ocho días</em>.",
        "private_intro":
            "El borgo puede reservarse en exclusiva para una sola familia o para un "
            "grupo restringido · ocho suites reservadas, brigada dedicada, "
            "restaurante cerrado al público, bodega abierta a los huéspedes. "
            "Disponibilidad únicamente en tres ventanas al año · escriban a la "
            "dirección con al menos seis meses de antelación. Hospitalidad de "
            "borgo elevada a la dimensión privada.",
        "private_primary":      "Escriban a la dirección",
        "private_primary_href": "concierge",
        "private_secondary":    "Descubran el borgo",
        "private_secondary_href": "borgo",
    },

    # ─── CAMERE (blog_list of suites) ─────────────────────────
    "camere": {
        "eyebrow":          "Ocho suites · Borgo San Marco",
        "headline":         "Las suites de la casa.",
        "intro":
            "Cada suite lleva el nombre de un ambiente histórico del borgo · cada "
            "una fue rediseñada por el estudio Castellini-Mancini en 2009 "
            "conservando la planta original del siglo XVII.",
        "lead_image":       _HERO_COURTYARD,
        "filter_label":     "Afinen la búsqueda",
        "filter_groups": [
            {"label": "Vistas", "options": ["Viñedo", "Patio", "Borgo", "Val d'Orcia", "Pérgola"]},
            {"label": "Camas", "options": ["Matrimonial king", "Matrimonial + saloncito", "Cama con dosel", "Suite con estudio"]},
            {"label": "Temporada", "options": ["Apertura en abril", "Disponible mayo – septiembre", "Solo temporada alta"]},
        ],
        "sort_label":       "Ordenar",
        "sort_options": [
            "Por superficie · de la más amplia",
            "Por temporada",
            "Por número de huéspedes",
            "Por quietud",
        ],
        "result_count":     "8 suites disponibles en la temporada 2026",
        "result_subtitle":  "Una sola recepción para las ocho habitaciones · brigada de sala dedicada.",
        "footer_note_label": "Tarifas",
        "footer_note":
            "Todas las suites incluyen desayuno en sala, acceso ilimitado al spa "
            "Aqua di Borgo y una cata de tres vinos en la bodega bajo reserva. "
            "Tarifa estacional comunicada al solicitar la información. "
            "Hospitalidad de borgo en todas las tarifas, sin distinción de "
            "suite.",
    },

    # ─── BORGO (about · territorio del relais) ────────────────
    "borgo": {
        "eyebrow":          "Val d'Orcia · UNESCO",
        "headline":         "Un borgo del siglo XVII todavía habitado.",
        "intro":
            "Borgo San Marco di Sopra es una aldea colinar de Pienza · 41 "
            "habitantes residentes · plaza central de 1571 · casa parroquial de "
            "1612 (hoy relais) · bodega del siglo XVIII (hoy spa). El borgo sigue "
            "habitado por las mismas seis familias desde hace cuatro generaciones; "
            "el relais es su huésped más reciente, desde 2009.",

        "statement_label":   "Nuestra hospitalidad",
        "statement_heading": "Ocho suites, una sola brigada, un borgo entero.",
        "statement_text":
            "Hospitalidad de borgo significa que la recepción es una sola para las "
            "ocho suites, que la brigada de sala conoce a cada huésped por su "
            "nombre desde el segundo día y que el borgo sigue siendo un borgo (con "
            "sus 41 habitantes) también mientras ustedes están alojados. No somos "
            "un resort. No somos una cadena. No somos un hotel de ciudad.",

        "territories_label":   "Los alrededores",
        "territories_heading": "Seis territorios a menos de una hora del borgo.",
        "territories_intro":
            "Los alrededores de la Val d'Orcia forman parte de la hospitalidad de "
            "borgo del relais: cada territorio cuenta con un referente en sala "
            "dedicado al descubrimiento · vino, termas, recorridos etruscos, "
            "excursiones al Amiata, ópera en el Palio de Siena.",
        "territories": [
            {
                "image":      _BORGO_VALDORCIA,
                "name":       "Val d'Orcia",
                "region":     "Pienza · San Quirico · Bagno Vignoni",
                "history":    "Patrimonio UNESCO desde 2004 · paisaje renacentista codificado por Lorenzetti. Cipreses, cretas y caseríos.",
                "architects": "Cipreses lineales · vías cavas etruscas",
                "count":      "12 km",
                "since":      "Visita: 1 hora · referente Federico en sala",
            },
            {
                "image":      _BORGO_MONTALCINO,
                "name":       "Montalcino",
                "region":     "Bodegas históricas del Brunello",
                "history":    "Bodegas históricas del Brunello di Montalcino DOCG · Biondi-Santi, Casanova di Neri, Il Poggione. Catas privadas con cita previa.",
                "architects": "Pievi medievales · castillos sieneses",
                "count":      "28 km",
                "since":      "Visita: 1 jornada · referente sumiller AIS",
            },
            {
                "image":      _BORGO_PIENZA,
                "name":       "Pienza · la ciudad ideal",
                "region":     "Plaza Pío II · catedral · Palazzo Piccolomini",
                "history":    "La ciudad ideal del Renacimiento proyectada por Bernardo Rossellino para Pío II en 1462. Plaza, catedral, Palazzo Piccolomini, vistas al Amiata.",
                "architects": "Bernardo Rossellino · 1459-1462",
                "count":      "1,8 km",
                "since":      "Visita: 2 horas a pie · concierge acompaña bajo petición",
            },
            {
                "image":      _BORGO_CHIANTI,
                "name":       "Montepulciano",
                "region":     "Vino Nobile · bodegas subterráneas",
                "history":    "Bodegas subterráneas excavadas en la toba, algunas del siglo XIV. Cata del Vino Nobile di Montepulciano DOCG · bodegas Avignonesi, Salcheto, Boscarelli.",
                "architects": "Antonio da Sangallo il Vecchio · Vignola",
                "count":      "32 km",
                "since":      "Visita: 1 jornada · referente sumiller AIS",
            },
            {
                "image":      _BORGO_CIPRESSI,
                "name":       "Bagno Vignoni",
                "region":     "Termas libres del siglo XV",
                "history":    "Plaza-balsa termal del siglo XV, única en el mundo. Agua sulfurosa a 49°C que aflora de la roca, de acceso libre. Cena en una trattoria de la plaza con Caterina, la cocinera.",
                "architects": "Balsa natural · siglo XV",
                "count":      "8 km",
                "since":      "Visita: media jornada · referente de sala Federico",
            },
            {
                "image":      _BORGO_PIENZA_PIAZZA,
                "name":       "Monte Amiata",
                "region":     "Volcán extinto · hayedos · estación de esquí",
                "history":    "Volcán extinto (1.738 m). Hayedos centenarios, senderos CAI, estación de esquí en invierno. Castañada de noviembre en la aldea de Castiglione d'Orcia.",
                "architects": "Senderos CAI · 4 cumbres señalizadas",
                "count":      "38 km",
                "since":      "Visita: 1 jornada · guía alpino bajo reserva",
            },
        ],
        "territory_card_cta":      "Planifiquemos juntos · escriban a la dirección",
        "territory_card_cta_href": "concierge",

        "referent_label":   "El referente en sala",
        "referent_heading": "Un solo referente para toda la estancia.",
        "referent_text":
            "Desde el instante de la llegada, cada huésped cuenta con un referente "
            "único en sala — el maître Federico Bonechi o la sumiller Anna Ricci, "
            "según la temporada. El referente acompaña toda la reserva: mesa en el "
            "restaurante, masajes en el spa, catas en la bodega, excursiones por "
            "los alrededores. La hospitalidad de borgo se sostiene en este "
            "vínculo de un solo nombre.",

        "stats_label":  "Borgo San Marco · cifras de 2025",
        # list[4] of tuple[2]
        "stats": [
            ("12",  "Años de afiliación a Relais & Châteaux"),
            ("162", "Noches abiertas al año"),
            ("8",   "Suites · temporada 2026"),
            ("41",  "Habitantes residentes del borgo"),
        ],
    },

    # ─── BRIGATA (team · staff en sala) ───────────────────────
    "brigata": {
        "eyebrow":       "La brigada · 14 personas en sala",
        "headline":      "Una misma brigada desde hace doce temporadas.",
        "intro":
            "La brigada de Borgo San Marco se compone de catorce personas, diez de "
            "las cuales regresan cada temporada desde 2014. Recepción, sala, "
            "restaurante, spa, bodega · una sola brigada para ocho suites. La "
            "hospitalidad de borgo nace de esta continuidad.",

        "director_label":       "Dirección",
        "director_name":        "Vittoria Sernigi",
        "director_role":        "Directora · propietaria desde 2008 · sumiller AIS · TCI",
        "director_text":
            "Vittoria Sernigi se hizo cargo de Borgo San Marco en 2008 tras treinta "
            "y dos temporadas de hostelería internacional entre París, Venecia y "
            "Fiesole. Diploma en la Escuela Hotelera Internacional de Lausana "
            "(1985), especialización en gestión hotelera en Cornell. Miembro del "
            "Touring Club Italiano desde 1995, sumiller AIS desde 2002.",
        "director_portrait":    _PORTRAIT_DIRECTOR,
        "director_quote":
            "La hospitalidad de borgo es la única hospitalidad que conozco. Es la "
            "más lenta, es la más exigente, es la más gratificante.",
        "director_quote_attribution": "Vittoria Sernigi · entrevista para Touring · 2024",

        "advisors_label":   "La brigada de sala",
        "advisors_heading": "Cuatro referentes, diez de temporada · una sola sala.",
        "advisors_intro":
            "Cuatro referentes sénior dirigen la sala. Las decisiones de servicio "
            "pasan por ellos, jamás por el algoritmo de una cadena. Es así como "
            "se preserva la hospitalidad de borgo.",
        # list[4] of dict (portrait, name, role, bio, territories, since, langs)
        "advisors": [
            {
                "portrait":    _PORTRAIT_MAITRE,
                "name":        "Federico Bonechi",
                "role":        "Maître de sala · referente único de los huéspedes",
                "bio":
                    "Maître de sala desde 2009 · diez temporadas en Borgo San Marco. "
                    "Diplomado por el Alberghiero di Chianciano · experiencia en el "
                    "Castello Banfi y en el Plaza Athénée. Conoce el nombre de cada "
                    "huésped desde el segundo día.",
                "territories": "Sala · recepción · concierge",
                "since":       "En la brigada desde 2014",
                "langs":       "Italiano · English · Français",
            },
            {
                "portrait":    _PORTRAIT_CHEF,
                "name":        "Tommaso Brigliadori",
                "role":        "Chef · restaurante Trebbio · una estrella Michelin",
                "bio":
                    "Chef del restaurante Trebbio desde 2017 · estrella Michelin desde "
                    "2019. Formado en l'Albereta a las órdenes de Gualtiero Marchesi, "
                    "perfeccionado con Bottura en Módena. Cocina de territorio: pici, "
                    "picci e pinoli, cordero de Zeri, alubias zolfini, queso caciotta "
                    "de Pienza.",
                "territories": "Cocina · bodega · huerto",
                "since":       "En la brigada desde 2017",
                "langs":       "Italiano · English",
            },
            {
                "portrait":    _PORTRAIT_SOMMELIER,
                "name":        "Anna Ricci",
                "role":        "Sumiller AIS · responsable de bodega",
                "bio":
                    "Sumiller AIS desde 2008 · responsable de bodega desde 2015. La "
                    "bodega alberga 4.200 referencias entre Brunello, Vino Nobile, "
                    "Chianti Classico y una pequeña colección de Champagne. Catas "
                    "privadas en bodega para los huéspedes, dos veces por semana.",
                "territories": "Bodega · catas · maridaje en el restaurante",
                "since":       "En la brigada desde 2015",
                "langs":       "Italiano · English · Deutsch",
            },
            {
                "portrait":    _PORTRAIT_SPA,
                "name":        "Caterina Sandri",
                "role":        "Responsable de Aqua di Borgo Spa",
                "bio":
                    "Responsable del spa desde 2018 · diploma en hidroterapia por la "
                    "Universidad de Siena, formación en gestión de spa en Six Senses "
                    "Toscana. El spa Aqua di Borgo está alojado en la cisterna del "
                    "siglo XVIII · solo tratamientos con cita previa.",
                "territories": "Spa Aqua di Borgo · tratamientos · piscina subterránea",
                "since":       "En la brigada desde 2018",
                "langs":       "Italiano · English",
            },
        ],

        "partners_label":   "Los productores del borgo",
        "partners_heading": "Los proveedores históricos de la mesa.",
        "partners_intro":
            "Las materias primas del restaurante Trebbio llegan de proveedores en "
            "un radio de treinta kilómetros alrededor del borgo, salvo el aceite "
            "(de producción propia) y el pan (panadería del borgo a 200 metros). "
            "Hospitalidad de borgo también en el plato.",
        # list[5] of tuple[2] (name, role)
        "partners": [
            ("Fattoria Trebbio",         "Aceite de oliva virgen extra propio · olivar histórico a 1,2 km del borgo"),
            ("Caseificio Castelmuzio",   "Pecorino de Pienza · caciotta · ricotta · 8 km de Pienza"),
            ("Azienda agricola Falcorosso", "Vacuno de Chianina · cordero de Zeri · aves · 12 km"),
            ("Forno di Pienza · Lorenzini", "Pan toscano · schiacciate · grissini · 1,8 km del borgo"),
            ("Erbario di Sant'Anna",     "Hierbas medicinales · tisanería del spa Aqua · monasterio a 18 km"),
        ],

        "press_label":   "Prensa · brigada y cocina",
        "press_heading": "Premios y menciones de la brigada.",
        # list[5] of dict (magazine, issue, title, byline)
        "press_items": [
            {
                "magazine": "Guía Michelin Italia",
                "issue":    "Ed. 2019 – confirmación 2025",
                "title":    "Una estrella · restaurante Trebbio · cocina toscana de territorio",
                "byline":   "Redacción Michelin",
            },
            {
                "magazine": "El País Viajero",
                "issue":    "Abril 2024",
                "title":    "Vittoria Sernigi · retrato de la directora de borgo",
                "byline":   "Maria Sirotti",
            },
            {
                "magazine": "Gambero Rosso",
                "issue":    "Enero 2025 · Tres tenedores",
                "title":    "Trebbio de Borgo San Marco · tres tenedores confirmados",
                "byline":   "Eleonora Cozzella",
            },
            {
                "magazine": "Condé Nast Traveler España",
                "issue":    "Mayo 2023 · Gold List",
                "title":    "Borgo San Marco · Top 50 Italia",
                "byline":   "Caterina Cesari",
            },
            {
                "magazine": "National Geographic Traveler España",
                "issue":    "Septiembre 2024",
                "title":    "Las 12 grandes casas de hospitalidad de la Val d'Orcia",
                "byline":   "Giovanni Rajberti",
            },
        ],

        "numbers_label": "La brigada en cifras",
        # list[6] of tuple[2]
        "numbers": [
            ("14", "Personas en la brigada de sala"),
            ("10", "De temporada recurrentes desde 2014"),
            ("32", "Años de experiencia de la directora"),
            ("4",  "Idiomas de sala (IT · EN · FR · DE)"),
            ("12", "Años de afiliación a Relais & Châteaux"),
            ("4200", "Referencias en bodega · responsable Anna Ricci AIS"),
        ],

        "visit_label":         "Para escribir a la brigada",
        "visit_heading":       "Una sola brigada, una sola sala.",
        "visit_text":
            "Para consultas sobre menús, alergias, vino, excursiones o tratamientos "
            "de spa escriban directamente a la brigada: respondemos antes de la "
            "siguiente jornada laboral. Vittoria firma personalmente la "
            "confirmación de la reserva.",
        "visit_primary":       "Escriban a la dirección",
        "visit_primary_href":  "concierge",
    },

    # ─── SOGGIORNO (services · la experiencia de la estancia) ─
    "soggiorno": {
        "eyebrow":      "La experiencia · cinco tiempos de la estancia",
        "headline":     "Cinco tiempos · de Pienza al regreso.",
        "intro":
            "La estancia en Borgo San Marco se articula en cinco tiempos · la "
            "llegada, la sala, el spa, la bodega y la salida hacia el territorio. "
            "Cada tiempo está cuidado por el referente de sala, según la práctica "
            "de la hospitalidad de borgo.",

        "process_label":   "Cinco tiempos",
        "process_heading": "Cómo transcurre una estancia.",
        "process_intro":
            "La narración de la estancia es una sola, desde el momento en que "
            "ustedes escriben a la dirección hasta el regreso a casa.",
        # list[5] of dict (n, title, text, duration)
        "process": [
            {
                "n":        "01",
                "title":    "La confirmación",
                "text":
                    "Respuesta personal de Vittoria en 24 horas tras la solicitud · "
                    "elección de la suite, de la ventana estacional y eventuales "
                    "peticiones especiales (menús, alergias, excursiones).",
                "duration": "1 jornada",
            },
            {
                "n":        "02",
                "title":    "La llegada",
                "text":
                    "Recepción desde las 14 · traslado desde el aeropuerto de "
                    "Florencia bajo petición · bienvenida en la plaza del borgo "
                    "con vino del territorio · presentación del referente de sala.",
                "duration": "2 horas",
            },
            {
                "n":        "03",
                "title":    "La sala y la bodega",
                "text":
                    "Cena en el restaurante Trebbio · menú del territorio en cinco "
                    "tiempos · maridaje comentado por la sumiller · bodega abierta "
                    "tras la cena para quienes deseen prolongar la velada.",
                "duration": "Una velada por estancia",
            },
            {
                "n":        "04",
                "title":    "El spa y el territorio",
                "text":
                    "Media jornada en el spa Aqua di Borgo (cisterna del siglo "
                    "XVIII) · natación, baño turco, sauna, hidromasaje en la balsa "
                    "natural · tratamientos con cita previa · excursión de media "
                    "jornada por la Val d'Orcia con el referente.",
                "duration": "Media jornada",
            },
            {
                "n":        "05",
                "title":    "La salida",
                "text":
                    "Check-out hasta las 11 · desayuno tardío hasta las 10:30 en "
                    "la pérgola de glicinia · regalo de despedida (aceite de la "
                    "Fattoria Trebbio · pequeño libro del borgo) · acompañamiento "
                    "al regreso.",
                "duration": "Media jornada",
            },
        ],

        "testimonial_label":  "La voz del huésped",
        "testimonial_text":
            "«Tres estancias en tres temporadas distintas, siempre la misma "
            "brigada, siempre Federico en la recepción. Es raro, en Italia, "
            "encontrar un hotel donde la promesa hecha la primera vez sigue "
            "siendo cierta también en la tercera visita.»",
        "testimonial_author": "Giorgio Borghi · Milán · huésped desde 2018",

        "faq_label":    "Preguntas recurrentes a la dirección",
        # list[6] of dict (q, a)
        "faq_items": [
            {
                "q": "¿El hotel está abierto todo el año?",
                "a":
                    "No. Borgo San Marco abre del 18 de abril al 27 de octubre de "
                    "2026 — veinticuatro semanas de temporada. El cierre invernal "
                    "permite el mantenimiento de las suites y el descanso de la "
                    "brigada de sala. Ninguna excepción, ni siquiera en Nochevieja.",
            },
            {
                "q": "¿Se puede reservar el borgo entero para una familia?",
                "a":
                    "Sí · en tres ventanas al año (junio, septiembre, final de "
                    "octubre). Ocho suites reservadas · restaurante cerrado al "
                    "público externo · brigada dedicada. Escriban a la dirección "
                    "con al menos seis meses de antelación respecto de la fecha "
                    "deseada.",
            },
            {
                "q": "¿Se pueden organizar bodas en el borgo?",
                "a":
                    "Solo bodas íntimas · máximo 36 invitados · ceremonia civil "
                    "en la logia de la planta noble · cena en la pérgola de "
                    "glicinia. No organizamos bodas con más de 36 invitados para "
                    "preservar la dimensión del borgo. Escriban a Vittoria con "
                    "al menos un año de antelación.",
            },
            {
                "q": "¿Se admiten perros de tamaño pequeño?",
                "a":
                    "Sí · bajo petición · en dos suites de la planta baja (Il "
                    "Frantoio y Il Pozzo). Suplemento de 30 € por noche · "
                    "comedero, cama y galletas incluidos. Pet sitter del borgo "
                    "disponible con cita previa para las horas de la cena en el "
                    "restaurante.",
            },
            {
                "q": "¿Puedo visitar la bodega aunque no sea huésped del restaurante?",
                "a":
                    "Sí · la bodega está abierta a los huéspedes del borgo dos "
                    "veces por semana (martes y jueves por la tarde, de 17 a 19) "
                    "para una cata de tres vinos con Anna · reserva obligatoria "
                    "en la recepción.",
            },
            {
                "q": "¿Hay wifi en las suites?",
                "a":
                    "Sí · línea de fibra a 1 Gbit/s · disponible en las ocho "
                    "suites, en sala y en el spa. Bajo petición es posible "
                    "activar la modalidad digital detox: la suite permanece sin "
                    "conexión durante toda la estancia · cajón para los "
                    "dispositivos a la llegada.",
            },
        ],

        "cta_label":         "Para empezar",
        "cta_heading":       "<em>Una temporada corta</em>, una sola brigada.",
        "cta_text":
            "Las ventanas estacionales de 2026 se abren el 18 de abril · las "
            "suites más solicitadas (La Vigna, Il Cortile, La Torre) se agotan "
            "antes de mayo. Escriban a la dirección para la reserva. La "
            "hospitalidad de borgo se reserva con tiempo.",
        "cta_primary":       "Reserve su estancia",
        "cta_primary_href":  "concierge",
    },

    # ─── CONCIERGE (contact · concierge dedicado) ─────────────
    "concierge": {
        "eyebrow":      "Concierge dedicado · Vittoria Sernigi",
        "headline":     "Escriban a la dirección.",
        "intro":
            "Para la solicitud de reserva, las fechas de exclusiva del borgo, los "
            "paquetes estacionales y cualquier consulta sobre la estancia escriban "
            "directamente a la dirección. Vittoria responde personalmente antes "
            "de la siguiente jornada laboral.",

        "phone_label":   "Líneas directas",
        "phone_intro":
            "Recepción abierta 24 horas · concierge dedicado en sala en turno "
            "continuo · número directo para emergencias.",
        # list[4] of tuple[2]
        "phone_rows": [
            ("Concierge",    "+39 0578 748 124"),
            ("Dirección",    "+39 0578 748 100 · solo Vittoria"),
            ("Restaurante",  "+39 0578 748 130 · reservas Trebbio"),
            ("Spa",          "+39 0578 748 145 · reservas Aqua"),
        ],

        "form_section_label": "Solicitud de reserva",
        "form_section_intro":
            "Indiquen las fechas deseadas, la suite preferida (o la exclusiva del "
            "borgo) y eventuales peticiones especiales. Vittoria responde "
            "personalmente al correo con la confirmación o con una propuesta "
            "alternativa en 24 horas.",
        "form_helper_required":  "Los campos marcados con · son obligatorios",
        "form_submit_button":    "Enviar solicitud a la dirección",
        "form_submit_note":
            "La confirmación definitiva se formaliza mediante una señal del 30 % "
            "por transferencia bancaria · saldo a la llegada en la recepción.",
        # list[10] of dict (label, name, type, required, options)
        "form_fields": [
            {"label": "Nombre y apellidos",         "name": "name",       "type": "text",     "required": True,  "options": []},
            {"label": "Email · respuesta directa", "name": "email",       "type": "email",    "required": True,  "options": []},
            {"label": "Teléfono",                   "name": "phone",      "type": "tel",      "required": False, "options": []},
            {"label": "Fecha de llegada",           "name": "arrival",    "type": "date",     "required": True,  "options": []},
            {"label": "Fecha de salida",            "name": "departure",  "type": "date",     "required": True,  "options": []},
            {"label": "Número de huéspedes",        "name": "guests",     "type": "number",   "required": True,  "options": []},
            {"label": "Suite preferida",            "name": "suite",      "type": "select",   "required": False,
             "options": ["La Vigna", "Il Frantoio", "Il Pozzo", "La Cisterna", "La Torre", "Il Cortile", "Exclusiva del borgo · 8 suites", "Sin preferencia"]},
            {"label": "Paquete",                    "name": "package",    "type": "select",   "required": False,
             "options": ["Estancia breve · 2 noches", "Estancia clásica · 4 noches", "Estancia larga · 7 noches", "Exclusiva del borgo · 5 noches", "Boda íntima"]},
            {"label": "Alergias o peticiones alimentarias", "name": "allergies", "type": "text", "required": False, "options": []},
            {"label": "Notas a la dirección",       "name": "notes",      "type": "textarea", "required": False, "options": []},
        ],

        "offices_label":   "Direcciones",
        "offices_heading": "El borgo y los caseríos.",
        "offices_intro":
            "El borgo es accesible en coche desde Florencia (1h45) o Roma (2h30) · "
            "traslado desde el aeropuerto de Florencia o desde la estación de "
            "Chiusi-Chianciano bajo petición.",
        # list[3] of dict (role, city, address, hours, email)
        "offices": [
            {
                "role":     "Borgo · recepción",
                "city":     "Pienza · Siena",
                "address":  "Borgo San Marco di Sopra 17 · 53026 Pienza",
                "hours":    "Recepción 24 horas · check-in 14–22 · check-out hasta las 11",
                "email":    "concierge@borgosanmarco.it",
            },
            {
                "role":     "Fattoria Trebbio · bodega y olivar",
                "city":     "Pienza · Siena · 1,2 km del borgo",
                "address":  "Strada provinciale 146 · 53026 Pienza",
                "hours":    "Bodega · martes y jueves 17–19 · catas bajo reserva",
                "email":    "cantina@borgosanmarco.it",
            },
            {
                "role":     "Aqua di Borgo · spa",
                "city":     "Cisterna del siglo XVIII · planta sótano",
                "address":  "Borgo San Marco di Sopra 17 · planta –1",
                "hours":    "Spa 9–13 · 15–20 · tratamientos con cita previa",
                "email":    "spa@borgosanmarco.it",
            },
        ],

        "press_contact_label": "Prensa y medios",
        "press_contact_text":
            "Para solicitudes editoriales, pruebas de servicio y entrevistas a la "
            "dirección · escriban a Maria Bonelli, oficina de prensa de Vittoria "
            "Sernigi, indicando la cabecera y el tema.",
        "press_contact_email": "stampa@borgosanmarco.it",
    },

    # ─── POSTS (8 suites · las tarjetas de habitación) ─
    "posts": [
        {
            "slug":         "suite-la-vigna",
            "image":        _SUITE_VIGNA,
            "kicker":       "Suite 01",
            "title":        "La Vigna",
            "date":         "Temporada 2026 · abril – octubre",
            "author":       "Borgo San Marco",
            "read_min":     "62 m²",
            "lede":
                "La suite asomada al viñedo histórico de Sangiovese de propiedad · "
                "primera planta del ala oeste · cama matrimonial king · techo de "
                "vigas originales del siglo XVII.",
            "footer_strap": "Disponible de mayo a septiembre · vistas al viñedo",
            # list of 2-tuples (k, v)
            "meta_rows": [
                ("Planta",        "Primera · ala oeste"),
                ("Camas",         "Matrimonial king + chaise longue"),
                ("Superficie",    "62 m² + 8 m² de pequeña logia"),
                ("Vistas",        "Viñedo histórico de Sangiovese · olivar"),
                ("Baño",          "Mármol travertino · ducha walk-in + bañera"),
                ("Incluye",       "Desayuno · spa · cata en bodega"),
                ("Temporada",     "Disponible de mayo a septiembre"),
            ],
            # list of 2-tuples (kind, text)
            "body": [
                ("p", "La Vigna es la suite más solicitada de la casa · vista directa sobre el viñedo histórico de Sangiovese que da los racimos al Brunello propio de la Fattoria Trebbio. Techo de vigas originales del siglo XVII, suelo de baldosa pulida, mobiliario recuperado de las casas del borgo."),
                ("p", "La pequeña logia privada de 8 m² está amueblada con un sofá de mimbre y una mesita de pietra serena · perfecta para el desayuno a dos o para la copa de Brunello al atardecer (siempre incluida, de la bodega de Anna)."),
                ("h3", "El viñedo histórico"),
                ("p", "El viñedo de propiedad de la Fattoria Trebbio se extiende sobre 4,2 hectáreas al sur del borgo, exposición este-sureste. Vendimia manual en octubre · vinificación en pequeños depósitos de acero · crianza en barrica grande de roble · embotellado en la finca. El Brunello lleva la misma firma del borgo."),
                ("ul", ["Capacidad · dos adultos · cuna para bebé bajo petición", "Wifi · fibra 1 Gbit/s · línea directa en la red del borgo", "Climatización · independiente, regulable desde la suite", "Caja fuerte · digital · para objetos de valor", "TV · 55 pulgadas · canales internacionales bajo petición"]),
                ("p", "La suite La Vigna está disponible de mayo a finales de septiembre. Para la temporada 2026 solo es reservable en paquete de al menos tres noches."),
            ],
        },
        {
            "slug":         "suite-il-frantoio",
            "image":        _SUITE_FRANTOIO,
            "kicker":       "Suite 02",
            "title":        "Il Frantoio",
            "date":         "Temporada 2026 · toda la temporada",
            "author":       "Borgo San Marco",
            "read_min":     "78 m²",
            "lede":
                "La suite más amplia · planta baja del ala sur · en el centro de la "
                "habitación la antigua muela del molino de aceite de 1620, "
                "conservada como elemento arquitectónico.",
            "footer_strap": "Disponible de abril a octubre · planta baja ala sur",
            "meta_rows": [
                ("Planta",        "Planta baja · ala sur"),
                ("Camas",         "Matrimonial + saloncito separado"),
                ("Superficie",    "78 m² + 12 m² de patio"),
                ("Vistas",        "Patio interior con muela de 1620"),
                ("Baño",          "Mármol blanco · bañera freestanding + ducha"),
                ("Incluye",       "Desayuno · spa · cata en bodega + aceite"),
                ("Temporada",     "Disponible toda la temporada"),
            ],
            "body": [
                ("p", "Il Frantoio es la mayor de las ocho suites · 78 m² de planta más 12 m² de patio privado sobre el patio interior. La muela circular del molino original de 1620 se ha conservado en el centro de la habitación como elemento arquitectónico — no funciona, pero permanece intacta, en pietra serena."),
                ("p", "La suite incluye una pequeña bodega privada con seis botellas del Brunello de la Fattoria Trebbio (vendimias 2018-2020) y una botella de aceite de oliva virgen extra del olivar histórico · los huéspedes pueden catar a su gusto y solo se factura al final de la estancia."),
                ("h3", "El molino histórico"),
                ("p", "El molino original estuvo en funcionamiento de 1620 hasta 1968, cuando el aceite de la Fattoria Trebbio empezó a procesarse en el molino comunal de Pienza. La muela de la suite es una de las dos originarias · la otra se expone en el museo de la casa, junto al patio."),
                ("ul", ["Capacidad · dos adultos + un niño en sofá-cama", "Wifi · fibra 1 Gbit/s", "Climatización · independiente, doble zona habitación/saloncito", "Patio · 12 m² con mesa y sillones de hierro forjado", "Mini bodega privada · 6 botellas de Brunello + 1 botella de aceite virgen extra"]),
                ("p", "Il Frantoio está disponible durante toda la temporada abierta. Reserva de al menos dos noches."),
            ],
        },
        {
            "slug":         "suite-il-pozzo",
            "image":        _SUITE_POZZO,
            "kicker":       "Suite 03",
            "title":        "Il Pozzo",
            "date":         "Temporada 2026 · bajo petición",
            "author":       "Borgo San Marco",
            "read_min":     "54 m²",
            "lede":
                "La suite más reservada · planta baja con acceso directo al patio "
                "interior del siglo XVII · en el centro del patio el pozo octogonal "
                "original de 1612.",
            "footer_strap": "Bajo petición · solo parejas · patio privado",
            "meta_rows": [
                ("Planta",        "Planta baja · patio interior"),
                ("Camas",         "Matrimonial estándar"),
                ("Superficie",    "54 m² + patio privado 28 m²"),
                ("Vistas",        "Patio octogonal con pozo de 1612"),
                ("Baño",          "Pietra serena · ducha walk-in"),
                ("Incluye",       "Desayuno · spa · bodega · patio"),
                ("Temporada",     "Bajo petición · solo parejas · animales admitidos"),
            ],
            "body": [
                ("p", "Il Pozzo es la suite más reservada de la casa · acceso únicamente desde el patio interior, sin ninguna vista al exterior del borgo. El pozo octogonal de 1612 sigue funcionando (agua dulce de la capa freática de San Quirico) y da sombra a un pequeño patio de 28 m² de uso exclusivo de la suite."),
                ("p", "Esta suite se ofrece solo a parejas · sin niños · y admite perros pequeños de menos de 10 kg bajo petición (suplemento de 30 € por noche, comedero y cama incluidos)."),
                ("h3", "El pozo octogonal"),
                ("p", "El pozo octogonal es uno de los tres pozos del borgo · es el único todavía activo. Octogonal como la cúpula de Brunelleschi, de la que Pío II era admirador. Construido en 1612 por el mismo albañil que levantó la casa parroquial · firma esculpida en el interior de la boca del pozo, ilegible desde 1923 pero documentada en un cuaderno de 1898 conservado en la casa parroquial."),
                ("ul", ["Capacidad · dos adultos · sin niños", "Perros pequeños admitidos · suplemento 30 €/noche", "Patio privado · 28 m² con mesa de hierro · sombra del pozo", "Wifi · fibra 1 Gbit/s", "Climatización · independiente"]),
                ("p", "Il Pozzo está disponible solo bajo petición directa a la dirección. Estancia mínima de tres noches."),
            ],
        },
        {
            "slug":         "suite-la-cisterna",
            "image":        _SUITE_CISTERNA,
            "kicker":       "Suite 04",
            "title":        "La Cisterna",
            "date":         "Temporada 2026 · bajo petición",
            "author":       "Borgo San Marco",
            "read_min":     "88 m²",
            "lede":
                "Suite alojada en la bóveda de la cisterna del siglo XVIII · planta "
                "sótano · cama con dosel · luz natural cenital a través de la "
                "claraboya original de 1742.",
            "footer_strap": "Bajo petición · luna de miel recomendada",
            "meta_rows": [
                ("Planta",        "Planta sótano (–1) · ala este"),
                ("Camas",         "Matrimonial + dosel de nogal"),
                ("Superficie",    "88 m² · bóveda de 4,2 m"),
                ("Vistas",        "Claraboya cenital · sin vistas al exterior"),
                ("Baño",          "Travertino · bañera en forma de cisterna"),
                ("Incluye",       "Desayuno · spa · bodega · experiencia nocturna"),
                ("Temporada",     "Bajo petición · luna de miel recomendada"),
            ],
            "body": [
                ("p", "La Cisterna es la suite más codiciada del borgo · alojada en la bóveda de la cisterna del siglo XVIII, planta sótano, techo a 4,2 metros de altura. La luz natural entra únicamente por la claraboya cenital de 1742 (original) · de noche el cielo estrellado de la Val d'Orcia entra directamente en la habitación."),
                ("p", "La cisterna original recogía el agua de lluvia del tejado de la casa parroquial hasta 1923, cuando el borgo se conectó al acueducto comunal. La restauración Castellini-Mancini de 2009 conservó la curvatura original y la inscripción mural del propietario del siglo XVIII (Giovan Pietro Buonsignori, 1742)."),
                ("h3", "La cama con dosel"),
                ("p", "La cama es una pieza histórica · dosel de nogal macizo de Pratomagno, hierro forjado a mano por el herrero del borgo (Mario Calzini, 1971-2018, hoy su sobrino Luca continúa el taller). Tejidos del dosel en lino de Bonotto. Las lámparas de aceite se han sustituido por pequeñas luces LED de temperatura cálida."),
                ("ul", ["Capacidad · dos adultos · sin niños", "Wifi · fibra 1 Gbit/s · sin cobertura 4G en el local subterráneo", "Climatización · independiente, temperatura constante 20 °C también en verano", "Bañera · de travertino · forma de cisterna", "Experiencia nocturna · bajo reserva, apertura de la claraboya con el observatorio astronómico del borgo"]),
                ("p", "La Cisterna está disponible solo bajo petición directa · particularmente recomendada para lunas de miel y aniversarios. Estancia mínima de cuatro noches."),
            ],
        },
        {
            "slug":         "suite-la-torre",
            "image":        _SUITE_TORRE,
            "kicker":       "Suite 05",
            "title":        "La Torre",
            "date":         "Temporada 2026 · abril – octubre",
            "author":       "Borgo San Marco",
            "read_min":     "70 m²",
            "lede":
                "Suite alojada en la torre angular medieval · segunda planta · "
                "vistas de 270° sobre la Val d'Orcia hasta el Monte Amiata · cama "
                "matrimonial con estudio contiguo.",
            "footer_strap": "Disponible de abril a octubre · vistas de 270°",
            "meta_rows": [
                ("Planta",        "Segunda planta · torre angular"),
                ("Camas",         "Matrimonial + estudio con sofá-cama"),
                ("Superficie",    "70 m² + 6 m² de estudio"),
                ("Vistas",        "270° · Val d'Orcia · Monte Amiata · Pienza"),
                ("Baño",          "Mármol negro · ducha walk-in"),
                ("Incluye",       "Desayuno · spa · bodega · catalejo astronómico"),
                ("Temporada",     "Abril – octubre · escalera de 23 peldaños"),
            ],
            "body": [
                ("p", "La Torre ocupa la segunda planta de la torre angular medieval del borgo · vistas de 270° sobre la Val d'Orcia (suroeste), Pienza (noroeste) y hasta el Monte Amiata (sureste) en los días despejados. Tres ventanas originales del siglo XVI con vidrios emplomados restaurados."),
                ("p", "El estudio contiguo de 6 m² está amueblado con un escritorio de nogal de Pratomagno y una librería con volúmenes sobre la Val d'Orcia (en italiano y en inglés) · perfecto para quien necesita media jornada de trabajo durante la estancia."),
                ("h3", "El catalejo astronómico"),
                ("p", "La torre cuenta con un pequeño catalejo astronómico Bresser de 90 mm instalado a la altura de la ventana oeste · ideal para observar las constelaciones de la Val d'Orcia (sin contaminación lumínica). Manual de uso en el cajón · guía vespertina con el referente de sala bajo reserva."),
                ("ul", ["Capacidad · dos adultos + un niño en sofá-cama del estudio", "Escalera · 23 peldaños · sin ascensor en la torre", "Wifi · fibra 1 Gbit/s", "Climatización · ventilador de techo + aparato independiente", "Catalejo · Bresser 90 mm + manual + guía bajo petición"]),
                ("p", "La Torre está disponible de abril a octubre. Estancia mínima de dos noches."),
            ],
        },
        {
            "slug":         "suite-il-cortile",
            "image":        _SUITE_CORTILE,
            "kicker":       "Suite 06",
            "title":        "Il Cortile",
            "date":         "Temporada 2026 · mayo – octubre",
            "author":       "Borgo San Marco",
            "read_min":     "65 m²",
            "lede":
                "Suite con pequeña logia privada sobre la pérgola de glicinia · "
                "planta baja del ala norte · jardín privado de 18 m² con mesita y "
                "sillones.",
            "footer_strap": "Disponible de mayo a octubre · jardín + pérgola",
            "meta_rows": [
                ("Planta",        "Planta baja · ala norte"),
                ("Camas",         "Matrimonial + sofá-cama"),
                ("Superficie",    "65 m² + jardín privado 18 m²"),
                ("Vistas",        "Pérgola de glicinia · jardín privado"),
                ("Baño",          "Travertino · ducha walk-in"),
                ("Incluye",       "Desayuno · spa · bodega · jardín privado"),
                ("Temporada",     "Mayo – octubre · glicinia en flor de mayo a junio"),
            ],
            "body": [
                ("p", "Il Cortile tiene el acceso más directo a la pérgola de glicinia, alma del borgo · la glicinia fue plantada en 1924 por la familia Buonsignori, floración plena en las tres primeras semanas de mayo. Jardín privado de 18 m² delimitado por un murete de pietra serena · amueblado con dos sillones de hierro forjado y una mesita de piedra."),
                ("p", "El desayuno en la pérgola es una costumbre de la casa · cada mañana de 8 a 10:30 la pérgola se convierte en pequeña corte de desayuno · huéspedes sentados en mesitas bajas, brigada de sala en circulación continua · pan de Lorenzini caliente del horno del borgo, mermeladas de escaramujo de la dirección, quesos de Castelmuzio, fruta de los caseríos vecinos."),
                ("h3", "La glicinia de 1924"),
                ("p", "La glicinia la plantó en 1924 Caterina Buonsignori (1902-1989, última de la familia originaria del borgo) como regalo de bodas para su hija Anna. Desde entonces ha crecido hasta cubrir la pérgola entera del patio. La floración plena dura tres semanas · primera decena de mayo hasta el 25 de mayo aproximadamente."),
                ("ul", ["Capacidad · dos adultos + un niño en sofá-cama", "Jardín privado · 18 m² · murete de pietra serena · amueblado", "Wifi · fibra 1 Gbit/s", "Climatización · independiente", "Desayuno · servido en la pérgola de glicinia de 8 a 10:30"]),
                ("p", "Il Cortile está disponible de mayo a octubre. Para admirar la glicinia en flor reserven en la primera quincena de mayo."),
            ],
        },
        {
            "slug":         "suite-la-loggia",
            "image":        _SUITE_LOGGIA,
            "kicker":       "Suite 07",
            "title":        "La Loggia",
            "date":         "Temporada 2026 · abril – octubre",
            "author":       "Borgo San Marco",
            "read_min":     "82 m²",
            "lede":
                "Suite de la planta noble · logia renacentista abierta sobre "
                "Pienza · techo artesonado pintado de 1671 · cama matrimonial king "
                "+ estudio + baño principal.",
            "footer_strap": "Disponible de abril a octubre · planta noble",
            "meta_rows": [
                ("Planta",        "Primera planta noble · ala oeste"),
                ("Camas",         "Matrimonial king + estudio"),
                ("Superficie",    "82 m² + logia 14 m²"),
                ("Vistas",        "Pienza · catedral · Palazzo Piccolomini"),
                ("Baño",          "Travertino + estatuario · bañera + ducha separada"),
                ("Incluye",       "Desayuno · spa · bodega · cena privada en logia bajo petición"),
                ("Temporada",     "Abril – octubre · ceremonia civil en logia posible"),
            ],
            "body": [
                ("p", "La Loggia es la suite de la planta noble · 82 m² más una logia renacentista de 14 m² abierta sobre Pienza · se ven la catedral de Bernardo Rossellino de 1462 y el Palazzo Piccolomini. El techo artesonado pintado de 1671 fue restaurado en 2009 por Mauro Pellegrini, restaurador de Siena."),
                ("p", "La logia es el lugar de la ceremonia civil de las bodas íntimas del borgo (máximo 36 invitados). Bajo petición es posible organizar una cena privada en la logia para los huéspedes de la suite · servicio del chef Tommaso · precio bajo petición."),
                ("h3", "El techo artesonado de 1671"),
                ("p", "El techo fue encargado por Pietro Buonsignori en 1671 al pintor Domenico Manetti de Siena (1609-1683). Treinta artesones pintados al temple: vistas de la Val d'Orcia, símbolos heráldicos de la familia, putti vendimiadores. La restauración de 2009 devolvió los colores originales; los dorados se confirmaron en laboratorio."),
                ("ul", ["Capacidad · dos adultos + un niño en sofá-cama del estudio", "Logia · 14 m² abierta sobre Pienza · amueblada · cena privada bajo petición", "Wifi · fibra 1 Gbit/s", "Climatización · doble zona", "Ceremonia civil · en logia · máximo 36 invitados · bajo petición"]),
                ("p", "La Loggia está disponible de abril a octubre. Estancia mínima de dos noches, tres noches para la ventana de ceremonia civil."),
            ],
        },
        {
            "slug":         "suite-la-cantina",
            "image":        _SUITE_CANTINA,
            "kicker":       "Suite 08",
            "title":        "La Cantina",
            "date":         "Temporada 2026 · bajo petición",
            "author":       "Borgo San Marco",
            "read_min":     "92 m²",
            "lede":
                "Suite alojada en la bodega antigua del siglo XVIII (la bodega "
                "operativa está hoy en la Fattoria Trebbio) · planta sótano · cama "
                "matrimonial + zona de estar + vinoteca privada de 12 referencias.",
            "footer_strap": "Bajo petición · ideal para amantes del vino",
            "meta_rows": [
                ("Planta",        "Planta sótano (–1) · ala sur"),
                ("Camas",         "Matrimonial king + zona de estar"),
                ("Superficie",    "92 m² · bóveda de 3,8 m"),
                ("Vistas",        "Vinoteca privada acristalada · sin vistas al exterior"),
                ("Baño",          "Travertino · ducha walk-in panorámica sobre la bodega"),
                ("Incluye",       "Desayuno · spa · 12 referencias en la vinoteca privada · cata guiada"),
                ("Temporada",     "Bajo petición · ideal en otoño"),
            ],
            "body": [
                ("p", "La Cantina está alojada en la bodega antigua del borgo · planta sótano, bóveda de 3,8 metros · fue bodega operativa hasta 2007, cuando el vino de la Fattoria Trebbio se trasladó a la bodega moderna a 1,2 km. La suite conserva la vinoteca privada acristalada, completada cada temporada con 12 referencias de la casa seleccionadas por la sumiller Anna."),
                ("p", "La vinoteca está incluida en la estancia · las 12 botellas quedan a disposición de los huéspedes para cata ilimitada durante la permanencia. La cata guiada por Anna está prevista una velada por estancia (incluida en la tarifa) · catas adicionales bajo petición."),
                ("h3", "Las 12 referencias de la temporada"),
                ("p", "La composición de la vinoteca cambia cada temporada. La selección de 2026 (a cargo de Anna Ricci): 4 Brunello (Fattoria Trebbio 2018, Biondi-Santi 2016, Casanova di Neri 2017, Il Poggione 2018) · 3 Vino Nobile (Avignonesi 2019, Salcheto 2020, Boscarelli 2018) · 2 Chianti Classico (Castello di Ama 2019, Felsina 2018) · 3 vinos experimentales de la Toscana del sur (Petricci 2020, Gualdo del Re 2021, Salvo 2019)."),
                ("ul", ["Capacidad · dos adultos · sin niños", "Vinoteca · 12 referencias · selección de Anna Ricci AIS · cambia cada temporada", "Cata guiada · una velada por estancia (incluida)", "Wifi · fibra 1 Gbit/s · sin cobertura 4G", "Climatización · independiente, temperatura constante 18 °C"]),
                ("p", "La Cantina está disponible bajo petición · ideal en temporada otoñal tras la vendimia. Estancia mínima de cuatro noches."),
            ],
        },
    ],
}
