"""Aura — Digital Studio · IT content registry.

Agency live rollout, Phase 2g3.6f, Session 49.

Voice contract (Milan / Torino / Bologna digital-product-studio register):
- Second-person / imperative light ("prenota una call", "parliamone", "vediamolo").
- Growth-tech lexicon: "sprint", "discovery", "backlog", "telemetria",
  "product-market fit", "dashboard", "funnel", "onboarding", "NPS".
  Mai vocabolario curatoriale / editoriale (quello è Vertex).
- Clients are tech / SaaS / product / scale-up — fintech italiane,
  piattaforme europee, B2B, early-stage con Serie A.
- Numbers explicit and measurable. "+34%", "6 settimane", "Δ NPS +22",
  "MRR € 840k". Mai "abbiamo cura" — la voce è diretta, misurata.
- Mono usato per: sprint ID, status, KPI, timestamp, stack logos.
"""
from __future__ import annotations

from typing import Any


AURA_CONTENT_IT: dict[str, Any] = {

    "pages": [
        {"slug": "home",         "label": "Studio",        "kind": "home"},
        {"slug": "studio",       "label": "Chi siamo",     "kind": "about"},
        {"slug": "capabilities", "label": "Capabilities",  "kind": "services"},
        {"slug": "lavori",       "label": "Lavori",        "kind": "project_list"},
        {"slug": "sprint",       "label": "Sprint",        "kind": "process"},
        {"slug": "brief",        "label": "Brief",         "kind": "contact"},
    ],

    # ── Site chrome ──────────────────────────────────────────────
    "site": {
        "logo_word":   "Aura",
        "tag":         "Digital · product · growth studio",
        "sprint_chip": "Sprint 07/Q2 · live",
        "nav_cta":     "Prenota una call",
        "inquiry_page_slug": "brief",
        "phone":       "+39 02 8728 4411",
        "email":       "hello@aura.studio",
        "address":     "Via Paolo Sarpi 41 · 20154 Milano",
        "hours_compact":"Call slots · lun — gio · 10 — 18",
        "license":     "P.IVA 12890440964 · Milano",
        "footer_intro":
            "Studio digitale indipendente. Disegniamo prodotti, "
            "piattaforme e sistemi di crescita per scale-up e "
            "aziende tech. Basati a Milano, delivery europea.",
        "foot_shiplog_label":    "// ship log · last 6",
        "foot_current_sprint":   "sprint 07/Q2 · live",
        "foot_shiplog_rows": [
            ("ieri · 18:04",  "v2.14",  "Soldo — nuovo onboarding corporate live"),
            ("ieri · 09:21",  "v2.13",  "Fastweb Plus — dashboard residenziale v2.3"),
            ("lun · 15:30",  "v2.12",  "Lendlease — portale asset manager"),
            ("ven · 11:12",  "v2.11",  "Casavo — retention A/B loop 003"),
            ("gio · 17:45",  "v2.10",  "Milkman — SDK ship tracking"),
            ("mer · 10:02",  "v2.09",  "Fiscozen — onboarding self-serve"),
        ],
        "foot_stack_marquee": [
            "Figma", "Linear", "Notion", "GitHub", "Vercel", "Stripe",
            "Segment", "PostHog", "Supabase", "Framer", "Mixpanel", "Sentry",
        ],
        "foot_studio_label":  "Studio",
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
        "chip": "3 slot disponibili · Q3 2026",
        "headline": "Dalla <em>call di discovery</em> al <em>primo KPI</em> in sei settimane.",
        "intro":
            "Siamo uno studio digitale che costruisce prodotti e "
            "sistemi di crescita per scale-up italiane ed europee. "
            "Sprint di due settimane, dashboard condiviso, "
            "consegne misurabili. Zero agenzia, tutto prodotto.",
        "primary_cta":   "Prenota una call",
        "primary_href":  "brief",
        "secondary_cta": "Lavori recenti",
        "secondary_href":"lavori",

        "hero_metrics": [
            ("<em>47</em>",     "prodotti spediti dal 2019"),
            ("<em>+34%</em>",   "conversione mediana post-rework"),
            ("<em>6 sett.</em>","dallo sprint zero al primo KPI"),
        ],

        # Dashboard console tile
        "console": {
            "path":           "aura.studio/clients/casavo/live",
            "status_chip":    "LIVE · sprint 07/Q2",
            "primary_metric": "+34%",
            "primary_label":  "Conversione post-rework · ultimi 30 giorni",
            "kpi": [
                ("<em>+18%</em>",    "Retention giorno 30"),
                ("<em>Δ 22</em>",    "NPS pre / post · Casavo"),
                ("<em>€ 840K</em>",  "MRR · sprint 1 – 14"),
                ("<em>99.98%</em>",  "Uptime ultimo trimestre"),
            ],
            "meta_label":     "Sprint corrente",
            "meta_value":     "07/Q2 · week 2 of 2",
        },

        # Capabilities mini
        "capab_label":   "Capabilities",
        "capab_heading": "Quattro <em>aree</em>, un solo team.",
        "capab_intro":
            "Lavoriamo per quattro tipi di progetto — lanci di prodotto, "
            "redesign di piattaforma, sistemi di crescita e delivery di "
            "piattaforme B2B. Ogni progetto attraversa un team di 3-5 persone "
            "dedicate, mai un account layer.",
        "capab_cards": [
            {
                "id":   "C.01",
                "title":"Product <em>launch</em>",
                "body": "Dal concept all'onboarding live. "
                        "Ideale per scale-up alla Serie A che devono "
                        "passare da MVP a prodotto pagante.",
                "tags": ["Discovery", "Design system", "Next.js", "Analytics"],
            },
            {
                "id":   "C.02",
                "title":"Platform <em>redesign</em>",
                "body": "Ripensare prodotti maturi senza perdere utenti. "
                        "Research, A/B test, migrazione progressiva.",
                "tags": ["UX audit", "A/B", "Incremental ship", "PostHog"],
            },
            {
                "id":   "C.03",
                "title":"Growth <em>systems</em>",
                "body": "Onboarding, retention, referral, pricing experiments. "
                        "Quick wins nei primi 30 giorni, sistemi a 90 giorni.",
                "tags": ["Onboarding", "Retention", "Pricing", "Experiments"],
            },
            {
                "id":   "C.04",
                "title":"B2B <em>delivery</em>",
                "body": "Portali asset manager, dashboard corporate, "
                        "backoffice interni. Integrazione SSO + data warehouse.",
                "tags": ["Dashboards", "SSO", "Roles", "BigQuery"],
            },
        ],

        # Sprint strip
        "sprint_label":   "Il modo in cui consegnamo",
        "sprint_heading": "Quattro <em>sprint</em>, dalla discovery alla scala.",
        "sprint_intro":
            "Ogni progetto è strutturato in sprint di due settimane. "
            "Vedi esattamente cosa stiamo facendo, quando verrà consegnato, "
            "e quali metriche stiamo muovendo. Nessuna sorpresa di fine mese.",
        "sprints": [
            {
                "id":"S.00", "duration":"Sprint 0 · 1 settimana",
                "title":"<em>Signal</em>",
                "body": "Discovery con gli stakeholder, utenti, dashboard. "
                        "Restituzione: brief condiviso + backlog iniziale.",
                "output": "OUT · brief + backlog",
            },
            {
                "id":"S.01", "duration":"Sprint 1 — 2 · 4 sett.",
                "title":"<em>Sketch</em>",
                "body": "Design system + prototipi testabili. "
                        "Research qualitativa + prime A/B sulle hypothesis critiche.",
                "output": "OUT · prototype + design tokens",
            },
            {
                "id":"S.02", "duration":"Sprint 3 — 5 · 6 sett.",
                "title":"<em>Ship</em>",
                "body": "Implementazione staging → produzione. "
                        "Monitoraggio live di metriche, rollback disponibili a 1 click.",
                "output": "OUT · production + first KPI",
            },
            {
                "id":"S.03", "duration":"Sprint 6+ · ongoing",
                "title":"<em>Scale</em>",
                "body": "Esperimenti continui, feature expansion, "
                        "ottimizzazione post-launch. Partner ship-log condiviso.",
                "output": "OUT · weekly ship-log",
            },
        ],

        # Lavori cards
        "work_label":      "Lavori recenti",
        "work_heading":    "Sette <em>prodotti</em>, sette <em>metriche</em>.",
        "work_intro":
            "Ogni progetto ha una metrica chiara, dichiarata in sprint zero "
            "e misurata in sprint tre. Se la metrica non si muove, lavoriamo "
            "gratis fino a quando non si muove.",
        "work_page_slug": "lavori",
        "work_cards": [
            {
                "slug": "casavo-retention-rework",
                "id":   "W.01",
                "cover":"https://images.unsplash.com/photo-1551434678-e076c223a692?w=900&q=80&auto=format&fit=crop",
                "title":"Retention rework di tre mesi",
                "client":"Casavo · Proptech Milano",
                "metric_chip": "+18% retention · D30",
                "stack":["Next.js", "PostHog", "Figma"],
            },
            {
                "slug": "fastweb-plus-dashboard",
                "id":   "W.02",
                "cover":"https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=900&q=80&auto=format&fit=crop",
                "title":"Dashboard residenziale v2",
                "client":"Fastweb · Telco Italia",
                "metric_chip": "NPS +22 · 6 mesi",
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
            ("<em>47</em>",      "prodotti spediti",     "dal 2019 — media 8 / anno"),
            ("<em>+34%</em>",    "conversione mediana",  "tra pre- e post-rework"),
            ("<em>99.98%</em>",  "uptime",               "ultimo trimestre · status.aura.studio"),
            ("<em>6 sett.</em>", "time to first KPI",    "dallo sprint zero alla prima metrica mossa"),
        ],

        "cta_label":   "Prossima call",
        "cta_heading": "Tre <em>slot</em> aperti per Q3 2026.",
        "cta_sub":
            "Il primo slot è una call di discovery di 30 minuti. Se il "
            "progetto fa per noi, nei successivi 5 giorni ricevi un "
            "brief di lettura + stima di sprint zero.",
        "cta_chip":    "30 min · zero committment",
        "cta_primary": "Prenota una call",
    },

    # ── STUDIO (about) ───────────────────────────────────────────
    "studio": {
        "chip": "Team · 11 persone · Milano + remote",
        "headline": "Un team di <em>undici</em>, <em>otto anni</em> di prodotti spediti.",
        "standfirst":
            "Aura è uno studio di product design e ingegneria fondato a "
            "Milano nel 2019. Undici persone — cinque designer, quattro "
            "engineer, due product manager — distribuite tra Milano, Torino "
            "e remote. Zero account manager, zero livelli intermedi: "
            "chi firma il brief è chi lo spedisce.",

        "facts": [
            ("<em>11</em>",    "persone", "5 design · 4 eng · 2 PM"),
            ("<em>47</em>",    "prodotti spediti", "Dal 2019 a oggi"),
            ("<em>3</em>",     "sedi", "Milano · Torino · remote"),
            ("<em>94%</em>",   "clienti rinnovano", "Tasso di retention 2024"),
        ],

        "story_label":   "Storia dello studio",
        "story_heading": "Come <em>scale-up</em> ci ha costretto a ripensare il design studio.",
        "story_paragraphs": [
            "Aura nasce nel 2019 da Luca Bianchi e Sofia Reggiani, "
            "ex product designer in Spotify e Figma. L'idea iniziale era "
            "semplice: <em>non vogliamo essere un'agenzia, non vogliamo "
            "essere freelance</em>. Volevamo uno studio che lavorasse "
            "come un team interno — con gli stessi strumenti, le stesse "
            "metriche, la stessa cadenza — ma da fuori.",
            "I primi tre anni sono stati di apprendimento. Abbiamo capito "
            "che le scale-up italiane non avevano bisogno di <em>design</em> "
            "— avevano bisogno di <em>delivery</em>. Così abbiamo assunto "
            "engineer full-stack. Abbiamo capito che non bastava la design "
            "review — serviva il ship log. Abbiamo capito che il valore "
            "non era nei mockup, ma nelle metriche mosse.",
            "Oggi Aura lavora con 6-8 clienti all'anno, in sprint da due "
            "settimane, con una metrica dichiarata all'inizio di ogni "
            "progetto. Ogni progetto pubblica un ship log interno che il "
            "cliente può leggere in tempo reale. Se la metrica non si "
            "muove, lavoriamo gratis fino a quando non si muove. "
            "È l'unico modo in cui sappiamo lavorare.",
        ],

        "team_label":   "Il team",
        "team_heading": "Chi <em>spedisce</em> i progetti.",
        "team_intro":
            "Ogni progetto è seguito da un team dedicato di 3-5 persone. "
            "I team vengono composti in base al tipo di progetto e non "
            "cambiano in corsa. Chi inizia il progetto, lo spedisce.",
        "team": [
            {
                "name": "Luca Bianchi",
                "role": "Co-fondatore · Head of product",
                "bio":  "Ex Spotify (Stoccolma · 2014-2018) e Figma "
                        "(San Francisco · 2018-2019). Ha guidato il "
                        "team di growth design per il mercato EU. "
                        "Si occupa della definizione degli sprint.",
                "portrait": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=900&q=80&auto=format&fit=crop",
                "stack": ["Figma", "Linear", "PostHog", "Notion"],
            },
            {
                "name": "Sofia Reggiani",
                "role": "Co-fondatrice · Head of engineering",
                "bio":  "Ex Spotify (Stoccolma) e Google (Londra). "
                        "Ha guidato la migrazione Next.js di due piattaforme "
                        "pan-europee. Si occupa della stack di delivery.",
                "portrait": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop",
                "stack": ["Next.js", "TypeScript", "Vercel", "Supabase"],
            },
            {
                "name": "Matteo Leone",
                "role": "Principal product designer",
                "bio":  "Otto anni in Satispay (Milano) prima di "
                        "unirsi ad Aura nel 2022. Ha disegnato tre "
                        "onboarding per fintech italiane con >1M utenti.",
                "portrait": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=900&q=80&auto=format&fit=crop",
                "stack": ["Figma", "Framer", "Stripe Elements"],
            },
        ],

        "values_label":   "Come lavoriamo",
        "values_heading": "<em>Quattro regole</em> che non negoziamo.",
        "values": [
            ("V.01", "Una <em>metrica</em> dichiarata",
             "Ogni progetto ha una metrica chiara definita in sprint zero. "
             "Se non si muove, restiamo fino a quando non si muove."),
            ("V.02", "Un <em>team</em> dedicato",
             "Chi inizia il progetto, lo spedisce. Zero account manager, "
             "zero handoff. Il designer che disegna è lo stesso che ship-a."),
            ("V.03", "Un <em>ship-log</em> pubblico",
             "Il cliente ha accesso in tempo reale al ship-log interno. "
             "Vede cosa abbiamo spedito, quando, perché, e cosa è fallito."),
            ("V.04", "Una <em>call</em> alla settimana",
             "Una sola riunione sincrona a settimana, di 30 minuti, "
             "con agenda scritta. Il resto è async su Linear e Slack."),
        ],
    },

    # ── CAPABILITIES (services) ──────────────────────────────────
    "capabilities": {
        "chip": "4 aree · 3-5 persone per progetto",
        "headline": "Quattro <em>capabilities</em>, tutte misurate.",
        "standfirst":
            "Ogni capability ha un metodo documentato, una metrica tipica, "
            "una durata prevedibile e uno stack predefinito. Non è un "
            "listino — è un sistema che ci permette di dirti, in sprint zero, "
            "cosa aspettarti e quando.",

        "capabilities": [
            {
                "id": "CAP.01 · Product launch",
                "title": "Portare <em>un prodotto nuovo</em> alla prima conversione.",
                "tagline": "Tipico: 14 — 20 sett. · KPI · attivazione + first paid",
                "body":
                    "Per scale-up che hanno validato il problema (Serie Seed / A) "
                    "e devono costruire il prodotto pagante. Partiamo dallo "
                    "sprint zero (research + backlog), passiamo per il design "
                    "system + le prime tre flow critiche, portiamo in produzione "
                    "con onboarding misurabile e pricing vivo.",
                "scope_label": "// scope",
                "scope": [
                    "Sprint zero + user research",
                    "Design system (tokens + 60 componenti)",
                    "Tre flow critiche in produzione",
                    "Onboarding self-serve",
                    "Pricing page live + Stripe",
                    "Analytics + funnel completo",
                    "Rollback + feature flag",
                    "Handover docs al team interno",
                ],
                "stack": ["Next.js 14", "TypeScript", "Figma", "Stripe", "Segment", "PostHog"],
            },
            {
                "id": "CAP.02 · Platform redesign",
                "title": "<em>Ri-disegnare</em> un prodotto maturo senza perdere utenti.",
                "tagline": "Tipico: 20 — 30 sett. · KPI · retention + NPS",
                "body":
                    "Per piattaforme con > 50k utenti attivi che hanno accumulato "
                    "debito di UX. Partiamo da un audit quantitativo + qualitativo, "
                    "costruiamo il nuovo sistema in parallelo, migriamo "
                    "progressivamente via feature flag. Nessun big-bang launch.",
                "scope_label": "// scope",
                "scope": [
                    "UX audit + quant analysis",
                    "30+ interviste utente",
                    "Migrazione progressiva",
                    "A/B test su cohort",
                    "Design system evolution",
                    "Rollout per mercato",
                    "Post-launch tuning · 8 sett.",
                    "Training team interno",
                ],
                "stack": ["React", "Django", "PostHog", "Segment", "Split.io"],
            },
            {
                "id": "CAP.03 · Growth systems",
                "title": "<em>Sistemi di crescita</em> misurabili in 30 giorni.",
                "tagline": "Tipico: 8 — 16 sett. · KPI · conversion + LTV",
                "body":
                    "Per prodotti già in produzione che devono crescere. "
                    "Lavoriamo su onboarding, pricing, retention, referral. "
                    "Quick wins nei primi 30 giorni (usualmente +12% su un funnel). "
                    "Sistemi a 90 giorni (nuovi esperimenti continui).",
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
                "title": "Portali <em>asset manager</em> e dashboard corporate.",
                "tagline": "Tipico: 24 — 36 sett. · KPI · task completion + time saved",
                "body":
                    "Per aziende B2B (proptech, fintech, healthtech) che devono "
                    "consegnare portali ai loro clienti enterprise. SSO, ruoli, "
                    "permessi, data warehouse integrato, export strutturati. "
                    "Non è sexy, ma è dove si gioca il rinnovo annuale.",
                "scope_label": "// scope",
                "scope": [
                    "Discovery con 3-5 enterprise",
                    "Design tokens corporate",
                    "SSO (SAML · Okta · Azure)",
                    "Ruoli + permessi granulari",
                    "Data warehouse integration",
                    "Export multi-formato",
                    "Audit log compliance",
                    "SLA 99.9% + monitoring",
                ],
                "stack": ["Next.js", "BigQuery", "Okta", "Datadog", "Sentry"],
            },
        ],

        "engagement_label":   "Tre modi di ingaggio",
        "engagement_heading": "Dal <em>progetto singolo</em> al <em>partner continuativo</em>.",
        "engagement_intro":
            "Scegliamo il modello di ingaggio insieme, in sprint zero. "
            "Usualmente il 70% dei progetti parte come fisso, il 30% come "
            "partnership continuativa. Il tempo & materiali è raro, lo "
            "usiamo solo per discovery di meno di 3 settimane.",
        "engagement_tiles": [
            {
                "id":    "E.01 · Discovery",
                "title": "<em>Discovery sprint</em>",
                "range": "2 — 3 settimane · fisso",
                "body":  "Sprint zero dedicato. Research, audit, backlog, "
                         "stima. Se poi si procede, viene scalato.",
                "includes": [
                    "User research (5-8 interviste)",
                    "Audit quantitativo (analytics)",
                    "Backlog iniziale",
                    "Stima di delivery",
                    "Documento condiviso 30 pagine",
                ],
            },
            {
                "id":    "E.02 · Fixed delivery",
                "title": "<em>Fixed delivery</em>",
                "range": "8 — 30 settimane · fisso",
                "body":  "Lancio o redesign con scope e budget fissi. "
                         "Il più comune per scale-up alla Serie A.",
                "includes": [
                    "Team dedicato 3-5 persone",
                    "Sprint da 2 settimane",
                    "Ship-log condiviso",
                    "Metrica dichiarata",
                    "Rollback + feature flags",
                    "Handover documentato",
                ],
                "featured": True,
            },
            {
                "id":    "E.03 · Partner mode",
                "title": "<em>Partner mode</em>",
                "range": "Q-by-Q · rinnovo trimestrale",
                "body":  "Ingaggio continuativo per piattaforme mature. "
                         "Fascia di giorni/trimestre, roadmap condivisa.",
                "includes": [
                    "Weekly ship cadence",
                    "Condivisione backlog cliente",
                    "Experiment continuo",
                    "Review trimestrale KPI",
                    "SLA supporto + on-call",
                ],
            },
        ],

        "cta_label":   "Prossimo passo",
        "cta_heading": "Vediamoci in <em>discovery</em>, 30 minuti.",
        "cta_primary": "Prenota una call",
    },

    # ── LAVORI (project_list) ────────────────────────────────────
    "lavori": {
        "chip": "Archivio prodotti · 2019 — 2026",
        "headline": "<em>Quarantasette</em> prodotti spediti. <em>Sette</em> in vetrina.",
        "standfirst":
            "Ogni caso ha una metrica dichiarata e misurata. "
            "Mostriamo sette progetti pubblici — gli altri quaranta sono "
            "sotto NDA (comune in fintech e B2B). Archivio completo su richiesta.",
        "tabs": ["Tutti", "Product launch", "Redesign", "Growth", "B2B delivery"],
        "tabs_count_label": "// totali archivio",
        "tabs_count_value": "047",

        "projects": [
            {
                "slug": "casavo-retention-rework",
                "id":   "P.01",
                "cover":"https://images.unsplash.com/photo-1551434678-e076c223a692?w=1200&q=80&auto=format&fit=crop",
                "title":"Retention rework · piattaforma acquisto casa",
                "client":"Casavo",
                "discipline":"PROPTECH · REDESIGN",
                "year": "2025",
                "blurb":
                    "Ripensato l'intero funnel dalla ricerca alla firma. "
                    "Migrazione progressiva via feature flag su 180k utenti. "
                    "Nessun downtime, +18% retention a 30 giorni.",
                "kpi": [
                    ("<em>+18%</em>",  "retention D30"),
                    ("<em>Δ+22</em>",  "NPS"),
                    ("<em>180K</em>",  "utenti migrati"),
                ],
            },
            {
                "slug": "fastweb-plus-dashboard",
                "id":   "P.02",
                "cover":"https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80&auto=format&fit=crop",
                "title":"Dashboard residenziale v2.3",
                "client":"Fastweb",
                "discipline":"TELCO · PLATFORM",
                "year": "2024",
                "blurb":
                    "Un nuovo cruscotto per 2.8M clienti residenziali. "
                    "SSO integrato, gestione servizi, self-care completo. "
                    "Riduzione chiamate call center −34% in sei mesi.",
                "kpi": [
                    ("<em>−34%</em>",   "chiamate CC"),
                    ("<em>2.8M</em>",   "utenti"),
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
                    "Da onboarding assistito (4 giorni mediani) a self-serve "
                    "(42 minuti). Compliance pan-EU, KYC integrato, "
                    "multi-currency day zero.",
                "kpi": [
                    ("<em>−54%</em>",      "TTFV"),
                    ("<em>+41%</em>",      "activation"),
                    ("<em>7 mercati</em>", "day one"),
                ],
            },
            {
                "slug": "milkman-ship-sdk",
                "id":   "P.04",
                "cover":"https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=1200&q=80&auto=format&fit=crop",
                "title":"SDK di ship tracking per retailer",
                "client":"Milkman",
                "discipline":"LOGISTICS · B2B",
                "year": "2024",
                "blurb":
                    "Un SDK JavaScript per tracking consegne integrato nel "
                    "checkout di 40+ retailer. Una sola chiamata API, "
                    "branding retailer-side, aggiornamenti real-time.",
                "kpi": [
                    ("<em>40+</em>",    "retailer"),
                    ("<em>1 chiam.</em>","API"),
                    ("<em>2MB</em>",    "bundle"),
                ],
            },
            {
                "slug": "lendlease-asset-portal",
                "id":   "P.05",
                "cover":"https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200&q=80&auto=format&fit=crop",
                "title":"Portale asset manager enterprise",
                "client":"Lendlease",
                "discipline":"PROPTECH · B2B",
                "year": "2024",
                "blurb":
                    "Un portale per 80 asset manager italiani. SSO Azure, "
                    "ruoli granulari, data warehouse integrato con "
                    "export multi-formato. Compliance MiFID II inclusa.",
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
                "title":"Onboarding self-serve partite IVA",
                "client":"Fiscozen",
                "discipline":"FISCTECH · GROWTH",
                "year": "2024",
                "blurb":
                    "Da onboarding assistito da commercialista a self-serve "
                    "completo. Riduzione tempi di attivazione e +47% di "
                    "conversione da trial a paid nei primi 90 giorni.",
                "kpi": [
                    ("<em>+47%</em>",   "trial → paid"),
                    ("<em>18 min.</em>","TTFV"),
                    ("<em>90 gg</em>",  "misurazione"),
                ],
            },
        ],

        "velocity_label":   "Velocity media",
        "velocity_heading": "Come <em>spediamo</em> · ultimi dodici mesi.",
        "velocity_body":
            "I numeri qui sotto sono quelli che guardiamo internamente. "
            "Aggiornati mensilmente. Se ti interessa la metodologia dietro, "
            "ne parliamo volentieri in call di discovery.",
        "velocity_stats": [
            ("<em>8</em>",      "prodotti spediti · 2025"),
            ("<em>94%</em>",    "progetti on-time"),
            ("<em>+26%</em>",   "KPI mediano mosso"),
            ("<em>47 gg</em>",  "median time-to-ship"),
        ],
    },

    # ── SPRINT (process) ─────────────────────────────────────────
    "sprint": {
        "chip": "Metodologia · 4 fasi · telemetria live",
        "headline": "Quattro <em>sprint</em>, dalla discovery alla scala.",
        "standfirst":
            "Ogni progetto attraversa quattro fasi dichiarate. "
            "Durate prevedibili, consegne chiare, metriche pubbliche. "
            "Il cliente vede in tempo reale dove siamo — e perché.",

        "sprints": [
            {
                "id": "Sprint 0 · Signal",
                "duration": "1 settimana · fissa",
                "title": "<em>Capire</em> il problema, prima di disegnarlo.",
                "tagline": "// output: brief condiviso + backlog iniziale",
                "body":
                    "Sprint zero è la fase più importante e la più sottovalutata. "
                    "In cinque giorni ascoltiamo gli stakeholder (CEO, prodotto, "
                    "customer success), intervistiamo 5-8 utenti reali, leggiamo "
                    "la dashboard attuale. Alla fine presentiamo un brief di "
                    "lettura + backlog di ipotesi da testare.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Brief condiviso · 24 pagine",
                    "Backlog iniziale · Linear",
                    "Stakeholder map",
                    "Research summary · 5-8 interviste",
                    "Metrica dichiarata + baseline",
                    "Stima di delivery (sprint count)",
                ],
            },
            {
                "id": "Sprint 1 — 2 · Sketch",
                "duration": "4 settimane",
                "title": "<em>Prototipare</em> prima di costruire.",
                "tagline": "// output: prototipo testabile + design system v0.1",
                "body":
                    "I primi due sprint sono di prototipazione rapida. "
                    "Costruiamo in Figma + Framer le tre flow più critiche, "
                    "le testiamo con utenti reali, iteriamo. In parallelo "
                    "avviamo il design system (tokens + 20 componenti base). "
                    "Il codice vero arriva allo sprint 3.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Prototipo Figma interattivo",
                    "3 round di user testing",
                    "Design system v0.1",
                    "Architettura di codice",
                    "Piano di A/B test",
                    "Design review al cliente",
                ],
            },
            {
                "id": "Sprint 3 — 5 · Ship",
                "duration": "6 settimane",
                "title": "<em>Portare in produzione</em>, incrementale.",
                "tagline": "// output: production live + prima metrica",
                "body":
                    "Implementazione e delivery incrementale. Ogni venerdì ship-a "
                    "qualcosa in staging, ogni fine sprint in produzione. "
                    "Feature flag + rollback a 1 click. Alla fine dello sprint 5 "
                    "la prima metrica dichiarata deve essersi mossa.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Staging deploy settimanale",
                    "Production deploy bi-settimanale",
                    "Feature flags tutti attivi",
                    "Rollback plan documentato",
                    "Monitoring · Datadog / Sentry",
                    "Prima metrica mossa",
                ],
            },
            {
                "id": "Sprint 6+ · Scale",
                "duration": "ongoing · trimestrale",
                "title": "<em>Scalare</em> · esperimenti continui.",
                "tagline": "// output: ship-log settimanale + review KPI trimestrale",
                "body":
                    "Post-launch entriamo in modalità scale. Esperimenti "
                    "settimanali, feature expansion, ottimizzazione post-launch. "
                    "Ship-log condiviso pubblico. Review trimestrale delle "
                    "metriche contro piano.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Ship-log pubblico",
                    "A/B weekly",
                    "Feature roadmap 6 mesi",
                    "Review KPI trimestrale",
                    "Training team interno",
                    "Handover continuo",
                ],
            },
        ],

        "mindset_label":   "Come <em>pensiamo</em> al processo",
        "mindset_heading": "Tre <em>principi</em> di delivery.",
        "mindset_cards": [
            {
                "id": "P.01",
                "title": "<em>Telemetria</em> visibile",
                "body": "Il ship-log è pubblico per il cliente dal giorno zero. "
                        "Cosa abbiamo spedito, quando, perché. Zero stanze buie.",
            },
            {
                "id": "P.02",
                "title": "<em>Rollback</em> a 1 click",
                "body": "Ogni feature è dietro flag. Se qualcosa non funziona "
                        "in produzione, lo disattiviamo in meno di 60 secondi.",
            },
            {
                "id": "P.03",
                "title": "<em>Skin in the game</em>",
                "body": "Se la metrica dichiarata non si muove, continuiamo a "
                        "lavorare gratis. Lo abbiamo fatto quattro volte in otto anni.",
            },
        ],

        "stack_label":   "Stack di delivery",
        "stack_heading": "Con cosa <em>consegnamo</em>.",
        "stack_intro":
            "La stack è scelta per essere affidabile, veloce, e facile "
            "da passare al team interno del cliente. Zero tecnologie boutique.",
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
        "chip": "3 slot aperti · Q3 2026",
        "headline": "Raccontaci il <em>progetto</em>. Ti chiamiamo in meno di 48h.",
        "standfirst":
            "Questo non è un form. È un brief strutturato in 3 step. "
            "Ogni risposta che ricevi è scritta personalmente da Luca o "
            "Sofia, non da un account manager. Se il progetto fa per noi, "
            "il secondo messaggio è già una proposta di call.",

        "form_heading": "// brief intake · 3 step",

        "step1": {
            "id": "STEP 01", "title": "Chi sei", "sub": "Solo i campi strettamente necessari.",
        },
        "step2": {
            "id": "STEP 02", "title": "Il progetto", "sub": "Più concreto è, più utile la risposta.",
        },
        "step3": {
            "id": "STEP 03", "title": "Quando", "sub": "Scegli uno slot indicativo — confermiamo poi via email.",
        },

        "labels": {
            "name":    "Nome e cognome",
            "role":    "Ruolo",
            "company": "Azienda / prodotto",
            "email":   "Email di lavoro",
            "scope":   "Tipo di progetto",
            "brief":   "Racconto breve",
            "slot":    "Slot preferito",
        },
        "placeholders": {
            "name":    "Nome Cognome",
            "role":    "es. Head of Product",
            "company": "Nome azienda",
            "email":   "name@company.com",
            "brief":   "Cosa stai costruendo, a che punto sei (MRR, utenti, round), qual è il problema che stai sentendo, come misuri il successo. Un brief concreto riceve una risposta concreta.",
        },
        "scope_options": [
            "Product launch · prima volta live",
            "Platform redesign · prodotto maturo",
            "Growth systems · funnel / retention",
            "B2B delivery · portale / dashboard",
            "Discovery sprint · 2-3 settimane",
            "Non sono ancora sicuro — parliamone",
        ],

        "slots": [
            ("mon10", "Lun · 10:00"),
            ("mon15", "Lun · 15:00"),
            ("tue10", "Mar · 10:00"),
            ("tue15", "Mar · 15:00"),
            ("wed10", "Mer · 10:00"),
            ("wed15", "Mer · 15:00"),
            ("thu10", "Gio · 10:00"),
            ("thu15", "Gio · 15:00"),
            ("async", "Solo async via email"),
        ],
        "form_submit_label": "Prenota la call",
        "form_submit_note":  "// risposta entro 48h lavorative · tutti i fusi EU",

        "async_label":   "Preferisci async?",
        "async_heading": "Scrivi a <em>Luca</em> e <em>Sofia</em>.",
        "async_body":
            "Ogni email arriva direttamente ai due co-founder. "
            "Rispondono loro — non un account manager, non un bot.",

        "studio_label":  "Lo studio",

        "response_label": "// SLA di risposta",
        "response_rows": [
            ("Brief", "< 48h"),
            ("Proposta", "5 giorni"),
            ("Sprint zero", "2 settimane"),
            ("Prima metrica", "6 settimane"),
        ],

        "boot_left":  "aura.studio · hello@aura.studio · +39 02 8728 4411",
        "boot_right": "// sempre aperti al brief",
    },

    # ── POSTS (project_detail) ───────────────────────────────────
    "posts": [
        {
            "slug": "casavo-retention-rework",
            "id":   "P.01 · PROPTECH",
            "title": "Casavo · <em>+18% retention</em> in tre mesi.",
            "client": "Casavo · Proptech Milano",
            "discipline": "Redesign · retention",
            "duration": "14 settimane",
            "year": "2025",
            "standfirst":
                "Il rework del funnel post-prenotazione di Casavo. "
                "Un'ottimizzazione incrementale su 180k utenti, "
                "feature flag ovunque, zero downtime. Tre mesi dopo: "
                "+18% retention a 30 giorni, NPS +22, MRR +€ 840K.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1551434678-e076c223a692?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Gli utenti tornavano, ma non convertivano.",
            "problem_paragraphs": [
                "Casavo aveva raddoppiato gli utenti attivi tra il 2023 e il 2024, "
                "ma la conversione da <em>visita 1</em> a <em>prenotazione visita reale</em> "
                "era scesa del 12% — su 180k utenti attivi, questo significava ~21k "
                "prenotazioni perse ogni mese.",
                "Il team interno aveva capito che il problema era nel funnel "
                "post-iscrizione, ma non aveva capacity per testare 10+ ipotesi "
                "in modo serio senza rallentare il roadmap principale.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Un secondo funnel, in parallelo al vecchio.",
            "solution_paragraphs": [
                "Invece di riscrivere il funnel principale (rischio troppo alto su "
                "180k utenti) abbiamo costruito un <em>secondo funnel sperimentale</em> "
                "dietro feature flag, disponibile al 10% del traffico. Sei settimane "
                "di test, sette iterazioni, quattro flow testate.",
                "Alla sesta iterazione il secondo funnel batteva il primo del 18% "
                "su retention D30. Abbiamo migrato progressivamente il resto dei "
                "180k utenti in tre settimane — fase del 25%, poi 50%, poi 100%.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "Quattordici settimane, <em>sette sprint</em>.",
            "timeline_intro":
                "Il timeline qui sotto è la reale cronologia di delivery — estratta "
                "dal ship-log condiviso con Casavo.",
            "timeline_steps": [
                {"id": "S.00", "duration": "sett. 1",       "title": "<em>Signal</em>", "body": "Research + audit funnel + backlog 14 ipotesi."},
                {"id": "S.01", "duration": "sett. 2-3",     "title": "<em>Sketch</em>", "body": "Prototipi di 4 flow alternative, 8 interviste."},
                {"id": "S.02", "duration": "sett. 4-6",     "title": "<em>Ship</em>",   "body": "Secondo funnel live al 10%, primo A/B test."},
                {"id": "S.03", "duration": "sett. 7-11",    "title": "<em>Iterate</em>","body": "6 iterazioni weekly. Cohort ogni venerdì."},
                {"id": "S.04", "duration": "sett. 12-14",   "title": "<em>Migrate</em>","body": "Rollout al 25% → 50% → 100%. Zero downtime."},
            ],

            "results_label": "// results",
            "results_heading": "Quattro <em>metriche mosse</em>.",
            "results_stats": [
                ("<em>+18%</em>",     "retention D30",           "da 42% a 49.6% (90 gg rolling)"),
                ("<em>Δ +22</em>",    "NPS",                     "da 31 a 53 nei 3 mesi post-rollout"),
                ("<em>+€ 840K</em>",  "MRR incrementale",         "proiezione a 12 mesi"),
                ("<em>0</em>",        "downtime durante rollout", "180k utenti, zero errori 5xx extra"),
            ],

            "quote": "In tre mesi hanno capito il nostro prodotto meglio di consulenti che ci avevano lavorato per un anno. E hanno shippato.",
            "quote_author": "Marianna Colombo",
            "quote_role":   "VP Product · Casavo",

            "next_label":   "// next case",
            "next_heading": "→ vedi tutti i <em>lavori</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ prenota una <em>call</em>",
        },
        {
            "slug": "fastweb-plus-dashboard",
            "id":   "P.02 · TELCO",
            "title": "Fastweb · <em>−34% chiamate CC</em> in 6 mesi.",
            "client": "Fastweb · Telco Italia",
            "discipline": "Platform redesign",
            "duration": "26 settimane",
            "year": "2024",
            "standfirst":
                "Un nuovo cruscotto residenziale per 2.8M clienti. "
                "Gestione servizi, pagamenti, auto-care, SSO. "
                "Risultato: −34% chiamate al call center, NPS 64 post-launch, "
                "migrazione completa in sei mesi senza downtime.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Un cruscotto del 2014 in un mondo del 2024.",
            "problem_paragraphs": [
                "La dashboard residenziale di Fastweb era stata costruita nel 2014 "
                "e ri-skin-nata tre volte senza toccare la struttura. Il risultato: "
                "task completion al 41%, 2.1M chiamate al call center all'anno per "
                "operazioni che avrebbero dovuto essere self-care.",
                "L'obiettivo: ricostruire senza perdere utenti, senza downtime, "
                "e senza un big-bang launch — abbiamo avuto 26 settimane.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Micro-frontend + migrazione progressiva.",
            "solution_paragraphs": [
                "Abbiamo costruito il nuovo cruscotto come <em>micro-frontend</em> "
                "accanto al vecchio — stesso dominio, stesso SSO, stesso backend. "
                "Gli utenti sono stati migrati per cluster geografico (Lombardia, "
                "Piemonte, Lazio...) in sei fasi.",
                "Ogni cluster veniva monitorato per 2 settimane. Se NPS e task "
                "completion migliori del vecchio, si procedeva al cluster successivo. "
                "Se peggiori, si tornava indietro di 24 ore e si fixava.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "<em>Sei fasi</em> di rollout geografico.",
            "timeline_intro":
                "Ogni fase del rollout aveva 2 settimane di monitoraggio prima "
                "della fase successiva. La più difficile è stata la terza.",
            "timeline_steps": [
                {"id": "R.01", "duration": "Settimana 10", "title": "Piemonte", "body": "400k utenti. NPS +18. Go."},
                {"id": "R.02", "duration": "Settimana 14", "title": "Lombardia",    "body": "680k utenti. NPS +22. Go."},
                {"id": "R.03", "duration": "Settimana 18", "title": "Veneto",       "body": "480k utenti. NPS +9. Hold 1 sett."},
                {"id": "R.04", "duration": "Settimana 22", "title": "Lazio",        "body": "520k utenti. NPS +21. Go."},
                {"id": "R.05", "duration": "Settimana 26", "title": "Resto Italia", "body": "720k utenti. NPS +19. Complete."},
            ],

            "results_label": "// results",
            "results_heading": "Sei mesi, <em>quattro numeri</em>.",
            "results_stats": [
                ("<em>−34%</em>",      "chiamate call center", "~720k chiamate in meno / anno"),
                ("<em>NPS 64</em>",    "post-launch",           "vs 32 pre-launch"),
                ("<em>2.8M</em>",      "utenti migrati",        "100% senza downtime"),
                ("<em>+41% TC</em>",   "task completion",        "da 41% a 82%"),
            ],

            "quote": "Aura è l'unico studio che mi ha presentato un piano di rollback per ogni singolo sprint. Abbiamo usato il rollback due volte. Zero drama.",
            "quote_author": "Stefano Petri",
            "quote_role":   "Head of digital · Fastweb",

            "next_label":   "// next case",
            "next_heading": "→ vedi tutti i <em>lavori</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ prenota una <em>call</em>",
        },
        {
            "slug": "soldo-corporate-onboarding",
            "id":   "P.03 · FINTECH",
            "title": "Soldo · onboarding da <em>4 giorni</em> a <em>42 minuti</em>.",
            "client": "Soldo · Fintech pan-EU",
            "discipline": "Product launch · onboarding",
            "duration": "18 settimane",
            "year": "2025",
            "standfirst":
                "Il ridisegno completo dell'onboarding corporate di Soldo. "
                "Da processo assistito (4 giorni) a self-serve completo "
                "(42 minuti) in 7 mercati europei, con KYC, multi-currency "
                "e compliance. Risultato: +41% activation, −54% time to value.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1559028012-481c04fa702d?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Un onboarding che richiedeva un umano.",
            "problem_paragraphs": [
                "L'onboarding Soldo nel 2024 richiedeva 4 giorni mediani "
                "(2 per KYC, 1 per setup multi-currency, 1 per attivazione "
                "carte). Ogni onboarding consumava 1.2 ore di customer success. "
                "Su 2.800 onboarding/mese, il costo era insostenibile.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Onboarding guidato, zero umano.",
            "solution_paragraphs": [
                "Abbiamo ridisegnato l'intero flusso come <em>self-serve guided</em>: "
                "il cliente carica i documenti una volta sola, il KYC gira in background, "
                "la configurazione multi-currency è pre-compilata sul mercato di residenza.",
                "Umano solo su richiesta esplicita (link in ogni step). "
                "CSAT non è calato — è salito del 22%.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "Nove <em>sprint</em>, sette mercati.",
            "timeline_intro":
                "I primi 4 sprint su UK (mercato più maturo). "
                "Gli altri 5 su rollout cross-market.",
            "timeline_steps": [
                {"id": "S.01", "duration": "sett. 1-2",  "title": "<em>Discovery</em>",       "body": "120 customer success calls analizzate."},
                {"id": "S.02", "duration": "sett. 3-6",  "title": "<em>UK beta</em>",         "body": "Nuovo flow live su UK. +28% activation."},
                {"id": "S.03", "duration": "sett. 7-10", "title": "<em>DE · NL · FR</em>", "body": "3 mercati aggiunti. Fix multi-currency."},
                {"id": "S.04", "duration": "sett. 11-14","title": "<em>IT · ES · IE</em>", "body": "3 mercati aggiunti. Fix lingua."},
                {"id": "S.05", "duration": "sett. 15-18","title": "<em>Scale</em>",           "body": "Ottimizzazione continua. A/B weekly."},
            ],

            "results_label": "// results",
            "results_heading": "Tre <em>metriche core</em> mosse.",
            "results_stats": [
                ("<em>42 min.</em>",    "time to activate",   "da 4 giorni mediani"),
                ("<em>+41%</em>",       "activation rate",     "trial → paid"),
                ("<em>+22%</em>",       "CSAT",                "post-onboarding"),
                ("<em>7</em>",          "mercati",             "day one go-live"),
            ],

            "quote": "Il risultato è che oggi il nostro team di onboarding corporate è il 60% più piccolo ma gestisce 3x le aziende. Soldo non sarebbe al livello attuale senza questo rework.",
            "quote_author": "Rebecca Hughes",
            "quote_role":   "VP Growth · Soldo",

            "next_label":   "// next case",
            "next_heading": "→ vedi tutti i <em>lavori</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ prenota una <em>call</em>",
        },
        {
            "slug": "milkman-ship-sdk",
            "id":   "P.04 · LOGISTICS",
            "title": "Milkman · <em>SDK tracking</em> per 40+ retailer.",
            "client": "Milkman · Logistics Italia",
            "discipline": "B2B delivery · SDK",
            "duration": "22 settimane",
            "year": "2024",
            "standfirst":
                "Un SDK JavaScript white-label per tracking consegne, "
                "integrato nel checkout di 40+ retailer italiani. "
                "Una sola chiamata API, branding retailer-side, "
                "aggiornamenti real-time. Bundle sotto i 2MB gzipped.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "40 retailer, 40 integrazioni custom.",
            "problem_paragraphs": [
                "Milkman gestiva le consegne di oltre 40 retailer italiani — "
                "Esselunga, Coop, Unieuro, Mediaworld — ciascuno con la propria "
                "integrazione custom. Ogni nuovo retailer richiedeva 8-12 "
                "settimane di engineering.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Un SDK, una chiamata API.",
            "solution_paragraphs": [
                "Abbiamo costruito un SDK JavaScript white-label. "
                "Un retailer deve fare una sola cosa: chiamare <em>milkman.track(orderId)</em>. "
                "L'SDK gestisce il branding retailer-side (colori, font, logo), "
                "le lingue, gli aggiornamenti real-time via WebSocket.",
                "Integrazione media: 3 ore. Prima: 8-12 settimane.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "<em>Cinque</em> sprint dall'SDK al 40° retailer.",
            "timeline_intro": "Primo retailer (Esselunga) in sprint 3. Gli altri 39 in autoservizio.",
            "timeline_steps": [
                {"id": "S.01", "duration": "sett. 1-4",   "title": "<em>SDK core</em>",         "body": "Architettura, bundle, branding."},
                {"id": "S.02", "duration": "sett. 5-10",  "title": "<em>Esselunga beta</em>",   "body": "Primo retailer live. 2 bug critici."},
                {"id": "S.03", "duration": "sett. 11-14", "title": "<em>Unieuro · Coop</em>",   "body": "2 retailer aggiunti. Zero bug."},
                {"id": "S.04", "duration": "sett. 15-18", "title": "<em>Docs + portal</em>",    "body": "Self-serve onboarding."},
                {"id": "S.05", "duration": "sett. 19-22", "title": "<em>Scale</em>",            "body": "40° retailer integrato in autoservizio."},
            ],

            "results_label": "// results",
            "results_heading": "Da <em>8 settimane</em> a <em>3 ore</em>.",
            "results_stats": [
                ("<em>40+</em>",        "retailer live",          "Al go-live del sesto mese"),
                ("<em>3 ore</em>",      "time-to-integrate",      "Da 8-12 settimane mediane"),
                ("<em>1.8 MB</em>",     "bundle gzipped",         "Sotto il tetto di 2 MB richiesto"),
                ("<em>0</em>",          "downtime",               "Dal primo sprint a oggi"),
            ],

            "quote": "L'SDK ci ha permesso di aprire tre mercati europei in sei mesi. Prima sarebbe stato impossibile.",
            "quote_author": "Antonio Perini",
            "quote_role":   "CEO · Milkman",

            "next_label":   "// next case",
            "next_heading": "→ vedi tutti i <em>lavori</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ prenota una <em>call</em>",
        },
        {
            "slug": "lendlease-asset-portal",
            "id":   "P.05 · PROPTECH",
            "title": "Lendlease · <em>portale enterprise</em> per 80 asset manager.",
            "client": "Lendlease · Proptech EU",
            "discipline": "B2B delivery",
            "duration": "30 settimane",
            "year": "2024",
            "standfirst":
                "Un portale enterprise per 80 asset manager italiani. "
                "SSO Azure, ruoli granulari, data warehouse integrato, "
                "compliance MiFID II. Non è sexy — è dove si gioca il rinnovo.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1600&q=80&auto=format&fit=crop",

            "problem_label":"// problem",
            "problem_heading":"Un portale enterprise con zero self-serve.",
            "problem_paragraphs":[
                "80 asset manager usavano un portale del 2016 che richiedeva "
                "assistenza umana per ogni azione. Ogni asset manager consumava "
                "~6 ore / settimana di customer success. Ri-contracting trimestrale "
                "a rischio.",
            ],
            "solution_label":"// solution",
            "solution_heading":"Dashboard self-serve + export automatizzato.",
            "solution_paragraphs":[
                "Abbiamo ricostruito il portale come piattaforma self-serve. "
                "SSO Azure, ruoli granulari (analista, manager, compliance), "
                "data warehouse integrato con export multi-formato "
                "(PDF, XLSX, CSV, MiFID II XML).",
            ],
            "timeline_label":"// timeline",
            "timeline_heading":"<em>Dieci</em> sprint, <em>tre</em> rollout cluster.",
            "timeline_intro": "Rollout per cluster di asset manager (20/30/30).",
            "timeline_steps":[
                {"id":"S.01","duration":"sett. 1-4","title":"<em>Discovery</em>","body":"Interviste a 12 asset manager."},
                {"id":"S.02","duration":"sett. 5-14","title":"<em>SSO + ruoli</em>","body":"Azure SSO + RBAC completo."},
                {"id":"S.03","duration":"sett. 15-22","title":"<em>Dashboard</em>","body":"Core dashboard + analytics."},
                {"id":"S.04","duration":"sett. 23-28","title":"<em>Export</em>","body":"Multi-formato + MiFID II."},
                {"id":"S.05","duration":"sett. 29-30","title":"<em>Rollout</em>","body":"80 asset manager migrati."},
            ],
            "results_label":"// results",
            "results_heading":"<em>80</em> asset manager, <em>zero</em> chiamate.",
            "results_stats":[
                ("<em>80</em>","asset manager migrati","100% entro fine rollout"),
                ("<em>−92%</em>","chiamate CS","6 ore → 28 min /sett."),
                ("<em>100%</em>","ricontracting","Per 2 anni consecutivi"),
                ("<em>MiFID II</em>","compliance","Audit superato al primo giro"),
            ],
            "quote":"Il portale è diventato il motivo principale per cui i nostri asset manager rinnovano.",
            "quote_author":"Valentina Greco",
            "quote_role":"Head of product · Lendlease IT",
            "next_label":"// next case",
            "next_heading":"→ vedi tutti i <em>lavori</em>",
            "cta_label":"// start a project",
            "cta_heading":"→ prenota una <em>call</em>",
        },
        {
            "slug": "fiscozen-onboarding-self-serve",
            "id":   "P.06 · FISCTECH",
            "title": "Fiscozen · <em>+47%</em> da trial a paid.",
            "client": "Fiscozen · Fisctech Milano",
            "discipline": "Growth systems",
            "duration": "16 settimane",
            "year": "2024",
            "standfirst":
                "Da onboarding assistito da commercialista a self-serve completo "
                "per partite IVA. +47% conversione trial → paid in 90 giorni.",
            "meta_client_label":"// client",
            "meta_discipline_label":"// capability",
            "meta_duration_label":"// duration",
            "meta_year_label":"// delivered",
            "cover_image": "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=1600&q=80&auto=format&fit=crop",
            "problem_label":"// problem",
            "problem_heading":"Onboarding che richiedeva un commercialista.",
            "problem_paragraphs":["Ogni partita IVA in prova aveva bisogno di 30 min con un commercialista per iniziare. Bottleneck critico."],
            "solution_label":"// solution",
            "solution_heading":"Guided onboarding self-serve, commercialista opzionale.",
            "solution_paragraphs":["Form guidato che pre-compila ATECO in base al racconto libero dell'utente, integrato con InfoCamere."],
            "timeline_label":"// timeline",
            "timeline_heading":"<em>Otto</em> sprint, KPI settimanale.",
            "timeline_intro":"Priorità: time-to-first-value sotto i 20 minuti.",
            "timeline_steps":[
                {"id":"S.01","duration":"sett. 1-3","title":"<em>Research</em>","body":"20 interviste partite IVA prime."},
                {"id":"S.02","duration":"sett. 4-8","title":"<em>Flow v1</em>","body":"Primo onboarding self-serve. 28% attivazione."},
                {"id":"S.03","duration":"sett. 9-12","title":"<em>Iterate</em>","body":"4 A/B test. 41% attivazione."},
                {"id":"S.04","duration":"sett. 13-16","title":"<em>Scale</em>","body":"Rollout 100%. 47% post-90gg."},
            ],
            "results_label":"// results",
            "results_heading":"<em>Quattro</em> mesi, <em>tre</em> metriche.",
            "results_stats":[
                ("<em>+47%</em>","trial → paid","da 21% a 31% conv. a 90 gg"),
                ("<em>18 min.</em>","TTFV","da 4 ore con commercialista"),
                ("<em>−38%</em>","CAC","customer acquisition cost"),
                ("<em>+2.1x</em>","volume","trial settimanali post-rollout"),
            ],
            "quote":"Il team di Aura ha shippato più A/B test in 16 settimane di quanti ne abbiamo fatti nei 2 anni precedenti.",
            "quote_author":"Vittorio Amato",
            "quote_role":"CEO · Fiscozen",
            "next_label":"// next case",
            "next_heading":"→ vedi tutti i <em>lavori</em>",
            "cta_label":"// start a project",
            "cta_heading":"→ prenota una <em>call</em>",
        },
    ],
}
