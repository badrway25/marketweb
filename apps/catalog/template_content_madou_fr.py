"""Content tree · `madou-pasticceria` · T50 multilingual rollout (FR).

French translation of `MADOU_CONTENT_IT`. Built for the marketweb T50
multilingual pass (IT → EN/FR/ES/AR · AAA walk · public flip). Shape
parity contract enforced against `template_content_madou.py`:

  * Same top-level keys, same nested keys at every depth.
  * Same list lengths (5 lievitati signature courses, 8 menu courses,
    4 produttori, 4 atmosphere images, 4 riconoscimenti, etc.).
  * Same tuple positions for tuple-typed values.
  * Same `pages[].slug` values (labels translated, slugs preserved).
  * Same `posts[].slug` values, same `page kind`.

Voice anchor — `longue pousse` (pâtisserie-craft register · Cyril
Lignac / Christophe Felder / L'École Lenôtre / Atelier Pâtisserie
artisan-baker idiom · the term Mof and CAP pâtissier holders use
for slow-leavening laminated dough) carries the IT
`lievitazione lenta` load-bearing promise across the same surfaces
(hero H1 with `<em>` italic emphasis, manifesto, cta_heading, forno
headline/values, pasticceria intro, ordina, produttori + signature
courses copy). A secondary `pousse lente` synonym variant is used
where the noun-em form would feel repetitive. Italian/French
heritage proper-names (Torino, Borgo Po, Pierre Marchais, Famiglia
Brero, Olivier Domori, Anna Negroni, Carla Madou, Tommaso Rinaldi,
Iginio Massari, Pierre Hermé, Cristian Beduschi, Cuneo IGP, Val Susa,
Isigny-sur-Mer, Sambirano, Mortara, Domori Criollo, Marrone IGP,
Nocciola Piemonte IGP, Gambero Rosso Pasticcerie, AMPI, Coppa del
Mondo Pasticceria, Identità di Pasticceria, Dissapore, Cook Corriere,
Vogue Cibo, Erbaluce passito Cieck, Caffè Vergnano, Damman, Inalpi,
Caffè Al Bicerin) preserved verbatim. Brand `Madou · Pasticceria
Atelier` preserved (NOT translated to «Pâtisserie Atelier»). Pastry
product names (Croissant viennoise, Maritozzo, Millefoglie, Bignè,
Saint-Honoré, Mont-Blanc, Tarte au chocolat, Macarons, Pasta sfoglia,
Bicerin) kept as international pâtisserie register. Carla Madou
addressed as `pâtissière` (feminine) throughout. Espaces insécables
(U+00A0) before `;` `:` `?` `!` `»` and inside `« »` quotes per
French typographic rule.
"""

from typing import Any


MADOU_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",         "label": "Accueil",        "kind": "home"},
        {"slug": "forno",        "label": "Le fournil",     "kind": "about"},
        {"slug": "pasticceria",  "label": "Pâtisserie",     "kind": "menu"},
        {"slug": "vetrina",      "label": "Vitrine",        "kind": "gallery"},
        {"slug": "diario",       "label": "Journal",        "kind": "blog_list"},
        {"slug": "ordina",       "label": "Commandes",      "kind": "reservations"},
    ],

    "site": {
        "logo_initial":  "MD",
        "logo_word":     "Madou",
        "tag":           "Pasticceria Atelier · Torino Borgo Po · depuis 2011",
        "phone":         "+39 011 8195 770",
        "email":         "atelier@madou-pasticceria.it",
        "address":       "Via Sant'Ottavio 36 · 10124 Torino",
        "hours_compact": "Mar – Sam · 7 h 30 – 19 h 30 · Dim 7 h 30 – 13 h 00",
        "star_line":     "★ Tre Torte · Gambero Rosso · 2023 · 2024 · 2025",
        "footer_intro":
            "Quinze ans de longue pousse. Un atelier ouvert sur la rue, "
            "une vitrine de pâte crue, deux fours à sole réfractaire. "
            "Aucun pré-mélange industriel, aucun surgelé, aucune précipitation.",
        "footer_hours_1": "Mar – Sam · 7 h 30 – 19 h 30",
        "footer_hours_2": "Dim · 7 h 30 – 13 h 00 · Lun · repos",
        "copyright": "© 2026 Madou Atelier S.r.l. · TVA 11237680016",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        # T49: hero plate URL threaded into the fine-dining template via
        # page_data so Madou swaps Gusto's plated-dish hero for the
        # pasticceria vetrina without forking home.html. URL from X.3
        # curator pack `bakery-pasticceria.md` (Pexels CC0-compatible).
        "hero_plate_url":
            "https://images.pexels.com/photos/19288569/pexels-photo-19288569.jpeg"
            "?auto=compress&cs=tinysrgb&w=1600",
        "eyebrow":  "Pasticceria Atelier · Torino Borgo Po · depuis 2011",
        "headline": "Douze heures de <em>longue pousse,</em> un feuilletage qui se laisse écouter.",
        "intro":
            "Pâtes feuilletées laminées à froid, levain naturel rafraîchi "
            "toutes les douze heures, crèmes montées à la minute. La "
            "vitrine change chaque jour selon ce qui est sorti du four "
            "à l'aube.",
        "primary_cta":   "Précommandez le feuilleté du samedi",
        "primary_href":  "ordina",
        "secondary_cta": "La pâtissière",
        "secondary_href":"forno",

        # Repurposed labels (Gusto's "chef" → Madou's "pasticciera")
        "chef_label":    "La pâtissière",
        "star_tag":      "★ Tre Torte · Gambero Rosso 2025",
        "photo_label":   "Photographie",
        "cuisine_label": "Pâtissière",

        "facts": [
            ("12 h", "longue pousse minimale · pâte feuilletée"),
            ("3",    "levains mères vivants à l'atelier · depuis 2011"),
            ("0",    "pré-mélanges industriels · 0 surgelés · 0 mix"),
        ],

        "manifesto_drop_cap": "Q",
        "manifesto":
            "uand une plaque de feuilletage entre au four, chez Madou le "
            "travail s'interrompt pendant quatre minutes et l'on écoute. Le "
            "bruit de la pâte qui gonfle — les bulles d'air qui se libèrent "
            "entre les 64 feuilles de pâte laminée — est le premier indice "
            "indiquant si ce lot sera vendu samedi matin ou s'il ira à la "
            "brigade. Pas de chronomètre, pas de thermomètre : seulement "
            "l'oreille.",

        # Pasticceria signature — 5 "lievitati" (vs Gusto 5 "atti")
        "signature_courses": [
            ("I",    "Croissant viennoise",           "12 heures de longue pousse · 64 feuilles · beurre normand d'Isigny",            "Café monorigine Éthiopie Sidamo"),
            ("II",   "Maritozzo à la crème",          "longue pousse naturelle de 24 heures · crème fraîche montée à la minute",      "Chocolat chaud Madagascar 72 %"),
            ("III",  "Millefoglie à la noisette",     "trois feuilles de feuilletage caramélisé · chantilly à la Nocciola IGP",       "Bicerin traditionnel torinois"),
            ("IV",   "Bignè au chocolat Domori",      "pâte à choux maison · ganache noire Criollo 80 %",                              "Thé noir Darjeeling First Flush"),
            ("V",    "Saint-Honoré aux marrons",      "saisonnier automne · marrons de Cuneo IGP · crème mousseline",                  "Vin doux Erbaluce passito"),
        ],

        # Persona — pasticciera Carla Madou
        "chef": {
            "name":  "Carla Madou",
            "role":  "Pâtissière de l'atelier · née en 1979",
            "bio":
                "Torinoise, née en 1979. Quatre années d'apprentissage chez "
                "Iginio Massari à Brescia, puis deux années chez Pierre Hermé "
                "à Paris, enfin deux chez Cristian Beduschi à Genève. Elle "
                "ouvre Madou en 2011 dans une ancienne imprimerie de Borgo "
                "Po, avec une seule intuition : ne travailler qu'avec des "
                "levains mères vivants, rafraîchis toutes les douze heures.",
        },

        "courses_label": "Cinq feuilletés de la semaine · octobre '26",
        "courses_footline": "Vitrine vivante — ce que vous voyez est sorti du four ce matin",
        "courses_full_cta": "Toute la pâtisserie",
        "chef_link_filosofia": "Le fournil et les mains",
        "chef_link_diario": "Le journal de farine",

        "press_label": "Parue dans",
        "press": ["GAMBERO ROSSO PASTICCERIE", "DISSAPORE", "COOK CORRIERE",
                  "IDENTITÀ DI PASTICCERIA", "VOGUE CIBO"],

        # Ingredients/sourcing editorial band — pasticceria-specific
        "ingredienti": {
            "label":   "Matière première",
            "heading": "Seize fournisseurs, <em>tous par leur nom.</em>",
            "text":
                "La filière Madou est courte et traçable ligne par ligne. Le "
                "beurre arrive d'une laiterie normande d'Isigny-sur-Mer · les "
                "œufs d'une ferme à soixante kilomètres de Torino · les "
                "farines d'un moulin à meule de pierre du Val Susa · le cacao "
                "de trois plantations single-origin (Madagascar, Venezuela, "
                "République dominicaine) sélectionnées sur le terrain en 2019.",
            "image":
                "https://images.pexels.com/photos/28183472/pexels-photo-28183472.jpeg"
                "?auto=compress&cs=tinysrgb&w=1000",
            "image_caption":
                "Pâte laminée sur le marbre réfrigéré · service de 5 h 30 du matin",
        },

        # Atmosphere teaser — pasticceria-specific imagery
        "atmosphere_teaser": {
            "label": "La vitrine vivante",
            "images": [
                ("https://images.pexels.com/photos/19288569/pexels-photo-19288569.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "La vitrine du samedi matin"),
                ("https://images.pexels.com/photos/16140003/pexels-photo-16140003.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Décor à la main · gâteau de confection à la commande"),
                ("https://images.pexels.com/photos/30853716/pexels-photo-30853716.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Croissants viennoise tout juste sortis du four"),
                ("https://images.pexels.com/photos/31000323/pexels-photo-31000323.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Macarons saisonniers · octobre '26"),
            ],
            "link_label": "Entrer dans la vitrine",
            "link_href":  "vetrina",
        },

        # Awards/recognition — pastry awards (not Michelin)
        "riconoscimenti": {
            "label": "Distinctions",
            "items": [
                ("★★★", "Tre Torte · Gambero Rosso", "Prix annuel · 2023 · 2024 · 2025"),
                ("AMPI", "Accademia Maestri Pasticceri", "Membre depuis 2017 · siège de Brescia"),
                ("CMP",  "Coppa del Mondo Pasticceria", "Équipe d'Italie · suppléante 2022 · 4ᵉ place à Lyon"),
                ("DIS",  "Dissapore · 50 Pasticcerie", "Première place Piémont 2024 · top 5 Italie 2025"),
            ],
        },

        # CTA section
        "cta_heading": "Rien que la longue pousse, <em>rien que ce qui sort du four au matin.</em>",
        "cta_primary":  "Précommandez le feuilleté du samedi",
        "cta_secondary": "Découvrez toute la pâtisserie",

        # Seasonal highlight card — pasticceria seasonal
        "stagione": {
            "label":     "En vitrine maintenant",
            "title":     "Pâtisserie automne '26",
            "subtitle":  "Marrons, kaki, chocolat monorigine · à partir du 6 octobre",
            "text":
                "La carte d'automne s'ouvre le 6 octobre avec le Saint-Honoré "
                "aux marrons de Cuneo IGP, la millefoglie au kaki astringent "
                "du Bel Paese et le Mont-Blanc 2026 en version individuelle. "
                "Toute la pâtisserie automnale reste en vitrine jusqu'au 30 "
                "novembre, puis l'on passe à Noël.",
            "cta_label": "Découvrez toute la carte d'automne →",
            "cta_href":  "pasticceria",
        },

        # Producer showcase — pastry supply chain (vs Gusto wine producers)
        "produttori": {
            "label":   "Les fournisseurs",
            "heading": "Seize mains, <em>une seule vitrine.</em>",
            "intro":
                "Chaque matière première Madou a un fournisseur avec un nom, "
                "une adresse et un numéro de téléphone. Beurre, lait, œufs, "
                "farines, cacao, fruits, miel — rien ne vient de catalogue. "
                "Tous les fournisseurs ont été visités personnellement par "
                "Carla au moins une fois.",
            "items": [
                {
                    "portrait":
                        "https://images.pexels.com/photos/8477754/pexels-photo-8477754.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Pierre Marchais",
                    "role": "Beurre normand AOP",
                    "area": "Isigny-sur-Mer · Normandie",
                    "blurb":
                        "Le beurre Isigny AOP arrive chaque mercredi en "
                        "transport réfrigéré à 4 °C. Laiterie familiale "
                        "depuis 1932, quatre vaches normandes à l'hectare.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/8188937/pexels-photo-8188937.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Famiglia Brero",
                    "role": "Moulin à meule de pierre · Val Susa",
                    "area": "Bussoleno · Piémont",
                    "blurb":
                        "Mouture à la pierre en trois passes · blé tendre "
                        "Bologna 100 % local · aucun raffinage. Trois "
                        "farines, une par mois en exclusivité, qui portent "
                        "la longue pousse de l'atelier.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/11869895/pexels-photo-11869895.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Olivier Domori",
                    "role": "Cacao single-origin",
                    "area": "Sambirano · Madagascar",
                    "blurb":
                        "Trois plantations sélectionnées sur le terrain par "
                        "Carla en 2019. Cacao Criollo trinitario à 80 %, "
                        "torréfaction à froid en Italie · lot tracé "
                        "individuellement.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/29198586/pexels-photo-29198586.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Anna Negroni",
                    "role": "Fruits de saison · Cuneo",
                    "area": "Lagnasco · Piémont",
                    "blurb":
                        "Pêches de Cuneo IGP en juin · marrons IGP en "
                        "octobre · kakis astringents en novembre. Huit "
                        "hectares, cueillette à la main, aucune chambre "
                        "froide.",
                },
            ],
        },

        # Repurposed `private_dining` → `eventi su misura` / cake design
        "private_dining": {
            "label":   "Événements sur mesure",
            "heading": "Cake design & <em>commandes privées.</em>",
            "intro":
                "Chez Madou, l'on peut commander des gâteaux de cérémonie, "
                "des wedding cakes et de petites productions privées pour "
                "des événements. Trois voies d'entrée, chacune avec ses "
                "délais et ses tarifs.",
            "experiences": [
                {
                    "icon": "fork",
                    "title": "Gâteau sur commande",
                    "meta":  "Min. 8 parts · à partir de 18 € / part",
                    "desc":
                        "Dessin personnalisé construit sur trois rendez-vous "
                        "préliminaires avec Carla. Délai de livraison : "
                        "deux semaines minimum. Nous ne décorons qu'à la "
                        "main, aucun moule industriel.",
                },
                {
                    "icon": "door",
                    "title": "Wedding cake",
                    "meta":  "À partir de 40 parts · 22 € / part",
                    "desc":
                        "Quatre mois de travail à quatre mains avec le "
                        "couple. Trois essais de dégustation inclus dans "
                        "la prestation. Retrait à l'atelier ou livraison "
                        "réfrigérée prise en charge par Madou dans le "
                        "Piémont central.",
                },
                {
                    "icon": "wine",
                    "title": "Buffet privé",
                    "meta":  "20 – 60 convives · à partir de 38 € / convive",
                    "desc":
                        "Pâtisserie mignon uniquement · 8 références, "
                        "150 pièces minimum. Cuisson le jour de l'événement, "
                        "livraison réfrigérée. Les samedis après-midi, "
                        "nous les gardons libres.",
                },
            ],
            "cta_label": "Écrivez à la pâtissière",
            "cta_href":  "ordina",
        },

        # Repurposed `wine_program` → `lieviti madre` collection
        "wine_program": {
            "label":   "L'archive des levains",
            "heading": "Trois levains mères vivants, <em>une seule pâtisserie.</em>",
            "intro":
                "L'atelier conserve trois levains mères actifs, chacun "
                "avec sa propre signature d'acidité et son propre "
                "rendement. Chaque feuilleté Madou est associé au levain "
                "qui lui appartient — pas de levure de boulanger, pas "
                "d'améliorants.",
            "sommelier": {
                "name": "Tommaso Rinaldi",
                "role": "Maître levainier · responsable des levains mères",
                "bio":
                    "Apprenti de Carla depuis 2014, responsable du "
                    "rafraîchissement des trois levains mères depuis 2018. "
                    "Il rafraîchit toutes les douze heures, à 5 h 30 et à "
                    "17 h 30. Il conserve la mémoire de farine de chaque "
                    "fournée.",
            },
            "pairings": [
                ("01", "Mère M-1 · feuilletage laminé",
                 "Levain actif depuis 2011 · acidité lactique dominante · "
                 "pH 4,2 · tours rapides, repos long. Utilisé pour les "
                 "croissants, le kouign-amann, la brioche col tuppo.",
                 "12 – 16 h"),
                ("02", "Mère M-2 · panettoni et pâtes levées hautes",
                 "Mère née en 2014 d'un rafraîchissement à triple. "
                 "Acidité mixte acétique-lactique, pH 4,5 · développement "
                 "vertical agressif. Panettone, colomba et veneziana "
                 "uniquement.",
                 "36 – 48 h"),
                ("03", "Mère M-3 · pain brioché et feuilletés sucrés",
                 "Mère rafraîchie au miel de châtaignier · acidité "
                 "contenue, pH 4,7 · parfum de noisette torréfiée. "
                 "Maritozzi, brioches rondes, tresse au chocolat.",
                 "8 – 12 h"),
            ],
            "cellar_facts": [
                ("3",   "levains mères vivants"),
                ("12h", "fréquence de rafraîchissement fixe"),
                ("2011", "année de la première mère · M-1"),
            ],
        },
    },

    # ─── FORNO (about) — Gusto's "filosofia" page ────────────
    "forno": {
        "eyebrow":  "Le fournil",
        "headline": "Quinze ans de fournil, <em>une seule promesse de longue pousse.</em>",
        "intro":
            "Madou est né en 2011 dans une ancienne imprimerie de Borgo Po, "
            "à Torino. L'atelier possède une seule salle de travail ouverte "
            "sur la rue et deux fours à sole réfractaire. La promesse est "
            "toujours la même : zéro pré-mélange, zéro surgelé, zéro mix "
            "industriel. Rien que la longue pousse, rien que des matières "
            "premières tracées.",

        "history": [
            ("2011",
             "Carla Madou ouvre l'atelier via Sant'Ottavio après huit années "
             "passées entre Brescia (Massari), Paris (Hermé) et Genève "
             "(Beduschi). Quatre places au comptoir, deux références de "
             "pâtisserie, une seule mère — M-1, fondée avec la farine du "
             "moulin Brero."),
            ("2014",
             "Tommaso Rinaldi entre comme apprenti et devient en trois ans "
             "responsable des levains mères. M-2, la mère des panettoni, "
             "naît d'un rafraîchissement à triple de M-1."),
            ("2017",
             "Carla est admise à l'Accademia Maestri Pasticceri Italiani "
             "(AMPI), deuxième femme piémontaise à y entrer après Sonia "
             "Balacchi."),
            ("2021",
             "Transfert de l'atelier au 36 via Sant'Ottavio, l'ancienne "
             "imprimerie entièrement réhabilitée. Trois fours, deux "
             "lamineurs, une vitrine de quinze mètres linéaires ouverte "
             "sur la rue."),
            ("2023",
             "Gambero Rosso décerne les Tre Torte (la plus haute "
             "distinction pâtissière) et le confirme en 2024 et en 2025. "
             "Madou devient une étape obligée du circuit des pâtisseries "
             "d'auteur italiennes."),
        ],

        "filosofia_image":
            "https://images.pexels.com/photos/30918889/pexels-photo-30918889.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400",
        "filosofia_image_caption": "Le laboratoire · Carla Madou au lamineur",

        "method_title": "Méthode",
        "method_paragraphs": [
            "Toute la pâtisserie Madou part du rafraîchissement de la mère. "
            "À 5 h 30 du matin, Tommaso rafraîchit les trois levains mères "
            "et prélève les quantités pour les pétrissages du jour · à "
            "17 h 30, il rafraîchit à nouveau pour les pétrissages "
            "nocturnes. C'est un horaire fixe, indépendant de Noël, de "
            "Pâques ou du 15 août.",
            "Les feuilletages laminés sont préparés la veille au soir et "
            "reposent en chambre à 4 °C pendant douze heures minimum, "
            "seize heures pour les lots du samedi. Le beurre est battu à "
            "froid · le sel de Mothia est ajouté en paillettes · les tours "
            "sont toujours quatre, jamais trois · le cycle final de "
            "laminage produit 64 feuilles de pâte visibles à la coupe.",
            "Les crèmes se préparent à vue, montées à la minute. Aucune "
            "pâtisserie Madou ne quitte le comptoir avec une crème "
            "préparée plus de deux heures auparavant · les pâtes sablées "
            "sont coupées à la main · les ganaches sont émulsionnées au "
            "fouet au passage suivant. Travailler à la minute est la "
            "raison pour laquelle nous ne vendons pas de cake design "
            "sans préavis.",
        ],

        "values_label": "Ce que nous garantissons",
        "values_heading": "Quatre promesses <em>non négociables</em>.",
        "values": [
            ("Temps",        "Douze heures de longue pousse minimum · seize pour le samedi."),
            ("Filière",      "Seize fournisseurs, tous rencontrés en personne au moins une fois."),
            ("Transparence", "Aucun mix, aucun améliorant, aucun surgelé."),
            ("Main",         "Décor à la main · crèmes montées à la minute · aucun moule industriel."),
        ],

        "cta_heading": "Voulez-vous voir la <em>pâtisserie de la semaine en cours ?</em>",
        "cta_menu": "Cinq feuilletés d'octobre '26",
        "cta_prenota": "Précommandez le feuilleté du samedi",
    },

    # ─── PASTICCERIA (menu) — Gusto's "menu" page ────────────
    "pasticceria": {
        "eyebrow":  "La carte de la semaine",
        "headline": "Vitrine vivante — <em>automne '26</em>",
        "intro":
            "La pâtisserie Madou change chaque semaine selon la fournée du "
            "lundi soir. Ce qui suit est la carte en vigueur du 6 au 12 "
            "octobre 2026 · vitrine ouverte du mardi au samedi, dimanche "
            "matin uniquement, lundi repos. La longue pousse demeure la "
            "seule règle.",
        "courses_label": "Cinq feuilletés · octobre '26",

        "courses": [
            ("I",     "Croissant viennoise",
             "Pâte feuilletée en longue pousse 12 heures · beurre normand "
             "AOP d'Isigny · 64 feuilles visibles à la coupe · dorure au "
             "jaune d'œuf entier · sucre glace de Mothia poudré à la "
             "sortie du four.",
             "Café monorigine Éthiopie Sidamo · Caffè Vergnano pour Madou"),
            ("II",    "Maritozzo à la crème",
             "Pâte à brioche en longue pousse 24 heures avec M-3 · crème "
             "fraîche de la laiterie Inalpi montée à la minute · vanille "
             "Tahitian entière de Madagascar · sucre filé en couronne.",
             "Chocolat chaud Madagascar Domori 72 %"),
            ("III",   "Millefoglie à la noisette",
             "Trois feuilles de feuilletage caramélisé · chantilly à la "
             "Nocciola Piemonte IGP du moulin Brero · brisures de noisette "
             "torréfiées sur la sole réfractaire.",
             "Bicerin traditionnel torinois · recette historique du Caffè "
             "Al Bicerin"),
            ("IV",    "Bignè au chocolat Domori",
             "Pâte à choux maison · ganache noire au cacao Criollo Domori "
             "80 % · brillance au sirop de glucose · finition à la poche · "
             "sucre glace à volonté.",
             "Thé noir Darjeeling First Flush · sélection Damman 2026"),
            ("V",     "Saint-Honoré aux marrons",
             "Automne uniquement · bignè garnis de mousseline au marron · "
             "marrons IGP de Cuneo du champ d'Anna Negroni · base de pâte "
             "feuilletée · couronne de sucre filé doré.",
             "Erbaluce di Caluso passito · sélection Cieck · 50 cl au verre"),
            ("VI",    "Mont-Blanc 2026",
             "Vermicelles de marrons IGP de Mortara · chantilly vanille · "
             "cœur de meringue française cuite à 90 °C pendant quatre "
             "heures · finition à la passe-main.",
             "Café turc au cardamome vert · service en cafetière de cuivre"),
            ("VII",   "Tarte au chocolat Sambirano",
             "Pâte sablée au cacao 22 % · ganache noire Madagascar "
             "Sambirano 72 % · sel de Mothia en paillettes · finition à "
             "l'huile d'olive vierge extra de Taggia.",
             "—"),
            ("VIII",  "Macarons de saison",
             "Six macarons saisonniers · safran des Abruzzes, framboise du "
             "Roero, châtaigne de Cuneo, chocolat Sambirano, vanille "
             "Tahitian, olive taggiasca · cuisson à 165 °C pendant 12 "
             "minutes.",
             "Thé blanc Pai Mu Tan · sélection Damman"),
        ],

        # Wine_program → repurposed as caffè & tisaneria
        "wine_intro_title": "Caféterie & théière",
        "wine_intro":
            "Chez Madou, chaque feuilleté est associé à un café monorigine "
            "torréfié à Torino par Vergnano ou à une infusion sélectionnée "
            "par Damman. La carte des thés et des cafés est complète, les "
            "accords sont laissés à la discrétion du comptoir — demandez à "
            "Tommaso au moment du passage en caisse.",

        "wine_highlights": [
            ("Café monorigine",        "8 origines · Éthiopie, Brésil, Colombie, Guatemala, Vietnam, Sambirano"),
            ("Thés noirs & verts",     "22 sélections Damman · Darjeeling, Ceylan, Sencha, Genmaicha"),
            ("Chocolats chauds",       "6 origines · Madagascar, Venezuela, Équateur, République dominicaine, Tanzanie, Ghana"),
            ("Boissons traditionnelles", "Bicerin · vin chaud à la cannelle · ponce à la mandarine · sabayon"),
        ],

        "footer":
            "Vitrine ouverte du mardi au samedi · précommande du samedi "
            "conseillée à partir du mercredi. Le feuilleté du samedi "
            "s'épuise régulièrement avant 11 h 00. Pour les commandes "
            "supérieures à 12 pièces, écrivez à atelier@madou-"
            "pasticceria.it au moins 48 heures à l'avance.",
    },

    # ─── VETRINA (gallery) — Gusto's "atmosfera" ─────────────
    "vetrina": {
        "eyebrow":  "La vitrine",
        "headline": "Quinze mètres de vitrine, <em>une seule vitrine.</em>",
        "intro":
            "Madou occupe une ancienne imprimerie de la via Sant'Ottavio · "
            "la vitrine est ouverte sur la rue sur quinze mètres linéaires "
            "et laisse voir tout le laboratoire. Aucun mur entre le four "
            "et le trottoir de Borgo Po.",

        "rooms": [
            ("La vitrine de rue",
             "Quinze mètres de vitrine le long de la via Sant'Ottavio · "
             "exposition sur deux niveaux · réfrigération à +4 °C pour "
             "les crèmes · vitrine sèche à +18 °C pour les feuilletés."),
            ("La salle de travail à vue",
             "L'atelier véritable — quatre postes : feuilletage, levains, "
             "crèmes, décoration. Toute la pâtisserie se voit en temps "
             "réel depuis la vitrine · aucune cuisine cachée."),
            ("La salle de dégustation",
             "Huit places au comptoir, face au lamineur. Ouverte "
             "uniquement pour les dégustations guidées du jeudi "
             "après-midi · trois heures avec Carla, six feuilletés, "
             "trois cafés monorigine."),
            ("La cour de l'ancienne imprimerie",
             "De mai à septembre, quatre tables en plein air sous la "
             "glycine de l'ancienne imprimerie. Ouvertes seulement au "
             "petit-déjeuner · menu fixe du lundi, croissant + bicerin."),
        ],

        "captions": [
            "La vitrine du samedi matin · mise en place à 7 h 30.",
            "Décor à la main · wedding cake automne '26.",
            "Les croissants viennoise tout juste sortis du four à 6 h 00.",
            "Les macarons d'octobre '26 · six parfums saisonniers.",
            "Carla Madou au lamineur · pâte feuilletée de 5 h 30.",
            "Le comptoir au passage du premier client · mardi 7 h 30.",
        ],

        "cta_quote": "« Aucun mur entre le four et le trottoir de Borgo Po. »",
        "cta_desc": "Vitrine ouverte Mar – Sam · 7 h 30 – 19 h 30 · Dim 7 h 30 – 13 h 00 · Lun repos.",
        "cta_primary": "Précommandez le feuilleté du samedi",
        "cta_secondary": "Voir toute la pâtisserie",
    },

    # ─── DIARIO (blog list / detail) ──────────────────────────
    "diario": {
        "eyebrow":  "Le journal de farine",
        "headline": "Notes de fournil, <em>de levain,</em> de laboratoire.",
        "intro":
            "Brèves notes de Carla Madou et de Tommaso Rinaldi sur les "
            "longues pousses en cours, sur les matières premières "
            "saisonnières, sur les plus belles pâtisseries et sur ce qui "
            "ne fonctionne pas en pâtisserie d'une semaine à l'autre.",
        "read_article": "Lire l'article",
        "min_label": "min",
        "min_read_label": "min de lecture",
        "crumb_label": "Journal",
        "back_link": "← Tout le journal",
        "footer_label": "Madou Pasticceria Atelier · Le journal de farine",
        "empty_body": [
            "Article en préparation éditoriale. La publication intégrale "
            "sera disponible sous peu, rédigée personnellement par la "
            "pâtissière ou par le maître levainier.",
            "Ce repère décrit la voix du Journal de farine : brèves notes "
            "de travail, réflexions sur les levains mères, récits de "
            "pousses lentes qui tournent mal. Jamais plus de deux mille "
            "mots, jamais moins de cinq cents.",
        ],
    },

    "posts": [
        {
            "slug":     "vetrina-autunno-26",
            "kicker":   "Vitrine en cours",
            "title":    "Les cinq idées de la vitrine automne '26",
            "date":     "6 octobre 2026",
            "read_min": 5,
            "author":   "Carla Madou",
            "lede":
                "La nouvelle carte est entrée en vitrine hier soir. Cinq "
                "feuilletés, deux relectures de classiques de la pâtisserie "
                "torinoise et une pâte feuilletée que j'ai poursuivie "
                "pendant trois ans.",
            "body": [
                ("p", "Construire une vitrine d'automne est moins une "
                      "affaire de recettes qu'une affaire de durées de "
                      "pousse lente. La température de la chambre baisse, "
                      "les levains ralentissent · les mères répondent plus "
                      "lentement. Pour la carte automne '26, nous avons "
                      "travaillé deux semaines uniquement sur les temps de "
                      "repos du Saint-Honoré aux marrons."),
                ("h2", "Les cinq idées nouvelles"),
                ("p", "Le premier feuilleté, le Saint-Honoré aux marrons "
                      "de Cuneo, est une relecture du Saint-Honoré classique "
                      "français bâtie sur trois matières premières "
                      "piémontaises : marrons de Cuneo IGP du champ d'Anna "
                      "Negroni, crème fraîche de la laiterie Inalpi et "
                      "pâte feuilletée au beurre normand. J'en avais envie "
                      "depuis 2022, depuis mon passage à Lyon et la "
                      "dégustation de celui de Cyril Lignac · mais je "
                      "voulais une version torinoise, pas parisienne."),
                ("h2", "Les relectures"),
                ("p", "Le Mont-Blanc 2026 et le maritozzo à la crème sont "
                      "deux gâteaux auxquels je travaille depuis sept "
                      "années · aucun des deux ne naît en octobre, mais "
                      "c'est en octobre que leurs matières premières "
                      "respectives donnent le meilleur : les marrons de "
                      "Mortara pour le premier, la crème d'automne pour le "
                      "second. Le maritozzo, en particulier, je l'ai "
                      "changé sept fois en douze mois. Cette fois, il est "
                      "juste."),
                ("h2", "Une pâte feuilletée"),
                ("p", "Le croissant viennoise est la pièce dont je suis la "
                      "plus fière sur cette carte. C'est une pâte feuilletée "
                      "en longue pousse 12 heures en chambre à +4 °C, avec "
                      "du beurre Isigny AOP battu à froid et la farine du "
                      "moulin Brero. Soixante-quatre feuilles visibles à "
                      "la coupe, une bulle d'air tous les 0,4 millimètres "
                      "de pâte. C'est le feuilleté auquel je suis arrivée "
                      "après huit ans d'essais, et la seule raison pour "
                      "laquelle je suis là."),
                ("h2", "Ce qui sort le samedi"),
                ("p", "Le samedi, Madou produit 220 croissants viennoise "
                      "qui s'épuisent régulièrement avant 11 h 00. La "
                      "précommande à partir du jeudi est donc chaudement "
                      "conseillée — surtout dès octobre, lorsque la "
                      "demande remonte avec le premier froid."),
            ],
        },
        {
            "slug":     "lievito-madre-m2",
            "kicker":   "Levain mère",
            "title":    "Pourquoi nous avons attendu sept ans avant de faire le panettone",
            "date":     "28 septembre 2026",
            "read_min": 6,
            "author":   "Tommaso Rinaldi",
            "lede":
                "Madou n'a mis le panettone à la carte qu'en 2018, sept "
                "ans après l'ouverture. La raison est unique : la mère "
                "M-2 n'était pas prête. Voici pourquoi.",
            "body": [
                ("p", "Le panettone exige une mère des mères · beaucoup de "
                      "pâtissiers se fabriquent leur mère à l'ouverture de "
                      "leur pâtisserie, mais pour le panettone haut de "
                      "gamme il faut une mère qui ait travaillé au moins "
                      "trois ans, développé son profil acétique, trouvé "
                      "son équilibre. La M-1 de Madou — fondée en 2011 — "
                      "était une mère lactique, parfaite pour le "
                      "feuilletage mais peu agressive pour le panettone."),
                ("h2", "Comment naît la M-2"),
                ("p", "En 2014, j'ai prélevé un morceau de 200 grammes de "
                      "M-1 et je l'ai rafraîchi à triple pendant quarante "
                      "jours · toutes les douze heures, sans exception. "
                      "C'est ainsi que l'on « vire » une mère lactique "
                      "vers un profil mixte · c'est un procédé que j'ai "
                      "appris d'Achille Zoia. Après les quarante jours, "
                      "la mère était devenue suffisamment acétique pour "
                      "le panettone, mais encore trop jeune."),
                ("h2", "Quatre ans d'attente"),
                ("p", "De 2014 à 2018, j'ai rafraîchi la M-2 toutes les "
                      "douze heures sans en sauter une seule · ni à Noël, "
                      "ni en août. Carla l'appelait « la mère du futur » "
                      "parce que nous ne l'utilisions jamais. En novembre "
                      "2018, au septième essai, le panettone est sorti "
                      "comme il devait sortir. Depuis, la M-2 ne produit "
                      "que panettone, colomba et veneziana, rien d'autre."),
            ],
        },
    ],

    # ─── ORDINA (reservations) — Gusto's "prenota" ────────────
    "ordina": {
        "eyebrow":      "Commandes & confections",
        "headline":     "Précommandez le feuilleté du samedi.",
        "intro":
            "La vitrine du samedi s'épuise régulièrement avant 11 h 00. "
            "Pour vous assurer les feuilletés issus de la longue pousse, "
            "il convient de précommander dès le mercredi · retrait au "
            "comptoir de 7 h 30 à 13 h 00. Pour les gâteaux de confection "
            "à la commande et les wedding cakes, écrivez à atelier@madou-"
            "pasticceria.it au moins deux semaines à l'avance.",
        "primary_label":   "Que souhaitez-vous précommander ?",
        "primary_placeholder": "Samedi 18 octobre · 12 croissants viennoise + 4 maritozzi · retrait à 9 h 30",
        "name_label":      "Nom et prénom",
        "phone_label":     "Téléphone",
        "email_label":     "Courriel",
        "submit_label":    "Envoyer la précommande",
        "submit_note":     "Vous recevrez la confirmation du comptoir sous 24 h. La précommande se règle au retrait.",

        "contact_block": {
            "address_label": "Atelier",
            "address":       "Via Sant'Ottavio 36 · 10124 Torino · Borgo Po",
            "phone_label":   "Comptoir",
            "phone":         "+39 011 8195 770",
            "email_label":   "Courriel",
            "email":         "atelier@madou-pasticceria.it",
            "hours_label":   "Horaires",
            "hours_list": [
                "Mar – Sam · 7 h 30 – 19 h 30",
                "Dim · 7 h 30 – 13 h 00",
                "Lun · repos",
            ],
        },

        "policy_label": "Notes de précommande",
        "policy_paragraphs": [
            "La précommande du samedi se clôt le vendredi à 18 h 00. "
            "Au-delà de cette heure, nous n'acceptons que si la production "
            "du jour le permet.",
            "Pour les commandes supérieures à 12 pièces, contactez le "
            "comptoir directement. Pour les wedding cakes, deux semaines "
            "minimum d'anticipation · pour le cake design, trois semaines.",
            "Les matières premières tracées (beurre Isigny, cacao "
            "Sambirano, marrons IGP, noisettes IGP) suivent le calendrier "
            "saisonnier. En cas de rupture de stock, nous vous proposons "
            "une variante cohérente, fidèle à la longue pousse de la "
            "maison.",
        ],

        "small_print":
            "Madou Atelier S.r.l. · TVA 11237680016 · Via Sant'Ottavio 36, "
            "10124 Torino · Pasticceria Atelier depuis 2011.",
    },
}
