"""Fiscus — Studio Tributario (business / corporate-suite archetype) content.

Wave 2 Pilot #1 — Phase X.4 (Session 80, 2026-04-20).

Editorial identity: independent Italian studio tributario based in Milan,
founded 2003, iscritto ODCEC. Serves partite IVA, PMI manifattura, studi
professionali and wealth privato. The voice is formal-precise (register
`Lei` nel primo piano-CTA, `noi/voi` quando si parla dello studio + cliente),
non caldo-corporate ma nemmeno freddo — il registro di chi spiega una
normativa con pazienza, senza semplificare. Photo direction: scrivanie con
documenti, portraits focalizzati in giacca senza cravatta, ambienti editorial
con profondità di campo ridotta — mai "stock handshake" o grafici a torta.

Differentiation vs Pragma (D-054 10-gate — recorded here for reviewers):
 1. Hero image:        scrivania con documenti e laptop (business-fiscal[0])
                       vs Pragma's boardroom long-table (business-corporate[0])
 2. First-2 imagery:   fiscal desk + modern office interior (business-fiscal[0,1])
                       vs Pragma boardroom + corporate atrium (business-corporate[0,1])
 3. Silhouette:        55/45 split serif L + photo R + fiscal-calendar-strip
                       vs Pragma KPI-strip over sectors-ribbon
 4. Section order:     hero → pillars → kpi → fiscal-calendar → sectors → cases → cta
                       vs Pragma hero → pillars → kpi → sectors → leadership → cases → cta
 5. Primary CTA:       "Primo appuntamento" + P.IVA/CF form + fascia oraria
                       vs Pragma "Fissa una call privata" + NDA-ready boardroom form
 6. Block rhythm:      airy editorial chapters with document-centric details
                       vs Pragma airy editorial chapters with board-portrait details
 7. Macro tone:        warm-neutral cream + blu-notte accent + gold filigrana
                       (institutional-fiscal, document-ready)
                       vs Pragma cream paper + navy slate + emerald accent
                       (institutional-advisory, boardroom-ready)
 8. Imagery direction: fiscal desks + tax documents + focused professional
                       portraits (no tie, Italian SMB credibility)
                       vs Pragma boardroom executives + corporate HQ facilities
 9. Typography:        IBM Plex Serif + IBM Plex Sans (document-transitional)
                       vs Pragma Merriweather + Inter (editorial-serif)
10. Voice anchor:      "Ci occupiamo dell'adempimento corretto, non della
                       trovata" — commercialista presidio, scadenze-first
                       vs Pragma "Dove si prendono le decisioni che contano" —
                       board advisory, strategy-first

Page kinds:
- home, about, services, case_study_list, case_study_detail, contact
  (reuses Pragma's skin page kinds — D-087 archetype-reuse contract)
"""
from __future__ import annotations

from typing import Any


FISCUS_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Studio",        "kind": "home"},
        {"slug": "lo-studio",     "label": "Lo studio",     "kind": "about"},
        {"slug": "competenze",    "label": "Competenze",    "kind": "services"},
        {"slug": "casi-seguiti",  "label": "Casi seguiti",  "kind": "case_study_list"},
        {"slug": "contatti",      "label": "Contatti",      "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial": "F",
        "logo_word":    "Fiscus",
        "tag":          "Studio tributario · Milano · iscritto ODCEC dal 2003",
        "phone":        "+39 02 4951 3388",
        "email":        "segreteria@fiscusstudio.it",
        "address":      "Via Melzo 14 · 20129 Milano",
        "hours_compact": "Lun – Ven · 9:00 – 18:30 · su appuntamento",
        "hours_footer_rows": [
            "Sabato · su appuntamento in prossimità scadenze",
            "Domenica · chiuso",
        ],
        "license":      "Iscritti ODCEC Milano · Sezione A · dal 2003",
        "footer_intro":
            "Studio tributario indipendente per partite IVA, PMI e famiglie "
            "imprenditoriali. Dichiarazione dei redditi, bilancio, contenzioso "
            "tributario e pianificazione fiscale pluriennale. Sede a Milano, "
            "rapporto di consulenza ricorrente — non prestazioni una tantum.",
        "foot_studio":   "Lo studio",
        "foot_pages":    "Sezioni",
        "foot_contact":  "Contatti",
        "foot_offices":  "Sede",
        "offices_footer_rows": [
            "Milano · Porta Venezia",
        ],
        # Case study cross-page meta labels
        "case_practice_label":     "Area",
        "case_year_label":         "Anno",
        "case_duration_label":     "Durata",
        "case_lead_label":         "Referente",
        "case_lead_partner_label": "Referente",
        "case_team_label":         "Team & timeline",
        "case_timeline_label":     "Timeline",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Studio tributario · Milano · iscritto ODCEC dal 2003",
        "headline":    "L'adempimento <em>corretto</em>, non la trovata.",
        "intro":
            "Studio tributario per partite IVA, PMI e famiglie imprenditoriali. "
            "Dichiarazione dei redditi, bilancio, contenzioso tributario e "
            "pianificazione fiscale pluriennale — senza promesse di risparmio, "
            "con il calendario delle scadenze alla mano.",
        "primary_cta":   "Primo appuntamento",
        "primary_href":  "contatti",
        "secondary_cta": "Scarica la guida scadenze",
        "secondary_href":"lo-studio",

        # Right-hand hero photo + credit overlay (fiscal-desk direction)
        "hero_image":              "https://images.pexels.com/photos/8927688/pexels-photo-8927688.jpeg?auto=compress&cs=tinysrgb&w=1600",
        "hero_image_credit_left":  ("Direzione",       "Dott. A. Ruffini"),
        "hero_image_credit_right": ("Anno fondazione", "2003"),
        "hero_meta_strip": [
            ("Sede",            "Milano · Porta Venezia"),
            ("Albo ODCEC",      "4 iscritti · dal 2003"),
            ("Clienti attivi",  "260 partite IVA"),
        ],

        # Advisory pillars — three practice areas on home
        "pillars_label":   "Aree di competenza",
        "pillars_heading": "Tre pratiche, una sola firma",
        "pillars_intro":
            "Un solo team multidisciplinare segue ogni cliente. Il commercialista "
            "iscritto albo non è un costo da minimizzare: è un presidio da scegliere.",
        "pillars": [
            ("01", "Dichiarazione & bilancio",
             "Dichiarazione dei redditi, quadro RW per redditi esteri, "
             "certificazione unica, bilancio d'esercizio — audit-ready, con "
             "calendario delle revisioni concordato a gennaio e firma entro "
             "le scadenze dell'Agenzia Entrate."),
            ("02", "Contenzioso tributario",
             "Assistenza in accertamento, ravvedimento operoso, ricorso in "
             "Commissione Tributaria Provinciale e Regionale. Mai promesse "
             "di esito, sempre una stima preliminare delle probabilità — "
             "per iscritto, in carta intestata, prima della delega."),
            ("03", "Wealth & passaggio generazionale",
             "Pianificazione fiscale pluriennale, holding di famiglia, "
             "successione e donazione — per patrimoni privati medio-alti "
             "e famiglie imprenditoriali che preparano il passaggio di "
             "generazione in un orizzonte di 5-10 anni."),
        ],

        # KPI strip — document the studio's continuity track record
        "kpi_heading": "Ventidue anni di pratica continuativa",
        "kpi_strip": [
            ("22",       "anni dalla fondazione"),
            ("260",      "partite IVA in portafoglio"),
            ("€ 180 M",  "fatturato clienti aggregato"),
            ("0",        "sanzioni non previste nel 2025"),
        ],

        # Sectors ribbon — the client base
        "sectors_label": "Settori dei clienti",
        "sectors": [
            "Partite IVA & freelance",
            "PMI manifattura",
            "Studi professionali",
            "Wealth privato",
            "Immobiliare",
        ],

        # Trust band — anonymized client categories (commercialisti don't
        # disclose client logos per secreto professionale)
        "trust_label":   "Seguono con Fiscus la propria fiscalità",
        "trust_logos":   [
            "PARTITE IVA INDIVIDUALI",
            "STUDI DI CONSULENZA",
            "PMI MANIFATTURIERE",
            "FAMIGLIE IMPRENDITORIALI",
            "IMMOBILIARI PRIVATE",
            "PROFESSIONISTI ISCRITTI ALBO",
        ],

        # Leadership preview — 3 partners on home
        "leadership_label":   "Direzione",
        "leadership_heading": "I commercialisti che siederanno al vostro tavolo",
        "leadership_intro":
            "Ogni cliente è seguito personalmente da almeno un socio iscritto "
            "ODCEC. Nessun junior delega, nessuna rotazione silenziosa — il "
            "referente che incontrate in prima visita firma le dichiarazioni "
            "e risponde degli adempimenti.",
        "leadership": [
            {
                "name":  "Dott. Andrea Ruffini",
                "role":  "Socio fondatore · Dichiarazione & bilancio",
                "bio":
                    "Commercialista iscritto ODCEC Milano dal 1999, sezione A. "
                    "Revisore legale iscritto al Registro dei Revisori Legali "
                    "dal 2004. Dottore commercialista con specializzazione in "
                    "fiscalità d'impresa e bilancio. Fondatore dello studio "
                    "nel 2003 insieme alla Dott.ssa Balestrieri.",
                "credentials": [
                    "ODCEC Milano n. 4488/A (dal 1999)",
                    "Revisore Legale n. 137952 (dal 2004)",
                    "Università Bocconi — CLEA '96",
                ],
            },
            {
                "name":  "Dott.ssa Ilaria Balestrieri",
                "role":  "Socia · Contenzioso tributario",
                "bio":
                    "Commercialista iscritta ODCEC Milano dal 2001, sezione A. "
                    "Cassazionista iscritta all'albo degli avvocati di Milano "
                    "dal 2010, specializzata in contenzioso tributario. "
                    "Patrocina davanti alle Commissioni Tributarie Provinciali "
                    "e Regionali della Lombardia e della Piemonte.",
                "credentials": [
                    "ODCEC Milano n. 5611/A (dal 2001)",
                    "Ordine Avvocati Milano (dal 2010)",
                    "Cassazionista iscritta dal 2018",
                ],
            },
            {
                "name":  "Dott. Stefano Conti",
                "role":  "Socio · Wealth & passaggio generazionale",
                "bio":
                    "Commercialista iscritto ODCEC Milano dal 2008, sezione A. "
                    "Specialist in pianificazione patrimoniale per famiglie "
                    "imprenditoriali — holding, trust, successione. Entrato in "
                    "studio nel 2014, socio dal 2019. Docente a contratto di "
                    "fiscalità internazionale alla LIUC Castellanza.",
                "credentials": [
                    "ODCEC Milano n. 7912/A (dal 2008)",
                    "LL.M. Diritto Tributario Bocconi",
                    "TEP · Society of Trust and Estate Practitioners",
                ],
            },
        ],

        # Case studies preview — three recent mandates on home
        "cases_label":   "Casi seguiti",
        "cases_heading": "Tre casi, tre aree di competenza",
        "cases_intro":
            "Una selezione recente di clienti seguiti negli ultimi tre anni. "
            "Per secreto professionale i nomi sono sostituiti dal codice settore, "
            "ma le cifre sono verificabili in fase di reference call.",

        # Final CTA band before footer — appointment-focused
        "cta_label":     "Primo appuntamento",
        "cta_heading":   "Quarantacinque minuti, agenda aperta, nessun impegno",
        "cta_intro":
            "La prima visita avviene con un socio iscritto ODCEC. "
            "Discutiamo l'area di competenza, l'orizzonte temporale del rapporto "
            "e la parcella indicativa — prima di qualsiasi delega firmata. "
            "I clienti esistenti prenotano nello spazio riservato.",
        "cta_primary":   "Richiedi appuntamento",
        "cta_primary_href": "contatti",
        "cta_secondary": "Scarica la guida scadenze",
        "cta_secondary_href": "lo-studio",
    },

    # ─── LO STUDIO (about + values + team + history) ────────────
    "lo-studio": {
        "eyebrow":   "Lo studio · 2003 — 2026",
        "headline":  "Uno studio tributario <em>indipendente</em>, ventidue anni di pratica continuativa.",
        "intro":
            "Fiscus nasce a Milano nel 2003 dall'incontro fra Andrea Ruffini e "
            "Ilaria Balestrieri — due commercialisti iscritti ODCEC con "
            "formazione in fiscalità d'impresa e contenzioso tributario. "
            "Siamo cresciuti per cooptazione, mai per acquisizione, e "
            "abbiamo mantenuto l'indipendenza dal capitale di terzi.",

        # Studio history — 5-step timeline
        "history_label":   "Storia dello studio",
        "history_heading": "Cinque tappe, ventidue anni",
        "history_intro":
            "Cinque date che hanno definito Fiscus. Ognuna riflette una scelta "
            "strutturale — di indipendenza, di specializzazione, di perimetro — "
            "che ancora oggi orienta il modo in cui accettiamo i nuovi clienti.",
        "history": [
            ("2003", "Fondazione",
             "Andrea Ruffini e Ilaria Balestrieri aprono Fiscus in via Melzo, "
             "con dodici clienti già in portafoglio — tutti ereditati dallo "
             "studio precedente con il consenso esplicito dei clienti stessi."),
            ("2008", "Pratica contenzioso tributario",
             "L'iscrizione di Ilaria Balestrieri all'albo degli avvocati apre "
             "la pratica contenzioso: ricorsi in CTP/CTR, accertamenti, "
             "ravvedimento. Prima udienza presso CTP Milano nel marzo 2009."),
            ("2014", "Ingresso del Dott. Conti",
             "Stefano Conti entra come associato per costituire la pratica "
             "wealth — holding di famiglia, trust, passaggio generazionale. "
             "Socio dal 2019 dopo cinque anni di affiancamento."),
            ("2020", "Digitalizzazione della dichiarazione",
             "Integrazione completa con Agenzia Entrate via Entratel e "
             "fatturazione elettronica. Archivio documentale cifrato con "
             "retention decennale e accesso cliente via area riservata."),
            ("2024", "Pratica revisione legale",
             "Andrea Ruffini formalizza la pratica revisione contabile per "
             "PMI con obbligo di collegio sindacale. Tre mandati di revisione "
             "attivi entro dicembre 2024."),
        ],

        # Method / values — 4 principi
        "values_label":   "Metodo",
        "values_heading": "Quattro principi <em>non negoziabili</em>",
        "values_intro":
            "Le quattro regole che separano un cliente Fiscus da un rapporto di "
            "consulenza ordinaria. Sono scritte in carta intestata sul mandato "
            "di delega — non solo in questa pagina.",
        "values": [
            ("01", "Indipendenza dal capitale",
             "Il capitale dello studio è interamente in mano ai soci attivi. "
             "Nessun conferimento di gruppi, nessun fondo in minoranza, "
             "nessun azionista esterno. La scelta dei clienti non è mai "
             "influenzata da agenda di terzi — e i clienti storici sanno "
             "che il rapporto non cambia colore perché è cambiato un socio."),
            ("02", "Un socio per ogni cliente",
             "Ogni cliente ha un socio di riferimento iscritto ODCEC che "
             "segue personalmente la pratica dall'apertura del fascicolo "
             "alla firma delle dichiarazioni. Il socio incontrato in prima "
             "visita risponde degli adempimenti — non deleghe silenziose, "
             "non rotazioni a fine anno."),
            ("03", "Nessuna promessa di risparmio",
             "Non firmiamo preventivi con promesse di riduzione fiscale in "
             "percentuale: è contrario al codice deontologico ODCEC, ed è il "
             "sintomo di rapporti opportunistici. Il nostro mestiere è "
             "applicare la normativa correttamente e segnalare gli strumenti "
             "agevolativi quando esistono."),
            ("04", "Onorari a forfait trasparente",
             "Tariffa annuale concordata a dicembre per l'anno successivo, "
             "revisionata solo in caso di oggettiva variazione del perimetro "
             "(nuova sede, nuova partita IVA, nuovo ramo d'azienda). Nessuna "
             "fatturazione a consumo nascosto, nessuna commissione retro."),
        ],

        # Full team — 3 soci + 4 collaboratori iscritti albo o praticanti
        "team_label":   "Equipe",
        "team_heading": "Tre soci, quattro collaboratori, una sola governance",
        "team_intro":
            "Le persone che seguiranno il vostro mandato. Ogni dichiarazione è "
            "firmata da un socio — i collaboratori affiancano sulla raccolta "
            "dati, la verifica preliminare e la gestione della documentazione.",
        "team": [
            {"name": "Dott. Andrea Ruffini",
             "role": "Socio fondatore · Dichiarazione & bilancio · Revisore legale",
             "office": "Milano",
             "bio": "Commercialista iscritto ODCEC dal 1999 + revisore legale "
                    "dal 2004. Bocconi CLEA '96. Fondatore dello studio."},
            {"name": "Dott.ssa Ilaria Balestrieri",
             "role": "Socia · Contenzioso tributario · Cassazionista",
             "office": "Milano",
             "bio": "Commercialista iscritta ODCEC dal 2001 + avvocato "
                    "cassazionista dal 2018. Patrocina in Lombardia e Piemonte."},
            {"name": "Dott. Stefano Conti",
             "role": "Socio · Wealth & passaggio generazionale · Docente LIUC",
             "office": "Milano",
             "bio": "Commercialista iscritto ODCEC dal 2008. LL.M. Diritto "
                    "Tributario Bocconi. TEP dal 2021."},
            {"name": "Dott.ssa Serena Lomazzi",
             "role": "Collaboratrice · Dichiarazione persone fisiche",
             "office": "Milano",
             "bio": "Commercialista iscritta ODCEC dal 2017. Coordina la "
                    "raccolta dati e la compilazione dichiarazioni 730 e RPF."},
            {"name": "Dott. Giacomo Prevedini",
             "role": "Collaboratore · Bilancio PMI · Praticante revisore",
             "office": "Milano",
             "bio": "Commercialista iscritto ODCEC dal 2021. Segue la "
                    "contabilità ordinaria e la chiusura bilanci per le PMI "
                    "manifatturiere del portafoglio."},
            {"name": "Rag. Nadia Kouadio",
             "role": "Responsabile contabilità · Paghe & contributi",
             "office": "Milano",
             "bio": "Ragioniera iscritta all'Albo Consulenti del Lavoro "
                    "dal 2012. Gestisce la parte paghe in collaborazione "
                    "con un CdL esterno, e la contabilità ordinaria."},
        ],

        # Coordinates strip
        "coordinates_label": "Sede",
        "coordinates": [
            ("Milano", "Via Melzo 14 · 20129 · Porta Venezia — a 200 metri da MM Porta Venezia"),
        ],

        # Page-level CTA
        "cta_heading": "Un primo incontro conoscitivo",
        "cta_intro":
            "I primi quarantacinque minuti con un socio sono una conversazione "
            "esplorativa, non una proposta commerciale. Si discute l'area di "
            "competenza, l'orizzonte temporale e la parcella indicativa. "
            "Al termine, siete liberi di scegliere un altro studio — "
            "e di noleggiare con sé tutta la documentazione preliminare.",
        "cta_primary":  "Richiedi appuntamento",
        "cta_primary_href": "contatti",
    },

    # ─── COMPETENZE (services) ──────────────────────────────────
    "competenze": {
        "eyebrow":  "Aree di competenza · 2026",
        "headline": "Sei aree di competenza, <em>una sola firma</em>.",
        "intro":
            "Le sei aree di pratica di Fiscus. Ogni cliente accede al team "
            "multidisciplinare — non si paga per ciascuna area separatamente, "
            "la parcella annuale copre la combinazione di competenze necessarie "
            "al mandato.",

        # Card meta labels
        "svc_duration_label": "Durata tipica",
        "svc_leader_label":   "Socio di riferimento",

        # 6 areas in airy cards
        "services": [
            {
                "num":   "01",
                "title": "Dichiarazione dei redditi & fiscalità ordinaria",
                "blurb":
                    "Dichiarazione dei redditi (Modello Redditi PF · SP · SC · ENC), "
                    "modello 730, quadro RW per redditi esteri, certificazione unica. "
                    "Lavoriamo su calendario concordato a gennaio, con scadenze "
                    "interne 30 giorni prima dell'Agenzia Entrate — perché una "
                    "dichiarazione firmata il 30 settembre è meglio del 30 novembre.",
                "scope": [
                    "Modello Redditi PF / SP / SC / ENC",
                    "Modello 730 per dipendenti e pensionati",
                    "Quadro RW — monitoraggio fiscale redditi esteri",
                    "Certificazione Unica per sostituti d'imposta",
                    "Ravvedimento operoso per dichiarazioni integrative",
                ],
                "duration": "Rapporto annuale ricorrente",
                "leader":   "Dott. Andrea Ruffini",
            },
            {
                "num":   "02",
                "title": "Bilancio d'esercizio & contabilità ordinaria",
                "blurb":
                    "Contabilità ordinaria, bilancio d'esercizio CEE, nota integrativa, "
                    "relazione sulla gestione, verbale assembleare. Per le PMI con "
                    "collegio sindacale curiamo anche la predisposizione della "
                    "documentazione per il revisore legale — audit-ready entro "
                    "marzo, pubblicazione Camera di Commercio entro maggio.",
                "scope": [
                    "Contabilità ordinaria e semplificata",
                    "Bilancio d'esercizio CEE + nota integrativa",
                    "Deposito bilancio Camera di Commercio",
                    "Relazione sulla gestione per società di capitali",
                    "Assistenza al collegio sindacale e revisore esterno",
                ],
                "duration": "Rapporto annuale ricorrente",
                "leader":   "Dott. Andrea Ruffini",
            },
            {
                "num":   "03",
                "title": "Contenzioso tributario",
                "blurb":
                    "Assistenza in fase di accertamento con adesione, ravvedimento "
                    "operoso, ricorso in Commissione Tributaria Provinciale e "
                    "Regionale, conciliazione giudiziale. Patrocino in Lombardia "
                    "e Piemonte. Per ogni pratica forniamo una stima preliminare "
                    "delle probabilità per iscritto, prima della delega.",
                "scope": [
                    "Accertamento con adesione",
                    "Ravvedimento operoso e rateizzazioni",
                    "Ricorso CTP · CTR · Cassazione (con avvocato)",
                    "Conciliazione giudiziale",
                    "Istanze di autotutela all'Agenzia Entrate",
                ],
                "duration": "Da 3 a 24 mesi secondo grado",
                "leader":   "Dott.ssa Ilaria Balestrieri",
            },
            {
                "num":   "04",
                "title": "Pianificazione fiscale & wealth",
                "blurb":
                    "Pianificazione fiscale pluriennale per patrimoni privati "
                    "medio-alti e famiglie imprenditoriali. Holding di famiglia, "
                    "trust, fondazioni, polizze assicurative fiscalmente efficienti, "
                    "pianificazione successoria. Sempre con orizzonte di 5-10 anni — "
                    "non con promesse fiscali annuali.",
                "scope": [
                    "Holding di famiglia e patti parasociali",
                    "Trust e fondazioni di famiglia",
                    "Pianificazione successoria e donazione",
                    "Strutturazione polizze assicurative IV ramo",
                    "Valutazione strumenti agevolativi (PIR, ELTIF)",
                ],
                "duration": "12 – 36 mesi per riassetto strutturale",
                "leader":   "Dott. Stefano Conti",
            },
            {
                "num":   "05",
                "title": "Consulenza del lavoro & sostituto d'imposta",
                "blurb":
                    "Gestione paghe, contributi, sostituto d'imposta per PMI e studi "
                    "professionali — in collaborazione con un consulente del lavoro "
                    "esterno iscritto albo CdL. Curiamo la parte fiscale e "
                    "contabile; il CdL cura la parte giuslavoristica e previdenziale.",
                "scope": [
                    "Elaborazione cedolini e F24 mensili",
                    "Certificazione Unica sostituto d'imposta",
                    "Modello 770",
                    "Assistenza in verifica INPS / INAIL / Ispettorato",
                    "Coordinamento con CdL esterno (Rag. Kouadio)",
                ],
                "duration": "Rapporto mensile ricorrente",
                "leader":   "Rag. Nadia Kouadio · Dott. A. Ruffini",
            },
            {
                "num":   "06",
                "title": "Revisione legale & collegio sindacale",
                "blurb":
                    "Revisione legale dei conti per PMI con obbligo di collegio "
                    "sindacale — società per azioni non quotate, società a "
                    "responsabilità limitata che superano i limiti di cui all'art. "
                    "2477 c.c. Attualmente tre mandati attivi. Ci presentiamo sempre "
                    "come revisore esterno, mai come sindaco interno dello stesso gruppo.",
                "scope": [
                    "Relazione di revisione legale ex D.Lgs. 39/2010",
                    "Verifica periodica dei conti trimestrale",
                    "Pianificazione ISA Italia della revisione",
                    "Comunicazione con collegio sindacale interno",
                    "Relazione in assemblea dei soci",
                ],
                "duration": "Rapporto triennale o novennale",
                "leader":   "Dott. Andrea Ruffini",
            },
        ],

        # Process — how a new client onboarding is run
        "process_label":   "Come lavoriamo",
        "process_heading": "Quattro passaggi, una sola sequenza",
        "process": [
            ("01", "Primo appuntamento",
             "Quarantacinque minuti riservati con un socio iscritto ODCEC. "
             "Si discute area di competenza, orizzonte temporale e parcella "
             "indicativa. Nessuna delega firmata, nessun costo."),
            ("02", "Preventivo scritto",
             "Entro sette giorni lavorativi, un preventivo di tre pagine "
             "con perimetro del mandato, elenco adempimenti, calendario "
             "delle scadenze interne e parcella annuale concordata."),
            ("03", "Apertura fascicolo",
             "Delega all'Agenzia Entrate via Entratel, trasferimento "
             "documentazione dal commercialista precedente (se esistente), "
             "apertura area cliente riservata sull'archivio cifrato."),
            ("04", "Rapporto continuativo",
             "Un socio di riferimento per tutto il rapporto. Scadenze "
             "presidiate 30 giorni prima delle date Agenzia Entrate. "
             "Review annuale a dicembre per l'anno successivo."),
        ],

        # Final CTA
        "cta_heading":   "Quale area di competenza fa al caso vostro?",
        "cta_intro":
            "Se il perimetro non è chiaro, inviateci una breve descrizione "
            "della situazione (tipo di impresa, anno di apertura, eventuali "
            "adempimenti scaduti). Rispondiamo entro 48 ore lavorative — "
            "anche se la risposta è \"non siamo lo studio giusto\".",
        "cta_primary":   "Scrivici",
        "cta_primary_href": "contatti",
    },

    # ─── CASI SEGUITI (case-studies list) ───────────────────────
    "casi-seguiti": {
        "eyebrow":  "Casi seguiti · 2022 — 2026",
        "headline": "Tre casi, <em>tre aree di competenza</em>.",
        "intro":
            "Una selezione di casi seguiti negli ultimi quattro anni. I clienti "
            "sono identificati tramite codice settore in osservanza del secreto "
            "professionale (art. 199 c.p.p. e Codice Deontologico ODCEC), ma "
            "le cifre sono reali e verificabili tramite reference call con "
            "il referente interno del cliente.",

        "cases_label": "Casi",
        "cases_intro":
            "Selezione bilanciata sulle tre aree principali — dichiarazione & "
            "bilancio, contenzioso, wealth. L'elenco completo dei casi disponibili "
            "come reference è fornito in formato PDF tramite la pagina contatti.",

        "cta_heading":   "Un caso simile al vostro?",
        "cta_intro":
            "I dossier completi (perimetro, cifre aggregate, possibile reference "
            "call con il referente interno del cliente) sono accessibili dietro "
            "firma di impegno di riservatezza reciproca. La firma avviene durante "
            "il primo appuntamento, prima di qualsiasi impegno di parcella.",
        "cta_primary":   "Richiedi i dossier completi",
        "cta_primary_href": "contatti",
    },

    # Posts powering case_study_detail. URL: /casi-seguiti/<slug>/
    "posts": [
        {
            "slug":     "pmi-manifattura-bilancio-revisione",
            "title":    "PMI manifatturiera lombarda · impianto revisione legale",
            "category": "Dichiarazione & bilancio",
            "year":     "2025",
            "duration": "10 settimane + mandato triennale",
            "client_code":
                "Industria manifatturiera · Brescia · 42 dipendenti · "
                "€ 12,4 M ricavi · S.r.l. con collegio sindacale ex art. 2477",
            "lead":
                "Primo esercizio con obbligo di revisione legale dopo superamento "
                "dei limiti di cui all'art. 2477 c.c. Il cliente ha incaricato "
                "Fiscus come revisore esterno in continuità con il rapporto "
                "tributario ordinario di lungo corso.",
            "sections": [
                {
                    "label": "Il problema",
                    "heading": "Passaggio a collegio sindacale in corso d'anno",
                    "body":
                        "La società ha superato per il secondo anno consecutivo "
                        "i limiti dimensionali previsti dall'art. 2477 c.c. "
                        "(ricavi > € 8,8 M, attivo > € 4,4 M, dipendenti > 50). "
                        "Il collegio sindacale è stato nominato in assemblea a "
                        "marzo 2025, ed era necessario incaricare un revisore "
                        "legale esterno ex D.Lgs. 39/2010 entro tre mesi. "
                        "La società aveva preferenza per la continuità con lo "
                        "studio tributario storico — purché senza conflitti di "
                        "interesse in punto di indipendenza.",
                },
                {
                    "label": "L'approccio",
                    "heading": "Separazione delle pratiche e pianificazione ISA",
                    "body":
                        "Fiscus ha accettato il mandato di revisione sotto "
                        "condizione di segregazione operativa: un socio diverso "
                        "segue la pratica tributaria (Dott. A. Ruffini) e la "
                        "pratica revisione (Dott.ssa I. Balestrieri, iscritta al "
                        "Registro dei Revisori dal 2011). Pianificazione della "
                        "revisione secondo ISA Italia 315 — valutazione del "
                        "sistema di controllo interno, identificazione dei rischi "
                        "significativi, determinazione della materialità. Il "
                        "piano di revisione è stato condiviso con il collegio "
                        "sindacale prima dell'esecuzione.",
                },
                {
                    "label": "Il risultato",
                    "heading": "Relazione di revisione senza rilievi",
                    "body":
                        "Relazione di revisione ex art. 14 D.Lgs. 39/2010 "
                        "pubblicata a maggio 2025 senza rilievi, senza richiami "
                        "di informativa e senza incertezze significative. "
                        "La revisione ha evidenziato due raccomandazioni di "
                        "rafforzamento del sistema di controllo interno (segregation "
                        "of duties nel ciclo acquisti, procedura di fine mese "
                        "inventariale) che la società ha implementato entro "
                        "settembre. Mandato di revisione triennale confermato "
                        "per gli esercizi 2025-2027.",
                },
            ],
            "kpi": [
                ("0",        "rilievi nella relazione di revisione"),
                ("2",        "raccomandazioni implementate dal cliente"),
                ("3 anni",   "durata mandato di revisione"),
                ("10 sett.", "dall'incarico alla firma relazione"),
            ],
            "lead_partner": "Dott.ssa Ilaria Balestrieri (revisione) · Dott. Andrea Ruffini (tributario)",
            "team":         "2 soci · 1 senior · 1 praticante revisore · 10 settimane",
            "next_label":   "Caso successivo",
        },
        {
            "slug":     "contenzioso-tributario-accertamento-iva",
            "title":    "Contenzioso · accertamento IVA su operazioni intracomunitarie",
            "category": "Contenzioso tributario",
            "year":     "2024",
            "duration": "14 mesi dall'accertamento alla sentenza CTR",
            "client_code":
                "Commercio all'ingrosso · Como · 18 dipendenti · "
                "€ 6,2 M ricavi · accertamento Agenzia Entrate € 187.000 IVA",
            "lead":
                "Accertamento dell'Agenzia Entrate per operazioni intracomunitarie "
                "qualificate come cessioni interne ordinarie (presunzione di "
                "destinazione nazionale). Il cliente ha incaricato Fiscus in "
                "sede di contraddittorio pre-accertamento, a ridosso del "
                "termine per l'adesione.",
            "sections": [
                {
                    "label": "Il problema",
                    "heading": "Presunzione di fattura nazionale su operazioni UE",
                    "body":
                        "L'Agenzia Entrate ha notificato un avviso di "
                        "accertamento per l'anno 2021 con recupero di IVA per "
                        "€ 187.000, sanzioni 90% e interessi. L'ufficio "
                        "qualificava una serie di operazioni verso un cliente "
                        "slovacco come cessioni interne ordinarie, sulla base "
                        "dell'assunto che la documentazione di trasporto non "
                        "provasse in modo sufficiente l'uscita effettiva della "
                        "merce dal territorio italiano. Il termine per l'adesione "
                        "scadeva in 28 giorni.",
                },
                {
                    "label": "L'approccio",
                    "heading": "Contraddittorio con documentazione CMR integrativa",
                    "body":
                        "Fiscus ha istruito un contraddittorio pre-accertamento "
                        "in tre settimane. Raccolti: 64 lettere di vettura CMR "
                        "originali timbrate dal destinatario UE, estratti conto "
                        "bancari dei pagamenti del cliente slovacco dalla sua "
                        "banca slovacca, VIES verification storici del cliente "
                        "UE, una perizia giurata del responsabile logistico "
                        "del cliente. La documentazione è stata depositata in "
                        "contraddittorio e, in parallelo, in sede di ricorso "
                        "alla Commissione Tributaria Provinciale di Como, per "
                        "anticipare l'ipotesi di diniego amministrativo.",
                },
                {
                    "label": "Il risultato",
                    "heading": "Ricorso accolto in CTP e confermato in CTR",
                    "body":
                        "La CTP di Como ha accolto integralmente il ricorso a "
                        "giugno 2024, annullando l'avviso di accertamento con "
                        "sentenza n. 412/2024. L'Agenzia Entrate ha proposto "
                        "appello alla CTR della Lombardia, che a dicembre 2024 "
                        "ha confermato la sentenza di primo grado rigettando "
                        "l'appello dell'ufficio. Sentenza passata in giudicato "
                        "a gennaio 2025. Il cliente ha recuperato le spese legali "
                        "ex art. 15 D.Lgs. 546/1992 per € 14.200.",
                },
            ],
            "kpi": [
                ("€ 187.000", "IVA accertata — totalmente annullata"),
                ("100%",      "spese legali recuperate ex art. 15"),
                ("2/2",       "gradi di giudizio favorevoli"),
                ("14 mesi",   "dall'accertamento al passaggio in giudicato"),
            ],
            "lead_partner": "Dott.ssa Ilaria Balestrieri",
            "team":         "1 socio cassazionista · 1 senior · 14 mesi",
            "next_label":   "Caso successivo",
        },
        {
            "slug":     "wealth-passaggio-generazionale-holding",
            "title":    "Wealth · holding di famiglia per passaggio generazionale",
            "category": "Wealth & passaggio generazionale",
            "year":     "2025",
            "duration": "20 mesi dal mandato al completamento",
            "client_code":
                "Famiglia imprenditoriale · Varese · patrimonio aggregato "
                "€ 38 M (partecipazione PMI manifatturiera + immobili + liquidità) · "
                "due figli, entrambi coinvolti in azienda",
            "lead":
                "Famiglia imprenditoriale con partecipazione di controllo in "
                "una PMI manifatturiera di secondo livello, tre immobili "
                "strumentali, due immobili di pregio e liquidità significativa. "
                "Fondatore 68 anni, due figli operativi in azienda, moglie "
                "non coinvolta nella gestione. Obiettivo: preparare il passaggio "
                "generazionale su orizzonte 7-10 anni.",
            "sections": [
                {
                    "label": "Il problema",
                    "heading": "Patrimonio eterogeneo, due figli con ruoli diversi",
                    "body":
                        "Il fondatore aveva tre preoccupazioni concrete. "
                        "Primo: preservare l'unitarietà del controllo societario "
                        "anche dopo la successione — entrambi i figli lavoravano "
                        "in azienda, ma con ruoli e prospettive diversi. "
                        "Secondo: consentire una liquidità di \"ritiro\" "
                        "alla moglie e al ramo famigliare non operativo senza "
                        "costringere a vendere partecipazioni. Terzo: minimizzare "
                        "l'impatto fiscale della successione (imposta di successione "
                        "oltre soglia di 1 M€ per parente in linea retta) "
                        "pur nel rispetto assoluto della normativa vigente — "
                        "nessuna struttura offshore, nessun trust aggressivo.",
                },
                {
                    "label": "L'approccio",
                    "heading": "Holding di famiglia + patto parasociale + PIR",
                    "body":
                        "Fiscus ha coordinato un percorso a 20 mesi in quattro "
                        "fasi. Fase 1 (mesi 1-4): costituzione di una holding "
                        "di famiglia S.r.l. con conferimento delle partecipazioni "
                        "operative in neutralità fiscale ex art. 177 TUIR. "
                        "Fase 2 (mesi 5-8): redazione del patto parasociale "
                        "tra i due rami famigliari con meccanismo di tag-along/"
                        "drag-along per prevenire spaccature future. "
                        "Fase 3 (mesi 9-14): donazione graduale delle quote "
                        "della holding ai figli, con usufrutto vitalizio a "
                        "favore del fondatore e della moglie — beneficia "
                        "dell'agevolazione art. 3, comma 4-ter D.Lgs. 346/1990 "
                        "(esenzione imposta successione per partecipazioni di "
                        "controllo). Fase 4 (mesi 15-20): sottoscrizione di "
                        "strumenti PIR compatibili per il ramo non operativo "
                        "della famiglia, sui flussi di dividendo.",
                },
                {
                    "label": "Il risultato",
                    "heading": "Successione fiscalmente ottimizzata + governance familiare",
                    "body":
                        "La struttura è stata completata a settembre 2025. "
                        "Imposta di successione azzerata sulle partecipazioni "
                        "operative grazie all'agevolazione art. 3, comma 4-ter "
                        "(patto di famiglia + holding di controllo). Patto "
                        "parasociale sottoscritto dai due fratelli + genitori, "
                        "con clausole di buy-out al valore di perizia "
                        "indipendente aggiornata annualmente. Il ramo non "
                        "operativo (moglie + eventuali nipoti) percepisce "
                        "dividendi regolari sulla holding e ha sottoscritto "
                        "PIR individuali per € 180.000 ciascuno sull'orizzonte "
                        "2025-2030. Il fondatore ha mantenuto diritti di voto "
                        "in usufrutto fino a 75 anni + 5 di opzione aggiuntiva.",
                },
            ],
            "kpi": [
                ("€ 0",      "imposta di successione sulle partecipazioni operative"),
                ("100%",     "unitarietà del controllo preservata"),
                ("20 mesi",  "dal mandato al completamento"),
                ("4/4",      "fasi completate nei tempi concordati"),
            ],
            "lead_partner": "Dott. Stefano Conti",
            "team":         "1 socio · 1 senior · notaio esterno · 20 mesi",
            "next_label":   "Caso successivo",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Primo appuntamento",
        "headline": "Quarantacinque minuti, agenda <em>aperta</em>, nessun impegno.",
        "intro":
            "Il primo contatto avviene con un socio iscritto ODCEC. "
            "Discutiamo l'area di competenza, l'orizzonte temporale del rapporto "
            "e la parcella indicativa — prima di qualsiasi delega firmata. "
            "I clienti esistenti prenotano nello spazio riservato in area cliente.",

        # Form fields — commercialista onboarding shape
        "form_label":   "Richiedi appuntamento",
        "form_heading": "Compila la scheda conoscitiva",
        "form_intro":
            "Riceverà conferma entro 48 ore lavorative dall'invio. "
            "I dati sono trattati ai sensi del Reg. UE 679/2016 e custoditi "
            "nell'archivio cifrato dello studio con retention decennale.",
        "form_fields": [
            {"name": "name",      "label": "Nome",           "type": "text",     "required": True,  "placeholder": "Es. Andrea",
             "helper": "Solo il nome di battesimo."},
            {"name": "surname",   "label": "Cognome",        "type": "text",     "required": True,  "placeholder": "Es. Ruffini",
             "helper": "Come compare sui documenti identificativi."},
            {"name": "company",   "label": "Ragione sociale o ditta individuale", "type": "text", "required": False,
             "placeholder": "Es. Officine Meccaniche Bresciane S.r.l.",
             "helper": "Opzionale — compilare se il contatto è a nome di un'impresa."},
            {"name": "vat",       "label": "Partita IVA",    "type": "text",     "required": False, "placeholder": "IT 12345678901",
             "helper": "Opzionale — utile se il rapporto riguarda fiscalità d'impresa."},
            {"name": "fiscal_code","label": "Codice Fiscale","type": "text",     "required": True,  "placeholder": "RFFNDR72M15F205Z",
             "helper": "Obbligatorio — necessario per l'abilitazione delega Entratel in caso di prosecuzione."},
            {"name": "email",     "label": "Email",          "type": "email",    "required": True,  "placeholder": "andrea.ruffini@esempio.it",
             "helper": "A questo indirizzo inviamo la conferma di appuntamento."},
            {"name": "phone",     "label": "Telefono",       "type": "tel",      "required": True,  "placeholder": "+39 ...",
             "helper": "Per eventuali richieste di chiarimento pre-appuntamento."},
            {"name": "area",      "label": "Area di competenza di interesse", "type": "select", "required": True,
             "options": [
                 "Da definire in appuntamento",
                 "Dichiarazione dei redditi e fiscalità ordinaria",
                 "Bilancio d'esercizio e contabilità ordinaria",
                 "Contenzioso tributario",
                 "Pianificazione fiscale e wealth",
                 "Consulenza del lavoro",
                 "Revisione legale",
             ],
             "helper": "Scegliere \"Da definire\" se la situazione è complessa."},
            {"name": "time_slot", "label": "Fascia oraria preferita", "type": "select", "required": True,
             "options": [
                 "Mattina 9:00 – 12:00",
                 "Primo pomeriggio 14:00 – 16:30",
                 "Secondo pomeriggio 16:30 – 18:30",
                 "Indifferente",
             ],
             "helper": "In prossimità scadenze diamo priorità alle fasce mattutine."},
            {"name": "situation", "label": "Breve descrizione della situazione", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Massimo 600 caratteri. Esempio: \"Partita IVA in regime forfettario dal 2021, primo anno di uscita dal forfettario, devo capire come procedere con la contabilità ordinaria.\"",
             "helper": "Quanto basta a valutare se la situazione rientra nelle nostre aree di competenza e a preparare la prima conversazione."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contatto",
             "meta": "La persona che incontreremo in primo appuntamento.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Identificativi fiscali",
             "meta": "Obbligatorio il Codice Fiscale; Partita IVA e ragione sociale solo se il rapporto riguarda un'attività d'impresa.",
             "fields": ["fiscal_code", "vat", "company"]},
            {"num": "03", "title": "Perimetro dell'incontro",
             "meta": "Per calendare il socio di riferimento sulla fascia richiesta. Nessun dettaglio sensibile qui — i documenti si portano in appuntamento.",
             "fields": ["area", "time_slot", "situation"]},
            {"num": "04", "title": "Documentazione (facoltativa)",
             "meta": "Ultima dichiarazione dei redditi, ultimo bilancio, eventuali avvisi dell'Agenzia Entrate: possono anticipare l'appuntamento.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "allegati_preliminari",
            "label":    "Documenti preliminari",
            "helper":   "Ultima dichiarazione dei redditi (Modello Redditi o 730), ultimo bilancio depositato, avvisi Agenzia Entrate ricevuti. "
                        "PDF · max 10 MB complessivi. Archivio cifrato con accesso limitato ai soci.",
            "accept":   ".pdf",
            "multiple": True,
            "primary":  "Trascina qui i documenti o",
            "link":     "sfoglia dall'archivio",
            "meta":     "PDF · max 10 MB · archivio cifrato AES-256",
        },

        "form_submit_label": "Richiedi appuntamento",
        "form_submit_note":
            "Conferma da un socio iscritto ODCEC entro 48 ore lavorative. "
            "Nessuna segreteria esterna, nessuna automazione — leggiamo "
            "personalmente ogni richiesta.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi del "
            "Reg. UE 679/2016. I dati sono custoditi nell'archivio cifrato "
            "dello studio con retention decennale, accesso limitato ai soci "
            "e ai collaboratori iscritti albo. Nessun dato viene comunicato "
            "a terzi senza esplicita autorizzazione scritta.",

        # Office meta-row labels (lifted from skin for i18n)
        "office_address_label": "Indirizzo",
        "office_area_label":    "Zona",
        "office_phone_label":   "Telefono",
        "office_email_label":   "Email",

        # Sidebar — sede + canali diretti
        "offices_label":   "Sede",
        "offices": [
            {
                "city":    "Milano",
                "tag":     "Sede unica",
                "address": "Via Melzo 14 · 20129",
                "area":    "Porta Venezia · a 200 metri da MM Porta Venezia",
                "phone":   "+39 02 4951 3388",
                "email":   "segreteria@fiscusstudio.it",
            },
        ],

        "channels_label": "Canali diretti",
        "channels": [
            ("Segreteria studio",      "+39 02 4951 3388",           "Lun – Ven · 9:00 – 18:30"),
            ("Email istituzionale",    "segreteria@fiscusstudio.it", "Risposta entro 48 ore lavorative"),
            ("Area cliente riservata", "area.fiscusstudio.it",       "Per clienti esistenti — scadenze + documenti"),
        ],

        "footnote":
            "Fiscus non risponde a richieste anonime e non rilascia pareri "
            "fiscali preliminari via email. Le informazioni amministrative "
            "(parcella indicativa, modalità di fatturazione, calendario delle "
            "scadenze del perimetro proposto) sono illustrate nel primo "
            "appuntamento — a titolo gratuito e senza impegno di delega.",
    },
}
