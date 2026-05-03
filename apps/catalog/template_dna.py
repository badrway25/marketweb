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
    # Ecommerce pilot
    "fashion-editorial": "High-fashion monobrand store — fully dark magazine cover with gold accents and italic serif drama.",
    "artisan-workshop":  "Handmade bottega — fully warm cream page with typographic hero, rubber-stamped info panel and labeled edition cards.",
    # Business hardening wave (Phase 2g2x)
    "corporate-suite":        "Board advisory / consulting suite — institutional navy band, photo-led hero with boardroom portrait, serif headline, advisory pillar cards + KPI strip over industry-sectors ribbon.",
    "startup-saas-landing":   "Conversion-first landing for SaaS & startups — cosmic gradient page, typographic manifesto hero with NO big photo, product mockup card overlap, feature pills, metric strip, pricing teaser + live ship log.",
    # Portfolio hardening wave (Phase 2g2x)
    "editorial-designer-grid": "Independent designer / art director studio — cream paper page with typographic drama, NO big hero photo, numbered project ledger in a 4-column index and clients/sector ribbon. Systemic, editorial, case-study driven.",
    "cinematic-photographer":  "Photographer / visual storyteller portfolio — fully dark page with a dominant fullbleed image hero carrying EXIF credit meta, image-first filmstrip gallery, series counter and a minimal ghost CTA. Atmospheric, cinematic, gallery-led.",
    # Agency live rollout (Phase 2g3.6f)
    "agency-creative-studio":  "Independent creative agency / brand studio — editorial ink page with oversized serif italic pull-quote hero, selected-work cover tile, press ribbon and indexed case-study ledger. Concept-led, curatorial, strategy-driven.",
    "agency-digital-studio":   "Digital / product / growth studio — midnight-violet page with product-dashboard hero, sprint telemetry chips, capability grid and live ship-log. Momentum-led, product-minded, delivery-driven.",
    # Lawyer live rollout (Phase 2g3.7)
    "classic-gold":            "Istituzionale studio legale — ink page with gold monogram crest, serif drama headline, vertical rule ledger, numbered practice areas and partner portrait cards. Forensic, notarile, high-trust.",
    "modern-transparent":      "Avvocato contemporaneo — bright advisory page with confident sans-serif kinetic headline, strategy-manifesto eyebrow, sector grid, process sprint and outcome metric band. Modern, advisory, solution-led.",
    # Real estate live rollout (Phase 2g3.7)
    "mass-market":             "Agenzia immobiliare accessibile — daylight page with hero search-widget over cover photo, listings tile grid with specs/price ribbon, neighborhood map cards and agent portrait strip. Practical, market-smart, visit-first.",
    "ultra-luxury-cinematic":  "Immobiliare di lusso — fullbleed editorial cover hero with champagne wordmark, rarefied property-dossier cards, continental locations ribbon and private viewing request. Cinematic, aspirational, concierge-led.",
}

HERO_STYLES: dict[str, str] = {
    "split-booking":         "50/50 photo + headline + booking card overlap.",
    "centered-soft":         "Rounded portrait card + warm headline + accent CTA.",
    "editorial-serif":       "Huge serif headline left, intimate portrait right.",
    "full-bleed-manifesto":  "Full-bleed photo + centered manifesto overlay.",
    "editorial-plate":       "Full-bleed plate photo right + huge serif manifesto headline left + course index gutter.",
    "warm-photo-frame":      "Photo card left + warm chalkboard headline & daily menu right.",
    "product-cutout":        "Tilted product photo right + giant condensed display headline left + price badge.",
    "split-executive":           "55/45 split: serif drama headline + meta strip left + full-bleed boardroom photo right with credit ribbon.",
    "centered-manifesto-product": "Centered typographic manifesto with feature pills + product-mockup dashboard card overlapping the hero bottom. No big hero photo.",
    "typographic-index-ledger":  "Huge display headline over a cream page with a numbered project index on the right — NO big hero photo, project names and numbers are the hero.",
    "fullbleed-exif":            "Fullbleed dominant photo with a film-style EXIF credit bar along the bottom edge — no text over image except a small series counter and ghost CTA.",
    "editorial-quote-cover":     "Oversized serif italic pull-quote left + a framed selected-work cover tile right with editorial credit strip — no product UI, press ribbon below.",
    "product-console-hero":      "Bold sans-serif kinetic headline left + dashboard-chrome product card right with live metric + a delivery-cadence status chip pinned bottom-left.",
    "split-ledger-monogram":     "Dark ink split hero with serif drama headline + vertical gold rule on the left + partner monogram crest and practice-areas ledger on the right. Notarile, studio-legale mood.",
    "centered-advisory-manifesto":"Bright advisory page with centered sans-serif kinetic headline + confident sector pills + strategic process sprint card below the fold. No big hero photo — headline is the hero.",
    "search-listings-grid":      "Cover photo hero with a translucent search widget overlay (location/type/price/rooms) and a 3- or 4-up listings tile grid immediately below. Market-first, visit-first.",
    "fullbleed-editorial-cover": "Fullbleed dominant property photo with a champagne serif wordmark, location eyebrow and a small property index on the right edge. Cinematic, rarefied, private-viewing hero.",
}

NAVBAR_STYLES: dict[str, str] = {
    "solid-phone":     "Solid colored bar with prominent phone number CTA.",
    "pill-floating":   "Floating rounded pill navbar, transparent over hero.",
    "minimal-serif":   "Centered serif logo with thin underline rule.",
    "soft-pastel":     "Translucent bar, soft pastel link colors, no hard edges.",
    "serif-centered":  "Centered serif wordmark with hairline rule and small reservation link right.",
    "warm-bar":        "Cream sticky bar with handwritten brand on left and big phone CTA on right.",
    "bold-pill":       "Black pill nav floating top, bright accent ORDER button on the right.",
    "solid-corporate":     "Full-bleed solid navy bar with left-aligned links and phone number on the right.",
    "pill-floating-glow":  "Floating rounded pill nav with glowing primary CTA button and launch-date badge.",
    "index-rule":          "Hairline rule navbar — wordmark left + uppercase index-letters navigation + quiet status pill on the right.",
    "fullbleed-dark":      "Transparent dark navbar with small uppercase wordmark, minimal link row and a tiny quiet ghost CTA on the right.",
    "serif-index-asterisk": "Ink page hairline navbar with serif wordmark + asterisk glyph + uppercase alpha-index links and a ghost dossier CTA on the right.",
    "pill-sprint-chip":     "Floating dark violet pill navbar with geometric wordmark + glow primary CTA and a tiny mono sprint chip beside it.",
    "ledger-monogram":      "Ink sticky bar with gold monogram crest on the left, serif-capital links in the centre and a quiet forensic ledger meta (Iscr. Ordine Avvocati) on the right.",
    "pill-advisory":        "Floating pale pill nav with slate wordmark + blue-chip links and a confident primary 'Prenota strategy call' button on the right.",
    "cover-search":         "Transparent bar over a hero cover photo with wordmark + listing filters + ghost 'Area riservata' link on the right.",
    "cinematic-dark":       "Transparent dark navbar over fullbleed imagery with a champagne wordmark + restrained uppercase link row + 'Richiesta privata' ghost CTA.",
}

FOOTER_STYLES: dict[str, str] = {
    "corporate-4col":   "Four columns: brand / specialties / contact / legal.",
    "compact-2col":     "Brand + opening hours, single line copyright.",
    "centered-minimal": "Centered logo, single legal line.",
    "spa-social":       "Social row + newsletter + minimal links.",
    "concierge-press":  "Concierge tile + press logos band.",
    "hours-warm":       "Hours strip + WhatsApp + map (warm cream).",
    "delivery-strip":   "Delivery partner logos + counter status + order CTA.",
    "sectors-ribbon":    "KPI strip over navy band + industry-sectors ribbon with uppercase wordmarks.",
    "shiplog-countdown": "Live ship-log list + next-release countdown chip (startup changelog vibe).",
    "clients-ribbon":    "Hairline rule over a horizontal ribbon of editorial clients/publications + studio coordinates on the right.",
    "exif-credits":      "Film-style EXIF credit bar: camera body, lens, location, year — monospaced, tiny uppercase, split in 4 cells.",
    "colophon-press":    "Editorial colophon footer: three-column credit block (studio, recognition, coordinates) with press ribbon above and a small standfirst quote.",
    "shiplog-console":   "Live console-style footer with ship-log row, current sprint chip, stack logo marquee and a boot-line telemetry string at the bottom.",
    "ledger-institutional": "Studio legale footer: 4 columns (studio / pratiche / foro / note legali) over ink with gold hairlines and a small Ordine degli Avvocati iscrizione line.",
    "advisory-panel":       "Advisory-firm footer: 3 columns (studio / services / booking) over slate with a confident primary CTA block and transparent sector chips.",
    "hours-map":            "Agency footer with office hours column, map snippet, phone + whatsapp strip and neighborhood chips.",
    "concierge-coords":     "Luxury footer: champagne serif wordmark + editorial coordinates (sede, concierge, rassegna stampa) + private-viewing promise line.",
}

CARD_STYLES: dict[str, str] = {
    "icon-grid":       "4-up cards with icon, title, blurb, link arrow.",
    "portrait-stack":  "3-up portrait cards with name + role + bio.",
    "editorial-large": "2-up oversized cards with serif numeral + caption.",
    "pricelist":       "Two-column menu: name+desc left, dotted leader, price right.",
    "course-index":    "Numbered serif course list with name + paired wine + ingredient line.",
    "chalkboard-day":  "Daily-special chalkboard cards with handwritten dish name + price tag.",
    "product-grid":    "Square product cards with photo + price + Add button.",
    "pillar-advisory":    "3-up wide advisory pillar cards: serif numeral + title + blurb + hairline.",
    "feature-glow":       "Feature pills + glowing product mockup card with metric readout.",
    "indexed-case-study": "Numbered row entries in a case-study ledger: index · project name · category · year, with a hover rule between rows.",
    "filmstrip-series":   "Horizontal filmstrip of series stills with series counter badges and a hairline divider between frames.",
    "editorial-index-dossier":"Editorial oversized numbered case-study rows (01/ 02/) with serif project name + italic client + year + discipline tag, clickable into a dossier.",
    "sprint-console":         "Dark violet sprint card: mono sprint ID + capability chip + deliverable metric + accent glow CTA, product-telemetry feel.",
    "practice-area-ledger":   "Numbered practice-area rows in a serif ledger: index (01 — 02 —) + area name + short blurb + gold arrow, ink card with gold hairline top.",
    "advisory-sector-pill":   "Advisory sector card: confident blue title + short strategic blurb + metric chip (mandati attivi, anni esperienza) + ghost 'Scopri' link.",
    "property-tile-specs":    "Property listing card: cover photo + price chip + title + address + specs row (camere · m² · bagni) + 'Visita' button.",
    "property-dossier":       "Luxury property dossier card: large editorial photo + champagne serif title + 'Private viewing su richiesta' + provenance + rarity meta (unico · da 3 giorni).",
}

BUTTON_STYLES: dict[str, str] = {
    "rounded-solid":     "10px radius, solid accent fill.",
    "pill-soft":         "999px pill, soft pastel fill.",
    "ghost-underline":   "Transparent, accent text, animated underline.",
    "square-bold":       "0px radius, heavy border, primary fill.",
    "ghost-gold-serif":  "Underline serif text in gold accent — concierge style.",
    "rustic-rounded":    "Warm rounded button with red fill and slight tilt.",
    "block-bold":        "Heavy block button, bright accent fill, arrow icon, no radius.",
    "ghost-institutional": "Outline pill in dove cream over navy — institutional consulting tone.",
    "glow-pill":           "Solid glowing rounded pill with subtle drop-glow, startup/SaaS conversion button.",
    "ghost-sans-rule":     "Uppercase sans label with a thin rule underneath, no fill — quiet editorial CTA for designer portfolios.",
    "ghost-mono-bracket":  "Monospaced uppercase label wrapped in [ square brackets ] — cinematographer CTA, minimal and technical.",
    "ghost-serif-dossier": "Italic serif underline label with a small right-arrow — editorial agency CTA, invitational.",
    "glow-sprint-arrow":   "Solid violet glowing pill with arrow — digital-studio primary CTA, startup-energetic but premium.",
    "serif-gold-border":   "Serif italic label inside a gold hairline border — studio-legale forensic CTA.",
    "pill-advisory-blue":  "Rounded confident blue pill with arrow — modern lawyer / advisory CTA.",
    "block-visit-primary": "Square bold navy button with 'Visita' / 'Cerca' label + chevron — agency real-estate search / visit CTA.",
    "ghost-champagne":     "Thin champagne hairline border with uppercase serif label — luxury editorial CTA.",
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
    "advisory-sober": "Istituzionale, cauto, board-room, evidence-led.",
    "growth-tech":    "Diretto, energico, product-led, orientato alla conversione.",
    "editorial-designer":   "Tipografico, sistemico, di studio — voce da direttore artistico, first-person plural, progettuale.",
    "cinematic-authorial":  "Autoriale, silenziosa, cinematografica — voce da autore di immagini, tempi lenti, ossessione per la luce.",
    "editorial-agency":     "Curatoriale, strategica, di brand — voce da art director / direttore creativo, first-person plural, manifesti e principi.",
    "digital-sprint":       "Digitale, diretta, di delivery — voce da product partner / head of digital, imperative leggero, sprint e metrica.",
    "forensic-notarile":    "Autorevole, sobria, forense — voce da studio legale di tradizione, terza persona plurale, riserbo e rigore, citazione dei codici.",
    "advisory-modern":      "Moderna, diretta, strategica — voce da partner advisory, prima persona plurale, orientata alla soluzione, chiara sui tempi.",
    "market-approachable":  "Concreta, pratica, accessibile — voce da agente immobiliare di fiducia, seconda persona singolare, orientata alla visita.",
    "editorial-concierge":  "Rarefatta, cinematografica, privata — voce da private client advisor / property concierge, riserbo, dossier, visita su appuntamento.",
}

CONVERSION_PATTERNS: dict[str, str] = {
    "booking-widget":         "Embedded date/time/specialty selector in hero.",
    "phone-and-chat":         "Prominent phone CTA + WhatsApp/chat pill.",
    "private-request":        "Underline link 'Richiedi visita privata' + email.",
    "calendar-spot":           "Inline mini-calendar with bookable spots.",
    "concierge-reservation":  "Concierge tile + email + 'Riserva la serata' link, no public form.",
    "phone-and-whatsapp":     "Giant phone number + WhatsApp pill, family-style.",
    "order-now-delivery":     "ORDINA ORA primary CTA + delivery partners strip + counter status.",
    "private-call":           "Ghost CTA 'Fissa una call privata' + direct phone + senior-partner meta row.",
    "free-trial-glow":        "Glowing primary 'Inizia gratis' CTA + secondary 'Guarda la demo' + pricing teaser card.",
    "case-study-request":     "Ghost 'Richiedi il portfolio completo' CTA + studio email + open-commission status strip.",
    "series-brief":           "Ghost 'Apri la serie completa' CTA + quiet 'Disponibile per commissioni' status pulse.",
    "dossier-request":        "Ghost serif 'Richiedi il dossier' CTA + single editorial contact email + slow reply-time promise.",
    "discovery-call":         "Glowing pill 'Prenota la call di discovery' CTA + next-sprint chip + 3-step brief intake.",
    "private-consultation":   "Ghost serif 'Richiedi una consulenza riservata' CTA + direct email to managing partner + discrete phone line. No public calendar.",
    "strategy-call":          "Confident blue pill 'Prenota una strategy call' CTA + online calendar link + 3-step intake card.",
    "viewing-request":        "Square 'Richiedi una visita' CTA + property reference field + agent phone + WhatsApp pill.",
    "private-viewing":        "Ghost champagne 'Richiedi una private viewing' CTA + dedicated concierge line + dossier download (solo su appuntamento).",
}

IMAGERY_DIRECTIONS: dict[str, str] = {
    "institutional-clinic": "Bright clinic interiors, doctors in coats, equipment.",
    "family-warmth":        "Pediatricians with kids, families, soft daylight.",
    "editorial-portrait":   "Single specialist portrait, low-key, magazine cover energy.",
    "spa-nature":           "Stone, water, plants, candles, slow tactile imagery.",
    "moody-plated":         "Dark plated dishes, low-key tungsten light, fine-dining mood.",
    "rustic-trattoria":     "Warm wood tables, hands kneading dough, terra-cotta tones.",
    "street-pop-product":   "Bold burger / pizza / fritti cutouts, daylight high-contrast.",
    "executive-boardroom":  "Boardroom meetings, corporate HQ interiors, executive portraits, industrial facilities.",
    "product-dashboard":    "Laptop screens with dashboards, product UIs, code editors, open-plan tech offices.",
    "design-workspace":     "Designer desk, sketchbooks, paper prototypes, studio work-in-progress — artifacts over portraits.",
    "cinematic-photostill":  "Moody, low-key photographic stills — reportage, still life, portrait — as if framed from a film.",
    "editorial-agency-craft":"Studio print/type close-ups, brand books on desks, art-direction contact sheets, gallery install shots — no team-lineup stock.",
    "digital-product-console":"Product UI close-ups, screen-in-screen reviews, dark IDE, sprint board detail, modern studio with monitors — momentum energy.",
    "legal-heritage-ink":   "Studio legale interiors — leather-bound codici, studio-library bookshelves, senior partner portraits at desk, gavel/justice scale accents. Ink-dark, serious, heritage-led.",
    "advisory-modern-light":"Modern advisory practice — bright consulting offices, collaborative meeting rooms, laptops with case-law databases, diverse professional portraits. Daylight, confident, solution-led.",
    "mass-market-listings": "Approachable property imagery — bright urban apartments, family homes with garden, agent with clients on viewing, keys handover. Daylight, lived-in, attainable.",
    "luxury-property-editorial":"Cinematic property photography — infinity-pool villas, editorial interior spreads, architectural details at golden hour, yacht-view terraces, heritage libraries. Dusk, champagne light, aspirational.",
}


# ---------------------------------------------------------------------------
# Per-template DNA registry
# ---------------------------------------------------------------------------

TEMPLATE_DNA: dict[str, dict[str, Any]] = {

    # ─────────────────────────────────────────────────────────────
    # Agency live rollout (Phase 2g3.6f) — 2 distinct archetypes
    # (agency-creative-studio · agency-digital-studio)
    #
    # Session 49 closes the Phase 2g2x.1 agency identity-crash by
    # splitting Vertex + Aura onto distinct DNAs. Vertex goes
    # editorial-studio (concept-led, brand/identity/curation). Aura
    # goes product-studio (delivery-led, digital/product/growth). They
    # never collapse into recolors of each other — the hero silhouette,
    # typography axis, case-study treatment, process section, CTA
    # language and imagery pool are all distinct.
    # ─────────────────────────────────────────────────────────────

    # ── A1) CREATIVE-STUDIO — Vertex, brand/identity editorial ───
    "vertex-creative-agency": {
        "archetype":          "agency-creative-studio",
        "hero_style":         "editorial-quote-cover",
        "navbar_style":       "serif-index-asterisk",
        "footer_style":       "colophon-press",
        "section_order":      ["serif-nav", "quote-hero", "selected-work", "capacita", "press-ribbon", "manifesto", "colophon"],
        "card_style":         "editorial-index-dossier",
        "button_style":       "ghost-serif-dossier",
        "density":            "very-airy",
        "tone":               "editorial-agency",
        "imagery_direction":  "editorial-agency-craft",
        "imagery_key":        "agency-creative",
        "conversion_pattern": "dossier-request",
        "font_pairing":       ("Space Grotesk", "Inter"),
        "content": {
            # Core hero copy — mirrors the live VERTEX_CONTENT_IT so the
            # static preview foreshadows the live page rather than showing
            # generic chrome. Session 50 expansion from 2 keys to full set.
            "eyebrow":       "Studio indipendente · fondato nel 2018 · Milano",
            "headline":      'Brand che <em>pesano</em>, <em>tengono</em>, <em>durano</em>.',
            "subhead":       "Uno studio indipendente che disegna sistemi di identità, collane editoriali e direzioni artistiche per un numero ristretto di clienti culturali e di lusso.",
            "primary_cta":   "Richiedi il dossier",
            "secondary_cta": "Lavori selezionati",
            "nav_links":     ["Studio", "Lavori", "Capacità", "Manifesto", "Contatti"],
            "availability":  "Nuove commesse · autunno 2026",
            "status_label":  "Disponibilità",
            "status_value":  "Autunno 2026",

            # Right-hand editorial cover tile (Case Study · 01)
            "cover_label":   "Case Study · 01",
            "cover_client":  "FONDAZIONE PRADA · Collana 2025",
            "cover_title":   "Un sistema editoriale per <em>quattro autori</em>.",
            "cover_discipline": "Identità · editoria",
            "cover_year":    "2025 — 2026",

            # Ledger of selected work (4 rows shown in preview)
            "ledger_label":   "Lavori recenti",
            "ledger_heading": "Archivio <em>selezionato</em> · 2023 — 2026",
            "ledger_link":    "Archivio completo →",
            "projects": [
                ("01", "Collana Narrativa Italiana",  "Adelphi Edizioni",     "Identità · editoria", "2025"),
                ("02", "Rebranding della Fondazione", "Fondazione Prada",      "Direzione artistica", "2025"),
                ("03", "Manuale di marca integrato",   "Maison Gentiluomo",    "Branding di lusso",   "2024"),
                ("04", "Segnaletica & wayfinding",     "Triennale Milano",     "Identità spaziale",   "2024"),
            ],

            # Press ribbon — cultural / design-trade publications
            "press_label":        "Pubblicato su",
            "press_publications": ["MONOCLE", "DOMUS", "WALLPAPER*", "CREATIVE REVIEW", "EYE MAGAZINE", "IT'S NICE THAT"],

            # Colophon strip (bottom)
            "colophon_label":      "Lo studio",
            "colophon_rows": [
                ("Sede",         "Via Tortona · Milano"),
                ("Fondato",      "2018 · otto anni"),
                ("Riconoscimenti","ADI · TDC · Compasso d'Oro"),
            ],
        },
    },

    # ── A2) DIGITAL-STUDIO — Aura, digital/product/growth ────────
    "aura-digital-studio": {
        "archetype":          "agency-digital-studio",
        "hero_style":         "product-console-hero",
        "navbar_style":       "pill-sprint-chip",
        "footer_style":       "shiplog-console",
        "section_order":      ["pill-nav", "console-hero", "capabilities-grid", "sprints", "lavori-cards", "metric-strip", "shiplog"],
        "card_style":         "sprint-console",
        "button_style":       "glow-sprint-arrow",
        "density":            "medium",
        "tone":               "digital-sprint",
        "imagery_direction":  "digital-product-console",
        "imagery_key":        "agency-digital",
        "conversion_pattern": "discovery-call",
        "font_pairing":       ("Plus Jakarta Sans", "Inter"),
        "content": {
            # Core hero copy — mirrors the live AURA_CONTENT_IT so the
            # static preview foreshadows the live page. Session 50
            # expansion from 2 keys to full set.
            "eyebrow":        "Digital · product · growth studio",
            "headline":       'Dalla <em>call di discovery</em> al <em>primo KPI</em> in sei settimane.',
            "subhead":        "Costruiamo prodotti e sistemi di crescita per scale-up italiane ed europee. Sprint di due settimane, dashboard condiviso, consegne misurabili.",
            "primary_cta":    "Prenota una call",
            "secondary_cta":  "Lavori recenti",
            "nav_links":      ["Studio", "Capabilities", "Lavori", "Sprint", "Brief"],
            "sprint_chip":    "Sprint 07/Q2 · live",

            # Product console tile (top-right, dark IDE look)
            "console_path":          "aura.studio/clients/casavo/live",
            "console_status":        "LIVE · sprint 07/Q2",
            "console_primary_metric":"+34%",
            "console_primary_label": "Conversione post-rework · 30 gg",
            "console_kpis": [
                ("+18%",    "Retention D30"),
                ("Δ 22",    "NPS pre / post"),
                ("€ 840K",  "MRR sprint 1-14"),
                ("99.98%",  "Uptime Q2"),
            ],

            # Capabilities mini — 4 sprint-card tiles
            "capab_label":   "Capabilities",
            "capab_heading": "Quattro <em>aree</em>, un solo team.",
            "capabilities": [
                ("C.01", "Product launch",      "Dal concept all'onboarding live."),
                ("C.02", "Platform redesign",   "Ripensare prodotti maturi senza perdere utenti."),
                ("C.03", "Growth systems",      "Onboarding, retention, referral, pricing."),
                ("C.04", "B2B delivery",        "Portali asset manager, dashboard corporate."),
            ],

            # Ship log footer strip (last 4 deploys)
            "shiplog_label":  "// ship log · last 4",
            "shiplog_rows": [
                ("ieri · 18:04",  "v2.14", "Soldo — onboarding corporate"),
                ("ieri · 09:21",  "v2.13", "Fastweb Plus — dashboard v2.3"),
                ("lun · 15:30",   "v2.12", "Lendlease — portale asset manager"),
                ("ven · 11:12",   "v2.11", "Casavo — retention A/B loop 003"),
            ],
            "shiplog_meta": "aura.studio · uptime 99.98 · last deploy 4 min ago",
        },
    },

    # ─────────────────────────────────────────────────────────────
    # Lawyer live rollout (Phase 2g3.7) — 2 distinct archetypes
    # (classic-gold · modern-transparent)
    #
    # Session 53 closes the Phase 2g2x.1 lawyer identity-crash by
    # splitting Lex + Juris onto distinct DNAs. Lex goes classic-gold
    # (serif institutional, gold + ink, forensic ledger). Juris goes
    # modern-transparent (advisory manifesto, confident blue, strategic
    # sprint). They never collapse into recolors — hero, navbar, card,
    # conversion pattern, tone and imagery direction are all distinct.
    # ─────────────────────────────────────────────────────────────

    # ── L1) CLASSIC-GOLD — Lex, studio legale istituzionale ──────
    "lex-studio-legale": {
        "archetype":          "classic-gold",
        "hero_style":         "split-ledger-monogram",
        "navbar_style":       "ledger-monogram",
        "footer_style":       "ledger-institutional",
        "section_order":      ["ink-nav", "ledger-hero", "practice-areas-ledger", "partners-portrait", "publications", "contact-ledger"],
        "card_style":         "practice-area-ledger",
        "button_style":       "serif-gold-border",
        "density":            "airy",
        "tone":               "forensic-notarile",
        "imagery_direction":  "legal-heritage-ink",
        "imagery_key":        "lawyer-classic",
        "conversion_pattern": "private-consultation",
        "font_pairing":       ("Cormorant Garamond", "Inter"),
        "content": {
            "eyebrow":       "Studio Legale Ferri · Roma · Milano · dal 1962",
            "headline":      'Competenza, <em>riservatezza</em>, risultati.',
            "subhead":       "Assistiamo imprese, famiglie e professionisti con un approccio rigoroso, personalizzato e discreto. Oltre sessant'anni di esperienza al servizio della giustizia.",
            "primary_cta":   "Richiedi una consulenza riservata",
            "secondary_cta": "Aree di pratica",
            "phone":         "+39 06 4567 2300",
            "monogram":      "LF",
            "nav_links":     ["Lo Studio", "Aree di pratica", "Avvocati", "Pubblicazioni", "Contatti"],
            "meta_strip": [
                ("Sede principale",   "Roma · via Piemonte"),
                ("Soci fondatori",    "1962 · famiglia Ferri"),
                ("Avvocati abilitati","14 · foro di Roma"),
            ],
            "hero_credit_left":  ("Direzione",       "Avv. Prof. A. Ferri"),
            "hero_credit_right": ("Foro",             "Roma · Milano"),
            "practice_label":    "Aree di pratica",
            "practice_heading":  "Dodici competenze, una sola <em>firma.</em>",
            "practice": [
                ("01", "Diritto societario",         "M&A, governance, contrattualistica commerciale e operazioni straordinarie."),
                ("02", "Diritto di famiglia",         "Separazioni, divorzi, successioni e tutela dei minori."),
                ("03", "Diritto del lavoro",          "Contenzioso, contrattazione collettiva, sicurezza sul lavoro."),
                ("04", "Diritto penale d'impresa",    "Reati societari, responsabilità 231, white collar crimes."),
            ],
            "stats_label": "Sessantadue anni di foro",
            "stats": [
                ("62",     "anni di attività"),
                ("14",     "avvocati abilitati"),
                ("2.400+", "cause patrocinate"),
                ("96%",    "esito favorevole"),
            ],
            "publications": ["FORO ITALIANO", "DIRITTO E GIUSTIZIA", "IL SOLE 24 ORE · LEGALE", "GUIDA AL DIRITTO", "CASSAZIONE PENALE"],
        },
    },

    # ── L2) MODERN-TRANSPARENT — Juris, avvocato moderno advisory
    "juris-avvocato-moderno": {
        "archetype":          "modern-transparent",
        "hero_style":         "centered-advisory-manifesto",
        "navbar_style":       "pill-advisory",
        "footer_style":       "advisory-panel",
        "section_order":      ["pill-nav", "manifesto-hero", "sector-grid", "process-sprint", "outcome-metrics", "insights-strip", "cta"],
        "card_style":         "advisory-sector-pill",
        "button_style":       "pill-advisory-blue",
        "density":            "medium",
        "tone":               "advisory-modern",
        "imagery_direction":  "advisory-modern-light",
        "imagery_key":        "lawyer-modern",
        "conversion_pattern": "strategy-call",
        "font_pairing":       ("DM Sans", "Inter"),
        "content": {
            "eyebrow":       "Martini & Partners · Milano · Torino · Bologna",
            "headline":      'Il diritto, <em>dalla tua parte.</em>',
            "subhead":       "Affianchiamo startup, PMI e professionisti nelle decisioni legali che contano — con tempi chiari, tariffe trasparenti e un dashboard condiviso dove segui l'avanzamento del tuo caso.",
            "primary_cta":   "Prenota una strategy call",
            "secondary_cta": "Come lavoriamo",
            "phone":         "hello@martinipartners.legal",
            "nav_links":     ["Approccio", "Servizi", "Settori", "Insights", "Contatti"],
            "sector_label":  "Settori",
            "sector_heading":"Sei aree, un solo <em>metodo</em>.",
            "sectors": [
                ("01", "Startup & Tech",        "Fundraising, cap table, IP, compliance GDPR e AI Act per aziende digitali."),
                ("02", "PMI & Famiglia",         "Passaggio generazionale, governance, patti parasociali e M&A mid-market."),
                ("03", "Lavoro & HR",            "Contratti, licenziamenti, welfare, stock option e remote-work internazionale."),
                ("04", "Contrattualistica B2B",  "SaaS, licensing, partnership, vendor due-diligence e MSA in inglese."),
                ("05", "Dispute resolution",     "Mediazione, arbitrato, ADR e contenzioso strategico."),
                ("06", "Privacy & AI",           "GDPR, AI Act, data mapping, DPIA e policy per aziende data-driven."),
            ],
            "process_label":"Come lavoriamo",
            "process_heading":"Dal brief al <em>primo atto</em> in due settimane.",
            "process": [
                ("S.01", "Discovery call",  "30 min via video · capiamo il problema, non vendiamo il servizio."),
                ("S.02", "Offerta chiara",  "Tempi, fasi, costo fisso o a consumo — tutto scritto, zero sorprese."),
                ("S.03", "Dashboard live",  "Segui in tempo reale atti, scadenze, documenti e ore lavorate."),
            ],
            "metric_heading": "I numeri dello studio",
            "metric_strip": [
                ("180+", "aziende assistite"),
                ("14 gg","tempo medio primo atto"),
                ("4.9★", "soddisfazione clienti"),
                ("€ 0",  "setup fee, sempre"),
            ],
            "sprint_chip":    "Strategy call · prossimo slot 17 aprile",
            "insights_label": "Insights · ultima settimana",
            "insights": [
                ("17 apr", "AI Act · cosa cambia per le PMI italiane"),
                ("14 apr", "Stock option 2026 · nuova disciplina fiscale"),
                ("11 apr", "Smart-working oltre confine · tre scenari"),
            ],
        },
    },

    # ─────────────────────────────────────────────────────────────
    # Real Estate live rollout (Phase 2g3.7) — 2 distinct archetypes
    # (mass-market · ultra-luxury-cinematic)
    #
    # Session 53 closes the Phase 2g2x.1 real-estate identity-crash.
    # Casa goes mass-market (daylight, search-widget, tile grid, orange
    # accent, accessible). Villa goes ultra-luxury-cinematic (fullbleed
    # editorial cover, champagne + black, rarefied, private viewing).
    # They never collapse into recolors of each other.
    # ─────────────────────────────────────────────────────────────

    # ── RE1) MASS-MARKET — Casa, agenzia immobiliare accessibile ──
    "casa-agenzia-immobiliare": {
        "archetype":          "mass-market",
        "hero_style":         "search-listings-grid",
        "navbar_style":       "cover-search",
        "footer_style":       "hours-map",
        "section_order":      ["nav", "search-hero", "featured-listings", "neighborhoods", "agents", "valuation-cta"],
        "card_style":         "property-tile-specs",
        "button_style":       "block-visit-primary",
        "density":            "medium",
        "tone":               "market-approachable",
        "imagery_direction":  "mass-market-listings",
        "imagery_key":        "realestate-casa",
        "conversion_pattern": "viewing-request",
        "font_pairing":       ("Poppins", "Inter"),
        "content": {
            "eyebrow":       "Domus Immobiliare · Milano · Torino · Lombardia & Piemonte",
            "headline":      'La casa dei tuoi <em>sogni</em>, vicino a te.',
            "subhead":       "Oltre 600 immobili selezionati a mano. Visite private, valutazione gratuita, tempi chiari dalla prima visita al rogito — e un solo agente dedicato a te.",
            "primary_cta":   "Cerca un immobile",
            "secondary_cta": "Valutazione gratuita",
            "phone":         "+39 02 8765 4321",
            "nav_links":     ["Vendita", "Affitto", "Quartieri", "Agenti", "Valutazione"],
            "search_widget": {
                "label":      "Cosa cerchi?",
                "location":   "Milano, Centro",
                "type":       "Appartamento",
                "price":      "€ 500K — € 1.2M",
                "rooms":      "3+ camere",
                "cta":        "Cerca immobile",
            },
            "listings_label":  "In evidenza questa settimana",
            "listings_link":   "Vedi tutti i 600+ immobili  →",
            "listings": [
                ("€ 1.250.000", "Attico panoramico con terrazzo",   "Milano · Brera",        "4", "180", "2", "Esclusiva"),
                ("€ 890.000",   "Villa moderna con giardino",        "Como · Cernobbio",      "5", "240", "3", "Nuova"),
                ("€ 650.000",   "Loft di design in zona Tortona",    "Milano · Navigli",      "2", "120", "2", "Rinnovato"),
                ("€ 420.000",   "Trilocale luminoso con balcone",    "Torino · Crocetta",     "3",  "95", "1", "Disponibile"),
            ],
            "neighborhoods_label":  "Quartieri",
            "neighborhoods_heading":"Dove <em>troviamo casa</em>.",
            "neighborhoods": [
                ("Brera",      "Milano · storico",    "124 immobili",  "da € 850K"),
                ("Navigli",    "Milano · design",     "89 immobili",   "da € 520K"),
                ("Cernobbio",  "Como · lago",         "42 immobili",   "da € 680K"),
                ("Crocetta",   "Torino · residenziale","67 immobili",  "da € 380K"),
            ],
            "stats_label":   "Venti anni sul mercato",
            "stats": [
                ("600+",   "immobili in portafoglio"),
                ("2.800+", "case trovate dal 2005"),
                ("20",     "anni di esperienza"),
                ("4.8 ★",  "su 420 recensioni Google"),
            ],
            "agents_label":   "I nostri agenti",
            "agents": [
                ("Giulia Ferrante",  "Milano · Brera & Centro", "15 anni"),
                ("Marco Lentini",    "Milano · Navigli & Sud",   "12 anni"),
                ("Silvia Mondelli",  "Torino · Crocetta",        "10 anni"),
                ("Andrea Colombo",   "Como · lago",              "18 anni"),
            ],
            "valuation_label":   "Valutazione gratuita",
            "valuation_heading": "Quanto vale <em>casa tua</em>?",
            "valuation_intro":   "Ti richiamiamo entro 24 ore con una stima onesta e il piano per metterla sul mercato.",
        },
    },

    # ── RE2) ULTRA-LUXURY-CINEMATIC — Villa, immobili di lusso ────
    "villa-immobili-lusso": {
        "archetype":          "ultra-luxury-cinematic",
        "hero_style":         "fullbleed-editorial-cover",
        "navbar_style":       "cinematic-dark",
        "footer_style":       "concierge-coords",
        "section_order":      ["dark-nav", "fullbleed-hero", "signature-properties", "territory-ribbon", "private-advisor", "private-viewing-cta"],
        "card_style":         "property-dossier",
        "button_style":       "ghost-champagne",
        "density":            "very-airy",
        "tone":               "editorial-concierge",
        "imagery_direction":  "luxury-property-editorial",
        "imagery_key":        "realestate-villa",
        "conversion_pattern": "private-viewing",
        "font_pairing":       ("Cormorant Garamond", "Montserrat"),
        "content": {
            "eyebrow":       "Villa Prestige · Private Advisory · Italia & Costa Azzurra",
            "headline":      "Dimore <em>d'autore</em>, a chi sa riconoscerle.",
            "subhead":       "Un portafoglio ristretto di residenze private, storiche e contemporanee, proposto solo su appuntamento. Visite riservate, dossier editoriale dedicato, trattativa discreta.",
            "primary_cta":   "Richiedi una private viewing",
            "secondary_cta": "Collezione in corso",
            "phone":         "concierge@villaprestige.it",
            "nav_links":     ["Lo studio", "Collezione", "Territorio", "Esperienza", "Concierge"],
            "hero_wordmark": "Villa Prestige",
            "hero_location": "Portofino · Collezione primavera 2026",
            "hero_counter_label": "Dimora in vetrina",
            "hero_counter_value": "N° 03 / 18",
            "series_label":   "In vetrina",
            "series_title":   "«Villa Aurelia» · Portofino",
            "series_note":    "Dimora storica del 1922 con parco di tre ettari a picco sul golfo. Quattrocento metri quadri, biblioteca d'autore, infinity pool affacciata sull'Isola Palmaria.",
            "hero_credit_cells": [
                ("Collezione",  "N° 03 / 18"),
                ("Territorio",  "Portofino · Liguria"),
                ("Superficie",  "400 m² · parco 30.000 m²"),
                ("Accesso",     "Solo su appuntamento"),
            ],
            "signature_label":   "Collezione primavera",
            "signature_heading": "Dimore <em>selezionate</em> per questa stagione.",
            "signature_intro":   "Ogni proprietà è proposta solo dopo una valutazione su due livelli — autorialità architettonica e coerenza del territorio. La lista completa è disponibile su richiesta, in formato dossier editoriale.",
            "signature": [
                # (index, title, territory, surface, provenance, availability)
                ("01", "Villa Aurelia",           "Portofino · Liguria",        "400 m² · parco 30.000 m²", "Anni '20 · firma Piacentini",    "Da 3 giorni"),
                ("02", "Castello di Monterò",      "Chianti · Toscana",          "1.200 m² · 18 ettari",      "XII secolo · restauro 2014",    "Esclusiva"),
                ("03", "Penthouse Quadronno",      "Milano · Magenta",           "380 m² · terrazza 180 m²",  "Attico unico · vista Duomo",    "Su appuntamento"),
                ("04", "Mas de la Mer",            "Saint-Tropez · Costa Azzurra","550 m² · vigna privata",    "XVIII secolo · certificato",    "Nuova"),
            ],
            "territory_label":  "Territori di riferimento",
            "territory":        ["PORTOFINO", "CHIANTI", "COSTA SMERALDA", "LAGO DI COMO", "SAINT-TROPEZ", "CAPRI", "VAL D'ORCIA"],
            "advisor_label":    "Private advisor",
            "advisor_heading":  "Un solo <em>referente</em>, dal primo dossier al rogito.",
            "advisor_name":     "Alessandra Visconti di Modrone",
            "advisor_role":     "Private client director · dal 2011",
            "advisor_bio":      "Quindici anni tra Savills, Knight Frank e Sotheby's International Realty. Ogni cliente privato è seguito da me personalmente, dal primo incontro di riservatezza alla firma notarile.",
            "press":            ["FINANCIAL TIMES · HOW TO SPEND IT", "MONOCLE", "ROBB REPORT", "CORRIERE LIVING", "AD ITALIA"],
        },
    },

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
            "headline":      'La tua salute, il nostro <em>lavoro quotidiano</em>',
            "subhead":       "Oltre 40 specialisti, percorsi diagnostici integrati e un'esperienza paziente pensata per metterti a tuo agio dal primo contatto.",
            "primary_cta":   "Prenota una visita",
            "secondary_cta": "Tutti i servizi",
            "phone":         "Numero verde 800 123 456",
            "services_title": "I nostri reparti specialistici",
            "services_link_all": "Vedi tutti i 40+ servizi  →",
            "card_cta": "Prenota →",
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
            "pricelist_title": "Listino rituali",
            "pricelist_sub_prefix": "Aggiornato al",
            "therapists_label": "Operatori  ·  iscritti albo",
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
            "hero_ribbon":     "Convenzionato SSN",
            "hero_pebble_name": "Dr.ssa Rambaldi",
            "hero_pebble_note": "oggi disponibile",
            "hours_label":     "Orari di apertura",
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

    # ─────────────────────────────────────────────────────────────
    # Ecommerce pilot — 2 distinct archetypes
    # (fashion-editorial · artisan-workshop)
    # ─────────────────────────────────────────────────────────────

    # ── E1) FASHION-EDITORIAL — dark Maison magazine cover ──────
    "luxe-fashion-store": {
        "archetype":          "fashion-editorial",
        "hero_style":         "editorial-serif",
        "navbar_style":       "minimal-serif",
        "footer_style":       "centered-minimal",
        "section_order":      ["nav", "editorial-cover", "edition-strip"],
        "card_style":         "editorial-large",
        "button_style":       "ghost-gold-serif",
        "density":            "very-airy",
        "tone":               "prestigious",
        "imagery_direction":  "editorial-portrait",
        "imagery_key":        "ecommerce",
        "conversion_pattern": "private-request",
        "font_pairing":       ("Cormorant Garamond", "Montserrat"),
        "content": {
            "eyebrow":    "Lookbook · Primavera Estate 2026",
            "headline":   "Il nuovo corpo del vestire.",
        },
    },

    # ── E2) ARTISAN-WORKSHOP — warm cream bottega catalogue ─────
    "bottega-shop-artigianale": {
        "archetype":          "artisan-workshop",
        "hero_style":         "warm-photo-frame",
        "navbar_style":       "warm-bar",
        "footer_style":       "hours-warm",
        "section_order":      ["warm-nav", "typographic-hero", "stamp-panel", "labeled-cards"],
        "card_style":         "chalkboard-day",
        "button_style":       "rustic-rounded",
        "density":            "medium",
        "tone":               "familiar-warm",
        "imagery_direction":  "rustic-trattoria",
        # Same pool as Luxe — differentiation is driven by macro tone + layout,
        # not imagery (Session 10 lesson: page-level color trumps hero details).
        "imagery_key":        "ecommerce",
        "conversion_pattern": "phone-and-whatsapp",
        "font_pairing":       ("Libre Baskerville", "Nunito Sans"),
        "content": {
            "eyebrow":    "Catalogo autunno · edizione 47",
            "headline":   "Pezzi unici fatti in bottega.",
        },
    },

    # ─────────────────────────────────────────────────────────────
    # Business hardening wave (Phase 2g2x) — 2 distinct archetypes
    # (corporate-suite · startup-saas-landing)
    # ─────────────────────────────────────────────────────────────

    # ── B1) CORPORATE-SUITE — Pragma, board advisory ─────────────
    "pragma-corporate-suite": {
        "archetype":          "corporate-suite",
        "hero_style":         "split-executive",
        "navbar_style":       "solid-corporate",
        "footer_style":       "sectors-ribbon",
        "section_order":      ["nav", "editorial-hero", "advisory-pillars", "kpi-strip", "sectors-ribbon"],
        "card_style":         "pillar-advisory",
        "button_style":       "ghost-institutional",
        "density":            "airy",
        "tone":               "advisory-sober",
        "imagery_direction":  "executive-boardroom",
        "imagery_key":        "business-corporate",
        "conversion_pattern": "private-call",
        "font_pairing":       ("Merriweather", "Inter"),
        "content": {
            "eyebrow":       "Advisory corporate · Milano · Francoforte · Zurigo",
            "headline":      'Dove si prendono le decisioni <em>che contano.</em>',
            "subhead":       "Affianchiamo direzioni generali e board di PMI consolidate nelle scelte strutturali — crescita organica, M&A, governance e trasformazione dei processi.",
            "primary_cta":   "Fissa una call privata",
            "secondary_cta": "Scarica la presentazione",
            "phone":         "+39 02 3611 9900",
            "nav_links":     ["Chi siamo", "Competenze", "Settori", "Board advisory", "Contatti"],
            "meta_strip": [
                ("Headquarters",  "Milano · Porta Nuova"),
                ("Equipe senior", "14 partner"),
                ("Mandati attivi", "42 progetti"),
            ],
            "hero_credit_left":  ("Direzione",       "Dott. F. Seregni"),
            "hero_credit_right": ("Anno fondazione", "2004"),
            "pillars_heading": "Tre competenze, una sola firma",
            "pillars_label":   "Practice",
            "pillars": [
                ("01", "Board advisory",    "Affianchiamo CdA e direzioni generali nelle decisioni di cambio di passo — piani industriali, assetti proprietari, successioni d'impresa."),
                ("02", "Crescita & M&A",    "Due diligence, valutazione, negoziazione e integrazione post-deal in 10 – 12 settimane, con team dedicati per settore."),
                ("03", "Governance & ESG",  "Compliance CSRD, reporting integrato, modelli 231, struttura dei comitati e policy di sostenibilità."),
            ],
            "kpi_heading": "Venti anni di mandati riservati",
            "kpi_strip": [
                ("22",      "anni di attività"),
                ("180+",    "mandati chiusi"),
                ("€ 1.4 B", "valore transato"),
                ("94%",     "ripetizione incarico"),
            ],
            "sectors_label": "Settori di intervento",
            "sectors": ["Industria & manifattura", "Servizi finanziari", "Energia & utilities", "Retail & consumer", "Healthcare & pharma"],
        },
    },

    # ── B2) STARTUP-SAAS-LANDING — Elevate, conversion-first ─────
    "elevate-startup-landing": {
        "archetype":          "startup-saas-landing",
        "hero_style":         "centered-manifesto-product",
        "navbar_style":       "pill-floating-glow",
        "footer_style":       "shiplog-countdown",
        "section_order":      ["launch-banner", "pill-nav", "manifesto-hero", "product-mockup", "metric-strip", "pricing-card", "ship-log"],
        "card_style":         "feature-glow",
        "button_style":       "glow-pill",
        "density":            "medium",
        "tone":               "growth-tech",
        "imagery_direction":  "product-dashboard",
        "imagery_key":        "business-startup",
        "conversion_pattern": "free-trial-glow",
        "font_pairing":       ("Manrope", "Inter"),
        "content": {
            "launch_banner":  "Serie A · Q2 2026 · Chiudiamo i primi 50 posti",
            "eyebrow":        "Landing conversion-first · GTM kit per SaaS & Startup",
            "headline":       'Dalla <em>waitlist</em> al primo <em>MRR</em> in quattordici giorni.',
            "subhead":        "Il kit di landing che trasforma i primi visitatori in utenti paganti — A/B test integrato, pricing table live, checkout Stripe out-of-the-box.",
            "primary_cta":    "Inizia gratis",
            "secondary_cta":  "Guarda la demo · 2 min",
            "phone":          "hello@elevatekit.io",
            "nav_links":      ["Prodotto", "Funzioni", "Prezzi", "Changelog", "Docs"],
            "feature_pills":  ["Stripe + Linear", "A/B test integrato", "Edge analytics", "Copy kit italiano"],
            "product_mockup": {
                "chrome_label":     "elevate.app / onboarding",
                "chrome_dots":      ["●", "●", "●"],
                "metric_primary":   "↑ 38%",
                "metric_label":     "conversione CTA primaria",
                "secondary_metric": "+ € 12.4K",
                "secondary_label":  "MRR ultimi 30 giorni",
                "badge":            "Live A/B",
            },
            "social_proof_label": "Adottato da 240 startup italiane",
            "social_proof_row":   ["FLUX", "NOVA/", "QUANTA", "HELIX", "RIFT.", "CASP"],
            "metric_heading": "I numeri del kit in produzione",
            "metric_strip": [
                ("3.1 ×",  "conversione landing media"),
                ("14 gg",  "dal deploy al primo utente pagante"),
                ("99.98%", "uptime infrastruttura"),
            ],
            "pricing_card": {
                "label":   "Prezzi trasparenti",
                "plan":    "Plan Launch",
                "price":   "€ 29",
                "period":  "/ mese",
                "note":    "Annullamento a un click · zero setup fee",
                "cta":     "Attiva il trial di 14 giorni",
                "perks":   ["Hosting incluso", "CLI deploy", "Supporto prioritario"],
            },
            "ship_log_label": "Ship log live",
            "ship_log_items": [
                ("Ieri",    "v2.8 · Nuova libreria hero & blocchi testimonial"),
                ("Martedì", "v2.7 · A/B test integrato con GrowthBook"),
                ("Lunedì",  "v2.6 · Stripe Checkout one-click"),
            ],
            "next_drop_label": "Prossima release",
            "next_drop_value": "v2.9 · venerdì 18",
        },
    },

    # ─────────────────────────────────────────────────────────────
    # Portfolio hardening wave (Phase 2g2x) — 2 distinct archetypes
    # (editorial-designer-grid · cinematic-photographer)
    #
    # Session 16 audit flagged portfolio as CRITICO: both templates
    # rendered through the legacy `portfolio.html` composition that
    # hardcoded designer-specific copy ("Sono una designer indipendente",
    # "Selected work · 2018 — 2026", "Ogni progetto una storia",
    # "Featured · Atlas Magazine", "Independent designer · Milano"),
    # so Pixel (photographer) rendered as a designer — identity crash.
    # Session 18 split the pair into two DNA archetypes. Chiara stays
    # on a paper-cream typographic ledger (no hero photo — the hero IS
    # the typography) and Pixel goes to a fully dark fullbleed cinematic
    # layout where the hero is a single dominant photograph.
    # ─────────────────────────────────────────────────────────────

    # ── P1) EDITORIAL-DESIGNER-GRID — Chiara, indep designer ────
    "chiara-portfolio-creativo": {
        "archetype":          "editorial-designer-grid",
        "hero_style":         "typographic-index-ledger",
        "navbar_style":       "index-rule",
        "footer_style":       "clients-ribbon",
        "section_order":      ["rule-nav", "typographic-hero", "project-ledger", "clients-ribbon"],
        "card_style":         "indexed-case-study",
        "button_style":       "ghost-sans-rule",
        "density":            "very-airy",
        "tone":               "editorial-designer",
        "imagery_direction":  "design-workspace",
        "imagery_key":        "portfolio-designer",
        "conversion_pattern": "case-study-request",
        "font_pairing":       ("Syne", "Inter"),
        "content": {
            "eyebrow":       "Studio indipendente · identità, libri e art direction",
            # Headline trimmed in Session 19 triage: the previous 57-char
            # phrase ("Sistemi di identità visiva costruiti una griglia alla
            # volta.") wrapped to 4-5 lines at the editorial-designer-grid
            # hero h1 size and collided with the left-column meta-strip and
            # the ledger below. The new 47-char version wraps cleanly to
            # 2 lines, preserves both signature signals ("identità visive"
            # + "una griglia alla volta") and reinforces the deliberate
            # syntactic parallel with Pixel's "Fermare il tempo, una luce
            # alla volta." — designer (griglia) vs photographer (luce).
            "headline":      'Identità visive, <em>una griglia alla volta</em>.',
            "subhead":       "Disegniamo brand culturali, collane editoriali e art direction per istituzioni e case editrici italiane. Ogni progetto parte da una griglia, una voce tipografica e una tavola cromatica su misura — dal marchio alla stampa.",
            "primary_cta":   "Richiedi il portfolio completo",
            "secondary_cta": "Scrivici",
            "contact_email": "studio",
            "status_label":  "Nuove commesse",
            "status_value":  "Aperte da settembre",
            "nav_links":     ["Indice", "Studio", "Approccio", "Archivio", "Contatti"],
            "meta_strip": [
                ("Fondato nel",        "2018"),
                ("Discipline",          "Identità · Editoria · Art direction"),
                ("Base",                "Studio · su appuntamento"),
            ],
            "ledger_label":     "Archivio lavori",
            "ledger_heading":   "Progetti selezionati · ventidue case study",
            "ledger_note":      "Una selezione ragionata dell'ultimo anno di studio. L'archivio completo è disponibile su richiesta, in formato PDF stampabile.",
            "categories":       ["Tutto", "Identità", "Editoria", "Art direction", "Packaging"],
            "projects": [
                # (index, title, category, year, medium)
                ("01", "Casa editrice · collana saggistica",     "Editoria",      "2026", "Collana · 24 titoli"),
                ("02", "Festival di poesia contemporanea",       "Identità",      "2026", "Identità integrale"),
                ("03", "Fondazione culturale · rebranding",      "Art direction", "2025", "Ridisegno completo"),
                ("04", "Vino naturale · etichette d'autore",     "Packaging",     "2025", "Sei cuvée · sei autori"),
                ("05", "Museo civico · segnaletica permanente",  "Identità",      "2025", "Wayfinding 42 sale"),
                ("06", "Rivista d'architettura · redesign",      "Editoria",      "2024", "Testata · template · griglia"),
            ],
            "clients_label":   "Hanno scelto lo studio",
            "clients":         ["CASA EDITRICE", "FESTIVAL POESIA", "FONDAZIONE", "VINO D'AUTORE", "MUSEO CIVICO", "RIVISTA D'ARCHITETTURA"],
            "coordinates_label": "Lo studio",
            "coordinates": [
                ("Indirizzo", "su appuntamento"),
                ("Telefono",  "solo via email"),
            ],
        },
    },

    # ── P2) CINEMATIC-PHOTOGRAPHER — Pixel, visual storyteller ──
    "pixel-portfolio-fotografico": {
        "archetype":          "cinematic-photographer",
        "hero_style":         "fullbleed-exif",
        "navbar_style":       "fullbleed-dark",
        "footer_style":       "exif-credits",
        "section_order":      ["fullbleed-dark-nav", "fullbleed-hero", "series-counter", "filmstrip-gallery", "exif-credits"],
        "card_style":         "filmstrip-series",
        "button_style":       "ghost-mono-bracket",
        "density":            "compact",
        "tone":               "cinematic-authorial",
        "imagery_direction":  "cinematic-photostill",
        "imagery_key":        "portfolio-photographer",
        "conversion_pattern": "series-brief",
        "font_pairing":       ("Archivo", "Inter"),
        "content": {
            "eyebrow":       "Fotografia documentaria · reportage editoriale e ritratti di scena",
            "headline":      'Fermare il <em>tempo</em>, una luce alla volta.',
            "subhead":       "Dodici anni tra commissioni editoriali, ritratti di scena e still-life per brand italiani. Ogni serie è un piccolo film — scritto con l'obiettivo, montato in camera oscura.",
            "primary_cta":   "Apri la serie completa",
            "secondary_cta": "Richiedi una commissione",
            "status_pulse":  "Disponibile per commissioni",
            "nav_links":     ["Serie", "Commissioni", "Stampe", "Diario", "Contatti"],
            "series_counter_label": "Serie in evidenza",
            "series_counter_value": "06 / 42",
            "series_label":    "Serie corrente",
            "series_title":    "«Le ore rubate»",
            "series_note":     "Ritratto di una notte senza luna, girato su pellicola 120mm tra le cinque e le otto del mattino. Venti fotogrammi, un'unica scatola di luce.",
            "hero_credit_cells": [
                # Film-strip EXIF bar: (label, value)
                ("Serie",       "N° 06"),
                ("Pellicola",    "Medio formato 120"),
                ("Ottica",       "Fisso 80mm · f/2.8"),
                ("Stampa",       "Fine art · tiratura 12"),
            ],
            "filmstrip_heading": "Ultime serie fotografiche",
            "filmstrip_label":   "Portfolio",
            "filmstrip": [
                # (index, title, discipline, year)
                ("06", "Le ore rubate",              "Ritratto notturno",     "2026"),
                ("05", "Campi lunghi",                "Paesaggio · reportage", "2025"),
                ("04", "Stanze vuote",                "Still-life · interni",  "2025"),
                ("03", "La città senza persone",      "Reportage urbano",      "2024"),
            ],
            "exif_footer_label": "Credit · prossima serie · Spring 2026",
            "exif_footer_cells": [
                ("Sede",        "Studio in affitto · prenota"),
                ("Commissioni", "Aperte · 3 slot"),
                ("Pubblicato",  "Stampa fine-art · su richiesta"),
                ("Contatto",    "solo email"),
            ],
        },
    },

    # ── 5) SPECIALIST (derm) — archetype reuse validation ────────
    # Second template on the `specialist` archetype. Proves that a new
    # multi-page template can ship with ZERO new HTML files: same chrome,
    # different brand / palette / content / tone / font pairing.
    "dermatologia-elite-roma": {
        "archetype":          "specialist",
        "preview_archetype":  "specialist-derm",
        "hero_style":         "editorial-serif",
        "navbar_style":       "minimal-serif",
        "footer_style":       "centered-minimal",
        "section_order":      ["nav", "editorial-hero", "drop-cap", "fields", "press", "footer"],
        "card_style":         "editorial-large",
        "button_style":       "ghost-underline",
        "density":            "very-airy",
        "tone":               "prestigious",
        "imagery_direction":  "aesthetic-clinical — skin, dermatoscopy, treatment rooms",
        "imagery_key":        "medical-dermatology",
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
            "hero_meta": [
                ("Direzione clinica", "Dr.ssa L. Ricciardi"),
                ("Esperienza", "18 anni"),
                ("Pazienti/anno", "2.400+"),
            ],
            "credit_left":  ("Studio",     "Roma · Via Veneto"),
            "credit_right": ("Specialità", "Dermatologia"),
            "press": ["JAMA Dermatology", "British Journal of Dermatology", "Vanity Fair Wellness", "Corriere Salute", "Vogue Italia"],
            "nav_links": ["Studio", "Visite", "Pubblicazioni", "Contatti"],
        },
    },

    # ── 4) SPECIALIST — editorial high-end ───────────────────────
    "cardio-studio-specialistico": {
        "archetype":          "specialist",
        "preview_archetype":  "specialist-cardio",
        "hero_style":         "editorial-serif",
        "navbar_style":       "minimal-serif",
        "footer_style":       "centered-minimal",
        "section_order":      ["nav", "editorial-hero", "drop-cap", "fields", "press", "footer"],
        "card_style":         "editorial-large",
        "button_style":       "ghost-underline",
        "density":            "very-airy",
        "tone":               "prestigious",
        "imagery_direction":  "clinical-cardiovascular — ECG, stethoscope, consultation",
        "imagery_key":        "medical-cardiology",
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
            "hero_meta": [
                ("Direzione clinica", "Dr. R. Marani"),
                ("Esperienza", "15 anni"),
                ("Visite/anno", "1.200+"),
            ],
            "credit_left":  ("Studio",      "Roma · Parioli"),
            "credit_right": ("Riferimento", "SC Cardiologia"),
            "press": ["LANCET", "European Heart Journal", "Corriere Salute", "Sole 24 Ore", "RAI Med"],
            "nav_links": ["Studio", "Visite", "Pubblicazioni", "Contatti"],
        },
    },

    # ─────────────────────────────────────────────────────────────
    # Wave 2 Pilot #1 — Fiscus (Phase X.4, 2026-04-20)
    # Reuses corporate-suite archetype (Pragma's skin) but with
    # dashboard-light visual style + warm-neutral palette + fiscal
    # voice. D-054 differentiation from Pragma is content + palette
    # + imagery driven (same chrome, different identity).
    # ─────────────────────────────────────────────────────────────

    # ── W2-2) CORPORATE-SUITE — Solaria, business coaching ───────
    # Third template on corporate-suite archetype (after Pragma
    # + Fiscus). D-054 differentiation vs both siblings is content
    # + palette + imagery-pool + typography + voice driven — zero
    # skin-folder changes. Reviewer MUST verify 10/10 gates against
    # both Pragma and Fiscus before the Commit B tier flip. Voice
    # anchor: "Il coaching non è terapia e non è consulenza." The
    # hero must contain "coaching" OR "percorso" + process verb
    # (decidere / orientare / ripensare) — NEVER "trasforma / cambia".
    "solaria-coaching": {
        "archetype":          "corporate-suite",
        "hero_style":         "split-conversation",
        "navbar_style":       "minimal-warm",
        "footer_style":       "sectors-ribbon",
        "section_order":      ["nav", "editorial-hero", "advisory-pillars", "kpi-strip", "sectors-ribbon"],
        "card_style":         "pillar-advisory",
        "button_style":       "ghost-warm",
        "density":            "airy",
        "tone":               "professional-warm",
        "imagery_direction":  "coaching-conversation",
        "imagery_key":        "business-coaching",
        "conversion_pattern": "discovery-call-booking",
        "font_pairing":       ("Fraunces", "Inter"),
        "content": {
            "eyebrow":       "Business coaching · ICF · Milano · dal 2014",
            "headline":      'Il coaching non è <em>terapia</em> e non è <em>consulenza</em>.',
            "subhead":       "Percorsi di coaching individuali e di team per imprenditori, dirigenti in transizione e middle manager. Metodo dichiarato (GROW · Co-Active · Immunity to Change), cadenza concordata, inizio e fine dichiarati — senza trasformazioni in trenta giorni.",
            "primary_cta":   "Prenota una discovery call",
            "secondary_cta": "Il metodo",
            "phone":         "+39 02 3663 4712",
            "nav_links":     ["Il metodo", "Il coach", "Percorsi", "Casi", "Contatti"],
            "meta_strip": [
                ("Sede",              "Milano · Isola · anche online"),
                ("Certificazione",    "ICF-PCC · EMCC"),
                ("Ore erogate",       "2.400+ ore · 160+ coachee"),
            ],
            "hero_credit_left":  ("Direzione",        "Dott.ssa G. Loreti"),
            "hero_credit_right": ("Certificazione",   "ICF-PCC dal 2017"),
            "pillars_heading": "Tre percorsi, un solo metodo",
            "pillars_label":   "Percorsi",
            "pillars": [
                ("01", "Executive 1:1",
                 "Otto sessioni da 60 minuti, cadenza bisettimanale, obiettivo definito in primo incontro. "
                 "Per dirigenti in transizione di ruolo, neo-promossi o in preparazione a un cambio di perimetro."),
                ("02", "Team coaching",
                 "Sei sessioni con il team (5-10 persone), più re-contracting a metà percorso. "
                 "Per team di middle management in fase di crescita o integrazione post-riorganizzazione."),
                ("03", "Gruppo aziendale",
                 "Masterclass + percorso 1:1 per 3-8 persone dell'azienda cliente. "
                 "Sponsor aziendale definito, obiettivi individuali + di sistema, follow-up trimestrale."),
            ],
            "kpi_heading": "Dodici anni di pratica certificata",
            "kpi_strip": [
                ("12",       "anni di pratica ICF"),
                ("2.400+",   "ore di coaching erogate"),
                ("160+",     "coachee seguiti"),
                ("100%",     "percorsi con follow-up a 3 mesi"),
            ],
            "sectors_label": "Settori dei coachee",
            "sectors": ["Tech & product", "Manifattura & industria", "Professional services", "Non-profit & scuola", "Health & vita"],
        },
    },

    # ── W2-1) CORPORATE-SUITE — Fiscus, studio tributario ────────
    "fiscus-commercialista": {
        "archetype":          "corporate-suite",
        "hero_style":         "split-advisory",
        "navbar_style":       "solid-institutional",
        "footer_style":       "sectors-ribbon",
        "section_order":      ["nav", "editorial-hero", "advisory-pillars", "kpi-strip", "sectors-ribbon"],
        "card_style":         "pillar-advisory",
        "button_style":       "ghost-institutional",
        "density":            "airy",
        "tone":               "institutional-fiscal",
        "imagery_direction":  "fiscal-desk-documents",
        "imagery_key":        "business-fiscal",
        "conversion_pattern": "appointment-request",
        "font_pairing":       ("IBM Plex Serif", "IBM Plex Sans"),
        "content": {
            "eyebrow":       "Studio tributario · Milano · iscritto ODCEC dal 2003",
            "headline":      'L\'adempimento <em>corretto</em>, non la trovata.',
            "subhead":       "Studio tributario per partite IVA, PMI e famiglie imprenditoriali. Dichiarazione dei redditi, bilancio, contenzioso tributario e pianificazione fiscale pluriennale — senza promesse di risparmio, con il calendario delle scadenze alla mano.",
            "primary_cta":   "Primo appuntamento",
            "secondary_cta": "Scarica la guida scadenze",
            "phone":         "+39 02 4951 3388",
            "nav_links":     ["Lo studio", "Competenze", "Scadenze", "Casi seguiti", "Contatti"],
            "meta_strip": [
                ("Sede",           "Milano · Porta Venezia"),
                ("Albo ODCEC",     "dal 2003 · 4 iscritti"),
                ("Clienti attivi", "260 partite IVA"),
            ],
            "hero_credit_left":  ("Direzione",       "Dott. A. Ruffini"),
            "hero_credit_right": ("Anno fondazione", "2003"),
            "pillars_heading": "Tre pratiche, una sola firma",
            "pillars_label":   "Aree di competenza",
            "pillars": [
                ("01", "Dichiarazione & bilancio",
                 "Dichiarazione dei redditi, quadro RW, certificazione unica e bilancio d'esercizio — audit-ready, con calendario delle revisioni concordato a gennaio."),
                ("02", "Contenzioso tributario",
                 "Assistenza in accertamento, ravvedimento operoso, ricorso in Commissione Tributaria. Mai promesse di esito, sempre una stima preliminare delle probabilità."),
                ("03", "Wealth & passaggio generazionale",
                 "Pianificazione fiscale pluriennale, holding di famiglia, successione e donazione — per patrimoni privati medio-alti e famiglie imprenditoriali."),
            ],
            "kpi_heading": "Ventidue anni di pratica continuativa",
            "kpi_strip": [
                ("22",       "anni dalla fondazione"),
                ("260",      "partite IVA in portafoglio"),
                ("€ 180 M",  "fatturato clienti aggregato"),
                ("0",        "sanzioni non previste nel 2025"),
            ],
            "sectors_label": "Settori dei clienti",
            "sectors": ["Partite IVA & freelance", "PMI manifattura", "Studi professionali", "Wealth privato", "Immobiliare"],
        },
    },

    # ── X.4D-OR1) CORPORATE-SUITE — Continua, family-office stewardship ──
    # Phase X.4 design-orchestrator first real candidate (pass 1 IT,
    # 2026-04-29). 4th corporate-suite sibling · 1st family-office
    # variant · multi-generational governance positioning. Reuses
    # the corporate-suite shell but with stewardship-specific voice
    # (custodial · multi-decade horizon · NOT decisional gravity ·
    # NOT presidio · NOT bounded-method), pine + pewter + brass
    # palette (matrix §1.3 cool-secondary + warm-accent · the only
    # OPEN warmth combo in the cluster), Crimson Pro + Public Sans
    # typography (closes the §1.4 cluster-collapse risk · explicitly
    # NOT Inter), object-led hero with zero people (the cluster's
    # first), and a governance-cycle-strip mid-beat (the differentiator
    # that names a CADENCE not a number/calendar/arc).
    "continua-stewardship": {
        "archetype":          "corporate-suite",
        "hero_style":         "split-stewardship",
        "navbar_style":       "solid-stewardship",
        "footer_style":       "sectors-ribbon-continuita",
        "section_order":      ["nav", "editorial-hero", "advisory-pillars", "kpi-strip", "governance-cycle-strip", "sectors-ribbon"],
        "card_style":         "pillar-stewardship",
        "button_style":       "ghost-stewardship",
        "density":            "airy",
        "tone":               "stewardship-longitudinal",
        "imagery_direction":  "stewardship-archive-room",
        "imagery_key":        "business-stewardship",
        "conversion_pattern": "mandate-dialogue",
        # Crimson Pro (heading · classical book-jacket ratios · strong italic
        # carrying multi-generational time-horizon) + Public Sans (body ·
        # public-trust association · gov-designed · explicitly NOT Inter).
        "font_pairing":       ("Crimson Pro", "Public Sans"),
        "content": {
            "eyebrow":       "Family office · Milano · stewardship multigenerazionale",
            "headline":      "La continuità di una famiglia si misura in <em>generazioni</em>.",
            "subhead":       "Custodi del patrimonio familiare attraverso le generazioni. Una famiglia, un Consiglio di Famiglia, un mandato che non si misura in trimestri.",
            "primary_cta":   "Avvia un dialogo di mandato",
            "secondary_cta": "Lo studio di custodia",
            "phone":         "+39 02 7600 4188",
            "nav_links":     ["Lo studio", "Custodia", "Governance", "Mandati", "Contatti"],
            "meta_strip": [
                ("Mandato medio",     "18 anni"),
                ("Generazioni in carico", "3"),
                ("Riunioni CdF",      "4 / anno"),
            ],
            "hero_credit_left":  ("Custodi del mandato", "Iscrizione Albo Trustees"),
            "hero_credit_right": ("Sede principale",     "Milano · Brera"),
            "pillars_heading": "Quattro presidi, un solo mandato",
            "pillars_label":   "Custodia",
            "pillars": [
                ("01", "Custodia patrimoniale",
                 "Custodiamo il patrimonio familiare attraverso il ciclo di tre generazioni — asset finanziari, partecipazioni, immobili strumentali e di famiglia, nel rispetto del patto di famiglia in vigore."),
                ("02", "Governance familiare",
                 "Facilitazione del Consiglio di Famiglia, redazione e revisione del patto familiare, voting structures dei rami familiari, codici di comportamento e regolamenti interni."),
                ("03", "Successione strutturata",
                 "Pianificazione del passaggio multigenerazionale — donazioni, holding di famiglia, trust dedicati, formazione della generazione entrante prima del trasferimento di responsabilità."),
                ("04", "Compliance fiduciaria",
                 "Vigilanza fiduciaria continuativa, audit di continuità annuale, presidio normativo in evoluzione (D.lgs. 24/2023, Codice della Crisi, OAM) e custodia documentale a accesso controllato."),
            ],
            "kpi_heading": "Diciotto anni di mandati in continuità",
            "kpi_strip": [
                ("18",      "anni · orizzonte medio mandato"),
                ("3",       "generazioni · famiglie in carico"),
                ("€ 1.8 B", "patrimonio in custodia"),
                ("4",       "riunioni CdF · anno"),
            ],
            "sectors_label": "Profili familiari",
            "sectors": ["Famiglie imprenditoriali", "Holding di partecipazioni", "Fondazioni di famiglia", "Seconde generazioni in trasferimento", "Single family office estero"],
        },
    },

    # ── X.5) CORPORATE-SUITE — Cornice, single-principal architecture studio ──
    # Phase X.5 · A.5 build · 5th corporate-suite sibling · 1st
    # architecture-firm variant · 1st LF-2 (Editorial Spread) occupant.
    # Validates the layout-family system per
    # `factory/reports/hardening/corporate-suite-layout-divergence-plan.md
    # §10 Step 6`. Reuses the corporate-suite shell but routes home
    # rendering through `_layouts/lf2/` (stacked-editorial hero · zero
    # dark band · narrative essay with drop-cap · single-portrait
    # masthead · 3+1 magazine-grid cases · split-wordmark navbar ·
    # 4-col footer with whistleblowing column).
    "cornice-architettura": {
        "archetype":          "corporate-suite",
        "hero_style":         "stacked-editorial-cornice",
        "navbar_style":       "split-wordmark-cornice",
        "footer_style":       "four-col-cornice",
        "section_order":      ["nav", "stacked-editorial-hero", "essay-with-anchors", "sectors-ribbon", "single-portrait-feature", "magazine-grid-cases", "cta-closer-cream"],
        "card_style":         "magazine-card-cornice",
        "button_style":       "ghost-cornice",
        "density":            "airy-editorial",
        "tone":               "editorial-curatorial",
        "imagery_direction":  "architecture-editorial-built-form",
        "imagery_key":        "business-architecture",
        "conversion_pattern": "project-dossier-submission",
        # Cormorant Garamond (heading · classical book-jacket display
        # ratios · architectural-monograph register · strong italic on
        # the curatorial noun `argomento`) + Source Sans 3 (body ·
        # editorial-clean · explicitly NOT Inter · NOT Plex Sans ·
        # NOT Public Sans). Closes the matrix §1.4 cluster-collapse
        # risk forward of Continua's Crimson + Public Sans choice.
        "font_pairing":       ("Cormorant Garamond", "Source Sans 3"),
        "content": {
            "eyebrow":       "Studio di architettura · Milano · dal 2008",
            "headline":      "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.",
            "subhead":       "Studio di architettura editoriale · committenze pubbliche e private · novanta fascicoli aperti dal 2008.",
            "primary_cta":   "Apri un fascicolo progetto",
            "secondary_cta": "Lo studio · pubblicazioni",
            "phone":         "+39 02 6610 4708",
            "nav_links":     ["Studio", "Servizi", "Progetti", "Contatti"],
            "meta_strip": [
                ("Progetti realizzati", "47"),
                ("Anni di pratica",     "18"),
                ("Città italiane",      "6"),
            ],
            "hero_credit_left":  ("Bologna · portico restaurato · 2023", "fascicolo n. 31"),
            "hero_credit_right": ("Sede dello studio",                   "Milano · via Paoli 9"),
            "sectors_label": "Tipologie d'intervento",
            "sectors": ["residenziale", "pubblico", "interno", "paesaggio", "restauro", "concorso", "culturale", "uffici", "industriale", "sanitario", "scolastico", "misto-uso"],
        },
    },

    # ── X.6) CORPORATE-SUITE — Causa, single-principal Cassazionista
    #         litigation boutique (2nd LF-2 occupant after Cornice) ──
    # Phase X.6 · A.5 build · 6th corporate-suite sibling · 1st
    # evidence-led litigation-boutique variant · 2nd LF-2 (Editorial
    # Spread) occupant. Validates the layout-family system at the
    # second-occupant level per `factory/reports/causa/causa-planner-
    # brief.md §2.4` (LF-2 family signatures inherited verbatim).
    # Reuses the corporate-suite shell + LF-2 `_layouts/lf2/` rendering
    # path identical to Cornice (stacked-editorial hero · zero dark
    # bands · narrative essay with drop-cap · single-portrait masthead
    # · 3+1 magazine-grid cases · split-wordmark navbar · 4-col footer
    # with whistleblowing column · cream-hairline CTA closer).
    #
    # Voice: forensic-publication · evidence-led · public-record
    # register, explicitly NOT decisional-gravity (Pragma) · NOT
    # presidio-with-scadenze (Fiscus) · NOT bounded-method (Solaria)
    # · NOT stewardship-longitudinal (Continua) · NOT curatorial-
    # thesis (Cornice). Voice anchor noun `evidenza` on ONE em per
    # heading (CS-EXEC-01 default · NOT Solaria's two-em pair).
    #
    # Palette: bottle-green primary + bone secondary + obsidian accent
    # — full cool · matte-on-matte · zero metallic. Third polarity
    # dimension per matrix §1.3 (`matte-on-matte without metallic` ·
    # opposite of Continua's cool-with-warm-chrome-only-metallic and
    # orthogonal to Cornice's neutral-with-warm-display-only-rust).
    # Hex distance ≥6 ΔE from Continua pine `#0F3A30` enforced.
    # Accent surface deployment: body-typographic-only (drop-cap ·
    # pull-quote em · CTA fill optional · focus ring) — explicitly
    # NOT chrome-metallic (Continua's brass deployment surface class).
    #
    # Typography: GT Sectra primary heading serif (forensic-publication
    # register · NOT architectural-press Cormorant Garamond) · Source
    # Serif Pro fallback declared at planner level. Manrope body sans
    # · Inter explicitly forbidden per CS-LAYOUT-20 (3rd cluster use
    # collapses body-sans differentiation).
    #
    # Imagery: NEW pool `business-legale` · Pexels-only · 6 URLs +
    # 4 magazine-grid extras + backups. Cross-cluster grep CLEAN
    # against business-corporate / business-architecture / business-
    # fiscal / business-coaching / business-stewardship. Hero subject
    # is empty courtroom interior (cool light · vertical timber + bone
    # walls · zero people · interior architectural) — explicitly NOT
    # Bologna golden-hour portico (Cornice) · NOT library reading-room
    # mahogany (Continua) · NOT boardroom long-table (Pragma) · NOT
    # tidy-desk-with-documents (Fiscus) · NOT 1:1 conversation
    # (Solaria).
    "causa-legale": {
        "archetype":          "corporate-suite",
        "hero_style":         "stacked-editorial-causa",
        "navbar_style":       "split-wordmark-causa",
        "footer_style":       "four-col-causa",
        "section_order":      ["nav", "stacked-editorial-hero", "essay-with-anchors", "sectors-ribbon", "single-portrait-feature", "magazine-grid-cases", "cta-closer-cream"],
        "card_style":         "magazine-card-causa",
        "button_style":       "filled-bottle-green-causa",
        "density":             "airy-forensic",
        "tone":                "forensic-publication",
        "imagery_direction":  "legal-courtroom-codex-chambers",
        "imagery_key":        "business-legale",
        "conversion_pattern": "parere-preliminare-screening",
        # GT Sectra primary heading serif (with Source Serif Pro
        # licence-fallback declared at planner-brief §9). Manrope body
        # sans · NO fallback (Inter explicitly forbidden per CS-LAYOUT-
        # 20 · 3rd cluster use collapses body-sans differentiation).
        "font_pairing":       ("GT Sectra", "Manrope"),
        "content": {
            "eyebrow":       "Studio legale · Milano · dal 1995",
            "headline":      "Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.",
            "subhead":       "Studio legale di patrocinio editoriale · Cassazionista fondatore · ventotto sentenze citate dal 1995.",
            "primary_cta":   "Apri un parere preliminare",
            "secondary_cta": "Studio · sede di Milano",
            "phone":         "+39 02 7634 8210",
            "nav_links":     ["Studio", "Materie", "Pubblicazioni", "Contenzioso", "Contatti"],
            "meta_strip": [
                ("Sentenze citate",    "28"),
                ("Voci in massimario", "14"),
                ("Anni di patrocinio", "31"),
            ],
            "hero_credit_left":  ("Aula di tribunale · interno · 2024", "Foro di Milano"),
            "hero_credit_right": ("Sede dello studio",                   "Milano · via Borgonuovo 14"),
            "sectors_label": "Materie del contenzioso",
            "sectors": ["penale tributario", "civile contrattualistica", "amministrativo regolatorio", "contenzioso bancario", "responsabilità professionale", "recupero crediti complesso", "diritto societario", "tributario", "esecuzioni", "lavoro complesso", "CTU forense", "ENCA mediation"],
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
