"""Elevate — Startup SaaS Landing Kit · French content tree.

Mirrors the shape of ``ELEVATE_CONTENT_IT`` exactly — same keys, nesting
and list shapes. Authored Session 40+ for the Elevate live i18n rollout
of the startup-saas-landing archetype. Modern French SaaS / growth-tech
register (Maddyness / FrenchWeb / Doctolib / Algolia marketing pages).
"""
from __future__ import annotations

from typing import Any


ELEVATE_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Accueil",     "kind": "home"},
        {"slug": "prodotto",   "label": "Produit",     "kind": "product"},
        {"slug": "prezzi",     "label": "Tarifs",      "kind": "pricing"},
        {"slug": "demo",       "label": "Démo",        "kind": "demo"},
        {"slug": "contatti",   "label": "Contact",     "kind": "contact"},
    ],

    # Site-wide chrome
    "site": {
        "logo_initial": "E",
        "logo_word":    "Elevate",
        "tag":          "Kit conversion-first · pour les founders qui shippent",
        "nav_cta":      "Démarrer gratuitement",
        "phone":        "hello@elevatekit.io",
        "email":        "hello@elevatekit.io",
        "address":      "Talent Garden Calabiana · Milan",
        "hours_compact":"Asynchrone d\u2019abord · Slack 9 h\u202f\u2013\u202f19 h CET",
        "hours_footer_rows": [
            "Démo on-demand · tous les mardis à 17 h 00 CET",
            "Office hours founder · vendredi à 11 h 00 CET",
        ],
        "license":      "",
        "footer_intro":
            "Elevate est le kit GTM qui emmène ta startup de la "
            "waitlist au premier MRR en quatorze jours. Built for founders, "
            "by founders. Shippé depuis Milan, déployé partout.",
        "foot_studio":   "Le produit",
        "foot_pages":    "Naviguer",
        "foot_contact":  "Nous parler",
        "foot_offices":  "Ship log",
        "shiplog_footer_rows": [
            "v2.9 · vendredi · hero builder drag-and-drop",
            "v2.8 · hier · bibliothèque testimonial premium",
            "v2.7 · mardi · A/B test intégré GrowthBook",
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "banner_label":   "Série A · T2 2026",
        "banner_text":    "Nous bouclons les cinquante premières places en early-access",
        "banner_href":    "demo",

        "eyebrow":     "Kit GTM conversion-first · pour SaaS & startups early-stage",
        "headline":    "De la <em>waitlist</em> au premier <em>MRR</em> en quatorze jours.",
        "intro":
            "Elevate est le kit de landing, pricing et onboarding qui "
            "transforme les premiers visiteurs en utilisateurs payants. A/B "
            "test intégré, checkout Stripe one-click, copy kit français, "
            "deploy sur Vercel en trente secondes.",
        "primary_cta":   "Démarrer gratuitement · 14 jours",
        "primary_href":  "demo",
        "secondary_cta": "Voir la démo · 2 min",
        "secondary_href":"prodotto",

        "trust_label":   "Adopté par 240\u202f+ startups européennes en early-stage",
        "trust_logos":   ["FLUX", "NOVA/", "QUANTA", "HELIX", "RIFT.", "CASP", "ARC", "LOOM"],

        # Product mockup card — overlaps the hero / sits below it
        "mockup": {
            "chrome_label":     "elevate.app / dashboard / onboarding-flow",
            "chrome_dots":      ["●", "●", "●"],
            "badge":            "Live A/B",
            "metric_primary":   "↑ 38\u202f%",
            "metric_label":     "Conversion CTA principal",
            "metric_desc":      "vs variante B (contrôle)",
            "secondary_metric": "+ 12,4\u202fK\u202f€",
            "secondary_label":  "MRR · 30 derniers jours",
            "secondary_desc":   "conversion trial-to-paid\u202f: 22\u202f%",
            "feature_label":    "Plan Launch · 29\u202f€ / mois",
            "perks":            ["Hosting + CDN inclus", "CLI deploy · zero config", "Support Slack direct"],
        },

        # Feature pills under the hero
        "feature_pills":  ["Stripe + Linear", "A/B test intégré", "Edge analytics", "Copy kit FR", "Deploy en 30 s"],

        # Capabilities — 6 cards in a 3x2 grid
        "features_label":   "Ce qu\u2019il y a dedans",
        "features_heading": "Six modules, <em>une seule installation</em>.",
        "features_intro":
            "Tous les morceaux nécessaires pour passer en live et commencer "
            "à monétiser — déjà intégrés, déjà testés, déjà documentés.",
        "features": [
            {
                "icon": "→",
                "title": "Hero builder drag-and-drop",
                "desc":
                    "Dix layouts hero pré-testés sur 1\u202f200 startups. "
                    "A/B test entre variantes sans écrire une seule ligne de code.",
            },
            {
                "icon": "$",
                "title": "Pricing table & Stripe",
                "desc":
                    "Trois tiers configurables, conversion checkout one-click, "
                    "subscription management out-of-the-box. Webhooks Stripe "
                    "déjà câblés sur Linear et Slack.",
            },
            {
                "icon": "▲",
                "title": "Edge analytics",
                "desc":
                    "Web vitals, funnel de conversion, attribution multi-touch — "
                    "collectés côté edge, zéro impact sur le TTI. Privacy-first, "
                    "cookieless, RGPD-clean.",
            },
            {
                "icon": "✱",
                "title": "Onboarding flow",
                "desc":
                    "Checklist guidée multi-step, progress bar, triggers email "
                    "sur milestone. Time-to-value médian de 4 minutes vs le "
                    "benchmark secteur de 18.",
            },
            {
                "icon": "◐",
                "title": "Copy kit français",
                "desc":
                    "Soixante blocs de copy testés sur les marchés FR/EN/IT — "
                    "headline, sub, CTA, microcopy onboarding, error states. "
                    "Prêts à éditer en markdown.",
            },
            {
                "icon": "↗",
                "title": "Deploy CLI",
                "desc":
                    "elevate deploy → Vercel / Netlify / Cloudflare en "
                    "trente secondes. Branch previews automatiques, rollback "
                    "en une commande, environment variables synchronisées.",
            },
        ],

        # Live product walkthrough invitation — replaces a fake video block.
        "product_demo_card": {
            "label":      "Voir Elevate en prise directe",
            "heading":    "Quinze minutes avec celles et ceux qui l\u2019ont construit.",
            "intro":
                "Au lieu d\u2019une vidéo enregistrée\u202f: on planifie un walkthrough "
                "court sur le projet réel — éditeur drag-and-drop, wizard de "
                "pricing, câblage Stripe + Linear, deploy sur Vercel. Vraies "
                "questions, vrai projet, sans email de follow-up.",
            "poster":     "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1800&q=80&auto=format&fit=crop",
            "primary_cta":    "Réserver le walkthrough",
            "primary_href":   "demo",
            "secondary_cta":  "Explorer le produit",
            "secondary_href": "prodotto",
            "caption":        "Walkthrough 1-à-1 · agenda en direct",
        },

        # Metric strip on dark band
        "metric_label":   "Les chiffres du kit en production",
        "metric_heading": "Le stack qui shippe",
        "metric_strip": [
            ("3,1\u202f×", "conversion landing moyenne"),
            ("14 j",       "du deploy au premier utilisateur payant"),
            ("99,98\u202f%", "uptime infrastructure"),
            ("4 min",      "time-to-value médian"),
        ],

        # Integrations row
        "integrations_label":   "Intégrations out-of-the-box",
        "integrations_heading": "Déjà câblé avec le stack que tu utilises",
        "integrations": [
            ("Stripe",     "Subscription · Checkout · Tax"),
            ("Linear",     "Issue tracking · changelog auto"),
            ("Slack",      "Notifications · alertes MRR"),
            ("Vercel",     "Deploy · preview · rollback"),
            ("PostHog",    "Funnel · session replay"),
            ("GrowthBook", "A/B test · feature flags"),
            ("Loops",      "Emails transactionnels"),
            ("Cal.com",    "Booking démo auto"),
        ],

        # Pricing teaser — cliccabile verso /prezzi
        "pricing_teaser_label":   "Tarifs transparents",
        "pricing_teaser_heading": "Trois plans, zéro frais de setup.",
        "pricing_teaser_intro":
            "Annulation en un clic, facturation mensuelle ou annuelle, "
            "essai de quatorze jours sans carte bancaire.",
        "pricing_teaser": [
            {"name": "Launch",  "price": "29\u202f€",  "period": "/ mois", "tag": "Pour les founders solo",
             "highlight": False, "perks": ["Tous les modules", "Hosting + CDN", "Email Slack"]},
            {"name": "Scale",   "price": "79\u202f€",  "period": "/ mois", "tag": "Le plus choisi",
             "highlight": True, "perks": ["Tout Launch +", "A/B avancé", "5 projets"]},
            {"name": "Studio",  "price": "199\u202f€", "period": "/ mois", "tag": "Pour studios & agences",
             "highlight": False, "perks": ["Tout Scale +", "Projets illimités", "White-label"]},
        ],
        "pricing_teaser_cta":      "Comparer les plans en détail",
        "pricing_teaser_cta_href": "prezzi",

        # Founder proof — 2 founder quotes
        "founders_label":   "Des founders qui ont shippé avec Elevate",
        "founders_heading": "On passe la parole à ceux qui <em>shippent pour de vrai</em>.",
        "founders": [
            {
                "name":  "Anna Vecchietti",
                "role":  "Founder · Quanta Analytics",
                "quote":
                    "J\u2019avais essayé trois boilerplates et deux builders "
                    "no-code. Avec Elevate je suis partie en live en deux "
                    "week-ends, premier MRR dix-sept jours après le deploy. "
                    "La différence c\u2019est le copy kit — ne pas avoir à "
                    "réécrire chaque headline.",
                "metric_primary": "+ 4,2\u202fK\u202f€",
                "metric_label":   "MRR 60 premiers jours",
            },
            {
                "name":  "Davide Zonca",
                "role":  "CTO · Helix Workflows",
                "quote":
                    "Le stack dont j\u2019avais besoin sans les sept jours "
                    "de setup. Stripe, GrowthBook, Linear déjà câblés, ça "
                    "veut dire qu\u2019on a passé le premier mois à parler "
                    "aux utilisateurs, pas à configurer des webhooks.",
                "metric_primary": "× 3,4",
                "metric_label":   "Conversion vs landing précédente",
            },
        ],

        # Ship log — what shipped recently (transparency block)
        "shiplog_label":   "Ship log live",
        "shiplog_heading": "Ce qu\u2019on a shippé récemment",
        "shiplog_intro":
            "Elevate est en continuous deploy. Chaque feature shippée apparaît "
            "ici en temps réel — pas de roadmap théorique, pas de saisons "
            "produit. Ce que tu vois, c\u2019est ce que tu utilises demain.",
        "shiplog": [
            {"version": "v2.9", "date": "Vendredi",  "title": "Hero builder drag-and-drop",
             "desc": "Dix layouts pré-testés, A/B entre variantes intégré, preview live."},
            {"version": "v2.8", "date": "Hier",      "title": "Bibliothèque testimonial premium",
             "desc": "Quatre layouts (carousel, masonry, single-feature, video-first) avec animations reveal."},
            {"version": "v2.7", "date": "Mardi",     "title": "A/B test intégré GrowthBook",
             "desc": "Wizard de setup d\u2019expérience en 4 étapes, hypothesis tracker, statistical significance auto."},
            {"version": "v2.6", "date": "Lundi",     "title": "Stripe Checkout one-click",
             "desc": "Adaptateurs pour les 4 principaux payment providers EU, gestion TVA automatique."},
            {"version": "v2.5", "date": "Semaine dernière", "title": "Edge analytics privacy-first",
             "desc": "Tracking cookieless, sous les 4\u202fKB sur le TTI, dashboard funnel inclus."},
        ],
        "shiplog_cta":      "S\u2019abonner au ship log via Slack",
        "shiplog_cta_href": "demo",
        "shiplog_release_label": "Prochaine release",
        "shiplog_release_value": "v3.0 · premier lundi du mois",
        "shiplog_release_chip":  "RC live",

        # Final CTA band before footer — glow ring
        "cta_label":     "Commencer maintenant",
        "cta_heading":   "Quatorze jours gratuits. Quarante minutes pour passer en live.",
        "cta_intro":
            "Pas de carte bancaire pour activer l\u2019essai. Slack direct "
            "avec le founding team. Si tu ne shippes pas en deux semaines, "
            "on te rembourse. Promesse écrite.",
        "cta_primary":   "Démarrer l\u2019essai",
        "cta_primary_href": "demo",
        "cta_secondary": "Voir le plan complet",
        "cta_secondary_href": "prezzi",
    },

    # ─── PRODOTTO (product tour) ────────────────────────────────
    "prodotto": {
        "eyebrow":   "Product tour · v2.9 (avril 2026)",
        "headline":  "Tout ce qu\u2019il te faut <em>shipper</em> pour passer en live.",
        "intro":
            "Six modules core + douze intégrations out-of-the-box. "
            "Pas de plugin à configurer, pas de boilerplate à forker, "
            "pas de thread Twitter à suivre pour faire ce qui devrait "
            "être évident. Ouvre, édite, deploy.",

        # Product modules — same 6 from home but expanded with detail
        "modules_label":   "Modules core",
        "modules_heading": "Six pièces, une seule installation",
        "modules": [
            {
                "num":   "01",
                "title": "Hero builder drag-and-drop",
                "blurb":
                    "Dix layouts hero pré-testés sur 1\u202f200 startups "
                    "early-stage. Chaque layout est livré avec trois variantes "
                    "de copy (B2B, B2C, dev-tool) et avec A/B test intégré.",
                "highlights": [
                    "10 layouts · 30 variantes de copy",
                    "A/B entre variantes sans code",
                    "Headline, sub, CTA, badge social tous éditables",
                    "Mobile + desktop optimisés séparément",
                ],
            },
            {
                "num":   "02",
                "title": "Pricing table & Stripe Checkout",
                "blurb":
                    "Trois tiers configurables avec highlight automatique sur "
                    "le plan central. Subscription management Stripe, "
                    "checkout one-click sur mobile, gestion TVA EU automatique.",
                "highlights": [
                    "1, 2, 3 ou 4 tiers · highlight au choix",
                    "Toggle mensuel / annuel built-in",
                    "Stripe Tax sur 38 pays EU",
                    "Webhooks Stripe → Slack déjà câblés",
                ],
            },
            {
                "num":   "03",
                "title": "Edge analytics privacy-first",
                "blurb":
                    "Web vitals, funnel multi-step, attribution multi-touch — "
                    "tout collecté côté edge via Cloudflare Worker. "
                    "Cookieless, RGPD-clean, sous les 4\u202fKB sur le TTI.",
                "highlights": [
                    "Cookieless · RGPD · ePrivacy clean",
                    "Web Vitals · LCP · FID · CLS en dashboard",
                    "Funnel de conversion visuel",
                    "Connecteur PostHog optionnel",
                ],
            },
            {
                "num":   "04",
                "title": "Onboarding flow guidé",
                "blurb":
                    "Checklist multi-step avec progress bar, milestone "
                    "celebration, triggers email automatiques. Time-to-value "
                    "médian de 4 minutes vs le benchmark secteur de 18.",
                "highlights": [
                    "Checklist drag-and-drop personnalisable",
                    "Triggers email sur Loops · Resend · Postmark",
                    "Achievement badge built-in",
                    "Re-engagement automatique après 48 h",
                ],
            },
            {
                "num":   "05",
                "title": "Copy kit français (et EN/IT)",
                "blurb":
                    "Soixante blocs de copy éditoriale testés sur les "
                    "marchés FR/EN/IT. Headline, sub, CTA, microcopy "
                    "onboarding, error states, empty states.",
                "highlights": [
                    "60 blocs · FR + EN + IT",
                    "Tone-of-voice configurable",
                    "Édition markdown directe",
                    "Snippet library avec recherche sémantique",
                ],
            },
            {
                "num":   "06",
                "title": "Deploy CLI · trente secondes",
                "blurb":
                    "elevate deploy. Trente secondes pour le premier deploy "
                    "live, branch previews automatiques sur PR, rollback en "
                    "une commande, environment variables synchronisées "
                    "entre dev / staging / prod.",
                "highlights": [
                    "Adaptateur Vercel · Netlify · Cloudflare",
                    "Branch previews automatiques sur PR",
                    "Rollback instantané · zero downtime",
                    "Sync env-var · dev / staging / prod",
                ],
            },
        ],

        # Integrations grid — bigger version of home
        "integrations_label":   "Intégrations out-of-the-box",
        "integrations_heading": "Le stack dont tu as besoin, déjà câblé.",
        "integrations_intro":
            "Douze intégrations natives, zéro plugin à installer. "
            "Celles que tu ne vois pas ici, on les ajoute si tu nous les "
            "demandes sur Slack.",
        "integrations_full": [
            {"name": "Stripe",     "category": "Paiements",   "desc": "Subscription · Checkout · Tax · Connect"},
            {"name": "Linear",     "category": "Tracking",    "desc": "Issues · Cycles · changelog auto-publié"},
            {"name": "Slack",      "category": "Comms",       "desc": "Notifications · alertes MRR · daily digest"},
            {"name": "Vercel",     "category": "Deploy",      "desc": "Production deploy · preview branch · rollback"},
            {"name": "Netlify",    "category": "Deploy",      "desc": "Edge functions · build hooks · analytics sync"},
            {"name": "Cloudflare", "category": "Deploy",      "desc": "Workers · KV · D1 · R2 storage"},
            {"name": "PostHog",    "category": "Analytics",   "desc": "Funnel · session replay · feature flags"},
            {"name": "GrowthBook", "category": "Expériences", "desc": "A/B test · hypothesis tracker · stat-sig auto"},
            {"name": "Loops",      "category": "Email",       "desc": "Transactionnels · onboarding sequences"},
            {"name": "Resend",     "category": "Email",       "desc": "Transactionnels · templates React Email"},
            {"name": "Cal.com",    "category": "Booking",     "desc": "Booking démo · routing · webhooks"},
            {"name": "Plain",      "category": "Support",     "desc": "Support inbox · CRM avec triage IA"},
        ],

        # Architecture — what runs where
        "stack_label":   "Architecture",
        "stack_heading": "Ce qui tourne où (et pourquoi)",
        "stack_intro":
            "Transparence technique — pas de magie, pas de lock-in caché. "
            "Le stack est documenté ouvertement, et l\u2019intégralité du "
            "code est exportable en un clic si tu décides de partir.",
        "stack": [
            ("Frontend",    "Next.js 15 · React 19 · App Router · Server Actions"),
            ("Edge",        "Cloudflare Workers + KV pour analytics et A/B"),
            ("Base de données", "PostgreSQL · Prisma · Neon serverless"),
            ("Auth",        "Clerk · OAuth · passkey · magic link"),
            ("Paiements",   "Stripe Subscriptions + Stripe Tax + Stripe Connect"),
            ("Email",       "Loops ou Resend au choix · templates React Email"),
            ("Analytics",   "PostHog optionnel · edge analytics natif"),
            ("Expériences", "GrowthBook · self-hosted ou cloud"),
        ],

        "cta_heading":   "Prêt·e à le voir tourner\u202f?",
        "cta_intro":
            "Démo en direct avec un founding member tous les mardis à "
            "17 h 00 CET. Demi-heure de call, screen-share, questions "
            "techniques bienvenues.",
        "cta_primary":   "Réserver une démo",
        "cta_primary_href": "demo",
        "cta_secondary": "Voir les plans",
        "cta_secondary_href": "prezzi",
    },

    # ─── PREZZI (pricing) ───────────────────────────────────────
    "prezzi": {
        "eyebrow":  "Tarifs transparents · 2026",
        "headline": "Tu annules en un clic. <em>Toujours</em>.",
        "intro":
            "Trois plans, zéro frais de setup, facturation mensuelle ou "
            "annuelle (deux mois offerts sur l\u2019annuel). Quatorze "
            "jours d\u2019essai gratuit, sans carte bancaire.",

        # Highlight badge label
        "highlight_badge": "Le plus choisi",
        "annual_prefix":   "ou",

        # Toggle row UI cue
        "billing_toggle_label": "Facturation",
        "billing_toggle_options": [
            ("monthly", "Mensuelle"),
            ("annual",  "Annuelle · –17\u202f%"),
        ],

        # Three pricing tiers
        "tiers": [
            {
                "name":     "Launch",
                "tag":      "Pour les founders solo",
                "price":    "29\u202f€",
                "annual":   "24\u202f€",
                "period":   "/ mois",
                "annual_period": "/ mois · payé annuellement",
                "highlight": False,
                "blurb":
                    "Tout ce qu\u2019il faut pour passer en live avec un "
                    "seul produit. Pensé pour le founder solo ou la "
                    "première semaine du founding team.",
                "cta":         "Démarrer gratuitement",
                "cta_href":    "demo",
                "perks": [
                    ("✓", "Les six modules core"),
                    ("✓", "Hosting + CDN global inclus"),
                    ("✓", "Deploy CLI · branch previews automatiques"),
                    ("✓", "Edge analytics + funnel de base"),
                    ("✓", "1 projet · 1 domaine custom"),
                    ("✓", "Slack direct avec le founding team"),
                    ("○", "A/B test basique (manuel)"),
                    ("○", "1 copy kit (FR ou EN ou IT)"),
                ],
            },
            {
                "name":     "Scale",
                "tag":      "Le plus choisi · pour startups post-PMF",
                "price":    "79\u202f€",
                "annual":   "65\u202f€",
                "period":   "/ mois",
                "annual_period": "/ mois · payé annuellement",
                "highlight": True,
                "blurb":
                    "Le plan pour le founding team qui a trouvé le "
                    "product/market fit et qui scale. Ajoute A/B avancé, "
                    "multi-projet, white-glove onboarding.",
                "cta":         "Démarrer gratuitement",
                "cta_href":    "demo",
                "perks": [
                    ("✓", "Tout Launch +"),
                    ("✓", "A/B test avancé (GrowthBook intégré)"),
                    ("✓", "5 projets · domaines custom illimités"),
                    ("✓", "Connecteur PostHog + session replay"),
                    ("✓", "Stripe Tax + Stripe Connect"),
                    ("✓", "Les 3 copy kits (FR + EN + IT)"),
                    ("✓", "Onboarding 1-1 avec le founding team (60 min)"),
                    ("✓", "Canal Slack dédié · SLA 4 h"),
                ],
            },
            {
                "name":     "Studio",
                "tag":      "Pour studios, agences & venture builders",
                "price":    "199\u202f€",
                "annual":   "165\u202f€",
                "period":   "/ mois",
                "annual_period": "/ mois · payé annuellement",
                "highlight": False,
                "blurb":
                    "Pour agences, studios créatifs et venture builders "
                    "qui shippent plusieurs landings pour des clients "
                    "différents. Projets illimités et white-label complet.",
                "cta":         "Nous parler",
                "cta_href":    "contatti",
                "perks": [
                    ("✓", "Tout Scale +"),
                    ("✓", "Projets illimités · branding white-label"),
                    ("✓", "Sub-account pour chaque client"),
                    ("✓", "API complète · webhooks custom"),
                    ("✓", "SLA 1 h · support téléphonique"),
                    ("✓", "Account manager dédié"),
                    ("✓", "Quarterly review avec le founding team"),
                    ("✓", "Audit trail · compliance SOC 2"),
                ],
            },
        ],

        # Comparison — what's NOT included
        "comparison_label":   "Ce qu\u2019il n\u2019y a pas (et pourquoi)",
        "comparison_heading": "La transparence que les autres évitent",
        "comparison": [
            ("Frais de setup",
             "Jamais. Ni sur Launch, ni sur Scale, ni sur Studio. Si tu "
             "trouves un boilerplate concurrent qui ne te facture pas de "
             "setup + qui te livre le stack déjà câblé, signale-le nous "
             "et on te rembourse le premier mois."),
            ("Lock-in du code",
             "Jamais. L\u2019intégralité de ton code est exportable en "
             "CLI en une commande. Si tu décides de quitter Elevate, on "
             "déplace ton deploy sur un Vercel qui t\u2019appartient "
             "gratuitement sous 24 h."),
            ("Tarifs cachés",
             "Jamais. Ce que tu lis, c\u2019est ce que tu paies. La TVA "
             "EU est automatiquement calculée et affichée au checkout — "
             "aucune surprise sur la facture."),
            ("Plafond de transactions",
             "Jamais. Stripe Connect n\u2019a pas de cap sur les "
             "transactions ou le volume. Tu vends 10 abonnements ou "
             "10\u202f000 — le prix est le même."),
        ],

        # FAQ accordion
        "faq_label":   "Questions fréquentes",
        "faq_heading": "Ce qu\u2019on nous demande le plus",
        "faq": [
            ("Je peux essayer avant de payer\u202f?",
             "Oui, quatorze jours d\u2019essai complet sans carte "
             "bancaire. Tu as accès à tous les modules du plan Scale "
             "pendant l\u2019essai — si tu décides de rester, tu choisis "
             "le plan qui te convient. Sinon, l\u2019essai expire "
             "automatiquement, aucun prélèvement automatique."),
            ("Qu\u2019est-ce qui se passe si j\u2019annule\u202f?",
             "Tu annules depuis le dashboard en un clic, à tout moment. "
             "Ton deploy reste live jusqu\u2019à la fin de la période "
             "déjà payée. On exporte ton code en CLI et on t\u2019aide à "
             "migrer vers ton propre Vercel/Netlify si tu veux continuer "
             "en autonomie."),
            ("Vous avez une remise pour startups\u202f?",
             "Oui, 50\u202f% sur les six premiers mois pour les startups "
             "pre-seed (levée <\u202f500\u202fK\u202f€) et 30\u202f% sur "
             "la première année pour les post-seed. Écris à "
             "hello@elevatekit.io avec le pitch deck pour activer la "
             "promotion."),
            ("Ça s\u2019intègre avec notre stack existant\u202f?",
             "Probablement oui. Les 12 intégrations natives couvrent "
             "90\u202f% des stacks qu\u2019on voit, et l\u2019API REST + "
             "webhooks custom permettent de brancher ce qui manque. Si "
             "tu as besoin d\u2019une intégration qui n\u2019existe pas, "
             "écris-nous sur Slack — en général on la shippe en deux "
             "semaines."),
            ("Je peux héberger moi-même\u202f?",
             "Sur le plan Studio, oui — on te fournit le container "
             "Docker et le schéma Postgres à héberger où tu préfères. "
             "Sur les plans Launch et Scale, l\u2019hosting est inclus "
             "et fait partie de la valeur du kit."),
            ("Les factures sont en Italie\u202f?",
             "Oui, on facture depuis Milan en EUR avec un numéro de "
             "TVA italien, facturation électronique SDI incluse. Pour "
             "les clients UE non-IT, la facture est en auto-liquidation "
             "de TVA."),
        ],

        "cta_heading":   "Prêt·e à démarrer\u202f?",
        "cta_intro":
            "Quatorze jours gratuits. Pas de carte bancaire. "
            "Quarante minutes pour passer en live avec ton premier deploy.",
        "cta_primary":   "Démarrer l\u2019essai",
        "cta_primary_href": "demo",
        "cta_secondary": "Des questions\u202f? Écris-nous",
        "cta_secondary_href": "contatti",
    },

    # ─── DEMO (lead form) ───────────────────────────────────────
    "demo": {
        "eyebrow":  "Démo en direct · mardi 17 h 00 CET",
        "headline": "Demi-heure avec un <em>founding member</em>.",
        "intro":
            "Démo en direct tous les mardis à 17 h 00 CET. Trente "
            "minutes de screen-share — on montre comment configurer un "
            "tier pricing, comment lancer un A/B test, comment faire le "
            "premier deploy. Questions techniques bienvenues, pitch deck "
            "pas requis.",

        # Form
        "form_label":   "Réserver un créneau",
        "form_heading": "Remplis et on te confirme sous une heure",
        "form_intro":
            "Le créneau du mardi prochain est celui qui te sera attribué "
            "par défaut. Si tu préfères un créneau ad hoc, choisis "
            "«\u202fCréneau personnalisé\u202f» et on t\u2019écrit pour "
            "le caler. Asynchrone only\u202f? Parfait, voir ci-dessous.",
        "form_fields": [
            {"name": "name",     "label": "Prénom",        "type": "text",  "required": True,  "placeholder": "Ex. Anna",
             "helper": "Pour qu\u2019on te salue en démo."},
            {"name": "email",    "label": "Email",         "type": "email", "required": True,  "placeholder": "anna@startup.io",
             "helper": "Le calendar invite + Loom arrivent ici."},
            {"name": "company",  "label": "Startup",       "type": "text",  "required": True,  "placeholder": "Ex. Quanta Analytics",
             "helper": "Le nom que tu utilises pour les commits et la facturation."},
            {"name": "role",     "label": "Rôle",          "type": "select","required": True,
             "options": ["Founder solo", "Co-founder · CEO", "Co-founder · CTO", "Co-founder · autre", "Hire 1-5", "Autre"],
             "helper": "Si tu es seul·e, «\u202fFounder solo\u202f» est le bon choix."},
            {"name": "stage",    "label": "Phase",         "type": "select","required": True,
             "options": ["Pré-idée / exploration", "Pre-launch / waitlist", "Post-launch / recherche PMF", "Post-PMF / scaling"],
             "helper": "La démo s\u2019adapte\u202f: pre-launch voit onboarding + waitlist, post-PMF voit tier pricing + A/B."},
            {"name": "slot",     "label": "Créneau préféré","type": "select","required": True,
             "options": ["Mardi prochain 17 h 00 CET", "Créneau personnalisé (on vous écrit)", "Asynchrone — envoyez-moi un Loom enregistré"],
             "helper": "Créneau async = tu reçois tout de suite le Loom de 12 min par email."},
            {"name": "stack",    "label": "Stack actuel",
             "type": "text", "required": False,
             "placeholder": "Ex. Next.js + Vercel + Stripe",
             "helper": "Facultatif. On se cale tout de suite sur les bons points d\u2019intégration."},
            {"name": "context",  "label": "Qu\u2019est-ce que tu veux savoir\u202f?", "type": "textarea",
             "required": False, "full_width": True,
             "placeholder": "Questions spécifiques, blocs que tu veux voir en démo, doutes techniques… (optionnel)",
             "helper": "Deux lignes suffisent. Les doutes techniques joués à découvert."},
        ],

        "form_sections": [
            {"num": "01", "title": "Qui tu es",
             "meta": "Pas de BDR, pas de sequence — un founding member te répond.",
             "fields": ["name", "email", "company"]},
            {"num": "02", "title": "Contexte",
             "meta": "Pour adapter la démo à ton stage et ton stack.",
             "fields": ["role", "stage", "stack"]},
            {"num": "03", "title": "Préférences démo",
             "meta": "En direct tous les mardis à 17 h 00 CET, sinon en asynchrone via Loom.",
             "fields": ["slot", "context"]},
            {"num": "04", "title": "Supports (facultatifs)",
             "meta": "Un Loom à toi, des screenshots du produit ou un "
                     "snapshot metrics nous permettent d\u2019arriver "
                     "préparés.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "demo_allegati",
            "label":    "Supports de contexte",
            "helper":   "PDF, PNG, JPG, MP4, MOV · max 3 fichiers, 25 Mo au total. "
                        "Utile pour celles et ceux qui veulent nous montrer "
                        "le produit ou un funnel existant.",
            "accept":   ".pdf,.png,.jpg,.jpeg,.mp4,.mov",
            "multiple": True,
            "primary":  "Glisse ici deck, screenshots ou Loom ou bien",
            "link":     "parcours le dossier",
            "meta":     "PDF / PNG / JPG / MP4 · max 25 Mo",
        },

        "form_submit_label": "Réserver la démo",
        "form_submit_note":
            "Confirmation sous une heure aux horaires de bureau (9 h\u202f–\u202f19 h CET) · pas de newsletter, "
            "pas de sequence automatique.",
        "form_consent":
            "En t\u2019inscrivant, tu acceptes l\u2019envoi du calendar "
            "invite et d\u2019un email de rappel 24 h avant. Pas de "
            "newsletter, pas de sequence automatique. Traitement des "
            "données conformément au Règl. UE 679/2016.",

        # Async option block
        "async_label":   "Tu préfères asynchrone\u202f?",
        "async_heading": "Loom enregistré de 12 minutes",
        "async_intro":
            "Si tu ne peux pas faire la démo en direct, on a enregistré "
            "un Loom de douze minutes qui montre le setup complet "
            "end-to-end. Tu le recevras par email dans l\u2019heure qui "
            "suit la demande.",
        "async_cta":     "Recevoir le Loom par email",
        "async_cta_href": "demo",

        # Trust strip
        "trust_label":   "Ce à quoi t\u2019attendre en démo",
        "trust_items": [
            ("01", "Demi-heure de screen-share",
             "Pas de slides. On ouvre l\u2019app, on configure un tier pricing, on lance un A/B test, on deploy."),
            ("02", "Questions techniques bienvenues",
             "Latence edge, schéma Postgres, webhooks Stripe — "
             "n\u2019importe quelle question d\u2019implémentation est "
             "jouée à découvert."),
            ("03", "Zéro pression",
             "On ne closent pas en call. Si tu en as besoin, on te donne "
             "accès à l\u2019essai tout de suite\u202f; sinon on en "
             "reparle dans une semaine."),
        ],

        "footnote":
            "Les démos sont animées par l\u2019un des trois founding "
            "members d\u2019Elevate (pas par des BDR externes). Si la "
            "fenêtre du mardi 17 h 00 ne fonctionne pas pour ton fuseau, "
            "on te propose un créneau alternatif par email sous 24 h.",
    },

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Nous parler · asynchrone d\u2019abord",
        "headline": "Slack, email ou démo en direct. <em>À toi de choisir</em>.",
        "intro":
            "Asynchrone d\u2019abord, ça veut dire qu\u2019on répond "
            "sous une heure aux horaires de bureau (9 h\u202f–\u202f19 h "
            "CET) et que les décisions se prennent par écrit. Si tu "
            "préfères un call, il suffit de le réserver — c\u2019est "
            "inclus dans tous les plans, sans extra.",

        # Channels grid — 4 ways to reach
        "channels_label":   "Quatre canaux, une seule personne te répond",
        "channels": [
            {
                "icon":  "✉",
                "title": "Email",
                "value": "hello@elevatekit.io",
                "desc":  "Le founding team lit tout. Réponse sous 1 h aux horaires de bureau.",
                "cta":   "Écrire maintenant",
            },
            {
                "icon":  "#",
                "title": "Slack community",
                "value": "elevate-founders.slack.com",
                "desc":  "Canal pour celles et ceux qui ont activé l\u2019essai ou un plan. 220\u202f+ founders dedans.",
                "cta":   "Demander l\u2019invitation",
            },
            {
                "icon":  "▶",
                "title": "Démo en direct",
                "value": "Mardi 17 h 00 CET",
                "desc":  "Trente minutes de screen-share avec un founding member. Option asynchrone disponible.",
                "cta":   "Réserver le créneau",
            },
            {
                "icon":  "✱",
                "title": "Office hours founder",
                "value": "Vendredi 11 h 00 CET",
                "desc":  "Open call hebdomadaire pour les plans Scale et Studio. Questions publiques, réponses ouvertes.",
                "cta":   "S\u2019inscrire au calendar",
            },
        ],

        # Founders block — 3 founders with emails (transparency signal)
        "team_label":   "Le founding team",
        "team_heading": "Les personnes qui lisent tes emails",
        "team_intro":
            "Quand tu écris à hello@elevatekit.io, l\u2019une de ces "
            "trois personnes te répond — pas un BDR externe, pas un "
            "copilot IA. Ci-dessous, leurs emails directs pour les "
            "demandes spécifiques.",
        "team": [
            {
                "name":  "Riccardo Camillini",
                "role":  "Co-founder · Product",
                "email": "riccardo@elevatekit.io",
                "tag":   "Questions produit · roadmap",
                "bio":
                    "Trois exits précédents comme technical founder, le "
                    "dernier vers un fonds SaaS B2B européen. Il pilote "
                    "la product strategy, la roadmap et les architecture "
                    "decisions.",
            },
            {
                "name":  "Beatrice Lavia",
                "role":  "Co-founder · Engineering",
                "email": "beatrice@elevatekit.io",
                "tag":   "Questions techniques · stack · API",
                "bio":
                    "Huit ans comme senior engineer chez Vercel et "
                    "Linear. A architecturé l\u2019edge analytics et "
                    "tous les adapters deploy. Répond à n\u2019importe "
                    "quelle question d\u2019implémentation.",
            },
            {
                "name":  "Tommaso Adami",
                "role":  "Co-founder · Growth",
                "email": "tommaso@elevatekit.io",
                "tag":   "Onboarding · pricing · partnership",
                "bio":
                    "Ex growth lead d\u2019une scale-up fintech "
                    "européenne. Il pilote l\u2019onboarding, la pricing "
                    "strategy, les remises pour startups pre-seed et les "
                    "partnerships avec accelerators.",
            },
        ],

        # Office meta-row labels
        "office_address_label":   "Bureau",
        "office_transport_label": "Transports",
        "office_model_label":     "Modèle",

        # Studio info — async-first office
        "office_label":   "Async-first office",
        "office_heading": "Où on est (même si tu nous trouveras en ligne)",
        "office_intro":
            "Le bureau physique est au Talent Garden Calabiana à Milan, "
            "mais l\u2019équipe est distribuée (Milan, Berlin, Lisbonne, "
            "Cracovie). Asynchrone d\u2019abord veut dire que les "
            "meetings internes sont réduits au minimum, et que presque "
            "tout se décide sur Linear en pull request.",
        "office": {
            "address":     "Talent Garden Calabiana · Via Calabiana 6 · 20139 Milan",
            "transport":   "M3 Lodi · 8 minutes à pied · parking intérieur disponible",
            "hours":       "Asynchrone d\u2019abord · founders au bureau mardi et jeudi",
            "schedule": [
                ("Slack",          "Lun\u202f–\u202fVen · 9 h 00\u202f–\u202f19 h 00 CET"),
                ("Email",          "Réponse sous 1 h aux horaires · sous 24 h hors horaires"),
                ("Démo on-demand", "Mardi 17 h 00 CET · asynchrone via Loom à tout moment"),
                ("Office hours",   "Vendredi 11 h 00 CET · pour les plans Scale et Studio"),
            ],
        },

        "footnote":
            "Elevate, c\u2019est une équipe de six personnes — trois "
            "founders + trois engineers. On répondra personnellement à "
            "ton email. Si tu n\u2019as pas de retour sous 24 h, ce "
            "n\u2019est pas perdu\u202f: écris sur Slack et tu nous "
            "déclenches un rappel. Promis, aucune demande ne reste sans "
            "réponse.",
    },
}
