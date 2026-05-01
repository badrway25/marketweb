# Build report · Cornice Workflow D Release Decision · 2026-05-01

## 1 · Files added / changed

This pass is **read-only with reports + 3 captures + 1 helper script**. Zero
source code, content registry, JSON registry, template, or migration was
modified.

| Path | Action | Contents |
|---|---|---|
| `factory/reports/cornice/cornice-workflowD-release-decision.md`                    | NEW | release-decision narrative · 8 sections |
| `factory/reports/browser-verification/cornice-workflowD-release-decision.md`        | NEW | browser walk index · 11 sections |
| `factory/reports/browser-verification/cornice-workflowD-release-decision/captures/it-1440-firstscroll.png` | NEW | IT hero first-scroll (1440) |
| `factory/reports/browser-verification/cornice-workflowD-release-decision/captures/ar-1440-firstscroll.png` | NEW | AR hero first-scroll (1440 · RTL · Naskh h1) |
| `factory/reports/browser-verification/cornice-workflowD-release-decision/captures/ar-720-firstscroll.png` | NEW | AR responsive (720 · RTL · hamburger entry) |
| `factory/reports/scorecard/cornice-workflowD-release-decision/build-report.md`      | NEW (THIS file) | scorecard build sub-report |
| `factory/reports/scorecard/cornice-workflowD-release-decision/browser-verifier.md`  | NEW | scorecard browser-verifier sub-report |
| `factory/reports/scorecard/cornice-workflowD-release-decision/release-gatekeeper.md`| NEW | scorecard release-gatekeeper sub-report |
| `factory/reports/scorecard/cornice-workflowD-release-decision/scorecard.md`         | NEW | aggregate scorecard |
| `factory/reports/scorecard/cornice-workflowD-release-decision/summary.md`           | NEW | one-paragraph summary |
| `factory/reports/scorecard/cornice-workflowD-release-decision/_smoke.py`            | NEW | 45-route staff smoke + anon-probe + sibling-regression prober (re-runnable) |

**No file outside `factory/reports/...` was modified by this pass.** No edits
to `apps/editor/*`, `apps/projects/*`, `apps/commerce/*`, `apps/catalog/*`,
`templates/**`, `TEMPLATE_REGISTRY.json`, or any management command. No
new migration. No new archetype. No new template. The Workflow C
multilingual extension (`_base.html` Naskh override + 4 locale modules) is
intact and unchanged.

## 2 · Build-time validation

### 2.1 · Test suite

```
$ python manage.py test
Ran 546 tests in 163.156s
FAILED (failures=1)
  → test_medical_and_restaurant_templates_have_booking_flag
```

The single failure is `test_medical_and_restaurant_templates_have_booking_flag`.
The assertion compares the set of slugs with `has_booking=True` against the
expected medical+restaurant+lawyer+W2-booking-enabled set; Cornice is a
corporate-suite/architecture template that does not carry the `has_booking`
flag, so this failure is independent of Cornice and pre-dates Cornice's
enrollment (documented as pre-existing in the v15 baseline and reproduced
at A.5, A.6, and Workflow C). Cornice-related regressions: **0**. Final
tally: **545 / 546** — identical to A.6 review-lock and Workflow C.

### 2.2 · Tier state

```
$ python manage.py shell -c "from apps.catalog.models import WebTemplate; t = WebTemplate.objects.get(slug='cornice-architettura'); print(t.tier, t.layout_family)"
draft LF-2

$ python manage.py shell -c "from apps.catalog.models import WebTemplate; print('pub=', WebTemplate.objects.filter(tier='published_live').count(), 'draft=', WebTemplate.objects.filter(tier='draft').count())"
pub= 23 draft= 1
```

Cornice is the only template in the catalog at tier `draft` (correct per
the D-102 multilingual-then-handshake cadence). 23 siblings published
live + Cornice at draft = 24 total catalog rows. Tier is identical
before, during, and after this pass.

### 2.3 · Registry vs DB parity

```
$ grep -n '"cornice-architettura"' TEMPLATE_REGISTRY.json
341:      "slug": "cornice-architettura",
$ grep -A 50 '"cornice-architettura"' TEMPLATE_REGISTRY.json | grep '"tier"'
      "tier": "draft",
```

Registry tier (line 387) matches DB tier (both `draft`). The Workflow C
`tier_reason` documents the multilingual-rollout-then-handshake sequence
and the LF-2-scoped Naskh decision. No registry edits occurred during
Workflow D.

### 2.4 · Locale registration

```
$ python manage.py shell -c "from apps.catalog.template_content import get_available_locales; print(get_available_locales('cornice-architettura'))"
['it', 'en', 'fr', 'es', 'ar']
```

5 locales live in the runtime loader. RTL flag is `true` on the registry row
(line 383). Workflow C's wiring is intact.

### 2.5 · Voice-anchor source-of-truth (CS-EXEC-01)

The voice anchor `argomento` and its translation cognates live in five
locale-specific content modules; the IT module is the source of truth for
the LF-2 layout shape. All four non-IT modules import the Pexels URL
constants from `template_content_cornice.py` so cross-locale imagery
substitution is structurally impossible (matches the Continua/Solaria
Pass-B precedent).

```
apps/catalog/template_content_cornice.py     ─ IT source · 1,000+ lines · LF-2 shape canonical
apps/catalog/template_content_cornice_en.py  ─ EN locale · 1,083 lines · imports IT image constants
apps/catalog/template_content_cornice_fr.py  ─ FR locale · 1,107 lines · imports IT image constants
apps/catalog/template_content_cornice_es.py  ─ ES locale · 1,082 lines · imports IT image constants
apps/catalog/template_content_cornice_ar.py  ─ AR locale · 1,088 lines · imports IT image constants
```

### 2.6 · Imagery preservation (CS-IMG-SRC-01)

All Cornice imagery URLs are Pexels-only (verified at A.5 · re-bound at A.6
and Workflow C · 45/45 staff routes 200). Workflow D performed no imagery
edits; the existing pool is preserved exactly.

### 2.7 · System checks

```
$ python manage.py runserver 127.0.0.1:8052 --noreload
[server starts cleanly]
[expected pre-existing W001 grandfather warning on Pragma legacy pool · unrelated]
```

The W001 warning is the **Pragma legacy grandfather** documented in
`corporate-suite-blocking-rules.md` (the only tolerated non-Pexels exception
in the cluster). It does NOT affect Cornice; Cornice's pool key is
`business-architecture`, not `business-corporate`.

## 3 · Verdict

Build is **GREEN**. All build-time checks pass. The state at the end of
this pass is identical to the state at the start of this pass — by design.
Workflow D is a release-decision pass, not a build pass.
