"""Phase 2g3.7 · Session 53 · Juris — FR native-voice tree. Advisory-modern tech boutique voice."""
from __future__ import annotations

from typing import Any


JURIS_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Accueil",     "kind": "home"},
        {"slug": "approccio",  "label": "Approche",    "kind": "about"},
        {"slug": "servizi",    "label": "Services",    "kind": "services"},
        {"slug": "settori",    "label": "Secteurs",    "kind": "team"},
        {"slug": "insights",   "label": "Insights",    "kind": "blog_list"},
        {"slug": "contatti",   "label": "Contact",     "kind": "contact"},
    ],

    "site": {
        "logo_initial": "M",
        "logo_word":    "Martini & Partners",
        "tag":          "Conseil juridique · depuis 2018",
        "phone":        "hello@martinipartners.legal",
        "email":        "hello@martinipartners.legal",
        "address":      "Via Solferino 40 · 20121 Milan",
        "hours_compact":"Rendez-vous stratégique · Lun – Ven · 09:00 – 19:00",
        "hours_footer_rows": [
            "Visio depuis notre dashboard",
            "Réponse sous 2 heures ouvrées",
        ],
        "license":      "Barreau de Milan n° MI18224 · TVA IT10123540967",
        "nav_cta":      "Prendre un rendez-vous stratégique",
        "footer_intro":
            "Martini & Partners est le cabinet qui réunit droit, technologie "
            "et stratégie pour les startups, PME et fondateurs. Tarifs "
            "clairs, délais définis, un dashboard partagé.",
        "foot_studio":  "Le cabinet",
        "foot_pages":   "Pages",
        "foot_contact": "Contact",
        "foot_offices": "Bureaux",
        "offices_footer_rows": [
            "Milan · via Solferino 40",
            "Turin · via Roma 324",
            "Bologne · via Indipendenza 18",
        ],
        "post_date_label":    "Publié",
        "post_reading_label": "Lecture",
        "post_author_label":  "Par",
        "post_topic_label":   "Pratique",
        "post_back_label":    "Tous les insights",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Martini & Partners · Milan · Turin · Bologne",
        "headline":    "Le droit, <em>de votre côté.</em>",
        "intro":
            "Nous accompagnons startups, PME et fondateurs dans les "
            "décisions juridiques qui font avancer l'entreprise — avec "
            "des délais clairs, des honoraires transparents et un dashboard "
            "partagé où vous suivez chaque étape du dossier.",
        "primary_cta":    "Prendre un rendez-vous stratégique",
        "primary_href":   "contatti",
        "secondary_cta":  "Notre façon de travailler",
        "secondary_href": "approccio",

        "sprint_chip":     "Rendez-vous stratégique · Prochain créneau · 17 avril",
        "sprint_chip_cta": "Réserver →",

        "sectors_label":   "Secteurs",
        "sectors_heading": "Six pratiques, une seule <em>méthode</em>.",
        "sectors_intro":
            "Chaque pratique est pilotée par un binôme associé + legal ops. "
            "Le premier associé avec qui vous échangez est celui qui "
            "signera le mandat — pas de passage de relais, pas de BDR, "
            "pas de pitch deck.",
        "sectors": [
            ("01", "Startup & Tech",
             "Levée de fonds, cap table, PI, conformité RGPD et règlement sur l'IA pour les entreprises digitales."),
            ("02", "PME & Famille",
             "Transmission, gouvernance, pactes d'actionnaires et M&A mid-market."),
            ("03", "Droit social & RH",
             "Contrats, licenciements, avantages, BSA/AGA/BSPCE et télétravail transfrontalier."),
            ("04", "Contrats B2B",
             "SaaS, licensing, partenariats, due diligence fournisseurs et MSA en anglais."),
            ("05", "Règlement des différends",
             "Médiation, arbitrage, MARD et contentieux stratégique."),
            ("06", "Privacy & IA",
             "RGPD, règlement sur l'IA, cartographie des données, AIPD et politiques pour entreprises data-driven."),
        ],

        "process_label":   "Notre méthode",
        "process_heading": "Du brief au <em>premier acte</em> en deux semaines.",
        "process_intro":
            "Nous ne vendons pas des heures, nous vendons des résultats. "
            "La méthode est la même pour chaque client — de la seed qui "
            "boucle son premier tour à la PME au quatrième mandat "
            "consécutif. Trois étapes, aucun mystère.",
        "process": [
            ("S.01", "Appel de découverte",
             "30 min en visio · nous cadrons le problème, nous ne vendons pas le service."),
            ("S.02", "Devis clair",
             "Délais, phases, coût fixe ou plafonné — tout écrit, aucune surprise."),
            ("S.03", "Dashboard en direct",
             "Suivi en temps réel des actes, échéances, documents et heures travaillées."),
        ],

        "metric_label":    "Les chiffres du cabinet",
        "metric_heading":  "Huit ans sur le terrain, trois villes, une centaine de mandats par an.",
        "metric_strip": [
            ("180+", "entreprises accompagnées"),
            ("14",   "jours · délai médian avant premier acte"),
            ("4,9",  "★ satisfaction clients"),
            ("0",    "€ frais de setup, toujours"),
        ],

        "trust_label": "Nous avons accompagné ces douze derniers mois",
        "trust_logos": [
            "UNE FINTECH MILANAISE · SEED",
            "UN GROUPE FAMILIAL VÉNITIEN · TRANSMISSION",
            "UN SAAS B2B TURINOIS · SÉRIE A",
            "UNE PME BOLOGNAISE · M&A TRANSFRONTALIER",
            "UNE MARKETPLACE ROMAINE · POLITIQUE IA",
            "UNE SCALE-UP FLORENTINE · BSA/AGA",
        ],

        "insights_label":   "Insights · cette semaine",
        "insights_heading": "Ce que nous lisons <em>au cabinet</em>.",
        "insights_intro":
            "Les notes que nous écrivons quand une règle change. Nos "
            "clients les lisent le matin avec le café — pas de newsletter, "
            "pas de lead magnet, pas de séquence automatisée.",
        "insights_link":    "Tous les insights →",
        "insights_link_href":"insights",
        "insights": [
            ("17 avr", "Règlement sur l'IA · ce qui change pour les PME italiennes", "ai-act-pmi-italiane"),
            ("14 avr", "BSA/AGA 2026 · nouveau régime fiscal",                       "stock-option-2026"),
            ("11 avr", "Télétravail transfrontalier · trois scénarios",               "smart-working-confine"),
        ],

        "cta_label":     "Prêts à en parler ?",
        "cta_heading":   "Trente minutes, en visio, sans engagement.",
        "cta_intro":
            "Le premier échange est avec un associé, pas avec un BDR. "
            "Si le dossier n'est pas dans notre pratique, nous vous "
            "orientons vers le bon cabinet — même si vous ne travaillez "
            "jamais avec nous.",
        "cta_primary":      "Prendre un rendez-vous stratégique",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Lire notre méthode",
        "cta_secondary_href":"approccio",
    },

    # ─── APPROCCIO (about) ──────────────────────────────────────
    "approccio": {
        "eyebrow":  "Notre méthode · 2018 — 2026",
        "headline": "Nous ne vendons pas d'heures, <em>nous vendons des résultats.</em>",
        "intro":
            "Nous avons fondé le cabinet en 2018 par réelle frustration — "
            "deux associés qui avaient passé dix ans dans des cabinets "
            "d'affaires internationaux à Milan et ne supportaient plus "
            "la facturation à l'heure, les collaborateurs juniors laissés "
            "de côté et les outils de gestion juridique dignes des années "
            "quatre-vingt-dix. Nous avons ouvert Martini & Partners pour faire autrement.",

        "manifesto_label":   "Manifeste",
        "manifesto_heading": "Quatre principes, <em>non négociables</em>.",
        "manifesto_intro":
            "Nous les inscrivons en première page de la convention "
            "d'honoraires. Ce ne sont pas des slogans, ce sont des règles "
            "opérationnelles — si l'une de ces quatre saute, nous ne "
            "travaillons pas avec vous (ou vous ne travaillez plus avec nous).",
        "manifesto": [
            ("01", "Le problème d'abord, les honoraires ensuite",
             "L'appel de découverte est gratuit. Nous écrivons le devis "
             "uniquement après avoir compris si le problème relève de "
             "notre pratique et si la solution vaut les honoraires. "
             "Si ce n'est pas notre domaine, nous vous orientons vers "
             "le bon cabinet — sans commission d'apport."),
            ("02", "Tarif écrit, jamais horaire",
             "Chaque mandat a un coût fixe ou un plafond. Nous n'utilisons "
             "la facturation horaire que pour les urgences non planifiables, "
             "toujours signalées avant de commencer. Aucune ligne surprise, "
             "aucune entrée vague \"suivi du dossier\"."),
            ("03", "Un associé, du premier acte au dernier",
             "L'associé rencontré en découverte est celui qui signe "
             "l'acte final. L'équipe tourne par spécialisation, jamais "
             "par seniorité — vous ne trouverez jamais un collaborateur "
             "junior inconnu sur votre dossier sans votre approbation préalable."),
            ("04", "Dashboard partagé, toujours",
             "Chaque client dispose d'un espace dédié avec l'état des "
             "dossiers, les documents, les actes déposés, les heures "
             "travaillées et la timeline des échéances. Nous n'envoyons "
             "pas de PDF par e-mail — tout passe par le dashboard, "
             "toujours à jour, toujours exportable."),
        ],

        "story_label":   "L'histoire",
        "story_heading": "Huit ans, trois villes, une seule méthode.",
        "story": [
            ("2018", "Fondation à Milan",
             "Giorgia Martini (ex-DLA Piper) et Davide Romano (ex-Bird & Bird) "
             "ouvrent le cabinet via Solferino avec trois mandats déjà "
             "signés par des clients de leur pratique précédente."),
            ("2020", "Premier dashboard interne",
             "Nous construisons avec un product manager ex-Zalando la "
             "première version du dashboard client. L'idée d'en faire "
             "la signature de la méthode Martini & Partners naît ici."),
            ("2022", "Ouverture du bureau de Turin",
             "Nous ouvrons le deuxième bureau à Turin pour suivre de près "
             "les mandats scale-up piémontaises — aujourd'hui la moitié "
             "des dossiers startup du cabinet passent par ce bureau."),
            ("2024", "Ouverture du bureau de Bologne",
             "Le troisième bureau à Bologne couvre le corridor Emilie-"
             "Romagne, avec un focus PME familiales et M&A mid-market. "
             "En 2025 les premiers dossiers règlement sur l'IA en sortent aussi."),
            ("2026", "Cabinet à la bonne taille",
             "Aujourd'hui nous sommes huit avocats et deux legal ops. "
             "Nous ne comptons pas grandir au-delà — nous préférons "
             "sélectionner les mandats plutôt qu'ouvrir un quatrième bureau."),
        ],

        "dashboard_label":   "Le dashboard client",
        "dashboard_heading": "Suivez votre dossier comme <em>un déploiement</em>.",
        "dashboard_intro":
            "Chaque client accède à un espace chiffré avec ses dossiers, "
            "documents, échéances et heures réellement travaillées. "
            "Inspiré plus par Linear que par un portail juridique — "
            "parce que nous travaillons pour des gens qui utilisent "
            "Linear dans leur propre métier.",
        "dashboard_features": [
            ("État des dossiers",       "Chaque dossier a un kanban · statut · responsable · prochaine échéance."),
            ("Documents versionnés",    "Actes déposés, brouillons, annexes — avec historique et commentaires en ligne."),
            ("Heures travaillées, en clair","Les heures de chaque associé et legal ops, actualisées chaque vendredi soir."),
            ("Échéances calendrier",    "Chaque échéance est un événement · synchronisable avec Google Calendar."),
            ("Export comptable",        "Un clic pour l'export facture + notes de frais pour votre comptable."),
            ("Accès partagé",           "Invitez le DAF, le CEO, l'expert-comptable — avec permissions granulaires."),
        ],
        "dashboard_mock": {
            "url":         "martini-partners.dashboard",
            "sidebar":     ["Dossiers", "Actes", "Heures", "Échéances", "Équipe"],
            "sidebar_active_index": 0,
            "columns": [
                {"label": "Découverte",
                 "cards": [
                     {"title": "Fintech · seed",      "accent": False},
                     {"title": "PME · transmission",  "accent": False},
                 ]},
                {"label": "En cours",
                 "cards": [
                     {"title": "Scale-up · Série A",  "accent": True},
                     {"title": "SaaS · MSA",          "accent": False},
                     {"title": "M&A · due diligence", "accent": False},
                 ]},
                {"label": "Clôture",
                 "cards": [
                     {"title": "RH · BSA/AGA",        "accent": False},
                 ]},
            ],
        },

        "founders_label":   "Fondateurs",
        "founders_heading": "Deux avocats, <em>une idée partagée</em>.",
        "founders": [
            {
                "name":  "Avv. Giorgia Martini",
                "role":  "Managing partner · Startup & Tech",
                "bio":
                    "Douze ans chez DLA Piper Milan, département corporate. "
                    "A clôturé deux Séries A avec des fonds italiens et "
                    "un tour transfrontalier avec Orange Ventures. Pilote "
                    "la pratique startup et le bureau de Milan.",
                "credentials": [
                    "Bocconi (Droit '10)",
                    "LL.M. NYU '13",
                    "Membre · Italian Tech Alliance",
                ],
            },
            {
                "name":  "Avv. Davide Romano",
                "role":  "Co-fondateur · Contrats B2B",
                "bio":
                    "Dix ans chez Bird & Bird, département tech & comms. "
                    "Spécialiste du SaaS licensing, des MSA transfrontaliers "
                    "et des contrats pour plateformes marketplace. "
                    "Pilote le bureau de Turin et la pratique règlement sur l'IA.",
                "credentials": [
                    "Sapienza (Droit '11)",
                    "LL.M. Fordham '14",
                    "Contributeur · AIGA",
                ],
            },
        ],

        "offices_label": "Les bureaux",
        "offices": [
            ("Milan",    "Via Solferino 40 · 20121 · Brera",         "Siège · toutes les pratiques"),
            ("Turin",    "Via Roma 324 · 10123 · Centre",            "Bureau scale-up + corridor piémontais"),
            ("Bologne",  "Via Indipendenza 18 · 40121 · Centre",     "Bureau PME + corridor Émilie-Romagne"),
        ],

        "cta_heading": "Envie de voir le dashboard en direct ?",
        "cta_intro":
            "L'appel de découverte inclut un walkthrough de l'espace "
            "client. Nous vous montrons à quoi il ressemble, ce que "
            "vous voyez, ce que vous exportez et comment nous l'intégrons "
            "à votre stack (Notion, Slack, Google Workspace).",
        "cta_primary":      "Réserver l'appel de découverte",
        "cta_primary_href": "contatti",
    },

    # ─── SERVIZI (services) ─────────────────────────────────────
    "servizi": {
        "eyebrow":  "Services · 2026",
        "headline": "Sept offres, <em>délais garantis</em>, prix affichés.",
        "intro":
            "Les sept offres du cabinet. Chacune a un périmètre écrit, "
            "un délai indicatif et un coût fixe ou plafonné. Aucun tarif "
            "horaire générique, aucun \"à voir en call\".",

        "svc_duration_label": "Durée",
        "svc_price_label":    "Tarif",
        "svc_deliverables_label": "Livrables",
        "svc_engagement_label":   "Modalités",

        "services": [
            {
                "num":   "01",
                "title": "Startup Legal Sprint",
                "blurb":
                    "Tout le setup juridique pour une startup qui boucle "
                    "sa seed en trois semaines — statuts, pacte "
                    "d'actionnaires, term sheet, onboarding investisseurs "
                    "et cap table propre.",
                "deliverables": [
                    "Statuts et pacte d'actionnaires sur mesure",
                    "Term sheet et revue SAFE/OCA",
                    "Cap table sur Ledgy ou Capdesk",
                    "Onboarding des premiers investisseurs en visio",
                ],
                "duration":   "3 semaines",
                "price":      "6 500 € tout compris",
                "engagement": "Fixe · 60 % au lancement · 40 % au closing",
                "tier":       "Seed-ready",
            },
            {
                "num":   "02",
                "title": "Conseil M&A · PME",
                "blurb":
                    "Nous accompagnons les PME familiales dans les "
                    "opérations stratégiques — cession de parts, entrée "
                    "d'un fonds, M&A transfrontalier Italie-DACH. Côté "
                    "cédant ou acquéreur, jamais les deux dans le même dossier.",
                "deliverables": [
                    "Due diligence juridique et fiscale",
                    "Valorisation et rédaction du SPA",
                    "Négociation et accompagnement au closing",
                    "Post-closing · intégration 100 jours",
                ],
                "duration":   "12 – 24 semaines selon périmètre",
                "price":      "45 000 € base + 0,8 % de success fee",
                "engagement": "Mixte · fixe de base + success fee au closing",
                "tier":       "Mid-market",
            },
            {
                "num":   "03",
                "title": "Contract-as-a-Service · B2B",
                "blurb":
                    "Pour les SaaS et scale-ups qui signent des MSA "
                    "chaque semaine — une équipe dédiée gère la "
                    "rédaction, la négociation et l'archivage contractuel. "
                    "Un canal Slack, SLA 48 heures, forfait mensuel.",
                "deliverables": [
                    "Templates MSA / DPA / SOW personnalisés",
                    "Négociation redline avec les contreparties",
                    "Archive contrats sur Notion ou Juro",
                    "Reporting mensuel avec KPI délais et volumes",
                ],
                "duration":   "Abonnement mensuel · minimum 6 mois",
                "price":      "À partir de 3 200 € / mois",
                "engagement": "Récurrent · canal Slack + dashboard",
                "tier":       "Scale-ready",
            },
            {
                "num":   "04",
                "title": "Privacy & règlement sur l'IA · mise en conformité",
                "blurb":
                    "Audit RGPD complet + cartographie des risques "
                    "règlement sur l'IA pour entreprises data-driven. "
                    "AIPD, registre des traitements, politiques internes, "
                    "formation des équipes et readiness report pour "
                    "conseil d'administration ou investisseurs.",
                "deliverables": [
                    "Audit RGPD + registre des traitements mis à jour",
                    "Analyse de conformité règlement sur l'IA et cartographie par classe de risque",
                    "AIPD sur les processus critiques (max 4)",
                    "Formation de deux heures pour l'équipe opérationnelle",
                ],
                "duration":   "6 semaines",
                "price":      "12 500 € tout compris",
                "engagement": "Fixe · 50 % au lancement · 50 % à la livraison",
                "tier":       "Compliance",
            },
            {
                "num":   "05",
                "title": "BSA/AGA/BSPCE & avantages",
                "blurb":
                    "Conception et mise en place des plans d'actions "
                    "gratuites, BSA et BSPCE pour startups et scale-ups "
                    "— incluant le régime fiscal 2026 et les aspects "
                    "droit social pour contrats italiens et transfrontaliers.",
                "deliverables": [
                    "Plan BSA/AGA/BSPCE sur mesure",
                    "Règlement interne + onboarding collaborateurs",
                    "Régime fiscal 2026 documenté",
                    "Accords fonds pour lock-up et tag-along",
                ],
                "duration":   "4 semaines",
                "price":      "8 200 € base + 180 € / collaborateur onboardé",
                "engagement": "Fixe + per-seat sur onboarding",
                "tier":       "Scale-ready",
            },
            {
                "num":   "06",
                "title": "Règlement des différends",
                "blurb":
                    "Médiation, arbitrage et contentieux stratégique — "
                    "nous privilégions toujours la solution négociée, "
                    "mais quand il faut aller à l'audience nous le "
                    "faisons avec des associés dédiés.",
                "deliverables": [
                    "Évaluation du contentieux + mémo stratégique",
                    "Tentative de médiation ou MARD",
                    "Assistance en arbitrage ou au fond",
                    "Reporting hebdomadaire de l'état du litige",
                ],
                "duration":   "12 – 36 semaines selon complexité",
                "price":      "Devis sur périmètre écrit",
                "engagement": "Mixte · fixe par phase + success fee",
                "tier":       "Protection",
            },
            {
                "num":   "07",
                "title": "Fractional General Counsel",
                "blurb":
                    "Un associé dédié comme General Counsel à temps "
                    "partiel pour scale-ups et PME qui ont encore besoin "
                    "d'un niveau cabinet sans le coût d'un poste interne. "
                    "Deux à trois jours par mois, présence en conseil d'administration.",
                "deliverables": [
                    "Présence physique ou en visio 2-3 j / mois",
                    "Board book juridique et risk dashboard trimestriel",
                    "Revue des contrats clés + gouvernance",
                    "Escalade vers tous les bureaux Martini & Partners",
                ],
                "duration":   "Abonnement trimestriel · minimum 12 mois",
                "price":      "À partir de 5 400 € / mois",
                "engagement": "Récurrent · présence en CA",
                "tier":       "Scale-ready",
            },
        ],

        "process_label":   "Notre méthode",
        "process_heading": "Du brief au premier acte en deux semaines.",
        "process": [
            ("S.01", "Appel de découverte",  "30 min en visio · périmètre et adéquation."),
            ("S.02", "Devis écrit",          "Sous 5 j · coûts et délais fermes."),
            ("S.03", "Dashboard en direct",  "Kickoff sous 48 heures · tout est tracé."),
        ],

        "faq_label":   "Questions fréquentes",
        "faq_heading": "Ce que vous nous demandez en visio.",
        "faq": [
            ("Acceptez-vous les mandats en success fee variable ?",
             "Oui, mais uniquement sur les opérations stratégiques "
             "(M&A, levée, exit). Sur tout le reste nous travaillons "
             "au forfait ou en abonnement."),
            ("Comment gérez-vous les conflits d'intérêt ?",
             "Un conflict check est automatisé dans le dashboard. Nous "
             "n'acceptons jamais deux clients en concurrence directe "
             "dans le même secteur. La vérification a lieu avant "
             "l'appel de découverte, pas après."),
            ("Travaillez-vous avec des freelances et professionnels indépendants ?",
             "Oui, mais uniquement sur des offres spécifiques — BSA/AGA/BSPCE, "
             "Privacy & IA, et Contrats B2B. Sur le reste nous préférons "
             "les entreprises avec équipes."),
            ("Pouvez-vous signer un NDA en amont ?",
             "Oui, envoyez-nous votre NDA standard — nous le revoyons "
             "sous 24 heures. Sinon, nous utilisons notre template "
             "réciproque, disponible sur le dashboard."),
        ],

        "cta_heading": "Pas sûrs de l'offre à choisir ?",
        "cta_intro":
            "Écrivez-nous périmètre et délais — sous 24 heures nous "
            "vous orientons vers la bonne offre (ou nous vous disons "
            "que ce n'est pas notre domaine). Gratuit, sans engagement, "
            "réponse d'un associé réel.",
        "cta_primary":      "Envoyez-nous périmètre et délais",
        "cta_primary_href": "contatti",
    },

    # ─── SETTORI ────────────────────────────────────────────────
    "settori": {
        "eyebrow":  "Secteurs · là où nous évoluons naturellement",
        "headline": "Six secteurs, <em>une seule méthode</em>, des associés dédiés.",
        "intro":
            "Chaque secteur a un associé responsable et un legal ops en "
            "appui. Notre \"secteur\" n'est pas un claim marketing — "
            "c'est la liste des mandats que nous avons suffisamment "
            "travaillés pour être certains de ne pas devoir les apprendre sur votre dossier.",

        "sectors_label":   "Les six pratiques",
        "sectors_heading": "Là où nous avons <em>déjà résolu</em> des problèmes comme les vôtres.",

        "sectors": [
            {
                "num":   "01",
                "title": "Startup & Tech",
                "tagline": "Pour fondateurs au premier ou au troisième tour.",
                "pain_points": [
                    "Cap table et pacte d'actionnaires à remettre en ordre",
                    "SAFE, OCA ou term sheet à revoir avant signature",
                    "BSA/AGA/BSPCE avec le bon régime fiscal 2026",
                    "Conformité RGPD + règlement sur l'IA avant le pitch investisseurs",
                ],
                "signals": [
                    "8 Séries A bouclées ces 24 derniers mois",
                    "3 exits pilotés côté cédant",
                    "Associée dédiée · Avv. Giorgia Martini",
                ],
                "case_snippet":
                    "Nous avons accompagné une fintech milanaise dans sa "
                    "seed avec un fonds italien + un business angel UK — "
                    "cap table propre en trois semaines, closing en six.",
                "partner":    "Avv. Giorgia Martini",
                "legal_ops":  "Elena Vasile · legal ops lead",
            },
            {
                "num":   "02",
                "title": "PME & Famille",
                "tagline": "Pour entrepreneurs de deuxième ou troisième génération.",
                "pain_points": [
                    "Transmission avec plusieurs branches familiales",
                    "Pactes d'actionnaires obsolètes ou absents",
                    "Entrée d'un fonds minoritaire au capital",
                    "Gouvernance avec un CA encore informel",
                ],
                "signals": [
                    "14 transmissions familiales bouclées depuis 2019",
                    "5 entrées de fonds minoritaires dans des PME familiales",
                    "Associée dédiée · Avv. Chiara Belforte",
                ],
                "case_snippet":
                    "Un groupe familial vénitien du textile nous a confié "
                    "la transmission entre trois frères et un cousin au "
                    "second degré — pacte d'actionnaires bouclé en douze "
                    "semaines, zéro contentieux successoral ouvert.",
                "partner":    "Avv. Chiara Belforte",
                "legal_ops":  "Matteo Orsi · legal ops",
            },
            {
                "num":   "03",
                "title": "Droit social & RH",
                "tagline": "Pour les RH qui doivent avancer vite.",
                "pain_points": [
                    "Licenciement individuel ou collectif à gérer",
                    "Télétravail transfrontalier (salariés en UE ou UK)",
                    "Restructuration avec départs incités",
                    "BSA/AGA/BSPCE et avantages pour scale-ups",
                ],
                "signals": [
                    "40+ licenciements individuels clos en conciliation",
                    "12 plans de départs incités sans contentieux ouvert",
                    "Associée dédiée · Avv. Sara Miccoli",
                ],
                "case_snippet":
                    "Une scale-up turinoise a réduit ses effectifs de "
                    "18 % sans un contentieux ouvert — via notre méthode "
                    "de conciliation individuelle sur 34 postes.",
                "partner":    "Avv. Sara Miccoli",
                "legal_ops":  "Luca Tagliavini · legal ops",
            },
            {
                "num":   "04",
                "title": "Contrats B2B",
                "tagline": "Pour ceux qui signent des MSA chaque semaine.",
                "pain_points": [
                    "MSA / DPA / SOW à standardiser",
                    "Négociation redline avec clients grands comptes",
                    "Licensing SaaS avec contreparties US",
                    "Archive contrats morcelée ou inexistante",
                ],
                "signals": [
                    "Canal Slack dédié · SLA 48 heures",
                    "Templates validés sur 6 secteurs verticaux",
                    "Associé dédié · Avv. Davide Romano",
                ],
                "case_snippet":
                    "Un SaaS B2B turinois nous a confié toute la "
                    "contractualisation commerciale — depuis juillet "
                    "2024 nous signons chaque semaine un MSA grand "
                    "compte avec un délai médian de 8 jours entre "
                    "première version et signature.",
                "partner":    "Avv. Davide Romano",
                "legal_ops":  "Alice Piatti · legal ops",
            },
            {
                "num":   "05",
                "title": "Règlement des différends",
                "tagline": "Quand une négociation part en vrille.",
                "pain_points": [
                    "Contentieux avec fournisseur ou client grand compte",
                    "Arbitrage sur clause internationale",
                    "Médiation obligatoire pré-contentieuse",
                    "Gestion de crise réputationnelle",
                ],
                "signals": [
                    "75 % des litiges clos sans jugement",
                    "4 arbitrages CCI gérés ces 24 derniers mois",
                    "Associé dédié · Avv. Marco Trentini",
                ],
                "case_snippet":
                    "Une PME bolognaise avec un contentieux de 2,8 M € "
                    "contre un fournisseur allemand — bouclé en médiation "
                    "en 14 semaines avec un accord transactionnel plus "
                    "favorable que la demande initiale.",
                "partner":    "Avv. Marco Trentini",
                "legal_ops":  "Irene Bonomi · legal ops",
            },
            {
                "num":   "06",
                "title": "Privacy & IA",
                "tagline": "Pour les entreprises qui travaillent avec données ou modèles.",
                "pain_points": [
                    "Audit RGPD avant une levée ou un M&A",
                    "Analyse de conformité règlement sur l'IA et cartographie par classe de risque",
                    "AIPD sur processus critiques ou modèles prédictifs",
                    "Gestion de violation de données et notification au Garante",
                ],
                "signals": [
                    "Première AIPD règlement sur l'IA italienne pour marketplace B2C",
                    "6 audits RGPD pré-M&A sans impact sur le deal",
                    "Associée dédiée · Avv. Giulia Masi",
                ],
                "case_snippet":
                    "Une marketplace romaine a mis sa plateforme en "
                    "conformité règlement sur l'IA avant l'entrée en "
                    "vigueur effective — cartographie complète, AIPD "
                    "sur 3 processus et politique publique prête, "
                    "le tout en 6 semaines.",
                "partner":    "Avv. Giulia Masi",
                "legal_ops":  "Paolo Sangermano · legal ops",
            },
        ],

        "team_label":   "L'équipe complète",
        "team_heading": "Huit avocats, <em>deux legal ops</em>.",
        "team_intro":
            "L'équipe du cabinet — les noms que vous retrouvez sur les "
            "dossiers et en visio. Pas de junior-of-record : les seniors "
            "sont à la table de la découverte au closing, les legal ops "
            "pilotent le dashboard.",
        "team": [
            {"name": "Avv. Giorgia Martini",  "role": "Managing partner · Startup & Tech",        "office": "Milan",   "email": "giorgia@martinipartners.legal",
             "bio":  "12 ans chez DLA Piper · 2 Séries A clôturées en 2025."},
            {"name": "Avv. Davide Romano",    "role": "Co-fondateur · Contrats B2B",              "office": "Turin",   "email": "davide@martinipartners.legal",
             "bio":  "10 ans chez Bird & Bird · LL.M. Fordham · contributeur AIGA."},
            {"name": "Avv. Chiara Belforte",  "role": "Associée · PME & Famille",                 "office": "Bologne", "email": "chiara@martinipartners.legal",
             "bio":  "15 ans dans un cabinet familial émilien · Bocconi."},
            {"name": "Avv. Sara Miccoli",     "role": "Associée · Droit social & RH",             "office": "Milan",   "email": "sara@martinipartners.legal",
             "bio":  "Ex-responsable du département travail d'une boutique milanaise."},
            {"name": "Avv. Marco Trentini",   "role": "Associé · Règlement des différends",       "office": "Milan",   "email": "marco@martinipartners.legal",
             "bio":  "Spécialiste des arbitrages CCI et de la médiation commerciale."},
            {"name": "Avv. Giulia Masi",      "role": "Associée · Privacy & IA",                  "office": "Milan",   "email": "giulia@martinipartners.legal",
             "bio":  "Ex Autorité Garante · doctorat en éthique de l'IA."},
            {"name": "Avv. Tommaso Neri",     "role": "Senior associate · Startup & M&A",         "office": "Turin",   "email": "tommaso@martinipartners.legal",
             "bio":  "6 ans dans une boutique M&A milanaise · focus scale-up tech."},
            {"name": "Avv. Beatrice Riva",    "role": "Senior associate · Contract-as-a-Service", "office": "Turin",   "email": "beatrice@martinipartners.legal",
             "bio":  "Spécialiste du SaaS licensing transfrontalier · IAPP CIPP/E."},
            {"name": "Elena Vasile",          "role": "Legal ops lead",                           "office": "Milan",   "email": "elena@martinipartners.legal",
             "bio":  "Ex operations manager dans une scale-up logistique · conçoit les flux dashboard."},
            {"name": "Matteo Orsi",           "role": "Legal ops · bureau PME",                   "office": "Bologne", "email": "matteo@martinipartners.legal",
             "bio":  "Ex paralégal dans un cabinet fiscal bolognais · expert de l'archivage des dossiers."},
        ],

        "cta_heading": "Votre secteur n'est pas dans cette liste ?",
        "cta_intro":
            "Il arrive que des mandats hors des six secteurs nous soient "
            "adressés — nous les acceptons uniquement si nous avons "
            "l'expérience spécifique ou si nous co-travaillons avec un "
            "cabinet partenaire. Écrivez-nous le périmètre : sous 24 "
            "heures nous vous disons si c'est notre domaine.",
        "cta_primary":      "Racontez-nous le dossier",
        "cta_primary_href": "contatti",
    },

    # ─── INSIGHTS ───────────────────────────────────────────────
    "insights": {
        "eyebrow":  "Insights · 2026",
        "headline": "Quand une règle change, <em>nous écrivons une note</em>.",
        "intro":
            "Nous n'avons pas de newsletter. Nous n'avons pas de "
            "séquences marketing. Quand une règle change ou qu'un dossier "
            "arrive sur le bureau, quelqu'un au cabinet écrit une note — "
            "nous la publions ici parce que nos clients nous le demandent, "
            "et parce que nos candidats la lisent avant l'entretien.",

        "card_topic_label":   "Pratique",
        "card_author_label":  "Par",
        "card_reading_label": "Lecture",

        "posts_intro":
            "Six notes récentes. L'archive complète est sur le dashboard "
            "client — ici nous publions uniquement celles d'intérêt public.",

        "topics_label": "Pratiques",
        "topics":       ["Tous", "Startup & Tech", "Droit social & RH", "Privacy & IA", "M&A", "Différends"],

        "cta_heading": "Vous voulez recevoir nos notes en avant-première ?",
        "cta_intro":
            "Les clients du cabinet reçoivent les notes sur le dashboard "
            "avant la publication. Si cela vous intéresse, réservez un "
            "appel de découverte — et nous vous montrons comment cela fonctionne.",
        "cta_primary":      "Prendre un rendez-vous stratégique",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Rendez-vous stratégique",
        "headline": "Trente minutes, en visio, <em>sans engagement</em>.",
        "intro":
            "Le premier contact est avec un associé, pas un BDR. Nous "
            "discutons du périmètre, du délai et de l'éventuel conflit "
            "d'intérêt — avant toute proposition financière. Gratuit, "
            "sans engagement, réponse d'un associé réel.",

        "slot_label": "Prochain créneau disponible",
        "slot_value": "Jeudi 17 avril · 10:30",
        "slot_note":  "L'appel se déroule depuis le dashboard client · pas besoin de compte Zoom",

        "form_label":   "Réserver l'appel",
        "form_heading": "Trois étapes, deux minutes, une conversation.",
        "form_intro":
            "Les informations sont traitées au sens du Règlement UE "
            "679/2016 et conservées sur notre dashboard chiffré, accès "
            "limité aux associés. Pas de CRM tiers.",
        "form_fields": [
            {"name": "name",      "label": "Prénom",         "type": "text",     "required": True,  "placeholder": "Ex. Giorgia",
             "helper": "Simplement le prénom, merci."},
            {"name": "surname",   "label": "Nom",            "type": "text",     "required": True,  "placeholder": "Ex. Rossi",
             "helper": "Tel qu'il apparaît sur les documents d'entreprise."},
            {"name": "email",     "label": "E-mail",         "type": "email",    "required": True,  "placeholder": "giorgia@entreprise.com",
             "helper": "Nous acceptons aussi les domaines grand public — nous ne sommes pas un cabinet d'affaires du siècle dernier."},
            {"name": "phone",     "label": "Téléphone",      "type": "tel",      "required": False, "placeholder": "+33 ...",
             "helper": "Facultatif. Utilisé uniquement si l'appel saute."},
            {"name": "company",   "label": "Entreprise ou cabinet", "type": "text","required": True,  "placeholder": "Ex. Acme S.A.S.",
             "helper": "Le nom enregistré ou le nom commercial."},
            {"name": "company_type", "label": "Type d'entreprise","type": "select", "required": True,
             "options": [
                 "Startup (pre-seed)",
                 "Startup (seed)",
                 "Scale-up (Série A ou plus)",
                 "PME / entreprise familiale",
                 "Scale-up mature / corporate",
                 "Indépendant ou freelance",
                 "Autre",
             ],
             "helper": "Sert à vérifier si vous entrez dans notre pratique."},
            {"name": "stage",      "label": "Stade",           "type": "select", "required": True,
             "options": [
                 "Encore en discussion interne",
                 "Prêts à démarrer sous un mois",
                 "Prêts à démarrer sous trois mois",
                 "Exploratoire, pas d'urgence",
             ],
             "helper": "Aide à réserver le bon associé sur votre dossier."},
            {"name": "help_type",  "label": "Type d'accompagnement", "type": "select", "required": True,
             "options": [
                 "Je ne sais pas encore · à cadrer en visio",
                 "Contrats B2B",
                 "Startup legal sprint / levée de fonds",
                 "M&A ou transmission",
                 "Droit social, RH, BSA/AGA/BSPCE",
                 "Privacy, RGPD, règlement sur l'IA",
                 "Contentieux ou différends",
                 "Fractional General Counsel",
             ],
             "helper": "Choisissez \"Je ne sais pas encore\" si le périmètre couvre plusieurs pratiques."},
            {"name": "message",   "label": "Racontez-nous le dossier", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Max 600 caractères. Pas de noms de contrepartie ni de données sensibles — on en parle en visio après NDA réciproque.",
             "helper": "Juste ce qu'il faut pour voir si c'est notre domaine. "
                       "Les noms des contreparties ne se partagent qu'après NDA."},
        ],

        "form_sections": [
            {"num": "01", "title": "Qui vous êtes",
             "meta": "La personne avec qui nous échangerons en visio.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Ce que vous faites",
             "meta": "Pour le conflict-check préliminaire.",
             "fields": ["company", "company_type", "stage"]},
            {"num": "03", "title": "Ce dont vous avez besoin",
             "meta": "Aucun détail sensible ici — nous entrons dans le fond uniquement après NDA réciproque.",
             "fields": ["help_type", "message"]},
        ],

        "form_submit_label": "Réserver le rendez-vous stratégique",
        "form_submit_note":
            "Réponse d'un associé réel sous 2 heures ouvrées. "
            "Pas de BDR, pas de séquence, pas de \"on revient vers vous\".",
        "form_consent":
            "Je consens au traitement de mes données personnelles au "
            "sens du Règlement UE 679/2016. Les données sont conservées "
            "sur le dashboard chiffré du cabinet avec accès limité aux "
            "associés. Aucune donnée n'est communiquée à des tiers sans "
            "autorisation explicite.",

        "office_address_label": "Adresse",
        "office_area_label":    "Quartier",
        "office_phone_label":   "Téléphone",
        "office_email_label":   "E-mail",

        "offices_label": "Les trois bureaux",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Siège",
                "address": "Via Solferino 40 · 20121",
                "area":    "Brera · à deux pas de la Piazza della Scala",
                "phone":   "+39 02 4546 7789",
                "email":   "milano@martinipartners.legal",
                "note":    "Toutes les pratiques · salles de réunion réservables depuis le dashboard",
            },
            {
                "city":    "Turin",
                "tag":     "Bureau scale-up",
                "address": "Via Roma 324 · 10123",
                "area":    "Centre · proche de la Piazza Castello",
                "phone":   "+39 011 5667 2240",
                "email":   "torino@martinipartners.legal",
                "note":    "Bureau scale-up tech · siège principal contract-as-a-service",
            },
            {
                "city":    "Bologne",
                "tag":     "Bureau PME",
                "address": "Via Indipendenza 18 · 40121",
                "area":    "Centre · proche de la Piazza Maggiore",
                "phone":   "+39 051 3344 8812",
                "email":   "bologna@martinipartners.legal",
                "note":    "Bureau PME et M&A mid-market · corridor Émilie-Romagne",
            },
        ],

        "channels_label": "Canaux directs",
        "channels": [
            ("E-mail général",      "hello@martinipartners.legal", "Réponse sous 2 heures ouvrées"),
            ("Standard Milan",      "+39 02 4546 7789",            "Lun – Ven · 09:00 – 19:00"),
            ("LinkedIn entreprise", "in/martini-partners",         "Notes publiques et AMA hebdomadaires"),
        ],

        "footnote":
            "Martini & Partners ne fait pas de cold outreach. Si "
            "quelqu'un se présente comme BDR en notre nom, ce n'est "
            "pas nous. Toutes les relations naissent d'une recommandation, "
            "de la lecture d'une de nos notes ou de ce formulaire.",
    },

    # ─── POSTS ──────────────────────────────────────────────────
    "posts": [
        {
            "slug":     "ai-act-pmi-italiane",
            "title":    "Règlement sur l'IA · ce qui change pour les PME italiennes",
            "topic":    "Privacy & IA",
            "date":     "17 avril 2026",
            "reading":  "8 min",
            "author":   "Avv. Giulia Masi",
            "lead":
                "Le règlement sur l'IA entre en application effective "
                "le 2 août 2026 pour les systèmes à haut risque. Pour "
                "les PME italiennes qui utilisent des modèles prédictifs "
                "en production — marketplaces, scoring clients, HR tech — "
                "la fenêtre pour se mettre en conformité est de quatre "
                "mois. Voici comment nous le faisons avec nos clients.",
            "sections": [
                {
                    "heading": "Pourquoi cela concerne aussi les PME",
                    "body":
                        "La lecture répandue est que le règlement sur "
                        "l'IA ne touche que les géants — OpenAI, Mistral, "
                        "Meta. Elle est fausse. Le règlement classe par "
                        "usage, pas par taille de l'entreprise qui "
                        "développe. Un algorithme de scoring de crédit "
                        "fait en interne par une fintech seed relève du "
                        "haut risque exactement comme celui d'une banque "
                        "d'affaires — et la PME a moins de ressources "
                        "pour se mettre en conformité.",
                },
                {
                    "heading": "Les quatre classes de risque",
                    "body":
                        "Risque inacceptable (interdit), risque élevé "
                        "(exigences très strictes), risque limité "
                        "(transparence obligatoire), risque minimal "
                        "(aucune obligation spécifique). La cartographie "
                        "des systèmes de l'entreprise dans les quatre "
                        "classes est la première étape — et pour les PME "
                        "elle demande en moyenne deux semaines de travail "
                        "avec un legal ops + un product manager.",
                },
                {
                    "heading": "Que faire maintenant",
                    "body":
                        "Trois actions concrètes : un inventaire complet "
                        "des systèmes IA en production (y compris les "
                        "plug-ins tiers comme chatbots ou moteurs de "
                        "recommandation), une AIPD intégrée pour les "
                        "systèmes à haut risque, et une politique "
                        "publique qui déclare l'usage de l'IA dans les "
                        "processus décisionnels touchant clients ou "
                        "collaborateurs. Pour la plupart des PME c'est "
                        "un projet de six semaines — notre offre "
                        "règlement sur l'IA Readiness le couvre intégralement.",
                },
            ],
            "takeaway":
                "Le règlement sur l'IA n'est pas un exercice bureaucratique "
                "— c'est une opportunité de mettre de l'ordre dans les "
                "systèmes qui touchent les données des clients ou des "
                "collaborateurs. Ceux qui s'y prennent bien aujourd'hui "
                "vendent mieux demain.",
            "tags":     ["Règlement sur l'IA", "RGPD", "Compliance", "PME"],
        },
        {
            "slug":     "stock-option-2026",
            "title":    "BSA/AGA 2026 · nouveau régime fiscal",
            "topic":    "Startup & Tech",
            "date":     "14 avril 2026",
            "reading":  "6 min",
            "author":   "Avv. Giorgia Martini",
            "lead":
                "La Loi de finances italienne 2026 a modifié le régime "
                "fiscal des plans d'actions gratuites et BSA pour les "
                "startups et PME innovantes. Le changement est favorable "
                "— mais la rédaction laisse des marges d'interprétation. "
                "Voyons comment nous structurons les nouveaux plans et "
                "que faire de ceux existants.",
            "sections": [
                {
                    "heading": "Ce qui change au 1er janvier 2026",
                    "body":
                        "L'imposition s'applique au moment de la vente "
                        "effective des actions (et non plus au vesting) "
                        "pour les startups innovantes inscrites au "
                        "registre spécial. Le taux sur les plus-values "
                        "reste à 26 %. C'est un changement significatif : "
                        "il supprime le paradoxe du collaborateur qui "
                        "paie des impôts sur des actions qu'il n'a pas "
                        "encore monétisées.",
                },
                {
                    "heading": "Les plans existants doivent-ils être réécrits ?",
                    "body":
                        "Pas nécessairement. Le nouveau régime s'applique "
                        "automatiquement aux plans respectant les "
                        "conditions — inscription en startup innovante, "
                        "vesting minimum de 24 mois, attribution à des "
                        "collaborateurs ou administrateurs en continuité "
                        "de relation. La plupart des plans récents sont "
                        "déjà compatibles. Les plans écrits avant 2022 "
                        "en revanche demandent presque toujours une mise à jour.",
                },
                {
                    "heading": "Comment structurer les nouveaux plans",
                    "body":
                        "Trois choses à bien faire : rédiger le règlement "
                        "interne avec une référence explicite au régime "
                        "2026, documenter la date d'attribution et le "
                        "plan de vesting individuel pour chaque "
                        "collaborateur, et fournir au collaborateur un "
                        "guide fiscal en italien au moment de l'attribution. "
                        "Notre template de plan BSA/AGA est déjà à jour.",
                },
            ],
            "takeaway":
                "Pour les startups innovantes le nouveau régime est "
                "une simplification nette — et un argument supplémentaire "
                "pour convaincre un senior de quitter un grand groupe "
                "pour rejoindre une équipe founder.",
            "tags":     ["BSA/AGA", "Startup", "Fiscalité", "RH"],
        },
        {
            "slug":     "smart-working-confine",
            "title":    "Télétravail transfrontalier · trois scénarios",
            "topic":    "Droit social & RH",
            "date":     "11 avril 2026",
            "reading":  "7 min",
            "author":   "Avv. Sara Miccoli",
            "lead":
                "Depuis 2023 la plupart des entreprises italiennes ont "
                "accepté le télétravail transfrontalier — mais les "
                "règles sur cotisations sociales, retenues fiscales et "
                "juridiction du droit du travail applicable restent "
                "confuses. Trois scénarios type que nous voyons chaque mois.",
            "sections": [
                {
                    "heading": "Scénario 1 · Salarié italien s'installant en Espagne",
                    "body":
                        "Si le salarié travaille plus de 183 jours par "
                        "an en Espagne, il devient résident fiscal "
                        "espagnol — l'entreprise italienne doit verser "
                        "des cotisations Social Security espagnoles "
                        "(convention bilatérale) et des retenues IRPF "
                        "espagnoles. La loi du contrat de travail reste "
                        "italienne si expressément stipulée, mais les "
                        "droits minimaux espagnols (congés, licenciement) "
                        "s'appliquent malgré tout.",
                },
                {
                    "heading": "Scénario 2 · Salarié UE s'installant en Italie",
                    "body":
                        "Plus simple mais non trivial. L'entreprise "
                        "devient substitut d'impôt italien, ouvre une "
                        "position INPS et verse des cotisations "
                        "italiennes. Si le salarié a un contrat français "
                        "ou allemand d'origine, il faut renégocier — "
                        "beaucoup d'entreprises choisissent d'établir "
                        "un nouveau contrat italien avec clause de continuité.",
                },
                {
                    "heading": "Scénario 3 · Salarié italien s'installant hors UE",
                    "body":
                        "Le plus délicat. Sans convention bilatérale "
                        "adéquate (ex. USA, Canada), on risque double "
                        "imposition fiscale et double cotisation "
                        "sociale. La solution propre est presque "
                        "toujours un contrat local avec entité "
                        "étrangère (filiale ou PEO / EOR) — maintenir "
                        "le contrat italien en mission longue n'est "
                        "soutenable que 18-24 mois au maximum.",
                },
            ],
            "takeaway":
                "Avant de dire oui à un télétravail transfrontalier, "
                "vérifiez toujours le pays de destination. Les règles "
                "changent entre UE, UK, USA et reste du monde — et les "
                "coûts pour l'entreprise peuvent varier de 30 % entre scénarios.",
            "tags":     ["Télétravail", "RH", "Transfrontalier", "Droit social"],
        },
        {
            "slug":     "contratti-saas-enterprise",
            "title":    "Contrats SaaS grand compte · trois clauses à ne jamais manquer",
            "topic":    "Contrats B2B",
            "date":     "8 avril 2026",
            "reading":  "5 min",
            "author":   "Avv. Davide Romano",
            "lead":
                "Après avoir signé plus de trois cents MSA SaaS grand "
                "compte ces trois dernières années, nous avons une "
                "liste mentale de clauses qui ne devraient jamais "
                "manquer. Trois que nous recommandons toujours, même "
                "quand le client \"ne les a jamais vues\".",
            "sections": [
                {
                    "heading": "1. Cap de responsabilité proportionné et au moins égal à 12 mois d'honoraires",
                    "body":
                        "Le cap de responsabilité standard proposé par "
                        "les grands vendors (Salesforce, ServiceNow) "
                        "est généralement de 12 mois d'honoraires du "
                        "service. L'accepter est raisonnable · négocier "
                        "à la baisse à 3 ou 6 mois est souvent possible "
                        "pour les deals sous 500 K €.",
                },
                {
                    "heading": "2. Portabilité des données et clause d'export",
                    "body":
                        "Le droit d'exporter toutes les données dans "
                        "un format machine-readable sous 30 jours "
                        "après résiliation, sans coûts supplémentaires. "
                        "Souvent absente, presque toujours négociable.",
                },
                {
                    "heading": "3. Préavis de changement de sous-traitant",
                    "body":
                        "Le droit d'être notifié au moins 30 jours "
                        "avant un changement de sous-traitant (hosting, "
                        "e-mail, analytics) — avec droit d'opt-out "
                        "sans pénalité si le nouveau sous-traitant ne "
                        "respecte pas les standards convenus.",
                },
            ],
            "takeaway":
                "Ces trois clauses se retrouvent dans 70 % des contrats "
                "grand compte que nous signons — les 30 % restants se "
                "laissent convaincre avec un drafting clair. Nous avons "
                "un template prêt sur le dashboard.",
            "tags":     ["SaaS", "Contrats", "Grand compte", "B2B"],
        },
        {
            "slug":     "mandati-m-and-a-2025",
            "title":    "M&A mid-market · ce que nous avons appris en 2025",
            "topic":    "M&A",
            "date":     "4 avril 2026",
            "reading":  "9 min",
            "author":   "Avv. Chiara Belforte",
            "lead":
                "En 2025 nous avons bouclé sept opérations de M&A "
                "mid-market — trois côté cédant, quatre côté acquéreur, "
                "cinq italiennes et deux transfrontalières. Voici les "
                "trois tendances que nous avons vues se répéter "
                "suffisamment pour mériter une note.",
            "sections": [
                {
                    "heading": "Le retour des earn-outs",
                    "body":
                        "Après deux ans où les cessions se bouclaient "
                        "à prix fixe avec sortie du fondateur à 6-12 "
                        "mois, en 2025 l'earn-out est réapparu. Dans "
                        "le mid-market aussi. Typiquement 25-35 % du "
                        "prix lié à des KPI opérationnels post-closing, "
                        "durée 24-36 mois. Pour le fondateur c'est une "
                        "opportunité mais cela demande un contrat "
                        "d'earn-out bien rédigé pour éviter le contentieux.",
                },
                {
                    "heading": "La due diligence IA/privacy est devenue normale",
                    "body":
                        "Même le fonds le plus classique demande "
                        "désormais un résumé de la conformité RGPD "
                        "et une cartographie des systèmes IA avant "
                        "de signer. Un audit préventif côté cédant "
                        "coûte 5-10 K € et fait gagner 2-3 semaines "
                        "sur le processus.",
                },
                {
                    "heading": "Les signings transfrontaliers demandent plus de temps",
                    "body":
                        "Les deux opérations italo-DACH de 2025 ont "
                        "demandé en moyenne 8 semaines de plus que "
                        "les signings italiens purs — entre traduction "
                        "certifiée des actes, approbation antitrust "
                        "et coordination avec notaire allemand. Mieux "
                        "vaut le planifier dès le départ que le "
                        "découvrir en DD.",
                },
            ],
            "takeaway":
                "2025 a normalisé l'earn-out et rendu standard la "
                "due diligence IA/privacy. Sur le transfrontalier, "
                "mieux vaut surévaluer le temps que stresser le closing.",
            "tags":     ["M&A", "Fonds", "Due diligence", "Transfrontalier"],
        },
        {
            "slug":     "dashboard-cliente-perche",
            "title":    "Pourquoi nous avons construit un dashboard client (au lieu de l'acheter)",
            "topic":    "Startup & Tech",
            "date":     "28 mars 2026",
            "reading":  "6 min",
            "author":   "Avv. Giorgia Martini",
            "lead":
                "En 2020 nous avons évalué Clio, MyCase, PracticePanther "
                "et six autres logiciels \"practice management\" pour "
                "cabinets juridiques. Aucun ne nous a convaincus. Nous "
                "avons construit le nôtre — en interne, avec un product "
                "manager à temps partiel. Voici pourquoi, et ce que "
                "nous en avons appris.",
            "sections": [
                {
                    "heading": "Le problème des PM juridiques standard",
                    "body":
                        "Les logiciels practice management pour "
                        "cabinets juridiques sont construits pour des "
                        "cabinets de 50+ personnes qui facturent à "
                        "l'heure. L'UX est pensée pour des assistantes "
                        "et des avocats qui remplissent des timesheets. "
                        "Nous sommes dix, nous ne facturons pas à "
                        "l'heure et nos clients sont des product "
                        "managers habitués à Linear. Incompatible.",
                },
                {
                    "heading": "Ce que nous avons construit",
                    "body":
                        "Un workspace modèle Linear + Notion avec "
                        "kanban pour les dossiers, une archive "
                        "documentaire chiffrée, un calendrier partagé "
                        "des échéances et un canal chat pour chaque "
                        "dossier. Pas de timesheet — les heures se "
                        "tracent en fin de semaine, en clair pour le "
                        "client. Six mois de développement, coût "
                        "80 K €, aujourd'hui tout le monde s'en sert.",
                },
                {
                    "heading": "Pourquoi c'est devenu un avantage commercial",
                    "body":
                        "Nous avons découvert a posteriori que le "
                        "dashboard est la première raison pour laquelle "
                        "les clients nous choisissent. En pitch nous "
                        "montrons un walkthrough de deux minutes du "
                        "workspace réel — et pour des entreprises "
                        "habituées à Linear + Notion c'est un "
                        "game-changer face aux PDF par e-mail des autres cabinets.",
                },
            ],
            "takeaway":
                "Faire ce que les autres ne veulent pas faire. Le "
                "dashboard a été l'investissement le plus important "
                "de nos huit premières années — plus que tout nouveau "
                "bureau ou toute nouvelle embauche.",
            "tags":     ["Dashboard", "Product", "Cabinet", "Outillage"],
        },
    ],
}

# D-047 compliance note:
# French locale tree · same shape as JURIS_CONTENT_IT. The skin files
# never author any French literal — every user-facing string in FR
# flows through this file.
