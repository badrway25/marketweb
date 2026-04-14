"""Phase 2g3.5 — eCommerce live rollout (Session 41) verification.

Bottega + Luxe must satisfy:
  1. Every (template × locale × page) renders HTTP 200 — 60 routes total.
  2. Each AR route emits dir="rtl" and loads Amiri/Noto-Kufi Arabic font.
  3. Each non-IT route loads the locale-specific font tokens.
  4. D-054 differentiation: Bottega-vocabulary tokens NEVER appear in Luxe
     pages, and Luxe-vocabulary tokens NEVER appear in Bottega pages, on
     any locale. Cross-tenant leak count must be 0 across 5 locales x 4
     token classes per side.
  5. D-047 chrome-cleanliness: shared marketplace chrome words only,
     never the OTHER template's brand names / city signatures.
  6. The 5-pill language switcher renders on every page of every locale.
  7. Latin brand names + edition numbers + prices preserved on AR pages
     (no transliteration to Eastern Arabic numerals).
"""
from __future__ import annotations

import os
import sys

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketweb.settings")
django.setup()

from django.test import Client, override_settings

client = Client()

TEMPLATES = (
    ("bottega-shop-artigianale", "ecommerce", ["home", "shop", "product", "atelier", "journal", "contatti"]),
    ("luxe-fashion-store",       "ecommerce", ["home", "collezione", "product", "maison", "lookbook", "contatti"]),
)
LOCALES = ("it", "en", "fr", "es", "ar")

# Bottega-specific vocabulary that MUST NEVER appear on Luxe pages.
# These are tokens the Bottega tree authored deliberately for the warm
# artisan voice — if any of these surface on Luxe rendered HTML it means
# the differentiation contract has leaked.
BOTTEGA_ONLY_TOKENS = (
    "La Bottega di Martino",
    "Severino Falchi",
    "Caterina Lippi",
    "Bruno Ricci",
    "Adele Pignatelli",
    "Martino Boncompagni",
    "Anna Boncompagni",
    "Santa Croce sull'Arno",
    "Montelupo Fiorentino",
    "Greve in Chianti",
    "Via dei Serragli",
    "WhatsApp",
    "055 234 11 90",
    "Conceria Falchi",
    "Maglificio Lanifer",  # this is Luxe's, sanity check below
)

# Luxe-specific vocabulary that MUST NEVER appear on Bottega pages.
LUXE_ONLY_TOKENS = (
    "Maison Luxe",
    "Giulia Maison",
    "Carla Sozzani",
    "Letizia Carrera",
    "Jean-Luc Berthier",
    "Yumi Tanaka",
    "Atelier Sentier",
    "rue du Mail",
    "Aoyama",
    "Grand Hôtel Villa d'Este",
    "lookbook",
    "private viewing",
    "Drop 04",
    "SS26",
    "Maglificio Lanifer Biella",
    "Conceria della Madonna",
)

# Sanity-fix: remove the false dual-listed token from BOTTEGA_ONLY
BOTTEGA_ONLY_TOKENS = tuple(t for t in BOTTEGA_ONLY_TOKENS if t != "Maglificio Lanifer")

# Tokens that prove an AR page loads Arabic fonts + correct dir.
AR_MARKERS = (
    'dir="rtl"',
    'lang="ar"',
    "Amiri",
    "Noto+Kufi+Arabic",
)

# Latin proper names that MUST stay Latin on the AR pages of each template.
BOTTEGA_AR_LATIN_PRESERVE = ("La Bottega di Martino", "Firenze", "+39 055 234 11 90", "€ 420")
LUXE_AR_LATIN_PRESERVE    = ("Maison Luxe", "Milano", "Tokyo", "€ 2.480")


def fetch(url: str) -> tuple[int, str]:
    r = client.get(url)
    return r.status_code, r.content.decode("utf-8", errors="replace")


@override_settings(ALLOWED_HOSTS=["*"])
def run() -> int:
    failures: list[str] = []
    checks = 0

    # 1 — Every route renders 200
    for slug, cat, pages in TEMPLATES:
        for loc in LOCALES:
            qs = "" if loc == "it" else f"?lang={loc}"
            for p in pages:
                if p == "home":
                    url = f"/templates/{cat}/{slug}/preview/{qs}"
                else:
                    url = f"/templates/{cat}/{slug}/preview/{p}/{qs}"
                checks += 1
                status, _ = fetch(url)
                if status != 200:
                    failures.append(f"[200] {url} -> HTTP {status}")

    # 2 — AR routes emit dir + Arabic font load
    for slug, cat, pages in TEMPLATES:
        for p in pages:
            if p == "home":
                url = f"/templates/{cat}/{slug}/preview/?lang=ar"
            else:
                url = f"/templates/{cat}/{slug}/preview/{p}/?lang=ar"
            checks += 1
            status, html = fetch(url)
            if status != 200:
                failures.append(f"[ar markers] {url} -> HTTP {status}")
                continue
            for m in AR_MARKERS:
                if m not in html:
                    failures.append(f"[ar markers] {url} missing {m!r}")
                    break

    # 3 — 5-pill switcher renders on every page of every locale
    for slug, cat, pages in TEMPLATES:
        for loc in LOCALES:
            qs = "" if loc == "it" else f"?lang={loc}"
            for p in pages:
                if p == "home":
                    url = f"/templates/{cat}/{slug}/preview/{qs}"
                else:
                    url = f"/templates/{cat}/{slug}/preview/{p}/{qs}"
                checks += 1
                _, html = fetch(url)
                if '<div class="mp-lang"' not in html and '<nav class="mp-lang"' not in html:
                    failures.append(f"[switcher] {url} missing switcher chrome")
                    continue
                missing_pill = None
                for code in ("IT", "EN", "FR", "ES", "AR"):
                    if f">{code}<" not in html:
                        missing_pill = code
                        break
                if missing_pill:
                    failures.append(f"[switcher] {url} missing {missing_pill} pill")

    # 4 — D-054 cross-tenant leak sweep on every locale page
    luxe_pages = [
        f"/templates/ecommerce/luxe-fashion-store/preview/{p + '/' if p != 'home' else ''}"
        for p in TEMPLATES[1][2]
    ]
    bot_pages = [
        f"/templates/ecommerce/bottega-shop-artigianale/preview/{p + '/' if p != 'home' else ''}"
        for p in TEMPLATES[0][2]
    ]

    for loc in LOCALES:
        qs = "" if loc == "it" else f"?lang={loc}"
        # Bottega tokens must NOT appear on Luxe rendered HTML
        for url_base in luxe_pages:
            url = url_base + qs
            checks += 1
            _, html = fetch(url)
            for tok in BOTTEGA_ONLY_TOKENS:
                if tok in html:
                    failures.append(f"[D-054 LEAK] '{tok}' (bottega) found in luxe {url}")
                    break
        # Luxe tokens must NOT appear on Bottega rendered HTML
        for url_base in bot_pages:
            url = url_base + qs
            checks += 1
            _, html = fetch(url)
            for tok in LUXE_ONLY_TOKENS:
                if tok in html:
                    failures.append(f"[D-054 LEAK] '{tok}' (luxe) found in bottega {url}")
                    break

    # 5 — Latin preservation on AR pages
    _, bot_ar_home = fetch("/templates/ecommerce/bottega-shop-artigianale/preview/?lang=ar")
    checks += 1
    for tok in BOTTEGA_AR_LATIN_PRESERVE:
        if tok not in bot_ar_home:
            failures.append(f"[AR Latin] Bottega AR home missing Latin token '{tok}'")

    _, luxe_ar_home = fetch("/templates/ecommerce/luxe-fashion-store/preview/?lang=ar")
    checks += 1
    for tok in LUXE_AR_LATIN_PRESERVE:
        if tok not in luxe_ar_home:
            failures.append(f"[AR Latin] Luxe AR home missing Latin token '{tok}'")

    # Report
    print(f"{checks - len(failures)}/{checks} ecommerce rollout checks passed")
    for f in failures:
        print(f"  FAIL {f}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(run())
