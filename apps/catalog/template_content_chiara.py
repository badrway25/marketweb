"""Chiara — Portfolio Creativo (portfolio / editorial-designer-grid archetype) content.

Phase 2g3.4 — Portfolio live rollout (Session 34, 2026-04-13).

Editorial identity: independent Milan design studio led by Chiara Velluti,
art director. Disciplines: brand identity, editorial design, signage and
graphic systems for cultural institutions, publishers and small-luxury
maisons. The voice is sober, structural, AD-led, with a typographic
sensibility — references books, paper stock, grid systems. Photo
direction is studio work-in-progress (sketchbooks, prototypes, paste-ups,
press proofs), never glossy lifestyle.

Differentiation vs Pixel (10-gate D-054 — recorded here for reviewers):
 1. Hero image:        no big hero photo — typographic ledger drives the
                       hero; Pixel ships a fullbleed cinematic photo.
 2. First-2 imagery:   sketchbook + paste-up close-ups (designer-pool)
                       vs Pixel's moody hero + filmstrip stills.
 3. Silhouette:        hairline-rule nav + typographic-index hero +
                       project ledger; Pixel has dark fullbleed-cover.
 4. Section order:     hero → ledger → ribbon → capabilities → commissions
                       vs Pixel hero → filmstrip → bio → publications.
 5. Primary CTA:       "Richiedi il portfolio completo" (case-study request)
                       vs Pixel "Apri la serie" (series brief).
 6. Block rhythm:      very-airy editorial chapters
                       vs Pixel compact image-dense.
 7. Macro tone:        cream paper + ink + accent rule (editorial)
                       vs Pixel near-black + warm grey + accent pulse.
 8. Imagery direction: studio work-in-progress (designer-pool)
                       vs Pixel cinematic photostill (photographer-pool).
 9. Typography:        Syne (display) + Inter — designer's bookshelf voice
                       vs Pixel Archivo (geometric) + Inter — author voice.
10. Inner pages:       project ledger + design notes + capabilities
                       vs Pixel series index + exhibitions + bio.

Page kinds:
- home, about (kind: about), project_list, project_detail,
  process (kind: process), contact (kind: contact)
"""
from __future__ import annotations

from typing import Any


CHIARA_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Studio",      "kind": "home"},
        {"slug": "studio",     "label": "Chi siamo",   "kind": "about"},
        {"slug": "lavoro",     "label": "Lavoro",      "kind": "project_list"},
        {"slug": "processo",   "label": "Processo",    "kind": "process"},
        {"slug": "contatti",   "label": "Contatti",    "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial":   "C",
        "logo_word":      "Chiara Velluti Studio",
        "logo_short":     "CV",
        "tag":            "Direzione artistica · Milano",
        "phone":          "+39 02 8736 4408",
        "email":          "studio@chiaravelluti.it",
        "address":        "Via Tortona 27 · 20144 Milano",
        "hours_compact":  "Lun – Ven · 10:00 – 19:00 · su appuntamento",
        "license":        "P. IVA IT 09621460963 · REA MI-2092841",
        "footer_intro":
            "Studio indipendente di direzione artistica a Milano. "
            "Identità di marca, sistemi editoriali e segnaletica per "
            "istituzioni culturali, editori e maison di piccolo lusso. "
            "Fondato nel 2014.",
        "foot_studio":   "Lo studio",
        "foot_pages":    "Sezioni",
        "foot_contact":  "Contatti",
        "foot_clients":  "Hanno scelto lo studio",
        "clients_footer_rows": [
            "Triennale Milano",
            "Edizioni Adelphi",
            "Fondazione Prada (commissione 2022)",
            "Ateliers Velluti & Co.",
        ],
        # Studio coordinates strip — used in footer + ribbon
        "coordinates": [
            ("Studio",     "Via Tortona 27 · 20144 Milano"),
            ("Founder",    "Chiara Velluti, AD"),
            ("Equipe",     "5 designer · 1 stagista · 2 collaboratori"),
            ("Disciplines","Brand · Editorial · Sistemi grafici"),
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":   "Studio indipendente · 2014 — 2026",
        # Headline kept short (47 chars) per D-052 to avoid hero overflow
        "headline":  "Forme che durano, <em>una pagina</em> alla volta.",
        "intro":
            "Disegniamo identità di marca, libri e sistemi grafici per "
            "istituzioni culturali, editori e maison di piccolo lusso. "
            "Lo studio è guidato dall'art director e ogni progetto è "
            "seguito personalmente dall'apertura del fascicolo alla "
            "consegna delle linee guida.",
        "primary_cta":   "Richiedi il portfolio completo",
        "primary_href":  "contatti",
        "secondary_cta": "Visita lo studio",
        "secondary_href":"studio",

        # Hero ledger card footer label + count format (lifted from skin)
        "ledger_full_link_label":   "Tutto l'archivio",
        "ledger_count_prefix":      "→",
        "ledger_count_unit":        "progetti",

        # Project ledger preview — 6 indexed rows
        "ledger_label":   "Lavoro selezionato · 2022 — 2026",
        "ledger_heading": "Sei progetti, sei discipline",
        "ledger_intro":
            "Una selezione recente. L'archivio completo conta 47 progetti "
            "firmati dal 2014. Per la lista integrale è disponibile un "
            "PDF di consultazione su richiesta.",
        # Each row: (num, title, discipline, year, medium)
        "ledger_rows": [
            ("01", "Triennale Milano · catalogo 2025",
             "Editoria d'arte", "2025",
             "Volume 24 × 32 cm · 412 pagine · stampa offset"),
            ("02", "Adelphi · collana «Carta Bianca»",
             "Identità di collana", "2024",
             "Sistema tipografico + 12 copertine in serie"),
            ("03", "Fondazione Querini Stampalia · segnaletica",
             "Segnaletica & wayfinding", "2024",
             "Sistema bilingue · ottone inciso + stampa diretta"),
            ("04", "Maison Lambrate · rebrand",
             "Identità di marca", "2023",
             "Logotipo + sistema visivo + linee guida 96 pagine"),
            ("05", "Festival di Pordenone · 38ª edizione",
             "Identità di evento", "2023",
             "Marchio temporaneo + materiali stampa + segnaletica"),
            ("06", "Atelier Velluti & Co. · monografia",
             "Editoria di studio", "2022",
             "Volume 19 × 25 cm · 240 pagine · stampa fine art"),
        ],

        # Capabilities preview (full list on /processo)
        "capabilities_label":   "Discipline",
        "capabilities_heading": "Cinque competenze, una sola firma",
        "capabilities_intro":
            "Ogni progetto è seguito da un team multidisciplinare. "
            "Non scaliamo per dimensione del cliente — scaliamo "
            "per complessità del problema.",
        "capabilities": [
            ("Brand identity",
             "Identità complete per istituzioni e maison: dalla "
             "ricerca tipografica alle linee guida operative."),
            ("Editoria & libri",
             "Cataloghi d'arte, monografie d'autore, collane "
             "editoriali. Direzione tipografica e impaginato."),
            ("Sistemi & wayfinding",
             "Segnaletica, sistemi grafici per spazi espositivi, "
             "wayfinding bilingue e materiale didattico museale."),
            ("Direzione artistica",
             "Consulenza AD per uffici interni: revisione "
             "linee guida, audit visivi, mentorship al team grafico."),
        ],

        # Selected clients ribbon (text-only wordmarks)
        "clients_label":   "Hanno scelto lo studio",
        "clients": [
            "TRIENNALE MILANO",
            "ADELPHI EDIZIONI",
            "FONDAZIONE PRADA",
            "MUSEO POLDI PEZZOLI",
            "QUERINI STAMPALIA",
            "FESTIVAL PORDENONE",
            "MAISON LAMBRATE",
            "ATELIER VELLUTI & CO.",
        ],

        # Featured projects — visual grid below the typo hero. Lightbox-enabled,
        # 4 cards with project image, year, discipline. Reads as a designer's
        # opening reel without breaking the typographic editorial identity.
        "featured_works": {
            "label":   "Lavori in catalogo",
            "heading": "Quattro progetti, <em>quattro discipline.</em>",
            "intro":
                "Una selezione del 2024 — 2025 — sistemi tipografici, identità "
                "istituzionali, segnaletica museale, oggetti editoriali stampati. "
                "Cliccare per aprire il dossier completo.",
            "items": [
                {
                    "year":       "2025",
                    "discipline": "Catalogo · Editoria d'arte",
                    "title":      "Triennale Milano 2025",
                    "blurb":      "Direzione tipografica e impaginazione del catalogo principale dell'edizione.",
                    "image":      "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2024 — 2025",
                    "discipline": "Sistema tipografico · Editoriale",
                    "title":      "Collana «Carta Bianca» · Adelphi",
                    "blurb":      "Sistema editoriale per dodici titoli — copertine, tipografia, codice cromatico.",
                    "image":      "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2024",
                    "discipline": "Segnaletica · Identità museale",
                    "title":      "Querini Stampalia · Venezia",
                    "blurb":      "Segnaletica permanente delle sale + sistema di chiamata sale conferenze.",
                    "image":      "https://images.unsplash.com/photo-1564399579883-451a5d44ec08?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
                {
                    "year":       "2023",
                    "discipline": "Monografia · Editoria indipendente",
                    "title":      "Atelier Velluti · Lambrate",
                    "blurb":      "Monografia di studio — 240 pagine, sistema typografico custom, stampa Antiga.",
                    "image":      "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=1400&q=80&auto=format&fit=crop",
                    "href":       "lavoro",
                },
            ],
            "footer_link":  "Vedi tutti i progetti",
            "footer_href":  "lavoro",
        },

        # Press / recognitions — 3 honors
        "press_label":   "Riconoscimenti recenti",
        "press_heading": "Premi, mostre e pubblicazioni",
        "press": [
            {
                "year":  "2025",
                "honor": "ADI Design Index",
                "work":  "Catalogo Triennale Milano 2025",
                "note":  "Selezione editoria d'arte · giuria nazionale.",
            },
            {
                "year":  "2024",
                "honor": "European Design Awards · Bronze",
                "work":  "Collana «Carta Bianca» per Adelphi",
                "note":  "Categoria sistemi tipografici editoriali.",
            },
            {
                "year":  "2023",
                "honor": "Aiap Design Per · Mostra collettiva",
                "work":  "Monografia Atelier Velluti & Co.",
                "note":  "Esposta a Triennale per quattro mesi.",
            },
        ],

        # Selected commissions — what we accept this year
        "commissions_label":   "Commissioni 2026",
        "commissions_heading": "Cosa stiamo cercando questo anno",
        "commissions_intro":
            "Lo studio accetta otto-dieci progetti l'anno, scelti per "
            "complessità più che per dimensione del cliente. La scelta "
            "del lavoro è la disciplina più importante che esercitiamo.",
        "commissions": [
            ("Identità per istituzioni culturali",
             "Musei, fondazioni, festival. Preferiamo i mandati di "
             "rebrand strutturale ai semplici aggiornamenti."),
            ("Cataloghi d'arte e monografie",
             "Editori d'arte indipendenti, gallerie con programma "
             "editoriale, monografie d'autore."),
            ("Sistemi grafici per spazi",
             "Segnaletica museale, wayfinding bilingue, sistemi "
             "didattici per mostre temporanee."),
        ],

        # Final CTA band
        "cta_label":   "Una conversazione preliminare",
        "cta_heading": "Trenta minuti con l'AD, niente impegno",
        "cta_intro":
            "La prima call avviene direttamente con Chiara Velluti. "
            "Discutiamo il perimetro, la timeline e l'eventuale "
            "conflitto di calendario — prima di qualsiasi proposta.",
        "cta_primary":      "Scrivi allo studio",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Sfoglia il lavoro",
        "cta_secondary_href":"lavoro",
    },

    # ─── STUDIO (about) ─────────────────────────────────────────
    "studio": {
        "eyebrow":   "Lo studio · 2014 — 2026",
        "headline":  "Uno studio guidato dall'<em>art director</em>, dodici anni di lavoro.",
        "intro":
            "Chiara Velluti Studio nasce nel 2014 a Milano, in un primo "
            "spazio di trentaquattro metri quadrati a Lambrate. Oggi "
            "siamo cinque designer, due collaboratori esterni e una "
            "stagista in via Tortona. Continuiamo a scegliere uno per "
            "uno i progetti.",

        # Founder block (full bio)
        "founder_label":   "Direzione artistica",
        "founder_heading": "Chiara Velluti, fondatrice",
        "founder": {
            "name":  "Chiara Velluti",
            "role":  "Art director · Founder",
            "bio":
                "Diplomata Isia Urbino in progettazione grafica, "
                "tre anni a Studio Pentagram New York come senior "
                "designer (sotto Paula Scher), cinque anni a Studio "
                "Sonnoli a Rimini come associata. Apre lo studio "
                "Velluti nel 2014 a Milano. Insegna progettazione "
                "tipografica al Politecnico dal 2018, è membro Aiap "
                "dal 2010 e dirige la collana editoriale «Carta "
                "Bianca» per Adelphi dal 2024.",
            "credentials": [
                "Isia Urbino · Progettazione grafica '06",
                "Pentagram New York · senior '07—'10",
                "Studio Sonnoli Rimini · associata '10—'14",
                "Politecnico Milano · docente progettazione tipografica",
                "Aiap · membro ordinario dal 2010",
                "ADI · giurata Design Index 2024",
            ],
            "image": "https://images.unsplash.com/photo-1544717305-2782549b5136?w=1200&q=80&auto=format&fit=crop",
        },

        # Studio team (full team — 4 collaborators beyond founder)
        "team_label":   "Equipe di studio",
        "team_heading": "Cinque designer, due collaboratori esterni",
        "team_intro":
            "Lavoriamo in un open space unico — niente uffici separati. "
            "Ogni progetto ha un team dedicato di tre persone fisse, "
            "guidato dall'AD. I collaboratori esterni intervengono "
            "solo su tipografia originale e impaginato di lungo periodo.",
        "team": [
            {"name": "Marco Salvioli",
             "role": "Senior designer · editoria",
             "bio":
                "Cinque anni a Tassinari/Vetta a Trieste prima di "
                "raggiungere lo studio nel 2019. Coordina i progetti "
                "editoriali e le linee guida tipografiche."},
            {"name": "Anna Brambilla",
             "role": "Designer · identità di marca",
             "bio":
                "Naba Milano '17, due anni a Studio Mut Bolzano. "
                "Si occupa di rebrand di studio e maison di piccolo "
                "lusso, dalla ricerca al manuale operativo."},
            {"name": "Lorenzo Tagliabue",
             "role": "Designer · sistemi & wayfinding",
             "bio":
                "Politecnico Milano '19, tirocinio a Atelier Carvalho "
                "Bernau a Berlino. Cura i sistemi segnaletici e i "
                "materiali per spazi espositivi."},
            {"name": "Sara Pellegrini",
             "role": "Designer · digitale",
             "bio":
                "Iuav Venezia '20, due anni a Cantiere Creativo "
                "Firenze. Estende le identità ai sistemi digitali "
                "(siti, applicativi, materiali animati)."},
            {"name": "Filippo Vigorelli",
             "role": "Collaboratore · disegno tipografico",
             "bio":
                "Type designer indipendente, formato a Type@Cooper "
                "New York. Collabora ai caratteri custom dello studio "
                "dal 2017."},
            {"name": "Beatrice Fornaro",
             "role": "Stagista · 2026",
             "bio":
                "Ultimo anno Isia Urbino. Affianca la pratica "
                "editoriale e contribuisce all'archivio dei progetti "
                "passati."},
        ],

        # Studio principles — 4 design notes
        "principles_label":   "Principi di studio",
        "principles_heading": "Quattro regole <em>non negoziabili</em>",
        "principles_intro":
            "Sono le quattro regole che separano un progetto firmato "
            "Velluti da un'esecuzione standard di studio. Le trovate "
            "scritte nel manuale interno del 2018, mai aggiornato.",
        "principles": [
            ("01", "Una sola voce, dall'inizio alla fine",
             "L'AD entra in prima call e firma la consegna. Niente "
             "passaggi a junior dopo il pitch — la persona "
             "che incontrate in riunione di apertura è la stessa "
             "che firma le linee guida finali."),
            ("02", "La tipografia prima del marchio",
             "In ogni progetto la scelta dei caratteri precede il "
             "disegno del logo. Le identità che proponiamo nascono "
             "da una grammatica tipografica, non da un simbolo "
             "decorativo."),
            ("03", "Niente moodboard di Pinterest",
             "I riferimenti che proponiamo provengono dalla nostra "
             "biblioteca di studio, dagli archivi delle istituzioni "
             "con cui lavoriamo, e da visite dirette a mostre. "
             "Mai immagini scaricate."),
            ("04", "Le linee guida sono un libro",
             "Ogni identità chiude con un manuale operativo "
             "stampato — non un PDF, un volume di centoventi/duecento "
             "pagine. Resta nella biblioteca del cliente, non in "
             "una cartella server."),
        ],

        # Press band — full press list (extended from home)
        "press_label":   "Premi, mostre, pubblicazioni",
        "press_heading": "Selezione 2020 — 2026",
        "press_full": [
            ("2025", "ADI Design Index",
             "Selezione editoria d'arte", "Catalogo Triennale 2025"),
            ("2024", "European Design Awards · Bronze",
             "Sistemi tipografici editoriali", "Collana «Carta Bianca»"),
            ("2024", "Brand New (Under Consideration)",
             "Recensione critica", "Rebrand Maison Lambrate"),
            ("2023", "Aiap Design Per · Mostra collettiva",
             "Editoria d'autore", "Monografia Velluti & Co."),
            ("2023", "Type Directors Club New York · Honor",
             "Disegno tipografico", "Carattere custom Querini"),
            ("2022", "Eye Magazine n. 102",
             "Saggio illustrato di otto pagine", "Identità Velluti Studio"),
            ("2021", "ADI Compasso d'Oro · Menzione",
             "Categoria comunicazione visiva", "Sistema Triennale 2021"),
            ("2020", "Brno Biennial Czechia · Selezione",
             "Identità museali", "Festival Pordenone 36ª"),
        ],

        # Final CTA — visit the studio
        "cta_heading":      "Visita lo studio",
        "cta_intro":
            "Lo studio è in via Tortona 27, ingresso dal cortile "
            "interno. La biblioteca è aperta su appuntamento — "
            "scrivete due righe e fissiamo una mattina.",
        "cta_primary":      "Fissa una visita",
        "cta_primary_href": "contatti",
    },

    # ─── LAVORO (project_list) ──────────────────────────────────
    "lavoro": {
        "eyebrow":   "Archivio dei progetti · 2014 — 2026",
        "headline":  "Quarantasette progetti firmati, <em>sei discipline</em>.",
        "intro":
            "L'archivio completo dei progetti dello studio. La selezione "
            "qui mostrata copre i sei mandati più recenti per ciascuna "
            "disciplina. Per il PDF integrale del portfolio (96 pagine, "
            "tutti i progetti firmati dal 2014) scrivete a studio@chiaravelluti.it.",

        # Discipline filter pills
        "filter_label": "Discipline",
        "filters": [
            "Tutte",
            "Editoria d'arte",
            "Identità di marca",
            "Sistemi & wayfinding",
            "Identità di evento",
            "Direzione artistica",
        ],

        # Ledger row labels (lifted from skin for i18n)
        "row_discipline_label": "Disciplina",
        "row_duration_label":   "Durata",
        "row_year_label":       "Anno",

        # Index intro band on top of the ledger
        "ledger_label": "Indice cronologico",
        "ledger_intro":
            "Scorrere dall'alto verso il basso per il cronologico inverso. "
            "Cliccare una riga per aprire il dossier completo del progetto.",

        # CTA before footer
        "cta_label":   "Cercate qualcosa di specifico?",
        "cta_heading": "Su richiesta inviamo dossier per disciplina",
        "cta_intro":
            "Se valutate lo studio per un mandato specifico, indicateci "
            "la disciplina e vi inviamo entro 48 ore tre dossier "
            "rilevanti — formato A4, stampa per la presentazione interna.",
        "cta_primary":      "Scrivici",
        "cta_primary_href": "contatti",

        # Dossier (project_detail) labels — constants across all posts,
        # localized via the `lavoro` page_data block.
        "dossier_meta_discipline_label": "Disciplina",
        "dossier_meta_year_label":       "Anno",
        "dossier_meta_duration_label":   "Durata",
        "dossier_meta_team_label":       "Equipe",
        "dossier_summary_label":         "Sintesi del progetto",
        "dossier_deliverables_label":    "Deliverable consegnati",
        "dossier_deliverables_heading":  "Cosa abbiamo prodotto",
        "dossier_colophon_label":        "Colophon",
    },

    # ─── PROCESSO (process) ─────────────────────────────────────
    "processo": {
        "eyebrow":   "Come lavoriamo · metodo di studio",
        "headline":  "Cinque fasi, <em>un solo file</em> per progetto.",
        "intro":
            "Il metodo di studio è scritto, condiviso al cliente in "
            "prima call e seguito senza eccezioni. Ogni progetto ha "
            "un proprio fascicolo fisico — cartella verde con numero, "
            "etichetta tipografica, conservata in archivio per "
            "vent'anni minimo.",

        # Process step + capability labels (lifted from skin for i18n)
        "step_sequence_label":       "Sequenza",
        "step_index_prefix":         "Step",
        "step_index_separator":      "di",
        "capability_duration_label": "Durata indicativa",

        # 5-step process (richer than business)
        "process_label":   "Sequenza di studio",
        "process_heading": "Apertura, ricerca, proposta, costruzione, consegna",
        "process": [
            ("01", "Apertura del fascicolo",
             "Prima call con l'AD (45 minuti, gratuita). Si discute il "
             "perimetro, le aspettative del cliente, l'eventuale "
             "conflitto di calendario. Entro cinque giorni una proposta "
             "scritta di tre pagine: perimetro, deliverable, timeline, "
             "tariffario.",
             "Deliverable", "Proposta scritta · 3 pagine"),
            ("02", "Ricerca preliminare",
             "Quattro a sei settimane di ricerca: visita all'archivio "
             "del cliente, biblioteca di studio, riferimenti storici "
             "e contemporanei. Mai moodboard di Pinterest. Si chiude "
             "con un brief illustrato condiviso al cliente.",
             "Durata", "4 — 6 settimane"),
            ("03", "Proposta di direzione",
             "Una sola direzione viene presentata, non tre. La "
             "presentazione è dal vivo, in studio o presso il cliente, "
             "mai per email. Il cliente può accettare, chiedere "
             "revisioni circoscritte (massimo due cicli) o interrompere "
             "il mandato (clausola di uscita prevista in contratto).",
             "Durata", "2 — 3 settimane di disegno + presentazione"),
            ("04", "Costruzione del sistema",
             "La direzione approvata viene declinata in un sistema "
             "completo: tipografia, palette, griglia, marchi, materiali, "
             "applicazioni. Per identità complete: dieci a sedici "
             "settimane. Il team dedicato lavora a porte chiuse con "
             "due check intermedi mensili al cliente.",
             "Durata", "10 — 16 settimane secondo perimetro"),
            ("05", "Consegna e manuale stampato",
             "Ogni progetto chiude con un manuale operativo stampato — "
             "120 a 240 pagine, formato A4, stampa offset bianco e "
             "nero. Una copia al cliente, una nella biblioteca di studio. "
             "Sei mesi di assistenza inclusi sull'applicazione delle "
             "linee guida.",
             "Deliverable", "Manuale stampato + assistenza 6 mesi"),
        ],

        # Capabilities — full list (extended from home)
        "capabilities_label":   "Discipline complete",
        "capabilities_heading": "Cosa progettiamo",
        "capabilities_intro":
            "Le discipline che pratichiamo regolarmente. Non lavoriamo "
            "su pubblicità above-the-line, packaging FMCG, motion graphics "
            "di durata superiore ai 30 secondi, né su template "
            "ricolorabili.",
        "capabilities_full": [
            {
                "num": "01",
                "title": "Brand identity",
                "blurb":
                    "Identità complete per istituzioni culturali e maison "
                    "di piccolo lusso. Marchio + sistema tipografico + "
                    "palette + griglia + manuale operativo stampato.",
                "scope": [
                    "Naming e ricerca tipografica",
                    "Disegno del marchio e varianti",
                    "Sistema visivo + griglia",
                    "Manuale operativo (120 — 240 pp.)",
                ],
                "duration": "16 — 24 settimane per identità completa",
            },
            {
                "num": "02",
                "title": "Editoria d'arte",
                "blurb":
                    "Cataloghi d'arte, monografie d'autore, collane "
                    "editoriali. Direzione tipografica, impaginato, "
                    "scelta della carta, follow-up in tipografia.",
                "scope": [
                    "Direzione tipografica",
                    "Impaginato e griglia editoriale",
                    "Scelta della carta + ricerca tipografica",
                    "Follow-up in stampa (visita tipografia)",
                ],
                "duration": "12 — 32 settimane per volume singolo",
            },
            {
                "num": "03",
                "title": "Sistemi & wayfinding",
                "blurb":
                    "Segnaletica museale, sistemi grafici per spazi "
                    "espositivi, wayfinding bilingue, materiali "
                    "didattici per mostre temporanee.",
                "scope": [
                    "Audit dello spazio esistente",
                    "Sistema bilingue/trilingue",
                    "Disegno della segnaletica",
                    "Direzione di produzione (incisione/stampa)",
                ],
                "duration": "10 — 18 settimane per spazio museale",
            },
            {
                "num": "04",
                "title": "Identità di evento",
                "blurb":
                    "Marchi temporanei per festival, biennali, edizioni "
                    "limitate. Materiale stampa, segnaletica per la "
                    "sede, sistema digitale.",
                "scope": [
                    "Marchio temporaneo + variante per anno",
                    "Sistema stampa (locandine, brochure, biglietti)",
                    "Segnaletica per la sede",
                    "Sistema digitale (sito + materiali animati)",
                ],
                "duration": "8 — 14 settimane per edizione",
            },
            {
                "num": "05",
                "title": "Direzione artistica",
                "blurb":
                    "Consulenza AD per uffici interni: revisione "
                    "linee guida esistenti, audit visivi, mentorship "
                    "al team grafico interno, formazione tipografica.",
                "scope": [
                    "Audit visivo dell'esistente",
                    "Revisione delle linee guida",
                    "Mentorship al team grafico (1 giorno/mese)",
                    "Workshop tipografico (formazione)",
                ],
                "duration": "Mandato annuale, rinnovabile",
            },
        ],

        # Final CTA before footer
        "cta_heading":      "Quale disciplina fa al caso vostro?",
        "cta_intro":
            "Se il perimetro non è chiaro, scrivete due righe di "
            "contesto. Vi rispondiamo con la disciplina giusta entro "
            "48 ore — anche se non sarà lo studio Velluti a seguirvi.",
        "cta_primary":      "Scrivici",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI (contact) ─────────────────────────────────────
    "contatti": {
        "eyebrow":   "Una conversazione preliminare",
        "headline":  "Trenta minuti con l'AD, <em>niente impegno</em>.",
        "intro":
            "Il primo contatto avviene direttamente con Chiara Velluti, "
            "art director e fondatrice. Discutiamo il perimetro del "
            "progetto, la timeline e l'eventuale conflitto di calendario "
            "— prima di qualsiasi proposta scritta.",

        # Studio info side card
        "studio_label":          "Lo studio",
        "studio_address":        "Via Tortona 27 · 20144 Milano",
        "studio_area":           "Ingresso dal cortile interno · campanello «Velluti»",
        "studio_metro":          "MM2 Porta Genova · 4 minuti a piedi",
        "studio_hours":          "Lun – Ven · 10:00 – 19:00 · su appuntamento",
        # Studio card row labels (lifted from skin for i18n)
        "studio_address_label":  "Indirizzo",
        "studio_area_label":     "Ingresso",
        "studio_metro_label":    "Metro",
        "studio_hours_label":    "Orari",

        # Form fields — generic loop in chrome
        "form_label":   "Richiedi una prima call",
        "form_heading": "Compila il modulo",
        "form_intro":
            "Riceverà conferma entro 48 ore lavorative. Le call si "
            "tengono il martedì e il giovedì pomeriggio, a porte "
            "chiuse, con l'AD.",
        "form_fields": [
            {"name": "name",      "label": "Nome",          "type": "text",     "required": True,  "placeholder": "Es. Chiara",
             "helper": "Solo nome di battesimo, grazie."},
            {"name": "surname",   "label": "Cognome",       "type": "text",     "required": True,  "placeholder": "Es. Velluti",
             "helper": "Come compare nel biglietto da visita."},
            {"name": "organization", "label": "Organizzazione", "type": "text", "required": True,  "placeholder": "Es. Triennale Milano",
             "helper": "Istituzione, casa editrice o maison."},
            {"name": "role",      "label": "Ruolo",         "type": "text",     "required": True,  "placeholder": "Es. Direttrice editoriale",
             "helper": "Posizione di chi seguirà il progetto."},
            {"name": "email",     "label": "Email",         "type": "email",    "required": True,  "placeholder": "chiara.velluti@triennale.org",
             "helper": "Preferibilmente email istituzionale."},
            {"name": "phone",     "label": "Telefono",      "type": "tel",      "required": False, "placeholder": "+39 ...",
             "helper": "Linea diretta · solo se preferite essere richiamati."},
            {"name": "discipline", "label": "Disciplina di interesse", "type": "select", "required": True,
             "options": [
                 "Da definire in call",
                 "Brand identity",
                 "Editoria d'arte",
                 "Sistemi & wayfinding",
                 "Identità di evento",
                 "Direzione artistica",
             ],
             "helper": "Scegliere «da definire» se il perimetro tocca più discipline."},
            {"name": "horizon",   "label": "Orizzonte temporale", "type": "select", "required": True,
             "options": [
                 "Avvio entro un mese",
                 "Avvio entro tre mesi",
                 "Avvio entro sei mesi",
                 "Esplorativo · nessuna urgenza",
             ],
             "helper": "Aiuta a calendare la prima call con l'AD."},
            {"name": "brief",     "label": "Breve descrizione del progetto", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Massimo 800 caratteri. Niente nomi di controparti — verranno discussi "
                            "solo dopo NDA reciproca, se necessario.",
             "helper": "Quanto basta a capire se il progetto è di nostra competenza."},
        ],

        "form_sections": [
            {"num": "01", "title": "Referente",
             "meta": "La persona che seguirà il progetto da lato cliente.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Organizzazione",
             "meta": "Per il conflict-check preliminare con altri progetti in corso.",
             "fields": ["organization", "role"]},
            {"num": "03", "title": "Perimetro del progetto",
             "meta": "Una descrizione sintetica — gli allegati arrivano in seconda call, dopo NDA.",
             "fields": ["discipline", "horizon", "brief"]},
            {"num": "04", "title": "Allegati (facoltativi)",
             "meta": "Brief interno, dossier istituzionale, ricerca preliminare. Possono anticipare la prima call.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "brief_allegato",
            "label":    "Documenti preliminari",
            "helper":   "Brief interno, dossier istituzionale, immagini di riferimento. "
                        "PDF / DOCX / JPG · max 20 MB complessivi.",
            "accept":   ".pdf,.docx,.jpg,.jpeg,.png",
            "multiple": True,
            "primary":  "Trascina qui i documenti o",
            "link":     "sfoglia dall'archivio",
            "meta":     "PDF / DOCX / JPG · max 20 MB",
        },

        "form_submit_label": "Invia richiesta",
        "form_submit_note":
            "Conferma direttamente dall'AD entro 48 ore lavorative. "
            "Nessun account manager esterno, nessuna automazione di lead.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi del "
            "Regolamento UE 679/2016. Le richieste sono lette e "
            "archiviate solo dall'art director — nessun terzo coinvolto.",

        # Channels strip
        "channels_label": "Canali diretti",
        "channels": [
            ("Email studio",       "studio@chiaravelluti.it",     "Risposta entro 48 ore lavorative"),
            ("Centralino",         "+39 02 8736 4408",            "Lun – Ven · 10:00 – 19:00"),
            ("Visita allo studio", "Via Tortona 27 · Milano",     "Su appuntamento, mai a sorpresa"),
        ],

        "footnote":
            "Lo studio non risponde a richieste anonime e non rilascia "
            "preventivi via email senza una prima call. Le tariffe e le "
            "condizioni economiche sono presentate in proposta scritta, "
            "mai per messaggio.",
    },

    # ─── POSTS — drives /lavoro/<slug>/ project_detail ──────────
    "posts": [
        {
            "slug":        "triennale-milano-catalogo-2025",
            "title":       "Triennale Milano · catalogo 2025",
            "category":    "Editoria d'arte",
            "year":        "2025",
            "duration":    "32 settimane",
            "client_code": "Triennale Milano · catalogo della 24ª edizione · 412 pagine offset",
            "lead":
                "Direzione tipografica e impaginato del catalogo "
                "ufficiale della 24ª Triennale di Milano. Volume "
                "412 pagine, 24 × 32 cm, stampa offset in cinque colori "
                "su carta uncoated 130 g/m² Fedrigoni Arena.",
            "summary": [
                "Direzione tipografica e impaginato",
                "Sistema di griglia variabile per 87 contributi",
                "Disegno custom delle iniziali capolettera",
                "Follow-up in tipografia · 4 visite · 12 giorni",
            ],
            "discipline":  "Editoria d'arte",
            "team":        "AD + 2 senior · 32 settimane",
            "deliverables":[
                "Volume 412 pp. · 24 × 32 cm · stampa offset",
                "Sistema di griglia variabile per saggi e schede",
                "Carattere custom Triennale Display (12 glifi capolettera)",
                "Manuale di redazione interno · 48 pp.",
            ],
            "credits": [
                ("Cliente",          "Triennale Milano"),
                ("Direzione editoriale","Maria Sebregondi"),
                ("Stampa",           "Grafiche Antiga · Treviso"),
                ("Carta",            "Fedrigoni Arena Natural Smooth 130 g/m²"),
                ("Legatura",         "Brossura cucita filo refe · cartoncino 350 g/m²"),
                ("Tiratura",         "3.200 copie · seconda ristampa giugno 2025"),
            ],
            "sections": [
                {
                    "label": "Il progetto",
                    "heading": "Quattrocentododici pagine, ottantasette autori",
                    "body":
                        "Il catalogo della 24ª Triennale documenta una "
                        "mostra di mille metri quadrati su otto sale, "
                        "con ottantasette contributi fra saggi "
                        "critici, schede d'opera e apparati documentali. "
                        "Il problema progettuale era costruire un sistema "
                        "di griglia capace di accogliere testi di lunghezza "
                        "molto diversa (da 200 a 12.000 parole) "
                        "preservando una lettura editoriale unitaria.",
                },
                {
                    "label": "La direzione tipografica",
                    "heading": "Tre famiglie, una sola voce",
                    "body":
                        "Abbiamo costruito il sistema su tre famiglie "
                        "tipografiche complementari — un transitional "
                        "serif (Lyon Text) per i corpi testo, un grottesco "
                        "geometrico (GT Walsheim) per i titoli e un "
                        "monospaziato (JetBrains Mono) per gli apparati "
                        "documentali. Le tre famiglie convivono su una "
                        "griglia di nove colonne capace di articolarsi "
                        "in formati diversi senza spezzare la riconoscibilità.",
                },
                {
                    "label": "L'esecuzione",
                    "heading": "Trentadue settimane, quattro visite in stampa",
                    "body":
                        "Il volume è stato impaginato in trentadue settimane "
                        "da un team di tre designer dello studio, con "
                        "supervisione settimanale dell'AD. Quattro visite "
                        "in tipografia a Treviso fra luglio e settembre 2025 "
                        "hanno permesso di calibrare la stampa direttamente "
                        "su macchina — la copertina è stata rifatta due volte "
                        "per arrivare al nero pieno desiderato senza riflessi.",
                },
            ],
            "next_label": "Mandato successivo",
        },
        {
            "slug":        "adelphi-collana-carta-bianca",
            "title":       "Adelphi · collana «Carta Bianca»",
            "category":    "Identità di collana",
            "year":        "2024",
            "duration":    "44 settimane",
            "client_code": "Adelphi Edizioni · collana editoriale · 12 titoli all'anno",
            "lead":
                "Sistema visivo e copertine di una nuova collana di "
                "saggistica di filosofia contemporanea per Adelphi. "
                "Dodici titoli all'anno, formato 14 × 22 cm, brossura "
                "cucita su carta uncoated.",
            "summary": [
                "Direzione di collana + sistema tipografico",
                "12 copertine in serie · disegno custom",
                "Sistema di colore per anno editoriale",
                "Manuale di redazione tipografica",
            ],
            "discipline":  "Identità di collana",
            "team":        "AD + senior editoria · 44 settimane",
            "deliverables":[
                "Sistema visivo della collana · 36 pagine",
                "12 copertine in serie · disegno per titolo",
                "Carattere custom Adelphi Sans (per la collana)",
                "Manuale di redazione tipografica · 64 pp.",
            ],
            "credits": [
                ("Cliente",          "Adelphi Edizioni"),
                ("Direttore di collana","Roberto Calasso (postumo) · Aldo Schiavone"),
                ("Carta",            "Munken Pure Smooth 100 g/m²"),
                ("Stampa",           "Tipografia Mariani · Bergamo"),
                ("Legatura",         "Brossura cucita filo refe"),
                ("Tiratura",         "2.000 — 4.500 copie per titolo"),
            ],
            "sections": [
                {
                    "label": "Il progetto",
                    "heading": "Una nuova collana per Adelphi",
                    "body":
                        "Adelphi cerca un sistema visivo per «Carta Bianca», "
                        "una collana di saggistica filosofica destinata "
                        "a contenere voci giovani della filosofia europea "
                        "contemporanea. Dodici titoli all'anno, profilo "
                        "editoriale dichiaratamente sperimentale, "
                        "ma il marchio Adelphi va onorato.",
                },
                {
                    "label": "L'idea",
                    "heading": "Una sola architettura, dodici declinazioni",
                    "body":
                        "Il sistema è costruito su un'unica architettura "
                        "tipografica — il titolo lavorato in carattere "
                        "custom (Adelphi Sans, disegnato in collaborazione "
                        "con Filippo Vigorelli), composto a tutta pagina "
                        "su sfondo monocromo. Ogni anno editoriale "
                        "introduce una palette di sei colori, ogni titolo "
                        "viene stampato in due colori della palette "
                        "annuale. La riconoscibilità nasce dal sistema, "
                        "non dalla decorazione.",
                },
                {
                    "label": "L'esecuzione",
                    "heading": "Quarantaquattro settimane, dodici copertine",
                    "body":
                        "Il sistema è stato consegnato in luglio 2024, "
                        "le prime quattro copertine in settembre, le "
                        "altre otto a cadenza trimestrale fino a luglio "
                        "2025. La direzione editoriale di Aldo Schiavone "
                        "approva personalmente ogni copertina prima della "
                        "stampa. Lo studio ha curato anche la formazione "
                        "della redazione interna sull'uso del manuale.",
                },
            ],
            "next_label": "Progetto successivo",
        },
        {
            "slug":        "querini-stampalia-segnaletica",
            "title":       "Fondazione Querini Stampalia · segnaletica",
            "category":    "Segnaletica & wayfinding",
            "year":        "2024",
            "duration":    "26 settimane",
            "client_code": "Fondazione Querini Stampalia · sistema bilingue ITA / ENG",
            "lead":
                "Sistema segnaletico bilingue per la Fondazione Querini "
                "Stampalia di Venezia. Tre piani, museo + biblioteca + "
                "spazio Carlo Scarpa. Ottone inciso e stampa diretta "
                "su pannelli sostituibili.",
            "summary": [
                "Audit dello spazio esistente · 2 settimane",
                "Sistema bilingue ITA / ENG · grammatica unificata",
                "Disegno carattere custom Querini Sans (96 glifi)",
                "Direzione di produzione · ottone inciso + stampa diretta",
            ],
            "discipline":  "Sistemi & wayfinding",
            "team":        "AD + senior wayfinding · 26 settimane",
            "deliverables":[
                "Sistema segnaletico completo · 142 elementi",
                "Carattere custom Querini Sans · 96 glifi · 3 pesi",
                "Manuale operativo · 88 pagine",
                "Direzione di produzione fino al collaudo",
            ],
            "credits": [
                ("Cliente",          "Fondazione Querini Stampalia, Venezia"),
                ("Direzione",        "Marigusta Lazzari, direttrice"),
                ("Architettura",     "Studio Carlo Scarpa (1961—63 · originale)"),
                ("Produzione ottone","Bottega Pasinetti · Murano"),
                ("Stampa diretta",   "Tipografia Adriatica · Mestre"),
                ("Collaudo",         "Settembre 2024 · 142 elementi installati"),
            ],
            "sections": [
                {
                    "label": "Il problema",
                    "heading": "Una segnaletica nata per addizioni successive",
                    "body":
                        "La segnaletica della Fondazione si era stratificata "
                        "in cinque cicli successivi (dagli anni Sessanta a "
                        "una revisione del 2009), con materiali, caratteri "
                        "e logiche di posizionamento diversi. Il risultato "
                        "era illeggibile, ma il problema vero era "
                        "rispettare l'architettura di Carlo Scarpa al "
                        "piano terra — uno spazio che non tollera "
                        "sovraimposizioni grafiche pesanti.",
                },
                {
                    "label": "L'approccio",
                    "heading": "Una grammatica, due materiali",
                    "body":
                        "Abbiamo costruito una grammatica unificata in due "
                        "materiali: ottone inciso a bagno (per la "
                        "segnaletica permanente, in dialogo con "
                        "l'ottone Scarpa al piano terra) e stampa "
                        "diretta su pannelli alluminio sostituibili "
                        "(per la segnaletica di mostra, sostituibile "
                        "ad ogni allestimento). Il carattere custom "
                        "Querini Sans riprende le proporzioni delle "
                        "lapidi epigrafiche venete del Cinquecento.",
                },
                {
                    "label": "Il risultato",
                    "heading": "Centoquarantadue elementi, zero sovraimposizioni",
                    "body":
                        "Il sistema è stato installato in tre cantieri "
                        "successivi tra giugno e settembre 2024, con "
                        "collaudo congiunto con la Soprintendenza per "
                        "il piano Scarpa. Le incisioni in ottone sono "
                        "state realizzate dalla bottega Pasinetti a "
                        "Murano con tecnica tradizionale — quindici "
                        "settimane di lavorazione, tutte verificate "
                        "in situ dallo studio.",
                },
            ],
            "next_label": "Progetto successivo",
        },
    ],
}
