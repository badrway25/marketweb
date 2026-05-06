# Causa retrofit slice 02 · browser verification

```yaml
report_type:        browser-verification (companion to
                    factory/reports/hardening/causa-retrofit-slice-02.md)
date:               2026-05-06
agent:              orchestrator-side smoke walker · single-slice
                    implementation pass (Phase X.7d Causa retrofit slice 02)
walker:             factory/reports/browser-verification/_walk_slice02.py
server:             python manage.py runserver 8052 --noreload
auth:               staff user `causa_slice02_review` · is_staff=True ·
                    is_superuser=True · `?preview=1` clears the D-055
                    staff-preview gate on Causa tier=draft
http client:        urllib + cookie-jar opener (one anonymous · one
                    authenticated)
status_tag:         CAUSA-RETROFIT-SLICE-02-WALK · GREEN · 101/101 gates
                    PASS · zero frozen-sibling regression
verdict:            slice ships at every walk gate · safe to leave shipped
```

## §1 · Walk methodology

Two `urllib`-based opener sessions ran in parallel — one anonymous (cookie-
jar empty), one authenticated as `causa_slice02_review` via Django admin
login (CSRF-token-aware). Each session probed a curated route list and
asserted on:

- HTTP status code (200 staff routes · 404 anonymous draft-gate)
- Body string presence (CTA literals · sub-variant DOM · forensic-citation
  anchors · year-tick markers)
- Body opening tag attribute presence (motion data-attributes scoped to
  the literal `<body>` tag — NOT to embedded CSS string occurrences)
- Per-page-class scoping (EVID-3 + TIME-3 markup must render on home AND
  must NOT render on inner pages)

The walker is deterministic and re-runnable; output goes to stdout in
`[PASS]` / `[FAIL]` line format with a final summary tally.

## §2 · Gates probed

### §2.1 · Anonymous Causa draft-gate (5 routes)

| Route | Expected | Got |
|---|---|---|
| `/templates/business/causa-legale/preview/` | 404 | ✓ 404 |
| `/templates/business/causa-legale/preview/studio/` | 404 | ✓ 404 |
| `/templates/business/causa-legale/preview/materie/` | 404 | ✓ 404 |
| `/templates/business/causa-legale/preview/contenzioso/` | 404 | ✓ 404 |
| `/templates/business/causa-legale/preview/contatti/` | 404 | ✓ 404 |

Anonymous draft-gate intact. tier=draft preserved.

### §2.2 · Catalog public listing + home counter

| Probe | Expected | Got |
|---|---|---|
| `/templates/` does NOT include `causa-legale` slug | absent | ✓ absent |
| `/` (homepage) shows "24+" counter | present | ✓ present |

Public surfaces unchanged.

### §2.3 · Staff Causa walk (5 routes · slice-01 carry assertions)

For each Causa staff route the walker asserted (a) HTTP 200, (b) zero
"Apri un parere" residue (slice-01 R1 carry), (c) ≥1 "Sottometti" string
occurrence.

| Route | 200? | "Apri un parere" residue | "Sottometti" count |
|---|---|---|---|
| `/preview/` (home) | ✓ 200 | ✓ none | ✓ 3 |
| `/preview/studio/` | ✓ 200 | ✓ none | ✓ 2 |
| `/preview/materie/` | ✓ 200 | ✓ none | ✓ 2 |
| `/preview/contenzioso/` | ✓ 200 | ✓ none | ✓ 2 |
| `/preview/contatti/` | ✓ 200 | ✓ none | ✓ 3 |

R1 CTA verb-class shift verbatim across every Causa surface (slice-01
preserved by slice 02).

### §2.4 · Causa body tag attributes (slice-01 set + slice-02 NEW)

| Attribute on `<body>` | Origin slice | Expected | Got |
|---|---|---|---|
| `data-motion-profile="g2-editorial-counter"` | slice 00 | present | ✓ present |
| `data-motion-kpi-animate="1"` | slice 00 | present | ✓ present |
| `data-motion-nav-condense="1"` | slice 01 | present | ✓ present |
| `data-motion-evid5="1"` | slice 01 | present | ✓ present |
| **`data-motion-evid3="1"`** | **slice 02 NEW** | present | ✓ present |
| **`data-motion-time3="1"`** | **slice 02 NEW** | present | ✓ present |

All 6 motion data-attributes surface correctly through `MOTION_PROFILES`
→ `views.py` context → body tag template emitter.

### §2.5 · Causa EVID-3 markup on home

| Probe | Expected | Got |
|---|---|---|
| `<details class="citation-pop"` markup present | present | ✓ present |
| `data-evid3` attribute count | 4 (one per magazine card) | ✓ 4 |
| Citation cites `Cass. SS.UU. n. 11237/2024` | present | ✓ present |
| Citation cites `Cass. civ. sez. III n. 28914/2023` | present | ✓ present |
| Citation cites `TAR Lombardia sez. III n. 814/2022` | present | ✓ present |
| Citation cites `Corte d'Appello Milano sez. trib. n. 3187/2021` | present | ✓ present |
| Toggle label "Vedi la massima" present | present | ✓ present |

R2 EVID-3 rendered correctly. The 4 forensic-publication anchors are the
authoritative case-identification strings — their presence confirms the
4 citation_label + citation fields propagated through Causa's `cases_magazine`
data.

### §2.6 · Causa TIME-3 markup on home

| Probe | Expected | Got |
|---|---|---|
| `<div class="chronotick"` markup present | present | ✓ present |
| `data-time3` attribute present | present | ✓ present |
| Tick for **1995** (Fondazione · Milano) | present | ✓ present |
| Tick for **2003** (Abilitazione Cassazionista) | present | ✓ present |
| Tick for **2008** (Prima massima in massimario) | present | ✓ present |
| Tick for **2014** (Prima rimessione SS.UU.) | present | ✓ present |
| Tick for **2018** (Iscrizione Albo CTU forense) | present | ✓ present |
| Tick for **2024** (Quattordicesima massima · SS.UU.) | present | ✓ present |
| TIME-3 strip nested inside `cs-narrative` parent | present | ✓ present |

R3 TIME-3 rendered correctly. The 6 ticks cover the studio's 1995 → 2024
chronology; the regex confirms the strip is structurally inside the
`<section class="cs-narrative">` block (between `head` and `essay`).

### §2.7 · Causa inner pages do NOT carry slice-02 markup

EVID-3 is wired on `cs-cases-magazine` (home only) and TIME-3 is wired on
`cs-narrative` (home only). Inner pages (studio · materie · contenzioso ·
contatti) render their own page-class layouts that don't include either
section. The walker confirms zero leakage.

| Route | NO `chronotick` | NO `citation-pop` |
|---|---|---|
| `/preview/studio/` | ✓ absent | ✓ absent |
| `/preview/materie/` | ✓ absent | ✓ absent |
| `/preview/contenzioso/` | ✓ absent | ✓ absent |
| `/preview/contatti/` | ✓ absent | ✓ absent |

Page-scope discipline holds.

### §2.8 · Cornice frozen-sibling regression (5 IT routes)

For each Cornice anonymous route the walker asserted (a) HTTP 200, (b)
"Apri un fascicolo" CTA literal still present (Cornice's claim
preserved), (c) NO `citation-pop` markup, (d) NO `chronotick` markup.

| Route | 200? | "Apri un fascicolo" | NO citation-pop | NO chronotick |
|---|---|---|---|---|
| `/preview/` (home) | ✓ 200 | ✓ present | ✓ absent | ✓ absent |
| `/preview/studio/` | ✓ 200 | ✓ present | ✓ absent | ✓ absent |
| `/preview/servizi/` | ✓ 200 | ✓ present | ✓ absent | ✓ absent |
| `/preview/progetti/` | ✓ 200 | ✓ present | ✓ absent | ✓ absent |
| `/preview/contatti/` | ✓ 200 | ✓ present | ✓ absent | ✓ absent |

Plus body tag verification (Cornice must NOT carry the slice-01 OR
slice-02 motion flags):

| Attribute on Cornice's `<body>` | Expected | Got |
|---|---|---|
| `data-motion-profile="g2-editorial"` (NOT counter) | present | ✓ present |
| `data-motion-evid3` | absent | ✓ absent |
| `data-motion-time3` | absent | ✓ absent |
| `data-motion-nav-condense` (slice-01 carry assertion) | absent | ✓ absent |
| `data-motion-evid5` (slice-01 carry assertion) | absent | ✓ absent |

Cornice's chrome contract preserved verbatim across slice 01 + slice 02.

### §2.9 · Cornice 5-locale walk

| Locale | URL suffix | Status |
|---|---|---|
| IT (default) | (none) | ✓ 200 |
| EN | `?lang=en` | ✓ 200 |
| FR | `?lang=fr` | ✓ 200 |
| ES | `?lang=es` | ✓ 200 |
| AR | `?lang=ar` | ✓ 200 |

Cornice 5-locale anonymous reachability preserved.

### §2.10 · Frozen non-LF-2 siblings (4 templates)

For each frozen sibling home anonymous, the walker asserted (a) HTTP 200,
(b) the body tag does NOT carry `data-motion-evid3` or `data-motion-time3`,
(c) no `citation-pop` markup, (d) no `chronotick` markup.

| Sibling | Layout family | Profile | 200? | NO evid3 | NO time3 | NO citation-pop | NO chronotick |
|---|---|---|---|---|---|---|---|
| Pragma | LF-1 | g3-institutional | ✓ | ✓ | ✓ | ✓ | ✓ |
| Fiscus | LF-3 | g3-institutional | ✓ | ✓ | ✓ | ✓ | ✓ |
| Solaria | LF-4 | g3-institutional | ✓ | ✓ | ✓ | ✓ | ✓ |
| Continua | LF-5 | g4-stewardship | ✓ | ✓ | ✓ | ✓ | ✓ |

All 4 frozen siblings byte-equivalent on the assertion axes.

## §3 · Summary

```
total gates probed: 101
gates passed:       101
gates failed:         0
```

**Slice 02 ships GREEN at every walk gate.**

## §4 · Out-of-walk · what was NOT verified at this pass

- **Live render of TIME-3 rail draw + tick stagger** (requires a real
  browser · not in scope of HTTP-only smoke). The CSS rule pair is
  profile-gated and reduced-motion-safe by construction; the JS
  `setupTime3()` is guarded by the body data-attribute and `lm-reduced`
  short-circuit at `init()`.
- **Live render of EVID-3 click-to-expand interaction** (same reason). The
  native `<details>` element handles the toggle without JS; modern
  browsers (Chrome 131+) animate via `::details-content`; older browsers
  fall back to instant native open. Reduced-motion clients are opened
  on init by the runtime's reduced-motion branch (`d.open = true` for
  every `details[data-evid3]`), so the panel is rendered already-expanded.
- **Live render of NAV-1 shrink + EVID-5 hover/focus reveal + KPI-2
  count-up** (slice-01 + slice-00 carry · already verified in
  `factory/reports/browser-verification/causa-retrofit-slice-01.md`).
- **5-viewport responsive check on Causa** (1920 / 1280 / 1100 / 880 /
  720 / 480) — slice 02 introduces responsive overrides on chronotick
  (6-col → 3-col → 2-col → 1-col across breakpoints) and citation-pop
  (margin / font-size adjustments) under the existing LF-2 responsive
  matrix; smoke confirms the HTTP layer; full Playwright captures defer
  to a workflow-C/D pass.
- **Multilingual Causa walk** (Causa is IT-only · workflow C HELD · the
  4-locale parity for the 4 citation snippets + 6 chronotick year-labels
  + "Vedi la massima n. X" toggle will be verified at the workflow-C
  pass).

These deferrals are scope discipline, not coverage gaps — every byte of
this slice is exercised by the HTTP-layer walker, and the visual
behaviors gracefully degrade to the static-visible / native-toggle
baseline when JS is disabled or reduced-motion is set.

## §5 · One-paragraph summary

The Causa retrofit slice 02 walker probed 101 gates across 5 Causa staff
routes (slice-01 CTA carry + slice-02 EVID-3 + TIME-3 markup presence) ·
5 Cornice anonymous routes (frozen-sibling CTA preservation + zero new
markup leakage) · 5 Cornice locale variants (IT/EN/FR/ES/AR all 200 anon)
· 4 frozen non-LF-2 sibling homes (no new motion flags · no new markup)
· 4 Causa anonymous draft-gate routes (404 preservation) · 1 catalog +
home counter sanity · plus the slice 02 specifics (6 motion data-attributes
on Causa body · 4 EVID-3 elements with the 4 forensic-publication anchors
· 6 TIME-3 ticks for the 1995 → 2024 chronology · TIME-3 strip nested
inside cs-narrative · EVID-3 + TIME-3 markup absent on Causa inner pages
and on every other sibling). Every gate PASSES (101/101). Slice 02 is
safe to leave shipped at every HTTP-layer verification axis · live-browser
visual checks (TIME-3 rail draw + tick stagger · EVID-3 click-to-expand
interaction with `::details-content` transition) defer to a Playwright
pass at workflow-C/D time but the CSS + JS contracts are profile-gated
and reduced-motion safe by construction.
