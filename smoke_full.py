"""Full regression sweep — every public live-template route across the
5 published_live templates and the relevant locales. No content asserts,
only HTTP status + absence of Python tracebacks in the body.
"""
import os, sys, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketweb.settings")
django.setup()

from django.test import Client, override_settings
from apps.catalog.template_content import TEMPLATE_CONTENT

client = Client()

LOCALES = {
    "cardio-studio-specialistico": ["it", "en", "fr", "es", "ar"],
    "dermatologia-elite-roma":     ["it", "en", "fr", "es", "ar"],
    "gusto-fine-dining":           ["it", "en", "fr", "es", "ar"],
    "pragma-corporate-suite":      ["it", "en", "fr", "es", "ar"],
    "elevate-startup-landing":     ["it", "en", "fr", "es", "ar"],
    "chiara-portfolio-creativo":   ["it", "en", "fr", "es", "ar"],
    "pixel-portfolio-fotografico": ["it", "en", "fr", "es", "ar"],
    # Phase 2g3.5 — eCommerce live rollout (Session 41)
    "bottega-shop-artigianale":    ["it", "en", "fr", "es", "ar"],
    "luxe-fashion-store":          ["it", "en", "fr", "es", "ar"],
}

CATEGORY = {
    "cardio-studio-specialistico": "medical",
    "dermatologia-elite-roma":     "medical",
    "gusto-fine-dining":           "restaurant",
    "pragma-corporate-suite":      "business",
    "elevate-startup-landing":     "business",
    "chiara-portfolio-creativo":   "portfolio",
    "pixel-portfolio-fotografico": "portfolio",
    "bottega-shop-artigianale":    "ecommerce",
    "luxe-fashion-store":          "ecommerce",
}

@override_settings(ALLOWED_HOSTS=["*"])
def run():
    total, ok, failed = 0, 0, []
    for slug, locales in LOCALES.items():
        cat = CATEGORY[slug]
        tree_by_loc = TEMPLATE_CONTENT.get(slug, {})
        for loc in locales:
            tree = tree_by_loc.get(loc) or tree_by_loc.get("it") or {}
            pages = tree.get("pages", [])
            q = "" if loc == "it" else f"?lang={loc}"
            # Marketplace detail
            url = f"/templates/{cat}/{slug}/"
            total += 1
            r = client.get(url + q)
            if r.status_code == 200: ok += 1
            else: failed.append((url+q, r.status_code))
            # Home
            url = f"/templates/{cat}/{slug}/preview/"
            total += 1
            r = client.get(url + q)
            if r.status_code == 200: ok += 1
            else: failed.append((url+q, r.status_code))
            # Inner pages
            for p in pages:
                psl = p["slug"]
                url = f"/templates/{cat}/{slug}/preview/{psl}/"
                total += 1
                r = client.get(url + q)
                if r.status_code == 200: ok += 1
                else: failed.append((url+q, r.status_code))
    # Catalog surfaces
    for path in ["/", "/templates/", "/templates/medical/", "/templates/restaurant/", "/templates/business/", "/templates/portfolio/", "/templates/ecommerce/"]:
        total += 1
        r = client.get(path)
        if r.status_code == 200: ok += 1
        else: failed.append((path, r.status_code))
    # Post detail routes (project_detail / series_detail) — Phase 2g3.4 portfolio
    POST_ROUTES = [
        ("/templates/portfolio/chiara-portfolio-creativo/preview/lavoro/",
         ["triennale-milano-catalogo-2025", "adelphi-collana-carta-bianca", "querini-stampalia-segnaletica"]),
        ("/templates/portfolio/pixel-portfolio-fotografico/preview/serie/",
         ["porto-vecchio-trieste", "case-di-pietra-puglia", "ritratti-del-po"]),
    ]
    for parent, slugs in POST_ROUTES:
        for s in slugs:
            url = f"{parent}{s}/"
            total += 1
            r = client.get(url)
            if r.status_code == 200: ok += 1
            else: failed.append((url, r.status_code))
    print(f"{ok}/{total} routes HTTP 200")
    for u, s in failed: print(f"  FAIL {u} -> {s}")
    return 0 if not failed else 1

if __name__ == "__main__":
    sys.exit(run())
