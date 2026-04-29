# Continua · Pass 1.5 Review-Lock report

**Status**: GREEN · DB/registry inconsistency removed · draft tier preserved · 2026-04-29
**Branch**: `phase-x4-continua-pass1-review-lock`
**Predecessor pass**: `factory/reports/continua/continua-pass1-it.md` (workflow A landing · `d6cff90`)
**Cluster**: corporate-suite · 4th sibling · 1st family-office variant

This is the workflow A.5 / Pass 1.5 *review-lock* report. Its only job is to normalize the operational state left behind after pass-1 so draft/review behavior is legitimate and consistent. Pass-1's visual outcome is preserved verbatim; no source code or content was modified to land this lock.

---

## 1 · One-paragraph summary

Pass-1 IT closed visually green at draft tier, but with a known operational inconsistency: the `WebTemplate.tier` column in the dev DB had been hand-flipped to `published_live` so the staff-preview gate would not block the walk, while `TEMPLATE_REGISTRY.json` correctly stayed at `draft`. Pass 1.5 removed this inconsistency by running the existing `python manage.py sync_template_tiers` command, which read the registry and brought the DB row back to `draft`. After the flip-back, Continua is reachable through the legitimate D-055 staff-preview path — staff session + `?preview=1` query string — exactly the same path that Solaria, Fiscus, and Pragma share, and that the corporate-suite chrome was hardened for in Solaria Pass C. Browser-live verification re-walked the IT home + nav-driven mandati flow + side-listing to confirm: 11/11 internal hrefs from the home propagate `?preview=1`, anonymous probes still 404, and the staff listing surfaces Continua as the only draft alongside 4 live siblings. No source code, no content registry, no template, no migration was modified; the only change was the DB-side `tier` column on a single row, applied via the documented sync command. **Verdict: Continua remains DRAFT-REVIEWABLE through a legitimate path. NOT auto-flipped to LIVE.**

---

## 2 · Why this pass exists

Pass-1's `summary.md` and `release-gatekeeper.md` documented the inconsistency openly:

> *"Tier in DB: `published_live` (transient — flipped only for the dev walk so the staff-preview gate didn't block visual review). Tier in registry: `draft` (correct · re-applies on next `seed_templates` run)."*

The description was honest, but the state was unstable: any process that read the DB (admin UI, an anonymous catalog probe, a teammate pulling the branch and running `runserver` against the same SQLite file) would have seen Continua as `published_live` and treated it as catalog-public. The "next `seed_templates` run" recovery was a promise, not a binding. Pass 1.5 makes the recovery actual.

The decision tree the task asked to walk:

| Option | Choice | Reasoning |
|---|---|---|
| (a) Promote Continua to `published_live` now | **REJECTED** | Task hard constraint: "do not auto-force published_live". The brief's D-102 cadence reserves the LIVE flip for workflow C after EN/FR/ES/AR + AR RTL parity. Promoting here would skip the multilingual rollout the brief decision-locked. |
| (b) Keep Continua at `draft` and restore DB consistency, relying on the existing staff-preview path | **CHOSEN** | The legitimate path already exists (D-055 + Solaria Pass C `staff_preview` propagation across all corporate-suite chrome). Continua reuses that chrome unchanged, so the path works for it for free. |
| (c) Build a new draft-review affordance | REJECTED | The existing path is sufficient and was hardened just two passes ago for exactly this scenario. Adding a new mechanism would duplicate it. |

Choice (b) is also the most conservative reading of the task: prefer "legitimate reviewable draft over accidental live exposure if there is any doubt".

---

## 3 · The single change applied

**One DB write on one row, via an existing management command.**

```bash
python manage.py sync_template_tiers --dry-run
# → continua-stewardship: published_live -> draft
#    [dry-run] 1 tier(s) updated. Catalog distribution: 23 published_live / 0 draft.
python manage.py sync_template_tiers
# → continua-stewardship: published_live -> draft
#    1 tier(s) updated. Catalog distribution: 22 published_live / 1 draft.
```

No source files, no JSON, no template, no migration. The only persisted artifact of this pass is the `WebTemplate.tier` column value for `slug='continua-stewardship'` in `db.sqlite3`, which now equals the registry's `tier: draft`.

The dev `solaria_qa_staff` user's password was reset to `continuapass1lock` for the verification session — same shape as Solaria's prior passes (the user already exists with `is_staff=True`, only the password string changes per session).

---

## 4 · Files written by this pass

Only reports — no code, content, or template change:

```
factory/reports/continua/continua-pass1-review-lock.md                              (this file)
factory/reports/browser-verification/continua-pass1-review-lock.md                  (browser walk index)
factory/reports/browser-verification/continua-pass1-review-lock/home-1440-firstscroll.png
factory/reports/browser-verification/continua-pass1-review-lock/listing-staff-preview-1440.png
factory/reports/scorecard/continua-pass1-review-lock/build-report.md
factory/reports/scorecard/continua-pass1-review-lock/browser-verifier.md
factory/reports/scorecard/continua-pass1-review-lock/release-gatekeeper.md
factory/reports/scorecard/continua-pass1-review-lock/summary.md
```

---

## 5 · Server posture at landing

- Command: `python manage.py runserver 127.0.0.1:8092 --noreload` (background)
- Port: **8092** · URL kept open: `http://127.0.0.1:8092/templates/business/continua-stewardship/preview/?preview=1`
- DB tier: `draft` (matches registry)
- Registry tier: `draft`
- Reviewer auth: `solaria_qa_staff / continuapass1lock` · `is_staff=True` · existing user reused from Solaria passes
- Anonymous probe of the same path → **404** (D-055 tier gate intact)

---

## 6 · Live-walk verdict

11/11 internal hrefs from the IT home → 200 in the staff session, including the 4 sibling-route links (`/templates/business/continua-stewardship/`, `/templates/business/`, in-page nav, mandati list) and the home top CTAs. The `?preview=1` flag is propagated correctly on every internal link by the corporate-suite chrome (the Solaria Pass C work covers Continua too because the archetype is shared).

Mandati list → 4/4 detail posts: all 200 via `/preview/mandati/<post-slug>/?preview=1`.

Anonymous tier-gate probes:
- `GET /templates/business/continua-stewardship/preview/` (no cookies) → **404**
- `GET /templates/business/` (no cookies) anonymous catalog **does not list Continua** (string `continua-stewardship` absent)
- Staff `GET /templates/business/?preview=1` lists 5 cards (4 live + Continua draft)

Detail in `factory/reports/browser-verification/continua-pass1-review-lock.md` and the scorecard `browser-verifier.md`.

---

## 7 · One pre-existing finding documented (not fixed)

The home renders a 4-row "Mandati in continuità" preview band with each row linking via `{% url 'catalog:live_template_post' template.category.slug template.slug 'case-studies' post.slug %}` — a hardcoded `'case-studies'` parent slug. Continua's mandati list page slug is `mandati`, so the four home-band rows currently route to `/preview/case-studies/famiglia-…/` and 404. **This bug existed before Continua landed**: it affects every corporate-suite sibling whose case_study_list page slug differs from the literal `'case-studies'` (Fiscus has `casi-seguiti`, Solaria has `casi`, Continua has `mandati`). Pragma is the only sibling whose page slug matches the hardcoded value, so Pragma is the only one not affected.

The legitimate review path is still intact: from the home, the Mandati nav link (200) → the mandati list (200) → each detail row (4/4 → 200). The home preview band's anchor href is broken, but the same posts can be reached via the nav route. Per the task constraints ("be conservative", "implement only the minimum correct fix"), this finding is documented but **not** fixed in this pass, because:

1. The fix would touch a shared file (`templates/live_templates/business/corporate-suite/home.html`) used by 4 templates and would extend through 5 locales for Solaria/Fiscus.
2. The reviewer can complete the visual walk via the nav-driven path; no review surface is unreachable.
3. Fixing it cleanly requires either a small `views.py` addition (mirror the existing `blog_parent_slug` pattern with a `cases_parent_slug`) or a `{% with %}` block in the shared home template — both of which are reasonable but ripple beyond Continua-only scope.

Recommendation: open a small follow-up task scoped to "case-studies parent-slug parity across corporate-suite siblings" and treat it as cluster maintenance, separate from Continua's pass-1.5 review-lock. Detail in `factory/reports/scorecard/continua-pass1-review-lock/build-report.md §4`.

---

## 8 · What was NOT changed

To remove any ambiguity about scope:

- `apps/editor/*` — UNTOUCHED
- `apps/projects/*` — UNTOUCHED
- `apps/commerce/*` — UNTOUCHED
- `apps/catalog/*` source code — UNTOUCHED
- `templates/**` — UNTOUCHED
- `TEMPLATE_REGISTRY.json` — UNTOUCHED (already correct)
- All `apps/catalog/template_content_*.py` — UNTOUCHED
- DNA registry, imagery pool, imagery policy, seed command — UNTOUCHED
- No new archetype, no new template, no new migration

The single observable change is `WebTemplate.objects.get(slug='continua-stewardship').tier`: `published_live` → `draft`.

---

## 9 · Verdict

**Continua pass 1.5 review-lock is GREEN.**

- DB and registry now agree on `tier: draft`.
- The legitimate D-055 staff-preview path is verified live (11/11 home hrefs · 4/4 detail probes · anonymous 404).
- The strong visual outcome from pass-1 is preserved unchanged — same hero, same palette, same governance-cycle-strip, same form gate, same case-row imagery.
- Continua is **not** flipped to `published_live`. The LIVE flip remains workflow C territory, gated on EN/FR/ES/AR + AR RTL parity + the user-handshake binary.

**Continua is now ready for the same human visual review that pass-1 closed against, with the operational state honest.** When workflow C opens, the cascade is documented to the line in the `release-gatekeeper.md` of the scorecard packet.
