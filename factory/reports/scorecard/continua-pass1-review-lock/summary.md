# Continua · Pass 1.5 Review-Lock · Summary

**Date**: 2026-04-29
**Branch**: `phase-x4-continua-pass1-review-lock`
**Predecessor pass**: `factory/reports/scorecard/continua-pass1-it/` (pass-1 IT · GREEN at draft · 4.74 / 5)
**Final tier**: `draft` (registry + DB now agree)
**Server URL kept open**: `http://127.0.0.1:8092/templates/business/continua-stewardship/preview/?preview=1`

---

## What landed

A single DB-side write applied through the documented `python manage.py sync_template_tiers` command, flipping `WebTemplate.tier` for `slug='continua-stewardship'` from `published_live` (the transient pass-1 walk-state) back to `draft` (the registry value). After the sync, both sources of truth agree:

| Source | Pre-pass-1.5 | Post-pass-1.5 |
|---|---|---|
| `TEMPLATE_REGISTRY.json` | `tier: draft` | `tier: draft` |
| `WebTemplate.tier` (DB) | `tier: published_live` | `tier: draft` |

No source code, no content registry, no template, no migration was modified. Only operational state.

---

## Decision matrix

| Option | Verdict | Why |
|---|---|---|
| Promote to `published_live` now | REJECTED | Hard constraint "do not auto-force published_live"; brief's D-102 cadence reserves LIVE for workflow C. |
| Keep `draft`, restore DB consistency, reuse existing staff-preview path | **CHOSEN** | The legitimate path already exists end-to-end (D-055 + Solaria Pass C). Continua reuses unchanged corporate-suite chrome that already propagates `?preview=1` on every internal href. |
| Build a new draft-review affordance | REJECTED | Duplicates the chosen path. |

---

## What was on the line

Pass-1 closed visually GREEN but the operational state was unstable. Any of these would have surfaced the inconsistency:

- A teammate pulling the branch and running the dev server against the same SQLite file
- An admin opening the template in `/admin/` and seeing it as `published_live`
- An anonymous catalog probe seeing Continua as a public card while the registry, the catalog roadmap, and the brief all said "draft"
- A test suite run that re-counts `published_live` templates and finds an unexpected 23

Pass 1.5 closes the door before any of those happen.

---

## Where the live walk caught a real surface defect

The walk surfaced 4 home-band hrefs that 404 because the shared corporate-suite `home.html:660` hardcodes `'case-studies'` as the parent slug for the `live_template_post` URL — and Continua's case_study_list slug is `mandati`. Same defect affects Fiscus (`casi-seguiti`) and Solaria (`casi`); Pragma is the only sibling whose page slug matches the literal value, so it is the only one not affected.

This is **pre-existing technical debt** that predates Continua's commit; it is documented in detail in `build-report.md §4` and `release-gatekeeper.md §5`. The legitimate review path is intact via the nav (home → Mandati nav link (200) → list (200) → 4/4 detail rows (200)), so no review surface is unreachable. Per the task's "implement only the minimum correct fix" + "be conservative" constraints, the fix is **not** applied in this pass.

A small follow-up task is recommended scoped to "case-studies parent-slug parity across corporate-suite siblings" — the proper fix mirrors the existing `blog_parent_slug` pattern in `views.py` and updates 1–2 hardcoded `'case-studies'` literals in the shared `home.html`. Strict superset semantics: Pragma stays at `case-studies`; Fiscus/Solaria/Continua route correctly.

---

## Live verification at a glance

| Probe | Auth | Status | Verdict |
|---|---|---|---|
| `/preview/` | anonymous | 404 | PASS — D-055 tier gate intact |
| `/templates/business/` body contains `continua-stewardship` | anonymous | NO | PASS — anonymous catalog does not surface draft |
| `/preview/?preview=1` | staff | 200 | PASS — legitimate review path works |
| `/templates/business/?preview=1` lists Continua | staff | YES (5 cards) | PASS |
| 11 home internal hrefs propagate `?preview=1` | staff | 11/11 | PASS |
| 7/11 → 200 (nav, mp-back, language, page CTAs) | staff | 7/11 | PASS at the review-relevant set |
| 4/11 home preview-band → 404 (hardcoded slug bug) | staff | 4/11 | DOCUMENTED — pre-existing |
| 4/4 case-detail posts via nav-driven path | staff | 4/4 | PASS |

---

## Server state at end of pass

- Server command: `python manage.py runserver 127.0.0.1:8092 --noreload` (background)
- URL kept open: `http://127.0.0.1:8092/templates/business/continua-stewardship/preview/?preview=1`
- Login: `solaria_qa_staff / continuapass1lock` (existing staff user reused from Solaria passes; `is_staff=True`; password reset for this verification session)
- DB tier: `draft` (matches registry)
- Registry tier: `draft`
- `sync_template_tiers` is idempotent on this row (re-run prints "0 tier(s) updated")

The user can open the URL in a browser, log in with the credentials above, and walk Continua exactly as they would walk Solaria pre-Pass-D — through the legitimate D-055 staff-preview path — with no DB/registry mismatch lurking underneath.

---

## Files written by this pass

```
factory/reports/continua/continua-pass1-review-lock.md
factory/reports/browser-verification/continua-pass1-review-lock.md
factory/reports/browser-verification/continua-pass1-review-lock/home-1440-firstscroll.png
factory/reports/browser-verification/continua-pass1-review-lock/listing-staff-preview-1440.png
factory/reports/scorecard/continua-pass1-review-lock/build-report.md
factory/reports/scorecard/continua-pass1-review-lock/browser-verifier.md
factory/reports/scorecard/continua-pass1-review-lock/release-gatekeeper.md
factory/reports/scorecard/continua-pass1-review-lock/summary.md   (this file)
```

No source files modified. No tests modified. No migrations created.

---

## Verdict

**Continua pass-1.5 review-lock is GREEN.**

- DB and registry now agree on `tier: draft`.
- The legitimate D-055 staff-preview path is verified live (anonymous 404 · staff 200 · `?preview=1` propagation 11/11 · case-detail reachable 4/4 via nav).
- The strong visual outcome from pass-1 is preserved unchanged.
- Continua is **draft-reviewable**, not flipped to LIVE. Workflow C (multilingual rollout + LIVE flip + user handshake) remains the binding next step.

**Continua is now ready for the same human visual review pass-1 closed against — with the operational state honest.**
