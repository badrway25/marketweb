"""Atto · Studio Notarile Conti–Sironi–Verri · French content tree.

Wave 1 Pass-4 (T48 · workflow C · multilingual handshake). Mirrors the
IT tree `ATTO_CONTENT_IT` in `template_content_atto.py` shape-for-shape
— same top-level keys, same nested keys, same tuple arities, same
field names. Generated through the 4-sub-agent parallel-translator
workflow C, voice anchor preserved verbatim-in-translation across all
load-bearing surfaces.

Voice anchor: `atto pubblico` → `acte authentique` (the public-faith
deed in the French notarial tradition · the official term used by the
Conseil Supérieur du Notariat for the document carrying authenticité
publique). Italian honorific `Notaio dott./dott.ssa` becomes the
French notarial honorific `Me` (Maître), preserved before given/family
names which remain in their Italian form (Italian civil-status data).

Register: institutional-notarial French · vous · classical Parisian
prose modelled on the Conseil Supérieur du Notariat communications
and the patrimonial-law columns of Les Echos Patrimoine. Espaces
insécables before `:`, `;`, `!`, `?` and around `«»` consistently.

Non-localizable: phone, email, prices in €, press outlets (Italian
notarial reviews kept verbatim), photo URLs, Italian legal citations
(art. X c.c. · L. 89/1913 · Reg. UE 650/2012), the brand name
`Studio Notarile Conti–Sironi–Verri`, and the street component of
the address. Only the city tail `Milano` → `Milan`.
"""
from __future__ import annotations

from typing import Any


# ─── Imagery — verbatim from IT tree (same Pexels URLs) ──────────────────
_NOTARY_HERO = "https://images.pexels.com/photos/6077091/pexels-photo-6077091.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop"
_NOTARY_SIGNING = "https://images.pexels.com/photos/5235410/pexels-photo-5235410.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
_NOTARY_PORTRAIT_F1 = "https://images.pexels.com/photos/6077124/pexels-photo-6077124.jpeg?auto=compress&cs=tinysrgb&w=800&h=1200&fit=crop"
_NOTARY_PORTRAIT_M = "https://images.pexels.com/photos/7841445/pexels-photo-7841445.jpeg?auto=compress&cs=tinysrgb&w=800&h=1200&fit=crop"
_NOTARY_DETAIL = "https://images.pexels.com/photos/5669602/pexels-photo-5669602.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop"
_NOTARY_AMBIENT = "https://images.pexels.com/photos/1842502/pexels-photo-1842502.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop"


ATTO_CONTENT_FR: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "L'Étude",            "kind": "home"},
        {"slug": "studio",        "label": "À propos",           "kind": "about"},
        {"slug": "pratiche",      "label": "Domaines d'actes",   "kind": "services"},
        {"slug": "avvocati",      "label": "Les Notaires",       "kind": "team"},
        {"slug": "pubblicazioni", "label": "Publications",       "kind": "blog_list"},
        {"slug": "contatti",      "label": "Contact",            "kind": "contact"},
    ],

    # ─── SITE — chrome rendered by _base.html ──────────────────────────
    "site": {
        "logo_initial":  "CSV",
        "logo_word":     "Studio Notarile Conti–Sironi–Verri",
        "tag":           "Chambre des Notaires de Milan · depuis 2007",
        "phone":         "+39 02 7641 1898",
        "email":         "studio@notaiconti-sironi-verri.it",
        "address":       "Via Manin 12 · 20121 Milan",
        "hours_compact": "Lundi – Vendredi · 09 h 00 – 18 h 30",
        "hours_footer_rows": [
            "Samedi · sur rendez-vous pour actes urgents",
            "Dimanche · fermé",
        ],
        "license":
            "Notaires inscrits au tableau de la Chambre des Notaires "
            "de Milan · Conseil Notarial des Circonscriptions Réunies "
            "de Milan, Busto Arsizio, Lodi, Monza et Varèse · L. 89/1913",
        "nav_cta":       "Demandez un premier rendez-vous",
        "footer_intro":
            "Studio Notarile Conti–Sironi–Verri — dix-sept ans "
            "d'actes authentiques au service des familles, des "
            "entreprises et des opérateurs de la Chambre des Notaires "
            "de Milan. Trois notaires associés, une seule signature "
            "pour la force probante.",
        "foot_studio":  "L'étude",
        "foot_pages":   "Pages",
        "foot_contact": "Contact",
        "foot_offices": "Siège",
        "offices_footer_rows": [
            "Milan · via Manin 12",
            "Chambre des Notaires de Milan",
        ],

        # Cross-page meta labels (lifted from skin for locale support).
        "case_practice_label":  "Type d'acte",
        "case_year_label":      "Année",
        "case_outcome_label":   "Issue",
        "case_lead_label":      "Notaire instrumentaire",
    },

    # ════════════════════════════════════════════════════════════════════
    # HOME (studio)
    # ════════════════════════════════════════════════════════════════════
    "home": {
        "eyebrow":  "Studio Notarile Conti–Sironi–Verri · Milan · depuis 2007",
        "headline": "Dix-sept ans d'<em>acte authentique</em>, une signature qui fait foi en droit.",
        "intro":
            "L'étude assiste les particuliers, les familles et les "
            "entreprises dans la rédaction de l'acte notarié — actes "
            "de vente immobilière, successions, actes de société, "
            "donations, prêts hypothécaires, procurations et "
            "testaments. Chaque acte authentique est rédigé "
            "personnellement par l'un des trois notaires associés, "
            "inscrits au tableau de la Chambre des Notaires de Milan, "
            "dans le plein exercice de la fonction d'officier public "
            "et de la force probante que la loi lui reconnaît.",
        "primary_cta":    "Demandez un premier rendez-vous",
        "primary_href":   "contatti",
        "secondary_cta":  "Domaines d'actes",
        "secondary_href": "pratiche",

        # Hero — split-ledger-monogram silhouette
        "hero_credit_left":  ("Notaire fondateur",  "Me M. B. Conti"),
        "hero_credit_right": ("Chambre",            "Milan · inscription au tableau"),
        "hero_meta_strip": [
            ("Siège de l'étude",     "Milan · via Manin 12"),
            ("Notaires associés",    "Trois · inscrits depuis 2007/2014/2021"),
            ("Actes instrumentés",   "4 200+ · IT · EN · FR"),
        ],

        # Practice-area ledger — 4 rows on home, full 7 on /pratiche
        "practice_label":   "Domaines d'actes",
        "practice_heading": "Sept types d'<em>acte</em>, une seule force probante.",
        "practice_intro":
            "L'étude traite les principaux types d'acte notarié "
            "prévus par l'ordre juridique italien. Chaque acte "
            "authentique est rédigé personnellement par un notaire "
            "de l'étude, lu au comparant dans la langue choisie "
            "(italien, anglais ou français) et inscrit au répertoire "
            "au sens de la Loi Notariale (L. 89/1913).",
        "practice": [
            ("01", "Actes de vente immobilière",
             "Rédaction de l'acte notarié pour la vente de biens "
             "immobiliers résidentiels, commerciaux et de production. "
             "Les vérifications cadastrales, les inspections "
             "hypothécaires et le contrôle de la régularité "
             "urbanistique précèdent la signature. L'acte est reçu "
             "en la forme authentique, avec la force probante "
             "reconnue par l'art. 2700 c.c."),
            ("02", "Successions et déclarations",
             "Ouverture de la succession, rédaction de la déclaration "
             "de succession, acceptation de l'hérédité sous bénéfice "
             "d'inventaire, publication du testament olographe, "
             "renonciations et partages successoraux. Pour les "
             "successions transfrontalières s'applique le "
             "Reg. UE 650/2012."),
            ("03", "Actes de société et opérations extraordinaires",
             "Constitution de sociétés par acte authentique au sens "
             "des art. 2328 et 2463 c.c., modifications statutaires, "
             "procès-verbaux d'assemblée extraordinaire, fusions, "
             "scissions et transformations. L'étude suit la procédure "
             "complète, de la délibération au dépôt auprès du Registre "
             "des Entreprises."),
            ("04", "Prêts hypothécaires et garanties réelles",
             "Actes de prêt foncier et hypothécaire, constitution "
             "d'hypothèque volontaire, subrogations ex L. 40/2007, "
             "actes récognitifs et mainlevées. Coordination "
             "opérationnelle avec l'établissement prêteur pour la "
             "signature concomitante à l'acte de vente."),
        ],

        # Stats band — counter animation (notarial-institutional facts)
        "stats_label":   "Dix-sept ans de force probante",
        "stats_heading": "Les chiffres de l'étude",
        "stats": [
            ("3",      "notaires inscrits au tableau"),
            ("17",     "ans depuis la fondation"),
            ("4 200+", "actes instrumentés"),
            ("3",      "langues d'instrumentation (IT/EN/FR)"),
        ],

        # Partners portrait preview — 3 notai associati
        "partners_label":   "Les trois notaires",
        "partners_heading": "Trois notaires, une seule étude",
        "partners_intro":
            "L'étude est dirigée par trois notaires associés, "
            "chacun inscrit au tableau de la Chambre des Notaires "
            "de Milan et responsable de ses propres types d'acte. "
            "La signature est personnelle : le notaire qui reçoit "
            "le comparant est celui-là même qui rédige, lit et "
            "souscrit l'acte authentique en forme de répertoire.",
        "partners": [
            {
                "name":  "Me Maria Beatrice Conti",
                "role":  "Notaire fondateur · Actes de société · M&A internationales",
                "foro":  "Chambre des Notaires de Milan · inscrite au tableau depuis 2007",
                "bio":
                    "Fondatrice de l'étude, elle reçoit les actes de "
                    "constitution de société, les opérations "
                    "extraordinaires et les actes authentiques en "
                    "langue anglaise. Anciennement stagiaire dans "
                    "une étude notariale internationale de Milan "
                    "(2004-2006), elle traite en particulier les "
                    "M&A transfrontalières et les groupes "
                    "multinationaux avec filiale italienne.",
            },
            {
                "name":  "Me Andrea Sironi",
                "role":  "Notaire associé · Droit des sociétés · CTU au Tribunal de Milan",
                "foro":  "Chambre des Notaires de Milan · inscrit au tableau depuis 2014",
                "bio":
                    "Il traite les actes de société ordinaires et "
                    "extraordinaires, les pactes d'associés, les "
                    "financements d'associés et les opérations en "
                    "capital. CTU auprès du Tribunal de Milan pour "
                    "les expertises ex art. 2343 c.c. Membre de la "
                    "Commission Études du Conseil Notarial des "
                    "Circonscriptions Réunies de Milan.",
            },
            {
                "name":  "Me Stefano Verri",
                "role":  "Notaire associé · Immobilier · Successions",
                "foro":  "Chambre des Notaires de Milan · inscrit au tableau depuis 2021",
                "bio":
                    "Il reçoit les actes de vente immobilière, de "
                    "prêt hypothécaire, de donation et de succession. "
                    "Commissaire aux comptes inscrit au registre tenu "
                    "par le MEF, il coordonne les vérifications "
                    "urbanistiques et cadastrales préalables à la "
                    "signature. Anciennement stagiaire notarial à "
                    "Milan et Brescia (2017-2020).",
            },
        ],

        # Publications ribbon — riviste notarili (verbatim in Italian)
        "publications_label": "Publications et citations",
        "publications": [
            "NOTARIATO",
            "RIVISTA DEL NOTARIATO",
            "GUIDA AL DIRITTO",
            "CNN NOTIZIE",
            "RIVISTA TRIMESTRALE DI DIRITTO E PROCEDURA",
            "FEDERNOTAI",
        ],

        # Final CTA band — first-meeting (orientamento) ghost serif
        "cta_label":      "Premier rendez-vous d'orientation",
        "cta_heading":    "Trente minutes pour cadrer l'acte.",
        "cta_intro":
            "Le premier rendez-vous avec l'un des notaires de "
            "l'étude dure environ trente minutes, il est gratuit "
            "et sans engagement. On y discute le type d'acte, "
            "la liste des documents préliminaires à réunir et le "
            "barème des honoraires notariaux applicables. Aucune "
            "décision opérationnelle n'est demandée à ce stade.",
        "cta_primary":       "Demandez un premier rendez-vous",
        "cta_primary_href":  "contatti",
        "cta_secondary":     "Découvrez l'étude",
        "cta_secondary_href":"studio",
    },

    # ════════════════════════════════════════════════════════════════════
    # STUDIO (about) — storia, notai associati, valori, sede
    # ════════════════════════════════════════════════════════════════════
    "studio": {
        "eyebrow":  "L'étude · 2007 — 2026",
        "headline": "Dix-sept ans d'<em>acte authentique</em>, trois notaires associés.",
        "intro":
            "Le Studio Notarile Conti–Sironi–Verri naît à Milan en "
            "2007 de l'inscription au tableau de Me Maria Beatrice "
            "Conti, premier notaire de la circonscription à recevoir "
            "des actes authentiques en langue anglaise. L'étude a "
            "grandi par cooptation de confrères et compte aujourd'hui "
            "trois notaires associés et six collaborateurs à temps "
            "plein, tous opérationnels au siège unique de la "
            "via Manin 12.",

        # History timeline — sei date che hanno definito lo studio
        "history_label":   "Histoire de l'étude",
        "history_heading": "Six dates, dix-sept ans",
        "history_intro":
            "Six jalons qui marquent la trajectoire de l'étude — "
            "de la première inscription au tableau en 2007 à "
            "l'entrée du troisième notaire en 2021. Chaque étape "
            "a défini la composition collégiale de l'association "
            "et l'élargissement des types d'acte traités.",
        "history": [
            ("2007", "Inscription au tableau du notaire fondateur",
             "Me Maria Beatrice Conti est inscrite au tableau de "
             "la Chambre des Notaires de Milan et ouvre l'étude "
             "au 12 de la via Manin. Les premiers actes concernent "
             "des constitutions de sociétés de capitaux pour des "
             "entrepreneurs du Nord de l'Italie."),
            ("2011", "Actes authentiques trilingues",
             "L'étude commence à recevoir des actes authentiques "
             "rédigés en italien, anglais et français au sens de "
             "l'art. 54 de la Loi Notariale. La section "
             "internationale sert avant tout les groupes "
             "multinationaux avec filiale italienne et les familles "
             "résidant à l'étranger."),
            ("2014", "Entrée de Me Andrea Sironi",
             "Me Andrea Sironi, déjà stagiaire de longue date dans "
             "la circonscription, est coopté comme deuxième notaire "
             "de l'association. Il se spécialise en actes de société, "
             "opérations extraordinaires et expertises d'évaluation "
             "ex art. 2343 c.c."),
            ("2018", "Section successions et immobilier",
             "L'étude structure une section dédiée aux successions "
             "et à l'immobilier. Les procédures internes d'inspection "
             "hypothécaire et de consultation cadastrale préalables "
             "à l'acte de vente sont codifiées."),
            ("2021", "Entrée de Me Stefano Verri",
             "Me Stefano Verri complète la composition collégiale "
             "de l'association. Commissaire aux comptes inscrit au "
             "registre tenu par le MEF, il assume la responsabilité "
             "opérationnelle de la section immobilière et des "
             "successions."),
            ("2025", "Dix-sept ans de force probante",
             "L'étude dépasse les quatre mille deux cents actes "
             "instrumentés. Les trois notaires associés sont actifs "
             "dans la formation professionnelle : Me Conti comme "
             "membre de la Commission Études du Conseil Notarial, "
             "Me Sironi comme CTU au Tribunal de Milan, Me Verri "
             "comme enseignant en pratique notariale."),
        ],

        # Method — quattro principi non negoziabili
        "values_label":   "Méthode notariale",
        "values_heading": "Quatre principes <em>non négociables</em>",
        "values_intro":
            "Ce sont les quatre règles opérationnelles qui orientent "
            "le travail de l'étude. Elles ne décrivent pas un style "
            "commercial mais une pratique professionnelle fidèle à "
            "la Loi Notariale (L. 89/1913) et au Code de Déontologie "
            "du Conseil National du Notariat.",
        "values": [
            ("01", "Impartialité de l'officier public",
             "Le notaire est officier public et agit dans l'intérêt "
             "de toutes les parties à l'acte, jamais d'une seule. "
             "L'étude n'accepte aucun mandat de partie : aucun "
             "acte n'est préparé au bénéfice de l'une ou de l'autre "
             "des parties contractantes. Les instructions "
             "opérationnelles sont identiques pour le vendeur et "
             "l'acquéreur, le donateur et le donataire, l'apporteur "
             "et le bénéficiaire de l'apport."),
            ("02", "Vérification documentaire préalable",
             "Avant de recevoir l'acte, l'étude vérifie les "
             "documents urbanistiques, cadastraux et hypothécaires "
             "relatifs à l'immeuble ou à la société objet de l'acte. "
             "La consultation cadastrale, l'inspection hypothécaire "
             "et le DPE sont obtenus directement, jamais délégués "
             "aux parties, et sont annexés à l'acte selon l'usage."),
            ("03", "Lecture intégrale au comparant",
             "L'acte authentique est lu intégralement aux comparants "
             "au sens de l'art. 51 de la Loi Notariale, en italien "
             "ou dans la langue choisie parmi celles dans lesquelles "
             "le notaire est habilité (IT/EN/FR). Ce n'est qu'après "
             "lecture et approbation explicite que la signature et "
             "le numéro de répertoire sont apposés."),
            ("04", "Barème d'honoraires notariaux transparent",
             "Les honoraires sont déterminés selon le barème en "
             "vigueur approuvé par le Conseil National du Notariat. "
             "L'étude communique par écrit le devis indicatif avant "
             "chaque acte, droits et taxes d'enregistrement compris. "
             "Aucune ligne n'est ajoutée lors de la signature."),
        ],

        # Coordinates strip — sede unica milanese
        "coordinates_label": "Le siège",
        "coordinates": [
            ("Milan · siège",        "Via Manin 12 · 20121 · Porta Nuova"),
            ("Chambre des Notaires", "Milan · Conseil Notarial des Circonscriptions Réunies"),
        ],

        # Page-level CTA
        "cta_heading":  "Un premier rendez-vous pour cadrer l'acte.",
        "cta_intro":
            "Le premier rendez-vous avec l'un des notaires de "
            "l'étude est gratuit, dure environ trente minutes et "
            "n'engage à aucune démarche ultérieure. On y discute "
            "le type d'acte, les documents préliminaires et le "
            "barème des honoraires notariaux applicables.",
        "cta_primary":       "Demandez un premier rendez-vous",
        "cta_primary_href":  "contatti",
    },

    # ════════════════════════════════════════════════════════════════════
    # PRATICHE (services) — 7 tipologie di atti notarili
    # ════════════════════════════════════════════════════════════════════
    "pratiche": {
        "eyebrow":  "Domaines d'actes · 2026",
        "headline": "Sept types d'<em>acte notarié</em>, une seule signature.",
        "intro":
            "Les sept types d'acte traités par l'étude. Chaque "
            "acte authentique est rédigé personnellement par un "
            "notaire de l'association, inscrit au tableau de la "
            "Chambre des Notaires de Milan, et inscrit au "
            "répertoire au sens de la Loi Notariale (L. 89/1913). "
            "Les lignes du barème des honoraires notariaux sont "
            "communiquées par écrit avant la signature.",

        # Card meta labels (lifted from skin for locale support)
        "svc_lead_label":          "Notaire responsable",
        "svc_jurisdiction_label":  "Circonscription",

        # 7 atti notarili
        "services": [
            {
                "num":   "01",
                "title": "Actes de vente immobilière",
                "blurb":
                    "Rédaction de l'acte notarié pour la vente de "
                    "biens immobiliers résidentiels, commerciaux et "
                    "de production. L'étude se charge également de "
                    "la promesse synallagmatique de vente "
                    "(compromis) et des actes d'échange. La force "
                    "probante de l'acte est reconnue par "
                    "l'art. 2700 c.c.",
                "scope": [
                    "Consultation cadastrale et inspection hypothécaire",
                    "Vérification de la régularité urbanistique et DPE",
                    "Promesse de vente enregistrée",
                    "Acte authentique lu au comparant",
                ],
                "lead":          "Me Stefano Verri",
                "jurisdiction":  "Milan · Chambre des Notaires",
            },
            {
                "num":   "02",
                "title": "Successions et déclarations",
                "blurb":
                    "Ouverture de la succession, rédaction de la "
                    "déclaration de succession auprès de l'Agence "
                    "des Recettes, acceptation de l'hérédité sous "
                    "bénéfice d'inventaire, publication du testament "
                    "olographe, partages successoraux. Pour les "
                    "successions internationales s'applique le "
                    "Reg. UE 650/2012.",
                "scope": [
                    "Déclaration de succession",
                    "Acceptation bénéficiaire et sous réserve",
                    "Publication du testament olographe",
                    "Partages successoraux et renonciations",
                ],
                "lead":          "Me Stefano Verri",
                "jurisdiction":  "Milan · UE 650/2012",
            },
            {
                "num":   "03",
                "title": "Actes de société · constitutions · opérations extraordinaires",
                "blurb":
                    "Constitution de société par acte authentique au "
                    "sens des art. 2328 et 2463 c.c., modifications "
                    "statutaires, procès-verbaux d'assemblée "
                    "extraordinaire, fusions ex art. 2501 ss. c.c., "
                    "scissions proportionnelles ou non, "
                    "transformations hétérogènes. Dépôt au Registre "
                    "des Entreprises pris en charge par l'étude.",
                "scope": [
                    "Constitution de s.p.a. et s.r.l.",
                    "Modifications statutaires et pactes d'associés",
                    "Fusions, scissions, transformations",
                    "Dépôt au Registre des Entreprises",
                ],
                "lead":          "Me Andrea Sironi",
                "jurisdiction":  "Milan · CCIAA Milano Monza Brianza Lodi",
            },
            {
                "num":   "04",
                "title": "Prêts hypothécaires et garanties réelles",
                "blurb":
                    "Actes de prêt foncier et hypothécaire, "
                    "constitution d'hypothèque volontaire, "
                    "subrogations ex L. 40/2007 (portabilité du "
                    "prêt), actes récognitifs de créance et "
                    "mainlevées d'hypothèque. La signature a lieu "
                    "en règle générale concomitamment à l'acte "
                    "de vente.",
                "scope": [
                    "Prêt foncier concomitant à l'acte de vente",
                    "Constitution d'hypothèque volontaire",
                    "Subrogation ex L. 40/2007 (portabilité)",
                    "Mainlevée et réduction d'hypothèque",
                ],
                "lead":          "Me Stefano Verri",
                "jurisdiction":  "Milan · Agence des Recettes",
            },
            {
                "num":   "05",
                "title": "Donations · actes entre vifs",
                "blurb":
                    "Acte authentique de donation de biens "
                    "immobiliers, de sommes d'argent ou de "
                    "participations sociales au sens des art. 769 "
                    "et suivants c.c. L'étude traite également les "
                    "donations indirectes, les pactes de famille "
                    "ex art. 768-bis c.c. et les donations avec "
                    "réserve d'usufruit.",
                "scope": [
                    "Donation immobilière avec/sans réserve d'usufruit",
                    "Donation de participations sociales",
                    "Pactes de famille (art. 768-bis c.c.)",
                    "Planification fiscale et droit sur les donations",
                ],
                "lead":          "Me Maria Beatrice Conti",
                "jurisdiction":  "Milan · Agence des Recettes",
            },
            {
                "num":   "06",
                "title": "Procurations · légalisations de signature",
                "blurb":
                    "Procuration spéciale et procuration générale "
                    "au sens de l'art. 1387 c.c., légalisation de "
                    "signature sur acte sous seing privé, "
                    "certification de copie conforme. L'étude "
                    "délivre des procurations trilingues (IT/EN/FR) "
                    "pour des actes à accomplir à l'étranger, avec "
                    "apostille au sens de la Convention de La Haye "
                    "de 1961.",
                "scope": [
                    "Procuration spéciale et procuration générale",
                    "Légalisation de signature sur acte sous seing privé",
                    "Certification de copie conforme",
                    "Apostille et légalisation internationale",
                ],
                "lead":          "Me Maria Beatrice Conti",
                "jurisdiction":  "Milan · Convention de La Haye 1961",
            },
            {
                "num":   "07",
                "title": "Testaments · planification successorale",
                "blurb":
                    "Testament authentique au sens de l'art. 603 "
                    "c.c., réception du testament olographe, "
                    "testament international ex Convention de "
                    "Washington 1973. L'étude assiste les "
                    "comparants dans la reconnaissance du "
                    "patrimoine, dans la quantification de la "
                    "quotité disponible et de la réserve héréditaire.",
                "scope": [
                    "Testament authentique en forme de répertoire",
                    "Réception de testament olographe",
                    "Testament international (Washington 1973)",
                    "Planification de la réserve et quotité disponible",
                ],
                "lead":          "Me Stefano Verri",
                "jurisdiction":  "Milan · Archives Notariales",
            },
        ],

        # Process strip — come si svolge la pratica dell'atto
        "process_label":   "Cheminement de l'acte",
        "process_heading": "Quatre phases, une seule séquence",
        "process": [
            ("01", "Premier rendez-vous d'orientation",
             "Trente minutes gratuites avec l'un des notaires de "
             "l'association. On y cadre le type d'acte, on clarifie "
             "la liste des documents préliminaires et on communique "
             "le barème des honoraires notariaux applicables. "
             "Aucune décision opérationnelle n'est demandée à "
             "ce stade."),
            ("02", "Collecte documentaire et vérifications",
             "L'étude recueille et vérifie directement les documents "
             "nécessaires : consultation cadastrale, inspection "
             "hypothécaire, régularité urbanistique, DPE, certificats "
             "d'état civil. Le comparant reçoit la liste écrite de "
             "ce qui reste à sa charge."),
            ("03", "Préparation et projet de l'acte",
             "Le notaire responsable prépare le projet de l'acte et "
             "le transmet au comparant au moins cinq jours ouvrés "
             "avant la signature, afin de permettre une lecture "
             "réfléchie. Les éventuelles clarifications sont "
             "discutées lors d'un second rendez-vous technique."),
            ("04", "Signature, lecture et inscription au répertoire",
             "Le notaire lit l'acte au comparant au sens de "
             "l'art. 51 de la Loi Notariale, en italien ou dans la "
             "langue choisie. Après la signature, l'acte est inscrit "
             "au répertoire, enregistré auprès de l'Agence des "
             "Recettes et conservé en original auprès de l'étude."),
        ],

        # Final CTA
        "cta_heading":  "Le type d'acte n'est pas encore clair ?",
        "cta_intro":
            "Si le type d'acte n'est pas encore défini, il est "
            "possible de demander un premier rendez-vous "
            "d'orientation. Au cours des trente minutes gratuites, "
            "l'un des notaires de l'étude oriente vers la procédure "
            "correcte et communique la liste des documents "
            "préliminaires à réunir.",
        "cta_primary":       "Demandez un premier rendez-vous",
        "cta_primary_href":  "contatti",
    },

    # ════════════════════════════════════════════════════════════════════
    # AVVOCATI (team) — i tre notai associati
    # ════════════════════════════════════════════════════════════════════
    "avvocati": {
        "eyebrow":  "Les notaires · trois inscrits au tableau",
        "headline": "Trois notaires associés, <em>une seule</em> signature de force probante.",
        "intro":
            "L'étude est composée de trois notaires associés, tous "
            "inscrits au tableau de la Chambre des Notaires de "
            "Milan. L'entrée dans l'association se fait par "
            "cooptation unanime entre notaires déjà associés, "
            "jamais par acquisition d'étude : chaque nouveau "
            "notaire apporte en dot sa propre inscription et ses "
            "propres spécialisations. Six collaborateurs à temps "
            "plein complètent l'équipe.",

        # Card meta labels
        "lawyer_foro_label":           "Chambre",
        "lawyer_year_label":           "Inscription au tableau",
        "lawyer_specialization_label": "Types d'acte",

        # 3 notai associati
        "lawyers": [
            {
                "name":           "Me Maria Beatrice Conti",
                "role":           "Notaire fondateur de l'étude",
                "specialization": "Actes de société · M&A · donations · procurations trilingues",
                "foro":           "Chambre des Notaires de Milan",
                "year":           "Inscrite au tableau depuis 2007",
                "bio":
                    "Fondatrice du Studio Notarile Conti–Sironi–Verri, "
                    "elle a ouvert le siège du 12, via Manin en "
                    "mars 2007, juste après son inscription au "
                    "tableau de la Chambre des Notaires de Milan. "
                    "Elle reçoit les actes authentiques en italien, "
                    "anglais et français au sens de l'art. 54 de la "
                    "Loi Notariale, avec une spécialisation "
                    "particulière en constitutions de sociétés pour "
                    "groupes multinationaux avec filiale italienne, "
                    "fusions transfrontalières et procurations "
                    "internationales avec apostille au sens de la "
                    "Convention de La Haye. Membre de la Commission "
                    "Études du Conseil Notarial des Circonscriptions "
                    "Réunies de Milan, Busto Arsizio, Lodi, Monza "
                    "et Varèse.",
            },
            {
                "name":           "Me Andrea Sironi",
                "role":           "Notaire associé · droit des sociétés",
                "specialization": "Actes de société · opérations extraordinaires · expertises ex art. 2343 c.c.",
                "foro":           "Chambre des Notaires de Milan",
                "year":           "Inscrit au tableau depuis 2014",
                "bio":
                    "Coopté dans l'association en 2015 après huit "
                    "années de pratique notariale auprès d'une étude "
                    "milanaise de premier plan, il traite les actes "
                    "de société ordinaires et extraordinaires, les "
                    "pactes d'associés, les financements d'associés, "
                    "les augmentations de capital ex art. 2441 et "
                    "2443 c.c. CTU auprès du Tribunal de Milan pour "
                    "les expertises d'évaluation ex art. 2343 c.c. "
                    "et pour l'estimation de la valeur de liquidation "
                    "ex art. 2437-ter c.c. Enseignant en pratique "
                    "notariale à l'École du Notariat de Lombardie.",
            },
            {
                "name":           "Me Stefano Verri",
                "role":           "Notaire associé · immobilier et successions",
                "specialization": "Actes de vente · prêts · successions · testaments",
                "foro":           "Chambre des Notaires de Milan",
                "year":           "Inscrit au tableau depuis 2021",
                "bio":
                    "Dernier entré dans l'association, il complète "
                    "la composition collégiale des trois notaires. "
                    "Il traite les actes de vente immobilière, les "
                    "prêts hypothécaires, les subrogations ex "
                    "L. 40/2007 et l'ensemble de la filière "
                    "successorale — ouverture de la succession, "
                    "déclaration de succession, publication du "
                    "testament olographe, acceptation sous bénéfice "
                    "d'inventaire. Commissaire aux comptes inscrit "
                    "au registre tenu par le MEF depuis 2018, il "
                    "coordonne les vérifications urbanistiques, "
                    "cadastrales et hypothécaires préalables aux "
                    "actes de l'étude.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════════
    # PUBBLICAZIONI (blog_list) — publications et analyses notariales
    # ════════════════════════════════════════════════════════════════════
    "pubblicazioni": {
        "eyebrow":  "Publications et analyses · 2023 — 2026",
        "headline": "Cinq analyses sur l'<em>acte notarié</em> contemporain.",
        "intro":
            "Une sélection d'analyses et de publications rédigées "
            "par les notaires de l'étude ou citées dans des revues "
            "spécialisées. Les articles orientent les comparants, "
            "les entrepreneurs et les professionnels dans les "
            "principaux types d'acte — vente, succession, "
            "constitution de société, donation et procuration — "
            "sans prétention d'exhaustivité ni valeur de conseil "
            "dans le cas concret.",

        # Lead post image
        "lead_image": _NOTARY_HERO,

        # Footer strap and fallbacks
        "footer_strap":
            "Les publications de l'étude ont une finalité "
            "informative. Pour le cas concret, un premier "
            "rendez-vous avec l'un des notaires de l'association "
            "est nécessaire.",
        "empty_body_fallback_paragraphs": [
            "L'article est en cours de rédaction. L'étude publie "
            "ses analyses après lecture collégiale des trois "
            "notaires associés, afin d'éviter toute imprécision "
            "ou évaluation rendue obsolète par des modifications "
            "normatives.",
            "Pour le cas concret, il est possible de demander un "
            "premier rendez-vous d'orientation (trente minutes "
            "gratuites) avec l'un des notaires de l'étude.",
        ],
    },

    # Posts powering blog_detail. URL: /pubblicazioni/<slug>/
    "posts": [
        {
            "slug":     "atto-pubblico-mercato-immobiliare-2026",
            "kicker":   "Actes immobiliers",
            "title":    "L'acte authentique sur le marché immobilier 2026 · pratiques notariales et vérifications préalables",
            "date":     "Avril 2026",
            "read_min": "9",
            "author":   "Me Stefano Verri",
            "lede":
                "Une recension des vérifications urbanistiques, "
                "cadastrales et hypothécaires que l'étude accomplit "
                "avant de recevoir un acte de vente immobilière, à "
                "la lumière des modifications introduites par le "
                "D.Lgs. 23/2023 en matière de transparence "
                "énergétique et de la jurisprudence la plus récente "
                "de la Cassation sur la non-conformité urbanistique.",
            "body": [
                ("p",
                 "L'acte notarié de vente immobilière est acte "
                 "authentique au sens de l'art. 2699 c.c. et produit "
                 "la force probante reconnue par l'art. 2700 c.c. "
                 "Le notaire instrumentaire, en qualité d'officier "
                 "public, est tenu de vérifier au préalable la "
                 "régularité urbanistique, cadastrale et "
                 "hypothécaire de l'immeuble."),
                ("h2", "Les trois vérifications préalables"),
                ("p",
                 "L'étude recueille trois séries de documents avant "
                 "la signature : la consultation cadastrale à jour, "
                 "l'inspection hypothécaire vicennale et le "
                 "diagnostic de performance énergétique (DPE) en "
                 "cours de validité. La vérification de la "
                 "régularité urbanistique se fonde en outre sur "
                 "l'examen des titres habilitants déposés auprès "
                 "de la Commune."),
                ("h2", "Le rôle du notaire"),
                ("p",
                 "Le notaire n'est pas conseil de partie : il "
                 "assiste les deux comparants dans le cadrage de "
                 "l'acte et dans la lecture des clauses. Les "
                 "éventuelles difficultés urbanistiques apparues "
                 "lors de la vérification sont communiquées par "
                 "écrit au vendeur et à l'acquéreur, de sorte que "
                 "la décision de signer ou de reporter soit "
                 "éclairée."),
                ("blockquote",
                 "La force probante de l'acte authentique n'est "
                 "garantie que si les vérifications préalables ont "
                 "été accomplies avec la diligence propre à "
                 "l'officier public. Toute omission documentaire "
                 "expose les parties à des risques de nullité ou "
                 "d'annulabilité postérieurs à l'acte."),
            ],
        },
        {
            "slug":     "successioni-famiglia-orientamento",
            "kicker":   "Successions",
            "title":    "Successions en famille · s'orienter sans confusion entre déclaration, acceptation et partage",
            "date":     "Février 2026",
            "read_min": "8",
            "author":   "Me Stefano Verri",
            "lede":
                "Les étapes concrètes de la succession mortis causa "
                "en droit italien. De l'ouverture de la succession "
                "à la déclaration auprès de l'Agence des Recettes, "
                "en passant par la publication du testament "
                "olographe, l'acceptation sous bénéfice d'inventaire "
                "et le partage successoral. Quand l'acte notarié "
                "est requis, quand l'acte sous seing privé suffit.",
            "body": [
                ("p",
                 "La succession s'ouvre au moment du décès du "
                 "de cujus, au lieu de son dernier domicile, au "
                 "sens de l'art. 456 c.c. À compter de cet instant "
                 "courent les délais pour la déclaration de "
                 "succession (douze mois) et pour les éventuelles "
                 "renonciations ou acceptations sous bénéfice "
                 "d'inventaire."),
                ("h2", "Déclaration de succession"),
                ("p",
                 "L'étude prépare la déclaration de succession à "
                 "présenter à l'Agence des Recettes dans les douze "
                 "mois suivant l'ouverture de la succession. La "
                 "déclaration contient la liste des biens du "
                 "de cujus, des appelés à l'hérédité et des "
                 "éventuelles passivités déductibles."),
                ("h2", "Quand l'acte notarié est requis"),
                ("p",
                 "L'acte notarié est nécessaire pour la publication "
                 "du testament olographe au sens de l'art. 620 "
                 "c.c., pour l'acceptation de l'hérédité sous "
                 "bénéfice d'inventaire ex art. 484 c.c., pour le "
                 "partage successoral de biens immobiliers et "
                 "pour les renonciations à l'hérédité comportant "
                 "des biens immobiliers."),
            ],
        },
        {
            "slug":     "costituzione-srl-semplificata-passaggi-reali",
            "kicker":   "Actes de société",
            "title":    "Constitution de s.r.l. simplifiée · les étapes concrètes au-delà des formulaires",
            "date":     "Décembre 2025",
            "read_min": "7",
            "author":   "Me Andrea Sironi",
            "lede":
                "La constitution de s.r.l. simplifiée ex art. "
                "2463-bis c.c. paraît une procédure standard à "
                "coût réduit. Dans les faits, l'acte authentique "
                "exige une série d'évaluations préalables que le "
                "modèle-type ne couvre pas : objet social, "
                "administration, apports, modalités de convocation "
                "de l'assemblée.",
            "body": [
                ("p",
                 "La s.r.l. simplifiée, introduite par le D.L. 1/2012, "
                 "représente une version à coût notarial réduit "
                 "(honoraires notariaux nuls pour la constitution, "
                 "droits d'enregistrement réduits) de la s.r.l. "
                 "ordinaire. Les statuts sont conformes au modèle "
                 "ministériel et ne peuvent être modifiés en phase "
                 "de constitution."),
                ("h2", "Les choix préalables"),
                ("p",
                 "Malgré les statuts-type, certains choix importants "
                 "restent à définir : l'objet social (qui doit être "
                 "licite et déterminé), la composition de l'organe "
                 "d'administration (administrateur unique ou "
                 "conseil d'administration), la durée de la société, "
                 "les modalités de convocation de l'assemblée, les "
                 "apports en numéraire des associés."),
                ("h2", "L'acte authentique constitutif"),
                ("p",
                 "L'acte constitutif est reçu en forme d'acte "
                 "authentique au sens de l'art. 2463-bis alinéa 2 "
                 "c.c. et inscrit au Registre des Entreprises par "
                 "le notaire dans les vingt jours suivant la "
                 "signature. La lecture aux associés comparants "
                 "est intégrale, en italien ou dans la langue "
                 "choisie parmi celles dans lesquelles le notaire "
                 "est habilité."),
            ],
        },
        {
            "slug":     "donazione-coniugi-riforma-2024",
            "kicker":   "Donations",
            "title":    "Donation entre époux · ce que change la réforme de 2024 et la circulaire 32/E",
            "date":     "Octobre 2025",
            "read_min": "10",
            "author":   "Me Maria Beatrice Conti",
            "lede":
                "La donation entre époux est acte authentique "
                "typique au sens des art. 769 et suivants c.c. "
                "Les modifications normatives de 2024 et la "
                "circulaire 32/E de l'Agence des Recettes ont "
                "clarifié certains aspects d'application sur le "
                "droit sur les donations, sur les abattements et "
                "sur la révocabilité pour survenance d'enfants.",
            "body": [
                ("p",
                 "La donation entre époux est régie par les "
                 "art. 769 et suivants du code civil et est soumise "
                 "à la forme de l'acte authentique sous peine de "
                 "nullité ex art. 782 c.c. L'abattement pour le "
                 "droit sur les donations entre époux est d'un "
                 "million d'euros pour chaque donataire."),
                ("h2", "Réserve d'usufruit et nue-propriété"),
                ("p",
                 "Un choix fréquent dans les donations immobilières "
                 "entre époux est la donation de la nue-propriété "
                 "avec réserve d'usufruit en faveur du donateur. "
                 "L'opération, parfaitement légitime ex art. 796 "
                 "c.c., permet au donateur de conserver la "
                 "jouissance du bien tout en en maintenant les "
                 "revenus."),
                ("h2", "Révocabilité pour survenance d'enfants"),
                ("p",
                 "La donation est révocable pour survenance "
                 "d'enfants ex art. 803 c.c. lorsque le donateur, "
                 "au moment de l'acte, n'avait pas d'enfants ni de "
                 "descendants. La révocabilité s'étend aux enfants "
                 "adoptés par adoption plénière intervenue après "
                 "la donation."),
            ],
        },
        {
            "slug":     "procura-art-1387-cc-quando-serve",
            "kicker":   "Procurations",
            "title":    "Procuration au sens de l'art. 1387 c.c. · quand elle est requise et comment la rédiger (avec apostille)",
            "date":     "Juillet 2025",
            "read_min": "6",
            "author":   "Me Maria Beatrice Conti",
            "lede":
                "La procuration est l'acte par lequel le "
                "représenté confère au représentant le pouvoir "
                "d'accomplir un ou plusieurs actes juridiques en "
                "son nom. Lorsque l'acte à accomplir exige la "
                "forme de l'acte authentique — par exemple une "
                "vente immobilière — la procuration doit elle "
                "aussi être reçue en la forme authentique.",
            "body": [
                ("p",
                 "L'art. 1387 c.c. régit les cas dans lesquels la "
                 "procuration est nécessaire pour accomplir des "
                 "actes juridiques au nom du représenté. En vertu "
                 "du principe de symétrie formelle (art. 1392 c.c.), "
                 "la procuration doit revêtir la même forme requise "
                 "pour l'acte que le représentant doit accomplir."),
                ("h2", "Procuration spéciale et procuration générale"),
                ("p",
                 "La procuration spéciale confère le pouvoir "
                 "d'accomplir un acte déterminé (par exemple : la "
                 "vente d'un immeuble précis). La procuration "
                 "générale confère le pouvoir d'accomplir tous "
                 "les actes relevant d'une catégorie (par "
                 "exemple : tous les actes d'administration "
                 "ordinaire du patrimoine du représenté)."),
                ("h2", "Procurations trilingues et apostille"),
                ("p",
                 "Pour les actes à accomplir à l'étranger, l'étude "
                 "rédige les procurations en italien et dans la "
                 "langue du pays de destination (anglais ou "
                 "français) au sens de l'art. 54 de la Loi "
                 "Notariale. L'apostille au sens de la Convention "
                 "de La Haye de 1961 est apposée par le Procureur "
                 "de la République près le Tribunal de Milan."),
            ],
        },
    ],

    # ════════════════════════════════════════════════════════════════════
    # CONTATTI (contact) — siège unique milanais, formulaire d'orientation
    # ════════════════════════════════════════════════════════════════════
    "contatti": {
        "eyebrow":  "Premier rendez-vous d'orientation · gratuit · sans engagement",
        "headline": "Trente minutes avec un <em>notaire</em> pour cadrer l'acte.",
        "intro":
            "Le premier rendez-vous a lieu directement avec l'un "
            "des trois notaires de l'association. On y discute le "
            "type d'acte, la liste des documents préliminaires à "
            "réunir et le barème des honoraires notariaux "
            "applicables. Le rendez-vous dure environ trente "
            "minutes, il est gratuit et n'engage à aucune "
            "démarche ultérieure.",

        # Form fields
        "form_label":   "Formulaire de demande",
        "form_heading": "Demandez un premier rendez-vous d'orientation",
        "form_intro":
            "Vous recevrez une confirmation de réception sous "
            "quarante-huit heures ouvrées, de la part du secrétariat "
            "de l'étude, accompagnée de la proposition de trois "
            "créneaux horaires disponibles et de l'indication du "
            "notaire responsable du type d'acte concerné. Les "
            "données sont traitées au sens du Règlement UE 679/2016 "
            "et conservées sur des systèmes conformes aux lignes "
            "directrices du Conseil National du Notariat.",
        "form_fields": [
            {"name": "name", "label": "Prénom", "type": "text", "required": True,
             "placeholder": "Ex. Anne",
             "helper": "Uniquement le prénom, tel qu'il figure sur la pièce d'identité."},
            {"name": "surname", "label": "Nom", "type": "text", "required": True,
             "placeholder": "Ex. Bianchi",
             "helper": "Tel qu'il figure sur la pièce d'identité du comparant."},
            {"name": "email", "label": "Adresse électronique", "type": "email", "required": True,
             "placeholder": "anne.bianchi@exemple.fr",
             "helper": "Pour la correspondance préliminaire. Nous n'utilisons pas l'adresse à d'autres fins."},
            {"name": "phone", "label": "Téléphone", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "Ligne directe du référent pour les modalités d'horaire."},
            {"name": "capacity", "label": "En qualité de", "type": "select", "required": True,
             "options": [
                 "Particulier",
                 "Entrepreneur ou associé de société",
                 "Administrateur de société",
                 "Héritier ou légataire",
                 "Professionnel (expert-comptable, avocat, agent immobilier)",
                 "Établissement bancaire ou assurance",
             ],
             "helper": "Pour orienter l'entretien et identifier le notaire responsable."},
            {"name": "act_type", "label": "Type d'acte", "type": "select", "required": True,
             "options": [
                 "À définir lors de l'entretien",
                 "Acte de vente immobilière",
                 "Prêt hypothécaire ou subrogation",
                 "Succession ou déclaration de succession",
                 "Testament authentique ou publication d'olographe",
                 "Constitution de société ou acte de société",
                 "Fusion, scission ou transformation",
                 "Donation ou pacte de famille",
                 "Procuration spéciale ou générale",
                 "Légalisation de signature ou copie conforme",
             ],
             "helper": "Choisissez « À définir » si le type n'est pas encore clair."},
            {"name": "timing", "label": "Délais indicatifs", "type": "select", "required": True,
             "options": [
                 "Sous un mois",
                 "Sous trois mois",
                 "Sous six mois",
                 "Exploratoire, sans échéance définie",
             ],
             "helper": "Pour planifier le premier rendez-vous et le cheminement de l'acte."},
            {"name": "language", "label": "Langue de l'acte (si pertinent)", "type": "select", "required": False,
             "options": [
                 "Italien",
                 "Italien avec traduction en anglais",
                 "Italien avec traduction en français",
                 "À évaluer lors de l'entretien",
             ],
             "helper": "L'étude reçoit les actes authentiques en italien, anglais et français."},
            {"name": "scope", "label": "Brève description de l'acte",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Maximum 600 caractères. Indiquez de façon "
                 "synthétique l'objet de l'acte (par exemple : "
                 "« vente d'un appartement situé à Milan, côté "
                 "vendeur »). Les données des tiers sont recueillies "
                 "uniquement lors du rendez-vous, jamais dans ce "
                 "formulaire.",
             "helper":
                 "Le strict nécessaire pour cadrer le type d'acte "
                 "et orienter le dossier vers le notaire responsable. "
                 "Les détails se discutent lors du premier "
                 "rendez-vous."},
        ],

        "form_sections": [
            {"num": "01", "title": "Référent",
             "meta": "La personne qui participera au premier rendez-vous en qualité de comparant.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Position",
             "meta": "Pour orienter la demande vers le notaire responsable.",
             "fields": ["capacity"]},
            {"num": "03", "title": "Type d'acte",
             "meta":
                 "Aucune donnée de tiers ici — les noms des "
                 "contreparties, héritiers ou apporteurs sont "
                 "recueillis lors du premier rendez-vous.",
             "fields": ["act_type", "timing", "language", "scope"]},
            {"num": "04", "title": "Documents préliminaires (facultatifs)",
             "meta":
                 "Consultations cadastrales, actes antérieurs, "
                 "plans ou projets peuvent accélérer le cadrage.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "documenti_preliminari",
            "label":    "Documents préliminaires",
            "helper":
                "Consultations cadastrales, actes d'origine, plans, "
                "projets de statuts. PDF / DOCX · max 15 Mo au total. "
                "Les documents sont conservés sur archive chiffrée "
                "selon les lignes directrices du Conseil National "
                "du Notariat.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Glissez ici les documents ou",
            "link":     "sélectionnez depuis l'archive",
            "meta":     "PDF / DOCX · max 15 Mo · archive chiffrée",
        },

        "form_submit_label": "Demandez un premier rendez-vous",
        "form_submit_note":
            "Confirmation de réception sous quarante-huit heures "
            "ouvrées, avec la proposition de trois créneaux "
            "horaires. Aucune automatisation commerciale, aucun "
            "BDR, aucune communication marketing ultérieure.",
        "form_consent":
            "Je consens au traitement de mes données personnelles "
            "au sens du Règlement UE 679/2016 et déclare être "
            "informé que les données sont conservées sur des "
            "systèmes conformes aux lignes directrices du Conseil "
            "National du Notariat et des Archives Notariales. Les "
            "données ne sont pas communiquées à des tiers sans "
            "consentement écrit explicite du comparant.",

        # Office meta-row labels
        "office_address_label": "Adresse",
        "office_area_label":    "Quartier",
        "office_phone_label":   "Téléphone",
        "office_email_label":   "Courriel",
        "office_hours_label":   "Horaires",

        # Sidebar — siège unique, canaux directs
        "offices_label":   "Le siège",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Siège unique de l'étude",
                "address": "Via Manin 12 · 20121",
                "area":    "Porta Nuova · à 200 mètres de Repubblica M3",
                "phone":   "+39 02 7641 1898",
                "email":   "studio@notaiconti-sironi-verri.it",
                "hours":   "Lun – Ven · 09 h 00 – 18 h 30",
            },
        ],

        "channels_label": "Canaux directs",
        "channels": [
            ("Secrétariat de l'étude",
             "+39 02 7641 1898",
             "Lun – Ven · 09 h 00 – 18 h 30"),
            ("Courriel institutionnel",
             "studio@notaiconti-sironi-verri.it",
             "Réponse sous 48 heures ouvrées"),
            ("PEC certifiée",
             "studio.contisironi@postacertificata.notariato.it",
             "Pour actes, notifications et dépôts télématiques"),
        ],

        "footnote":
            "Le Studio Notarile Conti–Sironi–Verri ne délivre "
            "aucun avis contraignant par courriel sans un premier "
            "rendez-vous d'orientation avec l'un des trois "
            "notaires de l'association. Le barème des honoraires "
            "notariaux applicables au cas concret est communiqué "
            "par écrit à l'issue du premier rendez-vous, avant "
            "tout conférence formelle de mandat.",
    },
}


# ─────────────────────────────────────────────────────────────────────
# D-047 — chrome-authoring contract (FR mirror).
# Every visible string in the lawyer/classic-gold skin templates
# must come from THIS file (or from chrome.* / dna.content.*).
# Zero literal "Conti", "Sironi", "Verri", "2007", "Milan",
# "via Manin", notaires names, headline text, or other brand-specific
# strings in the .html files. The skin is reused verbatim from Lex —
# the distinctness lives in the content tree, not in the templates.
# ─────────────────────────────────────────────────────────────────────
