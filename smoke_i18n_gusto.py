"""Smoke test for Gusto fine-dining i18n/RTL rollout (Session 29).

Exercises every Gusto route in all 5 locales, plus regression checks
on cardio + derm in a representative locale each.

Run from project root:
    python smoke_i18n_gusto.py
"""
import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketweb.settings")
django.setup()

from django.conf import settings  # noqa: E402

if "testserver" not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS = list(settings.ALLOWED_HOSTS) + ["testserver"]

from django.test import Client  # noqa: E402

c = Client()
passed = 0
failed = 0
failures: list[tuple[str, int, str]] = []


def hit(url: str, label: str, expect: int = 200):
    global passed, failed
    resp = c.get(url)
    status = resp.status_code
    if status == expect:
        passed += 1
        print(f"  OK {label}  [{status}]  {url}")
    else:
        failed += 1
        failures.append((label, status, url))
        print(f"  FAIL {label}  [{status} expected {expect}]  {url}")


def banner(text: str):
    print(f"\n{'=' * 72}\n{text}\n{'=' * 72}")


GUSTO_CAT = "restaurant"
GUSTO_SLUG = "gusto-fine-dining"
GUSTO_PAGES = ["filosofia", "menu", "atmosfera", "diario", "prenota"]
GUSTO_POST_SLUG = "menu-autunno-26"
LOCALES = ["it", "en", "fr", "es", "ar"]


banner("GUSTO i18n — 5 locales × 7 routes = 35 routes")
for loc in LOCALES:
    suffix = "" if loc == "it" else f"?lang={loc}"
    print(f"\n--- locale = {loc} ---")
    hit(f"/templates/{GUSTO_CAT}/{GUSTO_SLUG}/preview/{suffix}", f"home [{loc}]")
    for p in GUSTO_PAGES:
        hit(f"/templates/{GUSTO_CAT}/{GUSTO_SLUG}/preview/{p}/{suffix}", f"{p} [{loc}]")
    hit(
        f"/templates/{GUSTO_CAT}/{GUSTO_SLUG}/preview/diario/{GUSTO_POST_SLUG}/{suffix}",
        f"diario/{GUSTO_POST_SLUG} [{loc}]",
    )

banner("CARDIO regression — full locale matrix")
CARDIO_CAT = "medical"
CARDIO_SLUG = "cardio-studio-specialistico"
CARDIO_PAGES = ["studio", "visite", "medici", "pubblicazioni", "contatti", "richiedi-visita"]
for loc in LOCALES:
    suffix = "" if loc == "it" else f"?lang={loc}"
    print(f"\n--- cardio {loc} ---")
    hit(f"/templates/{CARDIO_CAT}/{CARDIO_SLUG}/preview/{suffix}", f"cardio home [{loc}]")
    hit(
        f"/templates/{CARDIO_CAT}/{CARDIO_SLUG}/preview/contatti/{suffix}",
        f"cardio contatti [{loc}]",
    )

banner("DERM regression — spot check")
DERM_SLUG = "dermatologia-elite-roma"
for loc in LOCALES:
    suffix = "" if loc == "it" else f"?lang={loc}"
    hit(f"/templates/medical/{DERM_SLUG}/preview/{suffix}", f"derm home [{loc}]")

banner("NEGATIVE / FALLBACK checks")
hit(f"/templates/{GUSTO_CAT}/{GUSTO_SLUG}/preview/?lang=zz", "unknown locale -> IT fallback")
hit(f"/templates/{GUSTO_CAT}/{GUSTO_SLUG}/preview/?lang=", "empty lang -> IT fallback")

banner(f"RESULTS — passed {passed} · failed {failed}")
if failed:
    print("\nFailures:")
    for label, status, url in failures:
        print(f"  {status}  {label}  {url}")
    sys.exit(1)
else:
    sys.exit(0)
