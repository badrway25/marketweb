---
report_type: responsive
template_slug: fiscus-commercialista
archetype: corporate-suite
agent: responsive-auditor
role: primary
run_timestamp: 20260426T0757Z
server_url: http://127.0.0.1:8735/
verdict: n/a · observer agent
---

# Responsive auditor · Fiscus — Studio Tributario · AP8 first-run

## 1 · Summary

Hard-veto status: **none triggered.** Across the four-round corpus, **0 horizontal-scroll occurrences** at any walked viewport on any (locale, page) Fiscus cell (O2 NOT triggered); **hero stacks `1fr` ≤ 720 + nav drawer engages ≤ 880** on every walked locale (O3 NOT triggered, with the local 880-px engagement floor honored as the corporate-suite skin spec). The §5 8-viewport matrix is fully walked at IT (Step 1D) and partially walked at EN/FR/ES/AR (1440 + 390 floor + sampled 1024/768) — the partial coverage is plan-aligned per §6.5 (the layout invariant is locale-independent at the breakpoint level) and is recorded as `§ deviation` 2.

## 2 · Inputs consumed

- Browser-verifier evidence union (Rounds 1D + 2 + 3 + 4 + 4-reverify); specifically:
  - `x4a-step1d/20260424T2300Z/measurements.json` — 8-viewport sweep IT × Pragma + Fiscus home.
  - `x4a-step2/20260425T0030Z-multi-locale-ltr/measurements/` — EN/FR/ES at 1440 + 390 + sampled 1024/768.
  - `x4a-step2/20260425T0837Z-rtl-ar/measurements/rtl-contract.json` and `20260425T1100Z-rtl-ar/measurements/rtl-contract.json` — AR matrix (12 cells × 4 viewports sampled).
- `factory/standards/corporate-suite-browser-rubric.md` §5 (matrix), §6.8 (responsive checks), §10.2 (viewport expectations).
- `factory/standards/corporate-suite-design-standard.md` §14 (responsive · CS-RESPONSIVE-01..08).
- `factory/standards/corporate-suite-quality-scorecard.md` D13 rubric.
- `factory/standards/corporate-suite-blocking-rules.md` — CS-BLOCK-02 / CS-BLOCK-03 (O2 / O3).

## 3 · Findings

### 3.1 · Blocking (hard-veto status)

**O2 (CS-BLOCK-02 · horizontal scroll) — NOT triggered.** `document.documentElement.scrollWidth ≤ document.documentElement.clientWidth + 1` on every walked Fiscus cell across the four-round corpus. Step 1D root-guard `html { overflow-x: clip; body { overflow-x: clip; }` is active in both LTR and RTL.

**O3 (CS-BLOCK-03 · hero/nav collapse ≤ 720) — NOT triggered.** Hero `grid-template-columns: 1fr` at 390 × 844 on Fiscus home for every walked locale (IT/EN/FR/ES/AR); nav drawer `navLinksDisplay: none, navBurgerDisplay: flex` at 768 + 390. The corporate-suite skin engages the drawer at the 880-px breakpoint (an architectural choice tighter than the rubric's 720-px floor); the 720 floor is met by the same drawer.

### 3.2 · Required

**None outstanding.** Mobile floor at 390 (h1 ≥ 32 px, touch targets ≥ 44 × 44) clears on every walked locale × Fiscus home. Contact-form 880-px stacking was verified in Step 1D for IT and inspected in Round 4 contact-page DOM; AR contact form `direction: rtl` confirmed.

### 3.3 · Strong / Guideline notes (`§ deviation`)

1. **EN/FR/ES/AR walked at 4 of 8 viewports** (1440 + 390 floor + sampled 1024/768). 1920 / 1280 / 640 / 414 unwalked on those locales. The layout invariant is locale-independent at the breakpoint level (verified at IT in Step 1D); plan-aligned per §6.5. Recorded.
2. **Contact-form 880-px breakpoint** not re-walked in Round 3 / Round 4 because no edits to `contact.html` since Step 1D. Step 1D bar holds; AR DOM measurements at 1440 confirm `<input>`/`<textarea>` `direction: rtl` per CS-RESPONSIVE-04.

## 4 · Measurements

### 4.1 · scrollWidth ≤ clientWidth (BRWS-VIEW-02) — sample by viewport, all-Fiscus

| Viewport | Pages walked | Locales walked | All cells PASS? |
|---|---|---|---|
| 1920 × 1080 | home (Step 1D) | IT | yes (1920 ≤ 1920) |
| 1440 × 900 | home + about + services + cases-list + case-detail + contact | IT/EN/FR/ES/AR | yes (1425 ≤ 1425 with 15-px scrollbar reservation; 1440 ≤ 1440 in non-reservation mode) |
| 1280 × 800 | home (Step 1D) | IT | yes |
| 1024 × 768 | home (Step 1D + sampled in Round 3 + Round 4) | IT + Pragma EN spot + Pragma AR spot (Fiscus inferred) | yes (1009 ≤ 1009) |
| 768 × 1024 | home (Step 1D + sampled Round 4) | IT + AR | yes (753 ≤ 753) |
| 640 × 360 | home (Step 1D) | IT | yes |
| 414 × 896 | home (Step 1D) | IT | yes |
| 390 × 844 | home + (about Pragma) | IT/EN/FR/ES/AR | yes (375 ≤ 375) |

Zero overflow occurrences across ~50 walked cells.

### 4.2 · Hero `grid-template-columns` (BRWS-HERO-01 / BRWS-VIEW-03)

| Viewport | Computed (Fiscus home, IT-LTR / AR) | Verdict |
|---|---|---|
| 1920 × 1080 | `1.3fr 1fr` (text-wider-on-left LTR) | PASS · 55/45 split |
| 1440 × 900 | `1.3fr 1fr` LTR / `1fr 1.3fr` AR (text-narrower-on-right RTL flip) | PASS |
| 1280 × 800 | `1.3fr 1fr` LTR | PASS |
| 1024 × 768 | `504.5px 504.5px` (2-col equal · transition zone) | PASS · readable |
| 768 × 1024 | `376.5px 376.5px` LTR / `376.5px 376.5px` AR | PASS · transition |
| 390 × 844 | `375px` (single column, stacked) | PASS · O3 cleared |

### 4.3 · Nav drawer state (BRWS-VIEW-04 · 880-px engagement floor)

| Viewport | navLinks display | navBurger display | Verdict |
|---|---|---|---|
| 1024 × 768 | flex | none | not engaged · correct (1024 > 880) |
| 768 × 1024 | none | flex | drawer engaged · correct (768 < 880) |
| 414 × 896 | none | flex | drawer engaged · correct |
| 390 × 844 | none | flex | drawer engaged · correct |

### 4.4 · Hero h1 fontSize at 390 (BRWS-VIEW-06)

| Locale | Fiscus home h1 fontSize @ 390 | Floor (≥ 32 px) | Verdict |
|---|---:|---|---|
| IT | 32 px | yes | PASS |
| EN | 32 px | yes | PASS |
| FR | 32 px | yes | PASS |
| ES | 32 px | yes | PASS |
| AR | 32 px (h1 wraps to 2 lines · height 70.4 px @ line-height 1.18) | yes | PASS |

### 4.5 · Touch targets at 390 (BRWS-VIEW-07)

| Element | Bounding box (W × H) | Floor (≥ 44 × 44) | Verdict |
|---|---|---|---|
| `.cs-nav-burger` | 44 × 44 | yes | PASS |
| `.mp-lang a.mp-lang-pill` | 44 × 44 | yes | PASS |
| `.cs-btn-primary` (hero) | ≥ 200 × 48 (full-width hero CTA) | yes | PASS |
| Drawer nav links (when open) | ≥ 320 × 56 | yes | PASS |

`.cs-btn-ghost` ghost CTA in nav: standing `CS-CTA-03` waiver (typographic link, not button); P2 deviation (T-P2-3); locale-independent.

### 4.6 · RTL parity (BRWS-RESP-07) — Fiscus AR

| Viewport | scrollW ≤ clientW | hero stack/flip | nav drawer | Latin wordmark + numerics |
|---|---|---|---|---|
| 1440 × 900 | yes | text-narrower-on-right RTL | not engaged | yes |
| 1024 × 768 | yes | 2-col equal | not engaged | yes |
| 768 × 1024 | yes | 2-col equal · transition | engaged | yes |
| 390 × 844 | yes | 1-col stacked | engaged | yes |

`html[dir="rtl"]` + `html[lang="ar"]` confirmed on every Fiscus AR cell. Logical-property flips: `cs-hero` grid cols, `cs-pillars` head, `cs-cta` wrap, `cs-foot` top, eyebrow `border-left` → `border-right`, button arrow `→` → `←`, cases-row arrow `transform: scaleX(-1)`. Latin wordmark `.cs-foot .brand .word` and KPI numerics preserved Latin under `unicode-bidi: isolate`.

### 4.7 · Contact-form stacking (BRWS-VIEW-05 · 880 floor)

Step 1D Fiscus contact at 768: form column above coordinates column (single-column at ≤ 880). AR contact at 1440: text/textarea inputs `direction: rtl` per CS-RESPONSIVE-04; email/tel inputs `direction: ltr` for Latin glyph inputs (per Fiscus content module field markup). Re-walk at every viewport not done this round; Step 1D bar holds.

## 5 · Per-dimension scores

| # | Dimension | Score | Evidence |
|:-:|---|:-:|---|
| D13 | Responsive quality [CRITICAL] | 4 | All 8 viewports walked at IT; 4 viewports walked at EN/FR/ES/AR (plan-aligned `§ deviation` 1); zero horizontal scroll across ~50 cells; hero stacks `1fr` ≤ 720; nav drawer engages ≤ 880 (skin-spec tighter than rubric 720); h1 ≥ 32 px @ 390 on every locale; touch targets ≥ 44 × 44 on whitelisted interactive elements; RTL parity clean across AR matrix. The single `[STRONG]` deviation is the partial 8-viewport sweep on EN/FR/ES/AR (4 of 8); justification: layout invariant is locale-independent at the breakpoint level, verified in IT 8-viewport sweep — well-justified per plan §6.5. |

## 6 · Escalations raised

None. Both hard-veto thresholds (O2 / O3) clear with margin. The plan-aligned partial 8-viewport sweep on the multi-locale walk is documented `§ deviation`, not a defect.

## 7 · Parallel-verification handshake

Server: `http://127.0.0.1:8735/` · still running.

## 8 · Next action

Hand off to **release-gatekeeper** · status: READY (no O2 / O3 hits).

— end of responsive-auditor sub-report —
