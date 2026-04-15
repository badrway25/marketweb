"""BENESSERE_CONTENT_FR — native wellness-premium translation.

Registre éditorial: Marie Claire Bien-Être / Thermes Marins Saint-Malo /
Cinq Mondes. Vous de politesse chaleureux, écriture littéraire, sensorielle.
Noms propres italiens (Studio Armonia, Bergamo Alta, Via Arena 15, Sara
Conti, Davide Lai, Yara Bonomi, Elena Rossi, Miguel Ferrari, Chiara Bonomi)
préservés verbatim.
"""
from __future__ import annotations

from typing import Any

from apps.catalog.template_content_benessere import (
    _AMBIENT_CANDLES,
    _AMBIENT_MASSAGE,
    _AMBIENT_RITUAL,
    _AMBIENT_TEA,
    _AMBIENT_YOGA,
    _HERO_IMG,
    _MAP_IMG,
    _PORTRAIT_DAVIDE,
    _PORTRAIT_ELENA,
    _PORTRAIT_MIGUEL,
    _PORTRAIT_SARA,
    _PORTRAIT_YARA,
    _ROOM_GARDEN,
    _ROOM_HAMMAM,
    _ROOM_MEDITATION,
    _ROOM_RECEPTION,
    _ROOM_TISANERIA,
    _ROOM_WATER,
)


BENESSERE_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",           "label": "Accueil",       "kind": "home"},
        {"slug": "filosofia",      "label": "Philosophie",   "kind": "about"},
        {"slug": "rituali",        "label": "Rituels",       "kind": "services"},
        {"slug": "ambienti",       "label": "Espaces",       "kind": "gallery"},
        {"slug": "professionisti", "label": "Praticiens",    "kind": "team"},
        {"slug": "contatti",       "label": "Contact",       "kind": "contact"},
        {"slug": "prenota",        "label": "Réserver",      "kind": "appointment"},
    ],

    "site": {
        "logo_initial":  "A",
        "logo_word":     "Studio Armonia",
        "tag":           "Maison holistique · Bergamo Alta · 800 m d’altitude",
        "nav_cta":       "Réserver un rituel",
        "phone":         "+39 035 412 998",
        "email":         "ritual@studioarmonia.it",
        "address":       "Via Arena 15 · 24129 Bergamo Alta",
        "hours_compact": "Lun – Sam · sur rendez-vous",
        "hours_footer_rows": [
            "Lun – Ven · 9 h 00 – 20 h 00",
            "Samedi · 9 h 00 – 18 h 00",
            "Dimanche · journée du silence",
        ],
        "license":       "Praticiens certifiés FIF et SIAF (fédérations italiennes)",
        "footer_intro":
            "Studio Armonia est une maison holistique indépendante, ouverte "
            "en 2011 à l’abri des remparts de Bergamo Alta. Rituels sur "
            "mesure, praticiens certifiés, temps lent — pour celles et ceux "
            "qui cherchent un souffle, non une prestation.",
        "socials": [
            ("Instagram", "#"),
            ("Journal",   "#"),
            ("Telegram",  "#"),
        ],
    },

    # ───────────────────────── HOME ─────────────────────────
    "home": {
        "hero_image":  _HERO_IMG,
        "eyebrow":     "Maison holistique · Bergamo Alta",
        "headline":    'Un souffle est la mesure de <em>notre temps</em>',
        "subhead":
            "Rituels sur mesure, inspirés des traditions méditerranéennes "
            "et orientales, dans un refuge de pierre hors du temps, à huit "
            "cents mètres d’altitude.",
        "primary_cta":   "Réservez votre rituel",
        "secondary_cta": "Parcourir les soins",
        "hero_meta": [
            "Bergamo Alta",
            "Depuis 2011",
            "Cinq praticiens certifiés",
            "Silence le dimanche",
        ],

        "manifesto_label": "Manifeste · Studio Armonia",
        "manifesto":
            "À Armonia on ne vient pas pour ajouter — on vient pour "
            "déposer. Déposer la hâte, la voix intérieure qui réprimande, "
            "la posture fatiguée de qui porte trois pensées à la fois. Nos "
            "rituels sont faits de temps lent, d’huiles chaudes, d’eaux de "
            "source et de silences choisis. Nous ne sommes pas un spa "
            "d’hôtel : nous sommes un atelier de présence, ouvert depuis "
            "quinze ans entre les hautes murailles de Bergame.",
        "manifesto_signature": "— Chiara Bonomi, fondatrice",

        "rituali_label": "Rituels à l’honneur",
        "rituali_heading": 'Quatre <em>mesures du temps</em>, à choisir',
        "rituali_intro":
            "La liste complète des dix rituels figure sur sa page dédiée. "
            "Voici les plus demandés par celles et ceux qui viennent pour "
            "la première fois.",
        "rituali": [
            ("Massage Méditerranéen",
             "55 minutes · huile d’olive et agrumes de Sorrente",
             "85 €"),
            ("Rituel Hammam",
             "90 minutes · vapeur, sel brut, argile rouge",
             "120 €"),
            ("Rééquilibrage énergétique",
             "60 minutes · pranothérapie et souffle guidé",
             "95 €"),
            ("Ayurveda Abhyanga",
             "90 minutes · huiles chaudes, deux praticiennes",
             "135 €"),
        ],

        "benefits_label": "Ce que l’on emporte",
        "benefits_heading": 'Trois <em>mots</em>, non trois promesses',
        "benefits_intro":
            "Nous ne promettons pas de transformation radicale en "
            "quatre-vingt-dix minutes. Nous promettons un ralentissement "
            "mesuré et répétable.",
        "benefits": [
            ("Équilibre",
             "Un système nerveux qui se détend, une posture qui se "
             "retrouve, un rythme respiratoire qui cesse de poursuivre "
             "les échéances."),
            ("Souffle",
             "La pratique respiratoire est le fil rouge de chaque rituel. "
             "On en repart en sachant où se trouve son diaphragme — et "
             "jusqu’où il s’était arrêté."),
            ("Enracinement",
             "Contact avec son propre poids, avec la pierre ancienne sous "
             "les pieds, avec ce territoire. On ne médite pas dans le vide : "
             "on médite chez soi."),
        ],

        "ambients_label": "Espaces · Studio Armonia",
        "ambients_heading": 'Un édifice du <em>XVIIᵉ siècle</em>, restauré avec retenue',
        "ambients_intro":
            "Palazzo Bonomi Suardi, Via Arena 15. Quatre salles, un "
            "cloître d’herbes officinales, une tisanerie ouverte à tous "
            "nos hôtes.",
        "ambients": [
            (_AMBIENT_MASSAGE, "Salle du Massage",       "lumière rasante par les vitrages toute hauteur"),
            (_AMBIENT_TEA,     "Tisanerie des Herbes",   "cueillies au cloître · servies en porcelaine"),
            (_AMBIENT_CANDLES, "Salle du Rituel",        "bougies de cire d’abeille · serviettes chaudes"),
            (_AMBIENT_YOGA,    "Atelier du Souffle",     "parquet ancien · tapis de laine brute"),
        ],

        "therapists_label": "Praticiens",
        "therapists_heading": 'Cinq <em>mains</em> qui connaissent le prénom de chaque hôte',
        "therapists_intro":
            "Chaque rituel est mené personnellement par un praticien "
            "certifié. La liste complète, avec biographies étendues, se "
            "trouve sur la page Praticiens.",
        "therapists_trio": [
            {
                "name": "Sara Conti",
                "role": "Naturopathe · Co-fondatrice",
                "bio":
                    "Douze années d’exercice, formée à l’Istituto Riza de "
                    "Milan. Elle s’occupe de phytothérapie, d’hydrothérapie "
                    "alpine et du programme saisonnier de dépuration.",
                "portrait": _PORTRAIT_SARA,
            },
            {
                "name": "Davide Lai",
                "role": "Ostéopathe D.O.",
                "bio":
                    "Diplômé de la Scuola Superiore di Osteopatia Italiana, "
                    "spécialisé en techniques craniosacrées et viscérales. "
                    "Il reçoit le mardi et le jeudi.",
                "portrait": _PORTRAIT_DAVIDE,
            },
            {
                "name": "Yara Bonomi",
                "role": "Praticienne ayurvédique",
                "bio":
                    "Formée à Varkala (Inde) et certifiée par la S.I.A. "
                    "(Société italienne d’Ayurveda). Elle conduit les "
                    "rituels Abhyanga et le Lomi-Lomi hawaïen, toujours à "
                    "quatre mains avec une seconde praticienne.",
                "portrait": _PORTRAIT_YARA,
            },
        ],

        "journey_label": "Comment se déroule votre visite",
        "journey_heading": 'La <em>visite</em>, pas à pas',
        "journey_intro":
            "Chaque rituel suit la même liturgie : accueil silencieux, "
            "soin, pause tisane, souffle. Nous n’avons ni enceintes ni "
            "musique imposée — le temps se mesure tout seul.",
        "journey": [
            {
                "num": "01",
                "title": "Accueil",
                "body":
                    "Au seuil, vous déposez chaussures, téléphone et "
                    "précipitation. On vous offre une tisane chaude de "
                    "saison, une feuille de papier recyclé pour noter vos "
                    "demandes et vos attentions, dix minutes de silence "
                    "avant d’entrer en salle.",
            },
            {
                "num": "02",
                "title": "Rituel du corps",
                "body":
                    "Le soin choisi — massage, hammam, shiatsu — est mené "
                    "par votre praticien avec des huiles préparées sur "
                    "place et des étoffes en lin naturel. Aucune attente "
                    "en salle.",
            },
            {
                "num": "03",
                "title": "Pause tisane",
                "body":
                    "Après le rituel, quinze minutes à la tisanerie autour "
                    "d’un mélange ajusté à la saison et à votre "
                    "constitution : ortie au printemps, mélisse en été, "
                    "gingembre en hiver.",
            },
            {
                "num": "04",
                "title": "Souffle de clôture",
                "body":
                    "Trois minutes de respiration guidée avant que l’on "
                    "vous rende téléphone et chaussures. C’est la part la "
                    "plus brève de la liturgie — et c’est elle que vous "
                    "emporterez.",
            },
        ],

        "calendar_label": "Prochaines disponibilités",
        "calendar_heading": 'Choisissez votre <em>moment</em>',
        "calendar_intro":
            "Une sélection des créneaux ouverts cette semaine. Pour "
            "l’agenda complet et les demandes particulières, utilisez le "
            "formulaire de la page Réserver.",
        "calendar": [
            {"day": "Lun", "num": "14", "month": "Avr",
             "slots": ["10 h 00", "14 h 30", "17 h 00"], "has_slots": True, "soldout": False},
            {"day": "Mar", "num": "15", "month": "Avr",
             "slots": ["9 h 30", "15 h 00"],             "has_slots": True, "soldout": False},
            {"day": "Mer", "num": "16", "month": "Avr",
             "slots": ["11 h 00", "16 h 30"],            "has_slots": True, "soldout": False},
            {"day": "Jeu", "num": "17", "month": "Avr",
             "slots": ["complet"],                       "has_slots": False, "soldout": True},
            {"day": "Ven", "num": "18", "month": "Avr",
             "slots": ["10 h 30", "14 h 00", "18 h 00"], "has_slots": True, "soldout": False},
            {"day": "Sam", "num": "19", "month": "Avr",
             "slots": ["complet"],                       "has_slots": False, "soldout": True},
            {"day": "Dim", "num": "20", "month": "Avr",
             "slots": ["silence"],                       "has_slots": False, "soldout": True},
        ],
        "calendar_cta": "Ouvrir le formulaire de réservation",

        "press_label": "Ils en ont parlé",
        "press": [
            "Vogue Italia Living",
            "Marie Claire",
            "Io Donna",
            "Natural Style",
            "Corriere della Sera · Salute",
        ],
    },

    # ──────────────────── FILOSOFIA (about) ────────────────────
    "filosofia": {
        "eyebrow":  "Notre philosophie",
        "headline": "Trois mots, <em>aucune promesse</em>",
        "intro":
            "Studio Armonia est né en 2011 d’une idée simple : une maison "
            "holistique qui ne vende pas de transformation, mais qui "
            "restitue du temps. Trois piliers — Souffle, Rituel, Nature — "
            "inspirent chaque choix, du palimpseste des soins aux herbes "
            "de la tisanerie.",

        "pillars": [
            {
                "init":  "S",
                "title": "Souffle",
                "body":
                    "Le souffle est le fil rouge de chaque rituel. Chaque "
                    "soin s’ouvre et se referme sur trois minutes de "
                    "pratique respiratoire — nous l’appelons le rythme du "
                    "retour.",
            },
            {
                "init":  "R",
                "title": "Rituel",
                "body":
                    "Ni séances, ni forfaits : des rituels. Chacun doté "
                    "d’une liturgie précise, répétable, indépendante de "
                    "l’humeur du praticien comme de l’agenda de la semaine.",
            },
            {
                "init":  "N",
                "title": "Nature",
                "body":
                    "Nos matières viennent du territoire : huile d’olive "
                    "des Pouilles, sel de l’Adriatique, argiles des "
                    "collines émiliennes, herbes cueillies au cloître de "
                    "mars à octobre.",
            },
        ],

        "photo_image": _AMBIENT_RITUAL,
        "photo_caption":
            "Salle du Rituel · Palazzo Bonomi Suardi, Bergamo Alta",
        "photo_sub": "Restauration conservative · 2011",

        "timeline_label": "Notre histoire",
        "timeline_heading": "Quinze années de <em>travail silencieux</em>",
        "timeline": [
            {
                "year":  "2011",
                "title": "La première salle, Via Arena",
                "body":
                    "Chiara Bonomi et Sara Conti ouvrent le premier espace "
                    "au rez-de-chaussée du Palazzo Bonomi Suardi. Deux "
                    "salles, une salle d’attente, une tisanerie de quatre "
                    "mètres carrés.",
            },
            {
                "year":  "2014",
                "title": "Le cloître des herbes officinales",
                "body":
                    "Le cloître intérieur est restauré et le premier "
                    "jardin d’herbes officinales planté : mélisse, "
                    "lavande, sauge sclarée, millepertuis, ortie, menthe "
                    "poivrée.",
            },
            {
                "year":  "2018",
                "title": "Le hammam et la salle de vapeur",
                "body":
                    "Ajout de la salle hammam, voûte en berceau de "
                    "briques récupérées, conçue par l’architecte Valeria "
                    "Cipolli en dialogue avec la Soprintendenza.",
            },
            {
                "year":  "2022",
                "title": "L’atelier du Souffle",
                "body":
                    "Ouverture de l’Atelier du Souffle au premier étage, "
                    "sur parquet ancien restauré, dédié au yoga, à la "
                    "méditation et aux pratiques somatiques de groupe "
                    "(six personnes au maximum).",
            },
        ],

        "cta_label": "Le pas suivant",
        "cta_heading": 'Rencontrer <em>Studio Armonia</em> en personne',
        "cta_sub":
            "Le seuil ne se franchit pas en ligne. Réservez un rituel "
            "court — soixante-cinq minutes — et laissez l’espace faire "
            "le reste.",
        "cta_primary":   "Réserver un rituel",
        "cta_secondary": "Parcourir les rituels",
    },

    # ──────────────────── RITUALI (services) ────────────────────
    "rituali": {
        "eyebrow":  "Carte des rituels",
        "headline": "Dix rituels, <em>aucune voie rapide</em>",
        "intro":
            "Chaque rituel a une durée précise, un praticien dédié, une "
            "liturgie sédimentée au fil des années. Les tarifs sont "
            "définitifs — ni majoration week-end, ni supplément caché.",

        "treatments": [
            {
                "name":  "Massage Méditerranéen",
                "meta":  "55 min · huile d’olive de Sorrente et agrumes",
                "desc":
                    "Pressions longues, huile chaude extraite à froid, "
                    "essences de bergamote et de citron de Sorrente. "
                    "Indiqué pour la première visite ou pour un rituel "
                    "d’introduction non invasif.",
                "price": "85 €",
            },
            {
                "name":  "Rituel Hammam",
                "meta":  "90 min · vapeur, sel brut, argile rouge",
                "desc":
                    "Vingt-quatre minutes en salle de vapeur aux huiles "
                    "essentielles d’eucalyptus, gommage au sel brut de "
                    "l’Adriatique, masque d’argile rouge des collines "
                    "bolonaises, douche de source, tisane de clôture. "
                    "À quatre mains.",
                "price": "120 €",
            },
            {
                "name":  "Rééquilibrage énergétique",
                "meta":  "60 min · pranothérapie et souffle guidé",
                "desc":
                    "Séance sans contact de pranothérapie menée par "
                    "Chiara Bonomi, avec pratique respiratoire guidée "
                    "dans les dix premières et les dix dernières minutes. "
                    "Adapté à la grossesse à partir du deuxième trimestre.",
                "price": "95 €",
            },
            {
                "name":  "Hydrothérapie alpine",
                "meta":  "75 min · eaux de source du Monte Resegone",
                "desc":
                    "Parcours en trois bassins à température croissante "
                    "avec eaux de source mises en bouteille à la source, "
                    "alternées de jets froids. Parcours mené par Davide Lai.",
                "price": "110 €",
            },
            {
                "name":  "Pierres Chaudes",
                "meta":  "75 min · basalte volcanique · huile d’amande",
                "desc":
                    "Douze pierres de basalte chauffées à 48 °C posées "
                    "sur les points Shu du dos, massage de dénouement à "
                    "l’huile d’amande douce et à l’huile essentielle "
                    "d’encens.",
                "price": "105 €",
            },
            {
                "name":  "Ayurveda Abhyanga",
                "meta":  "90 min · huiles chaudes médicinales · deux praticiennes",
                "desc":
                    "Rituel ayurvédique classique mené par Yara Bonomi "
                    "en binôme avec une seconde praticienne. Huiles "
                    "médicinales choisies selon la constitution (Vata, "
                    "Pitta, Kapha) identifiée lors de l’entretien "
                    "préliminaire.",
                "price": "135 €",
            },
            {
                "name":  "Shiatsu",
                "meta":  "60 min · pressions sur les méridiens · sur futon",
                "desc":
                    "Séance traditionnelle de shiatsu menée par Miguel "
                    "Ferrari sur futon japonais. Vous restez vêtu·e de "
                    "tenues confortables fournies par le studio.",
                "price": "90 €",
            },
            {
                "name":  "Lomi-Lomi",
                "meta":  "75 min · massage hawaïen à vagues longues",
                "desc":
                    "Longues vagues de l’avant-bras et de la paume, "
                    "huiles tropicales de coco et de monoï. Mené par "
                    "Yara Bonomi, certifiée par la Hawaiian Lomi-Lomi "
                    "School de Kauai.",
                "price": "115 €",
            },
            {
                "name":  "Craniosacré",
                "meta":  "55 min · toucher léger · fluides céphalorachidiens",
                "desc":
                    "Séance d’ostéopathie craniosacrée menée par Davide "
                    "Lai. Pressions très légères (moins de cinq grammes) "
                    "pour écouter et accompagner le rythme des fluides. "
                    "Compatible avec la grossesse.",
                "price": "95 €",
            },
            {
                "name":  "Rituel Mère-Terre",
                "meta":  "105 min · rituel complet saisonnier",
                "desc":
                    "Notre rituel le plus long, pensé pour les changements "
                    "de saison : hydrothérapie brève, gommage intégral, "
                    "massage aux huiles de saison, rite de clôture avec "
                    "bol tibétain et tisane de cynorrhodon.",
                "price": "150 €",
            },
        ],
        "reserve_label": "Réserver",

        "advice_label":   "Avant le soin",
        "advice_heading": "Trois <em>attentions</em> que nous conseillons",
        "advice": [
            {
                "title": "Arrivez un quart d’heure avant",
                "body":
                    "La transition n’est pas un luxe : elle fait partie "
                    "du rituel. Quinze minutes en salle d’attente, "
                    "autour d’une tisane chaude, permettent au système "
                    "nerveux de s’accorder à l’espace.",
            },
            {
                "title": "Évitez le café dans les deux heures précédentes",
                "body":
                    "La caféine rend le corps plus réactif aux "
                    "pressions et raccourcit la fenêtre de relâchement. "
                    "Une tisane, un verre d’eau tiède, une camomille : "
                    "mieux vaut.",
            },
            {
                "title": "Signalez chaque attention",
                "body":
                    "Grossesse, cycle menstruel, intolérances "
                    "olfactives, blessures récentes, médicaments : à "
                    "communiquer systématiquement à la réservation. "
                    "Rien n’est embarrassant — tout est utile à votre "
                    "praticien.",
            },
        ],

        "packages_label":   "Forfaits · longs week-ends",
        "packages_heading": 'Deux <em>séjours</em> pensés comme des parenthèses',
        "packages_intro":
            "Deux propositions cousues avec des hôtels partenaires de "
            "Bergamo Alta, pour celles et ceux qui souhaitent un court "
            "séjour de récupération.",
        "packages": [
            {
                "tag":       "Journée unique",
                "title":     "Souffle",
                "duration":  "1 journée · 3 rituels · tisanes illimitées",
                "desc":
                    "Une journée entière au studio avec trois rituels "
                    "enchaînés, accès à la tisanerie de dix heures à dix-"
                    "huit heures, déjeuner léger sur place préparé par "
                    "le chef Matteo Riva.",
                "includes": [
                    "Arrivée 10 h 00, départ avant 18 h 00",
                    "Rééquilibrage énergétique (60 min)",
                    "Massage Méditerranéen (55 min)",
                    "Rituel Mère-Terre court (75 min)",
                    "Déjeuner léger · tisanerie illimitée",
                ],
                "price": "340 €",
                "cta":   "Réserver Souffle",
            },
            {
                "tag":       "Trois jours",
                "title":     "Détox trois jours",
                "duration":  "3 journées · 5 rituels · tisanerie saisonnière",
                "desc":
                    "Trois journées cousues avec l’Hotel Gombit "
                    "quatre étoiles (chambre double incluse), cinq "
                    "rituels répartis sur les trois jours, plan "
                    "alimentaire végétarien convenu avec la naturopathe.",
                "includes": [
                    "2 nuits · Hotel Gombit 4★",
                    "Cinq rituels sur trois journées",
                    "Plan alimentaire végétarien par la naturopathe",
                    "Accès libre au cloître et à l’Atelier du Souffle",
                    "Coffret saisonnier à emporter · valeur 85 €",
                ],
                "price": "920 €",
                "cta":   "Réserver les trois jours",
            },
        ],

        "cta_label": "Le pas suivant",
        "cta_heading": 'Un seul <em>seuil</em> à franchir',
        "cta_sub":
            "Réservez le rituel qui vous attire le plus. Si vous n’êtes "
            "pas sûr·e, écrivez-nous : nous vous orientons.",
        "cta_primary":   "Ouvrir le formulaire de réservation",
        "cta_secondary": "Demander un conseil",
    },

    # ──────────────────── AMBIENTI (gallery) ────────────────────
    "ambienti": {
        "eyebrow":  "Palazzo Bonomi Suardi",
        "headline": 'Huit <em>salles</em>, un cloître, une tisanerie',
        "intro":
            "Chaque espace a été restauré en dialogue avec la "
            "Soprintendenza ai Beni Architettonici de Bergame. Briques "
            "apparentes, parquet ancien, vitrages qui ouvrent sur le "
            "cloître des herbes officinales.",
        "rooms": [
            {
                "span":  "a",
                "image": _ROOM_HAMMAM,
                "tag":   "Salle I · Hammam",
                "title": "Hammam à voûte",
                "sub":
                    "Voûte en berceau de briques récupérées lors de la "
                    "restauration, assise à deux niveaux, gommage au sel "
                    "brut et jet d’eau de source froide.",
            },
            {
                "span":  "b",
                "image": _AMBIENT_MASSAGE,
                "tag":   "Salle II · Massages",
                "title": "Salle du Soleil",
                "sub":
                    "Deux lits côte à côte pour les rituels à quatre "
                    "mains. Lumière rasante sud-est.",
            },
            {
                "span":  "c",
                "image": _ROOM_WATER,
                "tag":   "Salle III · Eau",
                "title": "Salle du Rituel d’Eau",
                "sub":
                    "Bassin d’hydrothérapie en cuivre martelé, parcours "
                    "à trois températures. Eau de source du Resegone.",
            },
            {
                "span":  "d",
                "image": _ROOM_TISANERIA,
                "tag":   "Tisanerie",
                "title": "Tisanerie des Herbes",
                "sub":
                    "Mélanges saisonniers cueillis dans notre cloître. "
                    "Servis en porcelaine blanche de Limoges.",
            },
            {
                "span":  "e",
                "image": _ROOM_GARDEN,
                "tag":   "Cloître",
                "title": "Jardin officinal",
                "sub":
                    "Mélisse, lavande, sauge sclarée, millepertuis, "
                    "ortie. Accessible à tous nos hôtes.",
            },
            {
                "span":  "f",
                "image": _AMBIENT_YOGA,
                "tag":   "Atelier du Souffle",
                "title": "Atelier du Souffle",
                "sub":
                    "Parquet ancien restauré, tapis de laine brute, "
                    "six personnes au maximum par séance de groupe.",
            },
            {
                "span":  "g",
                "image": _ROOM_MEDITATION,
                "tag":   "Salle IV · Méditation",
                "title": "Chambre du Silence",
                "sub":
                    "Six tatamis en coton biologique, bol tibétain "
                    "d’époque, lumière de bougies en cire d’abeille.",
            },
            {
                "span":  "h",
                "image": _ROOM_RECEPTION,
                "tag":   "Entrée",
                "title": "Seuil · Réception",
                "sub":
                    "Sol d’origine du XVIIᵉ siècle, livre d’or, "
                    "première tisane chaude au-delà du seuil.",
            },
        ],

        "cta_label": "Le pas suivant",
        "cta_heading": 'Franchissez <em>le seuil</em>',
        "cta_sub":
            "Les espaces s’habitent, ils ne se photographient pas. "
            "La meilleure manière de les connaître reste un rituel bref "
            "de soixante minutes.",
        "cta_primary":   "Réserver un rituel",
        "cta_secondary": "Choisir un soin",
    },

    # ──────────────────── PROFESSIONISTI (team) ────────────────────
    "professionisti": {
        "eyebrow":  "Les praticiens",
        "headline": 'Cinq <em>signatures</em>, un seul livre d’or',
        "intro":
            "Chaque praticien possède une formation spécifique, un "
            "calendrier personnel, une signature de soin distincte. Celui "
            "ou celle qui vous accueille au seuil est aussi celui ou "
            "celle qui vous accompagne au rituel.",

        "people": [
            {
                "name":     "Sara Conti",
                "role":     "Naturopathe · Co-fondatrice",
                "portrait": _PORTRAIT_SARA,
                "tags":     ["Phytothérapie", "Hydrothérapie", "Programme saisonnier"],
                "bio":
                    "Diplômée en Naturopathie à l’Istituto Riza de Milan "
                    "en 2009 et certifiée FIF (Fédération italienne de "
                    "phytothérapie). Après cinq années au Spa du Château "
                    "d’Annecy, elle rentre à Bergame et cofonde Studio "
                    "Armonia avec Chiara Bonomi. Elle dirige le programme "
                    "saisonnier de dépuration et le jardin officinal du "
                    "cloître.",
                "quote":
                    "« Il n’existe pas de régime détox. Il existe une "
                    "attention répétée à la manière dont on mange, "
                    "dont on respire, dont on dort. »",
            },
            {
                "name":     "Davide Lai",
                "role":     "Ostéopathe D.O.",
                "portrait": _PORTRAIT_DAVIDE,
                "tags":     ["Craniosacré", "Viscéral", "Structurel"],
                "bio":
                    "Diplômé de la Scuola Superiore di Osteopatia Italiana "
                    "(S.S.O.I.) en 2014, il s’est spécialisé en "
                    "techniques craniosacrées et viscérales. Il reçoit le "
                    "mardi et le jeudi sur rendez-vous, et il est la "
                    "référence du studio pour le post-partum et la "
                    "douleur chronique.",
                "quote":
                    "« Le corps sait déjà comment guérir — mon travail est "
                    "d’écouter où il a cessé de le faire. »",
            },
            {
                "name":     "Yara Bonomi",
                "role":     "Praticienne ayurvédique",
                "portrait": _PORTRAIT_YARA,
                "tags":     ["Abhyanga", "Lomi-Lomi", "Shirodhara"],
                "bio":
                    "Formée à Varkala (Kerala, Inde), à la Kerala "
                    "Ayurveda Academy en 2016, certifiée par la Società "
                    "Italiana di Ayurveda (S.I.A.). Elle mène les rituels "
                    "Abhyanga et Shirodhara — toujours à quatre mains — "
                    "ainsi que le Lomi-Lomi hawaïen.",
                "quote":
                    "« L’abhyanga n’est pas un massage : c’est une "
                    "conversation avec la peau, faite d’huile et de temps. »",
            },
            {
                "name":     "Elena Rossi",
                "role":     "Professeure de yoga certifiée RYT-500",
                "portrait": _PORTRAIT_ELENA,
                "tags":     ["Hatha", "Yin", "Souffle somatique"],
                "bio":
                    "Certifiée RYT-500 par la Yoga Alliance après quatre "
                    "années de pratique à Rishikesh et deux années "
                    "d’études avec Judith Hanson Lasater à San Francisco. "
                    "Elle conduit les séances collectives à l’Atelier du "
                    "Souffle les mercredis, vendredis et samedis matin.",
                "quote":
                    "« Le yoga que je propose ici n’est pas une gymnastique "
                    "exotique : c’est une façon de se rappeler où "
                    "reposent les épaules. »",
            },
            {
                "name":     "Miguel Ferrari",
                "role":     "Praticien shiatsu · FISIEO",
                "portrait": _PORTRAIT_MIGUEL,
                "tags":     ["Shiatsu Namikoshi", "Do-in", "Médecine chinoise"],
                "bio":
                    "Diplômé de l’École européenne de shiatsu de Milan "
                    "en 2018 et inscrit à la FISIEO (Fédération italienne "
                    "des opérateurs shiatsu). Il reçoit le lundi, le "
                    "mercredi et le vendredi, et signe une chronique "
                    "mensuelle sur les saisons du corps selon la médecine "
                    "traditionnelle chinoise.",
                "quote":
                    "« La pression n’est pas la technique : la technique "
                    "est là où j’écoute avant d’appuyer. »",
            },
        ],

        "philo_label": "La philosophie des praticiens",
        "philo_quote":
            "« Un rituel bien mené n’<em>ajoute</em> rien à qui le reçoit : "
            "il lui rappelle seulement ce qu’il savait déjà. »",
        "philo_attr": "— Manifeste des praticiens · 2015",

        "cta_label":   "Le pas suivant",
        "cta_heading": 'Réservez votre <em>première rencontre</em>',
        "cta_primary": "Ouvrir le formulaire de réservation",
    },

    # ──────────────────── CONTATTI (contact) ────────────────────
    "contatti": {
        "eyebrow":  "Trouver le studio",
        "headline": 'Via Arena 15, <em>Bergamo Alta</em>',
        "intro":
            "Nous sommes au cœur de la ville médiévale haute, à quelques "
            "pas de la Piazza Vecchia et de la Basilique Santa Maria "
            "Maggiore. L’entrée est signalée par une plaque en laiton "
            "satiné.",

        "map_image": _MAP_IMG,

        "blocks": [
            {"label": "Adresse",
             "value": "Via Arena 15",
             "sub":   "24129 Bergamo Alta · Palazzo Bonomi Suardi"},
            {"label": "Téléphone",
             "value": "+39 035 412 998",
             "sub":   "Ligne directe 9 h 00 – 19 h 00"},
            {"label": "E-mail",
             "value": "ritual@studioarmonia.it",
             "sub":   "Réponse dans la journée"},
            {"label": "Demandes particulières",
             "value": "+39 346 772 4108",
             "sub":   "WhatsApp · actif 9 h 00 – 18 h 00"},
        ],

        "access_label": "Comment nous rejoindre",
        "access": [
            {"mode": "En voiture",
             "text": "Parking Monterosso (Via Fara), puis cinq minutes à "
                     "pied jusqu’à la Via Arena."},
            {"mode": "Funiculaire",
             "text": "Funiculaire de Bergamo Alta depuis le Viale Vittorio "
                     "Emanuele, arrêt Mercato delle Scarpe, deux minutes "
                     "à pied."},
            {"mode": "À pied",
             "text": "Depuis la gare ferroviaire de Bergamo Bassa, bus "
                     "ligne 1 (15 minutes), ou 35 minutes de promenade "
                     "urbaine."},
        ],

        "form_title": "Écrivez-nous",
        "form_intro":
            "Pour toute information sur les rituels, les rituels-cadeaux "
            "ou les forfaits séjour, utilisez le formulaire ci-dessous. "
            "Nous répondons toujours avant la fin du jour ouvré suivant.",

        "form_placeholders": {
            "name":    "Chiara Ferrari",
            "email":   "chiara@email.fr",
            "phone":   "+39 333 ...",
            "message":
                "Je souhaiterais réserver un rituel pour un cadeau, "
                "de préférence un vendredi après-midi.",
        },
        "form_helpers": {
            "name":     "Comment souhaitez-vous être appelé·e ?",
            "email":    "Nous n’utilisons votre e-mail que pour vous répondre.",
            "phone":    "Si vous préférez que l’on vous rappelle, indiquez-le ici.",
            "interest": "En cas de doute, choisissez Consultation initiale.",
            "message":  "Quelques lignes suffisent — nous savons répondre "
                        "aux questions concrètes.",
        },
        "form_fields": {
            "interest_label": "Rituel d’intérêt",
            "interest_options": [
                "Consultation initiale",
                "Massage Méditerranéen",
                "Rituel Hammam",
                "Rééquilibrage énergétique",
                "Ayurveda Abhyanga",
                "Forfait Souffle",
                "Forfait Détox trois jours",
                "Rituel-cadeau",
                "Autre",
            ],
        },
        "form_consent":
            "Je consens au traitement des données personnelles "
            "conformément au Règl. UE 679/2016. Les données sont "
            "conservées au sein du Studio Armonia et ne sont jamais "
            "cédées à des tiers.",
        "form_submit_note":
            "Réponse avant la fin du jour ouvré suivant.",

        "hours_label":   "Horaires",
        "hours_heading": 'Ouverts <em>six jours</em> sur sept',
        "hours_note":
            "Le dimanche, Studio Armonia observe sa journée du silence. "
            "Pour toute urgence, les hôtes déjà en parcours peuvent "
            "écrire à ritual@studioarmonia.it — réponse garantie sous "
            "trois heures.",
        "hours": [
            {"day": "Lundi",    "value": "9 h 00 – 20 h 00"},
            {"day": "Mardi",    "value": "9 h 00 – 20 h 00"},
            {"day": "Mercredi", "value": "9 h 00 – 20 h 00"},
            {"day": "Jeudi",    "value": "9 h 00 – 20 h 00"},
            {"day": "Vendredi", "value": "9 h 00 – 20 h 00"},
            {"day": "Samedi",   "value": "9 h 00 – 18 h 00"},
            {"day": "Dimanche", "value": "Journée du silence"},
        ],
    },

    # ──────────────────── PRENOTA (appointment) ────────────────────
    "prenota": {
        "eyebrow":  "Réservation",
        "headline": 'Le rituel commence dès que vous <em>franchissez le seuil</em>',
        "intro":
            "La réservation est le premier geste du rituel. Choisissez "
            "la journée qui vous attire le plus, remplissez le "
            "formulaire ci-dessous : nous revenons vers vous sous deux "
            "heures ouvrées pour confirmer.",

        "calendar_heading": 'Sept jours de <em>prochaines disponibilités</em>',
        "calendar_hint":    "Indicatif · confirmation par e-mail",
        "calendar": [
            {"day": "Lun", "num": "14", "month": "Avr",
             "slots": ["10 h 00", "14 h 30", "17 h 00"], "has_slots": True, "soldout": False},
            {"day": "Mar", "num": "15", "month": "Avr",
             "slots": ["9 h 30", "13 h 00", "15 h 00"],  "has_slots": True, "soldout": False},
            {"day": "Mer", "num": "16", "month": "Avr",
             "slots": ["11 h 00", "16 h 30"],            "has_slots": True, "soldout": False},
            {"day": "Jeu", "num": "17", "month": "Avr",
             "slots": ["complet"],                       "has_slots": False, "soldout": True},
            {"day": "Ven", "num": "18", "month": "Avr",
             "slots": ["10 h 30", "14 h 00", "18 h 00"], "has_slots": True, "soldout": False},
            {"day": "Sam", "num": "19", "month": "Avr",
             "slots": ["complet"],                       "has_slots": False, "soldout": True},
            {"day": "Dim", "num": "20", "month": "Avr",
             "slots": ["silence"],                       "has_slots": False, "soldout": True},
        ],

        "form_title":
            'Formulaire de <em>réservation</em>',
        "form_side_note":
            "Prenez cinq minutes pour remplir avec soin. Plus vous nous "
            "laissez de détails, plus le rituel que nous vous "
            "proposerons sera cohérent avec vous.",
        "form_side_small": "↓ Formulaire privé",

        "why_label": "Pourquoi réserver en ligne",
        "why": [
            "Confirmation par e-mail sous deux heures ouvrées.",
            "Annulation courtoise jusqu’à 24 heures avant, sans frais.",
            "Intolérances et attentions lues à l’avance par le praticien.",
            "Votre créneau reste bloqué jusqu’à notre confirmation.",
        ],

        "form_fields": [
            {"name": "name", "label": "Nom et prénom",
             "placeholder": "Chiara Ferrari",
             "type": "text", "required": True, "full_width": False,
             "helper": "Comment souhaitez-vous être appelé·e ?"},
            {"name": "email", "label": "E-mail",
             "placeholder": "chiara@email.fr",
             "type": "email", "required": True, "full_width": False,
             "helper": "La confirmation arrive ici."},
            {"name": "phone", "label": "Téléphone",
             "placeholder": "+39 333 ...",
             "type": "tel", "required": True, "full_width": False,
             "helper": "Utilisé uniquement en cas de besoin."},
            {"name": "ritual", "label": "Rituel",
             "type": "select", "required": True, "full_width": False,
             "options": [
                 "Massage Méditerranéen (55 min · 85 €)",
                 "Rituel Hammam (90 min · 120 €)",
                 "Rééquilibrage énergétique (60 min · 95 €)",
                 "Hydrothérapie alpine (75 min · 110 €)",
                 "Pierres Chaudes (75 min · 105 €)",
                 "Ayurveda Abhyanga (90 min · 135 €)",
                 "Shiatsu (60 min · 90 €)",
                 "Lomi-Lomi (75 min · 115 €)",
                 "Craniosacré (55 min · 95 €)",
                 "Rituel Mère-Terre (105 min · 150 €)",
                 "Forfait Souffle (1 jour · 340 €)",
                 "Forfait Détox trois jours (920 €)",
             ],
             "helper": "En cas de doute, choisissez le Massage "
                       "Méditerranéen : c’est l’introduction la plus "
                       "douce à notre travail."},
            {"name": "duration", "label": "Durée souhaitée",
             "type": "select", "required": False, "full_width": False,
             "options": [
                 "55 minutes",
                 "60 minutes",
                 "75 minutes",
                 "90 minutes",
                 "105 minutes",
             ],
             "helper": "Facultatif · cohérent avec le rituel choisi."},
            {"name": "therapist", "label": "Praticien souhaité",
             "type": "select", "required": False, "full_width": False,
             "options": [
                 "Indifférent",
                 "Sara Conti (naturopathe)",
                 "Davide Lai (ostéopathe)",
                 "Yara Bonomi (ayurveda)",
                 "Elena Rossi (yoga)",
                 "Miguel Ferrari (shiatsu)",
             ],
             "helper": "Si vous souhaitez un praticien précis, indiquez-le ici."},
            {"name": "date", "label": "Date souhaitée",
             "placeholder": "14 avril 2026",
             "type": "date", "required": True, "full_width": False,
             "helper": "Indiquez votre premier choix ; nous proposerons "
                       "des alternatives si nécessaire."},
            {"name": "slot", "label": "Plage horaire",
             "type": "select", "required": True, "full_width": False,
             "options": [
                 "Matin (9 h 00 – 12 h 30)",
                 "Début d’après-midi (13 h 00 – 15 h 30)",
                 "Après-midi (15 h 30 – 18 h 00)",
                 "Fin d’après-midi (18 h 00 – 20 h 00)",
             ],
             "helper": "Les plages sont indicatives, nous confirmons "
                       "l’horaire exact."},
            {"name": "notes", "label": "Attentions et intolérances",
             "placeholder":
                 "Grossesse ? Intolérances olfactives ? Blessures "
                 "récentes ? Quelque chose que votre praticien devrait "
                 "savoir ? C’est ici que nous le lisons.",
             "type": "textarea", "required": False, "full_width": True,
             "helper": "Rien n’est trop petit. Grossesse, cycle, "
                       "médicaments, anxiétés : nous lisons tout à l’avance."},
        ],

        "form_sections": [
            {"num": "01", "title": "Qui vous êtes",
             "meta": "Vos coordonnées essentielles.",
             "fields": ["name", "email", "phone"]},
            {"num": "02", "title": "Le rituel que vous désirez",
             "meta": "En cas de doute, choisissez « indifférent » — nous vous orientons.",
             "fields": ["ritual", "duration", "therapist"]},
            {"num": "03", "title": "Quand",
             "meta": "Indiquez un premier choix · nous confirmons par e-mail.",
             "fields": ["date", "slot"]},
            {"num": "04", "title": "Attentions",
             "meta": "Tout ce que votre praticien doit savoir au préalable.",
             "fields": ["notes"]},
        ],

        "consent":
            "Je consens au traitement des données personnelles selon "
            "la politique de confidentialité (Règl. UE 679/2016). Les "
            "données cliniques et les attentions communiquées restent "
            "dans l’archive interne privée.",

        "submit_label": "Réserver votre moment",
        "form_submit_note":
            "Nous confirmons la disponibilité sous deux heures ouvrées.",

        "footnote":
            "La réservation n’est confirmée qu’après notre e-mail de "
            "réponse. L’annulation courtoise est possible sans frais "
            "jusqu’à vingt-quatre heures avant le rituel — au-delà, "
            "nous retenons 50 % de la valeur au titre de la protection "
            "du praticien.",
    },
}

__all__ = ["BENESSERE_CONTENT_FR"]
