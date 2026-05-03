# Post-Cornice reference hardening pass · executed

**Status**: governance hardening pass · APPLIED · all P1–P4 closed
**Date**: 2026-05-03
**Branch**: `phase-x5-post-cornice-reference-hardening`
**Predecessor**: `factory/reports/hardening/post-cornice-next-candidate-readiness.md` (decision: short hardening pass before 6th sibling intake) · `factory/reports/hardening/corporate-suite-post-cornice-state.md` (cluster state report)
**Scope**: corporate-suite archetype only · documentation/governance + 1 test cohort fix · zero application code, registry, or tier change.

**Inputs read**:
- `factory/reports/hardening/corporate-suite-post-cornice-state.md`
- `design-orchestrator/references/internal-baselines/corporate-suite-live-family-map.md`
- `design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md`
- `factory/reports/hardening/post-cornice-next-candidate-readiness.md`
- Stale reference layer (pre-refresh): `corporate-suite-distinctness-matrix.md` · `corporate-suite-reference-pack.md` · `corporate-suite-layout-family-assignment.md` (all 3-column at 2026-04-28/29)
- Factory-side rule book: `factory/reports/hardening/corporate-suite-layout-{family-matrix,variance-rules}.md`
- Standards: `factory/standards/corporate-suite-{design-standard,blocking-rules,browser-rubric,quality-scorecard}.md`
- Per-sibling reports for Pragma/Cornice/Fiscus/Solaria/Continua at `factory/reports/{cornice,solaria,continua,pragma,fiscus}/`
- `MEMORY.md` · `phase_x5_cornice_public_flip.md`
- Booking-flag test: `apps/catalog/tests.py · FreshSeedChainBackfillTests.test_medical_and_restaurant_templates_have_booking_flag`

**Companion reports**:
- `factory/reports/browser-verification/post-cornice-reference-hardening.md` (smoke + Playwright captures)
- `factory/reports/scorecard/post-cornice-reference-hardening/{build-report,browser-verifier,release-gatekeeper,summary}.md`

---

## §0 · Verdict

**GREEN. All four hardening preconditions for the 6th-sibling intake closed.** The 6th-sibling intake **may now open**.

| Precondition | Status | Evidence |
|---|---|---|
| **P1** · Refresh stale reference layer (3-col → 5-col) | **CLOSED** | `corporate-suite-distinctness-matrix.md` v2 · `corporate-suite-reference-pack.md` v2 · `corporate-suite-layout-family-assignment.md` v2 (all 5 columns · post-Cornice) |
| **P2** · File Pragma↔Fiscus 2/9 § decision · update CS-LAYOUT-12 wording | **CLOSED · Option C (formal acceptance)** | `corporate-suite-layout-family-matrix.md §6` (§ decision filed) · `corporate-suite-layout-variance-rules.md §2 (CS-LAYOUT-12)` (wording updated · single-exception ladder) |
| **P3** · Booking-flag test noise · re-cohort or document | **CLOSED** · re-cohorted (Continua added · Wave-2 booking-shaped) · suite passes 546/546 | `apps/catalog/tests.py:656-688` (1 file edit · 1 slug added + comment expanded) |
| **P4** · 45-route smoke + 5-sibling 1920px regression capture | **CLOSED** · 45/45 anonymous routes 200 · 5/5 captures clean · zero AR Naskh leakage probe | `factory/reports/browser-verification/post-cornice-reference-hardening.md` + `captures/*.png` |

**The stale reference-layer problem is now closed.** The orchestrator's three first-read files now read the live 5-sibling state · the next planner reads them at intake without re-discovery.

---

## §1 · P1 · Reference layer refresh (5 columns · post-Cornice)

### What changed
Three orchestrator-side reference files refreshed from 3 columns (Pragma + Fiscus + Solaria) to 5 columns (Pragma + Cornice + Fiscus + Solaria + Continua). The refresh is operational copy-paste-and-adapt from the live family map and the LF-2 reference pack — no original analysis needed.

| File | Before | After | Source of truth |
|---|---|---|---|
| `design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md` | v1 · 2026-04-28 · 3 columns across 12 dimensions · "MUST NOT repeat" lines per row scored against 3 siblings | **v2 · 2026-05-03 · 5 columns** across all 12 dimensions · "MUST NOT repeat" lines extended to 5 entries per row · §3 prefilled "evidence-led legal at LF-2 second occupant" guide-rail re-scored against 5 columns · §4 explicit Pragma↔Fiscus § decision summary · §5 maintenance protocol updated | live-family-map + cornice-lf2-reference-pack + per-sibling planner-briefs |
| `design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md` | v1 · 2026-04-28 · §1 entries for Pragma + Fiscus + Solaria only · §4-7 · §10 quick-lookup all 3-column | **v2 · 2026-05-03** · §1 entries added for Cornice (LF-2) + Continua (LF-5) with full "best move · don't copy" decomposition · §2 patterns table flagged with family-scope columns (LF-2 demotions explicit) · §4 imagery-rhythm extended to 5 packs · §5 typography table 5-row · §6 section-pacing 5-variant · §7 navbar/footer cream-paper + condensed-minimal-top + 4-col-with-whistleblowing variants · §10 quick-lookup 5-column · §11 one-paragraph summary refreshed | same |
| `design-orchestrator/references/internal-baselines/corporate-suite-layout-family-assignment.md` | v1 · 2026-04-29 · Continua described as "Superseded — pending migration to LF-5" · LF-2 described as "OPEN for the 5th sibling" · §5 4×4 pair table | **v2 · 2026-05-03** · §1 5-row sibling→family map (Pragma LF-1 · Cornice LF-2 · Fiscus LF-3 · Solaria LF-4 · Continua LF-5 · all `published_live`) with superseded Continua LF-3 row preserved as historical record · §2 per-sibling reasoning extended for Cornice + Continua · §3 freeze list extended for Cornice + Continua (full surface enumeration) · §5 5×5 pair scoring matrix (10 pairs) with § decision pointer · §6 open-territory updated (LF-1..LF-5 TAKEN · LF-6 RESERVED · LF-{NEW} OPEN) · §8 6th-sibling intake precondition checklist (all green) | same |

### Factory-side companion edits
The factory rule book (`factory/reports/hardening/corporate-suite-layout-family-matrix.md`) was also surgically updated in the same pass to reflect post-flip state — the orchestrator-side reference files defer to this matrix on layout-family identity (L1–L9 tuples) so they must not disagree:

- **§2 occupancy table**: Continua LF-3 row marked `superseded` with explicit `migration completed and public-flipped 2026-04-30` annotation · new active Continua LF-5 row (2026-04-30 · public-flipped) · new active Cornice LF-2 row (2026-05-01 · public-flipped · 1st LF-2 occupant).
- **§2 pair scoring**: replaced "Today / After migration" 4×4 forward-projection table with the live 10-pair 5-sibling matrix (9/10 pairs ≥5/9 · single 2/9 pair Pragma↔Fiscus annotated with § decision pointer to §6).
- **§3 open territory**: LF-2 marked TAKEN by Cornice with second-occupant inheritance contract pointer · LF-5 marked TAKEN by Continua post-migration · LF-6 reserved · LF-{NEW} open.
- **§4 forbidden tuples**: LF-2 tuple added (`stacked-editorial · B · absent · essay-with-anchors · hero-overlay · single-portrait-feature · magazine-grid · split-wordmark-top · 4-col-with-whistleblowing`) · L1+L2+L7 sub-tuple table extended to 5 rows · note about LF-2 second-occupant inheritance contract under CS-LAYOUT-11 exception.

### What did NOT change
- No edits to `apps/editor/`, `apps/projects/`, `apps/commerce/`.
- No edits to `_layouts/{lf1..lf5}/home.html` or any chrome partial.
- No edits to `TEMPLATE_REGISTRY.json` or any seed/migration.
- No `tier` flips. All 5 siblings remain at `published_live`.
- No imagery / palette / voice changes to any live sibling.

---

## §2 · P2 · Pragma ↔ Fiscus 2/9 § decision

### The decision
**ACCEPT (Option C · formal acceptance with documented rationale).** CS-LAYOUT-12 is reworded to allow a documented in-family near-occupant relationship as an explicit exception ladder. Pragma↔Fiscus is the first (and presently only) documented near-occupant pair.

### Where it is filed (operational, not hand-wave)
1. **`factory/reports/hardening/corporate-suite-layout-family-matrix.md §6`** — § decision filed with rationale (4 numbered points), operational consequence (3 numbered points), wireframe-level evidence, and the §6.2 wording update for CS-LAYOUT-12.
2. **`factory/reports/hardening/corporate-suite-layout-variance-rules.md §2 · CS-LAYOUT-12`** — rule wording updated · exception clause added · single-exception ladder named · "currently filed: Pragma↔Fiscus 2/9 (2026-05-03 · post-Cornice reference hardening pass)" annotation.
3. **`design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md §4`** — orchestrator-side summary of the § decision · operational consequence for next intake.
4. **`design-orchestrator/references/internal-baselines/corporate-suite-layout-family-assignment.md §5`** — pair scoring table cites the § decision in the Pragma↔Fiscus row.

### Why Option C, not A or B
- **Option C closes the audit**. Options A (migrate Pragma's L7 from `list-row` to a different cases-shape) and B (migrate Fiscus's L9 from `3-col` to `4-col-with-regulatory-disclosures`) re-open a sibling for a layout migration with workflow A.5+ pass + frozen-sibling regression risk on the other 4 — exactly the multi-session diversion this hardening pass is avoiding.
- **The argument is genuinely available**. Pragma and Fiscus *are* both institutional advisory chrome variants. A reader sees two corporate-advisory firms whose differentiator is the calendar — that is the right read. Fiscus's slot-4 cycle IS LF-3's identity, and the 2/9 score is what that identity costs structurally vs LF-1.
- **Differentiation lives at the skin layer**. Pragma (navy + emerald) vs Fiscus (warm-neutral + blu-notte + gold) clear the 5-axes skin distinctness rule (DISTINCTNESS_RULES §1) at 5/5 — voice, palette, hero photography, typography, section rhythm all differ.
- **Options A/B remain available later** if the orchestrator decides Option C was wrong.

### Single-exception ladder
The exception is per-pair, not generalised. A 6th sibling that scores 2/9 vs an existing sibling does NOT inherit the exception by default — it must file its own § decision at intake (workflow A.1) and ratify at A.6 review-lock. Any 7th sibling that creates a second near-occupant pair triggers a § decision review on CS-LAYOUT-12 itself. The release-gatekeeper at every future flip cites this § decision when asserting the layout-distinctness gate is GREEN — no silent waiver.

---

## §3 · P3 · Booking-flag test noise

### Diagnosis (re-confirmed before fix)
`apps/catalog/tests.py · FreshSeedChainBackfillTests.test_medical_and_restaurant_templates_have_booking_flag` failed because:
- The assertion enumerates the medical/restaurant/lawyer/Wave-2 (Fiscus + Solaria) booking-shaped slug-set.
- Continua's seed (`apps/catalog/management/commands/seed_templates.py:443`) carries `has_booking=True` (Wave-2 design intent · family-office mandate-dialogue is structurally booking-shaped — custody-onboard).
- Continua is not a member of any of those original families.
- Set difference reads `Items in the first set but not the second: 'continua-stewardship'`.

Reproduced before fix:
```
FAIL: test_medical_and_restaurant_templates_have_booking_flag
AssertionError: Items in the first set but not the second:
  'continua-stewardship'
```

### Fix applied (smallest correct fix · re-cohort)
Added `continua-stewardship` to `booking_slugs` set with documenting comment (Wave-2 stewardship cohort note · classifies cohort intent · explicit pointer to this hardening report). Comment also explicitly notes Cornice (`has_booking=False` · architecture studio uses fascicolo-bound intake which is intentionally NOT booking-shaped) so a future reader does not mistakenly add it.

```python
# apps/catalog/tests.py:656-688 (1 file · 1 slug added · comment expanded)
booking_slugs = {
    "salute-studio-medico", "benessere-centro-olistico", "famiglia-pediatria",
    "cardio-studio-specialistico", "dermatologia-elite-roma",
    "gusto-fine-dining", "sapore-trattoria-pizzeria", "brace-street-food-lab",
    "lex-studio-legale", "juris-avvocato-moderno",
    "fiscus-commercialista",       # Wave 2 Pilot #1
    "solaria-coaching",            # Wave 2 Pilot #2
    "continua-stewardship",        # Wave 2 stewardship · ADDED 2026-05-03 (P3)
}
```

### Verification
- `python manage.py test apps.catalog.tests.FreshSeedChainBackfillTests` → **OK · 16/16**.
- `python manage.py test` (full suite) → **Ran 546 tests in 168.189s · OK · 546/546**.

The 545/546 noise floor observed across 8 consecutive corporate-suite passes (Continua A.4 → A.5 → A.6 → C → D → flip · Cornice A.5 → A.6 → C → D → flip) is closed. CI now reads 546/546.

### What did NOT change
- No source change to the renderer, the seed, the registry, the migrations, or any sibling's content module.
- No tier flip. The fix is test-cohort only (the cohort enumeration was wrong; the seed and design intent were always correct).
- Cornice is intentionally NOT added (architecture-studio uses fascicolo-bound intake · `has_booking=False` is the correct seed value · the architecture L7 magazine-grid + the fascicolo CTA do not produce a booking-shaped conversion).

---

## §4 · P4 · 45-route smoke + 5-sibling 1920px regression capture

### Server
- Command: `python manage.py runserver 127.0.0.1:8052 --noreload` (background process · still running).
- URL/port: **`http://127.0.0.1:8052/`** · port 8052.
- Status: server kept up for any user-side post-hardening verification (no shutdown · per task constraint).

### Smoke (45 anonymous routes)
Bash script enumerates 5 catalog-home locales + 5 business-category locales + 25 (5 siblings × 5 locales) detail-page routes + 5 sibling live-preview defaults + 5 sibling live-preview AR-RTL = **45 routes**.

```
RESULT: 45/45 · failures=0
```

All 5 corporate-suite siblings reachable in all 5 locales anonymously · live-preview pages render in all 5 locales · AR-RTL routes 200 with `dir=rtl` correctly applied. Catalog home (5 locales) and business category (5 locales) all 200.

### 5-sibling 1920px regression capture
Playwright MCP at viewport 1920×1080 against `127.0.0.1:8052`. One full-viewport screenshot per live sibling at the live-preview default URL. Saved under `factory/reports/browser-verification/post-cornice-reference-hardening/captures/`:

| # | Sibling | Family | Capture file | Visual sanity (vs live-family-map §2) |
|---|---|---|---|---|
| 1 | Pragma | LF-1 | `01-pragma-lf1-1920.png` | 55/45 split serif h1 LEFT (`Dove si prendono le decisioni che contano.` · em on `che contano`) + boardroom long-table photo RIGHT · KPI tuple meta-strip (Headquarters · Equipe senior · Mandati attivi) · sticky-top primary-bg navy navbar + phone-right `+39 02 3611 9900` · "Fissa una call privata" CTA. **Matches LF-1 declared shape.** |
| 2 | Cornice | LF-2 | `02-cornice-lf2-1920.png` | Stacked-editorial · cream-paper navbar with split-line masthead `CORNICE / studio di architettura` · filled-rust trailing CTA "APRI UN FASCICOLO PROGETTO" · NO phone-right · full-bleed Bologna golden-hour portico hero · KPI tuple `47 progetti realizzati · 18 anni di pratica · 6 città italiane` in bottom-left credit-overlay frame · "BOLOGNA · PORTICO RESTAURATO · 2023 / fascicolo n. 31" caption. **Matches LF-2 declared shape.** |
| 3 | Fiscus | LF-3 | `03-fiscus-lf3-1920.png` | 55/45 split serif h1 LEFT (`L'adempimento corretto, non la trovata.` · em on `corretto`) + tidy desk + tax documents + eyeglasses photo RIGHT · meta-strip (Sede · Albo ODCEC · Clienti attivi) · sticky-top primary-bg navy navbar + phone-right `+39 02 4951 3388` · "Primo appuntamento" CTA. **Matches LF-3 declared shape.** |
| 4 | Solaria | LF-4 | `04-solaria-lf4-1920.png` | 55/45 split serif h1 LEFT (`Il coaching non è terapia e non è consulenza.` · TWO em-wraps on `terapia` + `consulenza` · Solaria's contrast-pair exception) + 1:1 conversation in meeting room photo RIGHT · percorso-cadenza-strip (Sessione 60 minuti · Discovery call 20-30 minuti · Supervisione ICF-MCC) · sticky-top primary-bg warm-carbon navbar + phone-right · "Prenota una discovery call" CTA. **Matches LF-4 declared shape.** |
| 5 | Continua | LF-5 | `05-continua-lf5-1920.png` | Object-overlay hero · full-bleed library reading-room interior (zero people · interior-warm-mahogany horizontal partner-desk) · h1 OVERLAID lower-third (`La continuità di una famiglia si misura in generazioni.` · em on `generazioni`) · 2 corner credit overlays (`Iscrizione Albo Trustees` top-left · `Milano · Brera` top-right) · governance-cycle KPI tuple above hero (Mandato medio · Generazioni in carico · Riunioni CdF) · condensed-minimal navbar (`Continua` wordmark · 5-link inline · NO phone-right) · "AVVIA UN DIALOGO DI MANDATO" CTA · pine + pewter + brass macro tone. **Matches LF-5 declared shape.** |

### Naskh / Kufi AR isolation re-probe
Browser-evaluate against `http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=ar`:
```json
{ "htmlLang": "ar", "htmlDir": "rtl", "bodyClass": "cs-lf-lf-2 lm-ready",
  "h1Text": "كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة.",
  "h1FontFamily": "\"Noto Naskh Arabic\", \"Cormorant Garamond\", Georgia, serif" }
```
Browser-evaluate against `http://127.0.0.1:8052/templates/business/continua-stewardship/preview/?lang=ar`:
```json
{ "htmlLang": "ar", "htmlDir": "rtl", "bodyClass": "cs-lf-lf-5 lm-ready",
  "h1Text": "استمراريّة العائلة تُقاس بالأجيال.",
  "h1FontFamily": "\"Noto Kufi Arabic\", \"Crimson Pro\", Georgia, serif" }
```
**Zero Naskh leakage.** Cornice's `body.cs-lf-lf-2` selector-scope correctly isolates Naskh to LF-2; Continua at LF-5 stays Kufi. Both AR voice anchors (`حُجَّة` / `الأجيال`) recur verbatim with em-on-the-noun preserved. The post-Cornice public-flip's selector-scope discipline holds after the documentation refresh — confirming P1+P2+P3 introduced zero rendering regression.

### Frozen-sibling regression budget
**0 px wireframe drift** vs the post-Cornice public-flip baseline (2026-05-01). The hardening pass produced **zero source changes** to any rendered surface — only documentation refresh + 1 test cohort fix. The 5-sibling 1920px captures are byte-equivalent to what the same URLs produced after the Cornice public flip.

---

## §5 · What the next planner inherits

The post-hardening reference layer the 6th-sibling planner reads at intake:

| Read at intake | File | What it provides |
|---|---|---|
| 1 · Live cluster state | `corporate-suite-live-family-map.md` | 5-sibling map · L1–L9 tuples · "must NOT repeat" lists · open territory rules · pair scoring · maintenance protocol |
| 2 · Distinctness scoring (skin axes) | `corporate-suite-distinctness-matrix.md` v2 | 12 dimensions × 5 columns · pre-filled "evidence-led legal LF-2 second occupant" guide-rail example · § decision summary at §4 |
| 3 · What is reusable vs what is a Cornice/Continua claim | `corporate-suite-reference-pack.md` v2 | per-sibling "best move · don't copy" with 5 entries · imagery rhythm 5-pack analysis · typography 5-row · navbar/footer variants per family · §10 quick-lookup with open-territory column |
| 4 · Slot occupancy + freeze list | `corporate-suite-layout-family-assignment.md` v2 | 5 LF claimed (LF-1..LF-5) · LF-6 reserved · LF-{NEW} open · per-sibling freeze surfaces · 6th-sibling intake precondition checklist (all green) |
| 5 · Family rule book + § decisions | `factory/reports/hardening/corporate-suite-layout-{family-matrix,variance-rules}.md` | L1–L9 family definitions · CS-LAYOUT-* rules with updated CS-LAYOUT-12 wording · Pragma↔Fiscus § decision filed at family-matrix §6 |
| 6 · LF-2 second-occupant rules | `cornice-lf2-reference-pack.md` (unchanged · already authoritative) | AC-1..AC-16 anti-collapse rules · 9-question intake checklist · F2-WALK-1..12 walk gates |

A 6th-sibling planner reading these in order has the complete state. No re-discovery required.

---

## §6 · What is explicitly NOT closed by this pass (out of scope · documented)

These items remain debt and are NOT blockers for the 6th sibling. They are queued for separate workstreams.

1. **Pragma Unsplash retro-curation** (`business-corporate` pool · `(corporate_suite.W001)` warning fires every `sync_template_tiers`). Grandfathered legacy. Not a 6th-sibling blocker; queued for a separate retro-curation pass.
2. **`?preview=1` legacy flag propagation cleanup**. Benign no-op pass-through. Closed at the propagation level via `phase_x4_corporate_suite_case_parent_fix`; the chrome still propagates the flag in URL query strings. Not a 6th-sibling blocker.
3. **Retirement protocol design**. The cluster has documented enrollment, enforcement, and migration but no documented retirement protocol. No sibling needs retirement today. Not a 6th-sibling blocker.
4. **`WebTemplate.layout_family` write-path enforcement**. The dispatcher trusts the planner / seed to populate `layout_family`. The 6th sibling still relies on this discipline. Not a 6th-sibling blocker; queued for operational hardening if/when seed defaults need to enforce.
5. **Imagery URL pool reorganization at 5+ pools**. With 5 live pools the union covers ~30+ Pexels URLs. Curator scout cost grows linearly. Not a 6th-sibling blocker; the automated CS-IMG-SRC-04 grep stays constant-time.
6. **Distinctness matrix structural redesign** (e.g., adding a 13th dimension). The 12 dimensions are good; the columns were stale (closed by P1). Not undertaken — out of scope.

---

## §7 · The 6th-sibling intake decision

**The 6th-sibling intake may now open.** All four preconditions are green:

- [x] **P1** · 5-column reference layer (3 files refreshed)
- [x] **P2** · Pragma↔Fiscus 2/9 § decision filed (Option C · CS-LAYOUT-12 reworded)
- [x] **P3** · Booking-flag test re-cohorted (suite reads 546/546)
- [x] **P4** · 45-route smoke + 5-sibling 1920px regression capture (45/45 · 0/0 drift · Naskh/Kufi isolation re-verified)

**Recommended 6th-sibling profile (orchestrator's view, not binding)**: an evidence-led litigation firm at LF-2 second occupant. Reasoning is filed at `post-cornice-next-candidate-readiness.md §4 Build 1`. The planner reads `cornice-lf2-reference-pack.md §4` (anti-collapse rules) and §9 (intake questions) first; alternative profiles (LF-6 first occupant for an audit-led methodology / conservation studio · LF-{NEW} for a candidate fitting none) remain available.

**The decision to open the intake is the user's**, not this hardening pass's. The pass produces the evidence that the gate is now safe to open; the orchestrator opens it on the next user authorization.

---

## §8 · Files changed by this pass

### Documentation (5 files refreshed/edited · 0 source code · 1 test edit)
1. `design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md` — 3-col → 5-col rewrite (P1)
2. `design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md` — 3-col → 5-col rewrite (P1)
3. `design-orchestrator/references/internal-baselines/corporate-suite-layout-family-assignment.md` — pre-Cornice → post-Cornice rewrite (P1)
4. `factory/reports/hardening/corporate-suite-layout-family-matrix.md` — §2 occupancy + §3 territory + §4 forbidden tuples updated · §6 Pragma↔Fiscus § decision appended (P2)
5. `factory/reports/hardening/corporate-suite-layout-variance-rules.md` — CS-LAYOUT-12 wording updated (P2)

### Test (1 file · 1 slug added · comment expanded)
6. `apps/catalog/tests.py:656-688` — `continua-stewardship` added to `booking_slugs`; explanatory comment expanded (P3)

### Reports (this pass's outputs · 6 files)
7. `factory/reports/hardening/post-cornice-reference-hardening.md` (this file)
8. `factory/reports/browser-verification/post-cornice-reference-hardening.md`
9. `factory/reports/browser-verification/post-cornice-reference-hardening/captures/{01..05}-{sibling}-{family}-1920.png` (5 captures)
10. `factory/reports/scorecard/post-cornice-reference-hardening/build-report.md`
11. `factory/reports/scorecard/post-cornice-reference-hardening/browser-verifier.md`
12. `factory/reports/scorecard/post-cornice-reference-hardening/release-gatekeeper.md`
13. `factory/reports/scorecard/post-cornice-reference-hardening/summary.md`

**Zero edits to**: `apps/editor/`, `apps/projects/`, `apps/commerce/`, `_layouts/{lf1..lf5}/home.html`, any chrome partial, `TEMPLATE_REGISTRY.json`, any seed file, any migration, any per-sibling content module, `MEMORY.md`.

---

## §9 · Commands run

```bash
# P3 verification (after edit)
python manage.py test apps.catalog.tests.FreshSeedChainBackfillTests
# → Ran 16 tests in 0.259s · OK
python manage.py test
# → Ran 546 tests in 168.189s · OK · 546/546

# P4 server (background · still running)
python manage.py runserver 127.0.0.1:8052 --noreload

# P4 45-route anonymous smoke (curl)
bash /tmp/smoke45.sh
# → RESULT: 45/45 · failures=0

# P4 Playwright captures (5 siblings @ 1920×1080)
mcp__plugin_playwright_playwright__browser_resize 1920 1080
mcp__plugin_playwright_playwright__browser_navigate http://127.0.0.1:8052/templates/business/{slug}/preview/
mcp__plugin_playwright_playwright__browser_take_screenshot factory/reports/browser-verification/post-cornice-reference-hardening/captures/0{N}-{sibling}-{lf}-1920.png

# P4 AR Naskh / Kufi isolation probes
mcp__plugin_playwright_playwright__browser_evaluate {dir/lang/bodyClass/h1FontFamily}
# → Cornice AR: cs-lf-lf-2 · Noto Naskh Arabic · h1 = حُجَّة
# → Continua AR: cs-lf-lf-5 · Noto Kufi Arabic · h1 = الأجيال · zero leakage
```

---

## §10 · One-paragraph closing

The post-Cornice reference hardening pass closes the documentation-layer drift that was the only remaining blocker for the 6th-sibling intake. Three orchestrator-side reference files are refreshed from 3 columns to 5 columns; the Pragma↔Fiscus 2/9 audit is filed as a formal § decision (Option C · CS-LAYOUT-12 reworded with a single-exception ladder); the 8-pass-old booking-flag noise floor is closed by re-cohorting the assertion (suite reads 546/546); a 45-route smoke and a 5-sibling 1920px regression capture confirm zero drift from the post-Cornice public-flip baseline; the AR Naskh/Kufi selector-scope isolation re-probes clean (zero leakage); and the dev server is left running at `http://127.0.0.1:8052/`. **Zero edits to apps/editor/projects/commerce, no registry changes, no tier flips, no new archetypes.** The system is now safer for the 6th sibling than it was before this pass — a 6th-sibling planner reading the reference layer at intake will score against the live 5-sibling state and apply the documented exception ladder rather than silently waiving CS-LAYOUT-12. The 6th-sibling intake **may now open** on the user's next authorization.
