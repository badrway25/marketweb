# Release-gatekeeper · Cornice Workflow D Release Decision · 2026-05-01

**Verdict**: HOLD public flip · `tier=draft` preserved · `release-ready in principle`, **not** `flip now`
**Aggregate**: 4.97 / 5 · 0 BLOCKING · 0 STRONG outstanding · 0 OBSERVATION new
**Branch**: `phase-x5-cornice-workflowD-release-decision`
**Run timestamp**: 2026-05-01
**Status tag**: APPROVED-PENDING-HANDSHAKE

---

## 1 · Decision

**HOLD public flip.** Tier remains `draft` in DB and registry.

The technical work is complete. Layer 1 (overrides), Layer 2 (critical
floors), and Layer 3 (aggregate) all clear with margin. The cluster's
release contract requires one additional element that the technical
pipeline cannot provide: the user parallel-verification handshake
(CS-BLOCK-13 / O13 · cluster R-SOL-8 · SOP §5.4 · D-102 cadence).
Until that handshake lands in the conversation, the gatekeeper holds.

This is the conservative reading of the task constraint **"if any
meaningful doubt exists, HOLD wins"** — the doubt here is not a defect
doubt; it is a process doubt. The cluster-wide rule that the user must
walk the live preview themselves before LIVE flip is the entire point
of the corporate-suite SOP §5.4 handshake; auto-flipping on technical
greenness would short-circuit it.

---

## 2 · Layer 1 · Blocking-override review

| # | Override | Triggered? | Source agent | Evidence |
|---|---|---|---|---|
| O1  | h1..h5 distance < 120 OR WCAG < 4.5 | NO | contrast | walk §4 · h1 / nav-link / cta-closer 13.99:1 · KPI 18.39:1 · all AAA |
| O2  | Horizontal scrollbar at any viewport | NO | responsive | walk §3.1 (1440 1425=1425) + §3.2 (AR 1440 1425=1425) + §3.3 (AR 720 705=705) |
| O3  | Hero / nav fail to stack at ≤ 720 | NO | responsive | live capture ar-720-firstscroll.png + Workflow C 480/880 captures |
| O4  | Imagery URL 404 on live | NO | imagery | 45/45 staff routes 200 (every imagery surface fetched) |
| O5  | Imagery 3-second semantic fail | NO | imagery | A.5 §6 + Workflow C captures · Bologna golden-hour portico reads architectural at 3s |
| O6  | Imagery mood vs voice anchor | NO | imagery | A.5 §6 (architectural-editorial-built-form mood matches curatorial voice) |
| O7  | Non-Pexels URL on a new pilot | NO | imagery | A.5 / A.6 / Workflow C all confirmed Pexels-only · zero non-Pexels |
| O8  | Editor affordance on `/preview/` | NO | style-critic | bodyClass `cs-lf-lf-2 lm-ready` only |
| O9  | Lorem ipsum / placeholders | NO | style-critic / copy | Workflow C `style-critic.md` · 5 locales authored |
| O10 | Fake certifications | NO | copy-live | OAPPC · CNAPPC · MIBAC · Soprintendenza · D.lgs. 24/2023 · D.lgs. 42/2004 (real Italian normative refs) |
| O11 | Voice anchor missing in any locale | NO | copy-live | walk §3 · 5/5 locales verbatim-in-translation on h1 + CTA closer (12 italic em / locale) |
| O12 | D-054 10-gate triangulation absent | NO | copy-live | A.6 §5 + Workflow C §8 · 5/5 axes vs Pragma+Fiscus+Solaria+Continua |
| O13 | Walk URL + port not recorded | **half-met** | gatekeeper | URL recorded (`http://127.0.0.1:8052/`) · **user confirmation pending** |
| O14 | Walk missing any rubric viewport | NO | browser-verifier | Workflow C 1440/1100/880/480 + this pass 1440 + 720 (AR-RTL) = 5 viewport coverage |
| O15 | Evidence directory incomplete | NO | browser-verifier | 11 captures (Workflow C) + 3 captures (this pass) + 8 scorecard panels (Workflow C) + 5 scorecard panels (this pass) |
| O16 | Nav polarity broken / >1 accent | NO | style-critic | cream paper masthead with single rust accent (CTA pill) · single underline accent on active nav link · live-confirmed §3.1 |
| O17 | Dark-on-dark in `.dark` sections | NO | contrast | walk §4 (KPI 18.39:1 on dark photo · CTA closer 13.99:1) |
| O18 | No live walk | NO | browser-verifier | This pass performed a live walk · 5 locales (probed via DOM + smoke) · 1440 + 720 |

**0 / 18 overrides triggered.** O13's "URL recorded" half is met; the
"user confirmation" half is the handshake described above and is the
reason the gatekeeper holds.

## 3 · Layer 2 · Critical-dimension floor review

| D# | Dim | CRITICAL? | Score | Floor | Met? | Source |
|---|---|---|---|---|---|---|
| D1  | Premium feel | ✓ | 5 | ≥ 4 | YES | Workflow C `style-critic.md` + this pass §3.2 (architectural editorial register · cream-paper masthead distinct from any other sibling) |
| D2  | Elegance | ✓ | 5 | ≥ 4 | YES | Workflow C `style-critic.md` (12 italic em / locale · curatorial register) |
| D3  | Modern professionalism | ✓ | 5 | ≥ 4 | YES | Workflow C `style-critic.md` (5/5 locale register guides verified) |
| D4  | Hero readability | ✓ | 5 | ≥ 4 | YES | walk §4 (h1 13.99:1 · KPI 18.39:1 AAA) |
| D5  | Navbar quality | — | 5 | ≥ 3 | YES | walk §3.1, §3.4 (cs-nav cs-nav--lf2 · cream-paper · split-wordmark · F2 lift to _base.html holds across inner pages) |
| D6  | Footer quality | — | 5 | ≥ 3 | YES | A.6 + Workflow C (4-col-with-whistleblowing · D.lgs. 24/2023 column · Italian normative refs across 5 locales) |
| D7  | Typography hierarchy | — | 5 | ≥ 3 | YES | Workflow C `style-critic.md` (12 em-words / locale · LF-2-scoped Naskh swap · 4 fonts active under AR) |
| D8  | Spacing rhythm | — | 5 | ≥ 3 | YES | A.6 F3 magazine-grid hero card flex-grow restored editorial-spread baselines · live-bound across 5 locales |
| D9  | Imagery quality | — | 4.5 | ≥ 3 | YES | A.5 / A.6 imagery scorecard · pillar photographer rotation could broaden · STRONG observation only |
| D10 | Imagery coherence | ✓ | 5 | ≥ 4 | YES | Pexels URLs imported from IT module · cross-locale substitution structurally impossible |
| D11 | Pexels-only compliance | ✓ | 5 | ≥ 4 | YES | A.5 §6 (zero non-Pexels) · re-bound at Workflow C · re-bound at Workflow D |
| D12 | Contrast safety | ✓ | 5 | ≥ 4 | YES | walk §4 + Workflow C `contrast-accessibility.md` · all critical surfaces AAA |
| D13 | Responsive quality | ✓ | 5 | ≥ 4 | YES | Workflow C 1440/880/480 + this pass 1440/720 · zero overflow at every probed viewport |
| D14 | Browser live verification quality | ✓ | 5 | ≥ 4 | YES | A.5 walk + A.6 walk + Workflow C walk + this pass walk = 4 distinct walks · fresh-process reproduction |
| D15 | Text/image coherence | — | 5 | ≥ 3 | YES | Workflow C `style-critic.md` (curatorial-architectural tone preserved 5/5 · post-A.6 founder gender match Marta↔photo) |

**All 9 CRITICAL dimensions ≥ 4: YES.** All 6 non-critical dimensions
≥ 3: YES. Aggregate (mean of 15) =
(5+5+5+5+5+5+5+5+4.5+5+5+5+5+5+5)/15 = **4.97 / 5**.

## 4 · Layer 3 · Aggregate

| Gate | Threshold | Actual | Met? |
|---|---|---|---|
| Overall average | ≥ 4.3 | 4.97 | YES (margin 0.67) |
| `[BLOCKING]` outstanding | 0 | 0 | YES |
| `[REQUIRED]` outstanding | 0 | 0 | YES |
| All 9 CRITICAL ≥ 4 | required | all = 5 | YES |
| All 6 non-critical ≥ 3 | required | min = 4.5 | YES |
| Evidence directory | complete | 11 captures (Workflow C) + 3 captures (this pass) + 8 + 5 scorecard panels | YES |
| Server URL + port recorded | required | `http://127.0.0.1:8052/` | YES |

Per `corporate-suite-quality-scorecard.md §6.1`: this profile maps to
**PASS · reference class** (the "all 15 dims at 5, zero overrides,
complete evidence" row, modulo the D9 4.5 — still PASS because no
critical dimension is below 4 and the average is 4.97), modulo the
handshake.

## 5 · Per-locale flip-decision matrix

| Locale | Walk verdict | BLOCKING | Anchor preserved? | RTL parity? | Recommended |
|---|---|---|---|---|---|
| IT | PASS | 0 | ✓ argomento | n/a | flip-eligible at workflow D handshake |
| EN | PASS | 0 | ✓ argument | n/a | flip-eligible at workflow D handshake |
| FR | PASS | 0 | ✓ argument | n/a | flip-eligible at workflow D handshake |
| ES | PASS | 0 | ✓ argumento | n/a | flip-eligible at workflow D handshake |
| AR | PASS | 0 | ✓ حُجَّة | ✓ Naskh swap LF-2-scoped · Continua LF-5 still Kufi | flip-eligible at workflow D handshake |

5 locales · 5 PASS · 0 BLOCKING. The flip can land on all 5 simultaneously
when the user authorizes — there is no held-locale subset.

## 6 · Pass-D / public-flip cascade (documented to the line)

When the user authorizes, the gatekeeper applies, in order:

1. **Registry flip** — single-line `Edit` on `TEMPLATE_REGISTRY.json` line
   387: `"tier": "draft"` → `"tier": "published_live"`. The `tier_reason`
   field can optionally be appended with the workflow-D approval timestamp
   (matches the Continua public-flip precedent which extended `tier_reason`
   to record the Workflow-D verdict line).
2. **DB sync** — `python manage.py sync_template_tiers` propagates registry
   → DB. Distribution moves 23 published_live + 1 draft → 24 published_live
   + 0 draft.
3. **Trust counter** — search `apps/catalog/tests.py` for the literal `23+`
   and `23`, plus any rendered counter text used on `/templates/business/`
   (the public catalog header banner). Bump to `24+` / `24` per the
   Continua public-flip precedent (7 explicit-literal test bumps were
   sufficient there). Verify before editing — the registry-derived count
   may already be authoritative on some surfaces.
4. **Tier-fact tests** — re-run the corporate-suite contract tests that
   scan tier-fact (Workflow C `release-gatekeeper.md` precedent §4.3);
   expect Cornice now in the live count, not the draft count. If any
   test hard-codes "4 corporate-suite live siblings" expect to bump it
   to 5.
5. **Cluster smoke** — re-run the catalog-card reachability smoke
   (24/24 anonymous now), the full 546/546 test suite, and the 5/5
   Cornice locale routes anonymous (formerly 404, expected 200 post-flip).
   The pre-existing booking-flag failure is the only allowed deviation.
6. **MEMORY.md roll-up** — append a `phase_x5_cornice_workflowD_public_flip.md`
   checkpoint pointer; promote `phase_x5_cornice_workflowC_multilingual.md`
   from CURRENT to RECENT; bump the CURRENT baseline-pointer line to reflect
   the 24-template live catalog and Cornice as the cluster's 5th `published_live`
   sibling.
7. **Public visit verification** — anonymous probes after the flip should
   show: `/templates/business/cornice-architettura/preview/` → 200 (not
   404); slug present in `/templates/business/` HTML; locale switcher
   visible to anon; `?lang=ar` AR RTL working anon. Negative tests too:
   any test that asserts Cornice is *absent* from the live catalog must
   be revised.
8. **Server shutdown** — record the shutdown timestamp on this scorecard.

The flip is **1 file edit + 1 management command + ~7 trust-counter / test
literal bumps + 1 MEMORY rollup + 1 cluster smoke**. Not complex. The
reason the flip is held is the handshake, not the work.

## 7 · Risk register

| Risk | Severity | Mitigation status |
|---|---|---|
| Voice anchor lost on a translation | HIGH | MITIGATED · 5/5 verbatim-in-translation (walk §3.1–3.2) |
| LF-2 layout reshapes under RTL | HIGH | MITIGATED · DOM-equivalent across 5 locales · zero overflow at 1440/880/480/720 |
| AR Naskh override leaks to other LF families | HIGH | MITIGATED · selector-scoped to `body.cs-lf-lf-2` · Continua LF-5 AR live-probed: still Noto Kufi (zero leakage) |
| F1 founder gender mismatch reappears in translation | MEDIUM | MITIGATED · 4 locale modules carry "Marta" + feminine agreement (Workflow C verified) |
| F2 cs-nav--lf2 inner-page chrome consistency | MEDIUM | MITIGATED · F2 lift to `_base.html` live-confirmed in this pass on /studio/ inner page (cream nav class + bg) |
| F3 magazine-grid hero card empty-band | MEDIUM | MITIGATED · F3 flex-grow scoped to LF-2 layout file · live-confirmed across 5 locales at Workflow C |
| Italian normative refs collapse in non-IT locales | MEDIUM | MITIGATED · D.lgs./MIBAC/OAPPC/CNAPPC/PRG/Soprintendenza/DAStU preserved verbatim across 5 locales (Workflow C §6) |
| `?preview=1` leak across locale switcher | MEDIUM | MITIGATED · staff-preview-aware href generation works on all 5 locale pills |
| Anonymous catalog leak after tier-flip prep | LOW | MITIGATED · slug ABSENT from `/templates/business/` HTML at draft tier (live-probed) |
| Pre-existing booking-flag test failure | LOW | DOCUMENTED · pre-dates Cornice · independent feature surface · v15 baseline known |
| D9 imagery photographer rotation | LOW (STRONG observation) | DOCUMENTED · pillar imagery cohesion is excellent; broader rotation deferred to imagery-hardening pass |
| Hero `<picture>` + srcset not introduced | LOW | DOCUMENTED · imagery-hardening pass deferred · not blocking |
| Pragma↔Fiscus 2/9 layout-distinctness (cluster legacy) | LOW | DOCUMENTED · cluster audit deferred · does not affect Cornice's 9/9 distinctness |

No HIGH or MEDIUM risk left active for Cornice's release. Two LOW items
(D9 imagery cohesion, hero `<picture>`) are documented for future
imagery-hardening passes; not blocking the public flip.

## 8 · Parallel-verification handshake block

The dev server remains at **http://127.0.0.1:8052/**. URLs to walk:

```
http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?preview=1            (IT)
http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=en&preview=1    (EN)
http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=fr&preview=1    (FR)
http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=es&preview=1    (ES)
http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=ar&preview=1    (AR · RTL · Naskh h1 · Amiri body)
```

User: please open these URLs in your own browser (logged in as
`cornice_review` or any `is_staff=True` account) and confirm visual
parity with the walk evidence before the registry flip proceeds. On
confirmation ("confirmed · proceed with public flip" or equivalent),
the gatekeeper applies the §6 cascade.

## 9 · Pending Commit B diff (NOT applied)

```diff
--- TEMPLATE_REGISTRY.json
+++ TEMPLATE_REGISTRY.json
@@ -384,7 +384,7 @@
       "price": 89,
       "featured": false,
       "status": "published",
-      "tier": "draft",
+      "tier": "published_live",
       "tier_reason": "Phase X.5 Cornice · workflow C multilingual rollout ..."
```

Single-line edit. **NOT applied.** Awaits user explicit confirmation in
the conversation per SOP §5.4 / gatekeeper §3.2.

## 10 · Verdict

**APPROVED-PENDING-HANDSHAKE.** Cornice workflow D is release-ready in
principle (4.97/5 · 0 / 18 overrides · all critical floors met · all
evidence packages complete). The flip is held until the user explicitly
authorizes parallel-verification confirmation in the conversation.
Server is kept running. Tier is preserved at `draft`.

If meaningful doubt arises during the user walk, the gatekeeper holds.
If the walk lands clean, the §6 cascade is documented to the line so
the flip ships without re-discovery.
