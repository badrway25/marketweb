"""Smoke test for the Premium Forms Polish session (Session 33).

Exercises every form page on the 5 published_live templates, across the
locales each template supports. Asserts the new .lf-* primitives show
up in the rendered HTML, and that no new 5xx / template error leaks.
"""
import os, sys, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketweb.settings")
django.setup()

from django.test import Client, override_settings

client = Client()

PAGES = [
    # (slug, cat, page-kind URL, form class hint present in output)
    # Medical specialist — cardio + derm share archetype, both have
    # contact (6-field) and appointment (8-field + upload)
    ("cardio-studio-specialistico",    "medical", "contatti",        "sp-form"),
    ("cardio-studio-specialistico",    "medical", "richiedi-visita", "sp-form-band"),
    ("dermatologia-elite-roma",        "medical", "contatti",        "sp-form"),
    ("dermatologia-elite-roma",        "medical", "richiedi-visita", "sp-form-band"),
    # Gusto fine-dining reservations (8-field)
    ("gusto-fine-dining",              "restaurant", "prenota",      "fd-form-band"),
    # Pragma corporate-suite contact (9-field + upload)
    ("pragma-corporate-suite",         "business",   "contatti",     "cs-form"),
    # Elevate startup-saas demo (8-field + upload)
    ("elevate-startup-landing",        "business",   "demo",         "sl-form"),
]

LOCALES_BY_TEMPLATE = {
    "cardio-studio-specialistico":    ["it", "en", "fr", "es", "ar"],
    "dermatologia-elite-roma":        ["it", "en", "fr", "es", "ar"],
    "gusto-fine-dining":              ["it", "en", "fr", "es", "ar"],
    "pragma-corporate-suite":         ["it"],
    "elevate-startup-landing":        ["it"],
}

# Features the new polish must expose
MARKER_LF_PRIMITIVE = 'class="lf-'       # shared prim wrapper
MARKER_LF_SELECT    = 'class="lf-select"' # custom listbox
MARKER_LF_FORMS_CSS = 'live-forms.css'
MARKER_LF_FORMS_JS  = 'live-forms.js'

@override_settings(ALLOWED_HOSTS=["*"])
def run():
    total = 0
    ok = 0
    errors = []
    missing_primitives = []
    for slug, cat, page_kind, _hint in PAGES:
        for loc in LOCALES_BY_TEMPLATE[slug]:
            url = f"/templates/{cat}/{slug}/preview/{page_kind}/"
            q = "" if loc == "it" else f"?lang={loc}"
            total += 1
            try:
                resp = client.get(url + q)
            except Exception as e:
                errors.append((url+q, f"EXC: {e!r}"))
                continue
            if resp.status_code != 200:
                errors.append((url+q, f"HTTP {resp.status_code}"))
                continue
            body = resp.content.decode("utf-8", "replace")
            # Assert the form polish markers show up for every form page
            if MARKER_LF_PRIMITIVE not in body:
                missing_primitives.append((url+q, "no .lf-* primitives"))
            if MARKER_LF_FORMS_CSS not in body:
                missing_primitives.append((url+q, "live-forms.css not linked"))
            if MARKER_LF_FORMS_JS not in body:
                missing_primitives.append((url+q, "live-forms.js not linked"))
            # Every form page must carry at least ONE custom listbox except
            # the medical contact form which is select-free.
            if page_kind != "contatti" or slug in {"pragma-corporate-suite", "elevate-startup-landing"}:
                if MARKER_LF_SELECT not in body:
                    missing_primitives.append((url+q, "no .lf-select"))
            ok += 1

    print(f"Form routes: {ok}/{total} HTTP 200")
    if errors:
        print("ERRORS:")
        for u, e in errors: print(f"  {u} -> {e}")
    if missing_primitives:
        print("MISSING PRIMITIVES:")
        for u, m in missing_primitives: print(f"  {u} -> {m}")
    if not errors and not missing_primitives:
        print("ALL FORM POLISH CHECKS GREEN")
        return 0
    return 1 if errors else 2

if __name__ == "__main__":
    sys.exit(run())
