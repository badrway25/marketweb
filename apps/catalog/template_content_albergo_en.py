"""Albergo Borgo — Relais hospitality in a Tuscan UNESCO village (EN voice).

T57 · Wave 2 Pass-2 (2026-05-12) · EN native-voice tree mirroring the IT
recursive shape (225 leaf paths · zero missing · zero extra).

Voice contract (EN):
- Condé Nast Traveler / Travel + Leisure / Departures / Monocle Travel
  editorial register. Warm but knowledgeable. Second-person plural where
  IT uses `voi`; second-person formal `you` otherwise.
- Voice anchor `ospitalità di borgo` → `village hospitality`. Preserved
  verbatim across every band (home headline, borgo statement_heading,
  soggiorno headline, contatti faq) — load-bearing.
- Italian proper names preserved verbatim: Borgo San Marco · Relais & Spa,
  Vittoria Sernigi, Federico Bonechi, Tommaso Brigliadori, Anna Ricci,
  Caterina Sandri. Suite names stay Italian: La Vigna, Il Frantoio,
  Il Pozzo, La Cisterna, La Torre, Il Cortile, La Loggia, La Cantina.
- Places preserved: Pienza · Val d'Orcia · Siena · Toscana · Florence
  (always Florence, not Firenze in EN) · Borgo San Marco di Sopra ·
  Montalcino · Montepulciano · Bagno Vignoni · San Quirico d'Orcia.
- Wines stay literal: Brunello · Vino Nobile · Chianti Classico ·
  Sangiovese · Champagne. DOCG/DOC stay Italian.
- Professional registers: Relais & Châteaux · Touring Club Italiano ·
  Michelin · AIS · maître. `Borgo` kept as a loanword in editorial EN
  (CNT/Monocle usage). `Relais` kept as a loanword.
- Latin digits throughout (8, 14, 1, 12, 41) · Italian phone format
  preserved verbatim (+39 0578 748 124) · Euro prices European notation.
- Differentiation vs Villa Prestige: hospitality voice (overnight stay,
  spa, restaurant, brigade, cellar open to guests) · CTAs `Reserve your
  stay` + `Write to the management`. Direttrice with a name attached.
"""
from __future__ import annotations

from typing import Any


# Imagery — Unsplash CC0 travel-boutique-hotel pool (interim until X.5
# curator pack lands · 6 hero/feature URLs reused inline below).
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


ALBERGO_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "The borgo",     "kind": "home"},
        {"slug": "camere",     "label": "The suites",    "kind": "blog_list"},
        {"slug": "borgo",      "label": "The territory", "kind": "about"},
        {"slug": "brigata",    "label": "The brigade",   "kind": "team"},
        {"slug": "soggiorno",  "label": "The stay",      "kind": "services"},
        {"slug": "concierge",  "label": "Concierge",     "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":   "B",
        "logo_word":      "Borgo San Marco",
        "logo_subline":   "Relais & Spa · Pienza since 1612",
        "tag":            "2026 season · reservations open May through October",
        "phone":          "+39 0578 748 124",
        "phone_label":    "Direct concierge line",
        "email":          "concierge@borgosanmarco.it",
        "email_label":    "Write to the management",
        "address":        "Borgo San Marco di Sopra · 53026 Pienza · Siena",
        "hours_compact":  "24-hour reception · check-in from 2 p.m. · check-out by 11 a.m.",
        "hours_footer_rows": [
            "Reception open 24 hours · concierge on the floor",
            "Languages on the floor: italiano · english · français · deutsch",
        ],
        "license":        "CITRA code 0521-053026-100201 · Cat. Five Stars Luxury · Confindustria Alberghi register 0428",
        "footer_intro":
            "Borgo San Marco is a relais of eight suites carved from the 17th-century parsonage "
            "of the village it takes its name from — a hillside hamlet of Pienza overlooking the "
            "UNESCO Val d'Orcia. Restoration by Studio Castellini-Mancini in 2009, affiliated "
            "with Relais & Châteaux since 2014, one Michelin star for the Trebbio restaurant "
            "since 2019. Village hospitality is our promise: a single reception for eight rooms, "
            "a floor brigade of fourteen, and the stillness of a borgo that is still inhabited. "
            "Not a resort, not a chain, not a country hotel — village hospitality, kept honest.",

        # Nav reservation CTA (hospitality)
        "nav_cta":         "Reserve your stay",
        "nav_cta_kind":    "appointment",
        "nav_cta_short":   "Reserve",

        # Footer labels
        "foot_studio":   "The relais",
        "foot_pages":    "Sitemap",
        "foot_contact":  "Concierge",
        "foot_offices":  "Addresses",
        "offices_footer_rows": [
            "Borgo San Marco di Sopra · 53026 Pienza · Siena",
            "Tenuta Trebbio · cellar and olive grove · 1.2 km to the south",
        ],
        "office_rows": [
            "Borgo San Marco di Sopra 17 · 53026 Pienza · Siena",
            "Tel +39 0578 748 124 · concierge@borgosanmarco.it",
        ],
        "dossier_label":     "Suite",
        "portfolio_label":   "Overnight stays / year",
        "territorio_label":  "Borgo",
        "superficie_label":  "Surface",
        "provenance_label":  "View",
        "access_label":      "Languages on the floor",
        "availability_label": "Seasonality",
        "price_note":        "Rate on application · seasonal packages",
        "nda_required_label": "Confidential",
        "viewing_on_request": "By reservation only",
        "referent_label":    "Floor referent",
        "concierge_line_label": "Dedicated concierge",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "cover_location":    "Borgo San Marco di Sopra · Val d'Orcia · UNESCO",
        "cover_image_credit": "Photograph · Massimo Listri",
        "cover_image":       _HERO_COURTYARD,

        "eyebrow":           "Relais & Spa · Val d'Orcia · Pienza since 1612",
        "headline":          'Eight suites in a 17th-century Tuscan borgo. <em>Village hospitality</em>, one season a year.',
        "sub":
            "A relais of eight suites carved from the 17th-century parsonage of Borgo "
            "San Marco di Sopra, a hillside hamlet of Pienza overlooking the Val d'Orcia. "
            "Seasonal opening from May through late October · single reception · Michelin-starred "
            "kitchen · Aqua di Borgo spa set inside the 18th-century cistern · estate cellar.",
        "hero_wordmark":     "Borgo San Marco",
        "hero_location":     "Pienza · Siena · Toscana",
        "hero_counter_label": "Suites",
        "hero_counter_value": "8",
        "hero_series_label": "Season",
        "hero_series_title": "2026 · April – October",
        "hero_series_note":  "Opening April 18 · closing October 27 · floor brigade of fourteen",

        "primary_cta":         "Reserve your stay",
        "primary_cta_href":    "concierge",
        "secondary_cta":       "Discover the suites",
        "secondary_cta_href":  "camere",

        # Hero credit cells — list[4] of tuple[2] (label, value)
        "hero_credit_cells": [
            ("Affiliation",   "Relais & Châteaux"),
            ("Kitchen",       "One Michelin star"),
            ("Restoration",   "Castellini-Mancini · 2009"),
            ("Opening",       "Seasonal · 24 weeks"),
        ],

        # Signature suite section — list[6] of dict (keys: slug, image,
        # index, title, territorio, superficie, provenance, availability)
        "signature_label":    "The suites",
        "signature_heading":  "The suites of the house — one for every room of the borgo.",
        "signature_intro":
            "Eight suites, each one carved from a historic room of the parsonage and the "
            "adjoining 18th-century cellar. No two rooms are alike; every one of them faces "
            "the Val d'Orcia.",
        "signature": [
            {
                "slug":         "suite-la-vigna",
                "image":        _SUITE_VIGNA,
                "index":        "Suite 01",
                "title":        "La Vigna",
                "territorio":   "West wing · first floor",
                "superficie":   "62 m² · king double",
                "provenance":   "Looking out over the historic Sangiovese vineyard",
                "availability": "Available May – September",
            },
            {
                "slug":         "suite-il-frantoio",
                "image":        _SUITE_FRANTOIO,
                "index":        "Suite 02",
                "title":        "Il Frantoio",
                "territorio":   "Ground floor · south wing",
                "superficie":   "78 m² · double with sitting room",
                "provenance":   "The 1620 olive press millstone preserved at the centre of the room",
                "availability": "Available throughout the season",
            },
            {
                "slug":         "suite-il-pozzo",
                "image":        _SUITE_POZZO,
                "index":        "Suite 03",
                "title":        "Il Pozzo",
                "territorio":   "Inner courtyard · ground floor",
                "superficie":   "54 m² · standard double",
                "provenance":   "17th-century octagonal well in the private courtyard",
                "availability": "On request · couples only",
            },
            {
                "slug":         "suite-la-cisterna",
                "image":        _SUITE_CISTERNA,
                "index":        "Suite 04",
                "title":        "La Cisterna",
                "territorio":   "East wing · lower level",
                "superficie":   "88 m² · four-poster bed",
                "provenance":   "Vault of the 18th-century cistern · natural light from above",
                "availability": "On request · honeymoon recommended",
            },
            {
                "slug":         "suite-la-torre",
                "image":        _SUITE_TORRE,
                "index":        "Suite 05",
                "title":        "La Torre",
                "territorio":   "Corner tower · second floor",
                "superficie":   "70 m² · double bed + study",
                "provenance":   "270° view of the Val d'Orcia all the way to Monte Amiata",
                "availability": "Available April – October",
            },
            {
                "slug":         "suite-il-cortile",
                "image":        _SUITE_CORTILE,
                "index":        "Suite 06",
                "title":        "Il Cortile",
                "territorio":   "Ground floor · north wing",
                "superficie":   "65 m² · double + private garden",
                "provenance":   "Private loggia onto the wisteria pergola",
                "availability": "Available May – October",
            },
        ],
        "signature_link_all":  "See all eight suites",
        "signature_link_href": "camere",

        # Territory chip-row — list of scalar strings
        "territory_label": "Territory",
        "territory": [
            "Pienza · Val d'Orcia",
            "Montalcino · cellars of Brunello",
            "Montepulciano · Vino Nobile",
            "San Quirico d'Orcia · historic routes",
            "Bagno Vignoni · medieval thermal piazza",
            "Monte Amiata · hiking trails",
            "Siena · Palio in July and August",
            "Cortona · Etruscan roads",
        ],

        # Director / advisor band — single block
        "advisor_label":     "The direction",
        "advisor_heading":   "A direttrice who works on the floor. <em>Thirty-two seasons of village hospitality</em>.",
        "advisor_intro":
            "Borgo San Marco is directed in person by Vittoria Sernigi, a Tuscan hotelier born "
            "in 1964, trained under Maestro Casiraghi at the Plaza Athénée in Paris and Maestro "
            "Cipriani at the Cipriani in Venice. Thirty-two seasons of luxury hospitality before "
            "taking over the borgo in 2008 to practise the kind of village hospitality Tuscany "
            "rarely keeps within the hotel-chain register.",
        "advisor_name":      "Vittoria Sernigi",
        "advisor_role":      "Direttrice · member of the Touring Club Italiano · AIS sommelier",
        "advisor_bio":
            "Thirty-two years of international hospitality before Pienza: Plaza Athénée Paris · "
            "Cipriani Venice · Villa San Michele Fiesole. Member of the Touring Club Italiano "
            "since 1995, AIS sommelier since 2002, instructor at the Scuola Alberghiera in Siena. "
            "On the floor every morning at breakfast, every evening at key hand-over.",
        "advisor_portrait":  _PORTRAIT_DIRECTOR,
        "advisor_cta":       "Write to Vittoria",
        "advisor_cta_href":  "concierge",

        # Numbers band — list[4] of tuple[2] (counter, label)
        "numbers_label":    "Borgo San Marco in figures",
        "numbers_heading":  "One season, one full reception, one brigade.",
        "numbers": [
            ("8",   "Suites · no two alike"),
            ("14",  "People on the floor brigade"),
            ("1",   "Michelin star · Trebbio restaurant"),
            ("12",  "Years affiliated with Relais & Châteaux"),
        ],
        "numbers_note":
            "Seasonal opening April 18 – October 27 · full floor brigade present across the "
            "12 service shifts · 24-hour reception.",

        # Press band — list of scalar strings (NB: home version, NOT team version)
        "press_label":   "Press",
        "press_intro":   "Borgo San Marco in the editorial travel pages of 2023-2025",
        "press_items": [
            "Condé Nast Traveler Italia",
            "Touring Magazine",
            "Departures",
            "Monocle Travel",
            "Bell'Italia",
        ],

        # Private band — closing CTA
        "private_label":     "For your dearest guests",
        "private_heading":   "The whole borgo, one single family. <em>An eight-day exclusive</em>.",
        "private_intro":
            "The borgo can be reserved exclusively for one family or a small group · eight "
            "suites held back, dedicated brigade, restaurant closed to outside guests, cellar "
            "open to the party. Availability on only three windows a year · write to the "
            "management at least six months ahead.",
        "private_primary":      "Write to the management",
        "private_primary_href": "concierge",
        "private_secondary":    "Discover the borgo",
        "private_secondary_href": "borgo",
    },

    # ─── CAMERE (blog_list of suites) ─────────────────────────
    "camere": {
        "eyebrow":          "Eight suites · Borgo San Marco",
        "headline":         "The suites of the house.",
        "intro":
            "Every suite carries the name of a historic room of the borgo · each one was "
            "reimagined by Studio Castellini-Mancini in 2009, preserving the original "
            "17th-century floor plan.",
        "lead_image":       _HERO_COURTYARD,
        "filter_label":     "Refine your search",
        "filter_groups": [
            {"label": "View",   "options": ["Vineyard", "Courtyard", "Borgo", "Val d'Orcia", "Pergola"]},
            {"label": "Beds",   "options": ["King double", "Double with sitting room", "Four-poster bed", "Suite with study"]},
            {"label": "Season", "options": ["April opening", "Available May – September", "High season only"]},
        ],
        "sort_label":       "Sort by",
        "sort_options": [
            "Surface · largest first",
            "By seasonality",
            "By number of guests",
            "By quietness",
        ],
        "result_count":     "8 suites available for the 2026 season",
        "result_subtitle":  "A single reception for all eight rooms · dedicated floor brigade · village hospitality on every threshold.",
        "footer_note_label": "Rates",
        "footer_note":
            "Every suite includes breakfast in the lounge, unlimited access to the Aqua di "
            "Borgo spa, and a three-wine tasting in the cellar by reservation. Seasonal "
            "rate confirmed at the request stage.",
    },

    # ─── BORGO (about · territorio del relais) ────────────────
    "borgo": {
        "eyebrow":          "Val d'Orcia · UNESCO",
        "headline":         "A 17th-century borgo that is still inhabited.",
        "intro":
            "Borgo San Marco di Sopra is a hillside hamlet of Pienza · 41 resident inhabitants "
            "· central piazza from 1571 · parsonage from 1612 (now the relais) · 18th-century "
            "cellar (now the spa). The borgo has been lived in by the same six families for "
            "four generations; the relais is the most recent arrival, here since 2009.",

        "statement_label":   "Our hospitality",
        "statement_heading": "Eight suites, one brigade, a whole borgo. Village hospitality.",
        "statement_text":
            "Village hospitality means that the reception desk is the same one for all eight "
            "suites, that the floor brigade knows every guest by name from the second day on, "
            "and that the borgo remains a borgo (with its 41 inhabitants) even when you are "
            "our guests. We are not a resort. We are not a chain. We are not a city hotel.",

        "territories_label":   "The surroundings",
        "territories_heading": "Six territories less than an hour from the borgo.",
        "territories_intro":
            "The surroundings of the Val d'Orcia are part of the village hospitality of the relais: "
            "each territory has a floor referent dedicated to discovery · wine, thermal baths, "
            "Etruscan trails, hikes on the Amiata, opera at the Palio di Siena.",
        "territories": [
            {
                "image":      _BORGO_VALDORCIA,
                "name":       "Val d'Orcia",
                "region":     "Pienza · San Quirico · Bagno Vignoni",
                "history":    "UNESCO World Heritage since 2004 · a Renaissance landscape codified by Lorenzetti. Cypress lines, crete and farmsteads.",
                "architects": "Cypress alignments · Etruscan sunken roads",
                "count":      "12 km",
                "since":      "Visit: 1 hour · Federico on the floor as referent",
            },
            {
                "image":      _BORGO_MONTALCINO,
                "name":       "Montalcino",
                "region":     "Historic cellars of Brunello",
                "history":    "Historic cellars of Brunello di Montalcino DOCG · Biondi-Santi, Casanova di Neri, Il Poggione. Private tastings by appointment.",
                "architects": "Medieval parish churches · Sienese castles",
                "count":      "28 km",
                "since":      "Visit: 1 full day · AIS sommelier as referent",
            },
            {
                "image":      _BORGO_PIENZA,
                "name":       "Pienza · the ideal city",
                "region":     "Piazza Pio II · cathedral · Palazzo Piccolomini",
                "history":    "The ideal Renaissance city designed by Bernardo Rossellino for Pio II in 1462. Piazza, cathedral, Palazzo Piccolomini, view of the Amiata.",
                "architects": "Bernardo Rossellino · 1459-1462",
                "count":      "1.8 km",
                "since":      "Visit: 2 hours on foot · concierge accompanies on request",
            },
            {
                "image":      _BORGO_CHIANTI,
                "name":       "Montepulciano",
                "region":     "Vino Nobile · underground cellars",
                "history":    "Underground cellars dug into the tuff stone, some from the 14th century. Tasting of Vino Nobile di Montepulciano DOCG · Avignonesi, Salcheto, Boscarelli.",
                "architects": "Antonio da Sangallo il Vecchio · Vignola",
                "count":      "32 km",
                "since":      "Visit: 1 full day · AIS sommelier as referent",
            },
            {
                "image":      _BORGO_CIPRESSI,
                "name":       "Bagno Vignoni",
                "region":     "15th-century open thermal baths",
                "history":    "A 15th-century thermal piazza-pool, the only one of its kind. Sulphurous water rising from the rock at 49°C, freely accessible. Dinner at the trattoria on the piazza with Caterina the cook.",
                "architects": "Natural basin · 15th century",
                "count":      "8 km",
                "since":      "Visit: 1 half day · Federico on the floor as referent",
            },
            {
                "image":      _BORGO_PIENZA_PIAZZA,
                "name":       "Monte Amiata",
                "region":     "Extinct volcano · beech woods · ski lift",
                "history":    "Extinct volcano (1,738 m). Century-old beech woods, CAI trails, ski lift in winter. November chestnut festival in the borgo of Castiglione d'Orcia.",
                "architects": "CAI trails · 4 marked peaks",
                "count":      "38 km",
                "since":      "Visit: 1 full day · mountain guide by reservation",
            },
        ],
        "territory_card_cta":      "Let us plan together · write to the management",
        "territory_card_cta_href": "concierge",

        "referent_label":   "The floor referent",
        "referent_heading": "A single point of contact for the whole stay.",
        "referent_text":
            "From the moment of arrival, each guest has a single floor referent — maître "
            "Federico Bonechi or sommelier Anna Ricci, depending on the season. The referent "
            "carries the whole reservation: booking the restaurant, scheduling the spa "
            "treatments, arranging cellar tastings, planning outings into the surroundings.",

        "stats_label":  "Borgo San Marco · 2025 figures",
        # list[4] of tuple[2]
        "stats": [
            ("12",  "Years affiliated with Relais & Châteaux"),
            ("162", "Open nights per year"),
            ("8",   "Suites · 2026 season"),
            ("41",  "Resident inhabitants of the borgo"),
        ],
    },

    # ─── BRIGATA (team · staff in sala) ───────────────────────
    "brigata": {
        "eyebrow":       "The brigade · 14 on the floor",
        "headline":      "The same brigade for twelve seasons running.",
        "intro":
            "The Borgo San Marco brigade is fourteen strong, ten of whom return every "
            "season since 2014. Reception, floor, restaurant, spa, cellar · one single "
            "brigade for eight suites.",

        "director_label":       "Direction",
        "director_name":        "Vittoria Sernigi",
        "director_role":        "Direttrice · owner since 2008 · AIS sommelier · TCI",
        "director_text":
            "Vittoria Sernigi took over Borgo San Marco in 2008 after thirty-two seasons "
            "of international hospitality between Paris, Venice and Fiesole. Diploma at "
            "the Scuola Alberghiera Internazionale di Lausanne (1985), advanced studies "
            "in hotel management at Cornell. Member of the Touring Club Italiano since "
            "1995, AIS sommelier since 2002.",
        "director_portrait":    _PORTRAIT_DIRECTOR,
        "director_quote":
            "Village hospitality is the only hospitality I know. It is the slowest, the "
            "most demanding, the most rewarding.",
        "director_quote_attribution": "Vittoria Sernigi · interview with Touring · 2024",

        "advisors_label":   "The floor brigade",
        "advisors_heading": "Four referents, ten seasonal staff · one single floor.",
        "advisors_intro":
            "Four senior referents lead the floor. Service decisions go through their "
            "judgement, never through the algorithm of a chain. Village hospitality, "
            "with four names attached.",
        # list[4] of dict (portrait, name, role, bio, territories, since, langs)
        "advisors": [
            {
                "portrait":    _PORTRAIT_MAITRE,
                "name":        "Federico Bonechi",
                "role":        "Maître · single point of contact for guests",
                "bio":
                    "Maître on the floor since 2009 · ten seasons at Borgo San Marco. "
                    "Trained at the Alberghiero di Chianciano · experience at Castello "
                    "Banfi and Plaza Athénée. He knows every guest by name from the "
                    "second day on.",
                "territories": "Floor · reception · concierge",
                "since":       "In the brigade since 2014",
                "langs":       "Italiano · English · Français",
            },
            {
                "portrait":    _PORTRAIT_CHEF,
                "name":        "Tommaso Brigliadori",
                "role":        "Chef · Trebbio restaurant · one Michelin star",
                "bio":
                    "Chef at the Trebbio restaurant since 2017 · Michelin star awarded "
                    "in 2019. Trained at l'Albereta under Gualtiero Marchesi, refined "
                    "under Bottura in Modena. Cuisine of place: pici, picci e pinoli, "
                    "Zeri lamb, zolfini beans, Pienza caciotta.",
                "territories": "Kitchen · cellar · kitchen garden",
                "since":       "In the brigade since 2017",
                "langs":       "Italiano · English",
            },
            {
                "portrait":    _PORTRAIT_SOMMELIER,
                "name":        "Anna Ricci",
                "role":        "AIS sommelier · cellar manager",
                "bio":
                    "AIS sommelier since 2008 · cellar manager since 2015. The cellar "
                    "holds 4,200 labels across Brunello, Vino Nobile, Chianti Classico, "
                    "and a small Champagne selection. Private cellar tastings for guests, "
                    "twice a week.",
                "territories": "Cellar · tastings · restaurant pairings",
                "since":       "In the brigade since 2015",
                "langs":       "Italiano · English · Deutsch",
            },
            {
                "portrait":    _PORTRAIT_SPA,
                "name":        "Caterina Sandri",
                "role":        "Head of Aqua di Borgo Spa",
                "bio":
                    "Head of the spa since 2018 · diploma in hydrotherapy at the "
                    "Università di Siena, training in spa management at Six Senses "
                    "Toscana. The Aqua di Borgo spa is carved into the 18th-century "
                    "cistern · all treatments by appointment only.",
                "territories": "Aqua di Borgo spa · treatments · underground pool",
                "since":       "In the brigade since 2018",
                "langs":       "Italiano · English",
            },
        ],

        "partners_label":   "The producers of the borgo",
        "partners_heading": "The long-standing suppliers of the table.",
        "partners_intro":
            "The raw ingredients of the Trebbio restaurant come from producers within "
            "a thirty-kilometre radius of the borgo, except for olive oil (estate "
            "production) and bread (the village bakery, 200 metres away).",
        # list[5] of tuple[2] (name, role)
        "partners": [
            ("Fattoria Trebbio",            "Estate EVO oil · historic olive grove 1.2 km from the borgo"),
            ("Caseificio Castelmuzio",      "Pienza pecorino · caciotta · ricotta · 8 km from Pienza"),
            ("Azienda agricola Falcorosso", "Chianina beef · Zeri lamb · poultry · 12 km"),
            ("Forno di Pienza · Lorenzini", "Tuscan bread · schiacciate · grissini · 1.8 km from the borgo"),
            ("Erbario di Sant'Anna",        "Officinal herbs · spa tisanerie · monastery 18 km away"),
        ],

        "press_label":   "Press · brigade and kitchen",
        "press_heading": "Awards and recognitions of the brigade.",
        # list[5] of dict (magazine, issue, title, byline) — DIFFERENT shape from home.press_items!
        "press_items": [
            {
                "magazine": "Guida Michelin Italia",
                "issue":    "2019 edition – confirmed 2025",
                "title":    "One star · Trebbio restaurant · Tuscan cuisine of place",
                "byline":   "Michelin editorial board",
            },
            {
                "magazine": "Touring Magazine",
                "issue":    "April 2024",
                "title":    "Vittoria Sernigi · a portrait of the direttrice who keeps village hospitality honest",
                "byline":   "Maria Sirotti",
            },
            {
                "magazine": "Gambero Rosso",
                "issue":    "January 2025 · Three forks",
                "title":    "Trebbio di Borgo San Marco · three forks confirmed",
                "byline":   "Eleonora Cozzella",
            },
            {
                "magazine": "Condé Nast Traveler Italia",
                "issue":    "May 2023 · Gold List",
                "title":    "Borgo San Marco · Top 50 Italy",
                "byline":   "Caterina Cesari",
            },
            {
                "magazine": "Bell'Italia",
                "issue":    "September 2024",
                "title":    "The 12 great hospitality houses of the Val d'Orcia",
                "byline":   "Giovanni Rajberti",
            },
        ],

        "numbers_label": "The brigade in figures",
        # list[6] of tuple[2]
        "numbers": [
            ("14",   "People on the floor brigade"),
            ("10",   "Seasonal staff returning since 2014"),
            ("32",   "Years of experience of the direttrice"),
            ("4",    "Languages on the floor (IT · EN · FR · DE)"),
            ("12",   "Years affiliated with Relais & Châteaux"),
            ("4200", "Labels in the cellar · led by Anna Ricci AIS"),
        ],

        "visit_label":         "To write to the brigade",
        "visit_heading":       "One brigade, one floor.",
        "visit_text":
            "For requests about the menu, allergies, wine, outings or spa treatments "
            "write directly to the brigade: we reply within the next working day. "
            "Vittoria personally signs off every reservation confirmation. "
            "Village hospitality begins in the inbox.",
        "visit_primary":       "Write to the management",
        "visit_primary_href":  "concierge",
    },

    # ─── SOGGIORNO (services · l'esperienza del soggiorno) ────
    "soggiorno": {
        "eyebrow":      "The experience · five movements of the stay",
        "headline":     "Five movements · from Pienza to your return. Village hospitality.",
        "intro":
            "A stay at Borgo San Marco unfolds in five movements · the arrival, the "
            "floor, the spa, the cellar and the way out into the territory. Each "
            "movement is curated by your floor referent. Village hospitality, "
            "in five acts.",

        "process_label":   "Five movements",
        "process_heading": "How a stay unfolds.",
        "process_intro":
            "The narrative of the stay is a single thread, from the moment you write "
            "to the management until you return home.",
        # list[5] of dict (n, title, text, duration)
        "process": [
            {
                "n":        "01",
                "title":    "The confirmation",
                "text":
                    "A personal reply from Vittoria within 24 hours of your request · "
                    "choice of suite, seasonal window, any special requests (menu, "
                    "allergies, outings).",
                "duration": "1 day",
            },
            {
                "n":        "02",
                "title":    "The arrival",
                "text":
                    "Reception from 2 p.m. · transfer from Florence airport on request "
                    "· welcome on the village piazza with a wine of the territory · "
                    "introduction of your floor referent.",
                "duration": "2 hours",
            },
            {
                "n":        "03",
                "title":    "The floor and the cellar",
                "text":
                    "Dinner at the Trebbio restaurant · a five-course menu of the "
                    "territory · wine pairings commented by the sommelier · cellar "
                    "open after dinner for those who wish to linger.",
                "duration": "One evening per stay",
            },
            {
                "n":        "04",
                "title":    "The spa and the territory",
                "text":
                    "Half a day in the Aqua di Borgo spa (18th-century cistern) · "
                    "swimming, hammam, sauna, hydromassage in the natural basin · "
                    "treatments by appointment · half-day outing in the Val d'Orcia "
                    "with your referent.",
                "duration": "One half-day",
            },
            {
                "n":        "05",
                "title":    "The way out",
                "text":
                    "Check-out by 11 a.m. · late breakfast until 10:30 served under "
                    "the wisteria pergola · parting gift (Fattoria Trebbio olive oil "
                    "· small book of the borgo) · accompanied departure.",
                "duration": "One half-day",
            },
        ],

        "testimonial_label":  "The voice of the guest",
        "testimonial_text":
            "«Three stays across three different seasons, always the same brigade, "
            "always Federico at reception. It is rare, in Italy, to find a hotel "
            "where the promise made the first time still holds true on the third "
            "visit.»",
        "testimonial_author": "Giorgio Borghi · Milan · guest since 2018",

        "faq_label":    "Recurring questions from the management",
        # list[6] of dict (q, a)
        "faq_items": [
            {
                "q": "Is the hotel open all year round?",
                "a":
                    "No. Borgo San Marco opens from April 18 to October 27, 2026 — "
                    "twenty-four weeks of season. The winter closure allows for the "
                    "upkeep of the suites and the rest of the floor brigade. No "
                    "exceptions, not even for New Year's Eve. Village hospitality "
                    "requires the off-season as much as the season.",
            },
            {
                "q": "Can the whole borgo be reserved for one family?",
                "a":
                    "Yes · on three windows a year (June, September, late October). "
                    "Eight suites held back · restaurant closed to outside guests · "
                    "dedicated brigade. Write to the management at least six months "
                    "ahead of the desired date.",
            },
            {
                "q": "Are weddings held at the borgo?",
                "a":
                    "Intimate weddings only · maximum 36 guests · civil ceremony in "
                    "the loggia of the piano nobile · dinner under the wisteria "
                    "pergola. We do not host weddings of more than 36 guests in order "
                    "to preserve the scale of the borgo. Write to Vittoria at least "
                    "one year ahead.",
            },
            {
                "q": "Are small dogs welcome?",
                "a":
                    "Yes · on request · in two ground-floor suites (Il Frantoio and "
                    "Il Pozzo). Supplement of € 30 per night · bowl, bed and biscuits "
                    "included. Pet sitter from the borgo available by appointment "
                    "during dinner hours at the restaurant.",
            },
            {
                "q": "Can I visit the cellar even if I am not dining at the restaurant?",
                "a":
                    "Yes · the cellar is open to the borgo's guests twice a week "
                    "(Tuesday and Thursday afternoons, 5–7 p.m.) for a three-wine "
                    "tasting with Anna · advance reservation at the reception is "
                    "required.",
            },
            {
                "q": "Is there wi-fi in the suites?",
                "a":
                    "Yes · fibre line at 1 Gbit/s · available in all eight suites, "
                    "on the floor and in the spa. On request a digital detox mode "
                    "can be activated: the suite remains without connection for the "
                    "whole stay · a drawer for devices is provided on arrival.",
            },
        ],

        "cta_label":         "To begin",
        "cta_heading":       "<em>A short season</em>, one single brigade.",
        "cta_text":
            "The 2026 seasonal windows open on April 18 · the most requested suites "
            "(La Vigna, Il Cortile, La Torre) are usually fully booked by the end of "
            "May. Write to the management to confirm your reservation — village "
            "hospitality keeps a short calendar.",
        "cta_primary":       "Reserve your stay",
        "cta_primary_href":  "concierge",
    },

    # ─── CONCIERGE (contact · concierge dedicato) ─────────────
    "concierge": {
        "eyebrow":      "Dedicated concierge · Vittoria Sernigi",
        "headline":     "Write to the management. Village hospitality, with a name attached.",
        "intro":
            "For reservation requests, the exclusive borgo windows, seasonal packages "
            "and any question about the stay, write directly to the management. "
            "Vittoria replies personally within the next working day — village "
            "hospitality, with a single name on every reply.",

        "phone_label":   "Direct lines",
        "phone_intro":
            "Reception open 24 hours · dedicated concierge on the floor in continuous "
            "shifts · direct number for emergencies.",
        # list[4] of tuple[2]
        "phone_rows": [
            ("Concierge",   "+39 0578 748 124"),
            ("Direction",   "+39 0578 748 100 · Vittoria only"),
            ("Restaurant",  "+39 0578 748 130 · Trebbio reservations"),
            ("Spa",         "+39 0578 748 145 · Aqua reservations"),
        ],

        "form_section_label": "Reservation request",
        "form_section_intro":
            "Indicate your desired dates, preferred suite (or borgo exclusive) and "
            "any special requests. Vittoria replies personally by email with the "
            "confirmation or an alternative proposal within 24 hours.",
        "form_helper_required":  "Fields marked with · are required",
        "form_submit_button":    "Send your request to the management",
        "form_submit_note":
            "Final confirmation is made by a 30% deposit via bank transfer · balance "
            "settled at reception on arrival.",
        # list[10] of dict (label, name, type, required, options)
        "form_fields": [
            {"label": "Full name",                      "name": "name",      "type": "text",     "required": True,  "options": []},
            {"label": "Email · personal reply",         "name": "email",     "type": "email",    "required": True,  "options": []},
            {"label": "Telephone",                      "name": "phone",     "type": "tel",      "required": False, "options": []},
            {"label": "Arrival date",                   "name": "arrival",   "type": "date",     "required": True,  "options": []},
            {"label": "Departure date",                 "name": "departure", "type": "date",     "required": True,  "options": []},
            {"label": "Number of guests",               "name": "guests",    "type": "number",   "required": True,  "options": []},
            {"label": "Preferred suite",                "name": "suite",     "type": "select",   "required": False,
             "options": ["La Vigna", "Il Frantoio", "Il Pozzo", "La Cisterna", "La Torre", "Il Cortile", "Borgo exclusive · 8 suites", "No preference"]},
            {"label": "Package",                        "name": "package",   "type": "select",   "required": False,
             "options": ["Short stay · 2 nights", "Classic stay · 4 nights", "Long stay · 7 nights", "Borgo exclusive · 5 nights", "Intimate wedding"]},
            {"label": "Allergies or dietary requests",  "name": "allergies", "type": "text",     "required": False, "options": []},
            {"label": "Notes to the management",        "name": "notes",     "type": "textarea", "required": False, "options": []},
        ],

        "offices_label":   "Addresses",
        "offices_heading": "The borgo and the estates.",
        "offices_intro":
            "The borgo is reachable by car from Florence (1h45) or Rome (2h30) · "
            "transfer from Florence airport or Chiusi-Chianciano railway station "
            "on request.",
        # list[3] of dict (role, city, address, hours, email)
        "offices": [
            {
                "role":     "Borgo · reception",
                "city":     "Pienza · Siena",
                "address":  "Borgo San Marco di Sopra 17 · 53026 Pienza",
                "hours":    "24-hour reception · check-in 2 p.m.–10 p.m. · check-out by 11 a.m.",
                "email":    "concierge@borgosanmarco.it",
            },
            {
                "role":     "Fattoria Trebbio · cellar and olive grove",
                "city":     "Pienza · Siena · 1.2 km from the borgo",
                "address":  "Strada Provinciale 146 · 53026 Pienza",
                "hours":    "Cellar · Tuesday and Thursday 5–7 p.m. · tastings by reservation",
                "email":    "cantina@borgosanmarco.it",
            },
            {
                "role":     "Aqua di Borgo · spa",
                "city":     "18th-century cistern · lower level",
                "address":  "Borgo San Marco di Sopra 17 · level –1",
                "hours":    "Spa 9 a.m.–1 p.m. · 3–8 p.m. · treatments by appointment",
                "email":    "spa@borgosanmarco.it",
            },
        ],

        "press_contact_label": "Press and media",
        "press_contact_text":
            "For editorial enquiries, press visits and interviews with the management "
            "· write to Maria Bonelli, press office for Vittoria Sernigi, including "
            "publication and topic.",
        "press_contact_email": "stampa@borgosanmarco.it",
    },

    # ─── POSTS (8 suites · the room cards consumed by camere blog_list) ─
    "posts": [
        {
            "slug":         "suite-la-vigna",
            "image":        _SUITE_VIGNA,
            "kicker":       "Suite 01",
            "title":        "La Vigna",
            "date":         "2026 season · April – October",
            "author":       "Borgo San Marco",
            "read_min":     "62 m²",
            "lede":
                "The suite looking out over the estate's historic Sangiovese vineyard · "
                "first floor of the west wing · king double bed · original 17th-century "
                "beamed ceiling.",
            "footer_strap": "Available May – September · vineyard view",
            # list of 2-tuples (k, v)
            "meta_rows": [
                ("Floor",       "First · west wing"),
                ("Beds",        "King double + chaise longue"),
                ("Surface",     "62 m² + 8 m² of loggia"),
                ("View",        "Historic Sangiovese vineyard · olive grove"),
                ("Bathroom",    "Travertino marble · walk-in shower + bathtub"),
                ("Included",    "Breakfast · spa · cellar tasting"),
                ("Seasonality", "Available May – September"),
            ],
            # list of 2-tuples (kind, text)
            "body": [
                ("p", "La Vigna is the most requested suite in the house · looking directly out over the historic Sangiovese vineyard that yields the grapes for the Brunello of Fattoria Trebbio. Original 17th-century beamed ceiling, patinated cotto floor, furniture salvaged from houses of the borgo."),
                ("p", "The private 8 m² loggia is set with a wicker daybed and a pietra serena side table · perfect for breakfast for two or for the evening glass of Brunello (always included, from Anna's cellar)."),
                ("h3", "The historic vineyard"),
                ("p", "The Fattoria Trebbio vineyard spreads across 4.2 hectares to the south of the borgo, east-south-east exposure. Hand-harvested in October · vinified in small steel vats · aged in large oak casks · bottled at the estate. The Brunello carries the same signature as the borgo."),
                ("ul", ["Capacity · two adults · cot for an infant on request", "Wi-Fi · 1 Gbit/s fibre · direct line on the borgo network", "Climate control · independent, adjustable from the suite", "Safe · digital · for valuables", "TV · 55-inch · international channels on request"]),
                ("p", "Suite La Vigna is available from May to late September. For the 2026 season it can only be reserved as a package of three nights or more."),
            ],
        },
        {
            "slug":         "suite-il-frantoio",
            "image":        _SUITE_FRANTOIO,
            "kicker":       "Suite 02",
            "title":        "Il Frantoio",
            "date":         "2026 season · throughout",
            "author":       "Borgo San Marco",
            "read_min":     "78 m²",
            "lede":
                "The largest suite · ground floor of the south wing · at the centre of "
                "the room, the 1620 olive press millstone preserved as an architectural "
                "element.",
            "footer_strap": "Available April – October · south wing ground floor",
            "meta_rows": [
                ("Floor",       "Ground floor · south wing"),
                ("Beds",        "Double + separate sitting room"),
                ("Surface",     "78 m² + 12 m² of patio"),
                ("View",        "Inner courtyard with the 1620 millstone"),
                ("Bathroom",    "White marble · freestanding bathtub + shower"),
                ("Included",    "Breakfast · spa · cellar tasting + olive oil"),
                ("Seasonality", "Available throughout the season"),
            ],
            "body": [
                ("p", "Il Frantoio is the largest of the eight suites · 78 m² of floor plan plus a 12 m² private patio onto the inner courtyard. The circular millstone of the original 1620 olive press has been preserved at the centre of the room as an architectural element — no longer operational but intact, in pietra serena."),
                ("p", "The suite includes a small private cellar with six bottles of Brunello from Fattoria Trebbio (2018-2020 vintages) and one bottle of EVO oil from the historic olive grove · guests may taste freely and are invoiced only at the end of the stay."),
                ("h3", "The historic olive press"),
                ("p", "The olive press was in operation from 1620 until 1968, when the oil of Fattoria Trebbio began to be pressed at the communal mill of Pienza. The suite's millstone is one of the two originals · the second is on display in the house museum, next to the courtyard."),
                ("ul", ["Capacity · two adults + one child on the sofa-bed", "Wi-Fi · 1 Gbit/s fibre", "Climate control · independent, dual zone room/sitting room", "Patio · 12 m² with wrought-iron side table and armchairs", "Private mini-cellar · 6 bottles of Brunello + 1 bottle of EVO oil"]),
                ("p", "Il Frantoio is available throughout the open season. Minimum stay of two nights."),
            ],
        },
        {
            "slug":         "suite-il-pozzo",
            "image":        _SUITE_POZZO,
            "kicker":       "Suite 03",
            "title":        "Il Pozzo",
            "date":         "2026 season · on request",
            "author":       "Borgo San Marco",
            "read_min":     "54 m²",
            "lede":
                "The most private suite · ground floor with direct access to the "
                "17th-century inner courtyard · at the centre of the courtyard, the "
                "original 1612 octagonal well.",
            "footer_strap": "On request · couples only · private courtyard",
            "meta_rows": [
                ("Floor",       "Ground floor · inner courtyard"),
                ("Beds",        "Standard double"),
                ("Surface",     "54 m² + 28 m² private courtyard"),
                ("View",        "Octagonal courtyard with the 1612 well"),
                ("Bathroom",    "Pietra serena · walk-in shower"),
                ("Included",    "Breakfast · spa · cellar · courtyard"),
                ("Seasonality", "On request · couples only · dogs welcome"),
            ],
            "body": [
                ("p", "Il Pozzo is the most private suite in the house · accessed only from the inner courtyard, with no openings onto the outside of the borgo. The octagonal 1612 well is still working (fresh water from the San Quirico aquifer) and shades a small 28 m² courtyard reserved exclusively for the suite."),
                ("p", "This suite is offered only to couples · no children · and welcomes small dogs under 10 kg on request (supplement of € 30 per night, bowl and bed included)."),
                ("h3", "The octagonal well"),
                ("p", "The octagonal well is one of three wells in the borgo · it is the only one still active. Octagonal like the dome of Brunelleschi, of whom Pio II was an admirer. Built in 1612 by the same mason who raised the parsonage · signature carved inside the mouth of the well, illegible since 1923 but documented in an 1898 booklet kept in the parsonage."),
                ("ul", ["Capacity · two adults · no children", "Small dogs welcome · supplement € 30/night", "Private courtyard · 28 m² with an iron table · shaded by the well", "Wi-Fi · 1 Gbit/s fibre", "Climate control · independent"]),
                ("p", "Il Pozzo is available only on direct request to the management. Minimum stay of three nights."),
            ],
        },
        {
            "slug":         "suite-la-cisterna",
            "image":        _SUITE_CISTERNA,
            "kicker":       "Suite 04",
            "title":        "La Cisterna",
            "date":         "2026 season · on request",
            "author":       "Borgo San Marco",
            "read_min":     "88 m²",
            "lede":
                "A suite carved into the vault of the 18th-century cistern · lower "
                "level · four-poster bed · natural light from above through the "
                "original 1742 skylight.",
            "footer_strap": "On request · honeymoon recommended",
            "meta_rows": [
                ("Floor",       "Lower level (–1) · east wing"),
                ("Beds",        "Double + walnut four-poster"),
                ("Surface",     "88 m² · vault ceiling 4.2 m"),
                ("View",        "Zenithal skylight · no exterior openings"),
                ("Bathroom",    "Travertino stone · cistern-shaped bathtub"),
                ("Included",    "Breakfast · spa · cellar · night experience"),
                ("Seasonality", "On request · honeymoon recommended"),
            ],
            "body": [
                ("p", "La Cisterna is the most sought-after suite in the borgo · carved into the vault of the 18th-century cistern, lower level, ceiling 4.2 metres high. Natural light enters only through the zenithal skylight of 1742 (original) · at night the starry sky of the Val d'Orcia falls directly into the room."),
                ("p", "The original cistern collected rainwater from the roof of the parsonage until 1923, when the borgo was connected to the municipal aqueduct. The 2009 Castellini-Mancini restoration preserved the original curvature and the engraved inscription of the 18th-century owner (Giovan Pietro Buonsignori, 1742)."),
                ("h3", "The four-poster bed"),
                ("p", "The bed is a historic piece · canopy frame in solid Pratomagno walnut, hand-forged iron by the village blacksmith (Mario Calzini, 1971-2018; today his nephew Luca carries on the workshop). Canopy textiles in Bonotto linen. Oil lamps replaced with small warm-temperature LED lights."),
                ("ul", ["Capacity · two adults · no children", "Wi-Fi · 1 Gbit/s fibre · no 4G reception in the lower-level room", "Climate control · independent, constant temperature 20°C even in summer", "Bathtub · travertino stone · cistern-shaped", "Night experience · on request, opening of the skylight with the borgo's astronomical observatory"]),
                ("p", "La Cisterna is available only on direct request · particularly recommended for honeymoons and anniversaries. Minimum stay of four nights."),
            ],
        },
        {
            "slug":         "suite-la-torre",
            "image":        _SUITE_TORRE,
            "kicker":       "Suite 05",
            "title":        "La Torre",
            "date":         "2026 season · April – October",
            "author":       "Borgo San Marco",
            "read_min":     "70 m²",
            "lede":
                "A suite carved into the medieval corner tower · second floor · "
                "270° view of the Val d'Orcia all the way to Monte Amiata · "
                "double bed with adjoining study.",
            "footer_strap": "Available April – October · 270° view",
            "meta_rows": [
                ("Floor",       "Second floor · corner tower"),
                ("Beds",        "Double + study with sofa-bed"),
                ("Surface",     "70 m² + 6 m² study"),
                ("View",        "270° · Val d'Orcia · Monte Amiata · Pienza"),
                ("Bathroom",    "Black marble · walk-in shower"),
                ("Included",    "Breakfast · spa · cellar · astronomical telescope"),
                ("Seasonality", "April – October · staircase of 23 steps"),
            ],
            "body": [
                ("p", "La Torre occupies the second floor of the medieval corner tower of the borgo · 270° view of the Val d'Orcia (south-west), Pienza (north-west) and all the way to Monte Amiata (south-east) on clear days. Three original 16th-century windows with restored leaded glass."),
                ("p", "The adjoining 6 m² study is furnished with a Pratomagno walnut desk and a library of volumes on the Val d'Orcia (in Italian and English) · ideal for those who need a half-day of work during the stay."),
                ("h3", "The astronomical telescope"),
                ("p", "The tower is equipped with a small Bresser 90 mm astronomical telescope installed at the west window · ideal for observing the constellations of the Val d'Orcia (zero light pollution). User's manual in the drawer · guided evening with the floor referent on request."),
                ("ul", ["Capacity · two adults + one child on the study sofa-bed", "Staircase · 23 steps · no lift in the tower", "Wi-Fi · 1 Gbit/s fibre", "Climate control · ceiling fan + independent unit", "Telescope · Bresser 90 mm + manual + guided session on request"]),
                ("p", "La Torre is available from April to October. Minimum stay of two nights."),
            ],
        },
        {
            "slug":         "suite-il-cortile",
            "image":        _SUITE_CORTILE,
            "kicker":       "Suite 06",
            "title":        "Il Cortile",
            "date":         "2026 season · May – October",
            "author":       "Borgo San Marco",
            "read_min":     "65 m²",
            "lede":
                "A suite with a private loggia onto the wisteria pergola · ground "
                "floor of the north wing · 18 m² private garden with side table "
                "and armchairs.",
            "footer_strap": "Available May – October · garden + pergola",
            "meta_rows": [
                ("Floor",       "Ground floor · north wing"),
                ("Beds",        "Double + sofa-bed"),
                ("Surface",     "65 m² + 18 m² private garden"),
                ("View",        "Wisteria pergola · private garden"),
                ("Bathroom",    "Travertino marble · walk-in shower"),
                ("Included",    "Breakfast · spa · cellar · private garden"),
                ("Seasonality", "May – October · wisteria in bloom May–June"),
            ],
            "body": [
                ("p", "Il Cortile has the most direct access to the wisteria pergola, the soul of the borgo · the wisteria was planted in 1924 by the Buonsignori family, full bloom in the first three weeks of May. Private garden of 18 m² bounded by a low pietra serena wall · set with two wrought-iron armchairs and a stone side table."),
                ("p", "Breakfast under the pergola is a house practice · every morning from 8 to 10:30 the pergola becomes a small breakfast court · guests seated at low tables, floor brigade in continuous passage · warm Lorenzini bread from the village oven, the management's wild rose marmalade, Castelmuzio cheeses, fruit from the surrounding farms."),
                ("h3", "The wisteria of 1924"),
                ("p", "The wisteria was planted in 1924 by Caterina Buonsignori (1902-1989, the last of the original family of the borgo) as a wedding gift for her daughter Anna. Since then it has grown to cover the entire pergola of the courtyard. Full bloom lasts three weeks · from the first ten days of May until about May 25."),
                ("ul", ["Capacity · two adults + one child on the sofa-bed", "Private garden · 18 m² · pietra serena low wall · furnished", "Wi-Fi · 1 Gbit/s fibre", "Climate control · independent", "Breakfast · served under the wisteria pergola 8–10:30"]),
                ("p", "Il Cortile is available from May to October. To see the wisteria in bloom, reserve in the first half of May."),
            ],
        },
        {
            "slug":         "suite-la-loggia",
            "image":        _SUITE_LOGGIA,
            "kicker":       "Suite 07",
            "title":        "La Loggia",
            "date":         "2026 season · April – October",
            "author":       "Borgo San Marco",
            "read_min":     "82 m²",
            "lede":
                "Suite of the piano nobile · Renaissance loggia opening onto Pienza "
                "· painted coffered ceiling from 1671 · king double bed + study + "
                "master bathroom.",
            "footer_strap": "Available April – October · piano nobile",
            "meta_rows": [
                ("Floor",       "First floor · piano nobile · west wing"),
                ("Beds",        "King double + study"),
                ("Surface",     "82 m² + 14 m² loggia"),
                ("View",        "Pienza · cathedral · Palazzo Piccolomini"),
                ("Bathroom",    "Travertino + statuario marble · bathtub + separate shower"),
                ("Included",    "Breakfast · spa · cellar · private dinner in the loggia on request"),
                ("Seasonality", "April – October · civil ceremony in the loggia possible"),
            ],
            "body": [
                ("p", "La Loggia is the suite of the piano nobile · 82 m² plus a 14 m² Renaissance loggia opening onto Pienza · one sees Bernardo Rossellino's 1462 cathedral and Palazzo Piccolomini. The painted coffered ceiling from 1671 was restored in 2009 by Mauro Pellegrini, a restorer from Siena."),
                ("p", "The loggia is the setting for the civil ceremony at the borgo's intimate weddings (maximum 36 guests). On request a private dinner in the loggia can be arranged for the suite's guests · service by chef Tommaso · price on application."),
                ("h3", "The coffered ceiling of 1671"),
                ("p", "The ceiling was commissioned by Pietro Buonsignori in 1671 from the Sienese painter Domenico Manetti (1609-1683). Thirty coffers painted in tempera: views of the Val d'Orcia, heraldic symbols of the family, harvesting putti. The 2009 restoration brought back the original colours; the gilding was confirmed in the laboratory."),
                ("ul", ["Capacity · two adults + one child on the study sofa-bed", "Loggia · 14 m² opening onto Pienza · furnished · private dinner on request", "Wi-Fi · 1 Gbit/s fibre", "Climate control · dual zone", "Civil ceremony · in the loggia · up to 36 guests · on request"]),
                ("p", "La Loggia is available from April to October. Minimum stay of two nights, three nights for the civil-ceremony window."),
            ],
        },
        {
            "slug":         "suite-la-cantina",
            "image":        _SUITE_CANTINA,
            "kicker":       "Suite 08",
            "title":        "La Cantina",
            "date":         "2026 season · on request",
            "author":       "Borgo San Marco",
            "read_min":     "92 m²",
            "lede":
                "A suite carved into the 18th-century historic cellar (the working "
                "cellar is now at Fattoria Trebbio) · lower level · king double bed "
                "+ sitting area + private 12-label cellar.",
            "footer_strap": "On request · ideal for wine lovers",
            "meta_rows": [
                ("Floor",       "Lower level (–1) · south wing"),
                ("Beds",        "King double + sitting area"),
                ("Surface",     "92 m² · vault ceiling 3.8 m"),
                ("View",        "Private glassed cellar · no exterior openings"),
                ("Bathroom",    "Travertino stone · walk-in shower with view onto the cellar"),
                ("Included",    "Breakfast · spa · 12 labels in the private cellar · guided tasting"),
                ("Seasonality", "On request · ideal autumn"),
            ],
            "body": [
                ("p", "La Cantina is carved into the historic cellar of the borgo · lower level, vault 3.8 metres high · it was the working cellar until 2007, when the wine of Fattoria Trebbio was moved to the modern cellar 1.2 km away. The suite retains the private glassed cellar, restocked every season with 12 estate labels selected by sommelier Anna."),
                ("p", "The cellar is included in the stay · the 12 bottles are at the guests' disposal for unlimited tasting throughout the stay. Anna's guided tasting is scheduled one evening per stay (included in the rate) · further tastings on request."),
                ("h3", "The 12 labels of the season"),
                ("p", "The cellar composition changes every season. The 2026 selection (curated by Anna Ricci): 4 Brunello (Fattoria Trebbio 2018, Biondi-Santi 2016, Casanova di Neri 2017, Il Poggione 2018) · 3 Vino Nobile (Avignonesi 2019, Salcheto 2020, Boscarelli 2018) · 2 Chianti Classico (Castello di Ama 2019, Felsina 2018) · 3 experimental wines of southern Toscana (Petricci 2020, Gualdo del Re 2021, Salvo 2019)."),
                ("ul", ["Capacity · two adults · no children", "Cellar · 12 labels · selection by Anna Ricci AIS · changes every season", "Guided tasting · one evening per stay (included)", "Wi-Fi · 1 Gbit/s fibre · no 4G reception", "Climate control · independent, constant temperature 18°C"]),
                ("p", "La Cantina is available on request · ideal autumn season after the harvest. Minimum stay of four nights."),
            ],
        },
    ],
}
