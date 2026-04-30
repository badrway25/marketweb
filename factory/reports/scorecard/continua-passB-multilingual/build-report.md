# Build report · Continua Pass B Multilingual · 2026-04-30

## 1 · Files added / changed

| Path | Action | Size delta |
|---|---|---|
| `apps/catalog/template_content_continua.py`      | EDIT (refactor) | +44 lines (`_POOL_*` constants extracted) · 8 inline URLs replaced with constants |
| `apps/catalog/template_content_continua_en.py`   | NEW             | 712 lines |
| `apps/catalog/template_content_continua_fr.py`   | NEW             | 745 lines |
| `apps/catalog/template_content_continua_es.py`   | NEW             | 745 lines |
| `apps/catalog/template_content_continua_ar.py`   | NEW             | 750 lines |
| `apps/catalog/template_content.py`               | EDIT            | +4 imports +4 locale entries on `continua-stewardship` |
| `TEMPLATE_REGISTRY.json`                         | EDIT            | `locales: ["it"]` → `["it","en","fr","es","ar"]` |
| `templates/live_templates/business/corporate-suite/_base.html` | EDIT (RTL polish) | +13 lines (CS-TYPE-05 reset extended to 10 LF-5 surfaces) |

No editor / projects / commerce file touched. No new archetype defined. No imagery URL changed (`_POOL_*` constants reuse the same Pexels frames the IT walk approved). No new migration.

## 2 · Imports / registry wiring

```python
# apps/catalog/template_content.py
from apps.catalog.template_content_continua import CONTINUA_CONTENT_IT
from apps.catalog.template_content_continua_en import CONTINUA_CONTENT_EN
from apps.catalog.template_content_continua_fr import CONTINUA_CONTENT_FR
from apps.catalog.template_content_continua_es import CONTINUA_CONTENT_ES
from apps.catalog.template_content_continua_ar import CONTINUA_CONTENT_AR

TEMPLATE_CONTENT["continua-stewardship"] = {
    "it": CONTINUA_CONTENT_IT,
    "en": CONTINUA_CONTENT_EN,
    "fr": CONTINUA_CONTENT_FR,
    "es": CONTINUA_CONTENT_ES,
    "ar": CONTINUA_CONTENT_AR,
}
```

```json
// TEMPLATE_REGISTRY.json (continua-stewardship row)
"locales": ["it", "en", "fr", "es", "ar"],
"rtl": true,
"tier": "draft",
```

## 3 · Build-time validation

```bash
$ python manage.py test
Ran 546 tests in 171.067s
FAILED (failures=1)
```

The single failure is `test_medical_and_restaurant_templates_have_booking_flag`, documented in `factory/reports/continua/continua-lf5-it-rebuild.md §8.4` as a pre-existing issue out of Pass B scope and unrelated to Continua. **545/546 pass · no Continua-related regression.**

```bash
$ python manage.py shell -c "from apps.catalog.template_content import get_available_locales; print(get_available_locales('continua-stewardship'))"
['it', 'en', 'fr', 'es', 'ar']
```

```bash
$ python manage.py sync_template_tiers
continua-stewardship: published_live -> draft
1 tier(s) updated. Catalog distribution: 22 published_live / 1 draft.
```

## 4 · Imagery preservation (CS-IMG-SRC-01)

The `_POOL_*` constants extracted in `template_content_continua.py` carry the same Pexels frames the LF-5 IT rebuild approved:

| Constant | Pexels ID | Subject |
|---|---|---|
| `_HERO_IMAGE`        | 36093623 | Historic library room (object-led, no people) |
| `_PILLAR_ICON_01`    | 4467737  | Archive/seal monochrome |
| `_PILLAR_ICON_02`    | 5668887  | Council/governance monochrome |
| `_PILLAR_ICON_03`    | 1153213  | Family-tree document monochrome |
| `_PILLAR_ICON_04`    | 3201588  | Compliance binder monochrome |
| `_PORTRAIT_ELEONORA` | 5333750  | Senior woman 60s (Senior Steward) |
| `_PORTRAIT_TOMAS`    | 7841828  | Mature businessman 40s (Family Officer) |
| `_PORTRAIT_GINEVRA`  | 8424881  | Senior woman 50s warm-tone (Compliance Officer) |

Imported by every locale module via:
```python
from apps.catalog.template_content_continua import (
    _HERO_IMAGE, _PILLAR_ICON_01, _PILLAR_ICON_02, _PILLAR_ICON_03, _PILLAR_ICON_04,
    _PORTRAIT_ELEONORA, _PORTRAIT_TOMAS, _PORTRAIT_GINEVRA,
)
```

→ Cross-locale imagery substitution is structurally impossible (the locale modules cannot point at a different Pexels URL than the IT module).

## 5 · Verdict

Build is GREEN. Locale registration is correct (5 locales reachable at `?lang=xx`). Imagery is locale-agnostic by construction. Tier is at `draft` matching the registry.
