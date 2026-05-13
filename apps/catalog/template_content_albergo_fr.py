"""Albergo Borgo — Hospitalité Relais dans un village toscan UNESCO (FR).

T57 · Wave 2 Pass-2 (2026-05-12) · traduction française du contenu IT.
Translation française fidèle de `template_content_albergo.py` (IT).
Parité de forme stricte avec ALBERGO_CONTENT_IT — 225 chemins-feuilles,
zéro manquant, zéro en surplus.

Contrat de voix (FR) :
- Registre Le Figaro Magazine · Condé Nast Traveler France · Côté Sud ·
  Air France Magazine — hospitalité éditoriale, jamais blog-de-voyage,
  jamais chaîne-hôtelière. Vouvoiement systématique de l'hôte.
- Détail concret : Val d'Orcia · Pienza · Sienne · zone UNESCO ·
  presbytère du XVIIe siècle · restauration de 2009 par le studio
  Castellini-Mancini · huit suites · brigade de quatorze personnes ·
  spa Aqua souterraine · restaurant étoilé Michelin (chef Tommaso
  Brigliadori) · pergola de glycine · cave du XVIIIe siècle.
- Ancre de voix `hospitalité de borgo` — usage éditorial consacré en
  français pour les villages toscans (cf. Le Figaro · Châteaux & Hôtels
  Collection). Le mot `borgo` reste tel quel en tant qu'emprunt à
  l'italien. Verbatim dans chaque bandeau primaire.
- Noms propres italiens préservés tels quels : Borgo San Marco · Vittoria
  Sernigi · Federico Bonechi · Tommaso Brigliadori · Anna Ricci · Caterina
  Sandri · Pietro Brero · suites (La Vigna, Il Frantoio, Il Pozzo, La
  Cisterna, La Torre, Il Cortile, La Loggia, La Cantina) · lieux (Pienza,
  Val d'Orcia, Montalcino, Montepulciano, Bagno Vignoni, San Quirico
  d'Orcia, Monte Amiata, Castelmuzio) · vins et appellations DOCG/DOC ·
  producteurs (Biondi-Santi, Casanova di Neri, Avignonesi, Salcheto, etc.)
  · Relais & Châteaux · Touring Club Italiano · AIS · Plaza Athénée ·
  Cipriani.
- Chiffres en chiffres arabes (latins) · 24 heures · trentaine, etc.
"""
from __future__ import annotations

from typing import Any


# Imagery — pool Unsplash CC0 boutique-hôtel (mêmes URLs que IT · partage
# du pack visuel commun en attendant la curation X.5).
_HERO_COURTYARD = "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=1600&q=80&auto=format&fit=crop"
_SUITE_VIGNA = "https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=1200&q=80&auto=format&fit=crop"
_SUITE_FRANTOIO = "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1200&q=80&auto=format&fit=crop"
_SUITE_POZZO = "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=1200&q=80&auto=format&fit=crop"
_SUITE_CISTERNA = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1200&q=80&auto=format&fit=crop"
_SUITE_TORRE = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200&q=80&auto=format&fit=crop"
_SUITE_CORTILE = "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=1200&q=80&auto=format&fit=crop"
_SUITE_LOGGIA = "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=1200&q=80&auto=format&fit=crop"
_SUITE_CANTINA = "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=1200&q=80&auto=format&fit=crop"
_BORGO_VALDORCIA = "https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?w=1200&q=80&auto=format&fit=crop"
_BORGO_PIENZA = "https://images.unsplash.com/photo-1568822617270-2c1579f8dfe2?w=1200&q=80&auto=format&fit=crop"
_BORGO_MONTALCINO = "https://images.unsplash.com/photo-1517760444937-f6397edcbbcd?w=1200&q=80&auto=format&fit=crop"
_BORGO_CIPRESSI = "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=1200&q=80&auto=format&fit=crop"
_BORGO_CHIANTI = "https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=1200&q=80&auto=format&fit=crop"
_BORGO_PIENZA_PIAZZA = "https://images.unsplash.com/photo-1543429776-2782fc8e1acd?w=1200&q=80&auto=format&fit=crop"
_PORTRAIT_DIRECTOR = "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_MAITRE = "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_CHEF = "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_SOMMELIER = "https://images.unsplash.com/photo-1566753323558-f4e0952af115?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_SPA = "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=900&q=80&auto=format&fit=crop"


ALBERGO_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Le borgo",       "kind": "home"},
        {"slug": "camere",     "label": "Les suites",     "kind": "blog_list"},
        {"slug": "borgo",      "label": "Le territoire",  "kind": "about"},
        {"slug": "brigata",    "label": "La brigade",     "kind": "team"},
        {"slug": "soggiorno",  "label": "Séjour",         "kind": "services"},
        {"slug": "concierge",  "label": "Conciergerie",   "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":   "B",
        "logo_word":      "Borgo San Marco",
        "logo_subline":   "Relais & Spa · Pienza depuis 1612",
        "tag":            "Saison 2026 · réservations ouvertes de mai à octobre",
        "phone":          "+39 0578 748 124",
        "phone_label":    "Ligne directe conciergerie",
        "email":          "concierge@borgosanmarco.it",
        "email_label":    "Écrivez à la direction",
        "address":        "Borgo San Marco di Sopra · 53026 Pienza · Sienne",
        "hours_compact":  "Réception 24 heures · arrivée à partir de 14 h · départ avant 11 h",
        "hours_footer_rows": [
            "Réception ouverte 24 heures avec concierge en salle",
            "Langues de salle : italiano · english · français · deutsch",
        ],
        "license":        "Code CITRA 0521-053026-100201 · Cat. Cinq Étoiles Luxe · Insc. Confindustria Alberghi 0428",
        "footer_intro":
            "Borgo San Marco est un relais de huit suites aménagé dans le presbytère "
            "du XVIIe siècle du borgo éponyme, hameau de colline de Pienza ouvert sur "
            "le Val d'Orcia UNESCO. Restauration du studio Castellini-Mancini en 2009, "
            "affiliation Relais & Châteaux depuis 2014, une étoile Michelin pour le "
            "restaurant Trebbio depuis 2019. L'hospitalité de borgo est notre promesse : "
            "une seule réception pour les huit chambres, une brigade de salle de "
            "quatorze personnes et la quiétude d'un borgo encore habité.",

        # Nav reservation CTA (hospitality)
        "nav_cta":         "Réservez votre séjour",
        "nav_cta_kind":    "appointment",
        "nav_cta_short":   "Réservez",

        # Footer labels
        "foot_studio":   "Le relais",
        "foot_pages":    "Plan du site",
        "foot_contact":  "Conciergerie",
        "foot_offices":  "Sites",
        "offices_footer_rows": [
            "Borgo San Marco di Sopra · 53026 Pienza · Sienne",
            "Tenuta Trebbio · cave et oliveraie · 1,2 km au sud",
        ],
        "office_rows": [
            "Borgo San Marco di Sopra 17 · 53026 Pienza · Sienne",
            "Tél. +39 0578 748 124 · concierge@borgosanmarco.it",
        ],
        "dossier_label":     "Suite",
        "portfolio_label":   "Nuitées / an",
        "territorio_label":  "Borgo",
        "superficie_label":  "Surface",
        "provenance_label":  "Vue",
        "access_label":      "Langues de salle",
        "availability_label": "Saisonnalité",
        "price_note":        "Tarif sur demande · forfaits saisonniers",
        "nda_required_label": "Confidentiel",
        "viewing_on_request": "Uniquement sur réservation",
        "referent_label":    "Référent en salle",
        "concierge_line_label": "Concierge dédié",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "cover_location":    "Borgo San Marco di Sopra · Val d'Orcia · UNESCO",
        "cover_image_credit": "Photographie · Massimo Listri",
        "cover_image":       _HERO_COURTYARD,

        "eyebrow":           "Relais & Spa · Val d'Orcia · Pienza depuis 1612",
        "headline":          'Huit suites dans un borgo toscan du XVIIe siècle. <em>Hospitalité de borgo</em>, une seule saison par an.',
        "sub":
            "Un relais de huit suites aménagé dans le presbytère du XVIIe siècle de "
            "Borgo San Marco di Sopra, hameau de colline de Pienza ouvert sur le "
            "Val d'Orcia. L'hospitalité de borgo s'y décline en ouverture saisonnière "
            "de mai à fin octobre · réception entière · cuisine étoilée Michelin · "
            "spa Aqua di Borgo dans la citerne du XVIIIe siècle · cave personnelle.",
        "hero_wordmark":     "Borgo San Marco",
        "hero_location":     "Pienza · Sienne · Toscane",
        "hero_counter_label": "Suites",
        "hero_counter_value": "8",
        "hero_series_label": "Saison",
        "hero_series_title": "2026 · Avril – Octobre",
        "hero_series_note":  "Ouverture le 18 avril · fermeture le 27 octobre · brigade de 14 personnes en salle",

        "primary_cta":         "Réservez votre séjour",
        "primary_cta_href":    "concierge",
        "secondary_cta":       "Découvrez les suites",
        "secondary_cta_href":  "camere",

        # Hero credit cells — list[4] of tuple[2] (label, value)
        "hero_credit_cells": [
            ("Affiliation",   "Relais & Châteaux"),
            ("Cuisine",       "Une étoile Michelin"),
            ("Restauration",  "Castellini-Mancini · 2009"),
            ("Ouverture",     "Saisonnière · 24 semaines"),
        ],

        # Signature suite section — list[6] of dict (keys: slug, image,
        # index, title, territorio, superficie, provenance, availability)
        "signature_label":    "Les suites",
        "signature_heading":  "Les suites de la maison, une pour chaque pièce du borgo.",
        "signature_intro":
            "Huit suites, chacune aménagée dans un volume historique du presbytère et "
            "de la cave du XVIIIe siècle attenante. Aucune chambre n'est semblable à "
            "une autre ; toutes ouvertes sur le Val d'Orcia. C'est ainsi que se "
            "dessine l'hospitalité de borgo, pièce après pièce.",
        "signature": [
            {
                "slug":         "suite-la-vigna",
                "image":        _SUITE_VIGNA,
                "index":        "Suite 01",
                "title":        "La Vigna",
                "territorio":   "Côté ouest · premier étage",
                "superficie":   "62 m² · lit king-size",
                "provenance":   "Vue sur le vignoble historique de Sangiovese",
                "availability": "Disponible mai – septembre",
            },
            {
                "slug":         "suite-il-frantoio",
                "image":        _SUITE_FRANTOIO,
                "index":        "Suite 02",
                "title":        "Il Frantoio",
                "territorio":   "Rez-de-chaussée · aile sud",
                "superficie":   "78 m² · lit double + salon",
                "provenance":   "Ancienne meule du moulin à huile de 1620 au centre de la pièce",
                "availability": "Disponible toute la saison",
            },
            {
                "slug":         "suite-il-pozzo",
                "image":        _SUITE_POZZO,
                "index":        "Suite 03",
                "title":        "Il Pozzo",
                "territorio":   "Cour intérieure · rez-de-chaussée",
                "superficie":   "54 m² · lit double standard",
                "provenance":   "Puits octogonal du XVIIe siècle dans la cour privée",
                "availability": "Sur demande · couples uniquement",
            },
            {
                "slug":         "suite-la-cisterna",
                "image":        _SUITE_CISTERNA,
                "index":        "Suite 04",
                "title":        "La Cisterna",
                "territorio":   "Aile est · niveau souterrain",
                "superficie":   "88 m² · lit à baldaquin",
                "provenance":   "Voûte de la citerne du XVIIIe siècle · lumière zénithale",
                "availability": "Sur demande · lune de miel conseillée",
            },
            {
                "slug":         "suite-la-torre",
                "image":        _SUITE_TORRE,
                "index":        "Suite 05",
                "title":        "La Torre",
                "territorio":   "Tour d'angle · deuxième étage",
                "superficie":   "70 m² · lit double + bureau",
                "provenance":   "Vue à 270° sur le Val d'Orcia jusqu'au Monte Amiata",
                "availability": "Disponible avril – octobre",
            },
            {
                "slug":         "suite-il-cortile",
                "image":        _SUITE_CORTILE,
                "index":        "Suite 06",
                "title":        "Il Cortile",
                "territorio":   "Rez-de-chaussée · aile nord",
                "superficie":   "65 m² · lit double + jardin privé",
                "provenance":   "Loggia privée sur la pergola de glycine",
                "availability": "Disponible mai – octobre",
            },
        ],
        "signature_link_all":  "Voir l'ensemble des huit suites",
        "signature_link_href": "camere",

        # Territory chip-row — list of scalar strings
        "territory_label": "Territoire",
        "territory": [
            "Pienza · Val d'Orcia",
            "Montalcino · caves du Brunello",
            "Montepulciano · Vino Nobile",
            "San Quirico d'Orcia · voies historiques",
            "Bagno Vignoni · thermes médiévales",
            "Monte Amiata · randonnées",
            "Sienne · Palio en juillet et août",
            "Cortona · voies étrusques",
        ],

        # Director / advisor band — single block
        "advisor_label":     "La direction",
        "advisor_heading":   "Une directrice qui travaille en salle. <em>Trente-deux saisons d'hôtellerie</em>.",
        "advisor_intro":
            "Borgo San Marco est dirigé en personne par Vittoria Sernigi, hôtelière "
            "toscane née en 1964, élève du Maestro Casiraghi au Plaza Athénée à Paris "
            "et du Maestro Cipriani au Cipriani de Venise. Trente-deux saisons "
            "d'hôtellerie de luxe avant de reprendre le borgo en 2008.",
        "advisor_name":      "Vittoria Sernigi",
        "advisor_role":      "Directrice · membre du Touring Club Italiano · sommelier AIS",
        "advisor_bio":
            "Trente-deux ans d'hôtellerie internationale avant Pienza : Plaza Athénée "
            "Paris · Cipriani Venise · Villa San Michele à Fiesole. Membre du Touring "
            "Club Italiano depuis 1995, sommelier AIS depuis 2002, formatrice à l'École "
            "Hôtelière de Sienne. En salle chaque matin au petit-déjeuner, chaque soir "
            "à la remise des clés.",
        "advisor_portrait":  _PORTRAIT_DIRECTOR,
        "advisor_cta":       "Écrivez à Vittoria",
        "advisor_cta_href":  "concierge",

        # Numbers band — list[4] of tuple[2] (counter, label)
        "numbers_label":    "Borgo San Marco en chiffres",
        "numbers_heading":  "Une saison, une seule réception, une brigade.",
        "numbers": [
            ("8",   "Suites · aucune semblable à une autre"),
            ("14",  "Personnes en brigade de salle"),
            ("1",   "Étoile Michelin · restaurant Trebbio"),
            ("12",  "Années d'affiliation Relais & Châteaux"),
        ],
        "numbers_note":
            "Ouverture saisonnière 18 avril – 27 octobre · brigade de salle entière "
            "présente sur les 12 services · réception 24 heures.",

        # Press band — list of scalar strings (NB: home version, NOT team version)
        "press_label":   "Revue de presse",
        "press_intro":   "Borgo San Marco dans les pages voyage éditoriales 2023-2025",
        "press_items": [
            "Condé Nast Traveler Italia",
            "Touring Magazine",
            "Departures",
            "Monocle Travel",
            "Bell'Italia",
        ],

        # Private band — closing CTA
        "private_label":     "Pour vos hôtes les plus chers",
        "private_heading":   "Le borgo entier, une seule famille. <em>Exclusivité de huit jours</em>.",
        "private_intro":
            "Le borgo peut être réservé en exclusivité pour une seule famille ou un "
            "groupe restreint · huit suites privatisées, brigade dédiée, restaurant "
            "fermé au public, cave ouverte aux hôtes. C'est l'hospitalité de borgo "
            "à son expression la plus rare. Disponibilité sur trois fenêtres par an "
            "uniquement · écrivez à la direction au moins six mois à l'avance.",
        "private_primary":      "Écrivez à la direction",
        "private_primary_href": "concierge",
        "private_secondary":    "Découvrez le borgo",
        "private_secondary_href": "borgo",
    },

    # ─── CAMERE (blog_list of suites) ─────────────────────────
    "camere": {
        "eyebrow":          "Huit suites · Borgo San Marco",
        "headline":         "Les suites de la maison.",
        "intro":
            "Chaque suite porte le nom d'un volume historique du borgo · chacune a "
            "été repensée par le studio Castellini-Mancini en 2009 en conservant le "
            "plan d'origine du XVIIe siècle. L'hospitalité de borgo se lit dans "
            "chacun des huit volumes.",
        "lead_image":       _HERO_COURTYARD,
        "filter_label":     "Affinez la recherche",
        "filter_groups": [
            {"label": "Vue", "options": ["Vignoble", "Cour", "Borgo", "Val d'Orcia", "Pergola"]},
            {"label": "Lits", "options": ["Lit king-size", "Lit double + salon", "Lit à baldaquin", "Suite avec bureau"]},
            {"label": "Saison", "options": ["Ouverture avril", "Disponible mai – septembre", "Haute saison uniquement"]},
        ],
        "sort_label":       "Trier",
        "sort_options": [
            "Par surface · de la plus vaste",
            "Par saisonnalité",
            "Par nombre d'hôtes",
            "Par quiétude",
        ],
        "result_count":     "8 suites disponibles pour la saison 2026",
        "result_subtitle":  "Réception entière pour les huit chambres · brigade de salle dédiée.",
        "footer_note_label": "Tarifs",
        "footer_note":
            "Toutes les suites incluent le petit-déjeuner en salle, l'accès illimité "
            "à la spa Aqua di Borgo et une dégustation de trois vins en cave sur "
            "réservation. L'hospitalité de borgo est comprise dans chaque nuitée. "
            "Tarif saisonnier communiqué au moment de la demande.",
    },

    # ─── BORGO (about · territorio del relais) ────────────────
    "borgo": {
        "eyebrow":          "Val d'Orcia · UNESCO",
        "headline":         "Un borgo du XVIIe siècle encore habité.",
        "intro":
            "Borgo San Marco di Sopra est un hameau de colline de Pienza · 41 "
            "habitants résidents · place centrale de 1571 · presbytère de 1612 "
            "(aujourd'hui relais) · cave du XVIIIe siècle (aujourd'hui spa). Le borgo "
            "est encore habité par les six mêmes familles depuis quatre générations ; "
            "le relais en est l'hôte le plus récent, depuis 2009 · c'est de cette "
            "cohabitation que naît l'hospitalité de borgo.",

        "statement_label":   "Notre hospitalité",
        "statement_heading": "Huit suites, une seule brigade, un borgo entier.",
        "statement_text":
            "L'hospitalité de borgo signifie qu'il n'y a qu'une seule réception pour "
            "les huit suites, que la brigade de salle connaît chaque hôte par son "
            "prénom dès le deuxième jour, et que le borgo demeure un borgo (avec ses "
            "41 habitants) y compris lorsque vous y êtes hôtes. Nous ne sommes pas un "
            "resort. Nous ne sommes pas une chaîne. Nous ne sommes pas un hôtel de ville.",

        "territories_label":   "Les environs",
        "territories_heading": "Six territoires à moins d'une heure du borgo.",
        "territories_intro":
            "Les environs du Val d'Orcia font partie intégrante de l'hospitalité du "
            "relais : chaque territoire dispose d'un référent en salle dédié à la "
            "découverte · vin, thermes, parcours étrusques, randonnées sur l'Amiata, "
            "opéra au Palio de Sienne.",
        "territories": [
            {
                "image":      _BORGO_VALDORCIA,
                "name":       "Val d'Orcia",
                "region":     "Pienza · San Quirico · Bagno Vignoni",
                "history":    "Patrimoine UNESCO depuis 2004 · paysage Renaissance codifié par Lorenzetti. Cyprès, crêtes argileuses et fermes.",
                "architects": "Cyprès en ligne · voies cavées étrusques",
                "count":      "12 km",
                "since":      "Visite : 1 heure · référent Federico en salle",
            },
            {
                "image":      _BORGO_MONTALCINO,
                "name":       "Montalcino",
                "region":     "Caves historiques du Brunello",
                "history":    "Caves historiques du Brunello di Montalcino DOCG · Biondi-Santi, Casanova di Neri, Il Poggione. Dégustations privées sur rendez-vous.",
                "architects": "Pieves médiévales · châteaux siennois",
                "count":      "28 km",
                "since":      "Visite : 1 journée · référent sommelier AIS",
            },
            {
                "image":      _BORGO_PIENZA,
                "name":       "Pienza · la cité idéale",
                "region":     "Piazza Pio II · cathédrale · Palazzo Piccolomini",
                "history":    "La cité idéale de la Renaissance dessinée par Bernardo Rossellino pour Pio II en 1462. Place, cathédrale, Palazzo Piccolomini, vue sur l'Amiata.",
                "architects": "Bernardo Rossellino · 1459-1462",
                "count":      "1,8 km",
                "since":      "Visite : 2 heures à pied · le concierge vous accompagne sur demande",
            },
            {
                "image":      _BORGO_CHIANTI,
                "name":       "Montepulciano",
                "region":     "Vino Nobile · caves souterraines",
                "history":    "Caves souterraines creusées dans le tuf, certaines du XIVe siècle. Dégustation du Vino Nobile di Montepulciano DOCG · maisons Avignonesi, Salcheto, Boscarelli.",
                "architects": "Antonio da Sangallo il Vecchio · Vignola",
                "count":      "32 km",
                "since":      "Visite : 1 journée · référent sommelier AIS",
            },
            {
                "image":      _BORGO_CIPRESSI,
                "name":       "Bagno Vignoni",
                "region":     "Thermes libres du XVe siècle",
                "history":    "Place-bassin thermal du XVe siècle, unique au monde. Eau sulfureuse à 49 °C jaillissant de la roche, accès libre. Dîner à la trattoria de la place avec Caterina la cuisinière.",
                "architects": "Bassin naturel · XVe siècle",
                "count":      "8 km",
                "since":      "Visite : demi-journée · référent de salle Federico",
            },
            {
                "image":      _BORGO_PIENZA_PIAZZA,
                "name":       "Monte Amiata",
                "region":     "Volcan éteint · hêtraies · téléski",
                "history":    "Volcan éteint (1 738 m). Hêtraies séculaires, sentiers CAI, téléski en hiver. Fête des châtaignes en novembre dans le borgo de Castiglione d'Orcia.",
                "architects": "Sentiers CAI · 4 sommets balisés",
                "count":      "38 km",
                "since":      "Visite : 1 journée · guide de haute montagne sur réservation",
            },
        ],
        "territory_card_cta":      "Planifions ensemble · écrivez à la direction",
        "territory_card_cta_href": "concierge",

        "referent_label":   "Le référent en salle",
        "referent_heading": "Un seul référent pour tout le séjour.",
        "referent_text":
            "Dès l'arrivée, chaque hôte se voit attribuer un référent unique en salle "
            "— le maître d'hôtel Federico Bonechi ou la sommelière Anna Ricci selon la "
            "saison. Le référent accompagne toute la réservation : restaurant, "
            "massages en spa, dégustations en cave, excursions dans les environs. "
            "Voilà le visage humain de l'hospitalité de borgo.",

        "stats_label":  "Borgo San Marco · chiffres 2025",
        # list[4] of tuple[2]
        "stats": [
            ("12",  "Années d'affiliation Relais & Châteaux"),
            ("162", "Nuits ouvertes par an"),
            ("8",   "Suites · saison 2026"),
            ("41",  "Habitants résidents du borgo"),
        ],
    },

    # ─── BRIGATA (team · staff in sala) ───────────────────────
    "brigata": {
        "eyebrow":       "La brigade · 14 personnes en salle",
        "headline":      "La même brigade depuis douze saisons.",
        "intro":
            "La brigade de Borgo San Marco est composée de quatorze personnes, dont "
            "dix reviennent chaque saison depuis 2014. Réception, salle, restaurant, "
            "spa, cave · une seule brigade pour huit suites, gardienne de "
            "l'hospitalité de borgo au quotidien.",

        "director_label":       "Direction",
        "director_name":        "Vittoria Sernigi",
        "director_role":        "Directrice · propriétaire depuis 2008 · sommelier AIS · TCI",
        "director_text":
            "Vittoria Sernigi a repris Borgo San Marco en 2008 après trente-deux "
            "saisons d'hôtellerie internationale entre Paris, Venise et Fiesole. "
            "Diplôme de l'École Hôtelière Internationale de Lausanne (1985), "
            "perfectionnement en management hôtelier à Cornell. Membre du Touring "
            "Club Italiano depuis 1995, sommelier AIS depuis 2002.",
        "director_portrait":    _PORTRAIT_DIRECTOR,
        "director_quote":
            "L'hospitalité de borgo est la seule hospitalité que je connaisse. C'est "
            "la plus lente, c'est la plus exigeante, c'est la plus gratifiante.",
        "director_quote_attribution": "Vittoria Sernigi · entretien à Touring · 2024",

        "advisors_label":   "La brigade de salle",
        "advisors_heading": "Quatre référents, dix saisonniers · une seule salle.",
        "advisors_intro":
            "Quatre référents seniors conduisent la salle. Les décisions de service "
            "passent par leur jugement, jamais par l'algorithme d'une chaîne · ainsi "
            "se transmet l'hospitalité de borgo d'une saison à l'autre.",
        # list[4] of dict (portrait, name, role, bio, territories, since, langs)
        "advisors": [
            {
                "portrait":    _PORTRAIT_MAITRE,
                "name":        "Federico Bonechi",
                "role":        "Maître d'hôtel · référent unique des hôtes",
                "bio":
                    "Maître d'hôtel depuis 2009 · dix saisons à Borgo San Marco. "
                    "Diplômé de l'Alberghiero di Chianciano · expérience au Castello "
                    "Banfi et au Plaza Athénée. Connaît le prénom de chaque hôte dès "
                    "le deuxième jour.",
                "territories": "Salle · réception · conciergerie",
                "since":       "Dans la brigade depuis 2014",
                "langs":       "Italiano · English · Français",
            },
            {
                "portrait":    _PORTRAIT_CHEF,
                "name":        "Tommaso Brigliadori",
                "role":        "Chef · restaurant Trebbio · une étoile Michelin",
                "bio":
                    "Chef du restaurant Trebbio depuis 2017 · étoile Michelin depuis "
                    "2019. Formé à l'Albereta sous Gualtiero Marchesi, perfectionné "
                    "auprès de Bottura à Modène. Cuisine du territoire : pici, picci "
                    "et pinoli, agneau de Zeri, haricots zolfini, caciotta di Pienza.",
                "territories": "Cuisine · cave · jardin potager",
                "since":       "Dans la brigade depuis 2017",
                "langs":       "Italiano · English",
            },
            {
                "portrait":    _PORTRAIT_SOMMELIER,
                "name":        "Anna Ricci",
                "role":        "Sommelier AIS · responsable cave",
                "bio":
                    "Sommelier AIS depuis 2008 · responsable cave depuis 2015. La "
                    "cave abrite 4 200 références entre Brunello, Vino Nobile, Chianti "
                    "Classico et une petite collection de Champagne. Dégustations "
                    "privées en cave pour les hôtes, deux fois par semaine.",
                "territories": "Cave · dégustations · accord mets-vins au restaurant",
                "since":       "Dans la brigade depuis 2015",
                "langs":       "Italiano · English · Deutsch",
            },
            {
                "portrait":    _PORTRAIT_SPA,
                "name":        "Caterina Sandri",
                "role":        "Responsable Aqua di Borgo Spa",
                "bio":
                    "Responsable de la spa depuis 2018 · diplôme d'hydrothérapie à "
                    "l'Université de Sienne, formation en spa management chez Six "
                    "Senses Toscane. La spa Aqua di Borgo est aménagée dans la "
                    "citerne du XVIIIe siècle · uniquement sur rendez-vous.",
                "territories": "Spa Aqua di Borgo · soins · piscine souterraine",
                "since":       "Dans la brigade depuis 2018",
                "langs":       "Italiano · English",
            },
        ],

        "partners_label":   "Les producteurs du borgo",
        "partners_heading": "Les fournisseurs historiques de la table.",
        "partners_intro":
            "Les matières premières du restaurant Trebbio proviennent de fournisseurs "
            "dans un rayon de trente kilomètres autour du borgo, à l'exception de "
            "l'huile (de production propre) et du pain (boulangerie du borgo à "
            "200 mètres).",
        # list[5] of tuple[2] (name, role)
        "partners": [
            ("Fattoria Trebbio",         "Huile d'olive extra-vierge en propre · oliveraie historique à 1,2 km du borgo"),
            ("Caseificio Castelmuzio",   "Pecorino de Pienza · caciotta · ricotta · 8 km de Pienza"),
            ("Azienda agricola Falcorosso", "Bœuf de Chianina · agneau de Zeri · volailles · 12 km"),
            ("Forno di Pienza · Lorenzini", "Pain toscan · schiacciate · gressins · 1,8 km du borgo"),
            ("Erbario di Sant'Anna",     "Herbes officinales · tisanerie de la spa Aqua · monastère à 18 km"),
        ],

        "press_label":   "Revue de presse · brigade et cuisine",
        "press_heading": "Distinctions et mentions de la brigade.",
        # list[5] of dict (magazine, issue, title, byline) — DIFFERENT shape from home.press_items!
        "press_items": [
            {
                "magazine": "Guida Michelin Italia",
                "issue":    "Éd. 2019 – confirmée 2025",
                "title":    "Une étoile · restaurant Trebbio · cuisine toscane de terroir",
                "byline":   "Rédaction Michelin",
            },
            {
                "magazine": "Touring Magazine",
                "issue":    "Avril 2024",
                "title":    "Vittoria Sernigi · portrait de la directrice de borgo",
                "byline":   "Maria Sirotti",
            },
            {
                "magazine": "Gambero Rosso",
                "issue":    "Janvier 2025 · Tre forchette",
                "title":    "Trebbio de Borgo San Marco · trois fourchettes confirmées",
                "byline":   "Eleonora Cozzella",
            },
            {
                "magazine": "Condé Nast Traveler Italia",
                "issue":    "Mai 2023 · Gold List",
                "title":    "Borgo San Marco · Top 50 Italie",
                "byline":   "Caterina Cesari",
            },
            {
                "magazine": "Bell'Italia",
                "issue":    "Septembre 2024",
                "title":    "Les 12 grandes maisons d'hospitalité du Val d'Orcia",
                "byline":   "Giovanni Rajberti",
            },
        ],

        "numbers_label": "La brigade en chiffres",
        # list[6] of tuple[2]
        "numbers": [
            ("14", "Personnes en brigade de salle"),
            ("10", "Saisonniers récurrents depuis 2014"),
            ("32", "Années d'expérience de la directrice"),
            ("4",  "Langues de salle (IT · EN · FR · DE)"),
            ("12", "Années d'affiliation Relais & Châteaux"),
            ("4200", "Références en cave · responsable Anna Ricci AIS"),
        ],

        "visit_label":         "Pour écrire à la brigade",
        "visit_heading":       "Une seule brigade, une seule salle.",
        "visit_text":
            "Pour vos questions de menu, d'allergies, de vin, d'excursions ou de "
            "soins en spa, écrivez directement à la brigade : nous répondons dans "
            "la journée ouvrée suivante. Vittoria signe personnellement la "
            "confirmation de réservation — c'est la marque de l'hospitalité de "
            "borgo dans la correspondance.",
        "visit_primary":       "Écrivez à la direction",
        "visit_primary_href":  "concierge",
    },

    # ─── SOGGIORNO (services · l'esperienza del soggiorno) ────
    "soggiorno": {
        "eyebrow":      "L'expérience · cinq temps du séjour",
        "headline":     "Cinq temps · de Pienza au retour.",
        "intro":
            "Le séjour à Borgo San Marco s'articule en cinq temps · l'arrivée, la "
            "salle, la spa, la cave et la sortie vers le territoire. Chaque temps "
            "est orchestré par le référent de salle · cinq tempi pour décliner "
            "l'hospitalité de borgo.",

        "process_label":   "Cinq temps",
        "process_heading": "Comment se déroule un séjour.",
        "process_intro":
            "Le récit du séjour est un seul, du moment où vous écrivez à la "
            "direction jusqu'au retour à la maison.",
        # list[5] of dict (n, title, text, duration)
        "process": [
            {
                "n":        "01",
                "title":    "La confirmation",
                "text":
                    "Réponse personnelle de Vittoria dans les 24 heures suivant la "
                    "demande · choix de la suite, de la fenêtre saisonnière, "
                    "éventuelles demandes particulières (menu, allergies, "
                    "excursions).",
                "duration": "1 journée",
            },
            {
                "n":        "02",
                "title":    "L'arrivée",
                "text":
                    "Réception à partir de 14 h · transfert depuis l'aéroport de "
                    "Florence sur demande · accueil sur la place du borgo avec un "
                    "vin du territoire · présentation du référent de salle.",
                "duration": "2 heures",
            },
            {
                "n":        "03",
                "title":    "La salle et la cave",
                "text":
                    "Dîner au restaurant Trebbio · menu du territoire en cinq temps "
                    "· accord des vins commenté par la sommelière · cave ouverte "
                    "après le dîner pour qui souhaite prolonger la soirée.",
                "duration": "Une soirée par séjour",
            },
            {
                "n":        "04",
                "title":    "La spa et le territoire",
                "text":
                    "Demi-journée à la spa Aqua di Borgo (citerne du XVIIIe siècle) "
                    "· nage, hammam, sauna, hydromassage dans le bassin naturel · "
                    "soins sur rendez-vous · excursion d'une demi-journée en Val "
                    "d'Orcia avec le référent.",
                "duration": "Une demi-journée",
            },
            {
                "n":        "05",
                "title":    "Le départ",
                "text":
                    "Départ avant 11 h · petit-déjeuner prolongé jusqu'à 10 h 30 "
                    "sous la pergola de glycine · cadeau de départ (huile d'olive "
                    "extra-vierge de la Fattoria Trebbio · petit livret du borgo) "
                    "· accompagnement au moment du retour.",
                "duration": "1 demi-journée",
            },
        ],

        "testimonial_label":  "La voix de l'hôte",
        "testimonial_text":
            "« Trois séjours en trois saisons différentes, toujours la même "
            "brigade, toujours Federico à la réception. Il est rare, en Italie, "
            "de trouver un hôtel où la promesse faite la première fois reste "
            "vraie jusqu'à la troisième visite. »",
        "testimonial_author": "Giorgio Borghi · Milan · hôte depuis 2018",

        "faq_label":    "Questions récurrentes posées à la direction",
        # list[6] of dict (q, a)
        "faq_items": [
            {
                "q": "L'hôtel est-il ouvert toute l'année ?",
                "a":
                    "Non. Borgo San Marco ouvre du 18 avril au 27 octobre 2026 — "
                    "vingt-quatre semaines de saison. La fermeture hivernale "
                    "permet l'entretien des suites et le repos de la brigade de "
                    "salle. Aucune exception, pas même pour le Nouvel An.",
            },
            {
                "q": "Peut-on réserver le borgo entier pour une famille ?",
                "a":
                    "Oui · sur trois fenêtres par an (juin, septembre, fin octobre). "
                    "Huit suites privatisées · restaurant fermé au public extérieur "
                    "· brigade dédiée. Écrivez à la direction au moins six mois "
                    "avant la date souhaitée.",
            },
            {
                "q": "Peut-on organiser des mariages dans le borgo ?",
                "a":
                    "Uniquement des mariages intimes · 36 invités au maximum · "
                    "cérémonie civile dans la loggia de l'étage noble · dîner sous "
                    "la pergola de glycine. Nous n'organisons pas de mariages de "
                    "plus de 36 invités afin de préserver la dimension du borgo. "
                    "Écrivez à Vittoria au moins un an à l'avance.",
            },
            {
                "q": "Acceptez-vous les chiens de petite taille ?",
                "a":
                    "Oui · sur demande · dans deux suites du rez-de-chaussée (Il "
                    "Frantoio et Il Pozzo). Supplément de 30 € par nuit · gamelle, "
                    "couchage et biscuits compris. Pet sitter du borgo disponible "
                    "sur rendez-vous pour la durée du dîner au restaurant.",
            },
            {
                "q": "Puis-je visiter la cave sans être hôte du restaurant ?",
                "a":
                    "Oui · la cave est ouverte aux hôtes du borgo deux fois par "
                    "semaine (mardi et jeudi après-midi, 17 h – 19 h) pour une "
                    "dégustation de trois vins avec Anna · réservation obligatoire "
                    "à la réception.",
            },
            {
                "q": "Y a-t-il le wi-fi dans les suites ?",
                "a":
                    "Oui · ligne en fibre à 1 Gbit/s · disponible dans toutes les "
                    "huit suites, en salle et à la spa. Sur demande, il est "
                    "possible d'activer un mode digital detox : la suite reste "
                    "sans connexion pendant tout le séjour · coffret pour les "
                    "appareils à l'arrivée.",
            },
        ],

        "cta_label":         "Pour commencer",
        "cta_heading":       "<em>Une saison courte</em>, une seule brigade.",
        "cta_text":
            "Les fenêtres saisonnières de 2026 ouvrent le 18 avril · les suites les "
            "plus demandées (La Vigna, Il Cortile, La Torre) sont complètes dès "
            "le mois de mai. Écrivez à la direction pour la réservation et "
            "rejoignez l'hospitalité de borgo le temps d'une saison.",
        "cta_primary":       "Réservez votre séjour",
        "cta_primary_href":  "concierge",
    },

    # ─── CONCIERGE (contact · concierge dedicato) ─────────────
    "concierge": {
        "eyebrow":      "Concierge dédié · Vittoria Sernigi",
        "headline":     "Écrivez à la direction.",
        "intro":
            "Pour une demande de réservation, les dates d'exclusivité du borgo, les "
            "forfaits saisonniers et toute question concernant votre séjour, "
            "écrivez directement à la direction. Vittoria répond personnellement "
            "dans la journée ouvrée suivante · entrée en matière de l'hospitalité "
            "de borgo.",

        "phone_label":   "Lignes directes",
        "phone_intro":
            "Réception ouverte 24 heures · concierge dédié en salle en service "
            "continu · numéro direct pour les urgences.",
        # list[4] of tuple[2]
        "phone_rows": [
            ("Conciergerie", "+39 0578 748 124"),
            ("Direction",    "+39 0578 748 100 · Vittoria uniquement"),
            ("Restaurant",   "+39 0578 748 130 · réservations Trebbio"),
            ("Spa",          "+39 0578 748 145 · réservations Aqua"),
        ],

        "form_section_label": "Demande de réservation",
        "form_section_intro":
            "Indiquez les dates souhaitées, la suite que vous préférez (ou "
            "l'exclusivité du borgo) et toute demande particulière. Vittoria "
            "répond personnellement par courriel avec la confirmation ou une "
            "proposition alternative dans les 24 heures.",
        "form_helper_required":  "Champs marqués d'un · obligatoires",
        "form_submit_button":    "Envoyez la demande à la direction",
        "form_submit_note":
            "La confirmation définitive intervient par acompte de 30 % par "
            "virement bancaire · solde à l'arrivée à la réception.",
        # list[10] of dict (label, name, type, required, options)
        "form_fields": [
            {"label": "Nom et prénom",                "name": "name",       "type": "text",     "required": True,  "options": []},
            {"label": "Courriel · réponse directe",   "name": "email",      "type": "email",    "required": True,  "options": []},
            {"label": "Téléphone",                    "name": "phone",      "type": "tel",      "required": False, "options": []},
            {"label": "Date d'arrivée",               "name": "arrival",    "type": "date",     "required": True,  "options": []},
            {"label": "Date de départ",               "name": "departure",  "type": "date",     "required": True,  "options": []},
            {"label": "Nombre d'hôtes",               "name": "guests",     "type": "number",   "required": True,  "options": []},
            {"label": "Suite préférée",               "name": "suite",      "type": "select",   "required": False,
             "options": ["La Vigna", "Il Frantoio", "Il Pozzo", "La Cisterna", "La Torre", "Il Cortile", "Exclusivité du borgo · 8 suites", "Sans préférence"]},
            {"label": "Forfait",                      "name": "package",    "type": "select",   "required": False,
             "options": ["Séjour court · 2 nuits", "Séjour classique · 4 nuits", "Séjour long · 7 nuits", "Exclusivité du borgo · 5 nuits", "Mariage intime"]},
            {"label": "Allergies ou demandes alimentaires", "name": "allergies", "type": "text", "required": False, "options": []},
            {"label": "Note à la direction",          "name": "notes",      "type": "textarea", "required": False, "options": []},
        ],

        "offices_label":   "Adresses",
        "offices_heading": "Le borgo et les domaines.",
        "offices_intro":
            "Le borgo est accessible en voiture depuis Florence (1 h 45) ou Rome "
            "(2 h 30) · transfert depuis l'aéroport de Florence ou la gare de "
            "Chiusi-Chianciano sur demande.",
        # list[3] of dict (role, city, address, hours, email)
        "offices": [
            {
                "role":     "Borgo · réception",
                "city":     "Pienza · Sienne",
                "address":  "Borgo San Marco di Sopra 17 · 53026 Pienza",
                "hours":    "Réception 24 heures · arrivée 14 h – 22 h · départ avant 11 h",
                "email":    "concierge@borgosanmarco.it",
            },
            {
                "role":     "Fattoria Trebbio · cave et oliveraie",
                "city":     "Pienza · Sienne · 1,2 km du borgo",
                "address":  "Strada provinciale 146 · 53026 Pienza",
                "hours":    "Cave · mardi et jeudi 17 h – 19 h · dégustations sur réservation",
                "email":    "cantina@borgosanmarco.it",
            },
            {
                "role":     "Aqua di Borgo · spa",
                "city":     "Citerne du XVIIIe siècle · niveau souterrain",
                "address":  "Borgo San Marco di Sopra 17 · niveau –1",
                "hours":    "Spa 9 h – 13 h · 15 h – 20 h · soins sur rendez-vous",
                "email":    "spa@borgosanmarco.it",
            },
        ],

        "press_contact_label": "Presse et médias",
        "press_contact_text":
            "Pour vos demandes éditoriales, services photo et entretiens avec la "
            "direction · écrivez à Maria Bonelli, attachée de presse de Vittoria "
            "Sernigi, en précisant le titre et le sujet.",
        "press_contact_email": "stampa@borgosanmarco.it",
    },

    # ─── POSTS (8 suites · the room cards consumed by camere blog_list) ─
    "posts": [
        {
            "slug":         "suite-la-vigna",
            "image":        _SUITE_VIGNA,
            "kicker":       "Suite 01",
            "title":        "La Vigna",
            "date":         "Saison 2026 · avril – octobre",
            "author":       "Borgo San Marco",
            "read_min":     "62 m²",
            "lede":
                "La suite ouverte sur le vignoble historique de Sangiovese de la "
                "maison · premier étage de l'aile ouest · lit king-size · plafond "
                "à poutres d'origine du XVIIe siècle.",
            "footer_strap": "Disponible mai – septembre · vue vignoble",
            # list of 2-tuples (k, v)
            "meta_rows": [
                ("Étage",         "Premier · aile ouest"),
                ("Lits",          "Lit king-size + chaise longue"),
                ("Surface",       "62 m² + 8 m² de loggia"),
                ("Vue",           "Vignoble historique de Sangiovese · oliveraie"),
                ("Salle de bain", "Marbre travertin · douche walk-in + baignoire"),
                ("Inclusions",    "Petit-déjeuner · spa · dégustation en cave"),
                ("Saisonnalité",  "Disponible mai – septembre"),
            ],
            # list of 2-tuples (kind, text)
            "body": [
                ("p", "La Vigna est la suite la plus demandée de la maison · ouverture directe sur le vignoble historique de Sangiovese qui donne ses grappes au Brunello en propre de la Fattoria Trebbio. Plafond à poutres d'origine du XVIIe siècle, sol en terre cuite patinée, mobilier récupéré dans les maisons du borgo."),
                ("p", "La loggia privée de 8 m² est meublée d'un canapé en osier et d'une table en pierre serena · idéale pour le petit-déjeuner à deux ou pour le verre du soir de Brunello (toujours inclus, depuis la cave d'Anna)."),
                ("h3", "Le vignoble historique"),
                ("p", "Le vignoble en propre de la Fattoria Trebbio s'étend sur 4,2 hectares au sud du borgo, exposition est-sud-est. Vendange manuelle en octobre · vinification en petites cuves d'acier · élevage en grande botte de chêne · mise en bouteille au domaine. Le Brunello porte la même signature que le borgo."),
                ("ul", ["Capacité · deux adultes · sur demande berceau pour nourrisson", "Wifi · fibre 1 Gbit/s · ligne directe sur le réseau du borgo", "Climatisation · indépendante, réglable depuis la suite", "Coffre-fort · numérique · pour les objets de valeur", "TV · 55 pouces · chaînes internationales sur demande"]),
                ("p", "La suite La Vigna est disponible de mai à fin septembre. Pour la saison 2026, elle se réserve exclusivement en forfait d'au moins trois nuits."),
            ],
        },
        {
            "slug":         "suite-il-frantoio",
            "image":        _SUITE_FRANTOIO,
            "kicker":       "Suite 02",
            "title":        "Il Frantoio",
            "date":         "Saison 2026 · toute la période",
            "author":       "Borgo San Marco",
            "read_min":     "78 m²",
            "lede":
                "La suite la plus vaste · rez-de-chaussée de l'aile sud · au centre "
                "de la pièce, l'ancienne meule du moulin à huile de 1620 conservée "
                "comme élément architectural.",
            "footer_strap": "Disponible avril – octobre · rez-de-chaussée aile sud",
            "meta_rows": [
                ("Étage",         "Rez-de-chaussée · aile sud"),
                ("Lits",          "Lit double + salon séparé"),
                ("Surface",       "78 m² + 12 m² de patio"),
                ("Vue",           "Cour intérieure avec meule de 1620"),
                ("Salle de bain", "Marbre blanc · baignoire freestanding + douche"),
                ("Inclusions",    "Petit-déjeuner · spa · dégustation cave + huile"),
                ("Saisonnalité",  "Disponible toute la saison"),
            ],
            "body": [
                ("p", "Il Frantoio est la plus grande des huit suites · 78 m² au sol auxquels s'ajoutent 12 m² de patio privé sur la cour intérieure. La meule circulaire du moulin à huile d'origine de 1620 a été conservée au centre de la pièce comme élément architectural — non fonctionnelle mais intacte, en pierre serena."),
                ("p", "La suite comprend une petite cave privée avec six bouteilles du Brunello de la Fattoria Trebbio (millésimes 2018-2020) et une bouteille d'huile d'olive extra-vierge de l'oliveraie historique · les hôtes peuvent goûter à volonté et la facturation n'intervient qu'en fin de séjour."),
                ("h3", "Le moulin à huile historique"),
                ("p", "Le moulin à huile d'origine a été en activité de 1620 à 1968, lorsque l'huile de la Fattoria Trebbio a commencé à être travaillée au moulin commun de Pienza. La meule de la suite est l'une des deux d'origine · l'autre est exposée dans le musée de la maison, à côté de la cour."),
                ("ul", ["Capacité · deux adultes + un enfant sur le canapé-lit", "Wifi · fibre 1 Gbit/s", "Climatisation · indépendante, double zone chambre/salon", "Patio · 12 m² avec table et fauteuils en fer forgé", "Mini-cave privée · 6 bouteilles de Brunello + 1 bouteille d'huile d'olive extra-vierge"]),
                ("p", "Il Frantoio est disponible pendant toute la saison d'ouverture. Réservation d'au moins deux nuits."),
            ],
        },
        {
            "slug":         "suite-il-pozzo",
            "image":        _SUITE_POZZO,
            "kicker":       "Suite 03",
            "title":        "Il Pozzo",
            "date":         "Saison 2026 · sur demande",
            "author":       "Borgo San Marco",
            "read_min":     "54 m²",
            "lede":
                "La suite la plus réservée · rez-de-chaussée avec accès direct à la "
                "cour intérieure du XVIIe siècle · au centre de la cour, le puits "
                "octogonal d'origine de 1612.",
            "footer_strap": "Sur demande · couples uniquement · cour privée",
            "meta_rows": [
                ("Étage",         "Rez-de-chaussée · cour intérieure"),
                ("Lits",          "Lit double standard"),
                ("Surface",       "54 m² + cour privée 28 m²"),
                ("Vue",           "Cour octogonale avec puits de 1612"),
                ("Salle de bain", "Pierre serena · douche walk-in"),
                ("Inclusions",    "Petit-déjeuner · spa · cave · cour"),
                ("Saisonnalité",  "Sur demande · couples uniquement · animaux admis"),
            ],
            "body": [
                ("p", "Il Pozzo est la suite la plus réservée de la maison · accès uniquement par la cour intérieure, aucune ouverture sur l'extérieur du borgo. Le puits octogonal de 1612 est encore en service (eau douce depuis la nappe de San Quirico) et ombrage une petite cour de 28 m² à l'usage exclusif de la suite."),
                ("p", "Cette suite est réservée aux couples · sans enfant · et accepte sur demande les chiens de petite taille de moins de 10 kg (supplément de 30 € par nuit, gamelle et couchage compris)."),
                ("h3", "Le puits octogonal"),
                ("p", "Le puits octogonal est l'un des trois puits du borgo · le seul encore actif. Octogonal comme la coupole de Brunelleschi, dont Pio II était admirateur. Construit en 1612 par le même maçon qui éleva le presbytère · signature sculptée à l'intérieur de la margelle du puits, illisible depuis 1923 mais consignée dans un livret de 1898 conservé au presbytère."),
                ("ul", ["Capacité · deux adultes · pas d'enfants", "Petits chiens admis · supplément 30 €/nuit", "Cour privée · 28 m² avec table en fer · ombre du puits", "Wifi · fibre 1 Gbit/s", "Climatisation · indépendante"]),
                ("p", "Il Pozzo n'est disponible que sur demande directe à la direction. Séjour minimum de trois nuits."),
            ],
        },
        {
            "slug":         "suite-la-cisterna",
            "image":        _SUITE_CISTERNA,
            "kicker":       "Suite 04",
            "title":        "La Cisterna",
            "date":         "Saison 2026 · sur demande",
            "author":       "Borgo San Marco",
            "read_min":     "88 m²",
            "lede":
                "Suite aménagée dans la voûte de la citerne du XVIIIe siècle · "
                "niveau souterrain · lit à baldaquin · lumière zénithale par la "
                "lucarne d'origine de 1742.",
            "footer_strap": "Sur demande · lune de miel conseillée",
            "meta_rows": [
                ("Étage",         "Niveau souterrain (–1) · aile est"),
                ("Lits",          "Lit double + baldaquin en noyer"),
                ("Surface",       "88 m² · voûte à 4,2 m"),
                ("Vue",           "Lucarne zénithale · aucune ouverture extérieure"),
                ("Salle de bain", "Pierre travertin · baignoire en forme de citerne"),
                ("Inclusions",    "Petit-déjeuner · spa · cave · expérience nocturne"),
                ("Saisonnalité",  "Sur demande · lune de miel conseillée"),
            ],
            "body": [
                ("p", "La Cisterna est la suite la plus prisée du borgo · aménagée dans la voûte de la citerne du XVIIIe siècle, niveau souterrain, plafond à 4,2 mètres de hauteur. La lumière naturelle n'entre que par la lucarne zénithale de 1742 (d'origine) · la nuit, le ciel étoilé du Val d'Orcia s'invite directement dans la pièce."),
                ("p", "La citerne d'origine recueillait l'eau de pluie du toit du presbytère jusqu'en 1923, année où le borgo fut raccordé à l'aqueduc communal. La restauration Castellini-Mancini de 2009 a conservé la courbure d'origine et l'inscription murée du propriétaire du XVIIIe siècle (Giovan Pietro Buonsignori, 1742)."),
                ("h3", "Le lit à baldaquin"),
                ("p", "Le lit est une pièce historique · baldaquin en noyer massif du Pratomagno, ferronnerie battue à la main par le forgeron du borgo (Mario Calzini, 1971-2018, aujourd'hui son neveu Luca poursuit l'atelier). Étoffes du baldaquin en lin de Bonotto. Lampes à huile remplacées par de petites LED à température chaude."),
                ("ul", ["Capacité · deux adultes · pas d'enfants", "Wifi · fibre 1 Gbit/s · aucune réception 4G au niveau souterrain", "Climatisation · indépendante, température constante 20 °C même l'été", "Baignoire · en pierre travertin · forme de citerne", "Expérience nocturne · sur réservation, ouverture de la lucarne avec observatoire astronomique du borgo"]),
                ("p", "La Cisterna n'est disponible que sur demande directe · particulièrement conseillée pour les lunes de miel et les anniversaires. Séjour minimum de quatre nuits."),
            ],
        },
        {
            "slug":         "suite-la-torre",
            "image":        _SUITE_TORRE,
            "kicker":       "Suite 05",
            "title":        "La Torre",
            "date":         "Saison 2026 · avril – octobre",
            "author":       "Borgo San Marco",
            "read_min":     "70 m²",
            "lede":
                "Suite aménagée dans la tour d'angle médiévale · deuxième étage · "
                "vue à 270° sur le Val d'Orcia jusqu'au Monte Amiata · lit double "
                "avec bureau attenant.",
            "footer_strap": "Disponible avril – octobre · vue 270°",
            "meta_rows": [
                ("Étage",         "Deuxième étage · tour d'angle"),
                ("Lits",          "Lit double + bureau avec canapé-lit"),
                ("Surface",       "70 m² + 6 m² de bureau"),
                ("Vue",           "270° · Val d'Orcia · Monte Amiata · Pienza"),
                ("Salle de bain", "Marbre noir · douche walk-in"),
                ("Inclusions",    "Petit-déjeuner · spa · cave · lunette astronomique"),
                ("Saisonnalité",  "Avril – octobre · escalier 23 marches"),
            ],
            "body": [
                ("p", "La Torre occupe le deuxième étage de la tour d'angle médiévale du borgo · vue à 270° sur le Val d'Orcia (sud-ouest), sur Pienza (nord-ouest) et jusqu'au Monte Amiata (sud-est) par temps clair. Trois fenêtres d'origine du XVIe siècle aux vitres au plomb restaurées."),
                ("p", "Le bureau attenant de 6 m² est meublé d'une écritoire en noyer du Pratomagno et d'une bibliothèque de volumes sur le Val d'Orcia (en italien et en anglais) · idéal pour qui a besoin d'une demi-journée de travail pendant le séjour."),
                ("h3", "La lunette astronomique"),
                ("p", "La tour est équipée d'une petite lunette astronomique Bresser 90 mm installée à la hauteur de la fenêtre ouest · idéale pour observer les constellations du Val d'Orcia (pollution lumineuse nulle). Manuel d'utilisation dans le tiroir · accompagnement du soir avec le référent de salle sur réservation."),
                ("ul", ["Capacité · deux adultes + un enfant sur le canapé-lit du bureau", "Escalier · 23 marches · pas d'ascenseur dans la tour", "Wifi · fibre 1 Gbit/s", "Climatisation · ventilateur de plafond + appareil indépendant", "Lunette · Bresser 90 mm + manuel + accompagnement sur demande"]),
                ("p", "La Torre est disponible d'avril à octobre. Séjour minimum de deux nuits."),
            ],
        },
        {
            "slug":         "suite-il-cortile",
            "image":        _SUITE_CORTILE,
            "kicker":       "Suite 06",
            "title":        "Il Cortile",
            "date":         "Saison 2026 · mai – octobre",
            "author":       "Borgo San Marco",
            "read_min":     "65 m²",
            "lede":
                "Suite avec loggia privée sur la pergola de glycine · rez-de-chaussée "
                "de l'aile nord · jardin privé de 18 m² avec table et fauteuils.",
            "footer_strap": "Disponible mai – octobre · jardin + pergola",
            "meta_rows": [
                ("Étage",         "Rez-de-chaussée · aile nord"),
                ("Lits",          "Lit double + canapé-lit"),
                ("Surface",       "65 m² + jardin privé 18 m²"),
                ("Vue",           "Pergola de glycine · jardin privé"),
                ("Salle de bain", "Marbre travertin · douche walk-in"),
                ("Inclusions",    "Petit-déjeuner · spa · cave · jardin privé"),
                ("Saisonnalité",  "Mai – octobre · glycine en fleur mai-juin"),
            ],
            "body": [
                ("p", "Il Cortile possède l'accès le plus direct à la pergola de glycine, âme du borgo · la glycine a été plantée en 1924 par la famille Buonsignori, pleine floraison sur les trois premières semaines de mai. Jardin privé de 18 m² délimité par un muret en pierre serena · meublé de deux fauteuils en fer forgé et d'une table en pierre."),
                ("p", "Le petit-déjeuner sous la pergola est une pratique de la maison · chaque matin de 8 h à 10 h 30 la pergola se transforme en petite cour de petit-déjeuner · les hôtes assis à des tables basses, la brigade de salle en passage continu · pain de Lorenzini chaud du four du borgo, confitures d'églantine de la direction, fromages de Castelmuzio, fruits des domaines voisins."),
                ("h3", "La glycine de 1924"),
                ("p", "La glycine a été plantée en 1924 par Caterina Buonsignori (1902-1989, dernière de la famille d'origine du borgo) en présent de noces pour sa fille Anna. Elle a depuis grandi jusqu'à couvrir l'intégralité de la pergola de la cour. La pleine floraison dure trois semaines · première décade de mai jusqu'au 25 mai environ."),
                ("ul", ["Capacité · deux adultes + un enfant sur le canapé-lit", "Jardin privé · 18 m² · muret en pierre serena · meublé", "Wifi · fibre 1 Gbit/s", "Climatisation · indépendante", "Petit-déjeuner · servi sous la pergola de glycine 8 h – 10 h 30"]),
                ("p", "Il Cortile est disponible de mai à octobre. Pour admirer la glycine en fleur, réservez dans la première quinzaine de mai."),
            ],
        },
        {
            "slug":         "suite-la-loggia",
            "image":        _SUITE_LOGGIA,
            "kicker":       "Suite 07",
            "title":        "La Loggia",
            "date":         "Saison 2026 · avril – octobre",
            "author":       "Borgo San Marco",
            "read_min":     "82 m²",
            "lede":
                "Suite de l'étage noble · loggia Renaissance ouverte sur Pienza · "
                "plafond à caissons peints de 1671 · lit king-size + bureau + salle "
                "de bain de maître.",
            "footer_strap": "Disponible avril – octobre · étage noble",
            "meta_rows": [
                ("Étage",         "Premier étage noble · aile ouest"),
                ("Lits",          "Lit king-size + bureau"),
                ("Surface",       "82 m² + loggia 14 m²"),
                ("Vue",           "Pienza · cathédrale · Palazzo Piccolomini"),
                ("Salle de bain", "Marbre travertin + statuaire · baignoire + douche séparée"),
                ("Inclusions",    "Petit-déjeuner · spa · cave · dîner privé en loggia sur demande"),
                ("Saisonnalité",  "Avril – octobre · cérémonie civile en loggia possible"),
            ],
            "body": [
                ("p", "La Loggia est la suite de l'étage noble · 82 m² auxquels s'ajoute une loggia Renaissance de 14 m² ouverte sur Pienza · on aperçoit la cathédrale de Bernardo Rossellino de 1462 et le Palazzo Piccolomini. Le plafond à caissons peints de 1671 a été restauré en 2009 par Mauro Pellegrini, restaurateur de Sienne."),
                ("p", "La loggia est le lieu de la cérémonie civile pour les mariages intimes du borgo (36 invités au maximum). Sur demande, il est possible d'organiser un dîner privé en loggia pour les hôtes de la suite · service du chef Tommaso · tarif sur demande."),
                ("h3", "Le plafond à caissons de 1671"),
                ("p", "Le plafond a été commandé par Pietro Buonsignori en 1671 au peintre Domenico Manetti de Sienne (1609-1683). Trente caissons peints à tempera : vues du Val d'Orcia, symboles héraldiques de la famille, putti vendangeurs. La restauration de 2009 a fait ressortir les couleurs d'origine ; les dorures ont été authentifiées en laboratoire."),
                ("ul", ["Capacité · deux adultes + un enfant sur le canapé-lit du bureau", "Loggia · 14 m² ouverte sur Pienza · meublée · dîner privé sur demande", "Wifi · fibre 1 Gbit/s", "Climatisation · double zone", "Cérémonie civile · en loggia · 36 invités au maximum · sur demande"]),
                ("p", "La Loggia est disponible d'avril à octobre. Séjour minimum de deux nuits, trois nuits pour la fenêtre de cérémonie civile."),
            ],
        },
        {
            "slug":         "suite-la-cantina",
            "image":        _SUITE_CANTINA,
            "kicker":       "Suite 08",
            "title":        "La Cantina",
            "date":         "Saison 2026 · sur demande",
            "author":       "Borgo San Marco",
            "read_min":     "92 m²",
            "lede":
                "Suite aménagée dans l'ancienne cave du XVIIIe siècle (la cave "
                "opérationnelle est aujourd'hui à la Fattoria Trebbio) · niveau "
                "souterrain · lit double + coin salon + cave privée de 12 références.",
            "footer_strap": "Sur demande · idéal pour les amateurs de vin",
            "meta_rows": [
                ("Étage",         "Niveau souterrain (–1) · aile sud"),
                ("Lits",          "Lit king-size + coin salon"),
                ("Surface",       "92 m² · voûte à 3,8 m"),
                ("Vue",           "Cave privée vitrée · aucune ouverture extérieure"),
                ("Salle de bain", "Pierre travertin · douche walk-in panoramique sur la cave"),
                ("Inclusions",    "Petit-déjeuner · spa · 12 références dans la cave privée · dégustation guidée"),
                ("Saisonnalité",  "Sur demande · idéal en automne"),
            ],
            "body": [
                ("p", "La Cantina est aménagée dans l'ancienne cave du borgo · niveau souterrain, voûte à 3,8 mètres · elle fut cave opérationnelle jusqu'en 2007, année où le vin de la Fattoria Trebbio a été transféré dans la cave moderne située à 1,2 km. La suite conserve la cave privée vitrée, garnie chaque saison de 12 références de la maison sélectionnées par la sommelière Anna."),
                ("p", "La cave est incluse dans le séjour · les 12 bouteilles sont à la disposition des hôtes pour dégustation illimitée durant le séjour. La dégustation guidée d'Anna est prévue une soirée par séjour (comprise dans le tarif) · dégustations supplémentaires sur demande."),
                ("h3", "Les 12 références de la saison"),
                ("p", "La cave change de composition à chaque saison. La sélection 2026 (signée Anna Ricci) : 4 Brunello (Fattoria Trebbio 2018, Biondi-Santi 2016, Casanova di Neri 2017, Il Poggione 2018) · 3 Vino Nobile (Avignonesi 2019, Salcheto 2020, Boscarelli 2018) · 2 Chianti Classico (Castello di Ama 2019, Felsina 2018) · 3 vins expérimentaux de la Toscane du sud (Petricci 2020, Gualdo del Re 2021, Salvo 2019)."),
                ("ul", ["Capacité · deux adultes · pas d'enfants", "Cave · 12 références · sélection Anna Ricci AIS · renouvelée chaque saison", "Dégustation guidée · une soirée par séjour (incluse)", "Wifi · fibre 1 Gbit/s · aucune réception 4G", "Climatisation · indépendante, température constante 18 °C"]),
                ("p", "La Cantina est disponible sur demande · idéale à la saison d'automne après les vendanges. Séjour minimum de quatre nuits."),
            ],
        },
    ],
}
