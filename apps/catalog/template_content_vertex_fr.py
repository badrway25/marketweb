"""Vertex — Creative Studio · FR content registry.

Agency live rollout, Phase 2g3.6f, Session 49 · French locale.

Voice contract (Paris / Bruxelles independent creative-studio register):
- Libération Next / Études / Grafik / A3 Magazine / M/M Paris register.
- « Nous dessinons », « nous accompagnons », « nous signons ». Vouvoiement.
- Lexicon: brief, système d'identité, manuel de marque, ligne éditoriale,
  collection, direction artistique, signalétique. Jamais sprint / KPI.
- Insecable spaces before : ; ? ! and inside « … » (U+00A0).
- Proper names stay (Fondazione Prada, Triennale Milano, Adelphi, etc.).
- Publication names stay as-is. Quote authors keep Italian names.
"""
from __future__ import annotations

from typing import Any


VERTEX_CONTENT_FR: dict[str, Any] = {

    "pages": [
        {"slug": "home",     "label": "Studio",       "kind": "home"},
        {"slug": "studio",   "label": "À propos",     "kind": "about"},
        {"slug": "capacita", "label": "Savoir-faire", "kind": "services"},
        {"slug": "lavori",   "label": "Travaux",      "kind": "project_list"},
        {"slug": "manifesto","label": "Manifeste",    "kind": "process"},
        {"slug": "contatti", "label": "Contact",      "kind": "contact"},
    ],

    # ── Site chrome ──────────────────────────────────────────────
    "site": {
        "logo_word":   "Vertex Studio",
        "tag":         "Studio de création indépendant · Milan",
        "availability":"Nouvelles commandes · automne 2026",
        "nav_cta":     "Demander le dossier",
        "inquiry_page_slug": "contatti",
        "phone":       "+39 02 4981 2066",
        "email":       "studio@vertex.milano",
        "address":     "Via Tortona 32 · 20144 Milan",
        "hours_compact": "Studio ouvert · mar / jeu",
        "license":     "P.IVA 10456770963 · Milan",
        "footer_intro":
            "Studio de création indépendant fondé à Milan en 2018. "
            "Nous dessinons des systèmes d'identité, des collections "
            "éditoriales et des directions artistiques pour des "
            "fondations, maisons et maisons d'édition italiennes.",
        "foot_clients_label":     "Selected clients · 2018 — 2026",
        "clients_footer_rows": [
            "FONDAZIONE PRADA", "2024",
            "MAISON GENTILUOMO", "2025",
            "ADELPHI EDIZIONI", "2024",
            "TRIENNALE MILANO", "2023",
            "MUSEO DEL '900", "2025",
            "VILLA NECCHI", "2024",
        ],
        "foot_standfirst":
            "Une marque ne devrait jamais avoir l'air de sortir à peine du studio. "
            "Un bon système visuel tient la saison. Un système construit "
            "avec soin tient la décennie.",
        "foot_studio_label":      "Le studio",
        "foot_recognition_label": "Reconnaissances",
        "foot_recognition_rows": [
            "ADI Design Index — 2024",
            "Type Directors Club — 2023",
            "Prix Compasso d'Oro — Mention 2022",
            "European Design Awards — 2022",
        ],
    },

    # ── HOME ─────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Studio indépendant · fondé en 2018 · Milan",
        "headline": "Des marques qui <em>pèsent</em>, qui <em>tiennent</em>, qui <em>durent</em>.",
        "pull_quote":
            "« La marque n'est pas un logo. C'est la manière dont une chose "
            "vous regarde quand personne ne parle d'elle. »",
        "intro":
            "Nous sommes un studio de création indépendant qui dessine "
            "des systèmes d'identité, des collections éditoriales et "
            "des directions artistiques pour un nombre restreint de "
            "clients culturels et de luxe. Nous accompagnons chaque "
            "marque du premier brief jusqu'au dernier tirage.",
        "primary_cta":   "Demander le dossier",
        "primary_href":  "contatti",
        "secondary_cta": "Travaux sélectionnés",
        "secondary_href":"lavori",

        # Hero right — editorial cover tile
        "cover": {
            "image":  "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=900&q=80&auto=format&fit=crop",
            "badge":  "Case Study · 01",
            "client_name": "FONDAZIONE PRADA · Collection 2025",
            "title":  "Un système éditorial pour <em>quatre auteurs</em> et vingt-deux titres.",
            "discipline": "Identité · édition",
            "year":   "2025 — 2026",
            "credit_left_label":  "Direction artistique",
            "credit_left_value":  "M. Serafini",
            "credit_right_label": "Déploiement",
            "credit_right_value": "Oct 2025",
        },

        # Ledger
        "ledger_heading":   "Travaux <em>récents</em>",
        "ledger_link":      "Archives complètes →",
        "ledger_page_slug": "lavori",
        "ledger_rows": [
            ("01", "Collection Narrative Italienne", "Adelphi Edizioni",     "Identité & édition",   "2025", "adelphi-collana-narrativa"),
            ("02", "Refonte de la Fondation",         "Fondazione Prada",     "Direction artistique", "2025", "fondazione-prada-rebrand"),
            ("03", "Manuel de marque intégré",        "Maison Gentiluomo",    "Branding de luxe",     "2024", "maison-gentiluomo-manuale"),
            ("04", "Signalétique & wayfinding",       "Triennale Milano",     "Identité spatiale",    "2024", "triennale-milano-wayfinding"),
            ("05", "Série d'affiches d'auteur",       "Museo del Novecento",  "Direction artistique", "2024", "museo-900-manifesti"),
            ("06", "Packaging six cuvées",            "Villa Necchi Winery",  "Packaging d'auteur",   "2023", "villa-necchi-sei-cuvee"),
        ],

        # Capacità
        "capab_label":   "Savoir-faire du studio",
        "capab_heading": "Quatre <em>disciplines</em>, une seule direction.",
        "capab_intro":
            "Nous travaillons sur quatre axes qui s'entrelacent dans chaque "
            "projet : identité de marque, lignes éditoriales, direction "
            "artistique et campagnes. Nous ne sommes pas une agence de service — "
            "nous sommes un studio qui construit des systèmes.",
        "capab_items": [
            ("01", "Identité de marque",
             "Logo, système typographique, palette, grille, manuel. "
             "De la première restitution au déploiement sur les supports, "
             "en six à douze semaines.",
             ["Logotype", "Manuel", "Typeface sur mesure", "Grille"]),
            ("02", "Lignes éditoriales",
             "Collections, revues, catalogues, livres d'auteur. "
             "Nous construisons la grille, choisissons les caractères, "
             "suivons l'impression.",
             ["Collections", "Revues", "Catalogues", "Livres"]),
            ("03", "Direction artistique",
             "Campagnes saisonnières, shootings d'auteur, "
             "affiches, matériaux POS. De la moodboard "
             "à la prise de vue, jusqu'à l'impression.",
             ["Campagnes", "Shootings", "Affiches", "Motion"]),
            ("04", "Systèmes visuels",
             "Signalétique, wayfinding, scénographie, "
             "environnements d'exposition. Des identités qui "
             "s'habitent, qui ne se regardent pas.",
             ["Wayfinding", "Signalétique", "Scénographie", "Expositions"]),
        ],

        # Press
        "press_heading": "Publiés <em>et reconnus</em>.",
        "press_intro":
            "Notre pratique est petite, délibérée, "
            "elle choisit ses projets avec soin. Mais lorsqu'un travail "
            "tient, le travail se fait remarquer.",
        "press_publications": [
            "Monocle", "Domus", "Wallpaper*", "Creative Review",
            "It's Nice That", "Design Week", "Eye Magazine", "Slanted",
        ],

        # Manifesto
        "manifesto_label":   "Manifeste court",
        "manifesto_heading": "Une marque <em>ne se décore pas</em>. Elle se construit.",
        "manifesto_drop_cap": "U",
        "manifesto_body":
            "n bon projet part d'une question que personne "
            "n'a encore le courage de poser. Dessiner une marque "
            "ne signifie pas emballer ce qu'un client "
            "pense déjà savoir de lui-même — cela veut dire l'aider à "
            "reconnaître ce qu'il sait déjà mais qu'il n'a pas encore "
            "nommé. C'est pourquoi nous n'acceptons pas de commandes "
            "d'impulsion. C'est pourquoi chaque relation commence par "
            "une conversation, jamais par un devis.",
        "manifesto_principles": [
            ("01", "La forme <em>suit la voix</em>",
             "Le choix typographique vient après le choix du ton. "
             "D'abord on décide comment une marque parle, puis comment elle apparaît."),
            ("02", "Le système <em>avant l'image</em>",
             "Nous dessinons des règles, non des applications. La tâche "
             "d'une bonne règle est de se faire oublier."),
            ("03", "Le papier <em>tient le temps</em>",
             "Chaque projet doit dépasser au moins deux saisons "
             "de tendance sans perdre position. Sinon c'est du décor."),
            ("04", "Le client <em>est co-auteur</em>",
             "Nous travaillons avec ceux qui ont une voix. Qui cherche un service "
             "silencieux trouvera une réponse courtoise mais ferme."),
        ],

        # Inquiry CTA
        "cta_label":   "Prochaine étape",
        "cta_heading": "Un brief bien fait <em>vaut six semaines</em>.",
        "cta_sub":
            "Nous répondons sous trois jours ouvrés avec un bref "
            "dossier de lecture du projet.",
        "cta_primary": "Demander le dossier",
    },

    # ── STUDIO (about) ───────────────────────────────────────────
    "studio": {
        "eyebrow":   "Le studio · huit ans",
        "headline":  "Quarante mètres carrés de papier, épreuves d'impression <em>et caractères encore à choisir</em>.",
        "standfirst":
            "Nous sommes trois directeurs de création, deux designers seniors, "
            "une cheffe de projet et un photographe qui passe ici "
            "trois fois par semaine. Le studio a soufflé ses huit "
            "bougies, mené trente-deux projets qui ont changé "
            "de maison, et accumulé une archive d'épreuves d'impression qui "
            "ne tient plus derrière la porte.",

        "facts": [
            ("8",    "ans d'activité",      "Fondé en 2018 à Milan"),
            ("42",   "projets en archives", "Dont 22 publiés"),
            ("6",    "collaborateurs",      "Trois partenaires · trois seniors"),
            ("2",    "saisons de rollout",  "La durée moyenne d'une marque"),
        ],

        "essay_label":   "Histoire du studio",
        "essay_heading": "Nous avons commencé avec <em>un caractère et une question</em>.",
        "essay_paragraphs": [
            "Vertex naît en 2018 d'une idée de Margherita Serafini "
            "et Tommaso Boeri, camarades de promotion à l'ISIA d'Urbino "
            "puis collaborateurs dans deux studios milanais. La question "
            "de départ était très simple : <em>pourquoi tant de marques "
            "italiennes sont-elles magnifiques à découvrir et oubliables "
            "au bout de deux mois ?</em>",
            "La réponse — comprise lentement, projet après projet — "
            "c'est que la plupart des marques sont dessinées comme on "
            "habille une vitrine : on choisit ce qui se voit en premier, "
            "non ce qui tient le temps. Dessiner un système de "
            "marque qui tienne huit ans n'est pas une affaire de "
            "tendances, mais de choix que l'on retire quand il le faut.",
        ],
        "essay_pullquote":
            "Un manuel bien fait ne décrit pas la marque. "
            "Il la défend contre notre propre envie de la changer.",
        "essay_tail_paragraphs": [
            "Aujourd'hui, le studio travaille en moyenne avec huit clients par an. "
            "Nous refusons plus de la moitié des briefs que nous recevons — non par "
            "métier, mais par honnêteté : un projet mal fait fait mal "
            "deux fois, au client et au portfolio.",
            "Nous avons choisi de rester petits. Nous n'avons pas d'ambitions "
            "d'échelle. Nous voulons continuer à répondre personnellement "
            "à chaque premier e-mail, à suivre chaque épreuve d'impression, "
            "à connaître le nom des typographes qui impriment nos livres.",
        ],

        "partners_label":   "Les trois partenaires",
        "partners_heading": "Qui <em>signe</em> le studio.",
        "partners_intro":
            "Chaque projet est suivi par au moins un des trois partenaires "
            "du premier brief au déploiement final. Nous ne déléguons pas les moments "
            "décisifs — si une marque part bien, c'est parce que quelqu'un était "
            "présent au moment où l'on a dit non à une première idée.",
        "partners": [
            {
                "name": "Margherita Serafini",
                "role": "Co-fondatrice · Directrice de la création",
                "bio":  "Diplôme de graphisme éditorial à l'ISIA d'Urbino. "
                        "Avant Vertex, huit ans chez Cabinet (Milan) "
                        "comme senior designer. Obsédée par les caractères "
                        "serif de la seconde moitié du XXᵉ siècle.",
                "portrait": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=900&q=80&auto=format&fit=crop",
                "creds": ["ISIA Urbino", "ADI Design Index 2024", "Enseignante IED"],
            },
            {
                "name": "Tommaso Boeri",
                "role": "Co-fondateur · Directeur artistique",
                "bio":  "Formé à l'ECAL Lausanne. Il a travaillé pour Studio "
                        "Dumbar et M/M Paris avant de revenir à Milan. "
                        "Directeur artistique de deux maisons d'édition indépendantes.",
                "portrait": "https://images.unsplash.com/photo-1568602471122-7832951cc4c5?w=900&q=80&auto=format&fit=crop",
                "creds": ["ECAL Lausanne", "TDC Award 2023", "European Design"],
            },
            {
                "name": "Ilaria Ferri",
                "role": "Partenaire · Directrice éditoriale",
                "bio":  "Licence de lettres à la Statale de Milan. "
                        "Dix ans chez Adelphi avant de rejoindre le "
                        "studio en 2021. Elle dirige les lignes éditoriales "
                        "et la rédaction des manuels.",
                "portrait": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop",
                "creds": ["Statale Milan", "ex Adelphi", "Prix Gutenberg"],
            },
        ],

        "timeline_label":   "Chronologie",
        "timeline_heading": "Huit ans <em>sur papier</em>.",
        "timeline_rows": [
            ("2018",
             "Ouverture du studio Via Tortona 32",
             "Premier projet : refonte de la librairie indépendante Scheiwiller. "
             "Serafini et Boeri signent le premier manuel du studio sur une feuille A3."),
            ("2020",
             "Première commande institutionnelle",
             "Direction artistique pour la Triennale Milano — vingt-deux mois de travail "
             "sur la signalétique des salles permanentes."),
            ("2021",
             "Arrivée d'Ilaria Ferri comme partenaire",
             "Ouverture de la pratique éditoriale avec la première collection pour Adelphi "
             "— neuf titres parus en dix-huit mois."),
            ("2023",
             "Reconnaissance ADI Design Index",
             "Prix pour la collection Architectures Contemporaines. "
             "Première couverture italienne d'Eye Magazine."),
            ("2025",
             "Refonte de la Fondazione Prada",
             "Vingt-deux mois de travail. Déploiement complet à l'automne 2025, "
             "avec signalétique, édition, campagnes saisonnières."),
            ("2026",
             "Ouverture de la seconde salle",
             "Extension au 34 Via Tortona, avec archives d'épreuves d'impression "
             "consultables sur rendez-vous."),
        ],
    },

    # ── CAPACITA (services) ──────────────────────────────────────
    "capacita": {
        "eyebrow":   "Savoir-faire du studio",
        "headline":  "Quatre <em>disciplines</em> qui s'entrelacent dans chaque projet.",
        "standfirst":
            "Nous ne sommes pas une agence à service complet. Nous sommes un studio "
            "qui travaille sur quatre axes clairs, chacun avec une pratique "
            "stable et un processus documenté. Chaque projet puise dans "
            "un ou plusieurs de ces axes — rarement dans tous à la fois.",

        "disciplines": [
            {
                "num": "01",
                "title": "Identité de <em>marque</em>",
                "tagline": "Logo, caractère, grille, manuel. Six à douze semaines.",
                "body":
                    "Nous construisons des systèmes d'identité qui tiennent huit ans. "
                    "Chaque refonte part d'une conversation avec le directeur "
                    "général ou le fondateur — jamais d'un brief envoyé par e-mail. "
                    "Nous restituons trois directions, puis une seule. Le manuel final "
                    "a un index utile, non un index qui impressionne.",
                "scope_label": "Inclus",
                "scope": [
                    "Logotype et variations",
                    "Système typographique (texte + display)",
                    "Palette chromatique étendue",
                    "Grille et règles de composition",
                    "Manuel de marque (PDF interactif + impression)",
                    "Plates d'applications (print · web · environnement)",
                ],
            },
            {
                "num": "02",
                "title": "Lignes <em>éditoriales</em>",
                "tagline": "Collections, revues, catalogues, livres d'auteur.",
                "body":
                    "La pratique éditoriale est le cœur du studio. Nous dessinons "
                    "des collections qui tiennent la saison — la grille, le format, "
                    "la cage, les couvertures. Nous suivons l'impression jusqu'à l'épreuve "
                    "machine, avec les typographes de confiance de Milan et Bergame. "
                    "Nous sommes présents pour le premier livre de chaque collection signée.",
                "scope_label": "Inclus",
                "scope": [
                    "Dessin du format et cage",
                    "Couverture (système + application)",
                    "Mise en page typographique texte",
                    "Conseil en impression et papier",
                    "Suivi d'impression sur le premier titre",
                    "Fiche d'application pour le studio graphique interne",
                ],
            },
            {
                "num": "03",
                "title": "Direction <em>artistique</em>",
                "tagline": "Campagnes, shootings d'auteur, affiches.",
                "body":
                    "Nous dirigeons des campagnes saisonnières pour maisons et marques "
                    "italiennes avec une approche éditoriale — jamais publicitaire. "
                    "Nous choisissons les photographes, construisons la moodboard, "
                    "suivons le shooting. Les campagnes naissent pour tenir "
                    "deux cycles éditoriaux — non une semaine de social.",
                "scope_label": "Inclus",
                "scope": [
                    "Concept saisonnier (PDF de lecture · 24 pages)",
                    "Casting photographique + direction",
                    "Direction du jour de shooting",
                    "Sélection et post-production",
                    "Système d'application (print · digital · retail)",
                    "Affiches + collatéraux de lancement",
                ],
            },
            {
                "num": "04",
                "title": "Systèmes <em>spatiaux</em>",
                "tagline": "Signalétique, wayfinding, scénographie.",
                "body":
                    "Lorsqu'une identité devient un lieu, nous la concevons "
                    "avec l'architecte. Wayfinding permanent pour "
                    "musées et fondations, scénographies temporaires d'"
                    "expositions, signalétique pour retail de luxe. Chaque système "
                    "spatial part d'un relevé sur site. Nous ne travaillons jamais depuis un render.",
                "scope_label": "Inclus",
                "scope": [
                    "Relevé sur site et restitution technique",
                    "Grille de lecture de l'espace",
                    "Système typographique + pictographique",
                    "Plans d'exécution pour la production",
                    "Collaboration avec le cabinet d'architecture",
                    "Présence sur chantier · première installation",
                ],
            },
        ],

        "engagement_label":   "Trois manières de travailler",
        "engagement_heading": "Du <em>projet unique</em> au <em>partenaire éditorial</em>.",
        "engagement_intro":
            "Nous acceptons trois types de missions. Nous les dessinons avec le "
            "client en phase de brief — nous n'avons pas de tarifs cachés.",
        "engagement_tiles": [
            {
                "title":  "Projet <em>unique</em>",
                "range":  "Douze — vingt-quatre semaines",
                "body":   "Une identité ou une ligne éditoriale, du brief au déploiement. "
                          "Pour des marques qui ont besoin d'un geste net et défini.",
                "includes": [
                    "Brief conjoint + trois directions",
                    "Déploiement sur trois applications",
                    "Manuel de marque en italien / anglais",
                    "Présence au lancement",
                ],
            },
            {
                "title":  "Commande <em>saisonnière</em>",
                "range":  "Six — douze mois · contrat renouvelable",
                "body":   "Direction artistique saisonnière pour maisons ou institutions. "
                          "Deux campagnes par an, avec toutes les applications.",
                "includes": [
                    "Campagne printemps / automne",
                    "Collatéraux de lancement",
                    "Présence mensuelle au studio",
                    "Archive partagée",
                ],
            },
            {
                "title":  "Partenaire <em>éditorial</em>",
                "range":  "Engagement annuel · sur invitation",
                "body":   "Présence constante à la table éditoriale du client. "
                          "Pour maisons d'édition, fondations, institutions culturelles.",
                "includes": [
                    "Participation au plan éditorial",
                    "Direction sur toutes les parutions de l'année",
                    "Conseil en impression et papier",
                    "Archive + backup créatif",
                ],
            },
        ],

        "cta_label":   "Brief gratuit",
        "cta_heading": "Un premier <em>thé ensemble</em> ne coûte rien.",
        "cta_primary": "Demander le dossier",
    },

    # ── LAVORI (project_list) ────────────────────────────────────
    "lavori": {
        "eyebrow":   "Archives des travaux · 2018 — 2026",
        "headline":  "Quarante-deux projets <em>en archives</em>, vingt-deux en vitrine.",
        "standfirst":
            "Une sélection raisonnée. Nous ne montrons pas tout — tout "
            "ne tient pas à la relecture. L'archive complète est disponible sur "
            "demande, au format PDF imprimable (cent-six pages).",
        "filters": ["Tous", "Identité", "Édition", "Direction artistique", "Systèmes spatiaux"],

        "projects": [
            {
                "slug":       "fondazione-prada-rebrand",
                "index":      "01",
                "title":      "Refonte de la Fondation",
                "client":     "Fondazione Prada — Milan",
                "discipline": "Direction artistique",
                "year":       "2025",
            },
            {
                "slug":       "adelphi-collana-narrativa",
                "index":      "02",
                "title":      "Collection Narrative Italienne",
                "client":     "Adelphi Edizioni — Milan",
                "discipline": "Identité & édition",
                "year":       "2025",
            },
            {
                "slug":       "maison-gentiluomo-manuale",
                "index":      "03",
                "title":      "Manuel de marque intégré",
                "client":     "Maison Gentiluomo — Florence",
                "discipline": "Branding de luxe",
                "year":       "2024",
            },
            {
                "slug":       "triennale-milano-wayfinding",
                "index":      "04",
                "title":      "Signalétique & wayfinding permanent",
                "client":     "Triennale Milano — Parco Sempione",
                "discipline": "Identité spatiale",
                "year":       "2024",
            },
            {
                "slug":       "museo-900-manifesti",
                "index":      "05",
                "title":      "Série d'affiches d'auteur",
                "client":     "Museo del Novecento — Milan",
                "discipline": "Direction artistique",
                "year":       "2024",
            },
            {
                "slug":       "villa-necchi-sei-cuvee",
                "index":      "06",
                "title":      "Packaging six cuvées d'auteur",
                "client":     "Villa Necchi Winery — Valpolicella",
                "discipline": "Packaging",
                "year":       "2023",
            },
        ],

        "archive_label":   "Archives complètes",
        "archive_heading": "Disponibles <em>sur demande</em>, cent-six pages.",
        "archive_body":
            "Les archives complètes contiennent quarante-deux projets depuis 2018, "
            "avec processus de travail, échantillons d'impression, notes "
            "éditoriales et coordonnées du client.",
        "archive_stats": [
            ("42",   "projets en archives"),
            ("22",   "publiés"),
            ("8",    "années de pratique"),
            ("<em>6</em>", "clients par an en moyenne"),
        ],
    },

    # ── MANIFESTO (process) ──────────────────────────────────────
    "manifesto": {
        "eyebrow":   "Notre manière de travailler",
        "headline":  "Six semaines pour <em>comprendre</em>. Dix pour <em>construire</em>. Deux pour <em>défendre</em>.",
        "standfirst":
            "Chaque projet traverse quatre phases déclarées. "
            "Nous n'aimons pas les surprises — ni pour nous, ni pour le "
            "client. Le calendrier est public dès le premier jour.",

        "phases": [
            {
                "num": "01",
                "duration": "Semaines 1 — 6",
                "title": "<em>Écoute</em> · lectures · relevé",
                "tagline": "Comprendre avant de dessiner.",
                "body":
                    "Nous rencontrons le directeur général, la responsable communication "
                    "et, lorsque c'est possible, les clients. Nous lisons l'archive, les études "
                    "précédentes, les rapports annuels. Nous visitons les espaces. Aucune "
                    "forme n'est proposée dans cette phase — seulement une lecture écrite "
                    "de 24 à 32 pages qui devient la base du projet.",
                "deliverables_label": "Livrables",
                "deliverables": [
                    "Dossier de lecture (24-32 pages PDF)",
                    "Trois territoires stratégiques à explorer",
                    "Tableau de référence historique",
                    "Calendrier détaillé des livrables suivants",
                ],
            },
            {
                "num": "02",
                "duration": "Semaines 7 — 14",
                "title": "<em>Hypothèses</em> · trois directions",
                "tagline": "Trois propositions, aucune compromise.",
                "body":
                    "Nous présentons trois directions créatives pleinement construites — "
                    "non trois variantes d'une même intuition. Chaque direction a "
                    "logo, caractère, deux applications pilotes. Le client choisit "
                    "une direction (ou demande un quatrième tour — cela arrive rarement).",
                "deliverables_label": "Livrables",
                "deliverables": [
                    "Trois directions créatives (24 planches chacune)",
                    "Une application pilote par direction",
                    "Lecture comparative écrite",
                    "Présentation au studio · une demi-journée",
                ],
            },
            {
                "num": "03",
                "duration": "Semaines 15 — 22",
                "title": "<em>Construction</em> · système & manuel",
                "tagline": "De la direction au manuel, sans perdre le ton.",
                "body":
                    "La direction choisie est développée en un système complet : "
                    "grille, palette étendue, variations de la marque, règles "
                    "de composition, manuel final. En parallèle nous construisons "
                    "trois à cinq applications témoins pour éprouver le système "
                    "sur des cas réels.",
                "deliverables_label": "Livrables",
                "deliverables": [
                    "Système de marque complet (fichiers sources)",
                    "Manuel de marque (PDF interactif + version impression)",
                    "Trois à cinq applications témoins",
                    "Fontes retail + licences documentées",
                ],
            },
            {
                "num": "04",
                "duration": "Semaines 23 — 24",
                "title": "<em>Déploiement</em> · défense · clôture",
                "tagline": "Le manuel prend vie, nous restons proches.",
                "body":
                    "Nous accompagnons le déploiement sur les premières applications réelles "
                    "avec une présence au studio et du conseil à l'équipe interne du "
                    "client. Nous suivons le premier tirage important. Nous clôturons "
                    "par une réunion de passation documentée, où le "
                    "responsable interne devient gardien du système.",
                "deliverables_label": "Livrables",
                "deliverables": [
                    "Présence au lancement public",
                    "Premières applications suivies personnellement",
                    "Réunion de passation + document de gouvernance",
                    "Six mois de disponibilité pour les clarifications",
                ],
            },
        ],

        "principles_label":   "Principes du studio",
        "principles_heading": "<em>Sept</em> engagements que nous ne négocions pas.",
        "principles": [
            ("01", "Un <em>chapitre à la fois</em>",
             "Jamais deux phases ensemble. Un client qui accélère une phase compromet la suivante. Nous avons résilié plus d'un contrat sur ce point."),
            ("02", "<em>Trois directions</em>, jamais quatre",
             "Quatre directions rendent le choix arbitraire. Trois obligent à un raisonnement. Deux seraient paresseuses."),
            ("03", "Le <em>caractère</em> se licencie",
             "Nous n'utilisons pas de fontes gratuites pour des projets rémunérés. Chaque licence est documentée au client, avec budget séparé."),
            ("04", "L'<em>impression</em> se présence",
             "Le premier démarrage machine de chaque déploiement important est suivi par un partenaire du studio."),
            ("05", "Le <em>client</em> est co-auteur",
             "Le client signe le manuel avec le studio. Ce n'est pas un service — c'est un projet partagé."),
            ("06", "<em>Non</em> fait partie du service",
             "Nous disons non plus souvent que nous ne proposons. C'est la principale valeur que nous apportons."),
        ],

        "promise_label":   "Nos chiffres",
        "promise_heading": "Petits <em>par choix</em>, lents <em>par méthode</em>.",
        "promise_stats": [
            ("<em>6</em>",       "clients par an en moyenne",
             "Plus de 12 briefs reçus par mois, moins de 6 acceptés par an."),
            ("<em>8</em>",       "ans de durée moyenne",
             "Les identités signées entre 2018 et 2022 sont toutes encore actives."),
            ("<em>3 j</em>",     "réponse au premier brief",
             "Sous trois jours ouvrés vous recevrez une première lecture écrite du projet."),
        ],
    },

    # ── CONTATTI (contact) ───────────────────────────────────────
    "contatti": {
        "eyebrow":   "Demander le dossier",
        "headline":  "Racontez-nous <em>le projet</em>. Nous répondons sous trois jours.",
        "standfirst":
            "Chaque e-mail arrive directement à Margherita ou Tommaso. "
            "Il n'y a pas d'account manager filtre — celui qui vous répond est "
            "celui qui suivra le projet en première personne, si vous décidez "
            "de travailler ensemble.",

        "form_heading": "Brief du projet",
        "labels": {
            "name":       "Nom et prénom",
            "role":       "Rôle dans l'organisation",
            "company":    "Organisation / marque",
            "email":      "E-mail de contact",
            "discipline": "Discipline principale demandée",
            "budget":     "Fourchette de budget indicative",
            "brief":      "Récit du projet",
        },
        "placeholders": {
            "name":    "Prénom Nom",
            "role":    "ex. Directeur de la communication",
            "company": "Nom de l'organisation",
            "email":   "nom@organisation.it",
            "brief":   "Qui vous êtes, ce que vous cherchez à construire, dans quel délai, avec quelle équipe interne. Plus c'est concret, plus la réponse sera utile.",
        },
        "discipline_options": [
            "Identité de marque (refonte)",
            "Identité de marque (premier lancement)",
            "Ligne éditoriale · collection",
            "Direction artistique · campagne",
            "Système spatial · wayfinding",
            "Je ne suis pas encore sûr — parlons-en",
        ],
        "budget_bands": [
            ("12k",    "< 12 K€"),
            ("40k",    "12 — 40 K€"),
            ("120k",   "40 — 120 K€"),
            ("120plus","> 120 K€"),
        ],
        "form_submit_label": "Envoyer le brief",
        "form_submit_note":  "Nous répondons sous trois jours ouvrés avec une première lecture.",

        "direct_label":   "E-mail direct",
        "direct_heading": "Écrivez à <em>Margherita</em> et <em>Tommaso</em>.",

        "studio_label":   "Le studio",

        "reply_label":    "Délais de réponse",
        "reply_heading":  "Trois <em>jours ouvrés</em>, pas plus.",
        "reply_body":
            "Chaque brief reçoit sous 72 heures une première lecture écrite : "
            "nous vous disons si le projet nous correspond, si le moment est juste, "
            "si l'on se rencontre en personne pour approfondir. "
            "Jamais de réponses automatiques, jamais de devis sans lecture.",

        "channels_label": "Canaux",
        "channels": [
            ("E-mail",     "studio@vertex.milano"),
            ("Téléphone",  "+39 02 4981 2066"),
            ("Studio",     "Via Tortona 32 · Milan"),
            ("LinkedIn",   "/company/vertex-milano"),
            ("Are.na",     "/vertex-studio"),
            ("Secrétariat","mar · jeu · 10 — 18"),
        ],

        "promise_label":   "Un engagement",
        "promise_heading":
            "« Nous n'envoyons jamais un devis avant un brief de lecture. "
            "C'est un petit geste, mais il change la conversation. »",
    },

    # ── POSTS (project_detail) ───────────────────────────────────
    "posts": [
        {
            "slug": "fondazione-prada-rebrand",
            "index": "01",
            "title": "Une <em>refonte institutionnelle</em> qui ne se fait pas remarquer.",
            "client": "Fondazione Prada — Milan",
            "discipline": "Direction artistique · identité",
            "year": "2025",
            "team": "Serafini · Boeri · Ferri",
            "standfirst":
                "Une refonte de l'identité institutionnelle pensée pour tenir "
                "vingt ans de programmation culturelle, sans demander au "
                "visiteur d'apprendre un nouveau vocabulaire visuel.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Année de livraison",
            "meta_label_team":       "Équipe du studio",
            "cover_image": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "Le problème",
                    "title": "Une institution <em>lue par erreur</em>.",
                    "paragraphs": [
                        "Quand la Fondation nous a appelés, au premier trimestre 2024, "
                        "la question n'était pas la marque — la marque fonctionnait. Le problème "
                        "était que <em>l'identité n'accompagnait plus le programme</em>.",
                        "La Fondation avait publié cinquante-deux événements en 2023, "
                        "mais les communiqués de presse semblaient tous <em>une même institution "
                        "fatiguée</em>. La faute n'était pas celle de la marque. C'était celle du système — un "
                        "manuel de 2011, pensé pour un programme bien plus restreint.",
                    ],
                },
                {
                    "label": "La méthode",
                    "title": "Dessiner une <em>seconde voix</em>, non un second logo.",
                    "paragraphs": [
                        "Nous avons choisi de ne pas toucher à la marque principale. Nous avons "
                        "dessiné à la place un <em>système éditorial parallèle</em> — une "
                        "seconde voix visuelle, utilisée pour toute la communication du programme. "
                        "La marque institutionnelle reste, mais s'efface.",
                        "Ce choix a permis d'éviter la fracture qui accompagne "
                        "chaque refonte — personne n'a eu à désinstaller quoi que ce soit. "
                        "La nouvelle voix s'est juxtaposée à l'ancienne, conquérant l'espace "
                        "progressivement, saison après saison.",
                    ],
                    "pullquote":
                        "La marque institutionnelle est une signature. La seconde voix est une manière "
                        "de parler. Une signature ne change pas — la manière de parler peut évoluer.",
                },
                {
                    "label": "Le résultat",
                    "title": "Une <em>saison</em>, cinquante-deux événements, une seule voix.",
                    "paragraphs": [
                        "La nouvelle voix éditoriale a été appliquée pour la première fois "
                        "durant la saison automne 2025, sur cinquante-deux événements publiés. "
                        "L'équipe interne de communication a adopté le système avec "
                        "six jours d'accompagnement au studio. Aucun contenu n'a été "
                        "refait — tout a été re-vêtu.",
                    ],
                },
            ],
            "deliverables_label": "Livrables",
            "deliverables_heading": "Quatre <em>systèmes</em>, un seul manuel.",
            "deliverables_intro":
                "Le manuel final — 184 pages — a été rédigé avec l'équipe "
                "de communication de la Fondation, avec glossaire partagé.",
            "deliverables": [
                ("01", "Système éditorial secondaire",
                 "Typographie, grille, palette saisonnière, variations régionales. "
                 "Appliqué à tous les matériaux du programme — invitations, brochures, social."),
                ("02", "Manuel de marque intégré",
                 "184 pages, italien + anglais. Il contient les deux systèmes (historique + nouveau) "
                 "avec des critères clairs pour choisir l'un ou l'autre."),
                ("03", "Gabarits de production autonome",
                 "Fichiers sources prêts pour le studio graphique interne. "
                 "Trois typologies (invitation, communiqué, brochure) × quatre saisons."),
            ],
            "press_quote":
                "Une refonte presque invisible qui a changé la respiration de l'institution. "
                "Rare, en Italie, de voir un studio qui choisit de s'effacer.",
            "press_source":     "Domus — Novembre 2025",
            "press_journalist": "Giulia Bellini",
            "next_label":       "Cas suivant",
            "next_heading":     "Aller aux <em>archives des travaux</em> →",
            "cta_label":        "Commandes 2026",
            "cta_heading":      "Ouvrir le <em>dossier du studio</em> →",
        },
        {
            "slug": "adelphi-collana-narrativa",
            "index": "02",
            "title": "Une <em>collection</em> pour dix-huit voix narratives.",
            "client": "Adelphi Edizioni — Milan",
            "discipline": "Identité & édition",
            "year": "2025",
            "team": "Ferri · Serafini",
            "standfirst":
                "Le dessin d'une nouvelle collection narrative contemporaine pour une "
                "maison d'édition historique — dix-huit titres parus en dix-huit mois, "
                "avec un système de couverture qui alterne portrait et abstraction.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Année de parution",
            "meta_label_team":       "Équipe du studio",
            "cover_image": "https://images.unsplash.com/photo-1481487196290-c152efe083f5?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "Le brief",
                    "title": "Une <em>collection qui ne ressemble pas</em> à une collection.",
                    "paragraphs": [
                        "Adelphi voulait ouvrir un espace pour des auteurs narratifs contemporains "
                        "italiens, sans trahir le ton silencieux et médité de la maison. "
                        "Le brief initial était délibérément minimal : <em>une collection qui se "
                        "reconnaisse sans ressembler à une collection</em>.",
                    ],
                },
                {
                    "label": "Le choix",
                    "title": "Portrait <em>et</em> abstraction, jamais ensemble.",
                    "paragraphs": [
                        "Nous avons proposé un système qui alterne deux registres : couvertures avec "
                        "photographie (portrait de l'auteur sur papier travaillé) et couvertures "
                        "abstraites (compositions typographiques avec le titre seul). Le choix "
                        "entre les deux registres revient au directeur éditorial, cas par cas.",
                    ],
                    "pullquote":
                        "Le système n'oblige pas. Il suggère. La meilleure règle éditoriale "
                        "est celle que le directeur peut enfreindre une fois, à raison.",
                },
            ],
            "deliverables_label": "Livrables",
            "deliverables_heading": "Un système <em>discret</em>, dix-huit voix distinctes.",
            "deliverables_intro":
                "Chaque titre est suivi par Ilaria Ferri en phase de choix de "
                "couverture et en épreuve d'impression, pour les trois premières saisons.",
            "deliverables": [
                ("01", "Dessin du format + cage",
                 "120 × 185 mm, papier Palatina 80 g, brochure cousue fil. "
                 "Cage avec deux options de mise en page pour textes denses."),
                ("02", "Système de couverture",
                 "Deux registres alternés (portrait / abstraction) avec palette "
                 "de quatre couleurs. Règles de composition documentées."),
                ("03", "Premier titre · Comme les oiseaux nous voient",
                 "Suivi depuis la première épreuve d'impression jusqu'au tirage final, "
                 "avec présence à l'imprimerie à Bergame."),
            ],
            "press_quote":
                "Une collection qui ajoute sans déplacer. Très Adelphi, très neuf.",
            "press_source":     "Corriere della Sera · La Lettura — Décembre 2025",
            "press_journalist": "Andrea Pomella",
            "next_label":       "Cas suivant",
            "next_heading":     "Aller aux <em>archives des travaux</em> →",
            "cta_label":        "Pratique éditoriale",
            "cta_heading":      "Ouvrir le <em>dossier éditorial</em> →",
        },
        {
            "slug": "maison-gentiluomo-manuale",
            "index": "03",
            "title": "Un <em>manuel de marque</em> pour la troisième génération.",
            "client": "Maison Gentiluomo — Florence",
            "discipline": "Branding de luxe",
            "year": "2024",
            "team": "Boeri · Serafini",
            "standfirst":
                "La refonte intégrée d'une maison florentine au passage "
                "de la troisième génération — une refonte pensée pour préserver, "
                "non pour renouveler.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Année de livraison",
            "meta_label_team":       "Équipe du studio",
            "cover_image": "https://images.unsplash.com/photo-1586717791821-3f44a563fa4c?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "Le contexte",
                    "title": "Une <em>maison</em> sans manuel.",
                    "paragraphs": [
                        "Gentiluomo était une maison de maroquinerie fondée en 1967 "
                        "à Florence. À la troisième génération — deux sœurs, quarante "
                        "et trente-six ans — la communication était encore gérée comme "
                        "une urgence hebdomadaire. Pas de système, pas de règles, "
                        "pas d'archive.",
                    ],
                },
                {
                    "label": "La méthode",
                    "title": "Remonter <em>à 1967</em>, non à 2024.",
                    "paragraphs": [
                        "Nous avons passé cinq semaines aux archives à Florence, "
                        "reconstituant pièce par pièce l'identité historique — catalogues, "
                        "cartes, étiquettes, correspondance avec les boutiques. Le système "
                        "final n'est pas nouveau — c'est la première version documentée de "
                        "quelque chose qui existait depuis cinquante-sept ans.",
                    ],
                    "pullquote":
                        "La maison avait déjà une identité. Personne ne l'avait jamais écrite.",
                },
            ],
            "deliverables_label": "Livrables",
            "deliverables_heading": "Un <em>manuel gardien</em>, 240 pages.",
            "deliverables_intro":
                "Le manuel final a été signé par les deux sœurs et par le "
                "studio, en cérémonie privée à Florence en octobre 2024.",
            "deliverables": [
                ("01", "Reconstitution de l'archive historique",
                 "128 pièces cataloguées, numérisées, décrites. "
                 "Base documentaire pour chaque choix ultérieur."),
                ("02", "Système typographique historique + contemporain",
                 "Un serif italien redessiné à partir des étiquettes de 1971, "
                 "associé à un sans moderne pour la communication digitale."),
                ("03", "Manuel gardien",
                 "240 pages en italien + anglais, signé par les commanditaires. "
                 "Pensé pour être lu, non pour être consulté."),
            ],
            "press_quote":
                "Une refonte qui préserve au lieu de renouveler — une rareté à Florence.",
            "press_source":     "Monocle — Février 2025",
            "press_journalist": "Sophie Grove",
            "next_label":       "Cas suivant",
            "next_heading":     "Aller aux <em>archives des travaux</em> →",
            "cta_label":        "Maison & luxe",
            "cta_heading":      "Ouvrir le <em>dossier luxe</em> →",
        },
        {
            "slug": "triennale-milano-wayfinding",
            "index": "04",
            "title": "Un <em>wayfinding permanent</em> pour douze salles.",
            "client": "Triennale Milano — Parco Sempione",
            "discipline": "Identité spatiale",
            "year": "2024",
            "team": "Serafini · Boeri",
            "standfirst":
                "Le dessin d'un système de signalétique permanente pour les "
                "douze salles d'exposition de la Triennale — un système qui "
                "accompagne le visiteur sans parler plus qu'il ne le faut.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Année d'installation",
            "meta_label_team":       "Équipe du studio",
            "cover_image": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "Le projet",
                    "title": "Une <em>grammaire spatiale</em> pour vingt-deux mois de travail.",
                    "paragraphs": [
                        "La Triennale nous a confié la refonte du wayfinding "
                        "permanent en 2022. Vingt-deux mois de travail, douze salles, "
                        "quatre langues, deux parcours (visiteur + staff). Le système "
                        "a été installé en phases, sans jamais fermer au public.",
                    ],
                },
                {
                    "label": "Les règles",
                    "title": "Un caractère, trois tailles, deux couleurs.",
                    "paragraphs": [
                        "Nous avons travaillé par soustraction : un seul caractère (dessiné "
                        "spécialement), trois dimensions (directionnelle / informative / "
                        "cartel), deux couleurs (noir + ocre). La traduction en arabe "
                        "et en chinois a été confiée à des consultants linguistiques dédiés.",
                    ],
                },
            ],
            "deliverables_label": "Livrables",
            "deliverables_heading": "Un <em>système</em>, 420 éléments.",
            "deliverables_intro":
                "L'installation a été suivie sur chantier par Margherita "
                "Serafini pendant trois semaines consécutives.",
            "deliverables": [
                ("01", "Caractère typographique exclusif",
                 "Triennale Display — dessiné par le studio, "
                 "licencié exclusivement à la Triennale."),
                ("02", "420 éléments de signalétique",
                 "De la grande directionnelle extérieure au cartel de vitrine. "
                 "Quatre langues, deux parcours."),
                ("03", "Manuel de gestion",
                 "Document opérationnel pour l'équipe interne : quoi maintenir, "
                 "quand remplacer, comment commander de nouveaux éléments."),
            ],
            "press_quote":
                "Un wayfinding qui n'impose rien — il vous laisse marcher.",
            "press_source":     "Abitare — Mars 2025",
            "press_journalist": "Filippo Romano",
            "next_label":       "Cas suivant",
            "next_heading":     "Aller aux <em>archives des travaux</em> →",
            "cta_label":        "Systèmes spatiaux",
            "cta_heading":      "Ouvrir le <em>dossier wayfinding</em> →",
        },
        {
            "slug": "museo-900-manifesti",
            "index": "05",
            "title": "Une <em>série d'affiches</em> d'auteur pour douze expositions.",
            "client": "Museo del Novecento — Milan",
            "discipline": "Direction artistique",
            "year": "2024",
            "team": "Boeri · Ferri",
            "standfirst":
                "La direction artistique d'une saison d'affiches pour les "
                "expositions temporaires du Musée, avec commandes à des photographes "
                "italiens émergents.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Année de la saison",
            "meta_label_team":       "Équipe du studio",
            "cover_image": "https://images.unsplash.com/photo-1561070791-2526d30994b8?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "L'idée",
                    "title": "Une <em>affiche</em>, un <em>auteur</em>.",
                    "paragraphs": [
                        "Au lieu de produire des affiches en interne au studio, nous avons "
                        "commandé à douze photographes italiens émergents — un par "
                        "exposition — en demandant à chacun une image en réponse à l'œuvre "
                        "centrale de l'exposition.",
                    ],
                },
                {
                    "label": "Le résultat",
                    "title": "Douze voix <em>distinctes</em>, une seule grille.",
                    "paragraphs": [
                        "La grille typographique est restée constante — même titre, "
                        "même crédit, même format. La variation vit entièrement "
                        "dans l'image. Le visiteur perçoit la cohérence de la "
                        "saison, mais chaque affiche est un choc autonome.",
                    ],
                },
            ],
            "deliverables_label": "Livrables",
            "deliverables_heading": "Une <em>saison</em>, douze affiches.",
            "deliverables_intro":
                "Le projet a remporté la Mention ADI Design Index 2024.",
            "deliverables": [
                ("01", "Commande photographique",
                 "Douze photographes italiens émergents choisis parmi les finalistes "
                 "du Prix Graziadei 2023."),
                ("02", "Grille typographique saisonnière",
                 "Un dessin d'affiche qui tient douze images différentes "
                 "sans compromis."),
                ("03", "Catalogue de la saison",
                 "Recueil en édition limitée (500 exemplaires) signé par les douze "
                 "photographes + entretien avec le commissaire."),
            ],
            "press_quote":
                "Des affiches qui ne font pas la publicité de l'exposition — elles l'accompagnent.",
            "press_source":     "Eye Magazine — Été 2024",
            "press_journalist": "John L. Walters",
            "next_label":       "Cas suivant",
            "next_heading":     "Aller aux <em>archives des travaux</em> →",
            "cta_label":        "Direction artistique",
            "cta_heading":      "Ouvrir le <em>dossier saisonnier</em> →",
        },
        {
            "slug": "villa-necchi-sei-cuvee",
            "index": "06",
            "title": "Un <em>packaging</em> pour six cuvées, six auteurs.",
            "client": "Villa Necchi Winery — Valpolicella",
            "discipline": "Packaging d'auteur",
            "year": "2023",
            "team": "Serafini · Boeri",
            "standfirst":
                "Le dessin de six étiquettes pour les six cuvées historiques "
                "de la cave, chacune signée par un auteur littéraire "
                "italien contemporain.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Année du tirage",
            "meta_label_team":       "Équipe du studio",
            "cover_image": "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "Le projet",
                    "title": "Un <em>vin</em>, un <em>texte</em>, une étiquette.",
                    "paragraphs": [
                        "Six cuvées historiques de Villa Necchi. Six auteurs italiens "
                        "contemporains, invités à écrire un bref texte (max 120 mots) "
                        "en réponse au vin qu'ils avaient dégusté. Les textes ont été "
                        "ensuite intégrés typographiquement dans l'étiquette.",
                    ],
                },
                {
                    "label": "Les auteurs",
                    "title": "Six voix <em>très différentes</em>.",
                    "paragraphs": [
                        "Nous avons choisi délibérément six registres différents : une poète "
                        "sicilienne, un romancier milanais, une critique littéraire, "
                        "un auteur de nouvelles brèves, un traducteur du japonais, "
                        "une auteure de non-fiction. Chaque texte a sa typographie.",
                    ],
                },
            ],
            "deliverables_label": "Livrables",
            "deliverables_heading": "Six <em>étiquettes</em>, six typographies.",
            "deliverables_intro":
                "La série a été vendue en coffret de six bouteilles "
                "en édition limitée (1200 coffrets).",
            "deliverables": [
                ("01", "Six étiquettes d'auteur",
                 "Imprimées à Vérone sur papier Amatruda, "
                 "avec double ennoblissement (debossed + dorure)."),
                ("02", "Coffret en bois",
                 "Dessiné avec un menuisier de Valpolicella, "
                 "numéroté et signé par la cave."),
                ("03", "Livret des textes",
                 "Recueil des six textes originaux en édition italienne + "
                 "traduction anglaise, relié au fil."),
            ],
            "press_quote":
                "Un projet qui lie le vin à la littérature sans forcer l'analogie. Courageux.",
            "press_source":     "Gambero Rosso — Janvier 2024",
            "press_journalist": "Marco Sabellico",
            "next_label":       "Cas suivant",
            "next_heading":     "Aller aux <em>archives des travaux</em> →",
            "cta_label":        "Packaging d'auteur",
            "cta_heading":      "Ouvrir le <em>dossier packaging</em> →",
        },
    ],
}
