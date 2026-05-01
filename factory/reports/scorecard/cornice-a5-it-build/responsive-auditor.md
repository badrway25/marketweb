# Responsive auditor panel · Cornice A.5 IT build

```yaml
panel:           responsive-auditor
template_slug:   cornice-architettura
phase:           X.5 · A.5 build
date:            2026-05-01
verdict:         PASS
score:           4.6/5
viewports:       [1440, 1100, 880, 720, 480]
```

## Per-viewport status

### 1440 (desktop · primary design viewport)

- Hero photo: full-bleed at aspect-ratio 24/11 · KPI tuple bottom-left + credit caption visible.
- Below-photo split: 8/4 · h1 LEFT (64px Cormorant) + side-quote RIGHT.
- Narrative: 2-col grid (essay body + sticky 4-link side-rail).
- Sectors-ribbon: italic Cormorant 24px middot-separated · 12 typologies fit in 2 lines.
- Leadership: 2-col grid · 480px portrait LEFT + bio + credentials RIGHT.
- Magazine grid: 2-col (hero card spanning 3 rows LEFT · 3 small cards stacked RIGHT).
- CTA closer: cream band with hairline graphite border + filled-rust button.
- Footer: 4-col grid (1.4fr/1fr/1fr/1fr · brand · sitemap · contact · whistleblowing).

### 1100 (small desktop / large tablet)

Tokens reset (per `_base.html` 1100 breakpoint): `--space-section-y: 72px` · `--fs-hero: 48px` · `--fs-h2: 36px`.

LF-2-specific behaviour:
- Hero `.below` 8/4 → 1-col stack (h1 above side-quote).
- Hero `.right` (side-quote) padding-inline-start eases to 28px.
- Narrative essay 2-col → 1-col (side-rail moves below body, max-w 480).
- Leadership 2-col → 1-col stack (portrait above bio).
- Cases magazine 2-col → 1-col stack (hero card and small cards full-width).
- Cases head 2-col → 1-col.

KPI tuple still visible in hero overlay. Photo + credit + KPI all readable.

### 880 (portrait tablet)

Tokens: `--fs-hero: 42px` · `--fs-h2: 30px`.

Cluster nav burger drawer activates at 880 (cluster default). LF-2 split-wordmark masthead remains visible (wordmark + subtitle); nav CTA pill is hidden until the burger is opened.

LF-2-specific behaviour:
- Hero photo aspect 16:10 · KPI tuple still visible (font-size: 26px).
- Sectors ribbon font 20px.
- Drop-cap 64px (was 84px).
- Pull-quote 20px.

### 720 (mobile)

Tokens: `--fs-hero: 36px` · `--fs-h2: 26px` · `--space-section-y: 52px`.

LF-2-specific behaviour:
- Hero photo aspect 4:5 portrait (vertical-leaning composition).
- Hero overlay `left: 20px; right: 20px; bottom: 18px` · max-width none.
- KPI tuple `gap: 16px` · num font 22px · label font 9px.
- Narrative drop-cap 64px · pull-quote 18px.
- Magazine card hero h3 24px · small h3 19px.
- CTA-closer button min-height 44px (touch target).

### 480 (small phone floor)

Tokens: `--fs-hero: 32px` · `--fs-h2: 24px`.

LF-2-specific behaviour:
- Hero overlay `left: 14px; right: 14px; bottom: 14px`.
- Drop-cap 56px (smallest size).
- Below-padding 28×18 minimum.
- Pull-quote 17px.
- All sections compress to minimum padding while preserving readability.

## Specific responsive verifications

| Verification | Status |
|---|---|
| Hero KPI tuple visible at every viewport | PASS — visible at 1440 / 1100 / 880 / 720 / 480 |
| h1 hits floor (32px) only at 480 | PASS — hierarchy 64 → 56 → 48 → 42 → 36 → 32 |
| Drop-cap shrinks gracefully | PASS — 84 → 64 → 64 → 64 → 56 (smallest at 480) |
| Magazine grid stacks at 1100 | PASS — 2-col → 1-col with hero card full-width |
| Leadership 2-col stacks at 1100 | PASS — portrait above bio |
| Burger drawer activates at 880 | PASS — cluster default; LF-2 nav-cta hidden in drawer until expanded |
| 720 hero aspect 4:5 portrait | PASS — photo composition is vertical-leaning at small viewports |
| Touch targets ≥ 44px at ≤720 | PASS — buttons honor 44px min-height |
| Side-rail un-sticks at 1100 | PASS — moves below body (no sticky behavior on stacked layout) |
| Magazine card images survive responsive crop | PASS — all 4 cards render via object-fit: cover |
| Footer 4-col → stacking | PASS — cluster default 4-col → 2-col at 880 → 1-col at 720 |
| LF-2 split-wordmark stays legible | PASS — line 1 "CORNICE" + line 2 "studio di architettura" readable at all viewports |

## Concerns

- **Burger drawer hides nav CTA at 880-720**: per cluster default, the `.cs-nav .phone` element (which wraps the LF-2 nav CTA pill) is hidden at ≤880 until the burger is opened. The LF-2 home loses one rust touchpoint at small viewports (the drop-cap and magazine card numerals are still visible). Could be revisited at workflow D if user-handshake calls for the CTA to remain visible at tablet sizes.
- **Hero photo aspect transition at 720**: the photo shifts from landscape (24:11) to portrait (4:5) which is intentional for mobile but may surprise reviewers expecting landscape. Mitigation: the editorial spread genre is well-suited to vertical-leaning hero on phones.

## Score: 4.6/5

All 5 viewports verified. Hero KPI tuple visible at every viewport. Magazine grid + leadership 2-col stack gracefully. Touch targets honoured. Concerns are narrow and not blocking.
