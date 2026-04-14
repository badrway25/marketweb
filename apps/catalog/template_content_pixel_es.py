"""Pixel — Portfolio Fotografico · Spanish (peninsular) content tree.

Mirrors the shape of ``PIXEL_CONTENT_IT`` exactly — same keys, nesting and
list shapes. Authored Session 39 for the Pixel live i18n rollout of the
cinematic-photographer archetype. Blank Paper / EPS long-form reportage register.
"""
from __future__ import annotations

from typing import Any


PIXEL_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Índice",         "kind": "home"},
        {"slug": "serie",         "label": "Series",         "kind": "series_list"},
        {"slug": "biografia",     "label": "Biografía",      "kind": "about"},
        {"slug": "pubblicazioni", "label": "Publicaciones",  "kind": "publications"},
        {"slug": "contatti",      "label": "Contacto",       "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial":   "P",
        "logo_word":      "Pixel — Lorenzo Bianchi",
        "logo_short":     "PXL",
        "tag":            "Fotógrafo de autor · Milán · Trieste",
        "phone":          "+39 348 211 7720",
        "email":          "studio@lorenzobianchi.photo",
        "address":        "Via Tadino 18 · 20124 Milán",
        "hours_compact":  "Disponible para encargos · 2026 — 27",
        "license":        "Inscripción Tau · Colegio de Fotógrafos Profesionales n.º 4421/2014",
        "footer_intro":
            "Fotógrafo de autor independiente. Reportaje de largo "
            "aliento, retrato editorial y encargos de marca para "
            "editoriales, galerías y maisons de moda. Representado "
            "por la Galleria Carla Sozzani para la copia fine art.",
        # Primary nav bracket CTA (right-side) — lifted Session 39 per D-047
        "nav_cta":       "Abrir conversación",
        "foot_studio":   "El estudio",
        "foot_pages":    "Índice",
        "foot_contact":  "Contacto",
        "foot_kit":      "Equipamiento",
        # EXIF-style footer cells
        "exif_footer": [
            ("Sede",           "Milán · Trieste"),
            ("Disponible",     "Encargos 2026 — 27"),
            ("Representación", "Galleria Carla Sozzani · Milán"),
            ("Copia",          "Atelier Druckwerkstatt · Berlín"),
        ],
        # Footer kit column rows (per-tenant — never inline in skin per D-047)
        "kit_footer_rows": [
            "Mamiya 7II · Sony α7R V",
            "Kodak Portra 400",
            "Copia · Druckwerkstatt Berlín",
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        # Series counter chip (top-left of hero)
        "series_counter_label": "Serie actual",
        "series_counter_value": "07 / 24",

        # Status pulse on nav (right side)
        "status_pulse": "Disponible · 2026 — 27",

        # Eyebrow + headline
        "eyebrow":   "Fotografía de autor · 2014 — 2026",
        # All-caps cinematic hero per archetype
        "headline":  "OBSERVAR LO QUE PERMANECE <em>cuando la luz cambia</em>",
        "subhead":
            "Reportaje de largo aliento, retrato editorial y "
            "encargos de marca. Trabajo en película de medio formato "
            "y en digital de doble sensor — para proyectos que "
            "requieren diez días o tres años de tiempo.",
        "primary_cta":   "Abrir la serie completa",
        "primary_href":  "serie",
        "secondary_cta": "Disponibilidad 2026",
        "secondary_href":"contatti",

        # Hero image — fullbleed dominant
        "hero_image":
            "https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?w=2000&q=85&auto=format&fit=crop",
        "hero_image_alt":
            "Vista desde el puerto de Trieste a las 6:14 de la mañana · "
            "noviembre de 2025 · película Kodak Portra 400",

        # EXIF credit cells under hero (4-cell mono bar)
        "hero_credit_cells": [
            ("Cámara",   "Mamiya 7II"),
            ("Película", "Kodak Portra 400"),
            ("Lugar",    "Porto Vecchio · Trieste"),
            ("Fecha",    "Noviembre de 2025"),
        ],

        # Featured series (filmstrip on home — 4 series)
        "filmstrip_label":   "Trabajo reciente",
        "filmstrip_heading": "CUATRO SERIES · 2024 — 2026",
        "filmstrip_intro":
            "Cuatro trabajos de largo recorrido cerrados en los últimos dos años. "
            "Las series completas se consultan en la sección Series — "
            "cada serie reúne entre veinte y cuarenta fotografías.",
        # Each: (num, title, discipline, year, slug-for-link)
        "filmstrip": [
            ("07", "Porto Vecchio · Trieste",
             "Reportaje de largo aliento", "2024 — 2026",
             "porto-vecchio-trieste"),
            ("06", "Atelier Velluti & Co.",
             "Encargo editorial", "2025",
             "atelier-velluti"),
            ("05", "Las casas de piedra",
             "Reportaje arquitectónico", "2023 — 2024",
             "case-di-pietra-puglia"),
            ("04", "Retratos del Po",
             "Retrato de autor", "2023",
             "ritratti-del-po"),
        ],

        # Reel — REMOVED per D-068 (Session 36).
        # A short-film claim without a real signed MP4 shipped as a placeholder
        # contradicts the cinematic-photographer identity; the "Play · 3:12" +
        # "Reel · 1080p · 24 fps" meta also trespassed into codec-theatre.
        # Lorenzo's identity is stills — the filmstrip + EXIF cells + series
        # index already carry the cinematic voice. When a genuine Carso reel
        # exists, this block can return with a real `src` and meta pruned of
        # pseudo-technical cues.

        # About excerpt — 3 sentences (full bio on /biografia)
        "about_label":   "Notas autobiográficas",
        "about_heading": "LORENZO BIANCHI",
        "about_excerpt":
            "Nacido en Trieste en 1986, vivo entre Milán y el Carso "
            "triestino. Empecé fotografiando los mercados de Sarajevo "
            "en 2009 y desde entonces no he cambiado de disciplina — "
            "solo de tiempos, de luz y de formato. Trabajo en película "
            "Kodak Portra 400 de medio formato para el trabajo personal, "
            "y en digital Sony de doble sensor para los encargos.",
        "about_cta":     "Leer la biografía",
        "about_cta_href":"biografia",

        # Recent publications strip (3 selected)
        "publications_label":   "Publicado recientemente",
        "publications_heading": "PRENSA & EDITORIAL · 2025",
        "publications": [
            ("FOAM Magazine n.º 64",
             "Portfolio de ocho páginas sobre la serie «Porto Vecchio»",
             "Noviembre de 2025"),
            ("Internazionale n.º 1612",
             "Reportaje ilustrado sobre las casas de piedra del Salento",
             "Septiembre de 2025"),
            ("Domus n.º 1102",
             "Encargo editorial para el número monográfico Carlo Scarpa",
             "Abril de 2025"),
        ],

        # Final CTA band — commission inquiry
        "cta_label":   "Encargos · disponibilidad 2026 — 2027",
        "cta_heading": "[ ABRIR UNA CONVERSACIÓN ]",
        "cta_intro":
            "Estoy disponible para encargos editoriales, retrato de "
            "autor y proyectos de larga duración hasta septiembre "
            "de 2027. Los encargos de marca se valoran caso por "
            "caso — prefiero los mandatos con tiempo largo.",
        "cta_primary":      "Escribir una propuesta",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Consultar la representación",
        "cta_secondary_href":"biografia",
    },

    # ─── SERIE (series_list) ────────────────────────────────────
    "serie": {
        "series_counter_label": "Archivo",
        "series_counter_value": "24 SERIES",
        "status_pulse":         "Disponible · 2026 — 27",

        "eyebrow":   "Archivo de series · 2009 — 2026",
        "headline":  "VEINTICUATRO SERIES, <em>una sola disciplina</em>",
        "subhead":
            "El archivo completo de las series firmadas. Reportaje de "
            "largo aliento, retrato de autor, encargos editoriales. "
            "La selección mostrada cubre los trabajos más recientes — "
            "las series históricas (2009 — 2018) están disponibles "
            "bajo petición para estudio o publicación.",

        # Discipline filter pills
        "filter_label": "Disciplinas",
        "filters": [
            "Todas",
            "Reportaje de largo aliento",
            "Retrato de autor",
            "Encargo editorial",
            "Reportaje arquitectónico",
        ],

        # Index intro band
        "index_label": "Selección 2018 — 2026",
        "index_intro":
            "Pulse la portada para abrir la serie completa. "
            "Cada serie reúne entre veinte y cuarenta fotografías, "
            "con aparato crítico y EXIF de captura.",

        # CTA before footer
        "cta_label":   "¿Busca algo concreto?",
        "cta_heading": "[ ARCHIVO RESERVADO · PRENSA & ESTUDIO ]",
        "cta_intro":
            "Para acceder al archivo histórico (2009 — 2018), para "
            "solicitudes de copia fine art o para encargar un nuevo "
            "trabajo: abra una conversación preliminar.",
        "cta_primary":      "Escribir al fotógrafo",
        "cta_primary_href": "contatti",

        # Chrome labels shared by serie card + series_detail page.
        # Lifted Session 39 (D-047 lift) — same labels across every post,
        # so they live on the parent serie block rather than on each post.
        "card_arrow_label":        "abrir serie",
        "post_discipline_label":   "Disciplina",
        "post_period_label":       "Duración",
        "post_location_label":     "Lugar",
        "post_frames_label":       "Fotografías",
        "post_gallery_label":      "Galería",
        "post_edition_label":      "Edición",
    },

    # ─── BIOGRAFIA (about) ──────────────────────────────────────
    "biografia": {
        "series_counter_label": "Notas autobiográficas",
        "series_counter_value": "1986 — 2026",
        "status_pulse":         "Sede · Milán + Trieste",

        "eyebrow":   "Notas autobiográficas · 1986 — 2026",
        "headline":  "LORENZO BIANCHI <em>fotógrafo de autor</em>",
        "subhead":
            "Nacido en Trieste en 1986, vivo entre Milán y el Carso "
            "triestino. Empecé fotografiando los mercados de Sarajevo "
            "en 2009 — un ensayo para Granta que nunca llegó a ver la luz. "
            "Desde entonces no he cambiado de disciplina, solo de "
            "tiempos, de luz y de formato.",

        # Bio statement — 5 paragraphs
        "statement_label":   "Statement",
        "statement_heading": "POR QUÉ FOTOGRAFÍO",
        "statement_paragraphs": [
            "Fotografío para quedarme mucho tiempo en un lugar. La "
            "fotografía es la única disciplina que me obliga a volver. "
            "Una serie, para mí, son diez o veinte viajes a meses de "
            "distancia al mismo punto exacto, hasta que algo cambia lo "
            "suficiente como para merecer una toma.",
            "Trabajo en película de medio formato — Mamiya 7II, dos "
            "objetivos, Kodak Portra 400. La ralentización mecánica es "
            "la disciplina, no un capricho. Revelo y copio yo mismo, "
            "en una cocina transformada en cuarto oscuro para las "
            "tiradas cortas, y en Druckwerkstatt Berlín para el fine art.",
            "Para los encargos editoriales uso un sistema digital "
            "Sony Alpha de doble sensor — la velocidad de entrega que "
            "requiere una redacción no se concilia con el tiempo "
            "de la película. Pero la manera de mirar sigue siendo la misma, "
            "el digital es solo otro soporte.",
            "Estoy representado desde 2018 por la Galleria Carla Sozzani "
            "de Milán para la copia fine art y el mercado secundario. "
            "Para los encargos editoriales y de marca trabajo "
            "directamente, sin agente — un agente significa un "
            "filtro entre el fotógrafo y el comitente, y pierdo las "
            "conversaciones que más me interesan.",
            "Enseño fotografía documental en el CFP Bauer de Milán "
            "desde 2019 — un día a la semana, a los alumnos del "
            "segundo curso. Es el único compromiso fijo del calendario "
            "del estudio. Todo lo demás se elige proyecto a proyecto.",
        ],

        # Camera kit — what we shoot with.
        # Availability label + value lifted Session 39 (D-047).
        "kit_label":                "Equipamiento de trabajo",
        "kit_heading":              "CUATRO SISTEMAS, UNA SOLA ELECCIÓN POR PROYECTO",
        "kit_availability_label":   "Disponible",
        "kit_availability_value":   "Bajo encargo",
        "kit": [
            ("01", "Mamiya 7II",
             "Telemétrica de medio formato 6 × 7 cm, dos objetivos (80 mm y 43 mm). "
             "Para los trabajos personales en película — reportaje de largo aliento "
             "y retrato de autor.",
             "Película de estudio", "Kodak Portra 400 + Tri-X 400"),
            ("02", "Sony α7R V + α7S III",
             "Doble sensor (alta resolución + sensibilidad). "
             "Para los encargos editoriales y los trabajos que requieren "
             "entrega en menos de 72 horas.",
             "Objetivos", "GM 24/35/85 + Voigtländer 50/1.5"),
            ("03", "Linhof Master Technika 4 × 5",
             "Cámara de banco óptico para copia fine art y retrato de estudio. "
             "Reservada a ocho o diez tomas al año para la galería.",
             "Placa", "Ilford FP4+ · Foma Retropan 320"),
            ("04", "Cuarto oscuro · cocina de Milán",
             "Revelado y copia para las tiradas cortas (hasta 18 × 24 cm). "
             "Las tiradas fine art se copian en Druckwerkstatt Berlín "
             "en colaboración con Anna Wedekind.",
             "Papel de estudio", "Ilford Multigrade FB Classic"),
        ],

        # Exhibitions + publications timeline (selected — full list /pubblicazioni)
        "timeline_label":   "Exposiciones & publicaciones · selección",
        "timeline_heading": "DOCE ETAPAS, QUINCE AÑOS",
        "timeline": [
            ("2026", "FOAM Talent Lounge · Ámsterdam",
             "Exposición colectiva · serie «Porto Vecchio»"),
            ("2025", "FOAM Magazine n.º 64",
             "Portfolio de ocho páginas sobre la serie «Porto Vecchio»"),
            ("2024", "Triennale Milano · «Geografía de una tierra»",
             "Exposición individual · serie «Las casas de piedra»"),
            ("2024", "World Press Photo Story of the Year · Finalist",
             "Categoría long-term projects, serie «Las casas de piedra»"),
            ("2023", "Internazionale Festival Ferrara",
             "Exposición colectiva · serie «Retratos del Po»"),
            ("2022", "Photo London · booth de Galleria Carla Sozzani",
             "Copias fine art · selección 2018 — 2022"),
            ("2021", "Magnum Foundation Grant · finalista",
             "Categoría emerging photographer"),
            ("2020", "MAXXI Roma · «Diarios del confinamiento»",
             "Exposición colectiva · contribución personal de 12 copias"),
            ("2019", "GUP Magazine n.º 60 · portada",
             "Ensayo ilustrado sobre el archivo de los mercados de Sarajevo"),
            ("2018", "FOAM Talent · Ámsterdam · selección",
             "Serie «Los trenes nocturnos»"),
            ("2016", "Premio Marco Pesaresi · finalista",
             "Reportaje italiano · «El paso»"),
            ("2009", "Granta Magazine · ensayo por encargo (inédito)",
             "Los mercados de Sarajevo · debut profesional"),
        ],

        # Final CTA — commissions
        "cta_heading":      "[ ENCARGOS 2026 — 2027 ]",
        "cta_intro":
            "El estudio acepta seis u ocho encargos al año, elegidos por "
            "tiempo disponible y por coherencia con la disciplina. "
            "Las propuestas editoriales y de marca se valoran caso por "
            "caso — prefiero los mandatos con tiempo largo.",
        "cta_primary":      "Abrir una conversación",
        "cta_primary_href": "contatti",
    },

    # ─── PUBBLICAZIONI (publications) ───────────────────────────
    "pubblicazioni": {
        "series_counter_label": "Archivo de prensa",
        "series_counter_value": "47 PUBLICACIONES",
        "status_pulse":         "Actualizado · enero de 2026",

        "eyebrow":   "Publicaciones & exposiciones · 2009 — 2026",
        "headline":  "CUARENTA Y SIETE PUBLICACIONES, <em>quince años</em>",
        "subhead":
            "El archivo completo de las publicaciones impresas, exposiciones "
            "individuales y colectivas, premios y residencias. La lista está "
            "actualizada a enero de 2026 — están previstas más salidas "
            "a lo largo del año.",

        # Press band — magazine + book covers
        "press_label":   "Prensa & editorial · principales apariciones",
        "press_heading": "REVISTAS & MONOGRAFÍAS",
        "press": [
            {
                "year":    "2025",
                "outlet":  "FOAM Magazine n.º 64",
                "type":    "Portfolio editorial",
                "subject": "Serie «Porto Vecchio · Trieste»",
                "format":  "8 páginas · impresión offset · Ámsterdam",
            },
            {
                "year":    "2025",
                "outlet":  "Internazionale n.º 1612",
                "type":    "Reportaje ilustrado",
                "subject": "Serie «Las casas de piedra · Salento»",
                "format":  "12 páginas · huecograbado · Roma",
            },
            {
                "year":    "2025",
                "outlet":  "Domus n.º 1102",
                "type":    "Encargo editorial",
                "subject": "Número monográfico Carlo Scarpa",
                "format":  "16 páginas · impresión offset · Milán",
            },
            {
                "year":    "2024",
                "outlet":  "Las casas de piedra (monografía)",
                "type":    "Volumen monográfico",
                "subject": "Reportaje arquitectónico Salento 2023 — 24",
                "format":  "Editorial Quodlibet · 168 pp. · 24 × 28 cm",
            },
            {
                "year":    "2024",
                "outlet":  "GUP Magazine n.º 73",
                "type":    "Ensayo crítico",
                "subject": "Conversación con Sarah Kelly sobre tiempos largos",
                "format":  "10 páginas · impresión offset · Ámsterdam",
            },
            {
                "year":    "2023",
                "outlet":  "Vogue Italia · sección Photography",
                "type":    "Retrato editorial",
                "subject": "Retratos del Po · serie seleccionada",
                "format":  "6 páginas · impresión offset · Milán",
            },
            {
                "year":    "2022",
                "outlet":  "Aperture n.º 248",
                "type":    "Ensayo ilustrado",
                "subject": "Reflexión sobre la película en tiempo digital",
                "format":  "8 páginas · impresión offset · Nueva York",
            },
            {
                "year":    "2019",
                "outlet":  "GUP Magazine n.º 60 · portada",
                "type":    "Portada + ensayo ilustrado",
                "subject": "Archivo de los mercados de Sarajevo 2009",
                "format":  "Portada + 14 pp. · impresión offset · Ámsterdam",
            },
        ],

        # Exhibitions
        "exhibitions_label":   "Exposiciones · individuales y colectivas",
        "exhibitions_heading": "DOCE EXPOSICIONES, QUINCE AÑOS",
        "exhibitions": [
            ("2026", "FOAM Talent Lounge · Ámsterdam",
             "Colectiva · 18 fotógrafos internacionales",
             "Marzo — mayo de 2026"),
            ("2024", "Triennale Milano · «Geografía de una tierra»",
             "Individual · serie «Las casas de piedra» · 38 copias",
             "Septiembre — diciembre de 2024"),
            ("2023", "Internazionale Festival Ferrara",
             "Colectiva · sección long-term projects",
             "Octubre de 2023"),
            ("2022", "Photo London · booth de Galleria Carla Sozzani",
             "Mercado fine art · 14 copias en venta",
             "Mayo de 2022"),
            ("2020", "MAXXI Roma · «Diarios del confinamiento»",
             "Colectiva · 12 copias de la contribución personal",
             "Septiembre — noviembre de 2020"),
            ("2018", "FOAM Talent · Ámsterdam · serie seleccionada",
             "Colectiva · serie «Los trenes nocturnos» · 16 copias",
             "Abril — junio de 2018"),
        ],

        # Awards & residencies
        "awards_label":   "Premios & residencias",
        "awards_heading": "RECONOCIMIENTOS",
        "awards": [
            ("2024", "World Press Photo · Finalist · long-term projects",
             "Serie «Las casas de piedra»"),
            ("2023", "Magnum Foundation · Photography & Social Justice · selección",
             "Programa de mentoría · 6 meses en Nueva York"),
            ("2021", "Magnum Foundation Grant · finalista emerging",
             "Beca de estudio para trabajo personal"),
            ("2020", "Premio Voglino · finalista",
             "Categoría reportaje italiano"),
            ("2016", "Premio Marco Pesaresi · finalista",
             "Reportaje italiano · «El paso»"),
            ("2014", "Premio Angelo Frontoni · selección",
             "Categoría fotografía documental"),
        ],

        # Final CTA — speaking + workshops
        "cta_heading":      "[ CHARLAS · TALLERES · CONFERENCIAS ]",
        "cta_intro":
            "Para peticiones de intervención académica (festivales, escuelas, "
            "universidades), talleres sobre película de medio formato o "
            "conferencias editoriales: abra una conversación. La "
            "disponibilidad se calenda con al menos tres meses de antelación.",
        "cta_primary":      "Abrir una conversación",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI (contact) ─────────────────────────────────────
    "contatti": {
        "series_counter_label": "Disponibilidad",
        "series_counter_value": "2026 — 27",
        "status_pulse":         "Abierto a encargos",

        "eyebrow":   "Conversación preliminar · sin intermediarios",
        "headline":  "[ ABRIR UNA CONVERSACIÓN ] <em>directamente</em>",
        "subhead":
            "Los encargos se tratan directamente con el fotógrafo, "
            "sin agente. Para las propuestas editoriales, de marca o "
            "para la copia fine art (representación Galleria Carla "
            "Sozzani · Milán): escriba una propuesta. Respondo en un "
            "plazo de setenta y dos horas laborables.",

        # Studio info side card (dark style)
        "studio_label":   "Estudio operativo",
        "studio_address": "Via Tadino 18 · 20124 Milán",
        "studio_area":    "Porta Venezia · entrada lateral · timbre «Bianchi»",
        "studio_metro":   "MM1 / MM3 Loreto · 4 minutos a pie",
        "studio_hours":   "Disponible con cita previa · nunca por sorpresa",
        "studio_row_address_label":  "Dirección",
        "studio_row_entrance_label": "Entrada",
        "studio_row_metro_label":    "Metro",
        "studio_row_hours_label":    "Disponible",

        # Form fields
        "form_label":   "Propuesta de encargo",
        "form_heading": "[ RELLENAR LA PROPUESTA ]",
        "form_intro":
            "Una propuesta de encargo es una descripción estructurada "
            "del proyecto fotográfico. No es un brief de marketing — "
            "es una conversación preliminar para comprender si la disciplina "
            "del trabajo se corresponde con la mía.",
        "form_fields": [
            {"name": "name",      "label": "Nombre",          "type": "text",     "required": True,  "placeholder": "Ej. Lorenzo",
             "helper": "Solo el nombre, gracias."},
            {"name": "surname",   "label": "Apellidos",       "type": "text",     "required": True,  "placeholder": "Ej. Bianchi",
             "helper": "Tal y como aparece en la firma."},
            {"name": "organization", "label": "Organización", "type": "text",     "required": False, "placeholder": "Ej. FOAM Magazine",
             "helper": "Si el encargo es editorial o de marca."},
            {"name": "email",     "label": "Correo electrónico", "type": "email", "required": True,  "placeholder": "lorenzo@foam.org",
             "helper": "Correo directo · respuesta en 72 horas laborables."},
            {"name": "phone",     "label": "Teléfono",        "type": "tel",      "required": False, "placeholder": "+34 ...",
             "helper": "Solo si prefiere que le llamemos."},
            {"name": "discipline", "label": "Disciplina del encargo", "type": "select", "required": True,
             "options": [
                 "Por definir en conversación",
                 "Reportaje de largo aliento",
                 "Retrato editorial",
                 "Encargo de marca",
                 "Reportaje arquitectónico",
                 "Copia fine art (Galleria Sozzani)",
                 "Taller / conferencia",
             ],
             "helper": "Elija «por definir» si el perímetro aún no está claro."},
            {"name": "timeline",  "label": "Plazo de ejecución", "type": "select", "required": True,
             "options": [
                 "En el plazo de un mes (entrega rápida)",
                 "Tres — seis meses (encargo editorial)",
                 "Seis — dieciocho meses (trabajo de largo aliento)",
                 "Exploratorio · sin fecha de entrega",
             ],
             "helper": "Los plazos de entrega determinan el formato (digital vs película)."},
            {"name": "location",  "label": "Lugar de captura", "type": "text", "required": False,
             "placeholder": "Ej. Salento · Trieste · Sarajevo",
             "helper": "Indicar ciudad / región / país · sirve para estimar los viajes."},
            {"name": "story",     "label": "La historia que le gustaría contar", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Máximo 1000 caracteres. Una descripción del sujeto, de las razones "
                            "del proyecto y de la publicación prevista. Nada de brief de marketing "
                            "— aquí interesa el contenido, no el deliverable.",
             "helper": "Si no sabe por dónde empezar, escriba qué le ha llamado la atención."},
        ],

        "form_sections": [
            {"num": "01", "title": "Persona de contacto",
             "meta": "La persona que seguirá el encargo desde el lado del comitente.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Publicación",
             "meta": "Para comprender el contexto editorial o de marca.",
             "fields": ["organization"]},
            {"num": "03", "title": "Perímetro del encargo",
             "meta": "Los plazos de entrega determinan el formato de captura — película vs digital.",
             "fields": ["discipline", "timeline", "location", "story"]},
            {"num": "04", "title": "Referencias (opcional)",
             "meta": "Brief editorial, plan de número, imágenes de referencia. Pueden adelantar la conversación.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "brief_allegato",
            "label":    "Referencias preliminares",
            "helper":   "Brief editorial, plan de número, imágenes de referencia. "
                        "PDF / DOCX / JPG / PNG · máx. 25 MB en total.",
            "accept":   ".pdf,.docx,.jpg,.jpeg,.png",
            "multiple": True,
            "primary":  "Arrastre aquí los documentos o",
            "link":     "examine el archivo",
            "meta":     "PDF / DOCX / JPG · máx. 25 MB",
        },

        "form_submit_label": "[ ENVIAR LA PROPUESTA ]",
        "form_submit_note":
            "Respuesta directamente del fotógrafo en un plazo de 72 horas laborables. "
            "Ningún agente, ninguna automatización de leads.",
        "form_consent":
            "Consiento el tratamiento de mis datos personales conforme al "
            "Reglamento UE 679/2016. Las solicitudes de encargo son "
            "leídas y archivadas únicamente por el fotógrafo. Para la copia "
            "fine art (mercado secundario) la representación corresponde "
            "a la Galleria Carla Sozzani.",

        # Sidebar — channels (EXIF style)
        "channels_label": "Canales directos",
        "channels": [
            ("Estudio",         "studio@lorenzobianchi.photo",      "Respuesta en 72 horas"),
            ("Móvil",           "+39 348 211 7720",                 "Lun – Vie · 10:00 – 19:00"),
            ("Copia fine art",  "Galleria Carla Sozzani · Milán",   "Corso Como 10 · +39 02 6555 2223"),
            ("Docencia",        "CFP Bauer · Milán",                "Documental · 2.º curso · jueves"),
        ],

        "footnote":
            "Para la copia fine art — venta en el mercado secundario, "
            "ediciones limitadas, exposiciones de galería — la representación "
            "exclusiva corresponde a la Galleria Carla Sozzani de Milán desde 2018. "
            "Las peticiones comerciales de copia deben dirigirse "
            "directamente a la galería.",
    },

    # ─── POSTS — drives /serie/<slug>/ series_detail ────────────
    "posts": [
        {
            "slug":        "porto-vecchio-trieste",
            "title":       "Porto Vecchio · Trieste",
            "category":    "Reportaje de largo aliento",
            "discipline":  "Reportaje de largo aliento",
            "year":        "2024 — 2026",
            "duration":    "24 meses · 18 viajes",
            "location":    "Porto Vecchio · Trieste · Italia",
            "frame_count": "47 fotografías",
            "edition":     "Edición limitada · 12 + 2 AP por copia",
            "print_meta": [
                ("Tirada",         "12 + 2 AP por fotografía"),
                ("Copia",          "Druckwerkstatt Berlín"),
                ("Papel",          "Hahnemühle Photo Rag Baryta 315 g/m²"),
                ("Representación", "Galleria Carla Sozzani · Milán"),
            ],
            "lead":
                "Veinticuatro meses en el puerto en vías de desuso de "
                "Trieste — una zona de sesenta y seis hectáreas entre el "
                "mar Adriático y la ciudad, en transición entre la "
                "arqueología industrial habsbúrgica y un futuro urbanístico "
                "aún por decidir. Cuarenta y siete fotografías en película "
                "Kodak Portra 400 de medio formato.",
            "cover_image":
                "https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Cámara",     "Mamiya 7II · 80 mm + 43 mm"),
                ("Película",   "Kodak Portra 400 medio formato"),
                ("Periodo",    "Noviembre de 2024 — enero de 2026"),
                ("Copia",      "Druckwerkstatt Berlín · 30 × 40 cm"),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=1600&q=85&auto=format&fit=crop",
                 "Frame 03",
                 "Porto Vecchio al amanecer · Bacino San Marco · noviembre de 2024"),
                ("https://images.unsplash.com/photo-1505820013142-f86a3439c5b2?w=1600&q=85&auto=format&fit=crop",
                 "Frame 11",
                 "Almacenes abandonados · febrero de 2025 · 6:14 de la mañana"),
                ("https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1600&q=85&auto=format&fit=crop",
                 "Frame 18",
                 "Vista desde el hidroescalo · primavera de 2025"),
                ("https://images.unsplash.com/photo-1499346030926-9a72daac6c63?w=1600&q=85&auto=format&fit=crop",
                 "Frame 24",
                 "Astillero en desuso · verano de 2025"),
                ("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1600&q=85&auto=format&fit=crop",
                 "Frame 31",
                 "Línea de agua · octubre de 2025 · luz rasante"),
                ("https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=1600&q=85&auto=format&fit=crop",
                 "Frame 39",
                 "Vista final · enero de 2026 · último viaje"),
            ],
            "sections": [
                {
                    "label": "La serie",
                    "heading": "Sesenta y seis hectáreas, veinticuatro meses",
                    "body":
                        "El Porto Vecchio de Trieste es una zona de "
                        "sesenta y seis hectáreas sobre el mar Adriático, "
                        "en desuso desde 1991 y a la espera de un plan "
                        "urbanístico definitivo. La serie sigue su "
                        "estado suspendido entre noviembre de 2024 y "
                        "enero de 2026 — dieciocho viajes, tres estaciones "
                        "completas, una sola luz de primera hora de la mañana. "
                        "El trabajo se publicó en FOAM Magazine n.º 64 "
                        "(noviembre de 2025) y está en exposición en el "
                        "FOAM Talent Lounge de Ámsterdam desde marzo de 2026.",
                },
                {
                    "label": "El método",
                    "heading": "Película, amanecer, retorno",
                    "body":
                        "Fotografié siempre con Mamiya 7II y película "
                        "Kodak Portra 400 de medio formato — dos objetivos, "
                        "ochenta y cuarenta y tres milímetros. El trabajo "
                        "entero se hizo entre las 5:30 y las 7:00 de la "
                        "mañana, antes de la llegada del personal de "
                        "vigilancia. La luz de Trieste en esa franja "
                        "horaria es particular — la bora nocturna limpia "
                        "el aire, el agua de la dársena es un espejo, el sol "
                        "aún no ha salido sobre el Carso.",
                },
                {
                    "label": "La edición",
                    "heading": "Copia fine art · doce ejemplares",
                    "body":
                        "La edición fine art comprende doce copias "
                        "+ dos artist proof por cada fotografía, "
                        "copiadas en papel Hahnemühle Photo Rag Baryta "
                        "315 g/m² en Druckwerkstatt Berlín en "
                        "colaboración con Anna Wedekind. El formato "
                        "de copia es 30 × 40 cm. La distribución "
                        "fine art es exclusiva de la Galleria Carla "
                        "Sozzani de Milán.",
                },
            ],
            "next_label": "Serie siguiente",
        },
        {
            "slug":        "case-di-pietra-puglia",
            "title":       "Las casas de piedra · Salento",
            "category":    "Reportaje arquitectónico",
            "discipline":  "Reportaje arquitectónico",
            "year":        "2023 — 2024",
            "duration":    "16 meses · 9 viajes",
            "location":    "Salento · Apulia · Italia",
            "frame_count": "62 fotografías",
            "edition":     "Edición monográfica · Quodlibet · 168 pp.",
            "print_meta": [
                ("Tirada",         "1.500 ejemplares · primera reedición agotada"),
                ("Copia",          "Quodlibet · Macerata"),
                ("Papel",          "Munken Pure 130 g/m² · uncoated"),
                ("Representación", "Galleria Carla Sozzani · Milán"),
            ],
            "lead":
                "Dieciséis meses en las masserie de piedra en seco del "
                "Salento meridional — cuarenta edificios, ningún "
                "añadido contemporáneo. Reportaje arquitectónico "
                "documental, publicado en monografía por Quodlibet "
                "(noviembre de 2024) e Internazionale n.º 1612 (septiembre de 2025).",
            "cover_image":
                "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Cámara",    "Mamiya 7II + Sony α7R V"),
                ("Película",  "Kodak Portra 400 + digital doble"),
                ("Periodo",   "Marzo de 2023 — julio de 2024"),
                ("Copia",     "Volumen Quodlibet · 24 × 28 cm · 168 pp."),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1543248939-4296e1fea89b?w=1600&q=85&auto=format&fit=crop",
                 "Frame 04",
                 "Masseria San Giovanni · Otranto · primavera de 2023"),
                ("https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?w=1600&q=85&auto=format&fit=crop",
                 "Frame 12",
                 "Trullo dei Cento Giganti · Locorotondo · verano de 2023"),
                ("https://images.unsplash.com/photo-1512100356356-de1b84283e18?w=1600&q=85&auto=format&fit=crop",
                 "Frame 22",
                 "Masseria Pulicchia · Galatina · otoño de 2023"),
                ("https://images.unsplash.com/photo-1518131672697-613becd4fab5?w=1600&q=85&auto=format&fit=crop",
                 "Frame 31",
                 "Lamia interior · Sannicola · enero de 2024"),
                ("https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600&q=85&auto=format&fit=crop",
                 "Frame 41",
                 "Vista del muro en seco · Specchia · marzo de 2024"),
                ("https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=1600&q=85&auto=format&fit=crop",
                 "Frame 53",
                 "Patio interior · Tricase · julio de 2024"),
            ],
            "sections": [
                {
                    "label": "La serie",
                    "heading": "Cuarenta edificios, dieciséis meses",
                    "body":
                        "El reportaje documenta cuarenta edificios de "
                        "piedra en seco del Salento meridional — "
                        "masserie, lamie, trulli menores, pajare. "
                        "La idea era documentarlos antes de una "
                        "eventual restauración o demolición, en "
                        "colaboración con el Centro Studi Salentini "
                        "de Lecce. Dieciséis meses de trabajo, nueve "
                        "viajes, sesenta y dos fotografías seleccionadas.",
                },
                {
                    "label": "El método",
                    "heading": "Doble formato para la documentación",
                    "body":
                        "A diferencia de los trabajos personales, aquí "
                        "trabajé en doble formato — Mamiya 7II para los "
                        "exteriores en película y Sony α7R V para los "
                        "interiores en digital (para la documentación "
                        "arquitectónica precisa). Los dos formatos "
                        "conviven en el volumen Quodlibet sin "
                        "distinción editorial evidente — la película "
                        "y el digital, trabajados en la copia, "
                        "se vuelven indistinguibles a 24 × 28 cm.",
                },
                {
                    "label": "El volumen",
                    "heading": "Ciento sesenta y ocho páginas, Quodlibet",
                    "body":
                        "El volumen monográfico «Las casas de piedra» "
                        "fue publicado por Quodlibet (noviembre de 2024) "
                        "con ensayo crítico de Salvatore Settis. Ciento sesenta "
                        "y ocho páginas, formato 24 × 28 cm, rústica cosida, "
                        "papel uncoated Munken Pure 130 g/m². Tirada "
                        "de 1.500 ejemplares, primera reedición agotada en tres meses. "
                        "Selección finalista del World Press Photo 2024 "
                        "en la categoría long-term projects.",
                },
            ],
            "next_label": "Serie siguiente",
        },
        {
            "slug":        "ritratti-del-po",
            "title":       "Retratos del Po",
            "category":    "Retrato de autor",
            "discipline":  "Retrato de autor",
            "year":        "2023",
            "duration":    "8 meses · 7 viajes",
            "location":    "Delta del Po · Véneto · Italia",
            "frame_count": "28 fotografías",
            "edition":     "Publicado · Vogue Italia photography",
            "print_meta": [
                ("Tirada",         "8 + 2 AP por copia seleccionada"),
                ("Copia",          "Tiradas personales · cocina de Milán"),
                ("Papel",          "Ilford Multigrade FB Classic"),
                ("Representación", "Galleria Carla Sozzani · Milán"),
            ],
            "lead":
                "Veintiocho retratos de pescadores, marisqueras y "
                "barqueros del Delta del Po véneto. "
                "Ocho meses de trabajo entre la primavera y el otoño de 2023, "
                "publicado en la sección Photography de Vogue Italia "
                "(diciembre de 2023) y expuesto en el Festival Internazionale "
                "de Ferrara (octubre de 2023).",
            "cover_image":
                "https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Cámara",    "Mamiya 7II · 80 mm"),
                ("Película",  "Kodak Portra 400 medio formato"),
                ("Periodo",   "Abril — noviembre de 2023"),
                ("Copia",     "Tiradas personales · cocina de Milán"),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=1600&q=85&auto=format&fit=crop",
                 "Frame 01",
                 "Aldo · pescador · Pila · mayo de 2023"),
                ("https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=1600&q=85&auto=format&fit=crop",
                 "Frame 06",
                 "Maria · marisquera · Goro · junio de 2023"),
                ("https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=1600&q=85&auto=format&fit=crop",
                 "Frame 12",
                 "Carlo y Giuseppe · hermanos pescadores · julio de 2023"),
                ("https://images.unsplash.com/photo-1502323777036-f29e3972d82f?w=1600&q=85&auto=format&fit=crop",
                 "Frame 17",
                 "Anna · hostelera · septiembre de 2023"),
                ("https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=1600&q=85&auto=format&fit=crop",
                 "Frame 22",
                 "Luca · barquero · octubre de 2023"),
                ("https://images.unsplash.com/photo-1521252659862-eec69941b071?w=1600&q=85&auto=format&fit=crop",
                 "Frame 28",
                 "Retrato final · noviembre de 2023 · última luz"),
            ],
            "sections": [
                {
                    "label": "La serie",
                    "heading": "Veintiocho personas, ocho meses",
                    "body":
                        "Una serie de veintiocho retratos de quienes viven el "
                        "Delta del Po véneto como lugar de trabajo — "
                        "pescadores, marisqueras, hosteleros, barqueros. "
                        "Ocho meses de trabajo entre abril y "
                        "noviembre de 2023, siete viajes por las dos provincias "
                        "(Rovigo + Ferrara). Cada retrato viene precedido "
                        "por al menos una jornada pasada con el sujeto "
                        "— nunca sesiones de «toma y daca».",
                },
                {
                    "label": "El método",
                    "heading": "Una sola cámara, una sola luz",
                    "body":
                        "Todos los retratos se hicieron con Mamiya "
                        "7II y ochenta milímetros, en luz natural "
                        "disponible — nada de flash, nada de paneles "
                        "difusores. La película es siempre Kodak Portra "
                        "400, revelada en casa. La elección de un solo "
                        "objetivo (en lugar de un equipo de tres o "
                        "cuatro) es una disciplina formal — obliga "
                        "a moverse respecto al sujeto, no a girar "
                        "el anillo del objetivo.",
                },
                {
                    "label": "La publicación",
                    "heading": "Vogue Italia · Festival Ferrara",
                    "body":
                        "La serie se publicó en la sección "
                        "Photography de Vogue Italia (diciembre de 2023, "
                        "seis páginas) y se expuso en muestra colectiva "
                        "en el Festival Internazionale de Ferrara "
                        "(octubre de 2023, doce copias seleccionadas). "
                        "Una copia entró en la colección "
                        "permanente del MAXXI de Roma.",
                },
            ],
            "next_label": "Serie siguiente",
        },
    ],
}
