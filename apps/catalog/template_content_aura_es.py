"""Aura — Digital Studio · ES content registry.

Agency live rollout, Phase 2g3.6f · Spanish (peninsular) locale.

Voice contract (Xataka / K Fund / Barcelona product-studio register):
- Registro producto / SaaS peninsular. "Tú" en los CTA
  ("reserva una call", "cuéntanos", "hablémoslo").
- Léxico: "sprint", "discovery", "backlog", "telemetría", "dashboard",
  "onboarding", "NPS", "funnel", "A/B test", "rollout", "retención",
  "time to value". Anglicismos aceptados — es el registro real.
- Nombres de clientes permanecen (Casavo, Fastweb, Soldo, Milkman,
  Lendlease, Fiscozen). Stack en inglés. Sprint chip permanece.
- Unidades numéricas: "sett." → "sem.", "min." → "min", "gg" → "d".
- Euros peninsular: "€ 840K" → "840 K€" o "840.000 €".
"""
from __future__ import annotations

from typing import Any


AURA_CONTENT_ES: dict[str, Any] = {

    "pages": [
        {"slug": "home",         "label": "Estudio",        "kind": "home"},
        {"slug": "studio",       "label": "Quiénes somos",  "kind": "about"},
        {"slug": "capabilities", "label": "Capabilities",   "kind": "services"},
        {"slug": "lavori",       "label": "Trabajos",       "kind": "project_list"},
        {"slug": "sprint",       "label": "Sprint",         "kind": "process"},
        {"slug": "brief",        "label": "Brief",          "kind": "contact"},
    ],

    # ── Site chrome ──────────────────────────────────────────────
    "site": {
        "logo_word":   "Aura",
        "tag":         "Digital · product · growth studio",
        "sprint_chip": "Sprint 07/Q2 · live",
        "nav_cta":     "Reserva una call",
        "inquiry_page_slug": "brief",
        "phone":       "+39 02 8728 4411",
        "email":       "hello@aura.studio",
        "address":     "Via Paolo Sarpi 41 · 20154 Milán",
        "hours_compact":"Call slots · lun — jue · 10 — 18",
        "license":     "P.IVA 12890440964 · Milán",
        "footer_intro":
            "Estudio digital independiente. Diseñamos productos, "
            "plataformas y sistemas de crecimiento para scale-ups y "
            "empresas tech. Con base en Milán, delivery europeo.",
        "foot_shiplog_label":    "// ship log · last 6",
        "foot_current_sprint":   "sprint 07/Q2 · live",
        "foot_shiplog_rows": [
            ("ayer · 18:04", "v2.14",  "Soldo — nuevo onboarding corporate live"),
            ("ayer · 09:21", "v2.13",  "Fastweb Plus — dashboard residencial v2.3"),
            ("lun · 15:30",  "v2.12",  "Lendlease — portal asset manager"),
            ("vie · 11:12",  "v2.11",  "Casavo — retention A/B loop 003"),
            ("jue · 17:45",  "v2.10",  "Milkman — SDK ship tracking"),
            ("mié · 10:02",  "v2.09",  "Fiscozen — onboarding self-serve"),
        ],
        "foot_stack_marquee": [
            "Figma", "Linear", "Notion", "GitHub", "Vercel", "Stripe",
            "Segment", "PostHog", "Supabase", "Framer", "Mixpanel", "Sentry",
        ],
        "foot_studio_label":  "Estudio",
        "foot_stack_label":   "Stack delivery",
        "foot_stack_rows": [
            "Design — Figma · Framer",
            "Dev — Next.js · TypeScript",
            "Data — PostHog · Segment",
            "Payments — Stripe · Checkout",
            "Infra — Vercel · Supabase",
        ],
        "foot_boot_line":
            "aura.studio · uptime 99.98 · last deploy 4 min ago · built in Milano",
    },

    # ── HOME ─────────────────────────────────────────────────────
    "home": {
        "chip": "3 slots disponibles · Q3 2026",
        "headline": "De la <em>call de discovery</em> al <em>primer KPI</em> en seis semanas.",
        "intro":
            "Somos un estudio digital que construye productos y "
            "sistemas de crecimiento para scale-ups italianas y europeas. "
            "Sprints de dos semanas, dashboard compartido, "
            "entregas medibles. Cero agencia, todo producto.",
        "primary_cta":   "Reserva una call",
        "primary_href":  "brief",
        "secondary_cta": "Trabajos recientes",
        "secondary_href":"lavori",

        "hero_metrics": [
            ("<em>47</em>",     "productos enviados desde 2019"),
            ("<em>+34%</em>",   "conversión mediana tras rework"),
            ("<em>6 sem.</em>","del sprint cero al primer KPI"),
        ],

        # Dashboard console tile
        "console": {
            "path":           "aura.studio/clients/casavo/live",
            "status_chip":    "LIVE · sprint 07/Q2",
            "primary_metric": "+34%",
            "primary_label":  "Conversión tras rework · últimos 30 días",
            "kpi": [
                ("<em>+18%</em>",    "Retención día 30"),
                ("<em>Δ 22</em>",    "NPS pre / post · Casavo"),
                ("<em>840 K€</em>",  "MRR · sprint 1 – 14"),
                ("<em>99,98%</em>",  "Uptime último trimestre"),
            ],
            "meta_label":     "Sprint actual",
            "meta_value":     "07/Q2 · week 2 of 2",
        },

        # Capabilities mini
        "capab_label":   "Capabilities",
        "capab_heading": "Cuatro <em>áreas</em>, un solo equipo.",
        "capab_intro":
            "Trabajamos sobre cuatro tipos de proyecto — lanzamientos de producto, "
            "rediseños de plataforma, sistemas de crecimiento y delivery de "
            "plataformas B2B. Cada proyecto pasa por un equipo de 3-5 personas "
            "dedicadas, nunca por una capa de account.",
        "capab_cards": [
            {
                "id":   "C.01",
                "title":"Product <em>launch</em>",
                "body": "Del concept al onboarding live. "
                        "Ideal para scale-ups en Serie A que deben "
                        "pasar de MVP a producto que paga.",
                "tags": ["Discovery", "Design system", "Next.js", "Analytics"],
            },
            {
                "id":   "C.02",
                "title":"Platform <em>redesign</em>",
                "body": "Repensar productos maduros sin perder usuarios. "
                        "Research, A/B test, migración progresiva.",
                "tags": ["UX audit", "A/B", "Incremental ship", "PostHog"],
            },
            {
                "id":   "C.03",
                "title":"Growth <em>systems</em>",
                "body": "Onboarding, retención, referral, pricing experiments. "
                        "Quick wins en los primeros 30 días, sistemas a 90 días.",
                "tags": ["Onboarding", "Retención", "Pricing", "Experiments"],
            },
            {
                "id":   "C.04",
                "title":"B2B <em>delivery</em>",
                "body": "Portales asset manager, dashboards corporate, "
                        "backoffice internos. Integración SSO + data warehouse.",
                "tags": ["Dashboards", "SSO", "Roles", "BigQuery"],
            },
        ],

        # Sprint strip
        "sprint_label":   "La manera en que entregamos",
        "sprint_heading": "Cuatro <em>sprints</em>, del discovery a la escala.",
        "sprint_intro":
            "Cada proyecto se estructura en sprints de dos semanas. "
            "Ves exactamente qué estamos haciendo, cuándo se entregará, "
            "y qué métricas estamos moviendo. Ninguna sorpresa a fin de mes.",
        "sprints": [
            {
                "id":"S.00", "duration":"Sprint 0 · 1 semana",
                "title":"<em>Signal</em>",
                "body": "Discovery con stakeholders, usuarios, dashboard. "
                        "Entrega: brief compartido + backlog inicial.",
                "output": "OUT · brief + backlog",
            },
            {
                "id":"S.01", "duration":"Sprint 1 — 2 · 4 sem.",
                "title":"<em>Sketch</em>",
                "body": "Design system + prototipos testeables. "
                        "Research cualitativa + primeros A/B sobre las hipótesis críticas.",
                "output": "OUT · prototype + design tokens",
            },
            {
                "id":"S.02", "duration":"Sprint 3 — 5 · 6 sem.",
                "title":"<em>Ship</em>",
                "body": "Implementación staging → producción. "
                        "Monitorización live de métricas, rollback a 1 clic.",
                "output": "OUT · production + first KPI",
            },
            {
                "id":"S.03", "duration":"Sprint 6+ · ongoing",
                "title":"<em>Scale</em>",
                "body": "Experimentos continuos, feature expansion, "
                        "optimización post-launch. Ship log compartido.",
                "output": "OUT · weekly ship-log",
            },
        ],

        # Lavori cards
        "work_label":      "Trabajos recientes",
        "work_heading":    "Siete <em>productos</em>, siete <em>métricas</em>.",
        "work_intro":
            "Cada proyecto tiene una métrica clara, declarada en el sprint cero "
            "y medida en el sprint tres. Si la métrica no se mueve, trabajamos "
            "gratis hasta que se mueva.",
        "work_page_slug": "lavori",
        "work_cards": [
            {
                "slug": "casavo-retention-rework",
                "id":   "W.01",
                "cover":"https://images.unsplash.com/photo-1551434678-e076c223a692?w=900&q=80&auto=format&fit=crop",
                "title":"Rework de retención en tres meses",
                "client":"Casavo · Proptech Milán",
                "metric_chip": "+18% retención · D30",
                "stack":["Next.js", "PostHog", "Figma"],
            },
            {
                "slug": "fastweb-plus-dashboard",
                "id":   "W.02",
                "cover":"https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=900&q=80&auto=format&fit=crop",
                "title":"Dashboard residencial v2",
                "client":"Fastweb · Telco Italia",
                "metric_chip": "NPS +22 · 6 meses",
                "stack":["React", "Django", "Segment"],
            },
            {
                "slug": "soldo-corporate-onboarding",
                "id":   "W.03",
                "cover":"https://images.unsplash.com/photo-1559028012-481c04fa702d?w=900&q=80&auto=format&fit=crop",
                "title":"Onboarding corporate self-serve",
                "client":"Soldo · Fintech pan-EU",
                "metric_chip": "-54% time to activate",
                "stack":["Next.js", "Stripe", "Mixpanel"],
            },
        ],

        "metric_strip": [
            ("<em>47</em>",      "productos enviados",   "desde 2019 — media 8 / año"),
            ("<em>+34%</em>",    "conversión mediana",   "entre pre y post rework"),
            ("<em>99,98%</em>",  "uptime",               "último trimestre · status.aura.studio"),
            ("<em>6 sem.</em>", "time to first KPI",    "del sprint cero a la primera métrica movida"),
        ],

        "cta_label":   "Próxima call",
        "cta_heading": "Tres <em>slots</em> abiertos para Q3 2026.",
        "cta_sub":
            "El primer slot es una call de discovery de 30 minutos. Si el "
            "proyecto es para nosotros, en los 5 días siguientes recibes un "
            "brief de lectura + estimación de sprint cero.",
        "cta_chip":    "30 min · zero commitment",
        "cta_primary": "Reserva una call",
    },

    # ── STUDIO (about) ───────────────────────────────────────────
    "studio": {
        "chip": "Equipo · 11 personas · Milán + remoto",
        "headline": "Un equipo de <em>once</em>, <em>ocho años</em> de productos enviados.",
        "standfirst":
            "Aura es un estudio de product design e ingeniería fundado en "
            "Milán en 2019. Once personas — cinco designers, cuatro "
            "engineers, dos product managers — distribuidas entre Milán, Turín "
            "y remoto. Cero account managers, cero niveles intermedios: "
            "quien firma el brief es quien lo ship-ea.",

        "facts": [
            ("<em>11</em>",    "personas",           "5 design · 4 eng · 2 PM"),
            ("<em>47</em>",    "productos enviados", "De 2019 a hoy"),
            ("<em>3</em>",     "sedes",              "Milán · Turín · remoto"),
            ("<em>94%</em>",   "clientes renuevan",   "Tasa de retención 2024"),
        ],

        "story_label":   "Historia del estudio",
        "story_heading": "Cómo las <em>scale-ups</em> nos obligaron a repensar el design studio.",
        "story_paragraphs": [
            "Aura nace en 2019 de la mano de Luca Bianchi y Sofia Reggiani, "
            "ex product designers en Spotify y Figma. La idea inicial era "
            "sencilla: <em>no queremos ser una agencia, no queremos "
            "ser freelances</em>. Queríamos un estudio que trabajase "
            "como un equipo interno — con las mismas herramientas, las mismas "
            "métricas, la misma cadencia — pero desde fuera.",
            "Los primeros tres años fueron de aprendizaje. Entendimos "
            "que las scale-ups italianas no necesitaban <em>design</em> "
            "— necesitaban <em>delivery</em>. Así contratamos "
            "engineers full-stack. Entendimos que no bastaba la design "
            "review — hacía falta el ship log. Entendimos que el valor "
            "no estaba en los mockups, sino en las métricas movidas.",
            "Hoy Aura trabaja con 6-8 clientes al año, en sprints de dos "
            "semanas, con una métrica declarada al inicio de cada "
            "proyecto. Cada proyecto publica un ship log interno que el "
            "cliente puede leer en tiempo real. Si la métrica no se "
            "mueve, trabajamos gratis hasta que se mueva. "
            "Es la única manera en que sabemos trabajar.",
        ],

        "team_label":   "El equipo",
        "team_heading": "Quién <em>envía</em> los proyectos.",
        "team_intro":
            "Cada proyecto lo lleva un equipo dedicado de 3-5 personas. "
            "Los equipos se componen según el tipo de proyecto y no "
            "cambian sobre la marcha. Quien empieza el proyecto, lo envía.",
        "team": [
            {
                "name": "Luca Bianchi",
                "role": "Cofundador · Head of product",
                "bio":  "Ex Spotify (Estocolmo · 2014-2018) y Figma "
                        "(San Francisco · 2018-2019). Lideró el "
                        "equipo de growth design para el mercado EU. "
                        "Se encarga de la definición de los sprints.",
                "portrait": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=900&q=80&auto=format&fit=crop",
                "stack": ["Figma", "Linear", "PostHog", "Notion"],
            },
            {
                "name": "Sofia Reggiani",
                "role": "Cofundadora · Head of engineering",
                "bio":  "Ex Spotify (Estocolmo) y Google (Londres). "
                        "Lideró la migración Next.js de dos plataformas "
                        "paneuropeas. Se encarga del stack de delivery.",
                "portrait": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop",
                "stack": ["Next.js", "TypeScript", "Vercel", "Supabase"],
            },
            {
                "name": "Matteo Leone",
                "role": "Principal product designer",
                "bio":  "Ocho años en Satispay (Milán) antes de "
                        "incorporarse a Aura en 2022. Ha diseñado tres "
                        "onboardings para fintechs italianas con >1M usuarios.",
                "portrait": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=900&q=80&auto=format&fit=crop",
                "stack": ["Figma", "Framer", "Stripe Elements"],
            },
        ],

        "values_label":   "Cómo trabajamos",
        "values_heading": "<em>Cuatro reglas</em> innegociables.",
        "values": [
            ("V.01", "Una <em>métrica</em> declarada",
             "Cada proyecto tiene una métrica clara definida en el sprint cero. "
             "Si no se mueve, nos quedamos hasta que se mueva."),
            ("V.02", "Un <em>equipo</em> dedicado",
             "Quien empieza el proyecto, lo envía. Cero account managers, "
             "cero handoffs. El designer que diseña es el mismo que ship-ea."),
            ("V.03", "Un <em>ship log</em> público",
             "El cliente tiene acceso en tiempo real al ship log interno. "
             "Ve qué hemos enviado, cuándo, por qué, y qué ha fallado."),
            ("V.04", "Una <em>call</em> a la semana",
             "Una sola reunión síncrona por semana, de 30 minutos, "
             "con agenda escrita. El resto es async en Linear y Slack."),
        ],
    },

    # ── CAPABILITIES (services) ──────────────────────────────────
    "capabilities": {
        "chip": "4 áreas · 3-5 personas por proyecto",
        "headline": "Cuatro <em>capabilities</em>, todas medidas.",
        "standfirst":
            "Cada capability tiene un método documentado, una métrica típica, "
            "una duración previsible y un stack predefinido. No es un "
            "tarifario — es un sistema que nos permite decirte, en sprint cero, "
            "qué esperar y cuándo.",

        "capabilities": [
            {
                "id": "CAP.01 · Product launch",
                "title": "Llevar <em>un producto nuevo</em> a la primera conversión.",
                "tagline": "Típico: 14 — 20 sem. · KPI · activación + first paid",
                "body":
                    "Para scale-ups que han validado el problema (Serie Seed / A) "
                    "y deben construir el producto que paga. Partimos del "
                    "sprint cero (research + backlog), pasamos por el design "
                    "system + los tres flows críticos, llevamos a producción "
                    "con onboarding medible y pricing vivo.",
                "scope_label": "// scope",
                "scope": [
                    "Sprint cero + user research",
                    "Design system (tokens + 60 componentes)",
                    "Tres flows críticos en producción",
                    "Onboarding self-serve",
                    "Pricing page live + Stripe",
                    "Analytics + funnel completo",
                    "Rollback + feature flag",
                    "Handover docs al equipo interno",
                ],
                "stack": ["Next.js 14", "TypeScript", "Figma", "Stripe", "Segment", "PostHog"],
            },
            {
                "id": "CAP.02 · Platform redesign",
                "title": "<em>Rediseñar</em> un producto maduro sin perder usuarios.",
                "tagline": "Típico: 20 — 30 sem. · KPI · retención + NPS",
                "body":
                    "Para plataformas con > 50k usuarios activos que han acumulado "
                    "deuda de UX. Partimos de un audit cuantitativo + cualitativo, "
                    "construimos el nuevo sistema en paralelo, migramos "
                    "progresivamente vía feature flag. Ningún big-bang launch.",
                "scope_label": "// scope",
                "scope": [
                    "UX audit + quant analysis",
                    "30+ entrevistas de usuario",
                    "Migración progresiva",
                    "A/B test por cohorte",
                    "Design system evolution",
                    "Rollout por mercado",
                    "Post-launch tuning · 8 sem.",
                    "Training equipo interno",
                ],
                "stack": ["React", "Django", "PostHog", "Segment", "Split.io"],
            },
            {
                "id": "CAP.03 · Growth systems",
                "title": "<em>Sistemas de crecimiento</em> medibles en 30 días.",
                "tagline": "Típico: 8 — 16 sem. · KPI · conversion + LTV",
                "body":
                    "Para productos ya en producción que deben crecer. "
                    "Trabajamos sobre onboarding, pricing, retención, referral. "
                    "Quick wins en los primeros 30 días (normalmente +12% en un funnel). "
                    "Sistemas a 90 días (nuevos experimentos continuos).",
                "scope_label": "// scope",
                "scope": [
                    "Audit funnel + benchmark",
                    "Experiment backlog",
                    "A/B test weekly cadence",
                    "Onboarding redesign",
                    "Pricing page A/B",
                    "Email activation series",
                    "Referral loop",
                    "Reporting dashboard",
                ],
                "stack": ["PostHog", "Segment", "Mixpanel", "Customer.io", "GrowthBook"],
            },
            {
                "id": "CAP.04 · B2B delivery",
                "title": "Portales <em>asset manager</em> y dashboards corporate.",
                "tagline": "Típico: 24 — 36 sem. · KPI · task completion + time saved",
                "body":
                    "Para empresas B2B (proptech, fintech, healthtech) que deben "
                    "entregar portales a sus clientes enterprise. SSO, roles, "
                    "permisos, data warehouse integrado, exports estructurados. "
                    "No es sexy, pero es donde se juega la renovación anual.",
                "scope_label": "// scope",
                "scope": [
                    "Discovery con 3-5 enterprise",
                    "Design tokens corporate",
                    "SSO (SAML · Okta · Azure)",
                    "Roles + permisos granulares",
                    "Data warehouse integration",
                    "Export multi-formato",
                    "Audit log compliance",
                    "SLA 99.9% + monitoring",
                ],
                "stack": ["Next.js", "BigQuery", "Okta", "Datadog", "Sentry"],
            },
        ],

        "engagement_label":   "Tres modos de engagement",
        "engagement_heading": "Del <em>proyecto puntual</em> al <em>partner continuo</em>.",
        "engagement_intro":
            "Elegimos el modelo de engagement juntos, en sprint cero. "
            "Normalmente el 70% de los proyectos arrancan como fijo, el 30% como "
            "partnership continua. El tiempo y materiales es raro, lo "
            "usamos solo para discovery de menos de 3 semanas.",
        "engagement_tiles": [
            {
                "id":    "E.01 · Discovery",
                "title": "<em>Discovery sprint</em>",
                "range": "2 — 3 semanas · fijo",
                "body":  "Sprint cero dedicado. Research, audit, backlog, "
                         "estimación. Si luego se procede, se escala.",
                "includes": [
                    "User research (5-8 entrevistas)",
                    "Audit cuantitativo (analytics)",
                    "Backlog inicial",
                    "Estimación de delivery",
                    "Documento compartido 30 páginas",
                ],
            },
            {
                "id":    "E.02 · Fixed delivery",
                "title": "<em>Fixed delivery</em>",
                "range": "8 — 30 semanas · fijo",
                "body":  "Lanzamiento o redesign con scope y presupuesto fijos. "
                         "El más común para scale-ups en Serie A.",
                "includes": [
                    "Equipo dedicado 3-5 personas",
                    "Sprints de 2 semanas",
                    "Ship log compartido",
                    "Métrica declarada",
                    "Rollback + feature flags",
                    "Handover documentado",
                ],
                "featured": True,
            },
            {
                "id":    "E.03 · Partner mode",
                "title": "<em>Partner mode</em>",
                "range": "Q-by-Q · renovación trimestral",
                "body":  "Engagement continuo para plataformas maduras. "
                         "Banda de días/trimestre, roadmap compartida.",
                "includes": [
                    "Weekly ship cadence",
                    "Backlog compartido con el cliente",
                    "Experimento continuo",
                    "Review trimestral de KPI",
                    "SLA soporte + on-call",
                ],
            },
        ],

        "cta_label":   "Próximo paso",
        "cta_heading": "Vámonos a <em>discovery</em>, 30 minutos.",
        "cta_primary": "Reserva una call",
    },

    # ── LAVORI (project_list) ────────────────────────────────────
    "lavori": {
        "chip": "Archivo de productos · 2019 — 2026",
        "headline": "<em>Cuarenta y siete</em> productos enviados. <em>Siete</em> en vitrina.",
        "standfirst":
            "Cada caso tiene una métrica declarada y medida. "
            "Mostramos siete proyectos públicos — los otros cuarenta están "
            "bajo NDA (común en fintech y B2B). Archivo completo a petición.",
        "tabs": ["Todos", "Product launch", "Redesign", "Growth", "B2B delivery"],
        "tabs_count_label": "// total archivo",
        "tabs_count_value": "047",

        "projects": [
            {
                "slug": "casavo-retention-rework",
                "id":   "P.01",
                "cover":"https://images.unsplash.com/photo-1551434678-e076c223a692?w=1200&q=80&auto=format&fit=crop",
                "title":"Retention rework · plataforma de compra de vivienda",
                "client":"Casavo",
                "discipline":"PROPTECH · REDESIGN",
                "year": "2025",
                "blurb":
                    "Repensamos el funnel entero desde la búsqueda hasta la firma. "
                    "Migración progresiva vía feature flag sobre 180k usuarios. "
                    "Cero downtime, +18% de retención a 30 días.",
                "kpi": [
                    ("<em>+18%</em>",  "retención D30"),
                    ("<em>Δ+22</em>",  "NPS"),
                    ("<em>180K</em>",  "usuarios migrados"),
                ],
            },
            {
                "slug": "fastweb-plus-dashboard",
                "id":   "P.02",
                "cover":"https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80&auto=format&fit=crop",
                "title":"Dashboard residencial v2.3",
                "client":"Fastweb",
                "discipline":"TELCO · PLATFORM",
                "year": "2024",
                "blurb":
                    "Un nuevo cuadro de mando para 2,8M de clientes residenciales. "
                    "SSO integrado, gestión de servicios, self-care completo. "
                    "Reducción de llamadas al call center −34% en seis meses.",
                "kpi": [
                    ("<em>−34%</em>",   "llamadas CC"),
                    ("<em>2,8M</em>",   "usuarios"),
                    ("<em>NPS 64</em>", "post-launch"),
                ],
            },
            {
                "slug": "soldo-corporate-onboarding",
                "id":   "P.03",
                "cover":"https://images.unsplash.com/photo-1559028012-481c04fa702d?w=1200&q=80&auto=format&fit=crop",
                "title":"Onboarding corporate self-serve",
                "client":"Soldo",
                "discipline":"FINTECH · LAUNCH",
                "year": "2025",
                "blurb":
                    "De onboarding asistido (4 días medianos) a self-serve "
                    "(42 minutos). Compliance pan-EU, KYC integrado, "
                    "multi-currency desde el día cero.",
                "kpi": [
                    ("<em>−54%</em>",      "TTFV"),
                    ("<em>+41%</em>",      "activation"),
                    ("<em>7 mercados</em>", "day one"),
                ],
            },
            {
                "slug": "milkman-ship-sdk",
                "id":   "P.04",
                "cover":"https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=1200&q=80&auto=format&fit=crop",
                "title":"SDK de ship tracking para retailers",
                "client":"Milkman",
                "discipline":"LOGISTICS · B2B",
                "year": "2024",
                "blurb":
                    "Un SDK JavaScript para tracking de entregas integrado en el "
                    "checkout de más de 40 retailers. Una sola llamada API, "
                    "branding retailer-side, actualizaciones en tiempo real.",
                "kpi": [
                    ("<em>40+</em>",    "retailers"),
                    ("<em>1 llam.</em>","API"),
                    ("<em>2MB</em>",    "bundle"),
                ],
            },
            {
                "slug": "lendlease-asset-portal",
                "id":   "P.05",
                "cover":"https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200&q=80&auto=format&fit=crop",
                "title":"Portal asset manager enterprise",
                "client":"Lendlease",
                "discipline":"PROPTECH · B2B",
                "year": "2024",
                "blurb":
                    "Un portal para 80 asset managers italianos. SSO Azure, "
                    "roles granulares, data warehouse integrado con "
                    "export multi-formato. Compliance MiFID II incluida.",
                "kpi": [
                    ("<em>80</em>",      "asset mgr"),
                    ("<em>Azure SSO</em>","deploy"),
                    ("<em>MiFID II</em>","compliance"),
                ],
            },
            {
                "slug": "fiscozen-onboarding-self-serve",
                "id":   "P.06",
                "cover":"https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=1200&q=80&auto=format&fit=crop",
                "title":"Onboarding self-serve autónomos",
                "client":"Fiscozen",
                "discipline":"FISCTECH · GROWTH",
                "year": "2024",
                "blurb":
                    "De onboarding asistido por asesor fiscal a self-serve "
                    "completo. Reducción de tiempos de activación y +47% de "
                    "conversión de trial a paid en los primeros 90 días.",
                "kpi": [
                    ("<em>+47%</em>",   "trial → paid"),
                    ("<em>18 min</em>", "TTFV"),
                    ("<em>90 d</em>",   "medición"),
                ],
            },
        ],

        "velocity_label":   "Velocity media",
        "velocity_heading": "Cómo <em>enviamos</em> · últimos doce meses.",
        "velocity_body":
            "Los números de abajo son los que miramos internamente. "
            "Actualizados mensualmente. Si te interesa la metodología que hay detrás, "
            "hablémoslo en call de discovery.",
        "velocity_stats": [
            ("<em>8</em>",      "productos enviados · 2025"),
            ("<em>94%</em>",    "proyectos on-time"),
            ("<em>+26%</em>",   "KPI mediano movido"),
            ("<em>47 d</em>",   "median time-to-ship"),
        ],
    },

    # ── SPRINT (process) ─────────────────────────────────────────
    "sprint": {
        "chip": "Metodología · 4 fases · telemetría live",
        "headline": "Cuatro <em>sprints</em>, del discovery a la escala.",
        "standfirst":
            "Cada proyecto atraviesa cuatro fases declaradas. "
            "Duraciones previsibles, entregas claras, métricas públicas. "
            "El cliente ve en tiempo real dónde estamos — y por qué.",

        "sprints": [
            {
                "id": "Sprint 0 · Signal",
                "duration": "1 semana · fija",
                "title": "<em>Entender</em> el problema, antes de diseñarlo.",
                "tagline": "// output: brief compartido + backlog inicial",
                "body":
                    "El sprint cero es la fase más importante y la más infravalorada. "
                    "En cinco días escuchamos a los stakeholders (CEO, producto, "
                    "customer success), entrevistamos a 5-8 usuarios reales, leemos "
                    "el dashboard actual. Al final presentamos un brief de "
                    "lectura + backlog de hipótesis a testear.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Brief compartido · 24 páginas",
                    "Backlog inicial · Linear",
                    "Stakeholder map",
                    "Research summary · 5-8 entrevistas",
                    "Métrica declarada + baseline",
                    "Estimación de delivery (sprint count)",
                ],
            },
            {
                "id": "Sprint 1 — 2 · Sketch",
                "duration": "4 semanas",
                "title": "<em>Prototipar</em> antes de construir.",
                "tagline": "// output: prototipo testeable + design system v0.1",
                "body":
                    "Los primeros dos sprints son de prototipado rápido. "
                    "Construimos en Figma + Framer los tres flows más críticos, "
                    "los testeamos con usuarios reales, iteramos. En paralelo "
                    "arrancamos el design system (tokens + 20 componentes base). "
                    "El código de verdad llega en el sprint 3.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Prototipo Figma interactivo",
                    "3 rondas de user testing",
                    "Design system v0.1",
                    "Arquitectura de código",
                    "Plan de A/B test",
                    "Design review con el cliente",
                ],
            },
            {
                "id": "Sprint 3 — 5 · Ship",
                "duration": "6 semanas",
                "title": "<em>Llevar a producción</em>, incremental.",
                "tagline": "// output: production live + primera métrica",
                "body":
                    "Implementación y delivery incremental. Cada viernes ship-eamos "
                    "algo a staging, cada fin de sprint a producción. "
                    "Feature flags + rollback a 1 clic. Al final del sprint 5 "
                    "la primera métrica declarada ya debe haberse movido.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Staging deploy semanal",
                    "Production deploy quincenal",
                    "Feature flags todos activos",
                    "Rollback plan documentado",
                    "Monitoring · Datadog / Sentry",
                    "Primera métrica movida",
                ],
            },
            {
                "id": "Sprint 6+ · Scale",
                "duration": "ongoing · trimestral",
                "title": "<em>Escalar</em> · experimentos continuos.",
                "tagline": "// output: ship log semanal + review KPI trimestral",
                "body":
                    "Post-launch entramos en modo scale. Experimentos "
                    "semanales, feature expansion, optimización post-launch. "
                    "Ship log compartido público. Review trimestral de las "
                    "métricas frente al plan.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Ship log público",
                    "A/B weekly",
                    "Feature roadmap 6 meses",
                    "Review KPI trimestral",
                    "Training equipo interno",
                    "Handover continuo",
                ],
            },
        ],

        "mindset_label":   "Cómo <em>pensamos</em> el proceso",
        "mindset_heading": "Tres <em>principios</em> de delivery.",
        "mindset_cards": [
            {
                "id": "P.01",
                "title": "<em>Telemetría</em> visible",
                "body": "El ship log es público para el cliente desde el día cero. "
                        "Qué hemos enviado, cuándo, por qué. Cero habitaciones oscuras.",
            },
            {
                "id": "P.02",
                "title": "<em>Rollback</em> a 1 clic",
                "body": "Cada feature está tras un flag. Si algo no funciona "
                        "en producción, lo desactivamos en menos de 60 segundos.",
            },
            {
                "id": "P.03",
                "title": "<em>Skin in the game</em>",
                "body": "Si la métrica declarada no se mueve, seguimos "
                        "trabajando gratis. Lo hemos hecho cuatro veces en ocho años.",
            },
        ],

        "stack_label":   "Stack de delivery",
        "stack_heading": "Con qué <em>entregamos</em>.",
        "stack_intro":
            "El stack se elige para ser fiable, rápido, y fácil "
            "de traspasar al equipo interno del cliente. Cero tecnologías boutique.",
        "stack_tiles": [
            {"category": "// frontend",  "list": "<strong>Next.js 14</strong> · <span>TypeScript</span> · <strong>React</strong> · <span>Framer Motion</span>"},
            {"category": "// backend",   "list": "<strong>Node</strong> · <span>Django</span> · <strong>Supabase</strong> · <span>PostgreSQL</span>"},
            {"category": "// design",    "list": "<strong>Figma</strong> · <span>Framer</span> · <strong>Design tokens</strong> · <span>Maze</span>"},
            {"category": "// analytics", "list": "<strong>PostHog</strong> · <span>Segment</span> · <strong>Mixpanel</strong> · <span>GrowthBook</span>"},
            {"category": "// payments",  "list": "<strong>Stripe</strong> · <span>Checkout</span> · <strong>Elements</strong> · <span>Billing</span>"},
            {"category": "// infra",     "list": "<strong>Vercel</strong> · <span>Supabase</span> · <strong>Datadog</strong> · <span>Sentry</span>"},
            {"category": "// auth",      "list": "<strong>Auth0</strong> · <span>Okta SSO</span> · <strong>Azure AD</strong> · <span>Clerk</span>"},
            {"category": "// workflow",  "list": "<strong>Linear</strong> · <span>Notion</span> · <strong>Slack</strong> · <span>Loom</span>"},
        ],
    },

    # ── BRIEF (contact) ──────────────────────────────────────────
    "brief": {
        "chip": "3 slots abiertos · Q3 2026",
        "headline": "Cuéntanos el <em>proyecto</em>. Te llamamos en menos de 48h.",
        "standfirst":
            "Esto no es un form. Es un brief estructurado en 3 pasos. "
            "Cada respuesta que recibes la escribe personalmente Luca o "
            "Sofia, no un account manager. Si el proyecto es para nosotros, "
            "el segundo mensaje ya es una propuesta de call.",

        "form_heading": "// brief intake · 3 pasos",

        "step1": {
            "id": "PASO 01", "title": "Quién eres", "sub": "Solo los campos estrictamente necesarios.",
        },
        "step2": {
            "id": "PASO 02", "title": "El proyecto", "sub": "Cuanto más concreto, más útil la respuesta.",
        },
        "step3": {
            "id": "PASO 03", "title": "Cuándo", "sub": "Elige un slot indicativo — lo confirmamos luego por email.",
        },

        "labels": {
            "name":    "Nombre y apellidos",
            "role":    "Cargo",
            "company": "Empresa / producto",
            "email":   "Email de trabajo",
            "scope":   "Tipo de proyecto",
            "brief":   "Relato breve",
            "slot":    "Slot preferido",
        },
        "placeholders": {
            "name":    "Nombre Apellidos",
            "role":    "p. ej. Head of Product",
            "company": "Nombre de la empresa",
            "email":   "name@company.com",
            "brief":   "Qué estás construyendo, en qué punto estás (MRR, usuarios, ronda), cuál es el problema que estás sintiendo, cómo mides el éxito. Un brief concreto recibe una respuesta concreta.",
        },
        "scope_options": [
            "Product launch · primera vez live",
            "Platform redesign · producto maduro",
            "Growth systems · funnel / retención",
            "B2B delivery · portal / dashboard",
            "Discovery sprint · 2-3 semanas",
            "Todavía no estoy seguro — hablémoslo",
        ],

        "slots": [
            ("mon10", "Lun · 10:00"),
            ("mon15", "Lun · 15:00"),
            ("tue10", "Mar · 10:00"),
            ("tue15", "Mar · 15:00"),
            ("wed10", "Mié · 10:00"),
            ("wed15", "Mié · 15:00"),
            ("thu10", "Jue · 10:00"),
            ("thu15", "Jue · 15:00"),
            ("async", "Solo async por email"),
        ],
        "form_submit_label": "Reserva la call",
        "form_submit_note":  "// respuesta en 48h laborables · todos los husos EU",

        "async_label":   "¿Prefieres async?",
        "async_heading": "Escribe a <em>Luca</em> y <em>Sofia</em>.",
        "async_body":
            "Cada email llega directamente a los dos cofundadores. "
            "Responden ellos — no un account manager, no un bot.",

        "studio_label":  "El estudio",

        "response_label": "// SLA de respuesta",
        "response_rows": [
            ("Brief", "< 48h"),
            ("Propuesta", "5 días"),
            ("Sprint cero", "2 semanas"),
            ("Primera métrica", "6 semanas"),
        ],

        "boot_left":  "aura.studio · hello@aura.studio · +39 02 8728 4411",
        "boot_right": "// siempre abiertos al brief",
    },

    # ── POSTS (project_detail) ───────────────────────────────────
    "posts": [
        {
            "slug": "casavo-retention-rework",
            "id":   "P.01 · PROPTECH",
            "title": "Casavo · <em>+18% retención</em> en tres meses.",
            "client": "Casavo · Proptech Milán",
            "discipline": "Redesign · retención",
            "duration": "14 semanas",
            "year": "2025",
            "standfirst":
                "El rework del funnel post-reserva de Casavo. "
                "Una optimización incremental sobre 180k usuarios, "
                "feature flags por todas partes, cero downtime. Tres meses después: "
                "+18% de retención a 30 días, NPS +22, MRR +840 K€.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1551434678-e076c223a692?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Los usuarios volvían, pero no convertían.",
            "problem_paragraphs": [
                "Casavo había duplicado los usuarios activos entre 2023 y 2024, "
                "pero la conversión de <em>visita 1</em> a <em>reserva de visita real</em> "
                "había bajado un 12% — sobre 180k usuarios activos, eso significaba ~21k "
                "reservas perdidas cada mes.",
                "El equipo interno había entendido que el problema estaba en el funnel "
                "post-registro, pero no tenía capacity para testear más de 10 hipótesis "
                "en serio sin ralentizar la roadmap principal.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Un segundo funnel, en paralelo al viejo.",
            "solution_paragraphs": [
                "En lugar de reescribir el funnel principal (riesgo demasiado alto sobre "
                "180k usuarios) construimos un <em>segundo funnel experimental</em> "
                "tras feature flag, disponible para el 10% del tráfico. Seis semanas "
                "de test, siete iteraciones, cuatro flows testeados.",
                "En la sexta iteración el segundo funnel le ganaba al primero un 18% "
                "en retención D30. Migramos progresivamente al resto de los "
                "180k usuarios en tres semanas — fase del 25%, luego 50%, luego 100%.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "Catorce semanas, <em>siete sprints</em>.",
            "timeline_intro":
                "El timeline de abajo es la cronología real de delivery — extraída "
                "del ship log compartido con Casavo.",
            "timeline_steps": [
                {"id": "S.00", "duration": "sem. 1",    "title": "<em>Signal</em>",   "body": "Research + audit funnel + backlog 14 hipótesis."},
                {"id": "S.01", "duration": "sem. 2-3",  "title": "<em>Sketch</em>",   "body": "Prototipos de 4 flows alternativos, 8 entrevistas."},
                {"id": "S.02", "duration": "sem. 4-6",  "title": "<em>Ship</em>",     "body": "Segundo funnel live al 10%, primer A/B test."},
                {"id": "S.03", "duration": "sem. 7-11", "title": "<em>Iterate</em>",  "body": "6 iteraciones weekly. Cohorte cada viernes."},
                {"id": "S.04", "duration": "sem. 12-14","title": "<em>Migrate</em>",  "body": "Rollout al 25% → 50% → 100%. Cero downtime."},
            ],

            "results_label": "// results",
            "results_heading": "Cuatro <em>métricas movidas</em>.",
            "results_stats": [
                ("<em>+18%</em>",    "retención D30",            "de 42% a 49,6% (90 d rolling)"),
                ("<em>Δ +22</em>",   "NPS",                      "de 31 a 53 en los 3 meses post-rollout"),
                ("<em>+840 K€</em>", "MRR incremental",          "proyección a 12 meses"),
                ("<em>0</em>",       "downtime durante rollout", "180k usuarios, cero errores 5xx extra"),
            ],

            "quote": "En tres meses entendieron nuestro producto mejor que consultoras que habían trabajado con nosotros un año. Y shippearon.",
            "quote_author": "Marianna Colombo",
            "quote_role":   "VP Product · Casavo",

            "next_label":   "// next case",
            "next_heading": "→ ver todos los <em>trabajos</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ reserva una <em>call</em>",
        },
        {
            "slug": "fastweb-plus-dashboard",
            "id":   "P.02 · TELCO",
            "title": "Fastweb · <em>−34% llamadas CC</em> en 6 meses.",
            "client": "Fastweb · Telco Italia",
            "discipline": "Platform redesign",
            "duration": "26 semanas",
            "year": "2024",
            "standfirst":
                "Un nuevo cuadro de mando residencial para 2,8M de clientes. "
                "Gestión de servicios, pagos, auto-care, SSO. "
                "Resultado: −34% llamadas al call center, NPS 64 post-launch, "
                "migración completa en seis meses sin downtime.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Un cuadro de mando de 2014 en un mundo de 2024.",
            "problem_paragraphs": [
                "El dashboard residencial de Fastweb estaba construido en 2014 "
                "y re-skin-eado tres veces sin tocar la estructura. El resultado: "
                "task completion al 41%, 2,1M de llamadas al call center al año por "
                "operaciones que deberían haber sido self-care.",
                "El objetivo: reconstruir sin perder usuarios, sin downtime, "
                "y sin un big-bang launch — tuvimos 26 semanas.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Micro-frontend + migración progresiva.",
            "solution_paragraphs": [
                "Construimos el nuevo dashboard como <em>micro-frontend</em> "
                "al lado del viejo — mismo dominio, mismo SSO, mismo backend. "
                "Los usuarios fueron migrados por cluster geográfico (Lombardía, "
                "Piamonte, Lacio...) en seis fases.",
                "Cada cluster se monitorizaba durante 2 semanas. Si el NPS y el task "
                "completion eran mejores que el viejo, se procedía al siguiente cluster. "
                "Si eran peores, se volvía atrás 24 horas y se arreglaba.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "<em>Seis fases</em> de rollout geográfico.",
            "timeline_intro":
                "Cada fase del rollout tenía 2 semanas de monitorización antes "
                "de la fase siguiente. La más difícil fue la tercera.",
            "timeline_steps": [
                {"id": "R.01", "duration": "Semana 10", "title": "Piamonte",     "body": "400k usuarios. NPS +18. Go."},
                {"id": "R.02", "duration": "Semana 14", "title": "Lombardía",    "body": "680k usuarios. NPS +22. Go."},
                {"id": "R.03", "duration": "Semana 18", "title": "Véneto",       "body": "480k usuarios. NPS +9. Hold 1 sem."},
                {"id": "R.04", "duration": "Semana 22", "title": "Lacio",        "body": "520k usuarios. NPS +21. Go."},
                {"id": "R.05", "duration": "Semana 26", "title": "Resto Italia", "body": "720k usuarios. NPS +19. Complete."},
            ],

            "results_label": "// results",
            "results_heading": "Seis meses, <em>cuatro números</em>.",
            "results_stats": [
                ("<em>−34%</em>",     "llamadas call center", "~720k llamadas menos / año"),
                ("<em>NPS 64</em>",   "post-launch",           "vs 32 pre-launch"),
                ("<em>2,8M</em>",     "usuarios migrados",     "100% sin downtime"),
                ("<em>+41% TC</em>",  "task completion",       "de 41% a 82%"),
            ],

            "quote": "Aura es el único estudio que me presentó un plan de rollback para cada sprint. Usamos el rollback dos veces. Cero drama.",
            "quote_author": "Stefano Petri",
            "quote_role":   "Head of digital · Fastweb",

            "next_label":   "// next case",
            "next_heading": "→ ver todos los <em>trabajos</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ reserva una <em>call</em>",
        },
        {
            "slug": "soldo-corporate-onboarding",
            "id":   "P.03 · FINTECH",
            "title": "Soldo · onboarding de <em>4 días</em> a <em>42 minutos</em>.",
            "client": "Soldo · Fintech pan-EU",
            "discipline": "Product launch · onboarding",
            "duration": "18 semanas",
            "year": "2025",
            "standfirst":
                "El rediseño completo del onboarding corporate de Soldo. "
                "De proceso asistido (4 días) a self-serve completo "
                "(42 minutos) en 7 mercados europeos, con KYC, multi-currency "
                "y compliance. Resultado: +41% activation, −54% time to value.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1559028012-481c04fa702d?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Un onboarding que requería un humano.",
            "problem_paragraphs": [
                "El onboarding Soldo en 2024 requería 4 días medianos "
                "(2 para KYC, 1 para setup multi-currency, 1 para activación "
                "de tarjetas). Cada onboarding consumía 1,2 horas de customer success. "
                "Sobre 2.800 onboardings/mes, el coste era insostenible.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Onboarding guiado, cero humano.",
            "solution_paragraphs": [
                "Rediseñamos el flujo entero como <em>self-serve guided</em>: "
                "el cliente sube los documentos una sola vez, el KYC gira en background, "
                "la configuración multi-currency viene pre-rellenada según el mercado de residencia.",
                "Humano solo bajo petición explícita (link en cada paso). "
                "El CSAT no cayó — subió un 22%.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "Nueve <em>sprints</em>, siete mercados.",
            "timeline_intro":
                "Los primeros 4 sprints en UK (mercado más maduro). "
                "Los otros 5 en rollout cross-market.",
            "timeline_steps": [
                {"id": "S.01", "duration": "sem. 1-2",   "title": "<em>Discovery</em>",    "body": "120 customer success calls analizadas."},
                {"id": "S.02", "duration": "sem. 3-6",   "title": "<em>UK beta</em>",      "body": "Nuevo flow live en UK. +28% activation."},
                {"id": "S.03", "duration": "sem. 7-10",  "title": "<em>DE · NL · FR</em>", "body": "3 mercados añadidos. Fix multi-currency."},
                {"id": "S.04", "duration": "sem. 11-14", "title": "<em>IT · ES · IE</em>", "body": "3 mercados añadidos. Fix de idioma."},
                {"id": "S.05", "duration": "sem. 15-18", "title": "<em>Scale</em>",        "body": "Optimización continua. A/B weekly."},
            ],

            "results_label": "// results",
            "results_heading": "Tres <em>métricas core</em> movidas.",
            "results_stats": [
                ("<em>42 min</em>",    "time to activate",    "de 4 días medianos"),
                ("<em>+41%</em>",      "activation rate",      "trial → paid"),
                ("<em>+22%</em>",      "CSAT",                 "post-onboarding"),
                ("<em>7</em>",         "mercados",             "day one go-live"),
            ],

            "quote": "El resultado es que hoy nuestro equipo de onboarding corporate es un 60% más pequeño pero gestiona 3x las empresas. Soldo no estaría al nivel actual sin este rework.",
            "quote_author": "Rebecca Hughes",
            "quote_role":   "VP Growth · Soldo",

            "next_label":   "// next case",
            "next_heading": "→ ver todos los <em>trabajos</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ reserva una <em>call</em>",
        },
        {
            "slug": "milkman-ship-sdk",
            "id":   "P.04 · LOGISTICS",
            "title": "Milkman · <em>SDK tracking</em> para más de 40 retailers.",
            "client": "Milkman · Logistics Italia",
            "discipline": "B2B delivery · SDK",
            "duration": "22 semanas",
            "year": "2024",
            "standfirst":
                "Un SDK JavaScript white-label para tracking de entregas, "
                "integrado en el checkout de más de 40 retailers italianos. "
                "Una sola llamada API, branding retailer-side, "
                "actualizaciones en tiempo real. Bundle por debajo de 2MB gzipped.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "40 retailers, 40 integraciones custom.",
            "problem_paragraphs": [
                "Milkman gestionaba las entregas de más de 40 retailers italianos — "
                "Esselunga, Coop, Unieuro, Mediaworld — cada uno con su propia "
                "integración custom. Cada nuevo retailer requería 8-12 "
                "semanas de engineering.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Un SDK, una llamada API.",
            "solution_paragraphs": [
                "Construimos un SDK JavaScript white-label. "
                "Un retailer debe hacer una sola cosa: llamar a <em>milkman.track(orderId)</em>. "
                "El SDK gestiona el branding retailer-side (colores, tipografías, logo), "
                "los idiomas, las actualizaciones en tiempo real vía WebSocket.",
                "Integración media: 3 horas. Antes: 8-12 semanas.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "<em>Cinco</em> sprints del SDK al 40º retailer.",
            "timeline_intro": "Primer retailer (Esselunga) en sprint 3. Los otros 39 en autoservicio.",
            "timeline_steps": [
                {"id": "S.01", "duration": "sem. 1-4",   "title": "<em>SDK core</em>",        "body": "Arquitectura, bundle, branding."},
                {"id": "S.02", "duration": "sem. 5-10",  "title": "<em>Esselunga beta</em>",  "body": "Primer retailer live. 2 bugs críticos."},
                {"id": "S.03", "duration": "sem. 11-14", "title": "<em>Unieuro · Coop</em>",  "body": "2 retailers añadidos. Cero bugs."},
                {"id": "S.04", "duration": "sem. 15-18", "title": "<em>Docs + portal</em>",   "body": "Self-serve onboarding."},
                {"id": "S.05", "duration": "sem. 19-22", "title": "<em>Scale</em>",           "body": "40º retailer integrado en autoservicio."},
            ],

            "results_label": "// results",
            "results_heading": "De <em>8 semanas</em> a <em>3 horas</em>.",
            "results_stats": [
                ("<em>40+</em>",    "retailers live",     "Al go-live del sexto mes"),
                ("<em>3 horas</em>","time-to-integrate",  "De 8-12 semanas medianas"),
                ("<em>1,8 MB</em>", "bundle gzipped",     "Bajo el techo de 2 MB requerido"),
                ("<em>0</em>",      "downtime",           "Del primer sprint a hoy"),
            ],

            "quote": "El SDK nos permitió abrir tres mercados europeos en seis meses. Antes habría sido imposible.",
            "quote_author": "Antonio Perini",
            "quote_role":   "CEO · Milkman",

            "next_label":   "// next case",
            "next_heading": "→ ver todos los <em>trabajos</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ reserva una <em>call</em>",
        },
        {
            "slug": "lendlease-asset-portal",
            "id":   "P.05 · PROPTECH",
            "title": "Lendlease · <em>portal enterprise</em> para 80 asset managers.",
            "client": "Lendlease · Proptech EU",
            "discipline": "B2B delivery",
            "duration": "30 semanas",
            "year": "2024",
            "standfirst":
                "Un portal enterprise para 80 asset managers italianos. "
                "SSO Azure, roles granulares, data warehouse integrado, "
                "compliance MiFID II. No es sexy — es donde se juega la renovación.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1600&q=80&auto=format&fit=crop",

            "problem_label":"// problem",
            "problem_heading":"Un portal enterprise con cero self-serve.",
            "problem_paragraphs":[
                "80 asset managers usaban un portal de 2016 que requería "
                "asistencia humana para cada acción. Cada asset manager consumía "
                "~6 horas / semana de customer success. Re-contracting trimestral "
                "en riesgo.",
            ],
            "solution_label":"// solution",
            "solution_heading":"Dashboard self-serve + export automatizado.",
            "solution_paragraphs":[
                "Reconstruimos el portal como plataforma self-serve. "
                "SSO Azure, roles granulares (analista, manager, compliance), "
                "data warehouse integrado con export multi-formato "
                "(PDF, XLSX, CSV, MiFID II XML).",
            ],
            "timeline_label":"// timeline",
            "timeline_heading":"<em>Diez</em> sprints, <em>tres</em> rollouts por cluster.",
            "timeline_intro": "Rollout por cluster de asset managers (20/30/30).",
            "timeline_steps":[
                {"id":"S.01","duration":"sem. 1-4","title":"<em>Discovery</em>","body":"Entrevistas a 12 asset managers."},
                {"id":"S.02","duration":"sem. 5-14","title":"<em>SSO + roles</em>","body":"Azure SSO + RBAC completo."},
                {"id":"S.03","duration":"sem. 15-22","title":"<em>Dashboard</em>","body":"Core dashboard + analytics."},
                {"id":"S.04","duration":"sem. 23-28","title":"<em>Export</em>","body":"Multi-formato + MiFID II."},
                {"id":"S.05","duration":"sem. 29-30","title":"<em>Rollout</em>","body":"80 asset managers migrados."},
            ],
            "results_label":"// results",
            "results_heading":"<em>80</em> asset managers, <em>cero</em> llamadas.",
            "results_stats":[
                ("<em>80</em>","asset managers migrados","100% antes del fin del rollout"),
                ("<em>−92%</em>","llamadas CS","6 horas → 28 min /sem."),
                ("<em>100%</em>","recontracting","Por 2 años consecutivos"),
                ("<em>MiFID II</em>","compliance","Audit superado en la primera vuelta"),
            ],
            "quote":"El portal se ha convertido en la razón principal por la que nuestros asset managers renuevan.",
            "quote_author":"Valentina Greco",
            "quote_role":"Head of product · Lendlease IT",
            "next_label":"// next case",
            "next_heading":"→ ver todos los <em>trabajos</em>",
            "cta_label":"// start a project",
            "cta_heading":"→ reserva una <em>call</em>",
        },
        {
            "slug": "fiscozen-onboarding-self-serve",
            "id":   "P.06 · FISCTECH",
            "title": "Fiscozen · <em>+47%</em> de trial a paid.",
            "client": "Fiscozen · Fisctech Milán",
            "discipline": "Growth systems",
            "duration": "16 semanas",
            "year": "2024",
            "standfirst":
                "De onboarding asistido por asesor fiscal a self-serve completo "
                "para autónomos. +47% conversión trial → paid en 90 días.",
            "meta_client_label":"// client",
            "meta_discipline_label":"// capability",
            "meta_duration_label":"// duration",
            "meta_year_label":"// delivered",
            "cover_image": "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=1600&q=80&auto=format&fit=crop",
            "problem_label":"// problem",
            "problem_heading":"Onboarding que requería un asesor fiscal.",
            "problem_paragraphs":["Cada autónomo en prueba necesitaba 30 min con un asesor para arrancar. Bottleneck crítico."],
            "solution_label":"// solution",
            "solution_heading":"Guided onboarding self-serve, asesor opcional.",
            "solution_paragraphs":["Formulario guiado que pre-rellena ATECO a partir del relato libre del usuario, integrado con InfoCamere."],
            "timeline_label":"// timeline",
            "timeline_heading":"<em>Ocho</em> sprints, KPI semanal.",
            "timeline_intro":"Prioridad: time-to-first-value por debajo de los 20 minutos.",
            "timeline_steps":[
                {"id":"S.01","duration":"sem. 1-3","title":"<em>Research</em>","body":"20 entrevistas a autónomos primerizos."},
                {"id":"S.02","duration":"sem. 4-8","title":"<em>Flow v1</em>","body":"Primer onboarding self-serve. 28% activación."},
                {"id":"S.03","duration":"sem. 9-12","title":"<em>Iterate</em>","body":"4 A/B tests. 41% activación."},
                {"id":"S.04","duration":"sem. 13-16","title":"<em>Scale</em>","body":"Rollout 100%. 47% post-90d."},
            ],
            "results_label":"// results",
            "results_heading":"<em>Cuatro</em> meses, <em>tres</em> métricas.",
            "results_stats":[
                ("<em>+47%</em>","trial → paid","de 21% a 31% conv. a 90 d"),
                ("<em>18 min</em>","TTFV","de 4 horas con asesor fiscal"),
                ("<em>−38%</em>","CAC","customer acquisition cost"),
                ("<em>+2,1x</em>","volumen","trials semanales post-rollout"),
            ],
            "quote":"El equipo de Aura shippó más A/B tests en 16 semanas que los que habíamos hecho en los 2 años anteriores.",
            "quote_author":"Vittorio Amato",
            "quote_role":"CEO · Fiscozen",
            "next_label":"// next case",
            "next_heading":"→ ver todos los <em>trabajos</em>",
            "cta_label":"// start a project",
            "cta_heading":"→ reserva una <em>call</em>",
        },
    ],
}
