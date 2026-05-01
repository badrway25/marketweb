# Cornice · A.6 IT review-lock · Responsive auditor panel

```yaml
panel:    responsive-auditor
phase:    A.6 review-lock (IT-only)
date:     2026-05-01
score:    4.7 / 5
floor:    4.5
verdict:  PASS
viewports_walked: [1440, 1100, 880, 480]
```

## §1 · Viewport matrix (live walk · post-fix)

| Surface | 1440 | 1100 | 880 | 480 |
|---|---|---|---|---|
| Cream LF-2 nav | full split-wordmark + 5 links + filled rust CTA | full | wordmark + burger (links collapsed into drawer) | wordmark + burger |
| Hero photo | full-bleed with KPI overlay bottom-left | full-bleed; KPI still visible | full-bleed; KPI still visible | photo aspect compressed; KPI still readable |
| Hero h1 below photo (8/4 split) | h1 LEFT (8col) + side-quote RIGHT (4col) | 8/4 holds | h1 stacks above side-quote (1-col) | h1 stacks 1-col + ~32px floor |
| Narrative drop-cap | rust 84px | rust 64px (CSS rule) | rust 56px (CSS rule) | rust 48px (mobile fallback in `<= 480` query) |
| Narrative side-rail (sticky) | sticky on right | sticky on right | flows below body (no longer side-rail) | flows below body |
| Sectors-ribbon | 12 typologies on 2 lines (centered italic Cormorant) | flexes to 3 lines | flexes to 4 lines | flexes; readable |
| Leadership 2-col | photo LEFT + bio RIGHT | photo LEFT + bio RIGHT | stacks 1-col (photo top, bio bottom) | stacks 1-col |
| Magazine 3+1 grid | 3+1 layout · hero photo dominant (F3) | 1-col stacked · hero card first then 3 small | 1-col stacked | 1-col stacked |
| CTA closer cream | centered cream band with hairline borders | centered | centered | centered, button width respects mobile padding |
| Footer 4-col-with-whistleblowing | 4 columns | 4 columns | stacks to 2 columns | stacks to 1 column |

## §2 · Specific responsive verifications (post-fix)

### F3 magazine grid responsive (1100 boundary)

At 1100, the magazine grid stacks to 1 column. The hero card no
longer stretches to match a 3-card right column (because there is
no separate right column). The flex-grow rule on the hero photo
remains active but `min-height: 360px` keeps the photo visually
substantial without inflating row heights. The card foot baseline
behavior at 1440 is grid-row-driven; at 1100 each card is its own
row so the rule is moot. PASS.

### F2 cream nav responsive (880 burger boundary)

At 880, the LF-2 nav links collapse into a CSS-only burger
drawer (input checkbox + label sibling-selector). The cream
nav background is preserved; the burger lines are graphite (not
on-dark) per the F2 lift; focus ring on burger toggle reads rust.
Drawer slides into view; click-outside to dismiss is handled by
the cs-nav-toggle checkbox + label outside the drawer. Verified
live at 880 + 480. PASS.

### Hero overlay responsive (1440 → 480)

KPI tuple stays inside photo overlay at every viewport. At 480,
the photo is shorter (mobile aspect ratio) so the overlay band
sits closer to the photo's vertical middle, but the KPI cluster
is still readable + the credit caption above it still reads.
Tested live at 480 with 320×800 + 480×820 — KPI numerals still
readable at 32px or smaller. PASS.

### Hero h1 floor (480 small mobile)

H1 floors at 32px in the mobile media query (`@media (max-width:
480px)` block in lf2/styles.html). The voice anchor `Ogni progetto
è un argomento costruito, non un servizio reso.` wraps to 5-6
lines at 480 with `argomento` em still standing out. PASS.

### Side-rail mobile fallback

The narrative side-rail (4 anchor links) is `position: sticky` at
1440 + 1100. At 880 + 480 it flows below the body text as a
horizontal pill bar — verified live. PASS.

## §3 · Frozen-sibling responsive parity (anonymous)

Spot-checked at 1440 anonymous on the live URL during regression
walk:

- Pragma @ 1440 → 1100: 55/45 split holds, navy nav, emerald CTA — unchanged from A.5 baseline
- Fiscus @ 1440 → 1100: 55/45 split holds, dark gray nav — unchanged
- Solaria @ 1440 → 1100: 55/45 split holds, warm-carbon nav — unchanged
- Continua @ 1440 → 1100: object-overlay hero, pine nav, brass CTA — unchanged

No frozen sibling responsive regression.

## §4 · Layout-stability gates (no horizontal scroll, no content drop)

| Viewport | Horizontal scroll | Content drop | Verdict |
|---|---|---|---|
| 1440 | none | none | PASS |
| 1100 | none | none | PASS |
| 880 | none | none | PASS |
| 480 | none | none | PASS |

Verified via browser automation at every viewport. The
`overflow-x: clip` root guard from Phase X.4a step 1D inherited
from _base.html prevents accidental overflow if a future CSS
edit breaks a logical-property rule.

## Why score = 4.7 / 5

All declared LF-2 responsive behaviors render correctly across
the 4 walked viewports (1440 / 1100 / 880 / 480). F2 (cream nav)
and F3 (magazine grid) both verified at multiple breakpoints
with no regression. The 0.3 deduction covers two soft items:

- Did not walk 1280 or 720 explicitly at A.6 (only A.5 captured
  those mid-band widths). The walk shape was 4 viewports vs
  A.5's 5 viewports because A.6 prioritized post-fix verification
  density over breakpoint breadth.
- Side-rail mobile fallback to a horizontal pill bar works but
  the sticky behavior at 880 is borderline (just below the
  side-rail's 880px breakpoint). At 880 the side-rail flows
  below body — could revisit in a future polish if the user-
  handshake flags this scroll behavior.
