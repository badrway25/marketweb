"""Template DNA registry — per-template differentiation system.

Each template in the marketplace has a unique "DNA" — a structured set of
design decisions (layout archetype, hero style, navbar style, density, tone,
conversion pattern, ...) that makes it perceptibly different from every other
template in the same category. Without it, sibling templates collapse into
recolors of the same skeleton; with it, they become distinct products.

Why a Python registry, not a model field?
-----------------------------------------
The DNA needs to be reviewed in code (it drives layout files), versioned
alongside HTML compositions, and editable without a migration. A future
iteration can promote it to a `JSONField` on `TemplateBrand` once the
vocabulary stabilises and marketing wants admin-side editing.

Conventions
-----------
- Each entry is keyed by `WebTemplate.slug`.
- `archetype` is the most important field: it picks which HTML composition
  the preview generator will render. The composition file path is
    templates/preview_compositions/<category>/<archetype>.html
- `imagery_key` is the lookup key into `preview_imagery.IMAGERY_CONFIG`. This
  lets two templates in the same category use distinct photo pools.
- `font_pairing` overrides what the generator would otherwise infer from
  `TemplateBrand.typography`. Pair = (heading, body) Google Font families.
- `content` is the per-template copy block. Hero headline, eyebrow, CTAs,
  cards, doctors, prices, navbar links, etc. Compositions read it via
  `{{ dna.content.* }}`.
- Templates without a DNA entry fall back to the legacy per-category
  composition (`templates/preview_compositions/<category>.html`). The system
  is therefore strictly additive — adding DNA never breaks existing previews.

Adding a new template
---------------------
1. Decide which archetype it belongs to (or design a new one).
2. Add an entry below.
3. If you invented a new archetype, add the matching HTML composition under
   `templates/preview_compositions/<category>/<archetype>.html`.
4. (Optional) Add a dedicated `imagery_key` in
   `apps/catalog/preview_imagery.IMAGERY_CONFIG`.
5. Re-run `python manage.py generate_previews --force --only <slug>`.
"""
from __future__ import annotations

from typing import Any

# ---------------------------------------------------------------------------
# Vocabulary — allowed values for each DNA dimension.
# Keep these in sync with BRAND_SYSTEM_GUIDELINES.md.
# ---------------------------------------------------------------------------

LAYOUT_ARCHETYPES: dict[str, str] = {
    # Medical pilot
    "clinic":     "Multi-specialty clinic — split hero with embedded booking widget.",
    "family":     "Family/pediatric practice — soft, warm, portrait-led, pastel.",
    "specialist": "High-end specialist — editorial magazine layout with serif drama.",
    "wellness":   "Wellness/holistic centre — spa-like with treatment pricelist.",
    # Restaurant pilot
    "fine-dining":    "Editorial tasting-menu venue — serif drama, full-bleed plate, numbered courses, concierge tile.",
    "trattoria-warm": "Family trattoria — handwritten chalkboard daily menu, family portraits, warm hours strip.",
    "street-modern":  "Fast-casual street food — bold display type, tilted product cutout, order-now grid + delivery strip.",
}

HERO_STYLES: dict[str, str] = {
    "split-booking":         "50/50 photo + headline + booking card overlap.",
    "centered-soft":         "Rounded portrait card + warm headline + accent CTA.",
    "editorial-serif":       "Huge serif headline left, intimate portrait right.",
    "full-bleed-manifesto":  "Full-bleed photo + centered manifesto overlay.",
    "editorial-plate":       "Full-bleed plate photo right + huge serif manifesto headline left + course index gutter.",
    "warm-photo-frame":      "Photo card left + warm chalkboard headline & daily menu right.",
    "product-cutout":        "Tilted product photo right + giant condensed display headline left + price badge.",
}

NAVBAR_STYLES: dict[str, str] = {
    "solid-phone":     "Solid colored bar with prominent phone number CTA.",
    "pill-floating":   "Floating rounded pill navbar, transparent over hero.",
    "minimal-serif":   "Centered serif logo with thin underline rule.",
    "soft-pastel":     "Translucent bar, soft pastel link colors, no hard edges.",
    "serif-centered":  "Centered serif wordmark with hairline rule and small reservation link right.",
    "warm-bar":        "Cream sticky bar with handwritten brand on left and big phone CTA on right.",
    "bold-pill":       "Black pill nav floating top, bright accent ORDER button on the right.",
}

FOOTER_STYLES: dict[str, str] = {
    "corporate-4col":   "Four columns: brand / specialties / contact / legal.",
    "compact-2col":     "Brand + opening hours, single line copyright.",
    "centered-minimal": "Centered logo, single legal line.",
    "spa-social":       "Social row + newsletter + minimal links.",
    "concierge-press":  "Concierge tile + press logos band.",
    "hours-warm":       "Hours strip + WhatsApp + map (warm cream).",
    "delivery-strip":   "Delivery partner logos + counter status + order CTA.",
}

CARD_STYLES: dict[str, str] = {
    "icon-grid":       "4-up cards with icon, title, blurb, link arrow.",
    "portrait-stack":  "3-up portrait cards with name + role + bio.",
    "editorial-large": "2-up oversized cards with serif numeral + caption.",
    "pricelist":       "Two-column menu: name+desc left, dotted leader, price right.",
    "course-index":    "Numbered serif course list with name + paired wine + ingredient line.",
    "chalkboard-day":  "Daily-special chalkboard cards with handwritten dish name + price tag.",
    "product-grid":    "Square product cards with photo + price + Add button.",
}

BUTTON_STYLES: dict[str, str] = {
    "rounded-solid":     "10px radius, solid accent fill.",
    "pill-soft":         "999px pill, soft pastel fill.",
    "ghost-underline":   "Transparent, accent text, animated underline.",
    "square-bold":       "0px radius, heavy border, primary fill.",
    "ghost-gold-serif":  "Underline serif text in gold accent — concierge style.",
    "rustic-rounded":    "Warm rounded button with red fill and slight tilt.",
    "block-bold":        "Heavy block button, bright accent fill, arrow icon, no radius.",
}

DENSITY_PROFILES: dict[str, str] = {
    "compact":   "Tight spacing, dense grids, more content per fold.",
    "medium":    "Balanced rhythm, default for most business templates.",
    "airy":      "Generous whitespace, larger gaps, fewer items per row.",
    "very-airy": "Editorial scale — huge gaps, large type, max breathing room.",
}

TONES: dict[str, str] = {
    "institutional":  "Authoritative, formal, third-person, evidence-led.",
    "warm-family":    "Personal, second-person, reassuring, child-friendly.",
    "prestigious":    "Editorial, expert, restrained, status-led.",
    "serene":         "Sensorial, slow-paced, nature-led, mindful.",
    "editorial-chef": "Aulic, sensorial, restrained, chef-as-author.",
    "familiar-warm":  "Caloroso, dialettale, di casa, alla mano.",
    "energetic-bold": "Brutale, urbano, scanzonato, no-nonsense.",
}

CONVERSION_PATTERNS: dict[str, str] = {
    "booking-widget":         "Embedded date/time/specialty selector in hero.",
    "phone-and-chat":         "Prominent phone CTA + WhatsApp/chat pill.",
    "private-request":        "Underline link 'Richiedi visita privata' + email.",
    "calendar-spot":           "Inline mini-calendar with bookable spots.",
    "concierge-reservation":  "Concierge tile + email + 'Riserva la serata' link, no public form.",
    "phone-and-whatsapp":     "Giant phone number + WhatsApp pill, family-style.",
    "order-now-delivery":     "ORDINA ORA primary CTA + delivery partners strip + counter status.",
}

IMAGERY_DIRECTIONS: dict[str, str] = {
    "institutional-clinic": "Bright clinic interiors, doctors in coats, equipment.",
    "family-warmth":        "Pediatricians with kids, families, soft daylight.",
    "editorial-portrait":   "Single specialist portrait, low-key, magazine cover energy.",
    "spa-nature":           "Stone, water, plants, candles, slow tactile imagery.",
    "moody-plated":         "Dark plated dishes, low-key tungsten light, fine-dining mood.",
    "rustic-trattoria":     "Warm wood tables, hands kneading dough, terra-cotta tones.",
    "street-pop-product":   "Bold burger / pizza / fritti cutouts, daylight high-contrast.",
}


# ---------------------------------------------------------------------------
# Per-template DNA registry
# ---------------------------------------------------------------------------

TEMPLATE_DNA: dict[str, dict[str, Any]] = {

    # ─────────────────────────────────────────────────────────────
    # Medical pilot — 4 distinct archetypes
    # ─────────────────────────────────────────────────────────────

    # ── 1) CLINIC — multi-specialty institutional ────────────────
    "salute-studio-medico": {
        "archetype":          "clinic",
        "hero_style":         "split-booking",
        "navbar_style":       "solid-phone",
        "footer_style":       "corporate-4col",
        "section_order":      ["hero", "stats", "specialties", "doctors", "partners", "footer"],
        "card_style":         "icon-grid",
        "button_style":       "rounded-solid",
        "density":            "medium",
        "tone":               "institutional",
        "imagery_direction":  "institutional-clinic",
        "imagery_key":        "medical",
        "conversion_pattern": "booking-widget",
        "font_pairing":       ("Nunito Sans", "Inter"),
        "content": {
            "eyebrow":       "Poliambulatorio · Milano Centrale",
            "headline":      'La tua salute, la nostra <em>missione</em>',
            "subhead":       "Oltre 40 specialisti, percorsi diagnostici integrati e un'esperienza paziente pensata per metterti a tuo agio dal primo contatto.",
            "primary_cta":   "Prenota una visita",
            "secondary_cta": "Tutti i servizi",
            "phone":         "Numero verde 800 123 456",
            "stats": [
                ("40+", "Specialisti"),
                ("12",  "Reparti"),
                ("98%", "Pazienti soddisfatti"),
            ],
            "specialties": [
                ("Cardiologia",  "Visite, ECG e diagnostica avanzata."),
                ("Pediatria",    "Cura dell'infanzia e bilanci di salute."),
                ("Diagnostica",  "Ecografia, TAC e risonanza in giornata."),
                ("Fisioterapia", "Riabilitazione personalizzata in équipe."),
            ],
            "booking_widget": {
                "title":  "Prenota online",
                "fields": [
                    ("Specialità", "Cardiologia"),
                    ("Data",        "Mar 14 Apr · 10:30"),
                    ("Dottore",     "Dr.ssa Conti"),
                ],
                "cta":    "Conferma prenotazione",
            },
            "nav_links": ["Specialità", "Equipe medica", "Convenzioni", "Area paziente", "Contatti"],
        },
    },

    # ── 2) WELLNESS — holistic centre, pricelist-led ─────────────
    "benessere-centro-olistico": {
        "archetype":          "wellness",
        "hero_style":         "full-bleed-manifesto",
        "navbar_style":       "pill-floating",
        "footer_style":       "spa-social",
        "section_order":      ["hero", "manifesto", "pricelist", "therapists", "footer"],
        "card_style":         "pricelist",
        "button_style":       "pill-soft",
        "density":            "airy",
        "tone":               "serene",
        "imagery_direction":  "spa-nature",
        "imagery_key":        "medical-wellness",
        "conversion_pattern": "calendar-spot",
        "font_pairing":       ("Cormorant Garamond", "Nunito"),
        "content": {
            "eyebrow":       "Centro olistico · Bergamo Alta",
            "headline":      'Equilibrio fra <em>corpo, mente</em> e respiro',
            "subhead":       "Trattamenti su misura ispirati alle tradizioni mediterranee e orientali, in un rifugio fuori dal tempo a 800 metri sul livello del mare.",
            "primary_cta":   "Riserva il tuo benessere",
            "secondary_cta": "Scarica il listino",
            "phone":         "+39 035 412 998",
            "treatments": [
                ("Massaggio Mediterraneo", "55 min · olio d'oliva e agrumi",   "€ 85"),
                ("Rituale Hammam",          "90 min · vapore, sale e argilla",  "€ 120"),
                ("Riequilibrio Energetico", "60 min · pranoterapia e respiro",  "€ 95"),
                ("Idroterapia Alpina",      "75 min · acque sorgive",           "€ 110"),
            ],
            "therapists": [
                ("Sara Conti",  "Naturopata · 12 anni"),
                ("Davide Lai",  "Osteopata D.O."),
                ("Yara Bonomi", "Operatrice ayurveda"),
            ],
            "nav_links": ["Filosofia", "Trattamenti", "Listino", "Diario", "Prenota"],
        },
    },

    # ── 3) FAMILY — pediatric / family practice ──────────────────
    "famiglia-pediatria": {
        "archetype":          "family",
        "hero_style":         "centered-soft",
        "navbar_style":       "soft-pastel",
        "footer_style":       "compact-2col",
        "section_order":      ["hero", "intro-trio", "doctors", "hours", "footer"],
        "card_style":         "portrait-stack",
        "button_style":       "pill-soft",
        "density":            "airy",
        "tone":               "warm-family",
        "imagery_direction":  "family-warmth",
        "imagery_key":        "medical-family",
        "conversion_pattern": "phone-and-chat",
        "font_pairing":       ("Quicksand", "Nunito"),
        "content": {
            "eyebrow":       "Studio pediatrico · Torino Crocetta",
            "headline":      'Cresciamo <em>insieme</em> ai vostri bambini',
            "subhead":       "Tre pediatre, una psicomotricista e un'infermiera dedicata. Visite tranquille, tempi lunghi, ascolto vero — perché ogni famiglia merita un punto di riferimento.",
            "primary_cta":   "Chiama lo studio",
            "secondary_cta": "Scrivi su WhatsApp",
            "phone":         "011 549 21 88",
            "intro_trio": [
                ("Neonato",     "Bilanci, allattamento, sonno"),
                ("Bambino",     "Vaccinazioni e crescita"),
                ("Adolescente", "Prevenzione e ascolto"),
            ],
            "doctors": [
                ("Dr.ssa Elisa Rambaldi", "Pediatra di famiglia",      "Nutrizione infantile"),
                ("Dr.ssa Marta Greco",     "Pediatra · Allergologa",    "Asma e dermatiti"),
                ("Dr.ssa Lucia Sferra",    "Pediatra · Endocrinologa",  "Crescita e pubertà"),
            ],
            "hours": [
                ("Lun – Ven", "8:30 – 12:30  ·  15:00 – 19:00"),
                ("Sabato",     "9:00 – 12:00  · solo urgenze"),
                ("Domenica",   "Reperibilità telefonica"),
            ],
            "nav_links": ["Lo studio", "Le pediatre", "Servizi", "Orari", "Scrivici"],
        },
    },

    # ─────────────────────────────────────────────────────────────
    # Restaurant pilot — 3 distinct archetypes
    # (fine-dining · trattoria-warm · street-modern)
    # ─────────────────────────────────────────────────────────────

    # ── R1) FINE DINING — editorial tasting menu ─────────────────
    "gusto-fine-dining": {
        "archetype":          "fine-dining",
        "hero_style":         "editorial-plate",
        "navbar_style":       "serif-centered",
        "footer_style":       "concierge-press",
        "section_order":      ["nav", "editorial-hero", "course-index", "concierge", "press"],
        "card_style":         "course-index",
        "button_style":       "ghost-gold-serif",
        "density":            "very-airy",
        "tone":               "editorial-chef",
        "imagery_direction":  "moody-plated",
        "imagery_key":        "restaurant-fine",
        "conversion_pattern": "concierge-reservation",
        "font_pairing":       ("Playfair Display", "Lato"),
        "content": {
            "eyebrow":       "Tavolo unico · Milano Brera · 14 coperti",
            "headline":      'Una serata in <em>otto atti.</em>',
            "subhead":       "Un menù degustazione che cambia ogni due settimane secondo il mercato del giorno. Solo cena. Solo prenotazione. Solo per quattordici.",
            "primary_cta":   "Riserva la serata",
            "secondary_cta": "Lo chef",
            "phone":         "+39 02 3611 9920",
            "chef_name":     "Lorenzo Fioravanti",
            "chef_role":     "Chef patron · 1 stella Michelin",
            "courses": [
                ("I",   "Ostrica & cetriolo",          "acetosella, perle di yuzu",        "Champagne Selosse"),
                ("II",  "Risotto al midollo",           "estratto di prezzemolo, caffè",     "Soave Pieropan '21"),
                ("III", "Capesanta arrostita",          "burro nocciola, capperi di Pantelleria", "Riesling Pacherhof"),
                ("IV",  "Piccione di Bresse",           "fichi neri, cardamomo verde",      "Barolo Cannubi '17"),
                ("V",   "Cioccolato 80%",               "olio EVO, sale Maldon",             "Marsala Vintage '99"),
            ],
            "concierge": {
                "label":  "Concierge personale",
                "name":   "Greta Vallesi",
                "role":   "Maître & cellar manager",
                "email":  "greta@osteriamoderna.it",
            },
            "press": ["GUIDA MICHELIN", "GAMBERO ROSSO", "IDENTITÀ GOLOSE", "CORRIERE LIVING", "VOGUE FOOD"],
            "nav_links": ["Filosofia", "Menu degustazione", "Carta dei vini", "Le sale", "Riserva"],
        },
    },

    # ── R2) TRATTORIA-WARM — family chalkboard ───────────────────
    "sapore-trattoria-pizzeria": {
        "archetype":          "trattoria-warm",
        "hero_style":         "warm-photo-frame",
        "navbar_style":       "warm-bar",
        "footer_style":       "hours-warm",
        "section_order":      ["warm-nav", "framed-hero", "daily-chalkboard", "family-strip", "hours-band"],
        "card_style":         "chalkboard-day",
        "button_style":       "rustic-rounded",
        "density":            "medium",
        "tone":               "familiar-warm",
        "imagery_direction":  "rustic-trattoria",
        "imagery_key":        "restaurant-trattoria",
        "conversion_pattern": "phone-and-whatsapp",
        "font_pairing":       ("Caveat", "Inter"),
        "content": {
            "eyebrow":       "Trattoria di famiglia · Trastevere · dal 1987",
            "headline":      'Da Nonna Rosa, come a casa <em>vostra.</em>',
            "subhead":       "Pasta tirata a mano la mattina, pizza in forno a legna la sera, e un bicchiere di vino della casa offerto a chi torna due volte.",
            "primary_cta":   "Chiama: 06 581 4488",
            "secondary_cta": "WhatsApp",
            "phone":         "06 581 4488",
            "daily_specials": [
                ("Lun", "Cacio e pepe",          "tonnarelli tirati a mano",   "€ 10"),
                ("Mar", "Bucatini all'amatriciana", "guanciale di Amatrice",      "€ 11"),
                ("Mer", "Coda alla vaccinara",    "ricetta di Nonna Rosa",      "€ 14"),
                ("Gio", "Gnocchi al sugo d'arrosto","fatti al mattino",         "€ 11"),
                ("Ven", "Baccalà in pastella",    "pomodorini confit",          "€ 13"),
            ],
            "family": [
                ("Nonna Rosa",   "Pasta fresca dal '87"),
                ("Marco Trezzi", "Pizzaiolo · forno a legna"),
                ("Giulia Trezzi","Sala e dolci di casa"),
            ],
            "hours": [
                ("Mar – Sab", "12:30 – 15:00  ·  19:00 – 23:30"),
                ("Domenica",  "12:30 – 15:00 (solo pranzo)"),
                ("Lunedì",    "Riposo settimanale"),
            ],
            "review_quote": "«Mi sono sentito nella cucina della nonna che non ho mai avuto.»",
            "review_author": "Gambero Rosso · Tre Spicchi",
            "nav_links": ["La storia", "I piatti", "Pizza la sera", "Eventi", "Trovaci"],
        },
    },

    # ── R3) STREET-MODERN — fast-casual product grid ────────────
    "brace-street-food-lab": {
        "archetype":          "street-modern",
        "hero_style":         "product-cutout",
        "navbar_style":       "bold-pill",
        "footer_style":       "delivery-strip",
        "section_order":      ["bold-nav", "cutout-hero", "product-grid", "delivery-strip"],
        "card_style":         "product-grid",
        "button_style":       "block-bold",
        "density":            "compact",
        "tone":               "energetic-bold",
        "imagery_direction":  "street-pop-product",
        "imagery_key":        "restaurant-street",
        "conversion_pattern": "order-now-delivery",
        "font_pairing":       ("Big Shoulders Display", "Inter"),
        "content": {
            "eyebrow":       "Street food lab · Bologna · Via Indipendenza 42",
            "headline":      'BRUCIATO AL <em>FUOCO VIVO.</em>',
            "subhead":       "Smashburger di scottona piemontese, focacce al taglio, fritti contro corrente. Ordini al banco, ritiri al numero, divori al volo.",
            "primary_cta":   "Ordina ora",
            "secondary_cta": "Vedi il menu",
            "phone":         "Bologna · 12:00 → 24:00 · ogni giorno",
            "hero_badge_price": "€ 9.50",
            "hero_badge_label": "DOPPIO BRACE",
            "products": [
                ("DOPPIO BRACE",  "Doppia scottona, cheddar fuso, salsa Brace",     "€ 9.50", "TOP"),
                ("FRITTO MISTO",  "Crocchette di patata, jalapeño, baccalà",        "€ 6.00", ""),
                ("PIZZA AL TAGLIO","Pomodoro San Marzano DOP, fior di latte",       "€ 4.50", "VEG"),
                ("SODA BRACE",     "Limonata fatta in casa con basilico",            "€ 3.00", "NEW"),
            ],
            "delivery_partners": ["GLOVO", "DELIVEROO", "JUSTEAT", "UBER EATS"],
            "counter_status_label": "CODA AL BANCO",
            "counter_status_value": "≈ 4 MIN",
            "stat_blocks": [
                ("12.000",  "burger / mese"),
                ("4.9 ★",   "su 1.380 recensioni"),
                ("100%",    "scottona piemontese"),
            ],
            "nav_links": ["IL LAB", "MENU", "STORE", "ORDINA"],
        },
    },

    # ── 5) SPECIALIST (derm) — archetype reuse validation ────────
    # Second template on the `specialist` archetype. Proves that a new
    # multi-page template can ship with ZERO new HTML files: same chrome,
    # different brand / palette / content / tone / font pairing.
    "dermatologia-elite-roma": {
        "archetype":          "specialist",
        "hero_style":         "editorial-serif",
        "navbar_style":       "minimal-serif",
        "footer_style":       "centered-minimal",
        "section_order":      ["nav", "editorial-hero", "drop-cap", "fields", "press", "footer"],
        "card_style":         "editorial-large",
        "button_style":       "ghost-underline",
        "density":            "very-airy",
        "tone":               "prestigious",
        "imagery_direction":  "editorial-portrait",
        "imagery_key":        "medical-specialist",
        "conversion_pattern": "private-request",
        "font_pairing":       ("Bodoni Moda", "Inter"),
        "content": {
            "eyebrow":       "Dermatologia clinica · Roma Veneto",
            "headline":      'La pelle è una <em>carta d\'identità.</em> La leggiamo per intero.',
            "subhead":       "Dermatologia clinica, chirurgica ed estetica in un unico studio privato a Via Veneto. Mappa nei digitale, chirurgia in day-hospital, laser e medicina estetica dermatologica.",
            "primary_cta":   "Richiedi visita privata",
            "phone":         "+39 06 487 2311",
            "drop_cap":      "O",
            "intro_paragraph": (
                "gni pelle racconta una storia che è scritta dall'ambiente, dal tempo, "
                "dai geni e dalle abitudini. Il dermatologo è il lettore di quella storia — "
                "con il dermatoscopio, con le mani, con l'occhio allenato di chi ha visto "
                "decine di migliaia di pazienti. Allo Studio Ricciardi non abbiamo mai "
                "fretta di concludere una visita."
            ),
            "fields": [
                ("01", "Mappatura nevi digitale", "Videodermatoscopia ad alta risoluzione di tutti i nevi con archiviazione digitale e confronto con l'archivio storico del paziente."),
                ("02", "Chirurgia dermatologica in day-hospital", "Escissione di lesioni sospette in anestesia locale con esame istologico dedicato e chirurgia plastica ricostruttiva inclusa."),
            ],
            "press": ["JAMA Dermatology", "British Journal of Dermatology", "Vanity Fair Wellness", "Corriere Salute", "Vogue Italia"],
            "nav_links": ["Studio", "Visite", "Pubblicazioni", "Contatti"],
        },
    },

    # ── 4) SPECIALIST — editorial high-end ───────────────────────
    "cardio-studio-specialistico": {
        "archetype":          "specialist",
        "hero_style":         "editorial-serif",
        "navbar_style":       "minimal-serif",
        "footer_style":       "centered-minimal",
        "section_order":      ["nav", "editorial-hero", "drop-cap", "fields", "press", "footer"],
        "card_style":         "editorial-large",
        "button_style":       "ghost-underline",
        "density":            "very-airy",
        "tone":               "prestigious",
        "imagery_direction":  "editorial-portrait",
        "imagery_key":        "medical-specialist",
        "conversion_pattern": "private-request",
        "font_pairing":       ("Cormorant Garamond", "Inter"),
        "content": {
            "eyebrow":       "Cardiologia clinica · Roma Parioli",
            "headline":      'Una cardiologia <em>su misura</em>, per chi non accetta scorciatoie.',
            "subhead":       "Visite specialistiche, secondi pareri, programmi di prevenzione individuale. Una sola agenda, un solo medico, una sola firma.",
            "primary_cta":   "Richiedi visita privata",
            "phone":         "+39 06 320 1144",
            "drop_cap":      "L",
            "intro_paragraph": (
                "a cardiologia non è una catena di montaggio. È un dialogo lungo, "
                "fatto di tempo, di anamnesi paziente, di esami letti due volte. "
                "Lo Studio Marani da quindici anni accompagna pazienti pubblici e "
                "privati in un percorso di prevenzione cardiovascolare costruito "
                "su misura — con discrezione e con metodo."
            ),
            "fields": [
                ("01", "Visita cardiologica completa", "Anamnesi estesa, ECG, refertazione e piano di follow-up con timeline personalizzata."),
                ("02", "Secondo parere specialistico",  "Per pazienti con diagnosi complesse o terapie multiple già in corso."),
            ],
            "press": ["LANCET", "European Heart Journal", "Corriere Salute", "Sole 24 Ore", "RAI Med"],
            "nav_links": ["Studio", "Visite", "Pubblicazioni", "Contatti"],
        },
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_dna(slug: str) -> dict[str, Any] | None:
    """Return the DNA dict for a template slug, or None if unregistered."""
    return TEMPLATE_DNA.get(slug)


def has_dna(slug: str) -> bool:
    return slug in TEMPLATE_DNA


def archetypes_for_category(category_slug: str) -> list[str]:
    """Return the set of distinct archetypes registered in a category.

    Used for documentation / coverage reports — e.g. how many archetypes
    are filled in a given category compared to the target.
    """
    archetypes: set[str] = set()
    for slug, dna in TEMPLATE_DNA.items():
        # We don't store category in DNA, so this needs the WebTemplate.
        # The selectors layer can build the mapping. Kept here as a stub.
        archetypes.add(dna["archetype"])
    return sorted(archetypes)
