# Contrast & accessibility · Solaria Pass B multilingual

**Phase**: X.4 Pass B · `20260426T1500Z`
**Scope**: contrast / a11y for the multilingual rollout. Pass A
established the contrast baseline at archetype level; Pass B inherits.

## 1 · What Pass B can change vs not

Pass B added 4 locale content trees but did NOT touch CSS, did NOT
touch the archetype skin, did NOT change the palette, and did NOT
introduce new fonts (the Noto Kufi Arabic stack was already wired by
the corporate-suite RTL pilot).

Therefore the contrast properties verified in Pass A
(`solaria-passA-it/contrast-accessibility.md`) carry through unchanged
in EN/FR/ES, and only the AR locale needs separate verification —
because RTL flips the layout and the heading font swaps.

## 2 · Pass A contrast invariants (carry through)

These properties were measured and verified in Pass A and are inherited
by every Pass B locale:

| Surface | Color pair | Ratio | WCAG |
|---|---|---|---|
| Hero h1 (`color: var(--primary)`) | `#2B2A28` on `#F5F4F1` | ~13.4:1 | AAA |
| Body text on hero panel | `#2B2A28` on `#F5F4F1` | ~13.4:1 | AAA |
| Nav bar text | `#F5F4F1` on `#2B2A28` | ~13.4:1 | AAA |
| KPI band text | `#F5F4F1` on `#1B1A18` | ~16.1:1 | AAA |
| Italic em accent (`var(--accent)` in headline) | `#C8621A` on `#F5F4F1` | ~5.2:1 | AA |
| CTA dark band | `#F5F4F1` on `#2B2A28` | ~13.4:1 | AAA |
| Footer | `#F5F4F1` on `#1B1A18` | ~16.1:1 | AAA |

Pass B's content changes do not move any of these — same elements,
same color tokens, same backgrounds. Only the *strings* inside change.

## 3 · AR-specific contrast checks

The Arabic locale flips `<html dir="rtl">` and swaps the heading font
to `"Noto Kufi Arabic", Fraunces, Georgia, serif`. Two AR-only checks:

### CS-BLOCK-VI-03 (square-glyph regression)

Status: **PASS**. AR home h1 renders Arabic glyphs in Noto Kufi
Arabic (live `getComputedStyle(h1).fontFamily =
"Noto Kufi Arabic, Fraunces, Georgia, serif"`). No `□□□` fallback was
visible in any of the 4 AR captures (home + percorsi + contatti +
home-mobile-390). Glyph rendering is clean across the entire page.

### Visual contrast at AR-specific sizes

Noto Kufi Arabic at the same `font-size` as Fraunces produces a
slightly smaller x-height. Visual review of `05-ar-home-1440.png` and
`07-ar-contatti-1440.png` confirms the AR h1 still reads as the
load-bearing element — no readability collapse from the font swap.
Headline contrast is unchanged (`color: var(--primary)` → `#2B2A28`
on cream `#F5F4F1`).

## 4 · Per-locale focus-visible

The corporate-suite skin's focus-visible whitelist (added in X.4a step
1B for nav links, hero CTAs, and language-switcher pills) was
verified active across all 5 locales — pressing Tab cycles through
nav · primary CTA · secondary CTA · language pills with a visible
focus ring (`outline: 2px solid var(--accent)` at `outline-offset: 3px`).

Pass B did not touch the focus-visible CSS; the inherited behaviour
holds. The new AR pill (which Pass A did not have because the
switcher was hidden) participates correctly in the tab order.

## 5 · Form labels

The Solaria contact form (rendered on `/contatti/` per locale) carries
explicit `<label>` elements and `aria-required="true"` on required
fields — inherited from the archetype's `cs-form` partial. Pass B's
new locale content provides translated `label` strings; the markup
contract is unchanged. Spot-checked on AR (`/contatti/?lang=ar`):

```
الاسم · اللقب · البريد الإلكتروني · الهاتف · الشركة · الدور · الصيغة
المفضّلة · التوفّر · الهدف
```

All 9 form-field labels render in Arabic. Section headings
("التواصل · السياق · نطاق المكالمة · مرفقات") render in Arabic.
Submit button renders "احجز discovery call →" with the arrow direction
respecting RTL flow.

## 6 · A11y verdict

| Check | Status | Notes |
|---|---|---|
| Hero h1 contrast (all 5 locales) | PASS · AAA | inherited from archetype |
| KPI band contrast (all 5 locales) | PASS · AAA | inherited from archetype |
| Footer contrast (all 5 locales) | PASS · AAA | inherited from archetype |
| AR Noto Kufi font swap | PASS | computed fontFamily proof |
| AR no square-glyph regression (CS-BLOCK-VI-03) | PASS | visual + computed-style proof |
| Focus-visible across language pills | PASS | inherited X.4a step 1B |
| Form labels translated per locale | PASS | spot-checked AR |
| ARIA-required on required fields | PASS | inherited from archetype `cs-form` |

**ACCESSIBILITY: GREEN**. No new defects introduced by Pass B; all
inherited Pass-A contrast invariants hold across the 4 added locales.
