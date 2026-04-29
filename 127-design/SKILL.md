---
name: 127-design
description: Design system skill for 127. Activate when building UI components, pages, or any visual elements. Provides exact color tokens, typography scale, spacing grid, component patterns, and craft rules. Read references/DESIGN.md before writing any CSS or JSX.
---

# 127 Design System

You are building UI for **127**. Dark-themed, warm palette, sans-serif typography (Inter), compact density on a 4px grid, expressive motion.

## Design Philosophy

- **Layered depth** — use shadow tokens to create a sense of physical layering. Each elevation level has a specific shadow.
- **Gradient accents** — gradients are used thoughtfully for emphasis, not decoration.
- **Type pairing** — Inter for body/UI text, Plus Jakarta Sans for headings/display. Never introduce a third typeface.
- **compact density** — 4px base grid. Every dimension is a multiple of 4.
- **warm palette** — the color temperature runs warm, matching the sans-serif typography.
- **Restrained accent** — `#f59e0b` is the only pop of color. Used exclusively for CTAs, links, focus rings, and active states.
- **Expressive motion** — animations are an integral part of the experience. Use spring physics and layout animations.

## Color System

### Core Palette

| Role | Token | Hex | Use |
|------|-------|-----|-----|
| Background | `--background` | `#000000` | Page/app background |
| Surface | `--surface` | `#ffffff` | Cards, panels, modals |
| Text Primary | `--text-primary` | `#e4e7ec` | Headings, body text |
| Text Muted | `--text-muted` | `#6b7280` | Captions, placeholders |
| Accent | `--accent` | `#f59e0b` | CTAs, links, focus rings |
| Border | `--border` | `#52525b` | Dividers, card borders |

### Status Colors

| Status | Hex | Use |
|--------|-----|-----|
| Success | `#198754` | Confirmations, positive trends |
| Warning | `#ffc107` | Caution states, pending items |
| Danger | `#dc3545` | Errors, destructive actions |

### Extended Palette

- **bs-primary:** `#0d6efd`
- **mw-primary-dark:** `#0f1b33`
- **bs-info:** `#0dcaf0`
- **bs-secondary-bg:** `#3f3f46` — Secondary text, placeholder text
- **bs-dark-border-subtle:** `#adb5bd` — Secondary text, placeholder text
- **bs-link-hover-color:** `#8bb9fe`
- `#b45309`
- **mw-secondary:** `#6366f1` — Secondary text, placeholder text

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

## Typography

### Font Stack

- **Inter** — Heading 1, Heading 2, Heading 3
- **Plus Jakarta Sans** — Body, Caption

### Font Sources

```css
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

### Type Scale

| Role | Family | Size | Weight |
|------|--------|------|--------|
| Heading 1 | Inter | 5rem | 700 |
| Heading 2 | Inter | 4.5rem | 700 |
| Heading 3 | Inter | 4rem | 700 |
| Body | Plus Jakarta Sans | 1.25rem | 400 |
| Caption | Plus Jakarta Sans | .875rem | 400 |

### Typography Rules

- Body/UI: **Inter**, Headings: **Plus Jakarta Sans** — these are the only display fonts
- Max 3-4 font sizes per screen
- Headings: weight 600-700, body: weight 400
- Use color and opacity for text hierarchy, not additional font sizes
- Line height: 1.5 for body, 1.2 for headings

## Spacing & Layout

### Base Grid: 4px

Every dimension (margin, padding, gap, width, height) must be a multiple of **4px**.

### Spacing Scale

`2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24` px

### Spacing as Meaning

| Spacing | Use |
|---------|-----|
| 4-8px | Tight: related items (icon + label, avatar + name) |
| 12-16px | Medium: between groups within a section |
| 24-32px | Wide: between distinct sections |
| 48px+ | Vast: major page section breaks |

### Border Radius

Scale: `.25rem, .25em, .375rem, 1rem, 2em, 3px, 6px, 8px, 10px, 14px, 16px, 999px, inherit`
Default: `6px`

### Container

Max-width: `1399.98px`, centered with auto margins.

### Breakpoints

| Name | Value |
|------|-------|
| sm | 575.98px |
| sm | 576px |
| sm | 640px |
| md | 767.98px |
| md | 768px |
| lg | 900px |
| lg | 991.98px |
| lg | 992px |
| xl | 1199.98px |
| xl | 1200px |
| 2xl | 1399.98px |
| 2xl | 1400px |

Mobile-first: design for small screens, layer on responsive overrides.

## Component Patterns

### Card

```css
.card {
  background: #ffffff;
  border: 1px solid #52525b;
  border-radius: 6px;
  padding: 16px;
  box-shadow: var(--mw-shadow-md);
}
```

```html
<div class="card">
  <h3>Card Title</h3>
  <p>Card content goes here.</p>
</div>
```

### Button

```css
/* Primary */
.btn-primary {
  background: #f59e0b;
  color: #e4e7ec;
  border-radius: 6px;
  padding: 8px 16px;
  font-weight: 500;
  transition: opacity 150ms ease;
}
.btn-primary:hover { opacity: 0.9; }

/* Ghost */
.btn-ghost {
  background: transparent;
  border: 1px solid #52525b;
  color: #e4e7ec;
  border-radius: 6px;
  padding: 8px 16px;
}
```

```html
<button class="btn-primary">Get Started</button>
<button class="btn-ghost">Learn More</button>
```

### Input

```css
.input {
  background: #000000;
  border: 1px solid #52525b;
  border-radius: 6px;
  padding: 8px 12px;
  color: #e4e7ec;
  font-size: 14px;
}
.input:focus { border-color: #f59e0b; outline: none; }
```

```html
<input class="input" type="text" placeholder="Search..." />
```

### Badge / Chip

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 4px 8px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 500;
  background: #ffffff;
  color: #6b7280;
}
```

```html
<span class="badge">New</span>
<span class="badge">Beta</span>
```

### Modal / Dialog

```css
.modal-backdrop { background: rgba(0, 0, 0, 0.6); }
.modal {
  background: #ffffff;
  border: 1px solid #52525b;
  border-radius: inherit;
  padding: 24px;
  max-width: 480px;
  width: 90vw;
  box-shadow: 0 4px 12px -2px rgba(245,158,11,0.35);
}
```

```html
<div class="modal-backdrop">
  <div class="modal">
    <h2>Dialog Title</h2>
    <p>Dialog content.</p>
    <button class="btn-primary">Confirm</button>
    <button class="btn-ghost">Cancel</button>
  </div>
</div>
```

### Table

```css
.table { width: 100%; border-collapse: collapse; }
.table th {
  text-align: left;
  padding: 8px 12px;
  font-weight: 500;
  font-size: 12px;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-bottom: 1px solid #52525b;
}
.table td {
  padding: 12px;
  border-bottom: 1px solid #52525b;
}
```

```html
<table class="table">
  <thead><tr><th>Name</th><th>Status</th><th>Date</th></tr></thead>
  <tbody>
    <tr><td>Item One</td><td>Active</td><td>Jan 1</td></tr>
    <tr><td>Item Two</td><td>Pending</td><td>Jan 2</td></tr>
  </tbody>
</table>
```

### Navigation

```css
.nav {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  border-bottom: 1px solid #52525b;
}
.nav-link {
  color: #6b7280;
  padding: 8px 12px;
  border-radius: 6px;
  transition: color 150ms;
}
.nav-link:hover { color: #e4e7ec; }
.nav-link.active { color: #f59e0b; }
```

```html
<nav class="nav">
  <a href="/" class="nav-link active">Home</a>
  <a href="/about" class="nav-link">About</a>
  <a href="/pricing" class="nav-link">Pricing</a>
  <button class="btn-primary" style="margin-left: auto">Get Started</button>
</nav>
```

### Extracted Components

These components were found in the codebase:

**Button** (`html`)
- Variants: `icon`, `ghost`, `primary`, `sm`

**Card** (`html`)
- Variants: `-facet`, `img`, `badges`, `actions`, `body`

**Navigation** (`html`)

**Badge** (`html`)

## Page Structure

The following page sections were detected:

- **Navigation** — Top navigation bar (10 items)
- **Hero** — Hero/banner section with headline and CTAs
- **Features** — Feature/benefit cards grid (86 items)
- **Footer** — Page footer with links and info (27 items)
- **Cta** — Call-to-action section

When building pages, follow this section order and structure.

## Animation & Motion

This project uses **expressive motion**. Animations are part of the design language.

### CSS Animations

- `mw-float`
- `progress-bar-stripes`
- `spinner-border`
- `spinner-grow`
- `placeholder-glow`

### Motion Tokens

- **Duration scale:** `0ms`, `100ms`, `120ms`, `140ms`, `150ms`, `160ms`, `180ms`, `200ms`, `300ms`, `350ms`, `600ms`
- **Easing functions:** `ease`, `ease-in-out`, `linear`, `ease-out`
- **Animated properties:** `color`

### Motion Guidelines

- **Duration:** Use values from the duration scale above. Short (0ms) for micro-interactions, long (600ms) for page transitions
- **Easing:** Use `ease` as the default easing curve
- **Direction:** Elements enter from bottom/right, exit to top/left
- **Reduced motion:** Always respect `prefers-reduced-motion` — disable animations when set

## Depth & Elevation

### Shadow Tokens

- Subtle: `0 1px 2px rgba(15,23,42,0.03)`
- Subtle: `0 1px 2px rgba(15,23,42,0.08)`
- Subtle: `0 0 0 1px #fff,0 0 0 .25rem rgba(13,110,253,.25)`
- Raised (cards, buttons): `var(--mw-shadow-md)`
- Raised (cards, buttons): `var(--mw-shadow-sm)`
- Raised (cards, buttons): `var(--mw-shadow-2xl)`

### Z-Index Scale

`0, 1, 2, 3, 4, 5, 20, 40, 1020, 1030, 1040`

Use these exact values — never invent z-index values.

## Anti-Patterns (Never Do)

- **No blur effects** — no backdrop-blur, no filter: blur()
- **No zebra striping** — tables and lists use borders for separation
- **No invented colors** — every hex value must come from the palette above
- **No arbitrary spacing** — every dimension is a multiple of 4px
- **No extra fonts** — only Inter and Plus Jakarta Sans are allowed
- **No arbitrary border-radius** — use the scale: .25rem, .25em, .375rem, 1rem, 2em, 3px, 6px, 8px, 10px, 14px
- **No opacity for disabled states** — use muted colors instead

## Workflow

1. **Read** `references/DESIGN.md` before writing any UI code
2. **Pick colors** from the Color System section — never invent new ones
3. **Set typography** — Inter, Plus Jakarta Sans only, using the type scale
4. **Build layout** on the 4px grid — check every margin, padding, gap
5. **Match components** to patterns above before creating new ones
6. **Apply elevation** — use shadow tokens
7. **Validate** — every value traces back to a design token. No magic numbers.

## Brand Spec

- **Favicon:** `/favicon.ico`
- **Site URL:** `http://127.0.0.1:8731/`
- **Brand color:** `#f59e0b`
- **Brand typeface:** Inter

## Quick Reference

```
Background:     #000000
Surface:        #ffffff
Text:           #e4e7ec / #6b7280
Accent:         #f59e0b
Border:         #52525b
Font:           Inter
Spacing:        4px grid
Radius:         6px
Components:     9 detected
```

## When to Trigger

Activate this skill when:
- Creating new components, pages, or visual elements for 127
- Writing CSS, Tailwind classes, styled-components, or inline styles
- Building page layouts, templates, or responsive designs
- Reviewing UI code for design consistency
- The user mentions "127" design, style, UI, or theme
- Generating mockups, wireframes, or visual prototypes

---

# Full Reference Files

> Every output file is embedded below. Claude has full design system context from /skills alone.

## Design System Tokens (DESIGN.md)

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

## Bundled Fonts (fonts/)

The following font files are bundled in the `fonts/` directory:

- `fonts/bootstrap-icons-Regular.woff`
- `fonts/bootstrap-icons-Regular.woff2`
- `fonts/Inter-Black.ttf`
- `fonts/Inter-Bold.ttf`
- `fonts/Inter-ExtraBold.ttf`
- `fonts/Inter-ExtraLight.ttf`
- `fonts/Inter-Light.ttf`
- `fonts/Inter-Medium.ttf`
- `fonts/Inter-Regular.ttf`
- `fonts/Inter-SemiBold.ttf`
- `fonts/Inter-Thin.ttf`
- `fonts/PlusJakartaSans-Bold.ttf`
- `fonts/PlusJakartaSans-ExtraBold.ttf`
- `fonts/PlusJakartaSans-ExtraLight.ttf`
- `fonts/PlusJakartaSans-Light.ttf`
- `fonts/PlusJakartaSans-Medium.ttf`
- `fonts/PlusJakartaSans-Regular.ttf`
- `fonts/PlusJakartaSans-SemiBold.ttf`

Use these local font files in `@font-face` declarations instead of fetching from Google Fonts.

