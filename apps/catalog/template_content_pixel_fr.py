"""Pixel — Portfolio Fotografico · French content tree.

Mirrors the shape of ``PIXEL_CONTENT_IT`` exactly — same keys, nesting and
list shapes. Authored Session 39 for the Pixel live i18n rollout of the
cinematic-photographer archetype. Polka/6 Mois long-form reportage register.
"""
from __future__ import annotations

from typing import Any


PIXEL_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Sommaire",       "kind": "home"},
        {"slug": "serie",         "label": "Séries",         "kind": "series_list"},
        {"slug": "biografia",     "label": "Biographie",     "kind": "about"},
        {"slug": "pubblicazioni", "label": "Publications",   "kind": "publications"},
        {"slug": "contatti",      "label": "Contact",        "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial":   "P",
        "logo_word":      "Pixel — Lorenzo Bianchi",
        "logo_short":     "PXL",
        "tag":            "Photographe d'auteur · Milan · Trieste",
        "phone":          "+39 348 211 7720",
        "email":          "studio@lorenzobianchi.photo",
        "address":        "Via Tadino 18 · 20124 Milan",
        "hours_compact":  "Disponible pour commandes · 2026 — 27",
        "license":        "Inscription Tau · Ordre des Photographes Professionnels n° 4421/2014",
        "footer_intro":
            "Photographe d'auteur indépendant. Reportage au long "
            "cours, portrait éditorial et commandes de marque pour "
            "maisons d'édition, galeries et maisons de mode. Représenté "
            "par la Galleria Carla Sozzani pour le tirage fine art.",
        # Primary nav bracket CTA (right-side) — lifted Session 39 per D-047
        "nav_cta":       "Ouvrir une conversation",
        "foot_studio":   "Le studio",
        "foot_pages":    "Sommaire",
        "foot_contact":  "Contact",
        "foot_kit":      "Équipement",
        # EXIF-style footer cells
        "exif_footer": [
            ("Lieu",           "Milan · Trieste"),
            ("Disponible",     "Commandes 2026 — 27"),
            ("Représentation", "Galleria Carla Sozzani · Milan"),
            ("Tirage",         "Atelier Druckwerkstatt · Berlin"),
        ],
        # Footer kit column rows (per-tenant — never inline in skin per D-047)
        "kit_footer_rows": [
            "Mamiya 7II · Sony α7R V",
            "Kodak Portra 400",
            "Tirage · Druckwerkstatt Berlin",
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        # Series counter chip (top-left of hero)
        "series_counter_label": "Série en cours",
        "series_counter_value": "07 / 24",

        # Status pulse on nav (right side)
        "status_pulse": "Disponible · 2026 — 27",

        # Eyebrow + headline
        "eyebrow":   "Photographie d'auteur · 2014 — 2026",
        # All-caps cinematic hero per archetype
        "headline":  "OBSERVER CE QUI RESTE <em>quand la lumière change</em>",
        "subhead":
            "Reportage au long cours, portrait éditorial et "
            "commandes de marque. Je travaille en pellicule moyen "
            "format et en numérique à double capteur — pour des "
            "projets qui demandent dix jours ou trois ans.",
        "primary_cta":   "Ouvrir la série complète",
        "primary_href":  "serie",
        "secondary_cta": "Disponibilités 2026",
        "secondary_href":"contatti",

        # Hero image — fullbleed dominant
        "hero_image":
            "https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?w=2000&q=85&auto=format&fit=crop",
        "hero_image_alt":
            "Vue depuis le port de Trieste à 6h14 du matin · "
            "novembre 2025 · pellicule Kodak Portra 400",

        # EXIF credit cells under hero (4-cell mono bar)
        "hero_credit_cells": [
            ("Boîtier",   "Mamiya 7II"),
            ("Pellicule", "Kodak Portra 400"),
            ("Lieu",      "Porto Vecchio · Trieste"),
            ("Date",      "Novembre 2025"),
        ],

        # Featured series (filmstrip on home — 4 series)
        "filmstrip_label":   "Travaux récents",
        "filmstrip_heading": "QUATRE SÉRIES · 2024 — 2026",
        "filmstrip_intro":
            "Quatre travaux au long cours achevés ces deux dernières années. "
            "Les séries complètes sont accessibles dans la section Séries — "
            "chaque série compte entre vingt et quarante images.",
        # Each: (num, title, discipline, year, slug-for-link)
        "filmstrip": [
            ("07", "Porto Vecchio · Trieste",
             "Reportage au long cours", "2024 — 2026",
             "porto-vecchio-trieste"),
            ("06", "Atelier Velluti & Co.",
             "Commande éditoriale", "2025",
             "atelier-velluti"),
            ("05", "Les maisons de pierre",
             "Reportage d'architecture", "2023 — 2024",
             "case-di-pietra-puglia"),
            ("04", "Portraits du Pô",
             "Portrait d'auteur", "2023",
             "ritratti-del-po"),
        ],

        # Reel — REMOVED per D-068 (Session 36).
        # A short-film claim without a real signed MP4 shipped as a placeholder
        # contradicts the cinematic-photographer identity; the "Play · 3:12" +
        # "Reel · 1080p · 24 fps" meta also trespassed into codec-theatre.
        # Lorenzo's identity is stills — the filmstrip + EXIF cells + series
        # index already carry the cinematic voice. When a genuine Carso reel
        # exists, this block can return with a real `src` and meta pruned of
        # pseudo-technical cues.

        # About excerpt — 3 sentences (full bio on /biografia)
        "about_label":   "Notes autobiographiques",
        "about_heading": "LORENZO BIANCHI",
        "about_excerpt":
            "Né à Trieste en 1986, je vis entre Milan et le Carso "
            "triestin. J'ai commencé par photographier les marchés de "
            "Sarajevo en 2009 et depuis, je n'ai pas changé de "
            "discipline — seulement les durées, la lumière et le "
            "format. Je travaille en pellicule Kodak Portra 400 moyen "
            "format pour les travaux personnels, en numérique Sony à "
            "double capteur pour les commandes.",
        "about_cta":     "Lire la biographie",
        "about_cta_href":"biografia",

        # Recent publications strip (3 selected)
        "publications_label":   "Publié récemment",
        "publications_heading": "PRESSE & ÉDITION · 2025",
        "publications": [
            ("FOAM Magazine n° 64",
             "Portfolio de huit pages sur la série « Porto Vecchio »",
             "Novembre 2025"),
            ("Internazionale n° 1612",
             "Reportage illustré sur les maisons de pierre du Salento",
             "Septembre 2025"),
            ("Domus n° 1102",
             "Commande éditoriale pour le numéro monographique Carlo Scarpa",
             "Avril 2025"),
        ],

        # Final CTA band — commission inquiry
        "cta_label":   "Commandes · disponibilités 2026 — 2027",
        "cta_heading": "[ OUVRIR UNE CONVERSATION ]",
        "cta_intro":
            "Je suis disponible pour des commandes éditoriales, "
            "portraits d'auteur et projets de longue durée jusqu'en "
            "septembre 2027. Les commandes de marque sont étudiées "
            "au cas par cas — je préfère les mandats au long cours.",
        "cta_primary":      "Rédiger une note",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Voir la représentation",
        "cta_secondary_href":"biografia",
    },

    # ─── SERIE (series_list) ────────────────────────────────────
    "serie": {
        "series_counter_label": "Archives",
        "series_counter_value": "24 SÉRIES",
        "status_pulse":         "Disponible · 2026 — 27",

        "eyebrow":   "Archives des séries · 2009 — 2026",
        "headline":  "VINGT-QUATRE SÉRIES, <em>une seule discipline</em>",
        "subhead":
            "L'archive complète des séries signées. Reportage au "
            "long cours, portrait d'auteur, commandes éditoriales. "
            "La sélection présentée couvre les travaux les plus "
            "récents — les séries historiques (2009 — 2018) sont "
            "accessibles sur demande pour étude ou publication.",

        # Discipline filter pills
        "filter_label": "Disciplines",
        "filters": [
            "Toutes",
            "Reportage au long cours",
            "Portrait d'auteur",
            "Commande éditoriale",
            "Reportage d'architecture",
        ],

        # Index intro band
        "index_label": "Sélection 2018 — 2026",
        "index_intro":
            "Cliquer sur la couverture pour ouvrir la série complète. "
            "Chaque série compte entre vingt et quarante images, "
            "avec appareil critique et EXIF de prise de vue.",

        # CTA before footer
        "cta_label":   "Vous cherchez quelque chose de précis ?",
        "cta_heading": "[ ARCHIVES RÉSERVÉES · PRESSE & STUDIO ]",
        "cta_intro":
            "Pour accéder aux archives historiques (2009 — 2018), "
            "pour les demandes de tirage fine art, ou pour commander "
            "un nouveau travail : ouvrez une conversation préliminaire.",
        "cta_primary":      "Écrire au photographe",
        "cta_primary_href": "contatti",

        # Chrome labels shared by serie card + series_detail page.
        # Lifted Session 39 (D-047 lift) — same labels across every post,
        # so they live on the parent serie block rather than on each post.
        "card_arrow_label":        "ouvrir la série",
        "post_discipline_label":   "Discipline",
        "post_period_label":       "Durée",
        "post_location_label":     "Lieu",
        "post_frames_label":       "Images",
        "post_gallery_label":      "Galerie",
        "post_edition_label":      "Édition",
    },

    # ─── BIOGRAFIA (about) ──────────────────────────────────────
    "biografia": {
        "series_counter_label": "Notes autobiographiques",
        "series_counter_value": "1986 — 2026",
        "status_pulse":         "Base · Milan + Trieste",

        "eyebrow":   "Notes autobiographiques · 1986 — 2026",
        "headline":  "LORENZO BIANCHI <em>photographe d'auteur</em>",
        "subhead":
            "Né à Trieste en 1986, je vis entre Milan et le Carso "
            "triestin. J'ai commencé par photographier les marchés de "
            "Sarajevo en 2009 — un essai pour Granta qui n'a jamais "
            "vu le jour. Depuis, je n'ai pas changé de discipline, "
            "seulement les durées, la lumière et le format.",

        # Bio statement — 5 paragraphs
        "statement_label":   "Statement",
        "statement_heading": "POURQUOI JE PHOTOGRAPHIE",
        "statement_paragraphs": [
            "Je photographie pour rester longtemps dans un lieu. La "
            "photographie est la seule discipline qui m'oblige à "
            "revenir. Une série, pour moi, ce sont dix ou vingt "
            "voyages à des mois d'intervalle au même point précis, "
            "jusqu'à ce que quelque chose change assez pour mériter "
            "une prise de vue.",
            "Je travaille en pellicule moyen format — Mamiya 7II, "
            "deux objectifs, Kodak Portra 400. Le ralentissement "
            "mécanique est la discipline, non une coquetterie. Je "
            "développe et tire moi-même, dans une cuisine transformée "
            "en chambre noire pour les petits tirages, chez "
            "Druckwerkstatt Berlin pour le fine art.",
            "Pour les commandes éditoriales j'utilise un système "
            "numérique Sony Alpha à double capteur — la vitesse de "
            "livraison qu'exige une rédaction ne se concilie pas "
            "avec le temps de la pellicule. Mais la manière de "
            "regarder reste la même, le numérique n'est qu'un autre "
            "chariot.",
            "Je suis représenté depuis 2018 par la Galleria Carla "
            "Sozzani de Milan pour le tirage fine art et le marché "
            "secondaire. Pour les commandes éditoriales et de marque "
            "je travaille directement, sans agent — un agent signifie "
            "un filtre entre le photographe et le commanditaire, et "
            "je perds les conversations qui m'intéressent le plus.",
            "J'enseigne la photographie documentaire au CFP Bauer de "
            "Milan depuis 2019 — un jour par semaine, aux étudiants "
            "de deuxième année. C'est le seul engagement fixe du "
            "calendrier du studio. Tout le reste est choisi au projet.",
        ],

        # Camera kit — what we shoot with.
        # Availability label + value lifted Session 39 (D-047).
        "kit_label":                "Équipement de travail",
        "kit_heading":              "QUATRE SYSTÈMES, UN SEUL CHOIX PAR PROJET",
        "kit_availability_label":   "Disponible",
        "kit_availability_value":   "Sur commande",
        "kit": [
            ("01", "Mamiya 7II",
             "Télémétrique moyen format 6 × 7 cm, deux objectifs (80 mm et 43 mm). "
             "Pour les travaux personnels en pellicule — reportage au long "
             "cours et portrait d'auteur.",
             "Pellicule de studio", "Kodak Portra 400 + Tri-X 400"),
            ("02", "Sony α7R V + α7S III",
             "Double capteur (haute résolution + sensibilité). "
             "Pour les commandes éditoriales et les travaux qui exigent "
             "une livraison sous 72 heures.",
             "Objectifs", "GM 24/35/85 + Voigtländer 50/1.5"),
            ("03", "Linhof Master Technika 4 × 5",
             "Chambre photographique pour tirage fine art et portrait "
             "en studio. Réservée à huit-dix prises de vue par an "
             "pour la galerie.",
             "Plan-film", "Ilford FP4+ · Foma Retropan 320"),
            ("04", "Chambre noire · cuisine de Milan",
             "Développement et tirage pour les petites éditions (jusqu'à 18 × 24 cm). "
             "Les tirages fine art sont réalisés par Druckwerkstatt Berlin "
             "en collaboration avec Anna Wedekind.",
             "Papier de studio", "Ilford Multigrade FB Classic"),
        ],

        # Exhibitions + publications timeline (selected — full list /pubblicazioni)
        "timeline_label":   "Expositions & publications · sélection",
        "timeline_heading": "DOUZE ÉTAPES, QUINZE ANS",
        "timeline": [
            ("2026", "FOAM Talent Lounge · Amsterdam",
             "Exposition collective · série « Porto Vecchio »"),
            ("2025", "FOAM Magazine n° 64",
             "Portfolio de huit pages sur la série « Porto Vecchio »"),
            ("2024", "Triennale Milano · « Géographie d'une terre »",
             "Exposition personnelle · série « Les maisons de pierre »"),
            ("2024", "World Press Photo Story of the Year · Finaliste",
             "Catégorie long-term projects, série « Les maisons de pierre »"),
            ("2023", "Internazionale Festival Ferrara",
             "Exposition collective · série « Portraits du Pô »"),
            ("2022", "Photo London · stand Galleria Carla Sozzani",
             "Tirages fine art · sélection 2018 — 2022"),
            ("2021", "Magnum Foundation Grant · finaliste",
             "Catégorie emerging photographer"),
            ("2020", "MAXXI Rome · « Journaux du confinement »",
             "Exposition collective · contribution personnelle 12 tirages"),
            ("2019", "GUP Magazine n° 60 · couverture",
             "Essai illustré sur l'archive des marchés de Sarajevo"),
            ("2018", "FOAM Talent · Amsterdam · sélection",
             "Série « Les trains de nuit »"),
            ("2016", "Prix Marco Pesaresi · finaliste",
             "Reportage italien · « Le passage »"),
            ("2009", "Granta Magazine · essai commandé (jamais publié)",
             "Les marchés de Sarajevo · débuts professionnels"),
        ],

        # Final CTA — commissions
        "cta_heading":      "[ COMMANDES 2026 — 2027 ]",
        "cta_intro":
            "Le studio accepte six à huit commandes par an, choisies "
            "selon le temps disponible et la cohérence avec la "
            "discipline. Les propositions éditoriales et de marque "
            "sont étudiées au cas par cas — je préfère les mandats "
            "au long cours.",
        "cta_primary":      "Ouvrir une conversation",
        "cta_primary_href": "contatti",
    },

    # ─── PUBBLICAZIONI (publications) ───────────────────────────
    "pubblicazioni": {
        "series_counter_label": "Archives de presse",
        "series_counter_value": "47 PUBLICATIONS",
        "status_pulse":         "Mis à jour · janvier 2026",

        "eyebrow":   "Publications & expositions · 2009 — 2026",
        "headline":  "QUARANTE-SEPT PUBLICATIONS, <em>quinze ans</em>",
        "subhead":
            "L'archive complète des publications imprimées, "
            "expositions personnelles et collectives, prix et "
            "résidences. La liste est à jour en janvier 2026 — "
            "d'autres parutions sont prévues au cours de l'année.",

        # Press band — magazine + book covers
        "press_label":   "Presse & édition · principales parutions",
        "press_heading": "REVUES & MONOGRAPHIES",
        "press": [
            {
                "year":    "2025",
                "outlet":  "FOAM Magazine n° 64",
                "type":    "Portfolio éditorial",
                "subject": "Série « Porto Vecchio · Trieste »",
                "format":  "8 pages · impression offset · Amsterdam",
            },
            {
                "year":    "2025",
                "outlet":  "Internazionale n° 1612",
                "type":    "Reportage illustré",
                "subject": "Série « Les maisons de pierre · Salento »",
                "format":  "12 pages · impression rotogravure · Rome",
            },
            {
                "year":    "2025",
                "outlet":  "Domus n° 1102",
                "type":    "Commande éditoriale",
                "subject": "Numéro monographique Carlo Scarpa",
                "format":  "16 pages · impression offset · Milan",
            },
            {
                "year":    "2024",
                "outlet":  "Les maisons de pierre (monographie)",
                "type":    "Volume monographique",
                "subject": "Reportage d'architecture Salento 2023 — 24",
                "format":  "Éditeur Quodlibet · 168 pp. · 24 × 28 cm",
            },
            {
                "year":    "2024",
                "outlet":  "GUP Magazine n° 73",
                "type":    "Essai critique",
                "subject": "Conversation avec Sarah Kelly sur les durées longues",
                "format":  "10 pages · impression offset · Amsterdam",
            },
            {
                "year":    "2023",
                "outlet":  "Vogue Italia · section Photography",
                "type":    "Portrait éditorial",
                "subject": "Portraits du Pô · série sélectionnée",
                "format":  "6 pages · impression offset · Milan",
            },
            {
                "year":    "2022",
                "outlet":  "Aperture n° 248",
                "type":    "Essai illustré",
                "subject": "Réflexion sur la pellicule à l'âge numérique",
                "format":  "8 pages · impression offset · New York",
            },
            {
                "year":    "2019",
                "outlet":  "GUP Magazine n° 60 · couverture",
                "type":    "Couverture + essai illustré",
                "subject": "Archive des marchés de Sarajevo 2009",
                "format":  "Couverture + 14 pp. · impression offset · Amsterdam",
            },
        ],

        # Exhibitions
        "exhibitions_label":   "Expositions · personnelles et collectives",
        "exhibitions_heading": "DOUZE EXPOSITIONS, QUINZE ANS",
        "exhibitions": [
            ("2026", "FOAM Talent Lounge · Amsterdam",
             "Collective · 18 photographes internationaux",
             "Mars — mai 2026"),
            ("2024", "Triennale Milano · « Géographie d'une terre »",
             "Personnelle · série « Les maisons de pierre » · 38 tirages",
             "Septembre — décembre 2024"),
            ("2023", "Internazionale Festival Ferrara",
             "Collective · section long-term projects",
             "Octobre 2023"),
            ("2022", "Photo London · stand Galleria Carla Sozzani",
             "Marché fine art · 14 tirages en vente",
             "Mai 2022"),
            ("2020", "MAXXI Rome · « Journaux du confinement »",
             "Collective · 12 tirages de la contribution personnelle",
             "Septembre — novembre 2020"),
            ("2018", "FOAM Talent · Amsterdam · série sélectionnée",
             "Collective · série « Les trains de nuit » · 16 tirages",
             "Avril — juin 2018"),
        ],

        # Awards & residencies
        "awards_label":   "Prix & résidences",
        "awards_heading": "RECONNAISSANCES",
        "awards": [
            ("2024", "World Press Photo · Finaliste · long-term projects",
             "Série « Les maisons de pierre »"),
            ("2023", "Magnum Foundation · Photography & Social Justice · sélection",
             "Programme de mentorat · 6 mois à New York"),
            ("2021", "Magnum Foundation Grant · finaliste emerging",
             "Bourse d'étude pour travail personnel"),
            ("2020", "Prix Voglino · finaliste",
             "Catégorie reportage italien"),
            ("2016", "Prix Marco Pesaresi · finaliste",
             "Reportage italien · « Le passage »"),
            ("2014", "Prix Angelo Frontoni · sélection",
             "Catégorie photographie documentaire"),
        ],

        # Final CTA — speaking + workshops
        "cta_heading":      "[ CONFÉRENCES · ATELIERS · LECTURES ]",
        "cta_intro":
            "Pour toute demande d'intervention académique (festivals, "
            "écoles, universités), atelier sur la pellicule moyen "
            "format ou lecture éditoriale : ouvrez une conversation. "
            "Les disponibilités se calent avec au moins trois mois "
            "d'anticipation.",
        "cta_primary":      "Ouvrir une conversation",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI (contact) ─────────────────────────────────────
    "contatti": {
        "series_counter_label": "Disponibilités",
        "series_counter_value": "2026 — 27",
        "status_pulse":         "Ouvert aux commandes",

        "eyebrow":   "Conversation préliminaire · sans intermédiaire",
        "headline":  "[ OUVRIR UNE CONVERSATION ] <em>directement</em>",
        "subhead":
            "Les commandes se discutent directement avec le "
            "photographe, sans agent. Pour les propositions "
            "éditoriales, de marque ou pour le tirage fine art "
            "(représentation Galleria Carla Sozzani · Milan) : "
            "rédigez une note. Je réponds sous soixante-douze "
            "heures ouvrées.",

        # Studio info side card (dark style)
        "studio_label":   "Studio opérationnel",
        "studio_address": "Via Tadino 18 · 20124 Milan",
        "studio_area":    "Porta Venezia · entrée latérale · sonnette « Bianchi »",
        "studio_metro":   "MM1 / MM3 Loreto · 4 minutes à pied",
        "studio_hours":   "Disponible sur rendez-vous · jamais à l'improviste",
        "studio_row_address_label":  "Adresse",
        "studio_row_entrance_label": "Entrée",
        "studio_row_metro_label":    "Métro",
        "studio_row_hours_label":    "Disponible",

        # Form fields
        "form_label":   "Note de commande",
        "form_heading": "[ REMPLIR LA NOTE ]",
        "form_intro":
            "Une note de commande est une description structurée "
            "du projet photographique. Pas un brief de marketing — "
            "une conversation préliminaire pour savoir si la "
            "discipline du travail correspond à la mienne.",
        "form_fields": [
            {"name": "name",      "label": "Prénom",        "type": "text",     "required": True,  "placeholder": "Ex. Lorenzo",
             "helper": "Prénom uniquement, merci."},
            {"name": "surname",   "label": "Nom",           "type": "text",     "required": True,  "placeholder": "Ex. Bianchi",
             "helper": "Tel qu'il apparaît en signature."},
            {"name": "organization", "label": "Organisation", "type": "text", "required": False, "placeholder": "Ex. FOAM Magazine",
             "helper": "Si la commande est éditoriale ou de marque."},
            {"name": "email",     "label": "Courriel",      "type": "email",    "required": True,  "placeholder": "lorenzo@foam.org",
             "helper": "Courriel direct · réponse sous 72 heures ouvrées."},
            {"name": "phone",     "label": "Téléphone",     "type": "tel",      "required": False, "placeholder": "+33 ...",
             "helper": "Seulement si vous préférez être rappelé."},
            {"name": "discipline", "label": "Discipline de la commande", "type": "select", "required": True,
             "options": [
                 "À définir en conversation",
                 "Reportage au long cours",
                 "Portrait éditorial",
                 "Commande de marque",
                 "Reportage d'architecture",
                 "Tirage fine art (Galleria Sozzani)",
                 "Atelier / lecture",
             ],
             "helper": "Choisir « à définir » si le périmètre n'est pas encore clair."},
            {"name": "timeline",  "label": "Temps d'exécution", "type": "select", "required": True,
             "options": [
                 "Sous un mois (livraison rapide)",
                 "Trois — six mois (commande éditoriale)",
                 "Six — dix-huit mois (travail au long cours)",
                 "Exploratoire · sans échéance",
             ],
             "helper": "Les délais de livraison déterminent le format (numérique vs pellicule)."},
            {"name": "location",  "label": "Lieu de prise de vue", "type": "text", "required": False,
             "placeholder": "Ex. Salento · Trieste · Sarajevo",
             "helper": "Indiquer ville / région / pays · sert à estimer les voyages."},
            {"name": "story",     "label": "L'histoire que vous voudriez raconter", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "1000 caractères maximum. Une description du sujet, des raisons "
                            "du projet et de la publication prévue. Pas un brief de marketing "
                            "— ici c'est le contenu qui nous intéresse, pas le livrable.",
             "helper": "Si vous ne savez pas par où commencer, écrivez ce qui vous a frappé."},
        ],

        "form_sections": [
            {"num": "01", "title": "Référent",
             "meta": "La personne qui suivra la commande côté commanditaire.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Publication",
             "meta": "Pour comprendre le contexte éditorial ou de marque.",
             "fields": ["organization"]},
            {"num": "03", "title": "Périmètre de la commande",
             "meta": "Les délais de livraison déterminent le format de prise de vue — pellicule vs numérique.",
             "fields": ["discipline", "timeline", "location", "story"]},
            {"num": "04", "title": "Références (facultatives)",
             "meta": "Brief éditorial, chemin de fer, images de référence. Peuvent anticiper la conversation.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "brief_allegato",
            "label":    "Références préliminaires",
            "helper":   "Brief éditorial, chemin de fer, images de référence. "
                        "PDF / DOCX / JPG / PNG · 25 Mo au total maximum.",
            "accept":   ".pdf,.docx,.jpg,.jpeg,.png",
            "multiple": True,
            "primary":  "Glissez les documents ici ou",
            "link":     "parcourir l'archive",
            "meta":     "PDF / DOCX / JPG · 25 Mo max",
        },

        "form_submit_label": "[ ENVOYER LA NOTE ]",
        "form_submit_note":
            "Réponse directement du photographe sous 72 heures ouvrées. "
            "Aucun agent, aucune automatisation de lead.",
        "form_consent":
            "J'accepte le traitement de mes données personnelles "
            "conformément au Règlement UE 679/2016. Les demandes de "
            "commande sont lues et archivées uniquement par le "
            "photographe. Pour le tirage fine art (marché secondaire) "
            "la représentation revient à la Galleria Carla Sozzani.",

        # Sidebar — channels (EXIF style)
        "channels_label": "Canaux directs",
        "channels": [
            ("Studio",          "studio@lorenzobianchi.photo",      "Réponse sous 72 heures"),
            ("Mobile",          "+39 348 211 7720",                 "Lun – Ven · 10h00 – 19h00"),
            ("Tirage fine art", "Galleria Carla Sozzani · Milan",   "Corso Como 10 · +39 02 6555 2223"),
            ("Enseignement",    "CFP Bauer · Milan",                "Documentaire · 2e année · jeudi"),
        ],

        "footnote":
            "Pour le tirage fine art — vente sur le marché secondaire, "
            "éditions limitées, expositions de galerie — la "
            "représentation exclusive revient à la Galleria Carla "
            "Sozzani de Milan depuis 2018. Les demandes commerciales "
            "de tirage doivent être adressées directement à la galerie.",
    },

    # ─── POSTS — drives /serie/<slug>/ series_detail ────────────
    "posts": [
        {
            "slug":        "porto-vecchio-trieste",
            "title":       "Porto Vecchio · Trieste",
            "category":    "Reportage au long cours",
            "discipline":  "Reportage au long cours",
            "year":        "2024 — 2026",
            "duration":    "24 mois · 18 voyages",
            "location":    "Porto Vecchio · Trieste · Italie",
            "frame_count": "47 photographies",
            "edition":     "Édition limitée · 12 + 2 AP par tirage",
            "print_meta": [
                ("Tirage",         "12 + 2 AP par photographie"),
                ("Impression",     "Druckwerkstatt Berlin"),
                ("Papier",         "Hahnemühle Photo Rag Baryta 315 g/m²"),
                ("Représentation", "Galleria Carla Sozzani · Milan"),
            ],
            "lead":
                "Vingt-quatre mois dans le port en cours de "
                "désaffectation de Trieste — une zone de soixante-six "
                "hectares entre la mer Adriatique et la ville, en "
                "transition entre l'archéologie industrielle "
                "habsbourgeoise et un avenir urbain encore indécidable. "
                "Quarante-sept photographies en pellicule Kodak "
                "Portra 400 moyen format.",
            "cover_image":
                "https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Boîtier",    "Mamiya 7II · 80 mm + 43 mm"),
                ("Pellicule",  "Kodak Portra 400 moyen format"),
                ("Période",    "Novembre 2024 — janvier 2026"),
                ("Impression", "Druckwerkstatt Berlin · 30 × 40 cm"),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=1600&q=85&auto=format&fit=crop",
                 "Image 03",
                 "Porto Vecchio à l'aube · Bassin San Marco · novembre 2024"),
                ("https://images.unsplash.com/photo-1505820013142-f86a3439c5b2?w=1600&q=85&auto=format&fit=crop",
                 "Image 11",
                 "Entrepôts abandonnés · février 2025 · 6h14 du matin"),
                ("https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1600&q=85&auto=format&fit=crop",
                 "Image 18",
                 "Vue depuis l'hydrobase · printemps 2025"),
                ("https://images.unsplash.com/photo-1499346030926-9a72daac6c63?w=1600&q=85&auto=format&fit=crop",
                 "Image 24",
                 "Chantier naval désaffecté · été 2025"),
                ("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1600&q=85&auto=format&fit=crop",
                 "Image 31",
                 "Ligne d'eau · octobre 2025 · lumière rasante"),
                ("https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=1600&q=85&auto=format&fit=crop",
                 "Image 39",
                 "Vue finale · janvier 2026 · dernier voyage"),
            ],
            "sections": [
                {
                    "label": "La série",
                    "heading": "Soixante-six hectares, vingt-quatre mois",
                    "body":
                        "Le Porto Vecchio de Trieste est une zone de "
                        "soixante-six hectares sur la mer Adriatique, "
                        "désaffectée depuis 1991 et en attente d'un "
                        "plan d'urbanisme définitif. La série suit son "
                        "état suspendu entre novembre 2024 et janvier "
                        "2026 — dix-huit voyages, trois saisons "
                        "complètes, une seule lumière de tôt le matin. "
                        "Le travail a été publié dans FOAM Magazine "
                        "n° 64 (novembre 2025) et est exposé au FOAM "
                        "Talent Lounge d'Amsterdam à partir de mars 2026.",
                },
                {
                    "label": "La méthode",
                    "heading": "Pellicule, aube, retour",
                    "body":
                        "J'ai toujours photographié au Mamiya 7II et "
                        "en pellicule Kodak Portra 400 moyen format — "
                        "deux objectifs, quatre-vingts et "
                        "quarante-trois millimètres. L'ensemble du "
                        "travail a été fait entre 5h30 et 7h00 du "
                        "matin, avant l'arrivée du personnel de "
                        "surveillance. La lumière de Trieste dans "
                        "cette plage horaire est particulière — la "
                        "bora nocturne nettoie l'air, l'eau du "
                        "bassin est un miroir, le soleil n'est pas "
                        "encore levé sur le Carso.",
                },
                {
                    "label": "L'édition",
                    "heading": "Tirage fine art · douze exemplaires",
                    "body":
                        "L'édition fine art comprend douze tirages + "
                        "deux artist proof par photographie, imprimés "
                        "sur papier Hahnemühle Photo Rag Baryta "
                        "315 g/m² chez Druckwerkstatt Berlin en "
                        "collaboration avec Anna Wedekind. Le format "
                        "de tirage est 30 × 40 cm. La distribution "
                        "fine art est exclusive de la Galleria Carla "
                        "Sozzani de Milan.",
                },
            ],
            "next_label": "Série suivante",
        },
        {
            "slug":        "case-di-pietra-puglia",
            "title":       "Les maisons de pierre · Salento",
            "category":    "Reportage d'architecture",
            "discipline":  "Reportage d'architecture",
            "year":        "2023 — 2024",
            "duration":    "16 mois · 9 voyages",
            "location":    "Salento · Pouilles · Italie",
            "frame_count": "62 photographies",
            "edition":     "Édition monographique · Quodlibet · 168 pp.",
            "print_meta": [
                ("Tirage",         "1 500 exemplaires · premier retirage épuisé"),
                ("Impression",     "Quodlibet · Macerata"),
                ("Papier",         "Munken Pure 130 g/m² · non couché"),
                ("Représentation", "Galleria Carla Sozzani · Milan"),
            ],
            "lead":
                "Seize mois dans les masseries de pierre sèche du "
                "Salento méridional — quarante édifices, aucune "
                "intervention contemporaine. Reportage d'architecture "
                "documentaire, publié en monographie chez Quodlibet "
                "(novembre 2024) et dans Internazionale n° 1612 "
                "(septembre 2025).",
            "cover_image":
                "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Boîtier",    "Mamiya 7II + Sony α7R V"),
                ("Pellicule",  "Kodak Portra 400 + numérique double"),
                ("Période",    "Mars 2023 — juillet 2024"),
                ("Impression", "Volume Quodlibet · 24 × 28 cm · 168 pp."),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1543248939-4296e1fea89b?w=1600&q=85&auto=format&fit=crop",
                 "Image 04",
                 "Masseria San Giovanni · Otrante · printemps 2023"),
                ("https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?w=1600&q=85&auto=format&fit=crop",
                 "Image 12",
                 "Trullo dei Cento Giganti · Locorotondo · été 2023"),
                ("https://images.unsplash.com/photo-1512100356356-de1b84283e18?w=1600&q=85&auto=format&fit=crop",
                 "Image 22",
                 "Masseria Pulicchia · Galatina · automne 2023"),
                ("https://images.unsplash.com/photo-1518131672697-613becd4fab5?w=1600&q=85&auto=format&fit=crop",
                 "Image 31",
                 "Lamia intérieure · Sannicola · janvier 2024"),
                ("https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600&q=85&auto=format&fit=crop",
                 "Image 41",
                 "Vue du muret de pierre sèche · Specchia · mars 2024"),
                ("https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=1600&q=85&auto=format&fit=crop",
                 "Image 53",
                 "Cour intérieure · Tricase · juillet 2024"),
            ],
            "sections": [
                {
                    "label": "La série",
                    "heading": "Quarante édifices, seize mois",
                    "body":
                        "Le reportage documente quarante édifices de "
                        "pierre sèche du Salento méridional — "
                        "masseries, lamies, trulli mineurs, pajare. "
                        "L'idée était de les documenter avant une "
                        "éventuelle restauration ou démolition, en "
                        "collaboration avec le Centre d'études "
                        "salentines de Lecce. Seize mois de travail, "
                        "neuf voyages, soixante-deux photographies "
                        "sélectionnées.",
                },
                {
                    "label": "La méthode",
                    "heading": "Double format pour la documentation",
                    "body":
                        "À la différence des travaux personnels, j'ai "
                        "travaillé ici à double format — Mamiya 7II "
                        "pour les extérieurs en pellicule et Sony "
                        "α7R V pour les intérieurs en numérique (pour "
                        "la documentation architecturale précise). "
                        "Les deux formats cohabitent dans le volume "
                        "Quodlibet sans distinction éditoriale "
                        "évidente — la pellicule et le numérique, "
                        "une fois imprimés, deviennent "
                        "indiscernables à 24 × 28 cm.",
                },
                {
                    "label": "Le volume",
                    "heading": "Cent soixante-huit pages, Quodlibet",
                    "body":
                        "Le volume monographique « Les maisons de "
                        "pierre » a été publié par Quodlibet "
                        "(novembre 2024) avec un essai critique de "
                        "Salvatore Settis. Cent soixante-huit pages, "
                        "format 24 × 28 cm, reliure cousue, papier "
                        "non couché Munken Pure 130 g/m². Tirage de "
                        "1 500 exemplaires, premier retirage épuisé "
                        "en trois mois. Sélection finaliste au World "
                        "Press Photo 2024 catégorie long-term projects.",
                },
            ],
            "next_label": "Série suivante",
        },
        {
            "slug":        "ritratti-del-po",
            "title":       "Portraits du Pô",
            "category":    "Portrait d'auteur",
            "discipline":  "Portrait d'auteur",
            "year":        "2023",
            "duration":    "8 mois · 7 voyages",
            "location":    "Delta du Pô · Vénétie · Italie",
            "frame_count": "28 photographies",
            "edition":     "Publié · Vogue Italia photography",
            "print_meta": [
                ("Tirage",         "8 + 2 AP par tirage sélectionné"),
                ("Impression",     "Tirages personnels · cuisine de Milan"),
                ("Papier",         "Ilford Multigrade FB Classic"),
                ("Représentation", "Galleria Carla Sozzani · Milan"),
            ],
            "lead":
                "Vingt-huit portraits de pêcheurs, ramasseuses de "
                "coques et conducteurs de péniche du Delta du Pô "
                "vénète. Huit mois de travail entre le printemps et "
                "l'automne 2023, publié dans la section Photography "
                "de Vogue Italia (décembre 2023) et exposé au "
                "Festival Internazionale de Ferrare (octobre 2023).",
            "cover_image":
                "https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Boîtier",    "Mamiya 7II · 80 mm"),
                ("Pellicule",  "Kodak Portra 400 moyen format"),
                ("Période",    "Avril — novembre 2023"),
                ("Impression", "Tirages personnels · cuisine de Milan"),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=1600&q=85&auto=format&fit=crop",
                 "Image 01",
                 "Aldo · pêcheur · Pila · mai 2023"),
                ("https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=1600&q=85&auto=format&fit=crop",
                 "Image 06",
                 "Maria · ramasseuse de coques · Goro · juin 2023"),
                ("https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=1600&q=85&auto=format&fit=crop",
                 "Image 12",
                 "Carlo et Giuseppe · frères pêcheurs · juillet 2023"),
                ("https://images.unsplash.com/photo-1502323777036-f29e3972d82f?w=1600&q=85&auto=format&fit=crop",
                 "Image 17",
                 "Anna · restauratrice · septembre 2023"),
                ("https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=1600&q=85&auto=format&fit=crop",
                 "Image 22",
                 "Luca · conducteur de péniche · octobre 2023"),
                ("https://images.unsplash.com/photo-1521252659862-eec69941b071?w=1600&q=85&auto=format&fit=crop",
                 "Image 28",
                 "Portrait final · novembre 2023 · dernière lumière"),
            ],
            "sections": [
                {
                    "label": "La série",
                    "heading": "Vingt-huit personnes, huit mois",
                    "body":
                        "Une série de vingt-huit portraits de celles "
                        "et ceux qui vivent le Delta du Pô vénète "
                        "comme lieu de travail — pêcheurs, "
                        "ramasseuses de coques, restaurateurs, "
                        "conducteurs de péniche. Huit mois de travail "
                        "entre avril et novembre 2023, sept voyages "
                        "dans les deux provinces (Rovigo + Ferrare). "
                        "Chaque portrait est précédé d'au moins une "
                        "journée passée avec le sujet — jamais de "
                        "séances « expresses ».",
                },
                {
                    "label": "La méthode",
                    "heading": "Un seul boîtier, une seule lumière",
                    "body":
                        "Tous les portraits ont été faits au Mamiya "
                        "7II et au quatre-vingts millimètres, en "
                        "lumière naturelle disponible — pas de flash, "
                        "pas de panneaux diffuseurs. La pellicule "
                        "est toujours la Kodak Portra 400, développée "
                        "à la maison. Le choix d'un seul objectif "
                        "(au lieu d'un parc de trois ou quatre) est "
                        "une discipline formelle — il oblige à se "
                        "déplacer par rapport au sujet, non à "
                        "tourner la bague de l'objectif.",
                },
                {
                    "label": "La publication",
                    "heading": "Vogue Italia · Festival Ferrare",
                    "body":
                        "La série a été publiée dans la section "
                        "Photography de Vogue Italia (décembre 2023, "
                        "six pages) et exposée en exposition "
                        "collective au Festival Internazionale de "
                        "Ferrare (octobre 2023, douze tirages "
                        "sélectionnés). Un tirage est entré dans la "
                        "collection permanente du MAXXI de Rome.",
                },
            ],
            "next_label": "Série suivante",
        },
    ],
}
