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
    # Phase 2g3.6 — Restaurant live-completion (Session 48)
    "sapore-trattoria-pizzeria":   ["it", "en", "fr", "es", "ar"],
    "brace-street-food-lab":       ["it", "en", "fr", "es", "ar"],
    # Phase 2g3.6f — Agency live rollout (Session 49)
    "vertex-creative-agency":      ["it", "en", "fr", "es", "ar"],
    "aura-digital-studio":         ["it", "en", "fr", "es", "ar"],
    # Phase 2g3.2 — Medical second wave live rollout (Session 51)
    "salute-studio-medico":        ["it", "en", "fr", "es", "ar"],
    "benessere-centro-olistico":   ["it", "en", "fr", "es", "ar"],
    "famiglia-pediatria":          ["it", "en", "fr", "es", "ar"],
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
    "sapore-trattoria-pizzeria":   "restaurant",
    "brace-street-food-lab":       "restaurant",
    "vertex-creative-agency":      "agency",
    "aura-digital-studio":         "agency",
    # Phase 2g3.2 — Medical second wave
    "salute-studio-medico":        "medical",
    "benessere-centro-olistico":   "medical",
    "famiglia-pediatria":          "medical",
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
    for path in ["/", "/templates/", "/templates/medical/", "/templates/restaurant/", "/templates/business/", "/templates/portfolio/", "/templates/ecommerce/", "/templates/agency/"]:
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
        # Agency project_detail routes (Session 49)
        ("/templates/agency/vertex-creative-agency/preview/lavori/",
         ["fondazione-prada-rebrand", "adelphi-collana-narrativa", "maison-gentiluomo-manuale"]),
        ("/templates/agency/aura-digital-studio/preview/lavori/",
         ["casavo-retention-rework", "fastweb-plus-dashboard", "soldo-corporate-onboarding"]),
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
