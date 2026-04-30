# Continua · Workflow D · Final Release Decision

**Status**: HOLD public flip · `tier=draft` preserved · `release-ready in principle`, **not** `flip now` · 2026-04-30
**Branch**: `phase-x4-continua-workflowD-release-decision`
**Predecessor passes**:
- `factory/reports/continua/continua-pass1-it.md` (workflow A · IT-only foundation)
- `factory/reports/continua/continua-pass1-review-lock.md` (workflow A.5 · DB↔registry parity)
- `factory/reports/continua/continua-lf5-it-rebuild.md` (workflow B · LF-5 structural divergence)
- `factory/reports/continua/continua-passB-multilingual.md` (workflow C · 5-locale rollout · GREEN)
- `factory/reports/browser-verification/corporate-suite-layout-regression-walk.md` (cluster regression · GREEN)
**Cluster**: corporate-suite · 4th sibling · 1st family-office · LF-5 active
**Scope**: final conservative release-decision pass — separate `ready in principle` from `flip now`, name the exact next action, do **not** auto-force `published_live`.

---

## 1 · Final verdict (one paragraph)

Continua is structurally and visually ready in principle for `published_live` across all five locales (IT/EN/FR/ES/AR + AR RTL). Every load-bearing gate the cluster pipeline measures is GREEN: LF-5 layout-family divergence holds 9/9 vs Pragma · 8/9 vs Fiscus · 8/9 vs Solaria with zero pixel drift on the three frozen siblings; the voice anchor `La continuità di una famiglia si misura in <em>generazioni</em>` travels verbatim-in-translation on the equivalent temporal noun in all five locales (`generations · générations · generaciones · الأجيال`); the LF-5-specific RTL letter-spacing reset extension landed additively in `_base.html` and confirms `letter-spacing: normal` across all 9 LF-5 eyebrow surfaces under `html[dir="rtl"]`; 545/546 tests pass with the single failure (`test_medical_and_restaurant_templates_have_booking_flag`) documented as pre-existing and unrelated to Continua; the 5×5×9 = 45-route smoke walk returns 200/200 in the staff session and the anonymous tier gate continues to serve 404 on `/templates/business/continua-stewardship/preview/` while excluding the slug entirely from `/templates/business/`. The release-gatekeeper standard requires one more thing the technical pipeline cannot provide: the explicit user parallel-verification handshake (CS-BLOCK-13 / O13 · cluster R-SOL-8 · D-102 cadence). Until the user opens the five live URLs in their own browser and confirms visual parity, **the conservative posture is HOLD**. This is not a defect call; it is the cluster's release contract. Continua remains DRAFT-REVIEWABLE through the legitimate D-055 staff-preview path, with the public-flip cascade documented to the line so the gatekeeper can ship on user sign-off without re-discovery.

---

## 2 · The six task questions (explicit answers)

### Q1 · Is Continua still best kept as draft-reviewable, or is it genuinely ready for `published_live`?

**Best kept as draft-reviewable for now.** Continua is genuinely ready *in principle* — every Layer-1 blocking override (O1–O18) clears, every Layer-2 critical-dimension floor is met, and the Layer-3 aggregate is well above the 4.3 PASS threshold. What is missing is **not** technical work: it is the user parallel-verification handshake that the release-gatekeeper standard treats as a Layer-1 precondition (`O13`, CS-BROWSER-02, SOP §5.4). With the cluster's R-SOL-8 binary still un-toggled and the brief's D-102 cadence reserving the LIVE flip for after multilingual + handshake, the conservative reading is: **HOLD**. A flip executed without the handshake would be a CLI-ship and would short-circuit the very gate that the corporate-suite cluster spent the last seven passes hardening.

### Q2 · What evidence is sufficient and what evidence is still weak?

**Sufficient (load-bearing, fresh, multi-source)**:

| Gate | Evidence | Source |
|---|---|---|
| LF-5 layout-family divergence | 9/9 vs Pragma · 8/9 vs Fiscus · 8/9 vs Solaria · B-LAYOUT-1/2/3 wide pass | `continua-lf5-it-rebuild.md §6` + `corporate-suite-layout-regression-walk.md §4–6` |
| Voice anchor preserved 5/5 locales | em on equivalent temporal noun verbatim · 5 italic-em hits per locale | this pass §3.1 + `continua-passB-multilingual.md §3` |
| AR RTL parity (the primary risk) | `dir="rtl"`, Noto Kufi h1 + Amiri body, all 9 LF-5 surfaces letter-spacing normal | this pass §3.2 + `continua-passB-multilingual.md §5` |
| Frozen-sibling regression | 0 px drift on Pragma · Fiscus · Solaria across 8 sections each | `corporate-suite-layout-regression-walk.md §3` |
| `?preview=1` propagation | 11/11 home hrefs propagate the staff flag · 4/4 mandate posts reachable | `continua-pass1-review-lock.md §6` (corporate-suite shared chrome) |
| Anonymous tier gate | `/templates/business/continua-stewardship/preview/` → 404 anon · slug absent from `/templates/business/` HTML | this pass §3.3 |
| Routes 200 in staff session | 45/45 (5 locales × 5 pages + 5 × 4 mandate posts) | this pass §3.3 |
| Tests | 545/546 pass · the 1 failure is pre-existing and unrelated | this pass §3.4 + `continua-passB-multilingual.md §8` |
| Imagery substitution closed | `_POOL_*` constants imported by every locale module · structurally impossible to drift | `continua-passB-multilingual.md §10` |
| Hero contrast (AAA) | h1 cream-on-dark plate · `linear-gradient(...,rgba(15,23,42,0.78))` · ≥11:1 ratio · KPI band + CTA dark closer 11.0:1 | this pass §3.5 |

**Weak / not yet sufficient (the only missing piece)**:

- **User parallel-verification handshake** — the gatekeeper standard requires the user to open the live preview URLs in their own browser and confirm visual parity (SOP §5.4 · CS-BLOCK-13 / O13). Until that line lands in the conversation, the gate remains blocked. There is no automated substitute.

**Acknowledged but non-blocking** (filed for later passes; do not gate workflow D):

- Pragma↔Fiscus 2/9 layout-distinctness is still a deferred audit (divergence-plan §10 Step 7). It is **not** a Continua gate; the cluster decided to ship Continua's distinctness in this pass and tackle the inter-frozen-sibling collision later. Continua is 8–9/9 different from every frozen sibling, so its identity is unaffected.
- Fiscus's slot-4 calendar cell does not currently emit despite `cs-lf-lf-3` body class; Solaria's manifesto/percorsi/slot-5 cycle/omit-leadership shape does not currently emit despite `cs-lf-lf-4`. Both pre-date this pass and are documented in `corporate-suite-layout-regression-walk.md §8`. They do not affect Continua.
- Hero `<picture>` + srcset is still pending an imagery-hardening pass per `continua-pass2-lf5/release-gatekeeper.md §3`. Not blocking.
- Pre-existing test failure `test_medical_and_restaurant_templates_have_booking_flag` is unrelated (the assertion compares the medical/restaurant booking-enabled set; Continua isn't in either family). Documented in `continua-lf5-it-rebuild.md §8.4`.

### Q3 · Does the human-visible product now match the original goal (premium, modern, elegant, professional, structurally distinct)?

**Yes, on all five axes.**

- **Premium**: object-led library hero (Pexels 36093623) reads as room-architectural stewardship, not generic warm interior. Pine + brass palette consumes the only OPEN matrix §1.3 cool-secondary + warm-accent combination. Crimson Pro + Public Sans typography pulls Continua out of the cluster's generic "Inter on whatever serif" comfort zone. `MANDATO MEDIO 18 anni · GENERAZIONI IN CARICO 3 · RIUNIONI CDF 4/anno` meta-strip reads as an actual family-office firm, not a generic advisory consultancy. (See `it-1440-firstscroll.png`.)
- **Modern**: condensed-minimal-top 64px nav with no phone number signals stewardship not transactional. The dark CTA closer + brass border button is a contemporary corporate-suite move, not a 2018-era hero-only pattern. The locale switcher is a 5-pill bar, not a hreflang dropdown.
- **Elegant**: governance-cycle-strip in slot-2 frames the firm as cadence-led, not number-led — three cells with eyebrow + figure + context-line that reads as institutional rhythm. Italic-em on `<em>generazioni</em>` in the h1 + cta-closer is the cluster's strongest cross-locale identity signal and travels in every translation.
- **Professional / Modern professionalism**: 3-card leadership with environmental stations (Sala dell'archivio · Tavolo del Consiglio · Studio del compliance) and 60s/40s/50s demographics closes Solaria's 30sCx2 gap. Whistleblowing channel surfaced both in the sectors-band eyebrow and the 4-col footer column. D.lgs. 24/2023, Reg. UE 679/2016, OAM, ANC, STEP credentials are explicit. Voice anchor preserved verbatim across the page (h1 + cta-closer).
- **Structurally distinct**: every L1–L9 axis differs from Pragma, 8/9 from Fiscus, 8/9 from Solaria. The B-LAYOUT-1 wireframe overlay diff is 82.1% / 79.4% / 69.0% — well above the ≥30% threshold on every pair. CS-LAYOUT-12, CS-LAYOUT-13, CS-LAYOUT-14 all PASS. The cluster's "all four siblings are palette/copy variants of one master template" diagnosis from the divergence plan is closed.

### Q4 · Are there any remaining blockers, or only release-decision choices?

**Only a release-decision choice.** The blockers list is empty:

- 0 BLOCKING findings across all 5 locales (Pass B Multilingual scorecard §4 + this pass §3).
- 0 Layer-1 overrides triggered (O1–O18 all clear · this pass §4).
- 0 critical-dimension floors missed (this pass §5).
- 0 REQUIRED findings outstanding.

The single remaining item is a **decision** ("flip now" vs "stay in draft pending user handshake"), not a blocker. The conservative reading on a high-stakes flip is: HOLD until the user explicitly authorizes.

### Q5 · If release-ready, what exact minimal steps are needed for the flip?

When the user authorizes, the cascade is documented to the line so the gatekeeper can apply it without re-discovery. Mirrors the Solaria Pass D plan and the `continua-passB-multilingual.md §13` playbook:

1. **Registry flip** — single-line `Edit` on `TEMPLATE_REGISTRY.json` line 337: `"tier": "draft"` → `"tier": "published_live"`.
2. **DB sync** — `python manage.py sync_template_tiers` propagates registry → DB. Distribution moves 22 published_live / 1 draft → 23 published_live / 0 draft.
3. **Trust counter (catalog page)** — locate the marketplace counter string `22+` (or equivalent) used on `/templates/business/` and bump to `23+`. (The catalog count itself recomputes automatically from the registry; only the human-visible "trust count" string may need a 1-character edit. Check before editing — the registry-derived path may already be authoritative.)
4. **Tier-fact tests** — re-run the 6 corporate-suite contract tests that scan tier-fact (PASS B `release-gatekeeper.md §4.3`); expect Continua now in the live count, not the draft count. If any test hard-codes "5 corporate-suite live siblings" expect to bump it to 6.
5. **Cluster smoke** — re-run the 23/23 catalog-card reachability smoke + the full 546/546 test suite + the 5/5 Continua locale routes. The pre-existing booking-flag failure is the only allowed deviation.
6. **MEMORY.md roll-up** — append a `phase_x4_continua_workflowD_release_decision.md` checkpoint pointer; promote `phase_x4_continua_passB_multilingual.md` from CURRENT to RECENT; update the CURRENT baseline pointer line to reflect the 23-template live catalog.
7. **Public visit verification** — anonymous probes after the flip should show: `/templates/business/continua-stewardship/preview/` → 200 (not 404) · slug present in `/templates/business/` HTML · locale switcher 5-pill bar visible to anon · `?lang=ar` AR RTL working anon. (Negative tests too: any test that asserts Continua is *absent* from the live catalog must be revised.)
8. **Server shutdown** — gatekeeper records the shutdown timestamp on the scorecard.

The flip is 1 file edit + 1 management command + 1 trust-counter edit + 1 MEMORY rollup + 1 cluster smoke. **Not** complex. The reason the flip is held is the handshake, not the work.

### Q6 · If not release-ready, what exact issues remain?

**There are no product issues remaining.** The only outstanding item is the user parallel-verification handshake described in Q1 / Q2 / Q4. To convert that into an actionable list:

- The user opens these 5 URLs (server kept open for the walk):
  - `http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?preview=1` (IT)
  - `http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=en&preview=1` (EN)
  - `http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=fr&preview=1` (FR)
  - `http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=es&preview=1` (ES)
  - `http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=ar&preview=1` (AR · RTL)
- The user logs in as `cs_review_fix` (existing staff user from prior passes) — or a fresh staff session — to bypass the D-055 anonymous gate.
- The user confirms in the conversation: "confirmed · proceed with Commit B" (or equivalent explicit phrasing per SOP §5.4 / gatekeeper §3.2).
- The gatekeeper applies steps 1–8 above.

If the user prefers a **scoped** flip (e.g., IT-only, with EN/FR/ES/AR held), the gatekeeper re-scopes per Solaria's Pass C precedent: keep the 4 locale modules in place, keep the registry's `locales: ["it","en","fr","es","ar"]` (since that drives the runtime locale loader, not the visibility), but the user-facing review walk is documented as IT-only and the gatekeeper's flip line names IT-only. The all-5-locale flip is the recommended path because the multilingual walk already passed 70/70.

If the user prefers to **wait for an imagery-hardening pass** (`<picture>` + srcset + WebP/AVIF · per `continua-pass2-lf5/release-gatekeeper.md §3`), that is the only legitimate non-handshake reason to extend the hold. It is not a Continua-specific blocker; it is a cluster-wide forward-investment.

---

## 3 · Fresh evidence captured by this pass

### 3.1 · Voice anchor verbatim across 5 locales (live render at workflow D · 1440)

| Locale | h1 (rendered) | em-words (h1 + h2 italic-em) | All 5 italic-em hits? |
|---|---|---|---|
| IT | La continuità di una famiglia si misura in *generazioni*. | generazioni · cadenza · un solo · una sola cadenza · generazioni | ✓ |
| EN | The continuity of a family is measured in *generations*. | generations · cadence · one single · one single cadence · generations | ✓ |
| FR | La continuité d'une famille se mesure en *générations*. | générations · cadence · un seul · une seule cadence · générations | ✓ |
| ES | La continuidad de una familia se mide en *generaciones*. | generaciones · cadencia · un solo · una sola cadencia · generaciones | ✓ |
| AR | استمراريّة العائلة تُقاس *بالأجيال*. | بالأجيال · إيقاع · تفويض واحد · إيقاع واحد · بالأجيال | ✓ |

5 × 5 = **25/25 italic-em hits live-verified** at 1440. CTA-closer h2 carries the anchor sentence in every locale (page opens and closes on it). Pass B Multilingual's headline outcome reproduces verbatim on the workflow-D server.

### 3.2 · AR RTL parity re-verified

```
htmlLang = "ar"            htmlDir = "rtl"
fontH1   = "Noto Kufi Arabic", "Crimson Pro", Georgia, serif
fontBody = Amiri, "Public Sans", system-ui, sans-serif
```

CS-TYPE-05 reset (extended in Pass B `_base.html`) — all 9 LF-5 eyebrow surfaces compute `letter-spacing: normal` under `html[dir="rtl"]`:

```
.cs-cycle .cell .eyebrow                    : normal
.cs-pillars .pillar .num                    : normal
.cs-sectors .whistle                        : normal
.cs-leadership .card .station               : normal
.cs-cases-preview .row .title .eyebrow      : normal
.cs-cases-preview .row .horizon strong      : normal
.cs-hero .frame .anchor .eyebrow            : normal
.cs-hero .meta-strip .item                  : normal
.cs-hero .credit-row .credit                : normal
```

No horizontal overflow at AR @ 1440 (`pageW = scrollW = 1425`) or AR @ 720 (`pageW = scrollW = 705`). Locale switcher current=AR with 5 pills. Latin proper nouns preserved (Continua wordmark · Albo dei Trustees · FAMILY OFFICE · MILANO · STEWARDSHIP · Latin numerals 18 / 3 / 4).

### 3.3 · Tier-gate + smoke (workflow D server)

```
GET /templates/business/                                               anon → 200 · slug "continua-stewardship" absent
GET /templates/business/continua-stewardship/preview/                  anon → 404 (D-055 gate intact)
GET /templates/business/continua-stewardship/preview/?preview=1        anon → 404 (preview flag without staff is rejected)

Staff session (cs_review_fix · is_staff=True), 5 locales × 5 pages + 5 locales × 4 mandate posts = 45 routes
  → 45 / 45 HTTP 200
```

The legitimate D-055 staff-preview path established by `continua-pass1-review-lock.md` survives intact under the workflow-D server. Anonymous catalog still excludes Continua. Internal hrefs propagate `?preview=1` correctly via the corporate-suite chrome's `staff_preview` resolver.

### 3.4 · Test suite

```
$ python manage.py test
Ran 546 tests in 179.6s
FAILED (failures=1)
  → test_medical_and_restaurant_templates_have_booking_flag

Continua-related regressions: 0
Pre-existing failure (out of scope per `continua-lf5-it-rebuild.md §8.4`): 1
  reason: assertion expects exact set of medical+restaurant+lawyer+W2 booking
          slugs. Continua is not a member of any of those families and is
          unrelated to the booking flag. Documented as pre-existing across
          three prior Continua passes.
Final tally: 545 / 546 PASS · same as Pass B Multilingual.
```

### 3.5 · Hero contrast (AAA spot-check)

```
h1 (.cs-hero .frame h1)
  fg = rgb(238, 240, 243)  /* var(--cream) */
  bg-effective = rgb(15, 23, 42, 0.78) gradient over the photo plate
  approx ratio @ plate foot = 11–13 : 1   (AAA · WCAG ≥ 7.0)

KPI band (.cs-kpi-band)
  fg = rgb(238, 240, 243)
  bg = rgb(15, 58, 48)  /* var(--primary) */
  ratio = 11.03 : 1   (AAA)

CTA dark closer (.cs-cta h2)
  fg = rgb(238, 240, 243)
  bg = rgb(15, 58, 48)
  ratio = 11.03 : 1   (AAA)

Nav link (.cs-nav a)
  fg = rgb(238, 240, 243)
  bg = rgb(15, 58, 48)
  ratio = 11.03 : 1   (AAA)
```

No headline reads dark-on-dark; no hero h1 reads cream-on-cream. AP1 and AP11 cleared. (CS-BLOCK-01 · CS-BLOCK-17 · O1 · O17 all clear.)

---

## 4 · Layer 1 · Blocking-override review (all 18 must clear for PASS)

| # | Override | Triggered? | Evidence anchor |
|---|---|---|---|
| O1 | `h1..h5` distance < 120 OR WCAG < 4.5 | NO | this pass §3.5 (h1 ≥ 11:1 · KPI / CTA / nav 11.03:1) |
| O2 | Horizontal scrollbar at any rubric viewport | NO | Pass B §5 (1440 + 720 verified) + this pass §3.2 (AR @ 1440 + 720) |
| O3 | Hero / nav fail to stack at ≤ 720 | NO | LF-5 IT rebuild §7 (drawer at ≤ 880) · Pass B §3 (ar-720-fullpage) |
| O4 | Imagery URL 404 on live | NO | LF-5 IT rebuild §6 (7/7 reachable) · Pass B §3 (45/45 routes 200) |
| O5 | Imagery 3-second semantic fail | NO | Pass 1 IT §6 (slot 0 re-curate to 36093623 · object-led library) · Pass B §10 (`_POOL_*` reuse) |
| O6 | Imagery mood vs voice anchor contradiction | NO | Pass 1 IT §3 (room-architectural stewardship vs 1:1 conversation) |
| O7 | Non-Pexels URL on a new pilot | NO | LF-5 IT rebuild §6 + Pass B §10 (Pexels-only · 8 IDs) |
| O8 | Editor click-to-edit on `/preview/` route | NO | Pass B walk · `cs-lf-lf-5 lm-ready` body class · no editor affordance probed |
| O9 | Lorem ipsum / "Replace this text" | NO | All 5 locale modules ship realistic stewardship copy |
| O10 | Fake certifications | NO | OAM · ANC · Albo dei Trustees · STEP · D.lgs. 24/2023 (real institutions) |
| O11 | Voice anchor missing in any locale | NO | this pass §3.1 (5/5 verbatim-in-translation) |
| O12 | D-054 10-gate triangulation absent | NO | `continua-distinctness-proof.md` 5/5 vs Pragma · Fiscus · Solaria; per-locale docstrings name reference voices |
| O13 | Walk URL + port not recorded | **NO at this pass · YES at flip-readiness** | URL `http://127.0.0.1:8051/...` recorded in this report · §6 · the **handshake** is the part still pending — see Q1 |
| O14 | Walk missing any rubric viewport | NO | LF-5 IT rebuild §7 (1920/1440/1100/720/480) · Pass B (1440 + AR 720) · this pass (1440 + AR 720) |
| O15 | Evidence directory incomplete | NO | Aggregate evidence: 12 captures pass-1 + 7 captures Pass B + 4 captures regression-walk + 2 captures this pass + 26+ scorecard files |
| O16 | Nav polarity broken / >1 accent in nav | NO | Nav background = `--primary` (rgb(15,58,48)) · single brass underline on active item · per regression-walk §2 |
| O17 | Dark-on-dark in `.dark` sections | NO | this pass §3.5 (KPI + CTA + nav 11.03:1 ≥ 7.0 AAA) |
| O18 | No live walk (test-only ship) | NO | This pass performed a live walk · 5 locales × 1440 + AR 720 + IT firstscroll capture + AR firstscroll capture |

**0 / 18 overrides triggered.**

The single nuance: O13 is **half-met**. The "walk URL + port" is recorded (`http://127.0.0.1:8051/`); the **user parallel-verification confirmation** is the second half of the gatekeeper's handshake protocol (SOP §5.4) and that line has not yet been spoken in the conversation. Until it does, Continua sits at "PASS pending handshake" — which the SOP treats as HOLD, not LIVE.

---

## 5 · Layer 2 · Critical-dimension floor review

Per `corporate-suite-quality-scorecard.md §3 + §5`. Scores cite the upstream agent reports per SOP §2.2 (gatekeeper does not re-score).

| D# | Dim | CRITICAL? | Score | Floor | Met? | Source |
|---|---|---|---|---|---|---|
| D1  | Premium feel | ✓ | 5 | ≥ 4 | YES | LF-5 IT rebuild scorecard `style-critic.md` + this pass §2 Q3 |
| D2  | Elegance | ✓ | 5 | ≥ 4 | YES | LF-5 IT rebuild scorecard `style-critic.md` |
| D3  | Modern professionalism | ✓ | 5 | ≥ 4 | YES | Pass B `style-critic.md` (5/5 locale register guides) |
| D4  | Hero readability | ✓ | 5 | ≥ 4 | YES | this pass §3.5 (≥11:1 AAA) |
| D5  | Navbar quality | — | 5 | ≥ 3 | YES | regression-walk §2 (cs-nav cs-nav--lf5 64px LF-5-correct) |
| D6  | Footer quality | — | 5 | ≥ 3 | YES | LF-5 IT rebuild §3 (4-col-with-whistleblowing) |
| D7  | Typography hierarchy | — | 5 | ≥ 3 | YES | Pass B `style-critic.md` (5 italic-em / locale · Crimson + Public Sans + Noto Kufi + Amiri) |
| D8  | Spacing rhythm | — | 5 | ≥ 3 | YES | LF-5 IT rebuild §7 (`--space-section-y/x` per CS-RHYTHM-01) |
| D9  | Imagery quality | — | 4.5 | ≥ 3 | YES | LF-5 IT rebuild scorecard (pillar icons grayscale-flattened from 4 photographers · STRONG observation, not floor breach) |
| D10 | Imagery coherence | ✓ | 5 | ≥ 4 | YES | Pass 1 §6 + Pass B §10 (`_POOL_*` substitution structurally impossible) |
| D11 | Pexels-only compliance | ✓ | 5 | ≥ 4 | YES | LF-5 IT rebuild §6 (8 Pexels IDs · zero non-Pexels) |
| D12 | Contrast safety | ✓ | 5 | ≥ 4 | YES | this pass §3.5 + Pass B `contrast-accessibility.md` (AAA hero · KPI · CTA · nav) |
| D13 | Responsive quality | ✓ | 5 | ≥ 4 | YES | LF-5 IT rebuild §7 (1920/1440/1100/720/480) + AR 1440/720 · zero overflow |
| D14 | Browser live verification quality | ✓ | 5 | ≥ 4 | YES | regression-walk + LF-5 IT rebuild + Pass B + this pass = 4 distinct walks at separate ports |
| D15 | Text/image coherence | — | 5 | ≥ 3 | YES | Pass B `style-critic.md` (room-architectural stewardship + multi-generational tone preserved 5/5 locales) |

- **Aggregate (mean of 15)**: (5+5+5+5+5+5+5+5+4.5+5+5+5+5+5+5)/15 = **4.97 / 5**.
- All 9 CRITICAL dimensions ≥ 4: **YES**.
- All 6 non-critical dimensions ≥ 3: **YES**.
- Aggregate ≥ 4.3: **YES** (4.97 vs 4.3 floor · margin 0.67).
- Zero `[BLOCKING]` outstanding: **YES**.
- Zero `[REQUIRED]` outstanding: **YES**.

Per `corporate-suite-quality-scorecard.md §6.1` table: this profile maps to **PASS · reference class** (the "all 15 at 5" row), modulo the handshake.

---

## 6 · Server posture at landing

```
$ python manage.py runserver 127.0.0.1:8051 --noreload
```

Listening at **http://127.0.0.1:8051/**. The server is left running for the user parallel-verification walk. Staff session: existing `cs_review_fix` user (`is_staff=True`, password owned by the user from prior corporate-suite passes; rotate before any external visit).

URLs left open for the user-handshake walk:

```
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?preview=1            (IT)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=en&preview=1    (EN)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=fr&preview=1    (FR)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=es&preview=1    (ES)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=ar&preview=1    (AR · RTL)
```

Each URL also reaches `chi-siamo · custodia · mandati · contatti` and the 4 mandate-detail posts via the staff-preview-aware nav (verified 45/45 routes 200 · §3.3).

Anonymous probes:

```
http://127.0.0.1:8051/templates/business/                                       → 200 · slug ABSENT
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/          → 404
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?preview=1→ 404
```

Tier gate intact. DB tier and registry tier both equal `draft`.

---

## 7 · What was NOT changed by this pass

To remove any ambiguity about scope:

- `apps/editor/*` — UNTOUCHED
- `apps/projects/*` — UNTOUCHED
- `apps/commerce/*` — UNTOUCHED
- `apps/catalog/*` source code — UNTOUCHED
- `templates/**` — UNTOUCHED
- `TEMPLATE_REGISTRY.json` — UNTOUCHED (still `tier: draft`)
- All `apps/catalog/template_content_continua*.py` — UNTOUCHED
- DNA registry, imagery pool, imagery policy, seed command — UNTOUCHED
- No new archetype, no new template, no new migration
- No `sync_template_tiers` invocation that would alter persisted state (the test runner's transient flips self-revert at every test-DB teardown; final dev-DB state is `draft`)

The only persisted artifacts of this pass are reports + 2 verification captures + 1 helper script:

```
factory/reports/continua/continua-workflowD-release-decision.md                              (THIS file)
factory/reports/browser-verification/continua-workflowD-release-decision.md                  (browser walk index)
factory/reports/browser-verification/continua-workflowD-release-decision/it-1440-firstscroll.png
factory/reports/browser-verification/continua-workflowD-release-decision/ar-1440-firstscroll.png
factory/reports/scorecard/continua-workflowD-release-decision/build-report.md
factory/reports/scorecard/continua-workflowD-release-decision/browser-verifier.md
factory/reports/scorecard/continua-workflowD-release-decision/release-gatekeeper.md
factory/reports/scorecard/continua-workflowD-release-decision/scorecard.md
factory/reports/scorecard/continua-workflowD-release-decision/summary.md
factory/reports/scorecard/continua-workflowD-release-decision/_smoke.py                       (the 45-route prober)
```

---

## 8 · Operational distinction (the conservative core)

This pass insists on a separation that earlier passes elided in passing:

- **"Ready in principle"** = every Layer-1 / Layer-2 / Layer-3 gate satisfied, every observation agent GREEN, every walk artifact captured. **Continua is here.**
- **"Flip now"** = the above PLUS the user parallel-verification handshake spoken in the conversation. **Continua is not here yet.**

A pass that confuses the two would either:
- (a) auto-flip on technical greenness and short-circuit CS-BLOCK-13 / O13 / SOP §5.4 — **rejected as a CLI-ship** per gatekeeper standard; or
- (b) refuse to recognize that nothing technical remains and treat HOLD as a defect call — **rejected as conservative-theater** that wastes the user's review budget.

The honest posture is "release-ready in principle · explicit hold pending the handshake the cluster contracts for". That is the verdict this pass files.

---

## 9 · Verdict

**Continua workflow D · final release-decision: HOLD public flip · `tier=draft` preserved.**

- Technical readiness: **PASS** (all 18 overrides clear · all 9 critical floors ≥ 4 · aggregate 4.97 / 5).
- Release readiness: **PASS pending user handshake** (CS-BLOCK-13 / O13 / SOP §5.4 · cluster R-SOL-8 · D-102 cadence).
- Recommended next action: **the user opens the 5 URLs above in their own browser, completes the parallel-verification walk, and confirms in the conversation. On confirmation, the gatekeeper applies the §2 Q5 cascade (1 file edit + 1 management command + 1 trust-counter edit + 1 MEMORY rollup + 1 cluster smoke).**

If meaningful doubt arises during the walk, **HOLD wins** per the task's hard constraint. If the walk lands clean, the cascade is documented to the line so the flip can ship without re-discovery.

This pass does not flip the tier. It opens the handshake.
