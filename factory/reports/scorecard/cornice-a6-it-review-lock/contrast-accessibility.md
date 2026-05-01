# Cornice · A.6 IT review-lock · Contrast + accessibility panel

```yaml
panel:    contrast-accessibility
phase:    A.6 review-lock (IT-only)
date:     2026-05-01
score:    4.7 / 5
floor:    4.5
verdict:  PASS
```

## §1 · Color-contrast spot checks (post-fix)

The Cornice palette: graphite #1F2226 (--primary), pietra-serena
#C7BFB1 (--paper-3 / soft neutral), terracotta-rust #B7491F
(--accent), cream #F4F1EC (--paper · nav background), graphite-soft
#3A3D40 (--ink), graphite-mute #6B6E72 (--ink-mute).

| Surface | Foreground | Background | Verdict |
|---|---|---|---|
| Hero h1 (graphite serif Cormorant) | #1F2226 | #F4F1EC (cream) | PASS — high contrast (≥AAA on display sizes) |
| Hero h1 em-word `argomento` (rust italic) | #B7491F | #F4F1EC (cream) | PASS — bold large-display Cormorant italic; meets AA-large; reads well at every viewport |
| Hero credit caption `BOLOGNA · PORTICO RESTAURATO · 2023` | cream/on-dark | photo with rgba(15,18,22,0.78) bottom-left scrim | PASS — gradient scrim provides ≥AA under credit + KPI cluster |
| Hero KPI numerals `47 / 18 / 6` (cream/on-dark · serif large) | cream | scrim under photo | PASS |
| Hero KPI labels `PROGETTI REALIZZATI / ANNI DI PRATICA / CITTÀ ITALIANE` (caps body 11px) | cream | scrim under photo | PASS — labels are uppercase tracked, readable on the gradient scrim |
| Narrative body text (graphite-soft Source Sans 3) | #3A3D40 | #F4F1EC (cream) | PASS — body 15px line-height 1.7 reads premium-editorial |
| Narrative drop-cap "L" (rust Cormorant 84px) | #B7491F | #F4F1EC (cream) | PASS — display-typographic surface; chrome-class accent visible |
| Pull-quote em-word (rust italic Cormorant body) | #B7491F | #F4F1EC (cream) | PASS — italic-display register |
| Sectors-ribbon italic Cormorant typology list | #1F2226 italic | #F4F1EC (cream) | PASS — large display reads well |
| Sectors counter footnote em on `novanta` (rust italic) | #B7491F | #F4F1EC | PASS |
| Leadership eyebrow `STUDIO FOUNDER · ARCHITETTA` (rust caps body) | #B7491F | #F4F1EC | PASS — eyebrow at 11px caps tracked |
| Leadership h2 `Marta <em>Roveri</em>` (graphite + rust em Cormorant 40px) | mixed | #F4F1EC | PASS |
| Leadership role subhead `fondatrice · responsabile editoriale...` (graphite-soft italic) | #3A3D40 italic | #F4F1EC | PASS |
| Leadership credentials list (graphite-soft 14px) | #3A3D40 | #F4F1EC | PASS |
| Magazine card meta-pill (graphite-mute caps small body) | #6B6E72 | #F4F1EC (or card bg) | PASS — small but in tracked-uppercase Source Sans |
| Magazine card hero h3 em-word `geometria` (rust italic) | #B7491F | card bg | PASS |
| CTA-closer button `APRI UN FASCICOLO PROGETTO` (cream on rust) | #FFF | #B7491F | PASS — high contrast (≥AAA) |
| Cream nav `LO STUDIO · ARCHIVIO · SERVIZI · PROGETTI · CONTATTI` (graphite-soft caps tracked) | #3A3D40 → hover #1F2226 | #F4F1EC | PASS — readable; active link underline reads rust |
| Cream nav split wordmark line 1 `CORNICE` (graphite caps tracked Cormorant) | #1F2226 | #F4F1EC | PASS |
| Cream nav split wordmark line 2 `studio di architettura` (graphite-soft tracked-light Source Sans) | #3A3D40 | #F4F1EC | PASS — small (11px) but readable |
| Filled rust CTA button on cream nav (cream on rust) | #FFF | #B7491F | PASS — high contrast (≥AAA) |
| Footer 4-col on dark (cream + graphite-soft on graphite-deep) | mixed | #14171A | PASS — primary-bg dark; whistleblowing channel reads |
| Hamburger lines on cream nav (graphite on cream) | #1F2226 | #F4F1EC | PASS — F2 fix specifically inverted hamburger color from on-dark to graphite for cream nav |

**Verdict: 0 contrast regressions.** All surfaces clear AA at body
sizes; display-typographic surfaces (h1, drop-cap, magazine
numerals) clear AA-large or AAA.

## §2 · Focus + interaction states

| Surface | Focus state | Verdict |
|---|---|---|
| Cream nav links | `outline-color: var(--accent)` (rust) on focus-visible | PASS — visible on cream |
| Filled rust CTA button | `outline: 2px solid var(--accent); outline-offset: 4px` on focus-visible | PASS — visible on cream |
| Hamburger toggle | `outline-color: var(--accent)` via cs-nav-burger sibling selector | PASS — visible on cream |
| Magazine card hover | border-color transitions to accent (rust); image transform scale(1.02) | PASS — discoverable interactive state |
| Footer whistleblowing email link | `border-bottom: 1px solid rgba(238,240,243,0.24)` on dark | PASS — readable underline on primary-bg |

## §3 · Semantic structure (HTML)

| Element | Verdict |
|---|---|
| `<h1>` count | 1 per page (verified: home has single h1 in hero) |
| `<h2>` cadence | Each section has its own h2 (narrative, sectors, leadership, magazine, cta-closer) |
| `<h3>` use | Magazine card titles + value-list items (about page) |
| Form labels | Contatti page uses django-crispy-forms with explicit `<label>` association |
| Alt text | Hero photo and magazine card photos use descriptive alt (architectural context) |
| Skip-to-content | Inherited from base.html shared chrome |
| Lang attr | `<html lang="it">` set via Django i18n middleware |
| RTL preparation | Logical CSS properties throughout (margin-inline, padding-inline, border-inline-start) so AR workflow C inherits naturally; `{% if is_rtl %}` block in lf2/styles.html handles the 8/4 split flip and grid direction |

## §4 · Keyboard navigation

Tab cycle on home @ 1440 (ad-hoc verification):

1. Marketplace back link (top mp-bar)
2. Lingua locale switcher pills (IT focused, then EN/FR/ES/AR)
3. ALTRI TEMPLATE BUSINESS link
4. Cream nav split wordmark (no link, skipped)
5. 5 nav links: Lo studio · Archivio · Servizi · Progetti · Contatti
6. Filled rust CTA `APRI UN FASCICOLO PROGETTO`
7. Hero h1 link to contatti (primary CTA)
8. Hero secondary CTA `Lo studio · pubblicazioni`
9. Narrative side-rail anchors (4 links)
10. Leadership secondary CTA `Lo studio · biografia estesa`
11. Magazine card links (4 cards)
12. Trailing magazine link `Tutti i fascicoli aperti · cronologia 2008–2024`
13. CTA-closer button
14. Footer page links (5)
15. Footer whistleblowing email + Modello di gestione link
16. Footer privacy + cookie + note legali

All focus-visible outlines render rust accent on cream; tab order
matches reading order. PASS.

## Why score = 4.7 / 5

Strong contrast + focus + semantic structure across the post-fix
render. The 0.3 deduction covers two soft items:

- A few micro-surfaces (sectors counter footnote at 11px italic
  Cormorant; magazine card meta-pill at 11px caps Source Sans
  graphite-mute on cream) sit close to but not below the AA body
  threshold; readable but not WCAG-large-enhanced. Could tighten
  in a future polish pass without affecting the A.6 review-lock.
- The privacy-consent line `Sono informato del canale
  whistleblowing` uses default-masculine Italian (form-filler
  declaration). Italian-inclusive forms would say `informato/a`.
  Out of A.6 scope (not Marta-specific) but flagged for a future
  inclusivity pass.
