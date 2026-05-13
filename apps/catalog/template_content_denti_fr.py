"""Denti+Co — Studio Dentistico · French (FR) content tree.

Wave 1 Pass-2 (T46 · 2026-05-11) · workflow C multilingual rollout.
French (FR) locale tree authored by four parallel sub-agent translators
working in shape-parity with the canonical IT tree defined in
`template_content_denti.py` (`DENTI_CONTENT_IT`).

Mirror contract:
    DENTI_CONTENT_FR.keys() == DENTI_CONTENT_IT.keys()
Every nested key, every tuple arity, every dict shape preserved
verbatim. Only the visible strings are localised — page slugs stay
Italian (URLs do not change across locales).

Voice anchor — `igiene` → `hygiène`:
    The IT tree uses the noun-em `<em>igiene</em>` as the repeated
    editorial signature ("L'igiene non è un dettaglio", "Prenota
    igiene", "L'igiene è il primo capitolo"). The FR tree honours
    that voice anchor by surfacing `<em>hygiène</em>` in the SAME
    structural slots (hero headline, manifesto, signature visits
    intro, tabs body, CTA verbs) — verbatim-in-translation, never
    paraphrased away. The verb-em on the side-quote rail follows
    naturally from the noun anchor.

Tone register:
    `vous` formal · Parisian classical medical prose (Les Echos /
    Doctolib editorial sobriety, NOT bureaucratic, NOT Quebec).
    Espaces insécables ( ) before `:` `;` `!` `?` and around
    `«»` quotation marks per French typographic convention.

Non-localisable data preserved verbatim:
    · phone        +39 02 7770 4488
    · email        studio@denticostudio.it
    · address      Via Manzoni 18 · 20121 Milan ("Milano" → "Milan")
    · prices       € 95, € 220, € 1.850, …
    · doctor names Dr Chiara Vespa, Dr Riccardo Berti,
                   Dr Sofia Liccardi, Dr Andrea Carofiglio
                   (FR convention: "Dr" without dot, female form
                   conveyed by role copy rather than "Dr.ssa")
    · press        Il Dentista Moderno, Dental Tribune,
                   Bocca & Salute, Corriere Salute, Vanity Fair Italia
    · photo URLs   identical to IT (_CHIEF_PORTRAIT, _LEAD_IMAGE,
                   the three inline associate portraits, the studio
                   wide shot, the operatory close-up, the map fallback)
"""
from __future__ import annotations

from typing import Any


# Imagery URLs — verbatim from the IT tree per the T46 Pass-2 binding
# (one shared imagery pool across all locales).
_CHIEF_PORTRAIT = (
    "https://images.pexels.com/photos/4269363/pexels-photo-4269363.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_LEAD_IMAGE = (
    "https://images.pexels.com/photos/9062525/pexels-photo-9062525.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)


DENTI_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Cabinet",           "kind": "home"},
        {"slug": "studio",          "label": "Le Cabinet",        "kind": "about"},
        {"slug": "visite",          "label": "Soins",             "kind": "services"},
        {"slug": "medici",          "label": "Dentistes",         "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Publications",      "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contact",           "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Prendre rendez-vous", "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "D",
        "logo_word":    "Denti+Co",
        "tag":          "Cabinet dentaire associé · Milan Brera",
        "phone":        "+39 02 7770 4488",
        "email":        "studio@denticostudio.it",
        "address":      "Via Manzoni 18 · 20121 Milan",
        "hours_compact": "Lun – Ven · 8h30 – 19h30",
        "hours_footer_rows": [
            "Samedi · 9h00 – 13h00",
            "Dimanche · fermé",
        ],
        "license":      "Inscription OMCeO Milan 03 / 18742 · Directrice médicale Dr C. Vespa",
        "footer_intro":
            "Cabinet dentaire associé d'odontologie conservatrice, d'hygiène "
            "professionnelle et d'implantologie. Quatre praticiens, un seul "
            "dossier par patient.",
    },

    "home": {
        # Hero — editorial-magazine variant, identical to IT.
        "hero_variant": "editorial-magazine",
        "eyebrow":  "Odontologie · Milan Brera",
        "headline": "L'<em>hygiène</em> n'est pas un détail. C'est le premier chapitre.",
        "intro":
            "Hygiène professionnelle, soins conservateurs, implantologie et "
            "orthodontie transparente. Quatre dentistes associés, un seul "
            "dossier, contrôles semestriels inclus dans le forfait annuel.",
        "primary_cta":   "Prendre rendez-vous",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "Le cabinet",
        "secondary_href":"studio",

        # Three-fact band — dental-coded.
        "facts": [
            ("12", "années en cabinet associé"),
            ("3 400", "hygiènes et contrôles / an"),
            ("4", "dentistes spécialistes sur place"),
        ],

        # Manifesto with drop-cap.
        "manifesto_drop_cap": "L",
        "manifesto":
            "a santé bucco-dentaire ne se soigne pas deux fois par an : elle "
            "s'entretient tous les jours. C'est pourquoi Denti+Co travaille "
            "à partir de l'hygiène — professionnelle, reproductible, "
            "mesurable — et construit autour d'elle les soins conservateurs, "
            "l'implantologie et l'orthodontie. Quatre dentistes spécialistes, "
            "un seul dossier clinique partagé, une seule signature au plan de "
            "traitement. Aucun upselling, aucun soin fragmenté : l'hygiène "
            "est le premier chapitre et le seul véritable point de passage.",

        # Hero right sidebar — preserved for editorial-magazine pulse rail.
        "hero_sidebar_top_label": "Direction médicale",
        "hero_sidebar_quote":
            "« Une hygiène professionnelle bien menée évite 70 % des soins "
            "invasifs. Pour nous, c'est de la clinique sérieuse, pas un "
            "service cosmétique. »",
        "hero_sidebar_author": "— Dr Chiara Vespa · Directrice médicale",
        "hero_sidebar_pulse": [
            ("Cabinet",   "Milan · Brera"),
            ("Depuis",    "2013"),
            ("Référence", "Odontologie associée"),
        ],

        # Anchor subnav.
        "anchor_nav": [
            ("metodo",        "Méthode"),
            ("trattamenti",   "Soins"),
            ("percorso",      "Parcours patient"),
            ("medico",        "Direction médicale"),
            ("studio",        "Adresse & contact"),
        ],

        # Signature treatments — numbered 01-04.
        "signature_visits_label":   "Soins & parcours",
        "signature_visits_heading": "Quatre parcours cliniques, <em>un seul dossier.</em>",
        "signature_visits_intro":
            "Les quatre familles d'intervention les plus demandées. "
            "La liste complète figure dans la page Soins.",
        "signature_visits": [
            ("01", "Hygiène professionnelle semestrielle",
             "Détartrage sus et sous-gingival, aéropolissage au "
             "bicarbonate de sodium, indice de saignement et "
             "cartographie PSR. Inclus dans les forfaits annuels "
             "de maintenance."),
            ("02", "Odontologie conservatrice",
             "Obturations en composite stratifié, reconstructions "
             "esthétiques, dévitalisations au localisateur apical. "
             "Digue en caoutchouc obligatoire sur chaque intervention "
             "conservatrice."),
            ("03", "Implantologie & régénération",
             "Implants unitaires et réhabilitations complètes à "
             "mise en charge immédiate. Planification assistée par "
             "ordinateur et guide chirurgical imprimé en 3D au "
             "laboratoire interne."),
            ("04", "Orthodontie transparente",
             "Gouttières transparentes Invisalign et SmileLab pour "
             "adultes, orthodontie interceptive 8-12 ans avec "
             "appareils amovibles. Suivi mensuel inclus."),
        ],

        # Trattamenti tabs section.
        "trattamenti_tabs": {
            "label":   "Tarifs des soins",
            "heading": "Ce que nous faisons, <em>selon quels critères.</em>",
            "intro":
                "Quatre catégories cliniques, chacune avec un protocole "
                "écrit et un coût annoncé. Aucun devis personnalisé pour "
                "les actes de routine — seulement pour les plans de "
                "traitement structurés.",
            "tabs": [
                {
                    "id":      "igiene",
                    "label":   "Hygiène",
                    "eyebrow": "Hygiène professionnelle",
                    "heading": "Quarante-cinq minutes, pas vingt.",
                    "body":
                        "L'hygiène n'est pas un rendez-vous de routine : "
                        "c'est une consultation clinique de quarante-cinq "
                        "minutes avec charting parodontal, indice de "
                        "saignement, aéropolissage au bicarbonate et "
                        "photographies de contrôle.",
                    "items": [
                        ("Hygiène professionnelle, séance unique", "45 min · € 95"),
                        ("Forfait annuel (2 hygiènes + 1 contrôle)", "annuel · € 220"),
                        ("Aéropolissage au bicarbonate", "inclus · gratuit"),
                        ("Scellement des sillons (par dent)", "10 min · € 30"),
                    ],
                    "cta_label": "Tous les forfaits d'hygiène →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "conservativa",
                    "label":   "Conservateur",
                    "eyebrow": "Odontologie conservatrice",
                    "heading": "Composite stratifié, toujours sous digue.",
                    "body":
                        "Obturations en composite photopolymérisé, "
                        "reconstructions esthétiques, dévitalisations au "
                        "localisateur apical. Digue en caoutchouc "
                        "obligatoire sur chaque intervention conservatrice. "
                        "Aucune obturation à l'amalgame depuis 2013.",
                    "items": [
                        ("Obturation simple (1 face)", "45 min · € 140"),
                        ("Obturation composée (2-3 faces)", "60 min · € 220"),
                        ("Dévitalisation mono-radiculaire", "75 min · € 280"),
                        ("Dévitalisation pluri-radiculaire", "120 min · € 420"),
                    ],
                    "cta_label": "Tarifs conservateurs complets →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "implantologia",
                    "label":   "Implantologie",
                    "eyebrow": "Implantologie & régénération",
                    "heading": "Implants italiens, garantie à vie sur le pilier.",
                    "body":
                        "Implants Sweden+Martina de provenance italienne, "
                        "planification assistée par ordinateur avec cône "
                        "beam, guide chirurgical imprimé en 3D au "
                        "laboratoire interne. Mise en charge immédiate "
                        "réservée à certains cas après évaluation clinique.",
                    "items": [
                        ("Implant unitaire (pilier + couronne zircone)", "intervention · € 1 850"),
                        ("Mini-élévation du sinus maxillaire", "intervention · € 950"),
                        ("Régénération osseuse (zone unique)", "intervention · € 480"),
                        ("Réhabilitation fixe sur 4 implants", "plan · sur devis"),
                    ],
                    "cta_label": "Parcours implantaires →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "ortodonzia",
                    "label":   "Orthodontie",
                    "eyebrow": "Orthodontie transparente & interceptive",
                    "heading": "Gouttières pour adultes, interceptive pour les enfants.",
                    "body":
                        "Gouttières transparentes Invisalign et SmileLab "
                        "avec scan intra-oral iTero et plan simulé en 3D "
                        "avant de commencer. Orthodontie interceptive "
                        "8-12 ans avec appareils amovibles. Suivi mensuel "
                        "inclus dans le forfait.",
                    "items": [
                        ("Gouttières Invisalign — plan complet", "12-18 mois · € 3 200"),
                        ("Gouttières SmileLab — plan complet", "10-14 mois · € 2 400"),
                        ("Orthodontie interceptive enfant", "12-24 mois · € 1 600"),
                        ("Contention nocturne post-traitement", "permanente · € 220"),
                    ],
                    "cta_label": "Protocoles orthodontiques →",
                    "cta_href":  "visite",
                },
            ],
        },

        "chief_label":   "Direction médicale",
        "chief_heading": "Une seule signature <em>pour chaque dossier.</em>",
        "chief": {
            "name":  "Dr Chiara Vespa",
            "role":  "Directrice médicale · Odontologie conservatrice & endodontie",
            "bio":
                "Spécialiste en odontologie conservatrice formée à "
                "l'Università degli Studi di Milano et perfectionnée à "
                "la Loma Linda University en Californie. Membre de la "
                "SIE (Société italienne d'endodontie) et conférencière "
                "aux cours annuels de la Scuola Lombarda di Odontoiatria. "
                "Directrice médicale du cabinet depuis 2013.",
            "portrait": _CHIEF_PORTRAIT,
        },

        # Patient journey — five steps.
        "percorso": {
            "label":   "Parcours patient",
            "heading": "À quoi vous attendre lors de la <em>première consultation.</em>",
            "intro":
                "La première consultation au cabinet est consacrée à la "
                "constitution du dossier clinique : photographies, indices, "
                "scan et plan de traitement écrit. Jamais de soin dès la "
                "première séance — sauf urgence documentée.",
            "steps": [
                {
                    "num": "01",
                    "icon": "clipboard",
                    "title": "Accueil & anamnèse",
                    "desc": "Secrétariat, fiche d'anamnèse avec antécédents "
                            "médicaux et dentaires, éventuelles radiographies "
                            "antérieures ou panoramique récente.",
                    "duration": "10 min",
                },
                {
                    "num": "02",
                    "icon": "book",
                    "title": "Examen clinique complet",
                    "desc": "Charting parodontal, indice de plaque, indice "
                            "de saignement, examen objectif des tissus mous "
                            "et des muqueuses orales.",
                    "duration": "20 min",
                },
                {
                    "num": "03",
                    "icon": "heart",
                    "title": "Photographie & scan",
                    "desc": "Bilan photographique standardisé (8 clichés "
                            "intra-oraux + 4 extra-oraux), scan intra-oral "
                            "iTero pour l'archive numérique.",
                    "duration": "15 min",
                },
                {
                    "num": "04",
                    "icon": "chart",
                    "title": "Plan de traitement écrit",
                    "desc": "Discussion au fauteuil du plan clinique avec "
                            "devis détaillé poste par poste, remise "
                            "également au format PDF.",
                    "duration": "15 min",
                },
                {
                    "num": "05",
                    "icon": "document",
                    "title": "Programmation & suivi",
                    "desc": "Calendrier des rendez-vous, éventuel rappel "
                            "pour l'hygiène de maintenance, canal direct "
                            "WhatsApp pour les urgences.",
                    "duration": "5 min",
                },
            ],
        },

        # Press strip — outlets remain in original Italian script.
        "press": ["Il Dentista Moderno", "Dental Tribune", "Bocca & Salute",
                  "Corriere Salute", "Vanity Fair Italia"],
        "press_label": "Parutions presse",

        # FAQ.
        "faq": {
            "label": "Questions fréquentes",
            "heading": "Les questions <em>que vous nous posez le plus souvent.</em>",
            "items": [
                ("À quelle fréquence une séance d'hygiène est-elle nécessaire ?",
                 "Pour les patients sans pathologie parodontale avérée, le "
                 "rythme est semestriel. Pour celles et ceux qui présentent "
                 "une gingivite, une parodontite ou qui portent un appareil "
                 "orthodontique, il descend à trois ou quatre mois. Le plan "
                 "est personnalisé après la première consultation."),
                ("Les obturations en composite durent-elles vraiment ?",
                 "Oui, à condition que la cavité soit reconstruite sous "
                 "digue en caoutchouc avec un composite stratifié et une "
                 "lampe à photopolymériser qualifiée. Nos obturations ont "
                 "une longévité moyenne de dix ans avec des contrôles "
                 "réguliers. Nous n'utilisons plus d'amalgame depuis 2013."),
                ("Combien coûte réellement un implant ?",
                 "L'implant unitaire (pilier en titane Sweden+Martina + "
                 "couronne en zircone) est à € 1 850, TVA incluse. Les "
                 "éventuelles interventions régénératives préalables "
                 "(élévation du sinus, ROG) sont exclues et ne sont "
                 "chiffrées qu'après cône beam."),
                ("L'orthodontie transparente fonctionne-t-elle vraiment chez l'adulte ?",
                 "Dans quatre-vingt-dix pour cent des cas cliniques "
                 "adultes, les gouttières transparentes (Invisalign ou "
                 "SmileLab) sont aussi efficaces que l'appareil fixe "
                 "traditionnel. Les cas qui requièrent encore l'appareil "
                 "fixe — rotations sévères des prémolaires, égressions "
                 "marquées — sont discutés ouvertement au moment du plan."),
                ("Puis-je amener mes enfants dans le même cabinet ?",
                 "Oui. Le Dr Liccardi s'occupe de l'orthodontie "
                 "interceptive 8-12 ans avec des appareils amovibles. "
                 "L'hygiène pédiatrique est incluse pour les enfants des "
                 "patients disposant d'un forfait annuel actif."),
            ],
        },

        # Bottom CTA band.
        "cta_heading":
            "Chaque plan de traitement est <em>écrit, annoncé, partagé.</em>",
        "cta_primary_label":   "Prendre rendez-vous",
        "cta_secondary_label": "Contact du cabinet",

        # Sede / Location — Milan Brera.
        "location": {
            "label":   "Adresse du cabinet",
            "heading": "Via Manzoni 18, <em>Milan.</em>",
            "intro":
                "Le cabinet occupe le piano nobile d'un palais historique "
                "du quartier Brera, à cent vingt mètres de Montenapoleone. "
                "Quatre salles de soins, salle de radiologie cône beam, "
                "laboratoire orthodontique interne.",
            "map_image": "",
            "map_fallback_image":
                "https://images.pexels.com/photos/305567/pexels-photo-305567.jpeg"
                "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
            "details": [
                ("Adresse",
                 "Via Manzoni 18\n20121 Milan"),
                ("Métro",
                 "M3 Montenapoleone\n3 minutes à pied"),
                ("Stationnement",
                 "Parking conventionné\nVia Bigli, à 50 mètres"),
                ("Accessibilité",
                 "Entrée accessible avec ascenseur\njusqu'au piano nobile"),
            ],
            "hours_short": [
                ("Lun – Ven", "8h30 – 19h30"),
                ("Samedi",    "9h00 – 13h00"),
                ("Dimanche",  "Fermé"),
            ],
            "cta_label": "Obtenir l'itinéraire",
            "cta_href":  "contatti",
        },
    },

    # ─── STUDIO (about) ─────────────────────────────────────────────
    "studio": {
        "eyebrow":   "Le cabinet · Milan Brera",
        "headline":  "Quatre dentistes, <em>un seul dossier.</em>",
        "intro":
            "Denti+Co est un cabinet associé fondé en 2013 par quatre "
            "praticiens qui partagent le même dossier clinique et le "
            "même protocole de travail : photographies avant et après, "
            "digue en caoutchouc toujours, devis écrit remis également "
            "en PDF, suivi programmé.",
        # 5-row history timeline.
        "history": [
            ("2013",
             "Fondation du cabinet associé Via Manzoni avec deux "
             "spécialistes et une seule salle opératoire."),
            ("2016",
             "Lancement du pôle implantologique avec cône beam "
             "Carestream CS 9600 et salle chirurgicale dédiée."),
            ("2019",
             "Adoption du scan intra-oral iTero et des plans "
             "orthodontiques simulés en 3D avant traitement."),
            ("2022",
             "Ouverture du laboratoire orthodontique interne avec "
             "impression 3D de guides chirurgicaux et de contentions "
             "nocturnes."),
            ("2025",
             "Le cabinet clôt l'année avec quatre associés à temps "
             "plein et une équipe de six hygiénistes."),
        ],
        "studio_image":
            "https://images.pexels.com/photos/4269268/pexels-photo-4269268.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop",
        "studio_image_caption": "Salle opératoire · Via Manzoni 18",
        "method_title": "La méthode Denti+Co",
        "method_paragraphs": [
            "L'hygiène est le premier chapitre parce qu'elle est aussi le "
            "plus reproductible. Presque personne n'entre au cabinet pour "
            "la première fois avec la bouche en ordre : pour la plupart "
            "des patients, il faut remettre la base en place avant de "
            "parler d'esthétique, d'orthodontie ou d'implantologie. "
            "Quarante minutes d'hygiène professionnelle bien menée "
            "changent la perspective sur le devis de toutes les "
            "interventions suivantes.",
            "Le dossier clinique est unique — le même pour les quatre "
            "associés — parce qu'un patient n'est pas le patient d'un "
            "dentiste isolé, c'est le patient du cabinet. Quand "
            "l'hygiéniste relève une récession gingivale lors d'un "
            "rappel, elle le signale au parodontiste dans le même "
            "document clinique. Aucun soin fragmenté.",
            "Les coûts sont annoncés pour les actes de routine (hygiène, "
            "conservateur, blanchiment, contrôle). Pour les plans plus "
            "structurés — implantologie avec régénération, orthodontie "
            "complexe, réhabilitations totales — le devis est "
            "personnalisé après une première consultation de soixante-dix "
            "minutes, mais toujours remis par écrit et signé en bas de "
            "page.",
        ],
        "values_label":   "Valeurs du cabinet",
        "values_heading": "Quatre engagements, <em>écrits au dossier.</em>",
        "values": [
            ("Digue en caoutchouc toujours",
             "Sur chaque intervention de conservateur, d'endodontie et "
             "d'application de composites. Sans exception."),
            ("Photos avant et après",
             "Bilan photographique standardisé remis au patient au "
             "format numérique à la fin de chaque plan de traitement."),
            ("Devis écrit",
             "Jamais un coût discuté uniquement à l'oral. PDF transmis "
             "par e-mail ou remis au cabinet avant le début des soins."),
            ("Suivi programmé",
             "Calendrier des rendez-vous de maintenance envoyé "
             "également par SMS ou WhatsApp. Aucun patient laissé "
             "à lui-même après l'intervention."),
        ],
        "cta_heading":
            "Le premier pas est toujours <em>une consultation de soixante-dix minutes.</em>",
        "cta_primary_label":   "Rencontrer les dentistes",
        "cta_secondary_label": "Réserver la première consultation",
        "press_label": "Parutions presse",
        "press": ["Il Dentista Moderno", "Dental Tribune",
                  "Bocca & Salute", "Corriere Salute"],
    },

    # ─── VISITE (services) ──────────────────────────────────────────
    "visite": {
        "eyebrow":  "Soins · tarifs 2026",
        "headline": "Ce que nous faisons, <em>ce que cela coûte, ce que nous garantissons.</em>",
        "intro":
            "Le tarif complet pour les actes de routine. Les plans de "
            "traitement structurés (implantologie complexe, orthodontie, "
            "réhabilitations totales) font toujours l'objet d'un devis "
            "personnalisé après la première consultation.",
        "service_image":
            "https://images.pexels.com/photos/6502543/pexels-photo-6502543.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop",
        "service_image_caption": "Salle opératoire · instrumentation et laboratoire interne",
        "treatments": [
            ("Hygiène professionnelle, séance unique",
             "45 min · sans prescription du médecin traitant",
             "Charting parodontal, indice de saignement, aéropolissage au "
             "bicarbonate de sodium, photographies de contrôle. Comprend "
             "l'analyse des habitudes d'hygiène à domicile avec éventuelle "
             "remise d'une brosse à dents sonique en essai.",
             "€ 95"),
            ("Forfait annuel de maintenance",
             "annuel · 2 hygiènes + 1 contrôle + radiographies rétro-alvéolaires",
             "Deux hygiènes semestrielles calendarisées, une consultation "
             "de contrôle avec photographies, radiographies "
             "rétro-alvéolaires lorsqu'indiquées. Canal direct WhatsApp "
             "pour les urgences.",
             "€ 220"),
            ("Obturation conservatrice (1 face)",
             "45 min · composite stratifié sous digue en caoutchouc",
             "Composite de marque Tokuyama ou 3M, toujours sous digue en "
             "caoutchouc, photopolymérisation LED qualifiée. Garantie "
             "d'étanchéité cinq ans avec contrôles réguliers.",
             "€ 140"),
            ("Dévitalisation mono-radiculaire",
             "75 min · localisateur apical + obturation thermoplastique",
             "Endodontie au localisateur apical Morita, obturation "
             "tridimensionnelle à la gutta-percha thermoplastique, "
             "reconstitution coronaire en composite. Contrôle "
             "radiographique à six et douze mois.",
             "€ 280"),
            ("Implant unitaire (pilier + couronne zircone)",
             "intervention + 2 contrôles · garantie à vie sur le pilier",
             "Implant italien Sweden+Martina, pilier en zircone "
             "stabilisée, couronne monolithique fraisée au laboratoire "
             "interne. Cône beam préalable inclus.",
             "€ 1 850"),
            ("Gouttières Invisalign (plan complet)",
             "12-18 mois · scan iTero + plan 3D + contention",
             "Scan intra-oral iTero, plan simulé en 3D remis au patient "
             "avant de commencer. Gouttières livrées par étapes. "
             "Contention nocturne post-traitement incluse.",
             "€ 3 200"),
            ("Blanchiment professionnel au fauteuil",
             "60 min · peroxyde à 35 % + gel barrière gingival",
             "Une séance de soixante minutes avec peroxyde d'hydrogène à "
             "35 %, gel barrière gingival photodurcissable, contrôle du "
             "pH salivaire avant et après traitement.",
             "€ 380"),
            ("Première consultation (dossier + plan)",
             "70 min · anamnèse + scan iTero + plan en PDF",
             "Anamnèse médicale et dentaire, examen objectif, charting "
             "parodontal, scan intra-oral, photographies, remise du plan "
             "clinique en PDF. Coût déduit du premier soin.",
             "€ 80"),
        ],
        "footnote_heading": "Ce qui n'est PAS inclus dans le tarif",
        "footnote":
            "Les actes de routine ci-dessus sont annoncés. Les plans de "
            "traitement structurés (réhabilitations totales, implantologie "
            "avec régénération étendue, orthodontie avec chirurgie "
            "orthognatique) font l'objet d'un devis personnalisé après la "
            "première consultation de soixante-dix minutes. Aucun devis "
            "n'est jamais transmis par téléphone ou par e-mail avant une "
            "consultation clinique.",
        "cta_heading":
            "Le devis est toujours <em>écrit, signé, remis en PDF.</em>",
        "cta_primary_label":   "Réserver la première consultation",
        "cta_secondary_label": "Nous écrire",
    },

    # ─── MEDICI (team) ──────────────────────────────────────────────
    "medici": {
        "eyebrow":  "Les dentistes · équipe associée",
        "headline": "Quatre signatures, <em>un seul dossier.</em>",
        "intro":
            "Les quatre associés partagent le même dossier clinique et se "
            "consultent sur les plans complexes. Pour chaque patient, un "
            "dentiste référent est désigné, mais l'hygiène de maintenance "
            "peut être réalisée par n'importe quel membre de l'équipe.",
        "doctors": [
            {
                "name":  "Dr Chiara Vespa",
                "role":  "Directrice médicale · Conservateur & endodontie",
                "bio":
                    "Spécialiste en odontologie conservatrice formée à "
                    "l'Università degli Studi di Milano et perfectionnée "
                    "à la Loma Linda University. Membre SIE (Société "
                    "italienne d'endodontie). Coordinatrice clinique du "
                    "cabinet depuis 2013.",
                "portrait": _CHIEF_PORTRAIT,
            },
            {
                "name":  "Dr Riccardo Berti",
                "role":  "Implantologie & régénération",
                "bio":
                    "Implantologue formé à la New York University College "
                    "of Dentistry et perfectionné en gnathologie clinique "
                    "à l'Università di Pavia. Il prend en charge "
                    "l'implantologie guidée par ordinateur, les "
                    "réhabilitations complexes et la régénération osseuse.",
                "portrait":
                    "https://images.pexels.com/photos/6627850/pexels-photo-6627850.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
            {
                "name":  "Dr Sofia Liccardi",
                "role":  "Orthodontie & odontologie pédiatrique",
                "bio":
                    "Spécialiste en orthopédie dento-faciale formée à "
                    "l'Università Cattolica del Sacro Cuore. Certifiée "
                    "Invisalign Diamond Provider. Elle prend en charge "
                    "l'orthodontie adulte, l'interceptive enfant et le "
                    "suivi du patient pédiatrique jusqu'à seize ans.",
                "portrait":
                    "https://images.pexels.com/photos/4687404/pexels-photo-4687404.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
            {
                "name":  "Dr Andrea Carofiglio",
                "role":  "Parodontologie & médecine orale",
                "bio":
                    "Parodontiste formé à l'Università degli Studi di "
                    "Bologna et perfectionné à l'Université de Berne. "
                    "Membre SIdP (Société italienne de parodontologie et "
                    "d'implantologie). Il prend en charge la parodontite "
                    "chronique et la médecine orale.",
                "portrait":
                    "https://images.pexels.com/photos/6529057/pexels-photo-6529057.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
        ],
        "portrait_city": "Milan · Brera",
    },

    # ─── PUBBLICAZIONI (blog_list) ──────────────────────────────────
    "pubblicazioni": {
        "eyebrow":  "Publications & vulgarisation",
        "headline": "Ce que nous avons écrit, <em>pour qui.</em>",
        "intro":
            "Articles de vulgarisation publiés dans des revues "
            "spécialisées et contributions cliniques à des revues "
            "scientifiques. Tous les contenus sont relus personnellement "
            "par le Dr Vespa avant publication.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Denti+Co · Cabinet dentaire associé · Milan",
        "empty_body_fallback_paragraphs": [
            "Article en préparation éditoriale. La publication intégrale "
            "sera disponible prochainement.",
            "Cette réserve décrit la voix de l'article : une note "
            "clinique rédigée par le praticien, sur un ton direct et "
            "dépourvu de jargon, pensée pour les patients qui souhaitent "
            "une information fiable sur leur santé bucco-dentaire.",
        ],
    },

    # Posts list — top-level sibling.
    "posts": [
        {
            "slug":     "igiene-professionale-perche-semestrale",
            "kicker":   "Hygiène & prévention",
            "title":    "Hygiène professionnelle : pourquoi la cadence semestrielle est un choix clinique",
            "date":     "12 mars 2025",
            "read_min": 8,
            "author":   "Dr Chiara Vespa",
            "lede":
                "La littérature clinique soutient une cadence d'hygiène "
                "personnalisée, mais la règle des six mois reste le "
                "meilleur compromis entre coût, adhésion du patient et "
                "résultat parodontal à long terme.",
        },
        {
            "slug":     "impianti-carico-immediato-quando",
            "kicker":   "Implantologie",
            "title":    "Mise en charge immédiate en implantologie : quand est-elle vraiment indiquée",
            "date":     "23 janvier 2025",
            "read_min": 12,
            "author":   "Dr Riccardo Berti",
            "lede":
                "La mise en charge immédiate séduit par un temps de "
                "traitement raccourci, mais elle n'est pas la solution "
                "universelle. Les critères de sélection du patient sont "
                "restrictifs et doivent être exposés ouvertement avant "
                "l'intervention.",
        },
        {
            "slug":     "allineatori-trasparenti-cosa-non-fanno",
            "kicker":   "Orthodontie",
            "title":    "Gouttières transparentes : trois choses qu'elles ne font pas",
            "date":     "5 novembre 2024",
            "read_min": 6,
            "author":   "Dr Sofia Liccardi",
            "lede":
                "Elles sont efficaces chez la plupart des adultes, mais "
                "elles ne résolvent pas tout. Trois limites cliniques "
                "honnêtes que chaque patient devrait connaître avant de "
                "se lancer dans le plan.",
        },
        {
            "slug":     "parodontite-non-e-solo-gengivite",
            "kicker":   "Parodontologie",
            "title":    "La parodontite n'est pas seulement « des gencives qui saignent »",
            "date":     "18 septembre 2024",
            "read_min": 5,
            "author":   "Dr Andrea Carofiglio",
            "lede":
                "La parodontite chronique touche un adulte sur deux après "
                "trente-cinq ans, mais le diagnostic arrive tard car les "
                "signaux initiaux sont silencieux. Trois indices "
                "parodontaux que tout patient peut demander à son "
                "dentiste.",
        },
    ],

    # ─── CONTATTI (contact) ─────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contact & adresse",
        "headline": "Écrivez-nous, <em>nous vous rappelons dans la journée.</em>",
        "intro":
            "Pour réserver une première consultation ou une hygiène de "
            "maintenance, vous pouvez nous appeler, nous écrire sur "
            "WhatsApp ou remplir le formulaire ci-dessous. Nous "
            "répondons dans la journée ouvrée.",
        # 4 info-blocks: (label, value, sub).
        "blocks": [
            ("Adresse",
             "Via Manzoni 18\n20121 Milan",
             "Piano nobile · entrée indépendante"),
            ("Téléphone",
             "+39 02 7770 4488",
             "Réponse dans la journée ouvrée"),
            ("E-mail",
             "studio@denticostudio.it",
             "Pour les demandes non urgentes"),
            ("Horaires",
             "Lun – Ven · 8h30 – 19h30\nSam · 9h00 – 13h00",
             "Dimanche fermé"),
        ],
        "form_title": "Écrivez-nous, nous vous rappelons dans la journée.",
        "form_intro":
            "Formulaire pour les demandes d'information ou pour fixer la "
            "première consultation. Pour les urgences cliniques, "
            "appelez-nous directement.",
        "form_placeholders": {
            "first_name": "Marie",
            "last_name":  "Bernard",
            "email":      "marie.bernard@email.fr",
            "phone":      "+33 6 12 34 56 78",
            "subject":    "Première consultation / hygiène / urgence",
            "message":    "Indiquez la plage horaire préférée et un éventuel dentiste référent.",
        },
        "form_helpers": {},
        "form_consent":
            "Je consens au traitement de mes données personnelles à la "
            "seule fin d'être recontacté par le cabinet. RGPD Art. 6 · "
            "DPO joignable à dpo@denticostudio.it.",
        "form_submit_note":
            "Réponse dans la journée ouvrée suivante.",
        "hours_heading":    "Horaires d'ouverture",
        # 3-tuples (day, am, pm).
        "hours": [
            ("Lundi",    "8h30 – 13h00", "14h00 – 19h30"),
            ("Mardi",    "8h30 – 13h00", "14h00 – 19h30"),
            ("Mercredi", "8h30 – 13h00", "14h00 – 19h30"),
            ("Jeudi",    "8h30 – 13h00", "14h00 – 19h30"),
            ("Vendredi", "8h30 – 13h00", "14h00 – 19h30"),
            ("Samedi",   "9h00 – 13h00", "—"),
            ("Dimanche", "—", "Fermé"),
        ],
        "transport_heading": "Comment nous rejoindre",
        # 2-tuples (label, text).
        "transport": [
            ("Métro",         "M3 Montenapoleone · 3 minutes à pied"),
            ("Tramway",       "Ligne 1 · arrêt Manzoni"),
            ("Train",         "Gare Centrale · 12 minutes en M3"),
            ("Stationnement", "Parking Via Bigli · 50 mètres · conventionné"),
        ],
    },

    # ─── RICHIEDI-VISITA (appointment) ──────────────────────────────
    "richiedi-visita": {
        "eyebrow":  "Prendre rendez-vous · première consultation",
        "headline": "Réservez, <em>nous vous recontactons sous 24 heures.</em>",
        "intro":
            "Remplissez le formulaire : le secrétariat fixe le premier "
            "rendez-vous dans la journée ouvrée suivante et vous confirme "
            "également par SMS ou WhatsApp.",
        "process_label":   "Le parcours de réservation",
        "process_heading": "Du formulaire au premier <em>rendez-vous</em>, en quatre étapes.",
        # 4 process steps (num, title, blurb).
        "process": [
            ("01", "Formulaire & rappel",
             "Le secrétariat reçoit le formulaire, vérifie que toutes "
             "les informations nécessaires sont présentes, et vous "
             "rappelle dans la journée ouvrée suivante pour fixer le "
             "rendez-vous."),
            ("02", "Confirmation & rappel",
             "Vous recevrez la confirmation par SMS ou WhatsApp avec "
             "la date, l'heure, le dentiste référent, l'adresse du "
             "cabinet et l'itinéraire."),
            ("03", "Première consultation de 70 minutes",
             "Anamnèse, examen clinique complet, scan iTero, "
             "photographies intra-orales et extra-orales, charting "
             "parodontal, remise du plan clinique en PDF."),
            ("04", "Plan écrit",
             "Discussion du plan au fauteuil avec devis poste par "
             "poste. Le coût de la première consultation est déduit "
             "du premier soin du plan."),
        ],
        "form_title": "Réserver le premier rendez-vous",
        "form_band_side_note":
            "Réponse sous 24 heures ouvrées. Pour les urgences cliniques, "
            "appelez directement le +39 02 7770 4488.",
        "form_band_side_note_small":
            "Les données collectées sont utilisées exclusivement pour vous recontacter · RGPD Art. 6.",
        "form_fields": [
            {"name": "first_name", "label": "Prénom",
             "type": "text",       "required": True,
             "placeholder": "Marie"},
            {"name": "last_name",  "label": "Nom",
             "type": "text",       "required": True,
             "placeholder": "Bernard"},
            {"name": "email",      "label": "E-mail",
             "type": "email",      "required": True,
             "placeholder": "marie.bernard@email.fr"},
            {"name": "phone",      "label": "Téléphone",
             "type": "tel",        "required": True,
             "placeholder": "+33 6 12 34 56 78"},
            {"name": "service",    "label": "Soin demandé",
             "type": "select",     "required": True,
             "options": [
                 "Hygiène professionnelle",
                 "Première consultation (dossier + plan)",
                 "Urgence dentaire",
                 "Consultation implantologique",
                 "Consultation orthodontique",
                 "Autre",
             ]},
            {"name": "preferred",  "label": "Plage horaire préférée",
             "type": "select",     "required": False,
             "options": [
                 "Matin (8h30 – 13h00)",
                 "Après-midi (14h00 – 19h30)",
                 "Samedi matin",
                 "Indifférent",
             ]},
            {"name": "notes",      "label": "Notes (facultatives)",
             "type": "textarea",   "required": False,
             "full_width": True,
             "placeholder": "Indiquez d'éventuelles allergies aux médicaments, examens antérieurs, dentiste référent."},
        ],
        "submit_label": "Réserver le rendez-vous",
        "consent":
            "Je consens au traitement de mes données personnelles à la "
            "seule fin d'être recontacté par le cabinet. RGPD Art. 6 · "
            "DPO joignable à dpo@denticostudio.it.",
        "footnote":
            "Les données collectées sont utilisées exclusivement pour "
            "vous recontacter au sujet de votre demande. Conformité RGPD "
            "Art. 6 · DPO joignable à dpo@denticostudio.it.",
    },
}
