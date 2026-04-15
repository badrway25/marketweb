"""Phase 2g3.7 · Session 53 · Villa — EN native-voice tree. Editorial-concierge private-advisory voice."""
from __future__ import annotations

from typing import Any


VILLA_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Residences",  "kind": "home"},
        {"slug": "collezione", "label": "Collection",  "kind": "blog_list"},
        {"slug": "territorio", "label": "Territories", "kind": "about"},
        {"slug": "studio",     "label": "The Studio",  "kind": "team"},
        {"slug": "esperienza", "label": "Experience",  "kind": "services"},
        {"slug": "concierge",  "label": "Concierge",   "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":   "V",
        "logo_word":      "Villa Prestige",
        "logo_subline":   "Private Advisory · Since 1998",
        "tag":            "Spring 2026 Collection · Portfolio N° 03",
        "phone":          "concierge@villaprestige.it",
        "phone_label":    "Confidential concierge line",
        "email":          "concierge@villaprestige.it",
        "email_label":    "Private concierge",
        "address":        "Via Montenapoleone 17 · 20121 Milan",
        "hours_compact":  "Viewings by appointment only · Mon–Fri 10–19 · Sat on request",
        "hours_footer_rows": [
            "In-office meetings · private concierge",
            "Languages: Italian · English · French",
        ],
        "license":        "RIEA Milan N° 2841 · VAT IT07324110984 · Private advisor register",
        "footer_intro":
            "Villa Prestige — a private-advisory studio for signature residences across Italy and the French "
            "Riviera. A narrow portfolio, a single point of contact, absolute discretion. We select historic "
            "and contemporary homes exclusively for private clients and family offices, following a two-tier "
            "review of architectural authorship and territorial coherence.",

        # Nav reservation CTA (private viewing)
        "nav_cta":         "Request a private viewing",
        "nav_cta_kind":    "appointment",
        "nav_cta_short":   "Request viewing",

        # Footer labels
        "foot_studio":   "The studio",
        "foot_pages":    "Sitemap",
        "foot_contact":  "Concierge",
        "foot_offices":  "Offices",
        "offices_footer_rows": [
            "Milan · Montenapoleone 17",
            "Portofino · concierge office",
            "Saint-Tropez · by appointment",
        ],
        "office_rows": [
            "Milan · Montenapoleone 17",
            "Portofino · concierge office",
            "Saint-Tropez · by appointment",
        ],

        # Cross-page editorial meta-strip labels (D-047)
        "dossier_label":        "Dossier",
        "portfolio_label":      "Portfolio",
        "territorio_label":     "Territory",
        "superficie_label":     "Surface",
        "provenance_label":     "Provenance",
        "access_label":         "Access",
        "availability_label":   "Availability",
        "price_note":           "Price upon application",
        "nda_required_label":   "Non-disclosure agreement required before the dossier",
        "viewing_on_request":   "Available by appointment only",
        "referent_label":       "Single point of contact",
        "concierge_line_label": "Concierge line",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        # Fullbleed editorial cover
        "cover_location": "Portofino · Liguria",
        "cover_image_credit": "Spring collection · dossier 03 / 18",
        "cover_image":
            "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=2200&h=1400&fit=crop",

        # Eyebrow + serif drama
        "eyebrow":          "Villa Prestige · Private Advisory · Italy & the French Riviera",
        "headline":         "Signature <em>residences</em>, for those who recognise them.",
        "sub":
            "A narrow portfolio of private residences — historic and contemporary — released only by "
            "appointment. Confidential viewings, a dedicated editorial dossier, discreet negotiation. "
            "From the first encounter to the notary signature, a single point of contact.",

        # Hero wordmark + counter chip (from DNA)
        "hero_wordmark":        "Villa Prestige",
        "hero_location":        "Portofino · Spring 2026 Collection",
        "hero_counter_label":   "Residence in focus",
        "hero_counter_value":   "N° 03 / 18",
        "hero_series_label":    "In focus",
        "hero_series_title":    "« Villa Aurelia » · Portofino",
        "hero_series_note":
            "A 1922 historic residence set within a three-hectare park above the gulf. Four hundred "
            "square metres, a signed library, infinity pool overlooking the Palmaria island.",
        "primary_cta":          "Request a private viewing",
        "primary_cta_href":     "concierge",
        "secondary_cta":        "Spring collection",
        "secondary_cta_href":   "collezione",

        # Editorial credit cells — fullbleed hero bottom strip
        "hero_credit_cells": [
            ("Collection", "N° 03 / 18"),
            ("Territory",  "Portofino · Liguria"),
            ("Surface",    "400 m² · park 30,000 m²"),
            ("Access",     "By appointment only"),
        ],

        # Signature properties strip — 4 dossier cards (2-up editorial grid)
        "signature_label":   "Spring collection",
        "signature_heading": "Residences <em>chosen</em> for this season.",
        "signature_intro":
            "Every property is released only after a two-tier review — architectural authorship and "
            "territorial coherence. The full list is available upon request, in the form of an "
            "editorial dossier signed by your private advisor.",
        "signature": [
            {
                "index":       "01",
                "title":       "Villa Aurelia",
                "territorio":  "Portofino · Liguria",
                "superficie":  "400 m² · park 30,000 m²",
                "provenance":  "1920s · Piacentini signature",
                "availability":"Three-day window",
                "slug":        "villa-aurelia-portofino",
                "image":
                    "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "02",
                "title":       "Castello di Monterò",
                "territorio":  "Chianti Classico · Tuscany",
                "superficie":  "1,200 m² · 18 hectares",
                "provenance":  "12th century · 2014 restoration",
                "availability":"Exclusive mandate",
                "slug":        "castello-di-montero-chianti",
                "image":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "03",
                "title":       "Penthouse Quadronno",
                "territorio":  "Milan · Magenta",
                "superficie":  "380 m² · terrace 180 m²",
                "provenance":  "Sole top-floor · Duomo view",
                "availability":"By appointment",
                "slug":        "penthouse-quadronno-milano",
                "image":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "04",
                "title":       "Mas de la Mer",
                "territorio":  "Saint-Tropez · French Riviera",
                "superficie":  "550 m² · private vineyard",
                "provenance":  "18th century · certified",
                "availability":"Newly released",
                "slug":        "mas-de-la-mer-saint-tropez",
                "image":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
        ],
        "signature_link_all":  "View the full collection  →",
        "signature_link_href": "collezione",

        # Territory ribbon — continental destinations
        "territory_label":  "Territories of reference",
        "territory":        ["PORTOFINO", "CHIANTI CLASSICO", "COSTA SMERALDA", "LAGO DI COMO", "SAINT-TROPEZ", "CAPRI", "VAL D'ORCIA"],

        # Private advisor block
        "advisor_label":    "Private advisor",
        "advisor_heading":  "One <em>point of contact</em>, from the first dossier to the notary.",
        "advisor_intro":
            "Every private client is followed personally by their advisor, from the delivery of the "
            "first editorial dossier to the notary signature. Never more than eight active mandates "
            "per advisor, to ensure genuine presence and absolute discretion.",
        "advisor_name":     "Alessandra Visconti di Modrone",
        "advisor_role":     "Private client director · since 2011",
        "advisor_bio":
            "Fifteen years at Savills, Knight Frank and Sotheby's International Realty "
            "(London · Milan · Portofino). She has personally handled more than eighty private "
            "transactions across Italy and the French Riviera for European, American and Asian "
            "families. Each client is accompanied by her, from the first confidential meeting "
            "through to the notary signature.",
        "advisor_portrait":
            "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
        "advisor_cta":      "Request an introductory conversation",
        "advisor_cta_href": "concierge",

        # Editorial storytelling — the maison's numbers (discreet stats — counters OK)
        "numbers_label":    "The studio in figures",
        "numbers_heading":  "A <em>narrow</em> portfolio, fully attended to.",
        "numbers": [
            ("26",   "years of private advisory"),
            ("42",   "residences in portfolio"),
            ("9",    "dedicated private advisors"),
            ("150",  "family offices served"),
        ],
        "numbers_note":
            "Never more than fifty simultaneous mandates. Every dossier passes across the director's "
            "desk before entering the collection.",

        # Press ribbon
        "press_label":    "Editorial",
        "press_intro":    "Featured in",
        "press_items":    [
            "Financial Times · How to Spend It",
            "Monocle",
            "Robb Report",
            "Corriere Living",
            "AD Italia",
        ],

        # Editorial storytelling panel — closing private-viewing band
        "private_label":    "Private viewing",
        "private_heading":  "One hour in a reserved room, <em>the dossier in your hands.</em>",
        "private_intro":
            "In-office meetings take place by appointment, in the presence of your advisor. "
            "We prepare in advance the editorial dossiers of the residences compatible with the "
            "client profile and reserve a room where views are projected in large format. "
            "The service is at no charge and strictly confidential.",
        "private_primary":       "Request a private viewing",
        "private_primary_href":  "concierge",
        "private_secondary":     "Discover the experience",
        "private_secondary_href":"esperienza",
    },

    # ─── COLLEZIONE — signature properties list (blog_list) ───
    "collezione": {
        "eyebrow":   "Spring 2026 Collection · dossiers 01 – 14",
        "headline":  "Fourteen <em>signature residences</em>, awaiting their interlocutor.",
        "intro":
            "The collection is open exclusively to clients under a non-disclosure agreement. Every "
            "dossier includes architectural provenance, editorial floorplan, territory and a brief "
            "history of the residence. Prices are communicated directly by the advisor after the "
            "first confidential meeting.",

        # Lead post / hero dossier
        "lead_image":
            "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=1600&h=1000&fit=crop",

        # Filters by territorio / provenance / availability
        "filter_label":  "Selection",
        "filter_groups": [
            {
                "label":   "Territory",
                "options": ["All", "Portofino", "Chianti Classico", "Milan", "French Riviera", "Capri", "Lago di Como", "Val d'Orcia"],
            },
            {
                "label":   "Provenance",
                "options": ["All", "17th–18th century", "Early 20th century · signature architect", "Contemporary · recent restoration", "Sole top-floor"],
            },
            {
                "label":   "Availability",
                "options": ["Open", "Newly released", "Exclusive", "By appointment only"],
            },
        ],
        "sort_label":    "Arrange by",
        "sort_options":  ["Territory", "Provenance", "Most recent", "Exclusives"],

        "result_count":    "14 dossiers in the spring collection",
        "result_subtitle": "Updated the first Thursday of each month",

        "footer_note_label": "Entry to the collection",
        "footer_note":
            "The summer 2026 collection opens on Thursday 28 May. Clients already under NDA retain "
            "absolute priority on every new dossier. To join the confidential list, write directly "
            "to the maison's concierge.",
    },

    # ─── TERRITORIO (about) — editorial territorio cards ──────
    "territorio": {
        "eyebrow":   "Territories of reference · seven private geographies",
        "headline":  "The <em>landscape</em> is the first signature of a residence.",
        "intro":
            "We operate exclusively across seven territories in Italy and France. Each with a "
            "resident point of contact, a dedicated editorial archive, a network of trusted "
            "architects. We do not work outside these geographies — this is how we guarantee "
            "a genuine knowledge of the houses, of the neighbours, of the prevailing winds.",

        # Editorial statement
        "statement_label":   "Statement",
        "statement_heading": "Seven territories, <em>seven private archives.</em>",
        "statement_text":
            "Each territory is followed by a point of contact who has lived there for at least "
            "ten years. We know the residences before they come to market — often we have "
            "followed them across several generations of owners. Our archive holds historic "
            "land registry records, landscape studies, relationships with the relevant "
            "municipalities and heritage authorities.",

        # 6 territorio cards — history, provenance, architects, property count
        "territories_label":   "The seven territories",
        "territories_heading": "The geographies <em>of the collection.</em>",
        "territories_intro":
            "From the promontory of Portofino to the vineyards of Saint-Tropez, from the hills "
            "of Chianti to the Costa Smeralda. Each territory has its own season of entry, its "
            "own architectural backbone, its own register of families.",
        "territories": [
            {
                "name":      "Portofino",
                "region":    "Liguria · Tigullio gulf",
                "history":   "The promontory favoured by Milanese families since the second postwar. Seaside houses set above the water, terraces over the San Fruttuoso bay, enclosed gardens of bougainvillaea and centuries-old olive trees. The late-spring light is the best document.",
                "architects":"Gio Ponti · Gae Aulenti · Umberto Riva · recent restorations by A. Citterio",
                "count":     "9 residences in collection",
                "since":     "Resident point of contact since 2008",
                "image":
                    "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Chianti Classico",
                "region":    "Tuscany · Gaiole – Radda – Castellina",
                "history":   "The Chianti ridge between Siena and Florence, rich in medieval castles and restored parish churches. Residences lived in with productive vineyards, centuries-old olive groves and underground cellars. The territory favours conservative restoration under the Florence heritage authority.",
                "architects":"restorations by Tobia Scarpa · Massimo Carmassi · studio ACPV",
                "count":     "7 residences in collection",
                "since":     "Resident point of contact since 2011",
                "image":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Costa Smeralda",
                "region":    "Sardinia · Porto Cervo – Porto Rotondo",
                "history":   "The coastline shaped in the 1960s by Prince Karim Aga Khan. Villas designed by Jacques Couëlle and Luigi Vietti, local granite and juniper roofs. Stone terraces above the sea, private bays reachable only on foot or by tender.",
                "architects":"Jacques Couëlle · Luigi Vietti · Savin Couëlle · recent restorations by A. Citterio",
                "count":     "5 residences in collection",
                "since":     "Resident point of contact since 2014",
                "image":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Lago di Como",
                "region":    "Lombardy · Cernobbio – Tremezzo – Bellagio",
                "history":   "The historic villas on the Lario, from Villa d'Este to Villa Balbianello. Botanical parks sculpted in the 1700s, private boathouses, jasmine belvederes. Properties often listed, with restorations conducted under the Milan heritage authority.",
                "architects":"historic villas · Pelagio Palagi · restorations by Lissoni Casal Ribeiro",
                "count":     "6 residences in collection",
                "since":     "Resident point of contact since 2010",
                "image":
                    "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Saint-Tropez",
                "region":    "Côte d'Azur · Var · Pampelonne",
                "history":   "The inland Var, hills between Ramatuelle and Gassin. Provençal mas, original from the 17th–18th centuries, some with working AOP Côtes de Provence vineyards. Houses set at a discreet distance from the sea, half an hour from the port of Saint-Tropez.",
                "architects":"François Catroux · Jacques Grange · Studio KO · traditional restorations",
                "count":     "4 residences in collection",
                "since":     "Concierge office since 2016",
                "image":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Capri & Val d'Orcia",
                "region":    "Capri · southern Tuscany · Pienza – Montalcino",
                "history":   "Two territories kindred in rarity and family reserve. On Capri, terraced houses facing the Faraglioni, often passed down over three generations. In Val d'Orcia, agricultural estates with a Romanesque parish church and a Brunello vineyard, UNESCO properties under strict protection.",
                "architects":"Capri · Francesco Venezia · local Caprese tradition; Val d'Orcia · Matteo Nunziati · Studio Perruccio",
                "count":     "5 residences in collection",
                "since":     "Resident points of contact since 2013",
                "image":
                    "https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
        ],
        "territory_card_cta": "Request the territory dossier  →",
        "territory_card_cta_href": "concierge",

        # Closing — the referent promise
        "referent_label":   "The resident point of contact",
        "referent_heading": "We know the houses <em>before</em> they come to market.",
        "referent_text":
            "The resident point of contact is not a consultant on call: they are someone who "
            "has lived the territory for at least ten years, speaks the local language, knows "
            "the heritage authorities and the historic families. Many residences in the "
            "collection come to us through the word of a mutual friend, not through the market "
            "— this is the way these properties have always passed on, between people who trust "
            "one another.",

        # Discreet stats — territories in numbers
        "stats_label":      "Territories in figures",
        "stats": [
            ("7",   "territories of reference"),
            ("36",  "historic residences on file"),
            ("18",  "signature architects associated"),
            ("26",  "years of continuous presence"),
        ],
    },

    # ─── STUDIO (team) — private advisors ─────────────────────
    "studio": {
        "eyebrow":  "The studio · nine private advisors · Milan Portofino Saint-Tropez",
        "headline": "Nine advisors, <em>never more than eight mandates each.</em>",
        "intro":
            "The studio is a maison of private advisors: each of us has professional roots in "
            "the great international houses — Sotheby's International Realty, Knight Frank, "
            "Savills, Christie's Real Estate — and today works independently, with a narrow "
            "portfolio. We do not fly flags, only dossiers. We sell nothing under pressure.",

        # Director hero card — Alessandra Visconti
        "director_label":   "Direction",
        "director_name":    "Alessandra Visconti di Modrone",
        "director_role":    "Private client director · founder · since 1998",
        "director_text":
            "She founded Villa Prestige in Milan in 1998, after eight years at Sotheby's "
            "International Realty London. She has personally handled more than eighty private "
            "transactions across Italy and the French Riviera — from Villa Aurelia in Portofino "
            "to Castello di Monterò in Chianti — for European, American, Asian and Middle "
            "Eastern families. She writes an annual column for Monocle and Corriere Living on "
            "the market for historic residences.",
        "director_portrait":
            "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=800&h=1100&fit=crop",
        "director_quote":
            "\"We do not choose residences for their price. We choose the residences that "
            "remain in our thoughts after a single visit. Eighty per cent of the properties "
            "offered to us are declined before entry to the collection.\"",
        "director_quote_attribution": "Alessandra Visconti di Modrone · Monocle · March 2025",

        # 4 private advisors
        "advisors_label":   "Private advisors",
        "advisors_heading": "A <em>single point of contact</em>, from the first dossier to the notary.",
        "advisors_intro":
            "Every client is accompanied personally by an advisor appointed at the beginning "
            "of the mandate. Never an intermediary, never a handover. Should the client wish "
            "for a second opinion, the studio makes a second advisor available in a "
            "consultative capacity, always under the same roof of discretion.",
        "advisors": [
            {
                "name":      "Francesco Medici di Porrena",
                "role":      "Senior advisor · Chianti & Val d'Orcia territory",
                "bio":
                    "Twelve years at Knight Frank Florence, specialising in the conservative "
                    "restoration of historic residences across Chianti Classico. Architecture "
                    "degree from Florence, master's from the Bartlett in London. He personally "
                    "handles all negotiations across southern Tuscany.",
                "territories":"Chianti Classico · Val d'Orcia · Florence",
                "since":     "With the studio since 2014",
                "portrait":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Italian · English · French",
            },
            {
                "name":      "Élodie Charbonneau",
                "role":      "Senior advisor · French Riviera & Capri territory",
                "bio":
                    "Ten years at Savills Paris and Christie's Real Estate Monte-Carlo. "
                    "Curator of private sales for French and American collectors along the "
                    "Côte d'Azur. Specialised in authentic Provençal mas and signature villas. "
                    "In charge of the Saint-Tropez concierge office.",
                "territories":"Saint-Tropez · Monaco · Capri",
                "since":     "With the studio since 2016",
                "portrait":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "French · English · Italian",
            },
            {
                "name":      "Arianna Testa Piccolomini",
                "role":      "Senior advisor · Portofino & Lago di Como territory",
                "bio":
                    "Eight years at Sotheby's International Realty Milan, then independent "
                    "adviser to two family offices in Brescia and Piedmont. A resident of "
                    "Portofino for ten years, she knows personally the historic families of "
                    "the promontory. Working languages: Italian, English, German.",
                "territories":"Portofino · Lago di Como · Milan",
                "since":     "With the studio since 2017",
                "portrait":
                    "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Italian · English · German",
            },
            {
                "name":      "Omar Khoury",
                "role":      "Private client advisor · Asian & Middle Eastern clients",
                "bio":
                    "Nine years between Knight Frank Dubai and Christie's Hong Kong. "
                    "Specialised in the reception of private clients from Hong Kong, "
                    "Singapore, Doha, Riyadh and Dubai. He coordinates translations and "
                    "international notarial certifications. Resident between Milan and "
                    "Portofino.",
                "territories":"Asian clients · Emirates · Persian Gulf",
                "since":     "With the studio since 2019",
                "portrait":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "العربية · English · French · 中文 (basic)",
            },
        ],

        # Legal / fiscal partner ribbon
        "partners_label":   "Institutional partners",
        "partners_heading": "The studio's <em>legal and fiscal</em> partners.",
        "partners_intro":
            "Villa Prestige does not draft deeds. Every negotiation is accompanied by "
            "selected institutional partners — notarial studios, international lawyers, "
            "private-wealth tax counsel — operating under the same roof of discretion. The "
            "client signs a direct mandate with them, separate from ours, with transparent fees.",
        "partners": [
            ("Studio Notarile Baldi-Corsini",     "Milan · notary to Lombard families"),
            ("Gattai Minoli Agostinelli",         "Milan · international real-estate law"),
            ("Chiomenti",                          "Milan · private-wealth taxation for family offices"),
            ("Ughi e Nunziante",                   "Rome · cultural-heritage authority"),
            ("Cabinet Bredin Prat",                "Paris · Côte d'Azur transactions"),
        ],

        # Press / editorial mentions
        "press_label":   "Editorial",
        "press_heading": "Recent mentions <em>of the studio.</em>",
        "press_items": [
            {
                "magazine": "Financial Times · How to Spend It",
                "issue":    "Spring 2026",
                "title":    "The quiet sellers of the Italian coast",
                "byline":   "Profile · by Bill Prince",
            },
            {
                "magazine": "Monocle",
                "issue":    "Issue 181",
                "title":    "The Chianti Classico revival",
                "byline":   "Reportage · by Josh Fehnert",
            },
            {
                "magazine": "Robb Report",
                "issue":    "April 2025",
                "title":    "Nine villas, one director",
                "byline":   "Profile · by Laurie Kahle",
            },
            {
                "magazine": "Corriere Living",
                "issue":    "January 2026",
                "title":    "The market for historic residences, as seen from Milan",
                "byline":   "Annual column · signed Alessandra Visconti di Modrone",
            },
            {
                "magazine": "AD Italia",
                "issue":    "November 2025",
                "title":    "Villa Aurelia · the return of a Portofino icon",
                "byline":   "Photography · Gianluca Ruotolo",
            },
        ],

        # Studio in numbers
        "numbers_label":   "The studio in figures",
        "numbers": [
            ("26",   "years since founding"),
            ("9",    "dedicated private advisors"),
            ("42",   "residences in collection"),
            ("7",    "territories of reference"),
            ("150",  "family offices served"),
            ("91",   "private transactions since 2015"),
        ],

        # Closing visit CTA
        "visit_label":     "In-office meeting",
        "visit_heading":   "A first <em>confidential conversation</em> in the Milan or Portofino offices.",
        "visit_text":
            "We receive exclusively by appointment, in the Milan and Portofino offices, or at "
            "the Saint-Tropez concierge office. The first meeting is a confidential "
            "conversation — it entails no mandate — during which we define the client profile "
            "and sign the non-disclosure agreement that opens access to the dossiers.",
        "visit_primary":      "Request the first conversation",
        "visit_primary_href": "concierge",
    },

    # ─── ESPERIENZA (services) — private-viewing process ─────
    "esperienza": {
        "eyebrow":  "The experience · five steps in discretion",
        "headline": "From the first <em>dossier</em> to the notary signature.",
        "intro":
            "We accompany the client through five stages, each confidential and documented. "
            "The path lasts on average four months for properties ready for signing, up to "
            "twelve for historic residences under landscape protection. No stage is obligatory "
            "— the client may close the mandate at any time, at no cost.",

        # 5-step private-viewing process
        "process_label":   "The pathway",
        "process_heading": "Five steps, <em>a single point of contact.</em>",
        "process_intro":
            "Every step is followed personally by the advisor appointed at the beginning of "
            "the mandate. The client may at any time request to speak with the direction — "
            "Alessandra Visconti di Modrone replies personally within one working day.",
        "process": [
            {
                "n":        "01",
                "title":    "Dossier request",
                "duration": "Reply within 48 working hours",
                "text":
                    "The client writes to the concierge describing the profile of the desired "
                    "residence — territory, provenance, surface, season of use. The territorial "
                    "advisor replies within two working days with a first summary of the "
                    "compatible collection and a proposal for a first meeting.",
            },
            {
                "n":        "02",
                "title":    "Non-disclosure agreement",
                "duration": "Signed in office or remotely",
                "text":
                    "Before the delivery of the full dossiers, client and studio sign a mutual "
                    "non-disclosure agreement binding both parties to absolute confidentiality "
                    "on the properties, on the selling families and on the economic terms. The "
                    "NDA is standard and does not preclude the assistance of a second fiscal "
                    "adviser.",
            },
            {
                "n":        "03",
                "title":    "Editorial videocall",
                "duration": "Half a day · with the advisor",
                "text":
                    "A first videocall meeting — or in-office if the client prefers — in which "
                    "we review together three or four editorial dossiers, with floorplans, "
                    "residence history, updated images, landscape report. The client selects "
                    "the two residences for the in-person viewing.",
            },
            {
                "n":        "04",
                "title":    "In-person private viewing",
                "duration": "One or two days on territory",
                "text":
                    "We personally accompany the client to the property, in the presence of "
                    "the resident point of contact and, if the selling family wishes, of the "
                    "latter. The viewing is without commercial pressure: it lasts the time "
                    "needed, includes lunch nearby, and may be repeated a second time in a "
                    "different season.",
            },
            {
                "n":        "05",
                "title":    "Negotiation and notary",
                "duration": "From 45 days to 6 months",
                "text":
                    "The studio drafts the purchase proposal in agreement with the client and "
                    "presents it directly to the selling family. The notarial partners prepare "
                    "the preliminary and final deeds. The advisor personally accompanies the "
                    "client to the notary signature and remains available for the following "
                    "six months, for every matter subsequent to handover.",
            },
        ],

        # Testimonial slot (single, editorial, discreet)
        "testimonial_label":   "Reference",
        "testimonial_text":
            "\"The studio was recommended to me by a former partner in London. I requested a "
            "first conversation in Milan and within six months we had acquired a villa in "
            "Costa Smeralda for our family, without the negotiation ever leaving the circle "
            "of the three people involved. The point of contact remains the same — today she "
            "also knows my children.\"",
        "testimonial_author":  "A Lombard family office · acquisition 2024 · Porto Cervo",

        # FAQ accordion
        "faq_label":   "Recurring questions",
        "faq_items": [
            {
                "q": "How long does the pathway to the notary signature take on average?",
                "a": "From four to twelve months, depending on the complexity of the property. "
                     "Residences ready for signing close in forty-five days; historic houses "
                     "under landscape protection or requiring land-registry subdivision take "
                     "longer for verifications with the heritage authority.",
            },
            {
                "q": "What are the working languages of the studio?",
                "a": "Italian, English and French in every negotiation. German for the Como "
                     "territory, basic Arabic and Chinese for Middle Eastern and Asian clients. "
                     "Sworn translations of all notarial documents are included in the mandate.",
            },
            {
                "q": "How is the studio's fee calculated?",
                "a": "Always as a percentage of the final purchase price, transparently stated "
                     "in the initial mandate. No fixed fee is due during the study phases — "
                     "only at the effective notary signature.",
            },
            {
                "q": "Does the studio also represent sellers?",
                "a": "Yes, but never simultaneously on the same residence. Each mandate is "
                     "exclusive to one of the two parties, to ensure full transparency in the "
                     "negotiation. The client always knows for whom we are working.",
            },
            {
                "q": "May a residence be visited more than once?",
                "a": "Yes, on request. We accompany the client, at no additional charge, for a "
                     "second viewing in a different season — many coastal properties are "
                     "visited once in summer and once in winter before a decision.",
            },
            {
                "q": "How do you safeguard confidentiality in the negotiation?",
                "a": "Every negotiation opens with a mutual non-disclosure agreement, signed "
                     "in office or remotely, binding the studio, the client and the selling "
                     "family. No dossier is accessible in open digital form — all documents "
                     "are delivered on a confidential platform or in printed form.",
            },
        ],

        # Closing CTA
        "cta_label":      "First conversation",
        "cta_heading":    "A <em>first conversation</em> is always at no charge and confidential.",
        "cta_text":
            "No mandate is due after the first meeting. The client receives a first summary "
            "of the compatible collection, a proposal of a dedicated advisor and an indicative "
            "date for the first private viewing. Should the profile not be compatible, we "
            "thank the client and take our leave — with no follow-up.",
        "cta_primary":      "Request the first conversation",
        "cta_primary_href": "concierge",
    },

    # ─── CONCIERGE (contact) — private-viewing request ───────
    "concierge": {
        "eyebrow":  "Private concierge · by appointment",
        "headline": "By <em>appointment</em> only.",
        "intro":
            "We receive exclusively by appointment, in the Milan and Portofino offices and at "
            "the Saint-Tropez concierge office. The concierge reads every request personally "
            "and replies within the following working day. For requests in Arabic, Chinese or "
            "German, the reply is signed directly by the advisor dedicated to the relevant "
            "territory.",

        # Dedicated phone line by territorio
        "phone_label":    "Concierge line by territory",
        "phone_intro":
            "Each territory has a dedicated line, open only to clients under NDA or "
            "introduced by a referral. For a first contact, it is always preferable to write "
            "to the concierge by email — the reply is faster and better documented.",
        "phone_rows": [
            ("Milan · direction",              "concierge@villaprestige.it"),
            ("Portofino · concierge office",   "portofino@villaprestige.it"),
            ("Saint-Tropez · concierge office","saint-tropez@villaprestige.it"),
            ("Asian clients · Omar Khoury",    "asia@villaprestige.it"),
        ],

        # Form section (private-viewing request with NDA consent)
        "form_section_label":  "Private viewing request",
        "form_section_intro":
            "Please complete the required fields. The concierge will reply within the "
            "following working day, in Italian, English or French. For requests in other "
            "languages, please indicate your preference in the notes field.",

        "form_helper_required":  "Fields marked are required",
        "form_submit_button":    "Send confidential request",
        "form_submit_note":
            "Your request is read personally by the concierge to the direction. No "
            "newsletter, no commercial communication. Data is deleted within ninety days "
            "should the profile not be compatible with the collection.",

        "form_fields": [
            {"name":"titolo",    "label":"Title", "type":"select", "required":True,
             "options":["Ms.","Mr.","Studio · family office","Press · editorial"]},
            {"name":"nome",      "label":"Full name", "type":"text",
             "placeholder":"e.g. Ms Eleonora Visconti", "required":True},
            {"name":"email",     "label":"Confidential email", "type":"email",
             "placeholder":"e.visconti@example.com", "required":True},
            {"name":"telefono",  "label":"Telephone (optional)", "type":"tel",
             "placeholder":"+39 …", "required":False},
            {"name":"sede",      "label":"Preferred office", "type":"select", "required":True,
             "options":["Milan · Montenapoleone","Portofino · concierge","Saint-Tropez · concierge","Preliminary videocall","No preference"]},
            {"name":"territorio","label":"Territory of interest", "type":"select", "required":True,
             "options":["Portofino · Liguria","Chianti Classico · Tuscany","Costa Smeralda · Sardinia","Lago di Como · Lombardy","Saint-Tropez · French Riviera","Capri · Campania","Val d'Orcia · Tuscany","Two or more territories"]},
            {"name":"profilo",   "label":"Residence profile", "type":"select", "required":True,
             "options":["Historic residence with park","Urban attic or penthouse","Contemporary signature villa","Agricultural estate with vineyard","Coastal property","No predetermined profile"]},
            {"name":"date",      "label":"Preferred dates", "type":"text",
             "placeholder":"e.g. second week of May · or seasonal entry", "required":False},
            {"name":"note",      "label":"Notes for the concierge", "type":"textarea",
             "placeholder":"Please indicate preferred language, referral source, family availabilities.", "required":True, "rows":5},
            {"name":"nda",       "label":"I consent to signing a mutual non-disclosure agreement prior to the delivery of the editorial dossiers", "type":"checkbox", "required":True},
        ],

        # Office cards — three concierge offices
        "offices_label":   "The offices",
        "offices_heading": "Three offices, <em>three reserved rooms.</em>",
        "offices_intro":
            "Every office receives only by appointment, in a reserved room with a local "
            "editorial archive. The Milan office is the general direction; Portofino and "
            "Saint-Tropez are attended in season by the resident points of contact.",
        "offices": [
            {
                "city":    "Milan",
                "address": "Via Montenapoleone 17 · 20121 Milan",
                "hours":   "Mon – Fri · 10:00 – 19:00 · by appointment only",
                "email":   "concierge@villaprestige.it",
                "role":    "Direction · central archive · in-office meetings",
            },
            {
                "city":    "Portofino",
                "address": "Via Roma 28 · 16034 Portofino GE",
                "hours":   "Apr – Oct · viewings by appointment · November – March on request",
                "email":   "portofino@villaprestige.it",
                "role":    "Concierge office · resident point of contact · Liguria",
            },
            {
                "city":    "Saint-Tropez",
                "address": "Place de la Garonne 6 · 83990 Saint-Tropez",
                "hours":   "May – Sep · viewings by appointment · October – April on request",
                "email":   "saint-tropez@villaprestige.it",
                "role":    "Concierge office · resident point of contact · Côte d'Azur",
            },
        ],

        # Press contact ribbon
        "press_contact_label":   "Press enquiries",
        "press_contact_text":
            "For editorial and specialised-press enquiries, please write directly to the "
            "direction: stampa@villaprestige.it. Press releases, photographic portfolios and "
            "interviews are coordinated personally by the director. We reply to the "
            "international press within one working day, in Italian, English or French.",
        "press_contact_email":   "stampa@villaprestige.it",
    },

    # ─── BLOG POSTS (used by collezione blog_list + blog_detail) ──
    # These render the signature properties as editorial dossiers.
    "posts": [
        {
            "slug":     "villa-aurelia-portofino",
            "kicker":   "Portofino · Liguria · 1920s",
            "title":    "Villa Aurelia — a 1922 historic residence on the promontory",
            "lede":
                "Four hundred square metres above the Tigullio gulf, a three-hectare park, a signed "
                "library and an infinity pool suspended above the Palmaria island.",
            "date":     "12 April 2026",
            "read_min": "7",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 03 / 18 · spring 2026"),
                ("Territory",   "Portofino · Liguria · Tigullio gulf"),
                ("Surface",     "400 m² internal · park 30,000 m² · 7 bedrooms"),
                ("Provenance",  "1922 · Marcello Piacentini signature · restoration A. Citterio 2014"),
                ("Availability","Three-day window · by appointment"),
                ("Price",       "Upon application to the point of contact"),
            ],
            "body": [
                ("p",
                 "The residence opens its carriage gate onto a shaded drive of centuries-old holm "
                 "oaks and reveals itself only after three hundred metres, set above the Tigullio "
                 "gulf at a height of sixty metres. The plan is horseshoe-shaped, with a central "
                 "body from 1922 and two wings added in 1938 by the same hand of Marcello "
                 "Piacentini. The 2014 intervention — directed by Antonio Citterio with the "
                 "landscape architect Paolo Pejrone for the park — preserved every original fresco "
                 "of the central salon, restored the solid-wood window frames and introduced the "
                 "infinity pool now among the iconic images of the promontory."),
                ("h2", "The park · three hectares of holm oaks, olives and camellias"),
                ("p",
                 "The park, originally designed by Count Ricci in 1924 and revised by Paolo "
                 "Pejrone in 2014, alternates centuries-old holm oaks, productive olive groves "
                 "and a collection of thirty-two camellia varieties. The residence has a private "
                 "staircase descending directly to the sea, with a mooring for craft up to eight "
                 "metres. The garden is entirely self-sufficient in irrigation, thanks to a "
                 "rainwater cistern restored in 2018."),
                ("h2", "Interiors · a signed library and a salon of reception"),
                ("p",
                 "On the piano nobile unfold the central salon of 140 square metres, with "
                 "original Ligurian-school frescoes, a dining room facing the sea and the "
                 "signed library with walnut boiseries designed in 1938. On the first floor, "
                 "the master suite occupies the entire east wing, with a private bath in "
                 "Carrara marble and a terrace facing the Palmaria island. Six further "
                 "bedrooms are distributed across the first and second floors, each with its "
                 "own bath."),
                ("blockquote",
                 "« The Portofino villa is not a property: it is a gesture of reserve, passed "
                 "between families that trust one another. Our role is merely to safeguard "
                 "the passage. »"),
                ("h2", "Provenance · Piacentini's hand, Citterio's restoration"),
                ("p",
                 "Commissioned in 1921 from the architect Marcello Piacentini by the Genoese "
                 "Acquarone family — then already the author of several interventions on the "
                 "Viareggio seafront — Villa Aurelia was completed in 1922 and remained in the "
                 "same family for three generations. It passed in 2007 to a second Milanese "
                 "family, which in 2014 commissioned Antonio Citterio for the conservative "
                 "restoration, with Paolo Pejrone for the park. The intervention has been "
                 "published in AD Italia, Elle Decor and Corriere Living."),
                ("ol", [
                    "Access: private drive with carriage gate, landscape supervision from the Genoa heritage authority.",
                    "Park: three hectares · private staircase to the sea · mooring for craft up to eight metres.",
                    "Internal surface: four hundred square metres · seven bedrooms · Carrara-marble bathrooms.",
                    "Systems: geothermal heating · low-visual-impact photovoltaic array · rainwater cistern.",
                    "Price: upon application to the point of contact · NDA required before the full dossier.",
                ]),
                ("p",
                 "Availability is limited to three days per month for private viewings, in the "
                 "presence of the owning family. The territorial advisor — Arianna Testa "
                 "Piccolomini, resident in Portofino for ten years — accompanies the client "
                 "personally from the first videocall to the notary signature."),
            ],
            "footer_strap": "Villa Prestige · Portofino · dossier N° 03 / 18",
        },
        {
            "slug":     "castello-di-montero-chianti",
            "kicker":   "Chianti Classico · Tuscany · 12th century",
            "title":    "Castello di Monterò — a medieval fortress with a working vineyard",
            "lede":
                "One thousand two hundred square metres across eighteen hectares, a Chianti "
                "Classico vineyard in biodynamic cultivation, an underground cellar and a "
                "consecrated chapel from 1432.",
            "date":     "5 April 2026",
            "read_min": "9",
            "author":   "Francesco Medici di Porrena",
            "image":
                "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 07 / 18 · spring 2026"),
                ("Territory",   "Chianti Classico · Tuscany · Gaiole in Chianti"),
                ("Surface",     "1,200 m² internal · 18 hectares · 7 hectares of vineyard"),
                ("Provenance",  "12th century · conservative restoration Tobia Scarpa 2014"),
                ("Availability","Exclusive · a single active mandate"),
                ("Price",       "Upon application to the point of contact"),
            ],
            "body": [
                ("p",
                 "The castle stands on a ridge at 520 metres of altitude between Gaiole in "
                 "Chianti and Radda, facing south over the Arbia valley and north over the "
                 "hills of San Polo. The central body, with its 1185 watchtower, has remained "
                 "substantially intact since its original construction; the 2014 restoration, "
                 "conducted by Tobia Scarpa under the supervision of the Florence heritage "
                 "authority, rendered the one thousand two hundred internal square metres "
                 "habitable without altering a stone of the medieval shell."),
                ("h2", "The estate · eighteen hectares, a biodynamic working vineyard"),
                ("p",
                 "The property extends across eighteen hectares, of which seven are dedicated "
                 "to a Chianti Classico DOCG vineyard, in certified biodynamic cultivation "
                 "since 2016. Annual production is approximately fifteen thousand bottles, "
                 "distributed exclusively on private allocation — never on the market. The "
                 "underground cellar, carved beneath the central body, houses thirty barriques "
                 "and a historic collection of two thousand bottles."),
                ("h2", "The central body · hall of arms and 1432 chapel"),
                ("p",
                 "On the ground floor unfold the hall of arms of 180 square metres, the "
                 "private chapel consecrated in 1432 (still in annual use on 24 June, the "
                 "patron's feast day) and the historic kitchen with original wood-fired oven. "
                 "The first floor houses the family library with three thousand volumes, five "
                 "master bedrooms, two sitting rooms. On the second floor, the watchtower has "
                 "been transformed into a private studio with a three-hundred-and-sixty-degree "
                 "view over the valley."),
                ("blockquote",
                 "« The castle is not for sale because the family needs money. It is for sale "
                 "because the next generation lives between London and Shanghai, and we feel "
                 "the need to pass it on to those who will carry it forward. »"),
                ("h2", "Provenance · seven centuries, two families"),
                ("p",
                 "Documented since 1185 in the Sienese notarial records, the castle was for "
                 "four hundred years a stronghold of the Ricasoli family, then of the "
                 "Pannocchieschi from 1570, finally of the present Medici di Porrena family "
                 "since 1812. The decision to entrust the mandate to Villa Prestige arises "
                 "from the thirty-year personal bond between the family and the senior advisor "
                 "Francesco Medici di Porrena — cousin of the same family and the studio's "
                 "advisor for Chianti Classico."),
                ("ol", [
                    "Access: private gravel drive of one kilometre, UNESCO landscape protection under evaluation.",
                    "Park and vineyard: eighteen hectares · seven in biodynamic Chianti Classico · olive grove of two thousand centuries-old trees.",
                    "Internal surface: one thousand two hundred square metres · ten bedrooms · chapel consecrated 1432.",
                    "Cellar: underground beneath the central body · thirty barriques · historic collection of two thousand bottles.",
                    "Systems: biomass heating · low-visual-impact photovoltaic array · water from a private spring.",
                    "Price: upon application to the point of contact · absolute exclusive until autumn 2026.",
                ]),
                ("p",
                 "Availability is limited to a single day per month for private viewings, "
                 "directly with the family and the advisor. The purchase pathway requires at "
                 "least six months for verifications with the Florence heritage authority and "
                 "the Tuscany region. The transfer of the vineyard agricultural mandate is "
                 "coordinated with the Chianti Classico consortium."),
            ],
            "footer_strap": "Villa Prestige · Chianti Classico · dossier N° 07 / 18",
        },
        {
            "slug":     "penthouse-quadronno-milano",
            "kicker":   "Milan · Magenta · sole top-floor",
            "title":    "Penthouse Quadronno — a 1957 top-floor apartment facing the Duomo",
            "lede":
                "Three hundred and eighty square metres on the sixth floor of via Quadronno, a "
                "180 m² terrace, a head-on view of the Duomo, interiors signed Vico Magistretti "
                "in 1958.",
            "date":     "28 March 2026",
            "read_min": "6",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 11 / 18 · spring 2026"),
                ("Territory",   "Milan · Magenta · via Quadronno"),
                ("Surface",     "380 m² internal · terrace 180 m² · 4 bedrooms"),
                ("Provenance",  "1957 · Luigi Caccia Dominioni signature · interiors Vico Magistretti 1958"),
                ("Availability","By appointment"),
                ("Price",       "Upon application to the point of contact"),
            ],
            "body": [
                ("p",
                 "The penthouse occupies the entire sixth floor of the Quadronno building, "
                 "erected in 1957 to a design by Luigi Caccia Dominioni for a private client of "
                 "the Milanese industrial bourgeoisie. The interiors were completed ten months "
                 "later by Vico Magistretti, then thirty-three years old, with a work of "
                 "detailed craftsmanship on woods, marbles and handles which remains today "
                 "intact in its original integrity."),
                ("h2", "The plan · three hundred and eighty articulated square metres"),
                ("p",
                 "The entrance opens onto a gallery eighteen metres long which distributes the "
                 "two wings of the apartment — day zone to the south-east, night zone to the "
                 "north-west. The main salon of one hundred and ten square metres faces the "
                 "Duomo head-on through a Jacopo Foggini glass panel installed in 2018. The "
                 "dining room, the professional kitchen and the pantry complete the day wing. "
                 "Four bedrooms, each with a private bathroom in original 1957 Carrara marble, "
                 "compose the night wing."),
                ("h2", "The terrace · one hundred and eighty wrap-around square metres"),
                ("p",
                 "The perimeter terrace, one hundred and eighty square metres in total, offers "
                 "a three-hundred-and-sixty-degree view of the city: Duomo to the east, "
                 "Castello Sforzesco to the north, San Siro on the western horizon. Patricia "
                 "Urquiola's landscape intervention in 2019 added a covered whirlpool, a "
                 "terracotta-tiled pergola and a collection of fifteen Mediterranean aromatic "
                 "varieties."),
                ("blockquote",
                 "« The Quadronno is not a penthouse: it is a small museum of the 1950s "
                 "Milanese home. Every detail of Magistretti is in its place. »"),
                ("h2", "Provenance · Caccia Dominioni, Magistretti, Urquiola"),
                ("p",
                 "Commissioned in 1956 by the Brambilla family from Luigi Caccia Dominioni, "
                 "completed in 1957. Vico Magistretti's interiors were delivered in 1958 and "
                 "have undergone no significant alteration for sixty years. In 2018, the "
                 "second owning family commissioned Jacopo Foggini for the front glass panel; "
                 "in 2019, the landscape intervention on the terrace was signed by Patricia "
                 "Urquiola. All interventions have been documented in Domus, Interni and "
                 "Corriere Living."),
                ("ol", [
                    "Access: portered entrance of a building of high prestige · dedicated service lift.",
                    "Internal surface: three hundred and eighty square metres · four bedrooms · original 1957 marble bathrooms.",
                    "Terrace: one hundred and eighty square metres · covered whirlpool · terracotta Urquiola pergola 2019.",
                    "View: head-on over the Duomo of Milan · three-hundred-and-sixty-degree panorama.",
                    "Systems: autonomous heating · independent wing-by-wing climate control.",
                    "Price: upon application to the point of contact · NDA required before the full dossier.",
                ]),
                ("p",
                 "Availability is open by appointment. The average purchase pathway is of "
                 "forty-five days from NDA to notary signature, thanks to the complete and "
                 "already updated land-registry documentation. The selling family is available "
                 "for a direct meeting before the notary signature."),
            ],
            "footer_strap": "Villa Prestige · Milan · dossier N° 11 / 18",
        },
        {
            "slug":     "mas-de-la-mer-saint-tropez",
            "kicker":   "Saint-Tropez · Côte d'Azur · 18th century",
            "title":    "Mas de la Mer — a 1754 Provençal mas with an AOP vineyard",
            "lede":
                "Five hundred and fifty square metres on the hills of Ramatuelle, a private "
                "Côtes de Provence AOP vineyard, an original 1754 construction restored in 2017.",
            "date":     "20 March 2026",
            "read_min": "8",
            "author":   "Élodie Charbonneau",
            "image":
                "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 14 / 18 · spring 2026"),
                ("Territory",   "Saint-Tropez · Côte d'Azur · Ramatuelle"),
                ("Surface",     "550 m² internal · 6 hectares · vineyard 2.5 ha"),
                ("Provenance",  "1754 · original Provençal mas · restoration François Catroux 2017"),
                ("Availability","Newly released · just entered the collection"),
                ("Price",       "Upon application to the point of contact"),
            ],
            "body": [
                ("p",
                 "The mas stands on the inland hills of Ramatuelle, twelve kilometres from the "
                 "port of Saint-Tropez, in a silence only the inland Var can offer. The "
                 "original construction is of 1754, belonging to the same family of viticultural "
                 "tradition until 1948. Acquired in 1985 by a Parisian family, it was restored "
                 "in 2017 by François Catroux — the French architect's last private work before "
                 "his passing — with the aim of returning the interiors to their original "
                 "simplicity, after fifty years of uneven interventions."),
                ("h2", "The vineyard · two and a half hectares of Côtes de Provence AOP"),
                ("p",
                 "The property includes two and a half hectares of working AOP Côtes de "
                 "Provence vineyard, with vinification entrusted to Domaine Ott for the rosé "
                 "and to Domaine Tempier for the red. Annual production is approximately seven "
                 "thousand bottles, distributed exclusively to the owning family and its "
                 "guests. The cellar stands directly beneath the mas, in an underground space "
                 "dating from 1802."),
                ("h2", "Interiors · a double-volume salon and a master bedroom"),
                ("p",
                 "The ground floor is articulated around a double-volume salon of one hundred "
                 "and twenty square metres, with an original corner stone fireplace and "
                 "exposed oak beams. The kitchen is vaulted, paved in Salernes terracotta. On "
                 "the first floor, the master bedroom occupies the entire south wing with a "
                 "private bath in Caunes-Minervois marble; three further double bedrooms, each "
                 "with its own bath, complete the floor. The guardian's cottage houses an "
                 "apartment for custodian or guests."),
                ("blockquote",
                 "« François Catroux returned to the mas the slowness that the inland Var has "
                 "always known. It is his last private work, and it shows. »"),
                ("h2", "Provenance · from viticulture to the Parisian family"),
                ("p",
                 "Built in 1754 by the Bertrand family, who held it for six generations "
                 "cultivating the vineyard and producing olive oil, the mas passed to the "
                 "Parisian Armand family in 1948. Restored for the first time in 1985 by "
                 "Madeleine Castaing in a rich, ornate style, it was returned to its original "
                 "sobriety in 2017 by François Catroux's restoration. The work has been "
                 "published in Architectural Digest France and in Le Monde d'Hermès."),
                ("ol", [
                    "Access: private white-gravel drive of two hundred metres · original 1754 iron gate.",
                    "Park: six hectares · two and a half AOP vineyard · centuries-old olive grove · natural stone pool.",
                    "Internal surface: five hundred and fifty square metres · four bedrooms · guardian's cottage.",
                    "Vineyard: Côtes de Provence AOP · vinification Domaine Ott and Tempier · production seven thousand bottles.",
                    "Systems: pellet heating · gentle climate control · water from a private spring.",
                    "Price: upon application to the point of contact · NDA required before the full dossier.",
                ]),
                ("p",
                 "Availability opens by appointment from the next viewing season — mid-May. "
                 "The vineyard's agricultural mandate is transferred together with the real-"
                 "estate notary signature; the subsequent transfer of the AOP denomination "
                 "mark is coordinated with Domaine Ott. The average purchase pathway is of "
                 "four months from NDA to the French notary signature."),
            ],
            "footer_strap": "Villa Prestige · Saint-Tropez · dossier N° 14 / 18",
        },
        # Four shorter dossiers to round out the collezione list
        {
            "slug":     "villa-lario-tremezzo",
            "kicker":   "Lago di Como · Tremezzo · Nineteenth century",
            "title":    "Villa Lario — an 1862 lakeside residence with a private boathouse",
            "lede":
                "Four hundred and fifty square metres at lake level, a two-and-a-half-hectare park, "
                "a private boathouse for craft up to fifteen metres.",
            "date":     "15 March 2026",
            "read_min": "5",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 04 / 18 · spring 2026"),
                ("Territory",   "Lago di Como · Tremezzo"),
                ("Surface",     "450 m² internal · park 25,000 m² · private boathouse"),
                ("Provenance",  "1862 · nineteenth-century villa · restoration Lissoni 2020"),
                ("Availability","By appointment"),
                ("Price",       "Upon application to the point of contact"),
            ],
            "body": [
                ("p",
                 "Villa Lario stands at lake level on Lago di Como, five minutes from the "
                 "piazzetta of Tremezzo and ten minutes by motor launch from Villa d'Este. "
                 "The original construction is of 1862, for a Milanese family of the Lombard "
                 "industrial bourgeoisie. The conservative restoration of 2020, conducted by "
                 "the Lissoni Casal Ribeiro studio, has preserved intact the nineteenth-century "
                 "decorations of the main salon, the original boiseries and the internal "
                 "staircase in Candoglia marble."),
                ("h2", "The park and the boathouse · private access to the Lake"),
                ("p",
                 "The park extends over two and a half hectares sloping towards the Lake, "
                 "with an original Italian garden from 1875, a fish pond, a portico of "
                 "centuries-old jasmines. The private boathouse, original from 1870 and "
                 "restored in 2020, houses craft up to fifteen metres in length and is "
                 "equipped with an electric crane for winter lift-out. A stone staircase "
                 "descends directly from the main salon to the Lake belvedere."),
                ("ol", [
                    "Access: state road · private gate with porter's lodge.",
                    "Park: two and a half hectares · Italian garden · private boathouse.",
                    "Internal surface: four hundred and fifty square metres · five bedrooms · library.",
                    "Price: upon application to the point of contact · NDA required before the dossier.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Lago di Como · dossier N° 04 / 18",
        },
        {
            "slug":     "casa-delle-torri-porto-cervo",
            "kicker":   "Costa Smeralda · Porto Cervo · 1970s",
            "title":    "Casa delle Torri — a 1972 Jacques Couëlle villa",
            "lede":
                "Six hundred and twenty square metres on a private promontory, original design "
                "by Jacques Couëlle, terraces above the sea and direct access to a private bay.",
            "date":     "8 March 2026",
            "read_min": "6",
            "author":   "Élodie Charbonneau",
            "image":
                "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 08 / 18 · spring 2026"),
                ("Territory",   "Costa Smeralda · Porto Cervo"),
                ("Surface",     "620 m² internal · private promontory · bay"),
                ("Provenance",  "1972 · Jacques Couëlle signature · restoration A. Citterio 2018"),
                ("Availability","By appointment"),
                ("Price",       "Upon application to the point of contact"),
            ],
            "body": [
                ("p",
                 "Designed in 1972 by Jacques Couëlle for a Belgian family, Casa delle Torri "
                 "is one of the few villas fully surviving from the organic Smeraldine design. "
                 "The 2018 restoration conducted by Antonio Citterio preserved the absolute "
                 "integrity of the local-granite shell and the juniper roofs, introducing "
                 "invisible systems and a contemporary kitchen within the cottage."),
                ("ol", [
                    "Access: private consortium drive · Porto Cervo porter's lodge.",
                    "Terraces: three levels above the sea · private bay reachable on foot.",
                    "Surface: six hundred and twenty square metres · six bedrooms · staff cottage.",
                    "Price: upon application to the point of contact.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Costa Smeralda · dossier N° 08 / 18",
        },
        {
            "slug":     "casa-canapa-capri",
            "kicker":   "Capri · Anacapri · 1930s",
            "title":    "Casa Canapa — a Caprese villa facing the Faraglioni",
            "lede":
                "Two hundred and twenty square metres across three levels, stacked terraces "
                "towards the Faraglioni, a garden of centuries-old lemon trees, pedestrian access "
                "from the centre of Anacapri.",
            "date":     "1 March 2026",
            "read_min": "5",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 15 / 18 · spring 2026"),
                ("Territory",   "Capri · Anacapri"),
                ("Surface",     "220 m² internal · 3 terraces · garden 800 m²"),
                ("Provenance",  "1934 · original Caprese villa · three generations one family"),
                ("Availability","By appointment"),
                ("Price",       "Upon application to the point of contact"),
            ],
            "body": [
                ("p",
                 "Casa Canapa is an authentic Caprese villa of 1934, passed for three "
                 "generations within the same Neapolitan family. The original design is in "
                 "the Caprese tradition — vaults, pendentives, majolica-tiled external "
                 "staircases — and has undergone no substantial intervention. The ordinary "
                 "upkeep, entrusted to the Caprese craftsmen of a lifetime, has preserved "
                 "intact the island character of the house."),
                ("ol", [
                    "Access: pedestrian only · five minutes on foot from the piazzetta of Anacapri.",
                    "Terraces: three stacked levels · view over the Faraglioni of Capri.",
                    "Surface: two hundred and twenty square metres · four bedrooms.",
                    "Price: upon application to the point of contact.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Capri · dossier N° 15 / 18",
        },
        {
            "slug":     "pieve-di-santorso-val-dorcia",
            "kicker":   "Val d'Orcia · Montalcino · 12th century",
            "title":    "Pieve di Sant'Orso — a UNESCO estate with a Brunello vineyard",
            "lede":
                "Eight hundred square metres between Romanesque parish church and farmhouse, "
                "twenty-two hectares of UNESCO heritage, a working Brunello di Montalcino DOCG "
                "vineyard.",
            "date":     "22 February 2026",
            "read_min": "7",
            "author":   "Francesco Medici di Porrena",
            "image":
                "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("Collection",  "N° 17 / 18 · spring 2026"),
                ("Territory",   "Val d'Orcia · Montalcino"),
                ("Surface",     "800 m² internal · 22 ha UNESCO · vineyard 4 ha"),
                ("Provenance",  "12th century · Romanesque parish · restoration Matteo Nunziati 2019"),
                ("Availability","Exclusive"),
                ("Price",       "Upon application to the point of contact"),
            ],
            "body": [
                ("p",
                 "The Sant'Orso estate extends over twenty-two hectares of UNESCO heritage in "
                 "Val d'Orcia, between Montalcino and San Quirico d'Orcia. The historic core "
                 "includes the Romanesque parish church of 1182 — still consecrated, in "
                 "annual use once a year — and the original 1620 farmhouse, restored in 2019 "
                 "by Matteo Nunziati. The Brunello di Montalcino DOCG vineyard occupies four "
                 "hectares, in certified organic cultivation, with vinification entrusted to "
                 "the neighbouring estate."),
                ("ol", [
                    "Access: municipal white-gravel road of two kilometres · UNESCO protection.",
                    "Estate: twenty-two hectares · vineyard four hectares · olive grove of eight hundred trees.",
                    "Internal surface: eight hundred square metres · Romanesque parish · six bedrooms.",
                    "Price: upon application to the point of contact · absolute exclusive.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Val d'Orcia · dossier N° 17 / 18",
        },
    ],
}


# D-047 · all chrome labels flow from site/page_data above — no string
# should ever be hardcoded in the skin or preview composition HTML.
