"""Podere Le Querce — Tuscan family agriturismo (artisan-workshop · EN).

T60 · Wave 2 Pass-4 (2026-05-13) · close-out of the podere-agriturismo
template after the IT pass (T59). Mirrors the IT recursive shape leaf
for leaf · zero missing, zero extra paths (218 leaves verified).

Voice contract (EN):
- Editorial register: Travel + Leisure · Condé Nast Traveler Italia ·
  Slow Food USA · National Geographic Traveler. Warm-familiar tone
  (the family welcomes you to a long lunch · plural "you" across
  the contact band, polite "you" in form-helper text).
- Voice anchor `farm hospitality` — translates IT `ospitalità
  contadina` and foregrounds the multigenerational-family-hosts-
  you promise. Load-bearing in headline, famiglia statement, soggiorno
  intro and FAQ, footer intro. The anchor appears verbatim on ≥ 15
  surfaces across the file (counted at write time).
- Loanwords kept literal per T+L / CNT / Slow Food USA convention:
  `podere`, `agriturismo`, `pecorino`, `norcino`, `ribollita`, `Vin
  Santo`, `cinta senese`, `zolfini`, `Senatore Cappelli`. The page
  title "La dispensa" stays Italian — it is the literal name of the
  farm shop in EN editorial.
- Italian proper names preserved verbatim: family (Pasquinelli ·
  Maria · Carlo · Giovanni · Anna · Mario · Annetta · Maddalena),
  producers (Andrea Falleri · Famiglia Bartoletti · Davide Pieri ·
  Suore di San Vivaldo), historical (Antinori 1934), places (Greve
  in Chianti · Lamole · Roccastrada · Castelfiorentino · Montaione ·
  Vinci · Zeri · Le Querce). Tuscany / Florence are used in EN
  (consistent choice). Wines IT (Chianti Classico · Sangiovese ·
  Canaiolo · Colorino · Vin Santo). DOCG / DOP labels IT.
- Latin digits throughout. Phone format `+39 055 853 261`.
- The headline `Quattro generazioni in un podere. <em>Ospitalità
  contadina</em>, tutto l'anno.` becomes `Four generations on a
  Tuscan farm. <em>Farm hospitality</em>, all year round.` with the
  `<em>` tags preserved exactly.

Shape parity is verified at write time against template_content_podere
.py via factory/standards/artisan-workshop-shape-contract.md. All
critical iterator shapes (products[11] · provenance_steps tuple3 ·
size_options scalar · process_steps 5-key dict · faq_items q/a dict
· card_hours_rows scalar · press_items scalar) match the IT canon.
"""
from __future__ import annotations

from typing import Any


# Interim Unsplash CC0 imagery pool · same URLs as the IT file so
# that EN and IT render identical imagery. X.5 curator pack pending.
_PODERE_HERO = "https://images.unsplash.com/photo-1602941525521-46f6f1ab39ce?w=1600&q=80&auto=format&fit=crop"
_OLIVETO = "https://images.unsplash.com/photo-1567416661576-d8b6e92e63d2?w=1200&q=80&auto=format&fit=crop"
_VIGNA_CHIANTI = "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=1200&q=80&auto=format&fit=crop"
_TAVOLATA = "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1200&q=80&auto=format&fit=crop"
_CUCINA_CONTADINA = "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=1200&q=80&auto=format&fit=crop"
_FAMIGLIA_PORTRAIT = "https://images.unsplash.com/photo-1573497019418-b400bb3ab074?w=1200&q=80&auto=format&fit=crop"
_OLIO_BOTTLE = "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=1200&q=80&auto=format&fit=crop"
_VINO_BOTTLE = "https://images.unsplash.com/photo-1474722883778-792e7990302f?w=1200&q=80&auto=format&fit=crop"
_VINSANTO = "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=1200&q=80&auto=format&fit=crop"
_MIELE = "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=1200&q=80&auto=format&fit=crop"
_MARMELLATA = "https://images.unsplash.com/photo-1535990379313-50d1f6fc0c4f?w=1200&q=80&auto=format&fit=crop"
_PECORINO = "https://images.unsplash.com/photo-1452195100486-9cc805987862?w=1200&q=80&auto=format&fit=crop"
_SALAME = "https://images.unsplash.com/photo-1599379892470-bbe1eb01ea75?w=1200&q=80&auto=format&fit=crop"
_CANTUCCI = "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1200&q=80&auto=format&fit=crop"
_PORTRAIT_MARIA = "https://images.unsplash.com/photo-1559963110-71b394e7494d?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_CARLO = "https://images.unsplash.com/photo-1545167622-3a6ac756afa4?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_GIOVANNI = "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_ANNA = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_PRODUCER = "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=900&q=80&auto=format&fit=crop"


PODERE_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "The podere",       "kind": "home"},
        {"slug": "dispensa",  "label": "The dispensa",     "kind": "shop"},
        {"slug": "prodotto",  "label": "The product",      "kind": "product"},
        {"slug": "famiglia",  "label": "The family",       "kind": "about"},
        {"slug": "diario",    "label": "Field journal",    "kind": "journal"},
        {"slug": "soggiorno", "label": "Stay with us",     "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":    "Q",
        "logo_word":       "Podere Le Querce",
        "tag":             "Family agriturismo · Greve in Chianti · farm hospitality since 1934",
        "phone":           "+39 055 853 261",
        "whatsapp":        "+39 339 458 1126",
        "whatsapp_link":   "https://wa.me/393394581126",
        "email":           "famiglia@podereleQuerce.it",
        "address":         "Località Le Querce 14 · 50022 Greve in Chianti · Florence",
        "hours_compact":   "Open all year · kitchen by reservation 12:30 and 19:30",
        "hours_footer_rows": [
            "Guest reception 8-22 · Maria in the kitchen from 7",
            "Dispensa open daily 9-19 · closed on Sunday",
        ],
        "license":         "CITRA licence 048-029-001 · CCIAA Florence 354210 · Az. Agricola Pasquinelli S.S.",
        "footer_intro":
            "Podere Le Querce is a family-run agriturismo in Greve in Chianti · "
            "thirteen hectares of land with a historic olive grove, a Sangiovese "
            "vineyard, a kitchen garden, a Cinta Senese pig stable, a wine cellar "
            "and four guest rooms of farm hospitality. We make everything in "
            "house: olive oil, wine, honey, salami, pasta, cantucci. The "
            "Pasquinelli family has lived here since 1934. When you come as our "
            "guests, you eat at our table.",

        # Nav CTA — agriturismo-flavoured
        "nav_cta":         "Reserve your stay",
        "nav_cta_kind":    "appointment",

        # Footer labels
        "foot_studio":     "The podere",
        "foot_pages":      "Site map",
        "foot_contact":    "Stay with us",
        "foot_stockists":  "Where to find us",
        "stockists_rows": [
            "Mercato della Terra · Greve in Chianti · Sunday morning",
            "Slow Food Florence · monthly market stall",
            "Home shipping · Italy 24-48h · Europe 4-6 days",
            "Dispensa at the podere · open to the public daily 9-19",
        ],

        # Currency + product labels (used on shop cards + product page)
        "currency_symbol":   "€",
        "shop_filter_label": "Refine the dispensa",
        "shop_count_unit":   "products from the podere",
        "edition_label":     "Vintage",
        "made_in_label":     "Made in",
        "artisan_label":     "Hands of",
        "material_label":    "Raw material",
        "shipping_label":    "Shipping",
        "shipping_value":    "24-48h in Italy · refrigerated shipping in summer",
        "guarantee_label":   "Podere guarantee",
        "guarantee_value":   "We replace every broken or faulty bottle free of charge · within 30 days",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Agriturismo · farm hospitality · Greve in Chianti · since 1934",
        "headline": "Four generations on a Tuscan farm. <em>Farm hospitality</em>, all year round.",
        "intro":
            "Podere Le Querce has been home to the Pasquinelli family since "
            "1934, when great-grandparents Mario and Annetta bought it from "
            "the Antinori family with a deed of sale still kept at the town "
            "hall. Today it is an agriturismo with four guest rooms of farm "
            "hospitality, a family kitchen with a shared table by reservation, "
            "and a farm dispensa stocked with our eight farm-direct products.",

        "primary_cta":          "Reserve your stay",
        "primary_href":         "soggiorno",
        "secondary_cta":        "Visit the dispensa",
        "secondary_href":       "dispensa",

        # Stamp panel — list[4] of tuple[2]
        "stamp_label":   "The podere in four lines · farm hospitality",
        "stamp_heading": "Four generations · one shared table.",
        "stamp_rows": [
            ("Year",              "1934 · deed of sale Antinori → Pasquinelli"),
            ("Family",            "Maria + Carlo + Giovanni + Anna · four at the helm"),
            ("Hectares",          "13 hectares · olive grove + vineyard + garden + stable"),
            ("Rooms",             "4 guest rooms · farm hospitality open all year"),
        ],
        "stamp_footer":      "Mercato della Terra Greve · Slow Food Florence · Home shipping Italy 24-48h",
        "stamp_corner_index": "Season",
        "stamp_corner_word":  "2026",

        # Latest items — list[4] of dict[8 keys=edition,id,image,meta,n,name,price,tag]
        "latest_label":       "In the dispensa",
        "latest_heading":     "Eight farm-direct products, always available.",
        "latest_link_label":  "All products",
        "latest_link_href":   "dispensa",
        "latest_items": [
            {
                "id":      "olio-evo-podere-2025",
                "n":       "No. 01",
                "image":   _OLIO_BOTTLE,
                "edition": "2025 harvest",
                "name":    "Podere extra virgin olive oil",
                "meta":    "Moraiolo + Frantoio + Leccino · 2,400 trees",
                "price":   "€ 28 / 500 ml",
                "tag":     "New · November harvest",
            },
            {
                "id":      "chianti-classico-2022",
                "n":       "No. 02",
                "image":   _VINO_BOTTLE,
                "edition": "2022 vintage",
                "name":    "Chianti Classico DOCG",
                "meta":    "Sangiovese 95% · 1.8 ha of vineyard",
                "price":   "€ 22 / bottle",
                "tag":     "Podere cellar",
            },
            {
                "id":      "miele-millefiori",
                "n":       "No. 04",
                "image":   _MIELE,
                "edition": "July 2025 extraction",
                "name":    "Wildflower honey",
                "meta":    "12 hives · chestnut woodland clearing",
                "price":   "€ 14 / 250 g",
                "tag":     "One hundred percent podere",
            },
            {
                "id":      "salame-cinta-senese",
                "n":       "No. 07",
                "image":   _SALAME,
                "edition": "9-month curing",
                "name":    "Cinta Senese salami",
                "meta":    "Heritage black pigs raised semi-wild",
                "price":   "€ 38 / whole piece",
                "tag":     "8 head in the stable",
            },
        ],

        # Makers — list[4] of dict[6 keys=craft,name,place,portrait,quote,since]
        # NB: in the agriturismo register `makers` are local producers
        # whose work completes the family table when our own farm
        # production alone is not enough — shepherd, miller, norcino,
        # monastery.
        "makers_label":   "The producers of the territory",
        "makers_heading": "Four pairs of hands that complete our table.",
        "makers_intro":
            "The podere's own products are not enough for every guest at the "
            "table · for four generations the Pasquinelli family has relied on "
            "the same producers from the territory. All within thirty kilometres "
            "of the farm.",
        "makers": [
            {
                "craft":    "Shepherd · raw-milk pecorino",
                "name":     "Andrea Falleri",
                "place":    "Lamole · 4 km from the podere",
                "since":    "Family supplier since 1987",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "The Pasquinellis have been buying my Lamole pecorino since "
                    "I was a boy. My grandfather sold it to their father, and "
                    "now I sell it to Maria. That's how things are passed down "
                    "here.",
            },
            {
                "craft":    "Miller · Maremma durum wheat",
                "name":     "Famiglia Bartoletti",
                "place":    "Roccastrada · 28 km from the podere",
                "since":    "Family mill since 1820",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "We stone-mill Senatore Cappelli durum wheat · Maria turns "
                    "it into pasta for the Sunday shared table. The flavour of "
                    "the old flour is the flavour of her pasta.",
            },
            {
                "craft":    "Norcino · Cinta Senese salami",
                "name":     "Davide Pieri",
                "place":    "Castelfiorentino · 22 km from the podere",
                "since":    "Family norcineria since 1958",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "Maria's father taught me how to butcher a pig the right "
                    "way back in 1972. Now that Maria raises the podere's "
                    "Cinta Senese, I am the one who turns them into salami.",
            },
            {
                "craft":    "Monastery · quince jam",
                "name":     "Suore di San Vivaldo",
                "place":    "Montaione · 18 km from the podere",
                "since":    "Monastery active since the 15th century",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "The sisters of the monastery make quince jam the way it "
                    "was made in the fifteenth century · five hours of slow "
                    "cooking over a low flame. Maria serves it with the "
                    "pecorino.",
            },
        ],

        # Provenance items — list[4] of dict[4 keys=icon,title,desc,place]
        "provenance_label":   "The podere",
        "provenance_heading": "Thirteen hectares, four productions.",
        "provenance_intro":
            "The podere covers thirteen hectares farmed directly by the "
            "Pasquinelli family. Four historic productions · olive grove, "
            "vineyard, garden, stable · are still managed at the rhythm Maria "
            "learned from her father. The full circle of farm hospitality "
            "starts here, in the fields.",
        "provenance_items": [
            {
                "icon":  "🌿",
                "title": "Historic olive grove",
                "desc": "2,400 trees of Moraiolo, Frantoio and Leccino · some plants over 200 years old · hand-picked in November · cold-pressed within 8 hours.",
                "place": "8 hectares on the south-east slope of the podere",
            },
            {
                "icon":  "🍇",
                "title": "Sangiovese vineyard",
                "desc": "1.8 hectares of Sangiovese (95%) with small shares of Canaiolo and Colorino · hand vintage in late September · vinified in the family cellar · bottled by May.",
                "place": "1.8 hectares on the west slope · 380 m elevation",
            },
            {
                "icon":  "🥕",
                "title": "Kitchen garden",
                "desc": "1 hectare of seasonal garden · San Marzano tomatoes, zolfini beans, saffron, kitchen herbs · nothing bought in for Maria's table apart from winter lemons.",
                "place": "1 hectare next to the farmhouse",
            },
            {
                "icon":  "🐖",
                "title": "Cinta Senese stable",
                "desc": "8 head of Cinta Senese (black pig) raised semi-wild · fed on acorns from the podere's woodland and farro from the garden · local slaughter twice a year.",
                "place": "2.2 hectares of woodland with covered stable",
            },
        ],

        # Care items — list[4] of tuple[2] · the four ospitalità promises
        "care_label":   "The four promises of the house",
        "care_heading": "Farm hospitality: a few rules, always kept.",
        "care_items": [
            ("Shared table always with Maria",
             "Every dinner is cooked and brought to the table by Maria. When "
             "she sits down with you, it is because the serving is done — not "
             "to entertain you."),
            ("No automated check-in",
             "Carlo or Giovanni meet you at the gate and walk you to your "
             "room. The key is a real iron key, with the name of the room. "
             "No keycards."),
            ("Breakfast until 10:30",
             "Warm bread from the podere's oven · jams from the sisters of "
             "San Vivaldo · honey from our hives · eggs from the hens · "
             "coffee from the podere's historic blend."),
            ("Home shipping after your stay",
             "When you leave, the dispensa packs you a wooden case of six "
             "products from the podere of your choice. We ship home within "
             "a week · only the shipping cost is added."),
        ],

        # Press strip — list[5] of scalar str (NOT dicts per contract)
        "press_label":   "Press on the podere",
        "press_items": [
            "Slow Food Florence",
            "Bell'Italia · rural Tuscany",
            "Touring Club Italiano",
            "Gambero Rosso · Agriturismi 2025",
            "Vie del Gusto · Chianti Classico",
        ],

        # Journal teaser
        "journal_teaser_label":   "From the field journal · farm hospitality, week by week",
        "journal_teaser_heading": "Three voices from Greve in Chianti.",
        "journal_teaser_link":    "Read the journal",
        "journal_teaser_href":    "diario",

        # Final CTA
        "cta_label":          "To reserve the shared table",
        "cta_heading":        "<em>Four guest rooms</em>, one shared table, one family.",
        "cta_intro":
            "The four guest rooms of the podere are booked directly with Maria "
            "via WhatsApp or telephone. The shared dinner table is reserved on "
            "arrival · we cook for as many as you are.",
        "cta_primary":        "Message Maria on WhatsApp",
        "cta_primary_href":   "soggiorno",
        "cta_secondary":      "Direct line to the kitchen",
    },

    # ─── DISPENSA (shop · 8 farm products) ─────────────────────
    "dispensa": {
        "eyebrow":             "The farm dispensa",
        "headline":            "Eight farm-direct products · home shipping Italy 24-48h.",
        "intro":
            "The dispensa is the natural extension of Maria's kitchen and "
            "of our farm hospitality: the products you eat at the table when "
            "you are our guests, you find them here to take home. Refrigerated "
            "shipping in summer, wooden case stamped with the podere's mark.",
        "filter_section_label": "Refine the dispensa",
        "filter_groups": [
            {
                "label":   "Production",
                "options": ["Extra virgin olive oil", "Wine", "Preserves", "Cured meats", "Pasta · bread · sweets"],
            },
            {
                "label":   "Season",
                "options": ["2025 harvest", "2022-2024 vintage", "July extraction", "Long curing", "Always available"],
            },
            {
                "label":   "Wooden case",
                "options": ["Case of 6 products · free choice", "Olive oil + wine case", "Breakfast case (honey + jam + cantucci)", "Cured meat case"],
            },
        ],
        "sort_label":      "Sort by",
        "sort_options": [
            "By production",
            "By season",
            "By curing",
            "By availability",
        ],
        "result_count":    "8 farm-direct products in the dispensa",
        "result_subtitle": "Six under the podere's mark + two from producers of the territory · home shipping Italy 24-48h.",
        "featured_product_id": "olio-evo-podere-2025",

        # 8 products — full dict shape (11 keys per contract)
        "products": [
            {
                "id":         "olio-evo-podere-2025",
                "n":          "No. 01",
                "image":      _OLIO_BOTTLE,
                "edition":    "2025 harvest",
                "name":       "Podere extra virgin olive oil",
                "meta":       "Moraiolo 60% + Frantoio 25% + Leccino 15% · cold-pressed within 8 hours of picking",
                "place":      "Greve in Chianti",
                "artisan":    "Maria + Carlo Pasquinelli",
                "price":      "€ 28 / 500 ml",
                "tag":        "November harvest",
                "available":  True,
            },
            {
                "id":         "chianti-classico-2022",
                "n":          "No. 02",
                "image":      _VINO_BOTTLE,
                "edition":    "2022 vintage",
                "name":       "Chianti Classico DOCG",
                "meta":       "Sangiovese 95% · Canaiolo 4% · Colorino 1% · large cask + 6 months in bottle",
                "place":      "Podere vineyard · 1.8 ha · 380 m elevation",
                "artisan":    "Giovanni Pasquinelli · podere winemaker",
                "price":      "€ 22 / 750 ml",
                "tag":        "Podere cellar",
                "available":  True,
            },
            {
                "id":         "vin-santo-2018",
                "n":          "No. 03",
                "image":      _VINSANTO,
                "edition":    "2018 vintage · 7-year ageing",
                "name":       "Vin Santo del Chianti",
                "meta":       "Malvasia bianca + Trebbiano · 4-month drying · 50-litre oak caratelli",
                "place":      "Podere attic · historic caratelli",
                "artisan":    "Carlo Pasquinelli · cellarman",
                "price":      "€ 32 / 375 ml",
                "tag":        "Half bottle",
                "available":  True,
            },
            {
                "id":         "miele-millefiori",
                "n":          "No. 04",
                "image":      _MIELE,
                "edition":    "July 2025 extraction",
                "name":       "Wildflower honey",
                "meta":       "12 hives in a chestnut clearing · July harvest · no chemical treatment · no winter feeding",
                "place":      "Podere woodland",
                "artisan":    "Anna Pasquinelli · beekeeper",
                "price":      "€ 14 / 250 g",
                "tag":        "One hundred percent podere",
                "available":  True,
            },
            {
                "id":         "marmellata-susine",
                "n":          "No. 05",
                "image":      _MARMELLATA,
                "edition":    "August 2025 batch",
                "name":       "Plum jam",
                "meta":       "Yellow claudia plums · 38% sugar · no added pectin · 4-hour slow cooking",
                "place":      "Podere garden · 3 historic trees",
                "artisan":    "Maria Pasquinelli · kitchen",
                "price":      "€ 9 / 280 g",
                "tag":        "Small batch",
                "available":  True,
            },
            {
                "id":         "pecorino-toscano-dop",
                "n":          "No. 06",
                "image":      _PECORINO,
                "edition":    "6-month curing",
                "name":       "Pecorino Toscano DOP",
                "meta":       "Raw sheep's milk · natural rennet · cave-aged · brushed with podere extra virgin olive oil",
                "place":      "Lamole · 4 km from the podere",
                "artisan":    "Andrea Falleri · shepherd",
                "price":      "€ 24 / small wheel 600 g",
                "tag":        "Hands of Andrea",
                "available":  True,
            },
            {
                "id":         "salame-cinta-senese",
                "n":          "No. 07",
                "image":      _SALAME,
                "edition":    "9-month curing",
                "name":       "Cinta Senese salami",
                "meta":       "Cinta Senese pigs from the podere · semi-wild rearing · local slaughter · cured in a stone cellar",
                "place":      "Podere stable + Pieri norcineria, Castelfiorentino",
                "artisan":    "Davide Pieri · norcino",
                "price":      "€ 38 / whole piece 700 g",
                "tag":        "8 head in the stable",
                "available":  True,
            },
            {
                "id":         "cantucci-mandorle",
                "n":          "No. 08",
                "image":      _CANTUCCI,
                "edition":    "Weekly bake",
                "name":       "Almond cantucci",
                "meta":       "Unpeeled almonds · podere eggs · cane sugar · Annetta's 1948 recipe",
                "place":      "Podere oven · Maria's kitchen",
                "artisan":    "Maria Pasquinelli · kitchen",
                "price":      "€ 12 / 250 g bag",
                "tag":        "Annetta's recipe",
                "available":  True,
            },
        ],

        "footer_note_label": "Shipping and the wooden case",
        "footer_note":
            "Every product ships in a wooden case stamped with the podere's "
            "mark · orders over € 80 ship free within Italy · otherwise a flat "
            "€ 12. The case can come back to us at your discretion · or stay "
            "with you as a kitchen object.",
    },

    # ─── PRODOTTO (product page · featured = Olio EVO 2025) ───
    "prodotto": {
        "id":           "olio-evo-podere-2025",
        "n":            "No. 01",
        "edition":      "November 2025 harvest",
        "edition_note": "2025 vintage limited to 1,800 bottles · lot 23/01",
        "name":         "Podere extra virgin olive oil",
        "subtitle":     "Moraiolo + Frantoio + Leccino · cold-pressed within 8 hours",
        "price":        "€ 28 / 500 ml bottle",
        "vat_note":     "VAT included · shipping 24-48h within Italy",
        "intro":
            "The oil of Podere Le Querce is the house's historic product · the "
            "Pasquinelli family has always sold its own extra virgin olive oil "
            "directly, ever since great-grandparents Mario and Annetta. The "
            "2025 harvest was hand-picked by about ten people (the family plus "
            "four seasonal pickers) between the 6th and the 19th of November · "
            "cold-pressed within eight hours.",

        # Gallery — list of scalar URL strings
        "gallery": [
            _OLIO_BOTTLE,
            _OLIVETO,
            _CUCINA_CONTADINA,
        ],

        "info_label": "Technical sheet",
        # info_rows — list[10] of tuple[2]
        "info_rows": [
            ("Cultivar",        "Moraiolo 60% · Frantoio 25% · Leccino 15%"),
            ("Harvest",         "By hand · 6-19 November 2025"),
            ("Pressing",        "Cold · within 8 hours · 27 °C maximum"),
            ("Acidity",         "0.18% · below the excellence threshold"),
            ("Polyphenols",     "412 mg/kg · high value"),
            ("Bottle",          "Dark glass 500 ml · metal screw cap"),
            ("Lot",             "23/01 of 36 · label numbered by hand"),
            ("Storage",         "Cool place · away from light · within 18 months"),
            ("Awards",          "Slow Food Presidio · Gambero Rosso 2 leaves 2025"),
            ("Availability",    "1,800 bottles · available while stocks last"),
        ],

        "size_label":      "Available formats",
        "size_intro":      "Single 500 ml bottle, case of 6 bottles with a 12% discount, or a 3-litre tin for those who cook often.",
        # size_options — list[4] of SCALAR strings (per contract · NOT tuples)
        "size_options": [
            "500 ml bottle",
            "Case of 6 bottles · 500 ml",
            "3-litre tin",
            "Gift sleeve · 2 bottles + cantucci",
        ],
        "size_chart_link":   "All formats in the dispensa",
        "size_chart_href":   "dispensa",

        "artisan_label":     "Hands of",
        "artisan_name":      "Maria + Carlo Pasquinelli",
        "artisan_role":      "Fourth generation · at the podere since 1985",
        "artisan_bio":
            "Maria Pasquinelli (born 1962) and Carlo Pasquinelli (born 1960) "
            "took the reins of the podere in 1985 after the death of Maria's "
            "father Mario. Since then they have tended the olive grove as a "
            "pair · Carlo leads the hand harvest, Maria oversees the pressing "
            "at the Chianti cooperative mill. The family has never used "
            "pesticides in the olive grove.",
        "artisan_portrait":  _PORTRAIT_MARIA,

        "buy_primary":       "Add to case",
        "buy_secondary":     "Message Maria on WhatsApp",
        "buy_note":
            "For orders over 12 bottles, write directly to the family · we "
            "will pack a special case and calculate the discount. Cash on "
            "delivery within Italy, bank transfer for Europe.",

        "care_label":  "Storage and use",
        "care_intro":
            "The podere's oil is an oil to be used raw · on warm bread, "
            "beans, ribollita, bruschetta. Not recommended for frying.",
        # care_items — list[5] of tuple[2]
        "care_items": [
            ("Temperature",   "Keep at 14-18 °C · not in the fridge · not in a hot kitchen"),
            ("Light",         "Dark glass bottle · still keep away from direct light"),
            ("After opening", "Once opened · finish within 4 months · flavour fades after that"),
            ("Flavour",       "Green, bitter and peppery in balance · medium-intense fruit"),
            ("Pairing",       "Zolfini beans · unsalted bread · ribollita · Tuscan bruschetta"),
        ],

        "provenance_label":   "From the olive grove to the bottle",
        "provenance_heading": "Four steps, all by hand.",
        # provenance_steps — list[4] of 3-TUPLE (n, t, p) per contract
        "provenance_steps": [
            ("01", "Hand harvest",          "6 to 19 November 2025 · 10 pickers · 6 weeks of hand harvest · perforated plastic crates"),
            ("02", "Transport to the mill", "Same day · within 8 hours · 12 km to the Chianti cooperative mill"),
            ("03", "Cold pressing",         "27 °C maximum · mechanical extraction · no added water · no heat"),
            ("04", "Bottling",              "March 2026 · at the podere · dark glass 500 ml bottle · lot numbered by hand"),
        ],

        "related_label": "Other products from the podere",
        "related_intro": "The products of the same season that complete the case.",
        # related_items — list[4] of dict[5 keys=image,n,name,meta,price]
        "related_items": [
            {
                "id":    "chianti-classico-2022",
                "n":     "No. 02",
                "image": _VINO_BOTTLE,
                "name":  "Chianti Classico DOCG · 2022",
                "meta":  "Wine from the same historic vintage · perfect with the oil case",
                "price": "€ 22",
            },
            {
                "id":    "miele-millefiori",
                "n":     "No. 04",
                "image": _MIELE,
                "name":  "Wildflower honey",
                "meta":  "12 hives · chestnut clearing · July extraction",
                "price": "€ 14",
            },
            {
                "id":    "marmellata-susine",
                "n":     "No. 05",
                "image": _MARMELLATA,
                "name":  "Plum jam",
                "meta":  "Claudia plums · August batch · 4-hour slow cooking",
                "price": "€ 9",
            },
            {
                "id":    "cantucci-mandorle",
                "n":     "No. 08",
                "image": _CANTUCCI,
                "name":  "Almond cantucci",
                "meta":  "Annetta's recipe · podere's weekly bake",
                "price": "€ 12",
            },
        ],
    },

    # ─── FAMIGLIA (about · The Pasquinelli family) ────────────
    "famiglia": {
        "eyebrow":  "The Pasquinelli family",
        "headline": "Four generations at Le Querce · farm hospitality, all year.",
        "intro":
            "Podere Le Querce has been home to the Pasquinelli family since "
            "November 1934. Great-grandparents Mario and Annetta bought it "
            "from the Antinori family with a deed of sale still kept at the "
            "town hall. Four generations have lived at the podere since · "
            "today Maria and Carlo are at the helm with their children "
            "Giovanni and Anna.",

        "mission_label":   "Our mission",
        "mission_heading": "Farm hospitality the way you picture it.",
        "mission_text":
            "We cook for our guests the same food we cook for ourselves · no "
            "restaurant menu, no cheese trolley, no sommelier. There is Maria "
            "bringing the ribollita she made this morning to the table, "
            "Giovanni opening the wine he bottled in the spring, Anna "
            "slicing the bread she baked at dawn. Farm hospitality, in one "
            "long lunch.",

        "process_label":   "The family calendar",
        "process_heading": "Four seasons, four rhythms of the podere.",
        # process_steps — list[4] of DICT[5 keys=n,title,place,desc,duration]
        # CANONICAL shape (NOT Sapori's broken {num/title/desc})
        "process_steps": [
            {
                "n":        "01",
                "title":    "Spring · grafting and blossom",
                "place":    "Olive grove + vineyard + garden",
                "desc":
                    "March to May · grafting of the vines, pruning of the "
                    "olive grove, sowing of the kitchen garden · the four "
                    "guest rooms reopen after the January technical closure. "
                    "Easter shared table with Zeri lamb.",
                "duration": "Three months · March-May",
            },
            {
                "n":        "02",
                "title":    "Summer · harvest and full hospitality",
                "place":    "The whole podere",
                "desc":
                    "June to August · peak hospitality season · daily shared "
                    "tables of 12-16 guests · honey harvest · wheat harvest · "
                    "summer preserves harvest (tomatoes, plums, blackberries, "
                    "figs).",
                "duration": "Three months · June-August",
            },
            {
                "n":        "03",
                "title":    "September · grape harvest",
                "place":    "Vineyard + cellar",
                "desc":
                    "September · hand grape harvest of Sangiovese · "
                    "eighteen days of continuous work in the vineyard · "
                    "the cellar is closed to the public for the two "
                    "vinification weeks · closing shared table with the "
                    "whole family and the harvest crew.",
                "duration": "One month · September",
            },
            {
                "n":        "04",
                "title":    "Autumn-winter · olive oil and pork",
                "place":    "Olive grove + stable + kitchen",
                "desc":
                    "November · olive harvest (six weeks) · December "
                    "slaughter of the Cinta Senese · January salami "
                    "production with the norcino Pieri · February "
                    "technical closure of the podere · March reopening.",
                "duration": "Five months · November-March",
            },
        ],

        "founder_label":    "The matriarch",
        "founder_heading":  "Maria Pasquinelli · at the podere since 1985.",
        "founder_text":
            "Maria Pasquinelli (born 1962) is the third generation at the "
            "podere · daughter of Giovanni and Maddalena Pasquinelli, "
            "granddaughter of great-grandparents Mario and Annetta who bought "
            "the podere from the Antinoris. She took over the business in "
            "1985 after the death of her father · married to Carlo (from a "
            "neighbouring podere) since 1987 · two children Giovanni (1990) "
            "and Anna (1993) who have worked the podere full time since "
            "2015. In the kitchen from seven in the morning, at the evening "
            "shared table with the guests.",
        "founder_portrait":  _PORTRAIT_MARIA,
        "founder_caption":   "Maria Pasquinelli at the Sunday shared table · photograph by Paolo Codeluppi · summer 2024",

        "numbers_label": "The podere in figures",
        # numbers_items — list[4] of tuple[2]
        "numbers_items": [
            ("92",  "Years of the Pasquinelli family at the podere · since 1934"),
            ("13",  "Hectares farmed directly · olive grove + vineyard + garden + woodland"),
            ("4",   "Guest rooms of farm hospitality · the whole family in the kitchen"),
            ("8",   "Products in the dispensa · six under the podere's mark + two from producers of the territory"),
        ],

        "visit_label":          "To visit the podere",
        "visit_heading":        "Shared table by reservation · or guided visit.",
        "visit_text":
            "Guided visits of the podere by reservation · Tuesday and "
            "Thursday afternoons (4 pm) for non-resident guests. Evening "
            "shared table (12-16 people) by reservation at least 48 hours "
            "ahead. The four guest rooms are booked directly with Maria.",
        "visit_primary":         "Reserve the shared table",
        "visit_primary_href":    "soggiorno",
        "visit_secondary":       "Direct WhatsApp to Maria",
    },

    # ─── DIARIO (journal · 3 entries) ─────────────────────────
    "diario": {
        "eyebrow":     "Field journal",
        "headline":    "Three voices from Greve in Chianti.",
        "intro":
            "The podere journal gathers the voices of the family · Maria "
            "writes once a month, from January 2018 · Giovanni and Anna add "
            "seasonal notes. Working notes from the inside of farm "
            "hospitality · not tourist stories.",
        "list_label":  "Three recent notes",
        # entries — list[3] of dict[5 keys=n,title,place,excerpt,minutes]
        "entries": [
            {
                "n":       "001",
                "title":   "Vintage 2025 · the day of the rain",
                "place":   "Vineyard · 14 September 2025",
                "excerpt":
                    "The rain came in the afternoon of the tenth day · we "
                    "worked through it anyway · only three rows left to "
                    "finish. Giovanni brought the big vat under the "
                    "pergola · Maria opened the kitchen · by ten in the "
                    "evening we were all inside with the black-cabbage "
                    "soup.",
                "minutes": "4 minute read",
            },
            {
                "n":       "002",
                "title":   "Olive harvest 2025 · the oldest trees",
                "place":   "Olive grove · 12 November 2025",
                "excerpt":
                    "The trees over two hundred years old gave much less this "
                    "year · the August heat took its toll. Carlo says that "
                    "plant number 47 (the oldest, over 350 years old "
                    "according to the 1923 ledger) gave only 4 kg this year "
                    "against 28 last year. We will keep tending to it.",
                "minutes": "3 minute read",
            },
            {
                "n":       "003",
                "title":   "Anna starts beekeeping · the first three hives",
                "place":   "Podere woodland · 22 April 2025",
                "excerpt":
                    "Anna brought home the first three hives from the "
                    "beekeeping course in Vinci. She set them in the "
                    "podere's woodland, where there is a chestnut clearing. "
                    "Maria says her father kept bees until 1972 · then no "
                    "one. Let's see if they make it through the winter.",
                "minutes": "5 minute read",
            },
        ],
        "footer_note_label": "To receive the journal",
        "footer_note":
            "The journal has no automated newsletter · if you would like to "
            "receive it, write to Maria. We send a printed copy at the end "
            "of the year to the guests who ask for one.",
    },

    # ─── SOGGIORNO (contact · book the shared table) ──────────
    "soggiorno": {
        "eyebrow":  "Stay with us · direct booking",
        "headline": "Four guest rooms, one shared table.",
        "intro":
            "The four guest rooms of the podere are booked directly with the "
            "Pasquinelli family · no third-party platform, no intermediary "
            "commission. Write to Maria · she replies personally within the "
            "day, usually between the breaks in the kitchen. Farm hospitality "
            "as it should be.",

        "form_section_label":   "Request a stay",
        "form_section_intro":
            "Tell us the dates you have in mind, the number of guests and any "
            "special request · allergies, intolerances, children, animals. "
            "Maria writes back from the kitchen within 24 hours.",
        "form_helper_required": "Fields marked with · are required",
        "form_submit_button":   "Send to Maria",
        "form_submit_note":
            "Final confirmation with a 30% deposit by bank transfer · balance "
            "on arrival at the reception of the podere.",

        # form_fields — list[~7] of dict[5 keys=label,name,type,required,placeholder]
        "form_fields": [
            {
                "label":       "Full name",
                "name":        "name",
                "type":        "text",
                "required":    True,
                "placeholder": "How you introduce yourself · Maria will call you by name",
            },
            {
                "label":       "Direct email",
                "name":        "email",
                "type":        "email",
                "required":    True,
                "placeholder": "Maria writes from famiglia@podereleQuerce.it",
            },
            {
                "label":       "WhatsApp · or telephone",
                "name":        "phone",
                "type":        "tel",
                "required":    False,
                "placeholder": "+39 339 458 1126 · Maria also replies on WhatsApp",
            },
            {
                "label":       "Arrival date",
                "name":        "arrival",
                "type":        "date",
                "required":    True,
                "placeholder": "",
            },
            {
                "label":       "Departure date",
                "name":        "departure",
                "type":        "date",
                "required":    True,
                "placeholder": "",
            },
            {
                "label":       "Number of guests",
                "name":        "guests",
                "type":        "number",
                "required":    True,
                "placeholder": "Adults + children",
            },
            {
                "label":       "Allergies, intolerances, animals",
                "name":        "notes",
                "type":        "textarea",
                "required":    False,
                "placeholder": "Maria adapts the kitchen · tell us here",
                "rows":        5,
            },
        ],

        # Contact card
        "card_label":            "For quick replies",
        "card_address_label":    "Where we are",
        "card_address_value":    "Località Le Querce 14 · 50022 Greve in Chianti · Florence",
        "card_phone_label":      "Kitchen · Maria",
        "card_phone_value":      "+39 055 853 261",
        "card_whatsapp_label":   "Direct WhatsApp",
        "card_whatsapp_value":   "+39 339 458 1126 · Maria",
        "card_email_label":      "Email",
        "card_email_value":      "famiglia@podereleQuerce.it",
        "card_hours_label":      "Hours",
        # card_hours_rows — list of SCALAR strings (per contract · NOT tuples)
        "card_hours_rows": [
            "Kitchen open all year · lunch 12:30 · dinner 19:30",
            "Guest reception 8-22 · Maria in the kitchen from 7",
            "Dispensa 9-19 · closed Sunday (Greve market day)",
            "Technical closure · 1-28 February",
        ],
        "card_directions_label": "How to get here",
        "card_directions_text":
            "From Florence 28 km · exit A1 motorway at Firenze Sud · follow "
            "the Chiantigiana · 12 km past Greve in Chianti turn right "
            "towards Lamole · 1.4 km from the junction. Wooden gate with "
            "the handwritten sign \"Podere Le Querce\" · ring the bell.",

        "faq_label": "Questions from the kitchen",
        # faq_items — list[5] of DICT[2 keys=q,a]
        # CANONICAL shape (NOT Sapori's broken 2-tuples)
        "faq_items": [
            {
                "q": "Do we pay for the shared table if we are also staying in a room?",
                "a":
                    "Yes · the kitchen and the hospitality are two separate "
                    "things · the rooms are paid for the overnight stay, the "
                    "shared table is paid separately · € 35 per person for "
                    "dinner, € 28 for lunch (podere wine included). Breakfast "
                    "is included in the room rate.",
            },
            {
                "q": "Are children and animals welcome?",
                "a":
                    "Children are very welcome · we have cots for the little "
                    "ones, high chairs for the bigger ones · Anna often "
                    "takes them to the stable to see the Cinta Senese pigs. "
                    "Small dogs are allowed in the downstairs rooms (€ 15 "
                    "per night supplement) · larger dogs in the courtyard "
                    "and woodland, but not in the rooms or in the kitchen.",
            },
            {
                "q": "Can we visit the podere without staying overnight?",
                "a":
                    "Yes · Tuesday and Thursday afternoons (4 pm, 90 minutes, "
                    "by reservation at least 24 hours ahead) Carlo takes "
                    "visitors through the olive grove and the cellar · € 20 "
                    "per person · tasting of olive oil + wine + honey "
                    "included. Without a reservation, the dispensa is still "
                    "open daily 9-19.",
            },
            {
                "q": "Can we book the whole podere for weddings or events?",
                "a":
                    "Yes, for intimate weddings · up to 36 guests · civil "
                    "ceremony in the garden under the wisteria pergola · "
                    "shared table under the restored hayloft · write to "
                    "Maria at least eight months before the date. We do not "
                    "organise weddings with more than 36 guests or corporate "
                    "events.",
            },
            {
                "q": "Can we buy the products without coming to the podere?",
                "a":
                    "Yes · the dispensa ships throughout Italy (24-48 hours, "
                    "free shipping over € 80) and across Europe (4-6 days). "
                    "Wooden case stamped with the podere's mark · can come "
                    "back at your discretion · for orders over 12 bottles "
                    "write directly to Maria for a discount. Farm "
                    "hospitality at a distance.",
            },
        ],
    },
}
