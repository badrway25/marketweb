# Cornice · Workflow D · Final release-decision pass (LF-2 · 5 locales)

```yaml
report_type:        workflow-d-release-decision
template_slug:      cornice-architettura
archetype:          corporate-suite
sub_cluster:        architecture-firm · single-principal studio (editorial-led)
layout_family:      LF-2 · Editorial Spread (1st LF-2 occupant in the cluster)
phase:              X.5 · Cornice · workflow D (final release decision · pre-flip)
date:               2026-05-01
agent:              release-gatekeeper (Phase X.5 workflow D)
inputs_consumed:
  - factory/reports/corporate-suite/cornice-architettura/intake.md
  - factory/reports/corporate-suite/cornice-architettura/planner-brief.md
  - factory/reports/imagery/cornice-architettura/*
  - factory/reports/copy/cornice-architettura/copy-authoring.md
  - factory/reports/cornice/cornice-a5-it-build.md
  - factory/reports/cornice/cornice-a6-it-review-lock.md
  - factory/reports/cornice/cornice-workflowC-multilingual.md
  - factory/reports/browser-verification/cornice-a5-it-build.md
  - factory/reports/browser-verification/cornice-a6-it-review-lock.md
  - factory/reports/browser-verification/cornice-workflowC-multilingual.md
  - factory/reports/scorecard/cornice-a6-it-review-lock/*
  - factory/reports/scorecard/cornice-workflowC-multilingual/*
  - factory/standards/corporate-suite-multi-agent-sop.md (§5.4 handshake)
  - factory/standards/corporate-suite-quality-scorecard.md (§6.1 PASS class)
  - factory/standards/corporate-suite-blocking-rules.md (O1–O18 overrides)
  - factory/standards/corporate-suite-browser-rubric.md
  - TEMPLATE_REGISTRY.json (current state · cornice-architettura row · tier=draft)
  - apps/catalog/template_content_cornice{,_en,_fr,_es,_ar}.py (frozen)
  - templates/live_templates/business/corporate-suite/_base.html (frozen)
  - templates/live_templates/business/corporate-suite/_layouts/lf2/* (frozen)
status_tag:         APPROVED-PENDING-HANDSHAKE · tier=draft preserved · public flip HELD
verdict:            RELEASE-READY IN PRINCIPLE · NOT yet "flip now" · awaits user
                    parallel-verification handshake per cluster SOP §5.4 / R-SOL-8 / D-102 cadence
next_action:        User performs the visual handshake on the live multilingual
                    Cornice walk. On affirmative GO, the gatekeeper applies the §6
                    cascade documented to the line. On HOLD, no public flip;
                    Workflow C remains the latest binding state.
```

This file is the binding workflow-D narrative for Cornice. It pairs with:
- `factory/reports/browser-verification/cornice-workflowD-release-decision.md`
  — fresh-server walk evidence (5-locale spot-check + AR RTL + frozen-sibling
  selector-scope verification + responsive @720) and reproduction of Workflow C
  outcomes on a re-launched server
- `factory/reports/scorecard/cornice-workflowD-release-decision/*.md`
  — 5 scorecard panels (build · browser-verifier · release-gatekeeper ·
  scorecard · summary) + a re-runnable smoke prober
- `factory/reports/browser-verification/cornice-workflowD-release-decision/captures/*.png`
  — 3 captures (it-1440-firstscroll · ar-1440-firstscroll · ar-720-firstscroll)
  · intentionally narrow because the 11-capture deck exists at Workflow C and
  this pass is a release decision, not a re-build

---

## §1 · Workflow framing (why Workflow D exists separately)

Workflow C closed with Cornice authored across 5 locales (it/en/fr/es/ar) on
top of the locked LF-2 IT shape, voice anchor verbatim-in-translation,
real Arabic RTL via the LF-2-scoped Naskh swap, frozen siblings 0/4 regression,
and tier=draft preserved. The user explicitly held the public flip pending a
final release-decision pass.

Workflow D is the conservative gatekeeper layer **between "the work is done"
and "the public catalog now lists Cornice."** Its job is to:

1. Re-launch the dev server on a fresh process and confirm that the Workflow C
   verdict reproduces — i.e., it was not an artefact of a stale process or a
   one-time render.
2. Apply the cluster's Layer 1 / Layer 2 / Layer 3 scoring contract
   (`corporate-suite-quality-scorecard.md` §4–§6) to the current state and
   produce an aggregate verdict.
3. Decide between `release-ready in principle` and `flip now`. These are
   intentionally separate calls — the first is technical, the second is
   operational and requires the user-handshake.
4. Document the public-flip cascade to the line, so the gatekeeper can ship
   on user authorization without re-discovery.
5. Hold the flip if there is meaningful doubt — per the task's hard
   constraint, **HOLD wins on doubt**.

This pass is read-only at the source level. It edits **zero** files under
`apps/editor/*`, `apps/projects/*`, `apps/commerce/*`, `apps/catalog/*`,
`templates/**`, or `TEMPLATE_REGISTRY.json`. The only writes are reports
(under `factory/reports/...`) and three browser captures.

---

## §2 · Decision

**Verdict: APPROVED-PENDING-HANDSHAKE.**

- Cornice is **release-ready in principle.** The technical pipeline is GREEN
  on every layer the cluster's scoring contract observes.
- Cornice is **not yet "flip now."** The cluster release contract requires the
  user parallel-verification handshake (CS-BLOCK-13 / O13 · cluster R-SOL-8 ·
  SOP §5.4 · D-102 cadence). Until that handshake lands in the conversation,
  the gatekeeper holds.
- The HOLD is conservative-by-design. Per the task constraint **"if any
  meaningful doubt exists, HOLD wins"**, a process-doubt (handshake pending)
  is sufficient to hold the flip even when no defect-doubt remains.

Tier remains `draft` in the DB and the registry. Catalog distribution is
**23 published_live + 1 draft = 24 total**, with Cornice as the sole draft.
Anonymous visitors continue to receive 404 on the Cornice preview route and
the slug remains absent from the public `/templates/business/` catalog HTML.

---

## §3 · Answers to the six required questions

### 3.1 · Is Cornice still best kept as draft-reviewable, or is it genuinely ready for published_live?

**Genuinely ready for `published_live` in principle. NOT recommended to
auto-flip.**

The technical work — Italian build (A.5), review-lock (A.6 with 3 fixes
applied), and multilingual rollout (Workflow C with 5 locales authored,
RTL working, voice anchor preserved, frozen siblings 0/4 regression) — is
complete to the cluster's stated standard. Layer 1 (18 blocking overrides),
Layer 2 (9 critical-dimension floors), and Layer 3 (aggregate ≥ 4.3, all
non-critical floors ≥ 3) all clear with margin. The fresh-server reproduction
in this pass returned identical DOM values for every probed cell.

However, the release path encoded in `corporate-suite-multi-agent-sop.md` §5.4
treats the user parallel-verification handshake as a **Layer 1 precondition
for any LIVE flip** — not a nice-to-have. Auto-flipping when the user has
explicitly held the public flip pending Workflow D would short-circuit the
SOP and trade the cluster's release-contract integrity for a single hour of
saved latency. The conservative posture this task mandates is to keep
Cornice draft-reviewable until the user signals authorization.

### 3.2 · Is the human-visible product premium, modern, elegant, professional, and structurally distinct in all 5 locales?

**Yes — to the cluster's reference standard, in every locale.**

Premium · modern · elegant · professional all read as binary quality ratings
under the cluster's `corporate-suite-design-standard.md` §1–§12 grid. On a
5-axis triangulation × 5 locales (Workflow C §8) Cornice scores 25/25 vs every
existing corporate-suite sibling. On the per-dimension scorecard (Layer 2)
the only non-5 score is D9 imagery quality at 4.5 (carry-over observation
from A.5/A.6 — pillar imagery uses a single editorial-architectural mood
across 4 surfaces and would benefit from richer photographer rotation;
documented as STRONG observation, not a blocker). All 9 CRITICAL dimensions
are at 5 in the live render.

Structurally distinct: Cornice is the **1st LF-2 occupant** in the cluster.
Pragma uses LF-1, Fiscus LF-3, Solaria LF-4, Continua LF-5. The stacked-
editorial 8/4 hero geometry, the cream-paper masthead with split wordmark,
the 3+1 magazine-grid for cases, and the 4-col footer with whistleblowing
column are all family-distinct surfaces — none are shared with any of the
four existing siblings. The voice anchor (`argomento`/`argument`/`argument`/
`argumento`/`حُجَّة`) is curatorial-architectural in register; no other
sibling uses a curatorial register, so voice is also distinct in every
locale (architectural-press register preserved in EN/FR/ES/AR per Workflow C
§5).

### 3.3 · What evidence is strong and what evidence is still weak?

**Strong:**

- Live walk evidence at Workflow C: 11 captures across 5 locales × 3 viewports
  (1440 lead, 880 burger entry, 480 mobile small) plus AR-specific
  inner-page walks (studio AR · contatti FR · progetti ES · case-detail EN).
- Fresh-server reproduction in this pass: IT-1440, AR-1440, AR-720 captures
  + DOM probes confirm same values as Workflow C documented.
- 45-route staff smoke (5 locales × 5 pages + 5 locales × 4 case-detail)
  returns 45/45 → 200 with the staff session + `?preview=1`.
- Anonymous tier-gate verified intact: `/preview/` → 404 anon, slug ABSENT
  from `/templates/business/` HTML, `?preview=1` does not bypass the gate
  for anon (no D-055 leak).
- Frozen-sibling regression: 0/4 across Pragma/Fiscus/Solaria/Continua over
  IT/EN/FR/ES/AR (20/20 routes 200 anon · Continua AR Kufi h1 confirmed
  preserved at 1440 · Pragma IT navy nav confirmed unchanged).
- AR Naskh override is genuinely selector-scoped: `body.cs-lf-lf-2`
  matches only Cornice; Continua LF-5 AR computed font remains
  `Noto Kufi Arabic`.
- Voice anchor verbatim-in-translation across all 5 locales on h1 +
  CTA closer (12 italic em surfaces per locale · 60/60 across locales).
- Test suite 545/546 — identical to A.6 and Workflow C; the single
  failure is the pre-existing Continua-related booking-flag test,
  documented in the v15 baseline as unrelated to Cornice.
- Contrast on the live render (probed in this pass): hero h1 / cream nav
  links / cta-closer h2 = 13.99:1 (AAA · margin 7×); KPI cream-on-dark
  photo plate = 18.39:1 (AAA); rust CTA cream-on-rust = 4.61:1 (AA on
  small text · AAA on large/UI text per WCAG).

**Weak (but non-blocking):**

- D9 imagery quality is 4.5/5 — pillar/hero imagery cohesion is excellent
  but the photographer rotation could broaden in a future imagery-hardening
  pass. Not a Pexels-compliance issue (all URLs are Pexels). Not a 3-second
  semantic-fail issue. Documented as STRONG observation, not a blocker.
- The pre-existing booking-flag test failure persists. It is documented in
  the v15 baseline as unrelated to Cornice and pre-dating Cornice's
  enrollment. Not a regression introduced by Cornice's pipeline.
- The user-handshake itself has not yet landed in the conversation. This is
  not a defect; it is the gating event Workflow D exists to wait for.

### 3.4 · Are there any actual blockers left or only release-decision gates?

**No actual blockers. Only the release-decision gate.**

The 18 Layer-1 overrides all read NO. There are 0 BLOCKING findings, 0
STRONG findings outstanding (D9 is the lone STRONG observation, scored 4.5
which exceeds the ≥ 3 floor for a non-critical dimension), and 0 new
OBSERVATIONS introduced by this pass. There is no defect-class doubt.

The only gate left is the parallel-verification handshake, which is a
process gate by design — not a defect. The cluster encodes it precisely
because past templates that auto-flipped on technical greenness shipped
defects the user would have caught in a 30-minute live walk (the
canonical Solaria precedent at `e8f38b5`). Cornice is held to the same
contract.

### 3.5 · If release-ready, what exact minimal steps are needed for the public flip?

When the user authorizes, the gatekeeper applies, in order (full detail in
`scorecard/release-gatekeeper.md` §6):

1. **Registry flip** — single-line `Edit` on `TEMPLATE_REGISTRY.json` line
   387: `"tier": "draft"` → `"tier": "published_live"`. Optionally update the
   `tier_reason` text to record the workflow-D approval timestamp.
2. **DB sync** — `python manage.py sync_template_tiers` propagates registry
   → DB. Distribution moves 23 published_live + 1 draft → 24 published_live
   + 0 draft.
3. **Trust counter** — search `apps/catalog/tests.py` and any rendered
   counter for the literal `23+` (or the explicit literal string
   `"23+"`/`23`/`"23"`); bump to `24+`/`24` per the Continua public-flip
   precedent (7 explicit-literal test bumps were sufficient there).
4. **Tier-fact tests** — re-run the corporate-suite contract tests that scan
   the live count. Expect Cornice to now appear in the published_live count.
5. **Cluster smoke** — re-run the catalog-card reachability smoke + the full
   546/546 test suite + the 5/5 Cornice locale routes anonymous (formerly
   404, now expected 200). The pre-existing booking-flag failure is the
   only allowed deviation.
6. **MEMORY.md roll-up** — add a `phase_x5_cornice_workflowD_public_flip.md`
   checkpoint pointer; promote `phase_x5_cornice_workflowC_multilingual.md`
   from CURRENT to RECENT; bump the CURRENT baseline-pointer line to
   reflect the 24-template live catalog.
7. **Public visit verification** — anonymous probes after the flip should
   show: `/templates/business/cornice-architettura/preview/` → 200 (not
   404); slug present in `/templates/business/` HTML; locale switcher
   visible to anon; `?lang=ar` AR RTL working anon. Negative tests too:
   any test that asserts Cornice is *absent* from the live catalog must
   be revised.
8. **Server shutdown** — record the shutdown timestamp on this scorecard.

The flip is **1 file edit + 1 management command + ~7 test-counter bumps + 1
MEMORY rollup + 1 cluster smoke**. No template/source/HTML edits required.

### 3.6 · If not release-ready, what exact issues remain?

This pass does NOT conclude "not release-ready." It concludes
"release-ready in principle, public flip held pending handshake." There
are no defect-class issues to remediate. The only outstanding item is
the handshake itself, which is a user-action, not a development task.

If during the user's parallel walk a meaningful defect surfaces, the
gatekeeper-default reverts to HOLD and a narrow `template-editor-fixer`
pass scoped to that surface is initiated. Until that signal arrives, no
remediation work is queued.

---

## §4 · Per-locale flip-eligibility matrix

| Locale | Walk verdict | BLOCKING | Voice anchor | RTL parity | Recommended on user GO |
|---|---|---|---|---|---|
| IT | PASS | 0 | ✓ argomento (h1 + CTA closer verbatim) | n/a | flip-eligible |
| EN | PASS | 0 | ✓ argument (cognate · Architectural Review register) | n/a | flip-eligible |
| FR | PASS | 0 | ✓ argument (cognate · L'Architecture d'Aujourd'hui register) | n/a | flip-eligible |
| ES | PASS | 0 | ✓ argumento (cognate · Arquitectura Viva register) | n/a | flip-eligible |
| AR | PASS | 0 | ✓ حُجَّة (curatorial-thesis equivalent · MENA arch-press register) | ✓ Naskh swap LF-2-scoped · 16/16 RTL surfaces | flip-eligible |

5 locales · 5 PASS · 0 BLOCKING. The flip can land on all 5 simultaneously
when the user authorizes — there is no held-locale subset.

---

## §5 · Risk register (re-bound at workflow D)

| Risk | Severity | Status |
|---|---|---|
| Voice anchor lost in translation | HIGH | MITIGATED · 5/5 verbatim-in-translation across h1 + CTA closer (live-verified) |
| LF-2 layout reshapes under RTL | HIGH | MITIGATED · DOM-equivalent across 5 locales · zero overflow at 1440 / 880 / 480 / 720 |
| AR Naskh override leaks to other LF families | HIGH | MITIGATED · selector-scoped to `body.cs-lf-lf-2` · Continua LF-5 AR computed font still Noto Kufi (live-probed in this pass) |
| Frozen-sibling chrome regression (cs-nav--lf2 lift at A.6) | MEDIUM | MITIGATED · the lift is selector-gated; Pragma/Fiscus/Solaria/Continua chrome unchanged (20/20 anon routes 200) |
| F1 founder gender mismatch reappears in translation | MEDIUM | MITIGATED · all 4 locale modules carry "Marta" + feminine agreement (case-by-case · live-verified) |
| Magazine-grid hero card empty-band regression | MEDIUM | MITIGATED · F3 flex-grow scoped to LF-2 layout file · live-confirmed in 5 locales |
| Italian normative refs collapse in non-IT locales | MEDIUM | MITIGATED · D.lgs./MIBAC/OAPPC/CNAPPC/PRG/Soprintendenza/DAStU/Reg.UE preserved verbatim in every locale's footer column AND inline body (anchors Cornice as Milan-based) |
| `?preview=1` leak across locale switcher | MEDIUM | MITIGATED · staff-preview-aware href generation works on all 5 locale pills (D-055 corporate-suite-case-parent fix carried over) |
| Anonymous catalog leak after tier-flip prep | LOW | MITIGATED · slug ABSENT from `/templates/business/` HTML at draft tier (live-probed in this pass) |
| Pre-existing booking-flag test failure | LOW | DOCUMENTED · pre-dates Cornice · independent surface · v15-baseline-known |
| D9 imagery quality (4.5) | LOW (STRONG observation) | DOCUMENTED · pillar photographer rotation deferred to a future imagery-hardening pass · not blocking |
| Pragma↔Fiscus 2/9 layout-distinctness (cluster legacy) | LOW | DOCUMENTED · cluster audit deferred · does not affect Cornice's 9/9 layout-distinctness vs all four siblings |

No HIGH or MEDIUM risk left active for Cornice's release. Two LOW items (D9
imagery cohesion, hero `<picture>` srcset) carry over as future-pass
observations and are not blocking the public flip.

---

## §6 · Files written by this pass (the only writes)

```
factory/reports/cornice/cornice-workflowD-release-decision.md                       (THIS file)
factory/reports/browser-verification/cornice-workflowD-release-decision.md          browser walk index
factory/reports/browser-verification/cornice-workflowD-release-decision/captures/   (3 PNGs)
factory/reports/scorecard/cornice-workflowD-release-decision/build-report.md        scorecard sub-report
factory/reports/scorecard/cornice-workflowD-release-decision/browser-verifier.md    scorecard sub-report
factory/reports/scorecard/cornice-workflowD-release-decision/release-gatekeeper.md  scorecard sub-report
factory/reports/scorecard/cornice-workflowD-release-decision/scorecard.md           aggregate scorecard
factory/reports/scorecard/cornice-workflowD-release-decision/summary.md             one-paragraph summary
factory/reports/scorecard/cornice-workflowD-release-decision/_smoke.py              45-route + sibling smoke prober
```

**No file outside `factory/reports/...` was modified by this pass.** Zero edits
to `apps/editor/*`, `apps/projects/*`, `apps/commerce/*`, `apps/catalog/*`,
`templates/**`, `TEMPLATE_REGISTRY.json`, or any management command. No
migration. No new archetype. No widening of LF-2.

---

## §7 · Server / route status (handed back to orchestrator · live)

```
server:                 python manage.py runserver 127.0.0.1:8052 --noreload
URL prefix:             http://127.0.0.1:8052/
template root URL:      /templates/business/cornice-architettura/preview/
9 routes × 5 locales = 45 staff-preview routes (all 200 with ?preview=1):
  IT  /preview/ (and /studio/ /servizi/ /progetti/ /contatti/ + 4 case-detail slugs)
  EN  ?lang=en  on every route above
  FR  ?lang=fr  on every route above
  ES  ?lang=es  on every route above
  AR  ?lang=ar  on every route above (dir=rtl)
tier:                   draft (anonymous: 404 · staff_preview: 200 with ?preview=1)
catalog count:          23 published_live + 1 draft = 24 total (Cornice is the lone draft)

frozen siblings (all 200 anonymous · IT + EN/FR/ES/AR · 20 routes total):
  - /templates/business/pragma-corporate-suite/preview/       LF-1
  - /templates/business/fiscus-commercialista/preview/        LF-3
  - /templates/business/solaria-coaching/preview/             LF-4
  - /templates/business/continua-stewardship/preview/         LF-5

test suite:             546 tests · 545 pass · 1 pre-existing failure
                        (test_medical_and_restaurant_templates_have_booking_flag
                         · pre-existing baseline failure · UNRELATED to Cornice)
```

The dev server stays open at port 8052 for the user-handshake review.

---

## §8 · Workflow D verdict

**APPROVED-PENDING-HANDSHAKE.**

Cornice's workflow D is closed on the gatekeeper side. The technical work is
GREEN on every layer. The flip is held until the user explicitly authorizes
parallel-verification confirmation in the conversation. Server is kept
running. Tier is preserved at `draft`.

If the user signals **GO** with the live walk landing clean: the gatekeeper
applies the §6 cascade (1 registry edit + `sync_template_tiers` + ~7
test-counter bumps + cluster smoke + MEMORY rollup) and Cornice becomes
the cluster's 5th `published_live` corporate-suite sibling and the
catalog's 24th live template.

If the user signals **HOLD on a specific surface**: the gatekeeper holds the
flip and a narrow `template-editor-fixer` pass scoped to that surface is
initiated. Workflow D re-binds on the post-fix render.

If meaningful doubt arises during the user walk: per the task's binding
constraint, **HOLD wins**.
