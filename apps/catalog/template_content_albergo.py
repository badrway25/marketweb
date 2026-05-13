"""Albergo Borgo — Relais hospitality in a Tuscan UNESCO village.

T56 · Wave 2 Pass-1 (2026-05-12) · ultra-luxury-cinematic archetype.
1st reuse after Villa Prestige (D-051 Option A · zero new HTML files).
Opens the `travel` category (zero coverage pre-T56) and the
`boutique-hotel` cluster.

Voice contract (IT):
- Editorial-hospitality register: Touring Club Italiano · Conde Nast
  Traveler Italia · Monocle Travel · Departures editorial — never
  travel-blog breezy, never hotel-chain-marketing. Third person
  formal (`Si entra dal viale dei cipressi...`, `Il ricevimento
  attende su appuntamento`); guest addressed only as register
  (`gentile ospite`, `la famiglia in viaggio di nozze`,
  `la coppia internazionale`).
- Concrete detail: Val d'Orcia · Pienza · Siena · UNESCO Heritage
  zone · seicentesco · restauro del 2009 a firma dello studio
  Castellini-Mancini · 8 suites · brigata di 14 persone · spa
  Aqua sotterranea · ristorante con stella Michelin (chef Tommaso
  Brigliadori) · pergolato di glicine · cantina settecentesca.
- Voice anchor `ospitalità di borgo` — register that foregrounds
  the village-hospitality promise: a relais inside a still-living
  Tuscan borgo (not a resort, not a hotel-chain, not a country
  villa for-sale). Load-bearing in headline and every primary
  hospitality band.
- Vocabolario: ospitalità · borgo · relais · brigata · maitre ·
  concierge · pernottamento · soggiorno · spa · degustazione ·
  cantina · pergolato. Mai: prenotazione online · check-in
  immediato · early-bird · resort · all-inclusive.

Differentiation contract vs Villa Prestige (D-054 enforcement):
- Villa is private real-estate advisory: dossier · private viewing ·
  NDA · referente · dimora storica IN VENDITA per acquisto privato ·
  prezzi mai visibili · palette gold-champagne-noir su nero.
- Albergo Borgo is hospitality: pernottamento · spa · ristorante ·
  brigata di sala · cantina aperta agli ospiti · suite NON IN VENDITA
  · tariffa stagionale visibile (alta/bassa) · palette terracotta
  primary + travertino cream + olivo accento (calda toscana, non
  oro-nero metropolitana).
- CTA pattern: Villa = `Richiedi una private viewing` (advisory).
  Albergo Borgo = `Prenota il vostro soggiorno` + `Scrivete alla
  direzione` (hospitality with a name attached).
- Persona: Villa = Vittoria-Belluno-Sernigi anonymous advisor.
  Albergo Borgo = Vittoria Sernigi, direttrice trentennale ·
  membro del Touring Club Italiano · sommelier AIS · property
  affiliata Relais & Châteaux dal 2014 (named, biography, photo
  caption with year of joining the brigade).
"""
from __future__ import annotations

from typing import Any


# Imagery — Unsplash CC0 travel-boutique-hotel pool (interim until
# X.5 curator pack lands · 6 hero/feature URLs reused inline below).
_HERO_COURTYARD = "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=1600&q=80&auto=format&fit=crop"
_SUITE_VIGNA = "https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=1200&q=80&auto=format&fit=crop"
_SUITE_FRANTOIO = "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1200&q=80&auto=format&fit=crop"
_SUITE_POZZO = "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=1200&q=80&auto=format&fit=crop"
_SUITE_CISTERNA = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1200&q=80&auto=format&fit=crop"
_SUITE_TORRE = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200&q=80&auto=format&fit=crop"
_SUITE_CORTILE = "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=1200&q=80&auto=format&fit=crop"
_SUITE_LOGGIA = "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=1200&q=80&auto=format&fit=crop"
_SUITE_CANTINA = "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=1200&q=80&auto=format&fit=crop"
_BORGO_VALDORCIA = "https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?w=1200&q=80&auto=format&fit=crop"
_BORGO_PIENZA = "https://images.unsplash.com/photo-1568822617270-2c1579f8dfe2?w=1200&q=80&auto=format&fit=crop"
_BORGO_MONTALCINO = "https://images.unsplash.com/photo-1517760444937-f6397edcbbcd?w=1200&q=80&auto=format&fit=crop"
_BORGO_CIPRESSI = "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=1200&q=80&auto=format&fit=crop"
_BORGO_CHIANTI = "https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=1200&q=80&auto=format&fit=crop"
_BORGO_PIENZA_PIAZZA = "https://images.unsplash.com/photo-1543429776-2782fc8e1acd?w=1200&q=80&auto=format&fit=crop"
_PORTRAIT_DIRECTOR = "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_MAITRE = "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_CHEF = "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_SOMMELIER = "https://images.unsplash.com/photo-1566753323558-f4e0952af115?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_SPA = "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=900&q=80&auto=format&fit=crop"


ALBERGO_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Il borgo",   "kind": "home"},
        {"slug": "camere",     "label": "Le suite",   "kind": "blog_list"},
        {"slug": "borgo",      "label": "Il territorio", "kind": "about"},
        {"slug": "brigata",    "label": "La brigata", "kind": "team"},
        {"slug": "soggiorno",  "label": "Soggiorno",  "kind": "services"},
        {"slug": "concierge",  "label": "Concierge",  "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":   "B",
        "logo_word":      "Borgo San Marco",
        "logo_subline":   "Relais & Spa · Pienza dal 1612",
        "tag":            "Stagione 2026 · prenotazioni aperte da maggio a ottobre",
        "phone":          "+39 0578 748 124",
        "phone_label":    "Linea diretta concierge",
        "email":          "concierge@borgosanmarco.it",
        "email_label":    "Scrivete alla direzione",
        "address":        "Borgo San Marco di Sopra · 53026 Pienza · Siena",
        "hours_compact":  "Ricevimento 24 ore · check-in dalle 14 · check-out entro le 11",
        "hours_footer_rows": [
            "Ricevimento aperto 24 ore con concierge in sala",
            "Lingue di sala: italiano · english · français · deutsch",
        ],
        "license":        "Codice CITRA 0521-053026-100201 · Cat. Cinque Stelle Lusso · Iscr. Confindustria Alberghi 0428",
        "footer_intro":
            "Borgo San Marco è un relais di otto suite ricavato nella canonica seicentesca "
            "del borgo omonimo, frazione collinare di Pienza affacciata sulla Val d'Orcia "
            "UNESCO. Restauro dello studio Castellini-Mancini del 2009, affiliazione "
            "Relais & Châteaux dal 2014, una stella Michelin per il ristorante "
            "Trebbio dal 2019. L'ospitalità di borgo è la nostra promessa: un "
            "ricevimento intero per otto camere, una brigata di sala di quattordici "
            "persone, e la quiete di un borgo ancora abitato.",

        # Nav reservation CTA (hospitality)
        "nav_cta":         "Prenota il vostro soggiorno",
        "nav_cta_kind":    "appointment",
        "nav_cta_short":   "Prenota",

        # Footer labels
        "foot_studio":   "Il relais",
        "foot_pages":    "Mappa",
        "foot_contact":  "Concierge",
        "foot_offices":  "Sedi",
        "offices_footer_rows": [
            "Borgo San Marco di Sopra · 53026 Pienza · Siena",
            "Tenuta Trebbio · cantina e oliveto · 1,2 km a sud",
        ],
        "office_rows": [
            "Borgo San Marco di Sopra 17 · 53026 Pienza · Siena",
            "Tel +39 0578 748 124 · concierge@borgosanmarco.it",
        ],
        "dossier_label":     "Suite",
        "portfolio_label":   "Pernottamenti / anno",
        "territorio_label":  "Borgo",
        "superficie_label":  "Superficie",
        "provenance_label":  "Vista",
        "access_label":      "Lingue di sala",
        "availability_label": "Stagionalità",
        "price_note":        "Tariffa su richiesta · pacchetti stagionali",
        "nda_required_label": "Riservato",
        "viewing_on_request": "Solo su prenotazione",
        "referent_label":    "Referente in sala",
        "concierge_line_label": "Concierge dedicato",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "cover_location":    "Borgo San Marco di Sopra · Val d'Orcia · UNESCO",
        "cover_image_credit": "Fotografia · Massimo Listri",
        "cover_image":       _HERO_COURTYARD,

        "eyebrow":           "Relais & Spa · Val d'Orcia · Pienza dal 1612",
        "headline":          'Otto suite in un borgo del Seicento. <em>Ospitalità di borgo</em>, una sola stagione l\'anno.',
        "sub":
            "Un relais di otto suite ricavato dalla canonica seicentesca di Borgo "
            "San Marco di Sopra, frazione collinare di Pienza affacciata sulla "
            "Val d'Orcia. Apertura stagionale da maggio a fine ottobre · ricevimento "
            "intero · cucina con stella Michelin · spa Aqua di Borgo nella cisterna "
            "settecentesca · cantina propria.",
        "hero_wordmark":     "Borgo San Marco",
        "hero_location":     "Pienza · Siena · Toscana",
        "hero_counter_label": "Suite",
        "hero_counter_value": "8",
        "hero_series_label": "Stagione",
        "hero_series_title": "2026 · Aprile – Ottobre",
        "hero_series_note":  "Apertura il 18 aprile · chiusura il 27 ottobre · brigata di 14 persone in sala",

        "primary_cta":         "Prenota il vostro soggiorno",
        "primary_cta_href":    "concierge",
        "secondary_cta":       "Scoprite le suite",
        "secondary_cta_href":  "camere",

        # Hero credit cells — list[4] of tuple[2] (label, value)
        "hero_credit_cells": [
            ("Affiliazione",  "Relais & Châteaux"),
            ("Cucina",        "Una stella Michelin"),
            ("Restauro",      "Castellini-Mancini · 2009"),
            ("Apertura",      "Stagionale · 24 settimane"),
        ],

        # Signature suite section — list[6] of dict (keys: slug, image,
        # index, title, territorio, superficie, provenance, availability)
        "signature_label":    "Le suite",
        "signature_heading":  "Le suite della casa, una per ogni stanza del borgo.",
        "signature_intro":
            "Otto suite, ognuna ricavata da un ambiente storico della canonica e "
            "della cantina settecentesca attigua. Nessuna stanza è uguale all'altra; "
            "tutte affacciate sulla Val d'Orcia.",
        "signature": [
            {
                "slug":         "suite-la-vigna",
                "image":        _SUITE_VIGNA,
                "index":        "Suite 01",
                "title":        "La Vigna",
                "territorio":   "Lato ovest · primo piano",
                "superficie":   "62 m² · matrimoniale king",
                "provenance":   "Vista sul vigneto storico di Sangiovese",
                "availability": "Disponibile maggio – settembre",
            },
            {
                "slug":         "suite-il-frantoio",
                "image":        _SUITE_FRANTOIO,
                "index":        "Suite 02",
                "title":        "Il Frantoio",
                "territorio":   "Pianterreno · ala sud",
                "superficie":   "78 m² · matrimoniale + salotto",
                "provenance":   "Vecchia macina del frantoio del 1620 al centro della stanza",
                "availability": "Disponibile tutto l'arco stagionale",
            },
            {
                "slug":         "suite-il-pozzo",
                "image":        _SUITE_POZZO,
                "index":        "Suite 03",
                "title":        "Il Pozzo",
                "territorio":   "Cortile interno · pianterreno",
                "superficie":   "54 m² · matrimoniale standard",
                "provenance":   "Pozzo ottagonale del Seicento nel cortile privato",
                "availability": "Su richiesta · solo coppie",
            },
            {
                "slug":         "suite-la-cisterna",
                "image":        _SUITE_CISTERNA,
                "index":        "Suite 04",
                "title":        "La Cisterna",
                "territorio":   "Ala est · piano interrato",
                "superficie":   "88 m² · letto a baldacchino",
                "provenance":   "Volta della cisterna settecentesca · luce naturale dall'alto",
                "availability": "Su richiesta · luna di miele consigliata",
            },
            {
                "slug":         "suite-la-torre",
                "image":        _SUITE_TORRE,
                "index":        "Suite 05",
                "title":        "La Torre",
                "territorio":   "Torre angolare · secondo piano",
                "superficie":   "70 m² · letto matrimoniale + studio",
                "provenance":   "Vista a 270° sulla Val d'Orcia fino al Monte Amiata",
                "availability": "Disponibile aprile – ottobre",
            },
            {
                "slug":         "suite-il-cortile",
                "image":        _SUITE_CORTILE,
                "index":        "Suite 06",
                "title":        "Il Cortile",
                "territorio":   "Pianterreno · ala nord",
                "superficie":   "65 m² · matrimoniale + giardino privato",
                "provenance":   "Loggetta privata sul pergolato di glicine",
                "availability": "Disponibile maggio – ottobre",
            },
        ],
        "signature_link_all":  "Vedi tutte le otto suite",
        "signature_link_href": "camere",

        # Territory chip-row — list of scalar strings
        "territory_label": "Territorio",
        "territory": [
            "Pienza · Val d'Orcia",
            "Montalcino · cantine del Brunello",
            "Montepulciano · Vino Nobile",
            "San Quirico d'Orcia · vie storiche",
            "Bagno Vignoni · terme medievali",
            "Monte Amiata · escursioni",
            "Siena · Palio in luglio e agosto",
            "Cortona · vie etrusche",
        ],

        # Director / advisor band — single block
        "advisor_label":     "La direzione",
        "advisor_heading":   "Una direttrice che lavora in sala. <em>Trentadue stagioni in albergheria</em>.",
        "advisor_intro":
            "Borgo San Marco è diretto in prima persona da Vittoria Sernigi, "
            "albergatrice toscana classe 1964, allieva del Maestro Casiraghi al "
            "Plaza Athénée di Parigi e del Maestro Cipriani al Cipriani di Venezia. "
            "Trentadue stagioni di albergheria di lusso prima di rilevare il "
            "borgo nel 2008.",
        "advisor_name":      "Vittoria Sernigi",
        "advisor_role":      "Direttrice · membro del Touring Club Italiano · sommelier AIS",
        "advisor_bio":
            "Trentadue anni di albergheria internazionale prima di Pienza: Plaza Athénée "
            "Parigi · Cipriani Venezia · Villa San Michele Fiesole. Membro del Touring "
            "Club Italiano dal 1995, sommelier AIS dal 2002, formatrice alla Scuola "
            "Alberghiera di Siena. In sala ogni mattina alla colazione, ogni sera alla "
            "consegna delle chiavi.",
        "advisor_portrait":  _PORTRAIT_DIRECTOR,
        "advisor_cta":       "Scrivete a Vittoria",
        "advisor_cta_href":  "concierge",

        # Numbers band — list[4] of tuple[2] (counter, label)
        "numbers_label":    "Borgo San Marco in cifre",
        "numbers_heading":  "Una stagione, un ricevimento intero, una brigata.",
        "numbers": [
            ("8",   "Suite · nessuna uguale all'altra"),
            ("14",  "Persone in brigata di sala"),
            ("1",   "Stella Michelin · ristorante Trebbio"),
            ("12",  "Anni di affiliazione Relais & Châteaux"),
        ],
        "numbers_note":
            "Apertura stagionale 18 aprile – 27 ottobre · brigata di sala intera "
            "presente sui 12 turni di servizio · ricevimento 24 ore.",

        # Press band — list of scalar strings (NB: home version, NOT team version)
        "press_label":   "Rassegna",
        "press_intro":   "Borgo San Marco nei viaggi editoriali del 2023-2025",
        "press_items": [
            "Condé Nast Traveler Italia",
            "Touring Magazine",
            "Departures",
            "Monocle Travel",
            "Bell'Italia",
        ],

        # Private band — closing CTA
        "private_label":     "Per i vostri ospiti più cari",
        "private_heading":   "Il borgo intero, una sola famiglia. <em>Esclusiva di otto giorni</em>.",
        "private_intro":
            "Il borgo può essere prenotato in esclusiva per una sola famiglia o un "
            "gruppo ristretto · otto suite riservate, brigata dedicata, ristorante "
            "chiuso al pubblico, cantina aperta agli ospiti. Disponibilità solo su "
            "tre finestre l'anno · scrivere alla direzione almeno sei mesi prima.",
        "private_primary":      "Scrivete alla direzione",
        "private_primary_href": "concierge",
        "private_secondary":    "Scoprite il borgo",
        "private_secondary_href": "borgo",
    },

    # ─── CAMERE (blog_list of suites) ─────────────────────────
    "camere": {
        "eyebrow":          "Otto suite · Borgo San Marco",
        "headline":         "Le suite della casa.",
        "intro":
            "Ogni suite porta il nome di un ambiente storico del borgo · "
            "ognuna è stata riprogettata dallo studio Castellini-Mancini "
            "nel 2009 mantenendo la pianta originale del Seicento.",
        "lead_image":       _HERO_COURTYARD,
        "filter_label":     "Affina la ricerca",
        "filter_groups": [
            {"label": "Vista", "options": ["Vigneto", "Cortile", "Borgo", "Val d'Orcia", "Pergolato"]},
            {"label": "Letti", "options": ["Matrimoniale king", "Matrimoniale + salotto", "Letto a baldacchino", "Suite con studio"]},
            {"label": "Stagione", "options": ["Apertura aprile", "Disponibile maggio – settembre", "Solo alta stagione"]},
        ],
        "sort_label":       "Ordina",
        "sort_options": [
            "Per superficie · dalla più ampia",
            "Per stagionalità",
            "Per numero ospiti",
            "Per quiete",
        ],
        "result_count":     "8 suite disponibili nella stagione 2026",
        "result_subtitle":  "Ricevimento intero per le otto stanze · brigata di sala dedicata.",
        "footer_note_label": "Tariffe",
        "footer_note":
            "Tutte le suite includono colazione in sala, accesso illimitato alla "
            "spa Aqua di Borgo e una degustazione di tre vini in cantina su "
            "prenotazione. Tariffa stagionale comunicata in fase di richiesta.",
    },

    # ─── BORGO (about · territorio del relais) ────────────────
    "borgo": {
        "eyebrow":          "Val d'Orcia · UNESCO",
        "headline":         "Un borgo del Seicento ancora abitato.",
        "intro":
            "Borgo San Marco di Sopra è una frazione collinare di Pienza · 41 "
            "abitanti residenti · piazza centrale del 1571 · canonica del 1612 "
            "(oggi relais) · cantina del Settecento (oggi spa). Il borgo è ancora "
            "abitato dalle stesse sei famiglie da quattro generazioni; il relais "
            "ne è l'ospite più recente, dal 2009.",

        "statement_label":   "La nostra ospitalità",
        "statement_heading": "Otto suite, una sola brigata, un borgo intero.",
        "statement_text":
            "Ospitalità di borgo significa che il ricevimento è uno solo per "
            "tutte e otto le suite, che la brigata di sala conosce ogni ospite "
            "per nome dal secondo giorno, e che il borgo resta un borgo (con "
            "i suoi 41 abitanti) anche quando voi siete ospiti. Non siamo un "
            "resort. Non siamo una catena. Non siamo un hotel di città.",

        "territories_label":   "I dintorni",
        "territories_heading": "Sei territori a meno di un'ora dal borgo.",
        "territories_intro":
            "I dintorni della Val d'Orcia sono parte dell'ospitalità del relais: "
            "ogni territorio ha un referente in sala dedicato alla scoperta · "
            "vino, terme, percorsi etruschi, escursioni sull'Amiata, opera al "
            "Palio di Siena.",
        "territories": [
            {
                "image":      _BORGO_VALDORCIA,
                "name":       "Val d'Orcia",
                "region":     "Pienza · San Quirico · Bagno Vignoni",
                "history":    "Patrimonio UNESCO dal 2004 · paesaggio rinascimentale codificato dal Lorenzetti. Cipressi, crete e poderi.",
                "architects": "Cipressi lineari · vie cave etrusche",
                "count":      "12 km",
                "since":      "Visita: 1 ora · referente Federico in sala",
            },
            {
                "image":      _BORGO_MONTALCINO,
                "name":       "Montalcino",
                "region":     "Cantine storiche del Brunello",
                "history":    "Cantine storiche del Brunello di Montalcino DOCG · Biondi-Santi, Casanova di Neri, Il Poggione. Degustazioni private su appuntamento.",
                "architects": "Pievi medioevali · castelli senesi",
                "count":      "28 km",
                "since":      "Visita: 1 giornata · referente sommelier AIS",
            },
            {
                "image":      _BORGO_PIENZA,
                "name":       "Pienza · la città ideale",
                "region":     "Piazza Pio II · cattedrale · Palazzo Piccolomini",
                "history":    "La città ideale del Rinascimento progettata da Bernardo Rossellino per Pio II nel 1462. Piazza, cattedrale, Palazzo Piccolomini, vista sull'Amiata.",
                "architects": "Bernardo Rossellino · 1459-1462",
                "count":      "1,8 km",
                "since":      "Visita: 2 ore a piedi · concierge accompagna su richiesta",
            },
            {
                "image":      _BORGO_CHIANTI,
                "name":       "Montepulciano",
                "region":     "Vino Nobile · cantine sotterranee",
                "history":    "Cantine sotterranee scavate nel tufo, alcune del XIV secolo. Degustazione del Vino Nobile di Montepulciano DOCG · cantine Avignonesi, Salcheto, Boscarelli.",
                "architects": "Antonio da Sangallo il Vecchio · Vignola",
                "count":      "32 km",
                "since":      "Visita: 1 giornata · referente sommelier AIS",
            },
            {
                "image":      _BORGO_CIPRESSI,
                "name":       "Bagno Vignoni",
                "region":     "Terme libere del Quattrocento",
                "history":    "Piazza-vasca termale del Quattrocento, l'unica al mondo. Acqua sulfurea a 49°C affiorante dalla roccia, libera all'accesso. Cena in trattoria sulla piazza con Caterina la cuoca.",
                "architects": "Vasca naturale · sec. XV",
                "count":      "8 km",
                "since":      "Visita: 1 mezza giornata · referente di sala Federico",
            },
            {
                "image":      _BORGO_PIENZA_PIAZZA,
                "name":       "Monte Amiata",
                "region":     "Vulcano spento · faggete · sciovia",
                "history":    "Vulcano spento (1.738 m). Faggete secolari, sentieri CAI, sciovia in inverno. Castagnata di novembre nel borgo di Castiglione d'Orcia.",
                "architects": "Sentieri CAI · 4 vette segnate",
                "count":      "38 km",
                "since":      "Visita: 1 giornata · guida alpina su prenotazione",
            },
        ],
        "territory_card_cta":      "Pianifichiamo insieme · scrivete alla direzione",
        "territory_card_cta_href": "concierge",

        "referent_label":   "Il referente in sala",
        "referent_heading": "Un solo referente per tutto il soggiorno.",
        "referent_text":
            "Dal momento dell'arrivo, ogni ospite ha un referente unico in sala — "
            "il maitre Federico Bonechi o la sommelier Anna Ricci a seconda della "
            "stagione. Il referente accompagna tutta la prenotazione: prenotazione "
            "del ristorante, dei massaggi in spa, delle degustazioni in cantina, "
            "delle escursioni nei dintorni.",

        "stats_label":  "Borgo San Marco · cifre del 2025",
        # list[4] of tuple[2]
        "stats": [
            ("12",  "Anni di affiliazione Relais & Châteaux"),
            ("162", "Notti aperte all'anno"),
            ("8",   "Suite · stagione 2026"),
            ("41",  "Abitanti residenti del borgo"),
        ],
    },

    # ─── BRIGATA (team · staff in sala) ───────────────────────
    "brigata": {
        "eyebrow":       "La brigata · 14 persone in sala",
        "headline":      "Una stessa brigata da dodici stagioni.",
        "intro":
            "La brigata di Borgo San Marco è composta da quattordici persone, di "
            "cui dieci tornano ogni stagione dal 2014. Ricevimento, sala, "
            "ristorante, spa, cantina · una sola brigata per otto suite.",

        "director_label":       "Direzione",
        "director_name":        "Vittoria Sernigi",
        "director_role":        "Direttrice · titolare dal 2008 · sommelier AIS · TCI",
        "director_text":
            "Vittoria Sernigi ha rilevato Borgo San Marco nel 2008 dopo trentadue "
            "stagioni di albergheria internazionale tra Parigi, Venezia e Fiesole. "
            "Diploma alla Scuola Alberghiera Internazionale di Lausanne (1985), "
            "perfezionamento in management alberghiero a Cornell. Membro del "
            "Touring Club Italiano dal 1995, sommelier AIS dal 2002.",
        "director_portrait":    _PORTRAIT_DIRECTOR,
        "director_quote":
            "L'ospitalità di borgo è la sola ospitalità che conosco. È la più "
            "lenta, è la più pretenziosa, è la più gratificante.",
        "director_quote_attribution": "Vittoria Sernigi · intervista a Touring · 2024",

        "advisors_label":   "La brigata di sala",
        "advisors_heading": "Quattro referenti, dieci stagionali · una sola sala.",
        "advisors_intro":
            "Quattro referenti seniori conducono la sala. Le decisioni di servizio "
            "passano dalla loro decisione, mai dall'algoritmo di una catena.",
        # list[4] of dict (portrait, name, role, bio, territories, since, langs)
        "advisors": [
            {
                "portrait":    _PORTRAIT_MAITRE,
                "name":        "Federico Bonechi",
                "role":        "Maitre di sala · referente unico ospiti",
                "bio":
                    "Maitre di sala dal 2009 · dieci stagioni a Borgo San Marco. "
                    "Diplomato all'Alberghiero di Chianciano · esperienza al Castello "
                    "Banfi e al Plaza Athénée. Conosce il nome di ogni ospite dal "
                    "secondo giorno.",
                "territories": "Sala · ricevimento · concierge",
                "since":       "In brigata dal 2014",
                "langs":       "Italiano · English · Français",
            },
            {
                "portrait":    _PORTRAIT_CHEF,
                "name":        "Tommaso Brigliadori",
                "role":        "Chef · ristorante Trebbio · una stella Michelin",
                "bio":
                    "Chef del ristorante Trebbio dal 2017 · stella Michelin dal 2019. "
                    "Formato all'Albereta sotto Gualtiero Marchesi, perfezionato da "
                    "Bottura a Modena. Cucina del territorio: pici, picci e pinoli, "
                    "agnello di Zeri, fagioli zolfini, caciotta di Pienza.",
                "territories": "Cucina · cantina · giardino degli orti",
                "since":       "In brigata dal 2017",
                "langs":       "Italiano · English",
            },
            {
                "portrait":    _PORTRAIT_SOMMELIER,
                "name":        "Anna Ricci",
                "role":        "Sommelier AIS · responsabile cantina",
                "bio":
                    "Sommelier AIS dal 2008 · responsabile cantina dal 2015. La "
                    "cantina ospita 4.200 etichette tra Brunello, Vino Nobile, Chianti "
                    "Classico e una piccola collezione di Champagne. Degustazioni "
                    "private in cantina per ospiti, due volte la settimana.",
                "territories": "Cantina · degustazioni · accompagnamento ristorante",
                "since":       "In brigata dal 2015",
                "langs":       "Italiano · English · Deutsch",
            },
            {
                "portrait":    _PORTRAIT_SPA,
                "name":        "Caterina Sandri",
                "role":        "Responsabile Aqua di Borgo Spa",
                "bio":
                    "Responsabile della spa dal 2018 · diploma in idroterapia "
                    "all'Università di Siena, formazione in spa management presso "
                    "il Six Senses Toscana. La spa Aqua di Borgo è ricavata nella "
                    "cisterna settecentesca · solo trattamenti su appuntamento.",
                "territories": "Spa Aqua di Borgo · trattamenti · piscina sotterranea",
                "since":       "In brigata dal 2018",
                "langs":       "Italiano · English",
            },
        ],

        "partners_label":   "I produttori del borgo",
        "partners_heading": "I fornitori storici della tavola.",
        "partners_intro":
            "Le materie prime del ristorante Trebbio arrivano da fornitori del "
            "raggio di trenta chilometri intorno al borgo, salvo l'olio (di "
            "produzione propria) e il pane (panetteria del borgo a 200 metri).",
        # list[5] of tuple[2] (name, role)
        "partners": [
            ("Fattoria Trebbio",         "Olio EVO di proprietà · oliveto storico a 1,2 km dal borgo"),
            ("Caseificio Castelmuzio",   "Pecorino di Pienza · caciotta · ricotta · 8 km da Pienza"),
            ("Azienda agricola Falcorosso", "Manzo di Chianina · agnello di Zeri · pollame · 12 km"),
            ("Forno di Pienza · Lorenzini", "Pane toscano · schiacciate · grissini · 1,8 km dal borgo"),
            ("Erbario di Sant'Anna",     "Erbe officinali · tisaneria della spa Aqua · monastero a 18 km"),
        ],

        "press_label":   "Rassegna · brigata e cucina",
        "press_heading": "Premi e menzioni della brigata.",
        # list[5] of dict (magazine, issue, title, byline) — DIFFERENT shape from home.press_items!
        "press_items": [
            {
                "magazine": "Guida Michelin Italia",
                "issue":    "Ed. 2019 – conferma 2025",
                "title":    "Una stella · ristorante Trebbio · cucina toscana di territorio",
                "byline":   "Redazione Michelin",
            },
            {
                "magazine": "Touring Magazine",
                "issue":    "Aprile 2024",
                "title":    "Vittoria Sernigi · ritratto della direttrice di borgo",
                "byline":   "Maria Sirotti",
            },
            {
                "magazine": "Gambero Rosso",
                "issue":    "Gennaio 2025 · Tre forchette",
                "title":    "Trebbio di Borgo San Marco · tre forchette confermate",
                "byline":   "Eleonora Cozzella",
            },
            {
                "magazine": "Condé Nast Traveler Italia",
                "issue":    "Maggio 2023 · Gold List",
                "title":    "Borgo San Marco · Top 50 Italia",
                "byline":   "Caterina Cesari",
            },
            {
                "magazine": "Bell'Italia",
                "issue":    "Settembre 2024",
                "title":    "Le 12 grandi case d'ospitalità della Val d'Orcia",
                "byline":   "Giovanni Rajberti",
            },
        ],

        "numbers_label": "La brigata in cifre",
        # list[6] of tuple[2]
        "numbers": [
            ("14", "Persone in brigata di sala"),
            ("10", "Stagionali ricorrenti dal 2014"),
            ("32", "Anni di esperienza della direttrice"),
            ("4",  "Lingue di sala (IT · EN · FR · DE)"),
            ("12", "Anni di affiliazione Relais & Châteaux"),
            ("4200", "Etichette in cantina · responsabile Anna Ricci AIS"),
        ],

        "visit_label":         "Per scrivere alla brigata",
        "visit_heading":       "Una sola brigata, una sola sala.",
        "visit_text":
            "Per richieste su menù, allergie, vino, escursioni o trattamenti spa "
            "scrivete direttamente alla brigata: rispondiamo entro la giornata "
            "lavorativa successiva. Vittoria firma personalmente la conferma "
            "della prenotazione.",
        "visit_primary":       "Scrivete alla direzione",
        "visit_primary_href":  "concierge",
    },

    # ─── SOGGIORNO (services · l'esperienza del soggiorno) ────
    "soggiorno": {
        "eyebrow":      "L'esperienza · cinque tempi del soggiorno",
        "headline":     "Cinque tempi · da Pienza al rientro.",
        "intro":
            "Il soggiorno a Borgo San Marco si articola in cinque tempi · "
            "l'arrivo, la sala, la spa, la cantina e l'uscita verso il "
            "territorio. Ogni tempo è curato dal referente di sala.",

        "process_label":   "Cinque tempi",
        "process_heading": "Come si svolge un soggiorno.",
        "process_intro":
            "La narrazione del soggiorno è una sola, dal momento in cui scrivete "
            "alla direzione fino al ritorno a casa.",
        # list[5] of dict (n, title, text, duration)
        "process": [
            {
                "n":        "01",
                "title":    "La conferma",
                "text":
                    "Risposta personale di Vittoria entro 24 ore dalla richiesta · "
                    "scelta della suite, della finestra stagionale, eventuali "
                    "richieste speciali (menù, allergie, escursioni).",
                "duration": "1 giornata",
            },
            {
                "n":        "02",
                "title":    "L'arrivo",
                "text":
                    "Ricevimento dalle 14 · trasferimento dall'aeroporto di "
                    "Firenze su richiesta · benvenuto in piazza del borgo con "
                    "vino del territorio · presentazione del referente di sala.",
                "duration": "2 ore",
            },
            {
                "n":        "03",
                "title":    "La sala e la cantina",
                "text":
                    "Cena al ristorante Trebbio · menù del territorio in cinque "
                    "tempi · abbinamento vini commentato dalla sommelier · cantina "
                    "aperta dopo cena per chi desidera prolungare la serata.",
                "duration": "Una sera per soggiorno",
            },
            {
                "n":        "04",
                "title":    "La spa e il territorio",
                "text":
                    "Mezza giornata in spa Aqua di Borgo (cisterna settecentesca) "
                    "· nuoto, bagno turco, sauna, idromassaggio nella vasca naturale · "
                    "trattamenti su appuntamento · escursione di mezza giornata in "
                    "Val d'Orcia con il referente.",
                "duration": "Una mezza giornata",
            },
            {
                "n":        "05",
                "title":    "L'uscita",
                "text":
                    "Check-out entro le 11 · colazione tarda fino alle 10:30 in "
                    "pergolato di glicine · regalo di partenza (olio della Fattoria "
                    "Trebbio · piccolo libro del borgo) · accompagnamento al rientro.",
                "duration": "1 mezza giornata",
            },
        ],

        "testimonial_label":  "La voce dell'ospite",
        "testimonial_text":
            "«Tre soggiorni in tre stagioni diverse, sempre la stessa brigata, "
            "sempre Federico al ricevimento. È raro, in Italia, trovare un "
            "albergo dove la promessa fatta la prima volta resta vera anche "
            "alla terza visita.»",
        "testimonial_author": "Giorgio Borghi · Milano · ospite dal 2018",

        "faq_label":    "Domande ricorrenti dalla direzione",
        # list[6] of dict (q, a)
        "faq_items": [
            {
                "q": "L'albergo è aperto tutto l'anno?",
                "a":
                    "No. Borgo San Marco apre dal 18 aprile al 27 ottobre 2026 — "
                    "ventiquattro settimane di stagione. La chiusura invernale "
                    "permette la manutenzione delle suite e il riposo della "
                    "brigata di sala. Nessuna eccezione, neanche per Capodanno.",
            },
            {
                "q": "Si può prenotare il borgo intero per una famiglia?",
                "a":
                    "Sì · su tre finestre l'anno (giugno, settembre, fine ottobre). "
                    "Otto suite riservate · ristorante chiuso al pubblico esterno · "
                    "brigata dedicata. Scrivere alla direzione almeno sei mesi "
                    "prima della data desiderata.",
            },
            {
                "q": "Si possono organizzare matrimoni nel borgo?",
                "a":
                    "Solo matrimoni intimi · massimo 36 ospiti · cerimonia civile "
                    "nella loggia del piano nobile · cena nel pergolato di glicine. "
                    "Non organizziamo matrimoni con più di 36 ospiti per "
                    "preservare la dimensione del borgo. Scrivere a Vittoria "
                    "almeno un anno prima.",
            },
            {
                "q": "Si accettano cani di piccola taglia?",
                "a":
                    "Sì · su richiesta · in due suite del pianterreno (Il Frantoio "
                    "e Il Pozzo). Supplemento di 30 € a notte · ciotola, cuccia e "
                    "biscotti compresi. Pet sitter del borgo disponibile su "
                    "appuntamento per le ore della cena al ristorante.",
            },
            {
                "q": "Posso visitare la cantina anche se non sono ospite del ristorante?",
                "a":
                    "Sì · la cantina è aperta agli ospiti del borgo due volte "
                    "alla settimana (martedì e giovedì pomeriggio, ore 17–19) per "
                    "una degustazione di tre vini con Anna · prenotazione "
                    "obbligatoria al ricevimento.",
            },
            {
                "q": "C'è il wi-fi nelle suite?",
                "a":
                    "Sì · linea in fibra a 1 Gbit/s · disponibile in tutte le otto "
                    "suite, in sala e in spa. Su richiesta è possibile attivare "
                    "una modalità digital detox: la suite resta senza connessione "
                    "per tutto il soggiorno · cassetto per i dispositivi all'arrivo.",
            },
        ],

        "cta_label":         "Per cominciare",
        "cta_heading":       "<em>Una stagione corta</em>, una sola brigata.",
        "cta_text":
            "Le finestre stagionali del 2026 si aprono il 18 aprile · le suite "
            "più richieste (La Vigna, Il Cortile, La Torre) si esauriscono "
            "entro maggio. Scrivete alla direzione per la prenotazione.",
        "cta_primary":       "Prenota il vostro soggiorno",
        "cta_primary_href":  "concierge",
    },

    # ─── CONCIERGE (contact · concierge dedicato) ─────────────
    "concierge": {
        "eyebrow":      "Concierge dedicato · Vittoria Sernigi",
        "headline":     "Scrivete alla direzione.",
        "intro":
            "Per la richiesta di prenotazione, le date di esclusiva del borgo, "
            "i pacchetti stagionali e qualsiasi domanda sul soggiorno scrivete "
            "direttamente alla direzione. Vittoria risponde personalmente entro "
            "la giornata lavorativa successiva.",

        "phone_label":   "Linee dirette",
        "phone_intro":
            "Ricevimento aperto 24 ore · concierge dedicato in sala in turno "
            "continuo · numero diretto per emergenze.",
        # list[4] of tuple[2]
        "phone_rows": [
            ("Concierge",    "+39 0578 748 124"),
            ("Direzione",    "+39 0578 748 100 · solo Vittoria"),
            ("Ristorante",   "+39 0578 748 130 · prenotazioni Trebbio"),
            ("Spa",          "+39 0578 748 145 · prenotazioni Aqua"),
        ],

        "form_section_label": "Richiesta di prenotazione",
        "form_section_intro":
            "Indicate le date desiderate, la suite preferita (o l'esclusiva "
            "del borgo) e eventuali richieste speciali. Vittoria risponde "
            "personalmente alla mail con la conferma o una proposta "
            "alternativa entro 24 ore.",
        "form_helper_required":  "Campi indicati con · obbligatori",
        "form_submit_button":    "Invia richiesta alla direzione",
        "form_submit_note":
            "La conferma definitiva avviene tramite caparra del 30% via "
            "bonifico bancario · saldo all'arrivo al ricevimento.",
        # list[10] of dict (label, name, type, required, options)
        "form_fields": [
            {"label": "Nome e cognome",         "name": "name",       "type": "text",     "required": True,  "options": []},
            {"label": "Email · risposta diretta", "name": "email",    "type": "email",    "required": True,  "options": []},
            {"label": "Telefono",                "name": "phone",     "type": "tel",      "required": False, "options": []},
            {"label": "Data di arrivo",          "name": "arrival",   "type": "date",     "required": True,  "options": []},
            {"label": "Data di partenza",        "name": "departure", "type": "date",     "required": True,  "options": []},
            {"label": "Numero di ospiti",        "name": "guests",    "type": "number",   "required": True,  "options": []},
            {"label": "Suite preferita",         "name": "suite",     "type": "select",   "required": False,
             "options": ["La Vigna", "Il Frantoio", "Il Pozzo", "La Cisterna", "La Torre", "Il Cortile", "Esclusiva del borgo · 8 suite", "Senza preferenza"]},
            {"label": "Pacchetto",               "name": "package",   "type": "select",   "required": False,
             "options": ["Soggiorno breve · 2 notti", "Soggiorno classico · 4 notti", "Soggiorno lungo · 7 notti", "Esclusiva del borgo · 5 notti", "Matrimonio intimo"]},
            {"label": "Allergie o richieste alimentari", "name": "allergies", "type": "text", "required": False, "options": []},
            {"label": "Note alla direzione",     "name": "notes",     "type": "textarea", "required": False, "options": []},
        ],

        "offices_label":   "Indirizzi",
        "offices_heading": "Il borgo e i poderi.",
        "offices_intro":
            "Il borgo è raggiungibile in auto da Firenze (1h45) o Roma (2h30) · "
            "trasferimento dall'aeroporto di Firenze o dalla stazione di "
            "Chiusi-Chianciano su richiesta.",
        # list[3] of dict (role, city, address, hours, email)
        "offices": [
            {
                "role":     "Borgo · ricevimento",
                "city":     "Pienza · Siena",
                "address":  "Borgo San Marco di Sopra 17 · 53026 Pienza",
                "hours":    "Ricevimento 24 ore · check-in 14–22 · check-out entro le 11",
                "email":    "concierge@borgosanmarco.it",
            },
            {
                "role":     "Fattoria Trebbio · cantina e oliveto",
                "city":     "Pienza · Siena · 1,2 km dal borgo",
                "address":  "Strada provinciale 146 · 53026 Pienza",
                "hours":    "Cantina · martedì e giovedì 17–19 · degustazioni su prenotazione",
                "email":    "cantina@borgosanmarco.it",
            },
            {
                "role":     "Aqua di Borgo · spa",
                "city":     "Cisterna settecentesca · piano interrato",
                "address":  "Borgo San Marco di Sopra 17 · piano –1",
                "hours":    "Spa 9–13 · 15–20 · trattamenti su appuntamento",
                "email":    "spa@borgosanmarco.it",
            },
        ],

        "press_contact_label": "Stampa e media",
        "press_contact_text":
            "Per richieste editoriali, prove servizio e interviste alla "
            "direzione · scrivere a Maria Bonelli, ufficio stampa di "
            "Vittoria Sernigi, includendo testata e tema.",
        "press_contact_email": "stampa@borgosanmarco.it",
    },

    # ─── POSTS (8 suites · the room cards consumed by camere blog_list) ─
    "posts": [
        {
            "slug":         "suite-la-vigna",
            "image":        _SUITE_VIGNA,
            "kicker":       "Suite 01",
            "title":        "La Vigna",
            "date":         "Stagione 2026 · aprile – ottobre",
            "author":       "Borgo San Marco",
            "read_min":     "62 m²",
            "lede":
                "La suite affacciata sul vigneto storico di Sangiovese di proprietà · "
                "primo piano dell'ala ovest · letto matrimoniale king · soffitto a "
                "travi originali del Seicento.",
            "footer_strap": "Disponibile maggio – settembre · vista vigneto",
            # list of 2-tuples (k, v)
            "meta_rows": [
                ("Piano",         "Primo · ala ovest"),
                ("Letti",         "Matrimoniale king + chaise longue"),
                ("Superficie",    "62 m² + 8 m² di loggetta"),
                ("Vista",         "Vigneto storico di Sangiovese · oliveto"),
                ("Bagno",         "Marmo travertino · doccia walk-in + vasca"),
                ("Inclusioni",    "Colazione · spa · degustazione cantina"),
                ("Stagionalità",  "Disponibile maggio – settembre"),
            ],
            # list of 2-tuples (kind, text)
            "body": [
                ("p", "La Vigna è la suite più richiesta della casa · affaccio diretto sul vigneto storico di Sangiovese che dà i grappoli al Brunello di proprietà della Fattoria Trebbio. Soffitto a travi originali del Seicento, pavimento in cotto patinato, mobili recuperati dalle case del borgo."),
                ("p", "La loggetta privata di 8 m² è arredata con un divanetto in vimini e un tavolino in pietra serena · perfetta per la colazione a due o per il bicchiere serale di Brunello (sempre incluso, dalla cantina di Anna)."),
                ("h3", "Il vigneto storico"),
                ("p", "Il vigneto di proprietà della Fattoria Trebbio si stende su 4,2 ettari a sud del borgo, esposizione est-sud-est. Vendemmia manuale in ottobre · vinificazione in piccoli tini d'acciaio · affinamento in botte grande di rovere · imbottigliamento all'azienda. Il Brunello porta la stessa firma del borgo."),
                ("ul", ["Ospitanza · due adulti · su richiesta culla per neonato", "Wifi · fibra 1 Gbit/s · linea diretta sulla rete del borgo", "Climatizzazione · indipendente, regolabile dalla suite", "Cassaforte · digitale · per oggetti di valore", "TV · 55 pollici · canali internazionali su richiesta"]),
                ("p", "La suite La Vigna è disponibile da maggio a fine settembre. Per la stagione 2026 è prenotabile esclusivamente in pacchetto di almeno tre notti."),
            ],
        },
        {
            "slug":         "suite-il-frantoio",
            "image":        _SUITE_FRANTOIO,
            "kicker":       "Suite 02",
            "title":        "Il Frantoio",
            "date":         "Stagione 2026 · tutto l'arco",
            "author":       "Borgo San Marco",
            "read_min":     "78 m²",
            "lede":
                "La suite più ampia · pianterreno dell'ala sud · al centro della "
                "stanza la vecchia macina del frantoio del 1620 conservata come "
                "elemento architettonico.",
            "footer_strap": "Disponibile aprile – ottobre · pianterreno ala sud",
            "meta_rows": [
                ("Piano",         "Pianterreno · ala sud"),
                ("Letti",         "Matrimoniale + salotto separato"),
                ("Superficie",    "78 m² + 12 m² di patio"),
                ("Vista",         "Cortile interno con macina del 1620"),
                ("Bagno",         "Marmo bianco · vasca freestanding + doccia"),
                ("Inclusioni",    "Colazione · spa · degustazione cantina + olio"),
                ("Stagionalità",  "Disponibile tutta la stagione"),
            ],
            "body": [
                ("p", "Il Frantoio è la più grande delle otto suite · 78 m² di pianta più 12 m² di patio privato sul cortile interno. La macina circolare del frantoio originale del 1620 è stata conservata al centro della stanza come elemento architettonico — non funzionante ma intatta, in pietra serena."),
                ("p", "La suite include una piccola cantina privata con sei bottiglie del Brunello della Fattoria Trebbio (vendemmie 2018-2020) e una bottiglia di Olio EVO dell'oliveto storico · gli ospiti possono assaggiare a piacimento e si fattura solo a fine soggiorno."),
                ("h3", "Il frantoio storico"),
                ("p", "Il frantoio originale era in funzione dal 1620 fino al 1968, quando l'olio della Fattoria Trebbio iniziò a essere lavorato al frantoio comune di Pienza. La macina della suite è una delle due originarie · l'altra è esposta nel museo della casa, accanto al cortile."),
                ("ul", ["Ospitanza · due adulti + un bambino sul divano-letto", "Wifi · fibra 1 Gbit/s", "Climatizzazione · indipendente, doppia zona stanza/salotto", "Patio · 12 m² con tavolino e poltrone in ferro battuto", "Mini-cantina privata · 6 bottiglie Brunello + 1 bottiglia olio EVO"]),
                ("p", "Il Frantoio è disponibile per tutta la stagione aperta. Prenotazione di almeno due notti."),
            ],
        },
        {
            "slug":         "suite-il-pozzo",
            "image":        _SUITE_POZZO,
            "kicker":       "Suite 03",
            "title":        "Il Pozzo",
            "date":         "Stagione 2026 · su richiesta",
            "author":       "Borgo San Marco",
            "read_min":     "54 m²",
            "lede":
                "Suite più riservata · pianterreno con accesso diretto al cortile "
                "interno del Seicento · al centro del cortile il pozzo ottagonale "
                "originale del 1612.",
            "footer_strap": "Su richiesta · solo coppie · cortile privato",
            "meta_rows": [
                ("Piano",         "Pianterreno · cortile interno"),
                ("Letti",         "Matrimoniale standard"),
                ("Superficie",    "54 m² + cortile privato 28 m²"),
                ("Vista",         "Cortile ottagonale con pozzo del 1612"),
                ("Bagno",         "Pietra serena · doccia walk-in"),
                ("Inclusioni",    "Colazione · spa · cantina · cortile"),
                ("Stagionalità",  "Su richiesta · solo coppie · animali ammessi"),
            ],
            "body": [
                ("p", "Il Pozzo è la suite più riservata della casa · accesso unicamente dal cortile interno, nessun affaccio sull'esterno del borgo. Il pozzo ottagonale del 1612 è ancora funzionante (acqua dolce dalla falda di San Quirico) e dà ombra a un piccolo cortile di 28 m² ad uso esclusivo della suite."),
                ("p", "Questa suite è offerta solo a coppie · senza bambini · e ammette piccoli cani di taglia inferiore ai 10 kg su richiesta (supplemento di 30 € a notte, ciotola e cuccia incluse)."),
                ("h3", "Il pozzo ottagonale"),
                ("p", "Il pozzo ottagonale è uno dei tre pozzi del borgo · è l'unico ancora attivo. Ottagonale come la cupola di Brunelleschi, di cui Pio II era ammiratore. Costruito nel 1612 dallo stesso muratore che alzò la canonica · firma scolpita all'interno della bocca del pozzo, illeggibile dal 1923 ma documentata in un libretto del 1898 conservato in canonica."),
                ("ul", ["Ospitanza · due adulti · niente bambini", "Cani piccoli ammessi · supplemento 30 €/notte", "Cortile privato · 28 m² con tavolo in ferro · ombra del pozzo", "Wifi · fibra 1 Gbit/s", "Climatizzazione · indipendente"]),
                ("p", "Il Pozzo è disponibile solo su richiesta diretta alla direzione. Soggiorno minimo di tre notti."),
            ],
        },
        {
            "slug":         "suite-la-cisterna",
            "image":        _SUITE_CISTERNA,
            "kicker":       "Suite 04",
            "title":        "La Cisterna",
            "date":         "Stagione 2026 · su richiesta",
            "author":       "Borgo San Marco",
            "read_min":     "88 m²",
            "lede":
                "Suite ricavata nella volta della cisterna settecentesca · "
                "piano interrato · letto a baldacchino · luce naturale dall'alto "
                "attraverso il lucernario originale del 1742.",
            "footer_strap": "Su richiesta · luna di miele consigliata",
            "meta_rows": [
                ("Piano",         "Piano interrato (–1) · ala est"),
                ("Letti",         "Matrimoniale + baldacchino in noce"),
                ("Superficie",    "88 m² · soffitto a volta 4,2 m"),
                ("Vista",         "Lucernario zenitale · niente affaccio esterno"),
                ("Bagno",         "Pietra travertino · vasca a forma di cisterna"),
                ("Inclusioni",    "Colazione · spa · cantina · esperienza notturna"),
                ("Stagionalità",  "Su richiesta · luna di miele consigliata"),
            ],
            "body": [
                ("p", "La Cisterna è la suite più ricercata del borgo · ricavata nella volta della cisterna settecentesca, piano interrato, soffitto a 4,2 metri di altezza. La luce naturale entra solo dal lucernario zenitale del 1742 (originale) · di notte il cielo stellato della Val d'Orcia entra direttamente nella stanza."),
                ("p", "La cisterna originale raccoglieva l'acqua piovana del tetto della canonica fino al 1923, quando il borgo fu collegato all'acquedotto comunale. Il restauro Castellini-Mancini del 2009 ha conservato la curvatura originale e l'iscrizione murata del proprietario settecentesco (Giovan Pietro Buonsignori, 1742)."),
                ("h3", "Il letto a baldacchino"),
                ("p", "Il letto è un pezzo storico · baldacchino in noce massello di Pratomagno, ferro battuto a mano dal fabbro del borgo (Mario Calzini, 1971-2018, oggi suo nipote Luca prosegue la bottega). Tessuti del baldacchino in lino di Bonotto. Lampade a olio sostituite con piccole luci LED a temperatura calda."),
                ("ul", ["Ospitanza · due adulti · niente bambini", "Wifi · fibra 1 Gbit/s · nessuna ricezione 4G nel locale interrato", "Climatizzazione · indipendente, temperatura costante 20 °C anche d'estate", "Vasca · in pietra travertino · forma a cisterna", "Esperienza notturna · su prenotazione apertura del lucernario con osservatorio astronomico del borgo"]),
                ("p", "La Cisterna è disponibile solo su richiesta diretta · particolarmente consigliata per luna di miele e anniversari. Soggiorno minimo di quattro notti."),
            ],
        },
        {
            "slug":         "suite-la-torre",
            "image":        _SUITE_TORRE,
            "kicker":       "Suite 05",
            "title":        "La Torre",
            "date":         "Stagione 2026 · aprile – ottobre",
            "author":       "Borgo San Marco",
            "read_min":     "70 m²",
            "lede":
                "Suite ricavata nella torre angolare medievale · secondo piano · "
                "vista a 270° sulla Val d'Orcia fino al Monte Amiata · letto "
                "matrimoniale con studio adiacente.",
            "footer_strap": "Disponibile aprile – ottobre · vista 270°",
            "meta_rows": [
                ("Piano",         "Secondo piano · torre angolare"),
                ("Letti",         "Matrimoniale + studio con divano-letto"),
                ("Superficie",    "70 m² + 6 m² studio"),
                ("Vista",         "270° · Val d'Orcia · Monte Amiata · Pienza"),
                ("Bagno",         "Marmo nero · doccia walk-in"),
                ("Inclusioni",    "Colazione · spa · cantina · cannocchiale astronomico"),
                ("Stagionalità",  "Aprile – ottobre · scala 23 gradini"),
            ],
            "body": [
                ("p", "La Torre occupa il secondo piano della torre angolare medievale del borgo · vista a 270° sulla Val d'Orcia (sud-ovest), su Pienza (nord-ovest) e fino al Monte Amiata (sud-est) nelle giornate limpide. Tre finestre originali del Cinquecento con vetri al piombo restaurati."),
                ("p", "Lo studio adiacente di 6 m² è arredato con una scrivania in noce di Pratomagno e una libreria di volumi sulla Val d'Orcia (in italiano e inglese) · perfetto per chi ha bisogno di una mezza giornata di lavoro durante il soggiorno."),
                ("h3", "Il cannocchiale astronomico"),
                ("p", "La torre è dotata di un piccolo cannocchiale astronomico Bresser 90 mm installato all'altezza della finestra ovest · ideale per osservare le costellazioni della Val d'Orcia (zero inquinamento luminoso). Manuale d'uso in cassetto · guida di sera con il referente di sala su prenotazione."),
                ("ul", ["Ospitanza · due adulti + un bambino sul divano-letto dello studio", "Scala · 23 gradini · niente ascensore in torre", "Wifi · fibra 1 Gbit/s", "Climatizzazione · ventilatore a soffitto + apparato indipendente", "Cannocchiale · Bresser 90 mm + manuale + guida su richiesta"]),
                ("p", "La Torre è disponibile da aprile a ottobre. Soggiorno minimo di due notti."),
            ],
        },
        {
            "slug":         "suite-il-cortile",
            "image":        _SUITE_CORTILE,
            "kicker":       "Suite 06",
            "title":        "Il Cortile",
            "date":         "Stagione 2026 · maggio – ottobre",
            "author":       "Borgo San Marco",
            "read_min":     "65 m²",
            "lede":
                "Suite con loggetta privata sul pergolato di glicine · pianterreno "
                "dell'ala nord · giardino privato di 18 m² con tavolino e poltrone.",
            "footer_strap": "Disponibile maggio – ottobre · giardino + pergolato",
            "meta_rows": [
                ("Piano",         "Pianterreno · ala nord"),
                ("Letti",         "Matrimoniale + divano-letto"),
                ("Superficie",    "65 m² + giardino privato 18 m²"),
                ("Vista",         "Pergolato di glicine · giardino privato"),
                ("Bagno",         "Marmo travertino · doccia walk-in"),
                ("Inclusioni",    "Colazione · spa · cantina · giardino privato"),
                ("Stagionalità",  "Maggio – ottobre · glicine in fiore maggio-giugno"),
            ],
            "body": [
                ("p", "Il Cortile ha l'accesso più diretto al pergolato di glicine, anima del borgo · il glicine è stato piantato nel 1924 dalla famiglia Buonsignori, fioritura piena nelle prime tre settimane di maggio. Giardino privato di 18 m² delimitato da un muretto in pietra serena · arredato con due poltroncine in ferro battuto e un tavolino in pietra."),
                ("p", "La colazione in pergolato è una pratica della casa · ogni mattina dalle 8 alle 10:30 il pergolato si trasforma in piccola corte di colazione · ospiti seduti su tavolini bassi, brigata di sala in passaggio continuo · pane di Lorenzini caldo dal forno del borgo, marmellate di rosa canina della direzione, formaggi di Castelmuzio, frutta dei poderi vicini."),
                ("h3", "Il glicine del 1924"),
                ("p", "Il glicine fu piantato nel 1924 da Caterina Buonsignori (1902-1989, ultima della famiglia originaria del borgo) come dono di nozze per la figlia Anna. Da allora è cresciuto fino a coprire l'intero pergolato della corte. La fioritura piena dura tre settimane · prima decade di maggio fino al 25 maggio circa."),
                ("ul", ["Ospitanza · due adulti + un bambino sul divano-letto", "Giardino privato · 18 m² · muretto in pietra serena · arredato", "Wifi · fibra 1 Gbit/s", "Climatizzazione · indipendente", "Colazione · servita in pergolato di glicine ore 8-10:30"]),
                ("p", "Il Cortile è disponibile da maggio a ottobre. Per ammirare il glicine in fiore prenotare nella prima quindicina di maggio."),
            ],
        },
        {
            "slug":         "suite-la-loggia",
            "image":        _SUITE_LOGGIA,
            "kicker":       "Suite 07",
            "title":        "La Loggia",
            "date":         "Stagione 2026 · aprile – ottobre",
            "author":       "Borgo San Marco",
            "read_min":     "82 m²",
            "lede":
                "Suite del piano nobile · loggia rinascimentale aperta su Pienza · "
                "soffitto a cassettoni dipinti del 1671 · letto matrimoniale king "
                "+ studio + bagno padronale.",
            "footer_strap": "Disponibile aprile – ottobre · piano nobile",
            "meta_rows": [
                ("Piano",         "Primo piano nobile · ala ovest"),
                ("Letti",         "Matrimoniale king + studio"),
                ("Superficie",    "82 m² + loggia 14 m²"),
                ("Vista",         "Pienza · cattedrale · Palazzo Piccolomini"),
                ("Bagno",         "Marmo travertino + statuario · vasca + doccia separata"),
                ("Inclusioni",    "Colazione · spa · cantina · cena privata in loggia su richiesta"),
                ("Stagionalità",  "Aprile – ottobre · cerimonia civile in loggia possibile"),
            ],
            "body": [
                ("p", "La Loggia è la suite del piano nobile · 82 m² più una loggia rinascimentale di 14 m² aperta su Pienza · si vede la cattedrale di Bernardo Rossellino del 1462 e Palazzo Piccolomini. Il soffitto a cassettoni dipinti del 1671 è stato restaurato nel 2009 da Mauro Pellegrini, restauratore di Siena."),
                ("p", "La loggia è il luogo della cerimonia civile per i matrimoni intimi del borgo (massimo 36 ospiti). Su richiesta è possibile organizzare una cena privata in loggia per gli ospiti della suite · servizio dello chef Tommaso · prezzo su richiesta."),
                ("h3", "Il soffitto a cassettoni del 1671"),
                ("p", "Il soffitto fu commissionato da Pietro Buonsignori nel 1671 al pittore Domenico Manetti di Siena (1609-1683). Trenta cassettoni dipinti a tempera: vedute della Val d'Orcia, simboli araldici della famiglia, putti vendemmianti. Restauro 2009 ha riportato i colori originali; le dorature sono state confermate in laboratorio."),
                ("ul", ["Ospitanza · due adulti + un bambino sul divano-letto dello studio", "Loggia · 14 m² aperta su Pienza · arredata · cena privata su richiesta", "Wifi · fibra 1 Gbit/s", "Climatizzazione · doppia zona", "Cerimonia civile · in loggia · massimo 36 ospiti · su richiesta"]),
                ("p", "La Loggia è disponibile da aprile a ottobre. Soggiorno minimo di due notti, tre notti per la finestra di cerimonia civile."),
            ],
        },
        {
            "slug":         "suite-la-cantina",
            "image":        _SUITE_CANTINA,
            "kicker":       "Suite 08",
            "title":        "La Cantina",
            "date":         "Stagione 2026 · su richiesta",
            "author":       "Borgo San Marco",
            "read_min":     "92 m²",
            "lede":
                "Suite ricavata nella cantina antica del Settecento (la cantina "
                "operativa è oggi alla Fattoria Trebbio) · piano interrato · "
                "letto matrimoniale + zona soggiorno + cantinetta privata da 12 etichette.",
            "footer_strap": "Su richiesta · ideale per appassionati di vino",
            "meta_rows": [
                ("Piano",         "Piano interrato (–1) · ala sud"),
                ("Letti",         "Matrimoniale king + zona soggiorno"),
                ("Superficie",    "92 m² · soffitto a volta 3,8 m"),
                ("Vista",         "Cantinetta privata vetrata · niente affaccio esterno"),
                ("Bagno",         "Pietra travertino · doccia walk-in panoramica sulla cantina"),
                ("Inclusioni",    "Colazione · spa · 12 etichette nella cantinetta privata · degustazione guidata"),
                ("Stagionalità",  "Su richiesta · ideale autunno"),
            ],
            "body": [
                ("p", "La Cantina è ricavata nella cantina antica del borgo · piano interrato, volta a 3,8 metri · è stata cantina operativa fino al 2007, quando il vino della Fattoria Trebbio è stato trasferito nella cantina moderna a 1,2 km. La suite mantiene la cantinetta privata vetrata, riempita ogni stagione di 12 etichette della casa selezionate dalla sommelier Anna."),
                ("p", "La cantinetta è inclusa nel soggiorno · le 12 bottiglie sono a disposizione degli ospiti per assaggio illimitato durante la permanenza. La degustazione guidata di Anna è prevista una sera per soggiorno (compresa nella tariffa) · ulteriori degustazioni su richiesta."),
                ("h3", "Le 12 etichette della stagione"),
                ("p", "La cantinetta cambia composizione ogni stagione. La selezione del 2026 (curata da Anna Ricci): 4 Brunello (Fattoria Trebbio 2018, Biondi-Santi 2016, Casanova di Neri 2017, Il Poggione 2018) · 3 Vino Nobile (Avignonesi 2019, Salcheto 2020, Boscarelli 2018) · 2 Chianti Classico (Castello di Ama 2019, Felsina 2018) · 3 vini sperimentali della Toscana del sud (Petricci 2020, Gualdo del Re 2021, Salvo 2019)."),
                ("ul", ["Ospitanza · due adulti · niente bambini", "Cantinetta · 12 etichette · selezione Anna Ricci AIS · cambia ogni stagione", "Degustazione guidata · una sera per soggiorno (inclusa)", "Wifi · fibra 1 Gbit/s · nessuna ricezione 4G", "Climatizzazione · indipendente, temperatura costante 18 °C"]),
                ("p", "La Cantina è disponibile su richiesta · ideale stagione autunnale dopo la vendemmia. Soggiorno minimo di quattro notti."),
            ],
        },
    ],
}
