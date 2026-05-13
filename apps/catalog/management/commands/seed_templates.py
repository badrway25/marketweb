from decimal import Decimal

from django.core.management import call_command
from django.core.management.base import BaseCommand

from apps.catalog.models import (
    Category,
    ProfessionCluster,
    TemplateBrand,
    VisualStyle,
    WebTemplate,
)


# ── X.2 Commit 3 · taxonomy v2 metadata for fresh seeds ────────────
#
# Mirrors ``TEMPLATE_METADATA`` in ``migrations/0004_taxonomy_v2_backfill``
# so that: (a) a freshly-seeded database lands in the same end-state as
# a production DB that had backfill applied, and (b) future template
# additions carry metadata at seed time without a separate migration.
# Consistency between the two definitions is locked by
# ``test_backfill_dict_and_seed_templates_dict_match`` in the catalog
# test suite.
TEMPLATE_METADATA = {
    "vertex-creative-agency": {
        "cluster": "creative",
        "style": "editorial-warm",
        "price_tier": "premium",
        "use_cases": ["show-portfolio", "generate-leads", "brand-identity"],
        "audience": ["agency", "studio"],
        "search_keywords": (
            "agenzia creativa brand design portfolio case-study studio creative"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": True,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "aura-digital-studio": {
        "cluster": "digital-growth",
        "style": "dashboard-dark",
        "price_tier": "premium",
        "use_cases": ["show-portfolio", "generate-leads", "growth-tech"],
        "audience": ["agency", "studio"],
        "search_keywords": (
            "agenzia digital growth performance sprint studio tech midnight"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": True,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "pragma-corporate-suite": {
        "cluster": "corporate",
        "style": "classic-serif",
        "price_tier": "standard",
        "use_cases": ["corporate-presence", "generate-leads", "b2b-credibility"],
        "audience": ["enterprise", "smb"],
        "search_keywords": (
            "corporate azienda istituzionale b2b enterprise consulenza business"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "elevate-startup-landing": {
        "cluster": "saas-landing",
        "style": "dashboard-dark",
        "price_tier": "premium",
        "use_cases": ["product-launch", "generate-leads", "demo-bookings"],
        "audience": ["smb", "enterprise"],
        "search_keywords": (
            "saas startup prodotto landing pricing demo b2b tech"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "gusto-fine-dining": {
        "cluster": "fine-dining",
        "style": "editorial-warm",
        "price_tier": "premium",
        "use_cases": ["reservations", "menu-online", "brand-storytelling"],
        "audience": ["smb"],
        "search_keywords": (
            "ristorante stellato chef fine-dining gourmet haute-cuisine prenotazione"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "sapore-trattoria-pizzeria": {
        "cluster": "trattoria",
        "style": "editorial-warm",
        "price_tier": "standard",
        "use_cases": ["reservations", "menu-online", "local-presence"],
        "audience": ["smb", "freelance"],
        "search_keywords": (
            "trattoria pizzeria osteria menu tradizionale regionale prenotazione"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "brace-street-food-lab": {
        "cluster": "street-casual",
        "style": "bold-display",
        "price_tier": "standard",
        "use_cases": ["online-ordering", "menu-online", "brand-youth"],
        "audience": ["smb"],
        "search_keywords": (
            "street-food burger casual cloud-kitchen ordering pickup lab"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "salute-studio-medico": {
        "cluster": "multi-clinic",
        "style": "minimal-light",
        "price_tier": "standard",
        "use_cases": [
            "appointment-booking",
            "patient-info",
            "professional-credibility",
        ],
        "audience": ["smb", "studio"],
        "search_keywords": (
            "clinica poliambulatorio medicina-generale visita prenotazione ambulatorio"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "benessere-centro-olistico": {
        "cluster": "wellness-holistic",
        "style": "minimal-light",
        "price_tier": "standard",
        "use_cases": ["appointment-booking", "wellness-brand", "retreats-booking"],
        "audience": ["smb", "studio"],
        "search_keywords": (
            "olistico wellness benessere nutrizione naturopatia retreat trattamenti"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "famiglia-pediatria": {
        "cluster": "family-pediatric",
        "style": "minimal-light",
        "price_tier": "standard",
        "use_cases": ["appointment-booking", "family-trust", "pediatric-brand"],
        "audience": ["studio", "smb"],
        "search_keywords": (
            "pediatria famiglia bambini pediatra visita ginecologia"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "cardio-studio-specialistico": {
        "cluster": "specialist",
        "style": "minimal-light",
        "price_tier": "premium",
        "use_cases": [
            "appointment-booking",
            "specialist-credibility",
            "medical-authority",
        ],
        "audience": ["freelance", "studio"],
        "search_keywords": (
            "cardiologo cuore specialista studio-medico visita-specialistica"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    # Wave 1 Pass-1 (T45 · 2026-05-11) — Denti+Co Studio Dentistico.
    # 3rd template on `specialist` archetype (zero new HTML). Cluster
    # `dental` activates for the first time (was 0 templates). Price
    # tier `standard` (€ 75) vs Cardio/Derm `premium` — wider audience
    # reach, lower entry barrier.
    "denti-co-studio": {
        "cluster": "dental",
        "style": "minimal-light",
        "price_tier": "standard",
        "use_cases": [
            "appointment-booking",
            "specialist-credibility",
            "preventive-care",
        ],
        "audience": ["studio", "smb"],
        "search_keywords": (
            "dentista odontoiatra studio-dentistico igiene impianti "
            "ortodonzia invisalign implantologia"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "dermatologia-elite-roma": {
        "cluster": "specialist",
        "style": "minimal-light",
        "price_tier": "premium",
        "use_cases": [
            "appointment-booking",
            "specialist-credibility",
            "aesthetic-services",
        ],
        "audience": ["freelance", "studio"],
        "search_keywords": (
            "dermatologo pelle estetica specialista roma visita-dermatologica"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "lex-studio-legale": {
        "cluster": "classic-law",
        "style": "classic-serif",
        "price_tier": "premium",
        "use_cases": ["consultation-booking", "case-studies", "legal-authority"],
        "audience": ["studio", "smb"],
        "search_keywords": (
            "avvocato studio-legale civile penale commerciale consulenza-legale"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    # T47 · Wave 1 Pass-3 (2026-05-12) — Studio Notarile Conti-Sironi-Verri.
    # 1st reuse of `classic-gold` archetype after Lex (zero new HTML).
    # Cluster `notary-commercialista` activates for the first time (was 0
    # templates). Price tier `premium` (€ 89) — same band as Lex (€ 69)
    # plus £20 institutional uplift. Seeds at tier=draft via
    # TEMPLATE_REGISTRY.json — IT-only at T47 build (D-102 cadence);
    # multilingual + flip via T47b or T48 depending on cadence.
    "atto-notai-associati": {
        "cluster": "notary-commercialista",
        "style": "classic-serif",
        "price_tier": "premium",
        "use_cases": [
            "primo-incontro-orientamento",
            "notarial-authority",
            "institutional-credibility",
        ],
        "audience": ["studio", "smb", "enterprise"],
        "search_keywords": (
            "notaio studio-notarile rogito testamento successione "
            "compravendita costituzione-società atto-pubblico procura "
            "donazione mutuo-ipotecario commercialista pubblico-ufficiale"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    # T49 · Wave 1 Pass-5 (2026-05-12) — Madou Pasticceria Atelier.
    # 1st reuse of `fine-dining` archetype after Gusto (D-051 Option A:
    # zero new HTML files). Cluster `bakery-pasticceria` activates for
    # the first time (was 0 templates). Price tier `premium` (€ 75) —
    # +€16 over Gusto's € 59 to signal pasticceria-atelier positioning.
    # Seeds at tier=draft via TEMPLATE_REGISTRY.json — IT-only at T49
    # build (D-102 cadence); multilingual + flip via T50.
    "madou-pasticceria": {
        "cluster": "bakery-pasticceria",
        "style": "editorial-warm",
        "price_tier": "premium",
        "use_cases": [
            "saturday-laminate-preorder",
            "menu-online",
            "brand-storytelling",
        ],
        "audience": ["smb"],
        "search_keywords": (
            "pasticceria atelier croissant maritozzo millefoglie saint-honore "
            "lievitazione-lenta pasta-sfoglia lievito-madre pasticciere torino "
            "wedding-cake cake-design pasticceria-artigianale"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": True,
        "has_video": False,
        # has_rtl=True per the D-098 invariant ("RTL is the catalog-
        # wide default" — fine-dining chrome already supports RTL as
        # proven by Gusto AR). AR locale lands in T50; the flag is
        # forward-declared here so the catalog invariant holds at draft.
        "has_rtl": True,
        "is_multi_page": True,
    },
    # T51 · Wave 1 Pass-7 (2026-05-12) — Studio Veterinario Petro.
    # 4th reuse of `specialist` archetype after Cardio + Derm + Denti
    # (D-051 Option A: zero new HTML files). Cluster `veterinary`
    # activates for the first time (was 0 templates). Price tier
    # `standard` (€ 75) — same band as Denti (specialist standard
    # bracket). Seeds at tier=draft via TEMPLATE_REGISTRY.json —
    # IT-only at T51 build (D-102 cadence); multilingual EN/FR/ES/AR
    # + AAA walk + public flip happen in T52.
    "petro-veterinario": {
        "cluster": "veterinary",
        "style": "minimal-light",
        "price_tier": "standard",
        "use_cases": [
            "preventive-booking",
            "appointment-booking",
            "specialist-credibility",
        ],
        "audience": ["smb", "studio"],
        "search_keywords": (
            "veterinario veterinaria clinica-animali ambulatorio-veterinario "
            "cane gatto coniglio furetto esotici vaccinazioni sterilizzazione "
            "visita-preventiva cura-preventiva pet ecografia chirurgia padova"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": True,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "juris-avvocato-moderno": {
        "cluster": "modern-law-tech",
        "style": "minimal-mono",
        "price_tier": "premium",
        "use_cases": ["consultation-booking", "legal-tech-brand", "modern-law"],
        "audience": ["freelance", "studio"],
        "search_keywords": (
            "avvocato moderno ip startup diritto-tech privacy gdpr consulenza"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "casa-agenzia-immobiliare": {
        "cluster": "real-estate-mass-market",
        "style": "minimal-light",
        "price_tier": "standard",
        "use_cases": ["property-listings", "lead-capture", "local-real-estate"],
        "audience": ["smb"],
        "search_keywords": (
            "immobiliare agenzia casa appartamento affitto vendita ricerca-casa"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "villa-immobili-lusso": {
        "cluster": "real-estate-luxury",
        "style": "cinematic-fullbleed",
        "price_tier": "premium",
        "use_cases": ["luxury-listings", "premium-brand", "lead-capture"],
        "audience": ["smb", "agency"],
        "search_keywords": (
            "villa lusso immobili-lusso prestigio proprietà-esclusive luxury-estate"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    # ── T56 Wave 2 Pass-1 (2026-05-12) ─────────────────────────────
    # `albergo-borgo` opens the `boutique-hotel` cluster (was 0 templates).
    # 1st reuse of ultra-luxury-cinematic archetype after Villa.
    # IT-only draft tier · multilingual rollout deferred to T57.
    # ── T59 Wave 2 Pass-3 (2026-05-13) ─────────────────────────────
    # `podere-agriturismo` opens the `bnb-agriturismo` cluster
    # (was 0 templates). 3rd reuse of artisan-workshop archetype
    # after Bottega + Sapori (D-051 Option A) · 2nd cross-category
    # reuse. IT-only draft tier · multilingual deferred to T60.
    "podere-agriturismo": {
        "cluster": "bnb-agriturismo",
        "style": "typographic-first",
        "price_tier": "standard",
        "use_cases": [
            "appointment-booking",
            "sell-online",
            "brand-storytelling",
        ],
        "audience": ["smb", "freelance"],
        "search_keywords": (
            "agriturismo podere greve chianti famiglia ospitalita contadina "
            "olio chianti-classico miele cinta-senese vendemmia raccolta "
            "antinori toscana dispensa contadina firenze"
        ),
        "has_shop": True,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": True,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "albergo-borgo": {
        "cluster": "boutique-hotel",
        "style": "cinematic-fullbleed",
        "price_tier": "premium",
        "use_cases": [
            "lead-capture",
            "premium-brand",
            "appointment-booking",
        ],
        "audience": ["smb", "studio"],
        "search_keywords": (
            "albergo relais boutique-hotel ospitalità borgo toscana val-orcia "
            "pienza siena unesco relais-chateaux concierge dimora seicento "
            "michelin spa cantina vino brunello"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": True,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "chiara-portfolio-creativo": {
        "cluster": "designer-editorial",
        "style": "editorial-warm",
        "price_tier": "premium",
        "use_cases": ["show-portfolio", "attract-clients", "editorial-brand"],
        "audience": ["freelance", "studio"],
        "search_keywords": (
            "designer portfolio editoriale graphic-designer art-direction brand-identity"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": True,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "pixel-portfolio-fotografico": {
        "cluster": "photographer",
        "style": "cinematic-fullbleed",
        "price_tier": "premium",
        "use_cases": ["show-portfolio", "attract-clients", "cinematic-brand"],
        "audience": ["freelance", "studio"],
        "search_keywords": (
            "fotografo portfolio cinematic fine-art ritratto architettura serie"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": True,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "bottega-shop-artigianale": {
        "cluster": "artisan-workshop",
        "style": "typographic-first",
        "price_tier": "premium",
        "use_cases": ["sell-online", "brand-storytelling", "artisan-identity"],
        "audience": ["smb", "freelance"],
        "search_keywords": (
            "artigiano bottega atelier maker tipografico editoriale vendita-online journal"
        ),
        "has_shop": True,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": True,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    # ── T53 Wave 1 Pass-9 (2026-05-12) ─────────────────────────────
    # `sapori-di-langa` opens the new `wine-food-boutique` cluster.
    # 1st archetype reuse of artisan-workshop after Bottega (D-051
    # Option A: zero new HTML). IT-only draft tier; multilingual
    # rollout deferred to T54 per D-102 cadence.
    "sapori-di-langa": {
        # Visual style reuses `typographic-first` (Bottega's style)
        # — D-054 differentiation comes via palette (bordeaux+cream+
        # olive vs walnut+cream+orange) + font pairing (IBM Plex
        # Serif/Sans vs Libre Baskerville+Nunito Sans) + voice anchor
        # + persona register, not via a new visual_style row.
        "cluster": "wine-food-boutique",
        "style": "typographic-first",
        "price_tier": "premium",
        "use_cases": ["sell-online", "case-order", "terroir-storytelling"],
        "audience": ["smb", "freelance"],
        "search_keywords": (
            "vino langhe barolo barbera nebbiolo dolcetto vignaiolo enoteca "
            "alba castelmagno olio-evo tartufo-bianco terroir sommelier "
            "cassa-vignaiolo cantina indipendente"
        ),
        "has_shop": True,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": True,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "luxe-fashion-store": {
        "cluster": "fashion-editorial",
        "style": "magazine-hybrid",
        "price_tier": "premium",
        "use_cases": ["sell-online", "luxury-brand", "lookbook-campaigns"],
        "audience": ["smb", "enterprise"],
        "search_keywords": (
            "fashion moda maison luxury lookbook editoriale concept-store vendita-online"
        ),
        "has_shop": True,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": True,
        "has_video": True,
        "has_rtl": True,
        "is_multi_page": True,
    },
    # ── T61 Wave 2 Pass-5 (2026-05-13) ─────────────────────────────
    # `gemma-gioielleria` opens the `jewelry` cluster (was 0 templates).
    # 1st reuse of fashion-editorial archetype after Luxe (D-051 Option A).
    # Same category as Luxe (ecommerce) · no skin_source_category needed.
    # Premium tier (€ 119 · alta gioielleria band above Luxe). Seeds at
    # tier=draft · multilingual + flip via T62.
    "gemma-gioielleria": {
        "cluster": "jewelry",
        "style": "magazine-hybrid",
        "price_tier": "premium",
        "use_cases": [
            "sell-online",
            "luxury-brand",
            "lookbook-campaigns",
            "appointment-booking",
        ],
        "audience": ["smb", "studio"],
        "search_keywords": (
            "gioielleria atelier orafo alta-gioielleria pezzo-unico serie-limitata "
            "milano brera buccellati GIA gemmologia castone filigrana brillante "
            "platino oro zaffiro smeraldo private-viewing concierge eleonora gemma"
        ),
        "has_shop": True,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": True,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    # ── Wave 2 Pilot #1 · Phase X.4 (2026-04-20) ────────────────
    # First pilot template produced by the Content Factory pipeline
    # (X.3). Reuses the corporate-suite archetype (Pragma's shell)
    # with commercialista-specific voice, dashboard-light visual
    # style, and the financial-services cluster. Seeds at `tier:
    # draft` (set in TEMPLATE_REGISTRY.json) — flipped to
    # published_live only after the 8-point Playwright walk.
    "fiscus-commercialista": {
        "cluster": "financial-services",
        "style": "dashboard-light",
        "price_tier": "standard",
        "use_cases": [
            "consultation-booking",
            "generate-leads",
            "b2b-credibility",
        ],
        "audience": ["smb", "freelance", "studio"],
        "search_keywords": (
            "commercialista fiscale finanza tasse contabilità "
            "dichiarazione-redditi wealth-management revisore "
            "studio-tributario partita-iva"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    # ── Wave 2 Pilot #2 · Phase X.4 (2026-04-21) ────────────────
    # Second Content Factory pilot. Also rides corporate-suite
    # archetype (shared shell with Pragma + Fiscus), but with
    # coaching-specific voice (professional-warm · method-declared ·
    # non-guru · non-therapy · non-consulting) + minimal-light
    # visual style + warm-earth accent palette. Seeds at `tier:
    # draft` — flipped to published_live only after Commit B + the
    # full multi-locale walk. Re-introduced under controlled
    # re-entry pass 1 (`phase-x4-solaria-controlled-reentry-pass1`).
    # ── Phase X.4 design-orchestrator · Continua (2026-04-29) ──
    # First real candidate produced by the design-orchestrator
    # system. Reuses corporate-suite archetype (shared shell with
    # Pragma + Fiscus + Solaria) but with stewardship-longitudinal
    # voice (custodial · multi-generational · NOT decisional-
    # gravity · NOT presidio · NOT bounded-method) + pine + pewter
    # + brass palette + Crimson Pro + Public Sans typography.
    # Seeds at `tier: draft` — IT-only at draft per the build brief
    # (D-102 cadence); multilingual rollout via workflow C in a
    # separate pass.
    "continua-stewardship": {
        "cluster": "corporate",
        "style": "classic-serif",
        "price_tier": "premium",
        "use_cases": [
            "consultation-booking",
            "generate-leads",
            "b2b-credibility",
        ],
        "audience": ["enterprise", "smb"],
        "search_keywords": (
            "family-office famiglie-imprenditoriali holding patrimonio "
            "successione governance-familiare consiglio-di-famiglia "
            "patto-familiare trustees stewardship multigenerazionale "
            "trust fondazione"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    # ── Phase X.5 · Cornice (2026-04-30) · 5th corporate-suite sibling · ──
    # 1st architecture-firm variant · 1st LF-2 (Editorial Spread)
    # occupant. Reuses the corporate-suite shell (Pragma + Fiscus +
    # Solaria + Continua) but routes home through `_layouts/lf2/` —
    # stacked-editorial hero, narrative essay with drop-cap, single-
    # portrait masthead, 3+1 magazine-grid cases, split-wordmark navbar,
    # 4-col footer with whistleblowing column. Voice editorial-curatorial
    # · architectural-discipline (NOT decisional gravity · NOT presidio
    # · NOT bounded-method · NOT stewardship-longitudinal). Palette
    # graphite + pietra-serena + terracotta-rust (NEUTRAL/NEUTRAL/WARM
    # · the only un-claimed cluster polarity). Cormorant Garamond +
    # Source Sans 3 (closes Inter cluster-collapse risk). Seeds at
    # `tier: draft` (set in TEMPLATE_REGISTRY.json) — IT-only per
    # D-102 cadence; multilingual rollout via workflow C.
    "cornice-architettura": {
        "cluster": "corporate",
        "style": "classic-serif",
        "price_tier": "premium",
        "use_cases": [
            "generate-leads",
            "b2b-credibility",
        ],
        "audience": ["enterprise", "smb"],
        "search_keywords": (
            "studio-architettura architetto fascicolo committenza "
            "rilievo restauro concorso paesaggio MIBAC OAPPC CNAPPC "
            "Soprintendenza vincolo cantiere progetto monografia "
            "collana editoriale autoriale"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": True,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    # Phase X.6 · Causa (6th corporate-suite sibling · 1st evidence-
    # led litigation-boutique variant · 2nd LF-2 occupant after
    # Cornice · IT-only at A.5 build · tier=draft per D-102 cadence).
    # Reuses the corporate-suite shell + LF-2 _layouts/lf2/ rendering
    # path identical to Cornice (stacked-editorial hero · zero dark
    # bands · narrative essay with drop-cap · single-portrait
    # masthead · 3+1 magazine-grid cases · split-wordmark navbar ·
    # 4-col footer with whistleblowing column). Voice forensic-
    # publication · evidence-led · public-record register (NOT
    # decisional-gravity Pragma · NOT presidio Fiscus · NOT bounded-
    # method Solaria · NOT stewardship-longitudinal Continua · NOT
    # curatorial-thesis Cornice). Palette bottle-green + bone +
    # obsidian (full cool · matte-on-matte · zero metallic · the
    # third polarity dimension per matrix §1.3). GT Sectra + Manrope
    # (Inter explicitly forbidden per CS-LAYOUT-20). has_booking=False
    # — litigation-shaped (parere-screening, NOT scheduled-booking) ·
    # planner-brief §5 + copy-authoring §1 binding. Seeds at `tier:
    # draft` (set in TEMPLATE_REGISTRY.json) — IT-only per D-102
    # cadence; multilingual rollout via workflow C in a separate pass.
    "causa-legale": {
        "cluster": "corporate",
        "style": "classic-serif",
        "price_tier": "premium",
        "use_cases": [
            "generate-leads",
            "b2b-credibility",
        ],
        "audience": ["enterprise", "smb"],
        "search_keywords": (
            "studio-legale avvocato cassazionista patrocinio "
            "contenzioso evidenza giurisdizione massima ricorso "
            "memoria fascicolo processuale appello primo-grado "
            "legittimità sezioni-unite TAR commissione-tributaria "
            "Albo Avvocati Milano ENCA Albo-CTU forense parere-"
            "preliminare litigation"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": True,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "solaria-coaching": {
        "cluster": "coaching",
        "style": "minimal-light",
        "price_tier": "standard",
        "use_cases": [
            "consultation-booking",
            "generate-leads",
            "b2b-credibility",
        ],
        "audience": ["smb", "freelance"],
        "search_keywords": (
            "coach coaching business-coach executive-coach "
            "percorso-coaching icf team-coaching discovery-call "
            "mentor accountability"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
}

_FEATURE_FLAG_FIELDS = (
    "has_shop",
    "has_booking",
    "has_portfolio",
    "has_blog",
    "has_video",
    "has_rtl",
    "is_multi_page",
)


SEED_TEMPLATES = [
    # ── Agency (2) ──────────────────────────────────────────────
    {
        "name": "Vertex — Creative Agency",
        "slug": "vertex-creative-agency",
        "category_slug": "agency",
        "short_description": "Template audace e moderno per agenzie creative. Layout dinamico con portfolio interattivo e sezione case study.",
        "description": (
            "Vertex è il template definitivo per agenzie digitali e creative che vogliono fare colpo. "
            "Design audace con transizioni fluide, portfolio a griglia filtrabile, sezione case study con metriche di impatto, "
            "pagina team con profili dinamici, e un modulo contatto integrato con mappa.\n\n"
            "Include: homepage con hero animata, pagina servizi, portfolio filtrato, case study dettagliati, "
            "pagina chi siamo con timeline aziendale, blog con categorie e sidebar, modulo contatto avanzato."
        ),
        "price": Decimal("79.00"),
        "is_free": False,
        "featured": True,
        "order": 1,
        "brand": {
            "brand_name": "Vertex Studio",
            "tagline": "Dove la creatività incontra la strategia",
            "palette": {"primary": "#0D0D0D", "secondary": "#6366F1", "accent": "#F59E0B"},
            "typography": "Space Grotesk + Inter",
            "personality": "audace, tech-forward, dinamico",
            "logo_concept": "Lettera V stilizzata con angoli netti che richiama una freccia verso l'alto, in gradiente indigo-viola",
        },
    },
    {
        "name": "Aura — Digital Studio",
        "slug": "aura-digital-studio",
        "category_slug": "agency",
        "short_description": "Eleganza minimale per studi digitali e agenzie boutique. Focus su portfolio visivo e storytelling del brand.",
        "description": (
            "Aura è pensato per agenzie boutique che comunicano attraverso la qualità del lavoro. "
            "Layout pulito con ampi spazi bianchi, galleria portfolio fullscreen, "
            "animazioni scroll-based sottili e sezione testimonianze clienti.\n\n"
            "Include: homepage narrativa, portfolio con lightbox, pagina servizi modulare, "
            "sezione clienti con loghi, blog minimal, pagina contatti con calendario prenotazioni."
        ),
        "price": Decimal("69.00"),
        "is_free": False,
        "featured": False,
        "order": 2,
        "brand": {
            "brand_name": "Aura Creative",
            "tagline": "Design che parla da sé",
            "palette": {"primary": "#1A1A2E", "secondary": "#E2E8F0", "accent": "#8B5CF6"},
            "typography": "Plus Jakarta Sans + Inter",
            "personality": "minimale, sofisticato, elegante",
            "logo_concept": "Cerchio sfumato con effetto aurora boreale, tipografia sans-serif leggera",
        },
    },
    # ── Business (2) ────────────────────────────────────────────
    {
        "name": "Pragma — Corporate Suite",
        "slug": "pragma-corporate-suite",
        "category_slug": "business",
        "short_description": "Autorevolezza e solidità per aziende e consulenti. Sezione servizi, team, partnership e modulo contatto avanzato.",
        "description": (
            "Pragma trasmette professionalità e affidabilità dal primo scroll. "
            "Progettato per aziende consolidate, società di consulenza e imprese B2B che necessitano "
            "di una presenza online autorevole.\n\n"
            "Include: homepage corporate con video hero, pagina servizi con icone personalizzabili, "
            "sezione team con ruoli e contatti diretti, pagina partnership e clienti, "
            "area risorse con download PDF, modulo contatto multi-step."
        ),
        "price": Decimal("89.00"),
        "is_free": False,
        "featured": True,
        "order": 1,
        "brand": {
            "brand_name": "Pragma Corp",
            "tagline": "Soluzioni concrete per il tuo business",
            "palette": {"primary": "#1E293B", "secondary": "#3B82F6", "accent": "#10B981"},
            "typography": "Inter + Merriweather",
            "personality": "professionale, autorevole, affidabile",
            "logo_concept": "Monogramma P geometrico in navy e blu, linee nette che evocano struttura e solidità",
        },
    },
    {
        "name": "Elevate — Startup Landing",
        "slug": "elevate-startup-landing",
        "category_slug": "business",
        "short_description": "Landing page ad alta conversione per startup e SaaS. Hero potente, social proof e pricing table integrati.",
        "description": (
            "Elevate è progettato per startup, SaaS e aziende tech che necessitano di una landing page "
            "che converte. Design moderno con gradiente, animazioni di ingresso, "
            "sezione features con icone, pricing table comparativo e integrazione newsletter.\n\n"
            "Include: hero con CTA doppia, sezione benefici, features grid, "
            "testimonial carousel, pricing table a 3 colonne, FAQ accordion, footer CTA."
        ),
        "price": Decimal("59.00"),
        "is_free": False,
        "featured": False,
        "order": 2,
        "brand": {
            "brand_name": "Elevate Tech",
            "tagline": "Lancia il tuo prodotto con impatto",
            "palette": {"primary": "#0F172A", "secondary": "#7C3AED", "accent": "#22D3EE"},
            "typography": "Satoshi + Inter",
            "personality": "moderno, energico, tech-forward",
            "logo_concept": "Freccia ascendente stilizzata in gradiente viola-ciano, forme geometriche dinamiche",
        },
    },
    # ── Wave 2 Pilot #1 · Fiscus — Studio Tributario ───────────
    # Phase X.4 first pilot template. Reuses corporate-suite
    # archetype (shared shell with Pragma) but with
    # commercialista-specific voice, dashboard-light visual style,
    # warm-neutral palette (differs from Pragma's navy slate).
    # Seeds at tier=draft via TEMPLATE_REGISTRY.json; flipped to
    # published_live only after the Wave 2 reviewer acceptance walk.
    {
        "name": "Fiscus — Studio Tributario",
        "slug": "fiscus-commercialista",
        "category_slug": "business",
        "short_description": "Istituzionale e preciso per studi tributari e commercialisti. Calendario scadenze, iscrizioni albo, form appuntamento con P.IVA e CF.",
        "description": (
            "Fiscus è il template per studi tributari e commercialisti che vogliono comunicare "
            "competenza tecnica verificabile senza trovate grafiche. Voce formale-precisa, "
            "ritmo editoriale, palette warm-neutral con accento blu-notte — una presenza online "
            "che rassicura il decision-maker SMB che sta cercando un presidio, non un fornitore.\n\n"
            "Include: homepage con calendario scadenze del trimestre, pagina studio con bio "
            "albo-iscrizione dei partner, sei aree di competenza (dichiarazione, bilancio, "
            "contenzioso, wealth, lavoro, revisione), casistiche anonimizzate, form "
            "appuntamento con P.IVA/CF e fascia oraria, lead-magnet guida scadenze PDF."
        ),
        "price": Decimal("79.00"),
        "is_free": False,
        "featured": False,
        "order": 3,
        "brand": {
            "brand_name": "Fiscus — Studio Tributario",
            "tagline": "L'adempimento corretto, non la trovata",
            "palette": {"primary": "#1F2937", "secondary": "#B58F4A", "accent": "#1C3D5A"},
            "typography": "IBM Plex Serif + IBM Plex Sans",
            "personality": "preciso, istituzionale, continuativo",
            "logo_concept": "Monogramma F geometrico in serif transitional su fondo avorio, filetto oro sottile che richiama la filigrana dei documenti fiscali",
        },
    },
    # ── Wave 2 Pilot #2 · Solaria — Business Coaching ──────────
    # Phase X.4 second pilot template. Reuses corporate-suite
    # archetype (shared shell with Pragma + Fiscus) but with
    # coaching-specific voice — professional-warm, method-declared,
    # non-guru, non-therapy, non-consulting. Minimal-light visual
    # style, warm-earth accent palette (ocra + terra), humanist
    # typographic pair (Fraunces + Inter) distinct from Pragma
    # (Merriweather + Inter) and Fiscus (IBM Plex Serif + Sans).
    # Seeds at tier=draft via TEMPLATE_REGISTRY.json; flipped to
    # published_live only after Commit B (locales + Playwright).
    {
        "name": "Solaria — Business Coaching",
        "slug": "solaria-coaching",
        "category_slug": "business",
        "short_description": "Coaching professionale senza fuffa. Metodo dichiarato, percorso bounded, credenziali ICF verificabili, discovery call da 20-30 minuti gratuita.",
        "description": (
            "Solaria è il template per coach professionisti certificati (ICF, EMCC, AICP) che "
            "vogliono smarcarsi dalla fuffa-guru e dalla confusione con la consulenza classica. "
            "Voce professional-warm, palette minimal-light con accento warm-earth (ocra + terra), "
            "tipografia humanist (Fraunces + Inter) — per chi vende un percorso misurato, non "
            "una trasformazione in trenta giorni.\n\n"
            "Include: homepage con voice anchor coaching-non-è-terapia, pagina metodo con "
            "framework dichiarato (GROW, Co-Active, Immunity to Change) + codice deontologico "
            "ICF, bio coach con ore erogate + certificazione tier (ACC/PCC/MCC), 2-4 percorsi "
            "strutturati (executive, team, gruppo aziendale, sessione singola) con durata + "
            "frequenza + formato, 3 casi anonimizzati con contesto + obiettivo + percorso + "
            "risultato misurato, form discovery call con obiettivo in 1-2 righe e disponibilità "
            "prossimi 7 giorni."
        ),
        "price": Decimal("79.00"),
        "is_free": False,
        "featured": False,
        "order": 4,
        "brand": {
            "brand_name": "Solaria — Business Coaching",
            "tagline": "Metodo dichiarato, percorso misurato",
            # Palette follows corporate-suite skin convention:
            # primary = dark foreground text color (carbon)
            # secondary = main brand accent (warm-earth ocra)
            # accent = quieter secondary-accent (deep caramel)
            # Body background comes from the skin default (cream/neutral);
            # imagery pool + hero photo establish the warm-earth mood.
            # Pragma primary=#1E293B (dark slate), Fiscus primary=#1F2937
            # (dark gray), Solaria primary=#2B2A28 (warm dark carbon) —
            # all three are dark, but Solaria's tone sits warmer.
            # Build-time `corporate_suite.E001` enforces this polarity
            # contract on every enrolled corporate-suite primary.
            "palette": {"primary": "#2B2A28", "secondary": "#C8621A", "accent": "#8B5A2B"},
            "typography": "Fraunces + Inter",
            "personality": "professional-warm, metodico, misurato",
            "logo_concept": "Cerchio solare stilizzato in ocra scuro su fondo avorio-crema con lettera S disegnata come una curva aperta che richiama un percorso con inizio e fine dichiarati; tipografia humanist-serif Fraunces",
        },
    },
    # ── X.4 design-orchestrator pass 1 · Continua — Family-Office Stewardship ──
    # First real candidate produced by the design-orchestrator system
    # (`phase-x4-design-orchestrator-hardening-v1`, 2026-04-29). 4th
    # corporate-suite sibling · 1st family-office variant. Reuses the
    # corporate-suite shell (Pragma + Fiscus + Solaria) but with
    # stewardship-longitudinal voice, pine + pewter + brass palette
    # (matrix §1.3 cool-secondary + warm-accent · the only OPEN warmth
    # combo), Crimson Pro + Public Sans typography (closes the §1.4
    # cluster-collapse Inter risk), and an object-led hero with zero
    # people (the cluster's first). Seeds at tier=draft via
    # TEMPLATE_REGISTRY.json. IT-only at draft; multilingual rollout
    # via workflow C in a separate pass.
    {
        "name": "Continua — Family-Office Stewardship",
        "slug": "continua-stewardship",
        "category_slug": "business",
        "short_description": "Family office multigenerazionale per la custodia del patrimonio familiare attraverso le generazioni. Consiglio di Famiglia, audit di continuità annuale, patto familiare a revisione triennale.",
        "description": (
            "Continua è il template per famiglie imprenditoriali, holding di "
            "partecipazioni e fondazioni di famiglia che cercano un mandato "
            "di custodia su orizzonte multigenerazionale — non un advisory "
            "B2B trimestrale, non un commercialista presidio annuale, non "
            "un coaching bounded. Voce stewardship-longitudinal, palette "
            "deep pine + cool pewter + antique brass (la sola combinazione "
            "warm-accent ancora non occupata nel cluster corporate-suite), "
            "tipografia Crimson Pro + Public Sans (esplicitamente NOT Inter, "
            "chiude il rischio di terzo uso che collassa il cluster).\n\n"
            "Include: homepage con voice anchor «La continuità di una famiglia "
            "si misura in generazioni», 4 presidi (Custodia patrimoniale, "
            "Governance familiare, Successione strutturata, Compliance "
            "fiduciaria), KPI band scura (mandato medio · generazioni in "
            "carico · patrimonio in custodia · cadenza CdF), governance-cycle-strip "
            "che nomina una CADENZA non un numero o una scadenza, profili "
            "familiari come ribbon, Custodi del mandato (3 stewards 60s + "
            "40s + 50s photo-present con diversità anagrafica + di genere + "
            "di provenienza), 4 mandati in continuità con marker di durata "
            "pluriennale, form scope familiare + orizzonte temporale + "
            "struttura attuale (NO P.IVA + CF · NO NDA boardroom · NO ICF). "
            "Whistleblowing link prominente in legal row (D.lgs. 24/2023)."
        ),
        "price": Decimal("89.00"),
        "is_free": False,
        "featured": False,
        "order": 5,
        "brand": {
            "brand_name": "Continua — Family-Office Stewardship",
            "tagline": "Custodi del patrimonio familiare attraverso le generazioni",
            # Palette per the matrix §1.3 cool-secondary + warm-accent OPEN
            # combination · primary = deep pine (L* ≈ 21 · cream-safe),
            # secondary = cool pewter, accent = antique brass (the load-
            # bearing differentiator visible at ≥ 5 viewport touchpoints).
            "palette": {"primary": "#0F3A30", "secondary": "#5A6E78", "accent": "#B0875E"},
            "typography": "Crimson Pro + Public Sans",
            "personality": "custodial, longitudinale, multi-generazionale",
            "logo_concept": "Wordmark singolo «Continua» in Crimson Pro 500 con asta calligrafica dell'iniziale C che richiama il filetto di brass del navbar; preserva l'integrità Latin sotto RTL come da CS-NAV-06.",
        },
    },
    # ── Phase X.5 · Cornice — Studio di Architettura (2026-04-30) ──
    # 5th corporate-suite sibling · 1st architecture-firm variant ·
    # 1st LF-2 (Editorial Spread) occupant. Validates the layout-family
    # system (`factory/reports/hardening/corporate-suite-layout-divergence-
    # plan.md §10 Step 6`). Reuses the corporate-suite shell but with a
    # divergent home layout — stacked-editorial hero with KPI in photo
    # overlay, narrative essay with drop-cap replacing pillars, single-
    # portrait masthead, 3+1 magazine-grid cases, split-wordmark on
    # cream navbar, 4-col footer with whistleblowing column. Palette
    # graphite + pietra-serena + terracotta-rust (NEUTRAL/NEUTRAL/WARM).
    # Cormorant Garamond + Source Sans 3 (closes the §1.4 cluster-
    # collapse Inter risk). Seeds at `tier: draft` via
    # TEMPLATE_REGISTRY.json. IT-only at A.5 build (D-102 cadence).
    # ── Phase X.6 · Causa (6th corporate-suite sibling · 1st evidence-
    # led Cassazionista litigation-boutique variant · 2nd LF-2
    # occupant after Cornice). Reuses the corporate-suite shell +
    # LF-2 home dispatch identical to Cornice. Voice forensic-
    # publication · public-record register (NOT decisional-gravity
    # Pragma · NOT presidio-with-scadenze Fiscus · NOT bounded-
    # method Solaria · NOT stewardship-longitudinal Continua · NOT
    # curatorial-thesis Cornice). Palette bottle-green + bone +
    # obsidian (NEUTRAL/NEUTRAL/NEUTRAL on the warmth grid · third
    # polarity dimension matte-on-matte without metallic · explicitly
    # NOT graphite + pietra-serena + rust = Cornice claim). GT Sectra
    # + Manrope (Inter explicitly forbidden per CS-LAYOUT-20). Seeds
    # at `tier: draft` via TEMPLATE_REGISTRY.json. IT-only at A.5
    # build (D-102 cadence); multilingual rollout via workflow C in
    # a separate pass.
    {
        "name": "Causa — Studio Legale",
        "slug": "causa-legale",
        "category_slug": "business",
        "short_description": "Studio legale di patrocinio editoriale a Milano. Cassazionista fondatore, ventotto sentenze citate dal 1995, quattordici massime in massimario interno, contenzioso in tutti i gradi fino alla Cassazione.",
        "description": (
            "Causa è il template per studi legali italiani che "
            "trattano ogni causa come un'evidenza da incardinare — "
            "non come un servizio difensivo standardizzato. "
            "Progettato per studi single-principal Cassazionisti "
            "(un avvocato fondatore + due associati + segreteria), "
            "voce forensic-publication ed evidence-led, palette "
            "bottle-green + bone + obsidian (la sola polarità "
            "matte-on-matte con zero metallico ancora libera nel "
            "cluster corporate-suite), tipografia GT Sectra + "
            "Manrope (esplicitamente NOT Inter, chiude il rischio "
            "di terzo uso che collassa il cluster).\n\n"
            "Include: homepage editorial-spread con voice anchor "
            "«Ogni sentenza è un'evidenza incardinata, non "
            "un'opinione difesa», fotografia hero a tutta larghezza "
            "su aula di tribunale vuota con tuple di tre statistiche "
            "in overlay (28 sentenze citate · 14 voci in massimario "
            "· 31 anni di patrocinio), saggio metodologico di quattro "
            "paragrafi con drop-cap obsidian e tre pull-quote, "
            "ribbon di dodici materie del contenzioso (penale "
            "tributario, civile contrattualistica, amministrativo "
            "regolatorio, contenzioso bancario, responsabilità "
            "professionale, recupero crediti complesso, diritto "
            "societario, tributario, esecuzioni, lavoro complesso, "
            "CTU forense, ENCA mediation), masthead di leadership "
            "con singolo ritratto ambientale del Cassazionista "
            "fondatore e quattro credenziali Albo Avvocati Milano + "
            "Cassazionista + ENCA mediatori + Albo CTU forense, "
            "magazine-grid 3+1 di quattro decisioni rappresentative "
            "(Cass. SS.UU. responsabilità professionale 2024 · "
            "Cass. civ. III contenzioso bancario 2023 · TAR "
            "Lombardia AGCOM 2022 · App. Milano tributario 2021), "
            "parere preliminare come form di ingresso a 7 campi "
            "(oggetto · grado · controparte · valore · urgenza · "
            "evidenza · giurisdizione) — NO P.IVA + CF (collisione "
            "Fiscus evitata) · NO budget bracket (collisione "
            "Cornice evitata). Whistleblowing come colonna di "
            "footer (D.lgs. 24/2023). Navbar split-wordmark "
            "masthead 'CAUSA / studio legale'."
        ),
        "price": Decimal("89.00"),
        "is_free": False,
        "featured": False,
        "order": 7,
        "brand": {
            "brand_name": "Causa — Studio Legale",
            "tagline": "Studio legale di patrocinio editoriale · Cassazionista fondatore · Milano dal 1995",
            # Palette · NEUTRAL/NEUTRAL/NEUTRAL on the warmth grid
            # (full cool · matte-on-matte · zero metallic). primary
            # = bottle-green (L* ≤ 40 on cream · is_primary_safe_on_
            # cream PASS · ≥6 ΔE distance from Continua pine
            # `#0F3A30`), secondary = bone (warmer than Cornice
            # pietra-serena `#cdc9c0` · cooler than Fiscus warm-
            # neutral cream), accent = obsidian (deep neutral · zero
            # metallic · body-typographic-only deployment surface
            # · explicitly not chrome-metallic like Continua's
            # brass). Third polarity dimension per `corporate-suite-
            # distinctness-matrix.md §1.3` ("matte-on-matte without
            # metallic").
            "palette": {"primary": "#14342B", "secondary": "#F0EBE0", "accent": "#0B0A0E"},
            "typography": "GT Sectra + Manrope",
            "personality": "forensic, evidence-led, public-record",
            "logo_concept": "Wordmark split-line masthead «CAUSA / studio legale» — line 1 GT Sectra uppercase letter-spacing 0.18em bottle-green ink, line 2 Manrope lowercase ink-soft. Reads come una testata di pubblicazione forense (Foro Italiano · Giurisprudenza Italiana), non come un brand corporativo. Preserva l'integrità Latin sotto RTL come da CS-NAV-06.",
        },
    },
    {
        "name": "Cornice — Studio di Architettura",
        "slug": "cornice-architettura",
        "category_slug": "business",
        "short_description": "Studio di architettura editoriale a Milano. Fascicolo monografico per ogni progetto, qualifica MIBAC restauro, committenze pubbliche e private dal 2008.",
        "description": (
            "Cornice è il template per studi di architettura italiani che "
            "trattano ogni commissione come un argomento da costruire — "
            "non come un servizio standardizzato. Progettato per studi "
            "single-principal (un architetto fondatore + collaboratori), "
            "voce editoriale-curatoriale, palette graphite + pietra-serena "
            "+ terracotta-rust (la sola combinazione NEUTRAL/NEUTRAL/WARM "
            "ancora libera nel cluster corporate-suite), tipografia "
            "Cormorant Garamond + Source Sans 3 (esplicitamente NOT "
            "Inter, chiude il rischio di terzo uso che collassa il "
            "cluster).\n\n"
            "Include: homepage editorial-spread con voice anchor «Ogni "
            "progetto è un argomento costruito», fotografia hero a tutta "
            "larghezza con tuple di tre statistiche in overlay, saggio "
            "editoriale di quattro paragrafi con drop-cap e tre pull-quote, "
            "ribbon di dodici tipologie d'intervento (residenziale, "
            "pubblico, interno, paesaggio, restauro, concorso, culturale, "
            "uffici, industriale, sanitario, scolastico, misto-uso), "
            "masthead di leadership con singolo ritratto ambientale "
            "dell'architetto fondatore e quattro credenziali Albo "
            "OAPPC/CNAPPC/MIBAC, magazine-grid 3+1 di quattro fascicoli "
            "rappresentativi (concorso pubblico vinto · edificio "
            "residenziale · restauro pubblico · saggio in collana), "
            "fascicolo progetto come form di ingresso (sito · tipologia "
            "· cronoprogramma · documenti) — NO P.IVA + CF (collisione "
            "Fiscus evitata). Whistleblowing come colonna di footer "
            "(D.lgs. 24/2023). Navbar split-wordmark masthead 'CORNICE / "
            "studio di architettura'."
        ),
        "price": Decimal("89.00"),
        "is_free": False,
        "featured": False,
        "order": 6,
        "brand": {
            "brand_name": "Cornice — Studio di Architettura",
            "tagline": "Architettura editoriale · committenze pubbliche e private · Milano dal 2008",
            # Palette · NEUTRAL/NEUTRAL/WARM (the only un-claimed cluster
            # polarity per `intake.md §3.1`). primary = graphite (L* ≈ 12
            # · cream-safe), secondary = pietra-serena (drafting-paper
            # stone), accent = terracotta-rust (the load-bearing
            # differentiator on display-typographic surfaces — explicitly
            # not chrome-only like Continua's brass). Hex distance from
            # every existing sibling palette > 0/3 cells on warmth grid.
            "palette": {"primary": "#1F2226", "secondary": "#C7BFB1", "accent": "#B7491F"},
            "typography": "Cormorant Garamond + Source Sans 3",
            "personality": "editoriale, curatoriale, autoriale",
            "logo_concept": "Wordmark split-line masthead «CORNICE / studio di architettura» — line 1 Cormorant Garamond uppercase letter-spacing 0.18em, line 2 Source Sans 3 lowercase. Reads come una testata di pubblicazione (Casabella · Domus), non come un brand corporativo. Preserva l'integrità Latin sotto RTL come da CS-NAV-06.",
        },
    },
    # ── Ristorante (2) ─────────────────────────────────────────
    {
        "name": "Gusto — Fine Dining",
        "slug": "gusto-fine-dining",
        "category_slug": "restaurant",
        "short_description": "Eleganza e calore per ristoranti raffinati. Menu digitale, prenotazione tavoli e galleria fotografica immersiva.",
        "description": (
            "Gusto cattura l'essenza della ristorazione italiana d'eccellenza. "
            "Fotografia hero a schermo pieno, menu digitale con categorie e allergeni, "
            "sistema di prenotazione tavoli integrato, galleria con lightbox per gli ambienti.\n\n"
            "Include: homepage con slideshow, menu digitale interattivo, "
            "sezione chef con filosofia culinaria, galleria ambienti, "
            "widget prenotazione, pagina eventi privati, mappa con indicazioni."
        ),
        "price": Decimal("59.00"),
        "is_free": False,
        "featured": True,
        "order": 1,
        "brand": {
            "brand_name": "Osteria Moderna",
            "tagline": "Tradizione e innovazione a tavola",
            "palette": {"primary": "#2C1810", "secondary": "#D4A574", "accent": "#8B0000"},
            "typography": "Playfair Display + Lato",
            "personality": "caldo, elegante, autentico",
            "logo_concept": "Forchetta e foglia d'ulivo intrecciate in oro su fondo scuro, tipografia serif elegante",
        },
    },
    {
        "name": "Sapore — Trattoria & Pizzeria",
        "slug": "sapore-trattoria-pizzeria",
        "category_slug": "restaurant",
        "short_description": "Caloroso e accogliente per trattorie e pizzerie. Menu con foto, ordini online e recensioni Google integrate.",
        "description": (
            "Sapore è il template perfetto per trattorie, pizzerie e ristoranti informali "
            "che vogliono un sito web invitante e funzionale. "
            "Design caloroso con palette terrosa, menu fotografico, "
            "pulsante ordini online e widget recensioni.\n\n"
            "Include: homepage con hero e piatto del giorno, menu con foto e prezzi, "
            "sezione a domicilio con CTA, galleria Instagram, "
            "recensioni Google/TripAdvisor embed, mappa e orari."
        ),
        "price": Decimal("49.00"),
        "is_free": False,
        "featured": False,
        "order": 2,
        "brand": {
            "brand_name": "Trattoria Da Nonna Rosa",
            "tagline": "Il sapore di casa, dal 1987",
            "palette": {"primary": "#4A2C2A", "secondary": "#E8D5B7", "accent": "#C0392B"},
            "typography": "Libre Baskerville + Source Sans 3",
            "personality": "caloroso, familiare, genuino",
            "logo_concept": "Spiga di grano e mattarello in stile illustrato, colori caldi su fondo crema",
        },
    },
    {
        "name": "Brace — Street Food Lab",
        "slug": "brace-street-food-lab",
        "category_slug": "restaurant",
        "short_description": "Bold e brutalista per smashburger, pizza al taglio e street food d'autore. Product hero, griglia ordini e integrazione delivery.",
        "description": (
            "Brace è il template per format urbani di street food, smashburger lab e pizzerie "
            "al taglio che vogliono comunicare energia, ritmo e qualità senza i fronzoli del fine "
            "dining. Display type compresso, palette black-on-yellow, gerarchie brutaliste, e una "
            "product grid pensata per convertire al primo scroll.\n\n"
            "Include: hero a tutta pagina con product cutout e badge prezzo, menu griglia 4-up "
            "con descrizione e CTA aggiungi, integrazione partner delivery (Glovo, Deliveroo, "
            "Just Eat, Uber Eats), strip 'coda al banco' in tempo reale, mappa con orari estesi, "
            "sezione lavora con noi e store dedicato a sughi e merchandising."
        ),
        "price": Decimal("65.00"),
        "is_free": False,
        "featured": False,
        "order": 3,
        "brand": {
            "brand_name": "Brace Street Lab",
            "tagline": "Bruciato al fuoco vivo, servito al volo",
            "palette": {"primary": "#0F0F0F", "secondary": "#FFE600", "accent": "#FF3D00"},
            "typography": "Big Shoulders Display + Inter",
            "personality": "audace, brutalista, urbano, rapido",
            "logo_concept": "Lettera B incisa con ombra di fiamma stilizzata in giallo elettrico su fondo nero, font Anton condensato",
        },
    },
    # ── Medico (2) ──────────────────────────────────────────────
    {
        "name": "Salute — Studio Medico",
        "slug": "salute-studio-medico",
        "category_slug": "medical",
        "short_description": "Rassicurante e professionale per studi medici. Prenotazione online, profili dottori e area paziente dedicata.",
        "description": (
            "Salute comunica competenza e fiducia fin dal primo impatto. "
            "Progettato per studi medici, poliambulatori e cliniche private "
            "che necessitano di una presenza online professionale e rassicurante.\n\n"
            "Include: homepage con servizi e team medico, sistema prenotazione visite, "
            "profili dottori con specializzazioni e CV, area paziente con documentazione, "
            "sezione convenzioni e assicurazioni, blog salute con categorie, modulo contatti urgenti."
        ),
        "price": Decimal("69.00"),
        "is_free": False,
        "featured": True,
        "order": 1,
        "brand": {
            "brand_name": "SaluteVita Clinic",
            "tagline": "La tua salute, la nostra missione",
            "palette": {"primary": "#0B4F6C", "secondary": "#01BAEF", "accent": "#20BF55"},
            "typography": "Nunito Sans + Inter",
            "personality": "rassicurante, professionale, moderno",
            "logo_concept": "Croce medica stilizzata con cuore integrato in blu-verde, forme morbide e accoglienti",
        },
    },
    {
        "name": "Benessere — Centro Olistico",
        "slug": "benessere-centro-olistico",
        "category_slug": "medical",
        "short_description": "Sereno e armonioso per centri benessere e studi olistici. Prenotazione trattamenti e sezione blog integrata.",
        "description": (
            "Benessere trasmette serenità e armonia, perfetto per centri wellness, "
            "studi di fisioterapia, osteopatia e pratiche olistiche.\n\n"
            "Include: homepage con atmosfera rilassante, catalogo trattamenti con prezzi, "
            "calendario prenotazioni, profili terapisti, sezione testimonianze pazienti, "
            "blog benessere con consigli, galleria ambienti."
        ),
        "price": Decimal("59.00"),
        "is_free": False,
        "featured": False,
        "order": 2,
        "brand": {
            "brand_name": "Studio Armonia",
            "tagline": "Equilibrio tra corpo e mente",
            "palette": {"primary": "#2D4A3E", "secondary": "#A7C4BC", "accent": "#D4A574"},
            "typography": "Cormorant Garamond + Nunito",
            "personality": "sereno, naturale, accogliente",
            "logo_concept": "Foglia e goccia d'acqua in verde salvia, linee organiche e fluide",
        },
    },
    {
        "name": "Famiglia — Studio Pediatrico",
        "slug": "famiglia-pediatria",
        "category_slug": "medical",
        "short_description": "Caldo e accogliente per studi pediatrici e medicina di famiglia. Profili medici, orari e contatto WhatsApp diretto.",
        "description": (
            "Famiglia è il template per pediatri, medici di famiglia e piccole cliniche di quartiere "
            "che vogliono trasmettere fiducia e calore umano fin dal primo scroll. Palette pastello, "
            "layout arioso, fotografie di sguardi vicini.\n\n"
            "Include: homepage con presentazione dello studio e medici, sezione fasce d'età "
            "(neonato/bambino/adolescente), profili pediatri con bio breve, orari di apertura "
            "stile tabella, mappa con indicazioni, modulo WhatsApp diretto, blog consigli ai genitori."
        ),
        "price": Decimal("65.00"),
        "is_free": False,
        "featured": False,
        "order": 3,
        "brand": {
            "brand_name": "Pediatria Famiglia Plus",
            "tagline": "Cresciamo insieme ai vostri bambini",
            "palette": {"primary": "#4A2E2A", "secondary": "#FBD9B5", "accent": "#E97B5C"},
            "typography": "Quicksand + Nunito",
            "personality": "caldo, familiare, rassicurante",
            "logo_concept": "Volpina stilizzata con cuore al posto del muso, palette pastello terracotta",
        },
    },
    {
        "name": "Cardio — Studio Specialistico",
        "slug": "cardio-studio-specialistico",
        "category_slug": "medical",
        "short_description": "Editoriale e prestigioso per cardiologi e specialisti privati. Layout magazine, drop cap e pubblicazioni.",
        "description": (
            "Cardio è il template per specialisti di alto livello che operano in regime privato — "
            "cardiologi, dermatologi, neurologi — e che vogliono comunicare expertise e discrezione. "
            "Layout editoriale ispirato alle riviste di medicina, tipografia serif imponente, "
            "palette sobria con un solo accento.\n\n"
            "Include: homepage con headline editoriale e ritratto del medico, paragrafo con drop cap, "
            "sezione visite numerata 01/02, banda pubblicazioni e media, modulo richiesta visita "
            "privata, pagina CV scientifico, area pazienti riservata."
        ),
        "price": Decimal("109.00"),
        "is_free": False,
        "featured": False,
        "order": 4,
        "brand": {
            "brand_name": "Studio Marani Cardiologia",
            "tagline": "Cardiologia clinica e secondi pareri",
            "palette": {"primary": "#1c1612", "secondary": "#f7f3ee", "accent": "#9c2a2a"},
            "typography": "Cormorant Garamond + Inter",
            "personality": "editoriale, prestigioso, sobrio",
            "logo_concept": "Iniziali M+C in serif maiuscolo con linea sottile sotto, oro su fondo carta",
        },
    },
    {
        "name": "Dermatologia Elite — Studio Ricciardi",
        "slug": "dermatologia-elite-roma",
        "category_slug": "medical",
        "short_description": "Editoriale e prestigioso per dermatologi privati. Mappa nei digitale, chirurgia dermatologica, estetica clinica.",
        "description": (
            "Dermatologia Elite riutilizza la chrome editoriale dell'archetipo Specialist con "
            "contenuto dedicato agli studi dermatologici di altissimo profilo. Accento botanico "
            "forest-green al posto del rosso clinico, tipografia Bodoni Moda al posto di Cormorant "
            "per una sensazione di editoriale estetico-medico.\n\n"
            "Include: homepage con headline sulla 'carta d'identità' della pelle, fact-band "
            "18 anni / 2.400 mappature / 3 sale, manifesto con drop cap, quattro percorsi clinici "
            "numerati (mappa nei / chirurgia / laser / estetica), pagina Lo Studio con timeline "
            "2008→2024, Visite con sei tariffe dettagliate, Medici con tre dermatologhe, cinque "
            "pubblicazioni (di cui una con articolo integrale), Contatti con orari doppia fascia "
            "e Richiedi visita con processo in quattro step."
        ),
        "price": Decimal("115.00"),
        "is_free": False,
        "featured": False,
        "order": 5,
        "brand": {
            "brand_name": "Studio Ricciardi Dermatologia",
            "tagline": "Dermatologia clinica, chirurgica ed estetica · Roma Veneto",
            "palette": {"primary": "#1c1612", "secondary": "#f7f3ee", "accent": "#3d5437"},
            "typography": "Bodoni Moda + Inter",
            "personality": "editoriale, meticoloso, estetico-clinico",
            "logo_concept": "Monogramma R in serif maiuscolo con linea sottile sotto, verde-bosco su fondo carta",
        },
    },
    # Wave 1 Pass-1 (T45 · 2026-05-11) · 3rd template on the `specialist`
    # archetype (zero new HTML · D-051 Option A reuse pattern). Activates
    # the `dental` cluster for the first time (was 0 templates). Price
    # tier `standard` (€ 75) vs Cardio + Derm `premium` — broader audience
    # reach. Seeds at tier=draft via TEMPLATE_REGISTRY.json — IT-only at
    # T45 build (D-102 cadence); EN/FR/ES/AR + public flip via T46.
    {
        "name": "Denti+Co — Studio Dentistico",
        "slug": "denti-co-studio",
        "category_slug": "medical",
        "short_description": "Editoriale e clinico per studi dentistici associati. Igiene, conservativa, implantologia e ortodonzia trasparente · Milano Brera.",
        "description": (
            "Denti+Co riutilizza l'archetipo editoriale Specialist con identità dedicata "
            "agli studi dentistici associati di profilo premium. Palette deep-blue clinico "
            "con accento fresh-mint (terza polarità del cluster · NON rosso NON verde), "
            "tipografia DM Serif Display + Inter per una sensazione editoriale ma "
            "distintamente clinica.\n\n"
            "Include: homepage con headline incentrata sull'igiene come primo capitolo, "
            "manifesto con drop cap, quattro trattamenti numerati (igiene / conservativa / "
            "implantologia / ortodonzia trasparente), listino dettagliato con quattro tab, "
            "percorso paziente in cinque step, direzione clinica con ritratto editoriale, "
            "FAQ dental-specific, pagina trattamenti con costi dichiarati, pagina dentisti "
            "con quattro associati, pubblicazioni divulgative, contatti Milano Brera, "
            "modulo prenotazione igiene con cinque slot."
        ),
        "price": Decimal("75.00"),
        "is_free": False,
        "featured": False,
        "order": 6,
        "brand": {
            "brand_name": "Denti+Co Studio Dentistico Associato",
            "tagline": "Salute orale completa, dall'igiene all'implantologia",
            "palette": {"primary": "#0F2D40", "secondary": "#F7F3EE", "accent": "#2BC4A4"},
            "typography": "DM Serif Display + Inter",
            "personality": "editoriale, clinico-bright, premium-accessibile",
            "logo_concept": "Wordmark «Denti+Co» con + in fresh-mint #2BC4A4 e indicatore sottile sotto · DM Serif Display per il marchio, Inter mono-spaziato per il claim · pulizia clinica con un solo accento non clinico-rosso non clinico-verde.",
        },
    },
    # ── Avvocato (2) ────────────────────────────────────────────
    {
        "name": "Lex — Studio Legale",
        "slug": "lex-studio-legale",
        "category_slug": "lawyer",
        "short_description": "Autorevole e rassicurante per studi legali. Aree di pratica, profili avvocati, consulenza online e blog giuridico.",
        "description": (
            "Lex è il template per studi legali che vogliono trasmettere esperienza e affidabilità. "
            "Design sobrio e autorevole con palette scura e accenti oro.\n\n"
            "Include: homepage con aree di pratica in evidenza, profili avvocati con CV e specializzazioni, "
            "sezione risultati e casi di successo, form richiesta consulenza online, "
            "blog giuridico con categorie per area di diritto, pagina contatti con mappa sedi."
        ),
        "price": Decimal("69.00"),
        "is_free": False,
        "featured": True,
        "order": 1,
        "brand": {
            "brand_name": "Studio Legale Ferri",
            "tagline": "Competenza e dedizione al servizio della giustizia",
            "palette": {"primary": "#1A1A2E", "secondary": "#C5A55A", "accent": "#8B0000"},
            "typography": "Cormorant Garamond + Inter",
            "personality": "autorevole, classico, sobrio",
            "logo_concept": "Bilancia della giustizia stilizzata in oro su fondo navy, tipografia serif classica",
        },
    },
    {
        "name": "Juris — Avvocato Moderno",
        "slug": "juris-avvocato-moderno",
        "category_slug": "lawyer",
        "short_description": "Design contemporaneo per avvocati e professionisti legali. Prenotazione consulenze e area clienti riservata.",
        "description": (
            "Juris offre un approccio moderno alla comunicazione legale. "
            "Design pulito e accessibile che rompe con l'immagine tradizionale dello studio legale.\n\n"
            "Include: homepage con servizi e CTA prenotazione, sezione aree di pratica con dettaglio, "
            "sistema prenotazione consulenza online, area clienti riservata con documenti, "
            "FAQ giuridiche, blog con articoli e guide, profilo avvocato dettagliato."
        ),
        "price": Decimal("59.00"),
        "is_free": False,
        "featured": False,
        "order": 2,
        "brand": {
            "brand_name": "Avv. Martini & Partners",
            "tagline": "Il diritto dalla tua parte",
            "palette": {"primary": "#2D3748", "secondary": "#4299E1", "accent": "#ECC94B"},
            "typography": "DM Sans + Inter",
            "personality": "moderno, accessibile, trasparente",
            "logo_concept": "Lettera M con colonne stilizzate, blu e grigio ardesia, design contemporaneo",
        },
    },
    # T47 · Wave 1 Pass-3 (2026-05-12) · 1st classic-gold archetype reuse
    # after Lex (zero new HTML · D-051 Option A reuse pattern). Activates
    # the `notary-commercialista` cluster for the first time (was 0
    # templates). Premium tier (€ 89). Seeds at tier=draft via
    # TEMPLATE_REGISTRY.json — IT-only at T47 build (D-102 cadence);
    # multilingual + public flip via a separate T48 pass if cadence holds.
    {
        "name": "Atto — Studio Notarile Associato",
        "slug": "atto-notai-associati",
        "category_slug": "lawyer",
        "short_description": "Istituzionale e procedurale-chiaro per studi notarili associati. Rogiti, successioni, atti societari, mutui · Milano Distretto Notarile.",
        "description": (
            "Atto riutilizza l'archetipo classic-gold con identità istituzionale "
            "dedicata agli studi notarili associati. Palette ink-blue d'archivio "
            "con accento granata di sigillo (terza polarità del cluster lawyer · "
            "vs Lex gold prestige · vs Juris blue advisory), tipografia Source "
            "Serif 4 + Public Sans per una sensazione di pubblicazione forense "
            "istituzionale.\n\n"
            "Include: homepage con headline incentrata sull'atto pubblico, "
            "meta-strip notarile (sede unica, notai associati, lingue di rogito), "
            "sette tipologie d'atto numerate (rogiti / successioni / società / "
            "mutui / donazioni / procure / autentiche), banda Distretto Notarile, "
            "portrait dei tre notai associati con anno iscrizione al ruolo e "
            "specializzazione, pubblicazioni notarili istituzionali, pagina "
            "Lo Studio con timeline 2007-2025, Aree di Atti con dettaglio per "
            "tipologia, I Notai con bio e iscrizione, modulo Richiedi un primo "
            "incontro (orientativo · gratuito · non vincolante)."
        ),
        "price": Decimal("89.00"),
        "is_free": False,
        "featured": False,
        "order": 3,
        "brand": {
            "brand_name": "Studio Notarile Conti–Sironi–Verri",
            "tagline": "Atti pubblici redatti con la cura che la legge richiede · Distretto Notarile di Milano",
            "palette": {"primary": "#0F1A2A", "secondary": "#F1ECE4", "accent": "#1F3A5F"},
            "typography": "Source Serif 4 + Public Sans",
            "personality": "istituzionale, procedurale-chiaro, sobrio",
            "logo_concept": "Wordmark «CSV» monogramma in Source Serif 4 small-caps su sfondo carta-archivio · sigillo notarile minimo in accent ink-blue · niente bilance né colonne né simboli avvocatura.",
        },
    },
    # T49 · Wave 1 Pass-5 (2026-05-12) · 1st fine-dining archetype reuse
    # after Gusto (D-051 Option A: zero new HTML files). Activates the
    # `bakery-pasticceria` cluster for the first time (was 0 templates).
    # Premium tier (€ 75). Seeds at tier=draft via TEMPLATE_REGISTRY.json —
    # IT-only at T49 build (D-102 cadence); multilingual EN/FR/ES/AR +
    # AAA walk + public flip happen in T50.
    {
        "name": "Madou — Pasticceria Atelier",
        "slug": "madou-pasticceria",
        "category_slug": "restaurant",
        "short_description": "Pasticceria artigianale ad alta gamma · sfoglie laminate, lieviti madre, cake design su commessa · Torino Borgo Po.",
        "description": (
            "Madou riutilizza l'archetipo fine-dining con identità "
            "pasticcera-atelier dedicata alle pasticcerie d'alta gamma. "
            "Palette cacao-deep + crema-zucchero-a-velo + caramello "
            "(seconda polarità dell'archetipo fine-dining · vs Gusto "
            "coffee-amber-blood-red), tipografia Playfair Display + Lato "
            "ereditata dall'archetipo per coerenza editoriale ma usata "
            "con respiro pasticcero anziché ristorante.\n\n"
            "Include: homepage con headline incentrata sulla lievitazione "
            "lenta, meta-strip pasticceria (atelier, lieviti madre vivi, "
            "filiera tracciabile), cinque lievitati signature della "
            "settimana (croissant viennoise, maritozzo, millefoglie alla "
            "nocciola, bignè cioccolato Domori, Saint Honoré ai marroni), "
            "banda di otto referenze di pasticceria stagionale, archivio "
            "dei tre lieviti madre vivi (M-1 sfoglia, M-2 panettoni, M-3 "
            "brioche), eventi su misura (torta su commessa, wedding cake, "
            "buffet privato), pagina Il Forno con timeline 2011-2025, "
            "Pasticceria con dettaglio per lievitato e abbinamento "
            "caffetteria/tisaneria, Vetrina con quindici metri di "
            "esposizione lineare e quattro sale, modulo Pre-ordina la "
            "sfoglia del sabato (ritiro al banco entro le 13:00)."
        ),
        "price": Decimal("75.00"),
        "is_free": False,
        "featured": False,
        "order": 4,
        "brand": {
            "brand_name": "Madou · Pasticceria Atelier",
            "tagline": "Dodici ore di lievitazione lenta · Torino Borgo Po · dal 2011",
            "palette": {"primary": "#3D2817", "secondary": "#F4E8D0", "accent": "#C8965C"},
            "typography": "Playfair Display + Lato",
            "personality": "artigianale, pacato, ossessivo sul tempo",
            "logo_concept": "Wordmark «MD» monogramma serif piccolo in caramello su carta-zucchero-a-velo · niente forchette né piatti né stelle Michelin · estetica di pasticceria d'atelier, non di ristorante.",
        },
    },
    # T51 · Wave 1 Pass-7 (2026-05-12) · 4th specialist archetype reuse
    # after Cardio + Derm + Denti (D-051 Option A: zero new HTML files).
    # Activates the `veterinary` cluster for the first time (was 0
    # templates). Standard tier (€ 75 · same band as Denti). Seeds at
    # tier=draft via TEMPLATE_REGISTRY.json — IT-only at T51 build
    # (D-102 cadence); multilingual EN/FR/ES/AR + AAA walk + public
    # flip via T52.
    {
        "name": "Petro — Studio Veterinario",
        "slug": "petro-veterinario",
        "category_slug": "medical",
        "short_description": "Studio veterinario indipendente premium · medicina preventiva cane/gatto/esotici · chirurgia tessuti molli e diagnostica per immagini · Padova Borgo Trento.",
        "description": (
            "Petro riutilizza l'archetipo specialist con identità "
            "veterinaria dedicata alla medicina di piccoli animali. "
            "Palette ink + crema-paper + accento bronzo-tabacco "
            "(quarta polarità del cluster specialist · vs Cardio "
            "rosso clinico · Derm verde-bosco · Denti blu-menta), "
            "tipografia Lora + Inter (humanist book serif veterinary-"
            "textbook register vs Cormorant Cardio · Bodoni Derm · "
            "DM Serif Display Denti).\n\n"
            "Include: homepage con headline incentrata sulla cura "
            "preventiva veterinaria, meta-strip clinica (sede, "
            "iscrizione Albo, animali curati/anno), quattro famiglie "
            "di intervento numerate (preventiva / vaccinazioni / "
            "chirurgia tessuti molli / diagnostica), tabs trattamenti "
            "con listino voci di routine, banda Università di Padova "
            "+ convenzione Ospedale Veterinario Legnaro, portrait dei "
            "tre veterinari associati (Marco Petro direttore + Anna "
            "Bressan esotici + Tommaso Zen oncologia), diario clinico "
            "con due post (calendario vaccinale 2026 + sterilizzazione "
            "laparoscopica), pagina Studio con timeline 2008-2023, "
            "Visite con dettaglio per famiglia, I Veterinari con bio "
            "completi, modulo Prenota una visita preventiva con "
            "campi specie/razza/età/motivo della visita."
        ),
        "price": Decimal("75.00"),
        "is_free": False,
        "featured": False,
        "order": 5,
        "brand": {
            "brand_name": "Studio Veterinario Petro",
            "tagline": "Cura preventiva per cane gatto esotici · Padova Borgo Trento · dal 2008",
            "palette": {"primary": "#1C1612", "secondary": "#F7F3EE", "accent": "#A86E3C"},
            "typography": "Lora + Inter",
            "personality": "scrupoloso, paziente, scientifico-affidabile",
            "logo_concept": "Wordmark «P» serif Lora maiuscoletto · niente icone di cane o gatto · estetica di studio veterinario clinico premium, non di clinica catena.",
        },
    },
    # ── Immobiliare (2) ─────────────────────────────────────────
    {
        "name": "Casa — Agenzia Immobiliare",
        "slug": "casa-agenzia-immobiliare",
        "category_slug": "real-estate",
        "short_description": "Aspirazionale e funzionale per agenzie immobiliari. Ricerca immobili, schede proprietà e tour virtuali.",
        "description": (
            "Casa è il template per agenzie immobiliari che vogliono presentare il proprio portfolio "
            "con eleganza e funzionalità. Design aspirazionale con fotografie grandi e filtri di ricerca.\n\n"
            "Include: homepage con immobili in evidenza e ricerca rapida, griglia annunci filtrabile "
            "per zona/prezzo/tipologia, scheda proprietà con galleria e planimetria, "
            "pagina agenti con contatto diretto, sezione valutazione immobili, blog immobiliare."
        ),
        "price": Decimal("79.00"),
        "is_free": False,
        "featured": False,
        "order": 1,
        "brand": {
            "brand_name": "Domus Immobiliare",
            "tagline": "La casa dei tuoi sogni ti aspetta",
            "palette": {"primary": "#1B2838", "secondary": "#2ECC71", "accent": "#E67E22"},
            "typography": "Poppins + Inter",
            "personality": "aspirazionale, affidabile, elegante",
            "logo_concept": "Tetto stilizzato con chiave integrata in verde su fondo scuro, forme geometriche moderne",
        },
    },
    {
        "name": "Villa — Immobili di Lusso",
        "slug": "villa-immobili-lusso",
        "category_slug": "real-estate",
        "short_description": "Esclusivo per immobili di pregio. Gallerie immersive, tour 360° e presentazione proprietà cinematografica.",
        "description": (
            "Villa è il template per agenzie specializzate in immobili di pregio e lusso. "
            "Ogni pixel trasmette esclusività e attenzione al dettaglio.\n\n"
            "Include: homepage con video hero e proprietà in evidenza, schede immobili con galleria fullscreen, "
            "integrazione tour 360°, sezione quartiere con mappa interattiva, "
            "form richiesta visita privata, area agenti esclusivi."
        ),
        "price": Decimal("99.00"),
        "is_free": False,
        "featured": False,
        "order": 2,
        "brand": {
            "brand_name": "Villa Prestige",
            "tagline": "L'eccellenza nell'immobiliare di lusso",
            "palette": {"primary": "#0A0A0A", "secondary": "#C9A96E", "accent": "#FFFFFF"},
            "typography": "Cormorant Garamond + Montserrat",
            "personality": "lussuoso, esclusivo, cinematografico",
            "logo_concept": "Monogramma VP in oro su nero, serif elegante con spaziatura ampia",
        },
    },
    # ── Travel (1) ──────────────────────────────────────────────
    # T56 · Wave 2 Pass-1 (2026-05-12) · 1st reuse of ultra-luxury-cinematic
    # archetype after Villa (D-051 Option A: zero new HTML files). Opens
    # the `travel` category (was 0 templates) and `boutique-hotel` cluster.
    # Premium tier (€ 99 · enoteca-hotel premium band same as Villa).
    # Seeds at tier=draft via TEMPLATE_REGISTRY.json — IT-only at T56
    # build (D-102 cadence) · multilingual EN/FR/ES/AR + AAA walk +
    # public flip via T57.
    {
        "name": "Borgo San Marco — Relais & Spa",
        "slug": "albergo-borgo",
        "category_slug": "travel",
        "short_description": "Relais affiliato Relais & Châteaux in un borgo del Seicento · Val d'Orcia UNESCO · otto suite · brigata di 14 · ospitalità di borgo.",
        "description": (
            "Borgo San Marco riusa l'archetipo ultra-luxury-cinematic con "
            "identità di relais boutique in un borgo toscano del Seicento. "
            "Palette terracotta + travertino crema + olivo (seconda polarità "
            "dell'archetipo · vs Villa nero + champagne + bianco), tipografia "
            "Cormorant Garamond + Inter (display serif Italian-editorial vs "
            "Montserrat sans di Villa).\n\n"
            "Include: homepage con hero cinematografico sul cortile + 6 suite "
            "in evidenza con dossier editoriale, pagina Le suite con catalogo "
            "filtrato per vista/letti/stagione di 8 stanze, pagina Il territorio "
            "con 6 territori della Val d'Orcia (Pienza Brunello Bagno-Vignoni "
            "Montepulciano Monte-Amiata Val-d'Orcia UNESCO), pagina La brigata "
            "con direttrice Vittoria Sernigi + maitre Federico Bonechi + chef "
            "stellato Tommaso Brigliadori + sommelier Anna Ricci + responsabile "
            "spa Caterina Sandri, pagina Soggiorno con 5 tempi dell'esperienza "
            "e 6 FAQ ricorrenti, pagina Concierge con form prenotazione 10 "
            "campi + 3 sedi (ricevimento · cantina · spa)."
        ),
        "price": Decimal("99.00"),
        "is_free": False,
        "featured": False,
        "order": 1,
        "brand": {
            "brand_name": "Borgo San Marco · Relais & Spa",
            "tagline": "Otto suite in un borgo seicentesco · Val d'Orcia UNESCO · Pienza dal 1612",
            "palette": {"primary": "#653025", "secondary": "#EAE0CE", "accent": "#5B6A3D"},
            "typography": "Cormorant Garamond + Inter",
            "personality": "editoriale, ospitale, stagionale, di brigata",
            "logo_concept": "Wordmark «Borgo San Marco» in Cormorant Garamond italic con piccolo monogramma «BSM» dentro un riquadro in terracotta · niente cipresso stilizzato né cupola · estetica di canonica seicentesca restaurata, non di resort né di hotel di catena.",
        },
    },
    # T59 · Wave 2 Pass-3 (2026-05-13) · 3rd reuse of artisan-workshop
    # archetype after Bottega + Sapori (D-051 Option A · zero new HTML
    # files). 2nd cross-category reuse after Albergo. Opens the
    # `bnb-agriturismo` cluster (was 0 templates) — 2nd travel cluster
    # after boutique-hotel. Standard tier (€ 75 · agriturismo band).
    # Seeds at tier=draft via TEMPLATE_REGISTRY · multilingual + flip
    # via T60.
    {
        "name": "Podere Le Querce — Agriturismo di Famiglia",
        "slug": "podere-agriturismo",
        "category_slug": "travel",
        "short_description": "Agriturismo di famiglia in Chianti Classico · 4 camere + dispensa contadina con 8 prodotti del podere · Famiglia Pasquinelli dal 1934.",
        "description": (
            "Podere Le Querce riusa l'archetipo artisan-workshop con "
            "identità di agriturismo familiare in Chianti Classico. "
            "Palette deep oak-green + wheat-cream + harvest-copper "
            "(terza polarità dell'archetipo · vs Bottega walnut+cream+"
            "orange · vs Sapori bordeaux+travertine+olive · zero "
            "sovrapposizione di RGB primario), tipografia EB Garamond + "
            "Source Sans 3 (heritage-italiana editoriale · vs Libre "
            "Baskerville + Nunito di Bottega · vs IBM Plex Serif + Plex "
            "Sans di Sapori).\n\n"
            "Include: homepage con dispensa di 8 prodotti del podere "
            "(olio EVO · Chianti Classico DOCG · Vin Santo · miele · "
            "marmellata · pecorino · salame cinta senese · cantucci) + "
            "4 produttori del territorio (pastore · mugnaio · norcino · "
            "monastero) + 4 provenance items (oliveto · vigna · orto · "
            "stalla); dispensa con filtro per produzione e cassa di "
            "legno marchiata; product page con olio EVO 2025 in evidenza "
            "(2.400 piante · spremitura entro 8 ore · 412 mg/kg "
            "polifenoli); pagina famiglia con calendario stagionale "
            "(primavera/estate/vendemmia/autunno-inverno) + Maria "
            "Pasquinelli matriarca classe 1962 al timone dal 1985; diario "
            "con 3 voci dalla campagna (vendemmia · raccolta olive · "
            "prime arnie); soggiorno con form 7-campi e card hours + "
            "5 FAQ ricorrenti."
        ),
        "price": Decimal("75.00"),
        "is_free": False,
        "featured": False,
        "order": 2,
        "brand": {
            "brand_name": "Podere Le Querce · Agriturismo di Famiglia",
            "tagline": "Quattro generazioni di Pasquinelli · Greve in Chianti · dal 1934",
            "palette": {"primary": "#314020", "secondary": "#E8DCB8", "accent": "#B8651F"},
            "typography": "EB Garamond + Source Sans 3",
            "personality": "famiglia-che-ospita, contadino, multigenerazionale, stagionale",
            "logo_concept": "Wordmark «Podere Le Querce» in EB Garamond italic con piccolo simbolo di quercia stilizzata accanto · niente cipresso né mulino né tavolata · estetica di casa colonica toscana · NB la quercia è la pianta che dà il nome al podere (le querce secolari del bosco), non un cliché toscano generico.",
        },
    },
    # ── Portfolio (2) ───────────────────────────────────────────
    {
        "name": "Chiara — Portfolio Creativo",
        "slug": "chiara-portfolio-creativo",
        "category_slug": "portfolio",
        "short_description": "Design minimale e raffinato per freelancer e creativi. Galleria filtrata, bio animata e integrazione social.",
        "description": (
            "Chiara lascia che il lavoro parli da sé. Design minimale con ampio spazio bianco "
            "e focus assoluto sulle immagini del portfolio.\n\n"
            "Include: homepage con galleria masonry filtrabile, pagina progetto con dettaglio e processo creativo, "
            "sezione about con bio e timeline professionale, pagina contatti con form e social links, "
            "integrazione Instagram e Behance."
        ),
        "price": Decimal("0.00"),
        "is_free": True,
        "featured": True,
        "order": 1,
        "brand": {
            "brand_name": "Chiara Studio",
            "tagline": "Ogni progetto racconta una storia",
            "palette": {"primary": "#FAFAFA", "secondary": "#111111", "accent": "#FF6B6B"},
            "typography": "Syne + Inter",
            "personality": "minimale, raffinato, personale",
            "logo_concept": "Nome 'Chiara' in font handwritten con punto rosso corallo, sfondo bianco puro",
        },
    },
    {
        "name": "Pixel — Portfolio Fotografico",
        "slug": "pixel-portfolio-fotografico",
        "category_slug": "portfolio",
        "short_description": "Immersivo e drammatico per fotografi. Galleria fullscreen, slideshow e presentazione progetto cinematografica.",
        "description": (
            "Pixel è il template per fotografi che vogliono presentare il proprio lavoro "
            "con impatto visivo massimo. Background scuro che esalta ogni fotografia.\n\n"
            "Include: homepage con slideshow fullscreen, gallerie per progetto con lightbox, "
            "pagina about con attrezzatura e approccio, sezione servizi fotografici, "
            "form preventivo con dettagli evento, blog con storie dai set."
        ),
        "price": Decimal("49.00"),
        "is_free": False,
        "featured": False,
        "order": 2,
        "brand": {
            "brand_name": "Pixel Photography",
            "tagline": "L'arte di catturare l'attimo",
            "palette": {"primary": "#0A0A0A", "secondary": "#E0E0E0", "accent": "#FF4444"},
            "typography": "Archivo + Inter",
            "personality": "drammatico, immersivo, professionale",
            "logo_concept": "Diaframma di obiettivo stilizzato in bianco su nero, linee nette e precise",
        },
    },
    # ── eCommerce (3) ───────────────────────────────────────────
    {
        "name": "Bottega — Shop Artigianale",
        "slug": "bottega-shop-artigianale",
        "category_slug": "ecommerce",
        "short_description": "Caldo e autentico per negozi artigianali e prodotti Made in Italy. Catalogo, carrello e storytelling del prodotto.",
        "description": (
            "Bottega è il template per artigiani, produttori locali e negozi di prodotti autentici "
            "che vogliono vendere online mantenendo il calore della bottega tradizionale.\n\n"
            "Include: homepage con prodotti in evidenza e storia del brand, catalogo filtrato per categoria, "
            "scheda prodotto con galleria, varianti e recensioni, carrello e checkout, "
            "sezione about con storia dell'artigiano, blog con processo produttivo."
        ),
        "price": Decimal("69.00"),
        "is_free": False,
        "featured": False,
        "order": 1,
        "brand": {
            "brand_name": "La Bottega di Martino",
            "tagline": "Fatto a mano, fatto col cuore",
            "palette": {"primary": "#3E2723", "secondary": "#D7CCC8", "accent": "#FF8F00"},
            "typography": "Libre Baskerville + Nunito Sans",
            "personality": "artigianale, caldo, autentico",
            "logo_concept": "Mani che modellano argilla stilizzate in marrone caldo, tipografia serif classica",
        },
    },
    # T53 · Wave 1 Pass-9 (2026-05-12) · 1st reuse of artisan-workshop
    # archetype after Bottega (D-051 Option A: zero new HTML files).
    # Opens new `wine-food-boutique` cluster (was 0 templates). Premium
    # tier (€ 89 · enoteca premium pricing band). Seeds at tier=draft
    # via TEMPLATE_REGISTRY.json — IT-only at T53 build (D-102 cadence);
    # multilingual EN/FR/ES/AR + AAA walk + public flip via T54.
    {
        "name": "Sapori di Langa — Enoteca dei Vignaioli",
        "slug": "sapori-di-langa",
        "category_slug": "ecommerce",
        "short_description": "Enoteca terroir-curatoriale premium · quaranta vignaioli indipendenti delle Langhe Roero Monferrato · vino olio EVO castelmagno tartufo bianco · Alba dal 1987.",
        "description": (
            "Sapori di Langa riutilizza l'archetipo artisan-workshop "
            "con identità di enoteca-boutique dedicata ai vignaioli "
            "indipendenti delle Langhe. Palette bordeaux #4A1E1F + "
            "carta-cera crema + olivo (seconda polarità del cluster "
            "artisan-workshop · vs Bottega cuoio-mattone-noce caldo "
            "trattoria), tipografia IBM Plex Serif + IBM Plex Sans "
            "(register editoriale-tipografico vs Libre Baskerville + "
            "Nunito Sans di Bottega).\n\n"
            "Include: homepage con headline incentrata sulla figura "
            "del vignaiolo indipendente, stamp-panel «Cavalier dell'"
            "Ordine dei Cavalieri del Tartufo» + «quarant'anni di "
            "selezione» + «consegna in cassa di legno», catalogo "
            "Cantina con 8 referenze (Barolo Cannubi Brezza · Barbera "
            "Superiore Vajra · Dolcetto d'Alba Boasso · Verduno "
            "Pelaverga · Olio EVO Langhe Brovia · Castelmagno DOP · "
            "Nocciola Tonda Gentile · Tartufo Bianco di stagione), "
            "scheda bottiglia Barolo Cannubi 2019 con info-rows "
            "denominazione/annata/vinificazione/affinamento/gradazione, "
            "size-options (bottiglia/magnum/jeroboam/cassa da 6), pagina "
            "I vignaioli con portrait dei quattro produttori associati "
            "(Carlo Brezza · Maria Vajra · Luigi Boasso · Anna Brovia), "
            "Diario con tre voci di stagione (vendemmia / tartufo / "
            "olio nuovo), visite stagionali in vigna con form prenotazione."
        ),
        "price": Decimal("89.00"),
        "is_free": False,
        "featured": False,
        "order": 3,
        "brand": {
            "brand_name": "Sapori di Langa · Enoteca dei Vignaioli",
            "tagline": "Quaranta vignaioli indipendenti · Alba · dal 1987",
            "palette": {"primary": "#4A1E1F", "secondary": "#F2E9D8", "accent": "#6B7E47"},
            "typography": "IBM Plex Serif + IBM Plex Sans",
            "personality": "terroir-curatoriale, sommelier-pacato, vignaiolo-relazionale",
            "logo_concept": "Wordmark «Sapori di Langa» Plex Serif maiuscoletto su lozenge bordeaux con sigillo ceralacca olivo «SdL» · niente grappolo né bottiglia stilizzata · estetica di enoteca-tabernacolo dei vignaioli, non di wine-bar generalista né di cantina industriale.",
        },
    },
    {
        "name": "Luxe — Fashion Store",
        "slug": "luxe-fashion-store",
        "category_slug": "ecommerce",
        "short_description": "Esclusivo e raffinato per moda e accessori. Lookbook, quick view e checkout premium con stripe integrato.",
        "description": (
            "Luxe è il template per brand di moda, accessori e lifestyle che puntano "
            "all'esperienza di acquisto premium.\n\n"
            "Include: homepage con hero video e collezione stagionale, catalogo con quick view e filtri avanzati, "
            "pagina prodotto con zoom, taglie e wishlist, lookbook con shoppable images, "
            "carrello slide-out, checkout Stripe integrato, area account cliente."
        ),
        "price": Decimal("89.00"),
        "is_free": False,
        "featured": False,
        "order": 2,
        "brand": {
            "brand_name": "Maison Luxe",
            "tagline": "Stile senza compromessi",
            "palette": {"primary": "#000000", "secondary": "#F5F5F5", "accent": "#B8860B"},
            "typography": "Cormorant Garamond + Montserrat",
            "personality": "lussuoso, minimale, sofisticato",
            "logo_concept": "Nome 'LUXE' in maiuscolo spaziato, serif sottile, con linea oro sottostante",
        },
    },
    # T61 · Wave 2 Pass-5 (2026-05-13) · 1st reuse of fashion-editorial
    # archetype after Luxe (D-051 Option A · zero new HTML files). Same
    # category (ecommerce) so no `skin_source_category` override needed.
    # Opens the `jewelry` cluster (was 0 templates) · 4th ecommerce
    # cluster after artisan-workshop+fashion-editorial+wine-food-boutique.
    # Premium tier (€ 119 · alta gioielleria band · highest in catalog
    # above Luxe at € 89). Seeds at tier=draft · multilingual via T62.
    {
        "name": "Gemma — Atelier di Alta Gioielleria",
        "slug": "gemma-gioielleria",
        "category_slug": "ecommerce",
        "short_description": "Atelier di alta gioielleria a Milano Brera · 4 generazioni di orafi dal 1908 · pezzi unici e serie limitate · Eleonora Gemma gemmologa GIA ex-Buccellati.",
        "description": (
            "Gemma riusa l'archetipo fashion-editorial con identità di atelier "
            "di alta gioielleria. Palette pearl-night #0F0E14 + champagne-white "
            "#F1ECDF + rose-quartz #9F7373 (seconda polarità dell'archetipo · "
            "vs Luxe noir+ivory+champagne-gold · zero RGB overlap), tipografia "
            "Bodoni Moda + Inter (Didone-influenced jewelry register vs "
            "Cormorant Garamond + Montserrat fashion register di Luxe).\n\n"
            "Include: homepage con hero atelier + 4 pezzi della Serie Inverno "
            "2026 + manifesto «gioielleria d'autore» + atelier in cifre + "
            "editoriale teaser firmato Paolo Roversi · stilismo Camille "
            "Bidault-Waddington + drop metadata + private-CTA per commissione "
            "su misura; collezione con filter-groups (categoria/materiale/"
            "pietra-centrale) + 8 pezzi Serie Inverno (4 pezzi unici + 4 serie "
            "limitate · prezzo su richiesta o esposto da € 4 800 a € 47 800); "
            "pezzo featured anello «Cuneo» brillante 3,02 ct con scheda GIA + "
            "10-row info + 5-row care + 4-step provenance + 4 related; pagina "
            "casa Gemma con 4 generazioni (Eligio 1908 · Carlo 1932-1986 · "
            "Giuseppe 1958- · Eleonora 1968 ex-Buccellati 1996-2014 + GIA + "
            "Gübelin) + 3 ateliers (Milano Brera · Paris Place Vendôme · "
            "visite a domicilio Roma/Tokyo/Singapore) + 5 press dict + "
            "numbers; lookbook editoriale 4 studi al palazzo Cusani Brera "
            "firmati Paolo Roversi novembre 2025; concierge con form 8-campi "
            "+ 3 maison-cards + 5 faq."
        ),
        "price": Decimal("119.00"),
        "is_free": False,
        "featured": False,
        "order": 3,
        "brand": {
            "brand_name": "Gemma · Atelier di Alta Gioielleria",
            "tagline": "Quattro generazioni di orafi · Milano Brera · dal 1908",
            "palette": {"primary": "#0F0E14", "secondary": "#F1ECDF", "accent": "#9F7373"},
            "typography": "Bodoni Moda + Inter",
            "personality": "auteur-jeweler, gemmologa, milanese-brera, riservata",
            "logo_concept": "Wordmark «Gemma» in Bodoni Moda con sottolineatura tratteggiata e piccolo sigillo «117MI» (punzone Camera di Commercio Milano 1948) accanto · niente brillanti stilizzati né corone né flourish · estetica di atelier di famiglia · NB il sigillo «117MI» è il punzone Gemma reale registrato.",
        },
    },
]


class Command(BaseCommand):
    help = "Seed the database with realistic WebTemplate and TemplateBrand data for all MVP categories"

    def _apply_taxonomy_metadata(self, template):
        """Apply taxonomy v2 metadata to a freshly-created ``WebTemplate``.

        Looks up the per-template entry in ``TEMPLATE_METADATA`` and
        writes profession_cluster + visual_style + use_cases + audience
        + price_tier + search_keywords + 7 feature flags. Skips silently
        if the template slug is not in the metadata dict or if the
        required seed rows (clusters, styles) have not been loaded —
        a later ``manage.py seed_profession_clusters`` +
        ``seed_visual_styles`` + backfill migration can always catch up.
        """
        md = TEMPLATE_METADATA.get(template.slug)
        if not md:
            return

        try:
            cluster = ProfessionCluster.objects.get(slug=md["cluster"])
            style = VisualStyle.objects.get(slug=md["style"])
        except (ProfessionCluster.DoesNotExist, VisualStyle.DoesNotExist):
            self.stderr.write(
                self.style.WARNING(
                    f"  taxonomy skipped for {template.slug}: run "
                    f"seed_visual_styles + seed_profession_clusters first."
                )
            )
            return

        template.profession_cluster = cluster
        template.visual_style = style
        template.use_cases = list(md["use_cases"])
        template.audience = list(md["audience"])
        template.price_tier = md["price_tier"]
        template.search_keywords = md["search_keywords"]
        for flag in _FEATURE_FLAG_FIELDS:
            setattr(template, flag, md[flag])
        template.save(
            update_fields=[
                "profession_cluster",
                "visual_style",
                "use_cases",
                "audience",
                "price_tier",
                "search_keywords",
                *_FEATURE_FLAG_FIELDS,
                "updated_at",
            ]
        )

    def handle(self, *args, **options):
        categories = {c.slug: c for c in Category.objects.all()}
        if not categories:
            self.stderr.write(self.style.ERROR("No categories found. Run seed_categories first."))
            return

        # X.3 Commit 5 · post NOT NULL flip: cluster + style must be
        # present at CREATE time (INSERT can no longer land with NULL
        # FKs and be patched later). Ensure the taxonomy tables are
        # populated · callers that only ran ``seed_categories + seed_
        # templates`` (legacy fixture path in apps.projects tests)
        # still get a valid seed chain without touching apps/projects.
        if not ProfessionCluster.objects.exists():
            call_command("seed_profession_clusters", verbosity=0)
        if not VisualStyle.objects.exists():
            call_command("seed_visual_styles", verbosity=0)

        # Pre-resolve the taxonomy maps so the ``defaults`` dict
        # carries the FKs upfront. Idempotent: ``get_or_create`` still
        # keys on slug · admin-authored overrides on existing rows
        # are preserved.
        clusters = {c.slug: c for c in ProfessionCluster.objects.all()}
        styles = {s.slug: s for s in VisualStyle.objects.all()}

        created_count = 0
        for t_data in SEED_TEMPLATES:
            category = categories.get(t_data["category_slug"])
            if not category:
                self.stderr.write(f"  Category '{t_data['category_slug']}' not found, skipping {t_data['name']}")
                continue

            md = TEMPLATE_METADATA.get(t_data["slug"])
            cluster = clusters.get(md["cluster"]) if md else None
            style = styles.get(md["style"]) if md else None
            if cluster is None or style is None:
                self.stderr.write(
                    self.style.WARNING(
                        f"  Taxonomy missing for {t_data['slug']}: run "
                        f"seed_profession_clusters + seed_visual_styles "
                        f"first. Skipping."
                    )
                )
                continue

            template, created = WebTemplate.objects.get_or_create(
                slug=t_data["slug"],
                defaults={
                    "name": t_data["name"],
                    "category": category,
                    "description": t_data["description"],
                    "short_description": t_data["short_description"],
                    "price": t_data["price"],
                    "is_free": t_data["is_free"],
                    "featured": t_data["featured"],
                    "order": t_data["order"],
                    "status": WebTemplate.Status.PUBLISHED,
                    # NOT NULL FKs · required at INSERT post-X.3 C5.
                    "profession_cluster": cluster,
                    "visual_style": style,
                },
            )

            if created:
                created_count += 1
                brand_data = t_data["brand"]
                TemplateBrand.objects.get_or_create(
                    template=template,
                    defaults=brand_data,
                )
                # X.2 Commit 3 · apply the remaining taxonomy v2
                # metadata (use_cases, audience, price_tier,
                # search_keywords, feature flags) on fresh seed. The
                # FK columns already landed in the INSERT above · the
                # helper now only fills the additive non-FK fields.
                self._apply_taxonomy_metadata(template)
                self.stdout.write(f"  Created: {t_data['name']} ({brand_data['brand_name']})")
            else:
                self.stdout.write(f"  Exists:  {t_data['name']}")

        self.stdout.write(
            self.style.SUCCESS(f"\nDone. {created_count} templates created.")
        )

        # D-055: apply tier from the registry so newly-seeded rows (and any
        # existing rows whose tier the registry just changed) land on the
        # correct side of the public gate. Keeping the tier source of truth
        # in TEMPLATE_REGISTRY.json prevents two codepaths drifting apart.
        self.stdout.write("\nSyncing tiers from TEMPLATE_REGISTRY.json…")
        call_command("sync_template_tiers")
