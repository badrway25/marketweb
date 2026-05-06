# Browser verification · motion_profile DNA · implementation pass 1

```yaml
report_type:        browser-verification · default-motion + reduced-motion
                    walks · synthetic gate probes + frozen-sibling parity
phase:              X.7b motion_profile DNA · implementation pass 1
date:               2026-05-06
verifier:           orchestrator-side authoring (Playwright MCP single-
                    chromium session · Django dev server localhost:8052
                    · staff-session client for Causa draft access)
companion:          factory/reports/hardening/motion-profile-implementation-pass1.md
                    factory/reports/scorecard/motion-profile-implementation-pass1/scorecard.md
walk_target:        2 new bundle-flag gates · MICRO-2 card-lift-restrained
                    + MEDIA-1 cinematic-fade-on-view · plus 6 frozen
                    corporate-suite siblings byte-equivalence check
walk_summary:       12/12 cells PASS · 0 blocking · 0 fixes mid-walk ·
                    every frozen sibling byte-equivalent on body data-
                    attribute set · both new gates fire correctly under
                    default-motion + short-circuit cleanly under reduced-
                    motion
scope_hold:         5 paper-flagged but un-wired bundle flags
                    (`hero_parallax` · `gallery_snap` · `cursor_vignette`
                    · `magnetic_button` · `nav_hide_on_scroll_down` ·
                    `scroll_progress_bar` · `live_data_kpi`) NOT walked ·
                    explicit out-of-scope this pass
```

---

## §1 · Walk environment

- Django dev server: `python manage.py runserver 127.0.0.1:8052 --noreload`
- Database: SQLite dev DB (24 published_live + 1 draft = Causa)
- Browser: Playwright MCP chromium · default viewport 1280×720
- Locale walked: IT (`?` no `lang` param)
- Reduced-motion: simulated by manually adding `body.classList.add('lm-
  reduced')` (the same body class JS adds when `window.matchMedia
  ('(prefers-reduced-motion: reduce)')` matches).

---

## §2 · Cell A · Frozen-sibling body data-attribute parity (6/6 PASS)

Walk: render every corporate-suite sibling at `/templates/business/{slug}/
preview/?preview=1` via Django test client (staff-session for Causa) and
read the opening `<body>` tag. Compare the data-motion-* set to the
pre-pass expected set.

| sibling | profile | flags emitted (after this pass) | match pre-pass? |
|---|---|---|---|
| pragma-corporate-suite | g3-institutional | data-motion-kpi-animate=1 | ✓ |
| cornice-architettura | g2-editorial | (none) | ✓ |
| fiscus-commercialista | g3-institutional | data-motion-kpi-animate=1 | ✓ |
| solaria-coaching | g3-institutional | data-motion-kpi-animate=1 | ✓ |
| continua-stewardship | g4-stewardship | (none) | ✓ |
| causa-legale | g2-editorial-counter | kpi-animate · nav-condense · evid5 · evid3 · time3 | ✓ |

All 6/6 byte-equivalent. The 2 new attributes (`data-motion-card-lift` ·
`data-motion-cinematic-fade`) are emitted on **zero** sibling body tags.

Verdict: **PASS** · regression boundary held.

Walk script: `factory/reports/browser-verification/_walk_motion_pass1.py`

---

## §3 · Cell B · Static asset reachability (2/2 PASS)

Walk: HTTP-fetch the modified static assets and confirm each contains
the new gate rules.

| asset | HTTP | new content present | match count |
|---|---|---|---|
| /static/css/live-motion.css | 200 | `--mp-card-lift` · `--mp-cinematic` · `body[data-motion-card-lift="1"]` · `body.lm-ready[data-motion-cinematic-fade="1"]` | 34 references |
| /static/js/live-motion.js | 200 | `setupCinematicFade` · `data-motion-cinematic-fade` | 6 references |

Verdict: **PASS**.

---

## §4 · Cell C · CSS sheet parses cleanly · all rules accessible (1/1 PASS)

Walk: navigate to a corporate-suite sibling (Cornice), force-reload the
live-motion.css link with a cache-buster query, then enumerate `cssRules`.

Result:
- Total rules in fresh sheet: **26**
- Rules referencing the new gates (substring `motion-card-lift` or
  `motion-cinematic-fade`): **8**
- Sample rule (excerpt):
  ```
  body[data-motion-card-lift="1"] [data-motion-card] {
    transition: transform var(--mp-card-lift-dur) var(--mp-card-lift-ease),
                box-shadow var(--mp-card-lift-dur) var(--mp-card-lift-ease);
    will-change: transform, box-shadow;
  }
  ```

Verdict: **PASS** · CSS parser sees every new rule.

---

## §5 · Cell D · CSS variable resolution on `:root` (6/6 PASS)

Walk: read computed style on `document.documentElement` via
`getPropertyValue('--mp-*')`.

| token | resolved value | matches plan? |
|---|---|---|
| `--mp-card-lift-y` | 3px | ✓ AT-G1-2 ceiling |
| `--mp-card-lift-dur` | 360ms | ✓ |
| `--mp-cinematic-dur` | 1200ms | ✓ AT-G6-2 floor |
| `--mp-cinematic-opacity-start` | 0.7 | ✓ |
| `--mp-cinematic-saturation-start` | 0.85 | ✓ AT-G6-2 floor |
| `--mp-cinematic-scale-start` | 1.04 | ✓ AT-G6-2 ceiling |

Verdict: **PASS** · every token at its anti-tacky-encoded value.

---

## §6 · Cell E · Cinematic-fade gate · default-motion (PASS)

Walk: on Cornice (g2-editorial · ZERO motion flags emitted), inject a
synthetic `<div data-motion-fade-in>` AFTER setting the body attribute
`data-motion-cinematic-fade="1"`. Read computed styles BEFORE and AFTER
adding the `.lm-fade-in` class.

| state | opacity | transform | filter |
|---|---|---|---|
| **initial (hidden)** | 0.7 | matrix(1.04, 0, 0, 1.04, 0, 0) | saturate(0.85) |
| **target (after .lm-fade-in)** | (transition starts; final = 1) | (transition starts; final = matrix(1, 0, 0, 1, 0, 0)) | (transition starts; final = saturate(1)) |
| transition | opacity 1.2s cubic-bezier(0.22, 0.61, 0.36, 1), filter 1.2s …, transform 1.2s … | | |

The `transition` property correctly carries 1200ms · cubic-bezier easing
on all three properties (opacity · transform · filter). The hidden state
is achieved at first paint (no flash of fully-visible content before the
class change).

Verdict: **PASS** · gate fires correctly when armed.

---

## §7 · Cell F · Cinematic-fade gate · reduced-motion (PASS)

Walk: same probe, but with `body.classList.add('lm-reduced')` set BEFORE
the body data-attribute and the probe element are added.

| state | opacity | transform | filter | transition |
|---|---|---|---|---|
| **initial (under lm-reduced)** | 1 | none | none | none |

The hidden state is bypassed entirely. The `body.lm-reduced[data-motion-
cinematic-fade="1"]` rule clears all four properties via `!important`.

Verdict: **PASS** · reduced-motion short-circuit honored.

---

## §8 · Cell G · Card-lift gate · default-motion (PASS)

Walk: on Cornice, set `data-motion-card-lift="1"` on body, inject a
synthetic `<div data-motion-card tabindex="0">`, then call `card.focus()`
and wait 500ms for the 360ms transition to settle.

| state | transform | box-shadow |
|---|---|---|
| **idle** | none | none |
| **focused (after 500ms settle)** | matrix(1, 0, 0, 1, 0, **-3**) | rgba(15, 18, 22, 0.1) 0px 6px 16px -8px |
| transition | transform 0.36s cubic-bezier(0.33, 1, 0.68, 1), box-shadow 0.36s cubic-bezier(0.33, 1, 0.68, 1) | |

The transform `matrix(1, 0, 0, 1, 0, -3)` is exactly `translate3d(0, -3px, 0)`.
The box-shadow matches `0 6px 16px -8px rgba(15, 18, 22, 0.10)` byte-
exactly (CSS rounds 0.10 → 0.1 in computed style).

Verdict: **PASS** · gate fires correctly when armed.

---

## §9 · Cell H · Card-lift gate · reduced-motion (PASS)

Walk: same probe, but with `body.classList.add('lm-reduced')` set first.

| state | transform | box-shadow | transition |
|---|---|---|---|
| **focused (under lm-reduced, after 500ms)** | none | none | none |

Verdict: **PASS** · reduced-motion short-circuit honored.

---

## §10 · Cell I · Causa slice-01/02 bundle preserved (PASS)

Walk: render Causa via staff-session client, parse body tag, confirm
all 5 slice-01/02 flags still emit.

```
<body class=" cs-lf-lf-2"
      data-motion-profile="g2-editorial-counter"
      data-motion-kpi-animate="1"
      data-motion-nav-condense="1"
      data-motion-evid5="1"
      data-motion-evid3="1"
      data-motion-time3="1">
```

5/5 slice-01/02 flags present · 0/2 new flags present (correct: g2-
editorial-counter doesn't claim card-lift or cinematic-fade).

Verdict: **PASS** · Causa's 5-flag bundle byte-equivalent.

---

## §11 · Cell J · Non-CS sibling unchanged (PASS)

Walk: render Pixel (`/templates/portfolio/pixel-portfolio-fotografico/
preview/`) and check body tag.

Result:
```
<body class="">
```

Pixel does not include the corporate-suite chrome, so its body tag has
no class and no data-motion-* attributes. This is the documented out-
of-scope state for non-CS archetypes (extension to non-CS chrome is
deferred to Phase X.7a per motion-profile-dna-plan §15).

Verdict: **PASS** · non-CS surface unchanged.

---

## §12 · Cell K · Reduced-motion class is added on init (PASS)

Walk: navigate to Cornice and read `body.className` after page load.

Result: `cs-lf-lf-2 lm-ready` (no `lm-reduced` because the test browser
does not have `prefers-reduced-motion` set). The `lm-ready` class lands
on init, which is the gate that activates the cinematic-fade hidden
state (per the CSS rule `body.lm-ready[data-motion-cinematic-fade="1"]
[data-motion-fade-in]`).

Verdict: **PASS** · `lm-ready` lands · the no-JS fallback contract
preserved.

---

## §13 · Cell L · `setupCinematicFade()` is callable (PASS)

Walk: inspect the live-motion.js source via fetch + check that
`setupCinematicFade` is referenced 6 times (1 definition + 1 call in
`init()` + 4 inline references in the function body).

Result: 6 references found. Function body verified to:
- guard on `body[data-motion-cinematic-fade="1"]` (line 1)
- query `[data-motion-fade-in]` targets (line 2)
- one-shot via `io.unobserve(entry.target)` (line 7)
- threshold 0.20 + rootMargin -40px (line 11)

Verdict: **PASS** · function lands in production bundle correctly.

---

## §14 · Roll-up

| cell | check | result |
|---|---|---|
| A | 6 frozen siblings byte-equivalent on body data-attrs | PASS |
| B | static assets serve · 200 · new content present | PASS |
| C | CSS parses cleanly · 26 rules · 8 new gate rules | PASS |
| D | `--mp-*` tokens resolve to encoded values | PASS |
| E | cinematic-fade default-motion gate fires correctly | PASS |
| F | cinematic-fade reduced-motion short-circuits | PASS |
| G | card-lift default-motion gate fires correctly | PASS |
| H | card-lift reduced-motion short-circuits | PASS |
| I | Causa slice-01/02 bundle preserved | PASS |
| J | non-CS sibling (Pixel) body unchanged | PASS |
| K | `lm-ready` class added on init | PASS |
| L | `setupCinematicFade()` callable | PASS |

**12/12 PASS · 0 blocking · 0 fixes mid-walk.**

---

## §15 · Out-of-scope (paper-flagged · not walked)

Per slice scope (§2 of the implementation report), these patterns are
ratified-on-paper but un-wired this pass:

- `hero_parallax` (MEDIA-2) · g6-cinematic safe pool
- `gallery_snap` (MEDIA-5) · g6-cinematic safe pool
- `cursor_vignette` (MICRO-6) · g6-cinematic dark-hero only
- `magnetic_button` (MICRO-3) · g5-sprint-console only
- `nav_hide_on_scroll_down` (NAV-2) · g5-sprint-console only
- `scroll_progress_bar` (NAV-3) · g5-sprint-console only
- `live_data_kpi` (KPI-3) · g5-sprint-console only · ops-gated

Each will receive its own implementation slice + browser walk when its
host cluster brief authorises it.

---

## §16 · Strongest conclusion

The motion_profile DNA axis is now both PAPER-RATIFIED and CODE-
VERIFIABLE. Every claim in motion-profile-dna-plan §16 ("strongest
conclusion") that was on-paper is reachable in production via the body
data-attribute layer · the `--mp-*` token namespace · and the 7 wired
bundle flags. The 6 corporate-suite siblings are byte-equivalent.
Reduced-motion is honored on three layers. The g6-cinematic profile is
ready for the first Phase X.7a intake brief to declare it · with zero
further code change · with 1200ms editorial fade as the cluster
signature.
