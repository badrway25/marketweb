# Corporate-suite shared `case-studies` parent-slug fix — browser verification

**Date:** 2026-04-29
**Scope:** Shared cluster-level fix for `templates/live_templates/business/corporate-suite/home.html` line 660
**Affects:** All corporate-suite enrollees — Pragma, Solaria, Fiscus, Continua
**Branch:** `phase-x4-corporate-suite-case-parent-fix`
**Tier safety:** zero visual / identity / motion changes — chrome behavior only

---

## 1. Issue

`home.html:660` previously hardcoded the case-studies parent page slug to `'case-studies'` when generating the URL for each post in the home preview-band:

```django
href="{% url 'catalog:live_template_post' template.category.slug template.slug 'case-studies' post.slug %}…"
```

That literal slug exists only for **Pragma**. The other three corporate-suite enrollees use a per-archetype parent slug:

| Template | `case_study_list` page slug |
|---|---|
| Pragma | `case-studies` |
| Continua | `mandati` |
| Solaria | `casi` |
| Fiscus | `casi-seguiti` |

For Continua / Solaria / Fiscus the home-band hrefs therefore pointed at non-existent paths (e.g. `/preview/case-studies/famiglia-a-…/` for Continua), so all 3–4 case-study links from each home returned **404**.

Documented in memory as: *"Pre-existing `home.html:660` hardcoded `'case-studies'` parent slug … affects Fiscus/Solaria/Continua but not Pragma — held for cluster-level follow-up."*

---

## 2. Fix

### 2.1 Strategy

Mirror the existing `blog_parent_slug` precedent in `LiveTemplateView.get_context_data` and look up the parent slug dynamically from the page list (`kind == 'case_study_list'`). The chrome template then references the resolved slug instead of a literal.

This is the smallest correct change:

* **No new fields** in template-content registries (each archetype already declares its `case_study_list` page).
* **No visual change** — only the URL resolver argument changes.
* **No identity change** — chrome layout, copy, motion all untouched.
* **Single shared edit** in `home.html` — consistent with how `blog_parent_slug` is consumed in blog chrome.

### 2.2 Files changed

```
apps/catalog/views.py
templates/live_templates/business/corporate-suite/home.html
```

#### `apps/catalog/views.py`

Added a `cases_parent_slug` context entry next to the existing `blog_parent_slug` resolver:

```python
ctx["cases_parent_slug"] = next(
    (p["slug"] for p in self.content["pages"] if p["kind"] == "case_study_list"),
    None,
)
```

Falls back to `None` for templates without a `case_study_list` page (no corporate-suite enrollee is in that bucket today; the fallback is just defensive).

#### `templates/live_templates/business/corporate-suite/home.html` line 660

```diff
- <a class="row" href="{% url 'catalog:live_template_post' template.category.slug template.slug 'case-studies' post.slug %}…">
+ <a class="row" href="{% url 'catalog:live_template_post' template.category.slug template.slug cases_parent_slug post.slug %}…">
```

`case_study_list.html` was already correct — it uses `page.slug` (the current page object) so no edit was required.

---

## 3. Browser verification (Playwright MCP)

Server: `python manage.py runserver 8765` — left running on `http://127.0.0.1:8765/`.

### 3.1 Generated home preview-band hrefs

Resolved live for each archetype via `document.querySelectorAll('.cs-cases-preview a.row')`:

| Template | Parent slug rendered | Posts |
|---|---|---|
| Pragma | `case-studies` ✔ unchanged | 3 |
| Solaria | `casi` ✔ now correct | 3 |
| Fiscus | `casi-seguiti` ✔ now correct | 3 |
| Continua | `mandati` ✔ now correct | 4 |

### 3.2 Live HTTP status across all 13 home-band links

All fetched in-session (Continua via staff session with `?preview=1`; Pragma/Solaria/Fiscus anonymous since they are `published_live`):

```
200  /templates/business/pragma-corporate-suite/preview/case-studies/manifatturiero-bresciano-piano-industriale/
200  /templates/business/pragma-corporate-suite/preview/case-studies/carve-out-consumer-italia-dach/
200  /templates/business/pragma-corporate-suite/preview/case-studies/csrd-utility-quotata-roadmap/
200  /templates/business/solaria-coaching/preview/casi/executive-neo-ceo-tech-scaleup/
200  /templates/business/solaria-coaching/preview/casi/team-coaching-middle-management-manifattura/
200  /templates/business/solaria-coaching/preview/casi/gruppo-aziendale-neo-manager-studio-legale/
200  /templates/business/fiscus-commercialista/preview/casi-seguiti/pmi-manifattura-bilancio-revisione/
200  /templates/business/fiscus-commercialista/preview/casi-seguiti/contenzioso-tributario-accertamento-iva/
200  /templates/business/fiscus-commercialista/preview/casi-seguiti/wealth-passaggio-generazionale-holding/
200  /templates/business/continua-stewardship/preview/mandati/famiglia-a-quarta-generazione-holding-industriale/?preview=1
200  /templates/business/continua-stewardship/preview/mandati/famiglia-b-fondazione-di-famiglia/?preview=1
200  /templates/business/continua-stewardship/preview/mandati/famiglia-c-trasferimento-intergenerazionale/?preview=1
200  /templates/business/continua-stewardship/preview/mandati/famiglia-d-single-family-office-estero/?preview=1
```

**13/13 live → 200.** Before the fix, 10/13 returned 404 (only the 3 Pragma rows resolved).

### 3.3 Visual regression check

Screenshots saved (cropped to `.cs-cases-preview` band on each archetype):

* `cs-fix-pragma-cases-band-scrolled.png` — green accent, 3 numbered rows, intact
* `cs-fix-solaria-cases-band.png` — bronze/copper accent, image thumbs, 3 rows, intact
* `cs-fix-fiscus-cases-band.png` — navy + steel accent, 3 rows, intact
* `cs-fix-continua-cases-band.png` — green/gold accent, 4 rows, intact
* `cs-fix-continua-case-detail-load.png` — `mandati/famiglia-a-…` post detail loads with full content

No spacing, color, typography, motion, or copy difference vs. pre-fix snapshots in `factory/reports/browser-verification/x4a-step1d/` and `…/continua-pass1-review-lock/`. Layout is byte-identical at the chrome level — only the `<a href>` value changed.

---

## 4. Test suite

```
$ python manage.py test apps.catalog
Ran 171 tests in 2.058s
FAILED (failures=1)   ← pre-existing booking_flag check, confirmed via `git stash` on bare main
```

170/171 catalog tests pass. The one failure is `FreshSeedChainBackfillTests.test_medical_and_restaurant_templates_have_booking_flag` and reproduces with the fix stashed — unrelated to this change.

---

## 5. Outcome

* **Issue fixed:** corporate-suite home preview-band no longer hardcodes `'case-studies'`. It now resolves the case-study list page slug per archetype via a new `cases_parent_slug` context entry, mirroring the existing `blog_parent_slug` pattern.
* **Affected siblings verified live:** Pragma (3/3) · Solaria (3/3) · Fiscus (3/3) · Continua (4/4) → **all 13 home-band hrefs return 200**.
* **Visual regression:** none. Chrome rendering identical across all four archetypes.
* **Shared cluster issue status:** **CLOSED**. Any future corporate-suite enrollee inherits the dynamic resolver automatically as long as it declares a page with `kind == 'case_study_list'`.

### Files changed

* `apps/catalog/views.py` — added `cases_parent_slug` context entry
* `templates/live_templates/business/corporate-suite/home.html` — replaced `'case-studies'` literal with `cases_parent_slug`
* `factory/reports/browser-verification/corporate-suite-case-parent-fix.md` — this report

### Server still running

* Command: `python manage.py runserver 8765`
* Port: **8765**
* Open URL example: `http://127.0.0.1:8765/templates/business/continua-stewardship/preview/?preview=1` (staff session required for Continua, draft tier)
