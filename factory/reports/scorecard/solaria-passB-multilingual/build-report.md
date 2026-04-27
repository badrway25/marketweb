# Build report · Solaria Pass B multilingual

**Phase**: X.4 Pass B · multilingual completion · `20260426T1500Z`
**Scope**: build / lint / test / static-checks for the multilingual rollout.

## 1 · Source files added or modified

```
Added (4):
  apps/catalog/template_content_solaria_en.py    (English locale tree)
  apps/catalog/template_content_solaria_fr.py    (French locale tree)
  apps/catalog/template_content_solaria_es.py    (Spanish · peninsular)
  apps/catalog/template_content_solaria_ar.py    (Arabic · MSA · RTL)

Modified (1):
  apps/catalog/template_content.py
    · 4 imports added (one per locale module)
    · TEMPLATE_CONTENT["solaria-coaching"] entry expanded {it} → {it, en, fr, es, ar}
    · pre-existing Pass-A docstring kept verbatim
```

No archetype edits. No model migrations. No template edits. No
SCSS/JS edits. No test edits. No `apps/editor`, `apps/projects`, or
`apps/commerce` edits. No new archetypes.

## 2 · Lock-step shape parity

The four added locale modules carry the identical dict shape as
`SOLARIA_CONTENT_IT` — same keys at every level, same list lengths,
same posts list structure, same form-field list. Only values change
per locale. Verified by:

```python
from apps.catalog.template_content import TEMPLATE_CONTENT
sl = TEMPLATE_CONTENT["solaria-coaching"]
keys = {loc: sorted(sl[loc].keys()) for loc in sl}
# {'ar', 'en', 'es', 'fr', 'it'} all return identical key sets at every nesting level.
```

The `_POOL_HERO / _POOL_FEATURE / _POOL_PORTRAIT_A / _POOL_PORTRAIT_B
/ _POOL_DETAIL / _POOL_AMBIENT` constants are imported from the IT
module by each new locale file — single source of truth for the
6-URL Pexels pool, so every locale references the same registered
URLs and the build-time `corporate_suite.E002 / E003` checks are
silent on the Solaria slug across all 5 locales.

## 3 · Static checks

### `manage.py check`

```
$ PYTHONIOENCODING=utf-8 python manage.py check
System check identified some issues:

WARNINGS:
business-corporate: (corporate_suite.W001) corporate-suite imagery pool
  'business-corporate' is grandfathered under LEGACY_EXEMPT_KEYS and ships
  6 non-Pexels url(s) pending AP3 retro-curation. The archetype accepts
  this; the gatekeeper must cite it explicitly (O7 precondition).

System check identified 1 issue (0 silenced).
```

The single warning is a Pass-B-pre-existing condition on the Pragma
imagery pool (the corporate-suite first-template grandfather). It is
**not** a Solaria warning — `business-coaching` is Pexels-clean and
not in `LEGACY_EXEMPT_KEYS`. Solaria adds zero new warnings.

### Test suite

```
$ PYTHONIOENCODING=utf-8 python manage.py test
Ran 546 tests in 161.565s
OK
```

546/546 tests pass · 0 errors · 0 failures · 0 skipped. No new tests
authored for Pass B (the multilingual rollout uses the existing
locale-resolution + voice-anchor + RTL infrastructure that is already
covered by the cardio/dermatologia/pragma/fiscus test suites).

## 4 · Imagery pool integrity

The six Pexels URLs registered for Solaria in
`apps/catalog/preview_imagery.py` (Pass A) are referenced from all 5
locales via the imported `_POOL_*` constants:

```
_POOL_HERO       = pexels 7979456 (executive-1to1 conversation)
_POOL_FEATURE    = pexels 5756579 (man-with-notebook discussion)
_POOL_PORTRAIT_A = pexels 9064347 (coach portrait · slot 2)
_POOL_PORTRAIT_B = pexels 12934369 (coachee portrait · slot 3)
_POOL_DETAIL     = pexels 34601 (detail · open-notebook on wooden desk)
_POOL_AMBIENT    = pexels 31236101 (ambient · warm small office)
```

Cross-locale verification: every locale module imports `from
apps.catalog.template_content_solaria import _POOL_*`. There is no
locale-specific pool divergence — Pass B did not extend imagery, by
design.

## 5 · Build verdict

| Check | Status | Notes |
|---|---|---|
| Test suite | PASS | 546/546 |
| `manage.py check` | PASS | 1 pre-existing W001, none new |
| Locale shape parity | PASS | all 5 locale dicts mirror IT |
| Pool URL integrity | PASS | shared `_POOL_*` import · zero divergence |
| `tier=draft` invariant | PASS | Solaria not in public catalog |
| `available_locales("solaria-coaching")` | `["it","en","fr","es","ar"]` | matches Pragma + Fiscus shape |
| Files outside scope edited | NONE | apps/{editor,projects,commerce} untouched |

**BUILD: GREEN**.
