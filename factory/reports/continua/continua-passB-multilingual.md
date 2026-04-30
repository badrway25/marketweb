# Continua · Pass B Multilingual report (workflow C)

**Status**: GREEN · review-ready · `tier=draft` preserved · 2026-04-30
**Branch**: `phase-x4-continua-passB-multilingual-lf5`
**Predecessor pass**: `factory/reports/continua/continua-lf5-it-rebuild.md` (LF-5 IT rebuild · pass 2 · `d8253e5`)
**Cluster**: corporate-suite · 4th sibling · 1st family-office variant
**Scope**: multilingual rollout on top of the approved LF-5 Italian layout · IT preserved · EN/FR/ES/AR added · AR with real RTL via Noto Kufi heading + Amiri body swap
**Aggregate**: 5 / 5 locales GREEN · 0 BLOCKING · 1 STRONG fix mid-walk (closed) · 0 OBSERVATION

---

## 1 · One-paragraph summary

Continua's LF-5 IT rebuild closed visually green on 2026-04-29 with multilingual rollout explicitly held to a separate workflow C pass. This pass authors that rollout. The four locale trees (EN, FR, ES, AR) mirror the Italian shape exactly — same keys, same nesting, same list shapes — with the voice anchor preserved verbatim-in-translation across all five locales (the temporal noun *generazioni* travels to *generations* / *générations* / *generaciones* / *الأجيال*, with `<em>` always wrapping the equivalent load-bearing word). The Pexels-only imagery pool is re-used unchanged across every locale via `_POOL_*` constants extracted from the IT module, so the build-time imagery checks see identical URLs in every locale. The corporate-suite chrome's existing `dir="rtl"` + Noto Kufi heading + Amiri body swap pipeline picks up Arabic transparently; one STRONG finding emerged mid-walk — the LF-5-specific eyebrow surfaces (cycle cell eyebrows, pillar matrix numbers, sectors whistleblowing strip, leadership stations, timeline row eyebrows + horizon strongs, hero meta-strip, hero credit-row, hero anchor eyebrow) were absent from the original CS-TYPE-05 RTL letter-spacing reset list, so Arabic uppercase text still showed LTR tracking artifacts. Fixed in `_base.html` by extending the existing reset rule to the ten LF-5 surfaces, re-walked AR, all letter-spacing now reads `normal`, no other locale affected. Tier remains `draft` — public flip held for the user-handshake gate (cluster R-SOL-8 / D-102 cadence). **Verdict: Continua ships in 5 locales at draft tier, ready for human visual review across IT · EN · FR · ES · AR with RTL parity.**

---

## 2 · Files changed

```
apps/catalog/template_content_continua.py        (refactor · pool URL constants extracted to module level)
apps/catalog/template_content_continua_en.py     (NEW · 712 lines · English locale tree)
apps/catalog/template_content_continua_fr.py     (NEW · 745 lines · French locale tree)
apps/catalog/template_content_continua_es.py     (NEW · 745 lines · Spanish locale tree)
apps/catalog/template_content_continua_ar.py     (NEW · 750 lines · Arabic locale tree, MSA register)
apps/catalog/template_content.py                 (registry · 4 imports + 4 locale entries on `continua-stewardship`)
TEMPLATE_REGISTRY.json                           (locales: ["it"] → ["it","en","fr","es","ar"])
templates/live_templates/business/corporate-suite/_base.html
                                                 (CS-TYPE-05 RTL reset extended to 10 LF-5 surfaces · STRONG fix)
factory/reports/continua/continua-passB-multilingual.md                (THIS file)
factory/reports/browser-verification/continua-passB-multilingual.md    (browser walk index)
factory/reports/browser-verification/continua-passB-multilingual/      (7 captures · 5 locales × home + AR-720 + AR-contatti)
factory/reports/scorecard/continua-passB-multilingual/                 (8 scorecard files)
```

No editor / projects / commerce file touched. No new archetype defined. No imagery URL changed. The IT pass-2 LF-5 layout is preserved verbatim — the only IT-side edit is the URL-pool refactor (semantically a no-op).

---

## 3 · Voice anchor · verbatim-in-translation across 5 locales

| Locale | Headline (rendered) | Em-word | Em wraps the equivalent TEMPORAL noun? |
|---|---|---|---|
| IT | La continuità di una famiglia si misura in *generazioni*. | generazioni | ✓ |
| EN | The continuity of a family is measured in *generations*. | generations | ✓ |
| FR | La continuité d'une famille se mesure en *générations*. | générations | ✓ |
| ES | La continuidad de una familia se mide en *generaciones*. | generaciones | ✓ |
| AR | استمراريّة العائلة تُقاس *بالأجيال*. | الأجيال | ✓ |

The hero h1 and the cta-closer h2 carry the same anchor sentence in every locale (page opens and closes on the voice anchor · CS-EXEC-01). The em-word travels with the equivalent TEMPORAL noun in every locale; it does not get swapped out for an "easier" word.

Secondary italic-em hits (cycle / pillars / cases h2):
- IT: `cadenza` · `un solo` · `una sola cadenza`
- EN: `cadence` · `one single` · `one single cadence`
- FR: `cadence` · `un seul` · `une seule cadence`
- ES: `cadencia` · `un solo` · `una sola cadencia`
- AR: `إيقاع` · `تفويض واحد` · `إيقاع واحد`

5 italic-em hits per locale, all on load-bearing words, none flattened by translation.

---

## 4 · LF-5 layout integrity verdict

Each locale's home rendered the LF-5 section sequence intact:

```
cs-hero → cs-cycle → cs-pillars → cs-kpi-band → cs-sectors → cs-leadership → cs-cases-preview → cs-cta
```

Identical 8-section list across all 5 locales. The cycle promoted to slot-2 (governance opening, not mid-page aside), pillars matrix 2×2 with monochrome icons, KPI dark band at slot-4, sectors carrying the whistleblowing eyebrow, pillar-photo leadership, vertical timeline cases, dark CTA closer. The brand contract (cream paper, serif heading + sans body, italic-em, accent ≤3 hits/viewport, AAA h1, AA dark-section descendants) holds verbatim from `_base.html`.

| Cell | IT | EN | FR | ES | AR |
|---|---|---|---|---|---|
| Hero overlay (h1 cream-on-dark plate AAA) | PASS | PASS | PASS | PASS | PASS |
| Section sequence (8 sections in order) | PASS | PASS | PASS | PASS | PASS |
| Italic-em on load-bearing word(s) | PASS (5 hits) | PASS (5 hits) | PASS (5 hits) | PASS (5 hits) | PASS (5 hits) |
| Hero meta-strip (3 cells) | PASS | PASS | PASS | PASS | PASS |
| Pillars matrix (4-pillar 2×2) | PASS | PASS | PASS | PASS | PASS |
| KPI band (one dark band per home) | PASS | PASS | PASS | PASS | PASS |
| Sectors + whistleblowing eyebrow | PASS | PASS | PASS | PASS | PASS |
| Leadership 3-card with stations | PASS | PASS | PASS | PASS | PASS |
| Cases timeline (4 rows) | PASS | PASS | PASS | PASS | PASS |
| CTA dark closer + voice-anchor restate | PASS | PASS | PASS | PASS | PASS |
| Locale switcher (5 pills, current flagged) | PASS | PASS | PASS | PASS | PASS |
| `?lang=xx` propagation across nav/footer | PASS | PASS | PASS | PASS | PASS |
| No horizontal overflow at 1440 | PASS | PASS | PASS | PASS | PASS |
| `?preview=1` propagation across internal links | PASS | PASS | PASS | PASS | PASS |

**14 cells × 5 locales = 70/70 PASS.** Above the 11/11 Solaria Pass B precedent.

---

## 5 · AR RTL parity (the primary risk)

The corporate-suite chrome already supports `dir="rtl"` via the `_base.html` logical-property layer — Solaria Pass B was the precedent. LF-5 introduced new eyebrow surfaces that were not in the original CS-TYPE-05 RTL letter-spacing reset list, so Arabic uppercase text rendered with LTR tracking artifacts on those specific surfaces (cycle cell eyebrows, pillar matrix numbers, sectors whistleblowing strip, leadership stations, timeline row eyebrows + horizon strongs, hero meta-strip, hero credit-row, hero anchor eyebrow).

**Fix applied** (`_base.html` § "Letter-spacing flatten on chrome labels"):

```css
html[dir="rtl"] .mp-lang .mp-lang-label,
html[dir="rtl"] .mp-lang a.mp-lang-pill,
/* Phase X.4b Continua Pass B · LF-5 eyebrow surfaces. */
html[dir="rtl"] .cs-hero .frame .anchor .eyebrow,
html[dir="rtl"] .cs-hero .meta-strip .item,
html[dir="rtl"] .cs-hero .credit-row .credit,
html[dir="rtl"] .cs-cycle .cell .eyebrow,
html[dir="rtl"] .cs-pillars .pillar .num,
html[dir="rtl"] .cs-sectors .whistle,
html[dir="rtl"] .cs-leadership .card .station,
html[dir="rtl"] .cs-cases-preview .row .title .eyebrow,
html[dir="rtl"] .cs-cases-preview .row .horizon,
html[dir="rtl"] .cs-cases-preview .row .horizon strong {
  letter-spacing: 0;
}
```

Post-fix re-walk (computed `letter-spacing`):

| Surface | Pre-fix | Post-fix |
|---|---|---|
| cs-cycle .cell .eyebrow | 2.42px | normal |
| cs-pillars .pillar .num | 0.52px | normal |
| cs-sectors .whistle | 2.20px | normal |
| cs-leadership .card .station | 1.20px | normal |
| cs-cases-preview .row .title .eyebrow | 2.20px | normal |
| cs-cases-preview .row .horizon strong | 1.98px | normal |
| cs-hero .frame .anchor .eyebrow | 2.42px | normal |
| cs-hero .meta-strip .item | 2.20px | normal |
| cs-hero .credit-row .credit | 2.20px | normal |

The fix is RTL-scoped (`html[dir="rtl"]` selector) so IT/EN/FR/ES are byte-equivalent before and after — re-confirmed by re-rendering all four locales.

**AR RTL checklist** (per `template-multilingual-orchestrator.md §6`):

- [x] `<html dir="rtl" lang="ar">` set
- [x] LF-5 hero overlay (object-led, no 55/45 split): h1 cream-plate visible RTL-flowing, accent em on الأجيال
- [x] Navbar trailing CTA on the LEFT (mirrored)
- [x] Footer columns stacked right-to-left
- [x] Locale switcher pills (AR · ES · FR · EN · IT) flow RTL with current locale flagged
- [x] Latin wordmark "Continua" preserved (Latin font, no Arabic transliteration)
- [x] `.num` numerics stay Latin (18 / 3 / € 1.8 B / 4 — tabular alignment preserved)
- [x] Heading font swap to Noto Kufi Arabic working (`getComputedStyle(h1).fontFamily` → `"Noto Kufi Arabic", "Crimson Pro", Georgia, serif`)
- [x] Body font swap to Amiri working (`getComputedStyle(.cs-hero .frame .body .sub).fontFamily` → `Amiri, "Public Sans", system-ui, sans-serif`)
- [x] Letter-spacing on uppercase eyebrows is 0 across every LF-5 surface (CS-TYPE-05 reset extended above)
- [x] No horizontal scroll at any of the cluster viewports (1440 + 720 verified, scrollW = clientW)
- [x] Reading direction natural at every paragraph break (chi-siamo body + cases timeline + contatti form sections all RTL-flowing)
- [x] CTA copy is natural MSA, not transliterated English ("ابدأ حواراً تفويضياً", not "بوك ديسكوفري كول")
- [x] Italian normative references preserved as Latin (D.lgs. 24/2023, Reg. UE 679/2016, OAM, ANC, Albo dei Trustees, STEP, Codice della Crisi, Compliance Officer, Senior Steward, Family Officer, BDR)
- [x] Italian addresses preserved (Via San Marco 22 · 20121 Milano · Brera; Riva Caccia 1 · 6900 Lugano; Boulevard Royal 28 · L-2449 Luxembourg)

---

## 6 · Distinctness verdict across locales

The IT-side LF-5 distinctness matrix held at 9/9 vs Pragma · 8/9 vs Fiscus · 8/9 vs Solaria. Multilingual rollout does not change DOM shape (it only translates strings), so the matrix score is preserved across all 5 locales. The voice anchor's load-bearing italic-em on a TEMPORAL noun (verbatim-in-translation) is the cluster's strongest cross-locale identity signal — Continua reads as the same firm in every language, distinct from Pragma/Fiscus/Solaria in every language.

| Locale | Voice anchor visible? | Pillar count = 4? | Stewardship register? | Multi-generational tone? |
|---|---|---|---|---|
| IT | ✓ generazioni | ✓ | ✓ custodial/longitudinal | ✓ |
| EN | ✓ generations | ✓ | ✓ Pictet/Stonehage register | ✓ |
| FR | ✓ générations | ✓ | ✓ Mirabaud/Edmond register | ✓ |
| ES | ✓ generaciones | ✓ | ✓ Banque Pictet España register | ✓ |
| AR | ✓ بالأجيال | ✓ | ✓ formal MSA / HBR Arabia register | ✓ |

No locale flattens the stewardship voice into generic advisory copy. The multi-generational tone is preserved across all 5 locales (the `Famiglia A · 4ª generazione` / `Family A · 4th generation` / `Famille A · 4ᵉ génération` / `Familia A · 4ª generación` / `العائلة A · الجيل الرابع` line surfaces in every locale's home timeline + cases list).

---

## 7 · Browser walk · 7 captures + 6 instrumented walks

| Capture | Path |
|---|---|
| IT 1440 fullpage | `factory/reports/browser-verification/continua-passB-multilingual/it-1440-fullpage.png` |
| EN 1440 fullpage | `factory/reports/browser-verification/continua-passB-multilingual/en-1440-fullpage.png` |
| FR 1440 fullpage | `factory/reports/browser-verification/continua-passB-multilingual/fr-1440-fullpage.png` |
| ES 1440 fullpage | `factory/reports/browser-verification/continua-passB-multilingual/es-1440-fullpage.png` |
| AR 1440 fullpage (post-fix) | `factory/reports/browser-verification/continua-passB-multilingual/ar-1440-fullpage.png` |
| AR 720 fullpage (mobile RTL) | `factory/reports/browser-verification/continua-passB-multilingual/ar-720-fullpage.png` |
| AR 1440 contatti (RTL form) | `factory/reports/browser-verification/continua-passB-multilingual/ar-1440-contatti.png` |

Smoke walk · all 5 locales × 5 pages + 4 mandate-detail posts (45 routes) → 45/45 HTTP 200 (logged in `factory/reports/browser-verification/continua-passB-multilingual.md §3`).

---

## 8 · Issues found and fixes applied

| # | Finding | Severity | Fix | Time |
|---|---|---|---|---|
| 1 | LF-5-specific eyebrow surfaces not in CS-TYPE-05 RTL letter-spacing reset → Arabic uppercase tracking artifacts on 9 surfaces | STRONG | Extended reset rule in `_base.html` to 10 LF-5 surfaces; re-walk AR confirmed all `letter-spacing: normal` | 8 min |
| 2 | `runserver --noreload` did not pick up the `_base.html` edit on the live SQLite session | OBSERVATION (dev-env, not product) | `taskkill /F /PID 60232` + restart | 1 min |
| 3 | DB tier was hand-flipped to `published_live` for the walk (mirrors LF-5 IT rebuild §8.2 approach) | OPERATIONAL (transient) | `python manage.py sync_template_tiers` after walk; DB tier back to `draft` matching registry | 1 min |

No `[BLOCKING]` finding. Pre-existing `test_medical_and_restaurant_templates_have_booking_flag` failure is documented in LF-5 IT rebuild §8.4 as "out of scope" and is unrelated to Pass B.

---

## 9 · Server posture at landing

```
python manage.py runserver 127.0.0.1:8051 --noreload
```

Listening at **http://127.0.0.1:8051/**. The walk used `cs_review_fix`-equivalent staff session (`continua_passB / continuapassb2026`, is_staff=True, shared with the legitimate D-055 staff-preview path). DB and registry both at `tier: draft` post-walk.

URLs left open for human visual review:

```
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?preview=1            (IT)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=en&preview=1    (EN)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=fr&preview=1    (FR)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=es&preview=1    (ES)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=ar&preview=1    (AR · RTL)
```

Each URL also reaches `chi-siamo · custodia · mandati · contatti` and the 4 mandate-detail posts via the staff-preview-aware nav.

---

## 10 · What was NOT changed

To remove any ambiguity about scope:

- `apps/editor/*` — UNTOUCHED
- `apps/projects/*` — UNTOUCHED
- `apps/commerce/*` — UNTOUCHED
- `apps/catalog/views.py` and other selectors/services — UNTOUCHED
- `templates/live_templates/business/corporate-suite/_layouts/lf5/*.html` — UNTOUCHED (LF-5 layout preserved exactly)
- `templates/live_templates/business/corporate-suite/home.html` — UNTOUCHED (router by layout_family)
- `templates/live_templates/business/corporate-suite/_layouts/lf1/*.html` — UNTOUCHED
- DNA registry, imagery pool, imagery policy, seed command — UNTOUCHED
- No new archetype, no new template, no new migration
- No public flip (`tier=draft` preserved both in DB and registry)

The only chrome edit is the additive CS-TYPE-05 RTL reset extension in `_base.html` — it is RTL-scoped so it cannot affect any LTR locale or any other corporate-suite sibling.

---

## 11 · Distinctness verdict on live render across locales

Continua remains visibly distinct from Pragma · Fiscus · Solaria in every locale:

- **vs Pragma** (boardroom navy/emerald): different hero subject (object-led library vs people-led boardroom), different palette (pine+brass vs navy+emerald), different KPI/cycle treatment, different leadership demographics, different form gate. Distinct in EN/FR/ES/AR exactly as it was in IT.
- **vs Fiscus** (gray-blue/gold-blunotte fiscal): different hero subject (library vs tax desk), different mid-strip (governance-cycle vs fiscal-calendar), different cases shape (timeline vs list-row). Distinct in every locale.
- **vs Solaria** (warm-carbon coaching): different hero subject (object-led zero-people vs 1:1 conversation), different palette (pine+brass vs ocra/caramel), different leadership story (60s+40s+50s stewardship vs 30s coaching). Distinct in every locale.

The translation does not flatten the stewardship voice — the cross-locale register guides explicitly named in each file's docstring (Pictet/Stonehage for EN, Mirabaud/Edmond for FR, Banque Pictet España for ES, Asharq al-Awsat / HBR Arabia for AR) keep each locale on its own native institutional register without homogenising to "global English business."

---

## 12 · Verdict

**Continua Pass B Multilingual is GREEN.**

- 5 locales authored, voice anchor preserved verbatim-in-translation in every language
- LF-5 layout shape preserved exactly (no DOM change, no skin reshape)
- AR RTL parity working (Noto Kufi heading + Amiri body + logical-property layer + extended CS-TYPE-05 reset)
- 14 walk cells × 5 locales = 70/70 PASS
- 1 STRONG finding identified and fixed mid-walk (LF-5 eyebrow surfaces RTL letter-spacing)
- 0 BLOCKING findings, 0 OBSERVATION beyond the dev-env restart and the documented operational tier-flip
- Tier remains `draft` — public flip held for the user-handshake gate

**Continua is now ready for human visual review across IT · EN · FR · ES · AR with RTL parity. The next workstream is final release-decision (workflow D) gated on user authorization, per cluster R-SOL-8 and the brief's D-102 cadence.**

---

## 13 · Whether Continua is ready for final release-decision work

**YES** — at draft tier, with all five locales walked GREEN and zero BLOCKING findings, Continua is ready for the cluster's release-decision orchestrator (`design-orchestrator/prompts/release-decision-orchestrator.md`). The cascade documented to the line:

1. User reviews the 7 captures + 6 walk verdicts under `factory/reports/scorecard/continua-passB-multilingual/`.
2. User reviews the live render across the 5 URLs above.
3. On approval, the release-decision orchestrator runs the cluster scorecard with per-locale rows (mirrors the Solaria Pass C → Pass D pattern) and the gatekeeper signs `tier=draft → tier=published_live`.
4. Public catalog count moves 22 → 23; the `Continua` card surfaces under `/templates/business/`; the trust counter updates.
5. The `MEMORY.md` entry rolls up to a single line under "CURRENT baseline pointer" with the Pass B GREEN verdict, AR RTL working, and the 70/70 walk count.

This pass does **not** flip the tier. It opens the handshake.
