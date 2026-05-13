"""Petro · Studio Veterinario Cane Gatto Esotici · French content tree.

T52 multilingual rollout (FR · 2026-05-12). French translation of
`PETRO_CONTENT_IT`. Built for the marketweb T52 multilingual pass
(IT → EN/FR/ES/AR · AAA walk · public flip). Shape parity contract
enforced against `template_content_petro.py`:

  * Same top-level keys, same nested keys at every depth.
  * Same list lengths (4 signature_visits, 4 trattamenti tabs, 4
    items per tab, 5 percorso steps, 5 FAQ items, 8 treatments,
    3 doctors, 2 posts, 4 contatti blocks, 3 hours rows, 4
    transport rows, 3 process steps, 7 form_fields).
  * Same tuple positions for tuple-typed values:
      - home.facts                 → 2-tuples (num, label)
      - home.signature_visits      → 3-tuples (num, title, blurb)
      - home.hero_sidebar_pulse    → 2-tuples (label, value)
      - home.anchor_nav            → 2-tuples (slug, label)
      - home.press                 → flat list[str]
      - home.faq.items             → 2-tuples (q, a)
      - home.location.details      → 2-tuples (label, value)
      - home.location.hours_short  → 2-tuples (day, hours)
      - studio.history             → 2-tuples (year, blurb)
      - studio.values              → 2-tuples (title, desc)
      - visite.treatments          → 4-tuples (name, meta, desc, price)
      - contatti.blocks            → 3-tuples (label, value, sub)
      - contatti.hours             → 3-tuples (day, am, pm)  ← CRITICAL: 3 not 2
      - contatti.transport         → 2-tuples (label, text)
      - richiedi-visita.process    → 3-tuples (num, title, blurb)
  * Same `pages[].slug` values (labels translated, slugs preserved).
  * Same `posts[].slug` values, same `page kind`.

Voice anchor — `médecine préventive` (Ordre des Vétérinaires de
France / Atelier-de-la-Vétérinaire premium register · the clinical-
professional noun phrase that carries the IT `cura preventiva`
load-bearing promise). Used as italic `<em>` emphasis on the hero
H1, in cta_heading, manifesto, studio.values, visite intro,
signature_visits, doctor bios. Secondary anchor `soin préventif`
used where the noun feels too clinical and a softer pet-care
register works better (form helper text). Italian heritage proper
names preserved verbatim : `Padova` (NOT « Padoue »), `Borgo Trento`,
`Via Belzoni 71`, `Università di Padova`, `Royal Veterinary College
London`, `Cornell University Vet School`, `Ospedale Veterinario di
Legnaro`, `Clinica San Marco di Veggiano`, `SCIVAC`, `ANMVI`,
`AAEMV`, `Esaote MyLab Omega`, `Carestream`, `Cuneo IGP`. Vet
technical kept : `WSAVA`, `DA2PPi-L`, `FRCP+FeLV`, `RHDV1+2`,
`Mixoma`, `BCS`. Carla is `Dr. Marco Petro, vétérinaire` ; Anna is
`Dr. Anna Bressan, vétérinaire spécialiste NAC` (Nouveaux Animaux
de Compagnie · the FR-specific term for exotic pets). Pet-care
register : `cura preventiva` → `médecine préventive` · `visita
preventiva` → `visite préventive` · `screening geriatrico` →
`bilan gériatrique` · `sterilizzazione laparoscopica` →
`stérilisation en cœlioscopie` · `laparoscopia` → `cœlioscopie`
(preferred FR vet term, more precise than « laparoscopie »).
Currency : `18 €` (FR convention · space + symbol after). Times :
`7 h 30 – 19 h 30` with `h` separator and non-breaking spaces.
Decimal : comma `pH 4,2`, `0,4 mm`. Espaces insécables (U+00A0)
before `;` `:` `?` `!` and inside `« »` quotes per French
typographic rule.
"""
from __future__ import annotations

from typing import Any


# Imagery URLs from the X.3 curator pack
# `docs/content-factory/imagery/packs/veterinary.md`. All URLs
# Pexels License (CC0-compatible · commercial use OK).
_CHIEF_PORTRAIT = (
    # Veterinarian with white coat examining a small dog · matches
    # Dr. Petro "vétérinaire directeur" hands-on persona
    "https://images.pexels.com/photos/6235648/pexels-photo-6235648.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_STUDIO_IMAGE = (
    # Veterinary clinic interior — exam table + bright clinical
    "https://images.pexels.com/photos/7468978/pexels-photo-7468978.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop"
)
_LEAD_IMAGE = (
    # Bright veterinary clinic consultation · used as blog_list lead
    "https://images.pexels.com/photos/6235244/pexels-photo-6235244.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)
_MAP_FALLBACK = (
    # Modern veterinary clinic reception · map-fallback when Mapbox
    # tile fails to load
    "https://images.pexels.com/photos/6235241/pexels-photo-6235241.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)
_SERVICE_IMAGE = (
    # Vet auscultating cat patient close-up — visite page hero
    "https://images.pexels.com/photos/7470779/pexels-photo-7470779.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=900&fit=crop"
)


PETRO_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Cabinet",                  "kind": "home"},
        {"slug": "studio",          "label": "Le cabinet",               "kind": "about"},
        {"slug": "visite",          "label": "Consultations",            "kind": "services"},
        {"slug": "medici",          "label": "Vétérinaires",             "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Journal clinique",         "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contact",                  "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Réserver une visite",      "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "P",
        "logo_word":    "Petro",
        "tag":          "Cabinet vétérinaire · Padova Borgo Trento · chien chat NAC",
        "phone":        "+39 049 6731 220",
        "email":        "studio@studiopetro.it",
        "address":      "Via Belzoni 71 · 35121 Padova",
        "hours_compact": "Lun – Ven · 8 h 00 – 20 h 00 · Sam 9 h 00 – 13 h 00",
        "hours_footer_rows": [
            "Dimanche · uniquement urgences sur appel",
            "Astreinte de nuit 24/7 · +39 333 410 7726",
        ],
        "license":      "Inscription Ordre des Vétérinaires de Padova n° 1428 · Directeur sanitaire Dr. M. Petro",
        "footer_intro":
            "Cabinet vétérinaire indépendant de médecine préventive, "
            "chirurgie des tissus mous et soins gériatriques pour chien, "
            "chat et NAC. Trois vétérinaires, un seul dossier clinique "
            "pour chaque animal, astreinte de nuit sur appel.",
    },

    "home": {
        "hero_variant": "split-consultive",
        "eyebrow":  "Médecine vétérinaire · Padova Borgo Trento",
        "headline": "Les animaux ne parlent pas. La <em>médecine préventive</em> écoute en premier.",
        "intro":
            "Visites préventives annuelles, vaccinations selon calendrier, "
            "imagerie diagnostique et chirurgie des tissus mous pour chien, "
            "chat et NAC. Trois vétérinaires associés, astreinte de nuit "
            "sur appel, un seul dossier clinique partagé pour chaque "
            "patient.",
        "primary_cta":   "Réservez une visite préventive",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "Les vétérinaires",
        "secondary_href":"medici",

        "facts": [
            ("17",    "années de cabinet vétérinaire indépendant"),
            ("4 200", "animaux soignés chaque année"),
            ("3",     "vétérinaires associés en cabinet"),
        ],

        "manifesto_drop_cap": "L",
        "manifesto":
            "es animaux ne décrivent pas la douleur : ils la cachent. Le "
            "chat se réfugie, le chien mange moins, le lapin cesse de "
            "bouger. C'est pourquoi chez Petro la médecine est avant "
            "tout préventive — visite annuelle complète, bilan "
            "gériatrique semestriel à partir de sept ans, contrôle "
            "dentaire tous les deux ans, vaccinations selon calendrier. "
            "Lorsque l'animal arrive en consultation pour des symptômes "
            "visibles, nous sommes souvent déjà à mi-chemin du problème. "
            "Notre dossier clinique existe pour y parvenir avant.",

        "hero_sidebar_top_label": "Direction clinique",
        "hero_sidebar_quote":
            "« Les animaux ne disent pas où ils ont mal. La visite "
            "préventive est la seule manière honnête de pratiquer la "
            "médecine vétérinaire — le reste n'est qu'urgence. »",
        "hero_sidebar_author": "— Dr. Marco Petro · Directeur sanitaire · Inscription OMV Padova 1428",
        "hero_sidebar_pulse": [
            ("Cabinet",     "Padova · Borgo Trento"),
            ("Depuis",      "2008"),
            ("Référence",   "Chien chat NAC"),
        ],

        "anchor_nav": [
            ("metodo",        "Méthode clinique"),
            ("visite",        "Visites préventives"),
            ("percorso",      "Parcours patient"),
            ("medico",        "Direction clinique"),
            ("studio",        "Cabinet & contact"),
        ],

        "signature_visits_label":   "Quatre familles d'intervention",
        "signature_visits_heading": "Quatre parcours cliniques, <em>un seul dossier pour chaque animal.</em>",
        "signature_visits_intro":
            "Les quatre familles les plus demandées de la médecine "
            "vétérinaire des petits animaux. La liste complète figure "
            "dans la page Consultations.",
        "signature_visits": [
            ("01", "Visite préventive annuelle",
             "Examen clinique complet, poids et BCS, auscultation "
             "cardio-pulmonaire, palpation abdominale, contrôle "
             "dentaire, anamnèse vaccinale et prophylaxie parasitaire. "
             "Quarante minutes, sur rendez-vous."),
            ("02", "Vaccinations & prophylaxie",
             "Vaccins chien (DA2PPi-L) et chat (FRCP-FeLV) selon "
             "calendrier WSAVA. Prophylaxie dirofilariose, leishmaniose, "
             "tiques. Vaccins lapin (RHDV-Mixoma) et furet. "
             "Carnet de santé tenu à jour sur place."),
            ("03", "Chirurgie tissus mous",
             "Stérilisation chien et chat en cœlioscopie (mini-invasive, "
             "temps de récupération réduits), exérèse de néoformations "
             "cutanées, chirurgie oncologique avec examen histologique, "
             "sutures esthétiques."),
            ("04", "Imagerie diagnostique",
             "Échographie abdominale et cardiaque sur place, "
             "radiographie numérique avec images remises au "
             "propriétaire, cytologie par ponction à l'aiguille fine "
             "lue en 24 h par le laboratoire conventionné de "
             "l'Università di Padova."),
        ],

        "trattamenti_tabs": {
            "label":   "Tarifs des visites & interventions",
            "heading": "Ce que nous faisons, avec <em>quel critère.</em>",
            "intro":
                "Quatre familles cliniques, chacune avec un protocole "
                "écrit et un coût annoncé. Aucun devis personnalisé "
                "pour les actes de routine — uniquement pour les plans "
                "de soin structurés (chirurgie complexe, thérapie "
                "oncologique, rééducation).",
            "tabs": [
                {
                    "id":      "preventiva",
                    "label":   "Préventive",
                    "eyebrow": "Médecine préventive",
                    "heading": "Quarante minutes, une fois par an.",
                    "body":
                        "La visite préventive annuelle n'est pas un contrôle "
                        "rapide : c'est une évaluation clinique complète de "
                        "quarante minutes avec anamnèse, examen clinique "
                        "systématique, contrôle dentaire, poids/BCS, "
                        "auscultation et palpation. À partir de sept ans, "
                        "s'ajoute le bilan gériatrique semestriel.",
                    "items": [
                        ("Visite préventive annuelle chien/chat", "40 min · 65 €"),
                        ("Bilan gériatrique (≥ 7 ans)", "60 min · 95 €"),
                        ("Visite préventive NAC (lapin/furet)", "45 min · 75 €"),
                        ("Anamnèse pré-adoption chiot/chaton", "30 min · 50 €"),
                    ],
                    "cta_label": "Tous les protocoles préventifs →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "vaccinazioni",
                    "label":   "Vaccinations",
                    "eyebrow": "Vaccins & prophylaxie parasitaire",
                    "heading": "Protocole WSAVA, carnet sur place.",
                    "body":
                        "Les vaccins suivent les recommandations WSAVA "
                        "(chien DA2PPi-L core annuel, chat FRCP-FeLV "
                        "core triennal après rappel). Le carnet de "
                        "santé est délivré sur place, également en "
                        "version électronique via application. "
                        "Prophylaxie antiparasitaire mensuelle ou "
                        "trimestrielle selon la race et le contexte.",
                    "items": [
                        ("Vaccin chien DA2PPi-L (annuel)", "rendez-vous · 45 €"),
                        ("Vaccin chat FRCP + FeLV", "rendez-vous · 55 €"),
                        ("Vaccin lapin RHDV1+2 / Mixoma", "rendez-vous · 50 €"),
                        ("Prophylaxie dirofilariose + tiques (12 mois)", "plan · 95 €"),
                    ],
                    "cta_label": "Calendrier vaccinal complet →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "chirurgia",
                    "label":   "Chirurgie",
                    "eyebrow": "Chirurgie tissus mous",
                    "heading": "Cœlioscopie mini-invasive chaque fois que possible.",
                    "body":
                        "Stérilisation chien et chat en cœlioscopie "
                        "(trois petits accès · hospitalisation de jour · "
                        "douleur post-opératoire réduite). Exérèse de "
                        "néoformations cutanées avec examen histologique "
                        "au laboratoire d'Anatomie pathologique de "
                        "l'Università di Padova. Sutures esthétiques "
                        "sous-cuticulaires résorbables.",
                    "items": [
                        ("Stérilisation chatte (cœlioscopie)", "intervention · 320 €"),
                        ("Stérilisation chienne < 20 kg", "intervention · 480 €"),
                        ("Stérilisation chienne > 20 kg", "intervention · 620 €"),
                        ("Exérèse néoformation cutanée + histologique", "intervention · 220 €"),
                    ],
                    "cta_label": "Parcours chirurgicaux complets →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "diagnostica",
                    "label":   "Diagnostic",
                    "eyebrow": "Imagerie diagnostique & laboratoire",
                    "heading": "Écho, radiographie numérique, cytologie en 24 h.",
                    "body":
                        "Échographie abdominale et cardiaque sur place "
                        "avec Esaote MyLab Omega · radiographie "
                        "numérique Carestream avec remise des images "
                        "au propriétaire via cloud · cytologie par "
                        "ponction à l'aiguille fine lue en 24 h par "
                        "le laboratoire d'Anatomie pathologique de "
                        "l'Università di Padova. Bilans biochimiques "
                        "traités sur place en 30 minutes.",
                    "items": [
                        ("Échographie abdominale complète", "30 min · 95 €"),
                        ("Échographie cardiaque (échocardio)", "45 min · 130 €"),
                        ("Radiographie numérique (2 incidences)", "20 min · 75 €"),
                        ("Bilans biochimiques complets sur place", "30 min · 85 €"),
                    ],
                    "cta_label": "Protocoles diagnostiques →",
                    "cta_href":  "visite",
                },
            ],
        },

        "chief_label":   "Direction clinique",
        "chief_heading": "Un seul vétérinaire <em>signe chaque dossier.</em>",
        "chief": {
            "name":  "Dr. Marco Petro",
            "role":  "Directeur sanitaire · Médecine interne & chirurgie tissus mous",
            "bio":
                "Diplômé en Médecine Vétérinaire à l'Università di Padova "
                "en 2000, perfectionnement au Royal Veterinary College "
                "London (2002-2004) en petits animaux, stage de "
                "spécialisation à la Cornell University Vet School "
                "(NY, USA) en 2006. Membre SCIVAC (Società Culturale "
                "Italiana Veterinari Animali Compagnia) et ANMVI "
                "(Associazione Nazionale Medici Veterinari Italiani). "
                "Inscription Ordre des Vétérinaires de Padova n° 1428 "
                "depuis 2001. Directeur sanitaire du cabinet depuis 2008.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "percorso": {
            "label":   "Parcours patient",
            "heading": "Ce qu'il faut attendre de la <em>première visite.</em>",
            "intro":
                "La première visite au cabinet dure une heure et est "
                "consacrée à la constitution du dossier clinique "
                "complet : anamnèse, examen clinique, éventuelle "
                "échographie abdominale de base, plan de soin écrit. "
                "Jamais d'intervention non urgente lors de la première "
                "visite.",
            "steps": [
                {
                    "num": "01",
                    "icon": "clipboard",
                    "title": "Check-in & anamnèse",
                    "desc": "Secrétariat, fiche anamnestique complète "
                            "(race, âge, alimentation, environnement, "
                            "cohabitation avec d'autres animaux), "
                            "examens antérieurs du vétérinaire précédent "
                            "le cas échéant.",
                    "duration": "10 min",
                },
                {
                    "num": "02",
                    "icon": "book",
                    "title": "Examen clinique complet",
                    "desc": "Poids et Body Condition Score, auscultation "
                            "cardio-pulmonaire, palpation abdominale, "
                            "inspection de la cavité buccale, contrôle "
                            "de la peau et du pelage, palpation des "
                            "ganglions lymphatiques.",
                    "duration": "20 min",
                },
                {
                    "num": "03",
                    "icon": "heart",
                    "title": "Diagnostic de base",
                    "desc": "Échographie abdominale d'orientation "
                            "(si indiquée), prélèvements éventuels "
                            "pour bilans biochimiques traités sur "
                            "place en trente minutes. Radiographie "
                            "en cas de suspicion de traumatisme.",
                    "duration": "15 min",
                },
                {
                    "num": "04",
                    "icon": "chart",
                    "title": "Plan de soin écrit",
                    "desc": "Discussion avec le propriétaire du plan "
                            "préventif ou thérapeutique, devis "
                            "détaillé poste par poste, remise "
                            "également par courriel au format PDF.",
                    "duration": "10 min",
                },
                {
                    "num": "05",
                    "icon": "document",
                    "title": "Programmation & suivi",
                    "desc": "Calendrier des visites de rappel, "
                            "rappels par WhatsApp pour vaccins et "
                            "prophylaxie, ligne directe avec le "
                            "secrétariat pour les questions non "
                            "urgentes.",
                    "duration": "5 min",
                },
            ],
        },

        "press": ["Veterinaria Italiana", "SCIVAC Bulletin", "Il Mondo del Cane",
                  "QuattroZampe Mondadori", "Corriere Animali"],
        "press_label": "Paru dans",

        "faq": {
            "label": "Questions fréquentes",
            "heading": "Les questions que <em>les propriétaires nous posent le plus souvent.</em>",
            "items": [
                ("À quelle fréquence faut-il une visite préventive ?",
                 "Pour le chien et le chat adultes en bonne santé, la "
                 "fréquence est annuelle. À partir de sept ans (animaux "
                 "gériatriques), s'ajoute une visite de bilan "
                 "semestrielle avec bilans biochimiques. Pour le lapin "
                 "et le furet, la fréquence est semestrielle dès la "
                 "première visite, car l'espérance de vie est plus "
                 "courte."),
                ("Pratiquez-vous la stérilisation en cœlioscopie ?",
                 "Oui, sur chatte et chienne jusqu'à 35 kg. La "
                 "stérilisation en cœlioscopie comporte trois petits "
                 "accès abdominaux de 5 mm au lieu de l'incision "
                 "traditionnelle, hospitalisation de jour, douleur "
                 "post-opératoire réduite et retour à la normale en "
                 "48 heures. Pour les gabarits supérieurs à 35 kg, "
                 "l'indication est évaluée au cas par cas."),
                ("Soignez-vous également lapins, furets, oiseaux et reptiles ?",
                 "Lapin, furet et cobaye oui, sur tous les parcours "
                 "(préventive, vaccinations, chirurgie, diagnostic). "
                 "Oiseaux et reptiles uniquement pour des visites de "
                 "base — pour les pathologies complexes, nous orientons "
                 "vers des confrères spécialisés en NAC des cliniques "
                 "universitaires."),
                ("Disposez-vous d'un service d'astreinte de nuit ?",
                 "Oui, le docteur Petro est joignable 24/7 pour ses "
                 "propres patients au numéro +39 333 410 7726. Pour "
                 "les urgences sur des animaux non suivis, nous "
                 "orientons vers l'Ospedale Veterinario de "
                 "l'Università di Padova (Legnaro, ouvert 24h) ou "
                 "vers la Clinica San Marco de Veggiano."),
                ("Comment fonctionne le plan de prévention annuel ?",
                 "Il comprend visite préventive, vaccins chien "
                 "DA2PPi-L ou chat FRCP, prophylaxie mensuelle "
                 "dirofilariose et tiques, dépistage biochimique "
                 "annuel, un rappel semestriel gratuit. Coût 245 €/an "
                 "pour le chien, 195 €/an pour le chat. Remise de 15 % "
                 "sur les interventions chirurgicales programmées dans "
                 "les douze mois suivants."),
            ],
        },

        "cta_heading":
            "Chaque plan de soin est <em>écrit, annoncé, partagé avec le propriétaire.</em>",
        "cta_primary_label":   "Réservez une visite préventive",
        "cta_secondary_label": "Contact du cabinet",

        "location": {
            "label":   "Adresse du cabinet",
            "heading": "Via Belzoni 71, <em>Padova.</em>",
            "intro":
                "Le cabinet occupe le rez-de-chaussée d'un immeuble "
                "du XIXᵉ siècle en zone Borgo Trento, à quatre cents "
                "mètres de la Stazione Centrale et à dix minutes à "
                "pied de la Faculté de Médecine Vétérinaire. Trois "
                "salles de consultation séparées chien/chat/NAC, "
                "bloc opératoire, salle de diagnostic avec échographe "
                "et radiographie numérique, zone d'hospitalisation "
                "de jour.",
            "map_image": "",
            "map_fallback_image": _MAP_FALLBACK,
            "details": [
                ("Adresse",
                 "Via Belzoni 71\n35121 Padova"),
                ("Gare",
                 "Padova Centrale\n6 minutes à pied"),
                ("Stationnement",
                 "Parking Borgo Trento gratuit\n80 mètres du cabinet"),
                ("Accessibilité",
                 "Entrée de plain-pied sans marches\naccessible aux fauteuils roulants et grandes caisses de transport"),
            ],
            "hours_short": [
                ("Lun – Ven", "8 h 00 – 20 h 00"),
                ("Samedi",    "9 h 00 – 13 h 00"),
                ("Dimanche",  "Uniquement urgences sur appel"),
            ],
            "cta_label": "Obtenir l'itinéraire",
            "cta_href":  "contatti",
        },
    },

    # ─── STUDIO (about) ────────────────────────────────────────
    "studio": {
        "eyebrow":   "Le cabinet · Padova Borgo Trento",
        "headline":  "Trois vétérinaires, <em>un dossier pour chaque animal.</em>",
        "intro":
            "Le Cabinet Vétérinaire Petro est un cabinet associé "
            "fondé en 2008 par Marco Petro avec deux confrères formés "
            "à l'Università di Padova. Trois vétérinaires, un seul "
            "dossier clinique partagé pour chaque patient, une seule "
            "signature au bas de chaque plan de soin. Astreinte de "
            "nuit sur appel pour les patients déjà suivis.",
        "history": [
            ("2008",
             "Marco Petro ouvre le cabinet via Belzoni avec un seul "
             "cabinet de consultation et une assistante. Soixante-quinze "
             "animaux suivis la première année."),
            ("2012",
             "Arrivée de la Dr. Anna Bressan comme deuxième "
             "vétérinaire associée · spécialisation en NAC (lapin, "
             "furet, cobaye, petits reptiles)."),
            ("2015",
             "Ouverture du bloc opératoire avec anesthésie par "
             "inhalation isoflurane et monitorage multiparamétrique. "
             "Démarrage de la chirurgie cœlioscopique pour les "
             "stérilisations."),
            ("2018",
             "Acquisition de l'échographe Esaote MyLab Omega et du "
             "système de radiographie numérique Carestream. Toute "
             "l'imagerie diagnostique est internalisée au cabinet."),
            ("2023",
             "Arrivée du Dr. Tommaso Zen comme troisième associé · "
             "spécialisation en oncologie vétérinaire et chirurgie "
             "reconstructive. Le cabinet clôture l'année avec 4 200 "
             "animaux suivis."),
        ],
        "studio_image": _STUDIO_IMAGE,
        "studio_image_caption": "Salle de consultation · Via Belzoni 71 · Padova",
        "method_title": "La méthode Petro",
        "method_paragraphs": [
            "La médecine vétérinaire des petits animaux ne ressemble "
            "pas à la médecine humaine pour une raison : le patient ne "
            "parle pas. Le chat qui se met à boire trois fois plus que "
            "la normale est déjà à mi-chemin d'une insuffisance rénale. "
            "Le chien qui boite par intermittence présente déjà une "
            "arthrose avancée. C'est pourquoi chez Petro la médecine "
            "préventive n'est pas un service annexe : c'est le premier "
            "chapitre, et pour de nombreux patients c'est aussi le "
            "seul qui soit véritablement nécessaire.",
            "Le dossier clinique est unique — le même pour les trois "
            "associés — parce qu'un animal n'est pas le patient d'un "
            "seul vétérinaire, c'est le patient du cabinet. Lorsque "
            "Anna repère une néoformation cutanée suspecte pendant la "
            "vaccination, elle la signale à Tommaso pour l'exérèse "
            "chirurgicale dans le même document clinique. Aucun soin "
            "fragmenté, aucun compte-rendu égaré entre confrères.",
            "Les coûts sont annoncés pour les actes de routine "
            "(visite préventive, vaccins, stérilisation, échographie, "
            "diagnostic de base). Pour les plans structurés — thérapie "
            "oncologique, rééducation post-traumatique, chirurgie "
            "orthopédique complexe — le devis est personnalisé après "
            "une évaluation clinique complète, mais toujours remis "
            "par écrit et signé au bas du document.",
        ],
        "values_label":   "Valeurs du cabinet",
        "values_heading": "Quatre engagements, <em>consignés au dossier.</em>",
        "values": [
            ("Médecine préventive toujours",
             "La visite préventive annuelle est le point de départ "
             "de toute relation avec le patient. Jamais d'intervention "
             "non urgente sans anamnèse complète."),
            ("Un seul dossier",
             "Trois vétérinaires partagent le même dossier clinique "
             "pour chaque animal. Aucun compte-rendu perdu, aucun "
             "suivi manqué entre confrères."),
            ("Coûts annoncés",
             "Tarifs écrits pour les actes de routine. Devis en PDF "
             "signé pour chaque plan complexe avant le début des "
             "traitements."),
            ("Astreinte pour ses propres patients",
             "Astreinte de nuit 24/7 sur la ligne directe du docteur "
             "Petro pour les animaux déjà suivis. Aucun patient "
             "laissé à lui-même."),
        ],
        "cta_heading":
            "Le premier pas est toujours <em>une visite préventive d'une heure.</em>",
        "cta_primary_label":   "Découvrez les vétérinaires",
        "cta_secondary_label": "Réservez la première visite",
        "press_label": "Paru dans",
        "press": ["Veterinaria Italiana", "SCIVAC Bulletin", "Il Mondo del Cane",
                  "QuattroZampe Mondadori", "Corriere Animali"],
    },

    # ─── VISITE (services) ─────────────────────────────────────
    "visite": {
        "eyebrow":  "Consultations & interventions",
        "headline": "Quatre familles d'intervention, <em>un seul dossier par animal.</em>",
        "intro":
            "La liste complète des parcours cliniques disponibles au "
            "cabinet. Les coûts indiqués concernent les actes de "
            "routine ; pour les plans structurés, le devis est rédigé "
            "après évaluation clinique complète selon la logique de "
            "médecine préventive du cabinet.",
        "service_image": _SERVICE_IMAGE,
        "service_image_caption": "Auscultation cardio-pulmonaire · visite préventive",
        # Treatments — 4-tuples (name, meta, desc, price) per
        # specialist services.html:121 unpacking contract.
        "treatments": [
            ("Visite préventive annuelle chien/chat",
             "40 min · sur rendez-vous",
             "Anamnèse complète, poids et Body Condition Score, "
             "auscultation cardio-pulmonaire, palpation abdominale, "
             "contrôle de la cavité buccale, inspection de la peau "
             "et du pelage, palpation des ganglions, vérification du "
             "calendrier vaccinal et antiparasitaire.",
             "65 €"),
            ("Bilan gériatrique (≥ 7 ans)",
             "60 min · semestriel",
             "Visite complète + bilans biochimiques (NFS, fonction "
             "rénale et hépatique, ionogramme, T4 chez le chat), "
             "pression artérielle, échographie abdominale "
             "d'orientation. Indiqué pour le chien et le chat à "
             "partir de sept ans.",
             "95 €"),
            ("Vaccin chien DA2PPi-L (annuel)",
             "rendez-vous · 30 min",
             "Vaccin combiné maladie de Carré, adénovirus, "
             "parvovirus, parainfluenza, leptospirose quatre souches "
             "(L4). Calendrier WSAVA, carnet de santé tenu à jour "
             "sur place.",
             "45 €"),
            ("Vaccin chat FRCP + FeLV",
             "rendez-vous · 30 min",
             "Vaccin combiné rhinotrachéite, calicivirus, "
             "panleucopénie + vaccin leucose féline (FeLV). Pour "
             "les chats vivant exclusivement en intérieur, "
             "uniquement FRCP triennal après rappel, coût 40 €.",
             "55 €"),
            ("Stérilisation chatte en cœlioscopie",
             "intervention · hospitalisation de jour",
             "Ovariectomie mini-invasive avec trois accès de 5 mm, "
             "anesthésie par inhalation isoflurane, monitorage "
             "multiparamétrique, sutures sous-cuticulaires "
             "résorbables. Sortie le jour même.",
             "320 €"),
            ("Stérilisation chienne < 20 kg (cœlioscopie)",
             "intervention · hospitalisation de jour",
             "Ovariectomie en cœlioscopie avec trois accès "
             "abdominaux, anesthésie par inhalation, analgésie "
             "multimodale post-opératoire, sortie le jour même.",
             "480 €"),
            ("Échographie abdominale complète",
             "30 min · sur rendez-vous",
             "Esaote MyLab Omega · évaluation du foie, de la rate, "
             "des reins, de la vessie, des parois gastro-"
             "intestinales, des ganglions mésentériques, de la "
             "prostate. Compte-rendu remis le jour même.",
             "95 €"),
            ("Échocardiographie",
             "45 min · sur rendez-vous",
             "Étude échographique des cavités cardiaques, évaluation "
             "des valves, mesure de la fraction d'éjection et de la "
             "contractilité. Indiquée en pré-anesthésie chez les "
             "patients gériatriques ou les races prédisposées "
             "(Cavalier King Charles, Boxer, Maine Coon).",
             "130 €"),
        ],
        "footnote_heading": "Ce que nous ne faisons pas au cabinet",
        "footnote":
            "Cardiologie interventionnelle, neurochirurgie, "
            "orthopédie reconstructive complexe, obstétrique "
            "équine. Pour ces cas, nous orientons vers l'Ospedale "
            "Veterinario de l'Università di Padova (Legnaro), avec "
            "lequel nous avons une convention directe et une voie "
            "prioritaire pour nos patients.",
        "cta_heading":
            "Vous souhaitez réserver une <em>visite préventive ou un contrôle ?</em>",
        "cta_primary_label":   "Réservez une visite",
        "cta_secondary_label": "Découvrez les vétérinaires",
    },

    # ─── MEDICI (team) ─────────────────────────────────────────
    "medici": {
        "eyebrow":  "Les vétérinaires",
        "headline": "Trois vétérinaires associés, <em>trois spécialisations complémentaires.</em>",
        "intro":
            "Trois vétérinaires partagent le cabinet depuis 2008 "
            "(Marco), depuis 2012 (Anna) et depuis 2023 (Tommaso). "
            "Trois spécialisations complémentaires couvrent médecine "
            "interne, NAC et chirurgie reconstructive. Un seul "
            "dossier clinique pour chaque patient, dans la logique "
            "de médecine préventive du cabinet.",
        "doctors": [
            {
                "name":  "Dr. Marco Petro",
                "role":  "Directeur sanitaire",
                "specialty": "Médecine interne · chirurgie tissus mous",
                "bio":
                    "Diplôme Università di Padova 2000. Royal Veterinary "
                    "College London 2002-2004. Cornell University Vet "
                    "School (NY, USA) stage 2006. Inscription OMV Padova "
                    "1428 depuis 2001. Directeur sanitaire depuis 2008. "
                    "Membre SCIVAC et ANMVI. Médecine préventive comme "
                    "premier chapitre clinique.",
                "portrait": _CHIEF_PORTRAIT,
                "year_label": "Depuis",
                "year": "2008",
            },
            {
                "name":  "Dr. Anna Bressan",
                "role":  "Vétérinaire associée",
                "specialty": "NAC · lapin, furet, cobaye, reptiles",
                "bio":
                    "Diplôme Università di Padova 2010. Master en "
                    "Médecine des NAC à Cremona (Università di Milano) "
                    "2011-2012. Membre AAEMV (Associazione Italiana "
                    "Veterinari per Animali Esotici). Dirige la "
                    "section NAC du cabinet depuis 2012, dans une "
                    "logique de visite préventive semestrielle.",
                "portrait":
                    "https://images.pexels.com/photos/6235113/pexels-photo-6235113.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
                "year_label": "Depuis",
                "year": "2012",
            },
            {
                "name":  "Dr. Tommaso Zen",
                "role":  "Vétérinaire associé",
                "specialty": "Oncologie vétérinaire · chirurgie reconstructive",
                "bio":
                    "Diplôme Università di Bologna 2014. "
                    "Spécialisation en Oncologie Vétérinaire à "
                    "l'Università de Madrid 2017-2019. Publications "
                    "dans le Journal of Small Animal Practice (2018) "
                    "et Veterinary Surgery (2020). Dirige la section "
                    "de chirurgie oncologique du cabinet depuis 2023.",
                "portrait":
                    "https://images.pexels.com/photos/6234600/pexels-photo-6234600.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
                "year_label": "Depuis",
                "year": "2023",
            },
        ],
        "portrait_city": "Padova · Borgo Trento",
    },

    # ─── PUBBLICAZIONI (blog_list) ─────────────────────────────
    "pubblicazioni": {
        "eyebrow":  "Journal clinique du cabinet",
        "headline": "Notes de travail <em>depuis la salle de consultation.</em>",
        "intro":
            "Brèves notes des trois vétérinaires sur les protocoles "
            "cliniques en usage, sur les cas les plus représentatifs "
            "de l'année, sur les vaccins et les prophylaxies "
            "saisonnières. Lecture réservée aux propriétaires de "
            "patients suivis et aux confrères.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Cabinet Vétérinaire Petro · Le journal clinique",
        "empty_body_fallback_paragraphs": [
            "Article en préparation éditoriale. La publication "
            "intégrale sera disponible sous peu, rédigée "
            "personnellement par l'un des trois vétérinaires "
            "associés.",
            "Ce repère décrit la voix du Journal Clinique : brèves "
            "notes de travail, réflexions sur les protocoles "
            "préventifs, récits de cas cliniques représentatifs. "
            "Jamais plus de deux mille mots, jamais moins de cinq "
            "cents.",
        ],
    },

    "posts": [
        {
            "slug":     "calendario-vaccinale-2026",
            "kicker":   "Vaccinations en cours",
            "title":    "Le calendrier vaccinal du cabinet · mise à jour 2026",
            "date":     "8 octobre 2026",
            "read_min": 4,
            "author":   "Dr. Marco Petro",
            "cover_image": _LEAD_IMAGE,
            "lede":
                "WSAVA a publié en septembre les nouvelles "
                "recommandations sur les vaccins core pour chien et "
                "chat. Ce qui change à partir d'octobre 2026 dans le "
                "calendrier de rappel de nos patients.",
            "body": [
                ("p", "Les recommandations WSAVA 2026 confirment la "
                      "fréquence annuelle pour les vaccins core chien "
                      "(DA2PPi-L) et consolident le passage à triennal "
                      "après rappel pour les vaccins core chat (FRCP) "
                      "pour les chats vivant en intérieur strict. Pour "
                      "les chats avec accès extérieur, la fréquence "
                      "reste annuelle, y compris pour FRCP."),
                ("h2", "Ce qui change pour la prophylaxie"),
                ("p", "La leptospirose quatre souches (L4) reste core "
                      "annuel pour le chien en milieu urbain padouan "
                      "— l'incidence sur les dernières saisons s'est "
                      "révélée stable mais non en recul. Pour le chat "
                      "en intérieur, nous recalibrons à triennal le "
                      "FeLV après le rappel de la première année, "
                      "tandis que pour les chats free-roaming le FeLV "
                      "reste annuel."),
                ("h2", "Ce que nous faisons à partir d'octobre"),
                ("p", "Les propriétaires des patients suivis recevront "
                      "par WhatsApp le plan vaccinal mis à jour. Pour "
                      "les nouveaux patients, le calendrier est "
                      "construit à la première visite préventive sur "
                      "la base de la race, de l'âge, du milieu de vie "
                      "et du contact avec d'autres animaux."),
            ],
        },
        {
            "slug":     "sterilizzazione-laparoscopia-perche",
            "kicker":   "Chirurgie",
            "title":    "Pourquoi nous préférons la cœlioscopie pour la stérilisation",
            "date":     "25 septembre 2026",
            "read_min": 5,
            "author":   "Dr. Tommaso Zen",
            "cover_image":
                "https://images.pexels.com/photos/7470769/pexels-photo-7470769.jpeg"
                "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
            "lede":
                "Depuis 2015, le cabinet pratique la stérilisation "
                "des chattes et des chiennes en cœlioscopie "
                "mini-invasive. Voici pourquoi c'est notre standard "
                "et quand nous pratiquons encore l'intervention "
                "traditionnelle.",
            "body": [
                ("p", "La stérilisation en cœlioscopie comporte trois "
                      "accès abdominaux de 5 mm au lieu de l'incision "
                      "traditionnelle de 4-7 cm. La différence n'est "
                      "pas esthétique : elle est avant tout "
                      "physiologique. Douleur post-opératoire réduite, "
                      "retour à la normale en 48 heures, risque de "
                      "complications infectieuses considérablement "
                      "diminué, hospitalisation de jour au lieu d'une "
                      "nuit."),
                ("h2", "Quand nous pratiquons encore la chirurgie traditionnelle"),
                ("p", "Trois situations cliniques. Premièrement : "
                      "chiennes au-delà de 35 kg, où l'accès "
                      "cœlioscopique devient techniquement complexe "
                      "(l'ovaire est profond, l'espace opératoire "
                      "limité). Deuxièmement : pyomètre (infection "
                      "utérine) — l'utérus doit être retiré en "
                      "totalité et l'accès ouvert convient également. "
                      "Troisièmement : tumeurs ovariennes, pour la "
                      "même raison."),
                ("h2", "Les chiffres du cabinet"),
                ("p", "De 2015 à aujourd'hui, nous avons réalisé "
                      "environ 1 400 stérilisations cœlioscopiques. "
                      "Taux de complications majeures sous 1 %. Taux "
                      "de complications mineures (sérômes, œdèmes "
                      "locaux) autour de 3 %. Indice de satisfaction "
                      "du propriétaire (questionnaire de suivi à "
                      "sept jours) supérieur à 95 %."),
            ],
        },
    ],

    # ─── CONTATTI ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contact & adresse",
        "headline": "Trois canaux, <em>un seul secrétariat.</em>",
        "intro":
            "Pour les rendez-vous de routine, la réservation se fait "
            "depuis le formulaire en ligne ou par téléphone aux "
            "horaires d'ouverture. Pour les urgences, le numéro "
            "d'astreinte est actif 24/7 pour les patients déjà "
            "suivis.",
        # Blocks — 3-tuples (label, value, sub) per specialist
        # contact.html:105 unpacking contract.
        "blocks": [
            ("Secrétariat",
             "+39 049 6731 220",
             "Lun – Ven · 8 h 00 – 20 h 00 · Sam 9 h 00 – 13 h 00"),
            ("Astreinte de nuit",
             "+39 333 410 7726",
             "24/7 · uniquement pour patients déjà suivis"),
            ("Courriel",
             "studio@studiopetro.it",
             "Réponse sous 24 h en horaires d'ouverture"),
            ("Adresse",
             "Via Belzoni 71 · 35121 Padova",
             "Borgo Trento · 6 minutes de la Stazione Centrale"),
        ],
        "form_title": "Écrivez-nous",
        "form_intro":
            "Pour les rendez-vous de routine, utilisez le formulaire "
            "Réserver une visite. Ce formulaire est réservé aux "
            "demandes génériques, demande de copie du dossier "
            "clinique, deuxième avis ou questions sur les "
            "protocoles.",
        "form_placeholders": {
            "name":    "Nom et prénom",
            "email":   "Courriel",
            "phone":   "Téléphone",
            "subject": "Objet",
            "message": "Comment pouvons-nous vous aider ? Indiquez aussi le nom et l'espèce de l'animal.",
        },
        "form_helpers": {
            "name":    "Servira à adresser la réponse éventuelle.",
            "email":   "Nous répondrons sous 24 heures en horaires d'ouverture.",
            "phone":   "Uniquement pour demander un rappel téléphonique.",
            "subject": "Exemple : « demande de deuxième avis » ou « copie du dossier clinique ».",
        },
        "form_consent":
            "J'accepte le traitement des données conformément au RGPD. Politique de confidentialité disponible au cabinet.",
        "form_submit_note":
            "Pour les urgences cliniques sur patients déjà suivis, "
            "appelez le numéro d'astreinte 24/7. Ce formulaire n'est "
            "pas surveillé en dehors des horaires d'ouverture, "
            "conformément à la logique de soin préventif du cabinet.",
        "hours_heading": "Horaires d'ouverture",
        # hours — 3-tuples (day, am, pm) per specialist contact.html:175.
        "hours": [
            ("Lun – Ven", "8 h 00 – 13 h 00", "14 h 30 – 20 h 00"),
            ("Samedi",    "9 h 00 – 13 h 00", "fermé"),
            ("Dimanche",  "fermé",            "astreinte sur appel"),
        ],
        "transport_heading": "Comment venir",
        "transport": [
            ("Train",          "Stazione Centrale de Padova · 6 minutes à pied"),
            ("Voiture",        "Sortie Padova Est · 12 minutes en voiture"),
            ("Tramway",        "SIR1 arrêt Borgo Trento · 2 minutes à pied"),
            ("Stationnement",  "Parking Borgo Trento gratuit · 80 mètres du cabinet"),
        ],
    },

    # ─── RICHIEDI-VISITA (appointment) ─────────────────────────
    "richiedi-visita": {
        "eyebrow":  "Réserver une visite",
        "headline": "Une visite préventive, <em>quarante minutes.</em>",
        "intro":
            "Réservez en ligne la première visite préventive de "
            "votre animal. Le secrétariat confirme le rendez-vous "
            "sous 24 heures en horaires d'ouverture. Pour les "
            "urgences, appelez le numéro d'astreinte.",
        "process_label": "Comment cela fonctionne",
        "process_heading": "Trois étapes, <em>une seule visite.</em>",
        # process — 3-tuples (num, title, blurb) per specialist
        # appointment.html:97 unpacking contract.
        "process": [
            ("01", "Remplissez le formulaire",
             "Indiquez le nom de l'animal, l'espèce, la race, l'âge, "
             "le motif de la visite. Les examens antérieurs peuvent "
             "être joints ou apportés au cabinet."),
            ("02", "Confirmation sous 24 heures",
             "Le secrétariat vous contacte sous 24 heures pour "
             "confirmer date et horaire. Pour les visites urgentes "
             "(boiterie soudaine, inappétence, vomissements "
             "récurrents), appelez directement le secrétariat."),
            ("03", "Première visite de 60 minutes",
             "Anamnèse, examen clinique complet, diagnostic de base "
             "si indiqué, plan de soin écrit. Le devis est également "
             "remis en PDF, dans la logique de médecine préventive "
             "du cabinet."),
        ],
        "form_title": "Formulaire de réservation",
        "form_band_side_note":
            "Visite préventive — 40 minutes — 65 € (chien/chat), "
            "75 € (NAC).",
        "form_band_side_note_small":
            "Les coûts sont annoncés pour les actes de routine. "
            "Pour les plans structurés, le devis est rédigé après "
            "la première visite.",
        "form_fields": [
            {
                "name":    "owner_name",
                "label":   "Nom du propriétaire",
                "type":    "text",
                "required": True,
                "placeholder": "Nom et prénom du propriétaire",
            },
            {
                "name":    "email",
                "label":   "Courriel",
                "type":    "email",
                "required": True,
                "placeholder": "Pour la confirmation du rendez-vous",
            },
            {
                "name":    "phone",
                "label":   "Téléphone",
                "type":    "tel",
                "required": True,
                "placeholder": "Pour d'éventuels contacts rapides",
            },
            {
                "name":    "pet_name",
                "label":   "Nom de l'animal",
                "type":    "text",
                "required": True,
                "placeholder": "Ex. Luna · Briciola · Pepe",
            },
            {
                "name":    "pet_species",
                "label":   "Espèce et race",
                "type":    "text",
                "required": True,
                "placeholder": "Ex. Chat · Lapin nain · Chien Border Collie",
            },
            {
                "name":    "pet_age",
                "label":   "Âge de l'animal",
                "type":    "text",
                "required": True,
                "placeholder": "Ex. 8 ans · 6 mois",
            },
            {
                "name":    "visit_reason",
                "label":   "Motif de la visite",
                "type":    "textarea",
                "required": True,
                "placeholder":
                    "Ex. Visite préventive annuelle · contrôle "
                    "post-opératoire · questions sur l'alimentation. "
                    "Pour les urgences, appelez l'astreinte. Soin "
                    "préventif privilégié pour toute première visite.",
            },
        ],
        "submit_label": "Envoyer la demande",
        "consent":
            "J'accepte le traitement des données personnelles et "
            "sanitaires de mon animal conformément au RGPD. Le "
            "dossier clinique sera partagé entre les trois "
            "vétérinaires associés du cabinet.",
        "footnote":
            "Pour les urgences cliniques en dehors des horaires "
            "d'ouverture (boiterie soudaine, vomissements "
            "récurrents, prostration, traumatisme), appelez le "
            "numéro d'astreinte 24/7 : +39 333 410 7726. Pour les "
            "patients non encore suivis, nous orientons vers "
            "l'Ospedale Veterinario de Legnaro ou vers la Clinica "
            "San Marco de Veggiano.",
    },
}
