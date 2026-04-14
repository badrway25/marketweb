"""Chiara — Portfolio Creativo — Spanish (peninsular) content tree.

Phase 2i.2 — Live i18n rollout (Session 37). Mirrors the shape of
``CHIARA_CONTENT_IT`` verbatim and ships the Spanish editorial voice
(AD-led, usted form, Gràffica/Visual magazine register) for the
chiara-portfolio-creativo template.
"""
from __future__ import annotations

from typing import Any


CHIARA_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Estudio",      "kind": "home"},
        {"slug": "studio",     "label": "Quiénes somos","kind": "about"},
        {"slug": "lavoro",     "label": "Trabajo",      "kind": "project_list"},
        {"slug": "processo",   "label": "Proceso",      "kind": "process"},
        {"slug": "contatti",   "label": "Contacto",     "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial":   "C",
        "logo_word":      "Chiara Velluti Studio",
        "logo_short":     "CV",
        "tag":            "Dirección artística · Milán",
        "phone":          "+39 02 8736 4408",
        "email":          "studio@chiaravelluti.it",
        "address":        "Via Tortona 27 · 20144 Milán",
        "hours_compact":  "Lun – Vie · 10:00 – 19:00 · con cita previa",
        "license":        "P. IVA IT 09621460963 · REA MI-2092841",
        "footer_intro":
            "Estudio independiente de dirección artística en Milán. "
            "Identidad de marca, sistemas editoriales y señalética para "
            "instituciones culturales, editoriales y maisons de pequeño "
            "lujo. Fundado en 2014.",
        "foot_studio":   "El estudio",
        "foot_pages":    "Secciones",
        "foot_contact":  "Contacto",
        "foot_clients":  "Han elegido el estudio",
        "clients_footer_rows": [
            "Triennale Milano",
            "Edizioni Adelphi",
            "Fondazione Prada (encargo 2022)",
            "Ateliers Velluti & Co.",
        ],
        # Studio coordinates strip — used in footer + ribbon
        "coordinates": [
            ("Estudio",      "Via Tortona 27 · 20144 Milán"),
            ("Fundadora",    "Chiara Velluti, AD"),
            ("Equipo",       "5 diseñadores · 1 becaria · 2 colaboradores"),
            ("Disciplinas",  "Marca · Edición · Sistemas gráficos"),
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":   "Estudio independiente · 2014 — 2026",
        # Headline kept short per D-052 to avoid hero overflow
        "headline":  "Formas que perduran, <em>una página</em> a la vez.",
        "intro":
            "Diseñamos identidades de marca, libros y sistemas gráficos "
            "para instituciones culturales, editoriales y maisons de "
            "pequeño lujo. El estudio lo dirige la directora artística y "
            "cada proyecto lo sigue personalmente desde la apertura del "
            "expediente hasta la entrega del manual operativo.",
        "primary_cta":   "Solicitar el portfolio completo",
        "primary_href":  "contatti",
        "secondary_cta": "Visitar el estudio",
        "secondary_href":"studio",

        # Hero ledger card footer label + count format (lifted from skin)
        "ledger_full_link_label":   "Todo el archivo",
        "ledger_count_prefix":      "→",
        "ledger_count_unit":        "proyectos",

        # Project ledger preview — 6 indexed rows
        "ledger_label":   "Trabajo seleccionado · 2022 — 2026",
        "ledger_heading": "Seis proyectos, seis disciplinas",
        "ledger_intro":
            "Una selección reciente. El archivo completo reúne 47 proyectos "
            "firmados desde 2014. Para la lista íntegra disponemos de un "
            "PDF de consulta a petición.",
        # Each row: (num, title, discipline, year, medium)
        "ledger_rows": [
            ("01", "Triennale Milano · catálogo 2025",
             "Edición de arte", "2025",
             "Volumen 24 × 32 cm · 412 páginas · impresión offset"),
            ("02", "Adelphi · colección «Carta Bianca»",
             "Identidad de colección", "2024",
             "Sistema tipográfico + 12 cubiertas en serie"),
            ("03", "Fondazione Querini Stampalia · señalética",
             "Señalética & wayfinding", "2024",
             "Sistema bilingüe · latón grabado + impresión directa"),
            ("04", "Maison Lambrate · rebrand",
             "Identidad de marca", "2023",
             "Logotipo + sistema visual + manual de 96 páginas"),
            ("05", "Festival de Pordenone · 38.ª edición",
             "Identidad de evento", "2023",
             "Marca temporal + materiales impresos + señalética"),
            ("06", "Atelier Velluti & Co. · monografía",
             "Edición de estudio", "2022",
             "Volumen 19 × 25 cm · 240 páginas · impresión fine art"),
        ],

        # Capabilities preview (full list on /processo)
        "capabilities_label":   "Disciplinas",
        "capabilities_heading": "Cinco competencias, una sola firma",
        "capabilities_intro":
            "Cada proyecto lo acompaña un equipo multidisciplinar. "
            "No escalamos por el tamaño del cliente — escalamos por la "
            "complejidad del problema.",
        "capabilities": [
            ("Identidad de marca",
             "Identidades completas para instituciones y maisons: "
             "desde la investigación tipográfica al manual operativo."),
            ("Edición & libros",
             "Catálogos de arte, monografías de autor, colecciones "
             "editoriales. Dirección tipográfica y maquetación."),
            ("Sistemas & señalética",
             "Señalética, sistemas gráficos para espacios expositivos, "
             "wayfinding bilingüe y material didáctico museístico."),
            ("Dirección artística",
             "Consultoría AD para equipos internos: revisión de "
             "manuales, auditorías visuales, mentoría al equipo gráfico."),
        ],

        # Selected clients ribbon (text-only wordmarks)
        "clients_label":   "Han elegido el estudio",
        "clients": [
            "TRIENNALE MILANO",
            "ADELPHI EDIZIONI",
            "FONDAZIONE PRADA",
            "MUSEO POLDI PEZZOLI",
            "QUERINI STAMPALIA",
            "FESTIVAL PORDENONE",
            "MAISON LAMBRATE",
            "ATELIER VELLUTI & CO.",
        ],

        # Featured projects — visual grid below the typo hero.
        "featured_works": {
            "label":   "Trabajos en catálogo",
            "heading": "Cuatro proyectos, <em>cuatro disciplinas.</em>",
            "intro":
                "Una selección de 2024 — 2025 — sistemas tipográficos, "
                "identidades institucionales, señalética museística y objetos "
                "editoriales impresos. Pulse para abrir el dossier completo.",
            "items": [
                {
                    "year":       "2025",
                    "discipline": "Catálogo · Edición de arte",
                    "title":      "Triennale Milano 2025",
                    "blurb":      "Dirección tipográfica y maquetación del catálogo principal de la edición.",
                    "image":      "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2024 — 2025",
                    "discipline": "Sistema tipográfico · Editorial",
                    "title":      "Colección «Carta Bianca» · Adelphi",
                    "blurb":      "Sistema editorial para doce títulos — cubiertas, tipografía y código cromático.",
                    "image":      "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2024",
                    "discipline": "Señalética · Identidad museística",
                    "title":      "Querini Stampalia · Venecia",
                    "blurb":      "Señalética permanente de las salas y sistema de llamada para salas de conferencias.",
                    "image":      "https://images.unsplash.com/photo-1564399579883-451a5d44ec08?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2023",
                    "discipline": "Monografía · Edición independiente",
                    "title":      "Atelier Velluti · Lambrate",
                    "blurb":      "Monografía de estudio — 240 páginas, sistema tipográfico a medida, impresión Antiga.",
                    "image":      "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
            ],
            "footer_link":  "Ver todos los proyectos",
            "footer_href":  "lavoro",
        },

        # Press / recognitions — 3 honors
        "press_label":   "Reconocimientos recientes",
        "press_heading": "Premios, exposiciones y publicaciones",
        "press": [
            {
                "year":  "2025",
                "honor": "ADI Design Index",
                "work":  "Catálogo Triennale Milano 2025",
                "note":  "Selección de edición de arte · jurado nacional.",
            },
            {
                "year":  "2024",
                "honor": "European Design Awards · Bronze",
                "work":  "Colección «Carta Bianca» para Adelphi",
                "note":  "Categoría de sistemas tipográficos editoriales.",
            },
            {
                "year":  "2023",
                "honor": "Aiap Design Per · Exposición colectiva",
                "work":  "Monografía Atelier Velluti & Co.",
                "note":  "Expuesta en la Triennale durante cuatro meses.",
            },
        ],

        # Selected commissions — what we accept this year
        "commissions_label":   "Encargos 2026",
        "commissions_heading": "Lo que buscamos este año",
        "commissions_intro":
            "El estudio acepta entre ocho y diez proyectos al año, "
            "elegidos por su complejidad antes que por el tamaño del "
            "cliente. Elegir el encargo es la disciplina más importante "
            "que ejercemos.",
        "commissions": [
            ("Identidades para instituciones culturales",
             "Museos, fundaciones, festivales. Preferimos los encargos "
             "de rebrand estructural a las simples actualizaciones."),
            ("Catálogos de arte y monografías",
             "Editoriales de arte independientes, galerías con programa "
             "editorial, monografías de autor."),
            ("Sistemas gráficos para espacios",
             "Señalética museística, wayfinding bilingüe y sistemas "
             "didácticos para exposiciones temporales."),
        ],

        # Final CTA band
        "cta_label":   "Una conversación preliminar",
        "cta_heading": "Treinta minutos con la AD, sin compromiso",
        "cta_intro":
            "La primera llamada se celebra directamente con Chiara "
            "Velluti. Repasamos el perímetro, el calendario y el "
            "eventual conflicto de agenda — antes de cualquier propuesta.",
        "cta_primary":      "Escríbanos al estudio",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Consultar el trabajo",
        "cta_secondary_href":"lavoro",
    },

    # ─── STUDIO (about) ─────────────────────────────────────────
    "studio": {
        "eyebrow":   "El estudio · 2014 — 2026",
        "headline":  "Un estudio dirigido por la <em>directora artística</em>, doce años de oficio.",
        "intro":
            "Chiara Velluti Studio nace en 2014 en Milán, en un primer "
            "espacio de treinta y cuatro metros cuadrados en Lambrate. "
            "Hoy somos cinco diseñadores, dos colaboradores externos y "
            "una becaria en Via Tortona. Seguimos eligiendo uno a uno "
            "los proyectos.",

        # Founder block (full bio)
        "founder_label":   "Dirección artística",
        "founder_heading": "Chiara Velluti, fundadora",
        "founder": {
            "name":  "Chiara Velluti",
            "role":  "Directora artística · Fundadora",
            "bio":
                "Titulada en Isia Urbino en diseño gráfico, tres años en "
                "Studio Pentagram Nueva York como senior designer (bajo "
                "Paula Scher), cinco años en Studio Sonnoli de Rímini "
                "como asociada. Abre el estudio Velluti en 2014 en Milán. "
                "Enseña diseño tipográfico en el Politecnico desde 2018, "
                "es miembro de Aiap desde 2010 y dirige la colección "
                "editorial «Carta Bianca» para Adelphi desde 2024.",
            "credentials": [
                "Isia Urbino · Diseño gráfico '06",
                "Pentagram Nueva York · senior '07—'10",
                "Studio Sonnoli Rímini · asociada '10—'14",
                "Politecnico Milano · docente de diseño tipográfico",
                "Aiap · miembro de número desde 2010",
                "ADI · jurado Design Index 2024",
            ],
            "image": "https://images.unsplash.com/photo-1544717305-2782549b5136?w=1200&q=80&auto=format&fit=crop",
        },

        # Studio team (full team — 4 collaborators beyond founder)
        "team_label":   "Equipo del estudio",
        "team_heading": "Cinco diseñadores, dos colaboradores externos",
        "team_intro":
            "Trabajamos en un único espacio abierto — sin despachos "
            "separados. Cada proyecto cuenta con un equipo fijo de tres "
            "personas, dirigido por la AD. Los colaboradores externos "
            "intervienen únicamente en tipografía original y maquetación "
            "de largo recorrido.",
        "team": [
            {"name": "Marco Salvioli",
             "role": "Diseñador senior · edición",
             "bio":
                "Cinco años en Tassinari/Vetta en Trieste antes de "
                "incorporarse al estudio en 2019. Coordina los proyectos "
                "editoriales y los manuales tipográficos."},
            {"name": "Anna Brambilla",
             "role": "Diseñadora · identidad de marca",
             "bio":
                "Naba Milán '17, dos años en Studio Mut Bolzano. "
                "Se ocupa de los rebrands de estudio y maisons de "
                "pequeño lujo, desde la investigación al manual operativo."},
            {"name": "Lorenzo Tagliabue",
             "role": "Diseñador · sistemas & señalética",
             "bio":
                "Politecnico Milano '19, prácticas en Atelier Carvalho "
                "Bernau en Berlín. Se encarga de los sistemas de "
                "señalética y de los materiales para espacios expositivos."},
            {"name": "Sara Pellegrini",
             "role": "Diseñadora · digital",
             "bio":
                "Iuav Venecia '20, dos años en Cantiere Creativo "
                "Florencia. Extiende las identidades a los sistemas "
                "digitales (sitios, aplicaciones, piezas animadas)."},
            {"name": "Filippo Vigorelli",
             "role": "Colaborador · dibujo tipográfico",
             "bio":
                "Type designer independiente, formado en Type@Cooper "
                "Nueva York. Colabora con los caracteres a medida del "
                "estudio desde 2017."},
            {"name": "Beatrice Fornaro",
             "role": "Becaria · 2026",
             "bio":
                "Último año en Isia Urbino. Acompaña la práctica "
                "editorial y contribuye al archivo de los proyectos "
                "pasados."},
        ],

        # Studio principles — 4 design notes
        "principles_label":   "Principios del estudio",
        "principles_heading": "Cuatro reglas <em>no negociables</em>",
        "principles_intro":
            "Son las cuatro reglas que separan un proyecto firmado "
            "Velluti de una ejecución estándar de estudio. Están "
            "escritas en el manual interno de 2018, jamás actualizado.",
        "principles": [
            ("01", "Una sola voz, de principio a fin",
             "La AD entra en la primera llamada y firma la entrega. "
             "Nada de traspasos a junior tras el pitch — la persona "
             "que conocen en la reunión de apertura es la misma que "
             "firma el manual operativo final."),
            ("02", "La tipografía antes que la marca",
             "En cada proyecto la elección de los caracteres precede "
             "al dibujo del logo. Las identidades que proponemos nacen "
             "de una gramática tipográfica, no de un símbolo decorativo."),
            ("03", "Nada de moodboards de Pinterest",
             "Las referencias que proponemos proceden de nuestra "
             "biblioteca de estudio, de los archivos de las "
             "instituciones con las que trabajamos y de visitas "
             "directas a exposiciones. Jamás imágenes descargadas."),
            ("04", "El manual es un libro",
             "Toda identidad cierra con un manual operativo impreso — "
             "no un PDF, un volumen de ciento veinte a doscientas "
             "páginas. Queda en la biblioteca del cliente, no en una "
             "carpeta del servidor."),
        ],

        # Press band — full press list (extended from home)
        "press_label":   "Premios, exposiciones, publicaciones",
        "press_heading": "Selección 2020 — 2026",
        "press_full": [
            ("2025", "ADI Design Index",
             "Selección de edición de arte", "Catálogo Triennale 2025"),
            ("2024", "European Design Awards · Bronze",
             "Sistemas tipográficos editoriales", "Colección «Carta Bianca»"),
            ("2024", "Brand New (Under Consideration)",
             "Reseña crítica", "Rebrand Maison Lambrate"),
            ("2023", "Aiap Design Per · Exposición colectiva",
             "Edición de autor", "Monografía Velluti & Co."),
            ("2023", "Type Directors Club New York · Honor",
             "Dibujo tipográfico", "Carácter a medida Querini"),
            ("2022", "Eye Magazine n.º 102",
             "Ensayo ilustrado de ocho páginas", "Identidad Velluti Studio"),
            ("2021", "ADI Compasso d'Oro · Mención",
             "Categoría de comunicación visual", "Sistema Triennale 2021"),
            ("2020", "Brno Biennial Chequia · Selección",
             "Identidades museísticas", "Festival Pordenone 36.ª"),
        ],

        # Final CTA — visit the studio
        "cta_heading":      "Visitar el estudio",
        "cta_intro":
            "El estudio está en Via Tortona 27, entrada por el patio "
            "interior. La biblioteca abre con cita previa — escríbanos "
            "dos líneas y concertamos una mañana.",
        "cta_primary":      "Concertar una visita",
        "cta_primary_href": "contatti",
    },

    # ─── LAVORO (project_list) ──────────────────────────────────
    "lavoro": {
        "eyebrow":   "Archivo de proyectos · 2014 — 2026",
        "headline":  "Cuarenta y siete proyectos firmados, <em>seis disciplinas</em>.",
        "intro":
            "El archivo completo de los proyectos del estudio. La "
            "selección que aquí se muestra cubre los seis encargos más "
            "recientes de cada disciplina. Para el PDF íntegro del "
            "portfolio (96 páginas, todos los proyectos firmados desde "
            "2014) escriban a studio@chiaravelluti.it.",

        # Discipline filter pills
        "filter_label": "Disciplinas",
        "filters": [
            "Todas",
            "Edición de arte",
            "Identidad de marca",
            "Sistemas & señalética",
            "Identidad de evento",
            "Dirección artística",
        ],

        # Ledger row labels (lifted from skin for i18n)
        "row_discipline_label": "Disciplina",
        "row_duration_label":   "Duración",
        "row_year_label":       "Año",

        # Index intro band on top of the ledger
        "ledger_label": "Índice cronológico",
        "ledger_intro":
            "Recorra de arriba a abajo para el cronológico inverso. "
            "Pulse una fila para abrir el dossier completo del proyecto.",

        # CTA before footer
        "cta_label":   "¿Buscan algo concreto?",
        "cta_heading": "A petición enviamos dossieres por disciplina",
        "cta_intro":
            "Si están valorando al estudio para un encargo específico, "
            "indíquennos la disciplina y les enviamos en 48 horas tres "
            "dossieres relevantes — formato A4, listos para la "
            "presentación interna.",
        "cta_primary":      "Escríbanos",
        "cta_primary_href": "contatti",

        # Dossier (project_detail) labels — constants across all posts,
        # localized via the `lavoro` page_data block.
        "dossier_meta_discipline_label": "Disciplina",
        "dossier_meta_year_label":       "Año",
        "dossier_meta_duration_label":   "Duración",
        "dossier_meta_team_label":       "Equipo",
        "dossier_summary_label":         "Síntesis del proyecto",
        "dossier_deliverables_label":    "Entregables entregados",
        "dossier_deliverables_heading":  "Lo que hemos producido",
        "dossier_colophon_label":        "Colofón",
    },

    # ─── PROCESSO (process) ─────────────────────────────────────
    "processo": {
        "eyebrow":   "Cómo trabajamos · método del estudio",
        "headline":  "Cinco fases, <em>un solo expediente</em> por proyecto.",
        "intro":
            "El método del estudio está escrito, se comparte con el "
            "cliente en la primera llamada y se sigue sin excepciones. "
            "Cada proyecto cuenta con su expediente físico — carpeta "
            "verde con número, etiqueta tipográfica, conservada en "
            "archivo durante veinte años como mínimo.",

        # Process step + capability labels (lifted from skin for i18n)
        "step_sequence_label":       "Secuencia",
        "step_index_prefix":         "Paso",
        "step_index_separator":      "de",
        "capability_duration_label": "Duración orientativa",

        # 5-step process (richer than business)
        "process_label":   "Secuencia del estudio",
        "process_heading": "Apertura, investigación, propuesta, construcción, entrega",
        "process": [
            ("01", "Apertura del expediente",
             "Primera llamada con la AD (45 minutos, gratuita). Se "
             "repasan el perímetro, las expectativas del cliente y el "
             "eventual conflicto de agenda. En cinco días una propuesta "
             "escrita de tres páginas: perímetro, entregables, "
             "calendario, honorarios.",
             "Entregable", "Propuesta escrita · 3 páginas"),
            ("02", "Investigación preliminar",
             "De cuatro a seis semanas de investigación: visita al "
             "archivo del cliente, biblioteca del estudio, referentes "
             "históricos y contemporáneos. Nunca moodboards de "
             "Pinterest. Se cierra con un brief ilustrado que se "
             "comparte con el cliente.",
             "Duración", "4 — 6 semanas"),
            ("03", "Propuesta de dirección",
             "Se presenta una única dirección, no tres. La "
             "presentación es en persona, en el estudio o en la sede "
             "del cliente, nunca por correo. El cliente puede aceptar, "
             "pedir revisiones acotadas (máximo dos ciclos) o "
             "interrumpir el encargo (cláusula de salida prevista en "
             "el contrato).",
             "Duración", "2 — 3 semanas de diseño + presentación"),
            ("04", "Construcción del sistema",
             "La dirección aprobada se declina en un sistema completo: "
             "tipografía, paleta, retícula, marcas, materiales, "
             "aplicaciones. Para identidades completas: de diez a "
             "dieciséis semanas. El equipo asignado trabaja a puerta "
             "cerrada con dos revisiones mensuales con el cliente.",
             "Duración", "10 — 16 semanas según perímetro"),
            ("05", "Entrega y manual impreso",
             "Cada proyecto cierra con un manual operativo impreso — "
             "de 120 a 240 páginas, formato A4, impresión offset en "
             "blanco y negro. Una copia para el cliente, otra para la "
             "biblioteca del estudio. Seis meses de asistencia "
             "incluidos sobre la aplicación del manual.",
             "Entregable", "Manual impreso + asistencia de 6 meses"),
        ],

        # Capabilities — full list (extended from home)
        "capabilities_label":   "Disciplinas completas",
        "capabilities_heading": "Qué diseñamos",
        "capabilities_intro":
            "Las disciplinas que practicamos con regularidad. No "
            "trabajamos en publicidad above-the-line, packaging FMCG, "
            "motion graphics de más de 30 segundos, ni en plantillas "
            "recoloreables.",
        "capabilities_full": [
            {
                "num": "01",
                "title": "Identidad de marca",
                "blurb":
                    "Identidades completas para instituciones culturales "
                    "y maisons de pequeño lujo. Marca + sistema "
                    "tipográfico + paleta + retícula + manual operativo "
                    "impreso.",
                "scope": [
                    "Naming e investigación tipográfica",
                    "Dibujo de la marca y variantes",
                    "Sistema visual + retícula",
                    "Manual operativo (120 — 240 pp.)",
                ],
                "duration": "16 — 24 semanas por identidad completa",
            },
            {
                "num": "02",
                "title": "Edición de arte",
                "blurb":
                    "Catálogos de arte, monografías de autor, "
                    "colecciones editoriales. Dirección tipográfica, "
                    "maquetación, elección del papel y seguimiento "
                    "en imprenta.",
                "scope": [
                    "Dirección tipográfica",
                    "Maquetación y retícula editorial",
                    "Elección del papel + investigación tipográfica",
                    "Seguimiento en imprenta (visita a taller)",
                ],
                "duration": "12 — 32 semanas por volumen",
            },
            {
                "num": "03",
                "title": "Sistemas & señalética",
                "blurb":
                    "Señalética museística, sistemas gráficos para "
                    "espacios expositivos, wayfinding bilingüe y "
                    "materiales didácticos para exposiciones "
                    "temporales.",
                "scope": [
                    "Auditoría del espacio existente",
                    "Sistema bilingüe/trilingüe",
                    "Dibujo de la señalética",
                    "Dirección de producción (grabado/impresión)",
                ],
                "duration": "10 — 18 semanas por espacio museístico",
            },
            {
                "num": "04",
                "title": "Identidad de evento",
                "blurb":
                    "Marcas temporales para festivales, bienales y "
                    "ediciones limitadas. Material impreso, señalética "
                    "para la sede y sistema digital.",
                "scope": [
                    "Marca temporal + variante anual",
                    "Sistema impreso (carteles, folletos, entradas)",
                    "Señalética de la sede",
                    "Sistema digital (web + piezas animadas)",
                ],
                "duration": "8 — 14 semanas por edición",
            },
            {
                "num": "05",
                "title": "Dirección artística",
                "blurb":
                    "Consultoría AD para equipos internos: revisión "
                    "de manuales existentes, auditorías visuales, "
                    "mentoría al equipo gráfico interno y formación "
                    "tipográfica.",
                "scope": [
                    "Auditoría visual de lo existente",
                    "Revisión del manual",
                    "Mentoría al equipo gráfico (1 día/mes)",
                    "Taller tipográfico (formación)",
                ],
                "duration": "Encargo anual, renovable",
            },
        ],

        # Final CTA before footer
        "cta_heading":      "¿Qué disciplina es la suya?",
        "cta_intro":
            "Si el perímetro no está claro, escriban dos líneas de "
            "contexto. Les respondemos con la disciplina adecuada en "
            "48 horas — aunque no sea el estudio Velluti quien los "
            "acompañe.",
        "cta_primary":      "Escríbanos",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI (contact) ─────────────────────────────────────
    "contatti": {
        "eyebrow":   "Una conversación preliminar",
        "headline":  "Treinta minutos con la AD, <em>sin compromiso</em>.",
        "intro":
            "El primer contacto se produce directamente con Chiara "
            "Velluti, directora artística y fundadora. Repasamos el "
            "perímetro del proyecto, el calendario y el eventual "
            "conflicto de agenda — antes de cualquier propuesta "
            "escrita.",

        # Studio info side card
        "studio_label":          "El estudio",
        "studio_address":        "Via Tortona 27 · 20144 Milán",
        "studio_area":           "Entrada por el patio interior · timbre «Velluti»",
        "studio_metro":          "MM2 Porta Genova · 4 minutos a pie",
        "studio_hours":          "Lun – Vie · 10:00 – 19:00 · con cita previa",
        # Studio card row labels (lifted from skin for i18n)
        "studio_address_label":  "Dirección",
        "studio_area_label":     "Entrada",
        "studio_metro_label":    "Metro",
        "studio_hours_label":    "Horario",

        # Form fields — generic loop in chrome
        "form_label":   "Solicitar una primera llamada",
        "form_heading": "Cumplimente el formulario",
        "form_intro":
            "Recibirá confirmación en 48 horas laborables. Las "
            "llamadas se celebran los martes y los jueves por la "
            "tarde, a puerta cerrada, con la AD.",
        "form_fields": [
            {"name": "name",      "label": "Nombre",         "type": "text",     "required": True,  "placeholder": "Ej. Chiara",
             "helper": "Solo el nombre de pila, gracias."},
            {"name": "surname",   "label": "Apellido",       "type": "text",     "required": True,  "placeholder": "Ej. Velluti",
             "helper": "Tal y como figura en la tarjeta de visita."},
            {"name": "organization", "label": "Organización","type": "text",     "required": True,  "placeholder": "Ej. Triennale Milano",
             "helper": "Institución, editorial o maison."},
            {"name": "role",      "label": "Cargo",          "type": "text",     "required": True,  "placeholder": "Ej. Directora editorial",
             "helper": "Puesto de quien llevará el proyecto."},
            {"name": "email",     "label": "Correo electrónico", "type": "email","required": True,  "placeholder": "chiara.velluti@triennale.org",
             "helper": "Preferentemente correo institucional."},
            {"name": "phone",     "label": "Teléfono",       "type": "tel",      "required": False, "placeholder": "+39 ...",
             "helper": "Línea directa · solo si prefieren que los llamemos."},
            {"name": "discipline", "label": "Disciplina de interés", "type": "select", "required": True,
             "options": [
                 "A definir en la llamada",
                 "Identidad de marca",
                 "Edición de arte",
                 "Sistemas & señalética",
                 "Identidad de evento",
                 "Dirección artística",
             ],
             "helper": "Elijan «a definir» si el perímetro abarca varias disciplinas."},
            {"name": "horizon",   "label": "Horizonte temporal", "type": "select", "required": True,
             "options": [
                 "Inicio en un mes",
                 "Inicio en tres meses",
                 "Inicio en seis meses",
                 "Exploratorio · sin urgencia",
             ],
             "helper": "Ayuda a programar la primera llamada con la AD."},
            {"name": "brief",     "label": "Descripción breve del proyecto", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Máximo 800 caracteres. Sin nombres de contrapartes — se tratarán "
                            "únicamente tras un NDA recíproco, si procede.",
             "helper": "Lo justo para entender si el proyecto es de nuestra competencia."},
        ],

        "form_sections": [
            {"num": "01", "title": "Persona de contacto",
             "meta": "La persona que llevará el proyecto por parte del cliente.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Organización",
             "meta": "Para el conflict-check preliminar con otros proyectos en curso.",
             "fields": ["organization", "role"]},
            {"num": "03", "title": "Perímetro del proyecto",
             "meta": "Una descripción sintética — los anexos llegan en la segunda llamada, tras NDA.",
             "fields": ["discipline", "horizon", "brief"]},
            {"num": "04", "title": "Anexos (opcionales)",
             "meta": "Brief interno, dossier institucional, investigación preliminar. Pueden adelantar la primera llamada.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "brief_allegato",
            "label":    "Documentos preliminares",
            "helper":   "Brief interno, dossier institucional, imágenes de referencia. "
                        "PDF / DOCX / JPG · máx. 20 MB en total.",
            "accept":   ".pdf,.docx,.jpg,.jpeg,.png",
            "multiple": True,
            "primary":  "Arrastren aquí los documentos o",
            "link":     "búsquenlos en el archivo",
            "meta":     "PDF / DOCX / JPG · máx. 20 MB",
        },

        "form_submit_label": "Enviar solicitud",
        "form_submit_note":
            "Confirmación directa de la AD en 48 horas laborables. "
            "Sin account manager externo, sin automatización de leads.",
        "form_consent":
            "Consiento el tratamiento de los datos personales conforme "
            "al Reglamento UE 679/2016. Las solicitudes las lee y "
            "archiva únicamente la directora artística — ningún "
            "tercero interviene.",

        # Channels strip
        "channels_label": "Canales directos",
        "channels": [
            ("Correo del estudio", "studio@chiaravelluti.it",    "Respuesta en 48 horas laborables"),
            ("Centralita",         "+39 02 8736 4408",           "Lun – Vie · 10:00 – 19:00"),
            ("Visita al estudio",  "Via Tortona 27 · Milán",     "Con cita previa, nunca sin aviso"),
        ],

        "footnote":
            "El estudio no responde a solicitudes anónimas y no emite "
            "presupuestos por correo sin una primera llamada. Las "
            "tarifas y las condiciones económicas se presentan en "
            "propuesta escrita, jamás por mensaje.",
    },

    # ─── POSTS — drives /lavoro/<slug>/ project_detail ──────────
    "posts": [
        {
            "slug":        "triennale-milano-catalogo-2025",
            "title":       "Triennale Milano · catálogo 2025",
            "category":    "Edición de arte",
            "year":        "2025",
            "duration":    "32 semanas",
            "client_code": "Triennale Milano · catálogo de la 24.ª edición · 412 páginas offset",
            "lead":
                "Dirección tipográfica y maquetación del catálogo "
                "oficial de la 24.ª Triennale de Milán. Volumen de 412 "
                "páginas, 24 × 32 cm, impresión offset a cinco tintas "
                "sobre papel uncoated de 130 g/m² Fedrigoni Arena.",
            "summary": [
                "Dirección tipográfica y maquetación",
                "Sistema de retícula variable para 87 contribuciones",
                "Dibujo a medida de las capitulares",
                "Seguimiento en imprenta · 4 visitas · 12 jornadas",
            ],
            "discipline":  "Edición de arte",
            "team":        "AD + 2 senior · 32 semanas",
            "deliverables":[
                "Volumen 412 pp. · 24 × 32 cm · impresión offset",
                "Sistema de retícula variable para ensayos y fichas",
                "Carácter a medida Triennale Display (12 glifos capitulares)",
                "Manual de redacción interno · 48 pp.",
            ],
            "credits": [
                ("Cliente",             "Triennale Milano"),
                ("Dirección editorial", "Maria Sebregondi"),
                ("Imprenta",            "Grafiche Antiga · Treviso"),
                ("Papel",               "Fedrigoni Arena Natural Smooth 130 g/m²"),
                ("Encuadernación",      "Rústica cosida con hilo vegetal · cartulina 350 g/m²"),
                ("Tirada",              "3.200 ejemplares · segunda reimpresión junio 2025"),
            ],
            "sections": [
                {
                    "label": "El proyecto",
                    "heading": "Cuatrocientas doce páginas, ochenta y siete autores",
                    "body":
                        "El catálogo de la 24.ª Triennale documenta una "
                        "muestra de mil metros cuadrados en ocho salas, "
                        "con ochenta y siete contribuciones entre "
                        "ensayos críticos, fichas de obra y aparatos "
                        "documentales. El problema de diseño era "
                        "construir un sistema de retícula capaz de "
                        "acoger textos de extensión muy distinta (de 200 "
                        "a 12.000 palabras) preservando una lectura "
                        "editorial unitaria.",
                },
                {
                    "label": "La dirección tipográfica",
                    "heading": "Tres familias, una sola voz",
                    "body":
                        "Construimos el sistema sobre tres familias "
                        "tipográficas complementarias — una transitional "
                        "serif (Lyon Text) para los cuerpos de texto, "
                        "una grotesca geométrica (GT Walsheim) para los "
                        "titulares y una monoespaciada (JetBrains Mono) "
                        "para los aparatos documentales. Las tres "
                        "familias conviven sobre una retícula de nueve "
                        "columnas capaz de articularse en distintos "
                        "formatos sin romper la identidad.",
                },
                {
                    "label": "La ejecución",
                    "heading": "Treinta y dos semanas, cuatro visitas a imprenta",
                    "body":
                        "El volumen se maquetó en treinta y dos semanas "
                        "por un equipo de tres diseñadores del estudio, "
                        "con supervisión semanal de la AD. Cuatro "
                        "visitas a la imprenta en Treviso entre julio y "
                        "septiembre de 2025 permitieron calibrar la "
                        "impresión directamente en máquina — la "
                        "cubierta se rehízo dos veces hasta alcanzar el "
                        "negro pleno deseado sin reflejos.",
                },
            ],
            "next_label": "Encargo siguiente",
        },
        {
            "slug":        "adelphi-collana-carta-bianca",
            "title":       "Adelphi · colección «Carta Bianca»",
            "category":    "Identidad de colección",
            "year":        "2024",
            "duration":    "44 semanas",
            "client_code": "Adelphi Edizioni · colección editorial · 12 títulos al año",
            "lead":
                "Sistema visual y cubiertas de una nueva colección de "
                "ensayo de filosofía contemporánea para Adelphi. Doce "
                "títulos al año, formato 14 × 22 cm, rústica cosida "
                "sobre papel uncoated.",
            "summary": [
                "Dirección de colección + sistema tipográfico",
                "12 cubiertas en serie · dibujo a medida",
                "Sistema cromático por año editorial",
                "Manual de redacción tipográfica",
            ],
            "discipline":  "Identidad de colección",
            "team":        "AD + senior editorial · 44 semanas",
            "deliverables":[
                "Sistema visual de la colección · 36 páginas",
                "12 cubiertas en serie · dibujo por título",
                "Carácter a medida Adelphi Sans (para la colección)",
                "Manual de redacción tipográfica · 64 pp.",
            ],
            "credits": [
                ("Cliente",                "Adelphi Edizioni"),
                ("Director de colección",  "Roberto Calasso (póstumo) · Aldo Schiavone"),
                ("Papel",                  "Munken Pure Smooth 100 g/m²"),
                ("Imprenta",               "Tipografia Mariani · Bérgamo"),
                ("Encuadernación",         "Rústica cosida con hilo vegetal"),
                ("Tirada",                 "2.000 — 4.500 ejemplares por título"),
            ],
            "sections": [
                {
                    "label": "El proyecto",
                    "heading": "Una nueva colección para Adelphi",
                    "body":
                        "Adelphi busca un sistema visual para «Carta "
                        "Bianca», una colección de ensayo filosófico "
                        "destinada a acoger voces jóvenes de la "
                        "filosofía europea contemporánea. Doce títulos "
                        "al año, perfil editorial declaradamente "
                        "experimental, pero la marca Adelphi debe "
                        "honrarse.",
                },
                {
                    "label": "La idea",
                    "heading": "Una sola arquitectura, doce declinaciones",
                    "body":
                        "El sistema se construye sobre una arquitectura "
                        "tipográfica única — el título trabajado en "
                        "carácter a medida (Adelphi Sans, dibujado en "
                        "colaboración con Filippo Vigorelli), compuesto "
                        "a toda página sobre fondo monocromo. Cada año "
                        "editorial introduce una paleta de seis "
                        "colores; cada título se imprime a dos tintas "
                        "de la paleta anual. La identidad nace del "
                        "sistema, no de la decoración.",
                },
                {
                    "label": "La ejecución",
                    "heading": "Cuarenta y cuatro semanas, doce cubiertas",
                    "body":
                        "El sistema se entregó en julio de 2024; las "
                        "cuatro primeras cubiertas en septiembre y las "
                        "otras ocho a razón de una cada trimestre hasta "
                        "julio de 2025. La dirección editorial de Aldo "
                        "Schiavone aprueba personalmente cada cubierta "
                        "antes de la impresión. El estudio se encargó "
                        "asimismo de la formación de la redacción "
                        "interna sobre el uso del manual.",
                },
            ],
            "next_label": "Proyecto siguiente",
        },
        {
            "slug":        "querini-stampalia-segnaletica",
            "title":       "Fondazione Querini Stampalia · señalética",
            "category":    "Señalética & wayfinding",
            "year":        "2024",
            "duration":    "26 semanas",
            "client_code": "Fondazione Querini Stampalia · sistema bilingüe ITA / ENG",
            "lead":
                "Sistema de señalética bilingüe para la Fondazione "
                "Querini Stampalia de Venecia. Tres plantas, museo + "
                "biblioteca + espacio Carlo Scarpa. Latón grabado e "
                "impresión directa sobre paneles sustituibles.",
            "summary": [
                "Auditoría del espacio existente · 2 semanas",
                "Sistema bilingüe ITA / ENG · gramática unificada",
                "Dibujo del carácter a medida Querini Sans (96 glifos)",
                "Dirección de producción · latón grabado + impresión directa",
            ],
            "discipline":  "Sistemas & señalética",
            "team":        "AD + senior de wayfinding · 26 semanas",
            "deliverables":[
                "Sistema de señalética completo · 142 elementos",
                "Carácter a medida Querini Sans · 96 glifos · 3 pesos",
                "Manual operativo · 88 páginas",
                "Dirección de producción hasta la recepción",
            ],
            "credits": [
                ("Cliente",             "Fondazione Querini Stampalia, Venecia"),
                ("Dirección",           "Marigusta Lazzari, directora"),
                ("Arquitectura",        "Studio Carlo Scarpa (1961—63 · original)"),
                ("Producción en latón", "Bottega Pasinetti · Murano"),
                ("Impresión directa",   "Tipografia Adriatica · Mestre"),
                ("Recepción",           "Septiembre de 2024 · 142 elementos instalados"),
            ],
            "sections": [
                {
                    "label": "El problema",
                    "heading": "Una señalética nacida por adiciones sucesivas",
                    "body":
                        "La señalética de la Fondazione se había "
                        "estratificado en cinco ciclos sucesivos (desde "
                        "los años sesenta hasta una revisión de 2009), "
                        "con materiales, caracteres y lógicas de "
                        "emplazamiento distintos. El resultado era "
                        "ilegible, pero el verdadero problema era "
                        "respetar la arquitectura de Carlo Scarpa en la "
                        "planta baja — un espacio que no tolera "
                        "sobreimposiciones gráficas pesadas.",
                },
                {
                    "label": "El enfoque",
                    "heading": "Una gramática, dos materiales",
                    "body":
                        "Construimos una gramática unificada en dos "
                        "materiales: latón grabado al baño (para la "
                        "señalética permanente, en diálogo con el latón "
                        "de Scarpa en la planta baja) e impresión "
                        "directa sobre paneles de aluminio sustituibles "
                        "(para la señalética de exposición, "
                        "reemplazable en cada montaje). El carácter a "
                        "medida Querini Sans recoge las proporciones de "
                        "las lápidas epigráficas vénetas del siglo XVI.",
                },
                {
                    "label": "El resultado",
                    "heading": "Ciento cuarenta y dos elementos, cero sobreimposiciones",
                    "body":
                        "El sistema se instaló en tres fases sucesivas "
                        "entre junio y septiembre de 2024, con "
                        "recepción conjunta con la Soprintendenza para "
                        "la planta Scarpa. Los grabados en latón los "
                        "ejecutó la bottega Pasinetti en Murano con "
                        "técnica tradicional — quince semanas de "
                        "trabajo, todas verificadas in situ por el "
                        "estudio.",
                },
            ],
            "next_label": "Proyecto siguiente",
        },
    ],
}
