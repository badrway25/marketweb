"""Elevate — Startup SaaS Landing Kit (business / startup-saas-landing).

Phase 2g3.3 — Business live rollout (Session 32, 2026-04-13).

Editorial identity: a productized GTM landing kit for early-stage SaaS
startups. The "company" sells the kit itself (a meta-product). Voice is
energetic, product-oriented, growth-tech vocabulary (waitlist, MRR, A/B,
ship log, deploy, trial). NO Lei register — `tu` from line one. Photo
direction is product UI dashboards, code editors, bright tech offices —
never boardroom, never consulting.

Differentiation vs Pragma (10-gate D-054 — recorded for reviewers, mirror
of the comment block in template_content_pragma.py):
 1. Hero image:        no big photo — typographic + product mockup card
                       vs Pragma boardroom 55/45 split
 2. First-2 imagery:   product UI dashboards (business-startup pool)
                       vs Pragma boardroom + corporate atrium
 3. Silhouette:        centered manifesto + glow CTA + floating mockup
                       vs Pragma 55/45 editorial-serif + KPI strip
 4. Section order:     banner → manifesto → mockup → metrics → integrations → pricing → shiplog
                       vs Pragma hero → pillars → kpi → sectors → leadership → cases
 5. Primary CTA:       "Inizia gratis" + glow pill + 14-day trial
                       vs Pragma "Fissa una call privata" + private form
 6. Block rhythm:      medium-density glow cards + dark sections
                       vs Pragma airy editorial chapters + cream paper
 7. Macro tone:        dark cosmic gradient + cyan neon glow
                       vs Pragma cream paper + navy + gold
 8. Imagery direction: product UI + tech offices + dashboards
                       vs Pragma boardroom + corporate facilities
 9. Typography:        Manrope (geometric sans) + Inter
                       vs Pragma Merriweather (transitional serif) + Inter
10. Inner pages:       pricing + ship log + integrations + demo lead form
                       vs Pragma case studies + advisory pillars + 5-office presence

Page kinds:
- home, about, product, pricing, demo, contact
"""
from __future__ import annotations

from typing import Any


ELEVATE_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Home",        "kind": "home"},
        {"slug": "prodotto",   "label": "Prodotto",    "kind": "product"},
        {"slug": "prezzi",     "label": "Prezzi",      "kind": "pricing"},
        {"slug": "demo",       "label": "Demo",        "kind": "demo"},
        {"slug": "contatti",   "label": "Contatti",    "kind": "contact"},
    ],

    # Site-wide chrome
    "site": {
        "logo_initial": "E",
        "logo_word":    "Elevate",
        "tag":          "Conversion-first kit · per founder che spediscono",
        "phone":        "hello@elevatekit.io",
        "email":        "hello@elevatekit.io",
        "address":      "Talent Garden Calabiana · Milano",
        "hours_compact":"Async-first · Slack 9-19 CET",
        "hours_footer_rows": [
            "Demo on-demand · ogni martedì 17:00 CET",
            "Office hours founder · venerdì 11:00 CET",
        ],
        "license":      "",
        "footer_intro":
            "Elevate è il GTM kit che porta la tua startup dalla "
            "waitlist al primo MRR in quattordici giorni. Built for founders, "
            "by founders. Spedito da Milano, deployato ovunque.",
        "foot_studio":   "Il prodotto",
        "foot_pages":    "Naviga",
        "foot_contact":  "Parla con noi",
        "foot_offices":  "Ship log",
        # Footer tertiary column — last 3 ship-log entries (different per Pragma)
        "shiplog_footer_rows": [
            "v2.9 · venerdì · drag-and-drop hero builder",
            "v2.8 · ieri · libreria testimonial premium",
            "v2.7 · martedì · A/B test integrato GrowthBook",
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        # Top launch banner above the floating pill nav
        "banner_label":   "Serie A · Q2 2026",
        "banner_text":    "Stiamo chiudendo i primi cinquanta posti early-access",
        "banner_href":    "demo",

        "eyebrow":     "Conversion-first GTM kit · per SaaS & startup early-stage",
        "headline":    "Dalla <em>waitlist</em> al primo <em>MRR</em> in quattordici giorni.",
        "intro":
            "Elevate è il kit di landing, pricing e onboarding che trasforma "
            "i primi visitatori in utenti paganti. A/B test integrato, "
            "checkout Stripe one-click, copy kit italiano, deploy su "
            "Vercel in trenta secondi.",
        "primary_cta":   "Inizia gratis · 14 giorni",
        "primary_href":  "demo",
        "secondary_cta": "Guarda la demo · 2 min",
        "secondary_href":"prodotto",

        "trust_label":   "Adottato da 240+ startup italiane in early-stage",
        "trust_logos":   ["FLUX", "NOVA/", "QUANTA", "HELIX", "RIFT.", "CASP", "ARC", "LOOM"],

        # Product mockup card — overlaps the hero / sits below it
        "mockup": {
            "chrome_label":     "elevate.app / dashboard / onboarding-flow",
            "chrome_dots":      ["●", "●", "●"],
            "badge":            "Live A/B",
            "metric_primary":   "↑ 38%",
            "metric_label":     "Conversione CTA primaria",
            "metric_desc":      "vs. variante B (control)",
            "secondary_metric": "+ € 12.4K",
            "secondary_label":  "MRR ultimi 30 giorni",
            "secondary_desc":   "trial-to-paid conversion: 22%",
            "feature_label":    "Plan Launch · € 29 / mese",
            "perks":            ["Hosting + CDN inclusi", "CLI deploy · zero config", "Supporto Slack diretto"],
        },

        # Feature pills under the hero
        "feature_pills":  ["Stripe + Linear", "A/B test integrato", "Edge analytics", "Copy kit IT", "Deploy in 30s"],

        # Capabilities — 6 cards in a 3x2 grid
        "features_label":   "Cosa c'è dentro",
        "features_heading": "Sei moduli, <em>una sola installazione</em>.",
        "features_intro":
            "Tutti i pezzi che servono per andare live e iniziare a "
            "monetizzare — già integrati, già testati, già documentati.",
        "features": [
            {
                "icon": "→",
                "title": "Hero builder drag-and-drop",
                "desc":
                    "Dieci layout hero pre-testati su 1.200 startup. "
                    "A/B test fra varianti senza scrivere una riga di codice.",
            },
            {
                "icon": "$",
                "title": "Pricing table & Stripe",
                "desc":
                    "Tre tier configurabili, conversione checkout one-click, "
                    "subscription management out-of-the-box. Webhook Stripe "
                    "già cablati su Linear e Slack.",
            },
            {
                "icon": "▲",
                "title": "Edge analytics",
                "desc":
                    "Web vitals, funnel di conversione, attribution multi-touch — "
                    "raccolti edge-side, zero impatto sul TTI. Privacy-first, "
                    "cookieless, GDPR-clean.",
            },
            {
                "icon": "✱",
                "title": "Onboarding flow",
                "desc":
                    "Checklist guidata multi-step, progress bar, email "
                    "trigger su milestone. Time-to-value medio 4 minuti "
                    "vs il benchmark di settore di 18.",
            },
            {
                "icon": "◐",
                "title": "Copy kit italiano",
                "desc":
                    "Sessanta blocchi di copy testati sui mercati IT/EN/FR — "
                    "headline, sub, CTA, microcopy onboarding, error states. "
                    "Pronti da modificare in markdown.",
            },
            {
                "icon": "↗",
                "title": "Deploy CLI",
                "desc":
                    "elevate deploy → Vercel / Netlify / Cloudflare in "
                    "trenta secondi. Branch preview automatici, rollback "
                    "in un comando, environment variables sincronizzate.",
            },
        ],

        # Product demo video block — cosmic glass frame between mockup and trust
        # NOTE: the demo `src` below is a CC-licensed Big Buck Bunny sample hosted
        # on Google's public test bucket. Functional placeholder so the live preview
        # demonstrates the lm-video integration end-to-end (poster + click-to-play
        # native HTML5 player). Replace with a real product walkthrough mp4 in
        # production. Poster is an editorial code/dashboard still that fits the
        # cosmic skin without needing to ship the actual video assets.
        "product_video": {
            "label":      "Tour del prodotto",
            "heading":    "Vedi <em>Elevate</em> in azione, due minuti.",
            "intro":
                "Una panoramica registrata sul progetto reale: editor drag-and-drop, "
                "wizard di pricing, cablaggio Stripe + Linear, deploy su Vercel. "
                "Senza demo programmate, senza commerciali, senza email di follow-up.",
            "poster":     "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1800&q=80&auto=format&fit=crop",
            "src":        "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
            "play_label": "Guarda · 2 min",
            "caption":    "Demo · 2:14 · 1080p",
        },

        # Metric strip on dark band
        "metric_label":   "I numeri del kit in produzione",
        "metric_heading": "Lo stack che spedisce",
        "metric_strip": [
            ("3.1 ×",  "conversione landing media"),
            ("14 gg",  "dal deploy al primo utente pagante"),
            ("99.98%", "uptime infrastruttura"),
            ("4 min",  "time-to-value mediano"),
        ],

        # Integrations row
        "integrations_label":   "Integrazioni out-of-the-box",
        "integrations_heading": "Già cablato con lo stack che usi",
        "integrations": [
            ("Stripe",     "Subscription · Checkout · Tax"),
            ("Linear",     "Issue tracking · changelog auto"),
            ("Slack",      "Notifiche · alert MRR"),
            ("Vercel",     "Deploy · preview · rollback"),
            ("PostHog",    "Funnel · session replay"),
            ("GrowthBook", "A/B test · feature flags"),
            ("Loops",      "Email transazionali"),
            ("Cal.com",    "Demo booking auto"),
        ],

        # Pricing teaser — cliccabile verso /prezzi
        "pricing_teaser_label":   "Prezzi trasparenti",
        "pricing_teaser_heading": "Tre piani, nessun setup fee.",
        "pricing_teaser_intro":
            "Annullamento a un click, fatturazione mensile o annuale, "
            "trial di quattordici giorni senza carta di credito.",
        "pricing_teaser": [
            {"name": "Launch",  "price": "€ 29",  "period": "/ mese", "tag": "Per founder solitari",
             "highlight": False, "perks": ["Tutti i moduli", "Hosting + CDN", "Email Slack"]},
            {"name": "Scale",   "price": "€ 79",  "period": "/ mese", "tag": "Più scelto",
             "highlight": True, "perks": ["Tutto Launch +", "A/B avanzato", "5 progetti"]},
            {"name": "Studio",  "price": "€ 199", "period": "/ mese", "tag": "Per studi & agenzie",
             "highlight": False, "perks": ["Tutto Scale +", "Progetti illimitati", "White-label"]},
        ],
        "pricing_teaser_cta":      "Confronta i piani in dettaglio",
        "pricing_teaser_cta_href": "prezzi",

        # Founder proof — 2 founder quotes
        "founders_label":   "Founder che hanno spedito con Elevate",
        "founders_heading": "La parola passa a chi <em>spedisce davvero</em>.",
        "founders": [
            {
                "name":  "Anna Vecchietti",
                "role":  "Founder · Quanta Analytics",
                "quote":
                    "Avevo provato tre boilerplate e due costruttori no-code. "
                    "Con Elevate sono andata live in due weekend, primo MRR "
                    "diciassette giorni dopo il deploy. La differenza è il "
                    "copy kit italiano — non dover riscrivere ogni headline.",
                "metric_primary": "+ € 4.2K",
                "metric_label":   "MRR primi 60 giorni",
            },
            {
                "name":  "Davide Zonca",
                "role":  "CTO · Helix Workflows",
                "quote":
                    "Lo stack che mi serviva senza i sette giorni di setup. "
                    "Stripe, GrowthBook, Linear già cablati significa che "
                    "abbiamo speso il primo mese a parlare con utenti, non "
                    "a configurare webhook.",
                "metric_primary": "× 3.4",
                "metric_label":   "Conversione vs landing precedente",
            },
        ],

        # Ship log — what shipped recently (transparency block)
        "shiplog_label":   "Ship log live",
        "shiplog_heading": "Cosa abbiamo spedito di recente",
        "shiplog_intro":
            "Elevate è in continuous deploy. Ogni feature spedita compare "
            "qui in tempo reale — niente roadmap teoriche, niente stagioni "
            "del prodotto. Quello che vedi è quello che usi domani.",
        "shiplog": [
            {"version": "v2.9", "date": "Venerdì",  "title": "Hero builder drag-and-drop",
             "desc": "Dieci layout pre-testati, A/B fra varianti integrato, preview live."},
            {"version": "v2.8", "date": "Ieri",     "title": "Libreria testimonial premium",
             "desc": "Quattro layout (carousel, masonry, single-feature, video-first) con animazioni reveal."},
            {"version": "v2.7", "date": "Martedì",  "title": "A/B test integrato GrowthBook",
             "desc": "Wizard di setup esperimento in 4 step, hypothesis tracker, statistical significance auto."},
            {"version": "v2.6", "date": "Lunedì",   "title": "Stripe Checkout one-click",
             "desc": "Adattatori per i 4 maggiori payment provider EU, gestione VAT automatica."},
            {"version": "v2.5", "date": "Settimana scorsa", "title": "Edge analytics privacy-first",
             "desc": "Cookieless tracking, sotto i 4KB sul TTI, dashboard funnel inclusa."},
        ],
        "shiplog_cta":      "Iscriviti al ship log via Slack",
        "shiplog_cta_href": "demo",
        "shiplog_release_label": "Prossima release",
        "shiplog_release_value": "v3.0 · primo lunedì del mese",
        "shiplog_release_chip":  "RC live",

        # Final CTA band before footer — glow ring
        "cta_label":     "Inizia ora",
        "cta_heading":   "Quattordici giorni gratis. Quaranta minuti per andare live.",
        "cta_intro":
            "Niente carta di credito per attivare il trial. Slack diretto "
            "con il founding team. Se non spedisci entro due settimane, "
            "ti rimandiamo i soldi. Promessa scritta.",
        "cta_primary":   "Attiva il trial",
        "cta_primary_href": "demo",
        "cta_secondary": "Vedi il piano completo",
        "cta_secondary_href": "prezzi",
    },

    # ─── PRODOTTO (product tour) ────────────────────────────────
    "prodotto": {
        "eyebrow":   "Product tour · v2.9 (aprile 2026)",
        "headline":  "Tutto quello che <em>devi spedire</em> per andare live.",
        "intro":
            "Sei moduli core + dodici integrazioni out-of-the-box. "
            "Niente plugin da configurare, niente boilerplate da forkare, "
            "niente Twitter thread da seguire per fare quello che dovrebbe "
            "essere ovvio. Apri, modifica, deploy.",

        # Product modules — same 6 from home but expanded with detail
        "modules_label":   "Moduli core",
        "modules_heading": "Sei pezzi, una sola installazione",
        "modules": [
            {
                "num":   "01",
                "title": "Hero builder drag-and-drop",
                "blurb":
                    "Dieci layout hero pre-testati su 1.200 startup early-stage. "
                    "Ogni layout viene fornito con tre varianti di copy "
                    "(B2B, B2C, dev-tool) e con A/B test integrato.",
                "highlights": [
                    "10 layout · 30 varianti copy",
                    "A/B fra varianti senza codice",
                    "Headline, sub, CTA, badge sociale tutti editabili",
                    "Mobile + desktop ottimizzati separatamente",
                ],
            },
            {
                "num":   "02",
                "title": "Pricing table & Stripe Checkout",
                "blurb":
                    "Tre tier configurabili con highlight automatico sul "
                    "piano centrale. Subscription management Stripe, "
                    "checkout one-click su mobile, gestione VAT EU automatica.",
                "highlights": [
                    "1, 2, 3 o 4 tier · highlight a piacere",
                    "Toggle mensile / annuale built-in",
                    "Stripe Tax su 38 paesi EU",
                    "Webhook Stripe → Slack già cablati",
                ],
            },
            {
                "num":   "03",
                "title": "Edge analytics privacy-first",
                "blurb":
                    "Web vitals, funnel multi-step, attribution multi-touch — "
                    "tutto raccolto edge-side via Cloudflare Worker. "
                    "Cookieless, GDPR-clean, sotto i 4KB sul TTI.",
                "highlights": [
                    "Cookieless · GDPR · ePrivacy clean",
                    "Web Vitals · LCP · FID · CLS in dashboard",
                    "Funnel di conversione visuale",
                    "PostHog connector opzionale",
                ],
            },
            {
                "num":   "04",
                "title": "Onboarding flow guidato",
                "blurb":
                    "Checklist multi-step con progress bar, milestone "
                    "celebration, email trigger automatici. Time-to-value "
                    "mediano 4 minuti vs il benchmark di settore di 18.",
                "highlights": [
                    "Checklist drag-and-drop personalizzabile",
                    "Email trigger su Loops · Resend · Postmark",
                    "Achievement badge built-in",
                    "Re-engagement automatico dopo 48h",
                ],
            },
            {
                "num":   "05",
                "title": "Copy kit italiano (e EN/FR)",
                "blurb":
                    "Sessanta blocchi di copy editoriale testati sui "
                    "mercati IT/EN/FR. Headline, sub, CTA, microcopy "
                    "onboarding, error states, empty states.",
                "highlights": [
                    "60 blocchi · IT + EN + FR",
                    "Tone-of-voice configurabile",
                    "Markdown editing diretto",
                    "Snippet library con search semantica",
                ],
            },
            {
                "num":   "06",
                "title": "Deploy CLI · trenta secondi",
                "blurb":
                    "elevate deploy. Trenta secondi al primo deploy live, "
                    "branch preview automatici su PR, rollback in un comando, "
                    "environment variables sincronizzate fra dev / staging / prod.",
                "highlights": [
                    "Vercel · Netlify · Cloudflare adapter",
                    "Branch preview automatici su PR",
                    "Rollback istantaneo · zero downtime",
                    "Env-var sync · dev / staging / prod",
                ],
            },
        ],

        # Integrations grid — bigger version of home
        "integrations_label":   "Integrazioni out-of-the-box",
        "integrations_heading": "Lo stack che ti serve, già cablato.",
        "integrations_intro":
            "Dodici integrazioni native, zero plugin da installare. "
            "Quelle che non vedi qui le aggiungiamo se ce le chiedi su Slack.",
        "integrations_full": [
            {"name": "Stripe",     "category": "Pagamenti",  "desc": "Subscription · Checkout · Tax · Connect"},
            {"name": "Linear",     "category": "Tracking",   "desc": "Issue · Cycles · changelog auto-pubblicato"},
            {"name": "Slack",      "category": "Comms",      "desc": "Notifiche · alert MRR · daily digest"},
            {"name": "Vercel",     "category": "Deploy",     "desc": "Production deploy · preview branch · rollback"},
            {"name": "Netlify",    "category": "Deploy",     "desc": "Edge functions · build hooks · analytics sync"},
            {"name": "Cloudflare", "category": "Deploy",     "desc": "Workers · KV · D1 · R2 storage"},
            {"name": "PostHog",    "category": "Analytics",  "desc": "Funnel · session replay · feature flag"},
            {"name": "GrowthBook", "category": "Esperimenti","desc": "A/B test · hypothesis tracker · stat-sig auto"},
            {"name": "Loops",      "category": "Email",      "desc": "Transazionali · onboarding sequences"},
            {"name": "Resend",     "category": "Email",      "desc": "Transazionali · React Email templates"},
            {"name": "Cal.com",    "category": "Booking",    "desc": "Demo booking · routing · webhook"},
            {"name": "Plain",      "category": "Support",    "desc": "Support inbox · CRM con AI triage"},
        ],

        # Architecture — what runs where
        "stack_label":   "Architecture",
        "stack_heading": "Cosa gira dove (e perché)",
        "stack_intro":
            "Trasparenza tecnica — niente magia, niente lock-in nascosto. "
            "Lo stack è documentato apertamente, e l'intero codice è esportabile "
            "da un click se decidi di andartene.",
        "stack": [
            ("Frontend",    "Next.js 15 · React 19 · App Router · Server Actions"),
            ("Edge",        "Cloudflare Workers + KV per analytics e A/B"),
            ("Database",    "PostgreSQL · Prisma · Neon serverless"),
            ("Auth",        "Clerk · OAuth · passkey · magic link"),
            ("Pagamenti",   "Stripe Subscriptions + Stripe Tax + Stripe Connect"),
            ("Email",       "Loops o Resend a scelta · React Email templates"),
            ("Analytics",   "PostHog opzionale · edge analytics nativo"),
            ("Esperimenti", "GrowthBook · self-hosted o cloud"),
        ],

        "cta_heading":   "Pronto a vederlo girare?",
        "cta_intro":
            "Demo dal vivo con un founding member ogni martedì alle 17:00 CET. "
            "Mezz'ora di chiamata, screen-share, domande tecniche benvenute.",
        "cta_primary":   "Prenota la demo",
        "cta_primary_href": "demo",
        "cta_secondary": "Vedi i piani",
        "cta_secondary_href": "prezzi",
    },

    # ─── PREZZI (pricing) ───────────────────────────────────────
    "prezzi": {
        "eyebrow":  "Prezzi trasparenti · 2026",
        "headline": "Annulli a un click. <em>Sempre</em>.",
        "intro":
            "Tre piani, nessun setup fee, fatturazione mensile o annuale "
            "(due mensilità in regalo sull'annuale). Quattordici giorni "
            "di trial gratuito, senza carta di credito.",

        # Toggle row UI cue
        "billing_toggle_label": "Fatturazione",
        "billing_toggle_options": [
            ("monthly", "Mensile"),
            ("annual",  "Annuale · –17%"),
        ],

        # Three pricing tiers
        "tiers": [
            {
                "name":     "Launch",
                "tag":      "Per founder solitari",
                "price":    "€ 29",
                "annual":   "€ 24",
                "period":   "/ mese",
                "annual_period": "/ mese · pagato annualmente",
                "highlight": False,
                "blurb":
                    "Tutto il necessario per andare live con un solo prodotto. "
                    "Pensato per il founder solo o per la prima settimana di "
                    "founding team.",
                "cta":         "Inizia gratis",
                "cta_href":    "demo",
                "perks": [
                    ("✓", "Tutti i sei moduli core"),
                    ("✓", "Hosting + CDN globale inclusi"),
                    ("✓", "Deploy CLI · branch preview automatici"),
                    ("✓", "Edge analytics + funnel base"),
                    ("✓", "1 progetto · 1 dominio custom"),
                    ("✓", "Slack diretto con il founding team"),
                    ("○", "A/B test base (manuale)"),
                    ("○", "1 copy kit (IT o EN o FR)"),
                ],
            },
            {
                "name":     "Scale",
                "tag":      "Più scelto · per startup post-PMF",
                "price":    "€ 79",
                "annual":   "€ 65",
                "period":   "/ mese",
                "annual_period": "/ mese · pagato annualmente",
                "highlight": True,
                "blurb":
                    "Il piano per il founding team che ha trovato product/market "
                    "fit e sta scalando. Aggiunge A/B avanzato, multi-progetto, "
                    "white-glove onboarding.",
                "cta":         "Inizia gratis",
                "cta_href":    "demo",
                "perks": [
                    ("✓", "Tutto Launch +"),
                    ("✓", "A/B test avanzato (GrowthBook integrato)"),
                    ("✓", "5 progetti · domini custom illimitati"),
                    ("✓", "PostHog connector + session replay"),
                    ("✓", "Stripe Tax + Stripe Connect"),
                    ("✓", "Tutti e 3 i copy kit (IT + EN + FR)"),
                    ("✓", "Onboarding 1-1 con il founding team (60 min)"),
                    ("✓", "Slack canale dedicato · SLA 4h"),
                ],
            },
            {
                "name":     "Studio",
                "tag":      "Per studi, agenzie e venture builder",
                "price":    "€ 199",
                "annual":   "€ 165",
                "period":   "/ mese",
                "annual_period": "/ mese · pagato annualmente",
                "highlight": False,
                "blurb":
                    "Per agenzie, studi creativi e venture builder che spediscono "
                    "più landing per clienti diversi. Progetti illimitati e "
                    "white-label completo.",
                "cta":         "Parla con noi",
                "cta_href":    "contatti",
                "perks": [
                    ("✓", "Tutto Scale +"),
                    ("✓", "Progetti illimitati · branding white-label"),
                    ("✓", "Sub-account per ogni cliente"),
                    ("✓", "API completa · webhook custom"),
                    ("✓", "SLA 1h · supporto telefonico"),
                    ("✓", "Account manager dedicato"),
                    ("✓", "Quarterly review con il founding team"),
                    ("✓", "Audit trail · compliance SOC 2"),
                ],
            },
        ],

        # Comparison — what's NOT included
        "comparison_label":   "Cosa non c'è (e perché)",
        "comparison_heading": "La trasparenza che gli altri evitano",
        "comparison": [
            ("Setup fee",
             "Mai. Né su Launch, né su Scale, né su Studio. Se trovi un "
             "boilerplate concorrente che non ti chiede setup fee + ti dà "
             "lo stack già cablato, segnalacelo e ti rimborsiamo il primo mese."),
            ("Lock-in del codice",
             "Mai. Tutto il tuo codice è esportabile da CLI in un comando. "
             "Se decidi di lasciare Elevate, ti spostiamo il deploy su un "
             "Vercel di tua proprietà gratuitamente entro 24h."),
            ("Tariffe nascoste",
             "Mai. Quello che leggi è quello che paghi. La VAT EU è "
             "automaticamente calcolata e visualizzata in checkout — "
             "niente sorprese in fattura."),
            ("Limite di transazioni",
             "Mai. Stripe Connect non ha cap su transazioni o volume. "
             "Vendi 10 abbonamenti o 10.000 — il prezzo è lo stesso."),
        ],

        # FAQ accordion
        "faq_label":   "Domande frequenti",
        "faq_heading": "Quello che ci chiedono di più",
        "faq": [
            ("Posso provare prima di pagare?",
             "Sì, quattordici giorni di trial completo senza carta di credito. "
             "Hai accesso a tutti i moduli del piano Scale durante il trial — "
             "se decidi di restare, scegli il piano che fa per te. Se non "
             "decidi, il trial scade automaticamente, niente charge automatici."),
            ("Cosa succede se cancello?",
             "Cancelli da dashboard in un click, in qualunque momento. "
             "Il tuo deploy resta live fino alla fine del periodo già pagato. "
             "Ti esportiamo il codice in CLI e ti aiutiamo a migrare su un "
             "tuo Vercel/Netlify se vuoi continuare in autonomia."),
            ("Avete uno sconto per startup?",
             "Sì, il 50% sui primi sei mesi per startup pre-seed (raccolta "
             "<€500K) e il 30% sul primo anno per le post-seed. Scrivi a "
             "hello@elevatekit.io con il pitch deck per attivare la promozione."),
            ("Si integra col nostro stack esistente?",
             "Probabilmente sì. Le 12 integrazioni native coprono il 90% degli "
             "stack che vediamo, e l'API REST + webhook custom permettono "
             "di collegare quello che manca. Se ti serve un'integrazione "
             "che non c'è, scrivici su Slack — di solito la spediamo entro "
             "due settimane."),
            ("Posso ospitare in proprio?",
             "Sul piano Studio, sì — ti diamo il container Docker e lo "
             "schema Postgres da ospitare dove preferisci. Sui piani Launch "
             "e Scale, l'hosting è incluso e fa parte del valore del kit."),
            ("Le fatture sono in Italia?",
             "Sì, fatturiamo da Milano in EUR con partita IVA italiana, "
             "fatturazione elettronica SDI inclusa. Per i clienti UE non-IT "
             "la fattura è in reverse-charge VAT."),
        ],

        "cta_heading":   "Pronto a iniziare?",
        "cta_intro":
            "Quattordici giorni gratis. Niente carta di credito. "
            "Quaranta minuti per andare live con il tuo primo deploy.",
        "cta_primary":   "Attiva il trial",
        "cta_primary_href": "demo",
        "cta_secondary": "Domande? Scrivici",
        "cta_secondary_href": "contatti",
    },

    # ─── DEMO (lead form) ───────────────────────────────────────
    "demo": {
        "eyebrow":  "Demo dal vivo · martedì 17:00 CET",
        "headline": "Mezz'ora con un <em>founding member</em>.",
        "intro":
            "Demo dal vivo ogni martedì alle 17:00 CET. Trenta minuti di "
            "screen-share — mostriamo come si configura un tier pricing, "
            "come si lancia un A/B test, come si fa il primo deploy. "
            "Domande tecniche benvenute, pitch deck non richiesti.",

        # Form
        "form_label":   "Prenota uno slot",
        "form_heading": "Compila e ti confermiamo entro un'ora",
        "form_intro":
            "Lo slot del prossimo martedì è quello che riceverai per default. "
            "Se preferisci uno slot ad hoc, scegli 'Slot personalizzato' e "
            "ti scriviamo per fissarlo. Async-only? Va benissimo, vedi sotto.",
        "form_fields": [
            {"name": "name",     "label": "Nome",          "type": "text",  "required": True,  "placeholder": "Es. Anna",
             "helper": "Così ti salutiamo in demo."},
            {"name": "email",    "label": "Email",         "type": "email", "required": True,  "placeholder": "anna@startup.io",
             "helper": "Calendar invite + Loom finiscono qui."},
            {"name": "company",  "label": "Startup",       "type": "text",  "required": True,  "placeholder": "Es. Quanta Analytics",
             "helper": "Il nome che usi per commit e fatturazione."},
            {"name": "role",     "label": "Ruolo",         "type": "select","required": True,
             "options": ["Founder solo", "Co-founder · CEO", "Co-founder · CTO", "Co-founder · altro", "Hire 1-5", "Altro"],
             "helper": "Se sei da solo, \"Founder solo\" è la scelta giusta."},
            {"name": "stage",    "label": "Fase",          "type": "select","required": True,
             "options": ["Pre-idea / esplorando", "Pre-launch / waitlist", "Post-launch / cercando PMF", "Post-PMF / scaling"],
             "helper": "La demo si adatta: pre-launch vede onboarding + waitlist, post-PMF vede tier pricing + A/B."},
            {"name": "slot",     "label": "Slot preferito","type": "select","required": True,
             "options": ["Prossimo martedì 17:00 CET", "Slot personalizzato (ti scriviamo)", "Async — voglio un Loom registrato"],
             "helper": "Slot async = ricevi subito il Loom di 12 min per email."},
            {"name": "stack",    "label": "Stack attuale",
             "type": "text", "required": False,
             "placeholder": "Es. Next.js + Vercel + Stripe",
             "helper": "Facoltativo. Ci orientiamo subito sugli integration points giusti."},
            {"name": "context",  "label": "Cosa ti serve sapere?", "type": "textarea",
             "required": False, "full_width": True,
             "placeholder": "Domande specifiche, blocchi che vuoi vedere in demo, dubbi tecnici... (opzionale)",
             "helper": "Bastano due righe. Qualunque dubbio tecnico giocato in chiaro."},
        ],

        "form_sections": [
            {"num": "01", "title": "Chi sei",
             "meta": "Niente BDR, niente sequence — ti risponde un founding member.",
             "fields": ["name", "email", "company"]},
            {"num": "02", "title": "Contesto",
             "meta": "Per adattare la demo al tuo stage e stack.",
             "fields": ["role", "stage", "stack"]},
            {"num": "03", "title": "Preferenze demo",
             "meta": "Dal vivo ogni martedì alle 17:00 CET, altrimenti async via Loom.",
             "fields": ["slot", "context"]},
            {"num": "04", "title": "Materiali (facoltativi)",
             "meta": "Un Loom tuo, screenshot del prodotto o metrics snapshot "
                     "ci permettono di arrivare preparati.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "demo_allegati",
            "label":    "Materiali di contesto",
            "helper":   "PDF, PNG, JPG, MP4, MOV · max 3 file, 25 MB complessivi. "
                        "Utile per chi vuole farci guardare il prodotto o un funnel attuale.",
            "accept":   ".pdf,.png,.jpg,.jpeg,.mp4,.mov",
            "multiple": True,
            "primary":  "Trascina qui deck, screenshot o Loom oppure",
            "link":     "sfoglia dalla cartella",
            "meta":     "PDF / PNG / JPG / MP4 · max 25 MB",
        },

        "form_submit_label": "Prenota la demo",
        "form_submit_note":
            "Conferma entro un'ora negli orari ufficio (9-19 CET) · niente newsletter, "
            "niente sequence automatica.",
        "form_consent":
            "Iscrivendoti accetti l'invio del calendar invite e di una mail "
            "di promemoria 24h prima. Niente newsletter, niente sequence "
            "automatica. Trattamento dati ai sensi del Reg. UE 679/2016.",

        # Async option block
        "async_label":   "Preferisci async?",
        "async_heading": "Loom registrato di 12 minuti",
        "async_intro":
            "Se non riesci a fare la demo dal vivo, abbiamo registrato un Loom "
            "di dodici minuti che mostra il setup completo end-to-end. "
            "Lo riceverai per email entro un'ora dalla richiesta.",
        "async_cta":     "Ricevi il Loom via email",
        "async_cta_href": "demo",

        # Trust strip
        "trust_label":   "Cosa aspettarti dalla demo",
        "trust_items": [
            ("01", "Mezz'ora di screen-share",
             "Niente slide. Apriamo l'app, configuriamo un tier pricing, lanciamo un A/B test, deployiamo."),
            ("02", "Domande tecniche benvenute",
             "Latenza edge, schema Postgres, webhook Stripe — qualunque "
             "domanda implementativa è giocata in chiaro."),
            ("03", "Niente pressure",
             "Non chiudiamo in call. Se ti serve, ti diamo accesso al trial "
             "subito; altrimenti ne riparliamo in una settimana."),
        ],

        "footnote":
            "Le demo sono tenute da uno dei tre founding member di Elevate "
            "(non da BDR esterni). Se la finestra delle 17:00 di martedì non "
            "funziona per il tuo fuso, ti proponiamo uno slot alternativo via "
            "email entro 24 ore.",
    },

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Parla con noi · async-first",
        "headline": "Slack, email o demo dal vivo. <em>Tu scegli</em>.",
        "intro":
            "Async-first significa che rispondiamo entro un'ora in orario "
            "ufficio (9-19 CET) e che le decisioni si prendono per iscritto. "
            "Se preferisci una call, basta prenotarla — è inclusa in tutti "
            "i piani, nessun extra.",

        # Channels grid — 4 ways to reach
        "channels_label":   "Quattro canali, una sola persona ti risponde",
        "channels": [
            {
                "icon":  "✉",
                "title": "Email",
                "value": "hello@elevatekit.io",
                "desc":  "Il founding team legge tutto. Risposta entro 1h in orario ufficio.",
                "cta":   "Scrivi adesso",
            },
            {
                "icon":  "#",
                "title": "Slack community",
                "value": "elevate-founders.slack.com",
                "desc":  "Canale per chi ha attivato il trial o un piano. 220+ founder dentro.",
                "cta":   "Richiedi l'invito",
            },
            {
                "icon":  "▶",
                "title": "Demo dal vivo",
                "value": "Martedì 17:00 CET",
                "desc":  "Trenta minuti di screen-share con un founding member. Async option disponibile.",
                "cta":   "Prenota lo slot",
            },
            {
                "icon":  "✱",
                "title": "Office hours founder",
                "value": "Venerdì 11:00 CET",
                "desc":  "Open call settimanale per piani Scale e Studio. Domande pubbliche, risposte aperte.",
                "cta":   "Iscriviti al calendar",
            },
        ],

        # Founders block — 3 founders with emails (transparency signal)
        "team_label":   "Il founding team",
        "team_heading": "Le persone che leggono le tue email",
        "team_intro":
            "Quando scrivi a hello@elevatekit.io, una di queste tre persone "
            "ti risponde — non un BDR esterno, non un copilot AI. Sotto, "
            "le loro email dirette per richieste specifiche.",
        "team": [
            {
                "name":  "Riccardo Camillini",
                "role":  "Co-founder · Product",
                "email": "riccardo@elevatekit.io",
                "tag":   "Domande prodotto · roadmap",
                "bio":
                    "Tre exit precedenti come technical founder, "
                    "ultima a un fondo SaaS B2B europeo. Si occupa di "
                    "product strategy, roadmap e architecture decision.",
            },
            {
                "name":  "Beatrice Lavia",
                "role":  "Co-founder · Engineering",
                "email": "beatrice@elevatekit.io",
                "tag":   "Domande tecniche · stack · API",
                "bio":
                    "Otto anni come senior engineer in Vercel e Linear. "
                    "Architettata l'edge analytics e tutti gli adapter "
                    "deploy. Risponde a qualunque domanda implementativa.",
            },
            {
                "name":  "Tommaso Adami",
                "role":  "Co-founder · Growth",
                "email": "tommaso@elevatekit.io",
                "tag":   "Onboarding · pricing · partnership",
                "bio":
                    "Ex growth lead di una scale-up fintech europea. "
                    "Si occupa di onboarding, pricing strategy, sconti "
                    "per startup pre-seed e partnership con accelerator.",
            },
        ],

        # Studio info — async-first office
        "office_label":   "Async-first office",
        "office_heading": "Dove siamo (anche se ci troverai online)",
        "office_intro":
            "L'ufficio fisico è a Talent Garden Calabiana a Milano, ma il "
            "team è distribuito (Milano, Berlino, Lisbona, Cracovia). "
            "Async-first significa che i meeting interni sono ridotti al minimo, "
            "e quasi tutto si decide su Linear in pull request.",
        "office": {
            "address":     "Talent Garden Calabiana · Via Calabiana 6 · 20139 Milano",
            "transport":   "M3 Lodi · 8 minuti a piedi · parcheggio interno disponibile",
            "hours":       "Async-first · founder in ufficio martedì e giovedì",
            "schedule": [
                ("Slack",          "Lun – Ven · 9:00 – 19:00 CET"),
                ("Email",          "Risposta entro 1h in orario · entro 24h fuori orario"),
                ("Demo on-demand", "Martedì 17:00 CET · async via Loom anytime"),
                ("Office hours",   "Venerdì 11:00 CET · per piani Scale e Studio"),
            ],
        },

        "footnote":
            "Elevate è un team di sei persone — tre founder + tre engineer. "
            "Risponderemo personalmente alla tua email. Se non senti nulla "
            "entro 24h, non è andata persa: scrivi su Slack e ci attivi un "
            "promemoria. Promesso, non passa nessuna richiesta inascoltata.",
    },
}
