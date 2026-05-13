"""Sapori di Langa — Enoteca dei Vignaioli (artisan-workshop archetype) · IT.

Wave 1 Pass-9 (T53 · 2026-05-12). First reuse of `artisan-workshop`
after Bottega (Bottega is the prime instance · sapori is the 1st
reuse · zero new HTML files per D-051 Option A).

Voice contract (IT):
- Premium terroir-curation register · Piedmont/Langhe wine boutique
- `Lei` form (formal but warm · gastronomic-press register) — distinct
  from Bottega's `tu` familiare-toscano
- Concrete details: città (Alba, Barolo, Barbaresco, La Morra,
  Castiglione Falletto), vitigni (Nebbiolo, Barbera, Dolcetto, Arneis),
  gesti (vendemmia manuale · affinamento in botte grande · selezione
  del selezionatore)
- Edition numbers (Cuvée 2019, Lotto 23/200) + signed-by-the-vignaiolo
  proof on every bottle
- Conversion `producer-case-order`: la cassa del vignaiolo come unit
  of commerce — distinct from Bottega's `phone-and-whatsapp` and from
  Luxe's `private-request`

Differentiation contract vs Bottega (D-054 enforcement):
- Bottega vende oggetti (ceramiche, cuoio, tessuti) con voce artigiano-
  toscano. Sapori vende prodotti gastronomici (vino · olio · formaggi ·
  salumi · conserve) con voce vignaiolo-langarolo.
- Bottega: brand "La Bottega di Martino" Firenze · Sapori: brand
  "Sapori di Langa · Enoteca dei Vignaioli" Alba.
- Bottega persona Martino Boncompagni maestro artigiano · Sapori
  persona Pietro Brero oste/sommelier · Cavalier dell'Ordine dei
  Cavalieri del Tartufo e dei Vini di Alba.
- Bottega voice anchor `in bottega` (workshop-craft promise) · Sapori
  voice anchor `vignaiolo indipendente` (terroir-curation promise).
- Bottega CTA "Visita la bottega" · Sapori CTA "Ordina la cassa del
  vignaiolo".
- Bottega palette brown #3E2723 + cream #D7CCC8 + burnt-orange
  #FF8F00. Sapori palette bordeaux-oxblood #4A1E1F + wax-paper-cream
  #F2E9D8 + olive-grove-green #6B7E47 (third polarity for ecommerce
  category · NOT brown-toscano · NOT black-luxe).
- Bottega fonts Libre Baskerville + Nunito Sans (warm rustic) · Sapori
  fonts IBM Plex Serif + IBM Plex Sans (technical-typographic
  enoteca-press register).
- Bottega vocabulary: bottega · artigiano · pezzo unico · edizione ·
  cuoio vegetale · tornito · tessuto · firma. Sapori vocabulary:
  cantina · vignaiolo · cuvée · lotto · vendemmia · botte grande ·
  selezione · cassa.

Imagery direction: cantina-langhe-terroir · X.3 curator pack
`docs/content-factory/imagery/packs/wine-food-boutique.md` (23
Pexels CC0 URLs) consumed verbatim. Zero URL overlap with Bottega's
ecommerce pool or Luxe's fashion pool.

Cluster `wine-food-boutique` activates for the first time (was 0
templates) per the T44 plan §4.2 row 4. IT-only at T53 build per
D-102 cadence. Multilingual EN/FR/ES/AR + AAA + flip via T54.
"""
from __future__ import annotations

from typing import Any


# Imagery URLs from X.3 curator pack `wine-food-boutique.md`. All
# Pexels CC0 · commercial-safe.
_VIGNAIOLO_PORTRAIT_PIETRO = (
    "https://images.pexels.com/photos/8472892/pexels-photo-8472892.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_CARLO = (
    "https://images.pexels.com/photos/8472933/pexels-photo-8472933.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_MARIA = (
    "https://images.pexels.com/photos/8472896/pexels-photo-8472896.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_LUIGI = (
    "https://images.pexels.com/photos/5946081/pexels-photo-5946081.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_FOUNDER_PORTRAIT = (
    "https://images.pexels.com/photos/8472944/pexels-photo-8472944.jpeg"
    "?auto=compress&cs=tinysrgb&w=800&h=1000&fit=crop"
)
_BOTTLE_BAROLO = (
    "https://images.pexels.com/photos/1407847/pexels-photo-1407847.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_BARBERA = (
    "https://images.pexels.com/photos/1123260/pexels-photo-1123260.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_OLIO = (
    "https://images.pexels.com/photos/33783/olive-oil-salad-dressing-cooking-olive.jpg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_FORMAGGIO = (
    "https://images.pexels.com/photos/821365/pexels-photo-821365.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)


SAPORI_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Cantina",          "kind": "home"},
        {"slug": "shop",     "label": "Catalogo",         "kind": "shop"},
        {"slug": "product",  "label": "Bottiglia",        "kind": "product"},
        {"slug": "atelier",  "label": "I vignaioli",      "kind": "about"},
        {"slug": "journal",  "label": "Diario",           "kind": "journal"},
        {"slug": "contatti", "label": "Visita & ordini",  "kind": "contact"},
    ],

    "site": {
        "logo_initial": "S",
        "logo_word":    "Sapori di Langa",
        "tag":          "Enoteca dei vignaioli · Alba · dal 1992",
        "phone":        "+39 0173 364 990",
        "whatsapp":     "0173 364 990",
        "whatsapp_link": "https://wa.me/390173364990",
        "email":        "enoteca@saporidilanga.it",
        "address":      "Via Vittorio Emanuele 38 · 12051 Alba CN",
        "hours_compact": "Mar – Sab · 9:30 – 19:30 · Dom 10 – 13",
        "hours_footer_rows": [
            "Domenica · 10:00 – 13:00 (solo mattina)",
            "Lunedì · chiuso",
            "Fiera del Tartufo · orario continuato Ott – Nov",
        ],
        "license":      "P.IVA 02814730042 · CCIAA Cuneo REA 263118",
        "footer_intro":
            "Enoteca di Alba fondata nel 1992 da Pietro Brero. "
            "Trentadue vignaioli indipendenti delle Langhe, del Roero e del "
            "Monferrato, ognuno con il proprio numero di lotto, la propria "
            "firma in calce alla cuvée, la propria parcella vinificata in "
            "purezza. Spedizione refrigerata in 48 ore in Italia.",
        "nav_cta":      "Ordina la cassa del vignaiolo",
        "nav_cta_kind": "case-order",

        "foot_studio":   "L'enoteca",
        "foot_pages":    "Mappa del sito",
        "foot_contact":  "Ordini & visite",
        "foot_stockists":"Ristoranti che ci scelgono",
        "stockists_rows": [
            "Piazza Duomo · Alba · 3 stelle Michelin",
            "La Ciau del Tornavento · Treiso",
            "Locanda del Pilone · Madonna di Como",
            "Antica Corona Reale · Cervere",
        ],

        "currency_symbol":  "€",
        "shop_filter_label": "Filtri",
        "shop_count_unit":   "bottiglie",
        "edition_label":     "Lotto",
        "made_in_label":     "Vinificato a",
        "artisan_label":     "Vignaiolo",
        "material_label":    "Vitigno",
        "shipping_label":    "Spedizione",
        "shipping_value":    "Refrigerata in 48 ore · sei bottiglie per cassa",
        "guarantee_label":   "Garanzia",
        "guarantee_value":   "Bottiglia difettata sostituita gratuitamente",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Annata 2023 · trentadue vignaioli in cantina",
        "headline": "Vino di territorio, firmato dal <em>vignaiolo indipendente.</em>",
        "intro":
            "Andiamo due volte l'anno in vigna. Una per la vendemmia, una "
            "per assaggiare le annate in botte. Di ogni cantina conosciamo "
            "l'enologo di nome, la parcella vinificata, il lotto in "
            "bottiglia. Nessun vino arriva qui da un catalogo all'ingrosso.",
        "primary_cta":   "Ordina la cassa del vignaiolo",
        "primary_href":  "shop",
        "secondary_cta": "Visita l'enoteca",
        "secondary_href":"contatti",

        # Stamp-aside data
        "stamp_label":  "La nostra regola",
        "stamp_heading":"Due viaggi, <em>una bottiglia.</em>",
        "stamp_rows": [
            ("Vignaioli",   "32 cantine"),
            ("Etichette",   "180 in carta"),
            ("Vendemmia",   "Sempre manuale"),
            ("Cassa",       "6 bottiglie"),
        ],
        "stamp_footer": "Lotto numerato · spedizione refrigerata",
        "stamp_corner_index": "01",
        "stamp_corner_word":  "L'ENOTECA",

        # Latest-arrived band — 4 bottles
        "latest_label":   "Appena entrate in carta",
        "latest_heading": "Le ultime annate <em>dalle Langhe.</em>",
        "latest_link_label": "Tutto il catalogo",
        "latest_link_href":  "shop",
        "latest_items": [
            {
                "id":       "barolo-cannubi-2019",
                "n":        "Cuvée 2019",
                "edition":  "Lotto 23 / 280",
                "name":     "Barolo Cannubi",
                "meta":     "Nebbiolo 100% · Barolo · La Morra",
                "price":    "€ 58",
                "tag":      "Annata",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbera-superiore-2021",
                "n":        "Cuvée 2021",
                "edition":  "Lotto 87 / 1.200",
                "name":     "Barbera d'Alba Superiore",
                "meta":     "Barbera 100% · Roero",
                "price":    "€ 22",
                "tag":      "Quotidiana",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "olio-evo-langhe",
                "n":        "Raccolta 2024",
                "edition":  "Lotto 12 / 380",
                "name":     "Olio EVO Langhe DOP",
                "meta":     "Frantoio + Leccino · Diano d'Alba",
                "price":    "€ 28",
                "tag":      "Stagione",
                "image":    _BOTTLE_OLIO,
            },
            {
                "id":       "castelmagno-stagionato",
                "n":        "Stagionatura 18 mesi",
                "edition":  "Forma 04 / 22",
                "name":     "Castelmagno DOP d'Alpeggio",
                "meta":     "Latte vaccino · Castelmagno CN",
                "price":    "€ 36",
                "tag":      "Estate prodotto",
                "image":    _BOTTLE_FORMAGGIO,
            },
        ],

        # Vignaioli band — 4 named vintners
        "makers_label":   "Mani che vinificano",
        "makers_heading": "Trentadue cantine, <em>una sola carta.</em>",
        "makers_intro":
            "Lavoriamo solo con vignaioli indipendenti — chi vinifica la "
            "propria uva sulla propria parcella e firma di persona ogni "
            "lotto in carta. Ogni cantina è stata visitata da Pietro "
            "almeno tre volte prima di entrare nel catalogo.",
        "makers": [
            {
                "name":   "Carlo Brezza",
                "craft":  "Vignaiolo · Cannubi storico",
                "place":  "Barolo (CN)",
                "since":  "Vigna del 1885 · Brezza dal 1885",
                "quote":  "«Il Barolo non si fa con la fretta. Si fa col silenzio: "
                          "due anni di legno grande, e l'orecchio teso a sentire "
                          "se la botte canta o lamenta.»",
                "portrait": _VIGNAIOLO_PORTRAIT_CARLO,
            },
            {
                "name":   "Maria Vajra",
                "craft":  "Vignaiola · Bricco delle Viole",
                "place":  "Vergne · Barolo (CN)",
                "since":  "Cantina familiare dal 1972",
                "quote":  "«Vinifichiamo solo quello che vediamo crescere. Se "
                          "una parcella non rende come deve, quell'annata non "
                          "la imbottigliamo. La carta dei vignaioli si fa "
                          "anche con quello che non c'è.»",
                "portrait": _VIGNAIOLO_PORTRAIT_MARIA,
            },
            {
                "name":   "Luigi Boasso",
                "craft":  "Vignaiolo · Gabutti Roccaforte",
                "place":  "Serralunga d'Alba (CN)",
                "since":  "Quattro generazioni in vigna",
                "quote":  "«Il Nebbiolo è un'uva ingannevole. Diventa quello "
                          "che gli racconti del terreno. Per questo non lavoro "
                          "altre parcelle: imparare un suolo solo richiede "
                          "trent'anni.»",
                "portrait": _VIGNAIOLO_PORTRAIT_LUIGI,
            },
            {
                "name":   "Anna Brovia",
                "craft":  "Vignaiola · Villero & Rocche dei Brovia",
                "place":  "Castiglione Falletto (CN)",
                "since":  "Cantina dei Brovia dal 1863",
                "quote":  "«Non facciamo concorso, non facciamo punteggi. "
                          "Facciamo Barolo come si è sempre fatto a "
                          "Castiglione Falletto: lungo, austero, niente "
                          "fronzoli. Chi cerca il facile, vada altrove.»",
                "portrait": _VIGNAIOLO_PORTRAIT_PIETRO,
            },
        ],

        # Provenance — terroir + filiera
        "provenance_label":   "Da dove arriva",
        "provenance_heading": "Sessantacinque chilometri, <em>tre denominazioni.</em>",
        "provenance_intro":
            "Tutte le etichette in carta vengono da un raggio di "
            "sessantacinque chilometri attorno ad Alba. Tre denominazioni "
            "principali — Langhe, Roero, Monferrato — e una rete di "
            "vignaioli indipendenti che si sono scelti a vicenda.",
        "provenance_items": [
            {
                "icon": "vine",
                "title": "Langhe DOCG",
                "desc":  "Barolo, Barbaresco, Dolcetto · undici comuni di "
                         "produzione · suoli calcarei e marnosi · altitudine "
                         "200-400 m s.l.m.",
                "place": "Alba · La Morra · Barolo · Castiglione",
            },
            {
                "icon": "hills",
                "title": "Roero DOCG",
                "desc":  "Nebbiolo Roero, Arneis, Favorita · oltre Tanaro · "
                         "suoli sabbiosi · vini più snelli e profumati · "
                         "altitudine 280-380 m s.l.m.",
                "place": "Canale · Vezza · Santo Stefano Roero",
            },
            {
                "icon": "cheese",
                "title": "Monferrato Casalese",
                "desc":  "Barbera Superiore, Grignolino, Ruchè · pendici "
                         "collinari · suoli calcareo-argillosi · vini "
                         "quotidiani di carattere.",
                "place": "Casale · Vignale · Rosignano",
            },
            {
                "icon": "olive",
                "title": "Riviera ligure (50 km)",
                "desc":  "Olio EVO Taggiasco DOP · sale di Trapani al "
                         "carbone vegetale · sgombro sott'olio della Spezia. "
                         "Fornitori storici della casa.",
                "place": "Imperia · La Spezia · Trapani",
            },
        ],

        # Care — wine handling guarantees
        "care_label":   "Come arriva, come si conserva",
        "care_heading": "Quattro promesse di cassa.",
        "care_items": [
            ("Spedizione refrigerata",
             "Cassa di sei bottiglie spedita in scatola "
             "termica con gel pack a 14°C. Consegna in 48 ore in tutta "
             "Italia · 4 giorni in Europa Occidentale."),
            ("Lotto numerato in calce",
             "Ogni bottiglia porta scritto a mano il numero di lotto, "
             "l'annata della cuvée e la firma del vignaiolo. Niente "
             "etichetta industriale-tipografica."),
            ("Sostituzione bottiglia difettata",
             "TCA, ossidazione, rottura in transito · sostituiamo "
             "gratuitamente entro tre mesi dalla consegna · solo prova "
             "fotografica del tappo o del livello."),
            ("Consigli del sommelier",
             "Pietro o Federica vi richiamano entro 24 h se serve un "
             "abbinamento per una serata, una verticale per un "
             "compleanno, una cassa per un regalo aziendale."),
        ],

        # Press band — Italian wine press
        "press_label": "Recensiti su",
        "press_items": ["Slow Wine", "Gambero Rosso Vini", "Vitae AIS",
                        "I Vini di Veronelli", "Doctor Wine"],

        # Journal teaser
        "journal_teaser_label":   "Note di diario",
        "journal_teaser_heading": "Come abbiamo costruito la <em>carta autunno 2026.</em>",
        "journal_teaser_link":    "Leggi il diario",
        "journal_teaser_href":    "journal",

        # CTA section
        "cta_label":     "Ordina · visita · scrivici",
        "cta_heading":   "Una cassa di sei bottiglie, <em>scelta da Pietro.</em>",
        "cta_intro":
            "Le casse selezionate cambiano ogni mese secondo le cantine in "
            "consegna. Vino di tutti i giorni, vini per cellaring, formule "
            "miste con olio e formaggi. Si paga al ritiro, si spedisce in "
            "48 ore refrigerata.",
        "cta_primary":      "Ordina la cassa del mese",
        "cta_primary_href": "shop",
        "cta_secondary":    "Vieni in enoteca",
    },

    # ─── SHOP (catalog) ─────────────────────────────────────────
    "shop": {
        "eyebrow":  "Carta della casa · annata 2023-2024",
        "headline": "Centoottanta etichette, <em>una sola firma.</em>",
        "intro":
            "Carta dei vini, oli, formaggi e conserve. Tutte le etichette "
            "vengono da vignaioli indipendenti visitati personalmente. Per "
            "ogni vino è segnalata la cuvée, il lotto, l'annata e il "
            "vignaiolo che firma.",

        "filter_section_label": "Filtri",
        "filter_groups": [
            {
                "label": "Denominazione",
                "options": ["Barolo DOCG", "Barbaresco DOCG", "Roero DOCG",
                            "Langhe DOC", "Monferrato DOC", "Asti DOCG",
                            "Vino da Tavola"],
            },
            {
                "label": "Vitigno",
                "options": ["Nebbiolo", "Barbera", "Dolcetto", "Arneis",
                            "Favorita", "Grignolino"],
            },
            {
                "label": "Tipologia",
                "options": ["Vini rossi", "Vini bianchi", "Vini dolci",
                            "Spumanti", "Oli & condimenti", "Formaggi",
                            "Salumi & conserve"],
            },
        ],

        "sort_label": "Ordina per",
        "sort_options": ["Più recenti", "Vignaiolo", "Annata", "Prezzo"],

        "result_count": "180 bottiglie",
        "result_subtitle": "Aggiornato martedì 8 ottobre 2026",

        # Sample products — 8 cards (the shop shows more but this is the
        # featured slice)
        "products": [
            {
                "id":       "barolo-cannubi-2019",
                "n":        "01",
                "edition":  "Cuvée 2019 · Lotto 23",
                "name":     "Barolo Cannubi · Brezza",
                "meta":     "Nebbiolo · Barolo · La Morra",
                "price":    "€ 58",
                "tag":      "Annata",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbaresco-rabaja-2018",
                "n":        "02",
                "edition":  "Cuvée 2018 · Lotto 11",
                "name":     "Barbaresco Rabajà · Cortese",
                "meta":     "Nebbiolo · Barbaresco · Treiso",
                "price":    "€ 64",
                "tag":      "Verticale",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbera-superiore-2021",
                "n":        "03",
                "edition":  "Cuvée 2021 · Lotto 87",
                "name":     "Barbera d'Alba Superiore · Vajra",
                "meta":     "Barbera · Roero · Canale",
                "price":    "€ 22",
                "tag":      "Quotidiana",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "dolcetto-diano-2022",
                "n":        "04",
                "edition":  "Cuvée 2022 · Lotto 42",
                "name":     "Dolcetto di Diano d'Alba · Boasso",
                "meta":     "Dolcetto · Diano d'Alba",
                "price":    "€ 16",
                "tag":      "Tavola",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "arneis-roero-2023",
                "n":        "05",
                "edition":  "Cuvée 2023 · Lotto 56",
                "name":     "Roero Arneis · Brovia",
                "meta":     "Arneis · Vezza d'Alba",
                "price":    "€ 18",
                "tag":      "Bianco",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "olio-evo-langhe",
                "n":        "06",
                "edition":  "Raccolta 2024 · Lotto 12",
                "name":     "Olio EVO Langhe DOP · Frantoio Anfossi",
                "meta":     "Frantoio + Leccino · Diano d'Alba",
                "price":    "€ 28",
                "tag":      "Stagione",
                "image":    _BOTTLE_OLIO,
            },
            {
                "id":       "castelmagno-stagionato",
                "n":        "07",
                "edition":  "Stagionatura 18 mesi · Forma 04",
                "name":     "Castelmagno DOP d'Alpeggio",
                "meta":     "Latte vaccino di vacca piemontese",
                "price":    "€ 36",
                "tag":      "Formaggio",
                "image":    _BOTTLE_FORMAGGIO,
            },
            {
                "id":       "salame-cuneo",
                "n":        "08",
                "edition":  "Stagionatura 4 mesi · Lotto 08",
                "name":     "Salame Cuneo · Macelleria Cesare",
                "meta":     "Suino di Cuneo · pepe nero · vino al taglio",
                "price":    "€ 24",
                "tag":      "Norcineria",
                "image":    _BOTTLE_FORMAGGIO,
            },
        ],

        "featured_product_id": "barolo-cannubi-2019",

        "footer_note_label": "Spedizioni & ritiri",
        "footer_note":
            "Spedizione refrigerata in 48 ore in Italia · cassa minima sei "
            "bottiglie · costo spedizione € 12 (gratuita sopra € 200). "
            "Ritiro in enoteca senza preavviso. Per ordini oltre dodici "
            "bottiglie, contattare direttamente.",
    },

    # ─── PRODUCT ────────────────────────────────────────────────
    "product": {
        "id":       "barolo-cannubi-2019",
        "n":        "01",
        "edition":  "Cuvée 2019",
        "edition_note": "Lotto 23 / 280 · imbottigliato dicembre 2022",
        "name":     "Barolo Cannubi · Brezza",
        "subtitle": "Nebbiolo 100% · vinificato sulla collina storica del Cannubi",
        "price":    "€ 58",
        "vat_note": "IVA inclusa · cassa minima sei bottiglie",
        "intro":
            "Barolo della cantina Brezza, parcella di Cannubi storico (la "
            "collina più antica del comune di Barolo, vendemmia documentata "
            "dal 1752). Vendemmia manuale, fermentazione in tini d'acciaio, "
            "affinamento in botte grande di rovere di Slavonia per 30 mesi, "
            "altri 12 in bottiglia prima dell'uscita.",

        "gallery": [
            _BOTTLE_BAROLO,
            _BOTTLE_BAROLO,
            _BOTTLE_BAROLO,
        ],

        "info_label": "Scheda tecnica",
        "info_rows": [
            ("Vignaiolo",    "Carlo Brezza · Brezza & Figli"),
            ("Denominazione","Barolo DOCG"),
            ("Vitigno",      "Nebbiolo 100%"),
            ("Comune",       "Barolo (CN)"),
            ("Parcella",     "Cannubi storico"),
            ("Altitudine",   "260 m s.l.m. · esposizione sud-est"),
            ("Vendemmia",    "Manuale · seconda settimana di ottobre 2019"),
            ("Affinamento",  "30 mesi botte grande + 12 bottiglia"),
            ("Gradazione",   "14,5% vol"),
            ("Solfiti",      "< 80 mg/l · viticoltura biologica certificata"),
        ],

        "size_label": "Formati disponibili",
        "size_intro": "Disponibile in bottiglia singola, magnum, cassa orizzontale 2019 e cassa verticale 2015 – 2019.",
        "size_options": ["750 ml", "1,5 L Magnum", "Cassa 6 · 2019", "Cassa 6 · verticale"],
        "size_chart_link": "Vedi tutti i formati & verticali",
        "size_chart_href": "shop",

        "artisan_label":   "Vignaiolo",
        "artisan_name":    "Carlo Brezza",
        "artisan_role":    "Quarta generazione · Brezza & Figli dal 1885",
        "artisan_bio":
            "Cantina familiare fondata dal bisnonno di Carlo nel 1885, "
            "tramandata in linea diretta padre-figlio. Carlo è entrato in "
            "vigna nel 1997 dopo gli studi enologici ad Alba e tre vendemmie "
            "presso Domaine Romanée-Conti. Vinifica esclusivamente le "
            "parcelle di proprietà famigliare (Cannubi storico, Bricco "
            "Sarmassa, Cannubi Muscatel) — niente uve acquistate.",
        "artisan_portrait": _VIGNAIOLO_PORTRAIT_CARLO,

        "buy_primary":   "Aggiungi alla cassa",
        "buy_secondary": "Riserva in enoteca",
        "buy_note":
            "Ordini superiori a 12 bottiglie · contattare la cantina "
            "direttamente. Disponibilità verificata al momento dell'ordine.",

        "care_label": "Conservazione",
        "care_intro":
            "Barolo da invecchiamento · richiede conservazione attenta per "
            "esprimere il proprio potenziale.",
        "care_items": [
            ("Temperatura",  "12-14°C costanti · senza sbalzi"),
            ("Posizione",    "Orizzontale · tappo sempre in contatto col vino"),
            ("Umidità",      "Almeno 70% · ambiente buio"),
            ("Apertura",     "Aprire 2-3 ore prima · decantazione consigliata"),
            ("Plateau",      "Pronto da bere 2025-2040 · plateau di maturità 2028-2035"),
        ],

        "provenance_label":   "Da Cannubi al bicchiere",
        "provenance_heading": "Quattro passaggi tracciati.",
        "provenance_steps": [
            ("01", "Vendemmia",        "Raccolta manuale in cassette da 18 kg · Cannubi a 260 m s.l.m. · seconda settimana ottobre 2019"),
            ("02", "Affinamento",      "Botte grande di rovere di Slavonia · 30 mesi · niente barrique · Cantina Brezza Barolo"),
            ("03", "Imbottigliamento", "Dicembre 2022 · niente filtrazione · niente chiarifica · lotto 23 di 280"),
            ("04", "Spedizione",       "Cassa di legno timbrata · scatola termica con gel pack a 14°C · 48 ore in Italia"),
        ],

        "related_label":   "Verticali e abbinamenti",
        "related_intro":
            "Cuvée della stessa cantina nelle annate precedenti, e vini "
            "consigliati da Pietro come abbinamento di confronto.",
        "related_items": [
            {"id":"barolo-cannubi-2018",   "n":"N° 088","name":"Barolo Cannubi · 2018",   "meta":"Annata fresca · Brezza",         "price":"€ 62","image":_BOTTLE_BAROLO},
            {"id":"barolo-cannubi-2017",   "n":"N° 074","name":"Barolo Cannubi · 2017",   "meta":"Annata calda · Brezza",          "price":"€ 68","image":_BOTTLE_BAROLO},
            {"id":"barbaresco-rabaja-2018","n":"N° 142","name":"Barbaresco Rabajà · 2018","meta":"Confronto territoriale",         "price":"€ 64","image":_BOTTLE_BAROLO},
            {"id":"barbera-vajra",         "n":"N° 211","name":"Barbera Superiore · 2021","meta":"Quotidiano in tavola · Vajra",   "price":"€ 22","image":_BOTTLE_BARBERA},
        ],
    },

    # ─── ATELIER (about · "I vignaioli") ───────────────────────
    "atelier": {
        "eyebrow":  "L'enoteca",
        "headline": "Sapori di Langa: <em>trentadue vignaioli, una sola insegna.</em>",
        "intro":
            "Sapori di Langa è un'enoteca indipendente fondata ad Alba nel "
            "1992. Lavoriamo esclusivamente con vignaioli che vinificano "
            "in proprio · niente coopérative · niente vini d'industria · "
            "niente etichette costruite a tavolino. Per entrare in carta "
            "una cantina viene visitata almeno tre volte da Pietro.",

        "mission_label":   "La nostra missione",
        "mission_heading": "Pagare il vignaiolo il giusto.",
        "mission_text":
            "L'enoteca esiste per una ragione: ridare al vignaiolo "
            "indipendente il prezzo che il suo lavoro merita. Margine "
            "concordato in trasparenza, contratti annuali firmati a mano, "
            "anticipi sulle uve in vigna se serve. Non vendiamo \"sconti\" "
            "perché chi fa Nebbiolo a 14% non può scontare niente.",

        "process_label":   "Come scegliamo le etichette",
        "process_heading": "Tre visite, una carta.",
        "process_steps": [
            {"num": "01", "title": "Prima visita · primavera",
             "desc": "Pietro va in vigna in marzo o aprile, guarda la potatura, "
                     "assaggia le ultime annate dalle botti, parla col vignaiolo "
                     "di come è andata l'estate scorsa."},
            {"num": "02", "title": "Seconda visita · vendemmia",
             "desc": "Settembre-ottobre · presenza in vendemmia di una giornata, "
                     "almeno tre cassette aperte. Si guarda chi sta in vigna a "
                     "raccogliere e con che cura."},
            {"num": "03", "title": "Terza visita · degustazione in cantina",
             "desc": "Inverno seguente · degustazione tecnica delle botti con "
                     "l'enologo. Se i numeri tornano e il vino dice la verità, "
                     "si firma il contratto annuale."},
            {"num": "04", "title": "Entrata in carta",
             "desc": "Primo lotto in carta solo dopo la quarta visita (uscita "
                     "dalle botti, bottiglia in mano). Niente vino in carta "
                     "che Pietro non abbia assaggiato in tre annate diverse."},
        ],

        "founder_label":   "Il fondatore",
        "founder_heading": "Pietro Brero.",
        "founder_text":
            "Pietro è nato ad Alba nel 1958. Cresciuto nella trattoria di "
            "famiglia, ha lavorato come sommelier al Combal.Zero di Davide "
            "Scabin dal 1985 al 1991, l'anno in cui Combal era ancora a "
            "Almese. Apre Sapori di Langa nel 1992 in via Vittorio "
            "Emanuele con tre cantine in carta. Oggi sono trentadue. "
            "Insignito del Cavalierato dell'Ordine dei Cavalieri del "
            "Tartufo e dei Vini di Alba nel 2014.",
        "founder_portrait": _FOUNDER_PORTRAIT,
        "founder_caption": "Pietro Brero · Cavalier dell'Ordine dei Cavalieri del Tartufo e dei Vini di Alba",

        "numbers_label":   "L'enoteca in numeri",
        "numbers_items": [
            ("32",   "vignaioli indipendenti in carta"),
            ("180",  "etichette in catalogo annuale"),
            ("1992", "anno di apertura"),
            ("65 km","raggio massimo di selezione dalle Langhe"),
        ],

        "visit_label":   "Visita l'enoteca",
        "visit_heading": "Via Vittorio Emanuele 38, <em>Alba.</em>",
        "visit_text":
            "Cinque minuti dalla Stazione di Alba · dieci minuti dalla "
            "Cattedrale. Degustazione guidata su appuntamento il giovedì "
            "pomeriggio · cinque vini con tagliere di Castelmagno e "
            "salame Cuneo, 35 € a persona. Senza appuntamento per "
            "acquisti negli orari di apertura.",
        "visit_primary":      "Prenota una degustazione",
        "visit_primary_href": "contatti",
        "visit_secondary":    "Mappa & orari",
    },

    # ─── JOURNAL ───────────────────────────────────────────────
    "journal": {
        "eyebrow":  "Diario d'enoteca",
        "headline": "Note di cantina, <em>note di vendemmia.</em>",
        "intro":
            "Brevi appunti di Pietro e Federica sul lavoro in cantina, "
            "sulle vendemmie in corso, sulle bottiglie aperte di sera per "
            "i clienti più curiosi. Lettura riservata.",
        "list_label": "Voci del diario",
        "entries": [
            {
                "slug":    "vendemmia-2024-langhe",
                "kicker":  "Vendemmia 2024",
                "title":   "Vendemmia 2024 nelle Langhe · cosa è uscito dalle botti",
                "date":    "10 ottobre 2026",
                "read_min": 6,
                "author":  "Pietro Brero",
                "lede":
                    "La vendemmia 2024 ha richiesto pazienza. Il caldo di "
                    "agosto ha rallentato le maturazioni, settembre ha "
                    "rimesso le cose a posto. Ecco cosa entra in carta da "
                    "novembre.",
            },
            {
                "slug":    "barolo-2019-degustazione",
                "kicker":  "Annata in carta",
                "title":   "Perché il Barolo 2019 vale i sei anni di attesa",
                "date":    "28 settembre 2026",
                "read_min": 5,
                "author":  "Pietro Brero",
                "lede":
                    "L'annata 2019 è uscita ad agosto dopo trent'anni di "
                    "Barolo in cantina. Ecco perché vale i due anni di "
                    "botte grande e i sei anni minimi prima di stapparla.",
            },
            {
                "slug":    "olio-evo-langhe-2024",
                "kicker":  "Olio della casa",
                "title":   "Olio EVO Langhe 2024 · una raccolta da segnare",
                "date":    "15 settembre 2026",
                "read_min": 4,
                "author":  "Federica Bertola",
                "lede":
                    "Il frantoio Anfossi ha chiuso la raccolta 2024 il "
                    "5 settembre. Cinque ettolitri in carta da ottobre, "
                    "lotto 12. Ecco com'è.",
            },
        ],

        "footer_note_label": "Ricevi il diario via email",
        "footer_note":
            "Quattro o cinque uscite all'anno, mai più. Lo riceve solo chi "
            "ne fa esplicita richiesta in cassa o sul modulo contatti.",
    },

    # ─── CONTATTI ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Visita & ordini",
        "headline": "Una telefonata, <em>una cassa.</em>",
        "intro":
            "Per ordinare una cassa o prenotare una degustazione guidata, "
            "il modo più semplice è una telefonata in enoteca negli orari "
            "di apertura. Oppure usare il modulo qui sotto · risposta "
            "entro 24 h in orario lavorativo.",

        "form_section_label": "Scrivici",
        "form_section_intro":
            "Per ordini speciali (verticali, magnum, casse aziendali), "
            "indica il vignaiolo o l'annata di interesse. Per degustazioni "
            "guidate, indica data e numero di partecipanti.",
        "form_helper_required": "I campi contrassegnati sono obbligatori.",
        "form_submit_button":   "Invia richiesta",
        "form_submit_note":     "Riceverai conferma via email entro 24 ore in orario di apertura.",

        "form_fields": [
            {"name": "name",     "label": "Nome e cognome",  "type": "text",     "required": True},
            {"name": "email",    "label": "Email",           "type": "email",    "required": True},
            {"name": "phone",    "label": "Telefono",        "type": "tel",      "required": False},
            {"name": "subject",  "label": "Oggetto",         "type": "select",
             "options": ["Ordine cassa", "Degustazione guidata", "Verticale o magnum",
                         "Cassa aziendale o regalo", "Altro"],     "required": True},
            {"name": "message",  "label": "Messaggio",       "type": "textarea", "required": True,
             "placeholder": "Es. \"Cassa di sei Barolo cuvée 2019\" oppure "
                             "\"Degustazione per quattro persone giovedì 18 ottobre\"."},
        ],

        "card_label":          "L'enoteca",
        "card_address_label":  "Indirizzo",
        "card_address_value":  "Via Vittorio Emanuele 38 · 12051 Alba CN",
        "card_phone_label":    "Telefono",
        "card_phone_value":    "+39 0173 364 990",
        "card_whatsapp_label": "WhatsApp",
        "card_whatsapp_value": "0173 364 990",
        "card_email_label":    "Email",
        "card_email_value":    "enoteca@saporidilanga.it",
        "card_hours_label":    "Orari",
        "card_hours_rows": [
            "Mar – Sab · 9:30 – 19:30 orario continuato",
            "Domenica · 10:00 – 13:00 solo mattina",
            "Lunedì · chiuso · degustazioni private su appuntamento",
            "Fiera del Tartufo · ott – nov · 9 – 21 orario continuato",
        ],
        "card_directions_label": "Come arrivare",
        "card_directions_text":
            "Cinque minuti a piedi dalla Stazione di Alba (treno regionale "
            "diretto da Torino · 1 h 10 min). Dieci minuti dalla "
            "Cattedrale di San Lorenzo. Parcheggio gratuito in Piazza "
            "Risorgimento, 200 metri dall'enoteca.",

        "faq_label": "Domande frequenti",
        "faq_items": [
            ("Quanto costa la spedizione?",
             "Spedizione refrigerata in 48 ore: € 12 in Italia "
             "(gratuita sopra € 200), € 24 in Europa Occidentale. "
             "Cassa minima sei bottiglie."),
            ("Posso ordinare una sola bottiglia?",
             "No, la cassa minima è sei bottiglie. Composizione "
             "libera fra vino, olio, formaggi e salumi. Il valore "
             "indicativo della cassa minima è circa € 90-100."),
            ("Avete vini biologici o naturali?",
             "Sì. Circa il 70% dei vignaioli in carta lavora in "
             "biologico certificato, il 20% in biodinamica certificata "
             "Demeter. La parte restante segue protocolli a basso "
             "intervento ma non certificati."),
            ("Spedite all'estero?",
             "Europa Occidentale sì (Francia, Germania, Belgio, Olanda, "
             "Lussemburgo, Austria). Resto del mondo solo su preventivo "
             "(USA · UK · Svizzera · Giappone)."),
            ("Posso visitare l'enoteca senza prenotare?",
             "Sì, negli orari di apertura. Per la degustazione guidata "
             "del giovedì pomeriggio è necessaria prenotazione almeno "
             "48 h prima."),
        ],
    },
}
