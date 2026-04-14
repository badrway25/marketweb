"""Bottega — Artisan Shop (artisan-workshop archetype) — EN content tree.

Phase 2g3.5 — eCommerce live rollout (Session 41, 2026-04-14).

Voice contract (EN):
- Aesop / Toast / Etsy editorial English — warm, soulful, hand-written,
  never glossy, never machine-translated.
- Informal second-person "you" throughout — the workshop speaks like a
  friendly maker, never marketing-speak.
- Concrete details kept literal: Italian città (Santa Croce sull'Arno,
  Montelupo Fiorentino, Prato, Greve in Chianti, Firenze) are not
  translated. Artisan names (Severino Falchi, Caterina Lippi, Bruno
  Ricci, Adele Pignatelli, Martino Boncompagni, Anna Boncompagni) stay
  verbatim. Edition numbers (N° 042, 3/8) and prices (€ 420) stay literal.
- Material vocabulary: vegetable-tanned leather, hand-thrown ceramics,
  loom-woven linen, small-batch, edition, signed by the maker.
- Conversation feel: "we", "the workshop", "the bottega" — never
  "our company".

Differentiation contract vs Luxe (D-054 enforcement):
- Bottega is photographically tactile (hands at work, raw leather,
  ceramic on the wheel, looms, market produce). Luxe is photographically
  editorial (campaign portraits, runway, atelier interiors). Imagery
  pools must NOT overlap.
- Bottega CTA pattern: phone-and-whatsapp (warm, immediate, by-name).
  Luxe CTA pattern: private-request (formal, by-appointment).
- Bottega vocabulary: workshop · maker · one-of-a-kind · edition ·
  vegetable-tanned leather · hand-thrown · loom-woven · signed. Luxe
  vocabulary: maison · collection · lookbook · couture · campaign ·
  capsule · drop · private viewing.
"""
from __future__ import annotations

from typing import Any


BOTTEGA_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Workshop",  "kind": "home"},
        {"slug": "shop",     "label": "Catalogue", "kind": "shop"},
        {"slug": "product",  "label": "Piece",     "kind": "product"},
        {"slug": "atelier",  "label": "Atelier",   "kind": "about"},
        {"slug": "journal",  "label": "Notebook",  "kind": "journal"},
        {"slug": "contatti", "label": "Contact",   "kind": "contact"},
    ],

    # Site-wide chrome (consumed by _base.html nav + footer).
    "site": {
        "logo_initial": "M",
        "logo_word":    "La Bottega di Martino",
        "tag":          "Firenze · since 1968 · made by hand",
        "phone":        "+39 055 234 11 90",
        "whatsapp":     "055 234 11 90",
        "whatsapp_link": "https://wa.me/390552341190",
        "email":        "bottega@bottegadimartino.it",
        "address":      "Via dei Serragli 47/r · 50124 Firenze",
        "hours_compact": "Tue – Sat · 10:00 – 19:30",
        "hours_footer_rows": [
            "Sunday · by appointment only",
            "Monday · closed",
        ],
        "license":      "VAT 04891240484 · CCIAA Firenze REA 502118",
        "footer_intro":
            "An artisan workshop founded in 1968 by Martino Boncompagni. "
            "Leather, ceramics and textiles made by hand in Toscana, in small editions "
            "that never repeat. Shipped in 48 hours across Italy, two days longer "
            "across Europe.",
        # Nav CTA — primary action button next to nav links
        "nav_cta":      "Visit the workshop",
        "nav_cta_kind": "appointment",  # links to /contatti/

        # Marketplace footer chrome labels
        "foot_studio":   "The workshop",
        "foot_pages":    "Site map",
        "foot_contact":  "Workshop & orders",
        "foot_stockists":"Selected stockists",
        "stockists_rows": [
            "10 Corso Como · Milano",
            "Eataly Lingotto · Torino",
            "Spazio B**K · Milano",
            "Atelier Pitti · Firenze",
        ],

        # Cross-page meta-strip labels (D-047 lifts on shop/product/atelier)
        "currency_symbol":  "€",
        "shop_filter_label": "Filters",
        "shop_count_unit":   "pieces",
        "edition_label":     "Edition",
        "made_in_label":     "Made in",
        "artisan_label":     "Signed by",
        "material_label":    "Material",
        "shipping_label":    "Shipping",
        "shipping_value":    "48 hours in Italy · 4 days across Europe",
        "guarantee_label":   "Guarantee",
        "guarantee_value":   "Free repairs for two years",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Autumn catalogue · edition 47",
        "headline": "One-of-a-kind pieces stitched, thrown and woven <em>in the workshop.</em>",
        "intro":
            "Vegetable-tanned leather from Santa Croce sull'Arno, ceramics thrown in Montelupo "
            "Fiorentino, linen loom-woven in Prato. Every piece carries the signature of the maker "
            "who made it — and a running number that never repeats.",
        "primary_cta":   "Visit the workshop",
        "primary_href":  "contatti",
        "secondary_cta": "Browse the catalogue",
        "secondary_href":"shop",

        # Stamp-aside data — the rubber-stamped right column of the hero
        "stamp_label":  "Our rule",
        "stamp_heading":"Three hands, <em>one object.</em>",
        "stamp_rows": [
            ("Makers",      "12 workshops"),
            ("Materials",   "100% Italian"),
            ("Edition",     "Never over 50"),
            ("Shipping",    "Within 48 hours"),
        ],
        "stamp_footer": "Handwritten · wrapped in the workshop",
        "stamp_corner_index": "01",
        "stamp_corner_word":  "THE WORKSHOP",

        # Latest-arrived band — 4 product cards
        "latest_label":   "Just arrived",
        "latest_heading": "Fresh off <em>the workbench.</em>",
        "latest_link_label": "The whole catalogue",
        "latest_link_href":  "shop",
        "latest_items": [
            {
                "id":       "giubbotto-terra",
                "n":        "N° 042",
                "edition":  "3 / 8",
                "name":     "Terra Jacket",
                "meta":     "Vegetable-tanned leather · Santa Croce",
                "price":    "€ 420",
                "tag":      "One of a kind",
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "camicia-lino",
                "n":        "N° 108",
                "edition":  "1 / 6",
                "name":     "Linen Shirt",
                "meta":     "Raw linen · Prato",
                "price":    "€ 95",
                "tag":      "Made by hand",
                "image":    "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "ceramica-cucina",
                "n":        "N° 213",
                "edition":  "7 / 24",
                "name":     "Kitchen Set",
                "meta":     "Glazed ceramic · Montelupo",
                "price":    "€ 148",
                "tag":      "Edition",
                "image":    "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "conserve-chianti",
                "n":        "N° 317",
                "edition":  "12 / 60",
                "name":     "Market Preserves",
                "meta":     "Cherry tomatoes · Chianti",
                "price":    "€ 18",
                "tag":      "Seasonal",
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Makers band — 4 artisans with portrait
        "makers_label":   "The hands that sign",
        "makers_heading": "Twelve workshops, <em>one single name.</em>",
        "makers_intro":
            "We work only with makers we know by name. "
            "Every piece that leaves under our name carries theirs too — "
            "because whoever made it has the right to put their face on it.",
        "makers": [
            {
                "name":   "Severino Falchi",
                "craft":  "Master tanner",
                "place":  "Santa Croce sull'Arno",
                "since":  "In the workshop since 1989",
                "quote":  "\u201cYou know good leather by its smell. If it smells of chemicals, we didn't tan it.\u201d",
                "portrait": "https://images.unsplash.com/photo-1581094271901-8022df4466f9?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Caterina Lippi",
                "craft":  "Ceramic thrower",
                "place":  "Montelupo Fiorentino",
                "since":  "Workshop opened in 2003",
                "quote":  "\u201cEvery piece goes back into the kiln three times. If it doesn't sing on the third, I break it.\u201d",
                "portrait": "https://images.unsplash.com/photo-1604881991720-f91add269bed?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Bruno Ricci",
                "craft":  "Linen weaver",
                "place":  "Prato · Via del Telaio",
                "since":  "Hand loom since 1976",
                "quote":  "\u201cRaw linen is a plant. Treat it like bread: with patience and with hunger.\u201d",
                "portrait": "https://images.unsplash.com/photo-1521119989659-a83eee488004?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Adele Pignatelli",
                "craft":  "Chianti preserve-maker",
                "place":  "Greve in Chianti",
                "since":  "Three generations of jars",
                "quote":  "\u201cJam is made when the fruit decides. Not when the calendar does.\u201d",
                "portrait": "https://images.unsplash.com/photo-1607743386760-88ac62b89b8a?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Provenance trio — 3 cards on materials & places
        "provenance_label":   "Provenance",
        "provenance_heading": "Three lands, <em>three materials.</em>",
        "provenance_intro":
            "Nothing travels further than two hundred kilometres. Raw material is the maker's "
            "first signature: if they can tell you where they got it, they're telling you how they worked it.",
        "provenance_items": [
            {
                "icon":  "01",
                "title": "Valdarno leather",
                "desc":  "Vegetable-tanned with chestnut and mimosa bark. "
                         "Forty days in the vat, never chrome, never shortcuts. "
                         "One supplier only: Conceria Falchi, Santa Croce sull'Arno.",
                "place": "Santa Croce sull'Arno · 38 km from Firenze",
            },
            {
                "icon":  "02",
                "title": "Montelupo clay",
                "desc":  "Local red clay, cold-glazed with natural oxides. "
                         "Three firings at 980° in a wood-fired kiln. Thrown free-hand.",
                "place": "Montelupo Fiorentino · 22 km from Firenze",
            },
            {
                "icon":  "03",
                "title": "Prato linen",
                "desc":  "Raw unbleached linen, woven on a 1950s mechanical loom. "
                         "Wide weft, tight warp. Every bolt weighs differently.",
                "place": "Prato · 24 km from Firenze",
            },
        ],

        # Care / guarantee strip
        "care_label":   "Care & guarantee",
        "care_heading": "Repaired in the workshop, <em>forever.</em>",
        "care_items": [
            ("Free repairs for two years",
             "Unstitched handle, chipped glaze, loose embroidery: we fix it ourselves, in the workshop."),
            ("Returns accepted for seven days",
             "If a piece doesn't win you over, we take it back — no fees, no questions."),
            ("Shipped within 48 hours",
             "We ship from Firenze the day after your order, in heavy paper and twine."),
            ("Safe payment",
             "Card or bank transfer. No subscriptions, no accounts, no advertising cookies."),
        ],

        # Press / stockists strip
        "press_label":   "Written about us",
        "press_items":   ["Vogue Italia", "Domus", "La Repubblica", "Apartamento", "Cereal Magazine"],

        "journal_teaser_label":   "From the notebook",
        "journal_teaser_heading": "Work notes, <em>written by hand.</em>",
        "journal_teaser_link":    "Open the notebook",
        "journal_teaser_href":    "journal",

        # Final CTA band
        "cta_label":   "Visit the workshop",
        "cta_heading": "Come see us in Firenze, <em>we'll make you a coffee.</em>",
        "cta_intro":
            "The workshop is on Via dei Serragli, a few steps from Pitti. Open Tuesday to "
            "Saturday, ten to half past seven. We'll show you how leather is tanned, "
            "how a plate is thrown and — if you'd like — introduce you to the makers in person.",
        "cta_primary":   "Book a visit",
        "cta_primary_href": "contatti",
        "cta_secondary": "Write on WhatsApp",
        # cta_secondary_href is rendered as site.whatsapp_link
    },

    # ─── SHOP ─────────────────────────────────────────────────
    "shop": {
        "eyebrow":  "Catalogue · 47th edition",
        "headline": "The whole <em>workbench,</em> open.",
        "intro":
            "Forty-seven one-of-a-kind pieces, twelve makers, three lands. "
            "Every number runs on from 1968 and never repeats. Filter by "
            "material, by maker, or by availability.",

        "filter_section_label": "Filter by",
        "filter_groups": [
            {
                "label": "Material",
                "options": ["Leather", "Ceramic", "Linen & textiles", "Preserves", "Paper & binding"],
            },
            {
                "label": "Maker",
                "options": ["Severino Falchi", "Caterina Lippi", "Bruno Ricci", "Adele Pignatelli", "All"],
            },
            {
                "label": "Availability",
                "options": ["In the workshop", "By request", "Edition sold out"],
            },
        ],

        "sort_label": "Sort by",
        "sort_options": ["Latest arrivals", "Running number", "Price low to high", "Price high to low"],

        "result_count":    "47 pieces currently in the catalogue",
        "result_subtitle": "Updated Monday morning, before the workshop opens",

        "products": [
            {
                "id":       "giubbotto-terra",
                "n":        "N° 042",
                "edition":  "3 / 8",
                "name":     "Terra Jacket",
                "meta":     "Vegetable-tanned leather · hand-dyed",
                "place":    "Santa Croce sull'Arno",
                "artisan":  "Severino Falchi",
                "price":    "€ 420",
                "tag":      "One of a kind",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "borsa-cartolina",
                "n":        "N° 056",
                "edition":  "2 / 12",
                "name":     "Cartolina Bag",
                "meta":     "Natural leather + saddle stitch",
                "place":    "Santa Croce sull'Arno",
                "artisan":  "Severino Falchi",
                "price":    "€ 280",
                "tag":      "One of a kind",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "camicia-lino",
                "n":        "N° 108",
                "edition":  "1 / 6",
                "name":     "Linen Shirt",
                "meta":     "Raw unbleached linen",
                "place":    "Prato",
                "artisan":  "Bruno Ricci",
                "price":    "€ 95",
                "tag":      "Made by hand",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tovaglia-armaiolo",
                "n":        "N° 134",
                "edition":  "5 / 30",
                "name":     "Armaiolo Tablecloth",
                "meta":     "Linen & cotton · wide weft",
                "place":    "Prato",
                "artisan":  "Bruno Ricci",
                "price":    "€ 165",
                "tag":      "Edition",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "ceramica-cucina",
                "n":        "N° 213",
                "edition":  "7 / 24",
                "name":     "Kitchen Set",
                "meta":     "Cold-glazed ceramic",
                "place":    "Montelupo Fiorentino",
                "artisan":  "Caterina Lippi",
                "price":    "€ 148",
                "tag":      "Edition",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tazze-tornite",
                "n":        "N° 219",
                "edition":  "11 / 24",
                "name":     "Thrown Cups",
                "meta":     "Local red clay · wood-fired",
                "place":    "Montelupo Fiorentino",
                "artisan":  "Caterina Lippi",
                "price":    "€ 78",
                "tag":      "Edition",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1610701596007-11502861dcfa?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "vassoio-noce",
                "n":        "N° 251",
                "edition":  "Sold out",
                "name":     "Walnut Tray",
                "meta":     "Solid walnut · oil finish",
                "place":    "Pratovecchio",
                "artisan":  "Severino Falchi",
                "price":    "€ 210",
                "tag":      "Waiting list",
                "available": False,
                "image":    "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "conserve-chianti",
                "n":        "N° 317",
                "edition":  "12 / 60",
                "name":     "Market Preserves",
                "meta":     "Ox-heart cherry tomatoes + EVO oil",
                "place":    "Greve in Chianti",
                "artisan":  "Adele Pignatelli",
                "price":    "€ 18",
                "tag":      "Seasonal",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "marmellata-fichi",
                "n":        "N° 322",
                "edition":  "21 / 80",
                "name":     "Fig Preserve",
                "meta":     "Black September figs · slow-cooked",
                "place":    "Greve in Chianti",
                "artisan":  "Adele Pignatelli",
                "price":    "€ 14",
                "tag":      "Seasonal",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Featured product detail link — used by smoke and "see more"
        "featured_product_id": "giubbotto-terra",

        "footer_note_label": "Workshop",
        "footer_note":
            "No algorithms, no recommendations: the catalogue is laid out the way it is on the "
            "shelves of the workshop. If you're looking for a specific piece, write to us on "
            "WhatsApp — we reply ourselves, one person at a time.",
    },

    # ─── PRODUCT (detail) ─────────────────────────────────────
    "product": {
        # Hero (uses featured_product_id from shop)
        "id":       "giubbotto-terra",
        "n":        "N° 042",
        "edition":  "3 / 8",
        "edition_note": "Edition of eight pieces · three remaining",
        "name":     "Terra Jacket",
        "subtitle": "Vegetable-tanned leather · saddle-stitched · hand-dyed",
        "price":    "€ 420",
        "vat_note": "VAT included · 48-hour shipping in Italy",
        "intro":
            "A short jacket in Valdarno leather, vegetable-tanned for forty days with chestnut "
            "and mimosa bark. The dye is brushed on by hand with a linen cloth soaked in natural "
            "Siena earth pigment: every piece takes the colour a little differently and no two "
            "are ever alike.",

        "gallery": [
            "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=1200&q=80&auto=format&fit=crop",
        ],

        # Right-side info aside (the rubber-stamped data block)
        "info_label":  "Specifications",
        "info_rows": [
            ("Material",    "Valdarno leather · vegetable-tanned"),
            ("Thickness",   "1.8 mm uniform"),
            ("Dye",         "Siena earth · natural pigment"),
            ("Stitching",   "Saddle stitch, waxed thread"),
            ("Lining",      "Raw unbleached linen"),
            ("Buttons",     "Ox horn · sourced in Toscana"),
            ("Weight",      "780 g (size M)"),
            ("Make time",   "11 days in the workshop"),
        ],

        # Sizing card
        "size_label":    "Sizes available",
        "size_intro":    "Made to measure within three weeks. Write to us on WhatsApp.",
        "size_options":  ["S", "M", "L", "XL", "Made to measure"],
        "size_chart_link": "Read the sizing guide",
        "size_chart_href": "atelier",

        # Made by
        "artisan_label": "Signed by",
        "artisan_name":  "Severino Falchi",
        "artisan_role":  "Master tanner · in the workshop since 1989",
        "artisan_bio":
            "Severino has tanned leather in his own vat since 1989. He works with two sons and "
            "a nephew, and dyes every hide by hand. His motto at the tannery is 'slow is better'.",
        "artisan_portrait":
            "https://images.unsplash.com/photo-1581094271901-8022df4466f9?w=400&q=80&auto=format&fit=crop",

        # Buy band
        "buy_primary":   "Add to basket",
        "buy_secondary": "Write on WhatsApp",
        "buy_note":
            "Card, bank transfer, or pay on collection if you pick it up at the workshop. "
            "We ship within 48 hours, in heavy paper and twine.",

        # Care
        "care_label":   "Care for the piece",
        "care_intro":
            "Vegetable-tanned leather asks for little and lasts a lifetime. We've already "
            "treated it at the tannery with raw linseed oil. In the first months it will shift "
            "colour slightly, lightening along the folds — that's normal and intended.",
        "care_items": [
            ("Cleaning",      "Dry cloth. Never detergent, never alcohol."),
            ("Conditioning",  "Linseed oil or a neutral cream once a year."),
            ("Repair",        "For two years we do it free of charge in the workshop."),
            ("Rain",          "Dry away from heat sources. No hair dryer."),
        ],

        # Provenance map
        "provenance_label":   "Provenance",
        "provenance_heading": "Three stops, <em>forty kilometres.</em>",
        "provenance_steps": [
            ("01", "Tannery",   "Conceria Falchi · Santa Croce sull'Arno · 38 km"),
            ("02", "Dyeing",    "Bottega di Martino · Firenze · 0 km"),
            ("03", "Stitching", "Bottega di Martino · Firenze · 0 km"),
            ("04", "Wrapping",  "Bakery paper from Greve in Chianti · 32 km"),
        ],

        # Related products band
        "related_label":   "From the same hand",
        "related_intro":   "Pieces born in the same workshop, under the same signature.",
        "related_items": [
            {
                "id":      "borsa-cartolina",
                "n":       "N° 056",
                "name":    "Cartolina Bag",
                "meta":    "Natural leather · Severino Falchi",
                "price":   "€ 280",
                "image":   "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":      "vassoio-noce",
                "n":       "N° 251",
                "name":    "Walnut Tray",
                "meta":    "Solid walnut · Severino Falchi",
                "price":   "€ 210",
                "image":   "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":      "ceramica-cucina",
                "n":       "N° 213",
                "name":    "Kitchen Set",
                "meta":    "Glazed ceramic · Caterina Lippi",
                "price":   "€ 148",
                "image":   "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
        ],
    },

    # ─── ATELIER (about) ──────────────────────────────────────
    "atelier": {
        "eyebrow":  "The atelier on Via dei Serragli",
        "headline": "A workshop <em>of workshops.</em>",
        "intro":
            "Opened in 1968 by Martino Boncompagni, today it's a hundred-and-ten square-metre "
            "space on Via dei Serragli, where twelve Tuscan makers bring their pieces three times "
            "a week. No central warehouse, no chain — everything you see in the window is made "
            "less than two hundred kilometres from here.",

        # Mission stamp panel
        "mission_label":   "The rule of the workshop",
        "mission_heading": "Three hands, one object. <em>Always.</em>",
        "mission_text":
            "Every piece passes through three hands: the one that works the raw material, the one "
            "that finishes it, the one that makes sure the running number is written in pen before "
            "shipping. No machine replaces the last signature. If we can't get a piece through "
            "three hands, we don't make it.",

        # Process timeline — 5 steps
        "process_label":   "The journey",
        "process_heading": "From raw material <em>to twine.</em>",
        "process_steps": [
            {
                "n":    "01",
                "title":"We go and collect the material",
                "place":"Valdarno · Mugello · Chianti",
                "desc": "Leather from the Valdarno tanneries, red clay from Montelupo, "
                        "linen from the Prato looms. We go in person, never by courier.",
                "duration": "One week a month",
            },
            {
                "n":    "02",
                "title":"We let it rest",
                "place":"Workshop · back room",
                "desc": "The leather sits in the vat for forty days. The clay dries slowly "
                        "in the air. The linen waits for the weather to change. No shortcuts.",
                "duration": "Two weeks to three months",
            },
            {
                "n":    "03",
                "title":"We work it by hand",
                "place":"Workbench · garden window",
                "desc": "The piece takes shape under the hands of the lead maker. "
                        "Saddle stitching, free-hand throwing, 1950s mechanical loom.",
                "duration": "Four to twelve days",
            },
            {
                "n":    "04",
                "title":"We finish it",
                "place":"Workshop · Anna's bench",
                "desc": "Anna checks it, sands it, dyes it. Adds the running number. "
                        "If it doesn't pass her inspection, back it goes to the main bench.",
                "duration": "Half a day per piece",
            },
            {
                "n":    "05",
                "title":"We wrap it up",
                "place":"Workshop · packing bench",
                "desc": "Bakery paper from Greve, hemp twine, a handwritten card with the name "
                        "of who made the piece. We ship from Firenze within 48 hours.",
                "duration": "Same day as shipping",
            },
        ],

        # Founder
        "founder_label":   "Who we are",
        "founder_heading": "Martino, Anna, <em>and twelve workshops.</em>",
        "founder_text":
            "Martino opened up in '68 with a three-metre bench and a bale of leather. Today he "
            "runs the workshop with his niece Anna — he's mostly at the bench, she looks after "
            "whoever walks in, whoever calls, whoever writes. Together they keep in touch with "
            "the twelve makers. Without ever becoming a company.",
        "founder_portrait":
            "https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=600&q=80&auto=format&fit=crop",
        "founder_caption":
            "Martino Boncompagni and Anna Boncompagni · Workshop on Via dei Serragli, Firenze",

        # Numbers stamp
        "numbers_label":   "Workshop numbers",
        "numbers_items": [
            ("57",     "years continuously open"),
            ("12",     "makers who sign for us"),
            ("47th",   "edition of the catalogue"),
            ("0",      "industrial machines"),
        ],

        # Visit card
        "visit_label":   "Come and see us",
        "visit_heading": "Via dei Serragli 47/r, <em>a few steps from Pitti.</em>",
        "visit_text":
            "The workshop is open Tuesday to Saturday, ten to half past seven. Sunday by "
            "appointment only. If you come on a Thursday afternoon, there's usually a maker "
            "in to drop off pieces. Coffee and the guest book ready.",
        "visit_primary":   "Book a visit",
        "visit_primary_href": "contatti",
        "visit_secondary": "Write on WhatsApp",
    },

    # ─── JOURNAL ──────────────────────────────────────────────
    "journal": {
        "eyebrow":  "The workshop notebook",
        "headline": "Work notes, <em>written in pen.</em>",
        "intro":
            "One page a month, written by Anna on the quiet afternoons. About who came to see "
            "us, a new material that arrived, a piece that took twice as long. It isn't a blog: "
            "it's the workshop diary.",

        "list_label":  "Recent notes",
        "entries": [
            {
                "n":      "47",
                "title":  "An autumn of natural dyes",
                "place":  "Workshop · 12 March 2026",
                "excerpt":
                    "Severino is back from the tannery with six hides dyed with chestnut bark "
                    "alone. On the Terra Jacket, it's already the colour of the next batch.",
                "minutes":"3 minute read",
            },
            {
                "n":      "46",
                "title":  "Caterina and the kiln that sings",
                "place":  "Montelupo · 22 February 2026",
                "excerpt":
                    "Caterina has rebuilt the wood-fired kiln in her workshop. The first firing "
                    "was six pieces and they all sang as they cooled. A good sign.",
                "minutes":"4 minute read",
            },
            {
                "n":      "45",
                "title":  "Bruno's loom is beating again",
                "place":  "Prato · 31 January 2026",
                "excerpt":
                    "It stood still for two months while the reed was replaced. Bruno started "
                    "weaving again on Monday. The first bolt is a sand-coloured linen tablecloth.",
                "minutes":"5 minute read",
            },
            {
                "n":      "44",
                "title":  "Adele at the Greve market",
                "place":  "Chianti · 14 December 2025",
                "excerpt":
                    "Adele went to the December market for the late figs. January's preserves "
                    "all come from that harvest.",
                "minutes":"3 minute read",
            },
            {
                "n":      "43",
                "title":  "A day at the tannery",
                "place":  "Santa Croce · 8 November 2025",
                "excerpt":
                    "Anna spent a day at Severino's. You can see how a hide goes into the vat, "
                    "gets turned every four days, and after forty comes out transformed.",
                "minutes":"6 minute read",
            },
            {
                "n":      "42",
                "title":  "Preserves, books and new hands",
                "place":  "Firenze · 19 October 2025",
                "excerpt":
                    "From October two new makers are working for the workshop: a book-binder "
                    "in Pistoia and a paper-maker in San Frediano. Editions arriving in spring.",
                "minutes":"4 minute read",
            },
        ],

        "footer_note_label": "Notebook",
        "footer_note":
            "Old pages stay up, we don't rewrite them. If you like to receive the notebook in "
            "the post, write us an email — we send it out in print twice a year.",
    },

    # ─── CONTATTI (form) ──────────────────────────────────────
    "contatti": {
        "eyebrow":  "Come and see us",
        "headline": "Write, call, <em>or drop in.</em>",
        "intro":
            "The workshop is on Via dei Serragli, a few steps from Pitti. Open Tuesday to "
            "Saturday, ten to half past seven. If you want to know whether a piece is still "
            "in the window, write to us on WhatsApp — we reply within the hour.",

        # Two-column layout: left form, right contact card
        "form_section_label": "Send us a line",
        "form_section_intro":
            "A name, a way to reach you, and what you're looking for — that's enough. Anna "
            "replies within the next working day. For a piece made to measure, write it below: "
            "we'll send you a drawing with times and prices within three days.",

        # Form helper
        "form_helper_required":  "Fields with an asterisk are required",
        "form_submit_button":    "Send your request",
        "form_submit_note":      "No newsletter. We use your lines only to reply.",

        "form_fields": [
            {"name": "nome",          "label": "First and last name",   "type": "text",     "placeholder": "e.g. Mary Russell", "required": True},
            {"name": "email",         "label": "Email",                 "type": "email",    "placeholder": "mary@example.com", "required": True},
            {"name": "telefono",      "label": "Phone or WhatsApp",     "type": "tel",      "placeholder": "Optional · +39 …", "required": False},
            {"name": "interesse",     "label": "What you're after",     "type": "select",   "required": True,
             "options": ["A piece from the catalogue", "A made-to-measure commission", "A workshop visit", "A collaboration", "Press & media"]},
            {"name": "pezzo",         "label": "Piece or number (opt.)","type": "text",     "placeholder": "e.g. N° 042 · Terra Jacket", "required": False},
            {"name": "messaggio",     "label": "Your request",          "type": "textarea", "placeholder": "Tell us what you're looking for — a couple of lines is plenty.", "required": True, "rows": 5},
        ],

        # Right-side card
        "card_label":   "Bottega di Martino",
        "card_address_label":  "Address",
        "card_address_value":  "Via dei Serragli 47/r · 50124 Firenze",
        "card_phone_label":    "Phone",
        "card_phone_value":    "+39 055 234 11 90",
        "card_whatsapp_label": "WhatsApp",
        "card_whatsapp_value": "055 234 11 90",
        "card_email_label":    "Email",
        "card_email_value":    "bottega@bottegadimartino.it",
        "card_hours_label":    "Opening hours",
        "card_hours_rows": [
            "Tuesday – Saturday · 10:00 – 19:30",
            "Sunday · by appointment only",
            "Monday · closed",
        ],
        "card_directions_label": "How to get here",
        "card_directions_text":
            "A three-minute walk from Palazzo Pitti. Bus 11, Serragli stop. "
            "From SMN station: fifteen minutes on foot through the centre.",

        # FAQ accordion
        "faq_label":   "Frequently asked questions",
        "faq_items": [
            {
                "q": "Do you ship abroad?",
                "a": "Yes, all over Europe within four working days. For the United States and "
                     "Japan write first — we confirm timing case by case.",
            },
            {
                "q": "Can I see a piece before buying it?",
                "a": "Of course. Put it aside by calling the workshop, and when you come by "
                     "we'll show it to you, no pressure. If it doesn't win you over, no pressure either.",
            },
            {
                "q": "Do you take made-to-measure commissions?",
                "a": "Yes, in leather, ceramic and textile. Timing: three to eight weeks depending "
                     "on the piece. A thirty per cent deposit when the drawing is confirmed.",
            },
            {
                "q": "What happens if a piece breaks?",
                "a": "For two years we put it right in the workshop at no cost. For later repairs "
                     "we ask a token fee — usually under thirty euro.",
            },
        ],
    },
}
