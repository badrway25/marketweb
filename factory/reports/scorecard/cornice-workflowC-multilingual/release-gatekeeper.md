# Release gatekeeper · Cornice · workflow C multilingual

```yaml
phase:    X.5 Cornice · workflow C
date:     2026-05-01
gate:     workflow-D · public-flip authorisation
verdict:  HOLD · awaits user-handshake on the multilingual walk
```

## §1 · What workflow C delivered

5 locales authored on top of the locked LF-2 IT shape:
- 4 new content modules (EN/FR/ES/AR) · ~4,360 new lines
- 3 minimal wiring edits (loader · base.html chrome · registry)
- voice anchor verbatim-in-translation across all 5 locales
- AR Naskh-vs-Kufi decision resolved (planner-brief §11) — LF-2-
  scoped Naskh swap, every other RTL skin keeps Kufi
- LF-2 layout shape preserved exactly (zero edits to lf2/styles.html
  or lf2/content.html)
- frozen siblings 0/4 regression
- test suite 545/546 (same pre-existing failure as A.6)

## §2 · What workflow D will need to do (NOT in this scope)

If user signals **GO** on the multilingual review, workflow D ships
the public flip + cascade:

1. `TEMPLATE_REGISTRY.json` — Cornice row `tier`: `draft` →
   `published_live`. (Already locales-flipped + rtl true at workflow
   C.)
2. `python manage.py sync_template_tiers` — flips the DB row to
   match.
3. `apps/catalog/tests.py` — bump test assertions that track the
   catalog distribution count (current 23 → 24 published_live, 1 →
   0 draft). Likely 7 explicit-literal bumps (mirroring the Continua
   public-flip cascade · `22→23`, `"22+"→"23+"` precedent).
4. Live anonymous walk re-confirmation (anonymous → home + 5 locales
   200 · catalog list contains Cornice slug × 5 locales · home
   counter `24+`).

Workflow C explicitly does NOT do any of the above.

## §3 · Hold conditions

Cornice tier stays `draft` until ALL of the following are true:

- [ ] User performs the visual handshake on the 5-locale walk.
- [ ] User confirms voice register holds in EN/FR/ES/AR (no flatten).
- [ ] User confirms AR Naskh decision is editorially correct for the
      LF-2 family (or asks for Kufi instead — single-line revert).
- [ ] User signals GO for workflow D.

## §4 · Risks the gate watches

| Risk | Severity | Mitigation in workflow C | Status |
|---|---|---|---|
| Voice flatten in translation (loss of editorial-curatorial register) | high | per-locale lexical anchors documented in `style-critic.md` · architectural press references invoked per locale · normative refs preserved Latin | mitigated · live walk PASS |
| AR typography hostility (Kufi vs Naskh on editorial register) | high | planner-brief §11 decision resolved · LF-2-scoped Naskh swap · CS-TYPE-05 italics-to-bold reset | mitigated · live walk PASS |
| RTL layout collapse | high | logical-property layer pre-existing · LF-2 RTL block in lf2/styles.html lines 823-829 already declared at A.5 | mitigated · live walk PASS at 1440/880/480 |
| Frozen-sibling regression | high | selector-scoped Naskh override (`body.cs-lf-lf-2`) · 4 sibling LF classes do not match | mitigated · live walk PASS · Continua AR still Kufi |
| LF-2 distinctness drift across locales | high | layout/palette/imagery locale-neutral; voice anchor verbatim-in-translation; magazine grid + single-portrait shape preserved | mitigated · 5/5 axes × 5 locales = 25/25 |
| Italian normative ref translation drift | medium | Italian normative refs preserved Latin in every locale's body + footer | mitigated · audit clean |
| Pre-existing booking-flag test failure | low | pre-existing in v15 baseline · unrelated to Cornice · not gate-blocking per A.6 precedent | accepted · same failure |

## §5 · Verdict

**HOLD for workflow D.** The gate awaits user authorisation. Cornice
is review-ready in 5 locales at tier=draft. Server stays open at
`http://127.0.0.1:8052/` for the user-handshake walk.
