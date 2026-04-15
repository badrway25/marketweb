"""Sapore — Trattoria Da Nonna Rosa (trattoria-warm archetype) — FR content tree.

Phase 2i.2 — Restaurant live-completion i18n (Session 48, 2026-04-15).

Voice contract (FR):
- Registre éditorial chaleureux à la française — inspiration Le Fooding,
  Atabula, Le Monde Saveurs côté reportage sur une trattoria romaine.
  Voix observatrice, seconde personne inclusive, forme « tu » (trattoria
  de famille, jamais le « vous » d’un étoilé).
- Noms de plats italiens restent italiens : Cacio e pepe, Carbonara,
  Bucatini all’amatriciana, Coda alla vaccinara, Tonnarelli, Margherita
  verace, Cesanese del Lazio. Glose FR en parenthèse uniquement à la
  première rencontre d’un plat obscur, jamais sur les classiques.
- Noms propres italiens restent italiens : Trattoria Da Nonna Rosa,
  Rosa Trezzi, Marco Trezzi, Giulia Trezzi, Trastevere, Roma, Via dei
  Salumi, Lazio, Amatrice, Olevano Romano, Pienza, Agerola. Jamais de
  translittération.
- Guillemets français « » avec espaces insécables. Apostrophe courbe ’.
  Devise : « 12,00 € » (virgule décimale + espace + €).
- Espaces insécables avant : ; ! ? et à l’intérieur des « ».

Contrat de différenciation (D-054) :
- Brace FR = street-food bolognaise brutaliste, voix cassante, pop.
- Gusto FR = étoilé Michelin, voix éditoriale-chef en vouvoiement.
- Sapore FR = trattoria de quartier, voix reportage-chaleureuse en « tu ».
  Vocabulaire : trattoria, nonna, maison, four à bois, mattarello, cacio,
  guanciale, Cesanese, tablée, couverts, famille, Trastevere. Jamais
  « menu dégustation », jamais « maître », jamais « concierge », jamais
  « étoile Michelin ».
"""
from __future__ import annotations

from typing import Any


SAPORE_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Accueil",                    "kind": "home"},
        {"slug": "menu",     "label": "Carte",                      "kind": "menu"},
        {"slug": "storia",   "label": "Notre histoire",             "kind": "about"},
        {"slug": "forno",    "label": "Four à bois",                "kind": "signature"},
        {"slug": "eventi",   "label": "Tablées & événements",       "kind": "events"},
        {"slug": "contatti", "label": "Nous trouver & réserver",    "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "R",
        "logo_word":    "Trattoria Da Nonna Rosa",
        "tag":          "Trattoria de famille · Trastevere · depuis 1987",
        "phone":        "06 581 4488",
        "phone_tel":    "+390658144880",
        "whatsapp":     "06 581 4488",
        "whatsapp_link": "https://wa.me/390658144880",
        "email":        "ciao@trattoriadanonnarosa.it",
        "address":      "Via dei Salumi 16/a · 00153 Roma · Trastevere",
        "hours_compact": "Mar. – sam. · 12 h 30 – 15 h 00 · 19 h 00 – 23 h 30",
        "hours_footer_rows": [
            "Dimanche · déjeuner uniquement · 12 h 30 – 15 h 00",
            "Lundi · repos hebdomadaire",
        ],
        "license":      "TVA IT 07634211006 · CCIAA Roma REA 1138992",
        "footer_intro":
            "Trattoria de famille ouverte en 1987 par Rosa Trezzi. Pâtes "
            "tirées au mattarello chaque matin, pizza au four à bois le "
            "soir, verre de vin maison offert à celles et ceux qui "
            "reviennent deux fois. Soixante couverts, deux salles, trois "
            "générations en cuisine.",
        "nav_cta":      "Réserver une table",
        "nav_cta_href": "contatti",
        "nav_phone_cta": "Appelle : 06 581 4488",
        "star_line":    "Trattoria de famille · depuis 1987",
        "copyright":    "© 2026 Trattoria Da Nonna Rosa · TVA IT 07634211006",

        # Mirror the fine-dining _base.html footer keys used by the chrome
        "footer_hours_1": "Mar. – sam. · déjeuner & dîner",
        "footer_hours_2": "Dimanche · déjeuner uniquement",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Trattoria de famille · Trastevere · depuis 1987",
        "headline": "Chez Nonna Rosa, <em>comme à la maison.</em>",
        "intro":
            "Pâtes tirées au mattarello chaque matin, pizza au four à bois "
            "le soir, et un verre de vin maison offert à celles et ceux qui "
            "reviennent deux fois. Soixante couverts, deux salles, trois "
            "générations en cuisine.",
        "primary_cta":   "Réserver une table",
        "primary_href":  "contatti",
        "secondary_cta": "Écris-nous sur WhatsApp",
        "secondary_href_is_whatsapp": True,

        # Hero photo-frame
        "hero_image":   "https://images.unsplash.com/photo-1481931098730-318b6f776db0?w=1600&q=80&auto=format&fit=crop",
        "hero_caption": "Cacio e pepe du mardi · tonnarelli tirés au mattarello",
        "hero_stamp":   "Depuis 1987",

        # Facts band — 3 numbers/claims
        "facts": [
            ("1987",   "année où Rosa a ouvert la cuisine"),
            ("60",     "couverts en deux salles · pas de réservation au-delà de vingt"),
            ("3",      "générations de famille en cuisine"),
        ],

        # Chalkboard — 5 daily specials lun → ven
        "chalkboard_label":   "L’ardoise de la semaine",
        "chalkboard_heading": "Plat du jour, <em>écrit à la main.</em>",
        "chalkboard_intro":
            "Chaque matin, Nonna Rosa écrit l’ardoise à la craie — elle décide "
            "au comptoir ce qu’on cuisine aujourd’hui. Cette semaine, ça se "
            "passe comme ça.",
        "chalkboard_buongiorno": "Bon appétit !",
        "chalkboard_days": [
            ("Lun.", "Cacio e pepe",              "tonnarelli tirés à la main",                 "12,00 €"),
            ("Mar.", "Bucatini all’amatriciana",  "guanciale d’Amatrice de Sarnelli",           "11,00 €"),
            ("Mer.", "Coda alla vaccinara",       "recette de Nonna Rosa, comme en 1987",       "14,00 €"),
            ("Jeu.", "Gnocchi au jus de rôti",    "faits le matin avec des pommes de terre de garde", "11,00 €"),
            ("Ven.", "Baccalà in pastella",       "tomates cerises confites et artichaut romain", "13,00 €"),
        ],

        # Family strip — 3 portraits with personal blurbs
        "family_label":   "La famille en cuisine",
        "family_heading": "Trois générations, <em>une seule tablée.</em>",
        "family": [
            {
                "name":   "Rosa Trezzi",
                "role":   "Pâtes fraîches depuis 1987",
                "blurb":
                    "Nonna Rosa ouvre la trattoria le 3 septembre 1987 avec un "
                    "rêve et deux rouleaux à pâtisserie. Aujourd’hui, elle a "
                    "quatre-vingt-deux ans et tire encore les pâtes chaque "
                    "matin dès sept heures. Sa devise est simple : « la bonne "
                    "pâte, tu la sens sous les mains, pas besoin de balance ».",
                "portrait": "https://images.pexels.com/photos/2050990/pexels-photo-2050990.jpeg?auto=compress&cs=tinysrgb&w=600&h=750&fit=crop",
            },
            {
                "name":   "Marco Trezzi",
                "role":   "Pizzaiolo · four à bois depuis 2003",
                "blurb":
                    "Le fils de Rosa, élevé entre farine et briques. Il allume "
                    "le four chaque après-midi à seize heures — chêne du Cimino, "
                    "rien d’autre — et le garde vivant jusqu’à minuit. Sa "
                    "Margherita verace, il l’a apprise chez Peppe Guida à Vico "
                    "Equense en 2008.",
                "portrait": "https://images.unsplash.com/photo-1607631568010-a87245c0daf8?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Giulia Trezzi",
                "role":   "Salle & desserts de la maison",
                "blurb":
                    "La petite-fille de Rosa, trente ans, s’occupe de la salle "
                    "et des desserts. Tiramisù au mascarpone de Sarnelli, tarte "
                    "aux griottes quand la saison s’y prête, maritozzi à la "
                    "crème fouettée le samedi matin seulement. Elle t’accueille "
                    "avec un sourire et une carafe d’eau pétillante.",
                "portrait": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Forno teaser band
        "forno_label":   "Le four à bois",
        "forno_heading": "Allumé chaque après-midi à <em>seize heures pile.</em>",
        "forno_text":
            "Le four à coupole de Marco est en briques du Viterbese, monté "
            "à la main par le pizzaiolo Gennaro Esposito en 2003. Il brûle "
            "uniquement du chêne du Cimino, atteint 420 °C et cuit la pizza "
            "en soixante secondes. Du mardi au samedi, le soir uniquement, "
            "quand la première salle s’est vidée du déjeuner.",
        "forno_image":    "https://images.unsplash.com/photo-1593504049359-74330189a345?w=1200&q=80&auto=format&fit=crop",
        "forno_caption":  "Margherita verace · 420 °C · soixante secondes",
        "forno_cta":      "Découvre pizza & pâtes",
        "forno_cta_href": "forno",

        # Reviews band — 2–3 quotes
        "reviews_label": "Ce qu’on dit de nous",
        "reviews": [
            {
                "quote":  "Je me suis senti dans la cuisine de la grand-mère que je n’ai jamais eue.",
                "author": "Gambero Rosso · Tre Spicchi 2024",
            },
            {
                "quote":  "Une des dernières vraies trattorie de Trastevere. Vas-y à pied, le soir, et commande la coda.",
                "author": "Corriere della Sera · Cook",
            },
            {
                "quote":  "La carbonara de Rosa fait taire tout le monde, même ceux de Testaccio.",
                "author": "Puntarella Rossa · 2025",
            },
        ],

        # Hours strip — 3 rows under reviews
        "hours_label":  "Quand on est ouverts",
        "hours_rows": [
            ("Mar. – sam.", "12 h 30 – 15 h 00", "déjeuner"),
            ("Mar. – sam.", "19 h 00 – 23 h 30", "dîner · four à bois"),
            ("Dimanche",    "12 h 30 – 15 h 00", "déjeuner uniquement · fermeture 16 h 00"),
        ],
        "hours_note": "Lundi, repos hebdomadaire · ouverts tous les jours fériés sauf Noël",

        # Tavolata band — group experience teaser
        "tavolata_label":   "La tablée",
        "tavolata_heading": "Douze amis, <em>une seule table.</em>",
        "tavolata_text":
            "La tablée, c’est notre longue table de douze places dans la salle "
            "de la cheminée. Menu fixe à trente-deux euros, vin maison inclus, "
            "desserts de Giulia pour finir. Pour anniversaires, communions, "
            "dîners de promo ou simplement parce qu’aujourd’hui est un bon "
            "jour pour être ensemble.",
        "tavolata_cta":      "Organise une tablée",
        "tavolata_cta_href": "eventi",
        "tavolata_image":    "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=1200&q=80&auto=format&fit=crop",

        # Final CTA band
        "cta_label":    "Viens nous voir",
        "cta_heading":  "Via dei Salumi seize, <em>sonne fort.</em>",
        "cta_intro":
            "On est Via dei Salumi, à deux pas du lungotevere. La porte est en "
            "bois vert, la sonnette fait du bruit : n’aie pas peur, sonne fort. "
            "On te garde un verre de Cesanese frais et une part de pizza rossa "
            "tout juste sortie du four.",
        "cta_primary":      "Réserver une table",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Écris sur WhatsApp",
    },

    # ─── MENU ────────────────────────────────────────────────────
    "menu": {
        "eyebrow":  "La carte · saison automne ’26",
        "headline": "Pâtes tirées à la main, pizza au four à bois, <em>desserts maison.</em>",
        "intro":
            "La carte change peu, parce que les plats de la maison sont ceux-là : "
            "cacio e pepe, amatriciana, carbonara, coda, saltimbocca. Les pizzas "
            "tournent selon la saison. Le reste, c’est Nonna Rosa qui le décide "
            "au comptoir, le matin.",

        "wine_house_label":   "Vin maison",
        "wine_house_heading": "Cesanese del Lazio, <em>au pichet, 18,00 € le litre.</em>",
        "wine_house_text":
            "Le vin de la maison vient d’Olevano Romano, de la cave Proietti "
            "Riccardi, qui le fait depuis quarante ans. On le sert en carafe "
            "d’un litre, d’un demi ou d’un quart. Blanc : Malvasia Puntinata "
            "des Castelli, Cantina Ribelà, en pichet lui aussi.",

        "allergen_note":
            "Les plats marqués (G) contiennent du gluten, (L) du lactose, "
            "(P) du poisson. En cas d’allergie particulière, demande au "
            "comptoir avant de commander : Rosa a passé une formation HACCP "
            "en 2019 et elle sait tout.",

        "sections": [
            {
                "label": "Antipasti de la maison",
                "heading": "Du potager et du comptoir",
                "dishes": [
                    ("Bruschetta al pomodoro",        "tomates cerises du Piennolo, basilic, huile d’olive Sabina DOP", "7,00 €"),
                    ("Carciofo alla giudia",          "artichaut romain, frit deux fois, citron d’Amalfi",               "9,00 €"),
                    ("Suppli classique",              "riz, mozzarella filante, ragù de viande de la maison",            "4,00 €"),
                    ("Fleurs de courgette frites",    "farcies mozzarella et anchois, pâte à beignet légère",            "8,00 €"),
                    ("Puntarelle alla romana",        "anchois du Cantabrique, ail, vinaigre rouge",                     "8,00 €"),
                    ("Planche de charcuterie & fromages", "guanciale d’Amatrice, pecorino de Pienza, olives",            "14,00 €"),
                    ("Boulettes de Nonna Rosa",       "sauce tomate, pain de campagne à côté",                           "10,00 €"),
                ],
            },
            {
                "label": "Primi de pâtes tirées à la main",
                "heading": "Du mattarello du matin",
                "dishes": [
                    ("Cacio e pepe",                  "tonnarelli tirés au mattarello, pecorino de Pienza",              "12,00 €"),
                    ("Carbonara classique",           "guanciale d’Amatrice, pecorino romano, cinq jaunes",              "13,00 €"),
                    ("Bucatini all’amatriciana",      "guanciale, tomate San Marzano, pecorino",                         "12,00 €"),
                    ("Gnocchi au jus de rôti",        "faits le matin, jus du jeudi de Rosa",                            "11,00 €"),
                    ("Fettuccine alla papalina",      "jambon cru, petits pois frais, œufs, parmesan",                   "13,00 €"),
                    ("Rigatoni con la pajata",        "intestin de veau de lait, sauce tomate",                          "15,00 €"),
                    ("Tonnarelli au cacio et truffe", "truffe noire de Norcia, pecorino, poivre",                        "18,00 €"),
                ],
            },
            {
                "label": "Pizza au four à bois",
                "heading": "Le soir uniquement · mardi → samedi",
                "dishes": [
                    ("Margherita verace",             "tomate San Marzano, fiordilatte, basilic",                        "9,00 €"),
                    ("Capricciosa de Nonna Rosa",     "artichauts, champignons, jambon cuit, œuf",                       "12,00 €"),
                    ("Diavola au guanciale",          "tomate, fiordilatte, salami piquant, guanciale",                  "11,00 €"),
                    ("Bianca au cacio e pepe",        "fiordilatte, pecorino, poivre noir de Pondichéry",                "10,00 €"),
                    ("Nonna Rosa (signature)",        "stracciatella d’Andria, tomates cerises semi-séchées, basilic",   "13,00 €"),
                    ("Courge et saucisse",            "crème de courge, saucisse de Norcia, romarin",                    "12,00 €"),
                ],
            },
            {
                "label": "Secondi du comptoir",
                "heading": "De la cuisine du dimanche",
                "dishes": [
                    ("Saltimbocca alla romana",       "veau, jambon cru, sauge, vin blanc",                              "16,00 €"),
                    ("Coda alla vaccinara",           "queue de bœuf, céleri, cacao, pignons, raisins secs",             "17,00 €"),
                    ("Abbacchio a scottadito",        "côtelettes d’agneau, romarin, citron",                            "19,00 €"),
                    ("Trippa alla romana",            "tripes, sauce tomate, menthe, pecorino",                          "14,00 €"),
                    ("Baccalà in pastella",           "morue battue, pâte à beignet légère, tomates cerises",            "14,00 €"),
                ],
            },
            {
                "label": "Desserts de la maison",
                "heading": "Les mains de Giulia",
                "dishes": [
                    ("Tiramisù de Giulia",            "mascarpone de Sarnelli, boudoirs, café de la moka",               "6,00 €"),
                    ("Panna cotta à la vanille",      "aux griottes de Nonna Rosa",                                      "5,00 €"),
                    ("Tarte aux griottes",            "pâte sablée maison, griottes du millésime 2025",                  "6,00 €"),
                    ("Maritozzo à la crème",          "le samedi matin uniquement · crème fraîche de Valentini",         "4,00 €"),
                    ("Glace du grand-père",           "trois parfums · fior di latte, noisette, chocolat",               "5,00 €"),
                ],
            },
        ],
    },

    # ─── STORIA (about) ──────────────────────────────────────────
    "storia": {
        "eyebrow":  "Notre histoire · depuis 1987",
        "headline": "Quarante ans de pâtes tirées <em>au mattarello.</em>",
        "intro":
            "La Trattoria Da Nonna Rosa ouvre le 3 septembre 1987 dans deux "
            "pièces de la Via dei Salumi, héritées de la mère de Rosa Trezzi. "
            "Trente ans plus tard, on est encore là, dans la même cuisine, avec "
            "un four en plus et trois générations de famille qui se relaient "
            "au comptoir.",

        "story": [
            "Rosa Trezzi naît à Rome en 1944, fille d’un aubergiste de "
            "Testaccio. Elle grandit entre les casseroles, les mattarelli "
            "et le bruit du marché de Porta Portese. À quinze ans, elle "
            "épouse Marino, qui était boulanger, et ouvre avec lui une "
            "première osteria Via dei Foraggi. Ça dure six ans, jusqu’en "
            "1987, quand le père de Marino laisse en héritage deux pièces "
            "Via dei Salumi, à Trastevere.",

            "Le 3 septembre 1987, la trattoria ouvre au numéro seize/a, "
            "avec douze couverts, un four à gaz et un frigo mural. Le menu "
            "du premier soir est écrit au stylo sur une feuille de papier "
            "sulfurisé : cacio e pepe, amatriciana, coda alla vaccinara, "
            "et un tiramisù fait avec le mascarpone du crémier d’en bas. "
            "Coût total du dîner : quatre mille lires.",

            "En 2003, le fils Marco reprend la seconde salle — l’atelier "
            "d’un menuisier qui avait fermé — et monte le four à bois "
            "avec le pizzaiolo Gennaro Esposito, venu à Rome pour un "
            "mariage. Depuis cet été-là, la pizza entre au menu le soir "
            "uniquement, le mardi et le samedi. Puis tous les soirs, "
            "depuis 2005.",

            "En 2024, Giulia, la petite-fille de Rosa, rentre de Barcelone "
            "où elle travaillait en pâtisserie, et prend en main la salle "
            "et les desserts. Aujourd’hui, la trattoria compte soixante "
            "couverts, trois générations, un four à bois, un serveur "
            "historique — Beppe, depuis 1996 — et le même écriteau sur "
            "la porte : celui qui revient deux fois, le vin maison est "
            "offert.",
        ],

        # Timeline — 3 steps
        "timeline_label":   "Trois dates",
        "timeline": [
            {
                "year":  "1987",
                "title": "Rosa ouvre au seize/a",
                "desc":  "Trois septembre, douze couverts, quatre mille lires par personne. Le premier menu est écrit au stylo sur du papier sulfurisé.",
            },
            {
                "year":  "2003",
                "title": "Le four à bois arrive",
                "desc":  "Marco reprend la seconde salle et monte le four avec Gennaro Esposito. Première Margherita : vingt-deux juin.",
            },
            {
                "year":  "2024",
                "title": "Giulia rentre à la maison",
                "desc":  "Giulia revient de Barcelone et prend la salle. Premier maritozzo du samedi : vingt-six octobre.",
            },
        ],

        # Family portraits (reused shape from home but with longer blurbs)
        "family_label":   "Les mains qui te servent",
        "family": [
            {
                "name":   "Rosa Trezzi",
                "role":   "Fondatrice · pâtes fraîches depuis 1987",
                "blurb":
                    "Quatre-vingt-deux ans, un petit-enfant pour chaque doigt "
                    "de la main, et un mattarello qu’elle connaît par cœur. "
                    "Elle tire la pâte chaque matin de sept à dix heures, puis "
                    "passe écrire l’ardoise du jour. La carbonara, c’est elle "
                    "seule qui la fait : c’est un rite jaloux.",
                "portrait": "https://images.pexels.com/photos/2050990/pexels-photo-2050990.jpeg?auto=compress&cs=tinysrgb&w=600&h=750&fit=crop",
            },
            {
                "name":   "Marco Trezzi",
                "role":   "Pizzaiolo · four à bois depuis 2003",
                "blurb":
                    "Grandi dans la trattoria, menuisier pendant trois ans, "
                    "puis pizzaiolo depuis vingt-deux. Il allume le four à "
                    "seize heures, fait crépiter le chêne du Cimino, et "
                    "pétrit à la main avec un levain mère de 2008. La "
                    "Margherita, il l’enfourne les yeux fermés en soixante "
                    "secondes.",
                "portrait": "https://images.unsplash.com/photo-1607631568010-a87245c0daf8?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Giulia Trezzi",
                "role":   "Salle & desserts · depuis 2024",
                "blurb":
                    "Deux ans chez Josep Maria en pâtisserie à Barcelone, "
                    "puis le retour. Elle s’occupe de la salle avec le "
                    "serveur Beppe, prépare les desserts du jour et décide "
                    "de la carte des vins. Elle fait le meilleur maritozzo "
                    "à l’ouest du Tibre, mais le samedi matin seulement.",
                "portrait": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Valori grid — 4 cards
        "values_label":   "Nos règles",
        "values_heading": "Quatre choses <em>qui ne changent pas.</em>",
        "values": [
            {
                "title": "La pâte",
                "desc":
                    "Farine du Molino Paolo Mariani, eau de Rome, jaunes de "
                    "Paolo Parisi. Tirée au mattarello chaque matin dès sept "
                    "heures. Jamais séchée, jamais surgelée, jamais de la veille.",
            },
            {
                "title": "Le four à bois",
                "desc":
                    "Uniquement du chêne du Cimino, coupé à Vitorchiano. Allumé "
                    "chaque après-midi à seize heures pile. Si le four "
                    "n’atteint pas 420 °C, ce soir-là la pizza ne sort pas — "
                    "point final.",
            },
            {
                "title": "Le vin maison",
                "desc":
                    "Cesanese d’Olevano Romano de Proietti Riccardi, Malvasia "
                    "des Castelli de Cantina Ribelà. En pichet, à la carafe. "
                    "Dix-huit euros le litre, le même prix depuis 2019.",
            },
            {
                "title": "La règle du verre",
                "desc":
                    "Celui qui revient deux fois, le vin maison est offert. "
                    "C’est écrit sur l’ardoise, c’est là depuis le premier "
                    "jour, on ne l’a jamais changé. Même si on te reconnaît, "
                    "demande-le quand même.",
            },
        ],

        "photo_image":   "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1600&q=80&auto=format&fit=crop",
        "photo_caption": "La salle de la cheminée · dîner du samedi · novembre 2025",
    },

    # ─── FORNO (signature · pizza & pasta) ────────────────────────
    "forno": {
        "eyebrow":  "Pizza & pâtes · les signatures de la maison",
        "headline": "Quatre pizzas et quatre pâtes <em>écrites à la main.</em>",
        "intro":
            "Nos signatures sont au nombre de huit — quatre au four, quatre "
            "au mattarello. Elles ne changent pas, ne s’allongent pas, ne "
            "tournent pas. Ce sont les plats que Nonna Rosa a fixés en 1987 "
            "et sur lesquels la famille joue sa réputation depuis quarante "
            "ans.",

        # Pizza section
        "pizza_label":   "Du four à bois",
        "pizza_heading": "Quatre pizzas <em>d’auteur de la maison.</em>",
        "pizza_intro":
            "Le four à bois de Marco brûle uniquement du chêne du Cimino, "
            "atteint 420 °C et cuit la pizza en soixante secondes. Pâte à "
            "vingt-quatre heures de levée avec un levain mère de 2008. "
            "Tomate San Marzano DOP, fiordilatte d’Agerola de la laiterie "
            "Sorrentina.",
        "pizza_signatures": [
            {
                "n":     "I",
                "name":  "Margherita verace",
                "desc":  "Tomate San Marzano DOP, fiordilatte d’Agerola, basilic génois DOP, huile d’olive Sabina à cru.",
                "price": "9,00 €",
            },
            {
                "n":     "II",
                "name":  "Capricciosa de Nonna Rosa",
                "desc":  "Artichauts romains sautés, champignons de Paris, jambon cuit de Prato, œuf bio de Parisi au centre.",
                "price": "12,00 €",
            },
            {
                "n":     "III",
                "name":  "Diavola au guanciale",
                "desc":  "Tomate, fiordilatte, salami piquant d’Amatrice, guanciale de Sarnelli, piment de Diamante.",
                "price": "11,00 €",
            },
            {
                "n":     "IV",
                "name":  "Nonna Rosa (signature de la maison)",
                "desc":  "Stracciatella d’Andria à cru, tomates cerises semi-séchées, basilic, huile Sabina, zeste de citron d’Amalfi.",
                "price": "13,00 €",
            },
        ],

        # Pasta section
        "pasta_label":   "Du mattarello",
        "pasta_heading": "Quatre pâtes <em>tirées à la main dès sept heures.</em>",
        "pasta_intro":
            "Pâtes tirées au mattarello chaque matin de sept à dix heures. "
            "Farine du Molino Paolo Mariani, eau de Rome, jaunes de Paolo "
            "Parisi. Jamais séchées, jamais surgelées, jamais de la veille.",
        "pasta_signatures": [
            {
                "n":     "I",
                "name":  "Cacio e pepe",
                "desc":  "Tonnarelli tirés au mattarello, pecorino de Pienza DOP, poivre noir de Pondichéry moulu au moment.",
                "price": "12,00 €",
            },
            {
                "n":     "II",
                "name":  "Carbonara classique",
                "desc":  "Spaghetti, guanciale d’Amatrice, pecorino romano, cinq jaunes de Parisi, poivre noir. Jamais de crème.",
                "price": "13,00 €",
            },
            {
                "n":     "III",
                "name":  "Bucatini all’amatriciana",
                "desc":  "Bucatini du moulin, guanciale d’Amatrice croustillant, San Marzano, pecorino romano râpé à l’assiette.",
                "price": "12,00 €",
            },
            {
                "n":     "IV",
                "name":  "Fettuccine alla papalina",
                "desc":  "Fettuccine, jambon cru San Daniele, petits pois frais, œufs, parmesan reggiano affiné 36 mois.",
                "price": "13,00 €",
            },
        ],

        # Forno story
        "forno_story_label":   "Le four à bois",
        "forno_story_heading": "Quatre cent vingt degrés, <em>soixante secondes.</em>",
        "forno_story_text_1":
            "Le four à coupole de Marco a été monté à la main en 2003 par le "
            "pizzaiolo Gennaro Esposito, brique après brique, avec de la "
            "terre réfractaire de Viterbe. Il mesure deux mètres dix de "
            "diamètre, cuit six pizzas à la fois, atteint 420 °C avec un "
            "panier de chêne du Cimino coupé à Vitorchiano.",
        "forno_story_text_2":
            "Allumé chaque après-midi à seize heures pile. Si à dix-huit "
            "heures il n’a pas encore atteint la température, ce soir-là la "
            "pizza ne sort pas — ça s’est produit trois fois en vingt-deux "
            "ans, la dernière en février 2024 pendant la tempête de neige, "
            "et ce soir-là on a tous mangé des pâtes.",
        "forno_story_image":
            "https://images.unsplash.com/photo-1571997478779-2adcbbe9ab2f?w=1600&q=80&auto=format&fit=crop",
        "forno_story_caption": "Chêne du Cimino · four à 420 °C · juillet 2025",

        # Ingredients/producers band
        "producers_label":   "Cinq mains qui signent",
        "producers_heading": "D’où ils viennent, <em>et de qui.</em>",
        "producers": [
            {
                "name":       "Sarnelli Guanciale",
                "place":      "Amatrice · Lazio",
                "ingredient": "Guanciale de cochon noir casertan · affinage 90 jours",
            },
            {
                "name":       "Molino Paolo Mariani",
                "place":      "Barchi · Marche",
                "ingredient": "Farines type 0 et 00 · blé Senatore Cappelli · meule de pierre",
            },
            {
                "name":       "Proietti Riccardi",
                "place":      "Olevano Romano · Lazio",
                "ingredient": "Cesanese del Lazio au pichet · vignes en gobelet · millésime 2024",
            },
            {
                "name":       "Caseificio Sorrentina",
                "place":      "Agerola · Campania",
                "ingredient": "Fiordilatte de bufflonne campanienne · livraison quotidienne",
            },
            {
                "name":       "Paolo Parisi",
                "place":      "Usigliano di Lari · Toscana",
                "ingredient": "Œufs de poule nourrie au lait de chèvre · jaune orangé",
            },
        ],

        # Dough photo
        "dough_image":   "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=1600&q=80&auto=format&fit=crop",
        "dough_caption": "Pâte à vingt-quatre heures · levain mère de 2008",
    },

    # ─── EVENTI (events & tavolate) ──────────────────────────────
    "eventi": {
        "eyebrow":  "Tablées & événements · groupes de douze à soixante",
        "headline": "Une longue tablée, <em>tous assis côte à côte.</em>",
        "intro":
            "La salle de la cheminée s’ouvre pour les tablées à partir de "
            "douze couverts. Menu fixe, vin maison inclus, desserts de Giulia "
            "pour finir. Pour anniversaires, communions, dîners de promo, "
            "enterrements de vie de garçon, dîners d’entreprise — ou "
            "simplement parce qu’être ensemble fait du bien.",

        # 3 group experiences
        "experiences_label":   "Trois formules",
        "meta_menu_label":     "Menu",
        "meta_wine_label":     "Vins",
        "experiences": [
            {
                "n":       "01",
                "title":   "Longue tablée",
                "persons": "de 12 à 20 personnes",
                "menu":    "Antipasti, deux primi au choix, secondo, dessert · 32,00 €",
                "wine":    "Cesanese maison et eau inclus",
                "desc":
                    "La formule historique : longue table dans la salle de "
                    "la cheminée, plats à partager, rythme tranquille. "
                    "Parfait pour anniversaires, dîners de promo, "
                    "enterrements de vie de garçon. Réservation quatre "
                    "jours à l’avance.",
            },
            {
                "n":       "02",
                "title":   "Communion & baptême",
                "persons": "de 20 à 40 personnes",
                "menu":    "Buffet d’antipasti, deux primi, deux secondi, gâteau · 48,00 €",
                "wine":    "Cesanese + Malvasia + boissons inclus · bulles à part",
                "desc":
                    "Les deux salles ouvertes sur mesure, enfants bienvenus, "
                    "gâteau de Giulia inclus au menu (tu choisis parmi trois : "
                    "ricotta et griottes, chocolat et poires, mille-feuille "
                    "à la vanille). Réservation deux semaines à l’avance.",
            },
            {
                "n":       "03",
                "title":   "Dîner d’entreprise",
                "persons": "de 25 à 60 personnes",
                "menu":    "Menu dégustation en cinq services · 62,00 €",
                "wine":    "Accord signé par le sommelier de la maison · quatre verres",
                "desc":
                    "Privatisation complète de la trattoria, un soir en "
                    "semaine (mar. – jeu.). Menu en trois langues si besoin, "
                    "projecteur pour les présentations, Wi-Fi libre. "
                    "Réservation un mois à l’avance.",
            },
        ],

        # Birthday/celebration block
        "birthday_label":   "Anniversaires & jubilés",
        "birthday_heading": "Le gâteau de Giulia, les bougies, <em>et un toast avec Nonna Rosa.</em>",
        "birthday_text":
            "Pour chaque anniversaire, Giulia prépare un gâteau sur mesure "
            "(dis-lui deux jours à l’avance le parfum préféré). On l’apporte "
            "avec les bougies allumées, Nonna Rosa sort de la cuisine pour "
            "le toast, et si tu es chanceux elle te chante même une strophe "
            "de « Roma nun fa’ la stupida stasera » — mais seulement si c’est "
            "toi qui le demandes, parce qu’avec nous elle ne le fait jamais.",
        "birthday_image":   "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=1200&q=80&auto=format&fit=crop",
        "birthday_caption": "Tarte ricotta-griottes · soixantième anniversaire de Beppe",

        # Contact card specific to events
        "contact_label":    "Pour organiser une tablée",
        "contact_heading":  "Parle directement <em>avec Giulia.</em>",
        "contact_text":
            "Les tablées et les événements, c’est Giulia qui les gère en "
            "personne. Appelle-la entre dix heures et midi (c’est l’heure "
            "où elle n’est pas encore en salle) ou écris-lui sur WhatsApp : "
            "elle te répond dans l’après-midi. Si l’e-mail est plus pratique, "
            "ça marche aussi.",
        "contact_phone":    "06 581 4488",
        "contact_whatsapp": "06 581 4488",
        "contact_email":    "eventi@trattoriadanonnarosa.it",
        "contact_cta":      "Écris à Giulia",
        "contact_cta_href": "contatti",
    },

    # ─── CONTATTI (reservations + find us) ────────────────────────
    "contatti": {
        "eyebrow":  "Nous trouver & réserver · Via dei Salumi 16/a",
        "headline": "Réserve une table, <em>ou viens sans prévenir.</em>",
        "intro":
            "On est Via dei Salumi, à Trastevere, à cinq minutes à pied du "
            "lungotevere. Si tu viens à deux ou à trois, pas besoin de "
            "réserver : tu entres, on te trouve une table. À partir de "
            "quatre, mieux vaut un coup de fil la veille. Pour les groupes "
            "au-delà de douze, va sur la page tablées.",

        # Address card
        "address_label":   "Où l’on est",
        "address_heading": "Via dei Salumi 16/a",
        "address_text":
            "À Trastevere, entre Piazza dei Mercanti et le lungotevere Ripa. "
            "La porte est en bois vert, la sonnette fait du bruit. "
            "Métro B station Circo Massimo (dix minutes à pied), "
            "tram 8 arrêt Belli (quatre minutes), bus H arrêt Sonnino.",
        "address_city":    "00153 Roma · Trastevere",

        # Hours table — 4 rows
        "hours_label":   "Horaires d’ouverture",
        "hours_heading": "Déjeuner & dîner, <em>lundi repos.</em>",
        "hours_table": [
            ("Mardi – samedi", "12 h 30 – 15 h 00",     "déjeuner"),
            ("Mardi – samedi", "19 h 00 – 23 h 30",     "dîner · four à bois allumé"),
            ("Dimanche",       "12 h 30 – 15 h 00",     "déjeuner uniquement · fermeture 16 h 00"),
            ("Lundi",          "fermé",                 "repos hebdomadaire"),
        ],

        # Phone/WhatsApp/email card
        "contact_label":     "Parle avec nous",
        "contact_heading":   "Trois manières, <em>toutes bonnes.</em>",
        "contact_phone_label":    "Appelle au comptoir",
        "contact_phone_value":    "06 581 4488",
        "contact_phone_hours":    "Giulia répond de 10 h à 23 h",
        "contact_whatsapp_label": "Écris sur WhatsApp",
        "contact_whatsapp_value": "06 581 4488",
        "contact_whatsapp_hours": "On te répond en une heure",
        "contact_email_label":    "Écris-nous un e-mail",
        "contact_email_value":    "ciao@trattoriadanonnarosa.it",
        "contact_email_hours":    "On répond dans la journée qui suit",

        # Reservation form
        "form_label":    "Réserve en ligne",
        "form_heading":  "Réserve une table, <em>on t’écrit sur l’ardoise.</em>",
        "form_intro":
            "Remplis le formulaire ci-dessous. Tu recevras une confirmation "
            "par SMS ou WhatsApp dans les deux heures (on est en cuisine, "
            "mais on regarde les téléphones). Pour les groupes au-delà de "
            "douze, écris-nous directement sur WhatsApp.",

        "form_sections": [
            {
                "num":   "01",
                "title": "Qui tu es",
                "meta":  "Pour te confirmer la table",
                "fields": ["name", "email", "phone"],
            },
            {
                "num":   "02",
                "title": "Quand tu viens",
                "meta":  "Date, heure et combien vous êtes",
                "fields": ["date", "time", "people"],
            },
            {
                "num":   "03",
                "title": "Notes",
                "meta":  "Occasion, allergies, préférences",
                "fields": ["occasion", "notes"],
            },
        ],

        "form_fields": [
            {
                "name":     "name",
                "label":    "Nom et prénom",
                "type":     "text",
                "placeholder": "Comment on t’appelle à table",
                "required": True,
                "helper":   "On l’écrit sur l’ardoise des réservations.",
            },
            {
                "name":     "email",
                "label":    "E-mail",
                "type":     "email",
                "placeholder": "prenom@exemple.fr",
                "required": True,
                "helper":   "On t’envoie la confirmation ici.",
            },
            {
                "name":     "phone",
                "label":    "Téléphone ou WhatsApp",
                "type":     "tel",
                "placeholder": "+33 6 12 34 56 78",
                "required": True,
                "helper":   "On t’y cherche uniquement en cas d’imprévu.",
            },
            {
                "name":     "date",
                "label":    "Date",
                "type":     "date",
                "placeholder": "jj/mm/aaaa",
                "required": True,
                "helper":   "On est fermés le lundi.",
            },
            {
                "name":     "time",
                "label":    "Heure",
                "type":     "time",
                "placeholder": "ex. 20 h 30",
                "required": True,
                "helper":   "Déjeuner 12 h 30 – 14 h 30 · dîner 19 h 00 – 22 h 30.",
            },
            {
                "name":     "people",
                "label":    "Combien vous êtes",
                "type":     "number",
                "placeholder": "nombre de couverts",
                "required": True,
                "helper":   "Au-delà de douze, écris directement sur WhatsApp.",
            },
            {
                "name":     "occasion",
                "label":    "Occasion",
                "type":     "select",
                "placeholder": "",
                "required": False,
                "full_width": True,
                "helper":   "Si c’est un anniversaire, on prépare le gâteau de Giulia.",
            },
            {
                "name":     "notes",
                "label":    "Notes pour la cuisine",
                "type":     "textarea",
                "placeholder": "Allergies, plats préférés, demandes particulières…",
                "required": False,
                "full_width": True,
                "helper":   "Nonna Rosa a passé la formation HACCP en 2019 : dis-le nous, c’est tout.",
            },
        ],

        "occasion_options": [
            "Dîner normal",
            "Anniversaire",
            "Anniversaire de couple",
            "Déjeuner de travail",
            "Première fois chez nous",
            "Tablée (12 et +)",
            "Autre",
        ],

        "consent":
            "J’accepte le traitement de mes données pour la gestion de la "
            "réservation (aucune newsletter, aucune publicité, jamais).",
        "form_submit":      "Réserver la table",
        "form_submit_note": "On te confirme dans les deux heures, par SMS ou WhatsApp.",

        # Map
        "map_label":    "Sur le plan",
        "map_heading":  "Via dei Salumi 16/a · Trastevere",
        "map_embed":
            "https://www.openstreetmap.org/export/embed.html"
            "?bbox=12.4660%2C41.8880%2C12.4720%2C41.8910"
            "&layer=mapnik&marker=41.8893%2C12.4690",
        "map_link":     "Ouvrir sur OpenStreetMap",
        "map_link_href":"https://www.openstreetmap.org/?mlat=41.8893&mlon=12.4690#map=17/41.8893/12.4690",

        # Getting-here notes
        "transport_label":   "Comment venir",
        "transport_heading": "Trois moyens, <em>tous à pied depuis le centre.</em>",
        "transport": [
            {
                "mode":  "Métro",
                "line":  "B · station Circo Massimo",
                "note":  "Dix minutes à pied le long de la via di Monte Savello et du lungotevere Ripa.",
            },
            {
                "mode":  "Tram",
                "line":  "8 · arrêt Belli",
                "note":  "Quatre minutes à pied, en traversant Piazza Trilussa vers la Via dei Salumi.",
            },
            {
                "mode":  "Bus",
                "line":  "H · arrêt Sonnino",
                "note":  "Six minutes à pied, en passant par Piazza in Piscinula.",
            },
            {
                "mode":  "À pied depuis le centre",
                "line":  "Ponte Sisto · quinze minutes",
                "note":  "Depuis Piazza Navona, en traversant Campo de’ Fiori et le Ponte Sisto.",
            },
        ],
    },

    # No blog
    "posts": [],
}
