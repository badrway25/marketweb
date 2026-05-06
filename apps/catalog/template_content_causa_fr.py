"""Causa — Studio legale (corporate-suite archetype) ·
French locale content tree.

Phase X.6 Causa · workflow C · multilingual rollout on top of the
locked LF-2 Italian draft (A.6 review-lock + A.5b imagery re-curate +
slice-01 + slice-02 + motion_profile DNA pass 1). Mirrors the shape
of ``CAUSA_CONTENT_IT`` exactly — same keys, same nesting, same list
shapes. Only values are translated and adapted.

Voice register : publication forensique · adossée à la preuve ·
registre du dossier de Cassation. Équivalent natif français du
registre IT — la presse de droit du Cabinet français : Recueil Dalloz,
Gazette du Palais, Journal des Tribunaux, Revue trimestrielle de droit
civil, chroniques de la Cour de cassation. Vouvoiement, déclaratif,
jamais marketing-SaaS, jamais discours commercial. Voix de référence :
chroniques Dalloz · éditoriaux Gazette du Palais · arrêts versés à
la Documentation française.

Voice anchor (CS-EXEC-01 / CS-BLOCK-11 · preserved
verbatim-in-translation across all 5 locales · the load-bearing
italic moves with the equivalent PUBLIC-RECORD-EVIDENCE noun · per
factory/reports/copy/causa-legale/voice-anchor-lock.md §4.2 +
factory/reports/causa/causa-planner-brief.md §11) :
    « Chaque décision est une <em>preuve</em> versée au dossier — non une opinion défendue. »

Italian normative references and Italian proper nouns are preserved
verbatim (D.lgs. 24/2023 whistleblowing · D.lgs. 196/2003 vie privée
· D.M. 55/2014 tarifs forensiques · Codice Deontologico Forense ·
art. 622 c.p. secret professionnel · D.lgs. 28/2010 médiation
obligatoire · D.lgs. 74/2000 pénal-fiscal · D.lgs. 259/2003 télécoms
· ENCA · CTU forense · Tribunale di Milano · Cassazione · TAR
Lombardia · Corte d'Appello di Milano · Foro di Milano · Foro
Italiano · Giurisprudenza Italiana · Albo Avvocati · Reg. UE
679/2016 / RGPD). Italian addresses, phone formats, Euro figures and
years are kept as-is. Italian sentence-identifiers carry verbatim
across all locales (Cass. SS.UU. n. 11237/2024 · Cass. civ. sez. III
n. 28914/2023 · TAR Lombardia sez. III n. 814/2022 · Corte d'Appello
Milano sez. trib. n. 3187/2021).
"""
from __future__ import annotations

from typing import Any


from apps.catalog.template_content_causa import (  # noqa: E402
    _HERO_COURTROOM_INTERIOR,
    _PORTRAIT_FOUNDER,
    _CASE_HIGHCOURT_EXTERIOR,
    _CASE_FASCICOLI_STACK,
    _CASE_BENCH_CHAIR,
    _CASE_CODEX_SPINE,
)


CAUSA_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",        "label": "Le cabinet",   "kind": "home"},
        {"slug": "materie",     "label": "Matières",     "kind": "services"},
        {"slug": "studio",      "label": "Publications", "kind": "about"},
        {"slug": "contenzioso", "label": "Contentieux",  "kind": "case_study_list"},
        {"slug": "contatti",    "label": "Contact",      "kind": "contact"},
    ],

    "site": {
        "logo_initial": "C",
        "logo_word":     "CAUSA",
        "logo_subtitle": "studio legale",
        "tag":           "Cabinet d'avocat · Milan · depuis 1995",
        "phone":         "+39 02 7634 8210",
        "email":         "parere@causa.legal",
        "address":       "Via Borgonuovo 14 · 20121 Milan",
        "hours_compact": "Lun – Ven · 09:00 – 18:00 · sur rendez-vous",
        "hours_footer_rows": [
            "Samedi · uniquement pour délais en cours",
            "Dimanche · fermé · réponse au plus tard lundi",
        ],
        "license":
            "Albo Avvocati Milano · Cassazionista depuis 2003 · "
            "ENCA médiateurs · Albo CTU forense Tribunale di Milano",
        "footer_intro":
            "Cabinet de plaidoyer éditorial. Avocat fondateur "
            "Lorenzo Marchetti · inscrit au Barreau de Milan "
            "depuis 1995. Cabinet unique à Milan · Foro di Milano. "
            "Plaidoyer dans tous les degrés de juridiction "
            "jusqu'à la Cour de Cassation · vingt-huit décisions "
            "citées · quatorze entrées au répertoire interne · "
            "trente et un ans d'exercice éditorial.",
        "foot_studio":   "Cabinet",
        "foot_pages":    "Pages",
        "foot_contact":  "Contact",
        "foot_offices":  "Cabinet",
        "offices_footer_rows": [
            "Milan · Via Borgonuovo 14 · cabinet unique",
            "Sur rendez-vous · lundi-vendredi",
            "Foro di Milano · démarches au greffe traitées en interne",
        ],
        "whistleblowing_footer": {
            "heading":      "Signalements",
            "eyebrow":      "Canal interne · D.lgs. 24/2023",
            "note":
                "Le cabinet a institué un canal de signalement "
                "interne conforme au D.lgs. 24/2023 (directive UE "
                "2019/1937). Référent prévention : avocat associé "
                "senior, indépendant du fondateur. Confidentialité "
                "garantie au sens de la réglementation. Ouvert "
                "aux collaborateurs, associés et secrétariat.",
            "email":        "whistleblowing@causa.legal",
            "policy_label": "Politique de gestion des signalements",
            "policy_href":  "contatti",
        },
        "case_practice_label":     "Matière",
        "case_year_label":         "Année · dépôt",
        "case_duration_label":     "Degré · issue",
        "case_lead_label":         "Plaidoyer",
        "case_lead_partner_label": "Plaidoyer",
        "case_team_label":         "Rédaction du cabinet",
        "case_timeline_label":     "Chronologie procédurale",
    },

    "home": {
        "eyebrow":     "CABINET D'AVOCAT · MILAN · DEPUIS 1995",
        # Voice anchor verbatim · italic on `preuve`, the French
        # Cassation cognate of `evidenza` (per voice-anchor-lock §4.2).
        # Carries the forensic-press sense « preuve versée au dossier »
        # — distinct from `démonstration` (which would drift toward
        # architectural-press demonstration) or `argument` (which is
        # Cornice's anchor cognate).
        "headline":
            "Chaque décision est une <em>preuve</em> versée au dossier — non une opinion défendue.",
        "intro":
            "Cabinet de plaidoyer éditorial · avocat fondateur "
            "Cassazionista · vingt-huit décisions citées depuis 1995.",
        "primary_cta":   "Soumettez un avis préliminaire",
        "primary_href":  "contatti",
        "secondary_cta": "Le cabinet · siège unique à Milan",
        "secondary_href":"studio",

        "hero_image":              _HERO_COURTROOM_INTERIOR,
        "hero_image_alt":
            "Salle d'audience vide · lumière froide · panneaux de "
            "bois verticaux et murs ton bone · intérieur architectural",
        "hero_image_credit_left":  ("Salle d'audience · intérieur · 2024", "Foro di Milano"),
        "hero_image_credit_right": ("Cabinet", "Milan · Via Borgonuovo 14"),
        "hero_image_provenance":
            "Pexels · CC0 · St George's Hall, Liverpool · n° 33939830",
        "hero_image_provenance_aria":
            "Provenance de la photographie · banque Pexels · licence CC0",
        "hero_meta_strip": [
            ("Décisions citées",       "28"),
            ("Entrées au répertoire",  "14"),
            ("Années d'exercice",      "31"),
        ],
        # Side-quote em on the verb form `verse` — French Cassation
        # idiom « verser au dossier » is the canonical verb for the
        # forensic act of placing an item on the record. Per voice-
        # anchor-lock §6.4: the side-quote em moves with the verb-form
        # of the public-record-evidence anchor in each locale.
        "hero_side_quote":
            "Plaidoyer devant la Cour de Cassation et dans tous "
            "les degrés du fond. Le cabinet ne soutient que ce "
            "qu'il <em>verse</em> au dossier de procédure : la "
            "preuve déposée, la décision citable, la matière du "
            "droit elle-même.",

        "narrative_label":   "LE CABINET · MÉTHODE PROBATOIRE",
        "narrative_drop":    "L",
        "narrative_chronotick": [
            ("1995", "Fondation · Milan"),
            ("2003", "Habilitation Cassazionista"),
            ("2008", "Première décision au répertoire interne"),
            ("2014", "Première saisine SS.UU."),
            ("2018", "Inscription Albo CTU forense"),
            ("2024", "Quatorzième entrée · SS.UU. responsabilité professionnelle"),
        ],
        "narrative_blocks": [
            ("drop",
             "a bonne jurisprudence se verse au dossier. Causa "
             "est un cabinet de plaidoyer éditorial : chaque "
             "cause portée à l'audience est une preuve versée sur "
             "l'objet du contentieux, sur le degré de juridiction, "
             "sur la juridiction elle-même. Nous ne signons pas "
             "des opinions décoratives — nous déposons des "
             "mémoires, chacun avec sa documentation et sa "
             "décision citable. Le cabinet existe pour mesurer le "
             "dossier avant de le plaider, pour rédiger la "
             "décision avant de la soutenir, pour reconnaître ce "
             "qui a déjà été jugé avant de proposer ce qui doit "
             "l'être encore. C'est un métier lent, qui ouvre peu "
             "de causes par an, mais qui les porte jusqu'en "
             "Cassation."),

            ("quote",
             "La <em>juridiction</em> est la première forme de "
             "respect. Ce qui se soutient devant le for compétent "
             "sera toujours plus solide que ce qui se déclame au "
             "mauvais degré."),

            ("para",
             "Chaque cause traverse quatre saisons. La "
             "juridiction, d'abord : la matière qui existe déjà "
             "se lit comme un dossier, avec ses précédents, ses "
             "degrés, ses exceptions préliminaires. Le fond, "
             "ensuite : l'objet du contentieux, les parties en "
             "cause, la fourchette de valeur, l'urgence "
             "procédurale, la preuve préliminaire versable au "
             "dossier. La décision, enfin : le mémoire s'écrit "
             "comme une thèse citable — quel principe il invoque, "
             "quelle orientation il confirme, quelle preuve il "
             "verse. Alors seulement nous ouvrons la procédure, "
             "et nous la suivons audience par audience, degré par "
             "degré, jusqu'au prononcé. Les mémoires restent "
             "écrits : nous publions les décisions obtenues dans "
             "le répertoire interne du cabinet, parce qu'un "
             "plaidoyer sans mémoire ne laisse pas de règle."),

            ("quote",
             "Une <em>décision</em> ce n'est pas qui gagne le "
             "plus de causes, mais qui sait dire quel mémoire il "
             "n'a pas déposé — et pourquoi."),

            ("para",
             "Nous plaidons pour des entreprises et des "
             "particuliers qui cherchent un avocat — non un "
             "exécutant standard, non un prestataire en forfait. "
             "Sociétés en contentieux bancaire complexe, "
             "professionnels en responsabilité contestée, "
             "contribuables faisant face à des avis "
             "d'imposition agressifs, organismes privés en "
             "contentieux administratif réglementaire, parties "
             "civiles en procédure pénale-fiscale. Notre "
             "signature est celle d'un Cassazionista unique, "
             "non d'une marque de cabinet à plusieurs mains : la "
             "responsabilité technique reste concentrée, parce "
             "qu'une preuve, pour être soutenue, doit avoir une "
             "voix. Les collaborations avec consultants "
             "techniques, experts comptables, fiscalistes "
             "spécialisés et conseils de partie passent par le "
             "cabinet — elles ne le remplacent pas. Nous "
             "plaidons peu, et jusqu'au bout."),

            ("quote",
             "Publier une décision n'est pas en faire la "
             "publicité. C'est laisser une preuve <em>soutenue</em> "
             "— pour que ceux qui viendront après puissent la "
             "contester, la distinguer ou la reconnaître."),

            ("para",
             "Les décisions publiées ici ne constituent pas un "
             "CV forensique. Ce sont des preuves versées au "
             "dossier, rassemblées par matière et par année, "
             "avec la documentation du jugement qui les "
             "accompagne. Chaque fiche nomme la juridiction, le "
             "degré, la matière, l'année, l'objet du contentieux, "
             "et la décision déposée en cinq lignes — parce "
             "qu'une décision qui ne se laisse pas raconter en "
             "cinq lignes n'est probablement pas encore "
             "clarifiée. Les quatre décisions sélectionnées ci-"
             "dessous couvrent quatre années et quatre matières "
             "différentes : une orientation des Sezioni Unite "
             "sur la responsabilité professionnelle, une "
             "cassation civile en contentieux bancaire, une "
             "décision du TAR Lombardia en administratif "
             "réglementaire, et un appel fiscal à Milan."),
        ],
        "narrative_side_rail": [
            ("Cabinet · l'avocat fondateur",                  "studio"),
            ("Matières · les douze matières",                 "materie"),
            ("Publications · répertoire interne",             "studio"),
            ("Contact · soumettez un avis préliminaire",      "contatti"),
        ],

        "sectors_label":    "MATIÈRES · LE CHAMP DU CONTENTIEUX",
        "sectors_lead":
            "Douze matières du contentieux : toutes traitées au "
            "cabinet, jamais déléguées à des correspondants "
            "extérieurs. Le cabinet ne se déclare ni généraliste "
            "ni spécialiste — il choisit ses causes par objet, "
            "par degré de juridiction et par juridiction.",
        "sectors": [
            "pénal-fiscal", "civil contractuel", "administratif réglementaire",
            "contentieux bancaire", "responsabilité professionnelle", "recouvrement complexe",
            "droit des sociétés", "fiscal", "voies d'exécution",
            "travail complexe", "expert judiciaire", "médiation ENCA",
        ],
        "sectors_trailing":
            "Une matière entre au cabinet quand la preuve est "
            "versable au dossier et que la jurisprudence est "
            "lisible. Elle en sort quand le dossier ne se laisse "
            "pas écrire en cinq lignes.",
        "sectors_counter":
            "Vingt-huit décisions citées · quatorze entrées "
            "publiées par le Foro Italiano et la Giurisprudenza "
            "Italiana entre <em>2008</em> et 2024 · trente et un "
            "ans d'exercice dans tous les degrés jusqu'en "
            "Cassation.",

        "leadership_label":   "FONDATEUR DU CABINET · CASSAZIONISTA",
        "leadership_heading": "Lorenzo <em>Marchetti</em>",
        "leadership_role":
            "fondateur · responsable des mémoires et des pourvois en Cassation",
        "leadership_caption": "Le cabinet · chambres de Via Borgonuovo · 2024",
        "leadership_portrait": _PORTRAIT_FOUNDER,
        "leadership_bio_paragraphs": [
            "Lorenzo Marchetti a fondé Causa à Milan en 1995, "
            "après huit ans d'exercice dans deux cabinets "
            "milanais spécialisés en contentieux civil "
            "commercial et en droit bancaire. Il a soutenu en "
            "1987 sa licence en droit à l'Università degli Studi "
            "di Milano, avec une thèse sur le concours apparent "
            "de normes en droit fiscal, et obtenu la "
            "spécialisation en droit privé dans la même "
            "université. Inscrit au Barreau de Milan depuis 1995, "
            "habilité à plaider devant les Magistratures "
            "Supérieures (Cassazionista) depuis 2003. Il "
            "travaille à plein temps sur les contentieux du "
            "cabinet : il dirige la rédaction des mémoires, "
            "écrit les pourvois en Cassation, suit la procédure "
            "jusqu'au prononcé, et tient le répertoire interne "
            "qui publie les décisions obtenues.",

            "Parmi les décisions citées : l'orientation des "
            "Sezioni Unite de 2024 en matière de responsabilité "
            "professionnelle du conseil fiscal, la cassation "
            "civile sez. III de 2023 sur le droit du client "
            "bancaire au remboursement des intérêts "
            "anatocistiques, une décision du TAR Lombardia de "
            "2022 sur la légalité d'une sanction AGCOM, et la "
            "cassation fiscale de 2021 sur l'interprétation de "
            "l'art. 36-bis D.P.R. 600/1973. Ses voix sont "
            "rassemblées en quatorze entrées publiées par le "
            "Foro Italiano et la Giurisprudenza Italiana entre "
            "2008 et 2024.",
        ],
        "leadership_credentials": [
            "Albo Avvocati Milano · Inscrit au Barreau de Milan · depuis 1995",
            "Cassazionista · habilité devant les Magistratures Supérieures depuis 2003",
            "ENCA · Conseil National Conciliation Avocats · section médiateurs",
            "Albo CTU forense · Tribunale di Milano · section contentieux civil",
        ],
        "leadership_secondary_cta_label": "Cabinet · biographie étendue, entrées au répertoire",
        "leadership_secondary_cta_href":  "studio",

        "cases_label":   "CONTENTIEUX — PREUVES VERSÉES",
        "cases_intro":
            "Quatre preuves déposées, en ordre chronologique "
            "inverse. Juridiction, degré, matière, année, objet "
            "du contentieux et la décision.",
        "cases_magazine": [
            {
                "rank":     "hero",
                "num":      "01",
                "eyebrow":  "01 · CASS. SS.UU. · 2024 · RESPONSABILITÉ PROFESSIONNELLE",
                "title":
                    "Sezioni Unite — la responsabilité "
                    "professionnelle du conseil fiscal, relue "
                    "comme obligation de résultat <em>versée</em> "
                    "à la preuve préliminaire",
                "body":
                    "Causa était plaideur du demandeur dans le "
                    "pourvoi tranché par les Sezioni Unite de la "
                    "Cour de Cassation en avril 2024, sur saisine "
                    "de la troisième chambre civile. Le litige "
                    "opposait un contribuable à son conseil "
                    "fiscal, en matière de responsabilité "
                    "professionnelle pour défaut de signalement "
                    "d'un délai d'impugnation en matière fiscale. "
                    "Le cabinet a soutenu, et la Cour a accueilli, "
                    "l'orientation selon laquelle la "
                    "responsabilité du conseil fiscal se verse à "
                    "la preuve préliminaire dont le professionnel "
                    "pouvait et devait avoir connaissance au "
                    "moment de la mission — relisant la "
                    "prestation comme obligation de résultat "
                    "circonscrit. La décision a été publiée par "
                    "le Foro Italiano (entrée n° 14 du répertoire "
                    "interne du cabinet).",
                "pill":
                    "Cassazione SS.UU.  ·  degré de légitimité  ·  2024  ·  demandeur",
                "photo":    _CASE_HIGHCOURT_EXTERIOR,
                "photo_alt":
                    "Détail architectural d'une haute cour "
                    "italienne · fronton classique avec "
                    "inscription latine · lumière froide overcast",
                "slug":     "cass-ssuu-responsabilita-consulente-fiscale-2024",
                "citation_label": "Voir la décision n° 14",
                "citation":
                    "Cass. SS.UU. n. 11237/2024 — La "
                    "<em>responsabilité</em> professionnelle du "
                    "conseil fiscal se verse à la preuve "
                    "préliminaire dont le professionnel pouvait "
                    "et devait avoir connaissance au moment de "
                    "la mission, la prestation relue comme "
                    "obligation de résultat circonscrite à "
                    "l'objet du mandat. Entrée n° 14 du "
                    "répertoire interne · publiée Foro Italiano "
                    "2024.",
            },
            {
                "rank":     "small",
                "num":      "02",
                "eyebrow":  "02 · CASS. CIV. SEZ. III · 2023 · CONTENTIEUX BANCAIRE",
                "title":
                    "Cassation civile sez. III — anatocisme "
                    "bancaire et charge de la preuve dans la "
                    "<em>jurisprudence</em> de légitimité",
                "body":
                    "Causa a plaidé pour le client bancaire dans "
                    "la cassation civile sez. III d'octobre 2023, "
                    "sur le remboursement d'intérêts "
                    "anatocistiques perçus sur un compte "
                    "courant entre 2003 et 2014. Le cabinet a "
                    "soutenu l'attribution de la charge "
                    "probatoire du lien causal à l'établissement "
                    "bancaire, conformément à l'orientation de "
                    "légitimité consolidée depuis 2014. La "
                    "décision a cassé avec renvoi. Entrée n° 11 "
                    "du répertoire interne.",
                "pill":
                    "Cass. civ. III  ·  degré de légitimité  ·  2023  ·  demandeur",
                "photo":    _CASE_FASCICOLI_STACK,
                "photo_alt":
                    "Pile de dossiers juridiques avec étiquettes "
                    "de registre · lumière froide de bureau · "
                    "macro · zéro personne",
                "slug":     "cass-civ-iii-anatocismo-bancario-2023",
                "citation_label": "Voir la décision n° 11",
                "citation":
                    "Cass. civ. sez. III n. 28914/2023 — En "
                    "matière de remboursement d'intérêts "
                    "<em>anatocistiques</em> perçus sur un "
                    "compte courant bancaire, la charge "
                    "probatoire du lien causal entre "
                    "capitalisation trimestrielle et croissance "
                    "du solde pèse sur l'établissement bancaire, "
                    "conformément à l'orientation de légitimité "
                    "consolidée depuis 2014. Cassée avec renvoi. "
                    "Entrée n° 11 du répertoire interne.",
            },
            {
                "rank":     "small",
                "num":      "03",
                "eyebrow":  "03 · TAR LOMBARDIA · 2022 · ADMINISTRATIF RÉGLEMENTAIRE",
                "title":
                    "TAR Lombardia — annulation d'une sanction "
                    "AGCOM et le <em>principe</em> de "
                    "proportionnalité",
                "body":
                    "Causa était plaideur du demandeur en "
                    "première instance devant le TAR Lombardia, "
                    "sez. III, conclue en avril 2022 par "
                    "l'annulation de la sanction AGCOM "
                    "contestée pour excès de pouvoir et "
                    "violation du principe de proportionnalité "
                    "de la sanction administrative pécuniaire, "
                    "à la lumière de l'orientation du Conseil "
                    "d'État de 2019. La décision n'a pas été "
                    "frappée d'appel par AGCOM. Entrée n° 9 du "
                    "répertoire interne.",
                "pill":
                    "TAR Lombardia  ·  premier degré  ·  2022  ·  demandeur",
                "photo":    _CASE_BENCH_CHAIR,
                "photo_alt":
                    "Siège de tribunal vide · haut dossier en "
                    "chêne · panneaux de bois verticaux à "
                    "l'arrière · lumière froide · zéro personne",
                "slug":     "tar-lombardia-agcom-proporzionalita-2022",
                "citation_label": "Voir la décision n° 9",
                "citation":
                    "TAR Lombardia sez. III n. 814/2022 — "
                    "Annulation de la sanction AGCOM pour "
                    "excès de pouvoir et violation du "
                    "<em>principe</em> de proportionnalité de "
                    "la sanction administrative pécuniaire, à "
                    "la lumière de l'orientation du Conseil "
                    "d'État sec. VI 4419/2019. Décision non "
                    "frappée d'appel par AGCOM. Entrée n° 9 "
                    "du répertoire interne.",
            },
            {
                "rank":     "small",
                "num":      "04",
                "eyebrow":  "04 · COUR D'APPEL DE MILAN · 2021 · FISCAL",
                "title":
                    "Cour d'Appel de Milan — l'art. 36-bis "
                    "D.P.R. 600/1973 et le périmètre du "
                    "<em>litige</em> fiscal",
                "body":
                    "Causa a soutenu, en appel devant la Corte "
                    "d'Appello di Milano sez. tributaria, "
                    "l'interprétation restrictive de l'art. "
                    "36-bis D.P.R. 600/1973 en matière de "
                    "liquidation automatisée des déclarations "
                    "fiscales. La décision, déposée en septembre "
                    "2021, a infirmé la décision de première "
                    "instance de la Commission Fiscale, "
                    "annulant l'avis de paiement. Entrée n° 7 "
                    "du répertoire interne.",
                "pill":
                    "App. Milano trib.  ·  second degré  ·  2021  ·  appelant",
                "photo":    _CASE_CODEX_SPINE,
                "photo_alt":
                    "Macro du dos d'un codex relié · "
                    "typographie or sur cuir sombre · "
                    "numérotation romaine · lumière froide douce",
                "slug":     "appello-milano-art-36bis-dpr-600-1973-2021",
                "citation_label": "Voir la décision n° 7",
                "citation":
                    "Corte d'Appello Milano sez. trib. n. "
                    "3187/2021 — Interprétation restrictive de "
                    "l'art. 36-bis D.P.R. 29 septembre 1973 n. "
                    "600 en matière de liquidation automatisée "
                    "des déclarations fiscales · le périmètre du "
                    "<em>litige</em> fiscal se limite aux "
                    "simples erreurs matérielles et de calcul "
                    "détectables à partir de la déclaration, "
                    "excluant toute appréciation au fond. "
                    "Décision infirmée en appel. Entrée n° 7 du "
                    "répertoire interne.",
            },
        ],
        "cases_trailing_label": "Tout le contentieux · chronologie 1995–2024",
        "cases_trailing_href":  "contenzioso",

        "cta_label":     "AVIS PRÉLIMINAIRE",
        "cta_intro":
            "Tout plaidoyer commence par une seule page : l'avis préliminaire.",
        "cta_heading":
            "Chaque décision est une <em>preuve</em> versée au dossier — non une opinion défendue.",
        "cta_form_hint":
            "Objet du contentieux · degré de juridiction · "
            "partie adverse · fourchette de valeur · juridiction "
            "· preuve préliminaire versable. Réponse sous cinq "
            "jours ouvrés.",
        "cta_primary":   "Soumettez un avis préliminaire",
        "cta_primary_href": "contatti",
        "cta_closing_line":
            "Aucun appel de découverte. Aucun mandat sans "
            "screening. Seulement la preuve, et sa juridiction.",
        "cta_sub_line":
            "Causa · cabinet d'avocat · Milan · depuis 1995",
    },

    "studio": {
        "eyebrow":   "LE CABINET · QUI SOMMES-NOUS · CV",
        "headline":
            "Causa · cabinet de plaidoyer éditorial depuis <em>1995</em>.",
        "intro":
            "Milan. Un avocat fondateur, deux associés, un "
            "secrétariat. Nous plaidons peu, et jusqu'au bout.",
        "primary_cta":  "Soumettez un avis préliminaire",

        "history_label":   "ÉTAPES DU CABINET",
        "history_heading": "Cinq dates, trente et un ans de plaidoyer éditorial.",
        "history_intro":
            "Cinq choix structurels derrière lesquels se lit le "
            "caractère du cabinet — l'auctorialité d'un "
            "Cassazionista unique, le répertoire interne comme "
            "méthode, la juridiction comme première forme de "
            "respect, la matière comme champ du contentieux, le "
            "plaidoyer jusqu'au prononcé.",
        "history": [
            ("1995", "Fondation",
             "Lorenzo Marchetti ouvre Causa Via Borgonuovo à "
             "Milan, après huit ans d'exercice dans deux cabinets "
             "milanais spécialisés en contentieux civil "
             "commercial et en droit bancaire. Le siège est "
             "choisi pour une raison unique : trois pièces sur "
             "une cour intérieure, l'une pour la rédaction des "
             "mémoires, l'autre pour le répertoire interne, "
             "l'autre pour le secrétariat."),
            ("2003", "Habilitation Cassazionista",
             "Lorenzo Marchetti obtient l'habilitation à "
             "plaider devant les Magistratures Supérieures "
             "(Cassazionista). À partir de cette année, le "
             "cabinet accepte les pourvois en cassation en "
             "matière civile, fiscale et administrative, et "
             "tient les mémoires des défendeurs en degré de "
             "légitimité."),
            ("2008", "Première décision publiée au répertoire",
             "La première décision de légitimité citant une "
             "orientation soutenue par le cabinet est publiée "
             "par le Foro Italiano. À partir de cette année, le "
             "cabinet inscrit au répertoire interne chaque "
             "décision obtenue — gagnée ou perdue — dans les "
             "soixante jours du dépôt."),
            ("2018", "Inscription Albo CTU forense",
             "Le cabinet s'inscrit à l'Albo CTU forense du "
             "Tribunale di Milano (section contentieux civil). "
             "À partir de cette année, il accepte les "
             "expertises judiciaires sur contentieux des "
             "sociétés, évaluations d'entreprise contestées et "
             "responsabilité comptable."),
            ("2024", "Quatorzième entrée au répertoire interne",
             "La quatorzième entrée du cabinet entre au "
             "répertoire interne : l'orientation des Sezioni "
             "Unite en matière de responsabilité "
             "professionnelle du conseil fiscal, sur saisine de "
             "la troisième chambre civile. Plaidoyer du client "
             "demandeur, décision déposée en avril, entrée "
             "publiée par le Foro Italiano."),
        ],

        "values_label":   "PRINCIPES ÉDITORIAUX",
        "values_heading": "Quatre principes <em>non négociables</em>",
        "values_intro":
            "Quatre principes séparent un plaidoyer Causa d'un "
            "mandat standardisé. Ils sont écrits dans le pacte "
            "de mandat signé en première audience, non sur le "
            "site.",
        "values": [
            ("01", "Un Cassazionista auctorial",
             "La signature du mémoire est celle d'un seul "
             "avocat, non d'une marque de cabinet à plusieurs "
             "mains. La responsabilité technique reste "
             "concentrée, parce qu'une preuve, pour être "
             "soutenue, doit avoir une voix. Les collaborations "
             "extérieures passent par le cabinet — elles ne le "
             "remplacent pas."),
            ("02", "La juridiction comme premier geste",
             "Chaque cause s'ouvre par un screening sérieux de "
             "la juridiction. La matière qui existe déjà se lit "
             "comme un dossier, avec ses précédents, ses "
             "degrés, ses exceptions préliminaires. Aucun "
             "plaidoyer avant que le for, le degré et la "
             "juridiction n'aient été lus intégralement."),
            ("03", "Le répertoire interne comme méthode",
             "Toutes les décisions obtenues — gagnées et "
             "perdues — sont inscrites au répertoire interne "
             "dans les soixante jours du dépôt, avec la "
             "documentation du jugement complète. Le répertoire "
             "n'est pas du marketing : c'est la règle que nous "
             "laissons à ceux qui viendront après."),
            ("04", "Pas de screenings refusés payants",
             "Les avis préliminaires qui ne passent pas la "
             "phase de screening sont restitués avec une note "
             "motivée, gratuitement. Nous ne facturons pas les "
             "screenings refusés. L'évaluation de la versabilité "
             "de la preuve au dossier est la porte du cabinet, "
             "non un service à la consommation."),
        ],

        "team_label":   "CABINET ET ASSOCIÉS",
        "team_heading": "Trois avocats, un cabinet, un secrétariat.",
        "team_intro":
            "Le cabinet est composé d'un avocat fondateur "
            "Cassazionista, deux associés et un secrétariat. "
            "Nous plaidons à plein temps entre douze et dix-huit "
            "causes en parallèle — jamais plus de vingt. Les "
            "démarches au greffe, les bureaux du parquet, "
            "l'Avvocatura dello Stato et les autorités de "
            "régulation sont traités au cabinet, jamais "
            "délégués à des correspondants extérieurs.",
        "team": [
            {"name": "Lorenzo Marchetti",
             "role": "Studio Founder · Avocat Cassazionista",
             "office": "Milan",
             "bio":
                "Fondateur. Università degli Studi di Milano · "
                "Droit · spécialisation en droit privé. Barreau "
                "de Milan depuis 1995 · Cassazionista depuis "
                "2003 · ENCA médiateurs · Albo CTU forense "
                "Tribunale di Milano. Dirige la rédaction des "
                "mémoires, écrit les pourvois en Cassation, "
                "tient le répertoire interne."},
            {"name": "Avv. Chiara Bevilacqua",
             "role": "Avocate associée · Sociétés + bancaire",
             "office": "Milan",
             "bio":
                "Associée depuis 2017 · Barreau de Milan depuis "
                "2014 · spécialisation en droit des sociétés et "
                "en contentieux bancaire · supervise les "
                "mémoires de demandeur dans les contentieux "
                "sociétaires et les actions en responsabilité "
                "· référente du répertoire interne · inscrite "
                "section médiateurs ENCA depuis 2020."},
            {"name": "Avv. Tommaso De Luca",
             "role": "Avocat associé · Administratif + fiscal",
             "office": "Milan",
             "bio":
                "Associé depuis 2021 · Barreau de Milan depuis "
                "2018 · spécialisation en droit administratif "
                "et en contentieux fiscal · référent pour les "
                "recours au TAR Lombardia et aux Commissions "
                "Fiscales · Albo CTU forense Tribunale di "
                "Milano depuis 2022 (section contentieux civil)."},
        ],

        "coordinates_label": "LE CABINET",
        "coordinates": [
            ("Milan", "Via Borgonuovo 14 · 20121 · trois pièces sur cour intérieure"),
            ("Cabinet", "sur rendez-vous · lundi-vendredi · 09:00-18:00"),
            ("Foro di Milano", "démarches au greffe traitées en interne · zéro correspondant extérieur"),
        ],

        "cta_heading": "Un plaidoyer commence par une seule page.",
        "cta_intro":
            "La première page de tout plaidoyer est l'avis "
            "préliminaire : une fiche de synthèse que le "
            "cabinet lit intégralement, à laquelle il répond "
            "sous cinq jours ouvrés par une note motivée. Si "
            "l'avis est négatif, la note motivée est remise "
            "gratuitement · sans facturation de screening · "
            "sans obligation de mandat.",
        "cta_primary":   "Soumettez un avis préliminaire",
        "cta_primary_href": "contatti",
    },

    "materie": {
        "eyebrow":  "MATIÈRES · LES DOUZE MATIÈRES DU CONTENTIEUX",
        "headline": "Les <em>matières</em> du contentieux — douze, toutes traitées au cabinet.",
        "intro":
            "Le cabinet ne se déclare ni généraliste ni "
            "spécialiste. Les matières sont le champ du "
            "contentieux : ce qui détermine la juridiction et "
            "le degré de juridiction. Une matière entre au "
            "cabinet quand la preuve est versable au dossier "
            "et que la jurisprudence est lisible en cinq lignes.",
        "primary_cta":  "Soumettez un avis préliminaire",

        "svc_duration_label": "For · degré",
        "svc_leader_label":   "Plaidoyer",

        "services": [
            {
                "num":   "01",
                "title": "Pénal-fiscal",
                "blurb":
                    "Plaidoyer dans tous les degrés du procès "
                    "pénal-fiscal pour entrepreneurs, "
                    "administrateurs et professionnels libéraux. "
                    "Défense en procédure pour omission de "
                    "déclaration, omission de versement, "
                    "soustraction frauduleuse au paiement des "
                    "impôts au sens du D.lgs. 74/2000.",
                "scope": [
                    "Défense de prévenus et parties civiles",
                    "Procédures spéciales et plaider-coupable ex art. 444 c.p.p.",
                    "Pourvois en cassation pénale (sez. III + sez. V)",
                    "Coordination avec consultants fiscaux de partie",
                ],
                "duration": "Tribunal · App. · Cassation",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "02",
                "title": "Civil contractuel",
                "blurb":
                    "Contentieux civil sur contrats commerciaux, "
                    "fourniture, agence, distribution, "
                    "prestation. Actions en inexécution, "
                    "résolution contractuelle, dommages-intérêts "
                    "et actions en nullité pour vice du "
                    "consentement.",
                "scope": [
                    "Causes au-dessus de € 50.000",
                    "Assignations et conclusions autorisées",
                    "Mesures d'urgence ex art. 700 c.p.c.",
                    "Pourvois en cassation civile",
                ],
                "duration": "Tribunal · App. · Cassation",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "03",
                "title": "Administratif réglementaire",
                "blurb":
                    "Recours contre les actes des Autorités "
                    "indépendantes (AGCOM, AGCM, Garante "
                    "Privacy, ANAC). Contestation de décisions "
                    "de sanction, de refus, d'inhibition. "
                    "Plaidoyer en première instance TAR et en "
                    "appel devant le Conseil d'État.",
                "scope": [
                    "Recours au TAR Lombardia · sez. III · réglementaires",
                    "Appels au Conseil d'État · sez. VI",
                    "Conclusions de plaidoirie orale",
                    "Coordination avec consultants techniques de partie",
                ],
                "duration": "TAR · Cons. État",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "04",
                "title": "Contentieux bancaire",
                "blurb":
                    "Causes contre les établissements bancaires "
                    "pour anatocisme bancaire, usure, erreur de "
                    "déclaration à la Centrale des Risques, "
                    "contestation de contrats de prêt, leasing "
                    "et dérivés. Plaidoyer dans tous les degrés, "
                    "jusqu'à la Cassation civile.",
                "scope": [
                    "Expertises comptables et expertises de partie",
                    "Actions en restitution et en nullité de clauses",
                    "Pourvois en cassation civile sez. I + III",
                    "Coordination avec experts bancaires indépendants",
                ],
                "duration": "Trib. · App. · Cassation",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "05",
                "title": "Responsabilité professionnelle",
                "blurb":
                    "Actions en responsabilité contre conseils "
                    "fiscaux, avocats, médecins, professionnels "
                    "techniques. Plaidoyer tant pour la partie "
                    "lésée que pour le professionnel défendeur. "
                    "Matière en évolution jurisprudentielle "
                    "constante (cf. Cass. SS.UU. 2024).",
                "scope": [
                    "Actions en réparation contractuelle et extracontractuelle",
                    "Quantification du dommage selon la légitimité",
                    "Pourvois en cassation (y compris SS.UU.)",
                    "Conclusions techniques et reconstruction de la preuve",
                ],
                "duration": "Trib. · App. · Cassation · SS.UU.",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "06",
                "title": "Recouvrement complexe",
                "blurb":
                    "Recouvrement de créances commerciales "
                    "supérieures à € 50.000 · injonctions de "
                    "payer et oppositions correspondantes · "
                    "voies d'exécution mobilières et "
                    "immobilières · actions paulienne ordinaires "
                    "et faillite.",
                "scope": [
                    "Injonctions de payer et oppositions",
                    "Voies d'exécution auprès des tiers et actions paulienne",
                    "Saisies immobilières et mobilières",
                    "Coordination avec experts évaluateurs",
                ],
                "duration": "Trib. · Voies d'exécution",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "07",
                "title": "Droit des sociétés",
                "blurb":
                    "Actions en responsabilité contre "
                    "administrateurs, commissaires aux comptes "
                    "et directeurs généraux. Contestation de "
                    "résolutions d'assemblée et de conseil. "
                    "Pactes parasociaux, covenant breach. "
                    "Contentieux entre associés dans les "
                    "sociétés de capitaux.",
                "scope": [
                    "Actions ex artt. 2392-2395 c.c.",
                    "Contestations de résolutions ex art. 2377 c.c.",
                    "Causes devant le Tribunal des Entreprises",
                    "Pourvois en cassation civile sez. I",
                ],
                "duration": "Trib. impr. · App. · Cassation",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "08",
                "title": "Fiscal",
                "blurb":
                    "Recours contre les avis d'imposition de "
                    "l'Agenzia delle Entrate. Plaidoyer devant "
                    "les Cours de Justice Fiscale en premier et "
                    "second degré. Pourvois en cassation en "
                    "matière fiscale.",
                "scope": [
                    "Avis de paiement et inscriptions au rôle",
                    "Avis d'imposition et de rectification",
                    "Conclusions de contradictoire préalable",
                    "Pourvois ex art. 360 c.p.c. n. 3",
                ],
                "duration": "CGT 1° · CGT 2° · Cassation",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "09",
                "title": "Voies d'exécution",
                "blurb":
                    "Procédures d'exécution mobilières, "
                    "immobilières, auprès des tiers. "
                    "Oppositions à l'exécution et aux actes "
                    "exécutifs. Plaidoyer des créanciers "
                    "poursuivants et des débiteurs saisis.",
                "scope": [
                    "Saisies immobilières et procédures de vente",
                    "Oppositions ex artt. 615, 617, 619 c.p.c.",
                    "Distribution du produit",
                    "Coordination avec gardiens judiciaires",
                ],
                "duration": "Trib. exécutions",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "10",
                "title": "Travail complexe",
                "blurb":
                    "Contentieux du travail à haute "
                    "complexité — licenciements de cadres "
                    "dirigeants, harcèlement, déclassement, "
                    "rémunération variable contestée. Cas avec "
                    "implications sociétaires ou réglementaires. "
                    "PAS de contentieux individuel standard.",
                "scope": [
                    "Licenciements ex artt. 18 St. lav. + Jobs Act",
                    "Actions en réparation pour harcèlement et déclassement",
                    "Clauses de non-concurrence et recours conservatoires",
                    "Pourvois en cassation civile sez. travail",
                ],
                "duration": "Trib. trav. · App. · Cassation",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "11",
                "title": "Expert judiciaire",
                "blurb":
                    "Le cabinet est inscrit à l'Albo CTU forense "
                    "du Tribunale di Milano (section "
                    "contentieux civil). Expertises judiciaires "
                    "sur contentieux des sociétés, évaluations "
                    "d'entreprise contestées et responsabilité "
                    "comptable.",
                "scope": [
                    "CTU sur contentieux des sociétés",
                    "Évaluations d'entreprise contestées",
                    "Responsabilité comptable et financière",
                    "Rapports d'expertise sur mandat du juge",
                ],
                "duration": "CTU · Trib. Milano",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "12",
                "title": "Médiation ENCA",
                "blurb":
                    "Le cabinet est inscrit section médiateurs "
                    "ENCA (Conseil National Conciliation "
                    "Avocats). Médiation civile obligatoire "
                    "dans les matières de la loi, médiation "
                    "déléguée, et procédures arbitrales en "
                    "convention d'arbitrage rituel.",
                "scope": [
                    "Médiation civile obligatoire ex D.lgs. 28/2010",
                    "Médiations déléguées par le juge",
                    "Arbitrages rituels ex artt. 806 ss. c.p.c.",
                    "Procès-verbaux d'accord et de clôture motivée",
                ],
                "duration": "ENCA · arbitrage",
                "leader":   "Chiara Bevilacqua",
            },
        ],

        "process_label":   "MÉTHODE · QUATRE SAISONS DU PLAIDOYER",
        "process_heading": "Quatre phases, une seule séquence forensique.",
        "process": [
            ("01", "Juridiction",
             "La matière qui existe déjà se lit comme un "
             "dossier. For, degré, exceptions préliminaires. "
             "La juridiction est la première forme de respect "
             "et dure typiquement cinq jours de screening."),
            ("02", "Fond",
             "Objet du contentieux, parties en cause, "
             "fourchette de valeur, urgence procédurale, "
             "preuve préliminaire versable. Le fond est le "
             "cadre du plaidoyer : il définit quel mémoire "
             "s'écrit et lequel non."),
            ("03", "Décision",
             "Le mémoire s'écrit comme une thèse citable — "
             "quel principe il invoque, quelle orientation il "
             "confirme, quelle preuve il verse au dossier. "
             "Cinq lignes dans lesquelles la décision doit "
             "pouvoir se raconter."),
            ("04", "Dépôt",
             "Audience par audience, degré par degré, jusqu'au "
             "prononcé. Toutes les décisions obtenues restent "
             "écrites au répertoire interne · publiées dans "
             "les soixante jours du dépôt."),
        ],

        "cta_heading":   "Quelle matière convient à votre contentieux ?",
        "cta_intro":
            "Si la matière n'est pas claire, écrivez-nous une "
            "brève description de l'objet du contentieux et du "
            "degré de juridiction actuel. Nous vous "
            "indiquerons la matière juste sous cinq jours "
            "ouvrés · sous quarante-huit heures si l'urgence "
            "est procédurale (délai en cours · audience fixée).",
        "cta_primary":   "Soumettez un avis préliminaire",
        "cta_primary_href": "contatti",
    },

    "contenzioso": {
        "eyebrow":  "CONTENTIEUX · CHRONOLOGIE 1995-2024",
        "headline":
            "Les décisions citées — la <em>chronologie</em> du plaidoyer · 1995–2024.",
        "intro":
            "Quatorze entrées publiées par le Foro Italiano et "
            "la Giurisprudenza Italiana, plus les autres "
            "contentieux sélectionnés. Toutes inscrites au "
            "répertoire interne dans les soixante jours du "
            "dépôt.",
        "primary_cta":  "Soumettez un avis préliminaire",

        "cases_label": "Quatre décisions représentatives · en détail",
        "cases_intro":
            "Le cabinet inscrit chaque décision obtenue — "
            "gagnée ou perdue — au répertoire interne dans les "
            "soixante jours du dépôt. Les quatre décisions "
            "mises en évidence ci-dessous sont celles "
            "choisies éditorialement pour illustrer la méthode "
            "du cabinet : une pour les Sezioni Unite de la "
            "Cassation, une pour la cassation civile section "
            "simple, une pour la juridiction administrative, "
            "et une pour le contentieux fiscal en appel.",

        "cta_heading":   "Une cause similaire à la vôtre ?",
        "cta_intro":
            "Les dossiers complets (mémoires, pourvois, "
            "défenses, documentation du jugement, note à "
            "décision) sont disponibles au cabinet sur demande "
            "motivée. La consultation est gratuite au sens du "
            "Codice Deontologico Forense ; la copie intégrale "
            "du répertoire interne s'obtient à couverture des "
            "frais d'impression.",
        "cta_primary":   "Soumettez un avis préliminaire",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "cass-ssuu-responsabilita-consulente-fiscale-2024",
            "title":
                "Sezioni Unite — la responsabilité "
                "professionnelle du conseil fiscal, relue comme "
                "obligation de résultat versée à la preuve "
                "préliminaire",
            "category": "Responsabilité professionnelle",
            "year":     "2024 · dépôt avril",
            "duration": "Cassazione SS.UU. · degré de légitimité · cassée sans renvoi",
            "client_code":
                "Cassazione · Sezioni Unite civiles · saisine "
                "de la troisième chambre civile · demandeur "
                "principal · partie adverse : conseil fiscal "
                "défendeur · matière : responsabilité "
                "professionnelle · obligation de résultat "
                "circonscrit vs obligation de moyens.",
            "lead":
                "Le litige a été remis à la connaissance des "
                "Sezioni Unite de la Cour de Cassation par la "
                "troisième chambre civile, en raison du "
                "conflit entre deux orientations de légitimité "
                "sur la qualification de l'obligation du "
                "conseil fiscal au regard du signalement "
                "diligent d'un délai d'impugnation fiscale.",
            "sections": [
                {
                    "label": "La juridiction",
                    "heading": "Saisine de la troisième chambre civile aux Sezioni Unite",
                    "body":
                        "La procédure a été remise à la "
                        "connaissance des Sezioni Unite de la "
                        "Cour de Cassation par la troisième "
                        "chambre civile, par ordonnance "
                        "interlocutoire de septembre 2023, en "
                        "raison du conflit entre deux "
                        "orientations de légitimité sur la "
                        "qualification de l'obligation du "
                        "conseil fiscal. La première "
                        "orientation (dominante entre 2014 et "
                        "2020) qualifiait l'obligation comme "
                        "obligation de moyens, avec "
                        "conséquemment la charge de la preuve "
                        "du lien causal sur le client ; la "
                        "seconde (émergente depuis 2021) "
                        "qualifiait l'obligation comme "
                        "obligation de résultat circonscrit.",
                },
                {
                    "label": "L'argument soutenu",
                    "heading": "Obligation de résultat versée à la preuve préliminaire",
                    "body":
                        "Le cabinet, en qualité de plaideur du "
                        "client demandeur, a soutenu "
                        "l'orientation de l'obligation de "
                        "résultat circonscrit, invoquant le "
                        "principe de prévisibilité de la preuve "
                        "préliminaire au moment de l'acceptation "
                        "de la mission professionnelle. Le "
                        "mémoire en défense a rappelé "
                        "l'orientation de la cassation civile "
                        "sez. III de 2022 sur les critères de "
                        "prévisibilité du délai d'impugnation "
                        "en matière fiscale, et a proposé la "
                        "relecture de l'obligation comme "
                        "responsabilité versée à la diligence "
                        "qualifiée requise du conseil.",
                },
                {
                    "label": "L'issue",
                    "heading": "Cassée sans renvoi · entrée n° 14",
                    "body":
                        "Les Sezioni Unite ont accueilli la "
                        "reconstruction soutenue par le "
                        "cabinet, confirmant l'orientation de "
                        "l'obligation de résultat circonscrit "
                        "et la versant au critère de "
                        "prévisibilité de la preuve "
                        "préliminaire. La décision a cassé "
                        "sans renvoi la décision de second "
                        "degré de la Cour d'Appel, déclarant "
                        "la responsabilité du conseil fiscal "
                        "défendeur et quantifiant le dommage "
                        "selon la jurisprudence de légitimité "
                        "consolidée. L'entrée a été publiée "
                        "par le Foro Italiano (entrée n° 14 "
                        "du répertoire interne du cabinet).",
                },
            ],
            "kpi": [
                ("SS.UU.",       "Sezioni Unite civiles"),
                ("avril 2024",   "dépôt décision"),
                ("cassée",       "sans renvoi"),
                ("entrée 14",    "Foro Italiano"),
            ],
            "lead_partner": "Lorenzo Marchetti · Studio Founder",
            "team":
                "Avocat fondateur + 1 associée · rédaction du "
                "pourvoi, défense et mémoire en vue de "
                "l'audience devant les Sezioni Unite",
            "next_label":   "Chronologie suivante",
        },
        {
            "slug":     "cass-civ-iii-anatocismo-bancario-2023",
            "title":
                "Cassation civile sez. III — anatocisme "
                "bancaire et charge de la preuve dans la "
                "jurisprudence de légitimité",
            "category": "Contentieux bancaire",
            "year":     "2023 · dépôt octobre",
            "duration": "Cass. civ. III · degré de légitimité · cassée avec renvoi",
            "client_code":
                "Cassazione · troisième chambre civile · "
                "demandeur · partie adverse : établissement "
                "bancaire défendeur · matière : anatocisme "
                "bancaire · charge probatoire du lien causal "
                "sur l'établissement.",
            "lead":
                "La procédure de premier et second degré avait "
                "rejeté la demande du client bancaire en "
                "remboursement des intérêts anatocistiques. "
                "Le cabinet a formé un pourvoi en cassation, "
                "soutenant l'attribution de la charge "
                "probatoire à l'établissement de crédit.",
            "sections": [
                {
                    "label": "Les degrés précédents",
                    "heading": "Tribunal de Milan section entreprises et Cour d'Appel de Milan",
                    "body":
                        "La procédure de premier degré devant "
                        "le Tribunal de Milan section "
                        "entreprises et celle de second degré "
                        "devant la Cour d'Appel de Milan "
                        "avaient rejeté la demande du client "
                        "bancaire en remboursement d'intérêts "
                        "anatocistiques perçus sur un compte "
                        "courant entre 2003 et 2014, au motif "
                        "que le client n'avait pas fourni de "
                        "preuve spécifique de la "
                        "capitalisation illégale.",
                },
                {
                    "label": "L'argument soutenu",
                    "heading": "Charge probatoire versée à l'établissement bancaire",
                    "body":
                        "Le cabinet a formé un pourvoi en "
                        "cassation, soutenant l'attribution de "
                        "la charge probatoire du lien causal à "
                        "l'établissement bancaire, "
                        "conformément à l'orientation de "
                        "légitimité consolidée par la "
                        "cassation civile sez. I de 2014 et "
                        "par les Sezioni Unite de 2018. Le "
                        "pourvoi a articulé la relecture de la "
                        "discipline de l'anatocisme bancaire "
                        "dans le cadre de l'asymétrie "
                        "d'information entre établissement de "
                        "crédit et client titulaire de "
                        "compte.",
                },
                {
                    "label": "L'issue",
                    "heading": "Cassée avec renvoi · entrée n° 11",
                    "body":
                        "La cassation civile sez. III a cassé "
                        "la décision d'appel avec renvoi à la "
                        "Cour d'Appel de Milan en composition "
                        "différente, accueillant l'orientation "
                        "soutenue par le cabinet. La "
                        "procédure de renvoi a été ordonnée "
                        "sous le principe de légitimité "
                        "conforme. L'entrée a été inscrite au "
                        "répertoire interne (n° 11) et est "
                        "en attente de publication externe.",
                },
            ],
            "kpi": [
                ("Cass. III",      "section simple"),
                ("octobre 2023",   "dépôt décision"),
                ("cassée",         "avec renvoi"),
                ("entrée 11",      "répertoire interne"),
            ],
            "lead_partner": "Lorenzo Marchetti · Studio Founder",
            "team":
                "Avocat fondateur + 1 associée · pourvoi en "
                "cassation, mémoire en défense et conclusions "
                "déposées en vue de l'audience · soutien "
                "expert bancaire indépendant",
            "next_label":   "Chronologie suivante",
        },
        {
            "slug":     "tar-lombardia-agcom-proporzionalita-2022",
            "title":
                "TAR Lombardia — annulation d'une sanction "
                "AGCOM et le principe de proportionnalité",
            "category": "Administratif réglementaire",
            "year":     "2022 · dépôt avril",
            "duration": "TAR Lombardia · premier degré · annulation intégrale",
            "client_code":
                "TAR Lombardia · section III · demandeur · "
                "partie adverse : AGCOM · matière : "
                "administratif réglementaire · sanction "
                "pécuniaire · principe de proportionnalité ex "
                "Cons. État sec. VI 2019.",
            "lead":
                "Le cabinet a formé un recours au TAR "
                "Lombardia pour l'annulation d'une sanction "
                "AGCOM infligée à un opérateur de "
                "communications électroniques pour "
                "prétendue violation des règles sur la "
                "transparence des offres commerciales.",
            "sections": [
                {
                    "label": "L'acte attaqué",
                    "heading": "Sanction AGCOM ex art. 98 D.lgs. 259/2003",
                    "body":
                        "Le cabinet a formé un recours au TAR "
                        "Lombardia pour l'annulation d'une "
                        "sanction AGCOM infligée à un "
                        "opérateur de communications "
                        "électroniques pour prétendue "
                        "violation des règles sur la "
                        "transparence des offres "
                        "commerciales. La sanction avait été "
                        "infligée à l'issue d'une phase "
                        "instructoire avec contradictoire "
                        "procédural de six mois.",
                },
                {
                    "label": "Les motifs du recours",
                    "heading": "Excès de pouvoir et violation du principe de proportionnalité",
                    "body":
                        "Le recours s'est fondé sur deux "
                        "moyens principaux. Le premier, pour "
                        "excès de pouvoir sous l'angle du "
                        "défaut d'instruction : l'Autorité "
                        "n'avait pas acquis certains éléments "
                        "probatoires produits par l'opérateur "
                        "en contradictoire procédural. Le "
                        "second, pour violation du principe "
                        "de proportionnalité de la sanction "
                        "administrative pécuniaire, à la "
                        "lumière de l'orientation du Conseil "
                        "d'État sec. VI de 2019 sur les "
                        "critères de détermination de la "
                        "sanction tenant compte de la gravité "
                        "de la conduite, du comportement de "
                        "l'agent et de sa capacité "
                        "contributive.",
                },
                {
                    "label": "L'issue",
                    "heading": "Annulation intégrale · entrée n° 9",
                    "body":
                        "Le TAR Lombardia a accueilli le "
                        "recours, annulant intégralement la "
                        "sanction pour violation du principe "
                        "de proportionnalité. La décision n'a "
                        "pas été frappée d'appel par AGCOM. "
                        "L'entrée a été inscrite au "
                        "répertoire interne (n° 9) et a "
                        "contribué à la consolidation de "
                        "l'orientation sur la "
                        "proportionnalité des sanctions "
                        "réglementaires.",
                },
            ],
            "kpi": [
                ("TAR Lomb.",      "section III"),
                ("avril 2022",     "dépôt décision"),
                ("annulée",        "intégralement"),
                ("entrée 9",       "répertoire interne"),
            ],
            "lead_partner": "Tommaso De Luca · Avocat associé",
            "team":
                "Avocat associé + avocat fondateur · recours "
                "introductif, mémoire de réplique aux "
                "conclusions adverses AGCOM et conclusions de "
                "plaidoirie orale",
            "next_label":   "Chronologie suivante",
        },
        {
            "slug":     "appello-milano-art-36bis-dpr-600-1973-2021",
            "title":
                "Cour d'Appel de Milan section fiscale — "
                "l'art. 36-bis D.P.R. 600/1973 et le périmètre "
                "du litige fiscal",
            "category": "Fiscal",
            "year":     "2021 · dépôt septembre",
            "duration": "App. Milano trib. · second degré · infirmée en appel",
            "client_code":
                "Corte d'Appello Milano · section fiscale · "
                "appelant · partie adverse : Agenzia delle "
                "Entrate · matière : fiscal · liquidation "
                "automatisée ex art. 36-bis D.P.R. 600/1973 · "
                "périmètre contributif restrictif.",
            "lead":
                "La procédure de premier degré devant la "
                "Commission Fiscale Provinciale de Milan "
                "s'était conclue par le rejet du recours du "
                "contribuable contre un avis de paiement "
                "émis à la suite d'un contrôle automatisé ex "
                "art. 36-bis D.P.R. 600/1973.",
            "sections": [
                {
                    "label": "Le premier degré",
                    "heading": "Commission Fiscale Provinciale de Milan · rejet du recours",
                    "body":
                        "La procédure de premier degré devant "
                        "la Commission Fiscale Provinciale de "
                        "Milan s'était conclue par le rejet "
                        "du recours du contribuable contre un "
                        "avis de paiement émis à la suite "
                        "d'un contrôle automatisé ex art. "
                        "36-bis D.P.R. 600/1973. La "
                        "Commission avait jugé suffisant le "
                        "contrôle purement formel pour fonder "
                        "la prétention fiscale.",
                },
                {
                    "label": "L'argument soutenu",
                    "heading": "Interprétation restrictive de l'art. 36-bis D.P.R. 600/1973",
                    "body":
                        "Le cabinet a interjeté appel, "
                        "soutenant l'interprétation "
                        "restrictive de l'art. 36-bis qui "
                        "limite le contrôle automatisé à une "
                        "liquidation purement arithmétique "
                        "des impôts déclarés, sans possibilité "
                        "de rectification du contenu "
                        "substantiel de la déclaration "
                        "(orientation de la cassation fiscale "
                        "de 2017 et de 2019). Le mémoire en "
                        "défense a articulé la relecture du "
                        "périmètre du litige fiscal dans le "
                        "cadre de la répartition entre "
                        "contrôle automatisé et "
                        "rectification substantielle.",
                },
                {
                    "label": "L'issue",
                    "heading": "Infirmée en appel · entrée n° 7",
                    "body":
                        "La Cour d'Appel a accueilli "
                        "intégralement l'appel, annulant "
                        "l'avis de paiement et condamnant "
                        "l'Agenzia delle Entrate aux dépens. "
                        "La décision n'a pas été frappée de "
                        "pourvoi en Cassation et a contribué "
                        "à la consolidation de l'orientation "
                        "restrictive. Entrée n° 7 du "
                        "répertoire interne.",
                },
            ],
            "kpi": [
                ("App. Milan",      "section fiscale"),
                ("septembre 2021",  "dépôt décision"),
                ("infirmée",        "en appel"),
                ("entrée 7",        "répertoire interne"),
            ],
            "lead_partner": "Tommaso De Luca · Avocat associé",
            "team":
                "Avocat associé + avocat fondateur · acte "
                "d'appel, mémoire de réplique à l'Agenzia "
                "delle Entrate et conclusions de plaidoirie "
                "orale",
            "next_label":   "Chronologie suivante",
        },
    ],

    "contatti": {
        "eyebrow":  "SOUMETTEZ UN AVIS PRÉLIMINAIRE",
        "headline": "Soumettez un <em>avis</em> préliminaire — la première page du plaidoyer.",
        "intro":
            "Le cabinet répond sous cinq jours ouvrés · sous "
            "quarante-huit heures si l'urgence est "
            "procédurale (délai en cours · audience fixée).",
        "primary_cta":  "Soumettez un avis préliminaire",

        "form_label":   "AVIS PRÉLIMINAIRE",
        "form_heading": "Remplissez la fiche de screening",
        "form_intro":
            "L'avis préliminaire est la première page du "
            "plaidoyer : le cabinet lit l'objet du "
            "contentieux, le degré de juridiction actuel, la "
            "juridiction, la fourchette de valeur et "
            "l'urgence, et restitue une évaluation de la "
            "versabilité de la preuve au dossier et de la "
            "lisibilité de la jurisprudence en cinq lignes. "
            "L'avis N'EST PAS un mandat défensif · N'EST PAS "
            "un devis à la consommation · N'EST PAS un appel "
            "de découverte. C'est un screening technique, "
            "motivé par écrit, à partir duquel décider "
            "ensemble s'il convient d'ouvrir le dossier. Si "
            "l'avis est négatif, la note motivée est tout "
            "de même remise gratuitement.",

        "form_fields": [
            {"name": "name",      "label": "Prénom",   "type": "text", "required": True,
             "placeholder": "Ex. Marc",
             "helper": "Prénom uniquement, merci."},
            {"name": "surname",   "label": "Nom",      "type": "text", "required": True,
             "placeholder": "Ex. Bianchi",
             "helper": "Tel qu'il figure dans les documents du commettant."},
            {"name": "email",     "label": "Email",    "type": "email", "required": True,
             "placeholder": "marc@domaine.fr",
             "helper": "Une boîte qui recevra la note motivée fiduciaire."},
            {"name": "phone",     "label": "Téléphone", "type": "tel", "required": False,
             "placeholder": "+39 ...",
             "helper": "Ligne directe pour le premier contact. Facultatif."},
            {"name": "oggetto", "label": "Objet du contentieux",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Décrivez en 5-10 lignes l'objet du "
                 "contentieux, les parties, le point en "
                 "discussion. Il n'est pas nécessaire d'être "
                 "complet · une description synthétique "
                 "suffit.",
             "helper":
                 "De quoi comprendre si la matière est "
                 "versable au dossier. N'attachez pas encore "
                 "le dossier complet · les chiffres et autres "
                 "données se discutent en première audience."},
            {"name": "grado", "label": "Degré de juridiction actuel", "type": "select", "required": True,
             "options": [
                 "premier degré (Tribunal · CGT · TAR)",
                 "appel (Cour d'Appel · CGT 2° · Cons. État)",
                 "Cassation (en cours ou à proposer)",
                 "procédure administrative non engagée",
                 "procédure non encore engagée (avis préventif)",
             ],
             "helper": "Le degré dans lequel se trouve actuellement la cause."},
            {"name": "controparte", "label": "Type de partie adverse", "type": "text", "required": True,
             "placeholder":
                 "Ex. établissement bancaire · entité "
                 "publique · partie adverse commerciale · "
                 "administration publique · privé",
             "helper":
                 "Il n'est pas nécessaire de nommer la "
                 "partie adverse spécifique à ce stade · "
                 "uniquement la typologie."},
            {"name": "valore", "label": "Fourchette de valeur", "type": "select", "required": True,
             "options": [
                 "jusqu'à € 50.000",
                 "€ 50.000 — € 250.000",
                 "€ 250.000 — € 1 M",
                 "€ 1 M — € 5 M",
                 "au-delà de € 5 M",
             ],
             "helper": "La valeur estimée du litige."},
            {"name": "urgenza", "label": "Urgence procédurale", "type": "select", "required": True,
             "options": [
                 "ordinaire (aucun délai en cours)",
                 "qualifiée (délai sous 30 jours)",
                 "procédurale (délai sous 7 jours)",
             ],
             "helper":
                 "L'urgence détermine la cadence de réponse "
                 "du cabinet · 5 jours ouvrés · 48 heures "
                 "si procédurale."},
            {"name": "giurisdizione", "label": "Juridiction", "type": "select", "required": True,
             "options": [
                 "Italie (for italien)",
                 "Union Européenne (CJUE · TUE)",
                 "extra-UE (avec éléments de droit international privé)",
             ],
             "helper": "La juridiction est la première forme de respect."},
        ],

        "form_sections": [
            {"num": "01", "title": "Référent",
             "meta": "La personne qui signera la procuration ad litem, une fois le mandat ouvert.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Objet du contentieux",
             "meta": "L'objet est le premier texte du dossier. Cinq à dix lignes suffisent.",
             "fields": ["oggetto"]},
            {"num": "03", "title": "Cadre procédural",
             "meta": "Degré · partie adverse · valeur · urgence · juridiction.",
             "fields": ["grado", "controparte", "valore", "urgenza", "giurisdizione"]},
        ],

        "form_submit_label": "Soumettre l'avis préliminaire",
        "form_submit_note":
            "Le cabinet lira la fiche sous cinq jours ouvrés "
            "· sous quarante-huit heures si l'urgence est "
            "procédurale · et répondra par une note motivée "
            "à l'adresse indiquée. Aucun BDR externe, aucune "
            "automatisation de séquence — le premier contact "
            "se fait avec l'avocat.",
        "form_consent":
            "Je consens au traitement des données "
            "personnelles au sens du Reg. UE 679/2016 et du "
            "D.lgs. 196/2003. Les données sont traitées aux "
            "seules fins de l'évaluation de l'avis · "
            "conservées au cabinet de Via Borgonuovo avec "
            "accès limité aux trois avocats. Je suis informé "
            "du canal whistleblowing (D.lgs. 24/2023) actif "
            "au cabinet. Le cabinet respecte le secret "
            "professionnel au sens de l'art. 622 c.p. et du "
            "Codice Deontologico Forense.",

        "office_address_label": "Adresse",
        "office_area_label":    "Quartier",
        "office_phone_label":   "Téléphone",
        "office_email_label":   "Email",

        "offices_label":   "LE CABINET",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Cabinet unique · Foro di Milano",
                "address": "Via Borgonuovo 14 · 20121",
                "area":    "Brera · proche du Tribunale di Milano",
                "phone":   "+39 02 7634 8210",
                "email":   "parere@causa.legal",
            },
        ],

        "channels_label": "CANAUX DIRECTS",
        "channels": [
            ("Secrétariat du cabinet",                   "+39 02 7634 8210",                "Lun – Ven · 09:00 – 18:00"),
            ("Email pour avis préliminaires",            "parere@causa.legal",              "Réponse sous 5 jours"),
            ("PEC pour actes déjà dans les délais",      "causa.legale@pec.causa.legal",    "Actes urgents · sous 24 heures"),
            ("Whistleblowing (D.lgs. 24/2023)",          "whistleblowing@causa.legal",      "Canal interne · chiffré"),
        ],

        "footnote":
            "Causa respecte le secret professionnel au sens "
            "de l'art. 622 c.p. et du Codice Deontologico "
            "Forense. La consultation du site ne constitue "
            "pas un mandat. Le cabinet ne répond pas aux "
            "demandes anonymes et ne délivre pas d'avis "
            "préliminaires par écrit sans une fiche de "
            "screening remplie. Les informations sur les "
            "honoraires sont illustrées en première audience, "
            "selon les tarifs forensiques minimaux et les "
            "paramètres D.M. 55/2014. Le canal "
            "whistleblowing est géré au sens du D.lgs. "
            "24/2023 et est accessible aux collaborateurs, "
            "associés et secrétariat.",
    },
}
