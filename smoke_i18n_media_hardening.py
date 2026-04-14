"""Session 36 — Live i18n & media hardening verification.

Post-hardening checks on the 7 `tier=published_live` templates:

  1. IT-only templates (pragma/elevate/chiara/pixel) must NOT render a
     language switcher. The <div class="mp-lang"> / <nav class="mp-lang">
     element must be absent on every page for these templates.
  2. Multilingual templates (cardio/derm/gusto) must still render a
     5-pill language switcher on every locale.
  3. Gusto must not expose the signature_video fake asset.
  4. Pixel must not expose the reel fake asset.
  5. Elevate must not expose the product_video fake asset, and should
     render the new demo invitation card with the booking CTA.
  6. The Big Buck Bunny sample URL must not appear anywhere in any
     rendered live-template page body.
  7. Gratuitous codec-style captions must not survive ("Demo · 2:14 · 1080p",
     "Reel · 1080p · 24 fps", "Play · 3:12", "Due fisse · 4K").
"""
from __future__ import annotations

import os
import sys

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketweb.settings")
django.setup()

from django.test import Client, override_settings

from apps.catalog.template_content import TEMPLATE_CONTENT

client = Client()

IT_ONLY: tuple[str, ...] = (
    # Session 40 closed Phase 2g3.3b — Pragma + Elevate now ship 5 locales.
)
MULTILINGUAL = (
    "cardio-studio-specialistico",
    "dermatologia-elite-roma",
    "gusto-fine-dining",
    # Session 37 — Chiara perfection pass: full 5-locale rollout.
    "chiara-portfolio-creativo",
    # Session 39 — Pixel perfection pass: full 5-locale rollout.
    "pixel-portfolio-fotografico",
    # Session 40 — Business i18n completion pass.
    "pragma-corporate-suite",
    "elevate-startup-landing",
)
CATEGORY = {
    "pragma-corporate-suite":      "business",
    "elevate-startup-landing":     "business",
    "chiara-portfolio-creativo":   "portfolio",
    "pixel-portfolio-fotografico": "portfolio",
    "cardio-studio-specialistico": "medical",
    "dermatologia-elite-roma":     "medical",
    "gusto-fine-dining":           "restaurant",
}

FORBIDDEN_MEDIA_TOKENS = (
    "ForBiggerBlazes.mp4",
    "commondatastorage.googleapis.com",
    "Demo · 2:14 · 1080p",
    "Reel · 1080p · 24 fps",
    "Play · 3:12",
    "Due fisse · 4K",
)


def body(url: str) -> tuple[int, str]:
    r = client.get(url)
    return r.status_code, r.content.decode("utf-8", errors="replace")


@override_settings(ALLOWED_HOSTS=["*"])
def run() -> int:
    failures: list[str] = []
    checks = 0

    # 1 — IT-only templates: no switcher anywhere
    for slug in IT_ONLY:
        cat = CATEGORY[slug]
        tree = TEMPLATE_CONTENT[slug]["it"]
        urls = [f"/templates/{cat}/{slug}/preview/"]
        urls += [
            f"/templates/{cat}/{slug}/preview/{p['slug']}/"
            for p in tree["pages"]
            if p["slug"] != "home"
        ]
        for url in urls:
            checks += 1
            status, html = body(url)
            if status != 200:
                failures.append(f"[IT-only switcher] {url} -> HTTP {status}")
                continue
            # CSS rules like `.mp-lang .mp-lang-list` live in the inline
            # <style> block on every page — that is structural, not content.
            # What must NOT appear is the actual switcher markup: the opening
            # element tag. We check for the two forms the skins emit:
            #   <div class="mp-lang" aria-label=...>  (specialist/business/portfolio)
            #   <nav class="mp-lang" aria-label=...>  (fine-dining)
            for marker in (
                '<div class="mp-lang"',
                '<nav class="mp-lang"',
                'class="mp-lang-pill',
            ):
                if marker in html:
                    failures.append(
                        f"[IT-only switcher] {url} still renders {marker!r}"
                    )
                    break

    # 2 — Multilingual templates: 5 pills on every locale
    for slug in MULTILINGUAL:
        cat = CATEGORY[slug]
        for loc in ("it", "en", "fr", "es", "ar"):
            qs = "" if loc == "it" else f"?lang={loc}"
            url = f"/templates/{cat}/{slug}/preview/{qs}"
            checks += 1
            status, html = body(url)
            if status != 200:
                failures.append(f"[multi switcher] {url} -> HTTP {status}")
                continue
            if (
                '<div class="mp-lang"' not in html
                and '<nav class="mp-lang"' not in html
            ):
                failures.append(f"[multi switcher] {url} missing switcher chrome")
            # Must include a pill for every locale
            for code in ("IT", "EN", "FR", "ES", "AR"):
                if f">{code}<" not in html:
                    failures.append(
                        f"[multi switcher] {url} missing {code} badge"
                    )
                    break

    # 3–7 — Media hygiene — scan home page of every template for forbidden tokens
    for slug, cat in CATEGORY.items():
        url = f"/templates/{cat}/{slug}/preview/"
        checks += 1
        status, html = body(url)
        if status != 200:
            failures.append(f"[media scan] {url} -> HTTP {status}")
            continue
        for token in FORBIDDEN_MEDIA_TOKENS:
            if token in html:
                failures.append(f"[media scan] {url} leaks '{token}'")

    # 8 — Elevate demo card renders
    url = "/templates/business/elevate-startup-landing/preview/"
    checks += 1
    _, html = body(url)
    if "sl-demo-card" not in html:
        failures.append("[elevate] demo invitation card not rendered")
    if "Prenota il walkthrough" not in html:
        failures.append("[elevate] demo primary CTA copy missing")

    # 9 — Pixel no lm-video / no reel
    url = "/templates/portfolio/pixel-portfolio-fotografico/preview/"
    checks += 1
    _, html = body(url)
    if "lm-video" in html or "cp-reel" in html:
        failures.append("[pixel] legacy video frame not fully removed")

    # 10 — Gusto no lm-video / no signature_video section
    url = "/templates/restaurant/gusto-fine-dining/preview/"
    checks += 1
    _, html = body(url)
    if "lm-video" in html or "fd-signature-video" in html:
        failures.append("[gusto] legacy video frame not fully removed")

    print(f"{checks - len(failures)}/{checks} hardening checks passed")
    for f in failures:
        print(f"  FAIL {f}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(run())
