"""Podere Le Querce — Agriturismo familial toscan (artisan-workshop · FR).

T60 · Wave 2 Pass-4 (2026-05-13) · traduction FR du gabarit IT
podere-agriturismo · mirroring strict de la forme récursive IT
(218 chemins de feuilles · zéro manquant · zéro en trop).

Voice contract (FR):
- Registre éditorial-rural Le Figaro Magazine · Côté Sud · Saveurs ·
  Connaissance des Arts (Voyages) · Air France Magazine. Chaleur
  familière (la famille vous reçoit pour une longue tablée · le
  vouvoiement systématique à travers tout le gabarit).
- Voice anchor `hospitalité paysanne` — registre toscan-rural qui
  met en avant la promesse de la-famille-multigénérationnelle-vous-
  reçoit. Verbatim et porteur de sens dans le titre principal home,
  famiglia.statement_heading (mission_heading), soggiorno intro et
  FAQ, et site.footer_intro. Préservé tel quel à travers ≥ 15
  surfaces du gabarit.
- Mots italiens conservés en tant que loanwords éditoriaux (cf. Le
  Figaro Magazine Italia, Côté Sud Toscane): `podere`, `agriturismo`,
  `norcino`, `pecorino`, `ribollita`, `bruschetta`, `Vin Santo`,
  `Cinta Senese` (nom de race italienne), `Sangiovese`, `Canaiolo`,
  `Colorino`, `Moraiolo`, `Frantoio`, `Leccino`, `fagioli zolfini`
  (cultivar), `Senatore Cappelli` (cultivar de blé).
- Noms propres italiens préservés verbatim: famille Pasquinelli
  (Maria · Carlo · Giovanni · Anna · Mario · Annetta · Maddalena),
  producteurs (Andrea Falleri · Famille Bartoletti · Davide Pieri ·
  Sœurs de San Vivaldo), famille historique Antinori, lieux (Greve
  in Chianti · Chianti · Toscane · Florence · Lamole · Roccastrada
  · Castelfiorentino · Montaione · Vinci · Zeri · Pratomagno ·
  Maremma · Le Querce), DOCG/DOP en italien.
- Chiffres latins préservés: 1934 (acte de vente) · 1985 (reprise
  par Maria) · 2025 (récolte courante) · prix en € 28 · € 22 · etc.
- Vocabulaire FR éditorial: vendanges (toujours pluriel) · récolte
  des olives · oliveraie · vigne · potager · étable · meunier ·
  berger · monastère · matriarche · hectares · arrière-grands-
  parents · acompte · virement bancaire · solde à l'arrivée ·
  nuitée · séjour · tablée · enregistrement automatique (à éviter).
"""
from __future__ import annotations

from typing import Any


# Interim Unsplash CC0 imagery pool · travel-agriturismo signal.
# Identique au gabarit IT — la curatorial X.5 pack pour agriturismo
# couvrira les 6 rôles porteurs (hero podere golden hour · oliveraie
# · vigne · tablée en cour · cuisine paysanne · la famille en
# cuisine).
_PODERE_HERO = "https://images.unsplash.com/photo-1602941525521-46f6f1ab39ce?w=1600&q=80&auto=format&fit=crop"
_OLIVETO = "https://images.unsplash.com/photo-1567416661576-d8b6e92e63d2?w=1200&q=80&auto=format&fit=crop"
_VIGNA_CHIANTI = "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=1200&q=80&auto=format&fit=crop"
_TAVOLATA = "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1200&q=80&auto=format&fit=crop"
_CUCINA_CONTADINA = "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=1200&q=80&auto=format&fit=crop"
_FAMIGLIA_PORTRAIT = "https://images.unsplash.com/photo-1573497019418-b400bb3ab074?w=1200&q=80&auto=format&fit=crop"
_OLIO_BOTTLE = "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=1200&q=80&auto=format&fit=crop"
_VINO_BOTTLE = "https://images.unsplash.com/photo-1474722883778-792e7990302f?w=1200&q=80&auto=format&fit=crop"
_VINSANTO = "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=1200&q=80&auto=format&fit=crop"
_MIELE = "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=1200&q=80&auto=format&fit=crop"
_MARMELLATA = "https://images.unsplash.com/photo-1535990379313-50d1f6fc0c4f?w=1200&q=80&auto=format&fit=crop"
_PECORINO = "https://images.unsplash.com/photo-1452195100486-9cc805987862?w=1200&q=80&auto=format&fit=crop"
_SALAME = "https://images.unsplash.com/photo-1599379892470-bbe1eb01ea75?w=1200&q=80&auto=format&fit=crop"
_CANTUCCI = "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1200&q=80&auto=format&fit=crop"
_PORTRAIT_MARIA = "https://images.unsplash.com/photo-1559963110-71b394e7494d?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_CARLO = "https://images.unsplash.com/photo-1545167622-3a6ac756afa4?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_GIOVANNI = "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_ANNA = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_PRODUCER = "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=900&q=80&auto=format&fit=crop"


PODERE_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "Le podere",          "kind": "home"},
        {"slug": "dispensa",  "label": "La dispensa",        "kind": "shop"},
        {"slug": "prodotto",  "label": "Le produit",         "kind": "product"},
        {"slug": "famiglia",  "label": "La famille",         "kind": "about"},
        {"slug": "diario",    "label": "Journal de campagne","kind": "journal"},
        {"slug": "soggiorno", "label": "Séjour",             "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":    "Q",
        "logo_word":       "Podere Le Querce",
        "tag":             "Agriturismo de famille · Greve in Chianti · depuis 1934",
        "phone":           "+39 055 853 261",
        "whatsapp":        "+39 339 458 1126",
        "whatsapp_link":   "https://wa.me/393394581126",
        "email":           "famiglia@podereleQuerce.it",
        "address":         "Località Le Querce 14 · 50022 Greve in Chianti · Florence",
        "hours_compact":   "Ouvert toute l'année · cuisine sur réservation 12h30 et 19h30",
        "hours_footer_rows": [
            "Accueil des hôtes 8h-22h · Maria en cuisine dès 7h",
            "Dispensa ouverte tous les jours 9h-19h · fermée le dimanche",
        ],
        "license":         "Code CITRA 048-029-001 · Insc. CCIAA Florence 354210 · Az. Agricola Pasquinelli S.S.",
        "footer_intro":
            "Podere Le Querce est une exploitation agricole familiale à Greve in Chianti · "
            "13 hectares de terres avec oliveraie historique, vigne de Sangiovese, potager, "
            "étable de Cinta Senese, cave et quatre chambres d'hospitalité paysanne. "
            "Nous faisons tout maison : huile, vin, miel, salaisons, pâtes, cantucci. "
            "La famille Pasquinelli vit ici depuis 1934. L'hospitalité paysanne, "
            "ici, signifie qu'à votre venue en hôtes vous mangez à notre table.",

        # Nav CTA — registre agriturismo
        "nav_cta":         "Réservez votre séjour",
        "nav_cta_kind":    "appointment",

        # Footer labels
        "foot_studio":     "Le podere",
        "foot_pages":      "Plan du site",
        "foot_contact":    "Séjour",
        "foot_stockists":  "Où nous trouver",
        "stockists_rows": [
            "Mercato della Terra · Greve in Chianti · dimanche matin",
            "Slow Food Florence · comptoir mensuel",
            "Expédition à domicile · Italie 24-48h · Europe 4-6 jours",
            "Dispensa au podere · ouverte au public tous les jours 9h-19h",
        ],

        # Currency + product labels
        "currency_symbol":   "€",
        "shop_filter_label": "Affiner la dispensa",
        "shop_count_unit":   "produits du podere",
        "edition_label":     "Millésime",
        "made_in_label":     "Produit à",
        "artisan_label":     "Mains de",
        "material_label":    "Matière première",
        "shipping_label":    "Expédition",
        "shipping_value":    "24-48h en Italie · expédition réfrigérée l'été",
        "guarantee_label":   "Garantie du podere",
        "guarantee_value":   "Nous remplaçons gratuitement toute bouteille cassée ou défectueuse · sous 30 jours",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Agriturismo · Greve in Chianti · depuis 1934",
        "headline": "Quatre générations dans un podere toscan. <em>Hospitalité paysanne</em>, toute l'année.",
        "intro":
            "Podere Le Querce est la maison de la famille Pasquinelli depuis 1934, lorsque "
            "les arrière-grands-parents Mario et Annetta l'ont achetée à la famille Antinori "
            "par un acte de vente conservé en mairie. C'est aujourd'hui un agriturismo "
            "d'hospitalité paysanne avec quatre chambres, une cuisine de famille avec "
            "tablée sur réservation, et une dispensa paysanne avec nos huit produits.",

        "primary_cta":          "Réservez votre séjour",
        "primary_href":         "soggiorno",
        "secondary_cta":        "Visitez la dispensa",
        "secondary_href":       "dispensa",

        # Stamp panel — list[4] of tuple[2]
        "stamp_label":   "Le podere en quatre lignes",
        "stamp_heading": "Quatre générations · une seule tablée.",
        "stamp_rows": [
            ("Année",              "1934 · acte de vente Antinori → Pasquinelli"),
            ("Famille",            "Maria + Carlo + Giovanni + Anna · 4 à la barre"),
            ("Hectares",           "13 hectares · oliveraie + vigne + potager + étable"),
            ("Chambres",           "4 chambres · hospitalité paysanne ouverte toute l'année"),
        ],
        "stamp_footer":      "Mercato della Terra Greve · Slow Food Florence · Expédition à domicile Italie 24-48h",
        "stamp_corner_index": "Saison",
        "stamp_corner_word":  "2026",

        # Latest items — list[4] of dict[8 keys=edition,id,image,meta,n,name,price,tag]
        "latest_label":       "Dans la dispensa",
        "latest_heading":     "Huit produits du podere, toujours disponibles.",
        "latest_link_label":  "Tous les produits",
        "latest_link_href":   "dispensa",
        "latest_items": [
            {
                "id":      "olio-evo-podere-2025",
                "n":       "N° 01",
                "image":   _OLIO_BOTTLE,
                "edition": "Récolte 2025",
                "name":    "Huile d'olive extra vierge du Podere",
                "meta":    "Moraiolo + Frantoio + Leccino · 2 400 oliviers",
                "price":   "€ 28 / 500 ml",
                "tag":     "Nouveau · récolte de novembre",
            },
            {
                "id":      "chianti-classico-2022",
                "n":       "N° 02",
                "image":   _VINO_BOTTLE,
                "edition": "Vendanges 2022",
                "name":    "Chianti Classico DOCG",
                "meta":    "Sangiovese 95% · 1,8 ha de vigne",
                "price":   "€ 22 / bouteille",
                "tag":     "Cave du podere",
            },
            {
                "id":      "miele-millefiori",
                "n":       "N° 04",
                "image":   _MIELE,
                "edition": "Extraction juillet 2025",
                "name":    "Miel toutes fleurs",
                "meta":    "12 ruches · clairière de châtaigniers",
                "price":   "€ 14 / 250 g",
                "tag":     "Cent pour cent podere",
            },
            {
                "id":      "salame-cinta-senese",
                "n":       "N° 07",
                "image":   _SALAME,
                "edition": "Affinage 9 mois",
                "name":    "Saucisson de Cinta Senese",
                "meta":    "Porcs noirs élevés en semi-liberté",
                "price":   "€ 38 / pièce entière",
                "tag":     "8 bêtes en porcherie",
            },
        ],

        # Makers — list[4] of dict[6 keys=craft,name,place,portrait,quote,since]
        "makers_label":   "Les producteurs du territoire",
        "makers_heading": "Quatre mains qui complètent notre table.",
        "makers_intro":
            "Les produits du podere ne suffisent pas pour la table de tous "
            "les hôtes · depuis quatre générations la famille Pasquinelli "
            "s'appuie sur les mêmes producteurs du territoire pour faire "
            "tenir son hospitalité paysanne. Tous à moins de trente "
            "kilomètres.",
        "makers": [
            {
                "craft":    "Berger · pecorino au lait cru",
                "name":     "Andrea Falleri",
                "place":    "Lamole · 4 km du podere",
                "since":    "Client de la famille depuis 1987",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "Les Pasquinelli me prennent le pecorino de Lamole depuis "
                    "que j'étais jeune homme. Mon grand-père le fournissait à "
                    "leur père, et maintenant c'est moi qui le donne à Maria. "
                    "C'est la manière dont les choses se transmettent ici.",
            },
            {
                "craft":    "Meunier · blé dur de Maremma",
                "name":     "Famille Bartoletti",
                "place":    "Roccastrada · 28 km du podere",
                "since":    "Moulin familial depuis 1820",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "Nous moulons le blé dur Senatore Cappelli à la meule de "
                    "pierre · Maria en fait les pâtes pour la tablée du "
                    "dimanche. Le goût de la farine d'autrefois, c'est le "
                    "goût de leurs pâtes.",
            },
            {
                "craft":    "Norcino · saucissons de Cinta Senese",
                "name":     "Davide Pieri",
                "place":    "Castelfiorentino · 22 km du podere",
                "since":    "Charcuterie familiale depuis 1958",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "Le père de Maria m'a appris à découper le porc dans les "
                    "règles de l'art en 1972. Aujourd'hui que Maria élève les "
                    "Cinta Senese du podere, c'est moi qui leur prépare les "
                    "saucissons.",
            },
            {
                "craft":    "Monastère · confiture de coing",
                "name":     "Sœurs de San Vivaldo",
                "place":    "Montaione · 18 km du podere",
                "since":    "Monastère en activité depuis le XVe siècle",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "Les sœurs du monastère préparent la confiture de coing "
                    "comme on le faisait au Quattrocento · cinq heures de "
                    "cuisson à feu doux. Maria la sert à table avec le "
                    "pecorino.",
            },
        ],

        # Provenance items — list[4] of dict[4 keys=icon,title,desc,place]
        "provenance_label":   "Le podere",
        "provenance_heading": "Treize hectares, quatre productions.",
        "provenance_intro":
            "Le podere compte 13 hectares cultivés directement par la "
            "famille Pasquinelli. Quatre productions historiques · "
            "oliveraie, vigne, potager, étable · sont encore conduites "
            "aux rythmes que Maria a appris de son père.",
        "provenance_items": [
            {
                "icon":  "🌿",
                "title": "Oliveraie historique",
                "desc": "2 400 oliviers de Moraiolo, Frantoio et Leccino · certains arbres ont plus de 200 ans · récolte à la main en novembre · pressage à froid sous 8 heures.",
                "place": "8 hectares sur le versant sud-est du podere",
            },
            {
                "icon":  "🍇",
                "title": "Vigne de Sangiovese",
                "desc": "1,8 hectare de Sangiovese (95%) avec petites parts de Canaiolo et Colorino · vendanges manuelles fin septembre · vinification dans la cave de la famille · mise en bouteille avant mai.",
                "place": "1,8 hectare sur le versant ouest · 380 m d'altitude",
            },
            {
                "icon":  "🥕",
                "title": "Potager de la cuisine",
                "desc": "1 hectare de potager de saison · tomates San Marzano, fagioli zolfini, safran, plantes aromatiques · aucun produit acheté pour la table de Maria sauf les citrons en hiver.",
                "place": "1 hectare à côté de la maison de maître",
            },
            {
                "icon":  "🐖",
                "title": "Porcherie de Cinta Senese",
                "desc": "8 bêtes de Cinta Senese (porc noir) élevées en semi-liberté · alimentation aux glands du bois du podere et à l'épeautre du potager · abattage local deux fois par an.",
                "place": "2,2 hectares de bois avec porcherie couverte",
            },
        ],

        # Care items — list[4] of tuple[2] · les quatre promesses d'hospitalité
        "care_label":   "Les quatre promesses de la maison",
        "care_heading": "Hospitalité paysanne : peu de règles, toujours tenues.",
        "care_items": [
            ("Tablée toujours avec Maria",
             "Chaque dîner est préparé et porté à table par Maria. "
             "Lorsqu'elle s'assied avec vous, c'est qu'elle a fini de "
             "servir — non pour vous divertir."),
            ("Aucun enregistrement automatique",
             "Carlo ou Giovanni vous accueillent au portail et vous "
             "accompagnent à la chambre. La clé est une vraie clé, en "
             "fer, avec le nom de la chambre. Aucune carte magnétique."),
            ("Petit-déjeuner jusqu'à 10h30",
             "Pain de Lorenzini chaud sorti du four du podere · "
             "confitures des sœurs de San Vivaldo · miel de la ruche · "
             "œufs des poules · café du mélange historique du podere."),
            ("Expédition à domicile après le séjour",
             "À votre départ, la dispensa vous prépare une caisse de "
             "six produits du podere à votre choix. Nous expédions à "
             "domicile sous une semaine · seul le coût de l'expédition "
             "est à part."),
        ],

        # Press strip — list[5] of scalar str
        "press_label":   "Revue de presse du podere",
        "press_items": [
            "Slow Food Florence",
            "Bell'Italia · Toscane rurale",
            "Touring Club Italiano",
            "Gambero Rosso · Agriturismi 2025",
            "Vie del Gusto · Chianti Classico",
        ],

        # Journal teaser
        "journal_teaser_label":   "Extrait du journal de campagne",
        "journal_teaser_heading": "Trois voix depuis Greve in Chianti.",
        "journal_teaser_link":    "Lire le journal",
        "journal_teaser_href":    "diario",

        # Final CTA
        "cta_label":          "Pour réserver la tablée",
        "cta_heading":        "<em>Quatre chambres</em>, une seule tablée, une seule famille.",
        "cta_intro":
            "Les quatre chambres du podere se réservent directement avec "
            "Maria par WhatsApp ou téléphone. La tablée du dîner se "
            "réserve à l'arrivée · nous cuisinons pour le nombre que "
            "vous êtes.",
        "cta_primary":        "Écrivez à Maria via WhatsApp",
        "cta_primary_href":   "soggiorno",
        "cta_secondary":      "Téléphone direct en cuisine",
    },

    # ─── DISPENSA (shop · 8 farm products) ─────────────────────
    "dispensa": {
        "eyebrow":             "La dispensa paysanne",
        "headline":            "Huit produits du podere · expédition à domicile Italie 24-48h.",
        "intro":
            "La dispensa est le prolongement naturel de la cuisine de "
            "Maria et de l'hospitalité paysanne de la maison : les "
            "produits que vous mangez à table lorsque vous êtes en "
            "hôtes, vous les retrouvez ici pour les ramener chez vous. "
            "Expédition réfrigérée l'été, caisse en bois estampillée "
            "à la marque du podere.",
        "filter_section_label": "Affiner la dispensa",
        "filter_groups": [
            {
                "label":   "Production",
                "options": ["Huile d'olive EVO", "Vin", "Conserves", "Salaisons", "Pâtes · pain · douceurs"],
            },
            {
                "label":   "Saison",
                "options": ["Récolte 2025", "Vendanges 2022-2024", "Extraction juillet", "Affinage long", "Toujours disponibles"],
            },
            {
                "label":   "Caisse en bois",
                "options": ["Caisse de 6 produits · choix libre", "Caisse huile + vin", "Caisse petit-déjeuner (miel + confiture + cantucci)", "Caisse salaisons"],
            },
        ],
        "sort_label":      "Trier",
        "sort_options": [
            "Par production",
            "Par saison",
            "Par affinage",
            "Par disponibilité",
        ],
        "result_count":    "8 produits du podere dans la dispensa",
        "result_subtitle": "Six à la marque du podere + deux des producteurs du territoire · expédition à domicile Italie 24-48h.",
        "featured_product_id": "olio-evo-podere-2025",

        # 8 products — full dict shape (11 keys)
        "products": [
            {
                "id":         "olio-evo-podere-2025",
                "n":          "N° 01",
                "image":      _OLIO_BOTTLE,
                "edition":    "Récolte 2025",
                "name":       "Huile d'olive extra vierge du Podere",
                "meta":       "Moraiolo 60% + Frantoio 25% + Leccino 15% · pressage à froid sous 8 heures après la récolte",
                "place":      "Greve in Chianti",
                "artisan":    "Maria + Carlo Pasquinelli",
                "price":      "€ 28 / 500 ml",
                "tag":        "Récolte de novembre",
                "available":  True,
            },
            {
                "id":         "chianti-classico-2022",
                "n":          "N° 02",
                "image":      _VINO_BOTTLE,
                "edition":    "Vendanges 2022",
                "name":       "Chianti Classico DOCG",
                "meta":       "Sangiovese 95% · Canaiolo 4% · Colorino 1% · grand foudre + 6 mois bouteille",
                "place":      "Vigne du podere · 1,8 ha · 380 m d'altitude",
                "artisan":    "Giovanni Pasquinelli · œnologue du podere",
                "price":      "€ 22 / 750 ml",
                "tag":        "Cave du podere",
                "available":  True,
            },
            {
                "id":         "vin-santo-2018",
                "n":          "N° 03",
                "image":      _VINSANTO,
                "edition":    "Millésime 2018 · affinage 7 ans",
                "name":       "Vin Santo du Chianti",
                "meta":       "Malvasia bianca + Trebbiano · passerillage 4 mois · caratelli de 50 litres en chêne",
                "place":      "Grenier du podere · caratelli historiques",
                "artisan":    "Carlo Pasquinelli · maître de chai",
                "price":      "€ 32 / 375 ml",
                "tag":        "Demi-bouteille",
                "available":  True,
            },
            {
                "id":         "miele-millefiori",
                "n":          "N° 04",
                "image":      _MIELE,
                "edition":    "Extraction juillet 2025",
                "name":       "Miel toutes fleurs",
                "meta":       "12 ruches en clairière de châtaigniers · récolte de juillet · aucun traitement chimique · aucun nourrissement hivernal",
                "place":      "Bois du podere",
                "artisan":    "Anna Pasquinelli · apicultrice",
                "price":      "€ 14 / 250 g",
                "tag":        "Cent pour cent podere",
                "available":  True,
            },
            {
                "id":         "marmellata-susine",
                "n":          "N° 05",
                "image":      _MARMELLATA,
                "edition":    "Lot d'août 2025",
                "name":       "Confiture de prunes",
                "meta":       "Prunes reine-claude jaune · sucre 38% · sans pectine ajoutée · cuisson à feu doux 4 heures",
                "place":      "Potager du podere · 3 arbres historiques",
                "artisan":    "Maria Pasquinelli · cuisine",
                "price":      "€ 9 / 280 g",
                "tag":        "Petit lot",
                "available":  True,
            },
            {
                "id":         "pecorino-toscano-dop",
                "n":          "N° 06",
                "image":      _PECORINO,
                "edition":    "Affinage 6 mois",
                "name":       "Pecorino Toscano DOP",
                "meta":       "Lait cru de brebis · présure naturelle · affiné en grotte · brossé à l'huile EVO du podere",
                "place":      "Lamole · 4 km du podere",
                "artisan":    "Andrea Falleri · berger",
                "price":      "€ 24 / petite meule 600 g",
                "tag":        "Mains d'Andrea",
                "available":  True,
            },
            {
                "id":         "salame-cinta-senese",
                "n":          "N° 07",
                "image":      _SALAME,
                "edition":    "Affinage 9 mois",
                "name":       "Saucisson de Cinta Senese",
                "meta":       "Porcs Cinta Senese du podere · élevage en semi-liberté · abattage local · affinage dans la cave de pierre",
                "place":      "Porcherie du podere + charcuterie Pieri Castelfiorentino",
                "artisan":    "Davide Pieri · norcino",
                "price":      "€ 38 / pièce entière 700 g",
                "tag":        "8 bêtes en porcherie",
                "available":  True,
            },
            {
                "id":         "cantucci-mandorle",
                "n":          "N° 08",
                "image":      _CANTUCCI,
                "edition":    "Fournée hebdomadaire",
                "name":       "Cantucci aux amandes",
                "meta":       "Amandes non émondées · œufs du podere · sucre de canne · recette de la grand-mère Annetta de 1948",
                "place":      "Four du podere · cuisine de Maria",
                "artisan":    "Maria Pasquinelli · cuisine",
                "price":      "€ 12 / sachet 250 g",
                "tag":        "Recette de mamie Annetta",
                "available":  True,
            },
        ],

        "footer_note_label": "Expédition et caisse",
        "footer_note":
            "Tous les produits sont expédiés en caisse en bois marquée "
            "du podere · commandes au-dessus de € 80 expédition gratuite "
            "en Italie · sinon € 12 fixe. La caisse revient à votre "
            "discrétion · ou bien reste comme objet de cuisine.",
    },

    # ─── PRODOTTO (product page · featured = Huile EVO 2025) ──
    "prodotto": {
        "id":           "olio-evo-podere-2025",
        "n":            "N° 01",
        "edition":      "Récolte de novembre 2025",
        "edition_note": "Millésime 2025 limité à 1 800 bouteilles · lot 23/01",
        "name":         "Huile d'olive extra vierge du Podere",
        "subtitle":     "Moraiolo + Frantoio + Leccino · pressage à froid sous 8 heures",
        "price":        "€ 28 / bouteille 500 ml",
        "vat_note":     "TVA incluse · expédition 24-48h en Italie",
        "intro":
            "L'huile du Podere Le Querce est le produit historique de la "
            "maison · la famille Pasquinelli a toujours vendu sa propre "
            "huile d'olive extra vierge depuis les arrière-grands-parents "
            "Mario et Annetta. La récolte 2025 a été faite à la main par "
            "une dizaine de personnes (la famille plus quatre saisonniers) "
            "entre le 6 et le 19 novembre · pressage à froid sous huit "
            "heures.",

        # Gallery — list of scalar URL strings
        "gallery": [
            _OLIO_BOTTLE,
            _OLIVETO,
            _CUCINA_CONTADINA,
        ],

        "info_label": "Fiche technique",
        # info_rows — list[10] of tuple[2]
        "info_rows": [
            ("Cultivars",       "Moraiolo 60% · Frantoio 25% · Leccino 15%"),
            ("Récolte",         "Manuelle · 6-19 novembre 2025"),
            ("Pressage",        "À froid · sous 8 heures · 27 °C maximum"),
            ("Acidité",         "0,18% · sous le seuil d'excellence"),
            ("Polyphénols",     "412 mg/kg · valeur élevée"),
            ("Bouteille",       "Verre foncé 500 ml · bouchon à vis métallique"),
            ("Lot",             "23/01 sur 36 · étiquette numérotée à la main"),
            ("Conservation",    "Endroit frais · à l'abri de la lumière · sous 18 mois"),
            ("Distinctions",    "Slow Food Presidio · Gambero Rosso 2 feuilles 2025"),
            ("Disponibilité",   "1 800 bouteilles · disponibles jusqu'à épuisement"),
        ],

        "size_label":      "Formats disponibles",
        "size_intro":      "Bouteille seule de 500 ml, caisse de 6 bouteilles avec 12% de remise, ou bidon de 3 litres pour ceux qui cuisinent beaucoup.",
        # size_options — list[4] of SCALAR strings
        "size_options": [
            "Bouteille 500 ml",
            "Caisse de 6 bouteilles · 500 ml",
            "Bidon 3 litres",
            "Coffret cadeau · 2 bouteilles + cantucci",
        ],
        "size_chart_link":   "Tous les conditionnements de la dispensa",
        "size_chart_href":   "dispensa",

        "artisan_label":     "Mains de",
        "artisan_name":      "Maria + Carlo Pasquinelli",
        "artisan_role":      "Quatrième génération · au podere depuis 1985",
        "artisan_bio":
            "Maria Pasquinelli (née en 1962) et Carlo Pasquinelli (né en "
            "1960) ont pris les rênes du podere en 1985 après la mort de "
            "Mario, père de Maria. Depuis lors ils s'occupent de "
            "l'oliveraie en couple · Carlo dirige la récolte à la main, "
            "Maria supervise le pressage au moulin coopératif du Chianti. "
            "La famille n'a jamais utilisé de pesticides sur l'oliveraie.",
        "artisan_portrait":  _PORTRAIT_MARIA,

        "buy_primary":       "Ajouter à la caisse",
        "buy_secondary":     "Écrivez à Maria via WhatsApp",
        "buy_note":
            "Pour des commandes supérieures à 12 bouteilles écrivez "
            "directement à la famille · nous vous préparons une caisse "
            "spéciale et calculons la remise. Paiement à la livraison en "
            "Italie, virement bancaire pour l'Europe.",

        "care_label":  "Conservation et usage",
        "care_intro":
            "L'huile du podere est une huile à consommer crue · sur pain "
            "chaud, haricots, ribollita, bruschetta. Déconseillée pour "
            "les fritures.",
        # care_items — list[5] of tuple[2]
        "care_items": [
            ("Température",   "Conserver 14-18 °C · pas de réfrigérateur · pas de cuisine chaude"),
            ("Lumière",       "Bouteille en verre foncé · protéger tout de même de la lumière directe"),
            ("Consommation",  "Ouverte · à terminer sous 4 mois · ensuite la saveur s'atténue"),
            ("Sapidité",      "Vert, amer et piquant en équilibre · fruité moyennement intense"),
            ("Accord",        "Fagioli zolfini · pain sans sel · ribollita · bruschetta toscane"),
        ],

        "provenance_label":   "De l'oliveraie à la bouteille",
        "provenance_heading": "Quatre étapes à la main.",
        # provenance_steps — list[4] of 3-TUPLE (n, t, p)
        "provenance_steps": [
            ("01", "Récolte manuelle",       "Du six au dix-neuf novembre 2025 · 10 personnes · 6 semaines de récolte à la main · cageots de plastique perforé"),
            ("02", "Transport au moulin",    "Le jour même · sous 8 heures · 12 km jusqu'au moulin coopératif du Chianti"),
            ("03", "Pressage à froid",       "27 °C maximum · extraction mécanique · aucune eau ajoutée · aucune chaleur"),
            ("04", "Mise en bouteille",      "Mars 2026 · au podere · bouteille en verre foncé 500 ml · lot numéroté à la main"),
        ],

        "related_label": "Autres produits du podere",
        "related_intro": "Les produits de la même saison qui complètent la caisse.",
        # related_items — list[4] of dict[5 keys + n]
        "related_items": [
            {
                "id":    "chianti-classico-2022",
                "n":     "N° 02",
                "image": _VINO_BOTTLE,
                "name":  "Chianti Classico DOCG · 2022",
                "meta":  "Vin du même millésime historique · parfait avec la caisse huile",
                "price": "€ 22",
            },
            {
                "id":    "miele-millefiori",
                "n":     "N° 04",
                "image": _MIELE,
                "name":  "Miel toutes fleurs",
                "meta":  "12 ruches · clairière de châtaigniers · extraction de juillet",
                "price": "€ 14",
            },
            {
                "id":    "marmellata-susine",
                "n":     "N° 05",
                "image": _MARMELLATA,
                "name":  "Confiture de prunes",
                "meta":  "Prunes reine-claude · lot d'août · cuisson lente 4 heures",
                "price": "€ 9",
            },
            {
                "id":    "cantucci-mandorle",
                "n":     "N° 08",
                "image": _CANTUCCI,
                "name":  "Cantucci aux amandes",
                "meta":  "Recette de mamie Annetta · four hebdomadaire du podere",
                "price": "€ 12",
            },
        ],
    },

    # ─── FAMIGLIA (about · La famille Pasquinelli) ────────────
    "famiglia": {
        "eyebrow":  "La famille Pasquinelli",
        "headline": "Quatre générations à Le Querce.",
        "intro":
            "Le podere Le Querce est la maison de la famille Pasquinelli "
            "depuis novembre 1934. Les arrière-grands-parents Mario et "
            "Annetta l'ont acheté à la famille Antinori par un acte de "
            "vente conservé en mairie. Depuis lors quatre générations se "
            "sont succédé au podere · aujourd'hui à la barre se trouvent "
            "Maria et Carlo avec leurs enfants Giovanni et Anna, gardiens "
            "de la même hospitalité paysanne depuis quatre-vingt-douze ans.",

        "mission_label":   "Notre mission",
        "mission_heading": "Hospitalité paysanne telle que vous l'imaginez.",
        "mission_text":
            "Nous cuisinons pour nos hôtes la même cuisine que pour "
            "nous-mêmes · pas de menu de restaurant, pas de chariot de "
            "fromages, pas de sommelier. Il y a Maria qui apporte à table "
            "la ribollita qu'elle a préparée ce matin, Giovanni qui ouvre "
            "le vin qu'il a mis en bouteille au printemps, Anna qui "
            "tranche le pain qu'elle a enfourné à l'aube.",

        "process_label":   "Le calendrier de la famille",
        "process_heading": "Quatre saisons, quatre temps du podere.",
        # process_steps — list[4] of DICT[5 keys=n,title,place,desc,duration]
        "process_steps": [
            {
                "n":        "01",
                "title":    "Printemps · greffe et floraison",
                "place":    "Oliveraie + vigne + potager",
                "desc":
                    "Mars-mai · greffe des vignes, taille de l'oliveraie, "
                    "semis du potager · les quatre chambres rouvrent après "
                    "la fermeture technique de janvier. Tablée de Pâques "
                    "avec agneau de Zeri.",
                "duration": "Trois mois · mars-mai",
            },
            {
                "n":        "02",
                "title":    "Été · récolte et pleine hospitalité",
                "place":    "Tout le podere",
                "desc":
                    "Juin-août · pleine saison d'hospitalité paysanne · "
                    "tablées quotidiennes de 12-16 hôtes · récolte du miel "
                    "· récolte du blé · récolte des conserves d'été "
                    "(tomates, prunes, mûres, figues).",
                "duration": "Trois mois · juin-août",
            },
            {
                "n":        "03",
                "title":    "Septembre · vendanges",
                "place":    "Vigne + cave",
                "desc":
                    "Septembre · vendanges manuelles du Sangiovese · "
                    "dix-huit jours de travail continu dans la vigne · "
                    "cave fermée au public pendant les deux semaines de "
                    "vinification · tablée de clôture des vendanges avec "
                    "toute la famille et les saisonniers.",
                "duration": "Un mois · septembre",
            },
            {
                "n":        "04",
                "title":    "Automne-hiver · huile et cochon",
                "place":    "Oliveraie + porcherie + cuisine",
                "desc":
                    "Novembre · récolte des olives (six semaines) · "
                    "décembre abattage des Cinta Senese · janvier "
                    "fabrication des saucissons avec le norcino Pieri · "
                    "février fermeture technique du podere · mars "
                    "réouverture.",
                "duration": "Cinq mois · novembre-mars",
            },
        ],

        "founder_label":    "La matriarche",
        "founder_heading":  "Maria Pasquinelli · au podere depuis 1985.",
        "founder_text":
            "Maria Pasquinelli (née en 1962) est la troisième génération "
            "du podere · fille de Giovanni et Maddalena Pasquinelli, "
            "petite-fille des arrière-grands-parents Mario et Annetta qui "
            "ont acheté le podere aux Antinori. Elle a pris l'exploitation "
            "en main en 1985 après la mort de son père · mariée avec "
            "Carlo (d'un podere voisin) depuis 1987 · deux enfants "
            "Giovanni (1990) et Anna (1993) qui travaillent au podere à "
            "plein temps depuis 2015. En cuisine dès sept heures du "
            "matin, jusqu'à la tablée du soir avec les hôtes.",
        "founder_portrait":  _PORTRAIT_MARIA,
        "founder_caption":   "Maria Pasquinelli à la tablée du dimanche · photographie de Paolo Codeluppi · été 2024",

        "numbers_label": "Le podere en chiffres",
        # numbers_items — list[4] of tuple[2]
        "numbers_items": [
            ("92",  "Années de famille Pasquinelli au podere · depuis 1934"),
            ("13",  "Hectares cultivés directement · oliveraie + vigne + potager + bois"),
            ("4",   "Chambres d'hospitalité paysanne · toute la famille aux fourneaux"),
            ("8",   "Produits de la dispensa · six à la marque du podere + deux des producteurs du territoire"),
        ],

        "visit_label":          "Pour visiter le podere",
        "visit_heading":        "Tablée sur réservation · ou bien visite guidée.",
        "visit_text":
            "Visites guidées du podere sur réservation · mardi et jeudi "
            "après-midi (16h) pour les visiteurs non résidents. Tablée du "
            "soir (12-16 personnes · hospitalité paysanne complète) sur "
            "réservation au moins 48 heures à l'avance. Les quatre "
            "chambres se réservent directement avec Maria.",
        "visit_primary":         "Réservez la tablée",
        "visit_primary_href":    "soggiorno",
        "visit_secondary":       "WhatsApp direct à Maria",
    },

    # ─── DIARIO (journal · 3 entries) ─────────────────────────
    "diario": {
        "eyebrow":     "Journal de campagne",
        "headline":    "Trois voix depuis Greve in Chianti.",
        "intro":
            "Le journal du podere recueille les voix de la famille · "
            "Maria écrit une fois par mois depuis janvier 2018 · Giovanni "
            "et Anna ajoutent des notes de saison. Annotations de "
            "travail · non récits touristiques.",
        "list_label":  "Trois notes récentes",
        # entries — list[3] of dict[5 keys=n,title,place,excerpt,minutes]
        "entries": [
            {
                "n":       "001",
                "title":   "Vendanges 2025 · le jour de la pluie",
                "place":   "Vigne · 14 septembre 2025",
                "excerpt":
                    "La pluie est arrivée l'après-midi du dixième jour · "
                    "nous avons travaillé quand même · seulement trois "
                    "rangs à terminer. Giovanni a porté la grande cuve "
                    "sous la pergola · Maria a ouvert la cuisine · à dix "
                    "heures du soir nous étions tous à l'intérieur avec "
                    "la soupe de chou noir.",
                "minutes": "4 minutes de lecture",
            },
            {
                "n":       "002",
                "title":   "Récolte des olives 2025 · les arbres les plus anciens",
                "place":   "Oliveraie · 12 novembre 2025",
                "excerpt":
                    "Les oliviers de plus de deux cents ans ont donné "
                    "beaucoup moins cette année · la chaleur d'août les "
                    "a éprouvés. Carlo dit que l'olivier numéro 47 (le "
                    "plus ancien, plus de 350 ans selon le registre de "
                    "1923) n'a donné que 4 kg cette année contre 28 "
                    "l'année dernière. Nous continuerons à le soigner.",
                "minutes": "3 minutes de lecture",
            },
            {
                "n":       "003",
                "title":   "Anna commence l'apiculture · les trois premières ruches",
                "place":   "Bois du podere · 22 avril 2025",
                "excerpt":
                    "Anna a rapporté à la maison les trois premières "
                    "ruches du stage d'apiculture de Vinci. Elle les a "
                    "installées dans le bois du podere, là où se trouve "
                    "une clairière de châtaigniers. Maria dit que son "
                    "père avait gardé les abeilles jusqu'en 1972 · "
                    "ensuite plus personne. Nous verrons si elles "
                    "passent l'hiver.",
                "minutes": "5 minutes de lecture",
            },
        ],
        "footer_note_label": "Pour recevoir le journal",
        "footer_note":
            "Le journal n'a pas de newsletter automatique · si vous "
            "souhaitez le recevoir écrivez à Maria. Nous expédions une "
            "impression papier à la fin de l'année aux hôtes qui en "
            "font la demande.",
    },

    # ─── SOGGIORNO (contact · réservez la tablée) ────────────
    "soggiorno": {
        "eyebrow":  "Séjour · réservation directe",
        "headline": "Quatre chambres, une seule tablée.",
        "intro":
            "Les quatre chambres du podere se réservent directement avec "
            "la famille Pasquinelli · pas de plateforme externe, pas de "
            "commissions intermédiaires. Écrivez à Maria · elle vous "
            "répond personnellement dans la journée, généralement entre "
            "les pauses de la cuisine, dans le respect de "
            "l'hospitalité paysanne qui est la nôtre.",

        "form_section_label":   "Demande de séjour",
        "form_section_intro":
            "Indiquez les dates souhaitées, le nombre d'hôtes et toute "
            "demande particulière · allergies, intolérances, enfants, "
            "animaux. Maria répond depuis la cuisine sous 24 heures.",
        "form_helper_required": "Les champs marqués · sont obligatoires",
        "form_submit_button":   "Envoyez à Maria",
        "form_submit_note":
            "Confirmation définitive par acompte de 30% par virement "
            "bancaire · solde à l'arrivée à l'accueil du podere.",

        # form_fields — list[7] of dict[5 keys=label,name,type,required,placeholder]
        "form_fields": [
            {
                "label":       "Nom et prénom",
                "name":        "name",
                "type":        "text",
                "required":    True,
                "placeholder": "Comment vous vous présentez · Maria vous appellera par votre prénom",
            },
            {
                "label":       "Email direct",
                "name":        "email",
                "type":        "email",
                "required":    True,
                "placeholder": "Maria répond depuis famiglia@podereleQuerce.it",
            },
            {
                "label":       "WhatsApp · ou bien téléphone",
                "name":        "phone",
                "type":        "tel",
                "required":    False,
                "placeholder": "+39 339 458 1126 · Maria répond aussi par WhatsApp",
            },
            {
                "label":       "Date d'arrivée",
                "name":        "arrival",
                "type":        "date",
                "required":    True,
                "placeholder": "",
            },
            {
                "label":       "Date de départ",
                "name":        "departure",
                "type":        "date",
                "required":    True,
                "placeholder": "",
            },
            {
                "label":       "Nombre d'hôtes",
                "name":        "guests",
                "type":        "number",
                "required":    True,
                "placeholder": "Adultes + enfants",
            },
            {
                "label":       "Allergies, intolérances, animaux",
                "name":        "notes",
                "type":        "textarea",
                "required":    False,
                "placeholder": "Maria adapte la cuisine · dites-le-nous ici",
                "rows":        5,
            },
        ],

        # Contact card
        "card_label":            "Pour les réponses rapides",
        "card_address_label":    "Où nous sommes",
        "card_address_value":    "Località Le Querce 14 · 50022 Greve in Chianti · Florence",
        "card_phone_label":      "Cuisine · Maria",
        "card_phone_value":      "+39 055 853 261",
        "card_whatsapp_label":   "WhatsApp direct",
        "card_whatsapp_value":   "+39 339 458 1126 · Maria",
        "card_email_label":      "Email",
        "card_email_value":      "famiglia@podereleQuerce.it",
        "card_hours_label":      "Horaires",
        # card_hours_rows — list of SCALAR strings
        "card_hours_rows": [
            "Cuisine ouverte toute l'année · déjeuner 12h30 · dîner 19h30",
            "Accueil des hôtes 8h-22h · Maria en cuisine dès 7h",
            "Dispensa 9h-19h · fermée le dimanche (marché de Greve)",
            "Fermeture technique · 1er-28 février",
        ],
        "card_directions_label": "Comment venir",
        "card_directions_text":
            "Depuis Florence 28 km · sortie autoroute A1 Florence Sud · "
            "suivre la Chiantigiana · 12 km après Greve in Chianti tourner "
            "à droite vers Lamole · 1,4 km depuis l'embranchement. "
            "Portail en bois avec inscription « Podere Le Querce » à la "
            "main · sonnez au portier.",

        "faq_label": "Questions depuis la cuisine",
        # faq_items — list[5] of DICT[2 keys=q,a]
        "faq_items": [
            {
                "q": "La tablée se paie-t-elle même si nous sommes hôtes des chambres ?",
                "a":
                    "Oui · la cuisine et l'hospitalité paysanne sont deux "
                    "choses distinctes · les chambres se paient pour la "
                    "nuitée, la tablée se paie à part · 35 € par personne "
                    "pour le dîner, 28 € pour le déjeuner (vin du podere "
                    "compris). Le petit-déjeuner en revanche est compris "
                    "dans le prix de la chambre.",
            },
            {
                "q": "Acceptez-vous les enfants et les animaux ?",
                "a":
                    "Les enfants sont les bienvenus · nous avons des "
                    "petits lits pour les tout-petits, des chaises hautes "
                    "pour les plus grands · Anna se charge souvent de les "
                    "emmener à la porcherie voir les Cinta Senese. Les "
                    "petits chiens sont admis dans les chambres du bas "
                    "(supplément 15 € par nuit) · les grands dans la cour "
                    "et dans le bois, mais pas en chambre ni en cuisine.",
            },
            {
                "q": "Peut-on visiter le podere sans y dormir ?",
                "a":
                    "Oui · mardi et jeudi après-midi (16h, durée 90 "
                    "minutes, sur réservation au moins 24 heures à "
                    "l'avance) Carlo accompagne les visiteurs dans "
                    "l'oliveraie et à la cave · 20 € par personne · "
                    "dégustation d'huile + vin + miel comprise. Sans "
                    "réservation la dispensa est de toute façon ouverte "
                    "tous les jours 9h-19h.",
            },
            {
                "q": "Peut-on réserver le podere entier pour des mariages ou des événements ?",
                "a":
                    "Oui, pour des mariages intimes · maximum 36 hôtes · "
                    "cérémonie civile dans le jardin sous la pergola de "
                    "glycine · tablée sous la grange restaurée · écrire à "
                    "Maria au moins huit mois avant la date. Nous "
                    "n'organisons ni mariages de plus de 36 hôtes ni "
                    "événements d'entreprise — l'hospitalité paysanne "
                    "garde son échelle.",
            },
            {
                "q": "Peut-on acheter les produits sans venir au podere ?",
                "a":
                    "Oui · la dispensa expédie dans toute l'Italie (24-48 "
                    "heures, expédition gratuite au-dessus de € 80) et en "
                    "Europe (4-6 jours). Caisse en bois estampillée à la "
                    "marque du podere · revient à votre discrétion · pour "
                    "des commandes au-dessus de 12 bouteilles écrivez "
                    "directement à Maria pour une remise.",
            },
        ],
    },
}
