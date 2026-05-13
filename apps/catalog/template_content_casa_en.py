"""Phase 2g3.7 · Session 53 · Casa — EN native-voice tree. Warm residential-agency voice."""
from __future__ import annotations

from typing import Any


CASA_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",        "label": "Home",        "kind": "home"},
        {"slug": "immobili",    "label": "Properties",  "kind": "project_list"},
        {"slug": "quartieri",   "label": "Neighbourhoods", "kind": "about"},
        {"slug": "agenzia",     "label": "The Agency",  "kind": "team"},
        {"slug": "valutazione", "label": "Valuation",   "kind": "services"},
        {"slug": "contatti",    "label": "Contact",     "kind": "contact"},
    ],

    "site": {
        "logo_initial":  "D",
        "logo_word":     "Domus Immobiliare",
        "tag":           "Milan · Turin · since 2005",
        "phone":         "+39 02 8765 4321",
        "phone_tel":     "+390287654321",
        "phone_label":   "Call us",
        "email":         "hello@domusimmobiliare.it",
        "address":       "Corso Buenos Aires 15 · 20124 Milan",
        "address_short": "Milan · Turin",
        "hours_compact": "Mon – Sat · 09:00 – 19:30",
        "hours_footer_rows": [
            "Guided viewings on Sundays too",
            "WhatsApp always open",
        ],
        "whatsapp":      "02 8765 4321",
        "whatsapp_link": "https://wa.me/390287654321",
        "whatsapp_note": "We reply within 20 minutes during opening hours",
        "license":       "RIEA MI 1422 estate agency licence · VAT 05431920968",
        "nav_cta":       "Book a viewing",
        "nav_cta_href":  "contatti",
        "footer_intro":
            "Domus Immobiliare — every property we list is picked by hand. "
            "Twenty years across Milan, Turin, Lake Como and Piedmont, one "
            "dedicated agent from the first meeting through to completion.",
        "foot_studio":   "The agency",
        "foot_pages":    "Pages",
        "foot_contact":  "Get in touch",
        "foot_offices":  "Offices",
        "offices_footer_rows": [
            "Milan · Buenos Aires 15",
            "Turin · Crocetta 8",
        ],
        "tile_rooms_label":    "Beds",
        "tile_surface_label":  "Area",
        "tile_bathrooms_label":"Baths",
        "tile_surface_unit":   "m²",
        "tile_visit_cta":      "Book viewing",
        "tile_reference_label":"Ref.",
        "surface_short":       "m²",
        "price_label":         "Price",
        "energy_class_label":  "Energy rating",
        "floor_label":         "Floor",
        "parking_label":       "Parking",
        "elevator_label":      "Lift",
        "filter_label":        "Filter by",
        "sort_label":          "Sort by",
        "visit_request_label": "Book a viewing",
        "viewings_unit":       "viewings this week",
        "showings_schedule":   "Viewings every day, Saturdays and Sundays included",
    },

    "home": {
        "eyebrow":  "Domus Immobiliare · Milan · Turin · Lombardy & Piedmont",
        "headline": "Six hundred hand-picked homes, <em>one agent</em> from first viewing to closing.",
        "intro":
            "Over 600 hand-picked properties across Milan, Turin, Lake Como "
            "and Piedmont. Guided viewings on Sundays too, free valuation "
            "within 24 hours, and one single agent walking you from the "
            "first appointment all the way to completion.",
        "primary_cta":   "Browse properties",
        "primary_href":  "immobili",
        "secondary_cta": "Free valuation",
        "secondary_href":"valutazione",
        "hero_availability": "20 fresh listings this week",
        "hero_response":     "We call you back within 20 minutes",

        "search_widget": {
            "label":          "What are you looking for today?",
            "intro":          "Tell us the home and the area, we'll take it from there.",
            "location_label": "Where",
            "location_value": "Milan, city centre",
            "type_label":     "Property type",
            "type_value":     "Apartment",
            "price_label":    "Price",
            "price_value":    "€ 500K — € 1.2M",
            "rooms_label":    "Bedrooms",
            "rooms_value":    "3+ bedrooms",
            "cta":            "Search properties",
            "cta_href":       "immobili",
            "secondary_note": "Or tell us on WhatsApp what you're after",
            "popular_label":  "Most searched",
            "popular_tags": [
                "Apartments in Brera",
                "Villas in Cernobbio",
                "Lofts on the Navigli",
                "Three-bed flats in Turin",
                "Houses with gardens",
            ],
        },

        "featured_label":   "Featured this week",
        "featured_heading": "The homes <em>waiting for you</em>.",
        "featured_intro":
            "A tight shortlist from the viewings we've been on in the last "
            "ten days. Every listing is checked personally by an agent, "
            "every photograph is taken during the actual viewing.",
        "featured_link":    "See all 600+ properties",
        "featured_link_href":"immobili",
        "featured_listings": [
            ("€ 1,250,000", "Panoramic penthouse with terrace",    "Milano · Brera",        "4", "180", "2", "Exclusive",  "MI-1842"),
            ("€ 890,000",   "Modern villa with garden",            "Como · Cernobbio",      "5", "240", "3", "New",        "CO-0217"),
            ("€ 650,000",   "Design loft in the Tortona district", "Milano · Navigli",      "2", "120", "2", "Renovated",  "MI-1788"),
            ("€ 420,000",   "Bright three-bed with balcony",       "Torino · Crocetta",     "3",  "95", "1", "Available",  "TO-0904"),
        ],

        "neighborhoods_label":   "Neighbourhoods",
        "neighborhoods_heading": "Where <em>we find homes</em>.",
        "neighborhoods_intro":
            "Milan, Turin, the lake. Every area is covered by a locally "
            "based agent — we know the concierges, the cafés, the schools, "
            "the best stop for the morning commute.",
        "neighborhoods": [
            ("Brera",     "Milano · historic",     "124 properties", "from € 850K"),
            ("Navigli",   "Milano · design",       "89 properties",  "from € 520K"),
            ("Isola",     "Milano · contemporary", "71 properties",  "from € 480K"),
            ("Cernobbio", "Como · lakeside",       "42 properties",  "from € 680K"),
            ("Crocetta",  "Torino · residential",  "67 properties",  "from € 380K"),
            ("Borgo Po",  "Torino · hillside",     "38 properties",  "from € 410K"),
        ],
        "neighborhoods_cta":      "Explore every neighbourhood",
        "neighborhoods_cta_href": "quartieri",

        "stats_label":   "Twenty years on the market",
        "stats_heading": "Our numbers, in plain sight.",
        "stats_intro":
            "What matters isn't how many homes we have in the window, but "
            "how many have actually sold. Here are the numbers from 2005 "
            "to today.",
        "stats": [
            ("600",   "+", "properties on the books"),
            ("2,800", "+", "homes found since 2005"),
            ("20",    "",  "years of experience"),
            ("4.8",   " ★","across 420 Google reviews"),
        ],
        "stats_note": "Figures updated March 2026 · cross-checked on immobiliare.it",

        "agents_label":   "Who walks with you",
        "agents_heading": "One agent, <em>from start to finish</em>.",
        "agents_intro":
            "No switchboards, no rotating consultants. From the first "
            "appointment to the completion deed you speak with the same "
            "person — the one who knows the area, the building, often "
            "even your future next-door neighbour.",
        "agents_preview": [
            ("Giulia Ferrante", "Senior agent",   "Milano · Brera & Centre",  "15 years"),
            ("Marco Lentini",   "Senior agent",   "Milano · Navigli & South", "12 years"),
            ("Silvia Mondelli", "Head of office", "Torino · Crocetta",        "10 years"),
            ("Andrea Colombo",  "Senior agent",   "Como · lakeside",          "18 years"),
        ],
        "agents_cta":      "Meet the whole team",
        "agents_cta_href": "agenzia",

        "valuation_label":   "Free valuation",
        "valuation_heading": "What is <em>your home</em> worth?",
        "valuation_intro":
            "We call you back within 24 hours with an honest figure, based "
            "on a side-by-side of every completion registered in your "
            "block over the last twelve months. No commitment, zero cost, "
            "even if you later decide to sell with another agency.",
        "valuation_cta":       "Request a valuation",
        "valuation_cta_href":  "valutazione",
        "valuation_secondary": "See how it works",
        "valuation_secondary_href":"valutazione",
        "valuation_proof": [
            ("24 h",   "response time"),
            ("€ 0",    "cost, always"),
            ("420+",   "valuations in 2025"),
        ],

        "testimonial_label":  "They bought with us",
        "testimonial_quote":
            "They understood what we were after in ten minutes. Three "
            "viewings, the fourth was home. Giulia even came with us to "
            "the notary — and we had never bought a property before.",
        "testimonial_author": "Francesca & Tommaso Ranieri",
        "testimonial_meta":   "Three-bed · Brera · completed March 2026",
    },

    "quartieri": {
        "eyebrow":  "Area guide · Milan · Turin · Como",
        "headline": "The neighbourhoods <em>we know</em> best.",
        "intro":
            "Every neighbourhood below is covered by one of our local "
            "agents. Here you'll find average prices, current availability, "
            "typical floor areas and the signature of the person who "
            "works there every single day.",

        "guides_label": "Neighbourhood guide",
        "guides_heading": "Pick the area, <em>we know the way</em>.",
        "guides": [
            (
                "Brera", "Milano · historic & cultural",
                "€ 9,200 / m²", "124 properties available",
                "M2 Lanza · M3 Montenapoleone", "Parco Sempione 6 min away", "Historic luxury",
                "The historic heart of Milan: nineteenth-century palazzi, inner "
                "courtyards, ateliers and a fabric of one-of-a-kind shops you "
                "won't find anywhere else. Plenty of conservative refurbishments, "
                "very few new builds. Suited to buyers looking for classic layouts "
                "with a consolidated capital gain.",
                "Giulia Ferrante · resident agent since 2008",
            ),
            (
                "Navigli", "Milano · design & nightlife",
                "€ 7,100 / m²", "89 properties available",
                "M2 Porta Genova · Tram 3/9", "Darsena · Ticinese on foot", "Creative & young",
                "The two canals corridor: industrial lofts, period balcony houses, "
                "architecture studios. Dynamic, international, lively in the "
                "evenings. Perfect for a short-to-mid term investment or a young "
                "first purchase.",
                "Marco Lentini · senior agent",
            ),
            (
                "Porta Nuova", "Milano · the new skyline",
                "€ 10,400 / m²", "56 properties available",
                "M2 Gioia · M3 Repubblica", "BAM Library of Trees", "Contemporary & business",
                "The district of the new Milan: skyscrapers, finance, signature "
                "homes like Bosco Verticale and Solaria. For buyers looking for "
                "premium services, concierge, and fully integrated smart-home "
                "systems.",
                "Giulia Ferrante · resident agent",
            ),
            (
                "Isola", "Milano · creative & contemporary",
                "€ 7,600 / m²", "71 properties available",
                "M5 Isola · Tram 2/4", "BAM in 5 min · Parco Lambro in 10", "Creative & residential",
                "Once a working-class district, reborn around Porta Nuova. "
                "Restored balcony houses sit next to brand-new developments. "
                "Authentic Milanese atmosphere, a market in stable growth for "
                "the last ten years.",
                "Sofia Ranieri · junior agent · Milan North",
            ),
            (
                "Cernobbio", "Como · lake & villas",
                "€ 5,900 / m²", "42 properties available",
                "Cadorna-Como train · 48 min", "Lake on foot · Villa Erba gardens", "Lakeside & second homes",
                "The western shore of Lario: period villas with lake access, "
                "apartments in historic buildings facing the bay, penthouses "
                "with full views. International clientele, English and German "
                "spoken daily in our office.",
                "Andrea Colombo · senior lake agent",
            ),
            (
                "Bellagio", "Como · pearl of Lake Como",
                "€ 6,400 / m²", "29 properties available",
                "Como-Bellagio ferry · by car", "Pedestrian historic centre", "Exclusive & international",
                "The tip of the lake triangle: medieval old town, villas on "
                "Punta Spartivento, panoramic residences with dual views. A "
                "niche market, availability is always tight.",
                "Andrea Colombo · Lake Como",
            ),
            (
                "Crocetta", "Torino · elegant residential",
                "€ 3,900 / m²", "67 properties available",
                "M1 Re Umberto · Tram 4/10", "Parco del Valentino · 12 min", "Bourgeois & family",
                "Turin's best-loved district: 1930s palazzi, silent courtyards, "
                "historic schools, a covered market. Generous floor areas, a "
                "very liveable pace, prices still accessible compared to Milan. "
                "Our first recommendation for families.",
                "Silvia Mondelli · head of Turin",
            ),
            (
                "Borgo Po", "Torino · hillside & panoramic",
                "€ 4,200 / m²", "38 properties available",
                "Tram 13/15 · Gran Madre", "Hillside · Monte dei Cappuccini", "Romantic & view",
                "The right bank of the Po: liberty palazzi, villas on the hill, "
                "penthouses with Alpine views. A network of bistros and historic "
                "bars. For anyone wanting air and a panorama ten minutes from "
                "the centre.",
                "Silvia Mondelli · Turin hill & centre",
            ),
        ],

        "faq_label":   "Frequently asked questions on the neighbourhoods",
        "faq_heading": "What you ask us the most.",
        "faq": [
            (
                "Which neighbourhood is best for a family moving to Milan?",
                "For families we recommend Crocetta in Turin, Isola and Porta "
                "Nuova in Milan. Both have schools nearby, parks within walking "
                "distance, a metro stop around the corner. If you prefer the "
                "hillside, Borgo Po in Turin is the right call.",
            ),
            (
                "Historic centre or an emerging area — which is the better investment?",
                "It depends on your horizon. Historic centre = consolidated "
                "capital gain, 2-3 % annual growth. Emerging areas like Isola "
                "have posted +48 % in ten years, but the risk is higher. Let's "
                "discuss it over a fifteen-minute call.",
            ),
            (
                "Do you handle rentals too, or only sales?",
                "Mostly sales. We manage rentals only for properties entrusted "
                "to us by a selling client who wants to let in the meantime. "
                "For pure rentals we'll point you to the right colleague.",
            ),
            (
                "How does a viewing on Lake Como work if I live in Milan?",
                "On Saturday mornings we organise a shuttle from Milan Cadorna: "
                "three properties viewed the same day, lunch included, back "
                "home by 18:00. That way you see it all without renting a car.",
            ),
        ],

        "cta_label":   "Speak to the agent in your area",
        "cta_heading": "A coffee, twenty minutes, everything clearer.",
        "cta_intro":
            "Pick a neighbourhood and we'll connect you with the agent who "
            "works it every day. First meeting is free, in the office or "
            "on site.",
        "cta_primary":       "Book a viewing",
        "cta_primary_href":  "contatti",
        "cta_secondary":     "Free valuation",
        "cta_secondary_href":"valutazione",
    },

    "agenzia": {
        "eyebrow":  "The team · 14 people · Milan & Turin",
        "headline": "The agents walking with you <em>from first meeting to completion</em>.",
        "intro":
            "Nine registered agents, two office heads, three colleagues "
            "in the legal back-office. Every area has its resident agent, "
            "every transaction its own technical file, every client a "
            "single number to call.",

        "book_cta":       "Book a viewing",
        "agents_heading": "The full team.",
        "agents_intro":
            "In the office we work in pairs: a senior handles the property, "
            "a junior handles the families searching. That way you get "
            "answers in the evenings and on Saturdays too.",

        "agents": [
            {
                "name": "Giulia Ferrante",
                "role": "Partner · Head of Milan Centre",
                "area": "Milano · Brera, Quadrilatero, Porta Nuova",
                "years": "15 years",
                "languages": "Italian · English · French",
                "speciality": "Historic palazzi, high floors, piano nobile. "
                              "Full handholding from first viewing to completion.",
                "phone": "+39 02 8765 4322",
                "whatsapp_href": "https://wa.me/390287654322",
                "email": "giulia@domusimmobiliare.it",
                "quote": "The right home does exist: the work is listening "
                         "long enough to recognise it on the first viewing.",
            },
            {
                "name": "Marco Lentini",
                "role": "Senior agent · Milan South",
                "area": "Milano · Navigli, Tortona, Bocconi",
                "years": "12 years",
                "languages": "Italian · English",
                "speciality": "Industrial lofts, balcony houses, designer "
                              "conversions. Connections with local architecture practices.",
                "phone": "+39 02 8765 4323",
                "whatsapp_href": "https://wa.me/390287654323",
                "email": "marco@domusimmobiliare.it",
                "quote": "On the Navigli the value isn't the square metre: "
                         "it's the courtyard, the light, the silence between two canals.",
            },
            {
                "name": "Silvia Mondelli",
                "role": "Head of Turin office",
                "area": "Torino · Crocetta, Cit Turin, Centre",
                "years": "10 years",
                "languages": "Italian · English · Spanish",
                "speciality": "Relocating families, first homes, tax "
                              "guidance for buyers returning from abroad.",
                "phone": "+39 011 5328 4401",
                "whatsapp_href": "https://wa.me/390115328440",
                "email": "silvia@domusimmobiliare.it",
                "quote": "Turin today offers what Milan offered twenty years ago: "
                         "generous footprints, fair prices, quality of life.",
            },
            {
                "name": "Andrea Colombo",
                "role": "Senior agent · Lake Como",
                "area": "Como · Cernobbio, Bellagio, Tremezzo",
                "years": "18 years",
                "languages": "Italian · English · German",
                "speciality": "Period villas, second homes for international "
                              "clients, seasonal post-sale management.",
                "phone": "+39 031 2345 6789",
                "whatsapp_href": "https://wa.me/390312345678",
                "email": "andrea@domusimmobiliare.it",
                "quote": "On the lake every villa has a hundred years of story. "
                         "My job is to shorten the completion to three months.",
            },
            {
                "name": "Sofia Ranieri",
                "role": "Agent · Milan North",
                "area": "Milano · Isola, Porta Nuova, Dergano",
                "years": "6 years",
                "languages": "Italian · English",
                "speciality": "New builds, high energy rating, first homes "
                              "for professionals aged 30 to 40.",
                "phone": "+39 02 8765 4324",
                "whatsapp_href": "https://wa.me/390287654324",
                "email": "sofia@domusimmobiliare.it",
                "quote": "Isola today is not the Isola of ten years ago. "
                         "Easier to live in, harder to read the value.",
            },
            {
                "name": "Luca Benedetti",
                "role": "Agent · Turin hillside",
                "area": "Torino · Borgo Po, Gran Madre, Maddalena",
                "years": "9 years",
                "languages": "Italian · French",
                "speciality": "Liberty villas, penthouses with Alpine views, "
                              "heavy refurbishments with technical contract.",
                "phone": "+39 011 5328 4402",
                "whatsapp_href": "https://wa.me/390115328441",
                "email": "luca@domusimmobiliare.it",
                "quote": "Turin's hill is urban poetry: ten minutes from the "
                         "centre and the Alps greet you every morning.",
            },
            {
                "name": "Chiara Sestri",
                "role": "Junior agent · Milan Centre",
                "area": "Milano · Brera, Magenta, Cadorna",
                "years": "3 years",
                "languages": "Italian · English · French · Arabic",
                "speciality": "Language support for international clients, "
                              "tax-code paperwork, first approach to the Italian market.",
                "phone": "+39 02 8765 4325",
                "whatsapp_href": "https://wa.me/390287654325",
                "email": "chiara@domusimmobiliare.it",
                "quote": "People buying in Milan from abroad need to be "
                         "walked through it, not just served.",
            },
            {
                "name": "Davide Orsini",
                "role": "Agent · Monza & Brianza",
                "area": "Monza · Seregno · Desio",
                "years": "11 years",
                "languages": "Italian · English",
                "speciality": "Detached houses with gardens, standalone "
                              "villas, residential market for families leaving Milan.",
                "phone": "+39 039 5328 4403",
                "whatsapp_href": "https://wa.me/390395328440",
                "email": "davide@domusimmobiliare.it",
                "quote": "Every year I see families buying in Brianza for "
                         "a third child: it's a better economic index than the GDP.",
            },
            {
                "name": "Elisa Parini",
                "role": "Legal coordinator",
                "area": "Back-office · Milan head office",
                "years": "8 years",
                "languages": "Italian · English · Spanish",
                "speciality": "Notary files, mortgage searches, loan "
                              "underwriting, end-to-end completion management.",
                "phone": "+39 02 8765 4326",
                "whatsapp_href": "https://wa.me/390287654326",
                "email": "elisa@domusimmobiliare.it",
                "quote": "Completion is the last mile but often the most "
                         "delicate one: a single plan-drawing error costs months.",
            },
        ],

        "facts_label":   "The agency, in brief",
        "facts_heading": "Twenty years, one rule: one agent per family.",
        "facts": [
            ("2005", "",  "year founded"),
            ("9",    "",  "registered agents"),
            ("2",    "",  "offices · Milan & Turin"),
            ("2,800","+", "families walked to completion"),
        ],

        "footnote_strong": "Want to speak with one of us?",
        "footnote_body":
            "Pick the agent for your area or message us on chat: we'll "
            "put you in touch within one working hour. ",
        "footnote_link":  "Message us on WhatsApp",
    },

    "valutazione": {
        "eyebrow":  "Free valuation · reply within 24 hours",
        "headline": "What is <em>your home</em> worth?",
        "intro":
            "We call you back within 24 hours with an honest figure, based "
            "on a side-by-side of every completion registered in your "
            "block over the last twelve months. No commitment, zero cost, "
            "even if you later decide to sell with another agency.",

        "how_it_works_label":   "How it works",
        "how_it_works_heading": "Three steps, <em>no surprises</em>.",
        "how_it_works": [
            ("01", "Fill in the form",
             "All we need is the address, the property type, the floor area "
             "and four details on the condition. Five minutes, no attachments "
             "at this stage."),
            ("02", "We call you within 24 h",
             "An agent from your area calls you, confirms the details and, "
             "if needed, books a free site visit. For Milan and Turin often "
             "the very next day."),
            ("03", "You get the written appraisal",
             "Within 48 hours of the visit we send you a written valuation "
             "with a price bracket, area comparables, and a recommended "
             "go-to-market plan."),
        ],

        "form_label":   "Request a valuation",
        "form_heading": "Tell us about your property",
        "form_intro":
            "Describe your home in five minutes. Fields marked with an "
            "asterisk are required — the others help us give you a sharper "
            "figure from the first call.",
        "form_submit_label": "Request free valuation",
        "form_submit_note":
            "We call you back within 24 working hours. Your data is read "
            "only by your assigned agent — no third parties involved.",
        "form_consent":
            "I consent to the processing of my personal data under EU "
            "Regulation 679/2016. The request is read and stored only "
            "by the assigned Domus agent — no external broker involved.",

        "form_sections": [
            {"num": "01", "title": "Your property",
             "meta": "Address, type, floor area. Five minutes.",
             "fields": ["address", "city", "property_type", "surface", "rooms", "bathrooms"]},
            {"num": "02", "title": "Condition",
             "meta": "Four inputs that weigh heavily on the figure.",
             "fields": ["condition", "floor", "energy_class", "timeline"]},
            {"num": "03", "title": "Your details",
             "meta": "To call you back within 24 hours.",
             "fields": ["name", "surname", "email", "phone", "notes"]},
        ],

        "form_fields": [
            {"name": "address", "label": "Property address", "type": "text", "required": True,
             "placeholder": "e.g. Via della Spiga 12", "full_width": True,
             "helper": "Street and number. We'll work out the neighbourhood ourselves."},
            {"name": "city", "label": "City", "type": "select", "required": True,
             "options": ["Milan", "Turin", "Como and province", "Monza and Brianza", "Other (please specify in notes)"],
             "helper": "If your city is missing, tell us in the notes."},
            {"name": "property_type", "label": "Property type", "type": "select", "required": True,
             "options": [
                 "Apartment · one-bed",
                 "Apartment · two-bed",
                 "Apartment · three-bed or more",
                 "Penthouse",
                 "Loft",
                 "Detached villa",
                 "Terraced or semi-detached villa",
                 "Office",
                 "Other",
             ],
             "helper": "Required to proceed."},
            {"name": "surface", "label": "Usable floor area (m²)", "type": "number", "required": True,
             "placeholder": "e.g. 95",
             "helper": "Internal liveable area, excluding terraces and garages."},
            {"name": "rooms", "label": "Bedrooms", "type": "select", "required": True,
             "options": ["1", "2", "3", "4", "5", "6 or more"],
             "helper": "Count bedrooms only, not living rooms."},
            {"name": "bathrooms", "label": "Bathrooms", "type": "select", "required": True,
             "options": ["1", "2", "3", "4 or more"]},
            {"name": "condition", "label": "Condition", "type": "select", "required": True,
             "options": [
                 "New build or fully refurbished",
                 "Good condition · minor works",
                 "Needs partial refurbishment",
                 "Needs full refurbishment",
                 "Shell · new-build delivery",
             ],
             "helper": "Has a major impact on the appraisal."},
            {"name": "floor", "label": "Floor", "type": "select", "required": False,
             "options": ["Ground floor", "Raised ground", "1st", "2nd", "3rd", "4th or higher", "Penthouse", "Detached villa"],
             "helper": "Optional — useful for apartments."},
            {"name": "energy_class", "label": "Energy rating", "type": "select", "required": False,
             "options": ["A4 / A3 / A2 / A1", "B", "C", "D", "E", "F", "G", "Not available"],
             "helper": "If you don't know, pick «Not available»."},
            {"name": "timeline", "label": "Sale timeline", "type": "select", "required": True,
             "options": [
                 "Within 3 months · urgent",
                 "Within 6 months",
                 "Within 12 months",
                 "Exploratory · no urgency",
             ],
             "helper": "Helps us plan the viewings calendar."},
            {"name": "name", "label": "First name", "type": "text", "required": True, "placeholder": "e.g. Laura"},
            {"name": "surname", "label": "Last name", "type": "text", "required": True, "placeholder": "e.g. Ferrante"},
            {"name": "email", "label": "Email", "type": "email", "required": True,
             "placeholder": "laura.ferrante@example.it",
             "helper": "We send the written valuation to this address."},
            {"name": "phone", "label": "Phone", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "We call you back within 24 working hours."},
            {"name": "notes", "label": "Additional notes", "type": "textarea", "required": False,
             "full_width": True,
             "placeholder": "Tell us a bit more about the property — terrace, "
                            "garage, cellar, lift, any planned works. "
                            "Maximum 600 characters.",
             "helper": "Optional, but it helps us sharpen the figure."},
        ],

        "proof_label":   "Why trust us",
        "proof_heading": "A real appraisal, not a sales hook.",
        "proof": [
            ("420+",  "written valuations in 2025"),
            ("92 %",  "properties sold within 6 months"),
            ("€ 0",   "cost of the valuation"),
            ("24 h",  "response time"),
        ],

        "faq_label":   "Valuation FAQ",
        "faq_heading": "What you ask us the most.",
        "faq": [
            (
                "Is the valuation really free?",
                "Yes, always. Even if you later decide to sell with another "
                "agency — it's happened, it's not a drama. The cost of the "
                "visit is on us.",
            ),
            (
                "How long between the request and the written valuation?",
                "We call you back within 24 working hours. If a site visit "
                "is needed, we book it within 3 days. The written appraisal "
                "lands within 48 hours of the visit.",
            ),
            (
                "Is the valuation valid for a mortgage or a probate?",
                "For bank or probate use you need a sworn appraisal from a "
                "CTU-registered surveyor. Our figure is a market appraisal — "
                "very useful for decisions, not legally binding.",
            ),
            (
                "Do I need to share documents at this stage?",
                "No. We just need the form data. The deed, the plan and the "
                "energy certificate will only be needed if you decide to "
                "go to market with us.",
            ),
        ],
    },

    "contatti": {
        "eyebrow":  "Contact · Milan & Turin",
        "headline": "Write to us, <em>we call back within 20 minutes</em>.",
        "intro":
            "You can write, call, or drop by the office. On Saturdays "
            "we're open all day, on Sundays by appointment. For urgent "
            "matters WhatsApp is the fastest channel.",

        "offices_label":   "The offices",
        "offices_heading": "Two offices, <em>one team</em>.",
        "offices": [
            {
                "name": "Milan · head office",
                "address": "Corso Buenos Aires 15 · 20124 Milan",
                "metro": "M1 Lima · M1 Loreto · Tram 33",
                "hours": "Mon – Sat · 09:00 – 19:30 · Sun by appointment",
                "phone": "+39 02 8765 4321",
                "whatsapp": "02 8765 4321",
                "whatsapp_href": "https://wa.me/390287654321",
                "email": "milano@domusimmobiliare.it",
                "map_link": "Open in Google Maps",
                "map_href": "https://maps.google.com/?q=Corso+Buenos+Aires+15+Milano",
                "lead_agent": "Giulia Ferrante · head of Milan",
                "parking": "Discounted parking 80 m away · Garage Abadia",
                "note": "Spacious office with three rooms dedicated to "
                        "private meetings. Water, coffee and wi-fi at your disposal.",
            },
            {
                "name": "Turin · Crocetta",
                "address": "Via Legnano 8 · 10128 Turin",
                "metro": "M1 Re Umberto · Tram 4/10",
                "hours": "Mon – Fri · 09:00 – 19:00 · Sat 09:30 – 13:00",
                "phone": "+39 011 5328 4400",
                "whatsapp": "011 5328 4400",
                "whatsapp_href": "https://wa.me/390115328440",
                "email": "torino@domusimmobiliare.it",
                "map_link": "Open in Google Maps",
                "map_href": "https://maps.google.com/?q=Via+Legnano+8+Torino",
                "lead_agent": "Silvia Mondelli · head of Turin",
                "parking": "Free ZTL on weekends · Piazza Solferino car park",
                "note": "A warm office in the heart of Crocetta, two "
                        "minutes' walk from the Politecnico.",
            },
        ],

        "channels_label":   "Direct channels",
        "channels_heading": "Pick how to reach us.",
        "channels": [
            ("Phone",           "+39 02 8765 4321",                "Live reply during opening hours"),
            ("WhatsApp Milan",  "02 8765 4321",                    "Messages read within 20 minutes · evenings too"),
            ("WhatsApp Turin",  "011 5328 4400",                   "Mon – Sat · same team you see in the office"),
            ("Email",           "hello@domusimmobiliare.it",       "We reply within 4 working hours"),
            ("In the office",   "Milan · Corso Buenos Aires 15",   "No appointment needed Mon – Sat mornings"),
        ],

        "form_label":   "Send us a message",
        "form_heading": "Leave your details",
        "form_intro":
            "Fill in the form, we'll call you back within 20 minutes "
            "during opening hours. If you write us in the evening, we "
            "reply the next morning by 10:00.",
        "form_submit_label": "Send message",
        "form_submit_note":
            "Reply within 20 minutes in opening hours · 4 working hours "
            "for emails out of hours.",
        "form_consent":
            "I consent to the processing of my personal data under EU "
            "Regulation 679/2016. The request is read and stored only by "
            "the assigned Domus agent.",

        "form_sections": [
            {"num": "01", "title": "Your details",
             "meta": "So we can reply directly.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "How can we help",
             "meta": "A brief line, then we pick it up over the phone.",
             "fields": ["topic", "preferred_office", "message"]},
        ],

        "form_fields": [
            {"name": "name", "label": "First name", "type": "text", "required": True, "placeholder": "e.g. Francesca"},
            {"name": "surname", "label": "Last name", "type": "text", "required": True, "placeholder": "e.g. Ranieri"},
            {"name": "email", "label": "Email", "type": "email", "required": True,
             "placeholder": "francesca@example.it"},
            {"name": "phone", "label": "Phone", "type": "tel", "required": False,
             "placeholder": "+39 ...", "helper": "Optional · if you'd rather we call."},
            {"name": "topic", "label": "Your request", "type": "select", "required": True,
             "options": [
                 "I'd like to buy a home",
                 "I'd like to sell a home",
                 "I'd like a free valuation",
                 "I'm looking to rent (passed to partner agency)",
                 "Other · I'll tell you in the message",
             ]},
            {"name": "preferred_office", "label": "Preferred office", "type": "select", "required": True,
             "options": ["Milan · Corso Buenos Aires", "Turin · Via Legnano", "Lake Como · by appointment"]},
            {"name": "message", "label": "Message", "type": "textarea", "required": True, "full_width": True,
             "placeholder": "What you're after, where you are in the journey, "
                            "when you'd like to hear from us. Maximum 800 "
                            "characters — details we talk through on a call.",
             "helper": "A short summary is enough: the rest we discuss live."},
        ],
    },

    "immobili": {
        "eyebrow":  "Full showcase · 600+ properties · refreshed this week",
        "headline": "Every property <em>currently on our books</em>.",
        "intro":
            "A living shortlist: every listing is verified by the area "
            "agent, every photograph is taken on-site, no renders ever. "
            "New listings land every Monday morning.",

        "filter_label": "Filter",
        "filters": [
            "All",
            "Milan",
            "Turin",
            "Lake Como",
            "Under € 500K",
            "€ 500K — 1 M",
            "Over € 1 M",
            "Penthouse",
            "Villa",
            "Loft",
            "New build",
        ],
        "sort_label": "Sort",
        "sort_options": [
            "Newest first",
            "Price ascending",
            "Price descending",
            "Floor area descending",
        ],

        "ledger_label": "Full showcase",
        "ledger_intro":
            "Click any card to open the full dossier: floor plan, energy "
            "rating, history of works, lead agent and bookable viewing slots.",

        "row_rooms_label":    "Beds",
        "row_surface_label":  "m²",
        "row_area_label":     "Area",
        "row_price_label":    "Price",
        "row_year_label":     "Since",
        "row_discipline_label":"Type",
        "row_duration_label": "Average viewing",

        "map_label":   "Where we're searching",
        "map_heading": "Our showcase, <em>on the map</em>.",
        "map_intro":
            "Three provinces, two offices, one team. Every pin on the "
            "map matches a property either currently for sale or about "
            "to enter the window.",
        "map_note":
            "The interactive map is available on the commercial release "
            "of the site — here you see only an indicative overview of "
            "our footprint.",
        "map_cells": [
            ("Milan city",     "412 properties"),
            ("Monza Brianza",  "58 properties"),
            ("Lake Como",      "71 properties"),
            ("Turin city",     "105 properties"),
            ("Turin hillside", "38 properties"),
        ],

        "cta_label":        "Can't find what you're after?",
        "cta_heading":      "Tell us what's missing. <em>We'll find it</em>.",
        "cta_intro":
            "Over the last five years more than 30 % of the homes we've "
            "sold were never online: we had them from regular sellers. "
            "Tell us what you're after and we'll let you know as soon as "
            "something right comes in.",
        "cta_primary":        "Book a viewing",
        "cta_primary_href":   "contatti",
        "cta_secondary":      "Let's talk on the phone",
        "cta_secondary_href": "contatti",

        "dossier_meta_price_label":    "Price",
        "dossier_meta_surface_label":  "Area",
        "dossier_meta_rooms_label":    "Beds",
        "dossier_meta_bathrooms_label":"Baths",
        "dossier_meta_energy_label":   "Energy rating",
        "dossier_meta_floor_label":    "Floor",
        "dossier_summary_label":       "What you'll love",
        "dossier_highlights_label":    "Key points",
        "dossier_highlights_heading":  "The details that matter.",
        "dossier_agent_label":         "Lead agent",
        "dossier_book_cta":            "Book a viewing",
        "dossier_next_label":          "Next property",
    },

    "posts": [
        {
            "slug":       "attico-brera-duomo",
            "title":      "Panoramic penthouse with terrace · Brera",
            "price":      "€ 1,250,000",
            "area":       "Milano · Brera · Via Madonnina 14",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "180",
            "energy":     "B",
            "floor":      "7th (top · lift)",
            "badge":      "Exclusive",
            "reference":  "MI-1842",
            "year_built": "1923 · full refurbishment 2024",
            "lead":
                "A top-floor penthouse in a period palazzo with a sixty-"
                "metre terrace and a 270-degree view over the Duomo and "
                "Piazza della Scala. 2024 refurbishment signed by Studio "
                "Arfaioli, fully integrated smart-home technology.",
            "summary": [
                "62 m² terrace with Duomo and Sforzesco views",
                "Four bedrooms, two bathrooms in Carrara marble",
                "Energy rating B after 2024 envelope and glazing works",
                "Internal lift to the penthouse, three parking spaces included",
                "Move-in ready · completion within 45 days",
            ],
            "highlights": [
                ("Terrace", "62 m² Duomo view"),
                ("Parking", "Three spaces in private garage"),
                ("Smart home", "Full KNX integration"),
                ("Energy rating", "B · after 2024 works"),
            ],
            "description":
                "The apartment has been fully redesigned around the idea "
                "of a vertical loft: 70 m² living area with dual east-"
                "south aspect, brushed-brass island, full-height walnut "
                "library. The sleeping wing is given over to the two "
                "suites, each with dressing room and private bathroom in "
                "Statuario marble. On the terrace, outdoor hot tub and "
                "dining table for ten.",
            "agent_name":  "Giulia Ferrante",
            "agent_role":  "Senior agent · Milan Centre",
            "agent_phone": "+39 02 8765 4322",
        },
        {
            "slug":       "villa-cernobbio-lago",
            "title":      "Modern villa with garden · Cernobbio",
            "price":      "€ 890,000",
            "area":       "Como · Cernobbio · Via Regina 88",
            "rooms":      "5",
            "bathrooms":  "3",
            "surface":    "240",
            "energy":     "A2",
            "floor":      "Detached villa · 3 levels",
            "badge":      "New",
            "reference":  "CO-0217",
            "year_built": "2023",
            "lead":
                "Brand-new villa on three levels, two hundred metres from "
                "the lake, private garden of a thousand square metres "
                "with heated pool. Contemporary finishes, geothermal "
                "system, energy rating A2.",
            "summary": [
                "Private garden of 1,020 m² with 10 × 4 pool",
                "Five bedrooms, three bathrooms, separate study and laundry",
                "Geothermal system · energy rating A2",
                "Direct lake access 200 m away",
                "Double garage and covered guest space",
            ],
            "highlights": [
                ("Garden", "1,020 m² with pool"),
                ("Systems", "Geothermal · 8 kW solar"),
                ("Bedrooms", "Five · two suites"),
                ("Rating", "A2 · near-zero bills"),
            ],
            "description":
                "The villa sits on a corner plot with garden on three "
                "sides, south-east aspect for the living area. Basement "
                "with games room, climate-controlled cellar and double "
                "garage; ground floor with double-height lounge, "
                "professional Boffi kitchen and garden access; upper "
                "floor with four bedrooms and two bathrooms, plus master "
                "suite with dressing room.",
            "agent_name":  "Andrea Colombo",
            "agent_role":  "Senior agent · Lake Como",
            "agent_phone": "+39 031 2345 6789",
        },
        {
            "slug":       "loft-tortona-navigli",
            "title":      "Design loft in the Tortona district",
            "price":      "€ 650,000",
            "area":       "Milano · Navigli · Via Savona 22",
            "rooms":      "2",
            "bathrooms":  "2",
            "surface":    "120",
            "energy":     "C",
            "floor":      "Raised ground · courtyard",
            "badge":      "Renovated",
            "reference":  "MI-1788",
            "year_built": "1902 · early 1900s factory conversion 2020",
            "lead":
                "120 m² loft in an early-1900s former factory, double "
                "height of four and a half metres, original oak floor, "
                "black-iron mezzanine for the sleeping area. Facing a "
                "silent inner courtyard.",
            "summary": [
                "Exposed iron beams and concrete ceiling",
                "Double-height living area · open kitchen",
                "Iron and timber mezzanine · suite with dressing room",
                "Shared courtyard with small inner garden",
                "No street frontage · absolute silence",
            ],
            "highlights": [
                ("Height", "4.5 m double height"),
                ("Light", "6 × 3 m factory window"),
                ("Kitchen", "Boffi kitchen included"),
                ("Outlook", "Silent courtyard"),
            ],
            "description":
                "The loft was carved from the last bay of a former textile "
                "factory restored in 2020. The cast-iron structural "
                "columns are kept, the original oak floor was relaid, "
                "the iron-framed windows swapped for thermal double "
                "glazing. The mezzanine sleeping area tops the volume "
                "without closing it in.",
            "agent_name":  "Marco Lentini",
            "agent_role":  "Senior agent · Milan South",
            "agent_phone": "+39 02 8765 4323",
        },
        {
            "slug":       "trilocale-crocetta-torino",
            "title":      "Bright three-bed with balcony · Crocetta",
            "price":      "€ 420,000",
            "area":       "Torino · Crocetta · Corso Giovanni Lanza 7",
            "rooms":      "3",
            "bathrooms":  "1",
            "surface":    "95",
            "energy":     "D",
            "floor":      "3rd (lift)",
            "badge":      "Available",
            "reference":  "TO-0904",
            "year_built": "1932 · routine upkeep 2019",
            "lead":
                "Three-bed in the heart of Crocetta, beautifully kept "
                "1930s palazzo, seven-metre balcony overlooking a green "
                "inner courtyard, east-west aspect. Classic layout, "
                "original parquet.",
            "summary": [
                "1930s palazzo · envelope renewed 2018",
                "7 m² balcony onto green courtyard",
                "Original oak parquet · exposed beams at the entrance",
                "12 m² cellar included",
                "Move-in ready · vacant at completion",
            ],
            "highlights": [
                ("Palazzo", "1932 · 24/7 porter"),
                ("Balcony", "7 m² green outlook"),
                ("Parquet", "Original, restored"),
                ("Floor", "3rd with lift"),
            ],
            "description":
                "An apartment in one of Crocetta's signature palazzi, "
                "two hundred metres from Corso Galileo Ferraris. Classic "
                "layout: entrance, living room with balcony, eat-in "
                "kitchen, corridor, two double bedrooms, bathroom with "
                "window. Original parquet in excellent shape, systems "
                "renewed in 2019.",
            "agent_name":  "Silvia Mondelli",
            "agent_role":  "Head of Turin office",
            "agent_phone": "+39 011 5328 4401",
        },
        {
            "slug":       "quadrilocale-isola-milano",
            "title":      "Four-bed with BAM view · Isola",
            "price":      "€ 780,000",
            "area":       "Milano · Isola · Via Confalonieri 25",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "135",
            "energy":     "A3",
            "floor":      "8th (double lift)",
            "badge":      "Park view",
            "reference":  "MI-1915",
            "year_built": "2019",
            "lead":
                "Apartment in a 2019 design development, main aspect "
                "onto the Library of Trees park. Four bedrooms, two "
                "bathrooms, eleven-metre liveable balcony. Rating A3, "
                "smart-home as standard.",
            "summary": [
                "BAM park view from the living room",
                "11 m² liveable balcony",
                "24-hour concierge building",
                "Garage included · EV charging point",
                "Rating A3 · integrated air con",
            ],
            "highlights": [
                ("View", "BAM and Bosco Verticale"),
                ("Concierge", "24-hour reception"),
                ("Charging", "EV point included"),
                ("Rating", "A3 · heat pump"),
            ],
            "description":
                "Eighth floor in a Piuarch-signed development with 24-hour "
                "concierge, shared gym and inner garden. Corner apartment "
                "with dual aspect: living area onto the BAM park, bedroom "
                "wing onto the inner courtyard. 11 m² balcony-loggia "
                "useable nine months a year. Custom furniture included "
                "as standard.",
            "agent_name":  "Sofia Ranieri",
            "agent_role":  "Agent · Milan North",
            "agent_phone": "+39 02 8765 4324",
        },
        {
            "slug":       "bilocale-porta-nuova",
            "title":      "Smart two-bed · Porta Nuova",
            "price":      "€ 520,000",
            "area":       "Milano · Porta Nuova · Via Melchiorre Gioia 62",
            "rooms":      "2",
            "bathrooms":  "1",
            "surface":    "68",
            "energy":     "A2",
            "floor":      "12th (Unicredit view)",
            "badge":      "Strong investment",
            "reference":  "MI-1967",
            "year_built": "2015",
            "lead":
                "Two-bed with 80 % south aspect, park and Porta Nuova "
                "skyline view. Ideal for a first purchase or a buy-to-"
                "let investment, expected gross yield 4.2 %.",
            "summary": [
                "South aspect · sun all day",
                "Unicredit and Diamante tower view",
                "Local concierge · shared gym",
                "Estimated buy-to-let yield 4.2 % gross",
                "Move-in ready · vacant at completion",
            ],
            "highlights": [
                ("Aspect", "Full south"),
                ("Floor", "12th skyline view"),
                ("Yield", "4.2 % gross expected"),
                ("Vacancy", "At completion"),
            ],
            "description":
                "68 m² two-bed with 32 m² skyline-facing living room, "
                "double bedroom with dressing room, windowed bathroom in "
                "grey stone. Serviced building with gym and lounge, day-"
                "time concierge seven days a week. Perfect for buyers "
                "working in the nearby towers, or anyone after a yielding "
                "investment.",
            "agent_name":  "Giulia Ferrante",
            "agent_role":  "Senior agent · Milan Centre",
            "agent_phone": "+39 02 8765 4322",
        },
        {
            "slug":       "villa-bellagio-lago",
            "title":      "Period villa with Spartivento view · Bellagio",
            "price":      "€ 1,950,000",
            "area":       "Como · Bellagio · Via Garibaldi 12",
            "rooms":      "6",
            "bathrooms":  "4",
            "surface":    "320",
            "energy":     "E",
            "floor":      "Detached villa · 3 levels + turret",
            "badge":      "Historic villa",
            "reference":  "CO-0248",
            "year_built": "1908 · conservative restoration 2017",
            "lead":
                "Liberty-style villa at Punta Spartivento, 320 covered "
                "metres plus turret belvedere, terraced garden with "
                "private lake access. 2017 conservative restoration with "
                "climate control and upgraded systems.",
            "summary": [
                "Punta Spartivento · dual lake view",
                "Terraced garden with private lake access",
                "360° panoramic turret belvedere",
                "2017 restoration with contemporary systems",
                "Six bedrooms, four bathrooms, historic cellar",
            ],
            "highlights": [
                ("Location", "Punta Spartivento"),
                ("View", "Dual lake"),
                ("Access", "Private lake"),
                ("Turret", "360° belvedere"),
            ],
            "description":
                "A signature villa of the Lake Como Liberty style, "
                "designed by architect Pietro Lingeri in 1908. Three "
                "liveable levels plus a turret belvedere, east aspect "
                "onto the Lecco branch and west onto the Como branch. "
                "The 2017 restoration preserved the original stucco, "
                "Liberty glazing and Venetian terrazzo floors, embedding "
                "hidden radiant heating and climate control.",
            "agent_name":  "Andrea Colombo",
            "agent_role":  "Senior agent · Lake Como",
            "agent_phone": "+39 031 2345 6789",
        },
        {
            "slug":       "appartamento-borgo-po-torino",
            "title":      "Apartment with Alpine view · Borgo Po",
            "price":      "€ 560,000",
            "area":       "Torino · Borgo Po · Corso Casale 102",
            "rooms":      "4",
            "bathrooms":  "2",
            "surface":    "145",
            "energy":     "D",
            "floor":      "5th (top · lift)",
            "badge":      "Hill view",
            "reference":  "TO-0945",
            "year_built": "1928 · apartment refurbished 2021",
            "lead":
                "Top floor with open view onto the Mole, Monte dei "
                "Cappuccini and the Alps. 145 m² on a single level, two "
                "liveable balconies, a classic layout kept in superb "
                "condition.",
            "summary": [
                "Alpine and Mole Antonelliana view from the living room",
                "Two liveable balconies · 6 + 4 m²",
                "3.20 m ceilings with original stucco",
                "2021 refurbishment · new systems",
                "Cellar and 18 m² attic included",
            ],
            "highlights": [
                ("View", "Alps and Mole"),
                ("Floor", "5th, top"),
                ("Ceilings", "3.20 m stucco"),
                ("Balconies", "Two liveable"),
            ],
            "description":
                "A corner top floor in a 1920s palazzo restored in 2020, "
                "four bedrooms laid out on a single level, dual aspect "
                "onto Corso Casale and Via Villa della Regina. Living "
                "area facing the Mole, sleeping area facing the hill. "
                "Original stucco kept intact in every room.",
            "agent_name":  "Luca Benedetti",
            "agent_role":  "Agent · Turin hillside",
            "agent_phone": "+39 011 5328 4402",
        },
        {
            "slug":       "villa-monza-brianza",
            "title":      "Detached villa with park · Monza",
            "price":      "€ 1,050,000",
            "area":       "Monza · San Fruttuoso · Via Buonarroti 48",
            "rooms":      "6",
            "bathrooms":  "4",
            "surface":    "280",
            "energy":     "B",
            "floor":      "Detached villa · 3 levels",
            "badge":      "Private park",
            "reference":  "MB-0177",
            "year_built": "2001 · upgrade 2022",
            "lead":
                "Detached villa on a 1,200-metre plot, landscaped park "
                "with mature trees, heated pool and children's play "
                "area. Three liveable floors plus games room and gym.",
            "summary": [
                "1,200 m² private park with heated pool",
                "Six bedrooms · four bathrooms · study · games room",
                "Gym and sauna in the basement level",
                "Rating B after 2022 envelope · 12 kW solar",
                "Triple garage and covered guest space",
            ],
            "highlights": [
                ("Park", "1,200 m² mature"),
                ("Pool", "Heated · 10 × 4.5"),
                ("Fitness", "Sauna · basement gym"),
                ("Rating", "B · 12 kW solar"),
            ],
            "description":
                "The villa is set in a residential neighbourhood ten "
                "minutes from central Monza and twenty from north Milan. "
                "A high-quality 2001 project, upgraded in 2022 with "
                "envelope, triple-glazed windows and solar photovoltaic. "
                "Ground floor with 120 m² living area facing the park, "
                "first floor with four bedrooms and three bathrooms, "
                "attic with study and guest bedroom.",
            "agent_name":  "Davide Orsini",
            "agent_role":  "Agent · Monza & Brianza",
            "agent_phone": "+39 039 5328 4403",
        },
        {
            "slug":       "monolocale-navigli-milano",
            "title":      "Signature studio on the canal bank · Navigli",
            "price":      "€ 295,000",
            "area":       "Milano · Navigli · Alzaia Naviglio Grande 76",
            "rooms":      "1",
            "bathrooms":  "1",
            "surface":    "42",
            "energy":     "C",
            "floor":      "2nd (historic spiral staircase)",
            "badge":      "Waterfront",
            "reference":  "MI-1994",
            "year_built": "1898 · 2018 restoration",
            "lead":
                "42 m² studio with picture window onto the Naviglio "
                "Grande bank, 2018 conservative restoration signed by "
                "Studio Ca' Rossa. Ideal as a first purchase or a short-"
                "let investment.",
            "summary": [
                "Direct canal-bank aspect · 2 × 1.5 m picture window",
                "1898 palazzo · original spiral staircase",
                "Integrated Boffi kitchen · serene-stone bathroom",
                "Ideal for a short-let investment",
                "Estimated 5.8 % gross yield",
            ],
            "highlights": [
                ("Aspect", "Naviglio Grande"),
                ("Palazzo", "1898, historic staircase"),
                ("Yield", "5.8 % gross"),
                ("Use", "Short-let / first home"),
            ],
            "description":
                "Studio set on the second floor of a historic palazzo "
                "right on the Naviglio Grande bank. Double-aspect "
                "picture window with restored guillotine sashes, "
                "polished original terracotta floors, built-in Boffi "
                "kitchen and a serene-stone bathroom. Suited to own use "
                "or a yielding investment: over the last three years "
                "short-let has stayed above 5.5 % gross.",
            "agent_name":  "Marco Lentini",
            "agent_role":  "Senior agent · Milan South",
            "agent_phone": "+39 02 8765 4323",
        },
        {
            "slug":       "attico-centro-torino",
            "title":      "Penthouse facing Palazzo Reale · Turin",
            "price":      "€ 780,000",
            "area":       "Torino · Centro · Piazzetta Reale 3",
            "rooms":      "3",
            "bathrooms":  "2",
            "surface":    "140",
            "energy":     "C",
            "floor":      "6th (top · lift)",
            "badge":      "Historic view",
            "reference":  "TO-0982",
            "year_built": "1874 · penthouse carved 2022",
            "lead":
                "Penthouse with liveable terrace facing Palazzo Reale, "
                "Duomo and Mole Antonelliana. 140 m² on a single level, "
                "carved from the historic loft in a 2022 project by "
                "Studio Isolarchitetti.",
            "summary": [
                "24 m² liveable terrace with Palazzo Reale view",
                "Carved from historic loft · 2022",
                "Three bedrooms, two bathrooms, standalone study",
                "Sloped ceilings with original exposed beams",
                "Rating C after 2022 roof insulation",
            ],
            "highlights": [
                ("View", "Palazzo Reale, Mole, Duomo"),
                ("Terrace", "24 m² liveable"),
                ("Beams", "Original, exposed"),
                ("Rating", "C post-insulation"),
            ],
            "description":
                "Penthouse carved from the loft of a seventeenth-century "
                "palazzo refurbished in 2022 by Isolarchitetti. Original "
                "larch beams kept, floor in polished terracotta laid in "
                "herringbone, bathrooms in Luserna stone. The panoramic "
                "terrace opens onto Piazzetta Reale and delivers a dual "
                "view across Mole and Duomo.",
            "agent_name":  "Silvia Mondelli",
            "agent_role":  "Head of Turin office",
            "agent_phone": "+39 011 5328 4401",
        },
        {
            "slug":       "loft-isola-milano",
            "title":      "Ex-workshop loft with courtyard · Isola",
            "price":      "€ 680,000",
            "area":       "Milano · Isola · Via Borsieri 32",
            "rooms":      "2",
            "bathrooms":  "2",
            "surface":    "115",
            "energy":     "B",
            "floor":      "Ground · private courtyard",
            "badge":      "Private courtyard",
            "reference":  "MI-2012",
            "year_built": "1927 · full conversion 2023",
            "lead":
                "Loft carved out of a former workshop with thirty metres "
                "of private courtyard, five-metre double height and "
                "original industrial windows. Full 2023 conversion, "
                "radiant heating and solar photovoltaic.",
            "summary": [
                "30 m² private courtyard · Mediterranean planting",
                "5 m double height · industrial windows",
                "2023 conversion · radiant heating and solar",
                "Open loft with enclosed suite · interior service bathroom",
                "Rating B · heat pump + 4 kW solar",
            ],
            "highlights": [
                ("Courtyard", "30 m² private"),
                ("Height", "5 m industrial"),
                ("Systems", "Radiant + solar"),
                ("Rating", "B · nearly off-grid"),
            ],
            "description":
                "The loft comes from the conversion of a 1927 mechanical "
                "workshop. Volumes kept untouched, minimal zoning with "
                "an enclosed suite behind a glass wall and an island "
                "kitchen at the centre. Thirty-metre private courtyard "
                "for exclusive use, with climbing plants, an outdoor "
                "cooktop and a polished-concrete bench. A slice of the "
                "Milan that was and the Milan becoming.",
            "agent_name":  "Sofia Ranieri",
            "agent_role":  "Agent · Milan North",
            "agent_phone": "+39 02 8765 4324",
        },
    ],
}

# Phase 2g3.7 · Session 53 · D-047 compliance closing comment:
# All user-visible literals in skin + preview compositions MUST be sourced
# from this content tree (or chrome / dna.content). No "Brera" / "Turin"
# / "Milan" / "beds" / "Book viewing" / "m²" may appear hard-coded
# in the HTML. Review in every PR touching real-estate/mass-market.
