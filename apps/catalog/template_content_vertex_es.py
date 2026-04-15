"""Vertex — Creative Studio · ES content registry.

Agency live rollout, Phase 2g3.6f · Spanish (peninsular) locale.

Voice contract (Barcelona / Madrid independent creative-studio register):
- Fuera de Serie · AD España · Neo2 · Apartamento · Código register.
  Editorial, curatorial, tono formal.
- Primera persona del plural ("diseñamos", "firmamos", "acompañamos"),
  tono de "usted" implícito — nunca "tú" hacia el cliente.
- Léxico: "sistema de identidad", "manual de marca", "dirección artística",
  "línea editorial", "colección", "señalética", "brief". Nunca sprint /
  KPI / growth (esa es la voz de Aura).
- Nombres propios italianos permanecen (Fondazione Prada, Triennale Milano,
  Adelphi, Maison Gentiluomo, Villa Necchi, Museo del Novecento, Via Tortona 32).
- Publicaciones permanecen (Monocle, Domus, Wallpaper*, Creative Review,
  It's Nice That, Design Week, Eye Magazine, Slanted).
- Autores de citas mantienen el nombre italiano; se traduce el cuerpo.
"""
from __future__ import annotations

from typing import Any


VERTEX_CONTENT_ES: dict[str, Any] = {

    "pages": [
        {"slug": "home",     "label": "Estudio",    "kind": "home"},
        {"slug": "studio",   "label": "Quiénes somos", "kind": "about"},
        {"slug": "capacita", "label": "Capacidades", "kind": "services"},
        {"slug": "lavori",   "label": "Trabajos",    "kind": "project_list"},
        {"slug": "manifesto","label": "Manifiesto",  "kind": "process"},
        {"slug": "contatti", "label": "Contacto",    "kind": "contact"},
    ],

    # ── Site chrome ──────────────────────────────────────────────
    "site": {
        "logo_word":   "Vertex Studio",
        "tag":         "Estudio creativo independiente · Milán",
        "availability":"Nuevos encargos · otoño 2026",
        "nav_cta":     "Solicite el dossier",
        "inquiry_page_slug": "contatti",
        "phone":       "+39 02 4981 2066",
        "email":       "studio@vertex.milano",
        "address":     "Via Tortona 32 · 20144 Milán",
        "hours_compact": "Estudio abierto · mar / jue",
        "license":     "P.IVA 10456770963 · Milán",
        "footer_intro":
            "Estudio creativo independiente fundado en Milán en 2018. "
            "Diseñamos sistemas de identidad, colecciones editoriales y "
            "direcciones artísticas para fundaciones, maisons y casas "
            "editoriales italianas.",
        "foot_clients_label":     "Selected clients · 2018 — 2026",
        "clients_footer_rows": [
            "FONDAZIONE PRADA", "2024",
            "MAISON GENTILUOMO", "2025",
            "ADELPHI EDIZIONI", "2024",
            "TRIENNALE MILANO", "2023",
            "MUSEO DEL '900", "2025",
            "VILLA NECCHI", "2024",
        ],
        "foot_standfirst":
            "Una marca no debería parecer nunca recién salida del estudio. "
            "Un buen sistema visual aguanta la temporada. Un sistema construido "
            "con cuidado aguanta la década.",
        "foot_studio_label":      "El estudio",
        "foot_recognition_label": "Reconocimientos",
        "foot_recognition_rows": [
            "ADI Design Index — 2024",
            "Type Directors Club — 2023",
            "Premio Compasso d'Oro — Mención 2022",
            "European Design Awards — 2022",
        ],
    },

    # ── HOME ─────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Estudio independiente · fundado en 2018 · Milán",
        "headline": "Marcas que <em>pesan</em>, <em>aguantan</em>, <em>duran</em>.",
        "pull_quote":
            "« La marca no es un logo. Es la manera en que una cosa "
            "te mira cuando nadie está hablando de ella. »",
        "intro":
            "Somos un estudio creativo independiente que diseña "
            "sistemas de identidad, colecciones editoriales y "
            "direcciones artísticas para un número reducido de clientes "
            "culturales y de lujo. Acompañamos cada marca desde el "
            "primer brief hasta la última tirada.",
        "primary_cta":   "Solicite el dossier",
        "primary_href":  "contatti",
        "secondary_cta": "Trabajos seleccionados",
        "secondary_href":"lavori",

        # Hero right — editorial cover tile
        "cover": {
            "image":  "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=900&q=80&auto=format&fit=crop",
            "badge":  "Case Study · 01",
            "client_name": "FONDAZIONE PRADA · Colección 2025",
            "title":  "Un sistema editorial para <em>cuatro autores</em> y veintidós títulos.",
            "discipline": "Identidad · editorial",
            "year":   "2025 — 2026",
            "credit_left_label":  "Dirección artística",
            "credit_left_value":  "M. Serafini",
            "credit_right_label": "Rollout",
            "credit_right_value": "Oct 2025",
        },

        # Ledger
        "ledger_heading":   "Trabajos <em>recientes</em>",
        "ledger_link":      "Archivo completo →",
        "ledger_page_slug": "lavori",
        "ledger_rows": [
            ("01", "Colección Narrativa Italiana", "Adelphi Edizioni",      "Identidad y editorial",  "2025", "adelphi-collana-narrativa"),
            ("02", "Rebranding de la Fondazione", "Fondazione Prada",      "Dirección artística",     "2025", "fondazione-prada-rebrand"),
            ("03", "Manual de marca integrado",   "Maison Gentiluomo",     "Branding de lujo",        "2024", "maison-gentiluomo-manuale"),
            ("04", "Señalética y wayfinding",     "Triennale Milano",      "Identidad espacial",      "2024", "triennale-milano-wayfinding"),
            ("05", "Serie de carteles de autor",  "Museo del Novecento",   "Dirección artística",     "2024", "museo-900-manifesti"),
            ("06", "Packaging seis cuvées",       "Villa Necchi Winery",   "Packaging de autor",      "2023", "villa-necchi-sei-cuvee"),
        ],

        # Capacità
        "capab_label":   "Capacidades del estudio",
        "capab_heading": "Cuatro <em>disciplinas</em>, una sola dirección.",
        "capab_intro":
            "Trabajamos sobre cuatro ejes que se entrelazan en cada "
            "proyecto: identidad de marca, líneas editoriales, dirección "
            "artística y campañas. No somos una agencia de servicio — "
            "somos un estudio que construye sistemas.",
        "capab_items": [
            ("01", "Identidad de marca",
             "Logo, sistema tipográfico, paleta, retícula, manual. "
             "Desde la primera entrega al rollout sobre tangibles, "
             "en seis o doce semanas.",
             ["Logotipo", "Manual", "Tipografía curada", "Retícula"]),
            ("02", "Líneas editoriales",
             "Colecciones, revistas, catálogos, libros de autor. "
             "Construimos la retícula, elegimos los caracteres, "
             "seguimos la imprenta.",
             ["Colecciones", "Revistas", "Catálogos", "Libros"]),
            ("03", "Dirección artística",
             "Campañas de temporada, producciones de autor, "
             "carteles, materiales POP. De la moodboard "
             "a la toma, hasta la imprenta.",
             ["Campañas", "Producciones", "Carteles", "Motion"]),
            ("04", "Sistemas visuales",
             "Señalética, wayfinding, montajes, "
             "ambientes expositivos. Identidades que se "
             "habitan, no que se miran.",
             ["Wayfinding", "Señalética", "Montaje", "Exposiciones"]),
        ],

        # Press
        "press_heading": "Publicado <em>y reconocido</em>.",
        "press_intro":
            "La nuestra es una práctica pequeña, deliberada, "
            "que elige los proyectos con cuidado. Pero cuando un trabajo "
            "aguanta, el trabajo se hace notar.",
        "press_publications": [
            "Monocle", "Domus", "Wallpaper*", "Creative Review",
            "It's Nice That", "Design Week", "Eye Magazine", "Slanted",
        ],

        # Manifesto
        "manifesto_label":   "Manifiesto breve",
        "manifesto_heading": "Una marca <em>no se decora</em>. Se construye.",
        "manifesto_drop_cap": "U",
        "manifesto_body":
            "n buen proyecto parte de una pregunta que nadie "
            "tiene todavía el coraje de hacer. Diseñar una marca "
            "no significa empaquetar lo que un cliente ya "
            "cree saber de sí mismo — significa ayudarlo a "
            "reconocer aquello que ya sabe pero que aún no "
            "ha nombrado. Por eso no aceptamos encargos "
            "de impulso. Por eso cada relación comienza con "
            "una conversación, nunca con un presupuesto.",
        "manifesto_principles": [
            ("01", "La forma <em>sigue a la voz</em>",
             "La elección tipográfica viene después de la elección del tono. "
             "Primero se decide cómo habla una marca, luego cómo aparece."),
            ("02", "El sistema <em>antes que la imagen</em>",
             "Diseñamos reglas, no aplicaciones. La tarea "
             "de una buena regla es hacerse olvidar."),
            ("03", "El papel <em>aguanta el tiempo</em>",
             "Cada proyecto debe superar al menos dos temporadas "
             "de tendencia sin perder posición. De lo contrario es decoración."),
            ("04", "El cliente <em>es coautor</em>",
             "Trabajamos con quien tiene voz. Quien busca un servicio "
             "silencioso encontrará una respuesta amable pero firme."),
        ],

        # Inquiry CTA
        "cta_label":   "Próximo paso",
        "cta_heading": "Un brief bien hecho <em>vale seis semanas</em>.",
        "cta_sub":
            "Respondemos en tres días laborables con un breve "
            "dossier de lectura del proyecto.",
        "cta_primary": "Solicite el dossier",
    },

    # ── STUDIO (about) ───────────────────────────────────────────
    "studio": {
        "eyebrow":   "El estudio · ocho años",
        "headline":  "Cuarenta metros cuadrados de papel, pruebas de imprenta <em>y caracteres aún por elegir</em>.",
        "standfirst":
            "Somos tres directores creativos, dos diseñadores sénior, "
            "una project manager y un fotógrafo que pasa por aquí "
            "tres veces a la semana. El estudio ha cumplido ocho "
            "aniversarios, treinta y dos proyectos que han cambiado "
            "de casa, y un archivo de pruebas de imprenta que ya "
            "no cabe detrás de la puerta.",

        "facts": [
            ("8",    "años de actividad",     "Fundado en 2018 en Milán"),
            ("42",   "proyectos en archivo",  "De los cuales 22 publicados"),
            ("6",    "colaboradores",         "Tres socios · tres sénior"),
            ("2",    "temporadas de rollout", "El tiempo medio de una marca"),
        ],

        "essay_label":   "Historia del estudio",
        "essay_heading": "Empezamos con <em>un carácter y una pregunta</em>.",
        "essay_paragraphs": [
            "Vertex nace en 2018 de una idea de Margherita Serafini "
            "y Tommaso Boeri, compañeros de curso en la ISIA de Urbino "
            "y luego colaboradores en dos estudios milaneses. La pregunta "
            "de partida era muy sencilla: <em>¿por qué tantas marcas "
            "italianas son bellísimas al descubrirlas y olvidables "
            "después de dos meses?</em>",
            "La respuesta — llegada lentamente, proyecto a proyecto — "
            "es que la mayoría de las marcas se diseñan como se "
            "viste un escaparate: se elige aquello que se ve primero, "
            "no lo que sostiene el tiempo. Diseñar un sistema de "
            "marca que aguante ocho años no es una cuestión de "
            "tendencias, sino de decisiones que se retiran cuando conviene.",
        ],
        "essay_pullquote":
            "Un manual bien hecho no describe la marca. "
            "La defiende de nuestras propias ganas de cambiarla.",
        "essay_tail_paragraphs": [
            "Hoy el estudio trabaja de media con ocho clientes al año. "
            "Rechazamos más de la mitad de los briefs que recibimos — no por "
            "oficio, sino por honestidad: un proyecto mal hecho hace daño "
            "dos veces, al cliente y al portfolio.",
            "Hemos elegido permanecer pequeños. No tenemos ambiciones "
            "de escala. Queremos seguir respondiendo personalmente "
            "a cada primer correo, seguir cada prueba de imprenta, "
            "conocer el nombre de los tipógrafos que imprimen nuestros libros.",
        ],

        "partners_label":   "Los tres socios",
        "partners_heading": "Quién <em>firma</em> el estudio.",
        "partners_intro":
            "Cada proyecto es acompañado por al menos uno de los tres socios "
            "desde el primer brief hasta el rollout final. No delegamos los momentos "
            "decisivos — si una marca arranca bien, es porque había alguien "
            "presente cuando se dijo que no a una primera idea.",
        "partners": [
            {
                "name": "Margherita Serafini",
                "role": "Cofundadora · Directora creativa",
                "bio":  "Diploma en grafica editoriale en la ISIA de Urbino. "
                        "Antes de Vertex, ocho años en Cabinet (Milán) "
                        "como diseñadora sénior. Obsesionada con los caracteres "
                        "serif de la segunda mitad del siglo XX.",
                "portrait": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=900&q=80&auto=format&fit=crop",
                "creds": ["ISIA Urbino", "ADI Design Index 2024", "Docente IED"],
            },
            {
                "name": "Tommaso Boeri",
                "role": "Cofundador · Director artístico",
                "bio":  "Formado en ECAL Lausana. Trabajó para Studio "
                        "Dumbar y M/M Paris antes de volver a Milán. "
                        "Director artístico de dos casas editoriales independientes.",
                "portrait": "https://images.unsplash.com/photo-1568602471122-7832951cc4c5?w=900&q=80&auto=format&fit=crop",
                "creds": ["ECAL Lausana", "TDC Award 2023", "European Design"],
            },
            {
                "name": "Ilaria Ferri",
                "role": "Socia · Directora editorial",
                "bio":  "Licenciada en letras por la Statale de Milán. "
                        "Diez años en Adelphi antes de incorporarse al "
                        "estudio en 2021. Dirige las líneas editoriales "
                        "y la redacción de los manuales.",
                "portrait": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop",
                "creds": ["Statale Milán", "ex Adelphi", "Premio Gutenberg"],
            },
        ],

        "timeline_label":   "Cronología",
        "timeline_heading": "Ocho años <em>en papel</em>.",
        "timeline_rows": [
            ("2018",
             "Apertura del estudio en Via Tortona 32",
             "Primer proyecto: rebrand de la librería independiente Scheiwiller. "
             "Serafini y Boeri firman el primer manual del estudio sobre una hoja A3."),
            ("2020",
             "Primer encargo institucional",
             "Dirección artística para Triennale Milano — veintidós meses de trabajo "
             "sobre la señalética de las salas permanentes."),
            ("2021",
             "Incorporación de Ilaria Ferri como socia",
             "Apertura de la práctica editorial con la primera colección para Adelphi "
             "— nueve títulos publicados en dieciocho meses."),
            ("2023",
             "Reconocimiento ADI Design Index",
             "Premio para la colección Architetture Contemporanee. "
             "Primera portada italiana de Eye Magazine."),
            ("2025",
             "Rebranding Fondazione Prada",
             "Veintidós meses de trabajo. Rollout completo en otoño 2025, "
             "con señalética, editorial, campañas de temporada."),
            ("2026",
             "Apertura de la segunda sala",
             "Ampliación en Via Tortona 34, con archivo de pruebas de imprenta "
             "consultable con cita previa."),
        ],
    },

    # ── CAPACITA (services) ──────────────────────────────────────
    "capacita": {
        "eyebrow":   "Capacidades del estudio",
        "headline":  "Cuatro <em>disciplinas</em> que se entrelazan en cada proyecto.",
        "standfirst":
            "No somos una agencia de servicio completo. Somos un estudio "
            "que trabaja sobre cuatro ejes claros, cada uno con una práctica "
            "estable y un proceso documentado. Cada proyecto toma de "
            "uno o varios de estos ejes — raramente de todos a la vez.",

        "disciplines": [
            {
                "num": "01",
                "title": "Identidad de <em>marca</em>",
                "tagline": "Logo, carácter, retícula, manual. Seis a doce semanas.",
                "body":
                    "Construimos sistemas de identidad que aguantan ocho años. "
                    "Cada rebrand arranca con una conversación con el director "
                    "general o el fundador — nunca con un brief enviado por correo. "
                    "Presentamos tres direcciones, luego una sola. El manual final "
                    "tiene un índice que sirve, no uno que impresiona.",
                "scope_label": "Incluido",
                "scope": [
                    "Logotipo y variaciones",
                    "Sistema tipográfico (retail + display)",
                    "Paleta cromática extendida",
                    "Retícula y reglas compositivas",
                    "Manual de marca (PDF interactivo + impresión)",
                    "Set de aplicaciones (impresión · web · entorno)",
                ],
            },
            {
                "num": "02",
                "title": "Líneas <em>editoriales</em>",
                "tagline": "Colecciones, revistas, catálogos, libros de autor.",
                "body":
                    "La práctica editorial es el corazón del estudio. Diseñamos "
                    "colecciones que aguantan la temporada — la retícula, el formato, "
                    "la caja, las cubiertas. Seguimos la imprenta hasta la prueba "
                    "en máquina, con los tipógrafos de confianza de Milán y Bérgamo. "
                    "Estamos presentes en todos los primeros libros de cada colección firmada.",
                "scope_label": "Incluido",
                "scope": [
                    "Diseño del formato y caja",
                    "Cubierta (sistema + aplicación)",
                    "Configuración tipográfica retail",
                    "Asesoría de imprenta y papel",
                    "Seguimiento de imprenta del primer título",
                    "Ficha de aplicación para la oficina gráfica interna",
                ],
            },
            {
                "num": "03",
                "title": "Dirección <em>artística</em>",
                "tagline": "Campañas, producciones de autor, carteles.",
                "body":
                    "Dirigimos campañas de temporada para maisons y marcas "
                    "italianas con un enfoque editorial — nunca publicitario. "
                    "Elegimos a los fotógrafos, construimos la moodboard, "
                    "seguimos la producción. Las campañas nacen para aguantar "
                    "dos ciclos editoriales — no una semana de redes sociales.",
                "scope_label": "Incluido",
                "scope": [
                    "Concepto de temporada (PDF de lectura · 24 páginas)",
                    "Casting fotográfico + dirección",
                    "Dirección del día de producción",
                    "Selección y postproducción",
                    "Sistema de aplicación (impresión · digital · retail)",
                    "Carteles + colaterales de lanzamiento",
                ],
            },
            {
                "num": "04",
                "title": "Sistemas <em>espaciales</em>",
                "tagline": "Señalética, wayfinding, montaje.",
                "body":
                    "Cuando una identidad se vuelve lugar, la proyectamos "
                    "junto al arquitecto. Wayfinding permanente para "
                    "museos y fundaciones, montajes temporales de "
                    "exposiciones, señalética para retail de lujo. Cada sistema "
                    "espacial arranca con una visita. Nunca trabajamos desde renders.",
                "scope_label": "Incluido",
                "scope": [
                    "Visita y entrega técnica",
                    "Retícula de lectura del espacio",
                    "Sistema tipográfico + pictográfico",
                    "Planos ejecutivos para producción",
                    "Colaboración con estudio de arquitectura",
                    "Presencia en obra · primera instalación",
                ],
            },
        ],

        "engagement_label":   "Tres modos de trabajo",
        "engagement_heading": "Del <em>proyecto puntual</em> al <em>socio editorial</em>.",
        "engagement_intro":
            "Aceptamos tres tipos de encargo. Los diseñamos junto al "
            "cliente en fase de brief — no hay tarifarios ocultos.",
        "engagement_tiles": [
            {
                "title":  "Proyecto <em>puntual</em>",
                "range":  "Doce — veinticuatro semanas",
                "body":   "Una identidad o una línea editorial, del brief al rollout. "
                          "Para marcas que necesitan un gesto nítido y definido.",
                "includes": [
                    "Brief conjunto + tres direcciones",
                    "Rollout en tres aplicaciones",
                    "Manual de marca en italiano / inglés",
                    "Presencia en el lanzamiento",
                ],
            },
            {
                "title":  "Encargo <em>de temporada</em>",
                "range":  "Seis — doce meses · contrato renovable",
                "body":   "Dirección artística de temporada para maisons o instituciones. "
                          "Dos campañas al año, con todas las aplicaciones.",
                "includes": [
                    "Campaña primavera / otoño",
                    "Colaterales de lanzamiento",
                    "Presencia mensual en el estudio",
                    "Archivo compartido",
                ],
            },
            {
                "title":  "Socio <em>editorial</em>",
                "range":  "Compromiso anual · por invitación",
                "body":   "Presencia constante en la mesa editorial del cliente. "
                          "Para casas editoriales, fundaciones, instituciones culturales.",
                "includes": [
                    "Participación en el plan editorial",
                    "Dirección en todas las salidas del año",
                    "Asesoría de imprenta y papel",
                    "Archivo + respaldo creativo",
                ],
            },
        ],

        "cta_label":   "Brief gratuito",
        "cta_heading": "Un primer <em>té juntos</em> no cuesta nada.",
        "cta_primary": "Solicite el dossier",
    },

    # ── LAVORI (project_list) ────────────────────────────────────
    "lavori": {
        "eyebrow":   "Archivo de trabajos · 2018 — 2026",
        "headline":  "Cuarenta y dos proyectos <em>en archivo</em>, veintidós en vitrina.",
        "standfirst":
            "Una selección razonada. No mostramos todo — no todo "
            "aguanta la relectura. El archivo completo está disponible a "
            "petición, en formato PDF imprimible (ciento seis páginas).",
        "filters": ["Todos", "Identidad", "Editorial", "Dirección artística", "Sistemas espaciales"],

        "projects": [
            {
                "slug":       "fondazione-prada-rebrand",
                "index":      "01",
                "title":      "Rebranding de la Fondazione",
                "client":     "Fondazione Prada — Milán",
                "discipline": "Dirección artística",
                "year":       "2025",
            },
            {
                "slug":       "adelphi-collana-narrativa",
                "index":      "02",
                "title":      "Colección Narrativa Italiana",
                "client":     "Adelphi Edizioni — Milán",
                "discipline": "Identidad y editorial",
                "year":       "2025",
            },
            {
                "slug":       "maison-gentiluomo-manuale",
                "index":      "03",
                "title":      "Manual de marca integrado",
                "client":     "Maison Gentiluomo — Florencia",
                "discipline": "Branding de lujo",
                "year":       "2024",
            },
            {
                "slug":       "triennale-milano-wayfinding",
                "index":      "04",
                "title":      "Señalética y wayfinding permanente",
                "client":     "Triennale Milano — Parco Sempione",
                "discipline": "Identidad espacial",
                "year":       "2024",
            },
            {
                "slug":       "museo-900-manifesti",
                "index":      "05",
                "title":      "Serie de carteles de autor",
                "client":     "Museo del Novecento — Milán",
                "discipline": "Dirección artística",
                "year":       "2024",
            },
            {
                "slug":       "villa-necchi-sei-cuvee",
                "index":      "06",
                "title":      "Packaging seis cuvées de autor",
                "client":     "Villa Necchi Winery — Valpolicella",
                "discipline": "Packaging",
                "year":       "2023",
            },
        ],

        "archive_label":   "Archivo completo",
        "archive_heading": "Disponible <em>a petición</em>, ciento seis páginas.",
        "archive_body":
            "El archivo completo contiene cuarenta y dos proyectos desde 2018, "
            "con proceso de trabajo, muestras de impresión, notas "
            "editoriales y coordenadas del cliente.",
        "archive_stats": [
            ("42",   "proyectos en archivo"),
            ("22",   "publicados"),
            ("8",    "años de práctica"),
            ("<em>6</em>", "clientes al año de media"),
        ],
    },

    # ── MANIFESTO (process) ──────────────────────────────────────
    "manifesto": {
        "eyebrow":   "Nuestra manera de trabajar",
        "headline":  "Seis semanas para <em>comprender</em>. Diez para <em>construir</em>. Dos para <em>defender</em>.",
        "standfirst":
            "Cada proyecto atraviesa cuatro fases declaradas. "
            "No nos gustan las sorpresas — ni para nosotros, ni para el "
            "cliente. El calendario es público desde el primer día.",

        "phases": [
            {
                "num": "01",
                "duration": "Semanas 1 — 6",
                "title": "<em>Escucha</em> · lecturas · visita",
                "tagline": "Comprender antes de diseñar.",
                "body":
                    "Nos reunimos con el director general, con el responsable de comunicación "
                    "y, cuando es posible, con los clientes. Leemos el archivo, los estudios "
                    "previos, las memorias anuales. Visitamos los espacios. En esta fase no "
                    "se propone ninguna forma — solo una lectura escrita "
                    "de 24-32 páginas que se convierte en la base del proyecto.",
                "deliverables_label": "Entregas",
                "deliverables": [
                    "Dossier de lectura (24-32 páginas PDF)",
                    "Tres territorios estratégicos por explorar",
                    "Tabla de referencia histórica",
                    "Calendario detallado de las siguientes entregas",
                ],
            },
            {
                "num": "02",
                "duration": "Semanas 7 — 14",
                "title": "<em>Hipótesis</em> · tres direcciones",
                "tagline": "Tres propuestas, ninguna comprometida.",
                "body":
                    "Presentamos tres direcciones creativas plenamente construidas — "
                    "no tres variantes de una misma intuición. Cada dirección tiene "
                    "logo, carácter, dos aplicaciones piloto. El cliente elige "
                    "una dirección (o pide una cuarta ronda — sucede raramente).",
                "deliverables_label": "Entregas",
                "deliverables": [
                    "Tres direcciones creativas (24 láminas cada una)",
                    "Una aplicación piloto por dirección",
                    "Lectura comparada escrita",
                    "Presentación en estudio · media jornada",
                ],
            },
            {
                "num": "03",
                "duration": "Semanas 15 — 22",
                "title": "<em>Construcción</em> · sistema y manual",
                "tagline": "De la dirección al manual, sin perder el tono.",
                "body":
                    "La dirección elegida se desarrolla en un sistema completo: "
                    "retícula, paleta extendida, variaciones de la marca, reglas "
                    "compositivas, manual final. En paralelo construimos "
                    "tres a cinco aplicaciones muestra para probar el sistema "
                    "sobre casos reales.",
                "deliverables_label": "Entregas",
                "deliverables": [
                    "Sistema de marca completo (archivo fuente)",
                    "Manual de marca (PDF interactivo + versión impresa)",
                    "Tres a cinco aplicaciones muestra",
                    "Tipografías retail + licencias documentadas",
                ],
            },
            {
                "num": "04",
                "duration": "Semanas 23 — 24",
                "title": "<em>Rollout</em> · defensa · cierre",
                "tagline": "El manual toma vida, nosotros permanecemos cerca.",
                "body":
                    "Acompañamos el rollout sobre las primeras aplicaciones reales "
                    "con presencia en el estudio y asesoría al equipo interno del "
                    "cliente. Seguimos la primera tirada importante. Cerramos "
                    "con una reunión de handover documentada, donde el "
                    "responsable interno se convierte en custodio del sistema.",
                "deliverables_label": "Entregas",
                "deliverables": [
                    "Presencia en el lanzamiento público",
                    "Primeras aplicaciones seguidas personalmente",
                    "Reunión de handover + documento de gobernanza",
                    "Seis meses de disponibilidad para aclaraciones",
                ],
            },
        ],

        "principles_label":   "Principios de estudio",
        "principles_heading": "<em>Siete</em> compromisos innegociables.",
        "principles": [
            ("01", "Un <em>capítulo a la vez</em>",
             "Nunca dos fases juntas. Un cliente que acelera una fase compromete la siguiente. Hemos rescindido más de un contrato por este principio."),
            ("02", "<em>Tres direcciones</em>, nunca cuatro",
             "Cuatro direcciones vuelven arbitraria la elección. Tres obligan a un razonamiento. Dos serían perezosas."),
            ("03", "El <em>carácter</em> se licencia",
             "No usamos tipografías gratuitas en proyectos pagados. Cada licencia se documenta al cliente, con presupuesto aparte."),
            ("04", "La <em>imprenta</em> se presencia",
             "El primer arranque de máquina en cada rollout importante es seguido por un socio del estudio."),
            ("05", "El <em>cliente</em> es coautor",
             "El cliente firma el manual junto al estudio. No es un servicio — es un proyecto compartido."),
            ("06", "<em>No</em> forma parte del servicio",
             "Decimos que no más de lo que proponemos. Es el principal valor que aportamos."),
        ],

        "promise_label":   "Nuestros números",
        "promise_heading": "Pequeños <em>por elección</em>, lentos <em>por método</em>.",
        "promise_stats": [
            ("<em>6</em>",       "clientes al año de media",
             "Más de 12 briefs recibidos al mes, menos de 6 aceptados al año."),
            ("<em>8</em>",       "años de duración media",
             "Las identidades firmadas entre 2018 y 2022 siguen todas activas."),
            ("<em>3 d</em>",    "respuesta al primer brief",
             "En tres días laborables recibirá una primera lectura escrita del proyecto."),
        ],
    },

    # ── CONTATTI (contact) ───────────────────────────────────────
    "contatti": {
        "eyebrow":   "Solicite el dossier",
        "headline":  "Cuéntenos <em>el proyecto</em>. Respondemos en tres días.",
        "standfirst":
            "Cada correo llega directamente a Margherita o Tommaso. "
            "No hay un account manager que filtre — quien le responde es "
            "quien acompañará el proyecto en primera persona, si deciden "
            "trabajar juntos.",

        "form_heading": "Brief del proyecto",
        "labels": {
            "name":       "Nombre y apellidos",
            "role":       "Cargo en la organización",
            "company":    "Organización / marca",
            "email":      "Correo de contacto",
            "discipline": "Disciplina principal solicitada",
            "budget":     "Banda de presupuesto indicativa",
            "brief":      "Relato del proyecto",
        },
        "placeholders": {
            "name":    "Nombre Apellidos",
            "role":    "p. ej. Director de comunicación",
            "company": "Nombre de la organización",
            "email":   "nombre@organizacion.es",
            "brief":   "Quién es, qué está tratando de construir, en qué plazo, con qué equipo interno. Cuanto más concreto, más útil será la respuesta.",
        },
        "discipline_options": [
            "Identidad de marca (rebrand)",
            "Identidad de marca (primer lanzamiento)",
            "Línea editorial · colección",
            "Dirección artística · campaña",
            "Sistema espacial · wayfinding",
            "Todavía no estoy seguro — hablémoslo",
        ],
        "budget_bands": [
            ("12k",  "< 12 K€"),
            ("40k",  "12 — 40 K€"),
            ("120k", "40 — 120 K€"),
            ("120plus","> 120 K€"),
        ],
        "form_submit_label": "Enviar el brief",
        "form_submit_note":  "Respondemos en tres días laborables con una primera lectura.",

        "direct_label":   "Correo directo",
        "direct_heading": "Escriba a <em>Margherita</em> y <em>Tommaso</em>.",

        "studio_label":   "El estudio",

        "reply_label":    "Tiempos de respuesta",
        "reply_heading":  "Tres <em>días laborables</em>, no más.",
        "reply_body":
            "Cada brief recibe en 72 horas una primera lectura escrita: "
            "le decimos si el proyecto es para nosotros, si el momento es adecuado, "
            "si nos vemos en persona para profundizar. "
            "Nunca respuestas automáticas, nunca presupuestos sin lectura.",

        "channels_label": "Canales",
        "channels": [
            ("Correo",     "studio@vertex.milano"),
            ("Teléfono",   "+39 02 4981 2066"),
            ("Estudio",    "Via Tortona 32 · Milán"),
            ("LinkedIn",   "/company/vertex-milano"),
            ("Are.na",     "/vertex-studio"),
            ("Secretaría", "mar · jue · 10 — 18"),
        ],

        "promise_label":   "Un compromiso",
        "promise_heading":
            "« Nunca enviamos un presupuesto antes de un brief de lectura. "
            "Es un pequeño gesto, pero cambia la conversación. »",
    },

    # ── POSTS (project_detail) ───────────────────────────────────
    "posts": [
        {
            "slug": "fondazione-prada-rebrand",
            "index": "01",
            "title": "Un <em>rebranding institucional</em> que no se hace notar.",
            "client": "Fondazione Prada — Milán",
            "discipline": "Dirección artística · identidad",
            "year": "2025",
            "team": "Serafini · Boeri · Ferri",
            "standfirst":
                "Un rediseño de la identidad institucional pensado para aguantar "
                "veinte años de programación cultural, sin pedir al "
                "visitante que aprenda un vocabulario visual nuevo.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Año de entrega",
            "meta_label_team":       "Equipo del estudio",
            "cover_image": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "El problema",
                    "title": "Una institución <em>leída por error</em>.",
                    "paragraphs": [
                        "Cuando la Fondazione nos llamó, en el primer trimestre de 2024, "
                        "el punto no era la marca — la marca funcionaba. El problema "
                        "era que <em>la identidad ya no acompañaba al programa</em>.",
                        "La Fondazione había publicado cincuenta y dos eventos en 2023, "
                        "pero los comunicados parecían todos <em>una misma institución "
                        "cansada</em>. La culpa no era de la marca. Era del sistema — un "
                        "manual de 2011, pensado para un programa mucho más reducido.",
                    ],
                },
                {
                    "label": "El método",
                    "title": "Diseñar una <em>segunda voz</em>, no un segundo logo.",
                    "paragraphs": [
                        "Elegimos no tocar la marca principal. Diseñamos "
                        "en cambio un <em>sistema editorial paralelo</em> — una "
                        "segunda voz visual, empleada para toda la comunicación del programa. "
                        "La marca institucional permanece, pero se hace a un lado.",
                        "Esta decisión permitió evitar la fractura que acompaña "
                        "a todo rebranding — nadie tuvo que desinstalar nada. "
                        "La nueva voz se acercó a la antigua, ganando espacio "
                        "progresivamente, temporada a temporada.",
                    ],
                    "pullquote":
                        "La marca institucional es una firma. La segunda voz es una manera "
                        "de hablar. Una firma no cambia — la manera de hablar puede evolucionar.",
                },
                {
                    "label": "El resultado",
                    "title": "Una <em>temporada</em>, cincuenta y dos eventos, una sola voz.",
                    "paragraphs": [
                        "La nueva voz editorial se aplicó por primera vez "
                        "en la temporada otoño 2025, sobre cincuenta y dos eventos publicados. "
                        "El equipo interno de comunicación adoptó el sistema con "
                        "seis días de acompañamiento en el estudio. No se rehizo ningún contenido "
                        "— todo fue revestido.",
                    ],
                },
            ],
            "deliverables_label": "Entregas",
            "deliverables_heading": "Cuatro <em>sistemas</em>, un solo manual.",
            "deliverables_intro":
                "El manual final — 184 páginas — fue redactado junto al equipo "
                "de comunicación de la Fondazione, con glosario compartido.",
            "deliverables": [
                ("01", "Sistema editorial secundario",
                 "Tipografía, retícula, paleta de temporada, variaciones regionales. "
                 "Aplicado a todos los materiales del programa — invitaciones, folletos, redes."),
                ("02", "Manual de marca integrado",
                 "184 páginas, italiano + inglés. Contiene los dos sistemas (histórico + nuevo) "
                 "con criterios claros sobre cuándo usar uno u otro."),
                ("03", "Plantillas de producción autónoma",
                 "Archivos fuente listos para la oficina gráfica interna. "
                 "Tres tipologías (invitación, comunicado, folleto) × cuatro temporadas."),
            ],
            "press_quote":
                "Un rebranding casi invisible que ha cambiado el aliento de la institución. "
                "Raro, en Italia, ver a un estudio que elige hacerse a un lado.",
            "press_source":     "Domus — Noviembre 2025",
            "press_journalist": "Giulia Bellini",
            "next_label":       "Próximo caso",
            "next_heading":     "Ir al <em>archivo de trabajos</em> →",
            "cta_label":        "Encargos 2026",
            "cta_heading":      "Abrir el <em>dossier del estudio</em> →",
        },
        {
            "slug": "adelphi-collana-narrativa",
            "index": "02",
            "title": "Una <em>colección</em> para dieciocho voces narrativas.",
            "client": "Adelphi Edizioni — Milán",
            "discipline": "Identidad y editorial",
            "year": "2025",
            "team": "Ferri · Serafini",
            "standfirst":
                "El diseño de una nueva colección narrativa contemporánea para una "
                "casa editorial histórica — dieciocho títulos publicados en dieciocho meses, "
                "con un sistema de cubierta que alterna retrato y abstracción.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Año de publicación",
            "meta_label_team":       "Equipo del estudio",
            "cover_image": "https://images.unsplash.com/photo-1481487196290-c152efe083f5?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "El brief",
                    "title": "Una <em>colección que no parezca</em> una colección.",
                    "paragraphs": [
                        "Adelphi quería abrir un espacio para autores narrativos contemporáneos "
                        "italianos, pero sin traicionar el tono silencioso y meditado de la casa. "
                        "El brief inicial era deliberadamente mínimo: <em>una colección que se "
                        "reconozca sin parecer una colección</em>.",
                    ],
                },
                {
                    "label": "La elección",
                    "title": "Retrato <em>y</em> abstracción, nunca juntos.",
                    "paragraphs": [
                        "Propusimos un sistema que alterna dos registros: cubiertas con "
                        "fotografía (retrato del autor sobre papel trabajado) y cubiertas "
                        "abstractas (composiciones tipográficas con el título solo). La elección "
                        "entre los dos registros queda en manos del director editorial, caso por caso.",
                    ],
                    "pullquote":
                        "El sistema no obliga. Sugiere. La mejor regla editorial "
                        "es aquella que el director puede violar una vez, con razón.",
                },
            ],
            "deliverables_label": "Entregas",
            "deliverables_heading": "Un sistema <em>discreto</em>, dieciocho voces distintas.",
            "deliverables_intro":
                "Cada título es acompañado por Ilaria Ferri en la fase de elección de "
                "cubierta y en la prueba de imprenta, durante las tres primeras temporadas.",
            "deliverables": [
                ("01", "Diseño de formato + caja",
                 "120 × 185 mm, papel Palatina 80 g, rústica con cosido. "
                 "Caja con dos opciones de maquetación para textos densos."),
                ("02", "Sistema de cubierta",
                 "Dos registros alternados (retrato / abstracción) con paleta "
                 "de cuatro colores. Reglas de composición documentadas."),
                ("03", "Primer título · Come ci vedono gli uccelli",
                 "Acompañado desde la primera prueba de imprenta hasta la tirada final, "
                 "con seguimiento en imprenta en Bérgamo."),
            ],
            "press_quote":
                "Una colección que añade sin desplazar. Muy Adelphi, muy nuevo.",
            "press_source":     "Corriere della Sera · La Lettura — Diciembre 2025",
            "press_journalist": "Andrea Pomella",
            "next_label":       "Próximo caso",
            "next_heading":     "Ir al <em>archivo de trabajos</em> →",
            "cta_label":        "Práctica editorial",
            "cta_heading":      "Abrir el <em>dossier editorial</em> →",
        },
        {
            "slug": "maison-gentiluomo-manuale",
            "index": "03",
            "title": "Un <em>manual de marca</em> para la tercera generación.",
            "client": "Maison Gentiluomo — Florencia",
            "discipline": "Branding de lujo",
            "year": "2024",
            "team": "Boeri · Serafini",
            "standfirst":
                "El rediseño integrado de una maison florentina en el relevo "
                "de la tercera generación — un rebranding pensado para custodiar, "
                "no para renovar.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Año de entrega",
            "meta_label_team":       "Equipo del estudio",
            "cover_image": "https://images.unsplash.com/photo-1586717791821-3f44a563fa4c?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "El contexto",
                    "title": "Una <em>maison</em> sin manual.",
                    "paragraphs": [
                        "Gentiluomo era una maison de marroquinería fundada en 1967 "
                        "en Florencia. En la tercera generación — dos hermanas, cuarenta "
                        "y treinta y seis años — la comunicación seguía gestionándose como "
                        "una emergencia semanal. Nada de sistema, nada de reglas, "
                        "nada de archivo.",
                    ],
                },
                {
                    "label": "El método",
                    "title": "Remontarse <em>a 1967</em>, no a 2024.",
                    "paragraphs": [
                        "Pasamos cinco semanas en el archivo de Florencia, "
                        "reconstruyendo pieza por pieza la identidad histórica — catálogos, "
                        "tarjetas, etiquetas, correspondencia con las tiendas. El sistema "
                        "final no es nuevo — es la primera versión documentada de "
                        "algo que existía desde hacía cincuenta y siete años.",
                    ],
                    "pullquote":
                        "La maison ya tenía una identidad. Nadie la había escrito jamás.",
                },
            ],
            "deliverables_label": "Entregas",
            "deliverables_heading": "Un <em>manual custodio</em>, 240 páginas.",
            "deliverables_intro":
                "El manual final fue firmado por las dos hermanas y por el "
                "estudio, en ceremonia privada en Florencia en octubre de 2024.",
            "deliverables": [
                ("01", "Reconstrucción del archivo histórico",
                 "128 piezas catalogadas, escaneadas, descritas. "
                 "Base documental para cada decisión posterior."),
                ("02", "Sistema tipográfico histórico + contemporáneo",
                 "Un serif italiano rediseñado a partir de las etiquetas de 1971, "
                 "acompañado de un sans moderno para la comunicación digital."),
                ("03", "Manual custodio",
                 "240 páginas en italiano + inglés, firmado por las clientes. "
                 "Pensado para ser leído, no para ser consultado."),
            ],
            "press_quote":
                "Un rebranding que custodia en lugar de renovar — una rareza en Florencia.",
            "press_source":     "Monocle — Febrero 2025",
            "press_journalist": "Sophie Grove",
            "next_label":       "Próximo caso",
            "next_heading":     "Ir al <em>archivo de trabajos</em> →",
            "cta_label":        "Maison y lujo",
            "cta_heading":      "Abrir el <em>dossier lujo</em> →",
        },
        {
            "slug": "triennale-milano-wayfinding",
            "index": "04",
            "title": "Un <em>wayfinding permanente</em> para doce salas.",
            "client": "Triennale Milano — Parco Sempione",
            "discipline": "Identidad espacial",
            "year": "2024",
            "team": "Serafini · Boeri",
            "standfirst":
                "El diseño de un sistema de señalética permanente para las "
                "doce salas expositivas de la Triennale — un sistema que "
                "acompaña al visitante sin hablar más de lo necesario.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Año de instalación",
            "meta_label_team":       "Equipo del estudio",
            "cover_image": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "El proyecto",
                    "title": "Una <em>gramática espacial</em> para veintidós meses de trabajo.",
                    "paragraphs": [
                        "La Triennale nos encargó el rediseño del wayfinding "
                        "permanente en 2022. Veintidós meses de trabajo, doce salas, "
                        "cuatro idiomas, dos recorridos (visitante + personal). El sistema "
                        "se instaló por fases, sin cerrar nunca al público.",
                    ],
                },
                {
                    "label": "Las reglas",
                    "title": "Un carácter, tres tamaños, dos colores.",
                    "paragraphs": [
                        "Trabajamos por sustracción: un solo carácter (diseñado "
                        "a medida), tres tamaños (direccional / informativo / "
                        "explicativo), dos colores (negro + ocre). La traducción al árabe "
                        "y al chino fue cuidada con consultores lingüísticos dedicados.",
                    ],
                },
            ],
            "deliverables_label": "Entregas",
            "deliverables_heading": "Un <em>sistema</em>, 420 elementos.",
            "deliverables_intro":
                "La instalación fue seguida en obra por Margherita "
                "Serafini durante tres semanas consecutivas.",
            "deliverables": [
                ("01", "Carácter tipográfico exclusivo",
                 "Triennale Display — diseñado por el estudio, "
                 "licenciado en exclusiva a la Triennale."),
                ("02", "420 elementos de señalética",
                 "Desde el gran direccional exterior hasta la cédula de vitrina. "
                 "Cuatro idiomas, dos recorridos."),
                ("03", "Manual de gestión",
                 "Documento operativo para el equipo interno: qué mantener, "
                 "cuándo sustituir, cómo solicitar nuevos elementos."),
            ],
            "press_quote":
                "Un wayfinding que no impone — te deja caminar.",
            "press_source":     "Abitare — Marzo 2025",
            "press_journalist": "Filippo Romano",
            "next_label":       "Próximo caso",
            "next_heading":     "Ir al <em>archivo de trabajos</em> →",
            "cta_label":        "Sistemas espaciales",
            "cta_heading":      "Abrir el <em>dossier wayfinding</em> →",
        },
        {
            "slug": "museo-900-manifesti",
            "index": "05",
            "title": "Una <em>serie de carteles</em> de autor para doce exposiciones.",
            "client": "Museo del Novecento — Milán",
            "discipline": "Dirección artística",
            "year": "2024",
            "team": "Boeri · Ferri",
            "standfirst":
                "La dirección artística de una temporada de carteles para las "
                "exposiciones temporales del Museo, con comisión a fotógrafos "
                "italianos emergentes.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Año de la temporada",
            "meta_label_team":       "Equipo del estudio",
            "cover_image": "https://images.unsplash.com/photo-1561070791-2526d30994b8?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "La idea",
                    "title": "Un <em>cartel</em>, un <em>autor</em>.",
                    "paragraphs": [
                        "En lugar de producir carteles internamente en el estudio, "
                        "encargamos a doce fotógrafos italianos emergentes — uno por "
                        "exposición — una imagen en respuesta a la obra "
                        "central de la muestra.",
                    ],
                },
                {
                    "label": "El resultado",
                    "title": "Doce voces <em>distintas</em>, una sola retícula.",
                    "paragraphs": [
                        "La retícula tipográfica se mantuvo constante — mismo título, "
                        "mismo crédito, mismo formato. La variación vive enteramente "
                        "en la imagen. El visitante percibe la coherencia de la "
                        "temporada, pero cada cartel es una sorpresa autónoma.",
                    ],
                },
            ],
            "deliverables_label": "Entregas",
            "deliverables_heading": "Una <em>temporada</em>, doce carteles.",
            "deliverables_intro":
                "El proyecto ganó la Mención ADI Design Index 2024.",
            "deliverables": [
                ("01", "Comisión fotográfica",
                 "Doce fotógrafos italianos emergentes elegidos entre los finalistas "
                 "del Premio Graziadei 2023."),
                ("02", "Retícula tipográfica de temporada",
                 "Un diseño de cartel que aguanta doce imágenes distintas "
                 "sin compromisos."),
                ("03", "Catálogo de la temporada",
                 "Recopilación en edición limitada (500 copias) firmada por los doce "
                 "fotógrafos + entrevista con el comisario."),
            ],
            "press_quote":
                "Carteles que no publicitan la exposición — la acompañan.",
            "press_source":     "Eye Magazine — Verano 2024",
            "press_journalist": "John L. Walters",
            "next_label":       "Próximo caso",
            "next_heading":     "Ir al <em>archivo de trabajos</em> →",
            "cta_label":        "Dirección artística",
            "cta_heading":      "Abrir el <em>dossier de temporada</em> →",
        },
        {
            "slug": "villa-necchi-sei-cuvee",
            "index": "06",
            "title": "Un <em>packaging</em> para seis cuvées, seis autores.",
            "client": "Villa Necchi Winery — Valpolicella",
            "discipline": "Packaging de autor",
            "year": "2023",
            "team": "Serafini · Boeri",
            "standfirst":
                "El diseño de seis etiquetas para las seis cuvées históricas "
                "de la bodega, cada una firmada por un autor literario "
                "italiano contemporáneo.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Año de la tirada",
            "meta_label_team":       "Equipo del estudio",
            "cover_image": "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "El proyecto",
                    "title": "Un <em>vino</em>, un <em>texto</em>, una etiqueta.",
                    "paragraphs": [
                        "Seis cuvées históricas de la Villa Necchi. Seis autores italianos "
                        "contemporáneos, invitados a escribir un breve texto (máx. 120 palabras) "
                        "en respuesta al vino que habían degustado. Los textos se "
                        "integraron después tipográficamente en la etiqueta.",
                    ],
                },
                {
                    "label": "Los autores",
                    "title": "Seis voces <em>muy distintas</em>.",
                    "paragraphs": [
                        "Elegimos deliberadamente seis registros distintos: una poeta "
                        "siciliana, un novelista milanés, una crítica literaria, "
                        "un autor de relatos breves, un traductor del japonés, "
                        "una escritora de no-ficción. Cada texto tiene su tipografía.",
                    ],
                },
            ],
            "deliverables_label": "Entregas",
            "deliverables_heading": "Seis <em>etiquetas</em>, seis tipografías.",
            "deliverables_intro":
                "La serie se vendió como estuche de seis botellas "
                "en edición limitada (1200 sets).",
            "deliverables": [
                ("01", "Seis etiquetas de autor",
                 "Impresas en tipografía en Verona sobre papel Amatruda, "
                 "con doble ennoblecimiento (relieve + lámina)."),
                ("02", "Estuche de madera",
                 "Diseñado junto a un carpintero de Valpolicella, "
                 "numerado y firmado por la bodega."),
                ("03", "Libreto de los textos",
                 "Recopilación de los seis textos originales en edición italiana + "
                 "traducción inglesa, cosida con hilo."),
            ],
            "press_quote":
                "Un proyecto que liga el vino a la literatura sin forzar la analogía. Valiente.",
            "press_source":     "Gambero Rosso — Enero 2024",
            "press_journalist": "Marco Sabellico",
            "next_label":       "Próximo caso",
            "next_heading":     "Ir al <em>archivo de trabajos</em> →",
            "cta_label":        "Packaging de autor",
            "cta_heading":      "Abrir el <em>dossier packaging</em> →",
        },
    ],
}
