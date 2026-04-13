"""Pragma — Corporate Suite (business / corporate-suite archetype) content.

Phase 2g3.3 — Business live rollout (Session 32, 2026-04-13).

Editorial identity: institutional Italian corporate advisory firm based in
Milan, with offices in Frankfurt and Zurich. Boardroom-grade B2B
positioning — strategy, M&A, governance and ESG — for established mid-cap
companies. The voice is sober, formal, Anglo-Italian (Lei register, partner
& cda vocabulary). Photo direction is boardroom + corporate HQ + executive
portrait, never startup loft.

Differentiation vs Elevate (10-gate D-054 — recorded here for reviewers):
 1. Hero image:        boardroom long-table photo (business-corporate[0])
                       vs Elevate's typographic-only manifesto (no big photo)
 2. First-2 imagery:   boardroom + corporate atrium (business-corporate[0,1])
                       vs Elevate product UI (business-startup[1,2])
 3. Silhouette:        55/45 split serif L + photo R + KPI-strip
                       vs Elevate centered manifesto + product mockup card
 4. Section order:     hero → pillars → kpi → sectors → leadership → cases → cta
                       vs Elevate banner → manifesto → mockup → metrics → pricing → shiplog
 5. Primary CTA:       "Fissa una call privata" + private form + boardroom
                       vs Elevate "Inizia gratis" + glow-pill + 14-day trial
 6. Block rhythm:      airy editorial chapters (very-airy paddings)
                       vs Elevate medium-density glow cards
 7. Macro tone:        cream paper + navy + gold accent (institutional)
                       vs Elevate dark cosmic gradient + cyan glow (growth-tech)
 8. Imagery direction: boardroom executives + corporate facilities
                       vs Elevate product dashboards + tech offices
 9. Typography:        Merriweather (transitional serif) + Inter
                       vs Elevate Manrope (geometric sans) + Inter
10. Inner pages:       case studies + advisory pillars + 5-office presence
                       vs Elevate pricing + ship log + integrations + demo

Page kinds:
- home, about, services, case_study_list, case_study_detail, contact
"""
from __future__ import annotations

from typing import Any


PRAGMA_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Studio",        "kind": "home"},
        {"slug": "chi-siamo",     "label": "Chi siamo",     "kind": "about"},
        {"slug": "competenze",    "label": "Competenze",    "kind": "services"},
        {"slug": "case-studies",  "label": "Case studies",  "kind": "case_study_list"},
        {"slug": "contatti",      "label": "Contatti",      "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial": "P",
        "logo_word":    "Pragma Advisors",
        "tag":          "Advisory corporate · Milano",
        "phone":        "+39 02 3611 9900",
        "email":        "segreteria@pragmaadvisors.it",
        "address":      "Via Filodrammatici 10 · 20121 Milano",
        "hours_compact":"Lun – Ven · 9:00 – 19:00 · su appuntamento",
        "hours_footer_rows": [
            "Sabato · solo board call programmate",
            "Domenica · chiuso",
        ],
        "license":      "Iscrizione Albo Consulenti CONSOB n. 1148/2009",
        "footer_intro":
            "Boutique advisory indipendente per direzioni generali e CdA "
            "di PMI consolidate. Strategia, M&A, governance ed ESG. "
            "Sede a Milano, presenze stabili a Francoforte e Zurigo.",
        # Footer column headings — per-template (not shared chrome) because
        # each business template has a different sense of what "the studio" is
        "foot_studio":   "Lo studio",
        "foot_pages":    "Sezioni",
        "foot_contact":  "Contatti",
        "foot_offices":  "Sedi",
        "offices_footer_rows": [
            "Milano · Porta Nuova",
            "Frankfurt am Main · Bockenheim",
            "Zürich · Paradeplatz",
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Advisory corporate · Milano · Francoforte · Zurigo",
        "headline":    "Dove si prendono le decisioni <em>che contano</em>.",
        "intro":
            "Affianchiamo direzioni generali e consigli di amministrazione "
            "di PMI consolidate nelle scelte strutturali — piani industriali, "
            "operazioni di M&A, governance e percorsi ESG. Una boutique "
            "indipendente, vent'anni di mandati riservati.",
        "primary_cta":   "Fissa una call privata",
        "primary_href":  "contatti",
        "secondary_cta": "Scarica la presentazione",
        "secondary_href":"chi-siamo",

        # Right-hand boardroom photo + credit overlay
        "hero_image":              "https://images.unsplash.com/photo-1542626991-cbc4e32524cc?w=1600&q=80&auto=format&fit=crop",
        "hero_image_credit_left":  ("Fotografia",   "CdA Industriale Lombarda · 2025"),
        "hero_image_credit_right": ("Anno fondazione", "2004"),
        "hero_meta_strip": [
            ("Headquarters",   "Milano · Porta Nuova"),
            ("Equipe senior",  "14 partner"),
            ("Mandati attivi", "42 progetti"),
        ],

        # Advisory pillars — three-practice grid
        "pillars_label":   "Practice",
        "pillars_heading": "Tre competenze, una sola firma",
        "pillars_intro":
            "Un solo team multidisciplinare lavora a ogni mandato. "
            "I partner non vendono — siedono al tavolo dall'inizio alla firma.",
        "pillars": [
            ("01", "Board advisory",
             "Affianchiamo CdA e direzioni generali nelle decisioni di cambio di passo — "
             "piani industriali triennali, assetti proprietari, successioni d'impresa, "
             "gestione delle crisi reputazionali."),
            ("02", "Crescita & M&A",
             "Due diligence, valutazione, negoziazione e integrazione post-deal "
             "in 10 – 12 settimane, con team dedicati per settore. Operiamo sia "
             "lato vendor sia lato acquirer, mai entrambi nello stesso dossier."),
            ("03", "Governance & ESG",
             "Compliance CSRD, reporting integrato, modelli 231, struttura "
             "dei comitati endoconsiliari e policy di sostenibilità per gruppi "
             "industriali e financial-services."),
        ],

        # KPI strip on dark navy band
        "kpi_heading": "Venti anni di mandati riservati",
        "kpi_strip": [
            ("22",      "anni di attività"),
            ("180+",    "mandati chiusi"),
            ("€ 1.4 B", "valore transato"),
            ("94%",     "ripetizione incarico"),
        ],

        # Sectors ribbon
        "sectors_label": "Settori di intervento",
        "sectors": [
            "Industria & manifattura",
            "Servizi finanziari",
            "Energia & utilities",
            "Retail & consumer",
            "Healthcare & pharma",
        ],

        # Trust band — institutional client logos as text wordmarks
        "trust_label":   "Hanno scelto Pragma negli ultimi cinque anni",
        "trust_logos":   [
            "GRUPPO INDUSTRIALE BRESCIANO",
            "FONDO MEZZANINO ITALIA",
            "BIOTECH TORINO",
            "CASSA AGRICOLA EMILIA",
            "ENERGIA RINNOVABILE NORD",
            "RETAIL FAMILIARE TOSCANO",
        ],

        # Leadership preview — three managing partners on home
        "leadership_label":   "Direzione",
        "leadership_heading": "I partner che siederanno al vostro tavolo",
        "leadership_intro":
            "Ogni mandato è seguito personalmente da almeno un managing "
            "partner. Nessun executive di ricambio, nessun junior parcheggiato.",
        "leadership": [
            {
                "name":  "Dott. Federico Seregni",
                "role":  "Managing partner · Board advisory",
                "bio":
                    "Vent'anni in McKinsey & Company come senior partner industrial. "
                    "Membro indipendente di tre CdA quotati. Specializzato in piani "
                    "industriali e successioni familiari del manifatturiero italiano.",
                "credentials": [
                    "Bocconi (CLEACC '95)",
                    "Insead MBA '01",
                    "Consigliere Confindustria Lombardia",
                ],
            },
            {
                "name":  "Avv. Caterina Foschini",
                "role":  "Managing partner · Crescita & M&A",
                "bio":
                    "Oltre 70 operazioni di M&A chiuse fra Italia e DACH. "
                    "Già di Bonelli Erede, ha guidato due exit strategiche "
                    "del private-equity italiano nel comparto consumer.",
                "credentials": [
                    "Cattolica (Giurisprudenza '98)",
                    "LL.M. Frankfurt am Main",
                    "AIDC, IBA M&A Forum",
                ],
            },
            {
                "name":  "Ing. Marco Lavezzi",
                "role":  "Managing partner · Governance & ESG",
                "bio":
                    "Già responsabile sostenibilità di un gruppo utility quotato. "
                    "Coordina i progetti CSRD, reporting integrato e modelli 231 "
                    "per i clienti della pratica governance.",
                "credentials": [
                    "Politecnico Milano (Ing. Gestionale '02)",
                    "Certificato GRI · CDP",
                    "Membro CASUR-ANRI",
                ],
            },
        ],

        # Case studies preview — three on home, full list on /case-studies
        "cases_label":   "Recent work",
        "cases_heading": "Tre mandati, tre direzioni",
        "cases_intro":
            "Una selezione recente di progetti chiusi. Per riservatezza, "
            "i nomi dei clienti sono divulgati solo dietro NDA.",

        # Final CTA band before footer
        "cta_label":     "Una conversazione preliminare",
        "cta_heading":   "Trenta minuti, agenda ristretta, niente impegno",
        "cta_intro":
            "La prima call avviene con un partner senior. Discutiamo il "
            "perimetro, la timeline e l'eventuale conflitto di interesse — "
            "prima di qualsiasi proposta economica.",
        "cta_primary":   "Richiedi la call",
        "cta_primary_href": "contatti",
        "cta_secondary": "Scarica il dossier istituzionale",
        "cta_secondary_href": "chi-siamo",
    },

    # ─── CHI SIAMO (about + values) ─────────────────────────────
    "chi-siamo": {
        "eyebrow":   "Lo studio · 2004 — 2026",
        "headline":  "Una boutique <em>indipendente</em>, ventidue anni di mandati riservati.",
        "intro":
            "Pragma Advisors nasce a Milano nel 2004 dall'incontro fra "
            "professionisti di estrazione consulenziale, finanziaria e legale. "
            "Da allora siamo cresciuti per cooptazione — mai per acquisizione "
            "— e abbiamo mantenuto l'indipendenza dal capitale di terzi.",

        # Studio history — 5-step timeline
        "history_label":   "Storia dello studio",
        "history_heading": "Cinque tappe, ventidue anni",
        "history": [
            ("2004", "Fondazione",
             "Federico Seregni e tre soci aprono Pragma in via Filodrammatici, "
             "con quattro mandati di board advisory già firmati."),
            ("2009", "Iscrizione Albo Consulenti CONSOB",
             "Riconoscimento del registro dei consulenti finanziari indipendenti — "
             "la pratica M&A può presentarsi come advisor formale."),
            ("2014", "Apertura sede di Francoforte",
             "Caterina Foschini guida l'apertura della sede DACH per i mandati "
             "cross-border italo-tedeschi del manifatturiero."),
            ("2019", "Practice Governance & ESG",
             "Marco Lavezzi entra come managing partner per costituire la pratica "
             "ESG, con i primi mandati CSRD per due gruppi utility."),
            ("2024", "Apertura sede di Zurigo",
             "Per accompagnare i mandati di wealth structuring delle famiglie "
             "imprenditoriali italiane, apriamo l'ufficio di Paradeplatz."),
        ],

        # Method / values
        "values_label":   "Metodo",
        "values_heading": "Quattro principi <em>non negoziabili</em>",
        "values_intro":
            "Sono le quattro regole che separano un mandato Pragma da un "
            "incarico standard di consulenza strategica. Le trovate scritte "
            "in carta intestata sul mandato firmato, non nel sito.",
        "values": [
            ("01", "Indipendenza dal capitale",
             "Il capitale dello studio è interamente in mano ai partner attivi. "
             "Nessun conferimento di gruppi, nessun fondo di private equity in "
             "minoranza, nessun azionista esterno. La scelta dei mandati non è "
             "mai influenzata da agenda di terzi."),
            ("02", "Un partner per ogni mandato",
             "Un managing partner siede al tavolo dall'apertura del fascicolo "
             "alla firma del closing. Niente partner-of-record che spariscono "
             "dopo il pitch — il senior advisor incontrato in prima call è "
             "lo stesso che firmerà il chiusura del mandato."),
            ("03", "Niente conflitti, mai",
             "Nello stesso settore non assistiamo mai due clienti in concorrenza "
             "diretta. Su un'operazione di M&A, mai vendor + acquirer nello "
             "stesso dossier. Il nostro Compliance Officer interno verifica "
             "ogni nuovo mandato prima dell'accettazione."),
            ("04", "Onorari trasparenti",
             "Tariffa giornaliera dichiarata in proposta, success fee solo "
             "su operazioni straordinarie e sempre divulgata in fattura. "
             "Nessuna retroversione di commissioni, nessun accordo verbale "
             "con controparti finanziarie."),
        ],

        # Full team — 6 senior advisors + the 3 managing partners (also home)
        "team_label":   "Equipe senior",
        "team_heading": "Quattordici partner, tre uffici, una sola governance",
        "team_intro":
            "Le persone che lavoreranno al vostro mandato. I partner non "
            "consulenti, e non vi affidiamo a un dipartimento — siedono "
            "al tavolo dall'inizio alla fine.",
        "team": [
            {"name": "Dott. Federico Seregni",
             "role": "Managing partner · Board advisory",
             "office": "Milano",
             "bio": "Ex senior partner McKinsey, vent'anni di piani industriali. "
                    "Membro indipendente di tre CdA quotati."},
            {"name": "Avv. Caterina Foschini",
             "role": "Managing partner · M&A",
             "office": "Frankfurt",
             "bio": "70+ operazioni chiuse fra Italia e DACH. Già di Bonelli Erede, "
                    "specializzata in cross-border consumer."},
            {"name": "Ing. Marco Lavezzi",
             "role": "Managing partner · Governance & ESG",
             "office": "Milano",
             "bio": "Coordina pratica CSRD e modelli 231. Già responsabile "
                    "sostenibilità di un gruppo utility quotato."},
            {"name": "Dott.ssa Sabina Erlanger",
             "role": "Senior partner · Wealth structuring",
             "office": "Zürich",
             "bio": "Vent'anni nel private banking elvetico. Coordina "
                    "i mandati di passaggio generazionale per le famiglie italiane."},
            {"name": "Dott. Lorenzo Pellizzari",
             "role": "Senior partner · Industria & manifattura",
             "office": "Milano",
             "bio": "Ex direttore generale di un gruppo metalmeccanico bresciano. "
                    "Pratica strategica per la filiera lombarda e veneta."},
            {"name": "Dott.ssa Giulia Antinori",
             "role": "Senior partner · Servizi finanziari",
             "office": "Milano",
             "bio": "Già McKinsey financial-services. Mandati di trasformazione "
                    "per banche territoriali e SGR italiane."},
        ],

        # Coordinates strip
        "coordinates_label": "Le sedi",
        "coordinates": [
            ("Milano",     "Via Filodrammatici 10 · 20121 · Porta Nuova"),
            ("Frankfurt",  "Bockenheimer Landstr. 51 · 60325 · Westend"),
            ("Zürich",     "Paradeplatz 8 · 8001 · Innenstadt"),
        ],

        # Page-level CTA
        "cta_heading": "Una valutazione preliminare riservata",
        "cta_intro":
            "I primi trenta minuti con un partner sono una conversazione "
            "esplorativa, non una proposta commerciale. Si discute il perimetro "
            "del mandato, la timeline e l'eventuale conflitto di interesse.",
        "cta_primary":  "Richiedi la call",
        "cta_primary_href": "contatti",
    },

    # ─── COMPETENZE (services) ──────────────────────────────────
    "competenze": {
        "eyebrow":  "Practice areas · 2026",
        "headline": "Sei competenze, <em>una sola firma</em>.",
        "intro":
            "Le sei pratiche di Pragma. Ogni cliente accede a un team "
            "multidisciplinare — non si paga per ciascuna pratica separatamente, "
            "il mandato copre la combinazione di competenze necessarie.",

        # 6 services in airy cards
        "services": [
            {
                "num":   "01",
                "title": "Board advisory",
                "blurb":
                    "Affianchiamo CdA e direzioni generali nelle scelte di cambio di passo. "
                    "Piani industriali triennali, riassetti proprietari, successioni "
                    "familiari, gestione di crisi reputazionali e mandati ad interim.",
                "scope": [
                    "Piani industriali e revisione strategica",
                    "Successione familiare e governance",
                    "Mandati ad interim su CFO / COO",
                    "Comunicazione di crisi al CdA",
                ],
                "duration": "8 – 14 settimane per ciclo",
                "leader":   "Dott. Federico Seregni",
            },
            {
                "num":   "02",
                "title": "Crescita & M&A",
                "blurb":
                    "Due diligence, valutazione, negoziazione e integrazione "
                    "post-deal. Operiamo sia vendor-side sia buyer-side, mai "
                    "entrambi nello stesso dossier. Tipologia di operazioni: "
                    "carve-out, JV, exit di private equity, MBO familiari.",
                "scope": [
                    "Vendor due diligence e teaser",
                    "Buyer-side scouting e valutazione",
                    "Negoziazione e SPA assistance",
                    "Integrazione post-merger 100 giorni",
                ],
                "duration": "10 – 24 settimane secondo perimetro",
                "leader":   "Avv. Caterina Foschini",
            },
            {
                "num":   "03",
                "title": "Governance & ESG",
                "blurb":
                    "Adeguamento alla CSRD, reporting integrato, modelli "
                    "organizzativi 231, struttura dei comitati endoconsiliari. "
                    "Per gruppi industriali quotati e per family business "
                    "che si preparano alla quotazione su Euronext Growth.",
                "scope": [
                    "Compliance CSRD e reporting integrato",
                    "Modelli organizzativi 231",
                    "Comitati endoconsiliari e policy",
                    "Pre-IPO governance readiness",
                ],
                "duration": "12 – 18 settimane per ciclo",
                "leader":   "Ing. Marco Lavezzi",
            },
            {
                "num":   "04",
                "title": "Wealth structuring",
                "blurb":
                    "Pianificazione patrimoniale per famiglie imprenditoriali "
                    "italiane con perimetro internazionale. Holding di famiglia, "
                    "trust, family office, passaggio generazionale.",
                "scope": [
                    "Holding di famiglia e patti parasociali",
                    "Trust e fondazioni di famiglia",
                    "Family office e advisory committee",
                    "Passaggio generazionale e successione",
                ],
                "duration": "16 – 36 settimane per riassetto",
                "leader":   "Dott.ssa Sabina Erlanger",
            },
            {
                "num":   "05",
                "title": "Industria & manifattura",
                "blurb":
                    "Pratica verticale per la filiera industriale lombarda e "
                    "veneta. Diagnostica operativa, supply-chain redesign, "
                    "make-or-buy strategici, internazionalizzazione produttiva.",
                "scope": [
                    "Diagnostica operativa multi-stabilimento",
                    "Supply chain redesign",
                    "Make-or-buy strategico",
                    "Apertura impianti esteri",
                ],
                "duration": "10 – 20 settimane per progetto",
                "leader":   "Dott. Lorenzo Pellizzari",
            },
            {
                "num":   "06",
                "title": "Servizi finanziari",
                "blurb":
                    "Trasformazione strategica per banche territoriali, SGR "
                    "italiane e fintech regolate. Riposizionamento strategico, "
                    "M&A bancario, reporting prudenziale Banca d'Italia.",
                "scope": [
                    "Riposizionamento strategico bancario",
                    "M&A bancario e SGR",
                    "Compliance Banca d'Italia / EBA",
                    "Modelli operativi front-to-back",
                ],
                "duration": "12 – 24 settimane secondo perimetro",
                "leader":   "Dott.ssa Giulia Antinori",
            },
        ],

        # Process strip — how a mandate is run
        "process_label":   "Come lavoriamo",
        "process_heading": "Quattro fasi, una sola sequenza",
        "process": [
            ("01", "Call esplorativa",
             "Trenta minuti riservati con un managing partner. "
             "Si discute il perimetro, niente proposta economica."),
            ("02", "Proposta scritta",
             "Entro cinque giorni, una proposta di mandato di tre pagine "
             "con perimetro, deliverable, timeline e tariffario trasparente."),
            ("03", "Esecuzione",
             "Team dedicato dall'apertura alla chiusura. Il managing partner "
             "siede a ogni meeting di steering, mai un junior."),
            ("04", "Closing & follow-up",
             "Closing memo riservato al CdA + follow-up trimestrale "
             "non a pagamento per i 12 mesi successivi."),
        ],

        # Final CTA
        "cta_heading":   "Quale practice fa al caso vostro?",
        "cta_intro":
            "Se il perimetro non è chiaro, inviateci una breve descrizione "
            "del problema. Vi indirizziamo al partner giusto entro 48 ore — "
            "anche se non lavoriamo con voi.",
        "cta_primary":   "Scrivici",
        "cta_primary_href": "contatti",
    },

    # ─── CASE-STUDIES (list) ────────────────────────────────────
    "case-studies": {
        "eyebrow":  "Mandati selezionati · 2022 — 2026",
        "headline": "Tre mandati, <em>tre direzioni</em>.",
        "intro":
            "Una selezione di mandati conclusi negli ultimi quattro anni. "
            "I clienti sono identificati tramite codice settore (in osservanza "
            "degli NDA) ma le metriche di output sono reali e verificabili "
            "in fase di reference call.",

        # Card-list of case studies (full posts in `posts` below)
        "cases_label": "Casi",
        "cases_intro":
            "Selezione bilanciata sui tre filoni principali — board advisory, "
            "M&A, governance. La lista completa è disponibile in formato PDF "
            "su richiesta tramite la pagina contatti.",

        "cta_heading":   "Un caso simile al vostro?",
        "cta_intro":
            "I dossier completi (perimetro, KPI, reference call con il CFO "
            "del cliente) sono accessibili dietro firma di NDA reciproca. "
            "La firma avviene in prima call, prima di qualsiasi proposta.",
        "cta_primary":   "Richiedi i dossier integrali",
        "cta_primary_href": "contatti",
    },

    # Posts powering case_study_detail. URL: /case-studies/<slug>/
    "posts": [
        {
            "slug":     "manifatturiero-bresciano-piano-industriale",
            "title":    "Gruppo manifatturiero bresciano · piano industriale 2025-28",
            "category": "Board advisory",
            "year":     "2025",
            "duration": "14 settimane",
            "client_code": "Industria & manifattura · Brescia · 320 dipendenti · €78M ricavi",
            "lead":
                "Tre stabilimenti, due famiglie azioniste in disaccordo sul "
                "perimetro futuro. Pragma ha riallineato il piano industriale "
                "triennale prima del rinnovo del mandato del CdA.",
            "sections": [
                {
                    "label": "Il problema",
                    "heading": "Due famiglie, tre piani contraddittori",
                    "body":
                        "Il gruppo nasce nel 1968 dall'unione di due aziende "
                        "familiari. Nel 2024 il CdA si presentava con tre "
                        "piani industriali alternativi sul tavolo: chiusura "
                        "dello stabilimento più datato, apertura di un quarto "
                        "sito in Romania, oppure carve-out della divisione "
                        "componentistica per cessione a un fondo di private "
                        "equity. Le due famiglie azioniste sostenevano "
                        "scenari incompatibili e il mandato del CdA scadeva "
                        "in dodici mesi.",
                },
                {
                    "label": "L'approccio",
                    "heading": "Diagnostica operativa + governance check",
                    "body":
                        "Pragma ha lavorato in tre direzioni in parallelo. "
                        "Pratica industria & manifattura ha condotto una "
                        "diagnostica operativa di nove settimane sui tre "
                        "stabilimenti, con misurazione OEE, costing per "
                        "linea e benchmark di filiera. In parallelo la "
                        "pratica board advisory ha mediato fra le due "
                        "famiglie tramite tre cicli di workshop di "
                        "allineamento. La pratica governance ha rivisto "
                        "il patto parasociale e proposto un nuovo "
                        "regolamento del CdA con quorum rafforzati.",
                },
                {
                    "label": "Il risultato",
                    "heading": "Piano triennale approvato all'unanimità",
                    "body":
                        "Piano industriale 2025–28 approvato all'unanimità "
                        "dal CdA e dall'assemblea straordinaria. Lo "
                        "stabilimento più datato è stato riconvertito "
                        "(non chiuso) a produzione di componenti per "
                        "l'eolico — €4M di capex finanziati con fondo "
                        "Simest. Il carve-out della divisione "
                        "componentistica è stato accantonato. Il nuovo "
                        "patto parasociale ha ridotto i quorum di blocco "
                        "del 40%.",
                },
            ],
            "kpi": [
                ("€ 4 M",  "capex riconversione finanziato"),
                ("0",      "stabilimenti chiusi (3 mantenuti)"),
                ("100%",   "approvazione del piano in CdA"),
                ("12 mesi","prima del rinnovo del mandato"),
            ],
            "lead_partner": "Dott. Federico Seregni · Dott. Lorenzo Pellizzari",
            "team":         "3 partner · 4 senior · 2 junior · 14 settimane",
            "next_label":   "Mandato successivo",
        },
        {
            "slug":     "carve-out-consumer-italia-dach",
            "title":    "Carve-out divisione consumer · operazione cross-border Italia-DACH",
            "category": "Crescita & M&A",
            "year":     "2024",
            "duration": "22 settimane",
            "client_code": "Retail & consumer · Vicenza · 540 dipendenti · €112M ricavi",
            "lead":
                "Carve-out della divisione private-label di un gruppo retail "
                "vicentino, ceduta a un operatore strategico tedesco. "
                "Pragma ha agito sell-side, dalla teaser all'integrazione.",
            "sections": [
                {
                    "label": "Il problema",
                    "heading": "Una divisione strategica, un azionariato diviso",
                    "body":
                        "La divisione private-label rappresentava il 28% "
                        "dei ricavi ma il 51% dell'EBITDA del gruppo, ed "
                        "era cresciuta su clienti DACH (DM, Lidl Germania) "
                        "che non si sentivano serviti adeguatamente da una "
                        "struttura italiana. Una parte dell'azionariato "
                        "premeva per il carve-out con cessione a operatore "
                        "strategico tedesco; un'altra preferiva preservare "
                        "il perimetro e cercare un partner industriale italiano.",
                },
                {
                    "label": "L'approccio",
                    "heading": "Vendor due diligence + scouting parallelo",
                    "body":
                        "Pragma ha condotto una vendor due diligence "
                        "completa (operativa, finanziaria, legale, fiscale) "
                        "in dieci settimane. In parallelo, lo scouting "
                        "ha contattato sei potenziali acquirenti — tre "
                        "operatori strategici DACH, due fondi di private "
                        "equity europei specializzati su consumer, e un "
                        "operatore italiano. La cessione è stata gestita "
                        "tramite asta privata su quattro settimane con "
                        "process letter strutturata.",
                },
                {
                    "label": "Il risultato",
                    "heading": "Cessione al multiplo target, nessuna disruption",
                    "body":
                        "Cessione conclusa al multiplo EBITDA target "
                        "(8.4x), con clausola di earn-out su 24 mesi. "
                        "L'integrazione post-merger ha mantenuto l'80% "
                        "dell'organico della divisione (operatori produttivi "
                        "+ commerciali). Il 100% dei contratti con i tre "
                        "principali clienti DACH è stato rinnovato entro "
                        "i sei mesi successivi al closing.",
                },
            ],
            "kpi": [
                ("8.4 x",  "multiplo EBITDA al closing"),
                ("80%",    "organico ceduto preservato"),
                ("100%",   "contratti DACH rinnovati post-closing"),
                ("22 sett", "dall'incarico al signing"),
            ],
            "lead_partner": "Avv. Caterina Foschini · Dott.ssa Giulia Antinori",
            "team":         "2 partner · 5 senior · 3 junior · 22 settimane",
            "next_label":   "Mandato successivo",
        },
        {
            "slug":     "csrd-utility-quotata-roadmap",
            "title":    "Roadmap CSRD per gruppo utility quotato",
            "category": "Governance & ESG",
            "year":     "2025",
            "duration": "18 settimane",
            "client_code": "Energia & utilities · Bologna · 1.800 dipendenti · €420M ricavi",
            "lead":
                "Adeguamento al primo reporting CSRD per un gruppo utility "
                "quotato su Euronext Milan. Materialità doppia, baseline "
                "scope 1-2-3, governance di sostenibilità riconfigurata.",
            "sections": [
                {
                    "label": "Il problema",
                    "heading": "Reporting frammentato, baseline incompleta",
                    "body":
                        "Il gruppo aveva storicamente prodotto un bilancio "
                        "di sostenibilità GRI volontario, ma la baseline "
                        "scope 3 era incompleta, la materialità non era "
                        "doppia (impatto + finanziaria) e i KPI non erano "
                        "audit-ready. Il primo esercizio CSRD obbligatorio "
                        "ricadeva sull'esercizio 2025, da pubblicare ad "
                        "aprile 2026 — diciotto mesi disponibili.",
                },
                {
                    "label": "L'approccio",
                    "heading": "Materialità doppia + baseline + governance",
                    "body":
                        "Pragma ha lavorato in tre flussi paralleli per "
                        "diciotto settimane. Flusso A — analisi di "
                        "materialità doppia con 38 stakeholder consultati "
                        "(fornitori, clienti, sindacati, NGO ambientali, "
                        "investitori istituzionali). Flusso B — completamento "
                        "baseline scope 1-2-3 con metodologia GHG Protocol "
                        "e validazione esterna. Flusso C — riconfigurazione "
                        "governance: comitato sostenibilità endoconsiliare, "
                        "policy ESG aggiornata, KPI integrati nel piano "
                        "industriale.",
                },
                {
                    "label": "Il risultato",
                    "heading": "Primo reporting CSRD audit-ready in tempo",
                    "body":
                        "Primo reporting CSRD pubblicato con relazione di "
                        "assurance limitata da revisore esterno (zero "
                        "qualifiche). 142 datapoints ESRS coperti integralmente. "
                        "Comitato sostenibilità endoconsiliare attivo dal "
                        "primo trimestre 2026 con membro indipendente "
                        "Pragma in qualità di osservatore tecnico per il "
                        "primo anno. Punteggio MSCI ESG migliorato di "
                        "due rating notch.",
                },
            ],
            "kpi": [
                ("142", "datapoints ESRS coperti"),
                ("0",   "qualifiche da revisore"),
                ("38",  "stakeholder consultati"),
                ("+ 2", "notch rating MSCI ESG"),
            ],
            "lead_partner": "Ing. Marco Lavezzi",
            "team":         "1 partner · 4 senior · 2 junior · 18 settimane",
            "next_label":   "Mandato successivo",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Conversazione preliminare",
        "headline": "Trenta minuti, agenda <em>ristretta</em>, niente impegno.",
        "intro":
            "Il primo contatto avviene con un managing partner. "
            "Discutiamo il perimetro del mandato, la timeline e l'eventuale "
            "conflitto di interesse — prima di qualsiasi proposta economica.",

        # Form fields — generic loop in chrome
        "form_label":   "Richiedi la call",
        "form_heading": "Compila il modulo riservato",
        "form_intro":
            "Riceverà conferma entro 48 ore lavorative dall'invio. "
            "Le informazioni sensibili sono trattate ai sensi del Reg. UE 679/2016 "
            "e custodite in archivio cifrato a accesso limitato ai partner.",
        "form_fields": [
            {"name": "name",      "label": "Nome",           "type": "text",     "required": True,  "placeholder": "Es. Federico",
             "helper": "Solo il nome di battesimo, grazie."},
            {"name": "surname",   "label": "Cognome",        "type": "text",     "required": True,  "placeholder": "Es. Seregni",
             "helper": "Come compare nell'organigramma."},
            {"name": "company",   "label": "Società",        "type": "text",     "required": True,  "placeholder": "Es. Gruppo Industriale Lombardo",
             "helper": "Denominazione registrata, non nome commerciale."},
            {"name": "role",      "label": "Ruolo",          "type": "text",     "required": True,  "placeholder": "Es. CFO · CEO · Membro CdA",
             "helper": "Posizione in CdA o direzione di riferimento."},
            {"name": "email",     "label": "Email aziendale","type": "email",    "required": True,  "placeholder": "federico.seregni@gruppo.it",
             "helper": "Non accettiamo domini consumer (Gmail/Outlook/Libero) per questo primo contatto."},
            {"name": "phone",     "label": "Telefono",       "type": "tel",      "required": True,  "placeholder": "+39 ...",
             "helper": "Linea diretta del referente, non centralino."},
            {"name": "practice",  "label": "Practice di interesse", "type": "select", "required": True,
             "options": [
                 "Da definire in call",
                 "Board advisory",
                 "Crescita & M&A",
                 "Governance & ESG",
                 "Wealth structuring",
                 "Industria & manifattura",
                 "Servizi finanziari",
             ],
             "helper": "Scegliere \"Da definire\" se il perimetro copre più practice."},
            {"name": "horizon",   "label": "Orizzonte temporale", "type": "select", "required": True,
             "options": [
                 "Entro un mese",
                 "Entro tre mesi",
                 "Entro sei mesi",
                 "Esplorativo, nessuna urgenza",
             ],
             "helper": "Aiuta a calendare il partner giusto sul mandato."},
            {"name": "perimeter", "label": "Breve descrizione del perimetro", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Massimo 600 caratteri. Niente nomi di controparti — verranno "
                            "discussi solo dopo NDA reciproca.",
             "helper": "Quanto basta a capire se il mandato è di nostra competenza. "
                       "I nomi di controparti si condividono solo dopo NDA reciproca."},
        ],

        "form_sections": [
            {"num": "01", "title": "Referente",
             "meta": "La persona che firmerà l'eventuale NDA preliminare.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Società",
             "meta": "Per il conflict-check preliminare.",
             "fields": ["company", "role"]},
            {"num": "03", "title": "Perimetro del mandato",
             "meta": "Nessun dettaglio sensibile qui — il perimetro tecnico si condivide in call dopo NDA reciproca.",
             "fields": ["practice", "horizon", "perimeter"]},
            {"num": "04", "title": "Allegati (facoltativi)",
             "meta": "Company profile, one-pager di governance o NDA standard: possono anticipare la call.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "briefing_allegato",
            "label":    "Documenti preliminari",
            "helper":   "Company profile, one-pager di governance o NDA standard. "
                        "PDF / DOCX · max 15 MB complessivi. Archivio cifrato con "
                        "accesso limitato ai partner Pragma.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Trascina qui i documenti o",
            "link":     "sfoglia dall'archivio",
            "meta":     "PDF / DOCX · max 15 MB · archivio cifrato",
        },

        "form_submit_label": "Richiedi la call",
        "form_submit_note":
            "Conferma da un managing partner entro 48 ore lavorative. "
            "Nessun BDR esterno, nessuna automazione di sequence.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi del "
            "Regolamento UE 679/2016. I dati sono custoditi in archivio "
            "cifrato con accesso limitato ai partner Pragma. Nessun dato "
            "viene comunicato a terzi senza esplicita autorizzazione.",

        # Sidebar — offices + contact channels
        "offices_label":   "Le sedi",
        "offices": [
            {
                "city":    "Milano",
                "tag":     "Headquarters",
                "address": "Via Filodrammatici 10 · 20121",
                "area":    "Porta Nuova · vicino Piazza della Scala",
                "phone":   "+39 02 3611 9900",
                "email":   "milano@pragmaadvisors.it",
            },
            {
                "city":    "Frankfurt",
                "tag":     "DACH desk",
                "address": "Bockenheimer Landstr. 51 · 60325",
                "area":    "Westend · vicino Alte Oper",
                "phone":   "+49 69 8870 4400",
                "email":   "frankfurt@pragmaadvisors.it",
            },
            {
                "city":    "Zürich",
                "tag":     "Wealth desk",
                "address": "Paradeplatz 8 · 8001",
                "area":    "Innenstadt · vicino Bahnhofstrasse",
                "phone":   "+41 44 215 7700",
                "email":   "zurich@pragmaadvisors.it",
            },
        ],

        "channels_label": "Canali diretti",
        "channels": [
            ("Segreteria advisory",   "+39 02 3611 9900",         "Lun – Ven · 9:00 – 19:00"),
            ("Email istituzionale",   "segreteria@pragmaadvisors.it", "Risposta entro 48 ore"),
            ("LinkedIn aziendale",    "in/pragma-advisors",        "Per relazioni pubbliche"),
        ],

        "footnote":
            "Pragma Advisors non risponde a richieste anonime e non rilascia "
            "opinioni preliminari via email senza una prima call con un partner. "
            "Le informazioni amministrative (compensi indicativi, modalità di "
            "fatturazione, criteri di accettazione del mandato) sono illustrate "
            "in prima call, non per iscritto.",
    },
}
