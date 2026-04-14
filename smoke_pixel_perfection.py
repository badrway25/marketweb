"""Session 39 — Pixel perfection-pass content marker sweep.

For each of Pixel's 5 locales, fetch the home page and verify a locale-
specific signature phrase rendered. Then verify RTL applies on ?lang=ar,
the Noto Naskh/Kufi Arabic font stack loaded, and no IT chrome literals
leaked onto non-IT pages. Finally sweep every route across 5 locales.
"""
from __future__ import annotations

import os
import sys

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketweb.settings")
django.setup()

from django.test import Client, override_settings


client = Client()
SLUG = "pixel-portfolio-fotografico"
CAT = "portfolio"

# (locale, signature phrase that MUST appear, language pill badge)
# Use the nav-CTA chrome literal — each locale authors it distinctly and
# it appears on every inner page, so it's a reliable presence marker.
LOCALE_MARKERS = [
    ("it", "Apri conversazione",     "IT"),
    ("en", "Open a conversation",    "EN"),
    ("fr", "Ouvrir une conversation","FR"),
    ("es", "Abrir conversación",     "ES"),
    ("ar", "افتح محادثة",            "AR"),
]

# Hardcoded IT chrome literals that WERE lifted this session — they must
# NOT appear on non-IT locale pages. (Common Italian nouns that happen to
# be valid FR/ES words like "Disciplina"/"Galleria" are excluded — we check
# multi-word phrases that are unambiguously Italian.)
IT_LITERALS_LIFTED = [
    "Apri conversazione",   # nav_cta
    "[ apri serie ]",       # serie card arrow
    "[ Edizione ]",         # series_detail edition marker
    "Per commissione",      # kit availability value
    ">Indirizzo<",          # studio-card address row label (strong tag)
    ">Ingresso<",           # studio-card entrance row label
]

# Pixel-specific cinematic-photographer image IDs that must appear on the
# home + about + series surfaces (proves the curated imagery pool took
# effect and nothing regressed to generic stock).
PIXEL_IMAGE_IDS = [
    "photo-1517021897933-0e0319cfbc28",  # hero mountain dusk
    "photo-1518837695005-2083093ee35b",  # porto-vecchio frame
    "photo-1568605114967-8130f3a36994",  # stone architecture
    "photo-1545239351-1141bd82e8a6",     # portrait cover
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
        if f">{badge}<" not in html:
            failures.append(f"[{loc} render] {url} missing pill badge {badge!r}")

    # 2 — RTL marker on ?lang=ar + Arabic font stack loaded
    checks += 1
    _, html = body(f"/templates/{CAT}/{SLUG}/preview/?lang=ar")
    if 'dir="rtl"' not in html:
        failures.append("[AR RTL] home page does not declare dir=\"rtl\"")
    if "Noto Naskh Arabic" not in html and "Noto Kufi Arabic" not in html:
        failures.append("[AR RTL] Arabic font stack not loaded on AR page")

    # 3 — Pixel cinematic-photographer image IDs present on home
    for loc in ("it", "en", "fr", "es", "ar"):
        qs = "" if loc == "it" else f"?lang={loc}"
        url = f"/templates/{CAT}/{SLUG}/preview/{qs}"
        checks += 1
        _, html = body(url)
        present = sum(1 for img_id in PIXEL_IMAGE_IDS if img_id in html)
        if present < 2:  # hero + at least one filmstrip cover
            failures.append(
                f"[image sweep {loc}] only {present}/4 Pixel image IDs present"
            )

    # 4 — IT literals must NOT appear on non-IT locale pages
    inner_pages = [
        "",
        "serie/",
        "biografia/",
        "pubblicazioni/",
        "contatti/",
        "serie/porto-vecchio-trieste/",
    ]
    for loc in ("en", "fr", "es", "ar"):
        for page in inner_pages:
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

    # 5 — All routes 200 across 5 locales (sanity)
    all_inner = inner_pages + [
        "serie/case-di-pietra-puglia/",
        "serie/ritratti-del-po/",
    ]
    for loc in ("it", "en", "fr", "es", "ar"):
        qs = "" if loc == "it" else f"?lang={loc}"
        for p in all_inner:
            url = f"/templates/{CAT}/{SLUG}/preview/{p}{qs}"
            checks += 1
            status, _ = body(url)
            if status != 200:
                failures.append(f"[route] {url} -> HTTP {status}")

    # 6 — Five language pills actually render on every locale page
    for loc in ("it", "en", "fr", "es", "ar"):
        qs = "" if loc == "it" else f"?lang={loc}"
        url = f"/templates/{CAT}/{SLUG}/preview/{qs}"
        checks += 1
        _, html = body(url)
        for pill in ("IT", "EN", "FR", "ES", "AR"):
            if f">{pill}<" not in html:
                failures.append(
                    f"[switcher {loc}] pill {pill} not rendered on {url}"
                )

    print(f"{checks - len(failures)}/{checks} pixel perfection checks passed")
    for f in failures:
        print(f"  FAIL {f}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(run())
