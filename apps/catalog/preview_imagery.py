"""Curated stock imagery library for template previews.

Each MVP category maps to a list of category-appropriate photo URLs.
Images are downloaded once and cached on disk so the preview generator
operates against stable local files, even when offline.

Replace the URLs (or swap to local stock / licensed / generated images
later) without touching the preview generator or HTML compositions.
"""
from __future__ import annotations

import hashlib
import logging
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from django.conf import settings

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Imagery configuration — keyed by Category.slug
# ---------------------------------------------------------------------------
#
# All URLs are direct Unsplash CDN links (no API key required) using a
# common transform: ?w=1600&q=80&auto=format&fit=crop. Each list intentionally
# mixes a wide hero shot, a few content shots, and a couple of square/portrait
# accents that the HTML compositions can use as menu items / cards / avatars.
#
# Layout convention per category list:
#   index 0  → wide hero image
#   index 1  → secondary feature image
#   index 2..N → content cards / gallery / menu items / cast
#
IMAGERY_CONFIG: dict[str, list[str]] = {
    "restaurant": [
        # 0: hero - moody restaurant interior
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - chef plating
        "https://images.unsplash.com/photo-1577106263724-2c8e03bfe9cf?w=1200&q=80&auto=format&fit=crop",
        # 2-5: menu items
        "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1551782450-a2132b4ba21d?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=800&q=80&auto=format&fit=crop",
    ],
    # Per-archetype restaurant pools — see apps/catalog/template_dna.py.
    # Each pool uses FULLY-DISTINCT URLs from the others — zero overlap with
    # each other, zero overlap with legacy `restaurant`, zero overlap with
    # `restaurant-street`. Each photo was hand-checked in Session 10 after the
    # Session 9 set produced visually similar pools (5 of 6 URLs were shared
    # between fine and trattoria, only the hero differed).
    #
    # restaurant-fine: dark, low-key, plated close-ups, fine-dining mood.
    # restaurant-trattoria: bright daylight, rustic, sunny, family-table.
    "restaurant-fine": [
        # 0: hero — dark restaurant table close-up with plated dish & wine glass
        "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1600&q=80&auto=format&fit=crop",
        # 1: signature plated dish, dark backdrop, dramatic light
        "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=1200&q=80&auto=format&fit=crop",
        # 2-5: course imagery — all dark / low-key plated
        "https://images.unsplash.com/photo-1505253758473-96b7015fcd40?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1551218808-94e220e084d2?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1544025162-d76694265947?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=800&q=80&auto=format&fit=crop",
    ],
    "restaurant-trattoria": [
        # 0: hero — three pasta plates on a white tablecloth, sunny overhead
        "https://images.unsplash.com/photo-1481931098730-318b6f776db0?w=1600&q=80&auto=format&fit=crop",
        # 1: dramatic margherita pizza cheese-pull, warm light
        "https://images.unsplash.com/photo-1593504049359-74330189a345?w=1200&q=80&auto=format&fit=crop",
        # 2-5: bright rustic dishes — pesto pasta, panna cotta jars, fettuccine pan, family table
        "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=800&q=80&auto=format&fit=crop",
    ],
    "restaurant-street": [
        # 0: hero - bold burger product shot (NEW)
        "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - pizza counter (NEW)
        "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=1200&q=80&auto=format&fit=crop",
        # 2-5: product grid items (NEW street-food shots)
        "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=800&q=80&auto=format&fit=crop",
    ],
    "medical": [
        # 0: hero - bright modern clinic
        "https://images.unsplash.com/photo-1631815587646-b85a1bb027e1?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - doctor with patient
        "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1200&q=80&auto=format&fit=crop",
        # 2-5: services / staff
        "https://images.unsplash.com/photo-1582750433449-648ed127bb54?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1666214280557-f1b5022eb634?w=800&q=80&auto=format&fit=crop",
    ],
    # Per-archetype medical pools — see apps/catalog/template_dna.py.
    # All URLs reuse photos already proven to download from Unsplash so
    # the pilot run is offline-safe after a single warm cache. Two
    # templates in the same category never share the same image set.
    "medical-family": [
        # 0: hero - warm doctor + patient (bright, soft lighting)
        "https://images.unsplash.com/photo-1666214280557-f1b5022eb634?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - friendly clinician
        "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=1200&q=80&auto=format&fit=crop",
        # 2-5: portraits + cards
        "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1582750433449-648ed127bb54?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1631815587646-b85a1bb027e1?w=800&q=80&auto=format&fit=crop",
    ],
    "medical-specialist": [
        # 0: hero - low-key portrait (lawyer pool — serious editorial energy)
        "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - bookshelf (gravitas backdrop)
        "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&q=80&auto=format&fit=crop",
        # 2-5: alternative portraits + clinical
        "https://images.unsplash.com/photo-1505664194779-8beaceb93744?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1591025207163-942350e47db2?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1589994965851-a8f479c573a9?w=800&q=80&auto=format&fit=crop",
    ],
    # Session 26: per-specialty pools replace shared medical-specialist
    "medical-cardiology": [
        # 0: hero - clinical cardiovascular (stethoscope + white coat)
        "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - ECG / diagnostic equipment
        "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1200&q=80&auto=format&fit=crop",
        # 2-5: cardiology-specific
        "https://images.unsplash.com/photo-1631815587646-b85a1bb027e1?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1530026186672-2cd00ffc50fe?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1551076805-e1869033e561?w=800&q=80&auto=format&fit=crop",
    ],
    "medical-dermatology": [
        # 0: hero - aesthetic dermatology (clinical-beauty crossover)
        "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - skin examination / dermatoscopy
        "https://images.unsplash.com/photo-1582750433449-648ed127bb54?w=1200&q=80&auto=format&fit=crop",
        # 2-5: dermatology-specific
        "https://images.unsplash.com/photo-1594824476967-48c8b964273f?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1629909613654-28e377c37b09?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?w=800&q=80&auto=format&fit=crop",
    ],
    "medical-wellness": [
        # 0: hero - bright airy interior (real-estate pool — closest to spa)
        "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - editorial portrait studio (portfolio pool)
        "https://images.unsplash.com/photo-1452587925148-ce544e77e70d?w=1200&q=80&auto=format&fit=crop",
        # 2-5: tactile / quiet imagery
        "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=800&q=80&auto=format&fit=crop",
    ],
    "lawyer": [
        # 0: hero - law office / columns
        "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - law books shelf
        "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&q=80&auto=format&fit=crop",
        # 2-5: practice areas / portraits
        "https://images.unsplash.com/photo-1505664194779-8beaceb93744?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1589994965851-a8f479c573a9?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1591025207163-942350e47db2?w=800&q=80&auto=format&fit=crop",
    ],
    "agency": [
        # 0: hero - dark creative workspace
        "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - team brainstorm
        "https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80&auto=format&fit=crop",
        # 2-5: case studies
        "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1559028012-481c04fa702d?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1551434678-e076c223a692?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1558655146-9f40138edfeb?w=800&q=80&auto=format&fit=crop",
    ],
    "business": [
        # LEGACY pool, kept as fallback for any template that might still
        # resolve through `preview_compositions/business.html`. Phase 2g2x
        # (Session 17) moved both published business templates onto their
        # own per-archetype pools — `business-corporate` and
        # `business-startup` — so this pool is architecturally unused by
        # the two current published business templates. Do NOT delete: the
        # legacy composition still exists (D-036 additive rule) and could
        # be used by a future legacy-only sibling during migration.
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1600&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1556761175-b413da4baf72?w=1200&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1542744094-3a31f272c490?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=800&q=80&auto=format&fit=crop",
    ],
    # Per-archetype business pools — see apps/catalog/template_dna.py.
    # Phase 2g2x split: Pragma (corporate-suite) and Elevate (startup-saas-landing)
    # were renderring through the same legacy composition + the same 6-URL pool,
    # producing identity-crash cards. The pools below are fully distinct —
    # zero URL overlap with each other and zero overlap with the legacy
    # `business` pool.
    #
    # business-corporate: institutional — boardroom meetings, corporate HQ
    #     interiors, executive portraits, manufacturing facilities. Dark
    #     daylight, serious mood. Photo-led composition (the boardroom hero
    #     carries the whole above-the-fold mood).
    # business-startup:   product-led — laptop screens with dashboards,
    #     open-plan tech offices, code editors, bright tech interiors. The
    #     startup composition is typographic + mockup-card led (no big
    #     hero photo), so this pool mostly supplies accent tiles and
    #     background gradients — but the few places it does appear must
    #     still read as startup/product.
    "business-corporate": [
        # 0: hero — boardroom long-table meeting, day-light, serious
        "https://images.unsplash.com/photo-1542626991-cbc4e32524cc?w=1600&q=80&auto=format&fit=crop",
        # 1: feature — corporate HQ atrium / glass interior
        "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&q=80&auto=format&fit=crop",
        # 2-5: advisory portraits + industrial facility + conference detail
        "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1560439514-4e9645039924?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1664575602554-2087b04935a5?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1573497491208-6b1acb260507?w=800&q=80&auto=format&fit=crop",
    ],
    "business-startup": [
        # 0: hero placeholder (unused as big hero — composition is typographic-led)
        #    but kept as a product-dashboard shot in case the composition
        #    ever wants a subtle background tile.
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1600&q=80&auto=format&fit=crop",
        # 1: feature — MacBook with dashboard UI
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200&q=80&auto=format&fit=crop",
        # 2-5: product UI / code / open-plan tech office / smartphone app
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1517292987719-0369a794ec0f?w=800&q=80&auto=format&fit=crop",
    ],
    "real-estate": [
        # 0: hero - luxury modern home exterior
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - bright living room
        "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80&auto=format&fit=crop",
        # 2-5: property listings
        "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=800&q=80&auto=format&fit=crop",
    ],
    "portfolio": [
        # LEGACY pool, kept as fallback for any template that might still
        # resolve through `preview_compositions/portfolio.html`. Phase 2g2x
        # (Session 18) moved both published portfolio templates onto their
        # own per-archetype pools — `portfolio-designer` and
        # `portfolio-photographer` — so this pool is architecturally unused
        # by the two current published portfolio templates. Do NOT delete:
        # the legacy composition still exists (D-036 additive rule) and
        # could be used by a future legacy-only sibling during migration.
        "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1452587925148-ce544e77e70d?w=1200&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1542744095-291d1f67b221?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1483058712412-4245e9b90334?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?w=800&q=80&auto=format&fit=crop",
    ],
    # Per-archetype portfolio pools — see apps/catalog/template_dna.py.
    # Phase 2g2x split: Chiara (editorial-designer-grid) and Pixel
    # (cinematic-photographer) were rendering through the same legacy
    # composition + the same 6-URL pool, producing an identity-crash pair
    # (Pixel, a photographer, showed designer-editorial copy and identical
    # photos to Chiara). The pools below are fully distinct — zero URL
    # overlap with each other and zero overlap with the legacy `portfolio`
    # pool.
    #
    # portfolio-designer: design-workspace vibe — sketchbooks, paper
    #     prototypes, studio work-in-progress, systemic design artifacts.
    #     Chiara's composition is typographic-led (NO big hero photo) so
    #     this pool mostly supplies small project-index tiles and the
    #     optional clients ribbon background. A failing URL degrades
    #     gracefully — the card is still legible without any photo.
    # portfolio-photographer: cinematic-photostill vibe — moody, low-key
    #     photographic stills (reportage, still life, portrait). Pixel's
    #     composition is image-first with a dominant fullbleed hero, so
    #     URL 0 (hero) is the most important — reuse from restaurant-fine
    #     which is proven offline-safe. The other 5 slots come from pools
    #     whose photos already read as cinematic low-key work.
    "portfolio-designer": [
        # 0: hero-slot (NOT used as a big hero image — the Chiara composition
        #    is typographic; this fills small grid tiles if the composition
        #    ever wants a background accent). Creative workspace feel.
        "https://images.unsplash.com/photo-1558655146-9f40138edfeb?w=1600&q=80&auto=format&fit=crop",
        # 1: feature — laptop/paper case-study vibe
        "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=1200&q=80&auto=format&fit=crop",
        # 2-5: project-index tiles — creative workspace / design artifacts
        "https://images.unsplash.com/photo-1559028012-481c04fa702d?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1551434678-e076c223a692?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=800&q=80&auto=format&fit=crop",
    ],
    "portfolio-photographer": [
        # Pixel (cinematic-photographer) — image-first dominant fullbleed
        # hero + 4 filmstrip frames. All 6 URLs are lifted directly from
        # `template_content_pixel.py` (Pixel's live content registry) so
        # the static preview reads as the same photographer brand the
        # live preview already ships. Zero URL overlap with any other
        # imagery pool — in particular zero overlap with `restaurant-fine`
        # (Gusto), which the prior pool shared for slots 0-1 under a
        # "proven offline-safe" rationale that produced a Gusto/Pixel
        # visual collision in the listing card.
        #
        # 0: hero — moody editorial shadow portrait (Pixel live hero).
        "https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?w=1600&q=80&auto=format&fit=crop",
        # 1: feature — cinematic wide reportage still (Pixel live series).
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1200&q=80&auto=format&fit=crop",
        # 2-5: filmstrip series stills — reportage, portrait, still-life
        "https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1505820013142-f86a3439c5b2?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1499346030926-9a72daac6c63?w=800&q=80&auto=format&fit=crop",
    ],
    "ecommerce": [
        # 0: hero - editorial fashion
        "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1600&q=80&auto=format&fit=crop",
        # 1: feature - product flat lay
        "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1200&q=80&auto=format&fit=crop",
        # 2-5: products
        "https://images.unsplash.com/photo-1542838132-92c53300491e?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=800&q=80&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=800&q=80&auto=format&fit=crop",
    ],
}


# ---------------------------------------------------------------------------
# Cache helpers
# ---------------------------------------------------------------------------

def _cache_dir() -> Path:
    """Local cache root for downloaded preview imagery."""
    root = Path(settings.MEDIA_ROOT) / "preview_imagery"
    root.mkdir(parents=True, exist_ok=True)
    return root


def _cache_path(category_slug: str, url: str) -> Path:
    """Stable on-disk path for a given (category, url) pair."""
    cat_dir = _cache_dir() / category_slug
    cat_dir.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
    suffix = Path(urlparse(url).path).suffix or ".jpg"
    return cat_dir / f"{digest}{suffix}"


def _download(url: str, dest: Path) -> bool:
    """Download a URL to dest. Returns True on success."""
    try:
        req = Request(url, headers={"User-Agent": "marketweb-preview-bot/1.0"})
        with urlopen(req, timeout=30) as resp:  # noqa: S310 — controlled URL list
            data = resp.read()
        if not data:
            return False
        dest.write_bytes(data)
        return True
    except Exception as exc:  # noqa: BLE001
        logger.warning("preview imagery download failed for %s: %s", url, exc)
        return False


def ensure_cached(category_slug: str) -> list[Path]:
    """Ensure imagery for a category is on disk and return local paths.

    Falls back to whatever subset succeeded — callers should handle the
    possibility that the list is shorter than expected. If nothing is
    cached at all, returns an empty list and the caller should degrade
    gracefully (the HTML composition will still render, just without
    photos in those slots).
    """
    urls = IMAGERY_CONFIG.get(category_slug, [])
    paths: list[Path] = []
    for url in urls:
        dest = _cache_path(category_slug, url)
        if dest.exists() and dest.stat().st_size > 0:
            paths.append(dest)
            continue
        if _download(url, dest):
            paths.append(dest)
    return paths


def get_local_uris(category_slug: str) -> list[str]:
    """Return file:// URIs for the cached images of a category.

    These URIs are safe to embed inside HTML loaded by Playwright via a
    file:// page, because Chromium permits same-origin file:// references.
    """
    paths = ensure_cached(category_slug)
    return [p.resolve().as_uri() for p in paths]
