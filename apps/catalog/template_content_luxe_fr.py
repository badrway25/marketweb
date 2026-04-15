"""Luxe — Fashion Store (fashion-editorial archetype) — FR content tree.

Phase 2g3.5 — eCommerce live rollout (Session 41, 2026-04-14).

Voice contract (FR):
- Maison éditoriale italienne s'adressant à une clientèle francophone —
  registre Hermès / Le Bon Marché / Vogue Paris / AnOther Magazine French
  edition / Le Monde D'Hermès. « Vous » formel (jamais « tu » — c'est la
  règle de différenciation stricte avec Bottega FR, qui utilise « tu »),
  cadence éditoriale Vogue Paris, italiques de Cormorant sur les
  headlines, capitales en micro-grotesk pour les légendes.
- Détails concrets conservés : villes maison (Milan, Paris, Tokyo),
  étoffes (cachemire alpaga, cady double épaisseur, organza tressée de
  Côme, lin belge), ateliers (Sentier Paris, Brera Milan, Aoyama Tokyo),
  photographes + stylistes + références presse.
- « Lookbook », « drop », « capsule », « private viewing » (ou
  « rendez-vous privé »), « liste d'attente », « édition limitée » —
  jamais « panier » ni « tunnel de commande » : la conversion est un
  rendez-vous sur invitation.
- Drops semestriels (printemps-été · automne-hiver), chiffres de
  l'atelier (quarante-cinq pièces, neuf silhouettes), podium épinglé.
- Typographie française : espaces insécables avant « : ; ! ? % », format
  monétaire « 2 480 € » (chiffre suivi de l'euro avec espace insécable),
  guillemets français « » pour les citations éditoriales.

Differentiation contract vs Bottega FR (D-054 enforcement):
- Luxe FR utilise « vous », Bottega FR utilise « tu ». Les deux maisons
  francophones doivent rester lisiblement opposées.
- Luxe = maison éditoriale photographique (portraits mannequin, podium,
  intérieurs d'atelier, nature-morte d'accessoires). Bottega = atelier
  tactile (mains au travail, cuir brut, céramiques, métiers).
- Luxe vocabulaire : maison · collection · lookbook · couture · campagne ·
  capsule · drop · private viewing · rsvp · styliste · rendez-vous privé.
  Bottega FR vocabulaire à éviter ici : artisan · carnet · fait main ·
  WhatsApp · pièce unique.
- Luxe hero : cover pleine page GAUCHE + titre italique 108px Cormorant
  DROITE sur charbon. Bottega hero : monolithe typographique, sans photo.
"""
from __future__ import annotations

from typing import Any


LUXE_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Maison",     "kind": "home"},
        {"slug": "collezione", "label": "Collection", "kind": "collection"},
        {"slug": "product",    "label": "Look",       "kind": "product"},
        {"slug": "maison",     "label": "Atelier",    "kind": "about"},
        {"slug": "lookbook",   "label": "Lookbook",   "kind": "lookbook"},
        {"slug": "contatti",   "label": "Privé",      "kind": "contact"},
    ],

    # Site-wide chrome (consumed by _base.html nav + footer).
    "site": {
        "logo_initial": "L",
        "logo_word":    "Maison Luxe",
        "logo_subline": "Milan · Paris · Tokyo",
        "tag":          "Atelier · Printemps-Été 2026",
        "phone":        "+39 02 7600 1492",
        "private_phone_label": "Direction clientèle",
        "email":        "private@maisonluxe.com",
        "private_email_label": "Conciergerie clientèle",
        "address":      "Via Senato 28 · 20121 Milano",
        "showroom_paris": "9 rue du Mail · 75002 Paris",
        "showroom_tokyo": "1-1-7 Aoyama · Minato-ku · Tokyo",
        "hours_compact": "Mar – Sam · 11 h 00 – 19 h 00 · sur rendez-vous",
        "hours_footer_rows": [
            "Dimanche · privé",
            "Lundi · fermé",
        ],
        "license":      "Maison Luxe Srl · P.IVA 11489720152 · CCIAA Milano REA 2589441",
        "footer_intro":
            "Maison fondée à Milan en 2014 par Giulia Maison, avec atelier à Paris et "
            "salon d'accueil à Tokyo. Pièces dessinées et cousues entre Milan et Paris, "
            "en séries limitées, exclusivement sur liste d'attente. Drops semestriels "
            "de quarante-cinq pièces et neuf silhouettes.",

        # Nav reservation CTA (private viewing)
        "nav_cta":      "Demander un viewing",
        "nav_cta_kind": "appointment",  # links to /contatti/

        # Marketplace footer chrome labels
        "foot_studio":   "La maison",
        "foot_pages":    "Plan",
        "foot_contact":  "Direction clientèle",
        "foot_offices":  "Ateliers & salons",
        "office_rows": [
            "Milan · Via Senato 28",
            "Paris · 9 rue du Mail",
            "Tokyo · 1-1-7 Aoyama",
        ],

        # Cross-page meta-strip labels (D-047)
        "currency_symbol":  "€",
        "collection_label": "Collection",
        "drop_label":       "Drop",
        "season_label":     "Saison",
        "shipping_label":   "Livraison privée",
        "shipping_value":   "Coursier maison Milan · 24 h Italie · 72 h Europe",
        "viewing_label":    "Private viewing",
        "viewing_value":    "Uniquement sur rendez-vous · conciergerie dédiée",
        "waitlist_label":   "Liste d'attente",
        "rsvp_label":       "RSVP",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "issue":    "Issue 12 · Printemps '26",
        "issue_label": "Issue",
        "cover_styling_label": "Stylisme",
        "cover_styling_name":  "Carla Sozzani",
        "cover_label":         "Cover",
        "cover_subject":       "La Muse en Velours",
        "cover_image":
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1600&q=80&auto=format&fit=crop",

        "eyebrow":  "Lookbook · Printemps-Été 2026",
        "headline": "Le nouveau corps <em>du vêtement.</em>",
        "headline_credit_line": "Cinquante pièces · quatre-vingt-dix gestes de couture",
        "intro":
            "Une seule collection, tissée entre Côme et Prato, photographiée au Grand Hôtel "
            "Villa d'Este. Drops mensuels, exclusivement pour les clientes inscrites sur "
            "liste d'attente. La maison ne vend jamais deux fois la même pièce.",

        "primary_cta":   "Accéder au lookbook",
        "primary_href":  "lookbook",
        "secondary_label":   "Direction créative",
        "secondary_name":    "Giulia Maison",

        # Editorial tile strip — 4 silhouettes pinned below hero
        "edition_label":   "Édition limitée",
        "edition_subline": "quatre pièces sélectionnées",
        "tiles": [
            {
                "id":       "rack-atelier",
                "tag":      "Nouveau",
                "name":     "Rack Atelier",
                "price":    "2 480 €",
                "image":    "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "bomber-siena",
                "tag":      "Capsule",
                "name":     "Bomber Siena",
                "price":    "1 290 €",
                "image":    "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "pelletteria-isola",
                "tag":      "Atelier",
                "name":     "Borsa Isola",
                "price":    "860 €",
                "image":    "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "tag":      "Archives",
                "name":     "Sessione Vogue",
                "price":    "1 940 €",
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200&q=80&auto=format&fit=crop",
            },
        ],

        # Manifesto / maison statement
        "manifesto_label":   "Maison statement",
        "manifesto_heading": "Quarante-cinq pièces <em>par saison, jamais une de plus.</em>",
        "manifesto_text":
            "Nous dessinons la collection deux fois par an, dans un atelier de cent quarante "
            "mètres carrés, entre Brera et Sentier. Chaque pièce est coupée à la main, cousue "
            "à la mesure de la cliente et signée par celle qui l'a réalisée. Aucun outlet, "
            "aucune solde, aucune marque revendue. Seulement ce qui est sorti de la maison.",

        # Atelier numbers — KPI strip
        "atelier_numbers_label":   "L'atelier en chiffres",
        "atelier_numbers": [
            ("12",     "années de maison"),
            ("45",     "pièces par saison"),
            ("9",      "silhouettes signées"),
            ("3",      "ateliers dans le monde"),
        ],

        # Lookbook teaser — editorial 3-tile
        "lookbook_teaser_label":   "Lookbook en cours",
        "lookbook_teaser_heading": "Dix-huit images, <em>une seule lumière.</em>",
        "lookbook_teaser_intro":
            "Photographié au Grand Hôtel Villa d'Este, sur le lac de Côme, à la lumière "
            "naturelle de mars. Stylisme signé Carla Sozzani, photographies de Letizia "
            "Carrera, direction artistique assurée par la maison.",
        "lookbook_teaser_link": "Feuilleter le lookbook",
        "lookbook_teaser_href": "lookbook",
        "lookbook_teaser_tiles": [
            {
                "title":   "Look 03 · Cady double épaisseur",
                "credit":  "Stylisme · Carla Sozzani",
                "image":   "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "title":   "Look 09 · Laine cardée de Biella",
                "credit":  "Photographie · Letizia Carrera",
                "image":   "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "title":   "Look 14 · Crêpe de soie de Côme",
                "credit":  "Atelier · Sentier Paris",
                "image":   "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1000&q=80&auto=format&fit=crop",
            },
        ],

        # Press / editorial mentions strip
        "press_label":   "Éditorial",
        "press_intro":   "Vue dans",
        "press_items":   ["Vogue Italia", "The Gentlewoman", "AnOther Magazine", "Le Monde D'Hermès", "Wallpaper*"],

        # Seasonal drop card
        "drop_label":    "Prochain drop",
        "drop_heading":  "SS26 · Capsule 04 — <em>la lumière de Côme.</em>",
        "drop_subhead":  "Ouverture de la liste d'attente · vendredi 24 avril, 11 h 00 CET",
        "drop_metadata": [
            ("Pièces",        "9 silhouettes"),
            ("Matière",       "Crêpe de soie · cady · alpaga"),
            ("Exclusivité",   "12 pièces par silhouette"),
            ("Ouverture",     "Liste d'attente · vendredi 24 avril"),
        ],
        "drop_cta":      "M'inscrire à la liste",
        "drop_cta_href": "contatti",

        # Private viewing CTA band
        "private_label":   "Private viewing",
        "private_heading": "Trois salons, <em>une pièce réservée pour Vous.</em>",
        "private_intro":
            "Les maisons de Milan, Paris et Tokyo sont ouvertes uniquement sur rendez-vous. "
            "La direction clientèle réserve une heure de salon, prépare les pièces de votre "
            "profil, et organise l'essayage avec la couturière. Service gracieux · "
            "conciergerie dédiée.",
        "private_primary":     "Demander un private viewing",
        "private_primary_href":"contatti",
        "private_secondary":   "Découvrir les ateliers",
        "private_secondary_href":"maison",
    },

    # ─── COLLEZIONE (shop list) ───────────────────────────────
    "collezione": {
        "season_chip":  "Printemps-Été 2026",
        "eyebrow":      "Collection complète · drop 04 · capsules 01–04",
        "headline":     "Quarante-cinq pièces, <em>neuf silhouettes signées.</em>",
        "intro":
            "L'intégralité de la collection Printemps-Été 2026, organisée par silhouette. "
            "Chaque pièce est exclusivement disponible sur liste d'attente : de la "
            "confirmation à la livraison, compter de quatre à six semaines.",

        "filter_label":  "Filtrer",
        "filter_groups": [
            {
                "label": "Silhouette",
                "options": ["Tailleur fluide", "Robe-manteau", "Pantalon wide", "Maille éditoriale", "Maroquinerie atelier"],
            },
            {
                "label": "Matière",
                "options": ["Cachemire alpaga", "Cady double épaisseur", "Crêpe de soie de Côme", "Laine cardée de Biella", "Cuir de Florence"],
            },
            {
                "label": "Disponibilité",
                "options": ["En showroom", "Liste d'attente ouverte", "Sold-out · sur réservation"],
            },
        ],
        "sort_label":    "Trier",
        "sort_options":  ["Par silhouette", "Par drop", "Prix croissant", "Nouveautés"],

        "result_count":     "45 pièces dans la collection",
        "result_subtitle":  "Mise à jour le 1er de chaque mois, à la suite du drop",

        "products": [
            {
                "id":       "robe-manteau-grigio-perla",
                "n":        "Look 03",
                "name":     "Robe-manteau Gris Perle",
                "meta":     "Cachemire alpaga double · Maglificio Lanifer Biella",
                "drop":     "Drop 01 · Printemps 26",
                "price":    "2 840 €",
                "tag":      "Liste d'attente",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tailleur-cady-bianco",
                "n":        "Look 07",
                "name":     "Tailleur Cady Blanc",
                "meta":     "Cady double épaisseur · Setificio Tessitura Como",
                "drop":     "Drop 02 · Printemps 26",
                "price":    "3 420 €",
                "tag":      "En showroom",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "rack-atelier-nero",
                "n":        "Look 11",
                "name":     "Rack Atelier Noir",
                "meta":     "Cuir nappa de Florence · couture sellier",
                "drop":     "Drop 02 · Printemps 26",
                "price":    "2 480 €",
                "tag":      "Liste d'attente",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "bomber-siena",
                "n":        "Look 14",
                "name":     "Bomber Siena",
                "meta":     "Cady teint à Sienne · broderie Atelier Sentier",
                "drop":     "Drop 03 · Été 26",
                "price":    "1 290 €",
                "tag":      "Capsule",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "pantalone-wide-crepe",
                "n":        "Look 16",
                "name":     "Pantalon Wide Crêpe",
                "meta":     "Crêpe de soie de Côme · ceinture sellier",
                "drop":     "Drop 03 · Été 26",
                "price":    "1 180 €",
                "tag":      "Liste d'attente",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "borsa-isola",
                "n":        "Look 18",
                "name":     "Borsa Isola",
                "meta":     "Cuir Atelier Firenze · pochette de jour",
                "drop":     "Drop 03 · Été 26",
                "price":    "860 €",
                "tag":      "Atelier",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "abito-sera-organza",
                "n":        "Look 22",
                "name":     "Robe du soir Organza",
                "meta":     "Organza tressée de Côme · broderie Lesage",
                "drop":     "Drop 04 · Été 26",
                "price":    "4 690 €",
                "tag":      "Sold-out · réservable",
                "available":False,
                "image":    "https://images.unsplash.com/photo-1611042553365-9b101441c135?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "maglia-cashmere-corta",
                "n":        "Look 24",
                "name":     "Maille Cachemire Courte",
                "meta":     "Cachemire 12 fils · Maglificio Lanifer Biella",
                "drop":     "Drop 04 · Été 26",
                "price":    "1 420 €",
                "tag":      "Liste d'attente",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "n":        "Look 26",
                "name":     "Sessione Vogue",
                "meta":     "Manteau archives · drop 2024 réédition",
                "drop":     "Archives · 2024",
                "price":    "1 940 €",
                "tag":      "Archives",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
        ],

        "featured_product_id": "rack-atelier-nero",

        "footer_note_label": "Drop 04 à venir",
        "footer_note":
            "Les inscriptions au Drop 04 — capsule de la lumière de Côme — ouvrent le vendredi "
            "24 avril à 11 h 00 CET. Les clientes déjà inscrites sur liste d'attente bénéficient "
            "d'une priorité absolue sur toutes les silhouettes. Pour être ajoutée à la liste : "
            "écrire directement à la direction clientèle.",
    },

    # ─── PRODUCT DETAIL ───────────────────────────────────────
    "product": {
        "id":       "rack-atelier-nero",
        "n":        "Look 11 · Drop 02",
        "name":     "Rack Atelier Noir",
        "subtitle": "Cuir nappa de Florence · couture sellier · filet or",
        "price":    "2 480 €",
        "vat_note": "TVA incluse · livraison coursier maison · 24 h Italie",
        "tag":      "Liste d'attente · Drop 02 SS26",
        "intro":
            "Sac jour-soir en cuir nappa de Florence, cousu main à l'atelier de Sentier "
            "avec couture sellier or sur trois côtés. Filet patiné à la cire d'abeille, "
            "fond renforcé en vachette. Dessiné sur le corps de la directrice créative, "
            "produit en douze exemplaires numérotés, signé au fond par l'atelier qui "
            "l'a réalisé.",

        "gallery": [
            "https://images.pexels.com/photos/35115815/pexels-photo-35115815.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=1800&w=1400",
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1591561954557-26941169b49e?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1611042553365-9b101441c135?w=1400&q=80&auto=format&fit=crop",
        ],

        # Editorial caption strip below gallery
        "gallery_caption_styling":  "Stylisme · Carla Sozzani",
        "gallery_caption_photo":    "Photographie · Letizia Carrera",
        "gallery_caption_location": "Grand Hôtel Villa d'Este · mars 2026",

        # Right-side info panel — italic captioned
        "info_label":  "Spécifications atelier",
        "info_rows": [
            ("Atelier",        "Sentier · Paris"),
            ("Matière",        "Nappa de Florence · tannage végétal"),
            ("Couture",        "Sellier or sur trois côtés · fil ciré"),
            ("Filet",          "Cire d'abeille · poli à la main"),
            ("Fond",           "Vachette renforcée · pieds laiton"),
            ("Hardware",       "Laiton plaqué or 24 carats"),
            ("Dimensions",     "32 × 24 × 12 cm · bandoulière 105 cm"),
            ("Réalisation",    "21 heures d'atelier par pièce"),
        ],

        # Sizing / variant card (silhouette comes in 2 dimensions + 3 tonalities)
        "size_label":    "Dimension",
        "size_options":  ["Day · 32 × 24", "Evening · 25 × 18"],
        "color_label":   "Tonalité",
        "color_options": ["Noir de nuit", "Bordeaux de Côme", "Ivoire crème"],

        # Edition note
        "edition_label": "Édition",
        "edition_value": "12 exemplaires numérotés · n° 03/12 disponible",
        "edition_note":
            "Chaque exemplaire est marqué à froid à l'intérieur avec le numéro progressif, "
            "le nom du sellier principal et la date de livraison en atelier.",

        # Atelier signature
        "atelier_label":   "Signé par l'atelier",
        "atelier_name":    "Atelier Sentier · Paris",
        "atelier_founded": "Ouvert en 2017",
        "atelier_text":
            "Atelier de maroquinerie en régie directe de la maison, rue du Mail. Six "
            "selliers formés aux écoles d'Hermès et de Goyard, une coupeuse, une cireuse. "
            "Ils travaillent exclusivement pour Maison Luxe — aucun tiers, aucune "
            "production blanche.",
        "atelier_portrait":
            "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=600&q=80&auto=format&fit=crop",

        # Buy band — private request style
        "buy_primary":   "Demander à la maison",
        "buy_primary_href":  "contatti",
        "buy_secondary": "M'ajouter à la liste d'attente",
        "buy_note":
            "Acquisition sur rendez-vous ou demande directe à la direction clientèle. Acompte "
            "de trente pour cent à la confirmation. Livraison en 4 à 6 semaines à compter de "
            "la commande, coursier maison Milan dans un écrin signé.",

        # Care section (italic editorial style)
        "care_label":   "Entretien de la pièce",
        "care_intro":
            "Le nappa de Florence est un cuir vivant : il prend la forme de celle qui le porte, "
            "s'assouplissant les premiers mois sans jamais perdre sa structure. Traité en atelier "
            "à la cire d'abeille neutre, il ne demande aucun entretien durant les deux premières "
            "années d'usage quotidien.",
        "care_items": [
            ("Nettoyage",       "Chiffon doux légèrement humide. Jamais de produits chimiques."),
            ("Hydratation",     "Cire d'abeille maison tous les douze mois. Stick fourni avec la pièce."),
            ("Conservation",    "Pochon en coton bio, jamais de plastique. Jamais au soleil direct."),
            ("Pluie",           "Séchage naturel à l'ombre. Ensuite, un passage de cire."),
        ],

        # Atelier provenance
        "provenance_label":   "Provenance",
        "provenance_heading": "Quatre étapes, <em>quatre signatures.</em>",
        "provenance_steps": [
            ("01", "Tannerie",        "Conceria della Madonna · Florence · tannage végétal 45 jours"),
            ("02", "Coupe",           "Atelier Sentier · Paris · coupe à main levée"),
            ("03", "Couture sellier", "Atelier Sentier · Paris · 21 heures par pièce"),
            ("04", "Emballage",       "Maison Milan · écrin et cordon signés"),
        ],

        # Related — three other atelier pieces
        "related_label":   "Du même atelier",
        "related_intro":   "Maroquinerie signée Sentier · Paris.",
        "related_items": [
            {
                "id":      "borsa-isola",
                "n":       "Look 18",
                "name":    "Borsa Isola",
                "meta":    "Pochette de jour · Atelier Sentier",
                "price":   "860 €",
                "image":   "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "rack-atelier",
                "n":        "Look 09",
                "name":     "Rack Atelier Crème",
                "meta":     "Sac de jour · Atelier Sentier",
                "price":    "2 480 €",
                "image":    "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "n":        "Look 26",
                "name":     "Manteau Sessione Vogue",
                "meta":     "Manteau archives · drop 2024",
                "price":    "1 940 €",
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
        ],
    },

    # ─── MAISON (about) ───────────────────────────────────────
    "maison": {
        "eyebrow":  "La maison",
        "headline": "Trois villes, <em>une seule signature.</em>",
        "intro":
            "Maison Luxe a été fondée à Milan en 2014 par Giulia Maison, après huit années "
            "passées entre Hermès et Bottega Veneta. Elle dessine aujourd'hui deux collections "
            "par an, dans des ateliers partagés entre Brera et Sentier, et ne reçoit que sur "
            "rendez-vous dans les trois maisons de Milan, Paris et Tokyo. Quarante-cinq pièces "
            "par saison, jamais une de plus.",

        # Maison statement panel
        "statement_label":   "Statement",
        "statement_heading": "Quarante-cinq pièces <em>par saison.</em>",
        "statement_text":
            "La quantité est un parti pris éditorial, non une contrainte. Chaque pièce doit "
            "pouvoir être dessinée par la directrice créative, coupée en atelier, cousue par "
            "une couturière qui la signe, photographiée pour le lookbook et suivie personnellement "
            "jusqu'à la livraison. Quarante-cinq est le nombre maximal qui nous permet de le "
            "faire bien.",

        # Atelier cards — 3 cities
        "ateliers_label":   "Les trois ateliers",
        "ateliers_heading": "Milan, Paris, <em>Tokyo.</em>",
        "ateliers_intro":
            "Trois maisons, une seule signature. Milan dessine et dirige. Paris coud et brode. "
            "Tokyo reçoit la cliente asiatique dans un salon privé d'Aoyama.",
        "ateliers": [
            {
                "city":   "Milan",
                "place":  "Via Senato 28 · Brera",
                "role":   "Atelier créatif · direction · couture",
                "since":  "Ouvert en 2014",
                "head":   "Giulia Maison · directrice créative",
                "team":   "Six couturières · deux coupeuses · une direction clientèle",
                "image":  "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=900&q=80&auto=format&fit=crop",
            },
            {
                "city":   "Paris",
                "place":  "9 rue du Mail · Sentier",
                "role":   "Atelier maroquinerie · couture sellier",
                "since":  "Ouvert en 2017",
                "head":   "Jean-Luc Berthier · maître sellier",
                "team":   "Six selliers · une coupeuse · une cireuse",
                "image":  "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=900&q=80&auto=format&fit=crop",
            },
            {
                "city":   "Tokyo",
                "place":  "1-1-7 Aoyama · Minato-ku",
                "role":   "Salon privé · réception clientèle",
                "since":  "Ouvert en 2021",
                "head":   "Yumi Tanaka · conciergerie",
                "team":   "Trois concierges · couturière itinérante",
                "image":  "https://images.unsplash.com/photo-1559563458-527698bf5295?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Direction credit
        "direction_label":   "Direction créative",
        "direction_name":    "Giulia Maison",
        "direction_role":    "Directrice créative · fondatrice",
        "direction_text":
            "Giulia Maison a étudié à Central Saint Martins à Londres, puis a travaillé huit "
            "ans entre Hermès et Bottega Veneta avant de fonder la maison en 2014. Son écriture "
            "est italienne, de Brera, mais sa main coupe en français. La maison est son studio.",
        "direction_portrait":
            "https://images.unsplash.com/photo-1624206112918-f140f087f9b5?w=600&q=80&auto=format&fit=crop",
        "direction_quote":
            "« La quantité est une décision, non une conséquence. Quarante-cinq pièces par "
            "saison, c'est le nombre qui nous permet de regarder chaque cliente en face. »",
        "direction_quote_attribution": "Giulia Maison · The Gentlewoman, 2025",

        # Press / editorial mentions
        "press_label":   "Éditorial",
        "press_heading": "Apparitions presse <em>récentes.</em>",
        "press_items": [
            {
                "magazine": "Vogue Italia",
                "issue":    "Avril 2026",
                "title":    "Le nouveau silence du luxe italien",
                "byline":   "Reportage · Sara Maino",
            },
            {
                "magazine": "The Gentlewoman",
                "issue":    "Spring 2025",
                "title":    "Forty-five pieces. Never one more.",
                "byline":   "Profile · Penny Martin",
            },
            {
                "magazine": "AnOther Magazine",
                "issue":    "AW25",
                "title":    "L'atelier de Sentier",
                "byline":   "Photo · Mark Borthwick",
            },
            {
                "magazine": "Le Monde D'Hermès",
                "issue":    "Numéro 84",
                "title":    "Filiation italienne",
                "byline":   "Texte · Stefano Tonchi",
            },
            {
                "magazine": "Wallpaper*",
                "issue":    "Mars 2025",
                "title":    "Une maison bien cachée",
                "byline":   "Atelier visit · Tony Chambers",
            },
        ],

        # Numbers
        "numbers_label":   "Chiffres de la maison",
        "numbers_items": [
            ("12",    "années depuis la fondation"),
            ("3",     "ateliers dans le monde"),
            ("45",    "pièces par saison"),
            ("9",     "silhouettes par drop"),
        ],

        # Visit card — 3 cities
        "visit_label":   "Visiter la maison",
        "visit_heading": "Trois maisons, <em>trois salons privés.</em>",
        "visit_text":
            "Les maisons de Milan, Paris et Tokyo sont ouvertes uniquement sur rendez-vous. La "
            "direction clientèle réserve un salon, prépare les pièces de votre profil et "
            "organise l'essayage avec la couturière. Service gracieux, en toute discrétion.",
        "visit_primary":   "Demander un rendez-vous",
        "visit_primary_href": "contatti",
    },

    # ─── LOOKBOOK ─────────────────────────────────────────────
    "lookbook": {
        "issue":     "Printemps-Été 2026",
        "issue_label":"Issue",
        "issue_n":   "Issue 12",
        "eyebrow":   "Lookbook · Issue 12",
        "headline":  "La lumière de <em>Côme, en mars.</em>",
        "intro":
            "Dix-huit images prises en trois journées de mars au Grand Hôtel Villa d'Este, "
            "sur le lac de Côme. Stylisme signé Carla Sozzani, photographie de Letizia Carrera, "
            "set design de Sebastiano Pellion di Persano. La lumière naturelle du matin a été "
            "le seul instrument d'éclairage.",

        # Credits panel
        "credits_label":   "Credits",
        "credits_rows": [
            ("Direction créative", "Giulia Maison · Maison Luxe Milan"),
            ("Stylisme",           "Carla Sozzani"),
            ("Photographie",       "Letizia Carrera"),
            ("Set design",         "Sebastiano Pellion di Persano"),
            ("Hair & make-up",     "Lina Hammar · Art + Commerce"),
            ("Mannequin",          "Sara Grace Wallerstedt · IMG Models"),
            ("Location",           "Grand Hôtel Villa d'Este · Cernobbio"),
            ("Tirage",             "Tirage analogique · Studio Riffraff Milan"),
        ],

        # Editorial grid — 6 looks
        "looks_label":   "Les dix-huit looks",
        "looks_intro":   "Six sélectionnés pour la presse, douze dans la bibliothèque privée.",
        "looks": [
            {
                "n":       "Look 03",
                "title":   "Cady double épaisseur",
                "outfit":  "Robe-manteau cady double · bottes en cuir Sentier",
                "credit":  "Stylisme · écharpe archives 2018",
                "image":   "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 07",
                "title":   "Tailleur Cady Blanc",
                "outfit":  "Veste + pantalon wide · chaussures Atelier Sentier · pochette Isola",
                "credit":  "Set · jardin des camélias",
                "image":   "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 09",
                "title":   "Laine cardée de Biella",
                "outfit":  "Manteau cardé · pantalon crêpe · bottine sellier",
                "credit":  "Manteau Maglificio Lanifer",
                "image":   "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 11",
                "title":   "Rack Atelier Noir",
                "outfit":  "Maille cachemire courte · pantalon crêpe · sac Atelier",
                "credit":  "Sac Atelier Sentier · 21 heures de travail",
                "image":   "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 14",
                "title":   "Crêpe de soie de Côme",
                "outfit":  "Bomber Siena · pantalon wide crêpe · sandale lacée",
                "credit":  "Étoffe Setificio Tessitura Como",
                "image":   "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 18",
                "title":   "Borsa Isola · jour",
                "outfit":  "Maille cardée · jean atelier · sac Isola",
                "credit":  "Sac Atelier Sentier · cuir Madonna",
                "image":   "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1200&q=80&auto=format&fit=crop",
            },
        ],

        # Editorial pull-quote
        "pullquote":
            "« Côme en mars est une chambre close. La maison en est ressortie avec dix-huit "
            "photographies qui la rendent lisible. »",
        "pullquote_attribution": "Carla Sozzani · styliste du lookbook",

        # Notes from set
        "notes_label":   "Notes du plateau",
        "notes_intro":
            "Trois journées de mars, soleil voilé, vent de nord-est. Le mannequin a posé sans "
            "interruption de sept heures à onze heures, dans la lumière d'arrivée du matin. La "
            "veste cady du Look 03 a exigé deux heures de repassage chaque matin pour retrouver "
            "ses plis.",
        "notes_items": [
            {
                "label": "Jour 01 · Salon des camélias",
                "text":  "Sept looks en cinq heures de lumière. Changement de tenue entre deux "
                         "prises, dans la pièce attenante. Déjeuner à quinze heures.",
            },
            {
                "label": "Jour 02 · Belvédère sur le lac",
                "text":  "Six looks dans la lumière frontale du matin. Pluie fine entre onze "
                         "heures et midi : prise reportée à l'après-midi.",
            },
            {
                "label": "Jour 03 · Salon privé",
                "text":  "Cinq looks à la lumière de bougie et de fenêtre. Les trois dernières "
                         "photographies demandées par la directrice créative pour le pullquote "
                         "d'ouverture.",
            },
        ],

        # Buy from lookbook CTA
        "shop_label":   "Acheter depuis le lookbook",
        "shop_heading": "Chaque look conduit <em>à la pièce de la collection.</em>",
        "shop_intro":
            "Les dix-huit looks sont navigables depuis la collection complète. Pour solliciter "
            "une pièce, écrire à la direction clientèle — la liste d'attente ouvre le vendredi "
            "24 avril.",
        "shop_primary":     "Accéder à la collection",
        "shop_primary_href":"collezione",
        "shop_secondary":   "M'inscrire à la liste d'attente",
        "shop_secondary_href":"contatti",
    },

    # ─── CONTATTI (private appointment form) ──────────────────
    "contatti": {
        "eyebrow":  "Direction clientèle privée",
        "headline": "Uniquement sur <em>rendez-vous.</em>",
        "intro":
            "La maison reçoit exclusivement sur rendez-vous, dans trois salons privés à Milan, "
            "Paris et Tokyo. La direction clientèle prépare les pièces de votre profil avant "
            "votre arrivée et vous réserve la couturière pour l'essayage. Service discret, "
            "gracieux, sur demande directe.",

        # Form intro
        "form_section_label":  "Demande privée",
        "form_section_intro":
            "Nous vous prions de renseigner le formulaire avec les détails de votre rendez-vous "
            "ou de votre demande. La direction clientèle répond au cours de la journée ouvrée "
            "suivante. Pour la liste d'attente du Drop 04 — ouverture le 24 avril — sélectionner "
            "l'option dédiée.",

        "form_helper_required":  "Les champs marqués sont obligatoires",
        "form_submit_button":    "Envoyer la demande privée",
        "form_submit_note":
            "Vos données sont traitées exclusivement par la direction clientèle. Aucune "
            "newsletter, aucune communication commerciale.",

        "form_fields": [
            {"name":"titolo",    "label":"Titre",     "type":"select", "required":True,
             "options":["Madame","Monsieur","Mx","Studio·Atelier","Presse·Media"]},
            {"name":"nome",      "label":"Nom et prénom", "type":"text", "placeholder":"Ex. Madame Éléonore Cattaneo", "required":True},
            {"name":"email",     "label":"E-mail",          "type":"email", "placeholder":"e.cattaneo@exemple.fr",      "required":True},
            {"name":"telefono",  "label":"Téléphone",       "type":"tel",   "placeholder":"+33 …",                      "required":False},
            {"name":"city",      "label":"Maison d'intérêt", "type":"select", "required":True,
             "options":["Milan · Via Senato","Paris · Sentier","Tokyo · Aoyama","Indifférent"]},
            {"name":"servizio",  "label":"Service demandé", "type":"select", "required":True,
             "options":["Private viewing","Liste d'attente Drop 04","Pièce sur mesure","Réédition archives","Presse & media"]},
            {"name":"capo",      "label":"Look ou pièce (facultatif)", "type":"text", "placeholder":"Ex. Look 11 · Rack Atelier Noir", "required":False},
            {"name":"messaggio", "label":"Note à la direction clientèle", "type":"textarea", "placeholder":"Préciser la date souhaitée, les tailles, le profil personnel.", "required":True, "rows":5},
        ],

        # Right-side card — three maison addresses
        "card_label":   "Les trois maisons",
        "maison_cards": [
            {
                "city":    "Milan",
                "address": "Via Senato 28 · 20121 Milano",
                "phone":   "+39 02 7600 1492",
                "email":   "milano@maisonluxe.com",
                "hours":   "Mar – Sam · 11 h 00 – 19 h 00 · uniquement sur rendez-vous",
            },
            {
                "city":    "Paris",
                "address": "9 rue du Mail · 75002 Paris",
                "phone":   "+33 1 4296 4720",
                "email":   "paris@maisonluxe.com",
                "hours":   "Mar – Ven · 11 h 00 – 19 h 00 · uniquement sur rendez-vous",
            },
            {
                "city":    "Tokyo",
                "address": "1-1-7 Aoyama · Minato-ku · Tokyo 107-0062",
                "phone":   "+81 3 6450 5018",
                "email":   "tokyo@maisonluxe.com",
                "hours":   "Mer – Sam · 12 h 00 – 20 h 00 · uniquement sur rendez-vous",
            },
        ],

        # FAQ accordion (private viewing oriented)
        "faq_label":   "Questions fréquentes",
        "faq_items": [
            {
                "q": "Combien de temps à l'avance réserver un private viewing ?",
                "a": "Au moins une semaine pour Milan et Paris ; deux semaines pour Tokyo. "
                     "Pour toute demande urgente, écrire directement à la direction clientèle.",
            },
            {
                "q": "Le service de private viewing est-il payant ?",
                "a": "Non, il est gracieux et réservé. Il comprend la préparation des pièces, "
                     "la couturière en salon, café et champagne, ainsi qu'une carte "
                     "personnalisée de la collection.",
            },
            {
                "q": "Peut-on demander une pièce sur mesure ?",
                "a": "Oui, à partir des silhouettes existantes. Délais de livraison : de huit à "
                     "douze semaines. Acompte de cinquante pour cent à la confirmation du dessin.",
            },
            {
                "q": "Comment fonctionne la liste d'attente ?",
                "a": "Les clientes inscrites bénéficient d'une priorité absolue sur tous les "
                     "drops. L'inscription n'engage à aucun achat. Gratuite, sur demande directe.",
            },
        ],
    },
}
