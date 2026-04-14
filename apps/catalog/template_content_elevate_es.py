"""Elevate — Startup SaaS Landing Kit · Spanish (peninsular) content tree.

Mirrors the shape of ``ELEVATE_CONTENT_IT`` exactly — same keys, nesting and
list shapes. Authored for the Elevate live i18n rollout of the
startup-saas-landing archetype. Voice: Xataka / Itnig / K Fund / Typeform
marketing register — `tú` direct address, SaaS anglicismes expected
(MRR, A/B, funnel, onboarding, deploy, ship, trial, PMF, growth).
"""
from __future__ import annotations

from typing import Any


ELEVATE_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Inicio",      "kind": "home"},
        {"slug": "prodotto",   "label": "Producto",    "kind": "product"},
        {"slug": "prezzi",     "label": "Precios",     "kind": "pricing"},
        {"slug": "demo",       "label": "Demo",        "kind": "demo"},
        {"slug": "contatti",   "label": "Contacto",    "kind": "contact"},
    ],

    # Site-wide chrome
    "site": {
        "logo_initial": "E",
        "logo_word":    "Elevate",
        "tag":          "Kit conversion-first · para founders que shippean",
        # Pill nav CTA label — short, action-oriented, distinct from `tag`
        "nav_cta":      "Empieza gratis",
        "phone":        "hello@elevatekit.io",
        "email":        "hello@elevatekit.io",
        "address":      "Talent Garden Calabiana · Milán",
        "hours_compact":"Async-first · Slack 9-19 CET",
        "hours_footer_rows": [
            "Demo on-demand · todos los martes a las 17:00 CET",
            "Office hours founder · viernes a las 11:00 CET",
        ],
        "license":      "",
        "footer_intro":
            "Elevate es el GTM kit que lleva tu startup de la "
            "waitlist al primer MRR en catorce días. Built for founders, "
            "by founders. Enviado desde Milán, desplegado en cualquier sitio.",
        "foot_studio":   "El producto",
        "foot_pages":    "Navega",
        "foot_contact":  "Habla con nosotros",
        "foot_offices":  "Ship log",
        # Footer tertiary column — last 3 ship-log entries
        "shiplog_footer_rows": [
            "v2.9 · viernes · drag-and-drop hero builder",
            "v2.8 · ayer · librería testimonial premium",
            "v2.7 · martes · A/B test integrado con GrowthBook",
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        # Top launch banner above the floating pill nav
        "banner_label":   "Serie A · Q2 2026",
        "banner_text":    "Estamos cerrando las primeras cincuenta plazas early-access",
        "banner_href":    "demo",

        "eyebrow":     "GTM kit conversion-first · para SaaS y startups early-stage",
        "headline":    "De la <em>waitlist</em> al primer <em>MRR</em> en catorce días.",
        "intro":
            "Elevate es el kit de landing, pricing y onboarding que convierte "
            "a los primeros visitantes en usuarios de pago. A/B test integrado, "
            "checkout Stripe one-click, copy kit en español, deploy en "
            "Vercel en treinta segundos.",
        "primary_cta":   "Empieza gratis · 14 días",
        "primary_href":  "demo",
        "secondary_cta": "Mira la demo · 2 min",
        "secondary_href":"prodotto",

        "trust_label":   "Adoptado por más de 240 startups europeas en early-stage",
        "trust_logos":   ["FLUX", "NOVA/", "QUANTA", "HELIX", "RIFT.", "CASP", "ARC", "LOOM"],

        # Product mockup card — overlaps the hero / sits below it
        "mockup": {
            "chrome_label":     "elevate.app / dashboard / onboarding-flow",
            "chrome_dots":      ["●", "●", "●"],
            "badge":            "Live A/B",
            "metric_primary":   "↑ 38%",
            "metric_label":     "Conversión CTA principal",
            "metric_desc":      "vs. variante B (control)",
            "secondary_metric": "+ 12,4 K €",
            "secondary_label":  "MRR · últimos 30 días",
            "secondary_desc":   "conversión trial-to-paid: 22%",
            "feature_label":    "Plan Launch · 29 € / mes",
            "perks":            ["Hosting + CDN incluidos", "CLI deploy · zero config", "Soporte Slack directo"],
        },

        # Feature pills under the hero
        "feature_pills":  ["Stripe + Linear", "A/B test integrado", "Edge analytics", "Copy kit ES", "Deploy en 30s"],

        # Capabilities — 6 cards in a 3x2 grid
        "features_label":   "Qué hay dentro",
        "features_heading": "Seis módulos, <em>una sola instalación</em>.",
        "features_intro":
            "Todas las piezas que necesitas para ir live y empezar a "
            "monetizar — ya integradas, ya testeadas, ya documentadas.",
        "features": [
            {
                "icon": "→",
                "title": "Hero builder drag-and-drop",
                "desc":
                    "Diez layouts hero pre-testeados sobre 1.200 startups. "
                    "A/B test entre variantes sin escribir una línea de código.",
            },
            {
                "icon": "$",
                "title": "Pricing table y Stripe",
                "desc":
                    "Tres tiers configurables, conversión checkout one-click, "
                    "subscription management out-of-the-box. Webhooks Stripe "
                    "ya cableados con Linear y Slack.",
            },
            {
                "icon": "▲",
                "title": "Edge analytics",
                "desc":
                    "Web vitals, funnel de conversión, attribution multi-touch — "
                    "recogidos edge-side, cero impacto sobre el TTI. Privacy-first, "
                    "cookieless, GDPR-clean.",
            },
            {
                "icon": "✱",
                "title": "Onboarding flow",
                "desc":
                    "Checklist guiada multi-step, progress bar, email "
                    "trigger sobre milestone. Time-to-value medio de 4 minutos "
                    "frente al benchmark del sector de 18.",
            },
            {
                "icon": "◐",
                "title": "Copy kit en español",
                "desc":
                    "Sesenta bloques de copy testeados en los mercados ES/EN/FR — "
                    "headline, sub, CTA, microcopy de onboarding, error states. "
                    "Listos para editar en markdown.",
            },
            {
                "icon": "↗",
                "title": "Deploy CLI",
                "desc":
                    "elevate deploy → Vercel / Netlify / Cloudflare en "
                    "treinta segundos. Branch preview automáticos, rollback "
                    "en un comando, environment variables sincronizadas.",
            },
        ],

        # Live product walkthrough invitation — replaces a fake video block.
        "product_demo_card": {
            "label":      "Ve Elevate en directo",
            "heading":    "Quince minutos con quien lo ha construido.",
            "intro":
                "En lugar de un vídeo grabado: reservamos un walkthrough breve "
                "sobre el proyecto real — editor drag-and-drop, wizard de pricing, "
                "cableado Stripe + Linear, deploy en Vercel. Preguntas reales, "
                "proyecto real, sin emails de follow-up.",
            "poster":     "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1800&q=80&auto=format&fit=crop",
            "primary_cta":    "Reserva el walkthrough",
            "primary_href":   "demo",
            "secondary_cta":  "Explora el producto",
            "secondary_href": "prodotto",
            "caption":        "Walkthrough 1-a-1 · calendario live",
        },

        # Metric strip on dark band
        "metric_label":   "Los números del kit en producción",
        "metric_heading": "El stack que shippea",
        "metric_strip": [
            ("3,1 ×",  "conversión landing media"),
            ("14 d",   "del deploy al primer usuario de pago"),
            ("99,98%", "uptime infraestructura"),
            ("4 min",  "time-to-value mediano"),
        ],

        # Integrations row
        "integrations_label":   "Integraciones out-of-the-box",
        "integrations_heading": "Ya cableado con el stack que usas",
        "integrations": [
            ("Stripe",     "Subscription · Checkout · Tax"),
            ("Linear",     "Issue tracking · changelog auto"),
            ("Slack",      "Notificaciones · alertas MRR"),
            ("Vercel",     "Deploy · preview · rollback"),
            ("PostHog",    "Funnel · session replay"),
            ("GrowthBook", "A/B test · feature flags"),
            ("Loops",      "Emails transaccionales"),
            ("Cal.com",    "Reserva de demos automática"),
        ],

        # Pricing teaser — cliccable hacia /prezzi
        "pricing_teaser_label":   "Precios transparentes",
        "pricing_teaser_heading": "Tres planes, sin setup fee.",
        "pricing_teaser_intro":
            "Cancelación en un clic, facturación mensual o anual, "
            "trial de catorce días sin tarjeta de crédito.",
        "pricing_teaser": [
            {"name": "Launch",  "price": "29 €",  "period": "/ mes", "tag": "Para founders en solitario",
             "highlight": False, "perks": ["Todos los módulos", "Hosting + CDN", "Email Slack"]},
            {"name": "Scale",   "price": "79 €",  "period": "/ mes", "tag": "Más elegido",
             "highlight": True, "perks": ["Todo Launch +", "A/B avanzado", "5 proyectos"]},
            {"name": "Studio",  "price": "199 €", "period": "/ mes", "tag": "Para estudios y agencias",
             "highlight": False, "perks": ["Todo Scale +", "Proyectos ilimitados", "White-label"]},
        ],
        "pricing_teaser_cta":      "Compara los planes en detalle",
        "pricing_teaser_cta_href": "prezzi",

        # Founder proof — 2 founder quotes
        "founders_label":   "Founders que han shippeado con Elevate",
        "founders_heading": "La palabra se la damos a quien <em>shippea de verdad</em>.",
        "founders": [
            {
                "name":  "Anna Vecchietti",
                "role":  "Founder · Quanta Analytics",
                "quote":
                    "Había probado tres boilerplates y dos constructores no-code. "
                    "Con Elevate me fui live en dos weekends, primer MRR "
                    "diecisiete días después del deploy. La diferencia es el "
                    "copy kit en español — no tener que reescribir cada headline.",
                "metric_primary": "+ 4,2 K €",
                "metric_label":   "MRR primeros 60 días",
            },
            {
                "name":  "Davide Zonca",
                "role":  "CTO · Helix Workflows",
                "quote":
                    "El stack que necesitaba sin los siete días de setup. "
                    "Stripe, GrowthBook, Linear ya cableados significa que "
                    "hemos dedicado el primer mes a hablar con usuarios, no "
                    "a configurar webhooks.",
                "metric_primary": "× 3,4",
                "metric_label":   "Conversión vs landing anterior",
            },
        ],

        # Ship log — what shipped recently (transparency block)
        "shiplog_label":   "Ship log live",
        "shiplog_heading": "Lo que hemos shippeado recientemente",
        "shiplog_intro":
            "Elevate está en continuous deploy. Cada feature enviada aparece "
            "aquí en tiempo real — nada de roadmaps teóricas, nada de temporadas "
            "del producto. Lo que ves es lo que usarás mañana.",
        "shiplog": [
            {"version": "v2.9", "date": "Viernes",        "title": "Hero builder drag-and-drop",
             "desc": "Diez layouts pre-testeados, A/B entre variantes integrado, preview live."},
            {"version": "v2.8", "date": "Ayer",           "title": "Librería testimonial premium",
             "desc": "Cuatro layouts (carousel, masonry, single-feature, video-first) con animaciones reveal."},
            {"version": "v2.7", "date": "Martes",         "title": "A/B test integrado con GrowthBook",
             "desc": "Wizard de setup de experimento en 4 pasos, hypothesis tracker, significancia estadística auto."},
            {"version": "v2.6", "date": "Lunes",          "title": "Stripe Checkout one-click",
             "desc": "Adaptadores para los 4 mayores payment providers de la UE, gestión de IVA automática."},
            {"version": "v2.5", "date": "Semana pasada", "title": "Edge analytics privacy-first",
             "desc": "Cookieless tracking, menos de 4KB sobre el TTI, dashboard funnel incluida."},
        ],
        "shiplog_cta":      "Suscríbete al ship log vía Slack",
        "shiplog_cta_href": "demo",
        "shiplog_release_label": "Próxima release",
        "shiplog_release_value": "v3.0 · primer lunes del mes",
        "shiplog_release_chip":  "RC live",

        # Final CTA band before footer — glow ring
        "cta_label":     "Empieza ahora",
        "cta_heading":   "Catorce días gratis. Cuarenta minutos para ir live.",
        "cta_intro":
            "Sin tarjeta de crédito para activar el trial. Slack directo "
            "con el founding team. Si no shippeas en dos semanas, "
            "te devolvemos el dinero. Promesa por escrito.",
        "cta_primary":   "Activa el trial",
        "cta_primary_href": "demo",
        "cta_secondary": "Ve el plan completo",
        "cta_secondary_href": "prezzi",
    },

    # ─── PRODOTTO (product tour) ────────────────────────────────
    "prodotto": {
        "eyebrow":   "Product tour · v2.9 (abril 2026)",
        "headline":  "Todo lo que <em>tienes que shippear</em> para ir live.",
        "intro":
            "Seis módulos core + doce integraciones out-of-the-box. "
            "Nada de plugins que configurar, nada de boilerplates que forkear, "
            "nada de hilos de Twitter que seguir para hacer lo que debería "
            "ser obvio. Abre, edita, deploy.",

        # Product modules — same 6 from home but expanded with detail
        "modules_label":   "Módulos core",
        "modules_heading": "Seis piezas, una sola instalación",
        "modules": [
            {
                "num":   "01",
                "title": "Hero builder drag-and-drop",
                "blurb":
                    "Diez layouts hero pre-testeados sobre 1.200 startups early-stage. "
                    "Cada layout viene con tres variantes de copy "
                    "(B2B, B2C, dev-tool) y con A/B test integrado.",
                "highlights": [
                    "10 layouts · 30 variantes de copy",
                    "A/B entre variantes sin código",
                    "Headline, sub, CTA y badge social todos editables",
                    "Mobile y desktop optimizados por separado",
                ],
            },
            {
                "num":   "02",
                "title": "Pricing table y Stripe Checkout",
                "blurb":
                    "Tres tiers configurables con highlight automático sobre "
                    "el plan central. Subscription management Stripe, "
                    "checkout one-click en mobile, gestión automática del IVA UE.",
                "highlights": [
                    "1, 2, 3 o 4 tiers · highlight a voluntad",
                    "Toggle mensual / anual built-in",
                    "Stripe Tax sobre 38 países UE",
                    "Webhooks Stripe → Slack ya cableados",
                ],
            },
            {
                "num":   "03",
                "title": "Edge analytics privacy-first",
                "blurb":
                    "Web vitals, funnel multi-step, attribution multi-touch — "
                    "todo recogido edge-side vía Cloudflare Worker. "
                    "Cookieless, GDPR-clean, menos de 4KB sobre el TTI.",
                "highlights": [
                    "Cookieless · GDPR · ePrivacy clean",
                    "Web Vitals · LCP · FID · CLS en dashboard",
                    "Funnel de conversión visual",
                    "PostHog connector opcional",
                ],
            },
            {
                "num":   "04",
                "title": "Onboarding flow guiado",
                "blurb":
                    "Checklist multi-step con progress bar, milestone "
                    "celebration, email trigger automáticos. Time-to-value "
                    "mediano de 4 minutos frente al benchmark del sector de 18.",
                "highlights": [
                    "Checklist drag-and-drop personalizable",
                    "Email trigger en Loops · Resend · Postmark",
                    "Achievement badge built-in",
                    "Re-engagement automático tras 48h",
                ],
            },
            {
                "num":   "05",
                "title": "Copy kit en español (y EN/FR)",
                "blurb":
                    "Sesenta bloques de copy editorial testeados en los "
                    "mercados ES/EN/FR. Headline, sub, CTA, microcopy "
                    "de onboarding, error states, empty states.",
                "highlights": [
                    "60 bloques · ES + EN + FR",
                    "Tone-of-voice configurable",
                    "Edición en markdown directa",
                    "Snippet library con búsqueda semántica",
                ],
            },
            {
                "num":   "06",
                "title": "Deploy CLI · treinta segundos",
                "blurb":
                    "elevate deploy. Treinta segundos hasta el primer deploy live, "
                    "branch preview automáticos en PR, rollback en un comando, "
                    "environment variables sincronizadas entre dev / staging / prod.",
                "highlights": [
                    "Vercel · Netlify · Cloudflare adapter",
                    "Branch preview automáticos en PR",
                    "Rollback instantáneo · zero downtime",
                    "Env-var sync · dev / staging / prod",
                ],
            },
        ],

        # Integrations grid — bigger version of home
        "integrations_label":   "Integraciones out-of-the-box",
        "integrations_heading": "El stack que necesitas, ya cableado.",
        "integrations_intro":
            "Doce integraciones nativas, cero plugins que instalar. "
            "Las que no ves aquí las añadimos si nos las pides por Slack.",
        "integrations_full": [
            {"name": "Stripe",     "category": "Pagos",         "desc": "Subscription · Checkout · Tax · Connect"},
            {"name": "Linear",     "category": "Tracking",      "desc": "Issue · Cycles · changelog auto-publicado"},
            {"name": "Slack",      "category": "Comms",         "desc": "Notificaciones · alertas MRR · daily digest"},
            {"name": "Vercel",     "category": "Deploy",        "desc": "Deploy de producción · preview branch · rollback"},
            {"name": "Netlify",    "category": "Deploy",        "desc": "Edge functions · build hooks · sync analytics"},
            {"name": "Cloudflare", "category": "Deploy",        "desc": "Workers · KV · D1 · R2 storage"},
            {"name": "PostHog",    "category": "Analytics",     "desc": "Funnel · session replay · feature flag"},
            {"name": "GrowthBook", "category": "Experimentos",  "desc": "A/B test · hypothesis tracker · stat-sig auto"},
            {"name": "Loops",      "category": "Email",         "desc": "Transaccionales · secuencias de onboarding"},
            {"name": "Resend",     "category": "Email",         "desc": "Transaccionales · plantillas React Email"},
            {"name": "Cal.com",    "category": "Booking",       "desc": "Reserva de demo · routing · webhook"},
            {"name": "Plain",      "category": "Soporte",       "desc": "Support inbox · CRM con triage IA"},
        ],

        # Architecture — what runs where
        "stack_label":   "Architecture",
        "stack_heading": "Qué corre dónde (y por qué)",
        "stack_intro":
            "Transparencia técnica — nada de magia, nada de lock-in oculto. "
            "El stack está documentado abiertamente, y todo el código es exportable "
            "con un clic si decides marcharte.",
        "stack": [
            ("Frontend",     "Next.js 15 · React 19 · App Router · Server Actions"),
            ("Edge",         "Cloudflare Workers + KV para analytics y A/B"),
            ("Base de datos","PostgreSQL · Prisma · Neon serverless"),
            ("Auth",         "Clerk · OAuth · passkey · magic link"),
            ("Pagos",        "Stripe Subscriptions + Stripe Tax + Stripe Connect"),
            ("Email",        "Loops o Resend a elegir · plantillas React Email"),
            ("Analytics",    "PostHog opcional · edge analytics nativo"),
            ("Experimentos", "GrowthBook · self-hosted o cloud"),
        ],

        "cta_heading":   "¿Listo para verlo en marcha?",
        "cta_intro":
            "Demo en directo con un founding member todos los martes a las 17:00 CET. "
            "Media hora de llamada, screen-share, preguntas técnicas bienvenidas.",
        "cta_primary":   "Reserva la demo",
        "cta_primary_href": "demo",
        "cta_secondary": "Ve los planes",
        "cta_secondary_href": "prezzi",
    },

    # ─── PREZZI (pricing) ───────────────────────────────────────
    "prezzi": {
        "eyebrow":  "Precios transparentes · 2026",
        "headline": "Cancelas en un clic. <em>Siempre</em>.",
        "intro":
            "Tres planes, sin setup fee, facturación mensual o anual "
            "(dos mensualidades de regalo en el anual). Catorce días "
            "de trial gratuito, sin tarjeta de crédito.",

        # Highlight badge label
        "highlight_badge": "Más elegido",
        "annual_prefix":   "o",

        # Toggle row UI cue
        "billing_toggle_label": "Facturación",
        "billing_toggle_options": [
            ("monthly", "Mensual"),
            ("annual",  "Anual · –17%"),
        ],

        # Three pricing tiers
        "tiers": [
            {
                "name":     "Launch",
                "tag":      "Para founders en solitario",
                "price":    "29 €",
                "annual":   "24 €",
                "period":   "/ mes",
                "annual_period": "/ mes · pagado anualmente",
                "highlight": False,
                "blurb":
                    "Todo lo necesario para ir live con un solo producto. "
                    "Pensado para el founder en solitario o para la primera semana de "
                    "founding team.",
                "cta":         "Empieza gratis",
                "cta_href":    "demo",
                "perks": [
                    ("✓", "Los seis módulos core"),
                    ("✓", "Hosting + CDN global incluidos"),
                    ("✓", "Deploy CLI · branch preview automáticos"),
                    ("✓", "Edge analytics + funnel base"),
                    ("✓", "1 proyecto · 1 dominio propio"),
                    ("✓", "Slack directo con el founding team"),
                    ("○", "A/B test base (manual)"),
                    ("○", "1 copy kit (ES o EN o FR)"),
                ],
            },
            {
                "name":     "Scale",
                "tag":      "Más elegido · para startups post-PMF",
                "price":    "79 €",
                "annual":   "65 €",
                "period":   "/ mes",
                "annual_period": "/ mes · pagado anualmente",
                "highlight": True,
                "blurb":
                    "El plan para el founding team que ha encontrado product/market "
                    "fit y está escalando. Añade A/B avanzado, multiproyecto y "
                    "white-glove onboarding.",
                "cta":         "Empieza gratis",
                "cta_href":    "demo",
                "perks": [
                    ("✓", "Todo Launch +"),
                    ("✓", "A/B test avanzado (GrowthBook integrado)"),
                    ("✓", "5 proyectos · dominios propios ilimitados"),
                    ("✓", "PostHog connector + session replay"),
                    ("✓", "Stripe Tax + Stripe Connect"),
                    ("✓", "Los 3 copy kits (ES + EN + FR)"),
                    ("✓", "Onboarding 1-1 con el founding team (60 min)"),
                    ("✓", "Canal Slack dedicado · SLA 4h"),
                ],
            },
            {
                "name":     "Studio",
                "tag":      "Para estudios, agencias y venture builders",
                "price":    "199 €",
                "annual":   "165 €",
                "period":   "/ mes",
                "annual_period": "/ mes · pagado anualmente",
                "highlight": False,
                "blurb":
                    "Para agencias, estudios creativos y venture builders que shippean "
                    "varias landings para clientes distintos. Proyectos ilimitados y "
                    "white-label completo.",
                "cta":         "Habla con nosotros",
                "cta_href":    "contatti",
                "perks": [
                    ("✓", "Todo Scale +"),
                    ("✓", "Proyectos ilimitados · branding white-label"),
                    ("✓", "Subcuentas para cada cliente"),
                    ("✓", "API completa · webhooks custom"),
                    ("✓", "SLA 1h · soporte telefónico"),
                    ("✓", "Account manager dedicado"),
                    ("✓", "Quarterly review con el founding team"),
                    ("✓", "Audit trail · compliance SOC 2"),
                ],
            },
        ],

        # Comparison — what's NOT included
        "comparison_label":   "Qué no hay (y por qué)",
        "comparison_heading": "La transparencia que los demás evitan",
        "comparison": [
            ("Setup fee",
             "Nunca. Ni en Launch, ni en Scale, ni en Studio. Si encuentras "
             "un boilerplate competidor que no te cobre setup fee y te dé "
             "el stack ya cableado, avísanos y te reembolsamos el primer mes."),
            ("Lock-in del código",
             "Nunca. Todo tu código es exportable desde la CLI en un comando. "
             "Si decides dejar Elevate, te movemos el deploy a un "
             "Vercel de tu propiedad gratis en 24h."),
            ("Tarifas ocultas",
             "Nunca. Lo que lees es lo que pagas. El IVA UE se "
             "calcula automáticamente y se muestra en checkout — "
             "cero sorpresas en la factura."),
            ("Límite de transacciones",
             "Nunca. Stripe Connect no tiene tope de transacciones ni de volumen. "
             "Vendas 10 suscripciones o 10.000 — el precio es el mismo."),
        ],

        # FAQ accordion
        "faq_label":   "Preguntas frecuentes",
        "faq_heading": "Lo que más nos preguntáis",
        "faq": [
            ("¿Puedo probar antes de pagar?",
             "Sí, catorce días de trial completo sin tarjeta de crédito. "
             "Tienes acceso a todos los módulos del plan Scale durante el trial — "
             "si decides quedarte, eliges el plan que te encaja. Si no "
             "decides, el trial caduca automáticamente, sin cargos automáticos."),
            ("¿Qué pasa si cancelo?",
             "Cancelas desde el dashboard en un clic, en cualquier momento. "
             "Tu deploy sigue live hasta el final del periodo ya pagado. "
             "Te exportamos el código por CLI y te ayudamos a migrar a un "
             "Vercel/Netlify propio si quieres continuar por tu cuenta."),
            ("¿Tenéis descuento para startups?",
             "Sí, el 50% sobre los primeros seis meses para startups pre-seed "
             "(ronda <500 K €) y el 30% sobre el primer año para post-seed. Escribe a "
             "hello@elevatekit.io con el pitch deck para activar la promoción."),
            ("¿Se integra con nuestro stack existente?",
             "Probablemente sí. Las 12 integraciones nativas cubren el 90% de los "
             "stacks que vemos, y la API REST + webhooks custom permiten "
             "conectar lo que falte. Si te hace falta una integración "
             "que no está, escríbenos por Slack — normalmente la shippeamos en "
             "dos semanas."),
            ("¿Puedo self-hostear?",
             "En el plan Studio, sí — te damos el contenedor Docker y el "
             "esquema Postgres para hospedarlo donde prefieras. En los planes Launch "
             "y Scale, el hosting está incluido y forma parte del valor del kit."),
            ("¿Las facturas son italianas?",
             "Sí, facturamos desde Milán en EUR con NIF-IVA italiano, "
             "facturación electrónica SDI incluida. Para clientes UE no-IT "
             "la factura va en reverse-charge IVA."),
        ],

        "cta_heading":   "¿Listo para empezar?",
        "cta_intro":
            "Catorce días gratis. Sin tarjeta de crédito. "
            "Cuarenta minutos para ir live con tu primer deploy.",
        "cta_primary":   "Activa el trial",
        "cta_primary_href": "demo",
        "cta_secondary": "¿Dudas? Escríbenos",
        "cta_secondary_href": "contatti",
    },

    # ─── DEMO (lead form) ───────────────────────────────────────
    "demo": {
        "eyebrow":  "Demo en directo · martes 17:00 CET",
        "headline": "Media hora con un <em>founding member</em>.",
        "intro":
            "Demo en directo todos los martes a las 17:00 CET. Treinta minutos de "
            "screen-share — enseñamos cómo se configura un tier pricing, "
            "cómo se lanza un A/B test, cómo se hace el primer deploy. "
            "Preguntas técnicas bienvenidas, pitch decks no necesarios.",

        # Form
        "form_label":   "Reserva un slot",
        "form_heading": "Rellena y te confirmamos en una hora",
        "form_intro":
            "El slot del próximo martes es el que recibirás por defecto. "
            "Si prefieres un slot ad hoc, elige 'Slot personalizado' y "
            "te escribimos para fijarlo. ¿Solo async? Sin problema, mira más abajo.",
        "form_fields": [
            {"name": "name",     "label": "Nombre",        "type": "text",  "required": True,  "placeholder": "P. ej. Ana",
             "helper": "Para saludarte en la demo."},
            {"name": "email",    "label": "Email",         "type": "email", "required": True,  "placeholder": "ana@startup.io",
             "helper": "La invitación al calendar y el Loom llegan aquí."},
            {"name": "company",  "label": "Startup",       "type": "text",  "required": True,  "placeholder": "P. ej. Quanta Analytics",
             "helper": "El nombre que usas para commits y facturación."},
            {"name": "role",     "label": "Rol",           "type": "select","required": True,
             "options": ["Founder en solitario", "Co-founder · CEO", "Co-founder · CTO", "Co-founder · otro", "Hire 1-5", "Otro"],
             "helper": "Si estás solo, \"Founder en solitario\" es la opción correcta."},
            {"name": "stage",    "label": "Fase",          "type": "select","required": True,
             "options": ["Pre-idea / explorando", "Pre-launch / waitlist", "Post-launch / buscando PMF", "Post-PMF / scaling"],
             "helper": "La demo se adapta: pre-launch ve onboarding + waitlist, post-PMF ve tier pricing + A/B."},
            {"name": "slot",     "label": "Slot preferido","type": "select","required": True,
             "options": ["Próximo martes 17:00 CET", "Slot personalizado (te escribimos)", "Async — quiero un Loom grabado"],
             "helper": "Slot async = recibes al momento el Loom de 12 min por email."},
            {"name": "stack",    "label": "Stack actual",
             "type": "text", "required": False,
             "placeholder": "P. ej. Next.js + Vercel + Stripe",
             "helper": "Opcional. Nos orientamos de inmediato a los integration points correctos."},
            {"name": "context",  "label": "¿Qué necesitas saber?", "type": "textarea",
             "required": False, "full_width": True,
             "placeholder": "Preguntas concretas, bloques que quieras ver en demo, dudas técnicas... (opcional)",
             "helper": "Con dos líneas basta. Cualquier duda técnica la tratamos en abierto."},
        ],

        "form_sections": [
            {"num": "01", "title": "Quién eres",
             "meta": "Sin BDR, sin sequence — te responde un founding member.",
             "fields": ["name", "email", "company"]},
            {"num": "02", "title": "Contexto",
             "meta": "Para adaptar la demo a tu stage y stack.",
             "fields": ["role", "stage", "stack"]},
            {"num": "03", "title": "Preferencias de demo",
             "meta": "En directo todos los martes a las 17:00 CET, o async vía Loom.",
             "fields": ["slot", "context"]},
            {"num": "04", "title": "Materiales (opcionales)",
             "meta": "Un Loom tuyo, screenshots del producto o un snapshot de métricas "
                     "nos permiten llegar preparados.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "demo_allegati",
            "label":    "Materiales de contexto",
            "helper":   "PDF, PNG, JPG, MP4, MOV · máx. 3 archivos, 25 MB en total. "
                        "Útil para quien quiera enseñarnos el producto o un funnel actual.",
            "accept":   ".pdf,.png,.jpg,.jpeg,.mp4,.mov",
            "multiple": True,
            "primary":  "Arrastra aquí el deck, screenshots o Loom o bien",
            "link":     "explora desde la carpeta",
            "meta":     "PDF / PNG / JPG / MP4 · máx. 25 MB",
        },

        "form_submit_label": "Reserva la demo",
        "form_submit_note":
            "Confirmación en una hora dentro del horario de oficina (9-19 CET) · sin newsletter, "
            "sin sequence automática.",
        "form_consent":
            "Al suscribirte aceptas el envío de la invitación al calendar y de un correo "
            "recordatorio 24h antes. Sin newsletter, sin sequence "
            "automática. Tratamiento de datos conforme al Reg. UE 679/2016.",

        # Async option block
        "async_label":   "¿Prefieres async?",
        "async_heading": "Loom grabado de 12 minutos",
        "async_intro":
            "Si no puedes hacer la demo en directo, hemos grabado un Loom "
            "de doce minutos que enseña el setup completo end-to-end. "
            "Lo recibirás por email en una hora desde la solicitud.",
        "async_cta":     "Recibe el Loom por email",
        "async_cta_href": "demo",

        # Trust strip
        "trust_label":   "Qué esperar de la demo",
        "trust_items": [
            ("01", "Media hora de screen-share",
             "Sin diapositivas. Abrimos la app, configuramos un tier pricing, lanzamos un A/B test, deployamos."),
            ("02", "Preguntas técnicas bienvenidas",
             "Latencia edge, esquema Postgres, webhooks Stripe — cualquier "
             "pregunta de implementación la jugamos en abierto."),
            ("03", "Sin presión",
             "No cerramos en la call. Si te hace falta, te damos acceso al trial "
             "al momento; si no, hablamos dentro de una semana."),
        ],

        "footnote":
            "Las demos las da uno de los tres founding members de Elevate "
            "(no un BDR externo). Si la ventana de las 17:00 del martes no "
            "te encaja por zona horaria, te proponemos un slot alternativo por "
            "email en 24 horas.",
    },

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Habla con nosotros · async-first",
        "headline": "Slack, email o demo en directo. <em>Tú eliges</em>.",
        "intro":
            "Async-first significa que respondemos en una hora durante el horario "
            "de oficina (9-19 CET) y que las decisiones se toman por escrito. "
            "Si prefieres una call, basta con reservarla — está incluida en todos "
            "los planes, sin extra.",

        # Channels grid — 4 ways to reach
        "channels_label":   "Cuatro canales, una sola persona te responde",
        "channels": [
            {
                "icon":  "✉",
                "title": "Email",
                "value": "hello@elevatekit.io",
                "desc":  "El founding team lo lee todo. Respuesta en 1h dentro del horario de oficina.",
                "cta":   "Escribe ahora",
            },
            {
                "icon":  "#",
                "title": "Comunidad Slack",
                "value": "elevate-founders.slack.com",
                "desc":  "Canal para quien haya activado el trial o un plan. Más de 220 founders dentro.",
                "cta":   "Solicita la invitación",
            },
            {
                "icon":  "▶",
                "title": "Demo en directo",
                "value": "Martes 17:00 CET",
                "desc":  "Treinta minutos de screen-share con un founding member. Opción async disponible.",
                "cta":   "Reserva el slot",
            },
            {
                "icon":  "✱",
                "title": "Office hours founder",
                "value": "Viernes 11:00 CET",
                "desc":  "Open call semanal para planes Scale y Studio. Preguntas públicas, respuestas abiertas.",
                "cta":   "Apúntate al calendar",
            },
        ],

        # Founders block — 3 founders with emails (transparency signal)
        "team_label":   "El founding team",
        "team_heading": "Las personas que leen tus emails",
        "team_intro":
            "Cuando escribes a hello@elevatekit.io, una de estas tres personas "
            "te responde — no un BDR externo, no un copilot IA. Abajo, "
            "sus emails directos para peticiones específicas.",
        "team": [
            {
                "name":  "Riccardo Camillini",
                "role":  "Co-founder · Product",
                "email": "riccardo@elevatekit.io",
                "tag":   "Preguntas de producto · roadmap",
                "bio":
                    "Tres exits anteriores como technical founder, "
                    "la última con un fondo SaaS B2B europeo. Se ocupa de "
                    "product strategy, roadmap y decisiones de arquitectura.",
            },
            {
                "name":  "Beatrice Lavia",
                "role":  "Co-founder · Engineering",
                "email": "beatrice@elevatekit.io",
                "tag":   "Preguntas técnicas · stack · API",
                "bio":
                    "Ocho años como senior engineer en Vercel y Linear. "
                    "Ha arquitectado el edge analytics y todos los adapters "
                    "de deploy. Responde a cualquier pregunta de implementación.",
            },
            {
                "name":  "Tommaso Adami",
                "role":  "Co-founder · Growth",
                "email": "tommaso@elevatekit.io",
                "tag":   "Onboarding · pricing · partnerships",
                "bio":
                    "Ex growth lead de una scale-up fintech europea. "
                    "Se ocupa de onboarding, estrategia de pricing, descuentos "
                    "para startups pre-seed y partnerships con aceleradoras.",
            },
        ],

        # Office meta-row labels
        "office_address_label":   "Sede",
        "office_transport_label": "Transporte",
        "office_model_label":     "Modelo",

        # Studio info — async-first office
        "office_label":   "Oficina async-first",
        "office_heading": "Dónde estamos (aunque nos encuentres online)",
        "office_intro":
            "La oficina física está en Talent Garden Calabiana en Milán, pero el "
            "equipo está distribuido (Milán, Berlín, Lisboa, Cracovia). "
            "Async-first significa que las reuniones internas se reducen al mínimo "
            "y que casi todo se decide en Linear mediante pull request.",
        "office": {
            "address":     "Talent Garden Calabiana · Via Calabiana 6 · 20139 Milán",
            "transport":   "M3 Lodi · 8 minutos andando · parking interior disponible",
            "hours":       "Async-first · founders en oficina martes y jueves",
            "schedule": [
                ("Slack",          "Lun – Vie · 9:00 – 19:00 CET"),
                ("Email",          "Respuesta en 1h dentro de horario · en 24h fuera de horario"),
                ("Demo on-demand", "Martes 17:00 CET · async vía Loom en cualquier momento"),
                ("Office hours",   "Viernes 11:00 CET · para planes Scale y Studio"),
            ],
        },

        "footnote":
            "Elevate es un equipo de seis personas — tres founders + tres engineers. "
            "Te responderemos personalmente a tu email. Si no oyes nada "
            "en 24h, no se ha perdido: escribe por Slack y nos activas un "
            "recordatorio. Prometido, ninguna petición queda sin leer.",
    },
}
