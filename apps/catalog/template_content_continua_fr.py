"""Continua — Family-office stewardship (corporate-suite archetype) ·
French locale content tree.

Phase X.4b Continua Pass B · 2026-04-30 · Multilingual rollout pass on
top of the approved LF-5 Italian layout. Mirrors the shape of
``CONTINUA_CONTENT_IT`` exactly — same keys, same nesting, same list
shapes. Only values are translated and adapted.

Voice register: institutional, custodial, longitudinal,
multi-générationnel. Native French equivalent of the IT register —
le français des family offices genevois et parisiens (Mirabaud,
Edmond de Rothschild Family Advisory). Adulte à adulte, déclaratif,
jamais SaaS-marketing. Reference voices: Les Échos Patrimoine, Le
Revenu Famille, La Tribune Wealth.

Voice anchor (CS-EXEC-01 / CS-BLOCK-11 · preserved verbatim-in-translation
across all 5 locales · the load-bearing italic moves with the equivalent
TEMPORAL noun):
    "La continuité d'une famille se mesure en <em>générations</em>."

Italian normative references and proper nouns are preserved (D.lgs.
24/2023 whistleblowing, Codice della Crisi, OAM mediazione creditizia,
Albo dei Trustees, STEP, ANC audit, Codice Deontologico, Reg. UE
679/2016, Consiglio di Famiglia / Conseil de Famille). Italian addresses,
phone formats, Euro figures and years are kept as-is. Anti-pattern
guardrails carry across: pas de « Libérez votre potentiel
patrimonial », pas de « Pérennisez votre héritage », pas de « La
meilleure version de votre family office », pas de citations
Rothschild / Mirabaud / Pictet, pas de clichés boardroom de banque privée.
"""
from __future__ import annotations

from typing import Any


from apps.catalog.template_content_continua import (  # noqa: E402
    _HERO_IMAGE,
    _PILLAR_ICON_01,
    _PILLAR_ICON_02,
    _PILLAR_ICON_03,
    _PILLAR_ICON_04,
    _PORTRAIT_ELEONORA,
    _PORTRAIT_TOMAS,
    _PORTRAIT_GINEVRA,
)


CONTINUA_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Le cabinet",      "kind": "home"},
        {"slug": "chi-siamo",  "label": "À propos",         "kind": "about"},
        {"slug": "custodia",   "label": "Garde",            "kind": "services"},
        {"slug": "mandati",    "label": "Mandats",          "kind": "case_study_list"},
        {"slug": "contatti",   "label": "Contact",          "kind": "contact"},
    ],

    "site": {
        "logo_initial": "C",
        "logo_word":    "Continua",
        "tag":          "Family office multi-générationnel · Milan",
        "phone":        "+39 02 7600 4188",
        "email":        "mandato@continua.it",
        "address":      "Via San Marco 22 · 20121 Milan",
        "hours_compact":"Lun – Ven · 9h30 – 18h30 · sur rendez-vous",
        "hours_footer_rows": [
            "Samedi · uniquement Conseils de Famille programmés",
            "Dimanche · fermé",
        ],
        "license":      "Inscrit Albo dei Trustees · STEP Affiliate · audit de continuité ANC",
        "footer_intro":
            "Gardiens du patrimoine familial à travers les générations. "
            "Une boutique de stewardship indépendante, mandats de garde "
            "à horizon multi-générationnel, gouvernance familiale "
            "présidée par le Conseil de Famille. Siège principal à "
            "Milan, partenariats fiduciaires à Lugano et Luxembourg.",
        "foot_studio":   "Le cabinet",
        "foot_pages":    "Sections",
        "foot_contact":  "Contact",
        "foot_offices":  "Bureaux",
        "offices_footer_rows": [
            "Milan · Brera (siège principal)",
            "Lugano · Riva Caccia (correspondant fiduciaire)",
            "Luxembourg · Boulevard Royal (correspondant trustee)",
        ],
        "whistleblowing_footer": {
            "heading":      "Signalements",
            "eyebrow":      "Canal interne · D.lgs. 24/2023",
            "note":
                "Canal chiffré géré par le Compliance Officer. "
                "Réservé aux membres de la famille sous mandat et aux "
                "stewards Continua. Procès-verbal fiduciaire.",
            "email":        "whistleblowing@continua.it",
            "policy_label": "Protection du signalant",
            "policy_href":  "contatti",
        },
        "case_practice_label":     "Profil",
        "case_year_label":         "Mandat ouvert en",
        "case_duration_label":     "Années en continuité",
        "case_lead_label":         "Steward référent",
        "case_lead_partner_label": "Senior Steward",
        "case_team_label":         "Équipe & cadence",
        "case_timeline_label":     "Étapes de continuité",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Family office · Milan · stewardship multi-générationnel",
        "headline":
            "La continuité d'une famille se mesure en <em>générations</em>.",
        "intro":
            "Gardiens du patrimoine familial à travers les générations. "
            "Une boutique de stewardship indépendante — un Conseil de "
            "Famille, un mandat qui ne se mesure pas en trimestres, une "
            "vigilance fiduciaire qui traverse le passage entre pères, "
            "enfants et petits-enfants.",
        "primary_cta":   "Engagez un dialogue de mandat",
        "primary_href":  "contatti",
        "secondary_cta": "Le cabinet de garde",
        "secondary_href":"chi-siamo",

        "hero_image":              _HERO_IMAGE,
        "hero_image_credit_left":  ("Stewards du mandat", "Inscrit Albo dei Trustees"),
        "hero_image_credit_right": ("Siège principal",     "Milan · Brera"),
        "hero_meta_strip": [
            ("Horizon mandat",       "18 ans en moyenne"),
            ("Générations en garde", "3"),
            ("Conseils de Famille",  "4 / an"),
        ],

        "pillars_label":   "Garde",
        "pillars_heading": "Quatre piliers, <em>un seul</em> mandat",
        "pillars_intro":
            "Quatre pratiques qui travaillent en continuité sur le même "
            "patrimoine. Aucun pilier n'est facturé séparément — le "
            "mandat couvre la combinaison de garde, gouvernance, "
            "succession et conformité pour l'horizon convenu avec la famille.",
        "pillars": [
            ("01", "Garde patrimoniale",
             "Nous gardons le patrimoine familial dans ses quatre "
             "strates — actifs financiers liquides, participations "
             "industrielles, immeubles d'exploitation et immeubles "
             "familiaux — à travers le cycle des générations, en "
             "cohérence avec le pacte de famille en vigueur et les "
             "mandats fiduciaires sous-jacents."),
            ("02", "Gouvernance familiale",
             "Nous facilitons le Conseil de Famille à cadence "
             "trimestrielle, rédigeons et révisons le pacte de famille, "
             "concevons les voting structures des branches et les codes "
             "de conduite partagés entre générations en charge et "
             "générations entrantes."),
            ("03", "Succession structurée",
             "Nous planifions le passage multi-générationnel — donations "
             "modulées, holdings de famille, trusts dédiés, formation "
             "technique et de gouvernance pour la génération entrante "
             "avant le transfert effectif de la responsabilité décisionnelle."),
            ("04", "Conformité fiduciaire",
             "Vigilance fiduciaire continue, audit de continuité annuel "
             "indépendant, présidio normatif évolutif (D.lgs. 24/2023 "
             "whistleblowing, Codice della Crisi, OAM médiation de "
             "crédit) et garde documentaire à accès contrôlé sur les "
             "registres familiaux."),
        ],

        "pillars_matrix": [
            {
                "num":   "01",
                "title": "Garde patrimoniale",
                "body":
                    "Quatre strates gardées simultanément — financier "
                    "liquide, participations industrielles, immeubles "
                    "d'exploitation et familiaux — en cohérence avec "
                    "le pacte de famille.",
                "icon_image": _PILLAR_ICON_01,
            },
            {
                "num":   "02",
                "title": "Gouvernance familiale",
                "body":
                    "Conseil de Famille trimestriel. Procès-verbal "
                    "fiduciaire. Pacte de famille à révision triennale. "
                    "Voting structures dédiées par branche.",
                "icon_image": _PILLAR_ICON_02,
            },
            {
                "num":   "03",
                "title": "Succession structurée",
                "body":
                    "Holding de famille, trusts dédiés, donations "
                    "modulées. Programme biennal de formation "
                    "technique de la génération entrante.",
                "icon_image": _PILLAR_ICON_03,
            },
            {
                "num":   "04",
                "title": "Conformité fiduciaire",
                "body":
                    "Audit de continuité ANC annuel. Présidio AML, "
                    "Codice della Crisi, D.lgs. 24/2023. Garde "
                    "documentaire à accès contrôlé.",
                "icon_image": _PILLAR_ICON_04,
            },
        ],

        "kpi_heading": "Dix-huit ans de mandats en continuité",
        "kpi_strip": [
            ("18",      "ans · horizon moyen mandat"),
            ("3",       "générations · familles en garde"),
            ("€ 1,8 Md","patrimoine en garde"),
            ("4",       "Conseils de Famille · par an"),
        ],

        "cycle_label":   "Cycle de gouvernance",
        "cycle_heading": "La continuité a une <em>cadence</em>, pas une échéance.",
        "cycle_intro":
            "Trois rythmes qui régissent le mandat — non KPI, non "
            "échéances fiscales, non sessions de coaching. Ce sont les "
            "battements réguliers d'un Conseil de Famille, répétés au "
            "fil des années et traversés par les générations.",
        "cycle_strip": [
            ("Cadence Conseil de Famille", "4 réunions / an",
             "Calendrier de gouvernance partagé avec la famille · "
             "procès-verbal fiduciaire · ordre du jour ouvert aux deux "
             "générations en charge."),
            ("Audit de continuité", "annuel",
             "Vérification indépendante de la cohérence pluriannuelle "
             "du mandat (ANC) · revue de la garde documentaire · "
             "résultat communiqué au Conseil de Famille de décembre."),
            ("Pacte de famille", "révision triennale",
             "Mise à jour des règles internes, avec ou sans la "
             "génération entrante à table · clauses de vote et de "
             "protection des branches rediscutées tous les trois ans."),
        ],

        "sectors_label": "Profils familiaux",
        "sectors": [
            "Familles entrepreneuriales",
            "Holdings de participations",
            "Fondations de famille",
            "Groupes multi-actifs",
            "Deuxièmes générations en transfert",
            "Trustees indépendants",
            "Bureaux de représentation",
            "Single family offices étrangers",
        ],

        "trust_label":   "Reconnaissances institutionnelles",
        "trust_logos":   [
            "ALBO DEI TRUSTEES",
            "STEP AFFILIATE",
            "AUDIT DE CONTINUITÉ ANC",
            "OAM MÉDIATEURS DE CRÉDIT",
            "ASSOCIAZIONE BANCHE FIDUCIARIE",
            "FAMILY OFFICE NETWORK ITALIA",
        ],

        "whistleblowing": {
            "eyebrow":      "Protection du signalant",
            "channel_name": "Canal interne · D.lgs. 24/2023",
        },

        "leadership_label":   "Stewards du mandat",
        "leadership_heading": "Trois stewards qui siégeront à votre Conseil de Famille.",
        "leadership_intro":
            "Chaque mandat est suivi personnellement par au moins un "
            "Senior Steward, qui siège au Conseil de Famille de "
            "l'ouverture du dossier à la transition entre générations. "
            "Aucun steward de remplacement, aucune intervention "
            "extérieure non convenue.",
        "leadership": [
            {
                "name":  "Eleonora Marchesi",
                "role":  "Senior Steward",
                "station": "Salle des archives · Brera",
                "bio":
                    "Trente-cinq ans de pratique fiduciaire entre Milan "
                    "et Lugano. Inscrite à l'Albo dei Trustees depuis "
                    "2007, elle a présidé sept mandats de continuité "
                    "sur trois générations complètes et onze passages "
                    "intergénérationnels documentés.",
                "credentials": [
                    "Albo dei Trustees · inscription 2007",
                ],
                "portrait": _PORTRAIT_ELEONORA,
            },
            {
                "name":  "Tomas Okafor",
                "role":  "Family Officer",
                "station": "Table du Conseil · siège principal",
                "bio":
                    "Quatorze ans de pratique entre family offices "
                    "anglo-saxons et advisory continental. STEP "
                    "Affiliate depuis 2014, il coordonne la "
                    "facilitation du Conseil de Famille et la formation "
                    "technique de la génération entrante avant le "
                    "transfert de responsabilité.",
                "credentials": [
                    "STEP Affiliate · 2014",
                ],
                "portrait": _PORTRAIT_TOMAS,
            },
            {
                "name":  "Ginevra Conti",
                "role":  "Compliance Officer",
                "station": "Cabinet de conformité · garde documentaire",
                "bio":
                    "Vingt-deux ans dans la vigilance fiduciaire des "
                    "patrimoines privés. Inscrite OAM comme médiateur "
                    "de crédit depuis 2011, elle préside au respect du "
                    "D.lgs. 24/2023 (whistleblowing) et à l'audit de "
                    "continuité annuel de chaque mandat en garde.",
                "credentials": [
                    "OAM · inscription médiateurs de crédit",
                ],
                "portrait": _PORTRAIT_GINEVRA,
            },
        ],

        "cases_label":   "Mandats en continuité",
        "cases_heading": "Quatre mandats, quatre générations, <em>une seule cadence</em>.",
        "cases_intro":
            "Une sélection de mandats en continuité — non clôturés, "
            "encore en garde. Les noms des familles ne sont divulgués "
            "que sous pacte de confidentialité fiduciaire.",

        "cases_timeline": [
            {
                "slug":          "famiglia-b-fondazione-di-famiglia",
                "year":          "2011",
                "eyebrow":       "Fondation de famille",
                "title":         "Famille B · 3ᵉ génération · branche philanthropique + industrielle",
                "horizon_label": "Horizon",
                "horizon":       "15 ans en continuité · audit conjoint",
            },
            {
                "slug":          "famiglia-a-quarta-generazione-holding-industriale",
                "year":          "2014",
                "eyebrow":       "Holding industrielle",
                "title":         "Famille A · 4ᵉ génération · six branches familiales",
                "horizon_label": "Horizon",
                "horizon":       "12 ans · renouvellement du mandat 2034",
            },
            {
                "slug":          "famiglia-d-single-family-office-estero",
                "year":          "2017",
                "eyebrow":       "Single family office",
                "title":         "Famille D · garde transfrontalière IT · CH · LU",
                "horizon_label": "Horizon",
                "horizon":       "9 ans · extension AML 2030",
            },
            {
                "slug":          "famiglia-c-trasferimento-intergenerazionale",
                "year":          "2019",
                "eyebrow":       "Transfert intergénérationnel",
                "title":         "Famille C · 2ᵉ → 3ᵉ génération · trusts dédiés",
                "horizon_label": "Horizon",
                "horizon":       "Passage décennal · 2026 — 2029",
            },
        ],

        "cta_label":     "Un premier dialogue confidentiel",
        "cta_heading":   "La continuité d'une famille se mesure en <em>générations</em>.",
        "cta_intro":
            "Le premier dialogue se déroule avec un Senior Steward. "
            "Nous discutons du périmètre du mandat, de l'horizon "
            "temporel et d'un éventuel conflit fiduciaire — avant "
            "toute proposition de Conseil de Famille. Nous ne vendons "
            "pas la première réunion : nous l'offrons une seule fois, par famille.",
        "cta_primary":   "Engagez un dialogue de mandat",
        "cta_primary_href": "contatti",
        "cta_secondary": "Téléchargez le dossier institutionnel",
        "cta_secondary_href": "chi-siamo",
    },

    # ─── CHI SIAMO (about + values) ─────────────────────────────
    "chi-siamo": {
        "eyebrow":   "Le cabinet · 2007 — 2026",
        "headline":  "Une boutique de garde, <em>dix-neuf</em> ans de mandats en continuité.",
        "intro":
            "Continua naît à Milan en 2007 comme bureau de garde pour "
            "deux familles entrepreneuriales lombardes. Depuis, nous "
            "avons présidé au passage entre pères et enfants sur sept "
            "mandats au total, jamais par acquisition, jamais avec "
            "capital de tiers.",

        "history_label":   "Étapes de continuité",
        "history_heading": "Cinq dates, dix-neuf ans de stewardship.",
        "history_intro":
            "Cinq choix structurels derrière lesquels se lit le "
            "caractère du cabinet — l'indépendance vis-à-vis du "
            "capital de tiers, la cadence trimestrielle du Conseil de "
            "Famille, l'audit de continuité annuel, le pacte de "
            "famille triennal, le passage intergénérationnel comme "
            "méthode avant d'être un produit.",
        "history": [
            ("2007", "Fondation",
             "Eleonora Marchesi et deux co-stewards ouvrent le cabinet "
             "Via San Marco à Milan, sur mandat de deux familles "
             "entrepreneuriales lombardes, pour la garde patrimoniale "
             "à horizon vicennal."),
            ("2011", "Inscription OAM médiateurs de crédit",
             "Ginevra Conti rejoint comme Compliance Officer et active "
             "la vigilance fiduciaire continue sur les mandats en "
             "garde, selon le principe de séparation entre garde et advisory."),
            ("2014", "STEP Affiliate · Family Officer",
             "Tomas Okafor rejoint comme Family Officer et introduit "
             "la facilitation du Conseil de Famille — quatre réunions "
             "par an, ordre du jour partagé, procès-verbal fiduciaire."),
            ("2019", "Audit de continuité (ANC)",
             "Le cabinet adopte le protocole ANC pour l'audit de "
             "continuité annuel — vérification indépendante de la "
             "cohérence pluriannuelle de chaque mandat, résultat "
             "toujours communiqué au Conseil de Famille de décembre."),
            ("2024", "Correspondants fiduciaires Lugano + Luxembourg",
             "Pour accompagner les mandats de transfert "
             "intergénérationnel des familles italiennes, nous activons "
             "des partenariats fiduciaires Riva Caccia et Boulevard "
             "Royal — jamais de bureaux propres, toujours des "
             "correspondants accrédités."),
        ],

        "values_label":   "Principes de garde",
        "values_heading": "Quatre principes <em>non négociables</em>",
        "values_intro":
            "Quatre principes qui distinguent un mandat Continua d'une "
            "mission advisory standard. Ils sont écrits dans le pacte "
            "de mandat signé en Conseil de Famille, non sur le site.",
        "values": [
            ("01", "Indépendance vis-à-vis du capital de tiers",
             "Le capital du cabinet est entièrement détenu par les "
             "stewards actifs. Aucun fonds, aucun groupe bancaire, "
             "aucun actionnaire externe. Le choix des mandats n'est "
             "jamais influencé par des agendas tiers susceptibles de "
             "compromettre la garde."),
            ("02", "Un Senior Steward par mandat",
             "Un Senior Steward siège au Conseil de Famille de "
             "l'ouverture du dossier au transfert de responsabilité. "
             "Pas de steward-of-record qui disparaît après le premier "
             "dialogue : le gardien rencontré en première réunion est "
             "le même qui signera le passage intergénérationnel."),
            ("03", "Audit de continuité indépendant",
             "Chaque mandat fait l'objet, une fois par an, d'un audit "
             "de continuité (ANC) conduit par un réviseur externe. Le "
             "résultat est communiqué au Conseil de Famille de "
             "décembre sans filtre : la famille connaît toujours "
             "l'état de garde de son patrimoine."),
            ("04", "Confidentialité fiduciaire",
             "Aucun cas d'étude rendu public, aucune newsletter sur "
             "l'évolution des mandats, aucune référence croisée entre "
             "familles. Les anonymisations présentées sur les pages "
             "publiques sont convenues cas par cas et signées en "
             "Conseil de Famille."),
        ],

        "team_label":   "Stewards & officers",
        "team_heading": "Six gardiens, trois bureaux, une seule cadence.",
        "team_intro":
            "Les personnes qui siégeront à votre Conseil de Famille. "
            "Stewards, non consultants, et nous ne vous confions pas à "
            "un département — le gardien rencontré en première réunion "
            "est celui qui présidera au passage entre les générations.",
        "team": [
            {"name": "Eleonora Marchesi",
             "role": "Senior Steward · Garde",
             "office": "Milan",
             "bio": "Trente-cinq ans de pratique fiduciaire. Inscrite "
                    "à l'Albo dei Trustees depuis 2007 · sept mandats "
                    "de continuité sur trois générations complètes."},
            {"name": "Tomas Okafor",
             "role": "Family Officer · Gouvernance",
             "office": "Milan",
             "bio": "STEP Affiliate depuis 2014. Facilitation du "
                    "Conseil de Famille et formation de la génération "
                    "entrante avant le transfert de responsabilité."},
            {"name": "Ginevra Conti",
             "role": "Compliance Officer · Vigilance fiduciaire",
             "office": "Milan",
             "bio": "OAM médiateurs de crédit depuis 2011. Présidio "
                    "du D.lgs. 24/2023 (whistleblowing) et de l'audit "
                    "de continuité annuel pour chaque mandat en garde."},
            {"name": "Lorenzo Pellegrini",
             "role": "Steward · Succession structurée",
             "office": "Milan",
             "bio": "Dix-huit ans dans le passage générationnel des "
                    "patrimoines industriels lombards. Coordonne "
                    "holdings de famille, trusts dédiés et formation "
                    "technique de la génération entrante."},
            {"name": "Camille Béranger",
             "role": "Correspondante fiduciaire",
             "office": "Luxembourg",
             "bio": "Vingt ans de pratique en droit du trust "
                    "luxembourgeois. Garde les structures "
                    "transfrontalières pour les familles italiennes "
                    "avec résidences fiscales secondaires."},
            {"name": "Sofia Pessina",
             "role": "Junior Steward · Pactes de famille",
             "office": "Milan",
             "bio": "Six ans de pratique dans la rédaction et révision "
                    "des pactes de famille. Accompagne les Senior "
                    "Stewards dans les réunions de Conseil de Famille "
                    "et les cycles de révision triennale."},
        ],

        "coordinates_label": "Bureaux",
        "coordinates": [
            ("Milan",      "Via San Marco 22 · 20121 · Brera"),
            ("Lugano",     "Riva Caccia 1 · 6900 · correspondant fiduciaire"),
            ("Luxembourg", "Boulevard Royal 28 · L-2449 · correspondant trustee"),
        ],

        "cta_heading": "Un premier dialogue confidentiel.",
        "cta_intro":
            "Les premières quarante-cinq minutes avec un Senior "
            "Steward sont un dialogue exploratoire, non une "
            "proposition commerciale. On y discute le périmètre du "
            "mandat, l'horizon temporel et un éventuel conflit "
            "fiduciaire — avant toute convocation de Conseil.",
        "cta_primary":  "Engagez un dialogue de mandat",
        "cta_primary_href": "contatti",
    },

    # ─── CUSTODIA (services · 4 piliers) ────────────────────────
    "custodia": {
        "eyebrow":  "Garde · gouvernance · succession · conformité · 2026",
        "headline": "Quatre pratiques, <em>une seule signature fiduciaire</em>.",
        "intro":
            "Les quatre pratiques de Continua. Chaque famille accède à "
            "une équipe de stewardship qui les préside toutes "
            "simultanément — chaque pilier n'est pas facturé "
            "séparément, le mandat couvre la combinaison de garde, "
            "gouvernance, succession et conformité requise par "
            "l'horizon convenu en Conseil de Famille.",

        "svc_duration_label": "Cadence",
        "svc_leader_label":   "Steward référent",

        "services": [
            {
                "num":   "01",
                "title": "Garde patrimoniale",
                "blurb":
                    "Nous gardons le patrimoine dans ses quatre "
                    "strates — financier liquide, participations "
                    "industrielles, immeubles d'exploitation, "
                    "immeubles familiaux. La garde n'est pas la "
                    "gestion de portefeuille : c'est la prise en "
                    "charge, année après année, de la cohérence entre "
                    "le patrimoine et le pacte de famille en vigueur.",
                "scope": [
                    "Reporting trimestriel co-signé",
                    "Registre de garde numérique à accès contrôlé",
                    "Audit de continuité ANC annuel indépendant",
                    "Coordination des correspondants fiduciaires étrangers",
                ],
                "duration": "Trimestriel · audit annuel",
                "leader":   "Eleonora Marchesi",
            },
            {
                "num":   "02",
                "title": "Gouvernance familiale",
                "blurb":
                    "Nous facilitons le Conseil de Famille à cadence "
                    "trimestrielle, procès-verbal fiduciaire déposé au "
                    "cabinet, rédaction et révision triennale du pacte "
                    "de famille. La gouvernance n'est pas une réunion : "
                    "c'est la répétition régulière d'un battement de "
                    "garde traversé par les générations.",
                "scope": [
                    "Quatre Conseils de Famille par an",
                    "Procès-verbal fiduciaire déposé",
                    "Voting structures dédiées par branche",
                    "Code de conduite intergénérationnel",
                ],
                "duration": "4 Conseils / an · révision triennale du pacte",
                "leader":   "Tomas Okafor",
            },
            {
                "num":   "03",
                "title": "Succession structurée",
                "blurb":
                    "Nous planifions le passage intergénérationnel à "
                    "horizon décennal — donations modulées, holdings "
                    "de famille, trusts dédiés pour branches mineures "
                    "ou non opérationnelles. La succession ne "
                    "s'improvise pas le jour de la signature notariale : "
                    "elle se prépare avec un programme biennal de "
                    "formation technique.",
                "scope": [
                    "Holdings de famille et pactes d'actionnaires",
                    "Trusts dédiés pour branches mineures",
                    "Donations modulées à horizon décennal",
                    "Formation biennale de la génération entrante",
                ],
                "duration": "Horizon décennal · formation biennale",
                "leader":   "Lorenzo Pellegrini",
            },
            {
                "num":   "04",
                "title": "Conformité fiduciaire",
                "blurb":
                    "Vigilance fiduciaire continue sur le respect du "
                    "D.lgs. 24/2023 (whistleblowing), du Codice della "
                    "Crisi, de la réglementation OAM médiation de "
                    "crédit et des directives AML applicables. La "
                    "conformité n'est pas un obstacle administratif : "
                    "c'est la garantie de continuité du mandat entre "
                    "les générations.",
                "scope": [
                    "Canal whistleblowing interne chiffré",
                    "Vigilance AML renforcée sur mouvements transfrontaliers",
                    "Audit de continuité ANC annuel indépendant",
                    "Garde documentaire à accès contrôlé",
                ],
                "duration": "Continu · audit ANC annuel",
                "leader":   "Ginevra Conti",
            },
        ],

        "process_label":   "Comment nous gardons",
        "process_heading": "Quatre phases, une seule séquence.",
        "process": [
            ("01", "Premier dialogue confidentiel",
             "Quarante-cinq minutes avec un Senior Steward. On y "
             "discute le périmètre du mandat et l'horizon temporel, "
             "jamais une proposition économique."),
            ("02", "Pacte de mandat",
             "Sous dix jours, un pacte de mandat fiduciaire de quatre "
             "pages avec périmètre, horizon, cadence des Conseils et "
             "tarification fiduciaire transparente."),
            ("03", "Ouverture du dossier",
             "Installation du premier Conseil de Famille. Le Senior "
             "Steward siège au Conseil de l'ouverture du dossier au "
             "transfert de responsabilité."),
            ("04", "Continuité + audit annuel",
             "Quatre Conseils par an, audit de continuité ANC "
             "indépendant chaque décembre, révision triennale du "
             "pacte de famille. Le mandat ne se clôture pas : il se "
             "renouvelle en continuité."),
        ],

        "cta_heading":   "Quel pilier convient à votre famille ?",
        "cta_intro":
            "Si le périmètre n'est pas clair, écrivez-nous une brève "
            "description du noyau familial et de l'horizon temporel "
            "convenu. Nous vous indiquerons le Steward approprié sous "
            "72 heures — même si nous n'ouvrons pas de mandat.",
        "cta_primary":   "Engagez un dialogue de mandat",
        "cta_primary_href": "contatti",
    },

    # ─── MANDATI (case_study_list) ─────────────────────────────
    "mandati": {
        "eyebrow":  "Mandats en continuité · 2007 — 2026",
        "headline": "Quatre mandats, quatre générations, une seule <em>cadence fiduciaire</em>.",
        "intro":
            "Une sélection des mandats en garde — non clôturés, encore "
            "en continuité. Les noms des familles ne sont divulgués "
            "que sous pacte de confidentialité fiduciaire. Les étapes "
            "présentées sont convenues cas par cas et signées en "
            "Conseil de Famille.",

        "cases_label": "Mandats en garde",
        "cases_intro":
            "Pour chaque mandat nous présentons profil familial, "
            "générations en garde, années de continuité, périmètre "
            "convenu et cadence d'audit. Les familles sont codées par "
            "branche (A · B · C · D) selon l'ordre chronologique "
            "d'entrée en mandat.",

        "cta_heading":   "Un mandat similaire au vôtre ?",
        "cta_intro":
            "Les dossiers complets (périmètre fiduciaire, horizon, "
            "cadence du Conseil, audit ANC le plus récent) sont "
            "accessibles sous pacte de confidentialité fiduciaire "
            "réciproque. La signature a lieu en premier dialogue, "
            "avant toute proposition de mandat.",
        "cta_primary":   "Demandez les dossiers complets",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "famiglia-a-quarta-generazione-holding-industriale",
            "title":    "Famille A · 4ᵉ génération · holding industrielle lombarde",
            "category": "Famille entrepreneuriale",
            "year":     "2014",
            "duration": "12 ans · en continuité",
            "client_code":
                "Holding industrielle · 4ᵉ génération · 6 branches "
                "familiales · patrimoine industriel lombard · "
                "périmètre : continuité + gouvernance + audit triennal.",
            "lead":
                "Une holding industrielle lombarde à la quatrième "
                "génération de garde, six branches familiales, deux "
                "générations simultanément en garde. Continua préside "
                "au passage entre troisième et quatrième génération depuis 2014.",
            "sections": [
                {
                    "label": "Le contexte",
                    "heading": "Six branches, deux générations, un patrimoine partagé",
                    "body":
                        "En 2014 la holding entrait dans la phase de "
                        "passage entre la troisième génération (quatre "
                        "frères fondateurs) et la quatrième (douze "
                        "cousins, six branches familiales). Le pacte "
                        "de famille en vigueur — rédigé en 1989 — ne "
                        "prévoyait pas de voting structures pour la "
                        "quatrième génération et la troisième n'avait "
                        "pas encore convenu de calendrier de transfert. "
                        "Continua a été appelée à présider à la "
                        "cadence du Conseil de Famille et à mettre en "
                        "place le passage.",
                },
                {
                    "label": "La garde",
                    "heading": "Cadence trimestrielle + révision triennale du pacte",
                    "body":
                        "Continua a installé le Conseil de Famille à "
                        "cadence trimestrielle dès 2014, avec "
                        "procès-verbal fiduciaire déposé après chaque "
                        "réunion. En 2017 a été menée la première "
                        "révision triennale du pacte de famille, avec "
                        "voting structures dédiées aux six branches de "
                        "la quatrième génération et clause de "
                        "protection pour les branches non "
                        "opérationnelles. Audit de continuité ANC chaque décembre.",
                },
                {
                    "label": "Le passage",
                    "heading": "Pacte de famille 2023 · transfert progressif",
                    "body":
                        "La révision triennale 2023 du pacte de "
                        "famille a formalisé le calendrier de "
                        "transfert progressif de la responsabilité "
                        "décisionnelle de la troisième à la quatrième "
                        "génération à horizon septennal (2024-2031). "
                        "Le programme biennal de formation technique "
                        "de la quatrième génération a été lancé en "
                        "2024. La continuité du mandat Continua a été "
                        "renouvelée jusqu'en 2034.",
                },
            ],
            "kpi": [
                ("12 ans",  "en continuité · depuis 2014"),
                ("4ᵉ",      "génération en garde"),
                ("6",       "branches familiales · voting structures dédiées"),
                ("2034",    "renouvellement du mandat"),
            ],
            "lead_partner": "Eleonora Marchesi · Senior Steward",
            "team":         "Senior Steward + Family Officer + Compliance Officer · Conseil trimestriel · audit ANC annuel",
            "next_label":   "Mandat suivant",
        },
        {
            "slug":     "famiglia-b-fondazione-di-famiglia",
            "title":    "Famille B · fondation de famille · 3ᵉ génération",
            "category": "Fondation de famille",
            "year":     "2011",
            "duration": "15 ans · en continuité",
            "client_code":
                "Fondation de famille · 3ᵉ génération · 4 branches · "
                "patrimoine philanthropique + participations "
                "industrielles · périmètre : gouvernance + conformité "
                "+ audit triennal.",
            "lead":
                "Une fondation de famille lombarde à la troisième "
                "génération, patrimoine philanthropique flanqué de "
                "participations industrielles d'exploitation. Continua "
                "préside la gouvernance fondative et la conformité "
                "fiduciaire depuis 2011.",
            "sections": [
                {
                    "label": "Le contexte",
                    "heading": "Une fondation, deux natures de patrimoine",
                    "body":
                        "La fondation, constituée en 1986, garde un "
                        "patrimoine philanthropique de 240 M€ et des "
                        "participations de contrôle dans trois "
                        "entreprises industrielles lombardes. La "
                        "troisième génération, en garde depuis 2009, a "
                        "demandé à Continua en 2011 de présider la "
                        "gouvernance fondative et la conformité "
                        "séparée entre la branche philanthropique et "
                        "la branche industrielle.",
                },
                {
                    "label": "La garde",
                    "heading": "Séparation des deux natures · audit conjoint",
                    "body":
                        "Continua a installé deux Conseils de Famille "
                        "distincts — l'un fondatif, l'autre industriel "
                        "— avec réunions trimestrielles concaténées et "
                        "ordre du jour coordonné par le Family "
                        "Officer. L'audit de continuité ANC est "
                        "conjoint sur les deux branches une fois par "
                        "an, avec résultat communiqué à la famille au "
                        "Conseil de décembre.",
                },
                {
                    "label": "Le présidio",
                    "heading": "Conformité D.lgs. 24/2023 + AML renforcée",
                    "body":
                        "Depuis 2023 Continua a étendu le présidio "
                        "fiduciaire à la nouvelle réglementation "
                        "whistleblowing (D.lgs. 24/2023) pour la "
                        "fondation, avec canal de signalement interne "
                        "dédié et procès-verbal auprès du Compliance "
                        "Officer. AML renforcée sur les mouvements de "
                        "la branche industrielle en cohérence avec les "
                        "directives 2024.",
                },
            ],
            "kpi": [
                ("15 ans",   "en continuité · depuis 2011"),
                ("3ᵉ",       "génération en garde"),
                ("240 M€",   "patrimoine philanthropique en garde"),
                ("2",        "Conseils de Famille · cadence trimestrielle"),
            ],
            "lead_partner": "Ginevra Conti · Compliance Officer",
            "team":         "Senior Steward + Family Officer + Compliance Officer · 2 Conseils trimestriels · audit ANC annuel conjoint",
            "next_label":   "Mandat suivant",
        },
        {
            "slug":     "famiglia-c-trasferimento-intergenerazionale",
            "title":    "Famille C · transfert intergénérationnel · 2ᵉ → 3ᵉ génération",
            "category": "Famille en transfert",
            "year":     "2019",
            "duration": "7 ans · en transfert",
            "client_code":
                "Famille entrepreneuriale · 2ᵉ → 3ᵉ génération · 3 "
                "branches · trusts dédiés + holding de famille · "
                "périmètre : succession structurée + formation de la "
                "génération entrante.",
            "lead":
                "Un patrimoine industriel familial en transfert de la "
                "deuxième à la troisième génération, trois branches "
                "familiales, horizon de passage décennal. Continua "
                "coordonne la succession structurée et la formation "
                "technique des successeurs depuis 2019.",
            "sections": [
                {
                    "label": "Le contexte",
                    "heading": "Une transition à horizon décennal",
                    "body":
                        "En 2019 la deuxième génération (trois frères, "
                        "fondateurs de l'entreprise en 1978) a demandé "
                        "à Continua d'organiser le passage décennal "
                        "vers la troisième génération (sept "
                        "successeurs biologiques, dont cinq actifs "
                        "dans le business). La première étape a été "
                        "la séparation entre holding opérationnelle et "
                        "holding de famille, avec trusts dédiés pour "
                        "les deux branches mineures.",
                },
                {
                    "label": "La structure",
                    "heading": "Holding de famille + trusts dédiés",
                    "body":
                        "Continua a présidé la constitution de la "
                        "holding de famille en 2020 et des deux trusts "
                        "dédiés en 2021. Le programme biennal de "
                        "formation technique des cinq successeurs "
                        "actifs a été lancé en 2022, avec sessions "
                        "mensuelles facilitées par le Family Officer "
                        "et une journée annuelle de simulation de "
                        "Conseil de Famille.",
                },
                {
                    "label": "Le renouvellement",
                    "heading": "Pacte de famille 2025 · révision triennale",
                    "body":
                        "La révision triennale du pacte de famille "
                        "2025 a formalisé la voting structure "
                        "post-transfert, le calendrier de passage de "
                        "la responsabilité décisionnelle (2026-2029) "
                        "et les clauses de protection des deux "
                        "branches mineures. La continuité du mandat "
                        "Continua a été renouvelée jusqu'en 2032 avec "
                        "présidio sur l'achèvement du passage.",
                },
            ],
            "kpi": [
                ("7 ans",  "en transfert · depuis 2019"),
                ("2 → 3",  "génération en passage"),
                ("2",      "trusts dédiés · branches mineures"),
                ("2032",   "renouvellement du mandat"),
            ],
            "lead_partner": "Lorenzo Pellegrini · Steward Succession",
            "team":         "Senior Steward + Family Officer + Steward Succession · Conseil trimestriel · formation mensuelle + annuelle",
            "next_label":   "Mandat suivant",
        },
        {
            "slug":     "famiglia-d-single-family-office-estero",
            "title":    "Famille D · single family office étranger · garde transfrontalière",
            "category": "Single family office étranger",
            "year":     "2017",
            "duration": "9 ans · en continuité",
            "client_code":
                "Single family office · 2ᵉ génération · 1 branche "
                "principale · patrimoine transfrontalier IT/CH/LU · "
                "périmètre : garde + conformité + correspondants "
                "fiduciaires Lugano + Luxembourg.",
            "lead":
                "Un single family office italien avec patrimoine "
                "transfrontalier (Italie, Suisse, Luxembourg). "
                "Continua préside la garde patrimoniale et la "
                "conformité fiduciaire en coordonnant les "
                "correspondants de Lugano et Boulevard Royal depuis 2017.",
            "sections": [
                {
                    "label": "Le contexte",
                    "heading": "Un patrimoine en trois juridictions",
                    "body":
                        "En 2017 la famille demandait la coordination "
                        "fiduciaire d'un patrimoine réparti sur trois "
                        "juridictions — Italie (immeubles "
                        "d'exploitation et familiaux), Suisse (actifs "
                        "financiers liquides), Luxembourg (trusts "
                        "dédiés pour les branches non "
                        "opérationnelles). Continua a activé les deux "
                        "correspondants fiduciaires accrédités à "
                        "Lugano (Riva Caccia) et à Boulevard Royal."},
                {
                    "label": "La garde",
                    "heading": "Reporting unifié + audit conjoint",
                    "body":
                        "Continua produit un reporting trimestriel "
                        "unifié sur les trois branches "
                        "juridictionnelles, signé par le Senior "
                        "Steward + Compliance Officer + correspondants "
                        "accrédités. L'audit de continuité ANC est "
                        "conjoint sur les trois branches une fois par "
                        "an, avec résultat communiqué au Conseil de "
                        "janvier (décalé du cycle italien pour "
                        "alignement fiscal transfrontalier).",
                },
                {
                    "label": "L'évolution",
                    "heading": "Directives AML 2024 · présidio renforcé",
                    "body":
                        "Depuis 2024 Continua coordonne le présidio "
                        "AML renforcé selon les directives "
                        "européennes 2024, avec vérification "
                        "trimestrielle des mouvements transfrontaliers "
                        "et double signature fiduciaire pour les "
                        "opérations > 500 K€. Le mandat a été étendu "
                        "à 2030 avec périmètre coordonné sur les "
                        "trois correspondants.",
                },
            ],
            "kpi": [
                ("9 ans",       "en continuité · depuis 2017"),
                ("3",           "juridictions · IT · CH · LU"),
                ("trimestriel", "reporting unifié"),
                ("2030",        "renouvellement du mandat"),
            ],
            "lead_partner": "Eleonora Marchesi · Senior Steward",
            "team":         "Senior Steward + Compliance Officer + 2 correspondants accrédités · audit ANC annuel conjoint",
            "next_label":   "Mandat suivant",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Premier dialogue confidentiel",
        "headline": "Quarante-cinq minutes, agenda <em>familial</em>, sans engagement.",
        "intro":
            "Le premier dialogue se déroule avec un Senior Steward. "
            "Nous discutons du périmètre du mandat, de l'horizon "
            "temporel et d'un éventuel conflit fiduciaire — avant "
            "toute convocation de Conseil. Les informations sensibles "
            "sont gardées en archive chiffrée à accès limité aux stewards.",

        "form_label":   "Engagez un dialogue de mandat",
        "form_heading": "Remplissez le formulaire confidentiel",
        "form_intro":
            "Vous recevrez confirmation d'un Senior Steward sous 72 "
            "heures ouvrées après envoi. Les données sont traitées au "
            "titre du Règl. UE 679/2016 et gardées en archive chiffrée "
            "au cabinet Via San Marco. Aucun BDR externe, aucune "
            "automatisation de séquence — le dialogue s'ouvre avec un "
            "steward, toujours.",

        "form_fields": [
            {"name": "name",      "label": "Prénom",          "type": "text", "required": True,
             "placeholder": "Ex. Eleonora",
             "helper": "Le prénom uniquement, merci."},
            {"name": "surname",   "label": "Nom",             "type": "text", "required": True,
             "placeholder": "Ex. Marchesi",
             "helper": "Tel qu'il figure dans le pacte de famille en vigueur (s'il existe)."},
            {"name": "family",    "label": "Noyau familial",  "type": "text", "required": True,
             "placeholder": "Ex. Famille Marchesi · branche lombarde",
             "helper": "Le nom sous lequel on se présente en Conseil de Famille."},
            {"name": "role",      "label": "Rôle dans la famille", "type": "text", "required": True,
             "placeholder": "Ex. Chef de famille · Successeur désigné · Membre du Conseil",
             "helper": "La position dans le passage entre générations en garde."},
            {"name": "email",     "label": "Email confidentiel", "type": "email", "required": True,
             "placeholder": "eleonora@famigliamarchesi.it",
             "helper": "Une boîte qui reçoit uniquement des communications fiduciaires. Nous n'utiliserons pas de domaines grand public pour le premier contact."},
            {"name": "phone",     "label": "Téléphone direct", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "Ligne directe du référent, pas un standard d'entreprise."},
            {"name": "horizon",   "label": "Horizon temporel", "type": "select", "required": True,
             "options": [
                 "5 ans",
                 "10 ans",
                 "25 ans",
                 "Multi-générationnel (horizon au-delà de 25 ans)",
             ],
             "helper": "L'horizon convenu en famille pour le mandat de garde. Aide à calendariser le bon Senior Steward."},
            {"name": "structure", "label": "Structure actuelle", "type": "select", "required": True,
             "options": [
                 "Holding de famille",
                 "Fondation de famille",
                 "Trust dédié (italien ou étranger)",
                 "Pacte de famille en vigueur",
                 "Aucune formalisation",
             ],
             "helper": "La structure juridique existante (même si non encore formalisée)."},
            {"name": "scope",     "label": "Périmètre familial", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Maximum 800 caractères. Décrivez brièvement la structure actuelle et votre préoccupation de continuité — elle sera gardée en archive chiffrée dès ce formulaire.",
             "helper": "Suffisamment pour évaluer si le mandat est de notre compétence. Les noms des autres branches et les chiffres ne se partagent qu'après pacte de confidentialité fiduciaire réciproque."},
        ],

        "form_sections": [
            {"num": "01", "title": "Référent",
             "meta": "La personne qui signera l'éventuel pacte de confidentialité fiduciaire réciproque avant le premier Conseil.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Famille",
             "meta": "Pour le conflict-check fiduciaire préliminaire.",
             "fields": ["family", "role"]},
            {"num": "03", "title": "Mandat de garde",
             "meta": "L'horizon et la structure — le détail du patrimoine ne se discute qu'en dialogue, jamais par écrit en phase de premier contact.",
             "fields": ["horizon", "structure", "scope"]},
            {"num": "04", "title": "Pièces jointes (facultatives)",
             "meta": "Pacte de famille en vigueur, statut de la fondation, acte constitutif du trust ou dossier successoral : ils anticipent la première réunion et abrègent le dialogue.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "dossier_familiare",
            "label":    "Documents préliminaires",
            "helper":   "Pacte de famille en vigueur, statut de la "
                        "fondation, acte constitutif du trust ou "
                        "dossier successoral. PDF / DOCX · max 20 Mo "
                        "au total. Archive chiffrée à accès limité "
                        "aux stewards Continua.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Glissez les documents ici ou",
            "link":     "parcourez votre archive",
            "meta":     "PDF / DOCX · max 20 Mo · archive chiffrée fiduciaire",
        },

        "form_submit_label": "Engagez un dialogue de mandat",
        "form_submit_note":
            "Confirmation d'un Senior Steward sous 72 heures ouvrées. "
            "Aucun BDR externe, aucune automatisation de séquence — le "
            "dialogue s'ouvre avec un steward, toujours.",
        "form_consent":
            "Je consens au traitement des données personnelles au "
            "titre du Règl. UE 679/2016 et du D.lgs. 196/2003 modifié. "
            "Les données sont gardées en archive chiffrée au cabinet "
            "Via San Marco à accès limité aux stewards Continua. "
            "Aucune donnée n'est communiquée à des tiers sans "
            "autorisation fiduciaire explicite. Je suis informé du "
            "canal whistleblowing (D.lgs. 24/2023) actif au cabinet.",

        "office_address_label": "Adresse",
        "office_area_label":    "Quartier",
        "office_phone_label":   "Téléphone",
        "office_email_label":   "Email",

        "offices_label":   "Bureaux",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Siège principal",
                "address": "Via San Marco 22 · 20121",
                "area":    "Brera · près de Piazza San Marco",
                "phone":   "+39 02 7600 4188",
                "email":   "milano@continua.it",
            },
            {
                "city":    "Lugano",
                "tag":     "Correspondant fiduciaire",
                "address": "Riva Caccia 1 · 6900",
                "area":    "Centre · près de Piazza della Riforma",
                "phone":   "+41 91 922 7700",
                "email":   "lugano@continua.it",
            },
            {
                "city":    "Luxembourg",
                "tag":     "Correspondant trustee",
                "address": "Boulevard Royal 28 · L-2449",
                "area":    "Ville Haute · près de Place d'Armes",
                "phone":   "+352 24 87 5500",
                "email":   "luxembourg@continua.it",
            },
        ],

        "channels_label": "Canaux directs",
        "channels": [
            ("Secrétariat de garde",            "+39 02 7600 4188",            "Lun – Ven · 9h30 – 18h30"),
            ("Email fiduciaire",                "mandato@continua.it",         "Réponse sous 72 heures"),
            ("Whistleblowing (D.lgs. 24/2023)", "whistleblowing@continua.it",  "Canal interne chiffré · procès-verbal du Compliance Officer"),
        ],

        "footnote":
            "Continua ne répond pas aux demandes anonymes et ne "
            "délivre pas d'avis préliminaires écrits sans un premier "
            "dialogue avec un Senior Steward. Les informations "
            "administratives (honoraires indicatifs, modalités de "
            "facturation, critères d'acceptation du mandat) sont "
            "exposées en premier dialogue, jamais par écrit. Le "
            "canal whistleblowing est géré par le Compliance Officer "
            "au titre du D.lgs. 24/2023 et est également accessible "
            "aux seuls membres de la famille sous mandat.",
    },
}
