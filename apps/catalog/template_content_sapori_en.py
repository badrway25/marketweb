"""Sapori di Langa - Enoteca dei Vignaioli (artisan-workshop archetype) - EN.

Wave 1 Pass-10 (T54 - 2026-05-12). EN locale built for shape-parity with
the IT source `template_content_sapori.py`. Locale files are independent:
constants are re-declared inline rather than imported.

Voice contract (EN):
- Wine Spectator / Decanter / Slow Food USA editorial register. Warm,
  knowledgeable, never marketing-speak. Second-person where IT uses
  tu/voi - "you" used warmly.
- Voice anchor `independent winegrower` (plural `independent winegrowers`)
  preserved verbatim across every band: hero headline, shop intro,
  product info, atelier intro, contatti faq. The anchor is load-bearing
  and appears 20+ times across all surfaces, mirroring the IT
  `vignaiolo indipendente` occurrence count.
- The headline `Vini di <em>vignaiolo indipendente</em> dalle Langhe del
  Barolo.` becomes `Wines from <em>independent winegrowers</em> in the
  Langhe of Barolo.` - the `<em>...</em>` tags are preserved exactly.

Italian proper names preserved verbatim:
- Brand `Sapori di Langa - Enoteca dei Vignaioli` stays IT.
- Personae `Pietro Brero`, `Federica Brero` stay IT.
- Producers (`Carlo Brezza`, `Maria Vajra`, `Luigi Boasso`, `Anna Brovia`)
  and their cantine (`Brezza & Figli`, `Vajra`, `Boasso`, `Brovia`).
- Places (`Alba`, `Langhe`, `Roero`, `Monferrato`, `Barolo`, `Cannubi`,
  `Bricco delle Viole`, `Gabutti`, `Villero`, `Bricco Sarmassa`,
  `Cannubi Muscatel`).
- Wine names (`Barolo`, `Barbera`, `Dolcetto`, `Nebbiolo`, `Verduno
  Pelaverga`, `Barbaresco`, `Rabaja`) and product names (`Olio EVO`,
  `Castelmagno DOP`, `Nocciola Tonda Gentile`, `Tartufo Bianco`).
- Italian chivalric order title `Cavalier dell'Ordine dei Cavalieri del
  Tartufo e dei Vini di Alba` stays IT (glossed once in atelier prose).
- Italian wine press titles (`Slow Wine`, `Gambero Rosso Vini`,
  `Vitae AIS`, `I Vini di Veronelli`, `Doctor Wine`) stay verbatim.
- Reference Domaine Romanee-Conti (FR domain) stays verbatim.

Wine register cheat-sheet: vignaiolo indipendente -> independent
winegrower (anchor); vendemmia manuale -> hand-picked harvest;
fermentazione spontanea -> wild fermentation; botte grande -> large
Slavonian oak cask; cassa di sei -> six-bottle case; consigli del
sommelier -> sommelier guidance.
"""
from __future__ import annotations

from typing import Any


# Imagery URLs from X.3 curator pack `wine-food-boutique.md`. All
# Pexels CC0 - commercial-safe. Re-declared inline per the locale-file
# independence convention.
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


SAPORI_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Cellar",            "kind": "home"},
        {"slug": "shop",     "label": "Catalogue",         "kind": "shop"},
        {"slug": "product",  "label": "Bottle",            "kind": "product"},
        {"slug": "atelier",  "label": "The winegrowers",   "kind": "about"},
        {"slug": "journal",  "label": "Journal",           "kind": "journal"},
        {"slug": "contatti", "label": "Visit & orders",    "kind": "contact"},
    ],

    "site": {
        "logo_initial": "S",
        "logo_word":    "Sapori di Langa",
        "tag":          "Independent winegrowers · Alba · since 1992",
        "phone":        "+39 0173 364 990",
        "whatsapp":     "0173 364 990",
        "whatsapp_link": "https://wa.me/390173364990",
        "email":        "enoteca@saporidilanga.it",
        "address":      "Via Vittorio Emanuele 38 · 12051 Alba CN",
        "hours_compact": "Tue – Sat · 9:30 – 19:30 · Sun 10 – 13",
        "hours_footer_rows": [
            "Sunday · 10:00 – 13:00 (mornings only)",
            "Monday · closed",
            "Truffle Fair · all-day hours Oct – Nov",
        ],
        "license":      "VAT 02814730042 · CCIAA Cuneo REA 263118",
        "footer_intro":
            "Wine merchant in Alba founded in 1992 by Pietro Brero. "
            "Thirty-two independent winegrowers across the Langhe, Roero "
            "and Monferrato - each with their own lot number, their own "
            "signature on the cuvée, their own single-parcel vinification. "
            "Refrigerated shipping in 48 hours within Italy.",
        "nav_cta":      "Order the winegrower's case",
        "nav_cta_kind": "case-order",

        "foot_studio":   "The shop",
        "foot_pages":    "Site map",
        "foot_contact":  "Orders & visits",
        "foot_stockists":"Restaurants that pour our wines",
        "stockists_rows": [
            "Piazza Duomo · Alba · 3 Michelin stars",
            "La Ciau del Tornavento · Treiso",
            "Locanda del Pilone · Madonna di Como",
            "Antica Corona Reale · Cervere",
        ],

        "currency_symbol":  "€",
        "shop_filter_label": "Filters",
        "shop_count_unit":   "bottles",
        "edition_label":     "Lot",
        "made_in_label":     "Vinified in",
        "artisan_label":     "Independent winegrower",
        "material_label":    "Varietal",
        "shipping_label":    "Shipping",
        "shipping_value":    "Refrigerated in 48 hours · six bottles per case",
        "guarantee_label":   "Guarantee",
        "guarantee_value":   "Any faulty bottle replaced free of charge",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "2023 vintage · thirty-two independent winegrowers in the cellar",
        "headline": "Wines from <em>independent winegrowers</em> in the Langhe of Barolo.",
        "intro":
            "We visit the vineyards twice a year. Once for the harvest, "
            "once to taste the vintages still in cask. For every cellar "
            "we know the winemaker by name, the parcel that was vinified, "
            "the lot in the bottle. Nothing here comes from a wholesale "
            "catalogue.",
        "primary_cta":   "Order the winegrower's case",
        "primary_href":  "shop",
        "secondary_cta": "Visit the shop",
        "secondary_href":"contatti",

        # Stamp-aside data
        "stamp_label":  "Our rule",
        "stamp_heading":"Two visits, <em>one bottle.</em>",
        "stamp_rows": [
            ("Winegrowers",  "32 cellars"),
            ("Labels",       "180 on the list"),
            ("Harvest",      "Always by hand"),
            ("Case",         "6 bottles"),
        ],
        "stamp_footer": "Numbered lot · refrigerated shipping",
        "stamp_corner_index": "01",
        "stamp_corner_word":  "THE SHOP",

        # Latest-arrived band — 4 bottles
        "latest_label":   "Just on the list",
        "latest_heading": "The latest vintages <em>from the Langhe.</em>",
        "latest_link_label": "The full catalogue",
        "latest_link_href":  "shop",
        "latest_items": [
            {
                "id":       "barolo-cannubi-2019",
                "n":        "Cuvée 2019",
                "edition":  "Lot 23 / 280",
                "name":     "Barolo Cannubi",
                "meta":     "Nebbiolo 100% · Barolo · La Morra",
                "price":    "€ 58",
                "tag":      "Vintage",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbera-superiore-2021",
                "n":        "Cuvée 2021",
                "edition":  "Lot 87 / 1,200",
                "name":     "Barbera d'Alba Superiore",
                "meta":     "Barbera 100% · Roero",
                "price":    "€ 22",
                "tag":      "Everyday",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "olio-evo-langhe",
                "n":        "2024 harvest",
                "edition":  "Lot 12 / 380",
                "name":     "Olio EVO Langhe DOP",
                "meta":     "Frantoio + Leccino · Diano d'Alba",
                "price":    "€ 28",
                "tag":      "Season",
                "image":    _BOTTLE_OLIO,
            },
            {
                "id":       "castelmagno-stagionato",
                "n":        "Aged 18 months",
                "edition":  "Wheel 04 / 22",
                "name":     "Castelmagno DOP d'Alpeggio",
                "meta":     "Cow's milk · Castelmagno CN",
                "price":    "€ 36",
                "tag":      "Summer batch",
                "image":    _BOTTLE_FORMAGGIO,
            },
        ],

        # Vignaioli band — 4 named vintners
        "makers_label":   "Hands that vinify",
        "makers_heading": "Thirty-two cellars, <em>one single list.</em>",
        "makers_intro":
            "We work only with independent winegrowers - those who vinify "
            "their own grapes from their own parcel and sign every lot on "
            "the list in person. Every cellar has been visited by Pietro "
            "at least three times before joining the catalogue.",
        "makers": [
            {
                "name":   "Carlo Brezza",
                "craft":  "Independent winegrower · historic Cannubi",
                "place":  "Barolo (CN)",
                "since":  "Vines since 1885 · Brezza since 1885",
                "quote":  "\"You don't make Barolo in a hurry. You make it "
                          "in silence: two years in large oak, an ear cocked "
                          "to hear whether the cask is singing or "
                          "complaining.\"",
                "portrait": _VIGNAIOLO_PORTRAIT_CARLO,
            },
            {
                "name":   "Maria Vajra",
                "craft":  "Independent winegrower · Bricco delle Viole",
                "place":  "Vergne · Barolo (CN)",
                "since":  "Family cellar since 1972",
                "quote":  "\"We only vinify what we watch grow. If a parcel "
                          "doesn't deliver the way it should, we don't bottle "
                          "that vintage. The independent winegrower's list is "
                          "also built on what isn't there.\"",
                "portrait": _VIGNAIOLO_PORTRAIT_MARIA,
            },
            {
                "name":   "Luigi Boasso",
                "craft":  "Independent winegrower · Gabutti Roccaforte",
                "place":  "Serralunga d'Alba (CN)",
                "since":  "Four generations in the vineyard",
                "quote":  "\"Nebbiolo is a deceptive grape. It becomes "
                          "whatever you tell it about the soil. That's why "
                          "I don't farm other parcels: learning a single "
                          "soil takes thirty years.\"",
                "portrait": _VIGNAIOLO_PORTRAIT_LUIGI,
            },
            {
                "name":   "Anna Brovia",
                "craft":  "Independent winegrower · Villero & Rocche dei Brovia",
                "place":  "Castiglione Falletto (CN)",
                "since":  "Cantina dei Brovia since 1863",
                "quote":  "\"We don't enter competitions, we don't chase "
                          "scores. We make Barolo the way it has always been "
                          "made in Castiglione Falletto: long, austere, no "
                          "frills. Anyone looking for easy wine should look "
                          "elsewhere.\"",
                "portrait": _VIGNAIOLO_PORTRAIT_PIETRO,
            },
        ],

        # Provenance — terroir + filiera
        "provenance_label":   "Where it comes from",
        "provenance_heading": "Sixty-five kilometres, <em>three denominations.</em>",
        "provenance_intro":
            "Every label on the list comes from within a sixty-five "
            "kilometre radius of Alba. Three principal denominations - "
            "Langhe, Roero, Monferrato - and a network of independent "
            "winegrowers who have chosen each other.",
        "provenance_items": [
            {
                "icon": "vine",
                "title": "Langhe DOCG",
                "desc":  "Barolo, Barbaresco, Dolcetto · eleven producing "
                         "communes · limestone and marl soils · altitude "
                         "200-400 m above sea level.",
                "place": "Alba · La Morra · Barolo · Castiglione",
            },
            {
                "icon": "hills",
                "title": "Roero DOCG",
                "desc":  "Nebbiolo Roero, Arneis, Favorita · across the "
                         "Tanaro · sandy soils · leaner, more aromatic "
                         "wines · altitude 280-380 m above sea level.",
                "place": "Canale · Vezza · Santo Stefano Roero",
            },
            {
                "icon": "cheese",
                "title": "Monferrato Casalese",
                "desc":  "Barbera Superiore, Grignolino, Ruchè · rolling "
                         "hillsides · calcareous-clay soils · everyday "
                         "wines with character.",
                "place": "Casale · Vignale · Rosignano",
            },
            {
                "icon": "olive",
                "title": "Ligurian Riviera (50 km)",
                "desc":  "Olio EVO Taggiasco DOP · charcoal-cured Trapani "
                         "salt · La Spezia mackerel in oil. Long-standing "
                         "suppliers of the house.",
                "place": "Imperia · La Spezia · Trapani",
            },
        ],

        # Care — wine handling guarantees
        "care_label":   "How it arrives, how to keep it",
        "care_heading": "Four promises in every case.",
        "care_items": [
            ("Refrigerated shipping",
             "A six-bottle case shipped in a thermal box with gel packs at "
             "14°C. Delivery in 48 hours anywhere in Italy · 4 days in "
             "Western Europe."),
            ("Numbered lot, signed by hand",
             "Every bottle carries the lot number, the cuvée vintage and "
             "the independent winegrower's signature written by hand. No "
             "industrial-typographic label."),
            ("Faulty-bottle replacement",
             "TCA, oxidation, breakage in transit · we replace the bottle "
             "free of charge within three months of delivery, on simple "
             "photographic proof of the cork or the fill level."),
            ("Sommelier guidance",
             "Pietro or Federica will call you back within 24 hours if you "
             "need a pairing for an evening, a vertical for a birthday, a "
             "case for a corporate gift."),
        ],

        # Press band — Italian wine press
        "press_label": "Reviewed in",
        "press_items": ["Slow Wine", "Gambero Rosso Vini", "Vitae AIS",
                        "I Vini di Veronelli", "Doctor Wine"],

        # Journal teaser
        "journal_teaser_label":   "Notes from the journal",
        "journal_teaser_heading": "How we built the <em>autumn 2026 list.</em>",
        "journal_teaser_link":    "Read the journal",
        "journal_teaser_href":    "journal",

        # CTA section
        "cta_label":     "Order · visit · write to us",
        "cta_heading":   "A six-bottle case, <em>chosen by Pietro.</em>",
        "cta_intro":
            "The curated cases change every month according to which "
            "cellars are delivering. Everyday drinking wines, wines for "
            "cellaring, mixed formats with oil and cheese. Pay on "
            "collection, ships refrigerated in 48 hours.",
        "cta_primary":      "Order this month's case",
        "cta_primary_href": "shop",
        "cta_secondary":    "Come to the shop",
    },

    # ─── SHOP (catalog) ─────────────────────────────────────────
    "shop": {
        "eyebrow":  "House list · 2023-2024 vintage",
        "headline": "One hundred and eighty labels, <em>one single signature.</em>",
        "intro":
            "The full list of wines, oils, cheeses and preserves. Every "
            "label comes from an independent winegrower we have visited "
            "in person. For every wine we record the cuvée, the lot, the "
            "vintage and the independent winegrower who signs it.",

        "filter_section_label": "Filters",
        "filter_groups": [
            {
                "label": "Denomination",
                "options": ["Barolo DOCG", "Barbaresco DOCG", "Roero DOCG",
                            "Langhe DOC", "Monferrato DOC", "Asti DOCG",
                            "Vino da Tavola"],
            },
            {
                "label": "Varietal",
                "options": ["Nebbiolo", "Barbera", "Dolcetto", "Arneis",
                            "Favorita", "Grignolino"],
            },
            {
                "label": "Type",
                "options": ["Red wines", "White wines", "Sweet wines",
                            "Sparkling", "Oils & condiments", "Cheeses",
                            "Cured meats & preserves"],
            },
        ],

        "sort_label": "Sort by",
        "sort_options": ["Most recent", "Independent winegrower", "Vintage", "Price"],

        "result_count": "180 bottles",
        "result_subtitle": "Updated Tuesday 8 October 2026",

        # Sample products — 8 cards (the shop shows more but this is the
        # featured slice)
        "products": [
            {
                "id":       "barolo-cannubi-2019",
                "n":        "01",
                "edition":  "Cuvée 2019 · Lot 23",
                "name":     "Barolo Cannubi · Brezza",
                "meta":     "Nebbiolo · Barolo · La Morra",
                "price":    "€ 58",
                "tag":      "Vintage",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbaresco-rabaja-2018",
                "n":        "02",
                "edition":  "Cuvée 2018 · Lot 11",
                "name":     "Barbaresco Rabajà · Cortese",
                "meta":     "Nebbiolo · Barbaresco · Treiso",
                "price":    "€ 64",
                "tag":      "Vertical",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbera-superiore-2021",
                "n":        "03",
                "edition":  "Cuvée 2021 · Lot 87",
                "name":     "Barbera d'Alba Superiore · Vajra",
                "meta":     "Barbera · Roero · Canale",
                "price":    "€ 22",
                "tag":      "Everyday",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "dolcetto-diano-2022",
                "n":        "04",
                "edition":  "Cuvée 2022 · Lot 42",
                "name":     "Dolcetto di Diano d'Alba · Boasso",
                "meta":     "Dolcetto · Diano d'Alba",
                "price":    "€ 16",
                "tag":      "Table",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "arneis-roero-2023",
                "n":        "05",
                "edition":  "Cuvée 2023 · Lot 56",
                "name":     "Roero Arneis · Brovia",
                "meta":     "Arneis · Vezza d'Alba",
                "price":    "€ 18",
                "tag":      "White",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "olio-evo-langhe",
                "n":        "06",
                "edition":  "2024 harvest · Lot 12",
                "name":     "Olio EVO Langhe DOP · Frantoio Anfossi",
                "meta":     "Frantoio + Leccino · Diano d'Alba",
                "price":    "€ 28",
                "tag":      "Season",
                "image":    _BOTTLE_OLIO,
            },
            {
                "id":       "castelmagno-stagionato",
                "n":        "07",
                "edition":  "Aged 18 months · Wheel 04",
                "name":     "Castelmagno DOP d'Alpeggio",
                "meta":     "Piedmontese cow's milk",
                "price":    "€ 36",
                "tag":      "Cheese",
                "image":    _BOTTLE_FORMAGGIO,
            },
            {
                "id":       "salame-cuneo",
                "n":        "08",
                "edition":  "Aged 4 months · Lot 08",
                "name":     "Salame Cuneo · Macelleria Cesare",
                "meta":     "Cuneo pork · black pepper · wine in the cut",
                "price":    "€ 24",
                "tag":      "Cured meats",
                "image":    _BOTTLE_FORMAGGIO,
            },
        ],

        "featured_product_id": "barolo-cannubi-2019",

        "footer_note_label": "Shipping & collection",
        "footer_note":
            "Refrigerated shipping in 48 hours within Italy · minimum "
            "six-bottle case · shipping € 12 (free over € 200). Walk-in "
            "collection at the shop with no notice required. For orders "
            "over twelve bottles, contact us directly.",
    },

    # ─── PRODUCT ────────────────────────────────────────────────
    "product": {
        "id":       "barolo-cannubi-2019",
        "n":        "01",
        "edition":  "Cuvée 2019",
        "edition_note": "Lot 23 / 280 · bottled December 2022",
        "name":     "Barolo Cannubi · Brezza",
        "subtitle": "Nebbiolo 100% · vinified on the historic Cannubi hill",
        "price":    "€ 58",
        "vat_note": "VAT included · minimum six-bottle case",
        "intro":
            "A Barolo from the Brezza cellar, off the historic Cannubi "
            "parcel - the oldest single hill in the village of Barolo, "
            "with vineyard records dating back to 1752. Hand-picked "
            "harvest, fermentation in stainless steel, ageing in large "
            "Slavonian oak casks for 30 months, then another 12 in bottle "
            "before release.",

        "gallery": [
            _BOTTLE_BAROLO,
            _BOTTLE_BAROLO,
            _BOTTLE_BAROLO,
        ],

        "info_label": "Tasting sheet",
        "info_rows": [
            ("Independent winegrower", "Carlo Brezza · Brezza & Figli"),
            ("Denomination",  "Barolo DOCG"),
            ("Varietal",      "Nebbiolo 100%"),
            ("Commune",       "Barolo (CN)"),
            ("Parcel",        "Cannubi storico"),
            ("Altitude",      "260 m above sea level · south-east exposure"),
            ("Harvest",       "Hand-picked · second week of October 2019"),
            ("Ageing",        "30 months large cask + 12 months bottle"),
            ("Alcohol",       "14.5% vol"),
            ("Sulphites",     "< 80 mg/l · certified organic viticulture"),
        ],

        "size_label": "Available formats",
        "size_intro": "Available as single bottle, magnum, horizontal 2019 case and 2015 – 2019 vertical case.",
        "size_options": ["750 ml", "1.5 L Magnum", "Case 6 · 2019", "Case 6 · vertical"],
        "size_chart_link": "See all formats & verticals",
        "size_chart_href": "shop",

        "artisan_label":   "Independent winegrower",
        "artisan_name":    "Carlo Brezza",
        "artisan_role":    "Fourth generation · Brezza & Figli since 1885",
        "artisan_bio":
            "Family cellar founded by Carlo's great-grandfather in 1885, "
            "passed down father-to-son in a straight line. Carlo started "
            "in the vineyard in 1997 after studying oenology in Alba and "
            "spending three harvests at Domaine Romanée-Conti. He vinifies "
            "exclusively the parcels owned by the family (Cannubi storico, "
            "Bricco Sarmassa, Cannubi Muscatel) - no purchased grapes.",
        "artisan_portrait": _VIGNAIOLO_PORTRAIT_CARLO,

        "buy_primary":   "Add to the case",
        "buy_secondary": "Reserve at the shop",
        "buy_note":
            "Orders over 12 bottles · contact the cellar directly. "
            "Availability confirmed at the moment of ordering.",

        "care_label": "Storage",
        "care_intro":
            "A Barolo for cellaring · it needs careful storage to express "
            "its full potential.",
        "care_items": [
            ("Temperature",  "12-14°C constant · no swings"),
            ("Position",     "Lying flat · cork always in contact with the wine"),
            ("Humidity",     "At least 70% · dark environment"),
            ("Opening",      "Open 2-3 hours ahead · decanting recommended"),
            ("Plateau",      "Ready to drink 2025-2040 · maturity plateau 2028-2035"),
        ],

        "provenance_label":   "From Cannubi to the glass",
        "provenance_heading": "Four traced steps.",
        "provenance_steps": [
            ("01", "Harvest",       "Hand-picked into 18 kg crates · Cannubi at 260 m above sea level · second week of October 2019"),
            ("02", "Ageing",        "Large Slavonian oak cask · 30 months · never barriqued · Cantina Brezza Barolo"),
            ("03", "Bottling",      "December 2022 · no filtration · no fining · lot 23 of 280"),
            ("04", "Shipping",      "Stamped wooden case · thermal box with gel packs at 14°C · 48 hours within Italy"),
        ],

        "related_label":   "Verticals and pairings",
        "related_intro":
            "Cuvées from the same cellar in earlier vintages, plus wines "
            "Pietro recommends as a comparative pairing.",
        "related_items": [
            {"id":"barolo-cannubi-2018",   "n":"No. 088","name":"Barolo Cannubi · 2018",   "meta":"Cool vintage · Brezza",          "price":"€ 62","image":_BOTTLE_BAROLO},
            {"id":"barolo-cannubi-2017",   "n":"No. 074","name":"Barolo Cannubi · 2017",   "meta":"Warm vintage · Brezza",          "price":"€ 68","image":_BOTTLE_BAROLO},
            {"id":"barbaresco-rabaja-2018","n":"No. 142","name":"Barbaresco Rabajà · 2018","meta":"Side-by-side terroir",            "price":"€ 64","image":_BOTTLE_BAROLO},
            {"id":"barbera-vajra",         "n":"No. 211","name":"Barbera Superiore · 2021","meta":"Everyday at the table · Vajra",   "price":"€ 22","image":_BOTTLE_BARBERA},
        ],
    },

    # ─── ATELIER (about · "The winegrowers") ───────────────────
    "atelier": {
        "eyebrow":  "The shop",
        "headline": "Sapori di Langa: <em>thirty-two independent winegrowers, one single sign.</em>",
        "intro":
            "Sapori di Langa is an independent wine merchant founded in "
            "Alba in 1992. We work exclusively with independent "
            "winegrowers who vinify on their own land · no cooperatives · "
            "no industrial wine · no labels designed at a desk. To join "
            "the list, a cellar is visited by Pietro at least three times.",

        "mission_label":   "Our mission",
        "mission_heading": "Pay the winegrower a fair price.",
        "mission_text":
            "The shop exists for one reason: to give the independent "
            "winegrower back the price their work deserves. Margins agreed "
            "transparently, annual contracts signed by hand, advance "
            "payments on the grapes in the vineyard when needed. We don't "
            "do \"discounts\" because someone making 14% Nebbiolo cannot "
            "discount anything.",

        "process_label":   "How we choose the labels",
        "process_heading": "Three visits, one list.",
        "process_steps": [
            {"num": "01", "title": "First visit · spring",
             "desc": "Pietro goes to the vineyard in March or April, looks at "
                     "the pruning, tastes the last vintages straight from the "
                     "cask, talks with the winegrower about how the previous "
                     "summer went."},
            {"num": "02", "title": "Second visit · harvest",
             "desc": "September-October · a full day in at the harvest, with "
                     "at least three crates opened. We watch who's in the "
                     "vineyard picking, and with what care."},
            {"num": "03", "title": "Third visit · cellar tasting",
             "desc": "The following winter · technical tasting of the casks "
                     "with the winemaker. If the numbers add up and the wine "
                     "tells the truth, the annual contract is signed."},
            {"num": "04", "title": "Joining the list",
             "desc": "The first lot enters the list only after the fourth "
                     "visit (out of cask, in the bottle). Nothing reaches the "
                     "list that Pietro hasn't tasted across three different "
                     "vintages."},
        ],

        "founder_label":   "The founder",
        "founder_heading": "Pietro Brero.",
        "founder_text":
            "Pietro was born in Alba in 1958. Raised in the family "
            "trattoria, he worked as sommelier at Davide Scabin's "
            "Combal.Zero from 1985 to 1991, the year Combal was still in "
            "Almese. He opened Sapori di Langa in 1992 on Via Vittorio "
            "Emanuele with three cellars on the list. Today there are "
            "thirty-two. Inducted into the Cavalier dell'Ordine dei "
            "Cavalieri del Tartufo e dei Vini di Alba - the Order of the "
            "Knights of the Truffle and Wines of Alba - in 2014.",
        "founder_portrait": _FOUNDER_PORTRAIT,
        "founder_caption": "Pietro Brero · Cavalier dell'Ordine dei Cavalieri del Tartufo e dei Vini di Alba",

        "numbers_label":   "The shop in numbers",
        "numbers_items": [
            ("32",   "independent winegrowers on the list"),
            ("180",  "labels in the annual catalogue"),
            ("1992", "year we opened"),
            ("65 km","maximum sourcing radius from the Langhe"),
        ],

        "visit_label":   "Visit the shop",
        "visit_heading": "Via Vittorio Emanuele 38, <em>Alba.</em>",
        "visit_text":
            "Five minutes from Alba station · ten minutes from the "
            "Cathedral. Guided tasting by appointment on Thursday "
            "afternoons · five wines paired with a board of Castelmagno "
            "and Salame Cuneo, € 35 per person. No appointment needed for "
            "purchases during opening hours.",
        "visit_primary":      "Book a tasting",
        "visit_primary_href": "contatti",
        "visit_secondary":    "Map & hours",
    },

    # ─── JOURNAL ───────────────────────────────────────────────
    "journal": {
        "eyebrow":  "Shop journal",
        "headline": "Notes from the cellar, <em>notes from the harvest.</em>",
        "intro":
            "Short field notes from Pietro and Federica on the work in "
            "the cellar, on harvests in progress, on the bottles opened "
            "in the evening for the most curious customers. Read at your "
            "leisure.",
        "list_label": "Journal entries",
        "entries": [
            {
                "slug":    "vendemmia-2024-langhe",
                "kicker":  "Harvest 2024",
                "title":   "Harvest 2024 in the Langhe · what came out of the casks",
                "date":    "10 October 2026",
                "read_min": 6,
                "author":  "Pietro Brero",
                "lede":
                    "The 2024 harvest demanded patience. August's heat "
                    "slowed ripening, September put things back on track. "
                    "Here's what's joining the list in November.",
            },
            {
                "slug":    "barolo-2019-degustazione",
                "kicker":  "Vintage on the list",
                "title":   "Why the 2019 Barolo is worth the six-year wait",
                "date":    "28 September 2026",
                "read_min": 5,
                "author":  "Pietro Brero",
                "lede":
                    "The 2019 vintage was released in August after thirty "
                    "years of Barolo in the cellar. Here's why it's worth "
                    "the two years in large cask and the six-year minimum "
                    "before you uncork it.",
            },
            {
                "slug":    "olio-evo-langhe-2024",
                "kicker":  "House oil",
                "title":   "Olio EVO Langhe 2024 · a harvest to mark down",
                "date":    "15 September 2026",
                "read_min": 4,
                "author":  "Federica Bertola",
                "lede":
                    "Frantoio Anfossi closed the 2024 harvest on "
                    "5 September. Five hectolitres on the list from "
                    "October, lot 12. Here's how it tastes.",
            },
        ],

        "footer_note_label": "Receive the journal by email",
        "footer_note":
            "Four or five issues a year, no more. You only receive it if "
            "you explicitly ask at the till or via the contact form.",
    },

    # ─── CONTATTI ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Visit & orders",
        "headline": "One phone call, <em>one case.</em>",
        "intro":
            "To order a case or book a guided tasting, the simplest way is "
            "a phone call to the shop during opening hours. Or use the "
            "form below · we reply within 24 hours on working days.",

        "form_section_label": "Write to us",
        "form_section_intro":
            "For special orders (verticals, magnums, corporate cases), "
            "indicate the independent winegrower or the vintage you're interested in. "
            "For guided tastings, indicate the date and number of guests.",
        "form_helper_required": "Fields marked with an asterisk are required.",
        "form_submit_button":   "Send request",
        "form_submit_note":     "You'll receive an email confirmation within 24 hours during opening hours.",

        "form_fields": [
            {"name": "name",     "label": "Full name",       "type": "text",     "required": True},
            {"name": "email",    "label": "Email",           "type": "email",    "required": True},
            {"name": "phone",    "label": "Phone",           "type": "tel",      "required": False},
            {"name": "subject",  "label": "Subject",         "type": "select",
             "options": ["Case order", "Guided tasting", "Vertical or magnum",
                         "Corporate case or gift", "Other"],     "required": True},
            {"name": "message",  "label": "Message",         "type": "textarea", "required": True,
             "placeholder": "E.g. \"Six-bottle case of Barolo cuvée 2019\" or "
                             "\"Tasting for four people on Thursday 18 October\"."},
        ],

        "card_label":          "The shop",
        "card_address_label":  "Address",
        "card_address_value":  "Via Vittorio Emanuele 38 · 12051 Alba CN",
        "card_phone_label":    "Phone",
        "card_phone_value":    "+39 0173 364 990",
        "card_whatsapp_label": "WhatsApp",
        "card_whatsapp_value": "0173 364 990",
        "card_email_label":    "Email",
        "card_email_value":    "enoteca@saporidilanga.it",
        "card_hours_label":    "Hours",
        "card_hours_rows": [
            "Tue – Sat · 9:30 – 19:30 all-day hours",
            "Sunday · 10:00 – 13:00 mornings only",
            "Monday · closed · private tastings by appointment",
            "Truffle Fair · Oct – Nov · 9 – 21 all-day hours",
        ],
        "card_directions_label": "Getting here",
        "card_directions_text":
            "Five minutes on foot from Alba station (regional train direct "
            "from Turin · 1 h 10 min). Ten minutes from the Cathedral of "
            "San Lorenzo. Free parking in Piazza Risorgimento, 200 metres "
            "from the shop.",

        "faq_label": "Frequently asked",
        "faq_items": [
            ("How much does shipping cost?",
             "Refrigerated shipping in 48 hours: € 12 within Italy "
             "(free over € 200), € 24 to Western Europe. Minimum "
             "six-bottle case."),
            ("Can I order a single bottle?",
             "No, the minimum case is six bottles. Free composition "
             "across wine, oil, cheese and cured meats. The indicative "
             "value of the minimum case is around € 90-100."),
            ("Do you carry organic or natural wines?",
             "Yes. Around 70% of the independent winegrowers on our list "
             "farm in certified organic, 20% in Demeter-certified "
             "biodynamic. The rest follow low-intervention protocols but "
             "aren't certified."),
            ("Do you ship abroad?",
             "Western Europe yes (France, Germany, Belgium, Netherlands, "
             "Luxembourg, Austria). Rest of the world by quote only "
             "(USA · UK · Switzerland · Japan)."),
            ("Can I visit the shop without booking?",
             "Yes, during opening hours. The Thursday-afternoon guided "
             "tasting requires booking at least 48 hours in advance."),
        ],
    },
}
