"""Villa Prestige — Ultra-luxury private advisory (ultra-luxury-cinematic).

Phase 2g3.7 · Session 53 · Villa Prestige — ultra-luxury-cinematic archetype.
Editorial-concierge tone.

Voice contract (IT):
- Rarefied, editorial, third-person plural or impersonal. The maison of
  real-estate advisory: "Si apre su un parco di tre ettari…",
  "Proponiamo unicamente su appuntamento…". Never "tu"; clients are
  addressed only by register and region ("Lei · cortese famiglia romana",
  "gentile cliente asiatico"). The register is Financial Times
  How to Spend It · Monocle · AD Italia — never estate-agency breezy.
- Concrete details: territori (Portofino, Chianti Classico, Costa
  Smeralda, Lago di Como, Saint-Tropez, Capri, Val d'Orcia), provenance
  (architetti Gio Ponti, Piacentini, Mario Botta; XVII secolo; restauro
  A. Citterio 2014), superfici (400 m² · parco 3 ha · vigna privata
  · cantina interrata), numeri (42 dimore in portafoglio, 9 private
  advisor, 150+ family office serviti dal 1998).
- "Private viewing", "dossier", "riservatezza", "NDA", "referente
  unico", "concierge dedicato", "disponibile solo su appuntamento" —
  mai "visita", "in vendita", "offerta", "occasione", "mutuo",
  "valutazione gratuita", "agente".
- Prezzi mai visibili: solo "Prezzo su richiesta". Nessuna tabella
  specifiche tecniche — solo provenienza editoriale.

Differentiation contract vs Casa (D-054 enforcement):
- Casa è agenzia mass-market Milano-urban con search widget 4-colonne,
  €420K-€1.25M, palette arancio+blu, Poppins/Inter geometrici, CTA
  "Cerca immobile" e "Visita" — tile grid 4-up. Villa è l'antitesi:
  hero fullbleed cinematografico, palette oro-champagne+nero+bianco,
  Cormorant Garamond italic drama, 2-col property dossier cards
  (copertina editoriale + meta provenienza/superficie/territorio),
  CTA "Richiedi una private viewing", prezzi invisibili, territorio
  continentale (non quartieri urbani).
- Vocabolario Villa: dossier · private viewing · riservatezza · NDA ·
  referente · concierge · dimora · territorio · provenance · firma
  d'autore. Mai: immobile · visita · cercare · in vendita · agente.

Differentiation contract vs Luxe (D-054 enforcement):
- Luxe è maison fashion-editorial con carrello (benché private-request),
  drop · capsule · lookbook · silhouette · atelier sellier Parigi,
  tessuti cady/cashmere/organza, prodotti con prezzo visibile, PDP.
- Villa è advisory immobiliare senza alcun prodotto/carrello/PDP.
  Private viewing è un'ora di sala riservata per CONSULTARE un dossier
  di dimora, non per provarsi un abito. Territorio: Portofino · Chianti
  (immobiliare continentale), non Milano/Parigi/Tokyo (maison urbane).
- Vocabolario Villa: dimora · parco · ettari · superficie · provenance
  · referente · NDA · family office · acquisto · rogito · notaio.
  Non dice mai: drop · capsule · lookbook · silhouette · atelier ·
  seamstress · waitlist · RSVP · tessuto · sellier.
"""
from __future__ import annotations

from typing import Any


VILLA_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Dimore",     "kind": "home"},
        {"slug": "collezione", "label": "Collezione", "kind": "blog_list"},
        {"slug": "territorio", "label": "Territorio", "kind": "about"},
        {"slug": "studio",     "label": "Lo Studio",  "kind": "team"},
        {"slug": "esperienza", "label": "Esperienza", "kind": "services"},
        {"slug": "concierge",  "label": "Concierge",  "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":   "V",
        "logo_word":      "Villa Prestige",
        "logo_subline":   "Private Advisory · dal 1998",
        "tag":            "Collezione primavera 2026 · Portafoglio N° 03",
        "phone":          "concierge@villaprestige.it",
        "phone_label":    "Linea riservata concierge",
        "email":          "concierge@villaprestige.it",
        "email_label":    "Concierge privato",
        "address":        "Via Montenapoleone 17 · 20121 Milano",
        "hours_compact":  "Visite solo su appuntamento · Lun–Ven 10–19 · Sab su richiesta",
        "hours_footer_rows": [
            "Incontri in sede · concierge privato",
            "Lingue: italiano · english · français",
        ],
        "license":        "Iscr. RIEA Milano 2841 · P.IVA 07324110984 · Iscr. albo private advisor",
        "footer_intro":
            "Villa Prestige — studio di private advisory per immobili d'autore in Italia e Costa "
            "Azzurra. Un portafoglio ristretto, un referente unico, riserbo assoluto. Selezioniamo "
            "dimore storiche e contemporanee esclusivamente per clienti privati e family office, "
            "dopo una valutazione su due livelli: autorialità architettonica e coerenza del territorio.",

        # Nav reservation CTA (private viewing)
        "nav_cta":         "Richiedi una private viewing",
        "nav_cta_kind":    "appointment",
        "nav_cta_short":   "Richiedi viewing",

        # Footer labels
        "foot_studio":   "Lo studio",
        "foot_pages":    "Mappa",
        "foot_contact":  "Concierge",
        "foot_offices":  "Sedi",
        "offices_footer_rows": [
            "Milano · Montenapoleone 17",
            "Portofino · sede concierge",
            "Saint-Tropez · su appuntamento",
        ],
        "office_rows": [
            "Milano · Montenapoleone 17",
            "Portofino · sede concierge",
            "Saint-Tropez · su appuntamento",
        ],

        # Cross-page editorial meta-strip labels (D-047)
        "dossier_label":        "Dossier",
        "portfolio_label":      "Portafoglio",
        "territorio_label":     "Territorio",
        "superficie_label":     "Superficie",
        "provenance_label":     "Provenance",
        "access_label":         "Accesso",
        "availability_label":   "Disponibilità",
        "price_note":           "Prezzo su richiesta",
        "nda_required_label":   "NDA richiesto prima del dossier",
        "viewing_on_request":   "Disponibile solo su appuntamento",
        "referent_label":       "Referente unico",
        "concierge_line_label": "Linea concierge",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        # Fullbleed editorial cover
        "cover_location": "Portofino · Liguria",
        "cover_image_credit": "Collezione primavera · dossier 03 / 18",
        "cover_image":
            "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=2200&h=1400&fit=crop",

        # Eyebrow + serif drama
        "eyebrow":          "Villa Prestige · Private Advisory · Italia & Costa Azzurra",
        "headline":         "Dimore <em>d'autore</em>, a chi sa riconoscerle.",
        "sub":
            "Un portafoglio ristretto di residenze private, storiche e contemporanee, proposto "
            "solo su appuntamento. Visite riservate, dossier editoriale dedicato, trattativa "
            "discreta — dal primo incontro alla firma notarile, un unico referente.",

        # Hero wordmark + counter chip (from DNA)
        "hero_wordmark":        "Villa Prestige",
        "hero_location":        "Portofino · Collezione primavera 2026",
        "hero_counter_label":   "Dimora in vetrina",
        "hero_counter_value":   "N° 03 / 18",
        "hero_series_label":    "In vetrina",
        "hero_series_title":    "« Villa Aurelia » · Portofino",
        "hero_series_note":
            "Dimora storica del 1922 con parco di tre ettari a picco sul golfo. Quattrocento "
            "metri quadri, biblioteca d'autore, infinity pool affacciata sull'Isola Palmaria.",
        "primary_cta":          "Richiedi una private viewing",
        "primary_cta_href":     "concierge",
        "secondary_cta":        "Collezione primavera",
        "secondary_cta_href":   "collezione",

        # Editorial credit cells — fullbleed hero bottom strip
        "hero_credit_cells": [
            ("Collezione",  "N° 03 / 18"),
            ("Territorio",  "Portofino · Liguria"),
            ("Superficie",  "400 m² · parco 30.000 m²"),
            ("Accesso",     "Solo su appuntamento"),
        ],

        # Signature properties strip — 4 dossier cards (2-up editorial grid)
        "signature_label":   "Collezione primavera",
        "signature_heading": "Dimore <em>selezionate</em> per questa stagione.",
        "signature_intro":
            "Ogni proprietà è proposta solo dopo una valutazione su due livelli — autorialità "
            "architettonica e coerenza del territorio. La lista completa è disponibile su "
            "richiesta, in formato dossier editoriale firmato dal nostro referente.",
        "signature": [
            {
                "index":       "01",
                "title":       "Villa Aurelia",
                "territorio":  "Portofino · Liguria",
                "superficie":  "400 m² · parco 30.000 m²",
                "provenance":  "Anni '20 · firma Piacentini",
                "availability":"Da 3 giorni",
                "slug":        "villa-aurelia-portofino",
                "image":
                    "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "02",
                "title":       "Castello di Monterò",
                "territorio":  "Chianti Classico · Toscana",
                "superficie":  "1.200 m² · 18 ettari",
                "provenance":  "XII secolo · restauro 2014",
                "availability":"Esclusiva",
                "slug":        "castello-di-montero-chianti",
                "image":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "03",
                "title":       "Penthouse Quadronno",
                "territorio":  "Milano · Magenta",
                "superficie":  "380 m² · terrazza 180 m²",
                "provenance":  "Attico unico · vista Duomo",
                "availability":"Su appuntamento",
                "slug":        "penthouse-quadronno-milano",
                "image":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "04",
                "title":       "Mas de la Mer",
                "territorio":  "Saint-Tropez · Costa Azzurra",
                "superficie":  "550 m² · vigna privata",
                "provenance":  "XVIII secolo · certificato",
                "availability":"Nuova",
                "slug":        "mas-de-la-mer-saint-tropez",
                "image":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
        ],
        "signature_link_all":  "Visualizza la collezione completa  →",
        "signature_link_href": "collezione",

        # Territory ribbon — continental destinations
        "territory_label":  "Territori di riferimento",
        "territory":        ["PORTOFINO", "CHIANTI CLASSICO", "COSTA SMERALDA", "LAGO DI COMO", "SAINT-TROPEZ", "CAPRI", "VAL D'ORCIA"],

        # Private advisor block
        "advisor_label":    "Private advisor",
        "advisor_heading":  "Un solo <em>referente</em>, dal primo dossier al rogito.",
        "advisor_intro":
            "Ogni cliente privato è seguito personalmente dal proprio advisor, dall'invio del "
            "primo dossier editoriale alla firma notarile. Mai più di otto mandati attivi per "
            "advisor, per garantire presenza reale e riservatezza assoluta.",
        "advisor_name":     "Alessandra Visconti di Modrone",
        "advisor_role":     "Private client director · dal 2011",
        "advisor_bio":
            "Quindici anni tra Savills, Knight Frank e Sotheby's International Realty "
            "(Londra · Milano · Portofino). Ha seguito personalmente oltre ottanta "
            "transazioni private in Italia e Costa Azzurra per famiglie europee, americane "
            "e asiatiche. Ogni cliente è seguito da lei, dal primo incontro di "
            "riservatezza alla firma notarile.",
        "advisor_portrait":
            "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
        "advisor_cta":      "Richiedi un primo colloquio",
        "advisor_cta_href": "concierge",

        # Editorial storytelling — the maison's numbers (discreet stats — counters OK)
        "numbers_label":    "Lo studio in cifre",
        "numbers_heading":  "Un portafoglio <em>ristretto</em>, un presidio totale.",
        "numbers": [
            ("26",   "anni di private advisory"),
            ("42",   "dimore in portafoglio"),
            ("9",    "private advisor dedicati"),
            ("150",  "family office seguiti"),
        ],
        "numbers_note":
            "Mai più di cinquanta mandati simultanei. Ogni dossier passa dalla scrivania della "
            "direzione prima dell'ingresso in collezione.",

        # Press ribbon
        "press_label":    "Editoriale",
        "press_intro":    "Appare in",
        "press_items":    [
            "Financial Times · How to Spend It",
            "Monocle",
            "Robb Report",
            "Corriere Living",
            "AD Italia",
        ],

        # Editorial storytelling panel — closing private-viewing band
        "private_label":    "Private viewing",
        "private_heading":  "Un'ora di sala riservata, <em>il dossier nelle sue mani.</em>",
        "private_intro":
            "L'incontro in sede avviene su appuntamento e in presenza del referente. "
            "Prepariamo in anticipo i dossier editoriali delle dimore compatibili con il "
            "profilo del cliente e riserviamo una sala con viste proiettate in grande formato. "
            "Il servizio è gratuito e strettamente riservato.",
        "private_primary":       "Richiedi una private viewing",
        "private_primary_href":  "concierge",
        "private_secondary":     "Scopri l'esperienza",
        "private_secondary_href":"esperienza",
    },

    # ─── COLLEZIONE — signature properties list (blog_list) ───
    "collezione": {
        "eyebrow":   "Collezione primavera 2026 · dossier 01 – 14",
        "headline":  "Quattordici <em>dimore d'autore</em>, in attesa del proprio interlocutore.",
        "intro":
            "La collezione è aperta esclusivamente ai clienti sotto NDA. Ogni dossier include "
            "provenance architettonica, planimetria editoriale, territorio e breve storia "
            "della dimora. I prezzi sono comunicati direttamente dal referente dopo il primo "
            "incontro di riservatezza.",

        # Lead post / hero dossier
        "lead_image":
            "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=1600&h=1000&fit=crop",

        # Filters by territorio / provenance / availability
        "filter_label":  "Selezione",
        "filter_groups": [
            {
                "label":   "Territorio",
                "options": ["Tutti", "Portofino", "Chianti Classico", "Milano", "Costa Azzurra", "Capri", "Lago di Como", "Val d'Orcia"],
            },
            {
                "label":   "Provenance",
                "options": ["Tutte", "XVII–XVIII secolo", "Primo Novecento · firma d'autore", "Contemporaneo · restauro recente", "Attico unico"],
            },
            {
                "label":   "Disponibilità",
                "options": ["In corso", "Nuova", "Esclusiva", "Solo su appuntamento"],
            },
        ],
        "sort_label":    "Ordina",
        "sort_options":  ["Per territorio", "Per provenance", "Più recenti", "Esclusive"],

        "result_count":    "14 dossier in collezione primavera",
        "result_subtitle": "Aggiornato ogni primo giovedì del mese",

        "footer_note_label": "Ingresso in collezione",
        "footer_note":
            "La collezione estate 2026 apre giovedì 28 maggio. Clienti già sotto NDA hanno "
            "priorità assoluta su ogni nuovo dossier. Per unirsi alla lista riservata: scrivere "
            "direttamente al concierge della maison.",
    },

    # ─── TERRITORIO (about) — editorial territorio cards ──────
    "territorio": {
        "eyebrow":   "Territori di riferimento · sette geografie private",
        "headline":  "Il <em>paesaggio</em> è la prima firma di una dimora.",
        "intro":
            "Selezioniamo esclusivamente in sette territori italiani e francesi. Ciascuno "
            "con un referente residente, un archivio editoriale dedicato, una rete di "
            "architetti di fiducia. Non operiamo fuori da queste geografie — è così che "
            "garantiamo conoscenza reale delle case, delle vicine, dei venti dominanti.",

        # Editorial statement
        "statement_label":   "Statement",
        "statement_heading": "Sette territori, <em>sette archivi privati.</em>",
        "statement_text":
            "Ogni territorio è seguito da un referente che vi risiede da almeno dieci anni. "
            "Conosciamo le dimore prima che entrino sul mercato — spesso le seguiamo da più "
            "generazioni di proprietari. Il nostro archivio include dati catastali storici, "
            "studi paesaggistici, relazioni con i comuni e le soprintendenze competenti.",

        # 6 territorio cards — history, provenance, architects, property count
        "territories_label":   "I sette territori",
        "territories_heading": "Le geografie <em>della collezione.</em>",
        "territories_intro":
            "Dal promontorio di Portofino alle vigne di Saint-Tropez, dalle colline del "
            "Chianti alla Costa Smeralda. Ogni territorio ha la sua stagione di ingresso, "
            "la sua dorsale architettonica, il suo registro di famiglie.",
        "territories": [
            {
                "name":      "Portofino",
                "region":    "Liguria · Golfo del Tigullio",
                "history":   "Il promontorio frequentato dalle famiglie milanesi dal secondo dopoguerra. Case rivierasche a picco sul mare, terrazzi sulla baia di San Fruttuoso, giardini chiusi di bouganville e olivi centenari. La luce di tarda primavera è il documento migliore.",
                "architects":"Gio Ponti · Gae Aulenti · Umberto Riva · restauri recenti A. Citterio",
                "count":     "9 dimore in collezione",
                "since":     "Referente residente dal 2008",
                "image":
                    "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Chianti Classico",
                "region":    "Toscana · Gaiole – Radda – Castellina",
                "history":   "La dorsale del Chianti fra Siena e Firenze, ricca di castelli medievali e pievi restaurate. Dimore abitate con vigne di produzione, olivete secolari e cantine interrate. Il territorio privilegia il restauro conservativo sotto la soprintendenza di Firenze.",
                "architects":"restauri di Tobia Scarpa · Massimo Carmassi · studio ACPV",
                "count":     "7 dimore in collezione",
                "since":     "Referente residente dal 2011",
                "image":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Costa Smeralda",
                "region":    "Sardegna · Porto Cervo – Porto Rotondo",
                "history":   "Il litorale disegnato negli anni '60 dal Principe Karim Aga Khan. Ville disegnate da Jacques Couëlle e Luigi Vietti, granito locale e tetti in ginepro. Terrazze in pietra a picco sul mare, baie private raggiungibili solo a piedi o via tender.",
                "architects":"Jacques Couëlle · Luigi Vietti · Savin Couëlle · restauri recenti A. Citterio",
                "count":     "5 dimore in collezione",
                "since":     "Referente residente dal 2014",
                "image":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Lago di Como",
                "region":    "Lombardia · Cernobbio – Tremezzo – Bellagio",
                "history":   "Le ville storiche sul Lario, da Villa d'Este a Villa Balbianello. Parchi botanici scolpiti nel Settecento, darsene private, belvederi di gelsomino. Proprietà spesso vincolate, con restauri condotti in accordo con la Soprintendenza di Milano.",
                "architects":"ville storiche · Pelagio Palagi · restauri di Lissoni Casal Ribeiro",
                "count":     "6 dimore in collezione",
                "since":     "Referente residente dal 2010",
                "image":
                    "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Saint-Tropez",
                "region":    "Côte d'Azur · Var · Pampelonne",
                "history":   "Il Var interno, colline tra Ramatuelle e Gassin. Mas provenzali originali del XVII–XVIII secolo, alcuni con vigna di produzione AOP Côtes de Provence. Case a distanza discreta dal mare, a mezz'ora dal porto di Saint-Tropez.",
                "architects":"François Catroux · Jacques Grange · Studio KO · restauri tradizionali",
                "count":     "4 dimore in collezione",
                "since":     "Sede concierge dal 2016",
                "image":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Capri & Val d'Orcia",
                "region":    "Capri · Toscana meridionale · Pienza – Montalcino",
                "history":   "Due territori affini per rarità e per riserbo familiare. A Capri, case a terrazze verso i Faraglioni, spesso tramandate per tre generazioni. In Val d'Orcia, tenute agricole con pieve romanica e vigna di Brunello, proprietà UNESCO con vincoli rigorosi.",
                "architects":"Capri · Francesco Venezia · tradizione locale caprese; Val d'Orcia · Matteo Nunziati · Studio Perruccio",
                "count":     "5 dimore in collezione",
                "since":     "Referenti residenti dal 2013",
                "image":
                    "https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
        ],
        "territory_card_cta": "Richiedi il dossier territorio  →",
        "territory_card_cta_href": "concierge",

        # Closing — the referent promise
        "referent_label":   "Il referente residente",
        "referent_heading": "Conosciamo le case <em>prima</em> che entrino in mercato.",
        "referent_text":
            "Il referente residente non è un consulente a chiamata: è una persona che vive "
            "il territorio da almeno dieci anni, parla la lingua locale, conosce le soprintendenze "
            "e le famiglie storiche. Molte dimore della collezione ci arrivano per indicazione "
            "di un amico comune, non dal mercato — è il modo in cui queste proprietà si sono "
            "sempre passate, fra persone che si fidano.",

        # Discreet stats — territories in numbers
        "stats_label":      "Territori in numeri",
        "stats": [
            ("7",   "territori di riferimento"),
            ("36",  "dimore storiche in archivio"),
            ("18",  "architetti d'autore associati"),
            ("26",  "anni di presenza continua"),
        ],
    },

    # ─── STUDIO (team) — private advisors ─────────────────────
    "studio": {
        "eyebrow":  "Lo studio · nove private advisor · Milano Portofino Saint-Tropez",
        "headline": "Nove advisor, <em>mai più di otto mandati a testa.</em>",
        "intro":
            "Lo studio è una maison di private advisor: ognuno di noi ha radici professionali "
            "nelle grandi case internazionali — Sotheby's International Realty, Knight Frank, "
            "Savills, Christie's Real Estate — e oggi opera in autonomia, con un portafoglio "
            "ristretto. Non promuoviamo bandiere, solo dossier. Non vendiamo nulla sotto pressione.",

        # Director hero card — Alessandra Visconti
        "director_label":   "Direzione",
        "director_name":    "Alessandra Visconti di Modrone",
        "director_role":    "Private client director · fondatrice · dal 1998",
        "director_text":
            "Fonda Villa Prestige a Milano nel 1998, dopo otto anni a Sotheby's International "
            "Realty Londra. Ha seguito personalmente oltre ottanta transazioni private in "
            "Italia e Costa Azzurra — dalla Villa Aurelia di Portofino al Castello di Monterò "
            "in Chianti — per famiglie europee, americane, asiatiche e mediorientali. Pubblica "
            "su Monocle e Corriere Living una rubrica annuale sul mercato delle dimore storiche.",
        "director_portrait":
            "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=800&h=1100&fit=crop",
        "director_quote":
            "\"Non scegliamo le dimore per il loro prezzo. Scegliamo le dimore che ci restano "
            "nel pensiero dopo una sola visita. Ottanta per cento delle proprietà che ci "
            "arrivano viene rifiutato prima dell'ingresso in collezione.\"",
        "director_quote_attribution": "Alessandra Visconti di Modrone · Monocle · marzo 2025",

        # 4 private advisors
        "advisors_label":   "Private advisor",
        "advisors_heading": "Un <em>referente unico</em>, dal primo dossier al rogito.",
        "advisors_intro":
            "Ogni cliente è seguito personalmente da un advisor nominato all'inizio del "
            "mandato. Mai un intermediario, mai un subentro. Se il cliente desidera un "
            "secondo parere, lo studio mette a disposizione un secondo advisor a titolo "
            "consultivo, sempre sotto lo stesso tetto di riservatezza.",
        "advisors": [
            {
                "name":      "Francesco Medici di Porrena",
                "role":      "Senior advisor · territorio Chianti & Val d'Orcia",
                "bio":
                    "Dodici anni a Knight Frank Firenze, specializzato nel restauro "
                    "conservativo delle dimore storiche del Chianti Classico. Laurea in "
                    "Architettura a Firenze, master alla Bartlett London. Segue "
                    "personalmente tutte le trattative in Toscana meridionale.",
                "territories":"Chianti Classico · Val d'Orcia · Firenze",
                "since":     "In studio dal 2014",
                "portrait":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Italiano · English · Français",
            },
            {
                "name":      "Élodie Charbonneau",
                "role":      "Senior advisor · territorio Costa Azzurra & Capri",
                "bio":
                    "Dieci anni a Savills Paris e Christie's Real Estate Monte-Carlo. "
                    "Curatrice di vendite private per collezionisti francesi e americani "
                    "sulla Côte d'Azur. Specializzata in mas provenzali autentici e ville "
                    "d'autore. Responsabile della sede concierge di Saint-Tropez.",
                "territories":"Saint-Tropez · Monaco · Capri",
                "since":     "In studio dal 2016",
                "portrait":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Français · English · Italiano",
            },
            {
                "name":      "Arianna Testa Piccolomini",
                "role":      "Senior advisor · territorio Portofino & Lago di Como",
                "bio":
                    "Otto anni a Sotheby's International Realty Milano, prima consulente "
                    "indipendente per due family office bresciani e piemontesi. Residente "
                    "a Portofino da dieci anni, conosce personalmente le famiglie storiche "
                    "del promontorio. Lingua di lavoro: italiano, inglese, tedesco.",
                "territories":"Portofino · Lago di Como · Milano",
                "since":     "In studio dal 2017",
                "portrait":
                    "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Italiano · English · Deutsch",
            },
            {
                "name":      "Omar Khoury",
                "role":      "Private client advisor · clienti asiatici & mediorientali",
                "bio":
                    "Nove anni tra Knight Frank Dubai e Christie's Hong Kong. Specializzato "
                    "nell'accoglienza di clienti privati provenienti da Hong Kong, Singapore, "
                    "Doha, Riyadh e Dubai. Coordina le traduzioni e le certificazioni notarili "
                    "internazionali. Residente tra Milano e Portofino.",
                "territories":"clienti asiatici · Emirati · Golfo Persico",
                "since":     "In studio dal 2019",
                "portrait":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "العربية · English · Français · 中文 (di base)",
            },
        ],

        # Legal / fiscal partner ribbon
        "partners_label":   "Partner istituzionali",
        "partners_heading": "I partner <em>legali e fiscali</em> dello studio.",
        "partners_intro":
            "Villa Prestige non redige atti. Ogni trattativa è accompagnata da partner "
            "istituzionali selezionati — studi notarili, avvocati internazionali, fiscalisti "
            "patrimoniali — che operano sotto lo stesso tetto di riservatezza. Il cliente "
            "firma un mandato diretto con loro, separato dal nostro, con onorari trasparenti.",
        "partners": [
            ("Studio Notarile Baldi-Corsini",     "Milano · notaio storico famiglie lombarde"),
            ("Gattai Minoli Agostinelli",         "Milano · diritto immobiliare internazionale"),
            ("Chiomenti",                          "Milano · fiscalità patrimoniale family office"),
            ("Ughi e Nunziante",                   "Roma · soprintendenza beni culturali"),
            ("Cabinet Bredin Prat",                "Parigi · transazioni Côte d'Azur"),
        ],

        # Press / editorial mentions
        "press_label":   "Editoriale",
        "press_heading": "Menzioni recenti <em>dello studio.</em>",
        "press_items": [
            {
                "magazine": "Financial Times · How to Spend It",
                "issue":    "Spring 2026",
                "title":    "The quiet sellers of the Italian coast",
                "byline":   "Profilo · autore Bill Prince",
            },
            {
                "magazine": "Monocle",
                "issue":    "Issue 181",
                "title":    "The Chianti Classico revival",
                "byline":   "Reportage · autore Josh Fehnert",
            },
            {
                "magazine": "Robb Report",
                "issue":    "Aprile 2025",
                "title":    "Nine villas, one director",
                "byline":   "Profilo · autore Laurie Kahle",
            },
            {
                "magazine": "Corriere Living",
                "issue":    "Gennaio 2026",
                "title":    "Il mercato delle dimore storiche, visto da Milano",
                "byline":   "Rubrica annuale · firmato Alessandra Visconti di Modrone",
            },
            {
                "magazine": "AD Italia",
                "issue":    "Novembre 2025",
                "title":    "Villa Aurelia · il ritorno di un'icona di Portofino",
                "byline":   "Fotografia · Gianluca Ruotolo",
            },
        ],

        # Studio in numbers
        "numbers_label":   "Lo studio in numeri",
        "numbers": [
            ("26",   "anni dalla fondazione"),
            ("9",    "private advisor dedicati"),
            ("42",   "dimore in collezione"),
            ("7",    "territori di riferimento"),
            ("150",  "family office serviti"),
            ("91",   "transazioni private dal 2015"),
        ],

        # Closing visit CTA
        "visit_label":     "Incontro in sede",
        "visit_heading":   "Un primo <em>colloquio di riservatezza</em> nelle sedi di Milano o Portofino.",
        "visit_text":
            "Riceviamo esclusivamente su appuntamento, nelle sedi di Milano e Portofino, "
            "o presso la sede concierge di Saint-Tropez. Il primo incontro è un colloquio "
            "di riservatezza — non comporta mandato — durante il quale si definisce il "
            "profilo del cliente e si firma l'NDA che dà accesso ai dossier.",
        "visit_primary":      "Richiedi il primo colloquio",
        "visit_primary_href": "concierge",
    },

    # ─── ESPERIENZA (services) — private-viewing process ─────
    "esperienza": {
        "eyebrow":  "L'esperienza · cinque passi in riservatezza",
        "headline": "Dal primo <em>dossier</em> alla firma notarile.",
        "intro":
            "Accompagniamo il cliente in cinque tappe, ognuna riservata e documentata. "
            "Il percorso dura in media quattro mesi per le proprietà in pronto atto, fino a "
            "dodici per le dimore storiche con vincoli paesaggistici. Nessuna tappa è obbligatoria "
            "— il cliente può interrompere il mandato in qualsiasi momento senza penali.",

        # 5-step private-viewing process
        "process_label":   "Il percorso",
        "process_heading": "Cinque passi, <em>un solo referente.</em>",
        "process_intro":
            "Ogni passo è seguito personalmente dall'advisor nominato all'inizio del mandato. "
            "Il cliente può chiedere in qualsiasi momento di parlare con la direzione — "
            "Alessandra Visconti di Modrone risponde personalmente entro un giorno lavorativo.",
        "process": [
            {
                "n":        "01",
                "title":    "Richiesta del dossier",
                "duration": "Risposta entro 48 ore lavorative",
                "text":
                    "Il cliente scrive al concierge descrivendo il profilo della dimora "
                    "desiderata — territorio, provenance, superficie, stagione d'uso. L'advisor "
                    "di territorio risponde entro due giorni lavorativi con un primo riassunto "
                    "della collezione compatibile e una proposta di primo incontro.",
            },
            {
                "n":        "02",
                "title":    "NDA di riservatezza",
                "duration": "Firma in sede o a distanza",
                "text":
                    "Prima della consegna dei dossier completi, cliente e studio firmano un "
                    "NDA reciproco che vincola entrambe le parti al riserbo assoluto sulle "
                    "proprietà, sulle famiglie venditrici e sulle condizioni economiche. "
                    "L'NDA è standard, non preclude l'assistenza di un secondo consulente fiscale.",
            },
            {
                "n":        "03",
                "title":    "Videocall editoriale",
                "duration": "Mezza giornata · con l'advisor",
                "text":
                    "Un primo incontro in videocall — o in sede se il cliente lo desidera — "
                    "in cui sfogliamo insieme tre o quattro dossier editoriali, con "
                    "planimetrie, storia della dimora, immagini aggiornate, relazione "
                    "paesaggistica. Il cliente sceglie le due dimore per la visita in presenza.",
            },
            {
                "n":        "04",
                "title":    "Private viewing in presenza",
                "duration": "Una-due giornate sul territorio",
                "text":
                    "Accompagniamo personalmente il cliente sulla proprietà, in presenza del "
                    "referente residente e, se la famiglia venditrice lo gradisce, di "
                    "quest'ultima. La visita è senza pressione commerciale: dura il tempo "
                    "necessario, include un pranzo nelle immediate vicinanze, e può essere "
                    "ripetuta una seconda volta in una stagione diversa.",
            },
            {
                "n":        "05",
                "title":    "Negoziazione e rogito",
                "duration": "Da 45 giorni a 6 mesi",
                "text":
                    "Lo studio redige la proposta d'acquisto in accordo col cliente e la "
                    "presenta direttamente alla famiglia venditrice. I partner notarili "
                    "preparano compromesso e atto definitivo. L'advisor accompagna "
                    "personalmente il cliente al rogito e resta a disposizione per i sei "
                    "mesi successivi, per ogni adempimento successivo alla consegna.",
            },
        ],

        # Testimonial slot (single, editorial, discreet)
        "testimonial_label":   "Referenza",
        "testimonial_text":
            "\"Mi era stato segnalato lo studio da un ex-socio a Londra. Ho chiesto un primo "
            "colloquio a Milano e in sei mesi ho acquisito una villa in Costa Smeralda per la "
            "nostra famiglia, senza che la trattativa uscisse mai dalla cerchia delle tre "
            "persone coinvolte. Il referente è sempre lo stesso — conosce ora anche i miei "
            "figli.\"",
        "testimonial_author":  "Un family office lombardo · acquisto 2024 · Porto Cervo",

        # FAQ accordion
        "faq_label":   "Domande ricorrenti",
        "faq_items": [
            {
                "q": "Quanto dura mediamente il percorso fino al rogito?",
                "a": "Da quattro a dodici mesi, a seconda della complessità della proprietà. "
                     "Le dimore in pronto atto si chiudono in quarantacinque giorni; quelle "
                     "storiche con vincoli paesaggistici o frazionamento catastale richiedono "
                     "tempi più lunghi per le verifiche presso la soprintendenza.",
            },
            {
                "q": "Quali sono le lingue di lavoro dello studio?",
                "a": "Italiano, inglese e francese in ogni trattativa. Tedesco per Lago di "
                     "Como, arabo e cinese di base per clienti mediorientali e asiatici. "
                     "Traduzioni giurate di tutti i documenti notarili sono incluse nel mandato.",
            },
            {
                "q": "Come viene calcolato l'onorario dello studio?",
                "a": "Sempre come percentuale sul prezzo finale di acquisto, comunicata in "
                     "modo trasparente nel mandato iniziale. Nessuna fee fissa a carico del "
                     "cliente durante le fasi di studio — solo sul rogito effettivo.",
            },
            {
                "q": "Lo studio rappresenta anche i venditori?",
                "a": "Sì, ma mai simultaneamente sulla stessa dimora. Ogni mandato è esclusivo "
                     "a una delle due parti, per garantire la massima trasparenza nella "
                     "negoziazione. Il cliente sa sempre per quale parte stiamo lavorando.",
            },
            {
                "q": "È possibile visitare una dimora più di una volta?",
                "a": "Sì, su richiesta. Accompagniamo gratuitamente il cliente in una seconda "
                     "visita in stagione diversa — molte proprietà costiere vengono visitate "
                     "una volta in estate e una in inverno prima di una decisione.",
            },
            {
                "q": "Come tutelate la riservatezza della trattativa?",
                "a": "Ogni trattativa è aperta con un NDA reciproco, firmato in sede o a "
                     "distanza, che vincola lo studio, il cliente e la famiglia venditrice. "
                     "Nessun dossier è accessibile in forma digitale aperta — tutti i "
                     "documenti sono consegnati su piattaforma riservata o in formato stampato.",
            },
        ],

        # Closing CTA
        "cta_label":      "Primo colloquio",
        "cta_heading":    "Un <em>primo colloquio</em> è sempre gratuito e riservato.",
        "cta_text":
            "Nessun mandato è dovuto dopo il primo incontro. Il cliente riceve un primo "
            "riassunto della collezione compatibile, una proposta di advisor dedicato e una "
            "data indicativa per la prima private viewing. Se il profilo non è compatibile, "
            "ringraziamo e ci congediamo — senza seguito.",
        "cta_primary":      "Richiedi il primo colloquio",
        "cta_primary_href": "concierge",
    },

    # ─── CONCIERGE (contact) — private-viewing request ───────
    "concierge": {
        "eyebrow":  "Concierge privato · su appuntamento",
        "headline": "Su <em>appuntamento</em> soltanto.",
        "intro":
            "Riceviamo esclusivamente su appuntamento, nelle sedi di Milano e Portofino e "
            "presso la sede concierge di Saint-Tropez. Il concierge legge personalmente ogni "
            "richiesta e risponde entro il giorno lavorativo successivo. Per le richieste in "
            "lingua araba, cinese o tedesca, la risposta è firmata direttamente dall'advisor "
            "dedicato al territorio di competenza.",

        # Dedicated phone line by territorio
        "phone_label":    "Linea concierge per territorio",
        "phone_intro":
            "Ogni territorio ha una linea dedicata, aperta solo per clienti sotto NDA o "
            "segnalati da un referente. Per un primo contatto, è sempre preferibile scrivere "
            "al concierge via email — la risposta è più rapida e meglio documentata.",
        "phone_rows": [
            ("Milano · direzione",         "concierge@villaprestige.it"),
            ("Portofino · sede concierge", "portofino@villaprestige.it"),
            ("Saint-Tropez · sede concierge", "saint-tropez@villaprestige.it"),
            ("Clienti asiatici · Omar Khoury", "asia@villaprestige.it"),
        ],

        # Form section (private-viewing request with NDA consent)
        "form_section_label":  "Richiesta di private viewing",
        "form_section_intro":
            "Compilare con cortesia i campi necessari. Il concierge risponde entro il giorno "
            "lavorativo successivo, in italiano, inglese o francese. Per richieste in altre "
            "lingue, segnalare la preferenza nel campo note.",

        "form_helper_required":  "I campi contrassegnati sono obbligatori",
        "form_submit_button":    "Invia richiesta riservata",
        "form_submit_note":
            "La richiesta è letta personalmente dal concierge della direzione. "
            "Nessuna newsletter, nessuna comunicazione commerciale. I dati sono cancellati "
            "entro novanta giorni se il profilo non risulta compatibile con la collezione.",

        "form_fields": [
            {"name":"titolo",    "label":"Titolo", "type":"select", "required":True,
             "options":["Sig.ra","Sig.","Studio · family office","Stampa · editoriale"]},
            {"name":"nome",      "label":"Nome e cognome", "type":"text",
             "placeholder":"Es. Sig.ra Eleonora Visconti", "required":True},
            {"name":"email",     "label":"Email riservata", "type":"email",
             "placeholder":"e.visconti@esempio.it", "required":True},
            {"name":"telefono",  "label":"Telefono (opzionale)", "type":"tel",
             "placeholder":"+39 …", "required":False},
            {"name":"sede",      "label":"Sede preferita", "type":"select", "required":True,
             "options":["Milano · Montenapoleone","Portofino · concierge","Saint-Tropez · concierge","Videocall preliminare","Nessuna preferenza"]},
            {"name":"territorio","label":"Territorio di interesse", "type":"select", "required":True,
             "options":["Portofino · Liguria","Chianti Classico · Toscana","Costa Smeralda · Sardegna","Lago di Como · Lombardia","Saint-Tropez · Costa Azzurra","Capri · Campania","Val d'Orcia · Toscana","Due o più territori"]},
            {"name":"profilo",   "label":"Profilo della dimora", "type":"select", "required":True,
             "options":["Dimora storica con parco","Attico o penthouse urbano","Villa contemporanea d'autore","Tenuta agricola con vigna","Proprietà costiera","Nessun profilo prestabilito"]},
            {"name":"date",      "label":"Preferenza date", "type":"text",
             "placeholder":"Es. seconda settimana di maggio · o ingresso in stagione", "required":False},
            {"name":"note",      "label":"Note al concierge", "type":"textarea",
             "placeholder":"Segnalare preferenze di lingua, referente di presentazione, disponibilità familiari.", "required":True, "rows":5},
            {"name":"nda",       "label":"Acconsento alla firma di un NDA reciproco prima della consegna dei dossier editoriali", "type":"checkbox", "required":True},
        ],

        # Office cards — three concierge offices
        "offices_label":   "Le sedi",
        "offices_heading": "Tre sedi, <em>tre sale riservate.</em>",
        "offices_intro":
            "Ogni sede riceve solo su appuntamento, in una sala riservata con archivio "
            "editoriale locale. La sede di Milano è la direzione generale; Portofino e "
            "Saint-Tropez sono presidiate dai referenti residenti in stagione.",
        "offices": [
            {
                "city":    "Milano",
                "address": "Via Montenapoleone 17 · 20121 Milano",
                "hours":   "Lun – Ven · 10:00 – 19:00 · solo su appuntamento",
                "email":   "concierge@villaprestige.it",
                "role":    "Direzione · archivio centrale · incontri in sede",
            },
            {
                "city":    "Portofino",
                "address": "Via Roma 28 · 16034 Portofino GE",
                "hours":   "Apr – Ott · visite su appuntamento · novembre – marzo su richiesta",
                "email":   "portofino@villaprestige.it",
                "role":    "Sede concierge · referente residente · Liguria",
            },
            {
                "city":    "Saint-Tropez",
                "address": "Place de la Garonne 6 · 83990 Saint-Tropez",
                "hours":   "Mag – Set · visite su appuntamento · ottobre – aprile su richiesta",
                "email":   "saint-tropez@villaprestige.it",
                "role":    "Sede concierge · referente residente · Côte d'Azur",
            },
        ],

        # Press contact ribbon
        "press_contact_label":   "Contatti stampa",
        "press_contact_text":
            "Per richieste editoriali e di stampa specializzata, scrivere direttamente alla "
            "direzione: stampa@villaprestige.it. Comunicati stampa, cartelle fotografiche e "
            "interviste sono coordinati personalmente dalla direttrice. Rispondiamo alla "
            "stampa internazionale entro un giorno lavorativo, in italiano, inglese o francese.",
        "press_contact_email":   "stampa@villaprestige.it",
    },

    # ─── BLOG POSTS (used by collezione blog_list + blog_detail) ──
    # These render the signature properties as editorial dossiers.
    "posts": [
        {
            "slug":     "villa-aurelia-portofino",
            "kicker":   "Portofino · Liguria · Anni '20",
            "title":    "Villa Aurelia — dimora storica del 1922 sul promontorio",
            "lede":
                "Quattrocento metri quadri affacciati sul golfo del Tigullio, parco di tre ettari, "
                "biblioteca d'autore e infinity pool sospesa sopra l'Isola Palmaria.",
            "date":     "12 aprile 2026",
            "read_min": "7",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collezione",  "N° 03 / 18 · primavera 2026"),
                ("Territorio",  "Portofino · Liguria · Golfo del Tigullio"),
                ("Superficie",  "400 m² interni · parco 30.000 m² · 7 camere"),
                ("Provenance",  "1922 · firma Marcello Piacentini · restauro A. Citterio 2014"),
                ("Disponibilità","Da tre giorni · su appuntamento"),
                ("Prezzo",      "Su richiesta al referente"),
            ],
            "body": [
                ("p",
                 "La dimora apre il suo portone carrabile su una salita ombreggiata di lecci "
                 "secolari e si rivela solo dopo trecento metri, affacciata sul golfo del "
                 "Tigullio dall'altezza di sessanta metri. La pianta è a ferro di cavallo, con "
                 "corpo centrale del 1922 e due ali aggiunte nel 1938 dalla stessa firma di "
                 "Marcello Piacentini. L'intervento del 2014 — diretto da Antonio Citterio con "
                 "il paesaggista Paolo Pejrone per il parco — ha conservato tutti gli affreschi "
                 "originali del salone centrale, restituito le infissi in legno massiccio "
                 "e introdotto l'infinity pool oggi iscritta fra le immagini iconiche del "
                 "promontorio."),
                ("h2", "Il parco · tre ettari tra lecci, olivi e camelie"),
                ("p",
                 "Il parco, disegnato originariamente dal conte Ricci nel 1924 e rivisto da "
                 "Paolo Pejrone nel 2014, alterna lecci secolari, olivete in produzione e una "
                 "collezione di trentadue varietà di camelie. La casa dispone di una "
                 "scalinata privata che scende direttamente al mare, con approdo per "
                 "natanti fino a otto metri. Il giardino è irrigabile in completa "
                 "autonomia grazie a una cisterna di raccolta delle acque piovane "
                 "restaurata nel 2018."),
                ("h2", "Interni · biblioteca d'autore e salone di rappresentanza"),
                ("p",
                 "Al piano nobile si articolano il salone centrale di 140 metri quadri, con "
                 "affreschi originali di scuola ligure, una sala da pranzo affacciata sul "
                 "mare e la biblioteca d'autore con boiseries in noce disegnate nel 1938. Al "
                 "primo piano, la suite padronale occupa l'intera ala est, con bagno privato "
                 "in marmo di Carrara e terrazza vista Isola Palmaria. Altre sei camere sono "
                 "distribuite fra primo e secondo piano, ciascuna con bagno dedicato."),
                ("blockquote",
                 "« La villa di Portofino non è una proprietà: è un gesto di riserbo che si "
                 "tramanda fra famiglie che si fidano. Il nostro compito è solo custodire "
                 "il passaggio. »"),
                ("h2", "Provenance · la mano di Piacentini, il restauro di Citterio"),
                ("p",
                 "Commissionata nel 1921 dalla famiglia genovese Acquarone all'architetto "
                 "Marcello Piacentini — allora già autore di numerosi interventi nel "
                 "Lungomare di Viareggio — Villa Aurelia fu completata nel 1922 e rimase "
                 "nella stessa famiglia per tre generazioni. Passa nel 2007 a una seconda "
                 "famiglia milanese, che nel 2014 commissiona ad Antonio Citterio il "
                 "restauro conservativo con Paolo Pejrone al parco. L'intervento è stato "
                 "pubblicato su AD Italia, Elle Decor e Corriere Living."),
                ("ol", [
                    "Accesso: strada privata con portone carrabile, assistenza paesaggistica della Soprintendenza di Genova.",
                    "Parco: tre ettari · scala privata al mare · approdo natanti fino a otto metri.",
                    "Superficie interna: quattrocento metri quadri · sette camere · bagni in marmo di Carrara.",
                    "Impianti: riscaldamento geotermico · impianto fotovoltaico a basso impatto visivo · cisterna acque piovane.",
                    "Prezzo: su richiesta al referente · NDA richiesto prima del dossier completo.",
                ]),
                ("p",
                 "La disponibilità è di soli tre giorni al mese per private viewing, in "
                 "presenza della famiglia proprietaria. L'advisor di territorio — Arianna "
                 "Testa Piccolomini, residente a Portofino da dieci anni — accompagna "
                 "personalmente il cliente dalla prima videocall fino alla firma notarile."),
            ],
            "footer_strap": "Villa Prestige · Portofino · dossier N° 03 / 18",
        },
        {
            "slug":     "castello-di-montero-chianti",
            "kicker":   "Chianti Classico · Toscana · XII secolo",
            "title":    "Castello di Monterò — fortezza medievale con vigna di produzione",
            "lede":
                "Milleduecento metri quadri su diciotto ettari di proprietà, vigna di Chianti "
                "Classico in conduzione biodinamica, cantina interrata, cappella privata del 1432.",
            "date":     "5 aprile 2026",
            "read_min": "9",
            "author":   "Francesco Medici di Porrena",
            "image":
                "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collezione",  "N° 07 / 18 · primavera 2026"),
                ("Territorio",  "Chianti Classico · Toscana · Gaiole in Chianti"),
                ("Superficie",  "1.200 m² interni · 18 ettari · 7 ettari di vigna"),
                ("Provenance",  "XII secolo · restauro conservativo Tobia Scarpa 2014"),
                ("Disponibilità","Esclusiva · un solo mandato attivo"),
                ("Prezzo",      "Su richiesta al referente"),
            ],
            "body": [
                ("p",
                 "Il castello sorge su una dorsale a 520 metri di altitudine fra Gaiole in "
                 "Chianti e Radda, affacciato a sud sulla valle dell'Arbia e a nord sulle "
                 "colline di San Polo. Il corpo centrale, con torre di avvistamento del 1185, "
                 "è rimasto sostanzialmente intatto dalla costruzione originaria; il "
                 "restauro del 2014, condotto da Tobia Scarpa con la supervisione della "
                 "Soprintendenza di Firenze, ha reso abitabili i milleduecento metri quadri "
                 "interni senza alterare una pietra dell'involucro medievale."),
                ("h2", "La tenuta · diciotto ettari, vigna in conduzione biodinamica"),
                ("p",
                 "La proprietà si estende su diciotto ettari di cui sette destinati a vigna "
                 "di Chianti Classico DOCG, in conduzione biodinamica certificata dal 2016. "
                 "La produzione annua è di circa quindicimila bottiglie, distribuite "
                 "esclusivamente su allocazione privata — non sul mercato. La cantina "
                 "interrata, ricavata sotto il corpo centrale, ospita trenta barrique e "
                 "una collezione di duemila bottiglie storiche."),
                ("h2", "Il corpo centrale · sala d'armi e cappella del 1432"),
                ("p",
                 "Al piano terra si articolano la sala d'armi di 180 metri quadri, la "
                 "cappella privata consacrata nel 1432 (in uso annuale il 24 giugno, festa "
                 "del patrono), la cucina storica con forno a legna originale. Il primo "
                 "piano ospita la biblioteca di famiglia con tremila volumi, cinque camere "
                 "padronali, due salotti. Al secondo piano, la torre di avvistamento è "
                 "stata trasformata in studio privato con vista di trecentosessanta gradi "
                 "sulla valle."),
                ("blockquote",
                 "« Il castello non è in vendita perché la famiglia ha bisogno di soldi. "
                 "È in vendita perché la generazione successiva vive fra Londra e Shanghai "
                 "e noi sentiamo il bisogno di cederlo a chi saprà portarlo avanti. »"),
                ("h2", "Provenance · sette secoli, due famiglie"),
                ("p",
                 "Documentato dal 1185 negli atti notarili senesi, il castello fu per "
                 "quattrocento anni presidio della famiglia Ricasoli, poi dei Pannocchieschi "
                 "dal 1570, infine dell'attuale famiglia Medici di Porrena dal 1812. La "
                 "scelta di affidare il mandato a Villa Prestige nasce dal rapporto "
                 "personale trentennale fra la famiglia e il senior advisor Francesco "
                 "Medici di Porrena — cugino della stessa famiglia e advisor del nostro "
                 "studio per il Chianti Classico."),
                ("ol", [
                    "Accesso: strada sterrata privata di un chilometro, vincolo paesaggistico UNESCO in corso di valutazione.",
                    "Parco e vigna: diciotto ettari · sette a Chianti Classico biodinamico · oliveto di duemila piante secolari.",
                    "Superficie interna: milleduecento metri quadri · dieci camere · cappella consacrata 1432.",
                    "Cantina: interrata sotto corpo centrale · trenta barrique · collezione storica duemila bottiglie.",
                    "Impianti: riscaldamento a biomassa · impianto fotovoltaico a basso impatto · acqua da sorgente privata.",
                    "Prezzo: su richiesta al referente · esclusiva totale fino all'autunno 2026.",
                ]),
                ("p",
                 "La disponibilità è di una sola giornata al mese per private viewing, "
                 "direttamente con la famiglia e l'advisor. Il percorso di acquisto richiede "
                 "almeno sei mesi per le verifiche presso la Soprintendenza di Firenze e "
                 "la Regione Toscana. Il passaggio del mandato agricolo di vigna è "
                 "coordinato con il consorzio del Chianti Classico."),
            ],
            "footer_strap": "Villa Prestige · Chianti Classico · dossier N° 07 / 18",
        },
        {
            "slug":     "penthouse-quadronno-milano",
            "kicker":   "Milano · Magenta · attico unico",
            "title":    "Penthouse Quadronno — attico del 1957 con vista Duomo",
            "lede":
                "Trecentoottanta metri quadri al sesto piano di via Quadronno, terrazza di 180 m², "
                "vista frontale sul Duomo, interni firmati Vico Magistretti nel 1958.",
            "date":     "28 marzo 2026",
            "read_min": "6",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collezione",  "N° 11 / 18 · primavera 2026"),
                ("Territorio",  "Milano · Magenta · via Quadronno"),
                ("Superficie",  "380 m² interni · terrazza 180 m² · 4 camere"),
                ("Provenance",  "1957 · firma Luigi Caccia Dominioni · interni Vico Magistretti 1958"),
                ("Disponibilità","Su appuntamento"),
                ("Prezzo",      "Su richiesta al referente"),
            ],
            "body": [
                ("p",
                 "L'attico occupa l'intero sesto piano del palazzo Quadronno, edificato nel "
                 "1957 su progetto di Luigi Caccia Dominioni per una committenza privata "
                 "della borghesia industriale milanese. Gli interni furono completati "
                 "dieci mesi dopo da Vico Magistretti, allora trentatreenne, con un lavoro "
                 "di dettagliata artigianalità su legni, marmi e maniglie ancora oggi "
                 "intatto nella sua originale integrità."),
                ("h2", "La pianta · trecentoottanta metri quadri articolati"),
                ("p",
                 "L'ingresso si apre su una galleria lunga diciotto metri che distribuisce "
                 "le due ali della casa — zona giorno a sud-est, zona notte a nord-ovest. "
                 "Il salone principale di centodieci metri quadri si affaccia frontalmente "
                 "sul Duomo attraverso una vetrata di Jacopo Foggini del 2018. La sala "
                 "da pranzo, la cucina professionale e la dispensa completano l'ala diurna. "
                 "Quattro camere, ciascuna con bagno privato in marmo di Carrara originale "
                 "del 1957, compongono l'ala notturna."),
                ("h2", "La terrazza · centottanta metri quadri affacciati"),
                ("p",
                 "La terrazza perimetrale, centottanta metri quadri complessivi, offre una "
                 "vista di trecentosessanta gradi sulla città: Duomo a est, Castello "
                 "Sforzesco a nord, San Siro all'orizzonte occidentale. L'intervento "
                 "paesaggistico di Patricia Urquiola nel 2019 ha aggiunto una vasca "
                 "idromassaggio coperta, un pergolato in cotto e una collezione di "
                 "quindici varietà di aromatiche mediterranee."),
                ("blockquote",
                 "« Il Quadronno non è un attico: è un piccolo museo della casa milanese "
                 "degli anni Cinquanta. Ogni dettaglio di Magistretti è al suo posto. »"),
                ("h2", "Provenance · Caccia Dominioni, Magistretti, Urquiola"),
                ("p",
                 "Commissionato nel 1956 dalla famiglia Brambilla a Luigi Caccia Dominioni, "
                 "completato nel 1957. Gli interni di Vico Magistretti furono consegnati "
                 "nel 1958 e non hanno subito alterazioni significative per sessant'anni. "
                 "Nel 2018, la seconda famiglia proprietaria ha commissionato a Jacopo "
                 "Foggini la vetrata frontale; nel 2019, l'intervento paesaggistico sulla "
                 "terrazza è stato firmato da Patricia Urquiola. Tutti gli interventi sono "
                 "stati documentati su Domus, Interni e Corriere Living."),
                ("ol", [
                    "Accesso: portineria di palazzo di grande prestigio · ascensore di servizio dedicato.",
                    "Superficie interna: trecentoottanta metri quadri · quattro camere · bagni in marmo originali 1957.",
                    "Terrazza: centoottanta metri quadri · vasca idromassaggio coperta · pergolato in cotto Urquiola 2019.",
                    "Vista: frontale sul Duomo di Milano · panoramica trecentosessanta gradi.",
                    "Impianti: riscaldamento autonomo · climatizzazione a controllo indipendente ala per ala.",
                    "Prezzo: su richiesta al referente · NDA richiesto prima del dossier completo.",
                ]),
                ("p",
                 "La disponibilità è aperta su appuntamento. Il percorso medio di "
                 "acquisto è di quarantacinque giorni dall'NDA al rogito, grazie alla "
                 "documentazione catastale completa già aggiornata. La famiglia venditrice "
                 "è disponibile a un incontro diretto prima del rogito."),
            ],
            "footer_strap": "Villa Prestige · Milano · dossier N° 11 / 18",
        },
        {
            "slug":     "mas-de-la-mer-saint-tropez",
            "kicker":   "Saint-Tropez · Côte d'Azur · XVIII secolo",
            "title":    "Mas de la Mer — mas provenzale del 1754 con vigna AOP",
            "lede":
                "Cinquecentocinquanta metri quadri su colline di Ramatuelle, vigna privata in "
                "Côtes de Provence AOP, originaria costruzione del 1754 restaurata nel 2017.",
            "date":     "20 marzo 2026",
            "read_min": "8",
            "author":   "Élodie Charbonneau",
            "image":
                "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collezione",  "N° 14 / 18 · primavera 2026"),
                ("Territorio",  "Saint-Tropez · Côte d'Azur · Ramatuelle"),
                ("Superficie",  "550 m² interni · 6 ettari · vigna 2,5 ha"),
                ("Provenance",  "1754 · mas provenzale originale · restauro François Catroux 2017"),
                ("Disponibilità","Nuova · appena entrata in collezione"),
                ("Prezzo",      "Su richiesta al referente"),
            ],
            "body": [
                ("p",
                 "Il mas sorge sulle colline interne di Ramatuelle, a dodici chilometri dal "
                 "porto di Saint-Tropez, in un silenzio che solo il Var interno sa offrire. "
                 "La costruzione originaria è del 1754, appartenente alla stessa famiglia "
                 "di tradizione viticola fino al 1948. Acquisita nel 1985 da una famiglia "
                 "parigina, è stata restaurata nel 2017 da François Catroux — l'ultimo "
                 "lavoro privato dell'architetto francese prima della scomparsa — con "
                 "l'obiettivo di restituire gli interni alla loro semplicità originale, "
                 "dopo cinquant'anni di interventi disomogenei."),
                ("h2", "La vigna · due ettari e mezzo di Côtes de Provence AOP"),
                ("p",
                 "La proprietà include due ettari e mezzo di vigna in produzione AOP Côtes "
                 "de Provence, con vinificazione affidata al Domaine Ott per la quota rosé "
                 "e al Domaine Tempier per la quota rosso. La produzione annua è di "
                 "circa settemila bottiglie, distribuite esclusivamente alla famiglia "
                 "proprietaria e ai suoi ospiti. La cantina di trasformazione si trova "
                 "direttamente sotto il mas, in un locale ipogeo del 1802."),
                ("h2", "Interni · salon a doppio volume e camera padronale"),
                ("p",
                 "Il piano terra è articolato intorno a un salon a doppio volume di "
                 "centoventi metri quadri, con camino d'angolo in pietra originale e "
                 "travatura a vista in rovere. La cucina è coperta a volte, pavimentata "
                 "in terra cotta di Salernes. Al primo piano, la camera padronale occupa "
                 "l'intera ala sud con bagno privato in marmo di Caunes-Minervois; altre "
                 "tre camere doppie, ciascuna con bagno dedicato, completano il piano. "
                 "La dépendance della guardiania ospita un appartamento per custode o "
                 "ospiti."),
                ("blockquote",
                 "« François Catroux ha restituito al mas la lentezza che il Var interno "
                 "conosce da sempre. È l'ultimo suo lavoro privato, e si sente. »"),
                ("h2", "Provenance · dalla viticoltura alla famiglia parigina"),
                ("p",
                 "Costruito nel 1754 dalla famiglia Bertrand, che lo possedette per sei "
                 "generazioni coltivando la vigna e producendo olio d'oliva, il mas passò "
                 "alla famiglia parigina Armand nel 1948. Restaurato una prima volta nel "
                 "1985 da Madeleine Castaing in uno stile ricco e ornato, è stato "
                 "riportato alla sua sobrietà originaria nel 2017 dal restauro di "
                 "François Catroux. Il lavoro è stato pubblicato su Architectural Digest "
                 "France e sul Monde d'Hermès."),
                ("ol", [
                    "Accesso: strada bianca privata di duecento metri · portone in ferro originale 1754.",
                    "Parco: sei ettari · vigna AOP due e mezzo · oliveto secolare · piscina naturale in pietra.",
                    "Superficie interna: cinquecentocinquanta metri quadri · quattro camere · dépendance custode.",
                    "Vigna: Côtes de Provence AOP · vinificazione Domaine Ott e Tempier · produzione settemila bottiglie.",
                    "Impianti: riscaldamento a pellet · climatizzazione delicata · acqua da sorgente privata.",
                    "Prezzo: su richiesta al referente · NDA richiesto prima del dossier completo.",
                ]),
                ("p",
                 "La disponibilità è aperta su appuntamento dalla prossima stagione di "
                 "visite — metà maggio. Il mandato agricolo per la vigna è ceduto "
                 "contestualmente al rogito immobiliare; il successivo trasferimento del "
                 "marchio di denominazione AOP è coordinato con Domaine Ott. Il percorso "
                 "medio di acquisto è di quattro mesi dall'NDA al rogito francese."),
            ],
            "footer_strap": "Villa Prestige · Saint-Tropez · dossier N° 14 / 18",
        },
        # Four shorter dossiers to round out the collezione list
        {
            "slug":     "villa-lario-tremezzo",
            "kicker":   "Lago di Como · Tremezzo · Ottocento",
            "title":    "Villa Lario — dimora lacustre del 1862 con darsena privata",
            "lede":
                "Quattrocentocinquanta metri quadri a livello del Lago, parco di due ettari e "
                "mezzo, darsena privata per imbarcazioni fino a quindici metri.",
            "date":     "15 marzo 2026",
            "read_min": "5",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collezione",  "N° 04 / 18 · primavera 2026"),
                ("Territorio",  "Lago di Como · Tremezzo"),
                ("Superficie",  "450 m² interni · parco 25.000 m² · darsena privata"),
                ("Provenance",  "1862 · villa ottocentesca · restauro Lissoni 2020"),
                ("Disponibilità","Su appuntamento"),
                ("Prezzo",      "Su richiesta al referente"),
            ],
            "body": [
                ("p",
                 "Villa Lario sorge a livello del Lago di Como, a cinque minuti dalla "
                 "piazzetta di Tremezzo e a dieci minuti in motoscafo da Villa d'Este. La "
                 "costruzione originale è del 1862, per una famiglia milanese della "
                 "borghesia industriale lombarda. Il restauro conservativo del 2020, "
                 "condotto dallo studio Lissoni Casal Ribeiro, ha mantenuto intatti i "
                 "decori ottocenteschi del salone principale, le boiseries originali "
                 "e la scalinata interna in marmo di Candoglia."),
                ("h2", "Il parco e la darsena · privato accesso al Lago"),
                ("p",
                 "Il parco si estende su due ettari e mezzo degradanti verso il Lago, "
                 "con giardino all'italiana originale del 1875, peschiera, portico "
                 "di gelsomini centenari. La darsena privata, originale del 1870 e "
                 "restaurata nel 2020, ospita imbarcazioni fino a quindici metri di "
                 "lunghezza ed è dotata di gru elettrica per varo invernale. Una "
                 "scalinata di pietra scende direttamente dal salone principale al "
                 "belvedere sul Lago."),
                ("ol", [
                    "Accesso: strada statale · portone privato con portineria.",
                    "Parco: due ettari e mezzo · giardino all'italiana · darsena privata.",
                    "Superficie interna: quattrocentocinquanta metri quadri · cinque camere · biblioteca.",
                    "Prezzo: su richiesta al referente · NDA richiesto prima del dossier.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Lago di Como · dossier N° 04 / 18",
        },
        {
            "slug":     "casa-delle-torri-porto-cervo",
            "kicker":   "Costa Smeralda · Porto Cervo · Anni '70",
            "title":    "Casa delle Torri — villa di Jacques Couëlle del 1972",
            "lede":
                "Seicentoventi metri quadri su promontorio privato, disegno originale di Jacques "
                "Couëlle, terrazze a picco sul mare e accesso diretto a baia privata.",
            "date":     "8 marzo 2026",
            "read_min": "6",
            "author":   "Élodie Charbonneau",
            "image":
                "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collezione",  "N° 08 / 18 · primavera 2026"),
                ("Territorio",  "Costa Smeralda · Porto Cervo"),
                ("Superficie",  "620 m² interni · promontorio privato · baia"),
                ("Provenance",  "1972 · firma Jacques Couëlle · restauro A. Citterio 2018"),
                ("Disponibilità","Su appuntamento"),
                ("Prezzo",      "Su richiesta al referente"),
            ],
            "body": [
                ("p",
                 "Disegnata nel 1972 da Jacques Couëlle per una famiglia belga, Casa delle "
                 "Torri è una delle poche ville integralmente sopravvissute del disegno "
                 "organico smeraldino. Il restauro del 2018 condotto da Antonio Citterio "
                 "ha mantenuto l'integrità assoluta del guscio in granito locale e delle "
                 "coperture in ginepro, introducendo impianti invisibili e una cucina "
                 "contemporanea nella dépendance."),
                ("ol", [
                    "Accesso: strada privata del consorzio · portineria del Porto Cervo.",
                    "Terrazze: tre livelli a picco sul mare · baia privata raggiungibile a piedi.",
                    "Superficie: seicentoventi metri quadri · sei camere · dépendance del personale.",
                    "Prezzo: su richiesta al referente.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Costa Smeralda · dossier N° 08 / 18",
        },
        {
            "slug":     "casa-canapa-capri",
            "kicker":   "Capri · Anacapri · anni '30",
            "title":    "Casa Canapa — villa caprese con affaccio sui Faraglioni",
            "lede":
                "Duecentoventi metri quadri su tre livelli, terrazze sovrapposte verso i "
                "Faraglioni, giardino di limoni secolari, accesso pedonale dal centro di Anacapri.",
            "date":     "1 marzo 2026",
            "read_min": "5",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collezione",  "N° 15 / 18 · primavera 2026"),
                ("Territorio",  "Capri · Anacapri"),
                ("Superficie",  "220 m² interni · 3 terrazze · giardino 800 m²"),
                ("Provenance",  "1934 · villa caprese originale · tre generazioni stessa famiglia"),
                ("Disponibilità","Su appuntamento"),
                ("Prezzo",      "Su richiesta al referente"),
            ],
            "body": [
                ("p",
                 "Casa Canapa è una villa caprese autentica del 1934, passata per tre "
                 "generazioni alla stessa famiglia napoletana. Il disegno originario è "
                 "di tradizione caprese — volte, voltini, scale esterne in maiolica — e "
                 "non ha subito interventi di sostanza. La manutenzione ordinaria, "
                 "condotta con gli artigiani capresi di sempre, ha preservato intatto "
                 "il carattere isolano della casa."),
                ("ol", [
                    "Accesso: solo pedonale · cinque minuti a piedi dalla piazzetta di Anacapri.",
                    "Terrazze: tre livelli sovrapposti · affaccio sui Faraglioni di Capri.",
                    "Superficie: duecentoventi metri quadri · quattro camere.",
                    "Prezzo: su richiesta al referente.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Capri · dossier N° 15 / 18",
        },
        {
            "slug":     "pieve-di-santorso-val-dorcia",
            "kicker":   "Val d'Orcia · Montalcino · XII secolo",
            "title":    "Pieve di Sant'Orso — tenuta UNESCO con vigna di Brunello",
            "lede":
                "Ottocento metri quadri fra pieve romanica e casa colonica, ventidue ettari "
                "patrimonio UNESCO, vigna di Brunello di Montalcino DOCG in produzione.",
            "date":     "22 febbraio 2026",
            "read_min": "7",
            "author":   "Francesco Medici di Porrena",
            "image":
                "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collezione",  "N° 17 / 18 · primavera 2026"),
                ("Territorio",  "Val d'Orcia · Montalcino"),
                ("Superficie",  "800 m² interni · 22 ettari UNESCO · vigna 4 ha"),
                ("Provenance",  "XII secolo · pieve romanica · restauro Matteo Nunziati 2019"),
                ("Disponibilità","Esclusiva"),
                ("Prezzo",      "Su richiesta al referente"),
            ],
            "body": [
                ("p",
                 "La tenuta di Sant'Orso si estende su ventidue ettari di patrimonio UNESCO "
                 "nella Val d'Orcia, fra Montalcino e San Quirico d'Orcia. Il nucleo "
                 "storico comprende la pieve romanica del 1182 — consacrata ancora oggi, "
                 "in uso una volta l'anno — e la casa colonica originaria del 1620, "
                 "restaurata nel 2019 da Matteo Nunziati. La vigna di Brunello di "
                 "Montalcino DOCG occupa quattro ettari, in conduzione biologica "
                 "certificata, con vinificazione affidata alla tenuta vicina."),
                ("ol", [
                    "Accesso: strada comunale bianca di due chilometri · vincolo UNESCO.",
                    "Tenuta: ventidue ettari · vigna quattro ettari · oliveto ottocento piante.",
                    "Superficie interna: ottocento metri quadri · pieve romanica · sei camere.",
                    "Prezzo: su richiesta al referente · esclusiva totale.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Val d'Orcia · dossier N° 17 / 18",
        },
    ],
}


# D-047 · all chrome labels flow from site/page_data above — no string
# should ever be hardcoded in the skin or preview composition HTML.
