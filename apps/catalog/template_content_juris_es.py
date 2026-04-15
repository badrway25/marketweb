"""Phase 2g3.7 · Session 53 · Juris — ES native-voice tree. Advisory-modern tech boutique voice."""
from __future__ import annotations

from typing import Any


JURIS_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Inicio",      "kind": "home"},
        {"slug": "approccio",  "label": "Método",      "kind": "about"},
        {"slug": "servizi",    "label": "Servicios",   "kind": "services"},
        {"slug": "settori",    "label": "Sectores",    "kind": "team"},
        {"slug": "insights",   "label": "Insights",    "kind": "blog_list"},
        {"slug": "contatti",   "label": "Contacto",    "kind": "contact"},
    ],

    "site": {
        "logo_initial": "M",
        "logo_word":    "Martini & Partners",
        "tag":          "Asesoría jurídica · desde 2018",
        "phone":        "hello@martinipartners.legal",
        "email":        "hello@martinipartners.legal",
        "address":      "Via Solferino 40 · 20121 Milán",
        "hours_compact":"Reunión de estrategia · Lun – Vie · 09:00 – 19:00",
        "hours_footer_rows": [
            "Videollamada desde nuestro dashboard",
            "Respuesta en 2 horas hábiles",
        ],
        "license":      "Colegio de Abogados de Milán n.º MI18224 · IVA IT10123540967",
        "nav_cta":      "Reservar reunión de estrategia",
        "footer_intro":
            "Martini & Partners es el despacho que une derecho, "
            "tecnología y estrategia para startups, pymes y fundadores. "
            "Honorarios claros, plazos definidos, un dashboard compartido.",
        "foot_studio":  "El despacho",
        "foot_pages":   "Páginas",
        "foot_contact": "Contacto",
        "foot_offices": "Oficinas",
        "offices_footer_rows": [
            "Milán · via Solferino 40",
            "Turín · via Roma 324",
            "Bolonia · via Indipendenza 18",
        ],
        "post_date_label":    "Publicado",
        "post_reading_label": "Lectura",
        "post_author_label":  "Por",
        "post_topic_label":   "Práctica",
        "post_back_label":    "Todos los insights",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Martini & Partners · Milán · Turín · Bolonia",
        "headline":    "El derecho, <em>de tu lado.</em>",
        "intro":
            "Acompañamos a startups, pymes y fundadores en las decisiones "
            "legales que mueven el negocio — con plazos claros, "
            "honorarios transparentes y un dashboard compartido donde "
            "sigues cada paso de tu asunto.",
        "primary_cta":    "Reservar reunión de estrategia",
        "primary_href":   "contatti",
        "secondary_cta":  "Cómo trabajamos",
        "secondary_href": "approccio",

        "sprint_chip":     "Reunión de estrategia · Próxima cita · 17 de abril",
        "sprint_chip_cta": "Reservar →",

        "sectors_label":   "Sectores",
        "sectors_heading": "Seis prácticas, un solo <em>método</em>.",
        "sectors_intro":
            "Cada práctica está liderada por una pareja socio + legal "
            "ops. El primer socio con quien hablas es el mismo que firma "
            "el encargo — sin traspasos, sin BDR, sin pitch deck.",
        "sectors": [
            ("01", "Startup & Tech",
             "Rondas, cap table, propiedad intelectual, compliance RGPD y Reglamento de IA para empresas digitales."),
            ("02", "Pymes y empresas familiares",
             "Relevo generacional, gobierno corporativo, pactos de socios y M&A mid-market."),
            ("03", "Laboral y RR. HH.",
             "Contratos, despidos, retribución, planes de stock options y teletrabajo transfronterizo."),
            ("04", "Contratación B2B",
             "SaaS, licencias, acuerdos comerciales, due diligence de proveedores y MSA en inglés."),
            ("05", "Resolución de conflictos",
             "Mediación, arbitraje, ADR y litigación estratégica."),
            ("06", "Privacidad e IA",
             "RGPD, Reglamento de IA, data mapping, EIPD y políticas para empresas data-driven."),
        ],

        "process_label":   "Cómo trabajamos",
        "process_heading": "Del brief al <em>primer escrito</em> en dos semanas.",
        "process_intro":
            "No vendemos horas, vendemos resultados. El método es el "
            "mismo para cada cliente — desde la startup seed que cierra "
            "su primera ronda hasta la pyme en su cuarto encargo. "
            "Tres pasos, cero misterio.",
        "process": [
            ("S.01", "Llamada de discovery",
             "30 min por vídeo · delimitamos el problema, no vendemos el servicio."),
            ("S.02", "Oferta clara",
             "Plazos, fases, tarifa plana o tope — todo por escrito, cero sorpresas."),
            ("S.03", "Dashboard en directo",
             "Seguimiento en tiempo real de escritos, plazos, documentos y horas trabajadas."),
        ],

        "metric_label":    "El despacho en cifras",
        "metric_heading":  "Ocho años en el terreno, tres ciudades, un centenar de encargos al año.",
        "metric_strip": [
            ("180+", "empresas asesoradas"),
            ("14",   "días · plazo medio hasta primer escrito"),
            ("4,9",  "★ satisfacción clientes"),
            ("0",    "€ setup fee, siempre"),
        ],

        "trust_label": "Hemos acompañado en los últimos doce meses",
        "trust_logos": [
            "UNA FINTECH MILANESA · RONDA SEED",
            "UN GRUPO FAMILIAR VÉNETO · RELEVO GENERACIONAL",
            "UN SAAS B2B TURINÉS · SERIE A",
            "UNA PYME BOLOÑESA · M&A TRANSFRONTERIZO",
            "UN MARKETPLACE ROMANO · POLÍTICA DE IA",
            "UNA SCALE-UP FLORENTINA · STOCK OPTIONS",
        ],

        "insights_label":   "Insights · esta semana",
        "insights_heading": "Lo que leemos <em>en el despacho</em>.",
        "insights_intro":
            "Las notas que escribimos cuando cambia una norma. Nuestros "
            "clientes las leen por la mañana, con el café — sin "
            "newsletter, sin lead magnet, sin secuencias automatizadas.",
        "insights_link":    "Todos los insights →",
        "insights_link_href":"insights",
        "insights": [
            ("17 abr", "Reglamento de IA · qué cambia para las pymes italianas",   "ai-act-pmi-italiane"),
            ("14 abr", "Stock options 2026 · nuevo régimen fiscal",                "stock-option-2026"),
            ("11 abr", "Teletrabajo transfronterizo · tres escenarios",             "smart-working-confine"),
        ],

        "cta_label":     "¿Listos para hablarlo?",
        "cta_heading":   "Treinta minutos, por vídeo, sin compromiso.",
        "cta_intro":
            "El primer contacto es con un socio, no con un BDR. Si el "
            "asunto no es de nuestra competencia, te remitimos al "
            "despacho adecuado — aunque no trabajes con nosotros.",
        "cta_primary":      "Reservar reunión de estrategia",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Leer nuestro método",
        "cta_secondary_href":"approccio",
    },

    # ─── APPROCCIO (about) ──────────────────────────────────────
    "approccio": {
        "eyebrow":  "Nuestro método · 2018 — 2026",
        "headline": "No vendemos horas, <em>vendemos resultados.</em>",
        "intro":
            "Fundamos el despacho en 2018 por frustración real — dos "
            "socios que habían pasado diez años en despachos de "
            "negocios internacionales en Milán y no soportaban más el "
            "modelo de facturación por hora, los juniors aparcados y "
            "los dashboards jurídicos noventeros. Abrimos Martini & "
            "Partners para hacerlo de otra manera.",

        "manifesto_label":   "Manifiesto",
        "manifesto_heading": "Cuatro principios, <em>no negociables</em>.",
        "manifesto_intro":
            "Los escribimos en la primera página de la hoja de encargo. "
            "No son eslóganes, son reglas operativas — si alguno de "
            "estos cuatro salta, no trabajamos contigo (o tú ya no "
            "trabajas con nosotros).",
        "manifesto": [
            ("01", "Primero el problema, después los honorarios",
             "La llamada de discovery es gratuita. Escribimos la oferta "
             "solo después de entender si el problema es nuestro y si "
             "la solución vale los honorarios. Si no es nuestro campo, "
             "te remitimos al despacho adecuado — sin comisión por referencia."),
            ("02", "Tarifa escrita, nunca por hora",
             "Cada encargo tiene una tarifa plana o un tope. La "
             "facturación por hora solo la usamos para urgencias no "
             "planificables, siempre comunicada antes de empezar. Sin "
             "partidas sorpresa, sin entradas genéricas \"gestión de asunto\"."),
            ("03", "Un socio, del primer escrito al último",
             "El socio que te recibe en el discovery es quien firma "
             "el escrito final. El equipo rota por especialización, "
             "nunca por seniority — nunca encontrarás a un junior "
             "desconocido trabajando en tu expediente sin tu aprobación previa."),
            ("04", "Dashboard compartido, siempre",
             "Cada cliente tiene un workspace con el estado de los "
             "asuntos, los documentos, los escritos presentados, las "
             "horas trabajadas y la línea temporal de plazos. No "
             "enviamos PDF por correo — todo pasa por el dashboard, "
             "siempre actualizado, siempre exportable."),
        ],

        "story_label":   "La historia",
        "story_heading": "Ocho años, tres ciudades, un solo método.",
        "story": [
            ("2018", "Fundación en Milán",
             "Giorgia Martini (ex-DLA Piper) y Davide Romano (ex-Bird & "
             "Bird) abren el despacho en via Solferino con tres encargos "
             "ya firmados por clientes de su práctica anterior."),
            ("2020", "Primer dashboard interno",
             "Construimos con un product manager ex-Zalando la primera "
             "versión del dashboard cliente. Nace aquí la idea de "
             "convertirlo en la seña del método Martini & Partners."),
            ("2022", "Apertura de oficina en Turín",
             "Abrimos la segunda oficina en Turín para seguir de cerca "
             "los encargos con scale-ups piamontesas — hoy por esa "
             "sede pasan la mitad de los encargos startup del despacho."),
            ("2024", "Apertura de oficina en Bolonia",
             "La tercera oficina en Bolonia cubre el corredor Emilia-"
             "Romaña con foco en pymes familiares y M&A mid-market. "
             "En 2025 salen de ella también los primeros encargos del Reglamento de IA."),
            ("2026", "Despacho a la medida actual",
             "Hoy somos ocho abogados y dos legal ops. No pensamos "
             "crecer más — preferimos seleccionar los encargos que "
             "abrir una cuarta oficina."),
        ],

        "dashboard_label":   "El dashboard cliente",
        "dashboard_heading": "Sigue tu asunto como <em>sigues un deploy</em>.",
        "dashboard_intro":
            "Cada cliente accede a un workspace cifrado con sus "
            "asuntos, documentos, plazos y las horas efectivamente "
            "trabajadas. Inspirado más en Linear que en un portal "
            "jurídico — porque trabajamos para personas que usan "
            "Linear en su propio oficio.",
        "dashboard_features": [
            ("Estado de los asuntos",  "Cada expediente tiene un kanban con estado · responsable · próximo plazo."),
            ("Documentos versionados", "Escritos presentados, borradores, anexos — con historial y comentarios en línea."),
            ("Horas trabajadas, a la vista","Las horas de cada socio y legal ops, actualizadas cada viernes por la tarde."),
            ("Plazos en calendario",   "Cada plazo es un evento · sincronizable con Google Calendar."),
            ("Exportación contable",   "Un clic para extraer factura + notas de gastos para tu asesor fiscal."),
            ("Acceso compartido",      "Invita al CFO, al CEO, al asesor — con permisos granulares."),
        ],
        "dashboard_mock": {
            "url":         "martini-partners.dashboard",
            "sidebar":     ["Asuntos", "Escritos", "Horas", "Plazos", "Equipo"],
            "sidebar_active_index": 0,
            "columns": [
                {"label": "Discovery",
                 "cards": [
                     {"title": "Fintech · seed",      "accent": False},
                     {"title": "Pyme · relevo",       "accent": False},
                 ]},
                {"label": "En curso",
                 "cards": [
                     {"title": "Scale-up · Serie A",  "accent": True},
                     {"title": "SaaS · MSA",          "accent": False},
                     {"title": "M&A · due diligence", "accent": False},
                 ]},
                {"label": "Cierre",
                 "cards": [
                     {"title": "RR. HH. · stock options", "accent": False},
                 ]},
            ],
        },

        "founders_label":   "Fundadores",
        "founders_heading": "Dos abogados, <em>una idea compartida</em>.",
        "founders": [
            {
                "name":  "Avv. Giorgia Martini",
                "role":  "Managing partner · Startup & Tech",
                "bio":
                    "Doce años en DLA Piper Milán, departamento "
                    "corporate. Ha cerrado dos Series A con fondos "
                    "italianos y una ronda transfronteriza con Orange "
                    "Ventures. Coordina la práctica startup y la "
                    "oficina de Milán.",
                "credentials": [
                    "Bocconi (Derecho '10)",
                    "LL.M. NYU '13",
                    "Miembro · Italian Tech Alliance",
                ],
            },
            {
                "name":  "Avv. Davide Romano",
                "role":  "Cofundador · Contratación B2B",
                "bio":
                    "Diez años en Bird & Bird, departamento tech & "
                    "comms. Especializado en SaaS licensing, MSA "
                    "transfronterizos y contratación para plataformas "
                    "marketplace. Coordina la oficina de Turín y la "
                    "práctica del Reglamento de IA.",
                "credentials": [
                    "Sapienza (Derecho '11)",
                    "LL.M. Fordham '14",
                    "Contribuidor · AIGA",
                ],
            },
        ],

        "offices_label": "Las oficinas",
        "offices": [
            ("Milán",    "Via Solferino 40 · 20121 · Brera",         "Sede central · todas las prácticas"),
            ("Turín",    "Via Roma 324 · 10123 · Centro",            "Desk scale-up + corredor piamontés"),
            ("Bolonia",  "Via Indipendenza 18 · 40121 · Centro",     "Desk pymes + corredor Emilia-Romaña"),
        ],

        "cta_heading": "¿Quieres ver el dashboard en directo?",
        "cta_intro":
            "La llamada de discovery incluye un walkthrough del "
            "workspace cliente. Te enseñamos cómo es, qué ves, qué "
            "exportas y cómo lo integramos con tus herramientas "
            "(Notion, Slack, Google Workspace).",
        "cta_primary":      "Reservar la llamada de discovery",
        "cta_primary_href": "contatti",
    },

    # ─── SERVIZI (services) ─────────────────────────────────────
    "servizi": {
        "eyebrow":  "Servicios · 2026",
        "headline": "Siete ofertas, <em>plazos garantizados</em>, precios declarados.",
        "intro":
            "Las siete ofertas del despacho. Cada oferta tiene un "
            "alcance por escrito, un plazo orientativo y una tarifa "
            "plana o con tope. Sin lista de precios por hora "
            "genérica, sin \"a concretar en la llamada\".",

        "svc_duration_label": "Duración",
        "svc_price_label":    "Precio",
        "svc_deliverables_label": "Qué entregamos",
        "svc_engagement_label":   "Modalidad",

        "services": [
            {
                "num":   "01",
                "title": "Startup Legal Sprint",
                "blurb":
                    "Todo el setup legal para una startup que cierra "
                    "su ronda seed en tres semanas — estatutos, pacto "
                    "de socios, term sheet, onboarding de inversores "
                    "y cap table limpio.",
                "deliverables": [
                    "Estatutos y pacto de socios a medida",
                    "Term sheet y revisión SAFE / nota convertible",
                    "Cap table mantenido en Ledgy o Capdesk",
                    "Onboarding de los primeros inversores por vídeo",
                ],
                "duration":   "3 semanas",
                "price":      "6.500 € todo incluido",
                "engagement": "Fija · 60 % al arranque · 40 % al cierre de la ronda",
                "tier":       "Seed-ready",
            },
            {
                "num":   "02",
                "title": "Asesoría M&A · pymes",
                "blurb":
                    "Asesoramos a pymes familiares en operaciones "
                    "estratégicas — cesión de participaciones, entrada "
                    "de fondo, M&A transfronterizo Italia-DACH. "
                    "Lado vendor o acquirer, nunca ambos en el mismo deal.",
                "deliverables": [
                    "Due diligence legal y fiscal",
                    "Valoración y borrador de SPA",
                    "Negociación y asistencia en el closing",
                    "Post-closing · integración 100 días",
                ],
                "duration":   "12 – 24 semanas según alcance",
                "price":      "45.000 € base + 0,8 % de success fee",
                "engagement": "Mixta · fija base + success fee al closing",
                "tier":       "Mid-market",
            },
            {
                "num":   "03",
                "title": "Contract-as-a-Service · B2B",
                "blurb":
                    "Para SaaS y scale-ups que firman MSA cada semana "
                    "— un equipo dedicado se encarga de redacción, "
                    "negociación y archivo contractual. Un canal "
                    "Slack, SLA de 48 horas, tarifa mensual.",
                "deliverables": [
                    "Templates MSA / DPA / SOW personalizados",
                    "Negociación redline con contrapartes",
                    "Archivo contractual en Notion o Juro",
                    "Informe mensual con KPI de plazos y volumen",
                ],
                "duration":   "Suscripción mensual · mínimo 6 meses",
                "price":      "Desde 3.200 € / mes",
                "engagement": "Recurrente · canal Slack + dashboard",
                "tier":       "Scale-ready",
            },
            {
                "num":   "04",
                "title": "Privacidad y Reglamento de IA · Readiness",
                "blurb":
                    "Auditoría completa RGPD + mapa de riesgos del "
                    "Reglamento de IA para empresas data-driven. "
                    "EIPD, registro de actividades de tratamiento, "
                    "políticas internas, formación del equipo y "
                    "readiness report para consejo o inversores.",
                "deliverables": [
                    "Auditoría RGPD + registro de actividades actualizado",
                    "Análisis de brechas Reglamento de IA y mapa por clase de riesgo",
                    "EIPD sobre procesos críticos (máx. 4)",
                    "Formación de dos horas para el equipo operativo",
                ],
                "duration":   "6 semanas",
                "price":      "12.500 € todo incluido",
                "engagement": "Fija · 50 % al arranque · 50 % a la entrega",
                "tier":       "Compliance",
            },
            {
                "num":   "05",
                "title": "Stock options y retribución",
                "blurb":
                    "Diseño e implementación de planes de stock options "
                    "para startups y scale-ups — incluyendo el "
                    "tratamiento fiscal 2026 y los aspectos laborales "
                    "para contratos italianos y transfronterizos. "
                    "Aplicable también al plan ENISA español.",
                "deliverables": [
                    "Plan SO/SAR diseñado a medida",
                    "Reglamento interno + onboarding de empleados",
                    "Tratamiento fiscal 2026 documentado",
                    "Acuerdos con fondos para lock-up y tag-along",
                ],
                "duration":   "4 semanas",
                "price":      "8.200 € base + 180 € / empleado onboardado",
                "engagement": "Fija + per-seat en onboarding",
                "tier":       "Scale-ready",
            },
            {
                "num":   "06",
                "title": "Resolución de conflictos",
                "blurb":
                    "Mediación, arbitraje y litigación estratégica — "
                    "priorizamos siempre la solución negociada, pero "
                    "cuando hace falta llevar un asunto a los "
                    "tribunales lo hacemos con socios dedicados.",
                "deliverables": [
                    "Evaluación del conflicto + memo de estrategia",
                    "Intento de mediación o ADR",
                    "Asistencia en arbitraje o juicio ordinario",
                    "Informe semanal del estado del conflicto",
                ],
                "duration":   "12 – 36 semanas según complejidad",
                "price":      "Presupuesto sobre alcance escrito",
                "engagement": "Mixta · fija por fase + success fee",
                "tier":       "Protection",
            },
            {
                "num":   "07",
                "title": "Fractional General Counsel",
                "blurb":
                    "Un socio dedicado como General Counsel a tiempo "
                    "parcial para scale-ups y pymes que todavía "
                    "necesitan competencia de despacho sin el coste "
                    "del puesto interno. Dos o tres días al mes, "
                    "presencia en consejo.",
                "deliverables": [
                    "Presencia física o por vídeo 2-3 d / mes",
                    "Board book legal y risk dashboard trimestral",
                    "Revisión de contratos clave + gobierno corporativo",
                    "Escalado a todas las oficinas Martini & Partners",
                ],
                "duration":   "Suscripción trimestral · mínimo 12 meses",
                "price":      "Desde 5.400 € / mes",
                "engagement": "Recurrente · presencia en consejo",
                "tier":       "Scale-ready",
            },
        ],

        "process_label":   "Cómo trabajamos",
        "process_heading": "Del brief al primer escrito en dos semanas.",
        "process": [
            ("S.01", "Llamada de discovery", "30 min por vídeo · alcance y encaje."),
            ("S.02", "Oferta por escrito",   "En 5 días · costes y plazos cerrados."),
            ("S.03", "Dashboard en directo", "Kickoff en 48 horas · todo trazado."),
        ],

        "faq_label":   "Preguntas frecuentes",
        "faq_heading": "Lo que nos preguntáis en las llamadas.",
        "faq": [
            ("¿Aceptáis encargos con success fee variable?",
             "Sí, pero solo en operaciones estratégicas (M&A, rondas, "
             "exit). En todo lo demás trabajamos con tarifa plana o suscripción."),
            ("¿Cómo gestionáis los conflictos de interés?",
             "El conflict check está automatizado en el dashboard. "
             "Nunca aceptamos dos clientes en competencia directa en "
             "el mismo sector. La verificación ocurre antes de la "
             "llamada de discovery, no después."),
            ("¿Trabajáis también con freelances y profesionales individuales?",
             "Sí, pero solo en ofertas específicas — Stock Options, "
             "Privacidad e IA y Contratación B2B. En el resto "
             "preferimos empresas con equipo."),
            ("¿Podéis firmar un NDA por adelantado?",
             "Sí, envíanos vuestro NDA estándar — lo revisamos en "
             "24 horas. Alternativamente, usamos nuestro template "
             "recíproco, disponible en el dashboard."),
        ],

        "cta_heading": "¿No sabéis qué oferta elegir?",
        "cta_intro":
            "Escríbenos alcance y plazos — en 24 horas os derivamos "
            "a la oferta adecuada (o os decimos que no es nuestro "
            "campo). Gratuito, sin compromiso, respuesta de un socio real.",
        "cta_primary":      "Envíanos alcance y plazos",
        "cta_primary_href": "contatti",
    },

    # ─── SETTORI ────────────────────────────────────────────────
    "settori": {
        "eyebrow":  "Sectores · donde nos movemos con soltura",
        "headline": "Seis sectores, <em>un solo método</em>, socios dedicados.",
        "intro":
            "Cada sector tiene un socio responsable y una legal ops "
            "de apoyo. Nuestro \"sector\" no es un claim de marketing "
            "— es la lista de asuntos que hemos trabajado lo "
            "suficiente como para estar seguros de no tener que "
            "aprenderlo en vuestro expediente.",

        "sectors_label":   "Las seis prácticas",
        "sectors_heading": "Donde <em>ya hemos resuelto</em> problemas como los vuestros.",

        "sectors": [
            {
                "num":   "01",
                "title": "Startup & Tech",
                "tagline": "Para founders en su primera o tercera ronda.",
                "pain_points": [
                    "Cap table y pacto de socios por ordenar",
                    "SAFE, nota convertible o term sheet por revisar antes de firmar",
                    "Stock options con el tratamiento fiscal 2026 correcto",
                    "Compliance RGPD + Reglamento de IA antes del pitch a inversores",
                ],
                "signals": [
                    "8 Series A cerradas en los últimos 24 meses",
                    "3 exits gestionadas lado vendor",
                    "Socia dedicada · Avv. Giorgia Martini",
                ],
                "case_snippet":
                    "Acompañamos a una fintech milanesa en su ronda "
                    "seed con un fondo italiano + un business angel UK "
                    "— cap table limpio en tres semanas, closing en seis.",
                "partner":    "Avv. Giorgia Martini",
                "legal_ops":  "Elena Vasile · legal ops lead",
            },
            {
                "num":   "02",
                "title": "Pymes y empresas familiares",
                "tagline": "Para empresarios de segunda o tercera generación.",
                "pain_points": [
                    "Relevo generacional con varias ramas familiares",
                    "Pactos de socios obsoletos o inexistentes",
                    "Entrada de un fondo minoritario en el capital",
                    "Gobierno corporativo con consejo todavía informal",
                ],
                "signals": [
                    "14 relevos generacionales cerrados desde 2019",
                    "5 entradas de fondos minority en pymes familiares",
                    "Socia dedicada · Avv. Chiara Belforte",
                ],
                "case_snippet":
                    "Un grupo familiar véneto del textil nos confió "
                    "el relevo entre tres hermanos y un primo segundo "
                    "— pacto de socios cerrado en doce semanas, cero "
                    "pleitos hereditarios abiertos.",
                "partner":    "Avv. Chiara Belforte",
                "legal_ops":  "Matteo Orsi · legal ops",
            },
            {
                "num":   "03",
                "title": "Laboral y RR. HH.",
                "tagline": "Para RR. HH. que deben moverse deprisa.",
                "pain_points": [
                    "Despido individual o colectivo por gestionar",
                    "Teletrabajo transfronterizo (empleados en UE o UK)",
                    "Reestructuración con bajas incentivadas",
                    "Stock options y retribución para scale-ups",
                ],
                "signals": [
                    "40+ despidos individuales cerrados en conciliación",
                    "12 planes de salida incentivada sin litigios abiertos",
                    "Socia dedicada · Avv. Sara Miccoli",
                ],
                "case_snippet":
                    "Una scale-up turinesa redujo su plantilla un "
                    "18 % sin un pleito abierto — usando nuestro "
                    "método de conciliación individual sobre 34 puestos.",
                "partner":    "Avv. Sara Miccoli",
                "legal_ops":  "Luca Tagliavini · legal ops",
            },
            {
                "num":   "04",
                "title": "Contratación B2B",
                "tagline": "Para equipos que firman MSA cada semana.",
                "pain_points": [
                    "MSA / DPA / SOW por estandarizar",
                    "Negociación redline con clientes enterprise",
                    "Licensing SaaS con contrapartes de EE. UU.",
                    "Archivo contractual fragmentado o inexistente",
                ],
                "signals": [
                    "Canal Slack dedicado · SLA 48 horas",
                    "Templates validados para 6 sectores verticales",
                    "Socio dedicado · Avv. Davide Romano",
                ],
                "case_snippet":
                    "Un SaaS B2B turinés nos confió toda la "
                    "contratación comercial — desde julio de 2024 "
                    "firmamos cada semana un MSA enterprise con "
                    "plazos medios de 8 días desde el primer borrador "
                    "hasta la firma.",
                "partner":    "Avv. Davide Romano",
                "legal_ops":  "Alice Piatti · legal ops",
            },
            {
                "num":   "05",
                "title": "Resolución de conflictos",
                "tagline": "Para cuando una negociación se tuerce.",
                "pain_points": [
                    "Conflicto con proveedor o cliente enterprise",
                    "Arbitraje bajo cláusula internacional",
                    "Mediación obligatoria previa al pleito",
                    "Gestión de crisis reputacional",
                ],
                "signals": [
                    "75 % de los conflictos cerrados sin sentencia",
                    "4 arbitrajes CCI gestionados en los últimos 24 meses",
                    "Socio dedicado · Avv. Marco Trentini",
                ],
                "case_snippet":
                    "Una pyme boloñesa con un conflicto de 2,8 M € "
                    "contra un proveedor alemán — cerrado en "
                    "mediación en 14 semanas con un acuerdo "
                    "transaccional más favorable que la demanda inicial.",
                "partner":    "Avv. Marco Trentini",
                "legal_ops":  "Irene Bonomi · legal ops",
            },
            {
                "num":   "06",
                "title": "Privacidad e IA",
                "tagline": "Para empresas que trabajan con datos o modelos.",
                "pain_points": [
                    "Auditoría RGPD antes de una ronda o un M&A",
                    "Análisis de brechas Reglamento de IA y mapa por clase de riesgo",
                    "EIPD sobre procesos críticos o modelos predictivos",
                    "Respuesta a brechas de datos y notificación al Garante",
                ],
                "signals": [
                    "Primera EIPD de Reglamento de IA italiana para marketplace B2C",
                    "6 auditorías RGPD previas a M&A sin impacto en el deal",
                    "Socia dedicada · Avv. Giulia Masi",
                ],
                "case_snippet":
                    "Un marketplace romano adecuó su plataforma al "
                    "Reglamento de IA antes de su entrada en vigor "
                    "efectiva — mapping completo, EIPD sobre 3 "
                    "procesos y política pública lista, todo en 6 semanas.",
                "partner":    "Avv. Giulia Masi",
                "legal_ops":  "Paolo Sangermano · legal ops",
            },
        ],

        "team_label":   "El equipo completo",
        "team_heading": "Ocho abogados, <em>dos legal ops</em>.",
        "team_intro":
            "El equipo del despacho — los nombres que aparecen en los "
            "expedientes y en las llamadas. No tenemos junior-of-record: "
            "los socios se sientan a la mesa desde el discovery hasta "
            "el closing, los legal ops operan el dashboard.",
        "team": [
            {"name": "Avv. Giorgia Martini",  "role": "Managing partner · Startup & Tech",         "office": "Milán",   "email": "giorgia@martinipartners.legal",
             "bio":  "12 años en DLA Piper · 2 Series A cerradas en 2025."},
            {"name": "Avv. Davide Romano",    "role": "Cofundador · Contratación B2B",             "office": "Turín",   "email": "davide@martinipartners.legal",
             "bio":  "10 años en Bird & Bird · LL.M. Fordham · contribuidor AIGA."},
            {"name": "Avv. Chiara Belforte",  "role": "Socia · Pymes y empresas familiares",       "office": "Bolonia", "email": "chiara@martinipartners.legal",
             "bio":  "15 años en despacho familiar emiliano · Bocconi."},
            {"name": "Avv. Sara Miccoli",     "role": "Socia · Laboral y RR. HH.",                 "office": "Milán",   "email": "sara@martinipartners.legal",
             "bio":  "Exresponsable del departamento laboral de una boutique milanesa."},
            {"name": "Avv. Marco Trentini",   "role": "Socio · Resolución de conflictos",          "office": "Milán",   "email": "marco@martinipartners.legal",
             "bio":  "Especializado en arbitrajes CCI y mediación comercial."},
            {"name": "Avv. Giulia Masi",      "role": "Socia · Privacidad e IA",                   "office": "Milán",   "email": "giulia@martinipartners.legal",
             "bio":  "Ex Autoridad Garante · doctorado en ética de la IA."},
            {"name": "Avv. Tommaso Neri",     "role": "Senior associate · Startup & M&A",          "office": "Turín",   "email": "tommaso@martinipartners.legal",
             "bio":  "6 años en boutique M&A milanesa · foco en scale-ups tech."},
            {"name": "Avv. Beatrice Riva",    "role": "Senior associate · Contract-as-a-Service",  "office": "Turín",   "email": "beatrice@martinipartners.legal",
             "bio":  "Especializada en SaaS licensing transfronterizo · IAPP CIPP/E."},
            {"name": "Elena Vasile",          "role": "Legal ops lead",                            "office": "Milán",   "email": "elena@martinipartners.legal",
             "bio":  "Ex operations manager en scale-up logística · diseña los flujos del dashboard."},
            {"name": "Matteo Orsi",           "role": "Legal ops · desk pymes",                    "office": "Bolonia", "email": "matteo@martinipartners.legal",
             "bio":  "Expasante en despacho fiscal boloñés · experto en archivística de expedientes."},
        ],

        "cta_heading": "¿Vuestro sector no está en esta lista?",
        "cta_intro":
            "Hay encargos que nos llegan fuera de los seis sectores — "
            "los aceptamos solo si tenemos experiencia específica o "
            "si co-trabajamos con un despacho socio. Escribidnos el "
            "alcance: en 24 horas os decimos si es nuestro campo.",
        "cta_primary":      "Contadnos el caso",
        "cta_primary_href": "contatti",
    },

    # ─── INSIGHTS ───────────────────────────────────────────────
    "insights": {
        "eyebrow":  "Insights · 2026",
        "headline": "Cuando cambia una norma, <em>escribimos una nota</em>.",
        "intro":
            "No tenemos newsletter. No tenemos secuencias de marketing. "
            "Cuando cambia una norma o un asunto llega al escritorio, "
            "alguien del despacho escribe una nota — la publicamos "
            "aquí porque nuestros clientes nos la piden, y nuestros "
            "candidatos la leen antes de la entrevista.",

        "card_topic_label":   "Práctica",
        "card_author_label":  "Por",
        "card_reading_label": "Lectura",

        "posts_intro":
            "Seis notas recientes. El archivo completo está en el "
            "dashboard cliente — aquí publicamos solo las de interés público.",

        "topics_label": "Prácticas",
        "topics":       ["Todos", "Startup & Tech", "Laboral y RR. HH.", "Privacidad e IA", "M&A", "Conflictos"],

        "cta_heading": "¿Queréis recibir nuestras notas antes?",
        "cta_intro":
            "Los clientes del despacho reciben las notas en el "
            "dashboard antes de la publicación. Si os interesa, "
            "reservad una llamada de discovery — y os enseñamos cómo funciona.",
        "cta_primary":      "Reservar reunión de estrategia",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Reunión de estrategia",
        "headline": "Treinta minutos, por vídeo, <em>sin compromiso</em>.",
        "intro":
            "El primer contacto es con un socio, no un BDR. Hablamos "
            "del alcance, los plazos y el eventual conflicto de "
            "interés — antes de cualquier propuesta económica. "
            "Gratuito, sin compromiso, respuesta de un socio real.",

        "slot_label": "Próxima cita disponible",
        "slot_value": "Jueves 17 de abril · 10:30",
        "slot_note":  "La llamada se realiza desde el dashboard cliente · no necesitas cuenta de Zoom",

        "form_label":   "Reservar la llamada",
        "form_heading": "Tres pasos, dos minutos, una conversación.",
        "form_intro":
            "La información se trata conforme al Reg. UE 679/2016 y "
            "se custodia en nuestro dashboard cifrado con acceso "
            "limitado a los socios. Sin CRM de terceros.",
        "form_fields": [
            {"name": "name",      "label": "Nombre",         "type": "text",     "required": True,  "placeholder": "Ej. Giorgia",
             "helper": "Solo el nombre de pila, gracias."},
            {"name": "surname",   "label": "Apellidos",      "type": "text",     "required": True,  "placeholder": "Ej. Rossi",
             "helper": "Tal como aparecen en los documentos corporativos."},
            {"name": "email",     "label": "Email",          "type": "email",    "required": True,  "placeholder": "giorgia@empresa.com",
             "helper": "Aceptamos también dominios consumer — no somos un despacho de negocios del siglo pasado."},
            {"name": "phone",     "label": "Teléfono",       "type": "tel",      "required": False, "placeholder": "+34 ...",
             "helper": "Opcional. Lo usamos solo si la llamada se cae."},
            {"name": "company",   "label": "Empresa o despacho", "type": "text", "required": True,  "placeholder": "Ej. Acme S.L.",
             "helper": "El nombre registrado o el comercial."},
            {"name": "company_type", "label": "Tipo de empresa", "type": "select", "required": True,
             "options": [
                 "Startup (pre-seed)",
                 "Startup (seed)",
                 "Scale-up (Serie A o posterior)",
                 "Pyme / empresa familiar",
                 "Scale-up madura / corporate",
                 "Profesional o freelance",
                 "Otro",
             ],
             "helper": "Sirve para ver si entráis en nuestra práctica."},
            {"name": "stage",      "label": "Momento",            "type": "select", "required": True,
             "options": [
                 "Todavía en discusión interna",
                 "Listos para arrancar en un mes",
                 "Listos para arrancar en tres meses",
                 "Exploratorio, sin urgencia",
             ],
             "helper": "Ayuda a reservar al socio adecuado para vuestro asunto."},
            {"name": "help_type",  "label": "Tipo de apoyo",      "type": "select", "required": True,
             "options": [
                 "No lo sé todavía · lo vemos en la llamada",
                 "Contratación B2B",
                 "Startup legal sprint / ronda",
                 "M&A o relevo generacional",
                 "Laboral, RR. HH., stock options",
                 "Privacidad, RGPD, Reglamento de IA",
                 "Litigación o conflictos",
                 "Fractional General Counsel",
             ],
             "helper": "Elegid \"No lo sé todavía\" si el alcance abarca varias áreas."},
            {"name": "message",   "label": "Contadnos el caso",   "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Máx. 600 caracteres. Sin nombres de contrapartes ni datos sensibles — los vemos en la llamada tras NDA recíproca.",
             "helper": "Lo justo para ver si es nuestro campo. "
                       "Los nombres de contrapartes se comparten solo tras NDA."},
        ],

        "form_sections": [
            {"num": "01", "title": "Quién eres",
             "meta": "La persona con la que hablaremos en la llamada.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "A qué os dedicáis",
             "meta": "Para el conflict-check preliminar.",
             "fields": ["company", "company_type", "stage"]},
            {"num": "03", "title": "Qué necesitáis",
             "meta": "Ningún detalle sensible aquí — entramos en el fondo solo tras NDA recíproca.",
             "fields": ["help_type", "message"]},
        ],

        "form_submit_label": "Reservar la reunión de estrategia",
        "form_submit_note":
            "Respuesta de un socio real en 2 horas hábiles. "
            "Sin BDR, sin secuencias, sin \"en breve os contactamos\".",
        "form_consent":
            "Consiento el tratamiento de mis datos personales "
            "conforme al Reglamento UE 679/2016. Los datos se "
            "custodian en el dashboard cifrado del despacho con "
            "acceso limitado a los socios. Ningún dato se comunica "
            "a terceros sin autorización expresa.",

        "office_address_label": "Dirección",
        "office_area_label":    "Barrio",
        "office_phone_label":   "Teléfono",
        "office_email_label":   "Email",

        "offices_label": "Las tres oficinas",
        "offices": [
            {
                "city":    "Milán",
                "tag":     "Sede central",
                "address": "Via Solferino 40 · 20121",
                "area":    "Brera · a dos pasos de la Piazza della Scala",
                "phone":   "+39 02 4546 7789",
                "email":   "milano@martinipartners.legal",
                "note":    "Todas las prácticas · salas de reunión reservables desde el dashboard",
            },
            {
                "city":    "Turín",
                "tag":     "Desk scale-up",
                "address": "Via Roma 324 · 10123",
                "area":    "Centro · cerca de la Piazza Castello",
                "phone":   "+39 011 5667 2240",
                "email":   "torino@martinipartners.legal",
                "note":    "Desk scale-up tech · sede principal contract-as-a-service",
            },
            {
                "city":    "Bolonia",
                "tag":     "Desk pymes",
                "address": "Via Indipendenza 18 · 40121",
                "area":    "Centro · cerca de la Piazza Maggiore",
                "phone":   "+39 051 3344 8812",
                "email":   "bologna@martinipartners.legal",
                "note":    "Desk pymes y M&A mid-market · corredor Emilia-Romaña",
            },
        ],

        "channels_label": "Canales directos",
        "channels": [
            ("Email general",       "hello@martinipartners.legal", "Respuesta en 2 horas hábiles"),
            ("Centralita Milán",    "+39 02 4546 7789",             "Lun – Vie · 09:00 – 19:00"),
            ("LinkedIn corporativo","in/martini-partners",          "Notas públicas y AMA semanales"),
        ],

        "footnote":
            "Martini & Partners no hace cold outreach. Si alguien se "
            "presenta como BDR en nuestro nombre, no somos nosotros. "
            "Todas las relaciones nacen de una recomendación, de la "
            "lectura de alguna de nuestras notas o de este formulario.",
    },

    # ─── POSTS ──────────────────────────────────────────────────
    "posts": [
        {
            "slug":     "ai-act-pmi-italiane",
            "title":    "Reglamento de IA · qué cambia para las pymes italianas",
            "topic":    "Privacidad e IA",
            "date":     "17 de abril de 2026",
            "reading":  "8 min",
            "author":   "Avv. Giulia Masi",
            "lead":
                "El Reglamento de IA entra en aplicación efectiva el "
                "2 de agosto de 2026 para los sistemas de alto riesgo. "
                "Para las pymes italianas que usan modelos predictivos "
                "en producción — marketplaces, scoring de clientes, "
                "HR tech — la ventana para adecuarse es de cuatro "
                "meses. Así lo estamos haciendo con nuestros clientes.",
            "sections": [
                {
                    "heading": "Por qué afecta también a las pymes",
                    "body":
                        "La lectura común es que el Reglamento de IA "
                        "solo golpea a los gigantes — OpenAI, Mistral, "
                        "Meta. Es errónea. La Directiva clasifica por "
                        "uso, no por tamaño de la empresa que "
                        "desarrolla. Un algoritmo de scoring crediticio "
                        "hecho en casa por una fintech seed cae en "
                        "alto riesgo exactamente como uno de un banco "
                        "de inversión — y la pyme tiene menos recursos "
                        "para adecuarse.",
                },
                {
                    "heading": "Las cuatro clases de riesgo",
                    "body":
                        "Riesgo inaceptable (prohibido), alto riesgo "
                        "(requisitos muy estrictos), riesgo limitado "
                        "(transparencia obligatoria), riesgo mínimo "
                        "(sin obligaciones específicas). Mapear los "
                        "sistemas corporativos en las cuatro clases "
                        "es el primer paso — y para las pymes requiere "
                        "de media dos semanas de trabajo con un legal "
                        "ops + un product manager.",
                },
                {
                    "heading": "Qué hacer ya",
                    "body":
                        "Tres acciones concretas: un inventario "
                        "completo de los sistemas IA en producción "
                        "(incluyendo plug-ins de terceros como "
                        "chatbots o motores de recomendación), una "
                        "EIPD integrada para los sistemas de alto "
                        "riesgo y una política pública que declare "
                        "el uso de IA en procesos decisionales que "
                        "afecten a clientes o empleados. Para la "
                        "mayoría de las pymes es un proyecto de seis "
                        "semanas — nuestro Reglamento de IA Readiness "
                        "lo cubre de forma integral.",
                },
            ],
            "takeaway":
                "El Reglamento de IA no es un trámite burocrático — "
                "es una oportunidad para ordenar los sistemas que "
                "usan datos de clientes o empleados. Quien se adapta "
                "bien hoy vende mejor mañana.",
            "tags":     ["Reglamento de IA", "RGPD", "Compliance", "Pymes"],
        },
        {
            "slug":     "stock-option-2026",
            "title":    "Stock options 2026 · nuevo régimen fiscal",
            "topic":    "Startup & Tech",
            "date":     "14 de abril de 2026",
            "reading":  "6 min",
            "author":   "Avv. Giorgia Martini",
            "lead":
                "La Ley de Presupuestos italiana 2026 ha modificado "
                "el tratamiento fiscal de los planes de stock options "
                "para startups y pymes innovadoras. La modificación "
                "es favorable — pero la redacción deja márgenes de "
                "interpretación. Veamos cómo estamos montando los "
                "planes nuevos y qué hacer con los existentes. "
                "(En España, la Ley de Startups 2022 establece un "
                "marco paralelo que comparamos al final de la nota.)",
            "sections": [
                {
                    "heading": "Qué cambia desde el 1 de enero de 2026",
                    "body":
                        "La tributación se aplica en el momento de la "
                        "venta efectiva de las acciones (ya no al "
                        "vesting) para startups innovadoras inscritas "
                        "en el registro especial. El tipo de capital "
                        "gain se mantiene al 26 %. Es un cambio "
                        "relevante: elimina la paradoja del empleado "
                        "que paga impuestos sobre acciones que todavía "
                        "no ha monetizado.",
                },
                {
                    "heading": "¿Hay que reescribir los planes existentes?",
                    "body":
                        "No necesariamente. El nuevo régimen se "
                        "aplica de forma automática a los planes que "
                        "respetan los requisitos — inscripción como "
                        "startup innovadora, vesting mínimo de 24 "
                        "meses, asignación a empleados o "
                        "administradores en continuidad de relación. "
                        "La mayoría de los planes recientes ya son "
                        "compatibles. Los planes escritos antes de "
                        "2022 en cambio casi siempre requieren una actualización.",
                },
                {
                    "heading": "Cómo montar los planes nuevos",
                    "body":
                        "Tres cosas por hacer bien: redactar el "
                        "reglamento interno con referencia explícita "
                        "al régimen 2026, documentar la fecha de "
                        "asignación y el plan de vesting individual "
                        "para cada empleado, y facilitar al empleado "
                        "una guía fiscal en italiano en el momento "
                        "de la asignación. Nuestro template de plan "
                        "SO/SAR ya está actualizado.",
                },
            ],
            "takeaway":
                "Para las startups innovadoras el nuevo régimen es "
                "una simplificación neta — y un argumento más para "
                "convencer a un senior de dejar una gran empresa "
                "para entrar en un equipo founder.",
            "tags":     ["Stock options", "Startup", "Fiscal", "RR. HH."],
        },
        {
            "slug":     "smart-working-confine",
            "title":    "Teletrabajo transfronterizo · tres escenarios",
            "topic":    "Laboral y RR. HH.",
            "date":     "11 de abril de 2026",
            "reading":  "7 min",
            "author":   "Avv. Sara Miccoli",
            "lead":
                "Desde 2023 la mayoría de las empresas italianas ha "
                "aceptado el teletrabajo transfronterizo — pero las "
                "reglas sobre cotizaciones sociales, retenciones "
                "fiscales y jurisdicción del derecho laboral aplicable "
                "siguen siendo confusas. Tres escenarios tipo que "
                "vemos cada mes.",
            "sections": [
                {
                    "heading": "Escenario 1 · Empleado italiano que se traslada a España",
                    "body":
                        "Si el empleado trabaja más de 183 días al "
                        "año en España, se convierte en residente "
                        "fiscal español — la empresa italiana debe "
                        "aportar cotizaciones Seguridad Social "
                        "española (convenio bilateral) y retenciones "
                        "IRPF españolas. La ley del contrato de "
                        "trabajo sigue siendo italiana si se pacta "
                        "expresamente, pero los derechos mínimos "
                        "españoles (vacaciones, despido) se aplican igualmente.",
                },
                {
                    "heading": "Escenario 2 · Empleado UE que se traslada a Italia",
                    "body":
                        "Más sencillo pero no trivial. La empresa se "
                        "convierte en sustituto de impuestos italiano, "
                        "abre posición INPS y aporta cotizaciones "
                        "italianas. Si el empleado tiene un contrato "
                        "francés o alemán original, hay que "
                        "renegociar — muchas empresas optan por "
                        "suscribir un nuevo contrato italiano con "
                        "cláusula de continuidad.",
                },
                {
                    "heading": "Escenario 3 · Empleado italiano que se traslada fuera de la UE",
                    "body":
                        "El más delicado. Sin convenio bilateral "
                        "adecuado (p. ej. EE. UU., Canadá), hay "
                        "riesgo de doble imposición fiscal y doble "
                        "cotización social. La solución limpia es "
                        "casi siempre un contrato local con entidad "
                        "extranjera (filial o PEO / EOR) — mantener "
                        "el contrato italiano con desplazamiento "
                        "largo es sostenible solo 18-24 meses como máximo.",
                },
            ],
            "takeaway":
                "Antes de decir sí a un teletrabajo transfronterizo, "
                "verificad siempre el país de destino. Las reglas "
                "cambian entre UE, UK, EE. UU. y resto del mundo — "
                "y los costes para la empresa pueden variar un 30 % "
                "entre escenarios distintos.",
            "tags":     ["Teletrabajo", "RR. HH.", "Transfronterizo", "Laboral"],
        },
        {
            "slug":     "contratti-saas-enterprise",
            "title":    "Contratos SaaS enterprise · tres cláusulas que no deben faltar",
            "topic":    "Contratación B2B",
            "date":     "8 de abril de 2026",
            "reading":  "5 min",
            "author":   "Avv. Davide Romano",
            "lead":
                "Después de firmar más de trescientos MSA SaaS "
                "enterprise en los últimos tres años, tenemos una "
                "lista mental de cláusulas que no deberían faltar. "
                "Tres que recomendamos siempre, incluso cuando el "
                "cliente \"no las ha visto nunca\".",
            "sections": [
                {
                    "heading": "1. Liability cap proporcionado y no inferior a 12 meses de fees",
                    "body":
                        "El cap de responsabilidad estándar propuesto "
                        "por los grandes vendors (Salesforce, "
                        "ServiceNow) suele ser de 12 meses de fees "
                        "del servicio. Aceptarlo es razonable · "
                        "negociarlo a la baja a 3 o 6 meses es con "
                        "frecuencia posible para deals bajo 500 K €.",
                },
                {
                    "heading": "2. Data portability y cláusula de export",
                    "body":
                        "El derecho a exportar todos los datos en un "
                        "formato machine-readable en un plazo de 30 "
                        "días desde el termination, sin costes "
                        "añadidos. Suele estar ausente, casi siempre negociable.",
                },
                {
                    "heading": "3. Sub-processor notice period",
                    "body":
                        "El derecho a ser notificados al menos 30 "
                        "días antes de un cambio de sub-processor "
                        "(hosting, email, analytics) — con derecho "
                        "de opt-out sin penalización si el nuevo "
                        "sub-processor no respeta los estándares acordados.",
                },
            ],
            "takeaway":
                "Estas tres cláusulas están en el 70 % de los "
                "contratos enterprise que firmamos — el 30 % "
                "restante se convence con un drafting claro. "
                "Tenemos un template listo en el dashboard.",
            "tags":     ["SaaS", "Contratos", "Enterprise", "B2B"],
        },
        {
            "slug":     "mandati-m-and-a-2025",
            "title":    "M&A mid-market · lo que aprendimos en 2025",
            "topic":    "M&A",
            "date":     "4 de abril de 2026",
            "reading":  "9 min",
            "author":   "Avv. Chiara Belforte",
            "lead":
                "En 2025 cerramos siete operaciones de M&A mid-market "
                "— tres lado vendor, cuatro lado acquirer, cinco "
                "italianas y dos transfronterizas. Tres tendencias "
                "que vimos repetirse lo suficiente para merecer una nota.",
            "sections": [
                {
                    "heading": "Los earn-outs han vuelto",
                    "body":
                        "Después de dos años en los que las cesiones "
                        "se cerraban con precio fijo y salida del "
                        "fundador a 6-12 meses, en 2025 el earn-out "
                        "ha reaparecido. También en el mid-market. "
                        "Normalmente 25-35 % del precio ligado a "
                        "KPI operativos post-closing, duración 24-36 "
                        "meses. Para el fundador es una oportunidad "
                        "pero requiere un contrato de earn-out bien "
                        "redactado para evitar litigios.",
                },
                {
                    "heading": "La due diligence IA/privacidad se ha normalizado",
                    "body":
                        "Incluso el fondo más clásico ya pide un "
                        "resumen del compliance RGPD y un mapa de "
                        "los sistemas IA antes de firmar. Una "
                        "auditoría preventiva vendor-side cuesta "
                        "5-10 K € y hace ganar 2-3 semanas en el proceso.",
                },
                {
                    "heading": "Los signings transfronterizos requieren más tiempo",
                    "body":
                        "Las dos operaciones italo-DACH de 2025 "
                        "requirieron de media 8 semanas más que los "
                        "signings italianos puros — entre traducción "
                        "jurada de escrituras, aprobación antitrust "
                        "y coordinación con notario alemán. Mejor "
                        "planificarlo desde el inicio que descubrirlo "
                        "en la due.",
                },
            ],
            "takeaway":
                "2025 ha normalizado el earn-out y hecho estándar "
                "la due diligence IA/privacidad. En cross-border, "
                "mejor sobreplanificar el tiempo que estresar el closing.",
            "tags":     ["M&A", "Fondos", "Due diligence", "Transfronterizo"],
        },
        {
            "slug":     "dashboard-cliente-perche",
            "title":    "Por qué construimos un dashboard cliente (en vez de comprarlo)",
            "topic":    "Startup & Tech",
            "date":     "28 de marzo de 2026",
            "reading":  "6 min",
            "author":   "Avv. Giorgia Martini",
            "lead":
                "En 2020 evaluamos Clio, MyCase, PracticePanther y "
                "otros seis softwares de \"practice management\" "
                "para despachos. Ninguno nos convencía. Construimos "
                "el nuestro — internamente, con un product manager "
                "a tiempo parcial. He aquí por qué, y qué aprendimos.",
            "sections": [
                {
                    "heading": "El problema de los PM jurídicos estándar",
                    "body":
                        "Los softwares practice management para "
                        "despachos están construidos para despachos "
                        "de 50+ personas que facturan por hora. La "
                        "UX está pensada para secretarias y abogados "
                        "que rellenan timesheets. Nosotros somos "
                        "diez personas, no facturamos por hora y "
                        "nuestros clientes son product managers "
                        "acostumbrados a Linear. Incompatible.",
                },
                {
                    "heading": "Qué construimos",
                    "body":
                        "Un workspace al estilo Linear + Notion con "
                        "kanban para los asuntos, un archivo "
                        "documental cifrado, un calendario compartido "
                        "de plazos y un canal de chat para cada "
                        "expediente. Sin timesheets — las horas se "
                        "trazan a fin de semana, a la vista para el "
                        "cliente. Seis meses de desarrollo, coste "
                        "80 K €, hoy lo usan todos.",
                },
                {
                    "heading": "Por qué fue una ventaja comercial",
                    "body":
                        "Descubrimos a posteriori que el dashboard "
                        "es el primer motivo por el que los clientes "
                        "nos eligen. En los pitches mostramos un "
                        "walkthrough de dos minutos del workspace "
                        "real — y para empresas acostumbradas a "
                        "Linear + Notion es un game-changer frente "
                        "a los PDF por email de los demás despachos.",
                },
            ],
            "takeaway":
                "Haz lo que los demás no quieren hacer. El dashboard "
                "fue la inversión más importante de nuestros primeros "
                "ocho años — más que cualquier oficina nueva o nueva contratación.",
            "tags":     ["Dashboard", "Product", "Despacho", "Tooling"],
        },
    ],
}

# D-047 compliance note:
# Spanish locale tree · same shape as JURIS_CONTENT_IT. The skin files
# never author any Spanish literal — every user-facing string in ES
# flows through this file.
