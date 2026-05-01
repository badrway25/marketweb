"""Cornice — Studio d'architecture (corporate-suite archetype) ·
locale française.

Phase X.5 Cornice · workflow C · déploiement multilingue posé sur le
brouillon italien LF-2 verrouillé (A.6 review-lock). Reflète
exactement la forme de ``CORNICE_CONTENT_IT`` — mêmes clés, mêmes
imbrications, mêmes formes de listes. Seules les valeurs sont
traduites et adaptées.

Registre éditorial-curatorial · discipline architecturale. Voix
française native équivalente à celle de l'IT — la presse
d'architecture francophone (L'Architecture d'Aujourd'hui, AMC, Le
Moniteur Architecture, Domus française, AA' files). Adulte-à-adulte,
déclaratif, jamais SaaS-marketing. Vouvoiement formel.

Voice anchor (CS-EXEC-01 / CS-BLOCK-11 · préservé verbatim-en-
traduction sur les 5 locales · l'italique porte le mot CURATORIAL
équivalent — `argument` est le cognat français direct d'`argomento` et
porte le même sens discursif-thèse) :
    "Chaque projet est un <em>argument</em> construit, non un service rendu."

Les références normatives italiennes et les noms propres sont
préservés (D.lgs. 24/2023, Codice dei Beni Culturali D.lgs. 42/2004,
D.M. 154/2017 qualification MIBAC, OAPPC Milano, CNAPPC,
Soprintendenza Belle Arti, PRG, DAStU Politecnico di Milano, Reg. UE
679/2016 / RGPD). Adresses, numéros de téléphone, montants en euros
et années conservés tels quels. Garde-fous anti-pattern : pas de
« libérez le potentiel », pas de « meilleur cabinet de Milan », pas
de citations Le Corbusier / Mies / Renzo Piano, pas de moodboard
Pinterest.
"""
from __future__ import annotations

from typing import Any


from apps.catalog.template_content_cornice import (  # noqa: E402
    _HERO_BOLOGNA_PORTICO,
    _PORTRAIT_FOUNDER,
    _CASE_CONCORSO,
    _CASE_RESIDENZIALE,
    _CASE_RESTAURO,
    _CASE_CORNICE_DETAIL,
)


CORNICE_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "L'agence",   "kind": "home"},
        {"slug": "studio",    "label": "Archive",    "kind": "about"},
        {"slug": "servizi",   "label": "Pratique",   "kind": "services"},
        {"slug": "progetti",  "label": "Projets",    "kind": "case_study_list"},
        {"slug": "contatti",  "label": "Contact",    "kind": "contact"},
    ],

    "site": {
        "logo_initial": "C",
        "logo_word":     "CORNICE",
        "logo_subtitle": "studio d'architecture",
        "tag":           "Architecture éditoriale · Milan · depuis 2008",
        "phone":         "+39 02 6610 4708",
        "email":         "fascicolo@cornice-architettura.it",
        "address":       "Via Pasquale Paoli 9 · 20143 Milan",
        "hours_compact": "Mar – Ven · 10h00 – 18h00 · sur rendez-vous",
        "hours_footer_rows": [
            "Samedi · uniquement sur rendez-vous de chantier",
            "Dimanche · fermé",
        ],
        "license": "Tableau OAPPC Milan N° 12 847 · CNAPPC · qualification MIBAC restauration",
        "footer_intro":
            "Architecture éditoriale · commandes publiques et "
            "privées · Milan depuis 2008. Quarante-sept ouvrages "
            "réalisés, vingt-trois concours rendus, quatre-vingt-dix "
            "fascicules ouverts dans la collection monographique.",
        "foot_studio":   "Agence",
        "foot_pages":    "Pages",
        "foot_contact":  "Contact",
        "foot_offices":  "Siège",
        "offices_footer_rows": [
            "Milan · Via Paoli 9 (siège unique)",
            "Agence ouverte sur rendez-vous · mardi-vendredi",
            "Chantiers actifs · Bologne · Pietrasanta · Rome",
        ],
        "whistleblowing_footer": {
            "heading":      "Signalements",
            "eyebrow":      "Canal interne · D.lgs. 24/2023",
            "note":
                "L'agence a mis en place un canal de signalement "
                "interne conforme au D.lgs. 24/2023 (directive UE "
                "2019/1937). Anonymat préservé, données "
                "confidentielles. Le canal est ouvert aux maîtres "
                "d'ouvrage publics, fournisseurs de chantier et "
                "collaborateurs externes.",
            "email":        "whistleblowing@cornice-architettura.it",
            "policy_label": "Politique de gestion des signalements",
            "policy_href":  "contatti",
        },
        "case_practice_label":     "Programme",
        "case_year_label":         "Année du fascicule",
        "case_duration_label":     "État du chantier",
        "case_lead_label":         "Architecte référent",
        "case_lead_partner_label": "Architecte référent",
        "case_team_label":         "Équipe de chantier",
        "case_timeline_label":     "Chronologie de chantier",
    },

    "home": {
        "eyebrow":     "STUDIO D'ARCHITECTURE · MILAN · DEPUIS 2008",
        "headline":
            "Chaque projet est un <em>argument</em> construit, non un service rendu.",
        "intro":
            "Studio d'architecture éditoriale · commandes publiques "
            "et privées · quatre-vingt-dix fascicules ouverts depuis "
            "2008.",
        "primary_cta":   "Ouvrir un fascicule projet",
        "primary_href":  "contatti",
        "secondary_cta": "L'agence · publications",
        "secondary_href":"studio",

        "hero_image":              _HERO_BOLOGNA_PORTICO,
        "hero_image_alt":          "Portique restauré à Bologne · 2023",
        "hero_image_credit_left":  ("Bologne · portique restauré · 2023", "fascicule n° 31"),
        "hero_image_credit_right": ("Siège de l'agence", "Milan · Via Paoli 9"),
        "hero_meta_strip": [
            ("Ouvrages réalisés",   "47"),
            ("Années de pratique",  "18"),
            ("Villes italiennes",   "6"),
        ],
        # Em sur la forme verbale dérivée — `s'argumente` (verbe
        # pronominal du substantif curatorial `argument`). Le motif
        # éditorial-curatorial est porté par la racine commune.
        "hero_side_quote":
            "La bonne architecture <em>s'argumente</em> — elle ne "
            "se démontre pas, ne se vend pas, ne se décore pas.",

        "narrative_label":   "L'AGENCE · MANIFESTE ÉDITORIAL",
        "narrative_drop":    "L",
        "narrative_blocks": [
            ("drop",
             "a bonne architecture s'argumente. Cornice est une "
             "agence d'architecture éditoriale : chaque projet "
             "publié est un argument construit sur le site, sur la "
             "commande, sur la contrainte. Nous ne signons pas des "
             "images séduisantes — nous publions des ouvrages, "
             "chacun avec son histoire de chantier et sa "
             "documentation propre. L'agence existe pour mesurer le "
             "contexte avant de le dessiner, pour écrire le "
             "programme avant de l'habiter, pour reconnaître ce qui "
             "est déjà là avant d'ajouter ce qui manque. C'est un "
             "métier lent, qui produit peu de pages par an, mais qui "
             "les produit entières."),

            ("quote",
             "Le relevé est la <em>première</em> forme de respect. "
             "Ce qui s'argumente sur un site déjà lu sera toujours "
             "plus solide que ce qui se décore sur un site muet."),

            ("para",
             "Chaque commande traverse quatre saisons. Le relevé, "
             "d'abord : l'ouvrage qui existe est lu comme un texte, "
             "avec ses accents, ses paragraphes, ses césures. Le "
             "contexte, ensuite : la commande, l'usage, les "
             "contraintes du PLU et de la Soprintendenza, les "
             "habitudes du paysage. L'argument, enfin : le projet "
             "s'écrit comme une thèse — quel problème il résout, "
             "quel héritage il respecte, quelle figure il propose. "
             "Alors seulement nous ouvrons le chantier, et le "
             "suivons semaine par semaine, lieu par lieu, jusqu'à "
             "la réception. Les décisions de projet restent "
             "écrites : nous publions chaque ouvrage dans notre "
             "collection monographique, parce qu'une architecture "
             "sans mémoire ne laisse aucune règle."),

            ("quote",
             "Un <em>auteur</em> n'est pas celui qui signe le plus "
             "de projets, mais celui qui sait dire quel projet il "
             "n'a pas signé — et pourquoi."),

            ("para",
             "Nous travaillons pour des maîtres d'ouvrage publics "
             "et privés qui cherchent un auteur — pas un exécutant, "
             "pas un forfait clé en main. Communes restaurant une "
             "cour historique, organismes culturels reprogrammant "
             "un édifice désaffecté, familles réécrivant une maison "
             "de campagne, opérateurs privés à sensibilité "
             "éditoriale, services techniques municipaux engageant "
             "un concours. Notre signature est celle d'un seul "
             "architecte, non d'une marque à plusieurs mains : la "
             "responsabilité auctoriale reste concentrée, parce "
             "qu'un argument doit avoir une voix pour être "
             "reconnaissable. Les collaborations avec ingénieurs "
             "structure, paysagistes, restaurateurs et techniciens "
             "de chantier passent par l'agence, elles ne la "
             "remplacent pas."),

            ("quote",
             "Publier un projet n'est pas le promouvoir. C'est "
             "laisser une <em>règle</em> — afin que celui qui "
             "viendra après puisse la contester, la modifier, ou "
             "la reconnaître."),

            ("para",
             "Les ouvrages publiés ici ne sont pas un portfolio "
             "commercial. Ce sont des arguments construits, "
             "rassemblés par programme et par année, avec la "
             "documentation de chantier qui les accompagne. Chaque "
             "fiche nomme le site, la commande, le programme, la "
             "chronologie, la contrainte, et l'argument du projet "
             "en cinq lignes — parce qu'un ouvrage qui ne se laisse "
             "pas raconter en cinq lignes n'a probablement pas "
             "encore été éclairci."),
        ],
        "narrative_side_rail": [
            ("L'agence", "studio"),
            ("Pratique · commandes", "servizi"),
            ("Projets · fascicules", "progetti"),
            ("Contact · siège", "contatti"),
        ],

        "sectors_label": "TYPOLOGIES D'INTERVENTION",
        "sectors_lead":
            "L'agence intervient sur douze typologies principales, "
            "groupées par échelle de l'ouvrage, programme de la "
            "commande et rapport à la contrainte paysagère ou "
            "patrimoniale. Nous ne travaillons pas à un menu de "
            "services : chaque entrée nomme un argument déjà "
            "construit, déjà publié en fascicule monographique.",
        "sectors": [
            "résidentiel", "public", "intérieur", "paysage",
            "restauration", "concours", "culturel", "tertiaire",
            "industriel", "santé", "scolaire", "mixte",
        ],
        "sectors_trailing":
            "Les ouvrages de restauration et de concours passent "
            "par la qualification MIBAC et par les procédures de la "
            "Soprintendenza ; les commandes publiques entrent par "
            "marché ou par concours sur invitation.",
        "sectors_counter":
            "Numérotation des interventions publiées dans la "
            "collection : depuis 2008, <em>quatre-vingt-dix</em> "
            "fascicules ouverts — quarante-sept ouvrages réalisés "
            "et réceptionnés, vingt-trois concours rendus, dix "
            "publications majeures.",

        "leadership_label":   "FONDATRICE DE L'AGENCE · ARCHITECTE",
        "leadership_heading": "Marta <em>Roveri</em>",
        "leadership_role":    "fondatrice · responsable éditoriale des fascicules",
        "leadership_caption": "L'agence · intérieur · 2024",
        "leadership_portrait": _PORTRAIT_FOUNDER,
        "leadership_bio_paragraphs": [
            "Marta Roveri a ouvert Cornice en 2008, après dix "
            "années de pratique entre Milan et Bologne dans deux "
            "agences de restauration publique. Elle s'est formée au "
            "Politecnico di Milano sous la chaire de restauration "
            "architecturale, avec une période de recherche à "
            "l'École Polytechnique de Lausanne sur les caractères "
            "stéréotomiques des voûtes en pierre. Elle travaille à "
            "plein temps sur les projets de l'agence : elle dirige "
            "le relevé, écrit l'argument du fascicule, suit le "
            "chantier jusqu'à la réception, et tient la collection "
            "monographique qui publie les ouvrages réalisés.",

            "Parmi les ouvrages réalisés, la restauration de la "
            "cour de Palazzo Lignari à Bologne (2019, qualification "
            "MIBAC), le concours remporté pour la nouvelle "
            "bibliothèque civique de Pietrasanta (2021, en "
            "chantier) et l'immeuble résidentiel de la Via Volpe à "
            "Rome (2023, six logements sur lot étroit). Ses notes "
            "critiques — sur le rapport entre corniche et façade "
            "secondaire, sur la règle du module dans les concours "
            "publics — sont rassemblées dans deux monographies "
            "publiées par la collection de l'agence (2018, 2024) "
            "et dans des essais parus dans Casabella, Domus et Il "
            "Giornale dell'Architettura.",
        ],
        "leadership_credentials": [
            "Tableau OAPPC · Ordre des Architectes de Milan N° 12 847",
            "CNAPPC · Conseil National des Architectes P.P.C.",
            "MIBAC · Qualification pour la restauration architecturale (D.M. 154/2017)",
            "Politecnico di Milano · Professeure associée · Chaire de Restauration",
        ],
        "leadership_secondary_cta_label": "L'agence · biographie complète",
        "leadership_secondary_cta_href":  "studio",

        "cases_label":   "PROJETS — ARGUMENTS CONSTRUITS",
        "cases_intro":
            "Quatre fascicules ouverts, dans l'ordre de "
            "publication. Site, commande, programme, année, "
            "contrainte, et l'argument de l'ouvrage.",
        "cases_magazine": [
            {
                "rank":     "hero",
                "num":      "01",
                "eyebrow":  "01 · CONCOURS REMPORTÉ · 2021 · PIETRASANTA (LU)",
                "title":    "Bibliothèque civique · l'argument est la <em>géométrie</em> du module",
                "body":
                    "Concours sur invitation pour la nouvelle "
                    "bibliothèque civique de Pietrasanta. Lot en "
                    "lisière du centre historique, à soixante "
                    "mètres de l'enceinte, avec contrainte "
                    "paysagère et double front (rue urbaine à "
                    "l'est, parc public à l'ouest). L'argument du "
                    "projet est un module de six mètres par neuf, "
                    "répété huit fois, qui organise trois salles "
                    "de lecture, un dépôt en double hauteur et un "
                    "portique continu vers le parc. La peau en "
                    "béton brut raconte la règle, les ouvertures "
                    "lisent la lumière, la corniche du front tient "
                    "ensemble la portée civile de l'édifice.",
                "pill":     "Programme · concours / culturel  ·  1 450 m²  ·  5,2 M €",
                "photo":    _CASE_CONCORSO,
                "photo_alt":"Architecture minimaliste en béton · concours Pietrasanta",
                "slug":     "biblioteca-pietrasanta-concorso",
            },
            {
                "rank":     "small",
                "num":      "02",
                "eyebrow":  "02 · OUVRAGE RÉALISÉ · 2023 · ROME (TIBURTINO)",
                "title":    "Via Volpe — six logements sur <em>lot</em> étroit",
                "body":
                    "Immeuble résidentiel de six logements sur lot "
                    "urbain de neuf mètres de front et "
                    "vingt-huit de profondeur. L'argument est la "
                    "profondeur : le front se ferme, l'intérieur "
                    "s'ouvre sur une cour aveugle portée en "
                    "couverture. Cinq niveaux plus combles, "
                    "structure béton, remplissage en brique "
                    "apparente. Publié dans le fascicule n° 38 de "
                    "la collection.",
                "pill":     "Programme · résidentiel  ·  720 m²  ·  privé",
                "photo":    _CASE_RESIDENZIALE,
                "photo_alt":"Bâtiments résidentiels contemporains à Rome · Via Volpe",
                "slug":     "via-volpe-roma-residenziale",
            },
            {
                "rank":     "small",
                "num":      "03",
                "eyebrow":  "03 · RESTAURATION PUBLIQUE · 2019 · BOLOGNE (CENTRE)",
                "title":    "Palazzo Lignari — la cour comme <em>argument</em> civil",
                "body":
                    "Restauration de la cour intérieure et du "
                    "piano nobile de Palazzo Lignari, siège d'une "
                    "institution culturelle municipale. L'argument "
                    "est la cour comme espace civique : le "
                    "portique restauré redevient un passage "
                    "public, les pavements en terre cuite lisent "
                    "les trois interventions historiques "
                    "stratifiées. Qualification MIBAC ; "
                    "Soprintendenza Belle Arti de Bologne.",
                "pill":     "Programme · restauration / public  ·  980 m²  ·  MIBAC",
                "photo":    _CASE_RESTAURO,
                "photo_alt":"Cour historique bolonaise restaurée · Palazzo Lignari",
                "slug":     "palazzo-lignari-bologna-restauro",
            },
            {
                "rank":     "small",
                "num":      "04",
                "eyebrow":  "04 · PUBLICATION · 2024 · ESSAI EN COLLECTION",
                "title":    "La corniche de la façade <em>secondaire</em> — une note critique",
                "body":
                    "Essai illustré sur la règle de la corniche "
                    "dans les façades secondaires du bâti "
                    "milanais du XIXᵉ siècle. Cent vingt-quatre "
                    "façades relevées, vingt-deux corniches "
                    "typologiques, huit règles de proportion "
                    "documentées. La publication argumente la "
                    "valeur de la corniche comme dispositif "
                    "civil, non décoratif. Co-édition avec le "
                    "Politecnico di Milano · DAStU.",
                "pill":     "Programme · publication  ·  124 façades  ·  DAStU",
                "photo":    _CASE_CORNICE_DETAIL,
                "photo_alt":"Détail de corniche et chapiteau · essai en collection 2024",
                "slug":     "cornice-fronte-minore-saggio",
            },
        ],
        "cases_trailing_label": "Tous les fascicules ouverts · chronologie 2008–2024",
        "cases_trailing_href":  "progetti",

        "cta_label":     "FASCICULE PROJET",
        "cta_intro":
            "Les commandes commencent par une seule page : le fascicule projet.",
        "cta_heading":
            "Chaque projet est un <em>argument</em> construit, non un service rendu.",
        "cta_form_hint":
            "Brief en français ou italien · site · programme · "
            "calendrier · documents déjà disponibles. Réponse "
            "sous cinq jours ouvrés.",
        "cta_primary":   "Ouvrir un fascicule projet",
        "cta_primary_href": "contatti",
        "cta_closing_line":
            "Pas d'appel découverte. Pas de devis au temps "
            "passé. Seulement l'argument du projet, et sa règle.",
        "cta_sub_line":
            "Cornice · studio d'architecture · Milan · depuis 2008",
    },

    "studio": {
        "eyebrow":   "L'AGENCE · ARCHIVE · CV",
        "headline":  "Cornice · studio d'architecture éditoriale depuis <em>2008</em>.",
        "intro":
            "Milan. Une architecte fondatrice, deux "
            "collaborateurs, quatre-vingt-dix fascicules ouverts. "
            "Nous travaillons peu, et entièrement.",

        "history_label":   "JALONS DE L'AGENCE",
        "history_heading": "Cinq dates, seize années de pratique éditoriale.",
        "history_intro":
            "Cinq choix structurels derrière lesquels se lit le "
            "caractère de l'agence — l'auctorialité d'un seul "
            "architecte, la collection monographique comme "
            "méthode, le relevé comme premier geste de respect, "
            "la corniche comme dispositif civil, la restauration "
            "qualifiée comme pratique de lecture.",
        "history": [
            ("2008", "Fondation",
             "Marta Roveri ouvre Cornice Via Paoli à Milan, "
             "après dix ans de collaboration dans deux agences "
             "de restauration publique entre Milan et Bologne. "
             "Le siège est choisi pour une seule raison : deux "
             "pièces sur cour intérieure, une pour le relevé, "
             "une pour l'écriture."),
            ("2014", "Qualification MIBAC restauration",
             "Marta Roveri obtient la qualification pour la "
             "restauration architecturale (D.M. 154/2017). "
             "Depuis cette année, l'agence accepte des commandes "
             "de restauration sur des édifices protégés au titre "
             "du Code du Patrimoine et traite les dossiers avec "
             "la Soprintendenza Belle Arti."),
            ("2017", "Chaire au Politecnico di Milano",
             "Marta Roveri est nommée Professeure associée sur "
             "la Chaire de Restauration au Politecnico di "
             "Milano. La pratique de l'enseignement entre dans "
             "la méthode de l'agence : le relevé, le contexte et "
             "l'argument s'écrivent comme une thèse."),
            ("2019", "Palazzo Lignari · première restauration publique",
             "L'agence livre la restauration de la cour et du "
             "piano nobile de Palazzo Lignari à Bologne (siège "
             "culturel municipal · Soprintendenza Belle Arti). "
             "Publiée dans le fascicule n° 31 de la collection "
             "monographique."),
            ("2024", "Essai sur la corniche de la façade secondaire",
             "Co-édition avec le Politecnico di Milano · DAStU "
             "· essai illustré sur la règle de la corniche dans "
             "les façades secondaires du bâti milanais du XIXᵉ "
             "siècle. Publié dans le fascicule n° 47. La "
             "collection monographique atteint quatre-vingt-dix "
             "fascicules ouverts."),
        ],

        "values_label":   "PRINCIPES ÉDITORIAUX",
        "values_heading": "Quatre principes <em>non négociables</em>",
        "values_intro":
            "Ce sont les quatre principes qui séparent un "
            "fascicule Cornice d'une commande standardisée. Ils "
            "sont écrits dans le mandat signé en première réunion, "
            "non sur le site internet.",
        "values": [
            ("01", "Un architecte auteur",
             "La signature du projet est celle d'un seul "
             "architecte, non d'une marque à plusieurs mains. La "
             "responsabilité auctoriale reste concentrée, parce "
             "qu'un argument doit avoir une voix pour être "
             "reconnaissable. Les collaborations externes passent "
             "par l'agence, elles ne la remplacent pas."),
            ("02", "Le relevé comme premier geste",
             "Chaque commande s'ouvre sur un relevé sérieux. "
             "L'ouvrage existant est lu comme un texte, avec ses "
             "accents, ses paragraphes, ses césures. Pas de "
             "projet avant que le site ait été lu intégralement."),
            ("03", "La collection monographique comme méthode",
             "Tous les ouvrages réalisés sont publiés dans la "
             "collection monographique dans les douze mois "
             "suivant la réception, avec la documentation de "
             "chantier complète. La collection n'est pas du "
             "marketing : c'est la règle que nous laissons à qui "
             "viendra après."),
            ("04", "Pas de devis au temps passé",
             "Les honoraires de l'agence sont calculés sur les "
             "tarifs minima CNAPPC par classe et catégorie, sans "
             "remises en pourcentage. La première évaluation "
             "d'une commande est gratuite ; les études "
             "préliminaires refusées ne sont pas facturées."),
        ],

        "team_label":   "AGENCE ET COLLABORATEURS",
        "team_heading": "Trois architectes, un seul siège.",
        "team_intro":
            "L'agence est composée d'une architecte fondatrice "
            "et de deux collaborateurs. Nous travaillons à plein "
            "temps sur trois ou quatre commandes en parallèle, "
            "jamais davantage. Les dossiers Soprintendenza, les "
            "services municipaux et les autorités contractantes "
            "sont traités en agence, jamais délégués.",
        "team": [
            {"name": "Marta Roveri",
             "role": "Fondatrice · Architecte",
             "office": "Milan",
             "bio": "Fondatrice. Politecnico di Milano · chaire "
                    "de restauration architecturale · recherche "
                    "à l'EPFL Lausanne sur les caractères "
                    "stéréotomiques des voûtes en pierre. "
                    "Tableau OAPPC Milan N° 12 847 · CNAPPC · "
                    "qualification MIBAC restauration. "
                    "Professeure associée au Politecnico di "
                    "Milano depuis 2017."},
            {"name": "Architecte associé",
             "role": "Architecte associé · Chantier",
             "office": "Milan",
             "bio": "Architecte associé depuis 2018. "
                    "Politecnico di Torino · master en "
                    "conception du paysage. Tableau OAPPC "
                    "Milan. S'occupe du chantier et de la "
                    "coordination des commandes publiques, en "
                    "particulier des dossiers Soprintendenza et "
                    "des relations avec les services "
                    "municipaux."},
            {"name": "Architecte junior",
             "role": "Architecte junior · Relevé",
             "office": "Milan",
             "bio": "Architecte junior depuis 2022. Politecnico "
                    "di Milano · mémoire sur la corniche comme "
                    "dispositif civil (directrice de mémoire : "
                    "Roveri). Tableau OAPPC Milan. S'occupe du "
                    "relevé numérique, du modèle, et de la "
                    "rédaction graphique des fascicules. "
                    "Co-auteure de l'essai sur la corniche "
                    "(collection, 2024)."},
        ],

        "coordinates_label": "LE SIÈGE",
        "coordinates": [
            ("Milan", "Via Pasquale Paoli 9 · 20143 · deux pièces sur cour intérieure"),
            ("Agence", "ouverte sur rendez-vous · mardi-vendredi · 10h00-18h00"),
            ("Chantiers actifs", "Bologne · Pietrasanta · Rome · en cours 2024-2026"),
        ],

        "cta_heading": "Une commande commence par une seule page.",
        "cta_intro":
            "La première page de chaque commande est le "
            "fascicule projet : une fiche de synthèse que "
            "l'agence lit intégralement, et à laquelle elle "
            "répond sous cinq jours ouvrés par une note "
            "critique.",
        "cta_primary":   "Ouvrir un fascicule projet",
        "cta_primary_href": "contatti",
    },

    "servizi": {
        "eyebrow":  "PRATIQUE · COMMANDES · QUALIFICATIONS",
        "headline": "Quatre modes de <em>commande</em>.",
        "intro":
            "L'agence accepte des commandes directes, des "
            "concours publics, des restaurations qualifiées MIBAC "
            "et des publications en collection. Pas de forfait clé "
            "en main.",

        "svc_duration_label": "Cadence",
        "svc_leader_label":   "Architecte référent",

        "services": [
            {
                "num":   "01",
                "title": "Commande directe",
                "blurb":
                    "Familles réécrivant une maison de campagne, "
                    "opérateurs privés à sensibilité éditoriale, "
                    "communautés religieuses reprogrammant un "
                    "édifice désaffecté, petites entreprises "
                    "construisant un siège. La commande directe "
                    "est le mode le plus ancien de l'agence : le "
                    "maître d'ouvrage apporte un site et un "
                    "programme, l'agence écrit l'argument et "
                    "accompagne le projet jusqu'à la réception.",
                "scope": [
                    "Relevé initial inclus · cinq jours sur place",
                    "Fascicule monographique inclus · publié à la réception",
                    "Permis et direction de chantier inclus",
                    "Tarifs minima CNAPPC · sans remise en pourcentage",
                ],
                "duration": "Du relevé à la réception · 18-30 mois",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "02",
                "title": "Concours public",
                "blurb":
                    "L'agence participe à des concours publics "
                    "(procédure ouverte, restreinte, dialogue "
                    "compétitif) et à des concours sur invitation "
                    "lancés par communes, organismes culturels, "
                    "fondations, régions. Notre signature est "
                    "celle d'un seul architecte — non d'un "
                    "consortium pluridisciplinaire — donc nous "
                    "n'acceptons les concours que lorsque "
                    "l'argument du projet peut porter notre voix.",
                "scope": [
                    "Vingt-trois concours rendus depuis 2008",
                    "Six remportés · quatre en short-list · treize publiés",
                    "Planches archivées et disponibles pour le maître d'ouvrage",
                    "Inscription CNAPPC vérifiable",
                ],
                "duration": "Selon le programme · 2-9 mois",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "03",
                "title": "Restauration qualifiée MIBAC",
                "blurb":
                    "Marta Roveri est habilitée à la restauration "
                    "architecturale selon le D.M. 154/2017. "
                    "L'agence accepte des commandes de "
                    "restauration sur des édifices protégés au "
                    "titre du Code du Patrimoine (D.lgs. "
                    "42/2004) et sur cours, portiques, façades "
                    "secondaires, édifices du XIXᵉ et XXᵉ siècle. "
                    "Les stratigraphies se lisent comme des textes.",
                "scope": [
                    "Qualification MIBAC vérifiable (D.M. 154/2017)",
                    "Dossiers Soprintendenza traités en interne",
                    "Trois ouvrages de restauration publique réalisés",
                    "Publication intégrale en collection monographique",
                ],
                "duration": "24-48 mois · contraintes incluses",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "04",
                "title": "Publication éditoriale",
                "blurb":
                    "L'agence publie ses propres projets en "
                    "collection monographique, mais accepte aussi "
                    "des commandes externes de publication : "
                    "monographies sur les façades secondaires, "
                    "essais typologiques, fiches critiques pour "
                    "catalogues d'exposition, entrées pour "
                    "ouvrages de référence. Un argument de "
                    "projet publié sans être construit est un "
                    "argument que la discipline peut reprendre.",
                "scope": [
                    "Essai illustré · 80-200 pages",
                    "Co-édition avec institutions académiques",
                    "Tirage limité · 200 exemplaires numérotés",
                    "Distribution musées + librairies spécialisées",
                ],
                "duration": "De la commande à l'impression · 12-18 mois",
                "leader":   "Marta Roveri",
            },
        ],

        "process_label":   "MÉTHODE · QUATRE SAISONS",
        "process_heading": "Quatre phases, une seule séquence éditoriale.",
        "process": [
            ("01", "Relevé",
             "L'ouvrage existant est lu comme un texte. "
             "Mesures, matériaux, césures, accents. Le relevé "
             "est la première forme de respect et dure "
             "typiquement cinq jours sur place."),
            ("02", "Contexte",
             "Maîtrise d'ouvrage, contraintes du PLU, "
             "contraintes paysagères et de la Soprintendenza, "
             "règlement de construction, habitudes du site. Le "
             "contexte est la corniche du projet."),
            ("03", "Argument",
             "Le projet s'écrit comme une thèse — quel problème "
             "il résout, quel héritage il respecte, quelle "
             "figure il propose. Cinq lignes dans lesquelles "
             "l'ouvrage doit pouvoir se raconter."),
            ("04", "Chantier",
             "Semaine par semaine, lieu par lieu, jusqu'à la "
             "réception. Tout reste écrit dans le fascicule "
             "monographique — publié dans les douze mois suivant "
             "la réception."),
        ],

        "cta_heading":   "Quel mode convient à votre projet ?",
        "cta_intro":
            "Si le mode n'est pas clair, écrivez-nous une brève "
            "description du site et de l'intervention envisagée. "
            "Nous indiquerons le mode juste sous cinq jours "
            "ouvrés — même sans ouverture de fascicule.",
        "cta_primary":   "Ouvrir un fascicule projet",
        "cta_primary_href": "contatti",
    },

    "progetti": {
        "eyebrow":  "PROJETS · FASCICULES OUVERTS · 2008-2024",
        "headline": "Quarante arguments <em>construits</em>.",
        "intro":
            "Quarante-sept ouvrages réalisés, vingt-trois "
            "concours rendus, dix publications majeures. Tous "
            "les fascicules sont en collection monographique.",

        "cases_label": "Quatre fascicules représentatifs · en détail",
        "cases_intro":
            "Pour chaque fascicule ouvert nous publions ici la "
            "page d'argument — site, commande, programme, "
            "chronologie, contrainte, et l'argument du projet en "
            "cinq lignes.",

        "cta_heading":   "Un argument proche du vôtre ?",
        "cta_intro":
            "Les fascicules complets (relevé, planches "
            "techniques, documentation de chantier, note "
            "critique de clôture) sont disponibles à l'agence sur "
            "demande motivée. La consultation est gratuite ; le "
            "fascicule imprimé est cédé à couverture des frais "
            "d'impression.",
        "cta_primary":   "Demander un fascicule à l'agence",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "biblioteca-pietrasanta-concorso",
            "title":    "Bibliothèque civique · l'argument est la géométrie du module",
            "category": "Concours · culturel",
            "year":     "2021",
            "duration": "Chantier ouvert · réception prévue 2026",
            "client_code":
                "Concours sur invitation remporté · Commune de "
                "Pietrasanta (Direction Culture) · 1 450 m² · "
                "5,2 M € · contrainte paysagère · double front "
                "(urbain + parc).",
            "lead":
                "Concours sur invitation pour la nouvelle "
                "bibliothèque civique de Pietrasanta. L'argument "
                "du projet est un module de six mètres par neuf, "
                "répété huit fois, qui organise trois salles de "
                "lecture, un dépôt en double hauteur et un "
                "portique continu vers le parc public.",
            "sections": [
                {
                    "label": "Le site",
                    "heading": "Un double front et une contrainte paysagère",
                    "body":
                        "Lot en lisière du centre historique de "
                        "Pietrasanta, à soixante mètres de "
                        "l'enceinte, avec contrainte paysagère "
                        "au titre du Code du Patrimoine (D.lgs. "
                        "42/2004) et double front : rue urbaine à "
                        "l'est, parc public à l'ouest. Le relevé "
                        "s'est clos sur douze semaines de "
                        "campagne en 2020, deux stratigraphies "
                        "sur les murets périmétriques et une "
                        "campagne photographique sur les "
                        "contextes adjacents.",
                },
                {
                    "label": "L'argument",
                    "heading": "Un module qui s'argumente, qui ne se voit pas",
                    "body":
                        "Le module de six mètres par neuf se "
                        "répète huit fois selon une matrice "
                        "orthogonale. La peau en béton brut "
                        "raconte la règle, les ouvertures lisent "
                        "la lumière solaire le long de l'arc du "
                        "jour, la corniche du front tient "
                        "ensemble la portée civile de l'édifice "
                        "vers la rue et l'ouverture au parc vers "
                        "l'ouest. Le module ne se voit pas : il "
                        "s'argumente.",
                },
                {
                    "label": "Le chantier",
                    "heading": "Chantier ouvert novembre 2023",
                    "body":
                        "Chantier ouvert en novembre 2023 après "
                        "remise du dossier d'exécution en mai "
                        "2023. Direction des travaux assurée par "
                        "l'agence. Réception prévue juin 2026, "
                        "avec ouverture au public en septembre "
                        "2026 à l'occasion de l'inauguration de "
                        "la saison culturelle municipale. Le "
                        "fascicule monographique sera publié à la "
                        "réception (n° 44 de la collection).",
                },
            ],
            "kpi": [
                ("1 450 m²", "surface nette"),
                ("8",        "modules répétés"),
                ("5,2 M €",  "valeur d'ouvrage"),
                ("2026",     "réception prévue"),
            ],
            "lead_partner": "Marta Roveri · Fondatrice",
            "team":         "Architecte + 2 collaborateurs · ingénieur structure externe · DET en interne",
            "next_label":   "Fascicule suivant",
        },
        {
            "slug":     "via-volpe-roma-residenziale",
            "title":    "Via Volpe — six logements sur lot étroit",
            "category": "Résidentiel · privé",
            "year":     "2023",
            "duration": "Réalisé · réception juin 2023",
            "client_code":
                "Immeuble résidentiel · six logements · maître "
                "d'ouvrage privé · lot urbain 9×28 m · 720 m² "
                "SHON · cinq niveaux + combles · publié dans le "
                "fascicule n° 38.",
            "lead":
                "Immeuble résidentiel de six logements sur lot "
                "urbain de neuf mètres de front et vingt-huit de "
                "profondeur. L'argument est la profondeur : le "
                "front se ferme, l'intérieur s'ouvre sur une cour "
                "aveugle portée en couverture.",
            "sections": [
                {
                    "label": "Le site",
                    "heading": "Neuf mètres de front, vingt-huit de profondeur",
                    "body":
                        "Lot résidentiel à Tiburtino, Rome, dans "
                        "une rue de bâti mixte des années "
                        "Cinquante. Contraintes du PLU communal "
                        "assez permissives sur la hauteur, mais "
                        "strictes sur la profondeur d'élévation. "
                        "Le maître d'ouvrage demandait six "
                        "logements en vente, garage en sous-sol, "
                        "espace vert partagé.",
                },
                {
                    "label": "L'argument",
                    "heading": "La profondeur portée en couverture",
                    "body":
                        "L'argument du projet résout la "
                        "contrainte de profondeur en portant la "
                        "cour aveugle du sous-sol au niveau de "
                        "couverture — un patio commun en "
                        "altitude, cinq mètres par huit, éclairé "
                        "par lanterneau. Le front sur rue se "
                        "ferme en brique apparente ; les "
                        "logements reçoivent la lumière par les "
                        "deux côtés courts et par le patio en "
                        "couverture.",
                },
                {
                    "label": "Le chantier",
                    "heading": "Dix-neuf mois · chantier clos 2023",
                    "body":
                        "Chantier ouvert octobre 2021, réception "
                        "juin 2023. Structure béton, remplissage "
                        "en brique apparente, menuiseries en "
                        "aluminium anodisé bronze. Direction des "
                        "travaux par l'agence. Le fascicule "
                        "n° 38 a été publié dans la collection "
                        "en juin 2024.",
                },
            ],
            "kpi": [
                ("720 m²",  "SHON totale"),
                ("6",       "logements · 70-130 m²"),
                ("19 mois", "durée de chantier"),
                ("n° 38",   "fascicule en collection"),
            ],
            "lead_partner": "Marta Roveri · Fondatrice",
            "team":         "Architecte + 2 collaborateurs · ingénieur structure + DET interne",
            "next_label":   "Fascicule suivant",
        },
        {
            "slug":     "palazzo-lignari-bologna-restauro",
            "title":    "Palazzo Lignari — la cour comme argument civil",
            "category": "Restauration · public",
            "year":     "2019",
            "duration": "Réalisé · réception juin 2019",
            "client_code":
                "Restauration cour intérieure + piano nobile · "
                "Commune de Bologne (Secteur Culture) · "
                "qualification MIBAC · Soprintendenza Belle "
                "Arti Bologne · 980 m² · publié dans le "
                "fascicule n° 31 de la collection (2020).",
            "lead":
                "Restauration de la cour intérieure et du piano "
                "nobile de Palazzo Lignari, siège d'une "
                "institution culturelle municipale dédiée à la "
                "didactique du patrimoine. L'argument est la "
                "cour comme espace civique.",
            "sections": [
                {
                    "label": "Le site",
                    "heading": "Une cour à portique d'origine quattrocento",
                    "body":
                        "Bologne, centre historique, zone A1. "
                        "Contrainte au titre du Code du "
                        "Patrimoine (D.lgs. 42/2004) et "
                        "contrainte Soprintendenza Belle Arti "
                        "pour la ville métropolitaine. Palazzo "
                        "Lignari est d'origine quattrocento, "
                        "remanié au XVIIᵉ, au XIXᵉ et après-"
                        "guerre. La cour intérieure à portique "
                        "conserve deux fronts Renaissance et "
                        "trois stratifications historiques "
                        "distinctes.",
                },
                {
                    "label": "L'argument",
                    "heading": "La restauration n'ajoute pas de figure, elle rend la stratigraphie lisible",
                    "body":
                        "Nous avons écrit deux gestes : le "
                        "premier, le pavement en terre cuite "
                        "posé sur place selon trois orientations "
                        "légèrement différentes, une pour chaque "
                        "stratification historique lue dans le "
                        "relevé ; le second, l'éclairage intégré "
                        "dans le pavement, qui allume les "
                        "césures après le coucher du soleil et "
                        "dessine la cour comme texte lisible "
                        "même la nuit. La règle : la "
                        "restauration rend lisible la "
                        "stratigraphie qui est déjà là.",
                },
                {
                    "label": "Le chantier",
                    "heading": "Trente et un mois · campagne stratigraphique indépendante",
                    "body":
                        "Chantier ouvert novembre 2016, "
                        "réception juin 2019. Les 31 semaines de "
                        "campagne stratigraphique sur les "
                        "pavements ont nécessité la "
                        "collaboration d'un restaurateur "
                        "qualifié et d'une équipe de poseurs "
                        "spécialisés. Les dossiers "
                        "Soprintendenza ont nécessité onze "
                        "visites techniques et trois révisions "
                        "du dossier d'exécution. Réception sans "
                        "prescriptions.",
                },
            ],
            "kpi": [
                ("980 m²",  "cour + piano nobile"),
                ("31 mois", "durée de chantier"),
                ("n° 31",   "fascicule en collection 2020"),
                ("MIBAC",   "qualification restauration"),
            ],
            "lead_partner": "Marta Roveri · Fondatrice",
            "team":         "Architecte + 2 collaborateurs · restaurateur externe · DET interne",
            "next_label":   "Fascicule suivant",
        },
        {
            "slug":     "cornice-fronte-minore-saggio",
            "title":    "La corniche de la façade secondaire — une note critique",
            "category": "Publication · essai",
            "year":     "2024",
            "duration": "Publié · en librairie",
            "client_code":
                "Essai illustré · co-édition Politecnico di "
                "Milano (DAStU) · 124 façades relevées · 22 "
                "corniches typologiques · 8 règles de "
                "proportion · publié dans le fascicule n° 47 "
                "de la collection (2024) · tirage 200 exemplaires.",
            "lead":
                "Essai illustré sur la règle de la corniche dans "
                "les façades secondaires du bâti milanais du "
                "XIXᵉ siècle. La publication argumente la valeur "
                "de la corniche comme dispositif civil, non "
                "décoratif.",
            "sections": [
                {
                    "label": "Le relevé",
                    "heading": "Cent vingt-quatre façades secondaires à Milan",
                    "body":
                        "Le relevé s'est clos entre 2021 et "
                        "2023 sur cent vingt-quatre façades "
                        "secondaires du XIXᵉ siècle dans les "
                        "quartiers Brera, Magenta, Porta Nuova "
                        "et Porta Romana. Pour chaque façade : "
                        "relevé graphique au 1/50, campagne "
                        "photographique en lumière diurne et "
                        "rasante, fiche typologique de la "
                        "corniche et de ses rapports avec le "
                        "front.",
                },
                {
                    "label": "L'argument",
                    "heading": "La corniche comme dispositif civil",
                    "body":
                        "La corniche de la façade secondaire "
                        "n'est pas un ornement : c'est le "
                        "dispositif civil qui tient ensemble la "
                        "façade de l'édifice et la cortine de "
                        "la rue. C'est la règle qui permet à "
                        "des fronts différents de rester en "
                        "conversation. L'essai argumente huit "
                        "règles de proportion documentables et "
                        "vingt typologies récurrentes, et "
                        "propose une ligne directrice "
                        "opératoire pour la restauration "
                        "contemporaine.",
                },
                {
                    "label": "La publication",
                    "heading": "Co-édition Politecnico DAStU · 200 exemplaires",
                    "body":
                        "Publication en co-édition avec le "
                        "Politecnico di Milano · DAStU. Format "
                        "24×33 cm, 192 pages, couverture en "
                        "papier non couché, impression offset "
                        "quadrichromie, tirage limité à 200 "
                        "exemplaires numérotés. Distribution : "
                        "librairies spécialisées · "
                        "bibliothèques du Politecnico · "
                        "Triennale di Milano · MAXXI "
                        "Architettura.",
                },
            ],
            "kpi": [
                ("124", "façades relevées"),
                ("22",  "corniches typologiques"),
                ("192", "pages illustrées"),
                ("200", "exemplaires numérotés"),
            ],
            "lead_partner": "Marta Roveri · Fondatrice",
            "team":         "Architecte + 2 collaborateurs · co-édition DAStU",
            "next_label":   "Fascicule suivant",
        },
    ],

    "contatti": {
        "eyebrow":  "OUVRIR UN FASCICULE PROJET",
        "headline": "La commande commence par une <em>page</em>.",
        "intro":
            "Brief en français ou italien. Site · programme · "
            "calendrier · documents déjà disponibles. Réponse sous "
            "cinq jours ouvrés.",

        "form_label":   "FASCICULE PROJET",
        "form_heading": "Renseignez le fascicule d'ouverture",
        "form_intro":
            "L'agence accepte trois ou quatre nouvelles commandes "
            "par an. La première page de chaque commande est le "
            "fascicule projet : l'agence le lit intégralement, et "
            "y répond sous cinq jours ouvrés par une note "
            "critique. La note critique est gratuite et c'est la "
            "forme par laquelle nous déclarons si la commande est "
            "en ligne avec la collection.",

        "form_fields": [
            {"name": "name",      "label": "Prénom",   "type": "text", "required": True,
             "placeholder": "Ex. Anne",
             "helper": "Uniquement le prénom, merci."},
            {"name": "surname",   "label": "Nom",      "type": "text", "required": True,
             "placeholder": "Ex. Bianchi",
             "helper": "Tel qu'il apparaît dans les documents du maître d'ouvrage."},
            {"name": "email",     "label": "E-mail",   "type": "email", "required": True,
             "placeholder": "anne@domaine.fr",
             "helper": "Une boîte qui recevra la note critique fiduciaire."},
            {"name": "phone",     "label": "Téléphone","type": "tel", "required": False,
             "placeholder": "+33 ...",
             "helper": "Ligne directe pour le premier contact. Facultatif."},
            {"name": "tipologia", "label": "Typologie d'intervention", "type": "select", "required": True,
             "options": [
                 "résidentiel",
                 "public",
                 "intérieur",
                 "paysage",
                 "restauration",
                 "concours",
                 "culturel",
                 "tertiaire",
                 "industriel",
                 "santé",
                 "scolaire",
                 "mixte",
             ],
             "helper": "La typologie de l'intervention envisagée."},
            {"name": "cronoprogramma", "label": "Calendrier souhaité", "type": "select", "required": True,
             "options": [
                 "Moins de 12 mois",
                 "Entre 12 et 24 mois",
                 "Entre 24 et 36 mois",
                 "Plus de 36 mois",
             ],
             "helper": "L'horizon temporel convenu avec le maître d'ouvrage."},
            {"name": "documenti", "label": "Documents déjà disponibles", "type": "select", "required": False,
             "options": [
                 "Relevé · plans",
                 "Contraintes · PLU · Soprintendenza",
                 "Règlement de construction · cahiers des charges",
                 "Concept initial",
                 "Autre",
                 "Aucun (nous commençons par le relevé)",
             ],
             "helper": "Documents déjà disponibles pour le maître d'ouvrage. Facultatif."},
            {"name": "sito", "label": "Le site · l'intervention · la maîtrise d'ouvrage",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Maximum 800 caractères. Indiquez-nous "
                 "brièvement la localisation (Commune · "
                 "province), la typologie de l'intervention et "
                 "la maîtrise d'ouvrage à l'origine de la "
                 "demande. Une seule voix — la complétude n'est "
                 "pas requise.",
             "helper":
                 "De quoi évaluer si le site mérite un relevé. "
                 "Les chiffres et autres données sont discutés "
                 "en première réunion, jamais à l'écrit en "
                 "premier contact."},
        ],

        "form_sections": [
            {"num": "01", "title": "Référent",
             "meta": "La personne qui signera la commande en première réunion.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Argument de projet",
             "meta": "Typologie · calendrier · documents déjà disponibles.",
             "fields": ["tipologia", "cronoprogramma", "documenti"]},
            {"num": "03", "title": "Le site",
             "meta": "Le site est le premier texte du projet. Quatre cents mots suffisent.",
             "fields": ["sito"]},
        ],

        "form_submit_label": "Ouvrir le fascicule",
        "form_submit_note":
            "L'agence lira le fascicule sous cinq jours ouvrés et "
            "répondra par une note critique à l'adresse "
            "indiquée. Aucun BDR externe, aucune automatisation "
            "de séquence — le premier contact se fait avec "
            "l'architecte.",
        "form_consent":
            "Je consens au traitement des données personnelles "
            "au sens du Reg. UE 679/2016 et du D.lgs. "
            "196/2003. Les données sont conservées au siège de "
            "Via Paoli avec accès limité aux trois architectes. "
            "Je suis informé(e) du canal whistleblowing (D.lgs. "
            "24/2023) actif au siège.",

        "office_address_label": "Adresse",
        "office_area_label":    "Quartier",
        "office_phone_label":   "Téléphone",
        "office_email_label":   "E-mail",

        "offices_label":   "LE SIÈGE",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Siège unique",
                "address": "Via Pasquale Paoli 9 · 20143",
                "area":    "Sant'Agostino · proche Bocconi",
                "phone":   "+39 02 6610 4708",
                "email":   "fascicolo@cornice-architettura.it",
            },
        ],

        "channels_label": "CANAUX DIRECTS",
        "channels": [
            ("Secrétariat de l'agence",          "+39 02 6610 4708",                       "Mar – Ven · 10h00 – 18h00"),
            ("E-mail fiduciaire",                "fascicolo@cornice-architettura.it",      "Réponse sous 5 jours ouvrés"),
            ("Whistleblowing (D.lgs. 24/2023)",  "whistleblowing@cornice-architettura.it", "Canal interne · chiffré"),
        ],

        "footnote":
            "Cornice ne répond pas aux demandes anonymes et ne "
            "délivre pas d'avis préliminaires écrits sans "
            "premier dialogue. Les informations sur les "
            "honoraires sont présentées en première réunion, "
            "selon les tarifs minima CNAPPC. Le canal "
            "whistleblowing est géré au sens du D.lgs. 24/2023 "
            "et est ouvert aux maîtres d'ouvrage publics, "
            "fournisseurs de chantier et collaborateurs "
            "externes.",
    },
}
