"""Bottega — Boutique Artisanale (artisan-workshop archetype) — FR content tree.

Phase 2g3.5 — eCommerce live rollout (Session 41, 2026-04-14).

Voice contract (FR):
- Registre artisanal chaleureux à la française — inspiration Astier de
  Villatte, Merci (boulevard Beaumarchais), Le Bon Marché côté épicerie
  fine. Native FR, jamais une traduction mot-à-mot.
- Forme "tu" partout — la boutique parle comme un ami fabricant, jamais
  comme un service client. Posé, matériel, jamais mondain.
- Détails concrets : villes italiennes en italien (Santa Croce sull'Arno,
  Montelupo Fiorentino, Prato, Greve in Chianti, Firenze), matières
  ("cuir tanné végétal", "céramique tournée à la main", "lin tissé",
  "édition limitée", "signé par l'artisan"), gestes ("battre", "tourner",
  "tisser", "rempoter").
- Numéros d'édition (N° 042, 3/8) + signature de l'artisan partout.
- Schéma de conversion téléphone-et-WhatsApp : WhatsApp visible dans le
  CTA de nav, téléphone en footer, "visite à la boutique" comme CTA
  principal — jamais "passer à la caisse" comme s'il y avait un vrai
  panier.

Contrat de différenciation vs Luxe FR (D-054) :
- Bottega utilise "tu", registre provincial chaleureux, vocabulaire
  artisanal (boutique, atelier, cuir tanné végétal, tourné, tissé,
  signature, édition). Maison Luxe (séparément) utilise "vous",
  registre éditorial Hermès (maison, collection, lookbook, couture,
  campagne, capsule, drop, rendez-vous privé).
- Bottega CTA : téléphone-et-whatsapp (chaud, immédiat, par prénom).
- Si tu te retrouves à écrire "vous" ou en registre mode-maison, tu as
  dérivé — reviens au "tu" artisanal.

Contrat d'espace insécable : espace avant : ; ! ? %. EUR format "€ 420"
(€ à gauche, registre éditorial). Guillemets français « » pour les
citations d'artisans.
"""
from __future__ import annotations

from typing import Any


BOTTEGA_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Boutique",  "kind": "home"},
        {"slug": "shop",     "label": "Catalogue", "kind": "shop"},
        {"slug": "product",  "label": "Pièce",     "kind": "product"},
        {"slug": "atelier",  "label": "Atelier",   "kind": "about"},
        {"slug": "journal",  "label": "Carnet",    "kind": "journal"},
        {"slug": "contatti", "label": "Contact",   "kind": "contact"},
    ],

    # Site-wide chrome (consumed by _base.html nav + footer).
    "site": {
        "logo_initial": "M",
        "logo_word":    "La Bottega di Martino",
        "tag":          "Firenze · depuis 1968 · fait main",
        "phone":        "+39 055 234 11 90",
        "whatsapp":     "055 234 11 90",
        "whatsapp_link": "https://wa.me/390552341190",
        "email":        "bottega@bottegadimartino.it",
        "address":      "Via dei Serragli 47/r · 50124 Firenze",
        "hours_compact": "Mar – Sam · 10h00 – 19h30",
        "hours_footer_rows": [
            "Dimanche · uniquement sur rendez-vous",
            "Lundi · fermé",
        ],
        "license":      "P.IVA 04891240484 · CCIAA Firenze REA 502118",
        "footer_intro":
            "Boutique artisanale fondée en 1968 par Martino Boncompagni. "
            "Cuir, céramique et tissus faits main en Toscane, en petites "
            "éditions qui ne se répètent jamais. Expédition en 48 heures "
            "en Italie, deux jours de plus dans le reste de l'Europe.",
        # Nav CTA — primary action button next to nav links
        "nav_cta":      "Passe à la boutique",
        "nav_cta_kind": "appointment",  # links to /contatti/

        # Marketplace footer chrome labels
        "foot_studio":   "La boutique",
        "foot_pages":    "Plan du site",
        "foot_contact":  "Boutique & commandes",
        "foot_stockists":"Revendeurs choisis",
        "stockists_rows": [
            "10 Corso Como · Milano",
            "Eataly Lingotto · Torino",
            "Spazio B**K · Milano",
            "Atelier Pitti · Firenze",
        ],

        # Cross-page meta-strip labels (D-047 lifts on shop/product/atelier)
        "currency_symbol":  "€",
        "shop_filter_label": "Filtres",
        "shop_count_unit":   "pièces",
        "edition_label":     "Édition",
        "made_in_label":     "Fait à",
        "artisan_label":     "Signé par",
        "material_label":    "Matière",
        "shipping_label":    "Expédition",
        "shipping_value":    "48 heures en Italie · 4 jours en Europe",
        "guarantee_label":   "Garantie",
        "guarantee_value":   "Réparation gratuite pendant deux ans",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Catalogue d'automne · édition 47",
        "headline": "Des pièces uniques cousues, tournées et tissées <em>à l'atelier.</em>",
        "intro":
            "Cuir tanné végétal à Santa Croce sull'Arno, céramiques tournées à Montelupo "
            "Fiorentino, lin tissé à Prato. Chaque pièce porte la signature de l'artisan "
            "qui l'a faite — et un numéro progressif qui ne se répète jamais.",
        "primary_cta":   "Passe à la boutique",
        "primary_href":  "contatti",
        "secondary_cta": "Feuillette le catalogue",
        "secondary_href":"shop",

        # Stamp-aside data — the rubber-stamped right column of the hero
        "stamp_label":  "Notre règle",
        "stamp_heading":"Trois mains, <em>un objet.</em>",
        "stamp_rows": [
            ("Artisans",    "12 ateliers"),
            ("Matières",    "100 % italiennes"),
            ("Édition",     "Jamais au-dessus de 50"),
            ("Expédition",  "En 48 heures"),
        ],
        "stamp_footer": "Écrit à la main · emballé à la boutique",
        "stamp_corner_index": "01",
        "stamp_corner_word":  "LA BOUTIQUE",

        # Latest-arrived band — 4 product cards
        "latest_label":   "Les dernières venues",
        "latest_heading": "Tout juste sorties <em>de l'établi.</em>",
        "latest_link_label": "Tout le catalogue",
        "latest_link_href":  "shop",
        "latest_items": [
            {
                "id":       "giubbotto-terra",
                "n":        "N° 042",
                "edition":  "3 / 8",
                "name":     "Blouson Terra",
                "meta":     "Cuir tanné végétal · Santa Croce",
                "price":    "€ 420",
                "tag":      "Pièce unique",
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "camicia-lino",
                "n":        "N° 108",
                "edition":  "1 / 6",
                "name":     "Chemise en lin",
                "meta":     "Lin brut · Prato",
                "price":    "€ 95",
                "tag":      "Fait main",
                "image":    "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "ceramica-cucina",
                "n":        "N° 213",
                "edition":  "7 / 24",
                "name":     "Service de cuisine",
                "meta":     "Céramique émaillée · Montelupo",
                "price":    "€ 148",
                "tag":      "Édition",
                "image":    "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "conserve-chianti",
                "n":        "N° 317",
                "edition":  "12 / 60",
                "name":     "Conserves du marché",
                "meta":     "Tomates cerises · Chianti",
                "price":    "€ 18",
                "tag":      "Saison",
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Makers band — 4 artisans with portrait
        "makers_label":   "Des mains qui signent",
        "makers_heading": "Douze ateliers, <em>une seule enseigne.</em>",
        "makers_intro":
            "On ne travaille qu'avec des artisans qu'on appelle par leur prénom. "
            "Chaque pièce qui sort de notre enseigne porte leur signature — parce "
            "que celui qui l'a faite a le droit d'y mettre son visage.",
        "makers": [
            {
                "name":   "Severino Falchi",
                "craft":  "Maître tanneur",
                "place":  "Santa Croce sull'Arno",
                "since":  "À l'atelier depuis 1989",
                "quote":  "« Un bon cuir, tu le reconnais à l'odeur. S'il sent le produit chimique, ce n'est pas nous qui l'avons tanné. »",
                "portrait": "https://images.unsplash.com/photo-1581094271901-8022df4466f9?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Caterina Lippi",
                "craft":  "Tourneuse de terre cuite",
                "place":  "Montelupo Fiorentino",
                "since":  "Atelier ouvert en 2003",
                "quote":  "« Chaque pièce passe trois fois au four. Si à la troisième elle ne chante pas, je la casse. »",
                "portrait": "https://images.unsplash.com/photo-1604881991720-f91add269bed?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Bruno Ricci",
                "craft":  "Tisserand de lin",
                "place":  "Prato · Via del Telaio",
                "since":  "Métier à main depuis 1976",
                "quote":  "« Le lin brut est une plante. Ça se traite comme le pain : avec patience et avec faim. »",
                "portrait": "https://images.unsplash.com/photo-1521119989659-a83eee488004?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Adele Pignatelli",
                "craft":  "Confiturière du Chianti",
                "place":  "Greve in Chianti",
                "since":  "Trois générations de bocaux",
                "quote":  "« La confiture se fait quand le fruit le veut. Pas quand c'est le calendrier qui décide. »",
                "portrait": "https://images.unsplash.com/photo-1607743386760-88ac62b89b8a?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Provenance trio — 3 cards on materials & places
        "provenance_label":   "Provenance",
        "provenance_heading": "Trois territoires, <em>trois matières.</em>",
        "provenance_intro":
            "Rien ne vient de plus de deux cents kilomètres. La matière première est la "
            "première signature de l'artisan : s'il sait te dire où il l'a prise, il te "
            "dit comment il l'a travaillée.",
        "provenance_items": [
            {
                "icon":  "01",
                "title": "Cuir du Valdarno",
                "desc":  "Tanné végétal à l'écorce de châtaignier et de mimosa. "
                         "Quarante jours en cuve, jamais de chrome, jamais de raccourci. "
                         "Fournisseur unique : Conceria Falchi, Santa Croce sull'Arno.",
                "place": "Santa Croce sull'Arno · 38 km de Firenze",
            },
            {
                "icon":  "02",
                "title": "Argile de Montelupo",
                "desc":  "Argile rouge locale, émaillée à froid avec des oxydes naturels. "
                         "Trois cuissons à 980° au four à bois. Tournage à main levée.",
                "place": "Montelupo Fiorentino · 22 km de Firenze",
            },
            {
                "icon":  "03",
                "title": "Lin de Prato",
                "desc":  "Lin brut non blanchi, tissé sur un métier mécanique des années 50. "
                         "Trame large, chaîne serrée. Chaque rouleau a un poids différent.",
                "place": "Prato · 24 km de Firenze",
            },
        ],

        # Care / guarantee strip
        "care_label":   "Garanties & entretien",
        "care_heading": "Réparé à la boutique, <em>à vie.</em>",
        "care_items": [
            ("Réparation gratuite deux ans",
             "Anse décousue, émail ébréché, broderie desserrée : on remet la pièce d'aplomb nous-mêmes, à l'atelier."),
            ("Retour accepté sept jours",
             "Si la pièce ne te convient pas, on la reprend à la boutique sans frais et sans questions."),
            ("Expédition en 48 heures",
             "On expédie de Firenze le lendemain de la commande, dans un paquet en papier épais et ficelle."),
            ("Paiement sûr",
             "Carte ou virement. Pas d'abonnement, pas de compte, pas de cookie publicitaire."),
        ],

        # Press / stockists strip
        "press_label":   "On parle de nous",
        "press_items":   ["Vogue Italia", "Domus", "La Repubblica", "Apartamento", "Cereal Magazine"],

        "journal_teaser_label":   "Du carnet",
        "journal_teaser_heading": "Notes d'atelier, <em>écrites à la main.</em>",
        "journal_teaser_link":    "Ouvre le carnet",
        "journal_teaser_href":    "journal",

        # Final CTA band
        "cta_label":   "Passe à la boutique",
        "cta_heading": "Viens nous voir à Firenze, <em>on te fait un café.</em>",
        "cta_intro":
            "La boutique est via dei Serragli, à deux pas du Palais Pitti. Ouverte du mardi au "
            "samedi, de dix heures à dix-neuf heures trente. On te montre comment on tanne le "
            "cuir, comment on tourne une assiette et — si tu veux — on te présente les artisans "
            "en personne.",
        "cta_primary":   "Réserve une visite",
        "cta_primary_href": "contatti",
        "cta_secondary": "Écris-nous sur WhatsApp",
        # cta_secondary_href is rendered as site.whatsapp_link
    },

    # ─── SHOP ─────────────────────────────────────────────────
    "shop": {
        "eyebrow":  "Catalogue · 47ᵉ édition",
        "headline": "Tout <em>l'établi,</em> grand ouvert.",
        "intro":
            "Quarante-sept pièces uniques, douze artisans, trois territoires. "
            "Chaque numéro est progressif depuis 1968 et ne se répète jamais. Filtre par "
            "matière, par artisan ou par disponibilité.",

        "filter_section_label": "Filtrer par",
        "filter_groups": [
            {
                "label": "Matière",
                "options": ["Cuir", "Céramique", "Lin & tissus", "Conserves", "Papier & reliure"],
            },
            {
                "label": "Artisan",
                "options": ["Severino Falchi", "Caterina Lippi", "Bruno Ricci", "Adele Pignatelli", "Tous"],
            },
            {
                "label": "Disponibilité",
                "options": ["En boutique", "Sur réservation", "Édition épuisée"],
            },
        ],

        "sort_label": "Trier par",
        "sort_options": ["Dernières arrivées", "Numéro progressif", "Prix croissant", "Prix décroissant"],

        "result_count":    "47 pièces actuellement au catalogue",
        "result_subtitle": "Mis à jour le lundi matin, avant l'ouverture de la boutique",

        "products": [
            {
                "id":       "giubbotto-terra",
                "n":        "N° 042",
                "edition":  "3 / 8",
                "name":     "Blouson Terra",
                "meta":     "Cuir tanné végétal teint à la main",
                "place":    "Santa Croce sull'Arno",
                "artisan":  "Severino Falchi",
                "price":    "€ 420",
                "tag":      "Pièce unique",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "borsa-cartolina",
                "n":        "N° 056",
                "edition":  "2 / 12",
                "name":     "Sac Cartolina",
                "meta":     "Cuir naturel + couture sellier",
                "place":    "Santa Croce sull'Arno",
                "artisan":  "Severino Falchi",
                "price":    "€ 280",
                "tag":      "Pièce unique",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "camicia-lino",
                "n":        "N° 108",
                "edition":  "1 / 6",
                "name":     "Chemise en lin",
                "meta":     "Lin brut non blanchi",
                "place":    "Prato",
                "artisan":  "Bruno Ricci",
                "price":    "€ 95",
                "tag":      "Fait main",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tovaglia-armaiolo",
                "n":        "N° 134",
                "edition":  "5 / 30",
                "name":     "Nappe Armaiolo",
                "meta":     "Lin & coton · trame large",
                "place":    "Prato",
                "artisan":  "Bruno Ricci",
                "price":    "€ 165",
                "tag":      "Édition",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "ceramica-cucina",
                "n":        "N° 213",
                "edition":  "7 / 24",
                "name":     "Service de cuisine",
                "meta":     "Céramique émaillée à froid",
                "place":    "Montelupo Fiorentino",
                "artisan":  "Caterina Lippi",
                "price":    "€ 148",
                "tag":      "Édition",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tazze-tornite",
                "n":        "N° 219",
                "edition":  "11 / 24",
                "name":     "Tasses tournées",
                "meta":     "Argile rouge locale · cuisson au bois",
                "place":    "Montelupo Fiorentino",
                "artisan":  "Caterina Lippi",
                "price":    "€ 78",
                "tag":      "Édition",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1610701596007-11502861dcfa?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "vassoio-noce",
                "n":        "N° 251",
                "edition":  "Épuisé",
                "name":     "Plateau en noyer",
                "meta":     "Noyer massif · finition à l'huile",
                "place":    "Pratovecchio",
                "artisan":  "Severino Falchi",
                "price":    "€ 210",
                "tag":      "Liste d'attente",
                "available": False,
                "image":    "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "conserve-chianti",
                "n":        "N° 317",
                "edition":  "12 / 60",
                "name":     "Conserves du marché",
                "meta":     "Tomates cœur de bœuf + huile d'olive extra",
                "place":    "Greve in Chianti",
                "artisan":  "Adele Pignatelli",
                "price":    "€ 18",
                "tag":      "Saison",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "marmellata-fichi",
                "n":        "N° 322",
                "edition":  "21 / 80",
                "name":     "Confiture de figues",
                "meta":     "Figues noires de septembre · cuisson lente",
                "place":    "Greve in Chianti",
                "artisan":  "Adele Pignatelli",
                "price":    "€ 14",
                "tag":      "Saison",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Featured product detail link — used by smoke and "see more"
        "featured_product_id": "giubbotto-terra",

        "footer_note_label": "Boutique",
        "footer_note":
            "Pas d'algorithme, pas de recommandation : le catalogue est rangé comme sur les "
            "étagères de la boutique. Si tu cherches une pièce précise, écris-nous sur "
            "WhatsApp — c'est nous qui répondons, une personne à la fois.",
    },

    # ─── PRODUCT (detail) ─────────────────────────────────────
    "product": {
        # Hero (uses featured_product_id from shop)
        "id":       "giubbotto-terra",
        "n":        "N° 042",
        "edition":  "3 / 8",
        "edition_note": "Édition de huit pièces · il en reste trois",
        "name":     "Blouson Terra",
        "subtitle": "Cuir tanné végétal · couture sellier · teint à la main",
        "price":    "€ 420",
        "vat_note": "TVA incluse · expédition 48 heures en Italie",
        "intro":
            "Un blouson court en cuir du Valdarno, tanné végétal pendant quarante jours avec "
            "de l'écorce de châtaignier et de mimosa. La teinte est posée à la main avec un "
            "chiffon de lin imbibé de pigment naturel terre de Sienne : chaque pièce prend "
            "la couleur d'une manière légèrement différente et aucune n'est jamais identique "
            "à la précédente.",

        "gallery": [
            "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=1200&q=80&auto=format&fit=crop",
        ],

        # Right-side info aside (the rubber-stamped data block)
        "info_label":  "Spécifications",
        "info_rows": [
            ("Matière",       "Cuir du Valdarno · tannage végétal"),
            ("Épaisseur",     "1,8 mm uniforme"),
            ("Teinte",        "Terre de Sienne · pigment naturel"),
            ("Couture",       "Point sellier, fil ciré"),
            ("Doublure",      "Lin brut non blanchi"),
            ("Boutons",       "Corne de bœuf · provenance Toscane"),
            ("Poids",         "780 g (taille M)"),
            ("Réalisation",   "11 jours à l'atelier"),
        ],

        # Sizing card
        "size_label":    "Tailles disponibles",
        "size_intro":    "Sur mesure possible sous trois semaines. Écris-nous sur WhatsApp.",
        "size_options":  ["S", "M", "L", "XL", "Sur mesure"],
        "size_chart_link": "Voir le guide des tailles",
        "size_chart_href": "atelier",

        # Made by
        "artisan_label": "Signé par",
        "artisan_name":  "Severino Falchi",
        "artisan_role":  "Maître tanneur · à l'atelier depuis 1989",
        "artisan_bio":
            "Severino tanne le cuir dans sa cuve depuis 1989. Il travaille avec ses deux fils "
            "et un neveu, et teint chaque peau à la main. Sa devise à la tannerie est "
            "« doucement, c'est mieux ».",
        "artisan_portrait":
            "https://images.unsplash.com/photo-1581094271901-8022df4466f9?w=400&q=80&auto=format&fit=crop",

        # Buy band
        "buy_primary":   "Mettre au panier",
        "buy_secondary": "Écris sur WhatsApp",
        "buy_note":
            "Carte, virement ou paiement à la remise si tu passes la chercher à la boutique. "
            "On expédie sous 48 heures, dans une boîte en papier épais et ficelle.",

        # Care
        "care_label":   "Entretien de la pièce",
        "care_intro":
            "Le cuir végétal demande peu et dure une vie. On l'a déjà traité à la tannerie "
            "à l'huile de lin crue. Pendant les premiers mois il va changer légèrement de "
            "couleur, s'éclaircir dans les plis — c'est normal et c'est voulu.",
        "care_items": [
            ("Nettoyage",     "Chiffon sec. Jamais de détergent, jamais d'alcool."),
            ("Hydratation",   "Huile de lin ou crème neutre une fois par an."),
            ("Réparation",    "Pendant deux ans, on la fait gratuitement à l'atelier."),
            ("Pluie",         "Sèche loin des sources de chaleur. Pas de sèche-cheveux."),
        ],

        # Provenance map
        "provenance_label":   "Provenance",
        "provenance_heading": "Trois étapes, <em>quarante kilomètres.</em>",
        "provenance_steps": [
            ("01", "Tannerie",    "Conceria Falchi · Santa Croce sull'Arno · 38 km"),
            ("02", "Teinture",    "Bottega di Martino · Firenze · 0 km"),
            ("03", "Couture",     "Bottega di Martino · Firenze · 0 km"),
            ("04", "Emballage",   "Papier boulanger de Greve in Chianti · 32 km"),
        ],

        # Related products band
        "related_label":   "Aussi de la même main",
        "related_intro":   "Des pièces nées dans le même atelier, de la même signature.",
        "related_items": [
            {
                "id":      "borsa-cartolina",
                "n":       "N° 056",
                "name":    "Sac Cartolina",
                "meta":    "Cuir naturel · Severino Falchi",
                "price":   "€ 280",
                "image":   "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":      "vassoio-noce",
                "n":       "N° 251",
                "name":    "Plateau en noyer",
                "meta":    "Noyer massif · Severino Falchi",
                "price":   "€ 210",
                "image":   "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":      "ceramica-cucina",
                "n":       "N° 213",
                "name":    "Service de cuisine",
                "meta":    "Céramique émaillée · Caterina Lippi",
                "price":   "€ 148",
                "image":   "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
        ],
    },

    # ─── ATELIER (about) ──────────────────────────────────────
    "atelier": {
        "eyebrow":  "L'atelier de via dei Serragli",
        "headline": "Une boutique <em>d'atelier.</em>",
        "intro":
            "Ouverte en 1968 par Martino Boncompagni, c'est aujourd'hui un espace de cent "
            "dix mètres carrés via dei Serragli, où douze artisans toscans apportent leurs "
            "pièces trois fois par semaine. Pas d'entrepôt central, pas de chaîne — tout ce "
            "que tu vois en vitrine est fait à moins de deux cents kilomètres d'ici.",

        # Mission stamp panel
        "mission_label":   "La règle de la boutique",
        "mission_heading": "Trois mains, un objet. <em>Toujours.</em>",
        "mission_text":
            "Chaque pièce passe entre trois mains : celle qui travaille la matière, celle "
            "qui finit, celle qui vérifie que le numéro progressif est écrit à la plume avant "
            "l'expédition. Aucune machine ne remplace la dernière signature. Si on ne peut "
            "pas faire passer une pièce par trois mains, on ne la fait pas.",

        # Process timeline — 5 steps
        "process_label":   "Le parcours",
        "process_heading": "De la matière première <em>à la ficelle.</em>",
        "process_steps": [
            {
                "n":    "01",
                "title":"On va chercher la matière",
                "place":"Valdarno · Mugello · Chianti",
                "desc": "Cuir des tanneries du Valdarno, argile rouge de Montelupo, "
                        "lin des métiers à tisser de Prato. On y va en personne, jamais par transporteur.",
                "duration": "Une semaine par mois",
            },
            {
                "n":    "02",
                "title":"On la laisse reposer",
                "place":"Atelier · pièce de derrière",
                "desc": "Le cuir reste en cuve quarante jours. L'argile sèche lentement à l'air "
                        "libre. Le lin attend que le temps change. Aucun cycle accéléré.",
                "duration": "De deux semaines à trois mois",
            },
            {
                "n":    "03",
                "title":"On la travaille à la main",
                "place":"Établi · verrière sur le jardin",
                "desc": "La pièce prend forme sous les mains de l'artisan principal. "
                        "Couture sellier, tournage à main levée, métier mécanique des années 50.",
                "duration": "De quatre à douze jours",
            },
            {
                "n":    "04",
                "title":"On la finit",
                "place":"Atelier · établi d'Anna",
                "desc": "Anna contrôle, ponce, teint. Elle ajoute le numéro progressif. "
                        "Si la pièce ne passe pas son contrôle, elle repart à l'établi principal.",
                "duration": "Une demi-journée par pièce",
            },
            {
                "n":    "05",
                "title":"On emballe",
                "place":"Atelier · table d'emballage",
                "desc": "Papier boulanger de Greve, ficelle de chanvre, mot écrit à la main "
                        "avec le prénom de celui qui a fait la pièce. Expédition depuis Firenze en 48 heures.",
                "duration": "Le jour même de l'expédition",
            },
        ],

        # Founder
        "founder_label":   "Qui on est",
        "founder_heading": "Martino, Anna, <em>et douze ateliers.</em>",
        "founder_text":
            "Martino a ouvert en 68 avec un établi de trois mètres et une balle de cuir. Aujourd'hui "
            "il tient la boutique avec sa nièce Anna — lui reste plutôt à l'établi, elle s'occupe de "
            "ceux qui entrent, de ceux qui appellent, de ceux qui écrivent. Ensemble ils gardent "
            "le lien avec les douze artisans. Sans jamais devenir une entreprise.",
        "founder_portrait":
            "https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=600&q=80&auto=format&fit=crop",
        "founder_caption":
            "Martino Boncompagni et Anna Boncompagni · Boutique de via dei Serragli, Firenze",

        # Numbers stamp
        "numbers_label":   "Chiffres de la boutique",
        "numbers_items": [
            ("57",     "ans d'ouverture ininterrompue"),
            ("12",     "artisans qui signent pour nous"),
            ("47ᵉ",    "édition du catalogue"),
            ("0",      "machine industrielle"),
        ],

        # Visit card
        "visit_label":   "Viens nous voir",
        "visit_heading": "Via dei Serragli 47/r, <em>à deux pas du Palais Pitti.</em>",
        "visit_text":
            "La boutique est ouverte du mardi au samedi, de dix heures à dix-neuf heures trente. "
            "Le dimanche uniquement sur rendez-vous. Si tu passes le jeudi après-midi, il y a "
            "souvent un artisan en visite pour livrer les pièces. Le café et le livre d'or "
            "sont prêts.",
        "visit_primary":   "Réserve une visite",
        "visit_primary_href": "contatti",
        "visit_secondary": "Écris-nous sur WhatsApp",
    },

    # ─── JOURNAL ──────────────────────────────────────────────
    "journal": {
        "eyebrow":  "Le carnet de la boutique",
        "headline": "Notes d'atelier, <em>écrites à la plume.</em>",
        "intro":
            "Une page par mois, écrite par Anna dans les après-midis calmes. On y parle de "
            "ceux qui sont passés nous voir, d'une nouvelle matière qui est arrivée, d'une "
            "pièce qui a demandé le double du temps. Ce n'est pas un blog : c'est le journal "
            "de la boutique.",

        "list_label":  "Notes récentes",
        "entries": [
            {
                "n":      "47",
                "title":  "Un automne de teintes naturelles",
                "place":  "Boutique · 12 mars 2026",
                "excerpt":
                    "Severino est revenu de la tannerie avec six peaux teintes uniquement à "
                    "l'écorce de châtaignier. Sur le blouson Terra, c'est déjà la teinte du prochain lot.",
                "minutes":"3 minutes de lecture",
            },
            {
                "n":      "46",
                "title":  "Caterina et le four qui chante",
                "place":  "Montelupo · 22 février 2026",
                "excerpt":
                    "Caterina a refait le four à bois dans son atelier. La première cuisson a "
                    "été de six pièces et toutes ont chanté au refroidissement. C'est bon signe.",
                "minutes":"4 minutes de lecture",
            },
            {
                "n":      "45",
                "title":  "Le métier de Bruno reprend à battre",
                "place":  "Prato · 31 janvier 2026",
                "excerpt":
                    "Il était arrêté depuis deux mois pour le changement du peigne. Bruno a "
                    "repris à tisser lundi. La première pièce est une nappe en lin couleur sable.",
                "minutes":"5 minutes de lecture",
            },
            {
                "n":      "44",
                "title":  "Adele au marché de Greve",
                "place":  "Chianti · 14 décembre 2025",
                "excerpt":
                    "Adele est allée au marché de décembre pour prendre les figues tardives. "
                    "Les confitures de janvier viennent toutes de cette récolte.",
                "minutes":"3 minutes de lecture",
            },
            {
                "n":      "43",
                "title":  "Une journée à la tannerie",
                "place":  "Santa Croce · 8 novembre 2025",
                "excerpt":
                    "Anna a passé une journée chez Severino. On voit comment une peau entre "
                    "en cuve, se retourne tous les quatre jours, et après quarante ressort différente.",
                "minutes":"6 minutes de lecture",
            },
            {
                "n":      "42",
                "title":  "Conserves, livres et nouvelles mains",
                "place":  "Firenze · 19 octobre 2025",
                "excerpt":
                    "Depuis octobre, deux nouveaux artisans travaillent pour la boutique : un "
                    "relieur de livres de Pistoia et une papetière de San Frediano. Éditions à venir au printemps.",
                "minutes":"4 minutes de lecture",
            },
        ],

        "footer_note_label": "Carnet",
        "footer_note":
            "Les vieilles pages restent, on ne les met pas à jour. Si tu aimes recevoir le "
            "carnet en papier, écris-nous un mot — on te l'envoie à l'imprimé deux fois par an.",
    },

    # ─── CONTATTI (form) ──────────────────────────────────────
    "contatti": {
        "eyebrow":  "Viens nous voir",
        "headline": "Écris, appelle, <em>ou passe nous voir.</em>",
        "intro":
            "La boutique est via dei Serragli, à deux pas du Palais Pitti. Ouverte du mardi au "
            "samedi, de dix heures à dix-neuf heures trente. Si tu veux savoir si une pièce est "
            "encore en vitrine, écris-nous sur WhatsApp — on te répond dans l'heure.",

        # Two-column layout: left form, right contact card
        "form_section_label": "Envoie-nous deux lignes",
        "form_section_intro":
            "Il suffit du prénom, d'un contact, et de ce que tu cherches. C'est Anna qui te "
            "répond au plus tard le lendemain ouvré. Pour demander une pièce sur mesure, écris-le "
            "ci-dessous : on te renvoie un dessin avec les délais et les prix sous trois jours.",

        # Form helper
        "form_helper_required":  "Les champs avec astérisque sont obligatoires",
        "form_submit_button":    "Envoyer la demande",
        "form_submit_note":      "Aucune newsletter. On utilise tes lignes uniquement pour te répondre.",

        "form_fields": [
            {"name": "nome",          "label": "Prénom et nom",         "type": "text",     "placeholder": "Ex. Marie Dupont", "required": True},
            {"name": "email",         "label": "E-mail",                "type": "email",    "placeholder": "marie@exemple.fr", "required": True},
            {"name": "telefono",      "label": "Téléphone ou WhatsApp", "type": "tel",      "placeholder": "Facultatif · +33 …", "required": False},
            {"name": "interesse",     "label": "Ce qui t'intéresse",    "type": "select",   "required": True,
             "options": ["Une pièce du catalogue", "Une commande sur mesure", "Une visite à la boutique", "Une collaboration", "Presse & médias"]},
            {"name": "pezzo",         "label": "Pièce ou numéro (fac.)", "type": "text",    "placeholder": "Ex. N° 042 · Blouson Terra", "required": False},
            {"name": "messaggio",     "label": "Ta demande",            "type": "textarea", "placeholder": "Raconte-nous ce que tu cherches, même deux lignes suffisent.", "required": True, "rows": 5},
        ],

        # Right-side card
        "card_label":   "Bottega di Martino",
        "card_address_label":  "Adresse",
        "card_address_value":  "Via dei Serragli 47/r · 50124 Firenze",
        "card_phone_label":    "Téléphone",
        "card_phone_value":    "+39 055 234 11 90",
        "card_whatsapp_label": "WhatsApp",
        "card_whatsapp_value": "055 234 11 90",
        "card_email_label":    "E-mail",
        "card_email_value":    "bottega@bottegadimartino.it",
        "card_hours_label":    "Horaires d'ouverture",
        "card_hours_rows": [
            "Mardi – samedi · 10h00 – 19h30",
            "Dimanche · uniquement sur rendez-vous",
            "Lundi · fermé",
        ],
        "card_directions_label": "Comment venir",
        "card_directions_text":
            "Trois minutes à pied du Palais Pitti. Bus 11 arrêt Serragli. "
            "Depuis la gare SMN : quinze minutes à pied à travers le centre.",

        # FAQ accordion
        "faq_label":   "Questions fréquentes",
        "faq_items": [
            {
                "q": "Vous expédiez à l'étranger ?",
                "a": "Oui, dans toute l'Europe sous quatre jours ouvrés. Pour les États-Unis et "
                     "le Japon, écris-nous avant — on confirme les délais au cas par cas.",
            },
            {
                "q": "Je peux voir une pièce avant de l'acheter ?",
                "a": "Bien sûr. Mets-la de côté en appelant la boutique, et quand tu passes, on te "
                     "la fait voir sans engagement. Si elle ne te convainc pas, aucune pression.",
            },
            {
                "q": "Vous faites des commandes sur mesure ?",
                "a": "Oui, en cuir, en céramique et en tissu. Délais : de trois à huit semaines "
                     "selon la pièce. Acompte de trente pour cent à la confirmation du dessin.",
            },
            {
                "q": "Qu'est-ce qui se passe si la pièce casse ?",
                "a": "Pendant deux ans, on la remet en état à l'atelier sans frais. Pour les "
                     "réparations suivantes, on applique un coût symbolique — en général sous les trente euros.",
            },
        ],
    },
}
