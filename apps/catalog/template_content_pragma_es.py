"""Pragma — Corporate Suite — Spanish (peninsular) content tree.

Phase 2i.2 — Live i18n rollout. Mirrors the shape of ``PRAGMA_CONTENT_IT``
verbatim and ships the peninsular Spanish institutional advisory voice
(Cinco Días / Expansión / McKinsey España register, usted form) for the
pragma-corporate-suite template.
"""
from __future__ import annotations

from typing import Any


PRAGMA_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Despacho",      "kind": "home"},
        {"slug": "chi-siamo",     "label": "Quiénes somos", "kind": "about"},
        {"slug": "competenze",    "label": "Competencias",  "kind": "services"},
        {"slug": "case-studies",  "label": "Casos",         "kind": "case_study_list"},
        {"slug": "contatti",      "label": "Contacto",      "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial": "P",
        "logo_word":    "Pragma Advisors",
        "tag":          "Advisory corporativo · Milán",
        "phone":        "+39 02 3611 9900",
        "email":        "segreteria@pragmaadvisors.it",
        "address":      "Via Filodrammatici 10 · 20121 Milán",
        "hours_compact":"Lun. – Vie. · 9:00 – 19:00 · con cita previa",
        "hours_footer_rows": [
            "Sábado · únicamente board calls programadas",
            "Domingo · cerrado",
        ],
        "license":      "Inscripción en el registro CONSOB de asesores independientes n.º 1148/2009",
        "footer_intro":
            "Boutique advisory independiente para direcciones generales "
            "y consejos de administración de empresas medianas consolidadas. "
            "Estrategia, M&A, gobierno corporativo y ESG. Sede en Milán, "
            "presencias estables en Fráncfort y Zúrich.",
        # Footer column headings — per-template (not shared chrome)
        "foot_studio":   "El despacho",
        "foot_pages":    "Secciones",
        "foot_contact":  "Contacto",
        "foot_offices":  "Sedes",
        "offices_footer_rows": [
            "Milán · Porta Nuova",
            "Frankfurt am Main · Bockenheim",
            "Zúrich · Paradeplatz",
        ],
        # Case study cross-page meta labels
        "case_practice_label":     "Práctica",
        "case_year_label":         "Año",
        "case_duration_label":     "Duración",
        "case_lead_label":         "Lead",
        "case_lead_partner_label": "Socio responsable",
        "case_team_label":         "Equipo y plazos",
        "case_timeline_label":     "Calendario",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Advisory corporativo · Milán · Fráncfort · Zúrich",
        "headline":    "Donde se toman las decisiones <em>que importan</em>.",
        "intro":
            "Acompañamos a direcciones generales y consejos de administración "
            "de empresas medianas consolidadas en las decisiones estructurales: "
            "planes industriales, operaciones de M&A, gobierno corporativo y "
            "hojas de ruta ESG. Una boutique independiente, veinte años de "
            "mandatos reservados.",
        "primary_cta":   "Solicitar una llamada privada",
        "primary_href":  "contatti",
        "secondary_cta": "Descargar la presentación",
        "secondary_href":"chi-siamo",

        # Right-hand boardroom photo + credit overlay
        "hero_image":              "https://images.unsplash.com/photo-1542626991-cbc4e32524cc?w=1600&q=80&auto=format&fit=crop",
        "hero_image_credit_left":  ("Fotografía",      "Consejo industrial lombardo · 2025"),
        "hero_image_credit_right": ("Año de fundación", "2004"),
        "hero_meta_strip": [
            ("Sede central",    "Milán · Porta Nuova"),
            ("Equipo sénior",   "14 socios"),
            ("Mandatos activos","42 proyectos"),
        ],

        # Advisory pillars — three-practice grid
        "pillars_label":   "Prácticas",
        "pillars_heading": "Tres competencias, una única firma",
        "pillars_intro":
            "Un único equipo multidisciplinar trabaja en cada mandato. "
            "Los socios no venden: se sientan a la mesa desde el inicio "
            "hasta la firma.",
        "pillars": [
            ("01", "Board advisory",
             "Acompañamos a consejos de administración y direcciones generales "
             "en las decisiones de cambio de rumbo: planes industriales trienales, "
             "reorganizaciones accionariales, sucesiones familiares y gestión "
             "de crisis reputacionales."),
            ("02", "Crecimiento y M&A",
             "Due diligence, valoración, negociación e integración post-deal "
             "en 10 – 12 semanas, con equipos dedicados por sector. Actuamos "
             "tanto del lado vendedor como del lado comprador, nunca ambos "
             "en el mismo expediente."),
            ("03", "Gobierno corporativo y ESG",
             "Cumplimiento CSRD, reporting integrado, modelos organizativos 231, "
             "estructura de comisiones del consejo y políticas de sostenibilidad "
             "para grupos industriales y servicios financieros."),
        ],

        # KPI strip on dark navy band
        "kpi_heading": "Veinte años de mandatos reservados",
        "kpi_strip": [
            ("22",       "años de actividad"),
            ("180+",     "mandatos cerrados"),
            ("1.400 M €","valor transaccionado"),
            ("94%",      "tasa de continuidad"),
        ],

        # Sectors ribbon
        "sectors_label": "Sectores de intervención",
        "sectors": [
            "Industria y manufactura",
            "Servicios financieros",
            "Energía y utilities",
            "Retail y consumo",
            "Healthcare y farma",
        ],

        # Trust band — institutional client logos as text wordmarks
        "trust_label":   "Han elegido Pragma en los últimos cinco años",
        "trust_logos":   [
            "GRUPO INDUSTRIAL DE BRESCIA",
            "FONDO MEZZANINE ITALIA",
            "BIOTECNOLOGÍA TURÍN",
            "CAJA AGRÍCOLA EMILIA",
            "ENERGÍA RENOVABLE NORTE",
            "GRUPO FAMILIAR RETAIL TOSCANA",
        ],

        # Leadership preview — three managing partners on home
        "leadership_label":   "Dirección",
        "leadership_heading": "Los socios que se sentarán a su mesa",
        "leadership_intro":
            "Cada mandato lo sigue personalmente al menos un managing "
            "partner. Ningún ejecutivo de recambio, ningún júnior aparcado.",
        "leadership": [
            {
                "name":  "Federico Seregni",
                "role":  "Managing partner · Board advisory",
                "bio":
                    "Veinte años en McKinsey & Company como senior partner del área industrial. "
                    "Consejero independiente en tres consejos cotizados. Especializado en planes "
                    "industriales y sucesiones familiares de la manufactura italiana.",
                "credentials": [
                    "Bocconi (CLEACC '95)",
                    "Insead MBA '01",
                    "Consejero Confindustria Lombardia",
                ],
            },
            {
                "name":  "Caterina Foschini",
                "role":  "Managing partner · Crecimiento y M&A",
                "bio":
                    "Más de 70 operaciones de M&A cerradas entre Italia y DACH. "
                    "Procedente de Bonelli Erede, ha dirigido dos salidas estratégicas "
                    "del private equity italiano en el segmento de consumo.",
                "credentials": [
                    "Cattolica (Derecho '98)",
                    "LL.M. Frankfurt am Main",
                    "AIDC, IBA M&A Forum",
                ],
            },
            {
                "name":  "Marco Lavezzi",
                "role":  "Managing partner · Gobierno corporativo y ESG",
                "bio":
                    "Ex responsable de sostenibilidad de un grupo de utilities cotizado. "
                    "Coordina los proyectos CSRD, reporting integrado y modelos 231 "
                    "para los clientes de la práctica de gobierno corporativo.",
                "credentials": [
                    "Politecnico Milano (Ing. Gestión '02)",
                    "Certificación GRI · CDP",
                    "Miembro CASUR-ANRI",
                ],
            },
        ],

        # Case studies preview — three on home, full list on /case-studies
        "cases_label":   "Trabajo reciente",
        "cases_heading": "Tres mandatos, tres direcciones",
        "cases_intro":
            "Una selección reciente de proyectos cerrados. Por razones "
            "de confidencialidad, los nombres de los clientes se revelan "
            "únicamente bajo acuerdo de confidencialidad.",

        # Final CTA band before footer
        "cta_label":     "Una conversación preliminar",
        "cta_heading":   "Treinta minutos, agenda acotada, sin compromiso",
        "cta_intro":
            "La primera llamada se mantiene con un socio sénior. "
            "Se discute el perímetro, el calendario y el eventual conflicto "
            "de intereses, antes de cualquier propuesta económica.",
        "cta_primary":   "Solicitar la llamada",
        "cta_primary_href": "contatti",
        "cta_secondary": "Descargar el dossier institucional",
        "cta_secondary_href": "chi-siamo",
    },

    # ─── CHI SIAMO (about + values) ─────────────────────────────
    "chi-siamo": {
        "eyebrow":   "El despacho · 2004 — 2026",
        "headline":  "Una boutique <em>independiente</em>, veintidós años de mandatos reservados.",
        "intro":
            "Pragma Advisors nace en Milán en 2004 del encuentro de "
            "profesionales de extracción consultora, financiera y jurídica. "
            "Desde entonces hemos crecido por cooptación —nunca por "
            "adquisición— y hemos mantenido la independencia del capital ajeno.",

        # Studio history — 5-step timeline
        "history_label":   "Historia del despacho",
        "history_heading": "Cinco hitos, veintidós años",
        "history_intro":
            "Cinco fechas que han definido Pragma. Detrás de cada uno "
            "de estos hitos hay una decisión estructural —de independencia, "
            "de geografía, de práctica— que todavía hoy orienta la forma "
            "en que aceptamos los mandatos.",
        "history": [
            ("2004", "Fundación",
             "Federico Seregni y tres socios abren Pragma en Via Filodrammatici, "
             "con cuatro mandatos de board advisory ya firmados."),
            ("2009", "Inscripción en el registro CONSOB",
             "Reconocimiento en el registro de asesores financieros independientes: "
             "la práctica de M&A puede presentarse como advisor formal."),
            ("2014", "Apertura de la sede de Fráncfort",
             "Caterina Foschini dirige la apertura de la sede DACH para los "
             "mandatos transfronterizos italo-alemanes de la manufactura."),
            ("2019", "Práctica de Gobierno corporativo y ESG",
             "Marco Lavezzi se incorpora como managing partner para constituir "
             "la práctica ESG, con los primeros mandatos CSRD para dos grupos "
             "de utilities."),
            ("2024", "Apertura de la sede de Zúrich",
             "Para acompañar los mandatos de estructuración patrimonial de las "
             "familias empresariales italianas, abrimos la oficina de Paradeplatz."),
        ],

        # Method / values
        "values_label":   "Método",
        "values_heading": "Cuatro principios <em>no negociables</em>",
        "values_intro":
            "Son las cuatro reglas que separan un mandato Pragma de un "
            "encargo estándar de consultoría estratégica. Las encontrará "
            "en el papel de carta del mandato firmado, no en el sitio web.",
        "values": [
            ("01", "Independencia del capital",
             "El capital del despacho está íntegramente en manos de los socios "
             "activos. Ningún aporte de grupos, ningún fondo de private equity "
             "en minoría, ningún accionista externo. La selección de mandatos "
             "nunca está influida por agendas ajenas."),
            ("02", "Un socio por cada mandato",
             "Un managing partner se sienta a la mesa desde la apertura del "
             "expediente hasta la firma del closing. Nada de partners-of-record "
             "que desaparecen tras el pitch: el senior advisor con el que se "
             "reunió en la primera llamada es el mismo que firmará el cierre "
             "del mandato."),
            ("03", "Ningún conflicto, nunca",
             "En el mismo sector no asesoramos jamás a dos clientes en "
             "competencia directa. En una operación de M&A, nunca vendedor y "
             "comprador en el mismo expediente. Nuestro Compliance Officer "
             "interno verifica cada nuevo mandato antes de la aceptación."),
            ("04", "Honorarios transparentes",
             "Tarifa diaria declarada en la propuesta, success fee únicamente "
             "en operaciones extraordinarias y siempre desglosada en factura. "
             "Ninguna retrocesión de comisiones, ningún acuerdo verbal con "
             "contrapartes financieras."),
        ],

        # Full team — 6 senior advisors + the 3 managing partners
        "team_label":   "Equipo sénior",
        "team_heading": "Catorce socios, tres oficinas, un único gobierno",
        "team_intro":
            "Las personas que trabajarán en su mandato. Los socios no son "
            "consultores y no le derivamos a un departamento: se sientan "
            "a la mesa desde el inicio hasta el final.",
        "team": [
            {"name": "Federico Seregni",
             "role": "Managing partner · Board advisory",
             "office": "Milán",
             "bio": "Ex senior partner de McKinsey, veinte años de planes industriales. "
                    "Consejero independiente en tres consejos cotizados."},
            {"name": "Caterina Foschini",
             "role": "Managing partner · M&A",
             "office": "Frankfurt",
             "bio": "Más de 70 operaciones cerradas entre Italia y DACH. Procedente de Bonelli Erede, "
                    "especializada en cross-border de consumo."},
            {"name": "Marco Lavezzi",
             "role": "Managing partner · Gobierno corporativo y ESG",
             "office": "Milán",
             "bio": "Coordina la práctica CSRD y los modelos 231. Ex responsable "
                    "de sostenibilidad de un grupo de utilities cotizado."},
            {"name": "Sabina Erlanger",
             "role": "Senior partner · Estructuración patrimonial",
             "office": "Zúrich",
             "bio": "Veinte años en la banca privada suiza. Coordina "
                    "los mandatos de relevo generacional para las familias italianas."},
            {"name": "Lorenzo Pellizzari",
             "role": "Senior partner · Industria y manufactura",
             "office": "Milán",
             "bio": "Ex director general de un grupo metalmecánico de Brescia. "
                    "Práctica estratégica para la cadena lombarda y véneta."},
            {"name": "Giulia Antinori",
             "role": "Senior partner · Servicios financieros",
             "office": "Milán",
             "bio": "Procedente de McKinsey servicios financieros. Mandatos de transformación "
                    "para bancos territoriales y SGR italianas."},
        ],

        # Coordinates strip
        "coordinates_label": "Las sedes",
        "coordinates": [
            ("Milán",     "Via Filodrammatici 10 · 20121 · Porta Nuova"),
            ("Frankfurt", "Bockenheimer Landstr. 51 · 60325 · Westend"),
            ("Zúrich",    "Paradeplatz 8 · 8001 · Innenstadt"),
        ],

        # Page-level CTA
        "cta_heading": "Una evaluación preliminar reservada",
        "cta_intro":
            "Los primeros treinta minutos con un socio son una conversación "
            "exploratoria, no una propuesta comercial. Se discute el perímetro "
            "del mandato, el calendario y el eventual conflicto de intereses.",
        "cta_primary":  "Solicitar la llamada",
        "cta_primary_href": "contatti",
    },

    # ─── COMPETENZE (services) ──────────────────────────────────
    "competenze": {
        "eyebrow":  "Áreas de práctica · 2026",
        "headline": "Seis competencias, <em>una única firma</em>.",
        "intro":
            "Las seis prácticas de Pragma. Cada cliente accede a un equipo "
            "multidisciplinar: no se paga por cada práctica por separado, "
            "el mandato cubre la combinación de competencias necesarias.",

        # Card meta labels
        "svc_duration_label": "Duración",
        "svc_leader_label":   "Socio responsable",

        # 6 services in airy cards
        "services": [
            {
                "num":   "01",
                "title": "Board advisory",
                "blurb":
                    "Acompañamos a consejos de administración y direcciones generales en las "
                    "decisiones de cambio de rumbo. Planes industriales trienales, "
                    "reorganizaciones accionariales, sucesiones familiares, gestión de "
                    "crisis reputacionales y mandatos interinos.",
                "scope": [
                    "Planes industriales y revisión estratégica",
                    "Sucesión familiar y gobierno corporativo",
                    "Mandatos interinos en CFO / COO",
                    "Comunicación de crisis al consejo",
                ],
                "duration": "8 – 14 semanas por ciclo",
                "leader":   "Federico Seregni",
            },
            {
                "num":   "02",
                "title": "Crecimiento y M&A",
                "blurb":
                    "Due diligence, valoración, negociación e integración post-deal. "
                    "Actuamos tanto del lado vendedor como del lado comprador, nunca "
                    "ambos en el mismo expediente. Tipología de operaciones: "
                    "carve-outs, joint ventures, salidas de private equity, MBO familiares.",
                "scope": [
                    "Due diligence vendedora y teaser",
                    "Scouting y valoración del lado comprador",
                    "Negociación y asistencia en el SPA",
                    "Integración post-fusión de 100 días",
                ],
                "duration": "10 – 24 semanas según perímetro",
                "leader":   "Caterina Foschini",
            },
            {
                "num":   "03",
                "title": "Gobierno corporativo y ESG",
                "blurb":
                    "Adaptación a la CSRD, reporting integrado, modelos organizativos "
                    "231, estructura de comisiones del consejo. Para grupos industriales "
                    "cotizados y para family business que se preparan para salir a "
                    "cotizar en Euronext Growth.",
                "scope": [
                    "Cumplimiento CSRD y reporting integrado",
                    "Modelos organizativos 231",
                    "Comisiones del consejo y políticas",
                    "Pre-IPO governance readiness",
                ],
                "duration": "12 – 18 semanas por ciclo",
                "leader":   "Marco Lavezzi",
            },
            {
                "num":   "04",
                "title": "Estructuración patrimonial",
                "blurb":
                    "Planificación patrimonial para familias empresariales italianas "
                    "con perímetro internacional. Holdings familiares, trusts, "
                    "family offices, relevo generacional.",
                "scope": [
                    "Holding familiar y pactos parasociales",
                    "Trusts y fundaciones familiares",
                    "Family office y advisory committee",
                    "Relevo generacional y sucesión",
                ],
                "duration": "16 – 36 semanas por reestructuración",
                "leader":   "Sabina Erlanger",
            },
            {
                "num":   "05",
                "title": "Industria y manufactura",
                "blurb":
                    "Práctica vertical para la cadena industrial lombarda y véneta. "
                    "Diagnóstico operativo, rediseño de supply chain, decisiones "
                    "estratégicas de make-or-buy, internacionalización productiva.",
                "scope": [
                    "Diagnóstico operativo multiplanta",
                    "Rediseño de supply chain",
                    "Make-or-buy estratégico",
                    "Apertura de plantas en el extranjero",
                ],
                "duration": "10 – 20 semanas por proyecto",
                "leader":   "Lorenzo Pellizzari",
            },
            {
                "num":   "06",
                "title": "Servicios financieros",
                "blurb":
                    "Transformación estratégica para bancos territoriales, SGR "
                    "italianas y fintech reguladas. Reposicionamiento estratégico, "
                    "M&A bancario, reporting prudencial al Banco de Italia.",
                "scope": [
                    "Reposicionamiento estratégico bancario",
                    "M&A bancario y de SGR",
                    "Cumplimiento Banco de Italia / EBA",
                    "Modelos operativos front-to-back",
                ],
                "duration": "12 – 24 semanas según perímetro",
                "leader":   "Giulia Antinori",
            },
        ],

        # Process strip — how a mandate is run
        "process_label":   "Cómo trabajamos",
        "process_heading": "Cuatro fases, una única secuencia",
        "process": [
            ("01", "Llamada exploratoria",
             "Treinta minutos reservados con un managing partner. "
             "Se discute el perímetro, sin propuesta económica."),
            ("02", "Propuesta por escrito",
             "En un plazo de cinco días, una propuesta de mandato de tres páginas "
             "con perímetro, entregables, calendario y tarifas transparentes."),
            ("03", "Ejecución",
             "Equipo dedicado desde la apertura hasta el cierre. El managing "
             "partner asiste a cada comité de dirección, nunca un júnior."),
            ("04", "Closing y seguimiento",
             "Closing memo reservado al consejo más seguimiento trimestral "
             "gratuito durante los 12 meses siguientes."),
        ],

        # Final CTA
        "cta_heading":   "¿Qué práctica le conviene?",
        "cta_intro":
            "Si el perímetro no está claro, envíenos una breve descripción "
            "del problema. Le dirigimos al socio adecuado en un plazo de "
            "48 horas, incluso si no acabamos trabajando con usted.",
        "cta_primary":   "Escríbanos",
        "cta_primary_href": "contatti",
    },

    # ─── CASE-STUDIES (list) ────────────────────────────────────
    "case-studies": {
        "eyebrow":  "Mandatos seleccionados · 2022 — 2026",
        "headline": "Tres mandatos, <em>tres direcciones</em>.",
        "intro":
            "Una selección de mandatos concluidos en los últimos cuatro años. "
            "Los clientes se identifican mediante código de sector (en "
            "cumplimiento de los acuerdos de confidencialidad), pero las "
            "métricas de resultado son reales y verificables en fase de "
            "reference call.",

        # Card-list of case studies
        "cases_label": "Casos",
        "cases_intro":
            "Selección equilibrada sobre las tres líneas principales: board "
            "advisory, M&A y gobierno corporativo. La lista completa está "
            "disponible en formato PDF a solicitud a través de la página "
            "de contacto.",

        "cta_heading":   "¿Un caso parecido al suyo?",
        "cta_intro":
            "Los dossieres completos (perímetro, KPI, reference call con "
            "el CFO del cliente) son accesibles previa firma de un NDA "
            "recíproco. La firma se produce en la primera llamada, antes "
            "de cualquier propuesta.",
        "cta_primary":   "Solicitar los dossieres íntegros",
        "cta_primary_href": "contatti",
    },

    # Posts powering case_study_detail. URL: /case-studies/<slug>/
    "posts": [
        {
            "slug":     "manifatturiero-bresciano-piano-industriale",
            "title":    "Grupo manufacturero de Brescia · plan industrial 2025-28",
            "category": "Board advisory",
            "year":     "2025",
            "duration": "14 semanas",
            "client_code": "Industria y manufactura · Brescia · 320 empleados · 78 M € de ingresos",
            "lead":
                "Tres plantas, dos familias accionistas en desacuerdo sobre el "
                "perímetro futuro. Pragma realineó el plan industrial trienal "
                "antes de la renovación del mandato del consejo.",
            "sections": [
                {
                    "label": "El problema",
                    "heading": "Dos familias, tres planes contradictorios",
                    "body":
                        "El grupo nace en 1968 de la unión de dos empresas "
                        "familiares. En 2024, el consejo se presentaba con "
                        "tres planes industriales alternativos sobre la mesa: "
                        "el cierre de la planta más antigua, la apertura de "
                        "una cuarta sede en Rumanía, o bien el carve-out de "
                        "la división de componentes para su cesión a un fondo "
                        "de private equity. Las dos familias accionistas "
                        "defendían escenarios incompatibles y el mandato del "
                        "consejo expiraba en doce meses.",
                },
                {
                    "label": "El enfoque",
                    "heading": "Diagnóstico operativo + revisión de gobierno",
                    "body":
                        "Pragma trabajó en tres direcciones en paralelo. "
                        "La práctica de industria y manufactura realizó un "
                        "diagnóstico operativo de nueve semanas sobre las "
                        "tres plantas, con medición OEE, costing por línea "
                        "y benchmark sectorial. En paralelo, la práctica de "
                        "board advisory medió entre las dos familias mediante "
                        "tres ciclos de talleres de alineamiento. La práctica "
                        "de gobierno corporativo revisó el pacto parasocial "
                        "y propuso un nuevo reglamento del consejo con "
                        "quórums reforzados.",
                },
                {
                    "label": "El resultado",
                    "heading": "Plan trienal aprobado por unanimidad",
                    "body":
                        "Plan industrial 2025–28 aprobado por unanimidad por "
                        "el consejo y por la junta extraordinaria. La planta "
                        "más antigua se reconvirtió (no se cerró) a la "
                        "producción de componentes para el sector eólico: "
                        "4 M € de capex financiados con el fondo Simest. "
                        "El carve-out de la división de componentes quedó "
                        "aparcado. El nuevo pacto parasocial redujo los "
                        "quórums de bloqueo un 40%.",
                },
            ],
            "kpi": [
                ("4 M €",    "capex de reconversión financiado"),
                ("0",        "plantas cerradas (3 mantenidas)"),
                ("100%",     "aprobación del plan en el consejo"),
                ("12 meses", "antes de la renovación del mandato"),
            ],
            "lead_partner": "Federico Seregni · Lorenzo Pellizzari",
            "team":         "3 socios · 4 séniors · 2 júniors · 14 semanas",
            "next_label":   "Mandato siguiente",
        },
        {
            "slug":     "carve-out-consumer-italia-dach",
            "title":    "Carve-out de la división de consumo · operación transfronteriza Italia-DACH",
            "category": "Crecimiento y M&A",
            "year":     "2024",
            "duration": "22 semanas",
            "client_code": "Retail y consumo · Vicenza · 540 empleados · 112 M € de ingresos",
            "lead":
                "Carve-out de la división de marca blanca de un grupo de "
                "retail de Vicenza, cedida a un operador estratégico alemán. "
                "Pragma actuó del lado vendedor, desde el teaser hasta la "
                "integración.",
            "sections": [
                {
                    "label": "El problema",
                    "heading": "Una división estratégica, un accionariado dividido",
                    "body":
                        "La división de marca blanca representaba el 28% "
                        "de los ingresos pero el 51% del EBITDA del grupo, "
                        "y había crecido sobre clientes DACH (DM, Lidl "
                        "Alemania) que no se sentían bien atendidos por "
                        "una estructura italiana. Una parte del accionariado "
                        "presionaba por el carve-out con cesión a un operador "
                        "estratégico alemán; otra prefería preservar el "
                        "perímetro y buscar un socio industrial italiano.",
                },
                {
                    "label": "El enfoque",
                    "heading": "Due diligence vendedora + scouting en paralelo",
                    "body":
                        "Pragma llevó a cabo una due diligence vendedora "
                        "integral (operativa, financiera, legal, fiscal) "
                        "en diez semanas. En paralelo, el scouting contactó "
                        "con seis potenciales compradores: tres operadores "
                        "estratégicos DACH, dos fondos de private equity "
                        "europeos especializados en consumo y un operador "
                        "italiano. La cesión se gestionó mediante subasta "
                        "privada de cuatro semanas con process letter "
                        "estructurada.",
                },
                {
                    "label": "El resultado",
                    "heading": "Cesión al múltiplo objetivo, sin disrupción",
                    "body":
                        "Cesión cerrada al múltiplo EBITDA objetivo "
                        "(8,4x), con cláusula de earn-out a 24 meses. "
                        "La integración post-fusión preservó el 80% "
                        "de la plantilla de la división (operarios "
                        "productivos y comerciales). El 100% de los "
                        "contratos con los tres principales clientes DACH "
                        "se renovaron en los seis meses posteriores al "
                        "closing.",
                },
            ],
            "kpi": [
                ("8,4x",     "múltiplo EBITDA al closing"),
                ("80%",      "plantilla cedida preservada"),
                ("100%",     "contratos DACH renovados tras el closing"),
                ("22 sem.",  "del encargo al signing"),
            ],
            "lead_partner": "Caterina Foschini · Giulia Antinori",
            "team":         "2 socios · 5 séniors · 3 júniors · 22 semanas",
            "next_label":   "Mandato siguiente",
        },
        {
            "slug":     "csrd-utility-quotata-roadmap",
            "title":    "Hoja de ruta CSRD para un grupo de utilities cotizado",
            "category": "Gobierno corporativo y ESG",
            "year":     "2025",
            "duration": "18 semanas",
            "client_code": "Energía y utilities · Bolonia · 1.800 empleados · 420 M € de ingresos",
            "lead":
                "Adaptación al primer reporting CSRD de un grupo de "
                "utilities cotizado en Euronext Milan. Doble materialidad, "
                "baseline scope 1-2-3, gobierno de sostenibilidad reconfigurado.",
            "sections": [
                {
                    "label": "El problema",
                    "heading": "Reporting fragmentado, baseline incompleta",
                    "body":
                        "El grupo había producido históricamente una memoria "
                        "de sostenibilidad GRI voluntaria, pero la baseline "
                        "scope 3 era incompleta, la materialidad no era "
                        "doble (impacto + financiera) y los KPI no estaban "
                        "listos para auditoría. El primer ejercicio CSRD "
                        "obligatorio correspondía al ejercicio 2025, con "
                        "publicación en abril de 2026: dieciocho meses "
                        "disponibles.",
                },
                {
                    "label": "El enfoque",
                    "heading": "Doble materialidad + baseline + gobierno",
                    "body":
                        "Pragma trabajó en tres flujos paralelos durante "
                        "dieciocho semanas. Flujo A: análisis de doble "
                        "materialidad con 38 grupos de interés consultados "
                        "(proveedores, clientes, sindicatos, ONG "
                        "ambientales, inversores institucionales). Flujo B: "
                        "finalización de la baseline scope 1-2-3 con "
                        "metodología GHG Protocol y validación externa. "
                        "Flujo C: reconfiguración del gobierno: comisión "
                        "de sostenibilidad del consejo, política ESG "
                        "actualizada, KPI integrados en el plan industrial.",
                },
                {
                    "label": "El resultado",
                    "heading": "Primer reporting CSRD listo para auditoría en plazo",
                    "body":
                        "Primer reporting CSRD publicado con informe de "
                        "aseguramiento limitado por auditor externo (cero "
                        "salvedades). 142 datapoints ESRS cubiertos "
                        "íntegramente. Comisión de sostenibilidad del "
                        "consejo activa desde el primer trimestre de 2026 "
                        "con miembro independiente de Pragma en calidad de "
                        "observador técnico durante el primer año. "
                        "Puntuación MSCI ESG mejorada en dos notches "
                        "de rating.",
                },
            ],
            "kpi": [
                ("142", "datapoints ESRS cubiertos"),
                ("0",   "salvedades del auditor"),
                ("38",  "grupos de interés consultados"),
                ("+ 2", "notches rating MSCI ESG"),
            ],
            "lead_partner": "Marco Lavezzi",
            "team":         "1 socio · 4 séniors · 2 júniors · 18 semanas",
            "next_label":   "Mandato siguiente",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Conversación preliminar",
        "headline": "Treinta minutos, agenda <em>acotada</em>, sin compromiso.",
        "intro":
            "El primer contacto se mantiene con un managing partner. "
            "Discutimos el perímetro del mandato, el calendario y el "
            "eventual conflicto de intereses, antes de cualquier "
            "propuesta económica.",

        # Form fields — generic loop in chrome
        "form_label":   "Solicitar la llamada",
        "form_heading": "Complete el formulario reservado",
        "form_intro":
            "Recibirá confirmación en un plazo de 48 horas laborables desde "
            "el envío. La información sensible se trata conforme al "
            "Reglamento UE 2016/679 (RGPD) y se custodia en archivo cifrado "
            "con acceso limitado a los socios.",
        "form_fields": [
            {"name": "name",      "label": "Nombre",          "type": "text",     "required": True,  "placeholder": "Ej. Alejandro",
             "helper": "Solo el nombre de pila, gracias."},
            {"name": "surname",   "label": "Apellidos",       "type": "text",     "required": True,  "placeholder": "Ej. Seregni",
             "helper": "Tal como figura en el organigrama."},
            {"name": "company",   "label": "Sociedad",        "type": "text",     "required": True,  "placeholder": "Ej. Grupo Industrial Lombardo",
             "helper": "Denominación registrada, no el nombre comercial."},
            {"name": "role",      "label": "Cargo",           "type": "text",     "required": True,  "placeholder": "Ej. CFO · CEO · Consejero",
             "helper": "Posición en el consejo o dirección de referencia."},
            {"name": "email",     "label": "Correo corporativo","type": "email",  "required": True,  "placeholder": "alejandro.seregni@grupo.es",
             "helper": "No aceptamos dominios de consumo (Gmail/Outlook/Hotmail) para este primer contacto."},
            {"name": "phone",     "label": "Teléfono",        "type": "tel",      "required": True,  "placeholder": "+34 ...",
             "helper": "Línea directa del interlocutor, no la centralita."},
            {"name": "practice",  "label": "Práctica de interés", "type": "select", "required": True,
             "options": [
                 "Por definir en llamada",
                 "Board advisory",
                 "Crecimiento y M&A",
                 "Gobierno corporativo y ESG",
                 "Estructuración patrimonial",
                 "Industria y manufactura",
                 "Servicios financieros",
             ],
             "helper": "Seleccione \"Por definir\" si el perímetro abarca varias prácticas."},
            {"name": "horizon",   "label": "Horizonte temporal", "type": "select", "required": True,
             "options": [
                 "En un mes",
                 "En tres meses",
                 "En seis meses",
                 "Exploratorio, sin urgencia",
             ],
             "helper": "Ayuda a agendar al socio adecuado para el mandato."},
            {"name": "perimeter", "label": "Breve descripción del perímetro", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Máximo 600 caracteres. Sin nombres de contrapartes: "
                            "se discuten únicamente tras NDA recíproco.",
             "helper": "Lo justo para entender si el mandato entra dentro de nuestra competencia. "
                       "Los nombres de las contrapartes se comparten solo tras NDA recíproco."},
        ],

        "form_sections": [
            {"num": "01", "title": "Interlocutor",
             "meta": "La persona que firmará el eventual NDA preliminar.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Sociedad",
             "meta": "Para el conflict-check preliminar.",
             "fields": ["company", "role"]},
            {"num": "03", "title": "Perímetro del mandato",
             "meta": "Ningún detalle sensible aquí: el perímetro técnico se comparte en la llamada tras NDA recíproco.",
             "fields": ["practice", "horizon", "perimeter"]},
            {"num": "04", "title": "Anexos (opcionales)",
             "meta": "Company profile, one-pager de gobierno o NDA estándar: pueden adelantar la llamada.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "briefing_allegato",
            "label":    "Documentos preliminares",
            "helper":   "Company profile, one-pager de gobierno o NDA estándar. "
                        "PDF / DOCX · máx. 15 MB en total. Archivo cifrado con "
                        "acceso limitado a los socios de Pragma.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Arrastre aquí los documentos o",
            "link":     "busque en el archivo",
            "meta":     "PDF / DOCX · máx. 15 MB · archivo cifrado",
        },

        "form_submit_label": "Solicitar la llamada",
        "form_submit_note":
            "Confirmación por parte de un managing partner en un plazo de "
            "48 horas laborables. Ningún BDR externo, ninguna automatización "
            "de secuencias.",
        "form_consent":
            "Consiento el tratamiento de los datos personales conforme al "
            "Reglamento UE 2016/679 (RGPD). Los datos se custodian en "
            "archivo cifrado con acceso limitado a los socios de Pragma. "
            "Ningún dato se comunica a terceros sin autorización expresa.",

        # Office meta-row labels
        "office_address_label": "Dirección",
        "office_area_label":    "Zona",
        "office_phone_label":   "Teléfono",
        "office_email_label":   "Correo",

        # Sidebar — offices + contact channels
        "offices_label":   "Las sedes",
        "offices": [
            {
                "city":    "Milán",
                "tag":     "Headquarters",
                "address": "Via Filodrammatici 10 · 20121",
                "area":    "Porta Nuova · cerca de Piazza della Scala",
                "phone":   "+39 02 3611 9900",
                "email":   "milano@pragmaadvisors.it",
            },
            {
                "city":    "Frankfurt",
                "tag":     "DACH desk",
                "address": "Bockenheimer Landstr. 51 · 60325",
                "area":    "Westend · cerca de la Alte Oper",
                "phone":   "+49 69 8870 4400",
                "email":   "frankfurt@pragmaadvisors.it",
            },
            {
                "city":    "Zúrich",
                "tag":     "Wealth desk",
                "address": "Paradeplatz 8 · 8001",
                "area":    "Innenstadt · cerca de Bahnhofstrasse",
                "phone":   "+41 44 215 7700",
                "email":   "zurich@pragmaadvisors.it",
            },
        ],

        "channels_label": "Canales directos",
        "channels": [
            ("Secretaría advisory",   "+39 02 3611 9900",             "Lun. – Vie. · 9:00 – 19:00"),
            ("Correo institucional",  "segreteria@pragmaadvisors.it", "Respuesta en 48 horas"),
            ("LinkedIn corporativo",  "in/pragma-advisors",           "Para relaciones públicas"),
        ],

        "footnote":
            "Pragma Advisors no responde a solicitudes anónimas y no emite "
            "opiniones preliminares por correo sin una primera llamada con un "
            "socio. La información administrativa (honorarios orientativos, "
            "modalidad de facturación, criterios de aceptación del mandato) "
            "se detalla en la primera llamada, nunca por escrito.",
    },
}
