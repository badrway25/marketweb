# Release gatekeeper · Continua Pass B Multilingual · 2026-04-30

## 1 · Decision

**HOLD public flip.** Tier remains `draft` in DB and registry.

## 2 · Why hold

Pass B is the multilingual rollout pass (workflow C). Public flip is a separate workstream (workflow D · `release-decision-orchestrator.md`) that needs:

- the user-handshake binary (cluster R-SOL-8)
- the user's explicit visual review of all 5 locales
- the gatekeeper's evidence-based sign-off

This pass earned the right for that handshake to open — it did not flip the gate itself.

## 3 · Per-locale flip-decision matrix

| Locale | Walk verdict | Blocking | Anchor preserved? | RTL parity? | Recommended |
|---|---|---|---|---|---|
| IT | PASS | 0 | ✓ generazioni | n/a | flip-eligible at workflow D |
| EN | PASS | 0 | ✓ generations | n/a | flip-eligible at workflow D |
| FR | PASS | 0 | ✓ générations | n/a | flip-eligible at workflow D |
| ES | PASS | 0 | ✓ generaciones | n/a | flip-eligible at workflow D |
| AR | PASS | 0 (post-fix) | ✓ بالأجيال | ✓ | flip-eligible at workflow D |

5 locales, 5 PASS, 0 BLOCKING. The flip can land on all 5 simultaneously when workflow D opens — there is no held-locale subset.

## 4 · Pass D cascade preview

When the user authorises the public flip, the orchestrator routes to `release-decision-orchestrator.md` which performs:

1. **Tier flip in registry**: `TEMPLATE_REGISTRY.json` row `continua-stewardship.tier` from `draft` → `published_live` (1 line edit).
2. **Tier flip in DB**: `python manage.py sync_template_tiers` propagates registry → DB (1 transient SQL update).
3. **Tier-fact tests**: 6 corporate-suite contract tests that scan tier-fact will need to count Continua among the live siblings (5 → 6 within the `corporate-suite` archetype).
4. **Trust counter**: `22+` → `23+` on the catalog page (1 string).
5. **Public catalog count**: 22 → 23 (computed automatically from the registry · no edit needed).
6. **MEMORY.md roll-up**: `phase_x4_continua_passB_multilingual.md` checkpoint added · current-baseline pointer updated · earlier `continua-pass1` / `continua-lf5` entries roll into a "RECENT" stack.
7. **Cross-cluster smoke**: 23/23 catalog cards reachable + 5/5 Continua locales reachable · re-run the 834/834 smoke + the 546/546 test suite.

The cascade is documented to the line so the gatekeeper can ship without re-discovery.

## 5 · Risk register

| Risk | Severity | Mitigation status |
|---|---|---|
| Voice anchor lost on a translation | HIGH | MITIGATED · 5/5 locales preserve em on the equivalent temporal noun |
| LF-5 layout reshapes under RTL | HIGH | MITIGATED · DOM verified identical across 5 locales · zero overflow at every viewport |
| Arabic typography breaks (Latin tracking) | MEDIUM | MITIGATED · CS-TYPE-05 reset extended to 10 LF-5 surfaces · `letter-spacing: normal` confirmed |
| Cross-locale imagery substitution | MEDIUM | MITIGATED · `_POOL_*` constants make substitution structurally impossible |
| `?preview=1` leak across locale switcher | MEDIUM | MITIGATED · staff-preview-aware href generation works on all 5 locale pills |
| Pre-existing booking-flag test failure | LOW | DOCUMENTED · out of scope (LF-5 IT rebuild §8.4) · unrelated to Pass B |
| Sibling regression (Pragma · Fiscus · Solaria) | LOW | MITIGATED · chrome edit is RTL-scoped only · IT/EN/FR/ES bytes preserved |

No HIGH or MEDIUM risk left active.

## 6 · Evidence package

```
factory/reports/continua/continua-passB-multilingual.md                              (Pass B detail)
factory/reports/browser-verification/continua-passB-multilingual.md                  (browser walk index)
factory/reports/browser-verification/continua-passB-multilingual/                    (7 captures)
factory/reports/scorecard/continua-passB-multilingual/build-report.md
factory/reports/scorecard/continua-passB-multilingual/style-critic.md
factory/reports/scorecard/continua-passB-multilingual/contrast-accessibility.md
factory/reports/scorecard/continua-passB-multilingual/responsive-auditor.md
factory/reports/scorecard/continua-passB-multilingual/browser-verifier.md
factory/reports/scorecard/continua-passB-multilingual/release-gatekeeper.md          (THIS file)
factory/reports/scorecard/continua-passB-multilingual/scorecard.md                   (aggregate)
factory/reports/scorecard/continua-passB-multilingual/summary.md                     (one-paragraph)
```

8 panel files in the scorecard package · all GREEN.

## 7 · Verdict

Release gatekeeper recommends: **review-ready at draft tier, ready for the workflow D / user-handshake decision.** No regression on any sibling. No active blocker on any locale. The cascade for the public flip is documented to the line — workflow D can ship on user sign-off without further discovery work.
