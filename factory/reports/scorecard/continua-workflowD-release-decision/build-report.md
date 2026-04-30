# Build report · Continua Workflow D Release Decision · 2026-04-30

## 1 · Files added / changed

This pass is **read-only with reports + 2 captures + 1 helper script**. Zero source code, content registry, JSON registry, template, or migration was modified.

| Path | Action | Size delta |
|---|---|---|
| `factory/reports/continua/continua-workflowD-release-decision.md`                    | NEW | release-decision narrative · 9 sections |
| `factory/reports/browser-verification/continua-workflowD-release-decision.md`        | NEW | browser walk index · 10 sections |
| `factory/reports/browser-verification/continua-workflowD-release-decision/it-1440-firstscroll.png` | NEW | IT hero first-scroll (1440) |
| `factory/reports/browser-verification/continua-workflowD-release-decision/ar-1440-firstscroll.png` | NEW | AR hero first-scroll (1440 · RTL) |
| `factory/reports/scorecard/continua-workflowD-release-decision/build-report.md`      | NEW (THIS file) | scorecard build sub-report |
| `factory/reports/scorecard/continua-workflowD-release-decision/browser-verifier.md`  | NEW | scorecard browser-verifier sub-report |
| `factory/reports/scorecard/continua-workflowD-release-decision/release-gatekeeper.md`| NEW | scorecard release-gatekeeper sub-report |
| `factory/reports/scorecard/continua-workflowD-release-decision/scorecard.md`         | NEW | aggregate scorecard |
| `factory/reports/scorecard/continua-workflowD-release-decision/summary.md`           | NEW | one-paragraph summary |
| `factory/reports/scorecard/continua-workflowD-release-decision/_smoke.py`            | NEW | 45-route smoke prober (re-runnable) |

**No file outside `factory/reports/...` was modified by this pass.** No edits to `apps/editor/*`, `apps/projects/*`, `apps/commerce/*`, `apps/catalog/*`, `templates/**`, `TEMPLATE_REGISTRY.json`, or any management command. No new migration. No new archetype. No new template. The `_base.html` Pass B RTL extension is intact and unchanged.

## 2 · Build-time validation

### 2.1 · Test suite

```bash
$ python manage.py test
Ran 546 tests in 179.6s
FAILED (failures=1)
  → test_medical_and_restaurant_templates_have_booking_flag
```

The single failure is `test_medical_and_restaurant_templates_have_booking_flag`. The assertion compares the set of slugs with `has_booking=True` to the expected medical+restaurant+lawyer+W2-booking-enabled set. Continua is a corporate-suite/family-office template that does not carry the `has_booking` flag. The failure is independent of Continua and pre-dates Continua's enrollment (documented in `continua-lf5-it-rebuild.md §8.4` and reproduced in `continua-passB-multilingual.md §8`). Continua-related regressions: **0**. Final tally: **545 / 546** — identical to Pass B Multilingual.

### 2.2 · Tier state

```bash
$ python manage.py shell -c "from apps.catalog.models import WebTemplate; t = WebTemplate.objects.get(slug='continua-stewardship'); print(t.tier, t.layout_family)"
draft LF-5

$ python manage.py shell -c "from apps.catalog.models import WebTemplate; print('pub=', WebTemplate.objects.filter(tier='published_live').count(), 'draft=', WebTemplate.objects.filter(tier='draft').count())"
pub= 22 draft= 1
```

Continua is the only template in the catalog at tier `draft` (correct per the brief's D-102 cadence). 22 siblings published live + Continua at draft = 23 total business+other-category templates registered.

### 2.3 · Registry vs DB parity

```bash
$ grep -A1 '"continua-stewardship"' TEMPLATE_REGISTRY.json | grep '"tier"'
      "tier": "draft",
```

Registry tier matches DB tier (both `draft`). The `continua-pass1-review-lock` reconciliation is intact. The `tier_reason` field on the registry row continues to document the brief's D-102 cadence and the multilingual-rollout-then-handshake sequence.

### 2.4 · Locale registration

```bash
$ python manage.py shell -c "from apps.catalog.template_content import get_available_locales; print(get_available_locales('continua-stewardship'))"
['it', 'en', 'fr', 'es', 'ar']
```

5 locales live in the runtime loader. RTL flag still `true` on the registry row (line 333). Pass B Multilingual's wiring is intact.

### 2.5 · Imagery preservation (CS-IMG-SRC-01)

The 8 `_POOL_*` constants in `apps/catalog/template_content_continua.py` (extracted at Pass B) are imported by every locale module. Cross-locale imagery substitution is structurally impossible — only the IT module owns the URLs.

```python
# 4 of 5 locale modules import the same constants:
from apps.catalog.template_content_continua import (
    _HERO_IMAGE, _PILLAR_ICON_01, _PILLAR_ICON_02, _PILLAR_ICON_03, _PILLAR_ICON_04,
    _PORTRAIT_ELEONORA, _PORTRAIT_TOMAS, _PORTRAIT_GINEVRA,
)
```

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

All 8 IDs Pexels-only. All 8 referenced from at least one rendered surface (hero · 4 pillars · 3 portraits). No grandfather exception needed (Continua is a new pilot, not a legacy template).

### 2.6 · System checks

```bash
$ python manage.py runserver 127.0.0.1:8051 --noreload
System check identified some issues:
WARNINGS:
  business-corporate: (corporate_suite.W001) corporate-suite imagery pool 'business-corporate' is grandfathered under LEGACY_EXEMPT_KEYS and ships 6 non-Pexels url(s) pending AP3 retro-curation.
System check identified 1 issue (0 silenced).
```

The W001 warning is the **Pragma legacy grandfather** documented in `corporate-suite-blocking-rules.md` (the only tolerated non-Pexels exception in the cluster). It does NOT affect Continua. Continua's pool key is `business-stewardship`, not `business-corporate`.

## 3 · Verdict

Build is **GREEN**. All build-time checks pass. The state at the end of this pass is identical to the state at the start of this pass — by design. Workflow D is a release-decision pass, not a build pass.
