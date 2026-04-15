"""Casa — Domus Immobiliare (mass-market archetype) — IT content tree.

Phase 2g3.7 · Session 53 · Casa Domus Immobiliare — mass-market archetype.
Market-approachable tone.

Voice contract (IT):
- Pragmatic, concrete, accessible — "cerchi casa? noi l'abbiamo trovata
  per 2.800 famiglie dal 2005"
- "tu" throughout — the agency speaks like a trusted neighbourhood
  advisor, never luxury-editorial.
- Concrete details: indirizzi milanesi e torinesi (Brera, Navigli, Porta
  Nuova, Isola, Crocetta, Borgo Po), quartieri Cernobbio/Bellagio per
  il lago, prezzi onesti (€ 420K–€ 1.25M), metrature, bagni, camere.
- Visit-request conversion pattern everywhere: "Richiedi una visita"
  is the primary CTA on each listing tile, each agent card, each
  neighborhood surface.

Differentiation contract vs Villa (D-054 enforcement):
- Casa ships Poppins + Inter + #1B2838 navy + #2ECC71 emerald +
  #E67E22 orange; Villa ships Cormorant + Montserrat + black +
  champagne + white.
- Casa imagery is bright daylight attainable urban interiors.
  Villa imagery is golden-hour cinematic luxury estates.
- Casa hero over a cover photo carries a translucent SEARCH widget
  (location / type / price / rooms). Villa hero is fullbleed
  editorial cover with a dossier card.
- Casa listing grid is 3–4-up property tiles with price / title /
  camere / m² / bagni / badge. Villa is 2-up property dossiers.
- Casa conversion pattern is `viewing-request`. Villa is
  `private-viewing` (by appointment).
- Casa vocabulary: appartamento · trilocale · quadrilocale · attico ·
  monolocale · rogito · metratura · classe energetica · visita
  guidata. Villa vocabulary: dimora · tenuta · residenza · parco ·
  infinity pool · dossier · private viewing.

Page kinds (reusing existing kinds · ZERO view changes):
- home, about (quartieri), services (valutazione), team (agenzia),
  project_list → project_detail (immobili → single-property), contact.
"""
from __future__ import annotations

from typing import Any


CASA_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",        "label": "Home",        "kind": "home"},
        {"slug": "immobili",    "label": "Immobili",    "kind": "project_list"},
        {"slug": "quartieri",   "label": "Quartieri",   "kind": "about"},
        {"slug": "agenzia",     "label": "Agenzia",     "kind": "team"},
        {"slug": "valutazione", "label": "Valutazione", "kind": "services"},
        {"slug": "contatti",    "label": "Contatti",    "kind": "contact"},
    ],

    # Site-wide chrome (consumed by _base.html nav + footer).
    "site": {
        "logo_initial":  "D",
        "logo_word":     "Domus Immobiliare",
        "tag":           "Milano · Torino · dal 2005",
        "phone":         "+39 02 8765 4321",
        "phone_tel":     "+390287654321",
        "phone_label":   "Chiamaci",
        "email":         "ciao@domusimmobiliare.it",
        "address":       "Corso Buenos Aires 15 · 20124 Milano",
        "address_short": "Milano · Torino",
        "hours_compact": "Lun – Sab · 09:00 – 19:30",
        "hours_footer_rows": [
            "Visite guidate anche la domenica",
            "WhatsApp sempre attivo",
        ],
        "whatsapp":      "02 8765 4321",
        "whatsapp_link": "https://wa.me/390287654321",
        "whatsapp_note": "Rispondiamo entro 20 minuti negli orari di apertura",
        "license":       "Licenza agenzia immobiliare RIEA MI 1422 · P.IVA 05431920968",
        "nav_cta":       "Richiedi una visita",
        "nav_cta_href":  "contatti",
        "footer_intro":
            "Domus Immobiliare — selezioniamo a mano ogni immobile che "
            "proponiamo. Vent'anni fra Milano, Torino, il lago di Como e "
            "il Piemonte, un solo agente dedicato dal primo incontro al "
            "rogito.",
        "foot_studio":   "L'agenzia",
        "foot_pages":    "Pagine",
        "foot_contact":  "Contattaci",
        "foot_offices":  "Sedi",
        "offices_footer_rows": [
            "Milano · Buenos Aires 15",
            "Torino · Crocetta 8",
        ],
        # Labels used across listing tiles / property surfaces
        "tile_rooms_label":    "Camere",
        "tile_surface_label":  "Superficie",
        "tile_bathrooms_label":"Bagni",
        "tile_surface_unit":   "m²",
        "tile_visit_cta":      "Richiedi visita",
        "tile_reference_label":"Rif.",
        "surface_short":       "m²",
        "price_label":         "Prezzo",
        "energy_class_label":  "Classe energetica",
        "floor_label":         "Piano",
        "parking_label":       "Posto auto",
        "elevator_label":      "Ascensore",
        # Cross-page filter / label chrome
        "filter_label":        "Filtra per",
        "sort_label":          "Ordina per",
        "visit_request_label": "Richiedi una visita",
        "viewings_unit":       "visite questa settimana",
        "showings_schedule":   "Visite tutti i giorni, anche sabato e domenica",
    },

    # ═══════════════════════════════════════════════════════════════
    # HOME — cover-hero + search widget + featured listings + quartieri
    # + stats counter + agent strip + valuation teaser + testimonial
    # ═══════════════════════════════════════════════════════════════
    "home": {
        "eyebrow":  "Domus Immobiliare · Milano · Torino · Lombardia & Piemonte",
        "headline": "La casa dei tuoi <em>sogni</em>, vicino a te.",
        "intro":
            "Oltre 600 immobili selezionati a mano fra Milano, Torino, il "
            "lago di Como e il Piemonte. Visite guidate anche la domenica, "
            "valutazione gratuita in 24 ore, e un solo agente che ti segue "
            "dal primo appuntamento fino al rogito.",
        "primary_cta":   "Cerca un immobile",
        "primary_href":  "immobili",
        "secondary_cta": "Valutazione gratuita",
        "secondary_href":"valutazione",
        "hero_availability": "20 nuove proposte questa settimana",
        "hero_response":     "Ti ricontattiamo entro 20 minuti",

        # SEARCH WIDGET — the translucent overlay card on the cover photo
        "search_widget": {
            "label":          "Cosa cerchi oggi?",
            "intro":          "Raccontaci casa e quartiere, ci pensiamo noi.",
            "location_label": "Dove",
            "location_value": "Milano, Centro",
            "type_label":     "Tipo immobile",
            "type_value":     "Appartamento",
            "price_label":    "Prezzo",
            "price_value":    "€ 500K — € 1.2M",
            "rooms_label":    "Camere",
            "rooms_value":    "3+ camere",
            "cta":            "Cerca immobile",
            "cta_href":       "immobili",
            "secondary_note": "Oppure raccontaci per WhatsApp cosa cerchi",
            "popular_label":  "I più cercati",
            "popular_tags": [
                "Appartamenti a Brera",
                "Ville a Cernobbio",
                "Loft ai Navigli",
                "Trilocali a Torino",
                "Case con giardino",
            ],
        },

        # FEATURED LISTINGS — 4-up tile grid
        "featured_label":   "In evidenza questa settimana",
        "featured_heading": "Gli immobili <em>che ti aspettano</em>.",
        "featured_intro":
            "Una selezione stretta fra i sopralluoghi fatti negli ultimi "
            "dieci giorni. Ogni scheda è controllata personalmente da un "
            "agente, ogni fotografia è scattata durante la visita.",
        "featured_link":    "Vedi tutti i 600+ immobili",
        "featured_link_href":"immobili",
        # Tuples: (price, title, area, rooms, surface_m2, bathrooms, badge, reference)
        "featured_listings": [
            ("€ 1.250.000", "Attico panoramico con terrazzo",  "Milano · Brera",        "4", "180", "2", "Esclusiva",  "MI-1842"),
            ("€ 890.000",   "Villa moderna con giardino",       "Como · Cernobbio",      "5", "240", "3", "Nuova",      "CO-0217"),
            ("€ 650.000",   "Loft di design in zona Tortona",   "Milano · Navigli",      "2", "120", "2", "Rinnovato",  "MI-1788"),
            ("€ 420.000",   "Trilocale luminoso con balcone",   "Torino · Crocetta",     "3",  "95", "1", "Disponibile","TO-0904"),
        ],

        # NEIGHBORHOODS STRIP — 6 quartieri, shallow preview on home
        "neighborhoods_label":   "Quartieri",
        "neighborhoods_heading": "Dove <em>troviamo casa</em>.",
        "neighborhoods_intro":
            "Milano, Torino, il lago. Ogni quartiere è coperto da un "
            "agente residente — conosciamo i portieri, i bar, le scuole, "
            "la fermata migliore per chi va in centro.",
        "neighborhoods": [
            ("Brera",     "Milano · storico",      "124 immobili",  "da € 850K"),
            ("Navigli",   "Milano · design",       "89 immobili",   "da € 520K"),
            ("Isola",     "Milano · contemporaneo","71 immobili",   "da € 480K"),
            ("Cernobbio", "Como · lago",           "42 immobili",   "da € 680K"),
            ("Crocetta",  "Torino · residenziale", "67 immobili",   "da € 380K"),
            ("Borgo Po",  "Torino · collinare",    "38 immobili",   "da € 410K"),
        ],
        "neighborhoods_cta":      "Esplora tutti i quartieri",
        "neighborhoods_cta_href": "quartieri",

        # STATS BAND — counter-animated numeric strip
        "stats_label":   "Venti anni sul mercato",
        "stats_heading": "I nostri numeri, in chiaro.",
        "stats_intro":
            "Quello che conta non è quante case abbiamo in vetrina, ma "
            "quante ne abbiamo vendute davvero. Ecco i numeri dal 2005 "
            "a oggi.",
        # Tuples: (big_number, suffix, label) — big_number animates via
        # data-lm=counter, suffix sticks unchanged (preserved by motion lib)
        "stats": [
            ("600",   "+", "immobili in portafoglio"),
            ("2.800", "+", "case trovate dal 2005"),
            ("20",    "",  "anni di esperienza"),
            ("4.8",   " ★","su 420 recensioni Google"),
        ],
        "stats_note": "Dati aggiornati a marzo 2026 · verificabili sul portale immobiliare.it",

        # AGENT STRIP — 4 agents shown on home, full 9 on /agenzia
        "agents_label":   "Chi ti accompagna",
        "agents_heading": "Un solo agente, <em>dall'inizio alla fine</em>.",
        "agents_intro":
            "Niente centralino, niente consulenti rotanti. Dal primo "
            "appuntamento al rogito parli sempre con la stessa persona — "
            "quella che conosce il quartiere, il palazzo, spesso anche "
            "il vicino di pianerottolo.",
        # Tuples: (name, role, area, years)
        "agents_preview": [
            ("Giulia Ferrante", "Agente senior",  "Milano · Brera & Centro",  "15 anni"),
            ("Marco Lentini",   "Agente senior",  "Milano · Navigli & Sud",   "12 anni"),
            ("Silvia Mondelli", "Responsabile",   "Torino · Crocetta",        "10 anni"),
            ("Andrea Colombo",  "Agente senior",  "Como · lago",              "18 anni"),
        ],
        "agents_cta":      "Conosci tutto il team",
        "agents_cta_href": "agenzia",

        # VALUATION TEASER — CTA band with emerald call-out
        "valuation_label":   "Valutazione gratuita",
        "valuation_heading": "Quanto vale <em>casa tua</em>?",
        "valuation_intro":
            "Ti richiamiamo entro 24 ore con una stima onesta, basata "
            "sul confronto di tutti i rogiti registrati negli ultimi "
            "dodici mesi nel tuo isolato. Nessun impegno, zero costi, "
            "neanche se poi decidi di vendere con un'altra agenzia.",
        "valuation_cta":       "Richiedi valutazione",
        "valuation_cta_href":  "valutazione",
        "valuation_secondary": "Vedi come funziona",
        "valuation_secondary_href":"valutazione",
        "valuation_proof": [
            ("24 h",   "tempo di risposta"),
            ("€ 0",    "costo, sempre"),
            ("420+",   "valutazioni nel 2025"),
        ],

        # TESTIMONIAL — single warm voice quote
        "testimonial_label":  "Hanno comprato con noi",
        "testimonial_quote":
            "Hanno capito in dieci minuti cosa cercavamo. Tre visite, "
            "la quarta era casa. Giulia ci ha seguito anche dal notaio — "
            "e noi non avevamo mai comprato casa prima.",
        "testimonial_author": "Francesca & Tommaso Ranieri",
        "testimonial_meta":   "Trilocale · Brera · acquistato a marzo 2026",
    },

    # ═══════════════════════════════════════════════════════════════
    # QUARTIERI (about kind) — 8 neighborhood guide cards
    # ═══════════════════════════════════════════════════════════════
    "quartieri": {
        "eyebrow":  "Area guide · Milano · Torino · Como",
        "headline": "I quartieri <em>che conosciamo</em> meglio.",
        "intro":
            "Ogni quartiere qui sotto è coperto da un nostro agente "
            "residente. Di sotto trovi prezzi medi, disponibilità "
            "attuale, metratura tipica e la firma di chi lì lavora "
            "tutti i giorni.",

        "guides_label": "Guida ai quartieri",
        "guides_heading": "Scegli il quartiere, <em>noi conosciamo la strada</em>.",
        # Tuples: (name, city_context, avg_price, available_count, metro_tag, park_tag, vibe_tag, description, agent_lead)
        "guides": [
            (
                "Brera", "Milano · storico & culturale",
                "€ 9.200 / m²", "124 immobili disponibili",
                "M2 Lanza · M3 Montenapoleone", "Parco Sempione a 6 min", "Lusso storico",
                "Il cuore storico di Milano: palazzi ottocenteschi, cortili interni, "
                "ateliers e un tessuto di botteghe che non si ripetono altrove. "
                "Molti interventi di ristrutturazione conservativa, pochi nuovi cantieri. "
                "Adatto a chi cerca un taglio classico con plusvalenza consolidata.",
                "Giulia Ferrante · agente residente dal 2008",
            ),
            (
                "Navigli", "Milano · design & nightlife",
                "€ 7.100 / m²", "89 immobili disponibili",
                "M2 Porta Genova · Tram 3/9", "Darsena · Ticinese a piedi", "Creativo & young",
                "L'asse dei due Navigli: loft industriali, case d'epoca sui ringhioni, "
                "studi d'architettura. Dinamico, internazionale, vivace di sera. Ottimo "
                "per investimento breve-medio o prima casa giovane.",
                "Marco Lentini · agente senior",
            ),
            (
                "Porta Nuova", "Milano · nuovo skyline",
                "€ 10.400 / m²", "56 immobili disponibili",
                "M2 Gioia · M3 Repubblica", "BAM Biblioteca degli Alberi", "Contemporaneo & business",
                "Il distretto della Milano del nuovo millennio: grattacieli, finanza, "
                "residenze di design come Bosco Verticale e Solaria. Adatto a chi "
                "cerca servizi premium, concierge, soluzioni smart-home integrate.",
                "Giulia Ferrante · agente residente",
            ),
            (
                "Isola", "Milano · contemporaneo creativo",
                "€ 7.600 / m²", "71 immobili disponibili",
                "M5 Isola · tram 2/4", "BAM a 5 min · Parco Lambro in 10", "Creativo & residenziale",
                "Ex quartiere operaio oggi rinato intorno a Porta Nuova. Case di ringhiera "
                "recuperate accanto a residenze nuove. Atmosfera milanese autentica, "
                "mercato in crescita stabile da dieci anni.",
                "Sofia Ranieri · agente junior · Milano Nord",
            ),
            (
                "Cernobbio", "Como · lago & ville",
                "€ 5.900 / m²", "42 immobili disponibili",
                "Treno Cadorna-Como · 48 min", "Lago a piedi · Parco Villa Erba", "Lago & seconde case",
                "La sponda occidentale del Lario: ville d'epoca con accesso al lago, "
                "appartamenti in storici condomini affacciati sul golfo, attici con "
                "vista. Mercato internazionale, inglese-tedesco correnti in agenzia.",
                "Andrea Colombo · agente senior lago",
            ),
            (
                "Bellagio", "Como · perla del Lario",
                "€ 6.400 / m²", "29 immobili disponibili",
                "Battello Como-Bellagio · auto", "Centro storico pedonale", "Esclusivo & internazionale",
                "La punta del triangolo lariano: centro storico medievale, ville "
                "sulla punta Spartivento, residenze panoramiche con affaccio duale. "
                "Mercato di nicchia, disponibilità sempre limitata.",
                "Andrea Colombo · lago di Como",
            ),
            (
                "Crocetta", "Torino · residenziale elegante",
                "€ 3.900 / m²", "67 immobili disponibili",
                "M1 Re Umberto · Tram 4/10", "Parco del Valentino · 12 min", "Borghese & famiglie",
                "Il quartiere buono di Torino: palazzi anni '30, cortili silenziosi, "
                "scuole storiche, mercato coperto. Tagli ampi, vivibilità alta, "
                "prezzi ancora accessibili rispetto a Milano. Consigliato per famiglie.",
                "Silvia Mondelli · responsabile Torino",
            ),
            (
                "Borgo Po", "Torino · collinare & panoramico",
                "€ 4.200 / m²", "38 immobili disponibili",
                "Tram 13/15 · Gran Madre", "Collina · Monte dei Cappuccini", "Romantico & vista",
                "La riva destra del Po: palazzotti liberty, ville sulla collina, "
                "attici con vista sulle Alpi. Tessuto di bistrot e locali storici. "
                "Per chi cerca respiro e panorama a dieci minuti dal centro.",
                "Silvia Mondelli · Torino collina & centro",
            ),
        ],

        # FAQ-style band at the end
        "faq_label":   "Domande frequenti sui quartieri",
        "faq_heading": "Quello che ci chiedete più spesso.",
        "faq": [
            (
                "Qual è il quartiere migliore per chi si trasferisce a Milano con famiglia?",
                "Per famiglie raccomandiamo Crocetta a Torino, Isola e Porta Nuova a "
                "Milano. Entrambi hanno scuole in zona, parchi raggiungibili a piedi, "
                "metro vicina. Se invece preferite la collina, Borgo Po a Torino è "
                "la scelta giusta.",
            ),
            (
                "Meglio il centro storico o una zona emergente come investimento?",
                "Dipende dall'orizzonte. Centro storico = plusvalenza consolidata, "
                "crescita 2-3 % annuo. Zone emergenti come Isola hanno fatto +48 % "
                "in dieci anni, ma il rischio è più alto. Parliamone in una call "
                "di quindici minuti.",
            ),
            (
                "Fate anche affitti o solo compravendita?",
                "Principalmente compravendita. Gestiamo affitti solo per immobili "
                "che ci ha affidato un cliente venditore e che preferisce mettere "
                "in locazione nel frattempo. Per affitti puri ti indichiamo il "
                "collega giusto.",
            ),
            (
                "Come funziona il sopralluogo sul lago di Como se abito a Milano?",
                "Organizziamo il sabato mattina una navetta da Milano Cadorna: tre "
                "immobili visitati in giornata, pranzo offerto, rientro per le 18. "
                "Così vedi tutto senza noleggiare auto.",
            ),
        ],

        # Final CTA band
        "cta_label":   "Parla con l'agente del tuo quartiere",
        "cta_heading": "Un caffè, venti minuti, tutto più chiaro.",
        "cta_intro":
            "Scegli un quartiere e ti mettiamo in contatto con l'agente "
            "che ci lavora tutti i giorni. Primo appuntamento gratuito, "
            "in agenzia o sul posto.",
        "cta_primary":       "Richiedi una visita",
        "cta_primary_href":  "contatti",
        "cta_secondary":     "Valutazione gratuita",
        "cta_secondary_href":"valutazione",
    },

    # ═══════════════════════════════════════════════════════════════
    # AGENZIA (team kind) — 9 agent portraits
    # ═══════════════════════════════════════════════════════════════
    "agenzia": {
        "eyebrow":  "Il team · 14 persone · Milano & Torino",
        "headline": "Gli agenti che ti accompagnano <em>dall'incontro al rogito</em>.",
        "intro":
            "Nove agenti iscritti all'albo, due coordinatori, tre "
            "persone nel back-office notarile. Ogni zona ha il suo "
            "agente residente, ogni pratica la sua scheda tecnica, "
            "ogni cliente un solo numero da chiamare.",

        "book_cta":       "Richiedi una visita",
        "agents_heading": "Il team al completo.",
        "agents_intro":
            "In agenzia lavoriamo in coppia: un senior segue l'immobile, "
            "un junior le famiglie che cercano. Così puoi avere risposte "
            "anche la sera e il sabato.",

        # Tuples — rich data for team cards
        "agents": [
            {
                "name": "Giulia Ferrante",
                "role": "Socia · Responsabile Milano Centro",
                "area": "Milano · Brera, Quadrilatero, Porta Nuova",
                "years": "15 anni",
                "languages": "Italiano · Inglese · Francese",
                "speciality": "Palazzi storici, piani alti, piano nobile. "
                              "Accompagnamento completo fra sopralluogo e rogito.",
                "phone": "+39 02 8765 4322",
                "whatsapp_href": "https://wa.me/390287654322",
                "email": "giulia@domusimmobiliare.it",
                "quote": "La casa giusta esiste: il lavoro è ascoltare "
                         "abbastanza a lungo da riconoscerla al primo sopralluogo.",
            },
            {
                "name": "Marco Lentini",
                "role": "Agente senior · Milano Sud",
                "area": "Milano · Navigli, Tortona, Bocconi",
                "years": "12 anni",
                "languages": "Italiano · Inglese",
                "speciality": "Loft industriali, case di ringhiera, interventi "
                              "di design. Contatti con studi di architettura locali.",
                "phone": "+39 02 8765 4323",
                "whatsapp_href": "https://wa.me/390287654323",
                "email": "marco@domusimmobiliare.it",
                "quote": "Sui Navigli il valore non è il metro quadro: "
                         "è il cortile, la luce, il silenzio fra due canali.",
            },
            {
                "name": "Silvia Mondelli",
                "role": "Responsabile Torino",
                "area": "Torino · Crocetta, Cit Turin, Centro",
                "years": "10 anni",
                "languages": "Italiano · Inglese · Spagnolo",
                "speciality": "Famiglie in trasferimento, prime case, "
                              "accompagnamento fiscale per chi rientra dall'estero.",
                "phone": "+39 011 5328 4401",
                "whatsapp_href": "https://wa.me/390115328440",
                "email": "silvia@domusimmobiliare.it",
                "quote": "Torino oggi offre quello che Milano aveva vent'anni fa: "
                         "tagli ampi, prezzi giusti, qualità di vita.",
            },
            {
                "name": "Andrea Colombo",
                "role": "Agente senior · Lago di Como",
                "area": "Como · Cernobbio, Bellagio, Tremezzo",
                "years": "18 anni",
                "languages": "Italiano · Inglese · Tedesco",
                "speciality": "Ville d'epoca, seconde case per clientela "
                              "internazionale, gestione post-vendita stagionale.",
                "phone": "+39 031 2345 6789",
                "whatsapp_href": "https://wa.me/390312345678",
                "email": "andrea@domusimmobiliare.it",
                "quote": "Sul lago ogni villa ha una storia lunga cent'anni. "
                         "Il mio lavoro è accorciare a tre mesi il rogito.",
            },
            {
                "name": "Sofia Ranieri",
                "role": "Agente · Milano Nord",
                "area": "Milano · Isola, Porta Nuova, Dergano",
                "years": "6 anni",
                "languages": "Italiano · Inglese",
                "speciality": "Nuove costruzioni, classe energetica alta, "
                              "prime case per professionisti 30-40 anni.",
                "phone": "+39 02 8765 4324",
                "whatsapp_href": "https://wa.me/390287654324",
                "email": "sofia@domusimmobiliare.it",
                "quote": "La Isola di oggi non è quella di dieci anni fa. "
                         "È più facile vivere, più difficile riconoscere il valore.",
            },
            {
                "name": "Luca Benedetti",
                "role": "Agente · Torino Collina",
                "area": "Torino · Borgo Po, Gran Madre, Maddalena",
                "years": "9 anni",
                "languages": "Italiano · Francese",
                "speciality": "Ville liberty, attici con vista Alpi, "
                              "ristrutturazioni importanti con appalto tecnico.",
                "phone": "+39 011 5328 4402",
                "whatsapp_href": "https://wa.me/390115328441",
                "email": "luca@domusimmobiliare.it",
                "quote": "Torino collina è poesia urbana: dieci minuti dal "
                         "centro e davanti hai le Alpi ogni mattina.",
            },
            {
                "name": "Chiara Sestri",
                "role": "Agente junior · Milano Centro",
                "area": "Milano · Brera, Magenta, Cadorna",
                "years": "3 anni",
                "languages": "Italiano · Inglese · Francese · Arabo",
                "speciality": "Accompagnamento linguistico clientela "
                              "internazionale, pratiche codice fiscale, primo affaccio al mercato italiano.",
                "phone": "+39 02 8765 4325",
                "whatsapp_href": "https://wa.me/390287654325",
                "email": "chiara@domusimmobiliare.it",
                "quote": "Chi compra casa a Milano dall'estero ha bisogno "
                         "di essere accompagnato, non solo servito.",
            },
            {
                "name": "Davide Orsini",
                "role": "Agente · Monza & Brianza",
                "area": "Monza · Seregno · Desio",
                "years": "11 anni",
                "languages": "Italiano · Inglese",
                "speciality": "Case indipendenti con giardino, ville singole, "
                              "mercato residenziale per famiglie che lasciano Milano.",
                "phone": "+39 039 5328 4403",
                "whatsapp_href": "https://wa.me/390395328440",
                "email": "davide@domusimmobiliare.it",
                "quote": "Ogni anno vedo famiglie che comprano in Brianza "
                         "per il terzo figlio: è un indice economico migliore del PIL.",
            },
            {
                "name": "Elisa Parini",
                "role": "Coordinatrice notarile",
                "area": "Back-office · Milano sede centrale",
                "years": "8 anni",
                "languages": "Italiano · Inglese · Spagnolo",
                "speciality": "Pratiche notarili, verifiche ipotecarie, "
                              "istruttoria mutuo, gestione rogito end-to-end.",
                "phone": "+39 02 8765 4326",
                "whatsapp_href": "https://wa.me/390287654326",
                "email": "elisa@domusimmobiliare.it",
                "quote": "Il rogito è l'ultimo metro ma spesso il più "
                         "delicato: un errore sulla planimetria costa mesi.",
            },
        ],

        # Agency facts strip — counter-animated per D-081
        # Tuples: (big_number, suffix, label)
        "facts_label":   "L'agenzia, in breve",
        "facts_heading": "Venti anni, una sola regola: un agente per famiglia.",
        "facts": [
            ("2005", "",  "anno di fondazione"),
            ("9",    "",  "agenti iscritti all'albo"),
            ("2",    "",  "sedi · Milano & Torino"),
            ("2.800","+", "famiglie accompagnate al rogito"),
        ],

        # Close — a warm footer band to the team page
        "footnote_strong": "Vuoi parlare con uno di noi?",
        "footnote_body":
            "Scegli l'agente della tua zona o scrivici in chat: ti "
            "mettiamo in contatto entro un'ora lavorativa. ",
        "footnote_link":  "Scrivici su WhatsApp",
    },

    # ═══════════════════════════════════════════════════════════════
    # VALUTAZIONE (services kind) — multi-step valuation form
    # ═══════════════════════════════════════════════════════════════
    "valutazione": {
        "eyebrow":  "Valutazione gratuita · risposta entro 24 ore",
        "headline": "Quanto vale <em>casa tua</em>?",
        "intro":
            "Ti richiamiamo entro 24 ore con una stima onesta, basata "
            "sul confronto di tutti i rogiti registrati negli ultimi "
            "dodici mesi nel tuo isolato. Nessun impegno, zero costi, "
            "neanche se poi decidi di vendere con un'altra agenzia.",

        "how_it_works_label":   "Come funziona",
        "how_it_works_heading": "Tre passi, <em>niente sorprese</em>.",
        # Tuples: (num, title, body)
        "how_it_works": [
            ("01", "Compili il modulo",
             "Ci bastano indirizzo, tipologia, metratura e quattro dettagli "
             "sullo stato dell'immobile. Cinque minuti, niente documenti "
             "allegati in questa fase."),
            ("02", "Ti richiamiamo entro 24 h",
             "Un agente del tuo quartiere ti chiama, conferma i dati e se "
             "serve fissa un sopralluogo gratuito. Per Milano e Torino "
             "spesso già il giorno dopo."),
            ("03", "Ricevi la stima scritta",
             "Entro 48 ore dal sopralluogo ti arriva una valutazione "
             "scritta con forchetta di prezzo, comparabili della zona, "
             "piano di messa in vendita consigliato."),
        ],

        # The actual form — 3 sections
        "form_label":   "Richiedi la valutazione",
        "form_heading": "Parla del tuo immobile",
        "form_intro":
            "Raccontaci casa tua in cinque minuti. I campi con l'asterisco "
            "sono obbligatori — gli altri aiutano a darti una stima più "
            "precisa già al primo contatto.",
        "form_submit_label": "Richiedi valutazione gratuita",
        "form_submit_note":
            "Ti richiamiamo entro 24 ore lavorative. I tuoi dati sono "
            "trattati solo dall'agente incaricato, nessun terzo coinvolto.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi del "
            "Regolamento UE 679/2016. La richiesta è letta e archiviata "
            "solo dall'agente Domus — nessun broker esterno coinvolto.",

        "form_sections": [
            {"num": "01", "title": "Il tuo immobile",
             "meta": "Indirizzo, tipologia, metratura. Cinque minuti.",
             "fields": ["address", "city", "property_type", "surface", "rooms", "bathrooms"]},
            {"num": "02", "title": "Stato dell'immobile",
             "meta": "Quattro voci che pesano molto sulla stima.",
             "fields": ["condition", "floor", "energy_class", "timeline"]},
            {"num": "03", "title": "I tuoi dati",
             "meta": "Per ricontattarti entro 24 ore.",
             "fields": ["name", "surname", "email", "phone", "notes"]},
        ],

        "form_fields": [
            {"name": "address", "label": "Indirizzo immobile", "type": "text", "required": True,
             "placeholder": "Es. Via della Spiga 12", "full_width": True,
             "helper": "Via e numero civico. Il quartiere lo ricaviamo noi."},
            {"name": "city", "label": "Città", "type": "select", "required": True,
             "options": ["Milano", "Torino", "Como e provincia", "Monza e Brianza", "Altro (specifica nelle note)"],
             "helper": "Se non trovi la tua città, segnalacela nelle note."},
            {"name": "property_type", "label": "Tipologia immobile", "type": "select", "required": True,
             "options": [
                 "Appartamento · bilocale",
                 "Appartamento · trilocale",
                 "Appartamento · quadrilocale o più",
                 "Attico",
                 "Loft",
                 "Villa indipendente",
                 "Villa a schiera o bifamiliare",
                 "Ufficio",
                 "Altro",
             ],
             "helper": "Selezione obbligatoria per procedere."},
            {"name": "surface", "label": "Superficie calpestabile (m²)", "type": "number", "required": True,
             "placeholder": "Es. 95",
             "helper": "Superficie interna abitabile, senza terrazzi né box."},
            {"name": "rooms", "label": "Camere", "type": "select", "required": True,
             "options": ["1", "2", "3", "4", "5", "6 o più"],
             "helper": "Contando le camere da letto, non i soggiorni."},
            {"name": "bathrooms", "label": "Bagni", "type": "select", "required": True,
             "options": ["1", "2", "3", "4 o più"]},
            {"name": "condition", "label": "Stato di conservazione", "type": "select", "required": True,
             "options": [
                 "Nuovo o ristrutturato integralmente",
                 "Buono stato · piccoli interventi",
                 "Da ristrutturare parzialmente",
                 "Da ristrutturare completamente",
                 "Grezzo · immobile di nuova costruzione",
             ],
             "helper": "Influisce molto sulla valutazione."},
            {"name": "floor", "label": "Piano", "type": "select", "required": False,
             "options": ["Piano terra", "Rialzato", "1°", "2°", "3°", "4° o superiore", "Attico", "Villa indipendente"],
             "helper": "Facoltativo — utile per appartamenti."},
            {"name": "energy_class", "label": "Classe energetica", "type": "select", "required": False,
             "options": ["A4 / A3 / A2 / A1", "B", "C", "D", "E", "F", "G", "Non disponibile"],
             "helper": "Se non la sai, seleziona «Non disponibile»."},
            {"name": "timeline", "label": "Tempi di vendita", "type": "select", "required": True,
             "options": [
                 "Entro 3 mesi · urgente",
                 "Entro 6 mesi",
                 "Entro 12 mesi",
                 "Esplorativo · nessuna urgenza",
             ],
             "helper": "Aiuta a pianificare il calendario delle visite."},
            {"name": "name", "label": "Nome", "type": "text", "required": True, "placeholder": "Es. Laura"},
            {"name": "surname", "label": "Cognome", "type": "text", "required": True, "placeholder": "Es. Ferrante"},
            {"name": "email", "label": "Email", "type": "email", "required": True,
             "placeholder": "laura.ferrante@example.it",
             "helper": "Ti inviamo la stima scritta via email."},
            {"name": "phone", "label": "Telefono", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "Ti richiamiamo entro 24 ore lavorative."},
            {"name": "notes", "label": "Note aggiuntive", "type": "textarea", "required": False,
             "full_width": True,
             "placeholder": "Raccontaci qualcosa di più sull'immobile — terrazzo, box, "
                            "cantina, ascensore, eventuali lavori già preventivati. "
                            "Massimo 600 caratteri.",
             "helper": "Facoltativo ma ci aiuta a darti una stima più precisa."},
        ],

        # Reassurance strip
        "proof_label":   "Perché fidarsi",
        "proof_heading": "Una stima seria, non un'esca commerciale.",
        "proof": [
            ("420+",  "valutazioni scritte nel 2025"),
            ("92 %",  "immobili venduti entro il 6° mese"),
            ("€ 0",   "costo della valutazione"),
            ("24 h",  "tempo di risposta"),
        ],

        # FAQ for valuation
        "faq_label":   "Domande sulla valutazione",
        "faq_heading": "Quello che ci chiedete più spesso.",
        "faq": [
            (
                "La valutazione è davvero gratuita?",
                "Sì, sempre. Anche se dopo decidi di vendere con un'altra "
                "agenzia — ci è capitato, non è un dramma. Il costo del "
                "sopralluogo è a nostro carico.",
            ),
            (
                "Quanto tempo passa fra la richiesta e la stima scritta?",
                "Ti richiamiamo entro 24 ore lavorative. Se serve un "
                "sopralluogo, lo fissiamo entro 3 giorni. La stima "
                "scritta arriva entro 48 ore dal sopralluogo.",
            ),
            (
                "La valutazione vale anche per il mutuo o per una successione?",
                "Per uso bancario o successorio serve una perizia giurata "
                "da un perito iscritto al CTU. La nostra stima è di mercato — "
                "preziosa per prendere decisioni, non legalmente opponibile.",
            ),
            (
                "Devo farvi vedere documenti in questa fase?",
                "No. Ci bastano i dati del modulo. Rogito, planimetria e APE "
                "ci serviranno solo se poi decidi di metterla in vendita "
                "con noi.",
            ),
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # CONTATTI — 2 office cards + contact form
    # ═══════════════════════════════════════════════════════════════
    "contatti": {
        "eyebrow":  "Contatti · Milano & Torino",
        "headline": "Scrivici, <em>ti richiamiamo entro 20 minuti</em>.",
        "intro":
            "Puoi scrivere, telefonare, passare in agenzia. Il sabato "
            "siamo aperti tutto il giorno, la domenica per appuntamento. "
            "Per urgenze WhatsApp è il canale più veloce.",

        # Offices — 2 cards with full details + map link
        "offices_label":   "Le sedi",
        "offices_heading": "Due uffici, <em>un'unica squadra</em>.",
        "offices": [
            {
                "name": "Milano · sede centrale",
                "address": "Corso Buenos Aires 15 · 20124 Milano",
                "metro": "M1 Lima · M1 Loreto · Tram 33",
                "hours": "Lun – Sab · 09:00 – 19:30 · Dom su appuntamento",
                "phone": "+39 02 8765 4321",
                "whatsapp": "02 8765 4321",
                "whatsapp_href": "https://wa.me/390287654321",
                "email": "milano@domusimmobiliare.it",
                "map_link": "Apri su Google Maps",
                "map_href": "https://maps.google.com/?q=Corso+Buenos+Aires+15+Milano",
                "lead_agent": "Giulia Ferrante · responsabile Milano",
                "parking": "Parcheggio convenzionato a 80 m · Garage Abadia",
                "note": "Sede ampia con tre sale dedicate agli incontri "
                        "privati. Acqua, caffè, connessione a disposizione.",
            },
            {
                "name": "Torino · Crocetta",
                "address": "Via Legnano 8 · 10128 Torino",
                "metro": "M1 Re Umberto · Tram 4/10",
                "hours": "Lun – Ven · 09:00 – 19:00 · Sab 09:30 – 13:00",
                "phone": "+39 011 5328 4400",
                "whatsapp": "011 5328 4400",
                "whatsapp_href": "https://wa.me/390115328440",
                "email": "torino@domusimmobiliare.it",
                "map_link": "Apri su Google Maps",
                "map_href": "https://maps.google.com/?q=Via+Legnano+8+Torino",
                "lead_agent": "Silvia Mondelli · responsabile Torino",
                "parking": "ZTL gratuita nel weekend · parcheggio Piazza Solferino",
                "note": "Ufficio accogliente nel cuore della Crocetta, due "
                        "minuti a piedi dal Politecnico.",
            },
        ],

        # Direct channels
        "channels_label":   "Canali diretti",
        "channels_heading": "Scegli come sentirci.",
        "channels": [
            ("Telefono",        "+39 02 8765 4321",                "Risposta immediata in orario di apertura"),
            ("WhatsApp Milano", "02 8765 4321",                    "Messaggio letto entro 20 minuti · anche la sera"),
            ("WhatsApp Torino", "011 5328 4400",                   "Lun – Sab · stesso team che vedi in ufficio"),
            ("Email",           "ciao@domusimmobiliare.it",        "Rispondiamo entro 4 ore lavorative"),
            ("In agenzia",      "Milano · Corso Buenos Aires 15", "Senza appuntamento Lun – Sab mattina"),
        ],

        # General contact form
        "form_label":   "Scrivici un messaggio",
        "form_heading": "Lascia i tuoi riferimenti",
        "form_intro":
            "Compila il form, ti richiamiamo entro 20 minuti in orario "
            "di apertura. Se ci scrivi la sera, rispondiamo la mattina "
            "dopo entro le dieci.",
        "form_submit_label": "Invia messaggio",
        "form_submit_note":
            "Risposta entro 20 minuti in orario di apertura · 4 ore "
            "lavorative per email fuori orario.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi del "
            "Regolamento UE 679/2016. La richiesta è letta e archiviata "
            "solo dall'agente Domus.",

        "form_sections": [
            {"num": "01", "title": "I tuoi dati",
             "meta": "Per risponderti direttamente.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Come possiamo aiutarti",
             "meta": "Un breve riferimento, poi ne parliamo al telefono.",
             "fields": ["topic", "preferred_office", "message"]},
        ],

        "form_fields": [
            {"name": "name", "label": "Nome", "type": "text", "required": True, "placeholder": "Es. Francesca"},
            {"name": "surname", "label": "Cognome", "type": "text", "required": True, "placeholder": "Es. Ranieri"},
            {"name": "email", "label": "Email", "type": "email", "required": True,
             "placeholder": "francesca@example.it"},
            {"name": "phone", "label": "Telefono", "type": "tel", "required": False,
             "placeholder": "+39 ...", "helper": "Facoltativo · se preferisci essere richiamata."},
            {"name": "topic", "label": "Oggetto della richiesta", "type": "select", "required": True,
             "options": [
                 "Vorrei comprare casa",
                 "Vorrei vendere casa",
                 "Vorrei una valutazione gratuita",
                 "Sto cercando affitto (segnalo al partner)",
                 "Altro · ti racconto nel messaggio",
             ]},
            {"name": "preferred_office", "label": "Ufficio di riferimento", "type": "select", "required": True,
             "options": ["Milano · Corso Buenos Aires", "Torino · Via Legnano", "Lago di Como · su appuntamento"]},
            {"name": "message", "label": "Messaggio", "type": "textarea", "required": True, "full_width": True,
             "placeholder": "Cosa cerchi, a che punto sei, quando vorresti "
                            "sentirci. Massimo 800 caratteri — i dettagli li "
                            "approfondiamo in call.",
             "helper": "Basta una sintesi: il resto lo discutiamo a voce."},
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # IMMOBILI (project_list kind) — full listings grid
    # ═══════════════════════════════════════════════════════════════
    "immobili": {
        "eyebrow":  "Vetrina completa · 600+ immobili · aggiornata questa settimana",
        "headline": "Tutti gli immobili <em>che abbiamo in mano</em>.",
        "intro":
            "Una selezione viva: ogni scheda è verificata dall'agente "
            "di zona, ogni fotografia è scattata dal vivo, nessun "
            "rendering. Le novità arrivano ogni lunedì mattina.",

        "filter_label": "Filtra",
        "filters": [
            "Tutti",
            "Milano",
            "Torino",
            "Lago di Como",
            "Sotto € 500K",
            "€ 500K — 1 M",
            "Sopra € 1 M",
            "Attico",
            "Villa",
            "Loft",
            "Nuova costruzione",
        ],
        "sort_label": "Ordina",
        "sort_options": [
            "Più recenti",
            "Prezzo crescente",
            "Prezzo decrescente",
            "Metratura decrescente",
        ],

        "ledger_label": "Vetrina completa",
        "ledger_intro":
            "Clicca su una scheda per aprire la proposta completa: "
            "planimetria, classe energetica, storia dei lavori, agente "
            "di riferimento e slot di visita già prenotabili.",

        # Row labels used by the property_list template
        "row_rooms_label":    "Camere",
        "row_surface_label":  "m²",
        "row_area_label":     "Zona",
        "row_price_label":    "Prezzo",
        "row_year_label":     "Dal",
        "row_discipline_label":"Tipologia",
        "row_duration_label": "Durata media visita",

        # Map snippet — placeholder band
        "map_label":   "Dove stiamo cercando",
        "map_heading": "La nostra vetrina, <em>sulla cartina</em>.",
        "map_intro":
            "Tre province, due sedi, una squadra sola. Ogni punto sulla "
            "mappa corrisponde a un immobile attualmente in vendita o "
            "in procinto di entrare in vetrina.",
        "map_note":
            "La mappa interattiva è disponibile nella versione completa "
            "del sito commerciale — qui vedi solo una copertura "
            "indicativa della presenza.",
        "map_cells": [
            ("Milano città",   "412 immobili"),
            ("Monza Brianza",  "58 immobili"),
            ("Lago di Como",   "71 immobili"),
            ("Torino città",   "105 immobili"),
            ("Torino collina", "38 immobili"),
        ],

        # CTA band before footer
        "cta_label":        "Non trovi quello che cerchi?",
        "cta_heading":      "Scrivici cosa ti manca. <em>La troviamo noi</em>.",
        "cta_intro":
            "Negli ultimi cinque anni più del 30 % delle case che abbiamo "
            "venduto non erano ancora online: le avevamo in mano da "
            "venditori abituali. Raccontaci cosa cerchi e ti avvisiamo "
            "appena arriva qualcosa di giusto.",
        "cta_primary":        "Richiedi una visita",
        "cta_primary_href":   "contatti",
        "cta_secondary":      "Parliamone a voce",
        "cta_secondary_href": "contatti",

        # Dossier labels (used by property_detail)
        "dossier_meta_price_label":    "Prezzo",
        "dossier_meta_surface_label":  "Superficie",
        "dossier_meta_rooms_label":    "Camere",
        "dossier_meta_bathrooms_label":"Bagni",
        "dossier_meta_energy_label":   "Classe energetica",
        "dossier_meta_floor_label":    "Piano",
        "dossier_summary_label":       "Ciò che amerai",
        "dossier_highlights_label":    "Punti forti",
        "dossier_highlights_heading":  "I dettagli che contano.",
        "dossier_agent_label":         "Agente di riferimento",
        "dossier_book_cta":            "Richiedi una visita",
        "dossier_next_label":          "Prossimo immobile",
    },

    # ═══════════════════════════════════════════════════════════════
    # POSTS — 12 property detail surfaces (project_detail kind)
    # Each renders at /immobili/<slug>/
    # ═══════════════════════════════════════════════════════════════
    "posts": [
        {
            "slug":       "attico-brera-duomo",
            "title":      "Attico panoramico con terrazzo · Brera",
            "price":      "€ 1.250.000",
            "area":       "Milano · Brera · Via Madonnina 14",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "180",
            "energy":     "B",
            "floor":      "7° (ultimo · ascensore)",
            "badge":      "Esclusiva",
            "reference":  "MI-1842",
            "year_built": "1923 · ristrutturazione integrale 2024",
            "lead":
                "Un attico all'ultimo piano di un palazzo d'epoca con "
                "terrazzo di sessanta metri e vista a 270 gradi su Duomo "
                "e piazza della Scala. Ristrutturazione 2024 firmata da "
                "Studio Arfaioli, tecnologia smart-home integrata.",
            "summary": [
                "Terrazzo di 62 m² con vista Duomo e Sforzesco",
                "Quattro camere, due bagni con finiture marmo di Carrara",
                "Classe energetica B dopo cappotto e serramenti 2024",
                "Ascensore interno fino all'attico, tre posti auto inclusi",
                "Pronto consegna · rogito entro 45 giorni",
            ],
            "highlights": [
                ("Terrazzo", "62 m² vista Duomo"),
                ("Posto auto", "Tre posti in box privato"),
                ("Domotica", "Knx full-integrato"),
                ("Classe energetica", "B · dopo intervento 2024"),
            ],
            "description":
                "L'appartamento è stato completamente ridisegnato sull'idea "
                "di un loft verticale: zona giorno di 70 m² con doppia "
                "esposizione est-sud, isola in ottone spazzolato, libreria "
                "a tutta parete in noce canaletto. La zona notte è "
                "riservata alle due suite con cabina armadio e bagno "
                "privato in marmo statuario. Sul terrazzo, vasca "
                "idromassaggio outdoor e dining table per dieci.",
            "agent_name":  "Giulia Ferrante",
            "agent_role":  "Agente senior · Milano Centro",
            "agent_phone": "+39 02 8765 4322",
        },
        {
            "slug":       "villa-cernobbio-lago",
            "title":      "Villa moderna con giardino · Cernobbio",
            "price":      "€ 890.000",
            "area":       "Como · Cernobbio · Via Regina 88",
            "rooms":      "5",
            "bathrooms":  "3",
            "surface":    "240",
            "energy":     "A2",
            "floor":      "Villa indipendente · 3 livelli",
            "badge":      "Nuova",
            "reference":  "CO-0217",
            "year_built": "2023",
            "lead":
                "Villa di nuova costruzione su tre livelli a duecento "
                "metri dal lago, giardino privato di mille metri con "
                "piscina riscaldata. Finiture contemporanee, impianto "
                "geotermico, classe A2.",
            "summary": [
                "Giardino privato di 1.020 m² con piscina 10 × 4",
                "Cinque camere, tre bagni, studio e lavanderia separati",
                "Impianto geotermico · classe energetica A2",
                "Accesso diretto al lago a 200 m",
                "Box doppio e posto ospiti coperto",
            ],
            "highlights": [
                ("Giardino", "1.020 m² con piscina"),
                ("Impianto", "Geotermico · fotovoltaico 8 kW"),
                ("Camere", "Cinque · due suite"),
                ("Classe", "A2 · consumi quasi nulli"),
            ],
            "description":
                "La villa sorge su un lotto d'angolo con giardino tre "
                "lati, orientamento sud-est per la zona giorno. Piano "
                "interrato con taverna, cantina climatizzata e box "
                "doppio; piano terra con salotto doppio altezza, "
                "cucina professionale Boffi e accesso al giardino; "
                "piano superiore con quattro camere e due bagni, più "
                "suite matrimoniale con cabina armadio.",
            "agent_name":  "Andrea Colombo",
            "agent_role":  "Agente senior · Lago di Como",
            "agent_phone": "+39 031 2345 6789",
        },
        {
            "slug":       "loft-tortona-navigli",
            "title":      "Loft di design in zona Tortona",
            "price":      "€ 650.000",
            "area":       "Milano · Navigli · Via Savona 22",
            "rooms":      "2",
            "bathrooms":  "2",
            "surface":    "120",
            "energy":     "C",
            "floor":      "Piano terra rialzato · cortile",
            "badge":      "Rinnovato",
            "reference":  "MI-1788",
            "year_built": "1902 · recupero ex-opificio 2020",
            "lead":
                "Loft di centoventi metri in ex-opificio dei primi del "
                "'900, doppia altezza quattro metri e mezzo, pavimento "
                "originale in rovere, soppalco ferro nero per la zona "
                "notte. Affaccio su corte interna silenziosa.",
            "summary": [
                "Soffitto in travi di ferro e calcestruzzo a vista",
                "Zona giorno doppia altezza · open kitchen",
                "Soppalco ferro e legno · suite con cabina armadio",
                "Cortile comune con giardinetto interno",
                "Zero affacci stradali · silenzio totale",
            ],
            "highlights": [
                ("Altezza", "4,5 m doppia altezza"),
                ("Luce", "Finestrone 6 × 3 m"),
                ("Arredo", "Cucina Boffi inclusa"),
                ("Affaccio", "Cortile silenzioso"),
            ],
            "description":
                "Il loft è ricavato dall'ultimo modulo di un ex-opificio "
                "tessile restaurato nel 2020. Mantenute le colonne "
                "portanti in ghisa, il pavimento originale in rovere "
                "riposizionato, gli infissi in ferro sostituiti con "
                "vetro-camera termico. La zona notte soppalcata domina "
                "l'ambiente senza chiuderlo.",
            "agent_name":  "Marco Lentini",
            "agent_role":  "Agente senior · Milano Sud",
            "agent_phone": "+39 02 8765 4323",
        },
        {
            "slug":       "trilocale-crocetta-torino",
            "title":      "Trilocale luminoso con balcone · Crocetta",
            "price":      "€ 420.000",
            "area":       "Torino · Crocetta · Corso Giovanni Lanza 7",
            "rooms":      "3",
            "bathrooms":  "1",
            "surface":    "95",
            "energy":     "D",
            "floor":      "3° (ascensore)",
            "badge":      "Disponibile",
            "reference":  "TO-0904",
            "year_built": "1932 · manutenzione ordinaria 2019",
            "lead":
                "Trilocale nel cuore della Crocetta, palazzo anni Trenta "
                "ottimamente conservato, balcone di sette metri vista "
                "interno verde, esposizione est-ovest. Distribuzione "
                "classica, parquet originale.",
            "summary": [
                "Palazzo anni '30 · cappotto rifatto 2018",
                "Balcone di 7 m² con affaccio cortile verde",
                "Parquet originale in rovere · travi a vista ingresso",
                "Cantina di 12 m² in dotazione",
                "Pronto consegna · libero al rogito",
            ],
            "highlights": [
                ("Palazzo", "1932 · segreteria 24/7"),
                ("Balcone", "7 m² vista verde"),
                ("Parquet", "Originale restaurato"),
                ("Piano", "3° con ascensore"),
            ],
            "description":
                "Appartamento in uno dei palazzi simbolo della Crocetta, "
                "via tranquilla a duecento metri da corso Galileo "
                "Ferraris. Distribuzione classica: ingresso, soggiorno "
                "con balcone, cucina abitabile, corridoio, due camere "
                "matrimoniali, bagno finestrato. Parquet originale in "
                "ottimo stato, impianti rifatti nel 2019.",
            "agent_name":  "Silvia Mondelli",
            "agent_role":  "Responsabile Torino",
            "agent_phone": "+39 011 5328 4401",
        },
        {
            "slug":       "quadrilocale-isola-milano",
            "title":      "Quadrilocale vista BAM · Isola",
            "price":      "€ 780.000",
            "area":       "Milano · Isola · Via Confalonieri 25",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "135",
            "energy":     "A3",
            "floor":      "8° (ascensore doppio)",
            "badge":      "Vista parco",
            "reference":  "MI-1915",
            "year_built": "2019",
            "lead":
                "Appartamento in residenza di design del 2019, affaccio "
                "principale sulla Biblioteca degli Alberi. Quattro "
                "camere, due bagni, balcone abitabile di undici metri. "
                "Classe A3, domotica di serie.",
            "summary": [
                "Vista parco BAM dal soggiorno",
                "Balcone abitabile di 11 m²",
                "Condominio con concierge H24",
                "Box auto incluso · colonnina ricarica EV",
                "Classe A3 · aria condizionata integrata",
            ],
            "highlights": [
                ("Vista", "BAM e Bosco Verticale"),
                ("Concierge", "H24 in portineria"),
                ("Ricarica", "Colonnina EV inclusa"),
                ("Classe", "A3 · pompa di calore"),
            ],
            "description":
                "Ottavo piano in residenza firmata Piuarch con concierge "
                "H24, palestra condominiale e giardino interno. "
                "Appartamento d'angolo con doppio affaccio: soggiorno "
                "verso il parco BAM, zona notte verso cortile interno. "
                "Balcone-loggia di undici metri utilizzabile nove mesi "
                "l'anno. Arredi custom di serie inclusi.",
            "agent_name":  "Sofia Ranieri",
            "agent_role":  "Agente · Milano Nord",
            "agent_phone": "+39 02 8765 4324",
        },
        {
            "slug":       "bilocale-porta-nuova",
            "title":      "Bilocale smart · Porta Nuova",
            "price":      "€ 520.000",
            "area":       "Milano · Porta Nuova · Via Melchiorre Gioia 62",
            "rooms":      "2",
            "bathrooms":  "1",
            "surface":    "68",
            "energy":     "A2",
            "floor":      "12° (vista Unicredit)",
            "badge":      "Ottimo investimento",
            "reference":  "MI-1967",
            "year_built": "2015",
            "lead":
                "Bilocale all'ottantesimo per cento esposizione sud, "
                "vista sul parco e sui grattacieli di Porta Nuova. "
                "Ottimo per primo acquisto o investimento buy-to-let, "
                "rendimento lordo atteso 4,2 %.",
            "summary": [
                "Esposizione sud · luce tutto il giorno",
                "Vista torre Unicredit e Diamante",
                "Concierge di zona · palestra condominiale",
                "Rendimento buy-to-let stimato 4,2 % lordo",
                "Pronto consegna · sfitto al rogito",
            ],
            "highlights": [
                ("Esposizione", "Sud piena"),
                ("Piano", "12° vista skyline"),
                ("Rendimento", "4,2 % lordo atteso"),
                ("Sfitto", "Al rogito"),
            ],
            "description":
                "Bilocale di 68 m² con soggiorno-cucina di 32 m² vista "
                "skyline, camera matrimoniale con cabina armadio, bagno "
                "finestrato in pietra grigia. Condominio servito con "
                "palestra e lounge, concierge diurno sette giorni su "
                "sette. Ideale per chi lavora nelle torri limitrofe "
                "o cerca un investimento a reddito.",
            "agent_name":  "Giulia Ferrante",
            "agent_role":  "Agente senior · Milano Centro",
            "agent_phone": "+39 02 8765 4322",
        },
        {
            "slug":       "villa-bellagio-lago",
            "title":      "Villa d'epoca affaccio Spartivento · Bellagio",
            "price":      "€ 1.950.000",
            "area":       "Como · Bellagio · Via Garibaldi 12",
            "rooms":      "6",
            "bathrooms":  "4",
            "surface":    "320",
            "energy":     "E",
            "floor":      "Villa indipendente · 3 livelli + torretta",
            "badge":      "Villa storica",
            "reference":  "CO-0248",
            "year_built": "1908 · restauro conservativo 2017",
            "lead":
                "Villa liberty a Punta Spartivento, 320 metri coperti "
                "più torretta belvedere, giardino terrazzato con "
                "accesso privato al lago. Restauro conservativo 2017 "
                "con climatizzazione e impianti aggiornati.",
            "summary": [
                "Punta Spartivento · vista duale sul lago",
                "Giardino terrazzato con accesso privato al lago",
                "Torretta belvedere panoramica a 360°",
                "Restauro 2017 con impianti contemporanei",
                "Sei camere, quattro bagni, cantina storica",
            ],
            "highlights": [
                ("Posizione", "Punta Spartivento"),
                ("Vista", "Duale lago"),
                ("Accesso", "Privato al lago"),
                ("Torretta", "Belvedere 360°"),
            ],
            "description":
                "Villa simbolo del liberty lariano, disegnata dall'architetto "
                "Pietro Lingeri nel 1908. Tre livelli abitabili più "
                "torretta belvedere, affaccio a est sul ramo di Lecco "
                "e a ovest sul ramo di Como. Il restauro 2017 ha "
                "preservato stucchi originali, vetrate liberty e "
                "pavimenti in seminato veneziano, integrando impianti "
                "radianti e climatizzazione nascosta.",
            "agent_name":  "Andrea Colombo",
            "agent_role":  "Agente senior · Lago di Como",
            "agent_phone": "+39 031 2345 6789",
        },
        {
            "slug":       "appartamento-borgo-po-torino",
            "title":      "Appartamento vista Alpi · Borgo Po",
            "price":      "€ 560.000",
            "area":       "Torino · Borgo Po · Corso Casale 102",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "145",
            "energy":     "D",
            "floor":      "5° (ultimo · ascensore)",
            "badge":      "Vista collina",
            "reference":  "TO-0945",
            "year_built": "1928 · appartamento ristrutturato 2021",
            "lead":
                "Ultimo piano con vista aperta sulla Mole, il Monte "
                "dei Cappuccini e le Alpi. Centoquarantacinque metri "
                "su un unico livello, due balconi abitabili, taglio "
                "classico perfettamente conservato.",
            "summary": [
                "Vista Alpi e Mole Antonelliana dal soggiorno",
                "Due balconi abitabili · 6 + 4 m²",
                "Soffitti 3,20 m con stucchi originali",
                "Ristrutturazione 2021 · impianti nuovi",
                "Cantina e soffitta di 18 m² incluse",
            ],
            "highlights": [
                ("Vista", "Alpi e Mole"),
                ("Piano", "5° ultimo"),
                ("Soffitti", "3,20 m stucco"),
                ("Balconi", "Due abitabili"),
            ],
            "description":
                "Ultimo piano d'angolo in palazzo anni Venti restaurato "
                "nel 2020, quattro camere disposte su un unico "
                "livello, doppio affaccio su corso Casale e via "
                "Villa della Regina. Zona giorno affacciata sulla "
                "Mole, zona notte verso la collina. Stucchi originali "
                "mantenuti in tutti gli ambienti.",
            "agent_name":  "Luca Benedetti",
            "agent_role":  "Agente · Torino Collina",
            "agent_phone": "+39 011 5328 4402",
        },
        {
            "slug":       "villa-monza-brianza",
            "title":      "Villa indipendente con parco · Monza",
            "price":      "€ 1.050.000",
            "area":       "Monza · San Fruttuoso · Via Buonarroti 48",
            "rooms":      "6",
            "bathrooms":  "4",
            "surface":    "280",
            "energy":     "B",
            "floor":      "Villa indipendente · 3 livelli",
            "badge":      "Parco privato",
            "reference":  "MB-0177",
            "year_built": "2001 · riqualificazione 2022",
            "lead":
                "Villa indipendente su lotto di milleduecento metri, "
                "parco piantumato con alberi d'alto fusto, piscina "
                "riscaldata e area giochi per bambini. Tre livelli "
                "abitabili più taverna e area fitness.",
            "summary": [
                "Parco privato di 1.200 m² con piscina riscaldata",
                "Sei camere · quattro bagni · studio · taverna",
                "Area fitness e sauna al piano interrato",
                "Classe B dopo cappotto 2022 · fotovoltaico 12 kW",
                "Box triplo e posto ospiti coperto",
            ],
            "highlights": [
                ("Parco", "1.200 m² alberato"),
                ("Piscina", "Riscaldata · 10 × 4,5"),
                ("Fitness", "Sauna · palestra interrata"),
                ("Classe", "B · fotovoltaico 12 kW"),
            ],
            "description":
                "La villa si trova in zona residenziale a dieci minuti "
                "da Monza centro e a venti dalla Milano del nord. "
                "Progetto 2001 di grande qualità, riqualificazione "
                "2022 con cappotto, serramenti triplovetro, impianto "
                "fotovoltaico. Piano terra con zona giorno di "
                "centoventi metri affacciata sul parco, piano primo "
                "con quattro camere e tre bagni, mansarda con studio "
                "e camera ospiti.",
            "agent_name":  "Davide Orsini",
            "agent_role":  "Agente · Monza & Brianza",
            "agent_phone": "+39 039 5328 4403",
        },
        {
            "slug":       "monolocale-navigli-milano",
            "title":      "Monolocale d'autore affaccio alzaia · Navigli",
            "price":      "€ 295.000",
            "area":       "Milano · Navigli · Alzaia Naviglio Grande 76",
            "rooms":      "1",
            "bathrooms":  "1",
            "surface":    "42",
            "energy":     "C",
            "floor":      "2° (scala a chiocciola storica)",
            "badge":      "Affaccio acqua",
            "reference":  "MI-1994",
            "year_built": "1898 · restauro 2018",
            "lead":
                "Monolocale di quarantadue metri con finestrone "
                "sull'alzaia del Naviglio Grande, restauro "
                "conservativo 2018 firmato da studio Ca' Rossa. "
                "Ottimo come primo acquisto o investimento short-let.",
            "summary": [
                "Affaccio diretto sull'alzaia · finestrone 2 × 1,5",
                "Palazzo del 1898 · scala a chiocciola originale",
                "Cucina Boffi integrata · bagno in pietra serena",
                "Ideale per investimento short-let",
                "Rendimento stimato 5,8 % lordo",
            ],
            "highlights": [
                ("Affaccio", "Naviglio Grande"),
                ("Palazzo", "1898 scala storica"),
                ("Rendimento", "5,8 % lordo"),
                ("Uso", "Short-let/prima casa"),
            ],
            "description":
                "Monolocale ricavato al secondo piano di un palazzo "
                "storico direttamente sull'alzaia del Naviglio "
                "Grande. Finestrone doppio affaccio con vetrate a "
                "ghigliottina restaurate, pavimenti originali in "
                "cotto lucidato, cucina integrata firmata Boffi e "
                "bagno in pietra serena. Adatto a uso personale o "
                "come investimento a reddito: negli ultimi tre anni "
                "short-let stabile sopra il 5,5 % lordo.",
            "agent_name":  "Marco Lentini",
            "agent_role":  "Agente senior · Milano Sud",
            "agent_phone": "+39 02 8765 4323",
        },
        {
            "slug":       "attico-centro-torino",
            "title":      "Attico fronte Palazzo Reale · Torino",
            "price":      "€ 780.000",
            "area":       "Torino · Centro · Piazzetta Reale 3",
            "rooms":      "3",
            "bathrooms":  "2",
            "surface":    "140",
            "energy":     "C",
            "floor":      "6° (ultimo · ascensore)",
            "badge":      "Vista storica",
            "reference":  "TO-0982",
            "year_built": "1874 · attico ricavato 2022",
            "lead":
                "Attico con terrazzino abitabile affacciato su Palazzo "
                "Reale, Duomo e Mole Antonelliana. Centoquaranta "
                "metri su un unico livello, ricavato nel sottotetto "
                "storico con intervento firmato Studio Isolarchitetti.",
            "summary": [
                "Terrazzo abitabile 24 m² vista Palazzo Reale",
                "Ricavato da sottotetto storico · 2022",
                "Tre camere, due bagni, studio indipendente",
                "Soffitti mansardati con travi a vista originali",
                "Classe C dopo isolamento copertura 2022",
            ],
            "highlights": [
                ("Vista", "Palazzo Reale, Mole, Duomo"),
                ("Terrazzo", "24 m² abitabile"),
                ("Travi", "A vista originali"),
                ("Classe", "C post-isolamento"),
            ],
            "description":
                "Attico ricavato nel sottotetto di un palazzo "
                "seicentesco ristrutturato nel 2022 dagli "
                "Isolarchitetti. Mantenute travi in larice originali, "
                "pavimento in cotto lucido posato a spina di pesce, "
                "bagni in pietra di Luserna. Il terrazzo panoramico "
                "si apre su piazzetta Reale e regala vista duale "
                "verso Mole e Duomo.",
            "agent_name":  "Silvia Mondelli",
            "agent_role":  "Responsabile Torino",
            "agent_phone": "+39 011 5328 4401",
        },
        {
            "slug":       "loft-isola-milano",
            "title":      "Loft ex-officina con cortile · Isola",
            "price":      "€ 680.000",
            "area":       "Milano · Isola · Via Borsieri 32",
            "rooms":      "2",
            "bathrooms":  "2",
            "surface":    "115",
            "energy":     "B",
            "floor":      "Piano terra · cortile proprietà",
            "badge":      "Cortile privato",
            "reference":  "MI-2012",
            "year_built": "1927 · recupero integrale 2023",
            "lead":
                "Loft ricavato da ex-officina con trenta metri di "
                "cortile privato, doppia altezza cinque metri e "
                "finestroni industriali originali. Recupero "
                "integrale 2023, impianti radianti e fotovoltaico.",
            "summary": [
                "Cortile privato di 30 m² · essenze mediterranee",
                "Doppia altezza 5 m · finestroni industriali",
                "Recupero 2023 · impianti radianti + fotovoltaico",
                "Loft aperto con suite chiusa · bagno cieco di servizio",
                "Classe B · pompa di calore + 4 kW solare",
            ],
            "highlights": [
                ("Cortile", "30 m² privato"),
                ("Altezza", "5 m industriale"),
                ("Impianto", "Radiante + solare"),
                ("Classe", "B · quasi autonomo"),
            ],
            "description":
                "Il loft nasce dal recupero di un'ex-officina "
                "meccanica del 1927. Volumi lasciati intatti, "
                "zonizzazione minima con suite chiusa da parete "
                "vetrata e cucina-isola al centro. Cortile privato "
                "di trenta metri a uso esclusivo con rampicanti, "
                "piano di cottura outdoor integrato, seduta in "
                "cemento lisciato. Un pezzo della Milano che era e "
                "di quella che sta diventando.",
            "agent_name":  "Sofia Ranieri",
            "agent_role":  "Agente · Milano Nord",
            "agent_phone": "+39 02 8765 4324",
        },
    ],
}

# Phase 2g3.7 · Session 53 · D-047 compliance closing comment:
# All user-visible literals in skin + preview compositions MUST be sourced
# from this content tree (or chrome / dna.content). No "Brera" / "Torino"
# / "Milano" / "camere" / "Richiedi visita" / "m²" may appear hard-coded
# in the HTML. Review in every PR touching real-estate/mass-market.
