# Causa · A.6 IT review-lock · responsive-auditor

**Phase**: X.6 Step 5 · A.6 review-lock
**Template**: causa-legale (LF-2 · 6th corporate-suite sibling)
**Date**: 2026-05-04
**Verdict**: 4.8 / 5 · responsive matrix clean across 1440 / 880 / 375

---

## §1 · Viewport matrix walked (post-fix · home page)

Per the X.4a Step 1D corporate-suite layout-regression contract, every LF-2
template must hold at @media 1440 / 1280 / 1100 / 880 / 720 / 480. A.6
sampled 1440 (lead) · 880 (burger entry) · 375 (mobile small) on the home.

| Viewport | Capture | Verdict |
|---|---|---|
| 1440 × 900 | `12-home-1440-postfix-viewport.jpeg` + `13-home-1440-postfix-fullpage.jpeg` + `14-home-1440-postfix-revealed-fullpage.jpeg` | ✅ 8/4 hero split + below-fold KPI tuple + drop-cap narrative + 12-cell sectors row + leadership single-portrait + 3+1 magazine grid + cream CTA closer + 4-col footer all render correctly |
| 880 × 900 | `18-home-880-fullpage.jpeg` | ✅ Hero stacks 1-col · CSS-only hamburger drawer activates (per X.4a Step 1D contract) · 12 sectors reflow to 2 rows · magazine grid reflows to single column · footer reflows to 2-col then 1-col · placeholder hero proportional |
| 375 × 800 | `19-home-375-fullpage.jpeg` | ✅ Single column throughout · all sections legible · KPI tuple stacks · CTA pills full-width · footer 4-col stacks vertically · placeholder hero proportional |

---

## §2 · Layout integrity per section (1440 lead viewport · post-fix)

| Section | Width | Height | Notes |
|---|---|---|---|
| Marketplace top bar | 1440 | 32px | back-link + anteprima caption + altri-template-link |
| Navbar (cs-nav--lf2) | 1440 | 92px | cream paper · split wordmark + 5 links + filled bottle-green CTA pill on far right |
| Hero `.photo` (placeholder) | 1425 | 653px | aspect-ratio 24/11 · placeholder bottle-green gradient renders edge-to-edge · KPI overlay bottom-left @ 56px / 40px inset |
| Hero `.below` (8/4 split) | 1440 | ~520px | h1 left (8 cols) · italic side-quote right (4 cols) |
| Narrative essay | 1440 | ~1980px | drop-cap + 4 paras + 3 pull-quotes + sticky 4-link side-rail |
| Sectors-ribbon | 1440 | ~360px | 12 cells in italic Manrope · counter footnote |
| Leadership-single | 1440 | ~720px | 480px portrait + 1fr body grid · gap 72px |
| Magazine grid 3+1 | 1440 | ~880px | hero card 7 cols rows 1/4 · 3 small cards 5 cols stacked |
| CTA closer cream | 1440 | ~480px | centred · cream paper · hairline border |
| Footer 4-col | 1440 | ~520px | brand · pages · contatti · segnalazioni (whistleblowing) |
| Total scrollHeight | — | 9555px | within budget · matches Cornice's ~9500-9700 envelope |

---

## §3 · Responsive findings

| ID | Finding | Severity | Status |
|---|---|---|---|
| A.6-R1 | At 1440, the placeholder hero gradient renders edge-to-edge with `object-fit: cover` semantics (CSS `background-size: cover`). The label "imagery hold..." stays centred at viewport-relative 50% / 50% which means it sits about ~325px from the visible top. PASS. | none | PASS |
| A.6-R2 | At 880, the LF-2 8/4 hero split collapses to single column per the X.4a Step 1D @media query. The KPI tuple stacks vertically inside the credit overlay frame. The placeholder fills the full hero box correctly. | none | PASS |
| A.6-R3 | At 375, the leadership-single grid collapses to single column (portrait stacks above body). The magazine grid 3+1 collapses to 4 cards single-column. The 12-cell sectors ribbon flows to 4-6 lines. Footer 4-col stacks. | none | PASS |
| A.6-R4 | The hamburger checkbox toggle at ≤880 is functional · burger graphite · drawer reveals 5 nav links + CTA pill. Verified via DOM inspection of `cs-nav-toggle` checkbox. | none | PASS |
| A.6-R5 | The marketplace top bar `← Torna a marketweb / Anteprima completa / Altri template business →` reflows correctly at all 3 viewports (becomes 2-col stack at ≤480 per the X.4a Step 1D @media 480 rule). | none | PASS |

**Zero blocking responsive findings.** The placeholder mitigation does NOT
introduce any new responsive deficit because the hero box geometry is
unchanged (the placeholder is just a different `background-image` value
inside the same `aspect-ratio: 24/11 · min-height: 420px` photo container).

---

## §4 · X.4a Step 1D layout regression cross-check

Per the X.4a Step 1D contract, the @media breakpoints 1280 / 1100 / 880 /
720 / 480 + the CSS-only hamburger drawer at ≤880 + the `overflow-x:clip`
root guard + the Playwright PASS 0/0 must all hold. A.6 verified:

- @media 880 hamburger drawer: ✅ activates correctly (sampled at 880 viewport).
- overflow-x:clip root guard: ✅ no horizontal overflow on any sampled
  viewport (375 inclusive).
- Playwright PASS 0/0: not re-run at A.6 (the placeholder mitigation is
  byte-equivalent to A.5 at the layout layer); the X.4a Step 1D evidence
  remains the binding reference.

---

## §5 · Responsive verdict

**Responsive matrix clean.** The placeholder mitigation preserves all
responsive behaviour. Score: **4.8 / 5** (the 0.2 reflects the fact that
A.6 sampled 3 viewports rather than the full X.4a Step 1D 5-viewport matrix
· an A.5b combined re-curate + responsive walk should re-confirm 1280 +
720 + 480 · A.6's narrow scope did not require the full matrix re-walk).
