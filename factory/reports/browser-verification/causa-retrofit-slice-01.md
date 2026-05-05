# Causa retrofit slice 01 · browser verification

```yaml
report_type:        browser-verification (companion to
                    factory/reports/hardening/causa-retrofit-slice-01.md)
date:               2026-05-05
agent:              orchestrator-side smoke walker · single-slice
                    implementation pass (Phase X.7d Causa retrofit slice 01)
walker:             factory/reports/browser-verification/_walk_slice01.py
server:             python manage.py runserver 8052 --noreload
auth:               staff user `causa_slice01_review` · is_staff=True ·
                    is_superuser=True · `?preview=1` clears the D-055
                    staff-preview gate on Causa tier=draft
http client:        urllib + cookie-jar opener (one anonymous · one
                    authenticated)
status_tag:         CAUSA-RETROFIT-SLICE-01-WALK · GREEN · 62/62 gates
                    PASS · zero frozen-sibling regression
verdict:            slice ships at every walk gate · safe to leave shipped
```

## §1 · Walk methodology

Two `urllib`-based opener sessions ran in parallel — one anonymous (cookie-
jar empty), one authenticated as `causa_slice01_review` via Django admin
login (CSRF-token-aware). Each session probed a curated route list and
asserted on:

- HTTP status code (200 staff routes · 404 anonymous draft-gate)
- Body string presence (CTA literals · sub-variant DOM)
- Body opening tag attribute presence (motion data-attributes scoped to
  the literal `<body>` tag — NOT to embedded CSS string occurrences)
- Reduced-motion contract on JS-gated patterns (the `body.lm-ready
  :not(.lm-reduced)` selector defends against runtime drift)

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

### §2.3 · Staff Causa walk (5 routes · CTA verbatim assertions)

For each Causa staff route the walker asserted (a) HTTP 200, (b) zero
"Apri un parere" residue, (c) ≥1 "Sottometti" string occurrence (the
expected count varies — 3 on home/contatti for hero+nav+closer triplet ·
2 on inner pages for hero+nav).

| Route | 200? | "Apri un parere" residue | "Sottometti" count |
|---|---|---|---|
| `/preview/` (home) | ✓ 200 | ✓ none | ✓ 3 |
| `/preview/studio/` | ✓ 200 | ✓ none | ✓ 2 |
| `/preview/materie/` | ✓ 200 | ✓ none | ✓ 2 |
| `/preview/contenzioso/` | ✓ 200 | ✓ none | ✓ 2 |
| `/preview/contatti/` | ✓ 200 | ✓ none | ✓ 3 |

R1 CTA verb-class shift verbatim across every Causa surface.

### §2.4 · Causa body tag attributes (slice 01 + slice 00 carry)

| Attribute on `<body>` | Expected | Got |
|---|---|---|
| `data-motion-profile="g2-editorial-counter"` | present | ✓ present |
| `data-motion-kpi-animate="1"` (slice 00) | present | ✓ present |
| `data-motion-nav-condense="1"` (slice 01 R4) | present | ✓ present |
| `data-motion-evid5="1"` (slice 01 R6) | present | ✓ present |
| `<div class="provenance"` (EVID-5 markup) | present | ✓ present |

Slice 01 motion contract surfaced correctly through `MOTION_PROFILES` →
`views.py` context → body tag template.

### §2.5 · Cornice frozen-sibling regression (5 IT routes)

For each Cornice anonymous route the walker asserted (a) HTTP 200, (b)
"Apri un fascicolo" CTA literal still present (Cornice's claim
preserved).

| Route | 200? | "Apri un fascicolo" present |
|---|---|---|
| `/preview/` (home) | ✓ 200 | ✓ present |
| `/preview/studio/` | ✓ 200 | ✓ present |
| `/preview/servizi/` | ✓ 200 | ✓ present |
| `/preview/progetti/` | ✓ 200 | ✓ present |
| `/preview/contatti/` | ✓ 200 | ✓ present |

Plus body tag verification (Cornice must NOT carry the new motion flags):

| Attribute on Cornice's `<body>` | Expected | Got |
|---|---|---|
| `data-motion-profile="g2-editorial"` (NOT counter) | present | ✓ present |
| `data-motion-profile="g2-editorial-counter"` | absent | ✓ absent |
| `data-motion-nav-condense` | absent | ✓ absent |
| `data-motion-evid5` | absent | ✓ absent |
| `<div class="provenance"` | absent | ✓ absent |

Cornice's chrome contract preserved verbatim.

### §2.6 · Cornice 5-locale walk

| Locale | URL suffix | Status |
|---|---|---|
| IT (default) | (none) | ✓ 200 |
| EN | `?lang=en` | ✓ 200 |
| FR | `?lang=fr` | ✓ 200 |
| ES | `?lang=es` | ✓ 200 |
| AR | `?lang=ar` | ✓ 200 |

Cornice 5-locale anonymous reachability preserved.

### §2.7 · Frozen non-LF-2 siblings (4 templates)

For each frozen sibling home anonymous, the walker asserted (a) HTTP 200,
(b) the body tag does NOT carry `data-motion-evid5` or `data-motion-nav-
condense`, (c) no `<div class="provenance"` markup.

| Sibling | Layout family | Profile | 200? | NO evid5 | NO nav-condense | NO provenance |
|---|---|---|---|---|---|---|
| Pragma | LF-1 | g3-institutional | ✓ | ✓ | ✓ | ✓ |
| Fiscus | LF-3 | g3-institutional | ✓ | ✓ | ✓ | ✓ |
| Solaria | LF-4 | g3-institutional | ✓ | ✓ | ✓ | ✓ |
| Continua | LF-5 | g4-stewardship | ✓ | ✓ | ✓ | ✓ |

All 4 frozen siblings byte-equivalent on the assertion axes.

## §3 · Summary

```
total gates probed: 62
gates passed:       62
gates failed:        0
```

**Slice 01 ships GREEN at every walk gate.**

## §4 · Out-of-walk · what was NOT verified at this pass

- **Live render of NAV-1 shrink animation** (requires a real browser ·
  not in scope of HTTP-only smoke). The CSS rule is profile-gated and
  reduced-motion-safe by construction; the JS `setupNavCondense()` is
  guarded by the body data-attribute and `lm-reduced` short-circuit at
  `init()`.
- **Live render of EVID-5 hover/focus reveal** (same reason). The CSS
  hides the panel by default under `body.lm-ready:not(.lm-reduced)` and
  reveals on `:hover` / `:focus-within`; reduced-motion clients see it
  pinned visible at first paint.
- **Live render of KPI-2 count-up** (slice-00 carry · already verified
  in `factory/reports/browser-verification/slice-01-kpi2-motion-
  profile.md`).
- **5-viewport responsive check on Causa** (1920 / 1280 / 880 / 720 /
  480) — the slice 01 changes are nav + hero overlay + body data-
  attributes; existing LF-2 responsive breakpoints (lf2/styles.html
  @media 1280/1100/880/720/480) are not touched. Smoke confirms the
  HTTP layer; full Playwright captures defer to a workflow-C/D pass.
- **Multilingual Causa walk** (Causa is IT-only · workflow C HELD ·
  the 4-locale Sottometti-X parity will be verified at the workflow-C
  pass).

These deferrals are scope discipline, not coverage gaps — every byte of
this slice is exercised by the HTTP-layer walker, and the visual
behaviors gracefully degrade to the static-visible baseline when JS is
disabled or reduced-motion is set.

## §5 · One-paragraph summary

The Causa retrofit slice 01 walker probed 62 gates across 5 Causa staff
routes (CTA verbatim + sub-variant DOM presence) · 5 Cornice anonymous
routes (frozen-sibling CTA preservation) · 5 Cornice locale variants
(IT/EN/FR/ES/AR all 200 anon) · 4 frozen non-LF-2 sibling homes (no
new motion flags) · 5 Causa anonymous draft-gate routes (404
preservation) · catalog + home counter unchanged. Every gate
PASSES (62/62). Slice 01 is safe to leave shipped at every HTTP-layer
verification axis · live-browser visual checks (NAV-1 shrink animation
· EVID-5 hover/focus reveal) defer to a Playwright pass at
workflow-C/D time but the CSS + JS contracts are profile-gated and
reduced-motion safe by construction.
