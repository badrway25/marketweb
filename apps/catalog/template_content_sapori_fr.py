"""Sapori di Langa — Enoteca dei Vignaioli (artisan-workshop archetype) · FR.

Wave 1 Pass-10 close-out (T54 · 2026-05-12). FR translation of the
IT source `template_content_sapori.py`. Shape parity is strict: 179
leaf paths · zero missing · zero extra.

Voice contract (FR):
- Revue du Vin de France / Bettane+Desseauve / Le Figaro Vin register
  — sommelier-pacato, terroir-curatorial, dense et chaleureux à la
  fois.
- Vouvoiement systematique (vous) — un caviste de prestige s'adresse
  à un connaisseur.
- Voice anchor `vignaiolo indipendente` → `vigneron indépendant`
  (pluriel `vignerons indépendants`). Verbatim landing en français —
  c'est le terme consacré (Syndicat des Vignerons Indépendants).
- Le titre IT `Vini di <em>vignaiolo indipendente</em> dalle Langhe
  del Barolo.` devient `Vins de <em>vigneron indépendant</em> dans
  les Langhe du Barolo.` (les balises <em>...</em> sont préservées).
- La presse vinicole francophone utilise volontiers l'italique pour
  les noms propres italiens et les cépages — on garde verbatim les
  noms de personnes, cantine, lieux-dits, AOC italiennes (DOCG /
  DOP), cépages italiens (Nebbiolo, Barbera, Dolcetto, Arneis), et
  la presse italienne (Slow Wine, Gambero Rosso Vini, Vitae AIS, I
  Vini di Veronelli, Doctor Wine).
- Marque conservée verbatim : `Sapori di Langa · Enoteca dei
  Vignaioli`. Persona Pietro Brero · Federica Brero. L'Ordre
  conservé en italien (`Cavalier dell'Ordine dei Cavalieri del
  Tartufo e dei Vini di Alba`), glose française une fois en prose
  atelier.
- CTA conversion `producer-case-order` → "Commandez la caisse du
  vigneron" · "Réservez à la cave" · "Ajouter à la caisse".
"""
from __future__ import annotations

from typing import Any


# Imagery URLs from X.3 curator pack `wine-food-boutique.md`. All
# Pexels CC0 · commercial-safe. Re-declared verbatim from IT source.
_VIGNAIOLO_PORTRAIT_PIETRO = (
    "https://images.pexels.com/photos/8472892/pexels-photo-8472892.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_CARLO = (
    "https://images.pexels.com/photos/8472933/pexels-photo-8472933.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_MARIA = (
    "https://images.pexels.com/photos/8472896/pexels-photo-8472896.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_LUIGI = (
    "https://images.pexels.com/photos/5946081/pexels-photo-5946081.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_FOUNDER_PORTRAIT = (
    "https://images.pexels.com/photos/8472944/pexels-photo-8472944.jpeg"
    "?auto=compress&cs=tinysrgb&w=800&h=1000&fit=crop"
)
_BOTTLE_BAROLO = (
    "https://images.pexels.com/photos/1407847/pexels-photo-1407847.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_BARBERA = (
    "https://images.pexels.com/photos/1123260/pexels-photo-1123260.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_OLIO = (
    "https://images.pexels.com/photos/33783/olive-oil-salad-dressing-cooking-olive.jpg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_FORMAGGIO = (
    "https://images.pexels.com/photos/821365/pexels-photo-821365.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)


SAPORI_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Cave",              "kind": "home"},
        {"slug": "shop",     "label": "Catalogue",         "kind": "shop"},
        {"slug": "product",  "label": "Bouteille",         "kind": "product"},
        {"slug": "atelier",  "label": "Les vignerons",     "kind": "about"},
        {"slug": "journal",  "label": "Journal",           "kind": "journal"},
        {"slug": "contatti", "label": "Visite & commandes","kind": "contact"},
    ],

    "site": {
        "logo_initial": "S",
        "logo_word":    "Sapori di Langa",
        "tag":          "Cave des vignerons · Alba · depuis 1992",
        "phone":        "+39 0173 364 990",
        "whatsapp":     "0173 364 990",
        "whatsapp_link": "https://wa.me/390173364990",
        "email":        "enoteca@saporidilanga.it",
        "address":      "Via Vittorio Emanuele 38 · 12051 Alba CN",
        "hours_compact": "Mar – Sam · 9h30 – 19h30 · Dim 10h – 13h",
        "hours_footer_rows": [
            "Dimanche · 10h00 – 13h00 (matinée seule)",
            "Lundi · fermé",
            "Foire de la Truffe · horaire continu Oct – Nov",
        ],
        "license":      "P.IVA 02814730042 · CCIAA Cuneo REA 263118",
        "footer_intro":
            "Cave d'Alba fondée en 1992 par Pietro Brero. Trente-deux "
            "vignerons indépendants des Langhe, du Roero et du Monferrato, "
            "chacun avec son propre numéro de lot, sa signature au bas de "
            "la cuvée, sa parcelle vinifiée en pureté. Expédition "
            "réfrigérée en 48 heures en Italie.",
        "nav_cta":      "Commandez la caisse du vigneron",
        "nav_cta_kind": "case-order",

        "foot_studio":   "La cave",
        "foot_pages":    "Plan du site",
        "foot_contact":  "Commandes & visites",
        "foot_stockists":"Restaurants qui nous choisissent",
        "stockists_rows": [
            "Piazza Duomo · Alba · 3 étoiles Michelin",
            "La Ciau del Tornavento · Treiso",
            "Locanda del Pilone · Madonna di Como",
            "Antica Corona Reale · Cervere",
        ],

        "currency_symbol":  "€",
        "shop_filter_label": "Filtres",
        "shop_count_unit":   "bouteilles",
        "edition_label":     "Lot",
        "made_in_label":     "Vinifié à",
        "artisan_label":     "Vigneron",
        "material_label":    "Cépage",
        "shipping_label":    "Expédition",
        "shipping_value":    "Réfrigérée en 48 heures · six bouteilles par caisse",
        "guarantee_label":   "Garantie",
        "guarantee_value":   "Bouteille défectueuse remplacée gratuitement",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Millésime 2023 · trente-deux vignerons en cave",
        "headline": "Vins de <em>vigneron indépendant</em> dans les Langhe du Barolo.",
        "intro":
            "Nous allons deux fois par an dans les vignes. Une fois pour "
            "la vendange, une fois pour goûter les millésimes au foudre. "
            "De chaque cave nous connaissons l'œnologue par son prénom, "
            "la parcelle vinifiée, le lot en bouteille. Aucun vin n'arrive "
            "ici par un catalogue de gros.",
        "primary_cta":   "Commandez la caisse du vigneron",
        "primary_href":  "shop",
        "secondary_cta": "Visitez la cave",
        "secondary_href":"contatti",

        # Stamp-aside data
        "stamp_label":  "Notre règle",
        "stamp_heading":"Deux voyages, <em>une bouteille.</em>",
        "stamp_rows": [
            ("Vignerons",   "32 caves"),
            ("Étiquettes",  "180 à la carte"),
            ("Vendange",    "Toujours manuelle"),
            ("Caisse",      "6 bouteilles"),
        ],
        "stamp_footer": "Lot numéroté · expédition réfrigérée",
        "stamp_corner_index": "01",
        "stamp_corner_word":  "LA CAVE",

        # Latest-arrived band — 4 bottles
        "latest_label":   "Tout juste entrés à la carte",
        "latest_heading": "Les derniers millésimes <em>des Langhe.</em>",
        "latest_link_label": "Tout le catalogue",
        "latest_link_href":  "shop",
        "latest_items": [
            {
                "id":       "barolo-cannubi-2019",
                "n":        "Cuvée 2019",
                "edition":  "Lot 23 / 280",
                "name":     "Barolo Cannubi",
                "meta":     "Nebbiolo 100% · Barolo · La Morra",
                "price":    "58 €",
                "tag":      "Millésime",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbera-superiore-2021",
                "n":        "Cuvée 2021",
                "edition":  "Lot 87 / 1 200",
                "name":     "Barbera d'Alba Superiore",
                "meta":     "Barbera 100% · Roero",
                "price":    "22 €",
                "tag":      "Quotidien",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "olio-evo-langhe",
                "n":        "Récolte 2024",
                "edition":  "Lot 12 / 380",
                "name":     "Olio EVO Langhe DOP",
                "meta":     "Frantoio + Leccino · Diano d'Alba",
                "price":    "28 €",
                "tag":      "Saison",
                "image":    _BOTTLE_OLIO,
            },
            {
                "id":       "castelmagno-stagionato",
                "n":        "Affinage 18 mois",
                "edition":  "Meule 04 / 22",
                "name":     "Castelmagno DOP d'alpage",
                "meta":     "Lait de vache · Castelmagno CN",
                "price":    "36 €",
                "tag":      "Été du produit",
                "image":    _BOTTLE_FORMAGGIO,
            },
        ],

        # Vignaioli band — 4 named vintners
        "makers_label":   "Mains qui vinifient",
        "makers_heading": "Trente-deux caves, <em>une seule carte.</em>",
        "makers_intro":
            "Nous travaillons uniquement avec des vignerons indépendants "
            "— ceux qui vinifient leur propre raisin sur leur propre "
            "parcelle et signent personnellement chaque lot à la carte. "
            "Chaque cave a été visitée par Pietro au moins trois fois "
            "avant d'entrer au catalogue.",
        "makers": [
            {
                "name":   "Carlo Brezza",
                "craft":  "Vigneron · Cannubi historique",
                "place":  "Barolo (CN)",
                "since":  "Vigne de 1885 · Brezza depuis 1885",
                "quote":  "« Le Barolo ne se fait pas dans la hâte. Il se fait "
                          "dans le silence : deux ans de grand foudre, et "
                          "l'oreille tendue pour entendre si le fût chante ou "
                          "se plaint. »",
                "portrait": _VIGNAIOLO_PORTRAIT_CARLO,
            },
            {
                "name":   "Maria Vajra",
                "craft":  "Vigneronne · Bricco delle Viole",
                "place":  "Vergne · Barolo (CN)",
                "since":  "Cave familiale depuis 1972",
                "quote":  "« Nous ne vinifions que ce que nous voyons grandir. "
                          "Si une parcelle ne donne pas ce qu'elle doit, ce "
                          "millésime-là nous ne le mettons pas en bouteille. "
                          "La carte des vignerons se fait aussi avec ce qui "
                          "n'y est pas. »",
                "portrait": _VIGNAIOLO_PORTRAIT_MARIA,
            },
            {
                "name":   "Luigi Boasso",
                "craft":  "Vigneron · Gabutti Roccaforte",
                "place":  "Serralunga d'Alba (CN)",
                "since":  "Quatre générations dans la vigne",
                "quote":  "« Le Nebbiolo est un cépage trompeur. Il devient ce "
                          "que vous lui racontez du sol. C'est pourquoi je ne "
                          "travaille pas d'autres parcelles : apprendre un seul "
                          "terroir demande trente ans. »",
                "portrait": _VIGNAIOLO_PORTRAIT_LUIGI,
            },
            {
                "name":   "Anna Brovia",
                "craft":  "Vigneronne · Villero & Rocche dei Brovia",
                "place":  "Castiglione Falletto (CN)",
                "since":  "Cave des Brovia depuis 1863",
                "quote":  "« Nous ne faisons pas de concours, nous ne faisons "
                          "pas de notes. Nous faisons du Barolo comme on l'a "
                          "toujours fait à Castiglione Falletto : long, "
                          "austère, sans fioritures. Qui cherche la facilité, "
                          "qu'il aille ailleurs. »",
                "portrait": _VIGNAIOLO_PORTRAIT_PIETRO,
            },
        ],

        # Provenance — terroir + filiera
        "provenance_label":   "D'où il vient",
        "provenance_heading": "Soixante-cinq kilomètres, <em>trois appellations.</em>",
        "provenance_intro":
            "Toutes les étiquettes à la carte viennent d'un rayon de "
            "soixante-cinq kilomètres autour d'Alba. Trois appellations "
            "principales — Langhe, Roero, Monferrato — et un réseau de "
            "vignerons indépendants qui se sont choisis mutuellement.",
        "provenance_items": [
            {
                "icon": "vine",
                "title": "Langhe DOCG",
                "desc":  "Barolo, Barbaresco, Dolcetto · onze communes de "
                         "production · sols calcaires et marneux · altitude "
                         "200-400 m.",
                "place": "Alba · La Morra · Barolo · Castiglione",
            },
            {
                "icon": "hills",
                "title": "Roero DOCG",
                "desc":  "Nebbiolo Roero, Arneis, Favorita · au-delà du Tanaro · "
                         "sols sableux · vins plus tendus et parfumés · "
                         "altitude 280-380 m.",
                "place": "Canale · Vezza · Santo Stefano Roero",
            },
            {
                "icon": "cheese",
                "title": "Monferrato Casalese",
                "desc":  "Barbera Superiore, Grignolino, Ruchè · pentes "
                         "vallonnées · sols calcaréo-argileux · vins de "
                         "tous les jours, de caractère.",
                "place": "Casale · Vignale · Rosignano",
            },
            {
                "icon": "olive",
                "title": "Riviera ligure (50 km)",
                "desc":  "Huile EVO Taggiasco DOP · sel de Trapani au "
                         "charbon végétal · maquereau à l'huile de La "
                         "Spezia. Fournisseurs historiques de la maison.",
                "place": "Imperia · La Spezia · Trapani",
            },
        ],

        # Care — wine handling guarantees
        "care_label":   "Comment il arrive, comment il se conserve",
        "care_heading": "Quatre promesses de caisse.",
        "care_items": [
            ("Expédition réfrigérée",
             "Caisse de six bouteilles expédiée en carton thermique "
             "avec gel pack à 14 °C. Livraison en 48 heures en Italie · "
             "4 jours en Europe occidentale."),
            ("Lot numéroté à la main",
             "Chaque bouteille porte, écrits à la main, le numéro de "
             "lot, le millésime de la cuvée et la signature du vigneron. "
             "Aucune étiquette industrielle-typographique."),
            ("Remplacement bouteille défectueuse",
             "TCA, oxydation, casse en transit · nous remplaçons "
             "gratuitement dans les trois mois suivant la livraison · "
             "sur simple preuve photographique du bouchon ou du niveau."),
            ("Conseils du sommelier",
             "Pietro ou Federica vous rappellent sous 24 h si vous "
             "souhaitez un accord pour une soirée, une verticale pour "
             "un anniversaire, une caisse pour un cadeau d'entreprise."),
        ],

        # Press band — Italian wine press (kept verbatim)
        "press_label": "Recensés dans",
        "press_items": ["Slow Wine", "Gambero Rosso Vini", "Vitae AIS",
                        "I Vini di Veronelli", "Doctor Wine"],

        # Journal teaser
        "journal_teaser_label":   "Notes de journal",
        "journal_teaser_heading": "Comment nous avons bâti la <em>carte automne 2026.</em>",
        "journal_teaser_link":    "Lire le journal",
        "journal_teaser_href":    "journal",

        # CTA section
        "cta_label":     "Commandez · visitez · écrivez-nous",
        "cta_heading":   "Une caisse de six bouteilles, <em>choisie par Pietro.</em>",
        "cta_intro":
            "Les caisses sélectionnées changent chaque mois selon les "
            "caves en livraison. Vins de tous les jours, vins de garde, "
            "formules mixtes avec huile et fromages. Paiement à "
            "l'enlèvement, expédition réfrigérée en 48 heures.",
        "cta_primary":      "Commandez la caisse du mois",
        "cta_primary_href": "shop",
        "cta_secondary":    "Venez à la cave",
    },

    # ─── SHOP (catalog) ─────────────────────────────────────────
    "shop": {
        "eyebrow":  "Carte de la maison · millésimes 2023-2024",
        "headline": "Cent quatre-vingts étiquettes, <em>une seule signature.</em>",
        "intro":
            "Carte des vins, huiles, fromages et conserves. Toutes les "
            "étiquettes viennent de vignerons indépendants visités "
            "personnellement. Pour chaque vin, la cuvée, le lot, le "
            "millésime et le vigneron qui signe sont indiqués.",

        "filter_section_label": "Filtres",
        "filter_groups": [
            {
                "label": "Appellation",
                "options": ["Barolo DOCG", "Barbaresco DOCG", "Roero DOCG",
                            "Langhe DOC", "Monferrato DOC", "Asti DOCG",
                            "Vin de table"],
            },
            {
                "label": "Cépage",
                "options": ["Nebbiolo", "Barbera", "Dolcetto", "Arneis",
                            "Favorita", "Grignolino"],
            },
            {
                "label": "Typologie",
                "options": ["Vins rouges", "Vins blancs", "Vins doux",
                            "Vins effervescents", "Huiles & condiments",
                            "Fromages", "Charcuterie & conserves"],
            },
        ],

        "sort_label": "Trier par",
        "sort_options": ["Plus récents", "Vigneron", "Millésime", "Prix"],

        "result_count": "180 bouteilles",
        "result_subtitle": "Mis à jour le mardi 8 octobre 2026",

        # Sample products — 8 cards
        "products": [
            {
                "id":       "barolo-cannubi-2019",
                "n":        "01",
                "edition":  "Cuvée 2019 · Lot 23",
                "name":     "Barolo Cannubi · Brezza",
                "meta":     "Nebbiolo · Barolo · La Morra",
                "price":    "58 €",
                "tag":      "Millésime",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbaresco-rabaja-2018",
                "n":        "02",
                "edition":  "Cuvée 2018 · Lot 11",
                "name":     "Barbaresco Rabajà · Cortese",
                "meta":     "Nebbiolo · Barbaresco · Treiso",
                "price":    "64 €",
                "tag":      "Verticale",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbera-superiore-2021",
                "n":        "03",
                "edition":  "Cuvée 2021 · Lot 87",
                "name":     "Barbera d'Alba Superiore · Vajra",
                "meta":     "Barbera · Roero · Canale",
                "price":    "22 €",
                "tag":      "Quotidien",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "dolcetto-diano-2022",
                "n":        "04",
                "edition":  "Cuvée 2022 · Lot 42",
                "name":     "Dolcetto di Diano d'Alba · Boasso",
                "meta":     "Dolcetto · Diano d'Alba",
                "price":    "16 €",
                "tag":      "Table",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "arneis-roero-2023",
                "n":        "05",
                "edition":  "Cuvée 2023 · Lot 56",
                "name":     "Roero Arneis · Brovia",
                "meta":     "Arneis · Vezza d'Alba",
                "price":    "18 €",
                "tag":      "Blanc",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "olio-evo-langhe",
                "n":        "06",
                "edition":  "Récolte 2024 · Lot 12",
                "name":     "Olio EVO Langhe DOP · Frantoio Anfossi",
                "meta":     "Frantoio + Leccino · Diano d'Alba",
                "price":    "28 €",
                "tag":      "Saison",
                "image":    _BOTTLE_OLIO,
            },
            {
                "id":       "castelmagno-stagionato",
                "n":        "07",
                "edition":  "Affinage 18 mois · Meule 04",
                "name":     "Castelmagno DOP d'alpage",
                "meta":     "Lait de vache piémontaise",
                "price":    "36 €",
                "tag":      "Fromage",
                "image":    _BOTTLE_FORMAGGIO,
            },
            {
                "id":       "salame-cuneo",
                "n":        "08",
                "edition":  "Affinage 4 mois · Lot 08",
                "name":     "Salame Cuneo · Boucherie Cesare",
                "meta":     "Porc de Cuneo · poivre noir · vin de taille",
                "price":    "24 €",
                "tag":      "Charcuterie",
                "image":    _BOTTLE_FORMAGGIO,
            },
        ],

        "featured_product_id": "barolo-cannubi-2019",

        "footer_note_label": "Expéditions & retraits",
        "footer_note":
            "Expédition réfrigérée en 48 heures en Italie · caisse "
            "minimale six bouteilles · frais d'expédition 12 € "
            "(gratuite au-delà de 200 €). Retrait à la cave sans "
            "préavis. Pour les commandes au-delà de douze bouteilles, "
            "contactez-nous directement.",
    },

    # ─── PRODUCT ────────────────────────────────────────────────
    "product": {
        "id":       "barolo-cannubi-2019",
        "n":        "01",
        "edition":  "Cuvée 2019",
        "edition_note": "Lot 23 / 280 · mis en bouteille en décembre 2022",
        "name":     "Barolo Cannubi · Brezza",
        "subtitle": "Nebbiolo 100% · vinifié sur la colline historique du Cannubi",
        "price":    "58 €",
        "vat_note": "TVA incluse · caisse minimale six bouteilles",
        "intro":
            "Barolo de la cave Brezza, parcelle de Cannubi historique "
            "(la colline la plus ancienne de la commune de Barolo, "
            "vendange documentée depuis 1752). Vendange manuelle, "
            "fermentation en cuves d'acier, élevage en grand foudre de "
            "chêne de Slavonie pendant 30 mois, puis 12 mois "
            "supplémentaires en bouteille avant la sortie.",

        "gallery": [
            _BOTTLE_BAROLO,
            _BOTTLE_BAROLO,
            _BOTTLE_BAROLO,
        ],

        "info_label": "Fiche technique",
        "info_rows": [
            ("Vigneron",      "Carlo Brezza · Brezza & Figli"),
            ("Appellation",   "Barolo DOCG"),
            ("Cépage",        "Nebbiolo 100%"),
            ("Commune",       "Barolo (CN)"),
            ("Parcelle",      "Cannubi historique"),
            ("Altitude",      "260 m · exposition sud-est"),
            ("Vendange",      "Manuelle · deuxième semaine d'octobre 2019"),
            ("Élevage",       "30 mois en grand foudre + 12 mois en bouteille"),
            ("Degré",         "14,5% vol"),
            ("Sulfites",      "< 80 mg/l · viticulture biologique certifiée"),
        ],

        "size_label": "Formats disponibles",
        "size_intro": "Disponible en bouteille simple, magnum, caisse horizontale 2019 et caisse verticale 2015 – 2019.",
        "size_options": ["750 ml", "1,5 L Magnum", "Caisse 6 · 2019", "Caisse 6 · verticale"],
        "size_chart_link": "Voir tous les formats & verticales",
        "size_chart_href": "shop",

        "artisan_label":   "Vigneron",
        "artisan_name":    "Carlo Brezza",
        "artisan_role":    "Quatrième génération · Brezza & Figli depuis 1885",
        "artisan_bio":
            "Cave familiale fondée par l'arrière-grand-père de Carlo en "
            "1885, transmise en ligne directe de père en fils. Carlo est "
            "entré dans les vignes en 1997 après ses études œnologiques "
            "à Alba et trois vendanges au Domaine Romanée-Conti. Il "
            "vinifie exclusivement les parcelles familiales (Cannubi "
            "historique, Bricco Sarmassa, Cannubi Muscatel) — aucun "
            "raisin acheté.",
        "artisan_portrait": _VIGNAIOLO_PORTRAIT_CARLO,

        "buy_primary":   "Ajouter à la caisse",
        "buy_secondary": "Réservez à la cave",
        "buy_note":
            "Commandes au-delà de 12 bouteilles · contactez la cave "
            "directement. Disponibilité vérifiée au moment de la "
            "commande.",

        "care_label": "Conservation",
        "care_intro":
            "Barolo de garde · demande une conservation attentive pour "
            "exprimer son potentiel.",
        "care_items": [
            ("Température", "12-14 °C constants · sans à-coups"),
            ("Position",    "Horizontale · bouchon toujours en contact avec le vin"),
            ("Humidité",    "Au moins 70% · ambiance sombre"),
            ("Ouverture",   "Ouvrir 2-3 heures avant · décantation conseillée"),
            ("Plateau",     "Prêt à boire 2025-2040 · plateau de maturité 2028-2035"),
        ],

        "provenance_label":   "Du Cannubi au verre",
        "provenance_heading": "Quatre passages tracés.",
        "provenance_steps": [
            ("01", "Vendange",        "Récolte manuelle en cagettes de 18 kg · Cannubi à 260 m · deuxième semaine d'octobre 2019"),
            ("02", "Élevage",         "Grand foudre de chêne de Slavonie · 30 mois · sans barrique · Cave Brezza Barolo"),
            ("03", "Mise en bouteille","Décembre 2022 · sans filtration · sans collage · lot 23 sur 280"),
            ("04", "Expédition",      "Caisse en bois marquée au feu · carton thermique avec gel pack à 14 °C · 48 heures en Italie"),
        ],

        "related_label":   "Verticales et accords",
        "related_intro":
            "Cuvées de la même cave dans les millésimes précédents, et "
            "vins conseillés par Pietro comme accord de confrontation.",
        "related_items": [
            {"id":"barolo-cannubi-2018",   "n":"N° 088","name":"Barolo Cannubi · 2018",   "meta":"Millésime frais · Brezza",       "price":"62 €","image":_BOTTLE_BAROLO},
            {"id":"barolo-cannubi-2017",   "n":"N° 074","name":"Barolo Cannubi · 2017",   "meta":"Millésime chaud · Brezza",       "price":"68 €","image":_BOTTLE_BAROLO},
            {"id":"barbaresco-rabaja-2018","n":"N° 142","name":"Barbaresco Rabajà · 2018","meta":"Confrontation territoriale",      "price":"64 €","image":_BOTTLE_BAROLO},
            {"id":"barbera-vajra",         "n":"N° 211","name":"Barbera Superiore · 2021","meta":"Quotidien à table · Vajra",       "price":"22 €","image":_BOTTLE_BARBERA},
        ],
    },

    # ─── ATELIER (about · "Les vignerons") ─────────────────────
    "atelier": {
        "eyebrow":  "La cave",
        "headline": "Sapori di Langa : <em>trente-deux vignerons, une seule enseigne.</em>",
        "intro":
            "Sapori di Langa est une cave indépendante fondée à Alba en "
            "1992. Nous travaillons exclusivement avec des vignerons "
            "indépendants qui vinifient eux-mêmes · ni coopératives · "
            "ni vins d'industrie · ni étiquettes construites sur tapis "
            "vert. Pour entrer à la carte, une cave est visitée au moins "
            "trois fois par Pietro.",

        "mission_label":   "Notre mission",
        "mission_heading": "Payer le vigneron à sa juste valeur.",
        "mission_text":
            "La cave existe pour une raison : redonner au vigneron "
            "indépendant le prix que son travail mérite. Marge convenue "
            "en transparence, contrats annuels signés à la main, avances "
            "sur le raisin dans les vignes si nécessaire. Nous ne vendons "
            "pas de « remises » parce que celui qui fait un Nebbiolo à "
            "14% ne peut rien rabattre.",

        "process_label":   "Comment nous choisissons les étiquettes",
        "process_heading": "Trois visites, une carte.",
        "process_steps": [
            {"num": "01", "title": "Première visite · printemps",
             "desc": "Pietro va dans les vignes en mars ou avril, regarde "
                     "la taille, goûte les derniers millésimes au foudre, "
                     "parle avec le vigneron de l'été précédent."},
            {"num": "02", "title": "Deuxième visite · vendange",
             "desc": "Septembre-octobre · présence lors de la vendange "
                     "pendant une journée entière, au moins trois cagettes "
                     "ouvertes. On observe qui est dans la vigne à "
                     "récolter, et avec quel soin."},
            {"num": "03", "title": "Troisième visite · dégustation en cave",
             "desc": "L'hiver suivant · dégustation technique des foudres "
                     "avec l'œnologue. Si les chiffres tiennent et que le "
                     "vin dit la vérité, on signe le contrat annuel."},
            {"num": "04", "title": "Entrée à la carte",
             "desc": "Premier lot à la carte seulement après la quatrième "
                     "visite (sortie de foudre, bouteille en main). Aucun "
                     "vin à la carte que Pietro n'ait goûté dans trois "
                     "millésimes différents."},
        ],

        "founder_label":   "Le fondateur",
        "founder_heading": "Pietro Brero.",
        "founder_text":
            "Pietro est né à Alba en 1958. Élevé dans la trattoria "
            "familiale, il a travaillé comme sommelier au Combal.Zero "
            "de Davide Scabin de 1985 à 1991, l'année où Combal se "
            "trouvait encore à Almese. Il ouvre Sapori di Langa en 1992 "
            "via Vittorio Emanuele avec trois caves à la carte. "
            "Aujourd'hui elles sont trente-deux. Distingué Chevalier de "
            "l'Ordre des Chevaliers de la Truffe et des Vins d'Alba "
            "(Cavalier dell'Ordine dei Cavalieri del Tartufo e dei Vini "
            "di Alba) en 2014.",
        "founder_portrait": _FOUNDER_PORTRAIT,
        "founder_caption": "Pietro Brero · Cavalier dell'Ordine dei Cavalieri del Tartufo e dei Vini di Alba",

        "numbers_label":   "La cave en chiffres",
        "numbers_items": [
            ("32",    "vignerons indépendants à la carte"),
            ("180",   "étiquettes au catalogue annuel"),
            ("1992",  "année d'ouverture"),
            ("65 km", "rayon maximal de sélection depuis les Langhe"),
        ],

        "visit_label":   "Visitez la cave",
        "visit_heading": "Via Vittorio Emanuele 38, <em>Alba.</em>",
        "visit_text":
            "Cinq minutes de la gare d'Alba · dix minutes de la "
            "cathédrale. Dégustation guidée sur rendez-vous le jeudi "
            "après-midi · cinq vins avec planche de Castelmagno et "
            "salame Cuneo, 35 € par personne. Sans rendez-vous pour les "
            "achats aux heures d'ouverture.",
        "visit_primary":      "Réservez une dégustation",
        "visit_primary_href": "contatti",
        "visit_secondary":    "Plan & horaires",
    },

    # ─── JOURNAL ───────────────────────────────────────────────
    "journal": {
        "eyebrow":  "Journal de cave",
        "headline": "Notes de chai, <em>notes de vendange.</em>",
        "intro":
            "Brèves notes de Pietro et Federica sur le travail en cave, "
            "sur les vendanges en cours, sur les bouteilles ouvertes le "
            "soir pour les clients les plus curieux. Lecture réservée.",
        "list_label": "Voix du journal",
        "entries": [
            {
                "slug":    "vendemmia-2024-langhe",
                "kicker":  "Vendange 2024",
                "title":   "Vendange 2024 dans les Langhe · ce qui est sorti des foudres",
                "date":    "10 octobre 2026",
                "read_min": 6,
                "author":  "Pietro Brero",
                "lede":
                    "La vendange 2024 a demandé de la patience. La "
                    "chaleur d'août a ralenti les maturations, septembre "
                    "a remis les choses en place. Voici ce qui entre à "
                    "la carte à partir de novembre.",
            },
            {
                "slug":    "barolo-2019-degustazione",
                "kicker":  "Millésime à la carte",
                "title":   "Pourquoi le Barolo 2019 vaut les six ans d'attente",
                "date":    "28 septembre 2026",
                "read_min": 5,
                "author":  "Pietro Brero",
                "lede":
                    "Le millésime 2019 est sorti en août après trente "
                    "ans de Barolo en cave. Voici pourquoi il vaut les "
                    "deux ans de grand foudre et les six ans minimum "
                    "avant d'être débouché.",
            },
            {
                "slug":    "olio-evo-langhe-2024",
                "kicker":  "Huile de la maison",
                "title":   "Olio EVO Langhe 2024 · une récolte à retenir",
                "date":    "15 septembre 2026",
                "read_min": 4,
                "author":  "Federica Bertola",
                "lede":
                    "Le moulin Anfossi a clos la récolte 2024 le "
                    "5 septembre. Cinq hectolitres à la carte à partir "
                    "d'octobre, lot 12. Voici comment elle est.",
            },
        ],

        "footer_note_label": "Recevez le journal par e-mail",
        "footer_note":
            "Quatre ou cinq parutions par an, jamais plus. Le reçoit "
            "uniquement celui qui en fait la demande explicite en "
            "caisse ou via le formulaire de contact.",
    },

    # ─── CONTATTI ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Visite & commandes",
        "headline": "Un appel, <em>une caisse.</em>",
        "intro":
            "Pour commander une caisse ou réserver une dégustation "
            "guidée, le plus simple est un appel à la cave aux heures "
            "d'ouverture. Ou bien utiliser le formulaire ci-dessous · "
            "réponse sous 24 h en horaires ouvrables.",

        "form_section_label": "Écrivez-nous",
        "form_section_intro":
            "Pour les commandes spéciales (verticales, magnums, caisses "
            "d'entreprise), indiquez le vigneron ou le millésime "
            "souhaité. Pour les dégustations guidées, indiquez la date "
            "et le nombre de participants.",
        "form_helper_required": "Les champs marqués sont obligatoires.",
        "form_submit_button":   "Envoyer la demande",
        "form_submit_note":     "Vous recevrez confirmation par e-mail sous 24 heures pendant les heures d'ouverture.",

        "form_fields": [
            {"name": "name",     "label": "Nom et prénom",  "type": "text",     "required": True},
            {"name": "email",    "label": "E-mail",          "type": "email",    "required": True},
            {"name": "phone",    "label": "Téléphone",       "type": "tel",      "required": False},
            {"name": "subject",  "label": "Objet",           "type": "select",
             "options": ["Commande caisse", "Dégustation guidée", "Verticale ou magnum",
                         "Caisse d'entreprise ou cadeau", "Autre"],  "required": True},
            {"name": "message",  "label": "Message",         "type": "textarea", "required": True,
             "placeholder": "Ex. « Caisse de six Barolo cuvée 2019 » ou "
                             "« Dégustation pour quatre personnes jeudi 18 octobre »."},
        ],

        "card_label":          "La cave",
        "card_address_label":  "Adresse",
        "card_address_value":  "Via Vittorio Emanuele 38 · 12051 Alba CN",
        "card_phone_label":    "Téléphone",
        "card_phone_value":    "+39 0173 364 990",
        "card_whatsapp_label": "WhatsApp",
        "card_whatsapp_value": "0173 364 990",
        "card_email_label":    "E-mail",
        "card_email_value":    "enoteca@saporidilanga.it",
        "card_hours_label":    "Horaires",
        "card_hours_rows": [
            "Mar – Sam · 9h30 – 19h30 en continu",
            "Dimanche · 10h00 – 13h00 matinée seule",
            "Lundi · fermé · dégustations privées sur rendez-vous",
            "Foire de la Truffe · oct – nov · 9h – 21h en continu",
        ],
        "card_directions_label": "Comment venir",
        "card_directions_text":
            "Cinq minutes à pied de la gare d'Alba (train régional "
            "direct depuis Turin · 1 h 10 min). Dix minutes de la "
            "cathédrale Saint-Laurent. Parking gratuit Piazza "
            "Risorgimento, 200 mètres de la cave.",

        "faq_label": "Questions fréquentes",
        "faq_items": [
            ("Combien coûte l'expédition ?",
             "Expédition réfrigérée en 48 heures : 12 € en Italie "
             "(gratuite au-delà de 200 €), 24 € en Europe occidentale. "
             "Caisse minimale six bouteilles."),
            ("Puis-je commander une seule bouteille ?",
             "Non, la caisse minimale est de six bouteilles. "
             "Composition libre entre vin, huile, fromages et "
             "charcuterie. La valeur indicative de la caisse minimale "
             "est d'environ 90-100 €."),
            ("Avez-vous des vins biologiques ou naturels ?",
             "Oui. Environ 70% des vignerons à la carte travaillent en "
             "agriculture biologique certifiée, 20% en biodynamie "
             "certifiée Demeter. Le reste suit des protocoles à faible "
             "intervention, sans certification."),
            ("Expédiez-vous à l'étranger ?",
             "Europe occidentale oui (France, Allemagne, Belgique, "
             "Pays-Bas, Luxembourg, Autriche). Reste du monde "
             "uniquement sur devis (USA · UK · Suisse · Japon)."),
            ("Puis-je visiter la cave sans réserver ?",
             "Oui, aux heures d'ouverture. Pour la dégustation guidée "
             "du jeudi après-midi, la réservation est nécessaire au "
             "moins 48 h à l'avance."),
        ],
    },
}
