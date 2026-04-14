"""Bottega — Shop Artigianale (artisan-workshop archetype) — IT content tree.

Phase 2g3.5 — eCommerce live rollout (Session 41, 2026-04-14).

Voice contract (IT):
- Familiar warm soulful Toscana artisan register
- "tu" form throughout — the bottega speaks like a friendly maker, never
  marketing-speak. Soulful, never glossy.
- Concrete details: città (Santa Croce sull'Arno, Montelupo Fiorentino,
  Prato, Greve in Chianti), materiali (cuoio conciato al vegetale,
  ceramica smaltata, lino grezzo), gesti (battere, tornire, tessere).
- Edition numbers (N° 042, 3/8) + signed-by-the-maker proof everywhere.
- Phone-and-WhatsApp conversion pattern: WhatsApp visible in nav CTA,
  phone in footer, "visita la bottega" as primary hero CTA — never
  "checkout" as if a real cart exists.

Differentiation contract vs Luxe (D-054 enforcement):
- Bottega is photographically tactile (hands at work, raw leather,
  ceramic on wheel, looms, market produce). Luxe is photographically
  editorial (campaign portraits, runway, atelier interiors). Imagery
  pools must NOT overlap.
- Bottega CTA pattern: phone-and-whatsapp (warm, immediate, by-name).
  Luxe CTA pattern: private-request (formal, by-appointment).
- Bottega vocabulary: bottega · artigiano · pezzo unico · edizione ·
  cuoio vegetale · tornito · tessuto · firma. Luxe vocabulary: maison ·
  collezione · lookbook · couture · campagna · capsula · drop ·
  private viewing.
"""
from __future__ import annotations

from typing import Any


BOTTEGA_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Bottega",   "kind": "home"},
        {"slug": "shop",     "label": "Catalogo",  "kind": "shop"},
        {"slug": "product",  "label": "Pezzo",     "kind": "product"},
        {"slug": "atelier",  "label": "Atelier",   "kind": "about"},
        {"slug": "journal",  "label": "Quaderno",  "kind": "journal"},
        {"slug": "contatti", "label": "Contatti",  "kind": "contact"},
    ],

    # Site-wide chrome (consumed by _base.html nav + footer).
    "site": {
        "logo_initial": "M",
        "logo_word":    "La Bottega di Martino",
        "tag":          "Firenze · dal 1968 · fatto a mano",
        "phone":        "+39 055 234 11 90",
        "whatsapp":     "055 234 11 90",
        "whatsapp_link": "https://wa.me/390552341190",
        "email":        "bottega@bottegadimartino.it",
        "address":      "Via dei Serragli 47/r · 50124 Firenze",
        "hours_compact": "Mar – Sab · 10:00 – 19:30",
        "hours_footer_rows": [
            "Domenica · solo su appuntamento",
            "Lunedì · chiuso",
        ],
        "license":      "P.IVA 04891240484 · CCIAA Firenze REA 502118",
        "footer_intro":
            "Bottega artigiana fondata nel 1968 da Martino Boncompagni. "
            "Cuoio, ceramica e tessuti fatti a mano in Toscana, in piccole edizioni "
            "che non si ripetono. Spedizione in 48 ore in Italia, due giorni in più "
            "in Europa.",
        # Nav CTA — primary action button next to nav links
        "nav_cta":      "Visita la bottega",
        "nav_cta_kind": "appointment",  # links to /contatti/

        # Marketplace footer chrome labels
        "foot_studio":   "La bottega",
        "foot_pages":    "Mappa del sito",
        "foot_contact":  "Bottega & ordini",
        "foot_stockists":"Stockists selezionati",
        "stockists_rows": [
            "10 Corso Como · Milano",
            "Eataly Lingotto · Torino",
            "Spazio B**K · Milano",
            "Atelier Pitti · Firenze",
        ],

        # Cross-page meta-strip labels (D-047 lifts on shop/product/atelier)
        "currency_symbol":  "€",
        "shop_filter_label": "Filtri",
        "shop_count_unit":   "pezzi",
        "edition_label":     "Edizione",
        "made_in_label":     "Fatto a",
        "artisan_label":     "Firmato da",
        "material_label":    "Materiale",
        "shipping_label":    "Spedizione",
        "shipping_value":    "48 ore in Italia · 4 giorni in Europa",
        "guarantee_label":   "Garanzia",
        "guarantee_value":   "Riparazione gratuita per due anni",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Catalogo autunno · edizione 47",
        "headline": "Pezzi unici cuciti, tornìti e tessuti <em>in bottega.</em>",
        "intro":
            "Cuoio conciato al vegetale a Santa Croce sull'Arno, ceramiche tornite a Montelupo "
            "Fiorentino, lino tessuto a Prato. Ogni pezzo porta la firma dell'artigiano che l'ha "
            "fatto — e un numero progressivo che non si ripete mai.",
        "primary_cta":   "Visita la bottega",
        "primary_href":  "contatti",
        "secondary_cta": "Sfoglia il catalogo",
        "secondary_href":"shop",

        # Stamp-aside data — the rubber-stamped right column of the hero
        "stamp_label":  "La nostra regola",
        "stamp_heading":"Tre mani, <em>un oggetto.</em>",
        "stamp_rows": [
            ("Artigiani",   "12 botteghe"),
            ("Materiali",   "100% italiani"),
            ("Edizione",    "Mai sopra 50"),
            ("Spedizione",  "In 48 ore"),
        ],
        "stamp_footer": "Scritto a mano · impacchettato in bottega",
        "stamp_corner_index": "01",
        "stamp_corner_word":  "LA BOTTEGA",

        # Latest-arrived band — 4 product cards
        "latest_label":   "Le ultime arrivate",
        "latest_heading": "Appena uscite <em>dal banco da lavoro.</em>",
        "latest_link_label": "Tutto il catalogo",
        "latest_link_href":  "shop",
        "latest_items": [
            {
                "id":       "giubbotto-terra",
                "n":        "N° 042",
                "edition":  "3 / 8",
                "name":     "Giubbotto Terra",
                "meta":     "Cuoio vegetale · Santa Croce",
                "price":    "€ 420",
                "tag":      "Pezzo unico",
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "camicia-lino",
                "n":        "N° 108",
                "edition":  "1 / 6",
                "name":     "Camicia di lino",
                "meta":     "Lino grezzo · Prato",
                "price":    "€ 95",
                "tag":      "Fatto a mano",
                "image":    "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "ceramica-cucina",
                "n":        "N° 213",
                "edition":  "7 / 24",
                "name":     "Set da cucina",
                "meta":     "Ceramica smaltata · Montelupo",
                "price":    "€ 148",
                "tag":      "Edizione",
                "image":    "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "conserve-chianti",
                "n":        "N° 317",
                "edition":  "12 / 60",
                "name":     "Conserve del mercato",
                "meta":     "Pomodorini · Chianti",
                "price":    "€ 18",
                "tag":      "Stagione",
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Makers band — 4 artisans with portrait
        "makers_label":   "Mani che firmano",
        "makers_heading": "Dodici botteghe, <em>una sola insegna.</em>",
        "makers_intro":
            "Lavoriamo solo con artigiani che conosciamo per nome. "
            "Ogni pezzo che esce dalla nostra insegna porta la loro firma — "
            "perché chi l'ha fatto ha il diritto di metterci la faccia.",
        "makers": [
            {
                "name":   "Severino Falchi",
                "craft":  "Maestro conciatore",
                "place":  "Santa Croce sull'Arno",
                "since":  "Dal 1989 in bottega",
                "quote":  "«Il cuoio buono lo riconosci dall'odore. Se sa di chimica, non l'abbiamo conciato noi.»",
                "portrait": "https://images.unsplash.com/photo-1581094271901-8022df4466f9?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Caterina Lippi",
                "craft":  "Tornitrice di terraglie",
                "place":  "Montelupo Fiorentino",
                "since":  "Bottega aperta nel 2003",
                "quote":  "«Ogni pezzo torna in forno tre volte. Se al terzo non canta, lo rompo.»",
                "portrait": "https://images.unsplash.com/photo-1604881991720-f91add269bed?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Bruno Ricci",
                "craft":  "Tessitore di lino",
                "place":  "Prato · Via del Telaio",
                "since":  "Telaio a mano dal 1976",
                "quote":  "«Il lino grezzo è una pianta. Va trattato come il pane: con calma e con fame.»",
                "portrait": "https://images.unsplash.com/photo-1521119989659-a83eee488004?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Adele Pignatelli",
                "craft":  "Conserviera del Chianti",
                "place":  "Greve in Chianti",
                "since":  "Tre generazioni di vasetti",
                "quote":  "«La marmellata si fa quando la frutta vuole. Non quando lo decide il calendario.»",
                "portrait": "https://images.unsplash.com/photo-1607743386760-88ac62b89b8a?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Provenance trio — 3 cards on materials & places
        "provenance_label":   "Provenienza",
        "provenance_heading": "Tre territori, <em>tre materie.</em>",
        "provenance_intro":
            "Niente arriva da più di duecento chilometri. La materia prima è la prima firma "
            "dell'artigiano: se sa dirti dove l'ha presa, ti sta dicendo come l'ha lavorata.",
        "provenance_items": [
            {
                "icon":  "01",
                "title": "Cuoio del Valdarno",
                "desc":  "Conciato al vegetale con corteccia di castagno e mimosa. "
                         "Quaranta giorni in vasca, mai cromo, mai scorciatoie. "
                         "Fornitore unico: Conceria Falchi, Santa Croce sull'Arno.",
                "place": "Santa Croce sull'Arno · 38 km da Firenze",
            },
            {
                "icon":  "02",
                "title": "Argilla di Montelupo",
                "desc":  "Argilla rossa locale, smaltata a freddo con ossidi naturali. "
                         "Tre cotture a 980° in forno a legna. Tornitura a mano libera.",
                "place": "Montelupo Fiorentino · 22 km da Firenze",
            },
            {
                "icon":  "03",
                "title": "Lino di Prato",
                "desc":  "Lino grezzo non sbiancato, tessuto a telaio meccanico anni '50. "
                         "Trama larga, ordito stretto. Ogni rotolo ha un peso diverso.",
                "place": "Prato · 24 km da Firenze",
            },
        ],

        # Care / guarantee strip
        "care_label":   "Garanzie & cura",
        "care_heading": "Riparato in bottega, <em>per sempre.</em>",
        "care_items": [
            ("Riparazione gratuita due anni",
             "Manico scucito, smaltato sbeccato, ricamo allentato: lo aggiustiamo noi, in bottega."),
            ("Reso accettato sette giorni",
             "Se il pezzo non ti convince, lo riportiamo in bottega senza spese e senza domande."),
            ("Spedizione in 48 ore",
             "Spediamo da Firenze il giorno dopo l'ordine, in pacco di carta pesante e cordino."),
            ("Pagamento sicuro",
             "Carta o bonifico. Niente abbonamenti, niente account, niente cookie pubblicitari."),
        ],

        # Press / stockists strip
        "press_label":   "Si parla di noi",
        "press_items":   ["Vogue Italia", "Domus", "La Repubblica", "Apartamento", "Cereal Magazine"],

        "journal_teaser_label":   "Dal quaderno",
        "journal_teaser_heading": "Note di lavoro, <em>scritte a mano.</em>",
        "journal_teaser_link":    "Apri il quaderno",
        "journal_teaser_href":    "journal",

        # Final CTA band
        "cta_label":   "Visita la bottega",
        "cta_heading": "Vieni a trovarci a Firenze, <em>ti facciamo un caffè.</em>",
        "cta_intro":
            "La bottega è in via dei Serragli, a quattro passi da Pitti. Aperta da martedì a "
            "sabato, dieci alle diciannove e mezza. Ti facciamo vedere come si concia il cuoio, "
            "come si tornisce un piatto e — se vuoi — ti presentiamo gli artigiani di persona.",
        "cta_primary":   "Prenota una visita",
        "cta_primary_href": "contatti",
        "cta_secondary": "Scrivi su WhatsApp",
        # cta_secondary_href is rendered as site.whatsapp_link
    },

    # ─── SHOP ─────────────────────────────────────────────────
    "shop": {
        "eyebrow":  "Catalogo · 47ª edizione",
        "headline": "Tutto il <em>banco da lavoro,</em> aperto.",
        "intro":
            "Quarantasette pezzi unici, dodici artigiani, tre territori. "
            "Ogni numero è progressivo dal 1968 e non si ripete mai. Filtra per "
            "materia, per artigiano o per disponibilità.",

        "filter_section_label": "Filtra per",
        "filter_groups": [
            {
                "label": "Materia",
                "options": ["Cuoio", "Ceramica", "Lino & tessuti", "Conserve", "Carta & legature"],
            },
            {
                "label": "Artigiano",
                "options": ["Severino Falchi", "Caterina Lippi", "Bruno Ricci", "Adele Pignatelli", "Tutti"],
            },
            {
                "label": "Disponibilità",
                "options": ["In bottega", "Su prenotazione", "Edizione esaurita"],
            },
        ],

        "sort_label": "Ordina per",
        "sort_options": ["Ultimi arrivati", "Numero progressivo", "Prezzo crescente", "Prezzo decrescente"],

        "result_count":    "47 pezzi attualmente in catalogo",
        "result_subtitle": "Aggiornato di lunedì mattina, prima dell'apertura della bottega",

        "products": [
            {
                "id":       "giubbotto-terra",
                "n":        "N° 042",
                "edition":  "3 / 8",
                "name":     "Giubbotto Terra",
                "meta":     "Cuoio vegetale tinto a mano",
                "place":    "Santa Croce sull'Arno",
                "artisan":  "Severino Falchi",
                "price":    "€ 420",
                "tag":      "Pezzo unico",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "borsa-cartolina",
                "n":        "N° 056",
                "edition":  "2 / 12",
                "name":     "Borsa Cartolina",
                "meta":     "Cuoio naturale + cucitura a sella",
                "place":    "Santa Croce sull'Arno",
                "artisan":  "Severino Falchi",
                "price":    "€ 280",
                "tag":      "Pezzo unico",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "camicia-lino",
                "n":        "N° 108",
                "edition":  "1 / 6",
                "name":     "Camicia di lino",
                "meta":     "Lino grezzo non sbiancato",
                "place":    "Prato",
                "artisan":  "Bruno Ricci",
                "price":    "€ 95",
                "tag":      "Fatto a mano",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tovaglia-armaiolo",
                "n":        "N° 134",
                "edition":  "5 / 30",
                "name":     "Tovaglia Armaiolo",
                "meta":     "Lino & cotone · trama larga",
                "place":    "Prato",
                "artisan":  "Bruno Ricci",
                "price":    "€ 165",
                "tag":      "Edizione",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "ceramica-cucina",
                "n":        "N° 213",
                "edition":  "7 / 24",
                "name":     "Set da cucina",
                "meta":     "Ceramica smaltata a freddo",
                "place":    "Montelupo Fiorentino",
                "artisan":  "Caterina Lippi",
                "price":    "€ 148",
                "tag":      "Edizione",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tazze-tornite",
                "n":        "N° 219",
                "edition":  "11 / 24",
                "name":     "Tazze Tornite",
                "meta":     "Argilla rossa locale · cottura a legna",
                "place":    "Montelupo Fiorentino",
                "artisan":  "Caterina Lippi",
                "price":    "€ 78",
                "tag":      "Edizione",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1610701596007-11502861dcfa?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "vassoio-noce",
                "n":        "N° 251",
                "edition":  "Esaurito",
                "name":     "Vassoio in noce",
                "meta":     "Noce massello · finitura ad olio",
                "place":    "Pratovecchio",
                "artisan":  "Severino Falchi",
                "price":    "€ 210",
                "tag":      "Lista d'attesa",
                "available": False,
                "image":    "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "conserve-chianti",
                "n":        "N° 317",
                "edition":  "12 / 60",
                "name":     "Conserve del mercato",
                "meta":     "Pomodorini cuore di bue + olio EVO",
                "place":    "Greve in Chianti",
                "artisan":  "Adele Pignatelli",
                "price":    "€ 18",
                "tag":      "Stagione",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "marmellata-fichi",
                "n":        "N° 322",
                "edition":  "21 / 80",
                "name":     "Marmellata di fichi",
                "meta":     "Fichi neri di settembre · cottura lenta",
                "place":    "Greve in Chianti",
                "artisan":  "Adele Pignatelli",
                "price":    "€ 14",
                "tag":      "Stagione",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Featured product detail link — used by smoke and "see more"
        "featured_product_id": "giubbotto-terra",

        "footer_note_label": "Bottega",
        "footer_note":
            "Niente algoritmi, niente raccomandazioni: il catalogo è ordinato come sui ripiani "
            "della bottega. Se cerchi un pezzo specifico, scrivici su WhatsApp — ti rispondiamo "
            "noi, una persona alla volta.",
    },

    # ─── PRODUCT (detail) ─────────────────────────────────────
    "product": {
        # Hero (uses featured_product_id from shop)
        "id":       "giubbotto-terra",
        "n":        "N° 042",
        "edition":  "3 / 8",
        "edition_note": "Edizione di otto pezzi · ne restano tre",
        "name":     "Giubbotto Terra",
        "subtitle": "Cuoio conciato al vegetale · cucito a sella · tinto a mano",
        "price":    "€ 420",
        "vat_note": "IVA inclusa · spedizione 48 ore in Italia",
        "intro":
            "Un giubbotto corto in cuoio del Valdarno, conciato al vegetale per quaranta giorni "
            "con corteccia di castagno e mimosa. La tinta è data a mano con un panno di lino imbevuto "
            "di pigmento naturale terra di Siena: ogni pezzo prende il colore in modo leggermente "
            "diverso e nessuno è mai uguale al precedente.",

        "gallery": [
            "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=1200&q=80&auto=format&fit=crop",
        ],

        # Right-side info aside (the rubber-stamped data block)
        "info_label":  "Specifiche",
        "info_rows": [
            ("Materia",      "Cuoio del Valdarno · concia vegetale"),
            ("Spessore",     "1,8 mm uniforme"),
            ("Tinta",        "Terra di Siena · pigmento naturale"),
            ("Cucitura",     "Punto sella, filo cerato"),
            ("Fodera",       "Lino grezzo non sbiancato"),
            ("Bottoni",      "Corno di bue · provenienza Toscana"),
            ("Peso",         "780 g (taglia M)"),
            ("Realizzazione","11 giorni di bottega"),
        ],

        # Sizing card
        "size_label":    "Taglie disponibili",
        "size_intro":    "Su misura possibile entro tre settimane. Scrivici su WhatsApp.",
        "size_options":  ["S", "M", "L", "XL", "Su misura"],
        "size_chart_link": "Guarda la guida alle taglie",
        "size_chart_href": "atelier",

        # Made by
        "artisan_label": "Firmato da",
        "artisan_name":  "Severino Falchi",
        "artisan_role":  "Maestro conciatore · in bottega dal 1989",
        "artisan_bio":
            "Severino concia il cuoio nella sua vasca dal 1989. Lavora con due figli e un nipote, "
            "e tinge ogni pelle a mano. Il suo motto in conceria è 'piano è meglio'.",
        "artisan_portrait":
            "https://images.unsplash.com/photo-1581094271901-8022df4466f9?w=400&q=80&auto=format&fit=crop",

        # Buy band
        "buy_primary":   "Aggiungi al cesto",
        "buy_secondary": "Scrivi su WhatsApp",
        "buy_note":
            "Carta, bonifico o pagamento alla consegna se ritiri in bottega. "
            "Spediamo entro 48 ore, in scatola di carta pesante e cordino.",

        # Care
        "care_label":   "Cura del pezzo",
        "care_intro":
            "Il cuoio vegetale chiede poco e dura una vita. Lo abbiamo già trattato in conceria "
            "con olio di lino crudo. Per i primi mesi cambierà colore di poco, schiarendosi nelle "
            "pieghe — è normale e voluto.",
        "care_items": [
            ("Pulizia",     "Panno asciutto. Mai detersivi, mai alcool."),
            ("Idratazione", "Olio di lino o crema neutra una volta l'anno."),
            ("Riparazione", "Per due anni la facciamo gratuitamente in bottega."),
            ("Pioggia",     "Asciuga lontano dalle fonti di calore. Niente asciugacapelli."),
        ],

        # Provenance map
        "provenance_label":   "Provenienza",
        "provenance_heading": "Tre tappe, <em>quaranta chilometri.</em>",
        "provenance_steps": [
            ("01", "Conceria",     "Conceria Falchi · Santa Croce sull'Arno · 38 km"),
            ("02", "Tintura",      "Bottega di Martino · Firenze · 0 km"),
            ("03", "Cucitura",     "Bottega di Martino · Firenze · 0 km"),
            ("04", "Imballaggio",  "Carta da pane di Greve in Chianti · 32 km"),
        ],

        # Related products band
        "related_label":   "Anche dalla stessa mano",
        "related_intro":   "Pezzi nati nello stesso laboratorio, dalla stessa firma.",
        "related_items": [
            {
                "id":      "borsa-cartolina",
                "n":       "N° 056",
                "name":    "Borsa Cartolina",
                "meta":    "Cuoio naturale · Severino Falchi",
                "price":   "€ 280",
                "image":   "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":      "vassoio-noce",
                "n":       "N° 251",
                "name":    "Vassoio in noce",
                "meta":    "Noce massello · Severino Falchi",
                "price":   "€ 210",
                "image":   "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":      "ceramica-cucina",
                "n":       "N° 213",
                "name":    "Set da cucina",
                "meta":    "Ceramica smaltata · Caterina Lippi",
                "price":   "€ 148",
                "image":   "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
        ],
    },

    # ─── ATELIER (about) ──────────────────────────────────────
    "atelier": {
        "eyebrow":  "L'atelier di via dei Serragli",
        "headline": "Una bottega <em>di bottega.</em>",
        "intro":
            "Aperta nel 1968 da Martino Boncompagni, oggi è uno spazio di centodieci metri quadri "
            "in via dei Serragli, dove dodici artigiani toscani portano i loro pezzi tre volte a "
            "settimana. Niente magazzino centrale, niente catena — tutto quello che vedi in "
            "vetrina viene fatto a meno di duecento chilometri da qui.",

        # Mission stamp panel
        "mission_label":   "La regola della bottega",
        "mission_heading": "Tre mani, un oggetto. <em>Sempre.</em>",
        "mission_text":
            "Ogni pezzo passa per tre mani: chi lavora la materia prima, chi la rifinisce, chi "
            "controlla che il numero progressivo sia scritto a penna prima della spedizione. "
            "Nessun macchinario sostituisce l'ultima firma. Se non riusciamo a far passare un "
            "pezzo per tre mani, non lo facciamo.",

        # Process timeline — 5 steps
        "process_label":   "Il percorso",
        "process_heading": "Dalla materia prima <em>al cordino.</em>",
        "process_steps": [
            {
                "n":    "01",
                "title":"Si va a prendere la materia",
                "place":"Valdarno · Mugello · Chianti",
                "desc": "Cuoio dalle concerie del Valdarno, argilla rossa da Montelupo, "
                        "lino dai telai di Prato. Andiamo personalmente, mai per corriere.",
                "duration": "Una settimana al mese",
            },
            {
                "n":    "02",
                "title":"Si lascia riposare",
                "place":"Bottega · stanza dietro",
                "desc": "Il cuoio sta in vasca quaranta giorni. L'argilla si asciuga lentamente "
                        "all'aria. Il lino aspetta che cambi il tempo. Nessun ciclo accelerato.",
                "duration": "Da due settimane a tre mesi",
            },
            {
                "n":    "03",
                "title":"Si lavora a mano",
                "place":"Banco da lavoro · vetrata sul giardino",
                "desc": "Il pezzo prende forma sotto le mani dell'artigiano principale. "
                        "Cucitura a sella, tornitura libera, telaio meccanico anni '50.",
                "duration": "Da quattro a dodici giorni",
            },
            {
                "n":    "04",
                "title":"Si rifinisce",
                "place":"Bottega · banco di Anna",
                "desc": "Anna controlla, leviga, tinge. Aggiunge il numero progressivo. "
                        "Se non passa il suo controllo, torna indietro al banco principale.",
                "duration": "Mezza giornata per pezzo",
            },
            {
                "n":    "05",
                "title":"Si impacchetta",
                "place":"Bottega · banco dell'imballaggio",
                "desc": "Carta da pane di Greve, cordino di canapa, biglietto scritto a mano "
                        "con il nome di chi ha fatto il pezzo. Spediamo da Firenze in 48 ore.",
                "duration": "Stesso giorno della spedizione",
            },
        ],

        # Founder
        "founder_label":   "Chi siamo",
        "founder_heading": "Martino, Anna, <em>e dodici botteghe.</em>",
        "founder_text":
            "Martino ha aperto nel '68 con un banco di tre metri e una balla di cuoio. Oggi gestisce "
            "la bottega con la nipote Anna — lui sta più al banco, lei si occupa di chi entra, di chi "
            "telefona, di chi scrive. Insieme tengono i rapporti con i dodici artigiani. Senza mai "
            "diventare un'azienda.",
        "founder_portrait":
            "https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=600&q=80&auto=format&fit=crop",
        "founder_caption":
            "Martino Boncompagni e Anna Boncompagni · Bottega di via dei Serragli, Firenze",

        # Numbers stamp
        "numbers_label":   "Cifre della bottega",
        "numbers_items": [
            ("57",     "anni di apertura ininterrotta"),
            ("12",     "artigiani che firmano per noi"),
            ("47ª",    "edizione del catalogo"),
            ("0",      "macchinari industriali"),
        ],

        # Visit card
        "visit_label":   "Vienici a trovare",
        "visit_heading": "Via dei Serragli 47/r, <em>a quattro passi da Pitti.</em>",
        "visit_text":
            "La bottega è aperta da martedì a sabato, dalle dieci alle diciannove e mezza. La domenica "
            "solo su appuntamento. Se vieni il giovedì pomeriggio, c'è di solito qualche artigiano in "
            "visita per consegnare i pezzi. Caffè e libro degli ospiti pronti.",
        "visit_primary":   "Prenota una visita",
        "visit_primary_href": "contatti",
        "visit_secondary": "Scrivi su WhatsApp",
    },

    # ─── JOURNAL ──────────────────────────────────────────────
    "journal": {
        "eyebrow":  "Il quaderno di bottega",
        "headline": "Note di lavoro, <em>scritte a penna.</em>",
        "intro":
            "Una pagina al mese, scritta da Anna nei pomeriggi tranquilli. Si parla di chi è "
            "venuto a trovarci, di un materiale nuovo arrivato, di un pezzo che ha richiesto "
            "il doppio del tempo. Non è un blog: è il diario della bottega.",

        "list_label":  "Note recenti",
        "entries": [
            {
                "n":      "47",
                "title":  "Un autunno di tinte naturali",
                "place":  "Bottega · 12 marzo 2026",
                "excerpt":
                    "Severino è tornato dalla concia con sei pelli tinte solo con corteccia di "
                    "castagno. Sul giubbotto Terra è già la tinta del prossimo lotto.",
                "minutes":"3 minuti di lettura",
            },
            {
                "n":      "46",
                "title":  "Caterina e il forno che canta",
                "place":  "Montelupo · 22 febbraio 2026",
                "excerpt":
                    "Caterina ha rifatto il forno a legna nella sua bottega. La prima cottura è "
                    "stata di sei pezzi e tutti hanno cantato al raffreddamento. È buon segno.",
                "minutes":"4 minuti di lettura",
            },
            {
                "n":      "45",
                "title":  "Il telaio di Bruno torna a battere",
                "place":  "Prato · 31 gennaio 2026",
                "excerpt":
                    "Per due mesi era fermo per la sostituzione del pettine. Bruno ha ripreso a "
                    "tessere lunedì. La prima pezza è una tovaglia in lino color sabbia.",
                "minutes":"5 minuti di lettura",
            },
            {
                "n":      "44",
                "title":  "Adele al mercato di Greve",
                "place":  "Chianti · 14 dicembre 2025",
                "excerpt":
                    "Adele è andata al mercato di dicembre per prendere i fichi tardivi. Le "
                    "marmellate di gennaio sono tutte di questa raccolta.",
                "minutes":"3 minuti di lettura",
            },
            {
                "n":      "43",
                "title":  "Una giornata in conceria",
                "place":  "Santa Croce · 8 novembre 2025",
                "excerpt":
                    "Anna ha passato una giornata da Severino. Si vede come una pelle entra in "
                    "vasca, si gira ogni quattro giorni, e dopo quaranta esce diversa.",
                "minutes":"6 minuti di lettura",
            },
            {
                "n":      "42",
                "title":  "Conserve, libri e nuove mani",
                "place":  "Firenze · 19 ottobre 2025",
                "excerpt":
                    "Da ottobre due nuovi artigiani lavorano per la bottega: un legatore di libri "
                    "di Pistoia e una papiniera di San Frediano. Edizioni in arrivo a primavera.",
                "minutes":"4 minuti di lettura",
            },
        ],

        "footer_note_label": "Quaderno",
        "footer_note":
            "Le pagine vecchie restano, non le aggiorniamo. Se ti piace ricevere il quaderno "
            "in posta, scrivici una mail — te lo mandiamo in stampa due volte l'anno.",
    },

    # ─── CONTATTI (form) ──────────────────────────────────────
    "contatti": {
        "eyebrow":  "Vienici a trovare",
        "headline": "Scrivi, telefona, <em>oppure passa.</em>",
        "intro":
            "La bottega è in via dei Serragli, a quattro passi da Pitti. Aperti dal martedì al "
            "sabato, dieci alle diciannove e mezza. Se vuoi sapere se un pezzo è ancora in "
            "vetrina, scrivici su WhatsApp — ti rispondiamo nel giro di un'ora.",

        # Two-column layout: left form, right contact card
        "form_section_label": "Mandaci due righe",
        "form_section_intro":
            "Bastano nome, contatto, e cosa stai cercando. Ti risponde Anna entro la giornata "
            "lavorativa successiva. Per chiedere un pezzo su misura, scrivilo qui sotto: "
            "ti rimandiamo un disegno con tempi e prezzi entro tre giorni.",

        # Form helper
        "form_helper_required":  "Campi con asterisco obbligatori",
        "form_submit_button":    "Invia la richiesta",
        "form_submit_note":      "Niente newsletter. Usiamo le tue righe solo per risponderti.",

        "form_fields": [
            {"name": "nome",          "label": "Nome e cognome",        "type": "text",     "placeholder": "Es. Maria Rossi", "required": True},
            {"name": "email",         "label": "Email",                 "type": "email",    "placeholder": "maria@esempio.it", "required": True},
            {"name": "telefono",      "label": "Telefono o WhatsApp",   "type": "tel",      "placeholder": "Facoltativo · +39 …", "required": False},
            {"name": "interesse",     "label": "Cosa ti interessa",     "type": "select",   "required": True,
             "options": ["Un pezzo del catalogo", "Una commissione su misura", "Una visita in bottega", "Una collaborazione", "Stampa & media"]},
            {"name": "pezzo",         "label": "Pezzo o numero (opz.)", "type": "text",     "placeholder": "Es. N° 042 · Giubbotto Terra", "required": False},
            {"name": "messaggio",     "label": "La tua richiesta",      "type": "textarea", "placeholder": "Raccontaci cosa stai cercando, anche due righe vanno bene.", "required": True, "rows": 5},
        ],

        # Right-side card
        "card_label":   "Bottega di Martino",
        "card_address_label":  "Indirizzo",
        "card_address_value":  "Via dei Serragli 47/r · 50124 Firenze",
        "card_phone_label":    "Telefono",
        "card_phone_value":    "+39 055 234 11 90",
        "card_whatsapp_label": "WhatsApp",
        "card_whatsapp_value": "055 234 11 90",
        "card_email_label":    "Email",
        "card_email_value":    "bottega@bottegadimartino.it",
        "card_hours_label":    "Orari di apertura",
        "card_hours_rows": [
            "Martedì – sabato · 10:00 – 19:30",
            "Domenica · solo su appuntamento",
            "Lunedì · chiuso",
        ],
        "card_directions_label": "Come arrivare",
        "card_directions_text":
            "Tre minuti a piedi da Palazzo Pitti. Bus 11 fermata Serragli. "
            "Dalla stazione SMN: quindici minuti a piedi attraverso il centro.",

        # FAQ accordion
        "faq_label":   "Domande frequenti",
        "faq_items": [
            {
                "q": "Spedite all'estero?",
                "a": "Sì, in tutta Europa entro quattro giorni lavorativi. Per Stati Uniti e "
                     "Giappone scrivici prima — confermiamo i tempi caso per caso.",
            },
            {
                "q": "Posso vedere un pezzo prima di comprarlo?",
                "a": "Certamente. Tienilo da parte chiamando in bottega, e quando passi te lo "
                     "facciamo vedere senza impegno. Se non ti convince, niente pressione.",
            },
            {
                "q": "Fate commissioni su misura?",
                "a": "Sì, su cuoio, ceramica e tessuto. Tempi: da tre a otto settimane secondo "
                     "il pezzo. Acconto del trenta per cento alla conferma del disegno.",
            },
            {
                "q": "Cosa succede se il pezzo si rompe?",
                "a": "Per due anni lo riportiamo a posto in bottega senza spese. Per riparazioni "
                     "successive, applichiamo un costo simbolico — di solito sotto i trenta euro.",
            },
        ],
    },
}
