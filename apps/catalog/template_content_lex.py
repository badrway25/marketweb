"""Lex — Studio Legale Ferri (lawyer / classic-gold archetype) IT content tree.

Phase 2g3.7 · Session 53 · Lex Studio Legale Ferri — classic-gold archetype.
Forensic-notarile tone.

Editorial identity: studio legale civilistico romano, due sedi (Roma e
Milano), fondato nel 1962 dall'avv. Giuseppe Ferri, oggi diretto dal figlio
Avv. Prof. Alberto Ferri. Quattordici avvocati abilitati al foro di Roma,
collaborazioni a Milano e Bruxelles. La voce è notarile, terza persona
plurale, citazione costante dei codici (Art. 2343 c.c., D.Lgs. 231/2001,
c.p.p.). Riserbo assoluto: i clienti non vengono mai nominati, le cause
sono indicate per filiera ("gruppo industriale quotato del settore
energetico", "famiglia imprenditoriale del Nord-Est"). Conversion pattern:
ghost serif "Richiedi una consulenza riservata" CTA + email diretta al
managing partner — nessuna prenotazione automatica, nessun calendario
pubblico, nessun BDR.

Differentiation contract vs Juris (D-054 enforcement, 10 gates):
 1. Hero silhouette:   split-ledger-monogram (gold rule + serif drama L,
                       monogram crest + meta_strip R)
                       vs Juris centered-advisory-manifesto + sprint chip
 2. Palette:           ink #1A1A2E + bordeaux #8B0000 + gold #C5A55A
                       vs Juris cobalt blue + pill-blue
 3. Typography:        Cormorant Garamond (heading) + Inter
                       vs Juris DM Sans (heading) + Inter
 4. Density:           airy editorial chapters (96-100px paddings)
                       vs Juris medium pill density
 5. Conversion CTA:    "Richiedi consulenza riservata" + email directa
                       vs Juris "Prenota strategy call" + slot calendar
 6. Sub-pages:         studio · pratiche · avvocati · notabili (cause)
                       vs Juris approccio · servizi · settori · insights
 7. Tono di voce:      notarile, terza persona plurale, codici citati
                       vs Juris advisory-modern, "tu", numeri sprint
 8. Imagery direction: legal-heritage-ink (libri, gavel, ritratti senior)
                       vs Juris advisory-modern-light (workspace, dashboard)
 9. Contact pattern:   form riservato + email diretta managing partner,
                       NDA preliminare prima della consulenza
                       vs Juris discovery call form + dashboard live
10. Footer footprint:  4 colonne istituzionali, due sedi (Roma + Milano)
                       + iscrizione Ordine Avvocati Roma A18449
                       vs Juris pill-stack moderno con disclaimer fiscale

Page kinds:
- home (studio), about (studio), services (pratiche), team (avvocati),
  blog_list (notabili / cause notabili / pubblicazioni), contact (contatti)
"""
from __future__ import annotations

from typing import Any


LEX_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "Studio",           "kind": "home"},
        {"slug": "studio",    "label": "Lo Studio",        "kind": "about"},
        {"slug": "pratiche",  "label": "Aree di pratica",  "kind": "services"},
        {"slug": "avvocati",  "label": "Avvocati",         "kind": "team"},
        {"slug": "notabili",  "label": "Notabili",         "kind": "blog_list"},
        {"slug": "contatti",  "label": "Contatti",         "kind": "contact"},
    ],

    # ─── SITE — chrome rendered by _base.html ─────────────────────
    "site": {
        "logo_initial":  "LF",
        "logo_word":     "Studio Legale Ferri",
        "tag":           "Foro di Roma · dal 1962",
        "phone":         "+39 06 4567 2300",
        "email":         "studio@studioferri.legal",
        "address":       "Via Piemonte 39 · 00187 Roma",
        "hours_compact": "Lunedì – Venerdì · 09:00 – 19:00",
        "hours_footer_rows": [
            "Sabato · solo su appuntamento",
            "Domenica · chiuso",
        ],
        "license":       "Iscr. Ordine Avvocati Roma A18449 · P.IVA 03124770581",
        "nav_cta":       "Richiedi consulenza",
        "footer_intro":
            "Studio Legale Ferri — sessantadue anni di foro, due sedi "
            "(Roma e Milano), quattordici avvocati abilitati. Competenza, "
            "riservatezza, risultati.",
        "foot_studio":  "Lo studio",
        "foot_pages":   "Pagine",
        "foot_contact": "Contatti",
        "foot_offices": "Sedi",
        "offices_footer_rows": [
            "Roma · via Piemonte 39",
            "Milano · corso Venezia 11",
        ],

        # Cross-page meta labels (lifted from skin so each locale picks
        # up the right translation). Used by blog_list/blog_detail and
        # by services / team chrome strips.
        "case_practice_label":  "Pratica",
        "case_year_label":      "Anno",
        "case_outcome_label":   "Esito",
        "case_lead_label":      "Patrocinio",
    },

    # ════════════════════════════════════════════════════════════
    # HOME (studio)
    # ════════════════════════════════════════════════════════════
    "home": {
        "eyebrow":    "Studio Legale Ferri · Roma · Milano · dal 1962",
        "headline":   "Competenza, <em>riservatezza</em>, risultati.",
        "intro":
            "Assistiamo imprese, famiglie e professionisti con un approccio "
            "rigoroso, personalizzato e discreto. Sessantadue anni di foro, "
            "due sedi, quattordici avvocati abilitati. Ogni mandato è "
            "seguito personalmente da un socio dello studio dall'apertura "
            "del fascicolo al passaggio in giudicato.",
        "primary_cta":   "Richiedi una consulenza riservata",
        "primary_href":  "contatti",
        "secondary_cta": "Aree di pratica",
        "secondary_href":"pratiche",

        # Hero — split-ledger-monogram silhouette
        # LEFT: gold vertical rule + eyebrow + serif drama headline + credit cells
        # RIGHT: monogram crest + meta_strip institutional rows
        "hero_credit_left":  ("Direzione",        "Avv. Prof. A. Ferri"),
        "hero_credit_right": ("Foro",             "Roma · Milano"),
        "hero_meta_strip": [
            ("Sede principale",     "Roma · via Piemonte"),
            ("Soci fondatori",      "1962 · famiglia Ferri"),
            ("Avvocati abilitati",  "14 · foro di Roma"),
        ],

        # Practice-area ledger — 4 numbered rows on home, full 12 on /pratiche
        "practice_label":   "Aree di pratica",
        "practice_heading": "Dodici competenze, una sola <em>firma</em>.",
        "practice_intro":
            "Le pratiche dello studio coprono il diritto civile, "
            "commerciale, penale d'impresa e amministrativo. Ogni mandato "
            "è coordinato da un socio senior, mai delegato in toto a "
            "collaboratori junior.",
        "practice": [
            ("01", "Diritto societario",
             "M&A, governance, contrattualistica commerciale e operazioni "
             "straordinarie. Aumenti di capitale ex Art. 2343 c.c. con "
             "perizia giurata, fusioni transfrontaliere, riassetti di "
             "gruppo, patti parasociali."),
            ("02", "Diritto di famiglia e successioni",
             "Separazioni consensuali e giudiziali, divorzi, regolamento "
             "dell'affidamento, successioni internazionali, trust di "
             "famiglia, donazioni e patti di famiglia ex Art. 768-bis c.c."),
            ("03", "Diritto del lavoro",
             "Contenzioso individuale e collettivo, contrattazione di "
             "secondo livello, sicurezza sul lavoro ex D.Lgs. 81/2008, "
             "licenziamenti per giusta causa e giustificato motivo, "
             "transazioni in sede sindacale."),
            ("04", "Diritto penale d'impresa",
             "Reati societari ex Art. 2621-2641 c.c., responsabilità "
             "amministrativa degli enti ex D.Lgs. 231/2001, white collar "
             "crimes, reati tributari ex D.Lgs. 74/2000, modelli "
             "organizzativi e organismi di vigilanza."),
        ],

        # Stats band on dark ink — counter animation (D-081 binding)
        "stats_label":   "Sessantadue anni di foro",
        "stats_heading": "I numeri dello studio",
        "stats": [
            ("62",     "anni di attività"),
            ("14",     "avvocati abilitati"),
            ("2.400+", "cause patrocinate"),
            ("96%",    "esito favorevole"),
        ],

        # Partners portrait preview — 3 senior partners on home, 14 on /avvocati
        "partners_label":   "Direzione",
        "partners_heading": "Tre soci, una sola direzione",
        "partners_intro":
            "I soci dello studio firmano personalmente ogni atto. "
            "Nessun mandato viene accettato senza preventivo conflict-check "
            "e senza attribuzione formale a un socio responsabile.",
        "partners": [
            {
                "name":  "Avv. Prof. Alberto Ferri",
                "role":  "Managing partner · Diritto societario",
                "foro":  "Foro di Roma dal 1986 · Cassazionista dal 1999",
                "bio":
                    "Figlio del fondatore, ha guidato lo studio dal 2004. "
                    "Professore associato di diritto commerciale a "
                    "LUISS Guido Carli. Autore del volume \"L'aumento "
                    "di capitale nelle società quotate\" (Giuffrè, 2018).",
            },
            {
                "name":  "Avv. Maria Grazia Conti",
                "role":  "Socia senior · Diritto di famiglia",
                "foro":  "Foro di Roma dal 1991 · Cassazionista dal 2003",
                "bio":
                    "Specialista in successioni internazionali e patti di "
                    "famiglia. Collaboratrice della rivista \"Famiglia e "
                    "Diritto\" dal 2007. Mediatrice familiare iscritta "
                    "all'Ordine Mediatori del Tribunale di Roma.",
            },
            {
                "name":  "Avv. Lorenzo Marchetti",
                "role":  "Socio · Diritto penale d'impresa",
                "foro":  "Foro di Roma dal 1995 · Cassazionista dal 2007",
                "bio":
                    "Già pubblico ministero presso la Procura di Milano "
                    "(1998-2003), oggi specializzato in 231 e reati "
                    "tributari. Componente dell'Organismo di Vigilanza "
                    "di tre gruppi industriali quotati su Euronext Milan.",
            },
        ],

        # Publications ribbon — riviste + opere monografiche
        "publications_label": "Pubblicazioni e citazioni",
        "publications": [
            "FORO ITALIANO",
            "DIRITTO E GIUSTIZIA",
            "IL SOLE 24 ORE · LEGALE",
            "GUIDA AL DIRITTO",
            "CASSAZIONE PENALE",
            "RIVISTA DELLE SOCIETÀ",
        ],

        # Final CTA band — private-consultation ghost serif
        "cta_label":     "Consulenza preliminare riservata",
        "cta_heading":   "Una conversazione preliminare con un socio.",
        "cta_intro":
            "Il primo contatto avviene direttamente con un socio dello "
            "studio. Si discute il perimetro del mandato, l'eventuale "
            "conflitto di interesse e la tariffa indicativa — prima di "
            "qualsiasi incarico formale e nel rispetto del segreto "
            "professionale.",
        "cta_primary":      "Richiedi consulenza",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Conosci lo studio",
        "cta_secondary_href":"studio",
    },

    # ════════════════════════════════════════════════════════════
    # STUDIO (about) — storia, fondatori, metodo, valori, sedi
    # ════════════════════════════════════════════════════════════
    "studio": {
        "eyebrow":  "Lo studio · 1962 — 2026",
        "headline": "Sessantadue anni di foro, <em>due generazioni</em> della famiglia Ferri.",
        "intro":
            "Lo Studio Legale Ferri nasce nel 1962 a Roma per iniziativa "
            "dell'Avv. Giuseppe Ferri, allora trentaduenne magistrato "
            "dimissionario, con tre fascicoli di diritto societario e "
            "un solo praticante. Sessantadue anni più tardi siamo "
            "quattordici avvocati abilitati, due sedi, una sola "
            "governance — e l'indipendenza dal capitale di terzi che "
            "il fondatore pose come prima regola dello statuto.",

        # History timeline — sei date che hanno definito lo studio
        "history_label":   "Storia dello studio",
        "history_heading": "Sei date, sessantadue anni",
        "history_intro":
            "Sei pietre miliari che segnano la traiettoria dello studio — "
            "dalla fondazione del 1962 al passaggio generazionale del "
            "2004, fino all'apertura della sede di Milano nel 2019. "
            "Dietro ognuna di queste date c'è una scelta strutturale "
            "di indipendenza, di pratica o di geografia che ancora "
            "oggi orienta i mandati.",
        "history": [
            ("1962", "Fondazione",
             "L'Avv. Giuseppe Ferri, dimissionario dalla magistratura, "
             "apre lo studio in via Piemonte 39 con tre fascicoli di "
             "diritto societario e un solo praticante."),
            ("1978", "Iscrizione all'Albo dei Cassazionisti",
             "Dopo sedici anni di patrocinio davanti alle corti di "
             "merito, il fondatore viene iscritto all'Albo speciale "
             "dei Cassazionisti — la pratica civile può patrocinare "
             "in Cassazione direttamente, senza domiciliatario."),
            ("1989", "Pratica penale d'impresa",
             "Lo studio costituisce una sezione autonoma di diritto "
             "penale d'impresa, anticipando di un decennio il "
             "D.Lgs. 231/2001. I primi modelli organizzativi vengono "
             "redatti per due gruppi industriali del settore "
             "metalmeccanico."),
            ("2004", "Passaggio generazionale",
             "L'Avv. Prof. Alberto Ferri assume la direzione dello "
             "studio. Il padre fondatore mantiene il ruolo di Senior "
             "of Counsel fino al 2014. Lo statuto viene aggiornato "
             "per disciplinare l'associazione di nuovi soci per "
             "cooptazione, mai per acquisizione."),
            ("2014", "Pratica successioni internazionali",
             "Con l'entrata in vigore del Regolamento UE 650/2012 in "
             "materia di successioni transfrontaliere, lo studio "
             "costituisce una pratica dedicata. I primi mandati "
             "riguardano famiglie imprenditoriali italiane con "
             "patrimoni in Svizzera e Lussemburgo."),
            ("2019", "Apertura sede di Milano",
             "Per accompagnare i mandati di diritto societario e "
             "M&A del Nord, lo studio apre la seconda sede in "
             "corso Venezia 11. Tre soci e due collaboratori "
             "stabili. Le due sedi mantengono governance unica "
             "e nessuna conflict-list autonoma."),
        ],

        # Method — quattro principi non negoziabili
        "values_label":   "Metodo",
        "values_heading": "Quattro principi <em>non negoziabili</em>",
        "values_intro":
            "Sono le quattro regole che separano un mandato Studio "
            "Ferri da un incarico legale standard. Le trovate scritte "
            "in lettera di mandato, non in pagina marketing.",
        "values": [
            ("01", "Riservatezza assoluta",
             "Il segreto professionale ex Art. 622 c.p. è applicato "
             "in maniera estesa: i nominativi dei clienti non "
             "vengono mai divulgati, neppure in forma anonimizzata, "
             "senza esplicito consenso scritto. Lo studio non "
             "pubblica case histories nominative né cita clienti "
             "in materiale promozionale."),
            ("02", "Un socio per ogni mandato",
             "Ogni fascicolo è seguito personalmente da un socio "
             "dell'associazione professionale dall'apertura al "
             "passaggio in giudicato. Il socio firma gli atti "
             "rilevanti e partecipa alle udienze di merito. "
             "Nessun mandato viene delegato in toto a collaboratori "
             "junior, mai."),
            ("03", "Conflict-check rigoroso",
             "Prima dell'accettazione di ogni nuovo mandato, il "
             "Compliance Officer interno verifica l'assenza di "
             "conflitti di interesse rispetto al portafoglio clienti "
             "attivo e ai mandati chiusi negli ultimi cinque anni. "
             "In caso di dubbio, il mandato viene rifiutato "
             "preventivamente."),
            ("04", "Tariffario trasparente",
             "Onorari professionali concordati per iscritto in "
             "lettera di mandato secondo i parametri di cui al "
             "DM 55/2014. Success fee ammessi solo nei limiti del "
             "Codice Deontologico Forense. Nessuna retroversione, "
             "nessun accordo verbale con controparti."),
        ],

        # Coordinates strip — le due sedi
        "coordinates_label": "Le sedi",
        "coordinates": [
            ("Roma",    "Via Piemonte 39 · 00187 · Quirinale"),
            ("Milano",  "Corso Venezia 11 · 20121 · Porta Venezia"),
        ],

        # Page-level CTA
        "cta_heading":  "Una valutazione preliminare riservata.",
        "cta_intro":
            "Il primo colloquio avviene direttamente con un socio "
            "dello studio. Si discute il perimetro del mandato, "
            "l'eventuale conflitto di interesse e la tariffa "
            "indicativa, sotto vincolo di riservatezza.",
        "cta_primary":      "Richiedi consulenza",
        "cta_primary_href": "contatti",
    },

    # ════════════════════════════════════════════════════════════
    # PRATICHE (services) — 12 aree di pratica
    # ════════════════════════════════════════════════════════════
    "pratiche": {
        "eyebrow":  "Aree di pratica · 2026",
        "headline": "Dodici competenze, una sola <em>firma</em>.",
        "intro":
            "Le dodici aree di pratica dello studio. Ogni cliente "
            "accede a un team multidisciplinare — non si paga per "
            "ciascuna pratica separatamente, il mandato copre la "
            "combinazione di competenze necessarie alla soluzione "
            "del problema posto.",

        # Card meta labels (lifted from skin for locale support)
        "svc_lead_label":     "Socio responsabile",
        "svc_jurisdiction_label": "Foro di riferimento",

        # 12 services in airy ledger
        "services": [
            {
                "num":     "01",
                "title":   "Diritto societario",
                "blurb":
                    "Costituzione di società, governance, patti "
                    "parasociali, operazioni straordinarie. Aumenti di "
                    "capitale ex Art. 2343 c.c. con perizia giurata, "
                    "fusioni transfrontaliere ex D.Lgs. 108/2008, "
                    "trasformazioni eterogenee, scissioni proporzionali "
                    "e non proporzionali.",
                "scope": [
                    "Costituzione e statuti societari",
                    "Aumenti di capitale e perizie ex Art. 2343 c.c.",
                    "Patti parasociali e governance",
                    "Fusioni, scissioni, trasformazioni",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Foro di Roma · Milano · Bruxelles",
            },
            {
                "num":     "02",
                "title":   "M&A e operazioni straordinarie",
                "blurb":
                    "Due diligence, redazione di SPA e shareholders' "
                    "agreements, negoziazione, integrazione post-deal. "
                    "Operiamo lato vendor e lato acquirer, mai entrambi "
                    "nello stesso dossier. Tipologia di operazioni: "
                    "carve-out, JV, exit di private equity, MBO familiari.",
                "scope": [
                    "Vendor due diligence legale",
                    "Buyer-side due diligence e SPA",
                    "Shareholders' agreements e earn-out",
                    "Integrazione post-merger 100 giorni",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Foro di Roma · Milano",
            },
            {
                "num":     "03",
                "title":   "Diritto di famiglia",
                "blurb":
                    "Separazioni consensuali e giudiziali, divorzi, "
                    "regolamento dell'affidamento dei minori, modifiche "
                    "delle condizioni di separazione e divorzio. "
                    "Mediazione familiare in sede di trattativa "
                    "preventiva ex Art. 5 D.Lgs. 28/2010.",
                "scope": [
                    "Separazioni consensuali e giudiziali",
                    "Divorzi contenziosi e congiunti",
                    "Affidamento e mantenimento dei minori",
                    "Mediazione familiare",
                ],
                "lead":   "Avv. Maria Grazia Conti",
                "jurisdiction": "Foro di Roma · Milano",
            },
            {
                "num":     "04",
                "title":   "Successioni e patrimoni",
                "blurb":
                    "Successioni nazionali e internazionali ex "
                    "Reg. UE 650/2012, redazione di testamenti pubblici "
                    "e olografi, divisioni ereditarie, donazioni e "
                    "patti di famiglia ex Art. 768-bis c.c. Trust di "
                    "famiglia regolati dalla Convenzione dell'Aja.",
                "scope": [
                    "Pianificazione successoria internazionale",
                    "Testamenti e patti di famiglia",
                    "Divisioni ereditarie e arbitrati",
                    "Trust e fondazioni familiari",
                ],
                "lead":   "Avv. Maria Grazia Conti",
                "jurisdiction": "Foro di Roma · Milano · Lugano",
            },
            {
                "num":     "05",
                "title":   "Diritto del lavoro",
                "blurb":
                    "Contenzioso individuale e collettivo, "
                    "contrattazione di secondo livello, sicurezza sul "
                    "lavoro ex D.Lgs. 81/2008, licenziamenti ex Art. "
                    "18 St. Lav. e Jobs Act, transazioni in sede "
                    "sindacale ex Art. 411 c.p.c.",
                "scope": [
                    "Contenzioso del lavoro individuale e collettivo",
                    "Licenziamenti per giusta causa e GMO",
                    "Contrattazione di secondo livello",
                    "Sicurezza sul lavoro e D.Lgs. 81/2008",
                ],
                "lead":   "Avv. Federica Ronchi",
                "jurisdiction": "Foro di Roma · Milano",
            },
            {
                "num":     "06",
                "title":   "Diritto penale d'impresa",
                "blurb":
                    "Reati societari ex Art. 2621-2641 c.c., "
                    "responsabilità amministrativa degli enti ex "
                    "D.Lgs. 231/2001, white collar crimes, reati "
                    "tributari ex D.Lgs. 74/2000. Difesa di "
                    "amministratori, sindaci, organismi di vigilanza.",
                "scope": [
                    "Difesa nei procedimenti 231",
                    "Reati societari e tributari",
                    "Modelli organizzativi e OdV",
                    "Indagini interne e whistleblowing",
                ],
                "lead":   "Avv. Lorenzo Marchetti",
                "jurisdiction": "Foro di Roma · Milano · Cassazione",
            },
            {
                "num":     "07",
                "title":   "Contrattualistica commerciale",
                "blurb":
                    "Redazione e negoziazione di contratti commerciali "
                    "italiani e internazionali — distribuzione, "
                    "agenzia, franchising, joint venture, licensing. "
                    "Convenzione di Vienna 1980 sulla vendita "
                    "internazionale di beni mobili.",
                "scope": [
                    "Distribuzione e agenzia commerciale",
                    "Franchising e joint venture",
                    "Licensing IP e know-how",
                    "Contratti internazionali (CISG)",
                ],
                "lead":   "Avv. Stefano Bellini",
                "jurisdiction": "Foro di Roma · Milano · Bruxelles",
            },
            {
                "num":     "08",
                "title":   "Diritto bancario e finanziario",
                "blurb":
                    "Operazioni di finanziamento, garanzie reali e "
                    "personali, contenzioso bancario, anatocismo, "
                    "usura, rinegoziazioni, derivati. Vigilanza "
                    "Banca d'Italia, normativa CRR/CRD IV, MAR e "
                    "abusi di mercato.",
                "scope": [
                    "Finanziamenti corporate e LBO",
                    "Contenzioso bancario e usura",
                    "Strumenti derivati (IRS, FX)",
                    "Vigilanza Banca d'Italia · MAR",
                ],
                "lead":   "Avv. Caterina Albini",
                "jurisdiction": "Foro di Roma · Milano",
            },
            {
                "num":     "09",
                "title":   "Diritto amministrativo",
                "blurb":
                    "Contenzioso davanti ai TAR e al Consiglio di "
                    "Stato, appalti pubblici ex D.Lgs. 36/2023, "
                    "concessioni, autorizzazioni urbanistiche, "
                    "accesso agli atti ex L. 241/1990, ricorsi "
                    "straordinari al Capo dello Stato.",
                "scope": [
                    "Appalti pubblici e concessioni",
                    "Autorizzazioni urbanistiche e VIA",
                    "Accesso agli atti e trasparenza",
                    "Ricorsi TAR e Consiglio di Stato",
                ],
                "lead":   "Avv. Giulio Mancini",
                "jurisdiction": "Foro di Roma · TAR Lazio",
            },
            {
                "num":     "10",
                "title":   "Real estate e immobiliare",
                "blurb":
                    "Acquisizioni e cessioni di patrimoni immobiliari, "
                    "operazioni di sviluppo, fondi immobiliari, "
                    "locazioni commerciali, contenzioso condominiale. "
                    "Verifiche urbanistiche e catastali, atti notarili "
                    "in coordinamento con notaio di fiducia.",
                "scope": [
                    "Acquisizioni e cessioni immobiliari",
                    "Sviluppo e fondi immobiliari",
                    "Locazioni commerciali (L. 392/78)",
                    "Contenzioso condominiale",
                ],
                "lead":   "Avv. Stefano Bellini",
                "jurisdiction": "Foro di Roma · Milano",
            },
            {
                "num":     "11",
                "title":   "Privacy e protezione dei dati",
                "blurb":
                    "Compliance al Regolamento UE 679/2016 (GDPR), "
                    "data mapping, DPIA, nomine del DPO, registro dei "
                    "trattamenti, gestione dei data breach, contenzioso "
                    "con il Garante privacy. AI Act e profilazione "
                    "algoritmica.",
                "scope": [
                    "GDPR compliance e DPIA",
                    "Nomine DPO e registro trattamenti",
                    "Data breach e notifica al Garante",
                    "AI Act e profilazione algoritmica",
                ],
                "lead":   "Avv. Caterina Albini",
                "jurisdiction": "Foro di Roma · Milano",
            },
            {
                "num":     "12",
                "title":   "Arbitrato e ADR",
                "blurb":
                    "Arbitrato ad hoc e amministrato (CCI, CAM, ICC, "
                    "LCIA), mediazione civile e commerciale ex "
                    "D.Lgs. 28/2010, negoziazione assistita ex "
                    "D.L. 132/2014, perizia contrattuale.",
                "scope": [
                    "Arbitrato CCI / CAM / ICC / LCIA",
                    "Mediazione civile e commerciale",
                    "Negoziazione assistita",
                    "Perizia contrattuale e arbitraggio",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Foro di Roma · Milano · Camera Arbitrale",
            },
        ],

        # Process strip — come si svolge un mandato
        "process_label":   "Iter del mandato",
        "process_heading": "Quattro fasi, una sola sequenza",
        "process": [
            ("01", "Colloquio preliminare riservato",
             "Primo incontro con un socio dello studio. Si discute "
             "il perimetro, l'eventuale conflitto di interesse e la "
             "tariffa indicativa. Nessuna proposta scritta in questa "
             "fase, solo valutazione di fattibilità."),
            ("02", "Lettera di mandato",
             "Entro cinque giorni, lettera di mandato scritta con "
             "perimetro dettagliato, deliverable, timeline e "
             "tariffario professionale ex DM 55/2014. Il mandato "
             "viene formalizzato solo con sottoscrizione di entrambe "
             "le parti."),
            ("03", "Esecuzione e patrocinio",
             "Il socio responsabile firma personalmente gli atti "
             "rilevanti e partecipa alle udienze di merito. Il "
             "cliente riceve relazioni periodiche scritte sullo "
             "stato del fascicolo, mai per via telematica non "
             "cifrata."),
            ("04", "Chiusura e archivio",
             "Al passaggio in giudicato o alla chiusura del mandato, "
             "lettera di chiusura riservata con sintesi dell'esito "
             "e parere finale. Archivio cifrato per dieci anni come "
             "da Codice Deontologico Forense."),
        ],

        # Final CTA
        "cta_heading":  "Quale pratica fa al caso vostro?",
        "cta_intro":
            "Se il perimetro non è chiaro, scrivete una breve "
            "descrizione del problema all'indirizzo della segreteria "
            "dello studio. Vi indirizzeremo al socio competente entro "
            "quarantotto ore, anche se il mandato non rientrerà fra "
            "quelli accettabili.",
        "cta_primary":      "Scrivici",
        "cta_primary_href": "contatti",
    },

    # ════════════════════════════════════════════════════════════
    # AVVOCATI (team) — 14 avvocati abilitati
    # ════════════════════════════════════════════════════════════
    "avvocati": {
        "eyebrow":  "Avvocati · 14 abilitati al foro",
        "headline": "Quattordici avvocati, <em>una sola</em> direzione.",
        "intro":
            "Lo studio è composto da quattordici avvocati abilitati "
            "al foro di Roma e Milano — sei soci dell'associazione "
            "professionale e otto avvocati associati. La selezione "
            "avviene per cooptazione, non per acquisizione: ogni "
            "ingresso richiede l'unanimità dei soci.",

        # Card meta labels
        "lawyer_foro_label":  "Foro",
        "lawyer_year_label":  "Iscrizione",
        "lawyer_specialization_label": "Specializzazione",

        # 14 avvocati — 6 soci + 8 associati
        "lawyers": [
            {
                "name":  "Avv. Prof. Alberto Ferri",
                "role":  "Managing partner",
                "specialization": "Diritto societario · M&A · Arbitrato",
                "foro":  "Foro di Roma",
                "year":  "Iscritto dal 1986 · Cassazionista dal 1999",
                "bio":
                    "Figlio del fondatore, ha guidato lo studio dal 2004. "
                    "Professore associato di diritto commerciale a LUISS "
                    "Guido Carli. Autore del volume \"L'aumento di "
                    "capitale nelle società quotate\" (Giuffrè, 2018) e "
                    "di numerosi articoli sulla \"Rivista delle Società\".",
            },
            {
                "name":  "Avv. Maria Grazia Conti",
                "role":  "Socia senior",
                "specialization": "Diritto di famiglia · Successioni",
                "foro":  "Foro di Roma",
                "year":  "Iscritta dal 1991 · Cassazionista dal 2003",
                "bio":
                    "Specialista in successioni internazionali e patti "
                    "di famiglia. Collaboratrice della rivista \"Famiglia "
                    "e Diritto\" dal 2007. Mediatrice familiare iscritta "
                    "all'Ordine Mediatori del Tribunale di Roma.",
            },
            {
                "name":  "Avv. Lorenzo Marchetti",
                "role":  "Socio",
                "specialization": "Penale d'impresa · 231",
                "foro":  "Foro di Roma · Cassazione",
                "year":  "Iscritto dal 1995 · Cassazionista dal 2007",
                "bio":
                    "Già pubblico ministero presso la Procura della "
                    "Repubblica di Milano (1998-2003). Componente "
                    "dell'Organismo di Vigilanza di tre gruppi industriali "
                    "quotati su Euronext Milan. Docente alla Scuola di "
                    "Specializzazione per le Professioni Legali.",
            },
            {
                "name":  "Avv. Federica Ronchi",
                "role":  "Socia",
                "specialization": "Diritto del lavoro · Sicurezza",
                "foro":  "Foro di Roma · Milano",
                "year":  "Iscritta dal 1999",
                "bio":
                    "Specialista in licenziamenti collettivi e "
                    "contrattazione di secondo livello. Consulente di "
                    "tre grandi imprese del settore industriale per "
                    "la negoziazione sindacale. Componente del Comitato "
                    "Pari Opportunità dell'Ordine Avvocati di Roma.",
            },
            {
                "name":  "Avv. Stefano Bellini",
                "role":  "Socio",
                "specialization": "Contrattualistica · Real estate",
                "foro":  "Foro di Roma · Bruxelles",
                "year":  "Iscritto dal 2001",
                "bio":
                    "Esperto in contrattualistica internazionale e "
                    "operazioni immobiliari complesse. Iscritto al Foro "
                    "di Bruxelles per le pratiche di diritto comunitario. "
                    "LL.M. in International Business Law presso "
                    "Université Libre de Bruxelles.",
            },
            {
                "name":  "Avv. Caterina Albini",
                "role":  "Socia",
                "specialization": "Bancario · Privacy & GDPR",
                "foro":  "Foro di Milano",
                "year":  "Iscritta dal 2003",
                "bio":
                    "Coordina la pratica bancaria della sede di Milano. "
                    "Specialista in derivati e strumenti finanziari "
                    "complessi. DPO certificato secondo lo schema UNI "
                    "11697:2017. Autrice di \"GDPR e responsabilità "
                    "del titolare\" (Wolters Kluwer, 2021).",
            },
            {
                "name":  "Avv. Giulio Mancini",
                "role":  "Of counsel",
                "specialization": "Diritto amministrativo · Appalti",
                "foro":  "Foro di Roma · TAR Lazio",
                "year":  "Iscritto dal 1998",
                "bio":
                    "Già magistrato del TAR del Lazio (2002-2014), "
                    "oggi avvocato di parte nei contenziosi davanti "
                    "ai TAR e al Consiglio di Stato. Specialista in "
                    "appalti pubblici e concessioni di servizi. "
                    "Componente del Consiglio Direttivo dell'AIDA.",
            },
            {
                "name":  "Avv. Beatrice Lazzaro",
                "role":  "Avvocato associato",
                "specialization": "Penale d'impresa · Indagini interne",
                "foro":  "Foro di Roma",
                "year":  "Iscritta dal 2008",
                "bio":
                    "Collaboratrice della pratica penale d'impresa dal "
                    "2010. Specializzata in indagini interne aziendali "
                    "e whistleblowing ex D.Lgs. 24/2023. Docente alla "
                    "Master in Compliance 231 presso Università LUMSA.",
            },
            {
                "name":  "Avv. Marco Vergani",
                "role":  "Avvocato associato",
                "specialization": "M&A · Diritto societario",
                "foro":  "Foro di Milano",
                "year":  "Iscritto dal 2011",
                "bio":
                    "Coordinatore della sede di Milano per le operazioni "
                    "di M&A mid-market. Esperienza pregressa in primario "
                    "studio internazionale. Specialista in operazioni "
                    "cross-border Italia-DACH, in particolare con "
                    "controparti tedesche e svizzere.",
            },
            {
                "name":  "Avv. Sara Donati",
                "role":  "Avvocato associato",
                "specialization": "Diritto di famiglia · Minori",
                "foro":  "Foro di Roma",
                "year":  "Iscritta dal 2013",
                "bio":
                    "Specializzata nei procedimenti relativi all'affido "
                    "dei minori e nei procedimenti davanti al Tribunale "
                    "per i Minorenni. Curatrice speciale del minore in "
                    "procedimenti di adozione. Master in Diritto di "
                    "Famiglia presso Università di Roma Tre.",
            },
            {
                "name":  "Avv. Tommaso Ricci",
                "role":  "Avvocato associato",
                "specialization": "Lavoro · Contenzioso collettivo",
                "foro":  "Foro di Milano",
                "year":  "Iscritto dal 2014",
                "bio":
                    "Sede di Milano. Specializzato in contenzioso "
                    "collettivo del lavoro e procedure ex L. 223/1991 "
                    "(licenziamenti collettivi). Esperienza pregressa "
                    "presso direzione legale di gruppo industriale "
                    "quotato del settore manifatturiero.",
            },
            {
                "name":  "Avv. Elisa Falcone",
                "role":  "Avvocato associato",
                "specialization": "Bancario · Contenzioso usura",
                "foro":  "Foro di Milano",
                "year":  "Iscritta dal 2015",
                "bio":
                    "Specializzata nel contenzioso bancario e nelle "
                    "azioni di accertamento dell'anatocismo e dell'usura. "
                    "Coordina la sezione bancaria della sede di Milano. "
                    "Master in Diritto Bancario presso Università Bocconi.",
            },
            {
                "name":  "Avv. Riccardo Zambelli",
                "role":  "Avvocato associato",
                "specialization": "Amministrativo · Urbanistica",
                "foro":  "Foro di Roma · TAR Lazio",
                "year":  "Iscritto dal 2016",
                "bio":
                    "Collabora alla pratica amministrativa con focus "
                    "sull'urbanistica, sulla valutazione di impatto "
                    "ambientale (VIA) e sulle autorizzazioni paesaggistiche. "
                    "Esperienza pregressa presso ufficio legale di un "
                    "grande operatore delle infrastrutture.",
            },
            {
                "name":  "Avv. Chiara Tomei",
                "role":  "Avvocato associato",
                "specialization": "Privacy · AI Act · Tech",
                "foro":  "Foro di Milano",
                "year":  "Iscritta dal 2019",
                "bio":
                    "Specializzata in privacy e protezione dei dati "
                    "personali, con focus sui temi emergenti di "
                    "intelligenza artificiale generativa e adempimenti "
                    "ex AI Act (Reg. UE 2024/1689). Master in Diritto "
                    "delle Nuove Tecnologie presso Università di Pavia.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════
    # NOTABILI (blog_list) — cause notabili e pubblicazioni
    # ════════════════════════════════════════════════════════════
    "notabili": {
        "eyebrow":  "Cause notabili e pubblicazioni · 2018 — 2026",
        "headline": "Sei mandati selezionati, <em>nel pieno rispetto</em> del riserbo.",
        "intro":
            "Una selezione di cause notabili e pubblicazioni recenti. "
            "Per riserbo professionale e in ottemperanza all'Art. 622 "
            "c.p., i nominativi dei clienti non sono mai indicati: le "
            "cause sono identificate per filiera industriale e per "
            "perimetro tecnico, le pubblicazioni per rivista e per "
            "soggetto trattato.",

        # Lead post + list — 6 posts referenced below
        "lead_image": "https://images.pexels.com/photos/5668858/pexels-photo-5668858.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
    },

    # Posts powering blog_detail. URL: /notabili/<slug>/
    "posts": [
        {
            "slug":     "aumento-capitale-quotata-2343cc",
            "kicker":   "Diritto societario",
            "title":    "Aumento di capitale ex Art. 2343 c.c. di società quotata · perizia giurata · 2024",
            "date":     "Marzo 2024",
            "read_min": "8",
            "author":   "Avv. Prof. Alberto Ferri",
            "lede":
                "Su incarico di un gruppo industriale quotato del "
                "settore energetico, lo studio ha assistito il "
                "consiglio di amministrazione nella deliberazione e "
                "nell'esecuzione di un aumento di capitale in natura "
                "per 145 milioni di euro, con conferimento di una "
                "controllata estera valutata mediante perizia giurata "
                "ex Art. 2343 c.c.",
            "body": [
                ("p",
                 "Il mandato ha riguardato l'intera fase deliberativa, "
                 "dalla redazione della relazione illustrativa del "
                 "consiglio di amministrazione ex Art. 2441 c.c. fino "
                 "alla nomina dell'esperto designato dal Tribunale di "
                 "Roma per la perizia giurata di stima della controllata "
                 "conferita."),
                ("h2", "Il quadro normativo"),
                ("p",
                 "L'operazione si è svolta nel pieno rispetto dell'Art. "
                 "2343 c.c. (perizia giurata) e dell'Art. 2441 c.c. "
                 "(diritto di opzione), con esclusione del diritto di "
                 "opzione in favore di un investitore istituzionale "
                 "individuato dal CdA. La procedura ha richiesto "
                 "specifica relazione del collegio sindacale ex Art. "
                 "2441 comma 6 c.c."),
                ("h2", "Il ruolo dello studio"),
                ("p",
                 "Lo studio ha coordinato i rapporti con la Consob "
                 "per il deposito del prospetto di offerta, con il "
                 "Tribunale di Roma per la nomina del perito, con "
                 "il notaio per la verbalizzazione dell'assemblea "
                 "straordinaria e con il revisore per le verifiche "
                 "successive ex Art. 2343-bis c.c."),
                ("blockquote",
                 "Il rispetto della procedura ex Art. 2343 c.c. è "
                 "condizione di validità dell'aumento di capitale. "
                 "Ogni semplificazione operativa che pretenda di "
                 "comprimere i termini di legge espone l'operazione "
                 "al rischio di nullità."),
            ],
        },
        {
            "slug":     "modello-231-gruppo-utility",
            "kicker":   "Penale d'impresa",
            "title":    "Modello organizzativo ex D.Lgs. 231/2001 per gruppo utility quotato",
            "date":     "Novembre 2024",
            "read_min": "11",
            "author":   "Avv. Lorenzo Marchetti",
            "lede":
                "Lo studio ha redatto il modello organizzativo ex "
                "D.Lgs. 231/2001 per un gruppo utility quotato a "
                "seguito del rinnovo dell'organismo di vigilanza. "
                "L'incarico ha incluso la mappatura dei rischi-reato, "
                "il disegno dei protocolli operativi e la formazione "
                "interna a sessantadue dirigenti.",
            "body": [
                ("p",
                 "Il mandato ha avuto durata di nove mesi e si è "
                 "svolto in tre flussi paralleli: mappatura dei "
                 "rischi-reato presupposto, ridisegno dei protocolli "
                 "operativi, formazione obbligatoria al personale "
                 "esposto."),
                ("h2", "Mappatura dei rischi-reato"),
                ("p",
                 "Sono stati mappati i ventidue reati-presupposto "
                 "rilevanti per il settore utility, con particolare "
                 "attenzione ai reati ambientali ex Art. 25-undecies "
                 "D.Lgs. 231/2001 e ai reati contro la pubblica "
                 "amministrazione ex Art. 25 D.Lgs. 231/2001. La "
                 "mappatura ha richiesto interviste a quaranta "
                 "process owner."),
                ("h2", "Disegno dei protocolli"),
                ("p",
                 "I protocolli operativi sono stati ridisegnati "
                 "secondo il principio di separazione delle funzioni "
                 "e di tracciabilità documentale. Particolare attenzione "
                 "è stata posta ai processi di approvvigionamento, "
                 "alle gare d'appalto pubbliche e alla gestione dei "
                 "rapporti con la pubblica amministrazione."),
            ],
        },
        {
            "slug":     "successione-internazionale-reg-650",
            "kicker":   "Successioni internazionali",
            "title":    "Successione internazionale ex Reg. UE 650/2012 · famiglia imprenditoriale Italia-Svizzera",
            "date":     "Settembre 2024",
            "read_min": "9",
            "author":   "Avv. Maria Grazia Conti",
            "lede":
                "Per una famiglia imprenditoriale del Nord-Est con "
                "patrimoni in Italia, Svizzera e Lussemburgo, lo "
                "studio ha coordinato l'apertura della successione "
                "del de cuius — domiciliato a Lugano da oltre vent'anni "
                "— ai sensi del Regolamento UE 650/2012.",
            "body": [
                ("p",
                 "La successione ha posto questioni complesse di "
                 "diritto internazionale privato, in particolare sulla "
                 "professio iuris ex Art. 22 Reg. 650/2012 a favore "
                 "della legge italiana, esercitata dal de cuius mediante "
                 "testamento olografo redatto a Lugano nel 2018."),
                ("h2", "Coordinamento multi-giurisdizionale"),
                ("p",
                 "Lo studio ha coordinato i rapporti con il notaio "
                 "italiano per l'accettazione dell'eredità, con la "
                 "fiduciaria svizzera per la divisione dei conti "
                 "bancari e con il foro di Lussemburgo per la "
                 "liquidazione di una holding lussemburghese."),
                ("h2", "Esito"),
                ("p",
                 "L'intera procedura è stata chiusa in quattordici "
                 "mesi, con accordo divisionale ratificato davanti "
                 "al notaio di Roma. Nessun contenzioso giudiziario, "
                 "imposta di successione liquidata in sede tabellare."),
            ],
        },
        {
            "slug":     "ferri-aumento-capitale-giuffre-2018",
            "kicker":   "Pubblicazione monografica",
            "title":    "\"L'aumento di capitale nelle società quotate\" · Giuffrè · 2018",
            "date":     "2018",
            "read_min": "5",
            "author":   "Avv. Prof. Alberto Ferri",
            "lede":
                "La monografia, edita da Giuffrè Francis Lefebvre "
                "nel 2018, raccoglie l'esperienza professionale "
                "dell'autore in materia di aumenti di capitale di "
                "società quotate sui mercati regolamentati italiani. "
                "Il volume è oggi adottato in tre università italiane "
                "come testo di riferimento del corso di diritto "
                "commerciale.",
            "body": [
                ("p",
                 "Il volume si articola in dodici capitoli che "
                 "ripercorrono le varie tipologie di aumento di "
                 "capitale: in denaro, in natura, gratuiti, riservati, "
                 "con esclusione del diritto di opzione."),
                ("h2", "Struttura dell'opera"),
                ("p",
                 "I primi quattro capitoli affrontano la disciplina "
                 "generale ex Artt. 2438-2444 c.c. I capitoli "
                 "centrali approfondiscono le fattispecie speciali — "
                 "aumenti delegati al CdA, aumenti scindibili e "
                 "inscindibili, aumenti con warrant. Gli ultimi tre "
                 "capitoli sono dedicati alle peculiarità delle "
                 "società quotate."),
            ],
        },
        {
            "slug":     "licenziamento-collettivo-l-223-91",
            "kicker":   "Diritto del lavoro",
            "title":    "Procedura di licenziamento collettivo ex L. 223/1991 · gruppo manifatturiero",
            "date":     "Maggio 2024",
            "read_min": "7",
            "author":   "Avv. Federica Ronchi",
            "lede":
                "Lo studio ha assistito un gruppo manifatturiero "
                "del settore metalmeccanico nella procedura di "
                "licenziamento collettivo ex L. 223/1991, conclusa "
                "con accordo sindacale e ricollocazione del 78% "
                "del personale eccedente.",
            "body": [
                ("p",
                 "La procedura ha riguardato centoquaranta posizioni "
                 "lavorative e si è svolta in due fasi — esame "
                 "congiunto in sede aziendale ex Art. 4 L. 223/1991 "
                 "e successivo esame in sede ministeriale presso il "
                 "Ministero del Lavoro."),
                ("h2", "L'accordo sindacale"),
                ("p",
                 "L'accordo, sottoscritto con tutte le sigle sindacali "
                 "rappresentative, ha previsto l'attivazione di un "
                 "fondo bilaterale di riqualificazione, l'incentivazione "
                 "all'esodo per i lavoratori più anziani e un piano "
                 "di ricollocazione interna per il restante personale."),
                ("h2", "Esito quantitativo"),
                ("p",
                 "Sui centoquaranta dipendenti coinvolti, ventotto "
                 "hanno aderito all'incentivazione all'esodo, "
                 "ottantatré sono stati ricollocati su altre "
                 "linee produttive, ventinove sono stati supportati "
                 "dal fondo bilaterale di outplacement."),
            ],
        },
        {
            "slug":     "carve-out-dach-mid-cap-2023",
            "kicker":   "M&A cross-border",
            "title":    "Carve-out e cessione di divisione industriale a operatore tedesco · 2023",
            "date":     "Dicembre 2023",
            "read_min": "10",
            "author":   "Avv. Marco Vergani",
            "lede":
                "Lo studio ha agito sell-side in un'operazione di "
                "carve-out e cessione di una divisione industriale "
                "(€ 112 milioni di ricavi annui) a un operatore "
                "strategico tedesco, conclusa nel quarto trimestre "
                "del 2023 dopo ventidue settimane di trattativa.",
            "body": [
                ("p",
                 "Il mandato ha riguardato l'intera operazione di "
                 "carve-out — dalla preparazione del teaser alla "
                 "negoziazione dello share purchase agreement, fino "
                 "alle prime sei settimane di integrazione post-merger."),
                ("h2", "Le fasi"),
                ("ol", [
                    "Preparazione del teaser e information memorandum",
                    "Vendor due diligence (legale, fiscale, lavoristica)",
                    "Asta privata su quattro acquirenti potenziali",
                    "Negoziazione SPA e shareholders' agreement",
                    "Closing e integrazione post-merger 100 giorni",
                ]),
                ("h2", "Il risultato"),
                ("p",
                 "Cessione conclusa al multiplo EBITDA di mercato "
                 "(8.4x), con clausola di earn-out su due esercizi. "
                 "Il 100% dei contratti con i tre principali clienti "
                 "DACH è stato rinnovato entro i sei mesi successivi "
                 "al closing."),
            ],
        },
    ],

    # ════════════════════════════════════════════════════════════
    # CONTATTI (contact) — 2 sedi, form riservato
    # ════════════════════════════════════════════════════════════
    "contatti": {
        "eyebrow":  "Consulenza preliminare riservata",
        "headline": "Una conversazione preliminare con un <em>socio dello studio</em>.",
        "intro":
            "Il primo contatto avviene direttamente con un socio "
            "dell'associazione professionale. Si discute il perimetro "
            "del mandato, l'eventuale conflitto di interesse e la "
            "tariffa indicativa — sotto vincolo di riservatezza "
            "professionale ex Art. 622 c.p., prima di qualsiasi "
            "incarico formale.",

        # Form fields
        "form_label":   "Modulo riservato",
        "form_heading": "Compilate il modulo riservato",
        "form_intro":
            "Riceverete conferma di ricezione entro quarantotto ore "
            "lavorative, firmata dal socio responsabile della "
            "competenza richiesta. Le informazioni sono trattate ai "
            "sensi del Regolamento UE 679/2016 e custodite in "
            "archivio cifrato ad accesso limitato ai soci dello "
            "studio.",
        "form_fields": [
            {"name": "name", "label": "Nome", "type": "text", "required": True,
             "placeholder": "Es. Alessandro",
             "helper": "Solo il nome di battesimo, grazie."},
            {"name": "surname", "label": "Cognome", "type": "text", "required": True,
             "placeholder": "Es. Costa",
             "helper": "Come compare nel documento di identità."},
            {"name": "email", "label": "Indirizzo email", "type": "email", "required": True,
             "placeholder": "alessandro.costa@esempio.it",
             "helper": "Per la corrispondenza preliminare. Non utilizzeremo l'indirizzo per altri scopi."},
            {"name": "phone", "label": "Telefono", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "Linea diretta del referente, non centralino."},
            {"name": "capacity", "label": "In qualità di", "type": "select", "required": True,
             "options": [
                 "Privato cittadino",
                 "Imprenditore o socio di società",
                 "Amministratore o sindaco di società",
                 "Direzione legale di gruppo industriale",
                 "Professionista (commercialista, notaio, etc.)",
             ],
             "helper": "Per orientare il colloquio preliminare."},
            {"name": "practice", "label": "Area di pratica", "type": "select", "required": True,
             "options": [
                 "Da definire in colloquio",
                 "Diritto societario",
                 "M&A e operazioni straordinarie",
                 "Diritto di famiglia",
                 "Successioni e patrimoni",
                 "Diritto del lavoro",
                 "Diritto penale d'impresa",
                 "Contrattualistica commerciale",
                 "Diritto bancario e finanziario",
                 "Diritto amministrativo",
                 "Real estate e immobiliare",
                 "Privacy e protezione dei dati",
                 "Arbitrato e ADR",
             ],
             "helper": "Scegliere \"Da definire\" se il perimetro copre più aree."},
            {"name": "urgency", "label": "Urgenza", "type": "select", "required": True,
             "options": [
                 "Entro la settimana corrente",
                 "Entro un mese",
                 "Entro tre mesi",
                 "Esplorativo, nessuna urgenza",
             ],
             "helper": "Aiuta a calendare il socio competente."},
            {"name": "perimeter", "label": "Breve descrizione del problema",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Massimo 800 caratteri. I nominativi di controparti, "
                 "controllate o terzi vengono divulgati solo dopo "
                 "sottoscrizione di NDA reciproca, mai in questo modulo.",
             "helper":
                 "Quanto basta a effettuare il conflict-check preliminare "
                 "e a indirizzare il fascicolo al socio competente. "
                 "I dettagli sensibili si discutono in colloquio."},
        ],

        "form_sections": [
            {"num": "01", "title": "Referente",
             "meta": "La persona che firmerà l'eventuale mandato.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Posizione",
             "meta": "Per il conflict-check preliminare.",
             "fields": ["capacity"]},
            {"num": "03", "title": "Oggetto della consulenza",
             "meta":
                 "Nessun nome di controparte qui — il perimetro tecnico "
                 "si discute in colloquio dopo NDA reciproca.",
             "fields": ["practice", "urgency", "perimeter"]},
            {"num": "04", "title": "Allegati (facoltativi)",
             "meta":
                 "Documenti preliminari, organigrammi o NDA standard "
                 "possono accelerare il colloquio.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "documenti_preliminari",
            "label":    "Documenti preliminari",
            "helper":
                "Documenti preliminari, organigramma societario o "
                "NDA standard. PDF / DOCX · max 15 MB complessivi. "
                "Archivio cifrato ad accesso limitato ai soci dello studio.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Trascinate qui i documenti oppure",
            "link":     "selezionate dall'archivio",
            "meta":     "PDF / DOCX · max 15 MB · archivio cifrato",
        },

        "form_submit_label": "Invia richiesta riservata",
        "form_submit_note":
            "Conferma di ricezione firmata da un socio entro quarantotto "
            "ore lavorative. Nessun BDR, nessuna automazione, nessuna "
            "comunicazione commerciale.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi del "
            "Regolamento UE 679/2016 e dichiaro di essere informato "
            "che i dati sono custoditi in archivio cifrato ad accesso "
            "limitato ai soci dello Studio Legale Ferri. I dati non "
            "vengono comunicati a terzi senza esplicito consenso scritto.",

        # Office meta-row labels (lifted from skin for i18n)
        "office_address_label": "Indirizzo",
        "office_area_label":    "Zona",
        "office_phone_label":   "Telefono",
        "office_email_label":   "Email",
        "office_hours_label":   "Orario",

        # Sidebar — sedi + canali diretti
        "offices_label":   "Le sedi",
        "offices": [
            {
                "city":    "Roma",
                "tag":     "Sede principale",
                "address": "Via Piemonte 39 · 00187",
                "area":    "Quirinale · vicino Piazza Barberini",
                "phone":   "+39 06 4567 2300",
                "email":   "roma@studioferri.legal",
                "hours":   "Lun – Ven · 09:00 – 19:00",
            },
            {
                "city":    "Milano",
                "tag":     "Sede di Milano",
                "address": "Corso Venezia 11 · 20121",
                "area":    "Porta Venezia · vicino Giardini Pubblici",
                "phone":   "+39 02 7634 5500",
                "email":   "milano@studioferri.legal",
                "hours":   "Lun – Ven · 09:00 – 19:00",
            },
        ],

        "channels_label": "Canali diretti",
        "channels": [
            ("Segreteria dello studio",
             "+39 06 4567 2300",
             "Lun – Ven · 09:00 – 19:00"),
            ("Email istituzionale",
             "studio@studioferri.legal",
             "Risposta entro 48 ore lavorative"),
            ("PEC certificata",
             "studio.ferri@cert.ordineavvocatiroma.it",
             "Per atti e notifiche"),
        ],

        "footnote":
            "Lo Studio Legale Ferri non rilascia opinioni preliminari "
            "via email senza un primo colloquio con un socio. Le "
            "informazioni amministrative (parametri tariffari indicativi, "
            "modalità di fatturazione, criteri di accettazione del "
            "mandato) vengono illustrate nel corso del colloquio "
            "preliminare riservato, mai per iscritto in fase preliminare.",
    },
}


# ─────────────────────────────────────────────────────────────────
# D-047 — chrome-authoring contract.
# Every visible string in the lawyer/classic-gold skin templates
# must come from THIS file (or from chrome.* / dna.content.*).
# Zero literal "Ferri", "1962", "Roma", "Via Piemonte", partner
# names, headline text, or other brand-specific strings in the
# .html files. When a new label is needed in the skin, add it here
# first (preferably under `site` if shared across pages, or under
# the page block if scoped) and read it via `{{ page_data.* }}` /
# `{{ site.* }}`.
# ─────────────────────────────────────────────────────────────────
