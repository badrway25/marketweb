"""Session 37 — Chiara perfection-pass content marker sweep.

For each of Chiara's 5 locales, fetch the home page and verify a
locale-specific signature phrase rendered. Then verify the new
editorial-designer image IDs are in the rendered HTML (proves the
image swap took effect, not the old laptop stock photos). Then verify
Arabic RTL applies on `?lang=ar`.
"""
from __future__ import annotations

import os
import sys

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketweb.settings")
django.setup()

from django.test import Client, override_settings


client = Client()
SLUG = "chiara-portfolio-creativo"
CAT = "portfolio"

# (locale, signature phrase that MUST appear, language pill badge that MUST be active)
LOCALE_MARKERS = [
    ("it", "Forme che durano",         "IT"),
    ("en", "Forms that endure",        "EN"),
    ("fr", "qui durent",                "FR"),
    ("es", "que perduran",              "ES"),
    ("ar", "أشكال",                     "AR"),
]

# The 4 new editorial-designer image IDs that REPLACED the laptop stock photos.
NEW_IMAGE_IDS = [
    "photo-1611532736597-de2d4265fba3",  # Triennale (display type / editorial mag)
    "photo-1497633762265-9d179a990aa6",  # Adelphi (book series spines)
    "photo-1564399579883-451a5d44ec08",  # Querini (warm museum interior)
    "photo-1455390582262-044cdead277a",  # Velluti (fountain-pen on manuscript)
    "photo-1544717305-2782549b5136",     # Founder portrait (designer with editorial book)
]

# Old laptop stock IDs that MUST NOT appear anywhere.
OLD_LAPTOP_IDS = [
    "photo-1542744173-8e7e53415bb0",
    "photo-1559028012-481c04fa702d",
    "photo-1551434678-e076c223a692",
    "photo-1497366754035-f200968a6e72",
    "photo-1600880292203-757bb62b4baf",
]

# Hardcoded IT literals that MUST NO LONGER appear on non-IT pages.
# Note: some IT labels (Disciplina/Colophon/Metro) are valid words in other
# Romance languages too, so we only check IT-specific phrasings that have no
# crossover in EN/FR/ES.
IT_LITERALS_LIFTED = [
    "Tutto l'archivio",
    ">Equipe<",            # IT spelling; FR uses "Équipe" with accent
    "Sintesi del progetto",
    "Deliverable consegnati",
    "Cosa abbiamo prodotto",
    ">Sequenza<",
    "Durata indicativa",
    ">Indirizzo<",
    ">Ingresso<",
    ">Orari<",
]


def body(url: str) -> tuple[int, str]:
    r = client.get(url)
    return r.status_code, r.content.decode("utf-8", errors="replace")


@override_settings(ALLOWED_HOSTS=["*"])
def run() -> int:
    failures: list[str] = []
    checks = 0

    # 1 — Each locale renders its own signature phrase + active language pill
    for loc, phrase, badge in LOCALE_MARKERS:
        qs = "" if loc == "it" else f"?lang={loc}"
        url = f"/templates/{CAT}/{SLUG}/preview/{qs}"
        checks += 1
        status, html = body(url)
        if status != 200:
            failures.append(f"[{loc} render] {url} -> HTTP {status}")
            continue
        if phrase not in html:
            failures.append(f"[{loc} render] {url} missing signature phrase {phrase!r}")
        # Active pill marker
        if f">{badge}<" not in html:
            failures.append(f"[{loc} render] {url} missing pill badge {badge!r}")

    # 2 — RTL marker on ?lang=ar
    checks += 1
    _, html = body(f"/templates/{CAT}/{SLUG}/preview/?lang=ar")
    if 'dir="rtl"' not in html:
        failures.append("[AR RTL] home page does not declare dir=\"rtl\"")
    if "Amiri" not in html and "Noto Kufi Arabic" not in html:
        failures.append("[AR RTL] Arabic font stack not loaded on AR page")

    # 3 — New editorial images present + old laptop IDs absent
    for loc in ("it", "en", "fr", "es", "ar"):
        qs = "" if loc == "it" else f"?lang={loc}"
        url = f"/templates/{CAT}/{SLUG}/preview/{qs}"
        checks += 1
        _, html = body(url)
        new_present = sum(1 for img_id in NEW_IMAGE_IDS if img_id in html)
        if new_present < 4:  # at least 4/5 (founder lives on /studio not home)
            failures.append(
                f"[image swap {loc}] only {new_present}/5 new editorial image IDs present"
            )
        for old in OLD_LAPTOP_IDS:
            if old in html:
                failures.append(
                    f"[image swap {loc}] OLD laptop stock {old} still in HTML"
                )

    # 4 — Founder portrait check on /studio for each locale
    for loc in ("it", "en", "fr", "es", "ar"):
        qs = "" if loc == "it" else f"?lang={loc}"
        url = f"/templates/{CAT}/{SLUG}/preview/studio/{qs}"
        checks += 1
        _, html = body(url)
        if "photo-1544717305-2782549b5136" not in html:
            failures.append(f"[founder image {loc}] new portrait ID missing on /studio")
        if "photo-1600880292203-757bb62b4baf" in html:
            failures.append(
                f"[founder image {loc}] old businessperson portrait still present"
            )

    # 5 — IT literals MUST NOT appear on non-IT pages (4 pages × 4 locales)
    for loc in ("en", "fr", "es", "ar"):
        for page in ("", "lavoro/", "lavoro/triennale-milano-catalogo-2025/",
                     "processo/", "contatti/"):
            qs = f"?lang={loc}"
            url = f"/templates/{CAT}/{SLUG}/preview/{page}{qs}"
            checks += 1
            _, html = body(url)
            for lit in IT_LITERALS_LIFTED:
                if lit in html:
                    failures.append(
                        f"[IT-leak {loc}] {url} leaks {lit!r} (lift incomplete)"
                    )
                    break

    # 6 — All routes 200 across 5 locales (sanity)
    inner_pages = ["", "studio/", "lavoro/", "processo/", "contatti/",
                   "lavoro/triennale-milano-catalogo-2025/",
                   "lavoro/adelphi-collana-carta-bianca/",
                   "lavoro/querini-stampalia-segnaletica/"]
    for loc in ("it", "en", "fr", "es", "ar"):
        qs = "" if loc == "it" else f"?lang={loc}"
        for p in inner_pages:
            url = f"/templates/{CAT}/{SLUG}/preview/{p}{qs}"
            checks += 1
            status, _ = body(url)
            if status != 200:
                failures.append(f"[route] {url} -> HTTP {status}")

    print(f"{checks - len(failures)}/{checks} chiara perfection checks passed")
    for f in failures:
        print(f"  FAIL {f}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(run())
