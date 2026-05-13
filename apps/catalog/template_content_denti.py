"""Denti+Co — Studio Dentistico · Italian content tree.

Wave 1 Pass-1 (T45 · 2026-05-11). Third template on the `specialist`
archetype after Cardio + Dermatologia. Zero new HTML files: reuses
`templates/live_templates/medical/specialist/` skin verbatim.

Differentiation against Cardio (cardiology · #9c2a2a red accent · Roma
Parioli · "una cardiologia su misura") and Derm (dermatology · #3d5437
forest-green · Roma Veneto · "la pelle è una carta d'identità"):

- Brand:        Denti+Co · Studio Dentistico Associato (Milan, Brera-adjacent)
- Voice anchor: "igiene" (clinical hygiene as repeated noun-em italic)
- Palette:      #0F2D40 deep clinical blue + #F7F3EE cream paper + #2BC4A4
                fresh-mint accent (NOT red NOT green — third polarity)
- Typography:   DM Serif Display + Inter (Cormorant=Cardio · Bodoni=Derm)
- Hero variant: editorial-magazine (portrait-driven · Cardio defaults to
                split-consultive · Derm has no portrait variant)
- Lead doctor:  Dr.ssa Chiara Vespa (female direzione clinica — gender
                diversity vs Cardio's male Marani)
- Visit verb:   "Prenota igiene" (booking-widget verb · Cardio + Derm both
                use "Richiedi visita privata" private-request)
- Imagery:      dental operatory + patient-forward portraits + zero close-up
                bocche-aperte (T44 §6.1 binding · imagery pool TEMPORARILY
                reuses `medical-cardiology` until the dedicated dental pack
                lands as T45b sub-pass — see TODO in `preview_imagery.py`)

IT-only at T45 Pass-1 build per D-102 cadence (workflow A.5 phase).
EN/FR/ES/AR locale trees land as T46 workflow C multilingual rollout.
Tier stays `draft` until that multilingual pass completes and the user
runs the public-flip handshake. Staff preview reachable via `?preview=1`.
"""
from __future__ import annotations

from typing import Any


# Imagery URLs — T46 Wave 1 Pass-2 (2026-05-11) wires verified Pexels
# URLs from the X.3 imagery curator output at
# `docs/content-factory/imagery/packs/dental.md`. All URLs licensed
# under Pexels License (CC0-compatible, commercial use OK). Replaces
# the T45 cardio-pool placeholder.
_CHIEF_PORTRAIT = (
    # Dental professional demonstrating oral care — Cedric Fauntleroy
    # portrait 5389×8083 · matches Dr.ssa Vespa "direttore sanitario"
    # role visually (hands-on, instructive frame)
    "https://images.pexels.com/photos/4269363/pexels-photo-4269363.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_LEAD_IMAGE = (
    # Bright modern dental office . MM Dental . 4000×2670 · used as
    # blog_list lead_image + post cover_image
    "https://images.pexels.com/photos/9062525/pexels-photo-9062525.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)


DENTI_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Studio",           "kind": "home"},
        {"slug": "studio",          "label": "Lo Studio",        "kind": "about"},
        {"slug": "visite",          "label": "Trattamenti",      "kind": "services"},
        {"slug": "medici",          "label": "Dentisti",         "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Pubblicazioni",    "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contatti",         "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Prenota igiene",   "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "D",
        "logo_word":    "Denti+Co",
        "tag":          "Studio dentistico associato · Milano Brera",
        "phone":        "+39 02 7770 4488",
        "email":        "studio@denticostudio.it",
        "address":      "Via Manzoni 18 · 20121 Milano",
        "hours_compact": "Lun – Ven · 8:30 – 19:30",
        "hours_footer_rows": [
            "Sabato · 9:00 – 13:00",
            "Domenica · chiuso",
        ],
        "license":      "Iscrizione OMCeO Milano 03 / 18742 · Direttore sanitario Dr.ssa C. Vespa",
        "footer_intro":
            "Studio dentistico associato di odontoiatria conservativa, igiene "
            "professionale e implantologia. Quattro professionisti, una sola "
            "cartella per il paziente.",
    },

    "home": {
        # Hero — editorial-magazine variant: portrait-driven, different
        # silhouette from Cardio's default split-consultive.
        "hero_variant": "editorial-magazine",
        "eyebrow":  "Odontoiatria · Milano Brera",
        "headline": "L'<em>igiene</em> non è un dettaglio. È il primo capitolo.",
        "intro":
            "Igiene professionale, conservativa, implantologia e ortodonzia "
            "trasparente. Quattro dentisti associati, una sola cartella, "
            "controlli semestrali compresi nel piano annuale.",
        "primary_cta":   "Prenota igiene",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "Lo studio",
        "secondary_href":"studio",

        # Three-fact band (Cardio uses 3 numbers · we use 3 dental-coded)
        "facts": [
            ("12", "anni di studio associato"),
            ("3.400", "igieni & controlli / anno"),
            ("4", "dentisti specialisti in sede"),
        ],

        # Manifesto with drop-cap (specialist archetype signature)
        "manifesto_drop_cap": "L",
        "manifesto":
            "a salute orale non si cura due volte all'anno: si sostiene tutti "
            "i giorni. Per questo Denti+Co lavora a partire dall'igiene — "
            "professionale, ripetibile, misurabile — e costruisce intorno ad "
            "essa la conservativa, l'implantologia, l'ortodonzia. Quattro "
            "dentisti specialisti, una sola cartella clinica condivisa, una "
            "sola firma sul piano di cura. Niente upselling, niente cure "
            "frammentate: l'igiene è il primo capitolo e l'unico vero gate.",

        # Hero right sidebar (when hero_variant is split-consultive only —
        # but we kept the pulse data so the editorial-magazine pulse rail
        # also renders.)
        "hero_sidebar_top_label": "Direzione clinica",
        "hero_sidebar_quote":
            "«L'igiene professionale ben fatta evita il 70 % delle cure "
            "invasive. Per noi è clinica seria, non un servizio cosmetico.»",
        "hero_sidebar_author": "— Dr.ssa Chiara Vespa · Direttore sanitario",
        "hero_sidebar_pulse": [
            ("Studio",      "Milano · Brera"),
            ("Da",          "2013"),
            ("Riferimento", "Odontoiatria associata"),
        ],

        # Anchor subnav (helps a dense home read like a magazine)
        "anchor_nav": [
            ("metodo",        "Metodo"),
            ("trattamenti",   "Trattamenti"),
            ("percorso",      "Percorso paziente"),
            ("medico",        "Direzione clinica"),
            ("studio",        "Sede & contatti"),
        ],

        # Signature treatments (numbered 01-04 · the dental version of
        # Cardio's signature_visits — four core dental categories)
        "signature_visits_label":   "Trattamenti & percorsi",
        "signature_visits_heading": "Quattro percorsi clinici, <em>una sola cartella.</em>",
        "signature_visits_intro":
            "Le quattro famiglie di intervento più richieste. "
            "L'elenco completo è nella pagina Trattamenti.",
        "signature_visits": [
            ("01", "Igiene professionale semestrale",
             "Detartrasi sopra e sottogengivale, air-polishing al "
             "bicarbonato di sodio, indice di sanguinamento e mappatura "
             "PSR. Inclusa nei piani annuali di mantenimento."),
            ("02", "Odontoiatria conservativa",
             "Otturazioni in composito stratificato, ricostruzioni "
             "estetiche, devitalizzazioni con localizzatore apicale. "
             "Diga di gomma obbligatoria su ogni intervento conservativo."),
            ("03", "Implantologia & rigenerativa",
             "Impianti singoli e riabilitazioni complete a carico "
             "immediato. Pianificazione computer-assistita e dima "
             "chirurgica stampata in 3D in laboratorio interno."),
            ("04", "Ortodonzia trasparente",
             "Allineatori invisibili Invisalign e SmileLab per adulti, "
             "ortodonzia intercettiva bambini 8-12 anni con apparecchi "
             "removibili. Check-in mensile incluso."),
        ],

        # Trattamenti tabs section (the four dental categories with
        # detailed treatment lists — uses the trattamenti_tabs DNA hook
        # the specialist skin already supports, see home.html L954+).
        "trattamenti_tabs": {
            "label":   "Listino trattamenti",
            "heading": "Cosa facciamo, con <em>quale criterio.</em>",
            "intro":
                "Quattro categorie cliniche, ciascuna con un protocollo "
                "scritto e un costo dichiarato. Nessun preventivo "
                "personalizzato per le voci di routine — solo per piani "
                "di cura strutturati.",
            "tabs": [
                {
                    "id":      "igiene",
                    "label":   "Igiene",
                    "eyebrow": "Igiene professionale",
                    "heading": "Quarantacinque minuti, non venti.",
                    "body":
                        "L'igiene non è un appuntamento di routine: è una "
                        "visita clinica di quarantacinque minuti con "
                        "charting parodontale, indice di sanguinamento, "
                        "air-polishing al bicarbonato e foto di controllo.",
                    "items": [
                        ("Igiene professionale singola", "45 min · € 95"),
                        ("Piano annuale (2 igieni + 1 controllo)", "annuale · € 220"),
                        ("Air-polishing al bicarbonato", "incluso · gratis"),
                        ("Sigillatura solchi (per dente)", "10 min · € 30"),
                    ],
                    "cta_label": "Tutti i piani di igiene →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "conservativa",
                    "label":   "Conservativa",
                    "eyebrow": "Odontoiatria conservativa",
                    "heading": "Composito stratificato, sempre sotto diga.",
                    "body":
                        "Otturazioni in composito fotopolimerizzato, "
                        "ricostruzioni estetiche, devitalizzazioni con "
                        "localizzatore apicale. Diga di gomma obbligatoria "
                        "su ogni intervento conservativo. Nessuna otturazione "
                        "in amalgama dal 2013.",
                    "items": [
                        ("Otturazione singola (1 superficie)", "45 min · € 140"),
                        ("Otturazione composta (2-3 superfici)", "60 min · € 220"),
                        ("Devitalizzazione mono-radicolare", "75 min · € 280"),
                        ("Devitalizzazione pluri-radicolare", "120 min · € 420"),
                    ],
                    "cta_label": "Listino conservativa completo →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "implantologia",
                    "label":   "Implantologia",
                    "eyebrow": "Implantologia & rigenerativa",
                    "heading": "Impianti italiani, garanzia a vita sul fixture.",
                    "body":
                        "Impianti Sweden+Martina di provenienza italiana, "
                        "pianificazione computer-assistita con TAC cone-beam, "
                        "dima chirurgica stampata in 3D nel laboratorio "
                        "interno. Carico immediato solo in casi selezionati "
                        "su valutazione clinica.",
                    "items": [
                        ("Impianto singolo (fixture + corona zirconia)", "intervento · € 1.850"),
                        ("Mini rialzo seno mascellare", "intervento · € 950"),
                        ("Rigenerativa ossea (zona singola)", "intervento · € 480"),
                        ("Riabilitazione fissa su 4 impianti", "piano · su preventivo"),
                    ],
                    "cta_label": "Percorsi implantologici →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "ortodonzia",
                    "label":   "Ortodonzia",
                    "eyebrow": "Ortodonzia trasparente & intercettiva",
                    "heading": "Allineatori per adulti, intercettiva per i bambini.",
                    "body":
                        "Allineatori invisibili Invisalign e SmileLab con "
                        "scansione intraorale iTero e piano simulato 3D "
                        "prima di iniziare. Ortodonzia intercettiva 8-12 "
                        "anni con apparecchi removibili. Check-in mensile "
                        "incluso nel piano.",
                    "items": [
                        ("Allineatori Invisalign – piano completo", "12-18 mesi · € 3.200"),
                        ("Allineatori SmileLab – piano completo", "10-14 mesi · € 2.400"),
                        ("Ortodonzia intercettiva bambini", "12-24 mesi · € 1.600"),
                        ("Mantenitore notturno post-trattamento", "permanente · € 220"),
                    ],
                    "cta_label": "Protocolli ortodontici →",
                    "cta_href":  "visite",
                },
            ],
        },

        "chief_label":   "Direzione clinica",
        "chief_heading": "Una sola firma <em>per ogni cartella.</em>",
        "chief": {
            "name":  "Dr.ssa Chiara Vespa",
            "role":  "Direttore sanitario · Odontoiatria conservativa & endodonzia",
            "bio":
                "Specialista in odontoiatria conservativa formatasi "
                "all'Università degli Studi di Milano e perfezionata "
                "alla Loma Linda University in California. Membro "
                "della SIE (Società Italiana di Endodonzia) e relatrice "
                "ai corsi annuali della Scuola Lombarda di Odontoiatria. "
                "Direttore sanitario dello studio dal 2013.",
            "portrait": _CHIEF_PORTRAIT,
        },

        # Patient journey — five steps in dental key (Cardio uses
        # arrival → anamnesi → ECG → diagnostica → piano scritto; we
        # use arrival → check-in → cartella+foto → trattamento → follow-up)
        "percorso": {
            "label":   "Percorso paziente",
            "heading": "Cosa aspettarsi dalla <em>prima visita.</em>",
            "intro":
                "La prima visita allo studio è dedicata a costruire la "
                "cartella clinica: foto, indici, scansione e piano di "
                "cura scritto. Mai trattamento alla prima seduta — "
                "tranne urgenze documentate.",
            "steps": [
                {
                    "num": "01",
                    "icon": "clipboard",
                    "title": "Check-in & anamnesi",
                    "desc": "Segreteria, scheda anamnestica con storia "
                            "medica e dentale, eventuali radiografie "
                            "pregresse o panoramica recente.",
                    "duration": "10 min",
                },
                {
                    "num": "02",
                    "icon": "book",
                    "title": "Esame clinico completo",
                    "desc": "Charting parodontale, indice di placca, "
                            "indice di sanguinamento, esame obiettivo "
                            "dei tessuti molli e delle mucose orali.",
                    "duration": "20 min",
                },
                {
                    "num": "03",
                    "icon": "heart",
                    "title": "Fotografia & scansione",
                    "desc": "Set fotografico standardizzato (8 scatti "
                            "intraorali + 4 extraorali), scansione "
                            "intraorale iTero per l'archivio digitale.",
                    "duration": "15 min",
                },
                {
                    "num": "04",
                    "icon": "chart",
                    "title": "Piano di cura scritto",
                    "desc": "Discussione in poltrona del piano clinico "
                            "con preventivo dettagliato voce per voce, "
                            "consegna anche via PDF.",
                    "duration": "15 min",
                },
                {
                    "num": "05",
                    "icon": "document",
                    "title": "Programmazione & follow-up",
                    "desc": "Calendario degli appuntamenti, eventuale "
                            "richiamo per igiene di mantenimento, "
                            "canale diretto WhatsApp per le urgenze.",
                    "duration": "5 min",
                },
            ],
        },

        # Press strip (dental-coded outlets · NOT cardiology titles)
        "press": ["Il Dentista Moderno", "Dental Tribune", "Bocca & Salute",
                  "Corriere Salute", "Vanity Fair Italia"],
        "press_label": "Pubblicato su",

        # FAQ (dental-specific questions, not cardio)
        "faq": {
            "label": "Domande frequenti",
            "heading": "Le domande che <em>ci rivolgete più spesso.</em>",
            "items": [
                ("Ogni quanto serve una seduta di igiene?",
                 "Per i pazienti senza patologia parodontale conclamata "
                 "la cadenza è semestrale. Per chi ha gengivite, "
                 "parodontite o porta apparecchi ortodontici la cadenza "
                 "scende a tre o quattro mesi. Il piano è personalizzato "
                 "dopo la prima visita."),
                ("Le otturazioni in composito durano davvero?",
                 "Sì, se la cavità è ricostruita sotto diga di gomma con "
                 "composito stratificato e luce LED qualificata. Le "
                 "nostre otturazioni hanno una sopravvivenza media di "
                 "dieci anni con controlli regolari. Non utilizziamo "
                 "amalgama dal 2013."),
                ("Quanto costa davvero un impianto?",
                 "L'impianto singolo (fixture in titanio Sweden+Martina "
                 "+ corona in zirconia) è € 1.850, IVA inclusa. Sono "
                 "esclusi gli eventuali interventi rigenerativi "
                 "preliminari (rialzo seno, GBR) che vengono preventivati "
                 "solo dopo TAC cone-beam."),
                ("L'ortodonzia trasparente funziona davvero per gli adulti?",
                 "Per il novanta per cento dei casi clinici negli adulti "
                 "gli allineatori trasparenti (Invisalign o SmileLab) "
                 "sono efficaci come l'apparecchio fisso tradizionale. "
                 "I casi che richiedono ancora apparecchio fisso sono "
                 "i rotazioni gravi dei premolari e le estrusioni "
                 "marcate, e li discutiamo apertamente in piano."),
                ("Posso portare i miei figli dallo stesso studio?",
                 "Sì. La Dr.ssa Liccardi si occupa di ortodonzia "
                 "intercettiva 8-12 anni con apparecchi removibili. "
                 "L'igiene pediatrica è inclusa per i figli dei pazienti "
                 "con piano annuale attivo."),
            ],
        },

        # Bottom CTA band
        "cta_heading":
            "Ogni piano di cura è <em>scritto, dichiarato, condiviso.</em>",
        "cta_primary_label":   "Prenota igiene",
        "cta_secondary_label": "Contatti dello studio",

        # Sede / Location — Milan Brera, different from Cardio Roma Parioli
        # and Derm Roma Veneto
        "location": {
            "label":   "Sede dello studio",
            "heading": "Via Manzoni 18, <em>Milano.</em>",
            "intro":
                "Lo studio occupa il piano nobile di un palazzo storico "
                "in zona Brera, a centoventi metri da Montenapoleone. "
                "Quattro ambulatori, sala radiologica TAC cone-beam, "
                "laboratorio ortodontico interno.",
            "map_image": "",
            "map_fallback_image":
                # Bright clean modern dental clinic room — Daniel Frank
                # 3888×2592 · used as map-fallback when Mapbox tile fails
                "https://images.pexels.com/photos/305567/pexels-photo-305567.jpeg"
                "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
            "details": [
                ("Indirizzo",
                 "Via Manzoni 18\n20121 Milano"),
                ("Metropolitana",
                 "M3 Montenapoleone\n3 minuti a piedi"),
                ("Parcheggio",
                 "Garage convenzionato\nin Via Bigli, 50 metri"),
                ("Accessibilità",
                 "Ingresso accessibile con ascensore\nfino al piano nobile"),
            ],
            "hours_short": [
                ("Lun – Ven", "8:30 – 19:30"),
                ("Sabato",    "9:00 – 13:00"),
                ("Domenica",  "Chiuso"),
            ],
            "cta_label": "Ottieni indicazioni stradali",
            "cta_href":  "contatti",
        },
    },

    # ─── STUDIO (about) — full content, all keys the specialist
    # about.html requires (history, method_*, values_*, cta_*).
    "studio": {
        "eyebrow":   "Lo studio · Milano Brera",
        "headline":  "Quattro dentisti, <em>una cartella sola.</em>",
        "intro":
            "Denti+Co è uno studio associato fondato nel 2013 da quattro "
            "professionisti che condividono la stessa cartella clinica "
            "e lo stesso protocollo di lavoro: foto prima e dopo, "
            "diga di gomma sempre, preventivo scritto consegnato anche "
            "in PDF, follow-up programmato.",
        # 5-row history timeline (year + 1-line description · 2-tuples)
        "history": [
            ("2013",
             "Fondazione dello studio associato in Via Manzoni con due "
             "specialisti e una sala operativa."),
            ("2016",
             "Avvio del reparto implantologico con TAC cone-beam "
             "Carestream CS 9600 e sala chirurgica dedicata."),
            ("2019",
             "Adozione della scansione intraorale iTero e dei piani "
             "ortodontici simulati 3D prima del trattamento."),
            ("2022",
             "Apertura del laboratorio ortodontico interno con stampa "
             "3D di dime chirurgiche e mantenitori notturni."),
            ("2025",
             "Lo studio chiude l'anno con quattro associati a tempo "
             "pieno e una équipe di sei igieniste."),
        ],
        "studio_image":
            # Stylish modern dentist office wide — Cedric Fauntleroy 8244×5496
            "https://images.pexels.com/photos/4269268/pexels-photo-4269268.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop",
        "studio_image_caption": "Sala operativa · Via Manzoni 18",
        "method_title": "Il metodo Denti+Co",
        "method_paragraphs": [
            "L'igiene è il primo capitolo perché è anche il più ripetibile. "
            "Quasi nessuno entra nello studio per la prima volta con la "
            "bocca in ordine: per la maggior parte dei pazienti c'è da "
            "rimettere a posto la base prima di parlare di estetica, "
            "ortodonzia o implantologia. Quaranta minuti di igiene "
            "professionale fatta bene cambiano la prospettiva sul "
            "preventivo di tutti gli interventi successivi.",
            "La cartella clinica è una sola — la stessa per i quattro "
            "associati — perché un paziente non è il paziente di un "
            "singolo dentista, è il paziente dello studio. Quando "
            "l'igienista nota una recessione gengivale durante un "
            "richiamo, lo segnala al parodontologo nello stesso "
            "documento clinico. Niente cure frammentate.",
            "I costi sono dichiarati per le voci di routine (igiene, "
            "conservativa, sbiancamento, controllo). Per i piani più "
            "strutturati — implantologia con rigenerativa, ortodonzia "
            "complessa, riabilitazioni totali — il preventivo è "
            "personalizzato dopo una prima visita di settanta minuti, "
            "ma consegnato sempre per iscritto e firmato in calce.",
        ],
        "values_label":   "Valori dello studio",
        "values_heading": "Quattro impegni, <em>scritti in cartella.</em>",
        "values": [
            ("Diga di gomma sempre",
             "Su ogni intervento di conservativa, endodonzia e "
             "applicazione di compositi. Senza eccezioni."),
            ("Foto prima e dopo",
             "Set fotografico standardizzato consegnato al paziente "
             "in formato digitale alla fine di ogni piano di cura."),
            ("Preventivo scritto",
             "Mai un costo discusso solo verbalmente. PDF in mail "
             "o consegnato in studio prima dell'inizio dei lavori."),
            ("Follow-up programmato",
             "Calendario degli appuntamenti di mantenimento "
             "spedito anche via SMS o WhatsApp. Nessun paziente "
             "lasciato a sé dopo l'intervento."),
        ],
        "cta_heading":
            "Il primo passo è sempre <em>una visita di settanta minuti.</em>",
        "cta_primary_label":   "Conosci i dentisti",
        "cta_secondary_label": "Prenota la prima visita",
        "press_label": "Pubblicato su",
        "press": ["Il Dentista Moderno", "Dental Tribune",
                  "Bocca & Salute", "Corriere Salute"],
    },

    # ─── VISITE (services) — services.html expects `treatments`
    # as a list of 4-tuples (name, meta, desc, price) + cta_*.
    "visite": {
        "eyebrow":  "Trattamenti · listino 2026",
        "headline": "Cosa facciamo, <em>cosa costa, cosa garantiamo.</em>",
        "intro":
            "Il listino completo per le voci di routine. I piani di cura "
            "strutturati (implantologia complessa, ortodonzia, "
            "riabilitazioni totali) ricevono sempre un preventivo "
            "personalizzato dopo la prima visita.",
        "service_image":
            # Close-up advanced dental chair setup with instruments —
            # cottonbro studio 6365×4244 · evokes precision + sterilità
            "https://images.pexels.com/photos/6502543/pexels-photo-6502543.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop",
        "service_image_caption": "Sala operativa · strumentazione e laboratorio interno",
        "treatments": [
            ("Igiene professionale singola",
             "45 min · senza richiesta del medico curante",
             "Charting parodontale, indice di sanguinamento, air-polishing "
             "al bicarbonato di sodio, foto di controllo. Inclusa l'analisi "
             "delle abitudini di igiene domiciliare con eventuale assegnazione "
             "di spazzolino sonico in prova.",
             "€ 95"),
            ("Piano annuale di mantenimento",
             "annuale · 2 igieni + 1 controllo + radiografie endorali",
             "Due igieni semestrali calendarizzate, una visita di controllo "
             "con foto, radiografie endorali quando indicato. Canale "
             "diretto WhatsApp per le urgenze.",
             "€ 220"),
            ("Otturazione conservativa (1 superficie)",
             "45 min · composito stratificato sotto diga di gomma",
             "Composito di marca Tokuyama o 3M, sempre sotto diga di gomma, "
             "fotopolimerizzazione LED qualificata. Garanzia di tenuta "
             "cinque anni con controlli regolari.",
             "€ 140"),
            ("Devitalizzazione mono-radicolare",
             "75 min · localizzatore apicale + sigillatura termoplastica",
             "Endodonzia con localizzatore apicale Morita, sigillatura "
             "tridimensionale con guttaperca termoplastica, otturazione "
             "coronale in composito. Follow-up radiografico a sei e "
             "dodici mesi.",
             "€ 280"),
            ("Impianto singolo (fixture + corona zirconia)",
             "intervento + 2 controlli · garanzia a vita sul fixture",
             "Impianto italiano Sweden+Martina, abutment in zirconia "
             "stabilizzata, corona monolitica fresata in laboratorio "
             "interno. TAC cone-beam preliminare inclusa.",
             "€ 1.850"),
            ("Allineatori Invisalign (piano completo)",
             "12-18 mesi · scansione iTero + piano 3D + mantenitore",
             "Scansione intraorale iTero, piano simulato in 3D consegnato "
             "al paziente prima di iniziare. Allineatori consegnati a "
             "step. Mantenitore notturno post-trattamento incluso.",
             "€ 3.200"),
            ("Sbiancamento professionale alla poltrona",
             "60 min · perossido al 35 % + gel barriera gengivale",
             "Una seduta di sessanta minuti con perossido di idrogeno "
             "al 35 %, gel barriera gengivale fotoindurito, controllo "
             "del PH sulla saliva pre e post trattamento.",
             "€ 380"),
            ("Visita prima volta (cartella + piano)",
             "70 min · anamnesi + scansione iTero + piano in PDF",
             "Anamnesi medica e dentale, esame obiettivo, charting "
             "parodontale, scansione intraorale, foto, consegna del "
             "piano clinico in PDF. Costo detratto dal primo trattamento.",
             "€ 80"),
        ],
        "footnote_heading": "Cosa NON è incluso nel listino",
        "footnote":
            "Le voci di routine sopra sono dichiarate. I piani di cura "
            "strutturati (riabilitazioni totali, implantologia con "
            "rigenerativa estesa, ortodonzia con chirurgia ortognatica) "
            "ricevono un preventivo personalizzato dopo la prima visita "
            "di settanta minuti. Nessun preventivo viene mai dato per "
            "telefono o via mail prima di una visita clinica.",
        "cta_heading":
            "Il preventivo è sempre <em>scritto, firmato, consegnato in PDF.</em>",
        "cta_primary_label":   "Prenota la prima visita",
        "cta_secondary_label": "Scrivici",
    },

    # ─── MEDICI (team) — 4 dental specialists, mix gender ───
    "medici": {
        "eyebrow":  "I dentisti · équipe associata",
        "headline": "Quattro firme, <em>una sola cartella.</em>",
        "intro":
            "I quattro associati condividono la stessa cartella clinica "
            "e si consultano sui piani complessi. Per ogni paziente è "
            "indicato il dentista di riferimento, ma l'igiene di "
            "mantenimento può essere svolta da qualunque dei membri "
            "dell'équipe.",
        "doctors": [
            {
                "name":  "Dr.ssa Chiara Vespa",
                "role":  "Direttore sanitario · Conservativa & endodonzia",
                "bio":
                    "Specialista in odontoiatria conservativa formatasi "
                    "all'Università degli Studi di Milano e perfezionata "
                    "alla Loma Linda University. Membro SIE (Società "
                    "Italiana di Endodonzia). Coordinatrice clinica "
                    "dello studio dal 2013.",
                "portrait": _CHIEF_PORTRAIT,
            },
            {
                "name":  "Dr. Riccardo Berti",
                "role":  "Implantologia & rigenerativa",
                "bio":
                    "Implantologo formatosi alla New York University "
                    "College of Dentistry e perfezionato in Gnatologia "
                    "Clinica all'Università di Pavia. Si occupa di "
                    "implantologia computer-guidata, riabilitazioni "
                    "complesse e rigenerativa ossea.",
                "portrait":
                    # Medical pro in protective gear — kaboompics 4480×6720
                    "https://images.pexels.com/photos/6627850/pexels-photo-6627850.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
            {
                "name":  "Dr.ssa Sofia Liccardi",
                "role":  "Ortodonzia & odontoiatria pediatrica",
                "bio":
                    "Specialista in ortognatodonzia formatasi "
                    "all'Università Cattolica del Sacro Cuore. "
                    "Certificata Invisalign Diamond Provider. Si "
                    "occupa di ortodonzia adulti, intercettiva "
                    "bambini e cura del paziente pediatrico fino "
                    "ai sedici anni.",
                "portrait":
                    # Asian female dentist in clinic — Polina Zimmerman
                    # 3646×5469 · matches female lead role
                    "https://images.pexels.com/photos/4687404/pexels-photo-4687404.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
            {
                "name":  "Dr. Andrea Carofiglio",
                "role":  "Parodontologia & medicina orale",
                "bio":
                    "Parodontologo formatosi all'Università degli Studi "
                    "di Bologna e perfezionato all'Università di Berna. "
                    "Membro SIdP (Società Italiana di Parodontologia "
                    "e Implantologia). Si occupa di parodontite cronica "
                    "e medicina orale.",
                "portrait":
                    # Dentist performing dental care — cottonbro studio
                    # 4047×6070 · portrait orientation, white coat
                    "https://images.pexels.com/photos/6529057/pexels-photo-6529057.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
        ],
        "portrait_city": "Milano · Brera",
    },

    # ─── PUBBLICAZIONI (blog_list) — page metadata at this level,
    # the actual post list lives at the TOP-LEVEL `posts` key (sibling
    # to `pubblicazioni`), the same shape Cardio + Derm use.
    "pubblicazioni": {
        "eyebrow":  "Pubblicazioni & divulgazione",
        "headline": "Cosa abbiamo scritto, <em>per chi.</em>",
        "intro":
            "Articoli divulgativi pubblicati su testate specializzate "
            "e contributi clinici a riviste scientifiche. Tutti i "
            "contenuti sono rivisti personalmente dalla Dr.ssa Vespa "
            "prima della pubblicazione.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Denti+Co · Studio dentistico associato · Milano",
        "empty_body_fallback_paragraphs": [
            "Articolo in preparazione editoriale. La pubblicazione "
            "integrale sarà disponibile a breve.",
            "Questo segnaposto descrive la voce dell'articolo: una nota "
            "clinica scritta dal medico, in tono diretto e privo di "
            "tecnicismi, pensata per pazienti che vogliono informazioni "
            "affidabili sulla propria salute orale.",
        ],
    },

    # Posts list — TOP-LEVEL, sibling to `pubblicazioni`. Same shape
    # the blog_list.html template expects (slug, kicker, title, date,
    # read_min, author, lede).
    "posts": [
        {
            "slug":     "igiene-professionale-perche-semestrale",
            "kicker":   "Igiene & prevenzione",
            "title":    "Igiene professionale: perché la cadenza semestrale è una scelta clinica",
            "date":     "12 marzo 2025",
            "read_min": 8,
            "author":   "Dr.ssa Chiara Vespa",
            "lede":
                "La letteratura clinica supporta una cadenza di igiene "
                "personalizzata, ma la regola dei sei mesi resta il "
                "miglior compromesso fra costo, adesione del paziente "
                "e risultato parodontale a lungo termine.",
        },
        {
            "slug":     "impianti-carico-immediato-quando",
            "kicker":   "Implantologia",
            "title":    "Carico immediato in implantologia: quando è davvero indicato",
            "date":     "23 gennaio 2025",
            "read_min": 12,
            "author":   "Dr. Riccardo Berti",
            "lede":
                "Il carico immediato seduce per il tempo di trattamento "
                "ridotto, ma non è la soluzione universale. I criteri di "
                "selezione del paziente sono restrittivi e vanno spiegati "
                "apertamente prima dell'intervento.",
        },
        {
            "slug":     "allineatori-trasparenti-cosa-non-fanno",
            "kicker":   "Ortodonzia",
            "title":    "Allineatori trasparenti: tre cose che non fanno",
            "date":     "5 novembre 2024",
            "read_min": 6,
            "author":   "Dr.ssa Sofia Liccardi",
            "lede":
                "Sono efficaci nella maggior parte degli adulti, ma non "
                "risolvono tutto. Tre limiti clinici onesti che ogni "
                "paziente dovrebbe conoscere prima di iniziare il piano.",
        },
        {
            "slug":     "parodontite-non-e-solo-gengivite",
            "kicker":   "Parodontologia",
            "title":    "La parodontite non è solo \"gengive che sanguinano\"",
            "date":     "18 settembre 2024",
            "read_min": 5,
            "author":   "Dr. Andrea Carofiglio",
            "lede":
                "La parodontite cronica colpisce un adulto su due dopo i "
                "trentacinque anni, ma si fa diagnosi tardi perché i segnali "
                "iniziali sono silenti. Tre indici parodontali che ogni "
                "paziente può chiedere al proprio dentista.",
        },
    ],

    # ─── CONTATTI (contact) — contact.html expects blocks 3-tuples,
    # form_title/intro/placeholders/consent, hours 3-tuples, transport
    # 2-tuples.
    "contatti": {
        "eyebrow":  "Contatti & sede",
        "headline": "Scriveteci, <em>vi richiamiamo entro la giornata.</em>",
        "intro":
            "Per prenotare una prima visita o un'igiene di mantenimento "
            "potete chiamarci, scriverci via WhatsApp oppure compilare "
            "il modulo qui sotto. Rispondiamo entro la giornata lavorativa.",
        # 4 info-blocks: (label, value, sub) 3-tuples · matches the four
        # SVG icons hard-coded in contact.html (pin · phone · email · clock)
        "blocks": [
            ("Sede",
             "Via Manzoni 18\n20121 Milano",
             "Piano nobile · ingresso indipendente"),
            ("Telefono",
             "+39 02 7770 4488",
             "Risposta in giornata lavorativa"),
            ("Email",
             "studio@denticostudio.it",
             "Per richieste non urgenti"),
            ("Orari",
             "Lun – Ven · 8:30 – 19:30\nSab · 9:00 – 13:00",
             "Domenica chiuso"),
        ],
        "form_title": "Scriveteci, vi richiamiamo entro la giornata.",
        "form_intro":
            "Modulo per richieste informative o per fissare la prima "
            "visita. Per le urgenze cliniche chiamateci direttamente.",
        "form_placeholders": {
            "first_name": "Maria",
            "last_name":  "Bianchi",
            "email":      "maria.bianchi@email.it",
            "phone":      "+39 333 12 34 567",
            "subject":    "Prima visita / igiene / urgenza",
            "message":    "Indicate la fascia oraria preferita e un eventuale dentista di riferimento.",
        },
        "form_helpers": {},
        "form_consent":
            "Acconsento al trattamento dei miei dati personali per la "
            "sola finalità di ricontatto da parte dello studio. "
            "GDPR Art. 6 · DPO contattabile via dpo@denticostudio.it.",
        "form_submit_note":
            "Risposta entro la giornata lavorativa successiva.",
        "hours_heading":    "Orari di apertura",
        # 3-tuples (day, am, pm) — matches contact.html line 175
        "hours": [
            ("Lunedì",    "8:30 – 13:00", "14:00 – 19:30"),
            ("Martedì",   "8:30 – 13:00", "14:00 – 19:30"),
            ("Mercoledì", "8:30 – 13:00", "14:00 – 19:30"),
            ("Giovedì",   "8:30 – 13:00", "14:00 – 19:30"),
            ("Venerdì",   "8:30 – 13:00", "14:00 – 19:30"),
            ("Sabato",    "9:00 – 13:00", "—"),
            ("Domenica",  "—", "Chiuso"),
        ],
        "transport_heading": "Come raggiungerci",
        # 2-tuples (label, text)
        "transport": [
            ("Metropolitana", "M3 Montenapoleone · 3 minuti a piedi"),
            ("Tram",          "Linea 1 · fermata Manzoni"),
            ("Treno",         "Stazione Centrale · 12 minuti M3"),
            ("Parcheggio",    "Garage Via Bigli · 50 metri · convenzionato"),
        ],
    },

    # ─── RICHIEDI-VISITA (appointment) — needs process steps + flat
    # form_fields (form_sections is optional · the appointment.html
    # falls back to a flat field list at line 173-174 when sections
    # are absent).
    "richiedi-visita": {
        "eyebrow":  "Prenota igiene · prima visita",
        "headline": "Prenotate, <em>vi ricontattiamo entro 24 ore.</em>",
        "intro":
            "Compilate il modulo: la segreteria fissa il primo "
            "appuntamento entro la giornata lavorativa successiva e "
            "vi conferma anche via SMS o WhatsApp.",
        "process_label":   "Il percorso di prenotazione",
        "process_heading": "Dal modulo al primo <em>appuntamento</em>, in quattro passi.",
        # 4 process steps (num, title, blurb) — 3-tuples
        "process": [
            ("01", "Modulo & richiamo",
             "La segreteria riceve il modulo, controlla che ci siano "
             "tutti i dati necessari, vi richiama entro la giornata "
             "lavorativa successiva per fissare l'appuntamento."),
            ("02", "Conferma & promemoria",
             "Riceverete la conferma via SMS o WhatsApp con data, "
             "ora, dentista di riferimento, indirizzo dello studio e "
             "indicazioni stradali."),
            ("03", "Prima visita di 70 minuti",
             "Anamnesi, esame clinico completo, scansione iTero, foto "
             "intraorali ed extraorali, charting parodontale, consegna "
             "del piano clinico in PDF."),
            ("04", "Piano scritto",
             "Discussione del piano in poltrona con preventivo voce "
             "per voce. Il costo della prima visita è detratto dal "
             "primo trattamento del piano."),
        ],
        "form_title": "Prenota il primo appuntamento",
        "form_band_side_note":
            "Risposta entro 24 ore lavorative. Per le urgenze cliniche "
            "chiamate direttamente il +39 02 7770 4488.",
        "form_band_side_note_small":
            "I dati raccolti sono usati esclusivamente per ricontattarvi · GDPR Art. 6.",
        "form_fields": [
            {"name": "first_name", "label": "Nome",
             "type": "text",       "required": True,
             "placeholder": "Maria"},
            {"name": "last_name",  "label": "Cognome",
             "type": "text",       "required": True,
             "placeholder": "Bianchi"},
            {"name": "email",      "label": "Email",
             "type": "email",      "required": True,
             "placeholder": "maria.bianchi@email.it"},
            {"name": "phone",      "label": "Telefono",
             "type": "tel",        "required": True,
             "placeholder": "+39 333 12 34 567"},
            {"name": "service",    "label": "Trattamento richiesto",
             "type": "select",     "required": True,
             "options": [
                 "Igiene professionale",
                 "Prima visita (cartella + piano)",
                 "Urgenza odontoiatrica",
                 "Visita implantologica",
                 "Visita ortodontica",
                 "Altro",
             ]},
            {"name": "preferred",  "label": "Fascia oraria preferita",
             "type": "select",     "required": False,
             "options": [
                 "Mattina (8:30 – 13:00)",
                 "Pomeriggio (14:00 – 19:30)",
                 "Sabato mattina",
                 "Indifferente",
             ]},
            {"name": "notes",      "label": "Note (facoltative)",
             "type": "textarea",   "required": False,
             "full_width": True,
             "placeholder": "Indicate eventuali allergie a farmaci, esami pregressi, dentista di riferimento."},
        ],
        "submit_label": "Prenota appuntamento",
        "consent":
            "Acconsento al trattamento dei dati personali per la sola "
            "finalità di ricontatto da parte dello studio. GDPR Art. 6 "
            "· DPO contattabile via dpo@denticostudio.it.",
        "footnote":
            "I dati raccolti sono usati esclusivamente per ricontattarvi "
            "in merito alla richiesta. Conformità GDPR Art. 6 · DPO "
            "contattabile via dpo@denticostudio.it.",
    },
}
