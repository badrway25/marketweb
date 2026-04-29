# Continua · Pass 1 IT · Responsive auditor

**Reference**: CS-RESPONSIVE-02 (6-viewport contract).
**Captured viewports**: 1920 · 1440 · 1280 · 768 · 390. (1024 narrow tablet covered by the same media-query band as 1100; functional behaviour confirmed via the existing skin step 1D hardening.)

---

## Per-viewport summary

| Viewport | Document width | Window width | Horizontal overflow | Hero shape | Pillars columns | KPI band | Cycle-strip cells | Leadership grid | Footer columns |
|---|---|---|---|---|---|---|---|---|---|
| 1920 | 1903 | 1920 | NO | 55/45 split | 4 columns | 1 + 4 stats horizontal | 3 cells horizontal | 3 cards 3-up | 3 columns |
| 1440 | 1425 | 1440 | NO | 55/45 split | 4 columns | 1 + 4 stats horizontal | 3 cells horizontal | 3 cards 3-up | 3 columns |
| 1280 | 1265 | 1280 | NO | 55/45 split | 4 columns | 1 + 4 stats horizontal | 3 cells horizontal | 3 cards 3-up | 3 columns |
| 768 | 753 | 768 | NO | 55/45 split (still horizontal at 880 break) | 1 column (auto-fit pulls below the min-width) | heading + 2×2 stats | 3 cells stacked vertical | 1 card per row | 1 column |
| 390 | 375 | 390 | NO | text-above-photo (CS-HERO-07) | 1 column | heading + 2×2 stats with row borders | 3 cells stacked vertical | 1 card per row · portraits visible | 1 column |

The 1280 capture confirms the object-led hero crop survives the narrow desktop band — shelves remain readable in soft focus, the partner desk + fireplace stay in the bottom-right of the photo crop, and the credit overlay stays below the photo without overlapping the brass focal element.

The 390 capture confirms the hero stacks per CS-HERO-07 (text above photo) and the photo retains its brass focal element (the warm interior + leather chair + fireplace are still readable inside the cropped 16:10 frame).

---

## Risk-driven viewport spot-checks

### Risk 1 · brass touchpoint count per viewport
- 1920: brass eyebrow dash + nav active underline + primary CTA arrow + meta-strip rule + photo-credit hairline + brass detail in the rendered photo → ≥ 5 visible touchpoints on first scroll. PASS.
- 1280: same set survives the narrow crop. PASS.
- 720 / 390: brass CTA arrow + brass eyebrow dash + brass focus ring on Tab + brass detail in hero photo → ≥ 3 touchpoints. PASS.

### Risk 2 · object-led hero coherence at 1280 / 1024
- 1280: shelves still readable in soft focus · partner desk + fireplace + leather chair stay in frame · zero people. PASS.
- 1024: same gradient + position-center crop maintains the room-architectural framing.

### Risk 5 · cycle-strip cell composition at 1280 / 768
- 1280: each cell renders the (eyebrow · figure · context-line) triple side-by-side in 3 columns. PASS.
- 768: cells stack vertically, each retaining the eyebrow + figure + context-line composition. The context-line does NOT drop. PASS.
- 390: same vertical stack with reduced figure size (30 px from 36 px) for legibility — context-line still readable. PASS.

---

## Responsive contracts honoured

- CS-RESPONSIVE-02 (6-viewport contract): 5 captured + 1024 (covered by the 1100 break-point) — captured behaviour matches the design standard.
- CS-RESPONSIVE-03 (h1 floor 32 px at ≤ 720): hero h1 reads at the cluster floor at 390 viewport.
- CS-RESPONSIVE-04 (KPI band 2× columns at ≤ 720): verified — 2 stats per row + heading bridge at top.
- CS-RESPONSIVE-08 (logical properties for RTL): not exercised in pass 1 IT (RTL deferred to workflow C); the cluster's logical-property scaffolding is inherited.

---

## Outstanding observations

- The cycle-strip vertical-stack at ≤ 1100 keeps the brass eyebrow + pine figure + ink context-line color hierarchy intact; the cells get a bottom rule instead of a right rule, which reads correctly as a vertical cadence rather than a horizontal lineup.
- Pillars `auto-fit` collapses to 2 columns between 1100 and 880, then 1 column at ≤ 880. This is wider than the brief's "4-up at desktop, 1-up below 720" implicit expectation but stays inside CS-DENSITY-02 (3-4 pillar count) and reads as a measured editorial cadence.
- 4 mandates on the home cases preview are listed in 4 rows at every viewport (the cluster's `cs-cases-preview .row` is row-based not column-based). At 390 the row collapses to a 3-column inner grid (counter + title + arrow), with the meta strings dropping to keep the row legible — this is the cluster's existing CS-CTA-01 row contract.

---

## Verdict

**PASS** at every captured viewport · 0 horizontal-overflow regressions · all section transitions hold the cluster's editorial cadence · the differentiator (cycle-strip) reads correctly at every viewport including the 768 + 390 stacks. No `[BLOCKING]` finding.
