"""Pragma — Corporate Suite (business / corporate-suite archetype) FR content.

Phase 2i.2 — French locale for the Pragma institutional advisory template.
Mirrors the exact shape of ``PRAGMA_CONTENT_IT`` (same keys, same nesting,
same list arities); only copy is translated into a classical French
institutional advisory voice (vous, associé / directoire / conseil
d'administration vocabulary, no startup slang).
"""
from __future__ import annotations

from typing import Any


PRAGMA_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Cabinet",       "kind": "home"},
        {"slug": "chi-siamo",     "label": "À propos",      "kind": "about"},
        {"slug": "competenze",    "label": "Compétences",   "kind": "services"},
        {"slug": "case-studies",  "label": "Références",    "kind": "case_study_list"},
        {"slug": "contatti",      "label": "Contact",       "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial": "P",
        "logo_word":    "Pragma Advisors",
        "tag":          "Conseil aux dirigeants · Milan",
        "phone":        "+39 02 3611 9900",
        "email":        "segreteria@pragmaadvisors.it",
        "address":      "Via Filodrammatici 10 · 20121 Milan",
        "hours_compact":"Lun. – Ven. · 9\u00a0h – 19\u00a0h · sur rendez-vous",
        "hours_footer_rows": [
            "Samedi · uniquement conseils programmés",
            "Dimanche · fermé",
        ],
        "license":      "Inscription au registre CONSOB des conseillers indépendants n°\u00a01148/2009",
        "footer_intro":
            "Boutique de conseil indépendante au service des directions "
            "générales et des conseils d'administration d'ETI consolidées. "
            "Stratégie, M&A, gouvernance et ESG. Siège à Milan, présences "
            "permanentes à Francfort et Zurich.",
        # Footer column headings — per-template (not shared chrome) because
        # each business template has a different sense of what "the studio" is
        "foot_studio":   "Le cabinet",
        "foot_pages":    "Sections",
        "foot_contact":  "Contact",
        "foot_offices":  "Bureaux",
        "offices_footer_rows": [
            "Milan · Porta Nuova",
            "Frankfurt am Main · Bockenheim",
            "Zurich · Paradeplatz",
        ],
        # Case study cross-page meta labels (rendered on case_study_list +
        # case_study_detail meta-strips). Lifted from skin in Session 40 so
        # every locale picks up the right translation. Kept on `site` because
        # the labels appear in the chrome of TWO different page kinds.
        "case_practice_label":     "Pratique",
        "case_year_label":         "Année",
        "case_duration_label":     "Durée",
        "case_lead_label":         "Lead",
        "case_lead_partner_label": "Associé référent",
        "case_team_label":         "Équipe & calendrier",
        "case_timeline_label":     "Calendrier",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Conseil aux dirigeants · Milan · Francfort · Zurich",
        "headline":    "Là où se prennent les décisions <em>qui comptent</em>.",
        "intro":
            "Nous accompagnons les directions générales et les conseils "
            "d'administration d'ETI consolidées dans leurs choix structurants "
            "— plans stratégiques, opérations de M&A, gouvernance et "
            "trajectoires ESG. Une boutique indépendante, vingt ans de "
            "mandats confidentiels.",
        "primary_cta":   "Prendre rendez-vous",
        "primary_href":  "contatti",
        "secondary_cta": "Télécharger la présentation",
        "secondary_href":"chi-siamo",

        # Right-hand boardroom photo + credit overlay
        "hero_image":              "https://images.pexels.com/photos/6950031/pexels-photo-6950031.jpeg?auto=compress&cs=tinysrgb&w=1600",
        "hero_image_credit_left":  ("Photographie",  "Conseil industriel lombard · 2025"),
        "hero_image_credit_right": ("Année de fondation", "2004"),
        "hero_meta_strip": [
            ("Siège social",      "Milan · Porta Nuova"),
            ("Équipe associée",   "14 associés"),
            ("Mandats en cours",  "42 missions"),
        ],

        # Advisory pillars — three-practice grid
        "pillars_label":   "Pratiques",
        "pillars_heading": "Trois compétences, une seule signature",
        "pillars_intro":
            "Une seule équipe pluridisciplinaire pour chaque mandat. "
            "Les associés ne vendent pas — ils siègent à la table du "
            "premier entretien à la signature.",
        "pillars": [
            ("01", "Conseil aux conseils",
             "Nous accompagnons les conseils d'administration et les directions "
             "générales dans les décisions de rupture — plans stratégiques "
             "triennaux, réorganisations actionnariales, successions "
             "d'entreprise, gestion des crises réputationnelles."),
            ("02", "Croissance & M&A",
             "Due diligence, valorisation, négociation et intégration post-deal "
             "en 10 à 12 semaines, avec des équipes dédiées par secteur. "
             "Nous intervenons côté cédant ou côté acquéreur, jamais les deux "
             "sur un même dossier."),
            ("03", "Gouvernance & ESG",
             "Conformité CSRD, reporting intégré, modèles 231, structuration "
             "des comités spécialisés du conseil et politiques de durabilité "
             "pour groupes industriels et services financiers."),
        ],

        # KPI strip on dark navy band
        "kpi_heading": "Vingt ans de mandats confidentiels",
        "kpi_strip": [
            ("22",       "années d'activité"),
            ("180+",     "mandats clôturés"),
            ("1,4\u00a0Md\u00a0€", "valeur transactée"),
            ("94\u00a0%", "taux de réengagement"),
        ],

        # Sectors ribbon
        "sectors_label": "Secteurs d'intervention",
        "sectors": [
            "Industrie & manufacture",
            "Services financiers",
            "Énergie & utilities",
            "Retail & consumer",
            "Santé & pharma",
        ],

        # Trust band — institutional client logos as text wordmarks
        "trust_label":   "Ils ont choisi Pragma au cours des cinq dernières années",
        "trust_logos":   [
            "GROUPE INDUSTRIEL DE BRESCIA",
            "FONDS MEZZANINE ITALIE",
            "BIOTECH TURIN",
            "CAISSE AGRICOLE D'ÉMILIE",
            "ÉNERGIE RENOUVELABLE NORD",
            "GROUPE FAMILIAL TOSCAN — RETAIL",
        ],

        # Leadership preview — three managing partners on home
        "leadership_label":   "Direction",
        "leadership_heading": "Les associés qui siégeront à votre table",
        "leadership_intro":
            "Chaque mandat est suivi personnellement par au moins un "
            "managing partner. Aucun dirigeant de substitution, aucun "
            "junior laissé seul au dossier.",
        "leadership": [
            {
                "name":  "Dr. Federico Seregni",
                "role":  "Managing partner · Conseil aux conseils",
                "bio":
                    "Vingt ans chez McKinsey & Company comme senior partner "
                    "industrie. Administrateur indépendant de trois sociétés "
                    "cotées. Spécialiste des plans stratégiques et des "
                    "successions familiales dans la manufacture italienne.",
                "credentials": [
                    "Bocconi (CLEACC '95)",
                    "Insead MBA '01",
                    "Conseiller Confindustria Lombardia",
                ],
            },
            {
                "name":  "Me. Caterina Foschini",
                "role":  "Managing partner · Croissance & M&A",
                "bio":
                    "Plus de 70 opérations de M&A bouclées entre l'Italie "
                    "et la zone DACH. Ancienne de Bonelli Erede, elle a "
                    "conduit deux exits stratégiques du private equity "
                    "italien dans le secteur consumer.",
                "credentials": [
                    "Cattolica (Droit '98)",
                    "LL.M. Frankfurt am Main",
                    "AIDC, IBA M&A Forum",
                ],
            },
            {
                "name":  "Ing. Marco Lavezzi",
                "role":  "Managing partner · Gouvernance & ESG",
                "bio":
                    "Ancien responsable développement durable d'un groupe "
                    "utility coté. Il coordonne les projets CSRD, le reporting "
                    "intégré et les modèles 231 pour les clients de la "
                    "pratique gouvernance.",
                "credentials": [
                    "Politecnico Milano (Ing. de gestion '02)",
                    "Certifié GRI · CDP",
                    "Membre CASUR-ANRI",
                ],
            },
        ],

        # Case studies preview — three on home, full list on /case-studies
        "cases_label":   "Travaux récents",
        "cases_heading": "Trois mandats, trois trajectoires",
        "cases_intro":
            "Une sélection récente de missions clôturées. Par souci de "
            "confidentialité, les noms des clients ne sont communiqués "
            "qu'après signature d'un NDA.",

        # Final CTA band before footer
        "cta_label":     "Un entretien préliminaire",
        "cta_heading":   "Trente minutes, ordre du jour resserré, sans engagement",
        "cta_intro":
            "Le premier échange se tient avec un associé senior. Nous "
            "discutons du périmètre, du calendrier et d'un éventuel "
            "conflit d'intérêts — avant toute proposition économique.",
        "cta_primary":   "Demander l'entretien",
        "cta_primary_href": "contatti",
        "cta_secondary": "Télécharger le dossier institutionnel",
        "cta_secondary_href": "chi-siamo",
    },

    # ─── CHI SIAMO (about + values) ─────────────────────────────
    "chi-siamo": {
        "eyebrow":   "Le cabinet · 2004 — 2026",
        "headline":  "Une boutique <em>indépendante</em>, vingt-deux ans de mandats confidentiels.",
        "intro":
            "Pragma Advisors voit le jour à Milan en 2004, à l'initiative "
            "de professionnels issus du conseil, de la finance et du droit. "
            "Depuis, le cabinet a grandi par cooptation — jamais par "
            "acquisition — en préservant son indépendance à l'égard de "
            "tout capital tiers.",

        # Studio history — 5-step timeline
        "history_label":   "Histoire du cabinet",
        "history_heading": "Cinq étapes, vingt-deux années",
        "history_intro":
            "Cinq dates qui ont façonné Pragma. Derrière chacune de ces "
            "étapes se tient un choix structurel — d'indépendance, de "
            "géographie, de pratique — qui oriente encore aujourd'hui "
            "notre manière d'accepter les mandats.",
        "history": [
            ("2004", "Fondation",
             "Federico Seregni et trois associés ouvrent Pragma via Filodrammatici, "
             "avec quatre mandats de conseil aux conseils déjà signés."),
            ("2009", "Inscription au registre CONSOB",
             "Reconnaissance par le registre des conseillers financiers "
             "indépendants — la pratique M&A peut désormais se présenter "
             "en qualité de conseil formel."),
            ("2014", "Ouverture du bureau de Francfort",
             "Caterina Foschini conduit l'ouverture du bureau DACH pour "
             "les mandats transfrontaliers italo-allemands de la manufacture."),
            ("2019", "Pratique Gouvernance & ESG",
             "Marco Lavezzi rejoint le cabinet comme managing partner pour "
             "constituer la pratique ESG, avec les premiers mandats CSRD "
             "auprès de deux groupes utility."),
            ("2024", "Ouverture du bureau de Zurich",
             "Pour accompagner les mandats de structuration patrimoniale des "
             "familles entrepreneuriales italiennes, nous ouvrons le bureau "
             "de Paradeplatz."),
        ],

        # Method / values
        "values_label":   "Méthode",
        "values_heading": "Quatre principes <em>non négociables</em>",
        "values_intro":
            "Ce sont les quatre règles qui distinguent un mandat Pragma "
            "d'une mission standard de conseil en stratégie. Vous les "
            "retrouverez écrites sur le papier à en-tête du mandat signé, "
            "pas sur ce site.",
        "values": [
            ("01", "Indépendance du capital",
             "Le capital du cabinet est intégralement détenu par les associés "
             "actifs. Aucun apport de groupe, aucun fonds de private equity "
             "en minoritaire, aucun actionnaire extérieur. Le choix des "
             "mandats n'est jamais influencé par l'agenda de tiers."),
            ("02", "Un associé par mandat",
             "Un managing partner siège à la table de l'ouverture du dossier "
             "à la signature du closing. Pas de partner-of-record qui "
             "s'éclipse après le pitch — l'associé senior rencontré en "
             "premier entretien est celui qui paraphera la clôture du mandat."),
            ("03", "Jamais de conflit, jamais",
             "Dans un même secteur, nous n'accompagnons jamais deux clients "
             "en concurrence directe. Sur une opération de M&A, jamais "
             "cédant + acquéreur sur le même dossier. Notre Compliance "
             "Officer interne vérifie chaque nouveau mandat avant acceptation."),
            ("04", "Honoraires transparents",
             "Tarif journalier déclaré dans la proposition, success fee "
             "uniquement sur les opérations exceptionnelles et toujours "
             "divulguée en facture. Aucune rétrocession de commission, "
             "aucun accord verbal avec des contreparties financières."),
        ],

        # Full team — 6 senior advisors + the 3 managing partners (also home)
        "team_label":   "Équipe associée",
        "team_heading": "Quatorze associés, trois bureaux, une seule gouvernance",
        "team_intro":
            "Les personnes qui travailleront à votre mandat. Les associés "
            "ne sont pas de simples consultants, et nous ne vous confions "
            "pas à un département — ils siègent à la table du début à la fin.",
        "team": [
            {"name": "Dr. Federico Seregni",
             "role": "Managing partner · Conseil aux conseils",
             "office": "Milan",
             "bio": "Ancien senior partner McKinsey, vingt ans de plans "
                    "stratégiques. Administrateur indépendant de trois "
                    "sociétés cotées."},
            {"name": "Me. Caterina Foschini",
             "role": "Managing partner · M&A",
             "office": "Frankfurt",
             "bio": "70+ opérations bouclées entre l'Italie et la zone DACH. "
                    "Ancienne de Bonelli Erede, spécialiste du cross-border "
                    "consumer."},
            {"name": "Ing. Marco Lavezzi",
             "role": "Managing partner · Gouvernance & ESG",
             "office": "Milan",
             "bio": "Il coordonne la pratique CSRD et les modèles 231. "
                    "Ancien responsable développement durable d'un groupe "
                    "utility coté."},
            {"name": "Dr. Sabina Erlanger",
             "role": "Senior partner · Structuration patrimoniale",
             "office": "Zurich",
             "bio": "Vingt ans dans la banque privée helvétique. Elle "
                    "coordonne les mandats de transmission générationnelle "
                    "pour les familles italiennes."},
            {"name": "Dr. Lorenzo Pellizzari",
             "role": "Senior partner · Industrie & manufacture",
             "office": "Milan",
             "bio": "Ancien directeur général d'un groupe métallurgique "
                    "de Brescia. Pratique stratégique pour la filière "
                    "lombarde et vénète."},
            {"name": "Dr. Giulia Antinori",
             "role": "Senior partner · Services financiers",
             "office": "Milan",
             "bio": "Ancienne McKinsey financial-services. Mandats de "
                    "transformation pour banques régionales et sociétés "
                    "de gestion italiennes."},
        ],

        # Coordinates strip
        "coordinates_label": "Les bureaux",
        "coordinates": [
            ("Milan",      "Via Filodrammatici 10 · 20121 · Porta Nuova"),
            ("Frankfurt",  "Bockenheimer Landstr. 51 · 60325 · Westend"),
            ("Zurich",     "Paradeplatz 8 · 8001 · Innenstadt"),
        ],

        # Page-level CTA
        "cta_heading": "Une évaluation préliminaire confidentielle",
        "cta_intro":
            "Les trente premières minutes avec un associé sont une "
            "conversation exploratoire, non une proposition commerciale. "
            "On y discute du périmètre du mandat, du calendrier et d'un "
            "éventuel conflit d'intérêts.",
        "cta_primary":  "Demander l'entretien",
        "cta_primary_href": "contatti",
    },

    # ─── COMPETENZE (services) ──────────────────────────────────
    "competenze": {
        "eyebrow":  "Practice areas · 2026",
        "headline": "Six compétences, <em>une seule signature</em>.",
        "intro":
            "Les six pratiques de Pragma. Chaque client accède à une "
            "équipe pluridisciplinaire — vous ne payez pas chaque pratique "
            "séparément, le mandat couvre la combinaison de compétences "
            "nécessaires.",

        # Card meta labels (lifted from skin Session 40 for locale support)
        "svc_duration_label": "Durée",
        "svc_leader_label":   "Associé référent",

        # 6 services in airy cards
        "services": [
            {
                "num":   "01",
                "title": "Conseil aux conseils",
                "blurb":
                    "Nous accompagnons conseils d'administration et directions "
                    "générales dans les décisions de rupture. Plans stratégiques "
                    "triennaux, réorganisations actionnariales, successions "
                    "familiales, gestion de crise réputationnelle et mandats ad interim.",
                "scope": [
                    "Plans stratégiques et revue d'orientation",
                    "Succession familiale et gouvernance",
                    "Mandats ad interim CFO / COO",
                    "Communication de crise au conseil",
                ],
                "duration": "8 à 14 semaines par cycle",
                "leader":   "Dr. Federico Seregni",
            },
            {
                "num":   "02",
                "title": "Croissance & M&A",
                "blurb":
                    "Due diligence, valorisation, négociation et intégration "
                    "post-deal. Nous intervenons côté vendor ou côté buyer, "
                    "jamais les deux sur le même dossier. Typologies : "
                    "carve-out, JV, exit de private equity, MBO familiaux.",
                "scope": [
                    "Vendor due diligence et teaser",
                    "Buyer-side scouting et valorisation",
                    "Négociation et SPA assistance",
                    "Intégration post-merger 100 jours",
                ],
                "duration": "10 à 24 semaines selon périmètre",
                "leader":   "Me. Caterina Foschini",
            },
            {
                "num":   "03",
                "title": "Gouvernance & ESG",
                "blurb":
                    "Mise en conformité CSRD, reporting intégré, modèles "
                    "organisationnels 231, structuration des comités "
                    "spécialisés. Pour les groupes industriels cotés et les "
                    "family businesses qui préparent leur cotation sur "
                    "Euronext Growth.",
                "scope": [
                    "Conformité CSRD et reporting intégré",
                    "Modèles organisationnels 231",
                    "Comités spécialisés et politiques",
                    "Gouvernance pré-IPO",
                ],
                "duration": "12 à 18 semaines par cycle",
                "leader":   "Ing. Marco Lavezzi",
            },
            {
                "num":   "04",
                "title": "Structuration patrimoniale",
                "blurb":
                    "Planification patrimoniale pour familles entrepreneuriales "
                    "italiennes à périmètre international. Holding patrimoniale, "
                    "trust, family office, transmission générationnelle.",
                "scope": [
                    "Holding patrimoniale et pactes d'actionnaires",
                    "Trusts et fondations familiales",
                    "Family office et comité d'advisory",
                    "Transmission générationnelle et succession",
                ],
                "duration": "16 à 36 semaines par réorganisation",
                "leader":   "Dr. Sabina Erlanger",
            },
            {
                "num":   "05",
                "title": "Industrie & manufacture",
                "blurb":
                    "Pratique verticale dédiée à la filière industrielle "
                    "lombarde et vénète. Diagnostic opérationnel, refonte "
                    "de supply chain, make-or-buy stratégiques, "
                    "internationalisation productive.",
                "scope": [
                    "Diagnostic opérationnel multi-sites",
                    "Refonte de supply chain",
                    "Make-or-buy stratégique",
                    "Ouverture de sites à l'étranger",
                ],
                "duration": "10 à 20 semaines par projet",
                "leader":   "Dr. Lorenzo Pellizzari",
            },
            {
                "num":   "06",
                "title": "Services financiers",
                "blurb":
                    "Transformation stratégique pour banques régionales, "
                    "sociétés de gestion italiennes et fintech régulées. "
                    "Repositionnement stratégique, M&A bancaire, reporting "
                    "prudentiel Banque d'Italie.",
                "scope": [
                    "Repositionnement stratégique bancaire",
                    "M&A bancaire et sociétés de gestion",
                    "Conformité Banque d'Italie / ABE",
                    "Modèles opérationnels front-to-back",
                ],
                "duration": "12 à 24 semaines selon périmètre",
                "leader":   "Dr. Giulia Antinori",
            },
        ],

        # Process strip — how a mandate is run
        "process_label":   "Notre manière de travailler",
        "process_heading": "Quatre phases, une seule séquence",
        "process": [
            ("01", "Entretien exploratoire",
             "Trente minutes confidentielles avec un managing partner. "
             "On y discute du périmètre, pas de proposition économique."),
            ("02", "Proposition écrite",
             "Sous cinq jours, une proposition de mandat de trois pages "
             "avec périmètre, livrables, calendrier et grille tarifaire transparente."),
            ("03", "Exécution",
             "Équipe dédiée de l'ouverture à la clôture. Le managing "
             "partner siège à chaque comité de pilotage, jamais un junior."),
            ("04", "Closing & suivi",
             "Note de clôture confidentielle au conseil + suivi trimestriel "
             "sans frais pendant les 12 mois suivants."),
        ],

        # Final CTA
        "cta_heading":   "Quelle pratique vous concerne ?",
        "cta_intro":
            "Si le périmètre n'est pas arrêté, envoyez-nous une brève "
            "description du problème. Nous vous orientons vers le bon "
            "associé sous 48 heures — même si nous ne travaillons pas "
            "ensemble.",
        "cta_primary":   "Nous écrire",
        "cta_primary_href": "contatti",
    },

    # ─── CASE-STUDIES (list) ────────────────────────────────────
    "case-studies": {
        "eyebrow":  "Mandats sélectionnés · 2022 — 2026",
        "headline": "Trois mandats, <em>trois trajectoires</em>.",
        "intro":
            "Une sélection de mandats clôturés au cours des quatre "
            "dernières années. Les clients sont identifiés par code "
            "sectoriel (en respect des NDA) mais les métriques de "
            "sortie sont réelles et vérifiables lors d'un reference call.",

        # Card-list of case studies (full posts in `posts` below)
        "cases_label": "Cas",
        "cases_intro":
            "Sélection équilibrée sur les trois axes principaux — "
            "conseil aux conseils, M&A, gouvernance. La liste complète "
            "est disponible au format PDF sur demande depuis la page contact.",

        "cta_heading":   "Un cas comparable au vôtre ?",
        "cta_intro":
            "Les dossiers complets (périmètre, KPI, reference call avec "
            "le CFO du client) sont accessibles après signature d'un NDA "
            "réciproque. La signature intervient lors du premier entretien, "
            "avant toute proposition.",
        "cta_primary":   "Demander les dossiers intégraux",
        "cta_primary_href": "contatti",
    },

    # Posts powering case_study_detail. URL: /case-studies/<slug>/
    "posts": [
        {
            "slug":     "manifatturiero-bresciano-piano-industriale",
            "title":    "Groupe manufacturier de Brescia · plan stratégique 2025-28",
            "category": "Conseil aux conseils",
            "year":     "2025",
            "duration": "14 semaines",
            "client_code": "Industrie & manufacture · Brescia · 320 salariés · 78\u00a0M€ de revenus",
            "lead":
                "Trois sites industriels, deux familles actionnaires en "
                "désaccord sur le périmètre futur. Pragma a réaligné le "
                "plan stratégique triennal avant le renouvellement du "
                "mandat du conseil.",
            "sections": [
                {
                    "label": "Le problème",
                    "heading": "Deux familles, trois plans contradictoires",
                    "body":
                        "Le groupe est né en 1968 de la fusion de deux "
                        "entreprises familiales. En 2024, le conseil se "
                        "présentait avec trois plans stratégiques "
                        "alternatifs sur la table : fermeture du site le "
                        "plus ancien, ouverture d'un quatrième site en "
                        "Roumanie, ou carve-out de la division composants "
                        "pour cession à un fonds de private equity. Les "
                        "deux familles actionnaires défendaient des "
                        "scénarios incompatibles et le mandat du conseil "
                        "arrivait à échéance dans douze mois.",
                },
                {
                    "label": "L'approche",
                    "heading": "Diagnostic opérationnel + revue de gouvernance",
                    "body":
                        "Pragma a travaillé en trois directions parallèles. "
                        "La pratique industrie & manufacture a conduit un "
                        "diagnostic opérationnel de neuf semaines sur les "
                        "trois sites, avec mesure du TRS, costing par ligne "
                        "et benchmark de filière. En parallèle, la pratique "
                        "conseil aux conseils a médié entre les deux "
                        "familles à travers trois cycles d'ateliers "
                        "d'alignement. La pratique gouvernance a revu le "
                        "pacte d'actionnaires et proposé un nouveau "
                        "règlement intérieur du conseil avec des quorums "
                        "renforcés.",
                },
                {
                    "label": "Le résultat",
                    "heading": "Plan triennal approuvé à l'unanimité",
                    "body":
                        "Plan stratégique 2025–28 approuvé à l'unanimité "
                        "par le conseil et par l'assemblée générale "
                        "extraordinaire. Le site le plus ancien a été "
                        "reconverti (non fermé) à la production de "
                        "composants pour l'éolien — 4\u00a0M€ de capex "
                        "financés par le fonds Simest. Le carve-out de "
                        "la division composants a été mis de côté. Le "
                        "nouveau pacte d'actionnaires a réduit les quorums "
                        "de blocage de 40\u00a0%.",
                },
            ],
            "kpi": [
                ("4\u00a0M€",    "capex de reconversion financés"),
                ("0",            "site fermé (3 maintenus)"),
                ("100\u00a0%",   "approbation du plan en conseil"),
                ("12 mois",      "avant le renouvellement du mandat"),
            ],
            "lead_partner": "Dr. Federico Seregni · Dr. Lorenzo Pellizzari",
            "team":         "3 associés · 4 seniors · 2 juniors · 14 semaines",
            "next_label":   "Mandat suivant",
        },
        {
            "slug":     "carve-out-consumer-italia-dach",
            "title":    "Carve-out division consumer · opération cross-border Italie-DACH",
            "category": "Croissance & M&A",
            "year":     "2024",
            "duration": "22 semaines",
            "client_code": "Retail & consumer · Vicence · 540 salariés · 112\u00a0M€ de revenus",
            "lead":
                "Carve-out de la division private-label d'un groupe retail "
                "de Vicence, cédée à un acquéreur stratégique allemand. "
                "Pragma est intervenu sell-side, du teaser à l'intégration.",
            "sections": [
                {
                    "label": "Le problème",
                    "heading": "Une division stratégique, un actionnariat divisé",
                    "body":
                        "La division private-label représentait 28\u00a0% "
                        "des revenus mais 51\u00a0% de l'EBITDA du groupe ; "
                        "elle avait grandi sur des clients DACH (DM, Lidl "
                        "Allemagne) qui ne se sentaient pas correctement "
                        "servis par une structure italienne. Une partie "
                        "de l'actionnariat plaidait pour un carve-out avec "
                        "cession à un acquéreur stratégique allemand ; "
                        "une autre préférait préserver le périmètre et "
                        "chercher un partenaire industriel italien.",
                },
                {
                    "label": "L'approche",
                    "heading": "Vendor due diligence + scouting parallèle",
                    "body":
                        "Pragma a conduit une vendor due diligence complète "
                        "(opérationnelle, financière, juridique, fiscale) "
                        "en dix semaines. En parallèle, le scouting a "
                        "approché six acquéreurs potentiels — trois "
                        "acquéreurs stratégiques DACH, deux fonds de "
                        "private equity européens spécialistes consumer, "
                        "et un acquéreur italien. La cession a été gérée "
                        "via une enchère privée de quatre semaines avec "
                        "process letter structurée.",
                },
                {
                    "label": "Le résultat",
                    "heading": "Cession au multiple cible, sans disruption",
                    "body":
                        "Cession conclue au multiple EBITDA cible (8,4x), "
                        "avec clause d'earn-out sur 24 mois. L'intégration "
                        "post-merger a préservé 80\u00a0% des effectifs "
                        "de la division (opérateurs de production + "
                        "commerciaux). 100\u00a0% des contrats avec les "
                        "trois principaux clients DACH ont été reconduits "
                        "dans les six mois suivant le closing.",
                },
            ],
            "kpi": [
                ("8,4\u00a0x",   "multiple EBITDA au closing"),
                ("80\u00a0%",    "effectifs cédés préservés"),
                ("100\u00a0%",   "contrats DACH reconduits post-closing"),
                ("22\u00a0sem.", "du mandat au signing"),
            ],
            "lead_partner": "Me. Caterina Foschini · Dr. Giulia Antinori",
            "team":         "2 associés · 5 seniors · 3 juniors · 22 semaines",
            "next_label":   "Mandat suivant",
        },
        {
            "slug":     "csrd-utility-quotata-roadmap",
            "title":    "Feuille de route CSRD pour un groupe utility coté",
            "category": "Gouvernance & ESG",
            "year":     "2025",
            "duration": "18 semaines",
            "client_code": "Énergie & utilities · Bologne · 1\u00a0800 salariés · 420\u00a0M€ de revenus",
            "lead":
                "Mise en conformité au premier reporting CSRD pour un "
                "groupe utility coté sur Euronext Milan. Double "
                "matérialité, baseline scope 1-2-3, gouvernance de "
                "la durabilité reconfigurée.",
            "sections": [
                {
                    "label": "Le problème",
                    "heading": "Reporting fragmenté, baseline incomplète",
                    "body":
                        "Le groupe avait historiquement produit un "
                        "rapport de durabilité GRI volontaire, mais la "
                        "baseline scope 3 était incomplète, la matérialité "
                        "n'était pas double (impact + financière) et les "
                        "KPI n'étaient pas audit-ready. Le premier "
                        "exercice CSRD obligatoire portait sur l'exercice "
                        "2025, à publier en avril 2026 — dix-huit mois "
                        "disponibles.",
                },
                {
                    "label": "L'approche",
                    "heading": "Double matérialité + baseline + gouvernance",
                    "body":
                        "Pragma a travaillé en trois flux parallèles "
                        "pendant dix-huit semaines. Flux A — analyse de "
                        "double matérialité avec 38 parties prenantes "
                        "consultées (fournisseurs, clients, syndicats, "
                        "ONG environnementales, investisseurs institutionnels). "
                        "Flux B — achèvement de la baseline scope 1-2-3 "
                        "selon la méthodologie GHG Protocol avec validation "
                        "externe. Flux C — reconfiguration de la "
                        "gouvernance : comité durabilité spécialisé "
                        "du conseil, politique ESG actualisée, KPI "
                        "intégrés au plan stratégique.",
                },
                {
                    "label": "Le résultat",
                    "heading": "Premier reporting CSRD audit-ready dans les délais",
                    "body":
                        "Premier reporting CSRD publié avec rapport "
                        "d'assurance limitée par un auditeur externe "
                        "(zéro réserve). 142 datapoints ESRS couverts "
                        "intégralement. Comité durabilité spécialisé "
                        "actif dès le premier trimestre 2026 avec un "
                        "membre indépendant Pragma en qualité "
                        "d'observateur technique pour la première année. "
                        "Score MSCI ESG amélioré de deux crans.",
                },
            ],
            "kpi": [
                ("142",       "datapoints ESRS couverts"),
                ("0",         "réserve de l'auditeur"),
                ("38",        "parties prenantes consultées"),
                ("+\u00a02",  "crans de rating MSCI ESG"),
            ],
            "lead_partner": "Ing. Marco Lavezzi",
            "team":         "1 associé · 4 seniors · 2 juniors · 18 semaines",
            "next_label":   "Mandat suivant",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Entretien préliminaire",
        "headline": "Trente minutes, ordre du jour <em>resserré</em>, sans engagement.",
        "intro":
            "Le premier contact se tient avec un managing partner. "
            "Nous discutons du périmètre du mandat, du calendrier et "
            "d'un éventuel conflit d'intérêts — avant toute proposition "
            "économique.",

        # Form fields — generic loop in chrome
        "form_label":   "Demander l'entretien",
        "form_heading": "Remplissez le formulaire confidentiel",
        "form_intro":
            "Vous recevrez confirmation sous 48 heures ouvrées après "
            "l'envoi. Les informations sensibles sont traitées conformément "
            "au Règlement UE 2016/679 (RGPD) et conservées dans une archive "
            "chiffrée à accès restreint aux associés.",
        "form_fields": [
            {"name": "name",      "label": "Prénom",         "type": "text",     "required": True,  "placeholder": "Ex. Frédéric",
             "helper": "Uniquement le prénom, merci."},
            {"name": "surname",   "label": "Nom",            "type": "text",     "required": True,  "placeholder": "Ex. Seregni",
             "helper": "Tel qu'il apparaît sur l'organigramme."},
            {"name": "company",   "label": "Société",        "type": "text",     "required": True,  "placeholder": "Ex. Groupe Industriel Lombard",
             "helper": "Dénomination enregistrée, pas nom commercial."},
            {"name": "role",      "label": "Fonction",       "type": "text",     "required": True,  "placeholder": "Ex. CFO · CEO · Administrateur",
             "helper": "Position au conseil ou à la direction de référence."},
            {"name": "email",     "label": "E-mail professionnel", "type": "email", "required": True, "placeholder": "frederic.seregni@groupe.fr",
             "helper": "Nous n'acceptons pas les domaines grand public (Gmail, Outlook, Libero) pour ce premier contact."},
            {"name": "phone",     "label": "Téléphone",      "type": "tel",      "required": True,  "placeholder": "+33 ...",
             "helper": "Ligne directe du référent, pas le standard."},
            {"name": "practice",  "label": "Pratique concernée", "type": "select", "required": True,
             "options": [
                 "À définir lors de l'entretien",
                 "Conseil aux conseils",
                 "Croissance & M&A",
                 "Gouvernance & ESG",
                 "Structuration patrimoniale",
                 "Industrie & manufacture",
                 "Services financiers",
             ],
             "helper": "Choisir « À définir » si le périmètre couvre plusieurs pratiques."},
            {"name": "horizon",   "label": "Horizon temporel", "type": "select", "required": True,
             "options": [
                 "Sous un mois",
                 "Sous trois mois",
                 "Sous six mois",
                 "Exploratoire, aucune urgence",
             ],
             "helper": "Nous aide à caler l'associé adéquat sur le mandat."},
            {"name": "perimeter", "label": "Brève description du périmètre", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "600 caractères maximum. Aucun nom de contrepartie — "
                            "ils seront évoqués uniquement après NDA réciproque.",
             "helper": "Juste ce qu'il faut pour vérifier que le mandat relève "
                       "de notre compétence. Les noms de contreparties ne se "
                       "partagent qu'après NDA réciproque."},
        ],

        "form_sections": [
            {"num": "01", "title": "Référent",
             "meta": "La personne qui signera l'éventuel NDA préliminaire.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Société",
             "meta": "Pour le conflict-check préliminaire.",
             "fields": ["company", "role"]},
            {"num": "03", "title": "Périmètre du mandat",
             "meta": "Aucun détail sensible ici — le périmètre technique se partage lors de l'entretien, après NDA réciproque.",
             "fields": ["practice", "horizon", "perimeter"]},
            {"num": "04", "title": "Pièces jointes (facultatives)",
             "meta": "Company profile, one-pager de gouvernance ou NDA standard : ils peuvent préparer l'entretien.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "briefing_allegato",
            "label":    "Documents préliminaires",
            "helper":   "Company profile, one-pager de gouvernance ou NDA standard. "
                        "PDF / DOCX · 15\u00a0Mo au total maximum. Archive chiffrée "
                        "à accès restreint aux associés Pragma.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Déposez les documents ici ou",
            "link":     "parcourez l'archive",
            "meta":     "PDF / DOCX · 15\u00a0Mo max · archive chiffrée",
        },

        "form_submit_label": "Demander l'entretien",
        "form_submit_note":
            "Confirmation d'un managing partner sous 48 heures ouvrées. "
            "Aucun BDR externe, aucune automatisation de sequence.",
        "form_consent":
            "J'accepte le traitement de mes données personnelles conformément "
            "au Règlement UE 2016/679 (RGPD). Les données sont conservées "
            "dans une archive chiffrée à accès restreint aux associés Pragma. "
            "Aucune donnée n'est communiquée à des tiers sans autorisation "
            "explicite.",

        # Office meta-row labels (lifted from skin Session 40 for i18n)
        "office_address_label": "Adresse",
        "office_area_label":    "Quartier",
        "office_phone_label":   "Téléphone",
        "office_email_label":   "E-mail",

        # Sidebar — offices + contact channels
        "offices_label":   "Les bureaux",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Headquarters",
                "address": "Via Filodrammatici 10 · 20121",
                "area":    "Porta Nuova · à deux pas de la Piazza della Scala",
                "phone":   "+39 02 3611 9900",
                "email":   "milano@pragmaadvisors.it",
            },
            {
                "city":    "Frankfurt",
                "tag":     "DACH desk",
                "address": "Bockenheimer Landstr. 51 · 60325",
                "area":    "Westend · à deux pas de l'Alte Oper",
                "phone":   "+49 69 8870 4400",
                "email":   "frankfurt@pragmaadvisors.it",
            },
            {
                "city":    "Zurich",
                "tag":     "Wealth desk",
                "address": "Paradeplatz 8 · 8001",
                "area":    "Innenstadt · à deux pas de la Bahnhofstrasse",
                "phone":   "+41 44 215 7700",
                "email":   "zurich@pragmaadvisors.it",
            },
        ],

        "channels_label": "Canaux directs",
        "channels": [
            ("Secrétariat advisory", "+39 02 3611 9900",            "Lun. – Ven. · 9\u00a0h – 19\u00a0h"),
            ("E-mail institutionnel", "segreteria@pragmaadvisors.it", "Réponse sous 48 heures"),
            ("LinkedIn de cabinet",  "in/pragma-advisors",           "Pour les relations publiques"),
        ],

        "footnote":
            "Pragma Advisors ne répond pas aux demandes anonymes et ne "
            "délivre pas d'opinion préliminaire par e-mail sans un premier "
            "entretien avec un associé. Les informations administratives "
            "(honoraires indicatifs, modalités de facturation, critères "
            "d'acceptation du mandat) sont présentées lors du premier "
            "entretien, non par écrit.",
    },
}
