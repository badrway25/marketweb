# Causa · A.6 IT review-lock · release-gatekeeper

**Phase**: X.6 Step 5 · A.6 review-lock
**Template**: causa-legale (LF-2 · 6th corporate-suite sibling)
**Date**: 2026-05-04
**Verdict**: HOLD · NOT YET LOCKED FOR USER VISUAL HANDSHAKE

---

## §1 · Gate decision matrix

| Gate | Required state | Current state | Status |
|---|---|---|---|
| Test suite | 546 / 546 OK | 546 / 546 OK | ✅ |
| Frozen sibling regression | 0/5 regression | 0/5 regression (5/5 byte-equivalent) | ✅ |
| Tier preservation | tier=draft on causa-legale row | tier=draft (DB-verified) | ✅ |
| Anonymous draft-gate | 4/4 must-be-404 + 1 must-not-list | 4/4 + 1 = PASS | ✅ |
| Public catalog count | unchanged at 24 published_live | 24 published_live + 1 draft | ✅ |
| Trust counter | "24+" preserved | "24+" preserved | ✅ |
| Apps-untouched | editor / projects / commerce zero edits | zero edits verified | ✅ |
| LF-2 family file untouched | _layouts/lf2/* zero edits | zero edits verified | ✅ |
| Voice anchor verbatim 2/2 | 2 surfaces verified live | 2/2 verified | ✅ |
| Em audit | ≥10 forensic ems on home | 12 verified | ✅ |
| Navbar pill consistency | "APRI UN PARERE PRELIMINARE" on all 9 pages | 9/9 verified | ✅ |
| Hero subject reads courtroom-interior | hero photo verified live | **HELD · placeholder pending A.5b re-curate** | ⛔ |
| Founder portrait reads chambers-environmental | portrait verified live | **HELD · placeholder pending A.5b re-curate** | ⛔ |
| Case-card photos read public-record-evidence | 4 case cards verified live | **HELD · placeholders pending A.5b re-curate** | ⛔ |
| Pexels CDN issue clearly classified | sandbox vs real-product distinction | **DISAMBIGUATED · real product defect · curator pack must be re-curated** | ✅ |

**12 / 15 gates GREEN · 3 / 15 gates RED (all imagery-axis · all auto-resolve
at A.5b imagery re-curate).**

---

## §2 · Workflow C / Workflow D gating

Per the cluster's D-102 cadence + R-SOL-8 / CS-BLOCK-13 binding:

- **Workflow C (multilingual EN/FR/ES/AR + AR Naskh) is HELD.** Cannot
  proceed until A.5b imagery re-curate completes + A.6b rapid review
  re-verifies the priority surfaces (hero · founder · case-cards) live.
  Translating placeholder content would lock the imagery-hold pattern
  across 5 locales, which the user-handshake gate would never accept.

- **Workflow D (public flip · tier=draft → published_live) is HELD.** Cannot
  proceed until workflow C completes + a second user handshake on the
  multilingual walk. Currently locked behind workflow C.

---

## §3 · A.5b re-curate prerequisite (the recommended next workstream)

The orchestrator should authorise **Phase X.6 Step 5b · imagery re-curate**:

1. Re-curator does fresh Pexels search for the 6 primary slots + 4
   magazine-grid extras with **mandatory live-URL verification** at curator
   commit time (no LLM-fabricated IDs · every URL navigated and
   screenshotted before commit · attribute every photo URL to a real Pexels
   page).
2. Re-curator updates `docs/content-factory/imagery/packs/business-
   litigation.md` with the verified URLs + per-URL captions that match
   what the URL actually shows.
3. Re-curator updates `apps/catalog/preview_imagery.py business-legale`
   pool with the verified URLs.
4. Re-curator updates `apps/catalog/template_content_causa.py` to replace
   the `_IMAGERY_HOLD_PLACEHOLDER` with the new verified URLs (revert the
   A.6 mitigation).
5. **A.6b rapid review-lock** re-walks the priority surfaces (hero · founder
   · case-cards) live to confirm:
   - hero reads courtroom-interior (planner-brief §4 binding triple)
   - founder portrait reads chambers-environmental + 60s + Cassazionista (R-LF2-1 mitigation)
   - case-card visual register reads public-record-evidence (high-court exterior + fascicoli + bench-chair + codex-spine)
   - R-CAU-2 cool-vs-warm differentiation vs Continua holds
6. On A.6b GREEN: orchestrator re-issues user-handshake invitation with the
   now-fully-locked IT draft.

If A.5b cannot land within budget, the orchestrator's fallback options are:
- **HOLD**: keep Causa at IT draft + imagery hold indefinitely until
  imagery re-curate is feasible.
- **A.7 narrow re-author on copy axis**: per Cornice precedent, a copy-only
  re-pass that addresses any user feedback on the COPY/CHROME/TYPOGRAPHY/
  PALETTE layers (which ARE locked at A.6).

---

## §4 · Release-gatekeeper verdict

**HOLD · NOT YET LOCKED FOR USER VISUAL HANDSHAKE.** Causa IT is review-
lockable for everything-except-imagery. The imagery axis (3 of 15 gates)
requires the A.5b re-curate workstream before user-handshake can proceed.

**Recommended next action**: orchestrator authorises Phase X.6 Step 5b
imagery re-curate.

Score: **HOLD verdict** — not a numeric score (the gatekeeper's role is to
issue PASS / HOLD / FAIL, not to score; the numeric panels above sit at
4.0 — 4.8).
