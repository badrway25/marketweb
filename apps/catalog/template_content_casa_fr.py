"""Phase 2g3.7 · Session 53 · Casa — FR native-voice tree. Warm residential-agency voice."""
from __future__ import annotations

from typing import Any


CASA_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",        "label": "Accueil",       "kind": "home"},
        {"slug": "immobili",    "label": "Biens",         "kind": "project_list"},
        {"slug": "quartieri",   "label": "Quartiers",     "kind": "about"},
        {"slug": "agenzia",     "label": "L'Agence",      "kind": "team"},
        {"slug": "valutazione", "label": "Estimation",    "kind": "services"},
        {"slug": "contatti",    "label": "Contact",       "kind": "contact"},
    ],

    "site": {
        "logo_initial":  "D",
        "logo_word":     "Domus Immobiliare",
        "tag":           "Milan · Turin · depuis 2005",
        "phone":         "+39 02 8765 4321",
        "phone_tel":     "+390287654321",
        "phone_label":   "Appelez-nous",
        "email":         "bonjour@domusimmobiliare.it",
        "address":       "Corso Buenos Aires 15 · 20124 Milan",
        "address_short": "Milan · Turin",
        "hours_compact": "Lun – Sam · 09h00 – 19h30",
        "hours_footer_rows": [
            "Visites guidées aussi le dimanche",
            "WhatsApp toujours ouvert",
        ],
        "whatsapp":      "02 8765 4321",
        "whatsapp_link": "https://wa.me/390287654321",
        "whatsapp_note": "Nous répondons sous 20 minutes aux heures d'ouverture",
        "license":       "Licence d'agence immobilière RIEA MI 1422 · TVA 05431920968",
        "nav_cta":       "Réserver une visite",
        "nav_cta_href":  "contatti",
        "footer_intro":
            "Domus Immobiliare — chaque bien que nous proposons est choisi "
            "à la main. Vingt ans entre Milan, Turin, le lac de Côme et le "
            "Piémont, un seul agent dédié du premier rendez-vous jusqu'à "
            "la signature chez le notaire.",
        "foot_studio":   "L'agence",
        "foot_pages":    "Pages",
        "foot_contact":  "Contact",
        "foot_offices":  "Bureaux",
        "offices_footer_rows": [
            "Milan · Buenos Aires 15",
            "Turin · Crocetta 8",
        ],
        "tile_rooms_label":    "Chambres",
        "tile_surface_label":  "Surface",
        "tile_bathrooms_label":"SdB",
        "tile_surface_unit":   "m²",
        "tile_visit_cta":      "Réserver visite",
        "tile_reference_label":"Réf.",
        "surface_short":       "m²",
        "price_label":         "Prix",
        "energy_class_label":  "Classe énergie",
        "floor_label":         "Étage",
        "parking_label":       "Parking",
        "elevator_label":      "Ascenseur",
        "filter_label":        "Filtrer par",
        "sort_label":           "Trier par",
        "visit_request_label": "Réserver une visite",
        "viewings_unit":       "visites cette semaine",
        "showings_schedule":   "Visites tous les jours, samedi et dimanche inclus",
    },

    "home": {
        "eyebrow":  "Domus Immobiliare · Milan · Turin · Lombardie & Piémont",
        "headline": "Six cents biens choisis à la main, <em>un seul agent</em> de la visite à l'acte.",
        "intro":
            "Plus de 600 biens sélectionnés à la main entre Milan, Turin, "
            "le lac de Côme et le Piémont. Visites guidées le dimanche "
            "aussi, estimation gratuite sous 24 heures, et un seul agent "
            "qui vous accompagne du premier rendez-vous jusqu'au notaire.",
        "primary_cta":   "Chercher un bien",
        "primary_href":  "immobili",
        "secondary_cta": "Estimation gratuite",
        "secondary_href":"valutazione",
        "hero_availability": "20 nouvelles offres cette semaine",
        "hero_response":     "Nous vous rappelons sous 20 minutes",

        "search_widget": {
            "label":          "Que cherchez-vous aujourd'hui ?",
            "intro":          "Dites-nous la maison et le quartier, on s'occupe du reste.",
            "location_label": "Où",
            "location_value": "Milan, centre",
            "type_label":     "Type de bien",
            "type_value":     "Appartement",
            "price_label":    "Prix",
            "price_value":    "500 K € — 1,2 M €",
            "rooms_label":    "Chambres",
            "rooms_value":    "3+ chambres",
            "cta":            "Chercher un bien",
            "cta_href":       "immobili",
            "secondary_note": "Ou dites-nous sur WhatsApp ce que vous cherchez",
            "popular_label":  "Les plus recherchés",
            "popular_tags": [
                "Appartements à Brera",
                "Villas à Cernobbio",
                "Lofts aux Navigli",
                "Trois-pièces à Turin",
                "Maisons avec jardin",
            ],
        },

        "featured_label":   "À la une cette semaine",
        "featured_heading": "Les biens <em>qui vous attendent</em>.",
        "featured_intro":
            "Une sélection resserrée parmi les visites que nous avons "
            "faites ces dix derniers jours. Chaque fiche est contrôlée "
            "personnellement par un agent, chaque photo est prise "
            "pendant la visite.",
        "featured_link":    "Voir les 600+ biens",
        "featured_link_href":"immobili",
        "featured_listings": [
            ("1 250 000 €", "Penthouse panoramique avec terrasse",      "Milano · Brera",      "4", "180", "2", "Exclusivité", "MI-1842"),
            ("890 000 €",   "Villa moderne avec jardin",                "Como · Cernobbio",    "5", "240", "3", "Nouveau",     "CO-0217"),
            ("650 000 €",   "Loft de design dans le quartier Tortona",  "Milano · Navigli",    "2", "120", "2", "Rénové",      "MI-1788"),
            ("420 000 €",   "Trois-pièces lumineux avec balcon",         "Torino · Crocetta",   "3",  "95", "1", "Disponible",  "TO-0904"),
        ],

        "neighborhoods_label":   "Quartiers",
        "neighborhoods_heading": "Là où <em>nous trouvons votre maison</em>.",
        "neighborhoods_intro":
            "Milan, Turin, le lac. Chaque quartier est couvert par un "
            "agent qui y vit — on connaît les gardiens, les cafés, les "
            "écoles, le meilleur arrêt pour aller au centre.",
        "neighborhoods": [
            ("Brera",     "Milano · historique",   "124 biens", "dès 850 K €"),
            ("Navigli",   "Milano · design",       "89 biens",  "dès 520 K €"),
            ("Isola",     "Milano · contemporain", "71 biens",  "dès 480 K €"),
            ("Cernobbio", "Como · bord du lac",    "42 biens",  "dès 680 K €"),
            ("Crocetta",  "Torino · résidentiel",  "67 biens",  "dès 380 K €"),
            ("Borgo Po",  "Torino · collines",     "38 biens",  "dès 410 K €"),
        ],
        "neighborhoods_cta":      "Explorer tous les quartiers",
        "neighborhoods_cta_href": "quartieri",

        "stats_label":   "Vingt ans sur le marché",
        "stats_heading": "Nos chiffres, en toute clarté.",
        "stats_intro":
            "Ce qui compte n'est pas le nombre de biens en vitrine, mais "
            "combien nous en avons réellement vendus. Voici les chiffres "
            "depuis 2005.",
        "stats": [
            ("600",   "+", "biens en portefeuille"),
            ("2 800", "+", "maisons trouvées depuis 2005"),
            ("20",    "",  "années d'expérience"),
            ("4,8",   " ★","sur 420 avis Google"),
        ],
        "stats_note": "Données actualisées mars 2026 · vérifiables sur immobiliare.it",

        "agents_label":   "Ceux qui vous accompagnent",
        "agents_heading": "Un seul agent, <em>du début à la fin</em>.",
        "agents_intro":
            "Pas de standard, pas de conseillers qui tournent. Du premier "
            "rendez-vous au notaire vous parlez toujours à la même "
            "personne — celle qui connaît le quartier, l'immeuble, "
            "souvent même le voisin de palier.",
        "agents_preview": [
            ("Giulia Ferrante", "Agent senior",        "Milano · Brera & Centre",  "15 ans"),
            ("Marco Lentini",   "Agent senior",        "Milano · Navigli & Sud",   "12 ans"),
            ("Silvia Mondelli", "Responsable",         "Torino · Crocetta",        "10 ans"),
            ("Andrea Colombo",  "Agent senior",        "Como · bord du lac",       "18 ans"),
        ],
        "agents_cta":      "Découvrir toute l'équipe",
        "agents_cta_href": "agenzia",

        "valuation_label":   "Estimation gratuite",
        "valuation_heading": "Combien vaut <em>votre bien</em> ?",
        "valuation_intro":
            "Nous vous rappelons sous 24 heures avec une estimation "
            "honnête, basée sur la comparaison de toutes les ventes "
            "enregistrées ces douze derniers mois dans votre îlot. "
            "Aucun engagement, zéro coût, même si vous décidez ensuite "
            "de vendre avec une autre agence.",
        "valuation_cta":       "Demander une estimation",
        "valuation_cta_href":  "valutazione",
        "valuation_secondary": "Voir comment ça marche",
        "valuation_secondary_href":"valutazione",
        "valuation_proof": [
            ("24 h",   "délai de réponse"),
            ("0 €",    "coût, toujours"),
            ("420+",   "estimations en 2025"),
        ],

        "testimonial_label":  "Ils ont acheté avec nous",
        "testimonial_quote":
            "Ils ont compris en dix minutes ce que nous cherchions. Trois "
            "visites, la quatrième c'était chez nous. Giulia nous a même "
            "accompagnés chez le notaire — et nous n'avions jamais acheté "
            "de logement avant.",
        "testimonial_author": "Francesca & Tommaso Ranieri",
        "testimonial_meta":   "Trois-pièces · Brera · acquis en mars 2026",
    },

    "quartieri": {
        "eyebrow":  "Guide des quartiers · Milan · Turin · Côme",
        "headline": "Les quartiers <em>que nous connaissons</em> le mieux.",
        "intro":
            "Chaque quartier ci-dessous est couvert par un de nos agents "
            "qui y vit. Vous y trouverez les prix moyens, la disponibilité "
            "actuelle, les surfaces types et la signature de la personne "
            "qui y travaille tous les jours.",

        "guides_label": "Guide des quartiers",
        "guides_heading": "Choisissez le quartier, <em>nous connaissons le chemin</em>.",
        "guides": [
            (
                "Brera", "Milano · historique & culturel",
                "9 200 € / m²", "124 biens disponibles",
                "M2 Lanza · M3 Montenapoleone", "Parco Sempione à 6 min", "Luxe historique",
                "Le cœur historique de Milan : palais du XIXᵉ siècle, cours "
                "intérieures, ateliers et un tissu de boutiques uniques que "
                "l'on ne trouve nulle part ailleurs. Beaucoup d'interventions "
                "de restauration conservative, peu de nouveaux chantiers. "
                "Idéal pour qui cherche un découpage classique avec une "
                "plus-value consolidée.",
                "Giulia Ferrante · agent résidente depuis 2008",
            ),
            (
                "Navigli", "Milano · design & vie nocturne",
                "7 100 € / m²", "89 biens disponibles",
                "M2 Porta Genova · Tram 3/9", "Darsena · Ticinese à pied", "Créatif & jeune",
                "L'axe des deux canaux : lofts industriels, maisons "
                "d'époque sur balcons extérieurs, studios d'architecture. "
                "Dynamique, international, animé le soir. Parfait pour un "
                "investissement court-moyen terme ou un premier achat jeune.",
                "Marco Lentini · agent senior",
            ),
            (
                "Porta Nuova", "Milano · nouveau skyline",
                "10 400 € / m²", "56 biens disponibles",
                "M2 Gioia · M3 Repubblica", "BAM Bibliothèque des Arbres", "Contemporain & affaires",
                "Le quartier de la Milan du nouveau millénaire : gratte-"
                "ciel, finance, résidences signature comme le Bosco "
                "Verticale et Solaria. Pour qui cherche des services "
                "premium, le concierge, des solutions smart-home intégrées.",
                "Giulia Ferrante · agent résidente",
            ),
            (
                "Isola", "Milano · contemporain créatif",
                "7 600 € / m²", "71 biens disponibles",
                "M5 Isola · Tram 2/4", "BAM à 5 min · Parco Lambro en 10", "Créatif & résidentiel",
                "Ancien quartier ouvrier renaît aujourd'hui autour de "
                "Porta Nuova. Maisons à balcons restaurées côtoyant les "
                "nouvelles résidences. Atmosphère milanaise authentique, "
                "marché en croissance stable depuis dix ans.",
                "Sofia Ranieri · agent junior · Milan Nord",
            ),
            (
                "Cernobbio", "Como · lac & villas",
                "5 900 € / m²", "42 biens disponibles",
                "Train Cadorna-Como · 48 min", "Lac à pied · Parc Villa Erba", "Lac & résidences secondaires",
                "La rive occidentale du Lario : villas d'époque avec accès "
                "au lac, appartements dans des immeubles historiques face "
                "au golfe, penthouses panoramiques. Clientèle internationale, "
                "anglais et allemand courants à l'agence.",
                "Andrea Colombo · agent senior lac",
            ),
            (
                "Bellagio", "Como · perle du lac",
                "6 400 € / m²", "29 biens disponibles",
                "Bateau Como-Bellagio · voiture", "Centre historique piéton", "Exclusif & international",
                "La pointe du triangle du lac : centre historique médiéval, "
                "villas sur la Punta Spartivento, résidences panoramiques à "
                "double vue. Marché de niche, disponibilité toujours limitée.",
                "Andrea Colombo · lac de Côme",
            ),
            (
                "Crocetta", "Torino · résidentiel élégant",
                "3 900 € / m²", "67 biens disponibles",
                "M1 Re Umberto · Tram 4/10", "Parco del Valentino · 12 min", "Bourgeois & familles",
                "Le bon quartier de Turin : palais des années 30, cours "
                "silencieuses, écoles historiques, marché couvert. "
                "Grandes surfaces, qualité de vie élevée, prix encore "
                "accessibles par rapport à Milan. Recommandé aux familles.",
                "Silvia Mondelli · responsable Turin",
            ),
            (
                "Borgo Po", "Torino · collines & panoramique",
                "4 200 € / m²", "38 biens disponibles",
                "Tram 13/15 · Gran Madre", "Collines · Monte dei Cappuccini", "Romantique & vue",
                "La rive droite du Pô : petits palais Liberty, villas sur "
                "la colline, penthouses avec vue sur les Alpes. Tissu de "
                "bistros et lieux historiques. Pour qui cherche l'air "
                "libre et le panorama à dix minutes du centre.",
                "Silvia Mondelli · Turin collines & centre",
            ),
        ],

        "faq_label":   "Questions fréquentes sur les quartiers",
        "faq_heading": "Ce que vous nous demandez le plus souvent.",
        "faq": [
            (
                "Quel est le meilleur quartier pour une famille qui s'installe à Milan ?",
                "Pour les familles nous recommandons Crocetta à Turin, "
                "Isola et Porta Nuova à Milan. Écoles à proximité, parcs "
                "accessibles à pied, métro à deux pas. Si vous préférez "
                "la colline, Borgo Po à Turin est le bon choix.",
            ),
            (
                "Centre historique ou quartier émergent comme investissement ?",
                "Cela dépend de votre horizon. Centre historique = plus-"
                "value consolidée, croissance 2-3 % par an. Les quartiers "
                "émergents comme Isola ont pris +48 % en dix ans, mais "
                "le risque est plus élevé. Parlons-en lors d'un appel de "
                "quinze minutes.",
            ),
            (
                "Vous faites aussi de la location ou seulement de la vente ?",
                "Principalement de la vente. Nous gérons la location "
                "uniquement pour des biens confiés par un vendeur qui "
                "souhaite louer entre-temps. Pour une location pure nous "
                "vous indiquons le bon confrère.",
            ),
            (
                "Comment se déroule une visite sur le lac de Côme si je vis à Milan ?",
                "Le samedi matin nous organisons une navette depuis Milan "
                "Cadorna : trois biens visités dans la journée, déjeuner "
                "offert, retour pour 18 h. Vous voyez tout sans louer "
                "de voiture.",
            ),
        ],

        "cta_label":   "Parlez à l'agent de votre quartier",
        "cta_heading": "Un café, vingt minutes, tout devient clair.",
        "cta_intro":
            "Choisissez un quartier et nous vous mettons en contact avec "
            "l'agent qui y travaille tous les jours. Premier rendez-vous "
            "gratuit, à l'agence ou sur place.",
        "cta_primary":       "Réserver une visite",
        "cta_primary_href":  "contatti",
        "cta_secondary":     "Estimation gratuite",
        "cta_secondary_href":"valutazione",
    },

    "agenzia": {
        "eyebrow":  "L'équipe · 14 personnes · Milan & Turin",
        "headline": "Les agents qui vous accompagnent <em>du rendez-vous au notaire</em>.",
        "intro":
            "Neuf agents inscrits à l'ordre, deux coordinateurs, trois "
            "personnes au back-office notarial. Chaque zone a son agent "
            "résident, chaque dossier sa fiche technique, chaque client "
            "un seul numéro à appeler.",

        "book_cta":       "Réserver une visite",
        "agents_heading": "L'équipe au complet.",
        "agents_intro":
            "À l'agence nous travaillons en binôme : un senior suit le "
            "bien, un junior les familles qui cherchent. Vous avez ainsi "
            "des réponses aussi le soir et le samedi.",

        "agents": [
            {
                "name": "Giulia Ferrante",
                "role": "Associée · Responsable Milan Centre",
                "area": "Milano · Brera, Quadrilatero, Porta Nuova",
                "years": "15 ans",
                "languages": "Italien · Anglais · Français",
                "speciality": "Palais historiques, étages élevés, piano "
                              "nobile. Accompagnement complet de la visite au notaire.",
                "phone": "+39 02 8765 4322",
                "whatsapp_href": "https://wa.me/390287654322",
                "email": "giulia@domusimmobiliare.it",
                "quote": "La bonne maison existe : le travail est "
                         "d'écouter assez longtemps pour la reconnaître à la première visite.",
            },
            {
                "name": "Marco Lentini",
                "role": "Agent senior · Milan Sud",
                "area": "Milano · Navigli, Tortona, Bocconi",
                "years": "12 ans",
                "languages": "Italien · Anglais",
                "speciality": "Lofts industriels, maisons à balcons "
                              "extérieurs, interventions de design. Contacts avec les studios d'architecture locaux.",
                "phone": "+39 02 8765 4323",
                "whatsapp_href": "https://wa.me/390287654323",
                "email": "marco@domusimmobiliare.it",
                "quote": "Sur les Navigli la valeur n'est pas le mètre "
                         "carré : c'est la cour, la lumière, le silence entre deux canaux.",
            },
            {
                "name": "Silvia Mondelli",
                "role": "Responsable Turin",
                "area": "Torino · Crocetta, Cit Turin, Centre",
                "years": "10 ans",
                "languages": "Italien · Anglais · Espagnol",
                "speciality": "Familles en mutation, premiers achats, "
                              "accompagnement fiscal pour qui rentre de l'étranger.",
                "phone": "+39 011 5328 4401",
                "whatsapp_href": "https://wa.me/390115328440",
                "email": "silvia@domusimmobiliare.it",
                "quote": "Turin offre aujourd'hui ce que Milan offrait "
                         "il y a vingt ans : grandes surfaces, prix justes, qualité de vie.",
            },
            {
                "name": "Andrea Colombo",
                "role": "Agent senior · Lac de Côme",
                "area": "Como · Cernobbio, Bellagio, Tremezzo",
                "years": "18 ans",
                "languages": "Italien · Anglais · Allemand",
                "speciality": "Villas d'époque, résidences secondaires "
                              "pour clientèle internationale, gestion saisonnière après-vente.",
                "phone": "+39 031 2345 6789",
                "whatsapp_href": "https://wa.me/390312345678",
                "email": "andrea@domusimmobiliare.it",
                "quote": "Sur le lac chaque villa a cent ans d'histoire. "
                         "Mon travail est de ramener le notaire à trois mois.",
            },
            {
                "name": "Sofia Ranieri",
                "role": "Agent · Milan Nord",
                "area": "Milano · Isola, Porta Nuova, Dergano",
                "years": "6 ans",
                "languages": "Italien · Anglais",
                "speciality": "Constructions neuves, haute classe "
                              "énergétique, premiers achats pour cadres de 30 à 40 ans.",
                "phone": "+39 02 8765 4324",
                "whatsapp_href": "https://wa.me/390287654324",
                "email": "sofia@domusimmobiliare.it",
                "quote": "L'Isola d'aujourd'hui n'est plus celle d'il y a "
                         "dix ans. Plus facile à vivre, plus difficile à lire côté valeur.",
            },
            {
                "name": "Luca Benedetti",
                "role": "Agent · Turin Collines",
                "area": "Torino · Borgo Po, Gran Madre, Maddalena",
                "years": "9 ans",
                "languages": "Italien · Français",
                "speciality": "Villas Liberty, penthouses avec vue sur "
                              "les Alpes, grosses rénovations avec marché technique.",
                "phone": "+39 011 5328 4402",
                "whatsapp_href": "https://wa.me/390115328441",
                "email": "luca@domusimmobiliare.it",
                "quote": "La colline de Turin c'est de la poésie urbaine : "
                         "dix minutes du centre et les Alpes devant soi chaque matin.",
            },
            {
                "name": "Chiara Sestri",
                "role": "Agent junior · Milan Centre",
                "area": "Milano · Brera, Magenta, Cadorna",
                "years": "3 ans",
                "languages": "Italien · Anglais · Français · Arabe",
                "speciality": "Accompagnement linguistique de la clientèle "
                              "internationale, démarches code fiscal, première approche du marché italien.",
                "phone": "+39 02 8765 4325",
                "whatsapp_href": "https://wa.me/390287654325",
                "email": "chiara@domusimmobiliare.it",
                "quote": "Qui achète à Milan depuis l'étranger a besoin "
                         "d'être accompagné, pas seulement servi.",
            },
            {
                "name": "Davide Orsini",
                "role": "Agent · Monza & Brianza",
                "area": "Monza · Seregno · Desio",
                "years": "11 ans",
                "languages": "Italien · Anglais",
                "speciality": "Maisons indépendantes avec jardin, villas "
                              "uniques, marché résidentiel pour familles qui quittent Milan.",
                "phone": "+39 039 5328 4403",
                "whatsapp_href": "https://wa.me/390395328440",
                "email": "davide@domusimmobiliare.it",
                "quote": "Chaque année je vois des familles acheter en "
                         "Brianza pour le troisième enfant : c'est un meilleur indice que le PIB.",
            },
            {
                "name": "Elisa Parini",
                "role": "Coordinatrice notariale",
                "area": "Back-office · siège Milan",
                "years": "8 ans",
                "languages": "Italien · Anglais · Espagnol",
                "speciality": "Actes notariés, vérifications hypothécaires, "
                              "instruction de prêt, gestion notariale de bout en bout.",
                "phone": "+39 02 8765 4326",
                "whatsapp_href": "https://wa.me/390287654326",
                "email": "elisa@domusimmobiliare.it",
                "quote": "Le notaire est le dernier mètre mais souvent le "
                         "plus délicat : une erreur sur le plan coûte des mois.",
            },
        ],

        "facts_label":   "L'agence, en bref",
        "facts_heading": "Vingt ans, une seule règle : un agent par famille.",
        "facts": [
            ("2005", "",  "année de fondation"),
            ("9",    "",  "agents inscrits à l'ordre"),
            ("2",    "",  "bureaux · Milan & Turin"),
            ("2 800","+", "familles accompagnées au notaire"),
        ],

        "footnote_strong": "Envie de parler avec l'un de nous ?",
        "footnote_body":
            "Choisissez l'agent de votre zone ou écrivez-nous en chat : "
            "nous vous mettons en contact sous une heure ouvrée. ",
        "footnote_link":  "Écrivez-nous sur WhatsApp",
    },

    "valutazione": {
        "eyebrow":  "Estimation gratuite · réponse sous 24 heures",
        "headline": "Combien vaut <em>votre bien</em> ?",
        "intro":
            "Nous vous rappelons sous 24 heures avec une estimation "
            "honnête, basée sur la comparaison de toutes les ventes "
            "enregistrées ces douze derniers mois dans votre îlot. "
            "Aucun engagement, zéro coût, même si vous décidez ensuite "
            "de vendre avec une autre agence.",

        "how_it_works_label":   "Comment ça marche",
        "how_it_works_heading": "Trois étapes, <em>aucune surprise</em>.",
        "how_it_works": [
            ("01", "Vous remplissez le formulaire",
             "Il nous faut l'adresse, le type de bien, la surface et quatre "
             "détails sur son état. Cinq minutes, aucune pièce jointe à "
             "cette étape."),
            ("02", "Nous vous rappelons sous 24 h",
             "Un agent de votre quartier vous appelle, confirme les "
             "données et, si besoin, fixe une visite gratuite. Pour Milan "
             "et Turin souvent dès le lendemain."),
            ("03", "Vous recevez l'estimation écrite",
             "Sous 48 heures après la visite vous recevez une estimation "
             "écrite avec une fourchette de prix, les comparables du "
             "quartier, un plan de mise en vente recommandé."),
        ],

        "form_label":   "Demander l'estimation",
        "form_heading": "Parlez-nous de votre bien",
        "form_intro":
            "Décrivez votre logement en cinq minutes. Les champs avec un "
            "astérisque sont obligatoires — les autres aident à donner "
            "une estimation plus précise dès le premier contact.",
        "form_submit_label": "Demander une estimation gratuite",
        "form_submit_note":
            "Nous vous rappelons sous 24 heures ouvrées. Vos données "
            "sont traitées uniquement par l'agent dédié, aucun tiers "
            "impliqué.",
        "form_consent":
            "Je consens au traitement des données personnelles selon le "
            "Règlement UE 679/2016. La demande est lue et archivée "
            "uniquement par l'agent Domus — aucun courtier externe impliqué.",

        "form_sections": [
            {"num": "01", "title": "Votre bien",
             "meta": "Adresse, type, surface. Cinq minutes.",
             "fields": ["address", "city", "property_type", "surface", "rooms", "bathrooms"]},
            {"num": "02", "title": "État du bien",
             "meta": "Quatre points qui pèsent beaucoup sur l'estimation.",
             "fields": ["condition", "floor", "energy_class", "timeline"]},
            {"num": "03", "title": "Vos coordonnées",
             "meta": "Pour vous rappeler sous 24 heures.",
             "fields": ["name", "surname", "email", "phone", "notes"]},
        ],

        "form_fields": [
            {"name": "address", "label": "Adresse du bien", "type": "text", "required": True,
             "placeholder": "Ex. Via della Spiga 12", "full_width": True,
             "helper": "Rue et numéro. Le quartier, nous le déduisons."},
            {"name": "city", "label": "Ville", "type": "select", "required": True,
             "options": ["Milan", "Turin", "Côme et province", "Monza et Brianza", "Autre (préciser dans les notes)"],
             "helper": "Si votre ville n'y est pas, indiquez-la dans les notes."},
            {"name": "property_type", "label": "Type de bien", "type": "select", "required": True,
             "options": [
                 "Appartement · deux-pièces",
                 "Appartement · trois-pièces",
                 "Appartement · quatre-pièces ou plus",
                 "Penthouse",
                 "Loft",
                 "Villa indépendante",
                 "Villa mitoyenne ou bi-familiale",
                 "Bureau",
                 "Autre",
             ],
             "helper": "Sélection obligatoire pour avancer."},
            {"name": "surface", "label": "Surface habitable (m²)", "type": "number", "required": True,
             "placeholder": "Ex. 95",
             "helper": "Surface intérieure habitable, sans terrasses ni box."},
            {"name": "rooms", "label": "Chambres", "type": "select", "required": True,
             "options": ["1", "2", "3", "4", "5", "6 ou plus"],
             "helper": "Comptez les chambres à coucher, pas les salons."},
            {"name": "bathrooms", "label": "Salles de bain", "type": "select", "required": True,
             "options": ["1", "2", "3", "4 ou plus"]},
            {"name": "condition", "label": "État", "type": "select", "required": True,
             "options": [
                 "Neuf ou intégralement rénové",
                 "Bon état · petits travaux",
                 "À rénover partiellement",
                 "À rénover entièrement",
                 "Brut · bien de construction neuve",
             ],
             "helper": "Pèse beaucoup sur l'estimation."},
            {"name": "floor", "label": "Étage", "type": "select", "required": False,
             "options": ["Rez-de-chaussée", "Surélevé", "1er", "2ème", "3ème", "4ème ou plus", "Penthouse", "Villa indépendante"],
             "helper": "Facultatif — utile pour les appartements."},
            {"name": "energy_class", "label": "Classe énergétique", "type": "select", "required": False,
             "options": ["A4 / A3 / A2 / A1", "B", "C", "D", "E", "F", "G", "Non disponible"],
             "helper": "Si vous ne savez pas, cochez « Non disponible »."},
            {"name": "timeline", "label": "Délai de vente", "type": "select", "required": True,
             "options": [
                 "Sous 3 mois · urgent",
                 "Sous 6 mois",
                 "Sous 12 mois",
                 "Exploratoire · aucune urgence",
             ],
             "helper": "Aide à planifier le calendrier des visites."},
            {"name": "name", "label": "Prénom", "type": "text", "required": True, "placeholder": "Ex. Laura"},
            {"name": "surname", "label": "Nom", "type": "text", "required": True, "placeholder": "Ex. Ferrante"},
            {"name": "email", "label": "E-mail", "type": "email", "required": True,
             "placeholder": "laura.ferrante@example.it",
             "helper": "Nous vous envoyons l'estimation écrite par e-mail."},
            {"name": "phone", "label": "Téléphone", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "Nous vous rappelons sous 24 heures ouvrées."},
            {"name": "notes", "label": "Notes complémentaires", "type": "textarea", "required": False,
             "full_width": True,
             "placeholder": "Parlez-nous davantage du bien — terrasse, box, "
                            "cave, ascenseur, éventuels travaux déjà chiffrés. "
                            "Maximum 600 caractères.",
             "helper": "Facultatif mais aide à affiner l'estimation."},
        ],

        "proof_label":   "Pourquoi nous faire confiance",
        "proof_heading": "Une estimation sérieuse, pas une accroche commerciale.",
        "proof": [
            ("420+",  "estimations écrites en 2025"),
            ("92 %",  "biens vendus sous 6 mois"),
            ("0 €",   "coût de l'estimation"),
            ("24 h",  "délai de réponse"),
        ],

        "faq_label":   "Questions sur l'estimation",
        "faq_heading": "Ce que vous nous demandez le plus souvent.",
        "faq": [
            (
                "L'estimation est-elle vraiment gratuite ?",
                "Oui, toujours. Même si vous décidez ensuite de vendre "
                "avec une autre agence — ça arrive, ce n'est pas un "
                "drame. Le coût de la visite est à notre charge.",
            ),
            (
                "Combien de temps entre la demande et l'estimation écrite ?",
                "Nous vous rappelons sous 24 heures ouvrées. S'il faut "
                "une visite, nous la fixons sous 3 jours. L'estimation "
                "écrite arrive sous 48 heures après la visite.",
            ),
            (
                "L'estimation vaut-elle pour un prêt ou une succession ?",
                "Pour un usage bancaire ou successoral il faut une "
                "expertise assermentée par un expert inscrit au CTU. "
                "Notre estimation est de marché — précieuse pour décider, "
                "pas juridiquement opposable.",
            ),
            (
                "Dois-je vous montrer des documents à cette étape ?",
                "Non. Les données du formulaire suffisent. Acte, plan et "
                "DPE ne seront nécessaires que si vous décidez ensuite de "
                "mettre le bien en vente avec nous.",
            ),
        ],
    },

    "contatti": {
        "eyebrow":  "Contact · Milan & Turin",
        "headline": "Écrivez-nous, <em>nous vous rappelons sous 20 minutes</em>.",
        "intro":
            "Vous pouvez écrire, téléphoner, passer à l'agence. Le samedi "
            "nous sommes ouverts toute la journée, le dimanche sur rendez-"
            "vous. Pour les urgences WhatsApp est le canal le plus rapide.",

        "offices_label":   "Les bureaux",
        "offices_heading": "Deux bureaux, <em>une seule équipe</em>.",
        "offices": [
            {
                "name": "Milan · siège",
                "address": "Corso Buenos Aires 15 · 20124 Milan",
                "metro": "M1 Lima · M1 Loreto · Tram 33",
                "hours": "Lun – Sam · 09h00 – 19h30 · Dim sur rendez-vous",
                "phone": "+39 02 8765 4321",
                "whatsapp": "02 8765 4321",
                "whatsapp_href": "https://wa.me/390287654321",
                "email": "milano@domusimmobiliare.it",
                "map_link": "Ouvrir dans Google Maps",
                "map_href": "https://maps.google.com/?q=Corso+Buenos+Aires+15+Milano",
                "lead_agent": "Giulia Ferrante · responsable Milan",
                "parking": "Parking conventionné à 80 m · Garage Abadia",
                "note": "Bureau spacieux avec trois salles dédiées aux "
                        "rendez-vous privés. Eau, café, Wi-Fi à disposition.",
            },
            {
                "name": "Turin · Crocetta",
                "address": "Via Legnano 8 · 10128 Turin",
                "metro": "M1 Re Umberto · Tram 4/10",
                "hours": "Lun – Ven · 09h00 – 19h00 · Sam 09h30 – 13h00",
                "phone": "+39 011 5328 4400",
                "whatsapp": "011 5328 4400",
                "whatsapp_href": "https://wa.me/390115328440",
                "email": "torino@domusimmobiliare.it",
                "map_link": "Ouvrir dans Google Maps",
                "map_href": "https://maps.google.com/?q=Via+Legnano+8+Torino",
                "lead_agent": "Silvia Mondelli · responsable Turin",
                "parking": "ZTL gratuite le week-end · parking Piazza Solferino",
                "note": "Bureau accueillant au cœur de la Crocetta, à "
                        "deux minutes du Politecnico.",
            },
        ],

        "channels_label":   "Canaux directs",
        "channels_heading": "Choisissez comment nous joindre.",
        "channels": [
            ("Téléphone",       "+39 02 8765 4321",                "Réponse immédiate aux heures d'ouverture"),
            ("WhatsApp Milan",  "02 8765 4321",                    "Message lu sous 20 minutes · même le soir"),
            ("WhatsApp Turin",  "011 5328 4400",                   "Lun – Sam · la même équipe qu'au bureau"),
            ("E-mail",          "bonjour@domusimmobiliare.it",     "Nous répondons sous 4 heures ouvrées"),
            ("À l'agence",      "Milan · Corso Buenos Aires 15",   "Sans rendez-vous Lun – Sam le matin"),
        ],

        "form_label":   "Écrivez-nous un message",
        "form_heading": "Laissez vos coordonnées",
        "form_intro":
            "Remplissez le formulaire, nous vous rappelons sous 20 "
            "minutes aux heures d'ouverture. Si vous écrivez le soir, "
            "nous répondons le lendemain matin avant dix heures.",
        "form_submit_label": "Envoyer le message",
        "form_submit_note":
            "Réponse sous 20 minutes aux heures d'ouverture · 4 heures "
            "ouvrées pour les e-mails hors horaires.",
        "form_consent":
            "Je consens au traitement des données personnelles selon le "
            "Règlement UE 679/2016. La demande est lue et archivée "
            "uniquement par l'agent Domus.",

        "form_sections": [
            {"num": "01", "title": "Vos coordonnées",
             "meta": "Pour vous répondre directement.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Comment pouvons-nous aider",
             "meta": "Un bref repère, ensuite on en parle au téléphone.",
             "fields": ["topic", "preferred_office", "message"]},
        ],

        "form_fields": [
            {"name": "name", "label": "Prénom", "type": "text", "required": True, "placeholder": "Ex. Francesca"},
            {"name": "surname", "label": "Nom", "type": "text", "required": True, "placeholder": "Ex. Ranieri"},
            {"name": "email", "label": "E-mail", "type": "email", "required": True,
             "placeholder": "francesca@example.it"},
            {"name": "phone", "label": "Téléphone", "type": "tel", "required": False,
             "placeholder": "+39 ...", "helper": "Facultatif · si vous préférez être rappelée."},
            {"name": "topic", "label": "Objet de la demande", "type": "select", "required": True,
             "options": [
                 "Je souhaite acheter un bien",
                 "Je souhaite vendre un bien",
                 "Je souhaite une estimation gratuite",
                 "Je cherche une location (transmis à un partenaire)",
                 "Autre · je vous explique dans le message",
             ]},
            {"name": "preferred_office", "label": "Bureau préféré", "type": "select", "required": True,
             "options": ["Milan · Corso Buenos Aires", "Turin · Via Legnano", "Lac de Côme · sur rendez-vous"]},
            {"name": "message", "label": "Message", "type": "textarea", "required": True, "full_width": True,
             "placeholder": "Ce que vous cherchez, où vous en êtes, quand "
                            "vous souhaiteriez nous parler. Maximum 800 "
                            "caractères — les détails, nous les voyons en appel.",
             "helper": "Une synthèse suffit : le reste au téléphone."},
        ],
    },

    "immobili": {
        "eyebrow":  "Vitrine complète · 600+ biens · mise à jour cette semaine",
        "headline": "Tous les biens <em>que nous avons en main</em>.",
        "intro":
            "Une sélection vivante : chaque fiche est vérifiée par "
            "l'agent de la zone, chaque photo est prise en direct, "
            "aucun rendu. Les nouveautés arrivent tous les lundis matin.",

        "filter_label": "Filtrer",
        "filters": [
            "Tous",
            "Milan",
            "Turin",
            "Lac de Côme",
            "Sous 500 K €",
            "500 K € — 1 M €",
            "Au-dessus de 1 M €",
            "Penthouse",
            "Villa",
            "Loft",
            "Construction neuve",
        ],
        "sort_label": "Trier",
        "sort_options": [
            "Plus récents",
            "Prix croissant",
            "Prix décroissant",
            "Surface décroissante",
        ],

        "ledger_label": "Vitrine complète",
        "ledger_intro":
            "Cliquez sur une fiche pour ouvrir le dossier complet : "
            "plan, classe énergétique, historique des travaux, agent "
            "référent et créneaux de visite déjà réservables.",

        "row_rooms_label":    "Chambres",
        "row_surface_label":  "m²",
        "row_area_label":     "Zone",
        "row_price_label":    "Prix",
        "row_year_label":     "Depuis",
        "row_discipline_label":"Type",
        "row_duration_label": "Durée moyenne de visite",

        "map_label":   "Là où nous cherchons",
        "map_heading": "Notre vitrine, <em>sur la carte</em>.",
        "map_intro":
            "Trois provinces, deux bureaux, une seule équipe. Chaque "
            "point sur la carte correspond à un bien actuellement en "
            "vente ou sur le point d'entrer en vitrine.",
        "map_note":
            "La carte interactive est disponible dans la version "
            "commerciale du site — ici vous voyez seulement un aperçu "
            "indicatif de la présence.",
        "map_cells": [
            ("Milan ville",      "412 biens"),
            ("Monza Brianza",    "58 biens"),
            ("Lac de Côme",      "71 biens"),
            ("Turin ville",      "105 biens"),
            ("Turin collines",   "38 biens"),
        ],

        "cta_label":        "Vous ne trouvez pas ce que vous cherchez ?",
        "cta_heading":      "Dites-nous ce qui manque. <em>On le trouve</em>.",
        "cta_intro":
            "Ces cinq dernières années plus de 30 % des logements que "
            "nous avons vendus n'étaient pas encore en ligne : nous les "
            "avions en main par des vendeurs habitués. Dites-nous ce "
            "que vous cherchez et nous vous prévenons dès que le bon "
            "arrive.",
        "cta_primary":        "Réserver une visite",
        "cta_primary_href":   "contatti",
        "cta_secondary":      "Parlons-en de vive voix",
        "cta_secondary_href": "contatti",

        "dossier_meta_price_label":    "Prix",
        "dossier_meta_surface_label":  "Surface",
        "dossier_meta_rooms_label":    "Chambres",
        "dossier_meta_bathrooms_label":"SdB",
        "dossier_meta_energy_label":   "Classe énergie",
        "dossier_meta_floor_label":    "Étage",
        "dossier_summary_label":       "Ce que vous allez aimer",
        "dossier_highlights_label":    "Points forts",
        "dossier_highlights_heading":  "Les détails qui comptent.",
        "dossier_agent_label":         "Agent référent",
        "dossier_book_cta":            "Réserver une visite",
        "dossier_next_label":          "Bien suivant",
    },

    "posts": [
        {
            "slug":       "attico-brera-duomo",
            "title":      "Penthouse panoramique avec terrasse · Brera",
            "price":      "1 250 000 €",
            "area":       "Milano · Brera · Via Madonnina 14",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "180",
            "energy":     "B",
            "floor":      "7ème (dernier · ascenseur)",
            "badge":      "Exclusivité",
            "reference":  "MI-1842",
            "year_built": "1923 · rénovation intégrale 2024",
            "lead":
                "Un penthouse au dernier étage d'un palais d'époque avec "
                "une terrasse de soixante mètres et une vue à 270 degrés "
                "sur le Duomo et la Piazza della Scala. Rénovation 2024 "
                "signée Studio Arfaioli, technologie smart-home intégrée.",
            "summary": [
                "Terrasse de 62 m² avec vue Duomo et Sforzesco",
                "Quatre chambres, deux salles de bain en marbre de Carrare",
                "Classe énergétique B après isolation et menuiseries 2024",
                "Ascenseur interne jusqu'au penthouse, trois places de parking incluses",
                "Livrable · acte dans les 45 jours",
            ],
            "highlights": [
                ("Terrasse", "62 m² vue Duomo"),
                ("Parking", "Trois places en box privatif"),
                ("Domotique", "KNX intégralement intégré"),
                ("Classe énergie", "B · après travaux 2024"),
            ],
            "description":
                "L'appartement a été entièrement redessiné autour de "
                "l'idée d'un loft vertical : séjour de 70 m² à double "
                "exposition est-sud, îlot en laiton brossé, bibliothèque "
                "toute hauteur en noyer canaletto. Le secteur nuit est "
                "réservé aux deux suites avec dressing et salle de bain "
                "privative en marbre statuario. Sur la terrasse, un "
                "spa extérieur et une table pour dix.",
            "agent_name":  "Giulia Ferrante",
            "agent_role":  "Agent senior · Milan Centre",
            "agent_phone": "+39 02 8765 4322",
        },
        {
            "slug":       "villa-cernobbio-lago",
            "title":      "Villa moderne avec jardin · Cernobbio",
            "price":      "890 000 €",
            "area":       "Como · Cernobbio · Via Regina 88",
            "rooms":      "5",
            "bathrooms":  "3",
            "surface":    "240",
            "energy":     "A2",
            "floor":      "Villa indépendante · 3 niveaux",
            "badge":      "Nouveau",
            "reference":  "CO-0217",
            "year_built": "2023",
            "lead":
                "Villa de construction neuve sur trois niveaux à deux "
                "cents mètres du lac, jardin privatif de mille mètres "
                "avec piscine chauffée. Finitions contemporaines, "
                "géothermie, classe A2.",
            "summary": [
                "Jardin privé de 1 020 m² avec piscine 10 × 4",
                "Cinq chambres, trois salles de bain, bureau et buanderie séparés",
                "Géothermie · classe énergétique A2",
                "Accès direct au lac à 200 m",
                "Box double et place d'hôte couverte",
            ],
            "highlights": [
                ("Jardin", "1 020 m² avec piscine"),
                ("Installations", "Géothermie · photovoltaïque 8 kW"),
                ("Chambres", "Cinq · deux suites"),
                ("Classe", "A2 · consommations quasi nulles"),
            ],
            "description":
                "La villa s'élève sur une parcelle d'angle avec jardin "
                "sur trois côtés, orientation sud-est pour le secteur "
                "jour. Sous-sol avec taverne, cave climatisée et box "
                "double ; rez-de-chaussée avec salon double hauteur, "
                "cuisine professionnelle Boffi et accès au jardin ; "
                "étage avec quatre chambres et deux salles de bain, "
                "plus suite parentale avec dressing.",
            "agent_name":  "Andrea Colombo",
            "agent_role":  "Agent senior · Lac de Côme",
            "agent_phone": "+39 031 2345 6789",
        },
        {
            "slug":       "loft-tortona-navigli",
            "title":      "Loft de design dans le quartier Tortona",
            "price":      "650 000 €",
            "area":       "Milano · Navigli · Via Savona 22",
            "rooms":      "2",
            "bathrooms":  "2",
            "surface":    "120",
            "energy":     "C",
            "floor":      "Rez surélevé · cour",
            "badge":      "Rénové",
            "reference":  "MI-1788",
            "year_built": "1902 · reconversion ex-manufacture 2020",
            "lead":
                "Loft de cent vingt mètres dans un ex-atelier du début "
                "du XXᵉ, double hauteur quatre mètres cinquante, sol "
                "d'origine en chêne, mezzanine en fer noir pour le "
                "secteur nuit. Vue sur une cour intérieure silencieuse.",
            "summary": [
                "Plafond à poutres de fer et béton apparent",
                "Séjour double hauteur · cuisine ouverte",
                "Mezzanine fer et bois · suite avec dressing",
                "Cour commune avec jardinet intérieur",
                "Aucune exposition sur rue · silence total",
            ],
            "highlights": [
                ("Hauteur", "4,5 m double hauteur"),
                ("Lumière", "Grande baie 6 × 3 m"),
                ("Mobilier", "Cuisine Boffi incluse"),
                ("Exposition", "Cour silencieuse"),
            ],
            "description":
                "Le loft a été créé dans le dernier module d'un ex-"
                "atelier textile restauré en 2020. Colonnes porteuses "
                "en fonte conservées, parquet d'origine en chêne "
                "repositionné, menuiseries en fer remplacées par "
                "vitrage thermique. Le secteur nuit en mezzanine "
                "domine l'espace sans le fermer.",
            "agent_name":  "Marco Lentini",
            "agent_role":  "Agent senior · Milan Sud",
            "agent_phone": "+39 02 8765 4323",
        },
        {
            "slug":       "trilocale-crocetta-torino",
            "title":      "Trois-pièces lumineux avec balcon · Crocetta",
            "price":      "420 000 €",
            "area":       "Torino · Crocetta · Corso Giovanni Lanza 7",
            "rooms":      "3",
            "bathrooms":  "1",
            "surface":    "95",
            "energy":     "D",
            "floor":      "3ème (ascenseur)",
            "badge":      "Disponible",
            "reference":  "TO-0904",
            "year_built": "1932 · entretien courant 2019",
            "lead":
                "Trois-pièces au cœur de la Crocetta, palais des années "
                "trente parfaitement conservé, balcon de sept mètres "
                "sur cour verte, exposition est-ouest. Distribution "
                "classique, parquet d'origine.",
            "summary": [
                "Palais années 30 · isolation refaite 2018",
                "Balcon de 7 m² vue cour verte",
                "Parquet d'origine en chêne · poutres apparentes à l'entrée",
                "Cave de 12 m² incluse",
                "Livrable · libre à la signature",
            ],
            "highlights": [
                ("Palais", "1932 · gardien 24/7"),
                ("Balcon", "7 m² vue verdure"),
                ("Parquet", "D'origine restauré"),
                ("Étage", "3ème avec ascenseur"),
            ],
            "description":
                "Appartement dans l'un des palais emblématiques de la "
                "Crocetta, rue tranquille à deux cents mètres du corso "
                "Galileo Ferraris. Distribution classique : entrée, "
                "séjour avec balcon, cuisine à manger, couloir, deux "
                "chambres parentales, salle de bain avec fenêtre. "
                "Parquet d'origine en parfait état, installations "
                "refaites en 2019.",
            "agent_name":  "Silvia Mondelli",
            "agent_role":  "Responsable Turin",
            "agent_phone": "+39 011 5328 4401",
        },
        {
            "slug":       "quadrilocale-isola-milano",
            "title":      "Quatre-pièces vue BAM · Isola",
            "price":      "780 000 €",
            "area":       "Milano · Isola · Via Confalonieri 25",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "135",
            "energy":     "A3",
            "floor":      "8ème (double ascenseur)",
            "badge":      "Vue parc",
            "reference":  "MI-1915",
            "year_built": "2019",
            "lead":
                "Appartement dans une résidence de design de 2019, "
                "exposition principale sur la Bibliothèque des Arbres. "
                "Quatre chambres, deux salles de bain, balcon habitable "
                "de onze mètres. Classe A3, domotique de série.",
            "summary": [
                "Vue parc BAM depuis le séjour",
                "Balcon habitable de 11 m²",
                "Résidence avec concierge 24/7",
                "Box inclus · borne de recharge VE",
                "Classe A3 · climatisation intégrée",
            ],
            "highlights": [
                ("Vue", "BAM et Bosco Verticale"),
                ("Concierge", "24/7 à l'accueil"),
                ("Recharge", "Borne VE incluse"),
                ("Classe", "A3 · pompe à chaleur"),
            ],
            "description":
                "Huitième étage dans une résidence signée Piuarch avec "
                "concierge 24/7, salle de sport privative et jardin "
                "intérieur. Appartement d'angle à double exposition : "
                "séjour vers le parc BAM, secteur nuit vers la cour "
                "intérieure. Loggia-balcon de onze mètres utilisable "
                "neuf mois par an. Mobilier sur mesure inclus de série.",
            "agent_name":  "Sofia Ranieri",
            "agent_role":  "Agent · Milan Nord",
            "agent_phone": "+39 02 8765 4324",
        },
        {
            "slug":       "bilocale-porta-nuova",
            "title":      "Deux-pièces smart · Porta Nuova",
            "price":      "520 000 €",
            "area":       "Milano · Porta Nuova · Via Melchiorre Gioia 62",
            "rooms":      "2",
            "bathrooms":  "1",
            "surface":    "68",
            "energy":     "A2",
            "floor":      "12ème (vue Unicredit)",
            "badge":      "Excellent investissement",
            "reference":  "MI-1967",
            "year_built": "2015",
            "lead":
                "Deux-pièces à 80 % exposition sud, vue sur le parc et "
                "les gratte-ciel de Porta Nuova. Parfait pour un premier "
                "achat ou un investissement locatif, rendement brut "
                "attendu 4,2 %.",
            "summary": [
                "Exposition sud · lumière toute la journée",
                "Vue tours Unicredit et Diamante",
                "Concierge de zone · salle de sport privative",
                "Rendement locatif estimé 4,2 % brut",
                "Livrable · libre à la signature",
            ],
            "highlights": [
                ("Exposition", "Plein sud"),
                ("Étage", "12ème vue skyline"),
                ("Rendement", "4,2 % brut attendu"),
                ("Libre", "À la signature"),
            ],
            "description":
                "Deux-pièces de 68 m² avec séjour-cuisine de 32 m² vue "
                "skyline, chambre parentale avec dressing, salle de "
                "bain en pierre grise. Résidence avec services, salle "
                "de sport et lounge, concierge de jour sept jours sur "
                "sept. Idéal pour qui travaille dans les tours voisines "
                "ou cherche un investissement rentable.",
            "agent_name":  "Giulia Ferrante",
            "agent_role":  "Agent senior · Milan Centre",
            "agent_phone": "+39 02 8765 4322",
        },
        {
            "slug":       "villa-bellagio-lago",
            "title":      "Villa d'époque vue Spartivento · Bellagio",
            "price":      "1 950 000 €",
            "area":       "Como · Bellagio · Via Garibaldi 12",
            "rooms":      "6",
            "bathrooms":  "4",
            "surface":    "320",
            "energy":     "E",
            "floor":      "Villa indépendante · 3 niveaux + tour",
            "badge":      "Villa historique",
            "reference":  "CO-0248",
            "year_built": "1908 · restauration conservative 2017",
            "lead":
                "Villa Liberty à Punta Spartivento, 320 mètres couverts "
                "plus tour belvédère, jardin en terrasses avec accès "
                "privatif au lac. Restauration 2017 avec climatisation "
                "et installations mises à jour.",
            "summary": [
                "Punta Spartivento · double vue lac",
                "Jardin en terrasses avec accès privé au lac",
                "Tour belvédère panoramique à 360°",
                "Restauration 2017 avec installations contemporaines",
                "Six chambres, quatre salles de bain, cave historique",
            ],
            "highlights": [
                ("Position", "Punta Spartivento"),
                ("Vue", "Double lac"),
                ("Accès", "Privé au lac"),
                ("Tour", "Belvédère 360°"),
            ],
            "description":
                "Villa symbole du Liberty du Lario, dessinée par "
                "l'architecte Pietro Lingeri en 1908. Trois niveaux "
                "habitables plus tour belvédère, exposition est sur le "
                "bras de Lecco et ouest sur le bras de Côme. La "
                "restauration 2017 a préservé les stucs d'origine, les "
                "vitraux Liberty et les sols en terrazzo vénitien, en "
                "intégrant un chauffage rayonnant et une climatisation "
                "cachée.",
            "agent_name":  "Andrea Colombo",
            "agent_role":  "Agent senior · Lac de Côme",
            "agent_phone": "+39 031 2345 6789",
        },
        {
            "slug":       "appartamento-borgo-po-torino",
            "title":      "Appartement vue Alpes · Borgo Po",
            "price":      "560 000 €",
            "area":       "Torino · Borgo Po · Corso Casale 102",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "145",
            "energy":     "D",
            "floor":      "5ème (dernier · ascenseur)",
            "badge":      "Vue collines",
            "reference":  "TO-0945",
            "year_built": "1928 · appartement rénové 2021",
            "lead":
                "Dernier étage avec vue dégagée sur la Mole, le Monte "
                "dei Cappuccini et les Alpes. Cent quarante-cinq mètres "
                "sur un seul niveau, deux balcons habitables, "
                "distribution classique parfaitement préservée.",
            "summary": [
                "Vue Alpes et Mole Antonelliana depuis le séjour",
                "Deux balcons habitables · 6 + 4 m²",
                "Plafonds 3,20 m avec stucs d'origine",
                "Rénovation 2021 · installations neuves",
                "Cave et combles de 18 m² inclus",
            ],
            "highlights": [
                ("Vue", "Alpes et Mole"),
                ("Étage", "5ème, dernier"),
                ("Plafonds", "3,20 m stucs"),
                ("Balcons", "Deux habitables"),
            ],
            "description":
                "Dernier étage d'angle dans un palais des années vingt "
                "restauré en 2020, quatre chambres sur un seul niveau, "
                "double exposition sur corso Casale et via Villa della "
                "Regina. Secteur jour tourné vers la Mole, secteur nuit "
                "vers la colline. Stucs d'origine conservés dans toutes "
                "les pièces.",
            "agent_name":  "Luca Benedetti",
            "agent_role":  "Agent · Turin Collines",
            "agent_phone": "+39 011 5328 4402",
        },
        {
            "slug":       "villa-monza-brianza",
            "title":      "Villa indépendante avec parc · Monza",
            "price":      "1 050 000 €",
            "area":       "Monza · San Fruttuoso · Via Buonarroti 48",
            "rooms":      "6",
            "bathrooms":  "4",
            "surface":    "280",
            "energy":     "B",
            "floor":      "Villa indépendante · 3 niveaux",
            "badge":      "Parc privé",
            "reference":  "MB-0177",
            "year_built": "2001 · réhabilitation 2022",
            "lead":
                "Villa indépendante sur un terrain de mille deux cents "
                "mètres, parc planté d'arbres hauts, piscine chauffée "
                "et aire de jeux enfants. Trois niveaux habitables plus "
                "taverne et salle de sport.",
            "summary": [
                "Parc privé de 1 200 m² avec piscine chauffée",
                "Six chambres · quatre salles de bain · bureau · taverne",
                "Salle de sport et sauna au niveau sous-sol",
                "Classe B après isolation 2022 · photovoltaïque 12 kW",
                "Box triple et place d'hôte couverte",
            ],
            "highlights": [
                ("Parc", "1 200 m² arboré"),
                ("Piscine", "Chauffée · 10 × 4,5"),
                ("Fitness", "Sauna · sport au sous-sol"),
                ("Classe", "B · photovoltaïque 12 kW"),
            ],
            "description":
                "La villa se trouve en zone résidentielle à dix minutes "
                "du centre de Monza et à vingt de la Milan du nord. "
                "Projet 2001 de grande qualité, réhabilitation 2022 "
                "avec isolation, menuiseries triple vitrage, "
                "photovoltaïque. Rez-de-chaussée avec séjour de cent "
                "vingt mètres face au parc, premier étage avec quatre "
                "chambres et trois salles de bain, combles avec bureau "
                "et chambre d'amis.",
            "agent_name":  "Davide Orsini",
            "agent_role":  "Agent · Monza & Brianza",
            "agent_phone": "+39 039 5328 4403",
        },
        {
            "slug":       "monolocale-navigli-milano",
            "title":      "Studio d'auteur vue alzaia · Navigli",
            "price":      "295 000 €",
            "area":       "Milano · Navigli · Alzaia Naviglio Grande 76",
            "rooms":      "1",
            "bathrooms":  "1",
            "surface":    "42",
            "energy":     "C",
            "floor":      "2ème (escalier en colimaçon historique)",
            "badge":      "Vue canal",
            "reference":  "MI-1994",
            "year_built": "1898 · restauration 2018",
            "lead":
                "Studio de quarante-deux mètres avec grande baie sur "
                "l'alzaia du Naviglio Grande, restauration conservative "
                "2018 signée Studio Ca' Rossa. Idéal pour un premier "
                "achat ou un investissement short-let.",
            "summary": [
                "Vue directe sur l'alzaia · grande baie 2 × 1,5",
                "Palais de 1898 · escalier en colimaçon d'origine",
                "Cuisine Boffi intégrée · salle de bain en pierre serena",
                "Parfait pour un investissement short-let",
                "Rendement estimé 5,8 % brut",
            ],
            "highlights": [
                ("Exposition", "Naviglio Grande"),
                ("Palais", "1898 escalier historique"),
                ("Rendement", "5,8 % brut"),
                ("Usage", "Short-let / première maison"),
            ],
            "description":
                "Studio aménagé au deuxième étage d'un palais historique "
                "directement sur l'alzaia du Naviglio Grande. Grande "
                "baie à double exposition avec fenêtres à guillotine "
                "restaurées, sols en terre cuite d'origine polie, "
                "cuisine intégrée signée Boffi et salle de bain en "
                "pierre serena. Convient à un usage personnel ou comme "
                "investissement : ces trois dernières années short-let "
                "stable au-dessus de 5,5 % brut.",
            "agent_name":  "Marco Lentini",
            "agent_role":  "Agent senior · Milan Sud",
            "agent_phone": "+39 02 8765 4323",
        },
        {
            "slug":       "attico-centro-torino",
            "title":      "Penthouse face au Palazzo Reale · Turin",
            "price":      "780 000 €",
            "area":       "Torino · Centro · Piazzetta Reale 3",
            "rooms":      "3",
            "bathrooms":  "2",
            "surface":    "140",
            "energy":     "C",
            "floor":      "6ème (dernier · ascenseur)",
            "badge":      "Vue historique",
            "reference":  "TO-0982",
            "year_built": "1874 · penthouse créé 2022",
            "lead":
                "Penthouse avec terrasse habitable face au Palazzo "
                "Reale, au Duomo et à la Mole Antonelliana. Cent "
                "quarante mètres sur un seul niveau, créé dans les "
                "combles historiques par Studio Isolarchitetti.",
            "summary": [
                "Terrasse habitable 24 m² vue Palazzo Reale",
                "Créé à partir de combles historiques · 2022",
                "Trois chambres, deux salles de bain, bureau indépendant",
                "Plafonds mansardés avec poutres d'origine apparentes",
                "Classe C après isolation toiture 2022",
            ],
            "highlights": [
                ("Vue", "Palazzo Reale, Mole, Duomo"),
                ("Terrasse", "24 m² habitable"),
                ("Poutres", "D'origine apparentes"),
                ("Classe", "C post-isolation"),
            ],
            "description":
                "Penthouse créé dans les combles d'un palais du XVIIᵉ "
                "restauré en 2022 par les Isolarchitetti. Poutres "
                "d'origine en mélèze conservées, sol en terre cuite "
                "polie posé en chevrons, salles de bain en pierre de "
                "Luserne. La terrasse panoramique s'ouvre sur la "
                "Piazzetta Reale et offre une double vue Mole et Duomo.",
            "agent_name":  "Silvia Mondelli",
            "agent_role":  "Responsable Turin",
            "agent_phone": "+39 011 5328 4401",
        },
        {
            "slug":       "loft-isola-milano",
            "title":      "Loft ex-atelier avec cour · Isola",
            "price":      "680 000 €",
            "area":       "Milano · Isola · Via Borsieri 32",
            "rooms":      "2",
            "bathrooms":  "2",
            "surface":    "115",
            "energy":     "B",
            "floor":      "Rez-de-chaussée · cour privée",
            "badge":      "Cour privée",
            "reference":  "MI-2012",
            "year_built": "1927 · réhabilitation intégrale 2023",
            "lead":
                "Loft aménagé dans un ex-atelier mécanique avec trente "
                "mètres de cour privée, double hauteur cinq mètres et "
                "grandes baies industrielles d'origine. Réhabilitation "
                "intégrale 2023, chauffage rayonnant et photovoltaïque.",
            "summary": [
                "Cour privée de 30 m² · essences méditerranéennes",
                "Double hauteur 5 m · baies industrielles",
                "Réhabilitation 2023 · chauffage rayonnant + photovoltaïque",
                "Loft ouvert avec suite fermée · salle d'eau service",
                "Classe B · pompe à chaleur + 4 kW solaire",
            ],
            "highlights": [
                ("Cour", "30 m² privée"),
                ("Hauteur", "5 m industrielle"),
                ("Installations", "Rayonnant + solaire"),
                ("Classe", "B · quasi autonome"),
            ],
            "description":
                "Le loft naît de la réhabilitation d'un ex-atelier "
                "mécanique de 1927. Volumes préservés, zonage minimal "
                "avec suite fermée par cloison vitrée et cuisine-îlot "
                "au centre. Cour privée de trente mètres à usage "
                "exclusif avec plantes grimpantes, plan de cuisson "
                "extérieur intégré, banc en béton lissé. Un morceau de "
                "la Milan qui était et de celle qui advient.",
            "agent_name":  "Sofia Ranieri",
            "agent_role":  "Agent · Milan Nord",
            "agent_phone": "+39 02 8765 4324",
        },
    ],
}

# Phase 2g3.7 · Session 53 · D-047 compliance closing comment:
# All user-visible literals in skin + preview compositions MUST be sourced
# from this content tree (or chrome / dna.content). No "Brera" / "Turin"
# / "Milan" / "chambres" / "Réserver visite" / "m²" may appear hard-coded
# in the HTML. Review in every PR touching real-estate/mass-market.
