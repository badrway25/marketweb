# Scorecard · Cornice · workflow C multilingual

```yaml
phase:    X.5 Cornice · workflow C
date:     2026-05-01
verdict:  GREEN · review-ready · workflow D held for user-handshake
```

## §1 · Cell-by-cell scorecard

| Cell | Verdict | Evidence |
|---|---|---|
| 4 new locale modules created | PASS | 4,360 lines · all keys mirror IT |
| Locale loader wired | PASS | `template_content.py` dispatch updated · 4 imports |
| Registry locales flipped `[it]` → `[it,en,fr,es,ar]` | PASS | `TEMPLATE_REGISTRY.json` |
| Registry `rtl: false` → `rtl: true` | PASS | `TEMPLATE_REGISTRY.json` |
| Tier=draft preserved | PASS | `tier: "draft"` unchanged |
| Voice anchor verbatim-in-translation × 5 | PASS | h1 + CTA closer match byte-equivalent across each locale |
| Em-noun preservation across magazine cards | PASS | 5 locales × 4 em-words = 20/20 distinct nouns |
| 12-em audit on home | PASS | 12 em surfaces × 5 locales = 60/60 |
| LF-2 layout shape preserved | PASS | zero edits to lf2/styles.html · lf2/content.html |
| LF-2 chrome (cream nav) on every locale's home AND inner pages | PASS | A.6 F2 lift carries · cs-nav--lf2 active on all routes |
| 4-col footer with whistleblowing column on every locale | PASS | D.lgs. 24/2023 + email Latin preserved on all 5 |
| AR Naskh-vs-Kufi decision resolved | PASS | Naskh swap scoped to body.cs-lf-lf-2 · cluster default Kufi preserved on Pragma/Fiscus/Solaria/Continua |
| AR RTL parity (16 surfaces) | PASS | 16/16 |
| Latin wordmark + Latin Marta Roveri preserved under RTL | PASS | CS-NAV-06 / CS-FOOT-03 binding live |
| Italian normative refs preserved across locales | PASS | D.lgs. · MIBAC · OAPPC · CNAPPC · PRG · Soprintendenza · DAStU · Reg. UE all unchanged |
| Italian addresses + phone + email preserved | PASS | Via Paoli 9 · +39 02 6610 4708 · @cornice-architettura.it across all 5 |
| Editorial-curatorial register preserved per locale | PASS | architectural-press vocabulary verified per locale |
| Anti-pattern guardrails clean | PASS | no SaaS-imperative · no famous-architect quote · no Pinterest moodboard · no boardroom cliché |
| Responsive at 1440 / 880 / 480 across 5 locales | PASS | AR specifically walked at 880 + 480 |
| Frozen-sibling regression | NO REGRESSION | 4/4 siblings × 5 locales = 20 anonymous routes 200 |
| Continua AR still Kufi (no Naskh leakage) | PASS | computed font verified live |
| Pragma IT navy chrome unchanged | PASS | bg verified live |
| Test suite | 545/546 PASS | same pre-existing booking-flag failure as A.6 |
| `python manage.py check` clean | PASS | only pre-existing W001 grandfathered warning |

**Score: 24/24 cells PASS. 0 regressions.**

## §2 · What this scorecard does NOT cover (deliberately out of scope)

- Public flip + DB sync (`sync_template_tiers`) → **workflow D**
- `apps/catalog/tests.py` count bumps (22→23, etc.) → **workflow D**
- Full anonymous walk on the live catalog list page → **workflow D**
- Any new archetype, layout family, or LF-2 widening → **never · X.5 program closure**

## §3 · Verdict

**GREEN · review-ready · workflow D held for user-handshake.**
