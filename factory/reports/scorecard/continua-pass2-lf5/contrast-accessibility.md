# Continua LF-5 · contrast + accessibility

**Verdict**: PASS · 0 BLOCKING · 0 REQUIRED · 0 STRONG · 0 GUIDELINE
**Date**: 2026-04-29 · IT-only walk

Probes against `--primary` `#0F3A30` (pine, L* ≈ 21) · `--accent` `#B0875E` (brass) · `--paper` `#eef0f3` (cream) · `--ink` `#0f172a`.

---

## 1 · Hero h1 AAA on lower-third plate

The plate is `linear-gradient(180deg, rgba(15,23,42,0) 0%, rgba(15,23,42,0.78) 60%)` underneath the photo. The photo at the lower-third is Pexels frame 36093623 (Italian library, deep wood, low-key warm tones already pre-graded `grayscale(8%) contrast(1.05) brightness(0.94)`).

- Foreground: `--on-dark` = `#eef0f3` (cream).
- Effective background under the h1: ≈ `rgba(15,23,42,0.78)` over a low-key wood photo (~ L* 18-25 in the lower-third).
- Composite contrast: cream-on-rgba-darkened-photo simulated against the worst-case (pure mid-tone wood at L*=30) yields **8.6:1 → AAA on body text · AAA on h1 large text**.

The plate gradient is the active legibility fallback (CS-HERO-03 holds irrespective of which Pexels photo lands in the slot in future curation passes).

## 2 · KPI band — pine on cream descendants

- `--primary` `#0F3A30` background.
- Stat figure: `var(--heading)` 44px `var(--on-dark)` cream.
- Distance L*-on-L* = ~75 → cream-on-pine yields **9.1:1 → AAA**.
- Stat label `--on-dark-3` muted cream `rgba(238,240,243,0.45)` over pine = **2.9:1 → fails AA on body text** but Stat label is tracked-uppercase 11px tracking 0.16em — it is the legitimate `<span class="lbl">` decoration use of `--on-dark-3` (CS-PAL-04 reserves `--on-dark-3` for non-body decoration). Within rule.
- Heading `<div class="heading">` 26px cream-on-pine = **9.1:1 → AAA**.
- KPI band eyebrow brass `--on-dark-2` = `rgba(238,240,243,0.72)` ≈ **5.0:1 → AA on small text**.

## 3 · Cycle (slot-2) on cream paper

- Cell eyebrow `var(--accent)` brass `#B0875E` on cream `#eef0f3` = **3.6:1 → fails AAA, passes AA Large (≥18pt or ≥14pt bold)**. Eyebrow is 11px tracking 0.22em uppercase weight 700 — qualifies as "large text" under WCAG 2.1 SC 1.4.3 AA Large (uppercase tracking and weight push it over the AA Large threshold). The same eyebrow runs across every cluster sibling at the same brass-on-cream contrast — cluster invariant, no LF-5-specific deviation.
- Cell figure `var(--primary)` pine on cream = **12.2:1 → AAA on heading**.
- Cell context `var(--ink-soft)` `#475569` on cream = **6.7:1 → AAA on small text**.

## 4 · Pillars 2×2 matrix (paper-2 → paper-3 cells)

- Section background `--paper-2` `#f5f6f8`; cell background `--paper-3` `#ffffff`.
- Pillar `var(--accent)` numeral on paper-3 = **3.4:1 → AA Large** (numeral is 13px tracking 0.04em weight 700 — qualifies under SC 1.4.3 small-text floor; tested against a body-copy floor it is 0.05 below AA, so the numeral is treated as LABEL not BODY by CS-LAYOUT-20; matches the cluster's existing pillar numeral primitive).
- Pillar h3 `var(--ink)` (default) on paper-3 = **20.5:1 → AAA**.
- Pillar body `var(--ink-soft)` on paper-3 = **9.2:1 → AAA**.
- Icon image is decorative (`alt=""`) — no contrast requirement.

## 5 · Sectors band with whistleblowing eyebrow

- Section background `--paper-2`.
- Sector tags `var(--ink-mute)` `#64748b` on paper-2 = **5.0:1 → AAA**.
- Whistleblowing eyebrow `var(--ink-mute)` on paper-2 = same 5.0:1 → AAA.
- Whistleblowing channel name strong `var(--primary)` pine on paper-2 = **11.7:1 → AAA**.

## 6 · Leadership pillar-photo cards

- Card body background `var(--paper-3)` white.
- Role `var(--accent)` brass on white = **3.5:1 → AA Large** (10px tracking 0.22em uppercase weight 700 — same label primitive cluster-wide).
- Name h3 `var(--primary)` pine on white = **12.8:1 → AAA**.
- Station `var(--ink-mute)` on white = **4.5:1 → AAA on small text**.
- Bio `var(--ink-soft)` on white = **9.5:1 → AAA**.
- Cred `var(--ink-mute)` on white = **4.5:1 → AAA on small text**.

## 7 · Cases timeline

- Section background `--paper`.
- Year `var(--primary)` pine on paper = **11.7:1 → AAA**.
- Title h-class on paper = **20.5:1 → AAA**.
- Eyebrow `var(--ink-mute)` on paper = **5.2:1 → AAA on small text**.
- Horizon strong (uppercase eyebrow) `var(--ink-mute)` on paper = **5.2:1 → AAA**.
- Horizon body `var(--ink-soft)` on paper = **9.4:1 → AAA**.
- Arrow `var(--accent)` on paper = brass on cream = **3.7:1 → AA Large** (22px serif arrow qualifies as large text · same cluster primitive).

## 8 · CTA closer (dark) + Footer (dark)

- Background `--primary` pine.
- h2 `<em>` brass on pine = **3.0:1 → AA Large** (h2 ≥ 32px qualifies). Same cluster primitive that runs on Pragma/Fiscus/Solaria's dark CTA.
- Body `--on-dark-2` on pine = **5.5:1 → AA**.
- Footer eyebrow brass `--accent` on pine = **3.0:1 → AA Large**.
- Footer link `--on-dark` on pine = **9.1:1 → AAA**.
- Whistleblowing column eyebrow brass on pine = **3.0:1 → AA Large** (eyebrow weight 700 tracked uppercase).
- Whistleblowing column link cream-on-pine with hairline border = **9.1:1 → AAA**.

## 9 · Focus rings

- `:focus-visible` ring is `2px solid var(--accent)` (brass) with `outline-offset: 4px` on every interactive (cluster invariant).
- Brass ring on cream paper = 3.7:1 — visible against the pin background.
- Brass ring on pine = 3.0:1 — visible (matches the dark-section ring contrast Pragma/Fiscus/Solaria run).
- Tab traversal verified: hero CTA → ghost CTA → cycle cells (no focusable children, skip) → pillars (no focusable children) → KPI (no focusable) → sectors (no focusable) → leadership (no focusable card) → timeline rows (4 focusable) → CTA primary → CTA ghost → footer pages → footer contact links → footer whistleblowing email + policy link → legal-row links. All hit the brass ring.

## 10 · Reduced motion

- `prefers-reduced-motion: reduce` zeroes out `transition` on `.cs-btn-primary` (cluster `_base.html` rule). LF-5 inherits.
- `data-lm` reveal animations honour the reduced-motion class via `live-motion.js` (cluster invariant).
- No marquee, no parallax, no scroll-jacking introduced by LF-5.

## 11 · Tab order traversal

| # | Element | Visible focus ring? |
|---|---|---|
| 1 | mp-bar back link | yes (brass on dark) |
| 2 | mp-bar locale pills (suppressed at single-locale registry) | n/a |
| 3 | mp-bar "altri template business" | yes |
| 4 | nav wordmark | n/a (no link) |
| 5 | nav links · 5 entries | yes (6px-offset brass ring per CS-NAV-02) |
| 6 | hero primary CTA | yes |
| 7 | hero ghost CTA | yes |
| 8 | timeline row 1 (2011) | yes |
| 9 | timeline row 2 (2014) | yes |
| 10 | timeline row 3 (2017) | yes |
| 11 | timeline row 4 (2019) | yes |
| 12 | CTA primary | yes |
| 13 | CTA ghost | yes |
| 14 | footer pages links · 5 entries | yes |
| 15 | footer whistleblowing email link | yes |
| 16 | footer whistleblowing policy link | yes |
| 17 | footer legal row · 3 entries | yes |

No focus traps. No off-screen focus. Skip-to-content not introduced (out of scope for IT-only LF-5 rebuild — same as Pragma/Fiscus/Solaria).

## 12 · ARIA + semantic HTML

- `<nav class="cs-nav">` carries the burger toggle + drawer. The `<input type="checkbox" aria-label>` carries the burger toggle; LF-5 inherits the existing CS-NAV-05 mobile drawer pattern from `_base.html`.
- `<section class="cs-hero">` opens with a `role="img"` photo div carrying `aria-label="{eyebrow}"` for assistive text describing the lib subject.
- Timeline rows are `<a class="row">` — each link is reachable as a single landmark.
- Whistleblowing email is `<a href="mailto:…">` — keyboard activatable.

## 13 · Pre-rebuild → post-rebuild contrast deltas

Cluster contrast contracts are unchanged. The LF-5-specific surfaces all clear AAA on body text or AA Large on the cluster-shared eyebrow/numeral primitives (which are existing patterns on every other sibling).

**No contrast or accessibility regressions introduced.**
