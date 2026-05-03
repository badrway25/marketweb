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
    # Salute — clinic institutional (Pexels, Session medical-second-wave)
    # Pool tone: bright modern reception, teal/cyan, patient consultations,
    # professional but warm (not editorial-specialist like cardio/derm).
    "medical": [
        # 0: hero wide — modern teal-accent clinic reception (Pavel Danilyuk)
        "https://images.pexels.com/photos/7108324/pexels-photo-7108324.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
        # 1: feature — female doctor consulting patient, bright modern office (cottonbro)
        "https://images.pexels.com/photos/7579823/pexels-photo-7579823.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
        # 2: healthcare patient discussion (RDNE Stock)
        "https://images.pexels.com/photos/6129441/pexels-photo-6129441.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        # 3: bright waiting room (Los Muertos Crew)
        "https://images.pexels.com/photos/8459996/pexels-photo-8459996.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        # 4: clinic reception staff welcoming (Pavel Danilyuk)
        "https://images.pexels.com/photos/7108325/pexels-photo-7108325.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        # 5: doctor patient consultation (CDC)
        "https://images.pexels.com/photos/3992806/pexels-photo-3992806.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
    ],
    # Per-archetype medical pools — see apps/catalog/template_dna.py.
    # Each pool is curated on Pexels (Session medical-second-wave) to enforce
    # D-054 visual differentiation: clinic vs family vs wellness must read as
    # three different products, not recolored siblings.
    #
    # Famiglia — pediatric warm (peach/coral, child-friendly but not cartoon)
    "medical-family": [
        # 0: hero — pediatric check-up girl bright clinic (Gustavo Fring)
        "https://images.pexels.com/photos/7447009/pexels-photo-7447009.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
        # 1: feature — mother joyfully holding baby, warm indoor (Polina Tankilevitch)
        "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
        # 2: child stethoscope check (Gustavo Fring)
        "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        # 3: cheerful child yellow dress pediatric clinic (Los Muertos Crew)
        "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        # 4: medical practitioner newborn (Jonathan Borba)
        "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        # 5: pediatric doctor stethoscope back check cozy (cottonbro)
        "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
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
    # Benessere — holistic serene (sage green, candle light, ritual objects)
    "medical-wellness": [
        # 0: hero — tranquil massage room natural light (Anna Tarazevich)
        "https://images.pexels.com/photos/6560308/pexels-photo-6560308.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
        # 1: feature — spa aromatherapy wooden table (Anna Tarazevich)
        "https://images.pexels.com/photos/6560252/pexels-photo-6560252.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
        # 2: herbal tea lavender flat-lay (Ray Piedra)
        "https://images.pexels.com/photos/2752031/pexels-photo-2752031.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        # 3: lit candle spa ceramic towels (Tima Miroshnichenko)
        "https://images.pexels.com/photos/6186740/pexels-photo-6186740.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        # 4: crystals incense singing bowl ritual (Katrin Bolovtsova)
        "https://images.pexels.com/photos/6766585/pexels-photo-6766585.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        # 5: yoga meditation studio natural light (Yan Krukau)
        "https://images.pexels.com/photos/8436719/pexels-photo-8436719.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
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
    # ─────────────────────────────────────────────────────────────
    # Per-archetype lawyer pools — Session 53 lawyer live rollout.
    # Zero URL overlap with each other and zero overlap with legacy
    # `lawyer` pool. Lex (classic-gold) renders ink-dark heritage
    # imagery (codici, leather-bound books, gavel portrait). Juris
    # (modern-transparent) renders bright advisory imagery (modern
    # meeting rooms, diverse professionals, glass offices).
    # ─────────────────────────────────────────────────────────────
    "lawyer-classic": [
        # 0: hero — leather-bound Corpus Juris & brass scale, warm ink library
        "https://images.pexels.com/photos/5668772/pexels-photo-5668772.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
        # 1: feature — senior lawyer reviewing contract at mahogany desk
        "https://images.pexels.com/photos/5668858/pexels-photo-5668858.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
        # 2-5: heritage practice imagery — libraries, gavel, robes, ink
        "https://images.pexels.com/photos/5668473/pexels-photo-5668473.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/5669602/pexels-photo-5669602.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/5668854/pexels-photo-5668854.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/1181345/pexels-photo-1181345.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
    ],
    "lawyer-modern": [
        # 0: hero — bright modern advisory meeting, natural light, diverse team
        "https://images.pexels.com/photos/3184338/pexels-photo-3184338.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
        # 1: feature — professional with laptop and documents, glass office
        "https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
        # 2-5: modern consulting - laptop case, collaborative meeting, calendar
        "https://images.pexels.com/photos/3184433/pexels-photo-3184433.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/5439381/pexels-photo-5439381.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/3184418/pexels-photo-3184418.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
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
    # ─────────────────────────────────────────────────────────────
    # Per-archetype agency pools — Session 49 agency live rollout.
    # Fully distinct URL sets so Vertex (creative-studio) and Aura
    # (digital-studio) never render the same image. Every URL is
    # verified on a proven pool (reused from portfolio-designer /
    # business-startup / business-corporate where imagery already
    # passed visual audit in Sessions 31/38/47).
    #
    # agency-creative: editorial studio craft — type specimens on
    #     paper, brand-book hero shot, gallery install, designer desk,
    #     contact sheets. Concept-led, ink/charcoal mood.
    # agency-digital:  product-console momentum — dashboard UI,
    #     modern studio with monitors, dark IDE, product-design
    #     close-up, open-plan tech studio. Delivery energy, violet
    #     ambient light.
    # ─────────────────────────────────────────────────────────────
    "agency-creative": [
        # 0: hero — editorial studio desk with paper case-study artifacts.
        # Session 50 swap: the prior `photo-1561070791-2526d30994b8` URL
        # returned HTTP 404 on every call so the cache never warmed — the
        # composition then received an empty imagery list. Replaced with
        # the portfolio-designer slot-1 URL (proven in Sessions 34/37).
        "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=1600&q=80&auto=format&fit=crop",
        # 1: feature — brand book on desk (design-workspace)
        "https://images.unsplash.com/photo-1586717791821-3f44a563fa4c?w=1200&q=80&auto=format&fit=crop",
        # 2-5: case-study craft shots
        # gallery install / wall exhibit
        "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=900&q=80&auto=format&fit=crop",
        # paper prototypes / type specimens
        "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=900&q=80&auto=format&fit=crop",
        # packaging / editorial still life
        "https://images.unsplash.com/photo-1481487196290-c152efe083f5?w=900&q=80&auto=format&fit=crop",
        # studio portrait (art-director at desk)
        "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=900&q=80&auto=format&fit=crop",
    ],
    "agency-digital": [
        # 0: hero — product dashboard screen close-up (reused business-startup 0)
        "https://images.unsplash.com/photo-1551434678-e076c223a692?w=1600&q=80&auto=format&fit=crop",
        # 1: feature — modern studio with monitors + violet ambient
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200&q=80&auto=format&fit=crop",
        # 2-5: delivery / product / sprint imagery
        # dark IDE / code editor
        "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=900&q=80&auto=format&fit=crop",
        # product design detail on screen
        "https://images.unsplash.com/photo-1559028012-481c04fa702d?w=900&q=80&auto=format&fit=crop",
        # sprint board / post-its (open studio)
        "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=900&q=80&auto=format&fit=crop",
        # dashboard detail / analytics
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=900&q=80&auto=format&fit=crop",
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
    # ─────────────────────────────────────────────────────────────
    # business-fiscal — Wave 2 Pilot #1 (Phase X.4 · Fiscus).
    # Sourced from `docs/content-factory/imagery/packs/financial-
    # services.md` (Pexels · CC0-compatible · curator-verified). Pool
    # shape matches Pragma's: [hero, feature, portrait, portrait,
    # detail, ambient]. Direction per the financial-services blueprint:
    # desks with paperwork, professionals in focus, warm-neutral
    # corporate palette — no clichéd calculator close-ups or
    # handshake-over-monitor stock.
    # ─────────────────────────────────────────────────────────────
    "business-fiscal": [
        # 0: hero — tidy workspace with laptop, documents, eyeglasses
        "https://images.pexels.com/photos/8927688/pexels-photo-8927688.jpeg?auto=compress&cs=tinysrgb&w=1600",
        # 1: feature — contemporary office interior, sleek desk
        "https://images.pexels.com/photos/36175676/pexels-photo-36175676.jpeg?auto=compress&cs=tinysrgb&w=1200",
        # 2: portrait — professional man, eyeglasses, office
        "https://images.pexels.com/photos/7845284/pexels-photo-7845284.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 3: portrait — professional woman, modern office setting
        "https://images.pexels.com/photos/30614308/pexels-photo-30614308.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 4: detail — tax documents with calculator on wooden table
        "https://images.pexels.com/photos/7821914/pexels-photo-7821914.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 5: ambient — law/regulation bookshelf (institutional reassurance)
        "https://images.pexels.com/photos/159832/justice-law-case-hearing-159832.jpeg?auto=compress&cs=tinysrgb&w=800",
    ],
    # ─────────────────────────────────────────────────────────────
    # business-coaching — Wave 2 Pilot #2 (Phase X.4 · Solaria).
    # Sourced exclusively from `docs/content-factory/imagery/packs/
    # coaching.md` (Pexels · CC0-compatible · X.3 C3 reviewer-
    # verified · zero mountain-peak / motivational-quote / drawn-
    # arrow cliché per blueprint §8 + §13). Pool shape matches
    # Fiscus convention: [hero, feature, portrait-coach, portrait-
    # coachee, detail-notebook, ambient-warm-office]. Zero URL
    # overlap with business-fiscal or business-corporate pools.
    # Solaria is NOT grandfathered under LEGACY_EXEMPT_KEYS — every
    # URL must come from images.pexels.com (CS-IMG-SRC-01) and the
    # build-time check `corporate_suite.E002` enforces this.
    # ─────────────────────────────────────────────────────────────
    "business-coaching": [
        # 0: hero — two people conversing in bright office meeting (1:1)
        "https://images.pexels.com/photos/7979456/pexels-photo-7979456.jpeg?auto=compress&cs=tinysrgb&w=1600",
        # 1: feature — man writing in notebook during indoor discussion
        "https://images.pexels.com/photos/5756579/pexels-photo-5756579.jpeg?auto=compress&cs=tinysrgb&w=1200",
        # 2: portrait-coach — woman with clipboard, minimalist indoor
        "https://images.pexels.com/photos/9064347/pexels-photo-9064347.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 3: portrait-coachee — confident businesswoman, arms crossed
        "https://images.pexels.com/photos/12934369/pexels-photo-12934369.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 4: detail — open notebook with pen on wooden desk beside laptop
        "https://images.pexels.com/photos/34601/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=800",
        # 5: ambient — warm home-office with plants and ambient light
        "https://images.pexels.com/photos/31236101/pexels-photo-31236101.jpeg?auto=compress&cs=tinysrgb&w=800",
    ],
    # ─────────────────────────────────────────────────────────────
    # business-stewardship — Phase X.4 design-orchestrator first
    # real candidate (Continua · 4th corporate-suite sibling · 1st
    # family-office variant · pass 1 IT · 2026-04-29). Pool follows
    # the Pexels-only contract from URL #1 (CS-IMG-SRC-01 · no
    # Unsplash carve-out) and the canonical 6-slot shape [hero,
    # feature, portrait, portrait, detail, ambient]. Direction per
    # `design-orchestrator/real-candidates/continua-build-brief.md
    # §4`: object-led hero (zero people · cluster's first), oak
    # partner-desk feature, 60s + 40s diverse stewards (closes the
    # Solaria 30sCx2 demographic gap), wax-seal letterhead detail
    # (replaces "documents" with stewardship object), slate
    # stairwell ambient (NOT bookshelf · Fiscus reservation · NOT
    # atrium · Pragma overlap · NOT warm meeting room · Solaria
    # adjacency). Cross-cluster grep clean against business-
    # corporate / business-fiscal / business-coaching at intake.
    # ─────────────────────────────────────────────────────────────
    # ─────────────────────────────────────────────────────────────
    # business-architecture — Phase X.5 Cornice (5th corporate-suite
    # sibling · 1st architecture-firm variant · 1st LF-2 occupant ·
    # 2026-04-30 · `phase-x5-cornice-a5-it-build`). Pool follows the
    # Pexels-only contract from URL #1 (CS-IMG-SRC-01) and the canonical
    # 6-slot shape [hero, feature, portrait, portrait, detail, ambient].
    # Direction per `factory/reports/corporate-suite/cornice-architettura/
    # planner-brief.md §4` and `factory/reports/imagery/cornice-architettura/
    # pool-selection.md`: object-led golden-hour Italian portico hero
    # (Bologna · zero people · architectural-shadow-line cinematic),
    # scale-model + drafting feature, senior-mid-career environmental
    # founding-architect portrait, mid-career collaboratore portrait,
    # architectural-blueprint detail (still-life NOT desk-task),
    # concrete-studio-wall ambient (NOT bookshelf · Fiscus reservation;
    # NOT slate-stairwell · Continua adjacency; NOT atrium · Pragma
    # overlap). Cross-cluster grep CLEAN against business-corporate /
    # business-fiscal / business-coaching / business-stewardship at
    # A.3 curator entry (2026-04-30 · 0/26 IDs overlap).
    # ─────────────────────────────────────────────────────────────
    # ─────────────────────────────────────────────────────────────
    # business-legale — Phase X.6 Causa (6th corporate-suite sibling ·
    # 1st evidence-led litigation-boutique variant · 2nd LF-2 occupant
    # after Cornice · 2026-05-03 · `phase-x6-causa-a5-it-build`).
    # Pool follows the Pexels-only contract from URL #1 (CS-IMG-SRC-01)
    # and the canonical 6-slot shape [hero, feature, portrait, portrait,
    # detail, ambient]. Direction per `factory/reports/causa/causa-
    # imagery-pack.md §1` and `factory/reports/imagery/causa-legale/
    # pool-selection.md`: empty courtroom interior hero (vertical timber
    # + bone walls · cool light · zero people · architectural · the
    # cluster's first interior chamber subject), open Italian law codex
    # feature (NOT trace paper / drafting tools), senior Cassazionista
    # in chambers portrait (60s · environmental · downward gaze on
    # codex · binding-triple per planner §5), mid-career associata
    # portrait (about-page only · demographic-distinct vs slot 2),
    # codex page macro detail (NOT architectural floor plan · NOT tax
    # form · NOT method-notebook · NOT wax-seal letterhead), vertical
    # wall of leather-bound codex shelves ambient (NOT marble stairway
    # with golden banister · Continua reservation; NOT concrete-studio-
    # wall-with-blueprints · Cornice reservation; NOT atrium · Pragma
    # overlap; NOT warm meeting room · Solaria adjacency). Cross-
    # cluster grep CLEAN against business-corporate / business-
    # architecture / business-fiscal / business-coaching / business-
    # stewardship at A.3 curator entry (2026-05-03 · 0/26 IDs overlap)
    # + reviewer-lgtm independent re-grep (`factory/reports/imagery/
    # causa-legale/reviewer-lgtm.md`).
    # ─────────────────────────────────────────────────────────────
    "business-legale": [
        # 0: hero — empty courtroom interior · vertical timber
        #    wainscoting + bone-painted walls · daylight through high
        #    clerestory windows · low-luminance judicial bench in mid-
        #    ground · zero people · cool register · Pavel Danilyuk
        #    (Pexels 17109985). The 1-second material read MUST be
        #    cool timber + bone, NOT warm mahogany (Continua) and NOT
        #    golden-hour stone (Cornice). The empty courtroom is the
        #    chamber where evidence is incardinated · pairs with the
        #    voice anchor `Ogni sentenza è un'evidenza incardinata`.
        "https://images.pexels.com/photos/17109985/pexels-photo-17109985.jpeg?auto=compress&cs=tinysrgb&w=1600",
        # 1: feature — open Italian law codex on a wooden chambers
        #    table · single tome · faint marginal annotations · cool
        #    natural light raking from the left · zero hands · zero
        #    laptop · EKATERINA BOLOVTSOVA (Pexels 6077368). Subject-
        #    class distinct from Cornice's architectural scale model
        #    on worktable (codex is text-on-paper · NOT model · NOT
        #    drafting tools · NOT trace paper) and from Continua's
        #    oak partner-desk feature (NOT mahogany · NOT correspondence
        #    · NOT wax-seal). Doubles as the planner-pre-cleared backup
        #    hero subject if slot 0 fails A.6 critique.
        "https://images.pexels.com/photos/6077368/pexels-photo-6077368.jpeg?auto=compress&cs=tinysrgb&w=1200",
        # 2: portrait — senior man (60s · greying hair · horn-rimmed
        #    eyeglasses · charcoal-grey three-piece suit · pen in hand)
        #    seated 3/4 toward camera at a chambers desk · open codice
        #    in mid-ground · vertical timber wainscoting and full
        #    leather-bound-codex shelf in soft-focus background · cool
        #    window-light · downward gaze on the codex page · working
        #    posture · Pavel Danilyuk (Pexels 8101948). The R-LF2-1
        #    binding triple (50s-or-senior + chambers-with-codices-mid-
        #    ground + environmental-NOT-studio-backdrop) cleared on
        #    this URL — the working posture (downward gaze + pen in
        #    hand) avoids the LinkedIn-headshot collapse. Founder
        #    identity locked at A.4 as Lorenzo Marchetti · masculine
        #    · 60s · Cassazionista dal 2003 (R-LF2-2 mitigation per
        #    Cornice's Marta-vs-Marco precedent · all 8 surfaces
        #    agree on first commit).
        "https://images.pexels.com/photos/8101948/pexels-photo-8101948.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 3: portrait — mid-career woman (30s-40s · dark hair pulled
        #    back · navy blazer over white shirt · pen in hand · stack
        #    of fascicoli at the right edge of frame) reading a codex
        #    page at a chambers desk · timber wainscoting + codex
        #    shelves in soft-focus · cool window-light · downward
        #    focused gaze · August de Richelieu (Pexels 6325985).
        #    Demographic anti-collision vs slot 2: different age
        #    (30s-40s vs 60s · planner-brief §5 R-LF2-2 mitigation),
        #    different gender (F vs M), different photographer. Slot 3
        #    appears on about.html team-grid only · home masthead is
        #    single-portrait per LF-2 L6.
        "https://images.pexels.com/photos/6325985/pexels-photo-6325985.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 4: detail — close-up of a codex page · marbled-paper edge
        #    visible at the top of frame · printed Italian legal text
        #    in serif typography · faint pencil annotations in the
        #    margin · single page · macro distance · still-life
        #    composition · zero hands · EKATERINA BOLOVTSOVA (Pexels
        #    6077381). Subject-class distinct from Cornice's
        #    architectural blueprint (text-and-paper · NOT technical
        #    line-work), from Fiscus's tax document (codex page · NOT
        #    730/SPA/BILANCIO), from Solaria's method-notebook (printed
        #    serif · NOT handwriting), and from Continua's wax-seal
        #    letterhead (codex page · NO seal · NO envelope).
        "https://images.pexels.com/photos/6077381/pexels-photo-6077381.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 5: ambient — vertical wall of leather-bound codex volumes ·
        #    oak shelving · cool natural light from the left · faint
        #    dust-line on the top shelf · zero people · zero ladder-
        #    rail-with-brass-fittings · zero metallic dominance ·
        #    Pixabay (Pexels 2128249). Material palette pairs with
        #    Causa's full-cool matte-on-matte palette (bottle-green +
        #    bone + obsidian) without fighting tokens. NOT slate
        #    stairwell with golden banister (Continua slot 5 verbatim
        #    reservation) · NOT concrete studio wall with blueprints
        #    (Cornice slot 5 reservation) · NOT regulation-bookshelf
        #    with explicit "JUSTICE" lettering (Fiscus slot 5
        #    reservation · `pexels-photo-159832` reserved for
        #    business-fiscal). Industrial-quiet active-practice library
        #    register, NOT museum-piece display.
        "https://images.pexels.com/photos/2128249/pexels-photo-2128249.jpeg?auto=compress&cs=tinysrgb&w=800",
    ],
    "business-architecture": [
        # 0: hero — sunlit corridor of an Italian portico in Bologna,
        #    stone columns and ceiling at golden hour, zero people,
        #    exterior architectural · Marcel Gierschick (Pexels 35715509).
        #    Subject-class distinct from Continua's library reading-room
        #    interior (exterior vs interior · stone vs mahogany ·
        #    golden-hour vs daylight-contemplative · architectural-shadow
        #    vs furniture-and-fireplace).
        "https://images.pexels.com/photos/35715509/pexels-photo-35715509.jpeg?auto=compress&cs=tinysrgb&w=1600",
        # 1: feature — architectural scale model on a designer's
        #    worktable with drawing tools and trace paper, raking
        #    natural light, zero people, zero monitor · Tima
        #    Miroshnichenko (Pexels 6614835). Workshop-editorial mood,
        #    process-as-proof framing.
        "https://images.pexels.com/photos/6614835/pexels-photo-6614835.jpeg?auto=compress&cs=tinysrgb&w=1200",
        # 2: portrait — senior architect (woman, white hair) reviewing
        #    blueprints with pen at environmental home-office desk
        #    · RDNE Stock project (Pexels 5915290). Binding triple
        #    (senior-mid-career + drafting tools mid-ground + environmental-
        #    NOT-studio-backdrop) cleared per planner-pre-cleared
        #    widening (prebuild-quick-checks Ω·3). Closes Solaria 30sCx2
        #    demographic gap on the senior side without invoking
        #    Continua's 60s + 40s pair.
        "https://images.pexels.com/photos/5915290/pexels-photo-5915290.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 3: portrait — mid-career architect (man, afro hair) reviewing
        #    project blueprints at office desk · Tima Miroshnichenko
        #    (Pexels 6615222). Demographic anti-collision vs slot 2
        #    (different age + gender + ethnicity).
        "https://images.pexels.com/photos/6615222/pexels-photo-6615222.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 4: detail — architectural blueprint / floor plan close-up,
        #    intricate technical lines, single sheet macro still life
        #    · Ivan S (Pexels 4458196). Subject-class distinct from
        #    Fiscus's tax-document detail and from Continua's wax-seal
        #    letterhead.
        "https://images.pexels.com/photos/4458196/pexels-photo-4458196.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 5: ambient — architectural design studio wall with concrete
        #    surface and pinned blueprints / models, industrial finish,
        #    zero people · Jesus Rivera (Pexels 36809500). Material
        #    palette pairs with Cornice's NEUTRAL primary + secondary
        #    (graphite + pietra-serena) without fighting tokens. NOT
        #    bookshelf (Fiscus) · NOT slate-stairwell (Continua) ·
        #    NOT atrium (Pragma) · NOT warm meeting room (Solaria).
        "https://images.pexels.com/photos/36809500/pexels-photo-36809500.jpeg?auto=compress&cs=tinysrgb&w=800",
    ],
    "business-stewardship": [
        # 0: hero — historic library room with rich wooden interiors,
        #    partner desk in foreground, fireplace + brass details, ZERO
        #    people · the cluster's first object-led hero. Curator-
        #    verified live at A.3 re-curate (2026-04-29) after the
        #    initial slot 0 candidate (Pexels 207658) returned a
        #    "BACK TO SCHOOL" Scrabble-tile composition; this is the
        #    binding slot 0.
        "https://images.pexels.com/photos/36093623/pexels-photo-36093623.jpeg?auto=compress&cs=tinysrgb&w=1600",
        # 1: feature — black classic desk with leather chair next to
        #    window in light study room (no people · oak feel · the
        #    feature slot is also referenced by the Compliance Officer
        #    portrait via build-brief §10 portrait_slot reframing note).
        "https://images.pexels.com/photos/7045772/pexels-photo-7045772.jpeg?auto=compress&cs=tinysrgb&w=1200",
        # 2: portrait — senior steward · woman · white hair · coral suit
        #    holding eyeglasses thoughtfully (institutional · 60s ·
        #    Eleonora Marchesi · solves Solaria 30sCx2 demographic gap
        #    on the senior side).
        "https://images.pexels.com/photos/5333750/pexels-photo-5333750.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 3: portrait — Family Officer · mature businessman, arms crossed
        #    in a modern office setting (40s · West African heritage ·
        #    Tomas Okafor · explicit visible age + gender + ethnicity
        #    variation vs slot 2).
        "https://images.pexels.com/photos/7841828/pexels-photo-7841828.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 4: detail — elegant letter with red wax seal on a wooden desk
        #    (suggesting traditional correspondence · NO tax documents ·
        #    NO laptop · the "stewardship object" archival framing).
        "https://images.pexels.com/photos/36824936/pexels-photo-36824936.jpeg?auto=compress&cs=tinysrgb&w=800",
        # 5: ambient — marble stairway with golden banister in a classic
        #    styled villa in daylight (NOT bookshelf · Fiscus reservation;
        #    NOT atrium · Pragma overlap; NOT warm meeting room · Solaria
        #    adjacency. "Building of substance" framing per the brief).
        "https://images.pexels.com/photos/6587827/pexels-photo-6587827.jpeg?auto=compress&cs=tinysrgb&w=800",
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
    # ─────────────────────────────────────────────────────────────
    # Per-archetype real-estate pools — Session 53 live rollout.
    # Zero URL overlap with each other and zero overlap with legacy
    # `real-estate` pool. Casa (mass-market) renders bright urban
    # apartments and attainable family homes. Villa (ultra-luxury)
    # renders cinematic editorial estates at golden hour and
    # architectural details.
    # ─────────────────────────────────────────────────────────────
    "realestate-casa": [
        # 0: hero — bright urban apartment building with balconies, daylight
        "https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
        # 1: feature — modern light living room, attainable family home
        "https://images.pexels.com/photos/1643383/pexels-photo-1643383.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
        # 2-5: listing tiles — kitchens, bedrooms, studios, family homes
        "https://images.pexels.com/photos/2724749/pexels-photo-2724749.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/1571463/pexels-photo-1571463.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
    ],
    "realestate-villa": [
        # 0: hero — cinematic luxury villa infinity pool at golden hour
        "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
        # 1: feature — editorial villa interior, double-height salon
        "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
        # 2-5: luxury property editorial — terrace, architectural detail, pool, library
        "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
        "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
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
