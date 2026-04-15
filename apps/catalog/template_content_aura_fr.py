"""Aura — Digital Studio · FR content registry.

Agency live rollout, Phase 2g3.6f, Session 49 · French locale.

Voice contract (Paris / Bruxelles digital-product-studio register):
- Maddyness / Les Echos Tech register. Vouvoiement par défaut, tutoiement
  uniquement dans les CTAs organiques SaaS.
- Lexique growth-tech : sprint, discovery, backlog, télémétrie,
  tableau de bord, onboarding, NPS, time to value, rétention,
  A/B test. Jamais vocabulaire curatorial / éditorial.
- Anglicismes SaaS acceptés. Stack names, brand names conservés.
- Numbers explicit. "MRR 840 K€". Mono usage: ship log codes, sprint ID.
- sett. → sem., min. → min, gg → j.
"""
from __future__ import annotations

from typing import Any


AURA_CONTENT_FR: dict[str, Any] = {

    "pages": [
        {"slug": "home",         "label": "Studio",       "kind": "home"},
        {"slug": "studio",       "label": "À propos",     "kind": "about"},
        {"slug": "capabilities", "label": "Capabilities", "kind": "services"},
        {"slug": "lavori",       "label": "Travaux",      "kind": "project_list"},
        {"slug": "sprint",       "label": "Sprint",       "kind": "process"},
        {"slug": "brief",        "label": "Brief",        "kind": "contact"},
    ],

    # ── Site chrome ──────────────────────────────────────────────
    "site": {
        "logo_word":   "Aura",
        "tag":         "Digital · product · growth studio",
        "sprint_chip": "Sprint 07/Q2 · live",
        "nav_cta":     "Réserver une call",
        "inquiry_page_slug": "brief",
        "phone":       "+39 02 8728 4411",
        "email":       "hello@aura.studio",
        "address":     "Via Paolo Sarpi 41 · 20154 Milan",
        "hours_compact":"Call slots · lun — jeu · 10 — 18",
        "license":     "P.IVA 12890440964 · Milan",
        "footer_intro":
            "Studio digital indépendant. Nous dessinons des produits, "
            "des plateformes et des systèmes de croissance pour scale-up et "
            "entreprises tech. Basés à Milan, delivery européen.",
        "foot_shiplog_label":    "// ship log · last 6",
        "foot_current_sprint":   "sprint 07/Q2 · live",
        "foot_shiplog_rows": [
            ("hier · 18:04", "v2.14", "Soldo — nouvel onboarding corporate live"),
            ("hier · 09:21", "v2.13", "Fastweb Plus — tableau de bord résidentiel v2.3"),
            ("lun · 15:30",  "v2.12", "Lendlease — portail asset manager"),
            ("ven · 11:12",  "v2.11", "Casavo — retention A/B loop 003"),
            ("jeu · 17:45",  "v2.10", "Milkman — SDK ship tracking"),
            ("mer · 10:02",  "v2.09", "Fiscozen — onboarding self-serve"),
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
        "chip": "3 slots disponibles · Q3 2026",
        "headline": "De la <em>call de discovery</em> au <em>premier KPI</em> en six semaines.",
        "intro":
            "Nous sommes un studio digital qui construit des produits et "
            "des systèmes de croissance pour scale-up italiennes et européennes. "
            "Sprints de deux semaines, tableau de bord partagé, "
            "livraisons mesurables. Zéro agence, tout produit.",
        "primary_cta":   "Réserver une call",
        "primary_href":  "brief",
        "secondary_cta": "Travaux récents",
        "secondary_href":"lavori",

        "hero_metrics": [
            ("<em>47</em>",     "produits livrés depuis 2019"),
            ("<em>+34%</em>",   "conversion médiane post-rework"),
            ("<em>6 sem.</em>", "du sprint zéro au premier KPI"),
        ],

        # Dashboard console tile
        "console": {
            "path":           "aura.studio/clients/casavo/live",
            "status_chip":    "LIVE · sprint 07/Q2",
            "primary_metric": "+34%",
            "primary_label":  "Conversion post-rework · 30 derniers jours",
            "kpi": [
                ("<em>+18%</em>",    "Rétention jour 30"),
                ("<em>Δ 22</em>",    "NPS pre / post · Casavo"),
                ("<em>840 K€</em>",  "MRR · sprint 1 – 14"),
                ("<em>99.98%</em>",  "Uptime dernier trimestre"),
            ],
            "meta_label":     "Sprint en cours",
            "meta_value":     "07/Q2 · week 2 of 2",
        },

        # Capabilities mini
        "capab_label":   "Capabilities",
        "capab_heading": "Quatre <em>domaines</em>, une seule équipe.",
        "capab_intro":
            "Nous travaillons sur quatre types de projets — lancements produit, "
            "refontes de plateforme, systèmes de croissance et delivery de "
            "plateformes B2B. Chaque projet traverse une équipe de 3-5 personnes "
            "dédiées, jamais un account layer.",
        "capab_cards": [
            {
                "id":   "C.01",
                "title":"Product <em>launch</em>",
                "body": "Du concept à l'onboarding live. "
                        "Idéal pour scale-up en Série A qui doivent "
                        "passer du MVP au produit payant.",
                "tags": ["Discovery", "Design system", "Next.js", "Analytics"],
            },
            {
                "id":   "C.02",
                "title":"Platform <em>redesign</em>",
                "body": "Repenser des produits matures sans perdre d'utilisateurs. "
                        "Research, A/B test, migration progressive.",
                "tags": ["UX audit", "A/B", "Incremental ship", "PostHog"],
            },
            {
                "id":   "C.03",
                "title":"Growth <em>systems</em>",
                "body": "Onboarding, rétention, referral, pricing experiments. "
                        "Quick wins les 30 premiers jours, systèmes à 90 jours.",
                "tags": ["Onboarding", "Rétention", "Pricing", "Experiments"],
            },
            {
                "id":   "C.04",
                "title":"B2B <em>delivery</em>",
                "body": "Portails asset manager, tableaux de bord corporate, "
                        "backoffices internes. Intégration SSO + data warehouse.",
                "tags": ["Dashboards", "SSO", "Roles", "BigQuery"],
            },
        ],

        # Sprint strip
        "sprint_label":   "Comment nous livrons",
        "sprint_heading": "Quatre <em>sprints</em>, de la discovery à l'échelle.",
        "sprint_intro":
            "Chaque projet est structuré en sprints de deux semaines. "
            "Vous voyez exactement ce que nous faisons, quand ce sera livré, "
            "et quelles métriques nous déplaçons. Aucune surprise de fin de mois.",
        "sprints": [
            {
                "id":"S.00", "duration":"Sprint 0 · 1 semaine",
                "title":"<em>Signal</em>",
                "body": "Discovery avec les stakeholders, utilisateurs, dashboard. "
                        "Livraison : brief partagé + backlog initial.",
                "output": "OUT · brief + backlog",
            },
            {
                "id":"S.01", "duration":"Sprint 1 — 2 · 4 sem.",
                "title":"<em>Sketch</em>",
                "body": "Design system + prototypes testables. "
                        "Research qualitative + premiers A/B sur les hypothèses critiques.",
                "output": "OUT · prototype + design tokens",
            },
            {
                "id":"S.02", "duration":"Sprint 3 — 5 · 6 sem.",
                "title":"<em>Ship</em>",
                "body": "Implémentation staging → production. "
                        "Monitoring live des métriques, rollback disponible à 1 clic.",
                "output": "OUT · production + first KPI",
            },
            {
                "id":"S.03", "duration":"Sprint 6+ · ongoing",
                "title":"<em>Scale</em>",
                "body": "Expérimentations continues, expansion de features, "
                        "optimisation post-launch. Ship-log partenaire partagé.",
                "output": "OUT · weekly ship-log",
            },
        ],

        # Lavori cards
        "work_label":      "Travaux récents",
        "work_heading":    "Sept <em>produits</em>, sept <em>métriques</em>.",
        "work_intro":
            "Chaque projet a une métrique claire, déclarée au sprint zéro "
            "et mesurée au sprint trois. Si la métrique ne bouge pas, nous travaillons "
            "gratuitement jusqu'à ce qu'elle bouge.",
        "work_page_slug": "lavori",
        "work_cards": [
            {
                "slug": "casavo-retention-rework",
                "id":   "W.01",
                "cover":"https://images.unsplash.com/photo-1551434678-e076c223a692?w=900&q=80&auto=format&fit=crop",
                "title":"Retention rework de trois mois",
                "client":"Casavo · Proptech Milan",
                "metric_chip": "+18% rétention · D30",
                "stack":["Next.js", "PostHog", "Figma"],
            },
            {
                "slug": "fastweb-plus-dashboard",
                "id":   "W.02",
                "cover":"https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=900&q=80&auto=format&fit=crop",
                "title":"Tableau de bord résidentiel v2",
                "client":"Fastweb · Telco Italie",
                "metric_chip": "NPS +22 · 6 mois",
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
            ("<em>47</em>",      "produits livrés",       "depuis 2019 — moyenne 8 / an"),
            ("<em>+34%</em>",    "conversion médiane",    "entre pre- et post-rework"),
            ("<em>99.98%</em>",  "uptime",                "dernier trimestre · status.aura.studio"),
            ("<em>6 sem.</em>",  "time to first KPI",     "du sprint zéro à la première métrique déplacée"),
        ],

        "cta_label":   "Prochaine call",
        "cta_heading": "Trois <em>slots</em> ouverts pour Q3 2026.",
        "cta_sub":
            "Le premier slot est une call de discovery de 30 minutes. Si le "
            "projet nous correspond, sous 5 jours vous recevez un "
            "brief de lecture + estimation de sprint zéro.",
        "cta_chip":    "30 min · zéro engagement",
        "cta_primary": "Réserver une call",
    },

    # ── STUDIO (about) ───────────────────────────────────────────
    "studio": {
        "chip": "Équipe · 11 personnes · Milan + remote",
        "headline": "Une équipe de <em>onze</em>, <em>huit ans</em> de produits livrés.",
        "standfirst":
            "Aura est un studio de product design et d'engineering fondé à "
            "Milan en 2019. Onze personnes — cinq designers, quatre "
            "engineers, deux product managers — réparties entre Milan, Turin "
            "et remote. Zéro account manager, zéro couche intermédiaire : "
            "celui qui signe le brief est celui qui l'expédie.",

        "facts": [
            ("<em>11</em>",    "personnes",            "5 design · 4 eng · 2 PM"),
            ("<em>47</em>",    "produits livrés",      "De 2019 à aujourd'hui"),
            ("<em>3</em>",     "sites",                "Milan · Turin · remote"),
            ("<em>94%</em>",   "clients renouvellent", "Taux de rétention 2024"),
        ],

        "story_label":   "Histoire du studio",
        "story_heading": "Comment la <em>scale-up</em> nous a contraints à repenser le design studio.",
        "story_paragraphs": [
            "Aura naît en 2019 de Luca Bianchi et Sofia Reggiani, "
            "ex product designers chez Spotify et Figma. L'idée initiale était "
            "simple : <em>nous ne voulons pas être une agence, nous ne voulons "
            "pas être freelances</em>. Nous voulions un studio qui travaille "
            "comme une équipe interne — avec les mêmes outils, les mêmes "
            "métriques, la même cadence — mais depuis l'extérieur.",
            "Les trois premières années ont été celles de l'apprentissage. Nous avons compris "
            "que les scale-up italiennes n'avaient pas besoin de <em>design</em> "
            "— elles avaient besoin de <em>delivery</em>. Nous avons donc recruté des "
            "engineers full-stack. Nous avons compris qu'il ne suffisait pas de la design "
            "review — il fallait le ship log. Nous avons compris que la valeur "
            "n'était pas dans les mockups, mais dans les métriques déplacées.",
            "Aujourd'hui Aura travaille avec 6-8 clients par an, en sprints de deux "
            "semaines, avec une métrique déclarée au début de chaque "
            "projet. Chaque projet publie un ship log interne que le "
            "client peut lire en temps réel. Si la métrique ne se "
            "déplace pas, nous travaillons gratuitement jusqu'à ce qu'elle se déplace. "
            "C'est la seule manière que nous connaissons de travailler.",
        ],

        "team_label":   "L'équipe",
        "team_heading": "Qui <em>livre</em> les projets.",
        "team_intro":
            "Chaque projet est suivi par une équipe dédiée de 3-5 personnes. "
            "Les équipes sont composées en fonction du type de projet et ne "
            "changent pas en cours de route. Qui commence le projet, le livre.",
        "team": [
            {
                "name": "Luca Bianchi",
                "role": "Co-fondateur · Head of product",
                "bio":  "Ex Spotify (Stockholm · 2014-2018) et Figma "
                        "(San Francisco · 2018-2019). Il a dirigé "
                        "l'équipe growth design pour le marché EU. "
                        "Il s'occupe de la définition des sprints.",
                "portrait": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=900&q=80&auto=format&fit=crop",
                "stack": ["Figma", "Linear", "PostHog", "Notion"],
            },
            {
                "name": "Sofia Reggiani",
                "role": "Co-fondatrice · Head of engineering",
                "bio":  "Ex Spotify (Stockholm) et Google (Londres). "
                        "Elle a dirigé la migration Next.js de deux plateformes "
                        "pan-européennes. Elle s'occupe de la stack delivery.",
                "portrait": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop",
                "stack": ["Next.js", "TypeScript", "Vercel", "Supabase"],
            },
            {
                "name": "Matteo Leone",
                "role": "Principal product designer",
                "bio":  "Huit ans chez Satispay (Milan) avant de "
                        "rejoindre Aura en 2022. Il a dessiné trois "
                        "onboardings pour fintechs italiennes avec >1M utilisateurs.",
                "portrait": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=900&q=80&auto=format&fit=crop",
                "stack": ["Figma", "Framer", "Stripe Elements"],
            },
        ],

        "values_label":   "Comment nous travaillons",
        "values_heading": "<em>Quatre règles</em> que nous ne négocions pas.",
        "values": [
            ("V.01", "Une <em>métrique</em> déclarée",
             "Chaque projet a une métrique claire définie au sprint zéro. "
             "Si elle ne bouge pas, nous restons jusqu'à ce qu'elle bouge."),
            ("V.02", "Une <em>équipe</em> dédiée",
             "Qui commence le projet, le livre. Zéro account manager, "
             "zéro handoff. Le designer qui dessine est celui qui ship."),
            ("V.03", "Un <em>ship-log</em> public",
             "Le client a accès en temps réel au ship-log interne. "
             "Il voit ce que nous avons livré, quand, pourquoi, et ce qui a échoué."),
            ("V.04", "Une <em>call</em> par semaine",
             "Une seule réunion synchrone par semaine, de 30 minutes, "
             "avec agenda écrit. Le reste est async sur Linear et Slack."),
        ],
    },

    # ── CAPABILITIES (services) ──────────────────────────────────
    "capabilities": {
        "chip": "4 domaines · 3-5 personnes par projet",
        "headline": "Quatre <em>capabilities</em>, toutes mesurées.",
        "standfirst":
            "Chaque capability a une méthode documentée, une métrique typique, "
            "une durée prévisible et une stack prédéfinie. Ce n'est pas un "
            "tarif — c'est un système qui nous permet de vous dire, au sprint zéro, "
            "à quoi vous attendre et quand.",

        "capabilities": [
            {
                "id": "CAP.01 · Product launch",
                "title": "Amener <em>un produit nouveau</em> à la première conversion.",
                "tagline": "Typique : 14 — 20 sem. · KPI · activation + first paid",
                "body":
                    "Pour scale-up ayant validé le problème (Seed / Série A) "
                    "et devant construire le produit payant. Nous partons du "
                    "sprint zéro (research + backlog), passons par le design "
                    "system + les trois premiers flows critiques, amenons en production "
                    "avec onboarding mesurable et pricing vivant.",
                "scope_label": "// scope",
                "scope": [
                    "Sprint zéro + user research",
                    "Design system (tokens + 60 composants)",
                    "Trois flows critiques en production",
                    "Onboarding self-serve",
                    "Pricing page live + Stripe",
                    "Analytics + funnel complet",
                    "Rollback + feature flag",
                    "Handover docs à l'équipe interne",
                ],
                "stack": ["Next.js 14", "TypeScript", "Figma", "Stripe", "Segment", "PostHog"],
            },
            {
                "id": "CAP.02 · Platform redesign",
                "title": "<em>Redesigner</em> un produit mature sans perdre d'utilisateurs.",
                "tagline": "Typique : 20 — 30 sem. · KPI · rétention + NPS",
                "body":
                    "Pour plateformes avec > 50k utilisateurs actifs ayant accumulé "
                    "de la dette UX. Nous partons d'un audit quantitatif + qualitatif, "
                    "construisons le nouveau système en parallèle, migrons "
                    "progressivement via feature flag. Aucun big-bang launch.",
                "scope_label": "// scope",
                "scope": [
                    "UX audit + quant analysis",
                    "30+ interviews utilisateurs",
                    "Migration progressive",
                    "A/B test sur cohortes",
                    "Design system evolution",
                    "Rollout par marché",
                    "Post-launch tuning · 8 sem.",
                    "Formation équipe interne",
                ],
                "stack": ["React", "Django", "PostHog", "Segment", "Split.io"],
            },
            {
                "id": "CAP.03 · Growth systems",
                "title": "<em>Systèmes de croissance</em> mesurables en 30 jours.",
                "tagline": "Typique : 8 — 16 sem. · KPI · conversion + LTV",
                "body":
                    "Pour produits déjà en production qui doivent croître. "
                    "Nous travaillons sur onboarding, pricing, rétention, referral. "
                    "Quick wins les 30 premiers jours (généralement +12% sur un funnel). "
                    "Systèmes à 90 jours (nouveaux expériments continus).",
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
                "title": "Portails <em>asset manager</em> et tableaux de bord corporate.",
                "tagline": "Typique : 24 — 36 sem. · KPI · task completion + time saved",
                "body":
                    "Pour entreprises B2B (proptech, fintech, healthtech) qui doivent "
                    "livrer des portails à leurs clients enterprise. SSO, rôles, "
                    "permissions, data warehouse intégré, exports structurés. "
                    "Ce n'est pas sexy, mais c'est là que se joue le renouvellement annuel.",
                "scope_label": "// scope",
                "scope": [
                    "Discovery avec 3-5 enterprises",
                    "Design tokens corporate",
                    "SSO (SAML · Okta · Azure)",
                    "Rôles + permissions granulaires",
                    "Data warehouse integration",
                    "Export multi-format",
                    "Audit log compliance",
                    "SLA 99.9% + monitoring",
                ],
                "stack": ["Next.js", "BigQuery", "Okta", "Datadog", "Sentry"],
            },
        ],

        "engagement_label":   "Trois modes d'engagement",
        "engagement_heading": "Du <em>projet unique</em> au <em>partenaire continu</em>.",
        "engagement_intro":
            "Nous choisissons le modèle d'engagement ensemble, au sprint zéro. "
            "Généralement 70% des projets partent en forfait, 30% en "
            "partenariat continu. Le temps & matériaux est rare, nous ne "
            "l'utilisons que pour des discoveries de moins de 3 semaines.",
        "engagement_tiles": [
            {
                "id":    "E.01 · Discovery",
                "title": "<em>Discovery sprint</em>",
                "range": "2 — 3 semaines · forfait",
                "body":  "Sprint zéro dédié. Research, audit, backlog, "
                         "estimation. Si l'on continue ensuite, il est reporté.",
                "includes": [
                    "User research (5-8 interviews)",
                    "Audit quantitatif (analytics)",
                    "Backlog initial",
                    "Estimation de delivery",
                    "Document partagé 30 pages",
                ],
            },
            {
                "id":    "E.02 · Fixed delivery",
                "title": "<em>Fixed delivery</em>",
                "range": "8 — 30 semaines · forfait",
                "body":  "Lancement ou redesign avec scope et budget fixes. "
                         "Le plus courant pour scale-up en Série A.",
                "includes": [
                    "Équipe dédiée 3-5 personnes",
                    "Sprints de 2 semaines",
                    "Ship-log partagé",
                    "Métrique déclarée",
                    "Rollback + feature flags",
                    "Handover documenté",
                ],
                "featured": True,
            },
            {
                "id":    "E.03 · Partner mode",
                "title": "<em>Partner mode</em>",
                "range": "Q-by-Q · renouvellement trimestriel",
                "body":  "Engagement continu pour plateformes matures. "
                         "Enveloppe jours/trimestre, roadmap partagée.",
                "includes": [
                    "Weekly ship cadence",
                    "Partage du backlog client",
                    "Experiment continu",
                    "Review trimestrielle KPI",
                    "SLA support + on-call",
                ],
            },
        ],

        "cta_label":   "Prochaine étape",
        "cta_heading": "Voyons-nous en <em>discovery</em>, 30 minutes.",
        "cta_primary": "Réserver une call",
    },

    # ── LAVORI (project_list) ────────────────────────────────────
    "lavori": {
        "chip": "Archives produits · 2019 — 2026",
        "headline": "<em>Quarante-sept</em> produits livrés. <em>Sept</em> en vitrine.",
        "standfirst":
            "Chaque cas a une métrique déclarée et mesurée. "
            "Nous montrons sept projets publics — les quarante autres sont "
            "sous NDA (courant en fintech et B2B). Archives complètes sur demande.",
        "tabs": ["Tous", "Product launch", "Redesign", "Growth", "B2B delivery"],
        "tabs_count_label": "// totaux archive",
        "tabs_count_value": "047",

        "projects": [
            {
                "slug": "casavo-retention-rework",
                "id":   "P.01",
                "cover":"https://images.unsplash.com/photo-1551434678-e076c223a692?w=1200&q=80&auto=format&fit=crop",
                "title":"Retention rework · plateforme d'achat immobilier",
                "client":"Casavo",
                "discipline":"PROPTECH · REDESIGN",
                "year": "2025",
                "blurb":
                    "Refonte complète du funnel de la recherche à la signature. "
                    "Migration progressive via feature flag sur 180k utilisateurs. "
                    "Aucun downtime, +18% rétention à 30 jours.",
                "kpi": [
                    ("<em>+18%</em>",  "rétention D30"),
                    ("<em>Δ+22</em>",  "NPS"),
                    ("<em>180K</em>",  "utilisateurs migrés"),
                ],
            },
            {
                "slug": "fastweb-plus-dashboard",
                "id":   "P.02",
                "cover":"https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80&auto=format&fit=crop",
                "title":"Tableau de bord résidentiel v2.3",
                "client":"Fastweb",
                "discipline":"TELCO · PLATFORM",
                "year": "2024",
                "blurb":
                    "Un nouveau tableau de bord pour 2.8M clients résidentiels. "
                    "SSO intégré, gestion des services, self-care complet. "
                    "Réduction des appels call center de −34% en six mois.",
                "kpi": [
                    ("<em>−34%</em>",   "appels CC"),
                    ("<em>2.8M</em>",   "utilisateurs"),
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
                    "D'un onboarding assisté (4 jours médians) à self-serve "
                    "(42 minutes). Compliance pan-EU, KYC intégré, "
                    "multi-currency day zero.",
                "kpi": [
                    ("<em>−54%</em>",       "TTFV"),
                    ("<em>+41%</em>",       "activation"),
                    ("<em>7 marchés</em>",  "day one"),
                ],
            },
            {
                "slug": "milkman-ship-sdk",
                "id":   "P.04",
                "cover":"https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=1200&q=80&auto=format&fit=crop",
                "title":"SDK de ship tracking pour retailers",
                "client":"Milkman",
                "discipline":"LOGISTICS · B2B",
                "year": "2024",
                "blurb":
                    "Un SDK JavaScript pour le tracking des livraisons intégré dans le "
                    "checkout de 40+ retailers. Un seul appel API, "
                    "branding côté retailer, mises à jour temps réel.",
                "kpi": [
                    ("<em>40+</em>",    "retailers"),
                    ("<em>1 appel</em>","API"),
                    ("<em>2MB</em>",    "bundle"),
                ],
            },
            {
                "slug": "lendlease-asset-portal",
                "id":   "P.05",
                "cover":"https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200&q=80&auto=format&fit=crop",
                "title":"Portail asset manager enterprise",
                "client":"Lendlease",
                "discipline":"PROPTECH · B2B",
                "year": "2024",
                "blurb":
                    "Un portail pour 80 asset managers italiens. SSO Azure, "
                    "rôles granulaires, data warehouse intégré avec "
                    "export multi-format. Compliance MiFID II incluse.",
                "kpi": [
                    ("<em>80</em>",       "asset mgr"),
                    ("<em>Azure SSO</em>","deploy"),
                    ("<em>MiFID II</em>", "compliance"),
                ],
            },
            {
                "slug": "fiscozen-onboarding-self-serve",
                "id":   "P.06",
                "cover":"https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=1200&q=80&auto=format&fit=crop",
                "title":"Onboarding self-serve auto-entrepreneurs",
                "client":"Fiscozen",
                "discipline":"FISCTECH · GROWTH",
                "year": "2024",
                "blurb":
                    "D'un onboarding assisté par expert-comptable à self-serve "
                    "complet. Réduction des délais d'activation et +47% de "
                    "conversion trial → paid dans les 90 premiers jours.",
                "kpi": [
                    ("<em>+47%</em>",   "trial → paid"),
                    ("<em>18 min</em>", "TTFV"),
                    ("<em>90 j</em>",   "mesure"),
                ],
            },
        ],

        "velocity_label":   "Velocity moyenne",
        "velocity_heading": "Comment nous <em>livrons</em> · douze derniers mois.",
        "velocity_body":
            "Les chiffres ci-dessous sont ceux que nous regardons en interne. "
            "Mis à jour chaque mois. Si la méthodologie derrière vous intéresse, "
            "nous en parlons volontiers en call de discovery.",
        "velocity_stats": [
            ("<em>8</em>",     "produits livrés · 2025"),
            ("<em>94%</em>",   "projets on-time"),
            ("<em>+26%</em>",  "KPI médian déplacé"),
            ("<em>47 j</em>",  "median time-to-ship"),
        ],
    },

    # ── SPRINT (process) ─────────────────────────────────────────
    "sprint": {
        "chip": "Méthodologie · 4 phases · télémétrie live",
        "headline": "Quatre <em>sprints</em>, de la discovery à l'échelle.",
        "standfirst":
            "Chaque projet traverse quatre phases déclarées. "
            "Durées prévisibles, livraisons claires, métriques publiques. "
            "Le client voit en temps réel où nous en sommes — et pourquoi.",

        "sprints": [
            {
                "id": "Sprint 0 · Signal",
                "duration": "1 semaine · fixe",
                "title": "<em>Comprendre</em> le problème avant de le dessiner.",
                "tagline": "// output: brief partagé + backlog initial",
                "body":
                    "Le sprint zéro est la phase la plus importante et la plus sous-estimée. "
                    "En cinq jours, nous écoutons les stakeholders (CEO, produit, "
                    "customer success), interviewons 5-8 utilisateurs réels, lisons "
                    "le dashboard actuel. À la fin, nous présentons un brief de "
                    "lecture + backlog d'hypothèses à tester.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Brief partagé · 24 pages",
                    "Backlog initial · Linear",
                    "Stakeholder map",
                    "Research summary · 5-8 interviews",
                    "Métrique déclarée + baseline",
                    "Estimation de delivery (sprint count)",
                ],
            },
            {
                "id": "Sprint 1 — 2 · Sketch",
                "duration": "4 semaines",
                "title": "<em>Prototyper</em> avant de construire.",
                "tagline": "// output: prototype testable + design system v0.1",
                "body":
                    "Les deux premiers sprints sont de prototypage rapide. "
                    "Nous construisons sur Figma + Framer les trois flows les plus critiques, "
                    "les testons avec des utilisateurs réels, itérons. En parallèle "
                    "nous démarrons le design system (tokens + 20 composants de base). "
                    "Le vrai code arrive au sprint 3.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Prototype Figma interactif",
                    "3 tours de user testing",
                    "Design system v0.1",
                    "Architecture de code",
                    "Plan d'A/B test",
                    "Design review au client",
                ],
            },
            {
                "id": "Sprint 3 — 5 · Ship",
                "duration": "6 semaines",
                "title": "<em>Amener en production</em>, incrémental.",
                "tagline": "// output: production live + première métrique",
                "body":
                    "Implémentation et delivery incrémental. Chaque vendredi, nous shippons "
                    "quelque chose en staging, chaque fin de sprint en production. "
                    "Feature flag + rollback à 1 clic. À la fin du sprint 5 "
                    "la première métrique déclarée doit s'être déplacée.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Staging deploy hebdomadaire",
                    "Production deploy bi-mensuel",
                    "Feature flags tous actifs",
                    "Rollback plan documenté",
                    "Monitoring · Datadog / Sentry",
                    "Première métrique déplacée",
                ],
            },
            {
                "id": "Sprint 6+ · Scale",
                "duration": "ongoing · trimestriel",
                "title": "<em>Scaler</em> · expérimentations continues.",
                "tagline": "// output: ship-log hebdo + review KPI trimestrielle",
                "body":
                    "Post-launch, nous entrons en mode scale. Expériments "
                    "hebdomadaires, expansion de features, optimisation post-launch. "
                    "Ship-log partagé public. Review trimestrielle des "
                    "métriques contre le plan.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Ship-log public",
                    "A/B weekly",
                    "Feature roadmap 6 mois",
                    "Review KPI trimestrielle",
                    "Formation équipe interne",
                    "Handover continu",
                ],
            },
        ],

        "mindset_label":   "Comment nous <em>pensons</em> le processus",
        "mindset_heading": "Trois <em>principes</em> de delivery.",
        "mindset_cards": [
            {
                "id": "P.01",
                "title": "<em>Télémétrie</em> visible",
                "body": "Le ship-log est public pour le client dès le jour zéro. "
                        "Ce que nous avons livré, quand, pourquoi. Zéro pièces sombres.",
            },
            {
                "id": "P.02",
                "title": "<em>Rollback</em> à 1 clic",
                "body": "Chaque feature est derrière un flag. Si quelque chose ne fonctionne "
                        "pas en production, nous la désactivons en moins de 60 secondes.",
            },
            {
                "id": "P.03",
                "title": "<em>Skin in the game</em>",
                "body": "Si la métrique déclarée ne se déplace pas, nous continuons "
                        "à travailler gratuitement. Nous l'avons fait quatre fois en huit ans.",
            },
        ],

        "stack_label":   "Stack de delivery",
        "stack_heading": "Avec quoi nous <em>livrons</em>.",
        "stack_intro":
            "La stack est choisie pour être fiable, rapide, et facile "
            "à passer à l'équipe interne du client. Zéro technologies boutique.",
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
        "chip": "3 slots ouverts · Q3 2026",
        "headline": "Racontez-nous le <em>projet</em>. Nous rappelons en moins de 48h.",
        "standfirst":
            "Ceci n'est pas un form. C'est un brief structuré en 3 étapes. "
            "Chaque réponse que vous recevez est écrite personnellement par Luca ou "
            "Sofia, non par un account manager. Si le projet nous correspond, "
            "le second message est déjà une proposition de call.",

        "form_heading": "// brief intake · 3 étapes",

        "step1": {
            "id": "STEP 01", "title": "Qui vous êtes", "sub": "Seulement les champs strictement nécessaires.",
        },
        "step2": {
            "id": "STEP 02", "title": "Le projet", "sub": "Plus c'est concret, plus la réponse est utile.",
        },
        "step3": {
            "id": "STEP 03", "title": "Quand", "sub": "Choisissez un slot indicatif — nous confirmons ensuite par e-mail.",
        },

        "labels": {
            "name":    "Nom et prénom",
            "role":    "Rôle",
            "company": "Entreprise / produit",
            "email":   "E-mail professionnel",
            "scope":   "Type de projet",
            "brief":   "Récit bref",
            "slot":    "Slot préféré",
        },
        "placeholders": {
            "name":    "Prénom Nom",
            "role":    "ex. Head of Product",
            "company": "Nom entreprise",
            "email":   "name@company.com",
            "brief":   "Ce que vous construisez, où vous en êtes (MRR, utilisateurs, round), quel est le problème que vous ressentez, comment vous mesurez le succès. Un brief concret reçoit une réponse concrète.",
        },
        "scope_options": [
            "Product launch · première mise en ligne",
            "Platform redesign · produit mature",
            "Growth systems · funnel / rétention",
            "B2B delivery · portail / dashboard",
            "Discovery sprint · 2-3 semaines",
            "Je ne suis pas encore sûr — parlons-en",
        ],

        "slots": [
            ("mon10", "Lun · 10:00"),
            ("mon15", "Lun · 15:00"),
            ("tue10", "Mar · 10:00"),
            ("tue15", "Mar · 15:00"),
            ("wed10", "Mer · 10:00"),
            ("wed15", "Mer · 15:00"),
            ("thu10", "Jeu · 10:00"),
            ("thu15", "Jeu · 15:00"),
            ("async", "Uniquement async par e-mail"),
        ],
        "form_submit_label": "Réserver la call",
        "form_submit_note":  "// réponse sous 48h ouvrées · tous fuseaux EU",

        "async_label":   "Vous préférez async ?",
        "async_heading": "Écrivez à <em>Luca</em> et <em>Sofia</em>.",
        "async_body":
            "Chaque e-mail arrive directement aux deux co-founders. "
            "Ce sont eux qui répondent — pas un account manager, pas un bot.",

        "studio_label":  "Le studio",

        "response_label": "// SLA de réponse",
        "response_rows": [
            ("Brief",           "< 48h"),
            ("Proposition",     "5 jours"),
            ("Sprint zéro",     "2 semaines"),
            ("Première métrique","6 semaines"),
        ],

        "boot_left":  "aura.studio · hello@aura.studio · +39 02 8728 4411",
        "boot_right": "// toujours ouverts au brief",
    },

    # ── POSTS (project_detail) ───────────────────────────────────
    "posts": [
        {
            "slug": "casavo-retention-rework",
            "id":   "P.01 · PROPTECH",
            "title": "Casavo · <em>+18% rétention</em> en trois mois.",
            "client": "Casavo · Proptech Milan",
            "discipline": "Redesign · rétention",
            "duration": "14 semaines",
            "year": "2025",
            "standfirst":
                "Le rework du funnel post-réservation de Casavo. "
                "Une optimisation incrémentale sur 180k utilisateurs, "
                "feature flag partout, zéro downtime. Trois mois plus tard : "
                "+18% rétention à 30 jours, NPS +22, MRR +840 K€.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1551434678-e076c223a692?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Les utilisateurs revenaient, mais ne convertissaient pas.",
            "problem_paragraphs": [
                "Casavo avait doublé ses utilisateurs actifs entre 2023 et 2024, "
                "mais la conversion de la <em>visite 1</em> à la <em>réservation de visite réelle</em> "
                "avait baissé de 12% — sur 180k utilisateurs actifs, cela signifiait ~21k "
                "réservations perdues chaque mois.",
                "L'équipe interne avait compris que le problème était dans le funnel "
                "post-inscription, mais n'avait pas la capacity pour tester 10+ hypothèses "
                "sérieusement sans ralentir la roadmap principale.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Un second funnel, en parallèle à l'ancien.",
            "solution_paragraphs": [
                "Au lieu de réécrire le funnel principal (risque trop élevé sur "
                "180k utilisateurs) nous avons construit un <em>second funnel expérimental</em> "
                "derrière un feature flag, disponible pour 10% du trafic. Six semaines "
                "de test, sept itérations, quatre flows testés.",
                "À la sixième itération, le second funnel battait le premier de 18% "
                "sur la rétention D30. Nous avons migré progressivement le reste des "
                "180k utilisateurs en trois semaines — palier 25%, puis 50%, puis 100%.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "Quatorze semaines, <em>sept sprints</em>.",
            "timeline_intro":
                "La timeline ci-dessous est la chronologie réelle de delivery — extraite "
                "du ship-log partagé avec Casavo.",
            "timeline_steps": [
                {"id": "S.00", "duration": "sem. 1",       "title": "<em>Signal</em>",  "body": "Research + audit funnel + backlog 14 hypothèses."},
                {"id": "S.01", "duration": "sem. 2-3",     "title": "<em>Sketch</em>",  "body": "Prototypes de 4 flows alternatifs, 8 interviews."},
                {"id": "S.02", "duration": "sem. 4-6",     "title": "<em>Ship</em>",    "body": "Second funnel live à 10%, premier A/B test."},
                {"id": "S.03", "duration": "sem. 7-11",    "title": "<em>Iterate</em>", "body": "6 itérations weekly. Cohortes chaque vendredi."},
                {"id": "S.04", "duration": "sem. 12-14",   "title": "<em>Migrate</em>", "body": "Rollout 25% → 50% → 100%. Zéro downtime."},
            ],

            "results_label": "// results",
            "results_heading": "Quatre <em>métriques déplacées</em>.",
            "results_stats": [
                ("<em>+18%</em>",     "rétention D30",            "de 42% à 49.6% (90 j rolling)"),
                ("<em>Δ +22</em>",    "NPS",                      "de 31 à 53 dans les 3 mois post-rollout"),
                ("<em>+840 K€</em>",  "MRR incrémental",          "projection à 12 mois"),
                ("<em>0</em>",        "downtime durant rollout",  "180k utilisateurs, zéro erreurs 5xx extra"),
            ],

            "quote": "En trois mois ils ont compris notre produit mieux que des consultants qui y avaient travaillé un an. Et ils ont shippé.",
            "quote_author": "Marianna Colombo",
            "quote_role":   "VP Product · Casavo",

            "next_label":   "// next case",
            "next_heading": "→ voir tous les <em>travaux</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ réserver une <em>call</em>",
        },
        {
            "slug": "fastweb-plus-dashboard",
            "id":   "P.02 · TELCO",
            "title": "Fastweb · <em>−34% appels CC</em> en 6 mois.",
            "client": "Fastweb · Telco Italie",
            "discipline": "Platform redesign",
            "duration": "26 semaines",
            "year": "2024",
            "standfirst":
                "Un nouveau tableau de bord résidentiel pour 2.8M clients. "
                "Gestion des services, paiements, auto-care, SSO. "
                "Résultat : −34% d'appels au call center, NPS 64 post-launch, "
                "migration complète en six mois sans downtime.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Un tableau de bord de 2014 dans un monde de 2024.",
            "problem_paragraphs": [
                "Le tableau de bord résidentiel de Fastweb avait été construit en 2014 "
                "et re-skinné trois fois sans toucher à la structure. Le résultat : "
                "task completion à 41%, 2.1M d'appels au call center par an pour "
                "des opérations qui auraient dû être en self-care.",
                "L'objectif : reconstruire sans perdre d'utilisateurs, sans downtime, "
                "et sans big-bang launch — nous avons eu 26 semaines.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Micro-frontend + migration progressive.",
            "solution_paragraphs": [
                "Nous avons construit le nouveau tableau de bord comme <em>micro-frontend</em> "
                "à côté de l'ancien — même domaine, même SSO, même backend. "
                "Les utilisateurs ont été migrés par cluster géographique (Lombardie, "
                "Piémont, Latium...) en six phases.",
                "Chaque cluster était monitoré pendant 2 semaines. Si NPS et task "
                "completion meilleurs que l'ancien, on passait au cluster suivant. "
                "Si pires, on revenait 24 heures en arrière et on fixait.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "<em>Six phases</em> de rollout géographique.",
            "timeline_intro":
                "Chaque phase du rollout avait 2 semaines de monitoring avant "
                "la phase suivante. La plus difficile a été la troisième.",
            "timeline_steps": [
                {"id": "R.01", "duration": "Semaine 10", "title": "Piémont",       "body": "400k utilisateurs. NPS +18. Go."},
                {"id": "R.02", "duration": "Semaine 14", "title": "Lombardie",     "body": "680k utilisateurs. NPS +22. Go."},
                {"id": "R.03", "duration": "Semaine 18", "title": "Vénétie",       "body": "480k utilisateurs. NPS +9. Hold 1 sem."},
                {"id": "R.04", "duration": "Semaine 22", "title": "Latium",        "body": "520k utilisateurs. NPS +21. Go."},
                {"id": "R.05", "duration": "Semaine 26", "title": "Reste Italie",  "body": "720k utilisateurs. NPS +19. Complete."},
            ],

            "results_label": "// results",
            "results_heading": "Six mois, <em>quatre chiffres</em>.",
            "results_stats": [
                ("<em>−34%</em>",     "appels call center", "~720k appels en moins / an"),
                ("<em>NPS 64</em>",   "post-launch",         "vs 32 pre-launch"),
                ("<em>2.8M</em>",     "utilisateurs migrés", "100% sans downtime"),
                ("<em>+41% TC</em>",  "task completion",      "de 41% à 82%"),
            ],

            "quote": "Aura est le seul studio qui m'a présenté un plan de rollback pour chaque sprint. Nous avons utilisé le rollback deux fois. Zéro drama.",
            "quote_author": "Stefano Petri",
            "quote_role":   "Head of digital · Fastweb",

            "next_label":   "// next case",
            "next_heading": "→ voir tous les <em>travaux</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ réserver une <em>call</em>",
        },
        {
            "slug": "soldo-corporate-onboarding",
            "id":   "P.03 · FINTECH",
            "title": "Soldo · onboarding de <em>4 jours</em> à <em>42 minutes</em>.",
            "client": "Soldo · Fintech pan-EU",
            "discipline": "Product launch · onboarding",
            "duration": "18 semaines",
            "year": "2025",
            "standfirst":
                "La refonte complète de l'onboarding corporate de Soldo. "
                "D'un processus assisté (4 jours) à self-serve complet "
                "(42 minutes) dans 7 marchés européens, avec KYC, multi-currency "
                "et compliance. Résultat : +41% activation, −54% time to value.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1559028012-481c04fa702d?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Un onboarding qui exigeait un humain.",
            "problem_paragraphs": [
                "L'onboarding Soldo en 2024 exigeait 4 jours médians "
                "(2 pour le KYC, 1 pour le setup multi-currency, 1 pour l'activation "
                "des cartes). Chaque onboarding consommait 1.2 heure de customer success. "
                "Sur 2.800 onboardings/mois, le coût était insoutenable.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Onboarding guidé, zéro humain.",
            "solution_paragraphs": [
                "Nous avons redessiné tout le flow en <em>self-serve guided</em> : "
                "le client charge les documents une seule fois, le KYC tourne en background, "
                "la configuration multi-currency est pré-remplie selon le marché de résidence.",
                "Humain uniquement sur demande explicite (lien dans chaque étape). "
                "Le CSAT n'a pas baissé — il a grimpé de 22%.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "Neuf <em>sprints</em>, sept marchés.",
            "timeline_intro":
                "Les 4 premiers sprints sur UK (marché le plus mature). "
                "Les 5 autres sur rollout cross-market.",
            "timeline_steps": [
                {"id": "S.01", "duration": "sem. 1-2",  "title": "<em>Discovery</em>",    "body": "120 customer success calls analysées."},
                {"id": "S.02", "duration": "sem. 3-6",  "title": "<em>UK beta</em>",      "body": "Nouveau flow live sur UK. +28% activation."},
                {"id": "S.03", "duration": "sem. 7-10", "title": "<em>DE · NL · FR</em>", "body": "3 marchés ajoutés. Fix multi-currency."},
                {"id": "S.04", "duration": "sem. 11-14","title": "<em>IT · ES · IE</em>", "body": "3 marchés ajoutés. Fix langue."},
                {"id": "S.05", "duration": "sem. 15-18","title": "<em>Scale</em>",        "body": "Optimisation continue. A/B weekly."},
            ],

            "results_label": "// results",
            "results_heading": "Trois <em>métriques core</em> déplacées.",
            "results_stats": [
                ("<em>42 min</em>",  "time to activate", "depuis 4 jours médians"),
                ("<em>+41%</em>",    "activation rate",  "trial → paid"),
                ("<em>+22%</em>",    "CSAT",             "post-onboarding"),
                ("<em>7</em>",       "marchés",          "day one go-live"),
            ],

            "quote": "Le résultat : aujourd'hui notre équipe d'onboarding corporate est 60% plus petite mais gère 3x plus d'entreprises. Soldo ne serait pas à son niveau actuel sans ce rework.",
            "quote_author": "Rebecca Hughes",
            "quote_role":   "VP Growth · Soldo",

            "next_label":   "// next case",
            "next_heading": "→ voir tous les <em>travaux</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ réserver une <em>call</em>",
        },
        {
            "slug": "milkman-ship-sdk",
            "id":   "P.04 · LOGISTICS",
            "title": "Milkman · <em>SDK tracking</em> pour 40+ retailers.",
            "client": "Milkman · Logistics Italie",
            "discipline": "B2B delivery · SDK",
            "duration": "22 semaines",
            "year": "2024",
            "standfirst":
                "Un SDK JavaScript white-label pour tracking des livraisons, "
                "intégré dans le checkout de 40+ retailers italiens. "
                "Un seul appel API, branding côté retailer, "
                "mises à jour temps réel. Bundle sous les 2MB gzippés.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "40 retailers, 40 intégrations custom.",
            "problem_paragraphs": [
                "Milkman gérait les livraisons de plus de 40 retailers italiens — "
                "Esselunga, Coop, Unieuro, Mediaworld — chacun avec sa propre "
                "intégration custom. Chaque nouveau retailer exigeait 8-12 "
                "semaines d'engineering.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Un SDK, un appel API.",
            "solution_paragraphs": [
                "Nous avons construit un SDK JavaScript white-label. "
                "Un retailer n'a qu'une chose à faire : appeler <em>milkman.track(orderId)</em>. "
                "Le SDK gère le branding côté retailer (couleurs, font, logo), "
                "les langues, les mises à jour temps réel via WebSocket.",
                "Intégration moyenne : 3 heures. Avant : 8-12 semaines.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "<em>Cinq</em> sprints du SDK au 40ᵉ retailer.",
            "timeline_intro": "Premier retailer (Esselunga) au sprint 3. Les 39 autres en self-service.",
            "timeline_steps": [
                {"id": "S.01", "duration": "sem. 1-4",   "title": "<em>SDK core</em>",        "body": "Architecture, bundle, branding."},
                {"id": "S.02", "duration": "sem. 5-10",  "title": "<em>Esselunga beta</em>",  "body": "Premier retailer live. 2 bugs critiques."},
                {"id": "S.03", "duration": "sem. 11-14", "title": "<em>Unieuro · Coop</em>",  "body": "2 retailers ajoutés. Zéro bug."},
                {"id": "S.04", "duration": "sem. 15-18", "title": "<em>Docs + portal</em>",   "body": "Self-serve onboarding."},
                {"id": "S.05", "duration": "sem. 19-22", "title": "<em>Scale</em>",           "body": "40ᵉ retailer intégré en self-service."},
            ],

            "results_label": "// results",
            "results_heading": "De <em>8 semaines</em> à <em>3 heures</em>.",
            "results_stats": [
                ("<em>40+</em>",     "retailers live",      "Au go-live du sixième mois"),
                ("<em>3 heures</em>","time-to-integrate",   "Depuis 8-12 semaines médianes"),
                ("<em>1.8 MB</em>",  "bundle gzippé",       "Sous le plafond de 2 MB demandé"),
                ("<em>0</em>",       "downtime",            "Du premier sprint à aujourd'hui"),
            ],

            "quote": "Le SDK nous a permis d'ouvrir trois marchés européens en six mois. Avant, c'était impossible.",
            "quote_author": "Antonio Perini",
            "quote_role":   "CEO · Milkman",

            "next_label":   "// next case",
            "next_heading": "→ voir tous les <em>travaux</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ réserver une <em>call</em>",
        },
        {
            "slug": "lendlease-asset-portal",
            "id":   "P.05 · PROPTECH",
            "title": "Lendlease · <em>portail enterprise</em> pour 80 asset managers.",
            "client": "Lendlease · Proptech EU",
            "discipline": "B2B delivery",
            "duration": "30 semaines",
            "year": "2024",
            "standfirst":
                "Un portail enterprise pour 80 asset managers italiens. "
                "SSO Azure, rôles granulaires, data warehouse intégré, "
                "compliance MiFID II. Ce n'est pas sexy — c'est là que se joue le renouvellement.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1600&q=80&auto=format&fit=crop",

            "problem_label":"// problem",
            "problem_heading":"Un portail enterprise sans aucun self-serve.",
            "problem_paragraphs":[
                "80 asset managers utilisaient un portail de 2016 qui exigeait "
                "une assistance humaine pour chaque action. Chaque asset manager consommait "
                "~6 heures / semaine de customer success. Le re-contracting trimestriel "
                "était en risque.",
            ],
            "solution_label":"// solution",
            "solution_heading":"Dashboard self-serve + export automatisé.",
            "solution_paragraphs":[
                "Nous avons reconstruit le portail comme plateforme self-serve. "
                "SSO Azure, rôles granulaires (analyste, manager, compliance), "
                "data warehouse intégré avec export multi-format "
                "(PDF, XLSX, CSV, MiFID II XML).",
            ],
            "timeline_label":"// timeline",
            "timeline_heading":"<em>Dix</em> sprints, <em>trois</em> rollouts par cluster.",
            "timeline_intro": "Rollout par cluster d'asset managers (20/30/30).",
            "timeline_steps":[
                {"id":"S.01","duration":"sem. 1-4",  "title":"<em>Discovery</em>",    "body":"Interviews de 12 asset managers."},
                {"id":"S.02","duration":"sem. 5-14", "title":"<em>SSO + rôles</em>",  "body":"Azure SSO + RBAC complet."},
                {"id":"S.03","duration":"sem. 15-22","title":"<em>Dashboard</em>",    "body":"Core dashboard + analytics."},
                {"id":"S.04","duration":"sem. 23-28","title":"<em>Export</em>",       "body":"Multi-format + MiFID II."},
                {"id":"S.05","duration":"sem. 29-30","title":"<em>Rollout</em>",      "body":"80 asset managers migrés."},
            ],
            "results_label":"// results",
            "results_heading":"<em>80</em> asset managers, <em>zéro</em> appel.",
            "results_stats":[
                ("<em>80</em>",      "asset managers migrés","100% avant fin du rollout"),
                ("<em>−92%</em>",    "appels CS",            "6 heures → 28 min /sem."),
                ("<em>100%</em>",    "recontracting",        "Sur 2 ans consécutifs"),
                ("<em>MiFID II</em>","compliance",           "Audit passé du premier coup"),
            ],
            "quote":"Le portail est devenu la raison principale pour laquelle nos asset managers renouvellent.",
            "quote_author":"Valentina Greco",
            "quote_role":"Head of product · Lendlease IT",
            "next_label":"// next case",
            "next_heading":"→ voir tous les <em>travaux</em>",
            "cta_label":"// start a project",
            "cta_heading":"→ réserver une <em>call</em>",
        },
        {
            "slug": "fiscozen-onboarding-self-serve",
            "id":   "P.06 · FISCTECH",
            "title": "Fiscozen · <em>+47%</em> de trial à paid.",
            "client": "Fiscozen · Fisctech Milan",
            "discipline": "Growth systems",
            "duration": "16 semaines",
            "year": "2024",
            "standfirst":
                "D'un onboarding assisté par expert-comptable à self-serve complet "
                "pour auto-entrepreneurs. +47% de conversion trial → paid en 90 jours.",
            "meta_client_label":"// client",
            "meta_discipline_label":"// capability",
            "meta_duration_label":"// duration",
            "meta_year_label":"// delivered",
            "cover_image": "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=1600&q=80&auto=format&fit=crop",
            "problem_label":"// problem",
            "problem_heading":"Un onboarding qui exigeait un expert-comptable.",
            "problem_paragraphs":["Chaque auto-entrepreneur en essai avait besoin de 30 min avec un expert-comptable pour commencer. Bottleneck critique."],
            "solution_label":"// solution",
            "solution_heading":"Guided onboarding self-serve, expert-comptable optionnel.",
            "solution_paragraphs":["Formulaire guidé qui pré-remplit le code ATECO à partir du récit libre de l'utilisateur, intégré à InfoCamere."],
            "timeline_label":"// timeline",
            "timeline_heading":"<em>Huit</em> sprints, KPI hebdomadaire.",
            "timeline_intro":"Priorité : time-to-first-value sous les 20 minutes.",
            "timeline_steps":[
                {"id":"S.01","duration":"sem. 1-3",  "title":"<em>Research</em>", "body":"20 interviews d'auto-entrepreneurs débutants."},
                {"id":"S.02","duration":"sem. 4-8",  "title":"<em>Flow v1</em>",  "body":"Premier onboarding self-serve. 28% activation."},
                {"id":"S.03","duration":"sem. 9-12", "title":"<em>Iterate</em>",  "body":"4 A/B tests. 41% activation."},
                {"id":"S.04","duration":"sem. 13-16","title":"<em>Scale</em>",    "body":"Rollout 100%. 47% post-90j."},
            ],
            "results_label":"// results",
            "results_heading":"<em>Quatre</em> mois, <em>trois</em> métriques.",
            "results_stats":[
                ("<em>+47%</em>",   "trial → paid","de 21% à 31% conv. à 90 j"),
                ("<em>18 min</em>", "TTFV",        "depuis 4 heures avec expert-comptable"),
                ("<em>−38%</em>",   "CAC",         "customer acquisition cost"),
                ("<em>+2.1x</em>",  "volume",      "trials hebdomadaires post-rollout"),
            ],
            "quote":"L'équipe d'Aura a shippé plus d'A/B tests en 16 semaines que nous n'en avons fait les 2 années précédentes.",
            "quote_author":"Vittorio Amato",
            "quote_role":"CEO · Fiscozen",
            "next_label":"// next case",
            "next_heading":"→ voir tous les <em>travaux</em>",
            "cta_label":"// start a project",
            "cta_heading":"→ réserver une <em>call</em>",
        },
    ],
}
