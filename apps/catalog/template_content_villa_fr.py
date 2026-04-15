"""Phase 2g3.7 · Session 53 · Villa — FR native-voice tree. Editorial-concierge private-advisory voice."""
from __future__ import annotations

from typing import Any


VILLA_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Demeures",    "kind": "home"},
        {"slug": "collezione", "label": "Collection",  "kind": "blog_list"},
        {"slug": "territorio", "label": "Territoires", "kind": "about"},
        {"slug": "studio",     "label": "Le Cabinet",  "kind": "team"},
        {"slug": "esperienza", "label": "Expérience",  "kind": "services"},
        {"slug": "concierge",  "label": "Concierge",   "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":   "V",
        "logo_word":      "Villa Prestige",
        "logo_subline":   "Private Advisory · depuis 1998",
        "tag":            "Collection printemps 2026 · Portefeuille N° 03",
        "phone":          "concierge@villaprestige.it",
        "phone_label":    "Ligne confidentielle du concierge",
        "email":          "concierge@villaprestige.it",
        "email_label":    "Concierge privé",
        "address":        "Via Montenapoleone 17 · 20121 Milan",
        "hours_compact":  "Visites sur rendez-vous uniquement · Lun–Ven 10–19 · Sam sur demande",
        "hours_footer_rows": [
            "Rencontres dans nos bureaux · concierge privé",
            "Langues : italien · english · français",
        ],
        "license":        "Insc. RIEA Milan N° 2841 · TVA IT07324110984 · Registre des conseillers privés",
        "footer_intro":
            "Villa Prestige — cabinet de private advisory pour les demeures d'auteur en Italie et sur la "
            "Côte d'Azur. Un portefeuille resserré, un interlocuteur unique, une discrétion absolue. Nous "
            "sélectionnons des demeures historiques et contemporaines exclusivement pour une clientèle "
            "privée et des family offices, après une évaluation à deux niveaux : signature architecturale "
            "et cohérence du territoire.",

        # Nav reservation CTA (private viewing)
        "nav_cta":         "Demander une visite privée",
        "nav_cta_kind":    "appointment",
        "nav_cta_short":   "Demander une visite",

        # Footer labels
        "foot_studio":   "Le cabinet",
        "foot_pages":    "Plan du site",
        "foot_contact":  "Concierge",
        "foot_offices":  "Bureaux",
        "offices_footer_rows": [
            "Milan · Montenapoleone 17",
            "Portofino · bureau concierge",
            "Saint-Tropez · sur rendez-vous",
        ],
        "office_rows": [
            "Milan · Montenapoleone 17",
            "Portofino · bureau concierge",
            "Saint-Tropez · sur rendez-vous",
        ],

        # Cross-page editorial meta-strip labels (D-047)
        "dossier_label":        "Dossier",
        "portfolio_label":      "Portefeuille",
        "territorio_label":     "Territoire",
        "superficie_label":     "Surface",
        "provenance_label":     "Provenance",
        "access_label":         "Accès",
        "availability_label":   "Disponibilité",
        "price_note":           "Prix sur demande",
        "nda_required_label":   "Accord de confidentialité requis avant le dossier",
        "viewing_on_request":   "Disponible sur rendez-vous uniquement",
        "referent_label":       "Interlocuteur unique",
        "concierge_line_label": "Ligne concierge",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        # Fullbleed editorial cover
        "cover_location": "Portofino · Ligurie",
        "cover_image_credit": "Collection de printemps · dossier 03 / 18",
        "cover_image":
            "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=2200&h=1400&fit=crop",

        # Eyebrow + serif drama
        "eyebrow":          "Villa Prestige · Private Advisory · Italie & Côte d'Azur",
        "headline":         "Demeures <em>d'auteur</em>, pour ceux qui savent les reconnaître.",
        "sub":
            "Un portefeuille resserré de résidences privées — historiques et contemporaines — "
            "présenté uniquement sur rendez-vous. Visites confidentielles, dossier éditorial dédié, "
            "négociation discrète : de la première rencontre à la signature notariale, un seul interlocuteur.",

        # Hero wordmark + counter chip (from DNA)
        "hero_wordmark":        "Villa Prestige",
        "hero_location":        "Portofino · Collection printemps 2026",
        "hero_counter_label":   "Demeure à l'affiche",
        "hero_counter_value":   "N° 03 / 18",
        "hero_series_label":    "À l'affiche",
        "hero_series_title":    "« Villa Aurelia » · Portofino",
        "hero_series_note":
            "Demeure historique de 1922, parc de trois hectares dominant le golfe. Quatre cents "
            "mètres carrés, bibliothèque signée, piscine à débordement face à l'île Palmaria.",
        "primary_cta":          "Demander une visite privée",
        "primary_cta_href":     "concierge",
        "secondary_cta":        "Collection de printemps",
        "secondary_cta_href":   "collezione",

        # Editorial credit cells — fullbleed hero bottom strip
        "hero_credit_cells": [
            ("Collection", "N° 03 / 18"),
            ("Territoire", "Portofino · Ligurie"),
            ("Surface",    "400 m² · parc 30 000 m²"),
            ("Accès",      "Sur rendez-vous uniquement"),
        ],

        # Signature properties strip — 4 dossier cards (2-up editorial grid)
        "signature_label":   "Collection de printemps",
        "signature_heading": "Demeures <em>choisies</em> pour cette saison.",
        "signature_intro":
            "Chaque propriété n'est présentée qu'après une évaluation à deux niveaux — signature "
            "architecturale et cohérence du territoire. La liste complète est remise sur demande, "
            "sous forme de dossier éditorial signé par l'interlocuteur dédié.",
        "signature": [
            {
                "index":       "01",
                "title":       "Villa Aurelia",
                "territorio":  "Portofino · Ligurie",
                "superficie":  "400 m² · parc 30 000 m²",
                "provenance":  "Années 1920 · signature Piacentini",
                "availability":"Trois jours disponibles",
                "slug":        "villa-aurelia-portofino",
                "image":
                    "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "02",
                "title":       "Castello di Monterò",
                "territorio":  "Chianti Classico · Toscane",
                "superficie":  "1 200 m² · 18 hectares",
                "provenance":  "XIIe siècle · restauration 2014",
                "availability":"Mandat exclusif",
                "slug":        "castello-di-montero-chianti",
                "image":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "03",
                "title":       "Penthouse Quadronno",
                "territorio":  "Milan · Magenta",
                "superficie":  "380 m² · terrasse 180 m²",
                "provenance":  "Dernier étage unique · vue Duomo",
                "availability":"Sur rendez-vous",
                "slug":        "penthouse-quadronno-milano",
                "image":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "04",
                "title":       "Mas de la Mer",
                "territorio":  "Saint-Tropez · Côte d'Azur",
                "superficie":  "550 m² · vigne privée",
                "provenance":  "XVIIIe siècle · certifié",
                "availability":"Nouveauté",
                "slug":        "mas-de-la-mer-saint-tropez",
                "image":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
        ],
        "signature_link_all":  "Découvrir la collection complète  →",
        "signature_link_href": "collezione",

        # Territory ribbon — continental destinations
        "territory_label":  "Territoires de référence",
        "territory":        ["PORTOFINO", "CHIANTI CLASSICO", "COSTA SMERALDA", "LAGO DI COMO", "SAINT-TROPEZ", "CAPRI", "VAL D'ORCIA"],

        # Private advisor block
        "advisor_label":    "Conseiller privé",
        "advisor_heading":  "Un seul <em>interlocuteur</em>, du premier dossier à la signature.",
        "advisor_intro":
            "Chaque client privé est suivi personnellement par son conseiller, de l'envoi du "
            "premier dossier éditorial à la signature notariale. Jamais plus de huit mandats "
            "actifs par conseiller, afin de garantir une présence réelle et une discrétion absolue.",
        "advisor_name":     "Alessandra Visconti di Modrone",
        "advisor_role":     "Directrice clientèle privée · depuis 2011",
        "advisor_bio":
            "Quinze années entre Savills, Knight Frank et Sotheby's International Realty "
            "(Londres · Milan · Portofino). Elle a conduit personnellement plus de quatre-vingts "
            "transactions privées en Italie et sur la Côte d'Azur, pour des familles européennes, "
            "américaines et asiatiques. Chaque client est accompagné par elle, de la première "
            "rencontre confidentielle à la signature notariale.",
        "advisor_portrait":
            "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
        "advisor_cta":      "Demander un premier entretien",
        "advisor_cta_href": "concierge",

        # Editorial storytelling — the maison's numbers (discreet stats — counters OK)
        "numbers_label":    "Le cabinet en chiffres",
        "numbers_heading":  "Un portefeuille <em>resserré</em>, une présence totale.",
        "numbers": [
            ("26",   "années de private advisory"),
            ("42",   "demeures en portefeuille"),
            ("9",    "conseillers privés dédiés"),
            ("150",  "family offices accompagnés"),
        ],
        "numbers_note":
            "Jamais plus de cinquante mandats simultanés. Chaque dossier passe par le bureau de la "
            "direction avant son entrée en collection.",

        # Press ribbon
        "press_label":    "Éditorial",
        "press_intro":    "Paru dans",
        "press_items":    [
            "Financial Times · How to Spend It",
            "Monocle",
            "Robb Report",
            "Corriere Living",
            "AD Italia",
        ],

        # Editorial storytelling panel — closing private-viewing band
        "private_label":    "Visite privée",
        "private_heading":  "Une heure en salon réservé, <em>le dossier entre vos mains.</em>",
        "private_intro":
            "La rencontre dans nos bureaux se tient sur rendez-vous, en présence de l'interlocuteur "
            "dédié. Nous préparons à l'avance les dossiers éditoriaux des demeures compatibles avec "
            "le profil du client et réservons un salon où les vues sont projetées en grand format. "
            "Le service est gracieux et strictement confidentiel.",
        "private_primary":       "Demander une visite privée",
        "private_primary_href":  "concierge",
        "private_secondary":     "Découvrir l'expérience",
        "private_secondary_href":"esperienza",
    },

    # ─── COLLEZIONE — signature properties list (blog_list) ───
    "collezione": {
        "eyebrow":   "Collection printemps 2026 · dossiers 01 – 14",
        "headline":  "Quatorze <em>demeures d'auteur</em>, en attente de leur interlocuteur.",
        "intro":
            "La collection est ouverte exclusivement aux clients sous accord de confidentialité. "
            "Chaque dossier comprend la provenance architecturale, un plan éditorial, le territoire "
            "et une brève histoire de la demeure. Les prix sont communiqués directement par "
            "l'interlocuteur après la première rencontre confidentielle.",

        # Lead post / hero dossier
        "lead_image":
            "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=1600&h=1000&fit=crop",

        # Filters by territorio / provenance / availability
        "filter_label":  "Sélection",
        "filter_groups": [
            {
                "label":   "Territoire",
                "options": ["Tous", "Portofino", "Chianti Classico", "Milan", "Côte d'Azur", "Capri", "Lago di Como", "Val d'Orcia"],
            },
            {
                "label":   "Provenance",
                "options": ["Toutes", "XVIIe–XVIIIe siècle", "Début du XXe · signature d'auteur", "Contemporain · restauration récente", "Dernier étage unique"],
            },
            {
                "label":   "Disponibilité",
                "options": ["Ouvertes", "Nouveauté", "Exclusive", "Sur rendez-vous uniquement"],
            },
        ],
        "sort_label":    "Trier par",
        "sort_options":  ["Territoire", "Provenance", "Plus récentes", "Exclusives"],

        "result_count":    "14 dossiers dans la collection de printemps",
        "result_subtitle": "Mise à jour chaque premier jeudi du mois",

        "footer_note_label": "Entrée en collection",
        "footer_note":
            "La collection été 2026 ouvre le jeudi 28 mai. Les clients déjà sous accord de "
            "confidentialité conservent une priorité absolue sur tout nouveau dossier. Pour "
            "rejoindre la liste confidentielle : écrire directement au concierge de la maison.",
    },

    # ─── TERRITORIO (about) — editorial territorio cards ──────
    "territorio": {
        "eyebrow":   "Territoires de référence · sept géographies privées",
        "headline":  "Le <em>paysage</em> est la première signature d'une demeure.",
        "intro":
            "Nous intervenons exclusivement sur sept territoires italiens et français. Chacun "
            "dispose d'un interlocuteur résident, d'une archive éditoriale dédiée, d'un réseau "
            "d'architectes de confiance. Nous ne travaillons pas hors de ces géographies — c'est "
            "ainsi que nous garantissons une connaissance réelle des demeures, du voisinage, "
            "des vents dominants.",

        # Editorial statement
        "statement_label":   "Manifeste",
        "statement_heading": "Sept territoires, <em>sept archives privées.</em>",
        "statement_text":
            "Chaque territoire est suivi par un interlocuteur qui y réside depuis au moins dix ans. "
            "Nous connaissons les demeures avant qu'elles n'arrivent sur le marché — nous les "
            "suivons souvent depuis plusieurs générations de propriétaires. Notre archive comprend "
            "les données cadastrales historiques, les études paysagères, les relations avec les "
            "communes et les services compétents du patrimoine.",

        # 6 territorio cards — history, provenance, architects, property count
        "territories_label":   "Les sept territoires",
        "territories_heading": "Les géographies <em>de la collection.</em>",
        "territories_intro":
            "Du promontoire de Portofino aux vignes de Saint-Tropez, des collines du Chianti à "
            "la Costa Smeralda. Chaque territoire a sa saison d'entrée, sa dorsale architecturale, "
            "son registre de familles.",
        "territories": [
            {
                "name":      "Portofino",
                "region":    "Ligurie · golfe du Tigullio",
                "history":   "Le promontoire fréquenté par les familles milanaises depuis le second après-guerre. Demeures en surplomb de la mer, terrasses sur la baie de San Fruttuoso, jardins clos de bougainvillées et d'oliviers centenaires. La lumière de fin de printemps est le meilleur document.",
                "architects":"Gio Ponti · Gae Aulenti · Umberto Riva · restaurations récentes A. Citterio",
                "count":     "9 demeures en collection",
                "since":     "Interlocuteur résident depuis 2008",
                "image":
                    "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Chianti Classico",
                "region":    "Toscane · Gaiole – Radda – Castellina",
                "history":   "La dorsale du Chianti entre Sienne et Florence, riche en châteaux médiévaux et en pievi restaurées. Demeures habitées avec vignes de production, oliveraies séculaires et caves en sous-sol. Le territoire privilégie la restauration conservatrice sous la tutelle du patrimoine de Florence.",
                "architects":"restaurations de Tobia Scarpa · Massimo Carmassi · studio ACPV",
                "count":     "7 demeures en collection",
                "since":     "Interlocuteur résident depuis 2011",
                "image":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Costa Smeralda",
                "region":    "Sardaigne · Porto Cervo – Porto Rotondo",
                "history":   "Le littoral dessiné dans les années 1960 par le Prince Karim Aga Khan. Villas conçues par Jacques Couëlle et Luigi Vietti, granit local et toitures de genévrier. Terrasses de pierre en surplomb de la mer, criques privées accessibles uniquement à pied ou en tender.",
                "architects":"Jacques Couëlle · Luigi Vietti · Savin Couëlle · restaurations récentes A. Citterio",
                "count":     "5 demeures en collection",
                "since":     "Interlocuteur résident depuis 2014",
                "image":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Lago di Como",
                "region":    "Lombardie · Cernobbio – Tremezzo – Bellagio",
                "history":   "Les villas historiques du Lario, de la Villa d'Este à la Villa Balbianello. Parcs botaniques sculptés au XVIIIe siècle, darses privées, belvédères de jasmin. Propriétés souvent classées, dont les restaurations se conduisent de concert avec le patrimoine de Milan.",
                "architects":"villas historiques · Pelagio Palagi · restaurations de Lissoni Casal Ribeiro",
                "count":     "6 demeures en collection",
                "since":     "Interlocuteur résident depuis 2010",
                "image":
                    "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Saint-Tropez",
                "region":    "Côte d'Azur · Var · Pampelonne",
                "history":   "Le Var intérieur, collines entre Ramatuelle et Gassin. Mas provençaux originels des XVIIe–XVIIIe siècles, certains avec vigne de production AOP Côtes de Provence. Maisons à distance discrète de la mer, à une demi-heure du port de Saint-Tropez.",
                "architects":"François Catroux · Jacques Grange · Studio KO · restaurations traditionnelles",
                "count":     "4 demeures en collection",
                "since":     "Bureau concierge depuis 2016",
                "image":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Capri & Val d'Orcia",
                "region":    "Capri · Toscane méridionale · Pienza – Montalcino",
                "history":   "Deux territoires parents, par la rareté et la réserve familiale. À Capri, maisons en terrasses face aux Faraglioni, souvent transmises sur trois générations. En Val d'Orcia, domaines agricoles avec pieve romane et vigne de Brunello, propriétés UNESCO soumises à protection stricte.",
                "architects":"Capri · Francesco Venezia · tradition caprese locale ; Val d'Orcia · Matteo Nunziati · Studio Perruccio",
                "count":     "5 demeures en collection",
                "since":     "Interlocuteurs résidents depuis 2013",
                "image":
                    "https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
        ],
        "territory_card_cta": "Demander le dossier territoire  →",
        "territory_card_cta_href": "concierge",

        # Closing — the referent promise
        "referent_label":   "L'interlocuteur résident",
        "referent_heading": "Nous connaissons les maisons <em>avant</em> leur mise sur le marché.",
        "referent_text":
            "L'interlocuteur résident n'est pas un consultant à la demande : c'est une personne qui "
            "vit sur le territoire depuis au moins dix ans, parle la langue locale, connaît les "
            "services du patrimoine et les familles historiques. Beaucoup de demeures de la "
            "collection nous parviennent par la parole d'un ami commun, non par le marché — "
            "c'est ainsi que ces propriétés se sont toujours transmises, entre personnes qui se "
            "font confiance.",

        # Discreet stats — territories in numbers
        "stats_label":      "Territoires en chiffres",
        "stats": [
            ("7",   "territoires de référence"),
            ("36",  "demeures historiques en archive"),
            ("18",  "architectes d'auteur associés"),
            ("26",  "années de présence continue"),
        ],
    },

    # ─── STUDIO (team) — private advisors ─────────────────────
    "studio": {
        "eyebrow":  "Le cabinet · neuf conseillers privés · Milan Portofino Saint-Tropez",
        "headline": "Neuf conseillers, <em>jamais plus de huit mandats chacun.</em>",
        "intro":
            "Le cabinet est une maison de conseillers privés : chacun d'entre nous a fait ses armes "
            "dans les grandes maisons internationales — Sotheby's International Realty, Knight Frank, "
            "Savills, Christie's Real Estate — et exerce aujourd'hui en toute indépendance, avec un "
            "portefeuille resserré. Nous ne portons pas d'enseigne, seulement des dossiers. Nous ne "
            "vendons rien sous pression.",

        # Director hero card — Alessandra Visconti
        "director_label":   "Direction",
        "director_name":    "Alessandra Visconti di Modrone",
        "director_role":    "Directrice clientèle privée · fondatrice · depuis 1998",
        "director_text":
            "Elle fonde Villa Prestige à Milan en 1998, après huit années chez Sotheby's "
            "International Realty Londres. Elle a conduit personnellement plus de quatre-vingts "
            "transactions privées en Italie et sur la Côte d'Azur — de la Villa Aurelia de "
            "Portofino au Castello di Monterò en Chianti — pour des familles européennes, "
            "américaines, asiatiques et du Moyen-Orient. Elle signe dans Monocle et Corriere "
            "Living une chronique annuelle sur le marché des demeures historiques.",
        "director_portrait":
            "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=800&h=1100&fit=crop",
        "director_quote":
            "« Nous ne choisissons pas les demeures pour leur prix. Nous choisissons les demeures "
            "qui nous restent en mémoire après une seule visite. Quatre-vingts pour cent des "
            "propriétés qui nous parviennent sont écartées avant leur entrée en collection. »",
        "director_quote_attribution": "Alessandra Visconti di Modrone · Monocle · mars 2025",

        # 4 private advisors
        "advisors_label":   "Conseillers privés",
        "advisors_heading": "Un <em>interlocuteur unique</em>, du premier dossier à la signature.",
        "advisors_intro":
            "Chaque client est accompagné personnellement par un conseiller nommé au début du "
            "mandat. Jamais d'intermédiaire, jamais de relais. Si le client souhaite un second "
            "avis, le cabinet met à disposition un second conseiller en qualité consultative, "
            "toujours sous le même toit de confidentialité.",
        "advisors": [
            {
                "name":      "Francesco Medici di Porrena",
                "role":      "Conseiller senior · territoire Chianti & Val d'Orcia",
                "bio":
                    "Douze années chez Knight Frank Florence, spécialisé dans la restauration "
                    "conservatrice des demeures historiques du Chianti Classico. Diplôme "
                    "d'architecture à Florence, master à la Bartlett de Londres. Il conduit "
                    "personnellement toutes les négociations en Toscane méridionale.",
                "territories":"Chianti Classico · Val d'Orcia · Florence",
                "since":     "Au cabinet depuis 2014",
                "portrait":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Italien · English · Français",
            },
            {
                "name":      "Élodie Charbonneau",
                "role":      "Conseillère senior · territoire Côte d'Azur & Capri",
                "bio":
                    "Dix années chez Savills Paris et Christie's Real Estate Monte-Carlo. "
                    "Curatrice de ventes privées pour des collectionneurs français et "
                    "américains sur la Côte d'Azur. Spécialisée dans les mas provençaux "
                    "authentiques et les villas d'auteur. Responsable du bureau concierge "
                    "de Saint-Tropez.",
                "territories":"Saint-Tropez · Monaco · Capri",
                "since":     "Au cabinet depuis 2016",
                "portrait":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Français · English · Italien",
            },
            {
                "name":      "Arianna Testa Piccolomini",
                "role":      "Conseillère senior · territoire Portofino & Lago di Como",
                "bio":
                    "Huit années chez Sotheby's International Realty Milan, puis consultante "
                    "indépendante pour deux family offices de Brescia et du Piémont. "
                    "Résidente à Portofino depuis dix ans, elle connaît personnellement les "
                    "familles historiques du promontoire. Langues de travail : italien, "
                    "anglais, allemand.",
                "territories":"Portofino · Lago di Como · Milan",
                "since":     "Au cabinet depuis 2017",
                "portrait":
                    "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Italien · English · Deutsch",
            },
            {
                "name":      "Omar Khoury",
                "role":      "Conseiller clientèle privée · clients asiatiques & Moyen-Orient",
                "bio":
                    "Neuf années entre Knight Frank Dubaï et Christie's Hong Kong. Spécialisé "
                    "dans l'accueil d'une clientèle privée venue de Hong Kong, Singapour, "
                    "Doha, Riyad et Dubaï. Il coordonne les traductions et les certifications "
                    "notariales internationales. Résident entre Milan et Portofino.",
                "territories":"clients asiatiques · Émirats · Golfe persique",
                "since":     "Au cabinet depuis 2019",
                "portrait":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "العربية · English · Français · 中文 (notions)",
            },
        ],

        # Legal / fiscal partner ribbon
        "partners_label":   "Partenaires institutionnels",
        "partners_heading": "Les partenaires <em>juridiques et fiscaux</em> du cabinet.",
        "partners_intro":
            "Villa Prestige ne rédige pas les actes. Chaque négociation est accompagnée par des "
            "partenaires institutionnels sélectionnés — études notariales, avocats internationaux, "
            "fiscalistes du patrimoine — opérant sous le même toit de confidentialité. Le client "
            "signe un mandat direct avec eux, distinct du nôtre, aux honoraires transparents.",
        "partners": [
            ("Studio Notarile Baldi-Corsini",     "Milan · notaire des familles lombardes"),
            ("Gattai Minoli Agostinelli",         "Milan · droit immobilier international"),
            ("Chiomenti",                          "Milan · fiscalité patrimoniale pour family offices"),
            ("Ughi e Nunziante",                   "Rome · patrimoine et beaux-arts"),
            ("Cabinet Bredin Prat",                "Paris · transactions Côte d'Azur"),
        ],

        # Press / editorial mentions
        "press_label":   "Éditorial",
        "press_heading": "Mentions récentes <em>du cabinet.</em>",
        "press_items": [
            {
                "magazine": "Financial Times · How to Spend It",
                "issue":    "Printemps 2026",
                "title":    "The quiet sellers of the Italian coast",
                "byline":   "Portrait · par Bill Prince",
            },
            {
                "magazine": "Monocle",
                "issue":    "Issue 181",
                "title":    "The Chianti Classico revival",
                "byline":   "Reportage · par Josh Fehnert",
            },
            {
                "magazine": "Robb Report",
                "issue":    "Avril 2025",
                "title":    "Nine villas, one director",
                "byline":   "Portrait · par Laurie Kahle",
            },
            {
                "magazine": "Corriere Living",
                "issue":    "Janvier 2026",
                "title":    "Le marché des demeures historiques, vu de Milan",
                "byline":   "Chronique annuelle · signée Alessandra Visconti di Modrone",
            },
            {
                "magazine": "AD Italia",
                "issue":    "Novembre 2025",
                "title":    "Villa Aurelia · le retour d'une icône de Portofino",
                "byline":   "Photographie · Gianluca Ruotolo",
            },
        ],

        # Studio in numbers
        "numbers_label":   "Le cabinet en chiffres",
        "numbers": [
            ("26",   "années depuis la fondation"),
            ("9",    "conseillers privés dédiés"),
            ("42",   "demeures en collection"),
            ("7",    "territoires de référence"),
            ("150",  "family offices accompagnés"),
            ("91",   "transactions privées depuis 2015"),
        ],

        # Closing visit CTA
        "visit_label":     "Rencontre dans nos bureaux",
        "visit_heading":   "Un premier <em>entretien confidentiel</em> dans les bureaux de Milan ou Portofino.",
        "visit_text":
            "Nous recevons exclusivement sur rendez-vous, dans les bureaux de Milan et Portofino, "
            "ou au bureau concierge de Saint-Tropez. La première rencontre est un entretien "
            "confidentiel — elle n'engage aucun mandat — au cours duquel nous précisons le "
            "profil du client et signons l'accord de confidentialité qui donne accès aux dossiers.",
        "visit_primary":      "Demander le premier entretien",
        "visit_primary_href": "concierge",
    },

    # ─── ESPERIENZA (services) — private-viewing process ─────
    "esperienza": {
        "eyebrow":  "L'expérience · cinq étapes dans la discrétion",
        "headline": "Du premier <em>dossier</em> à la signature notariale.",
        "intro":
            "Nous accompagnons le client à travers cinq étapes, chacune confidentielle et "
            "documentée. Le parcours dure en moyenne quatre mois pour les propriétés prêtes à "
            "l'acte, jusqu'à douze pour les demeures historiques soumises à protection paysagère. "
            "Aucune étape n'est obligatoire — le client peut interrompre le mandat à tout moment, "
            "sans pénalité.",

        # 5-step private-viewing process
        "process_label":   "Le parcours",
        "process_heading": "Cinq étapes, <em>un seul interlocuteur.</em>",
        "process_intro":
            "Chaque étape est suivie personnellement par le conseiller nommé au début du "
            "mandat. Le client peut à tout moment demander à s'entretenir avec la direction — "
            "Alessandra Visconti di Modrone répond personnellement sous un jour ouvré.",
        "process": [
            {
                "n":        "01",
                "title":    "Demande du dossier",
                "duration": "Réponse sous 48 heures ouvrées",
                "text":
                    "Le client écrit au concierge en décrivant le profil de la demeure "
                    "souhaitée — territoire, provenance, surface, saison d'usage. Le "
                    "conseiller du territoire répond sous deux jours ouvrés avec un premier "
                    "résumé de la collection compatible et une proposition de première rencontre.",
            },
            {
                "n":        "02",
                "title":    "Accord de confidentialité",
                "duration": "Signé au bureau ou à distance",
                "text":
                    "Avant la remise des dossiers complets, client et cabinet signent un "
                    "accord de confidentialité réciproque qui engage les deux parties à une "
                    "discrétion absolue sur les propriétés, les familles vendeuses et les "
                    "conditions économiques. Cet accord est standard et n'empêche pas "
                    "l'assistance d'un second conseil fiscal.",
            },
            {
                "n":        "03",
                "title":    "Visioconférence éditoriale",
                "duration": "Une demi-journée · avec le conseiller",
                "text":
                    "Une première rencontre en visioconférence — ou dans nos bureaux si le "
                    "client le souhaite — au cours de laquelle nous parcourons ensemble trois "
                    "ou quatre dossiers éditoriaux, avec plans, histoire de la demeure, "
                    "images actualisées, rapport paysager. Le client choisit les deux "
                    "demeures pour la visite en présence.",
            },
            {
                "n":        "04",
                "title":    "Visite privée en présence",
                "duration": "Un à deux jours sur le territoire",
                "text":
                    "Nous accompagnons personnellement le client sur la propriété, en "
                    "présence de l'interlocuteur résident et, si la famille vendeuse le "
                    "souhaite, de cette dernière. La visite se tient sans pression "
                    "commerciale : elle dure le temps nécessaire, inclut un déjeuner à "
                    "proximité immédiate, et peut être répétée une seconde fois dans une "
                    "saison différente.",
            },
            {
                "n":        "05",
                "title":    "Négociation et signature",
                "duration": "De 45 jours à 6 mois",
                "text":
                    "Le cabinet rédige la proposition d'acquisition en accord avec le client "
                    "et la présente directement à la famille vendeuse. Les partenaires "
                    "notariaux préparent le compromis et l'acte authentique. Le conseiller "
                    "accompagne personnellement le client à la signature et demeure à sa "
                    "disposition pour les six mois suivants, pour toute formalité postérieure "
                    "à la remise des clefs.",
            },
        ],

        # Testimonial slot (single, editorial, discreet)
        "testimonial_label":   "Référence",
        "testimonial_text":
            "« Le cabinet m'avait été recommandé par un ancien associé à Londres. J'ai "
            "sollicité un premier entretien à Milan et en six mois nous avons acquis une "
            "villa en Costa Smeralda pour notre famille, sans que la négociation ne sorte "
            "jamais du cercle des trois personnes concernées. L'interlocutrice est restée "
            "la même — elle connaît aujourd'hui également mes enfants. »",
        "testimonial_author":  "Un family office lombard · acquisition 2024 · Porto Cervo",

        # FAQ accordion
        "faq_label":   "Questions récurrentes",
        "faq_items": [
            {
                "q": "Quelle est la durée moyenne du parcours jusqu'à la signature ?",
                "a": "De quatre à douze mois, selon la complexité de la propriété. Les demeures "
                     "prêtes à l'acte se closent en quarante-cinq jours ; les demeures "
                     "historiques soumises à protection paysagère ou nécessitant un "
                     "redécoupage cadastral demandent des délais plus longs pour les "
                     "vérifications auprès des services du patrimoine.",
            },
            {
                "q": "Quelles sont les langues de travail du cabinet ?",
                "a": "Italien, anglais et français dans chaque négociation. Allemand pour le "
                     "territoire du Lago di Como, arabe et chinois à un niveau de base pour la "
                     "clientèle du Moyen-Orient et d'Asie. Les traductions assermentées de "
                     "tous les documents notariés sont comprises dans le mandat.",
            },
            {
                "q": "Comment sont calculés les honoraires du cabinet ?",
                "a": "Toujours en pourcentage du prix d'acquisition final, précisé avec "
                     "transparence dans le mandat initial. Aucun forfait n'est dû pendant les "
                     "phases d'étude — uniquement à la signature notariale effective.",
            },
            {
                "q": "Le cabinet représente-t-il également les vendeurs ?",
                "a": "Oui, mais jamais simultanément sur la même demeure. Chaque mandat est "
                     "exclusif à l'une des deux parties, afin de garantir une transparence "
                     "totale dans la négociation. Le client sait toujours pour quelle partie "
                     "nous travaillons.",
            },
            {
                "q": "Peut-on visiter une demeure plus d'une fois ?",
                "a": "Oui, à la demande. Nous accompagnons gracieusement le client pour une "
                     "seconde visite en saison différente — beaucoup de propriétés côtières "
                     "se visitent une fois en été et une fois en hiver avant décision.",
            },
            {
                "q": "Comment protégez-vous la confidentialité de la négociation ?",
                "a": "Chaque négociation s'ouvre par un accord de confidentialité réciproque, "
                     "signé au bureau ou à distance, qui engage le cabinet, le client et la "
                     "famille vendeuse. Aucun dossier n'est accessible en format numérique "
                     "ouvert — tous les documents sont remis sur plateforme confidentielle "
                     "ou en format imprimé.",
            },
        ],

        # Closing CTA
        "cta_label":      "Premier entretien",
        "cta_heading":    "Un <em>premier entretien</em> est toujours gracieux et confidentiel.",
        "cta_text":
            "Aucun mandat n'est dû après la première rencontre. Le client reçoit un premier "
            "résumé de la collection compatible, une proposition de conseiller dédié et une "
            "date indicative pour la première visite privée. Si le profil n'est pas "
            "compatible, nous remercions et prenons congé — sans suite.",
        "cta_primary":      "Demander le premier entretien",
        "cta_primary_href": "concierge",
    },

    # ─── CONCIERGE (contact) — private-viewing request ───────
    "concierge": {
        "eyebrow":  "Concierge privé · sur rendez-vous",
        "headline": "Sur <em>rendez-vous</em> uniquement.",
        "intro":
            "Nous recevons exclusivement sur rendez-vous, dans les bureaux de Milan et "
            "Portofino ainsi qu'au bureau concierge de Saint-Tropez. Le concierge lit "
            "personnellement chaque demande et répond sous le jour ouvré suivant. Pour les "
            "demandes en arabe, en chinois ou en allemand, la réponse est signée directement "
            "par le conseiller dédié au territoire concerné.",

        # Dedicated phone line by territorio
        "phone_label":    "Ligne concierge par territoire",
        "phone_intro":
            "Chaque territoire dispose d'une ligne dédiée, ouverte uniquement aux clients "
            "sous accord de confidentialité ou présentés par un référent. Pour un premier "
            "contact, il est toujours préférable d'écrire au concierge par courriel — la "
            "réponse est plus rapide et mieux documentée.",
        "phone_rows": [
            ("Milan · direction",              "concierge@villaprestige.it"),
            ("Portofino · bureau concierge",   "portofino@villaprestige.it"),
            ("Saint-Tropez · bureau concierge","saint-tropez@villaprestige.it"),
            ("Clients asiatiques · Omar Khoury","asia@villaprestige.it"),
        ],

        # Form section (private-viewing request with NDA consent)
        "form_section_label":  "Demande de visite privée",
        "form_section_intro":
            "Merci de renseigner les champs nécessaires. Le concierge répondra sous le jour "
            "ouvré suivant, en italien, anglais ou français. Pour toute demande dans une "
            "autre langue, veuillez l'indiquer dans le champ notes.",

        "form_helper_required":  "Les champs indiqués sont obligatoires",
        "form_submit_button":    "Envoyer la demande confidentielle",
        "form_submit_note":
            "Votre demande est lue personnellement par le concierge de la direction. "
            "Aucune infolettre, aucune communication commerciale. Les données sont "
            "supprimées sous quatre-vingt-dix jours si le profil ne se révèle pas "
            "compatible avec la collection.",

        "form_fields": [
            {"name":"titolo",    "label":"Titre", "type":"select", "required":True,
             "options":["Mme","M.","Cabinet · family office","Presse · éditorial"]},
            {"name":"nome",      "label":"Nom et prénom", "type":"text",
             "placeholder":"Ex. Mme Eleonora Visconti", "required":True},
            {"name":"email",     "label":"Courriel confidentiel", "type":"email",
             "placeholder":"e.visconti@exemple.fr", "required":True},
            {"name":"telefono",  "label":"Téléphone (facultatif)", "type":"tel",
             "placeholder":"+33 …", "required":False},
            {"name":"sede",      "label":"Bureau préféré", "type":"select", "required":True,
             "options":["Milan · Montenapoleone","Portofino · concierge","Saint-Tropez · concierge","Visioconférence préliminaire","Sans préférence"]},
            {"name":"territorio","label":"Territoire d'intérêt", "type":"select", "required":True,
             "options":["Portofino · Ligurie","Chianti Classico · Toscane","Costa Smeralda · Sardaigne","Lago di Como · Lombardie","Saint-Tropez · Côte d'Azur","Capri · Campanie","Val d'Orcia · Toscane","Deux territoires ou plus"]},
            {"name":"profilo",   "label":"Profil de la demeure", "type":"select", "required":True,
             "options":["Demeure historique avec parc","Dernier étage ou penthouse urbain","Villa contemporaine d'auteur","Domaine agricole avec vigne","Propriété côtière","Pas de profil préétabli"]},
            {"name":"date",      "label":"Dates souhaitées", "type":"text",
             "placeholder":"Ex. deuxième semaine de mai · ou entrée de saison", "required":False},
            {"name":"note",      "label":"Notes au concierge", "type":"textarea",
             "placeholder":"Indiquer les préférences de langue, le référent qui vous présente, les disponibilités familiales.", "required":True, "rows":5},
            {"name":"nda",       "label":"Je consens à la signature d'un accord de confidentialité réciproque avant la remise des dossiers éditoriaux", "type":"checkbox", "required":True},
        ],

        # Office cards — three concierge offices
        "offices_label":   "Les bureaux",
        "offices_heading": "Trois bureaux, <em>trois salons réservés.</em>",
        "offices_intro":
            "Chaque bureau ne reçoit que sur rendez-vous, dans un salon réservé doté d'une "
            "archive éditoriale locale. Le bureau de Milan est la direction générale ; "
            "Portofino et Saint-Tropez sont tenus en saison par les interlocuteurs résidents.",
        "offices": [
            {
                "city":    "Milan",
                "address": "Via Montenapoleone 17 · 20121 Milan",
                "hours":   "Lun – Ven · 10:00 – 19:00 · sur rendez-vous uniquement",
                "email":   "concierge@villaprestige.it",
                "role":    "Direction · archive centrale · rencontres au bureau",
            },
            {
                "city":    "Portofino",
                "address": "Via Roma 28 · 16034 Portofino GE",
                "hours":   "Avr – Oct · visites sur rendez-vous · novembre – mars sur demande",
                "email":   "portofino@villaprestige.it",
                "role":    "Bureau concierge · interlocuteur résident · Ligurie",
            },
            {
                "city":    "Saint-Tropez",
                "address": "Place de la Garonne 6 · 83990 Saint-Tropez",
                "hours":   "Mai – Sep · visites sur rendez-vous · octobre – avril sur demande",
                "email":   "saint-tropez@villaprestige.it",
                "role":    "Bureau concierge · interlocuteur résident · Côte d'Azur",
            },
        ],

        # Press contact ribbon
        "press_contact_label":   "Contacts presse",
        "press_contact_text":
            "Pour toute demande éditoriale et presse spécialisée, veuillez écrire directement "
            "à la direction : stampa@villaprestige.it. Communiqués de presse, portfolios "
            "photographiques et entretiens sont coordonnés personnellement par la directrice. "
            "Nous répondons à la presse internationale sous un jour ouvré, en italien, "
            "anglais ou français.",
        "press_contact_email":   "stampa@villaprestige.it",
    },

    # ─── BLOG POSTS (used by collezione blog_list + blog_detail) ──
    # These render the signature properties as editorial dossiers.
    "posts": [
        {
            "slug":     "villa-aurelia-portofino",
            "kicker":   "Portofino · Ligurie · années 1920",
            "title":    "Villa Aurelia — demeure historique de 1922 sur le promontoire",
            "lede":
                "Quatre cents mètres carrés dominant le golfe du Tigullio, parc de trois hectares, "
                "bibliothèque signée et piscine à débordement suspendue au-dessus de l'île Palmaria.",
            "date":     "12 avril 2026",
            "read_min": "7",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 03 / 18 · printemps 2026"),
                ("Territoire",  "Portofino · Ligurie · golfe du Tigullio"),
                ("Surface",     "400 m² intérieurs · parc 30 000 m² · 7 chambres"),
                ("Provenance",  "1922 · signature Marcello Piacentini · restauration A. Citterio 2014"),
                ("Disponibilité","Trois jours par mois · sur rendez-vous"),
                ("Prix",        "Sur demande à l'interlocuteur"),
            ],
            "body": [
                ("p",
                 "La demeure ouvre son portail carrossable sur une montée ombragée de chênes verts "
                 "centenaires et ne se révèle qu'au bout de trois cents mètres, dominant le golfe "
                 "du Tigullio à soixante mètres de hauteur. Le plan est en fer à cheval, avec un "
                 "corps central de 1922 et deux ailes ajoutées en 1938 par la même main de "
                 "Marcello Piacentini. L'intervention de 2014 — dirigée par Antonio Citterio avec "
                 "le paysagiste Paolo Pejrone pour le parc — a préservé toutes les fresques "
                 "originelles du salon central, restitué les menuiseries en bois massif et "
                 "introduit la piscine à débordement aujourd'hui inscrite parmi les images "
                 "iconiques du promontoire."),
                ("h2", "Le parc · trois hectares de chênes verts, oliviers et camélias"),
                ("p",
                 "Le parc, dessiné à l'origine par le comte Ricci en 1924 et revu par Paolo "
                 "Pejrone en 2014, alterne chênes verts centenaires, oliveraies en production et "
                 "une collection de trente-deux variétés de camélias. La demeure dispose d'un "
                 "escalier privé qui descend directement à la mer, avec mouillage pour bateaux "
                 "jusqu'à huit mètres. Le jardin est entièrement autonome en arrosage grâce à "
                 "une citerne de récupération des eaux pluviales restaurée en 2018."),
                ("h2", "Intérieurs · bibliothèque signée et salon de réception"),
                ("p",
                 "Au piano nobile s'articulent le salon central de 140 mètres carrés, avec "
                 "fresques originelles de l'école ligurienne, une salle à manger face à la mer "
                 "et la bibliothèque signée, aux boiseries de noyer dessinées en 1938. Au "
                 "premier étage, la suite principale occupe toute l'aile est, avec salle de bain "
                 "privée en marbre de Carrare et terrasse face à l'île Palmaria. Six autres "
                 "chambres se distribuent entre le premier et le deuxième étage, chacune avec "
                 "salle de bain dédiée."),
                ("blockquote",
                 "« La villa de Portofino n'est pas une propriété : c'est un geste de réserve "
                 "qui se transmet entre familles qui se font confiance. Notre rôle est "
                 "seulement de veiller au passage. »"),
                ("h2", "Provenance · la main de Piacentini, la restauration de Citterio"),
                ("p",
                 "Commandée en 1921 par la famille génoise Acquarone à l'architecte Marcello "
                 "Piacentini — déjà auteur alors de nombreuses interventions sur le front de mer "
                 "de Viareggio — la Villa Aurelia fut achevée en 1922 et demeura dans la même "
                 "famille pendant trois générations. Elle passe en 2007 à une seconde famille "
                 "milanaise, qui confie en 2014 à Antonio Citterio la restauration conservatrice, "
                 "avec Paolo Pejrone pour le parc. L'intervention a été publiée dans AD Italia, "
                 "Elle Decor et Corriere Living."),
                ("ol", [
                    "Accès : voie privée avec portail carrossable, supervision paysagère du service du patrimoine de Gênes.",
                    "Parc : trois hectares · escalier privé à la mer · mouillage pour bateaux jusqu'à huit mètres.",
                    "Surface intérieure : quatre cents mètres carrés · sept chambres · salles de bain en marbre de Carrare.",
                    "Équipements : chauffage géothermique · panneaux photovoltaïques à faible impact visuel · citerne eaux pluviales.",
                    "Prix : sur demande à l'interlocuteur · accord de confidentialité requis avant le dossier complet.",
                ]),
                ("p",
                 "La disponibilité se limite à trois jours par mois pour les visites privées, "
                 "en présence de la famille propriétaire. La conseillère du territoire — "
                 "Arianna Testa Piccolomini, résidente à Portofino depuis dix ans — accompagne "
                 "personnellement le client de la première visioconférence à la signature notariale."),
            ],
            "footer_strap": "Villa Prestige · Portofino · dossier N° 03 / 18",
        },
        {
            "slug":     "castello-di-montero-chianti",
            "kicker":   "Chianti Classico · Toscane · XIIe siècle",
            "title":    "Castello di Monterò — forteresse médiévale avec vigne de production",
            "lede":
                "Mille deux cents mètres carrés sur dix-huit hectares, vigne de Chianti Classico "
                "en conduite biodynamique, cave en sous-sol, chapelle consacrée de 1432.",
            "date":     "5 avril 2026",
            "read_min": "9",
            "author":   "Francesco Medici di Porrena",
            "image":
                "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 07 / 18 · printemps 2026"),
                ("Territoire",  "Chianti Classico · Toscane · Gaiole in Chianti"),
                ("Surface",     "1 200 m² intérieurs · 18 hectares · 7 hectares de vigne"),
                ("Provenance",  "XIIe siècle · restauration conservatrice Tobia Scarpa 2014"),
                ("Disponibilité","Exclusive · un seul mandat actif"),
                ("Prix",        "Sur demande à l'interlocuteur"),
            ],
            "body": [
                ("p",
                 "Le château s'élève sur une crête à 520 mètres d'altitude, entre Gaiole in "
                 "Chianti et Radda, dominant au sud la vallée de l'Arbia et au nord les collines "
                 "de San Polo. Le corps central, avec sa tour de guet de 1185, est demeuré "
                 "substantiellement intact depuis sa construction originelle ; la restauration "
                 "de 2014, conduite par Tobia Scarpa sous la supervision du service du "
                 "patrimoine de Florence, a rendu habitables les mille deux cents mètres carrés "
                 "intérieurs sans altérer une pierre de l'enveloppe médiévale."),
                ("h2", "Le domaine · dix-huit hectares, vigne en conduite biodynamique"),
                ("p",
                 "La propriété s'étend sur dix-huit hectares dont sept consacrés à la vigne de "
                 "Chianti Classico DOCG, en conduite biodynamique certifiée depuis 2016. La "
                 "production annuelle est d'environ quinze mille bouteilles, distribuées "
                 "exclusivement sur allocation privée — jamais sur le marché. La cave en "
                 "sous-sol, creusée sous le corps central, abrite trente barriques et une "
                 "collection historique de deux mille bouteilles."),
                ("h2", "Le corps central · salle d'armes et chapelle de 1432"),
                ("p",
                 "Au rez-de-chaussée s'articulent la salle d'armes de 180 mètres carrés, la "
                 "chapelle privée consacrée en 1432 (encore en usage annuel le 24 juin, jour "
                 "du saint patron), la cuisine historique avec son four à bois d'origine. Le "
                 "premier étage abrite la bibliothèque familiale aux trois mille volumes, cinq "
                 "chambres de maître, deux salons. Au deuxième étage, la tour de guet a été "
                 "transformée en studio privé avec une vue à trois cent soixante degrés sur la "
                 "vallée."),
                ("blockquote",
                 "« Le château n'est pas à vendre parce que la famille a besoin d'argent. Il "
                 "est à vendre parce que la génération suivante vit entre Londres et Shanghai, "
                 "et nous éprouvons le besoin de le confier à qui saura le porter. »"),
                ("h2", "Provenance · sept siècles, deux familles"),
                ("p",
                 "Documenté depuis 1185 dans les actes notariés siennois, le château fut "
                 "durant quatre cents ans l'apanage de la famille Ricasoli, puis des "
                 "Pannocchieschi à partir de 1570, enfin de l'actuelle famille Medici di "
                 "Porrena depuis 1812. La décision de confier le mandat à Villa Prestige "
                 "procède de la relation personnelle de trente ans entre la famille et le "
                 "conseiller senior Francesco Medici di Porrena — cousin de la même famille et "
                 "conseiller du cabinet pour le Chianti Classico."),
                ("ol", [
                    "Accès : voie blanche privée d'un kilomètre, protection paysagère UNESCO en cours d'évaluation.",
                    "Parc et vigne : dix-huit hectares · sept en Chianti Classico biodynamique · oliveraie de deux mille arbres centenaires.",
                    "Surface intérieure : mille deux cents mètres carrés · dix chambres · chapelle consacrée 1432.",
                    "Cave : en sous-sol sous le corps central · trente barriques · collection historique deux mille bouteilles.",
                    "Équipements : chauffage à biomasse · panneaux photovoltaïques à faible impact · eau de source privée.",
                    "Prix : sur demande à l'interlocuteur · exclusive totale jusqu'à l'automne 2026.",
                ]),
                ("p",
                 "La disponibilité se limite à un seul jour par mois pour les visites privées, "
                 "directement avec la famille et le conseiller. Le parcours d'acquisition "
                 "demande au moins six mois pour les vérifications auprès du service du "
                 "patrimoine de Florence et de la Région Toscane. Le transfert du mandat "
                 "agricole de la vigne est coordonné avec le consortium du Chianti Classico."),
            ],
            "footer_strap": "Villa Prestige · Chianti Classico · dossier N° 07 / 18",
        },
        {
            "slug":     "penthouse-quadronno-milano",
            "kicker":   "Milan · Magenta · dernier étage unique",
            "title":    "Penthouse Quadronno — dernier étage de 1957 avec vue sur le Duomo",
            "lede":
                "Trois cent quatre-vingts mètres carrés au sixième étage de la via Quadronno, "
                "terrasse de 180 m², vue frontale sur le Duomo, intérieurs signés Vico Magistretti "
                "en 1958.",
            "date":     "28 mars 2026",
            "read_min": "6",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 11 / 18 · printemps 2026"),
                ("Territoire",  "Milan · Magenta · via Quadronno"),
                ("Surface",     "380 m² intérieurs · terrasse 180 m² · 4 chambres"),
                ("Provenance",  "1957 · signature Luigi Caccia Dominioni · intérieurs Vico Magistretti 1958"),
                ("Disponibilité","Sur rendez-vous"),
                ("Prix",        "Sur demande à l'interlocuteur"),
            ],
            "body": [
                ("p",
                 "Le dernier étage occupe l'ensemble du sixième niveau du palais Quadronno, "
                 "édifié en 1957 sur un projet de Luigi Caccia Dominioni pour une commande "
                 "privée de la bourgeoisie industrielle milanaise. Les intérieurs furent "
                 "achevés dix mois plus tard par Vico Magistretti, alors âgé de trente-trois "
                 "ans, dans un travail d'un artisanat méticuleux sur les bois, les marbres et "
                 "les poignées, demeuré aujourd'hui encore intact dans son intégrité originelle."),
                ("h2", "Le plan · trois cent quatre-vingts mètres carrés articulés"),
                ("p",
                 "L'entrée s'ouvre sur une galerie longue de dix-huit mètres qui distribue les "
                 "deux ailes de l'appartement — zone jour au sud-est, zone nuit au nord-ouest. "
                 "Le salon principal de cent dix mètres carrés fait face au Duomo à travers "
                 "une verrière de Jacopo Foggini installée en 2018. La salle à manger, la "
                 "cuisine professionnelle et l'office complètent l'aile de jour. Quatre "
                 "chambres, chacune avec salle de bain privée en marbre de Carrare originel de "
                 "1957, composent l'aile de nuit."),
                ("h2", "La terrasse · cent quatre-vingts mètres carrés en ceinture"),
                ("p",
                 "La terrasse périmétrale, cent quatre-vingts mètres carrés au total, offre une "
                 "vue à trois cent soixante degrés sur la ville : Duomo à l'est, Castello "
                 "Sforzesco au nord, San Siro à l'horizon occidental. L'intervention paysagère "
                 "de Patricia Urquiola en 2019 a ajouté une vasque balnéo couverte, une "
                 "pergola en terre cuite et une collection de quinze variétés d'aromatiques "
                 "méditerranéennes."),
                ("blockquote",
                 "« Le Quadronno n'est pas un dernier étage : c'est un petit musée de la "
                 "maison milanaise des années Cinquante. Chaque détail de Magistretti est à "
                 "sa place. »"),
                ("h2", "Provenance · Caccia Dominioni, Magistretti, Urquiola"),
                ("p",
                 "Commandé en 1956 par la famille Brambilla à Luigi Caccia Dominioni, achevé "
                 "en 1957. Les intérieurs de Vico Magistretti furent livrés en 1958 et n'ont "
                 "subi aucune altération significative pendant soixante ans. En 2018, la "
                 "seconde famille propriétaire a confié à Jacopo Foggini la verrière frontale ; "
                 "en 2019, l'intervention paysagère sur la terrasse a été signée par Patricia "
                 "Urquiola. L'ensemble des interventions a été documenté dans Domus, Interni "
                 "et Corriere Living."),
                ("ol", [
                    "Accès : conciergerie d'un immeuble de grand prestige · ascenseur de service dédié.",
                    "Surface intérieure : trois cent quatre-vingts mètres carrés · quatre chambres · salles de bain en marbre originel 1957.",
                    "Terrasse : cent quatre-vingts mètres carrés · vasque balnéo couverte · pergola en terre cuite Urquiola 2019.",
                    "Vue : frontale sur le Duomo de Milan · panorama à trois cent soixante degrés.",
                    "Équipements : chauffage autonome · climatisation à contrôle indépendant aile par aile.",
                    "Prix : sur demande à l'interlocuteur · accord de confidentialité requis avant le dossier complet.",
                ]),
                ("p",
                 "La disponibilité est ouverte sur rendez-vous. Le parcours d'acquisition "
                 "moyen est de quarante-cinq jours, de l'accord de confidentialité à la "
                 "signature, grâce à la documentation cadastrale complète et déjà actualisée. "
                 "La famille vendeuse est disponible pour une rencontre directe avant la "
                 "signature."),
            ],
            "footer_strap": "Villa Prestige · Milan · dossier N° 11 / 18",
        },
        {
            "slug":     "mas-de-la-mer-saint-tropez",
            "kicker":   "Saint-Tropez · Côte d'Azur · XVIIIe siècle",
            "title":    "Mas de la Mer — mas provençal de 1754 avec vigne AOP",
            "lede":
                "Cinq cent cinquante mètres carrés sur les collines de Ramatuelle, vigne privée "
                "en Côtes de Provence AOP, construction originelle de 1754 restaurée en 2017.",
            "date":     "20 mars 2026",
            "read_min": "8",
            "author":   "Élodie Charbonneau",
            "image":
                "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 14 / 18 · printemps 2026"),
                ("Territoire",  "Saint-Tropez · Côte d'Azur · Ramatuelle"),
                ("Surface",     "550 m² intérieurs · 6 hectares · vigne 2,5 ha"),
                ("Provenance",  "1754 · mas provençal originel · restauration François Catroux 2017"),
                ("Disponibilité","Nouveauté · tout juste entrée en collection"),
                ("Prix",        "Sur demande à l'interlocuteur"),
            ],
            "body": [
                ("p",
                 "Le mas s'élève sur les collines intérieures de Ramatuelle, à douze "
                 "kilomètres du port de Saint-Tropez, dans un silence que seul le Var "
                 "intérieur sait offrir. La construction originelle est de 1754, appartenant à "
                 "la même famille de tradition viticole jusqu'en 1948. Acquis en 1985 par une "
                 "famille parisienne, il a été restauré en 2017 par François Catroux — dernier "
                 "chantier privé de l'architecte français avant sa disparition — avec pour "
                 "objectif de rendre aux intérieurs leur simplicité originelle, après "
                 "cinquante ans d'interventions disparates."),
                ("h2", "La vigne · deux hectares et demi de Côtes de Provence AOP"),
                ("p",
                 "La propriété comprend deux hectares et demi de vigne en production AOP "
                 "Côtes de Provence, avec vinification confiée au Domaine Ott pour la part "
                 "rosé et au Domaine Tempier pour la part rouge. La production annuelle est "
                 "d'environ sept mille bouteilles, distribuées exclusivement à la famille "
                 "propriétaire et à ses hôtes. La cave de transformation se trouve "
                 "directement sous le mas, dans un local semi-enterré de 1802."),
                ("h2", "Intérieurs · salon à double volume et chambre principale"),
                ("p",
                 "Le rez-de-chaussée s'articule autour d'un salon à double volume de cent "
                 "vingt mètres carrés, avec cheminée d'angle en pierre originelle et "
                 "charpente en chêne apparente. La cuisine est voûtée, pavée en tomettes de "
                 "Salernes. Au premier étage, la chambre principale occupe toute l'aile sud "
                 "avec salle de bain privée en marbre de Caunes-Minervois ; trois autres "
                 "chambres doubles, chacune avec salle de bain dédiée, complètent l'étage. "
                 "La dépendance du gardien abrite un appartement pour gardien ou hôtes."),
                ("blockquote",
                 "« François Catroux a rendu au mas la lenteur que le Var intérieur connaît "
                 "depuis toujours. C'est son dernier chantier privé, et cela se sent. »"),
                ("h2", "Provenance · de la viticulture à la famille parisienne"),
                ("p",
                 "Construit en 1754 par la famille Bertrand, qui le posséda sur six "
                 "générations en cultivant la vigne et en produisant de l'huile d'olive, le "
                 "mas passa à la famille parisienne Armand en 1948. Restauré une première "
                 "fois en 1985 par Madeleine Castaing dans un style riche et orné, il a été "
                 "rendu à sa sobriété originelle en 2017 par la restauration de François "
                 "Catroux. Le chantier a été publié dans Architectural Digest France et dans "
                 "Le Monde d'Hermès."),
                ("ol", [
                    "Accès : voie blanche privée de deux cents mètres · portail en fer originel 1754.",
                    "Parc : six hectares · vigne AOP deux et demi · oliveraie séculaire · bassin naturel en pierre.",
                    "Surface intérieure : cinq cent cinquante mètres carrés · quatre chambres · dépendance du gardien.",
                    "Vigne : Côtes de Provence AOP · vinification Domaine Ott et Tempier · production sept mille bouteilles.",
                    "Équipements : chauffage à pellets · climatisation douce · eau de source privée.",
                    "Prix : sur demande à l'interlocuteur · accord de confidentialité requis avant le dossier complet.",
                ]),
                ("p",
                 "La disponibilité est ouverte sur rendez-vous à partir de la prochaine "
                 "saison de visites — mi-mai. Le mandat agricole pour la vigne est cédé "
                 "conjointement à la signature immobilière ; le transfert ultérieur de la "
                 "dénomination AOP se coordonne avec le Domaine Ott. Le parcours d'acquisition "
                 "moyen est de quatre mois, de l'accord de confidentialité à la signature "
                 "notariale française."),
            ],
            "footer_strap": "Villa Prestige · Saint-Tropez · dossier N° 14 / 18",
        },
        # Four shorter dossiers to round out the collezione list
        {
            "slug":     "villa-lario-tremezzo",
            "kicker":   "Lago di Como · Tremezzo · XIXe siècle",
            "title":    "Villa Lario — demeure lacustre de 1862 avec darse privée",
            "lede":
                "Quatre cent cinquante mètres carrés au niveau du Lac, parc de deux hectares et "
                "demi, darse privée pour embarcations jusqu'à quinze mètres.",
            "date":     "15 mars 2026",
            "read_min": "5",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 04 / 18 · printemps 2026"),
                ("Territoire",  "Lago di Como · Tremezzo"),
                ("Surface",     "450 m² intérieurs · parc 25 000 m² · darse privée"),
                ("Provenance",  "1862 · villa du XIXe siècle · restauration Lissoni 2020"),
                ("Disponibilité","Sur rendez-vous"),
                ("Prix",        "Sur demande à l'interlocuteur"),
            ],
            "body": [
                ("p",
                 "Villa Lario s'élève au niveau du Lago di Como, à cinq minutes de la piazzetta "
                 "de Tremezzo et à dix minutes en hors-bord de la Villa d'Este. La construction "
                 "originelle est de 1862, pour une famille milanaise de la bourgeoisie "
                 "industrielle lombarde. La restauration conservatrice de 2020, conduite par "
                 "le studio Lissoni Casal Ribeiro, a préservé intacts les décors du XIXe "
                 "siècle du salon principal, les boiseries originelles et l'escalier intérieur "
                 "en marbre de Candoglia."),
                ("h2", "Le parc et la darse · accès privé au Lac"),
                ("p",
                 "Le parc s'étend sur deux hectares et demi en pente vers le Lac, avec un "
                 "jardin à l'italienne originel de 1875, un vivier, un portique de jasmins "
                 "centenaires. La darse privée, originelle de 1870 et restaurée en 2020, "
                 "abrite des embarcations jusqu'à quinze mètres de longueur et est équipée "
                 "d'une grue électrique pour la mise à sec hivernale. Un escalier de pierre "
                 "descend directement du salon principal au belvédère sur le Lac."),
                ("ol", [
                    "Accès : route nationale · portail privé avec conciergerie.",
                    "Parc : deux hectares et demi · jardin à l'italienne · darse privée.",
                    "Surface intérieure : quatre cent cinquante mètres carrés · cinq chambres · bibliothèque.",
                    "Prix : sur demande à l'interlocuteur · accord de confidentialité requis avant le dossier.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Lago di Como · dossier N° 04 / 18",
        },
        {
            "slug":     "casa-delle-torri-porto-cervo",
            "kicker":   "Costa Smeralda · Porto Cervo · années 1970",
            "title":    "Casa delle Torri — villa de Jacques Couëlle de 1972",
            "lede":
                "Six cent vingt mètres carrés sur promontoire privé, dessin original de Jacques "
                "Couëlle, terrasses en surplomb de la mer et accès direct à une crique privée.",
            "date":     "8 mars 2026",
            "read_min": "6",
            "author":   "Élodie Charbonneau",
            "image":
                "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 08 / 18 · printemps 2026"),
                ("Territoire",  "Costa Smeralda · Porto Cervo"),
                ("Surface",     "620 m² intérieurs · promontoire privé · crique"),
                ("Provenance",  "1972 · signature Jacques Couëlle · restauration A. Citterio 2018"),
                ("Disponibilité","Sur rendez-vous"),
                ("Prix",        "Sur demande à l'interlocuteur"),
            ],
            "body": [
                ("p",
                 "Dessinée en 1972 par Jacques Couëlle pour une famille belge, la Casa delle "
                 "Torri est l'une des rares villas entièrement préservées du dessin organique "
                 "smaragdin. La restauration de 2018 conduite par Antonio Citterio a maintenu "
                 "l'intégrité absolue du manteau en granit local et des toitures en genévrier, "
                 "en y introduisant des équipements invisibles et une cuisine contemporaine "
                 "dans la dépendance."),
                ("ol", [
                    "Accès : voie privée du consortium · conciergerie de Porto Cervo.",
                    "Terrasses : trois niveaux en surplomb de la mer · crique privée accessible à pied.",
                    "Surface : six cent vingt mètres carrés · six chambres · dépendance du personnel.",
                    "Prix : sur demande à l'interlocuteur.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Costa Smeralda · dossier N° 08 / 18",
        },
        {
            "slug":     "casa-canapa-capri",
            "kicker":   "Capri · Anacapri · années 1930",
            "title":    "Casa Canapa — villa caprese face aux Faraglioni",
            "lede":
                "Deux cent vingt mètres carrés sur trois niveaux, terrasses superposées face aux "
                "Faraglioni, jardin de citronniers centenaires, accès piéton depuis le centre "
                "d'Anacapri.",
            "date":     "1er mars 2026",
            "read_min": "5",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 15 / 18 · printemps 2026"),
                ("Territoire",  "Capri · Anacapri"),
                ("Surface",     "220 m² intérieurs · 3 terrasses · jardin 800 m²"),
                ("Provenance",  "1934 · villa caprese originelle · trois générations même famille"),
                ("Disponibilité","Sur rendez-vous"),
                ("Prix",        "Sur demande à l'interlocuteur"),
            ],
            "body": [
                ("p",
                 "La Casa Canapa est une villa caprese authentique de 1934, transmise sur "
                 "trois générations dans la même famille napolitaine. Le dessin d'origine est "
                 "de tradition caprese — voûtes, voûtains, escaliers extérieurs en majolique — "
                 "et n'a subi aucune intervention de substance. L'entretien courant, confié "
                 "aux artisans caprese de toujours, a préservé intact le caractère insulaire "
                 "de la demeure."),
                ("ol", [
                    "Accès : piéton uniquement · cinq minutes à pied de la piazzetta d'Anacapri.",
                    "Terrasses : trois niveaux superposés · vue sur les Faraglioni de Capri.",
                    "Surface : deux cent vingt mètres carrés · quatre chambres.",
                    "Prix : sur demande à l'interlocuteur.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Capri · dossier N° 15 / 18",
        },
        {
            "slug":     "pieve-di-santorso-val-dorcia",
            "kicker":   "Val d'Orcia · Montalcino · XIIe siècle",
            "title":    "Pieve di Sant'Orso — domaine UNESCO avec vigne de Brunello",
            "lede":
                "Huit cents mètres carrés entre pieve romane et maison rurale, vingt-deux hectares "
                "patrimoine UNESCO, vigne de Brunello di Montalcino DOCG en production.",
            "date":     "22 février 2026",
            "read_min": "7",
            "author":   "Francesco Medici di Porrena",
            "image":
                "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 17 / 18 · printemps 2026"),
                ("Territoire",  "Val d'Orcia · Montalcino"),
                ("Surface",     "800 m² intérieurs · 22 ha UNESCO · vigne 4 ha"),
                ("Provenance",  "XIIe siècle · pieve romane · restauration Matteo Nunziati 2019"),
                ("Disponibilité","Exclusive"),
                ("Prix",        "Sur demande à l'interlocuteur"),
            ],
            "body": [
                ("p",
                 "Le domaine de Sant'Orso s'étend sur vingt-deux hectares de patrimoine UNESCO "
                 "en Val d'Orcia, entre Montalcino et San Quirico d'Orcia. Le noyau historique "
                 "comprend la pieve romane de 1182 — encore consacrée, en usage une fois l'an "
                 "— et la maison rurale originelle de 1620, restaurée en 2019 par Matteo "
                 "Nunziati. La vigne de Brunello di Montalcino DOCG occupe quatre hectares, "
                 "en conduite biologique certifiée, avec vinification confiée au domaine voisin."),
                ("ol", [
                    "Accès : voie communale blanche de deux kilomètres · protection UNESCO.",
                    "Domaine : vingt-deux hectares · vigne quatre hectares · oliveraie de huit cents arbres.",
                    "Surface intérieure : huit cents mètres carrés · pieve romane · six chambres.",
                    "Prix : sur demande à l'interlocuteur · exclusive totale.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Val d'Orcia · dossier N° 17 / 18",
        },
    ],
}


# D-047 · all chrome labels flow from site/page_data above — no string
# should ever be hardcoded in the skin or preview composition HTML.
