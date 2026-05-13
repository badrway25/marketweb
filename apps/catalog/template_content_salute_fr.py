"""SALUTE_CONTENT_FR — native translation per D-072 multilingual voice law.

Voice contract (FR) : registre Ramsay Sante / Doctolib, vouvoiement formel.
« Consultation », « prise de rendez-vous », « equipe medicale », « centre de
sante ». Noms propres italiens conserves (SaluteVita, Dr Elisa Conti, Via
Galvani, Milan Centrale). Conventions et assurances italiennes conservees
avec glose contextuelle. Prix en euros (centre italien). Horaires a la
francaise : « Lun - Sam · 7 h 00 - 21 h 00 ».
"""
from __future__ import annotations

from typing import Any

from apps.catalog.template_content_salute import (
    ICO_STETHOSCOPE,
    ICO_BABY,
    ICO_DERM,
    ICO_ULTRASOUND,
    ICO_WOMAN,
    ICO_BONE,
    ICO_BRAIN,
    ICO_EYE,
)


SALUTE_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",        "label": "Accueil",        "kind": "home"},
        {"slug": "studio",      "label": "Le centre",      "kind": "about"},
        {"slug": "servizi",     "label": "Services",       "kind": "services"},
        {"slug": "prevenzione", "label": "Prévention",     "kind": "prevention"},
        {"slug": "medici",      "label": "Médecins",       "kind": "team"},
        {"slug": "contatti",    "label": "Contact",        "kind": "contact"},
        {"slug": "prenota",     "label": "Rendez-vous",    "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "S",
        "logo_word":    "SaluteVita",
        "tag":          "Centre médical pluridisciplinaire · Milan Centrale",
        "phone_label":  "Numéro vert",
        "phone":        "800 123 456",
        "phone_tel":    "+39800123456",
        "email":        "rdv@salutevita.clinic",
        "address":      "Via Galvani 18 · 20124 Milan",
        "hours_compact": "Lun – Sam · 7 h 00 – 21 h 00",
        "hours_footer_rows": [
            "Lun – Ven · 7 h 00 – 21 h 00",
            "Sam · 8 h 00 – 18 h 00",
            "Dimanche · fermé",
        ],
        "foot_extra_label": "Conventions",
        "foot_extra_rows": [
            "Inail · Unisalute · Generali",
            "RBM Salute · Previmedical",
            "Caspie · MioDottore",
        ],
        "license": "Inscrit au registre des structures sanitaires ATS Milan · TVA 09812345678",
        "footer_intro":
            "Centre médical pluridisciplinaire au cœur de Milan Centrale. "
            "Plus de 40 praticiens répartis dans 12 services, ouvert six "
            "jours sur sept — un point de référence médical proche des "
            "familles depuis 1998.",
    },

    "home": {
        "eyebrow":   "Centre médical · Milan Centrale · depuis 1998",
        "headline":  'Rendez-vous en trente secondes, <em>des médecins que vous voudrez revoir</em>.',
        "subhead":
            "Plus de 40 spécialistes, des parcours diagnostiques coordonnés "
            "et une expérience patient pensée pour vous mettre à l'aise dès "
            "le premier contact. Réservez en ligne en 30 secondes, du lundi "
            "au samedi de 7 h à 21 h.",
        "primary_cta":    "Prendre rendez-vous",
        "primary_href":   "prenota",
        "secondary_cta":  "Numéro vert 800 123 456",
        "secondary_href": "contatti",
        "trust_note":     "Réponse en moins de 2 heures · sans engagement",

        "stats": [
            ("40+",  "Médecins spécialistes"),
            ("12",   "Services"),
            ("98 %", "Patients qui reviendraient"),
        ],

        "booking_widget": {
            "aria_label":  "Prise de rendez-vous en ligne en trois étapes",
            "title":       "Rendez-vous en ligne en 30 secondes",
            "subtitle":    "Premier créneau souvent sous 48 heures ouvrées",
            "badge":       "6 créneaux libres aujourd'hui",
            "specialty_label": "Spécialité",
            "specialty_value": "Cardiologie",
            "date_label":      "Premier créneau",
            "date_value":      "Mar. 14 avril · 10 h 30",
            "doctor_label":    "Praticien",
            "doctor_value":    "Dr Elisa Conti",
            "cta":             "Confirmer le rendez-vous",
            "footnote":        "Gratuit · annulation possible jusqu'à 24 h avant",
            "secure_label":    "Données chiffrées",
        },

        "stats_strip": [
            ("1998",    "Année de fondation"),
            ("28 000",  "Patients suivis chaque année"),
            ("6",       "Jours d'ouverture par semaine"),
            ("0 €",     "Coût du premier appel"),
        ],

        "specialties_label": "Nos spécialités",
        "specialties_heading": 'Douze services <em>sous un même toit</em>.',
        "specialties_intro":
            "Toutes les consultations qu'une famille milanaise peut "
            "solliciter, coordonnées entre elles : si votre cardiologue "
            "prescrit une échographie, nous la programmons le jour même, "
            "dans le même bâtiment.",
        "specialties": [
            {
                "icon_svg": ICO_STETHOSCOPE,
                "title":    "Cardiologie",
                "blurb":    "Consultation cardiologique, ECG de repos et "
                            "d'effort, échocardiographie, holter tensionnel et ECG 24 heures.",
                "link_label": "Découvrir le service",
            },
            {
                "icon_svg": ICO_BABY,
                "title":    "Pédiatrie",
                "blurb":    "Bilans de santé 0–14 ans, vaccinations et "
                            "consultation pédiatrique urgente sous 24 heures.",
                "link_label": "Découvrir le service",
            },
            {
                "icon_svg": ICO_DERM,
                "title":    "Dermatologie",
                "blurb":    "Cartographie des grains de beauté en "
                            "dermoscopie numérique, dermatites, acné et "
                            "contrôles oncologiques cutanés.",
                "link_label": "Découvrir le service",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "title":    "Radiologie & diagnostic",
                "blurb":    "Échographie multi-organes, scanner, IRM, "
                            "mammographie. Compte rendu le jour même sur demande.",
                "link_label": "Découvrir le service",
            },
            {
                "icon_svg": ICO_WOMAN,
                "title":    "Gynécologie",
                "blurb":    "Consultations obstétricales et gynécologiques, "
                            "échographie endovaginale, frottis et suivi de grossesse.",
                "link_label": "Découvrir le service",
            },
            {
                "icon_svg": ICO_BONE,
                "title":    "Orthopédie & kinésithérapie",
                "blurb":    "Consultation orthopédique, infiltrations "
                            "écho-guidées et rééducation post-opératoire "
                            "avec un kinésithérapeute dédié.",
                "link_label": "Découvrir le service",
            },
            {
                "icon_svg": ICO_BRAIN,
                "title":    "Neurologie",
                "blurb":    "Consultation neurologique, "
                            "électroencéphalogramme et bilan des "
                            "céphalées récurrentes et des troubles du sommeil.",
                "link_label": "Découvrir le service",
            },
            {
                "icon_svg": ICO_EYE,
                "title":    "Ophtalmologie",
                "blurb":    "Bilan visuel complet, OCT rétinien, champ "
                            "visuel, évaluation de la cataracte en "
                            "collaboration avec des centres chirurgicaux conventionnés.",
                "link_label": "Découvrir le service",
            },
        ],

        "journey_label":    "Le parcours patient",
        "journey_heading":  'De la prise de rendez-vous au compte rendu, <em>quatre étapes simples</em>.',
        "journey_intro":
            "Nous avons conçu chaque étape comme une famille aimerait être "
            "accueillie : pas d'attente debout, aucun document perdu, "
            "jamais à raconter deux fois la même histoire.",
        "journey_steps": [
            {"num": "01", "title": "Prise de rendez-vous en ligne",
             "body": "Choisissez spécialité, praticien et créneau en "
                     "30 secondes. Un SMS de rappel arrive deux jours avant."},
            {"num": "02", "title": "Accueil",
             "body": "Réception ouverte dès 7 h. Nous vous accompagnons en "
                     "salle d'attente et vous appelons par votre nom dès "
                     "que le médecin est prêt."},
            {"num": "03", "title": "Consultation",
             "body": "Le praticien a déjà votre dossier médical sous les "
                     "yeux. Consultation approfondie, examens sur place "
                     "lorsque c'est possible."},
            {"num": "04", "title": "Compte rendu numérique",
             "body": "Compte rendu et ordonnances dans votre espace "
                     "patient sous 24 heures, téléchargeables en PDF et "
                     "partageables avec votre médecin traitant."},
        ],

        "prevenzione_label":   "Bilans de prévention",
        "prevenzione_heading": 'Prévenir coûte <em>moins</em> que soigner.',
        "prevenzione_intro":
            "Trois forfaits conçus pour les tranches d'âge où le dépistage "
            "compte le plus. 15 % de remise si vous renouvelez votre bilan "
            "dans les 12 mois.",
        "prevenzione_cards": [
            {
                "eyebrow":  "Femme 40+",
                "title":    "Bilan Femme 40+",
                "desc":     "Consultation gynécologique, échographie pelvienne, "
                            "frottis, mammographie et consultation nutritionnelle — "
                            "tout en une seule matinée.",
                "includes": [
                    "Consultation gynécologique complète",
                    "Frottis et test HPV",
                    "Échographie pelvienne + mammographie",
                    "Consultation nutritionnelle de 30 minutes",
                ],
                "duration_label": "Durée",
                "duration":       "3 heures",
                "price_label":    "Tarif tout compris",
                "price":          "320 €",
                "cta":            "Réserver le bilan",
            },
            {
                "eyebrow":  "Homme 45+",
                "title":    "Bilan Homme 45+",
                "desc":     "Cardiologie, urologie, dépistage métabolique, "
                            "échographie abdominale et prostatique. "
                            "Compte rendu unique sous 48 heures.",
                "includes": [
                    "Consultation cardiologique + ECG",
                    "Consultation urologique + PSA",
                    "Échographie abdominale complète",
                    "Profil métabolique lipidique",
                ],
                "duration_label": "Durée",
                "duration":       "3 h 30",
                "price_label":    "Tarif tout compris",
                "price":          "280 €",
                "cta":            "Réserver le bilan",
            },
            {
                "eyebrow":  "Plus de 60 ans",
                "title":    "Bilan Seniors",
                "desc":     "Bilan cardiovasculaire, osseux, neurologique et "
                            "ophtalmologique, coordonné par un interniste qui "
                            "articule l'ensemble du tableau clinique.",
                "includes": [
                    "Cardiologie + échocardiographie + holter",
                    "Ostéodensitométrie DEXA",
                    "Consultation neurologique cognitive",
                    "Ophtalmologie + tonométrie",
                ],
                "duration_label": "Durée",
                "duration":       "4 heures",
                "price_label":    "Tarif tout compris",
                "price":          "420 €",
                "cta":            "Réserver le bilan",
            },
        ],

        "team_label":   "Nos spécialistes",
        "team_heading": 'Huit visages, <em>huit services phares</em>.',
        "team_intro":
            "Plus de 40 praticiens collaborent avec SaluteVita. Vous "
            "retrouvez ici les responsables des huit services les plus "
            "demandés — l'équipe complète figure sur une page dédiée.",
        "team_ribbon_people": [
            {
                "avatar": "https://images.pexels.com/photos/5327585/pexels-photo-5327585.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Elisa Conti",
                "specialty":"Cardiologie",
            },
            {
                "avatar": "https://images.pexels.com/photos/5452293/pexels-photo-5452293.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Marco Ferri",
                "specialty":"Pédiatrie",
            },
            {
                "avatar": "https://images.pexels.com/photos/5452274/pexels-photo-5452274.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Sofia Lenzi",
                "specialty":"Dermatologie",
            },
            {
                "avatar": "https://images.pexels.com/photos/4173239/pexels-photo-4173239.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Luca Russo",
                "specialty":"Radiologie",
            },
            {
                "avatar": "https://images.pexels.com/photos/5327921/pexels-photo-5327921.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Chiara Moretti",
                "specialty":"Gynécologie",
            },
            {
                "avatar": "https://images.pexels.com/photos/6129507/pexels-photo-6129507.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Paolo Serra",
                "specialty":"Orthopédie",
            },
            {
                "avatar": "https://images.pexels.com/photos/7659562/pexels-photo-7659562.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Andrea Villa",
                "specialty":"Neurologie",
            },
            {
                "avatar": "https://images.pexels.com/photos/5215024/pexels-photo-5215024.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr Laura Bianchi",
                "specialty":"Ophtalmologie",
            },
        ],
        "team_footnote_prefix": "Plus de 40 spécialistes composent l'équipe médicale complète.",
        "team_footnote_link":   "Voir tous les praticiens",

        "partners_label":   "Conventions et assurances",
        "partners_heading": "Nous travaillons en réseau avec les principales caisses et assurances santé italiennes.",
        "partners": [
            "Inail", "Unisalute", "Generali Welion",
            "RBM Salute", "Previmedical", "Caspie",
            "MioDottore", "Consap",
        ],

        "cta_band": {
            "heading":      "Besoin d'une consultation cette semaine ?",
            "body":         "Réservez en ligne en 30 secondes ou composez notre numéro vert : notre équipe répond tous les jours de 7 h à 21 h.",
            "primary_cta":  "Réserver en ligne",
            "primary_href": "prenota",
            "secondary_cta":"Appeler le 800 123 456",
        },
    },

    "studio": {
        "eyebrow":   "Le centre · à Milan depuis 1998",
        "headline":  'Un point de référence <em>proche</em> des personnes.',
        "intro":
            "SaluteVita a été fondé en 1998 par trois médecins milanais "
            "avec une conviction : réduire la distance entre l'hôpital et "
            "la famille, en proposant un centre médical complet à deux pas "
            "de la gare de Milan Centrale.",

        "values_label":   "Nos valeurs",
        "values_heading": 'Quatre principes <em>qui ne changeront pas</em>.',
        "values": [
            {"title": "Pluridisciplinarité",
             "body":  "Aucun patient n'est renvoyé ailleurs : si un examen "
                      "s'impose, nous le programmons dans le même bâtiment. "
                      "Comptes rendus partagés entre les spécialistes."},
            {"title": "Accueil",
             "body":  "Notre secrétariat répond dès 7 h. Nous vous "
                      "appelons par votre nom — pas de numéro, pas "
                      "d'attente debout."},
            {"title": "Technologie au service du soin",
             "body":  "Dossier médical numérique, comptes rendus PDF "
                      "sous 24 heures, dermoscopie numérique et IRM 1,5 T "
                      "dernière génération."},
            {"title": "Continuité",
             "body":  "Si votre fille a vu notre pédiatre il y a trois "
                      "ans, l'orthopédiste retrouve aujourd'hui le même "
                      "dossier quand elle en a besoin. Sans repartir de zéro."},
        ],

        "photo_label":   "Le centre",
        "photo_heading": "Quatre étages, douze services, un seul secrétariat.",
        "photo_body":
            "Le bâtiment du 18 Via Galvani abrite cabinets de consultation, "
            "salle de prélèvements, imagerie médicale et kinésithérapie. "
            "Tout se situe au rez-de-chaussée ou au premier étage, "
            "entièrement accessible, avec un parking partenaire à 40 mètres.",
        "photo_caption": "Via Galvani 18 · quartier Milan Centrale",
        "photo_src":     "https://images.pexels.com/photos/7108324/pexels-photo-7108324.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",

        "timeline_label":   "Notre histoire",
        "timeline_heading": 'Vingt-six ans, <em>une seule constante</em> : la personne en face de nous.',
        "timeline": [
            {"year": "1998", "title": "Les débuts",
             "body": "Trois médecins — un interniste, une pédiatre et un "
                     "cardiologue — ouvrent le premier cabinet Via Galvani, "
                     "sur 180 m²."},
            {"year": "2008", "title": "Le deuxième étage",
             "body": "Nous inaugurons l'imagerie médicale avec IRM, "
                     "scanner et mammographie. Les services passent à huit."},
            {"year": "2018", "title": "Dossier numérique",
             "body": "Passage complet au dossier médical numérique et à "
                     "l'espace patient en ligne. Comptes rendus sous "
                     "24 heures pour chaque examen."},
            {"year": "2024", "title": "Aujourd'hui",
             "body": "Plus de 40 spécialistes, 12 services, "
                     "28 000 patients suivis chaque année. Nous restons "
                     "le centre de famille que nous avons voulu être."},
        ],

        "cta_band": {
            "heading":    "Envie de nous rencontrer sur place ?",
            "body":       "Prenez rendez-vous ou passez nous voir : la réception ouvre à 7 h, sans rendez-vous préalable.",
            "primary_cta":"Prendre rendez-vous",
            "secondary_cta": "Appeler le 800 123 456",
        },
    },

    "servizi": {
        "eyebrow":   "Services · 12 spécialités · 40+ praticiens",
        "headline":  'Toutes les consultations <em>dont une famille a besoin</em>.',
        "intro":
            "De la cardiologie à la kinésithérapie, en passant par la "
            "pédiatrie, la dermatologie et l'imagerie médicale. Chaque "
            "consultation est réservable en ligne, avec des tarifs clairs "
            "et des forfaits de prévention dédiés.",

        "svc_label":   "Tous nos services",
        "svc_heading": 'Consultations spécialisées, <em>tarifs transparents</em>.',
        "price_label": "Première consultation",
        "book_cta":    "Réserver",

        "services": [
            {
                "icon_svg": ICO_STETHOSCOPE,
                "eyebrow":  "Cardiologie",
                "title":    "Consultation cardiologique avec ECG",
                "desc":     "Anamnèse approfondie, auscultation, ECG à "
                            "12 dérivations, évaluation du risque "
                            "cardiovasculaire et orientation vers d'autres "
                            "examens si nécessaire.",
                "items":    ["ECG inclus", "Compte rendu le jour même", "40 min"],
                "price":    "140 €",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "eyebrow":  "Cardiologie",
                "title":    "Échocardiographie Doppler couleur",
                "desc":     "Évaluation morphologique et fonctionnelle du "
                            "cœur avec un échographe dernière génération. "
                            "Utile pour les souffles, l'hypertension et le "
                            "suivi post-événement.",
                "items":    ["Doppler inclus", "Compte rendu sous 24 h", "35 min"],
                "price":    "160 €",
            },
            {
                "icon_svg": ICO_BABY,
                "eyebrow":  "Pédiatrie",
                "title":    "Consultation pédiatrique 0–14 ans",
                "desc":     "Bilan de santé, croissance, développement "
                            "psychomoteur, alimentation. Conseil vaccinal "
                            "selon le calendrier régional sur demande.",
                "items":    ["0–14 ans", "Créneau urgent sous 24 h", "45 min"],
                "price":    "120 €",
            },
            {
                "icon_svg": ICO_DERM,
                "eyebrow":  "Dermatologie",
                "title":    "Cartographie des grains de beauté en dermoscopie numérique",
                "desc":     "Dépistage oncologique cutané au "
                            "vidéodermoscope. Images archivées pour "
                            "comparaison annuelle. Recommandé à partir de 30 ans.",
                "items":    ["Archive sur 5 ans", "Images numériques", "40 min"],
                "price":    "180 €",
            },
            {
                "icon_svg": ICO_WOMAN,
                "eyebrow":  "Gynécologie",
                "title":    "Consultation gynéco-obstétrique + échographie",
                "desc":     "Consultation complète avec échographie "
                            "endovaginale ou abdominale. Parcours dédiés "
                            "à la première grossesse et à la ménopause.",
                "items":    ["Frottis disponible", "Échographie incluse", "45 min"],
                "price":    "150 €",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "eyebrow":  "Radiologie",
                "title":    "IRM 1,5 T",
                "desc":     "Appareil ouvert dernière génération, adapté "
                            "également aux patients claustrophobes. "
                            "Compte rendu radiologique sous 24 heures ouvrées.",
                "items":    ["Ouverte · sans claustrophobie", "Compte rendu sous 24 h", "30 min"],
                "price":    "dès 220 €",
            },
            {
                "icon_svg": ICO_BONE,
                "eyebrow":  "Orthopédie",
                "title":    "Consultation orthopédique + échographie musculaire",
                "desc":     "Évaluation clinique et échographique en une "
                            "seule séance. Infiltrations écho-guidées "
                            "d'acide hyaluronique ou de corticoïde sur indication.",
                "items":    ["Échographie incluse", "Infiltrations disponibles", "40 min"],
                "price":    "150 €",
            },
            {
                "icon_svg": ICO_BONE,
                "eyebrow":  "Kinésithérapie",
                "title":    "Séance de kinésithérapie de rééducation",
                "desc":     "Parcours personnalisé avec un kinésithérapeute "
                            "dédié, sur prescription de l'orthopédiste ou du "
                            "médecin traitant. Forfaits de 5 et 10 séances.",
                "items":    ["Forfaits disponibles", "Post-chirurgie", "50 min"],
                "price":    "55 € · séance",
            },
            {
                "icon_svg": ICO_BRAIN,
                "eyebrow":  "Neurologie",
                "title":    "Consultation neurologique avec EEG",
                "desc":     "Bilan des céphalées, des troubles du sommeil "
                            "et des tremblements, avec possibilité "
                            "d'électroencéphalogramme dans la même séance. "
                            "Tests cognitifs sur demande.",
                "items":    ["EEG disponible", "Tests cognitifs", "50 min"],
                "price":    "170 €",
            },
            {
                "icon_svg": ICO_EYE,
                "eyebrow":  "Ophtalmologie",
                "title":    "Bilan ophtalmologique complet",
                "desc":     "Mesure de la vue, tonométrie, fond d'œil, "
                            "OCT de la rétine. Évaluation chirurgicale de "
                            "la cataracte en collaboration avec des centres conventionnés.",
                "items":    ["OCT inclus", "Tonométrie", "35 min"],
                "price":    "130 €",
            },
        ],

        "faq_label":   "Questions fréquentes",
        "faq_heading": 'Les <em>trois</em> questions qui reviennent le plus.',
        "faqs": [
            ("Puis-je utiliser mon assurance santé ou ma caisse d'entraide ?",
             "Oui. SaluteVita est conventionné avec Unisalute, Generali "
             "Welion, RBM Salute, Previmedical, Caspie et Consap. Dans la "
             "plupart des cas la caisse règle directement la prestation, "
             "sans avance de frais. Envoyez-nous votre carte au moment de "
             "la prise de rendez-vous : nous confirmons la prise en charge "
             "sous 24 heures."),
            ("Dans quels délais reçois-je mon compte rendu ?",
             "Consultations cliniques : compte rendu numérique dans "
             "votre espace patient sous 24 heures ouvrées. Imagerie "
             "médicale (échographie, scanner, IRM) : compte rendu "
             "radiologique sous 24 à 48 heures. Si vous en avez besoin "
             "le jour même, signalez-le au moment de la réservation — "
             "c'est presque toujours possible."),
            ("Puis-je annuler ou déplacer mon rendez-vous ?",
             "Bien sûr. Vous pouvez modifier ou annuler depuis votre "
             "espace patient jusqu'à 24 heures à l'avance, sans frais. "
             "En deçà, appelez notre numéro vert 800 123 456 : nous "
             "examinons chaque cas, sans pénalité pour motif médical."),
        ],

        "cta_band": {
            "heading":    "Choisissez la consultation, nous nous occupons du reste.",
            "body":       "Réservez en ligne en quelques secondes : si vous ne trouvez pas la spécialité recherchée, appelez notre numéro vert et nous vous orienterons.",
            "primary_cta":"Prendre rendez-vous",
            "secondary_cta":"Appeler le 800 123 456",
        },
    },

    "prevenzione": {
        "eyebrow":   "Prévention · trois parcours dédiés",
        "headline":  'Un bilan complet en <em>une demi-journée</em>.',
        "intro":
            "Trois forfaits pensés pour les tranches d'âge où le dépistage "
            "compte le plus : femme 40+, homme 45+, seniors 60+. Un "
            "interniste coordonne l'ensemble et vous remet un compte "
            "rendu unique sous 48 heures.",

        "pack_label":   "Les trois parcours",
        "pack_heading": 'Choisissez selon <em>l\'âge et le profil</em>.',
        "duration_label": "Durée",
        "exams_label":    "Examens",

        "packages": [
            {
                "eyebrow": "FEMME 40+",
                "title":   "Bilan Femme 40+",
                "desc":    "Pensé pour garder sous contrôle la santé "
                           "gynécologique, sénologique et métabolique en une seule matinée.",
                "price":   "320 €",
                "price_meta": "tout compris",
                "duration": "3 heures",
                "exams_count": "7 examens",
                "includes": [
                    "Consultation gynécologique avec échographie pelvienne",
                    "Frottis et test HPV",
                    "Mammographie bilatérale",
                    "Consultation nutritionnelle de 30 minutes",
                    "Bilan sanguin profil métabolique",
                    "Consultation sénologique de contrôle",
                    "Compte rendu unique sous 48 heures",
                ],
                "cta":      "Réserver le bilan",
                "is_popular": True,
                "popular_label": "Le plus demandé",
            },
            {
                "eyebrow": "HOMME 45+",
                "title":   "Bilan Homme 45+",
                "desc":    "Le dépistage que nous reportons tous et qu'il ne "
                           "faut jamais différer : cœur, prostate, métabolisme, foie.",
                "price":   "280 €",
                "price_meta": "tout compris",
                "duration": "3 h 30",
                "exams_count": "7 examens",
                "includes": [
                    "Consultation cardiologique avec ECG",
                    "Échocardiographie Doppler couleur",
                    "Consultation urologique avec PSA",
                    "Échographie abdominale complète",
                    "Profil lipidique et glycémique",
                    "Évaluation du risque cardiovasculaire",
                    "Compte rendu unique sous 48 heures",
                ],
                "cta":      "Réserver le bilan",
                "is_popular": False,
                "popular_label": "",
            },
            {
                "eyebrow": "SENIORS 60+",
                "title":   "Bilan Seniors",
                "desc":    "Un tableau complet coordonné par un interniste "
                           "qui fait le lien entre cœur, os, cerveau et yeux.",
                "price":   "420 €",
                "price_meta": "tout compris",
                "duration": "4 heures",
                "exams_count": "9 examens",
                "includes": [
                    "Cardiologie + échocardiographie + holter 24 h",
                    "Ostéodensitométrie DEXA",
                    "Consultation neurologique avec tests cognitifs",
                    "Consultation ophtalmologique avec OCT rétinien",
                    "Tonométrie et champ visuel",
                    "Profil métabolique complet",
                    "Consultation interniste de coordination",
                    "Entretien final avec le médecin référent",
                    "Compte rendu unique sous 48 heures",
                ],
                "cta":      "Réserver le bilan",
                "is_popular": False,
                "popular_label": "",
            },
        ],

        "how_label":   "Comment ça marche",
        "how_heading": 'Quatre étapes, <em>sans surprise</em>.',
        "how_steps": [
            {"num": "01", "title": "Réservez en ligne",
             "body": "Choisissez le bilan adapté et la date. Vous recevez "
                     "une confirmation par e-mail avec les consignes de préparation."},
            {"num": "02", "title": "À jeun le matin",
             "body": "Les analyses sanguines exigent 8 heures de jeûne. "
                     "De l'eau plate est autorisée jusqu'à une heure "
                     "avant l'arrivée."},
            {"num": "03", "title": "Une demi-matinée chez nous",
             "body": "Vous arrivez à 7 h 30 et repartez avant midi. Tous "
                     "les examens s'enchaînent, sans temps morts."},
            {"num": "04", "title": "Compte rendu unique sous 48 h",
             "body": "Le médecin coordinateur vous rappelle pour "
                     "commenter les résultats et vous remet le PDF récapitulatif."},
        ],

        "cta_band": {
            "heading":    "Un bilan par an pour mieux dormir la nuit.",
            "body":       "Réservez aujourd'hui : nous vous rappelons sous deux heures ouvrées pour confirmer la date et les consignes de préparation.",
            "primary_cta":"Réserver un bilan",
            "secondary_cta":"Appeler le 800 123 456",
        },
    },

    "medici": {
        "eyebrow":   "Médecins · 40+ spécialistes",
        "headline":  'L\'équipe qui <em>prendra soin de vous</em>.',
        "intro":
            "Voici les six praticiens qui dirigent nos services les plus "
            "demandés. L'équipe complète compte plus de 40 spécialistes : "
            "si vous cherchez quelqu'un en particulier, appelez le "
            "secrétariat — nous vous aidons à le trouver.",

        "book_cta": "Réserver avec ce praticien",

        "doctors": [
            {
                "portrait": "https://images.pexels.com/photos/5327585/pexels-photo-5327585.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Cardiologie · cheffe de service",
                "name":     "Dr Elisa Conti",
                "credentials":
                    "Spécialisation en cardiologie à l'Université de Milan. "
                    "22 ans de pratique clinique, formée au Centro "
                    "Cardiologico Monzino. Membre de la Société italienne "
                    "de cardiologie.",
                "tags": ["Cardiologie", "Échocardiographie", "Prévention CV"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5452293/pexels-photo-5452293.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Pédiatrie · chef de service",
                "name":     "Dr Marco Ferri",
                "credentials":
                    "Pédiatre de famille, spécialisation à la Clinique "
                    "De Marchi. 18 ans au service des familles milanaises, "
                    "avec un intérêt particulier pour la néonatologie et "
                    "les troubles respiratoires de l'enfance.",
                "tags": ["0–14 ans", "Vaccinations", "Pneumologie pédiatrique"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5452274/pexels-photo-5452274.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Dermatologie",
                "name":     "Dr Sofia Lenzi",
                "credentials":
                    "Dermatologue, spécialisation à l'Université "
                    "Vita-Salute San Raffaele. Dix ans d'expérience en "
                    "dermoscopie numérique et suivi oncologique cutané.",
                "tags": ["Dermoscopie", "Oncologie cutanée", "Acné"],
            },
            {
                "portrait": "https://images.pexels.com/photos/4173239/pexels-photo-4173239.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Radiologie · directeur de l'imagerie",
                "name":     "Dr Luca Russo",
                "credentials":
                    "Radiologue, 25 ans d'expérience hospitalière avant "
                    "de rejoindre SaluteVita en 2015. Référent IRM et "
                    "scanner, dirige une équipe de six manipulateurs.",
                "tags": ["IRM 1,5 T", "Scanner", "Échographie multi-organes"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5327921/pexels-photo-5327921.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Gynécologie · obstétrique",
                "name":     "Dr Chiara Moretti",
                "credentials":
                    "Gynécologue et sage-femme, spécialisation à la "
                    "Clinique Mangiagalli. Accompagne les grossesses "
                    "physiologiques, la ménopause et le dépistage "
                    "oncologique féminin.",
                "tags": ["Grossesse", "Ménopause", "Frottis + HPV"],
            },
            {
                "portrait": "https://images.pexels.com/photos/6129507/pexels-photo-6129507.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Orthopédie · médecine du sport",
                "name":     "Dr Paolo Serra",
                "credentials":
                    "Orthopédiste, spécialisation à l'Institut Galeazzi. "
                    "Expert en échographie musculo-squelettique et "
                    "infiltrations écho-guidées, suit des athlètes de "
                    "Serie A comme des sportifs amateurs.",
                "tags": ["Échographie musculaire", "Infiltrations", "Médecine du sport"],
            },
        ],

        "footnote_strong": "Plus de 40 spécialistes composent l'équipe médicale complète.",
        "footnote_body":
            "Neurologie, ophtalmologie, ORL, urologie, endocrinologie et "
            "sept autres spécialités. Contactez le secrétariat pour "
            "identifier le praticien adapté à votre demande : ",
        "footnote_link": "écrivez-nous depuis la page contact",
    },

    "contatti": {
        "eyebrow":   "Contact · Via Galvani 18 · Milan",
        "headline":  'Nous sommes <em>là où il faut</em> : à deux pas de Milan Centrale.',
        "intro":
            "La réception est ouverte de 7 h à 21 h, du lundi au "
            "vendredi. Écrivez-nous ou appelez : nous répondons sous "
            "deux heures ouvrées, sans répondeur automatique.",

        "map_aria":    "Carte illustrative du site SaluteVita, Via Galvani 18 à Milan",
        "map_stamp":   "Via Galvani 18 · Milan Centrale",

        "address_label": "Adresse",
        "email_label":   "E-mail",

        "hours_heading": "Horaires d'ouverture",
        "hours_table": [
            ("Lundi – Vendredi", "7 h 00 – 21 h 00"),
            ("Samedi",           "8 h 00 – 18 h 00"),
            ("Dimanche",         "Fermé"),
            ("Jours fériés",     "Fermé · numéro vert actif"),
        ],

        "access": [
            {"icon": "car",        "title": "Parking partenaire",
             "body": "Garage Centrale à 40 mètres. 2 €/heure pour les patients SaluteVita."},
            {"icon": "metro",      "title": "Métro",
             "body": "M2/M3 Milano Centrale · 4 minutes à pied. Tram 5 et 9 devant l'entrée."},
            {"icon": "wheelchair", "title": "Accès PMR",
             "body": "Entrée sans barrière, ascenseur, toilettes aménagées au rez-de-chaussée."},
            {"icon": "info",       "title": "Urgences",
             "body": "Nous ne sommes pas un service d'urgences. Pour toute urgence sanitaire, composez le 112."},
        ],

        "form_title": "Écrivez-nous un message",
        "form_intro":
            "Pour une question générale ou des informations avant de "
            "prendre rendez-vous, écrivez-nous ici. Nous répondons sous "
            "deux heures ouvrées.",

        "form_fields": [
            {"name": "nome",       "label": "Prénom",     "type": "text",     "placeholder": "Mario",                  "required": True},
            {"name": "cognome",    "label": "Nom",        "type": "text",     "placeholder": "Rossi",                  "required": True},
            {"name": "email",      "label": "E-mail",     "type": "email",    "placeholder": "mario.rossi@email.fr",   "required": True},
            {"name": "telefono",   "label": "Téléphone",  "type": "tel",      "placeholder": "+39 ...",                "required": False},
            {"name": "specialita", "label": "Spécialité d'intérêt", "type": "select", "required": False,
             "options": ["Cardiologie", "Pédiatrie", "Dermatologie", "Radiologie",
                         "Gynécologie", "Orthopédie", "Neurologie", "Ophtalmologie",
                         "Autre / informations générales"]},
            {"name": "oggetto",    "label": "Objet",      "type": "text",     "placeholder": "Informations prévention", "required": True},
            {"name": "messaggio",  "label": "Message",    "type": "textarea", "placeholder": "Expliquez brièvement votre besoin…",
             "required": True, "full_width": True,
             "helper": "Merci de ne pas transmettre de données médicales sensibles via ce formulaire : pour les comptes rendus, utilisez votre espace patient."},
        ],
        "consent":
            "Je consens au traitement de mes données personnelles conformément "
            "au Règlement UE 2016/679, dans le seul but de répondre à cette demande.",
        "submit_label": "Envoyer le message",
        "form_note":    "Réponse sous deux heures ouvrées",
    },

    "prenota": {
        "eyebrow":   "Rendez-vous · en ligne en 30 secondes",
        "headline":  'Dites-nous quand, <em>nous nous occupons du reste</em>.',
        "intro":
            "Complétez le formulaire ci-dessous : nous vous rappelons "
            "sous deux heures ouvrées pour confirmer la date, le "
            "praticien et la préparation. Si vous préférez parler à "
            "quelqu'un, composez le numéro vert 800 123 456.",

        "form_sections": [
            {"num": "01", "title": "Vos coordonnées", "meta": "pour vous recontacter",
             "fields": ["nome", "cognome", "email", "telefono", "data_nascita", "codice_fiscale"]},
            {"num": "02", "title": "Détails du rendez-vous", "meta": "type et spécialité",
             "fields": ["specialita", "medico_preferito", "tipo_visita", "convenzione"]},
            {"num": "03", "title": "Vos disponibilités", "meta": "nous rappelons pour confirmer",
             "fields": ["data_preferita", "fascia_orario", "note"]},
        ],

        "form_fields": [
            {"name": "nome",            "label": "Prénom",          "type": "text",  "placeholder": "Mario",                    "required": True},
            {"name": "cognome",         "label": "Nom",             "type": "text",  "placeholder": "Rossi",                    "required": True},
            {"name": "email",           "label": "E-mail",          "type": "email", "placeholder": "mario.rossi@email.fr",     "required": True,
             "helper": "Nous envoyons les SMS de rappel et le compte rendu numérique à cette adresse."},
            {"name": "telefono",        "label": "Téléphone",       "type": "tel",   "placeholder": "+39 335 ...",              "required": True},
            {"name": "data_nascita",    "label": "Date de naissance","type": "date", "placeholder": "jj/mm/aaaa",               "required": True},
            {"name": "codice_fiscale",  "label": "Codice fiscale (code fiscal italien)", "type": "text",  "placeholder": "RSSMRA80A01F205X", "required": False,
             "helper": "Utile si vous avez une convention : nous traitons plus vite votre dossier."},
            {"name": "specialita",      "label": "Spécialité",      "type": "select","required": True,
             "options": ["Cardiologie", "Pédiatrie", "Dermatologie",
                         "Radiologie & diagnostic", "Gynécologie",
                         "Orthopédie & kinésithérapie", "Neurologie", "Ophtalmologie",
                         "Bilan de prévention", "Autre spécialité"]},
            {"name": "medico_preferito","label": "Praticien souhaité","type": "select","required": False,
             "options": ["Sans préférence · premier disponible",
                         "Dr Elisa Conti · Cardiologie",
                         "Dr Marco Ferri · Pédiatrie",
                         "Dr Sofia Lenzi · Dermatologie",
                         "Dr Luca Russo · Radiologie",
                         "Dr Chiara Moretti · Gynécologie",
                         "Dr Paolo Serra · Orthopédie",
                         "Dr Andrea Villa · Neurologie",
                         "Dr Laura Bianchi · Ophtalmologie"]},
            {"name": "tipo_visita",     "label": "Type de consultation","type": "select","required": True,
             "options": ["Première consultation", "Consultation de suivi", "Examen diagnostique",
                         "Consultation urgente (sous 24–48 h)"]},
            {"name": "convenzione",     "label": "Utilisez-vous une convention ?", "type": "select", "required": False,
             "options": ["Aucune · règlement privé",
                         "Unisalute", "Generali Welion", "RBM Salute",
                         "Previmedical", "Caspie", "MioDottore", "Consap",
                         "Inail", "Autre assurance / caisse"]},
            {"name": "data_preferita",  "label": "Date souhaitée",  "type": "date",  "placeholder": "jj/mm/aaaa", "required": True,
             "helper": "Dans les 30 prochains jours. Si un créneau se libère plus tôt, nous vous prévenons."},
            {"name": "fascia_orario",   "label": "Tranche horaire", "type": "select","required": True,
             "options": ["Tôt le matin · 7 h 00 – 9 h 00",
                         "Matin · 9 h 00 – 12 h 00",
                         "Début d'après-midi · 13 h 00 – 16 h 00",
                         "Fin d'après-midi · 16 h 00 – 19 h 00",
                         "Soirée · 19 h 00 – 21 h 00",
                         "Sans préférence"]},
            {"name": "note",            "label": "Notes pour le praticien", "type": "textarea",
             "placeholder": "Indiquez d'éventuels symptômes, traitements en cours ou questions précises…",
             "required": False, "full_width": True,
             "helper": "Facultatif. Nous ne demandons que ce qui est utile au praticien pour se préparer."},
        ],

        "consent":
            "Je consens au traitement de mes données personnelles conformément "
            "au Règlement UE 2016/679 et à la notice d'information sanitaire "
            "de SaluteVita. Les données seront utilisées uniquement pour la "
            "gestion de ce rendez-vous.",
        "submit_label":     "Confirmer le rendez-vous",
        "form_submit_note": "Nous vous rappelons sous deux heures ouvrées",

        "help_title": "Comment fonctionne la prise de rendez-vous",
        "help_steps": [
            {"num": "1", "title": "Vous remplissez le formulaire",
             "body": "90 secondes suffisent. Aucun paiement à l'avance."},
            {"num": "2", "title": "Nous rappelons sous deux heures",
             "body": "Un membre du secrétariat confirme la date, le praticien et les consignes de préparation."},
            {"num": "3", "title": "Rappel SMS",
             "body": "Deux jours avant, vous recevez un SMS avec la date, l'heure et le cabinet."},
            {"num": "4", "title": "Compte rendu numérique",
             "body": "Sous 24 à 48 h, compte rendu et ordonnances arrivent dans votre espace patient, téléchargeables en PDF."},
        ],

        "alt_title": "Vous préférez parler à quelqu'un ?",
        "alt_body":
            "Le numéro vert est gratuit et actif 7 jours sur 7, de 7 h à 21 h. "
            "Nous décrochons en moyenne en moins de 40 secondes.",

        "trust": [
            "Données chiffrées de bout en bout (AES-256, norme sanitaire)",
            "Annulation ou report possible jusqu'à 24 h avant, sans frais",
            "Conventions avec 8 grandes assurances et caisses santé",
        ],
    },
}

__all__ = ["SALUTE_CONTENT_FR"]
