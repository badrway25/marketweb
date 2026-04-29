# Continua · Pass 1 IT · Browser-verification index

**Date**: 2026-04-29
**Walk artefact root**: `factory/reports/browser-verification/continua-stewardship/it/20260429/`
**Scorecard packet**: `factory/reports/scorecard/continua-pass1-it/`

The walk was performed live via Playwright MCP against a local Django dev server at `http://127.0.0.1:8088`. This index summarises the captures, the walk-time anomalies caught, and the five risk-mitigation verifications.

---

## Captures filed

```
factory/reports/browser-verification/continua-stewardship/it/20260429/
  home-1920-firstscroll.png            · Continua hero · 1920 viewport
  home-1280-firstscroll.png            · Continua hero · 1280 viewport
  home-1440-fixed-em.png               · Continua home · 1440 fullPage (final)
  home-1440-final.png                  · Continua home · 1440 fullPage (pre-em-fix · diagnostic)
  home-1440-revealed.png               · Continua home · 1440 fullPage (pre-em-fix, after motion override)
  home-1440-after-recurate.png         · Continua home · 1440 fullPage (post imagery re-curate, pre-em-fix)
  home-1440-fullpage.png               · Continua home · 1440 fullPage (initial · with broken slot 0 imagery)
  home-768-fullpage.png                · Continua home · 768 fullPage
  home-390-fullpage.png                · Continua home · 390 fullPage
  _compare-pragma-1920.png             · Pragma hero side-by-side · 1920
  _compare-fiscus-1920.png             · Fiscus hero side-by-side · 1920
  _compare-solaria-1920.png            · Solaria hero side-by-side · 1920
  _curate-hero-207658.png              · Rejected slot 0 (Scrabble tiles)
  _curate-cand-36093623.png            · Approved slot 0 (historic library room)
  _curate-cand-28747091.png            · Alt slot 0 candidate (cozy bookshelf · portrait orientation, not selected)
  _curate-feat-4050291.png             · Rejected feature candidate (woman on sofa with laptop)
  _curate-port60-2379004.png           · Rejected senior-steward candidate (young man in T-shirt)
```

Total: 12 PNG captures (5 Continua viewports + 1 narrow-desktop firstscroll + 3 sibling compares + 5 imagery curate-trail diagnostics).

---

## Walk-time anomalies caught

### Anomaly 1 · imagery-curator failures (Risk 2 catch)

The initial imagery URLs were guess-by-pattern Pexels IDs that hadn't been verified against subject. Walk session loaded the home, captured the 1440 fullPage, screenshot review immediately revealed:

- Slot 0 hero rendered "BACK TO SCHOOL" Scrabble-tile composition (Pexels 207658)
- Slot 1 feature rendered woman with laptop on sofa (Pexels 4050291)
- Slot 2 portrait rendered young man in T-shirt (Pexels 2379004)

This is a curator-level fail per Risk 2's "no documents > 1, no human, no laptop" rejection rule and Risk 4's "60s + 40s + visible diversity" demographic triple. The walk caught it within the first capture.

**Fix**: live re-curate via the Pexels search UI from inside the walk session. Each replacement was screenshot-verified before commit:

| Slot | Initial (rejected) | Final (approved) |
|---|---|---|
| 0 hero | 207658 | 36093623 (historic library room with rich wooden interiors) |
| 1 feature | 4050291 | 7045772 (black classic desk + leather chair · light study room) |
| 2 portrait senior | 2379004 | 5333750 (senior woman white hair coral suit · 60s) |
| 3 portrait 40s | 3796217 | 7841828 (mature businessman arms crossed · 40s · African heritage) |
| 4 detail | 6266527 | 36824936 (elegant letter with red wax seal on wooden desk) |
| 5 ambient | 2724664 | 6587827 (marble stairway with golden banister · classic villa daylight) |

### Anomaly 2 · pillars 4-up grid wrap (Risk-adjacent · density)

`cs-pillars .grid` was fixed at `repeat(3, 1fr)` from the original Pragma/Fiscus/Solaria 3-pillar implementation. With Continua's 4-pillar count, the grid wrapped 3+1 — broke the cluster's rhythm.

**Fix**: switched to `repeat(auto-fit, minmax(220px, 1fr))` — backward-compatible with 3-pillar siblings (still renders 3-up at desktop) and lets 4-pillar Continua render 4-up. Verified visually that Pragma's compare capture still shows 3 columns.

### Anomaly 3 · cta-closer `<em>` rendering escaped (Risk-adjacent · voice anchor)

The cta-closer h2 used `{{ page_data.cta_heading }}` (no `|safe`). For Pragma/Fiscus/Solaria the closer didn't carry `<em>` so the missing `|safe` was invisible. Continua restates the voice anchor verbatim (`<em>generazioni</em>`), so the closer rendered literal `<em>` text.

**Fix**: added `|safe` filter to the cta-closer h2 in the shared `home.html`. Same pattern as the existing hero h1 `|safe` on line 464. Verified live.

### Anomaly 4 · `data-lm` reveal-state hiding sections in fullPage capture

`data-lm` reveal elements use IntersectionObserver to fade in on scroll. Playwright's fullPage screenshot doesn't trigger the observer for off-screen elements at capture time, so the captured PNG showed mostly-blank sections.

**Fix (capture-only)**: force-reveal via DOM override (`opacity: 1; transform: none` on every `[data-lm]`) before the screenshot call. Does NOT change production rendering — users see the staggered reveal as designed.

---

## Five risk-mitigation verifications

| Risk | Live verification | Verdict |
|---|---|---|
| R1 Pragma palette echo | 5+ brass touchpoints visible at 1920 first scroll · brass distinguishable from pine + cream at 1280 + 720 · side-by-side stakeholder reading distinguishes Continua as "pine + brass stewardship" vs Pragma as "navy + emerald advisory" | PASS |
| R2 Fiscus hero adjacency | Hero crop at 1920 + 1440 + 1280 + 768 + 390 reads room-architectural · 0 documents · 0 laptop · 0 humans (after slot 0 re-curate) | PASS |
| R3 Pragma stakeholder one-liner | "famiglia · generazioni · Consiglio di Famiglia" surface in first-scroll eyebrow + h1 + subhead + meta-strip; remove-the-studio-name swap test passes | PASS |
| R4 Solaria leadership-photo | 3 distinct demographics readable across coral 60s woman / blue-suit 40s African heritage man / brown 50s woman at 1920 / 1280 / 768 / 390 | PASS |
| R5 Mid-strip cadence framing | Each of 3 cycle cells renders the (eyebrow · figure · context-line) triple at every viewport including 768 + 390 vertical stacks · the context-line does NOT drop | PASS |

ALL FIVE — PASS.

---

## Stop-conditions checklist

15/15 stop-conditions cleared at landing. See `factory/reports/scorecard/continua-pass1-it/browser-verifier.md §stop-conditions-checklist`.

---

## Verdict

**Walk PASS** at the IT-only / draft-tier scope. Server URL kept open at:
`http://127.0.0.1:8088/templates/business/continua-stewardship/preview/`

Workflow C scope (EN/FR/ES/AR + AR RTL parity + LIVE-flip handshake) is OUT OF SCOPE for pass 1.
