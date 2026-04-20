"""Fiscus — Cabinet d\u2019expertise comptable et fiscale · FR locale content.

Wave 2 Pilot #1 — Phase X.4 (Session 80, 2026-04-20).

Locale français institutionnel · registre Les\u00a0Echos / Agefi, vouvoiement
d\u00e8s la premi\u00e8re ligne, espaces ins\u00e9cables avant `:`, `;`, `?`, `!`
et autour des chevrons «\u00a0 \u00a0», tirets cadratins pour les intervalles
de dates (2003\u20132026), apostrophes typographiques (\u2019) partout.
Domaine s\u00e9mantique d\u00e9plac\u00e9 vers l\u2019expertise-comptable\u00a0:
d\u00e9claration fiscale, bilan comptable, contentieux fiscal, r\u00e9gularisation
spontan\u00e9e. Les r\u00e9f\u00e9rences normatives italiennes (ODCEC,
Commissione Tributaria, Partita IVA, Albo, ravvedimento operoso) sont
conserv\u00e9es entre parenth\u00e8ses apr\u00e8s la traduction pour
pr\u00e9server la tra\u00e7abilit\u00e9 professionnelle. Noms propres
italiens (Ruffini, Balestrieri, Conti, Lomazzi, Prevedini, Kouadio) et
adresse (Via Melzo 14 · 20129 Milano) laiss\u00e9s tels quels. Parit\u00e9
de forme stricte avec FISCUS_CONTENT_IT.
"""
from __future__ import annotations

from typing import Any


FISCUS_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Cabinet",         "kind": "home"},
        {"slug": "lo-studio",     "label": "Le cabinet",      "kind": "about"},
        {"slug": "competenze",    "label": "Comp\u00e9tences", "kind": "services"},
        {"slug": "casi-seguiti",  "label": "Dossiers suivis", "kind": "case_study_list"},
        {"slug": "contatti",      "label": "Contact",         "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial": "F",
        "logo_word":    "Fiscus",
        "tag":          "Cabinet d\u2019expertise comptable et fiscale · Milan · inscrit \u00e0 l\u2019ODCEC depuis 2003",
        "phone":        "+39 02 4951 3388",
        "email":        "segreteria@fiscusstudio.it",
        "address":      "Via Melzo 14 · 20129 Milano",
        "hours_compact": "Lun.\u00a0\u2013 Ven. · 9\u00a0h\u00a0\u2013 18\u00a0h\u00a030 · sur rendez-vous",
        "hours_footer_rows": [
            "Samedi · sur rendez-vous \u00e0 l\u2019approche des \u00e9ch\u00e9ances",
            "Dimanche · ferm\u00e9",
        ],
        "license":      "Inscrits \u00e0 l\u2019ODCEC de Milan · Section A · depuis 2003",
        "footer_intro":
            "Cabinet d\u2019expertise comptable et fiscale ind\u00e9pendant au service "
            "des num\u00e9ros de TVA (Partita IVA), des PME et des familles "
            "entrepreneuriales. D\u00e9claration de revenus, comptes annuels, "
            "contentieux fiscal et ing\u00e9nierie fiscale pluriannuelle. "
            "Si\u00e8ge \u00e0 Milan, relation de conseil r\u00e9currente \u2014 "
            "jamais de prestations ponctuelles.",
        "foot_studio":   "Le cabinet",
        "foot_pages":    "Sections",
        "foot_contact":  "Contact",
        "foot_offices":  "Si\u00e8ge",
        "offices_footer_rows": [
            "Milan · Porta Venezia",
        ],
        # Case study cross-page meta labels
        "case_practice_label":     "Domaine",
        "case_year_label":         "Ann\u00e9e",
        "case_duration_label":     "Dur\u00e9e",
        "case_lead_label":         "R\u00e9f\u00e9rent",
        "case_lead_partner_label": "R\u00e9f\u00e9rent",
        "case_team_label":         "\u00c9quipe & calendrier",
        "case_timeline_label":     "Calendrier",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Cabinet d\u2019expertise comptable et fiscale · Milan · inscrit \u00e0 l\u2019ODCEC depuis 2003",
        "headline":    "L\u2019application <em>correcte</em> de la norme, jamais l\u2019artifice.",
        "intro":
            "Cabinet d\u2019expertise comptable et fiscale au service des num\u00e9ros "
            "de TVA, des PME et des familles entrepreneuriales. D\u00e9claration de "
            "revenus, comptes annuels, contentieux fiscal et ing\u00e9nierie fiscale "
            "pluriannuelle \u2014 sans promesse d\u2019\u00e9conomie d\u2019imp\u00f4t, "
            "le calendrier des \u00e9ch\u00e9ances \u00e0 la main.",
        "primary_cta":   "Premier rendez-vous",
        "primary_href":  "contatti",
        "secondary_cta": "T\u00e9l\u00e9charger le calendrier des \u00e9ch\u00e9ances",
        "secondary_href":"lo-studio",

        # Right-hand hero photo + credit overlay (fiscal-desk direction)
        "hero_image":              "https://images.pexels.com/photos/8927688/pexels-photo-8927688.jpeg?auto=compress&cs=tinysrgb&w=1600",
        "hero_image_credit_left":  ("Direction",        "Dr A. Ruffini"),
        "hero_image_credit_right": ("Ann\u00e9e de fondation", "2003"),
        "hero_meta_strip": [
            ("Si\u00e8ge",           "Milan · Porta Venezia"),
            ("Ordre ODCEC",          "4 inscrits · depuis 2003"),
            ("Clients actifs",       "260 num\u00e9ros de TVA"),
        ],

        # Advisory pillars — three practice areas on home
        "pillars_label":   "Domaines de comp\u00e9tence",
        "pillars_heading": "Trois pratiques, une seule signature",
        "pillars_intro":
            "Une seule \u00e9quipe pluridisciplinaire accompagne chaque client. "
            "L\u2019expert-comptable inscrit \u00e0 l\u2019ordre n\u2019est pas un "
            "co\u00fbt \u00e0 minimiser\u00a0: c\u2019est un rempart \u00e0 choisir.",
        "pillars": [
            ("01", "D\u00e9claration & comptes annuels",
             "D\u00e9claration de revenus, annexe RW pour les avoirs \u00e9trangers, "
             "certification unique (Certificazione Unica), comptes annuels (bilan "
             "et compte de r\u00e9sultat) \u2014 audit-ready, avec un calendrier "
             "de revue arr\u00eat\u00e9 en janvier et la signature d\u00e9pos\u00e9e "
             "avant les \u00e9ch\u00e9ances de l\u2019Agenzia Entrate."),
            ("02", "Contentieux fiscal",
             "Assistance en mati\u00e8re de redressement fiscal, r\u00e9gularisation "
             "spontan\u00e9e (ravvedimento operoso), recours devant la Commission "
             "fiscale provinciale et r\u00e9gionale (Commissione Tributaria). Jamais "
             "de promesse de r\u00e9sultat, toujours une estimation pr\u00e9liminaire "
             "des probabilit\u00e9s \u2014 par \u00e9crit, sur papier \u00e0 en-t\u00eate, "
             "avant tout mandat."),
            ("03", "Patrimoine & transmission g\u00e9n\u00e9rationnelle",
             "Ing\u00e9nierie fiscale pluriannuelle, holding familiale, succession "
             "et donation \u2014 pour les patrimoines priv\u00e9s de moyen \u00e0 "
             "haut de gamme et les familles entrepreneuriales qui pr\u00e9parent "
             "la transmission \u00e0 un horizon de 5 \u00e0 10 ans."),
        ],

        # KPI strip — document the studio's continuity track record
        "kpi_heading": "Vingt-deux ann\u00e9es de pratique continue",
        "kpi_strip": [
            ("22",                       "ans depuis la fondation"),
            ("260",                      "num\u00e9ros de TVA en portefeuille"),
            ("\u20ac\u00a0180\u00a0M",   "chiffre d\u2019affaires clients agr\u00e9g\u00e9"),
            ("0",                        "sanction impr\u00e9vue en 2025"),
        ],

        # Sectors ribbon — the client base
        "sectors_label": "Secteurs de la client\u00e8le",
        "sectors": [
            "Num\u00e9ros de TVA & ind\u00e9pendants",
            "PME manufacturi\u00e8res",
            "Cabinets lib\u00e9raux",
            "Patrimoine priv\u00e9",
            "Immobilier",
        ],

        # Trust band — anonymized client categories (commercialisti don't
        # disclose client logos per secreto professionale)
        "trust_label":   "Ils confient leur fiscalit\u00e9 \u00e0 Fiscus",
        "trust_logos":   [
            "NUM\u00c9ROS DE TVA INDIVIDUELS",
            "CABINETS DE CONSEIL",
            "PME MANUFACTURI\u00c8RES",
            "FAMILLES ENTREPRENEURIALES",
            "SOCI\u00c9T\u00c9S IMMOBILI\u00c8RES PRIV\u00c9ES",
            "PROFESSIONNELS INSCRITS \u00c0 UN ORDRE",
        ],

        # Leadership preview — 3 partners on home
        "leadership_label":   "Direction",
        "leadership_heading": "Les experts-comptables qui si\u00e9geront \u00e0 votre table",
        "leadership_intro":
            "Chaque client est suivi personnellement par au moins un associ\u00e9 "
            "inscrit \u00e0 l\u2019ODCEC. Aucune d\u00e9l\u00e9gation \u00e0 un "
            "junior, aucune rotation silencieuse \u2014 le r\u00e9f\u00e9rent "
            "rencontr\u00e9 lors de la premi\u00e8re visite signe les d\u00e9clarations "
            "et r\u00e9pond des diligences.",
        "leadership": [
            {
                "name":  "Dr Andrea Ruffini",
                "role":  "Associ\u00e9 fondateur · D\u00e9claration & comptes annuels",
                "bio":
                    "Expert-comptable inscrit \u00e0 l\u2019ODCEC de Milan depuis "
                    "1999, section\u00a0A. Auditeur l\u00e9gal inscrit au Registre "
                    "des R\u00e9viseurs L\u00e9gaux (Registro dei Revisori Legali) "
                    "depuis 2004. Expert-comptable dipl\u00f4m\u00e9, sp\u00e9cialis\u00e9 "
                    "en fiscalit\u00e9 d\u2019entreprise et comptes annuels. A fond\u00e9 "
                    "le cabinet en 2003 avec la Dr Balestrieri.",
                "credentials": [
                    "ODCEC Milan n.\u00a04488/A (depuis 1999)",
                    "Auditeur l\u00e9gal n.\u00a0137952 (depuis 2004)",
                    "Universit\u00e9 Bocconi \u2014 CLEA\u00a0\u201996",
                ],
            },
            {
                "name":  "Dr Ilaria Balestrieri",
                "role":  "Associ\u00e9e · Contentieux fiscal",
                "bio":
                    "Expert-comptable inscrite \u00e0 l\u2019ODCEC de Milan depuis "
                    "2001, section\u00a0A. Avocate habilit\u00e9e \u00e0 plaider "
                    "devant la Cour de cassation, inscrite au Barreau de Milan "
                    "depuis 2010, sp\u00e9cialis\u00e9e en contentieux fiscal. "
                    "Plaide devant les Commissions fiscales provinciales et "
                    "r\u00e9gionales de Lombardie et du Pi\u00e9mont.",
                "credentials": [
                    "ODCEC Milan n.\u00a05611/A (depuis 2001)",
                    "Barreau de Milan (depuis 2010)",
                    "Habilit\u00e9e en cassation depuis 2018",
                ],
            },
            {
                "name":  "Dr Stefano Conti",
                "role":  "Associ\u00e9 · Patrimoine & transmission g\u00e9n\u00e9rationnelle",
                "bio":
                    "Expert-comptable inscrit \u00e0 l\u2019ODCEC de Milan depuis "
                    "2008, section\u00a0A. Sp\u00e9cialiste de la planification "
                    "patrimoniale pour les familles entrepreneuriales \u2014 "
                    "holding, trust, succession. Entr\u00e9 au cabinet en 2014, "
                    "associ\u00e9 depuis 2019. Charg\u00e9 d\u2019enseignement "
                    "en fiscalit\u00e9 internationale \u00e0 la LIUC Castellanza.",
                "credentials": [
                    "ODCEC Milan n.\u00a07912/A (depuis 2008)",
                    "LL.M. Droit fiscal Bocconi",
                    "TEP · Society of Trust and Estate Practitioners",
                ],
            },
        ],

        # Case studies preview — three recent mandates on home
        "cases_label":   "Dossiers suivis",
        "cases_heading": "Trois dossiers, trois domaines de comp\u00e9tence",
        "cases_intro":
            "Une s\u00e9lection r\u00e9cente de clients suivis au cours des trois "
            "derni\u00e8res ann\u00e9es. Par secret professionnel, les noms sont "
            "remplac\u00e9s par un code sectoriel, mais les chiffres sont "
            "v\u00e9rifiables lors d\u2019un entretien de r\u00e9f\u00e9rence.",

        # Final CTA band before footer — appointment-focused
        "cta_label":     "Premier rendez-vous",
        "cta_heading":   "Quarante-cinq minutes, ordre du jour ouvert, sans engagement",
        "cta_intro":
            "La premi\u00e8re visite se tient avec un associ\u00e9 inscrit \u00e0 "
            "l\u2019ODCEC. Nous discutons du domaine de comp\u00e9tence, de "
            "l\u2019horizon temporel de la relation et des honoraires indicatifs "
            "\u2014 avant tout mandat sign\u00e9. Les clients existants prennent "
            "rendez-vous dans l\u2019espace r\u00e9serv\u00e9.",
        "cta_primary":   "Demander un rendez-vous",
        "cta_primary_href": "contatti",
        "cta_secondary": "T\u00e9l\u00e9charger le calendrier des \u00e9ch\u00e9ances",
        "cta_secondary_href": "lo-studio",
    },

    # ─── LO STUDIO (about + values + team + history) ────────────
    "lo-studio": {
        "eyebrow":   "Le cabinet · 2003\u20132026",
        "headline":  "Un cabinet d\u2019expertise comptable et fiscale <em>ind\u00e9pendant</em>, vingt-deux ann\u00e9es de pratique continue.",
        "intro":
            "Fiscus na\u00eet \u00e0 Milan en 2003 de la rencontre entre Andrea "
            "Ruffini et Ilaria Balestrieri \u2014 deux experts-comptables "
            "inscrits \u00e0 l\u2019ODCEC, form\u00e9s \u00e0 la fiscalit\u00e9 "
            "d\u2019entreprise et au contentieux fiscal. Nous avons grandi "
            "par cooptation, jamais par acquisition, et avons pr\u00e9serv\u00e9 "
            "notre ind\u00e9pendance \u00e0 l\u2019\u00e9gard de tout capital tiers.",

        # Studio history — 5-step timeline
        "history_label":   "Histoire du cabinet",
        "history_heading": "Cinq \u00e9tapes, vingt-deux ann\u00e9es",
        "history_intro":
            "Cinq dates qui ont d\u00e9fini Fiscus. Chacune refl\u00e8te un "
            "choix structurel \u2014 d\u2019ind\u00e9pendance, de sp\u00e9cialisation, "
            "de p\u00e9rim\u00e8tre \u2014 qui oriente aujourd\u2019hui encore "
            "la mani\u00e8re dont nous acceptons nos nouveaux clients.",
        "history": [
            ("2003", "Fondation",
             "Andrea Ruffini et Ilaria Balestrieri ouvrent Fiscus via Melzo, "
             "avec douze clients d\u00e9j\u00e0 en portefeuille \u2014 tous "
             "repris du cabinet pr\u00e9c\u00e9dent avec l\u2019accord "
             "expr\u00e8s des clients eux-m\u00eames."),
            ("2008", "Pratique contentieux fiscal",
             "L\u2019inscription d\u2019Ilaria Balestrieri au Barreau ouvre "
             "la pratique contentieux\u00a0: recours devant CTP/CTR, redressements, "
             "r\u00e9gularisation spontan\u00e9e. Premi\u00e8re audience devant "
             "la CTP de Milan en mars 2009."),
            ("2014", "Arriv\u00e9e du Dr Conti",
             "Stefano Conti rejoint le cabinet comme associ\u00e9 pour constituer "
             "la pratique patrimoine \u2014 holding familiale, trust, transmission "
             "g\u00e9n\u00e9rationnelle. Associ\u00e9 depuis 2019 apr\u00e8s cinq "
             "ans d\u2019accompagnement."),
            ("2020", "Num\u00e9risation de la d\u00e9claration",
             "Int\u00e9gration compl\u00e8te avec l\u2019Agenzia Entrate via "
             "Entratel et facturation \u00e9lectronique. Archive documentaire "
             "chiffr\u00e9e avec r\u00e9tention d\u00e9cennale et acc\u00e8s "
             "client via un espace r\u00e9serv\u00e9."),
            ("2024", "Pratique audit l\u00e9gal",
             "Andrea Ruffini formalise la pratique d\u2019audit l\u00e9gal pour "
             "les PME soumises \u00e0 l\u2019obligation de coll\u00e8ge des "
             "commissaires. Trois mandats d\u2019audit actifs avant d\u00e9cembre 2024."),
        ],

        # Method / values — 4 principi
        "values_label":   "M\u00e9thode",
        "values_heading": "Quatre principes <em>non n\u00e9gociables</em>",
        "values_intro":
            "Les quatre r\u00e8gles qui distinguent un client Fiscus d\u2019une "
            "relation de conseil ordinaire. Elles sont inscrites sur papier "
            "\u00e0 en-t\u00eate dans le mandat \u2014 pas seulement sur cette page.",
        "values": [
            ("01", "Ind\u00e9pendance du capital",
             "Le capital du cabinet est int\u00e9gralement d\u00e9tenu par les "
             "associ\u00e9s actifs. Aucun apport de groupe, aucun fonds en "
             "minoritaire, aucun actionnaire ext\u00e9rieur. Le choix des "
             "clients n\u2019est jamais influenc\u00e9 par l\u2019agenda de "
             "tiers \u2014 et les clients historiques savent que la relation "
             "ne change pas de couleur parce qu\u2019un associ\u00e9 a chang\u00e9."),
            ("02", "Un associ\u00e9 par client",
             "Chaque client a un associ\u00e9 r\u00e9f\u00e9rent inscrit \u00e0 "
             "l\u2019ODCEC qui suit personnellement le dossier de l\u2019ouverture "
             "\u00e0 la signature des d\u00e9clarations. L\u2019associ\u00e9 "
             "rencontr\u00e9 lors de la premi\u00e8re visite r\u00e9pond des "
             "diligences \u2014 pas de d\u00e9l\u00e9gations silencieuses, "
             "pas de rotations en fin d\u2019ann\u00e9e."),
            ("03", "Aucune promesse d\u2019\u00e9conomie d\u2019imp\u00f4t",
             "Nous ne signons pas de devis assortis de promesses de r\u00e9duction "
             "fiscale en pourcentage\u00a0: c\u2019est contraire au code "
             "d\u00e9ontologique de l\u2019ODCEC, et c\u2019est le sympt\u00f4me "
             "d\u2019une relation opportuniste. Notre m\u00e9tier consiste "
             "\u00e0 appliquer la norme correctement et \u00e0 signaler les "
             "dispositifs incitatifs lorsqu\u2019ils existent."),
            ("04", "Honoraires forfaitaires transparents",
             "Tarif annuel arr\u00eat\u00e9 en d\u00e9cembre pour l\u2019ann\u00e9e "
             "suivante, r\u00e9vis\u00e9 uniquement en cas de variation objective "
             "du p\u00e9rim\u00e8tre (nouveau si\u00e8ge, nouveau num\u00e9ro de "
             "TVA, nouvelle branche d\u2019activit\u00e9). Aucune facturation "
             "\u00e0 l\u2019usage dissimul\u00e9e, aucune r\u00e9trocession "
             "de commission."),
        ],

        # Full team — 3 soci + 4 collaboratori iscritti albo o praticanti
        "team_label":   "\u00c9quipe",
        "team_heading": "Trois associ\u00e9s, quatre collaborateurs, une seule gouvernance",
        "team_intro":
            "Les personnes qui suivront votre mandat. Chaque d\u00e9claration "
            "est sign\u00e9e par un associ\u00e9 \u2014 les collaborateurs "
            "appuient sur la collecte des donn\u00e9es, la v\u00e9rification "
            "pr\u00e9liminaire et la gestion documentaire.",
        "team": [
            {"name": "Dr Andrea Ruffini",
             "role": "Associ\u00e9 fondateur · D\u00e9claration & comptes annuels · Auditeur l\u00e9gal",
             "office": "Milan",
             "bio": "Expert-comptable inscrit \u00e0 l\u2019ODCEC depuis 1999 + "
                    "auditeur l\u00e9gal depuis 2004. Bocconi CLEA\u00a0\u201996. "
                    "Fondateur du cabinet."},
            {"name": "Dr Ilaria Balestrieri",
             "role": "Associ\u00e9e · Contentieux fiscal · Habilit\u00e9e en cassation",
             "office": "Milan",
             "bio": "Expert-comptable inscrite \u00e0 l\u2019ODCEC depuis 2001 + "
                    "avocate habilit\u00e9e en cassation depuis 2018. Plaide "
                    "en Lombardie et au Pi\u00e9mont."},
            {"name": "Dr Stefano Conti",
             "role": "Associ\u00e9 · Patrimoine & transmission g\u00e9n\u00e9rationnelle · Enseignant LIUC",
             "office": "Milan",
             "bio": "Expert-comptable inscrit \u00e0 l\u2019ODCEC depuis 2008. "
                    "LL.M. Droit fiscal Bocconi. TEP depuis 2021."},
            {"name": "Dr Serena Lomazzi",
             "role": "Collaboratrice · D\u00e9clarations personnes physiques",
             "office": "Milan",
             "bio": "Expert-comptable inscrite \u00e0 l\u2019ODCEC depuis 2017. "
                    "Coordonne la collecte des donn\u00e9es et la saisie des "
                    "d\u00e9clarations 730 et RPF."},
            {"name": "Dr Giacomo Prevedini",
             "role": "Collaborateur · Comptes annuels PME · Stagiaire audit",
             "office": "Milan",
             "bio": "Expert-comptable inscrit \u00e0 l\u2019ODCEC depuis 2021. "
                    "Suit la comptabilit\u00e9 ordinaire et la cl\u00f4ture "
                    "des comptes pour les PME manufacturi\u00e8res du "
                    "portefeuille."},
            {"name": "Mme Nadia Kouadio",
             "role": "Responsable comptabilit\u00e9 · Paie & charges sociales",
             "office": "Milan",
             "bio": "Comptable inscrite \u00e0 l\u2019Ordre des Consultants du "
                    "Travail (Consulenti del Lavoro) depuis 2012. G\u00e8re "
                    "la paie en collaboration avec un consultant du travail "
                    "externe, et la comptabilit\u00e9 ordinaire."},
        ],

        # Coordinates strip
        "coordinates_label": "Si\u00e8ge",
        "coordinates": [
            ("Milan", "Via Melzo 14 · 20129 · Porta Venezia \u2014 \u00e0 200\u00a0m\u00e8tres de la station MM Porta Venezia"),
        ],

        # Page-level CTA
        "cta_heading": "Un premier entretien exploratoire",
        "cta_intro":
            "Les quarante-cinq premi\u00e8res minutes avec un associ\u00e9 "
            "sont une conversation exploratoire, non une proposition commerciale. "
            "On y discute du domaine de comp\u00e9tence, de l\u2019horizon "
            "temporel et des honoraires indicatifs. Au terme de l\u2019entretien, "
            "vous \u00eates libres de choisir un autre cabinet \u2014 et "
            "d\u2019emporter avec vous l\u2019ensemble de la documentation "
            "pr\u00e9liminaire.",
        "cta_primary":  "Demander un rendez-vous",
        "cta_primary_href": "contatti",
    },

    # ─── COMPETENZE (services) ──────────────────────────────────
    "competenze": {
        "eyebrow":  "Domaines de comp\u00e9tence · 2026",
        "headline": "Six domaines de comp\u00e9tence, <em>une seule signature</em>.",
        "intro":
            "Les six domaines de pratique de Fiscus. Chaque client acc\u00e8de "
            "\u00e0 l\u2019\u00e9quipe pluridisciplinaire \u2014 vous ne payez "
            "pas chaque domaine s\u00e9par\u00e9ment, les honoraires annuels "
            "couvrent la combinaison de comp\u00e9tences n\u00e9cessaires au "
            "mandat.",

        # Card meta labels
        "svc_duration_label": "Dur\u00e9e type",
        "svc_leader_label":   "Associ\u00e9 r\u00e9f\u00e9rent",

        # 6 areas in airy cards
        "services": [
            {
                "num":   "01",
                "title": "D\u00e9claration de revenus & fiscalit\u00e9 ordinaire",
                "blurb":
                    "D\u00e9claration de revenus (Modello Redditi PF · SP · SC · ENC), "
                    "formulaire 730, annexe RW pour les avoirs \u00e9trangers, "
                    "certification unique. Nous travaillons sur un calendrier "
                    "arr\u00eat\u00e9 en janvier, avec des \u00e9ch\u00e9ances "
                    "internes 30\u00a0jours avant celles de l\u2019Agenzia Entrate "
                    "\u2014 parce qu\u2019une d\u00e9claration sign\u00e9e le "
                    "30 septembre vaut mieux qu\u2019une le 30 novembre.",
                "scope": [
                    "Modello Redditi PF / SP / SC / ENC",
                    "Formulaire 730 pour salari\u00e9s et retrait\u00e9s",
                    "Annexe RW \u2014 suivi fiscal des avoirs \u00e9trangers",
                    "Certification unique pour les collecteurs d\u2019imp\u00f4t \u00e0 la source",
                    "R\u00e9gularisation spontan\u00e9e (ravvedimento operoso) pour d\u00e9clarations rectificatives",
                ],
                "duration": "Relation annuelle r\u00e9currente",
                "leader":   "Dr Andrea Ruffini",
            },
            {
                "num":   "02",
                "title": "Comptes annuels & comptabilit\u00e9 ordinaire",
                "blurb":
                    "Comptabilit\u00e9 ordinaire, comptes annuels CEE (bilan et "
                    "compte de r\u00e9sultat), annexe, rapport de gestion, "
                    "proc\u00e8s-verbal d\u2019assembl\u00e9e. Pour les PME dot\u00e9es "
                    "d\u2019un coll\u00e8ge des commissaires, nous pr\u00e9parons "
                    "\u00e9galement la documentation destin\u00e9e \u00e0 l\u2019auditeur "
                    "l\u00e9gal \u2014 audit-ready avant mars, publication \u00e0 la "
                    "Chambre de commerce avant mai.",
                "scope": [
                    "Comptabilit\u00e9 ordinaire et simplifi\u00e9e",
                    "Comptes annuels CEE + annexe",
                    "D\u00e9p\u00f4t des comptes \u00e0 la Chambre de commerce",
                    "Rapport de gestion pour soci\u00e9t\u00e9s de capitaux",
                    "Assistance au coll\u00e8ge des commissaires et \u00e0 l\u2019auditeur externe",
                ],
                "duration": "Relation annuelle r\u00e9currente",
                "leader":   "Dr Andrea Ruffini",
            },
            {
                "num":   "03",
                "title": "Contentieux fiscal",
                "blurb":
                    "Assistance en phase de redressement avec adh\u00e9sion, "
                    "r\u00e9gularisation spontan\u00e9e, recours devant la "
                    "Commission fiscale provinciale et r\u00e9gionale, "
                    "conciliation judiciaire. Plaidoirie en Lombardie et au "
                    "Pi\u00e9mont. Pour chaque dossier, nous fournissons une "
                    "estimation pr\u00e9liminaire des probabilit\u00e9s par "
                    "\u00e9crit, avant tout mandat.",
                "scope": [
                    "Redressement fiscal avec adh\u00e9sion",
                    "R\u00e9gularisation spontan\u00e9e et \u00e9chelonnements",
                    "Recours CTP · CTR · Cassation (avec avocat)",
                    "Conciliation judiciaire",
                    "Demandes de recours gracieux aupr\u00e8s de l\u2019Agenzia Entrate",
                ],
                "duration": "De 3 \u00e0 24 mois selon le degr\u00e9",
                "leader":   "Dr Ilaria Balestrieri",
            },
            {
                "num":   "04",
                "title": "Ing\u00e9nierie fiscale & patrimoine",
                "blurb":
                    "Ing\u00e9nierie fiscale pluriannuelle pour les patrimoines "
                    "priv\u00e9s de moyen \u00e0 haut de gamme et les familles "
                    "entrepreneuriales. Holding familiale, trust, fondations, "
                    "contrats d\u2019assurance fiscalement efficients, "
                    "planification successorale. Toujours avec un horizon de "
                    "5 \u00e0 10\u00a0ans \u2014 jamais avec des promesses "
                    "fiscales annuelles.",
                "scope": [
                    "Holding familiale et pactes d\u2019actionnaires",
                    "Trusts et fondations de famille",
                    "Planification successorale et donation",
                    "Structuration de contrats d\u2019assurance de branche\u00a0IV",
                    "\u00c9valuation des dispositifs incitatifs (PIR, ELTIF)",
                ],
                "duration": "12 \u00e0 36\u00a0mois pour une restructuration",
                "leader":   "Dr Stefano Conti",
            },
            {
                "num":   "05",
                "title": "Paie et conseil social & collecte \u00e0 la source",
                "blurb":
                    "Gestion de la paie, charges sociales, collecteur d\u2019imp\u00f4t "
                    "\u00e0 la source pour PME et cabinets lib\u00e9raux \u2014 en "
                    "collaboration avec un consultant du travail externe "
                    "inscrit \u00e0 l\u2019ordre professionnel des Consulenti del "
                    "Lavoro. Nous couvrons le volet fiscal et comptable\u00a0; "
                    "le consultant du travail couvre le volet droit social et "
                    "pr\u00e9voyance.",
                "scope": [
                    "\u00c9laboration des bulletins de paie et F24 mensuels",
                    "Certification unique du collecteur \u00e0 la source",
                    "Formulaire 770",
                    "Assistance en contr\u00f4le INPS / INAIL / Inspection du travail",
                    "Coordination avec le consultant du travail externe (Mme Kouadio)",
                ],
                "duration": "Relation mensuelle r\u00e9currente",
                "leader":   "Mme Nadia Kouadio · Dr A. Ruffini",
            },
            {
                "num":   "06",
                "title": "Audit l\u00e9gal & coll\u00e8ge des commissaires",
                "blurb":
                    "Audit l\u00e9gal des comptes pour PME soumises \u00e0 "
                    "l\u2019obligation de coll\u00e8ge des commissaires \u2014 "
                    "soci\u00e9t\u00e9s par actions non cot\u00e9es, soci\u00e9t\u00e9s "
                    "\u00e0 responsabilit\u00e9 limit\u00e9e (S.r.l.) d\u00e9passant "
                    "les seuils de l\u2019art.\u00a02477 du Code civil italien. "
                    "Trois mandats actifs actuellement. Nous intervenons toujours "
                    "comme auditeur externe, jamais comme commissaire interne du "
                    "m\u00eame groupe.",
                "scope": [
                    "Rapport d\u2019audit l\u00e9gal ex D.Lgs.\u00a039/2010",
                    "V\u00e9rification trimestrielle des comptes",
                    "Planification ISA Italia de l\u2019audit",
                    "Communication avec le coll\u00e8ge des commissaires interne",
                    "Rapport en assembl\u00e9e des associ\u00e9s",
                ],
                "duration": "Mandat triennal ou nonennal",
                "leader":   "Dr Andrea Ruffini",
            },
        ],

        # Process — how a new client onboarding is run
        "process_label":   "Notre mani\u00e8re de travailler",
        "process_heading": "Quatre \u00e9tapes, une seule s\u00e9quence",
        "process": [
            ("01", "Premier rendez-vous",
             "Quarante-cinq minutes confidentielles avec un associ\u00e9 inscrit "
             "\u00e0 l\u2019ODCEC. On y discute du domaine de comp\u00e9tence, "
             "de l\u2019horizon temporel et des honoraires indicatifs. Aucun "
             "mandat sign\u00e9, aucun co\u00fbt."),
            ("02", "Devis \u00e9crit",
             "Sous sept jours ouvr\u00e9s, un devis de trois pages avec le "
             "p\u00e9rim\u00e8tre du mandat, la liste des diligences, le "
             "calendrier des \u00e9ch\u00e9ances internes et les honoraires "
             "annuels arr\u00eat\u00e9s."),
            ("03", "Ouverture du dossier",
             "Mandat \u00e0 l\u2019Agenzia Entrate via Entratel, transfert de la "
             "documentation depuis le pr\u00e9c\u00e9dent expert-comptable (le "
             "cas \u00e9ch\u00e9ant), ouverture de l\u2019espace client "
             "r\u00e9serv\u00e9 sur l\u2019archive chiffr\u00e9e."),
            ("04", "Relation continue",
             "Un associ\u00e9 r\u00e9f\u00e9rent pour toute la dur\u00e9e de la "
             "relation. \u00c9ch\u00e9ances suivies 30\u00a0jours avant les "
             "dates de l\u2019Agenzia Entrate. Revue annuelle en d\u00e9cembre "
             "pour l\u2019ann\u00e9e suivante."),
        ],

        # Final CTA
        "cta_heading":   "Quel domaine de comp\u00e9tence vous concerne\u00a0?",
        "cta_intro":
            "Si le p\u00e9rim\u00e8tre n\u2019est pas clair, envoyez-nous une "
            "br\u00e8ve description de la situation (type d\u2019entreprise, "
            "ann\u00e9e d\u2019ouverture, \u00e9ventuelles diligences \u00e9chues). "
            "Nous r\u00e9pondons sous 48\u00a0heures ouvr\u00e9es \u2014 m\u00eame "
            "si la r\u00e9ponse est «\u00a0nous ne sommes pas le cabinet qu\u2019il "
            "vous faut\u00a0».",
        "cta_primary":   "\u00c9crivez-nous",
        "cta_primary_href": "contatti",
    },

    # ─── CASI SEGUITI (case-studies list) ───────────────────────
    "casi-seguiti": {
        "eyebrow":  "Dossiers suivis · 2022\u20132026",
        "headline": "Trois dossiers, <em>trois domaines de comp\u00e9tence</em>.",
        "intro":
            "Une s\u00e9lection de dossiers suivis au cours des quatre "
            "derni\u00e8res ann\u00e9es. Les clients sont identifi\u00e9s par "
            "code sectoriel dans le respect du secret professionnel "
            "(art.\u00a0199 c.p.p. italien et Code d\u00e9ontologique ODCEC), "
            "mais les chiffres sont r\u00e9els et v\u00e9rifiables lors d\u2019un "
            "entretien de r\u00e9f\u00e9rence avec le r\u00e9f\u00e9rent interne "
            "du client.",

        "cases_label": "Dossiers",
        "cases_intro":
            "S\u00e9lection \u00e9quilibr\u00e9e sur les trois domaines principaux "
            "\u2014 d\u00e9claration & comptes annuels, contentieux, patrimoine. "
            "La liste compl\u00e8te des dossiers disponibles comme r\u00e9f\u00e9rence "
            "est fournie au format PDF via la page contact.",

        "cta_heading":   "Un dossier comparable au v\u00f4tre\u00a0?",
        "cta_intro":
            "Les dossiers complets (p\u00e9rim\u00e8tre, chiffres agr\u00e9g\u00e9s, "
            "\u00e9ventuel entretien de r\u00e9f\u00e9rence avec le r\u00e9f\u00e9rent "
            "interne du client) sont accessibles apr\u00e8s signature d\u2019un "
            "engagement de confidentialit\u00e9 r\u00e9ciproque. La signature "
            "intervient lors du premier rendez-vous, avant tout engagement "
            "d\u2019honoraires.",
        "cta_primary":   "Demander les dossiers complets",
        "cta_primary_href": "contatti",
    },

    # Posts powering case_study_detail. URL: /casi-seguiti/<slug>/
    "posts": [
        {
            "slug":     "pmi-manifattura-bilancio-revisione",
            "title":    "PME manufacturi\u00e8re lombarde · mise en place de l\u2019audit l\u00e9gal",
            "category": "D\u00e9claration & comptes annuels",
            "year":     "2025",
            "duration": "10\u00a0semaines + mandat triennal",
            "client_code":
                "Industrie manufacturi\u00e8re · Brescia · 42\u00a0salari\u00e9s · "
                "\u20ac\u00a012,4\u00a0M de revenus · S.r.l. avec coll\u00e8ge "
                "des commissaires ex art.\u00a02477",
            "lead":
                "Premier exercice soumis \u00e0 l\u2019audit l\u00e9gal apr\u00e8s "
                "le d\u00e9passement des seuils de l\u2019art.\u00a02477 du Code "
                "civil italien. Le client a confi\u00e9 \u00e0 Fiscus le mandat "
                "d\u2019auditeur externe dans la continuit\u00e9 d\u2019une "
                "relation fiscale ordinaire de longue date.",
            "sections": [
                {
                    "label": "Le probl\u00e8me",
                    "heading": "Passage au coll\u00e8ge des commissaires en cours d\u2019exercice",
                    "body":
                        "La soci\u00e9t\u00e9 a d\u00e9pass\u00e9 pour la deuxi\u00e8me "
                        "ann\u00e9e cons\u00e9cutive les seuils dimensionnels "
                        "pr\u00e9vus par l\u2019art.\u00a02477 du Code civil italien "
                        "(revenus\u00a0> \u20ac\u00a08,8\u00a0M, actif\u00a0> "
                        "\u20ac\u00a04,4\u00a0M, salari\u00e9s\u00a0> 50). Le "
                        "coll\u00e8ge des commissaires a \u00e9t\u00e9 nomm\u00e9 "
                        "en assembl\u00e9e en mars 2025, et il fallait d\u00e9signer "
                        "un auditeur l\u00e9gal externe ex D.Lgs.\u00a039/2010 "
                        "sous trois mois. La soci\u00e9t\u00e9 souhaitait la "
                        "continuit\u00e9 avec le cabinet fiscal historique \u2014 "
                        "\u00e0 condition qu\u2019il n\u2019y ait aucun conflit "
                        "d\u2019int\u00e9r\u00eats sur le plan de l\u2019ind\u00e9pendance.",
                },
                {
                    "label": "L\u2019approche",
                    "heading": "S\u00e9paration des pratiques et planification ISA",
                    "body":
                        "Fiscus a accept\u00e9 le mandat d\u2019audit sous condition "
                        "de s\u00e9gr\u00e9gation op\u00e9rationnelle\u00a0: un "
                        "associ\u00e9 diff\u00e9rent suit la pratique fiscale "
                        "(Dr A. Ruffini) et la pratique audit (Dr I. Balestrieri, "
                        "inscrite au Registre des R\u00e9viseurs depuis 2011). "
                        "Planification de l\u2019audit selon ISA Italia\u00a0315 "
                        "\u2014 \u00e9valuation du syst\u00e8me de contr\u00f4le "
                        "interne, identification des risques significatifs, "
                        "d\u00e9termination du seuil de significativit\u00e9. Le "
                        "plan d\u2019audit a \u00e9t\u00e9 partag\u00e9 avec le "
                        "coll\u00e8ge des commissaires avant ex\u00e9cution.",
                },
                {
                    "label": "Le r\u00e9sultat",
                    "heading": "Rapport d\u2019audit sans r\u00e9serve",
                    "body":
                        "Rapport d\u2019audit ex art.\u00a014 D.Lgs.\u00a039/2010 "
                        "publi\u00e9 en mai 2025 sans r\u00e9serve, sans paragraphe "
                        "d\u2019observation et sans incertitude significative. "
                        "L\u2019audit a mis en \u00e9vidence deux recommandations "
                        "de renforcement du syst\u00e8me de contr\u00f4le interne "
                        "(s\u00e9gr\u00e9gation des t\u00e2ches dans le cycle "
                        "achats, proc\u00e9dure d\u2019inventaire de fin de mois) "
                        "que la soci\u00e9t\u00e9 a mises en \u0153uvre avant "
                        "septembre. Mandat d\u2019audit triennal confirm\u00e9 "
                        "pour les exercices 2025\u20132027.",
                },
            ],
            "kpi": [
                ("0",           "r\u00e9serve dans le rapport d\u2019audit"),
                ("2",           "recommandations mises en \u0153uvre par le client"),
                ("3\u00a0ans",  "dur\u00e9e du mandat d\u2019audit"),
                ("10\u00a0sem.", "de la lettre de mission \u00e0 la signature du rapport"),
            ],
            "lead_partner": "Dr Ilaria Balestrieri (audit) · Dr Andrea Ruffini (fiscal)",
            "team":         "2 associ\u00e9s · 1 senior · 1 stagiaire audit · 10\u00a0semaines",
            "next_label":   "Dossier suivant",
        },
        {
            "slug":     "contenzioso-tributario-accertamento-iva",
            "title":    "Contentieux · redressement TVA sur op\u00e9rations intracommunautaires",
            "category": "Contentieux fiscal",
            "year":     "2024",
            "duration": "14\u00a0mois du redressement \u00e0 l\u2019arr\u00eat de la CTR",
            "client_code":
                "Commerce de gros · C\u00f4me · 18\u00a0salari\u00e9s · "
                "\u20ac\u00a06,2\u00a0M de revenus · redressement Agenzia Entrate "
                "\u20ac\u00a0187\u00a0000 de TVA",
            "lead":
                "Redressement de l\u2019Agenzia Entrate pour op\u00e9rations "
                "intracommunautaires requalifi\u00e9es en cessions internes "
                "ordinaires (pr\u00e9somption de destination nationale). Le "
                "client a confi\u00e9 le dossier \u00e0 Fiscus lors du "
                "contradictoire pr\u00e9-redressement, \u00e0 l\u2019approche "
                "de l\u2019\u00e9ch\u00e9ance d\u2019adh\u00e9sion.",
            "sections": [
                {
                    "label": "Le probl\u00e8me",
                    "heading": "Pr\u00e9somption de facturation nationale sur op\u00e9rations UE",
                    "body":
                        "L\u2019Agenzia Entrate a notifi\u00e9 un avis de "
                        "redressement pour l\u2019ann\u00e9e 2021 avec "
                        "r\u00e9cup\u00e9ration de TVA pour \u20ac\u00a0187\u00a0000, "
                        "p\u00e9nalit\u00e9s de 90\u00a0% et int\u00e9r\u00eats. "
                        "L\u2019administration requalifiait une s\u00e9rie "
                        "d\u2019op\u00e9rations vers un client slovaque en "
                        "cessions internes ordinaires, en consid\u00e9rant que "
                        "les documents de transport ne prouvaient pas de "
                        "mani\u00e8re suffisante la sortie effective de la "
                        "marchandise du territoire italien. Le d\u00e9lai "
                        "d\u2019adh\u00e9sion expirait sous 28\u00a0jours.",
                },
                {
                    "label": "L\u2019approche",
                    "heading": "Contradictoire avec documentation CMR compl\u00e9mentaire",
                    "body":
                        "Fiscus a instruit un contradictoire pr\u00e9-redressement "
                        "en trois semaines. R\u00e9unis\u00a0: 64\u00a0lettres de "
                        "voiture CMR originales tamponn\u00e9es par le destinataire "
                        "UE, relev\u00e9s bancaires des paiements du client "
                        "slovaque issus de sa banque slovaque, v\u00e9rifications "
                        "VIES historiques du client UE, une expertise asserment\u00e9e "
                        "du responsable logistique du client. La documentation a "
                        "\u00e9t\u00e9 d\u00e9pos\u00e9e en contradictoire et, en "
                        "parall\u00e8le, dans le cadre du recours devant la "
                        "Commission fiscale provinciale de C\u00f4me, afin "
                        "d\u2019anticiper l\u2019hypoth\u00e8se d\u2019un rejet "
                        "administratif.",
                },
                {
                    "label": "Le r\u00e9sultat",
                    "heading": "Recours accueilli en CTP et confirm\u00e9 en CTR",
                    "body":
                        "La CTP de C\u00f4me a accueilli int\u00e9gralement le "
                        "recours en juin 2024, annulant l\u2019avis de redressement "
                        "par d\u00e9cision n.\u00a0412/2024. L\u2019Agenzia "
                        "Entrate a interjet\u00e9 appel devant la CTR de "
                        "Lombardie, qui en d\u00e9cembre 2024 a confirm\u00e9 "
                        "la d\u00e9cision de premier degr\u00e9 en rejetant "
                        "l\u2019appel de l\u2019administration. D\u00e9cision "
                        "pass\u00e9e en force de chose jug\u00e9e en janvier 2025. "
                        "Le client a recouvr\u00e9 les d\u00e9pens ex art.\u00a015 "
                        "D.Lgs.\u00a0546/1992 pour \u20ac\u00a014\u00a0200.",
                },
            ],
            "kpi": [
                ("\u20ac\u00a0187\u00a0000", "TVA redress\u00e9e \u2014 totalement annul\u00e9e"),
                ("100\u00a0%",               "d\u00e9pens recouvr\u00e9s ex art.\u00a015"),
                ("2/2",                      "degr\u00e9s de juridiction favorables"),
                ("14\u00a0mois",             "du redressement \u00e0 la force de chose jug\u00e9e"),
            ],
            "lead_partner": "Dr Ilaria Balestrieri",
            "team":         "1 associ\u00e9e habilit\u00e9e en cassation · 1 senior · 14\u00a0mois",
            "next_label":   "Dossier suivant",
        },
        {
            "slug":     "wealth-passaggio-generazionale-holding",
            "title":    "Patrimoine · holding familiale pour transmission g\u00e9n\u00e9rationnelle",
            "category": "Patrimoine & transmission g\u00e9n\u00e9rationnelle",
            "year":     "2025",
            "duration": "20\u00a0mois de la lettre de mission \u00e0 l\u2019ach\u00e8vement",
            "client_code":
                "Famille entrepreneuriale · Varese · patrimoine agr\u00e9g\u00e9 "
                "\u20ac\u00a038\u00a0M (participation dans une PME manufacturi\u00e8re "
                "+ immobilier + liquidit\u00e9s) · deux enfants, tous deux impliqu\u00e9s "
                "dans l\u2019entreprise",
            "lead":
                "Famille entrepreneuriale d\u00e9tenant une participation de "
                "contr\u00f4le dans une PME manufacturi\u00e8re de second rang, "
                "trois immeubles d\u2019exploitation, deux immeubles de prestige "
                "et une liquidit\u00e9 significative. Fondateur de 68\u00a0ans, "
                "deux enfants op\u00e9rationnels dans l\u2019entreprise, \u00e9pouse "
                "non impliqu\u00e9e dans la gestion. Objectif\u00a0: pr\u00e9parer "
                "la transmission g\u00e9n\u00e9rationnelle \u00e0 un horizon de "
                "7 \u00e0 10\u00a0ans.",
            "sections": [
                {
                    "label": "Le probl\u00e8me",
                    "heading": "Patrimoine h\u00e9t\u00e9rog\u00e8ne, deux enfants aux r\u00f4les diff\u00e9rents",
                    "body":
                        "Le fondateur avait trois pr\u00e9occupations concr\u00e8tes. "
                        "Premi\u00e8re\u00a0: pr\u00e9server l\u2019unit\u00e9 du "
                        "contr\u00f4le social m\u00eame apr\u00e8s la succession "
                        "\u2014 les deux enfants travaillaient en entreprise, "
                        "mais avec des r\u00f4les et des perspectives diff\u00e9rents. "
                        "Deuxi\u00e8me\u00a0: permettre une liquidit\u00e9 de "
                        "«\u00a0retrait\u00a0» \u00e0 l\u2019\u00e9pouse et \u00e0 "
                        "la branche familiale non op\u00e9rationnelle sans "
                        "contraindre \u00e0 c\u00e9der des participations. "
                        "Troisi\u00e8me\u00a0: minimiser l\u2019impact fiscal de "
                        "la succession (droits de succession au-del\u00e0 du "
                        "seuil de 1\u00a0M\u20ac par parent en ligne directe) "
                        "dans le respect absolu de la norme en vigueur \u2014 "
                        "aucune structure offshore, aucun trust agressif.",
                },
                {
                    "label": "L\u2019approche",
                    "heading": "Holding familiale + pacte d\u2019actionnaires + PIR",
                    "body":
                        "Fiscus a coordonn\u00e9 un parcours de 20\u00a0mois en "
                        "quatre phases. Phase\u00a01 (mois\u00a01\u20134)\u00a0: "
                        "constitution d\u2019une holding familiale S.r.l. avec "
                        "apport des participations op\u00e9rationnelles en "
                        "neutralit\u00e9 fiscale ex art.\u00a0177 TUIR. "
                        "Phase\u00a02 (mois\u00a05\u20138)\u00a0: r\u00e9daction "
                        "du pacte d\u2019actionnaires entre les deux branches "
                        "familiales avec m\u00e9canisme de tag-along / drag-along "
                        "pour pr\u00e9venir les scissions futures. Phase\u00a03 "
                        "(mois\u00a09\u201314)\u00a0: donation graduelle des "
                        "parts de la holding aux enfants, avec usufruit viager "
                        "au profit du fondateur et de l\u2019\u00e9pouse \u2014 "
                        "b\u00e9n\u00e9ficiant du dispositif art.\u00a03, "
                        "alin\u00e9a 4-ter D.Lgs.\u00a0346/1990 (exon\u00e9ration "
                        "des droits de succession pour les participations de "
                        "contr\u00f4le). Phase\u00a04 (mois\u00a015\u201320)\u00a0: "
                        "souscription d\u2019instruments PIR compatibles pour "
                        "la branche non op\u00e9rationnelle de la famille, sur "
                        "les flux de dividendes.",
                },
                {
                    "label": "Le r\u00e9sultat",
                    "heading": "Succession fiscalement optimis\u00e9e + gouvernance familiale",
                    "body":
                        "La structure a \u00e9t\u00e9 finalis\u00e9e en septembre 2025. "
                        "Droits de succession ramen\u00e9s \u00e0 z\u00e9ro sur les "
                        "participations op\u00e9rationnelles gr\u00e2ce au dispositif "
                        "art.\u00a03, alin\u00e9a 4-ter (pacte de famille + holding "
                        "de contr\u00f4le). Pacte d\u2019actionnaires sign\u00e9 par "
                        "les deux fr\u00e8res et les parents, avec clauses de "
                        "buy-out au prix d\u2019expertise ind\u00e9pendante "
                        "actualis\u00e9e annuellement. La branche non "
                        "op\u00e9rationnelle (\u00e9pouse + \u00e9ventuels "
                        "petits-enfants) per\u00e7oit des dividendes r\u00e9guliers "
                        "sur la holding et a souscrit des PIR individuels pour "
                        "\u20ac\u00a0180\u00a0000 chacun sur l\u2019horizon "
                        "2025\u20132030. Le fondateur a conserv\u00e9 les droits "
                        "de vote en usufruit jusqu\u2019\u00e0 75\u00a0ans + "
                        "5\u00a0ans d\u2019option suppl\u00e9mentaire.",
                },
            ],
            "kpi": [
                ("\u20ac\u00a00",   "droits de succession sur les participations op\u00e9rationnelles"),
                ("100\u00a0%",      "unit\u00e9 du contr\u00f4le pr\u00e9serv\u00e9e"),
                ("20\u00a0mois",    "de la lettre de mission \u00e0 l\u2019ach\u00e8vement"),
                ("4/4",             "phases achev\u00e9es dans les d\u00e9lais"),
            ],
            "lead_partner": "Dr Stefano Conti",
            "team":         "1 associ\u00e9 · 1 senior · notaire externe · 20\u00a0mois",
            "next_label":   "Dossier suivant",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Premier rendez-vous",
        "headline": "Quarante-cinq minutes, ordre du jour <em>ouvert</em>, sans engagement.",
        "intro":
            "Le premier contact se tient avec un associ\u00e9 inscrit \u00e0 "
            "l\u2019ODCEC. Nous discutons du domaine de comp\u00e9tence, de "
            "l\u2019horizon temporel de la relation et des honoraires indicatifs "
            "\u2014 avant tout mandat sign\u00e9. Les clients existants prennent "
            "rendez-vous dans l\u2019espace r\u00e9serv\u00e9 sur l\u2019aire client.",

        # Form fields — commercialista onboarding shape
        "form_label":   "Demander un rendez-vous",
        "form_heading": "Remplissez la fiche exploratoire",
        "form_intro":
            "Vous recevrez confirmation sous 48\u00a0heures ouvr\u00e9es apr\u00e8s "
            "l\u2019envoi. Les donn\u00e9es sont trait\u00e9es conform\u00e9ment au "
            "R\u00e8gl.\u00a0UE 679/2016 et conserv\u00e9es dans l\u2019archive "
            "chiffr\u00e9e du cabinet avec r\u00e9tention d\u00e9cennale.",
        "form_fields": [
            {"name": "name",      "label": "Pr\u00e9nom",       "type": "text",     "required": True,  "placeholder": "Ex. Andrea",
             "helper": "Uniquement le pr\u00e9nom."},
            {"name": "surname",   "label": "Nom",               "type": "text",     "required": True,  "placeholder": "Ex. Ruffini",
             "helper": "Tel qu\u2019il appara\u00eet sur les pi\u00e8ces d\u2019identit\u00e9."},
            {"name": "company",   "label": "Raison sociale ou entreprise individuelle", "type": "text", "required": False,
             "placeholder": "Ex. Officine Meccaniche Bresciane S.r.l.",
             "helper": "Facultatif \u2014 \u00e0 remplir si le contact est au nom d\u2019une entreprise."},
            {"name": "vat",       "label": "Num\u00e9ro de TVA (Partita IVA)", "type": "text", "required": False, "placeholder": "IT 12345678901",
             "helper": "Facultatif \u2014 utile si la relation concerne la fiscalit\u00e9 d\u2019entreprise."},
            {"name": "fiscal_code","label": "Code fiscal (Codice Fiscale)", "type": "text", "required": True,  "placeholder": "RFFNDR72M15F205Z",
             "helper": "Obligatoire \u2014 n\u00e9cessaire pour l\u2019activation du mandat Entratel en cas de suite."},
            {"name": "email",     "label": "E-mail",            "type": "email",    "required": True,  "placeholder": "andrea.ruffini@exemple.fr",
             "helper": "Nous vous envoyons la confirmation de rendez-vous \u00e0 cette adresse."},
            {"name": "phone",     "label": "T\u00e9l\u00e9phone", "type": "tel",      "required": True,  "placeholder": "+39 ...",
             "helper": "Pour d\u2019\u00e9ventuelles demandes de pr\u00e9cision avant le rendez-vous."},
            {"name": "area",      "label": "Domaine de comp\u00e9tence d\u2019int\u00e9r\u00eat", "type": "select", "required": True,
             "options": [
                 "\u00c0 d\u00e9finir lors du rendez-vous",
                 "D\u00e9claration de revenus et fiscalit\u00e9 ordinaire",
                 "Comptes annuels et comptabilit\u00e9 ordinaire",
                 "Contentieux fiscal",
                 "Ing\u00e9nierie fiscale et patrimoine",
                 "Paie et conseil social",
                 "Audit l\u00e9gal",
             ],
             "helper": "Choisissez «\u00a0\u00c0 d\u00e9finir\u00a0» si la situation est complexe."},
            {"name": "time_slot", "label": "Cr\u00e9neau horaire pr\u00e9f\u00e9r\u00e9", "type": "select", "required": True,
             "options": [
                 "Matin\u00a0\u00b7 9\u00a0h\u00a0\u2013 12\u00a0h",
                 "D\u00e9but d\u2019apr\u00e8s-midi\u00a0\u00b7 14\u00a0h\u00a0\u2013 16\u00a0h\u00a030",
                 "Fin d\u2019apr\u00e8s-midi\u00a0\u00b7 16\u00a0h\u00a030\u00a0\u2013 18\u00a0h\u00a030",
                 "Indiff\u00e9rent",
             ],
             "helper": "\u00c0 l\u2019approche des \u00e9ch\u00e9ances, la priorit\u00e9 est donn\u00e9e aux cr\u00e9neaux matinaux."},
            {"name": "situation", "label": "Br\u00e8ve description de la situation", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "600\u00a0caract\u00e8res maximum. Exemple\u00a0: «\u00a0Num\u00e9ro de TVA en r\u00e9gime forfaitaire depuis 2021, premi\u00e8re ann\u00e9e de sortie du forfaitaire, je dois comprendre comment passer \u00e0 la comptabilit\u00e9 ordinaire.\u00a0»",
             "helper": "Juste ce qu\u2019il faut pour v\u00e9rifier que la situation rel\u00e8ve de nos domaines de comp\u00e9tence et pour pr\u00e9parer la premi\u00e8re conversation."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contact",
             "meta": "La personne que nous rencontrerons lors du premier rendez-vous.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Identifiants fiscaux",
             "meta": "Le Code fiscal est obligatoire\u00a0; le num\u00e9ro de TVA et la raison sociale uniquement si la relation concerne une activit\u00e9 d\u2019entreprise.",
             "fields": ["fiscal_code", "vat", "company"]},
            {"num": "03", "title": "P\u00e9rim\u00e8tre de l\u2019entretien",
             "meta": "Pour caler l\u2019associ\u00e9 r\u00e9f\u00e9rent sur le cr\u00e9neau demand\u00e9. Aucun d\u00e9tail sensible ici \u2014 les documents sont apport\u00e9s au rendez-vous.",
             "fields": ["area", "time_slot", "situation"]},
            {"num": "04", "title": "Documentation (facultative)",
             "meta": "Derni\u00e8re d\u00e9claration de revenus, derniers comptes annuels, \u00e9ventuels avis de l\u2019Agenzia Entrate\u00a0: ils peuvent pr\u00e9parer le rendez-vous.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "allegati_preliminari",
            "label":    "Documents pr\u00e9liminaires",
            "helper":   "Derni\u00e8re d\u00e9claration de revenus (Modello Redditi ou 730), derniers comptes annuels d\u00e9pos\u00e9s, avis de l\u2019Agenzia Entrate re\u00e7us. "
                        "PDF · 10\u00a0Mo maximum au total. Archive chiffr\u00e9e \u00e0 acc\u00e8s restreint aux associ\u00e9s.",
            "accept":   ".pdf",
            "multiple": True,
            "primary":  "D\u00e9posez les documents ici ou",
            "link":     "parcourez l\u2019archive",
            "meta":     "PDF · 10\u00a0Mo max · archive chiffr\u00e9e AES-256",
        },

        "form_submit_label": "Demander un rendez-vous",
        "form_submit_note":
            "Confirmation d\u2019un associ\u00e9 inscrit \u00e0 l\u2019ODCEC sous "
            "48\u00a0heures ouvr\u00e9es. Aucun secr\u00e9tariat externe, aucune "
            "automatisation \u2014 nous lisons personnellement chaque demande.",
        "form_consent":
            "J\u2019accepte le traitement de mes donn\u00e9es personnelles "
            "conform\u00e9ment au R\u00e8gl.\u00a0UE 679/2016. Les donn\u00e9es "
            "sont conserv\u00e9es dans l\u2019archive chiffr\u00e9e du cabinet "
            "avec r\u00e9tention d\u00e9cennale, acc\u00e8s restreint aux "
            "associ\u00e9s et aux collaborateurs inscrits \u00e0 l\u2019ordre "
            "professionnel. Aucune donn\u00e9e n\u2019est communiqu\u00e9e \u00e0 "
            "des tiers sans autorisation \u00e9crite explicite.",

        # Office meta-row labels (lifted from skin for i18n)
        "office_address_label": "Adresse",
        "office_area_label":    "Quartier",
        "office_phone_label":   "T\u00e9l\u00e9phone",
        "office_email_label":   "E-mail",

        # Sidebar — sede + canali diretti
        "offices_label":   "Si\u00e8ge",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Si\u00e8ge unique",
                "address": "Via Melzo 14 · 20129",
                "area":    "Porta Venezia · \u00e0 200\u00a0m\u00e8tres de la station MM Porta Venezia",
                "phone":   "+39 02 4951 3388",
                "email":   "segreteria@fiscusstudio.it",
            },
        ],

        "channels_label": "Canaux directs",
        "channels": [
            ("Secr\u00e9tariat du cabinet", "+39 02 4951 3388",           "Lun.\u00a0\u2013 Ven. · 9\u00a0h\u00a0\u2013 18\u00a0h\u00a030"),
            ("E-mail institutionnel",       "segreteria@fiscusstudio.it", "R\u00e9ponse sous 48\u00a0heures ouvr\u00e9es"),
            ("Espace client r\u00e9serv\u00e9", "area.fiscusstudio.it",    "Pour les clients existants \u2014 \u00e9ch\u00e9ances + documents"),
        ],

        "footnote":
            "Fiscus ne r\u00e9pond pas aux demandes anonymes et ne d\u00e9livre "
            "pas d\u2019avis fiscal pr\u00e9liminaire par e-mail. Les informations "
            "administratives (honoraires indicatifs, modalit\u00e9s de facturation, "
            "calendrier des \u00e9ch\u00e9ances du p\u00e9rim\u00e8tre propos\u00e9) "
            "sont pr\u00e9sent\u00e9es lors du premier rendez-vous \u2014 \u00e0 "
            "titre gratuit et sans engagement.",
    },
}
