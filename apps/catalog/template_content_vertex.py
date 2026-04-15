"""Vertex — Creative Studio · IT content registry.

Agency live rollout, Phase 2g3.6f, Session 49.

Voice contract (Milano independent creative-studio register):
- Third-person plural subject when talking about the studio
  ("disegniamo", "firmiamo", "accompagniamo") but always editorial,
  never over-familiar. Mai "noi vi offriamo" — il tono è curatoriale.
- Milano-craft register: "brief", "sistema visivo", "serie di stampa",
  "manuale di marca", "linee editoriali", "collana" — non
  growth / KPI / sprint vocabulary (quello è Aura).
- Clients are cultural / luxury / premium retail / editoriali —
  fondazioni, case editrici, maison, musei, marchi indipendenti.
- Numbers stay restrained. Never "3x conversione". Sometimes
  "settimane" / "otto anni" / "dodici titoli" scritti a parola.
"""
from __future__ import annotations

from typing import Any


VERTEX_CONTENT_IT: dict[str, Any] = {

    "pages": [
        {"slug": "home",     "label": "Studio",     "kind": "home"},
        {"slug": "studio",   "label": "Chi siamo",  "kind": "about"},
        {"slug": "capacita", "label": "Capacità",   "kind": "services"},
        {"slug": "lavori",   "label": "Lavori",     "kind": "project_list"},
        {"slug": "manifesto","label": "Manifesto",  "kind": "process"},
        {"slug": "contatti", "label": "Contatti",   "kind": "contact"},
    ],

    # ── Site chrome ──────────────────────────────────────────────
    "site": {
        "logo_word":   "Vertex Studio",
        "tag":         "Independent creative studio · Milano",
        "availability":"Nuove commesse · autunno 2026",
        "nav_cta":     "Richiedi il dossier",
        "inquiry_page_slug": "contatti",
        "phone":       "+39 02 4981 2066",
        "email":       "studio@vertex.milano",
        "address":     "Via Tortona 32 · 20144 Milano",
        "hours_compact": "Studio aperto · martedì / giovedì",
        "license":     "P.IVA 10456770963 · Milano",
        "footer_intro":
            "Studio creativo indipendente fondato a Milano nel 2018. "
            "Disegniamo sistemi di identità, collane editoriali e "
            "direzioni artistiche per fondazioni, maison e case "
            "editrici italiane.",
        "foot_clients_label":     "Selected clients · 2018 — 2026",
        "clients_footer_rows": [
            "FONDAZIONE PRADA", "2024",
            "MAISON GENTILUOMO", "2025",
            "ADELPHI EDIZIONI", "2024",
            "TRIENNALE MILANO", "2023",
            "MUSEO DEL '900", "2025",
            "VILLA NECCHI", "2024",
        ],
        "foot_standfirst":
            "Un marchio non dovrebbe mai sembrare appena uscito dallo studio. "
            "Un buon sistema visivo tiene la stagione. Un sistema costruito "
            "con cura tiene il decennio.",
        "foot_studio_label":      "Lo studio",
        "foot_recognition_label": "Riconoscimenti",
        "foot_recognition_rows": [
            "ADI Design Index — 2024",
            "Type Directors Club — 2023",
            "Premio Compasso d'Oro — Menzione 2022",
            "European Design Awards — 2022",
        ],
    },

    # ── HOME ─────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Studio indipendente · fondato nel 2018 · Milano",
        "headline": "Brand che <em>pesano</em>, <em>tengono</em>, <em>durano</em>.",
        "pull_quote":
            "« Il brand non è un logo. È il modo in cui una cosa "
            "ti guarda quando nessuno sta parlando di lei. »",
        "intro":
            "Siamo uno studio creativo indipendente che disegna "
            "sistemi di identità, collane editoriali e direzioni "
            "artistiche per un numero ristretto di clienti culturali "
            "e di lusso. Accompagniamo ogni marchio dal primo "
            "brief fino all'ultima tiratura.",
        "primary_cta":   "Richiedi il dossier",
        "primary_href":  "contatti",
        "secondary_cta": "Lavori selezionati",
        "secondary_href":"lavori",

        # Hero right — editorial cover tile
        "cover": {
            "image":  "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=900&q=80&auto=format&fit=crop",
            "badge":  "Case Study · 01",
            "client_name": "FONDAZIONE PRADA · Collana 2025",
            "title":  "Un sistema editoriale per <em>quattro autori</em> e ventidue titoli.",
            "discipline": "Identità · editoria",
            "year":   "2025 — 2026",
            "credit_left_label":  "Art direction",
            "credit_left_value":  "M. Serafini",
            "credit_right_label": "Rollout",
            "credit_right_value": "Ott 2025",
        },

        # Ledger
        "ledger_heading":   "Lavori <em>recenti</em>",
        "ledger_link":      "Archivio completo →",
        "ledger_page_slug": "lavori",
        "ledger_rows": [
            ("01", "Collana Narrativa Italiana", "Adelphi Edizioni",      "Identità & editoria",  "2025", "adelphi-collana-narrativa"),
            ("02", "Rebranding della Fondazione", "Fondazione Prada",      "Direzione artistica",  "2025", "fondazione-prada-rebrand"),
            ("03", "Manuale di marca integrato",  "Maison Gentiluomo",    "Branding di lusso",    "2024", "maison-gentiluomo-manuale"),
            ("04", "Segnaletica & wayfinding",    "Triennale Milano",      "Identità spaziale",    "2024", "triennale-milano-wayfinding"),
            ("05", "Serie di manifesti d'autore", "Museo del Novecento",   "Art direction",        "2024", "museo-900-manifesti"),
            ("06", "Packaging sei cuvée",         "Villa Necchi Winery",   "Packaging d'autore",   "2023", "villa-necchi-sei-cuvee"),
        ],

        # Capacità
        "capab_label":   "Capacità dello studio",
        "capab_heading": "Quattro <em>discipline</em>, una sola direzione.",
        "capab_intro":
            "Lavoriamo su quattro assi che si intrecciano in ogni "
            "progetto: identità di marca, linee editoriali, direzione "
            "artistica e campagne. Non siamo un'agenzia di servizio — "
            "siamo uno studio che costruisce sistemi.",
        "capab_items": [
            ("01", "Identità di marca",
             "Logo, sistema tipografico, palette, griglia, manuale. "
             "Dalla prima restituzione al rollout sulle tangibili, "
             "in sei-dodici settimane.",
             ["Logotipo", "Manuale", "Typeface curata", "Griglia"]),
            ("02", "Linee editoriali",
             "Collane, riviste, cataloghi, libri d'autore. "
             "Costruiamo la griglia, scegliamo i caratteri, "
             "seguiamo la stampa.",
             ["Collane", "Riviste", "Cataloghi", "Libri"]),
            ("03", "Direzione artistica",
             "Campagne stagionali, shooting d'autore, "
             "manifesti, materiali POP. Dalla moodboard "
             "allo scatto, fino alla stampa.",
             ["Campagne", "Shooting", "Manifesti", "Motion"]),
            ("04", "Sistemi visivi",
             "Segnaletica, wayfinding, allestimenti, "
             "ambienti espositivi. Identità che si "
             "abitano, non che si guardano.",
             ["Wayfinding", "Segnaletica", "Allestimento", "Mostre"]),
        ],

        # Press
        "press_heading": "Pubblicato <em>e riconosciuto</em>.",
        "press_intro":
            "La nostra è una pratica piccola, deliberata, "
            "che sceglie i progetti con cura. Ma quando un lavoro "
            "tiene, il lavoro si fa notare.",
        "press_publications": [
            "Monocle", "Domus", "Wallpaper*", "Creative Review",
            "It's Nice That", "Design Week", "Eye Magazine", "Slanted",
        ],

        # Manifesto
        "manifesto_label":   "Manifesto breve",
        "manifesto_heading": "Un marchio <em>non si decora</em>. Si costruisce.",
        "manifesto_drop_cap": "U",
        "manifesto_body":
            "n buon progetto parte da una domanda che nessuno "
            "ha ancora il coraggio di fare. Disegnare un brand "
            "non vuol dire impacchettare ciò che un cliente "
            "già pensa di sapere di sé — vuol dire aiutarlo a "
            "riconoscere quello che già sa ma non ha ancora "
            "nominato. Per questo non accettiamo commesse "
            "di impulso. Per questo ogni relazione parte con "
            "una conversazione, mai con un preventivo.",
        "manifesto_principles": [
            ("01", "La forma <em>segue la voce</em>",
             "La scelta tipografica viene dopo la scelta del tono. "
             "Prima si decide come una marca parla, poi come appare."),
            ("02", "Il sistema <em>prima dell'immagine</em>",
             "Disegniamo regole, non applicazioni. Il compito "
             "di una buona regola è farsi dimenticare."),
            ("03", "La carta <em>tiene il tempo</em>",
             "Ogni progetto deve superare almeno due stagioni "
             "di tendenza senza perdere posizione. Altrimenti è arredo."),
            ("04", "Il cliente <em>è un coautore</em>",
             "Lavoriamo con chi ha voce. Chi cerca un servizio "
             "silenzioso troverà una risposta gentile ma ferma."),
        ],

        # Inquiry CTA
        "cta_label":   "Prossimo passo",
        "cta_heading": "Un brief ben fatto <em>vale sei settimane</em>.",
        "cta_sub":
            "Rispondiamo entro tre giorni lavorativi con un breve "
            "dossier di lettura del progetto.",
        "cta_primary": "Richiedi il dossier",
    },

    # ── STUDIO (about) ───────────────────────────────────────────
    "studio": {
        "eyebrow":   "Lo studio · otto anni",
        "headline":  "Quaranta metri quadri di carta, prove di stampa <em>e caratteri ancora da scegliere</em>.",
        "standfirst":
            "Siamo tre direttori creativi, due designer senior, "
            "una project manager e un fotografo che passa di qui "
            "tre volte alla settimana. Lo studio ha fatto otto "
            "compleanni, trentadue progetti che hanno cambiato "
            "casa, e un archivio di prove di stampa che non sta "
            "più dietro la porta.",

        "facts": [
            ("8",    "anni di attività",    "Fondato nel 2018 a Milano"),
            ("42",   "progetti in archivio", "Di cui 22 pubblicati"),
            ("6",    "collaboratori",        "Tre partner · tre senior"),
            ("2",    "stagioni di rollout", "Il tempo medio di un brand"),
        ],

        "essay_label":   "Storia dello studio",
        "essay_heading": "Abbiamo cominciato con <em>un carattere e una domanda</em>.",
        "essay_paragraphs": [
            "Vertex nasce nel 2018 da un'idea di Margherita Serafini "
            "e Tommaso Boeri, compagni di corso all'ISIA di Urbino "
            "e poi collaboratori in due studi milanesi. La domanda "
            "di partenza era molto semplice: <em>perché tanti brand "
            "italiani sono bellissimi da scoprire e dimenticabili "
            "dopo due mesi?</em>",
            "La risposta — capita lentamente, progetto dopo progetto — "
            "è che la maggior parte dei brand viene disegnata come si "
            "veste una vetrina: si sceglie quello che si vede per primo, "
            "non quello che regge il tempo. Disegnare un sistema di "
            "marca che tenga otto anni non è una questione di "
            "tendenze, ma di scelte che si tolgono quando serve.",
        ],
        "essay_pullquote":
            "Un manuale ben fatto non descrive il marchio. "
            "Lo difende dalla nostra stessa voglia di cambiarlo.",
        "essay_tail_paragraphs": [
            "Oggi lo studio lavora in media con otto clienti all'anno. "
            "Rifiutiamo più della metà dei brief che riceviamo — non per "
            "mestiere, ma per onestà: un progetto fatto male fa male "
            "due volte, al cliente e al portfolio.",
            "Abbiamo scelto di restare piccoli. Non abbiamo ambizioni "
            "di scala. Vogliamo continuare a rispondere personalmente "
            "a ogni prima email, a seguire ogni prova di stampa, "
            "a conoscere il nome dei tipografi che stampano i nostri libri.",
        ],

        "partners_label":   "I tre partner",
        "partners_heading": "Chi <em>firma</em> lo studio.",
        "partners_intro":
            "Ogni progetto viene seguito da almeno uno dei tre partner "
            "dal primo brief al rollout finale. Non deleghiamo i momenti "
            "decisivi — se un brand parte bene, è perché c'era qualcuno "
            "presente quando si è detto di no a una prima idea.",
        "partners": [
            {
                "name": "Margherita Serafini",
                "role": "Co-fondatrice · Direttore creativo",
                "bio":  "Diploma in grafica editoriale all'ISIA di Urbino. "
                        "Prima di Vertex, otto anni a Cabinet (Milano) "
                        "come senior designer. Ossessionata dai caratteri "
                        "serif del secondo Novecento.",
                "portrait": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=900&q=80&auto=format&fit=crop",
                "creds": ["ISIA Urbino", "ADI Design Index 2024", "Docente IED"],
            },
            {
                "name": "Tommaso Boeri",
                "role": "Co-fondatore · Direttore artistico",
                "bio":  "Formato a ECAL Losanna. Ha lavorato per Studio "
                        "Dumbar e M/M Paris prima di tornare a Milano. "
                        "Art director di due case editrici indipendenti.",
                "portrait": "https://images.unsplash.com/photo-1568602471122-7832951cc4c5?w=900&q=80&auto=format&fit=crop",
                "creds": ["ECAL Losanna", "TDC Award 2023", "European Design"],
            },
            {
                "name": "Ilaria Ferri",
                "role": "Partner · Direttore editoriale",
                "bio":  "Laurea in lettere alla Statale di Milano. "
                        "Dieci anni in Adelphi prima di unirsi allo "
                        "studio nel 2021. Cura le linee editoriali "
                        "e la redazione dei manuali.",
                "portrait": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop",
                "creds": ["Statale Milano", "ex Adelphi", "Premio Gutenberg"],
            },
        ],

        "timeline_label":   "Cronologia",
        "timeline_heading": "Otto anni <em>in carta</em>.",
        "timeline_rows": [
            ("2018",
             "Apertura dello studio in Via Tortona 32",
             "Primo progetto: rebrand della libreria indipendente Scheiwiller. "
             "Serafini e Boeri firmano il primo manuale dello studio su un foglio A3."),
            ("2020",
             "Prima commessa istituzionale",
             "Direzione artistica per Triennale Milano — ventidue mesi di lavoro "
             "sulla segnaletica delle sale permanenti."),
            ("2021",
             "Ingresso di Ilaria Ferri come partner",
             "Apertura della pratica editoriale con la prima collana per Adelphi "
             "— nove titoli usciti in diciotto mesi."),
            ("2023",
             "Riconoscimento ADI Design Index",
             "Premio per la collana Architetture Contemporanee. "
             "Prima copertina italiana di Eye Magazine."),
            ("2025",
             "Rebranding Fondazione Prada",
             "Ventidue mesi di lavoro. Rollout completo nell'autunno 2025, "
             "con segnaletica, editoriale, campagne stagionali."),
            ("2026",
             "Apertura della seconda stanza",
             "Espansione in Via Tortona 34, con archivio prove di stampa "
             "consultabile su appuntamento."),
        ],
    },

    # ── CAPACITA (services) ──────────────────────────────────────
    "capacita": {
        "eyebrow":   "Capacità dello studio",
        "headline":  "Quattro <em>discipline</em> che si intrecciano in ogni progetto.",
        "standfirst":
            "Non siamo un'agenzia a servizio completo. Siamo uno studio "
            "che lavora su quattro assi chiari, ognuno con una pratica "
            "stabile e un processo documentato. Ogni progetto attinge da "
            "uno o più di questi assi — raramente da tutti insieme.",

        "disciplines": [
            {
                "num": "01",
                "title": "Identità di <em>marca</em>",
                "tagline": "Logo, carattere, griglia, manuale. Sei-dodici settimane.",
                "body":
                    "Costruiamo sistemi di identità che tengono otto anni. "
                    "Ogni rebrand parte da una conversazione con il direttore "
                    "generale o il fondatore — mai da un brief inviato via email. "
                    "Restituiamo tre direzioni, poi una sola. Il manuale finale "
                    "ha un'indice che serve, non uno che impressiona.",
                "scope_label": "Incluso",
                "scope": [
                    "Logotipo e variazioni",
                    "Sistema tipografico (retail + display)",
                    "Tavola cromatica estesa",
                    "Griglia e regole compositive",
                    "Manuale di marca (PDF interattivo + stampa)",
                    "Plate di applicazioni (stampa · web · ambiente)",
                ],
            },
            {
                "num": "02",
                "title": "Linee <em>editoriali</em>",
                "tagline": "Collane, riviste, cataloghi, libri d'autore.",
                "body":
                    "La pratica editoriale è il cuore dello studio. Disegniamo "
                    "collane che reggono la stagione — la griglia, il formato, "
                    "la gabbia, le copertine. Seguiamo la stampa fino alla prova "
                    "in macchina, con i tipografi di fiducia di Milano e Bergamo. "
                    "Siamo presenti a tutti i primi libri di ogni collana firmata.",
                "scope_label": "Incluso",
                "scope": [
                    "Disegno del formato e gabbia",
                    "Copertina (sistema + applicazione)",
                    "Impostazione tipografica retail",
                    "Consulenza di stampa e carta",
                    "Segui-stampa sul primo titolo",
                    "Scheda applicazione per l'ufficio grafico interno",
                ],
            },
            {
                "num": "03",
                "title": "Direzione <em>artistica</em>",
                "tagline": "Campagne, shooting d'autore, manifesti.",
                "body":
                    "Dirigiamo campagne stagionali per maison e marchi "
                    "italiani con un approccio editoriale — mai pubblicitario. "
                    "Scegliamo i fotografi, costruiamo la moodboard, "
                    "seguiamo lo shooting. Le campagne nascono per reggere "
                    "due cicli editoriali — non una settimana di social.",
                "scope_label": "Incluso",
                "scope": [
                    "Concept stagionale (PDF di lettura · 24 pagine)",
                    "Cast fotografico + direzione",
                    "Direzione del giorno di shooting",
                    "Selezione e post-produzione",
                    "Sistema di applicazione (stampa · digital · retail)",
                    "Manifesti + collaterali di lancio",
                ],
            },
            {
                "num": "04",
                "title": "Sistemi <em>spaziali</em>",
                "tagline": "Segnaletica, wayfinding, allestimento.",
                "body":
                    "Quando un'identità diventa un luogo, la progettiamo "
                    "insieme all'architetto. Wayfinding permanente per "
                    "musei e fondazioni, allestimenti temporanei di "
                    "mostre, segnaletica per retail di lusso. Ogni sistema "
                    "spaziale parte da un sopralluogo. Non lavoriamo mai da render.",
                "scope_label": "Incluso",
                "scope": [
                    "Sopralluogo e restituzione tecnica",
                    "Griglia di lettura dello spazio",
                    "Sistema tipografico + pittogrammatico",
                    "Tavole esecutive per produzione",
                    "Collaborazione con studio di architettura",
                    "Presenza in cantiere · prima installazione",
                ],
            },
        ],

        "engagement_label":   "Tre modi di lavorare",
        "engagement_heading": "Dal <em>progetto singolo</em> al <em>partner editoriale</em>.",
        "engagement_intro":
            "Accettiamo tre tipi di incarico. Li disegniamo insieme al "
            "cliente in fase di brief — non abbiamo listini nascosti.",
        "engagement_tiles": [
            {
                "title":  "Progetto <em>singolo</em>",
                "range":  "Dodici — ventiquattro settimane",
                "body":   "Un'identità o una linea editoriale, dal brief al rollout. "
                          "Per marchi che hanno bisogno di un gesto netto e definito.",
                "includes": [
                    "Brief congiunto + tre direzioni",
                    "Rollout su tre applicazioni",
                    "Manuale di marca in italiano / inglese",
                    "Presenza al lancio",
                ],
            },
            {
                "title":  "Commessa <em>stagionale</em>",
                "range":  "Sei — dodici mesi · contratto rinnovabile",
                "body":   "Direzione artistica stagionale per maison o istituzioni. "
                          "Due campagne all'anno, con tutte le applicazioni.",
                "includes": [
                    "Campagna primavera / autunno",
                    "Collaterali di lancio",
                    "Presenza mensile allo studio",
                    "Archivio condiviso",
                ],
            },
            {
                "title":  "Partner <em>editoriale</em>",
                "range":  "Impegno annuale · su invito",
                "body":   "Presenza costante al tavolo editoriale del cliente. "
                          "Per case editrici, fondazioni, istituzioni culturali.",
                "includes": [
                    "Partecipazione al piano editoriale",
                    "Direzione su tutte le uscite dell'anno",
                    "Consulenza di stampa e carta",
                    "Archivio + backup creativo",
                ],
            },
        ],

        "cta_label":   "Brief gratuito",
        "cta_heading": "Un primo <em>tè insieme</em> non costa nulla.",
        "cta_primary": "Richiedi il dossier",
    },

    # ── LAVORI (project_list) ────────────────────────────────────
    "lavori": {
        "eyebrow":   "Archivio lavori · 2018 — 2026",
        "headline":  "Quarantadue progetti <em>in archivio</em>, ventidue in vetrina.",
        "standfirst":
            "Una selezione ragionata. Non mostriamo tutto — non tutto "
            "regge la rilettura. L'archivio completo è disponibile su "
            "richiesta, in formato PDF stampabile (centosei pagine).",
        "filters": ["Tutti", "Identità", "Editoria", "Art direction", "Sistemi spaziali"],

        "projects": [
            {
                "slug":       "fondazione-prada-rebrand",
                "index":      "01",
                "title":      "Rebranding della Fondazione",
                "client":     "Fondazione Prada — Milano",
                "discipline": "Direzione artistica",
                "year":       "2025",
            },
            {
                "slug":       "adelphi-collana-narrativa",
                "index":      "02",
                "title":      "Collana Narrativa Italiana",
                "client":     "Adelphi Edizioni — Milano",
                "discipline": "Identità & editoria",
                "year":       "2025",
            },
            {
                "slug":       "maison-gentiluomo-manuale",
                "index":      "03",
                "title":      "Manuale di marca integrato",
                "client":     "Maison Gentiluomo — Firenze",
                "discipline": "Branding di lusso",
                "year":       "2024",
            },
            {
                "slug":       "triennale-milano-wayfinding",
                "index":      "04",
                "title":      "Segnaletica & wayfinding permanente",
                "client":     "Triennale Milano — Parco Sempione",
                "discipline": "Identità spaziale",
                "year":       "2024",
            },
            {
                "slug":       "museo-900-manifesti",
                "index":      "05",
                "title":      "Serie di manifesti d'autore",
                "client":     "Museo del Novecento — Milano",
                "discipline": "Art direction",
                "year":       "2024",
            },
            {
                "slug":       "villa-necchi-sei-cuvee",
                "index":      "06",
                "title":      "Packaging sei cuvée d'autore",
                "client":     "Villa Necchi Winery — Valpolicella",
                "discipline": "Packaging",
                "year":       "2023",
            },
        ],

        "archive_label":   "Archivio completo",
        "archive_heading": "Disponibile <em>su richiesta</em>, centosei pagine.",
        "archive_body":
            "L'archivio completo contiene quarantadue progetti dal 2018, "
            "con processo di lavoro, campionature di stampa, note "
            "editoriali e coordinate del cliente.",
        "archive_stats": [
            ("42",   "progetti in archivio"),
            ("22",   "pubblicati"),
            ("8",    "anni di pratica"),
            ("<em>6</em>", "clienti all'anno in media"),
        ],
    },

    # ── MANIFESTO (process) ──────────────────────────────────────
    "manifesto": {
        "eyebrow":   "Il nostro modo di lavorare",
        "headline":  "Sei settimane per <em>capire</em>. Dieci per <em>costruire</em>. Due per <em>difendere</em>.",
        "standfirst":
            "Ogni progetto attraversa quattro fasi dichiarate. "
            "Non ci piacciono le sorprese — né per noi, né per il "
            "cliente. La timeline è pubblica dal primo giorno.",

        "phases": [
            {
                "num": "01",
                "duration": "Settimane 1 — 6",
                "title": "<em>Ascolto</em> · letture · sopralluogo",
                "tagline": "Capire prima di disegnare.",
                "body":
                    "Incontriamo il direttore generale, il responsabile comunicazione "
                    "e, quando possibile, i clienti. Leggiamo l'archivio, gli studi "
                    "precedenti, le relazioni annuali. Visitiamo gli spazi. Nessuna "
                    "forma viene proposta in questa fase — solo una lettura scritta "
                    "di 24-32 pagine che diventa la base del progetto.",
                "deliverables_label": "Consegne",
                "deliverables": [
                    "Dossier di lettura (24-32 pagine PDF)",
                    "Tre territori strategici da esplorare",
                    "Tavola di riferimento storico",
                    "Calendario dettagliato dei deliverable successivi",
                ],
            },
            {
                "num": "02",
                "duration": "Settimane 7 — 14",
                "title": "<em>Ipotesi</em> · tre direzioni",
                "tagline": "Tre proposte, nessuna compromessa.",
                "body":
                    "Presentiamo tre direzioni creative pienamente costruite — "
                    "non tre varianti di una stessa intuizione. Ogni direzione ha "
                    "logo, carattere, due applicazioni pilota. Il cliente sceglie "
                    "una direzione (o chiede un quarto giro — succede raramente).",
                "deliverables_label": "Consegne",
                "deliverables": [
                    "Tre direzioni creative (24 tavole a testa)",
                    "Un'applicazione pilota per direzione",
                    "Lettura comparativa scritta",
                    "Presentazione in studio · mezza giornata",
                ],
            },
            {
                "num": "03",
                "duration": "Settimane 15 — 22",
                "title": "<em>Costruzione</em> · sistema & manuale",
                "tagline": "Dalla direzione al manuale, senza perdere il tono.",
                "body":
                    "La direzione scelta viene sviluppata in un sistema completo: "
                    "griglia, palette estesa, variazioni del marchio, regole "
                    "compositive, manuale finale. Parallelamente costruiamo "
                    "tre-cinque applicazioni campione per testare il sistema "
                    "sui casi reali.",
                "deliverables_label": "Consegne",
                "deliverables": [
                    "Sistema di marca completo (file sorgente)",
                    "Manuale di marca (PDF interattivo + versione stampa)",
                    "Tre-cinque applicazioni campione",
                    "Font retail + licenze documentate",
                ],
            },
            {
                "num": "04",
                "duration": "Settimane 23 — 24",
                "title": "<em>Rollout</em> · difesa · chiusura",
                "tagline": "Il manuale prende vita, noi restiamo vicini.",
                "body":
                    "Accompagniamo il rollout sulle prime applicazioni reali "
                    "con presenza in studio e consulenza al team interno del "
                    "cliente. Seguiamo la prima tiratura importante. Chiudiamo "
                    "con una riunione di handover documentata, dove il "
                    "responsabile interno diventa custode del sistema.",
                "deliverables_label": "Consegne",
                "deliverables": [
                    "Presenza al lancio pubblico",
                    "Prime applicazioni seguite personalmente",
                    "Riunione di handover + documento di governance",
                    "Sei mesi di disponibilità per chiarimenti",
                ],
            },
        ],

        "principles_label":   "Principi di studio",
        "principles_heading": "<em>Sette</em> impegni che non negoziamo.",
        "principles": [
            ("01", "Un <em>capitolo alla volta</em>",
             "Mai due fasi insieme. Un cliente che accelera una fase compromette la successiva. Abbiamo disdetto più di un contratto su questo punto."),
            ("02", "<em>Tre direzioni</em>, mai quattro",
             "Quattro direzioni rendono la scelta arbitraria. Tre obbligano a un ragionamento. Due sarebbero pigre."),
            ("03", "Il <em>carattere</em> si licenzia",
             "Non usiamo font free per progetti pagati. Ogni licenza è documentata al cliente, con budget separato."),
            ("04", "La <em>stampa</em> si presenzia",
             "Il primo avvio di macchina su ogni rollout importante viene seguito da un partner dello studio."),
            ("05", "Il <em>cliente</em> è coautore",
             "Il cliente firma il manuale insieme allo studio. Non è un servizio — è un progetto condiviso."),
            ("06", "<em>No</em> è parte del servizio",
             "Diciamo di no più di quanto proponiamo. È il principale valore che portiamo."),
        ],

        "promise_label":   "I nostri numeri",
        "promise_heading": "Piccoli <em>per scelta</em>, lenti <em>per metodo</em>.",
        "promise_stats": [
            ("<em>6</em>",       "clienti all'anno in media",
             "Più di 12 brief ricevuti al mese, meno di 6 accettati all'anno."),
            ("<em>8</em>",       "anni di durata media",
             "Le identità firmate tra 2018 e 2022 sono ancora tutte attive."),
            ("<em>3 gg</em>",    "risposta al primo brief",
             "Entro tre giorni lavorativi riceverai una prima lettura scritta del progetto."),
        ],
    },

    # ── CONTATTI (contact) ───────────────────────────────────────
    "contatti": {
        "eyebrow":   "Richiedi il dossier",
        "headline":  "Raccontaci <em>il progetto</em>. Rispondiamo entro tre giorni.",
        "standfirst":
            "Ogni email arriva direttamente a Margherita o Tommaso. "
            "Non c'è un account manager filtro — chi ti risponde è "
            "chi seguirà il progetto in prima persona, se deciderete "
            "di lavorare insieme.",

        "form_heading": "Brief del progetto",
        "labels": {
            "name":       "Nome e cognome",
            "role":       "Ruolo nell'organizzazione",
            "company":    "Organizzazione / marchio",
            "email":      "Email di contatto",
            "discipline": "Disciplina principale richiesta",
            "budget":     "Banda di budget indicativa",
            "brief":      "Racconto del progetto",
        },
        "placeholders": {
            "name":    "Nome Cognome",
            "role":    "es. Direttore comunicazione",
            "company": "Nome dell'organizzazione",
            "email":   "nome@organizzazione.it",
            "brief":   "Chi sei, cosa stai cercando di costruire, in quale tempo, con quale team interno. Più è concreto, più la risposta sarà utile.",
        },
        "discipline_options": [
            "Identità di marca (rebrand)",
            "Identità di marca (primo lancio)",
            "Linea editoriale · collana",
            "Direzione artistica · campagna",
            "Sistema spaziale · wayfinding",
            "Non sono ancora sicuro — parliamone",
        ],
        "budget_bands": [
            ("12k",  "< 12 K €"),
            ("40k",  "12 — 40 K €"),
            ("120k", "40 — 120 K €"),
            ("120plus","> 120 K €"),
        ],
        "form_submit_label": "Invia il brief",
        "form_submit_note":  "Rispondiamo entro tre giorni lavorativi con una prima lettura.",

        "direct_label":   "Email diretta",
        "direct_heading": "Scrivi a <em>Margherita</em> e <em>Tommaso</em>.",

        "studio_label":   "Lo studio",

        "reply_label":    "Tempi di risposta",
        "reply_heading":  "Tre <em>giorni lavorativi</em>, non di più.",
        "reply_body":
            "Ogni brief riceve entro 72 ore una prima lettura scritta: "
            "ti diciamo se il progetto fa per noi, se il momento è giusto, "
            "se ci vediamo di persona per approfondire. "
            "Mai risposte automatiche, mai preventivi senza lettura.",

        "channels_label": "Canali",
        "channels": [
            ("Email",      "studio@vertex.milano"),
            ("Telefono",   "+39 02 4981 2066"),
            ("Studio",     "Via Tortona 32 · Milano"),
            ("LinkedIn",   "/company/vertex-milano"),
            ("Are.na",     "/vertex-studio"),
            ("Segreteria", "mar · gio · 10 — 18"),
        ],

        "promise_label":   "Un impegno",
        "promise_heading":
            "« Non inviamo mai un preventivo prima di un brief di lettura. "
            "È un piccolo gesto, ma cambia la conversazione. »",
    },

    # ── POSTS (project_detail) ───────────────────────────────────
    "posts": [
        {
            "slug": "fondazione-prada-rebrand",
            "index": "01",
            "title": "Un <em>rebranding istituzionale</em> che non si fa notare.",
            "client": "Fondazione Prada — Milano",
            "discipline": "Direzione artistica · identità",
            "year": "2025",
            "team": "Serafini · Boeri · Ferri",
            "standfirst":
                "Un ridisegno dell'identità istituzionale pensato per reggere "
                "venti anni di programmazione culturale, senza chiedere al "
                "visitatore di imparare un nuovo vocabolario visivo.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Anno di consegna",
            "meta_label_team":       "Team dello studio",
            "cover_image": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "Il problema",
                    "title": "Un'istituzione <em>letta per errore</em>.",
                    "paragraphs": [
                        "Quando la Fondazione ci ha chiamati, nel primo trimestre 2024, "
                        "il punto non era il marchio — il marchio funzionava. Il problema "
                        "era che <em>l'identità non accompagnava più il programma</em>.",
                        "La Fondazione aveva pubblicato cinquantadue eventi nel 2023, "
                        "ma i comunicati stampa sembravano tutti <em>una stessa istituzione "
                        "stanca</em>. La colpa non era del marchio. Era del sistema — un "
                        "manuale del 2011, pensato per un programma molto più ristretto.",
                    ],
                },
                {
                    "label": "Il metodo",
                    "title": "Disegnare una <em>seconda voce</em>, non un secondo logo.",
                    "paragraphs": [
                        "Abbiamo scelto di non toccare il marchio principale. Abbiamo "
                        "disegnato invece un <em>sistema editoriale parallelo</em> — una "
                        "seconda voce visiva, usata per tutta la comunicazione del programma. "
                        "Il marchio istituzionale resta, ma si fa da parte.",
                        "Questa scelta ha permesso di evitare la frattura che accompagna "
                        "ogni rebranding — nessuno ha dovuto disinstallare niente. "
                        "La nuova voce si è accostata alla vecchia, conquistando spazio "
                        "progressivamente, stagione dopo stagione.",
                    ],
                    "pullquote":
                        "Il marchio istituzionale è una firma. La seconda voce è un modo "
                        "di parlare. Una firma non cambia — il modo di parlare può evolvere.",
                },
                {
                    "label": "Il risultato",
                    "title": "Una <em>stagione</em>, cinquantadue eventi, una sola voce.",
                    "paragraphs": [
                        "La nuova voce editoriale è stata applicata per la prima volta "
                        "nella stagione autunno 2025, su cinquantadue eventi pubblicati. "
                        "Il team interno di comunicazione ha adottato il sistema con "
                        "sei giorni di affiancamento in studio. Nessun contenuto è stato "
                        "rifatto — tutto è stato ri-vestito.",
                    ],
                },
            ],
            "deliverables_label": "Consegne",
            "deliverables_heading": "Quattro <em>sistemi</em>, un solo manuale.",
            "deliverables_intro":
                "Il manuale finale — 184 pagine — è stato redatto insieme al team "
                "di comunicazione della Fondazione, con glossario condiviso.",
            "deliverables": [
                ("01", "Sistema editoriale secondario",
                 "Tipografia, griglia, palette stagionale, variazioni regionali. "
                 "Applicato a tutti i materiali del programma — inviti, brochure, social."),
                ("02", "Manuale di marca integrato",
                 "184 pagine, italiano + inglese. Contiene i due sistemi (storico + nuovo) "
                 "con criteri chiari di quando usare l'uno o l'altro."),
                ("03", "Template di produzione autonoma",
                 "File sorgente pronti per l'ufficio grafico interno. "
                 "Tre tipologie (invito, comunicato, brochure) × quattro stagioni."),
            ],
            "press_quote":
                "Un rebranding quasi invisibile che ha cambiato il respiro dell'istituzione. "
                "Raro, in Italia, vedere uno studio che sceglie di farsi da parte.",
            "press_source":     "Domus — Novembre 2025",
            "press_journalist": "Giulia Bellini",
            "next_label":       "Prossimo caso",
            "next_heading":     "Vai all'<em>archivio lavori</em> →",
            "cta_label":        "Commesse 2026",
            "cta_heading":      "Apri il <em>dossier dello studio</em> →",
        },
        {
            "slug": "adelphi-collana-narrativa",
            "index": "02",
            "title": "Una <em>collana</em> per diciotto voci narrative.",
            "client": "Adelphi Edizioni — Milano",
            "discipline": "Identità & editoria",
            "year": "2025",
            "team": "Ferri · Serafini",
            "standfirst":
                "Il disegno di una nuova collana narrativa contemporanea per una "
                "casa editrice storica — diciotto titoli usciti in diciotto mesi, "
                "con un sistema di copertina che alterna ritratto e astrazione.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Anno di uscita",
            "meta_label_team":       "Team dello studio",
            "cover_image": "https://images.unsplash.com/photo-1481487196290-c152efe083f5?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "Il brief",
                    "title": "Una <em>collana che non assomigli</em> a una collana.",
                    "paragraphs": [
                        "Adelphi voleva aprire uno spazio per autori narrativi contemporanei "
                        "italiani, ma senza tradire il tono silenzioso e meditato della casa. "
                        "Il brief iniziale era deliberatamente minimo: <em>una collana che si "
                        "riconosca senza sembrare una collana</em>.",
                    ],
                },
                {
                    "label": "La scelta",
                    "title": "Ritratto <em>e</em> astrazione, mai insieme.",
                    "paragraphs": [
                        "Abbiamo proposto un sistema che alterna due registri: copertine con "
                        "fotografia (ritratto dell'autore su carta lavorata) e copertine "
                        "astratte (composizioni tipografiche con il solo titolo). La scelta "
                        "tra i due registri spetta al direttore editoriale, caso per caso.",
                    ],
                    "pullquote":
                        "Il sistema non obbliga. Suggerisce. La migliore regola editoriale "
                        "è quella che il direttore può violare una volta, con ragione.",
                },
            ],
            "deliverables_label": "Consegne",
            "deliverables_heading": "Un sistema <em>discreto</em>, diciotto voci distinte.",
            "deliverables_intro":
                "Ogni titolo viene seguito da Ilaria Ferri in fase di scelta della "
                "copertina e in prova di stampa, per le prime tre stagioni.",
            "deliverables": [
                ("01", "Disegno di formato + gabbia",
                 "120 × 185 mm, carta Palatina 80 g, brossura filo refe. "
                 "Gabbia con due opzioni di impaginazione per testi densi."),
                ("02", "Sistema di copertina",
                 "Due registri alternati (ritratto / astrazione) con palette "
                 "di quattro colori. Regole di composizione documentate."),
                ("03", "Primo titolo · Come ci vedono gli uccelli",
                 "Seguito dalla prima prova di stampa alla tiratura finale, "
                 "con segui-stampa in tipografia a Bergamo."),
            ],
            "press_quote":
                "Una collana che aggiunge senza spostare. Molto Adelphi, molto nuovo.",
            "press_source":     "Corriere della Sera · La Lettura — Dicembre 2025",
            "press_journalist": "Andrea Pomella",
            "next_label":       "Prossimo caso",
            "next_heading":     "Vai all'<em>archivio lavori</em> →",
            "cta_label":        "Pratica editoriale",
            "cta_heading":      "Apri il <em>dossier editoriale</em> →",
        },
        {
            "slug": "maison-gentiluomo-manuale",
            "index": "03",
            "title": "Un <em>manuale di marca</em> per la terza generazione.",
            "client": "Maison Gentiluomo — Firenze",
            "discipline": "Branding di lusso",
            "year": "2024",
            "team": "Boeri · Serafini",
            "standfirst":
                "Il ridisegno integrato di una maison fiorentina al passaggio "
                "della terza generazione — un rebranding pensato per custodire, "
                "non per rinnovare.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Anno di consegna",
            "meta_label_team":       "Team dello studio",
            "cover_image": "https://images.unsplash.com/photo-1586717791821-3f44a563fa4c?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "Il contesto",
                    "title": "Una <em>maison</em> senza manuale.",
                    "paragraphs": [
                        "Gentiluomo era una maison di pelletteria fondata nel 1967 "
                        "a Firenze. Alla terza generazione — due sorelle, quaranta "
                        "e trentasei anni — la comunicazione era ancora gestita come "
                        "un'emergenza settimanale. Niente sistema, niente regole, "
                        "niente archivio.",
                    ],
                },
                {
                    "label": "Il metodo",
                    "title": "Risalire <em>al 1967</em>, non al 2024.",
                    "paragraphs": [
                        "Abbiamo passato cinque settimane in archivio a Firenze, "
                        "ricostruendo pezzo per pezzo l'identità storica — cataloghi, "
                        "biglietti, etichette, corrispondenza con i negozi. Il sistema "
                        "finale non è nuovo — è la prima versione documentata di "
                        "qualcosa che esisteva da cinquantasette anni.",
                    ],
                    "pullquote":
                        "La maison aveva già un'identità. Nessuno l'aveva mai scritta.",
                },
            ],
            "deliverables_label": "Consegne",
            "deliverables_heading": "Un <em>manuale custode</em>, 240 pagine.",
            "deliverables_intro":
                "Il manuale finale è stato firmato dalle due sorelle e dallo "
                "studio, in cerimonia privata a Firenze nell'ottobre 2024.",
            "deliverables": [
                ("01", "Ricostruzione dell'archivio storico",
                 "128 pezzi catalogati, scannerizzati, descritti. "
                 "Base documentale per ogni scelta successiva."),
                ("02", "Sistema tipografico storico + contemporaneo",
                 "Un serif italiano ridisegnato a partire dalle etichette del 1971, "
                 "accoppiato a un sans moderno per comunicazione digitale."),
                ("03", "Manuale custode",
                 "240 pagine in italiano + inglese, firmato dalle committenti. "
                 "Pensato per essere letto, non per essere consultato."),
            ],
            "press_quote":
                "Un rebranding che custodisce anziché rinnovare — una rarità a Firenze.",
            "press_source":     "Monocle — Febbraio 2025",
            "press_journalist": "Sophie Grove",
            "next_label":       "Prossimo caso",
            "next_heading":     "Vai all'<em>archivio lavori</em> →",
            "cta_label":        "Maison & lusso",
            "cta_heading":      "Apri il <em>dossier lusso</em> →",
        },
        {
            "slug": "triennale-milano-wayfinding",
            "index": "04",
            "title": "Un <em>wayfinding permanente</em> per dodici sale.",
            "client": "Triennale Milano — Parco Sempione",
            "discipline": "Identità spaziale",
            "year": "2024",
            "team": "Serafini · Boeri",
            "standfirst":
                "Il disegno di un sistema di segnaletica permanente per le "
                "dodici sale espositive della Triennale — un sistema che "
                "accompagna il visitatore senza parlare più del necessario.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Anno di installazione",
            "meta_label_team":       "Team dello studio",
            "cover_image": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "Il progetto",
                    "title": "Una <em>grammatica spaziale</em> per ventidue mesi di lavoro.",
                    "paragraphs": [
                        "La Triennale ci ha affidato il ridisegno del wayfinding "
                        "permanente nel 2022. Ventidue mesi di lavoro, dodici sale, "
                        "quattro lingue, due percorsi (visitatore + staff). Il sistema "
                        "è stato installato in fasi, senza mai chiudere al pubblico.",
                    ],
                },
                {
                    "label": "Le regole",
                    "title": "Un carattere, tre taglie, due colori.",
                    "paragraphs": [
                        "Abbiamo lavorato per sottrazione: un solo carattere (disegnato "
                        "appositamente), tre dimensioni (direzionale / informativa / "
                        "didascalica), due colori (nero + ocra). La traduzione in arabo "
                        "e cinese è stata curata con consulenti linguistici dedicati.",
                    ],
                },
            ],
            "deliverables_label": "Consegne",
            "deliverables_heading": "Un <em>sistema</em>, 420 elementi.",
            "deliverables_intro":
                "L'installazione è stata seguita in cantiere da Margherita "
                "Serafini per tre settimane consecutive.",
            "deliverables": [
                ("01", "Carattere tipografico esclusivo",
                 "Triennale Display — disegnato dallo studio, "
                 "licenziato esclusivamente alla Triennale."),
                ("02", "420 elementi di segnaletica",
                 "Dalla grande direzionale esterna alla didascalia di vetrina. "
                 "Quattro lingue, due percorsi."),
                ("03", "Manuale di gestione",
                 "Documento operativo per il team interno: cosa manutentare, "
                 "quando sostituire, come chiedere nuovi elementi."),
            ],
            "press_quote":
                "Un wayfinding che non impone — ti lascia camminare.",
            "press_source":     "Abitare — Marzo 2025",
            "press_journalist": "Filippo Romano",
            "next_label":       "Prossimo caso",
            "next_heading":     "Vai all'<em>archivio lavori</em> →",
            "cta_label":        "Sistemi spaziali",
            "cta_heading":      "Apri il <em>dossier wayfinding</em> →",
        },
        {
            "slug": "museo-900-manifesti",
            "index": "05",
            "title": "Una <em>serie di manifesti</em> d'autore per dodici mostre.",
            "client": "Museo del Novecento — Milano",
            "discipline": "Art direction",
            "year": "2024",
            "team": "Boeri · Ferri",
            "standfirst":
                "La direzione artistica di una stagione di manifesti per le "
                "mostre temporanee del Museo, con commissione di fotografi "
                "italiani emergenti.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Anno della stagione",
            "meta_label_team":       "Team dello studio",
            "cover_image": "https://images.unsplash.com/photo-1561070791-2526d30994b8?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "L'idea",
                    "title": "Un <em>manifesto</em>, un <em>autore</em>.",
                    "paragraphs": [
                        "Invece di produrre manifesti interni allo studio, abbiamo "
                        "commissionato dodici fotografi italiani emergenti — uno per "
                        "mostra — chiedendo a ognuno un'immagine di risposta all'opera "
                        "centrale della mostra.",
                    ],
                },
                {
                    "label": "Il risultato",
                    "title": "Dodici voci <em>distinte</em>, una sola griglia.",
                    "paragraphs": [
                        "La griglia tipografica è rimasta costante — stesso titolo, "
                        "stesso credito, stesso formato. La variazione vive interamente "
                        "nell'immagine. Il visitatore percepisce la coerenza della "
                        "stagione, ma ogni manifesto è uno shock autonomo.",
                    ],
                },
            ],
            "deliverables_label": "Consegne",
            "deliverables_heading": "Una <em>stagione</em>, dodici manifesti.",
            "deliverables_intro":
                "Il progetto ha vinto la Menzione ADI Design Index 2024.",
            "deliverables": [
                ("01", "Commissione fotografica",
                 "Dodici fotografi italiani emergenti scelti tra i finalisti "
                 "del Premio Graziadei 2023."),
                ("02", "Griglia tipografica stagionale",
                 "Un disegno di manifesto che regge dodici immagini diverse "
                 "senza compromessi."),
                ("03", "Catalogo della stagione",
                 "Raccolta in edizione limitata (500 copie) firmata dai dodici "
                 "fotografi + intervista con il curatore."),
            ],
            "press_quote":
                "Manifesti che non pubblicizzano la mostra — la accompagnano.",
            "press_source":     "Eye Magazine — Estate 2024",
            "press_journalist": "John L. Walters",
            "next_label":       "Prossimo caso",
            "next_heading":     "Vai all'<em>archivio lavori</em> →",
            "cta_label":        "Art direction",
            "cta_heading":      "Apri il <em>dossier stagionale</em> →",
        },
        {
            "slug": "villa-necchi-sei-cuvee",
            "index": "06",
            "title": "Un <em>packaging</em> per sei cuvée, sei autori.",
            "client": "Villa Necchi Winery — Valpolicella",
            "discipline": "Packaging d'autore",
            "year": "2023",
            "team": "Serafini · Boeri",
            "standfirst":
                "Il disegno di sei etichette per le sei cuvée storiche "
                "della cantina, ognuna firmata da un autore letterario "
                "italiano contemporaneo.",
            "meta_label_client":     "Cliente",
            "meta_label_discipline": "Disciplina",
            "meta_label_year":       "Anno della tiratura",
            "meta_label_team":       "Team dello studio",
            "cover_image": "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "Il progetto",
                    "title": "Un <em>vino</em>, un <em>testo</em>, un'etichetta.",
                    "paragraphs": [
                        "Sei cuvée storiche della Villa Necchi. Sei autori italiani "
                        "contemporanei, invitati a scrivere un breve testo (max 120 parole) "
                        "in risposta al vino che avevano degustato. I testi sono stati "
                        "poi integrati tipograficamente nell'etichetta.",
                    ],
                },
                {
                    "label": "Gli autori",
                    "title": "Sei voci <em>molto diverse</em>.",
                    "paragraphs": [
                        "Abbiamo scelto deliberatamente sei registri diversi: una poeta "
                        "siciliana, un romanziere milanese, una critica letteraria, "
                        "un autore di racconti brevi, un traduttore dal giapponese, "
                        "una scrittrice di non-fiction. Ogni testo ha la sua tipografia.",
                    ],
                },
            ],
            "deliverables_label": "Consegne",
            "deliverables_heading": "Sei <em>etichette</em>, sei tipografie.",
            "deliverables_intro":
                "La serie è stata venduta come cofanetto da sei bottiglie "
                "in edizione limitata (1200 set).",
            "deliverables": [
                ("01", "Sei etichette d'autore",
                 "Stampate in tipografia a Verona su carta Amatruda, "
                 "con doppia nobilitazione (debossed + lamina)."),
                ("02", "Cofanetto in legno",
                 "Disegnato con un falegname di Valpolicella, "
                 "numerato e firmato dalla cantina."),
                ("03", "Libretto dei testi",
                 "Raccolta dei sei testi originali in edizione italiana + "
                 "traduzione inglese, legata a filo."),
            ],
            "press_quote":
                "Un progetto che lega il vino alla letteratura senza forzare l'analogia. Coraggioso.",
            "press_source":     "Gambero Rosso — Gennaio 2024",
            "press_journalist": "Marco Sabellico",
            "next_label":       "Prossimo caso",
            "next_heading":     "Vai all'<em>archivio lavori</em> →",
            "cta_label":        "Packaging d'autore",
            "cta_heading":      "Apri il <em>dossier packaging</em> →",
        },
    ],
}

