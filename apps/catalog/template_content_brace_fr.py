"""Brace — Brace Street Lab (street-modern archetype) — FR content tree.

Phase 2g3.6 — Restaurant live-completion · Session 48 (FR locale agent).

Voice contract (FR):
- Le Fooding (street-food sections) / Time Out Paris food guides / Trax
  Magazine food register. Native French.
- Second-person `tu` imperative ("commande au comptoir", "passe", "balance").
- Direct, fast, urban, sharp. Anglicismes welcome ("le smash", "le drop",
  "le crew", "le pass", "late-night").
- UPPERCASE display headlines mirror IT big-shoulders display.
- Italian dish names stay Italian (Margherita, Marinara, Mortadella e
  pistacchio, Tortellini, Sangiovese). FR gets a parenthetical gloss only
  if obscure, never a translation.
- Italian proper names stay Italian (Brace Street Lab, Bologna, Via
  Indipendenza, Modena, Castelfranco, Tropea, Cervia).
- Currency FR: "9,50 €" (virgule décimale + espace + €).
- Tabular FR: LUN – DIM, LUN – JEU, VEN – SAM.
- Insecable spaces before : ; ! ? as per French typography (handled
  pragmatically — long copy reads natural rather than over-typeset).

Differentiation contract:
- Voice MUST stay sharply opposite from Sapore FR (warm Roman trattoria
  food-writer reportage `tu`) and from Gusto FR (Michelin editorial
  vouvoiement). Brace FR uses `tu` urban-imperative — short, punchy,
  street-food fast-casual. Anglicisme tolerance HIGH.
- Voice MUST stay sharply opposite from Bottega FR (artisan-warm Toscana
  Astier register). Brace FR is brutalist near-black + neon yellow.
"""
from __future__ import annotations

from typing import Any


BRACE_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Accueil",   "kind": "home"},
        {"slug": "menu",     "label": "Carte",     "kind": "menu"},
        {"slug": "lab",      "label": "Le Lab",    "kind": "about"},
        {"slug": "moments",  "label": "Moments",   "kind": "gallery"},
        {"slug": "ordina",   "label": "Commander", "kind": "order"},
        {"slug": "contatti", "label": "Nous trouver", "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "B",
        "logo_word":    "BRACE STREET LAB",
        "tag":          "Bologna · Via Indipendenza 42 · 12 h → 24 h",
        "phone":        "051 234 5566",
        "phone_tel":    "+390512345566",
        "phone_display": "051 234 5566",
        "whatsapp":     "051 234 5566",
        "whatsapp_link": "https://wa.me/390512345566",
        "email":        "ordini@bracestreetlab.it",
        "address":      "Via Indipendenza 42 · 40121 Bologna",
        "hours_compact": "TOUS LES JOURS · 12 h – 24 h · VEN/SAM JUSQU'À 01 H 30",
        "hours_footer_rows": [
            "LUN – JEU · 12 h – 24 h",
            "VEN – SAM · 12 h – 01 h 30",
            "DIM · 12 h – 24 h",
        ],
        "license":      "TVA IT 04127880371 · CCIAA Bologna REA 358912",
        "footer_intro":
            "Street food lab à Bologna. Smashburger de scottona piémontaise, "
            "fritures envoyées au moment, pizza al taglio sortie du four à bois. "
            "Tu commandes au comptoir, tu retires au numéro, tu bouffes au vol. "
            "Ouvert tard, tous les jours, dimanche compris.",
        "nav_cta":      "COMMANDE",
        "nav_cta_href": "ordina",
        "nav_phone_cta": "051 234 5566",
        "star_line":    "STREET FOOD LAB · BOLOGNA",
        "copyright":    "© 2026 Brace Street Lab · TVA IT 04127880371",

        # Mirror the fine-dining/_base.html footer keys used by the chrome
        "footer_hours_1": "LUN – JEU · 12 h – 24 h",
        "footer_hours_2": "VEN – SAM · 12 h – 01 h 30",

        # Social
        "instagram_handle": "@brace.lab",
        "instagram_link":   "https://instagram.com/brace.lab",
        "tiktok_handle":    "@brace.bologna",
        "tiktok_link":      "https://tiktok.com/@brace.bologna",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "STREET FOOD LAB · BOLOGNA",
        "headline": 'AU FEU VIF. <em>SERVI AU VOL.</em>',
        "intro":
            "Smashburger de scottona piémontaise, fritures contre-courant, pizza al "
            "taglio sortie du four à bois. Commande au comptoir, retire au numéro, "
            "balance au vol.",
        "primary_cta":   "COMMANDE",
        "primary_href":  "ordina",
        "secondary_cta": "LA CARTE",
        "secondary_href": "menu",

        # Hero product cutout
        "hero_image":       "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=1400&q=80&auto=format&fit=crop",
        "hero_alt":         "Doppio Brace smashburger close-up",
        "hero_badge_price": "9,50 €",
        "hero_badge_label": "DOPPIO BRACE",
        "hero_badge_tag":   "TOP",

        # Real-time queue counter strip
        "counter_label": "FILE AU COMPTOIR",
        "counter_value": "≈ 4 MIN",
        "counter_kitchen_label": "CUISINE OUVERTE",
        "counter_kitchen_value": "JUSQU'À 24 H",
        "counter_last_label":    "DERNIÈRE COMMANDE",
        "counter_last_value":    "23 H 30",

        # Stat band — 4 numbers
        "stats_label": "LES CHIFFRES DU LAB",
        "stats": [
            ("12 000",  "BURGERS / MOIS"),
            ("4,9 ★",   "SUR 1 380 AVIS"),
            ("100 %",   "SCOTTONA PIÉMONTAISE"),
            ("420 °C",  "FOUR À BOIS"),
        ],

        # Menu strip — 6 product-grid items on home (teaser of full menu)
        "menu_strip_label":   "DU PASS CE SOIR",
        "menu_strip_heading": 'LA CARTE <em>DU VOL.</em>',
        "menu_strip_intro":
            "Six pièces qui sortent chaudes du pass toutes les quinze minutes. "
            "Tu pointes, tu choisis, tu paies au comptoir, on t'appelle au numéro.",
        "menu_strip_cta":      "VOIR TOUTE LA CARTE",
        "menu_strip_cta_href": "menu",
        "menu_strip_items": [
            {
                "name":  "DOPPIO BRACE",
                "desc":  "double scottona, cheddar fondu, sauce brace",
                "price": "9,50 €",
                "tag":   "TOP",
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "SMASH CLASSICO",
                "desc":  "scottona simple, cheddar, oignon caramélisé",
                "price": "7,50 €",
                "tag":   "",
                "image": "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "FRITTO MISTO",
                "desc":  "frites, jalapeños panés, baccalà frit",
                "price": "6,00 €",
                "tag":   "PIQUANT",
                "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "PIZZA ROSSA",
                "desc":  "tomate San Marzano DOP, fior di latte, basilic",
                "price": "4,50 €",
                "tag":   "VEG",
                "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "FRIES BRACE",
                "desc":  "frites double cuisson, gros sel, sauce brace",
                "price": "4,50 €",
                "tag":   "",
                "image": "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "SODA BRACE",
                "desc":  "limonade maison au basilic frais",
                "price": "3,00 €",
                "tag":   "NEW",
                "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Delivery partners marquee strip
        "delivery_label":    "COMMANDE OÙ TU VEUX",
        "delivery_subtitle": "LIVRAISON EN 30 MINUTES · BOLOGNA CENTRE",
        "delivery_partners": [
            ("GLOVO",     "30 MIN", "MIN 12 €"),
            ("DELIVEROO", "25 MIN", "MIN 10 €"),
            ("JUST EAT",  "35 MIN", "MIN 15 €"),
            ("UBER EATS", "30 MIN", "MIN 12 €"),
        ],

        # Lab manifesto — 3 short bold paragraphs
        "manifesto_label":   "LE LAB",
        "manifesto_heading": 'POURQUOI LE FEU. <em>POURQUOI LE VOL.</em>',
        "manifesto_paragraphs": [
            "Brace, c'est un labo. Pas de papier peint, pas de nappes. Juste du "
            "fer, du feu et cinq personnes qui taffent à vue pendant cent quatre-"
            "vingts secondes par assiette.",

            "On bosse uniquement la scottona piémontaise, hachée le matin sur le "
            "comptoir avec le hachoir devant tout le monde. Chaque frite est "
            "coupée à la main à dix heures. Chaque sauce est faite dans le lab, "
            "jamais achetée.",

            "Tu passes quand tu veux. Ouvert de midi à minuit, tous les jours, "
            "dimanche compris. Le samedi, on tire jusqu'à une heure et demie. La "
            "cuisine ne ferme jamais avant le dernier qui rentre.",
        ],
        "manifesto_cta":      "DÉCOUVRIR LE LAB",
        "manifesto_cta_href": "lab",

        # Crew band — 3 people (chef, griller, founder)
        "crew_label":   "LE CREW",
        "crew_heading": 'CINQ AU COMPTOIR. <em>UNE SEULE ÉQUIPE.</em>',
        "crew": [
            {
                "name":   "DARIO RIVA",
                "role":   "FONDATEUR & GRILLER",
                "quote":  "« Une smash réussie, c'est du fer chaud, de la scottona froide, quatre-vingt-dix secondes et basta. »",
                "portrait": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "AMINA BERETTA",
                "role":   "PIZZAIOLA · FOUR À BOIS",
                "quote":  "« Le four demande de l'attention toutes les deux minutes. C'est pour ça que je ne regarde pas mon téléphone. »",
                "portrait": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "LUKA HOXHA",
                "role":   "FRITURES & SAUCES",
                "quote":  "« La mayo à la brace, c'est moi qui la signe. Aucun secret, juste de la patience. »",
                "portrait": "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Urban photo strip — 3 atmosphere shots
        "atmo_label":   "L'AMBIANCE",
        "atmo_heading": 'COMPTOIR. NÉON. <em>FILE.</em>',
        "atmo_strip": [
            {
                "image": "https://images.unsplash.com/photo-1485962398834-fef83cc41e4f?w=900&q=80&auto=format&fit=crop",
                "cap":   "File au comptoir · 19 h 40 un samedi soir",
            },
            {
                "image": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=900&q=80&auto=format&fit=crop",
                "cap":   "Late-night DJ set · chaque dernier vendredi du mois",
            },
            {
                "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=900&q=80&auto=format&fit=crop",
                "cap":   "Four à bois allumé de 11 h jusqu'à la fermeture",
            },
        ],

        # Final CTA band — late-night order push
        "final_label":   "PRÊT À COMMANDER ?",
        "final_heading": 'DERNIÈRE COMMANDE <em>À 23 H 30.</em>',
        "final_intro":
            "Trois façons de nous avoir dans l'assiette. Passe au comptoir. Appelle "
            "pour le takeaway. Commande chez nos partenaires de livraison. Fais vite.",
        "final_primary_cta":   "COMMANDE MAINTENANT",
        "final_primary_href":  "ordina",
        "final_phone_cta":     "APPELLE 051 234 5566",
        "final_phone_href":    "+390512345566",
    },

    # ─── MENU ────────────────────────────────────────────────────
    "menu": {
        "eyebrow":  "CARTE · DU PASS",
        "headline": 'TOUT CE <em>QUI BRÛLE.</em>',
        "intro":
            "Cinq sections, vingt-deux pièces, prix au comptoir. Tu pointes du doigt, "
            "tu paies, on t'appelle au numéro. Aucun couvert, aucun service.",

        "sections": [
            {
                "id":    "burger",
                "label": "01",
                "title": "BURGERS",
                "desc":  "scottona piémontaise · hachée le matin · pain brioché au blé brûlé",
                "items": [
                    {
                        "name":  "DOPPIO BRACE",
                        "desc":  "double scottona, cheddar fondu, sauce brace, oignon cru",
                        "price": "9,50 €",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "SMASH CLASSICO",
                        "desc":  "scottona simple, cheddar, oignon caramélisé, sauce maison",
                        "price": "7,50 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "VEGGIE PATTY",
                        "desc":  "patty lentilles & betterave, houmous au citron, roquette",
                        "price": "8,00 €",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BRACE PICCANTE",
                        "desc":  "scottona, jalapeños frits, cheddar piquant, sriracha brace",
                        "price": "9,00 €",
                        "tag":   "PIQUANT",
                        "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "fritti",
                "label": "02",
                "title": "FRITURES",
                "desc":  "frites coupées main à 10 h · double cuisson · sel de Cervia",
                "items": [
                    {
                        "name":  "FRIES BRACE",
                        "desc":  "frites double cuisson, gros sel, sauce brace en coupelle",
                        "price": "4,50 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "FRITTO MISTO",
                        "desc":  "frites, jalapeños panés, baccalà frit, anneaux d'oignon",
                        "price": "6,00 €",
                        "tag":   "PIQUANT",
                        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "JALAPEÑO POPPER",
                        "desc":  "jalapeños farcis cheddar, panés, frits, sauce au citron vert",
                        "price": "5,50 €",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "ONION RINGS",
                        "desc":  "anneaux d'oignon rouge de Tropea en tempura, BBQ maison",
                        "price": "5,00 €",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "pizza",
                "label": "03",
                "title": "PIZZA AL TAGLIO",
                "desc":  "pâte 72 heures · four à bois 420 °C · soixante secondes de cuisson",
                "items": [
                    {
                        "name":  "PIZZA ROSSA",
                        "desc":  "tomate San Marzano DOP, fior di latte, basilic",
                        "price": "4,50 €",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BIANCA AL TARTUFO",
                        "desc":  "fior di latte, copeaux de truffe noire d'été, huile d'olive extra",
                        "price": "6,50 €",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "DIAVOLA NEW",
                        "desc":  "tomate, fior di latte, salame piccante calabrais, miel",
                        "price": "5,50 €",
                        "tag":   "PIQUANT",
                        "image": "https://images.unsplash.com/photo-1593504049359-74330189a345?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "MORTADELLA & PISTACCHIO",
                        "desc":  "fior di latte, mortadella di Bologna IGP, pistache de Bronte",
                        "price": "6,00 €",
                        "tag":   "NEW",
                        "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "drink",
                "label": "04",
                "title": "SODAS & BOISSONS",
                "desc":  "sodas maison pressés au comptoir · bières de Bologna à la pression · vin au verre",
                "items": [
                    {
                        "name":  "SODA BRACE",
                        "desc":  "limonade maison au basilic frais et au gingembre",
                        "price": "3,00 €",
                        "tag":   "NEW",
                        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "ICED TEA HOUSE",
                        "desc":  "thé glacé Earl Grey, miel de châtaignier et zeste de citron",
                        "price": "3,00 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BIRRA SPINA",
                        "desc":  "lager bolognaise du birrificio Sant'Orsola · 0,33 l",
                        "price": "4,50 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "VINO AL CALICE",
                        "desc":  "Sangiovese di Romagna DOC · cantina Ronchi di Solarolo",
                        "price": "5,00 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "dolci",
                "label": "05",
                "title": "DESSERTS",
                "desc":  "faits dans le lab · petites portions, à manger au vol",
                "items": [
                    {
                        "name":  "BRACE COOKIE",
                        "desc":  "cookie au cacao avec cœur de Nutella encore chaud",
                        "price": "3,50 €",
                        "tag":   "TOP",
                        "image": "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "GELATO ARTIGIANALE",
                        "desc":  "fior di panna ou pistache · fourni par la gelateria Stefino",
                        "price": "3,00 €",
                        "tag":   "VEG",
                        "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "TIRAMISÙ AL VOLO",
                        "desc":  "en pot, mascarpone frais, biscuits savoiardi, café bolognais",
                        "price": "4,00 €",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
        ],

        # Allergen line at bottom
        "allergen_label": "ALLERGÈNES",
        "allergen_text":
            "Tous les plats sont préparés dans un environnement où l'on travaille gluten, "
            "produits laitiers, œufs, soja et fruits à coque. Pour les intolérances "
            "sévères, parle au comptoir avant de commander. Liste complète des allergènes "
            "disponible au comptoir.",

        # Producer band — 3 producer names with city
        "producers_label":   "LES FOURNISSEURS",
        "producers_heading": 'D\'OÙ ARRIVE <em>CHAQUE CHOSE.</em>',
        "producers_intro":
            "On travaille avec trois fournisseurs historiques de la ville. Chaque "
            "produit est signé, tracé, livré en petits lots hebdomadaires.",
        "producers": [
            {
                "name":   "MACELLERIA SARTI",
                "city":   "BOLOGNA · VIA PETRONI",
                "role":   "Scottona piémontaise, hachée fraîche chaque matin à sept heures.",
            },
            {
                "name":   "FORNO BERETTA",
                "city":   "MODENA · CASTELFRANCO",
                "role":   "Pain brioché au blé brûlé et pâte à pizza maturée 72 heures.",
            },
            {
                "name":   "ORTOFRUTTA TOSI",
                "city":   "BOLOGNA · MARCHÉ ALBANI",
                "role":   "Pommes de terre, oignons rouges de Tropea, jalapeños cultivés sous serre.",
            },
        ],

        # Final CTA
        "final_label":         "COMMANDE TOUT DE SUITE",
        "final_heading":       'POINTE. <em>PAIE. RETIRE.</em>',
        "final_primary_cta":   "COMMANDE",
        "final_primary_href":  "ordina",
        "final_secondary_cta": "NOUS TROUVER",
        "final_secondary_href": "contatti",
    },

    # ─── LAB (about) ─────────────────────────────────────────────
    "lab": {
        "eyebrow":  "LE LAB",
        "headline": 'POURQUOI LE FEU. <em>POURQUOI LE VOL.</em>',
        "intro":
            "Brace est un labo ouvert tous les jours de midi à minuit. Cinq personnes, "
            "un comptoir, deux fours. Rien de plus, rien de moins.",

        # Big atmosphere photo
        "hero_image":   "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1600&q=80&auto=format&fit=crop",
        "hero_caption": "Le comptoir ouvert · four à bois à 420 °C · chaque service commence ici",

        # Manifesto — 4 short bold paragraphs
        "manifesto_label":   "MANIFESTE",
        "manifesto_paragraphs": [
            {
                "title": "01 PÂTE",
                "text":  "Levain renouvelé toutes les douze heures. Farines de type 1 moulues sur "
                         "pierre par le forno Beretta de Castelfranco. Soixante-douze heures de "
                         "pousse lente en chambre froide, jamais moins. La pizza, on la sent sous "
                         "les doigts avant de la sentir en bouche.",
            },
            {
                "title": "02 FEU",
                "text":  "Le four à bois ne brûle que du chêne du Cimino, rien d'autre. Il atteint "
                         "420 °C en trente-cinq minutes. La plaque du grill monte à 280 °C : "
                         "scottona piémontaise dessus, écrasée au fer, quatre-vingt-dix secondes par face.",
            },
            {
                "title": "03 MATIÈRE",
                "text":  "Uniquement de la scottona piémontaise de la Macelleria Sarti, hachée sur "
                         "le comptoir chaque matin à sept heures. Pommes de terre Tosi coupées à la "
                         "main à dix heures. Tomate San Marzano DOP de l'Agro Sarnese. Tout signé, tout tracé.",
            },
            {
                "title": "04 VITESSE",
                "text":  "Trois minutes du comptoir au pass. Quatorze secondes pour retourner la "
                         "smash. Soixante secondes pour la pizza. Cent quatre-vingts secondes au "
                         "total. Rapides oui, mais faits comme il faut.",
            },
        ],

        # Process strip — 3-step
        "process_label":   "LE PROCESS",
        "process_heading": "TROIS GESTES. <em>RIEN D'AUTRE.</em>",
        "process": [
            {
                "num":   "01",
                "title": "PÂTE",
                "desc":  "chaque nuit à 23 h, pousse 72 h en chambre à 4 °C",
            },
            {
                "num":   "02",
                "title": "FEU",
                "desc":  "four allumé à 11 h, plaque à 280 °C dès 12 h",
            },
            {
                "num":   "03",
                "title": "SERVICE",
                "desc":  "trois minutes du comptoir au pass, on t'appelle au numéro",
            },
        ],

        # Crew band — 4 people
        "crew_label":   "LE CREW AU COMPLET",
        "crew_heading": 'CINQ AU COMPTOIR. <em>UNE SEULE ÉQUIPE.</em>',
        "crew": [
            {
                "name":   "DARIO RIVA",
                "role":   "FONDATEUR & GRILLER",
                "quote":  "« Une smash réussie, c'est du fer chaud, de la scottona froide, quatre-vingt-dix secondes et basta. »",
                "portrait": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "AMINA BERETTA",
                "role":   "PIZZAIOLA · FOUR À BOIS",
                "quote":  "« Le four demande de l'attention toutes les deux minutes. C'est pour ça que je ne regarde pas mon téléphone. »",
                "portrait": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "LUKA HOXHA",
                "role":   "FRITURES & SAUCES",
                "quote":  "« La mayo à la brace, c'est moi qui la signe. Aucun secret, juste de la patience. »",
                "portrait": "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "SOFIA MARTINI",
                "role":   "COMPTOIR & ÉQUIPES",
                "quote":  "« Je t'appelle par ton prénom si tu es déjà venue deux fois. C'est la règle de la maison. »",
                "portrait": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Values grid — 4 cards
        "values_label":   "LES VALEURS",
        "values_heading": 'QUATRE TRUCS <em>NON NÉGOCIABLES.</em>',
        "values": [
            {"title": "TEMPS",       "tag": "ZÉRO ATTENTE",   "desc": "trois minutes du comptoir au pass, toujours"},
            {"title": "TEMPÉRATURE", "tag": "420 °C / 280 °C", "desc": "four et plaque contrôlés à vue, jamais moins"},
            {"title": "QUALITÉ",     "tag": "100 % PIÉMONT",   "desc": "scottona signée, tracée, hachée le matin"},
            {"title": "ÉNERGIE",     "tag": "TOUS LES JOURS", "desc": "ouvert de midi à minuit, dimanche compris"},
        ],

        # Kitchen energy band
        "kitchen_label":   "LA FICHE TECHNIQUE",
        "kitchen_heading": 'LES CHIFFRES <em>DE LA CUISINE.</em>',
        "kitchen_specs": [
            ("210 °C", "PLAQUE SMASH"),
            ("420 °C", "FOUR À BOIS"),
            ("14 SEC", "FLIP DE LA SMASH"),
            ("90 SEC", "CUISSON PIZZA"),
            ("3 MIN",  "COMPTOIR AU PASS"),
            ("72 H",   "POUSSE PÂTE"),
        ],

        # Final CTA
        "final_label":   "VIENS LE VOIR",
        "final_heading": 'LE LAB EST <em>TOUJOURS OUVERT.</em>',
        "final_intro":
            "Ouvert de midi à minuit, tous les jours. Passe quand tu veux, "
            "pointe du doigt, paie au comptoir. Aucune réservation, aucun couvert.",
        "final_primary_cta":   "LA CARTE",
        "final_primary_href":  "menu",
        "final_secondary_cta": "NOUS TROUVER",
        "final_secondary_href": "contatti",
    },

    # ─── MOMENTS (gallery) ───────────────────────────────────────
    "moments": {
        "eyebrow":  "MOMENTS · STREET DIARY",
        "headline": 'CHAQUE SOIR <em>UN MOMENT.</em>',
        "intro":
            "Le journal photo de Brace. File au comptoir, late-night DJ, friture en "
            "flammes, crew au taf. Tout shooté ici, par nous.",

        # Category pills
        "categories_label": "FILTRER",
        "categories": [
            "DJ NIGHTS",
            "FILE AU COMPTOIR",
            "LATE NIGHT",
            "FRY MOMENTS",
            "CREW",
            "OUVERTURE",
        ],

        # 6-image grid
        "grid": [
            {
                "image":    "https://images.unsplash.com/photo-1485962398834-fef83cc41e4f?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-001",
                "cap":      "File au comptoir · samedi 23 h 14 · quatre-vingts personnes en Via Indipendenza",
                "tag":      "FILE AU COMPTOIR",
            },
            {
                "image":    "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-002",
                "cap":      "DJ Tito Brama · last friday set · vinyle only jusqu'à 02 h",
                "tag":      "DJ NIGHTS",
            },
            {
                "image":    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-003",
                "cap":      "Four à bois · 420 °C · onzième heure de service",
                "tag":      "LATE NIGHT",
            },
            {
                "image":    "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-004",
                "cap":      "Double cuisson frites · sel de Cervia · prêt en trois cents secondes",
                "tag":      "FRY MOMENTS",
            },
            {
                "image":    "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-005",
                "cap":      "Luka au pass · vendredi 20 h 34 · septième couvercle de la soirée",
                "tag":      "CREW",
            },
            {
                "image":    "https://images.unsplash.com/photo-1567521464027-f127ff144326?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-006",
                "cap":      "Ouverture · 13 mars 2024 · première entrée au comptoir à 12 h 01",
                "tag":      "OUVERTURE",
            },
        ],

        # Featured shot with quote overlay
        "featured_image": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1600&q=80&auto=format&fit=crop",
        "featured_quote": "« Brace, c'est l'endroit où tu vas pour bouffer bien et vite, et où personne ne te demande ce que tu fais dans la vie. »",
        "featured_author": "ZERO MAGAZINE · BOLOGNA · MARS 2025",
        "featured_filename": "MO-FEAT-002",

        # End CTA
        "final_label":     "VOIR TOUT LE RESTE",
        "final_heading":   'SUIS-NOUS <em>SUR LES SOCIAUX.</em>',
        "final_intro":
            "Chaque jour une nouvelle story, chaque vendredi le drop de la semaine. "
            "Sur Instagram tu as le journal, sur TikTok tu vois comment on bosse "
            "derrière le comptoir.",
        "final_instagram_cta": "INSTAGRAM @brace.lab",
        "final_tiktok_cta":    "TIKTOK @brace.bologna",
    },

    # ─── ORDINA ──────────────────────────────────────────────────
    "ordina": {
        "eyebrow":  "COMMANDE AU VOL",
        "headline": 'TROIS FAÇONS. <em>UN SEUL PLAT.</em>',
        "intro":
            "Passe au comptoir, appelle pour le takeaway, commande chez nos partenaires "
            "de livraison. On t'appelle au numéro quand c'est prêt, jamais avant.",

        # Counter-status band
        "counter_status_label":  "STATUT DU COMPTOIR",
        "counter_queue_label":   "FILE AU COMPTOIR",
        "counter_queue_value":   "≈ 4 MIN",
        "counter_kitchen_label": "CUISINE OUVERTE",
        "counter_kitchen_value": "JUSQU'À 24 H",
        "counter_last_label":    "DERNIÈRE COMMANDE",
        "counter_last_value":    "23 H 30",

        # 3-route grid — counter / takeaway / delivery
        "routes_label":   "TROIS ROUTES",
        "routes_heading": 'CHOISIS <em>COMMENT TU COMMANDES.</em>',
        "routes": [
            {
                "id":      "01",
                "title":   "AU COMPTOIR",
                "subtitle": "VIENS ET POINTE",
                "desc":
                    "Via Indipendenza 42, Bologna. Tu pointes du doigt sur la carte, tu "
                    "paies au comptoir, on t'appelle au numéro quand c'est prêt. Aucune "
                    "réservation, aucun couvert, aucun service. Trois minutes du pass à "
                    "l'assiette.",
                "lines": [
                    ("ADRESSE",      "Via Indipendenza 42, Bologna"),
                    ("FILE ESTIMÉE", "≈ 4 MIN"),
                    ("HORAIRES",     "12 h – 24 h · tous les jours"),
                ],
                "cta_label": "OUVRIR LA CARTE",
                "cta_href":  "https://www.openstreetmap.org/?mlat=44.4949&mlon=11.3426#map=17/44.4949/11.3426",
                "cta_kind":  "external",
            },
            {
                "id":      "02",
                "title":   "TAKEAWAY",
                "subtitle": "APPELLE ET RETIRE",
                "desc":
                    "Appelle le comptoir, dis-nous ce que tu veux, on te donne un horaire "
                    "de retrait. Prêt en douze minutes, toujours. Tu paies au retrait, en "
                    "espèces ou par carte. WhatsApp si tu préfères écrire.",
                "lines": [
                    ("TÉLÉPHONE", "051 234 5566"),
                    ("WHATSAPP",  "Écris au 051 234 5566"),
                    ("PRÊT EN",   "12 MIN"),
                ],
                "cta_label": "APPELLE",
                "cta_href":  "+390512345566",
                "cta_kind":  "tel",
            },
            {
                "id":      "03",
                "title":   "LIVRAISON",
                "subtitle": "À LA MAISON",
                "desc":
                    "Quatre partenaires de livraison, tous sur Bologna centre. Commande "
                    "minimum à dix euros, livraison en trente minutes, gratuite au-delà "
                    "de vingt euros. Ouvre l'app du partenaire que tu utilises le plus.",
                "lines": [
                    ("PARTENAIRES", "GLOVO · DELIVEROO · JUST EAT · UBER EATS"),
                    ("ZONE",        "Bologna centre · rayon 4 km"),
                    ("MIN COMMANDE", "10 €"),
                ],
                "cta_label": "VOIR LES PARTENAIRES",
                "cta_href":  "#partners",
                "cta_kind":  "anchor",
            },
        ],

        # Delivery partners detail
        "partners_label":   "LES PARTENAIRES DE LIVRAISON",
        "partners_heading": 'LIVRAISON EN <em>30 MINUTES.</em>',
        "partners": [
            {"name": "GLOVO",     "eta": "30 MIN", "min": "MIN 12 €", "zone": "Bologna centre · 4 km"},
            {"name": "DELIVEROO", "eta": "25 MIN", "min": "MIN 10 €", "zone": "Bologna centre · 3 km"},
            {"name": "JUST EAT",  "eta": "35 MIN", "min": "MIN 15 €", "zone": "Bologna · 6 km"},
            {"name": "UBER EATS", "eta": "30 MIN", "min": "MIN 12 €", "zone": "Bologna centre · 5 km"},
        ],

        # Late-night opening hours table
        "hours_label":   "QUAND ON EST OUVERT",
        "hours_heading": 'DIMANCHE <em>COMPRIS.</em>',
        "hours_rows": [
            ("LUN", "12 h – 24 h"),
            ("MAR", "12 h – 24 h"),
            ("MER", "12 h – 24 h"),
            ("JEU", "12 h – 24 h"),
            ("VEN", "12 h – 01 h 30"),
            ("SAM", "12 h – 01 h 30"),
            ("DIM", "12 h – 24 h"),
        ],
        "hours_note":
            "Dernière commande toujours 30 minutes avant la fermeture. La cuisine "
            "ne ferme en avance que si la pâte à pizza est terminée, jamais avant minuit.",

        # Allergen note
        "allergen_label": "ALLERGÈNES",
        "allergen_text":
            "Tous les plats sont préparés dans un environnement où l'on travaille gluten, "
            "produits laitiers, œufs, soja et fruits à coque. Pour les intolérances "
            "sévères, parle au comptoir avant de commander ou écris-nous sur WhatsApp.",

        # Big phone CTA band
        "phone_label":   "PRÊT MAINTENANT",
        "phone_heading": 'APPELLE-NOUS <em>AU COMPTOIR.</em>',
        "phone_intro":
            "Réponse en trois sonneries, même pendant le service. Si on ne répond pas, "
            "c'est qu'on est en train de retourner une smash. Réessaie dans trente secondes.",
        "phone_cta_label": "APPELLE 051 234 5566",
        "phone_cta_href":  "+390512345566",

        # FAQ accordion — 4 questions
        "faq_label":   "QUESTIONS FRÉQUENTES",
        "faq_heading": 'LES TRUCS QU\'ON <em>NOUS DEMANDE SOUVENT.</em>',
        "faq": [
            {
                "q": "VOUS AVEZ DES OPTIONS GLUTEN FREE ?",
                "a": "Pain brioché gluten free sur demande, on te demande trente minutes "
                     "d'attente en plus. Préviens au comptoir avant de commander. Frites, "
                     "viande et sauces sont naturellement sans gluten, mais cuisinées dans "
                     "le même environnement — pour les intolérances sévères, parle au comptoir.",
            },
            {
                "q": "VOUS PRENEZ DES RÉSERVATIONS POUR LES GROUPES ?",
                "a": "Aucun couvert réservé, aucune réservation. Pour les groupes au-delà de "
                     "douze personnes, écris-nous sur WhatsApp deux jours avant : on te dit "
                     "si on peut organiser un horaire moins chargé (en général mar/mer à 19 h).",
            },
            {
                "q": "VOUS AVEZ DES OPTIONS VEGGIE ET VEGAN ?",
                "a": "Oui, toujours trois options veggie : veggie patty aux lentilles, pizza "
                     "rossa, fries brace. Les options vegan (sans laitier) tournent chaque "
                     "semaine — demande au comptoir laquelle est dispo aujourd'hui.",
            },
            {
                "q": "VOUS FAITES DU CATERING OU DES ÉVÉNEMENTS PRIVÉS ?",
                "a": "Oui, de vingt à soixante personnes. Smash burgers, pizza al taglio, "
                     "fritures, sodas maison. Four mobile pour événements à Bologna et en "
                     "province. Écris à eventi@bracestreetlab.it avec la date, l'endroit et "
                     "le nombre de personnes — on répond en 24 heures avec un devis.",
            },
        ],
    },

    # ─── CONTATTI ────────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "NOUS TROUVER · BOLOGNA",
        "headline": 'VIA INDIPENDENZA <em>42.</em>',
        "intro":
            "Centre de Bologna, à deux pas des Due Torri. Ouvert tous les jours, "
            "dimanche compris, jusque tard le soir. Viens à pied si tu peux.",

        # Address card
        "address_label": "ADRESSE",
        "address_value": "Via Indipendenza 42 · 40121 Bologna",
        "address_note":  "Entre Piazza Maggiore et la gare · zone piétonne",

        # Map iframe
        "map_lat":   "44.4949",
        "map_lon":   "11.3426",
        "map_zoom":  "16",
        "map_label": "Carte OpenStreetMap · Via Indipendenza 42, Bologna",

        # Contact channels grid
        "channels_label": "PARLE AU COMPTOIR",
        "channels": [
            {
                "icon":  "phone",
                "label": "TÉLÉPHONE",
                "value": "051 234 5566",
                "note":  "réponse en trois sonneries, même pendant le service",
                "href":  "+390512345566",
                "kind":  "tel",
            },
            {
                "icon":  "whatsapp",
                "label": "WHATSAPP",
                "value": "051 234 5566",
                "note":  "écris si tu préfères, on répond en 30 minutes",
                "href":  "https://wa.me/390512345566",
                "kind":  "external",
            },
            {
                "icon":  "email",
                "label": "EMAIL",
                "value": "ordini@bracestreetlab.it",
                "note":  "pour catering, événements, fournisseurs",
                "href":  "ordini@bracestreetlab.it",
                "kind":  "mail",
            },
        ],

        # Hours grid (compact)
        "hours_label": "HORAIRES D'OUVERTURE",
        "hours_rows": [
            ("LUN – JEU", "12 h – 24 h"),
            ("VEN – SAM", "12 h – 01 h 30"),
            ("DIMANCHE",  "12 h – 24 h"),
        ],
        "hours_note": "Dernière commande 30 minutes avant la fermeture · cuisine toujours active",

        # Transport note
        "transport_label": "COMMENT TU ARRIVES",
        "transport_rows": [
            ("BUS",        "lignes 11, 14, 27 · arrêt Indipendenza"),
            ("TRAIN",      "Stazione Centrale · 8 minutes à pied"),
            ("PARKING",    "Riva di Reno · 4 minutes à pied"),
            ("VÉLO",       "rack à vélos en Via dell'Indipendenza"),
        ],

        # Jobs band
        "jobs_label":    "BOSSE AVEC NOUS",
        "jobs_heading":  'ON CHERCHE <em>CINQ PERSONNES.</em>',
        "jobs_intro":
            "Brace grandit. On ouvre un deuxième lab à Modena d'ici l'été 2026. "
            "On a besoin de gens vrais, pas de CV parfaits.",
        "jobs": [
            {"role": "GRILLER",        "type": "TEMPS PLEIN",  "city": "BOLOGNA"},
            {"role": "PIZZAIOLO",      "type": "TEMPS PARTIEL", "city": "BOLOGNA"},
            {"role": "RUNNER & COMPTOIR", "type": "WEEKEND",   "city": "BOLOGNA"},
        ],
        "jobs_cta_label": "ENVOIE UN MESSAGE",
        "jobs_cta_href":  "lavoro@bracestreetlab.it",

        # Social block
        "social_label": "SUIS-NOUS",
        "social": [
            {"platform": "INSTAGRAM", "handle": "@brace.lab",     "href": "https://instagram.com/brace.lab"},
            {"platform": "TIKTOK",    "handle": "@brace.bologna", "href": "https://tiktok.com/@brace.bologna"},
        ],

        # Mini reservation/inquiry form
        "form_label":   "ÉCRIS-NOUS",
        "form_heading": 'DEUX LIGNES <em>SUFFISENT.</em>',
        "form_intro":
            "Pour catering, groupes au-delà de douze personnes, fournisseurs. Pour "
            "commander, écris-nous sur WhatsApp, c'est plus rapide.",
        "form_field_name":     "Nom",
        "form_field_email":    "Email",
        "form_field_phone":    "Téléphone",
        "form_field_message":  "Ce qu'il te faut",
        "form_field_message_placeholder": "Catering, événement, fourniture, autre…",
        "form_submit_label":   "ENVOIE",
        "form_submit_note":
            "Démo de démonstration · aucune donnée ne sera envoyée. Pour commander pour "
            "de vrai, appelle 051 234 5566 ou écris sur WhatsApp.",
    },

    # No blog on Brace
    "posts": [],
}
