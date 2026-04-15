"""Phase 2g3.7 · Session 53 · Villa — ES native-voice tree. Editorial-concierge private-advisory voice."""
from __future__ import annotations

from typing import Any


VILLA_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Residencias",  "kind": "home"},
        {"slug": "collezione", "label": "Colección",    "kind": "blog_list"},
        {"slug": "territorio", "label": "Territorios",  "kind": "about"},
        {"slug": "studio",     "label": "El Estudio",   "kind": "team"},
        {"slug": "esperienza", "label": "Experiencia",  "kind": "services"},
        {"slug": "concierge",  "label": "Concierge",    "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":   "V",
        "logo_word":      "Villa Prestige",
        "logo_subline":   "Private Advisory · desde 1998",
        "tag":            "Colección primavera 2026 · Cartera N.º 03",
        "phone":          "concierge@villaprestige.it",
        "phone_label":    "Línea reservada del concierge",
        "email":          "concierge@villaprestige.it",
        "email_label":    "Concierge privado",
        "address":        "Via Montenapoleone 17 · 20121 Milán",
        "hours_compact":  "Visitas únicamente bajo cita · Lun–Vie 10–19 · Sáb a petición",
        "hours_footer_rows": [
            "Reuniones en nuestras oficinas · concierge privado",
            "Idiomas: italiano · english · français",
        ],
        "license":        "Insc. RIEA Milán N.º 2841 · NIF IT07324110984 · Registro de asesores privados",
        "footer_intro":
            "Villa Prestige — estudio de private advisory para residencias de autor en Italia y la Costa "
            "Azul. Una cartera reducida, un único interlocutor, discreción absoluta. Seleccionamos "
            "residencias históricas y contemporáneas exclusivamente para clientes privados y family "
            "offices, previa evaluación en dos niveles: autoría arquitectónica y coherencia con el "
            "territorio.",

        # Nav reservation CTA (private viewing)
        "nav_cta":         "Solicitar una visita privada",
        "nav_cta_kind":    "appointment",
        "nav_cta_short":   "Solicitar visita",

        # Footer labels
        "foot_studio":   "El estudio",
        "foot_pages":    "Mapa",
        "foot_contact":  "Concierge",
        "foot_offices":  "Oficinas",
        "offices_footer_rows": [
            "Milán · Montenapoleone 17",
            "Portofino · oficina concierge",
            "Saint-Tropez · bajo cita",
        ],
        "office_rows": [
            "Milán · Montenapoleone 17",
            "Portofino · oficina concierge",
            "Saint-Tropez · bajo cita",
        ],

        # Cross-page editorial meta-strip labels (D-047)
        "dossier_label":        "Dossier",
        "portfolio_label":      "Cartera",
        "territorio_label":     "Territorio",
        "superficie_label":     "Superficie",
        "provenance_label":     "Procedencia",
        "access_label":         "Acceso",
        "availability_label":   "Disponibilidad",
        "price_note":           "Precio a consultar",
        "nda_required_label":   "Acuerdo de confidencialidad requerido antes del dossier",
        "viewing_on_request":   "Disponible únicamente bajo cita",
        "referent_label":       "Interlocutor único",
        "concierge_line_label": "Línea concierge",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        # Fullbleed editorial cover
        "cover_location": "Portofino · Liguria",
        "cover_image_credit": "Colección de primavera · dossier 03 / 18",
        "cover_image":
            "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=2200&h=1400&fit=crop",

        # Eyebrow + serif drama
        "eyebrow":          "Villa Prestige · Private Advisory · Italia y Costa Azul",
        "headline":         "Residencias <em>de autor</em>, para quienes saben reconocerlas.",
        "sub":
            "Una cartera reducida de residencias privadas — históricas y contemporáneas — presentada "
            "únicamente bajo cita. Visitas reservadas, dossier editorial dedicado, negociación "
            "discreta: del primer encuentro a la firma notarial, un solo interlocutor.",

        # Hero wordmark + counter chip (from DNA)
        "hero_wordmark":        "Villa Prestige",
        "hero_location":        "Portofino · Colección primavera 2026",
        "hero_counter_label":   "Residencia en portada",
        "hero_counter_value":   "N.º 03 / 18",
        "hero_series_label":    "En portada",
        "hero_series_title":    "« Villa Aurelia » · Portofino",
        "hero_series_note":
            "Residencia histórica de 1922, parque de tres hectáreas sobre el golfo. Cuatrocientos "
            "metros cuadrados, biblioteca firmada, piscina infinity frente a la isla Palmaria.",
        "primary_cta":          "Solicitar una visita privada",
        "primary_cta_href":     "concierge",
        "secondary_cta":        "Colección de primavera",
        "secondary_cta_href":   "collezione",

        # Editorial credit cells — fullbleed hero bottom strip
        "hero_credit_cells": [
            ("Colección", "N.º 03 / 18"),
            ("Territorio","Portofino · Liguria"),
            ("Superficie","400 m² · parque 30.000 m²"),
            ("Acceso",    "Únicamente bajo cita"),
        ],

        # Signature properties strip — 4 dossier cards (2-up editorial grid)
        "signature_label":   "Colección de primavera",
        "signature_heading": "Residencias <em>elegidas</em> para esta temporada.",
        "signature_intro":
            "Cada propiedad se presenta únicamente tras una evaluación en dos niveles — autoría "
            "arquitectónica y coherencia con el territorio. El listado completo está disponible "
            "a petición, en formato de dossier editorial firmado por el interlocutor dedicado.",
        "signature": [
            {
                "index":       "01",
                "title":       "Villa Aurelia",
                "territorio":  "Portofino · Liguria",
                "superficie":  "400 m² · parque 30.000 m²",
                "provenance":  "Años 20 · firma Piacentini",
                "availability":"Tres días disponibles",
                "slug":        "villa-aurelia-portofino",
                "image":
                    "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "02",
                "title":       "Castello di Monterò",
                "territorio":  "Chianti Classico · Toscana",
                "superficie":  "1.200 m² · 18 hectáreas",
                "provenance":  "Siglo XII · restauración 2014",
                "availability":"Mandato exclusivo",
                "slug":        "castello-di-montero-chianti",
                "image":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "03",
                "title":       "Penthouse Quadronno",
                "territorio":  "Milán · Magenta",
                "superficie":  "380 m² · terraza 180 m²",
                "provenance":  "Ático único · vista al Duomo",
                "availability":"Bajo cita",
                "slug":        "penthouse-quadronno-milano",
                "image":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "04",
                "title":       "Mas de la Mer",
                "territorio":  "Saint-Tropez · Costa Azul",
                "superficie":  "550 m² · viñedo privado",
                "provenance":  "Siglo XVIII · certificado",
                "availability":"Novedad",
                "slug":        "mas-de-la-mer-saint-tropez",
                "image":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
        ],
        "signature_link_all":  "Descubrir la colección completa  →",
        "signature_link_href": "collezione",

        # Territory ribbon — continental destinations
        "territory_label":  "Territorios de referencia",
        "territory":        ["PORTOFINO", "CHIANTI CLASSICO", "COSTA SMERALDA", "LAGO DI COMO", "SAINT-TROPEZ", "CAPRI", "VAL D'ORCIA"],

        # Private advisor block
        "advisor_label":    "Asesora privada",
        "advisor_heading":  "Un solo <em>interlocutor</em>, del primer dossier a la escritura.",
        "advisor_intro":
            "Cada cliente privado es atendido personalmente por su asesor, desde la entrega del "
            "primer dossier editorial hasta la firma notarial. Nunca más de ocho mandatos activos "
            "por asesor, para garantizar una presencia real y una discreción absoluta.",
        "advisor_name":     "Alessandra Visconti di Modrone",
        "advisor_role":     "Directora de clientela privada · desde 2011",
        "advisor_bio":
            "Quince años entre Savills, Knight Frank y Sotheby's International Realty "
            "(Londres · Milán · Portofino). Ha gestionado personalmente más de ochenta "
            "transacciones privadas en Italia y la Costa Azul para familias europeas, "
            "americanas y asiáticas. Cada cliente es atendido por ella, desde el primer "
            "encuentro confidencial hasta la firma notarial.",
        "advisor_portrait":
            "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
        "advisor_cta":      "Solicitar una primera conversación",
        "advisor_cta_href": "concierge",

        # Editorial storytelling — the maison's numbers (discreet stats — counters OK)
        "numbers_label":    "El estudio en cifras",
        "numbers_heading":  "Una cartera <em>reducida</em>, una presencia total.",
        "numbers": [
            ("26",   "años de private advisory"),
            ("42",   "residencias en cartera"),
            ("9",    "asesores privados dedicados"),
            ("150",  "family offices acompañados"),
        ],
        "numbers_note":
            "Nunca más de cincuenta mandatos simultáneos. Cada dossier pasa por la mesa de la "
            "dirección antes de entrar en colección.",

        # Press ribbon
        "press_label":    "Editorial",
        "press_intro":    "Aparece en",
        "press_items":    [
            "Financial Times · How to Spend It",
            "Monocle",
            "Robb Report",
            "Corriere Living",
            "AD Italia",
        ],

        # Editorial storytelling panel — closing private-viewing band
        "private_label":    "Visita privada",
        "private_heading":  "Una hora en sala reservada, <em>el dossier en sus manos.</em>",
        "private_intro":
            "La reunión en nuestras oficinas se celebra bajo cita, en presencia del interlocutor "
            "dedicado. Preparamos de antemano los dossieres editoriales de las residencias "
            "compatibles con el perfil del cliente y reservamos una sala donde las vistas se "
            "proyectan en gran formato. El servicio es gratuito y estrictamente reservado.",
        "private_primary":       "Solicitar una visita privada",
        "private_primary_href":  "concierge",
        "private_secondary":     "Descubrir la experiencia",
        "private_secondary_href":"esperienza",
    },

    # ─── COLLEZIONE — signature properties list (blog_list) ───
    "collezione": {
        "eyebrow":   "Colección primavera 2026 · dossieres 01 – 14",
        "headline":  "Catorce <em>residencias de autor</em>, a la espera de su interlocutor.",
        "intro":
            "La colección está abierta exclusivamente a clientes bajo acuerdo de confidencialidad. "
            "Cada dossier incluye procedencia arquitectónica, plano editorial, territorio y una "
            "breve historia de la residencia. Los precios se comunican directamente por el "
            "interlocutor tras el primer encuentro confidencial.",

        # Lead post / hero dossier
        "lead_image":
            "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=1600&h=1000&fit=crop",

        # Filters by territorio / provenance / availability
        "filter_label":  "Selección",
        "filter_groups": [
            {
                "label":   "Territorio",
                "options": ["Todos", "Portofino", "Chianti Classico", "Milán", "Costa Azul", "Capri", "Lago di Como", "Val d'Orcia"],
            },
            {
                "label":   "Procedencia",
                "options": ["Todas", "Siglos XVII–XVIII", "Principios del siglo XX · firma de autor", "Contemporáneo · restauración reciente", "Ático único"],
            },
            {
                "label":   "Disponibilidad",
                "options": ["Abiertas", "Novedad", "Exclusiva", "Únicamente bajo cita"],
            },
        ],
        "sort_label":    "Ordenar por",
        "sort_options":  ["Territorio", "Procedencia", "Más recientes", "Exclusivas"],

        "result_count":    "14 dossieres en la colección de primavera",
        "result_subtitle": "Actualizada cada primer jueves del mes",

        "footer_note_label": "Entrada en colección",
        "footer_note":
            "La colección de verano 2026 abre el jueves 28 de mayo. Los clientes ya bajo acuerdo "
            "de confidencialidad mantienen prioridad absoluta sobre todo nuevo dossier. Para "
            "sumarse a la lista reservada, escribir directamente al concierge de la maison.",
    },

    # ─── TERRITORIO (about) — editorial territorio cards ──────
    "territorio": {
        "eyebrow":   "Territorios de referencia · siete geografías privadas",
        "headline":  "El <em>paisaje</em> es la primera firma de una residencia.",
        "intro":
            "Trabajamos exclusivamente en siete territorios italianos y franceses. Cada uno "
            "cuenta con un interlocutor residente, un archivo editorial dedicado, una red de "
            "arquitectos de confianza. No operamos fuera de estas geografías — es así como "
            "garantizamos un conocimiento real de las casas, de los vecinos, de los vientos "
            "dominantes.",

        # Editorial statement
        "statement_label":   "Manifiesto",
        "statement_heading": "Siete territorios, <em>siete archivos privados.</em>",
        "statement_text":
            "Cada territorio está a cargo de un interlocutor que reside allí desde hace al "
            "menos diez años. Conocemos las residencias antes de que lleguen al mercado — a "
            "menudo las seguimos a través de varias generaciones de propietarios. Nuestro "
            "archivo recoge datos catastrales históricos, estudios paisajísticos, relaciones "
            "con los municipios y los servicios de patrimonio competentes.",

        # 6 territorio cards — history, provenance, architects, property count
        "territories_label":   "Los siete territorios",
        "territories_heading": "Las geografías <em>de la colección.</em>",
        "territories_intro":
            "Del promontorio de Portofino a los viñedos de Saint-Tropez, de las colinas del "
            "Chianti a la Costa Esmeralda. Cada territorio tiene su temporada de entrada, "
            "su espinazo arquitectónico, su registro de familias.",
        "territories": [
            {
                "name":      "Portofino",
                "region":    "Liguria · golfo del Tigullio",
                "history":   "El promontorio frecuentado por las familias milanesas desde la segunda posguerra. Casas ribereñas sobre el mar, terrazas sobre la bahía de San Fruttuoso, jardines cerrados de buganvillas y olivos centenarios. La luz de finales de primavera es el mejor documento.",
                "architects":"Gio Ponti · Gae Aulenti · Umberto Riva · restauraciones recientes A. Citterio",
                "count":     "9 residencias en colección",
                "since":     "Interlocutor residente desde 2008",
                "image":
                    "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Chianti Classico",
                "region":    "Toscana · Gaiole – Radda – Castellina",
                "history":   "El espinazo del Chianti entre Siena y Florencia, rico en castillos medievales y pievi restauradas. Residencias habitadas con viñedos en producción, olivares seculares y bodegas subterráneas. El territorio privilegia la restauración conservativa bajo la tutela del patrimonio de Florencia.",
                "architects":"restauraciones de Tobia Scarpa · Massimo Carmassi · studio ACPV",
                "count":     "7 residencias en colección",
                "since":     "Interlocutor residente desde 2011",
                "image":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Costa Smeralda",
                "region":    "Cerdeña · Porto Cervo – Porto Rotondo",
                "history":   "El litoral trazado en los años sesenta por el Príncipe Karim Aga Khan. Villas concebidas por Jacques Couëlle y Luigi Vietti, granito local y cubiertas de enebro. Terrazas de piedra sobre el mar, calas privadas accesibles sólo a pie o en tender.",
                "architects":"Jacques Couëlle · Luigi Vietti · Savin Couëlle · restauraciones recientes A. Citterio",
                "count":     "5 residencias en colección",
                "since":     "Interlocutor residente desde 2014",
                "image":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Lago di Como",
                "region":    "Lombardía · Cernobbio – Tremezzo – Bellagio",
                "history":   "Las villas históricas del Lario, de Villa d'Este a Villa Balbianello. Jardines botánicos esculpidos en el siglo XVIII, darsenas privadas, miradores de jazmín. Propiedades a menudo catalogadas, con restauraciones conducidas de acuerdo con el patrimonio de Milán.",
                "architects":"villas históricas · Pelagio Palagi · restauraciones de Lissoni Casal Ribeiro",
                "count":     "6 residencias en colección",
                "since":     "Interlocutor residente desde 2010",
                "image":
                    "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Saint-Tropez",
                "region":    "Costa Azul · Var · Pampelonne",
                "history":   "El Var interior, colinas entre Ramatuelle y Gassin. Mas provenzales originales de los siglos XVII–XVIII, algunos con viñedo de producción AOP Côtes de Provence. Casas a distancia discreta del mar, a media hora del puerto de Saint-Tropez.",
                "architects":"François Catroux · Jacques Grange · Studio KO · restauraciones tradicionales",
                "count":     "4 residencias en colección",
                "since":     "Oficina concierge desde 2016",
                "image":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Capri & Val d'Orcia",
                "region":    "Capri · Toscana meridional · Pienza – Montalcino",
                "history":   "Dos territorios hermanos por su rareza y por el recato familiar. En Capri, casas en terrazas hacia los Faraglioni, a menudo transmitidas durante tres generaciones. En Val d'Orcia, fincas agrícolas con pieve románica y viñedo de Brunello, propiedades UNESCO bajo estricta protección.",
                "architects":"Capri · Francesco Venezia · tradición caprese local; Val d'Orcia · Matteo Nunziati · Studio Perruccio",
                "count":     "5 residencias en colección",
                "since":     "Interlocutores residentes desde 2013",
                "image":
                    "https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
        ],
        "territory_card_cta": "Solicitar el dossier de territorio  →",
        "territory_card_cta_href": "concierge",

        # Closing — the referent promise
        "referent_label":   "El interlocutor residente",
        "referent_heading": "Conocemos las casas <em>antes</em> de que salgan al mercado.",
        "referent_text":
            "El interlocutor residente no es un consultor a llamada: es una persona que vive "
            "el territorio desde hace al menos diez años, habla la lengua local, conoce los "
            "servicios de patrimonio y las familias históricas. Muchas residencias de la "
            "colección nos llegan por la palabra de un amigo común, no por el mercado — así "
            "es como estas propiedades se han transmitido siempre, entre personas que se "
            "tienen confianza.",

        # Discreet stats — territories in numbers
        "stats_label":      "Territorios en cifras",
        "stats": [
            ("7",   "territorios de referencia"),
            ("36",  "residencias históricas en archivo"),
            ("18",  "arquitectos de autor asociados"),
            ("26",  "años de presencia continua"),
        ],
    },

    # ─── STUDIO (team) — private advisors ─────────────────────
    "studio": {
        "eyebrow":  "El estudio · nueve asesores privados · Milán Portofino Saint-Tropez",
        "headline": "Nueve asesores, <em>nunca más de ocho mandatos cada uno.</em>",
        "intro":
            "El estudio es una maison de asesores privados: cada uno de nosotros tiene raíces "
            "profesionales en las grandes casas internacionales — Sotheby's International "
            "Realty, Knight Frank, Savills, Christie's Real Estate — y hoy ejerce en total "
            "independencia, con una cartera reducida. No portamos enseñas, sólo dossieres. "
            "No vendemos nada bajo presión.",

        # Director hero card — Alessandra Visconti
        "director_label":   "Dirección",
        "director_name":    "Alessandra Visconti di Modrone",
        "director_role":    "Directora de clientela privada · fundadora · desde 1998",
        "director_text":
            "Funda Villa Prestige en Milán en 1998, tras ocho años en Sotheby's International "
            "Realty Londres. Ha gestionado personalmente más de ochenta transacciones "
            "privadas en Italia y la Costa Azul — de Villa Aurelia en Portofino al Castello "
            "di Monterò en Chianti — para familias europeas, americanas, asiáticas y de "
            "Oriente Medio. Firma en Monocle y Corriere Living una columna anual sobre el "
            "mercado de las residencias históricas.",
        "director_portrait":
            "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=800&h=1100&fit=crop",
        "director_quote":
            "«No elegimos las residencias por su precio. Elegimos las residencias que nos "
            "quedan en el pensamiento después de una sola visita. El ochenta por ciento de "
            "las propiedades que nos llegan son descartadas antes de su entrada en colección.»",
        "director_quote_attribution": "Alessandra Visconti di Modrone · Monocle · marzo 2025",

        # 4 private advisors
        "advisors_label":   "Asesores privados",
        "advisors_heading": "Un <em>interlocutor único</em>, del primer dossier a la escritura.",
        "advisors_intro":
            "Cada cliente es atendido personalmente por un asesor nombrado al inicio del "
            "mandato. Jamás un intermediario, jamás un relevo. Si el cliente desea una "
            "segunda opinión, el estudio pone a disposición un segundo asesor en calidad "
            "consultiva, siempre bajo el mismo techo de reserva.",
        "advisors": [
            {
                "name":      "Francesco Medici di Porrena",
                "role":      "Asesor sénior · territorio Chianti y Val d'Orcia",
                "bio":
                    "Doce años en Knight Frank Florencia, especializado en la restauración "
                    "conservativa de residencias históricas del Chianti Classico. Licenciatura "
                    "en Arquitectura en Florencia, máster en la Bartlett de Londres. Gestiona "
                    "personalmente todas las negociaciones en la Toscana meridional.",
                "territories":"Chianti Classico · Val d'Orcia · Florencia",
                "since":     "En el estudio desde 2014",
                "portrait":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Italiano · English · Français",
            },
            {
                "name":      "Élodie Charbonneau",
                "role":      "Asesora sénior · territorio Costa Azul y Capri",
                "bio":
                    "Diez años en Savills París y Christie's Real Estate Monte-Carlo. "
                    "Curadora de ventas privadas para coleccionistas franceses y americanos "
                    "en la Costa Azul. Especializada en mas provenzales auténticos y villas "
                    "de autor. Responsable de la oficina concierge de Saint-Tropez.",
                "territories":"Saint-Tropez · Mónaco · Capri",
                "since":     "En el estudio desde 2016",
                "portrait":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Français · English · Italiano",
            },
            {
                "name":      "Arianna Testa Piccolomini",
                "role":      "Asesora sénior · territorio Portofino y Lago di Como",
                "bio":
                    "Ocho años en Sotheby's International Realty Milán, luego consultora "
                    "independiente para dos family offices de Brescia y Piamonte. Residente "
                    "en Portofino desde hace diez años, conoce personalmente a las familias "
                    "históricas del promontorio. Lenguas de trabajo: italiano, inglés, alemán.",
                "territories":"Portofino · Lago di Como · Milán",
                "since":     "En el estudio desde 2017",
                "portrait":
                    "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Italiano · English · Deutsch",
            },
            {
                "name":      "Omar Khoury",
                "role":      "Asesor de clientela privada · clientes asiáticos y de Oriente Medio",
                "bio":
                    "Nueve años entre Knight Frank Dubái y Christie's Hong Kong. Especializado "
                    "en la acogida de clientela privada procedente de Hong Kong, Singapur, "
                    "Doha, Riad y Dubái. Coordina las traducciones y las certificaciones "
                    "notariales internacionales. Reside entre Milán y Portofino.",
                "territories":"clientes asiáticos · Emiratos · Golfo Pérsico",
                "since":     "En el estudio desde 2019",
                "portrait":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "العربية · English · Français · 中文 (nivel básico)",
            },
        ],

        # Legal / fiscal partner ribbon
        "partners_label":   "Socios institucionales",
        "partners_heading": "Los socios <em>jurídicos y fiscales</em> del estudio.",
        "partners_intro":
            "Villa Prestige no redacta escrituras. Cada negociación va acompañada de socios "
            "institucionales seleccionados — notarías, abogados internacionales, fiscalistas "
            "patrimoniales — que operan bajo el mismo techo de reserva. El cliente firma un "
            "mandato directo con ellos, separado del nuestro, con honorarios transparentes.",
        "partners": [
            ("Studio Notarile Baldi-Corsini",     "Milán · notaría de las familias lombardas"),
            ("Gattai Minoli Agostinelli",         "Milán · derecho inmobiliario internacional"),
            ("Chiomenti",                          "Milán · fiscalidad patrimonial para family offices"),
            ("Ughi e Nunziante",                   "Roma · patrimonio y bienes culturales"),
            ("Cabinet Bredin Prat",                "París · transacciones Costa Azul"),
        ],

        # Press / editorial mentions
        "press_label":   "Editorial",
        "press_heading": "Menciones recientes <em>del estudio.</em>",
        "press_items": [
            {
                "magazine": "Financial Times · How to Spend It",
                "issue":    "Primavera 2026",
                "title":    "The quiet sellers of the Italian coast",
                "byline":   "Perfil · por Bill Prince",
            },
            {
                "magazine": "Monocle",
                "issue":    "Issue 181",
                "title":    "The Chianti Classico revival",
                "byline":   "Reportaje · por Josh Fehnert",
            },
            {
                "magazine": "Robb Report",
                "issue":    "Abril 2025",
                "title":    "Nine villas, one director",
                "byline":   "Perfil · por Laurie Kahle",
            },
            {
                "magazine": "Corriere Living",
                "issue":    "Enero 2026",
                "title":    "El mercado de las residencias históricas, visto desde Milán",
                "byline":   "Columna anual · firmada por Alessandra Visconti di Modrone",
            },
            {
                "magazine": "AD Italia",
                "issue":    "Noviembre 2025",
                "title":    "Villa Aurelia · el regreso de un icono de Portofino",
                "byline":   "Fotografía · Gianluca Ruotolo",
            },
        ],

        # Studio in numbers
        "numbers_label":   "El estudio en cifras",
        "numbers": [
            ("26",   "años desde la fundación"),
            ("9",    "asesores privados dedicados"),
            ("42",   "residencias en colección"),
            ("7",    "territorios de referencia"),
            ("150",  "family offices acompañados"),
            ("91",   "transacciones privadas desde 2015"),
        ],

        # Closing visit CTA
        "visit_label":     "Reunión en nuestras oficinas",
        "visit_heading":   "Una primera <em>conversación confidencial</em> en las oficinas de Milán o Portofino.",
        "visit_text":
            "Recibimos exclusivamente bajo cita, en las oficinas de Milán y Portofino, o en "
            "la oficina concierge de Saint-Tropez. La primera reunión es una conversación "
            "confidencial — no comporta mandato alguno — durante la cual se define el perfil "
            "del cliente y se firma el acuerdo de confidencialidad que da acceso a los dossieres.",
        "visit_primary":      "Solicitar la primera conversación",
        "visit_primary_href": "concierge",
    },

    # ─── ESPERIENZA (services) — private-viewing process ─────
    "esperienza": {
        "eyebrow":  "La experiencia · cinco pasos en la discreción",
        "headline": "Del primer <em>dossier</em> a la firma notarial.",
        "intro":
            "Acompañamos al cliente a lo largo de cinco etapas, cada una reservada y "
            "documentada. El recorrido dura en promedio cuatro meses para las propiedades "
            "listas para escritura, hasta doce para las residencias históricas con protección "
            "paisajística. Ninguna etapa es obligatoria — el cliente puede interrumpir el "
            "mandato en cualquier momento, sin penalización alguna.",

        # 5-step private-viewing process
        "process_label":   "El recorrido",
        "process_heading": "Cinco pasos, <em>un solo interlocutor.</em>",
        "process_intro":
            "Cada paso es atendido personalmente por el asesor nombrado al inicio del "
            "mandato. El cliente puede pedir en cualquier momento hablar con la dirección — "
            "Alessandra Visconti di Modrone responde personalmente en un día hábil.",
        "process": [
            {
                "n":        "01",
                "title":    "Solicitud del dossier",
                "duration": "Respuesta en 48 horas hábiles",
                "text":
                    "El cliente escribe al concierge describiendo el perfil de la residencia "
                    "deseada — territorio, procedencia, superficie, temporada de uso. El "
                    "asesor del territorio responde en dos días hábiles con un primer resumen "
                    "de la colección compatible y una propuesta de primer encuentro.",
            },
            {
                "n":        "02",
                "title":    "Acuerdo de confidencialidad",
                "duration": "Firmado en la oficina o a distancia",
                "text":
                    "Antes de la entrega de los dossieres completos, cliente y estudio firman "
                    "un acuerdo de confidencialidad recíproco que compromete a ambas partes a "
                    "un recato absoluto sobre las propiedades, las familias vendedoras y las "
                    "condiciones económicas. Es un acuerdo estándar y no impide la asistencia "
                    "de un segundo asesor fiscal.",
            },
            {
                "n":        "03",
                "title":    "Videoconferencia editorial",
                "duration": "Media jornada · con el asesor",
                "text":
                    "Un primer encuentro por videoconferencia — o en la oficina, si el "
                    "cliente lo prefiere — en el que repasamos juntos tres o cuatro "
                    "dossieres editoriales, con planos, historia de la residencia, imágenes "
                    "actualizadas, informe paisajístico. El cliente elige las dos residencias "
                    "para la visita en presencia.",
            },
            {
                "n":        "04",
                "title":    "Visita privada en presencia",
                "duration": "Una o dos jornadas en el territorio",
                "text":
                    "Acompañamos personalmente al cliente a la propiedad, en presencia del "
                    "interlocutor residente y, si la familia vendedora lo acepta, de ésta. "
                    "La visita transcurre sin presión comercial: dura el tiempo necesario, "
                    "incluye un almuerzo en las inmediaciones y puede repetirse una segunda "
                    "vez en una temporada distinta.",
            },
            {
                "n":        "05",
                "title":    "Negociación y escritura",
                "duration": "De 45 días a 6 meses",
                "text":
                    "El estudio redacta la propuesta de adquisición de acuerdo con el cliente "
                    "y la presenta directamente a la familia vendedora. Los socios notariales "
                    "preparan el compromiso y la escritura definitiva. El asesor acompaña "
                    "personalmente al cliente a la firma y queda a su disposición durante "
                    "los seis meses siguientes, para toda gestión posterior a la entrega.",
            },
        ],

        # Testimonial slot (single, editorial, discreet)
        "testimonial_label":   "Referencia",
        "testimonial_text":
            "«El estudio me fue recomendado por un antiguo socio en Londres. Solicité una "
            "primera conversación en Milán y en seis meses adquirimos una villa en Costa "
            "Esmeralda para nuestra familia, sin que la negociación saliera jamás del "
            "círculo de las tres personas implicadas. La interlocutora sigue siendo la misma "
            "— hoy conoce también a mis hijos.»",
        "testimonial_author":  "Un family office lombardo · adquisición 2024 · Porto Cervo",

        # FAQ accordion
        "faq_label":   "Preguntas recurrentes",
        "faq_items": [
            {
                "q": "¿Cuánto dura de media el recorrido hasta la escritura?",
                "a": "De cuatro a doce meses, según la complejidad de la propiedad. Las "
                     "residencias listas para escritura se cierran en cuarenta y cinco días; "
                     "aquellas históricas con protección paisajística o que requieren "
                     "reparcelación catastral demandan plazos más largos para las "
                     "verificaciones ante los servicios de patrimonio.",
            },
            {
                "q": "¿Cuáles son los idiomas de trabajo del estudio?",
                "a": "Italiano, inglés y francés en cada negociación. Alemán para el "
                     "territorio del Lago di Como, árabe y chino a nivel básico para clientes "
                     "de Oriente Medio y Asia. Las traducciones juradas de todos los "
                     "documentos notariales están incluidas en el mandato.",
            },
            {
                "q": "¿Cómo se calculan los honorarios del estudio?",
                "a": "Siempre como porcentaje del precio final de adquisición, comunicado "
                     "con transparencia en el mandato inicial. No se debe cuota fija alguna "
                     "durante las fases de estudio — únicamente a la firma notarial efectiva.",
            },
            {
                "q": "¿Representa el estudio también a los vendedores?",
                "a": "Sí, pero nunca simultáneamente en la misma residencia. Cada mandato es "
                     "exclusivo de una de las dos partes, a fin de garantizar la máxima "
                     "transparencia en la negociación. El cliente sabe siempre para qué parte "
                     "estamos trabajando.",
            },
            {
                "q": "¿Es posible visitar una residencia más de una vez?",
                "a": "Sí, a petición. Acompañamos gratuitamente al cliente en una segunda "
                     "visita en temporada distinta — muchas propiedades costeras se visitan "
                     "una vez en verano y otra en invierno antes de una decisión.",
            },
            {
                "q": "¿Cómo protegen la confidencialidad de la negociación?",
                "a": "Cada negociación se abre con un acuerdo de confidencialidad recíproco, "
                     "firmado en la oficina o a distancia, que compromete al estudio, al "
                     "cliente y a la familia vendedora. Ningún dossier es accesible en "
                     "formato digital abierto — todos los documentos se entregan en "
                     "plataforma reservada o en formato impreso.",
            },
        ],

        # Closing CTA
        "cta_label":      "Primera conversación",
        "cta_heading":    "Una <em>primera conversación</em> es siempre gratuita y reservada.",
        "cta_text":
            "Ningún mandato se debe tras el primer encuentro. El cliente recibe un primer "
            "resumen de la colección compatible, una propuesta de asesor dedicado y una "
            "fecha orientativa para la primera visita privada. Si el perfil no resulta "
            "compatible, agradecemos y nos despedimos — sin continuidad.",
        "cta_primary":      "Solicitar la primera conversación",
        "cta_primary_href": "concierge",
    },

    # ─── CONCIERGE (contact) — private-viewing request ───────
    "concierge": {
        "eyebrow":  "Concierge privado · bajo cita",
        "headline": "Únicamente <em>bajo cita</em>.",
        "intro":
            "Recibimos exclusivamente bajo cita, en las oficinas de Milán y Portofino y en "
            "la oficina concierge de Saint-Tropez. El concierge lee personalmente cada "
            "solicitud y responde en el día hábil siguiente. Para las solicitudes en árabe, "
            "chino o alemán, la respuesta va firmada directamente por el asesor dedicado al "
            "territorio correspondiente.",

        # Dedicated phone line by territorio
        "phone_label":    "Línea concierge por territorio",
        "phone_intro":
            "Cada territorio cuenta con una línea dedicada, abierta únicamente a clientes "
            "bajo acuerdo de confidencialidad o presentados por un referente. Para un primer "
            "contacto, siempre es preferible escribir al concierge por correo electrónico — "
            "la respuesta es más rápida y está mejor documentada.",
        "phone_rows": [
            ("Milán · dirección",                "concierge@villaprestige.it"),
            ("Portofino · oficina concierge",    "portofino@villaprestige.it"),
            ("Saint-Tropez · oficina concierge", "saint-tropez@villaprestige.it"),
            ("Clientes asiáticos · Omar Khoury","asia@villaprestige.it"),
        ],

        # Form section (private-viewing request with NDA consent)
        "form_section_label":  "Solicitud de visita privada",
        "form_section_intro":
            "Cumplimente con amabilidad los campos necesarios. El concierge responderá en "
            "el día hábil siguiente, en italiano, inglés o francés. Para solicitudes en "
            "otros idiomas, indique su preferencia en el campo de notas.",

        "form_helper_required":  "Los campos marcados son obligatorios",
        "form_submit_button":    "Enviar solicitud reservada",
        "form_submit_note":
            "Su solicitud es leída personalmente por el concierge de la dirección. Ningún "
            "boletín, ninguna comunicación comercial. Los datos se eliminan en noventa días "
            "si el perfil no resulta compatible con la colección.",

        "form_fields": [
            {"name":"titolo",    "label":"Tratamiento", "type":"select", "required":True,
             "options":["Sra.","Sr.","Estudio · family office","Prensa · editorial"]},
            {"name":"nome",      "label":"Nombre y apellidos", "type":"text",
             "placeholder":"Ej. Sra. Eleonora Visconti", "required":True},
            {"name":"email",     "label":"Correo reservado", "type":"email",
             "placeholder":"e.visconti@ejemplo.es", "required":True},
            {"name":"telefono",  "label":"Teléfono (opcional)", "type":"tel",
             "placeholder":"+34 …", "required":False},
            {"name":"sede",      "label":"Oficina preferida", "type":"select", "required":True,
             "options":["Milán · Montenapoleone","Portofino · concierge","Saint-Tropez · concierge","Videoconferencia preliminar","Sin preferencia"]},
            {"name":"territorio","label":"Territorio de interés", "type":"select", "required":True,
             "options":["Portofino · Liguria","Chianti Classico · Toscana","Costa Smeralda · Cerdeña","Lago di Como · Lombardía","Saint-Tropez · Costa Azul","Capri · Campania","Val d'Orcia · Toscana","Dos o más territorios"]},
            {"name":"profilo",   "label":"Perfil de la residencia", "type":"select", "required":True,
             "options":["Residencia histórica con parque","Ático o penthouse urbano","Villa contemporánea de autor","Finca agrícola con viñedo","Propiedad costera","Sin perfil preestablecido"]},
            {"name":"date",      "label":"Fechas preferidas", "type":"text",
             "placeholder":"Ej. segunda semana de mayo · o entrada de temporada", "required":False},
            {"name":"note",      "label":"Notas para el concierge", "type":"textarea",
             "placeholder":"Indique preferencias de idioma, referente de presentación, disponibilidades familiares.", "required":True, "rows":5},
            {"name":"nda",       "label":"Consiento la firma de un acuerdo de confidencialidad recíproco antes de la entrega de los dossieres editoriales", "type":"checkbox", "required":True},
        ],

        # Office cards — three concierge offices
        "offices_label":   "Las oficinas",
        "offices_heading": "Tres oficinas, <em>tres salas reservadas.</em>",
        "offices_intro":
            "Cada oficina recibe únicamente bajo cita, en una sala reservada dotada de "
            "archivo editorial local. La oficina de Milán es la dirección general; "
            "Portofino y Saint-Tropez cuentan en temporada con los interlocutores residentes.",
        "offices": [
            {
                "city":    "Milán",
                "address": "Via Montenapoleone 17 · 20121 Milán",
                "hours":   "Lun – Vie · 10:00 – 19:00 · únicamente bajo cita",
                "email":   "concierge@villaprestige.it",
                "role":    "Dirección · archivo central · reuniones en la oficina",
            },
            {
                "city":    "Portofino",
                "address": "Via Roma 28 · 16034 Portofino GE",
                "hours":   "Abr – Oct · visitas bajo cita · noviembre – marzo a petición",
                "email":   "portofino@villaprestige.it",
                "role":    "Oficina concierge · interlocutor residente · Liguria",
            },
            {
                "city":    "Saint-Tropez",
                "address": "Place de la Garonne 6 · 83990 Saint-Tropez",
                "hours":   "May – Sep · visitas bajo cita · octubre – abril a petición",
                "email":   "saint-tropez@villaprestige.it",
                "role":    "Oficina concierge · interlocutor residente · Costa Azul",
            },
        ],

        # Press contact ribbon
        "press_contact_label":   "Contactos de prensa",
        "press_contact_text":
            "Para solicitudes editoriales y de prensa especializada, escribir directamente "
            "a la dirección: stampa@villaprestige.it. Notas de prensa, carpetas "
            "fotográficas y entrevistas son coordinadas personalmente por la directora. "
            "Respondemos a la prensa internacional en un día hábil, en italiano, inglés o "
            "francés.",
        "press_contact_email":   "stampa@villaprestige.it",
    },

    # ─── BLOG POSTS (used by collezione blog_list + blog_detail) ──
    # These render the signature properties as editorial dossiers.
    "posts": [
        {
            "slug":     "villa-aurelia-portofino",
            "kicker":   "Portofino · Liguria · años 20",
            "title":    "Villa Aurelia — residencia histórica de 1922 sobre el promontorio",
            "lede":
                "Cuatrocientos metros cuadrados sobre el golfo del Tigullio, parque de tres "
                "hectáreas, biblioteca firmada y piscina infinity suspendida frente a la isla "
                "Palmaria.",
            "date":     "12 de abril de 2026",
            "read_min": "7",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Colección",    "N.º 03 / 18 · primavera 2026"),
                ("Territorio",   "Portofino · Liguria · golfo del Tigullio"),
                ("Superficie",   "400 m² interiores · parque 30.000 m² · 7 dormitorios"),
                ("Procedencia",  "1922 · firma Marcello Piacentini · restauración A. Citterio 2014"),
                ("Disponibilidad","Tres días al mes · bajo cita"),
                ("Precio",       "A consultar con el interlocutor"),
            ],
            "body": [
                ("p",
                 "La residencia abre su portón carruajero sobre una subida sombreada de encinas "
                 "centenarias y se revela sólo al cabo de trescientos metros, dominando el "
                 "golfo del Tigullio a sesenta metros de altura. La planta es en herradura, con "
                 "cuerpo central de 1922 y dos alas añadidas en 1938 por la misma firma de "
                 "Marcello Piacentini. La intervención de 2014 — dirigida por Antonio Citterio "
                 "con el paisajista Paolo Pejrone para el parque — conservó todos los frescos "
                 "originales del salón central, restituyó las carpinterías en madera maciza e "
                 "introdujo la piscina infinity, hoy inscrita entre las imágenes icónicas del "
                 "promontorio."),
                ("h2", "El parque · tres hectáreas de encinas, olivos y camelias"),
                ("p",
                 "El parque, trazado originalmente por el conde Ricci en 1924 y revisado por "
                 "Paolo Pejrone en 2014, alterna encinas centenarias, olivares en producción y "
                 "una colección de treinta y dos variedades de camelia. La residencia dispone "
                 "de una escalera privada que desciende directamente al mar, con atraque para "
                 "embarcaciones de hasta ocho metros. El jardín es totalmente autónomo en "
                 "riego gracias a una cisterna de recogida de aguas pluviales restaurada en 2018."),
                ("h2", "Interiores · biblioteca firmada y salón de representación"),
                ("p",
                 "En el piano nobile se articulan el salón central de 140 metros cuadrados, con "
                 "frescos originales de escuela ligur, un comedor frente al mar y la "
                 "biblioteca firmada, con boiseries de nogal diseñadas en 1938. En la primera "
                 "planta, la suite principal ocupa toda el ala este, con baño privado en "
                 "mármol de Carrara y terraza frente a la isla Palmaria. Otras seis "
                 "habitaciones se distribuyen entre la primera y la segunda planta, cada una "
                 "con baño propio."),
                ("blockquote",
                 "«La villa de Portofino no es una propiedad: es un gesto de recato que se "
                 "transmite entre familias que se tienen confianza. Nuestra misión es sólo "
                 "custodiar el traspaso.»"),
                ("h2", "Procedencia · la mano de Piacentini, la restauración de Citterio"),
                ("p",
                 "Encargada en 1921 por la familia genovesa Acquarone al arquitecto Marcello "
                 "Piacentini — entonces ya autor de numerosas intervenciones en el paseo "
                 "marítimo de Viareggio — Villa Aurelia fue completada en 1922 y permaneció en "
                 "la misma familia durante tres generaciones. Pasa en 2007 a una segunda "
                 "familia milanesa, que en 2014 encarga a Antonio Citterio la restauración "
                 "conservativa, con Paolo Pejrone para el parque. La intervención ha sido "
                 "publicada en AD Italia, Elle Decor y Corriere Living."),
                ("ol", [
                    "Acceso: camino privado con portón carruajero, supervisión paisajística de la oficina de patrimonio de Génova.",
                    "Parque: tres hectáreas · escalera privada al mar · atraque para embarcaciones de hasta ocho metros.",
                    "Superficie interior: cuatrocientos metros cuadrados · siete dormitorios · baños en mármol de Carrara.",
                    "Instalaciones: calefacción geotérmica · fotovoltaica de bajo impacto visual · cisterna de aguas pluviales.",
                    "Precio: a consultar con el interlocutor · acuerdo de confidencialidad requerido antes del dossier completo.",
                ]),
                ("p",
                 "La disponibilidad se limita a tres días al mes para visitas privadas, en "
                 "presencia de la familia propietaria. La asesora del territorio — Arianna "
                 "Testa Piccolomini, residente en Portofino desde hace diez años — acompaña "
                 "personalmente al cliente desde la primera videoconferencia hasta la firma "
                 "notarial."),
            ],
            "footer_strap": "Villa Prestige · Portofino · dossier N.º 03 / 18",
        },
        {
            "slug":     "castello-di-montero-chianti",
            "kicker":   "Chianti Classico · Toscana · siglo XII",
            "title":    "Castello di Monterò — fortaleza medieval con viñedo en producción",
            "lede":
                "Mil doscientos metros cuadrados sobre dieciocho hectáreas, viñedo de Chianti "
                "Classico en conducción biodinámica, bodega subterránea, capilla consagrada en "
                "1432.",
            "date":     "5 de abril de 2026",
            "read_min": "9",
            "author":   "Francesco Medici di Porrena",
            "image":
                "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Colección",    "N.º 07 / 18 · primavera 2026"),
                ("Territorio",   "Chianti Classico · Toscana · Gaiole in Chianti"),
                ("Superficie",   "1.200 m² interiores · 18 hectáreas · 7 hectáreas de viñedo"),
                ("Procedencia",  "Siglo XII · restauración conservativa Tobia Scarpa 2014"),
                ("Disponibilidad","Exclusiva · un solo mandato activo"),
                ("Precio",       "A consultar con el interlocutor"),
            ],
            "body": [
                ("p",
                 "El castillo se alza sobre una dorsal a 520 metros de altitud entre Gaiole in "
                 "Chianti y Radda, mirando al sur sobre el valle del Arbia y al norte sobre las "
                 "colinas de San Polo. El cuerpo central, con torre de vigía de 1185, ha "
                 "permanecido sustancialmente intacto desde su construcción original; la "
                 "restauración de 2014, conducida por Tobia Scarpa bajo la supervisión de la "
                 "oficina de patrimonio de Florencia, ha vuelto habitables los mil doscientos "
                 "metros cuadrados interiores sin alterar una sola piedra del envoltorio medieval."),
                ("h2", "La finca · dieciocho hectáreas, viñedo en conducción biodinámica"),
                ("p",
                 "La propiedad se extiende sobre dieciocho hectáreas, de las cuales siete "
                 "están dedicadas a viñedo de Chianti Classico DOCG, en conducción biodinámica "
                 "certificada desde 2016. La producción anual es de unas quince mil botellas, "
                 "distribuidas exclusivamente por asignación privada — jamás en el mercado. La "
                 "bodega subterránea, excavada bajo el cuerpo central, alberga treinta "
                 "barricas y una colección histórica de dos mil botellas."),
                ("h2", "El cuerpo central · sala de armas y capilla de 1432"),
                ("p",
                 "En la planta baja se articulan la sala de armas de 180 metros cuadrados, la "
                 "capilla privada consagrada en 1432 (aún en uso anual el 24 de junio, "
                 "festividad del patrono), la cocina histórica con horno de leña original. La "
                 "primera planta alberga la biblioteca familiar con tres mil volúmenes, cinco "
                 "dormitorios principales, dos salones. En la segunda planta, la torre de "
                 "vigía ha sido transformada en despacho privado con vista de trescientos "
                 "sesenta grados sobre el valle."),
                ("blockquote",
                 "«El castillo no está en venta porque la familia necesite dinero. Está en "
                 "venta porque la siguiente generación vive entre Londres y Shanghái, y "
                 "sentimos la necesidad de cederlo a quien sabrá llevarlo adelante.»"),
                ("h2", "Procedencia · siete siglos, dos familias"),
                ("p",
                 "Documentado desde 1185 en los protocolos notariales sieneses, el castillo "
                 "fue durante cuatrocientos años fortín de la familia Ricasoli, luego de los "
                 "Pannocchieschi a partir de 1570 y, por último, de la actual familia Medici "
                 "di Porrena desde 1812. La decisión de confiar el mandato a Villa Prestige "
                 "nace del vínculo personal de treinta años entre la familia y el asesor "
                 "sénior Francesco Medici di Porrena — primo de la misma familia y asesor del "
                 "estudio para el Chianti Classico."),
                ("ol", [
                    "Acceso: camino blanco privado de un kilómetro, protección paisajística UNESCO en valoración.",
                    "Parque y viñedo: dieciocho hectáreas · siete en Chianti Classico biodinámico · olivar de dos mil árboles centenarios.",
                    "Superficie interior: mil doscientos metros cuadrados · diez dormitorios · capilla consagrada 1432.",
                    "Bodega: subterránea bajo el cuerpo central · treinta barricas · colección histórica de dos mil botellas.",
                    "Instalaciones: calefacción por biomasa · fotovoltaica de bajo impacto · agua de manantial privado.",
                    "Precio: a consultar con el interlocutor · exclusiva total hasta el otoño de 2026.",
                ]),
                ("p",
                 "La disponibilidad se limita a un solo día al mes para visitas privadas, "
                 "directamente con la familia y el asesor. El recorrido de adquisición "
                 "requiere al menos seis meses para las verificaciones ante la oficina de "
                 "patrimonio de Florencia y la Región Toscana. El traspaso del mandato "
                 "agrícola del viñedo se coordina con el consorcio del Chianti Classico."),
            ],
            "footer_strap": "Villa Prestige · Chianti Classico · dossier N.º 07 / 18",
        },
        {
            "slug":     "penthouse-quadronno-milano",
            "kicker":   "Milán · Magenta · ático único",
            "title":    "Penthouse Quadronno — ático de 1957 con vista al Duomo",
            "lede":
                "Trescientos ochenta metros cuadrados en la sexta planta de via Quadronno, "
                "terraza de 180 m², vista frontal al Duomo, interiores firmados por Vico "
                "Magistretti en 1958.",
            "date":     "28 de marzo de 2026",
            "read_min": "6",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Colección",    "N.º 11 / 18 · primavera 2026"),
                ("Territorio",   "Milán · Magenta · via Quadronno"),
                ("Superficie",   "380 m² interiores · terraza 180 m² · 4 dormitorios"),
                ("Procedencia",  "1957 · firma Luigi Caccia Dominioni · interiores Vico Magistretti 1958"),
                ("Disponibilidad","Bajo cita"),
                ("Precio",       "A consultar con el interlocutor"),
            ],
            "body": [
                ("p",
                 "El ático ocupa la totalidad de la sexta planta del palacio Quadronno, "
                 "levantado en 1957 sobre proyecto de Luigi Caccia Dominioni para un encargo "
                 "privado de la burguesía industrial milanesa. Los interiores fueron "
                 "completados diez meses después por Vico Magistretti, entonces de treinta y "
                 "tres años, con una labor de artesanía detallada en maderas, mármoles y "
                 "manillas, aún hoy intacta en su integridad original."),
                ("h2", "La planta · trescientos ochenta metros cuadrados articulados"),
                ("p",
                 "La entrada se abre sobre una galería de dieciocho metros de longitud que "
                 "distribuye las dos alas de la casa — zona de día al sudeste, zona de noche "
                 "al noroeste. El salón principal de ciento diez metros cuadrados se asoma "
                 "frontalmente al Duomo a través de una vidriera de Jacopo Foggini instalada "
                 "en 2018. El comedor, la cocina profesional y la despensa completan el ala "
                 "de día. Cuatro dormitorios, cada uno con baño privado en mármol de Carrara "
                 "original de 1957, componen el ala de noche."),
                ("h2", "La terraza · ciento ochenta metros cuadrados en perímetro"),
                ("p",
                 "La terraza perimetral, ciento ochenta metros cuadrados en total, ofrece una "
                 "vista de trescientos sesenta grados sobre la ciudad: Duomo al este, "
                 "Castello Sforzesco al norte, San Siro en el horizonte occidental. La "
                 "intervención paisajística de Patricia Urquiola en 2019 añadió una bañera "
                 "de hidromasaje cubierta, una pérgola de terracota y una colección de "
                 "quince variedades de aromáticas mediterráneas."),
                ("blockquote",
                 "«El Quadronno no es un ático: es un pequeño museo de la casa milanesa de "
                 "los años cincuenta. Cada detalle de Magistretti sigue en su sitio.»"),
                ("h2", "Procedencia · Caccia Dominioni, Magistretti, Urquiola"),
                ("p",
                 "Encargado en 1956 por la familia Brambilla a Luigi Caccia Dominioni, "
                 "completado en 1957. Los interiores de Vico Magistretti se entregaron en "
                 "1958 y no han sufrido alteración significativa durante sesenta años. En "
                 "2018, la segunda familia propietaria encargó a Jacopo Foggini la vidriera "
                 "frontal; en 2019, la intervención paisajística sobre la terraza fue "
                 "firmada por Patricia Urquiola. Todas las intervenciones han sido "
                 "documentadas en Domus, Interni y Corriere Living."),
                ("ol", [
                    "Acceso: portería de un palacio de gran prestigio · ascensor de servicio dedicado.",
                    "Superficie interior: trescientos ochenta metros cuadrados · cuatro dormitorios · baños en mármol original de 1957.",
                    "Terraza: ciento ochenta metros cuadrados · bañera de hidromasaje cubierta · pérgola de terracota Urquiola 2019.",
                    "Vista: frontal al Duomo de Milán · panorámica de trescientos sesenta grados.",
                    "Instalaciones: calefacción autónoma · climatización de control independiente ala por ala.",
                    "Precio: a consultar con el interlocutor · acuerdo de confidencialidad requerido antes del dossier completo.",
                ]),
                ("p",
                 "La disponibilidad está abierta bajo cita. El recorrido medio de "
                 "adquisición es de cuarenta y cinco días desde el acuerdo de "
                 "confidencialidad hasta la escritura, gracias a la documentación catastral "
                 "completa y ya actualizada. La familia vendedora está disponible para un "
                 "encuentro directo antes de la firma."),
            ],
            "footer_strap": "Villa Prestige · Milán · dossier N.º 11 / 18",
        },
        {
            "slug":     "mas-de-la-mer-saint-tropez",
            "kicker":   "Saint-Tropez · Costa Azul · siglo XVIII",
            "title":    "Mas de la Mer — mas provenzal de 1754 con viñedo AOP",
            "lede":
                "Quinientos cincuenta metros cuadrados en las colinas de Ramatuelle, viñedo "
                "privado en Côtes de Provence AOP, construcción original de 1754 restaurada "
                "en 2017.",
            "date":     "20 de marzo de 2026",
            "read_min": "8",
            "author":   "Élodie Charbonneau",
            "image":
                "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Colección",    "N.º 14 / 18 · primavera 2026"),
                ("Territorio",   "Saint-Tropez · Costa Azul · Ramatuelle"),
                ("Superficie",   "550 m² interiores · 6 hectáreas · viñedo 2,5 ha"),
                ("Procedencia",  "1754 · mas provenzal original · restauración François Catroux 2017"),
                ("Disponibilidad","Novedad · recién entrada en colección"),
                ("Precio",       "A consultar con el interlocutor"),
            ],
            "body": [
                ("p",
                 "El mas se alza en las colinas interiores de Ramatuelle, a doce kilómetros del "
                 "puerto de Saint-Tropez, en un silencio que sólo el Var interior sabe "
                 "ofrecer. La construcción original es de 1754, perteneciente a la misma "
                 "familia de tradición vitícola hasta 1948. Adquirido en 1985 por una "
                 "familia parisina, ha sido restaurado en 2017 por François Catroux — la "
                 "última obra privada del arquitecto francés antes de su desaparición — con "
                 "el propósito de devolver a los interiores su sencillez original, tras "
                 "cincuenta años de intervenciones dispares."),
                ("h2", "El viñedo · dos hectáreas y media de Côtes de Provence AOP"),
                ("p",
                 "La propiedad incluye dos hectáreas y media de viñedo en producción AOP "
                 "Côtes de Provence, con vinificación confiada al Domaine Ott para la parte "
                 "de rosado y al Domaine Tempier para la de tinto. La producción anual es de "
                 "unas siete mil botellas, distribuidas exclusivamente a la familia "
                 "propietaria y a sus invitados. La bodega de transformación se halla "
                 "directamente bajo el mas, en un local semisubterráneo de 1802."),
                ("h2", "Interiores · salón a doble altura y dormitorio principal"),
                ("p",
                 "La planta baja se articula en torno a un salón a doble altura de ciento "
                 "veinte metros cuadrados, con chimenea de esquina en piedra original y "
                 "vigas de roble a la vista. La cocina es abovedada, pavimentada en "
                 "baldosas de Salernes. En la primera planta, el dormitorio principal ocupa "
                 "toda el ala sur con baño privado en mármol de Caunes-Minervois; otros tres "
                 "dormitorios dobles, cada uno con baño propio, completan la planta. La "
                 "dependencia del guarda alberga un apartamento para custodio o invitados."),
                ("blockquote",
                 "«François Catroux devolvió al mas la lentitud que el Var interior conoce "
                 "desde siempre. Es su última obra privada, y se nota.»"),
                ("h2", "Procedencia · de la viticultura a la familia parisina"),
                ("p",
                 "Construido en 1754 por la familia Bertrand, que lo poseyó durante seis "
                 "generaciones cultivando la vid y produciendo aceite de oliva, el mas pasó "
                 "a la familia parisina Armand en 1948. Restaurado por primera vez en 1985 "
                 "por Madeleine Castaing en un estilo rico y ornamentado, fue devuelto a su "
                 "sobriedad original en 2017 por la restauración de François Catroux. La "
                 "obra ha sido publicada en Architectural Digest France y en Le Monde "
                 "d'Hermès."),
                ("ol", [
                    "Acceso: camino blanco privado de doscientos metros · portón de hierro original de 1754.",
                    "Parque: seis hectáreas · viñedo AOP de dos y media · olivar secular · alberca natural de piedra.",
                    "Superficie interior: quinientos cincuenta metros cuadrados · cuatro dormitorios · dependencia del guarda.",
                    "Viñedo: Côtes de Provence AOP · vinificación Domaine Ott y Tempier · producción siete mil botellas.",
                    "Instalaciones: calefacción por pellets · climatización suave · agua de manantial privado.",
                    "Precio: a consultar con el interlocutor · acuerdo de confidencialidad requerido antes del dossier completo.",
                ]),
                ("p",
                 "La disponibilidad se abre bajo cita a partir de la próxima temporada de "
                 "visitas — mediados de mayo. El mandato agrícola del viñedo se cede junto "
                 "con la firma inmobiliaria; el traspaso posterior de la denominación AOP se "
                 "coordina con Domaine Ott. El recorrido medio de adquisición es de cuatro "
                 "meses desde el acuerdo de confidencialidad hasta la firma notarial francesa."),
            ],
            "footer_strap": "Villa Prestige · Saint-Tropez · dossier N.º 14 / 18",
        },
        # Four shorter dossiers to round out the collezione list
        {
            "slug":     "villa-lario-tremezzo",
            "kicker":   "Lago di Como · Tremezzo · siglo XIX",
            "title":    "Villa Lario — residencia lacustre de 1862 con darsena privada",
            "lede":
                "Cuatrocientos cincuenta metros cuadrados a nivel del Lago, parque de dos "
                "hectáreas y media, darsena privada para embarcaciones de hasta quince metros.",
            "date":     "15 de marzo de 2026",
            "read_min": "5",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Colección",    "N.º 04 / 18 · primavera 2026"),
                ("Territorio",   "Lago di Como · Tremezzo"),
                ("Superficie",   "450 m² interiores · parque 25.000 m² · darsena privada"),
                ("Procedencia",  "1862 · villa decimonónica · restauración Lissoni 2020"),
                ("Disponibilidad","Bajo cita"),
                ("Precio",       "A consultar con el interlocutor"),
            ],
            "body": [
                ("p",
                 "Villa Lario se alza a nivel del Lago di Como, a cinco minutos de la "
                 "plazoleta de Tremezzo y a diez en lancha de Villa d'Este. La construcción "
                 "original es de 1862, para una familia milanesa de la burguesía industrial "
                 "lombarda. La restauración conservativa de 2020, conducida por el estudio "
                 "Lissoni Casal Ribeiro, ha preservado intactos los ornamentos decimonónicos "
                 "del salón principal, las boiseries originales y la escalera interior en "
                 "mármol de Candoglia."),
                ("h2", "El parque y la darsena · acceso privado al Lago"),
                ("p",
                 "El parque se extiende sobre dos hectáreas y media en pendiente hacia el "
                 "Lago, con jardín a la italiana original de 1875, vivero, pórtico de "
                 "jazmines centenarios. La darsena privada, original de 1870 y restaurada en "
                 "2020, alberga embarcaciones de hasta quince metros de eslora y cuenta con "
                 "grúa eléctrica para la puesta en seco invernal. Una escalera de piedra "
                 "desciende directamente del salón principal al mirador sobre el Lago."),
                ("ol", [
                    "Acceso: carretera estatal · portón privado con portería.",
                    "Parque: dos hectáreas y media · jardín a la italiana · darsena privada.",
                    "Superficie interior: cuatrocientos cincuenta metros cuadrados · cinco dormitorios · biblioteca.",
                    "Precio: a consultar con el interlocutor · acuerdo de confidencialidad requerido antes del dossier.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Lago di Como · dossier N.º 04 / 18",
        },
        {
            "slug":     "casa-delle-torri-porto-cervo",
            "kicker":   "Costa Smeralda · Porto Cervo · años 70",
            "title":    "Casa delle Torri — villa de Jacques Couëlle de 1972",
            "lede":
                "Seiscientos veinte metros cuadrados sobre promontorio privado, diseño "
                "original de Jacques Couëlle, terrazas sobre el mar y acceso directo a una "
                "cala privada.",
            "date":     "8 de marzo de 2026",
            "read_min": "6",
            "author":   "Élodie Charbonneau",
            "image":
                "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Colección",    "N.º 08 / 18 · primavera 2026"),
                ("Territorio",   "Costa Smeralda · Porto Cervo"),
                ("Superficie",   "620 m² interiores · promontorio privado · cala"),
                ("Procedencia",  "1972 · firma Jacques Couëlle · restauración A. Citterio 2018"),
                ("Disponibilidad","Bajo cita"),
                ("Precio",       "A consultar con el interlocutor"),
            ],
            "body": [
                ("p",
                 "Diseñada en 1972 por Jacques Couëlle para una familia belga, Casa delle "
                 "Torri es una de las pocas villas íntegramente supervivientes del diseño "
                 "orgánico esmeraldino. La restauración de 2018, conducida por Antonio "
                 "Citterio, ha preservado la integridad absoluta del envoltorio en granito "
                 "local y de las cubiertas de enebro, introduciendo instalaciones invisibles "
                 "y una cocina contemporánea en la dependencia."),
                ("ol", [
                    "Acceso: camino privado del consorcio · portería de Porto Cervo.",
                    "Terrazas: tres niveles sobre el mar · cala privada accesible a pie.",
                    "Superficie: seiscientos veinte metros cuadrados · seis dormitorios · dependencia del personal.",
                    "Precio: a consultar con el interlocutor.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Costa Smeralda · dossier N.º 08 / 18",
        },
        {
            "slug":     "casa-canapa-capri",
            "kicker":   "Capri · Anacapri · años 30",
            "title":    "Casa Canapa — villa caprese frente a los Faraglioni",
            "lede":
                "Doscientos veinte metros cuadrados en tres niveles, terrazas superpuestas "
                "hacia los Faraglioni, jardín de limoneros centenarios, acceso peatonal desde "
                "el centro de Anacapri.",
            "date":     "1 de marzo de 2026",
            "read_min": "5",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Colección",    "N.º 15 / 18 · primavera 2026"),
                ("Territorio",   "Capri · Anacapri"),
                ("Superficie",   "220 m² interiores · 3 terrazas · jardín 800 m²"),
                ("Procedencia",  "1934 · villa caprese original · tres generaciones misma familia"),
                ("Disponibilidad","Bajo cita"),
                ("Precio",       "A consultar con el interlocutor"),
            ],
            "body": [
                ("p",
                 "Casa Canapa es una villa caprese auténtica de 1934, transmitida durante "
                 "tres generaciones en la misma familia napolitana. El diseño original es de "
                 "tradición caprese — bóvedas, bovedillas, escaleras exteriores en mayólica — "
                 "y no ha sufrido intervenciones de sustancia. El mantenimiento corriente, "
                 "confiado a los artesanos capreses de siempre, ha preservado intacto el "
                 "carácter isleño de la casa."),
                ("ol", [
                    "Acceso: peatonal únicamente · cinco minutos a pie de la plazoleta de Anacapri.",
                    "Terrazas: tres niveles superpuestos · vista sobre los Faraglioni de Capri.",
                    "Superficie: doscientos veinte metros cuadrados · cuatro dormitorios.",
                    "Precio: a consultar con el interlocutor.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Capri · dossier N.º 15 / 18",
        },
        {
            "slug":     "pieve-di-santorso-val-dorcia",
            "kicker":   "Val d'Orcia · Montalcino · siglo XII",
            "title":    "Pieve di Sant'Orso — finca UNESCO con viñedo de Brunello",
            "lede":
                "Ochocientos metros cuadrados entre pieve románica y casa de labor, veintidós "
                "hectáreas patrimonio UNESCO, viñedo de Brunello di Montalcino DOCG en "
                "producción.",
            "date":     "22 de febrero de 2026",
            "read_min": "7",
            "author":   "Francesco Medici di Porrena",
            "image":
                "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Colección",    "N.º 17 / 18 · primavera 2026"),
                ("Territorio",   "Val d'Orcia · Montalcino"),
                ("Superficie",   "800 m² interiores · 22 ha UNESCO · viñedo 4 ha"),
                ("Procedencia",  "Siglo XII · pieve románica · restauración Matteo Nunziati 2019"),
                ("Disponibilidad","Exclusiva"),
                ("Precio",       "A consultar con el interlocutor"),
            ],
            "body": [
                ("p",
                 "La finca de Sant'Orso se extiende sobre veintidós hectáreas de patrimonio "
                 "UNESCO en la Val d'Orcia, entre Montalcino y San Quirico d'Orcia. El "
                 "núcleo histórico comprende la pieve románica de 1182 — aún consagrada, en "
                 "uso una vez al año — y la casa de labor original de 1620, restaurada en "
                 "2019 por Matteo Nunziati. El viñedo de Brunello di Montalcino DOCG ocupa "
                 "cuatro hectáreas, en conducción ecológica certificada, con vinificación "
                 "confiada a la finca vecina."),
                ("ol", [
                    "Acceso: camino comunal blanco de dos kilómetros · protección UNESCO.",
                    "Finca: veintidós hectáreas · viñedo cuatro hectáreas · olivar de ochocientos árboles.",
                    "Superficie interior: ochocientos metros cuadrados · pieve románica · seis dormitorios.",
                    "Precio: a consultar con el interlocutor · exclusiva total.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Val d'Orcia · dossier N.º 17 / 18",
        },
    ],
}


# D-047 · all chrome labels flow from site/page_data above — no string
# should ever be hardcoded in the skin or preview composition HTML.
