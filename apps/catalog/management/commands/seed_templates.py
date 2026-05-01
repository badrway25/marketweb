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
    # ── eCommerce (2) ───────────────────────────────────────────
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
