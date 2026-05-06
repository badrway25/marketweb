# Causa workflow C multilingual · scorecard summary

```yaml
report_type:        scorecard · single-panel summary for workflow C
                    multilingual rollout (companion to
                    factory/reports/causa/causa-workflowC-multilingual.md
                    + factory/reports/browser-verification/causa-workflowC-multilingual.md)
date:               2026-05-06
agent:              workflow-c-multilingual-rollout
status_tag:         WORKFLOW-C-GREEN-REVIEW-READY · WORKFLOW-D-GATED-ON-USER-HANDSHAKE
```

---

## §1 · 9-cell scorecard (mirroring slice-01 / slice-02 format)

| # | Cell | Target | Result | Verdict |
|---|---|---|---|---|
| 1 | **Test suite** | 546/546 OK · zero new failures | 546/546 OK · zero new failures · 169.146s | ✅ PASS |
| 2 | **Causa staff routes (5 pages × 5 locales)** | 25/25 · 200 OK | 25/25 · 200 OK · byte counts within ±1 KB across locales | ✅ PASS |
| 3 | **Causa case-detail staff (4 posts × 5 locales)** | 20/20 · 200 OK · CTA verb-class propagates | 20/20 · 200 OK · Sottometti / Submit / Soumettez / Someta / قَدِّم on every navbar pill | ✅ PASS |
| 4 | **Anonymous draft-gate** | Causa 404 anon · absent from public catalog · home counter stays 24+ | 5/5 PASS · Causa 404 on every probed route · public catalog excludes Causa · home counter "24+" preserved | ✅ PASS |
| 5 | **Frozen siblings** | 5/5 byte-equivalent on motion data-attrs · zero new patterns leaked | 5/5 200 anon · motion bundles UNCHANGED on Pragma / Cornice / Fiscus / Solaria / Continua · zero EVID-3 / TIME-3 / EVID-5 / NAV-1 / KPI-2 leakage | ✅ PASS |
| 6 | **Voice anchor verbatim recurrence** | 2-surface verbatim em-anchor in every locale · public-record-evidence cognate set | 5/5 locales · 2-surface verbatim · `evidenza/evidence/preuve/evidencia/دليل` · zero drift | ✅ PASS |
| 7 | **Voice anchor anti-collision** | Cornice cognate must NOT appear as em-target in any Causa locale | 5/5 locales · `argomento/argument/argomento/argumento/حُجَّة` ALL absent as em-target · zero leakage | ✅ PASS |
| 8 | **AR Naskh scoping (LF-2 only)** | Naskh swap fires on Causa AR (LF-2) and Cornice AR (LF-2); does NOT fire on Pragma/Fiscus/Solaria/Continua AR (non-LF-2) | 6/6 templates verified · `cs-lf-lf-2` body class only on Cornice + Causa AR · cluster-default Noto Kufi on the 4 non-LF-2 AR siblings | ✅ PASS |
| 9 | **Motion-profile bundle propagation** | All 5 Causa locales emit `g2-editorial-counter` + 5 patterns firing (KPI-2 + NAV-1 + EVID-5 + EVID-3 + TIME-3) | 5/5 locales identical body data-attrs · `data-motion-profile="g2-editorial-counter"` + 5 flags `=1` · zero variance | ✅ PASS |

**9 / 9 cells PASS.** Zero blocking failures. Zero regressions vs
slice-02 baseline.

---

## §2 · Anti-clone 2.0 score (post-workflow-C · preserved from slice-02)

| Score component | Pre-workflow-C (slice-02) | Post-workflow-C | Δ |
|---|---|---|---|
| Cornice ↔ Causa pair | 29/54 (or 30/54 with axis-18 promote) | **29/54 (or 30/54)** | 0 (locale-data-only slice · no axis-affecting source change) |
| AC-V1 sub-variant adoption | 5/9 | **5/9** in every locale | 0 |
| Critical-axis vetoes (5) | All PASS | All PASS in every locale | 0 |
| Within-family threshold (≥27/54) | Cleared with 2-3 pts margin | **Cleared with 2-3 pts margin in every locale** | 0 |

**Zero anti-clone regression.** Workflow C does not alter any axis
score; it propagates the slice-02 state across 4 additional locales
without introducing any locale-specific regression on the existing
axes.

---

## §3 · Critical-axis check post-workflow-C (5 locales)

| Axis | Floor | IT | EN | FR | ES | AR |
|---|---|---|---|---|---|---|
| 12 voice anchor (≥3) | 3 | ✓ | ✓ | ✓ | ✓ | ✓ |
| 13 CTA mental model (≥2) | 2 | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 hero subject (≥2) | 2 | ✓ | ✓ | ✓ | ✓ | ✓ |
| 18 motion + page choreography (≥2) | 2 | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17 imagery register (≥2) | 2 | ✓ | ✓ | ✓ | ✓ | ✓ |

**5 / 5 vetoes PASS in 5 / 5 locales.** Causa is anti-clone 2.0
COMPLIANT vs Cornice in every locale.

---

## §4 · User-brief do-NOT compliance (7 strict do-NOTs)

| User-brief do-NOT | Workflow C compliance |
|---|---|
| 1. NOT public-flip Causa | ✓ tier=draft preserved · public catalog count unchanged at 24 |
| 2. NOT redesign the layout | ✓ zero edits to LF-2 layout files / chrome / styles |
| 3. NOT widen into sibling 7 | ✓ no new template enrolled · cluster stays at 6 (5 live + Causa draft) |
| 4. NOT touch apps/editor / apps/projects / apps/commerce | ✓ zero edits in those directories |
| 5. NOT regress Cornice or the frozen live siblings | ✓ 5/5 frozen siblings byte-equivalent on motion data-attrs · zero changes to sibling content |
| 6. NOT silently flatten Causa into generic advisory tone | ✓ forensic-publication vocabulary density ≥40 hits/locale · litigation-evidence-led register preserved across 5 locales |
| 7. NOT alter motion_profile semantics except where locale/RTL requires | ✓ motion_profile = `g2-editorial-counter` identical across 5 locales · same 5 flags firing · CSS / JS unchanged · AR Naskh swap inherited verbatim from Cornice's Pass C chrome (no new chrome rule introduced) |

**7 / 7 user-brief do-NOTs respected.** Workflow C scope discipline
holds.

---

## §5 · Files touched (full diff manifest)

| file | nature | status |
|---|---|---|
| `apps/catalog/template_content_causa_en.py` | new EN locale tree (~1147 lines) | new |
| `apps/catalog/template_content_causa_fr.py` | new FR locale tree (~1238 lines) | new |
| `apps/catalog/template_content_causa_es.py` | new ES locale tree (~1244 lines) | new |
| `apps/catalog/template_content_causa_ar.py` | new AR locale tree (~1456 lines · LF-2-scoped Naskh inheritance) | new |
| `apps/catalog/template_content.py` | 4 new imports + locale dispatch map | modified (+14 / −3) |
| `TEMPLATE_REGISTRY.json` | locales array `["it"]` → `["it","en","fr","es","ar"]` + tier_reason narrative | modified (+5 / −1) |
| `factory/reports/causa/causa-workflowC-multilingual.md` | workflow C narrative | new |
| `factory/reports/browser-verification/causa-workflowC-multilingual.md` | live walk evidence | new |
| `factory/reports/scorecard/causa-workflowC-multilingual/summary.md` | this file | new |

**Zero edits** to: apps/editor / apps/projects / apps/commerce /
sibling content modules / sibling locale trees / LF-1 / LF-2 / LF-3 /
LF-4 / LF-5 layout files / corporate-suite chrome / live-motion.css /
live-motion.js / views.py / template_dna.py / preview_imagery.py /
migrations / standards / docs.

---

## §6 · Workflow D readiness · exact next step

Workflow C is **GREEN review-ready in 5 locales**. The user-handshake
gate is the only blocker between workflow C completion and workflow D
public flip.

**On user authorisation for workflow D:**
1. TEMPLATE_REGISTRY.json: flip `tier=draft` → `tier=published_live`
   on `causa-legale` row + extend `tier_reason` with the public-flip
   narrative.
2. `python manage.py sync_template_tiers` (single DB row update).
3. `apps/catalog/tests.py`: 7 explicit-literal test bumps (24 → 25 ·
   "24+" → "25+").
4. Walk re-verification: 25 anonymous routes 200 + 5 sibling homes
   200 byte-equivalent + AR-specific Naskh + locale switcher honesty.
5. Author `phase_x6_causa_workflow_c.md` + `phase_x6_causa_public_flip.md`
   memory + update MEMORY.md.

Catalog distribution moves 24 published_live / 1 draft → **25
published_live / 0 draft** at workflow D close.

**Until user-handshake lifts the hold, the slug stays `tier=draft`.**

---

## §7 · One-line verdict

**Causa workflow C multilingual rollout · 9/9 scorecard cells PASS ·
546/546 tests OK · 65/65 walk probes PASS · 7/7 user-brief do-NOTs
respected · workflow D ready for user-handshake hold lift.**
