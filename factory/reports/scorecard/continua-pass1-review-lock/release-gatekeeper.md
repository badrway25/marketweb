# Continua · Pass 1.5 Review-Lock · Release gatekeeper

**Reference**: `factory/agents/release-gatekeeper.md`
**Date**: 2026-04-29
**Predecessor pass**: `factory/reports/scorecard/continua-pass1-it/release-gatekeeper.md` (pass-1 IT · GREEN at draft)
**Tier requested**: keep at `tier: draft` per the pass-1 brief's D-102 cadence. The lock-pass restores DB→registry parity; it does **not** flip tier.

---

## 1 · What this gatekeeper checks

Pass 1.5 is operational, not visual. The gatekeeper here verifies one new property and one preserved property:

| Property | Source |
|---|---|
| (NEW) DB-side `WebTemplate.tier` matches `TEMPLATE_REGISTRY.json` for `continua-stewardship` | The whole reason this pass exists |
| (PRESERVED) Pass-1's GREEN scorecard verdict (4.74 / 5 · 0 BLOCKING · 0 deviation) | Pass-1's `release-gatekeeper.md` |

The visual scorecard, contrast/accessibility report, responsive auditor, and style-critique are **not** re-rendered — pass-1's verdicts remain authoritative because no source code, no content, no template was modified by this pass.

---

## 2 · Layer 1 · CLI + standards (operational)

| Check | Result |
|---|---|
| `python manage.py sync_template_tiers --dry-run` (pre-pass) shows 1 planned change `published_live → draft` | PASS |
| `python manage.py sync_template_tiers` (real) writes 1 row | PASS |
| `python manage.py sync_template_tiers --dry-run` (post-pass) shows 0 planned changes | PASS — idempotent |
| Catalog distribution post-sync | 22 published_live / 1 draft (Continua is the 1 draft) |
| Registry tier_reason still aligned with the pass-1 narrative | PASS — registry untouched |

Layer 1 — GREEN.

---

## 3 · Layer 2 · Live walk (review-path legitimacy)

| Check | Result |
|---|---|
| Anonymous probe of `/preview/` → 404 | PASS |
| Anonymous catalog `/templates/business/` does NOT list Continua | PASS |
| Staff `/preview/?preview=1` → 200 | PASS |
| Staff `/templates/business/?preview=1` lists Continua among 5 cards | PASS |
| Internal href `?preview=1` propagation on the rendered home | PASS (11/11) |
| Each of the 4 case-study detail posts reachable via the nav-driven path | PASS (5/5 including the mandati list) |
| Visual carry-forward (hero capture matches pass-1 reference) | PASS |
| Editor / projects / commerce surfaces unaffected | PASS (zero source change) |

Layer 2 — GREEN.

Detail in `browser-verifier.md` and `factory/reports/browser-verification/continua-pass1-review-lock.md`.

---

## 4 · Layer 3 · Aggregation

| Check | Result |
|---|---|
| Pass-1 scorecard aggregate carries forward at 4.74 / 5 | PASS — no source change invalidates pass-1's grading |
| User-handshake binary SHIP/HOLD on LIVE flip | DEFERRED — workflow C scope, unchanged from pass-1 |
| Distinctness 5/5 vs Pragma + Fiscus + Solaria | PRESERVED — visual outcome unmodified |
| Live DOM matches build brief at landing | PRESERVED |
| Pexels-only re-confirmed on live render | PRESERVED |
| No deviation note flags an unresolved `[BLOCKING]` rule | NONE flagged |
| No conservative override invoked | NONE invoked |

Layer 3 — GREEN at the draft-tier scope (unchanged).

---

## 5 · Pre-existing finding documented but NOT fixed

The home preview-band rows (`.cs-cases-preview .row`) on the shared `templates/live_templates/business/corporate-suite/home.html:660` use a hardcoded `'case-studies'` parent slug in `{% url 'catalog:live_template_post' … 'case-studies' post.slug %}`. Continua's case_study_list page slug is `mandati`, so these 4 home-band hrefs route to a non-existent page and 404. **Same defect affects Fiscus (`casi-seguiti`) and Solaria (`casi`); only Pragma's literal slug matches.**

This is a pre-existing pass-1 carryover and was not introduced by review-lock. The legitimate review path is intact via the nav (home → Mandati nav link (200) → list (200) → detail (4/4 → 200)).

The recommended minimum fix is documented in `build-report.md §4`. It is **NOT** applied in this pass per the hard constraints "be conservative" and "implement only the minimum correct fix" — the legitimate path already exists, and the proper fix touches a shared file that affects 3 sibling templates and 5 locales for two of them.

**Recommendation**: open a small follow-up scoped to "case-studies parent-slug parity across corporate-suite siblings" and treat as cluster maintenance, separate from Continua's review-lock pass.

---

## 6 · Walk freshness gate

All walk verdicts dated 2026-04-29 — same day as the lock-pass and within the 30-day freshness window per `BROWSER_QUALITY_GATE §3`.

---

## 7 · Release decision

**Tier action**: NO CHANGE. `continua-stewardship` stays at `tier: draft` in both `TEMPLATE_REGISTRY.json` AND in the dev DB. Running `sync_template_tiers` again would print "0 tier(s) updated" — the state is idempotent.

**Public-flip readiness**: NOT YET. That is workflow C territory. The brief explicitly defers EN/FR/ES/AR + AR RTL parity walks + user handshake to a separate pass. Pass 1 was the workflow A endpoint; pass 1.5 closes the operational drift left after pass 1 without changing the workflow C entry conditions.

**Cascade documented for the eventual workflow C public-flip pass** (use as recipe at that time, NOT now):

1. Author the four missing locale trees (EN, FR, ES, AR) with verbatim-in-translation voice anchor (`generazioni` → equivalents per the locale-pinned register list in the build brief). Mirror the IT shape exactly — the 5-page contract, the 4 detail posts, the form gate field set.
2. Author AR RTL parity (heading-font swap on `<html dir="rtl">`, mirrored hero crop, RTL-safe icons).
3. Run a 5-locale × 5-page browser walk in a staff session against the staff-preview path (Solaria Pass B precedent).
4. Walk all internal hrefs in each locale to confirm they propagate `?lang=` + `&preview=1` correctly (Solaria Pass C precedent · the chrome already does this for Continua because it shares the corporate-suite shell).
5. Apply the test-suite tier cascade per Solaria Pass D's recipe: 8 hardcoded asserts in `apps/catalog/tests.py` flip `21→22→23` (and the standard price-tier count rolls up by 1 at the affected line); the exact line-numbers will need re-resolution against the post-Solaria-Pass-D codebase.
6. Flip `TEMPLATE_REGISTRY.json` `tier: draft → published_live` and update the `tier_reason` narrative.
7. Run `python manage.py sync_template_tiers` to apply to DB.
8. Anonymous walk of all 5 locales × 5 pages must return 200.

**Operator action requested at end of this lock-pass**: take over the human visual review at the URL kept open. The three pass-1 checkpoints still apply (brass landing on first scroll · hero photo coherence · cycle-strip framing) — they were not re-graded by this pass and were not invalidated by it.

**Verdict**: PASS at the review-lock scope. Continua is reviewable in a legitimate and consistent way; DB/registry mismatch removed; no LIVE auto-flip. Workflow C remains the binding next step for public flip.
