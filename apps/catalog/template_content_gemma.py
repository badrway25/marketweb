"""Gemma · Atelier di Alta Gioielleria — Milano Brera (fashion-editorial IT).

T61 · Wave 2 Pass-5 (2026-05-13) · 1st reuse of fashion-editorial
archetype after Luxe (D-051 Option A · zero new HTML files).
Same category as Luxe (ecommerce) so no `skin_source_category`
override needed.

Voice contract (IT):
- High-jewelry editorial register: Vogue Gioielli · L'Officiel
  Italia (Joaillerie) · The Jewellery Editor · Robb Report Italia
  Watches&Jewellery · Departures. Third-person formal, never
  second-person · "L'atelier propone solo su appuntamento privato"
  · "Gli orafi della famiglia Gemma firmano ogni pezzo".
- Voice anchor `gioielleria d'autore` — load-bearing register that
  foregrounds the auteurship of the goldsmith family vs the
  marketing-anonymous luxury jewelry chain. Distinct from Luxe's
  `maison di moda` (fashion-maison register).
- Vocabolario: atelier · orafo · gemmologa · taglio · castone ·
  filigrana · cesello · brunitura · sigillo · firma · pezzo unico
  · serie limitata · appuntamento privato · NDA. Mai: collana ·
  bracciale · orologio (questi sì come categorie) ma niente
  `accessorio`, `must-have`, `wishlist`, `drop semestrale`, niente
  `lookbook fashion-week`.
- Concrete detail: Milano Brera · 4 generazioni Gemma (1908
  bottega aperta dal bisnonno Eligio + nonno Carlo + padre Giuseppe
  + Eleonora Gemma classe 1968 attuale direzione) · Eleonora
  gemmologa GIA (Gemological Institute of America · diploma 1994)
  · ex-Buccellati 1996-2014 (alta gioielleria romana) · rientro in
  atelier di famiglia 2014. Serie limitate stagionali · numerazione
  manuale incisa su retro · sigillo di garanzia con punzone della
  bottega registrato Camera di Commercio Milano 1948.

Differentiation contract vs Luxe Maison (D-054 enforcement):
- Luxe è maison fashion-editorial con drop semestrali · lookbook
  · waitlist RSVP · capsule · silhouette · seamstress · cady ·
  organza · cashmere · sellier · Parigi atelier · Tokyo private
  showroom. Palette nero #000000 + ivory #F5F5F5 + champagne-oro
  #B8860B. Tipografia Cormorant Garamond + Montserrat.
- Gemma è atelier alta gioielleria con pezzi unici · serie limitate
  · gemmologia · firma di famiglia · 4 generazioni · GIA · Milano
  Brera (NON Parigi/Tokyo/Roma) · Buccellati heritage register
  (Eleonora ex-Buccellati 18 anni). Palette pearl-night #0F0E14
  + champagne-white #F1ECDF + rose-quartz #9F7373 (gemma-flavoured
  · zero overlap con nero-oro Luxe). Tipografia Didone-influenced
  (Bodoni Moda + Inter) · NOT Cormorant.
- Conversion pattern: Luxe `private-request` (appuntamento maison
  di moda · RSVP per drop e capsule). Gemma `private-viewing-
  jewelry` (appuntamento gemmologica per visione pezzi · NDA su
  collezione su misura · concierge atelier).
- Vocabolario diverso: Luxe `drop`, `capsule`, `silhouette`,
  `lookbook`, `seamstress` vs Gemma `pezzo unico`, `serie limitata`,
  `castone`, `taglio brillante`, `cesello`, `filigrana`. Zero overlap
  semantico vs Luxe.

Shape compliance — see factory/standards/fashion-editorial-shape-
contract.md (T61 · authored DURING this build per T56 pattern).
All canonical iterator shapes from Luxe respected verbatim:
- `product.provenance_steps` 3-tuples (n, t, p) NOT dicts
- `product.size_options` + `product.color_options` scalar strings
- `home.press_items` scalar BUT `maison.press_items` dict[4] —
  SAME-NAME DIFFERENT-SHAPE warning per contract §2.3
- `<contact>.faq_items` `{q,a}` dicts NOT 2-tuples
- `<about>.ateliers` dict[7 keys] · `lookbook.looks` dict[5 keys]
- `<contact>.maison_cards` dict[5 keys] (multi-city)
"""
from __future__ import annotations

from typing import Any


# Interim Unsplash CC0 imagery pool · jewelry-craftsmanship signal.
# X.5 curator pack `jewelry-atelier.md` pending — these URLs cover
# the load-bearing roles: hero atelier workbench · gem close-up ·
# goldsmith hands · finished pezzo · brera street · founder portrait.
_HERO_BENCH = "https://images.unsplash.com/photo-1605100804763-247f67b3557e?w=1600&q=80&auto=format&fit=crop"
_GEMS_CLOSE = "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=1200&q=80&auto=format&fit=crop"
_GOLDSMITH_HANDS = "https://images.unsplash.com/photo-1611652022419-a9419f74343d?w=1200&q=80&auto=format&fit=crop"
_PEZZO_HERO = "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=1200&q=80&auto=format&fit=crop"
_BRERA_STREET = "https://images.unsplash.com/photo-1542038784456-1ea8e935640e?w=1200&q=80&auto=format&fit=crop"
_PORTRAIT_ELEONORA = "https://images.unsplash.com/photo-1573497019418-b400bb3ab074?w=900&q=80&auto=format&fit=crop"
_ANELLO_BRILLANTE = "https://images.unsplash.com/photo-1605100804763-247f67b3557e?w=1200&q=80&auto=format&fit=crop"
_COLLANA_FILIGRANA = "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=1200&q=80&auto=format&fit=crop"
_BRACCIALE_STORIA = "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=1200&q=80&auto=format&fit=crop"
_ORECCHINI_ZAFFIRO = "https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=1200&q=80&auto=format&fit=crop"
_OROLOGIO_SVIZZERO = "https://images.unsplash.com/photo-1547996160-81dfa63595aa?w=1200&q=80&auto=format&fit=crop"
_FERMASCIARPA = "https://images.unsplash.com/photo-1535632066274-95bb27dee0d9?w=1200&q=80&auto=format&fit=crop"
_ANELLO_SMERALDO = "https://images.unsplash.com/photo-1602173574767-37ac01994b2a?w=1200&q=80&auto=format&fit=crop"
_DIADEMA_NUZIALE = "https://images.unsplash.com/photo-1573408301185-9146fe634ad0?w=1200&q=80&auto=format&fit=crop"
_PORTRAIT_GIUSEPPE = "https://images.unsplash.com/photo-1545167622-3a6ac756afa4?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_CARLO = "https://images.unsplash.com/photo-1559963110-71b394e7494d?w=900&q=80&auto=format&fit=crop"
_LOOK_EDITORIAL_1 = "https://images.unsplash.com/photo-1535632787350-4e68ef0ac584?w=1200&q=80&auto=format&fit=crop"
_LOOK_EDITORIAL_2 = "https://images.unsplash.com/photo-1611652022419-a9419f74343d?w=1200&q=80&auto=format&fit=crop"
_LOOK_EDITORIAL_3 = "https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=1200&q=80&auto=format&fit=crop"
_LOOK_EDITORIAL_4 = "https://images.unsplash.com/photo-1605100804763-247f67b3557e?w=1200&q=80&auto=format&fit=crop"


GEMMA_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Atelier",         "kind": "home"},
        {"slug": "collezione", "label": "Collezione",      "kind": "collection"},
        {"slug": "pezzo",      "label": "Pezzo",           "kind": "product"},
        {"slug": "casa",       "label": "La casa Gemma",   "kind": "about"},
        {"slug": "lookbook",   "label": "Editoriale",      "kind": "lookbook"},
        {"slug": "concierge",  "label": "Concierge",       "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":   "G",
        "logo_word":      "Gemma",
        "logo_subline":   "Atelier di Alta Gioielleria · dal 1908",
        "tag":            "Serie Inverno 2026 · numerata a mano in atelier",
        "phone":          "+39 02 8642 1170",
        "email":          "atelier@gemmamilano.it",
        "address":        "Via Brera 28 · 20121 Milano",
        "hours_compact":  "Atelier su appuntamento privato · lun–sab 10–19",
        "hours_footer_rows": [
            "Atelier solo su appuntamento · ricevimento privato",
            "Lingue: italiano · english · français · 日本語",
        ],
        "license":        "Iscr. Camera di Commercio Milano 1948 · Punzone 117MI · Iva 09142730969 · Membro Federpreziosi",
        "footer_intro":
            "Gemma è l'atelier di alta gioielleria della famiglia Gemma a Milano "
            "Brera · quattro generazioni di orafi dal 1908. Eleonora Gemma "
            "(gemmologa GIA · classe 1968 · quarta generazione · ex-Buccellati "
            "1996-2014) ne è direttore artistico dal 2014. Pezzi unici e serie "
            "limitate, tutti firmati a mano con il sigillo di famiglia · "
            "appuntamento privato in atelier · NDA su collezione su misura.",

        # Nav reservation CTA
        "nav_cta":         "Richiedete un appuntamento privato",
        "nav_cta_kind":    "appointment",

        # Footer labels
        "foot_studio":   "L'atelier",
        "foot_pages":    "Mappa",
        "foot_contact":  "Concierge",
        "foot_offices":  "Indirizzi",
        "office_rows": [
            "Atelier · Via Brera 28 · 20121 Milano",
            "Showroom privato · Place Vendôme 19 · 75001 Paris · su appuntamento",
        ],

        # Collection / drop / season labels
        "collection_label":     "Serie Inverno 2026",
        "drop_label":           "Serie limitata",
        "season_label":         "Stagione",
        "rsvp_label":           "Appuntamento solo su richiesta",
        "waitlist_label":       "Lista d'attesa attiva",
        "viewing_label":        "Visione privata",
        "viewing_value":        "Solo su appuntamento · NDA per collezione su misura",
        "currency_symbol":      "€",

        # Private/atelier labels (used on home advisor band + concierge)
        "private_phone_label":  "Linea diretta Eleonora",
        "private_email_label":  "Concierge privato dell'atelier",
        "showroom_paris":       "Showroom privato Paris · Place Vendôme 19 · 75001",
        "showroom_tokyo":       "Visite a domicilio · Roma · Tokyo · Singapore · solo su appuntamento privato",
        "shipping_label":       "Consegna assicurata",
        "shipping_value":       "Corriere assicurato Loomis · valore dichiarato · Italia 24h · Europa 4-5 giorni · Stati Uniti 5-7 giorni",
    },

    # ─── HOME ──────────────────────────────────────────────────
    # Shape matches Luxe canonical · home.html template keys verified
    "home": {
        # Cover band (top of home)
        "cover_image":           _HERO_BENCH,
        "issue":                 "Serie Inverno 2026 · Volume IV · novembre 2025",
        "cover_styling_label":   "Fotografia · ",
        "cover_styling_name":    "Paolo Roversi",
        "cover_label":           "Soggetto · ",
        "cover_subject":         "Atelier Gemma · Milano Brera · novembre 2025",

        # Hero band
        "eyebrow":               "Atelier di Alta Gioielleria · Milano Brera · dal 1908",
        "headline":              "Quattro generazioni a Brera. <em>Gioielleria d'autore</em>, mai prodotta in serie.",
        "headline_credit_line":  "Eleonora Gemma · gemmologa GIA · direttore artistico dal 2014 · quarta generazione",
        "intro":
            "L'atelier Gemma è stato aperto nel 1908 in via Brera dal bisnonno "
            "Eligio Gemma. Da allora quattro generazioni di orafi vi hanno "
            "lavorato senza mai cambiare indirizzo né insegna. Eleonora Gemma · "
            "gemmologa GIA · ne è direttore artistico dal 2014 dopo diciotto "
            "anni a Buccellati Roma. Pezzi unici e serie limitate stagionali · "
            "firmati a mano col sigillo di famiglia.",
        "primary_cta":           "Richiedete un appuntamento privato",
        "primary_href":          "concierge",
        "secondary_label":       "Stilismo · ",
        "secondary_name":        "Camille Bidault-Waddington",

        # Edition band (cover for the tiles section)
        "edition_label":         "Serie Inverno 2026 · otto pezzi",
        "edition_subline":       "Numerazione manuale · sigillo Gemma · certificato GIA",
        "issue_label":           "Volume IV",

        # tiles — list[4] of dict[5 keys=id,image,name,price,tag]
        "tiles": [
            {
                "id":    "anello-brillante-3ct",
                "image": _ANELLO_BRILLANTE,
                "name":  "Anello «Cuneo» · brillante 3,02 ct",
                "price": "Prezzo su richiesta",
                "tag":   "Pezzo unico · 12/12",
            },
            {
                "id":    "collana-filigrana-platino",
                "image": _COLLANA_FILIGRANA,
                "name":  "Collana «Trama» · filigrana platino",
                "price": "Prezzo su richiesta",
                "tag":   "Serie limitata · 24 esemplari",
            },
            {
                "id":    "orecchini-zaffiri-ceylon",
                "image": _ORECCHINI_ZAFFIRO,
                "name":  "Orecchini «Acqua» · zaffiri Ceylon",
                "price": "Prezzo su richiesta",
                "tag":   "Pezzo unico · 1/1",
            },
            {
                "id":    "anello-smeraldo-colombiano",
                "image": _ANELLO_SMERALDO,
                "name":  "Anello «Foglia» · smeraldo Muzo",
                "price": "Prezzo su richiesta",
                "tag":   "Pezzo unico · 1/1",
            },
        ],

        # Manifesto band
        "manifesto_label":   "Cosa è gioielleria d'autore",
        "manifesto_heading": "Quattro principî · <em>una sola firma</em>.",
        "manifesto_text":
            "Gioielleria d'autore significa che ogni pezzo porta un nome (non "
            "un codice di catalogo), una firma manuale del maestro orafo, un "
            "certificato GIA per ogni pietra di carato superiore, e una "
            "garanzia di rilavorazione a vita in atelier Brera. Non vendiamo "
            "collezioni infinite né produciamo in fabbrica · accettiamo dieci "
            "commissioni su misura all'anno · le altre stagioni sono serie "
            "limitate da uno a dodici esemplari per modello.",

        # Atelier numbers — list[5] of tuple[2]
        "atelier_numbers_label":   "L'atelier in cifre",
        "atelier_numbers": [
            ("118",  "Anni di atelier in via Brera · dal 1908"),
            ("4",    "Generazioni di orafi Gemma in continuità diretta"),
            ("18",   "Anni di Eleonora Gemma da Buccellati Roma · 1996-2014"),
            ("117",  "Punzone della casa registrato a Milano · dal 1948"),
            ("24",   "Pezzi della Serie Inverno 2026 · numerati a mano"),
        ],
        # Lookbook teaser tiles — list[4] of dict[3 keys=credit,image,title]
        "lookbook_teaser_label":   "Editoriale",
        "lookbook_teaser_heading": "Quattro studi per la Serie Inverno.",
        "lookbook_teaser_intro":
            "Editoriale fotografico della serie · scatti firmati da Paolo "
            "Roversi · stilismo a cura di Camille Bidault-Waddington · "
            "ritratti in palazzo Cusani Brera nel novembre 2025.",
        "lookbook_teaser_tiles": [
            {
                "image":  _LOOK_EDITORIAL_1,
                "title":  "Studio I · ritratto al palazzo Cusani",
                "credit": "Fotografia Paolo Roversi · stilismo C. Bidault-Waddington",
            },
            {
                "image":  _LOOK_EDITORIAL_2,
                "title":  "Studio II · mani orafe sulla collana «Trama»",
                "credit": "Fotografia Paolo Roversi · still-life atelier",
            },
            {
                "image":  _LOOK_EDITORIAL_3,
                "title":  "Studio III · orecchini «Acqua» su zaffiro Ceylon",
                "credit": "Fotografia Paolo Roversi · macro 1:1",
            },
            {
                "image":  _LOOK_EDITORIAL_4,
                "title":  "Studio IV · anello «Cuneo» 3,02 ct",
                "credit": "Fotografia Paolo Roversi · still-life atelier",
            },
        ],
        "lookbook_teaser_link":    "Sfogliate l'editoriale",
        "lookbook_teaser_href":    "lookbook",

        # Press band — list[5] of scalar string (NOT dict · matches archetype pattern)
        "press_label":   "Stampa",
        "press_intro":   "Quindici anni di rassegna stampa internazionale",
        "press_items": [
            "Vogue Gioielli",
            "L'Officiel Italia · Joaillerie",
            "The Jewellery Editor",
            "Robb Report Italia · Watches & Jewellery",
            "Departures Italia",
        ],

        # Drop metadata — list[5] of tuple[2]
        "drop_label":     "Serie Inverno 2026 · scheda tecnica",
        "drop_heading":   "Numerazione e <em>firma</em>.",
        "drop_subhead":
            "Ogni pezzo della serie porta inciso a mano sul retro: il numero "
            "progressivo nella serie, l'anno, e il punzone della casa.",
        "drop_cta":       "Prenotate la visione privata",
        "drop_cta_href":  "concierge",
        "drop_metadata": [
            ("Apertura serie",    "10 dicembre 2025 · solo su invito"),
            ("Apertura pubblica", "10 gennaio 2026 · appuntamento privato"),
            ("Pezzi totali",      "24 esemplari numerati a mano"),
            ("Materiali",         "Platino · oro bianco · oro rosa · zaffiri Ceylon · smeraldi Muzo · brillanti taglio antico"),
            ("Garanzia",          "Sigillo Gemma + certificato GIA per ogni pietra · garanzia di rilavorazione a vita"),
        ],

        # Final private CTA band
        "private_label":      "Per i pezzi su misura",
        "private_heading":    "Su misura · <em>vostro disegno o nostro</em>.",
        "private_intro":
            "L'atelier accetta dieci commissioni di pezzi su misura all'anno · "
            "su disegno della cliente, su disegno di Eleonora, o su disegno "
            "co-firmato. Tempo di lavorazione · da 6 a 18 mesi · NDA reciproco · "
            "scrivete alla direzione di Eleonora.",
        "private_primary":         "Scrivete a Eleonora",
        "private_primary_href":    "concierge",
        "private_secondary":       "Scoprite la casa Gemma",
        "private_secondary_href":  "casa",
    },

    # ─── COLLEZIONE (collection · the 8-piece Serie Inverno 2026) ───
    "collezione": {
        "eyebrow":         "Serie Inverno 2026",
        "headline":        "Otto pezzi · ventiquattro esemplari · una sola firma.",
        "intro":
            "La Serie Inverno 2026 conta otto modelli · ognuno in serie limitata "
            "(tra uno e dodici esemplari per modello · 24 pezzi totali). "
            "Numerazione manuale incisa sul retro · sigillo Gemma · "
            "certificato GIA accluso per ogni pietra centrale.",
        "season_chip":     "Inverno 2026",
        "filter_label":    "Affina la collezione",
        "filter_groups": [
            {
                "label":   "Categoria",
                "options": ["Anelli", "Collane", "Orecchini", "Bracciali", "Orologi", "Diademi"],
            },
            {
                "label":   "Materiale",
                "options": ["Platino", "Oro bianco 18 kt", "Oro rosa 18 kt", "Oro giallo 18 kt", "Argento patinato"],
            },
            {
                "label":   "Pietra centrale",
                "options": ["Brillante", "Zaffiro Ceylon", "Smeraldo Muzo", "Rubino Mogok", "Perla Akoya"],
            },
        ],
        "sort_label":      "Ordina",
        "sort_options": [
            "Per esclusività · pezzo unico prima",
            "Per categoria",
            "Per materiale",
            "Per disponibilità",
        ],
        "result_count":    "Otto pezzi della Serie Inverno 2026",
        "result_subtitle": "Numerazione manuale · sigillo Gemma · certificato GIA accluso",
        "featured_product_id": "anello-brillante-3ct",

        # products — list[8] of dict[9 keys=available,drop,id,image,meta,n,name,price,tag]
        "products": [
            {
                "id":        "anello-brillante-3ct",
                "n":         "N° 01",
                "image":     _ANELLO_BRILLANTE,
                "drop":      "Inverno 2026",
                "name":      "Anello «Cuneo»",
                "meta":      "Brillante 3,02 ct · taglio antico cushion · castone platino · spalle filigranate",
                "price":     "Prezzo su richiesta",
                "tag":       "Pezzo unico · 1/1",
                "available": True,
            },
            {
                "id":        "collana-filigrana-platino",
                "n":         "N° 02",
                "image":     _COLLANA_FILIGRANA,
                "drop":      "Inverno 2026",
                "name":      "Collana «Trama»",
                "meta":      "Filigrana platino 950 · 14 inserti zaffiro Ceylon · chiusura mosquetone firma Gemma",
                "price":     "€ 28 400",
                "tag":       "Serie limitata · 12 esemplari",
                "available": True,
            },
            {
                "id":        "orecchini-zaffiri-ceylon",
                "n":         "N° 03",
                "image":     _ORECCHINI_ZAFFIRO,
                "drop":      "Inverno 2026",
                "name":      "Orecchini «Acqua»",
                "meta":      "Coppia di zaffiri Ceylon non scaldati · 2,18 + 2,14 ct · castone oro bianco 18 kt",
                "price":     "Prezzo su richiesta",
                "tag":       "Pezzo unico · 1/1",
                "available": True,
            },
            {
                "id":        "anello-smeraldo-colombiano",
                "n":         "N° 04",
                "image":     _ANELLO_SMERALDO,
                "drop":      "Inverno 2026",
                "name":      "Anello «Foglia»",
                "meta":      "Smeraldo Muzo 2,47 ct · taglio brillante quadrato · castone oro giallo 18 kt · pavé contorno",
                "price":     "Prezzo su richiesta",
                "tag":       "Pezzo unico · 1/1",
                "available": True,
            },
            {
                "id":        "bracciale-rivière-brillanti",
                "n":         "N° 05",
                "image":     _BRACCIALE_STORIA,
                "drop":      "Inverno 2026",
                "name":      "Bracciale «Rivière»",
                "meta":      "32 brillanti tagli antichi montati su lametta platino · sistema di chiusura firma Gemma",
                "price":     "€ 47 800",
                "tag":       "Serie limitata · 6 esemplari",
                "available": True,
            },
            {
                "id":        "orologio-svizzero-tonneau",
                "n":         "N° 06",
                "image":     _OROLOGIO_SVIZZERO,
                "drop":      "Inverno 2026",
                "name":      "Orologio «Tonneau Gemma»",
                "meta":      "Movimento meccanico manuale calibro Vaucher 1815 · cassa oro rosa · quadrante guilloché manuale",
                "price":     "€ 38 200",
                "tag":       "Serie limitata · 4 esemplari",
                "available": True,
            },
            {
                "id":        "fermasciarpa-cesello",
                "n":         "N° 07",
                "image":     _FERMASCIARPA,
                "drop":      "Inverno 2026",
                "name":      "Fermasciarpa «Cesellato»",
                "meta":      "Oro giallo 18 kt cesellato a mano · motivo geometrico Cusani · piccola perla Akoya centrale",
                "price":     "€ 4 800",
                "tag":       "Serie limitata · 18 esemplari",
                "available": True,
            },
            {
                "id":        "diadema-nuziale-pavé",
                "n":         "N° 08",
                "image":     _DIADEMA_NUZIALE,
                "drop":      "Inverno 2026",
                "name":      "Diadema «Nuziale»",
                "meta":      "Diadema pieghevole su misura · platino 950 · 84 brillanti pavé · castoni rilavorabili",
                "price":     "Prezzo su richiesta",
                "tag":       "Pezzo unico su misura · 1/1",
                "available": False,
            },
        ],

        "footer_note_label": "Prezzi e appuntamenti",
        "footer_note":
            "Il prezzo «su richiesta» si comunica solo in appuntamento "
            "privato · su richiesta scritta accettiamo richieste per pezzo "
            "indicato (nessun listino pubblico). Tutti i prezzi a partire "
            "da 4 800 € · senza IVA agevolata · IVA al 22% inclusa.",
    },

    # ─── PEZZO (product page · featured = anello brillante 3 ct) ────
    "pezzo": {
        "id":           "anello-brillante-3ct",
        "n":            "N° 01",
        "edition_label":"Numerazione",
        "edition_value":"Pezzo unico · 1/1",
        "edition_note": "Numero progressivo inciso a mano sul retro del castone",
        "name":         "Anello «Cuneo»",
        "subtitle":     "Brillante taglio antico cushion 3,02 ct · castone platino",
        "price":        "Prezzo su richiesta",
        "tag":          "Pezzo unico · Serie Inverno 2026",
        "vat_note":     "Iva 22% inclusa nel prezzo · prezzo comunicato solo in appuntamento privato",
        "intro":
            "L'anello «Cuneo» è il pezzo centrale della Serie Inverno 2026. Il "
            "brillante taglio antico cushion di 3,02 carati è stato selezionato "
            "personalmente da Eleonora Gemma all'asta Christie's Ginevra del "
            "maggio 2024 · provenienza documentata · castone platino 950 con "
            "spalle filigranate a mano da Andrea Marinetti, maestro orafo "
            "dell'atelier dal 2008.",

        # gallery — list of scalar URL strings
        "gallery": [
            _ANELLO_BRILLANTE,
            _GOLDSMITH_HANDS,
            _GEMS_CLOSE,
        ],
        "gallery_caption_location": "Atelier Gemma · Milano Brera · novembre 2025",
        "gallery_caption_photo":    "Fotografia · Paolo Roversi",
        "gallery_caption_styling":  "Styling · Camille Bidault-Waddington",

        "size_label":    "Misure disponibili",
        "size_options": ["Misura 11", "Misura 12", "Misura 13", "Misura 14", "Su misura"],
        "color_label":   "Castone",
        "color_options":["Platino 950 (standard)", "Oro bianco 18 kt", "Oro rosa 18 kt", "Oro giallo 18 kt"],

        "atelier_label":     "Mani di",
        "atelier_name":      "Andrea Marinetti",
        "atelier_founded":   "Maestro orafo · in atelier Gemma dal 2008 · diploma Scuola Orafa Valenza 1996",
        "atelier_portrait":  _PORTRAIT_GIUSEPPE,
        "atelier_text":
            "Andrea Marinetti è il maestro orafo dell'atelier Gemma dal 2008. "
            "Si è formato alla Scuola Orafa di Valenza (diploma 1996) · ha "
            "lavorato sei anni da Pomellato e quattro da Bvlgari prima di "
            "entrare in atelier Gemma. Specialista del castone classico e "
            "della filigrana a mano · firma personalmente con il proprio "
            "punzone (AM) accanto al sigillo della casa.",

        "buy_primary":         "Richiedete una visione privata",
        "buy_primary_href":    "concierge",
        "buy_secondary":       "Scrivete a Eleonora",
        "buy_note":
            "Il prezzo si comunica solo in visione privata · NDA reciproco · "
            "pagamento via bonifico bancario · spedizione assicurata Loomis · "
            "ritiro in atelier su appuntamento personale · resa entro 14 "
            "giorni per pezzi non su misura · senza rimborso per pezzi "
            "personalizzati.",

        "info_label": "Scheda tecnica",
        # info_rows — list[10] of tuple[2]
        "info_rows": [
            ("Pietra centrale",  "Brillante 3,02 ct · taglio antico cushion"),
            ("Colore",           "G (top color · GIA color grading)"),
            ("Purezza",          "VS1 (very slight inclusions · GIA clarity)"),
            ("Fluorescenza",     "Faint (impercettibile a occhio nudo)"),
            ("Provenienza",      "Christie's Ginevra · asta maggio 2024 · lotto 247"),
            ("Castone",          "Platino 950 · spalle filigranate a mano"),
            ("Punzone",          "Gemma 117MI · firma Andrea Marinetti AM"),
            ("Garanzia",         "Certificato GIA · sigillo Gemma · rilavorazione a vita"),
            ("Misura standard",  "Misura 13 italiana · ridimensionabile gratis"),
            ("Peso totale",      "8,42 grammi (anello + brillante)"),
        ],

        # care_items — list[5] of tuple[2]
        "care_label":  "Manutenzione",
        "care_intro":
            "Il pezzo richiede una manutenzione semplice · l'atelier offre "
            "pulizia gratuita illimitata in sede e rilavorazione a vita "
            "(saldature, ricastonatura, ridimensionamento, lucidatura).",
        "care_items": [
            ("Pulizia",        "Acqua tiepida + sapone neutro · spazzolino morbido sulla parte inferiore del castone · niente prodotti chimici"),
            ("Conservazione",  "Astuccio rigido in pelle Gemma · ogni pezzo nel proprio · niente contatti con altri pezzi"),
            ("Rilavorazione",  "Servizio gratuito a vita · saldature, ricastonatura, ridimensionamento, lucidatura · solo in atelier Brera"),
            ("Verifica",       "Controllo annuale gratuito · castone, saldature, lente · su appuntamento in atelier"),
            ("Assicurazione",  "Consigliamo assicurazione specifica gioielli · valore di stima fornito gratis con certificato GIA"),
        ],

        "provenance_label":   "Dalla pietra al castone",
        "provenance_heading": "Quattro passaggi tracciati.",
        # provenance_steps — list[4] of 3-tuple (n, t, p) per contract
        "provenance_steps": [
            ("01", "Selezione del brillante",     "Christie's Ginevra · asta maggio 2024 · lotto 247 · selezione personale di Eleonora"),
            ("02", "Certificazione GIA",          "Gemological Institute of America · laboratorio Carlsbad California · certificato 12345678 · agosto 2024"),
            ("03", "Disegno del castone",         "Eleonora Gemma · atelier Brera · settembre 2024 · disegno a mano libera + studio CAD"),
            ("04", "Castone e filigrana",         "Andrea Marinetti · atelier Brera · ottobre-novembre 2025 · 280 ore di lavoro manuale"),
        ],

        "related_label": "Altri pezzi della Serie Inverno",
        "related_intro": "Tre pezzi della stessa serie che possono completare il set.",
        # related_items — list[4] of dict[6 keys=id,image,meta,n,name,price]
        "related_items": [
            {
                "id":    "orecchini-zaffiri-ceylon",
                "n":     "N° 03",
                "image": _ORECCHINI_ZAFFIRO,
                "name":  "Orecchini «Acqua»",
                "meta":  "Zaffiri Ceylon non scaldati · pezzo unico",
                "price": "Prezzo su richiesta",
            },
            {
                "id":    "anello-smeraldo-colombiano",
                "n":     "N° 04",
                "image": _ANELLO_SMERALDO,
                "name":  "Anello «Foglia»",
                "meta":  "Smeraldo Muzo · pezzo unico",
                "price": "Prezzo su richiesta",
            },
            {
                "id":    "bracciale-rivière-brillanti",
                "n":     "N° 05",
                "image": _BRACCIALE_STORIA,
                "name":  "Bracciale «Rivière»",
                "meta":  "32 brillanti antichi · serie limitata",
                "price": "€ 47 800",
            },
            {
                "id":    "collana-filigrana-platino",
                "n":     "N° 02",
                "image": _COLLANA_FILIGRANA,
                "name":  "Collana «Trama»",
                "meta":  "Filigrana platino · serie limitata",
                "price": "€ 28 400",
            },
        ],
    },

    # ─── CASA (about · La casa Gemma) ─────────────────────────
    "casa": {
        "eyebrow":  "La casa Gemma",
        "headline": "Quattro generazioni a Brera. Dal 1908.",
        "intro":
            "L'atelier Gemma è stato fondato nel 1908 dal bisnonno Eligio Gemma "
            "(formato all'orafo Calderoni di Milano · indipendente dal 1908) · "
            "tramandato in linea diretta al figlio Carlo (1932-1986) · al "
            "nipote Giuseppe (1958-vivente · ritirato 2014) · oggi a Eleonora "
            "Gemma (classe 1968 · gemmologa GIA 1994 · ex-Buccellati 1996-2014 "
            "· direttore artistico Gemma dal 2014).",

        "statement_label":   "Cosa è gioielleria d'autore",
        "statement_heading": "Quattro principî della casa.",
        "statement_text":
            "Gioielleria d'autore significa che ogni pezzo porta un nome (non "
            "un codice di catalogo), una firma manuale, un certificato GIA "
            "per ogni pietra di carato superiore, e una garanzia di "
            "rilavorazione a vita. Non vendiamo collezioni infinite né "
            "produciamo in fabbrica · accettiamo dieci commissioni su misura "
            "all'anno · le altre stagioni sono serie limitate da una a "
            "dodici copie per modello.",

        # ateliers — list[3] of dict[7 keys=city,head,image,place,role,since,team]
        # NB: in jewelry register `ateliers` are the locations where the
        # casa works · Brera (Milano · sede storica), Paris (showroom privato),
        # plus visite a domicilio in Roma/Tokyo/Singapore.
        "ateliers_label":   "Le sedi della casa",
        "ateliers_heading": "Milano · Parigi · visite a domicilio.",
        "ateliers_intro":
            "L'atelier storico è in via Brera 28 dal 1908 · sede produttiva e "
            "sala visione. Lo showroom privato di Parigi (Place Vendôme 19) "
            "è aperto su appuntamento privato. Visite a domicilio a Roma, "
            "Tokyo e Singapore su richiesta scritta.",
        "ateliers": [
            {
                "image":  _BRERA_STREET,
                "city":   "Milano · sede storica",
                "place":  "Via Brera 28 · 20121 Milano",
                "role":   "Atelier · sede produttiva · sala visione",
                "head":   "Eleonora Gemma · direttore artistico",
                "since":  "Dal 1908 · 118 anni stessa insegna",
                "team":   "5 orafi · 1 gemmologa · 2 archivio · 1 concierge",
            },
            {
                "image":  _PEZZO_HERO,
                "city":   "Paris · Place Vendôme",
                "place":  "Place Vendôme 19 · 75001 Paris",
                "role":   "Showroom privato · solo su appuntamento",
                "head":   "Marie Lehmann · responsabile Francia · ex-Cartier",
                "since":  "Dal 2018",
                "team":   "1 responsabile · 1 gemmologa · 1 concierge",
            },
            {
                "image":  _HERO_BENCH,
                "city":   "Roma · Tokyo · Singapore",
                "place":  "Visite a domicilio · solo su appuntamento privato",
                "role":   "Eleonora si reca dalle clienti più affezionate · NDA reciproco",
                "head":   "Eleonora Gemma in persona",
                "since":  "Servizio attivo dal 2014",
                "team":   "Eleonora + 1 gemmologa di accompagnamento",
            },
        ],

        "direction_label":             "Direzione",
        "direction_name":              "Eleonora Gemma",
        "direction_role":              "Direttore artistico · gemmologa GIA · quarta generazione · ex-Buccellati 1996-2014",
        "direction_text":
            "Eleonora Gemma (classe 1968) è entrata nell'atelier di famiglia nel "
            "novembre 2014 dopo diciotto anni a Buccellati Roma (1996-2014). "
            "Diploma in storia dell'arte all'Università Cattolica di Milano "
            "(1990), Diploma di gemmologa al Gemological Institute of America "
            "(GIA · Carlsbad California · 1994), specializzazione in pietre "
            "colorate al Gübelin Gem Lab di Lucerna (1995). Ha vinto il Premio "
            "Andrea Palladio per il design gioielli nel 2008 · membro della "
            "giuria del Premio Hèrmes Gioielli dal 2019.",
        "direction_portrait":          _PORTRAIT_ELEONORA,
        "direction_quote":
            "«Mio bisnonno Eligio diceva: il gioiello è uno che porta una donna, "
            "non un oggetto che porta sé stesso. La gioielleria d'autore non "
            "deve mai eclissare chi la porta — deve solo rispondere alla luce.»",
        "direction_quote_attribution": "Eleonora Gemma · intervista a Vogue Gioielli · gennaio 2024",

        # press_items — list[5] of dict[4 keys=byline,issue,magazine,title]
        # NB: in casa/about page · DICT shape (NOT scalar like home.press_items!)
        "press_label":   "Rassegna · le firme della stampa",
        "press_heading": "Quindici anni di rassegna stampa.",
        "press_items": [
            {
                "magazine": "Vogue Gioielli",
                "issue":    "Gennaio 2024 · cover story",
                "title":    "Eleonora Gemma · la quarta generazione",
                "byline":   "Sara Maino",
            },
            {
                "magazine": "L'Officiel Italia · Joaillerie",
                "issue":    "Novembre 2025 · Serie Inverno preview",
                "title":    "L'atelier Gemma riapre via Brera dopo il restauro 2024",
                "byline":   "Beatrice Borelli",
            },
            {
                "magazine": "The Jewellery Editor",
                "issue":    "Aprile 2023 · independent ateliers",
                "title":    "Inside Milan's Gemma · four generations on Via Brera",
                "byline":   "Maria Doulton",
            },
            {
                "magazine": "Robb Report Italia · Watches & Jewellery",
                "issue":    "Marzo 2025 · Top 25 Italia",
                "title":    "Gemma Milano · Top 25 atelier italiani 2025",
                "byline":   "Daniela Mannucci",
            },
            {
                "magazine": "Departures Italia",
                "issue":    "Settembre 2024 · Milano profile",
                "title":    "Where Milan still makes things by hand · Atelier Gemma",
                "byline":   "Caterina Cesari",
            },
        ],

        # numbers_items — list[5] of tuple[2]
        "numbers_label": "La casa Gemma in cifre",
        "numbers_items": [
            ("118",  "Anni di atelier in via Brera · dal 1908"),
            ("4",    "Generazioni in continuità diretta"),
            ("117",  "Punzone della casa registrato a Milano · dal 1948"),
            ("10",   "Commissioni su misura l'anno · numero fisso"),
            ("32",   "Pezzi della Serie Inverno 2026 (24 numerati + 8 modelli)"),
        ],

        "visit_label":          "Per visitare l'atelier",
        "visit_heading":        "Solo su appuntamento privato.",
        "visit_text":
            "L'atelier è aperto solo su appuntamento privato · richiedete una "
            "visita scrivendo al concierge. Per la Serie Inverno 2026 le "
            "visioni private partono il 10 dicembre 2025 (solo su invito) e "
            "dal 10 gennaio 2026 (su appuntamento).",
        "visit_primary":         "Richiedete un appuntamento",
        "visit_primary_href":    "concierge",
    },

    # ─── LOOKBOOK (editorial fotografico della serie) ────────
    "lookbook": {
        "eyebrow":     "Editoriale · Serie Inverno 2026",
        "headline":    "Quattro studi al palazzo Cusani Brera.",
        "intro":
            "Editoriale fotografico della Serie Inverno 2026 · scatti firmati "
            "da Paolo Roversi · stilismo a cura di Camille Bidault-Waddington "
            "· ritratti in palazzo Cusani Brera nelle giornate del 12-14 "
            "novembre 2025 · stampa Gloss Italia di Cremona.",

        "issue_label":  "Numero",
        "issue":        "Volume IV · stagione invernale 2026 · 28 pagine",
        "issue_n":      "IV / 2026",

        "credits_label":  "Crediti",
        # credits_rows — list[6] of tuple[2]
        "credits_rows": [
            ("Fotografia",  "Paolo Roversi (Milano · Parigi)"),
            ("Styling",     "Camille Bidault-Waddington"),
            ("Casting",     "Catherine Wilcockson"),
            ("Pettinature", "Pier Giuseppe Moroni"),
            ("Trucco",      "Christelle Cocquet"),
            ("Modella",     "Constance Jablonski · Viva Models"),
        ],

        "looks_label":    "I quattro studi",
        "looks_intro":
            "Quattro studi · quattro pezzi della collezione fotografati a un "
            "ritratto in palazzo + un still-life · novembre 2025.",
        # looks — list[4] of dict[5 keys=credit,image,n,outfit,title]
        "looks": [
            {
                "n":      "I",
                "image":  _LOOK_EDITORIAL_1,
                "title":  "Studio I · Anello «Cuneo»",
                "outfit": "Abito Valentino · stola Loro Piana · capelli sciolti",
                "credit": "Anello Gemma «Cuneo» N° 01 · brillante 3,02 ct · platino",
            },
            {
                "n":      "II",
                "image":  _LOOK_EDITORIAL_2,
                "title":  "Studio II · Collana «Trama»",
                "outfit": "Pullover Loro Piana cashmere ivory · scollo chiuso",
                "credit": "Collana Gemma «Trama» N° 02 · filigrana platino · zaffiri Ceylon",
            },
            {
                "n":      "III",
                "image":  _LOOK_EDITORIAL_3,
                "title":  "Studio III · Orecchini «Acqua»",
                "outfit": "Camicia in seta Brunello Cucinelli · capelli raccolti",
                "credit": "Orecchini Gemma «Acqua» N° 03 · zaffiri Ceylon non scaldati",
            },
            {
                "n":      "IV",
                "image":  _LOOK_EDITORIAL_4,
                "title":  "Studio IV · Anello «Foglia»",
                "outfit": "Abito Tom Ford verde foresta · manica lunga",
                "credit": "Anello Gemma «Foglia» N° 04 · smeraldo Muzo 2,47 ct",
            },
        ],

        "pullquote":             "«La gioielleria d'autore non deve mai eclissare chi la porta · deve solo rispondere alla luce.»",
        "pullquote_attribution": "Eleonora Gemma · in atelier · novembre 2025",

        # notes_items — list[4] of dict[2 keys=label,text]
        "notes_label": "Note editoriali",
        "notes_intro": "Quattro note dello stilismo, della fotografia e della "
                       "direzione artistica della serie.",
        "notes_items": [
            {
                "label": "Sulla scelta della modella",
                "text":  "Constance Jablonski è stata scelta per la luce diffusa sui suoi tratti · "
                         "non c'è bisogno di flash per fotografare la pietra perché lei stessa "
                         "rispecchia luce diffusa.",
            },
            {
                "label": "Sulla location",
                "text":  "Palazzo Cusani Brera (XVII secolo · scalone monumentale del 1719) è "
                         "stato scelto per la corrispondenza dei marmi alla palette delle "
                         "pietre · niente set artificiale.",
            },
            {
                "label": "Sui colori",
                "text":  "Stile editoriale a luce naturale · niente correzione di colori in "
                         "post-produzione su pietre o metalli · il guilloché manuale dell'orologio "
                         "richiede la luce dell'alba che entra in palazzo.",
            },
            {
                "label": "Sul ritmo",
                "text":  "Quattro studi solo · ognuno con un pezzo solo · ogni pezzo con "
                         "un solo outfit. Niente accumulo · niente stratificazione · "
                         "il pezzo si vede da solo.",
            },
        ],

        "shop_label":     "Visione privata",
        "shop_heading":   "Per vedere i pezzi della serie.",
        "shop_intro":
            "I pezzi della Serie Inverno 2026 sono in visione privata in "
            "atelier Brera dal 10 gennaio 2026 · solo su appuntamento. "
            "Showroom Parigi (Place Vendôme 19) dal 18 gennaio.",
        "shop_primary":         "Richiedete un appuntamento",
        "shop_primary_href":    "concierge",
        "shop_secondary":       "Vedete la collezione",
        "shop_secondary_href":  "collezione",
    },

    # ─── CONCIERGE (contact · concierge dell'atelier) ────────
    "concierge": {
        "eyebrow":  "Concierge dell'atelier · Eleonora Gemma",
        "headline": "Per un appuntamento privato in atelier.",
        "intro":
            "Per richieste di visione, commissione su misura, valutazioni "
            "GIA o appuntamenti privati a Parigi, scrivete al concierge "
            "dell'atelier · Eleonora risponde personalmente entro la "
            "giornata lavorativa · NDA reciproco a disposizione su "
            "richiesta scritta.",

        "form_section_label":   "Richiesta di appuntamento",
        "form_section_intro":
            "Indicate la sede preferita (Brera o Parigi), il pezzo di "
            "interesse e l'eventuale commissione su misura · Eleonora "
            "risponde personalmente entro 24 ore.",
        "form_helper_required": "I campi con · sono obbligatori",
        "form_submit_button":   "Inviate a Eleonora",
        "form_submit_note":
            "La conferma dell'appuntamento avviene per email firmata da "
            "Eleonora · niente sistemi automatici.",

        # form_fields — list[8] of dict[5 keys=label,name,type,required,options]
        "form_fields": [
            {
                "label":    "Nome e cognome",
                "name":     "name",
                "type":     "text",
                "required": True,
                "options":  [],
            },
            {
                "label":    "Email · risposta diretta da Eleonora",
                "name":     "email",
                "type":     "email",
                "required": True,
                "options":  [],
            },
            {
                "label":    "Telefono",
                "name":     "phone",
                "type":     "tel",
                "required": False,
                "options":  [],
            },
            {
                "label":    "Sede preferita",
                "name":     "office",
                "type":     "select",
                "required": True,
                "options":  ["Atelier Brera · Milano", "Showroom privato Place Vendôme · Paris", "Visita a domicilio · Roma · Tokyo · Singapore"],
            },
            {
                "label":    "Pezzo di interesse",
                "name":     "piece",
                "type":     "select",
                "required": False,
                "options":  ["Serie Inverno 2026 · panoramica", "Anello «Cuneo» N° 01", "Collana «Trama» N° 02", "Orecchini «Acqua» N° 03", "Anello «Foglia» N° 04", "Commissione su misura · vostro disegno", "Commissione su misura · nostro disegno", "Senza preferenza"],
            },
            {
                "label":    "Data preferita",
                "name":     "date",
                "type":     "date",
                "required": False,
                "options":  [],
            },
            {
                "label":    "NDA richiesta",
                "name":     "nda",
                "type":     "select",
                "required": False,
                "options":  ["Sì · inviate NDA preliminare", "No · non necessario per questa richiesta"],
            },
            {
                "label":    "Note ad Eleonora",
                "name":     "notes",
                "type":     "textarea",
                "required": False,
                "options":  [],
            },
        ],

        "card_label":   "Sedi e contatti",
        # maison_cards — list[3] of dict[5 keys=address,city,email,hours,phone]
        "maison_cards": [
            {
                "city":    "Milano · atelier storico",
                "address": "Via Brera 28 · 20121 Milano · ingresso privato a corte interna",
                "phone":   "+39 02 8642 1170",
                "email":   "atelier@gemmamilano.it",
                "hours":   "Lun-Sab 10-19 · solo su appuntamento privato · chiuso domeniche e festività",
            },
            {
                "city":    "Paris · Place Vendôme",
                "address": "Place Vendôme 19 · 75001 Paris · piano nobile · ingresso scala A",
                "phone":   "+33 1 4260 1908",
                "email":   "paris@gemmamilano.it",
                "hours":   "Mar-Sab 11-19 · solo su appuntamento privato · responsabile Marie Lehmann",
            },
            {
                "city":    "A domicilio · Roma · Tokyo · Singapore",
                "address": "Visite a domicilio per clienti affezionati · NDA reciproco",
                "phone":   "+39 02 8642 1170 · linea diretta Eleonora",
                "email":   "eleonora@gemmamilano.it",
                "hours":   "Su appuntamento privato · Eleonora si reca personalmente · minimo 4 settimane preavviso",
            },
        ],

        "faq_label": "Domande ricorrenti",
        # faq_items — list[5] of dict[2 keys=q,a]
        # CANONICAL shape (NOT 2-tuples · per artisan-workshop-shape-contract precedent)
        "faq_items": [
            {
                "q": "I prezzi sono pubblici?",
                "a":
                    "No · per i pezzi unici e le commissioni su misura il prezzo si "
                    "comunica solo in appuntamento privato. Per le serie limitate "
                    "(otto pezzi della Serie Inverno 2026 · prezzi da € 4 800 a "
                    "€ 47 800) i prezzi indicativi sono pubblici sulla scheda · "
                    "il prezzo finale dipende dalla scelta di misura, castone e "
                    "personalizzazioni.",
            },
            {
                "q": "Quanto tempo richiede una commissione su misura?",
                "a":
                    "Da 6 a 18 mesi · dipende dalla complessità della scelta delle "
                    "pietre. Il primo appuntamento è di valutazione · il secondo "
                    "è di disegno · il terzo è di approvazione · poi inizia la "
                    "lavorazione. L'atelier accetta dieci commissioni su misura "
                    "all'anno · oltre questo numero rifiutiamo per garantire "
                    "qualità.",
            },
            {
                "q": "Avete una NDA standard?",
                "a":
                    "Sì · per le visioni della Serie Inverno 2026 non è richiesta · "
                    "per le commissioni su misura è obbligatoria. NDA bilaterale · "
                    "5 anni · contiene clausole specifiche per pietre rare "
                    "(provenienza non disclosable). Modello inviato su richiesta "
                    "scritta a Eleonora.",
            },
            {
                "q": "Si possono modificare pezzi esistenti?",
                "a":
                    "Sì · ridimensionamento, ricastonatura, lucidatura, saldature "
                    "sono offerti gratis a vita su pezzi Gemma. Modifiche più "
                    "consistenti (cambio pietra centrale, modifica disegno) si "
                    "valutano caso per caso · sempre in atelier Brera · mai a "
                    "distanza.",
            },
            {
                "q": "Si valutano gioielli antichi · anche non Gemma?",
                "a":
                    "Sì · Eleonora è gemmologa GIA + Gübelin · valutiamo gioielli "
                    "antichi anche di altre case · sia per acquisto (selezione "
                    "Serie Inverno) sia per valutazione fiscale o assicurativa. "
                    "Valutazione GIA-grade € 240 a pezzo · scrivete al concierge "
                    "per appuntamento dedicato.",
            },
        ],
    },
}
