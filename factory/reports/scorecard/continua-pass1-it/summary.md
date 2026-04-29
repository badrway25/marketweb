# Continua · Pass 1 IT · Summary

**Date**: 2026-04-29
**Branch**: `phase-x4-design-orchestrator-hardening-v1`
**Source brief**: `design-orchestrator/real-candidates/continua-build-brief.md`
**Sibling distinctness gate**: 5/5 vs Pragma · 5/5 vs Fiscus · 5/5 vs Solaria
**Scorecard aggregate**: **4.74 / 5** · 0 `[BLOCKING]` · 0 deviation

---

## What landed

Continua is the 4th corporate-suite sibling and the 1st family-office variant in the cluster. Pass 1 ships the IT template at draft tier with:

- Pine + pewter + brass palette (matrix §1.3 cool-secondary + warm-accent · the only OPEN warmth combo)
- Crimson Pro + Public Sans typography (closes the §1.4 Inter-collapse risk)
- Object-led hero with zero people — the cluster's first
- A new mid-strip beat (`governance-cycle-strip`) that names a CADENCE not a number / calendar / arc
- Leadership 3-card row spanning 40s · 50s · 60s + 2 women + 1 man + 3 visible ethnicities (closes Solaria's 30sCx2 demographic gap)
- "Avvia un dialogo di mandato" CTA + scope + orizzonte + struttura form gate (NO P.IVA + CF · NO NDA-boardroom · NO ICF-referenced)
- Whistleblowing channel (D.lgs. 24/2023) prominent in legal row + footnote

---

## What was on the line

The brief locked five risky overlaps before A.5 entry. All five were verified live during the walk:

| Risk | Verdict | Evidence |
|---|---|---|
| R1 Pragma palette echo | PASS | 5+ brass touchpoints visible at first scroll across 1920 / 1280 / 720 |
| R2 Fiscus hero adjacency | PASS | hero crop reads room-architectural · 0 documents · 0 laptop · 0 humans at every viewport |
| R3 Pragma stakeholder one-liner | PASS | "famiglia · generazioni · Consiglio di Famiglia" surface in first-scroll eyebrow + h1 + subhead + meta-strip; remove-the-studio-name swap test passes |
| R4 Solaria leadership-photo | PASS | 3 distinct demographics readable at 1920 / 1280 / 768 / 390 |
| R5 Mid-strip cadence framing | PASS | each cycle cell renders the (eyebrow · figure · context-line) triple at every viewport — the context-line does NOT drop |

---

## Where the live walk caught a real defect

The initial slot 0 hero candidate (Pexels 207658) returned a "BACK TO SCHOOL" Scrabble-tile composition — a curator-level fail per Risk 2's "no documents > 1, no human, no laptop" rejection rule. The walk caught this immediately, the curator searched the Pexels UI mid-session, and the replacement (Pexels 36093623 — historic library room with rich wooden interiors, partner desk in foreground, fireplace + leather chair · zero people) was screenshot-verified before commit. The replacement reads more strongly on-brief than the original "library / partner-study reading room with brass lamp on desk" specification — the room's full mahogany interior + fireplace + chair carries "stewardship office" at first glance.

This is the design-orchestrator system catching its first real defect inside the same workflow A pass that would have shipped it. Documented in `build-report.md §1` and `style-critic.md` `[INFO]` block.

---

## What's left vs the brief

| Brief item | Pass 1 status |
|---|---|
| IT-only draft | DONE — `tier: draft` in `TEMPLATE_REGISTRY.json` |
| 5 page kinds (home, about, services, case_study_list, case_study_detail, contact) | DONE — all 9 routes return HTTP 200 |
| 4-pillar count | DONE |
| Governance-cycle-strip mid-beat | DONE |
| Object-led hero + zero people | DONE (after live re-curate) |
| 3 stewards photo-present + diverse demographics | DONE |
| 4 mandates "in continuità" with multi-year markers | DONE |
| Form gate scope + orizzonte + struttura | DONE |
| Whistleblowing legal row | DONE |
| EN/FR/ES/AR locales | DEFERRED — workflow C |
| AR RTL parity walk | DEFERRED — workflow C |
| LIVE flip + user-handshake binary | DEFERRED — workflow C |

---

## Server state at end of pass

- Server command: `python manage.py runserver 8088` (background, ID `b2d6earw4`)
- URL kept open: `http://127.0.0.1:8088/templates/business/continua-stewardship/preview/`
- Tier in DB: `published_live` (transient — flipped only for the dev walk so the staff-preview gate didn't block visual review)
- Tier in registry: `draft` (correct · re-applies on next `seed_templates` run)

The user can open the URL above in a browser and walk all 9 pages without any auth. The DB-level tier flip is reversible — running `python manage.py seed_templates` will re-sync the tier from `TEMPLATE_REGISTRY.json` and restore `draft`.

---

## Verdict

**Continua IT pass 1 is ready for human visual review.**

Three checkpoints worth focusing the review on:
1. Brass landing on first scroll — does the brass read as the cool-on-cool palette differentiator vs Pragma's emerald?
2. Hero photo coherence — does the historic library room read as a stewardship office (NOT a generic warm interior)?
3. Cycle-strip framing — do the three cells read as a calendar rhythm (NOT three numeric KPIs)?

If all three land in the user's read of the page, pass 1 is human-ratified at draft tier and the orchestrator can route to workflow C planning. If any drift, the affected mitigation has a fallback ladder documented in `continua-distinctness-proof.md §5`.
