"""Luxe — Fashion Store (fashion-editorial archetype) — EN content tree.

Phase 2g3.5 — eCommerce live rollout (Session 41, 2026-04-14).

Voice contract (EN):
- Editorial fashion-press English — The Gentlewoman / Net-a-Porter /
  Vogue register. Formal, italic-thinking, reserved. Direct address
  but never informal ("you" carries the weight of the second person
  plural — never breezy). No contractions in formal copy; no marketing
  exclamations.
- Vocabulary: maison, atelier, private viewing, drop, capsule,
  lookbook, waitlist, by appointment, RSVP, house concierge.
- Italian proper names stay literal: Maison Luxe, Milano, Tokyo,
  Giulia Maison, Carla Sozzani, Letizia Carrera, Sebastiano Pellion
  di Persano, Sentier, Brera, Aoyama, Setificio Tessitura Como,
  Maglificio Lanifer Biella, Conceria della Madonna, Grand Hôtel
  Villa d'Este. Product names kept in Italian for editorial mystique
  (Rack Atelier, Bomber Siena, Borsa Isola). Paris (EN form), Tokyo,
  Milano retained.
- Magazine titles verbatim: Vogue Italia, The Gentlewoman, AnOther
  Magazine, Le Monde D'Hermès, Wallpaper*, Hermès, Bottega Veneta,
  Goyard, Lesage, Loewe, Central Saint Martins, IMG Models, Art +
  Commerce, Studio Riffraff Milano.
- Currency: "€2,480" (no space, comma thousand-sep, period decimal —
  fashion-press EN standard).
- HTML <em> tags preserved with EN editorial rhythm.

Differentiation contract vs Bottega EN (D-054 enforcement):
- Luxe EN is formal editorial maison (reserved, italic, by-appointment).
  Bottega EN is informal-warm Aesop register (hand-thrown, workshop,
  the makers, WhatsApp). Vocabularies must not overlap.
- Luxe EN says: "atelier", "maison", "private viewing", "drop",
  "capsule", "waitlist", "by appointment", "house concierge".
- Luxe EN must NOT say: "workshop", "hand-thrown", "edition",
  "small-batch", "WhatsApp", "the makers".
"""
from __future__ import annotations

from typing import Any


LUXE_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Maison",     "kind": "home"},
        {"slug": "collezione", "label": "Collection", "kind": "collection"},
        {"slug": "product",    "label": "Look",       "kind": "product"},
        {"slug": "maison",     "label": "Atelier",    "kind": "about"},
        {"slug": "lookbook",   "label": "Lookbook",   "kind": "lookbook"},
        {"slug": "contatti",   "label": "Private",    "kind": "contact"},
    ],

    # Site-wide chrome (consumed by _base.html nav + footer).
    "site": {
        "logo_initial": "L",
        "logo_word":    "Maison Luxe",
        "logo_subline": "Milano · Paris · Tokyo",
        "tag":          "Atelier · Spring–Summer 2026",
        "phone":        "+39 02 7600 1492",
        "private_phone_label": "House concierge",
        "email":        "private@maisonluxe.com",
        "private_email_label": "Private clients",
        "address":      "Via Senato 28 · 20121 Milano",
        "showroom_paris": "9 rue du Mail · 75002 Paris",
        "showroom_tokyo": "1-1-7 Aoyama · Minato-ku · Tokyo",
        "hours_compact": "Tue – Sat · 11:00 – 19:00 · by appointment",
        "hours_footer_rows": [
            "Sunday · private",
            "Monday · closed",
        ],
        "license":      "Maison Luxe Srl · VAT 11489720152 · CCIAA Milano REA 2589441",
        "footer_intro":
            "Maison founded in Milano in 2014 by Giulia Maison, with an atelier in Paris and a "
            "showroom in Tokyo. Pieces are drawn and sewn between Milano and Paris, in limited "
            "runs, exclusively by waitlist. Seasonal drops of forty-five pieces and nine "
            "silhouettes.",

        # Nav reservation CTA (private viewing)
        "nav_cta":      "Request a viewing",
        "nav_cta_kind": "appointment",  # links to /contatti/

        # Marketplace footer chrome labels
        "foot_studio":   "The maison",
        "foot_pages":    "Map",
        "foot_contact":  "House concierge",
        "foot_offices":  "Ateliers & showroom",
        "office_rows": [
            "Milano · Via Senato 28",
            "Paris · 9 rue du Mail",
            "Tokyo · 1-1-7 Aoyama",
        ],

        # Cross-page meta-strip labels (D-047)
        "currency_symbol":  "€",
        "collection_label": "Collection",
        "drop_label":       "Drop",
        "season_label":     "Season",
        "shipping_label":   "Private delivery",
        "shipping_value":   "Maison courier Milano · 24 hours Italy · 72 hours Europe",
        "viewing_label":    "Private viewing",
        "viewing_value":    "By appointment only · dedicated concierge",
        "waitlist_label":   "Waitlist",
        "rsvp_label":       "RSVP",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "issue":    "Issue 12 · Spring '26",
        "issue_label": "Issue",
        "cover_styling_label": "Styling",
        "cover_styling_name":  "Carla Sozzani",
        "cover_label":         "Cover",
        "cover_subject":       "La Muse en Velours",
        "cover_image":
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1600&q=80&auto=format&fit=crop",

        "eyebrow":  "Lookbook · Spring Summer 2026",
        "headline": "The new body <em>of dress.</em>",
        "headline_credit_line": "Fifty pieces · ninety gestures of tailoring",
        "intro":
            "A single collection, woven between Como and Prato, photographed at the Grand "
            "Hôtel Villa d'Este. Monthly drops, exclusively for those on the waitlist. The "
            "maison never sells the same piece twice.",

        "primary_cta":   "Enter the lookbook",
        "primary_href":  "lookbook",
        "secondary_label":   "Creative direction",
        "secondary_name":    "Giulia Maison",

        # Editorial tile strip — 4 silhouettes pinned below hero
        "edition_label":   "Limited run",
        "edition_subline": "four selected pieces",
        "tiles": [
            {
                "id":       "rack-atelier",
                "tag":      "New",
                "name":     "Rack Atelier",
                "price":    "€2,480",
                "image":    "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "bomber-siena",
                "tag":      "Capsule",
                "name":     "Bomber Siena",
                "price":    "€1,290",
                "image":    "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "pelletteria-isola",
                "tag":      "Atelier",
                "name":     "Borsa Isola",
                "price":    "€860",
                "image":    "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "tag":      "Archive",
                "name":     "Sessione Vogue",
                "price":    "€1,940",
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200&q=80&auto=format&fit=crop",
            },
        ],

        # Manifesto / maison statement
        "manifesto_label":   "Maison statement",
        "manifesto_heading": "Forty-five pieces <em>per season, never one more.</em>",
        "manifesto_text":
            "We draw the collection twice a year, in a one-hundred-and-forty square-metre "
            "atelier between Brera and Sentier. Each piece is cut by hand, sewn to the "
            "client's measure, and signed by the hand that made it. No outlet, no sales, no "
            "resold labels. Only what has left the maison.",

        # Atelier numbers — KPI strip
        "atelier_numbers_label":   "The atelier in numbers",
        "atelier_numbers": [
            ("12",     "years of maison"),
            ("45",     "pieces per season"),
            ("9",      "signature silhouettes"),
            ("3",      "ateliers around the world"),
        ],

        # Lookbook teaser — editorial 3-tile
        "lookbook_teaser_label":   "Lookbook in residence",
        "lookbook_teaser_heading": "Eighteen images, <em>one light alone.</em>",
        "lookbook_teaser_intro":
            "Photographed at the Grand Hôtel Villa d'Este, on the shore of Lake Como, in the "
            "natural light of March. Styling by Carla Sozzani, photography by Letizia Carrera, "
            "art direction by the maison.",
        "lookbook_teaser_link": "Browse the lookbook",
        "lookbook_teaser_href": "lookbook",
        "lookbook_teaser_tiles": [
            {
                "title":   "Look 03 · Double cady",
                "credit":  "Styling · Carla Sozzani",
                "image":   "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "title":   "Look 09 · Carded wool from Biella",
                "credit":  "Photo · Letizia Carrera",
                "image":   "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "title":   "Look 14 · Silk crêpe from Como",
                "credit":  "Atelier · Sentier Paris",
                "image":   "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1000&q=80&auto=format&fit=crop",
            },
        ],

        # Press / editorial mentions strip
        "press_label":   "Editorial",
        "press_intro":   "Featured in",
        "press_items":   ["Vogue Italia", "The Gentlewoman", "AnOther Magazine", "Le Monde D'Hermès", "Wallpaper*"],

        # Seasonal drop card
        "drop_label":    "Next drop",
        "drop_heading":  "SS26 · Capsule 04 — <em>the light of Como.</em>",
        "drop_subhead":  "Waitlist opens · Friday 24 April, 11:00 CET",
        "drop_metadata": [
            ("Pieces",      "9 silhouettes"),
            ("Material",    "Silk crêpe · cady · alpaca"),
            ("Exclusivity", "12 pieces per silhouette"),
            ("Opening",     "Waitlist · Friday 24 April"),
        ],
        "drop_cta":      "Join the waitlist",
        "drop_cta_href": "contatti",

        # Private viewing CTA band
        "private_label":   "Private viewing",
        "private_heading": "Three salons, <em>a room kept empty for you.</em>",
        "private_intro":
            "The maisons in Milano, Paris and Tokyo receive by appointment only. The house "
            "concierge reserves an hour of room time, prepares the pieces suited to your "
            "profile, and arranges the fitting with the seamstress. Service complimentary · "
            "dedicated concierge.",
        "private_primary":     "Request a private viewing",
        "private_primary_href":"contatti",
        "private_secondary":   "See the ateliers",
        "private_secondary_href":"maison",
    },

    # ─── COLLEZIONE (shop list) ───────────────────────────────
    "collezione": {
        "season_chip":  "Spring–Summer 2026",
        "eyebrow":      "Full collection · drop 04 · capsules 01–04",
        "headline":     "Forty-five pieces, <em>nine signature silhouettes.</em>",
        "intro":
            "The complete Spring–Summer 2026 collection, ordered by silhouette. Each piece "
            "is available exclusively by waitlist: from confirmation to delivery, four to "
            "six weeks.",

        "filter_label":  "Filter",
        "filter_groups": [
            {
                "label": "Silhouette",
                "options": ["Fluid tailoring", "Robe-manteau", "Wide trouser", "Editorial knitwear", "Atelier leather"],
            },
            {
                "label": "Material",
                "options": ["Cashmere alpaca", "Double cady", "Silk crêpe from Como", "Carded wool from Biella", "Firenze leather"],
            },
            {
                "label": "Availability",
                "options": ["In showroom", "Waitlist open", "Sold out · by request"],
            },
        ],
        "sort_label":    "Sort",
        "sort_options":  ["By silhouette", "By drop", "Price ascending", "Newest"],

        "result_count":     "45 pieces in the collection",
        "result_subtitle":  "Updated on the first of every month, following the drop",

        "products": [
            {
                "id":       "robe-manteau-grigio-perla",
                "n":        "Look 03",
                "name":     "Robe-manteau Grigio Perla",
                "meta":     "Double cashmere alpaca · Maglificio Lanifer Biella",
                "drop":     "Drop 01 · Spring 26",
                "price":    "€2,840",
                "tag":      "Waitlist",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tailleur-cady-bianco",
                "n":        "Look 07",
                "name":     "Tailleur Cady Bianco",
                "meta":     "Double cady · Setificio Tessitura Como",
                "drop":     "Drop 02 · Spring 26",
                "price":    "€3,420",
                "tag":      "In showroom",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "rack-atelier-nero",
                "n":        "Look 11",
                "name":     "Rack Atelier Nero",
                "meta":     "Nappa leather from Firenze · sellier stitching",
                "drop":     "Drop 02 · Spring 26",
                "price":    "€2,480",
                "tag":      "Waitlist",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "bomber-siena",
                "n":        "Look 14",
                "name":     "Bomber Siena",
                "meta":     "Cady dyed in Siena · embroidery by Atelier Sentier",
                "drop":     "Drop 03 · Summer 26",
                "price":    "€1,290",
                "tag":      "Capsule",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "pantalone-wide-crepe",
                "n":        "Look 16",
                "name":     "Pantalone Wide Crêpe",
                "meta":     "Silk crêpe from Como · sellier belt",
                "drop":     "Drop 03 · Summer 26",
                "price":    "€1,180",
                "tag":      "Waitlist",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "borsa-isola",
                "n":        "Look 18",
                "name":     "Borsa Isola",
                "meta":     "Leather from Atelier Firenze · day pochette",
                "drop":     "Drop 03 · Summer 26",
                "price":    "€860",
                "tag":      "Atelier",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "abito-sera-organza",
                "n":        "Look 22",
                "name":     "Abito Sera Organza",
                "meta":     "Woven organza from Como · embroidery by Lesage",
                "drop":     "Drop 04 · Summer 26",
                "price":    "€4,690",
                "tag":      "Sold out · by request",
                "available":False,
                "image":    "https://images.unsplash.com/photo-1611042553365-9b101441c135?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "maglia-cashmere-corta",
                "n":        "Look 24",
                "name":     "Maglia Cashmere Corta",
                "meta":     "12-ply cashmere · Maglificio Lanifer Biella",
                "drop":     "Drop 04 · Summer 26",
                "price":    "€1,420",
                "tag":      "Waitlist",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "n":        "Look 26",
                "name":     "Sessione Vogue",
                "meta":     "Archive coat · 2024 drop reissue",
                "drop":     "Archive · 2024",
                "price":    "€1,940",
                "tag":      "Archive",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
        ],

        "featured_product_id": "rack-atelier-nero",

        "footer_note_label": "Drop 04 opening",
        "footer_note":
            "Registration for Drop 04 — the Como-light capsule — opens on Friday 24 April at "
            "11:00 CET. Clients already on the waitlist hold absolute priority across every "
            "silhouette. To be added to the list: write to the house concierge.",
    },

    # ─── PRODUCT DETAIL ───────────────────────────────────────
    "product": {
        "id":       "rack-atelier-nero",
        "n":        "Look 11 · Drop 02",
        "name":     "Rack Atelier Nero",
        "subtitle": "Nappa leather from Firenze · sellier stitching · gold trim",
        "price":    "€2,480",
        "vat_note": "VAT included · maison courier delivery · 24 hours Italy",
        "tag":      "Waitlist · Drop 02 SS26",
        "intro":
            "A day-to-evening bag in nappa leather from Firenze, hand-sewn in the Sentier "
            "atelier with a gold sellier stitch on three sides. Edges burnished with beeswax, "
            "base reinforced in Vacchetta leather. Drawn on the body of the creative director, "
            "produced in twelve numbered pieces, signed on the base by the atelier that made it.",

        "gallery": [
            "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1591561954557-26941169b49e?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1611042553365-9b101441c135?w=1400&q=80&auto=format&fit=crop",
        ],

        # Editorial caption strip below gallery
        "gallery_caption_styling":  "Styling · Carla Sozzani",
        "gallery_caption_photo":    "Photo · Letizia Carrera",
        "gallery_caption_location": "Grand Hôtel Villa d'Este · March 2026",

        # Right-side info panel — italic captioned
        "info_label":  "Atelier specifications",
        "info_rows": [
            ("Atelier",      "Sentier · Paris"),
            ("Material",     "Nappa from Firenze · vegetable tanning"),
            ("Stitching",    "Gold sellier on three sides · waxed thread"),
            ("Edges",        "Beeswax · burnished by hand"),
            ("Base",         "Reinforced Vacchetta · brass feet"),
            ("Hardware",     "Brass plated in 24K gold"),
            ("Measurements", "32 × 24 × 12 cm · shoulder strap 105 cm"),
            ("Make",         "21 atelier hours per piece"),
        ],

        # Sizing / variant card (silhouette comes in 2 dimensions + 3 tonalities)
        "size_label":    "Dimension",
        "size_options":  ["Day · 32 × 24", "Evening · 25 × 18"],
        "color_label":   "Tone",
        "color_options": ["Nero notte", "Bordeaux Como", "Avorio crema"],

        # Edition note
        "edition_label": "Run",
        "edition_value": "12 numbered pieces · no. 03/12 available",
        "edition_note":
            "Each piece is cold-stamped inside with its progressive number, the name of the "
            "lead seamster, and the date of delivery from the atelier.",

        # Atelier signature
        "atelier_label":   "Signed by the atelier",
        "atelier_name":    "Atelier Sentier · Paris",
        "atelier_founded": "Opened in 2017",
        "atelier_text":
            "A leatherwork atelier run directly by the maison, on rue du Mail. Six selliers "
            "trained in the houses of Hermès and Goyard, one cutter, one burnisher. They work "
            "exclusively for Maison Luxe — no third parties, no white-label production.",
        "atelier_portrait":
            "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=600&q=80&auto=format&fit=crop",

        # Buy band — private request style
        "buy_primary":   "Request from the maison",
        "buy_primary_href":  "contatti",
        "buy_secondary": "Add to the waitlist",
        "buy_note":
            "Purchase by appointment or direct request to the house concierge. Thirty per "
            "cent deposit on confirmation. Delivery in 4–6 weeks from order, maison courier "
            "Milano, in a signed box.",

        # Care section (italic editorial style)
        "care_label":   "Care of the piece",
        "care_intro":
            "Nappa from Firenze is a living leather: it takes the form of the one who wears "
            "it, softening in the first months without losing structure. Treated in the "
            "atelier with neutral beeswax, it requires no upkeep in the first two years of "
            "daily wear.",
        "care_items": [
            ("Cleaning",     "Soft cloth, lightly damp. Never chemical agents."),
            ("Conditioning", "Maison beeswax every twelve months. Stick provided with the piece."),
            ("Storage",      "Organic cotton pouch, never plastic. Never direct sunlight."),
            ("Rain",         "Natural drying in the shade. Afterwards, a pass of wax."),
        ],

        # Atelier provenance
        "provenance_label":   "Provenance",
        "provenance_heading": "Four stages, <em>four signatures.</em>",
        "provenance_steps": [
            ("01", "Tannery",         "Conceria della Madonna · Firenze · 45-day vegetable tanning"),
            ("02", "Cutting",         "Atelier Sentier · Paris · free-hand cutting"),
            ("03", "Sellier stitch",  "Atelier Sentier · Paris · 21 hours per piece"),
            ("04", "Packaging",       "Maison Milano · signed box and cord"),
        ],

        # Related — three other atelier pieces
        "related_label":   "From the same atelier",
        "related_intro":   "Leatherwork signed Sentier · Paris.",
        "related_items": [
            {
                "id":      "borsa-isola",
                "n":       "Look 18",
                "name":    "Borsa Isola",
                "meta":    "Day pochette · Atelier Sentier",
                "price":   "€860",
                "image":   "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "rack-atelier",
                "n":        "Look 09",
                "name":     "Rack Atelier Crema",
                "meta":     "Day bag · Atelier Sentier",
                "price":    "€2,480",
                "image":    "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "n":        "Look 26",
                "name":     "Cappotto Sessione Vogue",
                "meta":     "Archive coat · 2024 drop",
                "price":    "€1,940",
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
        ],
    },

    # ─── MAISON (about) ───────────────────────────────────────
    "maison": {
        "eyebrow":  "The maison",
        "headline": "Three cities, <em>one signature.</em>",
        "intro":
            "Maison Luxe was founded in Milano in 2014 by Giulia Maison, after eight years "
            "between Hermès and Bottega Veneta. Today it draws two collections a year, in "
            "ateliers between Brera and Sentier, and receives by appointment only in the three "
            "maisons of Milano, Paris and Tokyo. Forty-five pieces per season, never one more.",

        # Maison statement panel
        "statement_label":   "Statement",
        "statement_heading": "Forty-five pieces <em>per season.</em>",
        "statement_text":
            "Quantity is an editorial decision, not a limitation. Each piece must be drawn "
            "by the creative director, cut in the atelier, sewn by a seamstress who signs it, "
            "photographed for the lookbook, and followed personally in delivery. Forty-five "
            "is the highest number that lets us do this well.",

        # Atelier cards — 3 cities
        "ateliers_label":   "The three ateliers",
        "ateliers_heading": "Milano, Paris, <em>Tokyo.</em>",
        "ateliers_intro":
            "Three houses, one maison. Milano draws and directs. Paris sews and embroiders. "
            "Tokyo receives the Asian client in a private salon in Aoyama.",
        "ateliers": [
            {
                "city":   "Milano",
                "place":  "Via Senato 28 · Brera",
                "role":   "Creative atelier · direction · tailoring",
                "since":  "Opened in 2014",
                "head":   "Giulia Maison · creative director",
                "team":   "Six seamstresses · two cutters · one house concierge",
                "image":  "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=900&q=80&auto=format&fit=crop",
            },
            {
                "city":   "Paris",
                "place":  "9 rue du Mail · Sentier",
                "role":   "Leatherwork atelier · sellier stitching",
                "since":  "Opened in 2017",
                "head":   "Jean-Luc Berthier · maître sellier",
                "team":   "Six selliers · one cutter · one burnisher",
                "image":  "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=900&q=80&auto=format&fit=crop",
            },
            {
                "city":   "Tokyo",
                "place":  "1-1-7 Aoyama · Minato-ku",
                "role":   "Private salon · client reception",
                "since":  "Opened in 2021",
                "head":   "Yumi Tanaka · concierge",
                "team":   "Three concierges · visiting seamstress",
                "image":  "https://images.unsplash.com/photo-1559563458-527698bf5295?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Direction credit
        "direction_label":   "Creative direction",
        "direction_name":    "Giulia Maison",
        "direction_role":    "Creative director · founder",
        "direction_text":
            "Giulia Maison studied at Central Saint Martins in London and worked for eight "
            "years between Hermès and Bottega Veneta before founding the maison in 2014. Her "
            "writing is Italian, of Brera, but her hand cuts in French. The maison is her "
            "studio.",
        "direction_portrait":
            "https://images.unsplash.com/photo-1624206112918-f140f087f9b5?w=600&q=80&auto=format&fit=crop",
        "direction_quote":
            "“Quantity is a decision, not a consequence. Forty-five pieces per season is the "
            "number that lets us look every client in the face.”",
        "direction_quote_attribution": "Giulia Maison · The Gentlewoman, 2025",

        # Press / editorial mentions
        "press_label":   "Editorial",
        "press_heading": "Recent press <em>appearances.</em>",
        "press_items": [
            {
                "magazine": "Vogue Italia",
                "issue":    "April 2026",
                "title":    "The new silence of Italian luxury",
                "byline":   "Feature · Sara Maino",
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
                "issue":    "Issue 84",
                "title":    "Filiation italienne",
                "byline":   "Text · Stefano Tonchi",
            },
            {
                "magazine": "Wallpaper*",
                "issue":    "March 2025",
                "title":    "Une maison bien cachée",
                "byline":   "Atelier visit · Tony Chambers",
            },
        ],

        # Numbers
        "numbers_label":   "Maison in numbers",
        "numbers_items": [
            ("12",    "years since founding"),
            ("3",     "ateliers around the world"),
            ("45",    "pieces per season"),
            ("9",     "silhouettes per drop"),
        ],

        # Visit card — 3 cities
        "visit_label":   "Visit the maison",
        "visit_heading": "Three houses, <em>three private salons.</em>",
        "visit_text":
            "The maisons in Milano, Paris and Tokyo receive by appointment only. The house "
            "concierge reserves a room, prepares the pieces suited to your profile, and "
            "arranges the fitting with the seamstress. Complimentary, reserved service.",
        "visit_primary":   "Request an appointment",
        "visit_primary_href": "contatti",
    },

    # ─── LOOKBOOK ─────────────────────────────────────────────
    "lookbook": {
        "issue":     "Spring–Summer 2026",
        "issue_label":"Issue",
        "issue_n":   "Issue 12",
        "eyebrow":   "Lookbook · Issue 12",
        "headline":  "The light of <em>Como, in March.</em>",
        "intro":
            "Eighteen images shot across three days of March at the Grand Hôtel Villa d'Este, "
            "on Lake Como. Styling by Carla Sozzani, photography by Letizia Carrera, set design "
            "by Sebastiano Pellion di Persano. The morning's natural light was the sole "
            "instrument of illumination.",

        # Credits panel
        "credits_label":   "Credits",
        "credits_rows": [
            ("Creative direction", "Giulia Maison · Maison Luxe Milano"),
            ("Styling",            "Carla Sozzani"),
            ("Photography",        "Letizia Carrera"),
            ("Set design",         "Sebastiano Pellion di Persano"),
            ("Hair & make-up",     "Lina Hammar · Art + Commerce"),
            ("Model",              "Sara Grace Wallerstedt · IMG Models"),
            ("Location",           "Grand Hôtel Villa d'Este · Cernobbio"),
            ("Print",              "Analogue run · Studio Riffraff Milano"),
        ],

        # Editorial grid — 6 looks
        "looks_label":   "The eighteen looks",
        "looks_intro":   "Six selected for press, twelve held in the private library.",
        "looks": [
            {
                "n":       "Look 03",
                "title":   "Double cady",
                "outfit":  "Double-cady robe-manteau · leather boots by Sentier",
                "credit":  "Styling · archive scarf 2018",
                "image":   "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 07",
                "title":   "Tailleur Cady Bianco",
                "outfit":  "Jacket + wide trouser · shoes by Atelier Sentier · Isola pochette",
                "credit":  "Set · the camellia garden",
                "image":   "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 09",
                "title":   "Carded wool from Biella",
                "outfit":  "Carded coat · crêpe trouser · sellier boot",
                "credit":  "Coat by Maglificio Lanifer",
                "image":   "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 11",
                "title":   "Rack Atelier Nero",
                "outfit":  "Short cashmere knit · crêpe trouser · Atelier bag",
                "credit":  "Atelier Sentier bag · 21 hours of making",
                "image":   "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 14",
                "title":   "Silk crêpe from Como",
                "outfit":  "Bomber Siena · wide crêpe trouser · tied sandal",
                "credit":  "Fabric by Setificio Tessitura Como",
                "image":   "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 18",
                "title":   "Borsa Isola · day",
                "outfit":  "Carded knit · atelier jeans · Borsa Isola",
                "credit":  "Atelier Sentier bag · Madonna leather",
                "image":   "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1200&q=80&auto=format&fit=crop",
            },
        ],

        # Editorial pull-quote
        "pullquote":
            "“Como in March is a closed room. The maison left it with eighteen photographs "
            "that render it legible.”",
        "pullquote_attribution": "Carla Sozzani · stylist of the lookbook",

        # Notes from set
        "notes_label":   "Notes from set",
        "notes_intro":
            "Three days of March, veiled sun, wind from the north-east. The model posed "
            "without interruption from seven to eleven, in the arriving light of morning. The "
            "cady jacket of Look 03 required two hours of pressing each morning to return to "
            "its pleats.",
        "notes_items": [
            {
                "label": "Day 01 · Camellia salon",
                "text":  "Seven looks in five hours of light. Changes of dress between one "
                         "take and the next in the adjoining room. Lunch at three.",
            },
            {
                "label": "Day 02 · Belvedere over the lake",
                "text":  "Six looks in the frontal light of morning. Light rain between eleven "
                         "and noon: the take postponed to the afternoon.",
            },
            {
                "label": "Day 03 · Private salon",
                "text":  "Five looks in candlelight and window light. The last three photographs "
                         "requested by the creative director for the opening pull-quote.",
            },
        ],

        # Buy from lookbook CTA
        "shop_label":   "Acquire from the lookbook",
        "shop_heading": "Every look leads <em>to its piece in the collection.</em>",
        "shop_intro":
            "The eighteen looks are navigable from the full collection. To request a piece, "
            "write to the house concierge — the waitlist opens on Friday 24 April.",
        "shop_primary":     "Go to the collection",
        "shop_primary_href":"collezione",
        "shop_secondary":   "Join the waitlist",
        "shop_secondary_href":"contatti",
    },

    # ─── CONTATTI (private appointment form) ──────────────────
    "contatti": {
        "eyebrow":  "Private client direction",
        "headline": "By <em>appointment only.</em>",
        "intro":
            "The maison receives exclusively by appointment, in three private salons in "
            "Milano, Paris and Tokyo. The house concierge prepares the pieces of your profile "
            "before your arrival and reserves the seamstress for the fitting. Reserved service, "
            "complimentary, by direct request.",

        # Form intro
        "form_section_label":  "Private request",
        "form_section_intro":
            "Kindly complete the card with the details of your appointment or your request. "
            "The house concierge replies within the next working day. For the Drop 04 waitlist "
            "— opening 24 April — please select the dedicated option.",

        "form_helper_required":  "Fields marked are required",
        "form_submit_button":    "Send private request",
        "form_submit_note":
            "Your data is handled exclusively by the house concierge. No newsletter, no "
            "commercial communication.",

        "form_fields": [
            {"name":"titolo",    "label":"Title",     "type":"select", "required":True,
             "options":["Ms.","Mr.","Mx","Studio·Atelier","Press"]},
            {"name":"nome",      "label":"Full name", "type":"text", "placeholder":"e.g. Ms. Eleonora Cattaneo", "required":True},
            {"name":"email",     "label":"Email",          "type":"email", "placeholder":"e.cattaneo@example.com", "required":True},
            {"name":"telefono",  "label":"Telephone",      "type":"tel",   "placeholder":"+39 …",                   "required":False},
            {"name":"city",      "label":"Maison of interest", "type":"select", "required":True,
             "options":["Milano · Via Senato","Paris · Sentier","Tokyo · Aoyama","No preference"]},
            {"name":"servizio",  "label":"Service requested", "type":"select", "required":True,
             "options":["Private viewing","Drop 04 waitlist","Bespoke piece","Archive reissue","Press"]},
            {"name":"capo",      "label":"Look or piece (opt.)", "type":"text", "placeholder":"e.g. Look 11 · Rack Atelier Nero", "required":False},
            {"name":"messaggio", "label":"Notes to the house concierge", "type":"textarea", "placeholder":"Please specify preferred date, sizes, personal profile.", "required":True, "rows":5},
        ],

        # Right-side card — three maison addresses
        "card_label":   "The three maisons",
        "maison_cards": [
            {
                "city":    "Milano",
                "address": "Via Senato 28 · 20121 Milano",
                "phone":   "+39 02 7600 1492",
                "email":   "milano@maisonluxe.com",
                "hours":   "Tue – Sat · 11:00 – 19:00 · by appointment only",
            },
            {
                "city":    "Paris",
                "address": "9 rue du Mail · 75002 Paris",
                "phone":   "+33 1 4296 4720",
                "email":   "paris@maisonluxe.com",
                "hours":   "Tue – Fri · 11:00 – 19:00 · by appointment only",
            },
            {
                "city":    "Tokyo",
                "address": "1-1-7 Aoyama · Minato-ku · Tokyo 107-0062",
                "phone":   "+81 3 6450 5018",
                "email":   "tokyo@maisonluxe.com",
                "hours":   "Wed – Sat · 12:00 – 20:00 · by appointment only",
            },
        ],

        # FAQ accordion (private viewing oriented)
        "faq_label":   "Frequently asked",
        "faq_items": [
            {
                "q": "How far in advance is a private viewing booked?",
                "a": "At least one week in advance for Milano and Paris; two weeks for Tokyo. "
                     "For urgent requests, please write directly to the house concierge.",
            },
            {
                "q": "Is the private viewing service charged for?",
                "a": "No — it is complimentary and reserved. It includes preparation of the "
                     "pieces, a seamstress in the salon, coffee and champagne, and a map of "
                     "the collection tailored to you.",
            },
            {
                "q": "May a bespoke piece be requested?",
                "a": "Yes, on the basis of the existing silhouettes. Delivery: eight to twelve "
                     "weeks. Fifty per cent deposit on confirmation of the drawing.",
            },
            {
                "q": "How does the waitlist work?",
                "a": "Those on the list hold absolute priority across every drop. Joining the "
                     "list carries no purchase obligation. Enrolment is complimentary, by "
                     "direct request.",
            },
        ],
    },
}
