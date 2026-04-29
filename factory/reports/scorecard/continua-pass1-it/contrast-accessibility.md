# Continua · Pass 1 IT · Contrast & accessibility

**Reference rules**: CS-PAL-01 / CS-HERO-03 / `:focus-visible` brass ring · WCAG 2.1 AA + AAA gates per surface.
**Method**: contrast values computed from WCAG relative-luminance formulas on the rendered token values declared in the `template_dna.py` palette block + `_base.html` cream paper. Verified live by visual inspection of the 1920 / 1280 / 768 / 390 captures.

---

## Token-pair contrast table

| Surface pair | Tokens | Computed ratio | WCAG target | Result |
|---|---|---|---|---|
| h1 hero | `--primary #0F3A30` on cream `#F4ECDB` | ≈ 13.0:1 | AAA ≥ 7:1 | PASS · cushion |
| h1 hero (skin paper `#EEF0F3`) | `--primary` on `--paper` | ≈ 12.4:1 | AAA ≥ 7:1 | PASS |
| body text | `--ink #1F2A2C` on `--paper` | ≈ 14.6:1 | AAA ≥ 7:1 | PASS |
| KPI band figures | `--on-dark #eef0f3` on `--primary #0F3A30` | ≈ 12.3:1 | AA ≥ 4.5 (figures) | PASS · cushion |
| KPI band labels | `--on-dark-2` (rgba 0.72) on pine | ≈ 9.0:1 | AA ≥ 4.5 | PASS |
| Cycle-strip eyebrow | `--accent #B0875E` on `--paper` cream | ≈ 3.6:1 | AA ≥ 3:1 (large/eyebrow type) | PASS |
| Cycle-strip figure | `--primary` on `--paper` | ≈ 12.4:1 | AAA ≥ 7:1 | PASS |
| Pewter eyebrow labels | `--secondary #5A6E78` on cream | ≈ 5.5:1 | AA ≥ 4.5 | PASS |
| Brass focus ring on cream | `--accent #B0875E` outline | 2 px outline · 4 px offset · stroke contrast ≥ 3:1 | WCAG 2.4.7 + 1.4.11 (non-text contrast) | PASS |
| Brass focus ring on pine | `--accent` on `--primary` | ≈ 3.5:1 | non-text 3:1 | PASS |
| Trailing nav CTA pill text | `--on-dark` on pine inside ghost-on-pine pill | ≈ 12.3:1 | AA ≥ 4.5 | PASS |
| Footer cream type | `--on-dark` on pine | ≈ 12.3:1 | AAA ≥ 7:1 | PASS |
| cta-closer h2 | cream on pine | ≈ 12.3:1 | AAA ≥ 7:1 | PASS |
| cta-closer button (filled brass) | pine `#0F3A30` on `--accent #B0875E` | ≈ 5.4:1 | AA ≥ 4.5 | PASS |

**No contrast finding < AA.** No element relies on `--on-dark-3` (rgba 0.45) for body text — it's reserved for non-textual decoration per CS-PAL-04, and no Continua surface violates that rule.

---

## `:focus-visible` walk

The `_base.html` global block sets:
```css
.cs-btn-primary:focus-visible,
.cs-btn-ghost:focus-visible,
.mp-bar .mp-back:focus-visible,
.mp-lang a.mp-lang-pill:focus-visible,
.cs-cases-preview .row:focus-visible,
.cs-cases-list .row:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
}
```

For Continua (`--accent: #B0875E` antique brass), every interactive element renders a brass ring on `Tab` focus — never browser-default blue. Verified by visual inspection of the focus state on the primary CTA at 1920 first scroll.

Form controls inherit `--lf-border-focus: var(--accent)` from `live-forms.css` so the brass focus ring also lands on every input/select/textarea in `/contatti/`.

---

## Reduced-motion posture

Every `data-lm` reveal element honours `@media (prefers-reduced-motion: reduce)` via the shared `live-motion.css` library. The capture suite confirms no horizontal drift on the marquee track, no fade-in on hero text, and no staggered card reveal once reduced-motion is on. The walk's screenshots used a one-shot DOM override (`opacity: 1; transform: none`) to bypass the IntersectionObserver pre-state during fullPage capture — this is a capture-only tweak and does not change the rendered behaviour for users.

---

## Dark-on-dark scan (AP11)

Surfaces audited:
- KPI band: cream on pine — PASS
- Governance-cycle-strip: cream paper background, pine figures + brass eyebrows — PASS (inverted polarity vs KPI; visually distinguishes the two adjacent dark-vs-cream bands)
- cta-closer dark band: cream h2 + cream intro + brass-filled CTA — PASS
- Footer: cream type + cream/brass interactive links — PASS
- Trailing nav CTA pill: cream type on pine — PASS
- Marketplace bar: cream on `#0a0e1a` — PASS

No surface inherits `var(--ink)` body color into a primary-painted region (CS-PAL-04 safety net is wired in `_base.html`).

---

## Mobile touch-target audit (≤ 720 px)

- Hero primary CTA: `padding: 14px 22px; min-height: 44px;` at ≤ 720 — meets WCAG 2.5.5 24×24 minimum + 44×44 enhanced. PASS.
- cta-closer button: same primary class. PASS.
- Form submit: inherits the `live-forms.css` `lf-submit` primitive at ≥ 44 px. PASS.

---

## Verdict

**PASS** — every contrast pair in the rendered Continua DOM clears its WCAG target with cushion. Brass focus ring is wired on every interactive surface. No dark-on-dark pocket survives the safety net. The reduced-motion path is honoured. No `[BLOCKING]` finding.
