"""Phase 2g3.7 · Session 53 · Casa — ES native-voice tree. Warm residential-agency voice."""
from __future__ import annotations

from typing import Any


CASA_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",        "label": "Inicio",         "kind": "home"},
        {"slug": "immobili",    "label": "Inmuebles",      "kind": "project_list"},
        {"slug": "quartieri",   "label": "Barrios",        "kind": "about"},
        {"slug": "agenzia",     "label": "La Agencia",     "kind": "team"},
        {"slug": "valutazione", "label": "Valoración",     "kind": "services"},
        {"slug": "contatti",    "label": "Contacto",       "kind": "contact"},
    ],

    "site": {
        "logo_initial":  "D",
        "logo_word":     "Domus Immobiliare",
        "tag":           "Milán · Turín · desde 2005",
        "phone":         "+39 02 8765 4321",
        "phone_tel":     "+390287654321",
        "phone_label":   "Llámanos",
        "email":         "hola@domusimmobiliare.it",
        "address":       "Corso Buenos Aires 15 · 20124 Milán",
        "address_short": "Milán · Turín",
        "hours_compact": "Lun – Sáb · 09:00 – 19:30",
        "hours_footer_rows": [
            "Visitas guiadas también los domingos",
            "WhatsApp siempre abierto",
        ],
        "whatsapp":      "02 8765 4321",
        "whatsapp_link": "https://wa.me/390287654321",
        "whatsapp_note": "Respondemos en 20 minutos en horario comercial",
        "license":       "Licencia de agencia inmobiliaria RIEA MI 1422 · CIF 05431920968",
        "nav_cta":       "Reservar una visita",
        "nav_cta_href":  "contatti",
        "footer_intro":
            "Domus Immobiliare — cada inmueble que proponemos lo elegimos "
            "a mano. Veinte años entre Milán, Turín, el lago de Como y "
            "el Piamonte, un solo agente dedicado desde la primera "
            "visita hasta la firma ante notario.",
        "foot_studio":   "La agencia",
        "foot_pages":    "Páginas",
        "foot_contact":  "Contáctanos",
        "foot_offices":  "Sedes",
        "offices_footer_rows": [
            "Milán · Buenos Aires 15",
            "Turín · Crocetta 8",
        ],
        "tile_rooms_label":    "Habs",
        "tile_surface_label":  "Superficie",
        "tile_bathrooms_label":"Baños",
        "tile_surface_unit":   "m²",
        "tile_visit_cta":      "Reservar visita",
        "tile_reference_label":"Ref.",
        "surface_short":       "m²",
        "price_label":         "Precio",
        "energy_class_label":  "Calificación energética",
        "floor_label":         "Planta",
        "parking_label":       "Plaza de garaje",
        "elevator_label":      "Ascensor",
        "filter_label":        "Filtrar por",
        "sort_label":          "Ordenar por",
        "visit_request_label": "Reservar una visita",
        "viewings_unit":       "visitas esta semana",
        "showings_schedule":   "Visitas todos los días, sábados y domingos incluidos",
    },

    "home": {
        "eyebrow":  "Domus Immobiliare · Milán · Turín · Lombardía y Piamonte",
        "headline": "Seiscientas casas elegidas a mano, <em>un solo agente</em> del primer encuentro a la escritura.",
        "intro":
            "Más de 600 inmuebles elegidos a mano entre Milán, Turín, el "
            "lago de Como y el Piamonte. Visitas guiadas también los "
            "domingos, valoración gratuita en 24 horas, y un solo agente "
            "que te acompaña desde la primera cita hasta la firma.",
        "primary_cta":   "Buscar un inmueble",
        "primary_href":  "immobili",
        "secondary_cta": "Valoración gratuita",
        "secondary_href":"valutazione",
        "hero_availability": "20 nuevas propuestas esta semana",
        "hero_response":     "Te devolvemos la llamada en 20 minutos",

        "search_widget": {
            "label":          "¿Qué buscas hoy?",
            "intro":          "Cuéntanos la casa y la zona, del resto nos ocupamos nosotros.",
            "location_label": "Dónde",
            "location_value": "Milán, centro",
            "type_label":     "Tipo de inmueble",
            "type_value":     "Piso",
            "price_label":    "Precio",
            "price_value":    "500 K € — 1,2 M €",
            "rooms_label":    "Dormitorios",
            "rooms_value":    "3+ dormitorios",
            "cta":            "Buscar inmueble",
            "cta_href":       "immobili",
            "secondary_note": "O cuéntanos por WhatsApp lo que buscas",
            "popular_label":  "Los más buscados",
            "popular_tags": [
                "Pisos en Brera",
                "Villas en Cernobbio",
                "Lofts en los Navigli",
                "Pisos de tres dormitorios en Turín",
                "Casas con jardín",
            ],
        },

        "featured_label":   "Destacados de la semana",
        "featured_heading": "Los inmuebles <em>que te están esperando</em>.",
        "featured_intro":
            "Una selección ajustada entre las visitas de los últimos "
            "diez días. Cada ficha está comprobada personalmente por un "
            "agente, cada foto se hace durante la visita real.",
        "featured_link":    "Ver los 600+ inmuebles",
        "featured_link_href":"immobili",
        "featured_listings": [
            ("1.250.000 €", "Ático panorámico con terraza",            "Milano · Brera",      "4", "180", "2", "Exclusiva",  "MI-1842"),
            ("890.000 €",   "Villa moderna con jardín",                "Como · Cernobbio",    "5", "240", "3", "Nueva",      "CO-0217"),
            ("650.000 €",   "Loft de diseño en zona Tortona",          "Milano · Navigli",    "2", "120", "2", "Reformado",  "MI-1788"),
            ("420.000 €",   "Piso luminoso de tres dorm. con balcón",  "Torino · Crocetta",   "3",  "95", "1", "Disponible", "TO-0904"),
        ],

        "neighborhoods_label":   "Barrios",
        "neighborhoods_heading": "Dónde <em>encontramos tu casa</em>.",
        "neighborhoods_intro":
            "Milán, Turín, el lago. Cada barrio lo cubre un agente que "
            "vive allí — conocemos a los conserjes, los cafés, las "
            "escuelas, la mejor parada para ir al centro.",
        "neighborhoods": [
            ("Brera",     "Milano · histórico",     "124 inmuebles", "desde 850 K €"),
            ("Navigli",   "Milano · diseño",        "89 inmuebles",  "desde 520 K €"),
            ("Isola",     "Milano · contemporáneo", "71 inmuebles",  "desde 480 K €"),
            ("Cernobbio", "Como · lago",            "42 inmuebles",  "desde 680 K €"),
            ("Crocetta",  "Torino · residencial",   "67 inmuebles",  "desde 380 K €"),
            ("Borgo Po",  "Torino · colinas",       "38 inmuebles",  "desde 410 K €"),
        ],
        "neighborhoods_cta":      "Explorar todos los barrios",
        "neighborhoods_cta_href": "quartieri",

        "stats_label":   "Veinte años en el mercado",
        "stats_heading": "Nuestros números, a la vista.",
        "stats_intro":
            "Lo que cuenta no es cuántas casas tenemos en el escaparate, "
            "sino cuántas hemos vendido de verdad. Estos son los números "
            "desde 2005 hasta hoy.",
        "stats": [
            ("600",   "+", "inmuebles en cartera"),
            ("2.800", "+", "casas encontradas desde 2005"),
            ("20",    "",  "años de experiencia"),
            ("4,8",   " ★","sobre 420 reseñas de Google"),
        ],
        "stats_note": "Datos actualizados a marzo de 2026 · verificables en immobiliare.it",

        "agents_label":   "Quién te acompaña",
        "agents_heading": "Un solo agente, <em>de principio a fin</em>.",
        "agents_intro":
            "Ni centralitas, ni asesores rotatorios. Desde la primera "
            "cita hasta la firma hablas siempre con la misma persona — "
            "la que conoce el barrio, el edificio y, muchas veces, "
            "también al vecino de rellano.",
        "agents_preview": [
            ("Giulia Ferrante", "Agente sénior",    "Milano · Brera y Centro",    "15 años"),
            ("Marco Lentini",   "Agente sénior",    "Milano · Navigli y Sur",     "12 años"),
            ("Silvia Mondelli", "Responsable",      "Torino · Crocetta",          "10 años"),
            ("Andrea Colombo",  "Agente sénior",    "Como · lago",                "18 años"),
        ],
        "agents_cta":      "Conoce a todo el equipo",
        "agents_cta_href": "agenzia",

        "valuation_label":   "Valoración gratuita",
        "valuation_heading": "¿Cuánto vale <em>tu casa</em>?",
        "valuation_intro":
            "Te devolvemos la llamada en 24 horas con una estimación "
            "honesta, basada en el contraste de todas las escrituras "
            "registradas en los últimos doce meses en tu manzana. Sin "
            "compromiso, coste cero, incluso si después decides vender "
            "con otra agencia.",
        "valuation_cta":       "Solicitar valoración",
        "valuation_cta_href":  "valutazione",
        "valuation_secondary": "Cómo funciona",
        "valuation_secondary_href":"valutazione",
        "valuation_proof": [
            ("24 h",   "tiempo de respuesta"),
            ("0 €",    "coste, siempre"),
            ("420+",   "valoraciones en 2025"),
        ],

        "testimonial_label":  "Han comprado con nosotros",
        "testimonial_quote":
            "En diez minutos entendieron lo que buscábamos. Tres visitas, "
            "la cuarta era nuestra casa. Giulia nos acompañó incluso al "
            "notario — y nunca habíamos comprado casa antes.",
        "testimonial_author": "Francesca y Tommaso Ranieri",
        "testimonial_meta":   "Tres dormitorios · Brera · comprado en marzo 2026",
    },

    "quartieri": {
        "eyebrow":  "Guía de barrios · Milán · Turín · Como",
        "headline": "Los barrios <em>que mejor conocemos</em>.",
        "intro":
            "Cada barrio aquí abajo lo cubre uno de nuestros agentes "
            "residentes. Encontrarás precios medios, disponibilidad "
            "actual, superficie tipo y la firma de quien trabaja allí "
            "todos los días.",

        "guides_label": "Guía de barrios",
        "guides_heading": "Elige el barrio, <em>nosotros conocemos el camino</em>.",
        "guides": [
            (
                "Brera", "Milano · histórico y cultural",
                "9.200 € / m²", "124 inmuebles disponibles",
                "M2 Lanza · M3 Montenapoleone", "Parco Sempione a 6 min", "Lujo histórico",
                "El corazón histórico de Milán: palacios del siglo XIX, "
                "patios interiores, atelieres y un tejido de comercios "
                "únicos que no se repiten en ningún otro sitio. Muchas "
                "reformas conservadoras, pocas obras nuevas. Ideal para "
                "quien busca un reparto clásico con plusvalía consolidada.",
                "Giulia Ferrante · agente residente desde 2008",
            ),
            (
                "Navigli", "Milano · diseño y vida nocturna",
                "7.100 € / m²", "89 inmuebles disponibles",
                "M2 Porta Genova · Tranvía 3/9", "Darsena · Ticinese a pie", "Creativo y joven",
                "El eje de los dos canales: lofts industriales, casas "
                "de época con galerías exteriores, estudios de "
                "arquitectura. Dinámico, internacional, vivo por la "
                "noche. Perfecto para inversión a corto o medio plazo "
                "o una primera compra joven.",
                "Marco Lentini · agente sénior",
            ),
            (
                "Porta Nuova", "Milano · nuevo skyline",
                "10.400 € / m²", "56 inmuebles disponibles",
                "M2 Gioia · M3 Repubblica", "BAM Biblioteca de los Árboles", "Contemporáneo y business",
                "El distrito del nuevo milenio milanés: rascacielos, "
                "finanzas, residencias de diseño como Bosco Verticale "
                "y Solaria. Ideal para quien busca servicios premium, "
                "conserjería, soluciones domóticas integradas.",
                "Giulia Ferrante · agente residente",
            ),
            (
                "Isola", "Milano · contemporáneo creativo",
                "7.600 € / m²", "71 inmuebles disponibles",
                "M5 Isola · Tranvía 2/4", "BAM a 5 min · Parco Lambro en 10", "Creativo y residencial",
                "Antiguo barrio obrero renacido en torno a Porta "
                "Nuova. Casas con galería restauradas junto a "
                "residencias nuevas. Ambiente milanés auténtico, "
                "mercado en crecimiento estable desde hace diez años.",
                "Sofia Ranieri · agente júnior · Milán Norte",
            ),
            (
                "Cernobbio", "Como · lago y villas",
                "5.900 € / m²", "42 inmuebles disponibles",
                "Tren Cadorna-Como · 48 min", "Lago a pie · Parque Villa Erba", "Lago y segundas residencias",
                "La orilla occidental del Lario: villas de época con "
                "acceso al lago, pisos en edificios históricos frente "
                "al golfo, áticos con vistas. Mercado internacional, "
                "inglés y alemán al día en la oficina.",
                "Andrea Colombo · agente sénior de lago",
            ),
            (
                "Bellagio", "Como · perla del Lario",
                "6.400 € / m²", "29 inmuebles disponibles",
                "Barco Como-Bellagio · coche", "Casco histórico peatonal", "Exclusivo e internacional",
                "La punta del triángulo del lago: centro histórico "
                "medieval, villas en la Punta Spartivento, residencias "
                "panorámicas con doble vistas. Mercado de nicho, "
                "disponibilidad siempre limitada.",
                "Andrea Colombo · lago de Como",
            ),
            (
                "Crocetta", "Torino · residencial elegante",
                "3.900 € / m²", "67 inmuebles disponibles",
                "M1 Re Umberto · Tranvía 4/10", "Parco del Valentino · 12 min", "Burgués y familiar",
                "El buen barrio de Turín: palacios de los años 30, "
                "patios silenciosos, escuelas históricas, mercado "
                "cubierto. Superficies amplias, alta calidad de vida, "
                "precios todavía accesibles frente a Milán. Recomendado "
                "para familias.",
                "Silvia Mondelli · responsable Turín",
            ),
            (
                "Borgo Po", "Torino · colinas y panorámico",
                "4.200 € / m²", "38 inmuebles disponibles",
                "Tranvía 13/15 · Gran Madre", "Colinas · Monte dei Cappuccini", "Romántico y vistas",
                "La orilla derecha del Po: palacetes modernistas, "
                "villas en la colina, áticos con vistas a los Alpes. "
                "Tejido de bistrós y locales históricos. Para quien "
                "busca aire y panorama a diez minutos del centro.",
                "Silvia Mondelli · Turín colinas y centro",
            ),
        ],

        "faq_label":   "Preguntas frecuentes sobre los barrios",
        "faq_heading": "Lo que más nos preguntan.",
        "faq": [
            (
                "¿Cuál es el mejor barrio para una familia que se muda a Milán?",
                "Para familias recomendamos Crocetta en Turín, Isola y "
                "Porta Nuova en Milán. Los tres tienen escuelas cerca, "
                "parques a pie, metro a dos pasos. Si prefieres la "
                "colina, Borgo Po en Turín es la elección correcta.",
            ),
            (
                "¿Centro histórico o zona emergente como inversión?",
                "Depende del horizonte. Centro histórico = plusvalía "
                "consolidada, crecimiento del 2-3 % anual. Zonas "
                "emergentes como Isola han subido un +48 % en diez años, "
                "pero el riesgo es mayor. Lo hablamos en una llamada "
                "de quince minutos.",
            ),
            (
                "¿Gestionáis también alquileres o solo compraventa?",
                "Principalmente compraventa. Gestionamos alquileres "
                "solo para inmuebles que nos encarga un vendedor y "
                "prefiere poner en renta mientras tanto. Para alquiler "
                "puro te indicamos al compañero adecuado.",
            ),
            (
                "¿Cómo funciona una visita al lago de Como si vivo en Milán?",
                "El sábado por la mañana organizamos una lanzadera "
                "desde Milán Cadorna: tres inmuebles visitados en el "
                "día, comida incluida, vuelta a las 18:00. Así lo ves "
                "todo sin alquilar coche.",
            ),
        ],

        "cta_label":   "Habla con el agente de tu barrio",
        "cta_heading": "Un café, veinte minutos, todo más claro.",
        "cta_intro":
            "Elige un barrio y te ponemos en contacto con el agente "
            "que trabaja allí todos los días. Primera cita gratis, en "
            "la oficina o sobre el terreno.",
        "cta_primary":       "Reservar una visita",
        "cta_primary_href":  "contatti",
        "cta_secondary":     "Valoración gratuita",
        "cta_secondary_href":"valutazione",
    },

    "agenzia": {
        "eyebrow":  "El equipo · 14 personas · Milán y Turín",
        "headline": "Los agentes que te acompañan <em>desde la primera visita hasta la firma</em>.",
        "intro":
            "Nueve agentes colegiados, dos coordinadores, tres personas "
            "en el back-office notarial. Cada zona tiene a su agente "
            "residente, cada expediente su ficha técnica, cada cliente "
            "un solo número al que llamar.",

        "book_cta":       "Reservar una visita",
        "agents_heading": "El equipo al completo.",
        "agents_intro":
            "En la agencia trabajamos en pareja: un sénior lleva el "
            "inmueble, un júnior lleva a las familias que buscan. Así "
            "tienes respuestas también por la tarde y los sábados.",

        "agents": [
            {
                "name": "Giulia Ferrante",
                "role": "Socia · Responsable Milán Centro",
                "area": "Milano · Brera, Quadrilatero, Porta Nuova",
                "years": "15 años",
                "languages": "Italiano · Inglés · Francés",
                "speciality": "Palacios históricos, plantas altas, piano "
                              "nobile. Acompañamiento completo desde la visita hasta la firma.",
                "phone": "+39 02 8765 4322",
                "whatsapp_href": "https://wa.me/390287654322",
                "email": "giulia@domusimmobiliare.it",
                "quote": "La casa adecuada existe: el trabajo es escuchar "
                         "lo suficiente para reconocerla en la primera visita.",
            },
            {
                "name": "Marco Lentini",
                "role": "Agente sénior · Milán Sur",
                "area": "Milano · Navigli, Tortona, Bocconi",
                "years": "12 años",
                "languages": "Italiano · Inglés",
                "speciality": "Lofts industriales, casas con galería, "
                              "reformas de diseño. Contactos con estudios de arquitectura locales.",
                "phone": "+39 02 8765 4323",
                "whatsapp_href": "https://wa.me/390287654323",
                "email": "marco@domusimmobiliare.it",
                "quote": "En los Navigli el valor no es el metro cuadrado: "
                         "es el patio, la luz, el silencio entre dos canales.",
            },
            {
                "name": "Silvia Mondelli",
                "role": "Responsable Turín",
                "area": "Torino · Crocetta, Cit Turin, Centro",
                "years": "10 años",
                "languages": "Italiano · Inglés · Español",
                "speciality": "Familias en traslado, primeras viviendas, "
                              "acompañamiento fiscal para quien regresa del extranjero.",
                "phone": "+39 011 5328 4401",
                "whatsapp_href": "https://wa.me/390115328440",
                "email": "silvia@domusimmobiliare.it",
                "quote": "Turín hoy ofrece lo que Milán ofrecía hace veinte "
                         "años: superficies amplias, precios justos, calidad de vida.",
            },
            {
                "name": "Andrea Colombo",
                "role": "Agente sénior · Lago de Como",
                "area": "Como · Cernobbio, Bellagio, Tremezzo",
                "years": "18 años",
                "languages": "Italiano · Inglés · Alemán",
                "speciality": "Villas de época, segundas residencias "
                              "para clientela internacional, gestión posventa estacional.",
                "phone": "+39 031 2345 6789",
                "whatsapp_href": "https://wa.me/390312345678",
                "email": "andrea@domusimmobiliare.it",
                "quote": "En el lago cada villa tiene cien años de historia. "
                         "Mi trabajo es llevar la firma a tres meses.",
            },
            {
                "name": "Sofia Ranieri",
                "role": "Agente · Milán Norte",
                "area": "Milano · Isola, Porta Nuova, Dergano",
                "years": "6 años",
                "languages": "Italiano · Inglés",
                "speciality": "Obra nueva, calificación energética alta, "
                              "primeras viviendas para profesionales de 30-40 años.",
                "phone": "+39 02 8765 4324",
                "whatsapp_href": "https://wa.me/390287654324",
                "email": "sofia@domusimmobiliare.it",
                "quote": "La Isola de hoy no es la de hace diez años. "
                         "Más fácil de vivir, más difícil de leer en valor.",
            },
            {
                "name": "Luca Benedetti",
                "role": "Agente · Turín Colinas",
                "area": "Torino · Borgo Po, Gran Madre, Maddalena",
                "years": "9 años",
                "languages": "Italiano · Francés",
                "speciality": "Villas modernistas, áticos con vistas a "
                              "los Alpes, reformas importantes con contratación técnica.",
                "phone": "+39 011 5328 4402",
                "whatsapp_href": "https://wa.me/390115328441",
                "email": "luca@domusimmobiliare.it",
                "quote": "La colina de Turín es poesía urbana: diez "
                         "minutos del centro y los Alpes de frente cada mañana.",
            },
            {
                "name": "Chiara Sestri",
                "role": "Agente júnior · Milán Centro",
                "area": "Milano · Brera, Magenta, Cadorna",
                "years": "3 años",
                "languages": "Italiano · Inglés · Francés · Árabe",
                "speciality": "Acompañamiento lingüístico a clientela "
                              "internacional, trámites del código fiscal, primer contacto con el mercado italiano.",
                "phone": "+39 02 8765 4325",
                "whatsapp_href": "https://wa.me/390287654325",
                "email": "chiara@domusimmobiliare.it",
                "quote": "Quien compra casa en Milán desde el extranjero "
                         "necesita que lo acompañen, no solo que lo atiendan.",
            },
            {
                "name": "Davide Orsini",
                "role": "Agente · Monza y Brianza",
                "area": "Monza · Seregno · Desio",
                "years": "11 años",
                "languages": "Italiano · Inglés",
                "speciality": "Casas independientes con jardín, villas "
                              "unifamiliares, mercado residencial para familias que dejan Milán.",
                "phone": "+39 039 5328 4403",
                "whatsapp_href": "https://wa.me/390395328440",
                "email": "davide@domusimmobiliare.it",
                "quote": "Cada año veo familias comprar en Brianza para "
                         "el tercer hijo: es un indicador económico mejor que el PIB.",
            },
            {
                "name": "Elisa Parini",
                "role": "Coordinadora notarial",
                "area": "Back-office · sede central Milán",
                "years": "8 años",
                "languages": "Italiano · Inglés · Español",
                "speciality": "Trámites notariales, comprobaciones "
                              "hipotecarias, instrucción del préstamo, gestión de firma de principio a fin.",
                "phone": "+39 02 8765 4326",
                "whatsapp_href": "https://wa.me/390287654326",
                "email": "elisa@domusimmobiliare.it",
                "quote": "La firma es el último metro pero a menudo el "
                         "más delicado: un error en el plano cuesta meses.",
            },
        ],

        "facts_label":   "La agencia, en breve",
        "facts_heading": "Veinte años, una sola regla: un agente por familia.",
        "facts": [
            ("2005", "",  "año de fundación"),
            ("9",    "",  "agentes colegiados"),
            ("2",    "",  "sedes · Milán y Turín"),
            ("2.800","+", "familias acompañadas hasta la firma"),
        ],

        "footnote_strong": "¿Quieres hablar con uno de nosotros?",
        "footnote_body":
            "Elige al agente de tu zona o escríbenos por chat: te "
            "ponemos en contacto en menos de una hora laboral. ",
        "footnote_link":  "Escríbenos por WhatsApp",
    },

    "valutazione": {
        "eyebrow":  "Valoración gratuita · respuesta en 24 horas",
        "headline": "¿Cuánto vale <em>tu casa</em>?",
        "intro":
            "Te devolvemos la llamada en 24 horas con una estimación "
            "honesta, basada en el contraste de todas las escrituras "
            "registradas en los últimos doce meses en tu manzana. Sin "
            "compromiso, coste cero, incluso si después decides vender "
            "con otra agencia.",

        "how_it_works_label":   "Cómo funciona",
        "how_it_works_heading": "Tres pasos, <em>sin sorpresas</em>.",
        "how_it_works": [
            ("01", "Rellenas el formulario",
             "Necesitamos dirección, tipo de inmueble, superficie y cuatro "
             "detalles sobre su estado. Cinco minutos, sin documentos "
             "adjuntos en esta fase."),
            ("02", "Te llamamos en 24 h",
             "Un agente de tu barrio te llama, confirma los datos y, si "
             "hace falta, concierta una visita gratuita. Para Milán y "
             "Turín muchas veces ya al día siguiente."),
            ("03", "Recibes la estimación por escrito",
             "En 48 horas desde la visita te llega una valoración escrita "
             "con horquilla de precio, comparables de la zona, plan "
             "recomendado de puesta en el mercado."),
        ],

        "form_label":   "Solicitar la valoración",
        "form_heading": "Háblanos de tu inmueble",
        "form_intro":
            "Descríbenos tu casa en cinco minutos. Los campos con "
            "asterisco son obligatorios — los demás ayudan a darte una "
            "estimación más precisa ya en el primer contacto.",
        "form_submit_label": "Solicitar valoración gratuita",
        "form_submit_note":
            "Te devolvemos la llamada en 24 horas laborables. Tus datos "
            "solo los trata el agente asignado, sin terceros involucrados.",
        "form_consent":
            "Consiento el tratamiento de los datos personales según el "
            "Reglamento UE 679/2016. La solicitud la lee y archiva "
            "únicamente el agente Domus — sin bróker externo implicado.",

        "form_sections": [
            {"num": "01", "title": "Tu inmueble",
             "meta": "Dirección, tipo, superficie. Cinco minutos.",
             "fields": ["address", "city", "property_type", "surface", "rooms", "bathrooms"]},
            {"num": "02", "title": "Estado del inmueble",
             "meta": "Cuatro puntos que pesan mucho en la estimación.",
             "fields": ["condition", "floor", "energy_class", "timeline"]},
            {"num": "03", "title": "Tus datos",
             "meta": "Para llamarte en 24 horas.",
             "fields": ["name", "surname", "email", "phone", "notes"]},
        ],

        "form_fields": [
            {"name": "address", "label": "Dirección del inmueble", "type": "text", "required": True,
             "placeholder": "Ej. Via della Spiga 12", "full_width": True,
             "helper": "Calle y número. El barrio lo deducimos nosotros."},
            {"name": "city", "label": "Ciudad", "type": "select", "required": True,
             "options": ["Milán", "Turín", "Como y provincia", "Monza y Brianza", "Otra (especificar en notas)"],
             "helper": "Si no encuentras tu ciudad, indícalo en las notas."},
            {"name": "property_type", "label": "Tipo de inmueble", "type": "select", "required": True,
             "options": [
                 "Piso · dos ambientes",
                 "Piso · tres ambientes",
                 "Piso · cuatro ambientes o más",
                 "Ático",
                 "Loft",
                 "Villa independiente",
                 "Villa adosada o pareada",
                 "Oficina",
                 "Otro",
             ],
             "helper": "Selección obligatoria para avanzar."},
            {"name": "surface", "label": "Superficie útil (m²)", "type": "number", "required": True,
             "placeholder": "Ej. 95",
             "helper": "Superficie interior habitable, sin terrazas ni plaza de garaje."},
            {"name": "rooms", "label": "Dormitorios", "type": "select", "required": True,
             "options": ["1", "2", "3", "4", "5", "6 o más"],
             "helper": "Cuenta los dormitorios, no los salones."},
            {"name": "bathrooms", "label": "Baños", "type": "select", "required": True,
             "options": ["1", "2", "3", "4 o más"]},
            {"name": "condition", "label": "Estado de conservación", "type": "select", "required": True,
             "options": [
                 "Obra nueva o reformado íntegramente",
                 "Buen estado · pequeñas intervenciones",
                 "A reformar parcialmente",
                 "A reformar por completo",
                 "En bruto · inmueble de obra nueva",
             ],
             "helper": "Influye mucho en la valoración."},
            {"name": "floor", "label": "Planta", "type": "select", "required": False,
             "options": ["Planta baja", "Entresuelo", "1ª", "2ª", "3ª", "4ª o superior", "Ático", "Villa independiente"],
             "helper": "Opcional — útil para pisos."},
            {"name": "energy_class", "label": "Calificación energética", "type": "select", "required": False,
             "options": ["A4 / A3 / A2 / A1", "B", "C", "D", "E", "F", "G", "No disponible"],
             "helper": "Si no la sabes, selecciona «No disponible»."},
            {"name": "timeline", "label": "Plazo de venta", "type": "select", "required": True,
             "options": [
                 "En 3 meses · urgente",
                 "En 6 meses",
                 "En 12 meses",
                 "Exploratorio · sin urgencia",
             ],
             "helper": "Ayuda a planificar el calendario de visitas."},
            {"name": "name", "label": "Nombre", "type": "text", "required": True, "placeholder": "Ej. Laura"},
            {"name": "surname", "label": "Apellidos", "type": "text", "required": True, "placeholder": "Ej. Ferrante"},
            {"name": "email", "label": "E-mail", "type": "email", "required": True,
             "placeholder": "laura.ferrante@example.it",
             "helper": "Te enviamos la valoración por escrito por correo."},
            {"name": "phone", "label": "Teléfono", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "Te devolvemos la llamada en 24 horas laborables."},
            {"name": "notes", "label": "Notas adicionales", "type": "textarea", "required": False,
             "full_width": True,
             "placeholder": "Cuéntanos algo más del inmueble — terraza, "
                            "trastero, bodega, ascensor, obras ya "
                            "presupuestadas. Máximo 600 caracteres.",
             "helper": "Opcional, pero ayuda a afinar la estimación."},
        ],

        "proof_label":   "Por qué confiar",
        "proof_heading": "Una valoración seria, no un reclamo comercial.",
        "proof": [
            ("420+",  "valoraciones escritas en 2025"),
            ("92 %",  "inmuebles vendidos en 6 meses"),
            ("0 €",   "coste de la valoración"),
            ("24 h",  "tiempo de respuesta"),
        ],

        "faq_label":   "Preguntas sobre la valoración",
        "faq_heading": "Lo que más nos preguntan.",
        "faq": [
            (
                "¿La valoración es realmente gratis?",
                "Sí, siempre. Incluso si luego decides vender con otra "
                "agencia — ha pasado, no es un drama. El coste de la "
                "visita corre de nuestra cuenta.",
            ),
            (
                "¿Cuánto tarda entre la solicitud y la valoración escrita?",
                "Te devolvemos la llamada en 24 horas laborables. Si hace "
                "falta una visita, la concertamos en 3 días. La "
                "valoración escrita llega en 48 horas desde la visita.",
            ),
            (
                "¿Vale la valoración para hipoteca o herencia?",
                "Para uso bancario o sucesorio hace falta una tasación "
                "jurada por un tasador colegiado. Nuestra estimación es "
                "de mercado — valiosa para decidir, no legalmente oponible.",
            ),
            (
                "¿Tengo que enseñaros documentos en esta fase?",
                "No. Nos basta con los datos del formulario. Escritura, "
                "plano y certificado energético solo serán necesarios "
                "si luego decides poner el inmueble a la venta con nosotros.",
            ),
        ],
    },

    "contatti": {
        "eyebrow":  "Contacto · Milán y Turín",
        "headline": "Escríbenos, <em>te devolvemos la llamada en 20 minutos</em>.",
        "intro":
            "Puedes escribir, llamar o pasar por la agencia. El sábado "
            "estamos abiertos todo el día, el domingo con cita previa. "
            "Para urgencias WhatsApp es el canal más rápido.",

        "offices_label":   "Las oficinas",
        "offices_heading": "Dos oficinas, <em>un solo equipo</em>.",
        "offices": [
            {
                "name": "Milán · sede central",
                "address": "Corso Buenos Aires 15 · 20124 Milán",
                "metro": "M1 Lima · M1 Loreto · Tranvía 33",
                "hours": "Lun – Sáb · 09:00 – 19:30 · Dom con cita",
                "phone": "+39 02 8765 4321",
                "whatsapp": "02 8765 4321",
                "whatsapp_href": "https://wa.me/390287654321",
                "email": "milano@domusimmobiliare.it",
                "map_link": "Abrir en Google Maps",
                "map_href": "https://maps.google.com/?q=Corso+Buenos+Aires+15+Milano",
                "lead_agent": "Giulia Ferrante · responsable Milán",
                "parking": "Parking concertado a 80 m · Garage Abadia",
                "note": "Oficina amplia con tres salas dedicadas a "
                        "reuniones privadas. Agua, café y wifi a disposición.",
            },
            {
                "name": "Turín · Crocetta",
                "address": "Via Legnano 8 · 10128 Turín",
                "metro": "M1 Re Umberto · Tranvía 4/10",
                "hours": "Lun – Vie · 09:00 – 19:00 · Sáb 09:30 – 13:00",
                "phone": "+39 011 5328 4400",
                "whatsapp": "011 5328 4400",
                "whatsapp_href": "https://wa.me/390115328440",
                "email": "torino@domusimmobiliare.it",
                "map_link": "Abrir en Google Maps",
                "map_href": "https://maps.google.com/?q=Via+Legnano+8+Torino",
                "lead_agent": "Silvia Mondelli · responsable Turín",
                "parking": "ZTL gratuita en fin de semana · parking Piazza Solferino",
                "note": "Oficina acogedora en el corazón de la Crocetta, "
                        "a dos minutos a pie del Politecnico.",
            },
        ],

        "channels_label":   "Canales directos",
        "channels_heading": "Elige cómo contactarnos.",
        "channels": [
            ("Teléfono",       "+39 02 8765 4321",                "Respuesta inmediata en horario comercial"),
            ("WhatsApp Milán", "02 8765 4321",                    "Mensaje leído en 20 minutos · también por la tarde"),
            ("WhatsApp Turín", "011 5328 4400",                   "Lun – Sáb · el mismo equipo que ves en oficina"),
            ("E-mail",         "hola@domusimmobiliare.it",        "Respondemos en 4 horas laborables"),
            ("En la oficina",  "Milán · Corso Buenos Aires 15",   "Sin cita Lun – Sáb por la mañana"),
        ],

        "form_label":   "Escríbenos un mensaje",
        "form_heading": "Déjanos tus datos",
        "form_intro":
            "Rellena el formulario, te devolvemos la llamada en 20 "
            "minutos en horario comercial. Si escribes por la tarde, "
            "respondemos la mañana siguiente antes de las diez.",
        "form_submit_label": "Enviar mensaje",
        "form_submit_note":
            "Respuesta en 20 minutos en horario comercial · 4 horas "
            "laborables para correos fuera de horario.",
        "form_consent":
            "Consiento el tratamiento de los datos personales según el "
            "Reglamento UE 679/2016. La solicitud la lee y archiva "
            "únicamente el agente Domus.",

        "form_sections": [
            {"num": "01", "title": "Tus datos",
             "meta": "Para responderte directamente.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Cómo podemos ayudarte",
             "meta": "Una breve referencia, luego lo hablamos por teléfono.",
             "fields": ["topic", "preferred_office", "message"]},
        ],

        "form_fields": [
            {"name": "name", "label": "Nombre", "type": "text", "required": True, "placeholder": "Ej. Francesca"},
            {"name": "surname", "label": "Apellidos", "type": "text", "required": True, "placeholder": "Ej. Ranieri"},
            {"name": "email", "label": "E-mail", "type": "email", "required": True,
             "placeholder": "francesca@example.it"},
            {"name": "phone", "label": "Teléfono", "type": "tel", "required": False,
             "placeholder": "+39 ...", "helper": "Opcional · si prefieres que te llamemos."},
            {"name": "topic", "label": "Asunto de la consulta", "type": "select", "required": True,
             "options": [
                 "Quiero comprar una vivienda",
                 "Quiero vender una vivienda",
                 "Quiero una valoración gratuita",
                 "Busco alquiler (derivado al partner)",
                 "Otro · te lo cuento en el mensaje",
             ]},
            {"name": "preferred_office", "label": "Oficina de referencia", "type": "select", "required": True,
             "options": ["Milán · Corso Buenos Aires", "Turín · Via Legnano", "Lago de Como · con cita"]},
            {"name": "message", "label": "Mensaje", "type": "textarea", "required": True, "full_width": True,
             "placeholder": "Qué buscas, en qué punto estás, cuándo te "
                            "gustaría hablar con nosotros. Máximo 800 "
                            "caracteres — los detalles los vemos en llamada.",
             "helper": "Basta con un resumen: el resto lo hablamos en directo."},
        ],
    },

    "immobili": {
        "eyebrow":  "Escaparate completo · 600+ inmuebles · actualizado esta semana",
        "headline": "Todos los inmuebles <em>que tenemos en cartera</em>.",
        "intro":
            "Una selección viva: cada ficha la verifica el agente de "
            "zona, cada foto se hace en directo, cero renders. Las "
            "novedades llegan cada lunes por la mañana.",

        "filter_label": "Filtrar",
        "filters": [
            "Todos",
            "Milán",
            "Turín",
            "Lago de Como",
            "Menos de 500 K €",
            "500 K € — 1 M €",
            "Más de 1 M €",
            "Ático",
            "Villa",
            "Loft",
            "Obra nueva",
        ],
        "sort_label": "Ordenar",
        "sort_options": [
            "Más recientes",
            "Precio ascendente",
            "Precio descendente",
            "Superficie descendente",
        ],

        "ledger_label": "Escaparate completo",
        "ledger_intro":
            "Pulsa sobre una ficha para abrir la propuesta completa: "
            "plano, calificación energética, historial de obras, "
            "agente de referencia y huecos de visita reservables.",

        "row_rooms_label":    "Habs",
        "row_surface_label":  "m²",
        "row_area_label":     "Zona",
        "row_price_label":    "Precio",
        "row_year_label":     "Desde",
        "row_discipline_label":"Tipo",
        "row_duration_label": "Duración media de la visita",

        "map_label":   "Dónde estamos buscando",
        "map_heading": "Nuestro escaparate, <em>sobre el mapa</em>.",
        "map_intro":
            "Tres provincias, dos oficinas, un solo equipo. Cada punto "
            "en el mapa corresponde a un inmueble actualmente en venta "
            "o a punto de entrar en el escaparate.",
        "map_note":
            "El mapa interactivo está disponible en la versión comercial "
            "del sitio — aquí solo ves una cobertura orientativa de la "
            "presencia.",
        "map_cells": [
            ("Milán ciudad",    "412 inmuebles"),
            ("Monza Brianza",   "58 inmuebles"),
            ("Lago de Como",    "71 inmuebles"),
            ("Turín ciudad",    "105 inmuebles"),
            ("Turín colinas",   "38 inmuebles"),
        ],

        "cta_label":        "¿No encuentras lo que buscas?",
        "cta_heading":      "Dinos qué falta. <em>Lo encontramos</em>.",
        "cta_intro":
            "En los últimos cinco años más del 30 % de las casas que "
            "hemos vendido no estaban en internet: las teníamos de "
            "vendedores habituales. Cuéntanos qué buscas y te avisamos "
            "en cuanto llegue algo adecuado.",
        "cta_primary":        "Reservar una visita",
        "cta_primary_href":   "contatti",
        "cta_secondary":      "Hablémoslo por teléfono",
        "cta_secondary_href": "contatti",

        "dossier_meta_price_label":    "Precio",
        "dossier_meta_surface_label":  "Superficie",
        "dossier_meta_rooms_label":    "Habs",
        "dossier_meta_bathrooms_label":"Baños",
        "dossier_meta_energy_label":   "Calificación energética",
        "dossier_meta_floor_label":    "Planta",
        "dossier_summary_label":       "Lo que te va a enamorar",
        "dossier_highlights_label":    "Puntos fuertes",
        "dossier_highlights_heading":  "Los detalles que importan.",
        "dossier_agent_label":         "Agente de referencia",
        "dossier_book_cta":            "Reservar una visita",
        "dossier_next_label":          "Siguiente inmueble",
    },

    "posts": [
        {
            "slug":       "attico-brera-duomo",
            "title":      "Ático panorámico con terraza · Brera",
            "price":      "1.250.000 €",
            "area":       "Milano · Brera · Via Madonnina 14",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "180",
            "energy":     "B",
            "floor":      "7ª (última · ascensor)",
            "badge":      "Exclusiva",
            "reference":  "MI-1842",
            "year_built": "1923 · reforma integral 2024",
            "lead":
                "Un ático en la última planta de un palacio de época "
                "con terraza de sesenta metros y vistas de 270 grados "
                "al Duomo y la Piazza della Scala. Reforma 2024 firmada "
                "por Studio Arfaioli, tecnología domótica integrada.",
            "summary": [
                "Terraza de 62 m² con vistas al Duomo y Sforzesco",
                "Cuatro dormitorios, dos baños con mármol de Carrara",
                "Calificación B tras aislamiento y carpinterías de 2024",
                "Ascensor interno hasta el ático, tres plazas de garaje incluidas",
                "Entrega inmediata · escritura en 45 días",
            ],
            "highlights": [
                ("Terraza", "62 m² vistas al Duomo"),
                ("Garaje", "Tres plazas en box privado"),
                ("Domótica", "KNX totalmente integrado"),
                ("Calificación", "B · tras obras 2024"),
            ],
            "description":
                "La vivienda se ha rediseñado por completo bajo la "
                "idea de un loft vertical: zona de día de 70 m² con "
                "doble orientación este-sur, isla de latón cepillado, "
                "biblioteca a toda pared en nogal canaletto. La zona "
                "de noche se reserva para las dos suites con vestidor "
                "y baño privado en mármol statuario. En la terraza, "
                "bañera de hidromasaje exterior y mesa para diez.",
            "agent_name":  "Giulia Ferrante",
            "agent_role":  "Agente sénior · Milán Centro",
            "agent_phone": "+39 02 8765 4322",
        },
        {
            "slug":       "villa-cernobbio-lago",
            "title":      "Villa moderna con jardín · Cernobbio",
            "price":      "890.000 €",
            "area":       "Como · Cernobbio · Via Regina 88",
            "rooms":      "5",
            "bathrooms":  "3",
            "surface":    "240",
            "energy":     "A2",
            "floor":      "Villa independiente · 3 niveles",
            "badge":      "Nueva",
            "reference":  "CO-0217",
            "year_built": "2023",
            "lead":
                "Villa de obra nueva en tres niveles a doscientos "
                "metros del lago, jardín privado de mil metros con "
                "piscina climatizada. Acabados contemporáneos, "
                "instalación geotérmica, calificación A2.",
            "summary": [
                "Jardín privado de 1.020 m² con piscina 10 × 4",
                "Cinco dormitorios, tres baños, estudio y lavadero separados",
                "Geotermia · calificación energética A2",
                "Acceso directo al lago a 200 m",
                "Box doble y plaza de invitados cubierta",
            ],
            "highlights": [
                ("Jardín", "1.020 m² con piscina"),
                ("Instalación", "Geotermia · fotovoltaica 8 kW"),
                ("Dormitorios", "Cinco · dos suites"),
                ("Calificación", "A2 · consumos casi nulos"),
            ],
            "description":
                "La villa se alza sobre una parcela en esquina con "
                "jardín en tres lados, orientación sureste para la "
                "zona de día. Sótano con sala, bodega climatizada y "
                "box doble; planta baja con salón de doble altura, "
                "cocina profesional Boffi y acceso al jardín; planta "
                "superior con cuatro dormitorios y dos baños, más "
                "suite principal con vestidor.",
            "agent_name":  "Andrea Colombo",
            "agent_role":  "Agente sénior · Lago de Como",
            "agent_phone": "+39 031 2345 6789",
        },
        {
            "slug":       "loft-tortona-navigli",
            "title":      "Loft de diseño en zona Tortona",
            "price":      "650.000 €",
            "area":       "Milano · Navigli · Via Savona 22",
            "rooms":      "2",
            "bathrooms":  "2",
            "surface":    "120",
            "energy":     "C",
            "floor":      "Baja elevada · patio",
            "badge":      "Reformado",
            "reference":  "MI-1788",
            "year_built": "1902 · recuperación ex-fábrica 2020",
            "lead":
                "Loft de ciento veinte metros en una antigua fábrica "
                "de principios del XX, doble altura cuatro metros y "
                "medio, suelo original de roble, altillo de hierro "
                "negro para la zona de noche. Vistas a un patio "
                "interior silencioso.",
            "summary": [
                "Techo con vigas de hierro y hormigón visto",
                "Zona de día doble altura · cocina abierta",
                "Altillo hierro y madera · suite con vestidor",
                "Patio común con jardincito interior",
                "Cero frente a la calle · silencio total",
            ],
            "highlights": [
                ("Altura", "4,5 m doble altura"),
                ("Luz", "Ventanal 6 × 3 m"),
                ("Mobiliario", "Cocina Boffi incluida"),
                ("Vistas", "Patio silencioso"),
            ],
            "description":
                "El loft se ha sacado del último módulo de una antigua "
                "fábrica textil restaurada en 2020. Se mantienen las "
                "columnas de fundición, el suelo original de roble "
                "reubicado, las carpinterías de hierro sustituidas por "
                "vidrio-cámara térmico. La zona de noche en altillo "
                "domina el espacio sin cerrarlo.",
            "agent_name":  "Marco Lentini",
            "agent_role":  "Agente sénior · Milán Sur",
            "agent_phone": "+39 02 8765 4323",
        },
        {
            "slug":       "trilocale-crocetta-torino",
            "title":      "Piso luminoso de tres dormitorios con balcón · Crocetta",
            "price":      "420.000 €",
            "area":       "Torino · Crocetta · Corso Giovanni Lanza 7",
            "rooms":      "3",
            "bathrooms":  "1",
            "surface":    "95",
            "energy":     "D",
            "floor":      "3ª (ascensor)",
            "badge":      "Disponible",
            "reference":  "TO-0904",
            "year_built": "1932 · mantenimiento ordinario 2019",
            "lead":
                "Piso de tres dormitorios en el corazón de la "
                "Crocetta, edificio de los años treinta "
                "perfectamente conservado, balcón de siete metros "
                "al patio verde, orientación este-oeste. Distribución "
                "clásica, parqué original.",
            "summary": [
                "Edificio años 30 · aislamiento rehecho 2018",
                "Balcón de 7 m² con vista a patio verde",
                "Parqué de roble original · vigas vistas en la entrada",
                "Trastero de 12 m² incluido",
                "Entrega inmediata · libre al firmar",
            ],
            "highlights": [
                ("Edificio", "1932 · portería 24/7"),
                ("Balcón", "7 m² vistas verdes"),
                ("Parqué", "Original restaurado"),
                ("Planta", "3ª con ascensor"),
            ],
            "description":
                "Piso en uno de los edificios emblema de la Crocetta, "
                "calle tranquila a doscientos metros del corso Galileo "
                "Ferraris. Distribución clásica: recibidor, salón con "
                "balcón, cocina comedor, pasillo, dos dormitorios "
                "dobles, baño con ventana. Parqué original en perfecto "
                "estado, instalaciones renovadas en 2019.",
            "agent_name":  "Silvia Mondelli",
            "agent_role":  "Responsable Turín",
            "agent_phone": "+39 011 5328 4401",
        },
        {
            "slug":       "quadrilocale-isola-milano",
            "title":      "Cuatro dormitorios con vistas al BAM · Isola",
            "price":      "780.000 €",
            "area":       "Milano · Isola · Via Confalonieri 25",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "135",
            "energy":     "A3",
            "floor":      "8ª (doble ascensor)",
            "badge":      "Vistas al parque",
            "reference":  "MI-1915",
            "year_built": "2019",
            "lead":
                "Piso en residencia de diseño de 2019, orientación "
                "principal a la Biblioteca de los Árboles. Cuatro "
                "dormitorios, dos baños, balcón habitable de once "
                "metros. Calificación A3, domótica de serie.",
            "summary": [
                "Vista parque BAM desde el salón",
                "Balcón habitable de 11 m²",
                "Comunidad con conserje 24 h",
                "Plaza de garaje incluida · punto de carga VE",
                "Calificación A3 · aire acondicionado integrado",
            ],
            "highlights": [
                ("Vistas", "BAM y Bosco Verticale"),
                ("Conserje", "24 h en portería"),
                ("Recarga", "Punto VE incluido"),
                ("Calificación", "A3 · bomba de calor"),
            ],
            "description":
                "Octava planta en residencia firmada Piuarch con "
                "conserje 24 h, gimnasio comunitario y jardín "
                "interior. Piso en esquina con doble orientación: "
                "salón hacia el parque BAM, zona de noche al patio "
                "interior. Terraza-loggia de once metros utilizable "
                "nueve meses al año. Mobiliario a medida incluido.",
            "agent_name":  "Sofia Ranieri",
            "agent_role":  "Agente · Milán Norte",
            "agent_phone": "+39 02 8765 4324",
        },
        {
            "slug":       "bilocale-porta-nuova",
            "title":      "Dos dormitorios smart · Porta Nuova",
            "price":      "520.000 €",
            "area":       "Milano · Porta Nuova · Via Melchiorre Gioia 62",
            "rooms":      "2",
            "bathrooms":  "1",
            "surface":    "68",
            "energy":     "A2",
            "floor":      "12ª (vistas a Unicredit)",
            "badge":      "Gran inversión",
            "reference":  "MI-1967",
            "year_built": "2015",
            "lead":
                "Dos dormitorios con 80 % de exposición sur, vistas "
                "al parque y a los rascacielos de Porta Nuova. Ideal "
                "para primera compra o inversión buy-to-let, "
                "rentabilidad bruta estimada 4,2 %.",
            "summary": [
                "Orientación sur · luz todo el día",
                "Vistas a torre Unicredit y Diamante",
                "Conserje de zona · gimnasio comunitario",
                "Rentabilidad buy-to-let estimada 4,2 % bruto",
                "Entrega inmediata · libre al firmar",
            ],
            "highlights": [
                ("Orientación", "Pleno sur"),
                ("Planta", "12ª vistas al skyline"),
                ("Rentabilidad", "4,2 % bruto estimado"),
                ("Libre", "Al firmar"),
            ],
            "description":
                "Piso de 68 m² con salón-cocina de 32 m² vistas al "
                "skyline, dormitorio principal con vestidor, baño con "
                "ventana en piedra gris. Comunidad con servicios, "
                "gimnasio y lounge, conserjería diurna siete días a "
                "la semana. Ideal para quien trabaja en las torres "
                "vecinas o busca una inversión rentable.",
            "agent_name":  "Giulia Ferrante",
            "agent_role":  "Agente sénior · Milán Centro",
            "agent_phone": "+39 02 8765 4322",
        },
        {
            "slug":       "villa-bellagio-lago",
            "title":      "Villa de época con vista Spartivento · Bellagio",
            "price":      "1.950.000 €",
            "area":       "Como · Bellagio · Via Garibaldi 12",
            "rooms":      "6",
            "bathrooms":  "4",
            "surface":    "320",
            "energy":     "E",
            "floor":      "Villa independiente · 3 niveles + torre",
            "badge":      "Villa histórica",
            "reference":  "CO-0248",
            "year_built": "1908 · restauración conservativa 2017",
            "lead":
                "Villa modernista en Punta Spartivento, 320 metros "
                "cubiertos más torre mirador, jardín aterrazado con "
                "acceso privado al lago. Restauración de 2017 con "
                "climatización e instalaciones actualizadas.",
            "summary": [
                "Punta Spartivento · doble vista al lago",
                "Jardín aterrazado con acceso privado al lago",
                "Torre mirador panorámica a 360°",
                "Restauración 2017 con instalaciones contemporáneas",
                "Seis dormitorios, cuatro baños, bodega histórica",
            ],
            "highlights": [
                ("Ubicación", "Punta Spartivento"),
                ("Vistas", "Doble al lago"),
                ("Acceso", "Privado al lago"),
                ("Torre", "Mirador 360°"),
            ],
            "description":
                "Villa símbolo del modernismo del Lario, diseñada por "
                "el arquitecto Pietro Lingeri en 1908. Tres niveles "
                "habitables más torre mirador, orientación este al "
                "ramal de Lecco y oeste al de Como. La restauración "
                "de 2017 preservó los estucos originales, las "
                "vidrieras modernistas y los suelos de terrazo "
                "veneciano, integrando calefacción radiante y "
                "climatización oculta.",
            "agent_name":  "Andrea Colombo",
            "agent_role":  "Agente sénior · Lago de Como",
            "agent_phone": "+39 031 2345 6789",
        },
        {
            "slug":       "appartamento-borgo-po-torino",
            "title":      "Piso con vistas a los Alpes · Borgo Po",
            "price":      "560.000 €",
            "area":       "Torino · Borgo Po · Corso Casale 102",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "145",
            "energy":     "D",
            "floor":      "5ª (última · ascensor)",
            "badge":      "Vistas a la colina",
            "reference":  "TO-0945",
            "year_built": "1928 · piso reformado 2021",
            "lead":
                "Última planta con vistas abiertas a la Mole, el "
                "Monte dei Cappuccini y los Alpes. Ciento cuarenta "
                "y cinco metros en un único nivel, dos balcones "
                "habitables, distribución clásica perfectamente "
                "conservada.",
            "summary": [
                "Vistas a los Alpes y la Mole Antonelliana desde el salón",
                "Dos balcones habitables · 6 + 4 m²",
                "Techos de 3,20 m con estucos originales",
                "Reforma 2021 · instalaciones nuevas",
                "Trastero y buhardilla de 18 m² incluidos",
            ],
            "highlights": [
                ("Vistas", "Alpes y Mole"),
                ("Planta", "5ª, última"),
                ("Techos", "3,20 m con estuco"),
                ("Balcones", "Dos habitables"),
            ],
            "description":
                "Última planta en esquina en edificio de los años "
                "veinte restaurado en 2020, cuatro dormitorios en "
                "un único nivel, doble orientación al corso Casale "
                "y a via Villa della Regina. Zona de día orientada "
                "a la Mole, zona de noche hacia la colina. Estucos "
                "originales conservados en todas las estancias.",
            "agent_name":  "Luca Benedetti",
            "agent_role":  "Agente · Turín Colinas",
            "agent_phone": "+39 011 5328 4402",
        },
        {
            "slug":       "villa-monza-brianza",
            "title":      "Villa independiente con parque · Monza",
            "price":      "1.050.000 €",
            "area":       "Monza · San Fruttuoso · Via Buonarroti 48",
            "rooms":      "6",
            "bathrooms":  "4",
            "surface":    "280",
            "energy":     "B",
            "floor":      "Villa independiente · 3 niveles",
            "badge":      "Parque privado",
            "reference":  "MB-0177",
            "year_built": "2001 · rehabilitación 2022",
            "lead":
                "Villa independiente sobre parcela de mil doscientos "
                "metros, parque arbolado con árboles de gran porte, "
                "piscina climatizada y zona de juegos infantiles. "
                "Tres niveles habitables más sala y zona fitness.",
            "summary": [
                "Parque privado de 1.200 m² con piscina climatizada",
                "Seis dormitorios · cuatro baños · estudio · sala",
                "Zona fitness y sauna en la planta sótano",
                "Calificación B tras aislamiento 2022 · fotovoltaica 12 kW",
                "Box triple y plaza de invitados cubierta",
            ],
            "highlights": [
                ("Parque", "1.200 m² arbolado"),
                ("Piscina", "Climatizada · 10 × 4,5"),
                ("Fitness", "Sauna · gimnasio en sótano"),
                ("Calificación", "B · fotovoltaica 12 kW"),
            ],
            "description":
                "La villa se encuentra en zona residencial a diez "
                "minutos del centro de Monza y a veinte de la Milán "
                "del norte. Proyecto de 2001 de gran calidad, "
                "rehabilitación de 2022 con aislamiento, carpinterías "
                "triple vidrio, instalación fotovoltaica. Planta baja "
                "con zona de día de ciento veinte metros al parque, "
                "planta primera con cuatro dormitorios y tres baños, "
                "buhardilla con estudio y dormitorio de invitados.",
            "agent_name":  "Davide Orsini",
            "agent_role":  "Agente · Monza y Brianza",
            "agent_phone": "+39 039 5328 4403",
        },
        {
            "slug":       "monolocale-navigli-milano",
            "title":      "Estudio de autor con vistas a la alzaia · Navigli",
            "price":      "295.000 €",
            "area":       "Milano · Navigli · Alzaia Naviglio Grande 76",
            "rooms":      "1",
            "bathrooms":  "1",
            "surface":    "42",
            "energy":     "C",
            "floor":      "2ª (escalera de caracol histórica)",
            "badge":      "Frente al canal",
            "reference":  "MI-1994",
            "year_built": "1898 · restauración 2018",
            "lead":
                "Estudio de cuarenta y dos metros con ventanal a la "
                "alzaia del Naviglio Grande, restauración conservativa "
                "de 2018 firmada por Studio Ca' Rossa. Ideal para "
                "primera compra o inversión de alquiler de corta estancia.",
            "summary": [
                "Frente directo a la alzaia · ventanal 2 × 1,5",
                "Edificio de 1898 · escalera de caracol original",
                "Cocina Boffi integrada · baño en piedra serena",
                "Ideal para inversión de corta estancia",
                "Rentabilidad estimada 5,8 % bruto",
            ],
            "highlights": [
                ("Vistas", "Naviglio Grande"),
                ("Edificio", "1898 escalera histórica"),
                ("Rentabilidad", "5,8 % bruto"),
                ("Uso", "Corta estancia / primera vivienda"),
            ],
            "description":
                "Estudio ubicado en la segunda planta de un edificio "
                "histórico directamente en la alzaia del Naviglio "
                "Grande. Ventanal de doble orientación con ventanas "
                "de guillotina restauradas, suelos originales de "
                "barro cocido pulido, cocina integrada firmada Boffi "
                "y baño en piedra serena. Apto para uso personal o "
                "como inversión: en los últimos tres años el alquiler "
                "de corta estancia se ha mantenido por encima del "
                "5,5 % bruto.",
            "agent_name":  "Marco Lentini",
            "agent_role":  "Agente sénior · Milán Sur",
            "agent_phone": "+39 02 8765 4323",
        },
        {
            "slug":       "attico-centro-torino",
            "title":      "Ático frente al Palazzo Reale · Turín",
            "price":      "780.000 €",
            "area":       "Torino · Centro · Piazzetta Reale 3",
            "rooms":      "3",
            "bathrooms":  "2",
            "surface":    "140",
            "energy":     "C",
            "floor":      "6ª (última · ascensor)",
            "badge":      "Vistas históricas",
            "reference":  "TO-0982",
            "year_built": "1874 · ático creado 2022",
            "lead":
                "Ático con terraza habitable frente al Palazzo "
                "Reale, el Duomo y la Mole Antonelliana. Ciento "
                "cuarenta metros en un solo nivel, creado en la "
                "buhardilla histórica por Studio Isolarchitetti.",
            "summary": [
                "Terraza habitable 24 m² vistas Palazzo Reale",
                "Creado a partir de buhardilla histórica · 2022",
                "Tres dormitorios, dos baños, estudio independiente",
                "Techos abuhardillados con vigas originales vistas",
                "Calificación C tras aislamiento de cubierta 2022",
            ],
            "highlights": [
                ("Vistas", "Palazzo Reale, Mole, Duomo"),
                ("Terraza", "24 m² habitable"),
                ("Vigas", "Originales vistas"),
                ("Calificación", "C post-aislamiento"),
            ],
            "description":
                "Ático creado en la buhardilla de un edificio del "
                "siglo XVII restaurado en 2022 por los Isolarchitetti. "
                "Se mantienen las vigas originales de alerce, el suelo "
                "de barro cocido pulido colocado en espiga, baños en "
                "piedra de Luserna. La terraza panorámica se abre a "
                "Piazzetta Reale y regala doble vista a la Mole y el Duomo.",
            "agent_name":  "Silvia Mondelli",
            "agent_role":  "Responsable Turín",
            "agent_phone": "+39 011 5328 4401",
        },
        {
            "slug":       "loft-isola-milano",
            "title":      "Loft ex-taller con patio · Isola",
            "price":      "680.000 €",
            "area":       "Milano · Isola · Via Borsieri 32",
            "rooms":      "2",
            "bathrooms":  "2",
            "surface":    "115",
            "energy":     "B",
            "floor":      "Baja · patio privado",
            "badge":      "Patio privado",
            "reference":  "MI-2012",
            "year_built": "1927 · recuperación integral 2023",
            "lead":
                "Loft sacado de un antiguo taller con treinta metros "
                "de patio privado, doble altura de cinco metros y "
                "ventanales industriales originales. Recuperación "
                "integral 2023, suelo radiante y fotovoltaica.",
            "summary": [
                "Patio privado de 30 m² · especies mediterráneas",
                "Doble altura 5 m · ventanales industriales",
                "Recuperación 2023 · suelo radiante + fotovoltaica",
                "Loft abierto con suite cerrada · baño ciego de servicio",
                "Calificación B · bomba de calor + 4 kW solar",
            ],
            "highlights": [
                ("Patio", "30 m² privado"),
                ("Altura", "5 m industrial"),
                ("Instalación", "Radiante + solar"),
                ("Calificación", "B · casi autónomo"),
            ],
            "description":
                "El loft nace de la recuperación de un antiguo taller "
                "mecánico de 1927. Volúmenes dejados intactos, "
                "zonificación mínima con suite cerrada por pared "
                "vidriada y cocina-isla en el centro. Patio privado "
                "de treinta metros de uso exclusivo con plantas "
                "trepadoras, zona de cocción exterior integrada, "
                "banco de hormigón pulido. Un trozo de la Milán que "
                "fue y de la que está siendo.",
            "agent_name":  "Sofia Ranieri",
            "agent_role":  "Agente · Milán Norte",
            "agent_phone": "+39 02 8765 4324",
        },
    ],
}

# Phase 2g3.7 · Session 53 · D-047 compliance closing comment:
# All user-visible literals in skin + preview compositions MUST be sourced
# from this content tree (or chrome / dna.content). No "Brera" / "Turín"
# / "Milán" / "habs" / "Reservar visita" / "m²" may appear hard-coded
# in the HTML. Review in every PR touching real-estate/mass-market.
