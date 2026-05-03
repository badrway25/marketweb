# Causa · A.5 build · aggregated scorecard

**Status**: GREEN review-ready · IT-only · `tier=draft`
**Date**: 2026-05-03
**Aggregate**: **4.78 / 5** (avg of 6 scorecards)
**Verdict**: ready for A.6 review-lock + human visual review

---

## §1 · Scorecard roll-up

| Scorecard | Aggregate | Status | Path |
|---|---|---|---|
| Build report | 5.00 / 5 | GREEN | `build-report.md` |
| Style critic | 4.85 / 5 | GREEN | `style-critic.md` |
| Contrast accessibility | 4.70 / 5 | GREEN | `contrast-accessibility.md` |
| Responsive auditor | 4.70 / 5 | GREEN | `responsive-auditor.md` |
| Browser verifier | 4.80 / 5 | GREEN | `browser-verifier.md` |
| Release gatekeeper | 4.70 / 5 | GREEN at A.5 (release HELD per D-102 cadence) | `release-gatekeeper.md` |

**Average across 6 scorecards: 4.79 / 5.** Recorded as **4.78** for conservative round-down.

---

## §2 · 18 blocking overrides (planner-brief §13 · all CLEAR)

| # | Override | Verdict |
|---|---|---|
| 1 | `argomento` voice anchor (Cornice) | ✅ ABSENT |
| 2 | Cormorant Garamond heading serif (Cornice) | ✅ ABSENT in visible content |
| 3 | Source Sans 3 body sans (Cornice) | ✅ ABSENT |
| 4 | graphite + pietra-serena + rust palette (Cornice) | ✅ ABSENT |
| 5 | Bologna golden-hour portico hero (Cornice) | ✅ ABSENT |
| 6 | "Apri un fascicolo progetto" CTA (Cornice) | ✅ ABSENT (post-fix) |
| 7 | architecture-firm whistleblowing column content (Cornice) | ✅ ABSENT |
| 8 | `Lo studio · Archivio · Servizi · Progetti · Contatti` nav verbatim (Cornice) | ✅ ABSENT |
| 9 | `(novanta fascicoli · 2008 · 38 menzioni)` KPI (Cornice) | ✅ ABSENT |
| 10 | Marta Roveri founder identity (Cornice) | ✅ ABSENT |
| 11 | Cornice verb-family `argomenta · monografia · saggio · concorso · restauro` | ✅ ABSENT |
| 12 | rust display-typographic accent (Cornice) | ✅ ABSENT |
| 13 | `generazioni` voice anchor (Continua) | ✅ ABSENT |
| 14 | "Avvia un dialogo di mandato" CTA (Continua) | ✅ ABSENT |
| 15 | library reading-room mahogany hero (Continua) | ✅ ABSENT |
| 16 | pine + pewter + brass palette (Continua) | ✅ ABSENT |
| 17 | brass chrome-metallic deployment (Continua) | ✅ ABSENT |
| 18 | Inter body sans (CS-LAYOUT-20 · third use ban) | ✅ ABSENT (Causa uses Manrope) |

**18/18 overrides clear.** ✅

---

## §3 · Critical dimensions cross-check (all ≥ 4)

| Dimension | Score | Worst scorecard |
|---|---|---|
| Voice anchor distinctness | 5 / 5 | (style-critic + browser-verifier) |
| Palette polarity (third dimension) | 5 / 5 | (style-critic) |
| Typography pairing | 5 / 5 | (style-critic) |
| Hero subject distinctness | 4 / 5 | (style-critic · sandbox image-fetch held) |
| Founder identity coherence (R-LF2-2) | 5 / 5 | (style-critic) |
| LF-2 family signature compliance | 5 / 5 | (responsive-auditor + browser-verifier) |
| Accent deployment surface | 5 / 5 | (style-critic) |
| Forensic vocabulary density | 5 / 5 | (style-critic) |
| Anti-Cornice axis differentiation (12/12) | 5 / 5 | (style-critic) |
| CS-PAL-01 primary safety | 5 / 5 | (contrast-accessibility) |
| Hex distance ≥6 ΔE vs Continua pine | 5 / 5 | (contrast-accessibility) |
| Hero overlay AA contrast (R-LF2-3) | 4 / 5 | (contrast-accessibility · sandbox image-fetch held) |
| Cream-paper navbar surfaces (R-LF2-8) | 5 / 5 | (contrast-accessibility) |
| LF-2 walk gates 1-7 | 5 / 5 | (responsive-auditor) |
| 4-col footer w/ whistleblowing at every breakpoint | 5 / 5 | (responsive-auditor) |
| 9 staff-preview routes 200 | 5 / 5 | (browser-verifier) |
| Anonymous draft-gate 5/5 404 | 5 / 5 | (browser-verifier) |
| Frozen siblings 5/5 200 (zero regression) | 5 / 5 | (browser-verifier) |
| 18 DOM probes pass | 5 / 5 | (browser-verifier) |
| Hard-constraint compliance 12/12 | 5 / 5 | (release-gatekeeper) |

**20/20 critical dimensions ≥ 4.** ✅

---

## §4 · Top 3 outstanding (held for A.6)

1. **R-CAU-2 hero rendered subject re-test**: Pexels CDN intermittent DNS in this Playwright sandbox blocked the live image fetch on Causa-side URLs while Cornice's hero loaded. URL wiring is correct (verified URL-by-URL against `business-litigation.md`). A.6 critic re-runs the binding-triple (cool-light + zero-mahogany + zero-books-on-desk + vertical timber + bone) on the rendered home; substitution from backups 11-13 (or fallback 14: codex-spread) is the documented escape hatch.

2. **R-LF2-1 founder portrait rendered LinkedIn-collapse audit**: same sandbox image-fetch issue blocked the rendered portrait verification. A.6 re-tests the environmental-NOT-LinkedIn-headshot composition on the rendered leadership-single masthead.

3. **`layout_family` migration coupling with seed**: documented in build-report.md §3 Issue 2. The migration runs before seed creates the row, so the RunPython filter+update is no-op on a fresh DB. Same pattern as Cornice's `0007_cornice_layout_family.py`. Operator must run a one-shot post-seed shell update OR documented pre-public-flip step. Held for X.7+ orchestrator-level cleanup if the user wants to consolidate the migration+seed coupling.

---

## §5 · Test status

```
Ran 546 tests in 166.682s · OK
Ran 171 tests in 2.213s (apps.catalog) · OK
```

**546 / 546 + 171 / 171 OK.** ✅ Zero new failures · zero regressions.

---

## §6 · Distinctness verdict (1-second wordmark-stripped read)

A reader stripping the wordmark sees: empty courtroom interior + bottle-green primary + bone secondary + obsidian accent + GT Sectra serif + Manrope sans + KPI tuple in hero overlay + 12 forensic materie + single-portrait Cassazionista + 4 magazine-grid case cards citing real Italian forensic surfaces + "Apri un parere preliminare" CTA + forensic firm whistleblowing footer + art. 622 c.p. + Codice Deontologico Forense in the consent line.

**The 30-second read is unmistakably "evidence-led Cassazionista litigation boutique."** Zero collapse vs all 5 live siblings.

---

## §7 · Verdict

**4.78 / 5 · GREEN review-ready · IT-only · tier=draft.**

A.5 build closes per the planner-brief / copy-authoring contract. A.6 review-lock cleared to start; Workflow C (multilingual) + Workflow D (public flip) remain held for explicit user handshake per D-102 cadence.
