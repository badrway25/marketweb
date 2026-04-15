"""Sapore — Trattoria Da Nonna Rosa (trattoria-warm archetype) — IT content tree.

Phase 2g3.6 — Restaurant live-completion (Session 48, 2026-04-15).

Voice contract (IT):
- Roman family-trattoria register, warm and proud, never aulico.
- "voi/tu" inclusive — the trattoria speaks like a friendly family, never
  marketing-speak. "Da Nonna Rosa, come a casa vostra." vibe.
- Concrete details: Trastevere, Via dei Salumi, forno a legna, guanciale
  di Amatrice, cesanese del Lazio, Cacio e pepe, Coda alla vaccinara.
- Phone-and-WhatsApp conversion pattern: big phone number in the nav CTA,
  WhatsApp as secondary on every page, "Prenota un tavolo" primary CTA —
  never a cart, never checkout, never e-commerce.

Differentiation contract vs Gusto (D-054 enforcement):
- Sapore is warm-cream-paper with hand-lettered touches (Caveat script).
  Gusto is dark editorial charcoal with Playfair italic drama.
- Sapore imagery: hands on dough, family tavolata, terracotta plates in
  sunlight, forno a legna burning, straw-covered Cesanese bottles.
  Gusto imagery: plated dark-backdrop signature courses, chef's portrait
  in low-key light. Imagery pools must NOT overlap.
- Sapore CTA pattern: phone + WhatsApp (warm, immediate, call-by-name).
  Gusto CTA pattern: concierge booking (private, appointment-only).
- Sapore vocabulary: trattoria · nonna · casa · forno · cacio · guanciale
  · cesanese · tavolata · coperti · famiglia. Gusto vocabulary: atti ·
  menù degustazione · sommelier · stella · cantina · maître · private.

Differentiation contract vs Brace (street-modern):
- Brace is black-pill energetic bold-typographic pop with neon-yellow
  accents and order-now flows. Sapore is warm cream rustic editorial
  with a rosso-casa accent and reservation flows.
- Sapore has no product-grid cards, no delivery strip, no QR menu.
  Brace has no family portraits, no chalkboard script, no tavolata band.
"""
from __future__ import annotations

from typing import Any


SAPORE_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Casa",               "kind": "home"},
        {"slug": "menu",     "label": "Menu",               "kind": "menu"},
        {"slug": "storia",   "label": "La storia",          "kind": "about"},
        {"slug": "forno",    "label": "Pizza & pasta",      "kind": "signature"},
        {"slug": "eventi",   "label": "Tavolate & eventi",  "kind": "events"},
        {"slug": "contatti", "label": "Trovaci & prenota",  "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "R",
        "logo_word":    "Trattoria Da Nonna Rosa",
        "tag":          "Trattoria di famiglia · Trastevere · dal 1987",
        "phone":        "06 581 4488",
        "phone_tel":    "+390658144880",
        "whatsapp":     "06 581 4488",
        "whatsapp_link": "https://wa.me/390658144880",
        "email":        "ciao@trattoriadanonnarosa.it",
        "address":      "Via dei Salumi 16/a · 00153 Roma · Trastevere",
        "hours_compact": "Mar – Sab · 12:30 – 15:00 · 19:00 – 23:30",
        "hours_footer_rows": [
            "Domenica · solo pranzo · 12:30 – 15:00",
            "Lunedì · riposo settimanale",
        ],
        "license":      "P.IVA 07634211006 · CCIAA Roma REA 1138992",
        "footer_intro":
            "Trattoria di famiglia aperta nel 1987 da Rosa Trezzi. Pasta tirata "
            "ogni mattina al mattarello, pizza nel forno a legna la sera, vino "
            "della casa offerto a chi torna due volte. Sessanta coperti, due "
            "sale, tre generazioni in cucina.",
        "nav_cta":      "Prenota un tavolo",
        "nav_cta_href": "contatti",
        "nav_phone_cta": "Chiama: 06 581 4488",
        "star_line":    "Trattoria di famiglia · dal 1987",
        "copyright":    "© 2026 Trattoria Da Nonna Rosa · P. IVA 07634211006",

        # Mirror the fine-dining _base.html footer keys used by the chrome
        "footer_hours_1": "Mar – Sab · pranzo & cena",
        "footer_hours_2": "Domenica · solo pranzo",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Trattoria di famiglia · Trastevere · dal 1987",
        "headline": "Da Nonna Rosa, <em>come a casa vostra.</em>",
        "intro":
            "Pasta tirata al mattarello ogni mattina, pizza nel forno a legna la "
            "sera, e un bicchiere di vino della casa offerto a chi torna due volte. "
            "Sessanta coperti, due sale, tre generazioni in cucina.",
        "primary_cta":   "Prenota un tavolo",
        "primary_href":  "contatti",
        "secondary_cta": "Scrivici su WhatsApp",
        "secondary_href_is_whatsapp": True,

        # Hero photo-frame
        "hero_image":   "https://images.unsplash.com/photo-1481931098730-318b6f776db0?w=1600&q=80&auto=format&fit=crop",
        "hero_caption": "Cacio e pepe del martedì · tonnarelli tirati al mattarello",
        "hero_stamp":   "Dal 1987",

        # Facts band — 3 numbers/claims
        "facts": [
            ("1987",   "anno in cui Rosa ha aperto la cucina"),
            ("60",     "coperti in due sale · nessuna prenotazione oltre le venti"),
            ("3",      "generazioni di famiglia in cucina"),
        ],

        # Chalkboard — 5 daily specials lun → ven
        "chalkboard_label":   "La lavagna della settimana",
        "chalkboard_heading": "Piatto del giorno, <em>scritto a mano.</em>",
        "chalkboard_intro":
            "Ogni mattina Nonna Rosa scrive la lavagna con il gesso, decidendo "
            "al banco cosa cuciniamo oggi. Questa settimana gira così.",
        "chalkboard_buongiorno": "Buon appetito!",
        "chalkboard_days": [
            ("Lun",  "Cacio e pepe",              "tonnarelli tirati a mano",             "€ 10,00"),
            ("Mar",  "Bucatini all'amatriciana",  "guanciale di Amatrice di Sarnelli",    "€ 11,00"),
            ("Mer",  "Coda alla vaccinara",       "ricetta di Nonna Rosa, come nel 1987", "€ 14,00"),
            ("Gio",  "Gnocchi al sugo d'arrosto", "fatti al mattino con le patate vecchie","€ 11,00"),
            ("Ven",  "Baccalà in pastella",       "pomodorini confit e carciofo romano",  "€ 13,00"),
        ],

        # Family strip — 3 portraits with personal blurbs
        "family_label":   "La famiglia in cucina",
        "family_heading": "Tre generazioni, <em>una sola tavolata.</em>",
        "family": [
            {
                "name":   "Rosa Trezzi",
                "role":   "Pasta fresca dal 1987",
                "blurb":
                    "Nonna Rosa apre la trattoria il 3 settembre 1987 con un sogno "
                    "e due mattarelli. Oggi ha ottantadue anni e tira ancora la pasta "
                    "ogni mattina dalle sette. Il suo motto è semplice: «la pasta "
                    "buona la senti sotto le mani, non ti serve la bilancia».",
                "portrait": "https://images.unsplash.com/photo-1604908554027-b6e7c2c5db1f?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Marco Trezzi",
                "role":   "Pizzaiolo · forno a legna dal 2003",
                "blurb":
                    "Figlio di Rosa, cresciuto tra farina e mattoni. Accende il forno "
                    "ogni pomeriggio alle quattro — quercia del Cimino, mai altro — e "
                    "lo tiene vivo fino a mezzanotte. La sua Margherita verace è "
                    "imparata da Peppe Guida a Vico Equense nel 2008.",
                "portrait": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Giulia Trezzi",
                "role":   "Sala & dolci di casa",
                "blurb":
                    "Nipote di Rosa, trent'anni, si occupa della sala e dei dolci. "
                    "Tiramisù con mascarpone di Sarnelli, crostata di visciole quando "
                    "la stagione c'è, maritozzi con la panna solo il sabato mattina. "
                    "Vi accoglie con un sorriso e una caraffa d'acqua frizzante.",
                "portrait": "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Forno teaser band
        "forno_label":   "Il forno a legna",
        "forno_heading": "Acceso ogni pomeriggio alle <em>quattro in punto.</em>",
        "forno_text":
            "Il forno a cupola di Marco è in mattoni del Viterbese, costruito a mano "
            "dal pizzaiolo Gennaro Esposito nel 2003. Brucia solo quercia del Cimino, "
            "raggiunge i 420° e fa la pizza in sessanta secondi. Da martedì a sabato, "
            "solo la sera, quando la prima sala si svuota del pranzo.",
        "forno_image":    "https://images.unsplash.com/photo-1593504049359-74330189a345?w=1200&q=80&auto=format&fit=crop",
        "forno_caption":  "Margherita verace · 420° · sessanta secondi",
        "forno_cta":      "Scopri pizza & pasta",
        "forno_cta_href": "forno",

        # Reviews band — 2–3 quotes
        "reviews_label": "Si parla di noi",
        "reviews": [
            {
                "quote":  "Mi sono sentito nella cucina della nonna che non ho mai avuto.",
                "author": "Gambero Rosso · Tre Spicchi 2024",
            },
            {
                "quote":  "Una delle ultime trattorie vere di Trastevere. Andateci a piedi, la sera, e ordinate la coda.",
                "author": "Corriere della Sera · Cook",
            },
            {
                "quote":  "La carbonara di Rosa fa tacere tutti, anche quelli di Testaccio.",
                "author": "Puntarella Rossa · 2025",
            },
        ],

        # Hours strip — 3 rows under reviews
        "hours_label":  "Quando siamo aperti",
        "hours_rows": [
            ("Mar – Sab",   "12:30 – 15:00", "pranzo"),
            ("Mar – Sab",   "19:00 – 23:30", "cena · forno a legna"),
            ("Domenica",    "12:30 – 15:00", "solo pranzo · chiusura 16:00"),
        ],
        "hours_note": "Lunedì riposo settimanale · aperti tutte le feste comandate tranne Natale",

        # Tavolata band — group experience teaser
        "tavolata_label":   "La tavolata",
        "tavolata_heading": "Dodici amici, <em>un tavolo solo.</em>",
        "tavolata_text":
            "La tavolata è il nostro tavolo lungo da dodici posti nella sala del "
            "camino. Menu fisso a trentadue euro, vino della casa incluso, dolci "
            "di Giulia a chiusura. Per compleanni, comunioni, cene di classe o "
            "semplicemente perché oggi è un giorno buono per stare insieme.",
        "tavolata_cta":      "Organizza una tavolata",
        "tavolata_cta_href": "eventi",
        "tavolata_image":    "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=1200&q=80&auto=format&fit=crop",

        # Final CTA band
        "cta_label":    "Venite a trovarci",
        "cta_heading":  "Via dei Salumi sedici, <em>suonate forte.</em>",
        "cta_intro":
            "Siamo in Via dei Salumi, a due passi dal lungotevere. La porta è di "
            "legno verde, il campanello fa rumore: non abbiate timore, suonate "
            "forte. Vi facciamo trovare un bicchiere di Cesanese fresco e una "
            "fetta di pizza rossa appena uscita dal forno.",
        "cta_primary":      "Prenota un tavolo",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Scrivi su WhatsApp",
    },

    # ─── MENU ────────────────────────────────────────────────────
    "menu": {
        "eyebrow":  "Il menu · stagione autunno '26",
        "headline": "Pasta tirata a mano, pizza al forno a legna, <em>dolci di casa.</em>",
        "intro":
            "Il menu cambia poco perché i piatti di casa sono quelli: cacio e pepe, "
            "amatriciana, carbonara, coda, saltimbocca. Le pizze girano secondo "
            "la stagione. Tutto il resto lo decide Nonna Rosa al banco, la mattina.",

        "wine_house_label":   "Vino della casa",
        "wine_house_heading": "Cesanese del Lazio, <em>sfuso, € 18,00 al litro.</em>",
        "wine_house_text":
            "Il vino della casa viene da Olevano Romano, dalla cantina Proietti "
            "Riccardi, che lo fa da quarant'anni. Lo serviamo in caraffa da litro, "
            "mezzo o quartino. Bianco: Malvasia Puntinata dei Castelli, Cantina "
            "Ribelà, sfuso anche lui.",

        "allergen_note":
            "I piatti contrassegnati con (G) contengono glutine, (L) lattosio, "
            "(P) pesce. In caso di allergie particolari, chiedete al banco "
            "prima di ordinare: Rosa ha fatto un corso HACCP nel 2019 e sa "
            "tutto.",

        "sections": [
            {
                "label": "Antipasti di casa",
                "heading": "Dall'orto e dal banco",
                "dishes": [
                    ("Bruschetta al pomodoro",       "pomodorini del Piennolo, basilico, olio EVO Sabina DOP", "€ 7,00"),
                    ("Carciofo alla giudia",         "carciofo romano, fritto due volte, limone di Amalfi",    "€ 9,00"),
                    ("Suppli classico",              "riso, mozzarella filante, ragù di carne della casa",     "€ 4,00"),
                    ("Fiori di zucca fritti",        "ripieni di mozzarella e acciuga, pastella leggera",      "€ 8,00"),
                    ("Puntarelle alla romana",       "acciughe del Cantabrico, aglio, aceto rosso",            "€ 8,00"),
                    ("Tagliere di salumi & formaggi","guanciale di Amatrice, pecorino di Pienza, olive",       "€ 14,00"),
                    ("Polpette di Nonna Rosa",       "sugo di pomodoro, pane casareccio a fianco",             "€ 10,00"),
                ],
            },
            {
                "label": "Primi di pasta tirata a mano",
                "heading": "Dal mattarello del mattino",
                "dishes": [
                    ("Cacio e pepe",                 "tonnarelli tirati al mattarello, pecorino di Pienza",    "€ 12,00"),
                    ("Carbonara classica",           "guanciale di Amatrice, pecorino romano, tuorli 5",       "€ 13,00"),
                    ("Bucatini all'amatriciana",     "guanciale, pomodoro San Marzano, pecorino",              "€ 12,00"),
                    ("Gnocchi al sugo d'arrosto",    "fatti al mattino, sugo del giovedì di Rosa",             "€ 11,00"),
                    ("Fettuccine alla papalina",     "prosciutto crudo, piselli freschi, uova, parmigiano",    "€ 13,00"),
                    ("Rigatoni con la pajata",       "intestino di vitello da latte, sugo di pomodoro",        "€ 15,00"),
                    ("Tonnarelli al cacio e tartufo","tartufo nero di Norcia, pecorino, pepe",                 "€ 18,00"),
                ],
            },
            {
                "label": "Pizza dal forno a legna",
                "heading": "Solo la sera · martedì → sabato",
                "dishes": [
                    ("Margherita verace",            "pomodoro San Marzano, fiordilatte, basilico",            "€ 9,00"),
                    ("Capricciosa di Nonna Rosa",    "carciofi, funghi, prosciutto cotto, uovo",               "€ 12,00"),
                    ("Diavola al guanciale",         "pomodoro, fiordilatte, salame piccante, guanciale",      "€ 11,00"),
                    ("Bianca al cacio e pepe",       "fiordilatte, pecorino, pepe nero di Pondichéry",         "€ 10,00"),
                    ("Nonna Rosa (firma)",           "stracciatella di Andria, pomodorini semi-dry, basilico", "€ 13,00"),
                    ("Zucca e salsiccia",            "crema di zucca, salsiccia di Norcia, rosmarino",         "€ 12,00"),
                ],
            },
            {
                "label": "Secondi dal banco",
                "heading": "Dalla cucina della domenica",
                "dishes": [
                    ("Saltimbocca alla romana",      "vitello, prosciutto crudo, salvia, vino bianco",         "€ 16,00"),
                    ("Coda alla vaccinara",          "coda di bue, sedano, cacao, pinoli, uvetta",             "€ 17,00"),
                    ("Abbacchio a scottadito",       "costolette di agnello, rosmarino, limone",               "€ 19,00"),
                    ("Trippa alla romana",           "trippa, sugo di pomodoro, mentuccia, pecorino",          "€ 14,00"),
                    ("Baccalà in pastella",          "baccalà mantecato, pastella leggera, pomodorini",        "€ 14,00"),
                ],
            },
            {
                "label": "Dolci di casa",
                "heading": "Le mani di Giulia",
                "dishes": [
                    ("Tiramisù di Giulia",           "mascarpone di Sarnelli, savoiardi, caffè della moka",    "€ 6,00"),
                    ("Panna cotta alla vaniglia",    "con visciole di Nonna Rosa",                             "€ 5,00"),
                    ("Crostata di visciole",         "pasta frolla di casa, visciole del 2025",                "€ 6,00"),
                    ("Maritozzo con la panna",       "solo il sabato mattina · panna fresca di Valentini",     "€ 4,00"),
                    ("Gelato del nonno",             "tre gusti · fior di latte, nocciola, cioccolato",        "€ 5,00"),
                ],
            },
        ],
    },

    # ─── STORIA (about) ──────────────────────────────────────────
    "storia": {
        "eyebrow":  "La storia · dal 1987",
        "headline": "Quarant'anni di pasta tirata <em>al mattarello.</em>",
        "intro":
            "Trattoria Da Nonna Rosa apre il 3 settembre 1987 in due stanze di "
            "Via dei Salumi, ereditate dalla madre di Rosa Trezzi. Trent'anni "
            "dopo, siamo ancora qui, nella stessa cucina, con un forno in più "
            "e tre generazioni di famiglia che si alternano al banco.",

        "story": [
            "Rosa Trezzi nasce a Roma nel 1944, figlia di un oste di Testaccio. "
            "Cresce tra pentole, mattarelli e il rumore del mercato di Porta "
            "Portese. A quindici anni sposa Marino, che faceva il panettiere, "
            "e con lui apre una prima osteria in Via dei Foraggi. Dura sei "
            "anni, fino al 1987, quando il padre di Marino lascia in eredità "
            "due stanze in Via dei Salumi, a Trastevere.",

            "Il 3 settembre 1987 la trattoria apre al numero sedici/a, con "
            "dodici coperti, un forno a gas e un frigorifero a muro. Il menu "
            "della prima sera è scritto a penna su un foglio di carta oleata: "
            "cacio e pepe, amatriciana, coda alla vaccinara, e un tiramisù "
            "fatto con il mascarpone del lattaio sotto casa. Costo totale "
            "della cena: quattromila lire.",

            "Nel 2003 il figlio Marco rileva la seconda sala — l'officina di "
            "un falegname che aveva chiuso — e costruisce il forno a legna "
            "con il pizzaiolo Gennaro Esposito, che era venuto a Roma per un "
            "matrimonio. Da quell'estate, la pizza entra nel menu solo la "
            "sera, martedì e sabato. Poi tutte le sere, dal 2005.",

            "Nel 2024 Giulia, nipote di Rosa, torna da Barcellona dove "
            "lavorava in pasticceria e prende in mano la sala e i dolci. "
            "Oggi la trattoria ha sessanta coperti, tre generazioni, un "
            "forno a legna, un cameriere storico — Beppe, dal 1996 — e il "
            "solito cartello sulla porta: chi torna due volte, il vino della "
            "casa è offerto.",
        ],

        # Timeline — 3 steps
        "timeline_label":   "Tre date",
        "timeline": [
            {
                "year":  "1987",
                "title": "Rosa apre al sedici/a",
                "desc":  "Tre settembre, dodici coperti, quattromila lire a testa. Il primo menu è scritto a penna su carta oleata.",
            },
            {
                "year":  "2003",
                "title": "Arriva il forno a legna",
                "desc":  "Marco rileva la seconda sala e costruisce il forno con Gennaro Esposito. Prima Margherita: ventidue giugno.",
            },
            {
                "year":  "2024",
                "title": "Giulia torna a casa",
                "desc":  "Giulia rientra da Barcellona e prende la sala. Primo maritozzo del sabato: ventisei ottobre.",
            },
        ],

        # Family portraits (reused shape from home but with longer blurbs)
        "family_label":   "Le mani che ti servono",
        "family": [
            {
                "name":   "Rosa Trezzi",
                "role":   "Fondatrice · pasta fresca dal 1987",
                "blurb":
                    "Ottantadue anni, un nipote per ogni dito della mano, e il "
                    "mattarello che conosce a memoria. Tira la pasta ogni mattina "
                    "dalle sette alle dieci, poi passa a scrivere la lavagna del "
                    "giorno. La carbonara la fa solo lei: è un rito geloso.",
                "portrait": "https://images.unsplash.com/photo-1604908554027-b6e7c2c5db1f?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Marco Trezzi",
                "role":   "Pizzaiolo · forno a legna dal 2003",
                "blurb":
                    "Cresciuto in trattoria, falegname per tre anni, poi "
                    "pizzaiolo per ventidue. Accende il forno alle sedici, "
                    "fa scoppiettare la quercia del Cimino, e impasta a mano "
                    "con lievito madre del 2008. La Margherita la infila a "
                    "occhi chiusi in sessanta secondi.",
                "portrait": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Giulia Trezzi",
                "role":   "Sala & dolci · dal 2024",
                "blurb":
                    "Due anni da Josep Maria in pasticceria a Barcellona, "
                    "poi il ritorno. Si occupa della sala con il cameriere "
                    "Beppe, prepara i dolci del giorno e decide la carta "
                    "dei vini. Fa il miglior maritozzo a ovest del Tevere, "
                    "ma solo il sabato mattina.",
                "portrait": "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Valori grid — 4 cards
        "values_label":   "Le nostre regole",
        "values_heading": "Quattro cose <em>che non cambiano.</em>",
        "values": [
            {
                "title": "Impasto della pasta",
                "desc":
                    "Farina del Molino Paolo Mariani, acqua di Roma, tuorli di "
                    "Paolo Parisi. Tirata al mattarello ogni mattina dalle sette. "
                    "Mai essiccata, mai surgelata, mai del giorno prima.",
            },
            {
                "title": "Il forno a legna",
                "desc":
                    "Solo quercia del Cimino, tagliata a Vitorchiano. Acceso "
                    "ogni pomeriggio alle quattro in punto. Se il forno non "
                    "prende i 420°, quella sera la pizza non esce — punto.",
            },
            {
                "title": "Vino della casa",
                "desc":
                    "Cesanese di Olevano Romano da Proietti Riccardi, "
                    "Malvasia dei Castelli da Cantina Ribelà. Sfuso in "
                    "caraffa. Diciotto euro al litro, la stessa cifra dal 2019.",
            },
            {
                "title": "La regola del bicchiere",
                "desc":
                    "Chi torna due volte, il vino della casa è offerto. È "
                    "scritto sulla lavagna, c'è dal primo giorno, non l'abbiamo "
                    "mai cambiato. Anche se ti riconosciamo, chiedilo lo stesso.",
            },
        ],

        "photo_image":   "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1600&q=80&auto=format&fit=crop",
        "photo_caption": "La sala del camino · cena del sabato · novembre 2025",
    },

    # ─── FORNO (signature · pizza & pasta) ────────────────────────
    "forno": {
        "eyebrow":  "Pizza & pasta · le firme della casa",
        "headline": "Quattro pizze e quattro paste <em>scritte a mano.</em>",
        "intro":
            "Le nostre firme sono otto — quattro dal forno, quattro dal "
            "mattarello. Non cambiano, non scalano, non girano. Sono i "
            "piatti che Nonna Rosa ha deciso nel 1987 e su cui la famiglia "
            "si gioca la reputazione da quarant'anni.",

        # Pizza section
        "pizza_label":   "Dal forno a legna",
        "pizza_heading": "Quattro pizze <em>d'autore di casa.</em>",
        "pizza_intro":
            "Il forno a legna di Marco brucia solo quercia del Cimino, "
            "raggiunge i 420° e fa la pizza in sessanta secondi. Impasto a "
            "24 ore di lievitazione con lievito madre del 2008. Pomodoro "
            "San Marzano dop, fiordilatte Agerola da Sorrentina.",
        "pizza_signatures": [
            {
                "n":     "I",
                "name":  "Margherita verace",
                "desc":  "Pomodoro San Marzano DOP, fiordilatte di Agerola, basilico genovese DOP, olio EVO Sabina a freddo.",
                "price": "€ 9,00",
            },
            {
                "n":     "II",
                "name":  "Capricciosa di Nonna Rosa",
                "desc":  "Carciofi romani saltati, funghi champignon, prosciutto cotto di Prato, uovo biologico di Parisi al centro.",
                "price": "€ 12,00",
            },
            {
                "n":     "III",
                "name":  "Diavola al guanciale",
                "desc":  "Pomodoro, fiordilatte, salame piccante di Amatrice, guanciale di Sarnelli, peperoncino di Diamante.",
                "price": "€ 11,00",
            },
            {
                "n":     "IV",
                "name":  "Nonna Rosa (firma della casa)",
                "desc":  "Stracciatella di Andria a crudo, pomodorini semi-dry, basilico, olio EVO Sabina, scorza di limone di Amalfi.",
                "price": "€ 13,00",
            },
        ],

        # Pasta section
        "pasta_label":   "Dal mattarello",
        "pasta_heading": "Quattro paste <em>tirate a mano dalle sette.</em>",
        "pasta_intro":
            "Pasta tirata al mattarello ogni mattina dalle sette alle "
            "dieci. Farina del Molino Paolo Mariani, acqua di Roma, tuorli "
            "di Paolo Parisi. Mai essiccata, mai surgelata, mai del giorno "
            "prima.",
        "pasta_signatures": [
            {
                "n":     "I",
                "name":  "Cacio e pepe",
                "desc":  "Tonnarelli tirati al mattarello, pecorino di Pienza DOP, pepe nero di Pondichéry macinato al momento.",
                "price": "€ 12,00",
            },
            {
                "n":     "II",
                "name":  "Carbonara classica",
                "desc":  "Spaghetti, guanciale di Amatrice, pecorino romano, cinque tuorli di Parisi, pepe nero. Niente panna mai.",
                "price": "€ 13,00",
            },
            {
                "n":     "III",
                "name":  "Bucatini all'amatriciana",
                "desc":  "Bucatini del molino, guanciale di Amatrice croccante, San Marzano, pecorino romano grattugiato al piatto.",
                "price": "€ 12,00",
            },
            {
                "n":     "IV",
                "name":  "Fettuccine alla papalina",
                "desc":  "Fettuccine, prosciutto crudo San Daniele, piselli freschi, uova, parmigiano reggiano 36 mesi.",
                "price": "€ 13,00",
            },
        ],

        # Forno story
        "forno_story_label":   "Il forno a legna",
        "forno_story_heading": "Quattrocentoventi gradi, <em>sessanta secondi.</em>",
        "forno_story_text_1":
            "Il forno a cupola di Marco è stato costruito a mano nel 2003 dal "
            "pizzaiolo Gennaro Esposito, mattone per mattone, con terra "
            "refrattaria di Viterbo. Misura due metri e dieci di diametro, "
            "cuoce sei pizze per volta, raggiunge i 420 gradi con una cesta "
            "di quercia del Cimino tagliata a Vitorchiano.",
        "forno_story_text_2":
            "Acceso ogni pomeriggio alle quattro in punto. Se alle sei non "
            "ha ancora raggiunto la temperatura, quella sera la pizza non "
            "esce — è capitato tre volte in ventidue anni, l'ultima nel "
            "febbraio 2024 con la bufera di neve, e abbiamo fatto tutti "
            "pasta quella sera.",
        "forno_story_image":
            "https://images.unsplash.com/photo-1571997478779-2adcbbe9ab2f?w=1600&q=80&auto=format&fit=crop",
        "forno_story_caption": "Quercia del Cimino · forno a 420° · luglio 2025",

        # Ingredients/producers band
        "producers_label":   "Cinque mani che firmano",
        "producers_heading": "Da dove vengono, <em>e da chi.</em>",
        "producers": [
            {
                "name":       "Sarnelli Guanciale",
                "place":      "Amatrice · Lazio",
                "ingredient": "Guanciale di maiale nero casertano · stagionatura 90 giorni",
            },
            {
                "name":       "Molino Paolo Mariani",
                "place":      "Barchi · Marche",
                "ingredient": "Farina tipo 0 e 00 · grano Senatore Cappelli · macinata a pietra",
            },
            {
                "name":       "Proietti Riccardi",
                "place":      "Olevano Romano · Lazio",
                "ingredient": "Cesanese del Lazio sfuso · vigne ad alberello · annata 2024",
            },
            {
                "name":       "Caseificio Sorrentina",
                "place":      "Agerola · Campania",
                "ingredient": "Fiordilatte di bufala campana · consegna giornaliera",
            },
            {
                "name":       "Paolo Parisi",
                "place":      "Usigliano di Lari · Toscana",
                "ingredient": "Uova di gallina nutrita a latte di capra · tuorlo arancione",
            },
        ],

        # Dough photo
        "dough_image":   "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=1600&q=80&auto=format&fit=crop",
        "dough_caption": "Impasto a 24 ore · lievito madre del 2008",
    },

    # ─── EVENTI (events & tavolate) ──────────────────────────────
    "eventi": {
        "eyebrow":  "Tavolate & eventi · gruppi dai dodici ai sessanta",
        "headline": "Una tavolata lunga, <em>tutti seduti vicini.</em>",
        "intro":
            "La sala del camino si apre per le tavolate dai dodici posti in su. "
            "Menu fisso, vino della casa incluso, dolci di Giulia a chiusura. "
            "Per compleanni, comunioni, cene di classe, addii al celibato, "
            "cene aziendali — o semplicemente perché stare insieme fa bene.",

        # 3 group experiences
        "experiences_label":   "Tre formule",
        "meta_menu_label":     "Menu",
        "meta_wine_label":     "Vini",
        "experiences": [
            {
                "n":       "01",
                "title":   "Tavolata lunga",
                "persons": "da 12 a 20 persone",
                "menu":    "Antipasto misto, due primi a scelta, secondo, dolce · € 32,00",
                "wine":    "Cesanese della casa + acqua inclusi",
                "desc":
                    "La formula storica: tavolo lungo nella sala del camino, "
                    "portate a condividere, tempi tranquilli. Perfetta per "
                    "compleanni, cene di classe, addii al celibato. Si "
                    "prenota con quattro giorni di anticipo.",
            },
            {
                "n":       "02",
                "title":   "Comunione & battesimo",
                "persons": "da 20 a 40 persone",
                "menu":    "Buffet di antipasti, due primi, due secondi, torta · € 48,00",
                "wine":    "Cesanese + Malvasia + bibite incluse · bollicine a parte",
                "desc":
                    "Due sale aperte su misura, bambini benvenuti, torta di "
                    "Giulia inclusa nel menu (scegli fra tre: ricotta e visciole, "
                    "cioccolato e pere, millefoglie alla vaniglia). Si "
                    "prenota con due settimane di anticipo.",
            },
            {
                "n":       "03",
                "title":   "Cena aziendale",
                "persons": "da 25 a 60 persone",
                "menu":    "Menu degustazione cinque portate · € 62,00",
                "wine":    "Abbinamento dal sommelier di casa · quattro calici",
                "desc":
                    "Privatizzazione completa della trattoria, una sera "
                    "infrasettimanale (mar–gio). Menu in tre lingue se serve, "
                    "proiettore per presentazioni, Wi-Fi libero. Si prenota "
                    "con un mese di anticipo.",
            },
        ],

        # Birthday/celebration block
        "birthday_label":   "Compleanni & anniversari",
        "birthday_heading": "Torta di Giulia, candele, <em>e un brindisi con Nonna Rosa.</em>",
        "birthday_text":
            "Per ogni compleanno, Giulia prepara una torta su misura (comunica "
            "con due giorni di anticipo il gusto preferito). La portiamo con le "
            "candele accese, Nonna Rosa esce dalla cucina per il brindisi, "
            "e se sei fortunato ti canta anche una strofa di Roma nun fa' la "
            "stupida stasera — ma solo se glielo chiedi tu, perché con noi "
            "non lo fa mai.",
        "birthday_image":   "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=1200&q=80&auto=format&fit=crop",
        "birthday_caption": "Torta di ricotta e visciole · sessantesimo compleanno di Beppe",

        # Contact card specific to events
        "contact_label":    "Per organizzare una tavolata",
        "contact_heading":  "Parla direttamente <em>con Giulia.</em>",
        "contact_text":
            "Le tavolate e gli eventi li gestisce Giulia in persona. Chiamala "
            "fra le dieci e le dodici del mattino (è l'ora in cui non è ancora "
            "in sala) o scrivile su WhatsApp: ti risponde entro il pomeriggio. "
            "Se l'email è più comoda, va bene anche quella.",
        "contact_phone":    "06 581 4488",
        "contact_whatsapp": "06 581 4488",
        "contact_email":    "eventi@trattoriadanonnarosa.it",
        "contact_cta":      "Scrivi a Giulia",
        "contact_cta_href": "contatti",
    },

    # ─── CONTATTI (reservations + find us) ────────────────────────
    "contatti": {
        "eyebrow":  "Trovaci & prenota · Via dei Salumi 16/a",
        "headline": "Prenota un tavolo, <em>o vieni e basta.</em>",
        "intro":
            "Siamo in Via dei Salumi, a Trastevere, cinque minuti a piedi dal "
            "lungotevere. Se vieni in due o in tre non serve prenotare: entri, "
            "ti trovi un tavolo. Dai quattro in su, meglio una telefonata il "
            "giorno prima. Per gruppi oltre i dodici, vai alla pagina tavolate.",

        # Address card
        "address_label":   "Dove siamo",
        "address_heading": "Via dei Salumi 16/a",
        "address_text":
            "A Trastevere, fra Piazza dei Mercanti e il lungotevere Ripa. "
            "La porta è di legno verde, il campanello fa rumore. "
            "Metropolitana B fermata Circo Massimo (dieci minuti a piedi), "
            "tram 8 fermata Belli (quattro minuti), autobus H fermata Sonnino.",
        "address_city":    "00153 Roma · Trastevere",

        # Hours table — 4 rows
        "hours_label":   "Orari di apertura",
        "hours_heading": "Pranzo & cena, <em>lunedì riposo.</em>",
        "hours_table": [
            ("Martedì – Sabato", "12:30 – 15:00",         "pranzo"),
            ("Martedì – Sabato", "19:00 – 23:30",         "cena · forno a legna acceso"),
            ("Domenica",         "12:30 – 15:00",         "solo pranzo · chiusura 16:00"),
            ("Lunedì",           "chiuso",                "riposo settimanale"),
        ],

        # Phone/WhatsApp/email card
        "contact_label":     "Parla con noi",
        "contact_heading":   "Tre modi, <em>tutti buoni.</em>",
        "contact_phone_label":    "Chiama al banco",
        "contact_phone_value":    "06 581 4488",
        "contact_phone_hours":    "Risponde Giulia dalle 10 alle 23",
        "contact_whatsapp_label": "Scrivi su WhatsApp",
        "contact_whatsapp_value": "06 581 4488",
        "contact_whatsapp_hours": "Ti rispondiamo entro un'ora",
        "contact_email_label":    "Scrivici una email",
        "contact_email_value":    "ciao@trattoriadanonnarosa.it",
        "contact_email_hours":    "Rispondiamo entro il giorno dopo",

        # Reservation form
        "form_label":    "Prenota online",
        "form_heading":  "Prenota un tavolo, <em>scriviamo noi sulla lavagna.</em>",
        "form_intro":
            "Compila il modulo qui sotto. Riceverai una conferma per SMS o "
            "WhatsApp entro due ore (siamo in cucina, ma i telefoni li "
            "guardiamo). Per gruppi oltre i dodici, scrivici direttamente "
            "su WhatsApp.",

        "form_sections": [
            {
                "num":   "01",
                "title": "Chi sei",
                "meta":  "Per confermarti il tavolo",
                "fields": ["name", "email", "phone"],
            },
            {
                "num":   "02",
                "title": "Quando vieni",
                "meta":  "Data, ora e quanti siete",
                "fields": ["date", "time", "people"],
            },
            {
                "num":   "03",
                "title": "Note",
                "meta":  "Occasione, allergie, preferenze",
                "fields": ["occasion", "notes"],
            },
        ],

        "form_fields": [
            {
                "name":     "name",
                "label":    "Nome e cognome",
                "type":     "text",
                "placeholder": "Come ti chiamiamo al tavolo",
                "required": True,
                "helper":   "Lo scriviamo sulla lavagna delle prenotazioni.",
            },
            {
                "name":     "email",
                "label":    "Email",
                "type":     "email",
                "placeholder": "nome@esempio.it",
                "required": True,
                "helper":   "Ti mandiamo la conferma qui.",
            },
            {
                "name":     "phone",
                "label":    "Telefono o WhatsApp",
                "type":     "tel",
                "placeholder": "+39 333 123 45 67",
                "required": True,
                "helper":   "Ti cerchiamo qui solo in caso di imprevisto.",
            },
            {
                "name":     "date",
                "label":    "Data",
                "type":     "date",
                "placeholder": "gg/mm/aaaa",
                "required": True,
                "helper":   "Siamo chiusi il lunedì.",
            },
            {
                "name":     "time",
                "label":    "Ora",
                "type":     "time",
                "placeholder": "es. 20:30",
                "required": True,
                "helper":   "Pranzo 12:30–14:30 · cena 19:00–22:30.",
            },
            {
                "name":     "people",
                "label":    "Quanti siete",
                "type":     "number",
                "placeholder": "numero di coperti",
                "required": True,
                "helper":   "Oltre i dodici, scrivi direttamente su WhatsApp.",
            },
            {
                "name":     "occasion",
                "label":    "Occasione",
                "type":     "select",
                "placeholder": "",
                "required": False,
                "full_width": True,
                "helper":   "Se è un compleanno, prepariamo la torta di Giulia.",
            },
            {
                "name":     "notes",
                "label":    "Note per la cucina",
                "type":     "textarea",
                "placeholder": "Allergie, piatti preferiti, richieste particolari…",
                "required": False,
                "full_width": True,
                "helper":   "Nonna Rosa ha fatto il corso HACCP nel 2019: diccelo e basta.",
            },
        ],

        "occasion_options": [
            "Cena normale",
            "Compleanno",
            "Anniversario",
            "Cena di lavoro",
            "Prima volta da noi",
            "Tavolata (12+)",
            "Altro",
        ],

        "consent":
            "Acconsento al trattamento dei dati per gestire la prenotazione "
            "(nessuna newsletter, nessuna pubblicità, mai).",
        "form_submit":      "Prenota il tavolo",
        "form_submit_note": "Ti confermiamo entro due ore, per SMS o WhatsApp.",

        # Map
        "map_label":    "In mappa",
        "map_heading":  "Via dei Salumi 16/a · Trastevere",
        "map_embed":
            "https://www.openstreetmap.org/export/embed.html"
            "?bbox=12.4660%2C41.8880%2C12.4720%2C41.8910"
            "&layer=mapnik&marker=41.8893%2C12.4690",
        "map_link":     "Apri su OpenStreetMap",
        "map_link_href":"https://www.openstreetmap.org/?mlat=41.8893&mlon=12.4690#map=17/41.8893/12.4690",

        # Getting-here notes
        "transport_label":   "Come arrivare",
        "transport_heading": "Tre modi, <em>tutti a piedi dal centro.</em>",
        "transport": [
            {
                "mode":  "Metropolitana",
                "line":  "B · fermata Circo Massimo",
                "note":  "Dieci minuti a piedi lungo via di Monte Savello e il lungotevere Ripa.",
            },
            {
                "mode":  "Tram",
                "line":  "8 · fermata Belli",
                "note":  "Quattro minuti a piedi, attraversando Piazza Trilussa verso Via dei Salumi.",
            },
            {
                "mode":  "Autobus",
                "line":  "H · fermata Sonnino",
                "note":  "Sei minuti a piedi, passando per Piazza in Piscinula.",
            },
            {
                "mode":  "A piedi dal centro",
                "line":  "Ponte Sisto · quindici minuti",
                "note":  "Da Piazza Navona, attraversando Campo de' Fiori e il ponte Sisto.",
            },
        ],
    },

    # No blog
    "posts": [],
}
