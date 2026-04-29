# Continua · Pass 1.5 Review-Lock · Build report

**Date**: 2026-04-29
**Branch**: `phase-x4-continua-pass1-review-lock`
**Predecessor pass**: `factory/reports/scorecard/continua-pass1-it/build-report.md` (pass-1 IT · `d6cff90`)
**Tier at landing**: `draft` in registry AND in DB (consistent · D-055 staff-preview path).

This is the build report for the operational-state lock pass, not a content/visual build pass. No source code, no content registry, no template, no migration was modified.

---

## 1 · Files changed

| Layer | File | Nature of change |
|---|---|---|
| (none) | — | No source files modified |

| Layer | File | Nature of change |
|---|---|---|
| Reports | `factory/reports/continua/continua-pass1-review-lock.md` | NEW · workflow A.5 review-lock landing report |
| Reports | `factory/reports/browser-verification/continua-pass1-review-lock.md` | NEW · live-walk index |
| Reports | `factory/reports/browser-verification/continua-pass1-review-lock/home-1440-firstscroll.png` | NEW · staff-session home capture (visual unchanged from pass-1) |
| Reports | `factory/reports/browser-verification/continua-pass1-review-lock/listing-staff-preview-1440.png` | NEW · staff listing capture (Continua draft + 4 live siblings) |
| Reports | `factory/reports/scorecard/continua-pass1-review-lock/build-report.md` | NEW (this file) |
| Reports | `factory/reports/scorecard/continua-pass1-review-lock/browser-verifier.md` | NEW |
| Reports | `factory/reports/scorecard/continua-pass1-review-lock/release-gatekeeper.md` | NEW |
| Reports | `factory/reports/scorecard/continua-pass1-review-lock/summary.md` | NEW |

| Operational state | Action | Effect |
|---|---|---|
| `WebTemplate.tier` (DB column) on `slug=continua-stewardship` | `python manage.py sync_template_tiers` | `published_live` → `draft` (1 row) |
| Staff QA user `solaria_qa_staff` password | Reset to `continuapass1lock` for the verification session | Re-uses the existing user with `is_staff=True`; password is the only volatile field |

**Files explicitly NOT touched** (per the hard constraints):
- `apps/editor/*` — UNTOUCHED
- `apps/projects/*` — UNTOUCHED
- `apps/commerce/*` — UNTOUCHED
- `apps/catalog/*` source code — UNTOUCHED
- `templates/**` — UNTOUCHED
- `TEMPLATE_REGISTRY.json` — UNTOUCHED
- All `apps/catalog/template_content_*.py` — UNTOUCHED
- `apps/catalog/template_dna.py`, `preview_imagery.py`, `imagery_policy.py`, `seed_templates.py` — UNTOUCHED
- No new archetype defined.

---

## 2 · Inconsistency that was removed

Pass-1 closed visually green but with a known operational drift between two sources of truth:

| Source | Pass-1 close state | What it implied |
|---|---|---|
| `TEMPLATE_REGISTRY.json` | `tier: draft` | Continua should be invisible to the public catalog and 404 on the preview path for anonymous traffic |
| `WebTemplate.tier` (DB) | `tier: published_live` | Continua is treated as a public catalog card AND its preview path is reachable without auth |

The DB-side flip was applied during the walk to bypass the staff-preview gate. The recovery promise was "next `seed_templates` run will re-sync from registry". Pass 1.5 makes that recovery actual — the existing `sync_template_tiers` command was the documented way to do it. After the run:

| Source | Pass-1.5 close state |
|---|---|
| `TEMPLATE_REGISTRY.json` | `tier: draft` (unchanged) |
| `WebTemplate.tier` (DB) | `tier: draft` (now matches) |

**Observable consequence**: `python manage.py sync_template_tiers` is now idempotent against this row — running it again would print `0 tier(s) updated. Catalog distribution: 22 published_live / 1 draft.` which is the binding state.

---

## 3 · The decision

The task asked the pass to explicitly decide between "remain draft-reviewable" and "actually become published_live now". The decision tree:

| Option | Verdict | Reasoning |
|---|---|---|
| (a) Promote to `published_live` | **REJECTED** | Hard constraint: "do not auto-force published_live". The brief's D-102 cadence reserves LIVE for workflow C after EN/FR/ES/AR + AR RTL parity. |
| (b) Keep `draft`, restore DB consistency, use existing staff-preview path | **CHOSEN** | The legitimate review affordance already exists end-to-end (D-055 + Solaria Pass C `staff_preview` propagation across all corporate-suite chrome). Continua reuses that chrome unchanged. |
| (c) Build a new draft-review affordance | REJECTED | Duplicates (b) for no gain. |

The chosen path also satisfies the task's tie-break rule: "prefer legitimate reviewable draft over accidental live exposure if there is any doubt".

---

## 4 · One pre-existing finding documented (not fixed)

While verifying the staff-preview path live, the walk caught a 404 on 4 of the 11 internal hrefs harvested from the home. Diagnosis:

**Symptom**: The home renders a 4-row "Mandati in continuità" preview band (`.cs-cases-preview .row`). Each row's `<a>` href routes via `{% url 'catalog:live_template_post' template.category.slug template.slug 'case-studies' post.slug %}` — i.e. a hardcoded `'case-studies'` parent slug.

**Root cause**: The literal `'case-studies'` was correct only for Pragma, the first corporate-suite sibling, whose case_study_list page slug is `case-studies`. Subsequent siblings author their list under a brand-coherent slug:

| Sibling | case_study_list page slug | home preview-band href routes to |
|---|---|---|
| Pragma | `case-studies` | `/preview/case-studies/<post>/` ✓ 200 |
| Fiscus | `casi-seguiti` | `/preview/case-studies/<post>/` ✗ 404 |
| Solaria | `casi` | `/preview/case-studies/<post>/` ✗ 404 |
| Continua | `mandati` | `/preview/case-studies/<post>/` ✗ 404 |

**Why this was not caught earlier**: Solaria Pass C's 11-href verification list (in its `browser-verifier.md`) included the language switcher, in-page nav links, and `mp-back`, but did NOT probe the home preview-band rows. Pass-1's `release-gatekeeper.md` claimed "9 page surfaces 200" — which is true for the routes themselves (`mandati/<slug>/` resolves), but the home-band hrefs that *should* point to those routes use the wrong parent slug.

**Reachability**: The legitimate review path is intact via the nav: home → Mandati nav link (200) → mandati list (200) → each detail (4/4 → 200). No review surface is unreachable.

**Fix sketch (NOT applied in this pass)**: mirror the existing `blog_parent_slug` pattern in `apps/catalog/views.py:LiveTemplateView.get_context_data`:

```python
ctx["cases_parent_slug"] = next(
    (p["slug"] for p in self.content["pages"] if p["kind"] == "case_study_list"),
    "case-studies",
)
```

then change the `home.html:660` literal `'case-studies'` to `cases_parent_slug|default:'case-studies'`. Mirror the same on `home.html:line for cases-preview second occurrence` if any. Strict superset: Pragma stays at `case-studies`; Fiscus/Solaria/Continua route correctly.

**Why this pass does NOT apply the fix**:
1. Hard constraint "implement only the minimum correct fix": the legitimate path already exists (nav-driven), so review-lock is achievable without this fix.
2. Hard constraint "be conservative": the fix touches a shared template used by 4 templates and would ripple through 5 locales for Solaria/Fiscus.
3. Hard constraint "preserve the strong visual outcome from pass-1": touching shared chrome carries non-zero regression risk.

**Recommendation**: open a small follow-up scoped to "case-studies parent-slug parity across corporate-suite siblings". Treat as cluster maintenance, not Continua-specific work.

---

## 5 · How to verify the lock-pass is intact

```bash
# 1. Registry vs DB agreement (1 row, both → draft)
python manage.py sync_template_tiers --dry-run
# Expect: "0 tier(s) updated. Catalog distribution: 22 published_live / 1 draft."

# 2. Anonymous tier gate
curl -sS -o /dev/null -w "%{http_code}\n" \
  http://127.0.0.1:8092/templates/business/continua-stewardship/preview/
# Expect: 404

# 3. Staff session reaches the preview
#    (interactive — log in as solaria_qa_staff / continuapass1lock)
#    GET .../preview/?preview=1 → 200
```

---

## 6 · Verdict

**Build PASS at the review-lock scope.** Single DB row updated through the documented sync command; no source change; pass-1's visual outcome preserved verbatim; legitimate review affordance verified live; anonymous tier gate intact. Pass-1.5 is GREEN.
