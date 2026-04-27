# Solaria · Pass C · summary

**Phase**: X.4 Wave 2 Pilot #2 · Solaria — Business Coaching · **Pass**: C
**Date**: 2026-04-27 · **Run-ISO**: `20260427T1000Z`
**Branch**: `phase-x4-solaria-passC-public-review`

This file is the one-page read for the project owner. The detailed
narrative lives in `factory/reports/solaria/solaria-passC-public-review.md`.

---

## 1 · One-line

**Pass C closed the staff-preview review-path leak so a stakeholder
can now review Solaria end-to-end with one staff login. Public flip is
held until you authorise it.**

---

## 2 · Why Pass C existed

After Pass B, Solaria had 5 locales authored and verified, but the
review path was technically broken: clicking the language switcher,
any in-page nav link, any footer link, or the marketplace mp-back
silently dropped `?preview=1` and 404'd the next page. A reviewer
holding the staff credentials could see exactly the home page they
typed by hand, and nothing else. That made staff-gated review a
useless surface for actual stakeholder review.

Pass C exists to make that path actually work.

---

## 3 · What Pass C changed

8 files, 41 + / 25 - lines:

- **`apps/catalog/views.py`** — `LiveTemplateView` exposes
  `staff_preview` to the template context.
- **6 corporate-suite chrome templates** — every internal `?lang=`
  href builder grew a sibling `&preview=1` clause when
  `staff_preview` is True. 20 occurrences, all replaced with the
  same 3-clause conditional.
- **`TEMPLATE_REGISTRY.json`** — Solaria's `locales` widened from
  `["it"]` to all 5; `rtl` flipped from false to true; `tier_reason`
  rewritten to consolidate Pass A + B + C.

The fix is a strict superset of prior behaviour: every non-staff or
non-draft request renders byte-identical HTML to before.

---

## 4 · What Pass C explicitly did NOT do

- **No tier flip.** Solaria stays `draft`. Public count remains 21/22.
  Homepage trust counter still reads `21+`.
- **No edits to apps/editor, apps/projects, apps/commerce.** Hard
  constraint from the user prompt.
- **No new archetypes, no new templates, no new tests, no new
  imagery, no archetype CSS edits.** All hard constraints honored.

---

## 5 · Live-browser proofs

- `factory/reports/browser-verification/solaria-passC-public-review/20260427T1000Z/01-it-home-1440-after-fix.png`
- `…/02-en-home-1440-after-fix.png` (reached via EN pill, not URL edit)
- `…/03-fr-home-1440-after-fix.png` (reached via FR pill)
- `…/04-es-home-1440-after-fix.png` (reached via ES pill)
- `…/05-ar-home-1440-after-fix.png` (reached via AR pill, RTL)
- `…/06-ar-percorsi-1440-via-link.png` (reached via in-page nav link)
- `…/07-ar-contatti-1440-via-link.png` (reached via in-page nav link)
- `…/08-ar-home-390-mobile.png` (mobile, hamburger visible)
- `…/09-it-home-1024-tablet.png` (tablet, KPI band wraps to 2×2)

The central proof is in `browser-verifier.md` §1: from the IT home
opened with `?preview=1`, all 11 internal hrefs returned HTTP 200 in
the same authenticated session. Before Pass C, 9 of those 11 hrefs
returned 404. After Pass C, 11/11 return 200.

---

## 6 · How to review Solaria yourself

```
URL:    http://127.0.0.1:8731/
Login:  http://127.0.0.1:8731/account/login/
        user: solaria_qa_staff
        pass: solariapassA2026
Open:   http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1
Click:  the EN, FR, ES, AR pills in the marketplace bar.
Click:  any inner-page link (Studio · Il Coach · Percorsi · Casi · Contatti).
        Each works in every locale.
Compare against:
        http://127.0.0.1:8731/templates/business/pragma-corporate-suite/preview/
        http://127.0.0.1:8731/templates/business/fiscus-commercialista/preview/
```

If steps 4–5 work without you ever editing the URL bar, the review
path is legitimate.

---

## 7 · Verdict

**GREEN for review-ready as a draft. HELD for public flip.**

| Question | Answer |
|---|---|
| Is Solaria still wrongly dependent on staff-gated preview? | No — the dependence is now legitimate, not accidental |
| What review path should be used? | Staff login + `?preview=1` on the home URL, then click freely (§6) |
| Is Solaria review-ready for a human stakeholder? | Yes |
| Does the scorecard support public-flip readiness? | Cascade is ready and documented, but the *decision* is held |
| If anything blocks public readiness, identify it | The 8-line test cascade + registry flip + sync command (release-gatekeeper §4) |
| Is tier/cascade happening now? | No — by user instruction "do not auto-force published_live" |
| Is tier/cascade happening later? | Yes, when you authorise it. See release-gatekeeper §4 |

---

## 8 · Files written by this pass

```
TEMPLATE_REGISTRY.json                                                       (modified)
apps/catalog/views.py                                                        (modified)
templates/live_templates/business/corporate-suite/_base.html                 (modified)
templates/live_templates/business/corporate-suite/about.html                 (modified)
templates/live_templates/business/corporate-suite/case_study_detail.html     (modified)
templates/live_templates/business/corporate-suite/case_study_list.html       (modified)
templates/live_templates/business/corporate-suite/home.html                  (modified)
templates/live_templates/business/corporate-suite/services.html              (modified)

factory/reports/solaria/solaria-passC-public-review.md                       (added)
factory/reports/browser-verification/solaria-passC-public-review.md          (added)
factory/reports/browser-verification/solaria-passC-public-review/20260427T1000Z/*.png  (9 captures added)
factory/reports/scorecard/solaria-passC-public-review/build-report.md        (added)
factory/reports/scorecard/solaria-passC-public-review/style-critic.md        (added)
factory/reports/scorecard/solaria-passC-public-review/contrast-accessibility.md  (added)
factory/reports/scorecard/solaria-passC-public-review/responsive-auditor.md  (added)
factory/reports/scorecard/solaria-passC-public-review/browser-verifier.md    (added)
factory/reports/scorecard/solaria-passC-public-review/release-gatekeeper.md  (added)
factory/reports/scorecard/solaria-passC-public-review/scorecard.md           (added)
factory/reports/scorecard/solaria-passC-public-review/summary.md             (this file)
```

Server stays up at `http://127.0.0.1:8731/` for the user's own walk.
