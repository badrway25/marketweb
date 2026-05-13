"""Content tree · `madou-pasticceria` · T50 multilingual rollout (EN).

English translation of `MADOU_CONTENT_IT`. Built for the marketweb T50
multilingual pass (IT → EN/FR/ES/AR · AAA walk · public flip). Shape
parity contract enforced against `template_content_madou.py`:

  * Same top-level keys, same nested keys at every depth.
  * Same list lengths (5 lievitati signature courses, 8 menu courses,
    4 produttori, 4 atmosphere images, 4 riconoscimenti, etc.).
  * Same tuple positions for tuple-typed values.
  * Same `pages[].slug` values (labels translated, slugs preserved).
  * Same `posts[].slug` values, same `page kind`.

Voice anchor — `slow proofing` (pastry-craft register · Food52 /
Cherry Bombe / King Arthur Flour artisan-baker idiom) carries the
IT `lievitazione lenta` load-bearing promise across the same surfaces
(hero H1 with `<em>` italic emphasis, manifesto, cta_heading, forno
headline/values, pasticceria intro, ordina, produttori + signature
courses copy). Italian heritage proper-names (Torino, Borgo Po,
Pierre Marchais, Famiglia Brero, Olivier Domori, Anna Negroni,
Carla Madou, Tommaso Rinaldi, Iginio Massari, Pierre Hermé, Cuneo
IGP, Val Susa, Isigny-sur-Mer, Sambirano, Mortara, Domori Criollo,
Marrone IGP, Nocciola Piemonte IGP, Gambero Rosso Pasticcerie,
AMPI, Coppa del Mondo Pasticceria, Identità di Pasticceria,
Dissapore, Cook Corriere, Vogue Cibo, Erbaluce passito Cieck,
Caffè Vergnano, Damman, Inalpi, Caffè Al Bicerin) preserved
verbatim. Brand name `Madou · Pasticceria Atelier` preserved.
Pastry product names (Croissant viennoise, Maritozzo, Millefoglie,
Bignè, Saint Honoré, Mont-Blanc, Tarte au chocolat, Macarons,
Pasta sfoglia, Bicerin) kept as Italian/French loanwords.
"""

from typing import Any


MADOU_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",         "label": "Home",          "kind": "home"},
        {"slug": "forno",        "label": "The oven",      "kind": "about"},
        {"slug": "pasticceria",  "label": "Patisserie",    "kind": "menu"},
        {"slug": "vetrina",      "label": "Window",        "kind": "gallery"},
        {"slug": "diario",       "label": "Journal",       "kind": "blog_list"},
        {"slug": "ordina",       "label": "Orders",        "kind": "reservations"},
    ],

    "site": {
        "logo_initial":  "MD",
        "logo_word":     "Madou",
        "tag":           "Pasticceria Atelier · Torino Borgo Po · since 2011",
        "phone":         "+39 011 8195 770",
        "email":         "atelier@madou-pasticceria.it",
        "address":       "Via Sant'Ottavio 36 · 10124 Torino",
        "hours_compact": "Tue – Sat · 7:30 AM – 7:30 PM · Sun 7:30 AM – 1:00 PM",
        "star_line":     "★ Tre Torte · Gambero Rosso · 2023 · 2024 · 2025",
        "footer_intro":
            "Fifteen years of slow proofing. One open workroom on the street, "
            "a window of raw dough, two stone-deck ovens. No industrial "
            "pre-mixes, no frozen blanks, no shortcuts.",
        "footer_hours_1": "Tue – Sat · 7:30 AM – 7:30 PM",
        "footer_hours_2": "Sun · 7:30 AM – 1:00 PM · Mon · closed",
        "copyright": "© 2026 Madou Atelier S.r.l. · VAT 11237680016",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        # T49: hero plate URL threaded into the fine-dining template via
        # page_data so Madou swaps Gusto's plated-dish hero for the
        # pasticceria vetrina without forking home.html. URL from X.3
        # curator pack `bakery-pasticceria.md` (Pexels CC0-compatible).
        "hero_plate_url":
            "https://images.pexels.com/photos/19288569/pexels-photo-19288569.jpeg"
            "?auto=compress&cs=tinysrgb&w=1600",
        "eyebrow":  "Pasticceria Atelier · Torino Borgo Po · since 2011",
        "headline": "Twelve hours of <em>slow proofing,</em> a laminated pastry you can hear rising.",
        "intro":
            "Cold-laminated pastries, natural leavening with mother dough "
            "refreshed every twelve hours, creams whipped to order. The "
            "window changes each day according to what came out of the oven "
            "at dawn.",
        "primary_cta":   "Pre-order Saturday's pastry",
        "primary_href":  "ordina",
        "secondary_cta": "The pastry chef",
        "secondary_href":"forno",

        # Repurposed labels (Gusto's "chef" → Madou's "pasticciera")
        "chef_label":    "The pastry chef",
        "star_tag":      "★ Tre Torte · Gambero Rosso 2025",
        "photo_label":   "Photography",
        "cuisine_label": "Pastry chef",

        "facts": [
            ("12 h", "minimum proofing · pasta sfoglia"),
            ("3",    "live mother starters in the atelier · since 2011"),
            ("0",    "industrial pre-mixes · 0 frozen blanks · 0 ready-mixes"),
        ],

        "manifesto_drop_cap": "W",
        "manifesto":
            "hen a sheet of laminated dough goes into the oven, work at "
            "Madou stops for four minutes and everyone listens. The sound "
            "of the dough rising — the air bubbles releasing between the 64 "
            "layers of laminated pastry — is the first sign of whether that "
            "batch will sell on Saturday morning or go to the brigade. No "
            "stopwatch, no thermometer: only the ear.",

        # Pasticceria signature — 5 "lievitati" (vs Gusto 5 "atti")
        "signature_courses": [
            ("I",    "Croissant viennoise",          "12 hours of slow proofing · 64 layers · Normandy butter from Isigny",       "Ethiopia Sidamo single-origin coffee"),
            ("II",   "Maritozzo with cream",         "24 hours of natural slow proofing · fresh cream whipped to order",          "Madagascar 72% hot chocolate"),
            ("III",  "Millefoglie with hazelnut",    "three layers of caramelised pasta sfoglia · Nocciola IGP chantilly cream",  "Traditional Torinese Bicerin"),
            ("IV",   "Bignè with Domori chocolate",  "house pâte à choux · 80% Criollo dark ganache",                             "Darjeeling First Flush black tea"),
            ("V",    "Saint Honoré with marroni",    "autumn seasonal · Cuneo IGP marroni · crème mousseline",                    "Erbaluce passito dessert wine"),
        ],

        # Persona — pasticciera Carla Madou
        "chef": {
            "name":  "Carla Madou",
            "role":  "Atelier pastry chef · class of 1979",
            "bio":
                "Torinese, born 1979. Four-year apprenticeship under Iginio "
                "Massari in Brescia, then two years with Pierre Hermé in "
                "Paris, finally two with Cristian Beduschi in Geneva. She "
                "opened Madou in 2011 in a former print shop in Borgo Po, "
                "with one single intuition: work only with live mother "
                "starters, refreshed every twelve hours.",
        },

        "courses_label": "Five slow-proofed pastries of the week · October '26",
        "courses_footline": "Living window — what you see came out of the oven this morning",
        "courses_full_cta": "The full patisserie",
        "chef_link_filosofia": "The oven and the hands",
        "chef_link_diario": "The flour journal",

        "press_label": "Featured in",
        "press": ["GAMBERO ROSSO PASTICCERIE", "DISSAPORE", "COOK CORRIERE",
                  "IDENTITÀ DI PASTICCERIA", "VOGUE CIBO"],

        # Ingredients/sourcing editorial band — pasticceria-specific
        "ingredienti": {
            "label":   "Raw materials",
            "heading": "Sixteen suppliers, <em>all on a first-name basis.</em>",
            "text":
                "The Madou supply chain is short and traceable line by "
                "line. The butter arrives from a Normandy dairy in "
                "Isigny-sur-Mer · the eggs from a farm sixty kilometres "
                "from Torino · the flours from a stone mill in Val Susa · "
                "the cacao from three single-origin plantations (Madagascar, "
                "Venezuela, Dominican Republic) selected in the field in 2019.",
            "image":
                "https://images.pexels.com/photos/28183472/pexels-photo-28183472.jpeg"
                "?auto=compress&cs=tinysrgb&w=1000",
            "image_caption":
                "Laminated pastry on the refrigerated marble · 5:30 AM shift",
        },

        # Atmosphere teaser — pasticceria-specific imagery
        "atmosphere_teaser": {
            "label": "The living window",
            "images": [
                ("https://images.pexels.com/photos/19288569/pexels-photo-19288569.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Saturday morning window"),
                ("https://images.pexels.com/photos/16140003/pexels-photo-16140003.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Hand-decoration · commissioned cake"),
                ("https://images.pexels.com/photos/30853716/pexels-photo-30853716.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Croissant viennoise fresh from the oven"),
                ("https://images.pexels.com/photos/31000323/pexels-photo-31000323.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Seasonal macarons · October '26"),
            ],
            "link_label": "Enter the window",
            "link_href":  "vetrina",
        },

        # Awards/recognition — pastry awards (not Michelin)
        "riconoscimenti": {
            "label": "Recognition",
            "items": [
                ("★★★", "Tre Torte · Gambero Rosso", "Annual award · 2023 · 2024 · 2025"),
                ("AMPI", "Accademia Maestri Pasticceri", "Member since 2017 · Brescia chapter"),
                ("CMP",  "Coppa del Mondo Pasticceria", "Italy team · alternate 2022 · 4th place Lyon"),
                ("DIS",  "Dissapore · 50 Pasticcerie", "First place Piemonte 2024 · top 5 Italy 2025"),
            ],
        },

        # CTA section
        "cta_heading": "Only slow proofing, <em>only what comes out of the oven each morning.</em>",
        "cta_primary":  "Pre-order Saturday's pastry",
        "cta_secondary": "Discover the full patisserie",

        # Seasonal highlight card — pasticceria seasonal
        "stagione": {
            "label":     "In the window now",
            "title":     "Autumn '26 patisserie",
            "subtitle":  "Marroni, persimmon, single-origin chocolate · from October 6",
            "text":
                "The autumn card opens on October 6 with the Saint Honoré "
                "with Cuneo IGP marroni, the millefoglie with astringent "
                "persimmon from the Bel Paese, and the 2026 Mont-Blanc in a "
                "single-portion version. The full autumn patisserie stays "
                "in the window until November 30, then the Christmas card "
                "begins.",
            "cta_label": "Discover the full autumn card →",
            "cta_href":  "pasticceria",
        },

        # Producer showcase — pastry supply chain (vs Gusto wine producers)
        "produttori": {
            "label":   "The suppliers",
            "heading": "Sixteen hands, <em>one single window.</em>",
            "intro":
                "Every Madou raw material has a supplier with a name, an "
                "address and a phone number. Butter, milk, eggs, flours, "
                "cacao, fruit, honey — nothing arrives from a catalogue. "
                "Every supplier has been visited personally by Carla at "
                "least once.",
            "items": [
                {
                    "portrait":
                        "https://images.pexels.com/photos/8477754/pexels-photo-8477754.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Pierre Marchais",
                    "role": "Normandy AOP butter",
                    "area": "Isigny-sur-Mer · Normandy",
                    "blurb":
                        "Isigny AOP butter arrives every Wednesday in a "
                        "refrigerated load at 4°C. Family dairy since 1932, "
                        "four Normande cows per hectare.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/8188937/pexels-photo-8188937.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Famiglia Brero",
                    "role": "Val Susa stone mill",
                    "area": "Bussoleno · Piemonte",
                    "blurb":
                        "Three-pass stone milling · 100% local soft "
                        "Bologna wheat · no refining. Three flour types, "
                        "one each month, all exclusive to the atelier.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/11869895/pexels-photo-11869895.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Olivier Domori",
                    "role": "Single-origin cacao",
                    "area": "Sambirano · Madagascar",
                    "blurb":
                        "Three plantations selected in the field by Carla "
                        "in 2019. 80% Criollo Trinitario cacao, cold-roasted "
                        "in Italy · each batch traced by lot.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/29198586/pexels-photo-29198586.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Anna Negroni",
                    "role": "Seasonal fruit · Cuneo",
                    "area": "Lagnasco · Piemonte",
                    "blurb":
                        "Cuneo IGP peaches in June · IGP marroni in "
                        "October · astringent persimmon in November. Eight "
                        "hectares, hand-picked, no cold storage.",
                },
            ],
        },

        # Repurposed `private_dining` → `eventi su misura` / cake design
        "private_dining": {
            "label":   "Bespoke events",
            "heading": "Cake design & <em>private commissions.</em>",
            "intro":
                "Madou accepts orders for ceremonial cakes, wedding cakes "
                "and small private productions for events. Three ways in, "
                "each with different lead times and prices.",
            "experiences": [
                {
                    "icon": "fork",
                    "title": "Commissioned cake",
                    "meta":  "Min. 8 portions · from €18 / portion",
                    "desc":
                        "Custom design built around three preliminary "
                        "meetings with Carla. Lead time: two weeks minimum. "
                        "We decorate only by hand — no industrial moulds.",
                },
                {
                    "icon": "door",
                    "title": "Wedding cake",
                    "meta":  "From 40 portions · from €22 / portion",
                    "desc":
                        "Four months of four-handed work with the couple. "
                        "Three taste trials included in the service. "
                        "Pickup at the atelier or refrigerated delivery "
                        "covered by Madou across central Piemonte.",
                },
                {
                    "icon": "wine",
                    "title": "Private buffet",
                    "meta":  "20 – 60 guests · from €38 / guest",
                    "desc":
                        "Mignon pastry only · 8 references, 150 pieces "
                        "minimum. Baking happens on the day of the event, "
                        "refrigerated delivery. Saturday afternoons we "
                        "keep free.",
                },
            ],
            "cta_label": "Write to the pastry chef",
            "cta_href":  "ordina",
        },

        # Repurposed `wine_program` → `lieviti madre` collection
        "wine_program": {
            "label":   "The mother starter archive",
            "heading": "Three live mother starters, <em>one single patisserie.</em>",
            "intro":
                "The atelier keeps three active mother starters, each with "
                "its own acidity signature and its own yield. Every Madou "
                "slow-proofed pastry is paired with the mother that belongs "
                "to it — no commercial yeast, no improvers.",
            "sommelier": {
                "name": "Tommaso Rinaldi",
                "role": "Master baker · mother dough lead",
                "bio":
                    "Carla's apprentice since 2014, responsible for the "
                    "refresh of the three mother doughs since 2018. He "
                    "refreshes every twelve hours, at 5:30 AM and 5:30 PM. "
                    "He keeps the flour memory of every batch.",
            },
            "pairings": [
                ("01", "Mother M-1 · laminated pastry",
                 "Active starter since 2011 · dominant lactic acidity · "
                 "pH 4.2 · fast folds, long rest. Used for croissants, "
                 "kouign-amann, brioche col tuppo.",
                 "12 – 16 h"),
                ("02", "Mother M-2 · panettoni and tall slow-proofed bakes",
                 "Mother born in 2014 from a triple refresh. Mixed "
                 "acetic-lactic acidity, pH 4.5 · aggressive vertical "
                 "development. Panettone, colomba and veneziana only.",
                 "36 – 48 h"),
                ("03", "Mother M-3 · pan brioche and sweet laminated bakes",
                 "Mother refreshed with chestnut honey · contained acidity, "
                 "pH 4.7 · scent of toasted hazelnut. Maritozzi, round "
                 "brioche, chocolate plait.",
                 "8 – 12 h"),
            ],
            "cellar_facts": [
                ("3",   "live mother starters"),
                ("12h", "fixed refresh cadence"),
                ("2011", "year of the first mother · M-1"),
            ],
        },
    },

    # ─── FORNO (about) — Gusto's "filosofia" page ────────────
    "forno": {
        "eyebrow":  "The oven",
        "headline": "Fifteen years of oven work, <em>one single promise of slow proofing.</em>",
        "intro":
            "Madou was born in 2011 in a former print shop in Borgo Po, "
            "Torino. The atelier has one single workroom open to the "
            "street and two stone-deck ovens. The promise is always the "
            "same: zero pre-mixes, zero frozen blanks, zero industrial "
            "ready-mixes. Only slow proofing, only traced raw materials.",

        "history": [
            ("2011",
             "Carla Madou opens the atelier on Via Sant'Ottavio after eight "
             "years between Brescia (Massari), Paris (Hermé) and Geneva "
             "(Beduschi). Four counter seats, two pastry references, one "
             "single mother — M-1, founded with flour from the Brero mill."),
            ("2014",
             "Tommaso Rinaldi joins as an apprentice and within three years "
             "becomes mother-starter lead. M-2, the panettone mother, is "
             "born from a triple refresh of M-1."),
            ("2017",
             "Carla is admitted to the Accademia Maestri Pasticceri Italiani "
             "(AMPI), the second Piemontese woman to enter after Sonia Balacchi."),
            ("2021",
             "The atelier moves to Via Sant'Ottavio 36, the fully restored "
             "former print shop. Three ovens, two laminators, a fifteen-metre "
             "linear window open to the street."),
            ("2023",
             "Gambero Rosso awards the Tre Torte (the highest pastry "
             "recognition) and confirms it in 2024 and 2025. Madou becomes "
             "a fixed stop on the Italian signature-pastry circuit."),
        ],

        "filosofia_image":
            "https://images.pexels.com/photos/30918889/pexels-photo-30918889.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400",
        "filosofia_image_caption": "The laboratory · Carla Madou at the laminator",

        "method_title": "Method",
        "method_paragraphs": [
            "Every Madou pastry starts from the mother refresh. At 5:30 AM "
            "Tommaso refreshes the three mother doughs and portions out the "
            "quantities for the day's mixes · at 5:30 PM he refreshes again "
            "for the overnight mixes. It is a fixed schedule, independent "
            "of Christmas, Easter or Ferragosto.",
            "The laminated pastries are prepared the evening before and "
            "rest in a cold chamber at 4°C for twelve hours minimum, "
            "sixteen hours for Saturday batches. The butter is beaten "
            "cold · the Mothia salt is added in flakes · the folds are "
            "always four, never three · the final lamination cycle yields "
            "64 layers of pastry visible at the cut.",
            "The creams are prepared in front of the customer, whipped to "
            "order. No Madou pastry leaves the counter with a cream "
            "prepared more than two hours earlier · the shortcrust is cut "
            "by hand · the ganaches are emulsified with a whisk at the "
            "next pass. Working to order is the reason we do not sell "
            "cake design without notice.",
        ],

        "values_label": "What we guarantee",
        "values_heading": "Four <em>non-negotiable</em> promises.",
        "values": [
            ("Time",          "Twelve hours of slow proofing minimum · sixteen on Saturdays."),
            ("Supply chain",  "Sixteen suppliers, all visited in person at least once."),
            ("Transparency",  "No ready-mixes, no improvers, no frozen blanks."),
            ("Hand",          "Hand-decoration · creams whipped to order · no industrial moulds."),
        ],

        "cta_heading": "Want to see the <em>patisserie of the current week?</em>",
        "cta_menu": "Five slow-proofed pastries of October '26",
        "cta_prenota": "Pre-order Saturday's pastry",
    },

    # ─── PASTICCERIA (menu) — Gusto's "menu" page ────────────
    "pasticceria": {
        "eyebrow":  "The card of the week",
        "headline": "Living window — <em>autumn '26</em>",
        "intro":
            "The Madou patisserie changes every week according to the "
            "Monday-night oven. What follows is the card in force from "
            "October 6 to 12, 2026 · window open from Tuesday to Saturday, "
            "Sunday mornings only, Monday closed.",
        "courses_label": "Five slow-proofed pastries · October '26",

        "courses": [
            ("I",     "Croissant viennoise",
             "Pasta sfoglia proofed 12 hours · Normandy AOP butter from "
             "Isigny · 64 layers visible at the cut · whole-egg yolk wash · "
             "Mothia icing sugar dusted as it leaves the oven.",
             "Ethiopia Sidamo single-origin coffee · Caffè Vergnano for Madou"),
            ("II",    "Maritozzo with cream",
             "Brioche dough proofed 24 hours with M-3 · fresh cream from "
             "the Inalpi dairy whipped to order · whole Tahitian vanilla "
             "from Madagascar · spun-sugar crown.",
             "Madagascar Domori 72% hot chocolate"),
            ("III",   "Millefoglie with hazelnut",
             "Three layers of caramelised pasta sfoglia · Nocciola Piemonte "
             "IGP chantilly cream from the Brero mill · hazelnut grain "
             "toasted on the refractory deck.",
             "Traditional Torinese Bicerin · historic Caffè Al Bicerin recipe"),
            ("IV",    "Bignè with Domori chocolate",
             "House pâte à choux · dark ganache with 80% Criollo Domori "
             "cacao · glucose-syrup glaze · piped finish · icing sugar to "
             "taste.",
             "Darjeeling First Flush black tea · Damman 2026 selection"),
            ("V",     "Saint Honoré with marroni",
             "Autumn only · bignè filled with marroni mousseline · Cuneo "
             "IGP marroni from Anna Negroni's field · pasta sfoglia base · "
             "golden spun-sugar crown.",
             "Erbaluce di Caluso passito · Cieck selection · 50 cl by the glass"),
            ("VI",    "Mont-Blanc 2026",
             "Chestnut vermicelli from Mortara IGP · vanilla chantilly · "
             "French meringue heart baked at 90°C for four hours · "
             "hand-finished.",
             "Turkish coffee with green cardamom · served in a copper pot"),
            ("VII",   "Tarte au chocolat Sambirano",
             "Cocoa shortcrust at 22% · Madagascar Sambirano 72% dark "
             "ganache · Mothia salt flakes · finish with Taggia "
             "extra-virgin olive oil.",
             "—"),
            ("VIII",  "Seasonal macarons",
             "Six seasonal macarons · Abruzzo saffron, Roero raspberry, "
             "Cuneo chestnut, Sambirano chocolate, Tahitian vanilla, "
             "Taggia olive · baked at 165°C for 12 minutes.",
             "Pai Mu Tan white tea · Damman selection"),
        ],

        # Wine_program → repurposed as caffè & tisaneria
        "wine_intro_title": "Coffee & tea bar",
        "wine_intro":
            "At Madou every slow-proofed pastry is paired with a "
            "single-origin coffee roasted in Torino by Vergnano or a tea "
            "selected by Damman. The tea and coffee list is complete, the "
            "pairings are at the counter's discretion — ask Tommaso when "
            "you pay.",

        "wine_highlights": [
            ("Single-origin coffee", "8 origins · Ethiopia, Brazil, Colombia, Guatemala, Vietnam, Sambirano"),
            ("Black & green teas",   "22 Damman selections · Darjeeling, Ceylon, Sencha, Genmaicha"),
            ("Hot chocolates",       "6 origins · Madagascar, Venezuela, Ecuador, Dominicana, Tanzania, Ghana"),
            ("Traditional drinks",   "Bicerin · cinnamon vin brulé · mandarin ponce · zabaione"),
        ],

        "footer":
            "Window open Tuesday to Saturday · Saturday pre-orders "
            "recommended from Wednesday. Saturday's laminated pastry "
            "regularly sells out by 11:00 AM. For orders above 12 pieces, "
            "please write to atelier@madou-pasticceria.it at least 48 "
            "hours in advance.",
    },

    # ─── VETRINA (gallery) — Gusto's "atmosfera" ─────────────
    "vetrina": {
        "eyebrow":  "The window",
        "headline": "Fifteen metres of window, <em>one single window.</em>",
        "intro":
            "Madou occupies a former print shop on Via Sant'Ottavio · the "
            "window is open to the street for fifteen linear metres and "
            "lets you see the entire workroom. No wall between the oven "
            "and the Borgo Po sidewalk.",

        "rooms": [
            ("The street window",
             "Fifteen metres of window along Via Sant'Ottavio · "
             "two-tier display · refrigeration at +4°C for the creams · "
             "dry case at +18°C for the slow-proofed pastries."),
            ("The open workroom",
             "The real atelier — four stations: lamination, slow-proofed "
             "doughs, creams, decoration. The full patisserie is visible "
             "in real time from the window · no hidden kitchen."),
            ("The tasting room",
             "Eight counter seats facing the laminator. Open only for the "
             "guided tastings on Thursday afternoons · three hours with "
             "Carla, six slow-proofed pastries, three single-origin coffees."),
            ("The print-shop courtyard",
             "From May to September, four open-air tables under the "
             "wisteria of the former print shop. Open for breakfast only · "
             "fixed Monday menu, croissant + Bicerin."),
        ],

        "captions": [
            "The Saturday morning window · 7:30 AM display.",
            "Hand-decoration · autumn '26 wedding cake.",
            "Croissant viennoise fresh from the oven at 6:00 AM.",
            "October '26 macarons · six seasonal flavours.",
            "Carla Madou at the laminator · 5:30 AM pasta sfoglia.",
            "The counter as the first customer arrives · Tuesday 7:30 AM.",
        ],

        "cta_quote": "«No wall between the oven and the Borgo Po sidewalk.»",
        "cta_desc": "Window open Tue – Sat · 7:30 AM – 7:30 PM · Sun 7:30 AM – 1:00 PM · Mon closed.",
        "cta_primary": "Pre-order Saturday's pastry",
        "cta_secondary": "See the full patisserie",
    },

    # ─── DIARIO (blog list / detail) ──────────────────────────
    "diario": {
        "eyebrow":  "The flour journal",
        "headline": "Notes from the oven, <em>from the starter,</em> from the laboratory.",
        "intro":
            "Short notes by Carla Madou and Tommaso Rinaldi on the "
            "slow proofings in progress, on seasonal raw materials, on "
            "the most beautiful pastries and on what is not working in "
            "the patisserie from week to week.",
        "read_article": "Read the article",
        "min_label": "min",
        "min_read_label": "min read",
        "crumb_label": "Journal",
        "back_link": "← Back to the journal",
        "footer_label": "Madou Pasticceria Atelier · The flour journal",
        "empty_body": [
            "Article in editorial preparation. The full publication will "
            "be available shortly, written personally by the pastry chef "
            "or by the master baker.",
            "This placeholder describes the voice of the Flour Journal: "
            "short working notes, reflections on the mother starters, "
            "stories of slow proofings that go wrong. Never more than two "
            "thousand words, never less than five hundred.",
        ],
    },

    "posts": [
        {
            "slug":     "vetrina-autunno-26",
            "kicker":   "Current window",
            "title":    "Five ideas behind the autumn '26 window",
            "date":     "October 6, 2026",
            "read_min": 5,
            "author":   "Carla Madou",
            "lede":
                "The new card entered the window last night. Five "
                "slow-proofed pastries, two reinterpretations of Torinese "
                "patisserie classics, and one pasta sfoglia I chased for "
                "three years.",
            "body": [
                ("p", "Building an autumn window is less a question of "
                      "recipes and more a question of slow proofing "
                      "timings. The chamber temperature drops, the "
                      "starters slow down · the mothers respond more "
                      "slowly. For the autumn '26 card we worked for two "
                      "weeks on the rest times of the Saint Honoré with "
                      "marroni alone."),
                ("h2", "The five new ideas"),
                ("p", "The first slow-proofed pastry, the Saint Honoré "
                      "with Cuneo marroni, is a rereading of the classic "
                      "French Saint Honoré built on three Piemontese raw "
                      "materials: Cuneo IGP marroni from Anna Negroni's "
                      "field, fresh cream from the Inalpi dairy, and "
                      "Normandy-butter pasta sfoglia. I had wanted this "
                      "since 2022, when I had passed through Lyon and "
                      "tasted Cyril Lignac's version · but I wanted a "
                      "Torinese version, not a Parisian one."),
                ("h2", "The reinterpretations"),
                ("p", "The Mont-Blanc 2026 and the maritozzo with cream "
                      "are two pastries I have been working on for seven "
                      "years · neither of them is born in October, but it "
                      "is in October that their respective raw materials "
                      "come into their best: the Mortara marroni for the "
                      "first, the autumn cream for the second. The "
                      "maritozzo, in particular, I have changed seven "
                      "times in twelve months. Now it is right."),
                ("h2", "One pasta sfoglia"),
                ("p", "The croissant viennoise is the piece I am proudest "
                      "of on this card. It is a pasta sfoglia proofed 12 "
                      "hours in a chamber at +4°C, with Isigny AOP butter "
                      "beaten cold and flour from the Brero mill. "
                      "Sixty-four layers visible at the cut, one air "
                      "bubble every 0.4 millimetres of dough. It is the "
                      "slow-proofed pastry I arrived at after eight years "
                      "of attempts, and the only reason I am here."),
                ("h2", "What comes out on Saturday"),
                ("p", "On Saturday Madou bakes 220 croissants viennoise "
                      "that regularly sell out by 11:00 AM. Pre-ordering "
                      "from Thursday is therefore warmly recommended — "
                      "especially from October, when demand climbs again "
                      "with the first cold weather."),
            ],
        },
        {
            "slug":     "lievito-madre-m2",
            "kicker":   "Mother starter",
            "title":    "Why we waited seven years before making panettone",
            "date":     "September 28, 2026",
            "read_min": 6,
            "author":   "Tommaso Rinaldi",
            "lede":
                "Madou only put panettone on the card in 2018, seven "
                "years after opening. The reason is one alone: the M-2 "
                "mother was not ready. Here is why.",
            "body": [
                ("p", "Panettone demands a mother of mothers · many "
                      "pastry chefs build their starter when they open "
                      "the patisserie, but for high-end panettone you "
                      "need a mother that has worked for at least three "
                      "years, developed its acetic profile, found its "
                      "balance. Madou's M-1 — founded in 2011 — was a "
                      "lactic mother, perfect for laminated pastry but "
                      "not aggressive enough for panettone."),
                ("h2", "How M-2 is born"),
                ("p", "In 2014 I took a 200-gram piece of M-1 and "
                      "refreshed it as a triple for forty days · every "
                      "twelve hours, always. That is how you \"turn\" a "
                      "lactic mother towards a mixed profile · it is a "
                      "process I learned from Achille Zoia. After the "
                      "forty days, the mother had become acetic enough "
                      "for panettone, but still too young."),
                ("h2", "Four years of waiting"),
                ("p", "From 2014 to 2018 I refreshed M-2 every twelve "
                      "hours without skipping a single time · not even "
                      "at Christmas, not even in August. Carla called it "
                      "\"the future's mother\" because we never used it. "
                      "In November 2018, on the seventh trial, the "
                      "panettone came out as it had to. Since then M-2 "
                      "produces only panettone, colomba and veneziana, "
                      "nothing else."),
            ],
        },
    ],

    # ─── ORDINA (reservations) — Gusto's "prenota" ────────────
    "ordina": {
        "eyebrow":      "Orders & commissions",
        "headline":     "Pre-order Saturday's pastry.",
        "intro":
            "Saturday's window regularly sells out by 11:00 AM. To secure "
            "the slow-proofed pastries, it is best to pre-order from "
            "Wednesday · pickup at the counter from 7:30 AM to 1:00 PM. "
            "For commissioned cakes and wedding cakes, please write to "
            "atelier@madou-pasticceria.it at least two weeks in advance.",
        "primary_label":   "What would you like to pre-order?",
        "primary_placeholder": "Saturday October 18 · 12 croissants viennoise + 4 maritozzi · pickup at 9:30 AM",
        "name_label":      "Full name",
        "phone_label":     "Phone",
        "email_label":     "Email",
        "submit_label":    "Send the pre-order",
        "submit_note":     "You will receive confirmation from the counter within 24 h. The pre-order is paid at pickup.",

        "contact_block": {
            "address_label": "Atelier",
            "address":       "Via Sant'Ottavio 36 · 10124 Torino · Borgo Po",
            "phone_label":   "Counter",
            "phone":         "+39 011 8195 770",
            "email_label":   "Email",
            "email":         "atelier@madou-pasticceria.it",
            "hours_label":   "Hours",
            "hours_list": [
                "Tue – Sat · 7:30 AM – 7:30 PM",
                "Sun · 7:30 AM – 1:00 PM",
                "Mon · closed",
            ],
        },

        "policy_label": "Pre-order notes",
        "policy_paragraphs": [
            "The Saturday pre-order closes on Friday at 6:00 PM. After that "
            "hour, we accept only if the day's production allows.",
            "For orders above 12 pieces, please contact the counter directly. "
            "Wedding cakes require two weeks minimum lead time · cake design, "
            "three weeks.",
            "Traced raw materials (Isigny butter, Sambirano cacao, IGP marroni, "
            "IGP hazelnuts) follow the seasonal calendar. In case of a stock "
            "break, we propose a coherent alternative.",
        ],

        "small_print":
            "Madou Atelier S.r.l. · VAT 11237680016 · Via Sant'Ottavio 36, "
            "10124 Torino · Pasticceria Atelier since 2011.",
    },
}
