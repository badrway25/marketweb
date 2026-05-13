"""Phase 2g3.7 · Session 53 · Lex — French native-voice tree. Bar / cabinet / despacho / مكتب voice."""
from __future__ import annotations

from typing import Any


LEX_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "Cabinet",                "kind": "home"},
        {"slug": "studio",    "label": "Le Cabinet",             "kind": "about"},
        {"slug": "pratiche",  "label": "Domaines d'intervention","kind": "services"},
        {"slug": "avvocati",  "label": "Nos Avocats",            "kind": "team"},
        {"slug": "notabili",  "label": "Affaires marquantes",    "kind": "blog_list"},
        {"slug": "contatti",  "label": "Contact",                "kind": "contact"},
    ],

    # ─── SITE — chrome rendered by _base.html ─────────────────────
    "site": {
        "logo_initial":  "LF",
        "logo_word":     "Studio Legale Ferri",
        "tag":           "Barreau de Rome · depuis 1962",
        "phone":         "+39 06 4567 2300",
        "email":         "studio@studioferri.legal",
        "address":       "Via Piemonte 39 · 00187 Roma",
        "hours_compact": "Lundi – Vendredi · 09h00 – 19h00",
        "hours_footer_rows": [
            "Samedi · uniquement sur rendez-vous",
            "Dimanche · fermé",
        ],
        "license":       "Insc. Barreau de Rome A18449 · N° TVA 03124770581",
        "nav_cta":       "Demander une consultation",
        "footer_intro":
            "Studio Legale Ferri — soixante-deux années de "
            "barreau, deux sièges (Rome et Milan), quatorze "
            "avocats inscrits. Compétence, réserve, résultats.",
        "foot_studio":  "Le Cabinet",
        "foot_pages":   "Pages",
        "foot_contact": "Contact",
        "foot_offices": "Sièges",
        "offices_footer_rows": [
            "Rome · via Piemonte 39",
            "Milan · corso Venezia 11",
        ],

        # Cross-page meta labels (lifted from skin so each locale picks
        # up the right translation). Used by blog_list/blog_detail and
        # by services / team chrome strips.
        "case_practice_label":  "Domaine",
        "case_year_label":      "Année",
        "case_outcome_label":   "Issue",
        "case_lead_label":      "Associé en charge",
    },

    # ════════════════════════════════════════════════════════════
    # HOME (studio)
    # ════════════════════════════════════════════════════════════
    "home": {
        "eyebrow":    "Studio Legale Ferri · Rome · Milan · depuis 1962",
        "headline":   "Soixante-deux ans de barreau, <em>une seule signature</em> sur votre dossier.",
        "intro":
            "Nous conseillons entreprises, familles et professionnels "
            "selon une approche rigoureuse, personnalisée et "
            "discrète. Soixante-deux années de barreau, deux sièges, "
            "quatorze avocats inscrits. Chaque dossier est suivi "
            "personnellement par un associé du Cabinet, de "
            "l'ouverture du dossier jusqu'au passage en force de "
            "chose jugée.",
        "primary_cta":   "Demander une consultation confidentielle",
        "primary_href":  "contatti",
        "secondary_cta": "Domaines d'intervention",
        "secondary_href":"pratiche",

        # Hero — split-ledger-monogram silhouette
        # LEFT: gold vertical rule + eyebrow + serif drama headline + credit cells
        # RIGHT: monogram crest + meta_strip institutional rows
        "hero_credit_left":  ("Direction",     "Me Prof. A. Ferri"),
        "hero_credit_right": ("Barreaux",      "Rome · Milan"),
        "hero_meta_strip": [
            ("Siège principal",    "Rome · via Piemonte"),
            ("Associés fondateurs","1962 · famille Ferri"),
            ("Avocats inscrits",   "14 · Barreau de Rome"),
        ],

        # Practice-area ledger — 4 numbered rows on home, full 12 on /pratiche
        "practice_label":   "Domaines d'intervention",
        "practice_heading": "Douze compétences, une seule <em>signature</em>.",
        "practice_intro":
            "Les domaines d'intervention du Cabinet couvrent le "
            "droit civil, commercial, pénal des affaires et "
            "administratif. Chaque dossier est coordonné par un "
            "associé senior et n'est jamais délégué dans son "
            "intégralité à des collaborateurs juniors.",
        "practice": [
            ("01", "Droit des sociétés",
             "Opérations de M&A, gouvernance, contrats commerciaux "
             "et opérations structurantes. Augmentations de capital "
             "selon l'art. 2343 du Code civil italien avec expertise "
             "assermentée, fusions transfrontalières, restructurations "
             "de groupe, pactes d'actionnaires."),
            ("02", "Droit de la famille et successions",
             "Séparations consensuelles et contentieuses, divorces, "
             "fixation de la garde, successions internationales, "
             "trusts familiaux, donations et pactes de famille "
             "selon l'art. 768-bis du Code civil italien."),
            ("03", "Droit du travail",
             "Contentieux individuel et collectif, négociation "
             "collective de second niveau, sécurité au travail "
             "selon le Décret législatif 81/2008, licenciements "
             "pour juste cause et motif légitime, transactions "
             "devant les instances syndicales."),
            ("04", "Droit pénal des affaires",
             "Infractions d'affaires selon les art. 2621-2641 du "
             "Code civil italien, responsabilité administrative "
             "des personnes morales selon le Décret législatif "
             "231/2001, délits en col blanc, infractions fiscales "
             "selon le Décret législatif 74/2000, modèles "
             "organisationnels et organes de surveillance."),
        ],

        # Stats band on dark ink — counter animation (D-081 binding)
        "stats_label":   "Soixante-deux années de barreau",
        "stats_heading": "Le Cabinet en chiffres",
        "stats": [
            ("62",     "années d'activité"),
            ("14",     "avocats inscrits"),
            ("2 400+", "dossiers plaidés"),
            ("96%",    "issues favorables"),
        ],

        # Partners portrait preview — 3 senior partners on home, 14 on /avvocati
        "partners_label":   "Direction",
        "partners_heading": "Trois associés, une seule direction",
        "partners_intro":
            "Les associés du Cabinet signent personnellement chaque "
            "acte. Aucun mandat n'est accepté sans vérification "
            "préalable de conflit d'intérêts et sans attribution "
            "formelle à un associé responsable.",
        "partners": [
            {
                "name":  "Avv. Prof. Alberto Ferri",
                "role":  "Associé gérant · Droit des sociétés",
                "foro":  "Barreau de Rome depuis 1986 · Avocat aux Cours suprêmes depuis 1999",
                "bio":
                    "Fils du fondateur, il dirige le Cabinet depuis "
                    "2004. Professeur associé de droit commercial "
                    "à LUISS Guido Carli. Auteur de l'ouvrage "
                    "\"L'aumento di capitale nelle società quotate\" "
                    "(Giuffrè, 2018).",
            },
            {
                "name":  "Avv. Maria Grazia Conti",
                "role":  "Associée senior · Droit de la famille",
                "foro":  "Barreau de Rome depuis 1991 · Avocate aux Cours suprêmes depuis 2003",
                "bio":
                    "Spécialiste des successions internationales et "
                    "des pactes de famille. Collaboratrice de la "
                    "revue \"Famiglia e Diritto\" depuis 2007. "
                    "Médiatrice familiale inscrite au Tableau des "
                    "Médiateurs du Tribunal de Rome.",
            },
            {
                "name":  "Avv. Lorenzo Marchetti",
                "role":  "Associé · Droit pénal des affaires",
                "foro":  "Barreau de Rome depuis 1995 · Avocat aux Cours suprêmes depuis 2007",
                "bio":
                    "Ancien magistrat du parquet de Milan "
                    "(1998-2003), aujourd'hui spécialisé en matière "
                    "de Décret 231 et d'infractions fiscales. "
                    "Membre de l'organe de surveillance de trois "
                    "groupes industriels cotés sur Euronext Milan.",
            },
        ],

        # Publications ribbon — riviste + opere monografiche
        "publications_label": "Publications et citations",
        "publications": [
            "FORO ITALIANO",
            "DIRITTO E GIUSTIZIA",
            "IL SOLE 24 ORE · LEGALE",
            "GUIDA AL DIRITTO",
            "CASSAZIONE PENALE",
            "RIVISTA DELLE SOCIETÀ",
        ],

        # Final CTA band — private-consultation ghost serif
        "cta_label":     "Consultation préliminaire confidentielle",
        "cta_heading":   "Un entretien préliminaire avec un associé.",
        "cta_intro":
            "Le premier contact se fait directement avec un "
            "associé du Cabinet. Nous évoquons le périmètre du "
            "mandat, l'éventuel conflit d'intérêts et les "
            "honoraires indicatifs — avant toute mission formelle "
            "et dans le respect du secret professionnel.",
        "cta_primary":      "Demander une consultation",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Découvrir le Cabinet",
        "cta_secondary_href":"studio",
    },

    # ════════════════════════════════════════════════════════════
    # STUDIO (about) — storia, fondatori, metodo, valori, sedi
    # ════════════════════════════════════════════════════════════
    "studio": {
        "eyebrow":  "Le Cabinet · 1962 — 2026",
        "headline": "Soixante-deux années de barreau, <em>deux générations</em> de la famille Ferri.",
        "intro":
            "Le Studio Legale Ferri naît à Rome en 1962, à "
            "l'initiative de Me Giuseppe Ferri, alors magistrat "
            "démissionnaire de trente-deux ans, avec trois "
            "dossiers de droit des sociétés et un unique stagiaire. "
            "Soixante-deux ans plus tard, nous sommes quatorze "
            "avocats inscrits, deux sièges, une seule gouvernance "
            "— et l'indépendance à l'égard de tout capital tiers "
            "que le fondateur a inscrite comme première règle des "
            "statuts.",

        # History timeline — sei date che hanno definito lo studio
        "history_label":   "Histoire du Cabinet",
        "history_heading": "Six dates, soixante-deux ans",
        "history_intro":
            "Six jalons qui retracent la trajectoire du Cabinet — "
            "de la fondation de 1962 à la passation de relais "
            "générationnelle de 2004, jusqu'à l'ouverture du "
            "siège de Milan en 2019. Derrière chacune de ces "
            "dates se trouve un choix structurel d'indépendance, "
            "de pratique ou de géographie qui oriente encore "
            "aujourd'hui nos mandats.",
        "history": [
            ("1962", "Fondation",
             "Me Giuseppe Ferri, démissionnaire de la magistrature, "
             "ouvre le Cabinet via Piemonte 39 avec trois dossiers "
             "de droit des sociétés et un unique stagiaire."),
            ("1978", "Inscription au Barreau des Cours suprêmes",
             "Après seize années de plaidoiries devant les "
             "juridictions du fond, le fondateur est inscrit au "
             "Tableau spécial des Avocats aux Cours suprêmes — "
             "le cabinet civil peut désormais plaider devant la "
             "Cour de cassation italienne directement, sans "
             "avocat de postulation."),
            ("1989", "Pratique du droit pénal des affaires",
             "Le Cabinet crée un département autonome de droit "
             "pénal des affaires, anticipant d'une décennie le "
             "Décret législatif 231/2001. Les premiers modèles "
             "organisationnels sont rédigés pour deux groupes "
             "industriels du secteur de la construction "
             "mécanique."),
            ("2004", "Passation générationnelle",
             "Me Prof. Alberto Ferri prend la direction du "
             "Cabinet. Le fondateur conserve le rôle de Senior "
             "of Counsel jusqu'en 2014. Les statuts sont "
             "actualisés pour régir l'association de nouveaux "
             "associés par cooptation, jamais par acquisition."),
            ("2014", "Pratique des successions internationales",
             "Avec l'entrée en vigueur du Règlement UE 650/2012 "
             "en matière de successions transfrontalières, le "
             "Cabinet crée un département dédié. Les premiers "
             "mandats concernent des familles entrepreneuriales "
             "italiennes disposant de patrimoines en Suisse et "
             "au Luxembourg."),
            ("2019", "Ouverture du siège de Milan",
             "Pour accompagner les dossiers de droit des "
             "sociétés et de M&A du Nord, le Cabinet ouvre son "
             "second siège corso Venezia 11. Trois associés et "
             "deux collaborateurs permanents. Les deux sièges "
             "relèvent d'une gouvernance unique et ne tiennent "
             "pas de registre de conflits distinct."),
        ],

        # Method — quattro principi non negoziabili
        "values_label":   "Méthode",
        "values_heading": "Quatre principes <em>non négociables</em>",
        "values_intro":
            "Ce sont les quatre règles qui distinguent un mandat "
            "Studio Ferri d'une mission juridique standard. Elles "
            "figurent dans la lettre de mission, non dans un "
            "document marketing.",
        "values": [
            ("01", "Confidentialité absolue",
             "Le secret professionnel selon l'art. 622 du Code "
             "pénal italien est appliqué dans son acception la "
             "plus large : les identités des clients ne sont "
             "jamais divulguées, même sous forme anonymisée, sans "
             "consentement écrit explicite. Le Cabinet ne publie "
             "aucun cas nominatif et ne cite aucun client dans "
             "ses supports promotionnels."),
            ("02", "Un associé par dossier",
             "Chaque dossier est suivi personnellement par un "
             "associé de l'association professionnelle, de "
             "l'ouverture jusqu'au passage en force de chose "
             "jugée. L'associé signe les actes substantiels et "
             "participe aux audiences au fond. Aucun mandat n'est "
             "jamais délégué dans son intégralité à des "
             "collaborateurs juniors."),
            ("03", "Vérification rigoureuse des conflits",
             "Avant l'acceptation de tout nouveau mandat, le "
             "Compliance Officer interne vérifie l'absence de "
             "conflits d'intérêts avec le portefeuille de clients "
             "actifs et les mandats clôturés au cours des cinq "
             "dernières années. En cas de doute, le mandat est "
             "refusé à titre préventif."),
            ("04", "Honoraires transparents",
             "Les honoraires professionnels sont convenus par "
             "écrit dans la lettre de mission, conformément aux "
             "paramètres du Décret ministériel 55/2014. Les "
             "honoraires de résultat sont admis uniquement dans "
             "les limites du Code de déontologie de la profession "
             "d'avocat. Aucune rétrocession, aucun accord verbal "
             "avec des parties adverses."),
        ],

        # Coordinates strip — le due sedi
        "coordinates_label": "Nos sièges",
        "coordinates": [
            ("Rome",    "Via Piemonte 39 · 00187 · Quartier du Quirinal"),
            ("Milan",   "Corso Venezia 11 · 20121 · Quartier de Porta Venezia"),
        ],

        # Page-level CTA
        "cta_heading":  "Une évaluation préliminaire confidentielle.",
        "cta_intro":
            "Le premier entretien se tient directement avec un "
            "associé du Cabinet. Nous évoquons le périmètre du "
            "mandat, l'éventuel conflit d'intérêts et les "
            "honoraires indicatifs, sous couvert de "
            "confidentialité.",
        "cta_primary":      "Demander une consultation",
        "cta_primary_href": "contatti",
    },

    # ════════════════════════════════════════════════════════════
    # PRATICHE (services) — 12 aree di pratica
    # ════════════════════════════════════════════════════════════
    "pratiche": {
        "eyebrow":  "Domaines d'intervention · 2026",
        "headline": "Douze compétences, une seule <em>signature</em>.",
        "intro":
            "Les douze domaines d'intervention du Cabinet. Chaque "
            "client accède à une équipe pluridisciplinaire — il "
            "n'y a pas de facturation séparée par domaine ; le "
            "mandat couvre la combinaison de compétences "
            "nécessaires à la résolution du problème posé.",

        # Card meta labels (lifted from skin for locale support)
        "svc_lead_label":     "Associé responsable",
        "svc_jurisdiction_label": "Barreau de référence",

        # 12 services in airy ledger
        "services": [
            {
                "num":     "01",
                "title":   "Droit des sociétés",
                "blurb":
                    "Constitution de sociétés, gouvernance, pactes "
                    "d'actionnaires, opérations structurantes. "
                    "Augmentations de capital selon l'art. 2343 du "
                    "Code civil italien avec expertise assermentée, "
                    "fusions transfrontalières selon le Décret "
                    "législatif 108/2008, transformations "
                    "hétérogènes, scissions proportionnelles et "
                    "non proportionnelles.",
                "scope": [
                    "Constitution et statuts des sociétés",
                    "Augmentations de capital et expertises art. 2343",
                    "Pactes d'actionnaires et gouvernance",
                    "Fusions, scissions, transformations",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Barreaux de Rome · Milan · Bruxelles",
            },
            {
                "num":     "02",
                "title":   "M&A et opérations structurantes",
                "blurb":
                    "Due diligence, rédaction des SPA et des pactes "
                    "d'actionnaires, négociation, intégration "
                    "post-opération. Nous intervenons soit côté "
                    "cédant, soit côté acquéreur, jamais des deux "
                    "côtés sur un même dossier. Typologie : "
                    "carve-out, joint-ventures, sortie de private "
                    "equity, MBO familiaux.",
                "scope": [
                    "Due diligence juridique vendeur",
                    "Due diligence acquéreur et SPA",
                    "Pactes d'actionnaires et earn-out",
                    "Intégration post-fusion 100 jours",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Barreaux de Rome · Milan",
            },
            {
                "num":     "03",
                "title":   "Droit de la famille",
                "blurb":
                    "Séparations consensuelles et contentieuses, "
                    "divorces, fixation de la garde des mineurs, "
                    "modifications des conditions de séparation et "
                    "de divorce. Médiation familiale en phase "
                    "pré-contentieuse selon l'art. 5 du Décret "
                    "législatif 28/2010.",
                "scope": [
                    "Séparations consensuelles et contentieuses",
                    "Divorces contentieux et consensuels",
                    "Garde et pension alimentaire des mineurs",
                    "Médiation familiale",
                ],
                "lead":   "Avv. Maria Grazia Conti",
                "jurisdiction": "Barreaux de Rome · Milan",
            },
            {
                "num":     "04",
                "title":   "Successions et patrimoines",
                "blurb":
                    "Successions nationales et internationales "
                    "selon le Règlement UE 650/2012, rédaction de "
                    "testaments authentiques et olographes, "
                    "partages successoraux, donations et pactes "
                    "de famille selon l'art. 768-bis du Code civil "
                    "italien. Trusts familiaux régis par la "
                    "Convention de La Haye.",
                "scope": [
                    "Planification successorale internationale",
                    "Testaments et pactes de famille",
                    "Partages successoraux et arbitrages",
                    "Trusts et fondations familiales",
                ],
                "lead":   "Avv. Maria Grazia Conti",
                "jurisdiction": "Barreaux de Rome · Milan · Lugano",
            },
            {
                "num":     "05",
                "title":   "Droit du travail",
                "blurb":
                    "Contentieux individuel et collectif, "
                    "négociation collective de second niveau, "
                    "sécurité au travail selon le Décret législatif "
                    "81/2008, licenciements selon l'art. 18 du "
                    "Statut des travailleurs et le Jobs Act, "
                    "transactions devant les instances syndicales "
                    "selon l'art. 411 du Code de procédure civile "
                    "italien.",
                "scope": [
                    "Contentieux du travail individuel et collectif",
                    "Licenciements pour juste cause et motif légitime",
                    "Négociation collective de second niveau",
                    "Sécurité au travail et Décret 81/2008",
                ],
                "lead":   "Avv. Federica Ronchi",
                "jurisdiction": "Barreaux de Rome · Milan",
            },
            {
                "num":     "06",
                "title":   "Droit pénal des affaires",
                "blurb":
                    "Infractions d'affaires selon les art. 2621-"
                    "2641 du Code civil italien, responsabilité "
                    "administrative des personnes morales selon le "
                    "Décret législatif 231/2001, délits en col "
                    "blanc, infractions fiscales selon le Décret "
                    "législatif 74/2000. Défense des administrateurs, "
                    "commissaires aux comptes et organes de "
                    "surveillance.",
                "scope": [
                    "Défense dans les procédures 231",
                    "Infractions d'affaires et fiscales",
                    "Modèles organisationnels et organes de surveillance",
                    "Enquêtes internes et lanceurs d'alerte",
                ],
                "lead":   "Avv. Lorenzo Marchetti",
                "jurisdiction": "Barreaux de Rome · Milan · Cour de cassation",
            },
            {
                "num":     "07",
                "title":   "Droit des contrats commerciaux",
                "blurb":
                    "Rédaction et négociation de contrats "
                    "commerciaux italiens et internationaux — "
                    "distribution, agence, franchise, joint-"
                    "ventures, licensing. Convention de Vienne "
                    "de 1980 sur la vente internationale de "
                    "marchandises.",
                "scope": [
                    "Distribution et agence commerciale",
                    "Franchise et joint-ventures",
                    "Licensing PI et savoir-faire",
                    "Contrats internationaux (CVIM)",
                ],
                "lead":   "Avv. Stefano Bellini",
                "jurisdiction": "Barreaux de Rome · Milan · Bruxelles",
            },
            {
                "num":     "08",
                "title":   "Droit bancaire et financier",
                "blurb":
                    "Opérations de financement, sûretés réelles et "
                    "personnelles, contentieux bancaire, "
                    "anatocisme, usure, renégociations, dérivés. "
                    "Supervision Banque d'Italie, réglementation "
                    "CRR/CRD IV, MAR et abus de marché.",
                "scope": [
                    "Financements corporate et LBO",
                    "Contentieux bancaire et usure",
                    "Instruments dérivés (IRS, FX)",
                    "Supervision Banque d'Italie · MAR",
                ],
                "lead":   "Avv. Caterina Albini",
                "jurisdiction": "Barreaux de Rome · Milan",
            },
            {
                "num":     "09",
                "title":   "Droit administratif",
                "blurb":
                    "Contentieux devant les TAR et le Conseil "
                    "d'État italien, marchés publics selon le "
                    "Décret législatif 36/2023, concessions, "
                    "autorisations d'urbanisme, accès aux "
                    "documents selon la loi 241/1990, recours "
                    "extraordinaire au Chef de l'État.",
                "scope": [
                    "Marchés publics et concessions",
                    "Autorisations d'urbanisme et VIA",
                    "Accès aux documents et transparence",
                    "Recours TAR et Conseil d'État",
                ],
                "lead":   "Avv. Giulio Mancini",
                "jurisdiction": "Barreau de Rome · TAR Lazio",
            },
            {
                "num":     "10",
                "title":   "Immobilier",
                "blurb":
                    "Acquisitions et cessions de patrimoines "
                    "immobiliers, opérations de développement, "
                    "fonds immobiliers, baux commerciaux, "
                    "contentieux de copropriété. Vérifications "
                    "urbanistiques et cadastrales, actes "
                    "notariés coordonnés avec notaire de "
                    "confiance.",
                "scope": [
                    "Acquisitions et cessions immobilières",
                    "Développement et fonds immobiliers",
                    "Baux commerciaux (loi 392/78)",
                    "Contentieux de copropriété",
                ],
                "lead":   "Avv. Stefano Bellini",
                "jurisdiction": "Barreaux de Rome · Milan",
            },
            {
                "num":     "11",
                "title":   "Protection des données personnelles",
                "blurb":
                    "Conformité au Règlement UE 679/2016 (RGPD), "
                    "cartographie des données, AIPD, désignation "
                    "des DPO, registre des traitements, gestion "
                    "des violations de données, contentieux "
                    "devant l'Autorité garante italienne. AI Act "
                    "et profilage algorithmique.",
                "scope": [
                    "Conformité RGPD et AIPD",
                    "Désignation DPO et registre des traitements",
                    "Violations de données et notification à l'Autorité",
                    "AI Act et profilage algorithmique",
                ],
                "lead":   "Avv. Caterina Albini",
                "jurisdiction": "Barreaux de Rome · Milan",
            },
            {
                "num":     "12",
                "title":   "Arbitrage et MARL",
                "blurb":
                    "Arbitrage ad hoc et institutionnel (CCI, CAM, "
                    "ICC, LCIA), médiation civile et commerciale "
                    "selon le Décret législatif 28/2010, "
                    "négociation assistée selon le Décret-loi "
                    "132/2014, expertise contractuelle.",
                "scope": [
                    "Arbitrage CCI / CAM / ICC / LCIA",
                    "Médiation civile et commerciale",
                    "Négociation assistée",
                    "Expertise contractuelle et arbitrage",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Barreaux de Rome · Milan · Chambre d'arbitrage",
            },
        ],

        # Process strip — come si svolge un mandato
        "process_label":   "Déroulement d'un mandat",
        "process_heading": "Quatre phases, une seule séquence",
        "process": [
            ("01", "Entretien préliminaire confidentiel",
             "Premier rendez-vous avec un associé du Cabinet. "
             "Nous évoquons le périmètre, l'éventuel conflit "
             "d'intérêts et les honoraires indicatifs. Aucune "
             "proposition écrite à ce stade, seulement une "
             "évaluation de faisabilité."),
            ("02", "Lettre de mission",
             "Dans un délai de cinq jours, lettre de mission "
             "écrite détaillant périmètre, livrables, calendrier "
             "et honoraires professionnels selon le Décret "
             "ministériel 55/2014. Le mandat n'est formalisé "
             "qu'à la signature des deux parties."),
            ("03", "Exécution et plaidoirie",
             "L'associé responsable signe personnellement les "
             "actes substantiels et participe aux audiences au "
             "fond. Le client reçoit des rapports écrits "
             "périodiques sur l'état du dossier, jamais par "
             "voie télématique non chiffrée."),
            ("04", "Clôture et archivage",
             "Au passage en force de chose jugée ou à la clôture "
             "du mandat, lettre de clôture confidentielle "
             "résumant l'issue et donnant un avis final. Archive "
             "chiffrée pendant dix ans conformément au Code de "
             "déontologie de la profession d'avocat."),
        ],

        # Final CTA
        "cta_heading":  "Quel domaine correspond à votre situation ?",
        "cta_intro":
            "Si le périmètre n'est pas encore clair, adressez "
            "une brève description du problème au secrétariat "
            "du Cabinet. Nous vous orienterons vers l'associé "
            "compétent sous quarante-huit heures, même si le "
            "mandat n'entre finalement pas dans nos critères "
            "d'acceptation.",
        "cta_primary":      "Nous écrire",
        "cta_primary_href": "contatti",
    },

    # ════════════════════════════════════════════════════════════
    # AVVOCATI (team) — 14 avvocati abilitati
    # ════════════════════════════════════════════════════════════
    "avvocati": {
        "eyebrow":  "Nos Avocats · 14 inscrits au barreau",
        "headline": "Quatorze avocats, <em>une seule</em> direction.",
        "intro":
            "Le Cabinet compte quatorze avocats inscrits aux "
            "Barreaux de Rome et Milan — six associés de "
            "l'association professionnelle et huit avocats "
            "collaborateurs. La sélection se fait par cooptation, "
            "jamais par acquisition : chaque nouvelle admission "
            "requiert l'unanimité des associés.",

        # Card meta labels
        "lawyer_foro_label":  "Barreau",
        "lawyer_year_label":  "Inscription",
        "lawyer_specialization_label": "Spécialisation",

        # 14 avvocati — 6 soci + 8 associati
        "lawyers": [
            {
                "name":  "Avv. Prof. Alberto Ferri",
                "role":  "Associé gérant",
                "specialization": "Droit des sociétés · M&A · Arbitrage",
                "foro":  "Barreau de Rome",
                "year":  "Inscrit en 1986 · Avocat aux Cours suprêmes depuis 1999",
                "bio":
                    "Fils du fondateur, il dirige le Cabinet "
                    "depuis 2004. Professeur associé de droit "
                    "commercial à LUISS Guido Carli. Auteur de "
                    "l'ouvrage \"L'aumento di capitale nelle "
                    "società quotate\" (Giuffrè, 2018) et de "
                    "nombreux articles dans la \"Rivista delle "
                    "Società\".",
            },
            {
                "name":  "Avv. Maria Grazia Conti",
                "role":  "Associée senior",
                "specialization": "Droit de la famille · Successions",
                "foro":  "Barreau de Rome",
                "year":  "Inscrite en 1991 · Avocate aux Cours suprêmes depuis 2003",
                "bio":
                    "Spécialiste des successions internationales "
                    "et des pactes de famille. Collaboratrice de "
                    "la revue \"Famiglia e Diritto\" depuis 2007. "
                    "Médiatrice familiale inscrite au Tableau des "
                    "Médiateurs du Tribunal de Rome.",
            },
            {
                "name":  "Avv. Lorenzo Marchetti",
                "role":  "Associé",
                "specialization": "Pénal des affaires · Décret 231",
                "foro":  "Barreau de Rome · Cour de cassation",
                "year":  "Inscrit en 1995 · Avocat aux Cours suprêmes depuis 2007",
                "bio":
                    "Ancien magistrat du parquet de la République "
                    "de Milan (1998-2003). Membre de l'organe de "
                    "surveillance de trois groupes industriels "
                    "cotés sur Euronext Milan. Enseignant à "
                    "l'École de spécialisation des professions "
                    "juridiques.",
            },
            {
                "name":  "Avv. Federica Ronchi",
                "role":  "Associée",
                "specialization": "Droit du travail · Sécurité",
                "foro":  "Barreaux de Rome · Milan",
                "year":  "Inscrite en 1999",
                "bio":
                    "Spécialiste des licenciements collectifs et "
                    "de la négociation collective de second "
                    "niveau. Conseillère de trois grandes "
                    "entreprises du secteur industriel pour la "
                    "négociation syndicale. Membre du Comité "
                    "pour l'égalité des chances du Barreau de "
                    "Rome.",
            },
            {
                "name":  "Avv. Stefano Bellini",
                "role":  "Associé",
                "specialization": "Contrats commerciaux · Immobilier",
                "foro":  "Barreaux de Rome · Bruxelles",
                "year":  "Inscrit en 2001",
                "bio":
                    "Expert en contrats commerciaux "
                    "internationaux et opérations immobilières "
                    "complexes. Inscrit au Barreau de Bruxelles "
                    "pour les dossiers de droit communautaire. "
                    "LL.M. en International Business Law à "
                    "l'Université Libre de Bruxelles.",
            },
            {
                "name":  "Avv. Caterina Albini",
                "role":  "Associée",
                "specialization": "Bancaire · RGPD et données",
                "foro":  "Barreau de Milan",
                "year":  "Inscrite en 2003",
                "bio":
                    "Coordonne le département bancaire du siège "
                    "de Milan. Spécialiste des dérivés et des "
                    "instruments financiers complexes. DPO "
                    "certifiée selon le schéma UNI 11697:2017. "
                    "Auteure de \"GDPR e responsabilità del "
                    "titolare\" (Wolters Kluwer, 2021).",
            },
            {
                "name":  "Avv. Giulio Mancini",
                "role":  "Of counsel",
                "specialization": "Droit administratif · Marchés publics",
                "foro":  "Barreau de Rome · TAR Lazio",
                "year":  "Inscrit en 1998",
                "bio":
                    "Ancien magistrat du TAR du Lazio "
                    "(2002-2014), aujourd'hui avocat plaidant "
                    "dans les contentieux devant les TAR et le "
                    "Conseil d'État italien. Spécialiste des "
                    "marchés publics et des concessions de "
                    "services. Membre du Conseil d'administration "
                    "de l'AIDA.",
            },
            {
                "name":  "Avv. Beatrice Lazzaro",
                "role":  "Avocate collaboratrice",
                "specialization": "Pénal des affaires · Enquêtes internes",
                "foro":  "Barreau de Rome",
                "year":  "Inscrite en 2008",
                "bio":
                    "Collaboratrice du département de droit "
                    "pénal des affaires depuis 2010. Spécialisée "
                    "dans les enquêtes internes d'entreprise et "
                    "le lancement d'alerte selon le Décret "
                    "législatif 24/2023. Enseignante au Master "
                    "en Compliance 231 de l'Université LUMSA.",
            },
            {
                "name":  "Avv. Marco Vergani",
                "role":  "Avocat collaborateur",
                "specialization": "M&A · Droit des sociétés",
                "foro":  "Barreau de Milan",
                "year":  "Inscrit en 2011",
                "bio":
                    "Coordinateur du siège de Milan pour les "
                    "opérations de M&A mid-market. Expérience "
                    "antérieure dans un cabinet international "
                    "de premier plan. Spécialiste des opérations "
                    "cross-border Italie-DACH, notamment avec "
                    "des contreparties allemandes et suisses.",
            },
            {
                "name":  "Avv. Sara Donati",
                "role":  "Avocate collaboratrice",
                "specialization": "Droit de la famille · Mineurs",
                "foro":  "Barreau de Rome",
                "year":  "Inscrite en 2013",
                "bio":
                    "Spécialisée dans les procédures relatives à "
                    "la garde des mineurs et dans les procédures "
                    "devant le Tribunal pour enfants. Curatrice "
                    "spéciale du mineur dans les procédures "
                    "d'adoption. Master en droit de la famille "
                    "à l'Université Rome Tre.",
            },
            {
                "name":  "Avv. Tommaso Ricci",
                "role":  "Avocat collaborateur",
                "specialization": "Travail · Contentieux collectif",
                "foro":  "Barreau de Milan",
                "year":  "Inscrit en 2014",
                "bio":
                    "Siège de Milan. Spécialisé dans le "
                    "contentieux collectif du travail et les "
                    "procédures selon la loi 223/1991 "
                    "(licenciements collectifs). Expérience "
                    "antérieure au sein de la direction "
                    "juridique d'un groupe industriel coté du "
                    "secteur manufacturier.",
            },
            {
                "name":  "Avv. Elisa Falcone",
                "role":  "Avocate collaboratrice",
                "specialization": "Bancaire · Contentieux usure",
                "foro":  "Barreau de Milan",
                "year":  "Inscrite en 2015",
                "bio":
                    "Spécialisée dans le contentieux bancaire et "
                    "dans les actions en constatation "
                    "d'anatocisme et d'usure. Coordonne la "
                    "section bancaire du siège de Milan. Master "
                    "en droit bancaire à l'Université Bocconi.",
            },
            {
                "name":  "Avv. Riccardo Zambelli",
                "role":  "Avocat collaborateur",
                "specialization": "Administratif · Urbanisme",
                "foro":  "Barreau de Rome · TAR Lazio",
                "year":  "Inscrit en 2016",
                "bio":
                    "Collabore au département administratif "
                    "avec un focus sur l'urbanisme, l'évaluation "
                    "d'impact environnemental (VIA) et les "
                    "autorisations paysagères. Expérience "
                    "antérieure au sein du service juridique "
                    "d'un grand opérateur d'infrastructures.",
            },
            {
                "name":  "Avv. Chiara Tomei",
                "role":  "Avocate collaboratrice",
                "specialization": "Données personnelles · AI Act · Tech",
                "foro":  "Barreau de Milan",
                "year":  "Inscrite en 2019",
                "bio":
                    "Spécialisée en protection des données "
                    "personnelles, avec un focus sur les "
                    "questions émergentes liées à l'intelligence "
                    "artificielle générative et aux obligations "
                    "de l'AI Act (Règlement UE 2024/1689). "
                    "Master en droit des nouvelles technologies "
                    "à l'Université de Pavie.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════
    # NOTABILI (blog_list) — cause notabili e pubblicazioni
    # ════════════════════════════════════════════════════════════
    "notabili": {
        "eyebrow":  "Affaires marquantes et publications · 2018 — 2026",
        "headline": "Six mandats sélectionnés, <em>dans le strict respect</em> du secret professionnel.",
        "intro":
            "Une sélection d'affaires marquantes et de publications "
            "récentes. Par déontologie professionnelle et en "
            "application de l'art. 622 du Code pénal italien, les "
            "identités des clients ne sont jamais indiquées : les "
            "affaires sont identifiées par secteur industriel et "
            "par périmètre technique, les publications par revue "
            "et par sujet traité.",

        # Lead post + list — 6 posts referenced below
        "lead_image": "https://images.pexels.com/photos/5668858/pexels-photo-5668858.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
    },

    # Posts powering blog_detail. URL: /notabili/<slug>/
    "posts": [
        {
            "slug":     "aumento-capitale-quotata-2343cc",
            "kicker":   "Droit des sociétés",
            "title":    "Augmentation de capital selon l'art. 2343 du Code civil italien pour société cotée · expertise assermentée · 2024",
            "date":     "Mars 2024",
            "read_min": "8",
            "author":   "Avv. Prof. Alberto Ferri",
            "lede":
                "Sur mandat d'un groupe industriel coté du "
                "secteur de l'énergie, le Cabinet a assisté le "
                "conseil d'administration dans la délibération "
                "et l'exécution d'une augmentation de capital "
                "en nature de 145 millions d'euros, avec apport "
                "d'une filiale étrangère évaluée par expertise "
                "assermentée selon l'art. 2343 du Code civil "
                "italien.",
            "body": [
                ("p",
                 "Le mandat a couvert l'intégralité de la phase "
                 "délibérative, de la rédaction du rapport "
                 "explicatif du conseil d'administration selon "
                 "l'art. 2441 du Code civil italien jusqu'à la "
                 "désignation par le Tribunal de Rome de "
                 "l'expert chargé de l'expertise assermentée "
                 "de la filiale apportée."),
                ("h2", "Le cadre normatif"),
                ("p",
                 "L'opération s'est déroulée dans le strict "
                 "respect de l'art. 2343 du Code civil italien "
                 "(expertise assermentée) et de l'art. 2441 du "
                 "Code civil italien (droit d'option), avec "
                 "exclusion du droit d'option au profit d'un "
                 "investisseur institutionnel désigné par le "
                 "conseil d'administration. La procédure a exigé "
                 "un rapport spécifique du collège des "
                 "commissaires aux comptes selon l'art. 2441 "
                 "alinéa 6 du Code civil italien."),
                ("h2", "Le rôle du Cabinet"),
                ("p",
                 "Le Cabinet a coordonné les rapports avec la "
                 "Consob pour le dépôt du prospectus d'offre, "
                 "avec le Tribunal de Rome pour la désignation "
                 "de l'expert, avec le notaire pour la "
                 "rédaction du procès-verbal de l'assemblée "
                 "générale extraordinaire et avec le commissaire "
                 "aux comptes pour les vérifications "
                 "postérieures selon l'art. 2343-bis du Code "
                 "civil italien."),
                ("blockquote",
                 "Le respect de la procédure selon l'art. 2343 "
                 "du Code civil italien est une condition de "
                 "validité de l'augmentation de capital. Toute "
                 "simplification opérationnelle prétendant "
                 "comprimer les délais légaux expose l'opération "
                 "au risque de nullité."),
            ],
        },
        {
            "slug":     "modello-231-gruppo-utility",
            "kicker":   "Pénal des affaires",
            "title":    "Modèle organisationnel selon le Décret législatif 231/2001 pour un groupe utility coté",
            "date":     "Novembre 2024",
            "read_min": "11",
            "author":   "Avv. Lorenzo Marchetti",
            "lede":
                "Le Cabinet a rédigé le modèle organisationnel "
                "selon le Décret législatif 231/2001 pour un "
                "groupe utility coté à la suite du renouvellement "
                "de son organe de surveillance. La mission a "
                "inclus la cartographie des risques d'infraction, "
                "la conception des protocoles opérationnels et la "
                "formation interne de soixante-deux cadres "
                "dirigeants.",
            "body": [
                ("p",
                 "Le mandat a duré neuf mois et s'est déroulé "
                 "selon trois flux parallèles : cartographie "
                 "des risques d'infraction présumée, refonte "
                 "des protocoles opérationnels, formation "
                 "obligatoire du personnel exposé."),
                ("h2", "Cartographie des risques d'infraction"),
                ("p",
                 "Les vingt-deux infractions présumées "
                 "pertinentes pour le secteur utility ont été "
                 "cartographiées, avec une attention "
                 "particulière pour les infractions "
                 "environnementales selon l'art. 25-undecies du "
                 "Décret législatif 231/2001 et les infractions "
                 "contre l'administration publique selon "
                 "l'art. 25 du Décret législatif 231/2001. La "
                 "cartographie a requis des entretiens avec "
                 "quarante process owners."),
                ("h2", "Conception des protocoles"),
                ("p",
                 "Les protocoles opérationnels ont été "
                 "refondus selon le principe de séparation des "
                 "fonctions et de traçabilité documentaire. Une "
                 "attention particulière a été portée aux "
                 "processus d'approvisionnement, aux appels "
                 "d'offres publics et à la gestion des relations "
                 "avec l'administration publique."),
            ],
        },
        {
            "slug":     "successione-internazionale-reg-650",
            "kicker":   "Successions internationales",
            "title":    "Succession internationale selon le Règl. UE 650/2012 · famille entrepreneuriale Italie-Suisse",
            "date":     "Septembre 2024",
            "read_min": "9",
            "author":   "Avv. Maria Grazia Conti",
            "lede":
                "Pour une famille entrepreneuriale du Nord-Est "
                "italien avec des patrimoines en Italie, en "
                "Suisse et au Luxembourg, le Cabinet a "
                "coordonné l'ouverture de la succession du "
                "de cujus — domicilié à Lugano depuis plus de "
                "vingt ans — aux termes du Règlement UE "
                "650/2012.",
            "body": [
                ("p",
                 "La succession a soulevé des questions "
                 "complexes de droit international privé, "
                 "notamment sur la professio iuris selon "
                 "l'art. 22 du Règlement 650/2012 en faveur "
                 "du droit italien, exercée par le de cujus "
                 "par testament olographe rédigé à Lugano "
                 "en 2018."),
                ("h2", "Coordination multi-juridictionnelle"),
                ("p",
                 "Le Cabinet a coordonné les rapports avec le "
                 "notaire italien pour l'acceptation de la "
                 "succession, avec la fiduciaire suisse pour "
                 "le partage des comptes bancaires et avec le "
                 "Barreau de Luxembourg pour la liquidation "
                 "d'une holding luxembourgeoise."),
                ("h2", "Issue"),
                ("p",
                 "L'intégralité de la procédure a été clôturée "
                 "en quatorze mois, avec accord de partage "
                 "ratifié devant le notaire de Rome. Aucun "
                 "contentieux judiciaire, droits de succession "
                 "liquidés selon barème."),
            ],
        },
        {
            "slug":     "ferri-aumento-capitale-giuffre-2018",
            "kicker":   "Publication monographique",
            "title":    "\"L'aumento di capitale nelle società quotate\" · Giuffrè · 2018",
            "date":     "2018",
            "read_min": "5",
            "author":   "Avv. Prof. Alberto Ferri",
            "lede":
                "La monographie, éditée par Giuffrè Francis "
                "Lefebvre en 2018, rassemble l'expérience "
                "professionnelle de l'auteur en matière "
                "d'augmentations de capital de sociétés cotées "
                "sur les marchés réglementés italiens. "
                "L'ouvrage est aujourd'hui adopté dans trois "
                "universités italiennes comme texte de "
                "référence du cours de droit commercial.",
            "body": [
                ("p",
                 "L'ouvrage s'articule en douze chapitres qui "
                 "parcourent les différentes typologies "
                 "d'augmentation de capital : en numéraire, en "
                 "nature, gratuites, réservées, avec exclusion "
                 "du droit d'option."),
                ("h2", "Structure de l'ouvrage"),
                ("p",
                 "Les quatre premiers chapitres traitent du "
                 "régime général selon les art. 2438-2444 du "
                 "Code civil italien. Les chapitres centraux "
                 "approfondissent les hypothèses spéciales — "
                 "augmentations déléguées au conseil "
                 "d'administration, augmentations scindables "
                 "et non scindables, augmentations avec "
                 "warrants. Les trois derniers chapitres sont "
                 "consacrés aux particularités des sociétés "
                 "cotées."),
            ],
        },
        {
            "slug":     "licenziamento-collettivo-l-223-91",
            "kicker":   "Droit du travail",
            "title":    "Procédure de licenciement collectif selon la loi 223/1991 · groupe manufacturier",
            "date":     "Mai 2024",
            "read_min": "7",
            "author":   "Avv. Federica Ronchi",
            "lede":
                "Le Cabinet a assisté un groupe manufacturier "
                "du secteur de la construction mécanique dans "
                "la procédure de licenciement collectif selon "
                "la loi 223/1991, conclue par accord syndical "
                "et reclassement de 78% du personnel "
                "excédentaire.",
            "body": [
                ("p",
                 "La procédure a concerné cent quarante postes "
                 "de travail et s'est déroulée en deux phases "
                 "— examen conjoint au niveau de l'entreprise "
                 "selon l'art. 4 de la loi 223/1991 et examen "
                 "successif au niveau ministériel auprès du "
                 "Ministère du Travail."),
                ("h2", "L'accord syndical"),
                ("p",
                 "L'accord, signé avec toutes les organisations "
                 "syndicales représentatives, a prévu "
                 "l'activation d'un fonds bilatéral de "
                 "requalification, l'incitation au départ pour "
                 "les salariés les plus âgés et un plan de "
                 "reclassement interne pour le personnel "
                 "restant."),
                ("h2", "Bilan quantitatif"),
                ("p",
                 "Sur les cent quarante salariés concernés, "
                 "vingt-huit ont adhéré à l'incitation au "
                 "départ, quatre-vingt-trois ont été reclassés "
                 "sur d'autres lignes de production, "
                 "vingt-neuf ont été accompagnés par le fonds "
                 "bilatéral d'outplacement."),
            ],
        },
        {
            "slug":     "carve-out-dach-mid-cap-2023",
            "kicker":   "M&A transfrontalier",
            "title":    "Carve-out et cession de division industrielle à un opérateur allemand · 2023",
            "date":     "Décembre 2023",
            "read_min": "10",
            "author":   "Avv. Marco Vergani",
            "lede":
                "Le Cabinet a agi sell-side dans une opération "
                "de carve-out et cession d'une division "
                "industrielle (112 millions d'euros de chiffre "
                "d'affaires annuel) à un opérateur stratégique "
                "allemand, conclue au quatrième trimestre 2023 "
                "après vingt-deux semaines de négociation.",
            "body": [
                ("p",
                 "Le mandat a couvert l'intégralité de "
                 "l'opération de carve-out — de la préparation "
                 "du teaser à la négociation du share purchase "
                 "agreement, jusqu'aux six premières semaines "
                 "d'intégration post-fusion."),
                ("h2", "Les phases"),
                ("ol", [
                    "Préparation du teaser et information memorandum",
                    "Vendor due diligence (juridique, fiscale, sociale)",
                    "Enchère privée sur quatre acquéreurs potentiels",
                    "Négociation SPA et pacte d'actionnaires",
                    "Closing et intégration post-fusion 100 jours",
                ]),
                ("h2", "Le résultat"),
                ("p",
                 "Cession conclue au multiple EBITDA de marché "
                 "(8,4x), avec clause d'earn-out sur deux "
                 "exercices. 100% des contrats avec les trois "
                 "principaux clients DACH ont été renouvelés "
                 "dans les six mois suivant le closing."),
            ],
        },
    ],

    # ════════════════════════════════════════════════════════════
    # CONTATTI (contact) — 2 sedi, form riservato
    # ════════════════════════════════════════════════════════════
    "contatti": {
        "eyebrow":  "Consultation préliminaire confidentielle",
        "headline": "Un entretien préliminaire avec un <em>associé du Cabinet</em>.",
        "intro":
            "Le premier contact se fait directement avec un "
            "associé de l'association professionnelle. Nous "
            "évoquons le périmètre du mandat, l'éventuel "
            "conflit d'intérêts et les honoraires indicatifs — "
            "sous couvert du secret professionnel selon "
            "l'art. 622 du Code pénal italien, avant toute "
            "mission formelle.",

        # Form fields
        "form_label":   "Formulaire confidentiel",
        "form_heading": "Remplissez le formulaire confidentiel",
        "form_intro":
            "Vous recevrez un accusé de réception dans un délai "
            "de quarante-huit heures ouvrées, signé par "
            "l'associé responsable du domaine concerné. Les "
            "informations sont traitées conformément au "
            "Règlement UE 679/2016 et conservées dans des "
            "archives chiffrées à accès réservé aux associés "
            "du Cabinet.",
        "form_fields": [
            {"name": "name", "label": "Prénom", "type": "text", "required": True,
             "placeholder": "Ex. Alessandro",
             "helper": "Prénom uniquement, merci."},
            {"name": "surname", "label": "Nom", "type": "text", "required": True,
             "placeholder": "Ex. Costa",
             "helper": "Tel qu'il figure sur votre pièce d'identité."},
            {"name": "email", "label": "Adresse email", "type": "email", "required": True,
             "placeholder": "alessandro.costa@exemple.fr",
             "helper": "Pour la correspondance préliminaire. Nous n'utiliserons pas cette adresse à d'autres fins."},
            {"name": "phone", "label": "Téléphone", "type": "tel", "required": True,
             "placeholder": "+33 ...",
             "helper": "Ligne directe du contact, pas un standard."},
            {"name": "capacity", "label": "En qualité de", "type": "select", "required": True,
             "options": [
                 "Particulier",
                 "Entrepreneur ou actionnaire",
                 "Administrateur ou commissaire aux comptes",
                 "Direction juridique de groupe industriel",
                 "Professionnel (expert-comptable, notaire, etc.)",
             ],
             "helper": "Pour orienter l'entretien préliminaire."},
            {"name": "practice", "label": "Domaine d'intervention", "type": "select", "required": True,
             "options": [
                 "À déterminer lors de l'entretien",
                 "Droit des sociétés",
                 "M&A et opérations structurantes",
                 "Droit de la famille",
                 "Successions et patrimoines",
                 "Droit du travail",
                 "Droit pénal des affaires",
                 "Droit des contrats commerciaux",
                 "Droit bancaire et financier",
                 "Droit administratif",
                 "Immobilier",
                 "Protection des données personnelles",
                 "Arbitrage et MARL",
             ],
             "helper": "Sélectionnez \"À déterminer\" si le périmètre couvre plusieurs domaines."},
            {"name": "urgency", "label": "Urgence", "type": "select", "required": True,
             "options": [
                 "Dans la semaine en cours",
                 "Sous un mois",
                 "Sous trois mois",
                 "Exploratoire, aucune urgence",
             ],
             "helper": "Permet de programmer l'associé compétent."},
            {"name": "perimeter", "label": "Brève description du problème",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Maximum 800 caractères. Les noms de contreparties, "
                 "de filiales ou de tiers ne sont divulgués qu'après "
                 "signature d'un NDA réciproque, jamais dans ce "
                 "formulaire.",
             "helper":
                 "Suffisant pour effectuer la vérification "
                 "préliminaire des conflits et orienter le "
                 "dossier vers l'associé compétent. Les détails "
                 "sensibles se discutent lors de l'entretien."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contact",
             "meta": "La personne qui signera l'éventuelle lettre de mission.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Qualité",
             "meta": "Pour la vérification préliminaire des conflits.",
             "fields": ["capacity"]},
            {"num": "03", "title": "Objet de la consultation",
             "meta":
                 "Aucun nom de contrepartie ici — le périmètre "
                 "technique se discute lors de l'entretien "
                 "après NDA réciproque.",
             "fields": ["practice", "urgency", "perimeter"]},
            {"num": "04", "title": "Pièces jointes (facultatives)",
             "meta":
                 "Documents préliminaires, organigrammes ou NDA "
                 "standard peuvent accélérer l'entretien.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "documenti_preliminari",
            "label":    "Documents préliminaires",
            "helper":
                "Documents préliminaires, organigramme "
                "sociétaire ou NDA standard. PDF / DOCX · "
                "15 Mo max au total. Archive chiffrée à accès "
                "réservé aux associés du Cabinet.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Déposez les documents ici ou",
            "link":     "sélectionnez depuis votre dossier",
            "meta":     "PDF / DOCX · 15 Mo max · archive chiffrée",
        },

        "form_submit_label": "Envoyer la demande confidentielle",
        "form_submit_note":
            "Accusé de réception signé par un associé dans un "
            "délai de quarante-huit heures ouvrées. Aucun BDR, "
            "aucune automatisation, aucune communication "
            "commerciale.",
        "form_consent":
            "Je consens au traitement de mes données "
            "personnelles conformément au Règlement UE 679/2016 "
            "et je déclare avoir été informé que les données "
            "sont conservées dans des archives chiffrées à "
            "accès réservé aux associés du Studio Legale Ferri. "
            "Les données ne sont pas communiquées à des tiers "
            "sans consentement écrit explicite.",

        # Office meta-row labels (lifted from skin for i18n)
        "office_address_label": "Adresse",
        "office_area_label":    "Quartier",
        "office_phone_label":   "Téléphone",
        "office_email_label":   "Email",
        "office_hours_label":   "Horaires",

        # Sidebar — sedi + canali diretti
        "offices_label":   "Nos sièges",
        "offices": [
            {
                "city":    "Rome",
                "tag":     "Siège principal",
                "address": "Via Piemonte 39 · 00187",
                "area":    "Quirinal · près de Piazza Barberini",
                "phone":   "+39 06 4567 2300",
                "email":   "roma@studioferri.legal",
                "hours":   "Lun – Ven · 09h00 – 19h00",
            },
            {
                "city":    "Milan",
                "tag":     "Siège de Milan",
                "address": "Corso Venezia 11 · 20121",
                "area":    "Porta Venezia · près des Giardini Pubblici",
                "phone":   "+39 02 7634 5500",
                "email":   "milano@studioferri.legal",
                "hours":   "Lun – Ven · 09h00 – 19h00",
            },
        ],

        "channels_label": "Canaux directs",
        "channels": [
            ("Secrétariat du Cabinet",
             "+39 06 4567 2300",
             "Lun – Ven · 09h00 – 19h00"),
            ("Email institutionnel",
             "studio@studioferri.legal",
             "Réponse sous 48 heures ouvrées"),
            ("Courriel certifié (PEC)",
             "studio.ferri@cert.ordineavvocatiroma.it",
             "Pour actes et notifications"),
        ],

        "footnote":
            "Le Studio Legale Ferri ne délivre pas d'avis "
            "préliminaire par courriel sans un premier "
            "entretien avec un associé. Les informations "
            "administratives (paramètres tarifaires indicatifs, "
            "modalités de facturation, critères d'acceptation "
            "du mandat) sont présentées au cours de l'entretien "
            "préliminaire confidentiel, jamais par écrit en "
            "phase préliminaire.",
    },
}


# ─────────────────────────────────────────────────────────────────
# D-047 — chrome-authoring contract.
# Every visible string in the lawyer/classic-gold skin templates
# must come from THIS file (or from chrome.* / dna.content.*).
# Zero literal "Ferri", "1962", "Roma", "Via Piemonte", partner
# names, headline text, or other brand-specific strings in the
# .html files. When a new label is needed in the skin, add it here
# first (preferably under `site` if shared across pages, or under
# the page block if scoped) and read it via `{{ page_data.* }}` /
# `{{ site.* }}`.
# ─────────────────────────────────────────────────────────────────
