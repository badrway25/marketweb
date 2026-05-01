# Cornice · A.6 IT review-lock · Release-gatekeeper panel

```yaml
panel:    release-gatekeeper
phase:    A.6 review-lock (IT-only)
date:     2026-05-01
score:    4.8 / 5
floor:    4.5
verdict:  PASS · CLEARED FOR USER VISUAL HANDSHAKE
```

## §1 · A.6 hard-constraint compliance check

| Constraint | Status |
|---|---|
| Italian only · no multilingual yet | PASS — Cornice locales = `[it]`. EN/FR/ES/AR untouched. |
| No public flip · tier=draft preserved | PASS — TEMPLATE_REGISTRY.json unchanged. WebTemplate row tier still `draft`. Anonymous returns 404 on Cornice routes. |
| Browser-live verification mandatory | PASS — Playwright MCP walked all 9 IT routes pre-fix and post-fix. 36 captures. |
| Playwright MCP mandatory | PASS — used throughout the walk |
| Keep server running and report URL/port | PASS — `http://127.0.0.1:8052/` running at hand-back |
| Preserve frozen siblings with zero drift | PASS — 4/4 frozen siblings byte-equivalent before/after; verified anonymous live |
| No apps/editor changes | PASS — zero edits |
| No apps/projects changes | PASS — zero edits |
| No apps/commerce changes | PASS — zero edits |
| No new archetypes | PASS — corporate-suite count still 5 (Pragma · Fiscus · Solaria · Continua · Cornice) |
| Do not weaken LF-2 distinctness | PASS — 5/5 axes vs every sibling; 9/9 (or 8/9) layout-distinctness; F3 STRENGTHENS L7 magazine-grid distinctness |

**11/11 hard constraints clear.**

## §2 · Mandatory verification checklist (from task brief)

| Item | Verdict |
|---|---|
| Hero overlay quality | PASS — KPI tuple inside photo overlay; cream-on-photo with gradient scrim ≥AA at every viewport |
| Magazine-grid quality | PASS — F3 fix; dominant hero photo + body+meta at foot + card baselines align (DOM-verified) |
| Leadership single-portrait credibility | PASS — F1 fix; photo↔copy now agree (Marta Roveri); environmental NOT headshot read intact |
| Navbar/footer polish | PASS — F2 fix; cream LF-2 nav consistent across all 9 pages; 4-col-with-whistleblowing footer on every page |
| Responsive behavior | PASS — 1440 / 1100 / 880 / 480 walked; no horizontal scroll; no content drop |
| Contrast/readability | PASS — chrome and content surfaces clear AA; display-typographic surfaces clear AA-large or AAA |
| Route usability in draft preview | PASS — staff session + `?preview=1` reaches all 9 routes 200; anonymous 404 |
| Frozen sibling stability | PASS — 4/4 unchanged; F1+F2+F3 all selector-scoped or content-scoped; no collateral |
| Premium/editorial feel on first scroll and full page | PASS — golden-hour Bologna portico + KPI overlay + voice anchor `argomento` reads consistently editorial-publication; full page maintains the register through narrative + sectors + leadership + magazine + cta-closer + footer |

**9/9 mandatory verification items clear.**

## §3 · A.5 → A.6 delta summary

| Surface | A.5 state | A.6 post-fix state |
|---|---|---|
| Founder identity | `Marco Roveri` + masculine Italian + photo of woman | `Marta Roveri` + feminine Italian + photo of woman (consistent) |
| Inner-page navbar | dark LF-1 default (chrome-class set but body styles missing) | cream LF-2 with split wordmark + filled rust CTA on all 9 pages |
| Magazine-grid hero card | photo aspect-ratio 16/9 + visible empty band below pill (~350-450px) | photo flex-grow + min-height 360 + body+meta clustered at foot + card baselines aligned |
| Distinctness vs siblings | 5/5 (margin) | 5/5 (same margin · L7 STRENGTHENED) |
| Frozen siblings | 4/4 PASS | 4/4 PASS (no regression introduced) |
| Tier | draft | draft (preserved) |
| Test suite | 545/546 | 545/546 (same pre-existing failure) |
| Total source files modified | 13 (8 modified + 5 created at A.5) | 16 (3 additional files modified at A.6) |

## §4 · Pass-or-hold decision

**PASS · CLEARED FOR USER VISUAL HANDSHAKE.**

The Cornice IT draft is now truly review-locked. The user can
visit `http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?preview=1`
on the staff session and walk all 9 IT routes without
encountering review-blocking defects.

The three findings that A.6 promoted to fix-status are all
landed and re-verified live:

- F1 (review-blocking founder gender mismatch): photo↔copy now agree
- F2 (high chrome consistency): cream LF-2 nav uniform across 9 pages
- F3 (medium editorial rhythm): magazine spread reads as Casabella spread

The user-handshake gate is the next step. The handshake answers
the open questions in `cornice-a6-it-review-lock.md §10` (LF-2
hero distinctness vs Continua, single-portrait masthead read,
3+1 magazine spread, cream nav register, architectural-vocabulary
density + `argomento` motif).

## §5 · On user GO

Workflow C kicks off:
- EN/FR/ES/AR translations of the entire CORNICE_CONTENT_IT dict
- AR RTL handling (Naskh-vs-Kufi decision per planner-brief §11)
- TEMPLATE_REGISTRY.json locales flip from `[it]` to `[it, en, fr, es, ar]` + `rtl: true`
- Per-page browser walk at every locale + AR RTL
- Tier remains `draft` through workflow C
- Workflow D (public flip) gated on a second user handshake on the multilingual walk

## §6 · On user HOLD

A.7 narrow re-author OR A.6b re-build per the documented
re-spec authority. The fix budget for a HOLD response stays
within the LF-2 family scope rules.

## Why score = 4.8 / 5

All 11 hard constraints + all 9 mandatory verification items
clear. The 0.2 deduction is for two soft items:

- The F3 between-fix iteration cost a small process margin (the
  margin-top:auto attempt didn't ship, and a server restart was
  needed mid-session because Django runserver --noreload doesn't
  reload module-level constants on edit).
- The privacy-consent line and a few generic-role-term cases
  remain in masculine-default Italian. Out of A.6 scope (not
  Marta-specific) but flagged for a future inclusivity polish.
