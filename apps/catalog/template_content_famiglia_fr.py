"""FAMIGLIA_CONTENT_FR — native pediatric warm-family translation.

Voice: Doctissimo Enfant / Magicmaman / cabinet pédiatrique premium Paris 16e.
Vouvoiement chaleureux — "votre enfant", "votre bébé", "les premières années".
Ton parental rassurant, jamais infantilisant, jamais clinique-institutionnel.
"""
from __future__ import annotations

from typing import Any


FAMIGLIA_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Accueil",      "kind": "home"},
        {"slug": "studio",   "label": "Le cabinet",   "kind": "about"},
        {"slug": "visite",   "label": "Consultations", "kind": "services"},
        {"slug": "crescita", "label": "Grandir",      "kind": "faq"},
        {"slug": "pediatre", "label": "Les pédiatres", "kind": "team"},
        {"slug": "contatti", "label": "Contact",      "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "P",
        "logo_word":    "Pediatria Famiglia Plus",
        "tag":          "Cabinet pédiatrique · Turin, quartier Crocetta",
        "phone":        "011 549 21 88",
        "phone_tel":    "+390115492188",
        "whatsapp":     "+39 349 123 4567",
        "whatsapp_link": "https://wa.me/393491234567",
        "nav_cta_wa":   "WhatsApp",
        "email":        "studio@crocettapediatria.it",
        "address":      "Corso Galileo Ferraris 140 · 10129 Turin",
        "emergency_tel": "+393491234567",

        "hours_compact": "Lun – Ven · 8:30 – 12:30 · 15:00 – 19:00",
        "hours_footer_rows": [
            "Samedi · 9:00 – 12:00 · urgences uniquement",
            "Dimanche · astreinte téléphonique",
        ],
        "license":
            "N° TVA 11234120014 · Ordre des Médecins de Turin 08/5412",
        "footer_intro":
            "Cabinet pédiatrique privé dans le quartier Crocetta de "
            "Turin. Quatre pédiatres, une néonatologue et une "
            "infirmière dédiée. Des consultations de trente minutes, "
            "une astreinte téléphonique les dimanches et jours fériés, "
            "une écoute sincère des enfants et de leurs parents.",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":       "Cabinet pédiatrique · Turin, Crocetta",
        "headline":      "Grandir <em>aux côtés</em> de vos enfants.",
        "subhead":
            "Quatre pédiatres, une psychomotricienne et une infirmière "
            "dédiée. Des consultations apaisées, du temps pour "
            "écouter vraiment — parce que chaque famille mérite un "
            "point de repère, pas un numéro de guichet.",
        "primary_cta":   "Appeler le cabinet",
        "secondary_cta": "Nous écrire sur WhatsApp",

        "hero_image":
            "https://images.pexels.com/photos/7447009/pexels-photo-7447009.jpeg"
            "?auto=compress&cs=tinysrgb&w=1000&h=1250&fit=crop",
        "hero_image_alt":
            "Pédiatre lors d'un bilan de santé avec une petite fille "
            "dans la salle de consultation lumineuse du quartier "
            "Crocetta",
        "hero_ribbon":   "Conventionné SSN (sécurité sociale italienne)",
        "hero_stamp_initial": "E",
        "hero_stamp_name":    "Dr. Rambaldi",
        "hero_stamp_meta":    "au cabinet aujourd'hui · 8:30 – 13:00",

        "trust_items": [
            {"icon": "clock",  "label": "Consultations de trente minutes, jamais dix"},
            {"icon": "shield", "label": "Astreinte 24h/24 pour les patients suivis"},
            {"icon": "people", "label": "Un cabinet à taille de famille depuis 1998"},
        ],

        # ── Intro trio · tranches d'âge ──
        "age_groups": [
            {
                "icon":  "baby",
                "range": "0 – 2 ans",
                "title": "Nouveau-né et première année",
                "blurb":
                    "Le parcours qui commence dès la première "
                    "semaine : allaitement, sommeil, bilans de "
                    "santé, retour de la maternité Sant'Anna ou "
                    "Mauriziano. Le Dr. Conti vous suit en "
                    "personne jusqu'aux deux ans révolus de votre "
                    "enfant.",
                "items": [
                    "Consultation post-natale sous sept jours",
                    "Bilans de santé au 1er, 3e, 6e, 9e et 12e mois",
                    "Accompagnement allaitement et sommeil",
                ],
            },
            {
                "icon":  "child",
                "range": "3 – 10 ans",
                "title": "Petite enfance et âge scolaire",
                "blurb":
                    "Les années de maternelle et de primaire : "
                    "vaccinations, certificats sportifs, "
                    "surveillance de la courbe de croissance, "
                    "petits imprévus et toutes les questions "
                    "qu'un parent garde d'ordinaire pour soi.",
                "items": [
                    "Bilans de santé annuels",
                    "Calendrier vaccinal complet",
                    "Certificats médicaux sportifs non compétitifs",
                ],
            },
            {
                "icon":  "teen",
                "range": "11 – 18 ans",
                "title": "Adolescence",
                "blurb":
                    "La phase la plus délicate, celle où "
                    "l'adolescent veut parler sans ses parents "
                    "dans la pièce. Consultations dédiées, "
                    "écoute confidentielle, un canal WhatsApp "
                    "pour les questions qu'on ne pose pas à "
                    "voix haute.",
                "items": [
                    "Consultation annuelle en autonomie",
                    "Endocrinologie, croissance, puberté",
                    "Canal confidentiel pour l'adolescent",
                ],
            },
        ],

        # ── Les pédiatres · portrait stack ──
        "team_label":   "Les pédiatres du cabinet",
        "team_heading": "Quatre signatures, <em>un seul dossier de famille.</em>",
        "team_intro":
            "Le cabinet réunit quatre pédiatres qui partagent "
            "dossiers, protocoles et standards de consultation. "
            "Chaque enfant, en revanche, a toujours une pédiatre "
            "référente — la même personne des premiers bilans à "
            "l'adolescence.",

        "doctors": [
            {
                "name":  "Dr.ssa Elisa Rambaldi",
                "role":  "Pédiatre de famille",
                "spec":  "Nutrition infantile",
                "wa_label": "Écrire sur WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Marta Greco",
                "role":  "Pédiatre allergologue",
                "spec":  "Asthme et dermatite atopique",
                "wa_label": "Écrire sur WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Lucia Sferra",
                "role":  "Pédiatre endocrinologue",
                "spec":  "Croissance et puberté",
                "wa_label": "Écrire sur WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Beatrice Conti",
                "role":  "Pédiatre néonatologue",
                "spec":  "Sommeil et allaitement",
                "wa_label": "Écrire sur WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
        ],

        "team_note":
            "L'équipe clinique est complétée par Luisa Ferraro, "
            "infirmière pédiatrique avec quinze ans d'expérience à "
            "l'Hôpital des enfants Regina Margherita, et Giada "
            "Porro, psychomotricienne spécialisée dans les troubles "
            "du développement 0–6 ans.",

        # ── Percorso della crescita · milestone timeline ──
        "journey_label":   "Le parcours de la croissance",
        "journey_heading": "Des premières semaines au <em>lycée</em>.",
        "journey_intro":
            "Un enfant croise la même pédiatre au moins douze fois "
            "avant ses dix-huit ans. Chaque rendez-vous est un "
            "bilan, pas une consultation d'urgence. Voici les cinq "
            "étapes qui rythment le plus ce parcours.",

        "journey_steps": [
            {
                "age":   "1 mois",
                "title": "Premier bilan",
                "desc":  "La pédiatre rencontre le nouveau-né au "
                         "cabinet dans les quarante jours : poids, "
                         "réflexes, allaitement, sommeil et "
                         "premières réassurances aux parents.",
            },
            {
                "age":   "6 mois",
                "title": "Diversification",
                "desc":  "Conseils pratiques sur l'introduction des "
                         "premiers aliments solides, suivi de la "
                         "courbe de croissance et première partie "
                         "du calendrier vaccinal.",
            },
            {
                "age":   "1 an",
                "title": "Premier anniversaire",
                "desc":  "Bilan complet de fin de première année : "
                         "motricité, langage, premières "
                         "interactions sociales. Les rythmes de la "
                         "famille se stabilisent.",
            },
            {
                "age":   "3 ans",
                "title": "Entrée à l'école",
                "desc":  "Le passage à l'école maternelle : "
                         "certificat, contrôles visuels et "
                         "auditifs, évaluation des autonomies et "
                         "des rythmes de sommeil.",
            },
            {
                "age":   "6 ans",
                "title": "Âge scolaire",
                "desc":  "Bilan avant l'école élémentaire : "
                         "posture, alimentation, premiers "
                         "contrôles de la vue et conseils "
                         "sur l'activité physique.",
            },
        ],

        # ── FAQ accordion parents ──
        "faq_label":   "Questions des parents",
        "faq_heading": "Les questions qui nous <em>reviennent</em> le plus souvent.",
        "faq_intro":
            "Nous avons rassemblé les huit questions les plus "
            "fréquentes que les parents nous posent au téléphone "
            "ou en salle d'attente. Si la vôtre n'y figure pas, "
            "vous pouvez nous joindre au numéro du cabinet ou sur "
            "WhatsApp.",

        "faq": [
            (
                "Quand appeler la pédiatre ?",
                "Immédiatement en cas de fièvre au-dessus de "
                "38,5 °C durant les trois premiers mois de vie, "
                "pleurs inconsolables, refus total de "
                "l'alimentation ou du lait pendant plus de 12 "
                "heures, diarrhée sanglante, lésions cutanées "
                "étendues. Pour tout le reste — une fièvre "
                "modérée, une toux nocturne, un coup de soleil "
                "— vous pouvez attendre le matin et appeler "
                "sereinement. Le cabinet répond en personne.",
            ),
            (
                "Comment prendre un premier rendez-vous ?",
                "Il suffit d'appeler le 011 549 21 88 du lundi "
                "au vendredi : le secrétariat, assuré par "
                "Silvia Pairetto, note le nom de l'enfant, son "
                "âge et le motif de la consultation. Vous "
                "pouvez également écrire au numéro WhatsApp "
                "dédié, y compris en dehors des horaires "
                "d'ouverture. Il n'existe pas d'agenda en "
                "ligne : nous préférons parler avec vous "
                "avant.",
            ),
            (
                "Que dois-je apporter à la première consultation ?",
                "Le carnet de santé de l'enfant, l'éventuelle "
                "lettre de sortie de la maternité, le "
                "récapitulatif des vaccinations déjà faites "
                "et — si l'enfant a plus d'un an — le carnet "
                "de diversification. Inutile d'apporter des "
                "examens récents : la pédiatre ne demande que "
                "ce dont elle a réellement besoin.",
            ),
            (
                "Le cabinet est-il accessible en poussette ?",
                "Oui. L'entrée se situe au rez-de-chaussée "
                "surélevé du 140 Corso Galileo Ferraris, avec "
                "deux marches et une rampe latérale. À "
                "l'intérieur, un coin poussettes est prévu "
                "dans la salle d'attente et les toilettes "
                "sont équipées d'une table à langer. Toutes "
                "les salles de consultation sont au rez-de-"
                "chaussée.",
            ),
            (
                "Que se passe-t-il le soir ou le week-end ?",
                "Le Dr. Rambaldi et le Dr. Greco se relaient "
                "pour l'astreinte téléphonique des patients "
                "suivis : soirées en semaine, nuit, samedi "
                "après-midi et dimanche. Le numéro dédié vous "
                "est communiqué après la première "
                "consultation. Pour les vraies urgences, "
                "composez le 118 ou rendez-vous à l'hôpital "
                "des enfants Regina Margherita.",
            ),
            (
                "Quels vaccins sont obligatoires ?",
                "Le décret Lorenzin de 2017 prévoit dix "
                "vaccinations obligatoires pour "
                "l'inscription à l'école obligatoire. Le "
                "cabinet suit le calendrier national de la "
                "Région Piémont et propose un parcours "
                "vaccinal privé, sans files d'attente à "
                "l'ASL, avec la possibilité d'espacer les "
                "doses à la demande des parents.",
            ),
            (
                "Combien de temps dure une consultation de suivi ?",
                "Une consultation de bilan au cabinet dure "
                "toujours trente minutes, même quand "
                "l'enfant va très bien. C'est le temps "
                "minimum pour faire l'examen clinique, "
                "peser et mesurer sans précipitation, mettre "
                "à jour le carnet de santé et répondre aux "
                "questions des parents sans que personne ne "
                "se sente pressé.",
            ),
            (
                "Combien coûte une consultation pédiatrique privée ?",
                "La première consultation coûte 90 euros, "
                "les bilans suivants 70 euros, les "
                "consultations de contrôle 60 euros. Les "
                "familles avec deux enfants suivis ou plus "
                "bénéficient d'une remise de 15 %. Tous les "
                "paiements sont déductibles en tant que "
                "frais de santé avec un reçu émis le jour "
                "même.",
            ),
        ],

        # ── Studio child-friendly gallery ──
        "gallery_label":   "Le cabinet",
        "gallery_heading": "Une maison, <em>pas un service hospitalier.</em>",
        "gallery_intro":
            "Nous avons pensé chaque pièce pour que l'enfant "
            "n'ait pas peur d'entrer. De la salle d'attente "
            "bordée de livres à la table à langer chauffée, des "
            "jouets sur tables basses à la salle de consultation "
            "colorée.",
        "gallery": [
            {
                "src": "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                       "?auto=compress&cs=tinysrgb&w=1000&h=800&fit=crop",
                "cap": "Salle de consultation · rez-de-chaussée",
            },
            {
                "src": "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Coin stéthoscope ludique",
            },
            {
                "src": "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Salle allaitement",
            },
            {
                "src": "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Salle bilans du nouveau-né",
            },
            {
                "src": "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Entrée · Corso Galileo Ferraris",
            },
        ],

        # ── Orari band ──
        "hours_heading": "Horaires d'ouverture",
        "hours": [
            ("Lun – Ven",  "8:30 – 12:30  ·  15:00 – 19:00"),
            ("Samedi",     "9:00 – 12:00  ·  urgences uniquement"),
            ("Dimanche",   "Astreinte téléphonique"),
            ("Jours fériés", "Ligne dédiée pour les patients suivis"),
        ],
        "urgency_label": "Urgences de nuit",
        "urgency_title": "Nous restons proches en dehors des horaires aussi.",
        "urgency_text":
            "Les patients suivis disposent d'un numéro dédié "
            "d'astreinte nocturne et les jours fériés, ouvert "
            "tous les jours de 19h30 à 8h00. Pour les "
            "véritables urgences, composez le 118 ou "
            "rendez-vous à l'hôpital des enfants Regina "
            "Margherita.",
        "urgency_phone": "+39 349 123 4567",

        # ── Bottom CTA band ──
        "cta_heading":     "Avez-vous besoin <em>de nous</em> ?",
        "cta_lead":
            "Appeler le cabinet est la manière la plus simple et "
            "la plus humaine de commencer. Nous répondons en "
            "personne, sans serveur vocal et sans temps d'attente. "
            "Si vous préférez, nous sommes aussi sur WhatsApp.",
        "cta_phone_label": "Téléphone du cabinet",
        "cta_or":          "ou bien",
        "cta_wa_label":    "Nous écrire sur WhatsApp",
    },

    # ─── LO STUDIO (about) ───────────────────────────────────────
    "studio": {
        "eyebrow":  "Le cabinet",
        "headline": "Depuis 1998, <em>une maison</em> pour les familles de Crocetta.",
        "intro":
            "Nous avons ouvert comme cabinet pédiatrique de quartier "
            "en 1998, à l'initiative du Dr. Rambaldi. En vingt-sept "
            "ans nous avons suivi plus de trois mille enfants — "
            "dont beaucoup sont aujourd'hui devenus parents et nous "
            "ramènent leurs propres enfants. C'est le plus beau "
            "compliment que nous puissions recevoir.",

        "values": [
            {
                "icon":  "clock",
                "title": "Des temps longs",
                "desc":  "Trente minutes par consultation, jamais "
                         "moins. Le temps est le seul outil qui "
                         "fasse réellement la différence entre un "
                         "diagnostic juste et un diagnostic "
                         "erroné.",
            },
            {
                "icon":  "ear",
                "title": "Une écoute sincère",
                "desc":  "Nous écoutons d'abord les parents, puis "
                         "les enfants, puis les adolescents. "
                         "Chacun avec son espace et sa voix.",
            },
            {
                "icon":  "home",
                "title": "Un cadre de maison",
                "desc":  "Des pièces colorées mais non "
                         "infantilisantes, une lumière naturelle, "
                         "des odeurs rassurantes. Un cabinet doit "
                         "ressembler à une maison, pas à un "
                         "service hospitalier.",
            },
            {
                "icon":  "people",
                "title": "Continuité",
                "desc":  "Chaque enfant a sa pédiatre référente, "
                         "la même des premiers bilans aux dix-huit "
                         "ans. On partage les dossiers, pas les "
                         "personnes.",
            },
        ],

        "studio_image":
            "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
            "?auto=compress&cs=tinysrgb&w=1600&h=700&fit=crop",
        "studio_image_caption":
            "Cabinet pédiatrique · Corso Galileo Ferraris 140, Turin",

        "history_label":   "Vingt-sept ans de cabinet",
        "history_heading": "Quatre étapes, <em>trois générations</em> d'enfants.",
        "history_intro":
            "Le cabinet a changé trois fois d'adresse dans la même "
            "rue, a élargi son équipe d'une à cinq "
            "professionnelles et a traversé trois réformes du "
            "système de santé. Une chose n'a jamais changé : la "
            "consultation dure trente minutes.",

        "history": [
            (
                "1998",
                "Le Dr. Elisa Rambaldi ouvre le premier cabinet "
                "pédiatrique rue Morgari, deux salles et une "
                "secrétaire. Les quinze premières familles "
                "sont toujours suivies aujourd'hui.",
            ),
            (
                "2008",
                "Transfert au 140 Corso Galileo Ferraris, "
                "rez-de-chaussée accessible en poussette. Le "
                "Dr. Marta Greco rejoint le cabinet comme "
                "pédiatre allergologue et Silvia Pairetto "
                "devient secrétaire clinique.",
            ),
            (
                "2016",
                "L'équipe s'élargit avec le Dr. Lucia Sferra "
                "(endocrinologie pédiatrique) et lancement "
                "d'une consultation de psychomotricité pour "
                "les troubles du développement avec Giada "
                "Porro.",
            ),
            (
                "2026",
                "Le cabinet atteint cinq professionnelles "
                "avec l'arrivée du Dr. Beatrice Conti "
                "(néonatologie) et inaugure le canal WhatsApp "
                "dédié à l'adolescence.",
            ),
        ],

        "cta_heading":
            "Vous souhaitez rencontrer les pédiatres <em>avant</em> de réserver ?",
        "cta_lead":
            "Vous pouvez lire leurs parcours, regarder leurs "
            "visages et choisir celle que vous préférez pour la "
            "première consultation. Si vous hésitez, appelez-nous : "
            "nous vous aidons à trouver la bonne personne pour "
            "votre enfant.",
        "cta_primary_label":   "Appeler le cabinet",
        "cta_secondary_label": "Les quatre pédiatres",
    },

    # ─── VISITE (services) ───────────────────────────────────────
    "visite": {
        "eyebrow":  "Les consultations",
        "headline": "Huit types de consultations, <em>une seule manière</em> de faire de la pédiatrie.",
        "intro":
            "Chaque consultation au cabinet a une durée, un motif "
            "et un tarif clairs. Appelez-nous pour réserver : nous "
            "choisissons ensemble la consultation qui convient à "
            "l'âge et à la situation de votre enfant.",

        "visits": [
            {
                "icon":     "baby",
                "title":    "Bilan du nouveau-né",
                "duration": "45 min · 0 – 12 mois",
                "desc":
                    "La première évaluation complète après la "
                    "naissance : poids, longueur, réflexes "
                    "archaïques, dépistage des hanches, "
                    "accompagnement à l'allaitement et au "
                    "sommeil. Répétée aux 1er, 3e, 6e, 9e et "
                    "12e mois.",
                "bring_label": "À apporter",
                "bring":    "Carnet de santé, lettre de sortie de "
                            "la maternité, éventuels examens "
                            "néonataux.",
                "cta_label": "Réserver par téléphone",
            },
            {
                "icon":     "child",
                "title":    "Bilan de santé de l'enfant",
                "duration": "30 min · 1 – 10 ans",
                "desc":
                    "Suivi annuel de la croissance, évaluation "
                    "des autonomies, de la posture, de "
                    "l'alimentation et du développement "
                    "psychomoteur. C'est le bilan le plus "
                    "demandé au cabinet.",
                "bring_label": "À apporter",
                "bring":    "Carnet de santé à jour, un carnet "
                            "alimentaire d'une semaine si "
                            "possible.",
                "cta_label": "Réserver par téléphone",
            },
            {
                "icon":     "vaccine",
                "title":    "Vaccinations",
                "duration": "20 min · tous âges",
                "desc":
                    "Le calendrier vaccinal de la Région Piémont "
                    "réalisé au cabinet, sans file d'attente à "
                    "l'ASL. Possibilité d'espacer les doses et "
                    "d'établir un parcours personnalisé en cas "
                    "d'hésitation vaccinale.",
                "bring_label": "À apporter",
                "bring":    "Carnet de vaccination et pièce "
                            "d'identité du parent accompagnant.",
                "cta_label": "Réserver par téléphone",
            },
            {
                "icon":     "sport",
                "title":    "Certificat sportif",
                "duration": "30 min · 6 – 18 ans",
                "desc":
                    "Certificat médical non compétitif pour "
                    "l'école et les activités sportives de "
                    "loisir. Comprend un examen clinique, une "
                    "mesure de la tension artérielle et un ECG "
                    "de repos si indiqué.",
                "bring_label": "À apporter",
                "bring":    "Le formulaire de la société "
                            "sportive et le carnet de santé.",
                "cta_label": "Réserver par téléphone",
            },
            {
                "icon":     "moon",
                "title":    "Consultation sommeil",
                "duration": "45 min · 0 – 4 ans",
                "desc":
                    "Pour les parents épuisés et les enfants qui "
                    "ne dorment pas. Analyse du contexte "
                    "familial, plan de régulation du rythme "
                    "veille-sommeil et suivi téléphonique "
                    "hebdomadaire pendant un mois.",
                "bring_label": "À apporter",
                "bring":    "Un journal du sommeil de l'enfant "
                            "tenu sur sept jours.",
                "cta_label": "Réserver par téléphone",
            },
            {
                "icon":     "leaf",
                "title":    "Consultation allergologie",
                "duration": "45 min · 2 – 18 ans",
                "desc":
                    "Évaluation allergologique pédiatrique : "
                    "anamnèse clinique détaillée, tests "
                    "cutanés Prick, orientations sur l'asthme, "
                    "la dermatite atopique et les allergies "
                    "alimentaires. Assurée par le Dr. Greco.",
                "bring_label": "À apporter",
                "bring":    "Examens sanguins récents et "
                            "journal des symptômes.",
                "cta_label": "Réserver par téléphone",
            },
            {
                "icon":     "skin",
                "title":    "Dermatologie pédiatrique",
                "duration": "30 min · tous âges",
                "desc":
                    "Pour les dermatites, érythèmes, petites "
                    "lésions cutanées et grains de beauté en "
                    "croissance. Assurée par le Dr. Greco avec "
                    "un suivi photographique pour comparer "
                    "dans le temps.",
                "bring_label": "À apporter",
                "bring":    "Photographies datées de la lésion "
                            "si disponibles, liste des produits "
                            "utilisés.",
                "cta_label": "Réserver par téléphone",
            },
            {
                "icon":     "apple",
                "title":    "Consultation nutrition",
                "duration": "45 min · 6 mois – 18 ans",
                "desc":
                    "Pour une diversification difficile, de la "
                    "sélectivité alimentaire, un surpoids, un "
                    "sous-poids ou simplement un doute des "
                    "parents. Assurée par le Dr. Rambaldi avec "
                    "un plan écrit personnalisé.",
                "bring_label": "À apporter",
                "bring":    "Carnet alimentaire de sept jours "
                            "et courbes de croissance du "
                            "carnet de santé.",
                "cta_label": "Réserver par téléphone",
            },
        ],

        "tips_label":   "Trois conseils aux parents",
        "tips_heading": "Ce que nous aimerions que vous <em>sachiez</em> avant de nous appeler.",
        "tips_intro":
            "Certaines recommandations valent plus qu'une "
            "consultation. Nous les avons rassemblées ici parce que "
            "nous sommes convaincues qu'un parent informé est un "
            "parent plus serein — et un enfant plus serein.",

        "tips": [
            {
                "title": "La fièvre n'est pas l'ennemie",
                "text":
                    "La fièvre est un mécanisme de défense, pas "
                    "un problème à faire tomber à tout prix. "
                    "Inquiétez-vous plutôt du comportement de "
                    "votre enfant — s'il mange, s'il boit, s'il "
                    "joue — que du chiffre sur le thermomètre.",
            },
            {
                "title": "Cinq minutes suffisent",
                "text":
                    "Chaque soir, avant de dormir, demandez à "
                    "votre enfant comment s'est passée sa "
                    "journée. Pas à table, pas pendant que vous "
                    "cuisinez. Dans sa chambre, avec lui ou "
                    "elle. Cinq minutes changent tout.",
            },
            {
                "title": "Appelez sans crainte",
                "text":
                    "Aucune question n'est bête en pédiatrie. "
                    "Le cabinet répond au téléphone du lundi "
                    "au vendredi : appeler avant de "
                    "s'inquiéter est toujours la bonne "
                    "attitude.",
            },
        ],

        "cta_heading":
            "Pour prendre rendez-vous, le plus simple reste <em>de nous appeler</em>.",
        "cta_primary_label":   "Appeler le cabinet",
        "cta_secondary_label": "Écrire sur WhatsApp",
    },

    # ─── CRESCITA (faq) ──────────────────────────────────────────
    "crescita": {
        "eyebrow":  "Grandir & rassurer",
        "headline": "Les questions qui <em>accompagnent</em> les dix-huit premières années.",
        "intro":
            "Nous avons rassemblé ici les questions qui nous "
            "reviennent le plus souvent de la part des parents, "
            "regroupées par thème. C'est une première lecture : "
            "pour tout le reste, parlez-en avec votre pédiatre "
            "référente.",

        "topics": [
            {
                "icon":  "apple",
                "meta":  "Thème 01",
                "title": "Nutrition et alimentation",
                "intro":
                    "De la montée de lait à l'adolescence, "
                    "l'alimentation est le terrain où parents et "
                    "pédiatres dialoguent le plus. Quatre "
                    "questions que nous entendons chaque semaine.",
                "items": [
                    (
                        "À quel âge commencer la diversification ?",
                        "Les recommandations actuelles indiquent "
                        "la fin du sixième mois comme moment "
                        "optimal pour débuter, quand l'enfant "
                        "tient assis seul, a perdu le réflexe "
                        "d'extrusion et montre de l'intérêt "
                        "pour la nourriture des adultes. Il n'y "
                        "a pas de jour magique : on commence "
                        "quand l'enfant est prêt, pas quand le "
                        "calendrier le dit.",
                    ),
                    (
                        "Mon enfant est-il trop maigre ?",
                        "Le poids seul ne dit rien. Trois "
                        "valeurs doivent être lues ensemble : "
                        "poids, taille et IMC rapportés à la "
                        "courbe de croissance personnelle de "
                        "l'enfant. Un enfant qui grandit "
                        "régulièrement le long de son "
                        "percentile — même le dixième — va "
                        "parfaitement bien.",
                    ),
                    (
                        "Comment gérer un enfant difficile à table ?",
                        "La sélectivité alimentaire entre 2 et "
                        "5 ans est physiologique. Pas de "
                        "batailles à table, pas de chantage, "
                        "pas de plats spéciaux : on propose, "
                        "on repropose, on attend. Si, après "
                        "six ans, la sélectivité persiste sur "
                        "des groupes entiers d'aliments, "
                        "appelez le cabinet.",
                    ),
                    (
                        "Les compléments alimentaires sont-ils vraiment utiles ?",
                        "Dans l'immense majorité des cas, non. "
                        "Un enfant qui mange varié n'a pas "
                        "besoin de compléments, sauf la "
                        "vitamine D dans les premières années "
                        "et la vitamine K chez le nouveau-né. "
                        "Tout le reste est du marketing, pas "
                        "de la pédiatrie.",
                    ),
                ],
            },
            {
                "icon":  "moon",
                "meta":  "Thème 02",
                "title": "Sommeil et repos",
                "intro":
                    "Le sommeil est le sujet qui épuise le plus "
                    "les parents pendant les trois premières "
                    "années. Quatre réassurances fondées sur la "
                    "pratique clinique, pas sur les livres.",
                "items": [
                    (
                        "Combien d'heures un enfant doit-il dormir ?",
                        "De 0 à 3 mois : 14 à 17 heures par "
                        "jour, réparties. De 4 à 11 mois : 12 "
                        "à 15 heures. De 1 à 2 ans : 11 à 14 "
                        "heures. De 3 à 5 ans : 10 à 13 "
                        "heures. Chaque enfant a toutefois son "
                        "propre rythme : des variations de "
                        "deux heures sont normales.",
                    ),
                    (
                        "Est-il normal qu'il se réveille toutes les deux heures ?",
                        "Durant les six premiers mois, oui, "
                        "c'est physiologique : l'estomac du "
                        "nourrisson est petit et le rythme "
                        "circadien n'est pas encore mature. "
                        "Après six mois, si les réveils "
                        "fréquents persistent, nous pouvons "
                        "construire ensemble un plan de "
                        "régulation.",
                    ),
                    (
                        "Puis-je endormir mon bébé à côté de moi ?",
                        "Le co-sommeil dans la même chambre "
                        "(mais pas dans le même lit) est "
                        "recommandé jusqu'à 12 mois. Après, "
                        "cela dépend des habitudes familiales : "
                        "aucune approche n'est mauvaise si "
                        "elle fonctionne pour les parents et "
                        "l'enfant.",
                    ),
                    (
                        "Quand retirer la couche de nuit ?",
                        "Le contrôle sphinctérien nocturne "
                        "arrive en moyenne entre 3 et 5 ans. "
                        "Ce n'est pas une course : certains "
                        "enfants sont prêts à deux ans et "
                        "demi, d'autres à six. Si à 7 ans "
                        "l'énurésie reste fréquente, "
                        "parlons-en.",
                    ),
                ],
            },
            {
                "icon":  "vaccine",
                "meta":  "Thème 03",
                "title": "Vaccinations et maladies courantes",
                "intro":
                    "Le paysage vaccinal italien a changé en "
                    "2017 avec le décret Lorenzin. Nous répondons "
                    "ici aux quatre questions les plus "
                    "fréquentes — avec patience, et avec les "
                    "données.",
                "items": [
                    (
                        "Quelles vaccinations sont obligatoires ?",
                        "Dix : diphtérie, tétanos, coqueluche, "
                        "hépatite B, poliomyélite, Hib, "
                        "rougeole, rubéole, oreillons et "
                        "varicelle. L'obligation concerne "
                        "l'inscription à la scolarité "
                        "obligatoire (0-16 ans) et est "
                        "encadrée par le décret Lorenzin de "
                        "2017.",
                    ),
                    (
                        "Puis-je espacer les doses ?",
                        "Oui. Le cabinet propose des parcours "
                        "personnalisés pour les familles qui "
                        "préfèrent répartir les vaccinations "
                        "sur plusieurs rendez-vous au lieu de "
                        "faire trois vaccins en une seule "
                        "séance. Nous en parlons ensemble au "
                        "premier bilan.",
                    ),
                    (
                        "Comment gérer la roséole ?",
                        "La roséole (roseola infantum) touche "
                        "les enfants entre 6 mois et 2 ans : "
                        "trois jours de fièvre élevée "
                        "soudaine suivis d'une éruption "
                        "cutanée rose. On la gère avec des "
                        "antipyrétiques et de la patience. "
                        "Appelez-nous uniquement si la "
                        "fièvre dépasse 40 °C ou dure plus "
                        "de quatre jours.",
                    ),
                    (
                        "Dois-je m'inquiéter d'une toux persistante ?",
                        "Une toux pendant trois semaines "
                        "après un rhume est normale : les "
                        "voies aériennes de l'enfant sont "
                        "plus réactives. Appelez-nous si la "
                        "toux s'accompagne d'une fièvre qui "
                        "ne tombe pas en cinq jours, d'une "
                        "respiration sifflante ou de tirages "
                        "intercostaux visibles.",
                    ),
                ],
            },
            {
                "icon":  "comp",
                "meta":  "Thème 04",
                "title": "Comportement et développement",
                "intro":
                    "Les questions les moins médicales sont "
                    "souvent les plus importantes. Nous "
                    "répondons ici sur le développement "
                    "psychomoteur, les colères, l'adolescence.",
                "items": [
                    (
                        "À quel âge un enfant parle-t-il ?",
                        "Les premiers mots arrivent entre 10 "
                        "et 18 mois, les premières phrases "
                        "entre 18 et 24 mois. Si à 24 mois "
                        "l'enfant n'associe pas deux mots, "
                        "il est raisonnable de demander un "
                        "bilan psychomoteur — que nous "
                        "réalisons au cabinet avec Giada "
                        "Porro.",
                    ),
                    (
                        "Les colères sont-elles normales ?",
                        "Oui, elles sont physiologiques et "
                        "essentielles : c'est la manière "
                        "dont l'enfant explore l'autonomie "
                        "et les limites. On ne les punit "
                        "pas, on les contient. Elles "
                        "deviennent un problème lorsqu'elles "
                        "s'accompagnent régulièrement "
                        "d'agressivité physique ou "
                        "d'automutilation.",
                    ),
                    (
                        "Combien de temps devant les écrans ?",
                        "Les recommandations de l'OMS "
                        "indiquent : pas d'écran avant 2 "
                        "ans, maximum 1 heure par jour entre "
                        "2 et 5 ans, maximum 2 heures après "
                        "5 ans. Télévision, tablette et "
                        "smartphone sont tous des écrans : "
                        "comptez aussi le dessin animé du "
                        "matin.",
                    ),
                    (
                        "Comment parler à mon adolescent ?",
                        "Moins que vous ne le voudriez, et "
                        "avec plus d'écoute que vous ne le "
                        "croyez. Les questions ouvertes "
                        "fonctionnent toujours mieux que les "
                        "questions fermées : « Comment "
                        "s'est passée ta journée ? » l'emporte "
                        "sur « As-tu fait tes devoirs ? » "
                        "dix à zéro. Et souvenez-vous : le "
                        "silence n'est pas un refus, c'est "
                        "une réflexion.",
                    ),
                ],
            },
        ],

        "materials_label":   "Documents utiles",
        "materials_heading": "Trois guides <em>à télécharger</em>.",
        "materials_intro":
            "Nous avons préparé trois vademecum en PDF que les "
            "parents peuvent télécharger et consulter à la "
            "maison. Ils sont rédigés par les pédiatres du "
            "cabinet et mis à jour en 2026.",

        "materials": [
            {
                "title":    "Vademecum du nouveau-né",
                "desc":
                    "Vingt-huit pages sur les trois premiers "
                    "mois de vie : allaitement, sommeil, "
                    "bain, premières vaccinations, quand "
                    "appeler le cabinet.",
                "size":     "PDF · 2,4 Mo",
                "dl_label": "Télécharger",
            },
            {
                "title":    "Calendrier vaccinal 2026",
                "desc":
                    "Le calendrier vaccinal à jour de la "
                    "Région Piémont en version résumée, "
                    "avec dates recommandées et "
                    "facultatives.",
                "size":     "PDF · 1,1 Mo",
                "dl_label": "Télécharger",
            },
            {
                "title":    "Guide de la diversification",
                "desc":
                    "Du sixième mois au premier "
                    "anniversaire : quels aliments "
                    "introduire, dans quel ordre, avec "
                    "quelles précautions. Avec des recettes "
                    "du Dr. Rambaldi.",
                "size":     "PDF · 3,1 Mo",
                "dl_label": "Télécharger",
            },
        ],

        "cta_heading":
            "Vous n'avez pas trouvé <em>votre</em> question ?",
        "cta_lead":
            "Appelez-nous ou écrivez-nous sur WhatsApp : nous "
            "répondons en personne dans la journée. Aucune "
            "question n'est bête en pédiatrie.",
        "cta_primary_label":   "Appeler le cabinet",
        "cta_secondary_label": "Écrire sur WhatsApp",
    },

    # ─── PEDIATRE (team) ─────────────────────────────────────────
    "pediatre": {
        "eyebrow":  "Les pédiatres",
        "headline": "Quatre signatures, <em>un seul dossier</em> de famille.",
        "intro":
            "Nous sommes quatre pédiatres aux formations "
            "différentes et à la même manière de travailler : "
            "trente minutes par consultation, dossiers partagés "
            "entre consœurs, continuité de la relation avec "
            "chaque enfant de la naissance à dix-huit ans.",

        "doctors": [
            {
                "name":  "Dr.ssa Elisa Rambaldi",
                "role":  "Fondatrice · Pédiatre de famille",
                "tag":   "Fondatrice",
                "specs": ["Nutrition infantile", "Diversification", "Âge scolaire"],
                "bio":
                    "Diplôme de médecine à l'Université de Turin, "
                    "spécialisation en pédiatrie à l'hôpital des "
                    "enfants Regina Margherita. Ouvre le cabinet "
                    "en 1998 avec l'objectif de rendre à la "
                    "pédiatrie de ville sa dimension de temps "
                    "long. Auteure de « Crescere insieme » "
                    "(Grandir ensemble), Einaudi Ragazzi, 2019.",
                "exp_label": "Expérience",
                "exp_value": "28 ans · plus de 3 000 dossiers actifs",
                "wa_label":  "Écrire sur WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Marta Greco",
                "role":  "Pédiatre · Allergologie et dermatologie",
                "tag":   "Allergologie",
                "specs": ["Asthme pédiatrique", "Dermatite atopique", "Allergies alimentaires"],
                "bio":
                    "Diplôme et spécialisation en pédiatrie à "
                    "l'Université de Pavie, master en Allergologie "
                    "pédiatrique au San Raffaele de Milan. Au "
                    "cabinet Crocetta depuis 2008, elle y dirige "
                    "le parcours allergologique et dermatologique "
                    "pédiatrique. Référente pour l'Institut "
                    "Gaslini de Gênes sur les consultations de "
                    "ville.",
                "exp_label": "Expérience",
                "exp_value": "22 ans · allergologie pédiatrique depuis 2006",
                "wa_label":  "Écrire sur WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Lucia Sferra",
                "role":  "Pédiatre · Endocrinologie",
                "tag":   "Endocrinologie",
                "specs": ["Croissance", "Puberté précoce", "Thyroïde pédiatrique"],
                "bio":
                    "Diplôme à l'Université Federico II de "
                    "Naples, spécialisation en pédiatrie à "
                    "l'Université de Bologne, fellowship en "
                    "endocrinologie pédiatrique au Boston "
                    "Children's Hospital. Au cabinet depuis "
                    "2016, elle y suit la croissance, la "
                    "puberté et les troubles endocriniens de "
                    "la tranche 8-18 ans.",
                "exp_label": "Expérience",
                "exp_value": "18 ans · endocrinologie pédiatrique",
                "wa_label":  "Écrire sur WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Beatrice Conti",
                "role":  "Pédiatre · Néonatologie",
                "tag":   "Néonatologie",
                "specs": ["Allaitement", "Sommeil 0-3 ans", "Prématurité"],
                "bio":
                    "Diplôme et spécialisation à l'Université de "
                    "Turin, quinze ans au service de "
                    "néonatologie de Sant'Anna, où elle a suivi "
                    "plus de deux mille nouveau-nés prématurés "
                    "et à terme. Consultante IBCLC en "
                    "allaitement. Rejoint le cabinet en 2026 "
                    "pour s'occuper de la première année de "
                    "vie et accompagner les nouvelles mères.",
                "exp_label": "Expérience",
                "exp_value": "15 ans · Sant'Anna · IBCLC depuis 2014",
                "wa_label":  "Écrire sur WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
        ],

        "extra_title": "L'équipe clinique est complétée par deux professionnelles.",
        "extra_text":
            "Luisa Ferraro, infirmière pédiatrique avec quinze "
            "ans de service à l'hôpital des enfants Regina "
            "Margherita, assure les vaccinations et les prises "
            "de sang au cabinet. Giada Porro, psychomotricienne "
            "spécialisée dans les troubles du développement "
            "0-6 ans, reçoit les mardis et jeudis sur "
            "rendez-vous.",
    },

    # ─── CONTATTI (contact) ──────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contact & accès",
        "headline": "Un <em>numéro</em>, une personne, une réponse.",
        "intro":
            "Silvia Pairetto répond personnellement au téléphone "
            "du lundi au vendredi. Elle connaît chaque dossier, "
            "chaque prénom et chaque maman de ce cabinet. Pour "
            "les demandes non urgentes, WhatsApp et le formulaire "
            "ci-dessous sont également à votre disposition.",

        "address_label": "Où nous sommes",
        "address_line":  "Corso Galileo Ferraris 140",
        "address_sub":   "10129 Turin · Quartier Crocetta · rez-de-chaussée surélevé",
        "phone_label":   "Téléphone",
        "email_label":   "E-mail",

        "map_image":
            "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
            "?auto=compress&cs=tinysrgb&w=1000&h=750&fit=crop",

        "travel_heading": "Comment nous rejoindre",
        "travel": [
            {
                "icon":  "metro",
                "title": "Métro",
                "text":  "Ligne 1 · station Re Umberto, 4 minutes à pied vers Corso Galileo Ferraris.",
            },
            {
                "icon":  "car",
                "title": "Voiture et stationnement",
                "text":  "Parking partenaire Q-Park Crocetta au 22 Via Governolo, à 80 mètres du cabinet.",
            },
            {
                "icon":  "walk",
                "title": "À pied",
                "text":  "À cinq minutes du Parc du Valentino et à 15 minutes de la gare Porta Nuova.",
            },
        ],

        "hours_heading": "Horaires d'ouverture",
        "hours": [
            ("Lun – Ven",  "8:30 – 12:30 · 15:00 – 19:00"),
            ("Samedi",     "9:00 – 12:00 · urgences uniquement"),
            ("Dimanche",   "Astreinte téléphonique"),
            ("Jours fériés", "Ligne dédiée"),
        ],

        "form_title": "Écrire au cabinet",
        "form_intro":
            "Pour les demandes non urgentes — tarifs, horaires, "
            "documents, première consultation — écrivez-nous "
            "ici. Nous répondons dans la journée ouvrée. Pour "
            "les urgences, appelez.",

        "label_parent_name": "Prénom et nom du parent",
        "label_child_age":   "Âge de l'enfant",
        "label_reason":      "Motif du contact",

        "reason_options": [
            "Première consultation",
            "Contrôle de routine",
            "Vaccinations",
            "Conseil sur un problème précis",
            "Informations administratives",
            "Autre",
        ],

        "form_placeholders": {
            "parent_name": "Giulia Bianchi",
            "email":       "giulia.bianchi@email.it",
            "phone":       "+39 333 …",
            "child_age":   "4 ans et demi",
            "message":
                "Écrivez votre demande ici. "
                "Nous répondons dans la journée ouvrée.",
        },
        "form_helpers": {
            "parent_name": "Indiquez le prénom et nom du parent qui écrit.",
            "email":       "Nous répondons ici dans la journée.",
            "phone":       "Optionnel — utile si vous préférez être rappelé.",
            "child_age":   "Âge et, si vous le souhaitez, prénom de l'enfant.",
            "reason":      "En cas d'hésitation, choisissez « Autre ».",
            "message":
                "Quelques lignes suffisent — pour le reste, "
                "le téléphone est plus efficace.",
        },
        "form_consent":
            "J'accepte le traitement de mes données personnelles "
            "conformément à la notice d'information du cabinet au "
            "titre du Règlement UE 679/2016 (RGPD). Les données "
            "des enfants sont conservées par le cabinet et ne "
            "sont jamais communiquées à des tiers.",
        "form_submit_note":
            "Réponse dans la journée ouvrée · pour les "
            "urgences, appelez directement le cabinet.",
    },
}
__all__ = ["FAMIGLIA_CONTENT_FR"]
