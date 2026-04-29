# 127 DESIGN.md

> Auto-generated design system — reverse-engineered via static analysis by skillui.
> Frameworks: None detected
> Colors: 20 · Fonts: 2 · Components: 8
> Icon library: not detected · State: not detected
> Primary theme: dark · Dark mode toggle: no · Motion: expressive

---

## 1. Visual Theme & Atmosphere

This is a **dark-themed** interface with a warm tone. Depth is expressed through layered shadows and subtle surface color variation. Typography pairs **Inter** for display/headings with **Georgia** for body text, creating clear visual hierarchy through type contrast. Spacing follows a **4px base grid** (compact density), with scale: 2, 4, 6, 8, 10, 12, 14, 16px. The accent color **#f59e0b** anchors interactive elements (buttons, links, focus rings). Motion is expressive — spring physics, layout animations, and staggered reveals are part of the visual language.

---

## 2. Color Palette & Roles

| Token | Hex | Role | Use |
|---|---|---|---|
| bs-emphasis-color | `#000000` | background | Page background, darkest surface |
| lm-marquee-color | `#0f172a` | surface | Card and panel backgrounds |
| lm-video-play-ring | `#ffffff` | text-primary | Headings and body text |
| bs-secondary | `#6b7280` | text-muted | Captions, placeholders, secondary info |
| primary | `#2b2a28` | border | Dividers, card borders, outlines |
| mw-accent | `#f59e0b` | accent | CTAs, links, focus rings, active states |
| bs-warning | `#ffc107` | accent | CTAs, links, focus rings, active states |
| mw-accent-light | `#fbbf24` | accent | CTAs, links, focus rings, active states |
| bs-danger | `#dc3545` | danger | Error states, destructive actions |
| bs-success | `#198754` | success | Success states, positive indicators |
| on-primary | `#f7f4ec` | warning | Warning states, caution indicators |
| bs-primary | `#0d6efd` | info | Informational highlights |
| bs-secondary-bg-subtle | `#e4e7ec` | unknown | Palette color |
| unknown | `#6e5e52` | unknown | Palette color |
| bs-secondary-bg | `#3f3f46` | unknown | Palette color |
| bs-light-text-emphasis | `#52525b` | unknown | Palette color |
| bs-info | `#0dcaf0` | unknown | Palette color |
| unknown | `#0a0a0a` | unknown | Palette color |
| unknown | `#b24a3a` | unknown | Palette color |
| unknown | `#9a8d80` | unknown | Palette color |

### CSS Variable Tokens

```css
--primary: #2B2A28;
--secondary: #C8621A;
--accent: #8B5A2B;
--on-primary: #F7F4EC;
--on-primary-soft: var(--on-dark-2);
--lf-border: var(--rule);
--lf-border-hover: #94a3b8;
--lf-border-focus: var(--accent);
--on-accent: var(--on-dark);
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
```


---

## 3. Typography Rules

**Font Stack:**
- **Georgia** — Heading 1, Heading 2, Heading 3
- **Inter** — Body, Caption

**Font Sources:**

```css
@font-face {
  font-family: "Fraunces";
  src: url("fonts/Fraunces-Bold.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "Fraunces";
  src: url("fonts/Fraunces-Regular.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "Inter";
  src: url("fonts/Inter-Bold.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "Inter";
  src: url("fonts/Inter-Regular.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "Plus Jakarta Sans";
  src: url("fonts/PlusJakartaSans-Bold.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "Plus Jakarta Sans";
  src: url("fonts/PlusJakartaSans-Regular.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "bootstrap-icons";
  src: url("fonts/bootstrap-icons-Regular.woff2") format("woff2");
  font-weight: 400;
}
```

| Role | Font | Size | Weight |
|---|---|---|---|
| Heading 1 | Georgia | 5rem | 700 |
| Heading 2 | Georgia | 4.5rem | 700 |
| Heading 3 | Georgia | 4rem | 700 |
| Body | Inter | 11px | 400 |
| Caption | Inter | 12px | 400 |

**Typographic Rules:**
- Limit to 2 font families max per screen
- Use **Georgia** for body/UI text, **Inter** for display/headings
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

### Data Input (1)

**Button** — `html`
- Variants: `icon`, `ghost`
- Animation: 

### Overlay (1)

**Modal** — `html`

### Media (1)

**Image** — `html`



---

## 5. Layout Principles

- **Base spacing unit:** 4px
- **Spacing scale:** 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24
- **Border radius:** .25rem, .25em, .375rem, 1rem, 2em, 3px, 6px, 8px, 10px, 14px, 999px, inherit
- **Max content width:** 1100px

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

- `0 0 0 var(--lf-ring-size,3px) var(--lf-ring,rgba(156,42,42,0.12))`
- `0 0 0 var(--lf-ring-size,3px) var(--lf-ring,rgba(156,42,42,0.18))`
- `0 0 0 var(--lf-ring-size,3px) var(--lf-ring,rgba(156,42,42,0.30))`

### Floating — dropdowns, popovers, modals

- `0 4px 12px -2px rgba(245,158,11,0.35)`

### Overlay — full-screen overlays, top-level dialogs

- `0 0 0 1px var(--lm-video-play-ring),0 24px 60px -22px rgba(0,0,0,0.45)`
- `0 0 0 4px var(--lm-video-play-ring),0 28px 70px -22px rgba(0,0,0,0.55)`
- `0 14px 40px -16px rgba(0,0,0,0.25),0 4px 10px -6px rgba(0,0,0,0.18)`

### Z-Index Scale

`0, 1, 2, 3, 4, 5, 20, 30, 40, 50, 1020, 1030, 1040`



---

## 7. Animation & Motion

This project uses **expressive motion**. Animations are an integral part of the experience.

### CSS Animations

- `@keyframes lm-marquee`
- `@keyframes lm-logo-drift`
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
- Pair **Georgia** (body) with **Inter** (display) — these are the only allowed fonts
- Follow the **4px** spacing grid for all margins, padding, and gaps
- Use the defined shadow tokens for elevation — see Section 6
- Use border-radius from the scale: .25rem, .25em, .375rem, 1rem, 2em
- Reuse existing components from Section 4 before creating new ones

### Don'ts

- Don't introduce colors outside this palette — extend the design tokens first
- Don't introduce additional font families beyond Georgia and Inter
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
| xs | 480px | css |
| sm | 575.98px | css |
| sm | 576px | css |
| md | 720px | css |
| md | 767.98px | css |
| md | 768px | css |
| lg | 880px | css |
| lg | 900px | css |
| lg | 991.98px | css |
| lg | 992px | css |
| xl | 1100px | css |
| xl | 1199.98px | css |
| xl | 1200px | css |
| xl | 1280px | css |
| 2xl | 1399.98px | css |
| 2xl | 1400px | css |

**Approach:** Use `@media (min-width: ...)` queries matching the breakpoints above.


---

## 10. Agent Prompt Guide

Use these as starting points when building new UI:

### Build a Card

```
Background: #0f172a
Border: 1px solid #2b2a28
Radius: 6px
Padding: 16px
Font: Georgia
Use shadow tokens from Section 6.
```

### Build a Button

```
Primary: bg #f59e0b, text white
Ghost: bg transparent, border #2b2a28
Padding: 8px 16px
Radius: 6px
Hover: opacity 0.9 or lighter shade
Focus: ring with #f59e0b
```

### Build a Page Layout

```
Background: #000000
Max-width: 1100px, centered
Grid: 4px base
Responsive: mobile-first, breakpoints from Section 9
```

### Build a Stats Card

```
Surface: #0f172a
Label: #6b7280 (muted, 12px, uppercase)
Value: #ffffff (primary, 24-32px, bold)
Status: use success/warning/danger from Section 2
```

### Build a Form

```
Input bg: #000000
Input border: 1px solid #2b2a28
Focus: border-color #f59e0b
Label: #6b7280 12px
Spacing: 16px between fields
Radius: 6px
```

### General Component

```
1. Read DESIGN.md Sections 2-6 for tokens
2. Colors: only from palette
3. Font: Georgia, type scale from Section 3
4. Spacing: 4px grid
5. Components: match patterns from Section 4
6. Elevation: shadow tokens
```
