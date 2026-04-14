"""Chiara — Portfolio Creativo (portfolio / editorial-designer-grid archetype) FR content.

Phase 2i.2 — French locale for the Chiara editorial design studio template,
authored Session 37. Mirrors the exact shape of ``CHIARA_CONTENT_IT`` (same
keys, same nesting, same list arities); only copy is translated into a
classical French editorial design voice (vous, AD-led, typographic).
"""
from __future__ import annotations

from typing import Any


CHIARA_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Studio",        "kind": "home"},
        {"slug": "studio",     "label": "À propos",      "kind": "about"},
        {"slug": "lavoro",     "label": "Travaux",       "kind": "project_list"},
        {"slug": "processo",   "label": "Processus",     "kind": "process"},
        {"slug": "contatti",   "label": "Contact",       "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial":   "C",
        "logo_word":      "Chiara Velluti Studio",
        "logo_short":     "CV",
        "tag":            "Direction artistique · Milan",
        "phone":          "+39 02 8736 4408",
        "email":          "studio@chiaravelluti.it",
        "address":        "Via Tortona 27 · 20144 Milan",
        "hours_compact":  "Lun – Ven · 10h – 19h · sur rendez-vous",
        "license":        "TVA IT 09621460963 · REA MI-2092841",
        "footer_intro":
            "Studio indépendant de direction artistique à Milan. "
            "Identités de marque, systèmes éditoriaux et signalétique "
            "pour institutions culturelles, éditeurs et maisons de "
            "petit luxe. Fondé en 2014.",
        "foot_studio":   "Le studio",
        "foot_pages":    "Sections",
        "foot_contact":  "Contact",
        "foot_clients":  "Ils nous ont fait confiance",
        "clients_footer_rows": [
            "Triennale Milano",
            "Edizioni Adelphi",
            "Fondazione Prada (commande 2022)",
            "Ateliers Velluti & Co.",
        ],
        # Studio coordinates strip — used in footer + ribbon
        "coordinates": [
            ("Studio",      "Via Tortona 27 · 20144 Milan"),
            ("Fondatrice",  "Chiara Velluti, directrice artistique"),
            ("Équipe",      "5 designers · 1 stagiaire · 2 collaborateurs"),
            ("Disciplines", "Identité · Édition · Systèmes graphiques"),
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":   "Studio indépendant · 2014 — 2026",
        # Headline kept short per D-052 to avoid hero overflow
        "headline":  "Des formes qui durent, <em>une page</em> à la fois.",
        "intro":
            "Nous concevons des identités de marque, des livres et des "
            "systèmes graphiques pour des institutions culturelles, des "
            "éditeurs et des maisons de petit luxe. Le studio est conduit "
            "par la direction artistique et chaque projet est suivi "
            "personnellement, de l'ouverture du dossier à la remise des "
            "chartes.",
        "primary_cta":   "Demander le portfolio complet",
        "primary_href":  "contatti",
        "secondary_cta": "Visiter le studio",
        "secondary_href":"studio",

        # Hero ledger card footer label + count format (lifted from skin)
        "ledger_full_link_label":   "Tout l'archive",
        "ledger_count_prefix":      "→",
        "ledger_count_unit":        "projets",

        # Project ledger preview — 6 indexed rows
        "ledger_label":   "Travaux choisis · 2022 — 2026",
        "ledger_heading": "Six projets, six disciplines",
        "ledger_intro":
            "Une sélection récente. L'archive complète compte 47 projets "
            "signés depuis 2014. La liste intégrale est disponible sous "
            "forme de PDF de consultation, sur simple demande.",
        # Each row: (num, title, discipline, year, medium)
        "ledger_rows": [
            ("01", "Triennale Milano · catalogue 2025",
             "Édition d'art", "2025",
             "Volume 24 × 32 cm · 412 pages · impression offset"),
            ("02", "Adelphi · collection « Carta Bianca »",
             "Identité de collection", "2024",
             "Système typographique + 12 couvertures en série"),
            ("03", "Fondazione Querini Stampalia · signalétique",
             "Signalétique & wayfinding", "2024",
             "Système bilingue · laiton gravé + impression directe"),
            ("04", "Maison Lambrate · refonte d'identité",
             "Identité de marque", "2023",
             "Logotype + système visuel + charte 96 pages"),
            ("05", "Festival de Pordenone · 38ᵉ édition",
             "Identité d'événement", "2023",
             "Marque temporaire + supports imprimés + signalétique"),
            ("06", "Atelier Velluti & Co. · monographie",
             "Édition de studio", "2022",
             "Volume 19 × 25 cm · 240 pages · impression fine art"),
        ],

        # Capabilities preview (full list on /processo)
        "capabilities_label":   "Disciplines",
        "capabilities_heading": "Cinq compétences, une seule signature",
        "capabilities_intro":
            "Chaque projet est suivi par une équipe pluridisciplinaire. "
            "Nous n'ajustons pas notre échelle à la taille du client — "
            "nous l'ajustons à la complexité du problème.",
        "capabilities": [
            ("Identité de marque",
             "Identités complètes pour institutions et maisons : de la "
             "recherche typographique aux chartes opérationnelles."),
            ("Édition & livres",
             "Catalogues d'art, monographies d'auteur, collections "
             "éditoriales. Direction typographique et mise en page."),
            ("Systèmes & wayfinding",
             "Signalétique, systèmes graphiques pour espaces "
             "d'exposition, wayfinding bilingue et matériel "
             "didactique muséal."),
            ("Direction artistique",
             "Conseil en direction artistique pour services intégrés : "
             "revue de chartes, audits visuels, mentorat de l'équipe "
             "graphique."),
        ],

        # Selected clients ribbon (text-only wordmarks)
        "clients_label":   "Ils nous ont fait confiance",
        "clients": [
            "TRIENNALE MILANO",
            "ADELPHI EDIZIONI",
            "FONDAZIONE PRADA",
            "MUSEO POLDI PEZZOLI",
            "QUERINI STAMPALIA",
            "FESTIVAL PORDENONE",
            "MAISON LAMBRATE",
            "ATELIER VELLUTI & CO.",
        ],

        # Featured projects — visual grid below the typo hero. Lightbox-enabled,
        # 4 cards with project image, year, discipline. Reads as a designer's
        # opening reel without breaking the typographic editorial identity.
        "featured_works": {
            "label":   "Travaux au catalogue",
            "heading": "Quatre projets, <em>quatre disciplines.</em>",
            "intro":
                "Une sélection 2024 — 2025 — systèmes typographiques, "
                "identités institutionnelles, signalétique muséale, "
                "objets éditoriaux imprimés. Cliquer pour ouvrir le "
                "dossier complet.",
            "items": [
                {
                    "year":       "2025",
                    "discipline": "Catalogue · Édition d'art",
                    "title":      "Triennale Milano 2025",
                    "blurb":      "Direction typographique et mise en page du catalogue principal de l'édition.",
                    "image":      "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2024 — 2025",
                    "discipline": "Système typographique · Édition",
                    "title":      "Collection « Carta Bianca » · Adelphi",
                    "blurb":      "Système éditorial pour douze titres — couvertures, typographie, code chromatique.",
                    "image":      "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2024",
                    "discipline": "Signalétique · Identité muséale",
                    "title":      "Querini Stampalia · Venise",
                    "blurb":      "Signalétique permanente des salles + système d'appel pour les salles de conférence.",
                    "image":      "https://images.unsplash.com/photo-1564399579883-451a5d44ec08?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2023",
                    "discipline": "Monographie · Édition indépendante",
                    "title":      "Atelier Velluti · Lambrate",
                    "blurb":      "Monographie de studio — 240 pages, système typographique sur mesure, impression Antiga.",
                    "image":      "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
            ],
            "footer_link":  "Voir tous les projets",
            "footer_href":  "lavoro",
        },

        # Press / recognitions — 3 honors
        "press_label":   "Distinctions récentes",
        "press_heading": "Prix, expositions et publications",
        "press": [
            {
                "year":  "2025",
                "honor": "ADI Design Index",
                "work":  "Catalogue Triennale Milano 2025",
                "note":  "Sélection édition d'art · jury national.",
            },
            {
                "year":  "2024",
                "honor": "European Design Awards · Bronze",
                "work":  "Collection « Carta Bianca » pour Adelphi",
                "note":  "Catégorie systèmes typographiques éditoriaux.",
            },
            {
                "year":  "2023",
                "honor": "Aiap Design Per · exposition collective",
                "work":  "Monographie Atelier Velluti & Co.",
                "note":  "Présentée à la Triennale pendant quatre mois.",
            },
        ],

        # Selected commissions — what we accept this year
        "commissions_label":   "Commandes 2026",
        "commissions_heading": "Ce que nous cherchons cette année",
        "commissions_intro":
            "Le studio accepte huit à dix projets par an, choisis pour "
            "leur complexité plutôt que pour la taille du client. "
            "Choisir le travail est la discipline la plus importante "
            "que nous exercions.",
        "commissions": [
            ("Identités pour institutions culturelles",
             "Musées, fondations, festivals. Nous préférons les "
             "mandats de refonte structurelle aux simples mises à jour."),
            ("Catalogues d'art et monographies",
             "Éditeurs d'art indépendants, galeries dotées d'un "
             "programme éditorial, monographies d'auteur."),
            ("Systèmes graphiques pour espaces",
             "Signalétique muséale, wayfinding bilingue, systèmes "
             "didactiques pour expositions temporaires."),
        ],

        # Final CTA band
        "cta_label":   "Une conversation préliminaire",
        "cta_heading": "Trente minutes avec la direction artistique, sans engagement",
        "cta_intro":
            "Le premier échange a lieu directement avec Chiara Velluti. "
            "Nous discutons du périmètre, du calendrier et d'un "
            "éventuel conflit d'agenda — avant toute proposition.",
        "cta_primary":      "Écrire au studio",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Parcourir les travaux",
        "cta_secondary_href":"lavoro",
    },

    # ─── STUDIO (about) ─────────────────────────────────────────
    "studio": {
        "eyebrow":   "Le studio · 2014 — 2026",
        "headline":  "Un studio conduit par la <em>direction artistique</em>, douze années de travail.",
        "intro":
            "Chiara Velluti Studio naît en 2014 à Milan, dans un premier "
            "espace de trente-quatre mètres carrés à Lambrate. "
            "Aujourd'hui, nous sommes cinq designers, deux collaborateurs "
            "extérieurs et une stagiaire, via Tortona. Nous continuons à "
            "choisir un par un nos projets.",

        # Founder block (full bio)
        "founder_label":   "Direction artistique",
        "founder_heading": "Chiara Velluti, fondatrice",
        "founder": {
            "name":  "Chiara Velluti",
            "role":  "Directrice artistique · fondatrice",
            "bio":
                "Diplômée en design graphique à l'Isia Urbino, trois "
                "années chez Pentagram New York comme senior designer "
                "(auprès de Paula Scher), cinq années chez Studio "
                "Sonnoli à Rimini comme associée. Ouvre le studio "
                "Velluti en 2014 à Milan. Enseigne la conception "
                "typographique au Politecnico depuis 2018, membre "
                "de l'Aiap depuis 2010, et dirige la collection "
                "éditoriale « Carta Bianca » pour Adelphi depuis 2024.",
            "credentials": [
                "Isia Urbino · design graphique, promotion 2006",
                "Pentagram New York · senior 2007—2010",
                "Studio Sonnoli Rimini · associée 2010—2014",
                "Politecnico Milano · enseignante en conception typographique",
                "Aiap · membre titulaire depuis 2010",
                "ADI · jurée Design Index 2024",
            ],
            "image": "https://images.unsplash.com/photo-1544717305-2782549b5136?w=1200&q=80&auto=format&fit=crop",
        },

        # Studio team (full team — 4 collaborators beyond founder)
        "team_label":   "Équipe du studio",
        "team_heading": "Cinq designers, deux collaborateurs extérieurs",
        "team_intro":
            "Nous travaillons dans un plateau ouvert unique — pas de "
            "bureaux séparés. Chaque projet dispose d'une équipe "
            "dédiée de trois personnes, conduite par la direction "
            "artistique. Les collaborateurs extérieurs n'interviennent "
            "que sur la typographie originale et la mise en page au "
            "long cours.",
        "team": [
            {"name": "Marco Salvioli",
             "role": "Senior designer · édition",
             "bio":
                "Cinq années chez Tassinari/Vetta à Trieste avant "
                "de rejoindre le studio en 2019. Coordonne les "
                "projets éditoriaux et les chartes typographiques."},
            {"name": "Anna Brambilla",
             "role": "Designer · identité de marque",
             "bio":
                "Naba Milan, promotion 2017, deux années chez Studio "
                "Mut à Bolzano. S'occupe de refontes de studio et de "
                "maisons de petit luxe, de la recherche au manuel "
                "opérationnel."},
            {"name": "Lorenzo Tagliabue",
             "role": "Designer · systèmes & wayfinding",
             "bio":
                "Politecnico Milano, promotion 2019, stage à l'Atelier "
                "Carvalho Bernau à Berlin. Responsable des systèmes "
                "signalétiques et des supports pour espaces "
                "d'exposition."},
            {"name": "Sara Pellegrini",
             "role": "Designer · numérique",
             "bio":
                "Iuav Venise, promotion 2020, deux années chez "
                "Cantiere Creativo à Florence. Étend les identités "
                "aux systèmes numériques (sites, applications, "
                "supports animés)."},
            {"name": "Filippo Vigorelli",
             "role": "Collaborateur · dessin typographique",
             "bio":
                "Type designer indépendant, formé à Type@Cooper "
                "New York. Collabore aux caractères sur mesure du "
                "studio depuis 2017."},
            {"name": "Beatrice Fornaro",
             "role": "Stagiaire · 2026",
             "bio":
                "Dernière année à l'Isia Urbino. Accompagne la "
                "pratique éditoriale et contribue à l'archive des "
                "projets passés."},
        ],

        # Studio principles — 4 design notes
        "principles_label":   "Principes de studio",
        "principles_heading": "Quatre règles <em>non négociables</em>",
        "principles_intro":
            "Ce sont les quatre règles qui séparent un projet signé "
            "Velluti d'une exécution de studio standard. Vous les "
            "trouverez dans le manuel interne de 2018, jamais révisé.",
        "principles": [
            ("01", "Une seule voix, du début à la fin",
             "La direction artistique entre en première réunion et "
             "signe la livraison. Pas de transmission à un junior "
             "après le pitch — la personne que vous rencontrez en "
             "réunion d'ouverture est la même qui signe les chartes "
             "finales."),
            ("02", "La typographie avant la marque",
             "Dans chaque projet, le choix des caractères précède le "
             "dessin du logo. Les identités que nous proposons "
             "naissent d'une grammaire typographique, et non d'un "
             "symbole décoratif."),
            ("03", "Pas de moodboard Pinterest",
             "Les références que nous proposons proviennent de notre "
             "bibliothèque de studio, des archives des institutions "
             "avec lesquelles nous travaillons, et de visites "
             "d'expositions en personne. Jamais d'images "
             "téléchargées."),
            ("04", "Les chartes sont un livre",
             "Chaque identité se clôt sur un manuel opérationnel "
             "imprimé — pas un PDF, un volume de cent-vingt à deux "
             "cents pages. Il reste dans la bibliothèque du client, "
             "pas dans un dossier serveur."),
        ],

        # Press band — full press list (extended from home)
        "press_label":   "Prix, expositions, publications",
        "press_heading": "Sélection 2020 — 2026",
        "press_full": [
            ("2025", "ADI Design Index",
             "Sélection édition d'art", "Catalogue Triennale 2025"),
            ("2024", "European Design Awards · Bronze",
             "Systèmes typographiques éditoriaux", "Collection « Carta Bianca »"),
            ("2024", "Brand New (Under Consideration)",
             "Recension critique", "Refonte Maison Lambrate"),
            ("2023", "Aiap Design Per · exposition collective",
             "Édition d'auteur", "Monographie Velluti & Co."),
            ("2023", "Type Directors Club New York · Honor",
             "Dessin typographique", "Caractère sur mesure Querini"),
            ("2022", "Eye Magazine n° 102",
             "Essai illustré de huit pages", "Identité Velluti Studio"),
            ("2021", "ADI Compasso d'Oro · mention",
             "Catégorie communication visuelle", "Système Triennale 2021"),
            ("2020", "Brno Biennial Czechia · sélection",
             "Identités muséales", "Festival Pordenone 36ᵉ"),
        ],

        # Final CTA — visit the studio
        "cta_heading":      "Visiter le studio",
        "cta_intro":
            "Le studio se trouve via Tortona 27, entrée par la cour "
            "intérieure. La bibliothèque est ouverte sur rendez-vous — "
            "écrivez-nous deux lignes et nous fixerons une matinée.",
        "cta_primary":      "Fixer une visite",
        "cta_primary_href": "contatti",
    },

    # ─── LAVORO (project_list) ──────────────────────────────────
    "lavoro": {
        "eyebrow":   "Archive des projets · 2014 — 2026",
        "headline":  "Quarante-sept projets signés, <em>six disciplines</em>.",
        "intro":
            "L'archive complète des projets du studio. La sélection "
            "présentée ici couvre les six mandats les plus récents "
            "pour chaque discipline. Pour le PDF intégral du "
            "portfolio (96 pages, tous les projets signés depuis "
            "2014), écrivez à studio@chiaravelluti.it.",

        # Discipline filter pills
        "filter_label": "Disciplines",
        "filters": [
            "Toutes",
            "Édition d'art",
            "Identité de marque",
            "Systèmes & wayfinding",
            "Identité d'événement",
            "Direction artistique",
        ],

        # Ledger row labels (lifted from skin for i18n)
        "row_discipline_label": "Discipline",
        "row_duration_label":   "Durée",
        "row_year_label":       "Année",

        # Index intro band on top of the ledger
        "ledger_label": "Index chronologique",
        "ledger_intro":
            "Parcourir du haut vers le bas pour l'ordre "
            "antéchronologique. Cliquer sur une ligne pour ouvrir "
            "le dossier complet du projet.",

        # CTA before footer
        "cta_label":   "Vous cherchez quelque chose de précis ?",
        "cta_heading": "Sur demande, nous envoyons des dossiers par discipline",
        "cta_intro":
            "Si vous évaluez le studio pour un mandat particulier, "
            "indiquez-nous la discipline et nous vous envoyons sous "
            "48 heures trois dossiers pertinents — format A4, "
            "imprimés pour la présentation interne.",
        "cta_primary":      "Écrivez-nous",
        "cta_primary_href": "contatti",

        # Dossier (project_detail) labels — constants across all posts,
        # localized via the `lavoro` page_data block.
        "dossier_meta_discipline_label": "Discipline",
        "dossier_meta_year_label":       "Année",
        "dossier_meta_duration_label":   "Durée",
        "dossier_meta_team_label":       "Équipe",
        "dossier_summary_label":         "Synthèse du projet",
        "dossier_deliverables_label":    "Livrables remis",
        "dossier_deliverables_heading":  "Ce que nous avons produit",
        "dossier_colophon_label":        "Colophon",
    },

    # ─── PROCESSO (process) ─────────────────────────────────────
    "processo": {
        "eyebrow":   "Comment nous travaillons · méthode de studio",
        "headline":  "Cinq étapes, <em>un seul dossier</em> par projet.",
        "intro":
            "La méthode du studio est écrite, partagée avec le client "
            "lors de la première réunion et suivie sans exception. "
            "Chaque projet a son propre dossier physique — chemise "
            "verte numérotée, étiquette typographique, conservée en "
            "archive pour vingt ans au minimum.",

        # Process step + capability labels (lifted from skin for i18n)
        "step_sequence_label":       "Séquence",
        "step_index_prefix":         "Étape",
        "step_index_separator":      "sur",
        "capability_duration_label": "Durée indicative",

        # 5-step process (richer than business)
        "process_label":   "Séquence de studio",
        "process_heading": "Ouverture, recherche, proposition, construction, livraison",
        "process": [
            ("01", "Ouverture du dossier",
             "Premier échange avec la direction artistique "
             "(45 minutes, gratuit). On y discute du périmètre, "
             "des attentes du client, d'un éventuel conflit "
             "d'agenda. Sous cinq jours, une proposition écrite "
             "de trois pages : périmètre, livrables, calendrier, "
             "barème.",
             "Livrable", "Proposition écrite · 3 pages"),
            ("02", "Recherche préliminaire",
             "Quatre à six semaines de recherche : visite des "
             "archives du client, bibliothèque de studio, "
             "références historiques et contemporaines. Jamais de "
             "moodboard Pinterest. Se clôt par un brief illustré "
             "partagé avec le client.",
             "Durée", "4 — 6 semaines"),
            ("03", "Proposition de direction",
             "Une seule direction est présentée, pas trois. La "
             "présentation se fait en personne, au studio ou chez "
             "le client, jamais par e-mail. Le client peut "
             "accepter, demander des révisions circonscrites "
             "(deux cycles au maximum) ou interrompre le mandat "
             "(clause de sortie prévue au contrat).",
             "Durée", "2 — 3 semaines de conception + présentation"),
            ("04", "Construction du système",
             "La direction validée est déclinée en un système "
             "complet : typographie, palette, grille, marques, "
             "supports, applications. Pour les identités "
             "complètes : dix à seize semaines. L'équipe dédiée "
             "travaille à huis clos, avec deux points "
             "intermédiaires mensuels avec le client.",
             "Durée", "10 — 16 semaines selon le périmètre"),
            ("05", "Livraison et manuel imprimé",
             "Chaque projet se clôt sur un manuel opérationnel "
             "imprimé — 120 à 240 pages, format A4, impression "
             "offset noir et blanc. Un exemplaire pour le client, "
             "un pour la bibliothèque du studio. Six mois "
             "d'accompagnement inclus sur l'application des "
             "chartes.",
             "Livrable", "Manuel imprimé + accompagnement 6 mois"),
        ],

        # Capabilities — full list (extended from home)
        "capabilities_label":   "Disciplines complètes",
        "capabilities_heading": "Ce que nous concevons",
        "capabilities_intro":
            "Les disciplines que nous exerçons régulièrement. Nous ne "
            "travaillons pas en publicité above-the-line, packaging "
            "FMCG, motion design de plus de 30 secondes, ni sur "
            "templates recolorisables.",
        "capabilities_full": [
            {
                "num": "01",
                "title": "Identité de marque",
                "blurb":
                    "Identités complètes pour institutions culturelles "
                    "et maisons de petit luxe. Marque + système "
                    "typographique + palette + grille + manuel "
                    "opérationnel imprimé.",
                "scope": [
                    "Naming et recherche typographique",
                    "Dessin de la marque et variantes",
                    "Système visuel + grille",
                    "Manuel opérationnel (120 — 240 pp.)",
                ],
                "duration": "16 — 24 semaines pour une identité complète",
            },
            {
                "num": "02",
                "title": "Édition d'art",
                "blurb":
                    "Catalogues d'art, monographies d'auteur, "
                    "collections éditoriales. Direction typographique, "
                    "mise en page, choix du papier, suivi en "
                    "imprimerie.",
                "scope": [
                    "Direction typographique",
                    "Mise en page et grille éditoriale",
                    "Choix du papier + recherche typographique",
                    "Suivi d'impression (visite de l'imprimerie)",
                ],
                "duration": "12 — 32 semaines pour un volume unique",
            },
            {
                "num": "03",
                "title": "Systèmes & wayfinding",
                "blurb":
                    "Signalétique muséale, systèmes graphiques pour "
                    "espaces d'exposition, wayfinding bilingue, "
                    "supports didactiques pour expositions "
                    "temporaires.",
                "scope": [
                    "Audit de l'espace existant",
                    "Système bilingue / trilingue",
                    "Dessin de la signalétique",
                    "Direction de production (gravure / impression)",
                ],
                "duration": "10 — 18 semaines pour un espace muséal",
            },
            {
                "num": "04",
                "title": "Identité d'événement",
                "blurb":
                    "Marques temporaires pour festivals, biennales, "
                    "éditions limitées. Supports imprimés, "
                    "signalétique pour le lieu, système numérique.",
                "scope": [
                    "Marque temporaire + variante annuelle",
                    "Système imprimé (affiches, brochures, billets)",
                    "Signalétique pour le lieu",
                    "Système numérique (site + supports animés)",
                ],
                "duration": "8 — 14 semaines par édition",
            },
            {
                "num": "05",
                "title": "Direction artistique",
                "blurb":
                    "Conseil en direction artistique pour services "
                    "intégrés : revue des chartes existantes, audits "
                    "visuels, mentorat de l'équipe graphique interne, "
                    "formation typographique.",
                "scope": [
                    "Audit visuel de l'existant",
                    "Revue des chartes",
                    "Mentorat de l'équipe graphique (1 jour / mois)",
                    "Atelier typographique (formation)",
                ],
                "duration": "Mandat annuel, renouvelable",
            },
        ],

        # Final CTA before footer
        "cta_heading":      "Quelle discipline vous convient ?",
        "cta_intro":
            "Si le périmètre n'est pas encore net, écrivez-nous deux "
            "lignes de contexte. Nous vous répondons avec la "
            "discipline juste sous 48 heures — même si ce n'est pas "
            "le studio Velluti qui vous accompagnera.",
        "cta_primary":      "Écrivez-nous",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI (contact) ─────────────────────────────────────
    "contatti": {
        "eyebrow":   "Une conversation préliminaire",
        "headline":  "Trente minutes avec la direction artistique, <em>sans engagement</em>.",
        "intro":
            "Le premier contact a lieu directement avec Chiara Velluti, "
            "directrice artistique et fondatrice. Nous discutons du "
            "périmètre du projet, du calendrier et d'un éventuel "
            "conflit d'agenda — avant toute proposition écrite.",

        # Studio info side card
        "studio_label":          "Le studio",
        "studio_address":        "Via Tortona 27 · 20144 Milan",
        "studio_area":           "Entrée par la cour intérieure · sonnette « Velluti »",
        "studio_metro":          "MM2 Porta Genova · 4 minutes à pied",
        "studio_hours":          "Lun – Ven · 10h – 19h · sur rendez-vous",
        # Studio card row labels (lifted from skin for i18n)
        "studio_address_label":  "Adresse",
        "studio_area_label":     "Entrée",
        "studio_metro_label":    "Métro",
        "studio_hours_label":    "Horaires",

        # Form fields — generic loop in chrome
        "form_label":   "Demander un premier échange",
        "form_heading": "Remplir le formulaire",
        "form_intro":
            "Vous recevrez une confirmation sous 48 heures ouvrées. "
            "Les échanges ont lieu le mardi et le jeudi après-midi, "
            "à huis clos, avec la direction artistique.",
        "form_fields": [
            {"name": "name",      "label": "Prénom",        "type": "text",     "required": True,  "placeholder": "Ex. Chiara",
             "helper": "Prénom uniquement, merci."},
            {"name": "surname",   "label": "Nom",           "type": "text",     "required": True,  "placeholder": "Ex. Velluti",
             "helper": "Tel qu'il figure sur votre carte de visite."},
            {"name": "organization", "label": "Organisation", "type": "text",   "required": True,  "placeholder": "Ex. Triennale Milano",
             "helper": "Institution, maison d'édition ou maison."},
            {"name": "role",      "label": "Fonction",      "type": "text",     "required": True,  "placeholder": "Ex. Directrice éditoriale",
             "helper": "Poste de la personne qui suivra le projet."},
            {"name": "email",     "label": "E-mail",        "type": "email",    "required": True,  "placeholder": "chiara.velluti@triennale.org",
             "helper": "De préférence une adresse institutionnelle."},
            {"name": "phone",     "label": "Téléphone",     "type": "tel",      "required": False, "placeholder": "+33 ...",
             "helper": "Ligne directe · uniquement si vous préférez être rappelé."},
            {"name": "discipline", "label": "Discipline souhaitée", "type": "select", "required": True,
             "options": [
                 "À définir lors de l'appel",
                 "Identité de marque",
                 "Édition d'art",
                 "Systèmes & wayfinding",
                 "Identité d'événement",
                 "Direction artistique",
             ],
             "helper": "Choisissez « à définir » si le périmètre "
                       "touche plusieurs disciplines."},
            {"name": "horizon",   "label": "Horizon temporel", "type": "select", "required": True,
             "options": [
                 "Démarrage sous un mois",
                 "Démarrage sous trois mois",
                 "Démarrage sous six mois",
                 "Exploratoire · sans urgence",
             ],
             "helper": "Aide à caler le premier échange avec la "
                       "direction artistique."},
            {"name": "brief",     "label": "Brève description du projet", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Au maximum 800 caractères. Aucun nom "
                            "de contrepartie — ils ne seront discutés "
                            "qu'après NDA réciproque, si nécessaire.",
             "helper": "De quoi comprendre si le projet relève de "
                       "notre compétence."},
        ],

        "form_sections": [
            {"num": "01", "title": "Référent",
             "meta": "La personne qui suivra le projet côté client.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Organisation",
             "meta": "Pour le conflict-check préliminaire avec "
                     "d'autres projets en cours.",
             "fields": ["organization", "role"]},
            {"num": "03", "title": "Périmètre du projet",
             "meta": "Une description synthétique — les pièces "
                     "jointes viennent au second échange, après NDA.",
             "fields": ["discipline", "horizon", "brief"]},
            {"num": "04", "title": "Pièces jointes (facultatif)",
             "meta": "Brief interne, dossier institutionnel, "
                     "recherche préliminaire. Ils peuvent anticiper "
                     "le premier échange.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "brief_allegato",
            "label":    "Documents préliminaires",
            "helper":   "Brief interne, dossier institutionnel, images "
                        "de référence. PDF / DOCX / JPG · 20 Mo max "
                        "au total.",
            "accept":   ".pdf,.docx,.jpg,.jpeg,.png",
            "multiple": True,
            "primary":  "Déposez vos documents ici ou",
            "link":     "parcourir l'archive",
            "meta":     "PDF / DOCX / JPG · 20 Mo max",
        },

        "form_submit_label": "Envoyer la demande",
        "form_submit_note":
            "Confirmation directement par la direction artistique "
            "sous 48 heures ouvrées. Aucun account manager externe, "
            "aucune automatisation de leads.",
        "form_consent":
            "Je consens au traitement de mes données personnelles "
            "au sens du Règlement UE 679/2016. Les demandes sont "
            "lues et archivées uniquement par la directrice "
            "artistique — aucun tiers n'est impliqué.",

        # Channels strip
        "channels_label": "Canaux directs",
        "channels": [
            ("E-mail studio",      "studio@chiaravelluti.it",    "Réponse sous 48 heures ouvrées"),
            ("Standard",           "+39 02 8736 4408",           "Lun – Ven · 10h – 19h"),
            ("Visite au studio",   "Via Tortona 27 · Milan",     "Sur rendez-vous, jamais à l'improviste"),
        ],

        "footnote":
            "Le studio ne répond pas aux demandes anonymes et ne "
            "délivre pas de devis par e-mail sans un premier "
            "échange. Les tarifs et les conditions économiques "
            "sont présentés dans la proposition écrite, jamais par "
            "message.",
    },

    # ─── POSTS — drives /lavoro/<slug>/ project_detail ──────────
    "posts": [
        {
            "slug":        "triennale-milano-catalogo-2025",
            "title":       "Triennale Milano · catalogue 2025",
            "category":    "Édition d'art",
            "year":        "2025",
            "duration":    "32 semaines",
            "client_code": "Triennale Milano · catalogue de la 24ᵉ édition · 412 pages offset",
            "lead":
                "Direction typographique et mise en page du catalogue "
                "officiel de la 24ᵉ Triennale de Milan. Volume de "
                "412 pages, 24 × 32 cm, impression offset en cinq "
                "couleurs sur papier non couché 130 g/m² Fedrigoni "
                "Arena.",
            "summary": [
                "Direction typographique et mise en page",
                "Système de grille variable pour 87 contributions",
                "Dessin sur mesure des lettrines capitales",
                "Suivi en imprimerie · 4 visites · 12 jours",
            ],
            "discipline":  "Édition d'art",
            "team":        "Direction artistique + 2 seniors · 32 semaines",
            "deliverables":[
                "Volume 412 pp. · 24 × 32 cm · impression offset",
                "Système de grille variable pour essais et notices",
                "Caractère sur mesure Triennale Display (12 glyphes capitaux)",
                "Manuel de rédaction interne · 48 pp.",
            ],
            "credits": [
                ("Client",                "Triennale Milano"),
                ("Direction éditoriale",  "Maria Sebregondi"),
                ("Impression",            "Grafiche Antiga · Trévise"),
                ("Papier",                "Fedrigoni Arena Natural Smooth 130 g/m²"),
                ("Reliure",               "Dos carré collé cousu fil · carton 350 g/m²"),
                ("Tirage",                "3 200 exemplaires · seconde réimpression en juin 2025"),
            ],
            "sections": [
                {
                    "label": "Le projet",
                    "heading": "Quatre-cent-douze pages, quatre-vingt-sept auteurs",
                    "body":
                        "Le catalogue de la 24ᵉ Triennale documente une "
                        "exposition de mille mètres carrés sur huit "
                        "salles, avec quatre-vingt-sept contributions "
                        "entre essais critiques, notices d'œuvres et "
                        "appareils documentaires. Le problème de "
                        "conception consistait à construire un système "
                        "de grille capable d'accueillir des textes de "
                        "longueur très différente (de 200 à 12 000 mots) "
                        "tout en préservant une lecture éditoriale "
                        "unifiée.",
                },
                {
                    "label": "La direction typographique",
                    "heading": "Trois familles, une seule voix",
                    "body":
                        "Nous avons construit le système sur trois "
                        "familles typographiques complémentaires — une "
                        "transitionnelle avec empattements (Lyon Text) "
                        "pour les corps de texte, un grotesque "
                        "géométrique (GT Walsheim) pour les titres et "
                        "un monospace (JetBrains Mono) pour les "
                        "appareils documentaires. Les trois familles "
                        "coexistent sur une grille de neuf colonnes "
                        "capable de s'articuler en formats différents "
                        "sans rompre la reconnaissance.",
                },
                {
                    "label": "L'exécution",
                    "heading": "Trente-deux semaines, quatre visites en imprimerie",
                    "body":
                        "Le volume a été mis en page en trente-deux "
                        "semaines par une équipe de trois designers du "
                        "studio, avec supervision hebdomadaire de la "
                        "direction artistique. Quatre visites à "
                        "l'imprimerie de Trévise entre juillet et "
                        "septembre 2025 ont permis de calibrer "
                        "l'impression directement sur machine — la "
                        "couverture a été refaite deux fois pour "
                        "atteindre le noir plein recherché sans "
                        "reflets.",
                },
            ],
            "next_label": "Mandat suivant",
        },
        {
            "slug":        "adelphi-collana-carta-bianca",
            "title":       "Adelphi · collection « Carta Bianca »",
            "category":    "Identité de collection",
            "year":        "2024",
            "duration":    "44 semaines",
            "client_code": "Adelphi Edizioni · collection éditoriale · 12 titres par an",
            "lead":
                "Système visuel et couvertures d'une nouvelle "
                "collection d'essais de philosophie contemporaine "
                "pour Adelphi. Douze titres par an, format 14 × 22 cm, "
                "dos carré collé cousu sur papier non couché.",
            "summary": [
                "Direction de collection + système typographique",
                "12 couvertures en série · dessin sur mesure",
                "Système de couleur par année éditoriale",
                "Manuel de rédaction typographique",
            ],
            "discipline":  "Identité de collection",
            "team":        "Direction artistique + senior édition · 44 semaines",
            "deliverables":[
                "Système visuel de la collection · 36 pages",
                "12 couvertures en série · dessin par titre",
                "Caractère sur mesure Adelphi Sans (pour la collection)",
                "Manuel de rédaction typographique · 64 pp.",
            ],
            "credits": [
                ("Client",                 "Adelphi Edizioni"),
                ("Direction de collection","Roberto Calasso (à titre posthume) · Aldo Schiavone"),
                ("Papier",                 "Munken Pure Smooth 100 g/m²"),
                ("Impression",             "Tipografia Mariani · Bergame"),
                ("Reliure",                "Dos carré collé cousu fil"),
                ("Tirage",                 "2 000 — 4 500 exemplaires par titre"),
            ],
            "sections": [
                {
                    "label": "Le projet",
                    "heading": "Une nouvelle collection pour Adelphi",
                    "body":
                        "Adelphi recherche un système visuel pour "
                        "« Carta Bianca », une collection d'essais "
                        "philosophiques destinée à accueillir les voix "
                        "jeunes de la philosophie européenne "
                        "contemporaine. Douze titres par an, profil "
                        "éditorial délibérément expérimental, mais la "
                        "marque Adelphi doit être honorée.",
                },
                {
                    "label": "L'idée",
                    "heading": "Une seule architecture, douze déclinaisons",
                    "body":
                        "Le système est bâti sur une architecture "
                        "typographique unique — le titre travaillé dans "
                        "un caractère sur mesure (Adelphi Sans, dessiné "
                        "en collaboration avec Filippo Vigorelli), "
                        "composé à pleine page sur fond monochrome. "
                        "Chaque année éditoriale introduit une palette "
                        "de six couleurs, chaque titre est imprimé dans "
                        "deux couleurs de la palette annuelle. La "
                        "reconnaissance naît du système, et non de la "
                        "décoration.",
                },
                {
                    "label": "L'exécution",
                    "heading": "Quarante-quatre semaines, douze couvertures",
                    "body":
                        "Le système a été livré en juillet 2024, les "
                        "quatre premières couvertures en septembre, les "
                        "huit autres à cadence trimestrielle jusqu'en "
                        "juillet 2025. La direction éditoriale, assurée "
                        "par Aldo Schiavone, approuve personnellement "
                        "chaque couverture avant impression. Le studio "
                        "a également conduit la formation de la "
                        "rédaction interne à l'usage du manuel.",
                },
            ],
            "next_label": "Projet suivant",
        },
        {
            "slug":        "querini-stampalia-segnaletica",
            "title":       "Fondazione Querini Stampalia · signalétique",
            "category":    "Signalétique & wayfinding",
            "year":        "2024",
            "duration":    "26 semaines",
            "client_code": "Fondazione Querini Stampalia · système bilingue ITA / ENG",
            "lead":
                "Système signalétique bilingue pour la Fondazione "
                "Querini Stampalia de Venise. Trois étages, "
                "musée + bibliothèque + espace Carlo Scarpa. Laiton "
                "gravé et impression directe sur panneaux "
                "interchangeables.",
            "summary": [
                "Audit de l'espace existant · 2 semaines",
                "Système bilingue ITA / ENG · grammaire unifiée",
                "Dessin du caractère sur mesure Querini Sans (96 glyphes)",
                "Direction de production · laiton gravé + impression directe",
            ],
            "discipline":  "Systèmes & wayfinding",
            "team":        "Direction artistique + senior wayfinding · 26 semaines",
            "deliverables":[
                "Système signalétique complet · 142 éléments",
                "Caractère sur mesure Querini Sans · 96 glyphes · 3 graisses",
                "Manuel opérationnel · 88 pages",
                "Direction de production jusqu'à la réception",
            ],
            "credits": [
                ("Client",              "Fondazione Querini Stampalia, Venise"),
                ("Direction",           "Marigusta Lazzari, directrice"),
                ("Architecture",        "Studio Carlo Scarpa (1961—63 · œuvre originale)"),
                ("Production laiton",   "Bottega Pasinetti · Murano"),
                ("Impression directe",  "Tipografia Adriatica · Mestre"),
                ("Réception",           "Septembre 2024 · 142 éléments installés"),
            ],
            "sections": [
                {
                    "label": "Le problème",
                    "heading": "Une signalétique née par additions successives",
                    "body":
                        "La signalétique de la Fondazione s'était "
                        "stratifiée en cinq cycles successifs (des "
                        "années soixante à une révision de 2009), avec "
                        "des matériaux, des caractères et des logiques "
                        "de positionnement différents. Le résultat "
                        "était illisible, mais le vrai problème "
                        "consistait à respecter l'architecture de "
                        "Carlo Scarpa au rez-de-chaussée — un espace "
                        "qui ne tolère pas les surimpositions "
                        "graphiques lourdes.",
                },
                {
                    "label": "L'approche",
                    "heading": "Une grammaire, deux matériaux",
                    "body":
                        "Nous avons construit une grammaire unifiée "
                        "en deux matériaux : laiton gravé au bain "
                        "(pour la signalétique permanente, en dialogue "
                        "avec le laiton Scarpa du rez-de-chaussée) et "
                        "impression directe sur panneaux aluminium "
                        "interchangeables (pour la signalétique "
                        "d'exposition, remplaçable à chaque "
                        "accrochage). Le caractère sur mesure "
                        "Querini Sans reprend les proportions des "
                        "stèles épigraphiques vénètes du seizième "
                        "siècle.",
                },
                {
                    "label": "Le résultat",
                    "heading": "Cent-quarante-deux éléments, zéro surimposition",
                    "body":
                        "Le système a été installé en trois chantiers "
                        "successifs entre juin et septembre 2024, avec "
                        "réception conjointe de la Surintendance pour "
                        "le rez-de-chaussée Scarpa. Les gravures sur "
                        "laiton ont été réalisées par la bottega "
                        "Pasinetti à Murano selon la technique "
                        "traditionnelle — quinze semaines de "
                        "fabrication, toutes vérifiées in situ par le "
                        "studio.",
                },
            ],
            "next_label": "Projet suivant",
        },
    ],
}
