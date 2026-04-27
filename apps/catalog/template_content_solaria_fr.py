"""Solaria — Business Coaching · French locale content tree.

Phase X.4 Pass B · 2026-04-26 · Multilingual completion pass.

Mirrors the shape of `SOLARIA_CONTENT_IT` exactly. Voice register:
warm-professional, vouvoiement throughout, ICF-aligned. Reference
voices: HBR France coaching column, Les Echos Executives, Coaching
Magazine France. Adulte qui parle à un adulte. Pas de jargon de
développement personnel. Pas de promesses de transformation.

Voice anchor (CS-EXEC-01 · preserved verbatim-in-translation):
    « Le coaching n'est ni une thérapie, ni du conseil. Nous ne
     dictons pas ce qu'il faut faire et nous n'analysons pas le passé
     pour le comprendre. Nous travaillons sur les choix que vous êtes
     sur le point de prendre, avec une méthode et une cadence. Un
     parcours a un début déclaré et une fin déclarée. À la fin, s'il
     a fonctionné, vous êtes plus autonome dans vos décisions — pas
     plus dépendant·e d'un coach. »

Italian normative references and proper nouns preserved (ICF, EMCC,
ODCEC, GROW, Co-Active, Immunity to Change, Codice Deontologico
ICF §2.4, Reg. UE 679/2016 ≈ RGPD européen). Italian addresses,
numéros, format téléphonique, montants en euros et années conservés.
Antipattern interdits (briefing §13) : « Libérez votre potentiel »,
« Transformez votre vie en N jours », « Meilleure version de
vous-même », « Mindset gagnant », citations Einstein/Jung/Gandhi/
Steve Jobs, métaphores de sommet de montagne.
"""
from __future__ import annotations

from typing import Any


from apps.catalog.template_content_solaria import (  # noqa: E402
    _POOL_HERO,
    _POOL_FEATURE,
    _POOL_PORTRAIT_A,
    _POOL_PORTRAIT_B,
    _POOL_DETAIL,
    _POOL_AMBIENT,
)


SOLARIA_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Cabinet",     "kind": "home"},
        {"slug": "il-coach",   "label": "La coach",    "kind": "about"},
        {"slug": "percorsi",   "label": "Parcours",    "kind": "services"},
        {"slug": "casi",       "label": "Cas",         "kind": "case_study_list"},
        {"slug": "contatti",   "label": "Contact",     "kind": "contact"},
    ],

    "site": {
        "logo_initial": "S",
        "logo_word":    "Solaria",
        "tag":          "Business coaching · Milano Isola · ICF-PCC depuis 2017",
        "phone":        "+39 02 3663 4712",
        "email":        "discovery@solariacoaching.it",
        "address":      "Via Thaon di Revel 21 · 20159 Milano",
        "hours_compact": "Lun – Ven · 9h00 – 19h00 · sur rendez-vous",
        "hours_footer_rows": [
            "Sessions en soirée pour les coachés internationaux (UTC+5 / UTC-5)",
            "Samedi et dimanche · fermé",
        ],
        "license":      "Professional Certified Coach (PCC) · International Coaching Federation (ICF)",
        "footer_intro":
            "Cabinet de coaching professionnel pour entrepreneurs, "
            "dirigeantes et dirigeants en transition et équipes de "
            "middle management. Méthode déclarée, cadence concertée, "
            "début et fin du parcours inscrits au contrat — aucune "
            "transformation promise, aucune dépendance recherchée. "
            "Cabinet à Milano, sessions sur place et en ligne.",
        "foot_studio":   "Le cabinet",
        "foot_pages":    "Sections",
        "foot_contact":  "Contact",
        "foot_offices":  "Cabinet",
        "offices_footer_rows": [
            "Milano · Isola",
        ],
        "case_practice_label":     "Domaine",
        "case_year_label":         "Année",
        "case_duration_label":     "Durée",
        "case_lead_label":         "Coach",
        "case_lead_partner_label": "Coach",
        "case_team_label":         "Parcours & sponsor",
        "case_timeline_label":     "Calendrier",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Business coaching · Milano Isola · ICF-PCC depuis 2017",
        "headline":    "Le coaching n'est ni une <em>thérapie</em>, ni du <em>conseil</em>.",
        "intro":
            "Parcours de coaching pour entrepreneurs, dirigeants en "
            "transition et middle managers. Méthode déclarée, cadence "
            "concertée, début et fin inscrits au contrat — aucune "
            "transformation en trente jours.",
        "primary_cta":   "Réserver une discovery call",
        "primary_href":  "contatti",
        "secondary_cta": "La méthode",
        "secondary_href":"il-coach",

        "hero_image":              _POOL_HERO,
        "hero_image_credit_left":  ("Reportage",   "Session executive 1:1"),
        "hero_image_credit_right": ("Cabinet",     "Solaria · Milano Isola"),
        "hero_meta_strip": [
            ("Session",          "60 minutes · cadence bimensuelle"),
            ("Discovery call",   "20 – 30 minutes · gratuite"),
            ("Supervision",      "ICF-MCC continue depuis 2019"),
        ],

        "pillars_label":   "Parcours",
        "pillars_heading": "Trois formats, un parcours écrit",
        "pillars_intro":
            "Même méthode pour chaque format : contrat initial avec un "
            "objectif mesurable, sessions à cadence concertée, "
            "re-contracting à mi-parcours, clôture avec vérification, "
            "follow-up à trois mois inclus dans les honoraires.",
        "pillars": [
            ("01", "Executive 1:1",
             "Huit sessions de soixante minutes à cadence bimensuelle pour "
             "dirigeantes et dirigeants en transition de fonction, "
             "récemment promus, ou en préparation d'un changement de "
             "périmètre. Référentiels : Co-Active + Immunity to Change."),
            ("02", "Team coaching",
             "Six sessions avec l'équipe (cinq à dix personnes) plus un "
             "re-contracting avec le sponsor d'entreprise à mi-parcours. "
             "Pour middle management en croissance ou après "
             "réorganisation. Référentiel : GROW de groupe."),
            ("03", "Groupe d'entreprise",
             "Masterclass d'une journée + huit sessions individuelles "
             "pour trois à huit personnes du même client. Objectifs "
             "individuels arrimés aux objectifs de système, follow-up "
             "trimestriel avec le sponsor."),
        ],

        "kpi_heading": "Douze ans de pratique certifiée",
        "kpi_strip": [
            ("12",       "années de pratique ICF"),
            ("2 400+",   "heures de coaching délivrées"),
            ("160+",     "coachés accompagnés depuis 2014"),
            ("100 %",    "parcours avec follow-up à trois mois"),
        ],

        "sectors_label": "Profils des coachés",
        "sectors": [
            "PDG fraîchement promus",
            "Directeurs de fonction en transition",
            "Middle managers en croissance",
            "Équipes de leadership après réorganisation",
            "Associés de cabinets professionnels",
        ],

        "trust_label":   "Entreprises sponsors 2023 — 2025 · noms occultés selon Code ICF §2.4",
        "trust_logos":   [
            "SCALE-UP FINTECH · SÉRIE B",
            "GROUPE INDUSTRIEL COTÉ",
            "CABINET D'AVOCATS ASSOCIÉ",
            "FABRICANT DE DISPOSITIFS MÉDICAUX",
            "FONDATION ÉDUCATIVE",
            "BOUTIQUE DE SERVICES PROFESSIONNELS",
        ],

        "leadership_label":   "La coach",
        "leadership_heading": "Qui s'assied de l'autre côté de la table",
        "leadership_intro":
            "Une coach fondatrice et une coach associée. Chaque parcours "
            "est suivi personnellement par la même coach du début à la "
            "clôture — aucun hand-over junior-senior, aucune rotation "
            "silencieuse.",
        "leadership": [
            {
                "name":  "Dr. Giulia Loreti",
                "role":  "Coach fondatrice · ICF-PCC · EMCC Senior Practitioner",
                "portrait": _POOL_PORTRAIT_A,
                "bio":
                    "Quinze ans en RH d'entreprise comme responsable du "
                    "développement managérial dans un groupe industriel coté, "
                    "avant de se consacrer pleinement au coaching en 2014. "
                    "Professional Certified Coach (PCC) certifiée par "
                    "l'International Coaching Federation depuis 2017. "
                    "Supervision continue avec une senior ICF-MCC depuis 2019.",
                "credentials": [
                    "ICF-PCC n° 011749 (depuis 2017 · renouvelée 2023)",
                    "EMCC Senior Practitioner (depuis 2020)",
                    "Coach Training Institute · cursus Co-Active (2014)",
                    "Università Bocconi — Psychologie du travail '02",
                ],
            },
            {
                "name":  "Dr. Martina Erriquez",
                "role":  "Coach associée · ICF-ACC · en parcours PCC",
                "portrait": _POOL_PORTRAIT_B,
                "bio":
                    "Huit ans comme consultante en développement "
                    "organisationnel avant de débuter le parcours coaching "
                    "en 2020. Associate Certified Coach (ACC) depuis 2022, "
                    "actuellement en parcours de certification PCC "
                    "(achèvement prévu 2027). Supervisée mensuellement "
                    "par Giulia Loreti et par une superviseure EMCC externe.",
                "credentials": [
                    "ICF-ACC n° 028914 (depuis 2022)",
                    "Co-Active Training Institute · Fondamentaux + Intermédiaire (2020-2022)",
                    "Università Cattolica — Psychologie du travail '12",
                    "Supervision mensuelle ICF + EMCC",
                ],
            },
        ],

        "cases_label":   "Cas",
        "cases_heading": "Trois parcours, trois objectifs mesurés",
        "cases_intro":
            "Cas conclus ces trois dernières années — coachés anonymisés "
            "selon le Code ICF §2.4, objectifs et résultats réels. "
            "Reference call avec le sponsor d'entreprise disponible sous "
            "NDA réciproque pour les parcours corporate.",

        "cta_label":     "Est-ce le bon moment ?",
        "cta_heading":   "Vingt minutes pour vérifier que Solaria vous correspond",
        "cta_intro":
            "Aucune session de coaching gratuite, aucun diagnostic, aucun "
            "devis à froid. Une conversation honnête sur votre objectif "
            "et l'adéquation du coaching à votre besoin. Si ce n'est pas "
            "du coaching, nous vous le disons — et nous indiquons le bon "
            "professionnel.",
        "cta_primary":   "Réserver une discovery call",
        "cta_primary_href": "contatti",
        "cta_secondary": "La méthode en cinq étapes",
        "cta_secondary_href": "il-coach",
    },

    # ─── IL COACH ───────────────────────────────────────────────
    "il-coach": {
        "eyebrow":   "La coach · 2014 — 2026",
        "headline":  "Une méthode <em>déclarée</em>, douze ans de pratique certifiée.",
        "intro":
            "Solaria a débuté en 2014 lorsque Giulia Loreti a quitté un "
            "poste de responsable RH dans le corporate pour se consacrer "
            "pleinement au coaching. Le premier parcours Solaria — un "
            "team coaching pour une scale-up fintech milanaise tout "
            "juste constituée — a démarré en novembre de la même année. "
            "Martina Erriquez a rejoint comme coach associée en 2020.",

        "history_label":   "La méthode · parcours type en cinq étapes",
        "history_heading": "Cinq étapes, une cadence concertée",
        "history_intro":
            "Le parcours Solaria suit la même structure indépendamment "
            "du format (1:1 executive, équipe, groupe d'entreprise). Ces "
            "cinq étapes sont écrites dans le contrat de coaching que "
            "le coaché signe au début du parcours.",
        "history": [
            ("01", "Discovery call",
             "Vingt à trente minutes gratuites, sans engagement. Nous "
             "vérifions si l'objectif relève du coaching, si Solaria "
             "est le cabinet adéquat, nous discutons un devis indicatif. "
             "Aucune obligation à l'issue."),
            ("02", "Contrat initial",
             "Premier rendez-vous de quatre-vingt-dix minutes payant, "
             "avec définition de l'objectif mesurable (référentiel "
             "SMART), choix du référentiel de conduite (GROW · "
             "Co-Active · Immunity to Change), signature du contrat "
             "de coaching qui précise nombre de sessions, cadence, "
             "confidentialité, référence au Code Déontologique ICF."),
            ("03", "Sessions régulières",
             "Sessions de 60 minutes à cadence concertée (typiquement "
             "bimensuelle pour l'executive 1:1, mensuelle pour les "
             "équipes, trimestrielle pour le follow-up). Chaque "
             "session se clôt par un commitment écrit que le coaché "
             "vérifie de manière autonome avant la session suivante."),
            ("04", "Re-contracting à mi-parcours",
             "À mi-parcours, session de re-contracting avec le "
             "coaché (et avec le sponsor d'entreprise si le coaching "
             "est sponsorisé). On revoit l'objectif initial, on décide "
             "des ajustements éventuels, on décide de poursuivre ou "
             "de clore en avance. Aucune obligation de continuer."),
            ("05", "Clôture & follow-up",
             "Session finale de consolidation avec vérification "
             "explicite du résultat par rapport à l'objectif initial. "
             "Follow-up programmé à trois mois de la clôture — une "
             "session de soixante minutes pour vérifier la durabilité "
             "du changement. Le follow-up est inclus dans les "
             "honoraires du parcours, jamais facturé séparément."),
        ],

        "values_label":   "Principes",
        "values_heading": "Quatre principes <em>non négociables</em>",
        "values_intro":
            "Quatre règles qui distinguent un parcours Solaria d'un "
            "coaching générique. Elles sont écrites dans le contrat "
            "signé au début du parcours, et le coaché peut en "
            "demander l'application à tout moment.",
        "values": [
            ("01", "Le coaching n'est ni une thérapie, ni du conseil",
             "Nous ne diagnostiquons pas de troubles psychologiques "
             "(nous ne sommes pas psychothérapeutes). Nous ne "
             "proposons pas de solutions d'entreprise (nous ne "
             "sommes pas consultantes en stratégie). Si lors de la "
             "discovery call ou au cours du parcours il apparaît "
             "que le besoin relève d'une de ces deux disciplines, "
             "nous le déclarons explicitement et orientons vers un "
             "professionnel de la discipline adéquate — quitte à "
             "clore la relation avec Solaria."),
            ("02", "Confidentialité sans exception",
             "Tout ce qui se passe en session reste en session. Les "
             "sponsors d'entreprise ne reçoivent que des reportings "
             "agrégés concertés au contrat initial — jamais de "
             "contenus spécifiques. Aucune exception sauf "
             "obligation légale, qui est explicitée au coaché avant "
             "toute communication tierce."),
            ("03", "Parcours borné, autonomie comme objectif",
             "Chaque parcours a un nombre de sessions déclaré au "
             "contrat initial. Nous n'offrons pas d'abonnement "
             "illimité, ni de coaching perpétuel. À la fin du "
             "parcours, s'il a fonctionné, le coaché est plus "
             "autonome dans ses décisions — pas plus dépendant "
             "d'un coach."),
            ("04", "Supervision continue obligatoire",
             "Les deux coachs Solaria sont en supervision continue : "
             "Giulia avec une senior ICF-MCC depuis 2019, Martina "
             "avec Giulia mensuellement plus une superviseure EMCC "
             "externe. La supervision est l'équivalent du contrôle "
             "qualité dans une pratique professionnelle sérieuse — "
             "et son coût est supporté par le cabinet, pas par le coaché."),
        ],

        "team_label":   "Cabinet",
        "team_heading": "Deux coachs, une superviseure externe, une seule gouvernance",
        "team_intro":
            "Les personnes qui suivent le travail de Solaria. Les "
            "sessions de coaching sont délivrées uniquement par "
            "Giulia ou Martina ; la superviseure externe n'interagit "
            "jamais avec les coachés mais vérifie la qualité de la "
            "pratique de la coach associée.",
        "team": [
            {"name": "Dr. Giulia Loreti",
             "role": "Coach fondatrice · ICF-PCC · EMCC Senior Practitioner",
             "office": "Milano",
             "bio": "Coaching 1:1 executive et team coaching. "
                    "2 400+ heures délivrées depuis 2014. Supervision avec ICF-MCC depuis 2019."},
            {"name": "Dr. Martina Erriquez",
             "role": "Coach associée · ICF-ACC · en parcours PCC",
             "office": "Milano",
             "bio": "Coaching 1:1 pour néo-managers et parcours de groupe d'entreprise. "
                    "Supervision mensuelle avec Giulia + EMCC externe."},
            {"name": "Dr. Elena Mannucci",
             "role": "Superviseure externe · ICF-MCC",
             "office": "Trento · consultante",
             "bio": "Supervise la pratique de Giulia depuis 2019 et de Martina depuis 2022. "
                    "N'interagit jamais avec les coachés — vérifie la qualité de la pratique."},
            {"name": "Mme Donatella Rinaldi",
             "role": "Assistante de cabinet · back-office",
             "office": "Milano",
             "bio": "Gestion des agendas, facturation, contractualisation. "
                    "N'accède jamais au contenu des sessions de coaching."},
        ],

        "coordinates_label": "Cabinet",
        "coordinates": [
            ("Milano",  "Via Thaon di Revel 21 · 20159 · Isola — à 300 mètres de la station MM Garibaldi FS"),
        ],

        "cta_heading": "Discovery call ou question par e-mail",
        "cta_intro":
            "La discovery call de vingt à trente minutes est la voie "
            "canonique pour évaluer si un parcours Solaria vous "
            "correspond. Si vous préférez poser une question écrite "
            "avant de réserver l'appel, l'e-mail du secrétariat est "
            "lu par Donatella tous les matins et l'une de nous deux "
            "vous répond dans la journée.",
        "cta_primary":  "Réserver une discovery call",
        "cta_primary_href": "contatti",
    },

    # ─── PERCORSI ───────────────────────────────────────────────
    "percorsi": {
        "eyebrow":  "Parcours de coaching · 2026",
        "headline": "Quatre parcours, <em>une seule méthode</em>.",
        "intro":
            "Quatre formats de parcours, chacun avec son nombre de "
            "sessions déclaré, sa cadence concertée, son format (sur "
            "place · en ligne · hybride) et son tarif indicatif. "
            "Chaque parcours suit la même méthode — contrat initial, "
            "sessions régulières, re-contracting à mi-parcours, "
            "clôture avec vérification, follow-up à trois mois.",

        "svc_duration_label": "Durée typique",
        "svc_leader_label":   "Coach référente",

        "services": [
            {
                "num":   "01",
                "title": "Executive 1:1",
                "blurb":
                    "Le format le plus demandé. Huit sessions de soixante "
                    "minutes à cadence bimensuelle, objectif mesurable "
                    "défini lors du premier rendez-vous et écrit dans le "
                    "contrat. Pour dirigeants en transition de fonction, "
                    "récemment promus, ou en préparation d'un changement "
                    "de périmètre. Référentiels : Co-Active + Immunity "
                    "to Change.",
                "scope": [
                    "Contrat initial avec objectif SMART mesurable",
                    "Huit sessions 60 min · cadence bimensuelle",
                    "Re-contracting à mi-parcours (quatrième session)",
                    "Clôture avec vérification du résultat",
                    "Follow-up 60 min à trois mois inclus",
                ],
                "duration": "16 semaines · 8 sessions + follow-up",
                "leader":   "Dr. Giulia Loreti",
            },
            {
                "num":   "02",
                "title": "Team coaching",
                "blurb":
                    "Travail avec des équipes de middle management "
                    "(cinq à dix personnes). Six sessions avec l'équipe "
                    "plus une session de re-contracting avec le sponsor "
                    "d'entreprise à mi-parcours. Pour équipes en "
                    "croissance, en intégration post-réorganisation, ou "
                    "en préparation d'un défi spécifique. Référentiel : "
                    "GROW appliqué au groupe.",
                "scope": [
                    "Contrat initial tripartite (équipe · sponsor · coach)",
                    "Six sessions 120 min · cadence mensuelle",
                    "Re-contracting avec sponsor à mi-parcours",
                    "Reporting agrégé au sponsor (jamais de contenus spécifiques)",
                    "Follow-up 90 min à trois mois inclus",
                ],
                "duration": "6 mois · 6 sessions + re-contracting + follow-up",
                "leader":   "Dr. Giulia Loreti",
            },
            {
                "num":   "03",
                "title": "Groupe d'entreprise",
                "blurb":
                    "Programme RH structuré pour trois à huit personnes "
                    "du même client corporate. Masterclass d'une journée "
                    "au début + huit sessions individuelles pour chaque "
                    "participant. Sponsor d'entreprise défini, objectifs "
                    "individuels reliés aux objectifs de système, "
                    "follow-up trimestriel avec le sponsor.",
                "scope": [
                    "Masterclass d'une journée d'ouverture (référentiel + code de déontologie)",
                    "Huit sessions 1:1 pour chaque participant",
                    "Tableau de bord agrégé pour le sponsor (KPI concertés)",
                    "Follow-up trimestriel avec le sponsor pour les 12 premiers mois",
                    "Devis personnalisé selon le nombre de participants",
                ],
                "duration": "6-9 mois · masterclass + 8 sessions/personne",
                "leader":   "Dr. Giulia Loreti · Dr. Martina Erriquez",
            },
            {
                "num":   "04",
                "title": "Session unique exploratoire",
                "blurb":
                    "Une seule session de quatre-vingt-dix minutes, sans "
                    "contrat de parcours. Pour qui souhaite évaluer "
                    "l'approche coaching sur un sujet spécifique avant "
                    "de s'engager dans un parcours. À l'issue, le coaché "
                    "décide d'ouvrir un parcours executive 1:1 ou de "
                    "clore la relation — aucune obligation de continuer.",
                "scope": [
                    "Session 90 min avec GROW appliqué au sujet",
                    "Livrable écrit remis sous 48 heures",
                    "Évaluation honnête : coaching · thérapie · conseil",
                    "Si coaching : devis indicatif pour un parcours",
                    "Si pas coaching : orientation vers le bon professionnel",
                ],
                "duration": "1 session · 90 minutes",
                "leader":   "Dr. Martina Erriquez",
            },
        ],

        "process_label":   "Comment s'ouvre un parcours",
        "process_heading": "Quatre étapes, une seule séquence",
        "process": [
            ("01", "Discovery call",
             "Vingt à trente minutes gratuites en visioconférence. "
             "Nous vérifions si l'objectif relève du coaching ou bien "
             "de la thérapie/du conseil, si Solaria est le cabinet "
             "adéquat, nous discutons un devis indicatif."),
            ("02", "Contrat initial",
             "Premier rendez-vous de quatre-vingt-dix minutes payant, "
             "sous sept jours ouvrés après la discovery call. "
             "Définition de l'objectif SMART, choix du référentiel, "
             "signature du contrat de coaching écrit."),
            ("03", "Parcours régulier",
             "Sessions à la cadence concertée au contrat. Chaque "
             "session se clôt par un commitment écrit que le coaché "
             "vérifie de manière autonome. Re-contracting à "
             "mi-parcours avec le coaché (et le sponsor pour le corporate)."),
            ("04", "Clôture & follow-up",
             "Session finale avec vérification explicite du résultat "
             "par rapport à l'objectif initial. Follow-up 60 min à "
             "trois mois de la clôture — inclus dans les honoraires "
             "du parcours, jamais facturé séparément."),
        ],

        "cta_heading":   "Quel format vous correspond ?",
        "cta_intro":
            "Si vous n'êtes pas certain·e du parcours à choisir, la "
            "discovery call est la voie canonique pour l'évaluer "
            "ensemble. Nous vous écoutons et indiquons le format le "
            "plus cohérent — même si la réponse est « un autre "
            "professionnel répond mieux à votre besoin ».",
        "cta_primary":   "Réserver une discovery call",
        "cta_primary_href": "contatti",
    },

    # ─── CASI ───────────────────────────────────────────────────
    "casi": {
        "eyebrow":  "Cas suivis · 2022 — 2026",
        "headline": "Trois parcours, <em>trois objectifs mesurés</em>.",
        "intro":
            "Une sélection de cas conclus ces trois dernières années. "
            "Les coachés sont identifiés par code secteur et fonction "
            "selon le Code Déontologique ICF §2.4 (confidentialité), "
            "mais les objectifs initiaux et les résultats mesurés "
            "sont réels. Reference call avec le sponsor d'entreprise "
            "disponible pour les parcours corporate après discovery "
            "call et NDA réciproque.",

        "cases_label": "Cas",
        "cases_intro":
            "Sélection équilibrée sur les trois formats principaux — "
            "executive 1:1, team coaching, groupe d'entreprise. Pas "
            "des témoignages mythologiques (« ma vie a changé ») : "
            "des parcours documentés avec objectif initial déclaré, "
            "parcours réalisé, résultat vérifié.",

        "cta_heading":   "Un cas similaire au vôtre ?",
        "cta_intro":
            "Si un cas décrit ici ressemble à votre situation, la "
            "discovery call est la voie canonique pour l'explorer. "
            "Aucune obligation d'ouvrir un parcours après l'appel — "
            "seulement une évaluation honnête de l'adéquation du "
            "coaching à votre besoin spécifique.",
        "cta_primary":   "Réserver une discovery call",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "executive-neo-ceo-tech-scaleup",
            "title":    "Executive 1:1 · PDG fraîchement nommé d'une scale-up tech milanaise",
            "category": "Executive 1:1",
            "thumb":    _POOL_DETAIL,
            "year":     "2025",
            "duration": "8 sessions · 16 semaines + follow-up",
            "client_code":
                "Tech & produit · Milano · scale-up fintech · Série B · "
                "PDG 42 ans · promu en interne après le départ du fondateur",
            "lead":
                "Le fondateur sortant après un tour Série B a vu le CTO "
                "promu en interne comme nouveau PDG. Le néo-PDG avait "
                "une expérience technique et produit mais aucune "
                "expérience de direction générale, et le conseil "
                "d'administration demandait une vérification de son "
                "positionnement sous six mois.",
            "sections": [
                {
                    "label": "L'objectif initial",
                    "heading": "De CTO à direction générale en six mois",
                    "body":
                        "L'objectif déclaré dans le contrat de coaching "
                        "était de travailler sur l'identité de fonction "
                        "(de CTO à PDG), sur la délégation opérationnelle "
                        "(le néo-PDG avait tendance à rester dans la "
                        "technicité produit) et sur la relation avec le "
                        "conseil d'administration (trois membres "
                        "indépendants plus deux des fonds Série B). "
                        "Résultat mesurable concerté : retour du conseil "
                        "à l'issue du semestre avec une évaluation "
                        "« confirmé dans la fonction » plutôt qu'« en "
                        "observation »."
                    ,
                },
                {
                    "label": "Le parcours",
                    "heading": "Co-Active + Immunity to Change",
                    "body":
                        "Huit sessions bimensuelles avec un référentiel "
                        "combiné. Les quatre premières sessions "
                        "(Co-Active) ont travaillé sur les valeurs que "
                        "le néo-PDG portait dans la fonction et sur leur "
                        "traduction en comportements de leadership "
                        "observables. Les quatre suivantes (Immunity to "
                        "Change de Kegan & Lahey) ont identifié et "
                        "désamorcé les résistances inconscientes au "
                        "changement d'identité. Re-contracting à "
                        "mi-parcours avec confirmation de l'objectif "
                        "d'origine et affinement des indicateurs "
                        "opérationnels. Supervision ICF-MCC sur le cas "
                        "avant la sixième session.",
                },
                {
                    "label": "Le résultat",
                    "heading": "Fonction confirmée avec observations positives",
                    "body":
                        "À l'issue du parcours, le conseil "
                        "d'administration a confirmé à l'unanimité le "
                        "PDG dans sa fonction avec un bonus de "
                        "performance plein. Le PDG a restructuré son "
                        "agenda en réduisant de 40 % le temps en calls "
                        "techniques et en réallouant ce temps à la "
                        "relation avec le fonds lead investor et avec "
                        "les membres indépendants du conseil. Deux ans "
                        "plus tard (follow-up à trois mois + check-ins "
                        "annuels spontanés), il est toujours en fonction "
                        "et la société a clôturé positivement la Série C.",
                },
            ],
            "kpi": [
                ("8/8",      "sessions du parcours conclues"),
                ("100 %",    "objectif initial atteint"),
                ("-40 %",    "temps en calls techniques opérationnels"),
                ("24 mois",  "permanence dans la fonction depuis la clôture"),
            ],
            "lead_partner": "Dr. Giulia Loreti · ICF-PCC",
            "team":         "1 coach · 1 superviseure ICF-MCC · 16 semaines",
            "next_label":   "Cas suivant",
        },
        {
            "slug":     "team-coaching-middle-management-manifattura",
            "title":    "Team coaching · middle management d'un industriel en restructuration",
            "category": "Team coaching",
            "thumb":    _POOL_AMBIENT,
            "year":     "2024",
            "duration": "6 sessions · 6 mois + re-contracting + follow-up",
            "client_code":
                "Manufacture & industrie · Brescia · 320 salariés · "
                "équipe de sept middle managers post-réorganisation · "
                "sponsor : directeur des opérations",
            "lead":
                "Un groupe industriel de Brescia avait réorganisé sa "
                "structure de production en consolidant trois sites en "
                "deux. Les sept middle managers des lignes de production "
                "se retrouvaient à coordonner des équipes mixtes "
                "(personnes issues de sites différents avec des "
                "processus différents). Le directeur des opérations, "
                "comme sponsor d'entreprise, a engagé Solaria pour un "
                "team coaching de six mois.",
            "sections": [
                {
                    "label": "L'objectif initial",
                    "heading": "Une équipe qui parle, pas sept référents séparés",
                    "body":
                        "Avant l'engagement, les sept middle managers "
                        "fonctionnaient comme « sept référents séparés "
                        "du directeur des opérations », sans échange "
                        "latéral d'informations et sans escalade "
                        "cohérente des problèmes. L'objectif déclaré "
                        "dans le contrat tripartite (équipe · sponsor · "
                        "coach) était de passer à un modèle d'équipe "
                        "coordonnée avec des pratiques d'échange "
                        "latéral mesurables sous six mois. KPI concerté "
                        "avec le sponsor : fréquence des échanges "
                        "latéraux documentés + diminution des escalades "
                        "« silencieuses » au directeur.",
                },
                {
                    "label": "Le parcours",
                    "heading": "GROW appliqué à l'équipe + artefacts opérationnels",
                    "body":
                        "Six sessions de 120 minutes à cadence "
                        "mensuelle, plus un re-contracting de 90 "
                        "minutes avec le sponsor à mi-parcours. "
                        "Référentiel GROW appliqué à la dynamique de "
                        "groupe (Goal collectif · Reality collective · "
                        "Options collectives · Will collectif) pour "
                        "chaque session. Trois artefacts opérationnels "
                        "co-créés par l'équipe ont été introduits : un "
                        "stand-up quotidien de dix minutes, une "
                        "rétrospective hebdomadaire de trente minutes, "
                        "une matrice d'escalade concertée avec le "
                        "sponsor. Reporting agrégé mensuel au sponsor "
                        "(jamais de contenus spécifiques selon code de déontologie ICF).",
                },
                {
                    "label": "Le résultat",
                    "heading": "Équipe coordonnée avec artefacts opérationnels qui tiennent",
                    "body":
                        "À l'issue du parcours, l'équipe maintenait en "
                        "autonomie les trois artefacts opérationnels "
                        "sans intervention du coach. Les escalades "
                        "silencieuses au directeur sont passées d'une "
                        "moyenne d'environ six par semaine à une "
                        "moyenne inférieure à une par semaine. Au "
                        "follow-up à trois mois, six des sept managers "
                        "étaient encore dans l'équipe et les artefacts "
                        "opérationnels avaient été absorbés dans la "
                        "pratique normale. Le sponsor a renouvelé le "
                        "mandat pour une seconde équipe dans la division logistique.",
                },
            ],
            "kpi": [
                ("6/6",      "sessions du parcours conclues"),
                ("-85 %",    "escalades silencieuses documentées"),
                ("3/3",      "artefacts opérationnels tenus au follow-up"),
                ("6/7",      "managers encore dans l'équipe au follow-up"),
            ],
            "lead_partner": "Dr. Giulia Loreti · ICF-PCC",
            "team":         "1 coach · 1 superviseure ICF-MCC · 6 mois",
            "next_label":   "Cas suivant",
        },
        {
            "slug":     "gruppo-aziendale-neo-manager-studio-legale",
            "title":    "Groupe d'entreprise · cinq nouvelles associées d'un cabinet d'avocats",
            "category": "Groupe d'entreprise",
            "thumb":    _POOL_FEATURE,
            "year":     "2023",
            "duration": "Masterclass + 8 sessions/personne · 8 mois",
            "client_code":
                "Services professionnels · Milano · cabinet d'avocats associé · "
                "cinq avocates fraîchement promues associées la même année · "
                "sponsor : managing partner RH",
            "lead":
                "Un cabinet d'avocats milanais de taille moyenne-grande "
                "avait promu la même année cinq avocates au statut "
                "d'associée (un effort délibéré sur la pipeline féminine "
                "du partnership). Le managing partner RH a engagé "
                "Solaria pour un parcours de groupe d'entreprise de huit "
                "mois : masterclass d'ouverture commune plus huit "
                "sessions 1:1 pour chacune des cinq coachées, avec "
                "follow-up trimestriel au sponsor.",
            "sections": [
                {
                    "label": "L'objectif initial",
                    "heading": "De senior à associée, avec visibilité différenciée",
                    "body":
                        "Les cinq coachées, malgré le même passage de "
                        "rôle, partaient avec des besoins individuels "
                        "différents : certaines avec des défis de "
                        "délégation envers les seniors qu'elles avaient "
                        "elles-mêmes été le mois précédent, d'autres "
                        "avec des défis de visibilité dans les comités "
                        "décisionnels du cabinet, d'autres avec des "
                        "tensions d'identité par rapport à la carrière "
                        "partnership future. Objectif concerté avec le "
                        "sponsor : chaque coachée avec un plan personnel "
                        "de développement écrit + un set de pratiques "
                        "observables activées sous huit mois. Tableau "
                        "de bord agrégé pour le sponsor (jamais de "
                        "contenus spécifiques de session).",
                },
                {
                    "label": "Le parcours",
                    "heading": "Masterclass commune + huit 1:1 personnalisés",
                    "body":
                        "Masterclass d'une journée ouverte aux cinq "
                        "coachées au cabinet, avec référentiel de "
                        "fonction + code de déontologie ICF + attentes "
                        "réciproques coach-coachée. À la suite, huit "
                        "sessions 1:1 de soixante minutes pour chaque "
                        "coachée à cadence concertée individuellement. "
                        "Distribution de la charge : trois coachées "
                        "suivies par Giulia (ICF-PCC) et deux par "
                        "Martina (ICF-ACC en parcours PCC), avec "
                        "supervision mensuelle de la cohorte de "
                        "Martina. Tableau de bord progrès au sponsor "
                        "avec trois KPI agrégés concertés.",
                },
                {
                    "label": "Le résultat",
                    "heading": "Cinq plans individuels actifs, trois promotions",
                    "body":
                        "À l'issue du parcours, les cinq coachées "
                        "avaient un plan de développement personnel "
                        "écrit et actif avec des pratiques observables. "
                        "Trois des cinq ont été promues à equity "
                        "partner dans les trois années suivantes "
                        "(follow-ups spontanés 2024 · 2025 · 2026), une "
                        "a choisi de quitter le cabinet pour une "
                        "direction générale d'une équipe juridique "
                        "interne, et une est encore associée senior "
                        "avec un mandat déclaré de développement. Le "
                        "sponsor a renouvelé le mandat en 2024 pour "
                        "une nouvelle cohorte de quatre associées.",
                },
            ],
            "kpi": [
                ("40/40",    "sessions du parcours conclues (5 × 8)"),
                ("5/5",      "plans personnels actifs à la clôture"),
                ("3/5",      "promues à equity partner sous 3 ans"),
                ("1/1",      "renouvellement de mandat l'année suivante"),
            ],
            "lead_partner": "Dr. Giulia Loreti · Dr. Martina Erriquez",
            "team":         "2 coachs · 1 superviseure ICF-MCC + 1 superviseure EMCC · 8 mois",
            "next_label":   "Cas suivant",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Discovery call",
        "headline": "Vingt à trente minutes, <em>sans engagement</em>, sans frais.",
        "intro":
            "La discovery call est une conversation exploratoire — pas "
            "une session de coaching gratuite et pas un diagnostic. "
            "Nous vérifions ensemble si votre objectif relève du "
            "coaching, si Solaria est le cabinet adéquat, et nous "
            "discutons un devis indicatif. À l'issue, vous êtes libre "
            "de choisir un autre coach, une autre discipline "
            "professionnelle, ou de n'ouvrir aucun parcours — aucune "
            "pression commerciale.",

        "form_label":   "Réserver une discovery call",
        "form_heading": "Remplissez la fiche de cadrage",
        "form_intro":
            "Vous recevrez confirmation du secrétariat du cabinet sous "
            "24 heures ouvrées, avec trois propositions de créneaux "
            "pour la discovery call (visioconférence de 20-30 minutes). "
            "Les données sont traitées au titre du Règl. UE 679/2016 "
            "(RGPD) et conservées dans une archive chiffrée accessible "
            "uniquement aux coachs du cabinet.",
        "form_fields": [
            {"name": "name",      "label": "Prénom",        "type": "text",  "required": True,  "placeholder": "P. ex. Giulia",
             "helper": "Prénom uniquement."},
            {"name": "surname",   "label": "Nom",           "type": "text",  "required": True,  "placeholder": "P. ex. Loreti",
             "helper": "Tel qu'il apparaît dans votre signature professionnelle."},
            {"name": "company",   "label": "Entreprise ou contexte professionnel", "type": "text", "required": False,
             "placeholder": "P. ex. Scale-up fintech milanaise",
             "helper": "Facultatif — nous aide à préparer la discovery call."},
            {"name": "role",      "label": "Fonction actuelle", "type": "text", "required": True,  "placeholder": "P. ex. PDG fraîchement promu · Middle manager · Associé de cabinet",
             "helper": "La fonction actuelle ou celle vers laquelle vous évoluez."},
            {"name": "email",     "label": "E-mail",        "type": "email", "required": True,  "placeholder": "giulia.loreti@exemple.fr",
             "helper": "Nous y envoyons confirmation et trois propositions de créneaux."},
            {"name": "phone",     "label": "Téléphone",     "type": "tel",   "required": False, "placeholder": "+33 ...",
             "helper": "Facultatif — uniquement si vous préférez que le secrétariat vous rappelle."},
            {"name": "format",    "label": "Format préféré", "type": "select", "required": True,
             "options": [
                 "À décider lors de la discovery call",
                 "Executive 1:1",
                 "Team coaching (je suis sponsor ou RH d'entreprise)",
                 "Groupe d'entreprise (je suis sponsor ou RH d'entreprise)",
                 "Session unique exploratoire",
             ],
             "helper": "Choisir « À décider » si vous n'êtes pas sûr·e du format adéquat."},
            {"name": "availability", "label": "Disponibilités sur les 7 prochains jours", "type": "select", "required": True,
             "options": [
                 "Matin 9h00 – 12h00",
                 "Début d'après-midi 14h00 – 16h00",
                 "Fin d'après-midi 16h30 – 19h00",
                 "Soirée 19h30 – 21h00 (en ligne uniquement)",
                 "Indifférent",
             ],
             "helper": "Aide le secrétariat à proposer les trois créneaux les plus proches de vos disponibilités."},
            {"name": "objective", "label": "Objectif en une-deux lignes", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "P. ex. « J'ai été promu PDG en janvier et je dois travailler la délégation opérationnelle ; le conseil m'évalue en juillet. »",
             "helper": "Une-deux lignes suffisent pour vérifier si l'objectif relève du coaching. Aucun détail réservé ici — cela se discute en discovery call sous NDA."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contact",
             "meta": "La personne que nous rencontrerons en discovery call.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Contexte",
             "meta": "Facultatif — nous aide à préparer l'appel. Aucun détail réservé ici.",
             "fields": ["company", "role"]},
            {"num": "03", "title": "Périmètre de l'appel",
             "meta": "Pour vous proposer le bon créneau avec la bonne coach. Une-deux lignes suffisent pour l'objectif.",
             "fields": ["format", "availability", "objective"]},
            {"num": "04", "title": "Pièces jointes (facultatives)",
             "meta": "Fiche de poste actuelle, brief du sponsor, autres documents : ils peuvent préparer la discovery call.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "allegati_preliminari",
            "label":    "Documents préliminaires",
            "helper":   "Fiche de poste, brief sponsor, éventuelle "
                        "évaluation 360° : tout ce que vous anticipez "
                        "ici rend la discovery call plus utile. "
                        "PDF · max 10 Mo total. Archive chiffrée "
                        "accessible uniquement aux coachs.",
            "accept":   ".pdf",
            "multiple": True,
            "primary":  "Glissez vos documents ici ou",
            "link":     "parcourez votre archive",
            "meta":     "PDF · max 10 Mo · archive chiffrée AES-256",
        },

        "form_submit_label": "Réserver une discovery call",
        "form_submit_note":
            "Confirmation du secrétariat du cabinet sous 24 heures "
            "ouvrées, avec trois propositions de créneaux pour "
            "l'appel. Aucune automatisation commerciale, aucune "
            "séquence d'e-mails — chaque demande est lue personnellement.",
        "form_consent":
            "Je consens au traitement de mes données personnelles au "
            "titre du Règl. UE 679/2016 (RGPD). Les données sont "
            "conservées dans l'archive chiffrée du cabinet et ne "
            "sont accessibles qu'aux coachs Solaria. Aucune donnée "
            "n'est communiquée à des tiers sans autorisation explicite.",

        "office_address_label": "Adresse",
        "office_area_label":    "Quartier",
        "office_phone_label":   "Téléphone",
        "office_email_label":   "E-mail",

        "offices_label":   "Cabinet",
        "offices": [
            {
                "city":    "Milano",
                "tag":     "Cabinet · également en ligne",
                "address": "Via Thaon di Revel 21 · 20159",
                "area":    "Isola · à 300 mètres de la station MM Garibaldi FS",
                "phone":   "+39 02 3663 4712",
                "email":   "discovery@solariacoaching.it",
            },
        ],

        "channels_label": "Canaux directs",
        "channels": [
            ("Secrétariat du cabinet", "+39 02 3663 4712",               "Lun – Ven · 9h00 – 19h00"),
            ("E-mail discovery",       "discovery@solariacoaching.it",   "Réponse sous 24 heures ouvrées"),
            ("LinkedIn Giulia Loreti", "in/giulialoreti-icf-pcc",        "Pour questions publiques non réservées"),
        ],

        "footnote":
            "Solaria ne répond pas aux demandes anonymes et ne propose "
            "pas de « diagnostic gratuit en dix questions » "
            "(diagnostiquer relève du conseil, pas du coaching). Les "
            "informations administratives (devis indicatif, modalités "
            "de facturation, critères d'acceptation) sont expliquées "
            "en discovery call — gratuite, sans engagement, avec une "
            "évaluation honnête de l'adéquation du coaching à votre "
            "besoin spécifique.",
    },
}
