# 127 DESIGN.md

> Auto-generated design system — reverse-engineered via static analysis by skillui.
> Frameworks: None detected
> Colors: 20 · Fonts: 2 · Components: 9
> Icon library: not detected · State: not detected
> Primary theme: dark · Dark mode toggle: no · Motion: expressive

---

## 1. Visual Theme & Atmosphere

This is a **dark-themed** interface with a warm tone. Depth is expressed through layered shadows and subtle surface color variation. Typography pairs **Plus Jakarta Sans** for display/headings with **Inter** for body text, creating clear visual hierarchy through type contrast. Spacing follows a **4px base grid** (compact density), with scale: 2, 4, 6, 8, 10, 12, 14, 16px. The accent color **#f59e0b** anchors interactive elements (buttons, links, focus rings). Motion is expressive — spring physics, layout animations, and staggered reveals are part of the visual language.

---

## 2. Color Palette & Roles

| Token | Hex | Role | Use |
|---|---|---|---|
| bs-emphasis-color | `#000000` | background | Page background, darkest surface |
| mw-surface | `#ffffff` | surface | Card and panel backgrounds |
| bs-secondary-bg-subtle | `#e4e7ec` | text-primary | Headings and body text |
| bs-secondary | `#6b7280` | text-muted | Captions, placeholders, secondary info |
| bs-secondary-text-emphasis | `#27272a` | text-muted | Captions, placeholders, secondary info |
| bs-light-text-emphasis | `#52525b` | border | Dividers, card borders, outlines |
| mw-accent | `#f59e0b` | accent | CTAs, links, focus rings, active states |
| mw-accent-light | `#fbbf24` | accent | CTAs, links, focus rings, active states |
| bs-danger | `#dc3545` | danger | Error states, destructive actions |
| bs-success | `#198754` | success | Success states, positive indicators |
| bs-warning | `#ffc107` | warning | Warning states, caution indicators |
| bs-primary | `#0d6efd` | info | Informational highlights |
| mw-primary-dark | `#0f1b33` | unknown | Palette color |
| bs-info | `#0dcaf0` | unknown | Palette color |
| bs-secondary-bg | `#3f3f46` | unknown | Palette color |
| bs-dark-border-subtle | `#adb5bd` | unknown | Palette color |
| bs-link-hover-color | `#8bb9fe` | unknown | Palette color |
| unknown | `#b45309` | unknown | Palette color |
| mw-secondary | `#6366f1` | unknown | Palette color |
| bs-secondary-border-subtle | `#c4c8cb` | unknown | Palette color |

### CSS Variable Tokens

```css
--mw-primary: #1B2A4A;
--mw-primary-light: #2C3E6B;
--mw-primary-dark: #0F1B33;
--mw-secondary: #6366F1;
--mw-secondary-light: #818CF8;
--mw-secondary-dark: #4F46E5;
--mw-accent: #F59E0B;
--mw-accent-light: #FBBF24;
--mw-accent-dark: #D97706;
--bs-primary: #0d6efd;
--bs-secondary: #6c757d;
--bs-primary-rgb: 13,110,253;
--bs-secondary-rgb: 108,117,125;
--bs-primary-text-emphasis: #052c65;
--bs-secondary-text-emphasis: #2b2f32;
--bs-primary-bg-subtle: #cfe2ff;
--bs-secondary-bg-subtle: #e2e3e5;
--bs-primary-border-subtle: #9ec5fe;
--bs-secondary-border-subtle: #c4c8cb;
--bs-success-border-subtle: #a3cfbb;
```


---

## 3. Typography Rules

**Font Stack:**
- **Inter** — Heading 1, Heading 2, Heading 3
- **Plus Jakarta Sans** — Body, Caption

**Font Sources:**

```css
@font-face {
  font-family: "Inter";
  src: url("https://fonts.gstatic.com/s/inter/v20/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuLyfMZg.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "Inter";
  src: url("https://fonts.gstatic.com/s/inter/v20/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuFuYMZg.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "Plus Jakarta Sans";
  src: url("https://fonts.gstatic.com/s/plusjakartasans/v12/LDIbaomQNQcsA88c7O9yZ4KMCoOg4IA6-91aHEjcWuA_TknNSg.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "bootstrap-icons";
  src: url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/fonts/bootstrap-icons.woff2?dd67030699838ea613ee6dbda90effa6");
  font-weight: 400;
}
```

| Role | Font | Size | Weight |
|---|---|---|---|
| Heading 1 | Inter | 5rem | 700 |
| Heading 2 | Inter | 4.5rem | 700 |
| Heading 3 | Inter | 4rem | 700 |
| Body | Plus Jakarta Sans | 1.25rem | 400 |
| Caption | Plus Jakarta Sans | .875rem | 400 |

**Typographic Rules:**
- Limit to 2 font families max per screen
- Use **Inter** for body/UI text, **Plus Jakarta Sans** for display/headings
- Maintain consistent hierarchy: no more than 3-4 font sizes per screen
- Headings use bold (600-700), body uses regular (400)
- Line height: 1.5 for body text, 1.2 for headings
- Use color and opacity for secondary hierarchy, not additional font sizes


---

## 4. Component Stylings

### Layout (1)

**Footer** — `html`

### Navigation (1)

**Navigation** — `html`

### Data Display (3)

**Card** — `html`
- Variants: `-facet`, `img`, `badges`, `actions`, `body`

**Badge** — `html`

**List** — `html`

### Data Input (2)

**Button** — `html`
- Variants: `icon`, `ghost`, `primary`, `sm`
- Animation: 

**Input** — `html`
- State: :focus, :placeholder

### Overlay (1)

**Modal** — `html`

### Media (1)

**Image** — `html`



---

## 5. Layout Principles

- **Base spacing unit:** 4px
- **Spacing scale:** 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24
- **Border radius:** .25rem, .25em, .375rem, 1rem, 2em, 3px, 6px, 8px, 10px, 14px, 16px, 999px, inherit
- **Max content width:** 1399.98px

**Spacing as Meaning:**
| Spacing | Use |
|---|---|
| 4-8px | Tight: related items within a group |
| 12-16px | Medium: between groups |
| 24-32px | Wide: between sections |
| 48px+ | Vast: major section breaks |


---

## 6. Depth & Elevation

### Flat — subtle depth hints

- `0 1px 2px rgba(15,23,42,0.03)`
- `0 1px 2px rgba(15,23,42,0.08)`
- `0 0 0 1px #fff,0 0 0 .25rem rgba(13,110,253,.25)`

### Raised — cards, buttons, interactive elements

- `var(--mw-shadow-md)`
- `var(--mw-shadow-sm)`
- `var(--mw-shadow-2xl)`

### Floating — dropdowns, popovers, modals

- `0 4px 12px -2px rgba(245,158,11,0.35)`
- `0 6px 14px -4px rgba(245,158,11,0.18)`

### Overlay — full-screen overlays, top-level dialogs

- `0 4px 24px -8px rgba(15,23,42,0.08)`
- `0 1px 2px rgba(15,23,42,0.03),0 12px 32px -16px rgba(15,23,42,0.08)`
- `0 1px 2px rgba(15,23,42,0.03),0 18px 40px -12px rgba(15,23,42,0.14)`

### Z-Index Scale

`0, 1, 2, 3, 4, 5, 20, 40, 1020, 1030, 1040`



---

## 7. Animation & Motion

This project uses **expressive motion**. Animations are an integral part of the experience.

### CSS Animations

- `@keyframes mw-float`
- `@keyframes progress-bar-stripes`
- `@keyframes spinner-border`
- `@keyframes spinner-grow`
- `@keyframes placeholder-glow`
- `@keyframes placeholder-wave`

### Animated Components

- **Button**: 

### Motion Guidelines

- Duration: 150-300ms for micro-interactions, 300-500ms for page transitions
- Easing: `ease-out` for enters, `ease-in` for exits
- Always respect `prefers-reduced-motion`


---

## 8. Do's and Don'ts

### Do's

- Use `#f59e0b` for interactive elements (buttons, links, focus rings)
- Use `#000000` as the primary page background
- Pair **Inter** (body) with **Plus Jakarta Sans** (display) — these are the only allowed fonts
- Follow the **4px** spacing grid for all margins, padding, and gaps
- Use the defined shadow tokens for elevation — see Section 6
- Use border-radius from the scale: .25rem, .25em, .375rem, 1rem, 2em
- Reuse existing components from Section 4 before creating new ones

### Don'ts

- Don't introduce colors outside this palette — extend the design tokens first
- Don't introduce additional font families beyond Inter and Plus Jakarta Sans
- Don't use arbitrary spacing values — stick to multiples of 4px
- Don't create custom box-shadow values outside the system tokens
- Don't use arbitrary border-radius values — pick from the defined scale
- Don't duplicate component patterns — check Section 4 first
- Don't use backdrop-blur or blur effects

### Anti-Patterns (detected from codebase)

- No blur or backdrop-blur effects
- No zebra striping on tables/lists


---

## 9. Responsive Behavior

| Name | Value | Source |
|---|---|---|
| sm | 575.98px | css |
| sm | 576px | css |
| sm | 640px | css |
| md | 767.98px | css |
| md | 768px | css |
| lg | 900px | css |
| lg | 991.98px | css |
| lg | 992px | css |
| xl | 1199.98px | css |
| xl | 1200px | css |
| 2xl | 1399.98px | css |
| 2xl | 1400px | css |

**Approach:** Use `@media (min-width: ...)` queries matching the breakpoints above.


---

## 10. Agent Prompt Guide

Use these as starting points when building new UI:

### Build a Card

```
Background: #ffffff
Border: 1px solid #52525b
Radius: 6px
Padding: 16px
Font: Inter
Use shadow tokens from Section 6.
```

### Build a Button

```
Primary: bg #f59e0b, text white
Ghost: bg transparent, border #52525b
Padding: 8px 16px
Radius: 6px
Hover: opacity 0.9 or lighter shade
Focus: ring with #f59e0b
```

### Build a Page Layout

```
Background: #000000
Max-width: 1399.98px, centered
Grid: 4px base
Responsive: mobile-first, breakpoints from Section 9
```

### Build a Stats Card

```
Surface: #ffffff
Label: #6b7280 (muted, 12px, uppercase)
Value: #e4e7ec (primary, 24-32px, bold)
Status: use success/warning/danger from Section 2
```

### Build a Form

```
Input bg: #000000
Input border: 1px solid #52525b
Focus: border-color #f59e0b
Label: #6b7280 12px
Spacing: 16px between fields
Radius: 6px
```

### General Component

```
1. Read DESIGN.md Sections 2-6 for tokens
2. Colors: only from palette
3. Font: Inter, type scale from Section 3
4. Spacing: 4px grid
5. Components: match patterns from Section 4
6. Elevation: shadow tokens
```
