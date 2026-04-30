# Pre-rebuild baseline · 2026-04-29

Captured before any code change so post-rebuild regression on the three frozen siblings can be measured at the byte/pixel level. URL pattern: `http://127.0.0.1:8042/templates/business/<slug>/preview/?preview=1` in a `cs_review_fix` superuser session.

## Section-list per sibling (1920×1080)

| Sibling | Section list (live render) | Notes |
|---|---|---|
| Pragma   | cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta | LF-1 reference (no cycle) |
| Fiscus   | cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta | LF-3 today, but `cycle_strip` not authored — no `cs-cycle` rendered |
| Solaria  | cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta | LF-4 in spirit (manifesto-style content); same DOM |
| Continua | cs-hero · cs-pillars · cs-kpi-band · **cs-cycle** · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta | The only sibling actually rendering `cs-cycle` (slot-4) today |

## Total page heights (1920px)

| Sibling | Document height | Total height |
|---|---|---|
| Pragma   | hero 686 + offset → cta-bottom **4310** |
| Fiscus   | cta-bottom **4578** |
| Solaria  | cta-bottom **4968** |
| Continua | cta-bottom **5737** (cycle adds 733+padding) |

## Bounding-box overlap diagnosis

Pragma vs Fiscus, Pragma vs Solaria, Fiscus vs Solaria all share an **identical 8-section list** at the same x-extent (cs-hero/kpi-band/sectors/trust/cta full-bleed at 1905px; cs-pillars/leadership/cases-preview at 1400px wrapped in 253px paper margin). Y-positions drift only by content height inside each section. Per the divergence-plan §1, the three siblings overlay at >90% bounding-box surface area against each other.

Continua vs Fiscus differ by exactly one section (`cs-cycle` at slot-4 on Continua). Per the divergence plan §5, this is **in-family variation**, not family-difference.

## Frozen-sibling regression contract

After the LF-5 rebuild lands, **0 px** of bounding-box drift is required for Pragma · Fiscus · Solaria when re-rendered at 1920px in the same staff session. Continua is allowed to change radically (target: ≥30% bounding-box surface-area difference vs each frozen sibling).

## Files filed in this directory

- `pragma-1920-fullpage.png`
- `fiscus-1920-fullpage.png`
- `solaria-1920-fullpage.png`
- `continua-1920-fullpage-pre-rebuild.png`
- `section-list-{pragma,fiscus,solaria,continua}.json`
- `baseline-summary.md` (this file)
