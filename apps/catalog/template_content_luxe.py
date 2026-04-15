"""Luxe — Fashion Store (fashion-editorial archetype) — IT content tree.

Phase 2g3.5 — eCommerce live rollout (Session 41, 2026-04-14).

Voice contract (IT):
- Maison editoriale italiana — Vogue Italia / The Gentlewoman / Net-a-Porter
  register. "Lei" formale (mai "tu"), italian fashion press cadence,
  italic display headlines, captions in micro-grotesk all-caps tracking.
- Concrete details: città maison (Milano, Parigi, Tokyo), tessuti
  (cashmere alpacha, cady doppio strato, organza intrecciata Como, lino
  Belga), atelier (Sentier Parigi, Brera Milano), photographers + stylists
  + magazine references.
- "Lookbook", "drop", "capsule", "private viewing", "lista d'attesa",
  "edizione limitata" — never "checkout" or "carrello": the conversion
  is a private appointment.
- Drop semestrali (Primavera-Estate · Autunno-Inverno), atelier numbers
  (45 capi, 9 silhouettes), runway pinned.

Differentiation contract vs Bottega (D-054 enforcement):
- Luxe is photographically editorial campaign-driven (model portraits,
  runway, atelier interiors, accessori still-life). Bottega is
  photographically tactile (hands at work, raw leather, ceramics, looms).
  Imagery pools must NOT overlap.
- Luxe CTA pattern: private-request (formal, by-appointment, by-list).
  Bottega CTA pattern: phone-and-whatsapp (warm, immediate, by-name).
- Luxe vocabulary: maison · collezione · lookbook · couture · campagna ·
  capsula · drop · private viewing · rsvp · stylist. Bottega vocabulary:
  bottega · artigiano · pezzo unico · edizione · cuoio vegetale ·
  tornito · firma.
- Luxe hero: full-bleed cover LEFT + italic 108px Cormorant headline
  RIGHT on charcoal. Bottega hero: typographic monolith, NO photo.
"""
from __future__ import annotations

from typing import Any


LUXE_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Maison",     "kind": "home"},
        {"slug": "collezione", "label": "Collezione", "kind": "collection"},
        {"slug": "product",    "label": "Look",       "kind": "product"},
        {"slug": "maison",     "label": "Atelier",    "kind": "about"},
        {"slug": "lookbook",   "label": "Lookbook",   "kind": "lookbook"},
        {"slug": "contatti",   "label": "Private",    "kind": "contact"},
    ],

    # Site-wide chrome (consumed by _base.html nav + footer).
    "site": {
        "logo_initial": "L",
        "logo_word":    "Maison Luxe",
        "logo_subline": "Milano · Parigi · Tokyo",
        "tag":          "Atelier · Spring–Summer 2026",
        "phone":        "+39 02 7600 1492",
        "private_phone_label": "Direzione clienti",
        "email":        "private@maisonluxe.com",
        "private_email_label": "Concierge clienti",
        "address":      "Via Senato 28 · 20121 Milano",
        "showroom_paris": "9 rue du Mail · 75002 Paris",
        "showroom_tokyo": "1-1-7 Aoyama · Minato-ku · Tokyo",
        "hours_compact": "Mar – Sab · 11:00 – 19:00 · su appuntamento",
        "hours_footer_rows": [
            "Domenica · privato",
            "Lunedì · chiuso",
        ],
        "license":      "Maison Luxe Srl · P.IVA 11489720152 · CCIAA Milano REA 2589441",
        "footer_intro":
            "Maison fondata a Milano nel 2014 da Giulia Maison con atelier a Parigi e showroom "
            "a Tokyo. Capi disegnati e cuciti tra Milano e Parigi, in serie limitate, "
            "esclusivamente in lista d'attesa. Drop semestrali di quarantacinque capi e nove "
            "silhouette.",

        # Nav reservation CTA (private viewing)
        "nav_cta":      "Richiedi viewing",
        "nav_cta_kind": "appointment",  # links to /contatti/

        # Marketplace footer chrome labels
        "foot_studio":   "La maison",
        "foot_pages":    "Mappa",
        "foot_contact":  "Direzione clienti",
        "foot_offices":  "Atelier & showroom",
        "office_rows": [
            "Milano · Via Senato 28",
            "Parigi · 9 rue du Mail",
            "Tokyo · 1-1-7 Aoyama",
        ],

        # Cross-page meta-strip labels (D-047)
        "currency_symbol":  "€",
        "collection_label": "Collezione",
        "drop_label":       "Drop",
        "season_label":     "Stagione",
        "shipping_label":   "Consegna riservata",
        "shipping_value":   "Corriere maison Milano · 24 ore Italia · 72 ore Europa",
        "viewing_label":    "Private viewing",
        "viewing_value":    "Solo su appuntamento · concierge dedicato",
        "waitlist_label":   "Lista d'attesa",
        "rsvp_label":       "RSVP",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "issue":    "Issue 12 · Primavera '26",
        "issue_label": "Issue",
        "cover_styling_label": "Styling",
        "cover_styling_name":  "Carla Sozzani",
        "cover_label":         "Cover",
        "cover_subject":       "La Muse en Velours",
        "cover_image":
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1600&q=80&auto=format&fit=crop",

        "eyebrow":  "Lookbook · Primavera Estate 2026",
        "headline": "Il nuovo corpo <em>del vestire.</em>",
        "headline_credit_line": "Cinquanta capi · novanta gesti di sartoria",
        "intro":
            "Una sola collezione, tessuta tra Como e Prato, fotografata al Grand Hôtel Villa "
            "d'Este. Drop mensili, esclusivamente per chi è in lista d'attesa. La maison "
            "non vende mai due volte lo stesso capo.",

        "primary_cta":   "Accedi al lookbook",
        "primary_href":  "lookbook",
        "secondary_label":   "Direzione creativa",
        "secondary_name":    "Giulia Maison",

        # Editorial tile strip — 4 silhouettes pinned below hero
        "edition_label":   "Edizione limitata",
        "edition_subline": "quattro pezzi selezionati",
        "tiles": [
            {
                "id":       "rack-atelier",
                "tag":      "Nuovo",
                "name":     "Rack Atelier",
                "price":    "€ 2.480",
                "image":    "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "bomber-siena",
                "tag":      "Capsula",
                "name":     "Bomber Siena",
                "price":    "€ 1.290",
                "image":    "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "pelletteria-isola",
                "tag":      "Atelier",
                "name":     "Borsa Isola",
                "price":    "€ 860",
                "image":    "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "tag":      "Archivio",
                "name":     "Sessione Vogue",
                "price":    "€ 1.940",
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200&q=80&auto=format&fit=crop",
            },
        ],

        # Manifesto / maison statement
        "manifesto_label":   "Maison statement",
        "manifesto_heading": "Quarantacinque capi <em>per stagione, mai uno di più.</em>",
        "manifesto_text":
            "Disegniamo la collezione due volte all'anno, in un atelier di centoquaranta metri "
            "quadri tra Brera e Sentier. Ogni capo viene tagliato a mano, cucito su misura del "
            "cliente, e firmato da chi l'ha realizzato. Niente outlet, niente svendite, niente "
            "marchi rivenduti. Solo ciò che è uscito dalla maison.",

        # Atelier numbers — KPI strip
        "atelier_numbers_label":   "L'atelier in cifre",
        "atelier_numbers": [
            ("12",     "anni di maison"),
            ("45",     "capi per stagione"),
            ("9",      "silhouette firmate"),
            ("3",      "atelier nel mondo"),
        ],

        # Lookbook teaser — editorial 3-tile
        "lookbook_teaser_label":   "Lookbook in corso",
        "lookbook_teaser_heading": "Diciotto immagini, <em>una sola luce.</em>",
        "lookbook_teaser_intro":
            "Fotografato al Grand Hôtel Villa d'Este, sul lago di Como, con luce naturale di "
            "marzo. Stilismo a cura di Carla Sozzani, fotografie di Letizia Carrera, "
            "direzione artistica della maison.",
        "lookbook_teaser_link": "Sfoglia il lookbook",
        "lookbook_teaser_href": "lookbook",
        "lookbook_teaser_tiles": [
            {
                "title":   "Look 03 · Cady doppio strato",
                "credit":  "Stilismo · Carla Sozzani",
                "image":   "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "title":   "Look 09 · Lana cardata di Biella",
                "credit":  "Foto · Letizia Carrera",
                "image":   "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "title":   "Look 14 · Crêpe di seta Como",
                "credit":  "Atelier · Sentier Parigi",
                "image":   "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1000&q=80&auto=format&fit=crop",
            },
        ],

        # Press / editorial mentions strip
        "press_label":   "Editoriale",
        "press_intro":   "Recensita su",
        "press_items":   ["Vogue Italia", "The Gentlewoman", "AnOther Magazine", "Le Monde D'Hermès", "Wallpaper*"],

        # Seasonal drop card
        "drop_label":    "Prossimo drop",
        "drop_heading":  "SS26 · Capsula 04 — <em>la luce di Como.</em>",
        "drop_subhead":  "Apertura lista d'attesa · venerdì 24 aprile, ore 11:00 CET",
        "drop_metadata": [
            ("Capi",       "9 silhouette"),
            ("Materia",    "Crêpe di seta · cady · alpaca"),
            ("Esclusività","12 pezzi per silhouette"),
            ("Apertura",   "Lista d'attesa · venerdì 24 aprile"),
        ],
        "drop_cta":      "Iscriviti alla lista",
        "drop_cta_href": "contatti",

        # Private viewing CTA band
        "private_label":   "Private viewing",
        "private_heading": "Tre saloni, <em>una stanza vuota apposta per Lei.</em>",
        "private_intro":
            "Le maison di Milano, Parigi e Tokyo sono aperte solo su appuntamento. La direzione "
            "clienti riserva un'ora di stanza, prepara i capi del Suo profilo, organizza la "
            "prova con la sarta. Servizio gratuito · concierge dedicato.",
        "private_primary":     "Richiedi un private viewing",
        "private_primary_href":"contatti",
        "private_secondary":   "Vedi gli atelier",
        "private_secondary_href":"maison",
    },

    # ─── COLLEZIONE (shop list) ───────────────────────────────
    "collezione": {
        "season_chip":  "Spring–Summer 2026",
        "eyebrow":      "Collezione completa · drop 04 · capsule 01–04",
        "headline":     "Quarantacinque capi, <em>nove silhouette firmate.</em>",
        "intro":
            "L'intera collezione Spring–Summer 2026, organizzata per silhouette. "
            "Ogni capo è disponibile esclusivamente in lista d'attesa: dalla conferma "
            "alla consegna, da quattro a sei settimane.",

        "filter_label":  "Filtra",
        "filter_groups": [
            {
                "label": "Silhouette",
                "options": ["Tailleur fluido", "Robe-manteau", "Pantalone wide", "Maglieria editoriale", "Pelletteria atelier"],
            },
            {
                "label": "Materia",
                "options": ["Cashmere alpaca", "Cady doppio strato", "Crêpe di seta Como", "Lana cardata Biella", "Cuoio firenze"],
            },
            {
                "label": "Disponibilità",
                "options": ["In showroom", "Lista d'attesa aperta", "Sold-out · su prenotazione"],
            },
        ],
        "sort_label":    "Ordina",
        "sort_options":  ["Per silhouette", "Per drop", "Prezzo crescente", "Novità"],

        "result_count":     "45 capi nella collezione",
        "result_subtitle":  "Aggiornata ogni primo del mese, in coda al drop",

        "products": [
            {
                "id":       "robe-manteau-grigio-perla",
                "n":        "Look 03",
                "name":     "Robe-manteau Grigio Perla",
                "meta":     "Cashmere alpaca doppio · Maglificio Lanifer Biella",
                "drop":     "Drop 01 · Spring 26",
                "price":    "€ 2.840",
                "tag":      "Lista d'attesa",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tailleur-cady-bianco",
                "n":        "Look 07",
                "name":     "Tailleur Cady Bianco",
                "meta":     "Cady doppio strato · Setificio Tessitura Como",
                "drop":     "Drop 02 · Spring 26",
                "price":    "€ 3.420",
                "tag":      "In showroom",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "rack-atelier-nero",
                "n":        "Look 11",
                "name":     "Rack Atelier Nero",
                "meta":     "Cuoio nappa firenze · cucitura sellier",
                "drop":     "Drop 02 · Spring 26",
                "price":    "€ 2.480",
                "tag":      "Lista d'attesa",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "bomber-siena",
                "n":        "Look 14",
                "name":     "Bomber Siena",
                "meta":     "Cady tinto a Siena · ricamo Atelier Sentier",
                "drop":     "Drop 03 · Summer 26",
                "price":    "€ 1.290",
                "tag":      "Capsula",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "pantalone-wide-crepe",
                "n":        "Look 16",
                "name":     "Pantalone Wide Crêpe",
                "meta":     "Crêpe di seta Como · cintura sellier",
                "drop":     "Drop 03 · Summer 26",
                "price":    "€ 1.180",
                "tag":      "Lista d'attesa",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "borsa-isola",
                "n":        "Look 18",
                "name":     "Borsa Isola",
                "meta":     "Cuoio Atelier Firenze · pochette giorno",
                "drop":     "Drop 03 · Summer 26",
                "price":    "€ 860",
                "tag":      "Atelier",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "abito-sera-organza",
                "n":        "Look 22",
                "name":     "Abito Sera Organza",
                "meta":     "Organza intrecciata Como · ricamo Lesage",
                "drop":     "Drop 04 · Summer 26",
                "price":    "€ 4.690",
                "tag":      "Sold-out · prenotabile",
                "available":False,
                "image":    "https://images.unsplash.com/photo-1611042553365-9b101441c135?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "maglia-cashmere-corta",
                "n":        "Look 24",
                "name":     "Maglia Cashmere Corta",
                "meta":     "Cashmere a 12 fili · Maglificio Lanifer Biella",
                "drop":     "Drop 04 · Summer 26",
                "price":    "€ 1.420",
                "tag":      "Lista d'attesa",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "n":        "Look 26",
                "name":     "Sessione Vogue",
                "meta":     "Cappotto archivio · drop 2024 riedizione",
                "drop":     "Archivio · 2024",
                "price":    "€ 1.940",
                "tag":      "Archivio",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
        ],

        "featured_product_id": "rack-atelier-nero",

        "footer_note_label": "Drop 04 in apertura",
        "footer_note":
            "Le iscrizioni a Drop 04 — capsula della luce di Como — aprono venerdì 24 aprile alle "
            "11:00 CET. Le clienti già in lista d'attesa hanno la precedenza assoluta su tutte le "
            "silhouette. Per essere aggiunte alla lista: scrivere alla direzione clienti.",
    },

    # ─── PRODUCT DETAIL ───────────────────────────────────────
    "product": {
        "id":       "rack-atelier-nero",
        "n":        "Look 11 · Drop 02",
        "name":     "Rack Atelier Nero",
        "subtitle": "Cuoio nappa firenze · cucitura sellier · profilo gold",
        "price":    "€ 2.480",
        "vat_note": "IVA inclusa · consegna corriere maison · 24 ore Italia",
        "tag":      "Lista d'attesa · Drop 02 SS26",
        "intro":
            "Borsa giorno-sera in cuoio nappa di Firenze, cucita a mano nell'atelier di Sentier "
            "con cucitura sellier oro a tre lati. Profilo lucidato a cera d'api, fondo rinforzato "
            "in cuoio Vacchetta. Disegnata sul corpo della direttrice creativa, prodotta in "
            "dodici esemplari numerati, firmata sul fondo dall'atelier che l'ha realizzata.",

        "gallery": [
            "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1591561954557-26941169b49e?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1611042553365-9b101441c135?w=1400&q=80&auto=format&fit=crop",
        ],

        # Editorial caption strip below gallery
        "gallery_caption_styling":  "Stilismo · Carla Sozzani",
        "gallery_caption_photo":    "Foto · Letizia Carrera",
        "gallery_caption_location": "Grand Hôtel Villa d'Este · marzo 2026",

        # Right-side info panel — italic captioned
        "info_label":  "Specifiche atelier",
        "info_rows": [
            ("Atelier",      "Sentier · Parigi"),
            ("Materia",      "Nappa firenze · concia vegetale"),
            ("Cucitura",     "Sellier oro a tre lati · filo cerato"),
            ("Profilo",      "Cera d'api · lucidato a mano"),
            ("Fondo",        "Vacchetta rinforzata · piedini ottone"),
            ("Hardware",     "Ottone bagnato in oro 24K"),
            ("Misure",       "32 × 24 × 12 cm · tracolla 105 cm"),
            ("Realizzazione","21 ore di atelier per pezzo"),
        ],

        # Sizing / variant card (silhouette comes in 2 dimensions + 3 tonalities)
        "size_label":    "Dimensione",
        "size_options":  ["Day · 32 × 24", "Evening · 25 × 18"],
        "color_label":   "Tonalità",
        "color_options": ["Nero notte", "Bordeaux Como", "Avorio crema"],

        # Edition note
        "edition_label": "Edizione",
        "edition_value": "12 esemplari numerati · n° 03/12 disponibile",
        "edition_note":
            "Ogni esemplare è marchiato a freddo all'interno con il numero progressivo, "
            "il nome del cucitore principale e la data di consegna in atelier.",

        # Atelier signature
        "atelier_label":   "Firmato dall'atelier",
        "atelier_name":    "Atelier Sentier · Parigi",
        "atelier_founded": "Aperto nel 2017",
        "atelier_text":
            "Atelier di pelletteria a conduzione diretta della maison, in rue du Mail. Sei "
            "sellier formati alle scuole di Hermès e Goyard, una tagliatrice, una cera. "
            "Lavorano esclusivamente per Maison Luxe — nessuna terza parte, nessuna "
            "produzione bianca.",
        "atelier_portrait":
            "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=600&q=80&auto=format&fit=crop",

        # Buy band — private request style
        "buy_primary":   "Richiedi alla maison",
        "buy_primary_href":  "contatti",
        "buy_secondary": "Aggiungi alla lista d'attesa",
        "buy_note":
            "Acquisto su appuntamento o richiesta diretta alla direzione clienti. Acconto del "
            "trenta per cento alla conferma. Consegna in 4–6 settimane dall'ordine, corriere "
            "maison Milano in scatola firmata.",

        # Care section (italic editorial style)
        "care_label":   "Cura del capo",
        "care_intro":
            "La nappa firenze è una pelle viva: prende la forma di chi la porta, ammorbidendosi "
            "nei primi mesi senza mai perdere struttura. Trattata in atelier con cera d'api "
            "neutra, non richiede manutenzione nei primi due anni di uso quotidiano.",
        "care_items": [
            ("Pulizia",     "Panno morbido leggermente umido. Mai prodotti chimici."),
            ("Idratazione", "Cera d'api maison ogni dodici mesi. Stick fornito in dotazione."),
            ("Conservazione","Sacchetto in cotone bio, mai plastica. Mai sole diretto."),
            ("Pioggia",     "Asciugatura naturale all'ombra. Dopo, una passata di cera."),
        ],

        # Atelier provenance
        "provenance_label":   "Provenienza",
        "provenance_heading": "Quattro tappe, <em>quattro firme.</em>",
        "provenance_steps": [
            ("01", "Conceria",       "Conceria della Madonna · Firenze · concia vegetale 45 giorni"),
            ("02", "Taglio",         "Atelier Sentier · Parigi · taglio a mano libera"),
            ("03", "Cucitura sellier","Atelier Sentier · Parigi · 21 ore per pezzo"),
            ("04", "Imballaggio",    "Maison Milano · scatola e cordino firmati"),
        ],

        # Related — three other atelier pieces
        "related_label":   "Dello stesso atelier",
        "related_intro":   "Pelletteria firmata Sentier · Parigi.",
        "related_items": [
            {
                "id":      "borsa-isola",
                "n":       "Look 18",
                "name":    "Borsa Isola",
                "meta":    "Pochette giorno · Atelier Sentier",
                "price":   "€ 860",
                "image":   "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "rack-atelier",
                "n":        "Look 09",
                "name":     "Rack Atelier Crema",
                "meta":     "Borsa giorno · Atelier Sentier",
                "price":    "€ 2.480",
                "image":    "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "n":        "Look 26",
                "name":     "Cappotto Sessione Vogue",
                "meta":     "Cappotto archivio · drop 2024",
                "price":    "€ 1.940",
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
        ],
    },

    # ─── MAISON (about) ───────────────────────────────────────
    "maison": {
        "eyebrow":  "La maison",
        "headline": "Tre città, <em>una sola firma.</em>",
        "intro":
            "Maison Luxe è stata fondata a Milano nel 2014 da Giulia Maison, dopo otto anni "
            "tra Hermès e Bottega Veneta. Oggi disegna due collezioni all'anno, in atelier "
            "tra Brera e Sentier, e riceve solo su appuntamento nelle tre maison di Milano, "
            "Parigi e Tokyo. Quarantacinque capi a stagione, mai uno di più.",

        # Maison statement panel
        "statement_label":   "Statement",
        "statement_heading": "Quarantacinque capi <em>per stagione.</em>",
        "statement_text":
            "La quantità è una scelta editoriale, non una limitazione. Ogni capo deve poter "
            "essere disegnato dalla direttrice creativa, tagliato in atelier, cucito da una "
            "sarta che lo firma, fotografato per il lookbook e seguito personalmente nella "
            "consegna. Quarantacinque è il numero massimo che ci permette di farlo bene.",

        # Atelier cards — 3 cities
        "ateliers_label":   "I tre atelier",
        "ateliers_heading": "Milano, Parigi, <em>Tokyo.</em>",
        "ateliers_intro":
            "Tre case, una sola maison. Milano disegna e dirige. Parigi cuce e ricama. "
            "Tokyo riceve la cliente asiatica in un salone privato di Aoyama.",
        "ateliers": [
            {
                "city":   "Milano",
                "place":  "Via Senato 28 · Brera",
                "role":   "Atelier creativo · direzione · sartoria",
                "since":  "Aperta nel 2014",
                "head":   "Giulia Maison · direttrice creativa",
                "team":   "Sei sarte · due tagliatrici · una direzione clienti",
                "image":  "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=900&q=80&auto=format&fit=crop",
            },
            {
                "city":   "Parigi",
                "place":  "9 rue du Mail · Sentier",
                "role":   "Atelier pelletteria · cucitura sellier",
                "since":  "Aperta nel 2017",
                "head":   "Jean-Luc Berthier · maître sellier",
                "team":   "Sei sellier · una tagliatrice · una cera",
                "image":  "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=900&q=80&auto=format&fit=crop",
            },
            {
                "city":   "Tokyo",
                "place":  "1-1-7 Aoyama · Minato-ku",
                "role":   "Salone privato · ricevimento clienti",
                "since":  "Aperto nel 2021",
                "head":   "Yumi Tanaka · concierge",
                "team":   "Tre concierge · sarta itinerante",
                "image":  "https://images.unsplash.com/photo-1559563458-527698bf5295?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Direction credit
        "direction_label":   "Direzione creativa",
        "direction_name":    "Giulia Maison",
        "direction_role":    "Direttrice creativa · founder",
        "direction_text":
            "Giulia Maison ha studiato a Central Saint Martins di Londra e ha lavorato otto "
            "anni tra Hermès e Bottega Veneta prima di fondare la maison nel 2014. La sua "
            "scrittura è italiana, di Brera, ma la sua mano taglia in francese. La maison "
            "è il suo studio.",
        "direction_portrait":
            "https://images.unsplash.com/photo-1624206112918-f140f087f9b5?w=600&q=80&auto=format&fit=crop",
        "direction_quote":
            "«La quantità è una decisione, non una conseguenza. Quarantacinque capi a stagione "
            "è il numero che ci permette di guardare in faccia ogni cliente.»",
        "direction_quote_attribution": "Giulia Maison · The Gentlewoman, 2025",

        # Press / editorial mentions
        "press_label":   "Editoriale",
        "press_heading": "Apparizioni stampa <em>recenti.</em>",
        "press_items": [
            {
                "magazine": "Vogue Italia",
                "issue":    "Aprile 2026",
                "title":    "Il nuovo silenzio del lusso italiano",
                "byline":   "Servizio · Sara Maino",
            },
            {
                "magazine": "The Gentlewoman",
                "issue":    "Spring 2025",
                "title":    "Forty-five pieces. Never one more.",
                "byline":   "Profile · Penny Martin",
            },
            {
                "magazine": "AnOther Magazine",
                "issue":    "AW25",
                "title":    "L'atelier de Sentier",
                "byline":   "Photo · Mark Borthwick",
            },
            {
                "magazine": "Le Monde D'Hermès",
                "issue":    "Numero 84",
                "title":    "Filiation italienne",
                "byline":   "Texte · Stefano Tonchi",
            },
            {
                "magazine": "Wallpaper*",
                "issue":    "Marzo 2025",
                "title":    "Une maison bien cachée",
                "byline":   "Atelier visit · Tony Chambers",
            },
        ],

        # Numbers
        "numbers_label":   "Cifre della maison",
        "numbers_items": [
            ("12",    "anni dalla fondazione"),
            ("3",     "atelier nel mondo"),
            ("45",    "capi per stagione"),
            ("9",     "silhouette a drop"),
        ],

        # Visit card — 3 cities
        "visit_label":   "Visita la maison",
        "visit_heading": "Tre case, <em>tre saloni privati.</em>",
        "visit_text":
            "Le maison di Milano, Parigi e Tokyo sono aperte solo su appuntamento. La "
            "direzione clienti riserva una stanza, prepara i capi del Suo profilo, e "
            "organizza la prova con la sarta. Servizio gratuito, riservato.",
        "visit_primary":   "Richiedi un appuntamento",
        "visit_primary_href": "contatti",
    },

    # ─── LOOKBOOK ─────────────────────────────────────────────
    "lookbook": {
        "issue":     "Spring–Summer 2026",
        "issue_label":"Issue",
        "issue_n":   "Issue 12",
        "eyebrow":   "Lookbook · Issue 12",
        "headline":  "La luce di <em>Como, in marzo.</em>",
        "intro":
            "Diciotto immagini scattate in tre giornate di marzo al Grand Hôtel Villa d'Este, "
            "sul lago di Como. Stilismo a cura di Carla Sozzani, fotografia di Letizia Carrera, "
            "set design di Sebastiano Pellion di Persano. La luce naturale del mattino è "
            "stata il solo strumento di illuminazione.",

        # Credits panel
        "credits_label":   "Credits",
        "credits_rows": [
            ("Direzione creativa", "Giulia Maison · Maison Luxe Milano"),
            ("Stilismo",           "Carla Sozzani"),
            ("Fotografia",         "Letizia Carrera"),
            ("Set design",         "Sebastiano Pellion di Persano"),
            ("Hair & make-up",     "Lina Hammar · Art + Commerce"),
            ("Modella",            "Sara Grace Wallerstedt · IMG Models"),
            ("Location",           "Grand Hôtel Villa d'Este · Cernobbio"),
            ("Stampa",             "Tiratura analogica · Studio Riffraff Milano"),
        ],

        # Editorial grid — 6 looks
        "looks_label":   "I diciotto look",
        "looks_intro":   "Sei selezionati per la stampa, dodici nella libreria privata.",
        "looks": [
            {
                "n":       "Look 03",
                "title":   "Cady doppio strato",
                "outfit":  "Robe-manteau cady doppio · stivali in cuoio Sentier",
                "credit":  "Stilismo · sciarpa archivio 2018",
                "image":   "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 07",
                "title":   "Tailleur Cady Bianco",
                "outfit":  "Giacca + pantalone wide · scarpe Atelier Sentier · pochette Isola",
                "credit":  "Set · giardino delle camelie",
                "image":   "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 09",
                "title":   "Lana cardata di Biella",
                "outfit":  "Cappotto cardato · pantalone crêpe · stivaletto sellier",
                "credit":  "Cappotto Maglificio Lanifer",
                "image":   "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 11",
                "title":   "Rack Atelier Nero",
                "outfit":  "Maglia cashmere corta · pantalone crêpe · borsa Atelier",
                "credit":  "Borsa Atelier Sentier · 21 ore di lavorazione",
                "image":   "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 14",
                "title":   "Crêpe di seta Como",
                "outfit":  "Bomber Siena · pantalone wide crêpe · sandalo legato",
                "credit":  "Tessuto Setificio Tessitura Como",
                "image":   "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 18",
                "title":   "Borsa Isola · giorno",
                "outfit":  "Maglia cardata · jeans atelier · borsa Isola",
                "credit":  "Borsa Atelier Sentier · pelle Madonna",
                "image":   "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1200&q=80&auto=format&fit=crop",
            },
        ],

        # Editorial pull-quote
        "pullquote":
            "«Como in marzo è una stanza chiusa. La maison ne è uscita con diciotto fotografie "
            "che la rendono leggibile.»",
        "pullquote_attribution": "Carla Sozzani · stilista del lookbook",

        # Notes from set
        "notes_label":   "Note dal set",
        "notes_intro":
            "Tre giornate di marzo, sole velato, vento da nord-est. La modella ha posato senza "
            "interruzioni dalle sette alle undici, alla luce d'arrivo del mattino. La giacca cady "
            "del Look 03 ha richiesto due ore di stiratura ogni mattina per tornare nelle pieghe.",
        "notes_items": [
            {
                "label": "Giorno 01 · Salone delle camelie",
                "text":  "Sette look in cinque ore di luce. Cambio di abito tra una "
                         "ripresa e l'altra in stanza adiacente. Pranzo alle quindici.",
            },
            {
                "label": "Giorno 02 · Belvedere sul lago",
                "text":  "Sei look in luce frontale del mattino. Pioggia leggera tra le undici "
                         "e mezzogiorno: ripresa rinviata al pomeriggio.",
            },
            {
                "label": "Giorno 03 · Salone privato",
                "text":  "Cinque look in luce di candela e finestra. Le ultime tre fotografie "
                         "richieste dalla direttrice creativa per il pullquote di apertura.",
            },
        ],

        # Buy from lookbook CTA
        "shop_label":   "Acquista dal lookbook",
        "shop_heading": "Ogni look porta <em>al capo della collezione.</em>",
        "shop_intro":
            "I diciotto look sono navigabili dalla collezione completa. Per richiedere un capo, "
            "scrivere alla direzione clienti — la lista d'attesa apre venerdì 24 aprile.",
        "shop_primary":     "Vai alla collezione",
        "shop_primary_href":"collezione",
        "shop_secondary":   "Iscriviti alla lista d'attesa",
        "shop_secondary_href":"contatti",
    },

    # ─── CONTATTI (private appointment form) ──────────────────
    "contatti": {
        "eyebrow":  "Direzione clienti privata",
        "headline": "Solo per <em>appuntamento.</em>",
        "intro":
            "La maison riceve esclusivamente su appuntamento, in tre saloni privati a Milano, "
            "Parigi e Tokyo. La direzione clienti prepara i capi del Suo profilo prima del Suo "
            "arrivo, e Le riserva la sarta per la prova. Servizio riservato, gratuito, su "
            "richiesta diretta.",

        # Form intro
        "form_section_label":  "Richiesta privata",
        "form_section_intro":
            "Si prega di compilare la scheda con i dettagli del Suo appuntamento o della Sua "
            "richiesta. La direzione clienti risponde entro la giornata lavorativa successiva. "
            "Per la lista d'attesa di Drop 04 — apertura 24 aprile — selezionare l'opzione "
            "dedicata.",

        "form_helper_required":  "I campi contrassegnati sono obbligatori",
        "form_submit_button":    "Invia richiesta privata",
        "form_submit_note":
            "I Suoi dati sono trattati esclusivamente dalla direzione clienti. Nessuna newsletter, "
            "nessuna comunicazione commerciale.",

        "form_fields": [
            {"name":"titolo",    "label":"Titolo",     "type":"select", "required":True,
             "options":["Sig.ra","Sig.","Mx","Studio·Atelier","Stampa·Press"]},
            {"name":"nome",      "label":"Nome e cognome", "type":"text", "placeholder":"Es. Sig.ra Eleonora Cattaneo", "required":True},
            {"name":"email",     "label":"Email",          "type":"email", "placeholder":"e.cattaneo@esempio.it",      "required":True},
            {"name":"telefono",  "label":"Telefono",       "type":"tel",   "placeholder":"+39 …",                      "required":False},
            {"name":"city",      "label":"Maison di interesse", "type":"select", "required":True,
             "options":["Milano · Via Senato","Parigi · Sentier","Tokyo · Aoyama","Indifferente"]},
            {"name":"servizio",  "label":"Servizio richiesto", "type":"select", "required":True,
             "options":["Private viewing","Lista d'attesa Drop 04","Capo su misura","Riedizione archivio","Stampa & press"]},
            {"name":"capo",      "label":"Look o capo (opz.)", "type":"text", "placeholder":"Es. Look 11 · Rack Atelier Nero", "required":False},
            {"name":"messaggio", "label":"Note alla direzione clienti", "type":"textarea", "placeholder":"Specificare data preferita, taglie, profilo personale.", "required":True, "rows":5},
        ],

        # Right-side card — three maison addresses
        "card_label":   "Le tre maison",
        "maison_cards": [
            {
                "city":    "Milano",
                "address": "Via Senato 28 · 20121 Milano",
                "phone":   "+39 02 7600 1492",
                "email":   "milano@maisonluxe.com",
                "hours":   "Mar – Sab · 11:00 – 19:00 · solo su appuntamento",
            },
            {
                "city":    "Parigi",
                "address": "9 rue du Mail · 75002 Paris",
                "phone":   "+33 1 4296 4720",
                "email":   "paris@maisonluxe.com",
                "hours":   "Mar – Ven · 11:00 – 19:00 · solo su appuntamento",
            },
            {
                "city":    "Tokyo",
                "address": "1-1-7 Aoyama · Minato-ku · Tokyo 107-0062",
                "phone":   "+81 3 6450 5018",
                "email":   "tokyo@maisonluxe.com",
                "hours":   "Mer – Sab · 12:00 – 20:00 · solo su appuntamento",
            },
        ],

        # FAQ accordion (private viewing oriented)
        "faq_label":   "Domande frequenti",
        "faq_items": [
            {
                "q": "Quanto tempo prima si prenota un private viewing?",
                "a": "Almeno una settimana di anticipo per Milano e Parigi; due settimane per "
                     "Tokyo. Per richieste urgenti, scrivere direttamente alla direzione clienti.",
            },
            {
                "q": "Si paga il servizio di private viewing?",
                "a": "No, è gratuito e riservato. Comprende preparazione dei capi, sarta in "
                     "salone, caffè e champagne, e una mappa della collezione personalizzata.",
            },
            {
                "q": "Si può richiedere un capo su misura?",
                "a": "Sì, sulla base delle silhouette esistenti. Tempi di consegna: da otto a "
                     "dodici settimane. Acconto del cinquanta per cento alla conferma del disegno.",
            },
            {
                "q": "Come funziona la lista d'attesa?",
                "a": "Le iscritte alla lista hanno la precedenza assoluta su tutti i drop. La "
                     "lista non comporta alcun obbligo di acquisto. Iscrizione gratuita, su "
                     "richiesta diretta.",
            },
        ],
    },
}
